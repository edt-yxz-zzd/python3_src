#__all__:goto
r'''[[[
e ../../python3_src/seed/helper/lazy_import__func7worker4funcss.py

seed.helper.lazy_import__func7worker4funcss
py -m nn_ns.app.debug_cmd   seed.helper.lazy_import__func7worker4funcss -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.helper.lazy_import__func7worker4funcss:__doc__ -ht # -ff -df

[[
]]

py_adhoc_call   seed.helper.lazy_import__func7worker4funcss   @f
]]]'''#'''
__all__ = r'''
worker4lazy_import4funcss_
check_kwds4worker
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_
#def lazy_import4func_(qnm4mdl8src, qnm4func8src, smay_qnm4mdl8dst='', smay_nm4func8dst='', /):
#def lazy_import4funcs_(qnm4mdl8src, xqnms4func8src, smay_qnm4mdl8dst='', /):
lazy_import4funcs_('seed.debug.print_err', 'print_err', __name__)
if 0:from seed.debug.print_err import print_err, print_ferr

#.from itertools import islice
from seed.tiny_.check import check_type_is, check_int_ge
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







#.def worker4lazy_import4funcss_(data4import_stmts4func8src, smay_qnm4mdl8dst, /):
#.    # precondition:[halfway:=True]
#.    for (qnm4mdl8src, as_ls) in data4import_stmts4func8src:
#.        xqnms4func8src = as_ls
#.            # !! [halfway:=True]
#.        nm_pairs = _parse__as_ls__AbbrStmt_(as_ls, halfway=False)
#.        lazy_import4funcs_(qnm4mdl8src, xqnms4func8src, smay_qnm4mdl8dst)
#.
def worker4lazy_import4funcss_(mdl__nm_pairs__pairs, smay_qnm4mdl8dst, /, *, to_show_nmss4func8dst=False, to_return_nmss4func8dst=False):
    r'''[[[
    [mdl__nm_pairs__pairs :: Iter (qnm4mdl8src, nm_pairs)]
    [nm_pairs::[(qnm,nm)|(nm,smay_nm)]]
    #]]]'''#'''
    #, **kwds4worker
    # precondition:[halfway:=False]
    #mdl__nm_pairs__pairs = data4import_stmts4func8src
        # !! [halfway:=False]
    check_type_is(bool, to_show_nmss4func8dst)
    check_type_is(bool, to_return_nmss4func8dst)
    check_type_is(str, smay_qnm4mdl8dst)
    nmss4func8dst = []
    rss = []
    for (qnm4mdl8src, nm_pairs) in mdl__nm_pairs__pairs:
        # nm_pairs::[(qnm,nm)|(nm,smay_nm)]
        xqnms4func8src = ','.join((f'{nm}:{smay_nm}' if smay_nm else nm) for nm, smay_nm in nm_pairs)
        nms4func8dst = [(smay_nm if smay_nm else nm) for nm, smay_nm in nm_pairs]
        rs = lazy_import4funcs_(qnm4mdl8src, xqnms4func8src, smay_qnm4mdl8dst)
        rss.append(rs)
        nmss4func8dst.append(nms4func8dst)
    rss
    nmss4func8dst
    nmss4func8dst__str = _str8list_(map(_str8list_, nmss4func8dst))
    if to_show_nmss4func8dst:
        print_err(nmss4func8dst__str)
    if to_return_nmss4func8dst:
        return (rss, nmss4func8dst, nmss4func8dst__str)
    return rss
def _str8list_(ss, /):
    r'[str] -> str # fmt=regex"\[({s}(, {s})*)?\]"'
    s = ', '.join(ss)
    return f'[{s!s}]'


def _check_kwds4worker(*, to_show_nmss4func8dst=False, to_return_nmss4func8dst=False):
    check_type_is(bool, to_show_nmss4func8dst)
    check_type_is(bool, to_return_nmss4func8dst)
def check_kwds4worker(kwds4worker, /):
    _check_kwds4worker(**kwds4worker)


__all__
from seed.helper.lazy_import__func7worker4funcss import worker4lazy_import4funcss_, check_kwds4worker
from seed.helper.lazy_import__func7worker4funcss import *
