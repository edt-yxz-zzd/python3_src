

'''
type IntMap a = Map Int a
two implements:
    let N be upper bound of keys
    let n be number of elements
    
    BigO_N
        [Maybe a] of len N
        get/set/del O(1)
        iter O(N)
    OneTime
        [Int] of len N
        [Int] of len n
        get/set/del O(1)
        iter O(n)
        
'''

from collections.abc import Mapping, MutableMapping
from .tuple_based_maybe import *

class BigO_N_Mapping(Mapping):
    # assume len(self) = n <= N ; where N is a constant
    # iter over Mapping will be O(N)
    pass


class ListBasedIntMapping__OneTime(OneTimeMap):
    def __init__(self, N):
        self.__ls = [None]*N
        super().__init__(self.__ls)



class ListBasedIntMapping__BigO_N(BigO_N_Mapping, MutableMapping):
    '__getitem__, __setitem__, __delitem__, __iter__, and __len__'
    def __init__(self, N):
        self.__ls = [nothing]*N
        self.__n = 0

    def __check_set_key(self, key):
        if not 0 <= key < len(self.__ls):
            raise KeyError('not {} <= {!r} < {}'.format(0, key, len(self.__ls)))

    def __get(self, key):
        self.__check_set_key(key)
        maybe = self.__ls[key]
        if maybe == nothing:
            raise KeyError('not found: {!r}'.format(key))
        return maybe
    def __getitem__(self, key):
        return unjust(self.__get(key))
    def __setitem__(self, key, value):
        self.__check_set_key(key)
        b = self.__ls[key] == nothing
        self.__ls[key] = just(value)
        if b:
            self.__n += 1
    def __delitem__(self, key):
        self.__get(key)
        self.__ls[key] = nothing
        self.__n -= 1

    def __iter__(self):
        return (i for i, maybe in enumerate(self.__ls) if maybe != nothing)
    
    def __len__(self):
        return self.__n


def make_list_based_int_mappinng_factory(n):
    def _(*args, **kwargs):
        return ListBasedIntMapping(n, *args, **kwargs)
    return _












    
