r'''[[[
e ../../python3_src/nn_ns/math_nn/integer/inv_mod_.py
py -m nn_ns.math_nn.integer.inv_mod_
from nn_ns.math_nn.integer.inv_mod_ import inv_mod_


e ../../python3_src/seed/math/inv_mod_.py
py -m seed.math.inv_mod_
from seed.math.inv_mod_ import inv_mod_

!mv ../../python3_src/seed/math/inv_mod_.py ../../python3_src/nn_ns/math_nn/integer/inv_mod_.py

#]]]'''
__all__ = '''
    inv_mod_
    '''.split()
from nn_ns.math_nn.integer.mod import invmod as _invmod

def inv_mod_(M, x, /):
    '[M=!=0] ==>> [0 <= inv_mod_(M, x) < abs(M)][(inv_mod_(M, x)*x-1)%M == 0]'
    if not type(M) is int: raise TypeError
    if not type(x) is int: raise TypeError
    if M == 0: raise ZeroDivisionError#ValueError
    M = abs(M)
    if M == 1:
        ans = 0
    else:
        ans = _invmod(x, M)
    assert 0 <= ans < abs(M)
    assert (ans*x-1)%M == 0
    return ans

assert inv_mod_(1, 0) == 0
assert inv_mod_(1, 4) == 0
assert inv_mod_(3, 2) == 2
assert inv_mod_(-3, 2) == 2
assert inv_mod_(3, -2) == 1
assert inv_mod_(-3, -2) == 1


