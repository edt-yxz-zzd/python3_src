#__all__:goto
r'''[[[
e ../../python3_src/seed/data_funcs/idc_mngr.py

indices manager
    delete idx; alloc idx/memory
    put idx;    free idx/memory
    idx is resource
doubly_list

seed.data_funcs.idc_mngr
py -m nn_ns.app.debug_cmd   seed.data_funcs.idc_mngr -x
py -m nn_ns.app.doctest_cmd seed.data_funcs.idc_mngr:__doc__
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.data_funcs.idc_mngr:DoublyList4Idc@T    =T

>>> sf = DoublyList4Idc(9, [])
>>> sf
DoublyList4Idc(9, [])
>>> sf.verify()
>>> sf.put(6)
True
>>> sf.verify()
>>> sf
DoublyList4Idc(9, [6])
>>> sf.put(8)
True
>>> sf.verify()
>>> sf
DoublyList4Idc(9, [6, 8])
>>> [*iter(sf)]
[6, 8]
>>> [*reversed(sf)]
[8, 6]
>>> sf.put(8)
False
>>> len(sf)
2
>>> 8 in sf
True
>>> sf.verify()
>>> sf.discard(8)
True
>>> sf.verify()
>>> sf
DoublyList4Idc(9, [6])
>>> 8 in sf
False
>>> sf.discard(8)
False
>>> 6 in sf
True
>>> sf.verify()
>>> sf.remove(6)
>>> sf.verify()
>>> len(sf)
0
>>> 6 in sf
False
>>> sf
DoublyList4Idc(9, [])


######################
######################
######################
######################
######################
######################
######################
######################
######################
>>> sf = DoublyList4Idc(9, [])
>>> sf
DoublyList4Idc(9, [])
>>> sf = DoublyList4Idc(None, [])
>>> sf
DoublyList4Idc(None, [])
>>> sf = DoublyList4Idc(None, [], list_vs_dict=True)
>>> sf
DoublyList4Idc(None, [], list_vs_dict = True)
>>> sf = DoublyList4Idc(9, [], list_vs_dict=True)
Traceback (most recent call last):
    ...
ValueError: irrational: fixed size of dict




######################
######################
>>> sf = DoublyList4Idc(None, [])
>>> sf
DoublyList4Idc(None, [])
>>> sf.verify()
>>> sf.put(3)
True
>>> sf.verify()
>>> sf.put(7)
True
>>> sf.verify()
>>> sf.put(2)
True
>>> sf.verify()
>>> sf.put_or_move_to_end(4)
True
>>> sf.verify()
>>> sf.put(7)
False
>>> sf.verify()
>>> sf
DoublyList4Idc(None, [3, 7, 2, 4])
>>> sf.put_or_move_to_end(7)
False
>>> sf.verify()
>>> sf
DoublyList4Idc(None, [3, 2, 4, 7])
>>> sf.remove(2)
>>> sf.verify()
>>> sf.remove(3)
>>> sf.verify()
>>> sf.remove(4)
>>> sf.verify()
>>> sf.remove(7)
>>> sf.verify()
>>> sf
DoublyList4Idc(None, [])



######################
######################
>>> sf = DoublyList4Idc(None, [], list_vs_dict=True)
>>> sf
DoublyList4Idc(None, [], list_vs_dict = True)
>>> sf.verify()
>>> sf.put(3)
True
>>> sf.verify()
>>> sf.put(7)
True
>>> sf.verify()
>>> sf.put(2)
True
>>> sf.verify()
>>> sf.put_or_move_to_end(4)
True
>>> sf.verify()
>>> sf.put(7)
False
>>> sf.verify()
>>> sf
DoublyList4Idc(None, [3, 7, 2, 4], list_vs_dict = True)
>>> sf.put_or_move_to_end(7)
False
>>> sf.verify()
>>> sf
DoublyList4Idc(None, [3, 2, 4, 7], list_vs_dict = True)
>>> sf.remove(2)
>>> sf.verify()
>>> sf.remove(3)
>>> sf.verify()
>>> sf.remove(4)
>>> sf.verify()
>>> sf.remove(7)
>>> sf.verify()
>>> sf
DoublyList4Idc(None, [], list_vs_dict = True)










######################
######################
>>> sf = DoublyList4Idc(9, [])
>>> sf.puts(range(5))
(5, 5)
>>> sf.puts(range(5))
(5, 0)
>>> sf.puts(range(3,9))
(6, 4)
>>> sf
DoublyList4Idc(9, [0, 1, 2, 3, 4, 5, 6, 7, 8])
>>> sf.pop_all()
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> sf
DoublyList4Idc(9, [])
>>> sf.puts(range(3,9))
(6, 6)
>>> sf
DoublyList4Idc(9, [3, 4, 5, 6, 7, 8])
>>> sf.clear()
>>> sf
DoublyList4Idc(9, [])

>>> sf = DoublyList4Idc(9, [])
>>> sf.first
Traceback (most recent call last):
    ...
IndexError: first
>>> sf.last
Traceback (most recent call last):
    ...
IndexError: last
>>> sf.put(6)
True
>>> sf.first
6
>>> sf.last
6
>>> sf.put(1)
True
>>> sf.first
6
>>> sf.last
1
>>> sf.put(5)
True
>>> sf.first
6
>>> sf.last
5
>>> sf.put(2)
True
>>> sf.first
6
>>> sf.last
2
>>> sf.put(4)
True
>>> sf.first
6
>>> sf.last
4
>>> sf.remove(4)
>>> sf.first
6
>>> sf.last
2
>>> sf.remove(5)
>>> sf.first
6
>>> sf.last
2
>>> sf.remove(6)
>>> sf.first
1
>>> sf.last
2
>>> sf
DoublyList4Idc(9, [1, 2])
>>> sf.put(1)
False
>>> sf.first
1
>>> sf.last
2
>>> sf.move_to_end(1)
>>> sf.first
2
>>> sf.last
1
>>> sf
DoublyList4Idc(9, [2, 1])
>>> sf.remove(2)
>>> sf.first
1
>>> sf.last
1
>>> sf.remove(1)
>>> sf.first
Traceback (most recent call last):
    ...
IndexError: first
>>> sf.last
Traceback (most recent call last):
    ...
IndexError: last
>>> sf
DoublyList4Idc(9, [])


#]]]'''
__all__ = r'''
DoublyList4Idc
'''.split()#'''
__all__
from seed.helper.repr_input import repr_helper
from seed.tiny_.check import check_uint_lt, check_uint, check_type_is

class DoublyList4Idc:
    r'''[[[
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.data_funcs.idc_mngr:DoublyList4Idc@T    =T    +exclude_attrs5listed_in_cls_doc

__repr__
__init__
__len__
__contains__
remove
discard
first
last
clear
pop_all
pop
move_to_end
put_or_move_to_end
puts
put
__iter__
__reversed__
verify

    #]]]'''#'''
    def __repr__(sf, /):
        fwd = sf._fwd
        may_max1 = _get_may_max1(sf)
        if sf._ls_vs_d_:
            kwds = dict(list_vs_dict=True)
        else:
            kwds = {}
        return repr_helper(sf, may_max1, [*sf], **kwds)
    def __init__(sf, may_max1, idc, /, *, list_vs_dict=False):
        sf._ls_vs_d_ = list_vs_dict
        check_type_is(bool, list_vs_dict)
        sf._dynamic_resize_ = may_max1 is None
        if sf._dynamic_resize_:
            max1 = 0
        else:
            max1 = may_max1
            check_uint(max1)
        max1

        if (not sf._dynamic_resize_) and sf._ls_vs_d_: raise ValueError('irrational: fixed size of dict')
        if sf._ls_vs_d_:
            assert sf._dynamic_resize_
            assert max1 == 0
            fwd = {}
            bwd = {}
        else:
            fwd = [None]*max1
            bwd = [None]*max1
        sf._fwd = fwd
        sf._bwd = bwd
        sf._may_j0 = None
        sf._sz = 0
        sf.puts(idc)
        return
    def __len__(sf, /):
        return sf._sz
    def __contains__(sf, j, /):
        fwd = sf._fwd
        max1 = len(fwd)
        if sf._dynamic_resize_:
            check_uint(j)
            if sf._ls_vs_d_:
                return j in fwd
            if not j < max1:
                return False
        else:
            check_uint_lt(max1, j)
        assert not sf._ls_vs_d_
        return not fwd[j] is None

    def remove(sf, j, /):
        '-> None'
        if not sf.discard(j):
            raise IndexError(j)
    def discard(sf, j, /):
        '-> actually_remove/existed/bool'
        if not j in sf:
            #non-existed
            #not remove
            return False
        fwd = sf._fwd
        bwd = sf._bwd
        if len(sf) == 1:
            sf._may_j0 = None
        else:
            j0 = sf._may_j0
            if j0 == j:
                j1 = fwd[j0]
                sf._may_j0 = j0 = j1
            next_j = fwd[j]
            prev_j = bwd[j]
            fwd[prev_j] = next_j
            bwd[next_j] = prev_j
        #erase:
        if sf._ls_vs_d_:
            del fwd[j]
            del bwd[j]
            assert sf._dynamic_resize_
        else:
            fwd[j] = None
            bwd[j] = None
            if sf._dynamic_resize_:
                while fwd and fwd[-1] is None:
                    fwd.pop()
                    bwd.pop()
        sf._sz -= 1
        return True
    @property
    def first(sf, /):
        if not sf:
            raise IndexError('first')
        (j0, last_j) = _get__j0__last_j(sf)
        return j0
    @property
    def last(sf, /):
        if not sf:
            raise IndexError('last')
        (j0, last_j) = _get__j0__last_j(sf)
        return last_j
    def clear(sf, /):
        while sf:
            sf.pop()
    def pop_all(sf, /):
        idc = [*sf]
        sf.clear()
        return idc
    def pop(sf, /):
        '-> idx/uint'
        if not sf:
            raise IndexError('pop empty')
        (j0, last_j) = _get__j0__last_j(sf)
        sf.remove(last_j)
        return last_j
    def move_to_end(sf, j, /):
        '-> None'
        sf.remove(j)
        sf.put(j)
    def put_or_move_to_end(sf, j, /):
        '-> actually_put/non_existed/bool'
        r = sf.put(j)
        if not r:
            sf.move_to_end(j)
        return r
    def puts(sf, idc, /):
        '-> (total, num_actually_put)/(uint,uint)'
        sz0 = len(sf)
        put = sf.put
        total = 0
        for total, j in enumerate(idc, 1):
            put(j)
        num_actually_put = len(sf) -sz0
        return (total, num_actually_put)
    def put(sf, j, /):
        '-> actually_put/non_existed/bool'
        if j in sf:
            #already-existed
            #not put
            return False
        fwd = sf._fwd
        bwd = sf._bwd
        if sf._dynamic_resize_ and not sf._ls_vs_d_:
            if not j < len(fwd):
                ns = [None]*(j+1 -len(fwd))
                fwd += ns
                bwd += ns
                assert j+1 == len(fwd)
        if not sf:
            sf._may_j0 = j0 = j
            fwd[j] = j
            bwd[j] = j
        else:
            #(j0, last_j) = _get__j0__last_j(sf)
            j0 = sf._may_j0
            ##########
            # last_j -> j0
            last_j = bwd[j0]
            ##########
            # last_j -> j -> j0
            fwd[last_j] = j
            fwd[j] = j0
            ##########
            # last_j <- j <- j0
            bwd[j0] = j
            bwd[j] = last_j
            ##########
        sf._sz += 1
        return True
    def __iter__(sf, /):
        if not sf:
            return
        j0 = sf._may_j0
        fwd = sf._fwd
        j = j0
        while 1:
            yield j
            j = fwd[j]
            if j == j0:break
    def __reversed__(sf, /):
        if not sf:
            return
        j0 = sf._may_j0
        bwd = sf._bwd
        j = j0
        while 1:
            j = bwd[j]
            yield j
            if j == j0:break
    def verify(sf, /):
        sz = len(sf)
        fwd = sf._fwd
        bwd = sf._bwd
        assert (not sz) is (sf._may_j0 is None)
        assert len(fwd) == len(bwd)
        js = [*iter(sf)]
        ks = [*reversed(sf)]
        assert len(js) == sz
        assert len(ks) == sz
        assert js == ks[::-1]
            #链表元素 一致
        if sf._ls_vs_d_:
            assert len(js) == len(fwd)
                #缓存无空位
            assert sf._dynamic_resize_
        else:
            max1 = len(fwd)
            assert fwd.count(None) == max1 -sz
            assert bwd.count(None) == max1 -sz
                #缓存空位 一致
            if sf._dynamic_resize_:
                assert not fwd or fwd[-1] is not None
                    #缓存末尾非空位
        return
def _get_j0(sf, j, /):
    if not sf:
        return j
    return sf._may_j0
def _get__j0__last_j(sf, /):
    j0 = sf._may_j0
    last_j = sf._bwd[j0]
        #last_j <-- j0
    return j0, last_j
def _get_may_max1(sf, /):
    return (may_max1 := None if sf._dynamic_resize_ else len(sf._fwd))

__all__



from seed.data_funcs.idc_mngr import DoublyList4Idc
from seed.data_funcs.idc_mngr import *
