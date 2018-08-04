




__all__ = '''
    IStackOps__factory
    ISizedStackOps
    IStackOps__reversed
    IMutableTopStackOps

IStackOpsBase
    IStackOps__factory
        IMutableCompleteStackOps
    IStackOps__is_empty
        ISizedStackOps
            IMutableSizedTopStackOps
        IStackOps__top_raise
            IStackOps__reversed
            IMutableTopStackOps

    IMutableStackOpsBase
        IMutableOutputStackOps
            IMutableOutputViewStackOps
        IMutableStackOps__pop_None
            IMutableOutputViewStackOps
                IMutableStackOps
            IMutableInputStackOps
                IMutableStackOps
                    IMutableTopStackOps
                        IMutableSizedTopStackOps
                            IMutableCompleteStackOps

    '''.split()
from .StackOpsCommon import (
    EmptyStackError
    ,ABC, abstractmethod

    ,instance_const_method
    ,instance_inplace_eval
    ,instance_inplace_stmt
    ,echo
    )
from .IStackOps import (
    IStackOpsBase
        ,IStackOps__factory
        ,IStackOps__is_empty
            ,ISizedStackOps
            ,IStackOps__top_raise
                ,IStackOps__reversed
    )

# TODO: add __slots__ = ()



class IMutableStackOpsBase(IStackOpsBase):
    __slots__ = ()
class IMutableOutputStackOps(IMutableStackOpsBase):
    # user side
    #   e.g. used as type of output arg of api
    #   e.g. wrapper for non-exist stack
    __slots__ = ()

    @instance_inplace_stmt
    @abstractmethod
    def push(self, ms, x):
        # push :: ms -> x -> None
        # after push, stack may or may not be empty
        pass



class IMutableStackOps__pop_None(IMutableStackOpsBase):
    # if stack is empty, pop_None may or maynot raise
    @instance_inplace_stmt
    @abstractmethod
    def pop_None(self, ms):
        # pop_None :: ms -> None
        # if stack is empty, pop_None may or maynot raise
        pass

class IMutableOutputViewStackOps(IMutableStackOps__pop_None, IMutableOutputStackOps):
    # `pop_None, `push
    __slots__ = ()
class IMutableInputStackOps(IMutableStackOps__pop_None):
    # user side
    #   e.g. used as type of input arg of api
    # should use iterable instead
    #
    # pop_None, `pop
    __slots__ = ()
    @instance_inplace_eval
    @abstractmethod
    def pop(self, ms):
        # pop :: ms -> x
        # if stack is empty, pop may or maynot raise
        #   e.g. return default value
        pass
    @instance_inplace_stmt
    def pop_None(self, ms):
        # pop_None :: ms -> None
        # if stack is empty, pop_None may or maynot raise
        self.pop(ms)


class IMutableStackOps(IMutableInputStackOps, IMutableOutputViewStackOps):
    # data structure side
    #   e.g. what the actually underlying data structure can offer
    # after push, stack may or may not be empty
    # pop empty stack, may or maynot raise
    #
    # pop_None, `pop, `push
    __slots__ = ()

class IMutableTopStackOps(IMutableStackOps, IStackOps__top_raise):
    # after push, stack should not be empty
    # pop empty stack then raise
    # top empty stack then raise
    #
    # `is_empty, `top, top_or_fdefault, pop_None, `pop, `push, pop_or_fdefault
    __slots__ = ()
    '''
    @instance_const_method
    @abstractmethod
    def is_empty(self, ms):
        # is_empty :: ms -> bool
        try:
            x = self.pop(ms)
        except EmptyStackError:
            return True
        self.push(ms, x)
        return False
        pass
    '''
    @instance_const_method
    @abstractmethod
    def top(self, ms):
        # top :: ms -> x
        # top empty stack then raise
        x = self.pop()
        self.push(x)
        return x

    @instance_inplace_eval
    def pop_or_fdefault(self, ms, fdefault, wrap=echo):
        # pop_or_fdefault :: ms -> (()->r) -> (x->y) -> (y|r)
        if self.is_empty(ms):
            return fdefault()
        return wrap(self.pop())

class IMutableSizedTopStackOps(IMutableTopStackOps, ISizedStackOps):
    # after push, stack should not be empty
    # pop empty stack then raise
    # top empty stack then raise
    #
    # is_empty, `top, top_or_fdefault, pop_None, `pop, `push, pop_or_fdefault
    #   `len
    __slots__ = ()
    is_empty = ISizedStackOps.is_empty
    '''
    @instance_const_method
    def is_empty(self, ms):
        # is_empty :: ms -> bool
        return bool(self.len(ms))
    '''
class IMutableCompleteStackOps(
        IMutableSizedTopStackOps
        , IStackOps__reversed
        , ISizedStackOps
        , IStackOps__factory):
    # after push, stack should not be empty
    # pop empty stack then raise
    # top empty stack then raise
    #
    # is_empty, `top, top_or_fdefault, pop_None, `pop, `push, pop_or_fdefault;
    #   `len; `from_iterable
    __slots__ = ()
    is_empty = ISizedStackOps.is_empty
    pass

