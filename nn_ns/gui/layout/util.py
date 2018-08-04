from root.math.math_func import vsub
import operator


def getSize(size):
    size = tuple(size)
    assert len(size) == 2
    for i in size:
        assert isinstance(i, int)
        assert i >= 0
    return size



def sizeSub(lhs, rhs):
    assert sizeLessOrEqual(rhs, lhs)
    r = vsub(lhs, rhs)
    return getSize(r)

def sizeLessOrEqual(lhs, rhs):
    r = all(map(operator.le, lhs, rhs))
    return r

def allUint(ls):
    return all(L >= 0 for L in ls)

