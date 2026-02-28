#__all__:goto
r'''[[[
e ../../python3_src/seed/int_tools/int_repr7lex_order7base.py
e ../../python3_src/seed/int_tools/int_repr7lex_order7base__part2.py


seed.int_tools.int_repr7lex_order7base
py -m nn_ns.app.debug_cmd   seed.int_tools.int_repr7lex_order7base -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.int_tools.int_repr7lex_order7base:__doc__ -ht # -ff -df
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.int_tools.int_repr7lex_order7base:cls@T    =T   +exclude_attrs5listed_in_cls_doc
#######
from seed.pkg_tools.ModuleReloader import mk_doctestXmodule_reloader_
doctestXmodule_reloader = mk_doctestXmodule_reloader_('', 'seed.int_tools.int_repr7lex_order7base:__doc__', '-ht')
doctestXmodule_reloader(reload_first=False)
doctestXmodule_reloader()
#######

[[
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.int_tools.int_repr7lex_order7base   @f

]]]'''#'''
__all__ = r'''
魖数据位元串表达牜词典序牜前置长度
    魖数据字符串表达牜词典序牜前置长度
        魖数据字符串表达牜词典序牜前置长度牜使用匴数据位元串表达

魖数据位元串表达牜词典序牜前置长度
    魖有理数位元串表达牜词典序牜前置长度
    魖整数位元串表达牜词典序牜前置长度
        魖整数位元串表达牜词典序牜前置长度牜整数零编码为单胞
            魖整数位元串表达牜词典序牜前置长度牜整数零编码为单胞牜使用自然数编码器
    魖自然数位元串表达牜词典序牜前置长度

魖数据位元串表达牜词典序牜前置长度
    表述冫数据讠位元串表达扌
    解读冫数据巛位元串表达扌
    详解读冫数据巛位元串表达扌
    详解读冫数据巛趃位元串扌
        encode_dat2digit_seq7lex_order_
        decode_dat5digit_seq7lex_order_
        xdecode_dat5digit_seq7lex_order_
        xdecode_dat5iter_digits7lex_order_

    魖数据字符串表达牜词典序牜前置长度
        表述冫数据讠字符串表达扌
        解读冫数据巛字符串表达扌
        详解读冫数据巛字符串表达扌
        详解读冫数据巛趃字符串扌
            encode_dat2txt7lex_order_
            decode_dat5txt7lex_order_
            xdecode_dat5txt7lex_order_
            xdecode_dat5iter_chars7lex_order_



FormatError
检查冫字母表扌
求冫总字母表相关信息扌
求冫符型相关信息扌


解读冫数据巛囜元串表达扌
详解读冫数据巛囜元串表达扌
    规范冫起讫纟列表扌
    趃子串扌
    魖定型定长前取器
        魖定型定长前取器牜造反
            乸定型定长前取器巛趃位元串
                乸计耗器
            乸定型定长前取器牜符型偏移
            乸定型定长前取器牜添加头胞



魖整数位元串表达牜词典序牜前置长度牜整数零编码为单胞牜使用自然数编码器
    乸整数位元串表达牜词典序牜前置长度牜整数零编码为单胞牜使用自然数编码器

魖数据字符串表达牜词典序牜前置长度牜使用匴数据位元串表达
    乸数据字符串表达牜词典序牜前置长度牜使用匴数据位元串表达




位元串巛趃位元串乊规模牜基准版扌
'''.split()#'''
    #_魖共通
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.abc.abc__ver1 import abstractmethod, override, ABC
from numbers import Rational
#.
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from functools import cached_property
    from itertools import islice, accumulate, chain
    from seed.types.FrozenDict import mk_FrozenDict
    from seed.iters.chains import chains
    from seed.tiny_.check import check_type_le, check_type_is, check_int_ge, icheck_, check_uint_lt, check_all_, check_non_ABC#no:icheck_int_ge_lt
    from seed.types.WordSeq import mk_WordSeq
    #def mk_WordSeq(may_words=None, imay_num_bytes4word=-1, imay_num_words=-1, may_bytes8words=None, /, *, imay_max_num_bytes4word=-1):

#.    from seed.helper.repr_input import repr_helper

#.#################################
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError(Exception, StopIteration)

__all__


class FormatError(Exception):pass



def 检查冫字母表扌(最小规模, 字母表, /, *, 欤无重复=True, 欤升序=True, 欤奇数规模=False):
    check_type_is(str, 字母表)
    if not 字母表:raise TypeError
    if not len(字母表) >= 最小规模:raise TypeError
    if 欤奇数规模:
        if not 1 == (len(字母表) & 1):raise TypeError
    if 欤无重复:
        if not len(字母表) == len(set(字母表)):raise TypeError
    if 欤升序:
        if not list(字母表) == sorted(字母表):raise TypeError


def 求冫符型相关信息扌(符型讠规模纟字母表, /, *, 欤编码无需头胞, 欤编码呈奇性对称分布):
    '-> 符型相关信息/(规模纟总字母表, 符型讠位元偏移量, 符型讠规模纟字母表, 位元讠取反位元)'
    check_type_is(tuple, 符型讠规模纟字母表)
    check_type_is(bool, 欤编码无需头胞)
    check_type_is(bool, 欤编码呈奇性对称分布)
    if not len(符型讠规模纟字母表) >= 2-欤编码无需头胞:raise TypeError
    if not 欤编码无需头胞:
        规模纟字母表牜头胞 = 符型讠规模纟字母表[0]
        check_int_ge(1, 规模纟字母表牜头胞)
        欤奇数规模 = 欤编码呈奇性对称分布
        if 欤奇数规模:
            if not 1 == (1 & 规模纟字母表牜头胞):raise TypeError

    for 规模纟字母表牜颈胞 in 符型讠规模纟字母表[1-欤编码无需头胞:-1]:
        check_int_ge(1, 规模纟字母表牜颈胞)
    规模纟字母表牜体胞 = 符型讠规模纟字母表[-1]
    check_int_ge(2, 规模纟字母表牜体胞)
    规模纟总字母表 = sum(符型讠规模纟字母表)
    #bug:符型讠位元偏移量 = (0, *accumulate(符型讠规模纟字母表[:-1]))
    符型讠位元偏移量 = (0, *accumulate(reversed(符型讠规模纟字母表[1:])))[::-1]
    assert len(符型讠位元偏移量) == len(符型讠规模纟字母表)
    if len(符型讠规模纟字母表) >= 2:
        assert 符型讠位元偏移量[-2] == 符型讠规模纟字母表[-1], (符型讠位元偏移量[-2],  符型讠规模纟字母表[-1], 符型讠位元偏移量, 符型讠规模纟字母表)
    assert 符型讠位元偏移量[0] == 规模纟总字母表 -符型讠规模纟字母表[0]
    assert 符型讠位元偏移量[-1] == 0
    #bug:位元讠取反位元 = tuple(chains(reversed(range(偏移量, 偏移量+规模)) for 偏移量, 规模 in zip(符型讠位元偏移量, 符型讠规模纟字母表)))
    位元讠取反位元 = tuple(chains(reversed(range(偏移量, 偏移量+规模)) for 偏移量, 规模 in zip(reversed(符型讠位元偏移量), reversed(符型讠规模纟字母表))))
    符型相关信息 = (规模纟总字母表, 符型讠位元偏移量, 符型讠规模纟字母表, 位元讠取反位元)
    hash(符型相关信息)
    return 符型相关信息


def 求冫总字母表相关信息扌(列表纟字母表牜头胞辻多种体胞, /, *, 欤编码无需头胞, 欤编码呈奇性对称分布):
    '-> 总字母表相关信息/(总字母表/位元讠字符, 字符讠位元, 字符讠取反字符)'
    check_type_is(tuple, 列表纟字母表牜头胞辻多种体胞)
    check_type_is(bool, 欤编码无需头胞)
    check_type_is(bool, 欤编码呈奇性对称分布)
    if not len(列表纟字母表牜头胞辻多种体胞) >= 2-欤编码无需头胞:raise TypeError
    if not 欤编码无需头胞:
        字母表牜头胞 = 列表纟字母表牜头胞辻多种体胞[0]
        检查冫字母表扌(1, 字母表牜头胞, 欤奇数规模=欤编码呈奇性对称分布)

    for 字母表牜颈胞 in 列表纟字母表牜头胞辻多种体胞[1-欤编码无需头胞:-1]:
        检查冫字母表扌(1, 字母表牜颈胞)
    字母表牜体胞 = 列表纟字母表牜头胞辻多种体胞[-1]
    检查冫字母表扌(2, 字母表牜体胞)
    总字母表 = ''.join(chains(reversed(列表纟字母表牜头胞辻多种体胞)))
    检查冫字母表扌(3-欤编码无需头胞, 总字母表, 欤升序=False)
    位元讠字符 = 总字母表
    字符讠位元 = mk_FrozenDict({字符:位元 for 位元, 字符 in enumerate(位元讠字符)})
    if not len(字符讠位元) == len(位元讠字符):raise 000
    字符讠取反字符 = mk_FrozenDict({字符:取反字符 for 字母表 in 列表纟字母表牜头胞辻多种体胞 for 字符,取反字符 in zip(字母表, reversed(字母表))})
    总字母表相关信息 = (位元讠字符, 字符讠位元, 字符讠取反字符)
    hash(总字母表相关信息)
    return 总字母表相关信息
    #.符型讠位元偏移量 = tuple(字符讠位元[字母表[0]] for 字母表 in 列表纟字母表牜头胞辻多种体胞)
    #.符型讠规模纟字母表 = tuple(map(len, 列表纟字母表牜头胞辻多种体胞))
    #.assert 符型讠规模纟字母表 == tuple(map(int.__sub__, (len(总字母表), *符型讠位元偏移量[:-1]), 符型讠位元偏移量))
    #.assert len(符型讠规模纟字母表) == len(符型讠位元偏移量) == len(列表纟字母表牜头胞辻多种体胞)
    #.if not 欤编码无需头胞:
    #.    assert 符型讠规模纟字母表[0] == len(字母表牜头胞)
    #.else:
    #.    assert 符型讠规模纟字母表[0] == len(列表纟字母表牜头胞辻多种体胞[0])
    #.assert 符型讠规模纟字母表[-1] == len(字母表牜体胞)
    #.assert 符型讠位元偏移量[0] == len(总字母表) -len(字母表牜体胞)
    #.assert 符型讠位元偏移量[-1] == 0
    #.return (位元讠字符, 字符讠位元, 符型讠位元偏移量, 符型讠规模纟字母表)


class _魖共通(ABC):
    __slots__ = ()
    @property
    @abstractmethod
    def 符型讠规模纟字母表(sf, /):
        '-> 符型讠规模纟字母表/tuple{len(列表纟字母表牜头胞辻多种体胞[符型])}{len=len(列表纟字母表牜头胞辻多种体胞)}'
    ##################
    def 位元串巛趃位元串牜合表扌(sf, 趃位元串, /):
        '趃位元串 -> 位元串'
        return sf.位元串巛趃位元串乊规模纟字母表扌(sf.规模纟总字母表, 趃位元串)
    def 位元串巛趃位元串牜子表扌(sf, 符型, 趃位元串, /):
        '符型 -> 趃位元串 -> 位元串'
        规模纟字母表乊符型 = sf.符型讠规模纟字母表[符型]
        return sf.位元串巛趃位元串乊规模纟字母表扌(规模纟字母表乊符型, 趃位元串)
    def 位元串巛趃位元串乊规模纟字母表扌(sf, 规模纟字母表, 趃位元串, /):
        '规模纟字母表 -> 趃位元串 -> 位元串'
        return 位元串巛趃位元串乊规模牜基准版扌(规模纟字母表, 趃位元串)
    ##################
def 位元串巛趃位元串乊规模牜基准版扌(规模纟字母表, 趃位元串, /):
    位元串 = bytes(趃位元串) if 规模纟字母表 <= 256 else mk_WordSeq(趃位元串, imay_max_num_bytes4word=4)
    return 位元串

#移至:...part2.py
#:::class 魖匴全局参数设置纟自然数编解码器(_魖共通):
#:::    '匴全局参数设置'
#:::    __slots__ = ()
#:::    r'''[[[
#:::    必要:
#:::        自然数巛位元串牜分离首胞乊规模纟字母表扌
#:::        符型讠规模纟字母表
#:::            #罓符型讠规模纟体胞
#:::        位元串巛趃位元串牜子表扌
#:::        位元串巛趃位元串乊规模纟字母表扌
#:::            #罓体胞规模讠趃位元串讠位元串扌
#:::    ]]]'''#'''
#:::    @abstractmethod
#:::    def 自然数巛位元串牜分离首胞乊规模纟字母表扌(sf, 规模纟字母表, 首胞, 位元串, /):
#:::        '规模纟字母表 -> 首胞 -> 位元串 -> 自然数'
class 魖数据位元串表达牜词典序牜前置长度(_魖共通):
    __slots__ = ()
    ##################
    @property
    @abstractmethod
    def 欤编码无需头胞(sf, /):
        '-> bool #eg:内部使用的自然数编码'
    @property
    @abstractmethod
    def 欤编码呈奇性对称分布(sf, /):
        #.def 欤编码负零正对称分布(sf, /):
        '-> bool #[整数vs自然数vs有理数/连分数]'
    @property
    @abstractmethod
    def 符型讠规模纟字母表(sf, /):
        '-> 符型讠规模纟字母表/tuple{len(列表纟字母表牜头胞辻多种体胞[符型])}{len=len(列表纟字母表牜头胞辻多种体胞)}'
    ##################

    @abstractmethod
    def 罓表述冫数据讠趃序列纟带符型位元串扌(sf, 数据, /):
        '数据 -> 趃序列纟带符型位元串/(Iter 带符型位元串/(符型/uint%len(符型讠规模纟字母表), 位元串牜子表/[位元{符型}]/(tuple|bytes|WordSeq)))'
    @abstractmethod
    def 罓解读冫数据巛定型定长前取器扌(sf, 定型定长前取器, /):
        '魖定型定长前取器{位元{符型}} -> 数据'
    @abstractmethod
    def 检查冫数据扌(sf, 数据, /):
        '数据 -> None'

    ##################
    #.@property
    #.@abstractmethod
    #.def 空位元串(sf, /):
    #.    '-> 位元串/[位元/uint%len(总字母表)]{len==0}'
    ##################

    @cached_property
    def 符型相关信息(sf, /):
        '-> (规模纟总字母表/uint, 符型讠位元偏移量/tuple{uint%len(总字母表)}{len=len(列表纟字母表牜头胞辻多种体胞)}, 符型讠规模纟字母表/tuple{len(列表纟字母表牜头胞辻多种体胞[符型])}{len=len(列表纟字母表牜头胞辻多种体胞)}, 位元讠取反位元/tuple{uint%len(总字母表)}{len=len(总字母表)})'
        (规模纟总字母表, 符型讠位元偏移量, 符型讠规模纟字母表, 位元讠取反位元) = 求冫符型相关信息扌(sf.符型讠规模纟字母表, 欤编码无需头胞=sf.欤编码无需头胞, 欤编码呈奇性对称分布=sf.欤编码呈奇性对称分布)
        return (规模纟总字母表, 符型讠位元偏移量, 符型讠规模纟字母表, 位元讠取反位元)

    @cached_property
    def 位元讠取反位元(sf, /):
        '-> 位元讠取反位元/tuple{uint%len(总字母表)}{len=len(总字母表)}'
        return sf.符型相关信息[3]
    @cached_property
    def 符型讠位元偏移量(sf, /):
        '-> 符型讠位元偏移量/tuple{uint%len(总字母表)}{len=len(列表纟字母表牜头胞辻多种体胞)}'
        return sf.符型相关信息[1]
    @cached_property
    def 规模纟总字母表(sf, /):
        '-> uint/len(总字母表)'
        return sf.符型相关信息[0]
        return sum(sf.符型讠规模纟字母表)

    ##################
    def 外移冫位元串扌(sf, 符型, 位元串牜子表, /):
        '符型 -> 位元串牜子表/[位元{字母表{符型}}] -> 位元串牜合表/[位元{总字母表}]'
        位元偏移量 = sf.符型讠位元偏移量[符型]
        位元串牜合表 = sf.位元串巛趃位元串牜合表扌(map(位元偏移量.__add__, 位元串牜子表))
        return 位元串牜合表
    def 内移冫位元串扌(sf, 符型, 位元串牜合表, /):
        '符型 -> 位元串牜合表/[位元{总字母表}] -> 位元串牜子表/[位元{字母表{符型}}]'
        位元偏移量 = sf.符型讠位元偏移量[符型]
        位元串牜子表 = sf.位元串巛趃位元串牜子表扌(符型, map(位元偏移量.__rsub__, 位元串牜合表))
        return 位元串牜子表
    def 取反冫带符型位元串扌(sf, 符型,  位元串牜子表, /):
        '符型 ->  位元串牜子表{符型} -> 带符型位元串/(符型/uint%len(符型讠规模纟字母表), 位元串牜子表/[位元{符型}])'
        规模纟字母表乊符型 = sf.符型讠规模纟字母表[符型]
        位元串牜子表 = sf.位元串巛趃位元串牜子表扌(符型, map((-1+规模纟字母表乊符型).__sub__, 位元串牜子表))
        带符型位元串 = (符型, 位元串牜子表)
        return 带符型位元串

    def 取反冫趃序列纟带符型位元串扌(sf, 趃序列纟带符型位元串, /):
        '趃序列纟带符型位元串 -> 趃序列纟带符型位元串/(Iter 带符型位元串/(符型/uint%len(符型讠规模纟字母表), 位元串牜子表/[位元{符型}]/(tuple|bytes|WordSeq)))'
        趃序列纟带符型位元串 = (sf.取反冫带符型位元串扌(符型, 位元串牜子表) for (符型, 位元串牜子表) in 趃序列纟带符型位元串)
        return 趃序列纟带符型位元串
    def 取反冫趃位元串牜合表扌(sf, 趃位元串牜合表, /):
        '趃位元串牜合表 -> 趃位元串牜合表/(Iter 位元牜合表{总字母表})'
        取反扌 = sf.位元讠取反位元.__getitem__
        return map(取反扌, 趃位元串牜合表)
        #.#趃位元串串 = (构串扌(map(取反扌, 位元串)) for 位元串 in 趃位元串串)
        #.构串扌 = sf.位元串巛趃位元串牜合表扌
        #.return 构串扌(map(取反扌, 位元串))
    ##################
    def 详解读冫数据巛趃位元串扌(sf, 趃位元串, /):
        '趃位元串/(Iter 位元) -> (数据, 已消耗位元数目, 趃位元串)'
        定型定长前取器 = 乸定型定长前取器巛趃位元串(sf, 已消耗位元数目:=0, 趃位元串:=iter(趃位元串))
        数据 = sf.罓解读冫数据巛定型定长前取器扌(定型定长前取器)
        sf.检查冫数据扌(数据)
        return (数据, 定型定长前取器.已消耗位元数目, 定型定长前取器.趃位元串)
    ##################
    def 表述冫数据讠趃位元串表达扌(sf, 数据, /):
        '数据 -> 趃位元串/(Iter 位元/uint%len(总字母表))'
        sf.检查冫数据扌(数据)
        趃序列纟带符型位元串 = sf.罓表述冫数据讠趃序列纟带符型位元串扌(数据)
        return chains(sf.外移冫位元串扌(符型, 位元串牜子表) for (符型, 位元串牜子表) in 趃序列纟带符型位元串)
    def 表述冫数据讠位元串表达扌(sf, 数据, /, *, 欤校验):
        '数据 -> 位元串/[位元/uint%len(总字母表)]'
        位元串 = sf.位元串巛趃位元串牜合表扌(sf.表述冫数据讠趃位元串表达扌(数据))
        if 欤校验:
            if not 数据 == (_数据:=sf.解读冫数据巛位元串表达扌(位元串, 欤校验=False)):raise Exception(数据, _数据, 位元串)
        return 位元串

    ##################
    def 解读冫数据巛位元串表达扌(sf, 位元串, 起址=None, 讫址=None, /, *, 欤校验):
        '位元串 -> 起址 -> 讫址 -> 数据'
        return 解读冫数据巛囜元串表达扌(sf.表述冫数据讠位元串表达扌, sf.详解读冫数据巛趃位元串扌, 位元串, 起址, 讫址, 欤校验=欤校验)
    def 详解读冫数据巛位元串表达扌(sf, 位元串, 起址=None, 讫址=None, /, *, 欤校验):
        '位元串 -> 起址 -> 讫址 -> (数据, 讫址)'
        return 详解读冫数据巛囜元串表达扌(sf.表述冫数据讠位元串表达扌, sf.详解读冫数据巛趃位元串扌, 位元串, 起址, 讫址, 欤校验=欤校验)
    ##################
    ##################
    def encode_dat2digit_seq7lex_order_(sf, dat, /, *, validate=True):
        'dat -> [digit/uint]'
        digit_seq = sf.表述冫数据讠位元串表达扌(dat, 欤校验=validate)
        return digit_seq
    def decode_dat5digit_seq7lex_order_(sf, digit_seq, begin=None, end=None, /, *, validate=True):
        '[digit/uint] -> dat'
        dat = sf.解读冫数据巛位元串表达扌(digit_seq, begin, end, 欤校验=validate)
        return dat
    def xdecode_dat5digit_seq7lex_order_(sf, digit_seq, begin=None, end=None, /, *, validate=True):
        '[digit/uint] -> (dat, end)'
        (dat, end) = sf.详解读冫数据巛位元串表达扌(digit_seq, begin, end, 欤校验=validate)
        return (dat, end)
    def xdecode_dat5iter_digits7lex_order_(sf, digits, /):
        '(Iter digit/uint) -> (dat, num_consumed_digits/uint, iter_remain_digits/(Iterator digit/uint))'
        (dat, num_consumed_digits, iter_remain_digits) = sf.详解读冫数据巛趃位元串扌(digits)
        return (dat, num_consumed_digits, iter_remain_digits)
    ##################
表述冫数据讠位元串表达扌 = 魖数据位元串表达牜词典序牜前置长度.表述冫数据讠位元串表达扌
解读冫数据巛位元串表达扌 = 魖数据位元串表达牜词典序牜前置长度.解读冫数据巛位元串表达扌
详解读冫数据巛位元串表达扌 = 魖数据位元串表达牜词典序牜前置长度.详解读冫数据巛位元串表达扌
详解读冫数据巛趃位元串扌 = 魖数据位元串表达牜词典序牜前置长度.详解读冫数据巛趃位元串扌
encode_dat2digit_seq7lex_order_ = 魖数据位元串表达牜词典序牜前置长度.encode_dat2digit_seq7lex_order_
decode_dat5digit_seq7lex_order_ = 魖数据位元串表达牜词典序牜前置长度.decode_dat5digit_seq7lex_order_
xdecode_dat5digit_seq7lex_order_ = 魖数据位元串表达牜词典序牜前置长度.xdecode_dat5digit_seq7lex_order_
xdecode_dat5iter_digits7lex_order_ = 魖数据位元串表达牜词典序牜前置长度.xdecode_dat5iter_digits7lex_order_



class 魖数据字符串表达牜词典序牜前置长度(魖数据位元串表达牜词典序牜前置长度):
    #class 魖整数字符串表达牜词典序牜前置长度(ABC):
    __slots__ = ()
    ##################
    @property
    @abstractmethod
    def 列表纟字母表牜头胞辻多种体胞(sf, /):
        '-> 列表纟字母表牜头胞辻多种体胞/符型讠字母表/[str{len>=1}]{len>=2}'
    ##################
    #@property
    @cached_property
    def 字母表牜头胞(sf, /):
        '-> str'
        if sf.欤编码无需头胞:
            raise AttributeError('字母表牜头胞')
        return sf.列表纟字母表牜头胞辻多种体胞[0]

    @cached_property
    def 总字母表相关信息(sf, /):
        '-> (总字母表/位元讠字符/str, 字符讠位元/{char:uint%len(总字母表)}, 字符讠取反字符/{字符:字符})'
        #'-> (总字母表/位元讠字符/str, 字符讠位元/{char:uint%len(总字母表)}, 符型讠位元偏移量/tuple{uint%len(总字母表)}{len=len(列表纟字母表牜头胞辻多种体胞)}, 符型讠规模纟字母表/tuple{len(列表纟字母表牜头胞辻多种体胞[符型])}{len=len(列表纟字母表牜头胞辻多种体胞)})'
        (位元讠字符, 字符讠位元, 字符讠取反字符) = 求冫总字母表相关信息扌(sf.列表纟字母表牜头胞辻多种体胞, 欤编码无需头胞=sf.欤编码无需头胞, 欤编码呈奇性对称分布=sf.欤编码呈奇性对称分布)
        return (位元讠字符, 字符讠位元, 字符讠取反字符)

    @cached_property
    def 位元讠字符(sf, /):
        '-> 总字母表/位元讠字符/str'
        return sf.总字母表相关信息[0]
    @cached_property
    def 字符讠位元(sf, /):
        '-> 字符讠位元/{char:uint%len(总字母表)}'
        return sf.总字母表相关信息[1]
    @cached_property
    def 字符讠取反字符(sf, /):
        '-> 字符讠取反字符/{字符:字符}'
        return sf.总字母表相关信息[2]
    ##################
    @property
    def 总字母表(sf, /):
        '-> 总字母表/位元讠字符/str'
        return sf.位元讠字符
        return len(sf.总字母表)
    @property
    def 符型讠字母表(sf, /):
        '-> 列表纟字母表牜头胞辻多种体胞/符型讠字母表/[str{len>=1}]{len>=2}'
        return sf.列表纟字母表牜头胞辻多种体胞
    #.@cached_property
    #.@override
    #.def 规模纟总字母表(sf, /):
    #.    '-> uint/len(总字母表)'
    @cached_property
    @override
    def 符型讠规模纟字母表(sf, /):
        '-> 符型讠规模纟字母表/tuple{len(列表纟字母表牜头胞辻多种体胞[符型])}{len=len(列表纟字母表牜头胞辻多种体胞)}'
        符型讠规模纟字母表 = tuple(map(len, sf.符型讠字母表))
        return 符型讠规模纟字母表
    ##################


    ##################
    def 趃字符串巛趃位元串扌(sf, 趃位元串, /):
        '趃位元串(Iter 位元) -> 趃字符串/(Iter 字符)'
        趃字符串 = map(sf.位元讠字符.__getitem__, 趃位元串)
        return 趃字符串
    def 趃字符串讠趃位元串扌(sf, 趃字符串, /):
        '趃字符串/(Iter 字符) -> 趃位元串(Iter 位元)'
        趃位元串 = map(sf.字符讠位元.__getitem__, 趃字符串)
        return 趃位元串
    ##################



    ##################
    def 详解读冫数据巛趃字符串扌(sf, 趃字符串, /):
        '趃字符串/(Iter 字符) -> (数据, 已消耗字符数目, 趃字符串)'
        趃字符串 = iter(趃字符串)
        趃位元串 = sf.趃字符串讠趃位元串扌(趃字符串)
        (数据, 已消耗位元串数目, 趃位元串) = sf.详解读冫数据巛趃位元串扌(趃位元串)
        return (数据, 已消耗字符数目:=已消耗位元串数目, 趃字符串)





    ##################
    def 表述冫数据讠字符串表达扌(sf, 数据, /, *, 欤校验):
        '数据 -> 字符串{总字母表}'
        趃位元串 = sf.表述冫数据讠趃位元串表达扌(数据)
        趃字符串 = sf.趃字符串巛趃位元串扌(趃位元串)
        字符串 = ''.join(趃字符串)
        if 欤校验:
            if not 数据 == (_数据:=sf.解读冫数据巛字符串表达扌(字符串, 欤校验=False)):raise Exception(数据, _数据, 字符串)
        return 字符串

    ##################
    def 解读冫数据巛字符串表达扌(sf, 字符串, 起址=None, 讫址=None, /, *, 欤校验):
        '字符串 -> 起址 -> 讫址 -> 数据'
        #check_type_is(str, 字符串)
        return 解读冫数据巛囜元串表达扌(sf.表述冫数据讠字符串表达扌, sf.详解读冫数据巛趃字符串扌, 字符串, 起址, 讫址, 欤校验=欤校验)
    def 详解读冫数据巛字符串表达扌(sf, 字符串, 起址=None, 讫址=None, /, *, 欤校验):
        '字符串 -> 起址 -> 讫址 -> (数据, 讫址)'
        check_type_is(str, 字符串)
        return 详解读冫数据巛囜元串表达扌(sf.表述冫数据讠字符串表达扌, sf.详解读冫数据巛趃字符串扌, 字符串, 起址, 讫址, 欤校验=欤校验)
    ##################
    ##################
    def encode_dat2txt7lex_order_(sf, dat, /, *, validate=True):
        'dat -> str'
        txt = sf.表述冫数据讠字符串表达扌(dat, 欤校验=validate)
        return txt
    def decode_dat5txt7lex_order_(sf, txt, begin=None, end=None, /, *, validate=True):
        'str -> dat'
        dat = sf.解读冫数据巛字符串表达扌(txt, begin, end, 欤校验=validate)
        return dat
    def xdecode_dat5txt7lex_order_(sf, txt, begin=None, end=None, /, *, validate=True):
        'str -> (dat, end)'
        (dat, end) = sf.详解读冫数据巛字符串表达扌(txt, begin, end, 欤校验=validate)
        return (dat, end)
    def xdecode_dat5iter_chars7lex_order_(sf, chars, /):
        '(Iter char) -> (dat, num_consumed_chars/uint, iter_remain_chars/(Iterator char))'
        (dat, num_consumed_chars, iter_remain_chars) = sf.详解读冫数据巛趃字符串扌(chars)
        return (dat, num_consumed_chars, iter_remain_chars)
    ##################
表述冫数据讠字符串表达扌 = 魖数据字符串表达牜词典序牜前置长度.表述冫数据讠字符串表达扌
解读冫数据巛字符串表达扌 = 魖数据字符串表达牜词典序牜前置长度.解读冫数据巛字符串表达扌
详解读冫数据巛字符串表达扌 = 魖数据字符串表达牜词典序牜前置长度.详解读冫数据巛字符串表达扌
详解读冫数据巛趃字符串扌 = 魖数据字符串表达牜词典序牜前置长度.详解读冫数据巛趃字符串扌
encode_dat2txt7lex_order_ = 魖数据字符串表达牜词典序牜前置长度.encode_dat2txt7lex_order_
decode_dat5txt7lex_order_ = 魖数据字符串表达牜词典序牜前置长度.decode_dat5txt7lex_order_
xdecode_dat5txt7lex_order_ = 魖数据字符串表达牜词典序牜前置长度.xdecode_dat5txt7lex_order_
xdecode_dat5iter_chars7lex_order_ = 魖数据字符串表达牜词典序牜前置长度.xdecode_dat5iter_chars7lex_order_


##################
def 解读冫数据巛囜元串表达扌(表述冫数据讠囜元串表达扌, 详解读冫数据巛趃囜元串扌, 囜元串, 起址, 讫址, /, *, 欤校验):
    '(数据->囜元串) -> (趃囜元串->(数据, 已消耗囜元串数目, 趃囜元串)) -> 囜元串 -> 起址 -> 讫址 -> 数据'
    (起址, 讫址) = 规范冫起讫纟列表扌(len(囜元串), 起址, 讫址)
    (数据, _讫址) = 详解读冫数据巛囜元串表达扌(表述冫数据讠囜元串表达扌, 详解读冫数据巛趃囜元串扌, 囜元串, 起址, 讫址, 欤校验=欤校验)
    #.if not _讫址 == 讫址:raise FormatError(囜元串, 数据, 囜元串[_讫址:min(_讫址+10, 讫址)], _讫址, 讫址)
    if not _讫址 == 讫址:raise FormatError(囜元串[_讫址:min(_讫址+10, 讫址)], _讫址, 讫址)
    return 数据
def 详解读冫数据巛囜元串表达扌(表述冫数据讠囜元串表达扌, 详解读冫数据巛趃囜元串扌, 囜元串, 起址, 讫址, /, *, 欤校验):
    '(数据->囜元串) -> (趃囜元串->(数据, 已消耗囜元串数目, 趃囜元串)) -> 囜元串 -> 起址 -> 讫址 -> (数据, 讫址)'
    (起址, 讫址) = 规范冫起讫纟列表扌(len(囜元串), 起址, 讫址)
    趃囜元串 = 趃子串扌(囜元串, 起址, 讫址)
    (数据, 已消耗囜元串数目, 趃囜元串) = 详解读冫数据巛趃囜元串扌(趃囜元串)
    _讫址 = 起址+已消耗囜元串数目
    if 欤校验:
        if not (_0囜元串:=囜元串[起址:_讫址]) == (_1囜元串:=表述冫数据讠囜元串表达扌(数据, 欤校验=False)):raise Exception(_0囜元串, _1囜元串, 数据)
    return (数据, _讫址)
##################



def 规范冫起讫纟列表扌(长度纟列表, 鬽起址纟列表, 鬽讫址纟列表, /):
    '长度纟列表/uint -> 鬽起址纟列表/(may int) -> 鬽讫址纟列表/(may int) -> (起址, 讫址)/Pair{uint%(1+长度纟列表)}'
    #range(长度纟列表)[鬽起址纟列表:鬽讫址纟列表]
    (起址, 讫址, _1) = slice(鬽起址纟列表, 鬽讫址纟列表, 1).indices(长度纟列表)
    return (起址, 讫址)

def 趃子串扌(列表, 起址=None, 讫址=None, /):
    '列表/[值] -> 起址 -> 讫址 -> 趃子串/(Iter 值)'
    for j in range(len(列表))[起址:讫址]:
        yield 列表[j]


class 乸计耗器:
    def __new__(cls, 趃, /):
        if type(趃) is cls:
            return 趃
        sf = super(__class__, cls).__new__(cls)
        sf._已耗数 = 10
        sf.趃 = iter(趃)
        return sf
    def diff(sf, i, /):
        return sf._已耗数 -i
    def __iter__(sf, /):
        return sf
    def __next__(sf, /):
        x = next(sf.趃)
        sf._已耗数 += 1
        return x

class 魖定型定长前取器(ABC):
    '定型定长前取器{位元{符型}}'
    __slots__ = ()
    @property
    @abstractmethod
    def 已消耗位元数目(sf, /):
        '-> uint'
    @abstractmethod
    def 取反扌(sf, /):
        '-> 魖定型定长前取器'
    @abstractmethod
    def 读取冫位元串牜子表扌(sf, 符型, 数目, /):
        '符型/uint%len(列表纟字母表牜头胞辻多种体胞) -> 数目/uint -> 子表位元串/[位元/uint%len(列表纟字母表牜头胞辻多种体胞[符型])]{len==数目}/(tuple|bytes|WordSeq)|^EOFError'
        #%s/取冫子表位元串巛趃位元串扌/读取冫位元串牜子表扌/g

class 魖定型定长前取器牜造反(魖定型定长前取器):
    __slots__ = ()
    @abstractmethod
    def 罓造反扌(sf, /):
        '-> 魖定型定长前取器'
    @override
    def 取反扌(sf, /):
        try:
            return sf._反
        except AttributeError:
            pass
        sf._反 = sf.罓造反扌()
        777;sf._反._反 = sf
        assert sf.取反扌().取反扌() is sf
        return sf.取反扌()


class 乸定型定长前取器巛趃位元串(魖定型定长前取器牜造反):
    '定型定长前取器{位元{符型}}'
    ___no_slots_ok___ = True
    def __new__(cls, ops, 已消耗位元数目, 趃位元串, /, *, 欤取反=False):
        '[趃位元串 :: Iter 位元]'
        sf = super(__class__, cls).__new__(cls)
        sf._ops = ops
        sf._符型相关信息 = ops.符型相关信息
        #sf.已消耗位元数目 = 已消耗位元数目
        sf.趃位元串 = 乸计耗器(趃位元串)#iter(趃位元串)
        sf._起点 = sf.趃位元串.diff(已消耗位元数目)
        sf.欤取反 = 欤取反
        return sf
    @property
    @override
    def 已消耗位元数目(sf, /):
        return sf.趃位元串.diff(sf._起点)
    @override
    def 罓造反扌(sf, /):
        return 乸定型定长前取器巛趃位元串(sf._ops, sf.已消耗位元数目, sf.趃位元串, 欤取反=not sf.欤取反)
    @override
    def 读取冫位元串牜子表扌(sf, 符型, 数目, /):
        '符型/uint%len(列表纟字母表牜头胞辻多种体胞) -> 数目/uint -> 子表位元串/[位元/uint%len(列表纟字母表牜头胞辻多种体胞[符型])]{len==数目}/(tuple|bytes|WordSeq)|^EOFError'
        (规模纟总字母表, 符型讠位元偏移量, 符型讠规模纟字母表, 位元讠取反位元) = sf._符型相关信息
        位元偏移量 = 符型讠位元偏移量[符型]
        规模纟字母表乊符型 = 符型讠规模纟字母表[符型]
        it = sf.趃位元串
        it = (icheck_([check_uint_lt, 规模纟总字母表], j) for j in it)
        it = map(位元偏移量.__rsub__, it)
        #it = (icheck_int_ge_lt(0, 规模纟字母表乊符型, j) for j in it)
        it = (icheck_([check_uint_lt, 规模纟字母表乊符型], j) for j in it)
        if sf.欤取反:
            it = map((-1+规模纟字母表乊符型).__sub__, it)
        位元串 = sf._ops.位元串巛趃位元串牜子表扌(符型, islice(it, 0, 数目))
        if not len(位元串) == 数目: raise EOFError(数目, len(位元串), 位元串)
        #.sf.已消耗位元数目 += len(位元串)
        #.try:
        #.    sf._反.已消耗位元数目 += len(位元串)
        #.except AttributeError:
        #.    pass
        return 位元串
    ##################
    #.@cached_property
    #.def 规模纟总字母表(sf, /):
    #.    '-> uint/len(总字母表)'
    #.    return sf._符型相关信息[0]
    #.@property
    #.def _位元串巛趃位元串牜合表扌(sf, /):
    #.    '趃位元串 -> 位元串'
    #.    return sf._ops.位元串巛趃位元串牜合表扌
    ##################

class 乸定型定长前取器牜符型偏移(魖定型定长前取器牜造反):
    ___no_slots_ok___ = True
    def __new__(cls, 符型偏移量, 定型定长前取器, /):
        check_int_ge(0, 符型偏移量)
        sf = super(__class__, cls).__new__(cls)
        sf._符型偏移量 = 符型偏移量
        sf._定型定长前取器 = 定型定长前取器
        return sf
    @property
    @override
    def 已消耗位元数目(sf, /):
        return sf._定型定长前取器.已消耗位元数目
    @override
    def 罓造反扌(sf, /):
        return 乸定型定长前取器牜符型偏移(sf._符型偏移量, sf._定型定长前取器.取反扌())
    @override
    def 读取冫位元串牜子表扌(sf, 符型, 数目, /):
        return sf._定型定长前取器.读取冫位元串牜子表扌(符型+sf._符型偏移量, 数目)

class 乸定型定长前取器牜添加头胞(魖定型定长前取器牜造反):
    ___no_slots_ok___ = True
    def __new__(cls, ops, 头胞, 定型定长前取器, /):
        check_int_ge(0, 头胞)
        sf = super(__class__, cls).__new__(cls)
        sf._ops = ops
        sf._头胞 = 头胞
        sf._定型定长前取器 = 定型定长前取器
        return sf
    @property
    def _欤过头(sf, /):
        return sf._头胞 == -1
    @property
    @override
    def 已消耗位元数目(sf, /):
        return sf._定型定长前取器.已消耗位元数目
    @override
    def 罓造反扌(sf, /):
        return 乸定型定长前取器牜添加头胞(sf._ops, sf._头胞, sf._定型定长前取器.取反扌())
    @override
    def 读取冫位元串牜子表扌(sf, 符型, 数目, /):
        if sf._欤过头:
            return sf._定型定长前取器.读取冫位元串牜子表扌(符型, 数目)
        if 数目 == 0:
            return b''
        check_int_ge(1, 数目)
        器 = 乸定型定长前取器巛趃位元串(sf._ops, sf.已消耗位元数目, 趃位元串=iter([sf._头胞]), 欤取反=False)
        串 = sf._定型定长前取器.读取冫位元串牜子表扌(符型, 1)
        assert len(串) == 1
        if 数目 == 1:
            return 串
        return 串 + sf._定型定长前取器.读取冫位元串牜子表扌(符型, 数目-1)








class 魖有理数位元串表达牜词典序牜前置长度(魖数据位元串表达牜词典序牜前置长度):
    __slots__ = ()
    #@override
    欤编码呈奇性对称分布 = True
    @override
    def 检查冫数据扌(sf, 数据, /):
        '数据 -> None'
        #check_type_is(Fraction, 数据)
        check_type_le(Rational, 数据)
        (分子, 分母) = 数据.int.as_integer_ratio()

class 魖整数位元串表达牜词典序牜前置长度(魖数据位元串表达牜词典序牜前置长度):
    __slots__ = ()
    #@override
    欤编码无需头胞 = False
    #@override
    欤编码呈奇性对称分布 = True
    @override
    def 检查冫数据扌(sf, 数据, /):
        '数据 -> None'
        check_type_is(int, 数据)

class 魖自然数位元串表达牜词典序牜前置长度(魖数据位元串表达牜词典序牜前置长度):
    __slots__ = ()
    #@override
    欤编码呈奇性对称分布 = False
    @override
    def 检查冫数据扌(sf, 数据, /):
        '数据 -> None'
        check_int_ge(0, 数据)









class 魖整数位元串表达牜词典序牜前置长度牜整数零编码为单胞(魖整数位元串表达牜词典序牜前置长度):
    __slots__ = ()
    #欤整数零编码为单胞
    @abstractmethod
    def 罓解读冫正整数巛定型定长前取器扌(sf, 删负偏移后头胞纟正整数编码, 定型定长前取器, /):
        '删负偏移后头胞纟正整数编码/uint{>0} -> (魖定型定长前取器|魖定型定长前取器牜取反){位元{符型}} -> 正整数'
    @abstractmethod
    def 罓表述冫正整数讠趃序列纟带符型位元串扌(sf, 正整数, /):
        '正整数 -> 趃序列纟带符型位元串/(Iter 带符型位元串/(符型/uint%len(符型讠规模纟字母表), 位元串牜子表/[位元{符型}]/(tuple|bytes|WordSeq)))'

    @cached_property
    def 头胞纟零编码牜子表(sf, /):
        '-> uint'
        头胞纟零编码牜子表 = (规模纟字母表牜头胞:=sf.符型讠规模纟字母表[0])//2
        assert 1+2*头胞纟零编码牜子表 == 规模纟字母表牜头胞
        return 头胞纟零编码牜子表
    @cached_property
    def 头胞纟零编码牜合表(sf, /):
        '-> uint'
        头胞纟零编码牜合表 = sf.头胞纟零编码牜子表 +sf.符型讠位元偏移量[0]
        return 头胞纟零编码牜合表

    @override
    def 罓表述冫数据讠趃序列纟带符型位元串扌(sf, 数据, /):
        整数 = 数据
        if 整数 == 0:
            符型 = 0
            位元串牜子表 = sf.位元串巛趃位元串牜子表扌(符型, [sf.头胞纟零编码牜子表])
            趃序列纟带符型位元串 = iter([(符型, 位元串牜子表)])
            return 趃序列纟带符型位元串
        正整数 = abs(整数)
        趃序列纟带符型位元串 = sf.罓表述冫正整数讠趃序列纟带符型位元串扌(正整数)
        if 整数 < 0:
            趃序列纟带符型位元串 = sf.取反冫趃序列纟带符型位元串扌(趃序列纟带符型位元串)
        return 趃序列纟带符型位元串
    @override
    def 罓解读冫数据巛定型定长前取器扌(sf, 定型定长前取器, /):
        '魖定型定长前取器{位元{符型}} -> 数据'
        [头胞纟整数编码] = 定型定长前取器.读取冫位元串牜子表扌(符型:=0, 数目:=1)
        差值 = 头胞纟整数编码 -sf.头胞纟零编码牜子表
        if 差值 == 0:
            return 0
        if 差值 < 0:
            #负数
            #头胞纟绝对值编码 = sf.头胞纟零编码牜子表 -差值
            删负偏移后头胞纟正整数编码 = -差值
            定型定长前取器牜正整数 = 定型定长前取器.取反扌()
        else:
            删负偏移后头胞纟正整数编码 = +差值
            定型定长前取器牜正整数 = 定型定长前取器
        正整数 = sf.罓解读冫正整数巛定型定长前取器扌(删负偏移后头胞纟正整数编码, 定型定长前取器牜正整数)
        整数 = -正整数 if 差值 < 0 else 正整数
        数据 = 整数
        return 数据




class 魖整数位元串表达牜词典序牜前置长度牜整数零编码为单胞牜使用自然数编码器(魖整数位元串表达牜词典序牜前置长度牜整数零编码为单胞):
    __slots__ = ()
    @property
    @abstractmethod
    def 匴自然数位元串表达牜词典序牜前置长度(sf, /):
        '-> 魖自然数位元串表达牜词典序牜前置长度'
    @property
    @abstractmethod
    def 规模纟头胞(sf, /):
        '-> uint'
    @property
    @abstractmethod
    def 欤深一(sf, /):
        '-> bool'

    @cached_property
    @override
    def 符型讠规模纟字母表(sf, /):
        匴 = sf.匴自然数位元串表达牜词典序牜前置长度
        欤深一 = sf.欤深一
        规模纟头胞 = sf.规模纟头胞
        check_int_ge(3, 规模纟头胞)
        if not 1 == 规模纟头胞&1:raise TypeError
        规模纟头胞纟自然数 = 匴.符型讠规模纟字母表[0]
        check_int_ge(1, 规模纟头胞纟自然数)
        if not (欤深一 or 规模纟头胞 == 1+2*规模纟头胞纟自然数):raise TypeError
        if 欤深一:
            符型讠规模纟字母表 = (规模纟头胞, *匴.符型讠规模纟字母表)
        else:
            assert 规模纟头胞 == 1+2*规模纟头胞纟自然数
            符型讠规模纟字母表 = (规模纟头胞, *匴.符型讠规模纟字母表[1:])
        符型讠规模纟字母表
        return 符型讠规模纟字母表
    @override
    def 罓解读冫正整数巛定型定长前取器扌(sf, 删负偏移后头胞纟正整数编码, 定型定长前取器, /):
        匴 = sf.匴自然数位元串表达牜词典序牜前置长度
        欤深一 = sf.欤深一
        规模纟头胞 = sf.规模纟头胞
        check_int_ge(1, 删负偏移后头胞纟正整数编码)
        if 欤深一:
            if not 1 == 删负偏移后头胞纟正整数编码:raise TypeError(sf, 删负偏移后头胞纟正整数编码)
            777;del 删负偏移后头胞纟正整数编码
            定型定长前取器 = 乸定型定长前取器牜符型偏移(1, 定型定长前取器)
        #elif 1 == 删负偏移后头胞纟正整数编码: del 删负偏移后头胞纟正整数编码
        else:
            定型定长前取器 = 乸定型定长前取器牜添加头胞(匴, 删负偏移后头胞纟正整数编码, 定型定长前取器)
        定型定长前取器
        return 匴.罓解读冫数据巛定型定长前取器扌(定型定长前取器)
    @override
    def 罓表述冫正整数讠趃序列纟带符型位元串扌(sf, 正整数, /):
        匴 = sf.匴自然数位元串表达牜词典序牜前置长度
        欤深一 = sf.欤深一
        趃序列纟带符型位元串 = 匴.罓表述冫数据讠趃序列纟带符型位元串扌(正整数)
        if 欤深一:
            #bug:趃序列纟带符型位元串 = chain([(0, 1)], ((1+符型, 位元串牜子表) for 符型, 位元串牜子表 in 趃序列纟带符型位元串))
            串一牜子表 = sf.位元串巛趃位元串牜子表扌(0, [1+sf.头胞纟零编码牜子表])
            趃序列纟带符型位元串 = chain([(0, 串一牜子表)], ((1+符型, 位元串牜子表) for 符型, 位元串牜子表 in 趃序列纟带符型位元串))
        return 趃序列纟带符型位元串





class 乸整数位元串表达牜词典序牜前置长度牜整数零编码为单胞牜使用自然数编码器(魖整数位元串表达牜词典序牜前置长度牜整数零编码为单胞牜使用自然数编码器):
    ___no_slots_ok___ = True
    def __init__(sf, 欤深一, 规模纟头胞, 匴自然数位元串表达牜词典序牜前置长度, /):
        check_type_is(bool, 欤深一)
        check_int_ge(3, 规模纟头胞)
        if not 1 == 规模纟头胞&1:raise TypeError

        check_type_le(魖自然数位元串表达牜词典序牜前置长度, 匴自然数位元串表达牜词典序牜前置长度)
        sf._b1 = 欤深一
        sf._R0 = 规模纟头胞
        sf._ops = 匴自然数位元串表达牜词典序牜前置长度
    @property
    @override
    def 匴自然数位元串表达牜词典序牜前置长度(sf, /):
        return sf._ops
    @property
    @override
    def 规模纟头胞(sf, /):
        return sf._R0
    @property
    @override
    def 欤深一(sf, /):
        return sf._b1

check_non_ABC(乸整数位元串表达牜词典序牜前置长度牜整数零编码为单胞牜使用自然数编码器)


class 魖数据字符串表达牜词典序牜前置长度牜使用匴数据位元串表达(魖数据字符串表达牜词典序牜前置长度):
    __slots__ = ()
    @property
    @abstractmethod
    def 匴数据位元串表达(sf, /):
        '-> 魖数据位元串表达牜词典序牜前置长度'
    ##################
    #.@property
    #.@abstractmethod
    #.def 列表纟字母表牜头胞辻多种体胞(sf, /):
    ##################
    @property
    @override
    def 欤编码无需头胞(sf, /):
        return sf.匴数据位元串表达.欤编码无需头胞
    @property
    @override
    def 欤编码呈奇性对称分布(sf, /):
        return sf.匴数据位元串表达.欤编码呈奇性对称分布
    @cached_property
    @override
    def 符型讠规模纟字母表(sf, /):
        符型讠规模纟字母表 = sf.匴数据位元串表达.符型讠规模纟字母表
        列表纟字母表牜头胞辻多种体胞 = sf.列表纟字母表牜头胞辻多种体胞
        if not tuple(map(len, 列表纟字母表牜头胞辻多种体胞)) == 符型讠规模纟字母表:raise TypeError
        return 符型讠规模纟字母表
    ##################

    @override
    def 罓表述冫数据讠趃序列纟带符型位元串扌(sf, 数据, /):
        return sf.匴数据位元串表达.罓表述冫数据讠趃序列纟带符型位元串扌(数据)
    @override
    def 罓解读冫数据巛定型定长前取器扌(sf, 定型定长前取器, /):
        return sf.匴数据位元串表达.罓解读冫数据巛定型定长前取器扌(定型定长前取器)
    @override
    def 检查冫数据扌(sf, 数据, /):
        return sf.匴数据位元串表达.检查冫数据扌(数据)

class 乸数据字符串表达牜词典序牜前置长度牜使用匴数据位元串表达(魖数据字符串表达牜词典序牜前置长度牜使用匴数据位元串表达):
    ___no_slots_ok___ = True
    def __init__(sf, 匴数据位元串表达, 列表纟字母表牜头胞辻多种体胞, /):
        check_type_le(魖数据位元串表达牜词典序牜前置长度, 匴数据位元串表达)
        列表纟字母表牜头胞辻多种体胞 = tuple(列表纟字母表牜头胞辻多种体胞)
        check_all_([check_type_is, str], 列表纟字母表牜头胞辻多种体胞)

        sf._ops = 匴数据位元串表达
        sf._j2cs = 列表纟字母表牜头胞辻多种体胞
    ##################
    @property
    @override
    def 匴数据位元串表达(sf, /):
        return sf._ops
    @property
    @override
    def 列表纟字母表牜头胞辻多种体胞(sf, /):
        return sf._j2cs
    ##################
check_non_ABC(乸数据字符串表达牜词典序牜前置长度牜使用匴数据位元串表达)


__all__
from seed.int_tools.int_repr7lex_order7base import FormatError
from seed.int_tools.int_repr7lex_order7base import 魖数据位元串表达牜词典序牜前置长度, 魖数据字符串表达牜词典序牜前置长度,魖有理数位元串表达牜词典序牜前置长度,魖整数位元串表达牜词典序牜前置长度,魖自然数位元串表达牜词典序牜前置长度
from seed.int_tools.int_repr7lex_order7base import 魖整数位元串表达牜词典序牜前置长度牜整数零编码为单胞, 乸整数位元串表达牜词典序牜前置长度牜整数零编码为单胞牜使用自然数编码器
from seed.int_tools.int_repr7lex_order7base import 魖数据字符串表达牜词典序牜前置长度牜使用匴数据位元串表达, 乸数据字符串表达牜词典序牜前置长度牜使用匴数据位元串表达

from seed.int_tools.int_repr7lex_order7base import 表述冫数据讠位元串表达扌, 解读冫数据巛位元串表达扌, 详解读冫数据巛位元串表达扌, 详解读冫数据巛趃位元串扌
from seed.int_tools.int_repr7lex_order7base import encode_dat2digit_seq7lex_order_, decode_dat5digit_seq7lex_order_, xdecode_dat5digit_seq7lex_order_, xdecode_dat5iter_digits7lex_order_

from seed.int_tools.int_repr7lex_order7base import 表述冫数据讠字符串表达扌, 解读冫数据巛字符串表达扌, 详解读冫数据巛字符串表达扌, 详解读冫数据巛趃字符串扌
from seed.int_tools.int_repr7lex_order7base import encode_dat2txt7lex_order_, decode_dat5txt7lex_order_, xdecode_dat5txt7lex_order_, xdecode_dat5iter_chars7lex_order_


if 1:from seed.int_tools.int_repr7lex_order7base import _魖共通
from seed.int_tools.int_repr7lex_order7base import *
