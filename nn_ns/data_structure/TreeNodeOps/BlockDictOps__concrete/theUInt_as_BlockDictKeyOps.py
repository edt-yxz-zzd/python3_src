
__all__ = '''
    theUInt_as_BlockDictKeyOps
    '''.split()

from .abc import override
from ..BlockDictOps.IBlockDictKeyOps import IBlockDictKeyOps, KeyExCase


class UInt_as_BlockDictKeyOps(IBlockDictKeyOps):
    '''UInt_as_BlockDictKeyOps

example:
    >>> ops = theUInt_as_BlockDictKeyOps
    >>> ops.is_key(0)
    True
    >>> ops.is_key(-1)
    False

    >>> ops.mkTheKey(1) == (KeyExCase.TheKey, 1)
    True

    >>> ops.getTheMinKeyEx() == (KeyExCase.TheKey, 0)
    True
    >>> ops.getTheMaxKeyEx() == (KeyExCase.VirtualLessMaxKeyEx, None)
    True

    >>> ops.mkMore(4) == (KeyExCase.TheKey, 5)
    True
    >>> ops.mkLess(4) == (KeyExCase.TheKey, 3)
    True

    >>> ops.key_ltTheMaxKeyEx(0)
    True
    >>> ops.key_ltTheMaxKeyEx(1)
    True
    >>> ops.key_gtTheMinKeyEx(1)
    True
    >>> ops.key_gtTheMinKeyEx(0)
    False

    >>> ops.getWholeRange() == ((KeyExCase.TheKey, 0), (KeyExCase.VirtualLessMaxKeyEx, None))
    True
'''
    __slots__ = ()

    @override
    def _get_total_key_ops_(ops):
        return super()._get_total_key_ops_()


    @override
    def is_key(self, key):
        return type(key) is int and key >= 0
    @override
    def getTheMinKeyEx(self):
        # () -> KeyEx
        return self.mkTheKey(0)
    @override
    def getTheMaxKeyEx(self):
        # () -> KeyEx
        return (KeyExCase.VirtualLessMaxKeyEx, None)
    @override
    def mkMore(self, key):
        # Key -> KeyEx
        assert self.key_ltTheMaxKeyEx(key)
        return self.mkTheKey(key+1)
    @override
    def mkLess(self, key):
        # Key -> KeyEx
        assert self.key_gtTheMinKeyEx(key)
        return self.mkTheKey(key-1)
    @override
    def key_gtTheMinKeyEx(self, key):
        # cmp Key with KeyEx
        return key > 0
    @override
    def key_ltTheMaxKeyEx(self, key):
        # cmp Key with KeyEx
        return True
    @override
    def get_args_for_eq_hash(ops):
        return ()


    @override
    def is_key_ex_case(self, case):
        return id(case) in case_ids
cases = (KeyExCase.TheKey, KeyExCase.VirtualLessMaxKeyEx)
case_ids = (*map(id, cases),)

theUInt_as_BlockDictKeyOps = UInt_as_BlockDictKeyOps()





if __name__ == "__main__":
    import doctest
    doctest.testmod()



