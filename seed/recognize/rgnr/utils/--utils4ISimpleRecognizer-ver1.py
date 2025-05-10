#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/rgnr/utils/utils4ISimpleRecognizer.py

seed.recognize.rgnr.utils.utils4ISimpleRecognizer
py -m nn_ns.app.debug_cmd   seed.recognize.rgnr.utils.utils4ISimpleRecognizer -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.recognize.rgnr.utils.utils4ISimpleRecognizer:__doc__ -ht # -ff -df

[[
]]

py_adhoc_call   seed.recognize.rgnr.utils.utils4ISimpleRecognizer   @f
]]]'''#'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.recognize.rgnr.abc.ISimpleRecognizer import ISimpleRecognizer, Case4ISimpleRecognizeReply, ISimpleRecognizeReply, IArgs4recur_call, ICommon4recur_call, ISimpleRecognizerNameServer, IInputSeqEx
import seed.recognize.rgnr.rgnrs.SimpleRecognizer as _S

#.from itertools import islice
from seed.tiny_.check import check_type_le, check_type_is, check_int_ge, check_pair
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
class SimpleRecognizeReply(ISimpleRecognizeReply):
    ___no_slots_ok___ = True
    def __init__(sf, /, end_idx4reply, rgnz_cresult):
        check_int_ge(0, end_idx4reply)
        check_pair(rgnz_cresult)
        check_type_is(_C, rgnz_cresult[0])
        sf._j = end_idx4reply
        sf._cr = rgnz_cresult
    def _as_kwds_(sf, /, **kwds):
        return dict(end_idx4reply=sf._j, rgnz_cresult=sf._cr)
    @override
    def ireplace_(sf, /, **kwds):
        '-> ot/__class__'
        d = sf._as_kwds_()
        d.update(kwds)
        return type(sf)(**d)
    @property
    @override
    def end_idx4reply(sf, /):
        '-> uint'
        return sf._j
    @property
    @override
    def rgnz_cresult(sf, /):
        '-> (Case4ISimpleRecognizeReply, payload)/((RETURN/1, rgnz_oresult)|(CONTINUE/2, rgnz_errmsg)|(BREAK/3, rgnz_errmsg))'
        return sf._cr

class Args4recur_call(IArgs4recur_call):
    ___no_slots_ok___ = True
    def __init__(sf, /, common4recur_call, begin_idx, end_idx, ignore):
        check_type_le(ICommon4recur_call, common4recur_call)
        sf._c = common4recur_call
        sf._reset_(begin_idx, end_idx, ignore)
    def _reset_(sf, /, begin_idx, end_idx, ignore):
        check_type_is(bool, ignore)
        check_int_ge(0, begin_idx)
        check_int_ge(begin_idx, end_idx)
        sf._i = begin_idx
        sf._j = end_idx
        sf._g = ignore
    @property
    @override
    def common4recur_call(sf, /):
        '-> ICommon4recur_call #immutable'
        return sf._c
    @property
    @override
    def mutable_args(sf, /):
        '-> (begin_idx, end_idx, ignore) # mutable property'
        return (sf._i, sf._j, sf._g)
    @mutable_args.setter
    def mutable_args(sf, args, /):
        '(begin_idx, end_idx, ignore) -> None # mutable property'
        i, j, g = args
        sf._reset(i, j, g)
    @property
    @override
    def begin_idx(sf, /):
        '-> uint # mutable property'
        return sf._i
    @mutable_args.setter
    def begin_idx(sf, begin_idx, /):
        'begin_idx -> None # mutable property'
        check_int_ge(0, begin_idx)
        if not (begin_idx <= sf.end_idx):raise ValueError
        sf._i = begin_idx
    @property
    @override
    def end_idx(sf, /):
        '-> uint # mutable property'
        return sf._j
    @mutable_args.setter
    def end_idx(sf, end_idx, /):
        'end_idx -> None # mutable property'
        check_int_ge(sf.begin_idx, end_idx)
        sf._j = end_idx
    @property
    @override
    def ignore(sf, /):
        '-> bool'
        return sf._g
    @mutable_args.setter
    def ignore(sf, ignore, /):
        'ignore -> None # mutable property'
        check_type_is(bool, ignore)
        sf._g = ignore
    @override
    def mk_rgnz_reply_(sf, end_idx4reply, rgnz_cresult, /):
        'end_idx4reply -> rgnz_cresult -> rgnz_reply/ISimpleRecognizeReply'
        return SimpleRecognizeReply(end_idx4reply, rgnz_cresult)

class Common4recur_call(ICommon4recur_call):
    ___no_slots_ok___ = True
    def __init__(sf, /, nm2cipost, rgnr_name_server, input_seq_ex):
        assert hasattr(nm2cipost, '__getitem__')
        check_type_le(ISimpleRecognizerNameServer, rgnr_name_server)
        check_type_le(IInputSeqEx, input_seq_ex)
        sf._nm2cipost = nm2cipost
        sf._svr = rgnr_name_server
        sf._seq = input_seq_ex
    @override
    def may_ci_postprocess5name4ref_(sf, nm4rgnr6ref, /):
        'nm4rgnr6ref -> may (rgnz_cresult -> payload)'
        return sf._nm2cipost.get(nm4rgnr6ref)
    @property
    @override
    def rgnr_name_server(sf, /):
        '-> ISimpleRecognizerNameServer'
        return sf._svr
    @property
    @override
    def input_seq_ex(sf, /):
        '-> iseqx/IInputSeqEx'
        return sf._seq

class SimpleRecognizerNameServer(ISimpleRecognizerNameServer):
    ___no_slots_ok___ = True
    def __init__(sf, /, name2rgnr, static_globals4rgnr_group=None):
        if static_globals4rgnr_group is None:
            static_globals4rgnr_group = {}
        assert hasattr(static_globals4rgnr_group, '__getitem__')
        assert hasattr(name2rgnr, '__getitem__')
        sf._gd = static_globals4rgnr_group
        sf._nm2r = name2rgnr
    @property
    @override
    def static_globals4rgnr_group(sf, /):
        '-> sggp/IMapping # configuration/settings and cache{descendant}'
        return sf._gd
    @override
    def rgnr5name_(sf, name, /):
        'nm4rgnr -> ISimpleRecognizer|^LookupError'
        return sf._nm2r
    @override
    def rgnr5or_name_(sf, rgnr_or_name, /):
        '(ISimpleRecognizer|nm4rgnr) -> ISimpleRecognizer|^LookupError'
        if hasattr(rgnr_or_name, 'recognize_'):
            rgnr = rgnr_or_name
        else:
            name = rgnr_or_name
            rgnr = sf._nm2r[name]
        return rgnr
    @override
    def mk_rgnr_(sf, case, /, *args6case):
        'case -> (*args{case}) -> ISimpleRecognizer'
        T = getattr(_S, f'SimpleRecognizer__{case}')
        rgnr = T(*args6case)
        return rgnr
        #.mk_rgnr__constant_(rgnz_eresult)
        #.mk_rgnr__ref_(nm4rgnr)
        #.mk_rgnr__tuple_(rgnrs)
        #.mk_rgnr__array_(min_sz,may_max_sz,rgnr)
        #.mk_rgnr__parallel_(rgnrs)
        #.mk_rgnr__postprocess_(rgnr, f6ok_, f6err_)
        #.mk_rgnr__look_ahead_(rgnr)
        #.mk_rgnr__ignore_(rgnr)
        #.mk_rgnr__tuple__ignore_(ignore_rgnr_pairs)
        #.mk_rgnr__tuple__getitem_(idx_or_idc_or_slice, rgnrs)
        #... ...


class InputSeqEx(IInputSeqEx):
    ___no_slots_ok___ = True
    def __init__(sf, /, seq_view, seq_begin_idx=None, seq_end_idx=None):
        assert hasattr(seq_view, '__getitem__')
        assert not hasattr(seq_view, '__setitem__')
        (start, stop, stride) = slice(seq_begin_idx, seq_end_idx).indices(len(seq_view))
        sf._s = seq_view
        sf._si = seq_begin_idx = start
        sf._sj = seq_end_idx = stop
    @property
    @override
    def seq_view(sf, /):
        '-> [token] # readonly property && immutable seq{eg:py.str}'
        return sf._s
    @property
    @override
    def seq_begin_idx(sf, /):
        '-> uint # immutable property'
        return sf._si
    @property
    @override
    def seq_end_idx(sf, /):
        '-> uint # immutable property'
        return sf._sj


__all__
from seed.recognize.rgnr.utils.utils4ISimpleRecognizer import SimpleRecognizeReply, Args4recur_call, Common4recur_call, SimpleRecognizerNameServer, InputSeqEx
from seed.recognize.rgnr.utils.utils4ISimpleRecognizer import *
