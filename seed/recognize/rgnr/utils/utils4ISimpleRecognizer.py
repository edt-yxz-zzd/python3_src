#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/rgnr/utils/utils4ISimpleRecognizer.py
view ../../python3_src/seed/recognize/rgnr/utils/auxiliary.py

seed.recognize.rgnr.utils.utils4ISimpleRecognizer
py -m nn_ns.app.debug_cmd   seed.recognize.rgnr.utils.utils4ISimpleRecognizer -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.recognize.rgnr.utils.utils4ISimpleRecognizer:__doc__ -ht # -ff -df

[[
]]

py_adhoc_call   seed.recognize.rgnr.utils.utils4ISimpleRecognizer   @f
]]]'''#'''
__all__ = r'''
SimpleRecognizeReply
Args4recur_call
Common4recur_call
SimpleRecognizerNameServer
InputSeqEx
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.recognize.rgnr.abc.ISimpleRecognizer import ISimpleRecognizer, ISimpleRecognizeReply, IArgs4recur_call, ICommon4recur_call, ISimpleRecognizerNameServer, IInputSeqEx
import seed.recognize.rgnr.rgnrs.SimpleRecognizer as _S
from seed.recognize.rgnr.rgnrs.SimpleRecognizer import AllSimpleRecognizers as _A

from seed.types.Either import Cased, Either# KindedName
from seed.types.Either import mk_Left, mk_Right

#.from itertools import islice
from seed.tiny_.check import check_type_le, check_type_is, check_int_ge# check_pair
#.
from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.from seed.helper.repr_input import repr_helper
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

#_C = Case4ISimpleRecognizeReply
class SimpleRecognizeReply(ISimpleRecognizeReply, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, /, end_idx4reply, rgnz_eresult):
        check_int_ge(0, end_idx4reply)
        check_type_is(Either, rgnz_eresult)
        sf._j = end_idx4reply
        sf._er = rgnz_eresult
        sf._init4repr(end_idx4reply, rgnz_eresult)
    def _as_kwds_(sf, /, **kwds):
        return dict(end_idx4reply=sf._j, rgnz_eresult=sf._er)
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
    def rgnz_eresult(sf, /):
        '-> (Either rgnz_errmsg rgnz_oresult)'
        return sf._er

class Args4recur_call(IArgs4recur_call, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, /, common4recur_call, begin_idx, end_idx, ignore, local_ctx):
        check_type_le(ICommon4recur_call, common4recur_call)
        sf._c = common4recur_call
        sf._reset_(begin_idx, end_idx, ignore, local_ctx)
        sf._init4repr(common4recur_call, begin_idx, end_idx, ignore, local_ctx)
    def _reset_(sf, /, begin_idx, end_idx, ignore, local_ctx):
        check_type_is(bool, ignore)
        check_int_ge(0, begin_idx)
        check_int_ge(begin_idx, end_idx)
        sf._i = begin_idx
        sf._j = end_idx
        sf._g = ignore
        sf._x = local_ctx
    @property
    @override
    def common4recur_call(sf, /):
        '-> ICommon4recur_call #immutable'
        return sf._c
    @property
    @override
    def mutable_args(sf, /):
        '-> (begin_idx, end_idx, ignore, local_ctx) # mutable property'
        return (sf._i, sf._j, sf._g, sf._x)
    @mutable_args.setter
    def mutable_args(sf, args, /):
        '(begin_idx, end_idx, ignore, local_ctx) -> None # mutable property'
        i, j, g, x = args
        sf._reset(i, j, g, x)
    @property
    @override
    def restored_mutable_args(sf, /):
        '-> (end_idx, ignore, local_ctx) # mutable property'
        return (sf._j, sf._g, sf._x)
    @restored_mutable_args.setter
    def restored_mutable_args(sf, args, /):
        '(end_idx, ignore, local_ctx) -> None # mutable property'
        j, g, x = args
        sf._reset(sf._i, j, g, x)
    @property
    @override
    def begin_idx(sf, /):
        '-> uint # mutable property'
        return sf._i
    @begin_idx.setter
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
    @end_idx.setter
    def end_idx(sf, end_idx, /):
        'end_idx -> None # mutable property'
        check_int_ge(sf.begin_idx, end_idx)
        sf._j = end_idx
    @property
    @override
    def ignore(sf, /):
        '-> bool # mutable property'
        return sf._g
    @ignore.setter
    def ignore(sf, ignore, /):
        'ignore -> None # mutable property'
        check_type_is(bool, ignore)
        sf._g = ignore
    @property
    @override
    def local_ctx(sf, /):
        '-> object # mutable property'
        return sf._x
    @local_ctx.setter
    def local_ctx(sf, local_ctx, /):
        'local_ctx -> None # mutable property'
        sf._x = local_ctx
    @override
    def mk_rgnz_reply_(sf, end_idx4reply, rgnz_eresult, /):
        'end_idx4reply -> rgnz_eresult -> rgnz_reply/ISimpleRecognizeReply'
        return SimpleRecognizeReply(end_idx4reply, rgnz_eresult)

class Common4recur_call(ICommon4recur_call, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, /, name2cipost, rgnr_name_server, input_seq_ex):
        assert hasattr(name2cipost, '__getitem__')
        check_type_le(ISimpleRecognizerNameServer, rgnr_name_server)
        check_type_le(IInputSeqEx, input_seq_ex)
        sf._nm2cipost = name2cipost
        sf._svr = rgnr_name_server
        sf._seq = input_seq_ex
        sf._init4repr(name2cipost, rgnr_name_server, input_seq_ex)
    @override
    def may_ci_postprocess5name4ref_(sf, nm4rgnr6ref, /):
        'nm4rgnr6ref -> may (rgnz_eresult -> payload)'
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

class SimpleRecognizerNameServer(ISimpleRecognizerNameServer, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, /, name2rgnr, static_globals4rgnr_group=None, name2ref_rgnr=None):
        if name2ref_rgnr is None:
            name2ref_rgnr = {}
        assert hasattr(name2ref_rgnr, '__getitem__')
        if static_globals4rgnr_group is None:
            static_globals4rgnr_group = {}
        assert hasattr(static_globals4rgnr_group, '__getitem__')
        assert hasattr(name2rgnr, '__getitem__')
        sf._nm2ref = name2ref_rgnr
        sf._gd = static_globals4rgnr_group
        sf._nm2r = name2rgnr
        sf._init4repr(name2rgnr, static_globals4rgnr_group)
    @property
    @override
    def static_globals4rgnr_group(sf, /):
        '-> sggp/IMapping # configuration/settings and cache{descendant}'
        return sf._gd
    @override
    def rgnr5name_(sf, name, /):
        'nm4rgnr -> ISimpleRecognizer|^LookupError'
        return sf._nm2r[name]
    #.@override
    #.def rgnr5or_name_(sf, rgnr_or_name, /):
    #.    '(ISimpleRecognizer|nm4rgnr) -> ISimpleRecognizer|^LookupError'
    #.    if hasattr(rgnr_or_name, 'recognize_'):
    #.        rgnr = rgnr_or_name
    #.    else:
    #.        name = rgnr_or_name
    #.        rgnr = sf._nm2r[name]
    #.    return rgnr
    @override
    def mk_rgnr_(sf, case, /, *args6case):
        'case -> (*args{case}) -> ISimpleRecognizer'
        T = getattr(_S, f'SimpleRecognizer__{case}')
        #T = getattr(_A, f'{case}')
        rgnr = T(*args6case)
        return rgnr
    @override
    def get_or_mk_ref_rgnr_(sf, nm4rgnr6ref, /):
        #required by basic_recognize_()._rgnr5or_name_()
        'nm4rgnr6ref -> ISimpleRecognizer # maybe cache and unify ref_rgnr{nm4rgnr6ref}'
        d = sf._nm2ref
        m = d.get(nm4rgnr6ref)
        if m is None:
            rgnr = sf.mk_rgnr_('ref', nm4rgnr6ref)
            d[nm4rgnr6ref] = rgnr
            rgnr = sf.get_or_mk_ref_rgnr_(nm4rgnr6ref)
        else:
            rgnr = m
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

class InputSeqEx(IInputSeqEx, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, /, seq_view, seq_begin_idx=None, seq_end_idx=None):
        assert hasattr(seq_view, '__getitem__')
        assert not hasattr(seq_view, '__setitem__')
        (start, stop, stride) = slice(seq_begin_idx, seq_end_idx).indices(len(seq_view))
        sf._s = seq_view
        sf._si = seq_begin_idx = start
        sf._sj = seq_end_idx = stop
        sf._init4repr(seq_view, seq_begin_idx, seq_end_idx)
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




def __():
    return [nm for nm, cls in sorted(globals().items()) if isinstance(cls, type) and cls.__module__ == __name__ and not issubclass(cls, _Base4repr)]
assert not (__:=__()), __



__all__
from seed.recognize.rgnr.utils.utils4ISimpleRecognizer import SimpleRecognizeReply, Args4recur_call, Common4recur_call, SimpleRecognizerNameServer, InputSeqEx
    ######################
    #SimpleRecognizeReply(end_idx4reply, rgnz_eresult)
    #Args4recur_call(common4recur_call, begin_idx, end_idx, ignore, local_ctx)
    #Common4recur_call(name2cipost, rgnr_name_server, input_seq_ex)
    #SimpleRecognizerNameServer(name2rgnr, static_globals4rgnr_group=None)
    #InputSeqEx(seq_view, seq_begin_idx=None, seq_end_idx=None)
    ######################
    #input_seq_ex = InputSeqEx(seq_view, seq_begin_idx=None, seq_end_idx=None)
    #rgnr_name_server = SimpleRecognizerNameServer(name2rgnr, static_globals4rgnr_group=None, name2ref_rgnr=None)
    #common4recur_call = Common4recur_call(name2cipost, rgnr_name_server, input_seq_ex)
    #args4recur_call = Args4recur_call(common4recur_call, begin_idx, end_idx, ignore, local_ctx)
    #rgnz_reply = SimpleRecognizeReply(end_idx4reply, rgnz_eresult)
    ######################

from seed.recognize.rgnr.utils.utils4ISimpleRecognizer import *
