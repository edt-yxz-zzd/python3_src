#__all__:goto
#######
#注意:命令行、文档:已分离到另一文件
#   view ../../python3_src/seed/math/power/addition_chain/shortest/mixed_recursive_greedy_zpow_addition_chain__doc__py_adhoc_call.py
#######
#注意:本文件的简并集:并非 所有最短加链的简并，而是 所有婪溟链牜递归最短的简并
#   正如:前一版的简并集 仅指 所有加星链牜递归最短的简并:所以12509成了前一版的首败点
#######
#注意:尾六表各表名不符实
#   eg:最短加链牜左侧最大-->理应更名为:婪溟链牜递归最短牜左侧最大
#######
#注意:last_leap:最后一跃版:是 残损版、不完整简并版#欤最后一跃牜轻算随缘而止
#   此时尾六表各表更加名不符实{只能说提供了些婪溟链牜递归最短，但不极端，下上界也失去意义}
#   意图:只是尝试一下能否更快得到更多后续最短加链
#######
#注意:虽然[加星链<:婪溟链][加星链牜递归最短<:婪溟链牜递归最短<:最短加链]，但是[婪溟链牜递归最短 与 加星链牜最短 之间 并无特别关系:309,12509]
#   12509:没有加星链，但有 婪溟链牜递归最短
#   309:数据证据见于:_校验冫兼容性纟替代方案扌()@view ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__the_max_one.py
#       (加星链牜最短牜左侧最大:(1, 2, 4, 8, 16, 32, 48, 49, 98, 130, 260, 309), 婪溟链牜递归最短牜左侧最大:(1, 2, 4, 8, 16, 32, 36, 68, 136, 272, 308, 309))
#######
#######
#TODO:sorted(次大数讠溟次.items(), reverse=???)@_f2()@{+欤最后一跃牜轻算随缘而止,[+-]欤只保留首条最短加链乊各次大数}:_过滤乊内点集扌/枚举冫最短加链乊内点集扌
#TODO:失误？:尾六表/尾六表牜最短加链版-->尾六表牜主线版，或者 同时 并存，再添上 主干值简并态，格式新增:dnzw_str as ver4
#TODO:简并记录、失败记录 合二为一:++欤真最小显链长
#TODO:简并记录:精深版-->深一版-->只保留:次大数讠溟次 {加载时计算简并态{允许非法点:并集{次大数.简并态}}{此前尝试简化是通过削减残损精深版简并态，禁止非法点}}，新增:次大数讠主线牜右侧最大、次大数讠主线牜右侧最小
#######
r'''[[[
e ../../python3_src/seed/math/power/addition_chain/shortest/mixed_recursive_greedy_zpow_addition_chain.py
    简并态{递归婪溟链}
doc:
    view ../../python3_src/seed/math/power/addition_chain/shortest/mixed_recursive_greedy_zpow_addition_chain__doc__py_adhoc_call.py
old:
    view script/min_add_ver5__mixed_recursive_greedy_zpow_addition_chain.py
view ../../python3_src/seed/recognize/text_recognizer/ITextRecognizer.py



%s/script[.]min_add_ver5__mixed_recursive_greedy_zpow_addition_chain/seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain

seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain
py -m nn_ns.app.debug_cmd   seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain:__doc__ -ht # -ff -df


]]]'''#'''
from seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain__doc__py_adhoc_call import __doc__ as _doc
777;__doc__ += '\n' + _doc
__all__ = r'''
枚举生成冫文件后续简并记录纟递归婪溟链扌
    加载冫数据扌
        构造冫局部变量环境纟解读简并记录扌

    枚举冫后续简并记录纟递归婪溟链牜自顶向下搜索扌
        求冫后续简并记录纟递归婪溟链牜自顶向下搜索扌
            构造冫简并记录纟靶值一扌
        枚举冫最短加链乊内点集扌
            枚举冫首条最短加链乊各次大数扌

    枚举冫后续简并记录纟递归婪溟链牜自底向上注册扌
        求冫后续简并记录纟递归婪溟链牜自底向上注册扌
            后续更新冫靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈乊已有后续简并记录纟递归婪溟链牜靶值大于一扌
        初始化构造冫靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈乊后续简并记录纟递归婪溟链牜靶值大于一扌

乸失败记录
乸简并记录纟递归婪溟链
    表述冫简并集讠文本表达扌
    表述冫次大数讠溟次讠文本表达扌

MAX_VERSION
转换冫文件格式纟简并记录纟递归婪溟链扌
转换冫文件格式纟简并记录纟递归婪溟链灬扌
转换冫尾六表纟简并记录纟递归婪溟链扌
另档冫尾六表纟简并记录纟递归婪溟链扌
另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌
    另档冫递归婪溟链暨最短加链牜某尾四表讠址距溟次形式扌
        另档冫递归婪溟链暨最短加链牜左侧最小讠址距溟次形式扌
        另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌
        另档冫递归婪溟链暨最短加链牜右侧最小讠址距溟次形式扌
        另档冫递归婪溟链暨最短加链牜右侧最大讠址距溟次形式扌
求冫丮最小比率辻靶值列表厈牜长度纟头部二幂纟左侧最大最短加链之于最小显链长纟靶值扌
求冫丮最大比率辻靶值列表厈牜次大数纟右侧最小最短加链之于靶值扌
求冫丮最大差值辻靶值列表厈牜两倍次大数纟右侧最小最短加链之于靶值扌
最大化乊已有简并记录冫最小化乊尾四链冫最大内点址距乊加链扌


乸异常牜最小显链长

乸异常牜最大靶值
规范冫列表纟文件路径冃靶值讠简并记录扌
reverse_
DELETED
'''.split()#'''
    #另档冫极简次大数集纟简并记录纟递归婪溟链扌
    #另档冫幸存次大数必由集纟简并记录纟递归婪溟链扌
    #另档冫双点易来简并态纟简并记录纟递归婪溟链扌
    #另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌

__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
#.from functools import cached_property
#see:dot_#from seed.func_tools.dot2 import dot
#.
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.filesys.check_paths_exist import check_paths_exist
    #.def check_paths_exist(paths, *, all_files=False, all_folders=False):

    from seed.tiny_.funcs import echo, fst, snd
    from seed.iters.chains import chains
    from itertools import pairwise, accumulate # islice
    #.from time import sleep, process_time, thread_time
    from seed.for_libs.for_time import sleep9KeyboardInterrupt_, resting9KeyboardInterrupt_, mk_rest_func_

    from seed.debug.print_err import print_err
    from seed.math.power.addition_chain.common.check import 检查冫严序加链乊靶值扌, 检查冫严序加链扌, 检查冫严序加链内容扌
    from seed.tiny_.check import check_type_in, check_type_is, check_int_ge, check_int_ge_le, check_may_
    from nn_ns.math_nn.numbers.shortest_addition_chain_length__ver3 import 靶值讠最小显链长扌 #取冫靶值讠最小显链长扌
    from seed.helper.stable_repr import stable_repr
    from seed.types.FrozenDict import mk_FrozenDict
    from seed.tiny_.containers import mk_tuple
    from seed.data_funcs.rngs import make_NonTouchRanges, sorted_ints_to_iter_nontouch_ranges
    from seed.data_funcs.rngs import ranges2hex2sz, ranges5hex2sz
        # [ver:=1]
    from seed.data_funcs.rngs import ranges2delta_txt_, ranges5delta_txt_, uint2base64_, uint5base64_
        # [ver:=2]
    from seed.mapping_tools.dict_op import inv__k2v_to_v2ks
    #.def inv__group_keys_by_value__immutable(k2v, ks=None, /, *, set_vs_list=False):
    #.    'Map k v -> Map v (Set k) #see also: seed.tiny_.dict__add_fmap_filter.group4dict_value'
    from seed.for_libs.for_collections.override_repr4namedtuple import mk_namedtuple_, mk_namedtuple__check6make_
    #[mk_namedtuple_,mk_namedtuple__check6make_] = lazy_import4funcs_('seed.for_libs.for_collections.override_repr4namedtuple', 'mk_namedtuple_,mk_namedtuple__check6make_', __name__)
    #def mk_namedtuple_(__module__, nm, nms_or_str, /, *args, **kwds):
    #def mk_namedtuple__check6make_(__module__, nm, nms_or_str, /, *args, **kwds):
    #    def _check6make_(sf, /):


    #########
    #.from seed.data_funcs.rngs import make_Ranges, sorted_rngs_to_iter_nontouch_ranges, sorted_ints_to_iter_nontouch_ranges, detect_iter_ranges, StackStyleSimpleIntSet, StackStyleSimpleIntMapping, TouchRangeBasedIntMapping
        #TouchRangeBasedIntMapping.from_value2begin2sz/.from_rng_value_pairs/.from_clone_of_rngs_with_default
    #.from seed.data_funcs.rngs import IRanges
        #for:.from_hexXhexszpair_list/.from_hex_repr_pair_list/.from_len_rng2hexbegins/.from_len_rng2begin_chars/.from_char_pairs__str/.from_wave_rngtxt/.from_hex_sz_pair_list/.from_hex2sz
        #for:.from_touch_rngs/.from_sorted_rngs/.from_unsorted_rngs/.from_sorted_ints/.from_unsorted_ints/.from_sorted_chars/.from_unsorted_chars
    #.from seed.data_funcs.rngs import NonTouchRanges, TouchRanges, make_NonTouchRanges, make_TouchRanges
    #.from seed.data_funcs.rngs import len_of__rng, len_of__rng__neg_as0
    #########
    #########



#.#################################
___end_mark_of_excluded_global_names__0___ = ...


__all__


def reverse_(xs, /):
    return xs[::-1]

######################
#copy_from:view script/min_add_ver4__pseudo_addition_chain.py
#   _mkrs4rngs_()
######################
def _mkrs4rngs_():
    global _mkrs4rngs_
    old = _mkrs4rngs_
    ######################
    from seed.data_funcs.rngs import make_Ranges, sorted_rngs_to_iter_nontouch_ranges, sorted_ints_to_iter_nontouch_ranges, detect_iter_ranges, StackStyleSimpleIntSet, StackStyleSimpleIntMapping, TouchRangeBasedIntMapping
        #TouchRangeBasedIntMapping.from_value2begin2sz/.from_rng_value_pairs/.from_clone_of_rngs_with_default
    from seed.data_funcs.rngs import IRanges
        #for:.from_hexXhexszpair_list/.from_hex_repr_pair_list/.from_len_rng2hexbegins/.from_len_rng2begin_chars/.from_char_pairs__str/.from_hex_sz_pair_list/.from_hex2sz
        #for:.from_touch_rngs/.from_sorted_rngs/.from_unsorted_rngs/.from_sorted_ints/.from_unsorted_ints/.from_sorted_chars/.from_unsorted_chars
    from seed.data_funcs.rngs import NonTouchRanges, TouchRanges, make_NonTouchRanges, make_TouchRanges
    ######################
    from seed.helper.repr_input import repr_helper
    from seed.helper.stable_repr import stable_repr
    class RT:
        def __init__(sf, ranges, ):
            check_type_is(NonTouchRanges, ranges)
            sf._rs = ranges
        def __repr__(sf, /):
            s = stable_repr({int(u):sz for u, sz in sf._rs.to_hex_sz_pair_list()})
                #from_hex2sz
                #from_hex_sz_pair_list
            return f'RT({s})'
            return repr_helper(sf, sf._rs.ranges)
    ######################
    Mk = IRanges.from_sorted_ints
    _mkrs4rngs = (Mk, NonTouchRanges, RT)
    def _mkrs4rngs_():
        return _mkrs4rngs
    new = _mkrs4rngs_
    assert not new is old
    return _mkrs4rngs_()
######################

class 乸异常牜最大靶值(Exception):pass
#.class 乸异常牜最小显链长(Exception):
#.    def __new__(cls, 病简并记录, 最小显链长, /):
#.        check_type_is(乸简并记录纟递归婪溟链, 病简并记录)
#.        check_int_ge(0, 最小显链长)
#.        args = (病简并记录, 最小显链长)
#.        sf = super(__class__, cls).__new__(cls, *args)
#.        #assert sf.args == (病简并记录, 最小显链长)
#.        return sf
#.def _test乸异常牜最小显链长():
#.    args = (构造冫简并记录纟靶值一扌(), 0)
#.    (病简并记录, 最小显链长) = 乸异常牜最小显链长(*args).args
#.    assert (病简并记录, 最小显链长) == args
#.class 乸失败记录(tuple):
#.    def __new__(cls, /, *args):
#.        sf = tuple.__new__(cls, args)
#.        return sf
#.    def __repr__(sf, /):
#.        args = tuple(sf)
#.        if len(args) == 1:
#.            [x] = args
#.            s = f'乸失败记录({x})'
#.        else:
#.            s = f'乸失败记录{args}'
#.        s
#.        return s
#.def _test乸失败记录():
#.    assert 乸失败记录(666) == (666,)
#.    assert 乸失败记录(666, 999) == (666, 999)
#.    assert '乸失败记录(666, 999)' == repr(乸失败记录(666, 999))
#.    assert '乸失败记录(666)' == repr(乸失败记录(666))
#.    assert 乸失败记录(666, 999) == eval(repr(乸失败记录(666, 999)))
#.    assert 乸失败记录(666) == eval(repr(乸失败记录(666)))
class 乸异常牜最小显链长(Exception):
    def __new__(cls, 失败记录, /):
        check_type_is(乸失败记录, 失败记录)
        sf = super(__class__, cls).__new__(cls, 失败记录)
        if 0:
            #assert sf.args == (失败记录,)
            [_失败记录] = sf.args
            assert _失败记录 is 失败记录
        sf._失败记录 = 失败记录
        return sf
    @property
    def 失败记录(sf, /):
        return sf._失败记录
_乸失败记录 = mk_namedtuple__check6make_(__name__, '_乸简并记录纟递归婪溟链', '病简并记录  真最小显链长')
class 乸失败记录(_乸失败记录):
    def _check6make_(sf, /):
        check_type_is(乸简并记录纟递归婪溟链, sf.病简并记录)
        check_int_ge(0, sf.真最小显链长)
        check_int_ge(1+sf.真最小显链长, sf.病简并记录.最小显链长)
    def to_str(sf, /, *, ver):
        check_int_ge_le(1, MAX_VERSION, ver)
        match sf:
            case 乸失败记录(病简并记录=病简并记录, 真最小显链长=真最小显链长):
                pass
            case _:
                raise 000

        #old:失败记录 = 乸失败记录('fail:', 病简并记录.靶值, 病简并记录.最小显链长, 病简并记录.to_str(ver=ver), 最小显链长)
        t = ('fail:', 病简并记录.靶值, 病简并记录.最小显链长, 病简并记录.to_str(ver=ver), 真最小显链长)
        return str(t)
#.class RT:
#.    '简并集'
#.    def __init__(sf, rngs, /):
#.        check_type_is(NonTouchRanges, rngs)
#.        sf._rngs = rngs
#.    @property
#.    def 简并集(sf, /):
#.        return sf._rngs
#.    def __repr__(sf, /):
_乸简并记录纟递归婪溟链 = mk_namedtuple__check6make_(__name__, '_乸简并记录纟递归婪溟链', '靶值  最小显链长 规模纟次大数集  规模纟简并集 次大数讠溟次  简并集     最短加链位置讠下界   最短加链位置讠上界    最短加链牜左侧最小 最短加链牜左侧最大 最短加链牜右侧最小 最短加链牜右侧最大')
    #RT(简并集)
class 乸简并记录纟递归婪溟链(_乸简并记录纟递归婪溟链):
    def _check6make_(sf, /):
        #check_type_is(NonTouchRanges, sf.简并集)
        sf.简并集.to_hex_sz_pair_list
        sf.次大数讠溟次.items
        check_int_ge(1, sf.靶值)
        check_int_ge(0, sf.最小显链长)
        L = 1+sf.最小显链长
        check_int_ge(0, sf.规模纟次大数集)
        check_int_ge(L, sf.规模纟简并集)
        assert sf.规模纟次大数集 == len(sf.次大数讠溟次)
        assert sf.规模纟简并集 == sf.简并集.len_ints()

        for x in sf[-6:]:
            check_type_is(tuple, x)
            assert len(x) == L
            assert x[-1] == sf.靶值
        for x in sf[-4:]:
            检查冫严序加链乊靶值扌(sf.靶值, x)


        左右小大 = (sf.最短加链牜左侧最小, sf.最短加链牜左侧最大, sf.最短加链牜右侧最小, sf.最短加链牜右侧最大)
        assert 左右小大 == sf[-4:]
        assert sf.最短加链牜左侧最小 == min(左右小大)
        assert sf.最短加链牜左侧最大 == max(左右小大)
        assert sf.最短加链牜右侧最小 == min(左右小大, key=reverse_)
        assert sf.最短加链牜右侧最大 == max(左右小大, key=reverse_)

        assert sf.最短加链位置讠下界 <= sf.最短加链位置讠上界

        if not (_最小显链长:=靶值讠最小显链长扌(sf.靶值)) == sf.最小显链长:
            #.raise 乸异常牜最小显链长(病简并记录:=sf, _最小显链长)#AssertionError
            raise 乸异常牜最小显链长(乸失败记录(病简并记录:=sf, _最小显链长))
    #def __str__(sf, /):
    def to_str(sf, /, *, ver):
        check_int_ge_le(1, MAX_VERSION, ver)
        match sf:
            case 乸简并记录纟递归婪溟链(靶值=靶值, 最小显链长=最小显链长, 规模纟次大数集=规模纟次大数集, 规模纟简并集=规模纟简并集, 次大数讠溟次=次大数讠溟次, 简并集=简并集, 最短加链位置讠下界=最短加链位置讠下界, 最短加链位置讠上界=最短加链位置讠上界, 最短加链牜左侧最小=最短加链牜左侧最小, 最短加链牜左侧最大=最短加链牜左侧最大, 最短加链牜右侧最小=最短加链牜右侧最小, 最短加链牜右侧最大=最短加链牜右侧最大):
                pass
            case _:
                raise 000

        def _0():
            yield 靶值
            yield 最小显链长
            yield 规模纟次大数集
            yield 规模纟简并集
            yield 表述冫次大数讠溟次讠文本表达扌(次大数讠溟次, ver=ver)
            yield 表述冫简并集讠文本表达扌(简并集, ver=ver)
            yield from _1(ver, _2())
        def _1(ver, uss, /):
            match ver:
                case 1 | 2:
                    yield from uss
                case 3:
                    yield _ver3__repr7uss_(uss)
                case bad:
                    raise Exception(ver)
        def _2():
            yield list(最短加链位置讠下界)
            yield list(最短加链位置讠上界)
            yield list(最短加链牜左侧最小)
            yield list(最短加链牜左侧最大)
            yield list(最短加链牜右侧最小)
            yield list(最短加链牜右侧最大)
        s = ', '.join(map(str, _0()))
        s = f'({s})'
        return s

MAX_VERSION = 3
    # check_int_ge_le
    # 构造冫局部变量环境纟解读简并记录扌()
    # 乸简并记录纟递归婪溟链.to_str(ver=ver)

def _ver3__eval7uss_(s8uss, /):
    ss = s8uss.split(';')
    if not len(ss) == 7:raise TypeError(s8uss)
    [j2u, *jss] = ([*ranges5delta_txt_(s).iter_ints()] for s in ss)
    uss = [[j2u[j] for j in js] for js in jss]
    if not len(uss) == 6:raise 000
    return uss
def _ver3__str7uss_(uss, /):
    uss = [*uss]
    if not len(uss) == 6:raise TypeError(uss)
    j2u = sorted(set(chains(uss)))
    u2j = {u:j for j, u in enumerate(j2u)}
    ss = []
    if 1:
        s8j2u = ranges2delta_txt_(_转换集合扌(j2u), validate=True)
        ss.append(s8j2u)
    for us in uss:
        js = [u2j[u] for u in us]
        s8js = ranges2delta_txt_(_转换集合扌(js), validate=True)
        ss.append(s8js)
    if not len(ss) == 7:raise Exception(uss)
    s8uss = ';'.join(ss)
    if not uss == (_uss:=_ver3__eval7uss_(s8uss)):raise Exception(uss, _uss, s8uss)
    return s8uss
def _ver3__repr7uss_(uss, /):
    s8uss = _ver3__str7uss_(uss)
    s = f'*UJ({s8uss!r})'
    return s
def _UJ6ver3_(txt, /):
    return _ver3__eval7uss_(txt)

def _FD6ver2_(txt, /):
    return mk_FrozenDict(_解读冫次大数讠溟次巛文本表达扌(txt))
def _解读冫次大数讠溟次巛文本表达扌(txt, /):
    'view ../../python3_src/seed/recognize/text_recognizer/ITextRecognizer.py'
    if not txt: raise Exception('bad format')
    if not txt[0] == '{': raise Exception('bad format')
    if not txt[-1] == '}': raise Exception('bad format')
    if txt == '{}':
        return {}
    ss = txt[1:-1].split(';')
    if not '' == ss[-1]: raise Exception('bad format')
    ss.pop()
    d = {}
    for s in ss:
        sk, sv = s.split(':', 1)
        溟次 = uint5base64_(sk)
        #.ssv = sv.split(',')
        #.差分表 = map(uint5base64_, ssv)
        #.次大数列表 = list(accumulate(差分表))
        #.assert len(次大数列表) == len(ssv)
        次大数列表 = list(ranges5delta_txt_(sv).iter_ints())
        sz = len(d)
        d.update((次大数, 溟次) for 次大数 in 次大数列表)
        assert sz + len(次大数列表) == len(d), (txt, sz, d, 次大数列表)
    d
    次大数讠溟次 = d
    return 次大数讠溟次
def _表述冫次大数讠溟次讠文本表达扌(次大数讠溟次, /):
    #次大数讠溟次 = dict(次大数讠溟次)
    check_type_is(dict, 次大数讠溟次)
    def __():
        溟次讠次大数列表 = inv__k2v_to_v2ks(次大数讠溟次, sorted(次大数讠溟次), set_vs_list=True)
        yield '{'
        for 溟次, 次大数列表 in sorted(溟次讠次大数列表.items()):
            yield uint2base64_(溟次)
            yield ':'
            #.yield ','.join(map(uint2base64_, _差分扌(次大数列表)))
            yield make_NonTouchRanges(sorted_ints_to_iter_nontouch_ranges(次大数列表)).to_delta_txt(validate=True)
            yield ';'
        yield '}'
    txt = ''.join(__())
    assert 次大数讠溟次 == (__:=_解读冫次大数讠溟次巛文本表达扌(txt)), (次大数讠溟次, txt, __)
    return txt
def _差分扌(us, /):
    us = list(us)
    差分表 = list(_0差分扌(us))
    _us = list(accumulate(差分表))
    assert us == _us, (us, _us)
    return 差分表
def _0差分扌(us, /):
    assert len(us)
    u = us[0]
    assert u >= 0
    yield u
    for u, v in pairwise(us):
        d = v - u
        assert d >= 0
        yield d
#_表述冫次大数讠溟次讠文本表达扌({36: 2, 82: 0, 84: 0, 92: 0, 98: 0, 100: 0, 132: 0, 144: 0, 160: 0})
def 表述冫次大数讠溟次讠文本表达扌(次大数讠溟次, /, *, ver):
    match ver:
        case 1:
            s = stable_repr(dict(次大数讠溟次))
        case 2 | 3:
            s = _表述冫次大数讠溟次讠文本表达扌(dict(次大数讠溟次))
            s = repr(s)
        case _:
            raise Exception('unknown ver', ver)
        #case
    s
    s = f'FD({s})'
    return s
def 表述冫简并集讠文本表达扌(简并集, /, *, ver):
    match ver:
        case 1:
            s = stable_repr({int(u):sz for u, sz in 简并集.to_hex_sz_pair_list()})
        case 2 | 3:
            #s = 简并集.to_delta_txt(validate=True)
            s = ranges2delta_txt_(简并集, validate=True)
            s = repr(s)
        case _:
            raise Exception('unknown ver', ver)
        #case
    s
    s = f'RT({s})'
    return s
    #.check_type_is(NonTouchRanges, 简并集)
    #.(Mk, NonTouchRanges, RT) = _mkrs4rngs_()
    #.return repr(RT(简并集))


def 构造冫简并记录纟靶值一扌():
    from seed.data_funcs.rngs import NonTouchRanges
    us = (1,)
    RT = NonTouchRanges.from_hex2sz
    简并记录纟靶值一 = 乸简并记录纟递归婪溟链(靶值=1, 最小显链长=0, 规模纟次大数集=0, 规模纟简并集=1, 次大数讠溟次=mk_FrozenDict({}), 简并集=RT({1:1}), 最短加链位置讠下界=us, 最短加链位置讠上界=us, 最短加链牜左侧最小=us, 最短加链牜左侧最大=us, 最短加链牜右侧最小=us, 最短加链牜右侧最大=us)
    return 简并记录纟靶值一

def 构造冫局部变量环境纟解读简并记录扌(ver, /):
    from seed.data_funcs.rngs import IRanges
    ex = {}
    match ver:
        case 1:
            ranges5hex2sz
            RT = IRanges.from_hex2sz
            FD = mk_FrozenDict
        case 2:
            ranges5delta_txt_
            RT = IRanges.from_delta_txt
            FD = _FD6ver2_
        case 3:
            ranges5delta_txt_
            RT = IRanges.from_delta_txt
            FD = _FD6ver2_
            ex = dict(UJ = _UJ6ver3_)
        case _:
            raise Exception('unknown ver', ver)
        #case

    RT, FD, ex
    _locals_ = dict(RT=RT, FD=FD, **ex)
    return _locals_
DELETED = object()
def 加载冫数据扌(ifile, /, *, ver, pre_ipaths, 鬽最大靶值, 欤只保留后半段数据乊最后一跃乊自顶向下, 鬽最大靶值纟留空数据段纟最后一跃乊自顶向下, verbose):
    ########
    _locals_ = 构造冫局部变量环境纟解读简并记录扌(ver)

    ########
    靶值讠简并记录 = [None]
    ########
    for pre_ipath in pre_ipaths:
        verbose and print_err('载入:', pre_ipath)
        with open(pre_ipath, 'rt', encoding='ascii') as pre_ifile:
            _加载冫数据扌(靶值讠简并记录, _locals_, pre_ifile, 鬽最大靶值, 欤只保留后半段数据乊最后一跃乊自顶向下, verbose)
    ########
    ifile.seek(0)
    _加载冫数据扌(靶值讠简并记录, _locals_, ifile, 鬽最大靶值, 欤只保留后半段数据乊最后一跃乊自顶向下, verbose)
    ########
    if 鬽最大靶值纟留空数据段纟最后一跃乊自顶向下:
        起始靶值纟最后一跃乊自顶向下 = 1+鬽最大靶值纟留空数据段纟最后一跃乊自顶向下
        if not (sz:=起始靶值纟最后一跃乊自顶向下 -len(靶值讠简并记录)) >= 0:raise TypeError(鬽最大靶值纟留空数据段纟最后一跃乊自顶向下, len(靶值讠简并记录))
        靶值讠简并记录 += [DELETED]*sz
    靶值讠简并记录
    ########
    return 靶值讠简并记录
def _加载冫数据扌(靶值讠简并记录, _locals_, ifile, 鬽最大靶值, 欤只保留后半段数据乊最后一跃乊自顶向下, verbose, /):
    for i, line in enumerate(ifile, len(靶值讠简并记录)):
        if 欤只保留后半段数据乊最后一跃乊自顶向下 and i > 40 and i&1==0:
            靶值讠简并记录[i//2-10] = DELETED
        verbose and i%1000==0 and print_err('载入...:靶值=', i)
        row = eval(line, _locals_)
        check_type_is(tuple, row)
        match row:
            case ('fail:', 靶值, 病最小显链长, 文本冃病简并记录, 真最小显链长):
                row = eval(文本冃病简并记录, _locals_)
                _加载乊囜囜记录扌 = _加载乊失败记录扌
            case _:
                _加载乊囜囜记录扌 = _加载乊简并记录扌
            #case
        #match
        assert row[0] == i, (i, row)
        _加载乊囜囜记录扌(靶值讠简并记录, _locals_, 鬽最大靶值, row)
    #for
    return
def _加载乊简并记录扌(靶值讠简并记录, _locals_, 鬽最大靶值, row, /):
    简并记录 = 乸简并记录纟递归婪溟链(*row[:-6], *map(tuple, row[-6:]))
    assert 简并记录.靶值 == len(靶值讠简并记录)
    assert 简并记录.靶值 == row[0]
    靶值讠简并记录.append(简并记录)
    if 简并记录.靶值 == 鬽最大靶值:
        raise 乸异常牜最大靶值(鬽最大靶值)#OverflowError
    #########
    #:if 0b00001:
    #:    # ^AssertionError: (15, 5, 5, 10, FD({3: 2, 5: 1, 9: 0, 10: 0, 12: 0}), RT({1: 6, 9: 2, 12: 1, 15: 1}), [1, 2, 3, 5, 9, 15], [1, 2, 4, 6, 12, 15], [1, 2, 3, 5, 10, 15], [1, 2, 4, 5, 10, 15], [1, 2, 3, 6, 9, 15], [1, 2, 3, 6, 12, 15])
    #:    assert 简并记录.最短加链位置讠上界 == 简并记录.最短加链牜右侧最大, 简并记录.to_str(ver=ver)
    #:    assert 简并记录.最短加链位置讠上界 == 简并记录.最短加链牜左侧最大, 简并记录.to_str(ver=ver)
    #########
    #:if 0b00001:
    #:    assert len(set(简并记录[-6:])) < 6, 简并记录.to_str(ver=ver)
    #:        # ^AssertionError: (15, 5, 5, 10, FD({3: 2, 5: 1, 9: 0, 10: 0, 12: 0}), RT({1: 6, 9: 2, 12: 1, 15: 1}), [1, 2, 3, 5, 9, 15], [1, 2, 4, 6, 12, 15], [1, 2, 3, 5, 10, 15], [1, 2, 4, 5, 10, 15], [1, 2, 3, 6, 9, 15], [1, 2, 3, 6, 12, 15])
    #########
    return

def _加载乊失败记录扌(靶值讠简并记录, _locals_, 鬽最大靶值, row, /):
    try:
        简并记录 = 乸简并记录纟递归婪溟链(*row[:-6], *map(tuple, row[-6:]))
    except 乸异常牜最小显链长 as exc:
        失败记录 = exc.失败记录
    else:
        raise Exception('病简并记录:未发作:', row or 简并记录)
    失败记录
    assert 失败记录.病简并记录.靶值 == row[0]
    靶值讠简并记录.append(失败记录)
    if 失败记录.病简并记录.靶值 == 鬽最大靶值:
        raise 乸异常牜最大靶值(鬽最大靶值)#OverflowError
    return


##################
def 转换冫文件格式纟简并记录纟递归婪溟链扌(输入文件路径冃靶值讠简并记录, 输出文件路径冃靶值讠简并记录, /, *, verI, verO):
    '注意:此版vs后一版:输入输出文件路径次序颠倒'
    return 转换冫文件格式纟简并记录纟递归婪溟链灬扌(输出文件路径冃靶值讠简并记录, 输入文件路径冃靶值讠简并记录, verI=verI, verO=verO, 彣匹配模板纟前置文件路径冃靶值讠简并记录='')
def 转换冫文件格式纟简并记录纟递归婪溟链灬扌(输出文件路径冃靶值讠简并记录, /, *列表纟输入文件路径冃靶值讠简并记录, verI, verO, verbose=False, 彣匹配模板纟前置文件路径冃靶值讠简并记录=''):
    check_int_ge_le(1, MAX_VERSION, verI)
    check_int_ge_le(1, MAX_VERSION, verO)
    assert not verI == verO, (verI, verO)
    (前置列表纟文件路径冃靶值讠简并记录, 输入文件路径冃靶值讠简并记录) = 规范冫列表纟文件路径冃靶值讠简并记录扌(彣匹配模板纟前置文件路径冃靶值讠简并记录, 列表纟输入文件路径冃靶值讠简并记录)
    with open(输出文件路径冃靶值讠简并记录, 'xt', encoding='ascii') as ofile:
        with open(输入文件路径冃靶值讠简并记录, 'rt', encoding='ascii') as ifile:
            靶值讠简并记录 = 加载冫数据扌(ifile, ver=verI, pre_ipaths=前置列表纟文件路径冃靶值讠简并记录, 鬽最大靶值=None, verbose=verbose)
        靶值讠简并记录
        for 靶值, 简并记录 in enumerate(靶值讠简并记录):
            if 靶值 == 0:continue
            verbose and print_err('靶值 =', 靶值)
            print(简并记录.to_str(ver=verO), file=ofile)
##################
def 另档冫极简次大数集纟简并记录纟递归婪溟链扌(输出文件路径冃靶值讠极简次大数集, /, *列表纟输入文件路径冃靶值讠简并记录, ver, 彣匹配模板纟前置文件路径冃靶值讠简并记录='', verbose=False):
    print_err('失败@[靶值==59]')
    check_int_ge_le(1, MAX_VERSION, ver)
    (前置列表纟文件路径冃靶值讠简并记录, 输入文件路径冃靶值讠简并记录) = 规范冫列表纟文件路径冃靶值讠简并记录扌(彣匹配模板纟前置文件路径冃靶值讠简并记录, 列表纟输入文件路径冃靶值讠简并记录)
    with open(输出文件路径冃靶值讠极简次大数集, 'xt', encoding='ascii') as ofile:
        with open(输入文件路径冃靶值讠简并记录, 'rt', encoding='ascii') as ifile:
            靶值讠简并记录 = 加载冫数据扌(ifile, ver=ver, pre_ipaths=前置列表纟文件路径冃靶值讠简并记录, 鬽最大靶值=None, verbose=verbose)
            靶值讠极简次大数讠溟次 = [None]
            for 靶值, 简并记录 in enumerate(靶值讠简并记录):
                if 靶值 == 0:continue
                assert 靶值 == 简并记录.靶值
                assert 靶值 == len(靶值讠极简次大数讠溟次)
                极简次大数讠溟次 = {}
                for 次大数, 溟次 in 简并记录.次大数讠溟次.items():
                    内点 = (靶值 -次大数) >> 溟次
                    if 内点 in [次大数, 2, 1] or 内点 in 靶值讠极简次大数讠溟次[次大数]:
                        #递归/递降
                        极简次大数讠溟次[次大数] = 溟次
                极简次大数讠溟次
                if not (极简次大数讠溟次 or 靶值==1):raise Exception(靶值)
                    # ^Exception: 59
                靶值讠极简次大数讠溟次.append(极简次大数讠溟次)
                s = stable_repr((靶值, 简并记录.最小显链长, len(极简次大数讠溟次), 极简次大数讠溟次))
                print(s, file=ofile)

##################
def 另档冫幸存次大数必由集纟简并记录纟递归婪溟链扌(输出文件路径冃靶值讠幸存次大数必由集, /, *列表纟输入文件路径冃靶值讠简并记录, ver, 彣匹配模板纟前置文件路径冃靶值讠简并记录='', verbose=False):
    print_err('失败@[靶值==77]')
    check_int_ge_le(1, MAX_VERSION, ver)
    (前置列表纟文件路径冃靶值讠简并记录, 输入文件路径冃靶值讠简并记录) = 规范冫列表纟文件路径冃靶值讠简并记录扌(彣匹配模板纟前置文件路径冃靶值讠简并记录, 列表纟输入文件路径冃靶值讠简并记录)
    with open(输出文件路径冃靶值讠幸存次大数必由集, 'xt', encoding='ascii') as ofile:
        with open(输入文件路径冃靶值讠简并记录, 'rt', encoding='ascii') as ifile:
            靶值讠简并记录 = 加载冫数据扌(ifile, ver=ver, pre_ipaths=前置列表纟文件路径冃靶值讠简并记录, 鬽最大靶值=None, verbose=verbose)
            #幸存次大数必由集-->(幸存次大数讠溟次, 幸存次大数讠必由集)
            #必由集-->内点溟化值集
            靶值讠幸存次大数讠溟次 = [None]
            #靶值讠幸存次大数讠必由集 = [None]
            #靶值讠幸存次大数讠内点溟化值集 = [None]
            靶值讠内点溟化值合集 = [None]
            for 靶值, 简并记录 in enumerate(靶值讠简并记录):
                if 靶值 == 0:continue
                assert 靶值 == 简并记录.靶值
                assert 靶值 == len(靶值讠幸存次大数讠溟次)
                assert 靶值 == len(靶值讠内点溟化值合集)
                幸存次大数讠溟次 = {}
                内点溟化值合集 = set()
                for 次大数, 溟次 in 简并记录.次大数讠溟次.items():
                    内点 = (靶值 -次大数) >> 溟次
                    if 内点 in [次大数, 2, 1] or 内点 in 靶值讠幸存次大数讠溟次[次大数] or 内点 in 靶值讠内点溟化值合集[次大数]:
                        #递归/递降
                        幸存次大数讠溟次[次大数] = 溟次
                        内点溟化值合集.update(内点<<ez for ez in range(1+溟次))
                幸存次大数讠溟次
                内点溟化值合集
                if not (幸存次大数讠溟次 or 靶值==1):raise Exception(靶值)
                    # ^Exception: 77
                靶值讠幸存次大数讠溟次.append(幸存次大数讠溟次)
                靶值讠内点溟化值合集.append(内点溟化值合集)
                s = stable_repr((靶值, 简并记录.最小显链长, len(幸存次大数讠溟次), 幸存次大数讠溟次, len(内点溟化值合集), 内点溟化值合集))
                print(s, file=ofile)


##################
def 另档冫双点易来简并态纟简并记录纟递归婪溟链扌(输出文件路径冃靶值讠双点易来简并态, /, *列表纟输入文件路径冃靶值讠简并记录, ver, 彣匹配模板纟前置文件路径冃靶值讠简并记录='', verbose=False):
    check_int_ge_le(1, MAX_VERSION, ver)
    (前置列表纟文件路径冃靶值讠简并记录, 输入文件路径冃靶值讠简并记录) = 规范冫列表纟文件路径冃靶值讠简并记录扌(彣匹配模板纟前置文件路径冃靶值讠简并记录, 列表纟输入文件路径冃靶值讠简并记录)
    with open(输出文件路径冃靶值讠双点易来简并态, 'xt', encoding='ascii') as ofile:
        with open(输入文件路径冃靶值讠简并记录, 'rt', encoding='ascii') as ifile:
            靶值讠简并记录 = 加载冫数据扌(ifile, ver=ver, pre_ipaths=前置列表纟文件路径冃靶值讠简并记录, 鬽最大靶值=None, verbose=verbose)
            #双点易来简并态-->(易来次大数讠溟次, 定点讠易来简并态)
            靶值讠易来次大数讠溟次 = [None]
            靶值讠定点讠易来简并态 = [None]
            for 靶值, 简并记录 in enumerate(靶值讠简并记录):
                if 靶值 == 0:continue
                assert 靶值 == 简并记录.靶值
                assert 靶值 == len(靶值讠易来次大数讠溟次)
                assert 靶值 == len(靶值讠定点讠易来简并态)
                ######
                易来次大数讠溟次 = _求冫易来次大数讠溟次扌(靶值讠易来次大数讠溟次, 靶值讠定点讠易来简并态, 靶值, 简并记录.次大数讠溟次)
                if not (易来次大数讠溟次 or 靶值==1):raise Exception(靶值)
                    # xxx^Exception: 77
                ######
                定点讠易来简并态 = _求冫定点讠易来简并态扌(靶值讠定点讠易来简并态, 靶值, 易来次大数讠溟次)
                if not 定点讠易来简并态.get(靶值):raise Exception(靶值)
                ######
                靶值讠易来次大数讠溟次.append(易来次大数讠溟次)
                靶值讠定点讠易来简并态.append(定点讠易来简并态)
                s = stable_repr((靶值, 简并记录.最小显链长, len(易来次大数讠溟次), 易来次大数讠溟次, len(定点讠易来简并态), 定点讠易来简并态))
                print(s, file=ofile)


def _求冫易来次大数讠溟次扌(靶值讠易来次大数讠溟次, 靶值讠定点讠易来简并态, 靶值, 次大数讠溟次, /):
    易来次大数讠溟次 = {}
    for 次大数, 溟次 in 次大数讠溟次.items():
        内点 = (靶值 -次大数) >> 溟次
        #内点溟化值集 = {内点<<ez for ez in range(1+溟次)}
        if 内点 in [次大数, 2, 1] or 内点 in 靶值讠易来次大数讠溟次[次大数] or 靶值讠定点讠易来简并态[次大数].get(内点):
            #递归/递降
            易来次大数讠溟次[次大数] = 溟次
    return 易来次大数讠溟次
def _求冫定点讠易来简并态扌(靶值讠定点讠易来简并态, 靶值, 易来次大数讠溟次, /):
    '-> 定点讠易来简并态'
    定点讠易来简并态 = {}
    if 靶值 <= 3:
        简并态 = set(range(1, 1+靶值))
        定点讠易来简并态 = {定点:简并态 for 定点 in 简并态}
    else:
        定点讠易来简并态 = {}
        for 定点 in range(3, 1+靶值):
            有效集 = 易来简并态纟靶值乊定点 = _求冫易来简并态巛定点牜大于二扌(靶值讠定点讠易来简并态, 靶值, 易来次大数讠溟次, 定点)
            if 有效集:
                定点讠易来简并态[定点] = 有效集
        #end-for 定点 in range(3, 靶值):
        for 定点 in [1, 2]:
            定点讠易来简并态[定点] = 定点讠易来简并态[靶值]
    return 定点讠易来简并态


def _求冫易来简并态巛定点牜大于二扌(靶值讠定点讠易来简并态, 靶值, 易来次大数讠溟次, 定点, /):
    '... -> 定点 -> 易来简并态'
    def 鬽取臫靶值讠定点讠易来简并态扌(次大数, 内点, 缺省值, /):
        return 靶值讠定点讠易来简并态[次大数].get(内点, 缺省值)
    return _求冫易来简并态巛定点牜大于二牜共用扌(鬽取臫靶值讠定点讠易来简并态扌, 靶值, 易来次大数讠溟次, 定点)
##################
#上下共用:
def _求冫易来简并态巛定点牜大于二牜共用扌(鬽取臫靶值讠定点讠易来简并态扌, 靶值, 易来次大数讠溟次, 定点, /):
    assert 3 <= 定点 <= 靶值
    有效集 = set()
    for (次大数, 溟次) in 易来次大数讠溟次.items():
        内点 = (靶值 -次大数) >> 溟次
        内点溟化值集 = [内点<<ez for ez in range(1+溟次)]
            #可能有:[次大数 < max(内点溟化值集)]
        if 定点 in [靶值, 次大数, 2, 1] or 定点 in 内点溟化值集:
            #s = 靶值讠定点讠易来简并态[次大数].get(内点, [])
            s = 鬽取臫靶值讠定点讠易来简并态扌(次大数, 内点, [])
        elif 定点 > 次大数:
            s = []
        elif 内点 in [次大数, 2, 1]:
            #s = 靶值讠定点讠易来简并态[次大数].get(定点, [])
            s = 鬽取臫靶值讠定点讠易来简并态扌(次大数, 定点, [])
        #elif 定点 in 靶值讠定点讠易来简并态[次大数].get(内点, []):
        elif 定点 in 鬽取臫靶值讠定点讠易来简并态扌(次大数, 内点, []):
            s = [定点]
        else:
            s = []
        内有效集 = s
        if 内有效集:
            有效集.update(内有效集)
            有效集.update(内点溟化值集)
    有效集
    if 有效集:
        有效集.update([靶值, 次大数, 2, 1])
    return (易来简并态:=有效集)
##################
def 另档冫双点易来简并态纟简并记录纟递归婪溟链牜按需计算扌(输出文件路径冃靶值讠双点易来简并态, /, *列表纟输入文件路径冃靶值讠简并记录, ver, 彣匹配模板纟前置文件路径冃靶值讠简并记录='', verbose=False):
    '按需计算'
    check_int_ge_le(1, MAX_VERSION, ver)
    (前置列表纟文件路径冃靶值讠简并记录, 输入文件路径冃靶值讠简并记录) = 规范冫列表纟文件路径冃靶值讠简并记录扌(彣匹配模板纟前置文件路径冃靶值讠简并记录, 列表纟输入文件路径冃靶值讠简并记录)
    with open(输出文件路径冃靶值讠双点易来简并态, 'xt', encoding='ascii') as ofile:
        with open(输入文件路径冃靶值讠简并记录, 'rt', encoding='ascii') as ifile:
            verbose and print_err('loading data...')
            靶值讠简并记录 = 加载冫数据扌(ifile, ver=ver, pre_ipaths=前置列表纟文件路径冃靶值讠简并记录, 鬽最大靶值=None, verbose=verbose)
            verbose and print_err('main loop...')
            #双点易来简并态-->(易来次大数讠溟次, 定点讠易来简并态)
            靶值讠易来次大数讠溟次 = [None]
            靶值讠易来简并态 = [None]
            缓存冃靶值讠定点讠易来简并态 = [None]
            for 靶值, 简并记录 in enumerate(靶值讠简并记录):
                if 靶值 == 0:continue
                verbose and print_err('靶值 =', 靶值)
                assert 靶值 == 简并记录.靶值
                assert 靶值 == len(靶值讠易来次大数讠溟次)
                assert 靶值 == len(靶值讠易来简并态)
                assert 靶值 == len(缓存冃靶值讠定点讠易来简并态)
                ######
                缓存冃靶值讠定点讠易来简并态.append({})
                ######
                易来次大数讠溟次 = _求冫易来次大数讠溟次牜按需计算扌(靶值讠易来简并态, 靶值, 简并记录.次大数讠溟次)
                if not (易来次大数讠溟次 or 靶值==1):raise Exception(靶值)
                    # ^Exception: 2077
                ######
                易来简并态纟靶值 = _靶值讠定点讠易来简并态扌(靶值讠易来次大数讠溟次, 靶值讠易来简并态, 缓存冃靶值讠定点讠易来简并态, 易来次大数讠溟次, 靶值, 靶值)
                if not 易来简并态纟靶值:raise Exception(靶值)
                ######
                靶值讠易来次大数讠溟次.append(易来次大数讠溟次)
                靶值讠易来简并态.append(易来简并态纟靶值)
                #s = stable_repr((靶值, 简并记录.最小显链长, len(易来次大数讠溟次), 易来次大数讠溟次, len(易来简并态纟靶值), 易来简并态纟靶值))
                s4s = ranges2delta_txt_(_转换集合扌(易来简并态纟靶值), validate=True)
                #.s = stable_repr((靶值, 简并记录.最小显链长, len(易来次大数讠溟次), 易来次大数讠溟次, len(易来简并态纟靶值), s4s))
                s4d = _表述冫次大数讠溟次讠文本表达扌(易来次大数讠溟次)
                s = stable_repr((靶值, 简并记录.最小显链长, len(易来次大数讠溟次), s4d, len(易来简并态纟靶值), s4s))
                print(s, file=ofile)

def _求冫易来次大数讠溟次牜按需计算扌(靶值讠易来简并态, 靶值, 次大数讠溟次, /):
    易来次大数讠溟次 = {}
    for 次大数, 溟次 in 次大数讠溟次.items():
        内点 = (靶值 -次大数) >> 溟次
        #内点溟化值集 = [内点<<ez for ez in range(1+溟次)]
        #if 内点 in [次大数, 2, 1] or 内点 in 靶值讠易来次大数讠溟次[次大数] or 内点 in 靶值讠易来简并态[次大数]:
        if 内点 in 靶值讠易来简并态[次大数]:
            #递归/递降
            易来次大数讠溟次[次大数] = 溟次
    return 易来次大数讠溟次


def _靶值讠定点讠易来简并态扌(靶值讠易来次大数讠溟次, 靶值讠易来简并态, 缓存冃靶值讠定点讠易来简并态, 易来次大数讠溟次, 靶值, 定点, /):
    '-> 易来简并态纟靶值乊定点'
    assert 1 <= 定点 <= 靶值
    v2s = 缓存冃靶值讠定点讠易来简并态[靶值]
    if not None is (s:=v2s.get(定点)):
        return s
    s = _0靶值讠定点讠易来简并态扌(靶值讠易来次大数讠溟次, 靶值讠易来简并态, 缓存冃靶值讠定点讠易来简并态, 易来次大数讠溟次, 靶值, 定点)
    v2s[定点] = s
    return _靶值讠定点讠易来简并态扌(靶值讠易来次大数讠溟次, 靶值讠易来简并态, 缓存冃靶值讠定点讠易来简并态, 易来次大数讠溟次, 靶值, 定点)
def _0靶值讠定点讠易来简并态扌(靶值讠易来次大数讠溟次, 靶值讠易来简并态, 缓存冃靶值讠定点讠易来简并态, 易来次大数讠溟次, 靶值, 定点, /):
    if 靶值 == 定点:
        if 靶值 < len(靶值讠易来简并态):
            return 靶值讠易来简并态[靶值]
        if not 靶值 == len(靶值讠易来简并态):raise 000
        if 靶值 <= 3:
            return set(range(1, 1+靶值))
        # [4 <= 定点 == 靶值 == len(靶值讠易来简并态)]
    else:
        # [1 <= 定点 < 靶值]
        pass
    # [4 <= 定点 == 靶值]or[1 <= 定点 < 靶值]
    if 定点 <= 2:
        # [1 <= 定点 < 靶值]
        assert 靶值 > 定点
        return _靶值讠定点讠易来简并态扌(靶值讠易来次大数讠溟次, 靶值讠易来简并态, 缓存冃靶值讠定点讠易来简并态, 易来次大数讠溟次, 靶值, 靶值)
    # [3 <= 定点]
    # [4 <= 定点 == 靶值]or[3 <= 定点 < 靶值]
    def 鬽取臫靶值讠定点讠易来简并态扌(次大数, 内点, 缺省值, /):
        s = _靶值讠定点讠易来简并态扌(靶值讠易来次大数讠溟次, 靶值讠易来简并态, 缓存冃靶值讠定点讠易来简并态, 靶值讠易来次大数讠溟次[次大数], 次大数, 内点)
        return s if s else 缺省值
    有效集 = 易来简并态纟靶值乊定点 = _求冫易来简并态巛定点牜大于二牜共用扌(鬽取臫靶值讠定点讠易来简并态扌, 靶值, 易来次大数讠溟次, 定点)
    return 易来简并态纟靶值乊定点

##################
#共用:
def _get_s4u_5line__verX_(line, /, *, 欤允许缺失乊最后一跃=False):
    a = 1+line.index('(')
    ')'
    b = line.index(',', a)
    s4u = line[a:b]
    if 欤允许缺失乊最后一跃:
        ok = not s4u == "'fail:'"
        if not ok:
            try:
                c = line.index(',', 1+b)
                _b = 1+line.rindex(' ', b, c)
            except ValueError:
                print_err((line, a, b))
                raise
            assert _b == b+2
            s4u = line[_b:c]
            return (ok, s4u, _b, c)
        return (ok, s4u, a, b)
    return (s4u, a, b)
def _get_s4uss_5line__ver1_ver2_(line, /):
    '('
    j = line.rindex(')')
    i = j
    for _ in range(6):
        i = line.rindex(', [1', 0, i)
        ']'
    assert line[i:i+4] == ', [1'
    ']'
    i += 2
    s4uss = line[i:j]
    return (s4uss, i, j)



    #.'('
    #.i = line.rindex(')', 0, j)
    #.'('
    #.assert line[i:i+5] == '), [1'
    #.']'
    #.s4uss = line[i+3:j]
    #.return s4uss
def _get_s4uss_5line__ver3_(line, /):
    '('
    j = line.rindex(')')
    i = line.rindex(', *UJ(', 0, j)
    ')'
    i += 2
    s4uss = line[i:j]
    return (s4uss, i, j)
def _mk_get_s4uss_5line__5ver_(ver, /):
    match ver:
        case 1 | 2:
            get_s4uss_5line__verX_ = _get_s4uss_5line__ver1_ver2_
        case 3:
            get_s4uss_5line__verX_ = _get_s4uss_5line__ver3_
        case bad:
            raise Exception(ver)
        #case
    return get_s4uss_5line__verX_
##################
_ver3__eval7uss_
_ver3__str7uss_
_ver3__repr7uss_
def _repr5uss__ver3_(uss, /):
    '-> s4uss'
    assert len(uss) == 6
    return _ver3__repr7uss_(uss)
def _repr5uss__ver1_ver2_(uss, /):
    '-> s4uss'
    assert len(uss) == 6
    return str(uss)[1:-1]
def _repr2uss__ver3_(s4uss, /):
    '-> uss'
    s = f'[{s4uss}]'
    return eval(s, dict(UJ=_ver3__eval7uss_))
def _repr2uss__ver1_ver2_(s4uss, /):
    '-> uss'
    s = f'[{s4uss}]'
    return eval(s)
def _mk_repr25uss__5ver_(ver, /):
    match ver:
        case 1 | 2:
            _repr25uss_ = (_repr2uss__ver1_ver2_, _repr5uss__ver1_ver2_)
        case 3:
            _repr25uss_ = (_repr2uss__ver3_, _repr5uss__ver3_)
        case bad:
            raise Exception(ver)
        #case
    return _repr25uss_
##################
##################
def 转换冫尾六表纟简并记录纟递归婪溟链扌(输出文件路径冃靶值讠尾六表, /, *列表纟输入文件路径冃靶值讠尾六表, verI, verO, 彣匹配模板纟前置文件路径冃靶值讠尾六表='', 欤删除中段数据=False, 欤允许输入输出是同版本=False, verbose=False):
    #++kw:欤删除中段数据
    #++kw:欤允许输入输出是同版本
    '[尾六表 =[def]= regex"({靶值}.*, {六表})"] #eg:简并记录,下上界辻左右大小四色最短加链'
    check_int_ge_le(1, MAX_VERSION, verI)
    check_int_ge_le(1, MAX_VERSION, verO)
    _verI = max(verI, 2)
    _verO = max(verO, 2)
    if _verI == _verO and not 欤允许输入输出是同版本:raise Exception((verI, verO))
    (前置列表纟文件路径冃靶值讠尾六表, 输入文件路径冃靶值讠尾六表) = 规范冫列表纟文件路径冃靶值讠简并记录扌(彣匹配模板纟前置文件路径冃靶值讠尾六表, 列表纟输入文件路径冃靶值讠尾六表)
    get_s4uss_5line__verX_ = _mk_get_s4uss_5line__5ver_(verI)
    (_repr2uss__verI_, _repr5uss__verI_) = _mk_repr25uss__5ver_(verI)
    (_repr2uss__verO_, _repr5uss__verO_) = _mk_repr25uss__5ver_(verO)
    def body_(ipath, ifile, ofile, /):
        verbose and print_err(f'ipath: {ipath!r}')
        for line in ifile:
            (s4u, a, b) = _get_s4u_5line__verX_(line)
            verbose and print_err(f'靶值: {s4u!s}')
            (s4ussI, i, j) = get_s4uss_5line__verX_(line)
            uss = _repr2uss__verI_(s4ussI)
            s4ussO = _repr5uss__verO_(uss)
            if 欤删除中段数据:
                t = f'({s4u}, {s4ussO})'
            else:
                prefix = line[a:i]
                t = f'({prefix}{s4ussO})'
            print(t, file=ofile)
    def main():
        with open(输出文件路径冃靶值讠尾六表, 'xt', encoding='ascii') as ofile:
            for ipath in [*前置列表纟文件路径冃靶值讠尾六表, 输入文件路径冃靶值讠尾六表]:
                with open(ipath, 'rt', encoding='ascii') as ifile:
                    body_(ipath, ifile, ofile)
    return main()


##################
def 另档冫尾六表纟简并记录纟递归婪溟链扌(输出文件路径冃靶值讠尾六表, /, *列表纟输入文件路径冃靶值讠尾六表, ver, verI=-1, verO=-1, 彣匹配模板纟前置文件路径冃靶值讠尾六表='', verbose=False):
    #原名:另档冫下上界辻左右大小四色最短加链纟简并记录纟递归婪溟链扌
    '[尾六表 =[def]= regex"({靶值}.*, {六表})"] #eg:简并记录,下上界辻左右大小四色最短加链'
    check_type_is(int, ver)
    check_type_is(int, verI)
    check_type_is(int, verO)
    if not ver == -1:
        check_int_ge_le(1, MAX_VERSION, ver)
        if not verI == -1:raise TypeError
        if not verO == -1:raise TypeError
        verI = ver
        verO = ver
    check_int_ge_le(1, MAX_VERSION, verI)
    check_int_ge_le(1, MAX_VERSION, verO)
    return 转换冫尾六表纟简并记录纟递归婪溟链扌(输出文件路径冃靶值讠尾六表, *列表纟输入文件路径冃靶值讠尾六表, verI=verI, verO=verO, 彣匹配模板纟前置文件路径冃靶值讠尾六表=彣匹配模板纟前置文件路径冃靶值讠尾六表, 欤删除中段数据=True, 欤允许输入输出是同版本=True, verbose=verbose)
    #.(前置列表纟文件路径冃靶值讠尾六表, 输入文件路径冃靶值讠尾六表) = 规范冫列表纟文件路径冃靶值讠简并记录扌(彣匹配模板纟前置文件路径冃靶值讠尾六表, 列表纟输入文件路径冃靶值讠尾六表)
    #.get_s4uss_5line__verX_ = _mk_get_s4uss_5line__5ver_(ver)
    #.def body_(ipath, ifile, ofile, /):
    #.    verbose and print_err(f'ipath: {ipath!r}')
    #.    for line in ifile:
    #.        (s4u, a, b) = _get_s4u_5line__verX_(line)
    #.        verbose and print_err(f'靶值: {s4u!s}')
    #.        (s4uss, i, j) = get_s4uss_5line__verX_(line)
    #.        s = f'({s4u}, {s4uss})'
    #.        if 0:
    #.            _s = s.replace(', *UJ', '')
    #.            if (__:=set(_s) -set('0123456789, []()')):raise Exception(__)
    #.            u_uss = tuple(map(tuple, eval(s)))
    #.            assert len(u_uss) == 1+6
    #.        s
    #.        print(s, file=ofile)
    #.def main():
    #.    with open(输出文件路径冃靶值讠尾六表, 'xt', encoding='ascii') as ofile:
    #.        for ipath in [*前置列表纟文件路径冃靶值讠尾六表, 输入文件路径冃靶值讠尾六表]:
    #.            with open(ipath, 'rt', encoding='ascii') as ifile:
    #.                body_(ipath, ifile, ofile)
    #.return main()

##################
_kind2idx = dict(下界=0, 上界=1, 左侧最小=2, 左侧最大=3, 右侧最小=4, 右侧最大=5)
def 另档冫递归婪溟链暨最短加链牜某尾四表讠址距溟次形式扌(输出文件路径冃靶值讠址距溟次形式, /, *列表纟输入文件路径冃靶值讠尾六表, ver, kind, 彣匹配模板纟前置文件路径冃靶值讠尾六表='', 欤允许缺失乊最后一跃=False, 欤追附=False, verbose=False):
    check_int_ge_le(1, MAX_VERSION, verI:=ver)
    _verI = max(verI, 2)
    idx = _kind2idx[kind]
    if idx < 2:raise TypeError('下界,上界:未必是加链，更无婪溟链的表达形式', kind)
    (前置列表纟文件路径冃靶值讠尾六表, 输入文件路径冃靶值讠尾六表) = 规范冫列表纟文件路径冃靶值讠简并记录扌(彣匹配模板纟前置文件路径冃靶值讠尾六表, 列表纟输入文件路径冃靶值讠尾六表)
    get_s4uss_5line__verX_ = _mk_get_s4uss_5line__5ver_(verI)
    (_repr2uss__verI_, _repr5uss__verI_) = _mk_repr25uss__5ver_(verI)
    from seed.math.power.addition_chain.shortest.rewrite3 import 严序加链讠最短缩写文本纟递归婪溟链扌, 严序加链巛最短缩写文本纟递归婪溟链扌
        #址距溟次形式:dnzw_str
    def body_(ipath, ifile, ofile, /):
        verbose and print_err(f'ipath: {ipath!r}')
        for line in ifile:
            #(s4u, a, b) = _get_s4u_5line__verX_(line)
            (ok, s4u, a, b) = _get_s4u_5line__verX_(line, 欤允许缺失乊最后一跃=True)
            verbose and print_err(f'靶值: {s4u!s}')
            if not ok:
                if not 欤允许缺失乊最后一跃:raise ValueError(line)
                print(f'-{s4u}', file=ofile)
                continue
            (s4ussI, i, j) = get_s4uss_5line__verX_(line)
            uss = _repr2uss__verI_(s4ussI)
            #原版:左侧最大 = uss[3] #递归婪溟链暨最短加链牜左侧最大
            #泛化后:
            us = uss[idx]
            址距溟次形式 = 严序加链讠最短缩写文本纟递归婪溟链扌(us, fmt_case='dnzw_str')
            print(址距溟次形式, file=ofile)
    def main():
        omode = 'xt' if not 欤追附 else 'at'
        with open(输出文件路径冃靶值讠址距溟次形式, omode, encoding='ascii') as ofile:
            for ipath in [*前置列表纟文件路径冃靶值讠尾六表, 输入文件路径冃靶值讠尾六表]:
                with open(ipath, 'rt', encoding='ascii') as ifile:
                    body_(ipath, ifile, ofile)
    return main()
def 另档冫递归婪溟链暨最短加链牜左侧最小讠址距溟次形式扌(输出文件路径冃靶值讠址距溟次形式, /, *列表纟输入文件路径冃靶值讠尾六表, ver, 彣匹配模板纟前置文件路径冃靶值讠尾六表='', verbose=False, **kwds):
    kind = '左侧最小'
    return 另档冫递归婪溟链暨最短加链牜某尾四表讠址距溟次形式扌(输出文件路径冃靶值讠址距溟次形式, *列表纟输入文件路径冃靶值讠尾六表, ver=ver, kind=kind, 彣匹配模板纟前置文件路径冃靶值讠尾六表=彣匹配模板纟前置文件路径冃靶值讠尾六表, verbose=verbose, **kwds)
def 另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌(输出文件路径冃靶值讠址距溟次形式, /, *列表纟输入文件路径冃靶值讠尾六表, ver, 彣匹配模板纟前置文件路径冃靶值讠尾六表='', verbose=False, **kwds):
    kind = '左侧最大'
    return 另档冫递归婪溟链暨最短加链牜某尾四表讠址距溟次形式扌(输出文件路径冃靶值讠址距溟次形式, *列表纟输入文件路径冃靶值讠尾六表, ver=ver, kind=kind, 彣匹配模板纟前置文件路径冃靶值讠尾六表=彣匹配模板纟前置文件路径冃靶值讠尾六表, verbose=verbose, **kwds)
def 另档冫递归婪溟链暨最短加链牜右侧最小讠址距溟次形式扌(输出文件路径冃靶值讠址距溟次形式, /, *列表纟输入文件路径冃靶值讠尾六表, ver, 彣匹配模板纟前置文件路径冃靶值讠尾六表='', verbose=False, **kwds):
    kind = '右侧最小'
    return 另档冫递归婪溟链暨最短加链牜某尾四表讠址距溟次形式扌(输出文件路径冃靶值讠址距溟次形式, *列表纟输入文件路径冃靶值讠尾六表, ver=ver, kind=kind, 彣匹配模板纟前置文件路径冃靶值讠尾六表=彣匹配模板纟前置文件路径冃靶值讠尾六表, verbose=verbose, **kwds)
def 另档冫递归婪溟链暨最短加链牜右侧最大讠址距溟次形式扌(输出文件路径冃靶值讠址距溟次形式, /, *列表纟输入文件路径冃靶值讠尾六表, ver, 彣匹配模板纟前置文件路径冃靶值讠尾六表='', verbose=False, **kwds):
    kind = '右侧最大'
    return 另档冫递归婪溟链暨最短加链牜某尾四表讠址距溟次形式扌(输出文件路径冃靶值讠址距溟次形式, *列表纟输入文件路径冃靶值讠尾六表, ver=ver, kind=kind, 彣匹配模板纟前置文件路径冃靶值讠尾六表=彣匹配模板纟前置文件路径冃靶值讠尾六表, verbose=verbose, **kwds)


##################
def 求冫丮最小比率辻靶值列表厈牜长度纟头部二幂纟左侧最大最短加链之于最小显链长纟靶值扌(*列表纟输入文件路径冃靶值讠尾六表, ver, verbose=False):
    from fractions import Fraction
    check_int_ge_le(1, MAX_VERSION, ver)
    get_s4uss_5line__verX_ = _mk_get_s4uss_5line__5ver_(ver)
    (_repr2uss__verI_, _repr5uss__verI_) = _mk_repr25uss__5ver_(ver)
    def body_(ipath, ifile, 最小比率, 列表纟靶值, /):
        verbose and print_err(f'ipath: {ipath!r}')
        for line in ifile:
            (s4u, a, b) = _get_s4u_5line__verX_(line)
            verbose and print_err(f'靶值: {s4u!s}')
            (s4ussI, i, j) = get_s4uss_5line__verX_(line)
            uss = _repr2uss__verI_(s4ussI)
            靶值 = int(s4u)
            最短加链牜左侧最大 = uss[3]
            最小显链长纟靶值 = -1+len(最短加链牜左侧最大)
            长度纟头部二幂 = 0
            for u, v in pairwise(最短加链牜左侧最大):
                if v == (u<<1):
                    长度纟头部二幂 += 1
                else:
                    break
            长度纟头部二幂
            if 最小显链长纟靶值 == 0:
                continue
            比率 = Fraction(长度纟头部二幂, 最小显链长纟靶值)
            if 比率 < 最小比率:
                最小比率 = 比率
                列表纟靶值 = [靶值]
            elif 比率 == 最小比率:
                列表纟靶值.append(靶值)
            else:
                continue
        return (最小比率, 列表纟靶值)
    def main():
        最小比率 = Fraction(1)
        列表纟靶值 = [1]
        for ipath in 列表纟输入文件路径冃靶值讠尾六表:
            with open(ipath, 'rt', encoding='ascii') as ifile:
                (最小比率, 列表纟靶值) = body_(ipath, ifile, 最小比率, 列表纟靶值)
        return (最小比率, 列表纟靶值)
    return main()

##################
def 求冫丮最大比率辻靶值列表厈牜次大数纟右侧最小最短加链之于靶值扌(*列表纟输入文件路径冃靶值讠尾六表, ver, verbose=False):
    from fractions import Fraction
    check_int_ge_le(1, MAX_VERSION, ver)
    get_s4uss_5line__verX_ = _mk_get_s4uss_5line__5ver_(ver)
    (_repr2uss__verI_, _repr5uss__verI_) = _mk_repr25uss__5ver_(ver)
    def body_(ipath, ifile, 最大比率, 列表纟靶值, /):
        verbose and print_err(f'ipath: {ipath!r}')
        for line in ifile:
            (s4u, a, b) = _get_s4u_5line__verX_(line)
            verbose and print_err(f'靶值: {s4u!s}')
            (s4ussI, i, j) = get_s4uss_5line__verX_(line)
            uss = _repr2uss__verI_(s4ussI)
            靶值 = int(s4u)
            if 靶值 == 1:
                continue
            最短加链牜右侧最小 = uss[4]
            次大数 = 最短加链牜右侧最小[-2]
            assert 靶值 == 最短加链牜右侧最小[-1]
            比率 = Fraction(次大数, 靶值)
            if 比率 > 最大比率:
                最大比率 = 比率
                列表纟靶值 = [靶值]
            elif 比率 == 最大比率:
                列表纟靶值.append(靶值)
            else:
                continue
        return (最大比率, 列表纟靶值)
    def main():
        最大比率 = Fraction(0)
        列表纟靶值 = [1]
        for ipath in 列表纟输入文件路径冃靶值讠尾六表:
            with open(ipath, 'rt', encoding='ascii') as ifile:
                (最大比率, 列表纟靶值) = body_(ipath, ifile, 最大比率, 列表纟靶值)
        return (最大比率, 列表纟靶值)
    return main()




##################
def 求冫丮最大差值辻靶值列表厈牜两倍次大数纟右侧最小最短加链之于靶值扌(*列表纟输入文件路径冃靶值讠尾六表, ver, verbose=False):
    #from fractions import Fraction
    check_int_ge_le(1, MAX_VERSION, ver)
    get_s4uss_5line__verX_ = _mk_get_s4uss_5line__5ver_(ver)
    (_repr2uss__verI_, _repr5uss__verI_) = _mk_repr25uss__5ver_(ver)
    def body_(ipath, ifile, 最大差值, 列表纟靶值, /):
        verbose and print_err(f'ipath: {ipath!r}')
        for line in ifile:
            (s4u, a, b) = _get_s4u_5line__verX_(line)
            verbose and print_err(f'靶值: {s4u!s}')
            (s4ussI, i, j) = get_s4uss_5line__verX_(line)
            uss = _repr2uss__verI_(s4ussI)
            靶值 = int(s4u)
            if 靶值 == 1:
                continue
            最短加链牜右侧最小 = uss[4]
            次大数 = 最短加链牜右侧最小[-2]
            assert 靶值 == 最短加链牜右侧最小[-1]
            差值 = (2*次大数 - 靶值)
            if 差值 > 最大差值:
                最大差值 = 差值
                列表纟靶值 = [靶值]
            elif 差值 == 最大差值:
                列表纟靶值.append(靶值)
            else:
                continue
        return (最大差值, 列表纟靶值)
    def main():
        最大差值 = 0
        列表纟靶值 = [1]
        for ipath in 列表纟输入文件路径冃靶值讠尾六表:
            with open(ipath, 'rt', encoding='ascii') as ifile:
                (最大差值, 列表纟靶值) = body_(ipath, ifile, 最大差值, 列表纟靶值)
        return (最大差值, 列表纟靶值)
    return main()



##################
def 最大化乊已有简并记录冫最小化乊尾四链冫最大内点址距乊加链扌(*列表纟输入文件路径冃靶值讠尾六表, ver, verbose=False, 欤记录首峰值位=False, 欤趃输出=False):
    from seed.math.power.addition_chain.shortest.rewrite3 import 枚举冫递归婪溟链巛严序加链扌
    from seed.iters.maxs import maxs_, maxs7continue_, mins_, mins7continue_

    check_int_ge_le(1, MAX_VERSION, ver)
    get_s4uss_5line__verX_ = _mk_get_s4uss_5line__5ver_(ver)
    (_repr2uss__verI_, _repr5uss__verI_) = _mk_repr25uss__5ver_(ver)
    def 最大内点址距辻列表乊加链扌(加链, /):
        #mins_-max
        (最小纟最大内点址距, 列表纟主线) = mins_(lambda 递归婪溟链:max(递归婪溟链.次大数址引讠内点址距), lambda 递归婪溟链:递归婪溟链.主线, 枚举冫递归婪溟链巛严序加链扌(加链))
            #先最大{@递归婪溟链}再最小{@加链}！
        return (最小纟最大内点址距, 列表纟主线)
    def 最小化乊尾四链冫最大内点址距乊加链扌(尾四链, /):
        (最小纟最大内点址距, 列表纟列表纟主线) = mins_(fst, snd, map(最大内点址距辻列表乊加链扌, sorted(set(map(mk_tuple, 尾四链)))))
        return (最小纟最大内点址距, 列表纟列表纟主线)
    def body_(ipath, ifile, 最大内点址距, 列表纟输出, 列表纟首峰值位, /):
        verbose and print_err(f'ipath: {ipath!r}')
        for line in ifile:
            (s4u, a, b) = _get_s4u_5line__verX_(line)
            verbose and print_err(f'靶值: {s4u!s}')
            (s4ussI, i, j) = get_s4uss_5line__verX_(line)
            uss = _repr2uss__verI_(s4ussI)
            尾六表 = uss
            assert len(尾六表) == 6
            尾四链 = 尾六表[2:]
            assert len(尾四链) == 4

            靶值 = int(s4u)
            if 靶值 == 1:
                continue
            (最小纟最大内点址距, 列表纟列表纟主线) = 最小化乊尾四链冫最大内点址距乊加链扌(尾四链)
            if 最小纟最大内点址距 < 最大内点址距:
                continue
            if 最小纟最大内点址距 > 最大内点址距:
                最大内点址距 = 最小纟最大内点址距
                列表纟输出 = []
                if 欤记录首峰值位:
                    列表纟首峰值位.append((最大内点址距, list(chains(列表纟列表纟主线))))
            列表纟输出.extend(chains(列表纟列表纟主线))
        return (最大内点址距, 列表纟输出)
    def main():
        列表纟首峰值位 = []
        最大内点址距 = 0
        列表纟输出 = [(1,)]
        for ipath in 列表纟输入文件路径冃靶值讠尾六表:
            with open(ipath, 'rt', encoding='ascii') as ifile:
                (最大内点址距, 列表纟输出) = body_(ipath, ifile, 最大内点址距, 列表纟输出, 列表纟首峰值位)
        总输出 = (最大内点址距, 列表纟输出) if not 欤记录首峰值位 else (最大内点址距, 列表纟输出, 列表纟首峰值位)
        if 欤趃输出:
            总输出 = chains([总输出[:1], *总输出[1:]])
        return 总输出
    return main()


##################




##################
##################
#move_to: view ../../python3_src/seed/for_libs/for_time.py
mk_rest_func_
##################
def 规范冫列表纟文件路径冃靶值讠简并记录扌(彣匹配模板纟前置文件路径冃靶值讠简并记录, 列表纟文件路径冃靶值讠简并记录, /):
    check_type_is(tuple, 列表纟文件路径冃靶值讠简并记录)
    #########
    (*前置列表纟文件路径冃靶值讠简并记录, 文件路径冃靶值讠简并记录) = 列表纟文件路径冃靶值讠简并记录
    777;0b00000 and print_err('verbose:', (前置列表纟文件路径冃靶值讠简并记录, 文件路径冃靶值讠简并记录, 彣匹配模板纟前置文件路径冃靶值讠简并记录))
    if 彣匹配模板纟前置文件路径冃靶值讠简并记录:
        if 前置列表纟文件路径冃靶值讠简并记录:raise TypeError(前置列表纟文件路径冃靶值讠简并记录, 彣匹配模板纟前置文件路径冃靶值讠简并记录)
        import pathlib, glob
        iopath = pathlib.Path(文件路径冃靶值讠简并记录)
        #.idir = pathlib.Path('.')
        #.前置列表纟文件路径冃靶值讠简并记录 = sorted(idir.glob(彣匹配模板纟前置文件路径冃靶值讠简并记录))
        #注意:iglob:乱序输出！
        ipaths = tuple(chains(sorted(glob.iglob(ptn)) for ptn in 彣匹配模板纟前置文件路径冃靶值讠简并记录.split(':|:')))
        #前置列表纟文件路径冃靶值讠简并记录 = sorted(set(ipaths))
        if not len(ipaths) == len(set(ipaths)):raise TypeError(彣匹配模板纟前置文件路径冃靶值讠简并记录, ipaths)
        前置列表纟文件路径冃靶值讠简并记录 = ipaths
        777;0b00000 and print_err('verbose:', (前置列表纟文件路径冃靶值讠简并记录, 文件路径冃靶值讠简并记录))
        if iopath.exists():
            if 前置列表纟文件路径冃靶值讠简并记录 and iopath.samefile(前置列表纟文件路径冃靶值讠简并记录[-1]):
                前置列表纟文件路径冃靶值讠简并记录.pop()
            for pre_ipath in 前置列表纟文件路径冃靶值讠简并记录:
                if iopath.samefile(pre_ipath):raise TypeError(iopath, pre_ipath)
        if not 'y' == input(f'ok?:{前置列表纟文件路径冃靶值讠简并记录}:{iopath!r}:{len(前置列表纟文件路径冃靶值讠简并记录)}+1:ok?(y):'):
            if 0:
                #需改变接口: -> may (xx, yy)
                print_err('abort')
                return
            raise Exception('abort')
        777;0b00000 and print_err('verbose:', (前置列表纟文件路径冃靶值讠简并记录, 文件路径冃靶值讠简并记录))
    前置列表纟文件路径冃靶值讠简并记录
    #########
    #前置列表纟文件路径冃靶值讠简并记录 = tuple(map(Path, 前置列表纟文件路径冃靶值讠简并记录))
    前置列表纟文件路径冃靶值讠简并记录 = tuple(前置列表纟文件路径冃靶值讠简并记录)
    check_paths_exist(前置列表纟文件路径冃靶值讠简并记录, all_files=True)
    文件路径冃靶值讠简并记录
    return (前置列表纟文件路径冃靶值讠简并记录, 文件路径冃靶值讠简并记录)
    #########
#.def 枚举生成冫文件后续简并记录纟递归婪溟链扌(文件路径冃靶值讠简并记录, /, *, ver, 休眠期=0.0):
def 枚举生成冫文件后续简并记录纟递归婪溟链扌(*列表纟文件路径冃靶值讠简并记录, ver, 休眠期=0.0, 苏醒期=2.0, 自顶向下搜索丷自底向上注册=False, 鬽最大靶值=None, 彣匹配模板纟前置文件路径冃靶值讠简并记录='', 欤最后一跃牜轻算随缘而止=False, 欤只保留首条最短加链乊各次大数=False, 欤允许缺失乊最后一跃=False, 欤允许追附乊最后一跃=False, 欤只保留后半段数据乊最后一跃乊自顶向下=False, 鬽最大靶值纟留空数据段纟最后一跃乊自顶向下=None, verbose=False):
    #@20260223:++kw:欤最后一跃牜轻算随缘而止:35035~>65536
    #@20260223:++kw:欤只保留首条最短加链乊各次大数
    #   :见:求冫丮最大差值辻靶值列表厈牜两倍次大数纟右侧最小最短加链之于靶值扌
    #@20260225:++kw:欤允许缺失乊最后一跃#乸异常牜最小显链长,乸失败记录
    #@20260225:++kw:欤允许追附乊最后一跃
    #@20260225:++kw:欤只保留后半段数据乊最后一跃乊自顶向下:内存不足，手机termux两次崩溃，考虑到 前半部分数据大概率无用，尝试省省
    if not 列表纟文件路径冃靶值讠简并记录:raise TypeError
    check_type_is(bool, 自顶向下搜索丷自底向上注册)
    check_type_in([float, str], 休眠期)
    check_int_ge_le(1, MAX_VERSION, ver)
    check_may_([check_int_ge, 1], 鬽最大靶值)
    check_type_is(str, 彣匹配模板纟前置文件路径冃靶值讠简并记录)
    check_type_is(bool, 欤最后一跃牜轻算随缘而止)
    check_type_is(bool, 欤只保留首条最短加链乊各次大数)
    check_type_is(bool, 欤允许缺失乊最后一跃)
    check_type_is(bool, 欤允许追附乊最后一跃)
    check_type_is(bool, 欤只保留后半段数据乊最后一跃乊自顶向下)
    check_may_([check_int_ge, 1], 鬽最大靶值纟留空数据段纟最后一跃乊自顶向下)

    if 欤只保留首条最短加链乊各次大数 and not 欤最后一跃牜轻算随缘而止:raise TypeError
    if 欤允许缺失乊最后一跃 and not 欤最后一跃牜轻算随缘而止:raise TypeError
    if 欤允许追附乊最后一跃 and not 欤最后一跃牜轻算随缘而止:raise TypeError
    if 欤只保留后半段数据乊最后一跃乊自顶向下 and not 欤最后一跃牜轻算随缘而止:raise TypeError
    if 欤只保留后半段数据乊最后一跃乊自顶向下 and 自顶向下搜索丷自底向上注册:raise TypeError
    if 欤只保留后半段数据乊最后一跃乊自顶向下:raise TypeError('无法实现:删除前半段数据，则 简并态牜精深版 搜索 无法进行#可以考虑删除后半段数据{最后一跃部分}')
    if 鬽最大靶值纟留空数据段纟最后一跃乊自顶向下 and not 欤最后一跃牜轻算随缘而止:raise TypeError
    if 鬽最大靶值纟留空数据段纟最后一跃乊自顶向下 and 自顶向下搜索丷自底向上注册:raise TypeError

    #########
    _rest = mk_rest_func_(休眠期, 苏醒期)
    #########
    (前置列表纟文件路径冃靶值讠简并记录, 文件路径冃靶值讠简并记录) = 规范冫列表纟文件路径冃靶值讠简并记录扌(彣匹配模板纟前置文件路径冃靶值讠简并记录, 列表纟文件路径冃靶值讠简并记录)
    #########
    omode = 'at+' if (not 欤最后一跃牜轻算随缘而止) or 欤允许追附乊最后一跃 else 'xt+'
    with open(文件路径冃靶值讠简并记录, omode, encoding='ascii') as iofile:
        起点 = iofile.tell()
        iofile.seek(0)
        靶值讠简并记录 = 加载冫数据扌(iofile, ver=ver, pre_ipaths=前置列表纟文件路径冃靶值讠简并记录, 鬽最大靶值=鬽最大靶值, 欤只保留后半段数据乊最后一跃乊自顶向下=欤只保留后半段数据乊最后一跃乊自顶向下, 鬽最大靶值纟留空数据段纟最后一跃乊自顶向下=鬽最大靶值纟留空数据段纟最后一跃乊自顶向下, verbose=verbose)
            #^乸异常牜最大靶值
        assert 起点 == iofile.tell()
        assert None is 鬽最大靶值 or -1+len(靶值讠简并记录) < 鬽最大靶值
        777;_rest()
        枚举冫后续简并记录纟递归婪溟链牜囜囜囜扌 = 枚举冫后续简并记录纟递归婪溟链牜自顶向下搜索扌 if not 自顶向下搜索丷自底向上注册 else 枚举冫后续简并记录纟递归婪溟链牜自底向上注册扌
        for 简并记录 in 枚举冫后续简并记录纟递归婪溟链牜囜囜囜扌(靶值讠简并记录, 鬽最大靶值=鬽最大靶值, 欤最后一跃牜轻算随缘而止=欤最后一跃牜轻算随缘而止, 欤只保留首条最短加链乊各次大数=欤只保留首条最短加链乊各次大数, 欤允许缺失乊最后一跃=欤允许缺失乊最后一跃, 欤只保留后半段数据乊最后一跃乊自顶向下=欤只保留后半段数据乊最后一跃乊自顶向下, 鬽最大靶值纟留空数据段纟最后一跃乊自顶向下=鬽最大靶值纟留空数据段纟最后一跃乊自顶向下):
            if 欤允许缺失乊最后一跃 and type(简并记录) is 乸失败记录:
                #缺失
                失败记录 = 简并记录
                靶值 = 失败记录.病简并记录.靶值
                s = 失败记录.to_str(ver=ver)
            else:
                靶值 = 简并记录.靶值
                s = 简并记录.to_str(ver=ver)
            靶值, s
            assert 1+靶值 == len(靶值讠简并记录)
            777;print(s, file=iofile)
            777;yield s
            #if 靶值 == 鬽最大靶值: return
            777;_rest()
def 枚举冫后续简并记录纟递归婪溟链牜自顶向下搜索扌(靶值讠简并记录, /, *, 鬽最大靶值, 欤最后一跃牜轻算随缘而止, 欤只保留首条最短加链乊各次大数, 欤允许缺失乊最后一跃, 欤只保留后半段数据乊最后一跃乊自顶向下, 鬽最大靶值纟留空数据段纟最后一跃乊自顶向下):
    '-> Iter (失败记录|简并记录)'
    777;0b00001 and print_err('自顶向下搜索')
    777;0b00001 and 欤最后一跃牜轻算随缘而止 and print_err('欤最后一跃牜轻算随缘而止')
    777;0b00001 and 欤只保留首条最短加链乊各次大数 and print_err('欤只保留首条最短加链乊各次大数')
    777;0b00001 and 欤允许缺失乊最后一跃 and print_err('欤允许缺失乊最后一跃')
    777;0b00001 and 欤只保留后半段数据乊最后一跃乊自顶向下 and print_err('欤只保留后半段数据乊最后一跃乊自顶向下')
    777;0b00001 and 鬽最大靶值纟留空数据段纟最后一跃乊自顶向下 and print_err('鬽最大靶值纟留空数据段纟最后一跃乊自顶向下')
    欤允许空洞数据乊最后一跃乊自顶向下 = bool(欤只保留后半段数据乊最后一跃乊自顶向下 or 鬽最大靶值纟留空数据段纟最后一跃乊自顶向下)

    if not len(靶值讠简并记录):raise TypeError
    check_may_([check_int_ge, len(靶值讠简并记录)], 鬽最大靶值)

    #raise 暂停使用冫自顶向下搜索-'TODO:++kw:欤最后一跃牜轻算随缘而止'
    000
    if not 鬽最大靶值 is None and 鬽最大靶值 < len(靶值讠简并记录): return
    while 1:
        lazy_next = lambda:求冫后续简并记录纟递归婪溟链牜自顶向下搜索扌(靶值讠简并记录, 欤最后一跃牜轻算随缘而止, 欤只保留首条最短加链乊各次大数, 欤允许缺失乊最后一跃, 欤允许空洞数据乊最后一跃乊自顶向下)
        b_stop = yield from _main_loop_body(lazy_next, 靶值讠简并记录, 鬽最大靶值, 欤允许缺失乊最后一跃)
        if b_stop: return

def _main_loop_body(lazy_next, 靶值讠简并记录, 鬽最大靶值, 欤允许缺失乊最后一跃, /):
    '-> Iter (失败记录|简并记录){return b_stop}'
    try:
        简并记录 = lazy_next()
            #^乸异常牜最小显链长
    except 乸异常牜最小显链长 as exc:
        if 欤允许缺失乊最后一跃:
            #.(病简并记录, 真最小显链长) = exc.args
            #.失败记录 = 乸失败记录('fail:', 病简并记录.靶值, 病简并记录.最小显链长, 病简并记录.to_str(ver=ver), 真最小显链长)
            #.失败记录 = 乸失败记录(病简并记录, 真最小显链长)
            #.[失败记录] = exc.args
            失败记录 = exc.失败记录
            (病简并记录, 真最小显链长) = 失败记录
            assert 病简并记录.靶值 == len(靶值讠简并记录)
            靶值讠简并记录.append(失败记录)
            yield 失败记录
            return 病简并记录.靶值 == 鬽最大靶值
            #.if 病简并记录.靶值 == 鬽最大靶值: return True
            #.return False # continue
        raise
    简并记录
    assert 简并记录.靶值 == len(靶值讠简并记录)
    靶值讠简并记录.append(简并记录)
    yield 简并记录
    return 简并记录.靶值 == 鬽最大靶值
    #.if 简并记录.靶值 == 鬽最大靶值: return True
    #.return False # continue


def 求冫后续简并记录纟递归婪溟链牜自顶向下搜索扌(靶值讠简并记录, 欤最后一跃牜轻算随缘而止, 欤只保留首条最短加链乊各次大数, 欤允许缺失乊最后一跃, 欤允许空洞数据乊最后一跃乊自顶向下, /):
    '-> 简并记录纟靶值 | ^乸异常牜最小显链长'
    assert 靶值讠简并记录
    靶值 = len(靶值讠简并记录)
    if 靶值 == 1:
        return 构造冫简并记录纟靶值一扌()
    (最小显链长纟靶值, 次大数讠溟次) = _求冫丮最小显链长辻次大数讠溟次厈乊后续简并记录纟递归婪溟链牜靶值大于一牜自顶向下搜索扌(靶值讠简并记录, 靶值, 欤允许缺失乊最后一跃, 欤允许空洞数据乊最后一跃乊自顶向下)
    777;伪简并集纟靶值 = make_NonTouchRanges([(1, 1+靶值)])
    777;伪简并记录纟靶值 = _乸简并记录纟递归婪溟链(靶值, 最小显链长纟靶值, len(次大数讠溟次), 伪简并集纟靶值.len_ints(), 次大数讠溟次, 伪简并集纟靶值, None, None, None, None, None, None)
    777;靶值讠简并记录.append(伪简并记录纟靶值)
    try:
        (简并集纟靶值, 下上界, 左右小大) = _过滤乊内点集扌(靶值讠简并记录, 靶值, (), 欤最后一跃牜轻算随缘而止, 欤只保留首条最短加链乊各次大数)
    finally:
        if not 靶值讠简并记录.pop() is 伪简并记录纟靶值:raise 000
    (最短加链位置讠下界, 最短加链位置讠上界) = 下上界
    (最短加链牜左侧最小, 最短加链牜左侧最大, 最短加链牜右侧最小, 最短加链牜右侧最大) = 左右小大
    简并集纟靶值 = _转换集合扌(简并集纟靶值)
    #.777;0b00001 and print_err(靶值, 简并集纟靶值)
    简并记录纟靶值 = 乸简并记录纟递归婪溟链(靶值, 最小显链长纟靶值, len(次大数讠溟次), 简并集纟靶值.len_ints(), 次大数讠溟次, 简并集纟靶值, 最短加链位置讠下界, 最短加链位置讠上界, 最短加链牜左侧最小, 最短加链牜左侧最大, 最短加链牜右侧最小, 最短加链牜右侧最大)
        # ^乸异常牜最小显链长
    #:if 0b00001:
    #:    #:    # ^AssertionError: (15, 5, 5, 10, FD({3: 2, 5: 1, 9: 0, 10: 0, 12: 0}), RT({1: 6, 9: 2, 12: 1, 15: 1}), [1, 2, 3, 5, 9, 15], [1, 2, 4, 6, 12, 15], [1, 2, 3, 5, 10, 15], [1, 2, 4, 5, 10, 15], [1, 2, 3, 6, 9, 15], [1, 2, 3, 6, 12, 15])
    #:    assert 最短加链位置讠上界 == 最短加链牜右侧最大, 简并记录纟靶值.to_str(ver=ver)
    #:    assert 最短加链位置讠上界 == 最短加链牜左侧最大, 简并记录纟靶值.to_str(ver=ver)
    return 简并记录纟靶值

    #bug:最短加链:缺失:内点*2**ez
    #.s = {靶值}
    #.ss = []
    #.lus = []
    #.lrs = []
    #.for 次大数, 溟次 in 次大数讠溟次.items():
    #.    内点 = (靶值 -次大数) >> 溟次
    #.    777;s.update(内点<<ez for ez in range(1, 1+溟次))
    #.    (简并集纟次大数乊内点, 下上界, 左右小大) = _过滤乊内点集扌(靶值讠简并记录, 次大数, {内点})
    #.    #简并集纟靶值乊次大数
    #.    ss.append(简并集纟次大数乊内点)
    #.    lus.append(下上界)
    #.    lrs.append(左右小大)
    #.s, ss, lus, lrs
    #.简并集纟靶值 = _集合并扌(s, ss)
    #.下上界 = _求冫下上界扌(靶值, lus)
    #.左右小大 = _求冫左右小大扌(靶值, lrs)
    #.(最短加链位置讠下界, 最短加链位置讠上界) = 下上界
    #.(最短加链牜左侧最小, 最短加链牜左侧最大, 最短加链牜右侧最小, 最短加链牜右侧最大) = 左右小大
    #.简并记录纟靶值 = 乸简并记录纟递归婪溟链(靶值, 最小显链长纟靶值, len(次大数讠溟次), 简并集纟靶值.len_ints(), 次大数讠溟次, 简并集纟靶值, 最短加链位置讠下界, 最短加链位置讠上界, 最短加链牜左侧最小, 最短加链牜左侧最大, 最短加链牜右侧最小, 最短加链牜右侧最大)
    #.return 简并记录纟靶值
def _求冫丮最小显链长辻次大数讠溟次厈乊后续简并记录纟递归婪溟链牜靶值大于一牜自顶向下搜索扌(靶值讠简并记录, 靶值, 欤允许缺失乊最后一跃, 欤允许空洞数据乊最后一跃乊自顶向下, /):
    #DONE:由 自顶向下搜索 改为 自底向上注册
    #   _求冫丮最小显链长辻次大数讠溟次厈乊后续简并记录纟递归婪溟链牜靶值大于一牜自底向上注册扌
    assert 靶值 >= 2
    最小显链长纟靶值 = 1+靶值
    777;次大数讠溟次 = None
    for 次大数 in reversed(range(1, 靶值)):
        溟化值 = 靶值 -次大数
        简并记录纟次大数 = 靶值讠简并记录[次大数]
        if 欤允许缺失乊最后一跃 and type(简并记录纟次大数) is 乸失败记录:
            #缺失
            continue
        if 欤允许空洞数据乊最后一跃乊自顶向下 and 简并记录纟次大数 is DELETED:
            #已删除
            continue
        简并集纟次大数 = 简并记录纟次大数.简并集
        最小显链长纟次大数 = 简并记录纟次大数.最小显链长

        欤成功 = False
        内点 = 溟化值
        for 溟次 in range(最小显链长纟靶值 -最小显链长纟次大数):
            if 内点 <= 次大数 and 内点 in 简并集纟次大数:
                欤成功 = True
                break
            if 内点 & 1:
                break
            内点 >>= 1
        if not 欤成功:
            continue
        #########
        # [:约束牜定义冫递归婪溟链]:goto
        assert 靶值 == 次大数 + (内点<<溟次)
        assert 内点 in 简并集纟次大数
        显链长纟靶值 = 最小显链长纟次大数 +1 +溟次
        #########
        assert 显链长纟靶值 <= 最小显链长纟靶值
        if 显链长纟靶值 == 最小显链长纟靶值:
            次大数讠溟次[次大数] = 溟次
        elif 显链长纟靶值 < 最小显链长纟靶值:
            最小显链长纟靶值 = 显链长纟靶值
            次大数讠溟次 = {次大数:溟次}
        else:
            raise 000
    次大数讠溟次
    if not 次大数讠溟次:raise Exception('次大数讠溟次 empty @靶值=', 靶值) #鬽最大靶值纟留空数据段纟最后一跃乊自顶向下/欤允许空洞数据乊最后一跃乊自顶向下
    assert 最小显链长纟靶值 < 靶值
    return (最小显链长纟靶值, 次大数讠溟次)

def 枚举冫首条最短加链乊各次大数扌(靶值讠简并记录, 靶值, /):
    return 枚举冫最短加链乊内点集扌(靶值讠简并记录, 靶值, 内点集:='', 欤只保留首条最短加链乊各次大数=True)
def 枚举冫最短加链乊内点集扌(靶值讠简并记录, 靶值, 内点集, /, *, 欤只保留首条最短加链乊各次大数):
    L = 1 + 靶值讠简并记录[靶值].最小显链长
    us = []         #部分纟最短加链
    ns = set(内点集)#内点集#过滤器
    ns.discard(靶值)
    def _f1(u, /):
        assert not u in ns
        us.append(u)
        if u == 1:
            #assert not ns, (us, ns)
            #   ^AssertionError: ([11, 6, 5, 2, 4, 1], {3})
            #       5 1 2 1 True {1} {3} [11, 6, 5, 2, 4, 1]
            #       11 5 1 3 True set() {3} [11, 6, 5, 2, 4, 1]
            if not ns:
                最短加链 = reverse_(us)
                最短加链.sort()
                assert L == len(最短加链)
                yield tuple(最短加链)
            else:
                pass#<<==us.pop()
            #bug:if ns:return
        else:
            yield from _f2(u)
        us.pop()
    def _f2(靶值, /):
        nonlocal us, ns
        assert 靶值 > 1
        简并记录 = 靶值讠简并记录[靶值]
        s = 简并记录.简并集
        #if not all(n in s for n in ns):
        if (_ns:=sorted(ns, reverse=True)) and not (_ns[0] <= 靶值 and all(n in s for n in _ns)):
            return
        sz4us = len(us)
        sz4ns = len(ns)
        _f1_f3 = _f3#_f1
        for 次大数, 溟次 in 简并记录.次大数讠溟次.items():
            内点 = (靶值 -次大数) >> 溟次
            777;ls = [内点<<ez for ez in range(1, 1+溟次)]
            777;s = {次大数, *ls}
            # [[次大数==内点]<->[内点 in s]]
            777;b = not 内点 in ns
            if b:ns.add(内点)
            #次序不可颠倒<<== 可能[内点==次大数]
            777;delta = {n for n in s if n in ns}
            # !! [内点 in ns]
            # [[次大数==内点]<->[内点 in delta]]
            #777;delta = s & ns
            ns -= delta
            # [[次大数==内点]<->[not 内点 in ns]]
            if ls:us += ls
            try:
                777;yield from _f1_f3(次大数)
            #bug:except:
                # !! GeneratorExit@欤最后一跃牜轻算随缘而止
            except Exception as exc:
                777;0b00001 and print_err('@枚举冫最短加链乊内点集扌', (靶值, 次大数, 溟次, 内点, b, delta, ns, us, exc))
                    #5 1 2 1 True {1} {3} [11, 6, 5, 2, 4, 1]
                    #11 5 1 3 True set() {3} [11, 6, 5, 2, 4, 1]
                raise
            if ls:del us[-len(ls):]
            # [[次大数==内点]<->[not 内点 in ns]]
            ns |= delta
            # !! [[次大数==内点]<->[内点 in delta]]
            # [内点 in ns]
            try:
                if b:ns.remove(内点)
            except KeyError:
                print_err((靶值, 次大数, 溟次, us, ns, ls))
                    #+欤只保留首条最短加链乊各次大数:{必须重置全局参数}:(531, 19, 5, [531, 32, 64, 128, 256, 512, 19, 17], set(), [32, 64, 128, 256, 512])
                raise
            assert sz4ns == len(ns)
            assert sz4us == len(us)
    def _f3(靶值, /):
        '仅用于:次大数:+欤只保留首条最短加链乊各次大数'
        nonlocal _f3
        _f3 = _f1
        #return _f3(靶值)
        _us = us.copy()
        _ns = ns.copy()
        for ls in _f3(靶值):
            yield ls
            #必须重置全局参数
            us[:] = _us
            ns.clear();ns.update(_ns)
            break
        return
    if not 欤只保留首条最短加链乊各次大数:
        _f3 = _f1

    return _f1(靶值)
def _过滤乊内点集扌(靶值讠简并记录, 靶值, 内点集, 欤最后一跃牜轻算随缘而止, 欤只保留首条最短加链乊各次大数, /):
    r'''[[[
+欤最后一跃牜轻算随缘而止,-欤只保留首条最短加链乊各次大数:
发现计算结果不同{只保留首条最短加链}:why?? 1097 vs 1103
    可能是:topdown:bypass:部分计算直接使用 次大数讠溟次, 而 内点集 只含 一条 最短加链 不能 涵盖所有 次大数讠溟次
    [1..=530] ==>> bottomup.last_leap[531..<1097]
    [1..=530] ==>> topdown.last_leap[531..<1103]
=>:++kw:欤只保留首条最短加链乊各次大数
    now:计算结果不同{只保留首条最短加链乊各次大数}:1335
    [1..=530] ==>> bottomup.last_leap.multi[531..<1335]
    [1..=530] ==>> topdown.last_leap.multi[531..<1335]
===
实战结果不理想:
    [1..=35035] ==>> topdown.last_leap.multi[35036..<37726]
===
    #]]]'''#'''
    #if 欤最后一跃牜轻算随缘而止 and 内点集:raise NotImplementedError
    it = 枚举冫最短加链乊内点集扌(靶值讠简并记录, 靶值, 内点集, 欤只保留首条最短加链乊各次大数=欤只保留首条最短加链乊各次大数)
    最短加链 = next(it)
    if 欤最后一跃牜轻算随缘而止 and not 欤只保留首条最短加链乊各次大数:
        #只保留首条最短加链
        it = iter([])
    it
    最短加链位置讠下界 = 最短加链
    最短加链位置讠上界 = 最短加链
    最短加链牜左侧最小 = 最短加链
    最短加链牜左侧最大 = 最短加链
    反转后最短加链 = reverse_(最短加链)
    反转后最短加链牜右侧最小 = 反转后最短加链
    反转后最短加链牜右侧最大 = 反转后最短加链
    s = set(最短加链)
    for 最短加链 in it:
        s.update(最短加链)
        最短加链位置讠下界 = tuple(map(min, 最短加链位置讠下界, 最短加链))
        最短加链位置讠上界 = tuple(map(max, 最短加链位置讠上界, 最短加链))

        最短加链牜左侧最小 = min(最短加链牜左侧最小, 最短加链)
        最短加链牜左侧最大 = max(最短加链牜左侧最大, 最短加链)

        反转后最短加链 = reverse_(最短加链)
        反转后最短加链牜右侧最小 = min(反转后最短加链牜右侧最小, 反转后最短加链)
        反转后最短加链牜右侧最大 = max(反转后最短加链牜右侧最大, 反转后最短加链)
    最短加链牜右侧最小 = reverse_(反转后最短加链牜右侧最小)
    最短加链牜右侧最大 = reverse_(反转后最短加链牜右侧最大)

    下上界 = (最短加链位置讠下界, 最短加链位置讠上界)
    左右小大 = (最短加链牜左侧最小, 最短加链牜左侧最大, 最短加链牜右侧最小, 最短加链牜右侧最大)
    简并集纟靶值乊内点集 = s
    return (简并集纟靶值乊内点集, 下上界, 左右小大)
def _转换集合扌(s, /):
    简并集纟靶值 = make_NonTouchRanges(sorted_ints_to_iter_nontouch_ranges(sorted(s)))
    return 简并集纟靶值
def _集合并扌(s, ss, /):
    s = set(s)
    s.union(*ss)
    简并集纟靶值 = _转换集合扌(s)
    return 简并集纟靶值
def _求冫下上界扌(靶值, lus, /):
    (下界, 上界) = lus[0]
    for (_下界, _上界) in lus:
        下界 = tuple(map(min, 下界, _下界))
        上界 = tuple(map(max, 上界, _上界))
    下界 += (靶值,)
    上界 += (靶值,)
    下上界 = (下界, 上界)
    return 下上界
def _求冫左右小大扌(靶值, lrs, /):
    (左侧最小, 左侧最大, 右侧最小, 右侧最大) = lrs[0]
    反转后右侧最小 = reverse_(右侧最小)
    反转后右侧最大 = reverse_(右侧最大)
    for (_左侧最小, _左侧最大, _右侧最小, _右侧最大) in lrs:
        _反转后右侧最小 = reverse_(_右侧最小)
        _反转后右侧最大 = reverse_(_右侧最大)

        左侧最小 = min(左侧最小, _左侧最小)
        左侧最大 = max(左侧最大, _左侧最大)

        反转后右侧最小 = min(反转后右侧最小, _反转后右侧最小)
        反转后右侧最大 = max(反转后右侧最大, _反转后右侧最大)
    #左侧最小 = 左侧最小.copy()
    #左侧最大 = 左侧最大.copy()
    右侧最小 = reverse_(反转后右侧最小)
    右侧最大 = reverse_(反转后右侧最大)
    左右小大 = (左侧最小, 左侧最大, 右侧最小, 右侧最大)
    return 左右小大








def _求冫丮最小显链长辻次大数讠溟次厈乊后续简并记录纟递归婪溟链牜靶值大于一牜自底向上注册扌(靶值讠简并记录, 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈, /):
    靶值 = len(靶值讠简并记录)
    assert 靶值 >= 2
    最小显链长纟靶值 = min(d:=靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈[靶值])
    ls = d[最小显链长纟靶值]
    次大数讠溟次 = {次大数:溟次 for (次大数,内点,溟次) in ls}
    return (最小显链长纟靶值, 次大数讠溟次)
def 后续更新冫靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈乊已有后续简并记录纟递归婪溟链牜靶值大于一扌(靶值讠简并记录, 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈, 简并记录纟当前靶值, 鬽最大靶值, /):
    当前靶值 = len(靶值讠简并记录)
    assert 当前靶值 >= 2
    assert 当前靶值 == 简并记录纟当前靶值.靶值, 当前靶值
    _mdu = 当前靶值<<1
    最大靶值 = _mdu if None is 鬽最大靶值 else min(_mdu, 鬽最大靶值)
    assert 2 <= 当前靶值 <= 最大靶值

    u2szmm2ls = 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈
    #########
    d = u2szmm2ls.pop(当前靶值)
    for 显链长, ls in d.items():
        _显链长 = 1+显链长
        for (次大数,内点,溟次) in ls:
            _溟次 = 1+溟次
            _靶值 = 次大数 + (内点<<_溟次)
            if _靶值 <= 最大靶值:
                u2szmm2ls.setdefault(_靶值, {}).setdefault(_显链长, []).append((次大数,内点,_溟次))
    u2szmm2ls

    #########
    次大数 = 当前靶值
    _溟次 = 0
    _显链长 = 1+简并记录纟当前靶值.最小显链长
    for 内点 in 简并记录纟当前靶值.简并集.iter_ints():
        _靶值 = 次大数 + (内点<<_溟次)
        if _靶值 <= 最大靶值:
            u2szmm2ls.setdefault(_靶值, {}).setdefault(_显链长, []).append((次大数,内点,_溟次))
        else:
            break
    u2szmm2ls
    #########
    assert not 当前靶值 in 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈
    assert ((1+当前靶值) in 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈)  is  (not 鬽最大靶值 == 当前靶值), (鬽最大靶值, 当前靶值, sorted(靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈), ((1+当前靶值) in 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈),  (not 鬽最大靶值 == 当前靶值))
    #########
    return None
def 初始化构造冫靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈乊后续简并记录纟递归婪溟链牜靶值大于一扌(靶值讠简并记录, /, *, 鬽最大靶值):
    if not len(靶值讠简并记录):raise TypeError
    check_may_([check_int_ge, len(靶值讠简并记录)], 鬽最大靶值)

    当前靶值 = len(靶值讠简并记录)
    assert 当前靶值 >= 2
    _mdu = 当前靶值<<1
    最大靶值 = _mdu if None is 鬽最大靶值 else min(_mdu, 鬽最大靶值)
    assert 2 <= 当前靶值 <= 最大靶值

    u2szmm2ls = 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈 = {}
    it = enumerate(靶值讠简并记录)
    777;next(it)
    for 次大数, 简并记录纟次大数 in it:
        最小显链长纟次大数 = 简并记录纟次大数.最小显链长
        差距 = 当前靶值 -次大数
        溟次 = 0
        777;显链长 = 最小显链长纟次大数+1+溟次
        for 内点 in 简并记录纟次大数.简并集.iter_ints_(reverse=True):
            溟化值 = 内点 << 溟次
            欤更新溟次 = False
            while 溟化值 < 差距:
                欤更新溟次 = True
                溟次 += 1
                溟化值 <<= 1
            if 欤更新溟次:
                assert 溟化值 == 内点 << 溟次
                777;显链长 = 最小显链长纟次大数+1+溟次
            靶值 = 次大数 +溟化值
            assert 靶值 >= 当前靶值
            if 欤更新溟次:
                assert 次大数+(溟化值>>1) < 当前靶值
            if 靶值 <= 最大靶值:
                u2szmm2ls.setdefault(靶值, {}).setdefault(显链长, []).append((次大数,内点,溟次))
    u2szmm2ls

    assert min(靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈) == 当前靶值
    return 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈

def 求冫后续简并记录纟递归婪溟链牜自底向上注册扌(靶值讠简并记录, 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈, 鬽最大靶值, 欤最后一跃牜轻算随缘而止, 欤只保留首条最短加链乊各次大数, 欤允许缺失乊最后一跃, /):
    '-> 简并记录纟靶值 | ^乸异常牜最小显链长'
    assert 靶值讠简并记录
    靶值 = len(靶值讠简并记录)
    if 靶值 == 1:
        assert not 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈
        #.简并记录纟靶值 = 构造冫简并记录纟靶值一扌()
        #.return (简并记录纟靶值, 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈)
        return 构造冫简并记录纟靶值一扌()
    (最小显链长纟靶值, 次大数讠溟次) = _求冫丮最小显链长辻次大数讠溟次厈乊后续简并记录纟递归婪溟链牜靶值大于一牜自底向上注册扌(靶值讠简并记录, 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈)
    777;伪简并集纟靶值 = make_NonTouchRanges([(1, 1+靶值)])
    777;伪简并记录纟靶值 = _乸简并记录纟递归婪溟链(靶值, 最小显链长纟靶值, len(次大数讠溟次), 伪简并集纟靶值.len_ints(), 次大数讠溟次, 伪简并集纟靶值, None, None, None, None, None, None)
    777;靶值讠简并记录.append(伪简并记录纟靶值)
    try:
        (简并集纟靶值, 下上界, 左右小大) = _过滤乊内点集扌(靶值讠简并记录, 靶值, (), 欤最后一跃牜轻算随缘而止, 欤只保留首条最短加链乊各次大数)
    finally:
        if not 靶值讠简并记录.pop() is 伪简并记录纟靶值:raise 000
    (最短加链位置讠下界, 最短加链位置讠上界) = 下上界
    (最短加链牜左侧最小, 最短加链牜左侧最大, 最短加链牜右侧最小, 最短加链牜右侧最大) = 左右小大
    简并集纟靶值 = _转换集合扌(简并集纟靶值)
    #.777;0b00001 and print_err(靶值, 简并集纟靶值)
    简并记录纟靶值 = 乸简并记录纟递归婪溟链(靶值, 最小显链长纟靶值, len(次大数讠溟次), 简并集纟靶值.len_ints(), 次大数讠溟次, 简并集纟靶值, 最短加链位置讠下界, 最短加链位置讠上界, 最短加链牜左侧最小, 最短加链牜左侧最大, 最短加链牜右侧最小, 最短加链牜右侧最大)
        # ^乸异常牜最小显链长
    777;后续更新冫靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈乊已有后续简并记录纟递归婪溟链牜靶值大于一扌(靶值讠简并记录, 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈, 简并记录纟靶值, 鬽最大靶值)
    #.return (简并记录纟靶值, 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈)
    return 简并记录纟靶值

def 枚举冫后续简并记录纟递归婪溟链牜自底向上注册扌(靶值讠简并记录, 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈=None, /, *, 鬽最大靶值, 欤最后一跃牜轻算随缘而止, 欤只保留首条最短加链乊各次大数, 欤允许缺失乊最后一跃, 欤只保留后半段数据乊最后一跃乊自顶向下, 鬽最大靶值纟留空数据段纟最后一跃乊自顶向下):
    '-> Iter (失败记录|简并记录)'
    777;0b00001 and print_err('自底向上注册')
    777;0b00001 and 欤最后一跃牜轻算随缘而止 and print_err('欤最后一跃牜轻算随缘而止')
    777;0b00001 and 欤只保留首条最短加链乊各次大数 and print_err('欤只保留首条最短加链乊各次大数')
    777;0b00001 and 欤允许缺失乊最后一跃 and print_err('欤允许缺失乊最后一跃')
    if 欤只保留后半段数据乊最后一跃乊自顶向下:raise TypeError
    if 鬽最大靶值纟留空数据段纟最后一跃乊自顶向下:raise TypeError

    if not (None is 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈 or 1 <= len(靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈)):raise TypeError

    if not len(靶值讠简并记录):raise TypeError
    check_may_([check_int_ge, len(靶值讠简并记录)], 鬽最大靶值)

    def nop(): pass
    def to_init_():
        nonlocal to_init_, 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈
        if None is 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈:
            if len(靶值讠简并记录) >= 2:
                靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈 = 初始化构造冫靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈乊后续简并记录纟递归婪溟链牜靶值大于一扌(靶值讠简并记录, 鬽最大靶值=鬽最大靶值)
                777;to_init_ = nop
            else:
                assert not to_init_ is nop
                assert None is 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈
                pass
        else:
            assert len(靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈)
            777;to_init_ = nop
    #end-def to_init_():
    if not 鬽最大靶值 is None and 鬽最大靶值 < len(靶值讠简并记录): return
    while 1:
        to_init_()
        lazy_next = lambda:求冫后续简并记录纟递归婪溟链牜自底向上注册扌(靶值讠简并记录, 靶值讠显链长讠列表纟丮次大数丶内点丶溟次厈, 鬽最大靶值, 欤最后一跃牜轻算随缘而止, 欤只保留首条最短加链乊各次大数, 欤允许缺失乊最后一跃)
        b_stop = yield from _main_loop_body(lazy_next, 靶值讠简并记录, 鬽最大靶值, 欤允许缺失乊最后一跃)
        if b_stop: return






__all__
from seed.math.power.addition_chain.shortest.mixed_recursive_greedy_zpow_addition_chain import *
