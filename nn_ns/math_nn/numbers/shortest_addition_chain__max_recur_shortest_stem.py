#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__max_recur_shortest_stem.py
=>:
    view ../../python3_src/seed/math/power/addition_chain/data/get_target_uint2may_optimal_addition_chain7max_recur_shortest_stem_.py
        from seed.math.power.addition_chain.data.get_target_uint2may_optimal_addition_chain7max_recur_shortest_stem_ import 取冫靶值讠婪溟链牜递归最短牜左侧最大扌, 靶值讠婪溟链牜递归最短牜左侧最大扌
        靶值讠最短加链 = 取冫靶值讠婪溟链牜递归最短牜左侧最大扌()


nn_ns.math_nn.numbers.shortest_addition_chain__max_recur_shortest_stem
py -m nn_ns.app.debug_cmd   nn_ns.math_nn.numbers.shortest_addition_chain__max_recur_shortest_stem -x # -off_defs
py -m nn_ns.app.doctest_cmd nn_ns.math_nn.numbers.shortest_addition_chain__max_recur_shortest_stem:__doc__ -ht # -ff -df
#######

[[
数据来源:
view ../../python3_src/seed/math/power/addition_chain/shortest/mixed_recursive_greedy_zpow_addition_chain__doc__py_adhoc_call.py

cp -iv /sdcard/0my_files/zip/addition_chain/靶值讠简并记录纟递归婪溟链/tar/mixed_recursive_greedy_zpow_addition_chain..另档冫递归婪溟链暨最短加链牜左侧最大讠址距溟次形式扌.1-39363.extract-out.txt.tar.lzma   ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__max_recur_shortest_stem.py..址距溟次形式纟左侧最大纟递归婪溟链.le39363.txt.tar.lzma
]]
[[
代码模板:
view ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__six_lists.py
%s/尾六表/婪溟链牜递归最短牜左侧最大/g
]]


[[
]]


'#'; __doc__ = r'#'
>>> from seed.types.Symbol import P
>>> 取冫靶值讠婪溟链牜递归最短牜左侧最大扌() is eval(repr(取冫靶值讠婪溟链牜递归最短牜左侧最大扌()))
True
>>> 取冫靶值讠婪溟链牜递归最短牜左侧最大扌()
P.nn_ns.math_nn.numbers.shortest_addition_chain__max_recur_shortest_stem().取冫靶值讠婪溟链牜递归最短牜左侧最大扌()
>>> 取冫靶值讠婪溟链牜递归最短牜左侧最大扌() is P.nn_ns.math_nn.numbers.shortest_addition_chain__max_recur_shortest_stem().取冫靶值讠婪溟链牜递归最短牜左侧最大扌()
True









>>> 取冫靶值讠婪溟链牜递归最短牜左侧最大扌()[0] is None
True
>>> 靶值讠婪溟链牜递归最短牜左侧最大扌(0)
Traceback (most recent call last):
    ...
TypeError: 0

>>> 取冫靶值讠婪溟链牜递归最短牜左侧最大扌()[1]
(1,)
>>> 靶值讠婪溟链牜递归最短牜左侧最大扌(1)
(1,)


>>> 取冫靶值讠婪溟链牜递归最短牜左侧最大扌()[35035]
(1, 2, 4, 8, 16, 32, 64, 128, 256, 384, 385, 770, 1540, 3080, 6160, 9240, 9625, 19250, 28875, 35035)
>>> 靶值讠婪溟链牜递归最短牜左侧最大扌(35035)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 384, 385, 770, 1540, 3080, 6160, 9240, 9625, 19250, 28875, 35035)

>>> 取冫靶值讠婪溟链牜递归最短牜左侧最大扌()[39363]
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 4352, 8704, 13056, 13120, 13121, 26242, 39363)
>>> 靶值讠婪溟链牜递归最短牜左侧最大扌(39363)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 4352, 8704, 13056, 13120, 13121, 26242, 39363)

>>> 取冫靶值讠婪溟链牜递归最短牜左侧最大扌()[1+39363]
Traceback (most recent call last):
    ...
IndexError: range object index out of range
>>> 靶值讠婪溟链牜递归最短牜左侧最大扌(1+39363)
Traceback (most recent call last):
    ...
IndexError: range object index out of range









py_adhoc_call   nn_ns.math_nn.numbers.shortest_addition_chain__max_recur_shortest_stem   @f
]]]'''#'''
__all__ = r'''
取冫靶值讠婪溟链牜递归最短牜左侧最大扌
    靶值讠婪溟链牜递归最短牜左侧最大扌
    枚举冫婪溟链牜递归最短牜左侧最大灬巛靶值灬扌


'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.tiny_.check import check_type_is, check_int_ge
___end_mark_of_excluded_global_names__0___ = ...

class _G:
    total = 39363
    stem_name4data = 'shortest_addition_chain__max_recur_shortest_stem.py..址距溟次形式纟左侧最大纟递归婪溟链.le39363.txt'
    basename4data6lzma = f'{stem_name4data}.tar.lzma'
    basename4txt_line_index = f'{stem_name4data}.idx'







def 枚举冫婪溟链牜递归最短牜左侧最大灬巛靶值灬扌(*列表纟靶值, 欤带靶值=False):
    靶值讠婪溟链牜递归最短牜左侧最大 = 取冫靶值讠婪溟链牜递归最短牜左侧最大扌()
    for 靶值 in 列表纟靶值:
        check_int_ge(1, 靶值)
        婪溟链牜递归最短牜左侧最大 = 靶值讠婪溟链牜递归最短牜左侧最大[靶值]
        yield (靶值, 婪溟链牜递归最短牜左侧最大) if 欤带靶值 else 婪溟链牜递归最短牜左侧最大

def 靶值讠婪溟链牜递归最短牜左侧最大扌(靶值, /):
    #===靶值讠最短加链牜递归婪溟链牜左侧最大扌
    check_int_ge(1, 靶值)
    return 取冫靶值讠婪溟链牜递归最短牜左侧最大扌()[靶值]

if 0:
    _靶值讠婪溟链牜递归最短牜左侧最大 = ...
def 取冫靶值讠婪溟链牜递归最短牜左侧最大扌():
    #===取冫靶值讠最短加链牜递归婪溟链牜左侧最大扌
    try:
        return _靶值讠婪溟链牜递归最短牜左侧最大
    except NameError:
        pass
    _加载冫靶值讠婪溟链牜递归最短牜左侧最大扌()
    return 取冫靶值讠婪溟链牜递归最短牜左侧最大扌()

def _加载冫靶值讠婪溟链牜递归最短牜左侧最大扌():
    global _靶值讠婪溟链牜递归最短牜左侧最大
    total = _G.total
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
    ipath7data6tiny_solo_tarfile = ipath6lzma
    iopath7line_index = iopath9idx
    class LineIndexArray__tiny_solo_tarfile__婪溟链牜递归最短牜左侧最大巛址距溟次形式(ILineIndexArray__tiny_solo_tarfile):
        #@override
        def _eval_bytes8line_(sf, lineno, bs8line, /):
            s = bs8line.strip().decode('ascii')
            return 严序加链巛最短缩写文本纟递归婪溟链扌(s, fmt_case='dnzw_str')
    _靶值讠婪溟链牜递归最短牜左侧最大 = LineIndexArray__tiny_solo_tarfile__婪溟链牜递归最短牜左侧最大巛址距溟次形式(cache:={0:None}, offset4lineno:=1, iopath7line_index, ipath7data6tiny_solo_tarfile, smay_repr='P.nn_ns.math_nn.numbers.shortest_addition_chain__max_recur_shortest_stem().取冫靶值讠婪溟链牜递归最短牜左侧最大扌()')
    assert len(_靶值讠婪溟链牜递归最短牜左侧最大) == 1+total
    return














__all__
from nn_ns.math_nn.numbers.shortest_addition_chain__max_recur_shortest_stem import 取冫靶值讠婪溟链牜递归最短牜左侧最大扌, 靶值讠婪溟链牜递归最短牜左侧最大扌, 枚举冫婪溟链牜递归最短牜左侧最大灬巛靶值灬扌

from nn_ns.math_nn.numbers.shortest_addition_chain__max_recur_shortest_stem import *
