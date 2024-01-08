#__all__:goto
r'''[[[
e ../../python3_src/seed/types/linked_list.py


[linked-list =[def]= (singly-linked-list | doubly-linked-list)]


seed.types.linked_list
py -m nn_ns.app.debug_cmd   seed.types.linked_list -x
py -m nn_ns.app.doctest_cmd seed.types.linked_list:__doc__ -ff -v
py_adhoc_call   seed.types.linked_list   @f


#class__DoublyLinkedList:goto
#class__DoublyLinkedList__methods:goto
>>> from seed.types.linked_list import DoublyLinkedList

#############
    validate_
    __del__
    __repr__
    __init__
>>> DoublyLinkedList()
DoublyLinkedList()
>>> DoublyLinkedList([1])
DoublyLinkedList([1])
>>> DoublyLinkedList([1, 2])
DoublyLinkedList([1, 2])
>>> DoublyLinkedList([1, 2, 3])
DoublyLinkedList([1, 2, 3])
>>> DoublyLinkedList([]).validate_()
>>> DoublyLinkedList([1]).validate_()
>>> DoublyLinkedList([1, 2]).validate_()
>>> DoublyLinkedList([1, 2, 3]).validate_() #see below for failure example

#############
    clear
    _clear_
    headend_xnode
    head_and_end_xnode_pair
    _head
    _end
    __bool__
    __len__
    count_size_via_enumerate_
    __iter__
    __reversed__
    sf__mk_empty
>>> dlnkls = DoublyLinkedList([1, 2, 3])
>>> he = dlnkls.headend_xnode
>>> dlnkls.head_and_end_xnode_pair == (he, he)
True
>>> dlnkls.sf__mk_empty()
DoublyLinkedList()
>>> dlnkls
DoublyLinkedList([1, 2, 3])
>>> [*iter(dlnkls)]
[1, 2, 3]
>>> [*reversed(dlnkls)]
[3, 2, 1]
>>> bool(dlnkls)
True
>>> dlnkls.count_size_via_enumerate_()
3
>>> dlnkls.clear()
>>> dlnkls
DoublyLinkedList()
>>> dlnkls.sf__mk_empty()
DoublyLinkedList()
>>> bool(dlnkls)
False
>>> dlnkls.count_size_via_enumerate_()
0
>>> len(dlnkls) #__len__#=None|NotImplemented
Traceback (most recent call last):
    ...
TypeError: 'NoneType' object is not callable

TypeError: 'NotImplementedType' object is not callable

>>> dlnkls.headend_xnode is he
True
>>> dlnkls.head_and_end_xnode_pair == (he, he)
True

#############
    split_out_nodes_between_
>>> dlnkls = DoublyLinkedList([1, 2, 3])
>>> dlnkls.split_out_nodes_between_(None, None)
DoublyLinkedList([1, 2, 3])
>>> dlnkls
DoublyLinkedList()
>>> dlnkls.validate_() #ok!

#############
    explain_may_range_bounds_
    index_node_via_enumerate_
    index_node_via_enumerate_between_
    iter_nodes_between_
    iter_nodes_
    iter_payloads_
    iter_payloads_between_
>>> dlnkls = DoublyLinkedList([0, 1, 2])
>>> node0 = dlnkls.index_node_via_enumerate_(0)
>>> node1 = dlnkls.index_node_via_enumerate_(1)
>>> node2 = dlnkls.index_node_via_enumerate_(2)

>>> node0 is dlnkls.index_node_via_enumerate_(-3)
True
>>> node0 is dlnkls.index_node_via_enumerate_(2, reverse=True)
True

>>> node1 is dlnkls.index_node_via_enumerate_(-2)
True
>>> node1 is dlnkls.index_node_via_enumerate_(1, reverse=True)
True

>>> node2 is dlnkls.index_node_via_enumerate_(-1)
True
>>> node2 is dlnkls.index_node_via_enumerate_(0, reverse=True)
True


>>> node1 is dlnkls.index_node_via_enumerate_between_(node0, node2, 0)
True
>>> node1 is dlnkls.index_node_via_enumerate_between_(node0, node2, 0, reverse=True)
True
>>> node1 is dlnkls.index_node_via_enumerate_between_(node0, node2, -1)
True
>>> node1 is dlnkls.index_node_via_enumerate_between_(node0, node2, -1, reverse=True)
True

>>> node1 is dlnkls.index_node_via_enumerate_between_(None, node2, 1)
True
>>> node1 is dlnkls.index_node_via_enumerate_between_(None, node2, 0, reverse=True)
True
>>> node1 is dlnkls.index_node_via_enumerate_between_(None, node2, -1)
True
>>> node1 is dlnkls.index_node_via_enumerate_between_(None, node2, -2, reverse=True)
True

>>> node1 is dlnkls.index_node_via_enumerate_between_(node0, None, 0)
True
>>> node1 is dlnkls.index_node_via_enumerate_between_(node0, None, 1, reverse=True)
True
>>> node1 is dlnkls.index_node_via_enumerate_between_(node0, None, -2)
True
>>> node1 is dlnkls.index_node_via_enumerate_between_(node0, None, -1, reverse=True)
True


>>> he = dlnkls.headend_xnode
>>> dlnkls.explain_may_range_bounds_(None, None) == (he, he)
True
>>> dlnkls.explain_may_range_bounds_(node0, None) == (node0, he)
True
>>> dlnkls.explain_may_range_bounds_(None, node2) == (he, node2)
True
>>> dlnkls.explain_may_range_bounds_(node0, node2) == (node0, node2)
True

>>> [*dlnkls.iter_nodes_between_(node0, node2)] == [node1]
True
>>> [*dlnkls.iter_nodes_between_(node0, None)] == [node1, node2]
True
>>> [*dlnkls.iter_nodes_between_(node0, None, reverse=True)] == [node2, node1]
True
>>> [*dlnkls.iter_nodes_between_(None, node2)] == [node0, node1]
True
>>> [*dlnkls.iter_nodes_between_(None, node2, reverse=True)] == [node1, node0]
True

>>> [*dlnkls.iter_nodes_()] == [node0, node1, node2]
True
>>> [*dlnkls.iter_nodes_(reverse=True)] == [node2, node1, node0]
True

>>> [*dlnkls.iter_payloads_()]
[0, 1, 2]
>>> [*dlnkls.iter_payloads_(reverse=True)]
[2, 1, 0]

>>> [*dlnkls.iter_payloads_between_(None, node2)]
[0, 1]
>>> [*dlnkls.iter_payloads_between_(None, node2, reverse=True)]
[1, 0]

>>> [*dlnkls.iter_payloads_between_(node0, None)]
[1, 2]
>>> [*dlnkls.iter_payloads_between_(node0, None, reverse=True)]
[2, 1]

#############
    extend
    extend_left__reversed_
    extend__
    extend_near_
    append
    append_left
    append__
>>> dlnkls = DoublyLinkedList([0, 1, 2])
>>> dlnkls
DoublyLinkedList([0, 1, 2])
>>> dlnkls.append_left(-1) is dlnkls.index_node_via_enumerate_(0)
True
>>> dlnkls
DoublyLinkedList([-1, 0, 1, 2])
>>> dlnkls.validate_() #ok!

>>> dlnkls = DoublyLinkedList([0, 1, 2])
>>> dlnkls.append(3) is dlnkls.index_node_via_enumerate_(-1)
True
>>> dlnkls
DoublyLinkedList([0, 1, 2, 3])
>>> dlnkls.validate_() #ok!
>>> dlnkls.append(-1, left_vs_right=False) is dlnkls.index_node_via_enumerate_(0)
True
>>> dlnkls
DoublyLinkedList([-1, 0, 1, 2, 3])
>>> dlnkls.validate_() #ok!




>>> dlnkls = DoublyLinkedList([0, 1, 2])
>>> dlnkls.extend_left__reversed_([3, 4])
>>> dlnkls
DoublyLinkedList([4, 3, 0, 1, 2])
>>> dlnkls.validate_() #ok!

>>> dlnkls = DoublyLinkedList([0, 1, 2])
>>> dlnkls.extend([3, 4], reverse=True, left_vs_right=False)
>>> dlnkls
DoublyLinkedList([4, 3, 0, 1, 2])
>>> dlnkls.validate_() #ok!

>>> dlnkls = DoublyLinkedList([0, 1, 2])
>>> dlnkls.extend([3, 4], reverse=True)
>>> dlnkls
DoublyLinkedList([0, 1, 2, 4, 3])
>>> dlnkls.validate_() #ok!

>>> dlnkls = DoublyLinkedList([0, 1, 2])
>>> dlnkls.extend([3, 4], left_vs_right=False)
>>> dlnkls
DoublyLinkedList([3, 4, 0, 1, 2])
>>> dlnkls.validate_() #ok!

>>> dlnkls = DoublyLinkedList([0, 1, 2])
>>> dlnkls.extend([3, 4])
>>> dlnkls
DoublyLinkedList([0, 1, 2, 3, 4])
>>> dlnkls.validate_() #ok!


>>> dlnkls = DoublyLinkedList([0, 1, 2])
>>> node1 = dlnkls.index_node_via_enumerate_(1)
>>> dlnkls.extend_near_(node1, [3, 4], reverse=False, before_vs_after=False)
>>> dlnkls
DoublyLinkedList([0, 3, 4, 1, 2])
>>> dlnkls.validate_() #ok!

>>> dlnkls = DoublyLinkedList([0, 1, 2])
>>> node1 = dlnkls.index_node_via_enumerate_(1)
>>> dlnkls.extend_near_(node1, [3, 4], reverse=False, before_vs_after=True)
>>> dlnkls
DoublyLinkedList([0, 1, 3, 4, 2])
>>> dlnkls.validate_() #ok!

>>> dlnkls = DoublyLinkedList([0, 1, 2])
>>> node1 = dlnkls.index_node_via_enumerate_(1)
>>> dlnkls.extend_near_(node1, [3, 4], reverse=True, before_vs_after=True)
>>> dlnkls
DoublyLinkedList([0, 1, 4, 3, 2])
>>> dlnkls.validate_() #ok!

>>> dlnkls = DoublyLinkedList([0, 1, 2])
>>> node1 = dlnkls.index_node_via_enumerate_(1)
>>> dlnkls.extend_near_(node1, [3, 4], reverse=True, before_vs_after=False)
>>> dlnkls
DoublyLinkedList([0, 4, 3, 1, 2])
>>> dlnkls.validate_() #ok!


#############
    pop_near_
    pop__
    pop
    pop_left
    pop_payload__drop_node_
    pop_payloads_
    pop_payloads__drop_nodes_between_
    iter_pop_payloads_
    iter_pop_payloads__drop_nodes_between_
>>> dlnkls = DoublyLinkedList([0, 1, 2])
>>> dlnkls.pop()
2
>>> dlnkls
DoublyLinkedList([0, 1])
>>> dlnkls.validate_() #ok!

>>> dlnkls = DoublyLinkedList([0, 1, 2])
>>> dlnkls.pop(left_vs_right=False)
0
>>> dlnkls
DoublyLinkedList([1, 2])
>>> dlnkls.validate_() #ok!

>>> dlnkls = DoublyLinkedList([0, 1, 2])
>>> dlnkls.pop_left()
0
>>> dlnkls
DoublyLinkedList([1, 2])
>>> dlnkls.validate_() #ok!


>>> dlnkls = DoublyLinkedList([0, 1, 2, 3, 4])
>>> node2 = dlnkls.index_node_via_enumerate_(2)
>>> dlnkls.pop_near_(node2, before_vs_after=False)
1
>>> dlnkls
DoublyLinkedList([0, 2, 3, 4])
>>> dlnkls.validate_() #ok!

>>> dlnkls = DoublyLinkedList([0, 1, 2, 3, 4])
>>> node2 = dlnkls.index_node_via_enumerate_(2)
>>> dlnkls.pop_near_(node2, before_vs_after=True)
3
>>> dlnkls
DoublyLinkedList([0, 1, 2, 4])
>>> dlnkls.validate_() #ok!
>>> dlnkls.pop_payload__drop_node_(node2)
2
>>> dlnkls
DoublyLinkedList([0, 1, 4])
>>> dlnkls.validate_() #ok!
>>> dlnkls.pop_payloads_()
[0, 1, 4]
>>> dlnkls
DoublyLinkedList()
>>> dlnkls.validate_() #ok!

>>> dlnkls = DoublyLinkedList([0, 1, 2, 3, 4])
>>> dlnkls.pop_payloads_(reverse=True)
[4, 3, 2, 1, 0]
>>> dlnkls
DoublyLinkedList()
>>> dlnkls.validate_() #ok!


>>> dlnkls = DoublyLinkedList([0, 1, 2, 3, 4])
>>> node0 = dlnkls.index_node_via_enumerate_(0)
>>> node4 = dlnkls.index_node_via_enumerate_(3)
>>> dlnkls.pop_payloads__drop_nodes_between_(node0, node4)
[1, 2]
>>> dlnkls
DoublyLinkedList([0, 3, 4])
>>> dlnkls.validate_() #ok!

>>> dlnkls = DoublyLinkedList([0, 1, 2, 3, 4])
>>> node0 = dlnkls.index_node_via_enumerate_(0)
>>> node4 = dlnkls.index_node_via_enumerate_(3)
>>> dlnkls.pop_payloads__drop_nodes_between_(node0, node4, reverse=True)
[2, 1]
>>> dlnkls
DoublyLinkedList([0, 3, 4])
>>> dlnkls.validate_() #ok!

#############
    insert_payload_near_
    insert_payload_before_
    insert_payload_after_
    explain_may_anchor_
    move__no_overlaps__before_
    move__no_overlaps__after_
    move__no_overlaps_
    swap__no_overlaps_
>>> dlnkls = DoublyLinkedList([0, 1, 2, 3, 4])
>>> node2 = dlnkls.index_node_via_enumerate_(2)
>>> node3 = dlnkls.index_node_via_enumerate_(3)
>>> node4 = dlnkls.index_node_via_enumerate_(4)
>>> node0 = dlnkls.index_node_via_enumerate_(0)
>>> node1 = dlnkls.index_node_via_enumerate_(1)

>>> dlnkls.explain_may_anchor_(node2, before_vs_after=True) == (node2, node3)
True
>>> dlnkls.explain_may_anchor_(node2, before_vs_after=False) == (node1, node2)
True

>>> he = dlnkls.headend_xnode
>>> dlnkls.explain_may_anchor_(None, before_vs_after=True) == (he, node0)
True
>>> dlnkls.explain_may_anchor_(None, before_vs_after=False) == (node4, he)
True

>>> dlnkls
DoublyLinkedList([0, 1, 2, 3, 4])
>>> dlnkls.move__no_overlaps_(node1, dlnkls, node1, node4, before_vs_after=False) == (node0, node1)
True
>>> dlnkls
DoublyLinkedList([0, 2, 3, 1, 4])
>>> dlnkls.validate_() #ok!


>>> dlnkls = DoublyLinkedList([0, 1, 2, 3, 4])
>>> nodes = [*dlnkls.iter_nodes_()]
>>> dlnkls.validate_() #ok!
>>> dlnkls.move__no_overlaps_(nodes[1], dlnkls, nodes[1], nodes[4], before_vs_after=True) == (nodes[1], nodes[2]) #!!!broken precondition!!!
True
>>> dlnkls #dead-loop   #doctest: +SKIP
    !!!dead if not SKIP!!!
>>> dlnkls # now detect "rho" kind broken
Traceback (most recent call last):
    ...
seed.types.linked_list.ValidateFail__broken_doubly_linked
>>> dlnkls.validate_() #fire!
Traceback (most recent call last):
    ...
seed.types.linked_list.ValidateFail__broken_doubly_linked
>>> he = dlnkls.headend_xnode
>>> nodes_ = [*nodes, he]
>>> [nodes_.index(node.prev_node) for node in nodes_]
[5, 0, 3, 2, 1, 4]
>>> [nodes_.index(node.next_node) for node in nodes_]
[1, 2, 3, 2, 5, 0]

==>>:
    start--> 4 -> he -> 0 -> 1 -> loop[2 -> 3 -> 2]
    [0 <- 1 <- 4 <- he <- 0]loop <--start
    [2 <- 3 <- 2]loop <--start
Exception ignored in: <function DoublyLinkedList.__del__ at 0x75986b1ab0>
Traceback (most recent call last):
    sf._clear_()
    for _ in sf.iter_pop_payloads_():pass
    yield sf.pop_payload__drop_node_(begin4sf)
    _connect_nodes_(node.prev_node, node.next_node)
    next_node.prev_node = node
AttributeError: 'NoneType' object has no attribute 'prev_node'

>>> _nodes = [he, *nodes]
>>> for prev, curr in zip(_nodes, nodes_):
...     curr.prev_node = prev
...     prev.next_node = curr
>>> dlnkls.validate_() #ok!


>>> dlnkls = DoublyLinkedList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> nodes = [*dlnkls.iter_nodes_()]
>>> dlnkls.swap__no_overlaps_(nodes[1], nodes[5], dlnkls, nodes[6], nodes[9])
>>> dlnkls
DoublyLinkedList([0, 1, 7, 8, 5, 6, 2, 3, 4, 9])
>>> dlnkls.validate_() #ok!

>>> dlnkls = DoublyLinkedList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> nodes = [*dlnkls.iter_nodes_()]
>>> dlnkls.swap__no_overlaps_(nodes[1], nodes[5], dlnkls, nodes[5], nodes[9])
>>> dlnkls
DoublyLinkedList([0, 1, 6, 7, 8, 5, 2, 3, 4, 9])
>>> dlnkls.validate_() #ok!






#]]]'''
__all__ = r'''
DoublyLinkedList


DoublyLinkedList_XNode
DoublyLinkedList_Node



Error
    Error__pop_headend
    Error__pop_empty
    Error__bad_range__include_headend_xnode
    Error__bad_range__head4rng_end4rng_not_in_same_circle
    ValidateFail__broken_doubly_linked

'''.split()#'''
__all__


from seed.tiny import ifNone, check_type_is, null_tuple
from seed.helper.repr_input import repr_helper

r'''[[[
class IDoublyLinkedList_BaseNode:
    __slots__ = ()
    def get_tmay_payload(sf, /):
        '-> tmay payload'
        raise NotImplementedError
    def is_end_node(sf, /):
        '-> [not$ contains payload]'
        raise NotImplementedError
        return not sf.get_tmay_payload()
    def get_may_prev_node(sf, /):
        '-> tmay payload'
        raise NotImplementedError
    ######################
    ######################
    def is_head_node(sf, /):
        '-> [not$ contains payload]'
        return sf.get_may_prev_node() is None
    def has_payload(sf, /):
        '-> [contains payload]'
        return not sf.is_end_node()

class DoublyLinkedList_EndNode(IDoublyLinkedList_BaseNode):
    __slots__ = ('may_prev_node',)
    def __init__(sf, may_prev_node, /):
        sf.may_prev_node = may_prev_node
    def get_tmay_payload(sf, /):
        '-> tmay payload'
        return null_tuple
    def is_end_node(sf, /):
        '-> [not$ contains payload]'
        return True
    def get_may_prev_node(sf, /):
        '-> tmay payload'
        return sf.may_prev_node
class DoublyLinkedList_Node(IDoublyLinkedList_BaseNode):
    __slots__ = ('payload', 'may_prev_node', 'may_next_node')
    #__slots__ = ('payload', 'prev_node', 'next_node')
    #__slots__ = ('__weakref__', 'payload', 'prev_node_wref', 'next_node')
    def __init__(sf, payload=None, may_prev_node, may_next_node=None, /):
        sf.payload = payload
        sf.may_prev_node = may_prev_node
        sf.may_next_node = may_next_node
    def get_tmay_payload(sf, /):
        '-> tmay payload'
        return (sf.payload,)
    def is_end_node(sf, /):
        '-> [not$ contains payload]'
        return False
    def get_may_prev_node(sf, /):
        '-> tmay payload'
        return sf.may_prev_node
#]]]'''#'''

__all__


class Error(Exception):pass
class Error__pop_headend(Error):pass
class Error__pop_empty(Error):pass
class Error__bad_range__include_headend_xnode(Error):pass
class Error__bad_range__head4rng_end4rng_not_in_same_circle(Error):pass
class ValidateFail__broken_doubly_linked(Error):pass

class _DoublyLinkedList_BaseNode:
    #__slots__ = ('prev_node', 'next_node')
    __slots__ = ()
    def bad_clear(sf, /):
        sf.prev_node = None
        sf.next_node = None
    def get_(sf, /, *, before_vs_after):
        if before_vs_after is False:
            #before
            node = sf.prev_node
        elif before_vs_after is True:
            #after
            node = sf.next_node
        else:
            raise 000
        if node is None: raise 000
        return node
class DoublyLinkedList_XNode(_DoublyLinkedList_BaseNode):
    __slots__ = ('prev_node', 'next_node')
    def __init__(sf, /):
        sf.prev_node = sf
        sf.next_node = sf
class DoublyLinkedList_Node(_DoublyLinkedList_BaseNode):
    __slots__ = ('payload', 'prev_node', 'next_node')
        # [head_xnode === end_xnode]
        # [head_xnode has no payload]
    def __init__(sf, payload=None, prev_node=None, next_node=None, /, *, to_fix_neighbors=False):
        sf.payload = payload
        sf.prev_node = ifNone(prev_node, sf)
        sf.next_node = ifNone(next_node, sf)
        if to_fix_neighbors:
            #_connect_nodes_
            sf.prev_node.next_node = sf
            sf.next_node.prev_node = sf
#class__DoublyLinkedList:here
class DoublyLinkedList:
    r'''[[[
    doubly-linked-list

range using open-interval instead of half-open-interval
    (head4sf, end4sf) instead of (begin4sf, end4sf)

    [head4sf===rend4sf]
    [head4sf.next_node===begin4sf===(end4sf|first4sf)]
    [end4sf.prev_node===rbegin4sf===(head4sf|last4sf)]
    ######################
    [MAYBE:[head4sf is end4sf]]
    ######################
    [head4sf is end4sf]:
        * [head4sf is sf.headend_xnode]:
            ok, repr whole range
        * [not$ head4sf is sf.headend_xnode]:
            err! Error__bad_range__include_headend_xnode

naming:
    + xxx__ vs xxx:
        #extend__ vs extend
        #append__ vs append
        #pop__ vs pop
        #
        API kwds: nodefaults vs set defaults

    + xxx__ vs xxx_near_:
        #extend__ vs extend_near_
        #pop__ vs pop_near_
        #append__ vs N/A
        #N/A vs insert_payload_near_
        #
        API (args,kwds) using: left_vs_right vs (may_anchor4sf, before_vs_after)


[[[
__len__#=None|NotImplemented
===
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.types.linked_list:DoublyLinkedList    =DoublyLinkedList
===
validate_
__del__
clear
_clear_
__repr__
__init__
headend_xnode
head_and_end_xnode_pair
_head
_end
__bool__
__len__#=None|NotImplemented
count_size_via_enumerate_
__iter__
__reversed__
sf__mk_empty
split_out_nodes_between_
explain_may_range_bounds_
index_node_via_enumerate_
index_node_via_enumerate_between_
iter_nodes_between_
iter_nodes_
iter_payloads_
iter_payloads_between_
extend
extend_left__reversed_
extend__
extend_near_
append
append_left
append__
pop_near_
pop__
pop
pop_left
pop_payload__drop_node_
pop_payloads_
pop_payloads__drop_nodes_between_
iter_pop_payloads_
iter_pop_payloads__drop_nodes_between_
insert_payload_near_
insert_payload_before_
insert_payload_after_
explain_may_anchor_
move__no_overlaps__before_
move__no_overlaps__after_
move__no_overlaps_
swap__no_overlaps_
===
]]]

__len__#=None|NotImplemented
#class__DoublyLinkedList__methods:here
no node&&payload:
    validate_
    __del__
    clear
    _clear_
    __bool__
    count_size_via_enumerate_
    sf__mk_empty
    __repr__

both node&&payload:
    iter_payloads_between_
    pop_payload__drop_node_
    pop_payloads__drop_nodes_between_
    iter_pop_payloads__drop_nodes_between_
    insert_payload_near_
    insert_payload_before_
    insert_payload_after_

node:
    headend_xnode
    head_and_end_xnode_pair
    _head
    _end
    split_out_nodes_between_
    explain_may_range_bounds_
    index_node_via_enumerate_
    index_node_via_enumerate_between_
    iter_nodes_between_
    iter_nodes_
    explain_may_anchor_
    move__no_overlaps__before_
    move__no_overlaps__after_
    move__no_overlaps_
    swap__no_overlaps_
payload:
    __init__
    __iter__
    __reversed__
    iter_payloads_
    extend
    extend_left__reversed_
    extend__
    extend_near_
    append
    append_left
    append__
    pop_near_
    pop__
    pop
    pop_left
    pop_payloads_
    iter_pop_payloads_



    #]]]'''#'''
    def validate_(sf, /):
        he = sf.headend_xnode
        check_type_is(DoublyLinkedList_XNode, he)
        prev_node = he
        for curr_node in sf.iter_nodes_():
            check_type_is(DoublyLinkedList_Node, curr_node)
            _check_node_connect_(prev_node, curr_node, reverse=False)
            prev_node = curr_node
        else:
            curr_node = he
            _check_node_connect_(prev_node, curr_node, reverse=False)
        return
    def __del__(sf, /):
        sf._clear_()
            #kill cycle ref
        sf.headend_xnode.bad_clear()
            #kill cycle ref
        sf._he = None
    def clear(sf, /):
        sf._clear_()
    def _clear_(sf, /):
        for _ in sf.iter_pop_payloads_():pass
        return
        ######################
        while sf:
            sf.pop()
        return
        ######################
        if not sf:
            return
        for node in sf.iter_nodes_():
            #node.bad_clear()
                #bug: 『node.bad_clear()』broken sf.iter_nodes_()
            node.prev_node = None
                # doubly --> singly
        _connect_nodes_(sf._head, sf._end)
            #drop ref to singly
        return
        ######################

    def __repr__(sf, /):
        if sf:
            payloads = [*sf]
            args = (payloads,)
        else:
            args = null_tuple
        return repr_helper(sf, *args)
    def __init__(sf, iterable=None, /):
        #sf._head = sf._end = DoublyLinkedList_Node(None)
        sf._he = DoublyLinkedList_XNode()
        #sf._sz = 0
            #no "__len__()" <<== to manipulate linked list nodes directly instead of just payload
        if not iterable is None:
            sf.extend(iterable)
    @property
    def headend_xnode(sf, /):
        return sf._he
    @property
    def head_and_end_xnode_pair(sf, /):
        node = sf._he
        return (node, node)
    _head = _end = headend_xnode
    def __bool__(sf, /):
        head_xnode = sf._head
        return not head_xnode.next_node is head_xnode
    #no:def __len__(sf, /):
    __len__ = NotImplemented
    __len__ = None

    def count_size_via_enumerate_(sf, /):
        'O(N)'
        sz = 0
        for sz, _ in enumerate(sf.iter_nodes_(), 1): pass
        return sz
    def __iter__(sf, /):
        return sf.iter_payloads_()
    def __reversed__(sf, /):
        return sf.iter_payloads_(reverse=True)

    def sf__mk_empty(sf, /):
        cls = type(sf)
        ot = cls()
        return ot
    def split_out_nodes_between_(sf, may_head4sf, may_end4sf, /):
        '-> DoublyLinkedList'
        (head4sf, end4sf) = sf.explain_may_range_bounds_(may_head4sf, may_end4sf)
        ot = sf.sf__mk_empty()
        ot.move__no_overlaps__before_(None, sf, head4sf, end4sf)
        return ot
    def explain_may_range_bounds_(sf, may_head4sf, may_end4sf, /):
        he = sf.headend_xnode
        head4sf = ifNone(may_head4sf, he)
        end4sf = ifNone(may_end4sf, he)
        if head4sf is end4sf is not he: raise Error__bad_range__include_headend_xnode
        return (head4sf, end4sf)
    def index_node_via_enumerate_(sf, idx, /, *, reverse=False):
        '-> node #O(N)#see:index_node_via_enumerate_between_'
        return sf.index_node_via_enumerate_between_(None, None, idx, reverse=reverse)
    def index_node_via_enumerate_between_(sf, may_head4sf, may_end4sf, idx, /, *, reverse=False):
        '-> node #O(N)#see:count_size_via_enumerate_'
        check_type_is(int, idx)
        check_type_is(bool, reverse)
        if idx < 0:
            reverse = not reverse
            idx = -idx -1
        # [idx >= 0]
        it = sf.iter_nodes_between_(may_head4sf, may_end4sf, reverse=reverse)
        i = -1
        for i, node in enumerate(it):
            if i == idx:
                break
        else:
            sz = i+1
            raise IndexError((idx, sz))
        return node
    #def iter_nodes_with_end_xnode_
    def iter_nodes_between_(sf, may_head4sf, may_end4sf, /, *, reverse=False):
        'see:iter_nodes_'
        #see:iter_pop_payloads__drop_nodes_between_
        (head4sf, end4sf) = sf.explain_may_range_bounds_(may_head4sf, may_end4sf)
        T = DoublyLinkedList_Node #not DoublyLinkedList_XNode
        X = DoublyLinkedList_XNode
        ######################
        check_type_is(bool, reverse)
        (head4sf, end4sf) = _reorder_(head4sf, end4sf, reverse=reverse)
        before_vs_after = not reverse
            #direction to move
        ######################
        #as-if [not reverse][before_vs_after is True/after]:
        prev_node = head4sf
        #while not (curr_node := prev_node.next_node) is end4sf:
        while not (curr_node := prev_node.get_(before_vs_after=before_vs_after)) is end4sf:
            #_check_node_connect_(prev_node, curr_node, reverse=reverse)
            #if not curr_node.prev_node is prev_node: raise ValidateFail__broken_doubly_linked
            if not curr_node.get_(before_vs_after=not before_vs_after) is prev_node: raise ValidateFail__broken_doubly_linked
                # exclude: "rho"
                # remains: infinite line or cycle
                # !! [memory finite]
                # [nodes finite]
                # ==>> cycle
                # ==>> 『while loop』hit headend_xnode or (end4sf if end4sf on cycle else head4sf)
            if curr_node is head4sf: raise Error__bad_range__head4rng_end4rng_not_in_same_circle
            if type(curr_node) is X: raise Error__bad_range__include_headend_xnode
            check_type_is(T, curr_node)
                #prevent headend_xnode@bad-range
                #???or: ^ Error__bad_range__include_headend_xnode
            ######################
            yield curr_node
            ######################
            #next_round:
            prev_node = curr_node
            ######################
        return

    def iter_nodes_(sf, /, *, reverse=False):
        return sf.iter_nodes_between_(None, None, reverse=reverse)
    def iter_payloads_(sf, /, *, reverse=False):
        return sf.iter_payloads_between_(None, None, reverse=reverse)
    def iter_payloads_between_(sf, may_head4sf, may_end4sf, /, *, reverse=False):
        'see:iter_payloads_/__iter__/__reversed__'
        return _iter_payloads5nodes_(sf.iter_nodes_between_(may_head4sf, may_end4sf, reverse=reverse))

    def extend(sf, iterable, /, *, reverse=False, left_vs_right=True):
        'left_vs_right~append_left/append_right, reverse~iterable'
        sf.extend__(iterable, reverse=reverse, left_vs_right=left_vs_right)
    def extend_left__reversed_(sf, reversed_iterable, /):
        sf.extend__(reversed_iterable, reverse=True, left_vs_right=False)
    def extend__(sf, iterable, /, *, reverse, left_vs_right):
        check_type_is(bool, left_vs_right)
        sf.extend_near_(None, iterable, reverse=reverse, before_vs_after=not left_vs_right)
    def extend_near_(sf, may_anchor4sf, iterable, /, *, reverse, before_vs_after):
        'before_vs_after~may_anchor4sf, reverse~iterable'
        check_type_is(bool, reverse)
        check_type_is(bool, before_vs_after)
        (head4sf, end4sf) = sf.explain_may_anchor_(may_anchor4sf, before_vs_after=before_vs_after)
        if not reverse:
            #before
            anchor_node = end4sf
        else:
            #after
            anchor_node = head4sf
        anchor_node
        for payload in iterable:
            new_node = sf.insert_payload_near_(anchor_node, payload, before_vs_after=reverse)
                #anchor_node keep the same
    def append(sf, payload, /, *, left_vs_right=True):
        return sf.append__(payload, left_vs_right=left_vs_right)
    def append_left(sf, payload, /):
        return sf.append__(payload, left_vs_right=False)
    def append__(sf, payload, /, *, left_vs_right):
        check_type_is(bool, left_vs_right)
        new_node = sf.insert_payload_near_(None, payload, before_vs_after=not left_vs_right)
        return new_node

    def pop_near_(sf, may_anchor4sf, /, *, before_vs_after):
        '-> payload'
        (head4sf, end4sf) = sf.explain_may_anchor_(may_anchor4sf, before_vs_after=before_vs_after)
        node = head4sf if before_vs_after is False else end4sf
            #anchor4sf = head4sf if before_vs_after is True else end4sf
        payload = sf.pop_payload__drop_node_(node)
            #^Error__pop_empty
        return payload
    def pop__(sf, /, *, left_vs_right):
        '-> payload'
        check_type_is(bool, left_vs_right)
        return sf.pop_near_(None, before_vs_after=not left_vs_right)
            #^Error__pop_empty
    def pop(sf, /, *, left_vs_right=True):
        '-> payload'
        return sf.pop__(left_vs_right=left_vs_right)
            #^Error__pop_empty

        #node = sf._end.prev_node
    def pop_left(sf, /):
        '-> payload'
        #node = sf._head.next_node
        return sf.pop__(left_vs_right=False)
            #^Error__pop_empty
    def pop_payload__drop_node_(sf, node, /):
        '-> payload'
        if node is sf._head:
            if not sf:
                raise Error__pop_empty
            raise Error__pop_headend
        if node.prev_node is node or node.next_node is node: raise 000

        payload = node.payload
        _connect_nodes_(node.prev_node, node.next_node)
        node.bad_clear()
        return payload
    def pop_payloads_(sf, /, *, reverse=False):
        return [*sf.iter_pop_payloads_(reverse=reverse)]
    def pop_payloads__drop_nodes_between_(sf, may_head4sf, may_end4sf, /, *, reverse=False):
        return [*sf.iter_pop_payloads__drop_nodes_between_(may_head4sf, may_end4sf, reverse=reverse)]
    def iter_pop_payloads_(sf, /, *, reverse=False):
        '-> Iter<payload>'
        return sf.iter_pop_payloads__drop_nodes_between_(None, None, reverse=reverse)
    def iter_pop_payloads__drop_nodes_between_(sf, may_head4sf, may_end4sf, /, *, reverse=False):
        '-> Iter<payload>'
        #see:iter_nodes_between_
        it = sf.iter_nodes_between_(may_head4sf, may_end4sf, reverse=reverse)
        for curr_node in it:
            break
        else:
            return
        # cannot pop curr_node now otherwise broken sf.iter_nodes_between_
        for next_node in it:
            # now sf.iter_nodes_between_ holds next_node, we can pop curr_node
            yield sf.pop_payload__drop_node_(curr_node)
            ######################
            #next_round:
            curr_node = next_node
            ######################
        else:
            yield sf.pop_payload__drop_node_(curr_node)
        return

        ######################
        # old-version:vivi iter_nodes_between_
        #   but keep read head4sf.next_node
        # terminology:using terms: (head4sf, begin4sf?first4sf?end4sf) instead of (prev_node, curr_node?end4sf)
        # iter_nodes_between_ do 『prev_node := curr_node』
        #   but iter_pop_payloads__drop_nodes_between_ keep head4sf unchanged
        #
        ######################
        # if not reverse:
            # [begin4sf is first4sf]
            # [head4sf keep the same, begin4sf is changing]
        # if reverse:
            # [rbegin4sf is last4sf]
            # [end4sf keep the same, rbegin4sf is changing]
        ######################
        return


    def insert_payload_near_(sf, may_anchor4sf, payload, /, *, before_vs_after):
        '-> new_node'
        (head4sf, end4sf) = sf.explain_may_anchor_(may_anchor4sf, before_vs_after=before_vs_after)
        new_node = DoublyLinkedList_Node(payload, head4sf, end4sf, to_fix_neighbors=True)
        #sf._sz += 1
        return new_node
    def insert_payload_before_(sf, may_anchor4sf, payload, /):
        '-> new_node'
        return sf.insert_payload_near_(may_anchor4sf, payload, before_vs_after=False)
    def insert_payload_after_(sf, may_anchor4sf, payload, /):
        '-> new_node'
        return sf.insert_payload_near_(may_anchor4sf, payload, before_vs_after=True)
    def explain_may_anchor_(sf, may_anchor4sf, /, *, before_vs_after):
        he = sf.headend_xnode
        anchor4sf = ifNone(may_anchor4sf, he)
            #anchor_node
        if before_vs_after is False:
            #before
            head4sf = anchor4sf.prev_node
            end4sf = anchor4sf
        elif before_vs_after is True:
            #after
            head4sf = anchor4sf
            end4sf = anchor4sf.next_node
        else:
            raise 000
        return (head4sf, end4sf)
    def move__no_overlaps__before_(sf, may_anchor4sf, ot, may_head4ot, may_end4ot, /):
        'see:move__no_overlaps_'
        return sf.move__no_overlaps_(may_anchor4sf, ot, may_head4ot, may_end4ot, before_vs_after=False)
    def move__no_overlaps__after_(sf, may_anchor4sf, ot, may_head4ot, may_end4ot, /):
        'see:move__no_overlaps_'
        return sf.move__no_overlaps_(may_anchor4sf, ot, may_head4ot, may_end4ot, before_vs_after=True)
    def move__no_overlaps_(sf, may_anchor4sf, ot, may_head4ot, may_end4ot, /, *, before_vs_after):
        '-> (head4sf, end4sf) #move nodes to sf from ot #precondition:[not$ overlaps]'
        # broken precondition: [overlaps] => [1 circle --> multi-circles]
        #
        (head4sf, end4sf) = sf.explain_may_anchor_(may_anchor4sf, before_vs_after=before_vs_after)
        (head4ot, end4ot) = ot.explain_may_range_bounds_(may_head4ot, may_end4ot)

        begin4ot = head4ot.next_node
        if begin4ot is end4ot:
            # [ot range is empty]
            return (head4sf, end4sf)
        # [ot range is not empty]
        first4ot = begin4ot
        last4ot = end4ot.prev_node
        ######################
        # [not$ first4ot is end4ot]
        # [not$ last4ot is head4ot]
        # [{} == {first4ot,last4ot} /-\ {head4ot,end4ot}]
        ######################
        # [MAYBE:[first4ot is last4ot]]
        # [MAYBE:[head4ot is end4ot]]
        # [MAYBE:[head4sf is end4sf]]

        ######################change 6 links between:
        head4ot, first4ot
        last4ot, end4ot
        head4sf, end4sf
        ######################connect 3 pairs:
        head4ot, end4ot
        head4sf, first4ot
        last4ot, end4sf
        ######################
        _connect_nodes_(head4ot, end4ot)
        _connect_nodes_(head4sf, first4ot)
        _connect_nodes_(last4ot, end4sf)
        ######################
        return (head4sf, end4sf)
    def swap__no_overlaps_(sf, may_head4sf, may_end4sf, ot, may_head4ot, may_end4ot, /):
        '-> None #precondition:[not$ overlaps]'
        (head4sf, end4sf) = sf.explain_may_range_bounds_(may_head4sf, may_end4sf)
        (head4ot, end4ot) = ot.explain_may_range_bounds_(may_head4ot, may_end4ot)

        begin4sf = head4sf.next_node
        sf.move__no_overlaps__after_(head4sf, ot, head4ot, end4ot)
        new_head4sf = begin4sf.prev_node
        ot.move__no_overlaps__before_(end4ot, sf, new_head4sf, end4sf)
        return



def _check_node_connect_(prev_node, curr_node, /, *, reverse):
    (prev_node, curr_node) = _reorder_(prev_node, curr_node, reverse=reverse)
    if not prev_node.next_node is curr_node: raise ValidateFail__broken_doubly_linked
    if not curr_node.prev_node is prev_node: raise ValidateFail__broken_doubly_linked
def _connect_nodes_(node, next_node, /):
    node.next_node = next_node
    next_node.prev_node = node
def _iter_payloads5nodes_(nodes, /):
    for node in nodes:
        yield node.payload
#def _reorder_(head4sf, end4sf, /, *, reverse)
def _reorder_(*args, reverse):
    if reverse:
        args = args[::-1]
    return args

def __():
    from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
    from seed.helper.repr_input import repr_helper
    class _(ABC):
        __slots__ = ()
        raise NotImplementedError
        ___no_slots_ok___ = True
if __name__ == "__main__":
    pass
__all__


#class__DoublyLinkedList__methods:goto
from seed.types.linked_list import DoublyLinkedList
from seed.types.linked_list import DoublyLinkedList_Node
from seed.types.linked_list import DoublyLinkedList_XNode
from seed.types.linked_list import *
