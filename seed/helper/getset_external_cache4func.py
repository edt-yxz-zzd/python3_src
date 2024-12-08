#__all__:goto
r'''[[[
e ../../python3_src/seed/helper/getset_external_cache4func.py
extract from:
    view ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/IRecognizerLLoo.py

seed.helper.getset_external_cache4func
py -m nn_ns.app.debug_cmd   seed.helper.getset_external_cache4func -x
py -m nn_ns.app.doctest_cmd seed.helper.getset_external_cache4func:__doc__ -ht
py_adhoc_call   seed.helper.getset_external_cache4func   @f
#]]]'''
__all__ = r'''
getset_external_cache4func
    getset_external_cache4method
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...

from types import FunctionType as Func, MethodType as Meth
from weakref import ref as wref_, WeakKeyDictionary as WkeyD# WeakValueDictionary as WvalD
from seed.tiny_.check import check_type_is, check_int_ge_lt
___end_mark_of_excluded_global_names__0___ = ...

def getset_external_cache4method(get_vs_set_vs_set_ex, mf, /, *weakable_args):
    'precondition:[mf/MethodType == (f/FunctionType + weakable_selfs)] => ' \
        '(0|1|2) -> mf/MethodType/((*weakable_args)->r) -> (*weakable_args) -> ((r|^KeyError)|r|(is_new,r))'
    check_int_ge_lt(0, 3, case:=get_vs_set_vs_set_ex)
    args = []
    while type(mf) is Meth:
        sf = mf.__self__
        wref_(sf)
            #check weakable
        args.append(sf)
        mf = mf.__func__
    f = mf
    check_type_is(Func, f)
    args.reverse()
    return getset_external_cache4func(case, f, *args, *weakable_args)

def getset_external_cache4func(get_vs_set_vs_set_ex, f, /, *weakable_args, __depth=0):
    '(0|1|2) -> f/FunctionType/((*weakable_args)->r) -> (*weakable_args) -> ((r|^KeyError)|r|(is_new,r))' \
        ' # (get_only|set_if_default_then_get|set_if_default_then_get_ex)'
    if not 0 <= __depth < 2:raise Exception(getset_external_cache4func, get_vs_set_vs_set_ex, f, *weakable_args)
    check_int_ge_lt(0, 3, case:=get_vs_set_vs_set_ex)
    check_type_is(Func, f)
    #xxx:if not weakable_args:raise TypeError
    d = vars(f)
    k = getset_external_cache4func
    if not k in d:
        check_type_is(Func, f)
        d[k] = WkeyD()
    wd0 = wd = d[k]
    check_type_is(WkeyD, wd)
    it = map(wref_, weakable_args)
    #bug:it = iter([*it])
    #   fail:wref_(wref_(...))
    [*it]
        #check weakable
    it = iter(weakable_args)
    if case == 0:
        for w in it:
            wd = wd[w]
                # ^KeyError
        else:
            r = wd
            return r
    try:
        for w in it:
            wd = wd[w]
                # ^KeyError
    except KeyError:
        pass
    else:
        r = wd
        if case == 1:
            return r
        if case == 2:
            return (is_new:=False, r)
        raise 000-case
    wd, w, it
        # !! KeyError => [w existed]
    # [w may be last]
    # [wd is not r]
    for _w in it:
        # [w is not last]
        if 0:
            #why? bug:『wd = wd[w] = WkeyD()』
            wd = wd[w] = WkeyD()
        else:
            tmp = WkeyD()
            wd[w] = tmp
            wd = tmp
            del tmp
        #if 0b0001:print_err({**wd0})
        # [wd is not r]
        w = _w
        # [w may be last]
        # [wd is not r]
    # [w is last]
    # [wd is not r]
    wd, w
    try:
        r = wd[w]
    except KeyError:
        is_new = True
    else:
        is_new = False
        if case == 1:
            return r
        if case == 2:
            return (is_new, r)
        raise 000-case
    r = wd[w] = f(*weakable_args)
    #if 0b0001:print_err({**wd0})
    rx = getset_external_cache4func(case, f, *weakable_args, __depth=__depth+1)
    if case == 1:
        assert rx is r
        return rx
    if case == 2:
        (_is_new, _r) = rx
        assert not _is_new
        assert _r is r
        return (is_new, r)
    raise 000-case


__all__
from seed.helper.getset_external_cache4func import getset_external_cache4func, getset_external_cache4method
from seed.helper.getset_external_cache4func import *
