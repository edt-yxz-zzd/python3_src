#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/rgnr/abc/IRecognizer.py
e ../../python3_src/seed/recognize/rgnr/abc/utilities4IRecognizer.py
e ../../python3_src/seed/recognize/rgnr/abc/ISimpleRecognizer.py

seed.recognize.rgnr.abc.IRecognizer
py -m nn_ns.app.debug_cmd   seed.recognize.rgnr.abc.IRecognizer -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.recognize.rgnr.abc.IRecognizer:__doc__ -ht # -ff -df

[[
@20250405
设计冫识别器
  主要目标:py.re+py.str
    用于:e script/对称多项式讠基表达.py
  极简:simple_text_rgnr
    e ../../python3_src/seed/recognize/rgnr/abc/ISimpleRecognizer.py
    *极简递归:simple_text_recursive_rgnr
      view ../../python3_src/seed/func_tools/recur5yield.py
    *极简非递归:simple_text_nonrecursive_rgnr
      no:yield#using "return"
      *极简非递归无环境变量无缓存:simple_text_nonrecursive_nogctx_nocache_rgnr
  参数:识别器.识别扌(通行包,讫限址,欤忽略结果) -> 讫讫错果
    语境无关(无:识别器动态参数)
    静态资源(无:资源解锁器:址==虚址==实址)
    使用语言内建数据类型:输入串::(str,uint) # (文本,起址)
    讫限址唯一(讫限址==讫限址牜虚==移驻型讫限址牜虚==前瞻型讫限址牜虚)
        因为py.re前瞻不越界<<==:
        >>> import re
        >>> rex = re.compile(r'a(?=b)')
        >>> rex.match('ab', 0, 2)
        <re.Match object; span=(0, 1), match='a'>
        >>> rex.match('ab', 0, 1)
        >>> rex.match('ab', 0, 1) is None
        True
        >>> rex.match('ab', 0, 2) is None
        False

  <<==:
  下面过于复杂:
    e ../../python3_src/seed/recognize/rgnr/abc/IRecognizer.py
  参数:识别器.识别扌(通行包,移驻型讫限址牜虚,前瞻型讫限址牜虚,欤忽略结果,识别器动态参数,资源解锁器) -> 讫讫错果
      讫讫错果==(讫址牜虚牜移至,讫址牜虚牜远至,错误屮成果)
      识别结果/错误屮成果==(错误丷成果,错误丨成果)
      通行包==(递归组,输入串,环境变量)
      递归组:
        +纯核递归组/识别器构造器名解析包::(识别器构造器名,识别器静态参数)->识别器
        +递归组配置
      识别器动态参数(语境相关:输入串+起址牜实:前文/前情提要:串联后件)
      输入串{定位于:,起址牜实(实址:锁定资源)}
          +回顾长度上限
          +前瞻长度上限
      移驻型讫限址牜虚,前瞻型讫限址牜虚(虚址:资源无关)
        前后关系？考虑到:前瞻长度上限...可能没有前后关系...
      资源解锁器/分支排他器:管理-动态资源{输入串}
      环境变量:
        #变量环境初始化:一次:本次识别过程
        #变量环境初始化:每:识别器
        +变量环境纟递归组
          比如:缓存:递归组-解析结果{(识别器构造器名,识别器静态参数):识别器}
          比如:缓存:递归组-识别器属性{递归组配置}{(识别器构造器名,识别器静态参数,符号冃属性名):识别器属性(浅|深)}
        +变量环境纟丮递归组丶输入串厈
          比如:缓存:识别结果{(识别器,起址牜虚,移驻型讫限址牜虚,前瞻型讫限址牜虚,欤忽略结果,识别器动态参数):讫讫错果}
          比如:缓存:输入串-回顾串&前瞻串
        +变量环境纟动态运行期#每次识别过程
    识别器-属性:
    识别器构造器-属性:
      +浅枚举冫子识别器构造器
        +深枚举冫后裔识别器构造器
      #(浅属性,深属性)@缓存于:变量环境纟递归组
      +回顾长度需求
      +前瞻长度需求
      +欤讫址无关:即:右侧自刹/合法语句不是合法语句的真前缀
      +欤语境无关:即:识别器动态参数-无用
      +欤识别结果不可改动:immutable
]]
URL:abbr. 全球资源定位器（Uniform Resource Locator）
DNS:abbr. 域名服务器（Domain Name Server）；十进位计数制（Dicimal Number System）
DDNS:abbr. 动态域名服务（Dynamic Domain Name Server）
[[
rgnz_reply
    .end_pure_locator4reply
    .end_pure_locator4access#[farthest via (peek|read)]
    .rgnz_eresult==(Either rgnz_errmsg rgnz_oresult)==(ok, (rgnz_errmsg|rgnz_oresult))
args4recur_call
    .ireplace_(...)
    .common4recur_call
        .rgnr_name_server
            .rgnr5name_(...)#vivi:DNS
            .static_globals4rgnr_group#sggp{rgnr_name_server[,all_input_stream,all_runs]}
                .cache4rgnr_group
                .settings4rgnr_group#sgsettings{rgnr_name_server[,all_input_stream,all_runs]}
            #.combinator
            .mk_rgnr_(case, *args)
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
        .seekable_input_stream
            .tell__pure_locator_()
            .tell__snapshot_()
            .seek__snapshot_(snapshot)
                [snapshot <: unlocker]
                [snapshot.pure_locator]
                #.tell__unlockable_locator_()
                #.seek__unlockable_locator_(unlockable_locator)
            .iter_peeks_(*, with_end_pure_locator)
            .iter_reads_()
            .imay_size4look_ahead
            .imay_size4look_behind
            .reversed_iter_peeks_(*, with_begin_pure_locator)
            #
            # .peek_le_(sz, *, with_end_pure_locator)
            # .read_le_(sz)
            # .peek1_()
            # .read1_()
            # .head
        .static_global_environ#sgenv{rgnr_name_server,seekable_input_stream[,all_runs]}
        .dynamic_global_context#dgctx{rgnr_name_server,seekable_input_stream,curr_run}
    .end_pure_locator4move_ahead#consume#unlocked/release
    .end_pure_locator4look_ahead#locked
    .ignore
    .user_defined_extra_data
args4local_call
    .may_dynamic_params6ctx#local_ctx#dlctx
    .unlocker
        .release_()
        .released
        .fork()
initialize+finalize:
    #only:rgnr_name_server
    rgnr.setup_per_grammar__static_globals4rgnr_group_(common4recur_call)

    #both:rgnr_name_server,seekable_input_stream
    rgnr.setup_per_grammarXistream__static_global_environ_(rgnr_name_server,seekable_input_stream,static_global_environ)
    main_rgnr.main_setup_per_run__dynamic_global_context_(args4recur_call)
    rgnr.setup_per_run__dynamic_global_context_(args4recur_call)
    main_rgnr.main_teardown_per_run__dynamic_global_context_(args4recur_call)
]]


py_adhoc_call   seed.recognize.rgnr.abc.IRecognizer   @f
from seed.recognize.rgnr.abc.IRecognizer import *
]]]'''#'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
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


class IQuasiRecognizer(ABC):
    '[quasi_rgnr==(rgnr|rgnr_mkr)] # cache@rgnr_name_server.static_globals4rgnr_group'
    __slots__ = ()
    @abstractmethod
    def iter_child_quasi_recognizers_(sf, rgnr_name_server, /):
        'rgnr_name_server -> Iter IQuasiRecognizer # [usually not includes self]'
    ######################
    #.view ../../python3_src/seed/recognize/rgnr/abc/utilities4IRecognizer.py
    #.@abstractmethod
    #.def iter_descendant_quasi_recognizers_(sf, rgnr_name_server, /):
    #.    'rgnr_name_server -> Iter IQuasiRecognizer # [usually not includes self]'
    ######################

    #asif-@cache_property
    @abstractmethod
    def get_whether_rgnr_reply_immutable_(sf, rgnr_name_server, /):
        '-> whether_rgnr_reply_immutable/bool'
    @abstractmethod
    def get_whether_context_free_(sf, rgnr_name_server, /):
        '-> whether_context_free/bool  #[may_dynamic_params6ctx := None]'
    @abstractmethod
    def get_whether_proper_prefix_illegal_(sf, rgnr_name_server, /):
        '-> whether_proper_prefix_illegal/bool  #auto_brake #e.g:no-tail-pattern:"a*"'
    @abstractmethod
    def get_imay_size4look_ahead_(sf, rgnr_name_server, /):
        '-> imay_size4look_ahead/int{>=-1}'
    @abstractmethod
    def get_imay_size4look_behind_(sf, rgnr_name_server, /):
        '-> imay_size4look_behind/int{>=-1}'

class IRecognizer(IQuasiRecognizer):
    'rgnr # [GI==GeneratorIterator]'
    __slots__ = ()
    @abstractmethod
    def recognize_(sf, args4recur_call, args4local_call, /):
        'IArgs4recur_call -> IArgs4local_call -> GI(yield:gi/GI;return:rgnz_reply/IRecognizeReply)'

    ######################
    ######################
    #only:rgnr_name_server
    @abstractmethod
    def setup_per_grammar__static_globals4rgnr_group_(sf, common4recur_call, /):
        '-> None # setup common4recur_call.static_globals4rgnr_group'

    #both:rgnr_name_server,seekable_input_stream
    @abstractmethod
    def setup_per_grammarXistream__static_global_environ_(sf, rgnr_name_server, seekable_input_stream, static_global_environ, /):
        '-> None # setup static_global_environ@args4recur_call'
    @abstractmethod
    def main_setup_per_run__dynamic_global_context_(sf8main, args4recur_call, /):
        '-> None # setup args4recur_call.dynamic_global_context when [sf is the main_rgnr of current run]'
    @abstractmethod
    def setup_per_run__dynamic_global_context_(sf, args4recur_call, /):
        '-> None # setup args4recur_call.dynamic_global_context'
    @abstractmethod
    def main_teardown_per_run__dynamic_global_context_(sf8main, args4recur_call, /):
        '-> None # teardown args4recur_call.dynamic_global_context when [sf is the main_rgnr of current run]'

class IRecognizeReply(ABC):
    'rgnz_reply'
    __slots__ = ()
    @abstractmethod
    def ireplace_(sf, /, **kwds):
        '-> ot/__class__'
    @property
    @abstractmethod
    def end_pure_locator4reply(sf, /):
        '-> IPureLocator'
    @property
    @abstractmethod
    def end_pure_locator4access(sf, /):
        '-> IPureLocator # [farthest reached via (peek|read)]'
    @property
    @abstractmethod
    def rgnz_eresult(sf, /):
        '-> (Either rgnz_errmsg rgnz_oresult)'
        from seed.types.Either import Cased, Either, KindedName
        from seed.types.Either import mk_Left, mk_Right
class IArgs4local_call(ABC):
    'args4local_call'
    __slots__ = ()
    @classmethod
    @abstractmethod
    def mk_(cls, may_dynamic_params6ctx, unlocker, /):
        '-> ot/cls'
    #.@abstractmethod
    #.def ireplace_(sf, /, **kwds):
    #.    '-> ot/__class__'
    @property
    @abstractmethod
    def may_dynamic_params6ctx(sf, /):
        '-> may dynamic_params6ctx/dyn_local_ctx#dlctx'
    @property
    @abstractmethod
    def unlocker(sf, /):
        '-> IUnlocker'
class IArgs4recur_call(ABC):
    'args4recur_call'
    __slots__ = ()
    # .user_defined_extra_data
    @abstractmethod
    def ireplace_(sf, /, **kwds):
        '-> ot/__class__'
    @property
    @abstractmethod
    def common4recur_call(sf, /):
        '-> ICommon4recur_call'
    @property
    @abstractmethod
    def end_pure_locator4look_ahead(sf, /):
        '-> IPureLocator'
    @property
    @abstractmethod
    def end_pure_locator4move_ahead(sf, /):
        '-> IPureLocator'
    @property
    @abstractmethod
    def ignore(sf, /):
        '-> bool'
class ICommon4recur_call(ABC):
    'common4recur_call'
    __slots__ = ()
    @property
    @abstractmethod
    def rgnr_name_server(sf, /):
        '-> IRecognizerNameServer'
    @property
    @abstractmethod
    def seekable_input_stream(sf, /):
        '-> sistream/ISeekableInputStream'
    @property
    @abstractmethod
    def static_global_environ(sf, /):
        '-> sgenv/IMapping # vars{sistream} # cache{rgnz_oresult@[whether_proper_prefix_illegal&&whether_context_free&&whether_rgnr_reply_immutable]}'
    @property
    @abstractmethod
    def dynamic_global_context(sf, /):
        '-> dgctx/IMapping #curr_rgnz only # cache{rgnz_oresult@[whether_proper_prefix_illegal&&whether_context_free&&not whether_rgnr_reply_immutable]}'

class IRecognizerNameServer(ABC):
    'rgnr_name_server#vivi:DNS'
    __slots__ = ()
    @property
    @abstractmethod
    def static_globals4rgnr_group(sf, /):
        '-> sggp/IMapping # configuration/settings and cache{descendant}'
    @abstractmethod
    def rgnr5name_(sf, name, /):
        'nm4rgnr -> IRecognizer|^LookupError'
    @abstractmethod
    def mk_rgnr_(sf, case, /, *args6case):
        'case -> (*args{case}) -> IRecognizer'
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
class IInputStream(ABC):
    'input_stream'
    __slots__ = ()
    ######################
    @property
    @abstractmethod
    def imay_size4look_ahead(sf, /):
        '-> int{>=-1}'
    @property
    @abstractmethod
    def imay_size4look_behind(sf, /):
        '-> int{>=-1}'
    ######################
    @abstractmethod
    def tell__pure_locator_(sf, /):
        '-> IPureLocator'
    @abstractmethod
    def iter_tokens_(sf, /, *, peek_vs_read, with_end_pure_locator):
        '-> Iter (token if not with_end_pure_locator else (token, end_pure_locator))'
    @abstractmethod
    def reversed_iter_peek_tokens_(*, with_begin_pure_locator)
        '-> Iter (token if not with_end_pure_locator else (begin_pure_locator, token))'
    ######################
    ######################
    #.@abstractmethod
    #.def iter_peeks_(sf, /, *, with_end_pure_locator):
    #.    '-> Iter (token if not with_end_pure_locator else (token, end_pure_locator))'
    #.@abstractmethod
    #.def iter_reads_(sf, /, *, with_end_pure_locator):
    #.    '-> Iter (token if not with_end_pure_locator else (token, end_pure_locator))'
    #..peek_le_(sz, *, with_end_pure_locator)
    #..read_le_(sz)
    #..peek1_()
    #..read1_()
    #..head
class ISeekableInputStream(IInputStream):
    'seekable_input_stream/sistream'
    __slots__ = ()
    @abstractmethod
    def tell__snapshot_(sf, /):
        '-> ISnapshot4ISeekableInputStream'
    @abstractmethod
    def seek__snapshot_(sf, snapshot, /):
        'ISnapshot4ISeekableInputStream -> None'
    #.@abstractmethod
    #.def iter_tokens_(sf, /, *, peek_vs_read, with_end_locator, pure_locator_vs_snapshot):
    #.    '-> Iter (token if not with_end_locator else (token, (end_pure_locator if not pure_locator_vs_snapshot else end_snapshot)))'
class IPureLocator(IHashable, ITotalOrdered):
    'pure_locator'
    __slots__ = ()
    @abstractmethod
    def __hash__(sf, /):
        '-> int'
    @abstractmethod
    def __eq__(sf, ot, /):
        '-> bool'
    @abstractmethod
    def __lt__(sf, ot, /):
        '-> bool'
class IUnlocker(ABC):
    'unlocker'
    __slots__ = ()
    @property
    @abstractmethod
    def released(sf, /):
        '-> bool'
    @abstractmethod
    def release_(sf, /):
        '-> None{sf.released}'
    @abstractmethod
    def fork_(sf, /):
        '-> ot/__class__'
class ISnapshot4ISeekableInputStream(IUnlocker):
    '[snapshot <: unlocker]'
    __slots__ = ()
    @property
    @abstractmethod
    def pure_locator(sf, /):
        '-> IPureLocator'





__all__
from seed.recognize.rgnr.abc.IRecognizer import *
