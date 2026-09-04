#__all__:goto
r'''[[[
e ../../python3_src/seed/excepts/repack_exception_.py

seed.excepts.repack_exception_
py -m nn_ns.app.debug_cmd   seed.excepts.repack_exception_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.excepts.repack_exception_:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>> class T(Exception):
...     def __init__(sf, a, b, c, /):
...         Exception.__init__(sf, a,b,c)

>>> repack_exception_(ValueError(555), 111, 222)
ValueError((ValueError(555), (111, 222)))
>>> repack_exception_(T(9,8,7), 111, 222)
repack_exception7new_subclass_((T(9, 8, 7), (111, 222)))
>>> isinstance(repack_exception_(T(9,8,7), 111, 222), T)
True


py_adhoc_call   seed.excepts.repack_exception_   @f
from seed.excepts.repack_exception_ import *
]]]'''#'''
__all__ = r'''
repack_exception_
    repack_exception7new_subclass_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...

def repack_exception_(exc, /, *args):
    assert isinstance(exc, BaseException)
    T = type(exc)
    try:
        #.new_exc = T(exc, *args)
        new_exc = T((exc, args))
    except Exception:
        # TypeError
        #.new_exc = repack_exception7new_subclass_(exc, *args)
        new_exc = repack_exception7new_subclass_((exc, args))
    return new_exc
def repack_exception7new_subclass_(exc_and_args):
    #def repack_exception7new_subclass_(exc, /, *args):
    (exc, args) = exc_and_args
    assert type(args) is tuple
    assert isinstance(exc, BaseException)
    T = type(exc)
    class E(T, BaseException):
        def __init__(sf, /, *args):
            BaseException.__init__(sf, *args)
        def __repr__(sf, /):
            #.(exc, args) = sf.args
            #.return repr_helper(sf, exc, *args)
            return repr_helper(sf, *sf.args)

    E.__name__ = 'repack_exception7new_subclass_'

    #.return E(exc, *args)
    return E((exc, args))


__all__
from seed.excepts.repack_exception_ import repack_exception_, repack_exception7new_subclass_
from seed.excepts.repack_exception_ import *
