#__all__:goto
#testing_________goto:goto
r'''[[[
seed.types.MergeableHeap__immutable_tree
view ../../python3_src/seed/types/MergeableHeap__immutable_tree.py
    using immutable_tree underlying
    O(1) copy
    ++unoin/merge: like eat() but donot clear() input heap
view ../../python3_src/seed/types/MergeableHeap__mutable_tree.py
    just forward seed.types.MergeableHeap

e ../../python3_src/seed/types/MergeableHeap__immutable_tree.py
    ver1:
        view ../../python3_src/seed/types/MergeableHeap-ver1-eat-O(logM_mul_logN)-not-best.py
        所有 非叶节点 含payload
        eat() - O(logM*logN)
    ver2:
        view ../../python3_src/seed/types/MergeableHeap.py
        view ../../python3_src/seed/types/MergeableHeap__mutable_tree.py
        所有 二叉节点fork 含min_payload
        只有 单元节点unit 含 min_payload是payload
        eat() - O(logM+logN)
    ver3 [当前]:
        view ../../python3_src/seed/types/MergeableHeap__immutable_tree.py
        using immutable_tree


[[[
===
used in:
    e script/matrix_chain_product.py
        e others/book/matrix_chain_product/Computation of matrix chain products I,II(1984)(Hu)(Shing)[polygon partitioning].pdf.txt

以下ver1相关，已过时[[
平衡二叉树:
    左右子树 高度相差 至多为一
[min_num_nodes_of_height(h) =[def]= if h==0 then 0 else if h==1 then 1 else min_num_nodes_of_height(h-1)+min_num_nodes_of_height(h-2)+1]
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

]]

ver2[[
bug: [min_num_nodes_of_height(h) =[def]= if h==0 then 0 else if h==1 then 1 else min_num_nodes_of_height(h-1)+min_num_nodes_of_height(h-2)+1]
[min_num_nodes_of_height(h) =[def]= if h==0 then 0 else if h==1 then 1 else if h==2 then 3 else min_num_nodes_of_height(h-1)+min_num_nodes_of_height(h-2)+1]
    非叶节点的数量:二叉节点+单元节点 # 不含 空叶节点
    (2->3)是因为 二叉节点 的 直接子代 不是 空叶节点
    0,1,3,5,9,15,25,41,67,109
    see:_eat_
[min_num_payloads_of_height(h) =[def]= if h==0 then 0 else if h==1 then 1 else if h==2 then 2 else min_num_payloads_of_height(h-1)+min_num_payloads_of_height(h-2)]
    实际数据的数量:单元节点
    (2->2)是因为 二叉节点 的 直接子代 不含 空叶节点
    0,1,2,3,5,8,13,21,34,55,89
[min_num_payloads_of_height(h) == Fibonacci_sequence[h+1] -[h==0]]
      0,1,2,3,5, 8,13
    0,1,1,2,3,5, 8,13
      0,1,3,5,9,15,25,41,67,109
[min_num_nodes_of_height(h) == min_num_payloads_of_height(h)*2 -1 +[h==0]]
    !! [num_nodes_of_height(tree) == max(0, num_payloads_of_height(tree)*2 -1)]
[min_num_nodes_of_height(h) == Fibonacci_sequence[h+1]*2 -1 -[h==0]]


[max_num_nodes_of_height(h) =[def]= if h==0 then 0 else max_num_nodes_of_height(h-1)+max_num_nodes_of_height(h-1)+1]
[max_num_payloads_of_height(h) =[def]= if h==0 then 0 else if h==1 then 1 else max_num_payloads_of_height(h-1)+max_num_payloads_of_height(h-1)]
[max_num_nodes_of_height(h) == 2**h-1]
[max_num_payloads_of_height(h) == floor(2**(h-1))]

]]

O(1)操作:
    len(heap) -> size
    bool(heap) -> bool
    heap.peak() -> min_item
O(log(N))操作:
    heap.push(item)
    heap.pop() -> min_item
        取出最小值
    heap.merge(const& heap)
        ver3[当前]:O(logN+logM)
        new in ver3
    heap.eat(std::move(heap))
        破坏性融合
        ver1:O(logN*logM)算法。比 普通情形O(N*logM)稍佳，但不及预期目标O(logN+logM)
        ver2:O(logN+logM)
    heap.push_then_pop(item) -> min_item
    heap.pop_then_push(item) -> min_item
O(logN+M+logM)操作:
    heap.pushs([item])
O(M)操作:
    MergeableHeap([item])
O(N)操作:
    [*iter(heap)]
        非破坏性无序只读操作
    heap.as_tree() -> tree=(()|(payload, tree, tree))
O(N*log(N))操作:
    [*heap.iter_pops()]
        破坏性有序操作
    heap.to_sorted()
        new in ver3
]]]



py -m nn_ns.app.debug_cmd   seed.types.MergeableHeap__immutable_tree
py -m seed.types.MergeableHeap__immutable_tree

from seed.types.MergeableHeap__immutable_tree import MergeableHeap__immutable_tree, MergeableHeap, HeapError__Empty, HeapError__EatSelf, HeapError__Validate


[[[
===

>>> from seed.types.MergeableHeap__immutable_tree import MergeableHeap__immutable_tree, MergeableHeap, HeapError__Empty, HeapError__EatSelf, HeapError__Validate
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
>>> heap.peak()
999
>>> [*heap.iter_pops()]
[999]
>>> heap.peak() #doctest: +IGNORE_EXCEPTION_DETAIL
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
MergeableHeap([999, 888])
>>> heap.as_tree()
(888, (999, (), ()), (888, (), ()))
>>> heap.verify()

>>> heap.push(222)
>>> heap
MergeableHeap([999, 222, 888])
>>> heap.as_tree()
(222, (222, (999, (), ()), (222, (), ())), (888, (), ()))
>>> heap.verify()

>>> heap.push(333)
>>> heap
MergeableHeap([999, 222, 888, 333])
>>> heap.as_tree()
(222, (222, (999, (), ()), (222, (), ())), (333, (888, (), ()), (333, (), ())))
>>> heap.verify()

>>> heap.push(777)
>>> heap
MergeableHeap([999, 777, 222, 888, 333])
>>> heap.as_tree()
(222, (222, (777, (999, (), ()), (777, (), ())), (222, (), ())), (333, (888, (), ()), (333, (), ())))
>>> heap.verify()

>>> heap.push(555)
>>> heap
MergeableHeap([999, 777, 222, 888, 555, 333])
>>> heap.as_tree()
(222, (222, (777, (999, (), ()), (777, (), ())), (222, (), ())), (333, (555, (888, (), ()), (555, (), ())), (333, (), ())))
>>> heap.verify()

>>> heap.push(444)
>>> heap
MergeableHeap([999, 777, 222, 444, 888, 555, 333])
>>> heap.as_tree()
(222, (222, (777, (999, (), ()), (777, (), ())), (222, (222, (), ()), (444, (), ()))), (333, (555, (888, (), ()), (555, (), ())), (333, (), ())))
>>> heap.verify()

>>> heap.push(666)
>>> heap
MergeableHeap([999, 666, 777, 222, 444, 888, 555, 333])
>>> heap.as_tree()
(222, (222, (666, (666, (999, (), ()), (666, (), ())), (777, (), ())), (222, (222, (), ()), (444, (), ()))), (333, (555, (888, (), ()), (555, (), ())), (333, (), ())))
>>> heap.verify()

>>> heap.push(111)
>>> heap
MergeableHeap([999, 666, 777, 222, 444, 888, 555, 333, 111])
>>> heap.as_tree()
(111, (222, (666, (666, (999, (), ()), (666, (), ())), (777, (), ())), (222, (222, (), ()), (444, (), ()))), (111, (555, (888, (), ()), (555, (), ())), (111, (333, (), ()), (111, (), ()))))
>>> heap.verify()

>>> bool(heap)
True
>>> len(heap)
9
>>> [*iter(heap)]
[999, 666, 777, 222, 444, 888, 555, 333, 111]
>>> heap.peak()
111
>>> heap.pop()
111
>>> heap.as_tree()
(222, (222, (666, (666, (), ()), (777, (), ())), (222, (222, (), ()), (444, (), ()))), (333, (555, (888, (), ()), (555, (), ())), (333, (333, (), ()), (999, (), ()))))
>>> heap.verify()

>>> heap.pop()
222
>>> heap.as_tree()
(333, (444, (777, (), ()), (444, (666, (), ()), (444, (), ()))), (333, (555, (888, (), ()), (555, (), ())), (333, (333, (), ()), (999, (), ()))))
>>> heap.verify()

>>> heap.pop()
333
>>> heap.as_tree()
(444, (444, (777, (), ()), (444, (), ())), (555, (555, (888, (), ()), (555, (), ())), (666, (666, (), ()), (999, (), ()))))
>>> heap.verify()

>>> heap.pop()
444
>>> heap.as_tree()
(555, (777, (777, (), ()), (888, (), ())), (555, (555, (), ()), (666, (666, (), ()), (999, (), ()))))
>>> heap.verify()

>>> heap.pop()
555
>>> heap.as_tree()
(666, (777, (777, (), ()), (888, (), ())), (666, (666, (), ()), (999, (), ())))
>>> heap.verify()

>>> heap.pop()
666
>>> heap.as_tree()
(777, (888, (), ()), (777, (777, (), ()), (999, (), ())))
>>> heap.verify()

>>> heap.pop()
777
>>> heap.as_tree()
(888, (888, (), ()), (999, (), ()))
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
(111, (111, (111, (111, (), ()), (222, (), ())), (333, (333, (), ()), (444, (), ()))), (555, (555, (555, (), ()), (666, (), ())), (777, (777, (777, (), ()), (888, (), ())), (999, (), ()))))
>>> heap.verify()
>>> heap.push_then_pop(-555)
-555
>>> heap.as_tree()
(111, (111, (111, (111, (), ()), (222, (), ())), (333, (333, (), ()), (444, (), ()))), (555, (555, (555, (), ()), (666, (), ())), (777, (777, (777, (), ()), (888, (), ())), (999, (), ()))))
>>> heap.verify()


>>> heap.clear()
>>> heap.as_tree()
()
>>> heap.pushs(range(111, 1000, 111))
>>> heap.push(-555)
>>> heap.as_tree()
(-555, (-555, (-555, (-555, (111, (), ()), (-555, (), ())), (222, (), ())), (333, (333, (), ()), (444, (), ()))), (555, (555, (555, (), ()), (666, (), ())), (777, (777, (777, (), ()), (888, (), ())), (999, (), ()))))
>>> heap.verify()

>>> heap.pop()
-555
>>> heap.as_tree()
(111, (111, (111, (111, (), ()), (222, (), ())), (333, (333, (), ()), (444, (), ()))), (555, (555, (555, (), ()), (666, (), ())), (777, (777, (777, (), ()), (888, (), ())), (999, (), ()))))
>>> heap.verify()



>>> heap.clear()
>>> heap.as_tree()
()
>>> heap.pushs(range(999, 100, -111))
>>> heap.as_tree()
(111, (666, (888, (999, (), ()), (888, (), ())), (666, (777, (), ()), (666, (), ()))), (111, (444, (555, (), ()), (444, (), ())), (111, (222, (333, (), ()), (222, (), ())), (111, (), ()))))
>>> heap.verify()
>>> heap.pop_then_push(-555)
111
>>> heap.as_tree()
(-555, (666, (888, (999, (), ()), (888, (), ())), (666, (777, (), ()), (666, (), ()))), (-555, (444, (555, (), ()), (444, (), ())), (-555, (222, (333, (), ()), (222, (), ())), (-555, (), ()))))
>>> heap.verify()

>>> heap.clear()
>>> heap.as_tree()
()
>>> heap.pushs(range(999, 100, -111))
>>> heap.as_tree()
(111, (666, (888, (999, (), ()), (888, (), ())), (666, (777, (), ()), (666, (), ()))), (111, (444, (555, (), ()), (444, (), ())), (111, (222, (333, (), ()), (222, (), ())), (111, (), ()))))
>>> heap.pop()
111
>>> heap.as_tree()
(222, (666, (888, (999, (), ()), (888, (), ())), (666, (777, (), ()), (666, (), ()))), (222, (444, (555, (), ()), (444, (), ())), (222, (222, (), ()), (333, (), ()))))
>>> heap.verify()
>>> heap.push(-555)
>>> heap.as_tree()
(-555, (-555, (-555, (-555, (999, (), ()), (-555, (), ())), (888, (), ())), (666, (777, (), ()), (666, (), ()))), (222, (444, (555, (), ()), (444, (), ())), (222, (222, (), ()), (333, (), ()))))
>>> heap.verify()






>>> heap.clear()
>>> heap.pushs(range(111, 1000, 111))
>>> heap.pop_then_push(700)
111
>>> heap.as_tree()
(222, (222, (222, (700, (), ()), (222, (), ())), (333, (333, (), ()), (444, (), ()))), (555, (555, (555, (), ()), (666, (), ())), (777, (777, (777, (), ()), (888, (), ())), (999, (), ()))))
>>> heap.verify()
>>> heap.push_then_pop(400)
222
>>> heap.as_tree()
(333, (333, (400, (700, (), ()), (400, (), ())), (333, (333, (), ()), (444, (), ()))), (555, (555, (555, (), ()), (666, (), ())), (777, (777, (777, (), ()), (888, (), ())), (999, (), ()))))
>>> heap.verify()












>>> heap.clear()
>>> heap.pushs(range(111, 1000, 111))
>>> heap2 = MergeableHeap(range(99, 10, -11))
>>> heap.as_tree()
(111, (111, (111, (111, (), ()), (222, (), ())), (333, (333, (), ()), (444, (), ()))), (555, (555, (555, (), ()), (666, (), ())), (777, (777, (777, (), ()), (888, (), ())), (999, (), ()))))
>>> heap2.as_tree()
(11, (66, (88, (99, (), ()), (88, (), ())), (66, (77, (), ()), (66, (), ()))), (11, (44, (55, (), ()), (44, (), ())), (11, (22, (33, (), ()), (22, (), ())), (11, (), ()))))
>>> heap.eat(heap2)
>>> heap2.as_tree()
()
>>> heap.as_tree()
(11, (111, (111, (111, (111, (), ()), (222, (), ())), (333, (333, (), ()), (444, (), ()))), (555, (555, (555, (), ()), (666, (), ())), (777, (777, (777, (), ()), (888, (), ())), (999, (), ())))), (11, (66, (88, (99, (), ()), (88, (), ())), (66, (77, (), ()), (66, (), ()))), (11, (44, (55, (), ()), (44, (), ())), (11, (22, (33, (), ()), (22, (), ())), (11, (), ())))))
>>> heap.verify()


>>> heap.clear()
>>> heap.pushs(range(111, 1000, 111))
>>> heap2 = MergeableHeap(range(44, 10, -11))
>>> heap2.as_tree()
(11, (33, (44, (), ()), (33, (), ())), (11, (22, (), ()), (11, (), ())))
>>> heap.eat(heap2)
>>> heap2.as_tree()
()
>>> heap.as_tree()
(11, (11, (111, (111, (111, (), ()), (222, (), ())), (333, (333, (), ()), (444, (), ()))), (11, (33, (44, (), ()), (33, (), ())), (11, (22, (), ()), (11, (), ())))), (555, (555, (555, (), ()), (666, (), ())), (777, (777, (777, (), ()), (888, (), ())), (999, (), ()))))
>>> heap.verify()




>>> heap.clear()
>>> heap.pushs(range(111, 500, 111))
>>> heap2 = MergeableHeap(range(88, 10, -11))
>>> heap.as_tree()
(111, (111, (111, (), ()), (222, (), ())), (333, (333, (), ()), (444, (), ())))
>>> heap2.as_tree()
(11, (55, (77, (88, (), ()), (77, (), ())), (55, (66, (), ()), (55, (), ()))), (11, (33, (44, (), ()), (33, (), ())), (11, (22, (), ()), (11, (), ()))))
>>> heap.eat(heap2)
>>> heap2.as_tree()
()
>>> heap.as_tree()
(11, (55, (55, (77, (88, (), ()), (77, (), ())), (55, (66, (), ()), (55, (), ()))), (111, (111, (111, (), ()), (222, (), ())), (333, (333, (), ()), (444, (), ())))), (11, (33, (44, (), ()), (33, (), ())), (11, (22, (), ()), (11, (), ()))))
>>> heap.verify()




>>> heap = MergeableHeap(key=len)
>>> heap.push({1,2,3})
>>> heap.push(range(100))
>>> heap.peak()
{1, 2, 3}
>>> heap.verify()

>>> heap = MergeableHeap(key=len, __lt__=opss.__gt__)
>>> heap.push({1,2,3})
>>> heap.push(range(100))
>>> heap.peak()
range(0, 100)
>>> heap.verify()

>>> heap = MergeableHeap(key=len, __lt__=opss.__gt__, reverse=True)
>>> heap.push({1,2,3})
>>> heap.push(range(100))
>>> heap.peak()
{1, 2, 3}
>>> heap.verify()



>>> heap = MergeableHeap([1, 2, 3])
>>> heap
MergeableHeap([1, 2, 3])
>>> heap.merge(heap)
>>> heap
MergeableHeap([1, 2, 3, 1, 2, 3])
>>> heap.verify()

>>> heap2 = MergeableHeap([4, 5, 6])
>>> heap2
MergeableHeap([4, 5, 6])
>>> heap | heap2
MergeableHeap([1, 2, 3, 4, 5, 6, 1, 2, 3])
>>> heap
MergeableHeap([1, 2, 3, 1, 2, 3])
>>> heap2
MergeableHeap([4, 5, 6])
>>> heap.verify()

>>> heap.merge(heap2)
>>> heap
MergeableHeap([1, 2, 3, 4, 5, 6, 1, 2, 3])
>>> heap2
MergeableHeap([4, 5, 6])
>>> heap.verify()


testing_________goto
    #]]]'''
r'''[[[
]]]

#]]]'''
__all__ = '''
    MergeableHeap__immutable_tree
    MergeableHeap
        HeapError__Empty
        HeapError__EatSelf
        HeapError__Validate

    '''.split()

import operator as opss
from itertools import pairwise
from seed.tiny import echo, null_tuple
from seed.helper.repr_input import repr_helper

from collections import namedtuple

class _MHNodeEmpty:
    __slots__ = ()
    is_empty = True
    is_unit = False
    is_fork = False
    height = 0
    size = 0
_empty_node = _MHNodeEmpty()
_MHNode = namedtuple('_MHNode', '''
    min_payload
    lhs_child
    rhs_child
    height
    size
    '''.split()
    )
class _MHNode(_MHNode):
    __slots__ = ()
    is_empty = False
    is_unit = False
    is_fork = True

    __iter__ = None
    __len__ = None
    __bool__ = None
    __getitem__ = None
    def __new__(cls, _lt__node, lhs_child, rhs_child, /):
        cls.check_args(lhs_child, rhs_child)
        (height, size) = cls.prepare_auto_args__shape(lhs_child, rhs_child)
        min_payload = cls.prepare_auto_arg__min_payload(_lt__node, lhs_child, rhs_child)
        sf = super(__class__, cls).__new__(cls, min_payload, lhs_child, rhs_child, height, size)
        return sf

    @classmethod
    def check_args(cls, lhs_child, rhs_child, /):
        assert isinstance(lhs_child, _MHNodeChildTypes)
        assert isinstance(rhs_child, _MHNodeChildTypes)
        assert abs(lhs_child.height - rhs_child.height) <= 1
        assert min(lhs_child.height, rhs_child.height) >= 1
    @classmethod
    def prepare_auto_args__shape(cls, lhs_child, rhs_child, /):
        height = 1+max(lhs_child.height, rhs_child.height)
        size = lhs_child.size + rhs_child.size
        return (height, size)
    @classmethod
    def prepare_auto_arg__min_payload(cls, _lt__node, lhs_child, rhs_child, /):
        min_child = rhs_child if _lt__node(rhs_child, lhs_child) else lhs_child
        min_payload = min_child.min_payload
        return min_payload



    @property
    def children(sf, /):
        return (sf.lhs_child, sf.rhs_child)
    @property
    def sorted_children_by_height(sf, /):
        return sorted(sf.children, key=_get_height4node)
    @property
    def large_child(sf, /):
        'giant'
        return max(sf.children, key=_get_height4node)
    @property
    def small_child(sf, /):
        'dwarf'
        return min(sf.children, key=_get_height4node)
    @property
    def the_min_payload_child(sf, /):
        for child in sf.children:
            if sf.min_payload is child.min_payload:
                break
        else:
            raise logic-err
        return child
    def another_child_of(sf, old_child, /):

        if sf.lhs_child is old_child:
            return sf.rhs_child
        elif sf.rhs_child is old_child:
            return sf.lhs_child
        else:
            raise logic-err
def _get_height4node(node, /):
    return node.height
_MHNodeUnit = namedtuple('_MHNodeUnit', '''
    payload
    '''.split()
    )

class _MHNodeUnit(_MHNodeUnit):
    __slots__ = ()
    is_empty = False
    is_unit = True
    is_fork = False
        #crotch fork
    lhs_child = _empty_node
    rhs_child = _empty_node
    height = 1
    size = 1

    __iter__ = None
    __len__ = None
    __bool__ = None
    __getitem__ = None
    @property
    def min_payload(sf, /):
        return sf.payload
    children = (_empty_node,)*2
    sorted_children_by_height = children
    small_child, large_child = sorted_children_by_height
    #no:the_min_payload_child
_MHNodeTypes = (_MHNode, _MHNodeUnit, _MHNodeEmpty)
_MHNodeChildTypes = (_MHNode, _MHNodeUnit)
del _MHNodeEmpty

class HeapError__Empty(Exception):pass
class HeapError__EatSelf(Exception):pass
class HeapError__Validate(Exception):pass


class _MergeableHeap__mixin:
    __slots__ = ()
    def verify(sf, /):
        for node in _unorder_iter_nodes5root(sf._node):
            sf._verify__node(node)
    def _verify__node(sf, node, /):
        if not node.is_empty:
            if not all(1 <= node.height-child.height <= 2 for child in node.children): raise HeapError__Validate
            if not any(node.height-child.height == 1 for child in node.children): raise HeapError__Validate
            if not abs(node.lhs_child.height-node.rhs_child.height) <= 1: raise HeapError__Validate
            if node.is_fork:
                if any(sf._lt__node(child, node) for child in node.children): raise HeapError__Validate
                if not any(node.min_payload is child.min_payload for child in node.children): raise HeapError__Validate

    def __bool__(sf, /):
        return not (sf._node.is_empty)
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
        if not sf._reverse is False:
            kwargs.update(reverse=sf._reverse)
        iterable = [*sf]
        args = [iterable] if iterable else []
        return repr_helper(sf, *args, **kwargs)

    def peak(sf, /):
        if not sf:
            raise HeapError__Empty
        return sf._node.min_payload
    def _lt__node(sf, lhs_node, rhs_node, /):
        assert not lhs_node.is_empty
        assert not rhs_node.is_empty
        return sf._lt__payload(lhs_node.min_payload, rhs_node.min_payload)
        #xxx '[_empty_node == +oo] <<== _pushdown_payload_at_root'
        if lhs_node.is_empty:
            return False
        if rhs_node.is_empty:
            return True
        return sf._lt__payload(lhs_node.min_payload, rhs_node.min_payload)
    def _lt__payload(sf, lhs_payload, rhs_payload, /):
        if sf._reverse:
            lhs_payload, rhs_payload = rhs_payload, lhs_payload
        return sf._lt(sf._key_func(lhs_payload), sf._key_func(rhs_payload))
#end-class _MergeableHeap__mixin:




if 0:
    MergeableHeap__immutable_tree = namedtuple('MergeableHeap__immutable_tree', '''
    _key_func
    _lt
    _reverse
    _node
    '''.split()
    )
    #ValueError: Field names cannot start with an underscore: '_key_func'
else:
    MergeableHeap__immutable_tree = namedtuple('MergeableHeap__immutable_tree', '''
    Xkey_func
    Xlt
    Xreverse
    Xnode
    '''.split()
    )


class MergeableHeap__immutable_tree(MergeableHeap__immutable_tree, _MergeableHeap__mixin):
    __slots__ = ()
    def __new__(cls, iterable=None, /, *, key=None, __lt__=None, reverse=False):
        _key_func = echo if key is None else key
        _lt = opss.__lt__ if __lt__ is None else __lt__
        _reverse = bool(reverse)
        #==>> __repr__, eat, _lt__payload

        _node = _empty_node
        sf = super(__class__, cls).__new__(cls, _key_func, _lt, _reverse, _node)
        iterable = '' if iterable is None else iterable
        sf._key_func
        #bug:sf = sf.ipushs(iterable)
        sf, _ = sf.ipushs(iterable)
        sf._key_func
        return sf

    @property
    def _key_func(sf, /):
        return sf.Xkey_func
    @property
    def _lt(sf, /):
        return sf.Xlt
    @property
    def _reverse(sf, /):
        return sf.Xreverse
    @property
    def _node(sf, /):
        return sf.Xnode
    _key_func
    _lt
    _reverse
    _node


    def _return(sf, root, result, /):
        new = sf._mk5new_root(root)
        return new, result
    def _mk5new_root(sf, root, /):
        assert isinstance(root, _MHNodeTypes)
        ot = sf._replace(Xnode=root)
        assert type(sf) is type(ot)
        return ot
    def iclear(sf, /):
        root = _empty_node
        return sf._return(root, None)
    def ipushs(sf, iterable, /):
        root = _pushs(sf, sf._node, iterable)
        return sf._return(root, None)
    def iter_ipops(sf, /):
        while sf:
            sf, min_payload = sf.ipop()
            yield min_payload
        return

    def ipop_then_push(sf, payload, /):
        min_payload, root = _pop_then_push(sf, sf._node, payload)
        return sf._return(root, min_payload)
    def ipush_then_pop(sf, payload, /):
        min_payload, root = _push_then_pop(sf, sf._node, payload)
        return sf._return(root, min_payload)

    def ipop(sf, /):
        min_payload, root = _pop(sf, sf._node)
        return sf._return(root, min_payload)
    def ipush(sf, payload, /):
        root = _push(sf, sf._node, payload)
        return sf._return(root, None)
    def imerge(sf, other_heap, /):
        if not isinstance(other_heap, __class__):raise TypeError
        if not sf._lt is other_heap._lt:raise TypeError
        if not sf._key_func is other_heap._key_func:raise TypeError
        if not sf._reverse is other_heap._reverse:raise TypeError
        root = _eat(sf, sf._node, other_heap._node)
        return sf._return(root, None)
    def __or__(sf, other_heap, /):
        union, _ = sf.imerge(other_heap)
        return union
    def copy(sf, /):
        'O(1)'
        return sf


class MergeableHeap(_MergeableHeap__mixin):
    __slots__ = '_heap'.split()
    def __init__(sf, iterable=None, /, *, key=None, __lt__=None, reverse=False):
        sf._heap = MergeableHeap__immutable_tree(iterable, key=key, __lt__=__lt__, reverse=reverse)
        sf._key_func
    def copy(sf, /):
        'O(1)'
        new = type(sf)()
        new._heap = sf._heap
        return new

    @property
    def _key_func(sf, /):
        return sf._heap._key_func
    @property
    def _lt(sf, /):
        return sf._heap._lt
    @property
    def _reverse(sf, /):
        return sf._heap._reverse
    @property
    def _node(sf, /):
        return sf._heap._node
    _key_func
    _lt
    _reverse
    _node

    def _fwd(sf, f, /, *args, **kwargs):
        sf._heap, result = f(*args, **kwargs)
        return result
    def clear(sf, /):
        return sf._fwd(sf._heap.iclear)
    def pushs(sf, iterable, /):
        return sf._fwd(sf._heap.ipushs, iterable)
    def iter_pops(sf, /):
        while sf:
            yield sf.pop()
        return

    def pop_then_push(sf, payload, /):
        return sf._fwd(sf._heap.ipop_then_push, payload)
    def push_then_pop(sf, payload, /):
        return sf._fwd(sf._heap.ipush_then_pop, payload)
    def pop(sf, /):
        return sf._fwd(sf._heap.ipop)
    def push(sf, payload, /):
        return sf._fwd(sf._heap.ipush, payload)
    def merge(sf, other_heap, /):
        if not isinstance(other_heap, __class__):raise TypeError
        #bug:return sf._fwd(sf._heap.imerge, other_heap)
        return sf._fwd(sf._heap.imerge, other_heap._heap)
    def __or__(sf, other_heap, /):
        new = sf.copy()
        new.merge(other_heap)
        return new
    def eat(sf, other_heap, /):
        'heap.eat(std::move(heap))'
        if sf is other_heap: raise HeapError__EatSelf
        sf.merge(other_heap)
        other_heap.clear()
        return None


def _pop(sf, root, /):
    '-> (min_payload, root)|raise HeapError__Empty'
    L = root.size
    H = root.height
    (min_payload, root) = _pop_(sf, root)
    assert root.size == L-1
    assert H-1 <= root.height <= H
    return (min_payload, root)

def _pop_(sf, root, /):
    (deepest_unit, root) = _pop__deepest_unit(sf, root)
    #bug:min_payload = _pop_then_push(sf, root, removed_unit.payload)
    (min_payload, root) = _push_then_pop(sf, root, deepest_unit.payload)
    return (min_payload, root)
def _pop__deepest_unit(sf, root, /):
    if root.is_empty: raise HeapError__Empty
    ls = [root]
    while not ls[-1].is_unit:
        ls.append(ls[-1].large_child)
    if not ls: raise logic-err
    removed_unit = ls.pop()
    assert removed_unit.height == 1
    if ls:
        #bug:_replace_child(ls[-1], removed_unit, _empty_node)
        removed_fork = ls.pop()
        assert removed_fork.lhs_child.is_unit
        assert removed_fork.rhs_child.is_unit
        another_unit = removed_fork.another_child_of(removed_unit)
        root = _replace_child_and_fresh_nodes(sf, ls, removed_fork, another_unit)
        deepest_unit = removed_unit

    else:
        assert root.is_unit
        deepest_unit = root
        root = _empty_node
    return (deepest_unit, root)

def _push_then_pop(sf, root, payload, /):
    if root.is_empty:
        return payload, root
    assert root.height
    if not sf._lt__payload(root.min_payload, payload):
        return payload, root
    return _pop_then_push(sf, root, payload)

def _pop_then_push(sf, root, payload, /):
    assert root.height > 0
    min_payload = root.min_payload
    ls = [root]
    while not ls[-1].is_unit:
        ls.append(ls[-1].the_min_payload_child)
    min_unit = ls.pop()
    assert min_unit.height == 1
    assert min_unit.payload is min_payload
    new_unit = _MHNodeUnit(payload)
    root = _replace_child_and_fresh_nodes(sf, ls, min_unit, new_unit)

    return min_payload, root





def _mk(sf, payloads, /):
    '-> root'
    ls = [*map(_MHNodeUnit, payloads)]
    L = len(ls)
    while len(ls) > 1:
        #INVARIANT: assert all(0 <= ls[-1].height - node.height <= 1 for node in ls[:-1])
        # let H := ls[0].height
        # [ls[?].height == H]
        # [H <= ls[-1].height <= H+1]
        assert 0 <= ls[-1].height - ls[-2].height <= 1

        #bug:xs = [_MHNode(sf._lt__node, ls[i], ls[i+1]) for i in range(0, len(ls), 2)]
        xs = [_MHNode(sf._lt__node, ls[i], ls[i+1]) for i in range(0, len(ls)-1, 2)]
        # [xs[?].height == H+1]
        # [H+1 <= xs[-1].height <= H+2]
        # [[xs[-1].height == H+2] <-> [[ls[-1].height == H+1][len(ls)%2==0]]]
        if len(ls)&1:
            # !! [[xs[-1].height == H+2] <-> [[ls[-1].height == H+1][len(ls)%2==0]]]
            # !! [len(ls)%2=!=0]
            # [xs[-1].height =!= H+2]
            # [xs[-1].height == H+1]

            #bug:xs.append(ls[-1])
            if ls[-1].height < xs[-1].height:
                # !! [H <= ls[-1].height <= H+1]
                # !! [xs[-1].height == H+1]
                # !! [ls[-1].height < xs[-1].height]
                # [ls[-1].height == H]
                xs[-1] = _MHNode(sf._lt__node, xs[-1], ls[-1])
                # [xs[-1].height == H+2]
                # [xs[?].height == H+1]
            else:
                # !! [H <= ls[-1].height <= H+1]
                # !! [not [ls[-1].height < xs[-1].height]]
                # !! [xs[-1].height == H+1]
                # [ls[-1].height == H+1]
                xs.append(ls[-1])
                # [xs[-1].height == H+1]
                # [xs[?].height == H+1]
            # [H+1 <= xs[-1].height <= H+2]
            # [xs[?].height == H+1]
        # [H+1 <= xs[-1].height <= H+2]
        # [xs[?].height == H+1]
        ls = xs
        # [H+1 <= ls[-1].height <= H+2]
        # [ls[?].height == H+1]
    if not ls:
        root = _empty_node
    else:
        [root] = ls
    assert root.size == L
    return root



def _pushs(sf, root, payloads, /):
    '-> root'
    return _eat(sf, root, _mk(sf, payloads))
def _push(sf, root, payload, /):
    '-> root'
    new_unit = _MHNodeUnit(payload)
    return _eat(sf, root, new_unit)

def _replace_child_and_fresh_nodes(sf, ancestors, old_child, new_child, /):
    for i in reversed(range(len(ancestors))):
        old_parent = ancestors[i]
        new_parent = _replace_child(sf, old_parent, old_child, new_child)
        ancestors[i] = new_parent
        (old_child, new_child) = (old_parent, new_parent)

    root = new_child
    return root

def _replace_child(sf, parent, old_child, new_child, /):
    assert not new_child.is_empty
    lhs_child, rhs_child = parent.children
    if parent.lhs_child is old_child:
        lhs_child = new_child
    elif parent.rhs_child is old_child:
        rhs_child = new_child
    else:
        raise logic-err
    return _MHNode(sf._lt__node, lhs_child, rhs_child)

def _eat(sf, lhs_root, rhs_root, /):
    '-> root #O(logM)算法'
    L = lhs_root.size + rhs_root.size
    H = max(lhs_root.height, rhs_root.height)
    ########
    root = _eat_(sf, lhs_root, rhs_root)
    assert root.size == L
    assert H <= root.height <= H+1
    return root
def _eat_(sf, lhs_root, rhs_root, /):
    (rhs_root, lhs_root) = sorted([rhs_root, lhs_root], key=_get_height4node)

    if rhs_root.is_empty:
        #[rhs_root is lhs_root is _empty_node] is OK
        return lhs_root
    if 0:
        if rhs_root is lhs_root:
            #[rhs_root is lhs_root is not _empty_node] is bug
            raise HeapError__EatSelf

    assert 1 <= rhs_root.height <= lhs_root.height

    ls = [lhs_root]
    while ls[-1].height > rhs_root.height:
        ls.append(ls[-1].small_child)
    removed_subtree = ls.pop()
    assert removed_subtree.height <= rhs_root.height
    assert not ls or 1 <= ls[-1].height - removed_subtree.height <= 2
    assert not ls or 1 <= ls[-1].height - rhs_root.height <= 2
    assert 0 <= rhs_root.height - removed_subtree.height <= 1

    if removed_subtree.is_empty:
        assert removed_subtree.height == 0 < 1 <= rhs_root.height <= lhs_root.height
        assert ls
        assert 1 == rhs_root.height < ls[-1].height == 2
        new_node = rhs_root
    else:
        new_node = _MHNode(sf._lt__node, removed_subtree, rhs_root)
        assert not ls or 0 <= ls[-1].height - new_node.height <= 1
        # small_child ==>> [0 <= ls[-1].another_child<removed_subtree>.height - removed_subtree.height <= 1]
        # [rhs_root.height >= removed_subtree.height] ==>> [new_node.height == rhs_root.height+1 > removed_subtree.height]
        # [rhs_root.height < ls[-1].height] ==>> [new_node.height <= ls[-1].height]
        # [removed_subtree.height < ls[-1].another_child<removed_subtree>.height <= new_node.height <= ls[-1].height]
        #   『==』==>>_fresh_nodes

    root = _replace_child_and_fresh_nodes(sf, ls, removed_subtree, new_node)

    return root


def _unorder_iter_payloads5root(root, /):
    for node in _unorder_iter_nodes5root(root):
        if node.is_unit:
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
            tree = (node.min_payload, *children)
        ls.append(tree)
    [tree] = ls
    return tree

if __name__ == "__main__":
    import doctest
    doctest.testmod()




