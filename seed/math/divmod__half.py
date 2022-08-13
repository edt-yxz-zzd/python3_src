r'''[[[
e ../../python3_src/seed/math/divmod__half.py
from seed.math.divmod__half import divmod__half, mod__half

#]]]'''
__all__ = '''
    divmod__half
    mod__half

    '''.split()
#from seed.math.GaussInteger import divmod__half
from seed.math.sign_of import sign_of

def divmod__half(n,d,/):
    (q,r) = divmod(n, d)
    if 2*r > abs(d):
        r -= abs(d)
        q += sign_of(d)
    assert q*d+r == n
    assert 2*abs(r) < abs(d) or 2*r == abs(d)
    return (q,r)

def mod__half(x,M,/):
    'x -> M -> [-((M-1)//2)..=M//2]'
    if M == 0: raise ZeroDivisionError#ValueError
    M = abs(M)
    half = M//2
    neg_half = (M%2==0)-half
    assert half - neg_half + 1 == M
    while not neg_half <= x <= half:
        x %= M
        if x > half:
            x -= M
    return x



