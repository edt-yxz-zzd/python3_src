#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__the_max_one__ver2.py
    @20260227
    动态加载牜逐项:[1..=4333]
view ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__the_max_one.py
    @20241226
    静态加载:[1..=4333]

@20260227
注意:『最短』未必是『递归最短』
[1..=4333]中只有[1..<309]被完全涵盖:
    #{已经数据校验}:_校验冫兼容性纟替代方案扌()
    from seed.math.power.addition_chain.data.get_target_uint2may_optimal_addition_chain7max_recur_shortest_stem_ import 取冫靶值讠婪溟链牜递归最短牜左侧最大扌# 靶值讠婪溟链牜递归最短牜左侧最大扌

nn_ns.math_nn.numbers.shortest_addition_chain__the_max_one__ver2
py -m nn_ns.app.debug_cmd   nn_ns.math_nn.numbers.shortest_addition_chain__the_max_one__ver2 -x # -off_defs
py -m nn_ns.app.doctest_cmd nn_ns.math_nn.numbers.shortest_addition_chain__the_max_one__ver2:__doc__ -ht # -ff -df
#######

[[
代码模板:
view ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain__max_recur_shortest_stem.py
%s/婪溟链牜递归最短牜左侧最大/最短加链牜左侧最大/g
]]


'#'; __doc__ = r'#'

>>> from seed.types.Symbol import P
>>> 取冫靶值讠最短加链牜左侧最大扌() is eval(repr(取冫靶值讠最短加链牜左侧最大扌()))
True
>>> 取冫靶值讠最短加链牜左侧最大扌()
P.nn_ns.math_nn.numbers.shortest_addition_chain__the_max_one__ver2().取冫靶值讠最短加链牜左侧最大扌()









>>> 取冫靶值讠最短加链牜左侧最大扌()[0] is None
True
>>> 靶值讠最短加链牜左侧最大扌(0)
Traceback (most recent call last):
    ...
TypeError: 0

>>> 取冫靶值讠最短加链牜左侧最大扌()[1]
(1,)
>>> 靶值讠最短加链牜左侧最大扌(1)
(1,)


>>> 取冫靶值讠最短加链牜左侧最大扌()[15]
(1, 2, 4, 5, 10, 15)
>>> 靶值讠最短加链牜左侧最大扌(15)
(1, 2, 4, 5, 10, 15)

>>> 取冫靶值讠最短加链牜左侧最大扌()[4333]
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 520, 521, 1033, 1097, 1618, 3236, 4333)
>>> 靶值讠最短加链牜左侧最大扌(4333)
(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 520, 521, 1033, 1097, 1618, 3236, 4333)


>>> 取冫靶值讠最短加链牜左侧最大扌()[1+4333]
Traceback (most recent call last):
    ...
IndexError: range object index out of range
>>> 靶值讠最短加链牜左侧最大扌(1+4333)
Traceback (most recent call last):
    ...
IndexError: range object index out of range






py_adhoc_call   nn_ns.math_nn.numbers.shortest_addition_chain__the_max_one__ver2   @_校验冫兼容性纟替代方案扌 +raise_vs_print | more
    (309, (1, 2, 4, 8, 16, 32, 48, 49, 98, 130, 260, 309), (1, 2, 4, 8, 16, 32, 36, 68, 136, 272, 308, 309))
    (383, (1, 2, 4, 8, 16, 32, 64, 80, 84, 85, 149, 298, 383), (1, 2, 4, 8, 16, 32, 40, 41, 82, 114, 228, 342, 383))
    (569, (1, 2, 4, 8, 16, 32, 48, 49, 98, 130, 260, 520, 569), (1, 2, 4, 8, 16, 32, 40, 41, 81, 122, 244, 488, 569))
    ... ...

py_adhoc_call   nn_ns.math_nn.numbers.shortest_addition_chain__the_max_one__ver2   @靶值讠最短加链牜左侧最大扌  =4333
py_adhoc_call   nn_ns.math_nn.numbers.shortest_addition_chain__the_max_one__ver2   ,枚举冫最短加链牜左侧最大灬巛靶值灬扌 =1 =15 =309 =4333

]]]'''#'''
__all__ = r'''
取冫靶值讠最短加链牜左侧最大扌
    靶值讠最短加链牜左侧最大扌
枚举冫最短加链牜左侧最大灬巛靶值灬扌
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.tiny_.check import check_type_is, check_int_ge
___end_mark_of_excluded_global_names__0___ = ...

class _G:
    total = 4333
    stem_name4data = 'shortest_addition_chain__the_max_one.py..data.statistics.up_eq_n.le4333'
        #ver2使用ver1的数据
    basename4data6lzma = f'{stem_name4data}.tar.lzma'
    basename4txt_line_index = f'{stem_name4data}.idx'







def 枚举冫最短加链牜左侧最大灬巛靶值灬扌(*列表纟靶值, 欤带靶值=False):
    靶值讠最短加链牜左侧最大 = 取冫靶值讠最短加链牜左侧最大扌()
    for 靶值 in 列表纟靶值:
        check_int_ge(1, 靶值)
        最短加链牜左侧最大 = 靶值讠最短加链牜左侧最大[靶值]
        yield (靶值, 最短加链牜左侧最大) if 欤带靶值 else 最短加链牜左侧最大

def 靶值讠最短加链牜左侧最大扌(靶值, /):
    check_int_ge(1, 靶值)
    return 取冫靶值讠最短加链牜左侧最大扌()[靶值]

if 0:
    _靶值讠最短加链牜左侧最大 = ...
def 取冫靶值讠最短加链牜左侧最大扌():
    try:
        return _靶值讠最短加链牜左侧最大
    except NameError:
        pass
    _加载冫靶值讠最短加链牜左侧最大扌()
    return 取冫靶值讠最短加链牜左侧最大扌()

def _加载冫靶值讠最短加链牜左侧最大扌():
    global _靶值讠最短加链牜左侧最大
    total = _G.total
    basename6lzma = _G.basename4data6lzma
    basename9idx = _G.basename4txt_line_index
    from pathlib import Path
    path4pkg = Path(__file__).parent
    ipath6lzma = path4pkg / basename6lzma
    iopath9idx = path4pkg / '_ignore__tmp' / basename9idx
    #if not iopath9idx.exists():
    from ast import literal_eval
    from seed.io.line_index_file import ILineIndexArray__tiny_solo_tarfile
        #ILineIndexArray__tiny_solo_tarfile(may_cache, offset4lineno, iopath7line_index, ipath7data6tiny_solo_tarfile, /, *, smay_repr='')
    ipath7data6tiny_solo_tarfile = ipath6lzma
    iopath7line_index = iopath9idx
    class LineIndexArray__tiny_solo_tarfile__提取冫最短加链牜左侧最大(ILineIndexArray__tiny_solo_tarfile):
        #@override
        def _eval_bytes8line_(sf, lineno, bs8line, /):
            s = bs8line.strip().decode('ascii')
            (n, sz, (us, statistics)) = literal_eval(s)
            return us
    _靶值讠最短加链牜左侧最大 = LineIndexArray__tiny_solo_tarfile__提取冫最短加链牜左侧最大(cache:={0:None}, offset4lineno:=1, iopath7line_index, ipath7data6tiny_solo_tarfile, smay_repr='P.nn_ns.math_nn.numbers.shortest_addition_chain__the_max_one__ver2().取冫靶值讠最短加链牜左侧最大扌()')
    assert len(_靶值讠最短加链牜左侧最大) == 1+total
    return



######################
def _校验冫兼容性纟替代方案扌(*, raise_vs_print=False):
    from nn_ns.math_nn.numbers.shortest_addition_chain__the_max_one__ver2 import 取冫靶值讠最短加链牜左侧最大扌
    from seed.math.power.addition_chain.data.get_target_uint2may_optimal_addition_chain7max_recur_shortest_stem_ import 取冫靶值讠婪溟链牜递归最短牜左侧最大扌
    靶值讠最短加链 = 取冫靶值讠最短加链牜左侧最大扌()
    _靶值讠最短加链 = 取冫靶值讠婪溟链牜递归最短牜左侧最大扌()
    assert len(靶值讠最短加链) <= len(_靶值讠最短加链)
    for 靶值 in range(0, len(靶值讠最短加链)):
        #包括:0
        try:
            assert 靶值讠最短加链[靶值] == _靶值讠最短加链[靶值], (靶值, 靶值讠最短加链[靶值], _靶值讠最短加链[靶值])
        except AssertionError as exc:
            if raise_vs_print:
                print(exc)
            else:
                raise



__all__
from nn_ns.math_nn.numbers.shortest_addition_chain__the_max_one__ver2 import 取冫靶值讠最短加链牜左侧最大扌, 靶值讠最短加链牜左侧最大扌
from nn_ns.math_nn.numbers.shortest_addition_chain__the_max_one__ver2 import 枚举冫最短加链牜左侧最大灬巛靶值灬扌
from nn_ns.math_nn.numbers.shortest_addition_chain__the_max_one__ver2 import *
