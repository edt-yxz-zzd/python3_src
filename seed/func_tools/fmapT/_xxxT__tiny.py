#__all__:goto
#main_body_src_code:goto
#HHHHH
#[[[__doc__:begin
r'''

fmapT
predicatorT/predT
filterT
alterT
checkT

[[
rename:
    !mv ../../python3_src/seed/func_tools/fmapT/fmapT__tiny.py ../../python3_src/seed/func_tools/fmapT/_xxxT__tiny.py
    ######################
    e ../../python3_src/seed/func_tools/fmapT/fmapT__tiny.py
    e ../../python3_src/seed/func_tools/fmapT/predT__tiny.py
    e ../../python3_src/seed/func_tools/fmapT/filterT__tiny.py
    e ../../python3_src/seed/func_tools/fmapT/alterT__tiny.py
    e ../../python3_src/seed/func_tools/fmapT/checkT__tiny.py
    ######################
    e ../../python3_src/seed/func_tools/fmapT/all_xxxT__tiny.py
    e ../../python3_src/seed/func_tools/fmapT/all_xxxT__common_utils.py


seed.func_tools.fmapT._xxxT__tiny
py -m    seed.func_tools.fmapT._xxxT__tiny
py -m nn_ns.app.debug_cmd   seed.func_tools.fmapT._xxxT__tiny
py -m nn_ns.app.debug_cmd   seed.func_tools.fmapT._xxxT__tiny > $my_tmp/out4py/debug_cmd.fmapT._xxxT__tiny.txt
view /sdcard/0my_files/tmp//out4py/debug_cmd.fmapT._xxxT__tiny.txt
]]



######################
######################
######################original
seed.func_tools.fmapT.fmapT__tiny
py -m    seed.func_tools.fmapT.fmapT__tiny
py -m nn_ns.app.debug_cmd   seed.func_tools.fmapT.fmapT__tiny

from seed.func_tools.fmapT.fmapT__tiny import fmapT__dict, fmapT__list, fmapT__iter, fmapT__tuple, fmapT__tpls, fmapT__pairs, fmap_rngs2hex_repr


e ../../python3_src/seed/func_tools/fmapT/fmapT__tiny.py
    简化版 of 设想中的 parameterized_transform.py
see:
    view ../../python3_src/seed/func_tools/parameterized_transform.py

#[[[doc_sections:begin
#doctest_examples:goto
#wwwzzz:goto

#[[[doctest_examples:begin
>>>
...
#]]]doctest_examples:end

#[[[wwwzzz:begin
#]]]wwwzzz:end
#]]]doc_sections:end


#'''
#]]]__doc__:end

#################################
#HHHHH
#__all__:begin[[
__all__ = '''
    items_of
    keys_of
    values_of
    zip__same_len
    chain_from_iterable
    dot
    to_True
    to_False
    to_None
    to_Ellipsis
    to_NotImplemented
    xor5iter
    unpack_star_args_of
    pack_star_args_of


    fmapT__dict
    fmapT__list
    fmapT__iter
    fmapT__tuple
    fmapT__iter_tuple
    fmapT__tpls
    fmapT__pairs
    fmap_rngs2hex_repr


    not_
    is_True
    is_False
    is_None
    is_Ellipsis
    is_NotImplemented
    is_not_True
    is_not_False
    is_not_None
    is_not_Ellipsis
    is_not_NotImplemented
    fix_predicator
    allT__pattern_tuple
    anyT__pattern_tuple
    anyT__pattern_list
    allT__pattern_list
    anyT__pattern_dict
    allT__pattern_dict
    type_isT
    type_leT
    isinstanceT
    issubclassT
    isT
    is_notT
    eqT
    neT
    ltT
    gtT
    leT
    geT
    ge_ltT
    pred__True
    pred__False
    not_dotT
    predT__NOT
    predT__bool_op_
    predT__AND
    predT__NOT_AND
    predT__AND_NOT
    predT__NOT_AND_NOT
    predT__OR
    predT__NOT_OR
    predT__OR_NOT
    predT__NOT_OR_NOT
    predT__XOR
    predT__NOT_XOR
    predT__XOR_NOT
    predT__NOT_XOR_NOT
    is_frozenset
    is_set
    is_dict
    is_bool
    is_int
    is_uint
    is_float
    is_complex
    is_bytes
    is_str
    is_char
    is_tuple
    is_list
    predT__tuple
    predT__list
    predT__frozenset
    predT__set
    predT__dict
    predT_on_property
    len_eqT
    len_ltT
    len_geT
    len_ge_ltT
    is_empty


    mk__x2tmay__from__pred
    predicator_to_x2xs
    mk_x2xs__pred
    filterT_
    filterT
    filterT_fix
    filterT__tuple
    mk_filterT__5xs_2xs
    filterT__list
    filterT__set
    filterT__dict


    mk_alterT__5xs_2xs
    alterT__dict
    alterT__set
    alterT__list
    alterT__tuple__chain
    tuple2iter_tuples__product


    icheckT
    checkT__pattern_tuple
    checkT__pattern_list
    checkT__pattern_dict
    checkT__pattern_dictKV
    checkT__pattern_tmay
    checkT__5pred
    checkT__AND
    checkT__type_is
    checkT__type_le
    checkT__issubclass__any
    checkT__issubclass__all
    checkT__type_is__AND
    checkT__type_le__AND
    check__pass
    check__fail
    checkT__ifelse
    checkT__if
    checkT__if_not
    checkT__is
    checkT__eq
    checkT__ne
    checkT__lt
    checkT__gt
    checkT__le
    checkT__ge
    checkT__ge_lt
    checkT__len_eq
    checkT__len_ne
    checkT__len_lt
    checkT__len_le
    checkT__len_gt
    checkT__len_ge
    checkT__len_ge_lt
    check_bool
    check_int
    check_uint
    check_float
    check_complex
    check_bytes
    check_str
    check_char
    check_tuple
    check_list
    check_frozenset
    check_set
    check_dict
    check__is_None
    check_callable
    checkT__tmay
    checkT__smay
    checkT__may
    checkT__imay
    checkT__tuple
    checkT__list
    checkT__frozenset
    checkT__set
    checkT__dict
    checkT__dictKV



    '''.split()
#__all__:end]]


#################################
#HHHHH
___begin_mark_of_excluded_global_names__0___ = ...
from seed.tiny import fmap4dict_value as _fmapT__dict
from seed.tiny import HexReprInt
#from seed.tiny import check_type_is
from seed.func_tools.dot2 import dot as __dot
from seed.func_tools.dotSBC import dotC__fT_g
#from seed.func_tools.dotSBC import dot, dotC__fT_g, dotB__f_gT, dotS__fT_gT, dotC__f1_g, dotB__f_g1, dotC__fm_g, dotB__f_gm, dotT__fs_gTs_hs, dotT__fs_g1s_hs, dotT__fs_gms_hs

#from functools import
from functools import reduce
import operator
from operator import is_not, not_ as __not_

from itertools import chain, product, compress

r'''[[[
from seed.types.FreeLocalBatchRouter4py import FreeLocalBatchRouter4py, mk_FreeLocalBatchRouter4py
TODO:使用 mk_FreeLocalBatchRouter4py 简化 表达式
    from seed.types.FreeLocalBatchRouter4py import FreeLocalBatchRouter4py, mk_FreeLocalBatchRouter4py,   Curry, mk_Curry, mk_CurriedFreeLocalBatchRouter4py,   AdaptiveCurry, mk_AdaptiveCurry, mk_AdaptiveCurriedFreeLocalBatchRouter4py,   UnCurry, mk_UnCurry
    e ../../python3_src/seed/types/FreeLocalBatchRouter4py.py
#TODO: predT__record???
#TODO: checkT__record???
#]]]'''

___end_mark_of_excluded_global_names__0___ = ...


#HHHHH
#[[[main_body_src_code:begin
#common_utils:goto
#fmapT:goto
#predicatorT/predT:goto
#filterT:goto
#alterT:goto
#checkT:goto
#zzzwww:goto

#[[[common_utils:begin
items_of = lambda d, /: d.items()
keys_of = lambda d, /: d.keys()
values_of = lambda d, /: d.values()


def _check_len_same(lhs, rhs, /):
    if 0:
        if not len(lhs) == len(rhs):raise TypeError(f'len(lhs)={len(lhs)}; len(rhs)={len(rhs)};    lhs={lhs!r};    rhs={rhs!r};')
    else:
        if not len(lhs) == len(rhs):raise TypeError(f'len(lhs)={len(lhs)}; len(rhs)={len(rhs)};    type(lhs)={type(lhs)}; type(rhs)={type(rhs)};')
    return
def zip__same_len(lhs, rhs, /):
    _check_len_same(lhs, rhs)
    return zip(lhs, rhs)
chain_from_iterable = chain.from_iterable


dot = __dot
to_True = lambda _, /: True
to_False = lambda _, /: False
to_None = lambda _, /: None
to_Ellipsis = lambda _, /: Ellipsis
to_NotImplemented = lambda _, /: NotImplemented


def xor5iter(it, /):
    it = map(bool, it)
    #op = operator.__xor__
    #op = bool.__xor__
    op = operator.is_not
    return reduce(op, it, False)


def unpack_star_args_of(f, /):
    return lambda args, /: f(*args)
def pack_star_args_of(f, /):
    return lambda *args: f(args)


#]]]common_utils:end

#[[[fmapT:begin
#fmap

def fmapT__dict(f, /):
    return lambda d, /: _fmapT__dict(f, d)
def fmapT__list(f, /):
    return lambda ls, /: [*map(f, ls)]
def fmapT__iter(f, /):
    return lambda it, /: map(f, it)
def fmapT__tuple(*funcs):
    return dot[tuple, fmapT__iter_tuple(*funcs)]
def fmapT__iter_tuple(*funcs):
    return lambda tpl, /: (f(x) for f, x in zip__same_len(funcs, tpl))
    return lambda tpl, /: _check_len_same(funcs, tpl) or (f(x) for f, x in zip(funcs, tpl))

#fmapT__pairs(f, g, /)
fmapT__tpls = dot[fmapT__list, fmapT__tuple]
fmapT__pairs = fmapT__tpls
fmap_rngs2hex_repr = fmapT__pairs(HexReprInt, HexReprInt)

#]]]fmapT:end


#[[[predicatorT/predT:begin
#predicator


#not_ = lambda x, /: not (x)
not_ = __not_

is_True = lambda x: x is True
is_False = lambda x: x is False
is_None = lambda x: x is None
is_Ellipsis = lambda x: x is Ellipsis
is_NotImplemented = lambda x: x is NotImplemented

is_not_True = lambda x: x is not True
is_not_False = lambda x: x is not False
is_not_None = lambda x: x is not None
is_not_Ellipsis = lambda x: x is not Ellipsis
is_not_NotImplemented = lambda x: x is not NotImplemented


_2pred = {
    None:bool
    ,'not': not_
    ,-1: not_
    ,True: to_True
    ,False: to_False
    }
def fix_predicator(pred, /):
    if callable(pred):
        return pred
    return _2pred[pred]
    if pred is None:
        return bool
    elif type(pred) is bool:
        return to_True if pred else to_False
    elif type(pred) is str:
        if pred == 'not':
            return not_
        return ...

def allT__pattern_tuple(*preds):
    return dot[all, fmapT__iter_tuple(*preds)]
def anyT__pattern_tuple(*preds):
    return dot[any, fmapT__iter_tuple(*preds)]
def anyT__pattern_list(pred, /):
    return dot[any, [map, pred],]
def allT__pattern_list(pred, /):
    return dot[all, [map, pred],]
    return dot[all, fmapT__iter(pred)]
def anyT__pattern_dict(pred, /):
    return dot[any, [map, pred], items_of]
def allT__pattern_dict(pred, /):
    return dot[all, [map, pred], items_of]

def type_isT(cls, /):
    return lambda x: type(x) is cls
def type_leT(cls, /):
    return lambda x: issubclass(type(x), cls)
def isinstanceT(cls, /):
    return lambda x: isinstance(x, cls)
def issubclassT(cls, /):
    return lambda x: issubclass(x, cls)
def isT(z, /):
    return lambda x: x is z
#is_notT = not_dotT(isT)
def is_notT(z, /):
    return lambda x: x is not z
def eqT(z, /):
    return lambda x: x == z
def neT(z, /):
    return lambda x: not x == z
    return lambda x: x != z
def ltT(z, /):
    return lambda x: x < z
def gtT(z, /):
    return lambda x: x > z
def leT(z, /):
    return lambda x: x <= z
def geT(z, /):
    return lambda x: x >= z
def ge_ltT(m, M, /):
    return lambda x: m <= x < M

pred__True = to_True
pred__False = to_False
#bug:predT__NOT = not_dotT
def not_dotT(f, /):
    'f(...) ==>> not f(...)'
    return dot[not_, f]
def predT__NOT(pred, /):
    'f(x) ==>> not f(x) #special form of not_dotT'
    return lambda x, /: not pred(x)
def predT__bool_op_(*preds, notI, notO, bool5iter):
    if notI:
        preds = tuple(map(predT__NOT, preds))
    f8out = not_ if notO else bool #echo
    def _pred(x, /):
        r = bool5iter(pred(x) for pred in preds)
        return f8out(r)
    return _pred
def predT__AND(*preds):
    return predT__bool_op_(*preds, notI=False, notO=False, bool5iter=all)
def predT__NOT_AND(*preds):
    return predT__bool_op_(*preds, notI=False, notO=True, bool5iter=all)
def predT__AND_NOT(*preds):
    return predT__bool_op_(*preds, notI=True, notO=False, bool5iter=all)
def predT__NOT_AND_NOT(*preds):
    return predT__bool_op_(*preds, notI=True, notO=True, bool5iter=all)

def predT__OR(*preds):
    return predT__bool_op_(*preds, notI=False, notO=False, bool5iter=any)
def predT__NOT_OR(*preds):
    return predT__bool_op_(*preds, notI=False, notO=True, bool5iter=any)
def predT__OR_NOT(*preds):
    return predT__bool_op_(*preds, notI=True, notO=False, bool5iter=any)
def predT__NOT_OR_NOT(*preds):
    return predT__bool_op_(*preds, notI=True, notO=True, bool5iter=any)




def predT__XOR(*preds):
    return predT__bool_op_(*preds, notI=False, notO=False, bool5iter=xor5iter)
def predT__NOT_XOR(*preds):
    return predT__bool_op_(*preds, notI=False, notO=True, bool5iter=xor5iter)
def predT__XOR_NOT(*preds):
    return predT__bool_op_(*preds, notI=True, notO=False, bool5iter=xor5iter)
def predT__NOT_XOR_NOT(*preds):
    return predT__bool_op_(*preds, notI=True, notO=True, bool5iter=xor5iter)






if 0:
    #is_x = isT(x)
    #see: above
    is_True = lambda x: x is True
    is_False = lambda x: x is False
    is_None = lambda x: x is None
    is_Ellipsis = lambda x: x is Ellipsis
    is_NotImplemented = lambda x: x is NotImplemented

#is_x = type_isT(x)
is_frozenset = isT(frozenset)
is_set = isT(set)
is_dict = isT(dict)

is_bool = type_isT(bool)
is_int = type_isT(int)
def is_uint(u, /):
    return is_int(u) and u >= 0
is_float = type_isT(float)
is_complex = type_isT(complex)

is_bytes = type_isT(bytes)
is_str = type_isT(str)
def is_char(ch, /):
    return is_str(ch) and len(ch)==1

is_tuple = type_isT(tuple)
is_list = type_isT(list)
is_frozenset = type_isT(frozenset)
is_set = type_isT(set)
is_dict = type_isT(dict)

if 0:
    def predT__tuple(*preds):
        return predT__AND(is_tuple, allT__pattern_tuple(*preds))
else:
    predT__tuple = dot[[predT__AND, is_tuple], allT__pattern_tuple]
    predT__list = dot[[predT__AND, is_list], allT__pattern_list]
    predT__frozenset = dot[[predT__AND, is_frozenset], allT__pattern_list]
    predT__set = dot[[predT__AND, is_set], allT__pattern_list]
    predT__dict = dot[[predT__AND, is_dict], allT__pattern_dict]
    #TODO: predT__record???


if 0:
    def predT_on_property(predT, f, /):
        def _predT(*args, **kwargs):
            return dot[predT(*args, **kwargs), f]
        return _predT
    #dotC__fT_g = predT_on_property


predT_on_property = dotC__fT_g

len_eqT = predT_on_property(eqT, len)
len_ltT = predT_on_property(ltT, len)
len_geT = predT_on_property(geT, len)
len_ge_ltT = predT_on_property(ge_ltT, len)


is_empty = not_
is_empty = len_eqT(0)

#]]]predicatorT/predT:end



#[[[filterT:begin
#filter

def mk__x2tmay__from__pred(pred, /):
    #def mk_x2xs__pred(pred, /):
    #def predicator_to_x2xs(pred, /):
    return lambda x, /: (x,) if pred(x) else ()
predicator_to_x2xs = mk__x2tmay__from__pred
mk_x2xs__pred = mk__x2tmay__from__pred


def filterT_(pred, /, fix):
    if fix:
        pred = fix_predicator(pred)
    return filterT(pred)
def filterT(pred, /):
    return lambda xs, /: filter(pred, xs)
    return dot[[filter, pred],]
filterT_fix = dot[filterT, fix_predicator]

if 0:
    filterT__tuple = lambda *preds: lambda xs, /: tuple(x for x, b in zip(xs, fmapT__tuple(*preds)(xs)) if b)
    filterT__list = lambda pred, /: dot[list, filterT(pred)]
    filterT__set = lambda pred, /: dot[set, filterT(pred)]
    filterT__dict = lambda pred, /: dot[dict, filterT(pred), items_of]

filterT__tuple = lambda *preds: (lambda _2preds, /: lambda xs, /: tuple(x for x, b in zip(xs, _2preds(xs)) if b))(fmapT__tuple(*preds))
    #compress
_mk_filterT__xxx = lambda xxx, _iter, /: lambda pred, /: (lambda xxx, _filterT, _iter, /: dot[xxx, _filterT, _iter])(xxx, filterT(pred), _iter)
def mk_filterT__5xs_2xs(_5xs, _2xs, /):
    def _mk_filterT(pred, /, fix=False):
        #bug:_filterT = filterT_fix(pred, fix=fix)
        _filterT = filterT_(pred, fix=fix)
        #bug:return lambda z, /: dot[_5xs, _filterT, _2xs]
        return dot[_5xs, _filterT, _2xs]
    return _mk_filterT
_mk_filterT__xxx = mk_filterT__5xs_2xs
filterT__list = _mk_filterT__xxx(list, iter)
filterT__set =  _mk_filterT__xxx(set, iter)
filterT__dict = _mk_filterT__xxx(dict, items_of)

#]]]filterT:end



#[[[alterT:begin
#alter

if 0:
    def alterT__dict(x2xs, /):
        return lambda d, /: dict(chain_from_iterable(map(x2xs, d.items())))

def mk_alterT__5xs_2xs(_5xs, _2xs, /):
    return lambda x2xs, /: lambda z, /: _5xs(chain_from_iterable(map(x2xs, _2xs(z))))
    return lambda x2xs, /: dot[_5xs, chain_from_iterable, [map, x2xs], _2xs, ]
alterT__dict = mk_alterT__5xs_2xs(dict, items_of)
alterT__set = mk_alterT__5xs_2xs(set, iter)
alterT__list = mk_alterT__5xs_2xs(list, iter)


if 1:
    #no  alterT__tuple???
    def alterT__tuple__chain(*x2xs__ls):
        #def alterT__tuple(*x2xs__ls):
        #def alterT__tuple__chain(*x2xs__ls, /):
        return dot[tuple, chain_from_iterable, fmapT__iter_tuple(*x2xs__ls)]
        return lambda xs, /: tuple(chain_from_iterable(fmapT__iter_tuple(*x2xs__ls)(xs)))
    def tuple2iter_tuples__product(*x2xs__ls):
        #def alterT__tuple__product(*x2xs__ls, /):
        return dot[unpack_star_args_of(product), fmapT__iter_tuple(*x2xs__ls)]
        return lambda xs, /: product(*fmapT__iter_tuple(*x2xs__ls)(xs))


#]]]alterT:end

#[[[checkT:begin
#check

def icheckT(check, /):
    def icheck(x, /):
        check(x)
        return x
    return icheck

def checkT__pattern_tuple(*checks):
    def check(xs, /):
        xs = [*xs]
        for x, f in zip__same_len(xs, checks):
            f(x)
    return check
def checkT__pattern_list(check, /):
    def _check_all(xs, /):
        xs = iter(xs)
        for x in xs:
            check(x)
    return _check_all
def checkT__pattern_dict(check4item, /):
    return dot[checkT__pattern_list(check4item), items_of]
def checkT__pattern_dictKV(check4key, check4value, /):
    check4item = checkT__pattern_tuple(check4key, check4value)
    return checkT__pattern_dict(check4item)
def checkT__pattern_tmay(check, /):
    def check(tm, /):
        if not len(tm) < 2: raise TypeError
        if tm:
            [x] = tm
            check(x)
    return check



def checkT__5pred(pred, /, *, lazy_exc=TypeError):
    def check(x, /):
        if not pred(x):raise lazy_exc()
    return check
def checkT__AND(*checks):
    def check(x, /):
        for f in checks:
            f(x)
    return check
def checkT__type_is(cls, /, *, lazy_exc=TypeError):
    def check(x, /):
        if not type(x) is cls:raise lazy_exc()
    return check
def checkT__type_le(cls, /, *, lazy_exc=TypeError):
    def check(x, /):
        if not issubclass(type(x),cls):raise lazy_exc()
    return check
def checkT__issubclass__any(*clss, lazy_exc=TypeError):
    def check(T, /):
        if not any(issubclass(T, cls) for cls in clss):raise lazy_exc()
    return check
def checkT__issubclass__all(*clss, lazy_exc=TypeError):
    def check(T, /):
        if not all(issubclass(T, cls) for cls in clss):raise lazy_exc()
    return check
def checkT__type_is__AND(cls, /, *checks, lazy_exc=TypeError):
    return checkT__AND(checkT__type_is(cls, lazy_exc=lazy_exc), *checks)
def checkT__type_le__AND(cls, /, *checks, lazy_exc=TypeError):
    return checkT__AND(checkT__type_le(cls, lazy_exc=lazy_exc), *checks)

def check__pass(_, /):pass
def check__fail(_, /, *, lazy_exc=TypeError):
    raise lazy_exc()

def checkT__ifelse(pred, check4then, check4else, /):
    def check(x, /):
        if pred(x):
            check4then(x)
        else:
            check4else(x)
    return check
def checkT__if(pred, check, /):
    return checkT__ifelse(pred, check, check__pass)
def checkT__if_not(pred, check, /):
    return checkT__ifelse(pred, check__pass, check)


def checkT__is(z, /, *, lazy_exc=TypeError):
    def check(x, /):
        if not (x is z):raise lazy_exc()
    return check
def checkT__eq(z, /, *, lazy_exc=TypeError):
    def check(x, /):
        if not (x == z):raise lazy_exc()
    return check
def checkT__ne(z, /, *, lazy_exc=TypeError):
    def check(x, /):
        #if not (x != z):raise lazy_exc()
        if (x == z):raise lazy_exc()
    return check
def checkT__lt(z, /, *, lazy_exc=TypeError):
    def check(x, /):
        if not (x < z):raise lazy_exc()
    return check
def checkT__gt(z, /, *, lazy_exc=TypeError):
    def check(x, /):
        if not (x > z):raise lazy_exc()
    return check
def checkT__le(z, /, *, lazy_exc=TypeError):
    def check(x, /):
        if not (x <= z):raise lazy_exc()
    return check
def checkT__ge(z, /, *, lazy_exc=TypeError):
    def check(x, /):
        if not (x >= z):raise lazy_exc()
    return check
def checkT__ge_lt(m, M, /, *, lazy_exc=TypeError):
    def check(x, /):
        if not (m <= x < M):raise lazy_exc()
    return check

def checkT__len_(check, /):
    return dot[check, len]
def checkTT__len_(checkT, /):
    return dot[checkT__len_, checkT]

checkT__len_eq = checkTT__len_(checkT__eq)
checkT__len_ne = checkTT__len_(checkT__ne)
checkT__len_lt = checkTT__len_(checkT__lt)
checkT__len_le = checkTT__len_(checkT__le)
checkT__len_gt = checkTT__len_(checkT__gt)
checkT__len_ge = checkTT__len_(checkT__ge)
checkT__len_ge_lt = checkTT__len_(checkT__ge_lt)



#check_x = checkT__type_is(x)
check_bool = checkT__type_is(bool)
check_int = checkT__type_is(int)
check_uint = checkT__5pred(is_uint)
check_float = checkT__type_is(float)
check_complex = checkT__type_is(complex)

check_bytes = checkT__type_is(bytes)
check_str = checkT__type_is(str)
check_char = checkT__5pred(is_char)
check_tuple = checkT__type_is(tuple)
check_list = checkT__type_is(list)
check_frozenset = checkT__type_is(frozenset)
check_set = checkT__type_is(set)
check_dict = checkT__type_is(dict)

#check__is_x = checkT__is(x)
check__is_None = checkT__is(None)

check_callable = checkT__5pred(callable)

#[[
if 0:
    def checkT__tmay(check, /):
        return checkT__AND(check_tuple, checkT__pattern_tmay(check))

    def checkT__smay(check, /):
        return checkT__AND(check_str, checkT__if(bool, check))
    def checkT__may(check, /):
        return checkT__if_not(is_None, check)
    def checkT__imay(check, /):
        return checkT__AND(check_int, checkT__ge(-1), checkT__if_not(eqT(-1), check))
else:
    checkT__tmay = dot[[checkT__AND, check_tuple], checkT__pattern_tmay]
    checkT__smay = dot[[checkT__AND, check_str], [checkT__if, bool],]
    checkT__may = dot[[checkT__if_not, is_None],]
    checkT__imay = dot[[checkT__AND, check_int, checkT__ge(-1)], [checkT__if_not, eqT(-1)],]
#]]

#[[
if 0:
    def checkT__tuple(*checks, cls=tuple):
        return checkT__AND(checkT__type_is(cls), checkT__pattern_tuple(*checks))
    def checkT__list(check, /, *, cls=list):
        return checkT__AND(checkT__type_is(cls), checkT__pattern_list(check))
    def checkT__frozenset(check, /):
        return checkT__list(check, cls=frozenset)
    def checkT__set(check, /):
        return checkT__list(check, cls=set)
    def checkT__dict(check4item, /, *, cls=dict):
        return checkT__AND(checkT__type_is(cls), checkT__pattern_dict(check4item))
    def checkT__dictKV(check4key, check4value, /, *, cls=dict):
        return checkT__AND(checkT__type_is(cls), checkT__pattern_dictKV(check4key, check4value))
else:
    checkT__tuple = dot[[checkT__AND, check_tuple], checkT__pattern_tuple]
    checkT__list = dot[[checkT__AND, check_list], checkT__pattern_list]
    checkT__frozenset = dot[[checkT__AND, check_frozenset], checkT__pattern_list]
    checkT__set = dot[[checkT__AND, check_set], checkT__pattern_list]
    checkT__dict = dot[[checkT__AND, check_dict], checkT__pattern_dict]
    checkT__dictKV = dot[[checkT__AND, check_dict], checkT__pattern_dictKV]
    #TODO: checkT__record???
#]]


#]]]checkT:end

#[[[zzzwww:begin
#]]]zzzwww:end
#]]]main_body_src_code:end


#HHHHH
if __name__ == "__main__":
    from seed.func_tools.fmapT._xxxT__tiny import *
    from seed.func_tools.fmapT._xxxT__tiny import fmapT__dict, fmapT__list, fmapT__iter, fmapT__tuple, fmapT__tpls, fmapT__pairs, fmap_rngs2hex_repr
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #<BLANKLINE>
    #Traceback (most recent call last):

#HHHHH
#e ../../python3_src/seed/func_tools/fmapT/all_xxxT__tiny.py
#e ../../python3_src/seed/func_tools/fmapT/all_xxxT__common_utils.py
#from seed.func_tools.fmapT.all_xxxT__common_utils import (dot)
from seed.func_tools.fmapT._xxxT__tiny import (dot
,items_of
,keys_of
,values_of
,zip__same_len
,chain_from_iterable
,dot
,to_True
,to_False
,to_None
,to_Ellipsis
,to_NotImplemented
,xor5iter
,unpack_star_args_of
,pack_star_args_of
)

#e ../../python3_src/seed/func_tools/fmapT/fmapT__tiny.py
#from seed.func_tools.fmapT.fmapT__tiny import (dot)
from seed.func_tools.fmapT._xxxT__tiny import (dot
,fmapT__dict
,fmapT__list
,fmapT__iter
,fmapT__tuple
,fmapT__iter_tuple
,fmapT__tpls
,fmapT__pairs
,fmap_rngs2hex_repr
)

#e ../../python3_src/seed/func_tools/fmapT/predT__tiny.py
#from seed.func_tools.fmapT.predT__tiny import (dot)
from seed.func_tools.fmapT._xxxT__tiny import (dot
,not_
,is_True
,is_False
,is_None
,is_Ellipsis
,is_NotImplemented
,is_not_True
,is_not_False
,is_not_None
,is_not_Ellipsis
,is_not_NotImplemented
,fix_predicator
,allT__pattern_tuple
,anyT__pattern_tuple
,anyT__pattern_list
,allT__pattern_list
,anyT__pattern_dict
,allT__pattern_dict
,type_isT
,type_leT
,isinstanceT
,issubclassT
,isT
,is_notT
,eqT
,neT
,ltT
,gtT
,leT
,geT
,ge_ltT
,pred__True
,pred__False
,not_dotT
,predT__NOT
,predT__bool_op_
,predT__AND
,predT__NOT_AND
,predT__AND_NOT
,predT__NOT_AND_NOT
,predT__OR
,predT__NOT_OR
,predT__OR_NOT
,predT__NOT_OR_NOT
,predT__XOR
,predT__NOT_XOR
,predT__XOR_NOT
,predT__NOT_XOR_NOT
,is_frozenset
,is_set
,is_dict
,is_bool
,is_int
,is_uint
,is_float
,is_complex
,is_bytes
,is_str
,is_char
,is_tuple
,is_list
,predT__tuple
,predT__list
,predT__frozenset
,predT__set
,predT__dict
,predT_on_property
,len_eqT
,len_ltT
,len_geT
,len_ge_ltT
,is_empty
)

#e ../../python3_src/seed/func_tools/fmapT/filterT__tiny.py
#from seed.func_tools.fmapT.filterT__tiny import (dot)
from seed.func_tools.fmapT._xxxT__tiny import (dot
,mk__x2tmay__from__pred
,predicator_to_x2xs
,mk_x2xs__pred
,filterT_
,filterT
,filterT_fix
,filterT__tuple
,mk_filterT__5xs_2xs
,filterT__list
,filterT__set
,filterT__dict
)

#e ../../python3_src/seed/func_tools/fmapT/alterT__tiny.py
#from seed.func_tools.fmapT.alterT__tiny import (dot)
from seed.func_tools.fmapT._xxxT__tiny import (dot
,mk_alterT__5xs_2xs
,alterT__dict
,alterT__set
,alterT__list
,alterT__tuple__chain
,tuple2iter_tuples__product
)

#e ../../python3_src/seed/func_tools/fmapT/checkT__tiny.py
#from seed.func_tools.fmapT.checkT__tiny import (dot)
from seed.func_tools.fmapT._xxxT__tiny import (dot
,icheckT
,checkT__pattern_tuple
,checkT__pattern_list
,checkT__pattern_dict
,checkT__pattern_dictKV
,checkT__pattern_tmay
,checkT__5pred
,checkT__AND
,checkT__type_is
,checkT__type_le
,checkT__issubclass__any
,checkT__issubclass__all
,checkT__type_is__AND
,checkT__type_le__AND
,check__pass
,check__fail
,checkT__ifelse
,checkT__if
,checkT__if_not
,checkT__is
,checkT__eq
,checkT__ne
,checkT__lt
,checkT__gt
,checkT__le
,checkT__ge
,checkT__ge_lt
,checkT__len_eq
,checkT__len_ne
,checkT__len_lt
,checkT__len_le
,checkT__len_gt
,checkT__len_ge
,checkT__len_ge_lt
,check_bool
,check_int
,check_uint
,check_float
,check_complex
,check_bytes
,check_str
,check_char
,check_tuple
,check_list
,check_frozenset
,check_set
,check_dict
,check__is_None
,check_callable
,checkT__tmay
,checkT__smay
,checkT__may
,checkT__imay
,checkT__tuple
,checkT__list
,checkT__frozenset
,checkT__set
,checkT__dict
,checkT__dictKV
)
#HHHHH
