

__all__ = '''
    IWrapperOpsBase
        IWrapperOps__factory
        IWrapperOps__get
        IWrapperOps__set
            IWrapperOps
    '''.split()

from abc import ABC, ABCMeta, abstractmethod


class IWrapperOpsBase(ABC):
    __slots__ = ()
class IWrapperOps__factory(IWrapperOpsBase):
    __slots__ = ()
    @abstractmethod
    def new_wrapper(self, x):
        # new_wrapper :: x -> w
        pass
class IWrapperOps__get(IWrapperOpsBase):
    __slots__ = ()
    @abstractmethod
    def get_wrapped_obj(self, w):
        # get_wrapped_obj :: w -> x
        pass
class IWrapperOps__set(IWrapperOpsBase):
    __slots__ = ()
    @abstractmethod
    def set_wrapped_obj(self, w, x):
        # set_wrapped_obj :: w -> x -> None
        pass
class IWrapperOps(IWrapperOps__set, IWrapperOps__get, IWrapperOps__factory):
    # `new_wrapper, `get_wrapped_obj, `set_wrapped_obj
    __slots__ = ()
    pass


