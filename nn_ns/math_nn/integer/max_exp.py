

from numbers import Integral

__all__ = ('max_exp',)


def max_exp(base, x):
    r'max{e | [base**e\x]}'
    assert base >= 2
    
    x0 = x
    e = 0
    while True:
        y, r = divmod(x, base)
        assert y < x
        assert r < base
        if r:
            break
        e += 1
        x = y
    assert is_int_factor(base**e, x0)
    assert not is_int_factor(base**(e+1), x0)
    return e

def divides(q, x):
    return x%q == 0

def max_exp(base, x):
    r'max{e | [base**e\x]}'
    if not all(isinstance(i, Integral) for i in [base, x]):
        raise TypeError()
    if not base >= 2:
        raise ValueError()

    old_x = x
    x = abs(x)

    ls = [base]
    while divides(ls[-1], x):
        ls.append(ls[-1]**2)
    ls.pop()

    
    exp = 0
    while ls:
        # the last one divides x
        #assert divides(ls[-1], x)
        
        exp += len(ls)
        x //= ls.pop()

        while ls and not divides(ls[-1], x):
            ls.pop()
    assert not divides(base, x)

    assert divides(base**exp, old_x)
    assert not divides(base**(exp+1), old_x)
    return exp

assert max_exp(3, 4) == 0
assert max_exp(3, -6) == 1
assert max_exp(3, 9) == 2
