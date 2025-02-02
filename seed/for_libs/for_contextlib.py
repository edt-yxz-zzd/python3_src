#__all__:goto
r'''[[[
e ../../python3_src/seed/for_libs/for_contextlib.py

seed.for_libs.for_contextlib
py -m nn_ns.app.debug_cmd   seed.for_libs.for_contextlib -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.for_libs.for_contextlib:__doc__ -ht # -ff -df

[[
used:
GroupContextManager used in:
    py_adhoc_call  { -end4print }  seed.for_libs.for_tarfile   ,str.iter_read_solo_tarfile_  :script/搜索冫最短加链长度.py..statistics.out.txt.tar.lzma  --xencoding4data:ascii
    <<==:
    view ../../python3_src/seed/for_libs/for_tarfile.py
    grp_ctx_mngr = group_open_solo_tarfile_(may_ipath_or_ifile, may_fmt4compression4read, xencoding4data=xencoding4data, kwds4open_tarfile=kwds4open_tarfile)
    with grp_ctx_mngr as (ifile4tar, ifile4data_or_ifile4text):
        ...
]]



py_adhoc_call   seed.for_libs.for_contextlib   @f
]]]'''#'''
__all__ = r'''
exit_then_enter
null_context
MovableContextManager
GroupContextManager

null_st_ctx_mngr_mkr
GroupStatedContextManagerMaker





check_withable
no_excinfo
enter_
exit_

st_enter_
st_exit_



IContextManager
    IContextManager__movable
        NullContext
            null_context
        MovableContextManager
        GroupContextManager


IStatedContextManagerMaker
    NullStatedContextManagerMaker
        null_st_ctx_mngr_mkr
    GroupStatedContextManagerMaker


'''.split()#'''
    #_StatedContextManager
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.tiny_.check import check_type_is, check_type_le
from seed.tiny_.containers import mk_tuple

import sys # sys.exc_info() -> excinfo/((None, None, None)|(exctype, excinst, exctb))
from contextlib import AbstractContextManager, ExitStack, nullcontext as mk_null_context5result_
['asynccontextmanager', 'contextmanager', 'closing', 'nullcontext', 'AbstractContextManager', 'AbstractAsyncContextManager', 'AsyncExitStack', 'ContextDecorator', 'ExitStack', 'redirect_stdout', 'redirect_stderr', 'suppress', 'aclosing', 'chdir']

from seed.tiny_.types5py import curry1

from seed.helper.repr_input import repr_helper
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
___end_mark_of_excluded_global_names__0___ = ...






no_excinfo = (None,)*3

def _call(nm, sf, /, *args):
    return getattr(type(sf), nm)(sf, *args)
def enter_(ctx_mngr, /):
    return _call('__enter__', ctx_mngr)
enter_ = curry1(_call, '__enter__')
exit_ = curry1(_call, '__exit__')

st_enter_ = curry1(_call, '__st_enter__')
st_exit_ = curry1(_call, '__st_exit__')




def exit_then_enter(sf, /):
    '-> None|^Exception... #used inside with_body'
    #copy from:view ../../python3_src/seed/for_libs/for_signal.py
        #@20250130:循环体每一轮结束时检查是否触发
        #   view ../../python3_src/seed/recognize/cmdline/adhoc_argparser.py
    #
    try:
        type(sf).__exit__(sf, exc_type:=None, exc_value:=None, traceback:=None)
            #^Exception
    finally:
        type(sf).__enter__(sf)

def check_withable(withable, /):
    check_type_le(AbstractContextManager, withable)

class IContextManager(AbstractContextManager, ABC):
    __slots__ = ()
class IContextManager__movable(IContextManager):
    __slots__ = ()
    @abstractmethod
    def move_ctx_mngr(sf, /):
        '-> ot # [copy by move to avoid sf.__exit__()]'


#.null_context = mk_null_context5result_(None)
#.null_context.close()
#.    #AttributeError: 'nullcontext' object has no attribute 'close'
#.with null_context:pass
#.null_context.close()
#.with null_context:pass

class NullContext(IContextManager__movable):
    ___no_slots_ok___ = True
    def __getitem__(sf, out4as, /):
        if out4as is None:
            return null_context
        if out4as is sf.out4as:
            return sf
        return type(sf)(out4as)
    def __init__(sf, out4as, /):
        sf._r = out4as
    @property
    def out4as(sf, /):
        return sf._r
    def __repr__(sf, /):
        return repr_helper(sf, sf.out4as)
    @override
    def __enter__(sf, /):
        return sf.out4as
    @override
    def __exit__(sf, /, *excinfo):
        sf.close()
        return False
    @override
    def move_ctx_mngr(sf, /):
        ot = sf
        return ot
    #@override
    def close(sf, /):
        return
null_context = NullContext(None)
assert null_context[None] is null_context
assert not null_context[1] is null_context
assert null_context[1][None] is null_context

null_context.close()
with null_context:pass
null_context.close()
with null_context:pass








class MovableContextManager(IContextManager__movable):
    ___no_slots_ok___ = True
    def __init__(sf, withable, /):
        check_withable(withable)
        sf._w = withable
        sf._m = None
    @property
    def withable(sf, /):
        return sf._w
    def __repr__(sf, /):
        return repr_helper(sf, sf.withable)
    @override
    def __enter__(sf, /):
        while sf._m is None:
            withable = sf._w
            r = enter_(withable)
            sf._m = (nwithable:=withable, r)
        (nwithable, r) = sf._m
        return r
    @override
    def __exit__(sf, /, *excinfo):
        (nwithable, r) = sf._m
            # [nwithable may be null_context]
        #sf._m = None
        #sf._m = ...
        return exit_(nwithable, *excinfo)
    @override
    def move_ctx_mngr(sf, /):
        r'''copy by move to avoid __exit__()

        usage:
        mvb_ctx_mngr = MovableContextManager(open(0))
        with mvb_ctx_mngr as stdin:
            use_(stdin)
            if to_return:
                return mvb_ctx_mngr.move_ctx_mngr()
                    # stdin will not be closed
        '''#'''
        ot = type(sf)(sf.withable)
        if None is sf._m: return
        (nwithable, r) = ot._m = sf._m
        if not nwithable is null_context:
            sf._m = (nwithable:=null_context, r)
        return ot


class GroupContextManager(IContextManager__movable):
    ___no_slots_ok___ = True
    def __init__(sf, withables, /):
        sf._ws = mk_tuple(withables)
        sf._m = None
    @property
    def withables(sf, /):
        return sf._ws
    def __repr__(sf, /):
        return repr_helper(sf, [*sf.withables])
    @override
    def __enter__(sf, /):
        while sf._m is None:
            exit_stack = ExitStack()
            rs = tuple(map(exit_stack.enter_context, sf._ws))
            sf._m = (nexit_stack:=exit_stack, rs)
        (nexit_stack, rs) = sf._m
        return rs
    @override
    def __exit__(sf, /, *excinfo):
        (nexit_stack, rs) = sf._m
            # [nexit_stack may be null_context]
        #sf._m = None
        #sf._m = ...
        #bug:nexit_stack.close()
        #bug:with nexit_stack:pass
        return exit_(nexit_stack, *excinfo)
    @override
    def move_ctx_mngr(sf, /):
        r'''copy by move to avoid __exit__()

        usage:
        grp_ctx_mngr = GroupContextManager([open(0), open(1), open(2)])
        with grp_ctx_mngr as (stdin, stderr, stdout):
            use_(stdin, stderr, stdout)
            if to_return:
                return grp_ctx_mngr.move_ctx_mngr()
                    # (stdin, stderr, stdout) will not be closed
        '''#'''
        ot = type(sf)(sf.withables)
        if None is sf._m: return
        (nexit_stack, rs) = ot._m = sf._m
        if not nexit_stack is null_context:
            sf._m = (nexit_stack:=null_context, rs)
        return ot





































































































class IStatedContextManagerMaker(ABC):
    'st_ctx_mngr_mkr # [not$ [IStatedContextManagerMaker <: AbstractContextManager]]'
    __slots__ = ()
    @abstractmethod
    def __st_enter__(sf, /):
        '-> (st4exit, out4as)'
    @abstractmethod
    def __st_exit__(sf, st, /, *excinfo):
        #__exit__(self, exctype, excinst, exctb)
        'st -> exctype -> excinst -> exctb -> not_to_reraise/to_suppress_exc/bool'
    #def ctx_mngr5st_ctx_mngr_mkr_
    #def __call__(sf, /, *, to_output_self:bool=False):
    def mk_ctx_mngr(sf, /, *, to_output_self:bool=False):
        '-> AbstractContextManager'
        return _StatedContextManager(sf, to_output_self=to_output_self)


class _StatedContextManager(IContextManager__movable):
    'st_ctx_mngr'
    ___no_slots_ok___ = True
    def __init__(sf, st_ctx_mngr_mkr:IStatedContextManagerMaker, /, *, to_output_self:bool):
        #check_type_le(IStatedContextManagerMaker, st_ctx_mngr_mkr)
        sf._mkr = st_ctx_mngr_mkr
        sf._b = to_output_self
        sf._m = None
    @property
    def st_ctx_mngr_mkr(sf, /):
        return sf._mkr
    @property
    def to_output_self(sf, /):
        return sf._b
    def __repr__(sf, /):
        return repr_helper(sf, sf.st_ctx_mngr_mkr, to_output_self=sf.to_output_self)
    @override
    def __enter__(sf, /):
        while sf._m is None:
            st_ctx_mngr_mkr = sf._mkr
            (st, out4as) = pair = st_enter_(st_ctx_mngr_mkr)
            sf._m = (nst_ctx_mngr_mkr:=st_ctx_mngr_mkr, pair)
        (nst_ctx_mngr_mkr, pair) = sf._m
        (st, out4as) = pair
        if sf.to_output_self:
            return (sf, out4as)
        return out4as
    @override
    def __exit__(sf, /, *excinfo):
        (nst_ctx_mngr_mkr, pair) = sf._m
            # [nst_ctx_mngr_mkr may be null_st_ctx_mngr_mkr]
        (st, out4as) = pair
        #sf._m = None
        #sf._m = ...
        return st_exit_(nst_ctx_mngr_mkr, st, *excinfo)
    @override
    def move_ctx_mngr(sf, /):
        r'copy by move to avoid __exit__()'
        ot = type(sf)(sf.st_ctx_mngr_mkr, to_output_self=sf.to_output_self)
        if None is sf._m: return
        (nst_ctx_mngr_mkr, pair) = ot._m = sf._m
        (st, out4as) = pair
        if not nst_ctx_mngr_mkr is null_st_ctx_mngr_mkr:
            sf._m = (nst_ctx_mngr_mkr:=null_st_ctx_mngr_mkr, pair)
        return ot

class NullStatedContextManagerMaker(IStatedContextManagerMaker):
    ___no_slots_ok___ = True
    def __getitem__(sf, out4as, /):
        if out4as is None:
            return null_st_ctx_mngr_mkr
        if out4as is sf.out4as:
            return sf
        return type(sf)(out4as)
    def __init__(sf, out4as, /):
        sf._r = out4as
    @property
    def out4as(sf, /):
        return sf._r
    def __repr__(sf, /):
        return repr_helper(sf, sf.out4as)
    @override
    def __st_enter__(sf, /):
        return (st:=None, sf.out4as)
    @override
    def __st_exit__(sf, st, /, *excinfo):
        #sf.close6st()
        return False
    #def close6st(sf, st, /): return
null_st_ctx_mngr_mkr = NullStatedContextManagerMaker(None)
assert null_st_ctx_mngr_mkr[None] is null_st_ctx_mngr_mkr
assert not null_st_ctx_mngr_mkr[1] is null_st_ctx_mngr_mkr
assert null_st_ctx_mngr_mkr[1][None] is null_st_ctx_mngr_mkr

with null_st_ctx_mngr_mkr.mk_ctx_mngr():pass
with null_st_ctx_mngr_mkr.mk_ctx_mngr() as __:
    assert __ is None
with null_st_ctx_mngr_mkr[999].mk_ctx_mngr() as __:
    assert __ == 999
with (__sf := null_st_ctx_mngr_mkr.mk_ctx_mngr(to_output_self=True)) as (__0, __1):
    assert __0 is __sf
    assert __1 is None
    with __sf as __pair:
        assert __pair == (__sf, None)
with (__sf := null_st_ctx_mngr_mkr[999].mk_ctx_mngr(to_output_self=True)) as (__0, __1):
    assert __0 is __sf
    assert __1 == 999
    with __sf as __pair:
        assert __pair == (__sf, 999)






class _ContextManager__bind_st_ctx_mngr_mkr_with_st(IContextManager):
    'st_ctx_mngr'
    ___no_slots_ok___ = True
    def __init__(sf, st_ctx_mngr_mkr:IStatedContextManagerMaker, st, /):
        #check_type_le(IStatedContextManagerMaker, st_ctx_mngr_mkr)
        sf._mkr = st_ctx_mngr_mkr
        sf._st = st
    @property
    def st_ctx_mngr_mkr(sf, /):
        return sf._mkr
    @property
    def st(sf, /):
        return sf._st
    def __repr__(sf, /):
        return repr_helper(sf, sf.st_ctx_mngr_mkr, sf.st)
    @override
    def __enter__(sf, /):
        return
    @override
    def __exit__(sf, /, *excinfo):
        st_ctx_mngr_mkr = sf._mkr
        st = sf._st
        return st_exit_(st_ctx_mngr_mkr, st, *excinfo)

class GroupStatedContextManagerMaker(IStatedContextManagerMaker):
    ___no_slots_ok___ = True
    def __init__(sf, st_ctx_mngr_mkrs, /):
        sf._ws = mk_tuple(st_ctx_mngr_mkrs)
    @property
    def st_ctx_mngr_mkrs(sf, /):
        return sf._ws
    def __repr__(sf, /):
        return repr_helper(sf, [*sf.st_ctx_mngr_mkrs])
    @override
    def __st_enter__(sf, /):
        st = tuple
        sts = []
        outs = []
        for st, out4as in map(st_enter_, sf.st_ctx_mngr_mkrs):
            sts.append(st)
            outs.append(out4as)
        return (st:=tuple(sts), out4as:=tuple(outs))
    @override
    def __st_exit__(sf, st, /, *excinfo):
        ######################
        sts = st
        mkrs = sf.st_ctx_mngr_mkrs
        L = len(mkrs)
        if not len(sts) == L:raise 000
        ######################
        bind_ = _ContextManager__bind_st_ctx_mngr_mkr_with_st
        exit_stack = ExitStack()
        for _ in map(exit_stack.enter_context, map(bind_, reversed(sf.st_ctx_mngr_mkrs), reversed(sts))):pass
        #with exit_stack:raise
        enter_(exit_stack)
        return exit_(exit_stack, *excinfo)
        ######################
        #.######################
        #.to_suppress_exc = False
        #.def on_(j, /):
        #.    '-> to_suppress_exc6j/bool |^BaseException # update:excinfo&to_suppress_exc/bool'
        #.    nonlocal excinfo, to_suppress_exc
        #.    try:
        #.        r = st_exit_(mkrs[j], sts[j], *excinfo)
        #.            # ^BaseException
        #.    except:
        #.        to_suppress_exc = False
        #.            # to_suppress_exc6j
        #.        excinfo = sys.exc_info()
        #.        raise
        #.            # ^BaseException
        #.    #bug:to_suppress_exc |= bool(r)
        #.    to_suppress_exc6j = bool(r)
        #.    to_suppress_exc = to_suppress_exc6j
        #.    if to_suppress_exc6j:
        #.        excinfo = no_excinfo
        #.    return to_suppress_exc6j
        #.def recur_(j, /):
        #.    '-> None |^BaseException # update:excinfo&to_suppress_exc/bool'
        #.    if j == L:
        #.        return
        #.    try:
        #.        recur_(j+1)
        #.            # ^BaseException
        #.    finally:
        #.        to_suppress_exc6j = on_(j)
        #.            # ^BaseException => [to_suppress_exc := False]
        #.        if to_suppress_exc6j:
        #.            assert excinfo is no_excinfo
        #.            return
        #.        #######
        #.        #here:re-return None|reraise
        #.        #######
        #.    #end-try
        #.#end-def recur_(j, /):
        #.recur_(0)
        #.    # ^BaseException
        #.return to_suppress_exc
        #.######################
        #.to_suppress_exc = False
        #.for mkr, st in zip(reversed(sf.st_ctx_mngr_mkrs), reversed(sts)):
        #.    try:
        #.        r = st_exit_(mkr, st, *excinfo)
        #.    except:
        #.        excinfo = sys.exc_info()
        #.        to_suppress_exc = False
        #.    else:
        #.        to_suppress_exc = to_suppress_exc or bool(r)
        #.return to_suppress_exc
        #.######################
        #.bs = reversed([bool(st_exit_(mkr, st, *excinfo)) for mkr, st in zip(reversed(sf.st_ctx_mngr_mkrs), reversed(sts))])
        #.    # !! stacked/Cascading Style
        #.#not_to_reraise =
        #.to_suppress_exc = any(bs)
        #.    # !! stacked/Cascading Style
        #.return to_suppress_exc
        #.######################


__all__
from seed.for_libs.for_contextlib import null_context, MovableContextManager, GroupContextManager

from seed.for_libs.for_contextlib import null_st_ctx_mngr_mkr, GroupStatedContextManagerMaker

from seed.for_libs.for_contextlib import check_withable, no_excinfo, enter_, exit_, st_enter_, st_exit_

from seed.for_libs.for_contextlib import IContextManager, IContextManager__movable

from seed.for_libs.for_contextlib import IStatedContextManagerMaker


from seed.for_libs.for_contextlib import exit_then_enter
from seed.for_libs.for_contextlib import *
