
__all__ = '''
    theFraction_as_BlockDictKeyOps
    '''.split()

from .abc import override
from fractions import Fraction
from ..BlockDictOps.IBlockDictKeyOps import IBlockDictKeyOps, KeyExCase

class Fraction_as_BlockDictKeyOps(IBlockDictKeyOps):
    '''Fraction_as_BlockDictKeyOps

example:

    >>> from ..OtherOps.ITotalOrderingOps import ITotalOrderingOps
    >>> ops = theFraction_as_BlockDictKeyOps
    >>> F = Fraction

    >>> ops.is_key(0)
    False
    >>> ops.is_key(-1)
    False
    >>> ops.is_key(F(0))
    True
    >>> ops.is_key(F(-1))
    True
    >>> ops.is_key(F(-3, 6))
    True

    >>> ops.mkTheKey(F(1)) == (KeyExCase.TheKey, F(1))
    True

    >>> ops.getTheMinKeyEx() == (KeyExCase.VirtualMoreMinKeyEx, None)
    True
    >>> ops.getTheMaxKeyEx() == (KeyExCase.VirtualLessMaxKeyEx, None)
    True

    >>> ops.mkMore(F(4)) == (KeyExCase.VirtualMoreKey, F(4))
    True
    >>> ops.mkLess(F(4)) == (KeyExCase.VirtualLessKey, F(4))
    True

    >>> ops.key_ltTheMaxKeyEx(F(0))
    True
    >>> ops.key_ltTheMaxKeyEx(F(1))
    True
    >>> ops.key_ltTheMaxKeyEx(F(-1))
    True
    >>> ops.key_gtTheMinKeyEx(F(-1))
    True
    >>> ops.key_gtTheMinKeyEx(F(1))
    True
    >>> ops.key_gtTheMinKeyEx(F(0))
    True




    >>> F0 = F(0)
    >>> F1 = F(1)
    >>> F2 = F(2)
    >>> ex0 = ops.mkTheKey(F0)
    >>> ex1 = ops.mkTheKey(F1)
    >>> ex2 = ops.mkTheKey(F2)
    >>> more0 = ops.mkMore(F0)
    >>> more1 = ops.mkMore(F1)
    >>> more2 = ops.mkMore(F2)
    >>> less0 = ops.mkLess(F0)
    >>> less1 = ops.mkLess(F1)
    >>> less2 = ops.mkLess(F2)
    >>> neg_inf = ops.getTheMinKeyEx()
    >>> pos_inf = ops.getTheMaxKeyEx()

    # X_right_bound: ex0, ex1, ex2, less0, less1, less2, pos_inf
    # Y_left_bound: ex0, ex1, ex2, more0, more1, more2, neg_inf
    # cross(X_right_bound, Y_left_bound)
    >>> ops.cross(ex1, ex0)
    True
    >>> ops.cross(ex1, ex1)     ######### (..., 1] and [1, ...)
    True
    >>> ops.cross(ex1, ex2)
    False
    >>> ops.cross(ex1, more0)
    True
    >>> ops.cross(ex1, more1)   ######### (..., 1] and (1, ...)
    False
    >>> ops.cross(ex1, more2)
    False
    >>> ops.cross(ex1, neg_inf)
    True

    >>> ops.cross(less1, ex0)
    True
    >>> ops.cross(less1, ex1)   ######## (..., 1) and [1, ...)
    False
    >>> ops.cross(less1, ex2)
    False
    >>> ops.cross(less1, more0)
    True
    >>> ops.cross(less1, more1)
    False
    >>> ops.cross(less1, more2)
    False
    >>> ops.cross(less1, neg_inf)
    True
    >>> ops.cross(pos_inf, ex1)   ######## (..., +inf) and [0, ...)
    True
    >>> ops.cross(pos_inf, more1)
    True
    >>> ops.cross(pos_inf, neg_inf)
    True



    >>> ops.eqKeyEx(pos_inf, pos_inf)
    True
    >>> ops.eqKeyEx(neg_inf, neg_inf)
    True
    >>> ops.eqKeyEx(ex1, ex1)
    True
    >>> ops.eqKeyEx(more1, more1)
    True
    >>> ops.eqKeyEx(less1, less1)
    True

    >>> ops.eqKeyEx(pos_inf, neg_inf)
    False
    >>> ops.eqKeyEx(pos_inf, ex1)
    False
    >>> ops.eqKeyEx(pos_inf, more1)
    False
    >>> ops.eqKeyEx(pos_inf, less1)
    False

    >>> ops.eqKeyEx(neg_inf, pos_inf)
    False
    >>> ops.eqKeyEx(neg_inf, ex1)
    False
    >>> ops.eqKeyEx(neg_inf, more1)
    False
    >>> ops.eqKeyEx(neg_inf, less1)
    False

    >>> ops.eqKeyEx(ex1, ex0)
    False
    >>> ops.eqKeyEx(ex1, more1)
    False
    >>> ops.eqKeyEx(ex1, less1)
    False
    >>> ops.eqKeyEx(less1, more1)
    False
    >>> ops.eqKeyEx(less2, more1)
    False


    >>> ops.cmpRange((more0, less1), (more0, less1))
    0
    >>> ops.cmpRange((more0, less1), (more0, ex1))
    -1
    >>> ops.cmpRange((more0, less1), (ex0, ex1))
    1
    >>> ops.eqRange((more0, less1), (more0, less1))
    True
    >>> ops.eqRange((more0, less1), (more0, ex1))
    False



    >>> ops.geKeyEx(less1, pos_inf)
    False
    >>> ops.geKeyEx(less1, neg_inf)
    True
    >>> ops.geKeyEx(less1, less1)
    True
    >>> ops.geKeyEx(less1, ex1)
    False
    >>> ops.geKeyEx(less1, more1)
    False
    >>> ops.geKeyEx(more1, pos_inf)
    False
    >>> ops.geKeyEx(more1, neg_inf)
    True
    >>> ops.geKeyEx(more1, less1)
    True
    >>> ops.geKeyEx(more1, ex1)
    True
    >>> ops.geKeyEx(more1, more1)
    True
    >>> ops.geKeyEx(ex1, pos_inf)
    False
    >>> ops.geKeyEx(ex1, neg_inf)
    True
    >>> ops.geKeyEx(ex1, more1)
    False
    >>> ops.geKeyEx(ex1, ex1)
    True
    >>> ops.geKeyEx(ex1, less1)
    True
    >>> ops.geKeyEx(pos_inf, pos_inf)
    True
    >>> ops.geKeyEx(pos_inf, neg_inf)
    True
    >>> ops.geKeyEx(pos_inf, ex1)
    True
    >>> ops.geKeyEx(pos_inf, more1)
    True
    >>> ops.geKeyEx(pos_inf, less1)
    True
    >>> ops.geKeyEx(neg_inf, pos_inf)
    False
    >>> ops.geKeyEx(neg_inf, neg_inf)
    True
    >>> ops.geKeyEx(neg_inf, ex1)
    False
    >>> ops.geKeyEx(neg_inf, more1)
    False
    >>> ops.geKeyEx(neg_inf, less1)
    False


    >>> ops.geRange((ex1, ex2), (ex1, ex2))
    True
    >>> ops.geRange((ex1, ex2), (ex2, ex1))
    False
    >>> ops.geRange((ex1, ex2), (ex1, ex1))
    True

    >>> ops.getTheMaxKeyEx() == (KeyExCase.VirtualLessMaxKeyEx, None)
    True
    >>> ops.getTheMinKeyEx() == (KeyExCase.VirtualMoreMinKeyEx, None)
    True



    >>> ops.gtKeyEx(ex1, pos_inf)
    False
    >>> ops.gtKeyEx(ex1, neg_inf)
    True
    >>> ops.gtKeyEx(ex1, ex1)
    False
    >>> ops.gtKeyEx(ex1, less1)
    True
    >>> ops.gtKeyEx(ex1, more1)
    False

    >>> ops.gtRange((ex1, ex2), (ex1, ex2))
    False
    >>> ops.gtRange((ex1, ex2), (ex1, less2))
    True
    >>> ops.gtRange((ex2, ex1), (ex1, ex2))
    True

    >>> ops.key_gtTheMinKeyEx(F0)
    True

    >>> ops.intersection_ranges1((ex2, ex1), (ex0, less1)) == (ex2, less1)
    True

    >>> ops.isEmptyRange((ex2, ex1))
    True
    >>> ops.isEmptyRange((ex1, ex1))
    False
    >>> ops.isEmptyRange((more1, ex1))
    True

    >>> ops.isKeyEx(more1)
    True
    >>> ops.isKeyEx(ex1)
    True
    >>> ops.isKeyEx(F1)
    False

    >>> ops.isLeftBound(neg_inf)
    True
    >>> ops.isLeftBound(less1)
    False
    >>> ops.isLeftBound(ex1)
    True
    >>> ops.isLeftBound(more1)
    True
    >>> ops.isLeftBound(pos_inf)
    False

    >>> ops.isRange((ex1, ex0))
    True
    >>> ops.isRange((less1, ex0))
    False

    >>> ops.isRightBound(neg_inf)
    False
    >>> ops.isRightBound(less1)
    True
    >>> ops.isRightBound(ex1)
    True
    >>> ops.isRightBound(more1)
    False
    >>> ops.isRightBound(pos_inf)
    True

    >>> ops.isTheKey(neg_inf)
    False
    >>> ops.isTheKey(less1)
    False
    >>> ops.isTheKey(ex1)
    True
    >>> ops.isTheKey(more1)
    False
    >>> ops.isTheKey(pos_inf)
    False


    >>> ops.isTheMaxKeyEx(neg_inf)
    False
    >>> ops.isTheMaxKeyEx(less1)
    False
    >>> ops.isTheMaxKeyEx(ex1)
    False
    >>> ops.isTheMaxKeyEx(more1)
    False
    >>> ops.isTheMaxKeyEx(pos_inf)
    True

    >>> ops.isTheMinKeyEx(neg_inf)
    True
    >>> ops.isTheMinKeyEx(less1)
    False
    >>> ops.isTheMinKeyEx(ex1)
    False
    >>> ops.isTheMinKeyEx(more1)
    False
    >>> ops.isTheMinKeyEx(pos_inf)
    False


    >>> ops.is_key(F1)
    True
    >>> ops.is_key(ex1)
    False

    >>> ops.is_key_ex_case(KeyExCase.TheKey)
    True
    >>> ops.is_key_ex_case('afsaf')
    False

    >>> ops.leKeyEx(ex1, ex0)
    False
    >>> ops.leKeyEx(ex1, ex1)
    True
    >>> ops.leKeyEx(ex1, ex2)
    True

    >>> ops.leRange((ex1, ex2), (ex1, ex2))
    True
    >>> ops.leRange((ex1, ex1), (ex1, ex2))
    True
    >>> ops.leRange((ex2, ex1), (ex1, ex2))
    False

    >>> ops.left_bound2right_bound_less(ex1) == less1
    True
    >>> ops.left_bound2right_bound_less(more1) == ex1
    True
    >>> ops.left_bound2right_bound_less(neg_inf)
    Traceback (most recent call last):
        ...
    ValueError: should not be TheMinKeyEx
    >>> ops.left_bound2right_bound_less(pos_inf)
    Traceback (most recent call last):
        ...
    TypeError: not isLeftBound
    >>> ops.left_bound2right_bound_less(less1)
    Traceback (most recent call last):
        ...
    TypeError: not isLeftBound


    >>> ops.ltKeyEx(ex1, ex0)
    False
    >>> ops.ltKeyEx(ex1, ex1)
    False
    >>> ops.ltKeyEx(ex1, ex2)
    True

    >>> ops.ltRange((ex1, ex2), (ex1, ex2))
    False
    >>> ops.ltRange((ex1, ex1), (ex1, ex2))
    True
    >>> ops.ltRange((ex2, ex1), (ex1, ex2))
    False

    >>> ops.key_ltTheMaxKeyEx(F1)
    True

    >>> total_left_bound_ops = ops.make_total_left_bound_ops()
    >>> isinstance(total_left_bound_ops, ITotalOrderingOps)
    True
    >>> total_left_bound_ops.le(ex1, neg_inf)
    False
    >>> total_left_bound_ops.le(ex1, more1)
    True

    >>> ops.mkLess(F1) == (KeyExCase.VirtualLessKey, F1)
    True
    >>> ops.mkMore(F1) == (KeyExCase.VirtualMoreKey, F1)
    True
    >>> ops.mkRange(more1, less0) == (more1, less0)
    True
    >>> ops.mkRange(more1, more1)
    Traceback (most recent call last):
        ...
    AssertionError

    >>> ops.mkSingletonRange(F1) == (ex1, ex1)
    True


    >>> ops.mkTheKey(F1) == (KeyExCase.TheKey, F1)
    True
    >>> ops.neKeyEx(ex1, more1)
    True
    >>> ops.neKeyEx(ex1, ex1)
    False
    >>> ops.neKeyEx(ex1, ex2)
    True
    >>> ops.neKeyEx(ex2, ex1)
    True

    >>> ops.neRange((ex1, ex2), (ex1, ex2))
    False
    >>> ops.neRange((ex1, ex1), (ex1, ex2))
    True
    >>> ops.neRange((ex2, ex1), (ex1, ex2))
    True

    >>> ops.right_bound2left_bound_more(less1) == ex1
    True
    >>> ops.right_bound2left_bound_more(ex1) == more1
    True
    >>> ops.right_bound2left_bound_more(pos_inf)
    Traceback (most recent call last):
        ...
    ValueError: should not be TheMaxKeyEx
    >>> ops.right_bound2left_bound_more(more1)
    Traceback (most recent call last):
        ...
    TypeError: not isRightBound
    >>> ops.right_bound2left_bound_more(neg_inf)
    Traceback (most recent call last):
        ...
    TypeError: not isRightBound


    >>> ops.subtract_two_touch_or_cross_ranges((ex0, ex1), (ex1, ex2)) == [(ex0, less1)]
    True
    >>> ops.subtract_two_touch_or_cross_ranges((ex0, ex1), (more1, ex2)) == [(ex0, ex1)]
    True
    >>> ops.subtract_two_touch_or_cross_ranges((ex0, ex1), (ex0, ex2)) == []
    True
    >>> ops.subtract_two_touch_or_cross_ranges((ex0, ex2), (ex0, ex2)) == []
    True
    >>> ops.subtract_two_touch_or_cross_ranges((ex0, ex2), (ex0, ex1)) == [(more1, ex2)]
    True
    >>> ops.subtract_two_touch_or_cross_ranges((more0, ex2), (ex0, ex1)) == [(more1, ex2)]
    True
    >>> ops.subtract_two_touch_or_cross_ranges((ex0, ex2), (more0, ex1)) == [(ex0, ex0), (more1, ex2)]
    True

    >>> ops.subtract_two_touch_or_cross_ranges((ex1, ex2), (ex0, ex1)) == [(more1, ex2)]
    True
    >>> ops.subtract_two_touch_or_cross_ranges((more1, ex2), (ex0, ex1)) == [(more1, ex2)]
    True
    >>> ops.subtract_two_touch_or_cross_ranges((ex1, ex2), (ex0, less1)) == [(ex1, ex2)]
    True
    >>> ops.subtract_two_touch_or_cross_ranges((ex0, ex2), (ex1, ex1)) == [(ex0, less1), (more1, ex2)]
    True

    >>> ops.total_key_ops is ops.get_total_key_ops()
    True


    # touch(right_bound, left_bound)
    >>> ops.touch(ex1, ex1)
    False
    >>> ops.touch(ex1, more1)
    True
    >>> ops.touch(less1, ex1)
    True
    >>> ops.touch_or_cross(ex1, more1)
    True
    >>> ops.touch_or_cross(less1, ex1)
    True
    >>> ops.touch_or_cross(ex1, ex1)
    True
    >>> ops.touch_or_cross(less1, more1)
    False

    >>> ops.union_touch_or_cross_ranges1((ex1, ex0), (more1, less2), (ex2, ex2)) == (more1, ex2)
    Traceback (most recent call last):
        ...
    ValueError
    >>> ops.union_touch_or_cross_ranges1((more1, less2), (ex2, ex2)) == (more1, ex2)
    True

    >>> ops.insideRange((ex1, ex1), (ex0, ex2))
    True
    >>> ops.insideRange((ex0, ex2), (ex0, ex2))
    True


    >>> ops.getWholeRange() == ((KeyExCase.VirtualMoreMinKeyEx, None), (KeyExCase.VirtualLessMaxKeyEx, None))
    True
'''

    __slots__ = ()

    @override
    def _get_total_key_ops_(ops):
        return super()._get_total_key_ops_()

    @override
    def is_key_ex_case(self, case):
        return type(case) is KeyExCase
    @override
    def is_key(self, key):
        return type(key) is Fraction
    @override
    def getTheMinKeyEx(self):
        # () -> KeyEx
        return (KeyExCase.VirtualMoreMinKeyEx, None)
    @override
    def getTheMaxKeyEx(self):
        # () -> KeyEx
        return (KeyExCase.VirtualLessMaxKeyEx, None)
    @override
    def mkMore(self, key):
        # Key -> KeyEx
        assert self.key_ltTheMaxKeyEx(key)
        return (KeyExCase.VirtualMoreKey, key)
    @override
    def mkLess(self, key):
        # Key -> KeyEx
        assert self.key_gtTheMinKeyEx(key)
        return (KeyExCase.VirtualLessKey, key)
    @override
    def key_gtTheMinKeyEx(self, key):
        # cmp Key with KeyEx
        return True
    @override
    def key_ltTheMaxKeyEx(self, key):
        # cmp Key with KeyEx
        return True
    @override
    def get_args_for_eq_hash(ops):
        return ()
theFraction_as_BlockDictKeyOps = Fraction_as_BlockDictKeyOps()





if __name__ == "__main__":
    import doctest
    doctest.testmod()



