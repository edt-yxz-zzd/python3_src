#__all__:goto
#TODO:消除new_hmi；整个识别过程hmi唯一；局部窜改hmi.ctx4inherit 使用with；recur5yield__strict 使用gi.throw() 传递异常；serial_rgnr 窜改+向后传递+返回 ctx4sibling；使用flow框架 唯一 处理 ctx4sibling的窜改；flow框架 使用wrapper框架；wrapper_rgnr.__init__(repr_/(rgnr4repr, args4repr), rgnr4impl/rgnr_expr)
    #view others/数学/编程/设计/通用树状数据-语境纟遍历.txt
r'''[[[
e ../../python3_src/seed/recognize/rgnr/abc/IRecognizer.py
    view ../../python3_src/seed/recognize/rgnr/abc/IRecognizer-ver1.py
e ../../python3_src/seed/recognize/rgnr/abc/utilities4IRecognizer.py
e ../../python3_src/seed/recognize/rgnr/abc/ISimpleRecognizer.py

seed.recognize.rgnr.abc.IRecognizer
py -m nn_ns.app.debug_cmd   seed.recognize.rgnr.abc.IRecognizer -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.recognize.rgnr.abc.IRecognizer:__doc__ -ht # -ff -df

[[
TODO:
@20250430
只定义最小接口
    只保留基本框架使用到的接口
    每一个具象类纟识别器 自定义 抽象基类纟入参(只含使用到的接口)
    基本框架:串联(无保护:不考虑重置:相当于默认长子解锁)，并联(分支失败后需要判定是否已移位)，前瞻，保护性串联(失败重置:相当于末子解锁)，语境关联性串联
参数隐式同一递归传递
    含许多处理函数
...无显式:unlocker:允许识别结束时不解锁，更加正交化的设计方案
串联:自身输出Rope，要求子部件输出Rope
基本框架不包含基础识别器，所以不需要输入文件的相关接口...

...
basic_serial
basic_parallel
null_chain_rgnr
no_branch_rgnr

TODO:
token_rgnr
match_tokens_rgnr
unlock_last_rgnr
trial_rgnr
box_rgnr#box8chain_
lift_rgnr#reply-->oresult
ignore_rgnr


...
reply case:
    * succ/ok
    * fail:
        * fatal_error
        * retriable_fail
            hmi.at_locator_(begin_locator)
]]



py_adhoc_call   seed.recognize.rgnr.abc.IRecognizer   @f
from seed.recognize.rgnr.abc.IRecognizer import *
]]]'''#'''
__all__ = r'''
Case4tkn
IHdlMutInput
    IHdlMutInput__4chain
    IHdlMutInput__4ignore
    IHdlMutInput__4unlocker
    IHdlMutInput__4snapshot4istream
    IHdlMutInput__4istream
    IHdlMutInput__4token
    IHdlMutInput__4cased
IRecognizer
    Recognizer__basic_serial
        null_chain_rgnr
    Recognizer__basic_parallel
        no_branch_rgnr
    Recognizer__token
    Recognizer__match_tokens
    Recognizer__unlock_last
    Recognizer__trial
    Recognizer__box
    Recognizer__lift
    Recognizer__ignore
    Recognizer__never_ignore
    Recognizer__tag
    Recognizer__look_ahead
    Recognizer__not_followed_by
    Recognizer__optional
    Recognizer__many_box
    Recognizer__basic_many
    Recognizer__basic_nongreedy_end_by
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from enum import Enum, auto
#.from itertools import islice
from seed.tiny_.check import check_type_is, check_int_ge
from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_
lazy_import4funcs_('seed.tiny_.containers', 'mk_tuple,null_tuple', __name__)
if 0:from seed.tiny_.containers import null_tuple, mk_tuple
lazy_import4funcs_('seed.tiny_.count_', 'count_', __name__)
if 0:from seed.tiny_.count_ import count_
#.
from seed.abc.abc__ver1 import abstractmethod, override, ABC
lazy_import4funcs_('seed.helper.repr_input', 'repr_helper', __name__)
if 0:from seed.helper.repr_input import repr_helper
#from seed.types.Rope import Rope, null_rope
#from seed.func_tools.recur5yield__strict import BoxedTailRecur, BoxedFinalResult
#from seed.types.Either import Cased, Either, KindedName
#from seed.types.Either import mk_Left, mk_Right
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError


class IHdlMutInput(ABC):
    #basic_hmi
    '[hmi==(handler/(ops,setting), mutable/(cache,variables,end_locator), input_stream/(data,begin_locator))]'
    __slots__ = ()
    #grep 'hmi\.\w\+' ../../python3_src/seed/recognize/rgnr/abc/IRecognizer.py -o | sort -u
    ######################
    ####### common #######
    ######################
    @abstractmethod
    def semi_apply_rgnr_(sf, rgnr, /):
        '#mk obj to be yield@IRecognizer._recognize_() #check rgnr._recognize_() return GI'
        #serial&parallel
    @abstractmethod
    def box4return5reply_(sf, reply, /):
        '#mk obj to be return@IRecognizer._recognize_() #BoxedFinalResult'
        #serial&parallel
    @abstractmethod
    def is_ok5reply_(sf, reply, /):
        'reply -> ok/bool'
        #serial&parallel
    ######################
    ####### serial #######
    ######################
    @abstractmethod
    def get_oresult5reply_(sf, reply, /):
        'reply -> oresult #[reply:.ok]'
        #serial
    @abstractmethod
    def mk_reply5oresult_(sf, oresult, /):
        'oresult -> reply{.end_locator==hmi:.end_locator}'
        #serial
    @abstractmethod
    def is_chain_(sf, oresult, /):
        'oresult -> bool #eg:[type(oresult) is Rope]'
        #serial&many
        #return type(oresult) is Rope
    @abstractmethod
    def mk_chain5chains_(sf, chains, /):
        'chains -> chain'
        #serial&unlock_last&many
    ######################
    ###### parallel ######
    ######################
    @abstractmethod
    def at_locator_(sf, locator, /):
        'locator -> bool{==(sf.tell_locator_() == locator)}'
        #parallel&many
        return sf.tell_locator_() == locator
    @abstractmethod
    def get_end_locator5reply_(sf, reply, /):
        'reply -> end_locator/locator'
        #parallel
    @abstractmethod
    def mk_reply5errmsg_(sf, errmsg, /):
        'errmsg -> reply{.end_locator==hmi:.end_locator}'
        #parallel
    @abstractmethod
    def tell_locator_(sf, /):
        '-> begin_locator/locator'
        #parallel
    ######################
    ####### extend #######
    ######################
    #.box4return5gi_
    #.box8chain_
    #.null_chain
    #.ireplace_oresult6reply_
    @abstractmethod
    def box4return5gi_(sf, reply, /):
        '#mk obj to be return@IRecognizer._recognize_() #BoxedTailRecur'
        #vs:box4return5reply_
        #Recognizer__never_ignore
    @abstractmethod
    def box8chain_(sf, x, /):
        'x -> chain{[.len==1]} #[==sf.mk_chain5leaves_([x])]'
        #vs:mk_chain5chains_
        #Recognizer__box
    @property
    @abstractmethod
    def null_chain(sf, /):
        '-> chain{[.len==0]}{==sf.mk_chain5chains_([])}{==sf.mk_chain5leaves_([])}'
        #vs:mk_chain5chains_
        #Recognizer__ignore
        return sf.mk_chain5chains_([])
        #return null_rope
    @abstractmethod
    def ireplace_oresult6reply_(sf, reply, oresult, /):
        'old_reply -> oresult -> new_reply{.end_locator==old_reply:.end_locator}'
        #vs:mk_reply5oresult_
        #Recognizer__ignore&Recognizer__box&Recognizer__lift
    @abstractmethod
    def iflip_ok6reply_(sf, reply, /):
        'old_reply -> new_reply{.end_locator==old_reply:.end_locator}{.ok==not old_reply:.ok}'
        #vs:ireplace_oresult6reply_
        #Recognizer__not_followed_by
#end-class IHdlMutInput(ABC):


class IHdlMutInput__4cased(IHdlMutInput):
    __slots__ = ()
    @abstractmethod
    def mk_cased_(sf, case, payload, /):
        'case -> payload -> pair{case, payload} #like:Cased(case, payload)'
        #Recognizer__tag
        #return Cased(case, payload)
        #return (case, payload)

class IHdlMutInput__4chain(IHdlMutInput):
    __slots__ = ()
    ##inherit:
    ###.is_chain_
    ###.mk_chain5chains_
    ###.box8chain_
    ###.null_chain
    #
    #.mk_chain5leaves_
    #.get_num_leaves5chain_
    #.iter_leaves5chain_
    #
    @abstractmethod
    def mk_chain5leaves_(sf, xs, /):
        'xs -> chain{[.len==len(xs)]}'
        #vs:mk_chain5chains_
        #return Rope(mk_tuple(xs))
    @abstractmethod
    def get_num_leaves5chain_(sf, chain, /):
        'chain -> uint'
        #vs:mk_chain5leaves_
        return len(chain)
    @abstractmethod
    def iter_leaves5chain_(sf, chain, /):
        'chain -> Iter x'
        #vs:mk_chain5leaves_
        return iter(chain)

class IHdlMutInput__4ignore(IHdlMutInput):
    #.iset_ignore6hmi_
    #
    __slots__ = ()
    @abstractmethod
    def iset_ignore6hmi_(sf, ignore, /):
        'bool -> ot/__class__ #[[ignore==sf:.ignore] -> [ot is sf]]'
        #Recognizer__ignore
class IHdlMutInput__4unlocker(IHdlMutInput):
    #.iattach_unlocker6hmi_
    #.ipop_unlocker6hmi_
    #.is_released5unlocker_
    #.release_unlocker6hmi_
    #
    __slots__ = ()
    @abstractmethod
    def iattach_unlocker6hmi_(sf, unlocker, /):
        'unlocker -> ot/__class__ #[[unlocker:.released] -> [ot is sf]] #[ot:=sf:.ireplace_(unlocker=sf:.unlocker<<unlocker)]'
        #Recognizer__trial
    @abstractmethod
    def ipop_unlocker6hmi_(sf, /):
        '-> ot/__class__ #[[sf:.unlocker:.released] -> [ot is sf]] #[ot:=sf:.ireplace_(unlocker=null_unlocker)]'
        #Recognizer__unlock_last
    @abstractmethod
    def is_released5unlocker_(sf, unlocker, /):
        'unlocker -> bool'
        #Recognizer__trial
    @abstractmethod
    def release_unlocker6hmi_(sf, /):
        '-> None #[sf:.unlocker:.release()]'
        #Recognizer__unlock_last&Recognizer__token&Recognizer__match_tokens
    @abstractmethod
    def release_unlocker_(sf, unlocker, /):
        'unlocker -> None #[unlocker:.release()]'
        #Recognizer__trial&Recognizer__look_ahead
class IHdlMutInput__4snapshot4istream(IHdlMutInput):
    '# [snapshot :: mutable/releaseable-unlocker]'
    #.restore_snapshot4istream_
    #.tell_snapshot4istream_
    #
    __slots__ = ()
    @abstractmethod
    def restore_snapshot4istream_(sf, snapshot, /):
        'snapshot -> None|^Exception{if snapshot:.released}  #[sf:.istream:.restore_(snapshot)]'
        #Recognizer__trial&Recognizer__look_ahead
    @abstractmethod
    def tell_snapshot4istream_(sf, snapshot, /):
        '-> snapshot #[==sf:.istream:.mk_snapshot_()]'
        #Recognizer__trial&Recognizer__look_ahead

class IHdlMutInput__4token(IHdlMutInput):
    '#[[tkn,tkd,tkey,tdat::Immutable][tkn==(begin_locator,tkd,end_locator)][tkd==(tkey,tdat)][tkey::Eq&&Hashable]]'
    #.extract5tokens_
    #
    #.get_compactor4tokens_
    #.get_extractor4token_
    #
    __slots__ = ()
    @abstractmethod
    def extract5tokens_(sf, xs, icase4tkn, ocase4tkn, /):
        '[tkn_of{icase4tkn}] -> icase4tkn/case4tkn -> ocase4tkn/case4tkn -> [tkn_of{ocase4tkn}] #[icase4tkn ~>=~ ocase4tkn]'
        #Recognizer__match_tokens
        if icase4tkn == ocase4tkn:
            return xs
        compactor = sf.get_compactor4tokens_(ocase4tkn)
        extractor = sf.get_extractor4token_(icase4tkn, ocase4tkn)
        ys = map(extractor, xs)
        ys = compactor(ys)
        return ys
    ######################
    ####### extend #######
    ######################
    @abstractmethod
    def get_compactor4tokens_(sf, case4tkn, /):
        'case4tkn/case4tkn -> compactor/([tkn_of{case4tkn}] -> compact[tkn_of{case4tkn}])'
        return mk_tuple
    @abstractmethod
    def get_extractor4token_(sf, icase4tkn, ocase4tkn, /):
        'icase4tkn/case4tkn -> ocase4tkn/case4tkn -> extractor/([tkn_of{icase4tkn}] -> [tkn_of{ocase4tkn}]) #[icase4tkn ~>=~ ocase4tkn]'
class IHdlMutInput__4istream(IHdlMutInput):
    '# [case4tkn == ("tkn"|"tkd"|"tkey"|"tdat")]'
    #.seek_advance_
    #.peek_le_
    #.read_le_
    #
    __slots__ = ()
    @abstractmethod
    def seek_advance_(sf, max_sz, /):
        'max_sz/uint -> None #[sf:.istream:.seek(max_sz+sf:.istream:.tell())]'
        #Recognizer__match_tokens
    @abstractmethod
    def peek_tmay__eq_(sf, sz, case4tkn, /):
        'sz/uint -> case4tkn -> [tkn_of{case4tkn}]{len==sz} #[sf:.istream:.peek_tmay__eq_(sz, case4tkn)] #[sf:.begin_locator unchanged]'
        #Recognizer__match_tokens
        xs = sf.peek_le_(sz, case4tkn)
            # :: [(tkn|tkd|tkey|tdat)]
        tm = (xs,) if len(xs) == sz else null_tuple
        return tm
    @abstractmethod
    def peek_le_(sf, max_sz, case4tkn, /):
        'max_sz/uint -> case4tkn -> [tkn_of{case4tkn}]{len<=max_sz} #[sf:.istream:.peek_le_(max_sz, case4tkn)] #[sf:.begin_locator unchanged]'
        #Recognizer__match_tokens
    @abstractmethod
    def read_le_(sf, max_sz, case4tkn, /):
        'max_sz/uint -> case4tkn -> [tkn_of{case4tkn}]{len<=max_sz} #[sf:.istream:.peek_le_(max_sz, case4tkn)] #[sf:.begin_locator changed if not eof]'
        #Recognizer__token
        xs = sf.peek_le_(max_sz, case4tkn)
        sf.seek_advance_(max_sz)
        return xs


class IRecognizer(ABC):
    '[hmi::IHdlMutInput][GI==generator_iterator#see:seed.func_tools.recur5yield__strict]' \
    '[hmi==(handler/(ops,setting), mutable/(cache,variables,end_locator), input_stream/(data,begin_locator))]'
    __slots__ = ()
    @abstractmethod
    def _recognize_(sf, hmi, /):
        '-> GI # [precondition:begin_locator<=end_locator]'


class Recognizer__basic_serial(IRecognizer):
    #basic_serial
    '#[unlocker:asif forwarding into first child rgnr#indeed forwarding into each child rgnr, since neednot unlock before reply] #[see:unlock_last_rgnr(unlock_snd_rgnr)&?null_chain_rgnr?(basic_serial([]))] #[using box_rgnr&lift_rgnr to get replys instead of oresults] #[rename:Rope-->chain]'
    ___no_slots_ok___ = True
    def __init__(sf, rgnrs, /):
        sf._rs = mk_tuple(rgnrs)
    def __repr__(sf, /):
        rgnrs = sf._rs
        return repr_helper(sf, rgnrs)

    @override
    def _recognize_(sf, hmi, /):
        '-> GI # [precondition:begin_locator<=end_locator]'
        ls = [] # :: [oresult/chain]
        rgnrs = sf._rs
        for rgnr in rgnrs:
            reply = yield hmi.semi_apply_rgnr_(rgnr)
            if hmi.is_ok5reply_(reply):
                oresult = hmi.get_oresult5reply_(reply)
                assert hmi.is_chain_(oresult)
                #check_type_is(Rope, oresult)
                ls.append(oresult)
            else:
                return hmi.box4return5reply_(reply)
        else:
            oresult = hmi.mk_chain5chains_(ls)
            #oresult = Rope(*ls)
            reply = hmi.mk_reply5oresult_(oresult)
            return hmi.box4return5reply_(reply)
#class Recognizer__basic_serial(IRecognizer):
null_chain_rgnr = Recognizer__basic_serial([])
    #null_rgnr
class Recognizer__basic_parallel(IRecognizer):
    #basic_parallel
    '#[unlocker:need to wrap all child rgnrs by trial_rgnr[seekback_if_fail]]'
    ___no_slots_ok___ = True
    def __init__(sf, rgnrs, /):
        sf._rs = mk_tuple(rgnrs)
    def __repr__(sf, /):
        rgnrs = sf._rs
        return repr_helper(sf, rgnrs)

    @override
    def _recognize_(sf, hmi, /):
        '-> GI # [precondition:begin_locator<=end_locator]'
        begin_locator = hmi.tell_locator_()
        ls = [] # :: [reply]
        rgnrs = sf._rs
        for rgnr in rgnrs:
            reply = yield hmi.semi_apply_rgnr_(rgnr)
            if hmi.is_ok5reply_(reply) or not hmi.at_locator_(begin_locator):
                # succ or fatal_error
                return hmi.box4return5reply_(reply)
            else:
                # retriable_fail
                ls.append(reply)
        else:
            if not ls:
                reply = hmi.mk_reply5errmsg_(errmsg:='no_branch')
            else:
                reply = max(ls, key=hmi.get_end_locator5reply_)
            reply
            return hmi.box4return5reply_(reply)
#class Recognizer__basic_parallel(IRecognizer):
no_branch_rgnr = Recognizer__basic_parallel([])
    #dead_rgnr


null_chain_rgnr
no_branch_rgnr

#DONE:
#token_rgnr
#match_tokens_rgnr
#unlock_last_rgnr
#trial_rgnr
#box_rgnr#box8chain_
#lift_rgnr#reply-->oresult#ireplace_oresult6reply_
#ignore_rgnr



class Recognizer__token(IRecognizer):
    #token_rgnr
    '[hmi::IHdlMutInput__4istream&&IHdlMutInput__4unlocker]'
    '# [case4tkn == ("tkn"|"tkd"|"tkey"|"tdat")] #[tkn,tkd,tkey,tdat::Immutable][tkn==(begin_locator,tkd,end_locator)][tkd==(tkey,tdat)][tkey::Eq&&Hashable]'
    ___no_slots_ok___ = True
    #.def __init__(sf, max_sz, case4tkn, /):
    #.    sf._n = max_sz
    #.    sf._c = case4tkn
    def __init__(sf, case4tkn, /):
        sf._c = case4tkn
    def __repr__(sf, /):
        case4tkn = sf._c
        return repr_helper(sf, case4tkn)
        #.max_sz = sf._n
        #.return repr_helper(sf, max_sz, case4tkn)

    @override
    def _recognize_(sf, hmi, /):
        '-> GI # [precondition:begin_locator<=end_locator]'
        #.ls = hmi.read_le_(max_sz, case4tkn)
        #.    # :: [(tkn|tkd|tkey|tdat)]
        #.ls = mk_tuple(ls)
        #.oresult = hmi.box8chain_(ls)
        case4tkn = sf._c
        tmay_oresult = hmi.read_le_(1, case4tkn)
            # :: tmay (tkn|tkd|tkey|tdat)
        if not tmay_oresult:
            reply = hmi.mk_reply5errmsg_('eof')
        else:
            [oresult] = tmay_oresult
            hmi.release_unlocker6hmi_()
            reply = hmi.mk_reply5oresult_(oresult)
        reply
        return hmi.box4return5reply_(reply)
        777; yield

#class Recognizer__token(IRecognizer):


class Recognizer__match_tokens(IRecognizer):
    #match_tokens_rgnr
    '[hmi::IHdlMutInput__4token&&IHdlMutInput__4istream&&IHdlMutInput__4unlocker]'
    '# [case4tkn:see:Recognizer__token]'
    ___no_slots_ok___ = True
    def __init__(sf, xs, icase4tkn, ocase4tkn, acase4tkn, /):
        '[xs::[tkn_of{icase4tkn}]][icase4tkn,ocase4tkn,acase4tkn::case4tkn][acase4tkn ~>=~ icase4tkn][acase4tkn ~>=~ ocase4tkn] #eg:Recognizer__match_tokens(["NUMBER", "+"], "tkey", "tdat", "tkd")'
        sf._ts = xs
        sf._ic = icase4tkn
        sf._oc = ocase4tkn
        sf._ac = acase4tkn
    def __repr__(sf, /):
        xs = sf._ts
        icase4tkn = sf._ic
        ocase4tkn = sf._oc
        acase4tkn = sf._ac
        return repr_helper(sf, xs, icase4tkn, ocase4tkn, acase4tkn)

    @override
    def _recognize_(sf, hmi, /):
        '-> GI # [precondition:begin_locator<=end_locator]'
        xs = sf._ts
        icase4tkn = sf._ic
        ocase4tkn = sf._oc
        acase4tkn = sf._ac

        sz = len(xs)
        #.ys = hmi.peek_le_(sz, acase4tkn)
        #.    # :: [(tkn|tkd|tkey|tdat)]
        tm_ts = hmi.peek_tmay__eq_(sz, acase4tkn)
        eof = not tm_ts
        if not eof:
            [ts] = tm_ts
            ys = hmi.extract5tokens_(ts, acase4tkn, icase4tkn)

        if eof:
            reply = hmi.mk_reply5errmsg_('eof')
        elif not ys == xs:
            #elif not ys == xs:
            reply = hmi.mk_reply5errmsg_('not_matched')
        else:
            zs = ys if icase4tkn == ocase4tkn else hmi.extract5tokens_(ts, acase4tkn, ocase4tkn)
            oresult = zs
            hmi.seek_advance_(sz)
            hmi.release_unlocker6hmi_()
            reply = hmi.mk_reply5oresult_(oresult)
        reply
        return hmi.box4return5reply_(reply)
        777; yield

#class Recognizer__match_tokens(IRecognizer):






class Recognizer__unlock_last(IRecognizer):
    #unlock_last_rgnr
    #unlock_snd_rgnr
    '[hmi::IHdlMutInput__4unlocker]'
    '#[input_stream::unique-mutable-stream][hmi::tmp-struct]'
    ___no_slots_ok___ = True
    def __init__(sf, fst_rgnr, snd_rgnr, /):
        sf._rs = (fst_rgnr, snd_rgnr)
    def __repr__(sf, /):
        (fst_rgnr, snd_rgnr) = sf._rs
        return repr_helper(sf, fst_rgnr, snd_rgnr)

    @override
    def _recognize_(sf, hmi, /):
        '-> GI # [precondition:begin_locator<=end_locator]'
        (fst_rgnr, snd_rgnr) = sf._rs

        old_hmi = hmi
        #(new_hmi, old_unlocker) = old_hmi:.ipop_unlocker6hmi_()
        new_hmi = old_hmi.ipop_unlocker6hmi_()
        # [new_hmi:.unlocker is null_unlocker]

        ######################
        fst_reply = yield new_hmi.semi_apply_rgnr_(fst_rgnr)
        if not new_hmi.is_ok5reply_(fst_reply):
            return new_hmi.box4return5reply_(fst_reply)
        fst_oresult = new_hmi.get_oresult5reply_(fst_reply)
        assert new_hmi.is_chain_(fst_oresult)

        ######################
        snd_reply = yield old_hmi.semi_apply_rgnr_(snd_rgnr)
            # !! [input_stream::unique-mutable-stream][hmi::tmp-struct]
            # => [ok to reuse old_hmi]
        if not old_hmi.is_ok5reply_(snd_reply):
            return old_hmi.box4return5reply_(snd_reply)
        snd_oresult = old_hmi.get_oresult5reply_(snd_reply)
        assert old_hmi.is_chain_(snd_oresult)

        ######################
        #ok:
        #old_hmi:.release5unlocker_(old_unlocker)
        old_hmi.release_unlocker6hmi_()
            # !! maybe not released@snd_rgnr
        ######################
        oresult = hmi.mk_chain5chains_([fst_oresult, snd_oresult])
        reply = hmi.mk_reply5oresult_(oresult)
        return hmi.box4return5reply_(reply)
#class Recognizer__unlock_last(IRecognizer):



class Recognizer__trial(IRecognizer):
    #trial_rgnr
    '[hmi::IHdlMutInput__4unlocker&&IHdlMutInput__4snapshot4istream]'
    '# [snapshot :: mutable/releaseable-unlocker]'
    ___no_slots_ok___ = True
    def __init__(sf, rgnr, /):
        sf._r = rgnr
    def __repr__(sf, /):
        rgnr = sf._r
        return repr_helper(sf, rgnr)

    @override
    def _recognize_(sf, hmi, /):
        '-> GI # [precondition:begin_locator<=end_locator]'
        rgnr = sf._r
        old_hmi = hmi
        snapshot = old_hmi.tell_snapshot4istream_()
            # [snapshot :: mutable/releaseable-unlocker]
        new_hmi = old_hmi.iattach_unlocker6hmi_(snapshot)
        reply = yield new_hmi.semi_apply_rgnr_(rgnr)
        if not new_hmi.is_released5unlocker_(snapshot):
            #if not snapshot.released:
            #seekback_if_fail
            if not new_hmi.is_ok5reply_(reply):
                #fail
                old_hmi.restore_snapshot4istream_(snapshot)
                #-->retriable_fail
            hmi.release_unlocker_(snapshot)
        return hmi.box4return5reply_(reply)
#class Recognizer__trial(IRecognizer):



class Recognizer__box(IRecognizer):
    #box_rgnr
    ___no_slots_ok___ = True
    def __init__(sf, rgnr, /):
        sf._r = rgnr
    def __repr__(sf, /):
        rgnr = sf._r
        return repr_helper(sf, rgnr)

    @override
    def _recognize_(sf, hmi, /):
        '-> GI # [precondition:begin_locator<=end_locator]'
        rgnr = sf._r
        reply = yield hmi.semi_apply_rgnr_(rgnr)
        if hmi.is_ok5reply_(reply):
            oresult = hmi.get_oresult5reply_(reply)
            _oresult = hmi.box8chain_(oresult)
            assert hmi.is_chain_(_oresult)
            reply = hmi.ireplace_oresult6reply_(reply, _oresult)
        reply
        return hmi.box4return5reply_(reply)
#class Recognizer__box(IRecognizer):


class Recognizer__lift(IRecognizer):
    #lift_rgnr
    ___no_slots_ok___ = True
    def __init__(sf, rgnr, /):
        sf._r = rgnr
    def __repr__(sf, /):
        rgnr = sf._r
        return repr_helper(sf, rgnr)

    @override
    def _recognize_(sf, hmi, /):
        '-> GI # [precondition:begin_locator<=end_locator]'
        rgnr = sf._r
        reply = yield hmi.semi_apply_rgnr_(rgnr)
        if hmi.is_ok5reply_(reply):
            _oresult = reply
            reply = hmi.ireplace_oresult6reply_(reply, _oresult)
        reply
        return hmi.box4return5reply_(reply)
#class Recognizer__lift(IRecognizer):



class _IRecognizer__xxx_ignore(IRecognizer):
    '[hmi::IHdlMutInput__4ignore]'
    __slots__ = ()
    @property
    @abstractmethod
    def ignore(sf, /):
        '-> bool'
    def __init__(sf, rgnr, /):
        #def __init__(sf, rgnr, ignore=True, /):
        #check_type_is(bool, ignore)
        sf._r = rgnr
        #sf._b = ignore
    def __repr__(sf, /):
        rgnr = sf._r
        #.ignore = sf._b
        #.if not ignore:
        #.    return repr_helper(sf, rgnr, ignore)
        return repr_helper(sf, rgnr)

    @override
    def _recognize_(sf, hmi, /):
        '-> GI # [precondition:begin_locator<=end_locator]'
        rgnr = sf._r
        #.ignore = sf._b
        ignore = sf.ignore

        #.if not ignore is hmi:.get_ignore6hmi_():
        #.    new_hmi = hmi.iset_ignore6hmi_(ignore)
        #.    777; old_hmi = hmi
        #.    # [new_hmi:.ignore is ignore]
        #.    hmi = new_hmi
        hmi = hmi.iset_ignore6hmi_(ignore)

        if not ignore:
            #Recognizer__never_ignore
            gi = hmi.semi_apply_rgnr_(rgnr)
            return hmi.box4return5gi_(gi)
            777; yield
        #Recognizer__ignore
        #overwrite oresult by null_chain
        reply = yield hmi.semi_apply_rgnr_(rgnr)
        if hmi.is_ok5reply_(reply):
            _oresult = hmi.null_chain
            reply = hmi.ireplace_oresult6reply_(reply, _oresult)
        reply
        return hmi.box4return5reply_(reply)
#end-class _IRecognizer__xxx_ignore(IRecognizer):
class Recognizer__never_ignore(_IRecognizer__xxx_ignore):
    #never_ignore_rgnr
    '[hmi::IHdlMutInput__4ignore]'
    ___no_slots_ok___ = True
    #@override
    ignore = False
class Recognizer__ignore(_IRecognizer__xxx_ignore):
    #ignore_rgnr
    '[hmi::IHdlMutInput__4ignore]' \
    '#[used with Recognizer__basic_serial]'
    ___no_slots_ok___ = True
    #@override
    ignore = True
#class Recognizer__ignore(IRecognizer):




#tag_rgnr
#look_ahead,not_followed_by
#many,optional,nongreedy_end_by
#ref,named/wrapper-->post6ok
#ctx_serial...#inherit ctx,ignore from parent&sibling
#   switch_rgnr/dependent_pair...
#



class Recognizer__tag(IRecognizer):
    #tag_rgnr
    '[hmi::IHdlMutInput__4cased]' \
    '#[used with Recognizer__basic_parallel]'
    ___no_slots_ok___ = True
    def __init__(sf, rgnr, tag, /):
        sf._r = rgnr
        sf._t = tag
    def __repr__(sf, /):
        rgnr = sf._r
        tag = sf._t
        return repr_helper(sf, rgnr, tag)

    @override
    def _recognize_(sf, hmi, /):
        '-> GI # [precondition:begin_locator<=end_locator]'
        rgnr = sf._r
        tag = sf._t
        reply = yield hmi.semi_apply_rgnr_(rgnr)
        if hmi.is_ok5reply_(reply):
            oresult = hmi.get_oresult5reply_(reply)
            _oresult = hmi.mk_cased_(tag, oresult)
            reply = hmi.ireplace_oresult6reply_(reply, _oresult)
        reply
        return hmi.box4return5reply_(reply)
#class Recognizer__tag(IRecognizer):




class Recognizer__look_ahead(IRecognizer):
    #look_ahead_rgnr
    '[hmi::IHdlMutInput__4unlocker&&IHdlMutInput__4snapshot4istream]' \
    '#[used with Recognizer__basic_serial]'
    ___no_slots_ok___ = True
    def __init__(sf, rgnr, /):
        sf._r = rgnr
    def __repr__(sf, /):
        rgnr = sf._r
        return repr_helper(sf, rgnr)

    @override
    def _recognize_(sf, hmi, /):
        '-> GI # [precondition:begin_locator<=end_locator]'
        #see:Recognizer__trial
        rgnr = sf._r
        snapshot = hmi.tell_snapshot4istream_()
            # [snapshot :: mutable/releaseable-unlocker]
        reply = yield hmi.semi_apply_rgnr_(rgnr)
        #seekback_always
        hmi.restore_snapshot4istream_(snapshot)
        hmi.release_unlocker_(snapshot)
        return hmi.box4return5reply_(reply)
#class Recognizer__look_ahead(IRecognizer):



class Recognizer__not_followed_by(IRecognizer):
    #not_followed_by_rgnr
    '[hmi::IHdlMutInput__4unlocker&&IHdlMutInput__4snapshot4istream&&IHdlMutInput__4ignore]' \
    '#[used with Recognizer__basic_serial]'
    ___no_slots_ok___ = True
    def __init__(sf, rgnr, /):
        sf._r = rgnr
        sf._r2 = Recognizer__ignore(Recognizer__look_ahead(rgnr))
    def __repr__(sf, /):
        rgnr = sf._r
        return repr_helper(sf, rgnr)

    @override
    def _recognize_(sf, hmi, /):
        '-> GI # [precondition:begin_locator<=end_locator]'
        #see:Recognizer__look_ahead
        rgnr2 = sf._r2
        snapshot = hmi.tell_snapshot4istream_()
        reply = yield hmi.semi_apply_rgnr_(rgnr2)
        #seekback_always
        hmi.restore_snapshot4istream_(snapshot)
        hmi.release_unlocker_(snapshot)
        #.if hmi.is_ok5reply_(reply):
        #.    reply = hmi.mk_reply5errmsg_(errmsg:='followed_by')
        #.else:
        #.    #not_followed_by
        #.    reply = hmi.mk_reply5oresult_(oresult:=hmi.null_chain)

        if hmi.is_ok5reply_(reply):
            errmsg = 'followed_by'
            reply = hmi.ireplace_oresult6reply_(reply, oresult:=errmsg)

        reply = hmi.iflip_ok6reply_(reply)
        if hmi.is_ok5reply_(reply):
            #not_followed_by
            reply = hmi.ireplace_oresult6reply_(reply, oresult:=hmi.null_chain)
        reply
        return hmi.box4return5reply_(reply)
#class Recognizer__not_followed_by(IRecognizer):



class Recognizer__optional(IRecognizer):
    #optional_rgnr
    #vs:many_box_rgnr
    #vs:basic_many_rgnr
    '[hmi::IHdlMutInput__4unlocker&&IHdlMutInput__4snapshot4istream]' \
    '#[used with Recognizer__basic_serial]' \
    '#NOTE:[optional_rgnr(rgnr)===many_box_rgnr(rgnr,0,1)=!=basic_many_rgnr(rgnr,0,1)]'
    ___no_slots_ok___ = True
    def __init__(sf, rgnr, /):
        sf._r = rgnr
        #xxx:sf._r2 = Recognizer__basic_many(rgnr, 0, 1)
        sf._r2 = Recognizer__box(Recognizer__trial(rgnr))
    def __repr__(sf, /):
        rgnr = sf._r
        return repr_helper(sf, rgnr)

    @override
    def _recognize_(sf, hmi, /):
        '-> GI # [precondition:begin_locator<=end_locator]'
        #see:Recognizer__basic_serial
        #see:Recognizer__trial
        rgnr2 = sf._r2

        begin_locator = hmi.tell_locator_()
        reply = yield hmi.semi_apply_rgnr_(rgnr2)
        if not hmi.is_ok5reply_(reply) and hmi.at_locator_(begin_locator):
            #retriable_fail
            reply = hmi.mk_reply5oresult_(hmi.null_chain)
            #-->ok

        if hmi.is_ok5reply_(reply):
            oresult = hmi.get_oresult5reply_(reply)
            assert hmi.is_chain_(oresult)
                # !! box_rgnr@ok
                # !! null_chain@retriable_fail->ok
        else:
            #fatal_error
            pass
        return hmi.box4return5reply_(reply)
#class Recognizer__optional(IRecognizer):




class Recognizer__many_box(IRecognizer):
    #many_box_rgnr
    #vs:basic_many_rgnr
    '[hmi::IHdlMutInput__4unlocker&&IHdlMutInput__4snapshot4istream]'
    ___no_slots_ok___ = True
    def __init__(sf, rgnr, min_sz, may_max_sz, /):
        sf._r = rgnr
        sf._r2 = Recognizer__basic_many(Recognizer__box(rgnr), min_sz, may_max_sz)
    def __repr__(sf, /):
        rgnr = sf._r
        min_sz = sf._m
        may_max_sz = sf._M
        return repr_helper(sf, rgnr, min_sz, may_max_sz)

    @override
    def _recognize_(sf, hmi, /):
        '-> GI # [precondition:begin_locator<=end_locator]'
        rgnr2 = sf._r2
            #Recognizer__basic_many <<< Recognizer__box
        gi = hmi.semi_apply_rgnr_(rgnr2)
        return hmi.box4return5gi_(gi)
        777; yield


class Recognizer__basic_many(IRecognizer):
    #basic_many_rgnr
    '[hmi::IHdlMutInput__4unlocker&&IHdlMutInput__4snapshot4istream]' \
    '#[used with Recognizer__basic_serial]'
    ___no_slots_ok___ = True
    def __init__(sf, rgnr, min_sz, may_max_sz, /):
        check_int_ge(0, min_sz)
        if not may_max_sz is None:
            max_sz = may_max_sz
            check_int_ge(min_sz, max_sz)
        sf._r = rgnr
        #sf._r2 = Recognizer__trial(rgnr)
        sf._r3 = Recognizer__basic_nongreedy_end_by(None, rgnr, min_sz, may_max_sz)
        sf._m = min_sz
        sf._M = may_max_sz
    def __repr__(sf, /):
        rgnr = sf._r
        min_sz = sf._m
        may_max_sz = sf._M
        return repr_helper(sf, rgnr, min_sz, may_max_sz)

    @override
    def _recognize_(sf, hmi, /):
        '-> GI # [precondition:begin_locator<=end_locator]'
        #see:Recognizer__basic_serial
        rgnr3 = sf._r3
            #Recognizer__basic_nongreedy_end_by
        gi = hmi.semi_apply_rgnr_(rgnr3)
        return hmi.box4return5gi_(gi)
        777; yield
        ############
        #.############
        #.#see:Recognizer__basic_serial
        #.rgnr = sf._r
        #.rgnr2 = sf._r2
        #.min_sz = sf._m
        #.may_max_sz = sf._M
        #.b_inf = may_max_sz is None

        #.############
        #.def __():
        #.    b_head = True
        #.    _rgnr = rgnr
        #.    for _ in count_(0, min_sz):
        #.        yield b_head, _rgnr
        #.    b_head = False
        #.    _rgnr = rgnr2
        #.    for _ in count_(min_sz, may_max_sz):
        #.        yield b_head, _rgnr
        #.#end-def __():
        #.############

        #.ls = [] # :: [oresult/chain]
        #.for b_head, _rgnr in __():
        #.    if b_inf:
        #.        begin_locator = hmi.tell_locator_()
        #.    reply = yield hmi.semi_apply_rgnr_(_rgnr)
        #.    if hmi.is_ok5reply_(reply):
        #.        if b_inf and hmi.at_locator_(begin_locator):raise Exception('basic_many_rgnr{nullable_rgnr}{inf}')
        #.        oresult = hmi.get_oresult5reply_(reply)
        #.        assert hmi.is_chain_(oresult)
        #.        #check_type_is(Rope, oresult)
        #.        ls.append(oresult)
        #.    elif b_head:
        #.        return hmi.box4return5reply_(reply)
        #.    else:
        #.        #fail{trial_rgnr{rgnr}}
        #.        break
        #.sz = len(ls)
        #.if sz < min_sz:
        #.    reply = hmi.mk_reply5errmsg_(errmsg:=sz)
        #.else:
        #.    oresult = hmi.mk_chain5chains_(ls)
        #.    #oresult = Rope(*ls)
        #.    reply = hmi.mk_reply5oresult_(oresult)
        #.reply
        #.return hmi.box4return5reply_(reply)
#class Recognizer__basic_many(IRecognizer):




class Recognizer__basic_nongreedy_end_by(IRecognizer):
    #basic_nongreedy_end_by_rgnr
    '[hmi::IHdlMutInput__4unlocker&&IHdlMutInput__4snapshot4istream]' \
    '#[used with Recognizer__basic_serial]'
    ___no_slots_ok___ = True
    def __init__(sf, may_rgnr8end, rgnr8body, min_sz, may_max_sz, /):
        check_int_ge(0, min_sz)
        if not may_max_sz is None:
            max_sz = may_max_sz
            check_int_ge(min_sz, max_sz)
        sf._m = min_sz
        sf._M = may_max_sz

        sf._rB = rgnr8body
        sf._rB2 = Recognizer__trial(rgnr8body)
        sf._mrE = may_rgnr8end
        if not may_rgnr8end is None:
            sf._rE2 = Recognizer__trial(may_rgnr8end)
    def __repr__(sf, /):
        may_rgnr8end = sf._mrE
        rgnr8body = sf._rB
        min_sz = sf._m
        may_max_sz = sf._M
        return repr_helper(sf, may_rgnr8end, rgnr8body, min_sz, may_max_sz)

    @override
    def _recognize_(sf, hmi, /):
        '-> GI # [precondition:begin_locator<=end_locator]'
        #see:Recognizer__basic_serial
        may_rgnr8end = sf._mrE
        rgnr8end2 = sf._rE2 if not may_rgnr8end is None else no_branch_rgnr
        rgnr8body = sf._rB
        rgnr8body2 = sf._rB2
        min_sz = sf._m
        may_max_sz = sf._M
        b_inf = may_max_sz is None
        b_head = True
        _rgnr8body = rgnr8body

        ############
        def __():
            b_head = True
            _rgnr8body = rgnr8body
            for _ in count_(0, min_sz):
                yield b_head, _rgnr8body
            b_head = False
            _rgnr = rgnr8body2
            for _ in count_(min_sz, may_max_sz):
                yield b_head, _rgnr8body
        #end-def __():
        ############

        ls = [] # :: [oresult/chain]
        b_end = False
            # whether ls.append(oresult{rgnr8end})
        for b_head, _rgnr8body in __():
            begin_locator = hmi.tell_locator_()
            reply = yield hmi.semi_apply_rgnr_(rgnr8end2)
            if hmi.is_ok5reply_(reply):
                oresult = hmi.get_oresult5reply_(reply)
                assert hmi.is_chain_(oresult)
                #check_type_is(Rope, oresult)
                ls.append(oresult)
                b_end = True
                break
            elif not hmi.at_locator_(begin_locator):
                #fatal_error
                return hmi.box4return5reply_(reply)
            else:
                #retriable_fail
                pass

            reply = yield hmi.semi_apply_rgnr_(_rgnr8body)
            if hmi.is_ok5reply_(reply):
                if b_inf and hmi.at_locator_(begin_locator):raise Exception('basic_nongreedy_end_by_rgnr{nullable_rgnr}{inf}')
                oresult = hmi.get_oresult5reply_(reply)
                assert hmi.is_chain_(oresult)
                #check_type_is(Rope, oresult)
                ls.append(oresult)
            elif b_head:
                # [sz < min_sz]
                return hmi.box4return5reply_(reply)
            elif not hmi.at_locator_(begin_locator):
                #fatal_error
                return hmi.box4return5reply_(reply)
            else:
                #retriable_fail{trial_rgnr{rgnr8body}}
                # [sz >= min_sz]
                break
        ############
        # [b_end] => nongreedy_completed but may have [sz < min_sz]
        # [not b_end] => [sz==max_sz]or[retriable_fail{trial_rgnr{rgnr8body}}][sz >= min_sz]
        ############
        if not may_rgnr8end is None and not b_end and len(ls) >= min_sz:
            rgnr8end = may_rgnr8end
            reply = yield hmi.semi_apply_rgnr_(rgnr8end) #vs:rgnr8end2
            if hmi.is_ok5reply_(reply):
                oresult = hmi.get_oresult5reply_(reply)
                assert hmi.is_chain_(oresult)
                #check_type_is(Rope, oresult)
                ls.append(oresult)
                b_end = True
            else:
                #vs:pass
                return hmi.box4return5reply_(reply)
        assert may_rgnr8end is None or b_end or len(ls) < min_sz
        sz = len(ls) -b_end
        assert b_inf or sz <= may_max_sz
        if sz < min_sz:
            reply = hmi.mk_reply5errmsg_(errmsg:=sz)
        else:
            oresult = hmi.mk_chain5chains_(ls)
            #oresult = Rope(*ls)
            reply = hmi.mk_reply5oresult_(oresult)
        reply
        return hmi.box4return5reply_(reply)
#class Recognizer__basic_nongreedy_end_by(IRecognizer):







class Case4tkn(Enum):
    '# [case4tkn == ("tkn"|"tkd"|"tkey"|"tdat")]' \
    '#[[tkn,tkd,tkey,tdat::Immutable][tkn==(begin_locator,tkd,end_locator)][tkd==(tkey,tdat)][tkey::Eq&&Hashable]]'
    tkn = auto()
    tkd = auto()
    tkey = auto()
    tdat = auto()
Case4tkn






__all__
from seed.recognize.rgnr.abc.IRecognizer import IHdlMutInput
from seed.recognize.rgnr.abc.IRecognizer import IRecognizer

from seed.recognize.rgnr.abc.IRecognizer import (Case4tkn
,IHdlMutInput
,   IHdlMutInput__4chain
,   IHdlMutInput__4ignore
,   IHdlMutInput__4unlocker
,   IHdlMutInput__4snapshot4istream
,   IHdlMutInput__4istream
,   IHdlMutInput__4token
,   IHdlMutInput__4cased
,IRecognizer
,   Recognizer__basic_serial
,       null_chain_rgnr
,   Recognizer__basic_parallel
,       no_branch_rgnr
,   Recognizer__token
,   Recognizer__match_tokens
,   Recognizer__unlock_last
,   Recognizer__trial
,   Recognizer__box
,   Recognizer__lift
,   Recognizer__ignore
,   Recognizer__never_ignore
,   Recognizer__tag
,   Recognizer__look_ahead
,   Recognizer__not_followed_by
,   Recognizer__optional
,   Recognizer__many_box
,   Recognizer__basic_many
,   Recognizer__basic_nongreedy_end_by
)
from seed.recognize.rgnr.abc.IRecognizer import *
