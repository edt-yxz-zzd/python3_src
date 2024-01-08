
#e ../../python3_src/seed/tiny_/std____key__le__reverse_.py
import operator #__le__
from seed.tiny_.check import check_callable, check_type_is
from seed.helper.ifNone import ifNone
from seed.helper.Echo import echo
def std____key__le__reverse_(key, __le__, reverse):
    check_type_is(bool, reverse)

    key = ifNone(key, echo)
    check_callable(key)

    __le__ = ifNone(__le__, operator.__le__)
    check_callable(__le__)
    return (key, __le__, reverse)

from seed.tiny_.std____key__le__reverse_ import std____key__le__reverse_
