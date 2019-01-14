
r'''
see:
    "decompose/README.txt"/UGraph
    nn_ns.CFG.CFG
        using class style like nn_ns.CFG.CFG

UGraph =
    # allow self_loop and multiedge
    #   # allow parallel_loop # multi_self_loop
    # every hedge is outgo hedge
    {num_vertices # for isolated vertices
    ,hedge2vertex
    ,hedge2aedge
    ######### generated dynamic on need or input ############
    ,hedge2fake_clockwise_next_hedge_around_vertex   # fake_embedding
    ,hedge2fake_clockwise_fface                      # named fface
    ######### generated dynamic on need ############
    #,hedge2is_outgo # always True
    ,num_hedges
    ,num_aedges # since no laedge
    ,num_ffaces

    ,hedge2another_hedge
    ,hedge2fake_clockwise_prev_hedge_around_vertex
    ,hedge2fake_clockwise_next_hedge_around_fface
        = hedge2fake_clockwise_prev_hedge_around_vertex . hedge2another_hedge
    ,hedge2fake_clockwise_prev_hedge_around_fface
        = hedge2another_hedge . hedge2fake_clockwise_next_hedge_around_vertex

    ,vertex2degree
    ,fface2degree
    #,aedge2degree # always 2

    ,vertex2unstable_maybe_arbitrary_hedge # vertex degree may be 0
    ,aedge2unstable_arbitrary_hedge # aedge degree == 2 # ugraph
    ,fface2unstable_arbitrary_hedge # fface degree >= 1
        # outgo hedges form fake_clockwise cycles1

    ,unstable_isolated_vertices
    ,unstable_self_loop_aedges
    }


'''


__all__ = '''
    UGraph
    VerifyUGraph
    '''.split()

from .UGraphBasic import UGraphBasic
from .UGraphFakeEmbedding import UGraphFakeEmbedding
from .makes_for_UGraph import makes_for_UGraph

from .iter_cycle_from import iter_cycle_from
from .inverse_uint_bijection import inverse_uint_bijection
from .is_uint_bijection import (
    is_uint_injection, is_uint_bijection, is_partial_uint_bijection
    )
from .get_attrs import get_attrs


from seed.types.StructBase import StructBase
from seed.helper.repr_input import repr_helper_ex
from seed.verify.common_verify import (
    is_UInt, is_Sequence, has_attrs
    #is_int, is_UInt, is_pair, is_tuple, is_Sequence
    #, is_strict_sorted_sequence
    )
from seed.verify.VerifyType import VerifyType__static
from seed.iters.iter_unique_by_hash import iter_unique_by_hash
from seed.tiny import null_iter
from itertools import chain


def Calc_UGraph_Info(self):
    from .calc_UGraph_info.Calc_UGraph_Info import Calc_UGraph_Info
    return Calc_UGraph_Info(self)

class UGraph(StructBase):
    '''

attrs:
    ugraph_basic
    ugraph_fake_embedding

    ###### properties
    ######  !xxx - input or eval
    ######  .xxx - redirected
    .num_vertices
    .num_aedges
    .num_hedges
        # <<== ugraph_fake_embedding.num_hedges
        # <<== ugraph_basic.num_vertices
        # <<== ugraph_basic.num_aedges
        # <<== ugraph_basic.num_hedges

    .hedge2vertex
    .hedge2aedge
        # <<== ugraph_basic.hedge2vertex
        # <<== ugraph_basic.hedge2aedge

    !aedge2arbitrary_hedge
        # <<== hedge2aedge
    .hedge2another_hedge
        # <<== ugraph_fake_embedding.hedge2another_hedge()
        # <<== ugraph_basic.hedge2another_hedge[]

    !fvertex2vertex
        # <<== hedge2vertex + ugraph_fake_embedding.fvertex2arbitrary_hedge
    !vertex2maybe_fvertex
        # <<== fvertex2vertex
    .vertex2degree
        <<== hedge2vertex
        <<== vertex2maybe_fvertex + ugraph_fake_embedding.fvertex2degree
        <<== ugraph_basic.vertex2degree

constructors:
    make_UGraph__simplest
    make_UGraph__simpler
    make_UGraph_kwargs__simpler
methods:
    vertex2maybe_arbitrary_hedge
        <<== vertex2maybe_fvertex + ugraph_fake_embedding.fvertex2arbitrary_hedge

    degree2unstable_iter_vertices
        <<== degree2sorted_vertices
    is_aedge_self_loop
    is_vertex_edgeless

    aedge2unstable_iter_hedges
    vertex2unstable_iter_hedges
    hedge2unstable_iter_hedges_around_vertex
    hedge2unstable_iter_other_hedges_around_vertex
    hedge2unstable_iter_other_hedges_around_another_vertex


calc attrs:
    """
    neednot:
    .calc.sorted_vertex_degrees
        .calc.num_vertex_degrees
        .calc.degree2maybe_sorted_vertex_degrees_idx
        .calc.sorted_vertex_degrees_idx2nonempty_sorted_vertices
        <<== .calc.sorted_isolated_vertices + ugraph_fake_embedding.calc fvertex version
    """
    .calc.sorted_self_loop_aedges
    .calc.degree2sorted_vertices
        <<== vertex2degree
        #.calc.sorted_isolated_vertices
    .calc.sorted_nonempty_vertex_degrees
        <<== degree2sorted_vertices
    .calc.either_ugraph_nonplanar_condition_or_ugraph_planar_embedding
        # ugraph_nonplanar_condition not ugraph_fake_embedding_nonplanar_condition
        # (False, ugraph_nonplanar_condition)
        # (True, ugraph_planar_embedding)
    .calc.is_ugraph_rigid_connected
    .calc.is_ugraph_rigid_biconnected
    .calc.is_ugraph_rigid_triconnected

ugraph_basic.calc attrs:
ugraph_fake_embedding.calc attrs:

'''
    all_UGraph_attr_seq = '''
        ugraph_basic
        ugraph_fake_embedding

        aedge2arbitrary_hedge
        fvertex2vertex
        vertex2maybe_fvertex
        '''.split()
    all_UGraph_attr_set = frozenset(all_UGraph_attr_seq)
    all_UGraph_primekey_attr_seq = tuple(all_UGraph_attr_seq)

    all_exported_UGraph_attr_seq = tuple(iter_unique_by_hash(chain(
        all_UGraph_attr_seq
        ,UGraphBasic.all_UGraphBasic_attr_seq
        ,UGraphFakeEmbedding.all_UGraphFakeEmbedding_attr_seq
        )))
        # duplicated: "num_hedges"


    @classmethod
    def make_UGraph__simplest(cls, *
        ,num_vertices
        ,hedge2vertex
        ,hedge2aedge
        ):
        ugraph_basic = UGraphBasic.make_UGraphBasic__simplest(
            num_vertices=num_vertices
            ,hedge2vertex=hedge2vertex
            ,hedge2aedge=hedge2aedge
            )
        return cls.make_UGraph__simpler(ugraph_basic=ugraph_basic)

    @classmethod
    def make_UGraph__simpler(cls, *
        ,ugraph_basic
        ,ugraph_fake_embedding=None
        ,aedge2arbitrary_hedge=None
        ,fvertex2vertex=None
        ,vertex2maybe_fvertex=None
        ):
        return cls.make_UGraph(**cls.make_UGraph_kwargs__simpler(
            ugraph_basic=ugraph_basic
            ,ugraph_fake_embedding=ugraph_fake_embedding
            ,aedge2arbitrary_hedge=aedge2arbitrary_hedge
            ,fvertex2vertex=fvertex2vertex
            ,vertex2maybe_fvertex=vertex2maybe_fvertex
            ))
    @classmethod
    def make_UGraph_kwargs__simpler(cls, *
        ,ugraph_basic
        ,ugraph_fake_embedding=None
        ,aedge2arbitrary_hedge=None
        ,fvertex2vertex=None
        ,vertex2maybe_fvertex=None
        ):
        if aedge2arbitrary_hedge is None:
            aedge2arbitrary_hedge = (makes_for_UGraph
                .aedge2arbitrary_hedge
                .from_hedge2aedge(hedge2aedge=ugraph_basic.hedge2aedge)
                )

        if fvertex2vertex is None:
            if ugraph_fake_embedding is None:
                fvertex2vertex = (makes_for_UGraph
                    .fvertex2vertex.from_vertex2degree(
                        vertex2degree=ugraph_basic.vertex2degree
                        )
                    )
            else:
                fvertex2vertex = (makes_for_UGraph
                    .fvertex2vertex.from_fvertex2arbitrary_hedge(
                        hedge2vertex=ugraph_basic.hedge2vertex
                        ,fvertex2arbitrary_hedge
                            =ugraph_fake_embedding.fvertex2arbitrary_hedge
                        )
                    )

        assert fvertex2vertex is not None
        num_fvertices = len(fvertex2vertex)

        if vertex2maybe_fvertex is None:
            vertex2maybe_fvertex = (makes_for_UGraph
                .vertex2maybe_fvertex.from_fvertex2vertex(
                    num_vertices=ugraph_basic.num_vertices
                    ,fvertex2vertex=fvertex2vertex
                    )
                )
        if ugraph_fake_embedding is None:
            num_fvertices
            vertex2maybe_fvertex

            ugraph_fake_embedding = (makes_for_UGraph
                .ugraph_fake_embedding.from_hedge2vertex(
                    num_fvertices=num_fvertices
                    ,hedge2vertex=ugraph_basic.hedge2vertex
                    ,vertex2maybe_fvertex=vertex2maybe_fvertex
                    ,hedge2another_hedge=ugraph_basic.hedge2another_hedge
                    )
                )
        return dict(
            ugraph_basic=ugraph_basic
            ,ugraph_fake_embedding=ugraph_fake_embedding
            ,aedge2arbitrary_hedge=aedge2arbitrary_hedge
            ,fvertex2vertex=fvertex2vertex
            ,vertex2maybe_fvertex=vertex2maybe_fvertex
            )


    @classmethod
    def make_UGraph(cls, *
        ,ugraph_basic
        ,ugraph_fake_embedding
        ,aedge2arbitrary_hedge
        ,fvertex2vertex
        ,vertex2maybe_fvertex
        ):
        return __class__(
            ugraph_basic=ugraph_basic
            ,ugraph_fake_embedding=ugraph_fake_embedding
            ,aedge2arbitrary_hedge=aedge2arbitrary_hedge
            ,fvertex2vertex=fvertex2vertex
            ,vertex2maybe_fvertex=vertex2maybe_fvertex
            )
    def __init__(self, *
        ,ugraph_basic
        ,ugraph_fake_embedding

        ,aedge2arbitrary_hedge
        ,fvertex2vertex
        ,vertex2maybe_fvertex
        #,degree2sorted_vertices
        #,sorted_vertex_degrees
        ):
        super().__init__(
            ugraph_basic=ugraph_basic
            ,ugraph_fake_embedding=ugraph_fake_embedding
            ,aedge2arbitrary_hedge=aedge2arbitrary_hedge
            ,fvertex2vertex=fvertex2vertex
            ,vertex2maybe_fvertex=vertex2maybe_fvertex
            )
        assert self.verify_ugraph(AssertionError)
        return

        self.ugraph_basic = ugraph_basic
        self.ugraph_fake_embedding = ugraph_fake_embedding

        self.aedge2arbitrary_hedge = aedge2arbitrary_hedge
        self.fvertex2vertex = fvertex2vertex
        self.vertex2maybe_fvertex = vertex2maybe_fvertex

        assert self.verify_ugraph(AssertionError)


        from .calc_UGraph_info.Calc_UGraph_Info import Calc_UGraph_Info
        assert isinstance(self, UGraph)
        self.calc = Calc_UGraph_Info(self)

    def verify_ugraph(self, __mkError=None):
        return VerifyUGraph(self, __mkError)

    def verify(self, __mkError=None):
        return self.verify_ugraph(__mkError)

    """
    def __repr__(self):
        all_UGraph_attr_seq = __class__.all_UGraph_attr_seq
        assert len(self.__dict__)-1 == len(all_UGraph_attr_seq)
            # exclude 'calc'
        return repr_helper_ex(self, (), all_UGraph_attr_seq, {}, ordered_attrs_only=True)
    def __delattr__(self, attr):
        raise AttributeError(attr)
    def __setattr__(self, attr, obj):
        if hasattr(self, attr):
            raise AttributeError(attr)
        if attr in __class__.all_UGraph_attr_set or attr == 'calc':
            super().__setattr__(attr, obj)
        raise AttributeError(attr)
    """

    '''
    def __setattr__(self, attr, obj):
        if attr in __class__.all_UGraph_attr_set or attr == 'calc':
            if hasattr(self, attr):
                # @property all_UGraph_attr_set
                raise AttributeError(attr)
            # inside __init__()
        super().__setattr__(attr, obj)
    '''

    @classmethod
    def __iter_all_primekey_attrs__(cls):
        yield from cls.all_UGraph_primekey_attr_seq
        yield from super().__iter_all_primekey_attrs__()
    @classmethod
    def __iter_all_user_attrs__(cls):
        yield from cls.all_UGraph_attr_seq
        yield from super().__iter_all_user_attrs__()
    @classmethod
    def __iter_all_impl_attrs__(cls):
        yield from cls.all_UGraph_attr_seq
        yield 'calc'
        yield from super().__iter_all_impl_attrs__()
    @classmethod
    def __iter_all_cached_attr_calc_pairs__(cls):
        yield 'calc', Calc_UGraph_Info
        yield from super().__iter_all_cached_attr_calc_pairs__()



    ############################ methods ###########################
    def vertex2maybe_arbitrary_hedge(self, vertex):
        maybe_fvertex = self.vertex2maybe_fvertex[vertex]
        if maybe_fvertex is None:
            return None
        else:
            fvertex = maybe_fvertex
            return self.fvertex2arbitrary_hedge[fvertex]
    def degree2unstable_iter_vertices(self, vertex_degree):
        assert vertex_degree >= 0
        ls = self.degree2sorted_vertices
        if not 0 <= vertex_degree < len(ls):
            return null_iter
        return iter(ls[vertex_degree])
    def is_aedge_self_loop(self, aedge):
        hedge = self.aedge2arbitrary_hedge[aedge]
        other = self.hedge2another_hedge[hedge]
        return self.hedge2vertex[hedge] == self.hedge2vertex[other]
    #def is_vertex_isolated(self, vertex):
    def is_vertex_edgeless(self, vertex):
        return not self.vertex2degree[vertex]

    def aedge2unstable_iter_hedges(self, aedge):
        hedge = self.aedge2arbitrary_hedge[aedge]
        yield hedge
        other = self.hedge2another_hedge[hedge]
        yield other
    def vertex2unstable_iter_hedges(self, vertex):
        maybe_hedge = self.vertex2maybe_arbitrary_hedge(vertex)
        if maybe_hedge is None:
            return null_iter
        else:
            hedge = maybe_hedge
            return self.hedge2unstable_iter_hedges_around_vertex(hedge)
    def hedge2unstable_iter_hedges_around_vertex(self, hedge):
        return self.ugraph_fake_embedding.hedge2iter_fake_clockwise_hedges_around_vertex(hedge)
    def hedge2unstable_iter_other_hedges_around_vertex(self, hedge):
        # like hedge2unstable_iter_hedges_around_vertex
        #   but exclude the input hedge
        it = self.ugraph_fake_embedding.hedge2iter_fake_clockwise_hedges_around_vertex(hedge)
        assert iter(it) is it
        for this in it:
            # skip head which is the input hedge
            if this != hedge: raise logic-error
            break
        else:
            raise logic-error
        return it

    def hedge2unstable_iter_other_hedges_around_another_vertex(self, hedge):
        other = self.hedge2another_hedge[hedge]
        return self.hedge2unstable_iter_other_hedges_around_vertex(other)

    ############################ properties ###########################

    '''
    UGraphBasic.all_UGraphBasic_attr_seq
        num_vertices
        num_aedges
        num_hedges
        hedge2vertex
        hedge2aedge
        hedge2another_hedge
        vertex2degree
    '''
    @property
    def num_vertices(self):
        return self.ugraph_basic.num_vertices
    @property
    def num_aedges(self):
        return self.ugraph_basic.num_aedges
    @property
    def num_hedges(self):
        return self.ugraph_basic.num_hedges
    @property
    def hedge2vertex(self):
        return self.ugraph_basic.hedge2vertex
    @property
    def hedge2aedge(self):
        return self.ugraph_basic.hedge2aedge
    @property
    def hedge2another_hedge(self):
        return self.ugraph_basic.hedge2another_hedge
    @property
    def vertex2degree(self):
        return self.ugraph_basic.vertex2degree

    '''
    UGraphFakeEmbedding.all_UGraphFakeEmbedding_attr_seq
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
    '''
    @property
    def num_ffaces(self):
        return self.ugraph_fake_embedding.num_ffaces
    @property
    def num_fvertices(self):
        return self.ugraph_fake_embedding.num_fvertices
    @property
    def hedge2fake_clockwise_next_hedge_around_vertex(self):
        return self.ugraph_fake_embedding.hedge2fake_clockwise_next_hedge_around_vertex
    @property
    def hedge2fake_clockwise_prev_hedge_around_vertex(self):
        return self.ugraph_fake_embedding.hedge2fake_clockwise_prev_hedge_around_vertex
    @property
    def hedge2fake_clockwise_next_hedge_around_fface(self):
        return self.ugraph_fake_embedding.hedge2fake_clockwise_next_hedge_around_fface
    @property
    def hedge2fake_clockwise_prev_hedge_around_fface(self):
        return self.ugraph_fake_embedding.hedge2fake_clockwise_prev_hedge_around_fface

    @property
    def fface2degree(self):
        return self.ugraph_fake_embedding.fface2degree
    @property
    def hedge2fake_clockwise_fface(self):
        return self.ugraph_fake_embedding.hedge2fake_clockwise_fface
    @property
    def fface2arbitrary_hedge(self):
        return self.ugraph_fake_embedding.fface2arbitrary_hedge

    @property
    def fvertex2degree(self):
        return self.ugraph_fake_embedding.fvertex2degree
    @property
    def hedge2fvertex(self):
        return self.ugraph_fake_embedding.hedge2fvertex
    @property
    def fvertex2arbitrary_hedge(self):
        return self.ugraph_fake_embedding.fvertex2arbitrary_hedge














class VerifyUGraph(VerifyType__static):
    types = UGraph
    def _iter_verify_object_(_, obj):
        # -> Iter (bool, err_msg_or_f)
        def is_mayuint(obj):
            return obj is None or is_UInt(obj)
        def is_mayuint_seq(obj):
            return is_Sequence.of(obj, is_mayuint)
        def is_uint_seq(obj):
            return is_Sequence.of(obj, is_UInt)
        attrs = UGraph.all_UGraph_attr_seq

        yield (has_attrs(obj, attrs=attrs)
            , lambda: f'missing some attrs: {attrs!r}'
            )

        yield (has_attrs(obj, attrs=UGraph.all_exported_UGraph_attr_seq)
            , lambda: f'missing some attrs: {attrs!r}'
            )


        '''
        ugraph_basic
        ugraph_fake_embedding
        '''
        ugraph_basic = obj.ugraph_basic
        ugraph_fake_embedding = obj.ugraph_fake_embedding
        yield (isinstance(ugraph_basic, UGraphBasic)
            , lambda: 'ugraph_basic is not UGraphBasic'
            )
        yield (isinstance(ugraph_fake_embedding, UGraphFakeEmbedding)
            , lambda: 'ugraph_fake_embedding is not UGraphFakeEmbedding'
            )
        yield (ugraph_basic.num_hedges == ugraph_fake_embedding.num_hedges
            , lambda: 'ugraph_basic.num_hedges != ugraph_fake_embedding.num_hedges'
            )
        yield (ugraph_basic.num_vertices >= ugraph_fake_embedding.num_fvertices
            , lambda: 'ugraph_basic.num_vertices < ugraph_fake_embedding.num_fvertices'
            )


        attrs = '''
            aedge2arbitrary_hedge
            fvertex2vertex
            vertex2maybe_fvertex
            '''.split()
        triples = [
            ('aedge2arbitrary_hedge', 'UInt', is_uint_seq)
            ,('fvertex2vertex', 'UInt', is_uint_seq)
            ,('vertex2maybe_fvertex', 'Maybe UInt', is_mayuint_seq)
            ]
        for attr, type_name, verifier in triples:
            value = getattr(obj, attr)
            yield (verifier(value)
                , lambda:f'{attr!s} is not sequence<{type_name!s}>: {value!r}'
                )


        #verify len of aedge2...
        #verify len of vertex2...
        #verify len of fvertex2...
        d = {'aedge2': 'num_aedges'
            ,'vertex2':'num_vertices'
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


        #verify value range of XXX2...hedge...
        #verify value range of XXX2...vertex...
        #verify value range of XXX2...maybe_fvertex...
        def _max_(iterable):
            return max(iterable, default=-1)
        def filter_out_Nones(iterable):
            return (x for x in iterable if x is not None)
        def _max_maybe_(iterable):
            return _max_(filter_out_Nones(iterable))

        triples = [
            #('attr', max_func, upper_bound)
            ('aedge2arbitrary_hedge', _max_, 'num_hedges')
            ,('fvertex2vertex', _max_, 'num_vertices')
            ,('vertex2maybe_fvertex', _max_maybe_, 'num_fvertices')
            ]
        for attr__XXX2mayYYY, max_func, attr__num_YYYs in triples:
            XXX2mayYYY = getattr(obj, attr__XXX2mayYYY)
            MAX = max_func(XXX2mayYYY)
            num_YYYs = getattr(obj, attr__num_YYYs)
            yield (MAX < num_YYYs
                , lambda: f'{MAX!r} == max({attr__XXX2mayYYY!s}) >= {attr__num_YYYs!s} == {num_YYYs!r}'
                )


        aedge2arbitrary_hedge = obj.aedge2arbitrary_hedge
        hedge2aedge = obj.hedge2aedge
        yield (is_uint_injection(aedge2arbitrary_hedge, hedge2aedge)
            , lambda: f'not is_uint_injection(aedge2arbitrary_hedge, hedge2aedge)'
            )

        fvertex2vertex = obj.fvertex2vertex
        vertex2maybe_fvertex = obj.vertex2maybe_fvertex
        yield (is_partial_uint_bijection(vertex2maybe_fvertex, fvertex2vertex)
            , lambda: f'not is_partial_uint_bijection(vertex2maybe_fvertex, fvertex2vertex)'
            )

        # since ugraph_fake_embedding =
        #   (hedge2fake_clockwise_next_hedge_around_vertex
        #   ,hedge2another_hedge
        #   )
        # we will verify: hedge2fvertex, hedge2another_hedge()

        #hedge2vertex vs hedge2fvertex
        hedge2vertex = ugraph_basic.hedge2vertex
        hedge2fvertex = ugraph_fake_embedding.hedge2fvertex
        yield (len(hedge2vertex) == len(hedge2fvertex)
            , 'len(hedge2vertex) != len(hedge2fvertex)'
            )
        yield (all(fvertex2vertex[fvertex] == vertex
                for vertex, fvertex in zip(hedge2vertex, hedge2fvertex)
                )
            , 'exist hedge. fvertex2vertex[hedge2fvertex[hedge]] != hedge2vertex[hedge]'
            )

        #hedge2another_hedge() vs hedge2another_hedge[]
        hedge2another_hedge = ugraph_basic.hedge2another_hedge
        hedge2another_hedge_func = ugraph_fake_embedding.hedge2another_hedge
        yield (all(hedge2another_hedge_func(hedge) == other
                for hedge, other in enumerate(hedge2another_hedge)
                )
            , 'exist hedge. hedge2another_hedge(hedge) != hedge2another_hedge[hedge]'
            )



if __name__ == "__main__":
    from .UGraph import UGraph
        # nn_ns.graph2.concrete_graph.ugraph__uint.UGraph instead of __main__.UGraph

    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


