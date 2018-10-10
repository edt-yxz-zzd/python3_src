
__all__ = '''
    StdMaybeOps
    theStdMaybeOps
    '''.split()

from ..IMaybeOps import IMaybeOps
from ..abc import override

class StdMaybeOps(IMaybeOps):
    '()|(value,)'
    __slots__ = ()

    @override
    def mkJust(ops, value):
        # value -> Just value
        return (value,)

    @override
    def mkNothing(ops):
        # () -> Nothing
        return ()

    @override
    def isNothing(ops, maybe):
        # Maybe value -> Bool
        return not maybe

    @override
    def unsafe_unjust(ops, just):
        # Just value -> value
        # Nothing -> undefined
        [value] = just
        return value

    @override
    def to_std_maybe(ops, maybe):
        # Just value -> (value,)
        # Nothing -> ()
        return maybe


    @override
    def __eq__(ops, other):
        if isinstance(other, __class__):
            return True
        return NotImplemented
    @override
    def __hash__(ops):
        return hash(__class__)

theStdMaybeOps = StdMaybeOps()

