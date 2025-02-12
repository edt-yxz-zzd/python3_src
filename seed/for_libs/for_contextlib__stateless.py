#__all__:goto
r'''[[[
e ../../python3_src/seed/for_libs/for_contextlib__stateless.py

seed.for_libs.for_contextlib__stateless
py -m nn_ns.app.debug_cmd   seed.for_libs.for_contextlib__stateless -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.for_libs.for_contextlib__stateless:__doc__ -ht # -ff -df

[[
[seed.for_libs.for_contextlib__stateless.IStatelessContextManager is almost the same as seed.for_libs.for_contextlib.IStatedContextManagerMaker]
    diff at (*args, **kwds)

usage:
with mk_ctx_mngr5stateless_(stateless_ctx_mngr, *args, **kwds) as target:
    ...

]]

py_adhoc_call   seed.for_libs.for_contextlib__stateless   @f

]]]'''#'''
__all__ = r'''
mk_ctx_mngr5stateless_
IStatelessContextManager

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
import sys # sys.exc_info() -> excinfo/((None, None, None)|(exctype, excinst, exctb))
from contextlib import AbstractContextManager# ExitStack, nullcontext as mk_null_context5result_

#.from itertools import islice
from seed.tiny_.check import check_type_is, check_type_le# check_int_ge
#.
from seed.abc.abc__ver1 import abstractmethod, override, ABC
from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...
class IStatelessContextManager(ABC):
    '[stateless_ctx_mngr is not AbstractContextManager]'
    __slots__ = ()
    @abstractmethod
    def __enter4stateless__(sf, /, *args, **kwds):
        '*args -> **kwds -> st'
    @abstractmethod
    def __state_and_ctx_mngr2target__(sf, st, ctx_mngr, /):
        'st -> ctx_mngr/AbstractContextManager -> target'
    @abstractmethod
    def __exit4stateless__(sf, st, may_excinfo, /):
        'st -> may_excinfo/may (exctype, excinst, exctb) -> whether_not_reraise/bool'

def mk_ctx_mngr5stateless_(stateless_ctx_mngr, /, *args, **kwds):
    'IStatelessContextManager -> *args -> **kwds -> AbstractContextManager'
    st = type(stateless_ctx_mngr).__enter4stateless__(stateless_ctx_mngr, *args, **kwds)
    return _ContextManager5Stateless(stateless_ctx_mngr, st)

class _ContextManager5Stateless(AbstractContextManager):
    'used by mk_ctx_mngr5stateless_()'
    def __init__(sf, stateless_ctx_mngr, st, /):
        check_type_le(IStatelessContextManager, stateless_ctx_mngr)
        sf._x = stateless_ctx_mngr
        sf._st = st
    def __repr__(sf, /):
        stateless_ctx_mngr = sf._x
        st = sf._st
        return repr_helper(sf, stateless_ctx_mngr, st)
    @override
    def __enter__(sf, /):
        stateless_ctx_mngr = sf._x
        st = sf._st
        target = type(stateless_ctx_mngr).__state_and_ctx_mngr2target__(stateless_ctx_mngr, st, sf)
        return target

    @override
    def __exit__(sf, /, *excinfo):
        stateless_ctx_mngr = sf._x
        st = sf._st
        may_excinfo = None if excinfo[0] is None else excinfo
        whether_not_reraise = type(stateless_ctx_mngr).__exit4stateless__(stateless_ctx_mngr, st, may_excinfo)
        check_type_is(bool, whether_not_reraise)
        return whether_not_reraise

#.class __(ABC):
#.    ___no_slots_ok___ = True
#.if __name__ == "__main__":
#.    raise NotImplementedError


__all__
from seed.for_libs.for_contextlib__stateless import mk_ctx_mngr5stateless_, IStatelessContextManager
from seed.for_libs.for_contextlib__stateless import *
