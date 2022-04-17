#__all__:goto
#main_body_src_code:goto
#HHHHH
#[[[__doc__:begin
r'''
[[
rename:
    e ../../python3_src/seed/tiny_/FreeLocalBatchRouter4py.py
    !mv ../../python3_src/seed/tiny_/FreeLocalBatchRouter4py.py    ../../python3_src/seed/types/FreeLocalBatchRouter4py.py
    e ../../python3_src/seed/types/FreeLocalBatchRouter4py.py
]]

seed.types.FreeLocalBatchRouter4py
py -m    seed.types.FreeLocalBatchRouter4py
py -m nn_ns.app.debug_cmd   seed.types.FreeLocalBatchRouter4py

from seed.types.FreeLocalBatchRouter4py import FreeLocalBatchRouter4py, mk_FreeLocalBatchRouter4py,   Curry, mk_Curry, mk_CurriedFreeLocalBatchRouter4py,   AdaptiveCurry, mk_AdaptiveCurry, mk_AdaptiveCurriedFreeLocalBatchRouter4py,   UnCurry, mk_UnCurry

from seed.types.FreeLocalBatchRouter4py import FreeLocalBatchRouter4py, mk_FreeLocalBatchRouter4py as mkF, mk_CurriedFreeLocalBatchRouter4py as mkCF, mk_AdaptiveCurriedFreeLocalBatchRouter4py as mkACF, mk_UnCurry as mkUC


from seed.types.FreeLocalBatchRouter4py import FreeLocalBatchRouter4py, mk_FreeLocalBatchRouter4py

from seed.types.FreeLocalBatchRouter4py import Curry, mk_Curry, mk_CurriedFreeLocalBatchRouter4py

from seed.types.FreeLocalBatchRouter4py import AdaptiveCurry, mk_AdaptiveCurry, mk_AdaptiveCurriedFreeLocalBatchRouter4py

from seed.types.FreeLocalBatchRouter4py import UnCurry, mk_UnCurry




######################
e ../../python3_src/seed/types/FreeLocalBatchRouter4py.py
    py -m nn_ns.app.mk_py_template -o ../../python3_src/seed/types/FreeLocalBatchRouter4py.py

SKIBC:
    S = \x2f x2a x -> ((x2f x) (x2a x))
    K = \a b -> a
    I = \a -> a
    B = \f g a -> f (g a)
    C = \f a b -> f b a


#[[[doc_sections:begin
#doctest_examples:goto
#wwwzzz:goto

#[[[doctest_examples:begin
>>> from seed.types.FreeLocalBatchRouter4py import FreeLocalBatchRouter4py, mk_FreeLocalBatchRouter4py as mkF, mk_CurriedFreeLocalBatchRouter4py as mkCF, mk_AdaptiveCurriedFreeLocalBatchRouter4py as mkACF, mk_UnCurry as mkUC

#mkF=mk_FreeLocalBatchRouter4py
>>> I = mkF(0, ())
>>> I(555)
Traceback (most recent call last):
    ...
TypeError
>>> I()(555)
555
>>> I = mkF(1, 0)
>>> I(555)
555
>>> K = mkF(2, 0)
>>> K(555, 777)
555
>>> K(555)(777)
Traceback (most recent call last):
    ...
TypeError
>>> B = mkF(3, (0, (1, 2)))
>>> B(repr, hex, 0x777)
"'0x777'"
>>> C = mkF(3, (0, 2, 1))
>>> C(int.__sub__, 555, 777)
222



#mkCF=mk_CurriedFreeLocalBatchRouter4py
>>> K = mkCF([1,1], 0, [])
>>> K(555)(777)
555
>>> K(555, 777)
Traceback (most recent call last):
    ...
TypeError
>>> B = mkCF([2,1], [0, [1, 2]], [])
>>> B(repr, hex)(0x777)
"'0x777'"
>>> C = mkCF([1,2], [0, 2, 1], [])
>>> C(int.__sub__)(555, 777)
222



#mkACF=mk_AdaptiveCurriedFreeLocalBatchRouter4py
>>> K = mkACF(2, 0, [], 0)
>>> K(555)(777)
555
>>> K(555, 777)
555
>>> K555 = K(555)
>>> K() is K
True
>>> K555() is K555
True




#mkUC=mk_UnCurry
>>> call = lambda g: lambda x: g(x)
>>> f = mkUC(call, 2, [1,1])
>>> f(hex, 0x777)
'0x777'




#]]]doctest_examples:end

#[[[wwwzzz:begin
#]]]wwwzzz:end
#]]]doc_sections:end


#'''
#]]]__doc__:end

#################################
#HHHHH
__all__ = '''
    FreeLocalBatchRouter4py
    mk_FreeLocalBatchRouter4py

    Curry
    mk_Curry
    mk_CurriedFreeLocalBatchRouter4py

    AdaptiveCurry
    mk_AdaptiveCurry
    mk_AdaptiveCurriedFreeLocalBatchRouter4py

    UnCurry
    mk_UnCurry
    '''.split()
    #call5iter

#################################
#HHHHH
___begin_mark_of_excluded_global_names__1___ = ...
from seed.tiny_.oXs import eat_iter as _eat_iter, check_intXs_between, check_uintXs_lt, check_uintXs, fold__objXtuple, fold__intXiter, intXiter2intXtuple
from seed.tiny import echo, mk_tuple, print_err
from seed.tiny import check_callable, check_type_is, check_uint
from seed.helper.repr_input import repr_helper


from seed.data_funcs.lnkls import lflnkls_ops, empty_lflnkls, lflnkls_ipush_left, lflnkls_ipop_left, lflnkls2iterable, lflnkls5reversed_iterable

from seed.data_funcs.lnkls import lflnkls5reverseable, lflnkls5args


from seed.data_funcs.lnkls import rglnkls_ops, empty_rglnkls, rglnkls_ipush_right, rglnkls_ipop_right, rglnkls2reversed_iterable, rglnkls5iterable

from seed.data_funcs.lnkls import rglnkls2list



#from functools import partial
from itertools import chain

___end_mark_of_excluded_global_names__1___ = ...

#HHHHH
#[[[main_body_src_code:begin
#FreeLocalBatchRouter4py:goto
#Curry:goto
#AdaptiveCurry:goto
#UnCurry:goto
#zzzwww:goto




#[[[FreeLocalBatchRouter4py:begin

class FreeLocalBatchRouter4py:
    r'''(num_args4call, uXss4body)

    see:
        view ../../python3_src/nn_ns/mimic_Haskell/Data.py
        :: FreeLocalBatchRouter
        view ../../python3_src/seed/tiny_/oXs.py


    #'''
    def __init__(sf, num_args4call, uXss4body, /):
        check_uint(num_args4call)
        #check_type_is(tuple, uXss4body)
        #   uint|tuple
        check_uintXs_lt(num_args4call, uXss4body)
        sf._num_args4call = num_args4call
        sf._uXss4body = uXss4body
        return
    def __ne__(sf, ot, /):
        return not sf == ot
    def __eq__(sf, ot, /):
        if sf is ot: return True
        if not type(sf) is type(ot): return False
        return sf.get_args8init_FreeLocalBatchRouter4py() == ot.get_args8init_FreeLocalBatchRouter4py()
    def __hash__(sf, /):
        cls = type(sf)
        (num_args4call, uXss4body) = sf.get_args8init_FreeLocalBatchRouter4py()
        return hash((cls, num_args4call, uXss4body))
    def __repr__(sf, /):
        (num_args4call, uXss4body) = sf.get_args8init_FreeLocalBatchRouter4py()
        return repr_helper(sf, num_args4call, uXss4body)
    def get_args8init_FreeLocalBatchRouter4py(sf, /):
        return sf._num_args4call,  sf._uXss4body
    def __call__(sf, /, *args):
        (num_args4call, uXss4body) = sf.get_args8init_FreeLocalBatchRouter4py()
        if not len(args) == num_args4call: raise TypeError
        f4u = args.__getitem__
        f4s = call5iter
        return fold__intXiter(f4u, f4s, uXss4body)
FreeLocalBatchRouter4py(0, ())

def mk_FreeLocalBatchRouter4py(num_args4call, uXss4body, /):
    #bug:def mk_FreeLocalBatchRouter4py(num_args4call, /, *uXss4body):
    #   why diff nn_ns.mimic_Haskell.Data::mk_FreeLocalBatchRouter API?
    #       since (*uXss4body) always be tuple, hence must be a call
    #       0 become _0()
    #       (0, 1) become _0(1)()
    return FreeLocalBatchRouter4py(num_args4call, intXiter2intXtuple(uXss4body))
def call5iter(it, /):
    #it = [*it]
    #print_err(it)
    it = iter(it)
    for f in it:
        break
    else:
        # [] ==>> echo
        return echo
    return f(*it)


#]]]FreeLocalBatchRouter4py:end



#[[[Curry:begin

#from seed.data_funcs.lnkls import
class Curry:
    r'''(func, args_rglnkls, num_args_lflnkls)


    args_rglnkls = rglnkls<args>
    num_args_lflnkls = lflnkls<num_args4call>


    args_rglnkls = () | (args_rglnkls, args)
    num_args_lflnkls = () | (num_args4call, num_args_lflnkls)

    per call:
        push args_rglnkls
        pop num_args_lflnkls

    #'''
    def __init__(sf, func, args_rglnkls, num_args_lflnkls, /):
        check_callable(func)
        check_type_is(tuple, args_rglnkls)
        check_type_is(tuple, num_args_lflnkls)
        assert len(args_rglnkls) in [0,2]
        #assert len(num_args_lflnkls) in [0,2]
        if not num_args_lflnkls: raise TypeError
        sf._func = func
        sf._args_rglnkls = args_rglnkls
        sf._num_args_lflnkls = num_args_lflnkls
        return
    def __ne__(sf, ot, /):
        return not sf == ot
    def __eq__(sf, ot, /):
        if sf is ot: return True
        if not type(sf) is type(ot): return False
        return sf.get_args8init_Curry() == ot.get_args8init_Curry()
    def __hash__(sf, /):
        cls = type(sf)
        (func, args_rglnkls, num_args_lflnkls) = sf.get_args8init_Curry()
        return hash((cls, func, args_rglnkls, num_args_lflnkls))

    def __repr__(sf, /):
        (func, args_rglnkls, num_args_lflnkls) = sf.get_args8init_Curry()
        return repr_helper(sf, func, args_rglnkls, num_args_lflnkls)
    def get_args8init_Curry(sf, /):
        return sf._func, sf._args_rglnkls, sf._num_args_lflnkls
    def __call__(sf, /, *args):
        (func, args_rglnkls, num_args_lflnkls) = sf.get_args8init_Curry()
        (_num_args_lflnkls, num_args4call) = lflnkls_ipop_left(num_args_lflnkls)
        if not len(args) == num_args4call: raise TypeError
        (_args_rglnkls, _) = rglnkls_ipush_right(args_rglnkls, args)
        if not _num_args_lflnkls:
            #call!
            argss = rglnkls2list(_args_rglnkls)
            args = chain(*argss)
            return func(*args)
        else:
            #partial
            return __class__(func, _args_rglnkls, _num_args_lflnkls)

Curry(echo, (), (0, ()))

def mk_Curry(func, argss, num_args__s, /):
    argss = mk_tuple(map(mk_tuple, argss))
    num_args__s = mk_tuple(num_args__s)
    if not all(num_args4call >= 0 for num_args4call in num_args__s):raise TypeError

    if type(func) is FreeLocalBatchRouter4py:
        router4py = func
        num_args4call__total = sum(map(len, argss)) + sum(num_args__s)
        (num_args4call, uXss4body) = router4py.get_args8init_FreeLocalBatchRouter4py()
        if not num_args4call == num_args4call__total: raise TypeError

    #print_err('x'*55)
    args_rglnkls = rglnkls5iterable(argss)
    #print_err('y'*55)
    num_args_lflnkls = lflnkls5reverseable(num_args__s)
    #print_err('z'*55)
    return Curry(func, args_rglnkls, num_args_lflnkls)
def mk_CurriedFreeLocalBatchRouter4py(all__num_args__s, uXss4body, argss, /):
    all__num_args__s = mk_tuple(all__num_args__s)
    num_args4call__total = sum(all__num_args__s)

    argss = mk_tuple(map(mk_tuple, argss))
    if not len(argss) < len(all__num_args__s): raise TypeError #no ==
    if not all(len(args) == num_args4call for args, num_args4call in zip(argss, all__num_args__s)): raise TypeError #no ==

    remain__num_args__s = all__num_args__s[len(argss):]


    func = mk_FreeLocalBatchRouter4py(num_args4call__total, uXss4body)
    return mk_Curry(func, argss, remain__num_args__s)



#]]]Curry:end


#[[[AdaptiveCurry:begin
class AdaptiveCurry:
    r'''(func, args_rglnkls, num_remain_args, num_remain_tail_laziness)


    args_rglnkls = rglnkls<args>

    args_rglnkls = () | (args_rglnkls, args)

    per call:
        push args_rglnkls
        if args:
            num_remain_args -= len(args)
        elif not num_remain_args:
            num_remain_tail_laziness -= 1


    #'''
    def __init__(sf, func, args_rglnkls, num_remain_args, num_remain_tail_laziness, /):
        check_callable(func)
        check_type_is(tuple, args_rglnkls)
        check_uint(num_remain_args)
        check_uint(num_remain_tail_laziness)
        assert len(args_rglnkls) in [0,2]
        if not (num_remain_args or num_remain_tail_laziness): raise TypeError
        sf._func = func
        sf._args_rglnkls = args_rglnkls
        sf._num_remain_args = num_remain_args
        sf._num_remain_tail_laziness = num_remain_tail_laziness
        return
    def __ne__(sf, ot, /):
        return not sf == ot
    def __eq__(sf, ot, /):
        if sf is ot: return True
        if not type(sf) is type(ot): return False
        return sf.get_args8init_AutoCurry() == ot.get_args8init_AutoCurry()
    def __hash__(sf, /):
        cls = type(sf)
        (func, args_rglnkls, num_remain_args, num_remain_tail_laziness) = sf.get_args8init_AutoCurry()
        return hash((cls, func, args_rglnkls, num_remain_args, num_remain_tail_laziness))

    def __repr__(sf, /):
        (func, args_rglnkls, num_remain_args, num_remain_tail_laziness) = sf.get_args8init_AutoCurry()
        return repr_helper(sf, func, args_rglnkls, num_remain_args, num_remain_tail_laziness)
    def get_args8init_AutoCurry(sf, /):
        return sf._func, sf._args_rglnkls, sf._num_remain_args, sf._num_remain_tail_laziness
    def __call__(sf, /, *args):
        (func, args_rglnkls, num_remain_args, num_remain_tail_laziness) = sf.get_args8init_AutoCurry()
        if not len(args) <= num_remain_args: raise TypeError
        if args:
            (_args_rglnkls, _) = rglnkls_ipush_right(args_rglnkls, args)
            num_remain_args -= len(args)
                # may (x,0) --> (0,0)
        elif not num_remain_args:
            assert num_remain_tail_laziness
            num_remain_tail_laziness -= 1
                # may (0,1) --> (0,0)
        else:
            #incomplete empty call
            # (x,y) --> (x,y)
            return sf
        ######################
        if not (num_remain_args or num_remain_tail_laziness):
            #call!
            #(0,0)
            argss = rglnkls2list(_args_rglnkls)
            args = chain(*argss)
            return func(*args)
        else:
            #partial
            return __class__(func, _args_rglnkls, num_remain_args, num_remain_tail_laziness)

AdaptiveCurry(echo, (), 1, 0)


def mk_AdaptiveCurry(num_args4call__total, func, argss, num_remain_tail_laziness, /):
    argss = mk_tuple(map(mk_tuple, argss))
    num_remain_args = num_args4call__total - sum(map(len, argss))
    if not num_remain_args >= 0: raise TypeError

    if type(func) is FreeLocalBatchRouter4py:
        router4py = func
        (num_args4call, uXss4body) = router4py.get_args8init_FreeLocalBatchRouter4py()
        if not num_args4call == num_args4call__total: raise TypeError

    args_rglnkls = rglnkls5iterable(argss)
    return AdaptiveCurry(func, args_rglnkls, num_remain_args, num_remain_tail_laziness)
def mk_AdaptiveCurriedFreeLocalBatchRouter4py(num_args4call__total, uXss4body, argss, num_remain_tail_laziness, /):
    func = mk_FreeLocalBatchRouter4py(num_args4call__total, uXss4body)
    return mk_AdaptiveCurry(num_args4call__total, func, argss, num_remain_tail_laziness)



#]]]AdaptiveCurry:end


#[[[UnCurry:begin
if 0:
    class UnCurry: pass
def UnCurry(func, num_args__s, /):
    check_callable(func)
    check_type_is(tuple, num_args__s)
    any(map(check_uint, num_args__s))
    if not num_args__s:
        data = func
        return data
    elif len(num_args__s) == 1:
        return func
    num_args4call__total = 1+sum(num_args__s)
        # 1 -- first arg _0 is "func" itself
    uXss4body = 0
        # _0 := func
    begin = 1
        # [_1..]
    for num_args4call in num_args__s:
        end = begin + num_args4call
        uXss4body = (uXss4body, *range(begin, end))
        begin = end
    assert begin == end == num_args4call__total

    g = mk_CurriedFreeLocalBatchRouter4py([1, num_args4call__total-1], uXss4body, [[func]])
    if __debug__:
        f_ = FreeLocalBatchRouter4py(num_args4call__total, uXss4body)
        f = Curry(f_, ((), (func,)), (num_args4call__total-1, ()))
        assert g.get_args8init_Curry() == f.get_args8init_Curry()
    return g

def mk_UnCurry(func, num_args4call__total, num_args__s, /):
    num_args__s = mk_tuple(num_args__s)
    if not num_args4call__total == sum(num_args__s): raise TypeError #not include "func" yet
    return UnCurry(func, num_args__s)


#]]]UnCurry:end


#[[[zzzwww:begin
#]]]zzzwww:end
#]]]main_body_src_code:end


#HHHHH
if __name__ == "__main__":
    from seed.types.FreeLocalBatchRouter4py import *

    from seed.types.FreeLocalBatchRouter4py import FreeLocalBatchRouter4py, mk_FreeLocalBatchRouter4py,   Curry, mk_Curry, mk_CurriedFreeLocalBatchRouter4py,   AdaptiveCurry, mk_AdaptiveCurry, mk_AdaptiveCurriedFreeLocalBatchRouter4py,   UnCurry, mk_UnCurry

    from seed.types.FreeLocalBatchRouter4py import FreeLocalBatchRouter4py, mk_FreeLocalBatchRouter4py as mkF, mk_CurriedFreeLocalBatchRouter4py as mkCF, mk_AdaptiveCurriedFreeLocalBatchRouter4py as mkACF, mk_UnCurry as mkUC


    from seed.types.FreeLocalBatchRouter4py import FreeLocalBatchRouter4py, mk_FreeLocalBatchRouter4py

    from seed.types.FreeLocalBatchRouter4py import Curry, mk_Curry, mk_CurriedFreeLocalBatchRouter4py

    from seed.types.FreeLocalBatchRouter4py import AdaptiveCurry, mk_AdaptiveCurry, mk_AdaptiveCurriedFreeLocalBatchRouter4py

    from seed.types.FreeLocalBatchRouter4py import UnCurry, mk_UnCurry


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #<BLANKLINE>
    #Traceback (most recent call last):


