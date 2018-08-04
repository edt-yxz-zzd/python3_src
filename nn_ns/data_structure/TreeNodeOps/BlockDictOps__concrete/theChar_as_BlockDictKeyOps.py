
__all__ = '''
    theChar_as_BlockDictKeyOps
    '''.split()

from .abc import override
from ..BlockDictOps.IBlockDictKeyOps import IBlockDictKeyOps, KeyExCase

try:
    chr(0x110000)
except ValueError:
    # ValueError: chr() arg not in range(0x110000)
    pass
else:
    raise logic-error

MAX_CHAR_ORD = 0x110000-1
chr(MAX_CHAR_ORD)
try:
    chr(MAX_CHAR_ORD+1)
except ValueError:pass
else:
    raise logic-error

MIN_CHAR_ORD = 0
MAX_CHAR = chr(MAX_CHAR_ORD)
MIN_CHAR = chr(MIN_CHAR_ORD)

class Char_as_BlockDictKeyOps(IBlockDictKeyOps):
    r'''Char_as_BlockDictKeyOps

example:
    >>> ops = theChar_as_BlockDictKeyOps
    >>> ops.is_key('0')
    True
    >>> ops.is_key(-1)
    False

    >>> ops.mkTheKey('1') == (KeyExCase.TheKey, '1')
    True

    >>> '\0' == MIN_CHAR
    True
    >>> ops.getTheMinKeyEx() == (KeyExCase.TheKey, '\0')
    True
    >>> ops.getTheMaxKeyEx() == (KeyExCase.TheKey, MAX_CHAR)
    True

    >>> ops.mkMore('4') == (KeyExCase.TheKey, '5')
    True
    >>> ops.mkLess('4') == (KeyExCase.TheKey, '3')
    True

    >>> ops.key_ltTheMaxKeyEx('0')
    True
    >>> ops.key_ltTheMaxKeyEx(MAX_CHAR)
    False
    >>> ops.key_gtTheMinKeyEx('0')
    True
    >>> ops.key_gtTheMinKeyEx(MIN_CHAR)
    False

    >>> ops.getWholeRange() == ((KeyExCase.TheKey, MIN_CHAR), (KeyExCase.TheKey, MAX_CHAR))
    True
'''
    __slots__ = ()

    @override
    def _get_total_key_ops_(ops):
        return super()._get_total_key_ops_()


    @override
    def is_key(self, key):
        return type(key) is str and len(key) == 1
    @override
    def getTheMinKeyEx(self):
        # () -> KeyEx
        return self.mkTheKey(MIN_CHAR)
    @override
    def getTheMaxKeyEx(self):
        # () -> KeyEx
        return self.mkTheKey(MAX_CHAR)
    @override
    def mkMore(self, key):
        # Key -> KeyEx
        assert self.key_ltTheMaxKeyEx(key)
        return self.mkTheKey(chr(ord(key)+1))
    @override
    def mkLess(self, key):
        # Key -> KeyEx
        assert self.key_gtTheMinKeyEx(key)
        return self.mkTheKey(chr(ord(key)-1))
    @override
    def key_gtTheMinKeyEx(self, key):
        # cmp Key with KeyEx
        return ord(key) > 0
    @override
    def key_ltTheMaxKeyEx(self, key):
        # cmp Key with KeyEx
        return ord(key) < MAX_CHAR_ORD
    @override
    def get_args_for_eq_hash(ops):
        return ()


    @override
    def is_key_ex_case(self, case):
        return case == KeyExCase.TheKey

theChar_as_BlockDictKeyOps = Char_as_BlockDictKeyOps()





if __name__ == "__main__":
    import doctest
    doctest.testmod()



