
__all__ = '''
    VerifyContainer
    VerifyContainerType
    '''.split()

from .VerifyType import VerifyType, VerifyType__static
class VerifyContainer(VerifyType):
    def __init__(self, types, element_verifier):
        # types :: type | tuple<types>
        # element_verifier :: Verify | element -> bool
        self.element_verifier = element_verifier
        super().__init__(types)
    def _iter_verify_object_(self, obj):
        element_verifier = self.element_verifier
        #maybe_mkError = self.maybe_mkError
        for element in obj:
            b = element_verifier(element) # maybe_mkError
            yield b, lambda: 'not {!r}: {!r}'.format(element_verifier, element)
        yield from super()._iter_verify_object_(obj)

class VerifyContainerType(VerifyType__static):
    @classmethod
    def of_type(cls, __obj, __types, __mkError=None):
        return cls.of(__obj, lambda x: isinstance(x, __types), __mkError)
    @classmethod
    def of(cls, __obj, element_verifier, __mkError=None):
        # usage: is_sorted_sequence.of(is_UInt)
        return (VerifyContainer(
                    __obj, __mkError
                    , types=cls.types, element_verifier=element_verifier
                    )
                and cls(__obj, __mkError)
                )

        #### should verify element first!!
        return (cls(__obj, __mkError)
            and VerifyContainer(
                __obj, __mkError
                , types=cls.types, element_verifier=element_verifier
                )
            )


