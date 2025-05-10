#__all__:goto
#_nms4neat__str:goto
#TODO:end_idx manager #vs:ignore_manager,local_ctx_manager
r'''[[[
e ../../python3_src/seed/recognize/rgnr/rgnrs/SimpleRecognizer.py
view ../../python3_src/seed/recognize/rgnr/abc/ISimpleRecognizer.py

e ../../python3_src/seed/recognize/rgnr/test/test4SimpleRecognizer.py
e ../../python3_src/seed/recognize/rgnr/example/example4SimpleRecognizer.py
view ../../python3_src/seed/recognize/rgnr/utils/utils4ISimpleRecognizer.py

seed.recognize.rgnr.rgnrs.SimpleRecognizer
py -m nn_ns.app.debug_cmd   seed.recognize.rgnr.rgnrs.SimpleRecognizer -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.recognize.rgnr.rgnrs.SimpleRecognizer:__doc__ -ht # -ff -df

[[
]]

py_adhoc_call   seed.recognize.rgnr.rgnrs.SimpleRecognizer   @f
from seed.recognize.rgnr.rgnrs.SimpleRecognizer import *
]]]'''#'''
__all__ = r'''
AllSimpleRecognizers


SimpleRecognizer__switch

SimpleRecognizer__chain
    SimpleRecognizer__flatten4Rope
    WithLocalContext
        check_may_oresult_parts
    SimpleRecognizer__many
        SimpleRecognizer__optional
    SimpleRecognizer__nongreedy_end_by0
    SimpleRecognizer__sep_by1

    SimpleRecognizer__local_ctx_manager__long_distance_local_ctx_controller
    SimpleRecognizer__local_ctx_manager__dependent_pair
    SimpleRecognizer__local_ctx_as_dispatch_key



SimpleRecognizer__py_regex
    SimpleRecognizer__py_str
SimpleRecognizer__constant




SimpleRecognizer__ref
    SimpleRecognizer__lift
ISimpleRecognizer__post6ok
    SimpleRecognizer__post6ok
        SimpleRecognizer__flatten4Rope
    SimpleRecognizer__post6ok__overwrite_oresult_by_constant
    SimpleRecognizer__post6ok__overwrite_oresult_by_null_rope
    ISimpleRecognizer__post6ok__never_ignore_fpost6ok__init
        SimpleRecognizer__tag
        SimpleRecognizer__box4Rope
            SimpleRecognizer__unbox
        SimpleRecognizer__local_ctx_manager__oresult_as_local_ctx4sibling
        SimpleRecognizer__local_ctx_manager__drop_local_ctx4sibling
        SimpleRecognizer__local_ctx_manager__tag_local_ctx4sibling_with_local_ctx4original
        SimpleRecognizer__local_ctx_manager__using_local_ctx4original_as_local_ctx4sibling

ISimpleRecognizer__local_ctx_manager__projector4local_ctx
    SimpleRecognizer__local_ctx_manager__projector4local_ctx
    SimpleRecognizer__local_ctx_manager__projector4local_ctx__via_getitem

ISimpleRecognizer__ignore_manager__init
    SimpleRecognizer__ignore_manager__always_ignore
    SimpleRecognizer__ignore_manager__never_ignore
SimpleRecognizer__look_ahead
    SimpleRecognizer__not_follow_by

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from seed.func_tools.func_access import FuncAccess
    #for:ci_post(),fpost6ok()
    #see:SimpleRecognizer__ref
    #see:SimpleRecognizer__post6ok

from seed.func_tools.recur5yield__strict import BoxedTailRecur, BoxedFinalResult
from seed.recognize.rgnr.abc.ISimpleRecognizer import ISimpleRecognizer, ISimpleRecognizeReply, IArgs4recur_call, ICommon4recur_call, ISimpleRecognizerNameServer, IInputSeqEx

from seed.types.Either import Cased, Either# KindedName
from seed.types.Either import mk_Left, mk_Right
from seed.types.Rope import Rope, null_rope
    # Rope(*ls_of__tpl_or_rope)

import re

from seed.tiny_.containers import mk_tuple, null_tuple
from seed.iters.count_ import count_

#.from itertools import islice
from seed.tiny_.check import check_type_is, check_int_ge, check_pair
from seed.tiny_.funcs import const

from seed.abc.abc__ver1 import abstractmethod, override, ABC
from seed.helper.repr_input import repr_helper
from seed.tiny_._Base4repr import _Base4repr
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


def check_may_oresult_parts(may_oresult_parts, /):
    if not may_oresult_parts is None:
        oresult_parts = may_oresult_parts
        check_type_is(Rope, oresult_parts)

class WithLocalContext(tuple):#xxx: _Base4repr
    def __new__(cls, may_oresult_parts, local_ctx4sibling, /):
        check_may_oresult_parts(may_oresult_parts)
        sf = super().__new__(cls, [may_oresult_parts, local_ctx4sibling])
        return sf
    def __repr__(sf, /):
        return repr_helper(sf, *sf)
    @property
    def may_oresult_parts(sf, /):
        return sf[0]
    @property
    def local_ctx4sibling(sf, /):
        return sf[1]

#_C = Case4ISimpleRecognizeReply
class SimpleRecognizer__chain(ISimpleRecognizer, _Base4repr):
    #vs:SimpleRecognizer__serial #deprecate by flatten4Rope
    #vs:SimpleRecognizer__chain
    #vs:SimpleRecognizer__many
    #vs:SimpleRecognizer__nongreedy_end_by0
    r'''[[[
    'chain'

    precondition:
        [child_rgnr.rgnz_oresult == (may oresult_parts/Rope | WithLocalContext(may oresult_parts/Rope, local_ctx{sibling}))]
    postcondition:
        [this_rgnr.rgnz_oresult == (may oresult_parts/Rope | WithLocalContext(may oresult_parts/Rope, local_ctx{uncle}{===local_ctx4sibling{last-child_rgnr}}))]
    #]]]'''#'''

    r'''[[[
    dependent_pair<<==:
        args4recur_call:++local_ctx
        local_ctx_manager
            context-dependent grammar
            context-sensitive
            remote/long-range/long-distance local_ctx controller
    #]]]'''#'''
    ___no_slots_ok___ = True
    def __init__(sf, rgnrs4protected, rgnrs4unprotected, never_ignore_rope_struct:bool, /):
        check_type_is(bool, never_ignore_rope_struct)
        rgnrs4protected = mk_tuple(rgnrs4protected)
        rgnrs4unprotected = mk_tuple(rgnrs4unprotected)
        sf._rs0 = rgnrs4protected
        sf._rs1 = rgnrs4unprotected
        sf._rs = (*rgnrs4protected, *rgnrs4unprotected)
        sf._k = len(rgnrs4protected)
        sf._ng = never_ignore_rope_struct
        sf._init4repr(rgnrs4protected, rgnrs4unprotected, never_ignore_rope_struct)
    @override
    def _recognize_(sf, args4recur_call, /):
        'IArgs4recur_call -> GI(yield:gi/GI;return:(BoxedTailRecur{recur-GI}|BoxedFinalResult{rgnz_reply/ISimpleRecognizeReply})'
        begin_idx = args4recur_call.begin_idx
        never_ignore_rope_struct = sf._ng
        _ignore = not never_ignore_rope_struct and args4recur_call.ignore

        rgnrs = sf._rs
        k = sf._k

        (may_ls, append, tmay_local_ctx4original, tmay_local_ctx4uncle) = _init4chain(_ignore)

        for j, rgnr in enumerate(rgnrs):
            rgnz_reply = yield rgnr._recognize_(args4recur_call)
            match rgnz_reply.rgnz_eresult:
                case Either(True, rgnz_oresult):
                    may_oresult_parts = _handle6ok4chain(debug:=rgnr, tmay_local_ctx4original, tmay_local_ctx4uncle, args4recur_call, rgnz_oresult)
                    #xxx:check_type_is(Rope, rgnz_oresult)
                    append(may_oresult_parts)
                case _:
                    if j < k:
                        #rgnrs4protected => restore:begin_idx
                        args4recur_call.begin_idx = begin_idx
                        #now be recoverable_failure
                    return BoxedFinalResult(rgnz_reply)
                    break
            #ls
        #ls
        return _finalize4chain(tmay_local_ctx4original, tmay_local_ctx4uncle, args4recur_call, may_ls)
        777;    yield
#end-class SimpleRecognizer__chain(ISimpleRecognizer):

def _init4chain(_ignore, /):
    if _ignore:
        def append(x, /):pass
        may_ls = None
    else:
        ls = []
        _append = ls.append
        def append(x, /):
            check_type_is(Rope, x)
            _append(x)
        append
        may_ls = ls
    may_ls
    append
    tmay_local_ctx4original = []
    tmay_local_ctx4uncle = []
    return (may_ls, append, tmay_local_ctx4original, tmay_local_ctx4uncle)
def _handle6ok4chain(debug, tmay_local_ctx4original, tmay_local_ctx4uncle, args4recur_call, rgnz_oresult, /):
    #SimpleRecognizer__chain
    #SimpleRecognizer__many
    #SimpleRecognizer__nongreedy_end_by0
    if type(rgnz_oresult) is WithLocalContext:
        if not tmay_local_ctx4original:
            tmay_local_ctx4original[:] = (args4recur_call.local_ctx,)
        (may_oresult_parts, local_ctx4sibling) = rgnz_oresult
        args4recur_call.local_ctx = local_ctx4sibling
        tmay_local_ctx4uncle[:] = (local_ctx4sibling,)
    else:
        may_oresult_parts = rgnz_oresult
        tmay_local_ctx4uncle[:] = ()
    may_oresult_parts
    try:
        check_may_oresult_parts(may_oresult_parts)
    except Exception:
        from seed.tiny import print_err
        print_err('@_handle6ok4chain:', debug)
    return may_oresult_parts
def _finalize4chain(tmay_local_ctx4original, tmay_local_ctx4uncle, args4recur_call, may_ls, /):
    #may_oresult_parts = None if _ignore else Rope(*ls)
    may_oresult_parts = None if may_ls is None else Rope(*may_ls)
    if tmay_local_ctx4original:
        [args4recur_call.local_ctx] = tmay_local_ctx4original
    if tmay_local_ctx4uncle:
        [local_ctx4uncle] = tmay_local_ctx4uncle
        rgnz_oresult = WithLocalContext(may_oresult_parts, local_ctx4uncle)
    else:
        rgnz_oresult = may_oresult_parts
    rgnz_oresult
    rgnz_eresult = mk_Right(rgnz_oresult)
    end_idx4reply = args4recur_call.begin_idx
    rgnz_reply = args4recur_call.mk_rgnz_reply_(end_idx4reply, rgnz_eresult)
    return BoxedFinalResult(rgnz_reply)

class SimpleRecognizer__switch(ISimpleRecognizer, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, rgnrs, /):
        rgnrs = mk_tuple(rgnrs)
        #if not rgnrs:raise ValueError
        sf._rs = rgnrs
        sf._init4repr(rgnrs)
    @override
    def _recognize_(sf, args4recur_call, /):
        'IArgs4recur_call -> GI(yield:gi/GI;return:(BoxedTailRecur{recur-GI}|BoxedFinalResult{rgnz_reply/ISimpleRecognizeReply})'
        rgnrs = sf._rs
        begin_idx = args4recur_call.begin_idx
        if not rgnrs:
            rgnz_errmsg = 'no_branches'
            rgnz_eresult = mk_Left(rgnz_errmsg)
            end_idx4reply = begin_idx
            rgnz_reply = args4recur_call.mk_rgnz_reply_(end_idx4reply, rgnz_eresult)
            return BoxedFinalResult(rgnz_reply)

        ls = []
        append = ls.append
        for j, rgnr in enumerate(rgnrs):
            # [args4recur_call.begin_idx == begin_idx]
            rgnz_reply = yield rgnr._recognize_(args4recur_call)
            match rgnz_reply.rgnz_eresult:
                case Either(True, rgnz_oresult):
                    break
                case _:
                    append((rgnz_reply.end_idx4reply, j, rgnz_reply))
                    if not args4recur_call.begin_idx == begin_idx:
                        #non-recoverable_failure
                        break
                    # [args4recur_call.begin_idx == begin_idx]
            ls
            # [args4recur_call.begin_idx == begin_idx]
        else:
            # no match && no non-recoverable_failure
            # all are recoverable_failure
            #=>recoverable_failure
            ls
            assert ls # see:above:"no_branches"
            (end_idx4reply, j, rgnz_reply) = max(ls)
        j, rgnz_reply

        return BoxedFinalResult(rgnz_reply)
        777;    yield
#end-class SimpleRecognizer__switch(ISimpleRecognizer):

class SimpleRecognizer__local_ctx_as_dispatch_key(ISimpleRecognizer, _Base4repr):
    'local_ctx_as_dispatch_key#see:SimpleRecognizer__local_ctx_manager__long_distance_local_ctx_controller,SimpleRecognizer__local_ctx_manager__dependent_pair'
    ___no_slots_ok___ = True
    def __init__(sf, key2rgnr, /):
        sf._d = key2rgnr
        sf._init4repr(key2rgnr)
    @override
    def _recognize_(sf, args4recur_call, /):
        'IArgs4recur_call -> GI(yield:gi/GI;return:(BoxedTailRecur{recur-GI}|BoxedFinalResult{rgnz_reply/ISimpleRecognizeReply})'
        key2rgnr = sf._d
        rgnr = key2rgnr[args4recur_call.local_ctx]
        return BoxedTailRecur(rgnr._recognize_(args4recur_call))
        777;    yield
#end-class SimpleRecognizer__local_ctx_as_dispatch_key(ISimpleRecognizer):





class SimpleRecognizer__py_regex(ISimpleRecognizer, _Base4repr):
    'py_regex'
    ___no_slots_ok___ = True
    def __init__(sf, regex, matchobj_vs_substr:bool, /):
        check_type_is(bool, matchobj_vs_substr)
        if not hasattr(regex, 'match'):
            regex = re.compile(regex)
        sf._regex = regex
        sf._b = matchobj_vs_substr
        sf._init4repr(regex.pattern, matchobj_vs_substr)
    @override
    def _recognize_(sf, args4recur_call, /):
        'IArgs4recur_call -> GI(yield:gi/GI;return:(BoxedTailRecur{recur-GI}|BoxedFinalResult{rgnz_reply/ISimpleRecognizeReply})'
        (begin_idx, end_idx, ignore) = args4recur_call.mutable_args[:3]
        matchobj_vs_substr = sf._b
        regex = sf._regex
        ss = args4recur_call.common4recur_call.input_seq_ex.seq_view
        #check_type_is(str, ss)
        m = regex.match(ss, begin_idx, end_idx)
        if m is None:
            end_idx4reply = begin_idx
            case = False
        else:
            assert m.start() == begin_idx
            end_idx4reply = m.end()
            777;    args4recur_call.begin_idx = end_idx4reply
            if not ignore and matchobj_vs_substr:
                m = m.group(0)
            case = True
        payload = None if ignore else m

        rgnz_eresult = Either(case, payload)
        rgnz_reply = args4recur_call.mk_rgnz_reply_(end_idx4reply, rgnz_eresult)
        return BoxedFinalResult(rgnz_reply)
        777;    yield

#end-class SimpleRecognizer__py_regex(ISimpleRecognizer):

class SimpleRecognizer__py_str(ISimpleRecognizer, _Base4repr):
    'py_str'
    ___no_slots_ok___ = True
    def __init__(sf, s, /):
        sf._s = s
        sf._init4repr(s)
    @override
    def _recognize_(sf, args4recur_call, /):
        'IArgs4recur_call -> GI(yield:gi/GI;return:(BoxedTailRecur{recur-GI}|BoxedFinalResult{rgnz_reply/ISimpleRecognizeReply})'
        (begin_idx, end_idx, ignore) = args4recur_call.mutable_args[:3]
        s = sf._s
        ss = args4recur_call.common4recur_call.input_seq_ex.seq_view
        if not ss.startswith(s, begin_idx, end_idx):
            end_idx4reply = begin_idx
            case = False
        else:
            end_idx4reply = begin_idx+len(s)
            777;    args4recur_call.begin_idx = end_idx4reply
            case = True
        payload = None if ignore else s

        rgnz_eresult = (case, payload)
        rgnz_reply = args4recur_call.mk_rgnz_reply_(end_idx4reply, rgnz_eresult)
        return BoxedFinalResult(rgnz_reply)
        777;    yield

#end-class SimpleRecognizer__py_str(ISimpleRecognizer):




class ISimpleRecognizer__post6ok(ISimpleRecognizer):
    'post6ok@[?ignore?]'
    __slots__ = ()
    @property
    @abstractmethod
    def wrapped_rgnr(sf, /):
        '-> ISimpleRecognizer'
    @property
    @abstractmethod
    def fpost6ok(sf, /):
        '-> fpost6ok/((*infos6pre) -> (*infos6post) -> rgnz_oresult -> rgnz_oresult)'
    @property
    @abstractmethod
    def never_ignore_fpost6ok(sf, /):
        '-> bool'
    def collect6pre(sf, args4recur_call, /):
        '-> infos6pre'
        return null_tuple
    def collect6post(sf, args4recur_call, /):
        '-> infos6post'
        return null_tuple
    @override
    def _recognize_(sf, args4recur_call, /):
        'IArgs4recur_call -> GI(yield:gi/GI;return:(BoxedTailRecur{recur-GI}|BoxedFinalResult{rgnz_reply/ISimpleRecognizeReply})'
        rgnr = sf.wrapped_rgnr
        never_ignore_fpost6ok = sf.never_ignore_fpost6ok
        if not never_ignore_fpost6ok and args4recur_call.ignore:
            return BoxedTailRecur(rgnr._recognize_(args4recur_call))

        777;    infos6pre = sf.collect6pre(args4recur_call)
        rgnz_reply = yield rgnr._recognize_(args4recur_call)

        match rgnz_reply.rgnz_eresult:
            case Either(True, rgnz_oresult):
                777;    infos6post = sf.collect6post(args4recur_call)
                _rgnz_oresult = sf.fpost6ok(*infos6pre, *infos6post, rgnz_oresult)
                if not _rgnz_oresult is rgnz_oresult:
                    rgnz_eresult = mk_Right(_rgnz_oresult)
                    rgnz_reply = rgnz_reply.ireplace_(rgnz_eresult=rgnz_eresult)
        return BoxedFinalResult(rgnz_reply)
        777;    yield
#end-class ISimpleRecognizer__post6ok(ISimpleRecognizer):


class SimpleRecognizer__post6ok(ISimpleRecognizer__post6ok, _Base4repr):
    'post6ok@[maybe ignore] #fpost6ok:see:seed.func_tools.func_access.FuncAccess'
    ___no_slots_ok___ = True
    def __init__(sf, rgnr, fpost6ok, never_ignore_fpost6ok:bool, /):
        check_type_is(bool, never_ignore_fpost6ok)
        #check_callable(fpost6ok)
        sf._rgnr = rgnr
        sf._fpost6ok = fpost6ok
        sf._ng = never_ignore_fpost6ok
        sf._init4repr(rgnr, fpost6ok, never_ignore_fpost6ok)
    @property
    @override
    def wrapped_rgnr(sf, /):
        '-> ISimpleRecognizer'
        return sf._rgnr
    @property
    @override
    def fpost6ok(sf, /):
        '-> fpost6ok/(rgnz_oresult->rgnz_oresult)'
        return sf._fpost6ok
    @property
    @override
    def never_ignore_fpost6ok(sf, /):
        '-> bool'
        return sf._ng

#end-class SimpleRecognizer__post6ok(ISimpleRecognizer__post6ok):

class SimpleRecognizer__post6ok__overwrite_oresult_by_constant(ISimpleRecognizer__post6ok, _Base4repr):
    'post6ok__overwrite_oresult_by_constant@[maybe ignore]'
    ___no_slots_ok___ = True
    def __init__(sf, rgnr, rgnz_oresult, never_ignore_fpost6ok:bool, /):
        check_type_is(bool, never_ignore_fpost6ok)
        sf._rgnr = rgnr
        sf._o = rgnz_oresult
        sf._fpost6ok = const(rgnz_oresult)
        sf._ng = never_ignore_fpost6ok
        sf._init4repr(rgnr, rgnz_oresult, never_ignore_fpost6ok)
    @property
    @override
    def wrapped_rgnr(sf, /):
        '-> ISimpleRecognizer'
        return sf._rgnr
    @property
    @override
    def fpost6ok(sf, /):
        '-> fpost6ok/(rgnz_oresult->rgnz_oresult)'
        return sf._fpost6ok
    @property
    @override
    def never_ignore_fpost6ok(sf, /):
        '-> bool'
        return sf._ng

#end-class SimpleRecognizer__post6ok__overwrite_oresult_by_constant(ISimpleRecognizer__post6ok):




_const__null_rope = const(null_rope)
class SimpleRecognizer__post6ok__overwrite_oresult_by_null_rope(ISimpleRecognizer__post6ok, _Base4repr):
    'post6ok__overwrite_oresult_by_null_rope@[maybe ignore] #see:box4Rope'
    ___no_slots_ok___ = True
    def __init__(sf, rgnr, never_ignore_fpost6ok:bool, /):
        check_type_is(bool, never_ignore_fpost6ok)
        sf._rgnr = rgnr
        sf._ng = never_ignore_fpost6ok
        sf._init4repr(rgnr, never_ignore_fpost6ok)
    @property
    @override
    def wrapped_rgnr(sf, /):
        '-> ISimpleRecognizer'
        return sf._rgnr
    #@override
    fpost6ok = staticmethod(_const__null_rope)

    @property
    @override
    def never_ignore_fpost6ok(sf, /):
        '-> bool'
        return sf._ng

#end-class SimpleRecognizer__post6ok__overwrite_oresult_by_null_rope(ISimpleRecognizer__post6ok):





#.class SimpleRecognizer__serial(ISimpleRecognizer__post6ok):
#.    #vs:SimpleRecognizer__serial #deprecate by flatten4Rope
#.    #vs:SimpleRecognizer__chain
#.    'serial@[maybe ignore]'
#.    ___no_slots_ok___ = True
#.    def __init__(sf, rgnrs4protected, rgnrs4unprotected, never_ignore_serial_struct:bool, /):
#.        rgnr = SimpleRecognizer__chain(rgnrs4protected, rgnrs4unprotected, never_ignore_rope_struct:=never_ignore_serial_struct)
#.        super().__init__(rgnr, _fpost6ok4flatten4Rope, never_ignore_fpost6ok:=never_ignore_serial_struct)
#.        sf._init4repr(. .)
#.#end-class SimpleRecognizer__serial(ISimpleRecognizer__post6ok):

class SimpleRecognizer__flatten4Rope(SimpleRecognizer__post6ok, _Base4repr):
    #see:SimpleRecognizer__chain
    r'''[[[
    precondition:
        [child_rgnr.rgnz_oresult == (may oresult_parts/Rope)]
    postcondition:
        [this_rgnr.rgnz_oresult == (may oresult_parts/tuple)]
    #]]]'''#'''
    ___no_slots_ok___ = True
    def __init__(sf, rgnr, never_ignore_flatten4Rope:bool, /):
        super().__init__(rgnr, _fpost6ok4flatten4Rope, never_ignore_fpost6ok:=never_ignore_flatten4Rope)
        sf._init4repr(rgnr, never_ignore_flatten4Rope)
def _fpost6ok4flatten4Rope(rgnz_oresult, /):
    check_type_is(Rope, rgnz_oresult)
    _rgnz_oresult = tuple(rgnz_oresult)
    return _rgnz_oresult

class ISimpleRecognizer__post6ok__never_ignore_fpost6ok__init(ISimpleRecognizer__post6ok, _Base4repr):
    'box4Rope@[never_ignore_fpost6ok]'
    ___no_slots_ok___ = True
    def __init__(sf, rgnr, /):
        sf._rgnr = rgnr
        sf._init4repr(rgnr)
    @property
    @override
    def wrapped_rgnr(sf, /):
        '-> ISimpleRecognizer'
        return sf._rgnr
    #@override
    never_ignore_fpost6ok = True
#end-class ISimpleRecognizer__post6ok__never_ignore_fpost6ok__init(ISimpleRecognizer__post6ok):


class SimpleRecognizer__tag(ISimpleRecognizer__post6ok__never_ignore_fpost6ok__init):
    'tag@[never_ignore_fpost6ok]'
    def __init__(sf, rgnr, tag, /):
        super().__init__(rgnr)
        sf._tag = tag
        sf._init4repr(rgnr, tag)
    @override
    def fpost6ok(sf, rgnz_oresult, /):
        tag = sf._tag
        _rgnz_oresult = Cased(tag, rgnz_oresult)
        return _rgnz_oresult
#end-class SimpleRecognizer__tag(ISimpleRecognizer__post6ok__never_ignore_fpost6ok__init):



class SimpleRecognizer__box4Rope(ISimpleRecognizer__post6ok__never_ignore_fpost6ok__init):
    'box4Rope@[never_ignore_fpost6ok]#see:SimpleRecognizer__post6ok__overwrite_oresult_by_null_rope,SimpleRecognizer__unbox'
    #vs:SimpleRecognizer__box4Rope
    #vs:SimpleRecognizer__unbox
    @staticmethod
    @override
    def fpost6ok(rgnz_oresult, /):
        _rgnz_oresult = Rope((rgnz_oresult,))
        #_rgnz_oresult = Rope(*[(rgnz_oresult,)])

        return _rgnz_oresult
#end-class SimpleRecognizer__box4Rope(ISimpleRecognizer__post6ok__never_ignore_fpost6ok__init):

class SimpleRecognizer__unbox(ISimpleRecognizer__post6ok__never_ignore_fpost6ok__init):
    'unbox@[never_ignore_fpost6ok]'
    #vs:SimpleRecognizer__box4Rope
    #vs:SimpleRecognizer__unbox
    @staticmethod
    @override
    def fpost6ok(rgnz_oresult, /):
        [_rgnz_oresult] = rgnz_oresult
        return _rgnz_oresult
#end-class SimpleRecognizer__unbox(ISimpleRecognizer__post6ok__never_ignore_fpost6ok__init):



class SimpleRecognizer__local_ctx_manager__oresult_as_local_ctx4sibling(ISimpleRecognizer__post6ok__never_ignore_fpost6ok__init):
    r'''[[[
    'local_ctx_manager:oresult_as_local_ctx4sibling@[never_ignore_fpost6ok]'

    precondition:
        None
    postcondition:
        [this_rgnr.rgnz_oresult == WithLocalContext(null_rope, child_rgnr.rgnz_oresult)]
    #]]]'''#'''
    @staticmethod
    @override
    def fpost6ok(rgnz_oresult, /):
        _rgnz_oresult = WithLocalContext(may_oresult_parts:=null_rope, local_ctx4sibling:=rgnz_oresult)
        return _rgnz_oresult
#end-class SimpleRecognizer__local_ctx_manager__oresult_as_local_ctx4sibling(ISimpleRecognizer__post6ok__never_ignore_fpost6ok__init):

class SimpleRecognizer__local_ctx_manager__drop_local_ctx4sibling(ISimpleRecognizer__post6ok__never_ignore_fpost6ok__init):
    r'''[[[
    'local_ctx_manager:drop_local_ctx4sibling@[never_ignore_fpost6ok]'

    precondition:
        [child_rgnr.rgnz_oresult == WithLocalContext(may oresult_parts/Rope, local_ctx{sibling})]
    postcondition:
        [this_rgnr.rgnz_oresult == (may oresult_parts/Rope)]
    #]]]'''#'''
    @staticmethod
    @override
    def fpost6ok(rgnz_oresult, /):
        check_type_is(WithLocalContext, rgnz_oresult)

        _rgnz_oresult = rgnz_oresult.may_oresult_parts
        return _rgnz_oresult
#end-class SimpleRecognizer__local_ctx_manager__drop_local_ctx4sibling(ISimpleRecognizer__post6ok__never_ignore_fpost6ok__init):


class SimpleRecognizer__local_ctx_manager__tag_local_ctx4sibling_with_local_ctx4original(ISimpleRecognizer__post6ok__never_ignore_fpost6ok__init):
    r'''[[[
    'local_ctx_manager:tag_local_ctx4sibling_with_local_ctx4original@[never_ignore_fpost6ok]'

    precondition:
        [child_rgnr.rgnz_oresult == WithLocalContext(may oresult_parts/Rope, local_ctx{sibling})]
    postcondition:
        [this_rgnr.rgnz_oresult == WithLocalContext(may oresult_parts/Rope, (local_ctx{original},local_ctx{sibling}))]
    #]]]'''#'''

    @override
    def collect6pre(sf, args4recur_call, /):
        '-> infos6pre'
        local_ctx4original = args4recur_call.local_ctx
            #will occur as args of fpost6ok()
        return (local_ctx4original,)
    @staticmethod
    @override
    def fpost6ok(local_ctx4original, rgnz_oresult, /):
        check_type_is(WithLocalContext, rgnz_oresult)
        w = rgnz_oresult
        _rgnz_oresult = WithLocalContext(w.may_oresult_parts, (local_ctx4original, w.local_ctx4sibling))
        return _rgnz_oresult
#end-class SimpleRecognizer__local_ctx_manager__tag_local_ctx4sibling_with_local_ctx4original(ISimpleRecognizer__post6ok__never_ignore_fpost6ok__init):

class SimpleRecognizer__local_ctx_manager__using_local_ctx4original_as_local_ctx4sibling(ISimpleRecognizer__post6ok__never_ignore_fpost6ok__init):
    r'''[[[
    'local_ctx_manager:using_local_ctx4original_as_local_ctx4sibling@[never_ignore_fpost6ok]'

    precondition:
        [child_rgnr.rgnz_oresult == (may oresult_parts/Rope)]
    postcondition:
        [this_rgnr.rgnz_oresult == WithLocalContext(may oresult_parts/Rope, local_ctx{original})]
    #]]]'''#'''

    @override
    def collect6pre(sf, args4recur_call, /):
        '-> infos6pre'
        local_ctx4original = args4recur_call.local_ctx
            #will occur as args of fpost6ok()
        return (local_ctx4original,)
    @staticmethod
    @override
    def fpost6ok(local_ctx4original, rgnz_oresult, /):
        check_may_oresult_parts(rgnz_oresult)
        may_oresult_parts = rgnz_oresult
        _rgnz_oresult = WithLocalContext(may_oresult_parts, local_ctx4original)
        return _rgnz_oresult
#end-class SimpleRecognizer__local_ctx_manager__using_local_ctx4original_as_local_ctx4sibling(ISimpleRecognizer__post6ok__never_ignore_fpost6ok__init):



class ISimpleRecognizer__local_ctx_manager__projector4local_ctx(ISimpleRecognizer):
    r'''[[[
    'local_ctx_manager:projector4local_ctx # via ?getitem?'

    precondition{this_rgnr}:
        [old_local_ctx{===args4recur_call.local_ctx} can be arg of transfrom4local_ctx]
    precondition{child_rgnr}:
        [args4recur_call.local_ctx == new_local_ctx == transfrom4local_ctx(old_local_ctx)]
    #]]]'''#'''
    __slots__ = ()
    @property
    @abstractmethod
    def wrapped_rgnr(sf, /):
        '-> ISimpleRecognizer'
    @abstractmethod
    def transfrom4local_ctx(sf, old_local_ctx, /):
        'old-local_ctx -> new-local_ctx'
    #@abstractmethod
    def recover4local_ctx(sf, old_local_ctx, new_local_ctx, /):
        'old-local_ctx -> new-local_ctx -> old-local_ctx'
        return old_local_ctx
    @override
    def _recognize_(sf, args4recur_call, /):
        'IArgs4recur_call -> GI(yield:gi/GI;return:(BoxedTailRecur{recur-GI}|BoxedFinalResult{rgnz_reply/ISimpleRecognizeReply})'
        rgnr = sf.wrapped_rgnr
        777;    saved_local_ctx = args4recur_call.local_ctx
        777;    args4recur_call.local_ctx = sf.transfrom4local_ctx(saved_local_ctx)
        rgnz_reply = yield rgnr._recognize_(args4recur_call)
        777;    args4recur_call.local_ctx = sf.recover4local_ctx(saved_local_ctx, args4recur_call.local_ctx)
        return BoxedFinalResult(rgnz_reply)
        777;    yield
#
#end-class ISimpleRecognizer__local_ctx_manager__projector4local_ctx(ISimpleRecognizer):

class SimpleRecognizer__local_ctx_manager__projector4local_ctx(ISimpleRecognizer__local_ctx_manager__projector4local_ctx, _Base4repr):
    r'''[[[
    'local_ctx_manager:projector4local_ctx # via ?getitem?'

    precondition{this_rgnr}:
        [old_local_ctx{===args4recur_call.local_ctx} can be arg of transfrom4local_ctx]
    precondition{child_rgnr}:
        [args4recur_call.local_ctx == new_local_ctx == transfrom4local_ctx(old_local_ctx)]
    #]]]'''#'''
    ___no_slots_ok___ = True
    def __init__(sf, rgnr, transfrom4local_ctx, /):
        sf._rgnr = rgnr
        sf._f = transfrom4local_ctx
        sf._init4repr(rgnr, transfrom4local_ctx)
    @property
    @override
    def wrapped_rgnr(sf, /):
        '-> ISimpleRecognizer'
        return sf._rgnr
    @property
    @override
    def transfrom4local_ctx(sf, /):
        #def transfrom4local_ctx(sf, old_local_ctx, /):
        'old-local_ctx -> new-local_ctx'
        return sf._f

class SimpleRecognizer__local_ctx_manager__projector4local_ctx__via_getitem(ISimpleRecognizer__local_ctx_manager__projector4local_ctx, _Base4repr):
    r'''[[[
    'local_ctx_manager:projector4local_ctx # via __getitem__'

    precondition{this_rgnr}:
        [old_local_ctx{===args4recur_call.local_ctx}.__getitem__(key4local_ctx) is ok]
    precondition{child_rgnr}:
        [args4recur_call.local_ctx == new_local_ctx == old_local_ctx[key4local_ctx]]
    #]]]'''#'''
    ___no_slots_ok___ = True
    def __init__(sf, rgnr, key4local_ctx, /):
        sf._rgnr = rgnr
        sf._k = key4local_ctx
        sf._init4repr(rgnr, key4local_ctx)
    @property
    @override
    def wrapped_rgnr(sf, /):
        '-> ISimpleRecognizer'
        return sf._rgnr
    @override
    def transfrom4local_ctx(sf, old_local_ctx, /):
        'old-local_ctx -> new-local_ctx'
        return old_local_ctx[sf._k]











class SimpleRecognizer__many(ISimpleRecognizer, _Base4repr):
    #vs:SimpleRecognizer__chain
    #vs:SimpleRecognizer__nongreedy_end_by0
    #vs:SimpleRecognizer__many
    r'''[[[
    'many'

    [precondition&postcondition are same as those of SimpleRecognizer__chain]
    ==>>:
    precondition:
        [child_rgnr.rgnz_oresult == (may oresult_parts/Rope | WithLocalContext(may oresult_parts/Rope, local_ctx{sibling}))]
    postcondition:
        [this_rgnr.rgnz_oresult == (may oresult_parts/Rope | WithLocalContext(may oresult_parts/Rope, local_ctx{uncle}{===local_ctx4sibling{last-child_rgnr}}))]
    #]]]'''#'''
    ___no_slots_ok___ = True
    def __init__(sf, rgnr, min0, may_max, never_ignore_rope_struct:bool, /):
        check_type_is(bool, never_ignore_rope_struct)
        sf._rgnr = rgnr
        sf._min0 = min0
        sf._may_max = may_max
        if not may_max is None and min0 >= may_max:raise ValueError
        sf._ng = never_ignore_rope_struct
        sf._init4repr(rgnr, min0, may_max, never_ignore_rope_struct)
    @override
    def _recognize_(sf, args4recur_call, /):
        'IArgs4recur_call -> GI(yield:gi/GI;return:(BoxedTailRecur{recur-GI}|BoxedFinalResult{rgnz_reply/ISimpleRecognizeReply})'
        begin_idx = args4recur_call.begin_idx

        rgnr = sf._rgnr
        min0 = sf._min0
        may_max = sf._may_max

        never_ignore_rope_struct = sf._ng
        _ignore = not never_ignore_rope_struct and args4recur_call.ignore
        (may_ls, append, tmay_local_ctx4original, tmay_local_ctx4uncle) = _init4chain(_ignore)

        empty_ok = not may_max is None
        j = -1
        # [j+1 == len(ls)]
        for j in count_(0, may_max):
            # [j == len(ls)]
            _saved_begin_idx = args4recur_call.begin_idx
            rgnz_reply = yield rgnr._recognize_(args4recur_call)
            match rgnz_reply.rgnz_eresult:
                case Either(True, rgnz_oresult):
                    #bug:if not j and not empty_ok ...
                    if not empty_ok and _saved_begin_idx == args4recur_call.begin_idx:raise Exception('many{may_max==inf} but match span 0 length', sf, j, rgnr, _saved_begin_idx)
                    #xxx:check_type_is(Rope, rgnz_oresult)
                    may_oresult_parts = _handle6ok4chain(debug:=rgnr, tmay_local_ctx4original, tmay_local_ctx4uncle, args4recur_call, rgnz_oresult)
                    # [j == len(ls)]
                    append(may_oresult_parts)
                    #append(rgnz_oresult)
                    # [j+1 == len(ls)]
                case _:
                    # [j == len(ls)]
                    if j < min0:
                        #failure
                        return BoxedFinalResult(rgnz_reply)
                    # [j >= min0]
                    # [j == len(ls)]
                    #restore:begin_idx to prev-begin_idx
                    args4recur_call.begin_idx = _saved_begin_idx
                    break
            #ls
            # [j+1 == len(ls)]
        else:
            # [j+1 == len(ls)]
            j += 1
            # [j == len(ls)]
            assert j == may_max >= min0
            # [j >= min0]
        # [j == len(ls)]
        # [j >= min0]
        assert j >= min0
        #ls
        return _finalize4chain(tmay_local_ctx4original, tmay_local_ctx4uncle, args4recur_call, may_ls)
        777;    yield
        #.rgnz_oresult = None if _ignore else Rope(*ls)
        #.rgnz_eresult = mk_Right(rgnz_oresult)
        #.end_idx4reply = args4recur_call.begin_idx
        #.rgnz_reply = args4recur_call.mk_rgnz_reply_(end_idx4reply, rgnz_eresult)
        #.return BoxedFinalResult(rgnz_reply)

#end-class SimpleRecognizer__many(ISimpleRecognizer):


class SimpleRecognizer__optional(SimpleRecognizer__many):
    r'''[[[
    'optional'

    [precondition&postcondition are same as those of SimpleRecognizer__chain]
    ==>>:
    precondition:
        [child_rgnr.rgnz_oresult == (may oresult_parts/Rope | WithLocalContext(may oresult_parts/Rope, local_ctx{sibling}))]
    postcondition:
        [this_rgnr.rgnz_oresult == (may oresult_parts/Rope | WithLocalContext(may oresult_parts/Rope, local_ctx{uncle}{===local_ctx4sibling{last-child_rgnr}}))]
    #]]]'''#'''
    def __init__(sf, rgnr, never_ignore_rope_struct:bool, /):
        super().__init__(rgnr, 0, 1, never_ignore_rope_struct)
        sf._init4repr(rgnr, never_ignore_rope_struct)
#end-class SimpleRecognizer__optional(ISimpleRecognizer):




class SimpleRecognizer__look_ahead(ISimpleRecognizer, _Base4repr):
    #vs:SimpleRecognizer__not_follow_by
    #vs:SimpleRecognizer__look_ahead
    r'''[[[
    'look_ahead'

    precondition:
        None
    postcondition:
        [this_rgnr.rgnz_oresult == child_rgnr.rgnz_oresult]
        [args4recur_call.begin_idx keeps unchanged]
    #]]]'''#'''
    ___no_slots_ok___ = True
    def __init__(sf, rgnr, /):
        sf._rgnr = rgnr
        sf._init4repr(rgnr)
    @override
    def _recognize_(sf, args4recur_call, /):
        'IArgs4recur_call -> GI(yield:gi/GI;return:(BoxedTailRecur{recur-GI}|BoxedFinalResult{rgnz_reply/ISimpleRecognizeReply})'
        begin_idx = args4recur_call.begin_idx
        rgnr = sf._rgnr
        rgnz_reply = yield rgnr._recognize_(args4recur_call)
        #restore:args4recur_call.begin_idx
        args4recur_call.begin_idx = begin_idx
        return BoxedFinalResult(rgnz_reply)
        777;    yield

#end-class SimpleRecognizer__look_ahead(ISimpleRecognizer):


class SimpleRecognizer__not_follow_by(ISimpleRecognizer, _Base4repr):
    #vs:SimpleRecognizer__not_follow_by
    #vs:SimpleRecognizer__look_ahead
    r'''[[[
    'not_follow_by'

    precondition:
        None
    postcondition:
        [this_rgnr.rgnz_eresult == child_rgnr{ignore}.rgnz_eresult.flip()]
        [args4recur_call.begin_idx keeps unchanged]
    #]]]'''#'''
    ___no_slots_ok___ = True
    def __init__(sf, rgnr, /):
        sf._rgnr = SimpleRecognizer__look_ahead(SimpleRecognizer__ignore_manager__always_ignore(rgnr))
        sf._init4repr(rgnr)
    @override
    def _recognize_(sf, args4recur_call, /):
        'IArgs4recur_call -> GI(yield:gi/GI;return:(BoxedTailRecur{recur-GI}|BoxedFinalResult{rgnz_reply/ISimpleRecognizeReply})'
        rgnr = sf._rgnr
        rgnz_reply = yield rgnr._recognize_(args4recur_call)
        rgnz_eresult = rgnz_reply.rgnz_eresult.flip()
        rgnz_reply = rgnz_reply.ireplace_(rgnz_eresult=rgnz_eresult)
        return BoxedFinalResult(rgnz_reply)
        777;    yield
#end-class SimpleRecognizer__not_follow_by(ISimpleRecognizer):

class SimpleRecognizer__ref(ISimpleRecognizer, _Base4repr):
    'ref #ci_post:see:SimpleRecognizer__lift,seed.func_tools.func_access.FuncAccess'
    ___no_slots_ok___ = True
    def __init__(sf, nm4rgnr, /):
        sf._nm = nm4rgnr
        sf._init4repr(nm4rgnr)
    @override
    def _recognize_(sf, args4recur_call, /):
        'IArgs4recur_call -> GI(yield:gi/GI;return:(BoxedTailRecur{recur-GI}|BoxedFinalResult{rgnz_reply/ISimpleRecognizeReply})'
        nm4rgnr = sf._nm
        ignore = args4recur_call.ignore
        rgnr5name_ = args4recur_call.common4recur_call.rgnr_name_server.rgnr5name_
        rgnr = rgnr5name_(nm4rgnr)
        rgnz_reply = yield rgnr._recognize_(args4recur_call)
        m = None if ignore else args4recur_call.common4recur_call.may_ci_postprocess5name4ref_(nm4rgnr)
        if not m is None:
            ci_post = m
            (case, payload) = rgnz_eresult = rgnz_reply.rgnz_eresult
            _payload = ci_post(rgnz_eresult)
            if not _payload is payload:
                rgnz_eresult = Either(case, _payload)
                rgnz_reply = rgnz_reply.ireplace_(rgnz_eresult=rgnz_eresult)
        return BoxedFinalResult(rgnz_reply)
        777;    yield

#end-class SimpleRecognizer__ref(ISimpleRecognizer):



class SimpleRecognizer__constant(ISimpleRecognizer, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, rgnz_eresult, /):
        check_type_is(Either, rgnz_eresult)
        sf._er = rgnz_eresult
        sf._init4repr(rgnz_eresult)
    @override
    def _recognize_(sf, args4recur_call, /):
        'IArgs4recur_call -> GI(yield:gi/GI;return:(BoxedTailRecur{recur-GI}|BoxedFinalResult{rgnz_reply/ISimpleRecognizeReply})'
        rgnz_eresult = sf._er
        end_idx4reply = args4recur_call.begin_idx
        rgnz_reply = args4recur_call.mk_rgnz_reply_(end_idx4reply, rgnz_eresult)
        return BoxedFinalResult(rgnz_reply)
        777;    yield

#end-class SimpleRecognizer__constant(ISimpleRecognizer):



class SimpleRecognizer__local_ctx_manager__long_distance_local_ctx_controller(SimpleRecognizer__chain):
    r'''[[[
    'local_ctx_manager:long_distance_local_ctx_controller'

    precondition{rgnr8open}:
        [rgnr8open.rgnz_oresult == WithLocalContext(may oresult_parts/Rope, local_ctx{sibling})]
    precondition{rgnr8body}:
        [rgnr8body@{args4recur_call.local_ctx===local_ctx{this_rgnr.original}}]
    precondition{rgnr8close}:
        [rgnr8close@{args4recur_call.local_ctx===local_ctx4sibling{rgnr8open}}]
    postcondition:
        [this_rgnr.rgnz_oresult == (may oresult_parts/Rope | WithLocalContext(may oresult_parts/Rope, local_ctx{uncle}{===local_ctx4sibling{rgnr8close}}))]
    #]]]'''#'''
    r'''[[[
    dependent_pair<<==:
        args4recur_call:++local_ctx
        local_ctx_manager
            context-dependent grammar
            context-sensitive
            remote/long-range/long-distance local_ctx controller
    #]]]'''#'''
    def __init__(sf, rgnr8open, rgnr8body, rgnr8close, never_ignore_rope_struct:bool, /):
        _rgnr8open = SimpleRecognizer__local_ctx_manager__tag_local_ctx4sibling_with_local_ctx4original(rgnr8open)
            # WithLocalContext(..., local_ctx4sibling)
            # -->WithLocalContext(..., (local_ctx4original, local_ctx4sibling))
        _rgnr8body = SimpleRecognizer__local_ctx_manager__projector4local_ctx__via_getitem(rgnr8body, 0)
            # (local_ctx4original, local_ctx4sibling)
            # -->local_ctx4original
        _rgnr8close = SimpleRecognizer__local_ctx_manager__projector4local_ctx__via_getitem(rgnr8close, 1)
            # (local_ctx4original, local_ctx4sibling)
            # -->local_ctx4sibling
            #
        rgnrs4protected = [_rgnr8open]
        rgnrs4unprotected = [_rgnr8body, _rgnr8close]
        super().__init__(rgnrs4protected, rgnrs4unprotected, never_ignore_rope_struct)
        sf._init4repr(rgnr8open, rgnr8body, rgnr8close, never_ignore_rope_struct)

#end-class SimpleRecognizer__local_ctx_manager__long_distance_local_ctx_controller(SimpleRecognizer__chain):


class SimpleRecognizer__local_ctx_manager__dependent_pair(SimpleRecognizer__chain):
    r'''[[[
    'local_ctx_manager:dependent_pair'

    precondition{rgnr8body}:
        [rgnr8body@{args4recur_call.local_ctx===rgnr8head.rgnz_oresult}]
    postcondition:
        [this_rgnr.rgnz_oresult == (may oresult_parts/Rope | WithLocalContext(may oresult_parts/Rope, local_ctx{uncle}{===local_ctx4sibling{rgnr8body}}))]
    #]]]'''#'''
    def __init__(sf, rgnr8head, rgnr8body, never_ignore_rope_struct:bool, /):
        _rgnr8head = SimpleRecognizer__local_ctx_manager__oresult_as_local_ctx4sibling(rgnr8head)
            # rgnz_oresult{head}
            # -->WithLocalContext(null_rope, local_ctx4sibling:=rgnz_oresult{head})
        rgnrs4protected = [_rgnr8head]
        rgnrs4unprotected = [rgnr8body]
        super().__init__(rgnrs4protected, rgnrs4unprotected, never_ignore_rope_struct)
        sf._init4repr(rgnr8head, rgnr8body, never_ignore_rope_struct)

#end-class SimpleRecognizer__local_ctx_manager__dependent_pair(SimpleRecognizer__chain):

class ISimpleRecognizer__ignore_manager__init(ISimpleRecognizer, _Base4repr):
    'ignore_manager'
    ___no_slots_ok___ = True
    def __init__(sf, rgnr, /):
        #check_type_is(bool, ignore)
        sf._rgnr = rgnr
        #sf._g = ignore
        sf._init4repr(rgnr)
    @property
    @abstractmethod
    def ignore(sf, /):
        '-> bool'
    @override
    def _recognize_(sf, args4recur_call, /):
        'IArgs4recur_call -> GI(yield:gi/GI;return:(BoxedTailRecur{recur-GI}|BoxedFinalResult{rgnz_reply/ISimpleRecognizeReply})'
        rgnr = sf._rgnr
        saved_ignore = args4recur_call.ignore
        777;    args4recur_call.ignore = sf.ignore
        rgnz_reply = yield rgnr._recognize_(args4recur_call)
        777;    args4recur_call.ignore = saved_ignore
        return BoxedFinalResult(rgnz_reply)
        777;    yield
#end-class ISimpleRecognizer__ignore_manager__init(ISimpleRecognizer):

class SimpleRecognizer__ignore_manager__always_ignore(ISimpleRecognizer__ignore_manager__init):
    'ignore_manager:always_ignore'
    #@override
    ignore = True

class SimpleRecognizer__ignore_manager__never_ignore(ISimpleRecognizer__ignore_manager__init):
    'ignore_manager:never_ignore'
    #@override
    ignore = False

class SimpleRecognizer__lift(ISimpleRecognizer, _Base4repr):
    'lift#update [rgnz_reply.rgnz_eresult.payload:=(infos6pre, infos6post, rgnz_reply)] #to be used with ci_post@SimpleRecognizer__ref'
    ___no_slots_ok___ = True
    def __init__(sf, rgnr, /):
        sf._rgnr = rgnr
        sf._init4repr(rgnr)
    def collect6pre(sf, args4recur_call, /):
        '-> infos6pre'
        return (args4recur_call.begin_idx, args4recur_call.restored_mutable_args, args4recur_call.common4recur_call)
    def collect6post(sf, args4recur_call, /):
        '-> infos6post'
        return (args4recur_call.begin_idx,)
    @override
    def _recognize_(sf, args4recur_call, /):
        'IArgs4recur_call -> GI(yield:gi/GI;return:(BoxedTailRecur{recur-GI}|BoxedFinalResult{rgnz_reply/ISimpleRecognizeReply})'
        rgnr = sf._rgnr
        777;    infos6pre = sf.collect6pre(args4recur_call)
        rgnz_reply = yield rgnr._recognize_(args4recur_call)
        777;    infos6post = sf.collect6post(args4recur_call)
        (case, payload) = rgnz_eresult = rgnz_reply.rgnz_eresult
        _payload = (infos6pre, infos6post, rgnz_reply)
        rgnz_eresult = Either(case, _payload)
        rgnz_reply = rgnz_reply.ireplace_(rgnz_eresult=rgnz_eresult)
        return BoxedFinalResult(rgnz_reply)
        777;    yield
#end-class SimpleRecognizer__lift(ISimpleRecognizer):



class SimpleRecognizer__nongreedy_end_by0(ISimpleRecognizer, _Base4repr):
    #vs:SimpleRecognizer__nongreedy_end_by0
    #vs:SimpleRecognizer__many
    r'''[[[
    'nongreedy_end_by0'

    [precondition&postcondition are same as those of SimpleRecognizer__chain]
    ==>>:
    precondition:
        [child_rgnr.rgnz_oresult == (may oresult_parts/Rope | WithLocalContext(may oresult_parts/Rope, local_ctx{sibling}))]
    postcondition:
        [this_rgnr.rgnz_oresult == (may oresult_parts/Rope | WithLocalContext(may oresult_parts/Rope, local_ctx{uncle}{===local_ctx4sibling{last-child_rgnr}}))]
    #]]]'''#'''
    ___no_slots_ok___ = True
    def __init__(sf, rgnr8end, rgnr8body, never_ignore_rope_struct:bool, /):
        check_type_is(bool, never_ignore_rope_struct)
        sf._rgnr8end = rgnr8end
        sf._rgnr8body = rgnr8body
        sf._ng = never_ignore_rope_struct
        sf._init4repr(rgnr8end, rgnr8body, never_ignore_rope_struct)
    @override
    def _recognize_(sf, args4recur_call, /):
        'IArgs4recur_call -> GI(yield:gi/GI;return:(BoxedTailRecur{recur-GI}|BoxedFinalResult{rgnz_reply/ISimpleRecognizeReply})'
        rgnr8end = sf._rgnr8end
        rgnr8body = sf._rgnr8body

        begin_idx = args4recur_call.begin_idx
        never_ignore_rope_struct = sf._ng
        _ignore = not never_ignore_rope_struct and args4recur_call.ignore
        (may_ls, append, tmay_local_ctx4original, tmay_local_ctx4uncle) = _init4chain(_ignore)
        while 1:
            _saved_begin_idx = args4recur_call.begin_idx
            rgnz_reply = yield rgnr8end._recognize_(args4recur_call)
            match rgnz_reply.rgnz_eresult:
                case Either(True, rgnz_oresult):
                    may_oresult_parts = _handle6ok4chain(debug:=rgnr8end, tmay_local_ctx4original, tmay_local_ctx4uncle, args4recur_call, rgnz_oresult)
                    append(may_oresult_parts)
                    break
                case _:
                    #failure{rgnr8end}
                    if not args4recur_call.begin_idx == _saved_begin_idx:
                        #non-recoverable_failure{rgnr8end}
                        return BoxedFinalResult(rgnz_reply)
                    #recoverable_failure{rgnr8end}
            #recoverable_failure{rgnr8end}
            #=> apply rgnr8body
            rgnz_reply = yield rgnr8body._recognize_(args4recur_call)
            match rgnz_reply.rgnz_eresult:
                case Either(True, rgnz_oresult):
                    may_oresult_parts = _handle6ok4chain(debug:=rgnr8body, tmay_local_ctx4original, tmay_local_ctx4uncle, args4recur_call, rgnz_oresult)
                    append(may_oresult_parts)
                    #continue
                case _:
                    #failure{rgnr8body}
                    return BoxedFinalResult(rgnz_reply)
        return _finalize4chain(tmay_local_ctx4original, tmay_local_ctx4uncle, args4recur_call, may_ls)
        777;    yield
#end-class SimpleRecognizer__nongreedy_end_by0(ISimpleRecognizer):



class SimpleRecognizer__sep_by1(ISimpleRecognizer, _Base4repr):
    r'''[[[
    'sep_by1'

    [precondition&postcondition are same as those of SimpleRecognizer__chain]
    ==>>:
    precondition:
        [child_rgnr.rgnz_oresult == (may oresult_parts/Rope | WithLocalContext(may oresult_parts/Rope, local_ctx{sibling}))]
    postcondition:
        [this_rgnr.rgnz_oresult == (may oresult_parts/Rope | WithLocalContext(may oresult_parts/Rope, local_ctx{uncle}{===local_ctx4sibling{last-child_rgnr}}))]
    #]]]'''#'''
    ___no_slots_ok___ = True
    def __init__(sf, rgnr8sep, rgnr8body, min0, may_max, never_ignore_rope_struct:bool, /):
        check_int_ge(0, min0)
        if not may_max is None:
            check_int_ge(min0, may_max)
        check_type_is(bool, never_ignore_rope_struct)
        sf._rgnr8sep = rgnr8sep
        sf._rgnr8body = rgnr8body
        sf._ng = never_ignore_rope_struct
        rgnr8sep_body = SimpleRecognizer__chain([], [rgnr8sep, rgnr8body], never_ignore_rope_struct)
        rgnr8tail = SimpleRecognizer__many(rgnr8sep_body, max(0,min0-1), None if may_max is None else max(0,may_max-1), never_ignore_rope_struct)
        rgnr1 = SimpleRecognizer__chain([], [rgnr8body, rgnr8tail], never_ignore_rope_struct)
        rgnr0 = SimpleRecognizer__optional(rgnr1, never_ignore_rope_struct)
        rgnr8whole = rgnr1 if min0 > 0 else rgnr0
        sf._rgnr8whole = rgnr8whole
        sf._init4repr(rgnr8sep, rgnr8body, min0, may_max, never_ignore_rope_struct)
    @override
    def _recognize_(sf, args4recur_call, /):
        'IArgs4recur_call -> GI(yield:gi/GI;return:(BoxedTailRecur{recur-GI}|BoxedFinalResult{rgnz_reply/ISimpleRecognizeReply})'
        rgnr8whole = sf._rgnr8whole
        return BoxedTailRecur(rgnr8whole._recognize_(args4recur_call))
        777;    yield
#end-class SimpleRecognizer__sep_by1(ISimpleRecognizer):

_nms4neat__str = (r'''
box4Rope
chain
constant
flatten4Rope
ignore_manager__always_ignore
ignore_manager__never_ignore
lift
local_ctx_as_dispatch_key
local_ctx_manager__dependent_pair
local_ctx_manager__drop_local_ctx4sibling
local_ctx_manager__long_distance_local_ctx_controller
local_ctx_manager__oresult_as_local_ctx4sibling
local_ctx_manager__projector4local_ctx
local_ctx_manager__projector4local_ctx__via_getitem
local_ctx_manager__tag_local_ctx4sibling_with_local_ctx4original
local_ctx_manager__using_local_ctx4original_as_local_ctx4sibling
look_ahead
many
nongreedy_end_by0
not_follow_by
optional
post6ok
post6ok__overwrite_oresult_by_constant
post6ok__overwrite_oresult_by_null_rope
py_regex
py_str
ref
sep_by1
switch
tag
unbox
'''.strip()#'''
)
def __():
    prefix = 'SimpleRecognizer__'
    nms4neat = []
    for nm, x in sorted(globals().items()):
        if nm.startswith(prefix):
            nms4neat.append(nm[len(prefix):])
    return nms4neat
assert (__:='\n'.join(__())) == _nms4neat__str, __
class AllSimpleRecognizers:
    locals().update((nm, globals()[f'SimpleRecognizer__{nm}']) for nm in _nms4neat__str.split())

def __():
    return [nm for nm in _nms4neat__str.split() for cls in [globals()[f'SimpleRecognizer__{nm}']] if not issubclass(cls, _Base4repr)]
assert not (__:=__()), __

__all__
from seed.recognize.rgnr.rgnrs.SimpleRecognizer import AllSimpleRecognizers #_nms4neat__str:goto
from seed.recognize.rgnr.rgnrs.SimpleRecognizer import *
