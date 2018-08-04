



__all__ = '''
    IStackOps__factory
    ISizedStackOps
    IStackOps__reversed
    IPseudoImmutableTopStackOps

IStackOpsBase
    IStackOps__factory
        IPseudoImmutableCompleteStackOps
    IStackOps__is_empty
        ISizedStackOps
            IPseudoImmutableSizedTopStackOps
        IStackOps__top_raise
            IStackOps__reversed
            IPseudoImmutableTopStackOps

    IPseudoImmutableStackOpsBase
        IPseudoImmutableOutputStackOps
            IPseudoImmutableOutputViewStackOps
        IPseudoImmutableStackOps__pop_None
            IPseudoImmutableOutputViewStackOps
                IPseudoImmutableStackOps
            IPseudoImmutableInputStackOps
                IPseudoImmutableStackOps
                    IPseudoImmutableTopStackOps
                        IPseudoImmutableSizedTopStackOps
                            IPseudoImmutableCompleteStackOps

    '''.split()



from .StackOpsCommon import (
    EmptyStackError
    ,ABC, abstractmethod

    ,instance_const_method
    ,instance_pseudo_inplace_eval
    ,instance_pseudo_inplace_stmt
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

class IPseudoImmutableStackOpsBase(IStackOpsBase):
    __slots__ = ()
class IPseudoImmutableOutputStackOps(IPseudoImmutableStackOpsBase):
    # user side
    #   e.g. used as type of output arg of api
    #   e.g. wrapper for non-exist stack
    __slots__ = ()

    @instance_pseudo_inplace_stmt
    @abstractmethod
    def ipush(self, im, x):
        # ipush :: im -> x -> im
        # after ipush, stack may or may not be empty
        pass



class IPseudoImmutableStackOps__pop_None(IPseudoImmutableStackOpsBase):
    # if stack is empty, ipop_None may or maynot raise
    @instance_pseudo_inplace_stmt
    @abstractmethod
    def ipop_None(self, im):
        # ipop_None :: im -> im
        # if stack is empty, ipop_None may or maynot raise
        pass

class IPseudoImmutableOutputViewStackOps(IPseudoImmutableStackOps__pop_None, IPseudoImmutableOutputStackOps):
    # `ipop_None, `ipush
    __slots__ = ()
class IPseudoImmutableInputStackOps(IPseudoImmutableStackOps__pop_None):
    # user side
    #   e.g. used as type of input arg of api
    # should use iterable instead
    #
    # ipop_None, `ipop
    __slots__ = ()

    @instance_pseudo_inplace_eval
    @abstractmethod
    def ipop(self, im):
        # ipop :: im -> (im, x)
        # if stack is empty, ipop may or maynot raise
        #   e.g. return default value
        pass

    @instance_pseudo_inplace_stmt
    def ipop_None(self, im):
        # ipop_None :: im -> im
        # if stack is empty, ipop_None may or maynot raise
        im, _ = self.ipop(im)
        return im


class IPseudoImmutableStackOps(
        IPseudoImmutableInputStackOps
        , IPseudoImmutableOutputViewStackOps):
    # data structure side
    #   e.g. what the actually underlying data structure can offer
    # after ipush, stack may or may not be empty
    # ipop empty stack, may or maynot raise
    #
    # ipop_None, `ipop, `ipush
    __slots__ = ()

class IPseudoImmutableTopStackOps(
        IPseudoImmutableStackOps, IStackOps__top_raise):
    # after ipush, stack should not be empty
    # ipop empty stack then raise
    # top empty stack then raise
    #
    # `is_empty, `top, top_or_fdefault, ipop_None, `ipop, `ipush, ipop_or_fdefault
    __slots__ = ()

    '''
    @instance_const_method
    @abstractmethod
    def is_empty(self, im):
        # is_empty :: im -> bool
        try:
            self.top(im)
        except EmptyStackError:
            return True
        return False
    '''
    @instance_const_method
    @abstractmethod
    def top(self, im):
        # top :: im -> x
        # top empty stack then raise
        pass

    @instance_pseudo_inplace_eval
    def ipop_or_fdefault(self, im, fdefault, wrap=echo):
        # ipop_or_fdefault :: im -> (()->r) -> (x->y) -> (im, (y|r))
        if self.is_empty(im):
            return im, fdefault()
        im, x = self.ipop()
        return im, wrap(x)


class IPseudoImmutableSizedTopStackOps(
        IPseudoImmutableTopStackOps, ISizedStackOps):
    # after ipush, stack should not be empty
    # ipop empty stack then raise
    # top empty stack then raise
    #
    # is_empty, `top, top_or_fdefault, ipop_None, `ipop, `ipush, ipop_or_fdefault;
    #   `len;
    __slots__ = ()
    is_empty = ISizedStackOps.is_empty
    '''
    @instance_const_method
    def is_empty(self, im):
        # is_empty :: im -> bool
        return bool(self.len(im))
    '''
class IPseudoImmutableCompleteStackOps(
        IPseudoImmutableSizedTopStackOps
        , IStackOps__reversed
        , ISizedStackOps
        , IStackOps__factory):
    # after ipush, stack should not be empty
    # ipop empty stack then raise
    # top empty stack then raise
    #
    # is_empty, `top, top_or_fdefault, ipop_None, `ipop, `ipush, ipop_or_fdefault;
    #   `len; `from_iterable
    __slots__ = ()
    is_empty = ISizedStackOps.is_empty
    pass

