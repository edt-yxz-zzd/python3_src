#__all__:goto
r'''[[[
e ../../python3_src/seed/math/matrix_chain_product/词典序最先的最优三角化方案囗立方算法囗.py
seed.math.matrix_chain_product.词典序最先的最优三角化方案囗立方算法囗
py -m nn_ns.app.debug_cmd   seed.math.matrix_chain_product.词典序最先的最优三角化方案囗立方算法囗

from seed.math.matrix_chain_product.词典序最先的最优三角化方案囗立方算法囗 import 词典序最先的最优三角化方案囗立方算法囗



#]]]'''
__all__ = r'''
    词典序最先的最优三角化方案囗立方算法囗
'''.split()#'''
__all__


from seed.math.matrix_chain_product.matrix_chain_product__common import mk_offset_, radix_sort__arcs, 准备囗词典序最先的最优三角化方案
from seed.math.matrix_chain_product.matrix_chain_product__dynamic_programming__O_NNN import matrix_chain_product__dynamic_programming__O_NNN


def 词典序最先的最优三角化方案囗立方算法囗(矩阵乘法链维数序列, /, *, may_imin):
    '-> (mno, L, imin, sorted_inner_arcs_)'
    (ls, imin, L, ls_, imin_) = 准备囗词典序最先的最优三角化方案(矩阵乘法链维数序列, may_imin=may_imin)
    num_matrices2mno_begin_mids_end_tpls_ = matrix_chain_product__dynamic_programming__O_NNN(ls_)
    if 0:
        #通通取消
        offset_idx_ = mk_offset_(L, imin)
        def L_(i_, /):
            return i_%L
    else:
        offset_idx_ = mk_offset_(L, 0)
        def L_(i_, /):
            return i_

    num_matrices2begin2mids_ = []
    for num_matrices, mno_begin_mids_end_tpls in enumerate(num_matrices2mno_begin_mids_end_tpls_):
        assert len(num_matrices2begin2mids_) == num_matrices
        begin2mids_ = {}
        for mno, begin, mids, end in mno_begin_mids_end_tpls:
            assert end-begin-1 == num_matrices
            begin_ = offset_idx_(begin)
            mids_ = [*map(offset_idx_, mids)]
            begin2mids_[begin_] = mids_
        num_matrices2begin2mids_.append(begin2mids_)
    num_matrices2begin2mids_
    #######
    num_matrices2begin2mid_leftmost_nodes_pair_ = []
    def mk_leftmost_nodes_or_self_(num_matrices, begin_, /):
        #最左不必是叶节点，范围不一定是2
        if num_matrices >= 2:
            (mid_, leftmost_nodes_) = num_matrices2begin2mid_leftmost_nodes_pair_[num_matrices][begin_]
        else:
            leftmost_nodes_ = []
        return leftmost_nodes_

    for num_matrices, begin2mids_ in enumerate(num_matrices2begin2mids_):
        assert len(num_matrices2begin2mid_leftmost_nodes_pair_) == num_matrices
        begin2mid_leftmost_nodes_pair_ = {}
        for begin_, mids_ in begin2mids_.items():
            end_ = L_(num_matrices+begin_+1)
            self_ = (*sorted([begin_, L_(begin_+num_matrices)]),)
            xs = []
            for mid_ in mids_:
                if mid_ == L_(begin_+1):
                    leftmost_nodes_ = mk_leftmost_nodes_or_self_(num_matrices-L_(mid_-begin_), mid_)
                else:
                    leftmost_nodes_ = mk_leftmost_nodes_or_self_(L_(mid_-begin_), begin_)
                leftmost_nodes_ = [*leftmost_nodes_, self_]
                xs.append((leftmost_nodes_, mid_))

            (leftmost_nodes_, mid_) = min(xs)
            leftmost_nodes_ = min([self_,], leftmost_nodes_)
            mid_leftmost_nodes_pair_ = (mid_, leftmost_nodes_)
            begin2mid_leftmost_nodes_pair_[begin_] = mid_leftmost_nodes_pair_

        num_matrices2begin2mid_leftmost_nodes_pair_.append(begin2mid_leftmost_nodes_pair_)
    num_matrices2begin2mid_leftmost_nodes_pair_
    #######
    #######
    #######
    if 0:
        print(num_matrices2mno_begin_mids_end_tpls_)
        print(num_matrices2begin2mids_)
        print(num_matrices2begin2mid_leftmost_nodes_pair_)
    #######
    unsorted_inner_arcs_ = []
    todo_arcs_ = []
    def mid_of_(i_, j_, /):
        num_matrices = j_-i_
        (mid_, leftmost_nodes_) = num_matrices2begin2mid_leftmost_nodes_pair_[num_matrices][i_]
        return mid_
    def topdown(i_, j_, /):
        assert i_ < j_
        if i_+1==j_:
            return
        mid_ = mid_of_(i_, j_)
        #print(i_, j_)
        #print(mid_)
        _put_todo(i_, mid_)
        _put_todo(mid_, j_)

    def _put_todo(i_, j_, /):
        assert 0 <= i_ < j_ < L
        if j_-i_ >= 2:
            arc_ = (i_, j_)
            unsorted_inner_arcs_.append(arc_)
            todo_arcs_.append(arc_)
    #end-def _put_todo(i_, j_, /):
    topdown(0, L-1)
        #避开_put_todo
    while todo_arcs_:
        (i_, j_) = arc_ = todo_arcs_.pop()
        topdown(i_, j_)

    sorted_inner_arcs_ = radix_sort__arcs(L, unsorted_inner_arcs_, None)
    assert len(sorted_inner_arcs_) == max(0, L-3), sorted_inner_arcs_
    mno = 0 if L==2 else num_matrices2mno_begin_mids_end_tpls_[L-1][0][0]
    return (mno, L, imin, sorted_inner_arcs_)

#end-def 词典序最先的最优三角化方案囗立方算法囗(矩阵乘法链维数序列, /, *, may_imin):


