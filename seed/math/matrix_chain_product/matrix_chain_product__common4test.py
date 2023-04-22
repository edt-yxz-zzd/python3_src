#__all__:goto
r'''[[[
e ../../python3_src/seed/math/matrix_chain_product/matrix_chain_product__common4test.py

seed.math.matrix_chain_product.matrix_chain_product__common4test
py -m nn_ns.app.debug_cmd   seed.math.matrix_chain_product.matrix_chain_product__common4test

from seed.math.matrix_chain_product.matrix_chain_product__common4test import 迭代囗随机生成囗矩阵乘法链维数序列
from seed.math.matrix_chain_product.matrix_chain_product__common4test import 迭代囗随机生成囗矩阵乘法链维数序列囗单调


#]]]'''
__all__ = r'''
    iter_randrange
    iter_list_of_randrange
    迭代囗随机生成囗矩阵乘法链维数序列
    迭代囗随机生成囗矩阵乘法链维数序列囗单调
    单调化囗
'''.split()#'''
__all__

from itertools import islice
from random import randrange

def iter_randrange(*args):
    while 1:
        yield randrange(*args)

def _iter_list_of_len_(L, iterable, /):
    it = iter(iterable)
    while 1:
        yield [*islice(it, L)]
def iter_list_of_randrange(L, /, *args):
    it = iter_randrange(*args)
    return _iter_list_of_len_(L, it)
def 迭代囗随机生成囗矩阵乘法链维数序列(L, upper4weight, /):
    assert L >= 2

    #bug: return iter_list_of_randrange(L, upper4weight)
    #   output 0
    return iter_list_of_randrange(L, 1, upper4weight)
def 迭代囗随机生成囗矩阵乘法链维数序列囗单调(L, upper4weight, /):
    lss = 迭代囗随机生成囗矩阵乘法链维数序列(L, upper4weight)
    jks = iter_list_of_randrange(2, L+1)
    return map(单调化囗, lss, jks)
    js = iter_randrange(L+1)
    #for ls, j in zip(lss, js):
    return map(单调化囗, lss, js)
def 单调化囗(ls, jk, /):
    #这是ls[]标准，允许:[11,33,22,22]
    #   若按fw()标准，这就不是 monotone polygon
    j, k = jk
    ls0 = ls[:j]
    ls1 = ls[j:]
    ls0.sort()
    ls1.sort(reverse=True)
    ls = ls0+ls1
    ls0 = ls[:k]
    ls1 = ls[k:]
    ls = ls1+ls0
    return ls





