#__all__:goto
r'''[[[
e ../../python3_src/seed/helper/context4overwrite_module_attrs.py

seed.helper.context4overwrite_module_attrs
py -m nn_ns.app.debug_cmd   seed.helper.context4overwrite_module_attrs -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.helper.context4overwrite_module_attrs:__doc__ -ht # -ff -df
#######

[[
come_from:
view ../../python3_src/seed/helper/import_stmt_context.py
    _Ctx4import_stmts__ver2
]]


'#'; __doc__ = r'#'
>>> import builtins
>>> (bin(8), hex(8))
('0b1000', '0x8')
>>> with mk_context4overwrite_module_attrs_(True, builtins, bin=hex, hex=bin):
...     (bin(8), hex(8))
('0x8', '0b1000')
>>> (bin(8), hex(8))
('0b1000', '0x8')
>>> with mk_context4overwrite_module_attrs_(False, vars(builtins), bin=hex, hex=bin):
...     (bin(8), hex(8))
('0x8', '0b1000')
>>> (bin(8), hex(8))
('0b1000', '0x8')

>>> with mk_context4overwrite_module_attrs_(..., builtins, bin=hex, hex=bin):
...     (bin(8), hex(8))
('0x8', '0b1000')
>>> (bin(8), hex(8))
('0b1000', '0x8')
>>> with mk_context4overwrite_module_attrs_(..., vars(builtins), bin=hex, hex=bin):
...     (bin(8), hex(8))
('0x8', '0b1000')
>>> (bin(8), hex(8))
('0b1000', '0x8')
>>> with mk_context4overwrite_module_attrs_(..., __builtins__, bin=hex, hex=bin):
...     (bin(8), hex(8))
('0x8', '0b1000')
>>> (bin(8), hex(8))
('0b1000', '0x8')




py_adhoc_call   seed.helper.context4overwrite_module_attrs   @f
]]]'''#'''
__all__ = r'''
mk_context4overwrite_module_attrs_
    Context4overwrite_module_attrs
    BadUsage

is_same_namespace_
    restore2mdl_or_vars_
        setattrs_
        setitems_
    extract5mdl_or_vars_
        getattrs_
        getitems_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.tiny_.check import check_type_is, check_int_ge
#.from seed.debug.print_err import print_err
___end_mark_of_excluded_global_names__0___ = ...


class BadUsage(Exception):pass

def setattrs_(obj, nm2v, /):
    for nm, v in nm2v.items():
        setattr(obj, nm, v)
def setitems_(d, k2v, /):
    for k, v in k2v.items():
        d[k] = v
def restore2mdl_or_vars_(whether_mdl, mdl_or_vars, nm2v, /):
    if whether_mdl:
        mdl = mdl_or_vars
        setattrs_(mdl, nm2v)
    else:
        vars4mdl = mdl_or_vars
        setitems_(vars4mdl, nm2v)
    return


def getattrs_(obj, nms, /):
    'x -> {nm} -> {nm:v}|^AttributeError'
    return {nm:getattr(obj, nm) for nm in nms}
def getitems_(d, ks, /):
    '{k:v} -> {k} -> {k:v}|^KeyError|^TypeError'
    # ^LookupError
    return {k:d[k] for k in ks}
def extract5mdl_or_vars_(whether_mdl, mdl_or_vars, nms, /):
    if whether_mdl:
        mdl = mdl_or_vars
        nm2v = getattrs_(mdl, nms)
    else:
        vars4mdl = mdl_or_vars
        nm2v = getitems_(vars4mdl, nms)
    return nm2v
def is_same_namespace_(lhs_nm2v, rhs_nm2v, /):
    return len(lhs_nm2v) == len(rhs_nm2v) and lhs_nm2v.keys() == rhs_nm2v.keys() and all(lhs_nm2v[nm] is rhs_nm2v[nm] for nm in lhs_nm2v)

class Context4overwrite_module_attrs:
    def __init__(sf, emay_whether_mdl, mdl_or_vars, /, **kwds7new_attrs):
        nm2new_v = kwds7new_attrs
        nms7using = nm2new_v.keys()
        if emay_whether_mdl is ...:
            try:
                nm2old_v = getattrs_(mdl_or_vars, nms7using)
            except AttributeError as e0:
                try:
                    nm2old_v = getitems_(mdl_or_vars, nms7using)
                except (KeyError, TypeError) as e1:
                    raise ExceptionGroup('not module_obj or its vars __dict__', [e0, e1, TypeError(mdl_or_vars, sorted(nms7using))])
                whether_mdl = False
            else:
                whether_mdl = True
            whether_mdl
            nm2old_v
        else:
            whether_mdl = emay_whether_mdl
            check_type_is(bool, whether_mdl)
            if whether_mdl:
                mdl = mdl_or_vars
                nm2old_v = getattrs_(mdl_or_vars, nms7using)
            else:
                vars4mdl = mdl_or_vars
                nm2old_v = getitems_(mdl_or_vars, nms7using)
            nm2old_v
            whether_mdl
        whether_mdl
        mdl_or_vars
        nm2old_v
        nm2new_v

        restore2mdl_or_vars_(whether_mdl, mdl_or_vars, nm2old_v)
        _nm2old_v = extract5mdl_or_vars_(whether_mdl, mdl_or_vars, nms7using)
        if not is_same_namespace_(_nm2old_v, nm2old_v):raise BadUsage('unknown err')


        sf._args = (whether_mdl, mdl_or_vars, nm2old_v, nm2new_v)

    def __enter__(sf, /):
        (whether_mdl, mdl_or_vars, nm2old_v, nm2new_v) = sf._args
        nms7using = nm2new_v.keys()

        _nm2old_v = extract5mdl_or_vars_(whether_mdl, mdl_or_vars, nms7using)
        if not is_same_namespace_(_nm2old_v, nm2old_v):raise BadUsage('reenter')
        restore2mdl_or_vars_(whether_mdl, mdl_or_vars, nm2new_v)

        try:
            _nm2new_v = extract5mdl_or_vars_(whether_mdl, mdl_or_vars, nms7using)
            if not is_same_namespace_(_nm2new_v, nm2new_v):raise BadUsage('unknown err')
        except:
            restore2mdl_or_vars_(whether_mdl, mdl_or_vars, nm2old_v)

    def __exit__(sf, /, *exc_info):
        (whether_mdl, mdl_or_vars, nm2old_v, nm2new_v) = sf._args
        nms7using = nm2new_v.keys()

        try:
            _nm2new_v = extract5mdl_or_vars_(whether_mdl, mdl_or_vars, nms7using)
            if not is_same_namespace_(_nm2new_v, nm2new_v):raise BadUsage('unknown err')
        finally:
            restore2mdl_or_vars_(whether_mdl, mdl_or_vars, nm2old_v)

        _nm2old_v = extract5mdl_or_vars_(whether_mdl, mdl_or_vars, nms7using)
        if not is_same_namespace_(_nm2old_v, nm2old_v):raise BadUsage('unknown err')
        return False



def mk_context4overwrite_module_attrs_(emay_whether_mdl, mdl_or_vars, /, **kwds7new_attrs):
    return Context4overwrite_module_attrs(emay_whether_mdl, mdl_or_vars, **kwds7new_attrs)

__all__
from seed.helper.context4overwrite_module_attrs import mk_context4overwrite_module_attrs_, BadUsage, Context4overwrite_module_attrs
from seed.helper.context4overwrite_module_attrs import *
