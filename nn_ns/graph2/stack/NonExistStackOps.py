__all__ = '''
    theNonExistStackOps
    theSizedNonExistStackOps
    '''.split()
from .IStackOps import IStackOps__factory, ISizedStackOps
from .IMutableStackOps import IMutableOutputViewStackOps
from ..wrapper.Wrapper import Wrapper
from .StackOpsCommon import (
    EmptyStackError
    ,PopEmptyStackErrorForRaise
    )

class NonExistStackOps(IMutableOutputViewStackOps, IStackOps__factory):
    # assume stack is None
    __slots__ = ()
    def from_iterable(self, iterable):
        return None
    def push(self, s, x):
        # after push, stack may or may not be empty
        pass
    def pop_None(self, s):
        # pop_None :: stack -> None
        # if stack is empty, pop_None may or maynot raise
        pass
theNonExistStackOps = NonExistStackOps()



class SizedNonExistStackOps(
        IMutableOutputViewStackOps, ISizedStackOps, IStackOps__factory):
    # assume stack is Wrapper<uint>
    __slots__ = ()
    def from_iterable(self, iterable):
        size = 0
        for size, _ in enumerate(iterable):pass
        return Wrapper(size)
    def push(self, s, x):
        size = s.get_wrapped_obj()
        s.set_wrapped_obj(size+1)
    def pop_None(self, s):
        # pop_None :: stack -> None
        size = s.get_wrapped_obj()
        if size <= 0: raise PopEmptyStackErrorForRaise
        s.set_wrapped_obj(size-1)
    def len(self, s):
        return s.get_wrapped_obj()
theSizedNonExistStackOps = SizedNonExistStackOps()

