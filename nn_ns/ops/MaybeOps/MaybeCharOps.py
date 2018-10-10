

__all__ = '''
    IMaybeCharOps
    MaybeCharOps
    theMaybeCharOps
    theMaybeUIntOps
    '''.split()

from ..IMaybeOps import IMaybeOps
from ..abc import override, not_implemented


def getNothing(ops):
    return type(ops).__getNothing__(ops)

class IMaybeCharOps(IMaybeOps):
    '''Maybe Char

assumptions:
    1) Nothing is immutable
    2) cmp Nothing with value/Nothing by __eq__

see NonBoxMaybeOps
    cmp Nothing with value/Nothing by 'is'


usage:
    MaybeCharOps('')
        for Maybe Char = ''|Char
    MaybeCharOps(-1)
        for Maybe UInt = -1|UInt
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
            raise ValueError('MaybeCharOps.mkJust(Nothing)')
        return value

    @override
    def mkNothing(ops):
        # () -> Nothing
        return getNothing(ops)          # apply assumption 1)

    @override
    def isNothing(ops, maybe):
        # Maybe value -> Bool
        return maybe == getNothing(ops) # apply assumption 2)

    @override
    def unsafe_unjust(ops, just):
        # Just value -> value
        # Nothing -> undefined
        return just



class MaybeCharOps(IMaybeCharOps):
    __slots__ = ('_Nothing',)
    def __init__(ops, immutable_Nothing):
        hash(immutable_Nothing)
        ops._Nothing = immutable_Nothing

    @override
    def __getNothing__(self):
        return self._Nothing

    @override
    def __eq__(ops, other):
        if not isinstance(other, __class__):
            return NotImplemented
        return ops._Nothing == other._Nothing
    @override
    def __hash__(ops):
        return hash((__class__, ops._Nothing))
theMaybeCharOps = MaybeCharOps('')
theMaybeUIntOps = MaybeCharOps(-1)

