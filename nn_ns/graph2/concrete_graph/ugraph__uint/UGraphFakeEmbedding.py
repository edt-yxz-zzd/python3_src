
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

    # 3 parallel non-loop edges
    >>> three_parallel_nonloops_graph = mk([2,5,4,1,0,3], [1,0,3,2,5,4])

    # 3 non_parallel non-loop edges
    >>> three_nonparallel_nonloops_graph = mk([2,3,4,5,0,1], [1,0,3,2,5,4])

    # a loop and a nonloop disconnected
    >>> one_loop_one_nonloop_disconnected_graph = mk([0,1,3,2], [1,0,3,2])

    >>> edgeless_graph
    UGraphFakeEmbedding(num_hedges = 0, num_ffaces = 0, num_fvertices = 0, hedge2fake_clockwise_next_hedge_around_vertex = [], hedge2fake_clockwise_prev_hedge_around_vertex = (), hedge2fake_clockwise_next_hedge_around_fface = (), hedge2fake_clockwise_prev_hedge_around_fface = (), fface2degree = (), hedge2fake_clockwise_fface = (), fface2arbitrary_hedge = (), fvertex2degree = (), hedge2fvertex = (), fvertex2arbitrary_hedge = ())
    >>> single_loop_graph
    UGraphFakeEmbedding(num_hedges = 2, num_ffaces = 2, num_fvertices = 1, hedge2fake_clockwise_next_hedge_around_vertex = [1, 0], hedge2fake_clockwise_prev_hedge_around_vertex = (1, 0), hedge2fake_clockwise_next_hedge_around_fface = (0, 1), hedge2fake_clockwise_prev_hedge_around_fface = (0, 1), fface2degree = (1, 1), hedge2fake_clockwise_fface = (0, 1), fface2arbitrary_hedge = (0, 1), fvertex2degree = (2,), hedge2fvertex = (0, 0), fvertex2arbitrary_hedge = (0,))
    >>> single_nonloop_graph
    UGraphFakeEmbedding(num_hedges = 2, num_ffaces = 1, num_fvertices = 2, hedge2fake_clockwise_next_hedge_around_vertex = [0, 1], hedge2fake_clockwise_prev_hedge_around_vertex = (0, 1), hedge2fake_clockwise_next_hedge_around_fface = (1, 0), hedge2fake_clockwise_prev_hedge_around_fface = (1, 0), fface2degree = (2,), hedge2fake_clockwise_fface = (0, 0), fface2arbitrary_hedge = (0,), fvertex2degree = (1, 1), hedge2fvertex = (0, 1), fvertex2arbitrary_hedge = (0, 1))
    >>> two_parallel_nonloops_graph
    UGraphFakeEmbedding(num_hedges = 4, num_ffaces = 2, num_fvertices = 2, hedge2fake_clockwise_next_hedge_around_vertex = [2, 3, 0, 1], hedge2fake_clockwise_prev_hedge_around_vertex = (2, 3, 0, 1), hedge2fake_clockwise_next_hedge_around_fface = (3, 2, 1, 0), hedge2fake_clockwise_prev_hedge_around_fface = (3, 2, 1, 0), fface2degree = (2, 2), hedge2fake_clockwise_fface = (0, 1, 1, 0), fface2arbitrary_hedge = (0, 1), fvertex2degree = (2, 2), hedge2fvertex = (0, 1, 0, 1), fvertex2arbitrary_hedge = (0, 1))
    >>> two_parallel_loops_graph
    UGraphFakeEmbedding(num_hedges = 4, num_ffaces = 3, num_fvertices = 1, hedge2fake_clockwise_next_hedge_around_vertex = [2, 0, 3, 1], hedge2fake_clockwise_prev_hedge_around_vertex = (1, 3, 0, 2), hedge2fake_clockwise_next_hedge_around_fface = (3, 1, 2, 0), hedge2fake_clockwise_prev_hedge_around_fface = (3, 1, 2, 0), fface2degree = (2, 1, 1), hedge2fake_clockwise_fface = (0, 1, 2, 0), fface2arbitrary_hedge = (0, 1, 2), fvertex2degree = (4,), hedge2fvertex = (0, 0, 0, 0), fvertex2arbitrary_hedge = (0,))
    >>> two_nonparallel_loops_graph
    UGraphFakeEmbedding(num_hedges = 4, num_ffaces = 1, num_fvertices = 1, hedge2fake_clockwise_next_hedge_around_vertex = [2, 3, 1, 0], hedge2fake_clockwise_prev_hedge_around_vertex = (3, 2, 0, 1), hedge2fake_clockwise_next_hedge_around_fface = (2, 3, 1, 0), hedge2fake_clockwise_prev_hedge_around_fface = (3, 2, 0, 1), fface2degree = (4,), hedge2fake_clockwise_fface = (0, 0, 0, 0), fface2arbitrary_hedge = (0,), fvertex2degree = (4,), hedge2fvertex = (0, 0, 0, 0), fvertex2arbitrary_hedge = (0,))
    >>> three_parallel_nonloops_graph
    UGraphFakeEmbedding(num_hedges = 6, num_ffaces = 3, num_fvertices = 2, hedge2fake_clockwise_next_hedge_around_vertex = [2, 5, 4, 1, 0, 3], hedge2fake_clockwise_prev_hedge_around_vertex = (4, 3, 0, 5, 2, 1), hedge2fake_clockwise_next_hedge_around_fface = (3, 4, 5, 0, 1, 2), hedge2fake_clockwise_prev_hedge_around_fface = (3, 4, 5, 0, 1, 2), fface2degree = (2, 2, 2), hedge2fake_clockwise_fface = (0, 1, 2, 0, 1, 2), fface2arbitrary_hedge = (0, 1, 2), fvertex2degree = (3, 3), hedge2fvertex = (0, 1, 0, 1, 0, 1), fvertex2arbitrary_hedge = (0, 1))
    >>> three_nonparallel_nonloops_graph
    UGraphFakeEmbedding(num_hedges = 6, num_ffaces = 1, num_fvertices = 2, hedge2fake_clockwise_next_hedge_around_vertex = [2, 3, 4, 5, 0, 1], hedge2fake_clockwise_prev_hedge_around_vertex = (4, 5, 0, 1, 2, 3), hedge2fake_clockwise_next_hedge_around_fface = (5, 4, 1, 0, 3, 2), hedge2fake_clockwise_prev_hedge_around_fface = (3, 2, 5, 4, 1, 0), fface2degree = (6,), hedge2fake_clockwise_fface = (0, 0, 0, 0, 0, 0), fface2arbitrary_hedge = (0,), fvertex2degree = (3, 3), hedge2fvertex = (0, 1, 0, 1, 0, 1), fvertex2arbitrary_hedge = (0, 1))
    >>> one_loop_one_nonloop_disconnected_graph
    UGraphFakeEmbedding(num_hedges = 4, num_ffaces = 3, num_fvertices = 3, hedge2fake_clockwise_next_hedge_around_vertex = [0, 1, 3, 2], hedge2fake_clockwise_prev_hedge_around_vertex = (0, 1, 3, 2), hedge2fake_clockwise_next_hedge_around_fface = (1, 0, 2, 3), hedge2fake_clockwise_prev_hedge_around_fface = (1, 0, 2, 3), fface2degree = (2, 1, 1), hedge2fake_clockwise_fface = (0, 0, 1, 2), fface2arbitrary_hedge = (0, 2, 3), fvertex2degree = (1, 1, 2), hedge2fvertex = (0, 1, 2, 2), fvertex2arbitrary_hedge = (0, 1, 2))







    >>> edgeless_graph.calc.is_ugraph_fake_embedding_planar
    True
    >>> single_loop_graph.calc.is_ugraph_fake_embedding_planar
    True
    >>> single_nonloop_graph.calc.is_ugraph_fake_embedding_planar
    True
    >>> two_parallel_nonloops_graph.calc.is_ugraph_fake_embedding_planar
    True
    >>> two_parallel_loops_graph.calc.is_ugraph_fake_embedding_planar
    True
    >>> two_nonparallel_loops_graph.calc.is_ugraph_fake_embedding_planar
    False
    >>> three_parallel_nonloops_graph.calc.is_ugraph_fake_embedding_planar
    True
    >>> three_nonparallel_nonloops_graph.calc.is_ugraph_fake_embedding_planar
    False
    >>> one_loop_one_nonloop_disconnected_graph.calc.is_ugraph_fake_embedding_planar
    True
'''












__all__ = '''
    UGraphFakeEmbedding
    VerifyUGraphFakeEmbedding
    '''.split()
'''
    iter_cycle_from
    inverse_uint_bijection

    make_hedge2another_hedge

    make_hedge2fake_clockwise_prev_hedge_around_fface
    make_hedge2fake_clockwise_fface_ex
    make_hedge2fake_clockwise_fface
    make_fface2degree

    make_hedge2fvertex_ex
    make_hedge2fvertex
    make_fvertex2degree

    make_XXX2degree
    make_hedge2XXX
    make_hedge2XXX_ex

    is_uint_injection
    is_uint_surjection
    is_uint_bijection
'''

from .iter_cycle_from import iter_cycle_from
from .inverse_uint_bijection import inverse_uint_bijection
from .is_uint_bijection import (is_uint_injection, is_uint_bijection)
from .get_attrs import get_attrs
from .makes_for_UGraphFakeEmbedding import (
    make_hedge2another_hedge

    ,make_hedge2fake_clockwise_prev_hedge_around_fface
    ,make_hedge2fake_clockwise_fface_ex
    ,make_hedge2fake_clockwise_fface
    ,make_fface2degree

    ,make_hedge2fvertex_ex
    ,make_hedge2fvertex
    ,make_fvertex2degree

    ,make_XXX2degree
    ,make_hedge2XXX
    ,make_hedge2XXX_ex
    )

from seed.helper.repr_input import repr_helper_ex
from seed.verify.common_verify import (
    is_UInt, is_Sequence, has_attrs
    #is_int, is_UInt, is_pair, is_tuple, is_Sequence
    #, is_strict_sorted_sequence
    )
from seed.verify.VerifyType import VerifyType__static


class UGraphFakeEmbedding:
    '''

methods:
    make_UGraphFakeEmbedding__simplest
    make_UGraphFakeEmbedding__simpler
    verify_ugraph_fake_embedding
    verify

    ireplace
    hedge2another_hedge
    hedge2iter_fake_clockwise_hedges_around_vertex
    hedge2iter_fake_clockwise_hedges_around_fface

    fvertex2iter_fake_clockwise_hedges
    fface2iter_fake_clockwise_hedges

calc attrs:
    # degree value that degree2sorted_XXXs[degree] is not empty
    # sorted_XXX_degrees_idx - index of sorted_XXX_degrees
    .calc.sorted_fface_degrees
        .calc.num_fface_degrees
        .calc.degree2maybe_sorted_fface_degrees_idx
        .calc.sorted_fface_degrees_idx2nonempty_sorted_ffaces
    .calc.sorted_fvertex_degrees
        .calc.num_fvertex_degrees
        .calc.degree2maybe_sorted_fvertex_degrees_idx
        .calc.sorted_fvertex_degrees_idx2nonempty_sorted_fvertices

'''
    all_UGraphFakeEmbedding_attr_seq = '''
        num_hedges
        num_ffaces
        num_fvertices
        hedge2fake_clockwise_next_hedge_around_vertex
        hedge2fake_clockwise_prev_hedge_around_vertex
        hedge2fake_clockwise_next_hedge_around_fface
        hedge2fake_clockwise_prev_hedge_around_fface

        fface2degree
        hedge2fake_clockwise_fface
        fface2arbitrary_hedge

        fvertex2degree
        hedge2fvertex
        fvertex2arbitrary_hedge
        '''.split()
    all_UGraphFakeEmbedding_attr_set = frozenset(all_UGraphFakeEmbedding_attr_seq)

    @classmethod
    def make_UGraphFakeEmbedding__simplest(cls, *
        ,hedge2fake_clockwise_next_hedge_around_vertex
        ,hedge2another_hedge
        ,fface2arbitrary_hedge = None
        ,fvertex2arbitrary_hedge = None
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
            ,fvertex2arbitrary_hedge = fvertex2arbitrary_hedge
            )
    @classmethod
    def make_UGraphFakeEmbedding__simpler(cls, *
        ,hedge2fake_clockwise_next_hedge_around_vertex
        ,hedge2fake_clockwise_prev_hedge_around_fface
        ,fface2arbitrary_hedge = None
        ,fvertex2arbitrary_hedge = None
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


        if fvertex2arbitrary_hedge is None:
            (hedge2fvertex, fvertex2arbitrary_hedge
            ) = make_hedge2fvertex_ex(
                hedge2fake_clockwise_next_hedge_around_vertex
                    = hedge2fake_clockwise_next_hedge_around_vertex
                )
        else:
            (hedge2fvertex
            ) = make_hedge2fvertex(
                hedge2fake_clockwise_next_hedge_around_vertex
                    = hedge2fake_clockwise_next_hedge_around_vertex
                ,fvertex2arbitrary_hedge
                    = fvertex2arbitrary_hedge
                )

        fface2degree = make_fface2degree(
            hedge2fake_clockwise_next_hedge_around_fface
                = hedge2fake_clockwise_next_hedge_around_fface
            ,fface2arbitrary_hedge
                = fface2arbitrary_hedge
            )
        fvertex2degree = make_fvertex2degree(
            hedge2fake_clockwise_next_hedge_around_vertex
                = hedge2fake_clockwise_next_hedge_around_vertex
            ,fvertex2arbitrary_hedge
                = fvertex2arbitrary_hedge
            )

        num_hedges = len(hedge2fake_clockwise_next_hedge_around_vertex)
        num_ffaces = len(fface2arbitrary_hedge)
        num_fvertices = len(fvertex2arbitrary_hedge)

        return cls.make_UGraphFakeEmbedding(
            num_hedges = num_hedges
            ,num_ffaces = num_ffaces
            ,num_fvertices = num_fvertices

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

            ,fvertex2degree = fvertex2degree
            ,hedge2fvertex = hedge2fvertex
            ,fvertex2arbitrary_hedge = fvertex2arbitrary_hedge
            )

    @classmethod
    def make_UGraphFakeEmbedding(cls, *
        ,num_hedges
        ,num_ffaces
        ,num_fvertices

        ,hedge2fake_clockwise_next_hedge_around_vertex
        ,hedge2fake_clockwise_prev_hedge_around_vertex
        ,hedge2fake_clockwise_next_hedge_around_fface
        ,hedge2fake_clockwise_prev_hedge_around_fface

        ,fface2degree
        ,hedge2fake_clockwise_fface
        ,fface2arbitrary_hedge

        ,fvertex2degree
        ,hedge2fvertex
        ,fvertex2arbitrary_hedge
        ):
        return __class__(
            num_hedges = num_hedges
            ,num_ffaces = num_ffaces
            ,num_fvertices = num_fvertices

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

            ,fvertex2degree = fvertex2degree
            ,hedge2fvertex = hedge2fvertex
            ,fvertex2arbitrary_hedge = fvertex2arbitrary_hedge
            )


    def __init__(self, *
        ,num_hedges
        ,num_ffaces
        ,num_fvertices

        ,hedge2fake_clockwise_next_hedge_around_vertex
        ,hedge2fake_clockwise_prev_hedge_around_vertex
        ,hedge2fake_clockwise_next_hedge_around_fface
        ,hedge2fake_clockwise_prev_hedge_around_fface

        ,fface2degree
        ,hedge2fake_clockwise_fface
        ,fface2arbitrary_hedge

        ,fvertex2degree
        ,hedge2fvertex
        ,fvertex2arbitrary_hedge
        ):
        self.num_hedges = num_hedges
        self.num_ffaces = num_ffaces
        self.num_fvertices = num_fvertices

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

        self.fvertex2degree = fvertex2degree
        self.hedge2fvertex = hedge2fvertex
        self.fvertex2arbitrary_hedge = fvertex2arbitrary_hedge

        assert self.verify_ugraph_fake_embedding(AssertionError)


        from .calc_UGraphFakeEmbedding_info.Calc_UGraphFakeEmbedding_Info import Calc_UGraphFakeEmbedding_Info
        assert isinstance(self, UGraphFakeEmbedding)
        self.calc = Calc_UGraphFakeEmbedding_Info(self) # .is_fake_embedding_planar

    def verify_ugraph_fake_embedding(self, __mkError=None):
        return VerifyUGraphFakeEmbedding(self, __mkError)

    def verify(self, __mkError=None):
        return self.verify_ugraph_fake_embedding(__mkError)

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


    def ireplace(self, **kwargs):
        d = get_attrs(self, __class__.all_UGraphFakeEmbedding_attr_seq)
        d.update(kwargs)
        cls = type(self)
        return cls.make_UGraphFakeEmbedding(**d)

    def hedge2another_hedge(self, hedge):
        return self.hedge2fake_clockwise_next_hedge_around_vertex[
                self.hedge2fake_clockwise_next_hedge_around_fface[hedge]]
    def hedge2iter_fake_clockwise_hedges_around_vertex(self, hedge, *, reverse=False):
        if reverse:
            hedge2next = self.hedge2fake_clockwise_prev_hedge_around_vertex
        else:
            hedge2next = self.hedge2fake_clockwise_next_hedge_around_vertex
        return iter_cycle_from(hedge2next, hedge)
    def hedge2iter_fake_clockwise_hedges_around_fface(self, hedge, *, reverse=False):
        if reverse:
            hedge2next = self.hedge2fake_clockwise_prev_hedge_around_fface
        else:
            hedge2next = self.hedge2fake_clockwise_next_hedge_around_fface
        return iter_cycle_from(hedge2next, hedge)
    def fvertex2iter_fake_clockwise_hedges(self, fvertex, *, reverse=False):
        hedge = self.fvertex2arbitrary_hedge[fvertex]
        return self.hedge2iter_fake_clockwise_hedges_around_vertex(hedge, reverse=reverse)
    def fface2iter_fake_clockwise_hedges(self, fface, *, reverse=False):
        hedge = self.fface2arbitrary_hedge[fface]
        return self.hedge2iter_fake_clockwise_hedges_around_fface(hedge, reverse=reverse)


class VerifyUGraphFakeEmbedding(VerifyType__static):
    types = UGraphFakeEmbedding
    def _iter_verify_object_(_, obj):
        # -> Iter (bool, err_msg_or_f)
        def is_uint_seq(obj):
            return is_Sequence.of(obj, is_UInt)
        attrs = UGraphFakeEmbedding.all_UGraphFakeEmbedding_attr_seq

        yield (has_attrs(obj, attrs=attrs)
            , lambda: f'missing some attrs: {attrs!r}'
            )


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
        num_fvertices = obj.num_fvertices

        #verify len of hedge2...
        #verify len of fface2...
        #verify len of fvertex2...
        d = {'hedge2': 'num_hedges'
            ,'fface2':'num_ffaces'
            ,'fvertex2':'num_fvertices'
            }
        for attr in attrs:
            attr_head = attr[:attr.find('2')+1]
            if not attr_head: continue
            attr__XXX2YYY = attr; del attr

            XXX2YYY = getattr(obj, attr__XXX2YYY)
            len_XXX2YYY = len(XXX2YYY)

            attr__num_XXXs = d[attr_head]
            num_XXXs = getattr(obj, attr__num_XXXs)

            yield (len_XXX2YYY == num_XXXs
                , lambda: f'len({attr__XXX2YYY!s}) != {attr__num_XXXs!s}: {len_XXX2YYY!r} != {num_XXXs!r}'
                )
        del d



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
        yield (all(hedge__from != hedge__to for hedge__from, hedge__to in enumerate(hedge2another_hedge))
            , lambda: 'hedge2another_hedge should have no self-reflect hedge: hedge2another_hedge={hedge2another_hedge!r}'
            )
        assert num_hedges & 1 == 0 # even



        fface2degree = obj.fface2degree
        hedge2fake_clockwise_fface = obj.hedge2fake_clockwise_fface
        fface2arbitrary_hedge = obj.fface2arbitrary_hedge

        fvertex2degree = obj.fvertex2degree
        hedge2fvertex = obj.hedge2fvertex
        fvertex2arbitrary_hedge = obj.fvertex2arbitrary_hedge

        #verify value range of XXX2...degree...
        #verify value range of XXX2...hedge...
        #verify value range of XXX2...fface...
        #verify value range of XXX2...fvertex...
        d = {'hedge':'num_hedges'
            ,'fface':'num_ffaces'
            ,'fvertex':'num_fvertices'
            }
        s = '''
            fface2degree
            hedge2fake_clockwise_fface
            fface2arbitrary_hedge

            fvertex2degree
            hedge2fvertex
            fvertex2arbitrary_hedge
            '''.split()
        for attr__XXX2YYY in s:
            XXX2YYY = getattr(obj, attr__XXX2YYY)

            i = max(attr__XXX2YYY.rfind('2'), attr__XXX2YYY.rfind('_'))
            assert i > 0
            attr__YYY = attr__XXX2YYY[i+1:]
            if attr__YYY == 'degree':
                min_XXX2YYY = min(XXX2YYY, default=1)
                yield (min_XXX2YYY >= 1
                    , lambda: f'min({attr__XXX2YYY!s}) == {min_XXX2YYY!r} < 1: {XXX2YYY!r}'
                    )
            else:
                attr__num_YYYs = d[attr__YYY]
                num_YYYs = getattr(obj, attr__num_YYYs)
                max_XXX2YYY = max(XXX2YYY, default=-1)
                yield (max_XXX2YYY < num_YYYs
                    , lambda: f'max({attr__XXX2YYY!s}) == {max_XXX2YYY!r} >= {num_YYYs!r} == {attr__num_YYYs!s}: {XXX2YYY!r}'
                    )
        del d, s

        yield from _verify_3(obj
            ,attr__XXX2degree = 'fface2degree'
            ,attr__hedge2XXX = 'hedge2fake_clockwise_fface'
            ,attr__XXX2arbitrary_hedge = 'fface2arbitrary_hedge'
            ,attr__hedge2next_hedge_around_XXX = 'hedge2fake_clockwise_next_hedge_around_fface'
            ,attr__num_XXXs = 'num_ffaces'
            )
        yield from _verify_3(obj
            ,attr__XXX2degree = 'fvertex2degree'
            ,attr__hedge2XXX = 'hedge2fvertex'
            ,attr__XXX2arbitrary_hedge = 'fvertex2arbitrary_hedge'
            ,attr__hedge2next_hedge_around_XXX = 'hedge2fake_clockwise_next_hedge_around_vertex'
            ,attr__num_XXXs = 'num_fvertices'
            )


def _verify_3(obj, *
    ,attr__XXX2degree
    ,attr__hedge2XXX
    ,attr__XXX2arbitrary_hedge
    ,attr__hedge2next_hedge_around_XXX
    ,attr__num_XXXs
    ):
    '''
output:
    Iter ...
input:
    attr__XXX2degree
    attr__hedge2XXX
    attr__XXX2arbitrary_hedge
    attr__hedge2next_hedge_around_XXX
    attr__num_XXXs
        fface2degree
        hedge2fake_clockwise_fface
        fface2arbitrary_hedge
        hedge2fake_clockwise_next_hedge_around_fface
        num_ffaces

        OR:
        fvertex2degree
        hedge2fvertex
        fvertex2arbitrary_hedge
        hedge2fake_clockwise_next_hedge_around_vertex
        num_fvertices

precondition:
    hedge2next_hedge_around_XXX, XXX2degree, hedge2XXX, XXX2arbitrary_hedge are seq<UInt>

    len(hedge2next_hedge_around_XXX) == num_hedges
    hedge2next_hedge_around_XXX is bijection

    len(XXX2degree) == num_XXXs
    len(hedge2XXX) == num_hedges
    len(XXX2arbitrary_hedge) == num_XXXs

    min(XXX2degree, default=1) >= 1
    max(hedge2XXX, default=-1) < num_XXXs
    max(XXX2arbitrary_hedge, default=-1) < num_hedges
'''
    XXX2degree = getattr(obj, attr__XXX2degree)
    hedge2XXX = getattr(obj, attr__hedge2XXX)
    XXX2arbitrary_hedge = getattr(obj, attr__XXX2arbitrary_hedge)
    hedge2next_hedge_around_XXX = getattr(obj, attr__hedge2next_hedge_around_XXX)

    num_hedges = len(hedge2XXX)
    assert num_hedges == len(hedge2next_hedge_around_XXX)

    #verify sum XXX2degree == num_hedges
    sum_XXX2degree = sum(XXX2degree)
    yield (sum_XXX2degree == num_hedges
        , lambda: f'sum({attr__XXX2degree!s}) == {sum_XXX2degree!r} != {num_hedges!r} == num_hedges: {XXX2degree!r}'
        )

    yield (is_uint_injection(XXX2arbitrary_hedge, hedge2XXX)
        , lambda: f'not is_uint_injection({attr__XXX2arbitrary_hedge!s}, {attr__hedge2XXX!s})'
        )

    (hedge2XXX__new, XXX2arbitrary_hedge__new) = make_hedge2XXX_ex(
        hedge2next_hedge_around_XXX=hedge2next_hedge_around_XXX)
        #make_hedge2fake_clockwise_fface_ex

    #verify num_XXXs is the true size
    num_XXXs__shouldbe = len(XXX2arbitrary_hedge__new)
    num_XXXs = getattr(obj, attr__num_XXXs)
    yield (num_XXXs__shouldbe == num_XXXs
        , lambda: f'{attr__num_XXXs!s} should be {num_XXXs__shouldbe!r}: {attr__num_XXXs!s} == {num_XXXs!r} != {num_XXXs__shouldbe!r} == {attr__num_XXXs!s}__shouldbe'
        )

    old_XXX2new_XXX = tuple(hedge2XXX__new[hedge] for hedge in XXX2arbitrary_hedge)

    new_XXX2old_XXX = [None]*num_XXXs
    for old_XXX, new_XXX in enumerate(old_XXX2new_XXX):
        new_XXX2old_XXX[new_XXX] = old_XXX
    new_XXX2old_XXX = tuple(new_XXX2old_XXX)

    yield (all(old_XXX is not None for old_XXX in new_XXX2old_XXX)
        , lambda: f'bad {attr__XXX2arbitrary_hedge!s}: not an exact cycle'
        )
    assert is_uint_bijection(old_XXX2new_XXX, new_XXX2old_XXX)

    del hedge2XXX__new, XXX2arbitrary_hedge__new
    # now XXX2arbitrary_hedge is collect
    #verify make_XXX2degree ==>> XXX2degree
    #verify make_hedge2XXX ==>> hedge2XXX

    hedge2XXX__shouldbe = make_hedge2XXX(
        hedge2next_hedge_around_XXX=hedge2next_hedge_around_XXX
        ,XXX2arbitrary_hedge = XXX2arbitrary_hedge
        )
        #make_hedge2fake_clockwise_fface
    (XXX2degree__shouldbe
    ) = make_XXX2degree(
        hedge2next_hedge_around_XXX=hedge2next_hedge_around_XXX
        ,XXX2arbitrary_hedge = XXX2arbitrary_hedge
        )
        #make_fface2degree

    triples = [(attr__hedge2XXX, hedge2XXX__shouldbe, hedge2XXX)
              ,(attr__XXX2degree, XXX2degree__shouldbe, XXX2degree)
              ]
    for attr, shouldbe, value in triples:
        yield (all(old==new for old, new in zip(value, shouldbe))
            , lambda: f'{attr!s} should be {shouldbe!r}: {attr!s} == {value!r} != {shouldbe!r} == {attr!s}__shouldbe'
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


