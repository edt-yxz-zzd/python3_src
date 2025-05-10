#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/rgnr/rgnrs/SimpleRecognizer.py
view ../../python3_src/seed/recognize/rgnr/abc/ISimpleRecognizer.py

seed.recognize.rgnr.rgnrs.SimpleRecognizer
py -m nn_ns.app.debug_cmd   seed.recognize.rgnr.rgnrs.SimpleRecognizer -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.recognize.rgnr.rgnrs.SimpleRecognizer:__doc__ -ht # -ff -df

[[
]]

py_adhoc_call   seed.recognize.rgnr.rgnrs.SimpleRecognizer   @f
from seed.recognize.rgnr.rgnrs.SimpleRecognizer import *
]]]'''#'''
__all__ = r'''
SimpleRecognizer__serial
SimpleRecognizer__parallel
SimpleRecognizer__py_regex
    SimpleRecognizer__py_str
SimpleRecognizer__post6ok
SimpleRecognizer__many
    SimpleRecognizer__optional
SimpleRecognizer__lookahead
SimpleRecognizer__ref
SimpleRecognizer__constant
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.func_tools.recur5yield__strict import BoxedTailRecur, BoxedFinalResult
from seed.recognize.rgnr.abc.ISimpleRecognizer import ISimpleRecognizer, Case4ISimpleRecognizeReply, ISimpleRecognizeReply, IArgs4recur_call, ICommon4recur_call, ISimpleRecognizerNameServer, IInputSeqEx
import re

from seed.tiny_.containers import mk_tuple
from seed.iters.count_ import count_

#.from itertools import islice
from seed.tiny_.check import check_type_is, check_int_ge, check_pair
#.
from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError




_C = Case4ISimpleRecognizeReply
class SimpleRecognizer__serial(ISimpleRecognizer):
    ___no_slots_ok___ = True
    def __init__(sf, rgnrs4CONTINUE, rgnrs4inherit, rgnrs4BREAK, /):
        rgnrs4CONTINUE = mk_tuple(rgnrs4CONTINUE)
        rgnrs4inherit = mk_tuple(rgnrs4inherit)
        rgnrs4BREAK = mk_tuple(rgnrs4BREAK)
        sf._rs0 = rgnrs4CONTINUE
        sf._rs1 = rgnrs4inherit
        sf._rs2 = rgnrs4BREAK
        sf._rs = (*rgnrs4CONTINUE, *rgnrs4inherit, *rgnrs4BREAK)
        sf._kA = len(rgnrs4CONTINUE)
        sf._kB = len(rgnrs4CONTINUE) + len(rgnrs4inherit)
    @override
    def _recognize_(sf, args4recur_call, /):
        'IArgs4recur_call -> GI(yield:gi/GI;return:(BoxedTailRecur{recur-GI}|BoxedFinalResult{rgnz_reply/ISimpleRecognizeReply})'
        (begin_idx, _end_idx, ignore) = args4recur_call.mutable_args
        #rgnrs4CONTINUE = sf._rs0
        #rgnrs4BREAK = sf._rs1
        rgnrs = sf._rs
        kA = sf._kA
        kB = sf._kB
        #rgnr5or_name_ = args4recur_call.common4recur_call.rgnr_name_server.rgnr5or_name_
        if ignore:
            def append(x, /):pass
        else:
            ls = []
            append = ls.append
        append
        failure = True
        for j, rgnr in enumerate(rgnrs):
            #rgnr = rgnr5or_name_(rgnr)
            rgnz_reply = yield rgnr._recognize_(args4recur_call)
            match rgnz_reply.rgnz_cresult:
                case (_C.RETURN, rgnz_oresult):
                    append(rgnz_oresult)
                case (_C.CONTINUE, rgnz_errmsg):
                    if j >= kB:
                        #rgnrs4BREAK
                        rgnz_reply = rgnz_reply.ireplace_(rgnz_cresult=(_C.BREAK, rgnz_errmsg))
                    break
                    return BoxedFinalResult(rgnz_reply)
                case (_C.BREAK, rgnz_errmsg):
                    if j < kA:
                        #rgnrs4CONTINUE
                        rgnz_reply = rgnz_reply.ireplace_(rgnz_cresult=(_C.CONTINUE, rgnz_errmsg))
                    break
                    return BoxedFinalResult(rgnz_reply)
                case _:
                    raise 000
            #ls
            #no:begin_idx = rgnz_reply.end_idx4reply
            #no:args4recur_call.mutable_args = (begin_idx, end_idx, ignore)
            #no:begin_idx = args4recur_call.begin_idx
        else:
            failure = False
        if failure:
            rgnz_reply
            #restore:args4recur_call.begin_idx
            #args4recur_call.mutable_args = (begin_idx, end_idx, ignore)
            args4recur_call.begin_idx = begin_idx
            return BoxedFinalResult(rgnz_reply)
        #ls
        rgnz_oresult = None if ignore else ls
        rgnz_cresult = (_C.RETURN, rgnz_oresult)
        end_idx4reply = args4recur_call.begin_idx
        rgnz_reply = args4recur_call.mk_rgnz_reply_(end_idx4reply, rgnz_cresult)
        return BoxedFinalResult(rgnz_reply)
#end-class SimpleRecognizer__serial(ISimpleRecognizer):

class SimpleRecognizer__parallel(ISimpleRecognizer):
    ___no_slots_ok___ = True
    def __init__(sf, with_idx8tag, rgnrs, /):
        with_idx8tag = bool(with_idx8tag)
        rgnrs = mk_tuple(rgnrs)
        #if not rgnrs:raise ValueError
        sf._rs = rgnrs
        sf._with_idx8tag = with_idx8tag
    @override
    def _recognize_(sf, args4recur_call, /):
        'IArgs4recur_call -> GI(yield:gi/GI;return:(BoxedTailRecur{recur-GI}|BoxedFinalResult{rgnz_reply/ISimpleRecognizeReply})'
        #.(begin_idx, end_idx, ignore) = args4recur_call.mutable_args
        ignore = args4recur_call.ignore
        rgnrs = sf._rs
        with_idx8tag = sf._with_idx8tag
        if not rgnrs:
            rgnz_cresult = (_C.CONTINUE, 'no_branches')
            end_idx4reply = args4recur_call.begin_idx
            rgnz_reply = args4recur_call.mk_rgnz_reply_(end_idx4reply, rgnz_cresult)
            return BoxedFinalResult(rgnz_reply)

        #rgnr5or_name_ = args4recur_call.common4recur_call.rgnr_name_server.rgnr5or_name_
        ls = []
        append = ls.append
        for j, rgnr in enumerate(rgnrs):
            #rgnr = rgnr5or_name_(rgnr)
            rgnz_reply = yield rgnr._recognize_(args4recur_call)
            match rgnz_reply.rgnz_cresult:
                case (_C.RETURN, rgnz_oresult):
                    # [case==RETURN]
                    break
                case (_C.CONTINUE, rgnz_errmsg):
                    append((rgnz_reply.end_idx4reply, j, rgnz_reply))
                case (_C.BREAK, rgnz_errmsg):
                    # [case==BREAK]
                    break
                case _:
                    raise 000
            ls
            #no:begin_idx = rgnz_reply.end_idx4reply
            #no:args4recur_call.mutable_args = (begin_idx, end_idx, ignore)
        else:
            ls
            if ls:
                (end_idx4reply, j, rgnz_reply) = max(ls)
                # [case==CONTINUE]
            else:
                raise 000
        j, rgnz_reply
        (case, payload) = rgnz_reply.rgnz_cresult
            # 3 cases are all possible...
        payload0 = payload
        #bug:if ignore: payload = None
            # !! payload<ignore>
        if with_idx8tag:
            payload = (j, payload)
        if not payload is payload0:
            rgnz_cresult = (case, payload)
            rgnz_reply = rgnz_reply.ireplace_(rgnz_cresult=rgnz_cresult)
        return BoxedFinalResult(rgnz_reply)
#end-class SimpleRecognizer__parallel(ISimpleRecognizer):




class SimpleRecognizer__py_regex(ISimpleRecognizer):
    ___no_slots_ok___ = True
    def __init__(sf, regex, /):
        if not hasattr(regex, 'match'):
            regex = re.compile(regex)
        sf._regex = regex
    @override
    def _recognize_(sf, args4recur_call, /):
        'IArgs4recur_call -> GI(yield:gi/GI;return:(BoxedTailRecur{recur-GI}|BoxedFinalResult{rgnz_reply/ISimpleRecognizeReply})'
        (begin_idx, end_idx, ignore) = args4recur_call.mutable_args
        regex = sf._regex
        s = args4recur_call.common4recur_call.input_seq_ex.seq_view
        #check_type_is(str, s)
        m = regex.match(s, begin_idx, end_idx)
        if m is None:
            end_idx4reply = begin_idx
            case = _C.CONTINUE
        else:
            end_idx4reply = m.end()
            777;    args4recur_call.begin_idx = end_idx4reply
            case = _C.RETURN
        payload = None if ignore else m

        rgnz_cresult = (case, payload)
        rgnz_reply = args4recur_call.mk_rgnz_reply_(end_idx4reply, rgnz_cresult)
        return BoxedFinalResult(rgnz_reply)

#end-class SimpleRecognizer__py_regex(ISimpleRecognizer):

class SimpleRecognizer__py_str(ISimpleRecognizer):
    ___no_slots_ok___ = True
    def __init__(sf, s, /):
        sf._s = s
    @override
    def _recognize_(sf, args4recur_call, /):
        'IArgs4recur_call -> GI(yield:gi/GI;return:(BoxedTailRecur{recur-GI}|BoxedFinalResult{rgnz_reply/ISimpleRecognizeReply})'
        (begin_idx, end_idx, ignore) = args4recur_call.mutable_args
        s = sf._s
        ss = args4recur_call.common4recur_call.input_seq_ex.seq_view
        if not ss.startswith(s, begin_idx, end_idx):
            end_idx4reply = begin_idx
            case = _C.CONTINUE
        else:
            end_idx4reply = begin_idx+len(s)
            777;    args4recur_call.begin_idx = end_idx4reply
            case = _C.RETURN
        payload = None if ignore else s

        rgnz_cresult = (case, payload)
        rgnz_reply = args4recur_call.mk_rgnz_reply_(end_idx4reply, rgnz_cresult)
        return BoxedFinalResult(rgnz_reply)

#end-class SimpleRecognizer__py_str(ISimpleRecognizer):




class SimpleRecognizer__post6ok(ISimpleRecognizer):
    ___no_slots_ok___ = True
    def __init__(sf, rgnr, fpost6ok, /):
        sf._rgnr = rgnr
        sf._fpost6ok = fpost6ok
    @override
    def _recognize_(sf, args4recur_call, /):
        'IArgs4recur_call -> GI(yield:gi/GI;return:(BoxedTailRecur{recur-GI}|BoxedFinalResult{rgnz_reply/ISimpleRecognizeReply})'
        #.(begin_idx, end_idx, ignore) = args4recur_call.mutable_args
        begin_idx = args4recur_call.begin_idx
        rgnr = sf._rgnr
        fpost6ok = sf._fpost6ok
        #rgnr5or_name_ = args4recur_call.common4recur_call.rgnr_name_server.rgnr5or_name_
        #rgnr = rgnr5or_name_(rgnr)
        rgnz_reply = yield rgnr._recognize_(args4recur_call)
        match rgnz_reply.rgnz_cresult:
            case (_C.RETURN, rgnz_oresult):
                _rgnz_oresult = fpost6ok(rgnz_oresult)
                if not _rgnz_oresult is rgnz_oresult:
                    rgnz_cresult = (_C.RETURN, _rgnz_oresult)
                    rgnz_reply = rgnz_reply.ireplace_(rgnz_cresult=rgnz_cresult)
        return BoxedFinalResult(rgnz_reply)

#end-class SimpleRecognizer__post6ok(ISimpleRecognizer):


class SimpleRecognizer__many(ISimpleRecognizer):
    ___no_slots_ok___ = True
    def __init__(sf, rgnr, min0, may_max, /):
        sf._rgnr = rgnr
        sf._min0 = min0
        sf._may_max = may_max
        if not may_max is None and min0 >= may_max:raise ValueError
    @override
    def _recognize_(sf, args4recur_call, /):
        'IArgs4recur_call -> GI(yield:gi/GI;return:(BoxedTailRecur{recur-GI}|BoxedFinalResult{rgnz_reply/ISimpleRecognizeReply})'
        (begin_idx, _end_idx, ignore) = args4recur_call.mutable_args
        rgnr = sf._rgnr
        min0 = sf._min0
        may_max = sf._may_max
        #rgnr5or_name_ = args4recur_call.common4recur_call.rgnr_name_server.rgnr5or_name_
        #rgnr = rgnr5or_name_(rgnr)
        if ignore:
            def _append(x, /):pass
        else:
            ls = []
            _append = ls.append
        append
        empty_ok = not may_max is None
        failure = True
        j = -1
        for j in count_(0, may_max):
            #assert j == len(ls)
            if empty_ok:
                _saved_begin_idx = args4recur_call.begin_idx
            rgnz_reply = yield rgnr._recognize_(args4recur_call)
            match rgnz_reply.rgnz_cresult:
                case (_C.RETURN, rgnz_oresult):
                    #bug:if not j and not empty_ok ...
                    if not empty_ok and _saved_begin_idx == args4recur_call.begin_idx:raise Exception('many{inf} but match span 0 length', sf, j, rgnr, _saved_begin_idx)
                    append(rgnz_oresult)
                case (_C.CONTINUE, rgnz_errmsg):
                    if j >= min0:
                        failure = False
                        break
                    #failure
                    if j >= 1:
                        #BREAK
                        rgnz_reply = rgnz_reply.ireplace_(rgnz_cresult=(_C.BREAK, rgnz_errmsg))
                    break
                    return BoxedFinalResult(rgnz_reply)
                case (_C.BREAK, rgnz_errmsg):
                    break
                    return BoxedFinalResult(rgnz_reply)
                case _:
                    raise 000
            #ls
        else:
            j += 1
            assert j >= min0
            failure = False
        if failure:
            rgnz_reply
            #restore:args4recur_call.begin_idx
            args4recur_call.begin_idx = begin_idx
            return BoxedFinalResult(rgnz_reply)
        #ls
        rgnz_oresult = None if ignore else ls
        rgnz_cresult = (_C.RETURN, rgnz_oresult)
        end_idx4reply = args4recur_call.begin_idx
        rgnz_reply = args4recur_call.mk_rgnz_reply_(end_idx4reply, rgnz_cresult)
        return BoxedFinalResult(rgnz_reply)

#end-class SimpleRecognizer__many(ISimpleRecognizer):


class SimpleRecognizer__optional(SimpleRecognizer__many):
    ___no_slots_ok___ = True
    def __init__(sf, rgnr, /):
        super().__init__(rgnr, 0, 1)
#end-class SimpleRecognizer__optional(ISimpleRecognizer):




class SimpleRecognizer__lookahead(ISimpleRecognizer):
    ___no_slots_ok___ = True
    def __init__(sf, rgnr, /):
        sf._rgnr = rgnr
    @override
    def _recognize_(sf, args4recur_call, /):
        'IArgs4recur_call -> GI(yield:gi/GI;return:(BoxedTailRecur{recur-GI}|BoxedFinalResult{rgnz_reply/ISimpleRecognizeReply})'
        #.(begin_idx, end_idx, ignore) = args4recur_call.mutable_args
        begin_idx = args4recur_call.begin_idx
        rgnr = sf._rgnr
        #rgnr5or_name_ = args4recur_call.common4recur_call.rgnr_name_server.rgnr5or_name_
        #rgnr = rgnr5or_name_(rgnr)
        rgnz_reply = yield rgnr._recognize_(args4recur_call)
        #restore:args4recur_call.begin_idx
        args4recur_call.begin_idx = begin_idx
        return BoxedFinalResult(rgnz_reply)

#end-class SimpleRecognizer__lookahead(ISimpleRecognizer):



class SimpleRecognizer__ref(ISimpleRecognizer):
    ___no_slots_ok___ = True
    def __init__(sf, nm4rgnr, /):
        sf._nm = nm4rgnr
    @override
    def _recognize_(sf, args4recur_call, /):
        'IArgs4recur_call -> GI(yield:gi/GI;return:(BoxedTailRecur{recur-GI}|BoxedFinalResult{rgnz_reply/ISimpleRecognizeReply})'
        nm4rgnr = sf._nm
        ignore = sf.ignore
        rgnr5name_ = args4recur_call.common4recur_call.rgnr_name_server.rgnr5name_
        rgnr = rgnr5name_(nm4rgnr)
        rgnz_reply = yield rgnr._recognize_(args4recur_call)
        m = None if ignore else args4recur_call.common4recur_call.may_ci_postprocess5name4ref_(nm4rgnr)
        if not m is None:
            ci_post = m
            (case, payload) = rgnz_cresult = rgnz_reply.rgnz_cresult
            _payload = ci_post(rgnz_cresult)
            if not _payload is payload:
                rgnz_cresult = (case, _payload)
                rgnz_reply = rgnz_reply.ireplace_(rgnz_cresult=rgnz_cresult)
        return BoxedFinalResult(rgnz_reply)

#end-class SimpleRecognizer__ref(ISimpleRecognizer):



class SimpleRecognizer__constant(ISimpleRecognizer):
    ___no_slots_ok___ = True
    def __init__(sf, rgnz_cresult, /):
        check_pair(rgnz_cresult)
        check_type_is(_C, rgnz_cresult[0])
        sf._cr = rgnz_cresult
    @override
    def _recognize_(sf, args4recur_call, /):
        'IArgs4recur_call -> GI(yield:gi/GI;return:(BoxedTailRecur{recur-GI}|BoxedFinalResult{rgnz_reply/ISimpleRecognizeReply})'
        rgnz_cresult = sf._cr
        end_idx4reply = args4recur_call.begin_idx
        rgnz_reply = args4recur_call.mk_rgnz_reply_(end_idx4reply, rgnz_cresult)
        return BoxedFinalResult(rgnz_reply)

#end-class SimpleRecognizer__constant(ISimpleRecognizer):

TODO:
    func_accessor
        cache
        nm4mdl+qnm4func
nongreedy_end_by0
sep_by1
dependent_pair#where?CONTINUE?BREAK?
    left_align,right_align
    ...为了避免麻烦考虑 begin_idx 不变 作为 CONTINUE 定义==>>Either/rgnz_eresult
ignore&end_idx$ctx controller/manager#restore
    serial --> chain强行解包合并Rope#指定保护区
        各单元 独立 使用: box,ignore 正交组合
    args4recur_call:++ctx
        many_chain:++empty_span4inf_many_ok
    ctx controller:
        ctx => open body close
        (rope8oresults0, ctx4close) := open{ctx}
        rope8oresults1 := body{ctx}
        ctx := ctx4close
            rope8oresults2 := close{ctx4close}
        finally:reset ctx
        rope8oresults = chain(rope8oresults0, rope8oresults1, rope8oresults2)
        return rope8oresults
not_follow_by
lift [case:=case][rgnz_oresult:=(common4recur_call, (begin_idx, end_idx, ignore), (end_idx4reply, rgnz_cresult))]
    -> xxx post6ok
    -> ci_post
tag
__repr__

__all__
from seed.recognize.rgnr.rgnrs.SimpleRecognizer import *
