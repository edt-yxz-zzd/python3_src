#__all__:goto
r'''[[[
e ../../python3_src/seed/math/matrix_chain_product/test4matrix_chain_product__polygon_partitioning__O_NlogN.py

seed.math.matrix_chain_product.test4matrix_chain_product__polygon_partitioning__O_NlogN


py -m nn_ns.app.debug_cmd   seed.math.matrix_chain_product.test4matrix_chain_product__polygon_partitioning__O_NlogN

L2num_tests, upper4weight, version, _turnon_debug

py -m seed.math.matrix_chain_product.test4matrix_chain_product__polygon_partitioning__O_NlogN @随机测试囗囗矩阵乘法链囗多边形囗词典序最先的最优三角化方案囗类同排序算法耗时 '--L2num_tests={L:1000//L for L in range(2,100)}' '--upper4weight=10000' '--version=3' '--_turnon_debug=0'









#]]]'''
__all__ = r'''
    单例测试囗囗矩阵乘法链囗多边形囗词典序最先的最优三角化方案囗类同排序算法耗时
    随机测试囗囗矩阵乘法链囗多边形囗词典序最先的最优三角化方案囗类同排序算法耗时
'''.split()#'''
__all__

from itertools import islice

from seed.math.matrix_chain_product.matrix_chain_product__polygon_partitioning__O_NlogN import matrix_chain_product__polygon_partitioning__O_NlogN, std_api4matrix_chain_product__polygon_partitioning__O_NlogN
from seed.math.matrix_chain_product.matrix_chain_product__dynamic_programming__O_NNN import matrix_chain_product__dynamic_programming__O_NNN, std_api4matrix_chain_product__dynamic_programming__O_NNN
from seed.math.matrix_chain_product.词典序最先的最优三角化方案囗立方算法囗 import 词典序最先的最优三角化方案囗立方算法囗



from seed.math.matrix_chain_product.matrix_chain_product__common4test import 迭代囗随机生成囗矩阵乘法链维数序列



def 单例测试囗囗矩阵乘法链囗多边形囗词典序最先的最优三角化方案囗类同排序算法耗时(version, ls, /, *, _turnon_debug):
    L = len(ls)
    #version = 2
    try:
        if version==1:
            (MNO4whole, imin, inner_idx_arcs_, kind2ij_ls) = matrix_chain_product__polygon_partitioning__O_NlogN(ls, may_imin=None, _turnon_debug=_turnon_debug)
            mno = 0 if L==2 else matrix_chain_product__dynamic_programming__O_NNN(ls)[L-1][0][0]
            def f():
                assert MNO4whole == mno, (version, L, ls, mno, (MNO4whole, inner_idx_arcs_, kind2ij_ls))
        elif version==2:
            mno_tree__testing = std_api4matrix_chain_product__polygon_partitioning__O_NlogN(ls)
            mno_tree__ans = std_api4matrix_chain_product__dynamic_programming__O_NNN(ls)
            def f():
                assert mno_tree__testing[0] == mno_tree__ans[0], (version, L, ls, (mno_tree__testing[0], mno_tree__ans[0]), (mno_tree__testing, mno_tree__ans))
        elif version==3:
            (MNO4whole, imin, inner_idx_arcs_, kind2ij_ls) = matrix_chain_product__polygon_partitioning__O_NlogN(ls, may_imin=None, _turnon_debug=_turnon_debug)
            (_mno, _L, _imin, sorted_inner_arcs_) = 词典序最先的最优三角化方案囗立方算法囗(ls, may_imin=None)
            def f():
                assert MNO4whole == _mno, (version, L, ls, (imin, _imin), (MNO4whole, _mno), (inner_idx_arcs_, sorted_inner_arcs_))
                assert inner_idx_arcs_ == sorted_inner_arcs_, (version, L, ls, (imin, _imin), (MNO4whole, _mno), (inner_idx_arcs_, sorted_inner_arcs_))
        else:
            raise Exception(version)
    except Exception as e:
        raise Exception((e, version, L, ls))
    f()


def 随机测试囗囗矩阵乘法链囗多边形囗词典序最先的最优三角化方案囗类同排序算法耗时(*, L2num_tests, upper4weight, version, _turnon_debug):
    lss = [
    [1,1]
    ,[9577, 3341, 3263, 4362, 8859, 4464]
    #
    ,[1260, 2101, 9659, 2273, 9458, 8399, 9039, 5002, 1281]
    #   比下面少3个:, 4880, 7349, 6392
    #
    ,[1260, 4880, 2101, 9659, 2273, 9458, 8399, 9039, 7349, 5002, 6392, 1281]
    ,[6392, 1281, 1260, 4880, 2101, 9659, 2273, 9458, 8399, 9039, 7349, 5002]
    ,[5900, 2220, 711, 2354, 8990, 2424, 3635]
    ,[8499, 1895, 5503, 936, 566, 1102]
    ,[5779, 7186, 7654, 9627, 5932, 7396]
    ,[5366, 2499, 6032, 1410, 1452, 8474]
    ,[44, 33, 55, 11, 22, 66]
    ,[11,33,22,44]
    ,[10,11,25,40,12]
    ,[1,2,3,2,2]
    ,[1,3,2,2]
    ,[1,1,1]
    ,[1,1,1,1]
    ,[1,1,1,1,1]
    ,[1,2,3,4]
    ,[2,1,3,4]
    ,[3,2,1,4]
    ,[3,1,2,4]
    ,[3,2,4,6]
    ,[3,2,4,12]
    ,[3,2,4,24]
    ,[11,11,33,22]
    ,[11,44,33,33,22]
    ,[11,33,22,22,11]
    ,[1,1,2,3,2,2,1]
    ,[1,1,1,2,2,2,3,3,3,2,2,2,1,1]
    ,[181, 5592, 1359, 2753, 2904, 5844, 3831, 6660, 4933, 3040, 9856, 6983, 2344, 6570, 8828, 5956, 4662, 9566]
    ]
    for ls in lss:
        print(f'L = {len(ls)}; ls = {ls}')
        单例测试囗囗矩阵乘法链囗多边形囗词典序最先的最优三角化方案囗类同排序算法耗时(version, ls, _turnon_debug=_turnon_debug)

    for L, num_tests in sorted(L2num_tests.items()):
        print(f'L = {L}')
        it = 迭代囗随机生成囗矩阵乘法链维数序列(L, upper4weight)
        it = islice(it, num_tests)
        for ls in it:
            print(f'L = {L}; ls = {ls}')
            单例测试囗囗矩阵乘法链囗多边形囗词典序最先的最优三角化方案囗类同排序算法耗时(version, ls, _turnon_debug=_turnon_debug)

if __name__ == "__main__":
    from seed.recognize.cmdline.adhoc_argparser import adhoc_argparser__main__call, AdhocArgParserError, _NOP_
    adhoc_argparser__main__call(globals(), None)
        #main()


