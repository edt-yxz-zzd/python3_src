#__all__:goto
r'''[[[
e ../../python3_src/seed/types/IForkable.py
view ../../python3_src/seed/types/ForkableForwardInputStream.py
view ../../python3_src/seed/types/LazyList.py
    [_LazyListIter <: IForkable__stamp]

seed.types.IForkable
py -m nn_ns.app.debug_cmd   seed.types.IForkable -x

#]]]'''
__all__ = r'''
IForkable
    IForkable__stamp
'''.split()#'''
__all__

from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots

class IForkable(ABC):
    'use 『.fork()』 to hold/cache curr state  #mutable_obj'
    __slots__ = ()
    @abstractmethod
    def fork(sf, /):
        '-> ot/IForkable #immutable_method'
    @abstractmethod
    def were(sf, ot, /):
        'sf/IForkable -> ot/IForkable -> bool #immutable_method'
    def __eq__(sf, ot, /):
        'sf/IForkable -> ot/IForkable -> bool #immutable_method'
        return sf.were(ot)
    def __ne__(sf, ot, /):
        'sf/IForkable -> ot/IForkable -> bool #immutable_method'
        return not sf == ot
class IForkable__stamp(IForkable):
    'use 『.get_stamp()』 to hold/cache curr position to detect changing'
    __slots__ = ()
    @abstractmethod
    def get_stamp(sf, /):
        '-> stamp'
    @abstractmethod
    def has_changed_since_stamp_(sf, stamp, /):
        'stamp -> changed/bool'





__all__
from seed.types.IForkable import IForkable, IForkable__stamp
from seed.types.IForkable import *
