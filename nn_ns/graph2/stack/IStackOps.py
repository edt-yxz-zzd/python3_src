


__all__ = '''
    IStackOps__factory
    ISizedStackOps
    IStackOps__reversed

IStackOpsBase
    IStackOps__factory
    IStackOps__is_empty
        ISizedStackOps
        IStackOps__top_raise
            IStackOps__reversed



    '''.split()

from .StackOpsCommon import (
    EmptyStackError, TopEmptyStackErrorForRaise
    ,ABC, abstractmethod

    ,obj_classmethod
    ,obj_constructor
    ,instance_const_method
    ,echo, null_iter
    )
# TODO: add __slots__ = ()


# const ops
#   shared by both mutable and immutable

class IStackOpsBase(ABC):
    __slots__ = ()
class IStackOps__factory(IStackOpsBase):
    # `from_iterable
    __slots__ = ()

    @obj_constructor
    def make_empty_stack(self):
        # make_empty_stack :: () -> s
        return self.from_iterable(null_iter)
        pass
    @obj_constructor
    @abstractmethod
    def from_iterable(self, iterable):
        # from_iterable :: Iter x -> s
        pass
class IStackOps__is_empty(IStackOpsBase):
    # `is_empty
    __slots__ = ()
    @instance_const_method
    @abstractmethod
    def is_empty(self, s):
        # is_empty :: s -> bool
        pass

class ISizedStackOps(IStackOps__is_empty):
    # is_empty, `len
    __slots__ = ()
    @instance_const_method
    @abstractmethod
    def len(self, s):
        # len :: s -> int
        pass
    @instance_const_method
    def is_empty(self, s):
        # is_empty :: s -> bool
        # bug:return bool(self.len(s))
        return not self.len(s)

class IStackOps__top_raise(IStackOps__is_empty):
    # top empty stack then raise
    #
    # `is_empty, `top, top_or_fdefault
    __slots__ = ()

    # is_empty = top() success
    @instance_const_method
    @abstractmethod
    def top(self, s):
        # top :: s -> x
        # top empty stack then raise
        pass
    @instance_const_method
    def top_or_fdefault(self, s, fdefault, wrap=echo):
        # top_or_fdefault :: s -> (()->r) -> (x->y) -> (y|r)
        if self.is_empty(s):
            return fdefault()
        return echo(self.top())


class IStackOps__reversed(IStackOps__top_raise):
    # is_empty, top, top_or_fdefault, `reversed
    @instance_const_method
    @abstractmethod
    def reversed(self, s):
        # reversed :: s -> Iter x
        pass

    @instance_const_method
    @abstractmethod
    def is_empty(self, s):
        # is_empty :: s -> bool
        for _ in self.reversed(s):
            return False
        else:
            return True

    @instance_const_method
    def top(self, s):
        # top :: s -> x
        # top empty stack then raise
        for x in self.reversed(s):
            return x
        else:
            raise TopEmptyStackErrorForRaise

        pass









