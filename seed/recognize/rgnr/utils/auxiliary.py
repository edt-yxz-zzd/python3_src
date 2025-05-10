#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/rgnr/utils/auxiliary.py

seed.recognize.rgnr.utils.auxiliary
py -m nn_ns.app.debug_cmd   seed.recognize.rgnr.utils.auxiliary -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.recognize.rgnr.utils.auxiliary:__doc__ -ht # -ff -df

[[
]]

py_adhoc_call   seed.recognize.rgnr.utils.auxiliary   @f
from seed.recognize.rgnr.utils.auxiliary import *
]]]'''#'''
__all__ = r'''
    Helper4mk_rgnr_
    mk_args4recur_call_ex_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
######################mk_args4recur_call_ex_
from seed.func_tools.func_access import FuncAccess
    #for:ci_post(),fpost6ok()
    #see:SimpleRecognizer__ref
    #see:SimpleRecognizer__post6ok

from seed.recognize.rgnr.abc.ISimpleRecognizer import basic_recognize_
#.def basic_recognize_(nm_or_rgnr, args4recur_call, /):
#.    '(nm44gnr|rgnr/ISimpleRecognizer) -> args4recur_call/IArgs4recur_call -> rgnz_reply/ISimpleRecognizeReply'
#from seed.recognize.rgnr.utils.utils4ISimpleRecognizer import SimpleRecognizeReply, Args4recur_call, Common4recur_call, SimpleRecognizerNameServer, InputSeqEx
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


######################Helper4mk_rgnr_
from seed.recognize.rgnr.abc.ISimpleRecognizer import ISimpleRecognizer, ISimpleRecognizeReply, IArgs4recur_call, ICommon4recur_call, ISimpleRecognizerNameServer, IInputSeqEx

from seed.tiny_.check import check_type_le, check_type_is, check_int_ge

from functools import partial
#.from itertools import islice
#.
#.from seed.abc.abc__ver1 import abstractmethod, override, ABC
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

class Helper4mk_rgnr_(_Base4repr):
    def __init__(sf, rgnr_name_server, /):
        check_type_le(ISimpleRecognizerNameServer, rgnr_name_server)
        #assert callable(mk_rgnr6rgnr_name_server)
        #sf._mk = mk_rgnr6rgnr_name_server
        sf._mk =rgnr_name_server. mk_rgnr_
        sf._init4repr(rgnr_name_server)
    def __getattr__(sf, nm, /):
        if not nm.startswith('_'):
            return partial(sf._mk, nm)
        raise AttributeError(nm)



def _dict5may_dict_(may_dict, /):
    return {} if may_dict is None else may_dict
def mk_args4recur_call_ex_(seq_view, seq_begin_idx=None, seq_end_idx=None, name2rgnr=None, static_globals4rgnr_group=None, name2ref_rgnr=None, name2cipost=None, ignore=False, local_ctx=None):
    '-> (args4recur_call, name2rgnr, name2cipost, hmk, FuncAccess, basic_recognize_)'
    from seed.recognize.rgnr.utils.utils4ISimpleRecognizer import SimpleRecognizeReply, Args4recur_call, Common4recur_call, SimpleRecognizerNameServer, InputSeqEx
    input_seq_ex = InputSeqEx(seq_view, seq_begin_idx, seq_end_idx)
    name2rgnr = _dict5may_dict_(name2rgnr)
    #static_globals4rgnr_group = _dict5may_dict_(static_globals4rgnr_group)
    #name2ref_rgnr = _dict5may_dict_(name2ref_rgnr)
    rgnr_name_server = SimpleRecognizerNameServer(name2rgnr, static_globals4rgnr_group, name2ref_rgnr)
    hmk = Helper4mk_rgnr_(rgnr_name_server)
    name2cipost = _dict5may_dict_(name2cipost)
    common4recur_call = Common4recur_call(name2cipost, rgnr_name_server, input_seq_ex)
    args4recur_call = Args4recur_call(common4recur_call, begin_idx=input_seq_ex.seq_begin_idx, end_idx=input_seq_ex.seq_end_idx, ignore=ignore, local_ctx=local_ctx)
    #rgnz_reply = SimpleRecognizeReply(end_idx4reply, rgnz_eresult)
    #rgnz_reply = basic_recognize_('main', args4recur_call)
    #f = FuncAccess(__name__, 'f')
    FuncAccess
    basic_recognize_
    return (args4recur_call, name2rgnr, name2cipost, hmk, FuncAccess, basic_recognize_)



__all__
from seed.recognize.rgnr.utils.auxiliary import Helper4mk_rgnr_, mk_args4recur_call_ex_
    # hmk = Helper4mk_rgnr_(rgnr_name_server)
    # (args4recur_call, name2rgnr, name2cipost, hmk, FuncAccess, basic_recognize_) = mk_args4recur_call_ex_(seq_view, seq_begin_idx=None, seq_end_idx=None, name2rgnr=None, static_globals4rgnr_group=None, name2ref_rgnr=None, name2cipost=None, ignore=False, local_ctx=None)
from seed.recognize.rgnr.utils.auxiliary import *
