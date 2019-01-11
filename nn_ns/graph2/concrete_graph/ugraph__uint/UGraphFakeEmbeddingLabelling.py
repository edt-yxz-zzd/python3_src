
__all__ = '''
    UGraphFakeEmbeddingLabelling
    VerifyUGraphFakeEmbeddingLabelling
    '''.split()


from .UIntBijection import UIntBijection
from seed.types.StructBase import StructBase
from seed.helper.repr_input import repr_helper_ex
from seed.verify.common_verify import has_attrs
from seed.verify.VerifyType import VerifyType__static


class UGraphFakeEmbeddingLabelling(StructBase):
    '''

methods:
    make_UGraphFakeEmbeddingLabelling__from_new2old_mappings
    make_UGraphFakeEmbeddingLabelling__from_old2new_mappings
    make_UGraphFakeEmbeddingLabelling__from_new2old_bijections
    make_UGraphFakeEmbeddingLabelling__from_old2new_bijections
    to_reversal_ugraph_labelling

'''
    all_UGraphFakeEmbeddingLabelling_attr_seq = '''
        old_fvertex2new_fvertex
        old_hedge2new_hedge
        old_fface2new_fface
        '''.split()
    all_UGraphFakeEmbeddingLabelling_attr_set = frozenset(
        all_UGraphFakeEmbeddingLabelling_attr_seq)
    all_UGraphFakeEmbeddingLabelling_primekey_attr_seq = tuple(
        all_UGraphFakeEmbeddingLabelling_attr_seq)


    @classmethod
    def make_UGraphFakeEmbeddingLabelling__from_new2old_mappings(cls, *
        ,new_fvertex2old_fvertex
        ,new_hedge2old_hedge
        ,new_fface2old_fface
        ):
        mk = UIntBijection.make_UIntBijection__from_backward_mapping
        old_fvertex2new_fvertex = mk(new_fvertex2old_fvertex)
        old_hedge2new_hedge = mk(new_hedge2old_hedge)
        old_fface2new_fface = mk(new_fface2old_fface)
        return cls.make_UGraphFakeEmbeddingLabelling__from_old2new_bijections(
            old_fvertex2new_fvertex=old_fvertex2new_fvertex
            ,old_hedge2new_hedge=old_hedge2new_hedge
            ,old_fface2new_fface=old_fface2new_fface
            )

    @classmethod
    def make_UGraphFakeEmbeddingLabelling__from_old2new_mappings(cls, *
        ,old_fvertex2new_fvertex
        ,old_hedge2new_hedge
        ,old_fface2new_fface
        ):
        mk = UIntBijection.make_UIntBijection__from_forward_mapping
        old_fvertex2new_fvertex = mk(old_fvertex2new_fvertex)
        old_hedge2new_hedge = mk(old_hedge2new_hedge)
        old_fface2new_fface = mk(old_fface2new_fface)
        return cls.make_UGraphFakeEmbeddingLabelling__from_old2new_bijections(
            old_fvertex2new_fvertex=old_fvertex2new_fvertex
            ,old_hedge2new_hedge=old_hedge2new_hedge
            ,old_fface2new_fface=old_fface2new_fface
            )


    @classmethod
    def make_UGraphFakeEmbeddingLabelling__from_new2old_bijections(cls, *
        ,new_fvertex2old_fvertex
        ,new_hedge2old_hedge
        ,new_fface2old_fface
        ):
        old_fvertex2new_fvertex = ~new_fvertex2old_fvertex
        old_hedge2new_hedge = ~new_hedge2old_hedge
        old_fface2new_fface = ~new_fface2old_fface
        return cls.make_UGraphFakeEmbeddingLabelling__from_old2new_bijections(
            old_fvertex2new_fvertex=old_fvertex2new_fvertex
            ,old_hedge2new_hedge=old_hedge2new_hedge
            ,old_fface2new_fface=old_fface2new_fface
            )

    @classmethod
    def make_UGraphFakeEmbeddingLabelling__from_old2new_bijections(cls, *
        ,old_fvertex2new_fvertex
        ,old_hedge2new_hedge
        ,old_fface2new_fface
        ):
        return cls(
            old_fvertex2new_fvertex=old_fvertex2new_fvertex
            ,old_hedge2new_hedge=old_hedge2new_hedge
            ,old_fface2new_fface=old_fface2new_fface
            )

    def __init__(self, *
        ,old_fvertex2new_fvertex
        ,old_hedge2new_hedge
        ,old_fface2new_fface
        ):
        self.old_fvertex2new_fvertex = old_fvertex2new_fvertex
        self.old_hedge2new_hedge = old_hedge2new_hedge
        self.old_fface2new_fface = old_fface2new_fface

        assert self.verify_UGraphFakeEmbeddingLabelling(AssertionError)

    @property
    def num_ffaces(self):
        return len(old_fface2new_fface.forward_mapping)
    @property
    def num_hedges(self):
        return len(old_hedge2new_hedge.forward_mapping)
    @property
    def num_fvertices(self):
        return len(old_fvertex2new_fvertex.forward_mapping)

    def verify_UGraphFakeEmbeddingLabelling(self, __mkError=None):
        return VerifyUGraphFakeEmbeddingLabelling(self, __mkError)

    def verify(self, __mkError=None):
        return self.verify_UGraphFakeEmbeddingLabelling(__mkError)


    def to_reversal_ugraph_labelling(self):
        cls = type(self)
        return cls.make_UGraphFakeEmbeddingLabelling__from_new2old_bijections(
                    new_fvertex2old_fvertex=self.old_fvertex2new_fvertex
                    ,new_hedge2old_hedge=self.old_hedge2new_hedge
                    ,new_fface2old_fface=self.old_fface2new_fface
                    )
    def __inv__(self):
        return self.to_reversal_ugraph_labelling()


    """
    def __repr__(self):
        all_UGraphFakeEmbeddingLabelling_attr_seq = __class__.all_UGraphFakeEmbeddingLabelling_attr_seq
        assert len(self.__dict__)-0 == len(all_UGraphFakeEmbeddingLabelling_attr_seq)
        return repr_helper_ex(self, (), all_UGraphFakeEmbeddingLabelling_attr_seq, {}, ordered_attrs_only=True)
    """

    @classmethod
    def __iter_all_primekey_attrs__(cls):
        yield from cls.all_UGraphFakeEmbeddingLabelling_primekey_attr_seq
        yield from super().__iter_all_primekey_attrs__()
    @classmethod
    def __iter_all_user_attrs__(cls):
        yield from cls.all_UGraphFakeEmbeddingLabelling_attr_seq
        yield from super().__iter_all_user_attrs__()
    @classmethod
    def __iter_all_impl_attrs__(cls):
        yield from cls.all_UGraphFakeEmbeddingLabelling_attr_seq
        #yield 'calc'
        yield from super().__iter_all_impl_attrs__()
    """
    @classmethod
    def __iter_all_cached_attr_calc_pairs__(cls):
        yield from super().__iter_all_cached_attr_calc_pairs__()
    """





class VerifyUGraphFakeEmbeddingLabelling(VerifyType__static):
    types = UGraphFakeEmbeddingLabelling
    def _iter_verify_object_(_, obj):
        # -> Iter (bool, err_msg_or_f)
        attrs = UGraphFakeEmbeddingLabelling.all_UGraphFakeEmbeddingLabelling_attr_seq

        yield (has_attrs(obj, attrs=attrs)
            , lambda: f'missing some attrs: {attrs!r}'
            )

        for attr in attrs:
            value = getattr(obj, attr)
            yield (isinstance(value, UIntBijection)
                , lambda:f'{attr} is not UIntBijection: {value!r}')

        old_fvertex2new_fvertex = obj.old_fvertex2new_fvertex
        old_hedge2new_hedge = obj.old_hedge2new_hedge
        old_fface2new_fface = obj.old_fface2new_fface

        num_fvertices = len(old_fvertex2new_fvertex.forward_mapping)
        num_hedges = len(old_hedge2new_hedge.forward_mapping)
        num_ffaces = len(old_fface2new_fface.forward_mapping)

        yield (num_fvertices <= num_hedges
            , lambda:f'{num_fvertices} == num_fvertices > num_hedges == {num_hedges}'
            )
        yield (num_ffaces <= num_hedges
            , lambda:f'{num_ffaces} == num_ffaces > num_hedges == {num_hedges}'
            )


