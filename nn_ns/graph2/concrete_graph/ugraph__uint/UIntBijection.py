
__all__ = '''
    UIntBijection
    VerifyUIntBijection
    '''.split()

from .is_uint_bijection import is_uint_bijection
from .inverse_uint_bijection import inverse_uint_bijection

from seed.helper.repr_input import repr_helper_ex
from seed.verify.common_verify import (
    is_UInt, is_Sequence, has_attrs
    )
from seed.verify.VerifyType import VerifyType__static


class UIntBijection:
    '''

methods:
    make_UIntBijection
    make_UIntBijection__from_forward_mapping
    make_UIntBijection__from_backward_mapping
    to_reversal_uint_bijection
'''
    all_UIntBijection_attr_seq = '''
        forward_mapping
        backward_mapping
        '''.split()
    all_UIntBijection_attr_set = frozenset(all_UIntBijection_attr_seq)


    @classmethod
    def make_UIntBijection(cls, *
        ,forward_mapping
        ,backward_mapping
        ):
        return cls(forward_mapping=forward_mapping, backward_mapping=backward_mapping)

    @classmethod
    def make_UIntBijection__from_forward_mapping(cls, *
        ,forward_mapping
        ):
        backward_mapping = inverse_uint_bijection(forward_mapping)
        return cls.make_UIntBijection(forward_mapping=forward_mapping, backward_mapping=backward_mapping)
    @classmethod
    def make_UIntBijection__from_backward_mapping(cls, *
        ,backward_mapping
        ):
        forward_mapping = inverse_uint_bijection(backward_mapping)
        return cls.make_UIntBijection(forward_mapping=forward_mapping, backward_mapping=backward_mapping)


    def __init__(self, *
        ,forward_mapping
        ,backward_mapping
        ):
        self.forward_mapping = forward_mapping
        self.backward_mapping = backward_mapping

        assert self.verify_UIntBijection(AssertionError)
    def verify_UIntBijection(self, __mkError=None):
        return VerifyUIntBijection(self, __mkError)

    def verify(self, __mkError=None):
        return self.verify_UIntBijection(__mkError)


    def __repr__(self):
        all_UIntBijection_attr_seq = __class__.all_UIntBijection_attr_seq
        assert len(self.__dict__)-0 == len(all_UIntBijection_attr_seq)
        return repr_helper_ex(self, (), all_UIntBijection_attr_seq, {}, ordered_attrs_only=True)


    def to_reversal_uint_bijection(self):
        cls = type(self)
        return cls.make_UIntBijection(
                    forward_mapping=self.backward_mapping
                    ,backward_mapping=self.forward_mapping
                    )
    def __inv__(self):
        return self.to_reversal_uint_bijection()

class VerifyUIntBijection(VerifyType__static):
    types = UIntBijection
    def _iter_verify_object_(_, obj):
        # -> Iter (bool, err_msg_or_f)
        def is_uint_seq(obj):
            return is_Sequence.of(obj, is_UInt)
        attrs = UIntBijection.all_UIntBijection_attr_seq

        yield (has_attrs(obj, attrs=attrs)
            , lambda: f'missing some attrs: {attrs!r}'
            )

        for attr in attrs:
            value = getattr(obj, attr)
            yield (is_uint_seq(value)
                , lambda:f'{attr} is not UInt sequence: {value!r}')

        forward_mapping = obj.forward_mapping
        backward_mapping = obj.backward_mapping

        yield (is_uint_bijection(forward_mapping, backward_mapping)
            , lambda:f'not is_uint_bijection(forward_mapping={forward_mapping!r}, backward_mapping={backward_mapping!r})'
            )


