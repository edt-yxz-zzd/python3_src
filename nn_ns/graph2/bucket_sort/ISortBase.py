

__all__ = '''
    ISortBase
    ISortBase_Key_Reverse
    ISortBase__ConvertNoneKey
    '''.split()
from abc import ABC, abstractmethod
from .echo import echo_ifNone
class ISortBase(ABC):
    @abstractmethod
    def __call__(self, __objs):
        # sort __objs
        raise NotImplementedError

class ISortBase_Key_Reverse(ISortBase):
    def __init__(self, *, key, reverse=False):
        self.key = key
        self.reverse = reverse
class ISortBase__ConvertNoneKey(ISortBase_Key_Reverse):
    def __init__(self, *, key=None, reverse=False):
        key = echo_ifNone(key)
        ISortBase_Key_Reverse.__init__(self, key=key, reverse=reverse)


