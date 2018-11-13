
'''
CFG.make_CFG__hashable_name__less

S = Ts1
Ts1 = Ts0 t
Ts0 = Ts1
Ts0 =

>>> from .the_py_terminal_set_ops import the_py_terminal_set_ops
>>> terminal_set_ops = the_py_terminal_set_ops
>>> terminal_set_name2terminal_set = lambda a:{a}
>>> make = lambda *args, **kwargs: CFG.make_CFG__hashable_name__less(
...     *args
...     , explain_ref_symbol_name=explain_ref_symbol_name
...     , terminal_set_ops=terminal_set_ops
...     , terminal_set_name2terminal_set=terminal_set_name2terminal_set
...     , **kwargs)
>>> __pairs = [('S', ['Ts1']), ('Ts1', ['Ts0', 't']), ('Ts0', ['Ts1']), ('Ts0', [])]
>>> explain_ref_symbol_name = lambda name: (name[0].isupper(), name)
>>> cfg = make(__pairs)
>>> __pairs = [('S', ['t'])]
>>> cfg = make(__pairs)
>>> cfg #doctest: +ELLIPSIS
CFG(production_idx2nonterminal_idx = [0], production_idx2alternative_tail_idx = [1], alternative_tail_idx2alternative_idx_maybe_pair = [(), (-1, 0)], num_nonterminals = 1, num_terminal_sets = 1, num_productions = 1, num_alternative_tails = 2, terminal_set_ops = PyTerminalSetOps(), terminal_set_idx2terminal_set = [{'t'}], terminal_set_idx2terminal_set_name = ['t'], nonterminal_idx2nonterminal_name = ['S'], production_idx2production_name = [('S', 0)], alternative_idx_maybe_pair2alternative_tail_idx = Mapping2Callable({(): 0, (-1, 0): 1}), terminal_set_name2terminal_set_idx = Mapping2Callable({'t': 0}), nonterminal_name2nonterminal_idx = Mapping2Callable({'S': 0}), production_name2production_idx = Mapping2Callable({('S', 0): 0}))

>>> cfg.calc.nonterminal_idx2inits_of_max_length(0)
(frozenset({()}),)
>>> cfg.calc.nonterminal_idx2inits_of_max_length(1)
(frozenset({(0,)}),)
>>> cfg.calc.nonterminal_idx2inits_of_max_length(2)
(frozenset({(0,)}),)
>>> cfg.calc.alternative_tail_idx2inits_of_max_length(2)
(frozenset({()}), frozenset({(0,)}))
>>> cfg.calc.nonterminal_idx2sorted_production_idc
((0,),)

'''

__all__ = '''
    CFG
    explain_ref_symbol_psidx
    nonterminal_idx2ref_symbol_psidx
    terminal_set_idx2ref_symbol_psidx
    '''.split()


from nn_ns.graph_tools.u2vtc.is_u2vtc_DAG import is_u2vtc_DAG
#from seed.abc.IReprHelper import IReprHelper
from seed.helper.repr_input import repr_helper_ex
#see below: from .calc_CFG_info.Calc_CFG_Info import Calc_CFG_Info
from seed.verify.common_verify import (
    is_int, is_UInt, is_pair, is_tuple, is_Sequence
    , is_strict_sorted_sequence, has_attrs
    )
from seed.verify.VerifyType import VerifyType__static
from seed.seq_tools.split_tuples import split_tuples
from seed.types.Mapping2Callable import Mapping2Callable
from collections import defaultdict

def make_alternative_tail_idx_related_triple(
    production_idx2ref_symbol_psidc
    ):

    production_idx2alternative_tail_idx = []
    idx2tail = []
    tail2idx = {}
    def put(tail):
        L = len(idx2tail)
        idx = tail2idx.setdefault(tail, L)
        if idx == L:
            idx2tail.append(tail)
        assert len(idx2tail) == len(tail2idx)
        return idx
    for ref_symbol_psidc in production_idx2ref_symbol_psidc:
        idx = put(())
        for ref_symbol_psidx in reversed(ref_symbol_psidc):
            idx = put((ref_symbol_psidx, idx))
        production_idx2alternative_tail_idx.append(idx)
    alternative_tail_idx2alternative_idx_maybe_pair = idx2tail
    alternative_idx_maybe_pair2alternative_tail_idx = Mapping2Callable(tail2idx)
    return (production_idx2alternative_tail_idx
            ,alternative_tail_idx2alternative_idx_maybe_pair
            ,alternative_idx_maybe_pair2alternative_tail_idx
            )

def make_half_bijection__hashable_name(names):
    idx2name = []
    name2idx = {}
    def put(name):
        L = len(idx2name)
        idx = name2idx.setdefault(name, L)
        if idx == L:
            idx2name.append(name)
        assert len(idx2name) == len(name2idx)
        return idx
    for name in names: put(name)
    return idx2name, Mapping2Callable(name2idx)




def terminal_set_idx2ref_symbol_psidx(terminal_set_idx):
    ref_symbol_psidx = -terminal_set_idx-1
    return ref_symbol_psidx
def nonterminal_idx2ref_symbol_psidx(nonterminal_idx):
    ref_symbol_psidx = nonterminal_idx
    return ref_symbol_psidx
def explain_ref_symbol_psidx(ref_symbol_psidx):
    # ref_symbol_psidx -> (is_nonterminal, ...idx)
    # vs explain_ref_symbol_name
    if ref_symbol_psidx < 0:
        terminal_set_idx = -ref_symbol_psidx-1
        return False, terminal_set_idx
    else:
        nonterminal_idx = ref_symbol_psidx
        return True, nonterminal_idx


#class CFG(IReprHelper):
class CFG:
    '''
see:
    "def - CFG.txt"


methods:
    explain_ref_symbol_psidx
    nonterminal_idx2ref_symbol_psidx
    terminal_set_idx2ref_symbol_psidx

    basic_make_CFG
    make_CFG__hashable_name
    make_CFG__hashable_name__less

    basic_make_CFG_kwargs
    make_CFG_kwargs__hashable_name
    make_CFG_kwargs__hashable_name__less

    verify

'''
    @staticmethod
    def explain_ref_symbol_psidx(ref_symbol_psidx):
        return explain_ref_symbol_psidx(ref_symbol_psidx)
    @staticmethod
    def nonterminal_idx2ref_symbol_psidx(nonterminal_idx):
        return nonterminal_idx2ref_symbol_psidx(nonterminal_idx)
    @staticmethod
    def terminal_set_idx2ref_symbol_psidx(terminal_set_idx):
        return terminal_set_idx2ref_symbol_psidx(terminal_set_idx)

    @classmethod
    def basic_make_CFG(cls
        ,__production_idx2pair
        ,*
        ,terminal_set_idx2terminal_set_name
        ,nonterminal_idx2nonterminal_name
        ,production_idx2production_name
        ,terminal_set_ops
        ,terminal_set_idx2terminal_set
        ):

        d = cls.basic_make_CFG_kwargs(
                __production_idx2pair
                ,terminal_set_idx2terminal_set_name \
                    = terminal_set_idx2terminal_set_name
                ,nonterminal_idx2nonterminal_name \
                    = nonterminal_idx2nonterminal_name
                ,production_idx2production_name \
                    = production_idx2production_name

                ,terminal_set_ops
                    = terminal_set_ops
                ,terminal_set_idx2terminal_set
                    = terminal_set_idx2terminal_set
                )
        return cls(**d)

    @classmethod
    def make_CFG__hashable_name__less(cls
        , __pairs, *
        ,terminal_set_ops
        ,terminal_set_name2terminal_set #callable
        ,explain_ref_symbol_name
        ):
        # pair = (nonterminal_name, [ref_symbol_name])
        d = cls.make_CFG_kwargs__hashable_name__less(
            __pairs
            , explain_ref_symbol_name=explain_ref_symbol_name
            ,terminal_set_ops=terminal_set_ops
            ,terminal_set_name2terminal_set
                =terminal_set_name2terminal_set
            )
        return cls(**d)
    @classmethod
    def make_CFG__hashable_name(cls
        ,__production_name2pair
        ,*
        ,terminal_set_names
        ,nonterminal_names
        ,production_names

        ,explain_ref_symbol_name
        ,terminal_set_ops
        ,terminal_set_name2terminal_set
        ):
        # pair = (nonterminal_name, [ref_symbol_name])

        d = cls.make_CFG_kwargs__hashable_name(
                __production_name2pair
                ,terminal_set_names = terminal_set_names
                ,nonterminal_names = nonterminal_names
                ,production_names = production_names
                ,explain_ref_symbol_name = explain_ref_symbol_name

                ,terminal_set_ops=terminal_set_ops
                ,terminal_set_name2terminal_set
                    =terminal_set_name2terminal_set
                )
        return cls(**d)





    ####################################

    @classmethod
    def make_CFG_kwargs__hashable_name__less(cls
        , __pairs, *
        ,terminal_set_ops
        ,terminal_set_name2terminal_set #callable
        ,explain_ref_symbol_name
        ):
        # pair = (nonterminal_name, [ref_symbol_name])
        nonterminal_name2count = defaultdict(int)
        __production_name2pair = {}
        for nonterminal_name, ref_symbol_names in __pairs:
            ref_symbol_names = tuple(ref_symbol_names)
            i = nonterminal_name2count[nonterminal_name]
            nonterminal_name2count[nonterminal_name] += 1

            production_name = (nonterminal_name, i)
            __production_name2pair[production_name] \
                = (nonterminal_name, ref_symbol_names)
        del __pairs, nonterminal_name2count



        def add_ref_symbol_name(ref_symbol_name):
            is_nonterminal, name = explain_ref_symbol_name(ref_symbol_name)
            if is_nonterminal:
                names = nonterminal_names
            else:
                names = terminal_set_names
            names.add(name)

        production_names = list(__production_name2pair)
        nonterminal_names = set()
        terminal_set_names = set()
        iter_pairs = __production_name2pair.values() # not items!!!
        for nonterminal_name, ref_symbol_names in iter_pairs:
            nonterminal_names.add(nonterminal_name)
            it = map(add_ref_symbol_name, ref_symbol_names)
            for _ in it: pass
        return cls.make_CFG_kwargs__hashable_name(
                __production_name2pair
                ,terminal_set_names = terminal_set_names
                ,nonterminal_names = nonterminal_names
                ,production_names = production_names
                ,explain_ref_symbol_name = explain_ref_symbol_name

                ,terminal_set_ops=terminal_set_ops
                ,terminal_set_name2terminal_set
                    =terminal_set_name2terminal_set
                )


    @classmethod
    def make_CFG_kwargs__hashable_name(cls
        ,__production_name2pair
        ,*
        ,terminal_set_names
        ,nonterminal_names
        ,production_names

        ,terminal_set_ops
        #callable
        ,terminal_set_name2terminal_set

        ,explain_ref_symbol_name
        ):
        # pair = (nonterminal_name, [ref_symbol_name])
        # explain_ref_symbol_name
        #   :: ref_symbol_name -> (False, terminal_set_name)|(True, nonterminal)
        assert callable(terminal_set_name2terminal_set)
        (terminal_set_idx2terminal_set_name
        ,terminal_set_name2terminal_set_idx
        ) = make_half_bijection__hashable_name(terminal_set_names)

        (nonterminal_idx2nonterminal_name
        ,nonterminal_name2nonterminal_idx
        ) = make_half_bijection__hashable_name(nonterminal_names)

        (production_idx2production_name
        ,production_name2production_idx
        ) = make_half_bijection__hashable_name(production_names)

        def ref_symbol_name2psidx(ref_symbol_name):
            is_nonterminal, name = explain_ref_symbol_name(ref_symbol_name)
            if is_nonterminal:
                name2idx = nonterminal_name2nonterminal_idx
                idx2psidx = nonterminal_idx2ref_symbol_psidx
            else:
                name2idx = terminal_set_name2terminal_set_idx
                idx2psidx = terminal_set_idx2ref_symbol_psidx
            return idx2psidx(name2idx(name))

        __production_idx2pair = [None]*len(__production_name2pair)
        for production_name, pair in __production_name2pair.items():
            nonterminal_name, ref_symbol_names = pair
            ref_symbol_psidc = \
                list(map(ref_symbol_name2psidx, ref_symbol_names))

            nonterminal_idx = \
                nonterminal_name2nonterminal_idx(nonterminal_name)
            production_idx = \
                production_name2production_idx(production_name)
            pair = nonterminal_idx, ref_symbol_psidc
            assert __production_idx2pair[production_idx] is None
            __production_idx2pair [production_idx] = pair

        terminal_set_idx2terminal_set = list(map(
            terminal_set_name2terminal_set
            , terminal_set_idx2terminal_set_name
            ))
        return cls.basic_make_CFG_kwargs(
            __production_idx2pair
            ,terminal_set_idx2terminal_set_name
                = terminal_set_idx2terminal_set_name
            ,nonterminal_idx2nonterminal_name
                = nonterminal_idx2nonterminal_name
            ,production_idx2production_name
                = production_idx2production_name

            ,terminal_set_ops
                = terminal_set_ops
            ,terminal_set_idx2terminal_set
                = terminal_set_idx2terminal_set

            ,terminal_set_name2terminal_set_idx
                = terminal_set_name2terminal_set_idx
            ,nonterminal_name2nonterminal_idx
                = nonterminal_name2nonterminal_idx
            ,production_name2production_idx
                = production_name2production_idx
            )

    @classmethod
    def basic_make_CFG_kwargs(cls
        ,__production_idx2pair
        ,*
        ,terminal_set_idx2terminal_set_name
        ,nonterminal_idx2nonterminal_name
        ,production_idx2production_name

        ,terminal_set_ops
        ,terminal_set_idx2terminal_set

        # callable
        ,terminal_set_name2terminal_set_idx
        ,nonterminal_name2nonterminal_idx
        ,production_name2production_idx
        ):
        # pair = (nonterminal_idx, [ref_symbol_psidx])

        num_nonterminals = len(nonterminal_idx2nonterminal_name)
        num_terminal_sets = len(terminal_set_idx2terminal_set_name)
        num_productions = len(__production_idx2pair)

        (production_idx2nonterminal_idx, production_idx2ref_symbol_psidc
            ) = split_tuples(2, __production_idx2pair)
        del __production_idx2pair


        (production_idx2alternative_tail_idx
        ,alternative_tail_idx2alternative_idx_maybe_pair
        ,alternative_idx_maybe_pair2alternative_tail_idx
        ) = make_alternative_tail_idx_related_triple(
                production_idx2ref_symbol_psidc)
        del production_idx2ref_symbol_psidc

        num_alternative_tails = len(alternative_tail_idx2alternative_idx_maybe_pair)



        d = dict(locals())
        del d['cls']
        return d












    all_CFG_attr_seq = '''
        production_idx2nonterminal_idx
        production_idx2alternative_tail_idx
        alternative_tail_idx2alternative_idx_maybe_pair

        num_nonterminals
        num_terminal_sets
        num_productions
        num_alternative_tails

        terminal_set_ops
        terminal_set_idx2terminal_set
        terminal_set_idx2terminal_set_name
        nonterminal_idx2nonterminal_name
        production_idx2production_name


        alternative_idx_maybe_pair2alternative_tail_idx
        terminal_set_name2terminal_set_idx
        nonterminal_name2nonterminal_idx
        production_name2production_idx
        '''.split()
    all_CFG_attr_seq = tuple(all_CFG_attr_seq)
        # for __repr__
    all_CFG_attr_set = frozenset(all_CFG_attr_seq)
        # for calc_CFG_info.Calc_CFG_Info
        #       cfg.calc.xxx
    assert 'calc' not in all_CFG_attr_set
    assert len(all_CFG_attr_seq) == len(all_CFG_attr_set)



    def __init__(self, *
        ,production_idx2nonterminal_idx
        ,production_idx2alternative_tail_idx
        ,alternative_tail_idx2alternative_idx_maybe_pair

        ,num_nonterminals
        ,num_terminal_sets
        ,num_productions
        ,num_alternative_tails

        ,terminal_set_ops
            # .is_empty(set)
            # .is_disjoint(this, that)
            # .contains(set, element)
            # .intersection(this, that)
            # .union(this, that)
            # parser.token2terminal
        ,terminal_set_idx2terminal_set
        ,terminal_set_idx2terminal_set_name
        ,nonterminal_idx2nonterminal_name
        ,production_idx2production_name


        ########## bijection
        ########## callable, not container
        ##########      can use Mapping2Callable
        ,alternative_idx_maybe_pair2alternative_tail_idx
        ,terminal_set_name2terminal_set_idx
        ,nonterminal_name2nonterminal_idx
        ,production_name2production_idx
        ):
        self.production_idx2nonterminal_idx \
            = production_idx2nonterminal_idx
        self.production_idx2alternative_tail_idx \
            = production_idx2alternative_tail_idx
        self.alternative_tail_idx2alternative_idx_maybe_pair \
            = alternative_tail_idx2alternative_idx_maybe_pair
        self.num_nonterminals \
            = num_nonterminals
        self.num_terminal_sets \
            = num_terminal_sets
        self.num_productions \
            = num_productions
        self.num_alternative_tails \
            = num_alternative_tails

        self.terminal_set_idx2terminal_set_name \
            = terminal_set_idx2terminal_set_name
        self.nonterminal_idx2nonterminal_name \
            = nonterminal_idx2nonterminal_name
        self.production_idx2production_name \
            = production_idx2production_name


        self.alternative_idx_maybe_pair2alternative_tail_idx \
            = alternative_idx_maybe_pair2alternative_tail_idx
        self.terminal_set_name2terminal_set_idx \
            = terminal_set_name2terminal_set_idx
        self.nonterminal_name2nonterminal_idx \
            = nonterminal_name2nonterminal_idx
        self.production_name2production_idx \
            = production_name2production_idx

        self.terminal_set_ops = terminal_set_ops
        self.terminal_set_idx2terminal_set = terminal_set_idx2terminal_set

        assert self.verify(AssertionError)
        from .calc_CFG_info.Calc_CFG_Info import Calc_CFG_Info
        assert type(self) is CFG
        assert isinstance(self, CFG)
        self.calc = Calc_CFG_Info(self)
    def __setattr__(self, attr, obj):
        if attr in __class__.all_CFG_attr_set or attr == 'calc':
            # assume 'calc' is the last attr to be init
            if hasattr(self, 'calc'):
                # @property all_CFG_attr_set
                raise AttributeError(attr)
            # inside __init__()
        super().__setattr__(attr, obj)

    def __repr__(self):
        all_CFG_attr_seq = __class__.all_CFG_attr_seq
        assert len(self.__dict__)-1 == len(all_CFG_attr_seq)
            # exclude 'calc'
        return repr_helper_ex(self, (), all_CFG_attr_seq, {}, ordered_attrs_only=True)

    #IReprHelper
    #def ___get_args_kwargs___(self): return (), dict(self.__dict__)

    def verify(self, __mkError=None):
        return VerifyCFG(self, __mkError)

class VerifyCFG(VerifyType__static):
    types = CFG
    def _iter_verify_object_(_, obj):
        # -> Iter (bool, err_msg_or_f)
        attr_nums = '''
            num_nonterminals
            num_terminal_sets
            num_productions
            num_alternative_tails
            '''.split()
        for attr in attr_nums:
            u = getattr(obj, attr)
            yield (is_UInt(u), lambda:'{} is not UInt: {!r}'.format(attr, u))

        num_nonterminals = obj.num_nonterminals
        num_terminal_sets = obj.num_terminal_sets
        num_productions = obj.num_productions
        num_alternative_tails = obj.num_alternative_tails



        def is_production_idx(u):
            return u < num_productions
        def is_production_idx_seq(ls):
            return is_Sequence.of(ls, is_production_idx)
        def is_nonterminal_idx(u):
            return u < num_nonterminals
        def is_alternative_tail_idx(u):
            return u < num_alternative_tails
        def is_ref_symbol_psidx(i):
            return -num_terminal_sets <= i < num_nonterminals
        def is_maybe_pair(x):
            return is_tuple(x) and len(x) in (2,0)
        def is_alternative_idx_maybe_pair(may_pair):
            if not may_pair: return True
            ref_symbol_psidx, alternative_tail_idx = pair = may_pair
            return (is_int(ref_symbol_psidx)
                and is_UInt(alternative_tail_idx)
                and is_alternative_tail_idx(alternative_tail_idx)
                and is_ref_symbol_psidx(ref_symbol_psidx)
                )
        def is_strict_sorted_uint_sequence(ls):
            return is_strict_sorted_sequence.of(ls, is_UInt)

        triples = \
            [('production_idx2nonterminal_idx', num_productions
                , is_UInt, is_nonterminal_idx)
            ,('production_idx2alternative_tail_idx', num_productions
                , is_UInt, is_alternative_tail_idx)
            ,('alternative_tail_idx2alternative_idx_maybe_pair'
                , num_alternative_tails
                , is_maybe_pair, is_alternative_idx_maybe_pair)
            #('nonterminal_idx2sorted_production_idc'
            #   , num_nonterminals
            #   , is_strict_sorted_uint_sequence, is_production_idx_seq)
            ]
        for attr, size, is_type, is_obj in triples:
            array = getattr(obj, attr)
            yield (is_Sequence(array)
                , '{} is not Sequence: {!r}'.format(attr, array)
                )
            yield (len(array) == size
                , 'len({}) != {}: {}'.format(attr, size, len(array))
                )

            for is_a in [is_type, is_obj]:
                yield (is_Sequence.of(array, is_a)
                    , lambda:'{} is not Sequence<{}>: {!r}'.format(
                        attr, is_a.__name__[3:], array)
                    )

        pairs = \
            [('terminal_set_idx2terminal_set_name', num_terminal_sets)
            ,('nonterminal_idx2nonterminal_name', num_nonterminals)
            ,('production_idx2production_name', num_productions)
            ,('terminal_set_idx2terminal_set', num_terminal_sets)
            ]
        for attr, size in pairs:
            array = getattr(obj, attr)
            yield (is_Sequence(array)
                , '{} is not Sequence: {!r}'.format(attr, array)
                )
            yield (len(array) == size
                , 'len({}) != {}: {}'.format(attr, size, len(array))
                )



        pairs = \
            [('alternative_idx_maybe_pair2alternative_tail_idx'
                ,'alternative_tail_idx2alternative_idx_maybe_pair')
            ,('terminal_set_name2terminal_set_idx'
                ,'terminal_set_idx2terminal_set_name')
            ,('nonterminal_name2nonterminal_idx'
                ,'nonterminal_idx2nonterminal_name')
            ,('production_name2production_idx'
                ,'production_idx2production_name')
            ]
        for callable_attr, sequence_attr in pairs:
            f = getattr(obj, callable_attr)
            c = getattr(obj, sequence_attr)
            yield (callable(f), lambda:'{} is not callable: {!r}'
                .format(callable_attr, f))
            for idx, elem in enumerate(c):
                back_idx = f(elem)
                yield (is_int(back_idx), lambda:'{}({!r}) is not int: {!r}'
                    .format(callable_attr, elem, back_idx))
                yield (back_idx == idx, lambda:'{}({!r}) == {} != {}'
                    .format(callable_attr, elem, back_idx, idx))



        '''
        ## more for nonterminal_idx2sorted_production_idc
        nonterminal_idx2sorted_production_idc = obj.nonterminal_idx2sorted_production_idc
        production_idx2nonterminal_idx = obj.production_idx2nonterminal_idx
        it = enumerate(nonterminal_idx2sorted_production_idc)
        for nonterminal_idx, sorted_production_idc in it:
            for production_idx in sorted_production_idc:
                _nonterminal_idx = production_idx2nonterminal_idx[production_idx]
                yield (nonterminal_idx == _nonterminal_idx, lambda:
                    '{pidx} in nonterminal_idx2sorted_production_idc[{nidx}]'
                    ', but production_idx2nonterminal_idx[{pidx}] != {nidx}'
                    .format(nidx=nonterminal_idx, pidx=production_idx)
                    )

        L = sum(map(len, nonterminal_idx2sorted_production_idc))
        yield (num_productions == L, lambda:
            'nonterminal_idx2sorted_production_idc miss some production_idc: {}'
            .format(set(range(num_productions))
                    - set(sum(nonterminal_idx2sorted_production_idc))
                    )
            )
        ## end of nonterminal_idx2sorted_production_idc
        '''


        attrs = '''
                is_empty
                is_disjoint
                contains
                intersection
                union
            '''.split()
        yield (has_attrs(obj.terminal_set_ops, attrs=attrs)
            , lambda: 'terminal_set_ops donot have enough methods: {}'
                .format(attrs)
            )

        # alternative_tail_idx form a DAG
        u2vtc = [may_pair[-1:] if may_pair else () for may_pair
                    in obj.alternative_tail_idx2alternative_idx_maybe_pair]
        yield (is_u2vtc_DAG(u2vtc, using_std_vertex=True)
            , lambda: 'alternative_tail_idx2alternative_idx_maybe_pair is not DAG'
            )
if __name__ == "__main__":
    from .CFG import CFG
        # nn_ns.CFG.CFG instead of __main__.CFG

    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


