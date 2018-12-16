
'''

see:
    "planar/algo - is fake_embedding relax_planar.txt"/ugraph_fake_embedding
    nn_ns.CFG.CFG
        using class style like nn_ns.CFG.CFG

ugraph_fake_embedding:
    # ugraph may be not connected graph
    # ugraph may has no edge
    # allow self_loop and multiedge
    hedge2fake_clockwise_next_hedge_around_vertex
        not self reflect
        hedge2fake_clockwise_next_hedge_around_vertex[hedge] != hedge

    #### may be generated ###
    hedge2fake_clockwise_prev_hedge_around_vertex
    hedge2fake_clockwise_next_hedge_around_fface
    hedge2fake_clockwise_prev_hedge_around_fface
        # hedge2fake_clockwise_next_hedge_around_fface[hedge] = hedge2fake_clockwise_prev_hedge_around_vertex[hedge2another_hedge[hedge]]
        # hedge2fake_clockwise_prev_hedge_around_fface[hedge] = hedge2another_hedge[hedge2fake_clockwise_next_hedge_around_vertex[hedge]]
        # ugraph ==>> hedge outgo
        # fface -> hedges which form a clockwise cycle
    fface2degree
        # >= 1
        # donot consider isolated vertex
        # diff connected components donot share same external ffaces
    hedge2fake_clockwise_fface
    fface2arbitrary_hedge





example:
    >>> _mk = UGraphFakeEmbedding.make_UGraphFakeEmbedding__simplest
    >>> mk = lambda hedge2fake_clockwise_next_hedge_around_vertex, hedge2another_hedge: _mk(hedge2fake_clockwise_next_hedge_around_vertex=hedge2fake_clockwise_next_hedge_around_vertex, hedge2another_hedge=hedge2another_hedge)

    # edgeless
    >>> edgeless_graph = mk([], [])

    # a loop edge
    >>> single_loop_graph = mk([1,0], [1,0])

    # a non-loop edge
    >>> single_nonloop_graph = mk([0,1], [1,0])

    # 2 parallel non-loop edges
    >>> two_parallel_nonloops_graph = mk([2,3,0,1], [1,0,3,2])

    # 2 parallel loop edges
    >>> two_parallel_loops_graph = mk([2,0,3,1], [1,0,3,2])

    # 2 non-parallel loop edges # non-planar
    >>> two_nonparallel_loops_graph = mk([2,3,1,0], [1,0,3,2])

    >>> edgeless_graph
    UGraphFakeEmbedding(num_hedges = 0, num_ffaces = 0, hedge2fake_clockwise_next_hedge_around_vertex = [], hedge2fake_clockwise_prev_hedge_around_vertex = (), hedge2fake_clockwise_next_hedge_around_fface = (), hedge2fake_clockwise_prev_hedge_around_fface = (), fface2degree = (), hedge2fake_clockwise_fface = (), fface2arbitrary_hedge = ())
    >>> single_loop_graph
    UGraphFakeEmbedding(num_hedges = 2, num_ffaces = 2, hedge2fake_clockwise_next_hedge_around_vertex = [1, 0], hedge2fake_clockwise_prev_hedge_around_vertex = (1, 0), hedge2fake_clockwise_next_hedge_around_fface = (0, 1), hedge2fake_clockwise_prev_hedge_around_fface = (0, 1), fface2degree = (1, 1), hedge2fake_clockwise_fface = (0, 1), fface2arbitrary_hedge = (0, 1))
    >>> single_nonloop_graph
    UGraphFakeEmbedding(num_hedges = 2, num_ffaces = 1, hedge2fake_clockwise_next_hedge_around_vertex = [0, 1], hedge2fake_clockwise_prev_hedge_around_vertex = (0, 1), hedge2fake_clockwise_next_hedge_around_fface = (1, 0), hedge2fake_clockwise_prev_hedge_around_fface = (1, 0), fface2degree = (2,), hedge2fake_clockwise_fface = (0, 0), fface2arbitrary_hedge = (0,))
    >>> two_parallel_nonloops_graph
    UGraphFakeEmbedding(num_hedges = 4, num_ffaces = 2, hedge2fake_clockwise_next_hedge_around_vertex = [2, 3, 0, 1], hedge2fake_clockwise_prev_hedge_around_vertex = (2, 3, 0, 1), hedge2fake_clockwise_next_hedge_around_fface = (3, 2, 1, 0), hedge2fake_clockwise_prev_hedge_around_fface = (3, 2, 1, 0), fface2degree = (2, 2), hedge2fake_clockwise_fface = (0, 1, 1, 0), fface2arbitrary_hedge = (0, 1))
    >>> two_parallel_loops_graph
    UGraphFakeEmbedding(num_hedges = 4, num_ffaces = 3, hedge2fake_clockwise_next_hedge_around_vertex = [2, 0, 3, 1], hedge2fake_clockwise_prev_hedge_around_vertex = (1, 3, 0, 2), hedge2fake_clockwise_next_hedge_around_fface = (3, 1, 2, 0), hedge2fake_clockwise_prev_hedge_around_fface = (3, 1, 2, 0), fface2degree = (2, 1, 1), hedge2fake_clockwise_fface = (0, 1, 2, 0), fface2arbitrary_hedge = (0, 1, 2))
    >>> two_nonparallel_loops_graph
    UGraphFakeEmbedding(num_hedges = 4, num_ffaces = 1, hedge2fake_clockwise_next_hedge_around_vertex = [2, 3, 1, 0], hedge2fake_clockwise_prev_hedge_around_vertex = (3, 2, 0, 1), hedge2fake_clockwise_next_hedge_around_fface = (2, 3, 1, 0), hedge2fake_clockwise_prev_hedge_around_fface = (3, 2, 0, 1), fface2degree = (4,), hedge2fake_clockwise_fface = (0, 0, 0, 0), fface2arbitrary_hedge = (0,))







    >>> edgeless_graph.calc.is_relax_planar_embedding
    True
    >>> single_loop_graph.calc.is_relax_planar_embedding
    True
    >>> single_nonloop_graph.calc.is_relax_planar_embedding
    True
    >>> two_parallel_nonloops_graph.calc.is_relax_planar_embedding
    True
    >>> two_parallel_loops_graph.calc.is_relax_planar_embedding
    True
    >>> two_nonparallel_loops_graph.calc.is_relax_planar_embedding
    False
'''











__all__ = '''
    UGraphFakeEmbedding
    VerifyUGraphFakeEmbedding
    '''.split()
'''
    iter_cycle_from
    inverse_uint_bijection
    make_hedge2fake_clockwise_prev_hedge_around_fface
    make_hedge2fake_clockwise_fface_ex
    make_hedge2fake_clockwise_fface
    make_fface2degree
    make_hedge2another_hedge
    is_uint_injection
    is_uint_surjection
    is_uint_bijection
'''

from .iter_cycle_from import iter_cycle_from
from .inverse_uint_bijection import inverse_uint_bijection
from .is_uint_bijection import (is_uint_injection, is_uint_bijection)
from .makes_for_UGraphFakeEmbedding import (
    make_hedge2fake_clockwise_prev_hedge_around_fface
    ,make_hedge2fake_clockwise_fface_ex
    ,make_hedge2fake_clockwise_fface
    ,make_fface2degree
    ,make_hedge2another_hedge
    )

from seed.helper.repr_input import repr_helper_ex
from seed.verify.common_verify import (
    is_UInt, is_Sequence
    #is_int, is_UInt, is_pair, is_tuple, is_Sequence
    #, is_strict_sorted_sequence, has_attrs
    )
from seed.verify.VerifyType import VerifyType__static


class UGraphFakeEmbedding:
    '''

methods:
    make_UGraphFakeEmbedding__simplest
    make_UGraphFakeEmbedding__simpler
    verify_ugraph_fake_embedding
    verify
    hedge2iter_fake_clockwise_hedges_around_vertex
    hedge2iter_fake_clockwise_hedges_around_fface
'''
    all_UGraphFakeEmbedding_attr_seq = '''
        num_hedges
        num_ffaces
        hedge2fake_clockwise_next_hedge_around_vertex
        hedge2fake_clockwise_prev_hedge_around_vertex
        hedge2fake_clockwise_next_hedge_around_fface
        hedge2fake_clockwise_prev_hedge_around_fface
        fface2degree
        hedge2fake_clockwise_fface
        fface2arbitrary_hedge
        '''.split()
    all_UGraphFakeEmbedding_attr_set = frozenset(all_UGraphFakeEmbedding_attr_seq)

    @classmethod
    def make_UGraphFakeEmbedding__simplest(cls, *
        ,hedge2fake_clockwise_next_hedge_around_vertex
        ,hedge2another_hedge
        ,fface2arbitrary_hedge = None
        ):
        hedge2fake_clockwise_prev_hedge_around_fface = \
            make_hedge2fake_clockwise_prev_hedge_around_fface(
                hedge2fake_clockwise_next_hedge_around_vertex
                    = hedge2fake_clockwise_next_hedge_around_vertex
                ,hedge2another_hedge
                    = hedge2another_hedge
                )
        return cls.make_UGraphFakeEmbedding__simpler(
            hedge2fake_clockwise_next_hedge_around_vertex
                = hedge2fake_clockwise_next_hedge_around_vertex
            ,hedge2fake_clockwise_prev_hedge_around_fface
                = hedge2fake_clockwise_prev_hedge_around_fface
            ,fface2arbitrary_hedge = fface2arbitrary_hedge
            )
    @classmethod
    def make_UGraphFakeEmbedding__simpler(cls, *
        ,hedge2fake_clockwise_next_hedge_around_vertex
        ,hedge2fake_clockwise_prev_hedge_around_fface
        ,fface2arbitrary_hedge = None
        ):
        hedge2fake_clockwise_prev_hedge_around_vertex = \
            inverse_uint_bijection(
                hedge2fake_clockwise_next_hedge_around_vertex)

        hedge2fake_clockwise_next_hedge_around_fface = \
            inverse_uint_bijection(
                hedge2fake_clockwise_prev_hedge_around_fface
                )

        if fface2arbitrary_hedge is None:
            (hedge2fake_clockwise_fface, fface2arbitrary_hedge
            ) = make_hedge2fake_clockwise_fface_ex(
                hedge2fake_clockwise_next_hedge_around_fface
                    = hedge2fake_clockwise_next_hedge_around_fface
                )
        else:
            (hedge2fake_clockwise_fface
            ) = make_hedge2fake_clockwise_fface(
                hedge2fake_clockwise_next_hedge_around_fface
                    = hedge2fake_clockwise_next_hedge_around_fface
                ,fface2arbitrary_hedge
                    = fface2arbitrary_hedge
                )

        fface2degree = make_fface2degree(
            hedge2fake_clockwise_next_hedge_around_fface
                = hedge2fake_clockwise_next_hedge_around_fface
            ,fface2arbitrary_hedge
                = fface2arbitrary_hedge
            )

        num_hedges = len(hedge2fake_clockwise_next_hedge_around_vertex)
        num_ffaces = len(fface2arbitrary_hedge)
        return __class__(
            num_hedges = num_hedges
            ,num_ffaces = num_ffaces
            ,hedge2fake_clockwise_next_hedge_around_vertex
                = hedge2fake_clockwise_next_hedge_around_vertex
            ,hedge2fake_clockwise_prev_hedge_around_vertex
                = hedge2fake_clockwise_prev_hedge_around_vertex
            ,hedge2fake_clockwise_next_hedge_around_fface
                = hedge2fake_clockwise_next_hedge_around_fface
            ,hedge2fake_clockwise_prev_hedge_around_fface
                = hedge2fake_clockwise_prev_hedge_around_fface
            ,fface2degree = fface2degree
            ,hedge2fake_clockwise_fface = hedge2fake_clockwise_fface
            ,fface2arbitrary_hedge = fface2arbitrary_hedge
            )

    def __init__(self, *
        ,num_hedges
        ,num_ffaces
        ,hedge2fake_clockwise_next_hedge_around_vertex
        ,hedge2fake_clockwise_prev_hedge_around_vertex
        ,hedge2fake_clockwise_next_hedge_around_fface
        ,hedge2fake_clockwise_prev_hedge_around_fface
        ,fface2degree
        ,hedge2fake_clockwise_fface
        ,fface2arbitrary_hedge
        ):
        self.num_hedges = num_hedges
        self.num_ffaces = num_ffaces
        self.hedge2fake_clockwise_next_hedge_around_vertex \
            = hedge2fake_clockwise_next_hedge_around_vertex
        self.hedge2fake_clockwise_prev_hedge_around_vertex \
            = hedge2fake_clockwise_prev_hedge_around_vertex
        self.hedge2fake_clockwise_next_hedge_around_fface \
            = hedge2fake_clockwise_next_hedge_around_fface
        self.hedge2fake_clockwise_prev_hedge_around_fface \
            = hedge2fake_clockwise_prev_hedge_around_fface
        self.fface2degree = fface2degree
        self.hedge2fake_clockwise_fface = hedge2fake_clockwise_fface
        self.fface2arbitrary_hedge = fface2arbitrary_hedge

        assert self.verify_ugraph_fake_embedding(AssertionError)


        from .calc_UGraphFakeEmbedding_info.Calc_UGraphFakeEmbedding_Info import Calc_UGraphFakeEmbedding_Info
        assert isinstance(self, UGraphFakeEmbedding)
        self.calc = Calc_UGraphFakeEmbedding_Info(self) # .is_fake_embedding_planar

    def verify_ugraph_fake_embedding(self, __mkError=None):
        return VerifyUGraphFakeEmbedding(self, __mkError)

    def verify(self, __mkError=None):
        return self.verify_ugraph_fake_embedding()

    def __setattr__(self, attr, obj):
        if attr in __class__.all_UGraphFakeEmbedding_attr_set or attr == 'calc':
            if hasattr(self, attr):
                # @property all_UGraphFakeEmbedding_attr_set
                raise AttributeError(attr)
            # inside __init__()
        super().__setattr__(attr, obj)

    def __repr__(self):
        all_UGraphFakeEmbedding_attr_seq = __class__.all_UGraphFakeEmbedding_attr_seq
        assert len(self.__dict__)-1 == len(all_UGraphFakeEmbedding_attr_seq)
            # exclude 'calc'
        return repr_helper_ex(self, (), all_UGraphFakeEmbedding_attr_seq, {}, ordered_attrs_only=True)


    def hedge2iter_fake_clockwise_hedges_around_vertex(self, hedge):
        return iter_cycle_from(self.hedge2fake_clockwise_next_hedge_around_vertex, hedge)
    def hedge2iter_fake_clockwise_hedges_around_fface(self, hedge):
        return iter_cycle_from(self.hedge2fake_clockwise_next_hedge_around_fface, hedge)
    def hedge2another_hedge(self, hedge):
        return self.hedge2fake_clockwise_next_hedge_around_vertex[
                self.hedge2fake_clockwise_next_hedge_around_fface[hedge]]


class VerifyUGraphFakeEmbedding(VerifyType__static):
    types = UGraphFakeEmbedding
    def _iter_verify_object_(_, obj):
        # -> Iter (bool, err_msg_or_f)
        def is_uint_seq(obj):
            return is_Sequence.of(obj, is_UInt)
        attrs = UGraphFakeEmbedding.all_UGraphFakeEmbedding_attr_seq
        for attr in attrs:
            value = getattr(obj, attr)
            if attr.startswith('num_'):
                yield (is_UInt(value)
                    , lambda:f'{attr} is not UInt: {value!r}')
            else:
                yield (is_uint_seq(value)
                    , lambda:f'{attr} is not UInt sequence: {value!r}')

        num_hedges = obj.num_hedges
        num_ffaces = obj.num_ffaces
        #verify len of hedge2...
        #verify len of fface2...
        for attr in attrs:
            value = getattr(obj, attr)
            if attr.startswith('fface2'):
                len_value = len(value)
                yield (len_value == num_ffaces
                    , lambda: f'len({attr}) != num_ffaces: {len_value} != {num_ffaces}'
                    )
            elif attr.startswith('hedge2'):
                len_value = len(value)
                yield (len_value == num_hedges
                    , lambda: f'len({attr}) != num_hedges: {len_value} != {num_hedges}'
                    )
            else:
                pass



        pairs = [('hedge2fake_clockwise_next_hedge_around_vertex'
                    ,'hedge2fake_clockwise_prev_hedge_around_vertex'
                    )
                ,('hedge2fake_clockwise_next_hedge_around_fface'
                    ,'hedge2fake_clockwise_prev_hedge_around_fface'
                    )
                ]
        for forward_mapping_attr, backward_mapping_attr in pairs:
            forward_mapping = getattr(obj, forward_mapping_attr)
            backward_mapping = getattr(obj, backward_mapping_attr)
            yield (is_uint_bijection(forward_mapping, backward_mapping)
                , lambda: '({forward_mapping_attr},{backward_mapping_attr}) is not bijection: ({forward_mapping!r}, {backward_mapping!r})'
                )


        hedge2fake_clockwise_next_hedge_around_vertex =\
            obj.hedge2fake_clockwise_next_hedge_around_vertex
        hedge2fake_clockwise_prev_hedge_around_vertex =\
            obj.hedge2fake_clockwise_prev_hedge_around_vertex
        hedge2fake_clockwise_next_hedge_around_fface =\
            obj.hedge2fake_clockwise_next_hedge_around_fface
        hedge2fake_clockwise_prev_hedge_around_fface =\
            obj.hedge2fake_clockwise_prev_hedge_around_fface

        fface2degree =\
            obj.fface2degree
        hedge2fake_clockwise_fface =\
            obj.hedge2fake_clockwise_fface
        fface2arbitrary_hedge =\
            obj.fface2arbitrary_hedge


        (hedge2another_hedge
        ) = make_hedge2another_hedge(
            hedge2fake_clockwise_next_hedge_around_vertex
                = hedge2fake_clockwise_next_hedge_around_vertex
            ,hedge2fake_clockwise_next_hedge_around_fface
                = hedge2fake_clockwise_next_hedge_around_fface
            )
        yield (is_uint_bijection(hedge2another_hedge, hedge2another_hedge)
            , lambda: f'(hedge2fake_clockwise_next_hedge_around_vertex,hedge2fake_clockwise_next_hedge_around_fface) mismatch: ({hedge2fake_clockwise_next_hedge_around_vertex!r}, {hedge2fake_clockwise_next_hedge_around_fface!r})'
            )


        #verify value range of XXX2...hedge...
        #verify value range of XXX2...fface...
        yield (all(fface_degree >= 1 for fface_degree in fface2degree)
            , lambda: f'not all(fface_degree >= 1 for fface_degree in fface2degree): {fface2degree!r}'
            )
        yield (all(fface < num_ffaces for fface in hedge2fake_clockwise_fface)
            , lambda: f'not all(fface < num_ffaces for fface in hedge2fake_clockwise_fface): {hedge2fake_clockwise_fface!r}'
            )
        yield (all(hedge < num_hedges for hedge in fface2arbitrary_hedge)
            , lambda: f'not all(hedge < num_hedges for hedge in fface2arbitrary_hedge): {fface2arbitrary_hedge!r}'
            )


        #verify sum fface2degree == num_hedges
        yield (sum(fface2degree) == num_hedges
            , lambda: f'sum(fface2degree) != num_hedges: sum({fface2degree!r}) == {sum(fface2degree)} != {num_hedges}'
            )

        yield (is_uint_injection(fface2arbitrary_hedge, hedge2fake_clockwise_fface)
            , lambda: f'not is_uint_injection(fface2arbitrary_hedge, hedge2fake_clockwise_fface)'
            )

        (hedge2fake_clockwise_fface__new, fface2arbitrary_hedge__new
        ) = make_hedge2fake_clockwise_fface_ex(
                hedge2fake_clockwise_next_hedge_around_fface
                    = hedge2fake_clockwise_next_hedge_around_fface
                )

        #verify num_ffaces is the true size
        num_ffaces__shouldbe = len(fface2arbitrary_hedge__new)
        yield (num_ffaces__shouldbe == num_ffaces
            , lambda: f'num_ffaces should be {num_ffaces__shouldbe}: num_ffaces == {num_ffaces} != {num_ffaces__shouldbe} == num_ffaces__shouldbe'
            )

        old_fface2new_fface = tuple(
            hedge2fake_clockwise_fface__new[hedge]
            for hedge in fface2arbitrary_hedge
            )

        new_fface2old_fface = [None]*num_ffaces
        for old_fface, new_fface in enumerate(old_fface2new_fface):
            new_fface2old_fface[new_fface] = old_fface
        new_fface2old_fface = tuple(new_fface2old_fface)

        yield (all(old_fface is not None for old_fface in new_fface2old_fface)
            , lambda: f'bad fface2arbitrary_hedge: 2 fface idx map to a same fake face: {fface2arbitrary_hedge}'
            )
        assert is_uint_bijection(old_fface2new_fface, new_fface2old_fface)

        del hedge2fake_clockwise_fface__new, fface2arbitrary_hedge__new
        # now fface2arbitrary_hedge is collect
        #verify make_fface2degree ==>> fface2degree
        #verify make_hedge2fake_clockwise_fface ==>> hedge2fake_clockwise_fface

        (hedge2fake_clockwise_fface__shouldbe
        ) = make_hedge2fake_clockwise_fface(
            hedge2fake_clockwise_next_hedge_around_fface
                = hedge2fake_clockwise_next_hedge_around_fface
            ,fface2arbitrary_hedge
                = fface2arbitrary_hedge
            )
        (fface2degree__shouldbe
        ) = make_fface2degree(
            hedge2fake_clockwise_next_hedge_around_fface
                = hedge2fake_clockwise_next_hedge_around_fface
            ,fface2arbitrary_hedge
                = fface2arbitrary_hedge
            )

        triples = [('hedge2fake_clockwise_fface'
                    ,hedge2fake_clockwise_fface__shouldbe
                    ,hedge2fake_clockwise_fface)
                  ,('fface2degree'
                    ,fface2degree__shouldbe
                    ,fface2degree)
                  ]
        for attr, shouldbe, value in triples:
            yield (all(old==new for old, new in zip(value, shouldbe))
                , lambda: f'{attr} should be {shouldbe!r}: {attr} = {value!r}'
                )

if __name__ == "__main__":
    from .UGraphFakeEmbedding import UGraphFakeEmbedding
        # nn_ns.graph2.concrete_graph.ugraph__uint.UGraphFakeEmbedding instead of __main__.UGraphFakeEmbedding

    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


