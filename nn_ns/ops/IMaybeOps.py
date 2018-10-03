
__all__ = ['IMaybeOps']
from .abc import ABC, abstractmethod, override, not_implemented, ABCMeta

class IMaybeOps:
    '''
use cases:
    for value in ops.iter(maybe):
        ...
        break
    else:
        ...
'''
    @not_implemented
    def mkJust(ops, value):
        # value -> Just value
        raise NotImplementedError

    @not_implemented
    def mkNothing(ops):
        # () -> Nothing
        # why mkNothing not getNothing?
        #   since the actual Maybe object may mutable
        raise NotImplementedError

    @not_implemented
    def isNothing(ops, maybe):
        # Maybe value -> Bool
        raise NotImplementedError

    @not_implemented
    def unsafe_unjust(ops, just):
        # Just value -> value
        # Nothing -> undefined
        raise NotImplementedError

    def unjust(ops, maybe):
        if ops.isNothing(maybe):
            raise ValueError('unjust(Nothing)')
        return ops.unsafe_unjust(maybe)
    def to_std_maybe(ops, maybe):
        # Just value -> (value,)
        # Nothing -> ()
        if ops.isNothing(maybe):
            return ()
        return (ops.unsafe_unjust(maybe),)
    def iter(ops, maybe):
        if not ops.isNothing(maybe):
            yield ops.unsafe_unjust(maybe)
        return

    def maybe_eq(ops, maybe0, maybe1):
        if ops.isNothing(maybe0):
            return ops.isNothing(maybe1)
        if ops.isNothing(maybe1):
            return False
        return ops.unsafe_unjust(maybe0) == ops.unsafe_unjust(maybe1)

    def fmap(ops, maybe, f):
        if ops.isNothing(maybe):
            return ops.mkNothing()
        value = ops.unsafe_unjust(maybe)
        return ops.mkJust(f(value))

    def mkMaybe(ops, to_mk_just:bool, f_value:'()->value'):
        return ops.mkNothing() if not to_mk_just else ops.mkJust(f_value())


