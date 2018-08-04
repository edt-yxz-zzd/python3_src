

r'''
see: "def - ops.txt"


1) def a bottom convertor # untyped
2) limit the power


export:
    convert_PseudoImmutable2MutableStackOps
    Wrapper

example:
    >>> from .LeftBiasListAsStackOps import the_left_bias_list_as_stack_ops
    >>> im_ops = the_left_bias_list_as_stack_ops
    >>> ms_ops = the_left_bias_list_as_wrapped_stack_ops = \
    ...   convert_PseudoImmutable2MutableStackOps(
    ...     im_ops
    ...     , IMutableTopStackOps
    ...     , IStackOps__factory)

    >>> r = ms_ops.from_iterable([1,2,3])
    >>> r
    Wrapper(((((), 1), 2), 3))
    >>> assert r.get_wrapped_obj() == ((((), 1), 2), 3)
    >>> assert ms_ops.top(r) == 3
    >>> assert not im_ops.is_empty(r.get_wrapped_obj())
    >>> assert not ms_ops.is_empty(r)

    >>> [*ls] = im_ops.reversed(r.get_wrapped_obj())
    >>> assert ls == [3,2,1]
    >>> assert exceptError(AttributeError, lambda:ms_ops.reversed)

    >>> ms_ops.pop(r)
    3
    >>> assert r.get_wrapped_obj() == (((),1),2)
    >>> assert ms_ops.top(r) == 2
    >>> ms_ops.push(r, 4)
    >>> assert r.get_wrapped_obj() == ((((),1),2), 4)
    >>> assert ms_ops.top(r) == 4
    >>> assert not ms_ops.is_empty(r)
    >>> ms_ops.pop(r)
    4
    >>> ms_ops.pop(r)
    2
    >>> ms_ops.pop(r)
    1
    >>> assert ms_ops.is_empty(r)
    >>> r
    Wrapper(())
'''

__all__ = '''
    convert_PseudoImmutable2MutableStackOps
    Wrapper
    '''.split()

#from operator import attrgettor
from ..wrapper.Wrapper import Wrapper, IWrapperOps, theWrapperOps
from .IStackOps import IStackOpsBase
from .IMutableStackOps import IMutableStackOpsBase
from .IPseudoImmutableStackOps import IPseudoImmutableStackOpsBase


from .IStackOps import (
IStackOpsBase
    ,IStackOps__factory
    ,IStackOps__is_empty
        ,ISizedStackOps
        ,IStackOps__top_raise
            ,IStackOps__reversed
    )
from .IMutableStackOps import (
    IMutableStackOpsBase
        ,IMutableOutputStackOps
            ,IMutableOutputViewStackOps
        ,IMutableStackOps__pop_None
            ,IMutableOutputViewStackOps
                ,IMutableStackOps
            ,IMutableInputStackOps
                ,IMutableStackOps
                    ,IMutableTopStackOps
                        ,IMutableSizedTopStackOps
                            ,IMutableCompleteStackOps
    )
from .IPseudoImmutableStackOps import (
    IPseudoImmutableStackOpsBase
        ,IPseudoImmutableOutputStackOps
            ,IPseudoImmutableOutputViewStackOps
        ,IPseudoImmutableStackOps__pop_None
            ,IPseudoImmutableOutputViewStackOps
                ,IPseudoImmutableStackOps
            ,IPseudoImmutableInputStackOps
                ,IPseudoImmutableStackOps
                    ,IPseudoImmutableTopStackOps
                        ,IPseudoImmutableSizedTopStackOps
                            ,IPseudoImmutableCompleteStackOps
    )

'''
IPseudoImmutableCompleteStackOps
class BottomWraper:
    def __init__(self, underlying):
        self.__underlying_obj = underlying
    def get_bottom_wrapper_underlying_obj(self):
        return self.__underlying_obj
'''

IMutableStackOpsBottom = IMutableCompleteStackOps
class PseudoImmutable2MutableStackOps__BottomWrapper(
        IMutableCompleteStackOps):
    # input: ops<istack<obj> >
    # self be ops<Wrapper<istack<obj> > >
    #   istack is immutable, but Wrapper<...> is mutable
    def __init__(self
            , istack_ops:IPseudoImmutableStackOpsBase
            , wrapper_ops:IWrapperOps=None
            ):
        if wrapper_ops is None: wrapper_ops = theWrapperOps
        else: assert isinstance(wrapper_ops, IWrapperOps)

        self.istack_ops = istack_ops
        self.wrapper_ops = wrapper_ops
    def from_iterable(self, iterable):
        # from_iterable :: Iter obj -> Wrapper<istack<obj> >
        im = self.istack_ops.from_iterable(iterable)
        ms = self.wrapper_ops.new_wrapper(im)
        return ms
    def push(self, ms, x):
        ops = self.wrapper_ops
        im = ops.get_wrapped_obj(ms)
        im = self.istack_ops.ipush(im, x)
        ops.set_wrapped_obj(ms, im)
        pass
    def pop(self, ms):
        ops = self.wrapper_ops
        im = ops.get_wrapped_obj(ms)
        im, x = self.istack_ops.ipop(im)
        ops.set_wrapped_obj(ms, im)
        return x
    def is_empty(self, ms):
        im = self.wrapper_ops.get_wrapped_obj(ms)
        return self.istack_ops.is_empty(im)
    def len(self, ms):
        im = self.wrapper_ops.get_wrapped_obj(ms)
        return self.istack_ops.len(im)

    def top(self, ms):
        im = self.wrapper_ops.get_wrapped_obj(ms)
        return self.istack_ops.top(im)
    def reversed(self, ms):
        im = self.wrapper_ops.get_wrapped_obj(ms)
        return self.istack_ops.reversed(im)



# to export:
def exceptError(Error, lazy):
    try:
        lazy()
    except Error:
        return True
    return False
def all_are_subclass_of(clss, superclass):
    return all(issubclass(T, superclass)for T in clss)
def all_are_superclass_of(clss, subclass):
    return all(issubclass(subclass, T)for T in clss)
def any_are_subclass_of(clss, superclass):
    return any(issubclass(T, superclass)for T in clss)
def is_instance_of_all(obj, types):
    return all(isinstance(obj, T) for T in types)

# subclass correspond
MutableStackOps2PseudoImmutableStackOps = \
    { #IMutableCompleteStackOps:IPseudoImmutableCompleteStackOps
    IMutableStackOpsBase
    :IPseudoImmutableStackOpsBase
        ,IMutableOutputStackOps
        :IPseudoImmutableOutputStackOps
            ,IMutableOutputViewStackOps
            :IPseudoImmutableOutputViewStackOps

        ,IMutableStackOps__pop_None
        :IPseudoImmutableStackOps__pop_None
            ,IMutableOutputViewStackOps
            :IPseudoImmutableOutputViewStackOps
                ,IMutableStackOps
                :IPseudoImmutableStackOps

            ,IMutableInputStackOps
            :IPseudoImmutableInputStackOps
                ,IMutableStackOps
                :IPseudoImmutableStackOps
                    ,IMutableTopStackOps
                    :IPseudoImmutableTopStackOps
                        ,IMutableSizedTopStackOps
                        :IPseudoImmutableSizedTopStackOps
                            ,IMutableCompleteStackOps
                            :IPseudoImmutableCompleteStackOps
    }
'''
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
'''
def convert_PseudoImmutable2MutableStackOps(
        im_ops:IPseudoImmutableStackOpsBase
        , *args:IMutableStackOpsBase
        , wrapper_ops:IWrapperOps=None):
    # convert PseudoImmutableStackOps to MutableStackOps
    #   stack from istack to Wrapper<istack>
    assert args, TypeError
    ms_types = args
    #if not all_are_subclass_of(ms_types, IMutableStackOpsBase): raise TypeError
    #if not all_are_subclass_of(ms_types, IStackOpsBase): raise TypeError
    if not all_are_superclass_of(ms_types, IMutableCompleteStackOps):
        raise TypeError('this convert function assume IMutableCompleteStackOps as Bottom type')
    if any_are_subclass_of(ms_types, IPseudoImmutableStackOpsBase):
        # superclass of IMutableCompleteStackOps should not contain IPseudoImmutableStackOpsBase
        if issubclass(IMutableCompleteStackOps, IPseudoImmutableStackOpsBase): raise logic-error
        raise logic-error
        raise TypeError('can not convert to IPseudoImmutableStackOpsBase')
    def MsOps2ImOps(MsOps):
        may_ImOps = MutableStackOps2PseudoImmutableStackOps.get(MsOps)
        if may_ImOps is None:
            # maybe MsOps is a const ops
            if issubclass(MsOps, IMutableStackOpsBase):
                raise TypeError('please update MutableStackOps2PseudoImmutableStackOps')
            else:
                # is a const ops
                ConstOps = MsOps
                return ConstOps
        ImOps = may_ImOps
        return ImOps

    im_types = tuple(map(MsOps2ImOps, ms_types))
    if not is_instance_of_all(im_ops, im_types): raise TypeError
    ms_ops = PseudoImmutable2MutableStackOps__BottomWrapper(im_ops)
    def f(attr):
        def method(self, *args, **kwargs):
            return getattr(self, attr)(*args, **kwargs)
        return method
    #class ToGetAttr(*ms_types):pass
    class DonotInitSuper__ToGetAttr(*ms_types):
        def __init__(self):
            return
        def __init_subclass__(self, *args, **kwargs):
            return
        def __getattribute__(self, name):
            super().__getattribute__(name)
            # if success, forward to wrapped obj
            return getattr(ms_ops, name)
    DonotInitSuper__ToGetAttr.__abstractmethods__ = frozenset()
    ms_ops_safe = DonotInitSuper__ToGetAttr()
    return ms_ops_safe

def t():
    #the_left_bias_list_as_stack_ops
    #LeftBiasListAsStackOps(IPseudoImmutableTopStackOps, IStackOps__factory)
    from .LeftBiasListAsStackOps import the_left_bias_list_as_stack_ops
    im_ops = the_left_bias_list_as_stack_ops
    ms_ops = the_left_bias_list_as_wrapped_stack_ops = \
        convert_PseudoImmutable2MutableStackOps(
            im_ops
            , IMutableTopStackOps
            , IStackOps__factory)

    r = ms_ops.from_iterable([1,2,3])
    assert r.get_wrapped_obj() == ((((),1),2), 3)
    assert ms_ops.top(r) == 3
    assert not im_ops.is_empty(r.get_wrapped_obj())
    assert not ms_ops.is_empty(r)

    [*ls] = im_ops.reversed(r.get_wrapped_obj())
    assert ls == [3,2,1]
    assert exceptError(AttributeError, lambda:ms_ops.reversed)

    ms_ops.pop(r)
    assert r.get_wrapped_obj() == (((),1),2)
    assert ms_ops.top(r) == 2
    ms_ops.push(r, 4)
    assert r.get_wrapped_obj() == ((((),1),2), 4)
    assert ms_ops.top(r) == 4
    assert not ms_ops.is_empty(r)
    ms_ops.pop(r)
    ms_ops.pop(r)
    ms_ops.pop(r)
    assert ms_ops.is_empty(r)
    # ValueError: not enough values to unpack (expected 2, got 0)
    assert exceptError(ValueError, lambda:ms_ops.pop(r))

    #ms_ops.len(r)
    # AttributeError: 'DonotInitSuper__ToGetAttr' object has no attribute 'len'
    assert exceptError(AttributeError, lambda:ms_ops.len)

t()


