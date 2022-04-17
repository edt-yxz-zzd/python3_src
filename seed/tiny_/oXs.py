#__all__:goto
#main_body_src_code:goto
#HHHHH
#[[[__doc__:begin
r'''
seed.tiny_.oXs
py -m    seed.tiny_.oXs
py -m nn_ns.app.debug_cmd   seed.tiny_.oXs


e ../../python3_src/seed/tiny_/oXs.py
    py -m nn_ns.app.mk_py_template -o ../../python3_src/seed/tiny_/oXs.py

from seed.tiny_.oXs import eat_iter as _eat_iter, check_intXs_between, check_uintXs_lt, check_uintXs, fold__objXtuple, fold__intXiter, intXiter2intXtuple


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
__all__ = '''
    eat_iter
    check_intXs_between
    check_uintXs_lt
    check_uintXs
    fold__objXtuple
    fold__intXiter
    intXiter2intXtuple
    '''.split()

#################################
#HHHHH
___begin_mark_of_excluded_global_names__0___ = ...

from seed.tiny_.check import check_uint, check_int_ge_lt as check_int_between
if 1:
    from seed.tiny import echo, mk_tuple
else:
    from seed.helper.Echo import echo
    from seed.tiny_.containers import mk_tuple

___end_mark_of_excluded_global_names__0___ = ...

#HHHHH
#[[[main_body_src_code:begin
#zzzwww:goto

#[[[zzzwww:begin


check_int_between
check_uint

def _eat_iter(it:'iter None', /):
    for _ in it:pass
eat_iter = _eat_iter


def check_intXs_between(m, M, iXs, /):
    'IntXs<m,M> = int<m,M> | tuple<IntXs<m,M> >'
    def f4i(i, /):
        check_int_between(m, M, i)
    f4s = _eat_iter
    fold__objXtuple(f4i, f4s, iXs)
def check_uintXs_lt(M, uXs, /):
    'UIntXs%M = uint%M | tuple<UIntXs%M>'
    check_intXs_between(0, M, uXs)
def check_uintXs(uXs, /):
    'UIntXs = uint | tuple<UIntXs>'
    f4u = check_uint
    f4s = _eat_iter
    fold__objXtuple(f4u, f4s, uXs)
def fold__objXtuple(f4o, f4s, oXs, /):
    '(obj->r) -> (Iter r -> r) -> objXs -> r   #objXs = obj | tuple<objXs>'

    def recur(oXs, /):
        if type(oXs) is tuple:
            oXss = oXs
            r = f4s(map(recur, oXss))
        else:
            o = oXs
            r = f4o(o)
        return r
    return recur(oXs)
def fold__intXiter(f4i, f4s, iXs, /):
    '(int->r) -> (Iter r -> r) ->  PseudoIntXs -> r   #PseudoIntXs = int | Iterable PseudoIntXs'

    def recur(iXs, /):
        if type(iXs) is int:
            i = iXs
            r = f4i(i)
        else:
            iXss = iXs
            r = f4s(map(recur, iXss))
        return r
    return recur(iXs)
def intXiter2intXtuple(iXit, /):
    'intXiter -> intXtuple'
    return fold__intXiter(echo, mk_tuple, iXit)

#]]]zzzwww:end
#]]]main_body_src_code:end


#HHHHH
if __name__ == "__main__":
    from seed.tiny_.oXs import *
    from seed.tiny_.oXs import eat_iter as _eat_iter, check_intXs_between, check_uintXs_lt, check_uintXs, fold__objXtuple, fold__intXiter, intXiter2intXtuple
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #<BLANKLINE>
    #Traceback (most recent call last):


