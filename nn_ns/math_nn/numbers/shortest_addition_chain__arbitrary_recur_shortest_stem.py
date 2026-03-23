#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__arbitrary_recur_shortest_stem.py
    动态加载牜逐项:[1..=70070]
=>:
    view ../../python3_src/seed/math/power/addition_chain/data/get_target_uint2may_optimal_addition_chain7arbitrary_recur_shortest_stem_.py
    from seed.math.power.addition_chain.data.get_target_uint2may_optimal_addition_chain7arbitrary_recur_shortest_stem_ import 取冫靶值讠婪溟链牜递归最短牜任意扌, 靶值讠婪溟链牜递归最短牜任意扌

nn_ns.math_nn.numbers.shortest_addition_chain__arbitrary_recur_shortest_stem
py -m nn_ns.app.debug_cmd   nn_ns.math_nn.numbers.shortest_addition_chain__arbitrary_recur_shortest_stem -x # -off_defs
py -m nn_ns.app.doctest_cmd nn_ns.math_nn.numbers.shortest_addition_chain__arbitrary_recur_shortest_stem:__doc__ -ht # -ff -df
#######

[[
代码模板:
view ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__max_recur_shortest_stem.py
view ../../python3_src/seed/math/power/addition_chain/data/get_target_uint2may_optimal_addition_chain7max_recur_shortest_stem_.py
]]


'#'; __doc__ = r'#'
>>> from seed.types.Symbol import P
>>> 取冫靶值讠婪溟链牜递归最短牜任意扌() is eval(repr(取冫靶值讠婪溟链牜递归最短牜任意扌()))
True
>>> 取冫靶值讠婪溟链牜递归最短牜任意扌()
P.nn_ns.math_nn.numbers.shortest_addition_chain__arbitrary_recur_shortest_stem().取冫靶值讠婪溟链牜递归最短牜任意扌()
>>> len(取冫靶值讠婪溟链牜递归最短牜任意扌())
70071
>>> 取冫靶值讠婪溟链牜递归最短牜任意扌()[70071]
Traceback (most recent call last):
    ...
IndexError: range object index out of range
>>> 取冫靶值讠婪溟链牜递归最短牜任意扌()[70070]
(1, 2, 4, 8, 16, 32, 64, 128, 144, 272, 544, 1088, 2176, 4352, 8704, 17408, 17410, 17554, 34962, 35108, 70070)
>>> 取冫靶值讠婪溟链牜递归最短牜任意扌()[39364]
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 2112, 4160, 6208, 12416, 12420, 14532, 24832, 39364)
>>> 取冫靶值讠婪溟链牜递归最短牜任意扌()[39363]
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 4352, 8704, 13056, 13120, 13121, 26242, 39363)
>>> 取冫靶值讠婪溟链牜递归最短牜任意扌()[1]
(1,)
>>> 取冫靶值讠婪溟链牜递归最短牜任意扌()[0] is None
True
>>> 取冫靶值讠婪溟链牜递归最短牜任意扌()[50215]
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 1025, 2050, 3075, 4099, 8198, 11273, 19471, 38942, 50215)
>>> 取冫靶值讠婪溟链牜递归最短牜任意扌()[37726]
(1, 2, 4, 8, 16, 32, 64, 128, 256, 257, 513, 770, 1540, 2053, 3593, 7186, 9239, 18478, 36956, 37726)
>>> 取冫靶值讠婪溟链牜递归最短牜任意扌()[12509]
(1, 2, 4, 8, 16, 17, 32, 64, 128, 256, 512, 1024, 1041, 2082, 4164, 8328, 12492, 12509)


#左侧最大:
>>> 取冫靶值讠婪溟链牜递归最短牜左侧最大扌()[39364]
Traceback (most recent call last):
    ...
IndexError: range object index out of range
>>> 取冫靶值讠婪溟链牜递归最短牜左侧最大扌()[39363]
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 4352, 8704, 13056, 13120, 13121, 26242, 39363)

[[
py_adhoc_call   nn_ns.math_nn.numbers.shortest_addition_chain__arbitrary_recur_shortest_stem   ,枚举冫婪溟链牜递归最短牜任意灬巛靶值灬扌 =1 =39363 =39364 =70070
(1,)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 4352, 8704, 13056, 13120, 13121, 26242, 39363)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 2112, 4160, 6208, 12416, 12420, 14532, 24832, 39364)
(1, 2, 4, 8, 16, 32, 64, 128, 144, 272, 544, 1088, 2176, 4352, 8704, 17408, 17410, 17554, 34962, 35108, 70070)
]]

]]]'''#'''
__all__ = r'''
取冫靶值讠婪溟链牜递归最短牜任意扌
    靶值讠婪溟链牜递归最短牜任意扌

枚举冫婪溟链牜递归最短牜任意灬巛靶值灬扌
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.tiny_.check import check_type_is, check_int_ge
from nn_ns.math_nn.numbers.shortest_addition_chain__max_recur_shortest_stem import 取冫靶值讠婪溟链牜递归最短牜左侧最大扌
    #39363
___end_mark_of_excluded_global_names__0___ = ...


class _G:
    _total = 39363
    _begin = 38039
    total = 70070
    stem_name4data = 'shortest_addition_chain__arbitrary_recur_shortest_stem.py..址距溟次形式纟任意纟递归婪溟链.ge38039.le70070.txt'
    #shortest_addition_chain__arbitrary_recur_shortest_stem.py..址距溟次形式纟任意纟递归婪溟链.ge38039.le70070.txt.tar.lzma
    basename4data6lzma = f'{stem_name4data}.tar.lzma'
    basename4txt_line_index = f'{stem_name4data}.idx'







def 枚举冫婪溟链牜递归最短牜任意灬巛靶值灬扌(*列表纟靶值, 欤带靶值=False, fmt_case=None):
    '[fmt_case == may ("stem_str" | "dnzw_str")]'
    if not fmt_case is None:
        from seed.math.power.addition_chain.shortest.rewrite3 import 严序加链讠最短缩写文本纟递归婪溟链扌
        def r5us_(us, /):
            return 严序加链讠最短缩写文本纟递归婪溟链扌(us, fmt_case=fmt_case)
    else:
        def r5us_(us, /):
            return us
    r5us_
    靶值讠婪溟链牜递归最短牜任意 = 取冫靶值讠婪溟链牜递归最短牜任意扌()
    for 靶值 in 列表纟靶值:
        check_int_ge(1, 靶值)
        婪溟链牜递归最短牜任意 = 靶值讠婪溟链牜递归最短牜任意[靶值]
        r = r5us_(婪溟链牜递归最短牜任意)
        yield (靶值, r) if 欤带靶值 else r

def 靶值讠婪溟链牜递归最短牜任意扌(靶值, /):
    #===靶值讠最短加链牜递归婪溟链牜任意扌
    check_int_ge(1, 靶值)
    return 取冫靶值讠婪溟链牜递归最短牜任意扌()[靶值]

if 0:
    _靶值讠婪溟链牜递归最短牜任意 = ...
def 取冫靶值讠婪溟链牜递归最短牜任意扌():
    #===取冫靶值讠最短加链牜递归婪溟链牜任意扌
    try:
        return _靶值讠婪溟链牜递归最短牜任意
    except NameError:
        pass
    _加载冫靶值讠婪溟链牜递归最短牜任意扌()
    return 取冫靶值讠婪溟链牜递归最短牜任意扌()

def _加载冫靶值讠婪溟链牜递归最短牜任意扌():
    global _靶值讠婪溟链牜递归最短牜任意
    total = _G.total
    _begin = _G._begin
    basename6lzma = _G.basename4data6lzma
    basename9idx = _G.basename4txt_line_index
    from pathlib import Path
    path4pkg = Path(__file__).parent
    ipath6lzma = path4pkg / basename6lzma
    iopath9idx = path4pkg / '_ignore__tmp' / basename9idx
    #if not iopath9idx.exists():
    from seed.math.power.addition_chain.shortest.rewrite3 import 严序加链讠最短缩写文本纟递归婪溟链扌, 严序加链巛最短缩写文本纟递归婪溟链扌
        #址距溟次形式:dnzw_str
    from seed.io.line_index_file import ILineIndexArray__tiny_solo_tarfile
        #ILineIndexArray__tiny_solo_tarfile(may_cache, offset4lineno, iopath7line_index, ipath7data6tiny_solo_tarfile, /, *, smay_repr='')
    from seed.types.view.SeqCatView import SeqCatView
        #SeqCatView(triples7begin_size_seq)
        #   :: [(begin, size, seq)] -> SeqCatView
    ipath7data6tiny_solo_tarfile = ipath6lzma
    iopath7line_index = iopath9idx
    #.class LineIndexArray__tiny_solo_tarfile__婪溟链牜递归最短牜任意巛址距溟次形式(ILineIndexArray__tiny_solo_tarfile):
    #.    #@override
    #.    def _eval_bytes8line_(sf, lineno, bs8line, /):
    #.        s = bs8line.strip().decode('ascii')
    #.        return 严序加链巛最短缩写文本纟递归婪溟链扌(s, fmt_case='dnzw_str')
    _low = 取冫靶值讠婪溟链牜递归最短牜左侧最大扌()
    _1total = len(_low)
    assert _1total >= _begin
    class LineIndexArray__tiny_solo_tarfile__婪溟链牜递归最短牜任意巛址距溟次形式(type(_low)):pass
    _high = LineIndexArray__tiny_solo_tarfile__婪溟链牜递归最短牜任意巛址距溟次形式(cache:={}, offset4lineno:=0, iopath7line_index, ipath7data6tiny_solo_tarfile)
    _靶值讠婪溟链牜递归最短牜任意 = SeqCatView([(0, _1total, _low), (j:=_1total-_begin, len(_high)-j, _high)], smay_repr='P.nn_ns.math_nn.numbers.shortest_addition_chain__arbitrary_recur_shortest_stem().取冫靶值讠婪溟链牜递归最短牜任意扌()')
    assert len(_靶值讠婪溟链牜递归最短牜任意) == 1+total
    return



__all__
from nn_ns.math_nn.numbers.shortest_addition_chain__arbitrary_recur_shortest_stem import 取冫靶值讠婪溟链牜递归最短牜任意扌, 靶值讠婪溟链牜递归最短牜任意扌

from nn_ns.math_nn.numbers.shortest_addition_chain__arbitrary_recur_shortest_stem import 枚举冫婪溟链牜递归最短牜任意灬巛靶值灬扌
from nn_ns.math_nn.numbers.shortest_addition_chain__arbitrary_recur_shortest_stem import *
