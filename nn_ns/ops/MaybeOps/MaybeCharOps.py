

__all__ = '''
    MaybeCharOps
    theMaybeCharOps
    theMaybeUIntOps
    '''.split()

from ..IMaybeOps import IMaybeOps
from ..abc import override

class MaybeCharOps(IMaybeOps):
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
    def __init__(ops, immutable_Nothing):
        hash(immutable_Nothing)
        ops._Nothing = immutable_Nothing
    @override
    def mkJust(ops, value):
        # value -> Just value
        if ops.isNothing(value):
            raise ValueError('MaybeCharOps.mkJust(Nothing)')
        return value

    @override
    def mkNothing(ops):
        # () -> Nothing
        return ops._Nothing            # apply assumption 1)

    @override
    def isNothing(ops, maybe):
        # Maybe value -> Bool
        return maybe == ops._Nothing    # apply assumption 2)

    @override
    def unsafe_unjust(ops, just):
        # Just value -> value
        # Nothing -> undefined
        return just


    def __eq__(ops, other):
        if not isinstance(other, __class__):
            return NotImplemented
        return ops._Nothing == other._Nothing
    def __hash__(ops):
        return hash((__class__, ops._Nothing))

theMaybeCharOps = MaybeCharOps('')
theMaybeUIntOps = MaybeCharOps(-1)

