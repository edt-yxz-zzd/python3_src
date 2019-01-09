


__all__ = '''
    UGraphBasic
    VerifyUGraphBasic
    '''.split()

from .make_hedge2another_hedge import make_hedge2another_hedge
from .make_vertex2degree import make_vertex2degree
from .is_uint_bijection import is_uint_bijection_without_self_reflect

from seed.helper.repr_input import repr_helper_ex
from seed.verify.common_verify import (
    is_UInt, is_Sequence, has_attrs
    )
from seed.verify.VerifyType import VerifyType__static





class UGraphBasic:
    all_UGraphBasic_attr_seq = '''
        num_vertices
        num_aedges
        num_hedges
        hedge2vertex
        hedge2aedge
        hedge2another_hedge
        vertex2degree
        '''.split()
    all_UGraphBasic_attr_set = frozenset(all_UGraphBasic_attr_seq)


    @classmethod
    def make_UGraphBasic__simplest(cls, *
        ,num_vertices
        ,hedge2vertex
        ,hedge2aedge
        ):
        hedge2another_hedge = make_hedge2another_hedge.from_hedge2aedge(hedge2aedge=hedge2aedge)
        vertex2degree = make_vertex2degree.from_hedge2vertex(num_vertices=num_vertices, hedge2vertex=hedge2vertex)
        return cls.make_UGraphBasic__simpler(
            hedge2vertex=hedge2vertex
            ,hedge2aedge=hedge2aedge
            ,hedge2another_hedge=hedge2another_hedge
            ,vertex2degree=vertex2degree
            )

    @classmethod
    def make_UGraphBasic__simpler(cls, *
        ,hedge2vertex
        ,hedge2aedge
        ,hedge2another_hedge
        ,vertex2degree
        ):
        num_vertices = len(vertex2degree)
        num_hedges = len(hedge2vertex)
        num_aedges = num_hedges // 2
        return cls(
            num_vertices=num_vertices
            ,num_aedges=num_aedges
            ,num_hedges=num_hedges
            ,hedge2vertex=hedge2vertex
            ,hedge2aedge=hedge2aedge
            ,hedge2another_hedge=hedge2another_hedge
            ,vertex2degree=vertex2degree
            )
    def __init__(self, *
        ,num_vertices
        ,num_aedges
        ,num_hedges
        ,hedge2vertex
        ,hedge2aedge
        ,hedge2another_hedge
        ,vertex2degree
        ):

        self.num_vertices = num_vertices
        self.num_aedges = num_aedges
        self.num_hedges = num_hedges
        self.hedge2vertex = hedge2vertex
        self.hedge2aedge = hedge2aedge
        self.hedge2another_hedge = hedge2another_hedge
        self.vertex2degree = vertex2degree

        #self.calc = 
        assert self.verify_UGraphBasic(AssertionError)
    def verify_UGraphBasic(self, __mkError=None):
        return VerifyUGraphBasic(self, __mkError)

    def verify(self, __mkError=None):
        return self.verify_UGraphBasic(__mkError)

    def __repr__(self):
        all_UGraphBasic_attr_seq = __class__.all_UGraphBasic_attr_seq
        assert len(self.__dict__)-0 == len(all_UGraphBasic_attr_seq)
        #assert len(self.__dict__)-1 == len(all_UGraphBasic_attr_seq)
            # exclude 'calc'
        return repr_helper_ex(self, (), all_UGraphBasic_attr_seq, {}, ordered_attrs_only=True)



class VerifyUGraphBasic(VerifyType__static):
    types = UGraphBasic
    def _iter_verify_object_(_, obj):
        # -> Iter (bool, err_msg_or_f)
        def is_uint_seq(obj):
            return is_Sequence.of(obj, is_UInt)
        attrs = UGraphBasic.all_UGraphBasic_attr_seq

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




        num_vertices = obj.num_vertices
        num_aedges = obj.num_aedges
        num_hedges = obj.num_hedges

        yield (num_hedges == num_aedges*2
            , lambda:f'{num_hedges} == num_hedges != num_aedges*2 == {num_aedges}*2'
            )




        hedge2vertex = obj.hedge2vertex
        hedge2aedge = obj.hedge2aedge
        hedge2another_hedge = obj.hedge2another_hedge
        vertex2degree = obj.vertex2degree



        # verify len(XXX2YYY)

        yield (num_vertices == len(vertex2degree)
            , lambda:f'{num_vertices} == num_vertices != len(vertex2degree) == {len(vertex2degree)}'
            )

        attrs__hedge2XXX = (attr for attr in attrs if attr.startswith('hedge2'))
        for attr__hedge2XXX in attrs__hedge2XXX:
            hedge2XXX = getattr(obj, attr__hedge2XXX)
            len_hedge2XXX = len(hedge2XXX)
            yield (num_hedges == len_hedge2XXX
                , lambda:f'{num_hedges} == num_hedges != len({attr__hedge2XXX!s}) == {len_hedge2XXX!r}'
                )


        # verify max items
        pairs = [
            ('hedge2vertex', 'num_vertices')
            ,('hedge2aedge', 'num_aedges')
            ,('hedge2another_hedge', 'num_hedges')
            #,('vertex2degree', 'num_vertices')
            ]
        for attr__hedge2XXX, attr__num_XXXs in pairs:
            hedge2XXX = getattr(obj, attr__hedge2XXX)
            num_XXXs = getattr(obj, attr__num_XXXs)
            yield (max(hedge2XXX, default=-1) < num_XXXs
                , lambda:f'not max({attr__hedge2XXX!s}) < {attr__num_XXXs!s}: max({hedge2XXX!r}) >= {num_XXXs!r}'
                )


        # verify vertex2degree
        yield (sum(vertex2degree) == num_hedges
            , lambda:f'sum(vertex2degree) != num_hedges'
            )

        # verify vertex2degree & hedge2vertex
        vertex2degree_ = make_vertex2degree.from_hedge2vertex(num_vertices=num_vertices, hedge2vertex=hedge2vertex)
        yield (all(d==d_ for d, d_ in zip(vertex2degree, vertex2degree_))
            , lambda:f'hedge2vertex & vertex2degree: wrong vertex degree'
            )


        # verify hedge2aedge
        aedge2degree_ = make_vertex2degree.from_hedge2vertex(num_vertices=num_aedges, hedge2vertex=hedge2aedge)
        yield (all(d_==2 for d_ in aedge2degree_)
            , lambda:f'hedge2aedge: wrong aedge degree'
            )


        #verify hedge2another_hedge
        yield (is_uint_bijection_without_self_reflect(hedge2another_hedge, hedge2another_hedge)
            , lambda:f'hedge2another_hedge is not uint_bijection without self_reflect: {hedge2another_hedge!r}'
            )


        # verify hedge2aedge & hedge2another_hedge
        hedge2another_hedge_ = make_hedge2another_hedge.from_hedge2aedge(hedge2aedge=hedge2aedge)
        yield (all(h==h_ for h, h_ in zip(hedge2another_hedge, hedge2another_hedge_))
            , lambda:f'hedge2aedge & hedge2another_hedge: wrong hedge reversal'
            )


