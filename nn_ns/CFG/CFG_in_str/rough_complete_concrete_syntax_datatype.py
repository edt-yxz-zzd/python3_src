
'''
rough_complete_concrete_syntax_datatype
    vs abstract_syntax_datatype
    see: rough_complete_in_simplified

'''


from seed.iters.duplicate_elements import iter_duplicate_representative_elements
from seed.tiny import fst
from seed.types.namedtuple import namedtuple
from seed.helper.repr_input import repr_helper_ex
from seed.verify.common_verify import (
    is_Sequence, is_UInt, is_Mapping, is_Hashable, is_pair)
from seed.verify.VerifyType import VerifyType
from .abc import ABC, abstractmethod, override, final
from.abstract_syntax_datatype import OP3, OP2

from collections.abc import Hashable
from collections import defaultdict
from enum import Enum
from itertools import chain
chains = chain.from_iterable


class RoughCompleteSyntaxDataTypeRelated(ABC):
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

class PartType(RoughCompleteSyntaxDataTypeRelated):
    __slots__ = ()
    pass
class FilteredRefName(PartType):
    arg_names_in_str = '''
        filter_names
        ref_name
        '''
    def __init__(self, filter_names, ref_name):
        assert is_Sequence.of(filter_names, is_Hashable)
        assert isinstance(ref_name, RefName)
        filter_names = tuple(filter_names)
        self.filter_names = filter_names
        self.ref_name = ref_name
#class FilterName:
#class DecoratorName:
class Suffix_OP2_Decorated_FilteredRefName(PartType):
    arg_names_in_str = '''
        may_op2
        may_decorator
        filtered_ref_name
        '''
    def __init__(self, may_op2, may_decorator, filtered_ref_name):
        assert may_op2 is None or isinstance(may_op2, OP2)
        assert may_decorator is None or (isinstance(may_decorator, str) and may_decorator.endswith('@') and may_decorator != '~@')
        assert isinstance(filtered_ref_name, FilteredRefName)
        self.may_op2 = may_op2
        self.may_decorator = may_decorator
        self.filtered_ref_name = filtered_ref_name
class Suffix_OP3_FilteredRefName(PartType):
    arg_names_in_str = '''
        may_op3
        filtered_ref_name
        '''
    def __init__(self, may_op3, filtered_ref_name):
        assert may_op3 is None or isinstance(may_op3, OP3)
        assert isinstance(filtered_ref_name, FilteredRefName)
        self.may_op3 = may_op3
        self.filtered_ref_name = filtered_ref_name

def is_nonterminal_name(nonterminal_name):
    return is_Hashable(nonterminal_name)

class BasicRefName:pass
class KW_BasicRefName(BasicRefName):
    def __init__(self, kw_name):
        assert kw_name in ['@any@', '@none@']
class CallName(BasicRefName):
    def __init__(self, name_ex, <>, ()):
        assert name_ex
        assert (name_ex[1:] if name_ex[0]=='!' else name_ex).isidentifier()
        name_ex
class RefName:
    def __init__(self, basic_ref_name, {..}*):#, '?*+'):
class DefName:
    def __init__(self, name, <>, ()):



class ProductionBase(RoughCompleteSyntaxDataTypeRelated, ABC):
    __slots__ = ()
    def __init__(self, filter_names, def_name):
        assert is_Sequence.of(filter_names, is_Hashable)
        assert isinstance(def_name, DefName)
        filter_names = tuple(filter_names)

        self.filter_names = filter_names
        self.def_name = def_name


    def to_basic_production(self):
        # -> (def_name, [ref_name])
        # can be used as production_name
        #   self hashable ==>> user can remove duplicated productions
        #       if all reduction/filters are the same besides basic_production
        return (self.def_name
                ,tuple(self.iter_rhs_ref_names())
                )
    @abstractmethod
    def maybe_get_lhs_filter_ex_name(self):
        '-> ()|(filter_ex_name,)'
        raise NotImplementedError
    @abstractmethod
    def iter_rhs_ref_names(self):
        '-> Iter ref_name'
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

Sand = bool
    # False - @no_noise@
    # True - @noise@
def is_sand(s):
    return type(s) is bool
def is_may_sand(s):
    return s is None or is_sand(s)

class UnitMayUnpack(ProductionBase):
    arg_names_in_str = '''
        filter_names
        def_name
        may_sand_suffix_op3_filtered_ref_name_pairss
        '''
    def __init__(self, filter_names, def_name, may_sand_suffix_op3_filtered_ref_name_pairss):
        assert is_Sequence.of(filter_names, is_Hashable)
        assert isinstance(def_name, DefName)
        assert is_Sequence.of(may_sand_suffix_op3_filtered_ref_name_pairss, is_Sequence)
        assert all(is_pair(pair)
            and is_may_sand(pair[0])
            and isinstance(pair[1], Suffix_OP3_FilteredRefName)
            for pairs in may_sand_suffix_op3_filtered_ref_name_pairss
            for pair in pairs
            )
        if not all(not pairs or pairs[0][0] is None
            for pairs in may_sand_suffix_op3_filtered_ref_name_pairss
            ):
            raise ValueError('first may_sand should be None; i.e. sand should not be first item in alternative')
        super().__init__(filter_names, def_name)
        pairss = self.may_sand_suffix_op3_filtered_ref_name_pairss = tuple(map(
            tuple, may_sand_suffix_op3_filtered_ref_name_pairss))

        self.has_op_unpacks = tuple(map(has_op_unpack, pairss))
        for pairs in pairss:
            check_may_sand_suffix_op3_filtered_ref_name_pairs(pairs)

def check_may_sand_suffix_op3_filtered_ref_name_pairs(
    may_sand_suffix_op3_filtered_ref_name_pairs
    ):
    d = count_may_op3(may_sand_suffix_op3_filtered_ref_name_pairs)
    if d[OP3.OP_UNPACK]:
        # unit unpack
        if d[None]:
            raise ValueError('unit unpack: cannot omit op3 [-+*]')
    else:
        # unit
        if d[OP3.OP_DISCARD]:
            raise ValueError('unit (not unpack): "-" shouldnot occur')
        if d[OP3.OP_SELECT] > 1:
            raise ValueError('unit (not unpack): "+" shouldnot occur more than once')

        L = len(may_sand_suffix_op3_filtered_ref_name_pairs)
        assert d[OP3.OP_SELECT] + d[None] == L
        if L != 1 and d[OP3.OP_SELECT] != 1:
            raise ValueError('unit (not unpack): too few "+"')

        assert (d[OP3.OP_DISCARD] == 0
            and (L == 1 or d[OP3.OP_SELECT] == 1)
            )

def count_may_op3(may_sand_suffix_op3_filtered_ref_name_pairs):
    d = dict.fromkeys(
            [None, OP3.OP_UNPACK, OP3.OP_SELECT, OP3.OP_DISCARD], 0)
    for may_sand, suffix_op3_filtered_ref_name in may_sand_suffix_op3_filtered_ref_name_pairs:
        may_op3 = suffix_op3_filtered_ref_name.may_op3
        d[may_op3] += 1
    return d

def has_op_unpack(may_sand_suffix_op3_filtered_ref_name_pairs):
    return any(suffix_op3_filtered_ref_name.may_op3 == OP3.OP_UNPACK
        for may_sand, suffix_op3_filtered_ref_name
        in may_sand_suffix_op3_filtered_ref_name_pairs
        )

class TupleMayWithAlias(ProductionBase):
    arg_names_in_str = '''
        filter_names
        has_lhs_op_discard
        may_filter_ex_name
        def_name
        may_sand_suffix_op2_decorated_filtered_ref_name_pairss
        '''
    def __init__(self
        , filter_names, has_lhs_op_discard, may_filter_ex_name, def_name
        , may_sand_suffix_op2_decorated_filtered_ref_name_pairss
        ):
        assert is_Sequence.of(filter_names, is_Hashable)
        assert type(has_lhs_op_discard) is bool
        if not (is_Sequence(may_filter_ex_name) and len(may_filter_ex_name) < 2): raise TypeError
        assert isinstance(def_name, DefName)
        assert is_Sequence.of(may_sand_suffix_op2_decorated_filtered_ref_name_pairss, is_Sequence)
        assert all(is_pair(pair)
            and is_may_sand(pair[0])
            and isinstance(pair[1], Suffix_OP2_Decorated_FilteredRefName)
            for pairs in may_sand_suffix_op2_decorated_filtered_ref_name_pairss
            for pair in pairs
            )
        if not all(not pairs or pairs[0][0] is None
            for pairs in may_sand_suffix_op2_decorated_filtered_ref_name_pairss
            ):
            raise ValueError('first may_sand should be None; i.e. sand should not be first item in alternative')


        super().__init__(filter_names, def_name)
        self.has_lhs_op_discard = bool(has_lhs_op_discard)
        self.may_filter_ex_name = tuple(may_filter_ex_name)
        pairss = self.may_sand_suffix_op2_decorated_filtered_ref_name_pairss \
            = tuple(map(tuple
                , may_sand_suffix_op2_decorated_filtered_ref_name_pairss))

        for pairs in pairss:
            check_may_sand_suffix_op2_decorated_filtered_ref_name_pairs(pairs)
        self.alias2idx_seq = tuple(map(mk_alias2idx_from_may_sand_suffix_op2_decorated_filtered_ref_name_pairs, pairss))

def count_may_op2(
    may_sand_suffix_op2_decorated_filtered_ref_name_pairs
    ):
    OP_DISCARD = False
    OP_SELECT = True
    d = dict.fromkeys([None, OP_DISCARD, OP_SELECT], 0)
    for may_sand, suffix_op2_decorated_filtered_ref_name in \
        may_sand_suffix_op2_decorated_filtered_ref_name_pairs:
        may_op2 = suffix_op2_decorated_filtered_ref_name.may_op2
        d[may_op2] += 1
    return d

def check_may_sand_suffix_op2_decorated_filtered_ref_name_pairs(
    may_sand_suffix_op2_decorated_filtered_ref_name_pairs
    ):
    d = count_may_op2(may_sand_suffix_op2_decorated_filtered_ref_name_pairs)
    keys = {key for key, count in d.items() if count}
    if len(keys) > 2:
        raise ValueError('tuple production: three values of may_op2 [-+]? cannot occur at same time')

def mk_alias2idx_from_may_sand_suffix_op2_decorated_filtered_ref_name_pairs(
    may_sand_suffix_op2_decorated_filtered_ref_name_pairs
    ):
    ls = []
    for i, (may_sand, suffix_op2_decorated_filtered_ref_name) in \
        enumerate(may_sand_suffix_op2_decorated_filtered_ref_name_pairs):
        may_decorator = suffix_op2_decorated_filtered_ref_name.may_decorator
        if may_decorator is not None:
            decorator = may_decorator
            assert decorator
            assert decorator[-1:] == '@'
            assert decorator != '~@'
            assert decorator != '@'
            alias = decorator[:-1]
            ls.append((alias, i))
    d = dict(ls)
    if len(d) < len(ls):
        [*names] = iter_duplicate_representative_elements(map(fst, ls))
        raise ValueError(f'alias duplicated: {names}')
    return d



