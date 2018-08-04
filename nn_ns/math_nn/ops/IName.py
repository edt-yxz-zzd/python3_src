

'''
IName is used in ICompositeDomain
'''

__all__ = '''
    IName
    is_name
    '''.split()

from abc import ABCMeta, abstractmethod
from collections.abc import Hashable



class IName(Hashable):pass
if 0:
    IName.register(str)
    IName.register(int)
    #IName.register(tuple)
    #IName.register(frozenset)
builtin_immutable_noncontainer_types = frozenset([
    str, bytes, int # ??bool?? collision with int
    ])
builtin_immutable_container_types = frozenset([
    tuple, frozenset
    ])
list(map(IName.register, builtin_immutable_noncontainer_types))
def is_name(x):
    def this_func(x):
        if type(x) in builtin_immutable_container_types:
            return all(map(this_func, x))
        return isinstance(x, IName)
    return this_func(x)



