
__all__ = ['NonBoxMaybeOps']
from ..IMaybeOps import IMaybeOps
from ..abc import override

class NonBoxMaybeOps(IMaybeOps):
    '''Nothing|value; where value is not Nothing

not a general Maybe implement!

unique Nothing
usage:
    NonBoxMaybeOps(None)
    NonBoxMaybeOps(object())
anti-usage:
    MaybeCharOps = '' | '<char>'
    MaybeUIntOps = -1 | UInt
    # since cmp Nothing using "is"
    #   , '' or -1 is not unique object

'''
    def __init__(ops, Nothing):
        ops._Nothing = Nothing

    @override
    def mkJust(ops, value):
        # value -> Just value
        if ops.isNothing(value):
            raise ValueError('NonBoxMaybeOps.mkJust(Nothing)')
        return value

    @override
    def mkNothing(ops):
        # () -> Nothing
        return ops._Nothing

    @override
    def isNothing(ops, maybe):
        # Maybe value -> Bool
        return maybe is ops._Nothing

    @override
    def unsafe_unjust(ops, just):
        # Just value -> value
        # Nothing -> undefined
        return just

    def __eq__(ops, other):
        if isinstance(other, __class__):
            return ops._Nothing is other._Nothing
        return NotImplemented
    def __hash__(ops):
        return hash((__class__, id(ops._Nothing)))



