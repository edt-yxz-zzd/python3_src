#__all__:goto
r'''[[[
e ../../python3_src/seed/helper/if_is_.py

seed.helper.if_is_
py -m nn_ns.app.debug_cmd   seed.helper.if_is_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.helper.if_is_:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>> ifNone(666, 999)
666
>>> ifNone(None, 999)
999
>>> ifNonef(666, lambda:999)
666
>>> ifNonef(None, lambda:999)
999


>>> if_is_(..., 666, -1, 999)
666
>>> if_is_(..., ..., -1, 999)
999
>>> if_is_(..., 666, 0, lambda:999)
666
>>> if_is_(..., ..., 0, lambda:999)
999
>>> if_is_(..., ..., 2, lambda x,y:(x,y,999), 77, 88)
(77, 88, 999)

>>> if_eq_(444, 666, -1, 999)
666
>>> if_eq_(444, 444, -1, 999)
999
>>> if_eq_(444, 666, 0, lambda:999)
666
>>> if_eq_(444, 444, 0, lambda:999)
999
>>> if_eq_(444, 444, 2, lambda x,y:(x,y,999), 77, 88)
(77, 88, 999)

>>> if_in_([222, 444], 666, -1, 999)
666
>>> if_in_([222, 444], 444, -1, 999)
999
>>> if_in_([222, 444], 666, 0, lambda:999)
666
>>> if_in_([222, 444], 444, 0, lambda:999)
999
>>> if_in_([222, 444], 444, 2, lambda x,y:(x,y,999), 77, 88)
(77, 88, 999)










if_tmay_, if_imay_, if_smay_, if_nmay_, if_emay_, if_True_, if_False_, if_NotImplemented_
>>> if_tmay_((666,), -1, 999)
666
>>> if_tmay_((), -1, 999)
999
>>> if_tmay_((666,), 0, lambda:999)
666
>>> if_tmay_((), 0, lambda:999)
999
>>> if_tmay_((), 2, lambda x,y:(x,y,999), 77, 88)
(77, 88, 999)

>>> if_imay_(666, -1, 999)
666
>>> if_imay_(-1, -1, 999)
999
>>> if_imay_(666, 0, lambda:999)
666
>>> if_imay_(-1, 0, lambda:999)
999
>>> if_imay_(-1, 2, lambda x,y:(x,y,999), 77, 88)
(77, 88, 999)

>>> if_smay_('aaa', -1, 999)
'aaa'
>>> if_smay_('', -1, 999)
999
>>> if_smay_('aaa', 0, lambda:999)
'aaa'
>>> if_smay_('', 0, lambda:999)
999
>>> if_smay_('', 2, lambda x,y:(x,y,999), 77, 88)
(77, 88, 999)

>>> if_nmay_(666, -1, 999)
666
>>> if_nmay_(None, -1, 999)
999
>>> if_nmay_(666, 0, lambda:999)
666
>>> if_nmay_(None, 0, lambda:999)
999
>>> if_nmay_(None, 2, lambda x,y:(x,y,999), 77, 88)
(77, 88, 999)

>>> if_emay_(666, -1, 999)
666
>>> if_emay_(..., -1, 999)
999
>>> if_emay_(666, 0, lambda:999)
666
>>> if_emay_(..., 0, lambda:999)
999
>>> if_emay_(..., 2, lambda x,y:(x,y,999), 77, 88)
(77, 88, 999)

>>> if_True_(666, -1, 999)
666
>>> if_True_(True, -1, 999)
999
>>> if_True_(666, 0, lambda:999)
666
>>> if_True_(True, 0, lambda:999)
999
>>> if_True_(True, 2, lambda x,y:(x,y,999), 77, 88)
(77, 88, 999)
>>> if_True_(1, -1, 999)
1
>>> if_True_(0, -1, 999)
0

>>> if_False_(666, -1, 999)
666
>>> if_False_(False, -1, 999)
999
>>> if_False_(666, 0, lambda:999)
666
>>> if_False_(False, 0, lambda:999)
999
>>> if_False_(False, 2, lambda x,y:(x,y,999), 77, 88)
(77, 88, 999)
>>> if_False_(1, -1, 999)
1
>>> if_False_(0, -1, 999)
0


>>> if_NotImplemented_(666, -1, 999)
666
>>> if_NotImplemented_(NotImplemented, -1, 999)
999
>>> if_NotImplemented_(666, 0, lambda:999)
666
>>> if_NotImplemented_(NotImplemented, 0, lambda:999)
999
>>> if_NotImplemented_(NotImplemented, 2, lambda x,y:(x,y,999), 77, 88)
(77, 88, 999)


py_adhoc_call   seed.helper.if_is_   @f
]]]'''#'''
__all__ = r'''
ifNone
ifNonef
if_is_
if_eq_
if_in_

if_tmay_
if_imay_
if_smay_
if_nmay_
if_emay_
if_True_
if_False_
if_NotImplemented_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    #from functools import singledispatch
    from seed.tiny_.check import check_type_is, check_int_ge
    from seed.tiny_.mk_fdefault import mk_default
        #def mk_default(imay_xdefault_rank, xdefault, /,*args4xdefault):
___end_mark_of_excluded_global_names__0___ = ...

from seed.helper.ifNone import ifNone, ifNonef
def if_is_(expected, obj, imay_xdefault_rank, xdefault, /, *args4xdefault):
    if obj is expected: return mk_default(imay_xdefault_rank, xdefault, *args4xdefault)
    return obj
def if_eq_(expected, obj, imay_xdefault_rank, xdefault, /, *args4xdefault):
    if obj == expected: return mk_default(imay_xdefault_rank, xdefault, *args4xdefault)
    return obj
def if_in_(expected, obj, imay_xdefault_rank, xdefault, /, *args4xdefault):
    if obj in expected: return mk_default(imay_xdefault_rank, xdefault, *args4xdefault)
    return obj

def if_tmay_(tmay_obj, imay_xdefault_rank, xdefault, /, *args4xdefault):
    #check_type_is(tuple, obj)
    match tmay_obj:
        case ():
            return mk_default(imay_xdefault_rank, xdefault, *args4xdefault)
        case (obj,):
            return obj
        #
    raise TypeError(tmay_obj)

def if_imay_(obj, imay_xdefault_rank, xdefault, /, *args4xdefault):
    check_int_ge(-1, obj)
    return if_eq_(-1, obj, imay_xdefault_rank, xdefault, *args4xdefault)
def if_smay_(obj, imay_xdefault_rank, xdefault, /, *args4xdefault):
    check_type_is(str, obj)
    return if_eq_('', obj, imay_xdefault_rank, xdefault, *args4xdefault)
def if_nmay_(obj, imay_xdefault_rank, xdefault, /, *args4xdefault):
    return if_is_(None, obj, imay_xdefault_rank, xdefault, *args4xdefault)
def if_emay_(obj, imay_xdefault_rank, xdefault, /, *args4xdefault):
    return if_is_(..., obj, imay_xdefault_rank, xdefault, *args4xdefault)
def if_True_(obj, imay_xdefault_rank, xdefault, /, *args4xdefault):
    return if_is_(True, obj, imay_xdefault_rank, xdefault, *args4xdefault)
def if_False_(obj, imay_xdefault_rank, xdefault, /, *args4xdefault):
    return if_is_(False, obj, imay_xdefault_rank, xdefault, *args4xdefault)

def if_NotImplemented_(obj, imay_xdefault_rank, xdefault, /, *args4xdefault):
    return if_is_(NotImplemented, obj, imay_xdefault_rank, xdefault, *args4xdefault)


__all__
from seed.helper.if_is_ import ifNone, ifNonef
from seed.helper.if_is_ import if_is_, if_eq_, if_in_
    # def if_is_(expected, obj, imay_xdefault_rank, xdefault, /, *args4xdefault):
from seed.helper.if_is_ import if_tmay_, if_imay_, if_smay_, if_nmay_, if_emay_, if_True_, if_False_, if_NotImplemented_
    #def if_tmay_(tmay_obj, imay_xdefault_rank, xdefault, /, *args4xdefault):

from seed.helper.if_is_ import *
