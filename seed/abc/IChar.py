#__all__:goto
r'''[[[
e ../../python3_src/seed/abc/IChar.py

seed.abc.IChar
py -m nn_ns.app.debug_cmd   seed.abc.IChar -x
py -m nn_ns.app.doctest_cmd seed.abc.IChar:__doc__ -ht
#]]]'''
__all__ = r'''
IChar
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots, ABCMeta
from seed.tiny_.check import check_ABC
from seed.tiny_.check import check_type_le
from seed.debug.expectError import expectError
___end_mark_of_excluded_global_names__0___ = ...

class _CharABCMeta(ABCMeta):
    __slots__ = ()
    @override
    def __instancecheck__(sf8cls, obj8sf, /):
        return type(obj8sf) is str and len(obj8sf) == 1
@abstractmethod
def __():pass
class IChar(metaclass=_CharABCMeta):
    __slots__ = ()
    locals()[777] = __
    pass
check_ABC(IChar)

check_type_le(IChar, 'x')
assert expectError(TypeError, lambda:check_type_le(IChar, ''))
assert expectError(TypeError, lambda:check_type_le(IChar, 'xx'))
assert expectError(TypeError, lambda:check_type_le(IChar, b'x'))
assert expectError(TypeError, lambda:check_type_le(IChar, 999))

__all__
from seed.abc.IChar import IChar
from seed.abc.IChar import *
