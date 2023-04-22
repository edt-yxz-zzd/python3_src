#__all__:goto
r'''[[[
[[[
e ../../python3_src/seed/math/matrix_chain_product/matrix_chain_product__polygon_partitioning__O_NlogN.py
部分修改:copy from:
    view script/matrix_chain_product[20221118].py
===
see:
    view ../../python3_src/seed/math/matrix_chain_product/matrix_chain_product__polygon_partitioning__O_NlogN.py
    view script/matrix_chain_product[20221118].py
    view others/book/matrix_chain_product/Computation of matrix chain products I,II(1984)(Hu)(Shing)[polygon partitioning].pdf.txt
    view ../../python3_src/seed/types/MergeableHeap.py
    view ../../python3_src/seed/types/MergeableHeap__immutable_tree.py
    view ../../python3_src/seed/types/MergeableHeap__mutable_tree.py
]]]

[[
===
ls=range(1,10000)
RecursionError:修改:
    _remove_arcs_as_nodes_of_tree_emplace_if_not
    _iter_all_unorder_ceil_arcs_
    _iter_all_unorder_ceil_hidden_children_
===
ls=[181, 5592, 1359, 2753, 2904, 5844, 3831, 6660, 4933, 3040, 9856, 6983, 2344, 6570, 8828, 5956, 4662, 9566]
_init_unorder_ceil_arcs4curr_arc_
    #bug:leftmost/rightmost在main_loop里没有更新！已更正！
    def main_loop(root_, idx_r0psh_arcs_, /):
        leftmost_above_or_side_arc4curr_arc_
        rightmost_above_or_side_arc4curr_arc_
===
++tmp4curr_arc_
++_check_tmp4curr_arc_
++_update1_tmp4curr_arc_
++_update2_tmp4curr_arc_
===
]]

e ../../python3_src/seed/math/matrix_chain_product/matrix_chain_product__polygon_partitioning__O_NlogN.py
e ../../python3_src/seed/math/matrix_chain_product/matrix_chain_product__common.py
e ../../python3_src/seed/math/matrix_chain_product/matrix_chain_product__dynamic_programming__O_NNN.py
e ../../python3_src/seed/math/matrix_chain_product/词典序最先的最优三角化方案囗立方算法囗.py
view ../../python3_src/nn_ns/app/adhoc_argparser__main__call8module.py

seed.math.matrix_chain_product.matrix_chain_product__polygon_partitioning__O_NlogN
py -m nn_ns.app.debug_cmd   seed.math.matrix_chain_product.matrix_chain_product__polygon_partitioning__O_NlogN

py -m nn_ns.app.adhoc_argparser__main__call8module       seed.math.matrix_chain_product.matrix_chain_product__polygon_partitioning__O_NlogN @matrix_chain_product__polygon_partitioning__O_NlogN  --may_imin=None  '--_turnon_debug=0'  ='range(1,10000)'
    #递归深度？
    #RecursionError: maximum recursion depth exceeded
    #   _recur__sub_root_/_recur__parent_
py -m seed.math.matrix_chain_product.test4matrix_chain_product__polygon_partitioning__O_NlogN @随机测试囗囗矩阵乘法链囗多边形囗词典序最先的最优三角化方案囗类同排序算法耗时 '--L2num_tests={L:1000//L for L in range(2,100)}' '--upper4weight=10000' '--version=3' '--_turnon_debug=0'

from seed.math.matrix_chain_product.matrix_chain_product__polygon_partitioning__O_NlogN import matrix_chain_product__polygon_partitioning__O_NlogN, std_api4matrix_chain_product__polygon_partitioning__O_NlogN

#]]]'''
__all__ = r'''
matrix_chain_product__polygon_partitioning__O_NlogN
    矩阵乘法链囗多边形囗词典序最先的最优三角化方案囗等同排序算法耗时
    std_api4matrix_chain_product__polygon_partitioning__O_NlogN
    tail4std_api4matrix_chain_product__polygon_partitioning__O_NlogN



'''.split()#'''
#囗矩阵乘法链维数序列囗相关函数
#    Imin8Arc_
#    IdxArc_
__all__

from fractions import Fraction
from itertools import chain
from seed.tiny import fst, snd
from seed.types.MergeableHeap import MergeableHeap
from seed.algo.bucket_sort.bucket_sort_per_row import bucket_sort_per_row
from seed.algo.bucket_sort.radix_sort_with_table import radix_sort_with_table

from seed.math.matrix_chain_product.matrix_chain_product__common import is_triangle_order, 准备囗词典序最先的最优三角化方案
from seed.math.matrix_chain_product.matrix_chain_product__common import unoffset_arcs_, mk_mno_tree_from_unsorted_inner_arcs

from seed.math.matrix_chain_product.matrix_chain_product__dynamic_programming__O_NNN import std_api4matrix_chain_product__dynamic_programming__O_NNN
    #_ONNN_debug__MNO_between_curr_arc_ceil_arcs_
    #_ONNN_debug__MNO_above_

class 囗矩阵乘法链维数序列囗相关函数:
    def fw(sf, i_, /):
        return sf.ls_[i_], i_
    def lt__fw(sf, i_, j_, /):
        return sf.fw(i_) < sf.fw(j_)
    def lt__ls(sf, i_, j_, /):
        return sf.ls_[i_] < sf.ls_[j_]
    def __init__(sf, 矩阵乘法链维数序列, /, *, may_imin, _turnon_debug):
        (ls, imin, L, ls_, imin_) = 准备囗词典序最先的最优三角化方案(矩阵乘法链维数序列, may_imin=may_imin)

        save = (ls, imin)
        del ls, imin
        ls_, imin_, L, save


        sf.ls_ = ls_
            #enable:sf.fw)
        if L >= 3:
            #bug:
            #   [i0_,i1_,i2_]= nsmallest(3, range(L), key=sf.fw)
            #   ground_triangle_ = i012_ = (i0_,i1_,i2_) or (i0_,i2_,i1_)
            #逻辑错误:{i0_,i1_}确实有，但第三个，必须在i1_之后，除非[i1_==L-1]
            # 现改正:012-->01X
            i0_ = imin_
            i1_ = min(range(1,L), key=sf.fw)
            if i1_ == L-1:
                iX_ = min(range(1,L-1), key=sf.fw)
                ground_triangle_ = (i0_,iX_,i1_)
                assert i0_ < iX_ < i1_
            else:
                iX_ = min(range(i1_+1,L), key=sf.fw)
                ground_triangle_ = (i0_,i1_,iX_)
                assert i0_ < i1_ < iX_
            ground_triangle_
            assert is_triangle_order(*ground_triangle_)
            assert ground_triangle_[0] < ground_triangle_[1] < ground_triangle_[2]

        sf._turnon_debug = _turnon_debug
        sf.L = L
        sf.save = save
        sf.imin_ = imin_
        if L >= 3:
            sf._init4get_side_product_above_curr_arc_()
        if L >= 3:
            sf.ground_triangle_ = ground_triangle_

    def _init4get_side_product_above_curr_arc_(sf, /):
        #get_side_product_above_curr_arc_
        L = sf.L
        assert L >= 3
        ls_ = sf.ls_
        accs_ = [0]
        for j_ in range(1, L):
            i_ = j_-1
            accs_.append(accs_[-1]+ls_[i_]*ls_[j_])
        accs_.append(accs_[-1]+ls_[-1]*ls_[0])
        assert len(accs_) == L+1
        sf.accs_ = accs_


    def 迭代囗三角化方案囗潜在的潜在的横对角线(sf, /):
        'one_sweep_algorithm-extend arc with upper triangle vtx'
        L = sf.L
        assert L >= 3
        ground_triangle_ = sf.ground_triangle_
        imin_ = sf.imin_
        assert imin_ == 0

        stack = [imin_] #0 == imin_
        def _mk_idx_pph_arc(i_, /):
            i_up_ = stack.pop()
            #bug:idx_pph_arc_ = sf.mk_idx_arc__iup_(i_up_, (i_, stack[-1]))
            idx_pph_arc_ = sf.mk_idx_arc__iup_(i_up_, (stack[-1], i_))
            return idx_pph_arc_

        for i_ in range(imin_+1, L-1):
            while sf.lt__fw(i_, stack[-1]):
                yield _mk_idx_pph_arc(i_)
            stack.append(i_)
        assert len(stack) >= 2

        if 1:
            i_ = L-1
            while len(stack) >= 3 and sf.lt__fw(i_, stack[-1]):
                yield _mk_idx_pph_arc(i_)
            stack.append(i_)
        assert len(stack) >= 3

        if 1:
            i_ = imin_
            while len(stack) >= 4:
                yield _mk_idx_pph_arc(i_)
        assert len(stack) == 3

        assert stack == [*ground_triangle_], (stack, ground_triangle_)
        #    inner edges of ground_triangle_ are children of root of idx_arc_tree_(root is Imin8Arc_(imin_))
        #曾经的反例:[11,33,22,44] --> [11,22,44]
        #   现在 由i012_改为i01X_
        return
    #end-def 迭代囗三角化方案囗潜在的潜在的横对角线(sf, /):

    def mk_idx_arc__iup_(sf, i_up_, idx_arc_, /):
        L = sf.L
        assert L >= 3

        (i_, j_) = idx_arc_
        if j_ > 0:
            assert 0 <= i_ < i_up_ < j_ < L
        else:
            assert j_ == 0 < i_ < i_up_ < L
        idx_arc_ = IdxArc_(i_, j_)
        idx_arc_.i_up_ = i_up_
        return idx_arc_

    def mk_idx_arc_tree_(sf, idx_pph_arcs_, /):
        'fan_out tree growing_from_ground_to_up'
        # -> (root_, i_up2may_idx_pph_arc_)

        L = sf.L
        assert L >= 3
        ground_triangle_ = sf.ground_triangle_
        imin_ = sf.imin_
        assert imin_ == 0

        #idx_pph_arcs_ = [*sf.迭代囗三角化方案囗潜在的潜在的横对角线()]
        assert len(idx_pph_arcs_) == L-3
        idx_pph_arcs_[:0]


        i_up2may_idx_pph_arc_ = [None]*L
        def _fill__i_up2may_idx_pph_arc_():
            for idx_pph_arc_ in idx_pph_arcs_:
                assert i_up2may_idx_pph_arc_[idx_pph_arc_.i_up_] is None
                i_up2may_idx_pph_arc_[idx_pph_arc_.i_up_] = idx_pph_arc_
            assert i_up2may_idx_pph_arc_.count(None) == 3
            assert all(i_up2may_idx_pph_arc_[i_] is None for i_ in ground_triangle_)
        _fill__i_up2may_idx_pph_arc_()

        root_ = Imin8Arc_(imin_)
        def _iter_tree_children_of_root_():
            s = {*ground_triangle_}
            #bug:for may_child_ in i_up2may_idx_pph_arc_:
            #   order of root_.tree_children_ matter
            for idx_pph_arc_ in idx_pph_arcs_:
                child_ = idx_pph_arc_
                if {*child_} < s:
                    yield child_
        root_.tree_children_ = [*_iter_tree_children_of_root_()]
        assert (L>=4) <= len(root_.tree_children_) <= 3
        #   order of root_.tree_children_ matter

        def _init__tree_children_of_nonroot_():
            for parent_ in idx_pph_arcs_:
                parent_.tree_children_ = []
                    # init
                    # why not lhs_child_+rhs_child_??
                    #   some arcs will be removed from tree
                    #
        _init__tree_children_of_nonroot_()

        #改为内边函数，因为没啥用，树一直在变动
        def __tree_child2parent_(sf, root_, i_up2may_idx_pph_arc_, child_, /):
            if child_ is root_:
                raise logic-err
            #begin-__tree_child2parent_
            if child_ in root_.tree_children_:
                return root_

            k_ = max(child_, key=sf.fw)
            parent_ = i_up2may_idx_pph_arc_[k_]
            assert parent_ is not None
            if __debug__:
                [e_] = {*parent_}&{*child_}
                assert {*child_} == {e_,k_}
            #end-__tree_child2parent_
            return (k_, parent_)

        def _fill__tree_children_of_nonroot_():
            #direction:
            #   find:child_ -> parent_
            #   but set/get:parent_ -> child_
            for child_ in idx_pph_arcs_:
                i_up_ = child_.i_up_
                if child_ in root_.tree_children_:
                    continue
                (k_, parent_) = __tree_child2parent_(sf, root_, i_up2may_idx_pph_arc_, child_)
                parent_.tree_children_.append(child_)

                'fan_out tree growing_from_ground_to_up'
                    # from_ground_to_up --> lhs_child_/rhs_child_
                    # fan_out --> (parent_->child_)
                    # why not fan_in?? the tree will change many times
        _fill__tree_children_of_nonroot_()

        def _check_len_children():
            for parent_ in idx_pph_arcs_:
                # case len(parent_.tree_children_) of:
                #   2 => no child be outer edge
                #   1 => one child be outer edge
                #   0 => two children be outer edge

                (i_, j_) = parent_
                if len(parent_.tree_children_):
                    assert not (i_+2)%L == j_
                else:
                    assert (i_+1) == parent_.i_up_
                    assert (i_+2)%L == j_
        _check_len_children()

        def _():
            for parent_ in idx_pph_arcs_:
                assert 0 <= len(parent_.tree_children_) <= 2
        _()
        return (root_, i_up2may_idx_pph_arc_)
    #end-def mk_idx_arc_tree_(sf, idx_pph_arcs_, /):

    r'''[[[ #RecursionError: maximum recursion depth exceeded #   _recur__parent_/_recur__sub_root_
    def _remove_arcs_as_nodes_of_tree_emplace_if_not(sf, arc2ok_, root_, /):
        assert type(root_) is Imin8Arc_
        def _recur__parent_(outs, parent_, /):
            #has .tree_children_
            #IdxArc_ and whole tree root_
            assert type(parent_) is IdxArc_ or parent_ is root_

            for child_ in parent_.tree_children_:
                _recur__sub_root_(outs, child_)
            return
        def _recur__sub_root_(outs, sub_root_, /):
            assert type(sub_root_) is IdxArc_ or sub_root_ is root_

            parent_ = sub_root_
            if parent_ is root_ or arc2ok_(parent_):
                outs.append(parent_)
                outs = []
                _recur__parent_(outs, parent_)
                parent_.tree_children_ = outs
            else:
                # remove parent_
                _recur__parent_(outs, parent_)
                pass
            return
        def _():
            outs = []
            _recur__sub_root_(outs, root_)
            [_root_] = outs
            assert _root_ is root_
        _()
        return None
    #]]]'''
    def _remove_arcs_as_nodes_of_tree_emplace_if_not(sf, arc2ok_, root_, /):
        assert type(root_) is Imin8Arc_
        #to avoid: RecursionError: maximum recursion depth exceeded
        ls = []
        def put(outs, sub_root_, /):
            ls.append((outs, sub_root_))
        def put_children(outs, parent_, /):
            for child_ in parent_.tree_children_:
                put(outs, child_)
        def main_loop():
            _outs = []
            put(_outs, root_)
            while ls:
                (outs, sub_root_) = ls.pop()
                parent_ = sub_root_
                if parent_ is root_ or arc2ok_(parent_):
                    outs.append(parent_)
                    outs = []
                    put_children(outs, parent_)
                    parent_.tree_children_ = outs
                else:
                    # remove parent_
                    put_children(outs, parent_)
            return _outs
        def main():

            [_root_] = main_loop()
            assert _root_ is root_
        main()
        return None


    def 潜在的潜在的横对角线树至第二版的除零的类横对角线树囗就地移除(sf, idx_pph_arcs_, root_, /):
        #移除 部分 潜在的潜在的横对角线
        #只保留 除零的类横对角线囗第二版
        L = sf.L
        assert L >= 3
        imin_ = sf.imin_
        assert imin_ == 0
        ls_ = sf.ls_


        def is_除零的类横对角线囗第二版(idx_arc_, /):
            (i_,j_) = idx_arc_
            return (imin_ < i_ < j_) and (max(ls_[i_],ls_[j_]) < ls_[idx_arc_.i_up_])

        sf._remove_arcs_as_nodes_of_tree_emplace_if_not(is_除零的类横对角线囗第二版, root_)
        idx_r0psh_arcs_ = [*filter(is_除零的类横对角线囗第二版, idx_pph_arcs_)]
        return idx_r0psh_arcs_
    #end-def 潜在的潜在的横对角线树至第二版的除零的类横对角线树囗就地移除(sf, root_, /):


    def two_vtc5arcs_(sf, arcs_, /):
        return [*map(sf.two_vtx5curr_arc_, arcs_)]
    def two_vtx5curr_arc_(sf, curr_arc_, /):
        #allow pair/tuple
        if type(curr_arc_) is Imin8Arc_:
            i_ = curr_arc_.i_
            return (i_, i_)

        assert type(curr_arc_) is IdxArc_ or type(curr_arc_) is tuple, (type(curr_arc_), curr_arc_)
        (i_, j_) = curr_arc_
        return (i_, j_)

    def get_side_product_above_curr_arc_(sf, curr_arc_, /):
        d = sf._get_side_product_above_curr_arc_(curr_arc_)
        if sf._turnon_debug and __debug__:
            _d = sf._ON_debug__diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_(curr_arc_, []) + sf.get_base_product_of_curr_arc_(curr_arc_)
            assert _d==d, (d, _d, sf.two_vtx5curr_arc_(curr_arc_))
        return d
    def _get_side_product_above_curr_arc_(sf, curr_arc_, /):
        accs_ = sf.accs_
        if type(curr_arc_) is Imin8Arc_:
            return accs_[-1]
        (i_, j_) = sf.two_vtx5curr_arc_(curr_arc_)
        assert 0 <= i_ <= j_ < sf.L
        r = accs_[j_] -accs_[i_]
        assert (r > 0) ^ (i_ == j_ > 0)
        return r
    def get_base_product_of_curr_arc_(sf, curr_arc_, /):
        ls_ = sf.ls_
        (i_, j_) = sf.two_vtx5curr_arc_(curr_arc_)
        return ls_[i_] *ls_[j_] if not i_ == j_ else 0
    def get_diff__side_product_above_curr_arc__base_product_above_curr_arc_(sf, curr_arc_, /):
        d = sf.get_side_product_above_curr_arc_(curr_arc_)-sf.get_base_product_of_curr_arc_(curr_arc_)
        assert (d > 0)
            #因为 除零的类横对角线囗第二版 的 定义:上方权值 比 横线 大
        if sf._turnon_debug and __debug__:
            _d = sf._ON_debug__diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_(curr_arc_, [])
            assert _d==d, (d, _d, sf.two_vtx5curr_arc_(curr_arc_))
        return d

    def get_min_weight4curr_arc_(sf, curr_arc_, /):
        (i_, j_) = sf.two_vtx5curr_arc_(curr_arc_)
        ls_ = sf.ls_
        return min(ls_[i_], ls_[j_])
    def find_the_focus_vtx4H0_above_curr_arc_(sf, curr_arc_, leftmost_above_or_side_arc4curr_arc_, rightmost_above_or_side_arc4curr_arc_, /):
        base_product4disappear_arcL4H0_ = sf.get_base_product_of_curr_arc_(leftmost_above_or_side_arc4curr_arc_)
        base_product4disappear_arcR4H0_ = sf.get_base_product_of_curr_arc_(rightmost_above_or_side_arc4curr_arc_)
        if type(curr_arc_) is Imin8Arc_:
            delta4h0 = base_product4disappear_arcL4H0_ + base_product4disappear_arcR4H0_
            focus_vtx4H0_above_curr_arc_ = sf.imin_

        else:
            r'''[[[无需如此！否则 横对角线
            (focus_vtx4H0_above_curr_arc_, delta4h0) = (curr_arc_.i_lhs_, base_product4disappear_arcL4H0_) if (ls_[curr_arc_.i_lhs_], -base_product4disappear_arcL4H0_) <= (ls_[curr_arc_.i_rhs_], -base_product4disappear_arcR4H0_) else (curr_arc_.i_rhs_, base_product4disappear_arcR4H0_)
            #]]]'''
            (i_, j_) = sf.two_vtx5curr_arc_(curr_arc_)
            assert i_ < j_
            k_ = min(i_, j_, key=sf.fw)
            focus_vtx4H0_above_curr_arc_ = k_
            delta4h0 = base_product4disappear_arcL4H0_ if i_==k_ else base_product4disappear_arcR4H0_
        #delta4H0 = delta4h0*min_weight4curr_arc_
        return (focus_vtx4H0_above_curr_arc_, delta4h0)


    def calc_diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_(sf, curr_arc_, unorder_ceil_arcs_, /):
        f = sf.get_diff__side_product_above_curr_arc__base_product_above_curr_arc_
        d = f(curr_arc_)
        d -= sum(map(f, unorder_ceil_arcs_))
        diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_ = d
        return diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_

    def _ON_debug__iter_all_sides_above_(sf, curr_arc_, /):
        L = sf.L
        imin_ = sf.imin_

        (i_, j_) = sf.two_vtx5curr_arc_(curr_arc_)
        assert 0 <= i_ <= j_ < L
        if i_ == j_:
            #if not j_ == imin_:raise logic-err
            if not j_ == imin_:
                s = range(i_, j_)
            else:
                s = range(L)
        else:
            if not imin_  <= i_ < j_:raise logic-err
            s = range(i_, j_)
        for i_ in s:
            j_ = (i_+1)%L
            yield (i_, j_)
        return
    def _ON_debug__all_sides_above_(sf, curr_arc_, /):
        return [*sf._ON_debug__iter_all_sides_above_(curr_arc_)]

    def _ON_debug__all_sides_between_curr_arc_ceil_arcs_(sf, curr_arc_, unorder_ceil_arcs_, /):
        f = sf._ON_debug__iter_all_sides_above_
        s = {*()}
        s.update(*map(f, unorder_ceil_arcs_))
        arcs_ = [arc_ for arc_ in f(curr_arc_) if arc_ not in s]


        assert arcs_ == sorted(arcs_)
        arcs_.extend((i_,j_) for (i_,j_) in sf.two_vtc5arcs_(unorder_ceil_arcs_) if not i_ == j_)
            #bug: 忘记 填充 unorder_ceil_arcs_ 本身！
        arcs_.sort()

        return arcs_
    def _ON_debug__diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_(sf, curr_arc_, unorder_ceil_arcs_, /):
        #-> diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_
        #-> diff__side_product_between_curr_arc_ceil_arcs__base_product_
        f = sf.get_base_product_of_curr_arc_
        return sum(map(f, sf._ON_debug__all_sides_between_curr_arc_ceil_arcs_(curr_arc_, unorder_ceil_arcs_))) -f(curr_arc_)



    def _ON_debug__all_vtc_above_(sf, curr_arc_, /):
        L = sf.L
        imin_ = sf.imin_

        (i_, j_) = sf.two_vtx5curr_arc_(curr_arc_)
        assert 0 <= i_ <= j_ < L
        if i_ == j_:
            #if not j_ == imin_:raise logic-err
            if not j_ == imin_:
                s = range(i_, j_+1)
            else:
                s = range(L)
        else:
            if not imin_  <= i_ < j_:raise logic-err
            s = range(i_, j_+1)
        return s
    def _ON_debug__all_vtc_between_curr_arc_ceil_arcs_(sf, curr_arc_, unorder_ceil_arcs_, /):
        f = sf._ON_debug__all_vtc_above_
        s = {*()}
        for ceil_arc_ in unorder_ceil_arcs_:
            s |= {*f(ceil_arc_)}
        g = sf.two_vtx5curr_arc_
        for ceil_arc_ in unorder_ceil_arcs_:
            s -= {*g(ceil_arc_)}
        return [i_ for i_ in f(curr_arc_) if i_ not in s]
    def weights5ordered_vtc_(sf, ordered_vtc_, /):
        ls_ = sf.ls_
        xs__ = [ls_[k_] for k_ in ordered_vtc_]
        return xs__
    def _ONNN_debug__weights_between_curr_arc_ceil_arcs_(sf, curr_arc_, unorder_ceil_arcs_, /):
        return sf.weights5ordered_vtc_(sf._ON_debug__all_vtc_between_curr_arc_ceil_arcs_(curr_arc_, unorder_ceil_arcs_))
    def _ONNN_debug__weights_above_(sf, curr_arc_, /):
        return sf.weights5ordered_vtc_(sf._ON_debug__all_vtc_above_(curr_arc_))
    ##def _ONNN_debug__H0_between_curr_arc_ceil_arcs_(sf, curr_arc_, unorder_ceil_arcs_, /):必是MNO
    def _ONNN_debug__MNO_between_curr_arc_ceil_arcs_(sf, curr_arc_, unorder_ceil_arcs_, /):
        xs = sf._ONNN_debug__weights_between_curr_arc_ceil_arcs_(curr_arc_, unorder_ceil_arcs_)
        mno_tree = std_api4matrix_chain_product__dynamic_programming__O_NNN(xs)
        return mno_tree[0]
    def _ONNN_debug__MNO_above_(sf, curr_arc_, /):
        #-> MNO_above_curr_arc_
        L = sf.L
        ls_ = sf.ls_
        (i_, j_) = sf.two_vtx5curr_arc_(curr_arc_)
        assert i_ <= j_
        if j_==0:
            j_ = L-1
        assert i_ <= j_
        xs = [ls_[k_] for k_ in range(i_, j_+1)]
        assert 3 <= len(xs) == j_+1-i_ <= L
        assert xs == sf._ONNN_debug__weights_above_(curr_arc_)
        mno_tree = std_api4matrix_chain_product__dynamic_programming__O_NNN(xs)
        return mno_tree[0]

    def 词典序最先的最优三角化方案囗(sf, /):
        '-> (MNO4whole, imin, 所有对角线囗偏移囗有序, (所有显式横对角线囗第二版囗偏移囗有序, 所有隐式横对角线囗第二版囗偏移囗有序, 所有竖对角线囗第二版囗偏移囗有序))'
        L = sf.L
        if L == 2:
            def _mk_result():
                (_ls, _imin) = sf.save
                result = (MNO4whole, imin, 所有对角线囗偏移囗有序, (所有显式横对角线囗第二版囗偏移囗有序, 所有隐式横对角线囗第二版囗偏移囗有序, 所有竖对角线囗第二版囗偏移囗有序)) = (0, _imin, [], ([], [], []))
                return result
            return _mk_result()
        assert L >= 3

        idx_pph_arcs_ = [*sf.迭代囗三角化方案囗潜在的潜在的横对角线()]

        (root_, i_up2may_idx_pph_arc_) = sf.mk_idx_arc_tree_(idx_pph_arcs_)
        idx_r0psh_arcs_ = sf.潜在的潜在的横对角线树至第二版的除零的类横对角线树囗就地移除(idx_pph_arcs_, root_)
        del idx_pph_arcs_
        #ls_ = sf.ls_
        #goto:main_loop(root_, idx_r0psh_arcs_)


        def get_initial_above_arcs_of(curr_arc_, /):
            #here child-parent of tree not hidden-child-ceil of paper
            return curr_arc_.tree_children_
        def get_unorder_ceil_arcs_of(curr_arc_, /):
            #here child-parent of tree not hidden-child-ceil of paper
            return curr_arc_.unorder_ceil_arcs_

        def _init_find_leftmost_above_or_side_arc4curr_arc_(curr_arc_, /):
            'leftmost_above_or_side_arc4curr_arc_ :: pair'
            'leftmost_side_arc4curr_arc_ :: pair'
            (i_, j_) = sf.two_vtx5curr_arc_(curr_arc_)
            assert 0 <= i_ < j_ < L or i_==0==j_
            assert i_+1 < L >= 2
            leftmost_side_arc4curr_arc_ = (i_, i_+1)
            unorder_above_arcs_ = get_initial_above_arcs_of(curr_arc_)
            if unorder_above_arcs_:
                #leftmost_above_or_side_arc4curr_arc_ = (*min(unorder_above_arcs_),)
                leftmost_above_or_side_arc4curr_arc_ = min(map(tuple, unorder_above_arcs_))
                if not leftmost_above_or_side_arc4curr_arc_[0] == i_:
                    leftmost_above_or_side_arc4curr_arc_ = leftmost_side_arc4curr_arc_
            else:
                leftmost_above_or_side_arc4curr_arc_ = leftmost_side_arc4curr_arc_
            assert leftmost_above_or_side_arc4curr_arc_ < (i_,j_) or i_==0==j_
            return leftmost_above_or_side_arc4curr_arc_

        def _init_find_rightmost_above_or_side_arc4curr_arc_(curr_arc_, /):
            'rightmost_above_or_side_arc4curr_arc_ :: pair'
            'rightmost_side_arc4curr_arc_ :: pair'
            (i_, j_) = sf.two_vtx5curr_arc_(curr_arc_)
            rightmost_side_arc4curr_arc_ = ((j_-1)%L, j_)
            unorder_above_arcs_ = get_initial_above_arcs_of(curr_arc_)
            if unorder_above_arcs_:
                #rightmost_above_or_side_arc4curr_arc_ = (*max(unorder_above_arcs_),)
                rightmost_above_or_side_arc4curr_arc_ = max(map(tuple, unorder_above_arcs_))
                if not rightmost_above_or_side_arc4curr_arc_[-1] == j_:
                    rightmost_above_or_side_arc4curr_arc_ = rightmost_side_arc4curr_arc_
            else:
                rightmost_above_or_side_arc4curr_arc_ = rightmost_side_arc4curr_arc_
            assert rightmost_above_or_side_arc4curr_arc_ > (i_,j_)
            return rightmost_above_or_side_arc4curr_arc_
        def key4heap4ceil_arc_(ceil_arc_, /):
            return -ceil_arc_.supporting_weight
        def _check_tmp4curr_arc_(tmp4curr_arc_, /):
            assert type(tmp4curr_arc_) is TmpArc_
            (i_, j_) = (tmp4curr_arc_)
            'rightmost_above_or_side_arc4curr_arc_ :: pair'
            'leftmost_above_or_side_arc4curr_arc_ :: pair'
            assert i_ == tmp4curr_arc_.leftmost_above_or_side_arc_[0]
            assert j_ == tmp4curr_arc_.rightmost_above_or_side_arc_[-1]
            assert tmp4curr_arc_.rightmost_above_or_side_arc_ > (i_,j_)
            assert tmp4curr_arc_.leftmost_above_or_side_arc_ < (i_,j_) or i_==0==j_

            assert tmp4curr_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_ > 0
            assert tmp4curr_arc_.MNO_above_ceil_arcs_ >= 0
                # 0 is ok
                #   !![len(unorder_above_arcs_) >= 0]
        def _update2_tmp4curr_arc_(tmp4curr_arc_, hidden_ceil_arc_as_son_, /):
            _update1_tmp4curr_arc_(tmp4curr_arc_, hidden_ceil_arc_as_son_)
            tmp4curr_arc_.MNO_between_curr_arc_ceil_arcs_ += hidden_ceil_arc_as_son_.MNO_between_curr_arc_ceil_arcs_
        def _update1_tmp4curr_arc_(tmp4curr_arc_, removed_above_arc_, /):
            tmp4curr_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_ += removed_above_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_
            tmp4curr_arc_.MNO_above_ceil_arcs_ -= removed_above_arc_.MNO_between_curr_arc_ceil_arcs_
            tmp4curr_arc_.leftmost_above_or_side_arc_ = min(tmp4curr_arc_.leftmost_above_or_side_arc_, removed_above_arc_.leftmost_above_or_side_arc_)
            tmp4curr_arc_.rightmost_above_or_side_arc_ = max(tmp4curr_arc_.rightmost_above_or_side_arc_, removed_above_arc_.rightmost_above_or_side_arc_)
            _check_tmp4curr_arc_(tmp4curr_arc_)

        def _init_unorder_ceil_arcs4curr_arc_(curr_arc_, min_weight4curr_arc_, /):
            assert curr_arc_.tree_children_ is get_initial_above_arcs_of(curr_arc_)
            unorder_above_arcs_ = MergeableHeap(get_initial_above_arcs_of(curr_arc_), key=key4heap4ceil_arc_)
            tmp4curr_arc_ = TmpArc_(*sf.two_vtx5curr_arc_(curr_arc_))
            tmp4curr_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_ = sf.calc_diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_(curr_arc_, unorder_above_arcs_)
            tmp4curr_arc_.MNO_above_ceil_arcs_ = sum(above_arc_.MNO_above_curr_arc_ for above_arc_ in unorder_above_arcs_)
            tmp4curr_arc_.leftmost_above_or_side_arc_ = _init_find_leftmost_above_or_side_arc4curr_arc_(curr_arc_)
            tmp4curr_arc_.rightmost_above_or_side_arc_ = _init_find_rightmost_above_or_side_arc4curr_arc_(curr_arc_)
            _check_tmp4curr_arc_(tmp4curr_arc_)
            while unorder_above_arcs_:
                above_arc_ = unorder_above_arcs_.peak()
                if above_arc_.supporting_weight < min_weight4curr_arc_:
                    break
                #discard above_arc_
                removed_above_arc_ = unorder_above_arcs_.pop()
                assert removed_above_arc_ is above_arc_
                del above_arc_
                if 0:
                    #bug:leftmost/rightmost在main_loop里没有更新！已更正！
                    print(f'curr_arc_ = {sf.two_vtx5curr_arc_(curr_arc_)}')
                    print(f'removed_above_arc_ = {sf.two_vtx5curr_arc_(removed_above_arc_)}')
                    print(f'rightmost_above_or_side_arc4curr_arc_ = {tmp4curr_arc_.rightmost_above_or_side_arc_}')
                    print(f'removed_above_arc_.rightmost_above_or_side_arc_ = {removed_above_arc_.rightmost_above_or_side_arc_}')
                    print(f'removed_above_arc_.unorder_ceil_arcs_ = {sf.two_vtc5arcs_(removed_above_arc_.unorder_ceil_arcs_)}')


                #########
                _unorder_above_arcs4removed_above_arc_ = get_unorder_ceil_arcs_of(removed_above_arc_)
                assert removed_above_arc_.unorder_ceil_arcs_ is _unorder_above_arcs4removed_above_arc_
                removed_above_arc_.unorder_ceil_arcs_ = None
                    #eat() clear _unorder_above_arcs4removed_above_arc_
                unorder_above_arcs_.eat(_unorder_above_arcs4removed_above_arc_)
                assert not _unorder_above_arcs4removed_above_arc_
                del _unorder_above_arcs4removed_above_arc_


                #########
                _update1_tmp4curr_arc_(tmp4curr_arc_, removed_above_arc_)
            #while unorder_above_arcs_:

            unorder_ceil_arcs4curr_arc_ = unorder_above_arcs_
            #assert all(ceil_arc_.supporting_weight < min_weight4curr_arc_ for ceil_arc_ in unorder_ceil_arcs4curr_arc_)

            initial_unorder_ceil_arcs4curr_arc_ = final_unorder_above_arcs4curr_arc_ = unorder_ceil_arcs4curr_arc_
            (focus_vtx4H0_above_curr_arc_, delta4h0) = sf.find_the_focus_vtx4H0_above_curr_arc_(curr_arc_, tmp4curr_arc_.leftmost_above_or_side_arc_, tmp4curr_arc_.rightmost_above_or_side_arc_)
            base_product4curr_arc_ = sf.get_base_product_of_curr_arc_(curr_arc_)
            H0_between_curr_arc_final_unorder_above_arcs_ = min_weight4curr_arc_*(tmp4curr_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_+base_product4curr_arc_-delta4h0)
                #new:find_the_focus_vtx4H0_above_curr_arc_
                #update:_iter_all_unorder_v_ij_arcs4all_h_arcsII_/_iter_all_unorder_v_ij_arcs4h_arcII_
            tmp4curr_arc_.MNO_between_curr_arc_ceil_arcs_ = H0_between_curr_arc_final_unorder_above_arcs_
            MNO_above_curr_arc_ = tmp4curr_arc_.MNO_above_ceil_arcs_ + tmp4curr_arc_.MNO_between_curr_arc_ceil_arcs_
                #final: MNO_above_curr_arc_, H0_between_curr_arc_final_unorder_above_arcs_
                #but not final:(MNO_above_ceil_arcs4curr_arc_, MNO_between_curr_arc_ceil_arcs_)
            return (initial_unorder_ceil_arcs4curr_arc_, H0_between_curr_arc_final_unorder_above_arcs_, MNO_above_curr_arc_, tmp4curr_arc_)
        #end-def _init_unorder_ceil_arcs4curr_arc_():




        #testing___________goto
        def main_loop(root_, idx_r0psh_arcs_, /):
          for curr_arc_ in chain(idx_r0psh_arcs_, [root_]):
            assert type(curr_arc_) is IdxArc_ or curr_arc_ is root_

            min_weight4curr_arc_ = sf.get_min_weight4curr_arc_(curr_arc_)
            (initial_unorder_ceil_arcs4curr_arc_, H0_between_curr_arc_final_unorder_above_arcs_, MNO_above_curr_arc_, tmp4curr_arc_) = _init_unorder_ceil_arcs4curr_arc_(curr_arc_, min_weight4curr_arc_)
            final_unorder_above_arcs4curr_arc_ = initial_unorder_ceil_arcs4curr_arc_
            assert H0_between_curr_arc_final_unorder_above_arcs_ > 0
            #final_unorder_above_arcs4curr_arc_
            if sf._turnon_debug and __debug__:
                final_unorder_above_arcs4curr_arc_ = [*final_unorder_above_arcs4curr_arc_]
                    #protected from eat()
                _mno = sf._ONNN_debug__MNO_between_curr_arc_ceil_arcs_(curr_arc_, final_unorder_above_arcs4curr_arc_)
                assert H0_between_curr_arc_final_unorder_above_arcs_ == _mno, (sf.two_vtx5curr_arc_(curr_arc_), H0_between_curr_arc_final_unorder_above_arcs_, _mno, sf.two_vtc5arcs_(curr_arc_.tree_children_), sf.two_vtc5arcs_(final_unorder_above_arcs4curr_arc_), [above_arc_.supporting_weight for above_arc_ in final_unorder_above_arcs4curr_arc_])
            ######
            curr_arc_.MNO_above_curr_arc_ = MNO_above_curr_arc_
            del MNO_above_curr_arc_
            assert curr_arc_.MNO_above_curr_arc_ > 0
            if sf._turnon_debug and __debug__:
                sf._ONNN_debug__MNO_above_(curr_arc_.MNO_above_curr_arc_, curr_arc_)
                _mno = sf._ONNN_debug__MNO_above_(curr_arc_)
                assert curr_arc_.MNO_above_curr_arc_ == _mno, (sf.two_vtx5curr_arc_(curr_arc_), curr_arc_.MNO_above_curr_arc_, _mno, sf.two_vtc5arcs_(curr_arc_.tree_children_), sf.two_vtc5arcs_(final_unorder_above_arcs4curr_arc_), [above_arc_.supporting_weight for above_arc_ in final_unorder_above_arcs4curr_arc_])
            ######
            if curr_arc_ is root_:
                curr_arc_.leftmost_above_or_side_arc_ = tmp4curr_arc_.leftmost_above_or_side_arc_
                curr_arc_.rightmost_above_or_side_arc_ = tmp4curr_arc_.rightmost_above_or_side_arc_
                curr_arc_.unorder_ceil_arcs_ = initial_unorder_ceil_arcs4curr_arc_
                curr_arc_.leftmost_above_or_side_arc_
                curr_arc_.rightmost_above_or_side_arc_
                curr_arc_.unorder_ceil_arcs_
                curr_arc_.MNO_above_curr_arc_
                if 0:
                    print(f'curr_arc_=root_')
                    print(f'curr_arc_.MNO_above_curr_arc_={curr_arc_.MNO_above_curr_arc_}')
                    print(f'curr_arc_.H0_between_curr_arc_final_unorder_above_arcs_={H0_between_curr_arc_final_unorder_above_arcs_}')

                break

            if 1:
                heap = initial_unorder_ceil_arcs4curr_arc_
                #会改变:initial_unorder_ceil_arcs4curr_arc_/final_unorder_above_arcs4curr_arc_
                del initial_unorder_ceil_arcs4curr_arc_, final_unorder_above_arcs4curr_arc_ # curr_arc_.final_unorder_above_arcs_ 没有了

            #定位:ceil_arcs_<curr_arc_> #除了paper-hidden-child-ceil之外 的 最低 above_arc_   #(not『tree-child』)
            #supporting_weight4curr_arc_<ceil_arcs_>
            #
            #   因为：删除 多条 横线 后，结果可能更优
            #   当 [ceil_arc_.supporting_weight >= curr_arc_.supporting_weight<ceil_arcs_>]，说明:
            #   * 当 next_curr_arc_.min_weight4curr_arc_ <= curr_arc_.supporting_weight<ceil_arcs_> 时，curr_arc_,ceil_arc_ 都得移除
            #   * 当 next_curr_arc_.min_weight4curr_arc_ > curr_arc_.supporting_weight<ceil_arcs_> 时，！！！却不能确定在局部多边形中『curr_arc_,ceil_arc_ 都能保留』！！！
            #     因为 两者 一起移除后结果可能更好==>> 不断 修正ceil_arcs_,curr_arc_.supporting_weight<ceil_arcs_>
            #       ceil_arcs_移除新增
            #       curr_arc_.supporting_weight<ceil_arcs_>缓慢增大，直到 稳定:
            #         即 ceil_arc_ 的 移除 无法令其继续增大
            #         即 全『<』，无有[ceil_arc_.supporting_weight >= curr_arc_.supporting_weight<ceil_arcs_>]
            #supporting_weight4curr_arc_<ceil_arcs_>
            #
            tmp4curr_arc_.MNO_between_curr_arc_ceil_arcs_ # H0_between_curr_arc_final_unorder_above_arcs_
            tmp4curr_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_

            if sf._turnon_debug and __debug__:
                _D = sf._ON_debug__diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_(curr_arc_, initial_unorder_ceil_arcs4curr_arc_)
                D = tmp4curr_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_
                assert D==_D, (D, _D, sf.two_vtx5curr_arc_(curr_arc_))

            curr_arc_.unorder_ceil_hidden_children_ = []
            if 1:
                assert tmp4curr_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_ > 0
                    #这是因为 上方 的 最小权值 都比 当前横对角线端点权值大
                assert tmp4curr_arc_.MNO_between_curr_arc_ceil_arcs_ > 0
                if 0:
                    #重启__floor_div__ 替代 Fraction
                    supporting_weight4curr_arc_ = Fraction(tmp4curr_arc_.MNO_between_curr_arc_ceil_arcs_,tmp4curr_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_)
                    assert 0 < supporting_weight4curr_arc_ < min_weight4curr_arc_
                else:
                    supporting_weight4curr_arc_ = tmp4curr_arc_.MNO_between_curr_arc_ceil_arcs_//tmp4curr_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_
                    assert 0 <= supporting_weight4curr_arc_ < min_weight4curr_arc_

            (i_, j_) = sf.two_vtx5curr_arc_(curr_arc_)
            while heap:
                ceil_arc_ = heap.peak()
                assert ceil_arc_.supporting_weight < min_weight4curr_arc_
                if ceil_arc_.supporting_weight < supporting_weight4curr_arc_:
                    break
                assert 0 < supporting_weight4curr_arc_ <= ceil_arc_.supporting_weight < min_weight4curr_arc_
                #testing___________goto
                hidden_ceil_arc_as_son_ = heap.pop()
                assert hidden_ceil_arc_as_son_ is ceil_arc_
                del ceil_arc_
                #ceil_arc_ is hidden-child of curr_arc_, hence not a ceil_arc_ anymore
                heap.eat(hidden_ceil_arc_as_son_.unorder_ceil_arcs_)
                del hidden_ceil_arc_as_son_.unorder_ceil_arcs_
                curr_arc_.unorder_ceil_hidden_children_.append(hidden_ceil_arc_as_son_)
                ######
                _update2_tmp4curr_arc_(tmp4curr_arc_, hidden_ceil_arc_as_son_)
                old_supporting_weight4curr_arc_ = supporting_weight4curr_arc_
                if 0:
                    #重启__floor_div__ 替代 Fraction
                    new_supporting_weight4curr_arc_ = Fraction(tmp4curr_arc_.MNO_between_curr_arc_ceil_arcs_,tmp4curr_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_)
                    assert 0 < old_supporting_weight4curr_arc_ <= new_supporting_weight4curr_arc_ <= hidden_ceil_arc_as_son_.supporting_weight < min_weight4curr_arc_
                else:
                    new_supporting_weight4curr_arc_ = tmp4curr_arc_.MNO_between_curr_arc_ceil_arcs_//tmp4curr_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_
                    assert 0 <= old_supporting_weight4curr_arc_ <= new_supporting_weight4curr_arc_ <= hidden_ceil_arc_as_son_.supporting_weight < min_weight4curr_arc_
                supporting_weight4curr_arc_ = new_supporting_weight4curr_arc_

                if sf._turnon_debug and __debug__:
                    __unorder_ceil_arcs4curr_arc_ = [ceil_arc_ for (_,_,ceil_arc_) in heap]
                    _D = sf._ON_debug__diff__side_product_between_curr_arc_ceil_arcs__base_product4curr_arc_(curr_arc_, __unorder_ceil_arcs4curr_arc_)
                    D = tmp4curr_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_
                    assert D==_D, (D, _D, sf.two_vtx5curr_arc_(curr_arc_))
                    _mno = sf._ONNN_debug__MNO_between_curr_arc_ceil_arcs_(curr_arc_, __unorder_ceil_arcs4curr_arc_)
                    assert tmp4curr_arc_.MNO_between_curr_arc_ceil_arcs_ == _mno
            #end-while heap:
            unorder_ceil_arcs4curr_arc_ = heap

            ########next round
            #assert all(ceil_arc_.supporting_weight < supporting_weight4curr_arc_ for ceil_arc_ in unorder_ceil_arcs4curr_arc_)

            curr_arc_.unorder_ceil_arcs_ = unorder_ceil_arcs4curr_arc_
            curr_arc_.supporting_weight = supporting_weight4curr_arc_
            curr_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_ = tmp4curr_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_
            curr_arc_.MNO_between_curr_arc_ceil_arcs_ = tmp4curr_arc_.MNO_between_curr_arc_ceil_arcs_
            curr_arc_.leftmost_above_or_side_arc_ = tmp4curr_arc_.leftmost_above_or_side_arc_
            curr_arc_.rightmost_above_or_side_arc_ = tmp4curr_arc_.rightmost_above_or_side_arc_
            ######
            curr_arc_.leftmost_above_or_side_arc_
            curr_arc_.rightmost_above_or_side_arc_
            curr_arc_.unorder_ceil_hidden_children_
            curr_arc_.unorder_ceil_arcs_
            curr_arc_.supporting_weight
            curr_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_
            curr_arc_.MNO_between_curr_arc_ceil_arcs_
            curr_arc_.MNO_above_curr_arc_
            if 0:
                #testing___________goto
                print(f'curr_arc_={tuple(curr_arc_)}')
                print(f'min_weight4curr_arc_={min_weight4curr_arc_}')
                print(f'curr_arc_.unorder_ceil_arcs_={sf.two_vtc5arcs_(curr_arc_.unorder_ceil_arcs_)}')
                print(f'curr_arc_.unorder_ceil_hidden_children_={sf.two_vtc5arcs_(curr_arc_.unorder_ceil_hidden_children_)}')
                print(f'curr_arc_.MNO_above_curr_arc_={curr_arc_.MNO_above_curr_arc_}')
                print(f'curr_arc_.MNO_between_curr_arc_ceil_arcs_={curr_arc_.MNO_between_curr_arc_ceil_arcs_}')
                print(f'curr_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_={curr_arc_.diff__side_product_between_curr_arc_ceil_arcs__base_product_}')
                print(f'curr_arc_.supporting_weight={curr_arc_.supporting_weight}')
                print(f'curr_arc_.leftmost_above_or_side_arc_={curr_arc_.leftmost_above_or_side_arc_}')
                print(f'curr_arc_.rightmost_above_or_side_arc_={curr_arc_.rightmost_above_or_side_arc_}')
          #end-for
          return
        #end-def main_loop(root_, idx_r0psh_arcs_, /):

        r'''[[[#to avoid:_remove_arcs_as_nodes_of_tree_emplace_if_not:RecursionError: maximum recursion depth exceeded
        def _iter_all_unorder_ceil_arcs_(root_or_ceil_arc_, /):
            yield from chain.from_iterable(map(_iter_all_unorder_ceil_arcs__not_top_, root_or_ceil_arc_.unorder_ceil_arcs_))
        def _iter_all_unorder_ceil_arcs__not_top_(ceil_arc_, /):
            yield ceil_arc_
            yield from _iter_all_unorder_ceil_arcs_(ceil_arc_)

        def _iter_all_unorder_ceil_hidden_children_(root_or_ceil_arc_, /):
            yield from chain.from_iterable(map(_iter_all_unorder_ceil_hidden_children__not_top_, root_or_ceil_arc_.unorder_ceil_hidden_children_))
        def _iter_all_unorder_ceil_hidden_children__not_top_(ceil_arc_, /):
            yield ceil_arc_
            yield from _iter_all_unorder_ceil_hidden_children_(ceil_arc_)
        #]]]'''
        def _iter_all_unorder_ceil_arcs_(sub_root_, /):
            sub_roots_ = [sub_root_]
            while sub_roots_:
                sub_root_ = sub_roots_.pop()
                yield from sub_root_.unorder_ceil_arcs_
                sub_roots_.extend(sub_root_.unorder_ceil_arcs_)

        def _iter_all_unorder_ceil_hidden_children_(sub_root_, /):
            sub_roots_ = [sub_root_]
            while sub_roots_:
                sub_root_ = sub_roots_.pop()
                yield from sub_root_.unorder_ceil_hidden_children_
                sub_roots_.extend(sub_root_.unorder_ceil_hidden_children_)

        def _iter_all_unorder_v_ij_arcs4all_h_arcsII_(root_, all_unorder_h_arcsII_, /):
            for h_arcII_ in all_unorder_h_arcsII_:
                yield from _iter_all_unorder_v_ij_arcs4h_arcII_(h_arcII_)
            yield from _iter_all_unorder_v_ij_arcs4h_arcII_(root_)
        def _iter_all_unorder_v_ij_arcs4h_arcII_(h_arcII_, /):
            (i_, j_) = sf.two_vtx5curr_arc_(h_arcII_)
            assert i_ <= j_
            assert 0 <= i_ < j_ < L or i_==j_==0==sf.imin_
            k_ = min(i_, j_, key=sf.fw)
            if k_ == i_:
                def _mk(z_, /):
                    return (k_, z_)
            else:
                def _mk(z_, /):
                    return (z_, k_)

            # i_~first_:最多3点:i_.+{0,1,2}
            # 可能出 幺蛾子的是:
            #   (i_, i_+2) 唯一可能出状况的情形
            #   (i_, i_+1) 外边 不可能
            #   (i_+1, i_+2) 外边 不可能

            sorted_above_arcs_ = [tuple(above_arc_) for above_arc_ in h_arcII_.final_sorted_above_arcs_]
            def moveL(i_, idx, /):
                if idx == len(sorted_above_arcs_):
                    return i_+1, idx
                a_,b_ = sorted_above_arcs_[idx]
                if a_ == i_:
                    return b_, idx+1
                return i_+1, idx
            def moveR(j_, idx, /):
                if idx == -len(sorted_above_arcs_)-1:
                    return (j_-1)%L, idx
                x_,y_ = sorted_above_arcs_[idx]
                if y_ == j_:
                    return x_, idx-1
                return (j_-1)%L, idx
            def apply_(n, f, k_, idx, /):
                for _ in range(n):
                    (k_, idx) = f(k_, idx)
                return (k_, idx)
            b_, idxA = apply_(1+(i_ == k_), moveL, i_, 0)
            x_, idxY = apply_(1+(j_ == k_), moveR, j_, -1)
            if 0:
                print(f'sorted_above_arcs_ = {sorted_above_arcs_}')
                print(f'i_ = {i_}')
                print(f'j_ = {j_}')
                print(f'b_ = {b_}')
                print(f'x_ = {x_}')
            while b_ <= x_:
                yield _mk(b_)
                (b_, idxA) = moveL(b_, idxA)
        #end-def _iter_all_unorder_v_ij_arcs4h_arcII_(h_arcII_, /):






        def is_h_arcII_(arc, /):
            return arc.is_h_arcII_
        def _setting__final_sorted_above_arcs_(root_, all_unorder_h_arcsII_, /):
            #setting:final_sorted_above_arcs_
            for may_idx_pph_arc_ in i_up2may_idx_pph_arc_:
                if may_idx_pph_arc_ is not None:
                    idx_pph_arc_ = may_idx_pph_arc_
                    idx_pph_arc_.is_h_arcII_ = False
            for h_arc_ in all_unorder_h_arcsII_:
                h_arc_.is_h_arcII_ = True
            sf._remove_arcs_as_nodes_of_tree_emplace_if_not(is_h_arcII_, root_)
                #now tree_children_ are final_unorder_above_arcs_
            unorder_ij_above_arcss_ = []
            ps_iups_ = []
            def _add(curr_arc_, ps_i_up_, /):
                assert _get(ps_i_up_) is curr_arc_
                unorder_ij_above_arcss_.append([(*sf.two_vtx5curr_arc_(above_arc_), above_arc_) for above_arc_ in curr_arc_.tree_children_])
                ps_iups_.append(ps_i_up_)
            def _get(ps_i_up_, /):
                if ps_i_up_ == sf.imin_:
                    return root_
                return i_up2may_idx_pph_arc_[ps_i_up_]

            for curr_arc_ in all_unorder_h_arcsII_:
                _add(curr_arc_, curr_arc_.i_up_)
            else:
                _add(root_, sf.imin_)

            #######
            unorder_ij_above_arcss_
            fst, snd
            table = [[] for _ in range(L)]
            unorder_ij_above_arcss_ = bucket_sort_per_row(L, unorder_ij_above_arcss_, table, key=snd)
            sorted_ij_above_arcss_ = bucket_sort_per_row(L, unorder_ij_above_arcss_, table, key=fst)
            sorted_above_arcss_ = [[above_arc_ for (i_, j_, above_arc_) in sorted_ij_above_arcs_] for sorted_ij_above_arcs_ in sorted_ij_above_arcss_]
            #print(f'unorder_ij_above_arcss_ = {unorder_ij_above_arcss_}')
            #print(f'sorted_ij_above_arcss_ = {sorted_ij_above_arcss_}')

            for ps_i_up_, sorted_above_arcs_ in zip(ps_iups_, sorted_above_arcss_):
                curr_arc_ = _get(ps_i_up_)
                curr_arc_.final_sorted_above_arcs_ = sorted_above_arcs_
        #end-def _setting__final_sorted_above_arcs_(root_, all_unorder_h_arcsII_, /):


        def _mk_xxx_arcss_():
            all_unorder_ceil_arcs_ = [ceil_arc_ for ceil_arc_ in _iter_all_unorder_ceil_arcs_(root_)]
            #rint(f'all_unorder_ceil_arcs_={all_unorder_ceil_arcs_}')
            #bug:all_unorder_ceil_hidden_children_ = [*_iter_all_unorder_ceil_hidden_children_(root_)]
            all_unorder_ceil_hidden_children_ = [*chain.from_iterable(map(_iter_all_unorder_ceil_hidden_children_, all_unorder_ceil_arcs_))]
            #rint(f'all_unorder_ceil_hidden_children_={all_unorder_ceil_hidden_children_}')
            all_unorder_h_arcsII_ = all_unorder_ceil_arcs_+all_unorder_ceil_hidden_children_
            所有显式横对角线囗第二版囗偏移囗无序 = [(i_, j_) for (i_, j_) in all_unorder_ceil_arcs_]
            所有隐式横对角线囗第二版囗偏移囗无序 = [(i_, j_) for (i_, j_) in all_unorder_ceil_hidden_children_]


            #using:final_sorted_above_arcs_
            _setting__final_sorted_above_arcs_(root_, all_unorder_h_arcsII_)
            所有竖对角线囗第二版囗偏移囗无序 = [*_iter_all_unorder_v_ij_arcs4all_h_arcsII_(root_, all_unorder_h_arcsII_)]
            assert len(所有显式横对角线囗第二版囗偏移囗无序) + len(所有隐式横对角线囗第二版囗偏移囗无序) + len(所有竖对角线囗第二版囗偏移囗无序) == L-3, (L, (所有显式横对角线囗第二版囗偏移囗无序, 所有隐式横对角线囗第二版囗偏移囗无序, 所有竖对角线囗第二版囗偏移囗无序))
            def _iter_with(k, xss, /):
                for xs in xss:
                    yield (*xs, k)
            def _it_3s():
                yield from _iter_with(0, 所有显式横对角线囗第二版囗偏移囗无序)
                yield from _iter_with(1, 所有隐式横对角线囗第二版囗偏移囗无序)
                yield from _iter_with(2, 所有竖对角线囗第二版囗偏移囗无序)
            it = _it_3s()
            table = [[] for _ in range(L)]
            ij_kind_ls_ = radix_sort_with_table([L, L], it, table)
            assert len(ij_kind_ls_) == L-3
            inner_idx_arcs_ = []
            [ceil_idx_arcs_
            ,hide_idx_arcs_
            ,ps_vertical_idx_arcs_
            ] = kind2ls = ([], [], [])
            for i_, j_, kind in ij_kind_ls_:
                ij_ = (i_, j_)
                inner_idx_arcs_.append(ij_)
                kind2ls[kind].append(ij_)
            assert len(inner_idx_arcs_) == L-3
            return (inner_idx_arcs_, (ceil_idx_arcs_, hide_idx_arcs_, ps_vertical_idx_arcs_))
        #end-def _mk_xxx_arcss_():
        main_loop(root_, idx_r0psh_arcs_)
        (inner_idx_arcs_, (ceil_idx_arcs_, hide_idx_arcs_, ps_vertical_idx_arcs_)) = _mk_xxx_arcss_()
        所有对角线囗偏移囗有序 = inner_idx_arcs_
        所有显式横对角线囗第二版囗偏移囗有序 = ceil_idx_arcs_
        所有隐式横对角线囗第二版囗偏移囗有序 = hide_idx_arcs_
        所有竖对角线囗第二版囗偏移囗有序 = ps_vertical_idx_arcs_
        MNO4whole = root_.MNO_above_curr_arc_
        def _mk_result():
            (_ls, imin) = sf.save
            result = (MNO4whole, imin, 所有对角线囗偏移囗有序, (所有显式横对角线囗第二版囗偏移囗有序, 所有隐式横对角线囗第二版囗偏移囗有序, 所有竖对角线囗第二版囗偏移囗有序))
            return result
        result = _mk_result()
        if sf._turnon_debug and __debug__ and 0:
            #tail4std_api4matrix_chain_product__polygon_partitioning__O_NlogN
            #rint(f'result={result}')
            (_ls, _imin) = sf.save
            tail4std_api4matrix_chain_product__polygon_partitioning__O_NlogN(_ls, result)
        return result


    #end-def 词典序最先的最优三角化方案囗(sf, /):
#end-class 囗矩阵乘法链维数序列囗相关函数:
class Imin8Arc_:
    __slots__ = '''
        i_
        tree_children_
        leftmost_above_or_side_arc_
        rightmost_above_or_side_arc_
        MNO_above_curr_arc_
        unorder_ceil_arcs_
        final_sorted_above_arcs_
        '''.split()
    unorder_ceil_hidden_children_ = ()
    def __init__(sf, i_, /):
        sf.i_ = i_
class IdxArc_:
    __slots__ = '''
        i_lhs_
        i_rhs_
        i_up_
        tree_children_
        leftmost_above_or_side_arc_
        rightmost_above_or_side_arc_
        unorder_ceil_hidden_children_
        unorder_ceil_arcs_
        supporting_weight
        diff__side_product_between_curr_arc_ceil_arcs__base_product_
        MNO_between_curr_arc_ceil_arcs_
        MNO_above_curr_arc_
        is_h_arcII_
        final_sorted_above_arcs_
        '''.split()
    def __init__(sf, i_lhs_, i_rhs_, /):
        sf.i_lhs_ = i_lhs_
        sf.i_rhs_ = i_rhs_
    def __iter__(sf, /):
        yield sf.i_lhs_
        yield sf.i_rhs_
    def __contains__(sf, k_, /):
        return (k_ == sf.i_lhs_) or (k_ == sf.i_rhs_)

assert 0 in IdxArc_(0,1)
assert 1 in IdxArc_(0,1)
class TmpArc_:
    __slots__ = '''
        i_lhs_
        i_rhs_
        leftmost_above_or_side_arc_
        rightmost_above_or_side_arc_
        diff__side_product_between_curr_arc_ceil_arcs__base_product_
        MNO_above_ceil_arcs_

        MNO_between_curr_arc_ceil_arcs_
        '''.split()
    def __init__(sf, i_lhs_, i_rhs_, /):
        sf.i_lhs_ = i_lhs_
        sf.i_rhs_ = i_rhs_
    def __iter__(sf, /):
        yield sf.i_lhs_
        yield sf.i_rhs_




def matrix_chain_product__polygon_partitioning__O_NlogN(矩阵乘法链维数序列, /, *, may_imin, _turnon_debug):
    sf = 囗矩阵乘法链维数序列囗相关函数(矩阵乘法链维数序列, may_imin=may_imin, _turnon_debug=_turnon_debug)
    return sf.词典序最先的最优三角化方案囗()
矩阵乘法链囗多边形囗词典序最先的最优三角化方案囗等同排序算法耗时 = matrix_chain_product__polygon_partitioning__O_NlogN

def std_api4matrix_chain_product__polygon_partitioning__O_NlogN(矩阵乘法链维数序列, /):
    '-> mno_tree# mno_tree = (0,i,(ls[i],ls[i+1])) | (mno, begin, mno_tree, mid, mno_tree, end, (ls[begin],ls[mid],ls[end-1]))'
    result = matrix_chain_product__polygon_partitioning__O_NlogN(矩阵乘法链维数序列, may_imin=None)
    return tail4std_api4matrix_chain_product__polygon_partitioning__O_NlogN(矩阵乘法链维数序列, result)
def tail4std_api4matrix_chain_product__polygon_partitioning__O_NlogN(矩阵乘法链维数序列, result, /):
    (MNO4whole, imin, 所有对角线囗偏移囗有序, (所有显式横对角线囗第二版囗偏移囗有序, 所有隐式横对角线囗第二版囗偏移囗有序, 所有竖对角线囗第二版囗偏移囗有序)) = result

    ls = 矩阵乘法链维数序列
    L = len(ls)
    inner_arcs_ = 所有对角线囗偏移囗有序
    unsorted_inner_arcs = unoffset_arcs_(L, imin, inner_arcs_)
    end4ground_outer_arc = 0
    mno_tree = mk_mno_tree_from_unsorted_inner_arcs(ls, end4ground_outer_arc, unsorted_inner_arcs)

    assert MNO4whole == mno_tree[0], (L, 矩阵乘法链维数序列, 所有对角线囗偏移囗有序, imin, MNO4whole, mno_tree)
    return mno_tree


