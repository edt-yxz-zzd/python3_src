r'''
see:
    view ../../python3_src/seed/tiny_/HexReprInt.py
    view ../../python3_src/seed/helper/ConstantRepr.py

usage:
    比如：ord(char) 就希望 显示 hex 而非 decimal
    当 ord(char) 出现在 容器 中，就 可用 HexReprInt 代替 int

used by:
    view ../../python3_src/script/try_python/unicodedata/list_all_values_of_property.py
        import unicodedata as U
        from seed.data_funcs.rngs import StackStyleSimpleIntSet
        from seed.tiny_.HexReprInt import HexReprInt

#'''


class HexReprInt(int):
    __slots__ = ()
    def __repr__(sf, /):
        return hex(sf)
assert repr(HexReprInt(15)) == hex(15) == '0xf'
assert repr(HexReprInt(-15)) == hex(-15) == '-0xf'

from seed.tiny_.HexReprInt import HexReprInt

