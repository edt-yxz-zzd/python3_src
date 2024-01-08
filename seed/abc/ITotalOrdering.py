r'''[[[
e ../../python3_src/seed/abc/ITotalOrdering.py

why not use functools.total_ordering?
    view ../../python3_src/seed/types/OverrideOrdering.py
    #>>> lnf_111 < lnf_222 # use "functools.total_ordering" and defined '__le__' only without '__eq__' will give wrong result 'True' here. since: [(x < y) =[def]= (x <= y) && (x != y)]

cp /data/data/com.termux/files/usr/lib/python3.10/functools.py /sdcard/0my_files/tmp/out4py/py_src/py-functools.py
view /sdcard/0my_files/tmp/out4py/py_src/py-functools.py

def _lt_from_le(self, other, NotImplemented=NotImplemented):
    'Return a < b.  Computed by @total_ordering from (a <= b) and (a != b).'
    op_result = type(self).__le__(self, other)
    if op_result is NotImplemented:
        return op_result
    return op_result and self != other



#]]]'''#'''
__all__ = r'''
    ITotalOrdering5le
'''.split()#'''

from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
class ITotalOrdering5le(ABC):
    __slots__ = ()
    @abstractmethod
    def __le__(sf, ot, /):
        if not type(ot) is type(sf):
            return NotImplemented
        raise NotImplementedError
    def __gt__(sf, ot, /):
        if not type(ot) is type(sf):
            return NotImplemented
        return not sf <= ot
    def __ge__(sf, ot, /):
        if not type(ot) is type(sf):
            return NotImplemented
        return ot <= sf
    def __lt__(sf, ot, /):
        if not type(ot) is type(sf):
            return NotImplemented
        return not ot <= sf
    def __eq__(sf, ot, /):
        return sf <= ot and ot <= sf
    def __ne__(sf, ot, /):
        return not sf == ot



from seed.abc.ITotalOrdering import ITotalOrdering5le
from seed.abc.ITotalOrdering import *
