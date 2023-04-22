#__all__:goto
r'''[[[
e ../../python3_src/seed/math/matrix_chain_product/matrix_chain_product__common.py

seed.math.matrix_chain_product.matrix_chain_product__common
py -m nn_ns.app.debug_cmd   seed.math.matrix_chain_product.matrix_chain_product__common

from seed.math.matrix_chain_product.matrix_chain_product__common import mk_mno_tree_from_unsorted_inner_arcs, mk_inner_arcs_from_mno_tree

from seed.math.matrix_chain_product.matrix_chain_product__common import check_matrix_chain_product_arg,准备囗词典序最先的最优三角化方案


#]]]'''
__all__ = r'''
    is_triangle_order
    check_pint_seq
    check_matrix_chain_product_arg
    准备囗词典序最先的最优三角化方案


    mk_offset_
    mk_unoffset_
    unoffset_arcs_


    mk_mno_tree_from_unsorted_inner_arcs
    mk_mno_tree_from_binary_arc_tree

    mk_binary_arc_tree_from_mno_tree
    mk_binary_arc_tree_from_unsorted_inner_arcs

    radix_sort__arcs
    mk_sorted_unoffseted_arcs_from_unsorted_offseted_arcs_
    mk_inner_arcs_from_mno_tree
    mk_inner_arcs_from_binary_arc_tree

    mk_binary_arc_tree_from_arc2next_triangle_vtx
    mk_arc2next_triangle_vtx_from_unsorted_inner_arcs
    mk_arc2next_triangle_vtx_from_v2ordered_vtc
    mk_arc2another_triangle_vtc_from_v2ordered_vtc
    mk_v2ordered_vtc_from_unsorted_inner_outer_arcs
    mk_v2unordered_vtc_from_unsorted_inner_outer_arcs
    mk_v2sorted_vtc_from_v2unordered_vtc
    mk_v2ordered_vtc_from_v2sorted_vtc

    iter_outer_arcs_of
    iter_unsorted_inner_outer_arcs_from_unsorted_inner_arcs
'''.split()#'''
__all__

from seed.tiny_.check import check_uint_lt
from seed.types.view.SeqLeftRotateView import SeqLeftRotateView
from seed.algo.bucket_sort.bucket_sort_per_row import bucket_sort_per_row
from seed.algo.bucket_sort.radix_sort_with_table import radix_sort_with_table

from collections import defaultdict
from itertools import pairwise



def is_triangle_order(v,x,y, /):
    #循环移动后 递增
    return v < x < y or y < v < x or x < y < v

def check_pint_seq(ls, /):
    assert all(type(d) is int for d in ls)
    assert all(d > 0 for d in ls)
    ls[:0]
    len(ls)
def check_matrix_chain_product_arg(矩阵乘法链维数序列, /):
    check_pint_seq(矩阵乘法链维数序列)
    assert len(矩阵乘法链维数序列) >= 2
    assert len(矩阵乘法链维数序列[:2]) == 2
        #seq


def 准备囗词典序最先的最优三角化方案(矩阵乘法链维数序列, /, *, may_imin):
    '-> (ls, imin, L, ls_, imin_)'
    check_matrix_chain_product_arg(矩阵乘法链维数序列)
    ls = 矩阵乘法链维数序列
    L = len(ls)
    if may_imin is None:
        imin = min(range(L), key=lambda i:ls[i])
    else:
        imin = may_imin
        check_uint_lt(L, imin)
        if not ls[imin] == min(ls): raise ValueError
    check_uint_lt(L, imin)

    ls_ = SeqLeftRotateView(ls, imin)
    imin_ = 0
    return (ls, imin, L, ls_, imin_)


def mk_offset_(L, imin, /):
    assert 0 <= imin < L
    def offset_(i, /):
        return (i-imin)%L
    return offset_

def mk_unoffset_(L, imin, /):
    assert 0 <= imin < L
    def unoffset_(i_, /):
        return (i_+imin)%L
    return unoffset_
def unoffset_arcs_(L, imin, arcs_, /):
    unoffset_ = mk_unoffset_(L, imin)
    arcs = [(unoffset_(i_), unoffset_(j_))for i_, j_ in arcs_]
    return arcs








def mk_mno_tree_from_unsorted_inner_arcs(矩阵乘法链维数序列, end4ground_outer_arc, unsorted_inner_arcs, /):
    L = len(矩阵乘法链维数序列)
    binary_arc_tree = mk_binary_arc_tree_from_unsorted_inner_arcs(L, end4ground_outer_arc, unsorted_inner_arcs)
    mno_tree = mk_mno_tree_from_binary_arc_tree(矩阵乘法链维数序列, binary_arc_tree)
    return mno_tree
def mk_mno_tree_from_binary_arc_tree(矩阵乘法链维数序列, binary_arc_tree, /):
    '-> mno_tree# mno_tree = (0,i,(ls[i],ls[i+1])) | (mno, begin, mno_tree, mid, mno_tree, end, (ls[begin],ls[mid],ls[end-1]))'
    ls = 矩阵乘法链维数序列
    L = len(ls)
    assert L >= 2
    def mk_mno_tree(binary_arc_tree, /):
        (root_arc, may_yvx_children) = binary_arc_tree
        if may_yvx_children is None:
            (x,y) = root_arc
            assert x == (y+1)%L
            i = y
            mno_tree = (0,i,(ls[i],ls[i+1]))
        else:
            (yvx, lhs_binary_arc_tree, rhs_binary_arc_tree) = may_yvx_children
            (y,v,x) = yvx
            assert is_triangle_order(v,x,y)

            #bug:begin,mid,end = y,v,x
            begin,mid,end = y,v,x+1
            lhs_mno_tree = mk_mno_tree(lhs_binary_arc_tree)
            rhs_mno_tree = mk_mno_tree(rhs_binary_arc_tree)

            mno = lhs_mno_tree[0] + rhs_mno_tree[0] + (ls[begin]*ls[mid]*ls[end-1])
            mno_tree = (mno, begin, lhs_mno_tree, mid, rhs_mno_tree, end, (ls[begin],ls[mid],ls[end-1]))
        return mno_tree
    return mk_mno_tree(binary_arc_tree)








def mk_binary_arc_tree_from_mno_tree(L, mno_tree, /):
    'binary_arc_tree = (root_arc, may ((root_arc[1], mid, root_arc[0]), binary_arc_tree, binary_arc_tree))'
    'mno_tree = (0,i,(ls[i],ls[i+1])) | (mno, begin, mno_tree, mid, mno_tree, end, (ls[begin],ls[mid],ls[end-1]))'
    def recur(mno_tree, /):
        if mno_tree[0] == 0:
            assert len(mno_tree)==3
            (_0,i,_ls_i_i1) = mno_tree
            i1 = (i+1)%L
            root_arc = leaf_arc = (i1, i)
            binary_arc_tree = (root_arc, None)
        else:
            assert len(mno_tree)==7
            (mno, begin, lhs_mno_tree, mid, rhs_mno_tree, end, ls_b_m_eneg1) = mno_tree
            root_arc = (end-1, begin)
            lhs_binary_arc_tree = recur(lhs_mno_tree)
            rhs_binary_arc_tree = recur(rhs_mno_tree)
            binary_arc_tree = (root_arc, ((root_arc[1], mid, root_arc[0]), lhs_binary_arc_tree, rhs_binary_arc_tree))
        return binary_arc_tree
    return recur(mno_tree)
def mk_binary_arc_tree_from_unsorted_inner_arcs(L, end4ground_outer_arc, unsorted_inner_arcs, /):
    arc2next_triangle_vtx = mk_arc2next_triangle_vtx_from_unsorted_inner_arcs(L, unsorted_inner_arcs)
    binary_arc_tree = mk_binary_arc_tree_from_arc2next_triangle_vtx(L, end4ground_outer_arc, arc2next_triangle_vtx)
    return binary_arc_tree











def radix_sort__arcs(L, unsorted_arcs, may_table, /):
    if may_table is None:
        table = [[] for _ in range(L)]
    else:
        table = may_table
    sorted_arcs = radix_sort_with_table([L,L], unsorted_arcs, table)
    return sorted_arcs
def mk_sorted_unoffseted_arcs_from_unsorted_offseted_arcs_(L, imin, unsorted_offseted_arcs_, /):
    unsorted_unoffseted_arcs = unoffset_arcs_(L, imin, unsorted_offseted_arcs_)
    sorted_unoffseted_arcs = radix_sort__arcs(L, unsorted_unoffseted_arcs, None)
    return sorted_unoffseted_arcs


def mk_inner_arcs_from_mno_tree(L, mno_tree, /):
    binary_arc_tree = mk_binary_arc_tree_from_mno_tree(L, mno_tree)
    inner_arcs = mk_inner_arcs_from_binary_arc_tree(L, binary_arc_tree)
    return inner_arcs
def mk_inner_arcs_from_binary_arc_tree(L, binary_arc_tree, /):
    assert L >= 2
    unsorted_inner_arcs = []
    todo_ls = [binary_arc_tree]
    while todo_ls:
        (root_arc, may_) = todo_ls.pop()
        if may_ is None:
            continue
        unsorted_inner_arcs.append(root_arc)
        (_, lhs_binary_arc_tree, rhs_binary_arc_tree) = may_
        todo_ls.append(lhs_binary_arc_tree)
        todo_ls.append(rhs_binary_arc_tree)
    assert len(unsorted_inner_arcs) == max(1, L-2)
    assert unsorted_inner_arcs
    del unsorted_inner_arcs[0]
    assert len(unsorted_inner_arcs) == max(0, L-3)
    sorted_inner_arcs = radix_sort__arcs(L, unsorted_inner_arcs, None)
    return sorted_inner_arcs







def mk_binary_arc_tree_from_arc2next_triangle_vtx(L, end4ground_outer_arc, arc2next_triangle_vtx, /):
    'binary_arc_tree = (root_arc, may ((root_arc[1], mid, root_arc[0]), binary_arc_tree, binary_arc_tree))'
    # [end4ground_outer_arc==0] -> [ground_outer_arc==(L-1,0)]即 代表的整个矩阵乘法链表达式的unoffseted_arc
    assert L >= 2
    begin4ground_outer_arc = (end4ground_outer_arc-1)%L
    root_arc = ground_outer_arc = (begin4ground_outer_arc, end4ground_outer_arc)
    def mk_tree(root_arc, /):
        (x,y) = xy = root_arc
        may_v = arc2next_triangle_vtx.get(root_arc)
        assert (x==(y+1)%L) is (may_v is None), (L, end4ground_outer_arc, root_arc, arc2next_triangle_vtx)
        if may_v is None:
            may_yvx_children = None
        else:
            v = may_v
            assert is_triangle_order(v,x,y)
            if 0:
                #bug: xy, yv, vx 皆向内;应当是 xy向内, vy,xv向外
                yv = (y,v)
                vx = (v,x)
                # [y==0][x==L-1]
                # yvx
                lhs_arc = yv
                rhs_arc = vx
            vy = (v,y)
            xv = (x,v)
            # [y==0][x==L-1]
            # yvx
            lhs_arc = vy
            rhs_arc = xv
            lhs_binary_arc_tree = mk_tree(lhs_arc)
            rhs_binary_arc_tree = mk_tree(rhs_arc)
            yvx = (y, v, x)
            may_yvx_children = (yvx, lhs_binary_arc_tree, rhs_binary_arc_tree)
        return (root_arc, may_yvx_children)
    binary_arc_tree = mk_tree(root_arc)
    return binary_arc_tree



def mk_arc2next_triangle_vtx_from_unsorted_inner_arcs(L, unsorted_inner_arcs, /):
    if __debug__:
        unsorted_inner_arcs = [*unsorted_inner_arcs]
        assert len(unsorted_inner_arcs) == max(0,L-3), (L, unsorted_inner_arcs)
    unsorted_inner_outer_arcs = iter_unsorted_inner_outer_arcs_from_unsorted_inner_arcs(L, unsorted_inner_arcs)
    v2ordered_vtc = mk_v2ordered_vtc_from_unsorted_inner_outer_arcs(L, unsorted_inner_outer_arcs)
    arc2next_triangle_vtx = mk_arc2next_triangle_vtx_from_v2ordered_vtc(L, v2ordered_vtc)
    return arc2next_triangle_vtx



def mk_arc2next_triangle_vtx_from_v2ordered_vtc(L, v2ordered_vtc, /):
    arc2next_triangle_vtx = {}
    for v, ordered_vtc in enumerate(v2ordered_vtc):
        for x, y in pairwise(ordered_vtc):
            # triangle(v,x,y)
            assert is_triangle_order(v,x,y), (L, (v,x,y), (v, ordered_vtc))
            xy = (x,y)
            arc2next_triangle_vtx[xy] = v
    return arc2next_triangle_vtx


def mk_arc2another_triangle_vtc_from_v2ordered_vtc(L, v2ordered_vtc, /):
    arc2another_triangle_vtc = defaultdict(list)
    for v, ordered_vtc in enumerate(v2ordered_vtc):
        for x, y in pairwise(ordered_vtc):
            # triangle(v,x,y)
            xy = (x,y) if x < y else (y,x)
            arc2another_triangle_vtc[xy].append(v)
    arc2another_triangle_vtc = {**arc2another_triangle_vtc}
    return arc2another_triangle_vtc

def mk_v2ordered_vtc_from_unsorted_inner_outer_arcs(L, unsorted_inner_outer_arcs, /):
    v2unordered_vtc = mk_v2unordered_vtc_from_unsorted_inner_outer_arcs(L, unsorted_inner_outer_arcs)
    v2sorted_vtc = mk_v2sorted_vtc_from_v2unordered_vtc(L, v2unordered_vtc)
    v2ordered_vtc = mk_v2ordered_vtc_from_v2sorted_vtc(L, v2sorted_vtc)
    return v2ordered_vtc

def mk_v2unordered_vtc_from_unsorted_inner_outer_arcs(L, unsorted_inner_outer_arcs, /):
    #unsorted_inner_outer_arcs = [*unsorted_inner_outer_arcs]; print(unsorted_inner_outer_arcs)
    v2unordered_vtc = [[] for _ in range(L)]
    for i, j in unsorted_inner_outer_arcs:
        assert not i == j
        assert 0 <= i < L
        assert 0 <= j < L
        v2unordered_vtc[i].append(j)
        v2unordered_vtc[j].append(i)
    return v2unordered_vtc

def mk_v2sorted_vtc_from_v2unordered_vtc(L, v2unordered_vtc, /):
    v2sorted_vtc = bucket_sort_per_row(L, v2unordered_vtc, None)
    return v2sorted_vtc

def mk_v2ordered_vtc_from_v2sorted_vtc(L, v2sorted_vtc, /):
    def iter_(v2sorted_vtc, /):
        for v, sorted_vtc in enumerate(v2sorted_vtc):
            k = -1
            for k, u in enumerate(sorted_vtc):
                if v < u: break
            else:
                k += 1
            if k > 0:
                assert sorted_vtc[k-1] < v
            if k < len(sorted_vtc):
                assert v < sorted_vtc[k]
            ordered_vtc = sorted_vtc[k:] + sorted_vtc[:k]
            yield ordered_vtc

    v2ordered_vtc = [*iter_(v2sorted_vtc)]
    return v2ordered_vtc


def iter_outer_arcs_of(L, /):
    assert L >= 1
    if L==1:
        return;yield
    assert L >= 2
    if L==2:
        yield (0,1)
        return
    assert L >= 3
    for i in range(L):
        j = (i+1)%L
        arc = (i, j)
        yield arc
def iter_unsorted_inner_outer_arcs_from_unsorted_inner_arcs(L, unsorted_inner_arcs, /):
    yield from unsorted_inner_arcs
    outer_arcs = iter_outer_arcs_of(L)
    yield from outer_arcs


