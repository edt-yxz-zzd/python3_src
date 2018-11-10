
__all__ = r'''
    OP3
    OP2
    FilteredRefName
    OP2_FilteredRefName
    OP3_FilteredRefName

    Discard
    Unit
    UnitUnpack
    Tuple
    TupleWithAlias

    Production
    productions2basic_productions
    collect_lhs_defined_nonterminal_names
    collect_rhs_ref_symbol_names
    collect_filter_ex_names
    collect_filter_names
    remove_duplicated_productions
    collect_duplicated_actions
    '''.split()

from seed.types.namedtuple import namedtuple
from seed.helper.repr_input import repr_helper_ex
from seed.verify.common_verify import (
    is_Sequence, is_UInt, is_Mapping, is_Hashable)
from seed.verify.VerifyType import VerifyType
from .abc import ABC, abstractmethod, override, final

from collections.abc import Hashable
from collections import defaultdict
from enum import Enum
from itertools import chain
chains = chain.from_iterable

OP3 = Enum('OP3', 'OP_UNPACK OP_SELECT OP_DISCARD')
OP2 = bool # Enum('OP2', 'OP_SELECT OP_DISCARD')

class AbstractSyntaxDataTypeRelated(ABC):
    __slots__ = ()
    def __repr__(self):
        names = self.get_arg_names()
        args = self.get_args()
        return repr_helper_ex(self, (), zip(names, args), {})
        kwargs = self.__dict__
        return repr_helper(self, **kwargs)
    def __hash__(self):
        return hash((id(type(self)), self.get_args()))
    def __eq__(self, other):
        return (self is other
            or (type(self) is type(other)
                and self.get_args() == other.get_args()
                )
            )
    def get_args(self):
        return tuple(getattr(self, name) for name in self.get_arg_names())
    @classmethod
    def get_arg_names(cls):
        return cls.arg_names_in_str.split()
    @abstractmethod
    def arg_names_in_str():
        # class property
        raise NotImplementedError

class PartType(AbstractSyntaxDataTypeRelated):
    __slots__ = ()
    pass
class FilteredRefName(PartType):
    arg_names_in_str = '''
        filter_names
        ref_symbol_name
        '''
    def __init__(self, filter_names, ref_symbol_name):
        assert is_Sequence.of(filter_names, is_Hashable)
        assert is_Hashable(ref_symbol_name)
        filter_names = tuple(filter_names)
        self.filter_names = filter_names
        self.ref_symbol_name = ref_symbol_name
class OP2_FilteredRefName(PartType):
    arg_names_in_str = '''
        op2
        filtered_ref_name
        '''
    def __init__(self, op2, filtered_ref_name):
        assert isinstance(op2, OP2)
        assert isinstance(filtered_ref_name, FilteredRefName)
        self.op2 = op2
        self.filtered_ref_name = filtered_ref_name
class OP3_FilteredRefName(PartType):
    arg_names_in_str = '''
        op3
        filtered_ref_name
        '''
    def __init__(self, op3, filtered_ref_name):
        assert isinstance(op3, OP3)
        assert isinstance(filtered_ref_name, FilteredRefName)
        self.op3 = op3
        self.filtered_ref_name = filtered_ref_name

def is_nonterminal_name(nonterminal_name):
    return is_Hashable(nonterminal_name)


class ProductionBase(AbstractSyntaxDataTypeRelated, ABC):
    __slots__ = ()
    def __init__(self, filter_names, nonterminal_name):
        assert is_Sequence.of(filter_names, is_Hashable)
        assert is_nonterminal_name(nonterminal_name)
        filter_names = tuple(filter_names)

        self.filter_names = filter_names
        self.nonterminal_name = nonterminal_name


    def to_basic_production(self):
        # -> (nonterminal_name, [ref_symbol_name])
        # can be used as production_name
        #   self hashable ==>> user can remove duplicated productions
        #       if all reduction/filters are the same besides basic_production
        return (self.nonterminal_name
                ,tuple(self.iter_rhs_ref_symbol_names())
                )
    @abstractmethod
    def maybe_get_lhs_filter_ex_name(self):
        '-> ()|(filter_ex_name,)'
        raise NotImplementedError
    @abstractmethod
    def iter_rhs_ref_symbol_names(self):
        '-> Iter ref_symbol_name'
        raise NotImplementedError
    @abstractmethod
    def iter_rhs_filter_names(self):
        '-> Iter filter_name'
        raise NotImplementedError
    @abstractmethod
    def get_rhs_length(self):
        raise NotImplementedError
    @abstractmethod
    def __rhs_eval__(self, filter_name2func, child_lazy_values):
        # -> (value,) or (args, kwargs)
        raise NotImplementedError
    def eval(self
        ,filter_name2func
        ,filter_ex_name2func
        ,child_lazy_values
        ):
        if len(child_lazy_values) != self.get_rhs_length():
            Lch = len(child_lazy_values)
            Lrhs = self.get_rhs_length()
            raise TypeError(f'length mismatch: len(child_lazy_values)={Lch} != {Lrhs}=self.get_rhs_length()')
        result = type(self).__rhs_eval__(self, filter_name2func, child_lazy_values)
        assert type(result) is tuple and 1 <= len(result) <= 2
        #(value,) or (args, kwargs)

        may_filter_ex_name = self.maybe_get_lhs_filter_ex_name()
        if bool(may_filter_ex_name) is not bool(len(result)==2):
            raise TypeError('may_filter_ex_name and __rhs_eval__ result mismatch')
        if may_filter_ex_name:
            [filter_ex_name] = may_filter_ex_name
            args, kwargs = result
            value = filter_ex_name2func[filter_ex_name](args, kwargs)
                # not (*args, **kwargs)
        else:
            [value] = result
        filter_names = self.filter_names
        value = self.apply_filters(filter_name2func, filter_names, value)
        return value

    def apply_filters(self, filter_name2func, filter_names, value):
        for filter_name in reversed(filter_names):
            value = filter_name2func[filter_name](value)
        return value


class Discard(ProductionBase):
        # f$g$ -A : ...
        # return f(g(None))
    arg_names_in_str = '''
        filter_names
        nonterminal_name
        filtered_ref_names
        '''
    def __init__(self, filter_names, nonterminal_name, filtered_ref_names):
        assert is_Sequence.of_type(filtered_ref_names, FilteredRefName)
        super().__init__(filter_names, nonterminal_name)
        filtered_ref_names = tuple(filtered_ref_names)
        self.filtered_ref_names = filtered_ref_names
    @override
    def maybe_get_lhs_filter_ex_name(self):
        return ()
    @override
    def iter_rhs_ref_symbol_names(self):
        return (
                filtered_ref_name.ref_symbol_name
                for filtered_ref_name in self.filtered_ref_names)
    @override
    def iter_rhs_filter_names(self):
        return chains(
                filtered_ref_name.filter_names
                for filtered_ref_name in self.filtered_ref_names)
    @override
    def get_rhs_length(self):
        return len(self.filtered_ref_names)
    @override
    def __rhs_eval__(self, filter_name2func, child_lazy_values):
        # -> (value,) or (args, kwargs)
        return (None,)
class Unit(ProductionBase):
        # f$g$A = ... +B ...
        # return f(g(B.value))
        # NOTE: '='
    arg_names_in_str = '''
        filter_names
        nonterminal_name
        filtered_ref_names_left
        filtered_ref_name
        filtered_ref_names_right
        '''
    def __init__(self
        , filter_names
        , nonterminal_name
        , filtered_ref_names_left
        , filtered_ref_name
        , filtered_ref_names_right
        ):
        assert is_Sequence.of_type(filtered_ref_names_left, FilteredRefName)
        assert isinstance(filtered_ref_name, FilteredRefName)
        assert is_Sequence.of_type(filtered_ref_names_right, FilteredRefName)
        super().__init__(filter_names, nonterminal_name)
        filtered_ref_names_left = tuple(filtered_ref_names_left)
        filtered_ref_names_right = tuple(filtered_ref_names_right)

        self.filtered_ref_names_left = filtered_ref_names_left
        self.filtered_ref_name = filtered_ref_name
        self.filtered_ref_names_right = filtered_ref_names_right

    @override
    def maybe_get_lhs_filter_ex_name(self):
        return ()
    def iter_rhs_filtered_ref_names(self):
        yield from self.filtered_ref_names_left
        yield self.filtered_ref_name
        yield from self.filtered_ref_names_right
    @override
    def iter_rhs_ref_symbol_names(self):
        return (
            filtered_ref_name.ref_symbol_name
            for filtered_ref_name in self.iter_rhs_filtered_ref_names())
    @override
    def iter_rhs_filter_names(self):
        return chains(
            filtered_ref_name.filter_names
            for filtered_ref_name in self.iter_rhs_filtered_ref_names())

    @override
    def get_rhs_length(self):
        return (len(self.filtered_ref_names_left)
                + 1
                + len(self.filtered_ref_names_right)
                )
    @override
    def __rhs_eval__(self, filter_name2func, child_lazy_values):
        # -> (value,) or (args, kwargs)
        i = len(self.filtered_ref_names_left)
        value = child_lazy_values[i]()
        filter_names = self.filtered_ref_name.filter_names
        value = self.apply_filters(filter_name2func, filter_names, value)
        return (value,)
class UnitUnpack(ProductionBase):
        # f$g$A = -C +B *D -E
        # return f(g([B.value, *D.value]))
        # NOTE: '='
        # concrete syntax require at least one '*' to distinguish with Unit
    arg_names_in_str = '''
        filter_names
        nonterminal_name
        op3_filtered_ref_names
        '''
    def __init__(self, filter_names, nonterminal_name, op3_filtered_ref_names):
        assert is_Sequence.of_type(op3_filtered_ref_names, OP3_FilteredRefName)
        super().__init__(filter_names, nonterminal_name)
        op3_filtered_ref_names = tuple(op3_filtered_ref_names)
        self.op3_filtered_ref_names = op3_filtered_ref_names
    @override
    def maybe_get_lhs_filter_ex_name(self):
        return ()
    @override
    def iter_rhs_ref_symbol_names(self):
        return (
            op3_filtered_ref_name.filtered_ref_name.ref_symbol_name
            for op3_filtered_ref_name in self.op3_filtered_ref_names)
    @override
    def iter_rhs_filter_names(self):
        return chains(
            op3_filtered_ref_name.filtered_ref_name.filter_names
            for op3_filtered_ref_name in self.op3_filtered_ref_names)
    @override
    def get_rhs_length(self):
        return len(self.op3_filtered_ref_names)
    @override
    def __rhs_eval__(self, filter_name2func, child_lazy_values):
        # -> (value,) or (args, kwargs)
        #
        def _eval():
            filter_names = op3_filtered_ref_name.filtered_ref_name.filter_names
            value = child_lazy_value()
            value = self.apply_filters(filter_name2func, filter_names, value)
            return value

        args = []
        for op3_filtered_ref_name, child_lazy_value in zip(
            self.op3_filtered_ref_names, child_lazy_values
            ):
            op3 = op3_filtered_ref_name.op3
            if op3 == OP3.OP_DISCARD: pass
            elif op3 == OP3.OP_SELECT:
                value = _eval()
                args.append(value)
            elif op3 == OP3.OP_UNPACK:
                value = _eval()
                args.extend(value)
            else:
                raise logic-error
        value = args # list!!
        return (value,)
class Tuple(ProductionBase):
        # f$g$A : -C +B +D...
        # return f(g((B.value, D.value, ...)))
        # NOTE: g :: tuple -> obj
    arg_names_in_str = '''
        filter_names
        nonterminal_name
        op2_filtered_ref_names
        '''
    def __init__(self, filter_names, nonterminal_name, op2_filtered_ref_names):
        assert is_Sequence.of_type(op2_filtered_ref_names, OP2_FilteredRefName)
        super().__init__(filter_names, nonterminal_name)
        op2_filtered_ref_names = tuple(op2_filtered_ref_names)
        self.op2_filtered_ref_names = op2_filtered_ref_names

    @override
    def maybe_get_lhs_filter_ex_name(self):
        return ()
    @override
    def iter_rhs_ref_symbol_names(self):
        return (
            op2_filtered_ref_name.filtered_ref_name.ref_symbol_name
            for op2_filtered_ref_name in self.op2_filtered_ref_names)
    @override
    def iter_rhs_filter_names(self):
        return chains(
            op2_filtered_ref_name.filtered_ref_name.filter_names
            for op2_filtered_ref_name in self.op2_filtered_ref_names)
    @override
    def get_rhs_length(self):
        return len(self.op2_filtered_ref_names)
    @override
    def __rhs_eval__(self, filter_name2func, child_lazy_values):
        # -> (value,) or (args, kwargs)
        #
        def _eval():
            filter_names = op2_filtered_ref_name.filtered_ref_name.filter_names
            value = child_lazy_value()
            value = self.apply_filters(filter_name2func, filter_names, value)
            return value

        args = []
        for op2_filtered_ref_name, child_lazy_value in zip(
            self.op2_filtered_ref_names, child_lazy_values
            ):
            is_selected = op2_filtered_ref_name.op2
            if is_selected:
                value = _eval()
                args.append(value)
        value = tuple(args)
        return (value,)

class TupleWithAlias(ProductionBase):
        # f$g$h$$A : -C +~@B +d1@D +d2@D -@E
        # return f(g(h(args, kwargs))) # B d1 d2 E
        # NOTE: not: return f(g(h(*args, **kwargs)))??
        #   since unpack is dangerous
        #
        # idx <- [0..len(rhs)-1] # not the result!!
        # idx 1-to-[0..] alias_names
        #
    arg_names_in_str = '''
        filter_names
        filter_ex_name
        nonterminal_name
        op2_filtered_ref_names
        alias_name2idx
        '''
    def __init__(self
        , filter_names, filter_ex_name, nonterminal_name
        , op2_filtered_ref_names, alias_name2idx
        ):
        assert is_Hashable(filter_ex_name)
        assert is_Sequence.of_type(op2_filtered_ref_names, OP2_FilteredRefName)
        assert is_Mapping(alias_name2idx)
        assert all(map(is_UInt, alias_name2idx.values()))
        super().__init__(filter_names, nonterminal_name)

        alias_name2idx = dict(alias_name2idx)
        op2_filtered_ref_names = tuple(op2_filtered_ref_names)
        L = len(op2_filtered_ref_names)
        idx2aliass = [[] for _ in range(L)]
        for alias, idx in alias_name2idx.items():
            #allow point to discard idx
            if not 0 <= idx < L:
                raise ValueError('out of index: alias_name2idx')
            idx2aliass[idx].append(alias)
        idx2aliass = tuple(map(frozenset, idx2aliass))


        self.filter_ex_name = filter_ex_name
        self.op2_filtered_ref_names = op2_filtered_ref_names
        self.alias_name2idx = alias_name2idx
        self.__idx2aliass = idx2aliass # for hash
            # donot assume sortable
    def __hash__(self):
        # bug:hargs = (self.filter_ex_name
        #       ,self.op2_filtered_ref_names
        #       ,self.__idx2aliass
        #       )
        args = self.get_args()
        assert type(args[-1]) is dict
        hargs = args[:-1] + (self.__idx2aliass,)
        return hash((id(type(self)), hargs))

    @override
    def maybe_get_lhs_filter_ex_name(self):
        return (self.filter_ex_name,)
    @override
    def iter_rhs_ref_symbol_names(self):
        return (
            op2_filtered_ref_name.filtered_ref_name.ref_symbol_name
            for op2_filtered_ref_name in self.op2_filtered_ref_names)
    @override
    def iter_rhs_filter_names(self):
        return chains(
            op2_filtered_ref_name.filtered_ref_name.filter_names
            for op2_filtered_ref_name in self.op2_filtered_ref_names)
    @override
    def get_rhs_length(self):
        return len(self.op2_filtered_ref_names)
    @override
    def __rhs_eval__(self, filter_name2func, child_lazy_values):
        # -> (value,) or (args, kwargs)
        #
        def _eval():
            filter_names = op2_filtered_ref_name.filtered_ref_name.filter_names
            value = child_lazy_value()
            value = self.apply_filters(filter_name2func, filter_names, value)
            return value

        args = []
        all_args = []
        for op2_filtered_ref_name, child_lazy_value in zip(
            self.op2_filtered_ref_names, child_lazy_values
            ):
            is_selected = op2_filtered_ref_name.op2
            if is_selected:
                value = _eval()
                args.append(value)
            else:
                value = None
            all_args.append(value)
        args = tuple(args)
        kwargs = {alias: all_args[idx]
                for alias, idx in alias_name2idx.items()
                }
        return (args, kwargs)

Production = (Discard, Unit, UnitUnpack, Tuple, TupleWithAlias)


def remove_duplicated_productions(productions):
    # -> (idx2production, production2idx)
    # -> ([production], {production:idx})
    production2idx = {}
    for production in productions:
        idx = len(production2idx)
        production2idx.setdefault(production, idx)

    idx2production = [None]*len(production2idx)
    for production, idx in production2idx.items():
        idx2production[idx] = production
    return idx2production, production2idx

def collect_duplicated_actions(productions):
    # {basic_production: {production}} # len(value)>=2
    basic_production2productions = defaultdict(set)
    for production in productions:
        basic_production = production.to_basic_production()
        basic_production2productions[basic_production].add(production)
    bads = {basic_production: productions
            for basic_production, productions
                in basic_production2productions.items()
            if len(productions) > 1
            }
    return bads

def productions2basic_productions(productions):
    '[Production] -> [(nonterminal_name, [ref_symbol_name])]'
    pairs = [p.to_basic_production() for p in productions]
    return pairs
def collect_lhs_defined_nonterminal_names(productions):
    '[Production] -> Set nonterminal_name'
    return {production.nonterminal_name for production in productions}
def collect_rhs_ref_symbol_names(productions):
    '[Production] -> Set ref_symbol_name'
    return {ref_symbol_name
        for production in productions
        for ref_symbol_name in production.iter_rhs_ref_symbol_names()
        }

def collect_filter_ex_names(productions):
    '[Production] -> Set filter_ex_name'
    return {filter_ex_name
            for production in productions
            for filter_ex_name in production.maybe_get_lhs_filter_ex_name()
            }
def collect_filter_names(productions):
    '[Production] -> Set filter_name'
    return {filter_name
            for production in productions
            for filter_name in chain(
                production.filter_names
                ,production.iter_rhs_filter_names()
                )
            }


