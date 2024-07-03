#__all__:goto
r'''[[[
e ../../python3_src/seed/data_funcs/finger_tree/FingerTree.py


seed.data_funcs.finger_tree.FingerTree
py -m nn_ns.app.debug_cmd   seed.data_funcs.finger_tree.FingerTree -x
py -m nn_ns.app.doctest_cmd seed.data_funcs.finger_tree.FingerTree:__doc__


>>> FingerTree()
FingerTree()
>>> bool(FingerTree())
False
>>> len(FingerTree())
0
>>> sf = FingerTree(range(9))
>>> bool(sf)
True
>>> len(sf)
9
>>> [*sf]
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> [*reversed(sf)]
[8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> sf
FingerTree([0, 1, 2, 3, 4, 5, 6, 7, 8])
>>> sf[::-1]
FingerTree([8, 7, 6, 5, 4, 3, 2, 1, 0])
>>> sf.ireverse()
FingerTree([8, 7, 6, 5, 4, 3, 2, 1, 0])
>>> sf.ireverse()._t is sf._t is sf[::-1]._t
True
>>> ot = FingerTree(range(9), reverse=True)
>>> ot
FingerTree([8, 7, 6, 5, 4, 3, 2, 1, 0])
>>> sf == ot
False
>>> sf[::-1] == ot
True
>>> FingerTree(range(9)[::-1]) == ot
True
>>> sf == ot[::-1]
True
>>> sf == FingerTree(range(9)[::-1], reverse=True)
True
>>> sf[4]
4
>>> sf[-4]
5
>>> sf[4:-4]
FingerTree([4])
>>> sf[-4:4]
FingerTree()
>>> sf.ipop_left()
(FingerTree([1, 2, 3, 4, 5, 6, 7, 8]), 0)
>>> sf.ipop_right()
(FingerTree([0, 1, 2, 3, 4, 5, 6, 7]), 8)
>>> sf.iappend_left(999)
(FingerTree([999, 0, 1, 2, 3, 4, 5, 6, 7, 8]), None)
>>> sf.iappend_right(999)
(FingerTree([0, 1, 2, 3, 4, 5, 6, 7, 8, 999]), None)
>>> sf << 999
FingerTree([0, 1, 2, 3, 4, 5, 6, 7, 8, 999])
>>> sf +ot
FingerTree([0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 7, 6, 5, 4, 3, 2, 1, 0])
>>> sf.iextend_left(range(66, 69))
(FingerTree([66, 67, 68, 0, 1, 2, 3, 4, 5, 6, 7, 8]), None)
>>> sf.iextend_right(range(66, 69))
(FingerTree([0, 1, 2, 3, 4, 5, 6, 7, 8, 66, 67, 68]), None)
>>> sf.iextend_left(range(66, 69), reverse=True)
(FingerTree([68, 67, 66, 0, 1, 2, 3, 4, 5, 6, 7, 8]), None)
>>> sf.iextend_right(range(66, 69), reverse=True)
(FingerTree([0, 1, 2, 3, 4, 5, 6, 7, 8, 68, 67, 66]), None)
>>> hash(a:=FingerTree(range(9))) == hash(b:=FingerTree(range(9)[::-1])[::-1])
True
>>> a._h_excl_cls_rv == b._h_excl_cls_rv
False
>>> (a._h_excl_cls_rv + b._h_excl_cls_rv) %_M
0
>>> a == b
True
>>> a._rv
False
>>> b._rv
True
>>> sf == sf
True
>>> sf != sf
False
>>> sf < sf
False
>>> sf <= sf
True
>>> sf > sf
False
>>> sf >= sf
True

>>> sf == ot
False
>>> sf != ot
True
>>> sf < ot
True
>>> sf <= ot
True
>>> sf > ot
False
>>> sf >= ot
False
>>> 
>>> 
>>> 
>>> 
>>> 

#]]]'''
__all__ = r'''
FingerTree
'''.split()#'''
__all__
from seed.data_funcs.finger_tree.finger_tree_ops__instances import (
匴双侧展翅树囗相关操作囗囗无长度囗囗二三树
,匴双侧展翅树囗相关操作囗囗仅长度囗囗二三树
#,匴双侧展翅树囗相关操作囗囗丮长度丶散列值厈囗囗二三树
    #散列值 只需 按需计算，每棵树都计算，有点费劲
)
from seed.tiny import check_type_is
from seed.helper.repr_input import repr_helper
from seed.iters.cmp4iterable import cmp4iterable__lt, lt4iterable__lt
import functools
import operator as opss
import sys
_M = sys.hash_info.modulus


_kkkkk = object()
@functools.total_ordering
class FingerTree:
    __slots__ = '_t _rv _h_excl_cls_rv _sz'.split()
    ######################
    #_ops_ = 匴双侧展翅树囗相关操作囗囗无长度囗囗二三树
    _ops_ = 匴双侧展翅树囗相关操作囗囗仅长度囗囗二三树
        #长度 用于 分裂, 定位/__getitem__
    ######################
    r'''[[[
    _t - tree
    _rv - reverse
    _h_excl_cls_rv - hash(tree) exclude "reverse" and type(sf)
    _sz - size/length
    #]]]'''#'''
    ######################
    #@classmethod
    @property
    def ops(sf, /):
        return type(sf)._ops_
    def __init__(sf, xs='', /, *, reverse=False, _=None):
        reverse = bool(reverse)
        sf._h_excl_cls_rv = ...
        if not _ is None:
            if not _ is _kkkkk: raise TypeError
            (tree, _rv, _h_excl_cls_rv, _sz) = xs
            sf._t = tree
            sf._rv = _rv ^ reverse
            sf._h_excl_cls_rv = _h_excl_cls_rv
            sf._sz = _sz
        elif isinstance(xs, type(sf)):
            ot = xs
            sf._t = ot._t
            sf._sz = ot._sz
            sf._rv = ot._rv ^ reverse
            #if type(sf) is type(ot):
            if 1:
                #__hash__():goto
                sf._h_excl_cls_rv = ot._h_excl_cls_rv
        else:
            sf._t = sf.ops.构造树囗(xs, 左起丷右起=reverse)
            sf._rv = False
            sf._sz = _brute_force_calc_len_(sf.ops, sf._t)
    def __repr__(sf, /):
        if not sf:
            return repr_helper(sf)
        return repr_helper(sf, [*sf])
    def __iter__(sf, /):
        return sf.ops.迭代元素囗(sf._t, 左起丷右起=sf._rv)
    def __reversed__(sf, /):
        return sf.ops.迭代元素囗(sf._t, 左起丷右起=not sf._rv)
    def ireverse(sf, /):
        return type(sf)(sf, reverse=True)
    def __len__(sf, /):
        return sf._sz
    def __bool__(sf, /):
        return not sf._sz == 0
        return sf.ops.是空树囗(sf._t)
    def __hash__(sf, /):
        if sf._h_excl_cls_rv is ...:
            h = 0 # high deg --> low deg
            d = 0 # low deg --> high deg
            B = 1
            R = 37
            #bug:for n in map(hash, sf):
            #   since now change (h+d)-->(h-d)
            f = reversed if sf._rv else iter
            for n in map(hash, f(sf)):
                h = (h*R +n) %_M
                d = (d + B*n) %_M
                B = (B*R) %_M
            hd = (h - d) %_M
                # !! no matter _rv

            sf._h_excl_cls_rv = hd
        hd = sf._h_excl_cls_rv
        if sf._rv:
            hd = _M -hd
        assert 0 <= hd < _M

        return hash((id(type(sf)), len(sf), hd))
    def __eq__(sf, ot, /):
        #if not isinstance(ot, type(sf))
        if not type(sf) is type(ot):
            # !! hash()
            return False
        if not len(sf) == len(ot):
            return False
        if not (sf._h_excl_cls_rv is ... or ot._h_excl_cls_rv is ...):
            #xxx:if not sf._h_excl_cls_rv == ot._h_excl_cls_rv:
                # !! sf._rv
            if not hash(sf) == hash(ot):
                return False

        # !! sf._rv: 不用ops.等价冃列表囗
        itL = iter(sf)
        itR = iter(ot)
        return all(map(opss.__eq__, itL, itR))
    def __lt__(sf, ot, /):
        if not isinstance(ot, type(sf)):
            return NotImplemented
        itL = iter(sf)
        itR = iter(ot)
        return lt4iterable__lt(itL, itR)
    def ipop_tmay_(sf, /, *, left_vs_right):
        '-> (new-sf, tmay x)'
        left_vs_right = bool(left_vs_right)
        left_vs_right ^= sf._rv
        tree, tm = sf.ops.巜弹出魊元素囗(sf._t, 左端丷右端=left_vs_right)
        st = (tree, sf._rv, ..., len(sf)-1)
        ot = type(sf)(st, _=_kkkkk)
        return ot, tm
    def iappend_(sf, x, /, *, left_vs_right):
        '-> (new-sf, None)'
        left_vs_right = bool(left_vs_right)
        left_vs_right ^= sf._rv
        tree, _ = sf.ops.巜压入元素囗(sf._t, x, 左端丷右端=left_vs_right)
        st = (tree, sf._rv, ..., len(sf)+1)
        ot = type(sf)(st, _=_kkkkk)
        return ot, None
    def iextend_left(sf, xs, /, *, reverse=False):
        '-> (new-sf, None)'
        return sf.iextend_(xs, left_vs_right=False, reverse=reverse)
    def iextend_right(sf, xs, /, *, reverse=False):
        '-> (new-sf, None)'
        return sf.iextend_(xs, left_vs_right=True, reverse=reverse)
    def iextend_(sf, xs, /, *, left_vs_right, reverse):
        '-> (new-sf, None)'
        reverse = bool(reverse)
        left_vs_right = bool(left_vs_right)
        xs = _brute_force_iter_(not (reverse^left_vs_right), xs)
        ######################
        ######################
        ######################
        left_vs_right ^= sf._rv
        tree = sf._t
        f = sf.ops.巜压入元素囗
        sz = 0
        for sz, x in enumerate(xs, 1):
            tree, _ = f(tree, x, 左端丷右端=left_vs_right)
        if not sz:
            return sf
        st = (tree, sf._rv, ..., len(sf)+sz)
        ot = type(sf)(st, _=_kkkkk)
        return ot, None
    def ipop_left(sf, /):
        '-> (new-sf, x)'
        if not sf:
            raise IndexError
        ot, [x] = sf.ipop_tmay_(left_vs_right=False)
        return ot, x
    def ipop_right(sf, /):
        '-> (new-sf, x)'
        if not sf:
            raise IndexError
        ot, [x] = sf.ipop_tmay_(left_vs_right=True)
        return ot, x
    def iappend_left(sf, x, /):
        '-> (new-sf, None)'
        return sf.iappend_(x, left_vs_right=False)
    def iappend_right(sf, x, /):
        '-> (new-sf, None)'
        return sf.iappend_(x, left_vs_right=True)
    def __add__(sf, ot, /):
        '-> new-sf'
        if not isinstance(ot, type(sf)): raise TypeError
        if not sf.ops is ot.ops: raise TypeError
        if not sf._rv is ot._rv: raise NotImplementedError('order diff not supportted yet')
            #或许 可以 通过 给所以内部节点 打上 左起丷右起 来 实现 自由组合
        ops = sf.ops
        if sf._rv:
            sf, ot = ot, sf
        tree = ops.合并两树囗(sf._t, ot._t)
        st = (tree, sf._rv, ..., len(sf)+len(ot))
        ot = type(sf)(st, _=_kkkkk)
        return ot


    def __lshift__(sf, x, /):
        '-> new-sf'
        ot, _ = sf.iappend_right(x)
        return ot
    def __iadd__(sf, ot, /):
        '-> new-sf'
        return sf + ot
    def __ilshift__(sf, x, /):
        '-> new-sf'
        return sf << x
    def __getitem__(sf, k0, /):
        T = type(k0)
        ops = sf.ops
        tree = sf._t
        sz = len(sf)
        if T is int:
            i = k0
            if i < 0:
                i += sz
            if not 0 <= i < sz: raise IndexError(k0)
            if sf._rv:
                i = sz-1-i
            [x] = ops.取魊元素囗(tree, i)
            return x
        elif T is slice:
            sl = k0
            begin, end, step = sl.indices(sz)
            check_type_is(int, step)
            if not abs(step) == 1: raise TypeError(k0)

            reverse = step < 0
            if reverse:
                begin, end = end+1, begin+1
            if sf._rv:
                begin, end = sz-1-end, sz-1-begin
            tree = ops.取子树囗(tree, begin, end)
            _sz = max(0, end-begin)
            assert _sz == ops.取长度囗(tree)
            st = (tree, sf._rv ^ reverse, ..., _sz)
            ot = type(sf)(st, _=_kkkkk)
            return ot
        raise TypeError(T)


def _brute_force_iter_(reverse, xs, /):
    if not reverse:
        return iter(xs)
    try:
        it = reversed(xs)
    except TypeError:
        xs = [*xs]
        it = reversed(xs)
    return it
def _brute_force_calc_len_(ops, tree, /):
    try:
        return ops.查询整树属性囗(tree, 'len')
    except LookupError:
        pass
    it = ops.迭代元素囗(tree, 左起丷右起=False)
    sz = 0
    for sz, _ in enumerate(it, 1):
        pass
    return sz

__all__


from seed.data_funcs.finger_tree.FingerTree import FingerTree
from seed.data_funcs.finger_tree.FingerTree import *
