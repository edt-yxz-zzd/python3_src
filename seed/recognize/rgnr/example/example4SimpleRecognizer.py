#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/rgnr/example/example4SimpleRecognizer.py

seed.recognize.rgnr.example.example4SimpleRecognizer
py -m nn_ns.app.debug_cmd   seed.recognize.rgnr.example.example4SimpleRecognizer -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.recognize.rgnr.example.example4SimpleRecognizer:__doc__ -ht # -ff -df

[[
]]


>>> run_example1_()
InputSeqEx('000, 111, (222, (333, [444]), 555), 666, 777', 4, 39)
SimpleRecognizeReply(39, Either(True, Rope((111,), Rope(((222, (333, [444]), 555),), (666,)))))
SimpleRecognizeReply(39, Either(True, (111, (222, (333, [444]), 555), 666)))

>>> run_example1_2_()
InputSeqEx('000, 111, (222, (333, [444]), 555), 666, 777', 4, 39)
SimpleRecognizeReply(39, Either(True, Rope((111,), Rope(((222, (333, [444]), 555),), (666,)))))
SimpleRecognizeReply(39, Either(True, (111, (222, (333, [444]), 555), 666)))

py_adhoc_call   seed.recognize.rgnr.example.example4SimpleRecognizer   @f
from seed.recognize.rgnr.example.example4SimpleRecognizer import *
]]]'''#'''
__all__ = r'''
run_example1_



mk_rgnr__ignore_with_constant_
mk_rgnr__ignore_with_constant__null_rope_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...

from seed.recognize.rgnr.utils.auxiliary import Helper4mk_rgnr_, mk_args4recur_call_ex_
    # hmk = Helper4mk_rgnr_(rgnr_name_server)
    # (args4recur_call, name2rgnr, name2cipost, hmk, FuncAccess, basic_recognize_) = mk_args4recur_call_ex_(seq_view, seq_begin_idx=None, seq_end_idx=None, name2rgnr=None, static_globals4rgnr_group=None, name2ref_rgnr=None, name2cipost=None, ignore=False, local_ctx=None)

from seed.func_tools.func_access import FuncAccess
    #for:ci_post(),fpost6ok()
    #see:SimpleRecognizer__ref
    #see:SimpleRecognizer__post6ok

from seed.recognize.rgnr.abc.ISimpleRecognizer import basic_recognize_
#.def basic_recognize_(nm_or_rgnr, args4recur_call, /):
#.    '(nm44gnr|rgnr/ISimpleRecognizer) -> args4recur_call/IArgs4recur_call -> rgnz_reply/ISimpleRecognizeReply'
#from seed.recognize.rgnr.utils.utils4ISimpleRecognizer import Helper4mk_rgnr_
from seed.recognize.rgnr.utils.auxiliary import Helper4mk_rgnr_
from seed.recognize.rgnr.utils.utils4ISimpleRecognizer import SimpleRecognizeReply, Args4recur_call, Common4recur_call, SimpleRecognizerNameServer, InputSeqEx
    #SimpleRecognizeReply(end_idx4reply, rgnz_eresult):
    #Args4recur_call(common4recur_call, begin_idx, end_idx, ignore, local_ctx)
    #Common4recur_call(name2cipost, rgnr_name_server, input_seq_ex)
    #SimpleRecognizerNameServer(name2rgnr, static_globals4rgnr_group=None, name2ref_rgnr=None)
    #InputSeqEx(seq_view, seq_begin_idx=None, seq_end_idx=None):
if 0:
    #class SimpleRecognizerNameServer: def mk_rgnr_(sf, case, /, *args6case):
    #from seed.recognize.rgnr.rgnrs.SimpleRecognizer import AllSimpleRecognizers #_nms4neat__str:goto
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

from seed.types.Rope import Rope, null_rope
from seed.tiny_.funcs import const
from seed.tiny_.check import check_type_is, check_int_ge

#.from itertools import islice
#.
#.from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.from seed.helper.repr_input import repr_helper
#.from seed.tiny_._Base4repr import _Base4repr
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
def _constant__null_rope(_, /):
    return null_rope
_constant__null_rope = const(null_rope)
def _rope2apply_tail_call(rope, /):
    check_type_is(Rope, rope)
    ls = list(rope)
    f = ls.pop()
    return f(ls)
def _uint5matchobj(m, /):
    return int(m.group(0))

def mk_rgnr__ignore_with_constant_(hmk_or_rgnr_name_server, rgnr, rgnz_oresult, /):
    if type(hmk_or_rgnr_name_server) is Helper4mk_rgnr_:
        hmk = hmk_or_rgnr_name_server
        return hmk.post6ok__overwrite_oresult_by_constant(hmk.ignore_manager__always_ignore(rgnr), rgnz_oresult, True)
    rgnr_name_server = hmk_or_rgnr_name_server
    return rgnr_name_server.mk_rgnr_('post6ok__overwrite_oresult_by_constant'
            , rgnr_name_server.mk_rgnr_('ignore_manager__always_ignore', rgnr)
            , rgnz_oresult
            , True
            )
def mk_rgnr__ignore_with_constant__null_rope_(hmk_or_rgnr_name_server, rgnr, /):
    return mk_rgnr__ignore_with_constant_(hmk_or_rgnr_name_server, rgnr, null_rope)
    rgnr_name_server = hmk_or_rgnr_name_server
    return rgnr_name_server.mk_rgnr_('post6ok'
            , rgnr_name_server.mk_rgnr_('ignore_manager__always_ignore', rgnr)
            , FuncAccess(__name__, '_constant__null_rope')
            , True
            )
def run_example1_():
    def box(rgnr, /):
        return rgnr_name_server.mk_rgnr_('box4Rope', rgnr)
    def unbox(rgnr, /):
        return rgnr_name_server.mk_rgnr_('unbox', rgnr)
    seq_view = '000, 111, (222, (333, [444]), 555), 666, 777'
    input_seq_ex = InputSeqEx(seq_view, seq_begin_idx=4, seq_end_idx=-5)
    name2rgnr = {}
    rgnr_name_server = SimpleRecognizerNameServer(name2rgnr, static_globals4rgnr_group=None, name2ref_rgnr=None)
    ######################
    rgnr3data = rgnr_name_server.mk_rgnr_('ref', 'data')
    rgnr3atom = rgnr_name_server.mk_rgnr_('ref', 'atom')
    rgnr3uint = rgnr_name_server.mk_rgnr_('ref', 'uint')
    rgnr3seq = rgnr_name_server.mk_rgnr_('ref', 'seq')
    ######################

    rgnr3spaces = mk_rgnr__ignore_with_constant__null_rope_(rgnr_name_server, rgnr_name_server.mk_rgnr_('py_regex', r'\s*', False))
    rgnr3comma = mk_rgnr__ignore_with_constant__null_rope_(rgnr_name_server, rgnr_name_server.mk_rgnr_('py_regex', r',\s*', False))
    rgnr3open = rgnr_name_server.mk_rgnr_('local_ctx_manager__oresult_as_local_ctx4sibling', rgnr_name_server.mk_rgnr_('py_regex', r'[\[\(]', True)) # '\)\]'
        # without: \s*
    rgnr3close = rgnr_name_server.mk_rgnr_('local_ctx_as_dispatch_key', {
        # '\(\['
        '(':mk_rgnr__ignore_with_constant_(rgnr_name_server, rgnr_name_server.mk_rgnr_('py_regex', r'\s*\)', False), Rope((tuple,)))
        ,'[':mk_rgnr__ignore_with_constant_(rgnr_name_server, rgnr_name_server.mk_rgnr_('py_regex', r'\s*\]', False), Rope((list,)))
        # '])'
    })
    rgnr3rope8data = rgnr_name_server.mk_rgnr_('chain'
            , [rgnr3spaces]
            , [rgnr_name_server.mk_rgnr_('sep_by1', rgnr3comma, box(rgnr3atom), 1, None, True)]
            , True)
    rgnr3tuple8data = rgnr_name_server.mk_rgnr_('flatten4Rope', rgnr3data, True)
    ######################
    name2rgnr['seq'] = rgnr_name_server.mk_rgnr_('post6ok'
        , rgnr_name_server.mk_rgnr_('local_ctx_manager__long_distance_local_ctx_controller'
            , rgnr3open
            , rgnr_name_server.mk_rgnr_('switch', [(rgnr3data), (rgnr3spaces)])
            , rgnr3close
            , True
            )
        , FuncAccess(__name__, '_rope2apply_tail_call')
        , True
        )


    name2rgnr['data'] = rgnr3rope8data
    name2rgnr['main4data'] = rgnr3tuple8data
    name2rgnr['atom'] = rgnr_name_server.mk_rgnr_('switch', [rgnr3uint, rgnr3seq])
    name2rgnr['uint'] = rgnr_name_server.mk_rgnr_('post6ok'
        , rgnr_name_server.mk_rgnr_('py_regex', r'\d+', True)
        , int
        , False
        )
    ######################
    name2cipost = {}
    common4recur_call = Common4recur_call(name2cipost, rgnr_name_server, input_seq_ex)
    args4recur_call = Args4recur_call(common4recur_call, begin_idx=input_seq_ex.seq_begin_idx, end_idx=input_seq_ex.seq_end_idx, ignore=False, local_ctx=None)
    #rgnz_reply = SimpleRecognizeReply(end_idx4reply, rgnz_eresult)
    ######################
    begin_idx = args4recur_call.begin_idx
    #rgnz_reply = basic_recognize_(rgnr3data, args4recur_call)
    rgnz_reply__Rope = basic_recognize_('data', args4recur_call)
    args4recur_call.begin_idx = begin_idx
    rgnz_reply__tuple = basic_recognize_('main4data', args4recur_call)
    ######################
    #return (rgnz_reply__Rope, rgnz_reply__tuple)
    print(input_seq_ex)
    print(rgnz_reply__Rope)
    print(rgnz_reply__tuple)
#end-def run_example1_():

def run_example1_2_():
    r'''[[[
    'using:Helper4mk_rgnr_()'

.+1,$s/rgnr_name_server.mk_rgnr_('\(\w\+\)', /hmk.\1(/g
.+1,$s/rgnr_name_server.mk_rgnr_('\(\w\+\)'$/hmk.\1(*[]/g
    #]]]'''#'''
    def box(rgnr, /):
        return hmk.box4Rope(rgnr)
    def unbox(rgnr, /):
        return hmk.unbox(rgnr)
    seq_view = '000, 111, (222, (333, [444]), 555), 666, 777'
    (args4recur_call, name2rgnr, name2cipost, hmk, FuncAccess, basic_recognize_) = mk_args4recur_call_ex_(seq_view, seq_begin_idx=4, seq_end_idx=-5, name2rgnr=None, static_globals4rgnr_group=None, name2ref_rgnr=None, name2cipost=None, ignore=False, local_ctx=None)

    ######################
    rgnr3data = hmk.ref('data')
    rgnr3atom = hmk.ref('atom')
    rgnr3uint = hmk.ref('uint')
    rgnr3seq = hmk.ref('seq')
    ######################

    rgnr3spaces = mk_rgnr__ignore_with_constant__null_rope_(hmk, hmk.py_regex(r'\s*', False))
    rgnr3comma = mk_rgnr__ignore_with_constant__null_rope_(hmk, hmk.py_regex(r',\s*', False))
    rgnr3open = hmk.local_ctx_manager__oresult_as_local_ctx4sibling(hmk.py_regex(r'[\[\(]', True)) # '\)\]'
        # without: \s*
    rgnr3close = hmk.local_ctx_as_dispatch_key({
        # '\(\['
        '(':mk_rgnr__ignore_with_constant_(hmk, hmk.py_regex(r'\s*\)', False), Rope((tuple,)))
        ,'[':mk_rgnr__ignore_with_constant_(hmk, hmk.py_regex(r'\s*\]', False), Rope((list,)))
        # '])'
    })
    rgnr3rope8data = hmk.chain(*[]
            , [rgnr3spaces]
            , [hmk.sep_by1(rgnr3comma, box(rgnr3atom), 1, None, True)]
            , True)
    rgnr3tuple8data = hmk.flatten4Rope(rgnr3data, True)
    ######################
    name2rgnr['seq'] = hmk.post6ok(*[]
        , hmk.local_ctx_manager__long_distance_local_ctx_controller(*[]
            , rgnr3open
            , hmk.switch([(rgnr3data), (rgnr3spaces)])
            , rgnr3close
            , True
            )
        , FuncAccess(__name__, '_rope2apply_tail_call')
        , True
        )


    name2rgnr['data'] = rgnr3rope8data
    name2rgnr['main4data'] = rgnr3tuple8data
    name2rgnr['atom'] = hmk.switch([rgnr3uint, rgnr3seq])
    name2rgnr['uint'] = hmk.post6ok(*[]
        , hmk.py_regex(r'\d+', True)
        , int
        , False
        )
    ######################
    begin_idx = args4recur_call.begin_idx
    #rgnz_reply = basic_recognize_(rgnr3data, args4recur_call)
    rgnz_reply__Rope = basic_recognize_('data', args4recur_call)
    args4recur_call.begin_idx = begin_idx
    rgnz_reply__tuple = basic_recognize_('main4data', args4recur_call)
    ######################
    #return (rgnz_reply__Rope, rgnz_reply__tuple)
    print(args4recur_call.common4recur_call.input_seq_ex)
    print(rgnz_reply__Rope)
    print(rgnz_reply__tuple)
#end-def run_example1_2_():

__all__
from seed.recognize.rgnr.example.example4SimpleRecognizer import *
