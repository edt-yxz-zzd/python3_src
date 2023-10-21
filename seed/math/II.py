
'''

II :: [a] -> (start=1) -> a


functools
    reduce(function, iterable[, initializer])
    # bad! not foldl
seed.iters.fold
    foldl0
seed.iters.binary_op
    foldl
seed.iters.product
    py_sum          py_product
    sum             product
    sum1            product1
    sum_default     product_default
    iter_sum        iter_product
    iter_sum_chain  iter_product_chain
'''#'''

__all__ = r'''
II
    II_mod
        II__ft_e_pairs_
            II__ft2e_
                II__p2e_
'''.split()#'''

#from seed.iters.product import py_product as II
from seed.iters.binary_op import foldl
from operator import __mul__, __mod__, __pow__

def II(iterable, *, one=1, mul=None):
    if mul is None:
        mul = __mul__
    return foldl(mul, one, iterable)
def II_mod(modulus, iterable, *, one=1, mul=None, mod=None):
    #modulus (plural moduli)
    #modulo
    if mul is None:
        mul = __mul__
    if mod is None:
        mod = __mod__
    def mul_mod(a, b, /):
        return mod(mul(a, b), modulus)
    return II(iterable, one=one, mul=mul_mod)
def II__ft2e_(ft2e, *, one=1, mul=None, mod=None, pow=None, modulus=None):
    return II__ft_e_pairs_(ft2e.items(), one=one, mul=mul, mod=mod, pow=pow, modulus=modulus)
def II__ft_e_pairs_(ft_e_pairs, *, one=1, mul=None, mod=None, pow=None, modulus=None):
    if pow is None:
        pow = __pow__
    if modulus is None:
        it = (pow(p,e) for p,e in ft_e_pairs)
        return II(it, one=one, mul=mul)
    else:
        it = (pow(p,e,modulus) for p,e in ft_e_pairs)
        return II_mod(modulus, it, one=one, mul=mul, mod=mod)
II__p2e_ = II__ft2e_



from seed.math.II import II, II_mod, II__p2e_, II__ft2e_, II__ft_e_pairs_
