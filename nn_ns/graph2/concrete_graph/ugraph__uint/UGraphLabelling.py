
__all__ = '''
    UGraphLabelling
    VerifyUGraphLabelling
    '''.split()


from .UIntBijection import UIntBijection
from seed.types.StructBase import StructBase
from seed.helper.repr_input import repr_helper_ex
from seed.verify.common_verify import has_attrs
from seed.verify.VerifyType import VerifyType__static


class UGraphLabelling(StructBase):
    '''

methods:
    make_UGraphLabelling__from_new2old_mappings
    make_UGraphLabelling__from_old2new_mappings
    make_UGraphLabelling__from_new2old_bijections
    make_UGraphLabelling__from_old2new_bijections
    to_reversal_ugraph_labelling

'''
    all_UGraphLabelling_attr_seq = '''
        old_vertex2new_vertex
        old_aedge2new_aedge
        old_hedge2new_hedge
        '''.split()
    all_UGraphLabelling_attr_set = frozenset(all_UGraphLabelling_attr_seq)
    all_UGraphLabelling_primekey_attr_seq = tuple(all_UGraphLabelling_attr_seq)


    @classmethod
    def make_UGraphLabelling__from_new2old_mappings(cls, *
        ,new_vertex2old_vertex
        ,new_aedge2old_aedge
        ,new_hedge2old_hedge
        ):
        mk = UIntBijection.make_UIntBijection__from_backward_mapping
        old_vertex2new_vertex = mk(new_vertex2old_vertex)
        old_aedge2new_aedge = mk(new_aedge2old_aedge)
        old_hedge2new_hedge = mk(new_hedge2old_hedge)
        return cls.make_UGraphLabelling__from_old2new_bijections(
            old_vertex2new_vertex=old_vertex2new_vertex
            ,old_aedge2new_aedge=old_aedge2new_aedge
            ,old_hedge2new_hedge=old_hedge2new_hedge
            )

    @classmethod
    def make_UGraphLabelling__from_old2new_mappings(cls, *
        ,old_vertex2new_vertex
        ,old_aedge2new_aedge
        ,old_hedge2new_hedge
        ):
        mk = UIntBijection.make_UIntBijection__from_forward_mapping
        old_vertex2new_vertex = mk(old_vertex2new_vertex)
        old_aedge2new_aedge = mk(old_aedge2new_aedge)
        old_hedge2new_hedge = mk(old_hedge2new_hedge)
        return cls.make_UGraphLabelling__from_old2new_bijections(
            old_vertex2new_vertex=old_vertex2new_vertex
            ,old_aedge2new_aedge=old_aedge2new_aedge
            ,old_hedge2new_hedge=old_hedge2new_hedge
            )


    @classmethod
    def make_UGraphLabelling__from_new2old_bijections(cls, *
        ,new_vertex2old_vertex
        ,new_aedge2old_aedge
        ,new_hedge2old_hedge
        ):
        old_vertex2new_vertex = ~new_vertex2old_vertex
        old_aedge2new_aedge = ~new_aedge2old_aedge
        old_hedge2new_hedge = ~new_hedge2old_hedge
        return cls.make_UGraphLabelling__from_old2new_bijections(
            old_vertex2new_vertex=old_vertex2new_vertex
            ,old_aedge2new_aedge=old_aedge2new_aedge
            ,old_hedge2new_hedge=old_hedge2new_hedge
            )

    @classmethod
    def make_UGraphLabelling__from_old2new_bijections(cls, *
        ,old_vertex2new_vertex
        ,old_aedge2new_aedge
        ,old_hedge2new_hedge
        ):
        return cls(
            old_vertex2new_vertex=old_vertex2new_vertex
            ,old_aedge2new_aedge=old_aedge2new_aedge
            ,old_hedge2new_hedge=old_hedge2new_hedge
            )

    def __init__(self, *
        ,old_vertex2new_vertex
        ,old_aedge2new_aedge
        ,old_hedge2new_hedge
        ):
        self.old_vertex2new_vertex = old_vertex2new_vertex
        self.old_aedge2new_aedge = old_aedge2new_aedge
        self.old_hedge2new_hedge = old_hedge2new_hedge

        assert self.verify_UGraphLabelling(AssertionError)

        '''
        assert isinstance(old_vertex2new_vertex, UIntBijection)
        assert isinstance(old_aedge2new_aedge, UIntBijection)
        assert isinstance(old_hedge2new_hedge, UIntBijection)
        assert self.num_hedges == self.num_aedges*2
        '''
    @property
    def num_hedges(self):
        return len(old_hedge2new_hedge.forward_mapping)
    @property
    def num_aedges(self):
        return len(old_aedge2new_aedge.forward_mapping)
    @property
    def num_vertices(self):
        return len(old_vertex2new_vertex.forward_mapping)

    def verify_UGraphLabelling(self, __mkError=None):
        return VerifyUGraphLabelling(self, __mkError)

    def verify(self, __mkError=None):
        return self.verify_UGraphLabelling(__mkError)



    def to_reversal_ugraph_labelling(self):
        cls = type(self)
        return cls.make_UGraphLabelling__from_new2old_bijections(
                    new_vertex2old_vertex=self.old_vertex2new_vertex
                    ,new_aedge2old_aedge=self.old_aedge2new_aedge
                    ,new_hedge2old_hedge=self.old_hedge2new_hedge
                    )
    def __inv__(self):
        return self.to_reversal_ugraph_labelling()



    """
    def __repr__(self):
        all_UGraphLabelling_attr_seq = __class__.all_UGraphLabelling_attr_seq
        assert len(self.__dict__)-0 == len(all_UGraphLabelling_attr_seq)
        return repr_helper_ex(self, (), all_UGraphLabelling_attr_seq, {}, ordered_attrs_only=True)
    """


    @classmethod
    def __iter_all_primekey_attrs__(cls):
        yield from cls.all_UGraphLabelling_primekey_attr_seq
        yield from super().__iter_all_primekey_attrs__()
    @classmethod
    def __iter_all_user_attrs__(cls):
        yield from cls.all_UGraphLabelling_attr_seq
        yield from super().__iter_all_user_attrs__()
    @classmethod
    def __iter_all_impl_attrs__(cls):
        yield from cls.all_UGraphLabelling_attr_seq
        #yield 'calc'
        yield from super().__iter_all_impl_attrs__()
    """
    @classmethod
    def __iter_all_cached_attr_calc_pairs__(cls):
        yield from super().__iter_all_cached_attr_calc_pairs__()
    """






class VerifyUGraphLabelling(VerifyType__static):
    types = UGraphLabelling
    def _iter_verify_object_(_, obj):
        # -> Iter (bool, err_msg_or_f)
        attrs = UGraphLabelling.all_UGraphLabelling_attr_seq

        yield (has_attrs(obj, attrs=attrs)
            , lambda: f'missing some attrs: {attrs!r}'
            )

        for attr in attrs:
            value = getattr(obj, attr)
            yield (isinstance(value, UIntBijection)
                , lambda:f'{attr} is not UIntBijection: {value!r}')

        old_vertex2new_vertex = obj.old_vertex2new_vertex
        old_aedge2new_aedge = obj.old_aedge2new_aedge
        old_hedge2new_hedge = obj.old_hedge2new_hedge

        num_vertices = len(old_vertex2new_vertex.forward_mapping)
        num_aedges = len(old_aedge2new_aedge.forward_mapping)
        num_hedges = len(old_hedge2new_hedge.forward_mapping)

        yield (num_hedges == num_aedges*2
            , lambda:f'{num_hedges} == num_hedges != num_aedges*2 == {num_aedges}*2'
            )

