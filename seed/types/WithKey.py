
__all__ = '''
    IWithKey
    IWithSortKey
    IWithHashKey
    IWithSortHashKey

    get_key_with
    get_obj_with

    WithKey
    WithSortKey
    WithHashKey
    WithSortHashKey

    LenAsSortKey
    LenAsSortHashKey
    make_obj2WithKey
    '''.split()
from abc import ABCMeta, abstractmethod

class IWithKey(metaclass=ABCMeta):
    # wrap obj to key to be used in heap or ...
    @abstractmethod
    def __get_key_with__(self):pass
    @abstractmethod
    def __get_obj_with__(self):pass


def get_key_with(aWithKey):
    # assert isinstance(aWithKey, IWithKey)
    return type(aWithKey).__get_key_with__(aWithKey)
def get_obj_with(aWithKey):
    # assert isinstance(aWithKey, IWithKey)
    return type(aWithKey).__get_obj_with__(aWithKey)



class IWithSortKey(IWithKey):
    # key used in "sorted", require "__lt__"/"__le__"...
    def __lt__(self, other):
        return get_key_with(self) < get_key_with(other)
    def __le__(self, other):
        return get_key_with(self) <= get_key_with(other)
    def __gt__(self, other):
        return get_key_with(self) > get_key_with(other)
    def __ge__(self, other):
        return get_key_with(self) >= get_key_with(other)
    def __eq__(self, other):
        return get_key_with(self) == get_key_with(other)
    def __ne__(self, other):
        return get_key_with(self) != get_key_with(other)
    pass

class IWithHashKey(IWithKey):
    # key used in "dict", require "__hash__"
    def __hash__(self):
        return hash(get_key_with(self))
    pass
class IWithSortHashKey(IWithHashKey, IWithSortKey):pass


class WithKey(IWithKey):
    def __init__(self, key, obj):
        self.__key = key
        self.__obj = obj
    def __get_key_with__(self):
        return self.__key
    def __get_obj_with__(self):
        return self.__obj

class WithSortKey(WithKey, IWithSortKey):pass
class WithHashKey(WithKey, IWithHashKey):pass
class WithSortHashKey(WithHashKey, WithSortKey, IWithSortHashKey):pass


class LenAsSortKey(WithSortKey):
    def __init__(self, obj):
        super().__init__(len(obj), obj)
class LenAsSortHashKey(LenAsSortKey, WithSortHashKey):pass

def make_obj2WithKey(key_obj2WithKey, obj2key):
    def obj2WithKey(obj):
        return key_obj2WithKey(obj2key(obj), obj)
    return obj2WithKey


