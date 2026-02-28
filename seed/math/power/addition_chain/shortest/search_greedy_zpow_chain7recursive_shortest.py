#:__all__:goto
#bug:毛病冫内点概念应用:goto
#   『内点』 的 使用有误: 根据 最小显链长差值 倒推出来的 未必是 内点，有可能是 溟化值，由于 可能是主干值或支线值，所以才需要 简并集 判定
#   doing...
r'''[[[
e ../../python3_src/seed/math/power/addition_chain/shortest/search_greedy_zpow_chain7recursive_shortest.py
    婪溟链牜递归最短:搜索{通过:靶值讠最小显链长}
vs:
    view ../../python3_src/seed/math/power/addition_chain/shortest/search_star_chain7recursive_shortest.py
        加星链牜递归最短:搜索{通过:靶值讠最小显链长}
        [加星链牜递归最短<:婪溟链牜递归最短]
    view ../../python3_src/seed/math/power/addition_chain/shortest/mixed_recursive_greedy_zpow_addition_chain.py
        婪溟链牜递归最短:搜索{通过:简并态}

seed.math.power.addition_chain.shortest.search_greedy_zpow_chain7recursive_shortest
py -m nn_ns.app.debug_cmd   seed.math.power.addition_chain.shortest.search_greedy_zpow_chain7recursive_shortest -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.power.addition_chain.shortest.search_greedy_zpow_chain7recursive_shortest:__doc__ -ht # -ff -df
#######

[[
代码模板:
view ../../python3_src/seed/math/power/addition_chain/shortest/search_star_chain7recursive_shortest.py
]]


'#'; __doc__ = r'#'
>>>



[[
py_adhoc_call   seed.math.power.addition_chain.shortest.search_greedy_zpow_chain7recursive_shortest   ,枚举冫婪溟链牜递归最短巛靶值扌 +欤次大数降序 =12509 +欤带主线
    ((1, 2, 4, 8, 12, 13, 781, 1562, 3124, 6248, 12496, 12509), (1, 2, 4, 8, 12, 13, 24, 48, 96, 192, 384, 768, 781, 1562, 3124, 6248, 12496, 12509))
    ((1, 2, 4, 6, 12, 13, 781, 1562, 3124, 6248, 12496, 12509), (1, 2, 4, 6, 12, 13, 24, 48, 96, 192, 384, 768, 781, 1562, 3124, 6248, 12496, 12509))
    ((1, 2, 3, 6, 12, 13, 781, 1562, 3124, 6248, 12496, 12509), (1, 2, 3, 6, 12, 13, 24, 48, 96, 192, 384, 768, 781, 1562, 3124, 6248, 12496, 12509))
    ((1, 3, 6, 12, 13, 781, 1562, 3124, 6248, 12496, 12509), (1, 2, 3, 6, 12, 13, 24, 48, 96, 192, 384, 768, 781, 1562, 3124, 6248, 12496, 12509))
    ((1, 2, 6, 12, 13, 781, 1562, 3124, 6248, 12496, 12509), (1, 2, 4, 6, 12, 13, 24, 48, 96, 192, 384, 768, 781, 1562, 3124, 6248, 12496, 12509))
    ((1, 2, 4, 12, 13, 781, 1562, 3124, 6248, 12496, 12509), (1, 2, 4, 8, 12, 13, 24, 48, 96, 192, 384, 768, 781, 1562, 3124, 6248, 12496, 12509))
    ((1, 2, 4, 8, 16, 17, 1041, 2082, 4164, 8328, 12492, 12509), (1, 2, 4, 8, 16, 17, 32, 64, 128, 256, 512, 1024, 1041, 2082, 4164, 8328, 12492, 12509))
    ((1, 2, 4, 8, 16, 17, 1041, 2082, 4164, 6246, 12492, 12509), (1, 2, 4, 8, 16, 17, 32, 64, 128, 256, 512, 1024, 1041, 2082, 4164, 6246, 12492, 12509))
    ((1, 2, 4, 8, 16, 17, 1041, 2082, 3123, 6246, 12492, 12509), (1, 2, 4, 8, 16, 17, 32, 64, 128, 256, 512, 1024, 1041, 2082, 3123, 6246, 12492, 12509))
    ((1, 2, 4, 8, 16, 17, 1041, 3123, 6246, 12492, 12509), (1, 2, 4, 8, 16, 17, 32, 64, 128, 256, 512, 1024, 1041, 2082, 3123, 6246, 12492, 12509))
    ((1, 2, 4, 8, 16, 17, 1041, 2082, 6246, 12492, 12509), (1, 2, 4, 8, 16, 17, 32, 64, 128, 256, 512, 1024, 1041, 2082, 4164, 6246, 12492, 12509))
    ((1, 2, 4, 8, 16, 17, 1041, 2082, 4164, 12492, 12509), (1, 2, 4, 8, 16, 17, 32, 64, 128, 256, 512, 1024, 1041, 2082, 4164, 8328, 12492, 12509))
    ... ...
    ^KeyboardInterrupt

py_adhoc_call   seed.math.power.addition_chain.shortest.search_greedy_zpow_chain7recursive_shortest   ,枚举冫婪溟链牜递归最短巛靶值扌 +欤次大数降序 =15 +欤带主线
    ((1, 2, 3, 6, 12, 15), (1, 2, 3, 6, 12, 15))
    ((1, 3, 6, 12, 15), (1, 2, 3, 6, 12, 15))
    ((1, 2, 4, 5, 10, 15), (1, 2, 4, 5, 10, 15))
    ((1, 2, 3, 5, 10, 15), (1, 2, 3, 5, 10, 15))
    ((1, 5, 10, 15), (1, 2, 4, 5, 10, 15))
    ((1, 2, 3, 6, 9, 15), (1, 2, 3, 6, 9, 15))
    ((1, 3, 6, 9, 15), (1, 2, 3, 6, 9, 15))
    ((1, 2, 4, 5, 15), (1, 2, 4, 5, 10, 15))
    ((1, 2, 3, 5, 15), (1, 2, 3, 5, 10, 15))
    ((1, 5, 15), (1, 2, 4, 5, 10, 15))
    ((1, 2, 3, 15), (1, 2, 3, 6, 12, 15))
    ((1, 3, 15), (1, 2, 3, 6, 12, 15))

py_adhoc_call   seed.math.power.addition_chain.shortest.search_greedy_zpow_chain7recursive_shortest   ,枚举冫鬽首条婪溟链牜递归最短巛靶值灬扌 -欤次大数降序 =1 =15 =100 =309
    (1,)
    (1, 2, 3, 6, 12, 15)
    (1, 2, 4, 8, 16, 20, 40, 80, 100)
    (1, 2, 3, 6, 12, 18, 21, 36, 72, 144, 288, 309)
py_adhoc_call   seed.math.power.addition_chain.shortest.search_greedy_zpow_chain7recursive_shortest   ,枚举冫鬽首条婪溟链牜递归最短巛靶值灬扌 +欤次大数降序 =1 =15 =100 =309
    (1,)
    (1, 2, 3, 6, 12, 15)
    (1, 2, 4, 8, 16, 32, 64, 96, 100)
    (1, 2, 4, 8, 16, 20, 36, 72, 144, 288, 308, 309)

]]





py_adhoc_call   seed.math.power.addition_chain.shortest.search_greedy_zpow_chain7recursive_shortest   @f
]]]'''#'''
__all__ = r'''
枚举冫婪溟链牜递归最短巛靶值扌
    枚举冫鬽首条婪溟链牜递归最短巛靶值灬扌

枚举生成冫文件冃靶值讠鬽首尾婪溟链牜递归最短扌
枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾婪溟链牜递归最短扌
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
#.def mk_context4lazy_import_registered_names_(qnm4mdl7inject, qnm4pseudo_mdl7import, name7importZqnm4mdl, name7importZalias7inject={}, may_bifix4lazy_name7import=None, lazy_name7importZoriginal_name7import={}):
#.from seed.helper.lazy_import__func7context7register import mk_context4lazy_import_registered_names_, name7importZqnm4mdl_7tiny
#.with mk_context4lazy_import_registered_names_(__name__, 'seed._lazy_', name7importZqnm4mdl_7tiny):
#.    from seed._lazy_ import print_err, fst, echo, ifNone
#.#################################
############################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from itertools import chain
    from bisect import bisect_left
    from seed.for_libs.for_time import mk_rest_func_
    from seed.tiny_.check import check_type_in, check_int_ge_le# check_type_is, check_int_ge, check_may_
    from seed.debug.print_err import print_err
    #.from seed.math.power.addition_chain.shortest.rewrite3 import 严序加链讠最短缩写文本纟递归婪溟链扌, 严序加链巛最短缩写文本纟递归婪溟链扌
    #.def 严序加链讠最短缩写文本纟递归婪溟链扌(严序加链, /, *, fmt_case):
    #.    '严序加链 -> 最短缩写文本纟递归婪溟链/str | ^Error__addition_chain_has_no_greedy_zpow_recur_shortest_stem # [fmt_case == ("stem_str" | "dnzw_str")]'

    #xxx:from seed.math.power.addition_chain.data.target_uint2may_len_optimal_addition_chain import 靶值讠最小显链长
    #xxx:from seed.math.power.addition_chain.data.sorted_target_uints5len_optimal_addition_chain import 最小显链长讠靶值列表 # .最大靶值牜可用 .最小靶值牜溢出
    #.from seed.data_funcs.rngs import make_NonTouchRanges, sorted_ints_to_iter_nontouch_ranges
    #.from seed.data_funcs.rngs import ranges2delta_txt_, ranges5delta_txt_, uint2base64_, uint5base64_

############################
from seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest import 初始化冫参数扌, 构造冫最小显链长讠升列纟靶值扌, 最小化冫最大靶值扌

from seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest import 加载冫靶值讠升列纟次大数牜递归最短扌



from seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest import FormatError


from seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest import 表述冫文本冃鬽首尾加链扌, 解读冫文本冃鬽首尾加链扌

from seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest import 升列讠文本扌, 升列巛文本扌

from seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest import 表述冫文本冃次大数讠首尾加链扌, 解读冫文本冃次大数讠首尾加链扌, 表述冫文本冃升列纟次大数扌, 解读冫文本冃升列纟次大数扌

from seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest import 表述冫文本冃首尾加链乊次大数扌, 解读冫文本冃首尾加链乊次大数扌, 表述冫文本冃加链乊次大数扌, 解读冫文本冃加链乊次大数扌

from seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest import 构造冫首尾加链扌

from seed.math.power.addition_chain.shortest.search_star_chain7recursive_shortest import _读冫末行扌, _解读冫行讠靶值扌, _MAX_VERSION4fmt4us

___end_mark_of_excluded_global_names__0___ = ...

def 枚举冫鬽首条婪溟链牜递归最短巛靶值灬扌(*列表纟靶值, 欤次大数降序, 欤带靶值=False):
    for 靶值 in 列表纟靶值:
        it = 枚举冫婪溟链牜递归最短巛靶值扌(靶值, 欤次大数降序=欤次大数降序)
        鬽首条加链 = next(it, None)
            #鬽首条婪溟链牜递归最短纟靶值
        yield 鬽首条加链 if not 欤带靶值 else (靶值, 鬽首条加链)
def 枚举冫婪溟链牜递归最短巛靶值扌(靶值, /, *, 欤次大数降序, 欤只保留首条加链乊次大数=False, 靶值讠最小显链长=None, 靶值讠升列纟次大数=None, 欤带主线=False):
    #, 最小显链长讠升列纟靶值=None
    (最大靶值, 靶值讠最小显链长, 最小显链长讠升列纟靶值) = 初始化冫参数扌(鬽最大靶值:=靶值, 靶值讠最小显链长, 最小显链长讠升列纟靶值:=None, 欤无需冫最小显链长讠升列纟靶值=True)
    assert 最小显链长讠升列纟靶值 is None
    del 最小显链长讠升列纟靶值

    if 靶值讠升列纟次大数 is None:
        靶值讠升列纟次大数 = ()


    iter_ = iter if not 欤次大数降序 else reversed
    最小显链长纟靶值 = 靶值讠最小显链长[靶值]
    #最小显链长讠升列纟靶值[最小显链长纟靶值]
    us = [None]*(1+最小显链长纟靶值)
    us[0] = 1
    us[-1] = 靶值
    #溟化值串栈 = []
    内点讠最大溟次 = {}
    内点讠欠费溟次 = {}
    主线牜逆向 = []
        #内点 也在 主线上
        #   但 溟化值 不在主线上，不受限于 最小显链长
        #   => 差值 未必受限于 最小显链长
        #bug:毛病冫内点概念应用:goto
    def _mk_us():
        #tuple(sorted(chain(reversed(主线牜逆向), chains(溟化值串栈))))
        支线 = (n<<e for n, ez in sorted(内点讠最大溟次.items()) for e in range(1, 1+ez))
        加链 = tuple(sorted(chain(reversed(主线牜逆向), 支线)))
        assert len(加链) == len(us)
        return 加链
    def _set_n2ez(n, ez, d_ez, /):
        old_ez = 内点讠最大溟次.get(n, 0)
        if ez > old_ez:
            内点讠最大溟次[n] = ez
        old_d_ez = 内点讠欠费溟次.get(n, 0)
        if d_ez > old_d_ez:
            内点讠欠费溟次[n] = d_ez
            #if not d_ez == 0:
            最小付款主干值 = n + (n<<d_ez) #n*(1+(1<<d_ez))
            麻烦！
            doing...
        return (old_ez, old_d_ez)
    def _reset_n2ez(n, ez, old_ez, /):
            doing...
        if ez > old_ez:
            if not 内点讠最大溟次[n] == ez:raise 000
            if old_ez == 0:
                del 内点讠最大溟次[n]
            else:
                内点讠最大溟次[n] = old_ez
    def _put4n(_szmm4v, n, /):
        #可能 最小显链长{n} 超过 最小显链长{靶值}
        szmm4n = 靶值讠最小显链长[n]
        existed = _0put_(szmm4n, n) if szmm4n <= _szmm4v else -1
        return (szmm4n, existed)
    def _put4stem(_szmm4v, v, /):
        existed = _0put_(_szmm4v, v)
        if not existed == -1:
            主线牜逆向.append(v)
        return existed
    def _0put_(szmm4u, u, /):
        '-> imay existed'
        try:
            existed = not us[szmm4u] is None
        except IndexError:
            raise IndexError((us, len(us), (szmm4u, u, 靶值讠最小显链长[u]), (最小显链长纟靶值, 靶值)))
            #^IndexError: ([1, None, None, None, None, None, None, None, None, None, None, 223, None, 4097, 4320], 15, (15, 2047, 15), (14, 4320))
        # [existed == (0|1)]
        if existed:
            # [existed == (1)]
            if not u == us[szmm4u]:
                existed = -1
                # [existed == (-1)]
                # [u =!= us[szmm4u]]
            else:
                # [existed == (1)]
                # [u == us[szmm4u]]
                pass
            # [existed == (-1|1)]
            # [[existed == (-1)] <-> [u =!= us[szmm4u]]]
        else:
            # [existed == (0)]
            us[szmm4u] = u
            # [u == us[szmm4u]]
            # [[existed == (-1)] <-> [u =!= us[szmm4u]]]
        # [[existed == (-1)] <-> [u =!= us[szmm4u]]]
        return existed
    def drop4n__(szmm4n, existed, n, /):
        _0drop__(szmm4n, existed, n)
    def drop4stem__(szmm4u, existed, u, /):
        _0drop__(szmm4u, existed, u)
        if not u == (_u:=主线牜逆向.pop()):raise Exception(主线牜逆向, _u, u)
    def _0drop__(szmm4u, existed, u, /):
        if not type(existed) is bool:raise 000
        if not existed:
            us[szmm4u] = None
        return
    if 欤只保留首条加链乊次大数:
        stop_ = bool
    else:
        def stop_(sz, /):
            return False
    def recur_iter0_(b_toplvl, szmm4u, u, /):
        # [szmm4u == 靶值讠最小显链长[u]]
        existed = _put4stem(szmm4u, u)
        if -1 == existed:
            return 0
        sz = yield from recur_iter1_(b_toplvl, szmm4u, u)
        drop4stem__(szmm4u, existed, u)
        return sz
    def recur_iter1_(b_toplvl, szmm4u, u, /):
        if u == 1:
            加链 = _mk_us()
            yield 加链 if not 欤带主线 else (tuple(reversed(主线牜逆向)), 加链)
            return 1
        _szmm = szmm4u -1
        assert _szmm >= 0
        if not None is (v:=us[_szmm]):
            diff = u - v
            ez = 0
            n = diff
            if not 0 < n <= v:
                return 0
            if u < len(靶值讠升列纟次大数):
                vs = 靶值讠升列纟次大数[u]
                j = bisect_left(vs, v)
                if not (j < len(vs) and vs[j] == v):
                    return 0
            vs = [v]
            js = [0]
            def ok_(_szmm4v, /):
                return True
        else:
            (vs, js) = _靶值讠候选次大数信息扌(最小显链长讠升列纟靶值:=None, 靶值讠升列纟次大数, u, _szmm)
            _imay_first = -1
            _last = _szmm
            def ok_(_szmm4v, /):
                # 次大数 与 下一主干值 之间 不能有 其他 主干值{主要是:前置内点}
                # [us[1+last:szmm4u] are all None]
                # finding:_first:[us[1+_first:szmm4u] are all None]
                nonlocal _imay_first, _last
                if not _imay_first == -1:
                    return _szmm4v >= _imay_first
                if _szmm4v >= _last:
                    return True
                for j in reversed(range(_szmm4v, 1+_last)):
                    if not None is us[j]:
                        _imay_first = _last = j
                        break
                else:
                    assert j > 0#[us[0] == 1]
                    _last = j-1
                return _szmm4v >= _last
        (vs, js), ok_
        sz = 0
        for j in iter_(js):
            v = vs[j]
            _szmm4v = 靶值讠最小显链长[v]
            if not _szmm4v <= _szmm:continue
            if not ok_(_szmm4v):continue
            diff = u - v
            #ez = szmm4u-1 -靶值讠最小显链长[v]
            #ez = _szmm -_szmm4v
            #0 and bug
            #n = diff >> ez
                #bug:毛病冫内点概念应用:here
            min_ez = _szmm -_szmm4v
            n_zpow = diff >> min_ez
                #n_zpow==内点|内点溟化值
            if not diff == (n_zpow<<min_ez):
                continue
            if not 0 < n_zpow <= v:
                continue
            d_ez = 0 # ez-min_ez
            ez = min_ez
            n = n_zpow
            while 1:
                old_ez = _set_n2ez(n, ez, d_ez)
                    doing...
                sz += yield from recur_iter2_(_szmm4v, v, n)
                _reset_n2ez(n, ez, old_ez)
                    doing...
                if not b_toplvl and stop_(sz):
                    break
                if not n&1 == 0:
                    break
                # [n even]
                szmm4n = 靶值讠最小显链长[n]
                if n == us[szmm4n]:
                    break
                # [n not in us]
                # [n even]
                n >>= 1
                ez += 1
                d_ez += 1 # ez-min_ez
                    #但:[d_ez:=ez-min_ez这部分加次在哪扣费？]
        sz
        return sz

    def recur_iter2_(_szmm4v, v, n, /):
        assert 0 < n <= v, (_szmm4v, v, n)
        (szmm4n, existed) = _put4n(_szmm4v, n)
        if -1 == existed:
            return 0
        sz = yield from recur_iter0_(False, _szmm4v, v)
        drop4n__(szmm4n, existed, n)
        return sz
    def main():
        sz = yield from recur_iter0_(True, 最小显链长纟靶值, 靶值)
        assert all(m is None for m in us[1:-1])
    return main()


def _靶值讠候选次大数信息扌(最小显链长讠升列纟靶值, 靶值讠升列纟次大数, u, _szmm, /):
    if u < len(靶值讠升列纟次大数):
        vs = 靶值讠升列纟次大数[u]
        js = range(len(vs))
    else:
        #.vs = 最小显链长讠升列纟靶值[_szmm]
        #.begin = bisect_left(vs, (u+1)//2)
        #.end = bisect_left(vs, u, begin)
        #.js = range(begin, end)
        vs = range(1, u)
        js = range(len(vs))
    vs, js
    return (vs, js)






def 枚举生成冫文件冃靶值讠鬽首尾婪溟链牜递归最短扌(文件路径, /, *, 休眠期=0.0, 苏醒期=2.0, 鬽最大靶值=None, 靶值讠最小显链长=None):
    #, 最小显链长讠升列纟靶值=None
    check_type_in([float, str], 休眠期)
    _rest = mk_rest_func_(休眠期, 苏醒期)
    (最大靶值, 靶值讠最小显链长, 最小显链长讠升列纟靶值) = 初始化冫参数扌(鬽最大靶值:=靶值, 靶值讠最小显链长, 最小显链长讠升列纟靶值:=None, 欤无需冫最小显链长讠升列纟靶值=True)
    assert 最小显链长讠升列纟靶值 is None
    del 最小显链长讠升列纟靶值
    kwds = dict(靶值讠最小显链长=靶值讠最小显链长)

    encoding = 'ascii'
    with open(文件路径, 'ab+') as iobfile:
        end_addr = iobfile.tell()
        bs = _读冫末行扌(end_addr, iobfile)
        assert end_addr == iobfile.tell()
        靶值纟末行 = _解读冫行讠靶值扌(bs.decode(encoding)) if bs else 0
        起始靶值 = 1+靶值纟末行
        #.靶值 = 靶值纟末行
        #.while 靶值 < 最大靶值:
        #.    靶值 += 1
        for 靶值 in range(起始靶值, 1+最大靶值):
            鬽首尾加链 = _靶值讠鬽首尾加链扌(kwds, 靶值)
            s = 表述冫文本冃鬽首尾加链扌(靶值, 鬽首尾加链, validate=True)
            iobfile.write(s.encode(encoding))
            777;iobfile.write(b'\n')
            yield (靶值, s)
            777;_rest()


def _靶值讠鬽首尾加链扌(kwds, 靶值, /):
    it = 枚举冫婪溟链牜递归最短巛靶值扌(靶值, 欤次大数降序=False, **kwds)
    鬽加链 = next(it, None)
    if None is 鬽加链:
        鬽首尾加链 = None
    else:
        首加链 = 鬽加链
        it = 枚举冫婪溟链牜递归最短巛靶值扌(靶值, 欤次大数降序=True, **kwds)
        尾加链 = next(it, None)
        首尾加链 = 构造冫首尾加链扌(首加链, 尾加链)
        鬽首尾加链 = 首尾加链
    鬽首尾加链
    return 鬽首尾加链








def 枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾婪溟链牜递归最短扌(文件路径冃靶值讠升列纟次大数牜递归最短, 输出文件路径冃靶值讠次大数讠首尾婪溟链牜递归最短, /, *, ver, 休眠期=0.0, 苏醒期=2.0, 鬽最大靶值=None, 靶值讠最小显链长=None, 最小显链长讠升列纟靶值=None):
    check_int_ge_le(1, _MAX_VERSION4fmt4us, ver)
    check_type_in([float, str], 休眠期)
    _rest = mk_rest_func_(休眠期, 苏醒期)
    (最大靶值, 靶值讠最小显链长, 最小显链长讠升列纟靶值) = 初始化冫参数扌(鬽最大靶值:=靶值, 靶值讠最小显链长, 最小显链长讠升列纟靶值:=None, 欤无需冫最小显链长讠升列纟靶值=True)
    assert 最小显链长讠升列纟靶值 is None
    del 最小显链长讠升列纟靶值

    encoding = 'ascii'
    with open(文件路径冃靶值讠升列纟次大数牜递归最短, 'at+', encoding=encoding) as iofile, open(输出文件路径冃靶值讠次大数讠首尾婪溟链牜递归最短, 'at', encoding=encoding) as ofile:
        end_addr = iofile.tell()
        iofile.seek(0)
        靶值讠升列纟次大数 = 加载冫靶值讠升列纟次大数牜递归最短扌(iofile)
        assert end_addr == iofile.tell()
        kwds = dict(靶值讠最小显链长=靶值讠最小显链长, 靶值讠升列纟次大数=靶值讠升列纟次大数, 欤只保留首条加链乊次大数=True)
        起始靶值 = len(靶值讠升列纟次大数)
        for 靶值 in range(起始靶值, 1+最大靶值):
            (升列纟次大数, 次大数讠首尾加链) = _靶值讠升列纟次大数丶次大数讠首尾加链扌(kwds, 靶值)
            #######
            s1 = 表述冫文本冃次大数讠首尾加链扌(靶值, 次大数讠首尾加链, validate=True, ver=ver)
            s0 = 表述冫文本冃升列纟次大数扌(靶值, 升列纟次大数, validate=True)
            #######
            #输出到:细节文件
            print(s1, file=ofile)
                #若是 抛出异常，两文件 依然匹配
            #输出到:摘要文件
            print(s0, file=iofile)
                #若是 抛出异常，细节文件 比 摘要文件 多一行，但是 删除重复行更容易，而且 摘要文件行 总是 细节文件行 的 前缀，更容易定位、摘选、复制
            #######
            yield (靶值, len(升列纟次大数), s0)
            777;_rest()

def _靶值讠升列纟次大数丶次大数讠首尾加链扌(kwds, 靶值, /):
    靶值讠升列纟次大数 = kwds['靶值讠升列纟次大数']
    if not 靶值 == len(靶值讠升列纟次大数):raise 000#append

    it = 枚举冫婪溟链牜递归最短巛靶值扌(靶值, 欤次大数降序=False, **kwds)
    列表纟首加链 = tuple(it)
    次大数讠首加链 = {us[-2]:us for us in 列表纟首加链} if not 靶值 == 1 else {}
    777;升列纟次大数 = tuple(sorted(次大数讠首加链.keys()))
    777;靶值讠升列纟次大数.append(升列纟次大数)#for next step:列表纟尾加链
    if 次大数讠首加链:
        it = 枚举冫婪溟链牜递归最短巛靶值扌(靶值, 欤次大数降序=True, **kwds)
        列表纟尾加链 = tuple(it)
        assert len(列表纟尾加链) == len(列表纟首加链)
        次大数讠首尾加链 = {us[-2]:构造冫首尾加链扌(次大数讠首加链[us[-2]], us) for us in 列表纟尾加链}
    else:
        assert 靶值 == 1 or not 列表纟首加链#12509
        次大数讠首尾加链 = {}
    return (升列纟次大数, 次大数讠首尾加链)


__all__



__all__
from seed.math.power.addition_chain.shortest.search_greedy_zpow_chain7recursive_shortest import 枚举冫婪溟链牜递归最短巛靶值扌, 枚举冫鬽首条婪溟链牜递归最短巛靶值灬扌

from seed.math.power.addition_chain.shortest.search_greedy_zpow_chain7recursive_shortest import 枚举生成冫文件冃靶值讠鬽首尾婪溟链牜递归最短扌, 枚举生成冫文件冃靶值讠升列纟次大数牜递归最短丶文件冃靶值讠次大数讠首尾婪溟链牜递归最短扌
from seed.math.power.addition_chain.shortest.search_greedy_zpow_chain7recursive_shortest import *
