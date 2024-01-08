#__all__:goto
r'''[[[
w ../../python3_src/seed/types/MergeableHeap-ver1-eat-O(logM_mul_logN)-not-best.py
e ../../python3_src/seed/types/MergeableHeap.py
seed.types.MergeableHeap

[[[
===
used in:
    e script/matrix_chain_product.py
        e others/book/matrix_chain_product/Computation of matrix chain products I,II(1984)(Hu)(Shing)[polygon partitioning].pdf.txt

平衡二叉树:
    左右子树 高度相差 至多为一
[min_num_nodes_of_height(h) =[def]= if h==0 then 0 else if h==1 then 1 min_num_nodes_of_height(h-1)+min_num_nodes_of_height(h-2)+1]
[max_num_nodes_of_height(h) =[def]= if h==0 then 0 else max_num_nodes_of_height(h-1)+max_num_nodes_of_height(h-1)+1]
[max_num_nodes_of_height(h) == 2**h-1]
    0,1,3,7,15,31
    1,2,4,8,16,32
[min_num_nodes_of_height(h) == Fibonacci_sequence[h+2]-1]
    # ~= 1.618**h * K
        0,1,2,4,7,12
    0,1,1,2,3,5,8,13

[min_num_nodes_of_height,max_num_nodes_of_height 都是指数增长]
    高度 最多比 完美平衡树 多一半
>>> from math import log
>>> log(2)/log(1.618)
1.4404829720657013

O(1)操作:
    len(heap) -> size
    bool(heap) -> bool
    heap.peek() -> min_item
O(log(N))操作:
    heap.push(item)
    heap.pop() -> min_item
        取出最小值
    xxx heap.eat(std::move(heap))
        破坏性融合
        O(logN*logM)算法。比 普通情形O(N*logM)稍佳，但不及预期目标O(logN+logM)'
    heap.pushs([item])
    heap.push_then_pop(item) -> min_item
    heap.pop_then_push(item) -> min_item
O(N)操作:
    [*iter(heap)]
        非破坏性无序只读操作
    heap.as_tree() -> tree=(()|(payload, tree, tree))
O(N*log(N))操作:
    [*heap.iter_pops()]
        破坏性有序操作
]]]



py -m nn_ns.app.debug_cmd   seed.types.MergeableHeap
py -m seed.types.MergeableHeap

from seed.types.MergeableHeap import MergeableHeap, HeapError__Empty, HeapError__EatSelf


[[[
===

>>> from seed.types.MergeableHeap import MergeableHeap, HeapError__Empty, HeapError__EatSelf
>>> heap = MergeableHeap()
>>> heap
MergeableHeap()
>>> bool(heap)
False
>>> len(heap)
0
>>> [*iter(heap)]
[]
>>> [*heap.iter_pops()]
[]
>>> heap.as_tree()
()
>>> heap.verify()
>>> heap.push(999)
>>> heap.verify()
>>> heap
MergeableHeap([999])
>>> bool(heap)
True
>>> len(heap)
1
>>> [*iter(heap)]
[999]
>>> heap.as_tree()
(999, (), ())
>>> heap.peek()
999
>>> [*heap.iter_pops()]
[999]
>>> heap.peek() #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
HeapError__Empty
>>> heap.pop() #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
HeapError__Empty
>>> heap.eat(heap) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
HeapError__EatSelf

>>> heap.push(999)
>>> heap
MergeableHeap([999])
>>> heap.as_tree()
(999, (), ())

>>> heap.push(888)
>>> heap
MergeableHeap([888, 999])
>>> heap.as_tree()
(888, (999, (), ()), ())
>>> heap.verify()

>>> heap.push(222)
>>> heap
MergeableHeap([222, 999, 888])
>>> heap.as_tree()
(222, (999, (), ()), (888, (), ()))
>>> heap.verify()

>>> heap.push(333)
>>> heap
MergeableHeap([222, 333, 999, 888])
>>> heap.as_tree()
(222, (333, (999, (), ()), ()), (888, (), ()))
>>> heap.verify()

>>> heap.push(777)
>>> heap
MergeableHeap([222, 333, 999, 777, 888])
>>> heap.as_tree()
(222, (333, (999, (), ()), ()), (777, (888, (), ()), ()))
>>> heap.verify()

>>> heap.push(555)
>>> heap
MergeableHeap([222, 333, 999, 555, 777, 888])
>>> heap.as_tree()
(222, (333, (999, (), ()), (555, (), ())), (777, (888, (), ()), ()))
>>> heap.verify()

>>> heap.push(444)
>>> heap
MergeableHeap([222, 333, 444, 999, 555, 777, 888])
>>> heap.as_tree()
(222, (333, (444, (999, (), ()), ()), (555, (), ())), (777, (888, (), ()), ()))
>>> heap.verify()

>>> heap.push(666)
>>> heap
MergeableHeap([222, 333, 444, 999, 555, 666, 888, 777])
>>> heap.as_tree()
(222, (333, (444, (999, (), ()), ()), (555, (), ())), (666, (888, (), ()), (777, (), ())))
>>> heap.verify()

>>> heap.push(111)
>>> heap
MergeableHeap([111, 333, 444, 999, 555, 222, 666, 888, 777])
>>> heap.as_tree()
(111, (333, (444, (999, (), ()), ()), (555, (), ())), (222, (666, (888, (), ()), ()), (777, (), ())))
>>> heap.verify()

>>> bool(heap)
True
>>> len(heap)
9
>>> [*iter(heap)]
[111, 333, 444, 999, 555, 222, 666, 888, 777]
>>> heap.peek()
111
>>> heap.pop()
111
>>> heap.as_tree()
(222, (333, (444, (), ()), (555, (), ())), (666, (888, (999, (), ()), ()), (777, (), ())))
>>> heap.verify()

>>> heap.pop()
222
>>> heap.as_tree()
(333, (444, (999, (), ()), (555, (), ())), (666, (888, (), ()), (777, (), ())))
>>> heap.verify()

>>> heap.pop()
333
>>> heap.as_tree()
(444, (555, (), (999, (), ())), (666, (888, (), ()), (777, (), ())))
>>> heap.verify()

>>> heap.pop()
444
>>> heap.as_tree()
(555, (999, (), ()), (666, (888, (), ()), (777, (), ())))
>>> heap.verify()

>>> heap.pop()
555
>>> heap.as_tree()
(666, (999, (), ()), (777, (), (888, (), ())))
>>> heap.verify()

>>> heap.pop()
666
>>> heap.as_tree()
(777, (999, (), ()), (888, (), ()))
>>> heap.verify()

>>> heap.pop()
777
>>> heap.as_tree()
(888, (), (999, (), ()))
>>> heap.verify()

>>> [*heap.iter_pops()]
[888, 999]
>>> len(heap)
0
>>> bool(heap)
False
>>> heap.as_tree()
()
>>> heap.verify()
>>> heap
MergeableHeap()

>>> heap.pushs(range(111, 1000, 111))
>>> heap.as_tree()
(111, (222, (444, (777, (), ()), ()), (666, (), ())), (333, (555, (999, (), ()), ()), (888, (), ())))
>>> heap.verify()
>>> heap.push_then_pop(-555)
-555
>>> heap.as_tree()
(111, (222, (444, (777, (), ()), ()), (666, (), ())), (333, (555, (999, (), ()), ()), (888, (), ())))
>>> heap.verify()

>>> heap.clear()
>>> heap.as_tree()
()
>>> heap.pushs(range(111, 1000, 111))
>>> heap.push(-555)
>>> heap.as_tree()
(-555, (111, (444, (777, (), ()), ()), (222, (666, (), ()), ())), (333, (555, (999, (), ()), ()), (888, (), ())))
>>> heap.verify()

>>> heap.pop()
-555
>>> heap.as_tree()
(111, (222, (444, (), ()), (666, (777, (), ()), ())), (333, (555, (999, (), ()), ()), (888, (), ())))
>>> heap.verify()



>>> heap.clear()
>>> heap.as_tree()
()
>>> heap.pushs(range(999, 100, -111))
>>> heap.as_tree()
(111, (444, (555, (999, (), ()), ()), (777, (), ())), (222, (333, (888, (), ()), ()), (666, (), ())))
>>> heap.verify()
>>> heap.pop_then_push(-555)
111
>>> heap.as_tree()
(-555, (444, (555, (999, (), ()), ()), (777, (), ())), (222, (333, (888, (), ()), ()), (666, (), ())))
>>> heap.verify()

>>> heap.clear()
>>> heap.as_tree()
()
>>> heap.pushs(range(999, 100, -111))
>>> heap.as_tree()
(111, (444, (555, (999, (), ()), ()), (777, (), ())), (222, (333, (888, (), ()), ()), (666, (), ())))
>>> heap.pop()
111
>>> heap.as_tree()
(222, (444, (555, (), ()), (777, (), ())), (333, (888, (999, (), ()), ()), (666, (), ())))
>>> heap.verify()
>>> heap.push(-555)
>>> heap.as_tree()
(-555, (222, (444, (555, (), ()), ()), (777, (), ())), (333, (888, (999, (), ()), ()), (666, (), ())))
>>> heap.verify()






>>> heap.clear()
>>> heap.pushs(range(111, 1000, 111))
>>> heap.pop_then_push(700)
111
>>> heap.as_tree()
(222, (444, (700, (777, (), ()), ()), (666, (), ())), (333, (555, (999, (), ()), ()), (888, (), ())))
>>> heap.verify()
>>> heap.push_then_pop(400)
222
>>> heap.as_tree()
(333, (444, (700, (777, (), ()), ()), (666, (), ())), (400, (555, (999, (), ()), ()), (888, (), ())))
>>> heap.verify()












>>> heap.clear()
>>> heap.pushs(range(111, 1000, 111))
>>> heap2 = MergeableHeap(range(99, 10, -11))
>>> heap.as_tree()
(111, (222, (444, (777, (), ()), ()), (666, (), ())), (333, (555, (999, (), ()), ()), (888, (), ())))
>>> heap2.as_tree()
(11, (44, (55, (99, (), ()), ()), (77, (), ())), (22, (33, (88, (), ()), ()), (66, (), ())))
>>> heap.eat(heap2)
>>> heap2.as_tree()
()
>>> heap.as_tree()
(11, (22, (44, (55, (99, (), ()), ()), (77, (), ())), (33, (88, (111, (), ()), ()), (66, (), ()))), (222, (444, (777, (), ()), (666, (), ())), (333, (555, (999, (), ()), ()), (888, (), ()))))
>>> heap.verify()

>>> heap.clear()
>>> heap.pushs(range(111, 1000, 111))
>>> heap2 = MergeableHeap(range(44, 10, -11))
>>> heap2.as_tree()
(11, (22, (44, (), ()), ()), (33, (), ()))
>>> heap.eat(heap2)
>>> heap2.as_tree()
()
>>> heap.as_tree()
(11, (22, (222, (444, (777, (), ()), ()), (666, (), ())), (33, (44, (), ()), (111, (), ()))), (333, (555, (999, (), ()), ()), (888, (), ())))



>>> heap.verify()

>>> heap.clear()
>>> heap.pushs(range(111, 500, 111))
>>> heap2 = MergeableHeap(range(88, 10, -11))
>>> heap.as_tree()
(111, (222, (444, (), ()), ()), (333, (), ()))
>>> heap2.as_tree()
(11, (33, (44, (88, (), ()), ()), (66, (), ())), (22, (77, (), ()), (55, (), ())))
>>> heap.eat(heap2)
>>> heap2.as_tree()
()
>>> heap.as_tree()
(11, (33, (44, (88, (), ()), ()), (66, (), ())), (22, (55, (77, (), ()), (111, (), ())), (222, (444, (), ()), (333, (), ()))))
>>> heap.verify()




>>> heap = MergeableHeap(key=len)
>>> heap.push({1,2,3})
>>> heap.push(range(100))
>>> heap.peek()
{1, 2, 3}
>>> heap.verify()

>>> heap = MergeableHeap(key=len, __lt__=opss.__gt__)
>>> heap.push({1,2,3})
>>> heap.push(range(100))
>>> heap.peek()
range(0, 100)
>>> heap.verify()



]]]

#]]]'''
__all__ = '''
    MergeableHeap
        HeapError__Empty
        HeapError__EatSelf

    '''.split()

import operator as opss
from itertools import pairwise
from seed.tiny import echo, null_tuple
from seed.helper.repr_input import repr_helper


class _MHNodeEmpty:
    is_empty = True
    height = 0
    size = 0
_empty_node = _MHNodeEmpty()
class _MHNode:
    __slots__ = '''
        payload
        lhs_child
        rhs_child
        height
        size
        '''.split()
    is_empty = False
    def __init__(sf, payload, lhs_child, rhs_child, /):
        assert isinstance(lhs_child, _MHNodeTypes)
        assert isinstance(rhs_child, _MHNodeTypes)
        assert abs(lhs_child.height-rhs_child.height) <= 1
        sf.payload = payload
        sf.lhs_child = lhs_child
        sf.rhs_child = rhs_child
        sf.fresh()
    def fresh(sf, /):
        if not abs(sf.lhs_child.height-sf.rhs_child.height) <= 1:raise logic-err
        sf.height = 1+max(sf.lhs_child.height, sf.rhs_child.height)
        sf.size = 1 + sf.lhs_child.size + sf.rhs_child.size
    @property
    def children(sf, /):
        return (sf.lhs_child, sf.rhs_child)
    @property
    def sorted_children(sf, /):
        return sorted(sf.children, key=_get_height4node)
    @property
    def large_child(sf, /):
        return max(sf.children, key=_get_height4node)
    @property
    def small_child(sf, /):
        return min(sf.children, key=_get_height4node)
def _get_height4node(node, /):
    return node.height
_MHNodeTypes = (_MHNode, _MHNodeEmpty)

class HeapError__Empty(Exception):pass
class HeapError__EatSelf(Exception):pass
class HeapError__Validate(Exception):pass

class MergeableHeap:
    def __init__(sf, iterable=None, /, *, key=None, __lt__=None):
        sf._key_func = echo if key is None else key
        sf._lt = opss.__lt__ if __lt__ is None else __lt__
        sf._node = _empty_node
        iterable = '' if iterable is None else iterable
        sf.pushs(iterable)
    def verify(sf, /):
        for node in _unorder_iter_nodes5root(sf._node):
            sf._verify__node(node)
    def _verify__node(sf, node, /):
        if not node.is_empty:
            if not all(1 <= node.height-child.height <= 2 for child in node.children): raise HeapError__Validate
            if not any(node.height-child.height == 1 for child in node.children): raise HeapError__Validate
            if not abs(node.lhs_child.height-node.rhs_child.height) <= 1: raise HeapError__Validate
            if any(sf._lt__node(child, node) for child in node.children): raise HeapError__Validate

    def clear(sf, /):
        sf._node = _empty_node
    def pushs(sf, iterable, /):
        for _ in map(sf.push, iterable):pass
    def iter_pops(sf, /):
        while sf:
            yield sf.pop()
        return
    def __bool__(sf, /):
        return not (sf._node.is_empty)
        return bool(sf._node.size)
        return sf._node is _empty_node
    def __len__(sf, /):
        return (sf._node.size)
    def as_tree(sf, /):
        'tree=(()|(payload, tree, tree))'
        return _node_as_tree(sf._node)
    def __iter__(sf, /):
        'unorder iter'
        return _unorder_iter_payloads5root(sf._node)

    def __repr__(sf, /):
        kwargs = {}
        if not sf._key_func is echo:
            kwargs.update(key=sf._key_func)
        if not sf._lt is opss.__lt__:
            kwargs.update(__lt__=sf._lt)
        iterable = [*sf]
        args = [iterable] if iterable else []
        return repr_helper(sf, *args, **kwargs)

    def peek(sf, /):
        if not sf:
            raise HeapError__Empty
        return sf._node.payload
    def _lt__node(sf, lhs_node, rhs_node, /):
        '[_empty_node == +oo] <<== _pushdown_payload_at_root'
        if lhs_node.is_empty:
            return False
        if rhs_node.is_empty:
            return True
        return sf._lt__payload(lhs_node.payload, rhs_node.payload)
    def _lt__payload(sf, lhs_payload, rhs_payload, /):
        return sf._lt(sf._key_func(lhs_payload), sf._key_func(rhs_payload))
    def pop_then_push(sf, payload, /):
        payload = _pop_then_push(sf, sf._node, payload)
        return payload
    def push_then_pop(sf, payload, /):
        if not sf:
            return payload
        if not sf._lt__payload(sf.peek(), payload):
            return payload
        return sf.pop_then_push(payload)

    def pop(sf, /):
        payload, sf._node = _pop(sf, sf._node)
        return payload
    def push(sf, payload, /):
        sf._node = _push(sf, sf._node, payload)
    def eat(sf, other_heap, /):
        'heap.eat(std::move(heap))'
        if sf is other_heap: raise HeapError__EatSelf
        if not isinstance(other_heap, __class__):raise TypeError
        if not sf._lt is other_heap._lt:raise TypeError
        if not sf._key_func is other_heap._key_func:raise TypeError
        sf._node = _eat(sf, sf._node, other_heap._node)
        other_heap._node = _empty_node



def _pop(sf, root, /):
    '-> (payload, root)|raise HeapError__Empty'
    if root.is_empty: raise HeapError__Empty
    ls = [root]
    while not ls[-1].is_empty:
        ls.append(ls[-1].large_child)
    ls.pop()
    if not ls: raise logic-err
    removed_leaf = ls.pop()
    assert removed_leaf.height == 1
    if ls:
        last = ls[-1]
        _replace_child(last, removed_leaf, _empty_node)

        _fresh_nodes(ls)

        payload = _pop_then_push(sf, root, removed_leaf.payload)
    else:
        payload = root.payload
        root = _empty_node

    return (payload, root)

def _pop_then_push(sf, root, payload, /):
    _payload = root.payload
    root.payload = payload
    _pushdown_payload_at_root(sf, root)
    return _payload
def _pushdown_payload_at_root(sf, root, /):
    assert root.size
    while root.size > 1:
        if sf._lt__node(root.lhs_child, root.rhs_child):
            min_child = root.lhs_child
        else:
            min_child = root.rhs_child
        if sf._lt__node(min_child, root):
            _swap_payload4node(min_child, root)
            root = min_child
        else:
            break
def _swap_payload4node(lhs_node, rhs_node, /):
    lhs_node.payload, rhs_node.payload = rhs_node.payload, lhs_node.payload




def _push(sf, root, payload, /):
    '-> root'
    new_node = _MHNode(payload, _empty_node, _empty_node)
    if root.is_empty:
        root = new_node
    else:
        ls = [root]
        while not ls[-1].is_empty:
            ls.append(ls[-1].small_child)
        empty_leaf = ls.pop()
        if not ls: raise logic-err
        last = ls[-1]
        _replace_child(last, empty_leaf, new_node)

        _fresh_nodes(ls)
        ls.append(new_node)
        _popup(sf, ls)
    return root

def _replace_child(parent, old_child, new_child, /):
    if parent.lhs_child is old_child:
        parent.lhs_child = new_child
    elif parent.rhs_child is old_child:
        parent.rhs_child = new_child
    else:
        raise logic-err

def _eat(sf, lhs_root, rhs_root, /):
    '-> root #O(logN*logM)算法。比 普通情形O(N*logM)稍佳，但不及预期目标O(logN+logM)'
    (rhs_root, lhs_root) = sorted([lhs_root, rhs_root], key=_get_height4node)

    if rhs_root.is_empty:
        #[rhs_root is lhs_root is _empty_node] is OK
        return lhs_root
    if rhs_root is lhs_root:
        #[rhs_root is lhs_root is not _empty_node] is bug
        raise HeapError__EatSelf
    if rhs_root.height == 1:
        return _push(sf, lhs_root, rhs_root.payload)

    assert 2 <= rhs_root.height <= lhs_root.height

    ls = [lhs_root]
    while ls[-1].height > rhs_root.height:
        ls.append(ls[-1].small_child)
    last = ls.pop()
    assert last.height <= rhs_root.height
    assert not ls or 1 <= ls[-1].height - last.height <= 2
    assert not ls or 1 <= ls[-1].height - rhs_root.height <= 2
    assert 0 <= rhs_root.height - last.height <= 1

    if 0:
        #bug:
        if last.is_empty:
            new_node = rhs_root
        else:
            payload, rhs_root = _pop(sf, rhs_root)
            new_node = _MHNode(payload, last, rhs_root)
            _pushdown_payload_at_root(sf, new_node)
        if ls:
            _replace_child(ls[-1], last, new_node)

        _fresh_nodes(ls)
        ls.append(new_node)
        _popup(sf, ls)
        return ls[0]
    else:
        for node in ls:
            # len(ls) = O(lhs.height-rhs.height)
            # len(ls)*_pushdown_payload_at_root<rhs> = O((lhs.height-rhs.height)*rhs.height) = O((logM-logN)*logN) = O(logN*logM) < O(N*logM)
            if sf._lt__node(rhs_root, node):
                _swap_payload4node(rhs_root, node)
                _pushdown_payload_at_root(sf, rhs_root)


        if last.is_empty:
            new_node = rhs_root
        #elif last.height == 1:
        #    new_node = _push(sf, rhs_root, last.payload)
        else:
            payload, rhs_root = _pop(sf, rhs_root)
            new_node = _MHNode(payload, last, rhs_root)
            _pushdown_payload_at_root(sf, new_node)
        if ls:
            _replace_child(ls[-1], last, new_node)

        _fresh_nodes(ls)
        ls.append(new_node)
        #_popup(sf, ls)
        return ls[0]


def _fresh_nodes(nodes, /):
    for node in reversed(nodes):
        node.fresh()
def _popup(sf, nodes, /):
    for child, parent in pairwise(reversed(nodes)):
        if sf._lt__node(child, parent):
            _swap_payload4node(child, parent)
        else:
            break

def _unorder_iter_payloads5root(root, /):
    for node in _unorder_iter_nodes5root(root):
        yield node.payload
def _unorder_iter_nodes5root(root, /):
    ls = [root]
    while ls:
        node = ls.pop()
        if not node.is_empty:
            yield node
            ls.append(node.rhs_child)
            ls.append(node.lhs_child)

def _node_as_tree(root, /):
    'tree=(()|(payload, tree, tree))'
    xs = []
    ls = [root]
    while ls:
        node = ls.pop()
        xs.append(node)
        if not node.is_empty:
            ls.append(node.rhs_child)
            ls.append(node.lhs_child)
    #xs = [root, root.lhs_child, ..., root.rhs_child, ...]
    while xs:
        node = xs.pop()
        if node.is_empty:
            tree = null_tuple
        else:
            children = []
            children.append(ls.pop())
            children.append(ls.pop())
            assert len(children)==2
            tree = (node.payload, *children)
        ls.append(tree)
    [tree] = ls
    return tree

if __name__ == "__main__":
    import doctest
    doctest.testmod()




