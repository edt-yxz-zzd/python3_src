#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/rgnr/abc/ISimpleRecognizer.py
e ../../python3_src/seed/recognize/rgnr/abc/IRecognizer.py
view ../../python3_src/seed/func_tools/recur5yield__strict.py
view ../../python3_src/seed/recognize/rgnr/rgnrs/SimpleRecognizer.py
view ../../python3_src/seed/recognize/rgnr/utils/utils4ISimpleRecognizer.py

seed.recognize.rgnr.abc.ISimpleRecognizer
py -m nn_ns.app.debug_cmd   seed.recognize.rgnr.abc.ISimpleRecognizer -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.recognize.rgnr.abc.ISimpleRecognizer:__doc__ -ht # -ff -df

%s/rgnz_cresult/rgnz_cresult/g
[[
[seekable_input_stream:=input_seq_ex]
[pure_locator:=idx]


args4recur_call:
    ignore      #!!!mutable!!!
    begin_idx   #!!!mutable!!!
    end_idx     #!!!mutable!!!
    local_ctx   #!!!mutable!!!
    common4recur_call:  #immutable
        may_ci_postprocess5name4ref_()
        rgnr_name_server
        input_seq_ex/iseqx:
            seq_view
            seq_begin_idx
            seq_end_idx
rgnz_reply:  #immutable
    end_idx4reply
    rgnz_cresult
        | (RETURN/1, rgnz_oresult)
        | (CONTINUE/2, rgnz_errmsg)
        | (BREAK/3, rgnz_errmsg)

]]

py_adhoc_call   seed.recognize.rgnr.abc.ISimpleRecognizer   @f

]]]'''#'''
__all__ = r'''
ISimpleRecognizer
    basic_recognize_
    ISimpleRecognizeReply
        Case4ISimpleRecognizeReply
    IArgs4recur_call
        ICommon4recur_call
            ISimpleRecognizerNameServer
            IInputSeqEx

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from enum import Enum


#.from itertools import islice
#.from seed.tiny_.check import check_type_is, check_int_ge
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

#.class IQuasiSimpleRecognizer(ABC):
#.    '[quasi_rgnr==(rgnr|rgnr_mkr)] # cache@rgnr_name_server.static_globals4rgnr_group'
#.    __slots__ = ()
#.    @abstractmethod
#.    def iter_child_quasi_recognizers_(sf, rgnr_name_server, /):
#.        'rgnr_name_server -> Iter IQuasiSimpleRecognizer # [usually not includes self]'
#.    ######################
#.    #.view ../../python3_src/seed/recognize/rgnr/abc/utilities4ISimpleRecognizer.py
#.    #.@abstractmethod
#.    #.def iter_descendant_quasi_recognizers_(sf, rgnr_name_server, /):
#.    #.    'rgnr_name_server -> Iter IQuasiSimpleRecognizer # [usually not includes self]'
#.    ######################
#.
#.    #asif-@cache_property
#.    #.@abstractmethod
#.    #.def get_whether_rgnr_reply_immutable_(sf, rgnr_name_server, /):
#.    #.    '-> whether_rgnr_reply_immutable/bool'
#.    #.@abstractmethod
#.    #.def get_whether_context_free_(sf, rgnr_name_server, /):
#.    #.    '-> whether_context_free/bool  #[may_dynamic_params6ctx := None]'
#.    #.@abstractmethod
#.    #.def get_whether_proper_prefix_illegal_(sf, rgnr_name_server, /):
#.    #.    '-> whether_proper_prefix_illegal/bool  #auto_brake #e.g:no-tail-pattern:"a*"'
#.
#.class ISimpleRecognizer(IQuasiSimpleRecognizer):
#.    'rgnr # [GI==GeneratorIterator]'
#.    __slots__ = ()
#.    @abstractmethod
#.    def recognize_(sf, args4recur_call, may_dynamic_params6ctx, /):
#.        'IArgs4recur_call -> may dynamic_params6ctx -> GI(yield:gi/GI;return:rgnz_reply/ISimpleRecognizeReply)'
#.
#.    ######################
#.    ######################
#.    #only:rgnr_name_server
#.    @abstractmethod
#.    def setup_per_grammar__static_globals4rgnr_group_(sf, common4recur_call, /):
#.        '-> None # setup common4recur_call.static_globals4rgnr_group'
#.
#.    #both:rgnr_name_server,iseqx{seekable_input_stream:=input_seq_ex, pure_locator:=idx}
#.    @abstractmethod
#.    def setup_per_grammarXiseqx__static_global_environ_(sf, rgnr_name_server, input_seq_ex, static_global_environ, /):
#.        '-> None # setup static_global_environ@args4recur_call'
#.    @abstractmethod
#.    def main_setup_per_run__dynamic_global_context_(sf8main, args4recur_call, /):
#.        '-> None # setup args4recur_call.dynamic_global_context when [sf is the main_rgnr of current run]'
#.    @abstractmethod
#.    def setup_per_run__dynamic_global_context_(sf, args4recur_call, /):
#.        '-> None # setup args4recur_call.dynamic_global_context'
#.    @abstractmethod
#.    def main_teardown_per_run__dynamic_global_context_(sf8main, args4recur_call, /):
#.        '-> None # teardown args4recur_call.dynamic_global_context when [sf is the main_rgnr of current run]'
#.
#.class ISimpleRecognizeReply(ABC):
#.    'rgnz_reply'
#.    __slots__ = ()
#.    @abstractmethod
#.    def ireplace_(sf, /, **kwds):
#.        '-> ot/__class__'
#.    @property
#.    @abstractmethod
#.    def end_idx4reply(sf, /):
#.        '-> IPureLocator'
#.    #.@property
#.    #.@abstractmethod
#.    #.def end_idx4access(sf, /):
#.    #.    '-> IPureLocator # [farthest reached via (peek|read)]'
#.    @property
#.    @abstractmethod
#.    def rgnz_eresult(sf, /):
#.        '-> (Either rgnz_errmsg rgnz_oresult)'
#.        from seed.types.Either import Cased, Either, KindedName
#.        from seed.types.Either import mk_Left, mk_Right
#.class IArgs4recur_call(ABC):
#.    'args4recur_call'
#.    __slots__ = ()
#.    # .user_defined_extra_data
#.    @abstractmethod
#.    def ireplace_(sf, /, **kwds):
#.        '-> ot/__class__'
#.    @property
#.    @abstractmethod
#.    def common4recur_call(sf, /):
#.        '-> ICommon4recur_call'
#.    #.@property
#.    #.@abstractmethod
#.    #.def end_idx4look_ahead(sf, /):
#.    #.    '-> IPureLocator'
#.    #.@property
#.    #.@abstractmethod
#.    #.def end_idx4move_ahead(sf, /):
#.    #.    '-> IPureLocator'
#.    @property
#.    @abstractmethod
#.    def end_idx(sf, /):
#.        '-> IPureLocator'
#.    @property
#.    @abstractmethod
#.    def ignore(sf, /):
#.        '-> bool'
#.class ICommon4recur_call(ABC):
#.    'common4recur_call'
#.    __slots__ = ()
#.    @property
#.    @abstractmethod
#.    def rgnr_name_server(sf, /):
#.        '-> ISimpleRecognizerNameServer'
#.    @property
#.    @abstractmethod
#.    def input_seq_ex(sf, /):
#.        '-> iseqx/IInputSeqEx'
#.    @property
#.    @abstractmethod
#.    def static_global_environ(sf, /):
#.        '-> sgenv/IMapping # vars{iseqx} # cache{rgnz_oresult@[whether_proper_prefix_illegal&&whether_context_free&&whether_rgnr_reply_immutable]}'
#.    @property
#.    @abstractmethod
#.    def dynamic_global_context(sf, /):
#.        '-> dgctx/IMapping #curr_rgnz only # cache{rgnz_oresult@[whether_proper_prefix_illegal&&whether_context_free&&not whether_rgnr_reply_immutable]}'
#.
#.class ISimpleRecognizerNameServer(ABC):
#.    'rgnr_name_server#vivi:DNS'
#.    __slots__ = ()
#.    @property
#.    @abstractmethod
#.    def static_globals4rgnr_group(sf, /):
#.        '-> sggp/IMapping # configuration/settings and cache{descendant}'
#.    @abstractmethod
#.    def rgnr5name_(sf, name, /):
#.        'nm4rgnr -> ISimpleRecognizer|^LookupError'
#.    @abstractmethod
#.    def mk_rgnr_(sf, case, /, *args6case):
#.        'case -> (*args{case}) -> ISimpleRecognizer'
#.        #.mk_rgnr__constant_(rgnz_eresult)
#.        #.mk_rgnr__ref_(nm4rgnr)
#.        #.mk_rgnr__tuple_(rgnrs)
#.        #.mk_rgnr__array_(min_sz,may_max_sz,rgnr)
#.        #.mk_rgnr__parallel_(rgnrs)
#.        #.mk_rgnr__postprocess_(rgnr, f6ok_, f6err_)
#.        #.mk_rgnr__look_ahead_(rgnr)
#.        #.mk_rgnr__ignore_(rgnr)
#.        #.mk_rgnr__tuple__ignore_(ignore_rgnr_pairs)
#.        #.mk_rgnr__tuple__getitem_(idx_or_idc_or_slice, rgnrs)
#.        #... ...
#.
#.class IInputSeqEx(ABC):
#.    'iseqx/input_seq_ex'
#.    __slots__ = ()
#.    @property
#.    @abstractmethod
#.    def seq_view(sf, /):
#.        '-> [token] # readonly property && immutable seq{eg:py.str}'
#.    @property
#.    @abstractmethod
#.    def begin_idx(sf, /):
#.        '-> uint # mutable property'
#.
#.


def _mk4basic_recognize_():
    from seed.func_tools.recur5yield__strict import BoxedTailRecur, BoxedFinalResult
    from seed.func_tools.recur5yield__strict import Decorator4recur5yield
    from seed.func_tools.recur5yield__strict import Executor4recur5yield__dispatch_by_dict
    #def Executor4recur5yield__dispatch_by_dict.__init__(sf, may_emplace_stack_ops, using_tail_recur_gi_protocol, _allow__gi2gi_, may_type2attr_or_child_gi_protocol, /):
    @Decorator4recur5yield(Executor4recur5yield__dispatch_by_dict(None, True, True, None))
    def _basic_recognize_(rgnr, args4recur_call, /):
        r'''[[[
        before wrapped:'rgnr/ISimpleRecognizer -> args4recur_call/IArgs4recur_call -> (st, main_GI.return_value)'
        after wrapped:'rgnr/ISimpleRecognizer -> args4recur_call/IArgs4recur_call -> rgnz_reply/ISimpleRecognizeReply'
        #]]]'''#'''
        return (st:=None, BoxedTailRecur(rgnr._recognize_(args4recur_call)))
#_basic_recognize_ = _mk4basic_recognize_()
def _basic_recognize_(rgnr, args4recur_call, /):
    'rgnr/ISimpleRecognizer -> args4recur_call/IArgs4recur_call -> rgnz_reply/ISimpleRecognizeReply'
    global _basic_recognize_
    _basic_recognize_ = _mk4basic_recognize_()
    return _basic_recognize_(rgnr, args4recur_call)
def basic_recognize_(rgnr, args4recur_call, /):
    '(nm44gnr|rgnr/ISimpleRecognizer) -> args4recur_call/IArgs4recur_call -> rgnz_reply/ISimpleRecognizeReply'
    rgnr5or_name_ = args4recur_call.common4recur_call.rgnr_name_server.rgnr5or_name_
    rgnr = rgnr5or_name_(rgnr)
    return _basic_recognize_(rgnr, args4recur_call)


class ISimpleRecognizer(ABC):
    r'''[[[
    'rgnr # [GI==GeneratorIterator]'

    TODO:
        ++local_ctx
        case: 3/Case4ISimpleRecognizeReply-->2/bool
        rgnz_cresult-->rgnz_eresult/Either
    [args4recur_call.mutable_args == (begin_idx, end_idx, ignore, local_ctx)]
        [args4recur_call.end_idx&.ignore&.local_ctx SHOULD BE restored when return]
    *[rgnz_reply.case==True]:
        [args4recur_call.begin_idx SHOULD BE set correctly for succeeding serial recognizations]
        [MAYNOT:[rgnz_reply.end_idx4reply == args4recur_call.begin_idx]]
            eg:lookahead
    *[rgnz_reply.case==False]:
        [[failure is recoverable(parallel/switch will resume&try succeeding branches)] <-> [args4recur_call.begin_idx == original-begin_idx]]


    #obsolete:
    *[rgnz_reply.case==RETURN]:
        [MAYNOT:[rgnz_reply.end_idx4reply == args4recur_call.begin_idx]]
            eg:lookahead
        [args4recur_call.begin_idx SHOULD BE set correctly for succeeding serial recognizations]
        [args4recur_call.end_idx&.ignore SHOULD BE restored as input]
    *[rgnz_reply.case==CONTINUE]:
        [args4recur_call.begin_idx&.end_idx&.ignore SHOULD BE restored as input]
    *[rgnz_reply.case==BREAK]:
        [args4recur_call.begin_idx&.end_idx&.ignore SHOULD BE restored as input]

    [0 <= seq_begin_idx <= begin_idx <= end_idx4reply <= end_idx <= seq_end_idx <= len(seq_view)]
        args4recur_call.common4recur_call.input_seq_ex.{seq_view,seq_begin_idx,seq_end_idx}
        args4recur_call.{begin_idx,end_idx}
        rgnz_reply.{end_idx4reply}
    #]]]'''#'''
    __slots__ = ()
    @abstractmethod
    def _recognize_(sf, args4recur_call, /):
        'IArgs4recur_call -> GI(yield:gi/GI;return:(BoxedTailRecur{recur-GI}|BoxedFinalResult{rgnz_reply/ISimpleRecognizeReply})'
class Case4ISimpleRecognizeReply(Enum):
    RETURN = 1
        #success
    CONTINUE = 2
        #failure,try-succeeding-branches
    BREAK = 3
        #failure,skip-succeeding-branches
#break
#continue
#return

class ISimpleRecognizeReply(ABC):
    'rgnz_reply'
    __slots__ = ()
    @abstractmethod
    def ireplace_(sf, /, **kwds):
        '-> ot/__class__'
    @property
    @abstractmethod
    def end_idx4reply(sf, /):
        '-> uint'
    @property
    @abstractmethod
    def rgnz_cresult(sf, /):
        '-> (Case4ISimpleRecognizeReply, payload)/((RETURN/1, rgnz_oresult)|(CONTINUE/2, rgnz_errmsg)|(BREAK/3, rgnz_errmsg))'
class IArgs4recur_call(ABC):
    'args4recur_call'
    __slots__ = ()
    #.@property
    #.@abstractmethod
    #.def user_defined_extra_data(sf, /):
    #.    '-> ??? #immutable'
    @property
    @abstractmethod
    def common4recur_call(sf, /):
        '-> ICommon4recur_call #immutable'
    @property
    @abstractmethod
    def mutable_args(sf, /):
        '-> (begin_idx, end_idx, ignore) # mutable property'
    @property
    @abstractmethod
    def begin_idx(sf, /):
        '-> uint # mutable property'
    @property
    @abstractmethod
    def end_idx(sf, /):
        '-> uint # mutable property'
    @property
    @abstractmethod
    def ignore(sf, /):
        '-> bool'
    @abstractmethod
    def mk_rgnz_reply_(sf, end_idx4reply, rgnz_cresult, /):
        'end_idx4reply -> rgnz_cresult -> rgnz_reply/ISimpleRecognizeReply'
class ICommon4recur_call(ABC):
    'common4recur_call'
    __slots__ = ()
    @abstractmethod
    def may_ci_postprocess5name4ref_(sf, nm4rgnr6ref, /):
        'nm4rgnr6ref -> may (rgnz_cresult -> payload)'
    @property
    @abstractmethod
    def rgnr_name_server(sf, /):
        '-> ISimpleRecognizerNameServer'
    @property
    @abstractmethod
    def input_seq_ex(sf, /):
        '-> iseqx/IInputSeqEx'
    #.@property
    #.@abstractmethod
    #.def static_global_environ(sf, /):
    #.    '-> sgenv/IMapping # @{rgnr_name_server}'
    #.@property
    #.@abstractmethod
    #.def dynamic_global_context(sf, /):
    #.    '-> dgctx/IMapping # @{rgnr_name_server,input_seq_ex}'

class ISimpleRecognizerNameServer(ABC):
    'rgnr_name_server#vivi:DNS'
    __slots__ = ()
    @property
    @abstractmethod
    def static_globals4rgnr_group(sf, /):
        '-> sggp/IMapping # configuration/settings and cache{descendant}'
    @abstractmethod
    def rgnr5name_(sf, name, /):
        'nm4rgnr -> ISimpleRecognizer|^LookupError'
    @abstractmethod
    def rgnr5or_name_(sf, rgnr_or_name, /):
        '(ISimpleRecognizer|nm4rgnr) -> ISimpleRecognizer|^LookupError'
    @abstractmethod
    def mk_rgnr_(sf, case, /, *args6case):
        'case -> (*args{case}) -> ISimpleRecognizer'
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

class IInputSeqEx(ABC):
    'iseqx/input_seq_ex'
    __slots__ = ()
    @property
    @abstractmethod
    def seq_view(sf, /):
        '-> [token] # readonly property && immutable seq{eg:py.str}'
    @property
    @abstractmethod
    def seq_begin_idx(sf, /):
        '-> uint # immutable property'
    @property
    @abstractmethod
    def seq_end_idx(sf, /):
        '-> uint # immutable property'




__all__
from seed.recognize.rgnr.abc.ISimpleRecognizer import ISimpleRecognizer, Case4ISimpleRecognizeReply, ISimpleRecognizeReply, IArgs4recur_call, ICommon4recur_call, ISimpleRecognizerNameServer, IInputSeqEx
from seed.recognize.rgnr.abc.ISimpleRecognizer import basic_recognize_
from seed.recognize.rgnr.abc.ISimpleRecognizer import *
