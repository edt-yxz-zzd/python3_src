#__all__:goto
r'''[[[
e ../../python3_src/seed/types/ctx/IGroupContextManager.py
view ../../python3_src/seed/for_libs/for_contextlib.py
    from seed.for_libs.for_contextlib import null_context, MovableContextManager, GroupContextManager
view ../../python3_src/seed/tiny_/null_dev.py
    from seed.tiny_.null_dev import null_context, null_context5result_




seed.types.ctx.IGroupContextManager
py -m nn_ns.app.debug_cmd   seed.types.ctx.IGroupContextManager -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.types.ctx.IGroupContextManager:__doc__ -ht # -ff -df
#######

[[
used in:
view ../../python3_src/seed/io/decompress_truncated_file.py
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.types.ctx.IGroupContextManager   @f
]]]'''#'''
__all__ = r'''
IGroupContextManager__ver2
    GroupContextManager__ver2
    InnermostContext
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
import sys # sys.exc_info() -> excinfo/((None, None, None)|(exctype, excinst, exctb))
from contextlib import AbstractContextManager, ExitStack, nullcontext as mk_null_context5result_
#.from itertools import islice
from seed.tiny_.check import check_type_is, check_int_ge_le, check_non_ABC, check_callable
from seed.tiny_.containers import mk_tuple
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
___end_mark_of_excluded_global_names__0___ = ...

def _exit(withable, /, *excinfo):
    return type(withable).__exit__(withable, *excinfo)

class IGroupContextManager__ver2(ABC):
    __slots__ = ()
    @property
    @abstractmethod
    def _withable_seq_(sf, /):
        '-> [context_manager]'
    @abstractmethod
    def _mk_target6with_as_(sf, target_seq, /):
        '[target{context_manager}] -> target{sf}'
    @abstractmethod
    def _push_ctx6enter_(sf, ctx, /):
        'ctx -> None'
    @abstractmethod
    def _pop_ctx6exit_(sf, /):
        '-> ctx'
    @override
    def __enter__(sf, /):
        exit_stack = ExitStack()
        sf._push_ctx6enter_(exit_stack)
        try:
            target_seq = tuple(map(exit_stack.enter_context, sf._withable_seq_))
            target4sf = sf._mk_target6with_as_(target_seq)
        except:
            _exit(exit_stack, *sys.exc_info())
            exit_stack = sf._pop_ctx6exit_()
            raise
        return target4sf
    @override
    def __exit__(sf, /, *excinfo):
        exit_stack = sf._pop_ctx6exit_()
        return _exit(exit_stack, *excinfo)

class _IGroupContextManager__ver2__mixins(IGroupContextManager__ver2):
    __slots__ = ()
    @property
    @override
    def _withable_seq_(sf, /):
        '-> [context_manager]'
        return sf._withables
    @override
    def _push_ctx6enter_(sf, ctx, /):
        'ctx -> None'
        sf._stk.append(ctx)
    @override
    def _pop_ctx6exit_(sf, /):
        '-> ctx'
        return sf._stk.pop()
class GroupContextManager__ver2(_IGroupContextManager__ver2__mixins):
    ___no_slots_ok___ = True
    def __init__(sf, withables, ncall, xmkr4target, /, *ex_args4mkr):
        check_int_ge_le(-1, 2, ncall)
        if ncall == -1:
            if ex_args4mkr:raise TypeError
        else:
            check_callable(xmkr4target)
        withables = mk_tuple(withables)
        sf._withables = withables
        sf._xdefault = (ncall, xmkr4target, ex_args4mkr)
        sf._stk = []
    @override
    def _mk_target6with_as_(sf, target_seq, /):
        '[target{context_manager}] -> target{sf}'
        (ncall, xmkr4target, ex_args4mkr) = sf._xdefault
        if ncall == -1:
            target4sf = xmkr4target
        else:
            mkr = xmkr4target
            target4sf = mkr(*[sf, target_seq][2-ncall:], *ex_args4mkr)
        target4sf
        return target4sf
check_non_ABC(GroupContextManager__ver2)

class InnermostContext(_IGroupContextManager__ver2__mixins):
    ___no_slots_ok___ = True
    def __init__(sf, nonempty_withables, /):
        nonempty_withables = mk_tuple(nonempty_withables)
        if not nonempty_withables:raise TypeError
        sf._withables = nonempty_withables
        sf._stk = []
    @override
    def _mk_target6with_as_(sf, target_seq, /):
        '[target{context_manager}] -> target{sf}'
        return target_seq[-1]
check_non_ABC(InnermostContext)


__all__
from seed.types.ctx.IGroupContextManager import IGroupContextManager__ver2
from seed.types.ctx.IGroupContextManager import GroupContextManager__ver2, InnermostContext
from seed.types.ctx.IGroupContextManager import *
