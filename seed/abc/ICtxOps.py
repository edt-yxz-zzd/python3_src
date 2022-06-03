r'''
e ../../python3_src/seed/abc/ICtxOps.py
py -m seed.abc.ICtxOps
py -m nn_ns.app.debug_cmd   seed.abc.ICtxOps
from seed.abc.ICtxOps import ICtxOps

move from:
    view ../../python3_src/seed/types/union_find_algo/DisjointSet.py

#'''
__all__ = '''
    ICtxOps
    '''.split()

#################################
#HHHHH
___begin_mark_of_excluded_global_names__0___ = ...
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.tiny import check_type_is
___end_mark_of_excluded_global_names__0___ = ...

#HHHHH


#class IOpsWithMutableContext(ABC):
class ICtxOps(ABC):
    '???normal ops should be immutable, ICtxOps=(IOps, MutableContext), just a wrapper to bind two concepts into one obj==>>mk_ctxops__via_ireplace_mutable_context/get...#no set'
    __slots__ = ()
    #@abstractmethod
    def _sketchy_check__mutable_context_(ctxops, mutable_context, /):
        'ctxops -> mutable_context?/obj -> None|TypeError'
    @abstractmethod
    def _get_mutable_context4ops_(ctxops, /):
        'ctxops -> mutable_context'
    @abstractmethod
    def _mk_ctxops__via_ireplace_mutable_context_(ctxops, mutable_context, /):
        'base_ctxops -> mutable_context -> new_ctxops'



    if 0:
        #has:get, no:set, but:ireplace
        @abstractmethod
        def _set_mutable_context4ops_(ctxops, mutable_context, /):
            'ctxops -> mutable_context -> None'
        def set_mutable_context4ops(ctxops, mutable_context, /):
            'ctxops -> mutable_context -> None'
            ctxops.sketchy_check__mutable_context(mutable_context)
            ctxops._set_mutable_context4ops_(mutable_context)



    def sketchy_check__mutable_context(ctxops, mutable_context, /):
        'ctxops -> mutable_context?/obj -> None|TypeError'
        ctxops._sketchy_check__mutable_context_(mutable_context)
    def get_mutable_context4ops(ctxops, /):
        'ctxops -> mutable_context'
        mutable_context = ctxops._get_mutable_context4ops_()
        ctxops.sketchy_check__mutable_context(mutable_context)
        return mutable_context
    def mk_ctxops__via_ireplace_mutable_context(ctxops, mutable_context, /):
        'base_ctxops -> mutable_context -> new_ctxops'
        ctxops.sketchy_check__mutable_context(mutable_context)
        new_ctxops = ctxops._mk_ctxops__via_ireplace_mutable_context_(mutable_context)
        check_type_is(type(ctxops), new_ctxops)
        return new_ctxops
#class ICtxOps(ABC):



