
__all__ = ['NonBoxMaybeOps']
from ..IMaybeOps import IMaybeOps
from ..abc import override, not_implemented


def getNothing(ops):
    return type(ops).__getNothing__(ops)


class INonBoxMaybeOps(IMaybeOps):
    '''Nothing|value; where value is not Nothing

not a general Maybe implement!

assumptions:
    1) unique Nothing

usage:
    NonBoxMaybeOps(None)
    NonBoxMaybeOps(object())
anti-usage:
    MaybeCharOps = '' | '<char>'
    MaybeUIntOps = -1 | UInt
    # since cmp Nothing using "is"
    #   , '' or -1 is not unique object

'''
    __slots__ = ()

    @not_implemented
    def __getNothing__(self):
        # -> Nothing
        raise NotImplementedError

    @override
    def mkJust(ops, value):
        # value -> Just value
        if ops.isNothing(value):
            raise ValueError('NonBoxMaybeOps.mkJust(Nothing)')
        return value

    @override
    def mkNothing(ops):
        # () -> Nothing
        return getNothing(ops)          # apply assumptions 1)

    @override
    def isNothing(ops, maybe):
        # Maybe value -> Bool
        return maybe is getNothing(ops) # apply assumptions 1)

    @override
    def unsafe_unjust(ops, just):
        # Just value -> value
        # Nothing -> undefined
        return just

class NonBoxMaybeOps(IMaybeOps):
    __slots__ = ('_Nothing',)

    def __init__(ops, Nothing):
        ops._Nothing = Nothing

    @override
    def __getNothing__(self):
        return self._Nothing

    @override
    def __eq__(ops, other):
        if isinstance(other, __class__):
            return ops._Nothing is other._Nothing
        return NotImplemented
    @override
    def __hash__(ops):
        return hash((__class__, id(ops._Nothing)))



