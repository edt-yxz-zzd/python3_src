#__all__:goto
r'''[[[
e ../../python3_src/seed/types/StackStyleSet.py
see:
    from seed.data_funcs.rngs import StackStyleSimpleIntSet, StackStyleSimpleIntMapping
        [key :: int]
        bisearch in sorted rngs
    view ../../python3_src/seed/types/OrderedSet.py
        [Ord key]
        based on immutable-red-black-tree
    view ../../python3_src/seed/types/StackStyleSet.py
        [key :: Hashable]
        based on py.dict,py.list

seed.types.StackStyleSet
py -m nn_ns.app.debug_cmd   seed.types.StackStyleSet
py -m nn_ns.app.adhoc_argparser__main__call8module   seed.types.StackStyleSet   @f
py -m nn_ns.app.doctest_cmd seed.types.StackStyleSet:__doc__ -v

from seed.types.StackStyleSet import StackStyleSet, MultiSetStyleStack

py_help seed.types.StackStyleSet@StackStyleSet
py_help seed.types.StackStyleSet@MultiSetStyleStack


>>> from seed.types.StackStyleSet import StackStyleSet, MultiSetStyleStack


################################
################################
################################
################################
################################

>>> StackStyleSet()
StackStyleSet()
>>> StackStyleSet([0,3,2,1,3])
StackStyleSet([0, 3, 2, 1])
>>> s = StackStyleSet()
>>> s.add(4)
>>> s.add(3)
>>> s.add(5)
>>> s.add(4)
>>> s.add(3)
>>> s
StackStyleSet([4, 3, 5])
>>> len(s)
3
>>> bool(s)
True
>>> [*s]
[4, 3, 5]
>>> [*reversed(s)]
[5, 3, 4]
>>> 4 in s
True
>>> 1 in s
False
>>> s == StackStyleSet([4, 3, 5])
True
>>> s == StackStyleSet()
False

>>> s.pop()
5
>>> s.pop()
3
>>> s.pop()
4
>>> s
StackStyleSet()
>>> len(s)
0
>>> bool(s)
False
>>> [*s]
[]
>>> 4 in s
False
>>> 1 in s
False
>>> s == StackStyleSet([4, 3, 5])
False
>>> s == StackStyleSet()
True


>>> s
StackStyleSet()
>>> s.discard(3)
>>> s.remove(3)
Traceback (most recent call last):
    ...
KeyError: 3
>>> s.add(3)
>>> s.remove(3)
>>> s
StackStyleSet()

>>> s = StackStyleSet([4, 3, 5])
>>> s[0]
4
>>> s[1]
3
>>> s[2]
5
>>> s.idx2key(0)
4
>>> s.idx2key(1)
3
>>> s.idx2key(2)
5
>>> s.key2idx(4)
0
>>> s.key2idx(3)
1
>>> s.key2idx(5)
2



#using set.cmp not consider stack seq.cmp
>>> StackStyleSet([4, 3, 5]) < StackStyleSet([4, 3, 5])
False
>>> StackStyleSet([4, 3, 5]) <= StackStyleSet([4, 3, 5])
True
>>> StackStyleSet([4, 3]) < StackStyleSet([4, 3, 5])
True
>>> StackStyleSet([4, 3]) <= StackStyleSet([4, 3, 5])
True
>>> StackStyleSet([4, 6]) <= StackStyleSet([4, 3, 5])
False
>>> StackStyleSet([4, 6]) < StackStyleSet([4, 3, 5])
False
>>> StackStyleSet([4, 6]) > StackStyleSet([4, 3, 5])
False
>>> StackStyleSet([4, 6]) >= StackStyleSet([4, 3, 5])
False


#using set.eq not consider stack order
>>> StackStyleSet([4, 6]) == StackStyleSet([6, 4])
True


>>> StackStyleSet([4, 6, 9]) & StackStyleSet([6, 4, 7])
StackStyleSet([6, 4])
>>> StackStyleSet([4, 6, 9]) | StackStyleSet([6, 4, 7])
StackStyleSet([4, 6, 9, 7])
>>> StackStyleSet([4, 6, 9]) ^ StackStyleSet([6, 4, 7])
StackStyleSet([9, 7])
>>> StackStyleSet([4, 6, 9]) - StackStyleSet([6, 4, 7])
StackStyleSet([9])





################################
################################
################################
################################
################################

>>> f = 10000 .__add__
>>> class MultiSetStyleStack(MultiSetStyleStack):
...     def _val2key_(sf, v):
...         return f(v)
>>> MultiSetStyleStack()
MultiSetStyleStack()
>>> MultiSetStyleStack([0,3,2,1,3])
MultiSetStyleStack([0, 3, 2, 1, 3])
>>> s = MultiSetStyleStack()
>>> s.push(4)
>>> s.add(3)
>>> s.append(5)
>>> s.push(4)
>>> s.add(3)
>>> s
MultiSetStyleStack([4, 3, 5, 4, 3])
>>> len(s)
5
>>> bool(s)
True
>>> [*s]
[4, 3, 5, 4, 3]
>>> [*reversed(s)]
[3, 4, 5, 3, 4]
>>> [*s.iter_ordered_uniqued_keys_(reverse=False)]
[10004, 10003, 10005]
>>> [*s.iter_ordered_uniqued_keys_(reverse=True)]
[10005, 10003, 10004]
>>> f(4) in s
True
>>> f(1) in s
False
>>> s == MultiSetStyleStack([4, 3, 5, 4, 3])
True
>>> s == MultiSetStyleStack()
False

>>> s.pop()
3
>>> s.pop()
4
>>> s.pop()
5
>>> s
MultiSetStyleStack([4, 3])
>>> [*s.iter_ordered_uniqued_keys_(reverse=False)]
[10004, 10003]
>>> [*s.iter_ordered_uniqued_keys_(reverse=True)]
[10003, 10004]
>>> s.pop()
3
>>> s.pop()
4
>>> s
MultiSetStyleStack()
>>> len(s)
0
>>> bool(s)
False
>>> [*s]
[]
>>> [*s.iter_ordered_uniqued_keys_(reverse=False)]
[]
>>> [*s.iter_ordered_uniqued_keys_(reverse=True)]
[]
>>> f(4) in s
False
>>> f(1) in s
False
>>> s == MultiSetStyleStack([4, 3, 5])
False
>>> s == MultiSetStyleStack()
True





>>> s = MultiSetStyleStack([4, 3, 5])
>>> s[0]
4
>>> s[1]
3
>>> s[2]
5
>>> s.idx2val(0)
4
>>> s.idx2val(1)
3
>>> s.idx2val(2)
5
>>> s.idx2key(0)
10004
>>> s.idx2key(1)
10003
>>> s.idx2key(2)
10005
>>> s.key2last_idx(10004)
0
>>> s.key2last_idx(10003)
1
>>> s.key2last_idx(10005)
2
>>> [*s.key2may_idc_view(f(4))]
[0]
>>> [*s.key2may_idc_view(f(3))]
[1]
>>> s.key2idc_copy(f(5))
[2]
>>> s.key2may_idc_view(f(-1))
>>> s.key2idc_copy(f(-1))
[]

>>> MultiSetStyleStack([4, 6]) <= MultiSetStyleStack([4, 3, 5])
Traceback (most recent call last):
    ...
TypeError: '<=' not supported between instances of 'MultiSetStyleStack' and 'MultiSetStyleStack'
>>> MultiSetStyleStack([4, 6]) < MultiSetStyleStack([4, 3, 5])
Traceback (most recent call last):
    ...
TypeError: '<' not supported between instances of 'MultiSetStyleStack' and 'MultiSetStyleStack'
>>> MultiSetStyleStack([4, 6]) > MultiSetStyleStack([4, 3, 5])
Traceback (most recent call last):
    ...
TypeError: '>' not supported between instances of 'MultiSetStyleStack' and 'MultiSetStyleStack'
>>> MultiSetStyleStack([4, 6]) >= MultiSetStyleStack([4, 3, 5])
Traceback (most recent call last):
    ...
TypeError: '>=' not supported between instances of 'MultiSetStyleStack' and 'MultiSetStyleStack'


#using ordered stack.eq not unordered set.eq
>>> MultiSetStyleStack([4, 6]) == MultiSetStyleStack([6, 4])
False
>>> MultiSetStyleStack([6, 4]) == MultiSetStyleStack([6, 4])
True
>>> MultiSetStyleStack([4, 6]) != MultiSetStyleStack([6, 4])
True
>>> MultiSetStyleStack([6, 4]) != MultiSetStyleStack([6, 4])
False


>>> MultiSetStyleStack([4, 6, 9]) & MultiSetStyleStack([6, 4, 7])
Traceback (most recent call last):
    ...
TypeError: unsupported operand type(s) for &: 'MultiSetStyleStack' and 'MultiSetStyleStack'
>>> MultiSetStyleStack([4, 6, 9]) | MultiSetStyleStack([6, 4, 7])
Traceback (most recent call last):
    ...
TypeError: unsupported operand type(s) for |: 'MultiSetStyleStack' and 'MultiSetStyleStack'
>>> MultiSetStyleStack([4, 6, 9]) ^ MultiSetStyleStack([6, 4, 7])
Traceback (most recent call last):
    ...
TypeError: unsupported operand type(s) for ^: 'MultiSetStyleStack' and 'MultiSetStyleStack'
>>> MultiSetStyleStack([4, 6, 9]) - MultiSetStyleStack([6, 4, 7])
Traceback (most recent call last):
    ...
TypeError: unsupported operand type(s) for -: 'MultiSetStyleStack' and 'MultiSetStyleStack'





#]]]'''
__all__ = r'''
    StackStyleSet
    MultiSetStyleStack
'''.split()#'''
__all__


from collections.abc import MutableSet, Set, Sequence
from seed.helper.repr_input import repr_helper
from seed.tiny import check_type_is
from seed.types.view.View import SeqView#, SetView, MapView


class StackStyleSet(MutableSet):
    'add/pop'
    #__slots__ = ()
    def _val2key_(sf, v, /):
        k = v
        return k
    def __init__(sf, iterable=None, /):
        sf._vs = []
            # [v]
        #sf._s = {*[]}
            # {k}
        sf._d = {}
            # {k:idx}
        if not iterable is None:
            sf.update(iterable)
    def __repr__(sf, /):
        if not sf:
            return repr_helper(sf)
        return repr_helper(sf, sf._vs)
    def update(sf, vs, /):
        for _ in map(sf.add, vs):pass
    def clear(sf, /):
        sf._d.clear()
        sf._vs.clear()
    def __bool__(sf, /):
        return bool(sf._vs)
    def __len__(sf, /):
        return len(sf._vs)
    def __contains__(sf, k, /):
        return k in sf._d
    def __iter__(sf, /):
        return iter(sf._vs)
    def __reversed__(sf, /):
        return reversed(sf._vs)
    def add(sf, v, /):
        k = sf._val2key_(v)
        d = sf._d
        if not k in d:
            #s.add(k)
            d[k] = idx = len(sf)
            sf._vs.append(v)
    def pop(sf, /):
        v = sf._vs.pop()
        k = sf._val2key_(v)
        #sf._s.remove(k)
        del sf._d[k]
        return v
    def idx2key(sf, i, /):
        check_type_is(int, i)
        v = sf.idx2val(i)
        k = sf._val2key_(v)
        return k
    def idx2val(sf, i, /):
        v = sf._vs[i]
        return v
    def key2idx(sf, k, /):
        return sf._d[k]
    def index(sf, k, /):
        try:
            return sf.key2idx(k)
        except KeyError:
            raise ValueError(k)

    def __getitem__(sf, i, /):
        return sf.idx2val(i)
    def remove(sf, k, /):
        if not len(sf)-1 == sf.key2idx(k): raise KeyError(k)
        v = sf.pop()
    def discard(sf, k, /):
        if not k in sf: return
        sf.remove(k)
StackStyleSet()



r'''
class MultiSetStyleStack(Sequence, Set):
class MultiSetStyleStack(Sequence, MutableSet):
#weird... set.op
MultiSetStyleStack([4, 6, 9]) - MultiSetStyleStack([6, 4, 7])
Expected:
    MultiSetStyleStack([9])
Got:
    MultiSetStyleStack([4, 6, 9])
#'''
class MultiSetStyleStack(Sequence):
    'push/pop'
    #__slots__ = ()
    def _val2key_(sf, v, /):
        k = v
        return k
    def __init__(sf, iterable=None, /):
        sf._vs = []
            # [v]
        #sf._s = {*[]}
        sf._d = {}
            # {k:[idx]}
        sf._ks = []
            # [k]
        if not iterable is None:
            sf.update(iterable)
    def __repr__(sf, /):
        if not sf:
            return repr_helper(sf)
        return repr_helper(sf, sf._vs)
    def update(sf, vs, /):
        for _ in map(sf.push, vs):pass
    def clear(sf, /):
        sf._vs.clear()
        sf._d.clear()
        sf._ks.clear()
    def __bool__(sf, /):
        return bool(sf._vs)
    def __len__(sf, /):
        return len(sf._vs)
    def __contains__(sf, k, /):
        return k in sf._d
    def __reversed__(sf, /):
        '-> Iter v'
        return reversed(sf._vs)
    def __iter__(sf, /):
        '-> Iter v'
        return iter(sf._vs)
    def iter_ordered_uniqued_keys_(sf, /, *, reverse):
        '-> Iter k'
        #==>> required: ++new-attr:sf._ks::[k]
        f = reversed if reverse else iter
        return f(sf._ks)
    def iter_ordered_vals_(sf, /, *, reverse):
        '-> Iter v'
        f = reversed if reverse else iter
        return f(sf._vs)
    #def view_key_set(sf, /): return sf._d.keys()
    def add(sf, v, /):
        sf.push(v)
    def append(sf, v, /):
        sf.push(v)
    def push(sf, v, /):
        k = sf._val2key_(v)
        idc = sf._d.setdefault(k, [])
        idx = len(sf)
        sf._vs.append(v)
        if not idc:
            sf._ks.append(k)
        idc.append(idx)
    def pop(sf, /):
        v = sf._vs.pop()
        k = sf._val2key_(v)
        idc = sf._d[k]
        idc.pop()
        if not idc:
            del sf._d[k]
            k_ = sf._ks.pop()
        return v
    if 0:
        def discard(sf, k, /):
            raise TypeError("unsupported operand .discard")
        discard = None
    def idx2key(sf, i, /):
        check_type_is(int, i)
        v = sf.idx2val(i)
        k = sf._val2key_(v)
        return k
    def idx2val(sf, i, /):
        v = sf._vs[i]
        return v
    def key2last_idx(sf, k, /):
        return sf._d[k][-1]
    def key2idc_copy(sf, k, /):
        return [*sf._d.get(k, '')]
    def key2may_idc_view(sf, k, /):
        may_idc = sf._d.get(k)
        if may_idc is None:
            may_idc_view = None
        else:
            idc = may_idc
            idc_view = SeqView(idc)
            may_idc_view = idc_view
        return may_idc_view

    def __getitem__(sf, i, /):
        return sf.idx2val(i)
    def __eq__(sf, ot, /):
        if type(ot) is not type(sf):return NotImplemented
        return (sf._vs == ot._vs)
MultiSetStyleStack()




from seed.types.StackStyleSet import StackStyleSet, MultiSetStyleStack

