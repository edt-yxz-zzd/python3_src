#__all__:goto
r'''[[[
e ../../python3_src/seed/helper/lazy_import__func7dict.py
vs:
    view ../../python3_src/seed/helper/lazy_import__func.py
        complex:circle import seed.tiny_.check
        complex:__call__,__getitem__,__getattribute__,__pos__...
    view ../../python3_src/seed/helper/lazy_import__func7dict.py
        simplified:without import anything
        simplified:only:__call__

seed.helper.lazy_import__func7dict
py -m nn_ns.app.debug_cmd   seed.helper.lazy_import__func7dict -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.helper.lazy_import__func7dict:__doc__ -ht # -ff -df
#######

[[
usage:
from seed.helper.lazy_import__func7dict import lazy_import__funcs7dict_
#lazy_import__funcs7dict_(globals(), ...)
#lazy_import__funcs7dict_(locals(), ...)
(check_type_is, check_int_ge, _ifNone) = lazy_import__funcs7dict_(__name__, 'seed.tiny_.check',  'check_type_is, check_int_ge      ifNone:_ifNone')
]]


'#'; __doc__ = r'#'
>>> d = {}
>>> check_type_is = lazy_import__func7dict_(d, 'seed.tiny_.check', 'check_type_is')
>>> check_type_is
_LazyImportFunc6Dict({}, 'seed.tiny_.check', 'check_type_is', '')
>>> d
{}
>>> check_type_is(str, '444')
>>> d  #doctest: +ELLIPSIS
{'check_type_is': <function check_type_is at 0x...>}
>>> check_type_is  #doctest: +ELLIPSIS
_LazyImportFunc6Dict({'check_type_is': <function check_type_is at 0x...>}, 'seed.tiny_.check', 'check_type_is', '')
>>> check_type_is(int, 444)


>>> d = {}
>>> check_type_is = lazy_import__func7dict_(d, 'seed.tiny_.check', 'check_type_is', inject=True)
>>> d
{'check_type_is': _LazyImportFunc6Dict({...}, 'seed.tiny_.check', 'check_type_is', '')}
>>> check_type_is(int, 444)
>>> d  #doctest: +ELLIPSIS
{'check_type_is': <function check_type_is at 0x...>}



>>> d = {}
>>> (check_type_is, check_int_ge) = lazy_import__funcs7dict_(d, 'seed.tiny_.check', 'check_type_is,,,,,,,,  check_int_ge', inject=True)
>>> d
{'check_type_is': _LazyImportFunc6Dict({...}, 'seed.tiny_.check', 'check_type_is', ''), 'check_int_ge': _LazyImportFunc6Dict({...}, 'seed.tiny_.check', 'check_int_ge', '')}
>>> check_type_is(int, 444)
>>> d  #doctest: +ELLIPSIS
{'check_type_is': <function check_type_is at 0x...>, 'check_int_ge': _LazyImportFunc6Dict({...}, 'seed.tiny_.check', 'check_int_ge', '')}
>>> check_int_ge(0, 444)
>>> d  #doctest: +ELLIPSIS
{'check_type_is': <function check_type_is at 0x...>, 'check_int_ge': <function check_int_ge at 0x...>}






>>> d = {}
>>> (_ifNone, _ifNonef) = lazy_import__funcs7dict_(d, 'seed.helper.ifNone', 'ifNone:_ifNone,,,,,,,,  ifNonef:_ifNonef', inject=True)
>>> d
{'_ifNone': _LazyImportFunc6Dict({...}, 'seed.helper.ifNone', 'ifNone:_ifNone', ''), '_ifNonef': _LazyImportFunc6Dict({...}, 'seed.helper.ifNone', 'ifNonef:_ifNonef', '')}
>>> _ifNone(666, 999)
666
>>> _ifNone(None, 999)
999
>>> _ifNonef(None, lambda:999)
999
>>> _ifNonef(666, lambda:999)
666
>>> d  #doctest: +ELLIPSIS
{'_ifNone': <function ifNone at 0x...>, '_ifNonef': <function ifNonef at 0x...>}











py_adhoc_call   seed.helper.lazy_import__func7dict   @f
]]]'''#'''
__all__ = r'''
lazy_import__func7dict_
lazy_import__funcs7dict_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from functools import cached_property
___end_mark_of_excluded_global_names__0___ = ...

def _import_module(*args, **kwds):
    global _import_module
    from importlib import import_module as _import_module
    return _import_module(*args, **kwds)

def _get_func(sf, /):
    try:
        return sf._f
    except AttributeError:
        pass
    d = sf._d
    nm7dst = sf._nm7dst
    if not d.get(nm7dst, sf) is sf:raise TypeError(nm7dst, sf)

    qnm4mdl7src = sf._qnm4mdl7src
    nm7src = sf._nm7src
    mdl7src = _import_module(qnm4mdl7src)
    f = getattr(mdl7src, nm7src)
    d[nm7dst] = f
    sf._f = f
    return _get_func(sf)
def _d5or_qnm4mdl(d_or_qnm4mdl, /):
    if type(d_or_qnm4mdl) is str:
        qnm4mdl7dst = d_or_qnm4mdl
        mdl7dst = _import_module(qnm4mdl7dst)
        d = vars(mdl7dst)
    else:
        d = d_or_qnm4mdl
    d
    d.keys()
    return d
class _LazyImportFunc6Dict:
    def __init__(sf, d_or_qnm4mdl, qnm4mdl7src, nm7src, smay_nm7dst, /):
        assert type(qnm4mdl7src) is str
        assert type(nm7src) is str
        assert type(smay_nm7dst) is str
        sf._args4repr = (d_or_qnm4mdl, qnm4mdl7src, nm7src, smay_nm7dst)
        #nm7dst = if_smay_(smay_nm7dst, -1, nm7src)
        nm7dst = smay_nm7dst if smay_nm7dst else nm7src
        if ':' in nm7src:
            assert not smay_nm7dst
            (nm7src, nm7dst) = nm7src.split(':')

        assert type(nm7dst) is str
        sf._dXq = d_or_qnm4mdl
        #d = _d5or_qnm4mdl(d_or_qnm4mdl)
        #sf._d = d
        sf._qnm4mdl7src = qnm4mdl7src
        sf._nm7src = nm7src
        sf._nm7dst = nm7dst
    @cached_property
    def _d(sf, /):
        return _d5or_qnm4mdl(sf._dXq)
    def __call__(sf, /, *args, **kwds):
        return _get_func(sf)(*args, **kwds)
    def __repr__(sf, /):
        return f'_LazyImportFunc6Dict{sf._args4repr}'
def lazy_import__func7dict_(d_or_qnm4mdl, qnm4mdl7src, nm7src, smay_nm7dst='', /, *, inject=False):
    f = _LazyImportFunc6Dict(d_or_qnm4mdl, qnm4mdl7src, nm7src, smay_nm7dst)
    if inject:
        f._d.setdefault(f._nm7dst, f)
    return f
def lazy_import__funcs7dict_(d_or_qnm4mdl, qnm4mdl7src, nms7src, /, *, inject=False):
    if type(nms7src) is str:
        nms7src = nms7src.replace(',', ' ').split()
    #d = _d5or_qnm4mdl(d_or_qnm4mdl)
    #   repr...
    return tuple(lazy_import__func7dict_(d_or_qnm4mdl, qnm4mdl7src, nm7src, inject=inject) for nm7src in nms7src)

__all__
from seed.helper.lazy_import__func7dict import lazy_import__func7dict_, lazy_import__funcs7dict_
from seed.helper.lazy_import__func7dict import *
