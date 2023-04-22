#__all__:goto
r'''[[[
e ../../python3_src/seed/helper/with4cleanup.py
see:
    seed.helper.with4cleanup
    seed.io.with4seekback





seed.helper.with4cleanup
py -m nn_ns.app.debug_cmd   seed.helper.with4cleanup
py -m nn_ns.app.adhoc_argparser__main__call8module   seed.helper.with4cleanup   @f
py -m nn_ns.app.doctest_cmd seed.helper.with4cleanup:__doc__ -v

>>> from seed.helper.with4cleanup import no_cleanup, with4cleanup_, with4cleanup__on_err_, with4cleanup__on_no_err, with4cleanup__on_exit, with4cleanup__never
>>> ls = []
>>> prepare = lambda:(ls, len(ls))
>>> def cleanup_on_err(internal_state, external_obj, /):
...     internal_state += [external_obj, 777]
>>> def cleanup_on_no_err(internal_state, external_obj, /):
...     internal_state += [external_obj, 888]
>>> def cleanup_on_exit(internal_state, external_obj, /):
...     internal_state += [external_obj, 999]

>>> with with4cleanup__never(0, prepare) as x:
...     x
0
>>> ls
[]
>>> with with4cleanup__never(0, prepare) as x:
...     raise DeprecationWarning
Traceback (most recent call last):
    ...
DeprecationWarning
>>> ls
[]
>>> with with4cleanup__on_err_(True, cleanup_on_err, 0, prepare) as x:
...     x
0
>>> ls
[]
>>> with with4cleanup__on_err_(True, cleanup_on_err, 0, prepare) as x:
...     raise DeprecationWarning
Traceback (most recent call last):
    ...
DeprecationWarning
>>> ls
[0, 777]
>>> with with4cleanup__on_no_err(cleanup_on_no_err, 0, prepare) as x:
...     raise DeprecationWarning
Traceback (most recent call last):
    ...
DeprecationWarning
>>> ls
[0, 777]
>>> with with4cleanup__on_no_err(cleanup_on_no_err, 0, prepare) as x:
...     x
2
>>> ls
[0, 777, 2, 888]
>>> with with4cleanup__on_exit(cleanup_on_exit, 0, prepare) as x:
...     x
4
>>> ls
[0, 777, 2, 888, 4, 999]
>>> with with4cleanup__on_exit(cleanup_on_exit, 0, prepare) as x:
...     raise DeprecationWarning
Traceback (most recent call last):
    ...
DeprecationWarning
>>> ls
[0, 777, 2, 888, 4, 999, 6, 999]


#]]]'''
__all__ = r'''
no_cleanup

with4cleanup_
    with4cleanup__on_err_
    with4cleanup__on_no_err
    with4cleanup__on_exit
    with4cleanup__never

'''.split()#'''
__all__



from seed.tiny_.mk_fdefault import mk_default__easy, mk_default, mk_default_or_raise
    #def mk_default__easy(*tmay_Nothing___or___args4mk_default_or_raise, mirror=False):
    #def mk_default(imay_xdefault_rank, xdefault, /, *args4xdefault):
    #def mk_default_or_raise(mirror_imay_xedefault_rank, xedefault, /, *args4xedefault, mirror:bool):
    #   imay_xdefault_ranks = (-3)-mirror_imay_xedefault_rank if mirror_imay_xedefault_rank < -1 else mirror_imay_xedefault_rank
    #   mirrored = (mirror_imay_xedefault_rank < -1) ^ bool(mirror)
    #


from seed.tiny import check_callable, check_type_is, ifNone
import contextlib

def no_cleanup(internal_state, external_obj, /): pass

@contextlib.contextmanager
def with4cleanup_(to_reraise:bool, may_cleanup_on_err, may_cleanup_on_no_err, may_cleanup_on_exit, /, *prepare5____tmay_Nothing___or___args4mk_default_or_raise, mirror=False):
    r'''
    (*tmay_Nothing___or___args4mk_default_or_raise, mirror=False)
        see:seed.tiny_.mk_fdefault::mk_default__easy
    prepare :: (internal_state, external_obj)
    cleanup_on_err, cleanup_on_no_err, cleanup_on_exit :: internal_state -> external_obj -> None
    '''#'''
    check_type_is(bool, to_reraise)

    cleanup_on_err = ifNone(may_cleanup_on_err, no_cleanup)
    cleanup_on_no_err = ifNone(may_cleanup_on_no_err, no_cleanup)
    cleanup_on_exit = ifNone(may_cleanup_on_exit, no_cleanup)

    check_callable(cleanup_on_err)
    check_callable(cleanup_on_no_err)
    check_callable(cleanup_on_exit)
    prepare = mk_default__easy(*prepare5____tmay_Nothing___or___args4mk_default_or_raise, mirror=mirror)
    (internal_state, external_obj) = prepare; del prepare
    try:
        yield external_obj
    except:
        cleanup_on_err(internal_state, external_obj)
        if to_reraise:
            raise
    else:
        cleanup_on_no_err(internal_state, external_obj)
    finally:
        cleanup_on_exit(internal_state, external_obj)
    return



#@contextlib.contextmanager
def with4cleanup__on_err_(to_reraise:bool, may_cleanup_on_err, /, *prepare5____tmay_Nothing___or___args4mk_default_or_raise, mirror=False):
    'see:with4cleanup_'
    return with4cleanup_(to_reraise, may_cleanup_on_err, None, None, *prepare5____tmay_Nothing___or___args4mk_default_or_raise, mirror=mirror)

#@contextlib.contextmanager
def with4cleanup__on_no_err(may_cleanup_on_no_err, /, *prepare5____tmay_Nothing___or___args4mk_default_or_raise, mirror=False):
    'see:with4cleanup_'
    return with4cleanup_(True, None, may_cleanup_on_no_err, None, *prepare5____tmay_Nothing___or___args4mk_default_or_raise, mirror=mirror)


#@contextlib.contextmanager
def with4cleanup__on_exit(may_cleanup_on_exit, /, *prepare5____tmay_Nothing___or___args4mk_default_or_raise, mirror=False):
    'see:with4cleanup_'
    return with4cleanup_(True, None, None, may_cleanup_on_exit, *prepare5____tmay_Nothing___or___args4mk_default_or_raise, mirror=mirror)

#@contextlib.contextmanager
def with4cleanup__never(*prepare5____tmay_Nothing___or___args4mk_default_or_raise, mirror=False):
    'see:with4cleanup_'
    return with4cleanup_(True, None, None, None, *prepare5____tmay_Nothing___or___args4mk_default_or_raise, mirror=mirror)

from seed.helper.with4cleanup import no_cleanup, with4cleanup_, with4cleanup__on_err_, with4cleanup__on_no_err, with4cleanup__on_exit, with4cleanup__never
from seed.helper.with4cleanup import *
