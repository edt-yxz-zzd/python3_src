
__all__ = '''
    Wrapper

    IWrapperOps
    theWrapperOps
    '''.split()

from seed.helper.repr_input import repr_helper
from .IWrapperOps import IWrapperOps


class Wrapper:
    # mutable; to wrap immutable to make it mutable
    #   e.g.
    #       obj is handled by PseudoImmutableOps<obj>
    #       now Wrapper<obj> is handled by MutableOps<Wrapper<obj> >
    __slots__ = '__underlying_obj'
    def __init__(self, underlying):
        self.__underlying_obj = underlying
    def get_wrapped_obj(self):
        return self.__underlying_obj
    def set_wrapped_obj(self, obj):
        self.__underlying_obj = obj
    def __repr__(self):
        return repr_helper(self, self.__underlying_obj)

class TheWrapperOps(IWrapperOps):
    # `new_wrapper, `get_wrapped_obj, `set_wrapped_obj
    #
    # assume w is Wrapper<x>
    __slots__ = ()
    def new_wrapper(self, x):
        return Wrapper(x)
    def get_wrapped_obj(self, w):
        return w.get_wrapped_obj()
    def set_wrapped_obj(self, w, x):
        return w.set_wrapped_obj(x)
theWrapperOps = TheWrapperOps()



