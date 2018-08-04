
__all__ = ['IOps']

from collections.abc import Hashable
from .abc import not_implemented, ABC

class IOps(ABC):#(Hashable, ABC):
    '''base class for all IXXXOps

instance of IXXXOps must be hashable
    immutable
    __eq__


class IXXXOps(IXXXOps):
    def instance_readonly_method(ops, self:XXX, ...):
        # do not modify XXX
    def static_method(ops, ...):
        # no self in input
class IXXXOps__constructor(IXXXOps):
    def make_XXX_from_...(ops, ...):
        # -> XXX
        ...
class IXXXOps__imodify(IXXXOps__constructor|IXXXOps):
    # self may or may not immutable
    def instance_iwriteonly_method(ops, self:XXX, ...):
        # -> new_self:XXX
        # modify self and return self
        #   or do not modify self and make new XXX and return it
        #   # like __iadd__ for list/tuple
    def instance_iwrite_and_read_method(ops, self:XXX, ...):
        # -> (result, new_self:XXX)
        # modify self and return (read_result, self)
        #   or do not modify self and make new XXX and return (read_result, it)
        # why not (new_self, result)?
        #   since
        #       new_self = ops.instance_iwriteonly_method...
        #       result, new_self = ops.instance_iwrite_and_read_method...
        #       where "new_self = " are easy to search
class IXXXOps__modify(IXXXOps__constructor|IXXXOps):
    # self must be mutable
    def instance_modify_method(ops, self:XXX, ...):
        # -> result
        # modify self inplace

########## example:
class IStack(ABC):
    # stack<X>
    @classmethod
    def make_empty_stack(cls):
        # -> stack<X>
    def is_empty(self):
    def top(self):
        # -> X | raise KeyError
    def pop(self):
        # -> X | raise KeyError
    def push(self, x):
        # -> None
class IStackOps(IOps):
    def is_empty(ops, self):
    def top(ops, self):
        # -> X | raise KeyError
class IStackOps__constructor(IStackOps):
    def make_empty_stack(ops):
        # -> stack<X>
class IStackOps__imodify(IStackOps__constructor):
    def ipop(ops, self):
        # -> (X, new_self) | raise KeyError
    def ipush(ops, self, x):
        # -> new_self
class IStackOps__modify(IStackOps__constructor):
    def pop(ops, self):
        # -> X | raise KeyError
    def push(ops, self, x):
        # -> None

concrete stack data for IStackOps are:
    mutable stack: list
    immutable stack: stack<X> = () | (stack<X>, X)

'''
    __slots__ = ()



    #@final
    def __eq__(ops, other_ops):
        if type(other_ops) is not type(ops): return NotImplemented
        return ops.get_args_for_eq_hash() == other_ops.get_args_for_eq_hash()
        return ops.__eq == other_ops.__eq
    #@final
    def __hash__(ops):
        return hash((type(ops), ops.get_args_for_eq_hash()))
        return hash((type(ops), ops.__eq))
    @not_implemented
    def get_args_for_eq_hash(ops):
        ...

    '''
    @not_implemented
    def __eq__(self, other):
        return self is other
    @not_implemented
    def __hash__(self):
        return id(self)
    '''

    def __ne__(self, other):
        return not (self == other)
Hashable.register(IOps)
assert issubclass(IOps, Hashable)


