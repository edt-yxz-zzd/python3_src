#__all__:goto
r'''[[[
e ../../python3_src/seed/int_tools/bijections4int.py

seed.int_tools.bijections4int
py -m nn_ns.app.debug_cmd   seed.int_tools.bijections4int -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.int_tools.bijections4int:__doc__ -ht # -ff -df

py -m nn_ns.app.doctest_cmd seed.int_tools.bijections4int:_doctest1 -ht # -ff -df
py -m nn_ns.app.doctest_cmd seed.int_tools.bijections4int:_doctest2 -ht # -ff -df
py -m nn_ns.app.doctest_cmd seed.int_tools.bijections4int:_doctest3 -ht # -ff -df
py -m nn_ns.app.doctest_cmd seed.int_tools.bijections4int:_doctest4 -ht # -ff -df

[[
[sint =[def]= int]
[imay =[def]= int{>=-1}]
[uint =[def]= int{>=0}]
[pint =[def]= int{>=1}]
[uints :: [uint]]
[uints1 :: [uint]{len>=1}]
[uint_tree :: (uint|tuple{uint_tree})]
]]



>>> uint2uints_(66666669999999)
(13, 10, 0, 1, 0, 120, 0, 6, 124)
>>> uint5uints_(_)
66666669999999

>>> uint2uint_tree_(66666669999999, validate=True)
(0, 0, 1, 3, 10, 0, 0, 0, ((0,),), ((0,), (), 0), 0)
>>> uint5uint_tree_(_, validate=True)
66666669999999

>>> check_uint_tree_(uint2uint_tree_(66666669999999))











py_adhoc_call   seed.int_tools.bijections4int   @f
]]]'''#'''
_doctest1 = r'''[[[
>>> def _test1(N, /):
...     for u in range(N):
...         us = uint2uints_(u)
...         v = uint5uints_(us)
...         assert u == v
...         yield (u, us)
>>> pairs = [*_test1(3**5)]
>>> for t in pairs[:20]:t
(0, ())
(1, (0,))
(2, (1,))
(3, (2,))
(4, (0, 0))
(5, (3,))
(6, (4,))
(7, (1, 0))
(8, (5,))
(9, (6,))
(10, (2, 0))
(11, (0, 1))
(12, (0, 2))
(13, (0, 0, 0))
(14, (7,))
(15, (8,))
(16, (3, 0))
(17, (9,))
(18, (10,))
(19, (4, 0))


#]]]'''#'''
_doctest2 = r'''[[[

>>> from itertools import product
>>> def _test2(L, N, /):
...     for sz in range(L):
...       for us in product(range(N), repeat=sz):
...         assert len(us) == sz
...         u = uint5uints_(us)
...         vs = uint2uints_(u)
...         assert us == vs
...         yield (us, u)
>>> pairs = [*_test2(5, 8)]
>>> for t in pairs[:20]:t
((), 0)
((0,), 1)
((1,), 2)
((2,), 3)
((3,), 5)
((4,), 6)
((5,), 8)
((6,), 9)
((7,), 14)
((0, 0), 4)
((0, 1), 11)
((0, 2), 12)
((0, 3), 32)
((0, 4), 33)
((0, 5), 35)
((0, 6), 36)
((0, 7), 95)
((1, 0), 7)
((1, 1), 20)
((1, 2), 21)




#]]]'''#'''
_doctest3 = r'''[[[

>>> def _test3(N, /):
...     for u in range(N):
...         utr = uint2uint_tree_(u)
...         v = uint5uint_tree_(utr)
...         assert u == v
...         yield (u, utr)
>>> pairs = [*_test3(26)]
>>> for t in pairs[:20]:t
(0, 0)
(1, ())
(2, 1)
(3, (0,))
(4, 2)
(5, ((),))
(6, 3)
(7, (1,))
(8, 4)
(9, (0, 0))
(10, 5)
(11, ((0,),))
(12, 6)
(13, (2,))
(14, 7)
(15, ((), 0))
(16, 8)
(17, (((),),))
(18, 9)
(19, (3,))
>>> pairs = [*_test3(2**16)]




#]]]'''#'''
_doctest4 = r'''[[[
>>> def _test4(utrs, /):
...     for utr in utrs:
...         u = uint5uint_tree_(utr)
...         _utr = uint2uint_tree_(u)
...         assert utr == _utr
...         yield (utr, u)
>>> pairs = [*_test4(range(50))]
>>> for t in pairs[:20]:t
(0, 0)
(1, 2)
(2, 4)
(3, 6)
(4, 8)
(5, 10)
(6, 12)
(7, 14)
(8, 16)
(9, 18)
(10, 20)
(11, 22)
(12, 24)
(13, 26)
(14, 28)
(15, 30)
(16, 32)
(17, 34)
(18, 36)
(19, 38)
>>> utrs = [(), (0,), (0, 7), (5, 0), (3, 4, 1, 0, 2), ((),), ((), ()), (((),),), (((3,9,8,12,0,1, ()),), 4, 0, ((),))]
>>> pairs = [*_test4(utrs)]
>>> for t in pairs[:20]:t
((), 1)
((0,), 3)
((0, 7), 217)
((5, 0), 111)
((3, 4, 1, 0, 2), 1085305)
(((),), 5)
(((), ()), 41)
((((),),), 17)
((((3, 9, 8, 12, 0, 1, ()),), 4, 0, ((),)), 4294107699598732869912611601395)






#]]]'''#'''
__all__ = r'''

uint2sint_
uint5sint_

uint2pint_
uint5pint_

uint2imay_
uint5imay_

uint2uints_
uint5uints_

uint2uints1_
uint5uints1_

imay2pints_
imay5pints_

uint2pints1_
uint5pints1_

uint2uint_tree_
uint5uint_tree_
check_uint_tree_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.tiny_.check import check_type_is, check_int_ge
from seed.tiny import mk_tuple, null_tuple, ifNone, echo
from seed.int_tools.digits.uint25bijective_numeration import uint5bijective_numeration_, uint2bijective_numeration_
def _API():
    def uint5bijective_numeration_(radix, offsetted_digits, /, *, is_big_endian, offset4digit):
        'radix/uint{>=2} -> Iter offsetted-digit/int{:<-[offset4digit..<offset4digit+radix]} -> uint # [original-bijective_numeration => [offset4digit:=1]]'
    def uint2bijective_numeration_(radix, u, /, *, is_big_endian, offset4digit):
        'radix/uint{>=2} -> uint -> Iter offsetted-digit/int{:<-[offset4digit..<offset4digit+radix]} # [original-bijective_numeration => [offset4digit:=1]]'

#.from itertools import islice
#.
#.from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.from seed.helper.repr_input import repr_helper
#.from seed.tiny_._Base4repr import _Base4repr
        #sf._reset4repr(may_args4repr, may_kwds4repr)
        #sf._init4repr(*args4repr, **kwds4repr)
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError

def uint2sint_(u, /):
    'uint -> int'
    h = (u>>1)
    i = -1-h if u&1 else h
    return i
def uint5sint_(i, /):
    'int -> uint'
    if i < 0:
        h = -1-i
        u = h<<1
        u ^= 1
    else:
        h = i
        u = h<<1
    return u

def uint2pint_(u, /):
    'uint -> pint'
    return (n:=u+1)
def uint5pint_(n, /):
    'pint -> uint'
    return (u:=n-1)

def uint2imay_(u, /):
    'uint -> imay'
    return (imay:=u-1)
def uint5imay_(imay, /):
    'imay -> uint'
    return (u:=imay+1)


_kwds6g = dict(is_big_endian=True, offset4digit=0)
def uint2uints_(u, /, *, x5uint_=None):
    'uint -> [uint]'
    check_int_ge(0, u)
    if u == 0:
        return null_tuple
    n = u
    us1 = uint2uints1_(uint5pint_(n))
    rs1 = _mk_tuple_fmap_(x5uint_, us1)
    return rs1
def uint5uints_(us, /, *, x2uint_=None):
    '[uint] -> uint'
    us = _may_fmap_(x2uint_, us)
    ns = map(uint2pint_, us)
    u = 1+imay5pints_(ns)
    return u
def uint2uints1_(u, /, *, x5uint_=None):
    'uint -> [uint]{len>=1}'
    ns1 = uint2pints1_(u)
    us1 = map(uint5pint_, ns1)
    rs1 = _mk_tuple_fmap_(x5uint_, us1)
    return rs1
def uint5uints1_(us1, /, *, x2uint_=None):
    '[uint]{len>=1} -> uint'
    us1 = _may_fmap_(x2uint_, us1)
    ns1 = map(uint2pint_, us1)
    u = uint5pints1_(ns1)
    return u


def imay5pints_(ns, /):
    '[pint] -> imay'
    def __(ns, /):
        nonlocal b_empty
        _b_empty = True
        for n in ns:
            _b_empty = False
            check_int_ge(1, n)
            bs = bin(n)[3:] # remove '0b1'
            yield bs
        b_empty = _b_empty
    b_empty = True
    ds = map(int, '2'.join(__(ns)))
    u = uint5bijective_numeration_(3, ds, **_kwds6g)
    imay = -1 if b_empty else u
    return imay
def imay2pints_(imay, /):
    'imay -> [pint]'
    check_int_ge(-1, imay)
    if imay == -1:
        return null_tuple
    u = imay
    return uint2pints1_(u)
def uint5pints1_(ns1, /, *, x2pint_=None, validate=False):
    '[pint]{len>=1} -> uint'
    #.if not x2pint_ is None:
    #.    xs1 = ns1
    #.    ns1 = map(x2pint_, xs1)
    ns1 = _may_fmap_(x2pint_, ns1)
    if validate:
        ns1 = mk_tuple(ns1)
    imay = imay5pints_(ns1)
    if imay == -1: raise ValueError('pints1 empty')
    u = imay
    if validate:
        if not uint2pints1_(u) == ns1:raise AssertionError
    return u
def uint2pints1_(u, /, *, x5pint_=None, validate=False):
    'uint -> [pint]{len>=1}'
    check_int_ge(0, u)
    ds = uint2bijective_numeration_(3, u, **_kwds6g)
    bss = ''.join(map(str, ds)).split('2')
    if not bss:
        bss = ['']
    #uints1 = tuple(tuple(uint5bijective_numeration_(2, bs, **_kwds6g)) for bs in bss)
    ns1 = (int('1'+bs, 2) for bs in bss)
    if validate:
        ns1 = tuple(ns1)
        if not uint5pints1_(ns1) == u:raise AssertionError
    rs1 = _mk_tuple_fmap_(x5pint_, ns1)
    return rs1
    #.if not x5pint_ is None:
    #.    xs1 = map(x5pint_, ns1)
    #.    rs1 = xs1
    #.else:
    #.    rs1 = ns1
    #.rs1 = mk_tuple(rs1)
    #.return rs1

def _may_fmap_(x2y_, ys, /):
    if not x2y_ is None:
        xs = ys
        ys = map(x2y_, xs)
    return ys
def _mk_tuple_fmap_(x5y_, ys, /):
    if not x5y_ is None:
        xs = map(x5y_, ys)
        rs = xs
    else:
        rs = ys
    rs = mk_tuple(rs)
    return rs





def check_uint_tree_(utr, /, *, x2uint_=None):
    'uint_tree -> None|^Exception'
    x2uint_ = ifNone(x2uint_, echo)
    stk = [utr]
    while stk:
        utr = stk.pop()
        T = type(utr)
        if T is tuple:
            utrs = utr
            stk.extend(utrs)
        else:
            x = utr
            u = x2uint_(x)
            check_int_ge(0, u)


def uint2uint_tree_(u, /, *, validate=False, x5uint_=None):
    'uint -> uint_tree'
    x5uint_ = ifNone(x5uint_, echo)
    if validate and not x5uint_ is echo:raise NotImplementedError
    ######################:loop-ver:
    stk = []
    def recur_(u, /):
        stk.append((recur_, u))
    def loop_(us, /):
        stk.append((loop_, (iter(us), [])))
    def return_(utr, /):
        stk.append((return_, utr))
    def main(u, /):
        recur_(u)
        while stk:
            case, x = stk[-1]
            if case == return_:
                utr = x
                stk.pop()
                if not stk:
                    return utr
                    break
                _case, _x = stk[-1]
                #no:if _case == recur_:
                if not _case == loop_:
                    raise 000
                (it, utrs) = _x
                utrs.append(utr)
            elif case == recur_:
                u = x
                stk.pop()
                i = uint2sint_(u)
                if i < 0:
                    h = -1-i
                    us = uint2uints_(h)
                    loop_(us)
                else:
                    v = i
                    x = x5uint_(v)
                    utr = x
                    return_(utr)
            elif case == loop_:
                (it, utrs) = x
                #no:stk.pop()
                for u in it:
                    recur_(u)
                    break
                else:
                    utr = tuple(utrs)
                    stk.pop()
                    return_(utr)
            else:
                raise 000
        #end-while stk:
        raise 000
    #end-def main(u, /):
    if validate:
        assert x5uint_ is echo
        _main = main
        def main(u, /):
            check_int_ge(0, u)
            utr = _main(u)
            check_uint_tree_(utr)
            _u = uint5uint_tree_(utr, validate=False)
            assert _u == u
            return utr
    return main(u)
    ######################:recur-ver:
    def main(u, /):
        i = uint2sint_(u)
        if i < 0:
            h = -1-i
            us = uint2uints_(h)
            #utrs = tuple(map(uint2uint_tree_, us))
            utrs = tuple(map(main, us))
                # !! x5uint_
            utr = utrs
        else:
            v = i
            x = x5uint_(v)
            utr = x
        return utr
    #end-def main(u, /):
    return main(u)
    ######################
def uint5uint_tree_(utr, /, *, validate=False, x2uint_=None):
    'uint_tree -> uint'
    x2uint_ = ifNone(x2uint_, echo)
    if validate and not x2uint_ is echo:raise NotImplementedError
    ######################:loop-ver:
    stk = []
    def recur_(utr, /):
        stk.append((recur_, utr))
    def loop_(utrs, /):
        stk.append((loop_, (iter(utrs), [])))
    def return_(u, /):
        stk.append((return_, u))
    def main(utr, /):
        recur_(utr)
        while stk:
            case, x = stk[-1]
            if case == return_:
                u = x
                stk.pop()
                if not stk:
                    return u
                    break
                _case, _x = stk[-1]
                #no:if _case == recur_:
                if not _case == loop_:
                    raise 000
                (it, us) = _x
                us.append(u)
            elif case == recur_:
                utr = x
                stk.pop()
                if not type(utr) is tuple:
                    x = utr
                    v = x2uint_(x)
                    check_int_ge(0, v)
                    i = v
                    u = uint5sint_(i)
                    return_(u)
                else:
                    utrs = utr
                    loop_(utrs)
            elif case == loop_:
                (it, us) = x
                #no:stk.pop()
                for utr in it:
                    recur_(utr)
                    break
                else:
                    h = uint5uints_(us)
                    i = -1-h
                    u = uint5sint_(i)
                    stk.pop()
                    return_(u)
            else:
                raise 000
        #end-while stk:
        raise 000
    #end-def main(utr, /):
    if validate:
        assert x2uint_ is echo
        _main = main
        def main(utr, /):
            check_uint_tree_(utr)
            u = _main(utr)
            _utr = uint2uint_tree_(u, validate=False)
            assert _utr == utr
            return u
    return main(utr)
    ######################:recur-ver:
    def main(utr, /):
        if not type(utr) is tuple:
            x = utr
            v = x2uint_(x)
            check_int_ge(0, v)
            i = v
        else:
            utrs = utr
            #us = map(uint5uint_tree_, utrs)
            us = map(main, utrs)
                # !! x2uint_
            h = uint5uints_(us)
            i = -1-h
        u = uint5sint_(i)
        return u
    #end-def main(utr, /):
    return main(utr)
    ######################

__all__
from seed.int_tools.bijections4int import uint2sint_, uint5sint_, uint2pint_, uint5pint_, uint2uints_, uint5uints_, uint2uint_tree_, uint5uint_tree_, check_uint_tree_
from seed.int_tools.bijections4int import uint2sint_, uint5sint_, uint2pint_, uint5pint_, uint2uints_, uint5uints_, uint2uints1_, uint5uints1_, imay2pints_, imay5pints_, uint5pints1_, uint2pints1_, uint2uint_tree_, uint5uint_tree_, check_uint_tree_
from seed.int_tools.bijections4int import *
