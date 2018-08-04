

from typing import (
    TypeVar, Generic, Sequence, Mapping, MutableMapping, MutableSequence)
from abc import abstractmethod

KT = TypeVar('KT')
VT = TypeVar('VT')
NT = TypeVar('NT')
T = TypeVar('T')

class IGetItem(Generic[KT, VT]):
    # no: __iter__, __contain__, __len__, __bool__
    # has: __getitem__
    @abstractmethod
    def __getitem__(self, __key:KT) -> VT:
        # raise LookupError if no found
        raise NotImplementedError
ISeqOrDict.register(list, tuple, dict, Sequence, Mapping)

class IOverwriteItem(ISeqOrDict[KT, VT]):
    # no: __iter__, __contain__, __len__, __bool__
    # no __delitem__; use "self[k] = nothing" instead
    # has: __getitem__, overwrite_item

    @abstractmethod
    def overwrite_item(self, __key:KT, __val:VT) -> None:
        raise NotImplementedError
    '''
    @abstractmethod
    def __setitem__(self, __key:KT, __val:VT) -> None:
        raise NotImplementedError
    '''

IMutableSeqOrDict.register(list, dict, MutableMapping, MutableSequence)

class IDefalutSeqOrDict(ISeqOrDict[KT, VT], Generic[KT, VT, NT]):
    # for some allow keys: when miss, instead of raise, set new value and return
    # see: defaultdict
    def __miss__(self, __key:KT) -> VT: # or raise LookupError
        raise LookupError
    @abstractmethod
    def __getitem__(self, __key:KT) -> VT:
        # return __miss__(__key) if no found
        raise NotImplementedError



class ISeqOrDict__getex(ISeqOrDict[KT, VT], Generic[KT, VT, NT]):
    # no: __iter__, __contain__, __len__, __bool__
    # has: __getitem__, get_or_default, get_the_nothing
    @abstractmethod
    def get_the_nothing(self) -> NT:
        raise NotImplementedError
    @abstractmethod
    def get_or_nothing(self, __key:KT) -> Union[VT, NT]:
        # return self.get_the_nothing() if no found
        raise NotImplementedError

    def __getitem__(self, __key:KT) -> VT:
        return self.get_or_raise(__key, LookupError)
    def get_or_raise(self, __key:KT, __err=LookupError:Exception) -> VT:
        v = self.get_or_nothing(__key)
        if v is self.get_the_nothing():
            raise __err
        return v
    def get_or_default(self, __key:KT, __default:T) -> Union[VT, T]:
        # return __default if no found
        v = self.get_or_nothing(__key)
        if v is self.get_the_nothing():
            return __default
        return v
class IMutableSeqOrDict__discard(
        ISeqOrDict__getex[KT, VT, NT]
        , IMutableSeqOrDict[KT, VT]):
    # no: __iter__, __contain__, __len__, __bool__
    # no __delitem__; use "self[k] = nothing" instead
    # has: __getitem__, __setitem__, discard
    def discard(self, __key:KT) -> None:
        self[__key] = self.get_the_nothing()




class ISeqOrDict__getMixin(ISeqOrDict__getex[KT, VT, NT]):
    def __init__(self, the_nothing:NT):
        self.__the_nothing = the_nothing
    def get_the_nothing(self) -> NT:
        return self.__the_nothing


