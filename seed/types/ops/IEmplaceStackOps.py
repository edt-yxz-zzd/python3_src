#__all__:goto
r'''[[[[[
py -m seed.types.ops.IEmplaceStackOps
py -m nn_ns.app.debug_cmd   seed.types.ops.IEmplaceStackOps

from seed.types.ops.IEmplaceStackOps import IEmplaceStackOps

from seed.types.ops.IEmplaceStackOps import the_emplace_stack_ops4list, the_emplace_stack_ops4HugeStack

from seed.types.ops.IEmplaceStackOps import EmplaceStackOps4list, EmplaceStackOps4HugeStack



e ../../python3_src/seed/types/ops/IEmplaceStackOps.py
[[
$ cd $my_git_py
$ grep istack -i -r  . -a -l
./.git/index
./nn_ns/graph2/stack/IMutableStackOps.py
./nn_ns/graph2/stack/IPseudoImmutableStackOps.py
./nn_ns/graph2/stack/IStackOps.py
./nn_ns/graph2/stack/LeftBiasedListAsStackOps.py
./nn_ns/graph2/stack/NonExistStackOps.py
./nn_ns/graph2/stack/SeqAsStackOps.py
./nn_ns/graph2/stack/convert_PseudoImmutable2MutableStackOps.py
./nn_ns/graph2/stack/def - ops.txt
./nn_ns/graph2/stack/testmod_all.py
./seed/abc/Ops/IOps.py
]]
[[[[

>>> from seed.types.ops.IEmplaceStackOps import IEmplaceStackOps
>>> from seed.types.ops.IEmplaceStackOps import the_emplace_stack_ops4list, the_emplace_stack_ops4HugeStack
>>> from seed.types.ops.IEmplaceStackOps import EmplaceStackOps4list, EmplaceStackOps4HugeStack

#the_emplace_stack_ops4list
>>> the_emplace_stack_ops4list is EmplaceStackOps4list()
True
>>> ops = the_emplace_stack_ops4list

[[[
>>> stack = ops.mk_empty_stack()
>>> stack
[]
>>> ops.is_empty(stack)
True
>>> ops.get_top__tmay(stack)
()
>>> ops.get_top(stack)
Traceback (most recent call last):
    ...
LookupError: get_top@empty_stack
>>> ops.pop__tmay(stack)
()
>>> ops.pop(stack)
Traceback (most recent call last):
    ...
LookupError: pop@empty_stack
>>> ops.push(stack, 999)
>>> ops.push(stack, 777)
>>> stack
[999, 777]
>>> ops.is_empty(stack)
False
>>> ops.get_top__tmay(stack)
(777,)
>>> ops.get_top(stack)
777
>>> ops.pop__tmay(stack)
(777,)
>>> ops.pop(stack)
999
>>> stack
[]
>>> ops.is_empty(stack)
True

]]]


#the_emplace_stack_ops4HugeStack
>>> the_emplace_stack_ops4HugeStack is EmplaceStackOps4HugeStack()
True
>>> ops = the_emplace_stack_ops4HugeStack

以下是从上面复制过来:只有[[999, 777]]不一样
[[[
>>> stack = ops.mk_empty_stack()
>>> stack
[]
>>> ops.is_empty(stack)
True
>>> ops.get_top__tmay(stack)
()
>>> ops.get_top(stack)
Traceback (most recent call last):
    ...
LookupError: get_top@empty_stack
>>> ops.pop__tmay(stack)
()
>>> ops.pop(stack)
Traceback (most recent call last):
    ...
LookupError: pop@empty_stack
>>> ops.push(stack, 999)
>>> ops.push(stack, 777)
>>> stack
[[999, 777]]
>>> ops.is_empty(stack)
False
>>> ops.get_top__tmay(stack)
(777,)
>>> ops.get_top(stack)
777
>>> ops.pop__tmay(stack)
(777,)
>>> ops.pop(stack)
999
>>> stack
[]
>>> ops.is_empty(stack)
True

]]]


测试 单列表满载附近的行为
[[[
>>> ops = the_emplace_stack_ops4HugeStack
>>> class List(list):
...     def __init__(sf, max_sz, /):
...         sf.max_sz = max_sz
...     def append(sf, x, /):
...         if len(sf) < sf.max_sz:
...             list.append(sf, x)
...         else:
...             raise MemoryError

>>> ls = List(3)
>>> stack = [ls]
>>> for i in range(6):
...     ops.push(stack, i)
>>> stack
[[0, 1, 2], [3, 4, 5]]
>>> for i in range(6):
...     ops.pop(stack)
5
4
3
2
1
0

]]]

#'''
r'''
[[[
>>> ls = []
>>> try:
...     while 1:
...         for i in range(2**16):
...             ls.append(i)
...         print_err(len(ls)>>16, len(ls))
... except MemoryError:
...     pass

>>> ops = the_emplace_stack_ops4HugeStack
>>> stack = [ls]
>>> while len(stack)==1:ops.push(stack, 0)
>>> len(stack)
2
>>> stack[-1]
[0]

!!!doctest测试通过！！！
    32bit Android.app.termux
    size_t max ~ 2**31-1
    ls无法增长时大约len(ls)~2**26
$ py -m seed.types.ops.IEmplaceStackOps
1 65536
2 131072
... ...
... ...
1022 66977792
1023 67043328
$
$


]]]
#'''
r'''
[[[
>>> ls = []
>>> for n in range(2**16): ls.extend([0]*2**n)
Traceback (most recent call last):
    ...
MemoryError
>>> L = 2**n
>>> while L:
...     try:
...         ls.extend(range(L))
...     except MemoryError:
...         L >>= 1

halt here:MemoryError exit doctest
    runout memory ==>> python list donot use a whole contiguous memory chunk
    view ../lots/NOTE/Python/list-max-length.txt
    但！从CPython.listobject的源代码看，Python.list确实是 单个C语言数组
        view others/数学/编程/python/CPython-listobj-impl.txt

>>> ops = the_emplace_stack_ops4HugeStack
>>> stack = [ls]
>>> while len(stack)==1:ops.push(stack, 0)
>>> len(stack)
2

]]]
#'''
r'''

]]]]
#]]]]]'''


__all__ = '''
    IEmplaceStackOps
        EmplaceStackOps4list
            the_emplace_stack_ops4list
        EmplaceStackOps4HugeStack
            the_emplace_stack_ops4HugeStack
    '''.split()


#HHHHH
___begin_mark_of_excluded_global_names__0___ = ...
from seed.abc.abc__ver1 import abstractmethod, ABC, override
from seed.abc.IHashable import IHashable
from seed.tiny import check_type_is, check_tmay
from seed.tiny import print_err
___end_mark_of_excluded_global_names__0___ = ...




class IEmplaceStackOps(IHashable):
    'emplace_stack_ops<emplace_stack<X> >'
    __slots__ = ()

    @abstractmethod
    def _mk_empty_stack_(ops, /):
        '-> stack<X>'
    @abstractmethod
    def _is_empty_(ops, stack, /):
        'stack<X> -> bool'
    @abstractmethod
    def _get_top__nonempty_(ops, nonempty_stack, /):
        '-> X'
    @abstractmethod
    def _pop__nonempty_(ops, nonempty_stack, /):
        '-> X'
    @abstractmethod
    def _push_(ops, stack, x, /):
        '-> None'




    # rename ___careless_check___ -> ___sketchy_check___
    #@abstractmethod
    def _sketchy_check_stack_(ops, stack, /):
        '-> None|TypeError'
    #@abstractmethod
    def _sketchy_check_element_(ops, x, /):
        '-> None|TypeError'





    def mk_empty_stack(ops, /):
        '-> stack<X>'
        stack = ops._mk_empty_stack_()
        if not ops.is_empty(stack): raise TypeError
            #ops.sketchy_check_stack(stack)
        return stack
    def is_empty(ops, stack, /):
        'stack<X> -> bool'
        ops.sketchy_check_stack(stack)
        is_empty = ops._is_empty_(stack)
        check_type_is(bool, is_empty)
        return is_empty
    def push(ops, stack, x, /):
        '-> None'
        ops.sketchy_check_stack(stack)
        ops.sketchy_check_element(x)
        ops._push_(stack, x)
        if ops.is_empty(stack): raise TypeError


    def sketchy_check_stack(ops, stack, /):
        '-> None|TypeError'
        ops._sketchy_check_stack_(stack)
    def sketchy_check_element(ops, x, /):
        '-> None|TypeError'
        ops._sketchy_check_element_(x)

    def get_top(ops, stack, /):
        '-> X | raise LookupError'
        if ops.is_empty(stack): raise LookupError('get_top@empty_stack')
        x = ops._get_top__nonempty_(stack)
        ops.sketchy_check_element(x)
        return x
    def pop(ops, stack, /):
        '-> X | raise LookupError'
        if ops.is_empty(stack): raise LookupError('pop@empty_stack')
        x = ops._pop__nonempty_(stack)
        ops.sketchy_check_element(x)
        return x
    def get_top__tmay(ops, stack, /):
        '-> tmay X'
        if ops.is_empty(stack):
            return ()
        x = ops._get_top__nonempty_(stack)
        ops.sketchy_check_element(x)
        return (x,)
    def pop__tmay(ops, stack, /):
        '-> tmay X'
        if ops.is_empty(stack):
            return ()
        x = ops._pop__nonempty_(stack)
        ops.sketchy_check_element(x)
        return (x,)


class IEmplaceStackOps__singleton_ops(IEmplaceStackOps):
    __slots__ = ()

    __cls2sf = {}
    def __new__(cls, /):
        d = __class__.__cls2sf
        while 1:
            try:
                return d[cls]
            except KeyError:
                sf = super(__class__, cls).__new__(cls)
                check_type_is(cls, sf)
                d[cls] = sf



    @override
    def __hash__(ops, /):
        '-> int'
        return id(type(ops))
    @override
    def __eq__(lhs_ops, rhs_ops, /):
        '-> bool'
        return  type(lhs_ops) is type(rhs_ops)

class EmplaceStackOps4list(IEmplaceStackOps__singleton_ops):
    'emplace_stack_ops<list<X> >; emplace_stack<X>===list<X>'
    __slots__ = ()

    @override
    def _sketchy_check_stack_(ops, stack, /):
        '-> None|TypeError'
        check_type_is(list, stack)
    @override
    def _mk_empty_stack_(ops, /):
        '-> stack<X>'
        return []
    @override
    def _is_empty_(ops, stack, /):
        'stack<X> -> bool'
        #bug:return bool(stack)
        return not stack
    @override
    def _get_top__nonempty_(ops, nonempty_stack, /):
        '-> X'
        return nonempty_stack[-1]
    @override
    def _pop__nonempty_(ops, nonempty_stack, /):
        '-> X'
        return nonempty_stack.pop()
    @override
    def _push_(ops, stack, x, /):
        '-> None'
        stack.append(x)


the_emplace_stack_ops4list = EmplaceStackOps4list()


class EmplaceStackOps4HugeStack(IEmplaceStackOps__singleton_ops):
    'emplace_stack_ops<list<nonempty_list<X> > >; emplace_stack<X>===list<nonempty_list<X> >'
    __slots__ = ()

    @override
    def _sketchy_check_stack_(ops, stack, /):
        '-> None|TypeError'
        check_type_is(list, stack)

    @override
    def _mk_empty_stack_(ops, /):
        '-> stack<X>'
        return []
    @override
    def _is_empty_(ops, stack, /):
        'stack<X> -> bool'
        #bug:return bool(stack)
        return not stack
    @override
    def _get_top__nonempty_(ops, nonempty_stack, /):
        '-> X'
        return nonempty_stack[-1][-1]
    @override
    def _pop__nonempty_(ops, nonempty_stack, /):
        '-> X'
        ls = nonempty_stack[-1]
        x = ls.pop()
        if not ls: nonempty_stack.pop()
        return x
    @override
    def _push_(ops, stack, x, /):
        '-> None'
        if not stack:
            stack.append([x])
        else:
            ls = stack[-1]
            try:
                ls.append(x)
            except MemoryError:
                stack.append([x])



the_emplace_stack_ops4HugeStack = EmplaceStackOps4HugeStack()



if __name__ == "__main__":
    import doctest
    doctest.testmod()
