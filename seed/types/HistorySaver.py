#__all__:goto
r'''[[[
e ../../python3_src/seed/types/HistorySaver.py

seed.types.HistorySaver
py -m nn_ns.app.debug_cmd   seed.types.HistorySaver -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.types.HistorySaver:__doc__ -ht # -ff -df
#######

[[
come_from:
e ../../python3_src/seed/math/factor_pint/factor_pint__smooth_group_order_method.py
move_from:
e ../../python3_src/seed/abc/IReproduceable.py
]]


'#'; __doc__ = r'#'
>>> from seed.types.Reproduceable import Reproduceable5seq
>>> from seed.math.sign_of import sign_of
>>> def jZhistory2rank_(j, /):
...     def history2rank_(history, /):
...         return sign_of(history.xidx - j)
...     return history2rank_
>>> history0 = Reproduceable5seq('0123456789', 0)
>>> saver = DenseHistorySaver(4)
>>> saver.append(history0)
>>> saver.full
False
>>> saver.fills_(3)
>>> saver.full
True
>>> saver.fills_(1)
Traceback (most recent call last):
    ...
seed.types.HistorySaver.FullError
>>> saver
DenseHistorySaver(4, history_array=[Reproduceable5seq('0123456789', 0), Reproduceable5seq('0123456789', 1), Reproduceable5seq('0123456789', 2), Reproduceable5seq('0123456789', 3)])
>>> saver.clear_but_last_()
>>> saver.fills_(3)
>>> saver
DenseHistorySaver(4, history_array=[Reproduceable5seq('0123456789', 3), Reproduceable5seq('0123456789', 4), Reproduceable5seq('0123456789', 5), Reproduceable5seq('0123456789', 6)])
>>> saver.search7dense_(jZhistory2rank_(5), zero6sparse_ok=True, validate6recursive=True)
(0, (1, Reproduceable5seq('0123456789', 4), -1), (2, Reproduceable5seq('0123456789', 5), 0))

(0, Reproduceable5seq('0123456789', 4), Reproduceable5seq('0123456789', 5))

>>> saver.search7sparse_(jZhistory2rank_(2))
(3, None, (0, Reproduceable5seq('0123456789', 3), 1))

(3, None, Reproduceable5seq('0123456789', 3))
>>> saver.search7sparse_(jZhistory2rank_(3))
(1, None, (0, Reproduceable5seq('0123456789', 3), 0))

(1, None, Reproduceable5seq('0123456789', 3))
>>> saver.search7sparse_(jZhistory2rank_(5))
(0, (1, Reproduceable5seq('0123456789', 4), -1), (2, Reproduceable5seq('0123456789', 5), 0))

(0, Reproduceable5seq('0123456789', 4), Reproduceable5seq('0123456789', 5))
>>> saver.search7sparse_(jZhistory2rank_(6))
(0, (2, Reproduceable5seq('0123456789', 5), -1), (3, Reproduceable5seq('0123456789', 6), 0))

(0, Reproduceable5seq('0123456789', 5), Reproduceable5seq('0123456789', 6))
>>> saver.search7sparse_(jZhistory2rank_(7))
(4, (3, Reproduceable5seq('0123456789', 6), -1), None)

(4, Reproduceable5seq('0123456789', 6), None)

>>> saver.search7sparse_(jZhistory2rank_(5.5))
(2, (2, Reproduceable5seq('0123456789', 5), -1), (3, Reproduceable5seq('0123456789', 6), 1))

(2, Reproduceable5seq('0123456789', 5), Reproduceable5seq('0123456789', 6))

>>> saver.search7dense_(jZhistory2rank_(2), validate6recursive=True)
(3, None, (0, Reproduceable5seq('0123456789', 3), 1))

(3, None, Reproduceable5seq('0123456789', 3))
>>> saver.search7dense_(jZhistory2rank_(3), validate6recursive=True)
(1, None, (0, Reproduceable5seq('0123456789', 3), 0))

(1, None, Reproduceable5seq('0123456789', 3))
>>> saver.search7dense_(jZhistory2rank_(5), validate6recursive=True)
(0, (1, Reproduceable5seq('0123456789', 4), -1), (2, Reproduceable5seq('0123456789', 5), 0))

(0, Reproduceable5seq('0123456789', 4), Reproduceable5seq('0123456789', 5))
>>> saver.search7dense_(jZhistory2rank_(6), validate6recursive=True)
(0, (2, Reproduceable5seq('0123456789', 5), -1), (3, Reproduceable5seq('0123456789', 6), 0))

(0, Reproduceable5seq('0123456789', 5), Reproduceable5seq('0123456789', 6))
>>> saver.search7dense_(jZhistory2rank_(7), validate6recursive=True)
(4, (3, Reproduceable5seq('0123456789', 6), -1), None)

(4, Reproduceable5seq('0123456789', 6), None)

>>> saver.search7dense_(jZhistory2rank_(5.5), validate6recursive=True)
(2, (2, Reproduceable5seq('0123456789', 5), -1), (3, Reproduceable5seq('0123456789', 6), 1))

(2, Reproduceable5seq('0123456789', 5), Reproduceable5seq('0123456789', 6))

>>> saver.clear()
>>> saver.search7sparse_(jZhistory2rank_(5.5))
(5, None, None)
>>> saver.search7dense_(jZhistory2rank_(5.5), validate6recursive=True)
(5, None, None)





>>> import seed.types.HistorySaver
>>> seed.types.HistorySaver._debug = True

>>> history0 = Reproduceable5seq('0123456789', 0)
>>> saver = SparseHistorySaver(2, 3, -1)
>>> saver.append(history0)
>>> saver.full
False
>>> saver.fills_(1) #1
>>> saver.fills_(1) #2
>>> saver.fills_(1) #3
>>> saver.full
False
>>> saver
SparseHistorySaver(2, 3, -1, history_array=[Reproduceable5seq('0123456789', 0), Reproduceable5seq('0123456789', 2), Reproduceable5seq('0123456789', 3)], size7apparent=4, curr_max_size7physical=3, curr_step=2, last_step=1)
>>> saver.fills_(3)
>>> saver
SparseHistorySaver(2, 3, -1, history_array=[Reproduceable5seq('0123456789', 0), Reproduceable5seq('0123456789', 4), Reproduceable5seq('0123456789', 6)], size7apparent=7, curr_max_size7physical=3, curr_step=4, last_step=2)
>>> saver.fills_(2)
>>> saver
SparseHistorySaver(2, 3, -1, history_array=[Reproduceable5seq('0123456789', 0), Reproduceable5seq('0123456789', 4), Reproduceable5seq('0123456789', 8)], size7apparent=9, curr_max_size7physical=3, curr_step=4, last_step=4)
>>> saver.fills_(2)
>>> saver
SparseHistorySaver(2, 3, -1, history_array=[Reproduceable5seq('0123456789', 0), Reproduceable5seq('0123456789', 8), Reproduceable5seq('0123456789', 10)], size7apparent=11, curr_max_size7physical=3, curr_step=8, last_step=2)

>>> saver.search7dense_(jZhistory2rank_(5.5), validate6recursive=True)
(2, (5, Reproduceable5seq('0123456789', 5), -1), (6, Reproduceable5seq('0123456789', 6), 1))

(2, Reproduceable5seq('0123456789', 5), Reproduceable5seq('0123456789', 6))
>>> saver.search7sparse_(jZhistory2rank_(5.5))
(2, (0, Reproduceable5seq('0123456789', 0), -1), (8, Reproduceable5seq('0123456789', 8), 1))

(2, Reproduceable5seq('0123456789', 0), Reproduceable5seq('0123456789', 8))

>>> saver.search7dense_(jZhistory2rank_(5), zero6sparse_ok=True, validate6recursive=True)
(0, (4, Reproduceable5seq('0123456789', 4), -1), (5, Reproduceable5seq('0123456789', 5), 0))

(0, Reproduceable5seq('0123456789', 4), Reproduceable5seq('0123456789', 5))
>>> saver.search7dense_(jZhistory2rank_(8), zero6sparse_ok=True, validate6recursive=True)
(0, (0, Reproduceable5seq('0123456789', 0), -1), (8, Reproduceable5seq('0123456789', 8), 0))

(0, Reproduceable5seq('0123456789', 0), Reproduceable5seq('0123456789', 8))



>>> history0 = Reproduceable5seq('0123456789', 0)
>>> saver = SparseHistorySaver(2, 4, -1)
>>> saver.append(history0)
>>> saver.full
False
>>> saver.fills_(1) #1
>>> saver.fills_(1) #2
>>> saver.fills_(1) #3
>>> saver.full
False
>>> saver
SparseHistorySaver(2, 4, -1, history_array=[Reproduceable5seq('0123456789', 0), Reproduceable5seq('0123456789', 2), Reproduceable5seq('0123456789', 3)], size7apparent=4, curr_max_size7physical=4, curr_step=2, last_step=1)
>>> saver.fills_(3)
>>> saver
SparseHistorySaver(2, 4, -1, history_array=[Reproduceable5seq('0123456789', 0), Reproduceable5seq('0123456789', 2), Reproduceable5seq('0123456789', 4), Reproduceable5seq('0123456789', 6)], size7apparent=7, curr_max_size7physical=4, curr_step=2, last_step=2)
>>> saver.fills_(2)
>>> saver
SparseHistorySaver(2, 4, -1, history_array=[Reproduceable5seq('0123456789', 0), Reproduceable5seq('0123456789', 4), Reproduceable5seq('0123456789', 8)], size7apparent=9, curr_max_size7physical=4, curr_step=4, last_step=4)
>>> saver.fills_(2)
>>> saver
SparseHistorySaver(2, 4, -1, history_array=[Reproduceable5seq('0123456789', 0), Reproduceable5seq('0123456789', 4), Reproduceable5seq('0123456789', 8), Reproduceable5seq('0123456789', 10)], size7apparent=11, curr_max_size7physical=4, curr_step=4, last_step=2)

>>> saver.search7dense_(jZhistory2rank_(5.5), validate6recursive=True)
(2, (5, Reproduceable5seq('0123456789', 5), -1), (6, Reproduceable5seq('0123456789', 6), 1))

(2, Reproduceable5seq('0123456789', 5), Reproduceable5seq('0123456789', 6))
>>> saver.search7sparse_(jZhistory2rank_(5.5))
(2, (4, Reproduceable5seq('0123456789', 4), -1), (8, Reproduceable5seq('0123456789', 8), 1))

(2, Reproduceable5seq('0123456789', 4), Reproduceable5seq('0123456789', 8))

>>> saver.search7dense_(jZhistory2rank_(5), zero6sparse_ok=True, validate6recursive=True)
(0, (4, Reproduceable5seq('0123456789', 4), -1), (5, Reproduceable5seq('0123456789', 5), 0))

(0, Reproduceable5seq('0123456789', 4), Reproduceable5seq('0123456789', 5))
>>> saver.search7dense_(jZhistory2rank_(8), zero6sparse_ok=True, validate6recursive=True)
(0, (4, Reproduceable5seq('0123456789', 4), -1), (8, Reproduceable5seq('0123456789', 8), 0))

(0, Reproduceable5seq('0123456789', 4), Reproduceable5seq('0123456789', 8))




>>> history0 = Reproduceable5seq(range(2**11), 0)
>>> saver = SparseHistorySaver(2, 17, -1)
>>> saver.append(history0)
>>> #saver.fills_(2**11)
>>> saver.fills7unlimit_()
>>> saver.validate()
>>> saver
SparseHistorySaver(2, 17, -1, history_array=[Reproduceable5seq(range(0, 2048), 0), Reproduceable5seq(range(0, 2048), 128), Reproduceable5seq(range(0, 2048), 256), Reproduceable5seq(range(0, 2048), 384), Reproduceable5seq(range(0, 2048), 512), Reproduceable5seq(range(0, 2048), 640), Reproduceable5seq(range(0, 2048), 768), Reproduceable5seq(range(0, 2048), 896), Reproduceable5seq(range(0, 2048), 1024), Reproduceable5seq(range(0, 2048), 1152), Reproduceable5seq(range(0, 2048), 1280), Reproduceable5seq(range(0, 2048), 1408), Reproduceable5seq(range(0, 2048), 1536), Reproduceable5seq(range(0, 2048), 1664), Reproduceable5seq(range(0, 2048), 1792), Reproduceable5seq(range(0, 2048), 1920), Reproduceable5seq(range(0, 2048), 2048)], size7apparent=2049, curr_max_size7physical=17, curr_step=128, last_step=128)
>>> saver.fills7unlimit_()


>>> history0 = Reproduceable5seq(range(2**11), 0)
>>> saver = SparseHistorySaver(2, 16, -1)
>>> saver.append(history0)
>>> saver.fills_(2**11)
>>> saver.validate()
>>> saver
SparseHistorySaver(2, 16, -1, history_array=[Reproduceable5seq(range(0, 2048), 0), Reproduceable5seq(range(0, 2048), 256), Reproduceable5seq(range(0, 2048), 512), Reproduceable5seq(range(0, 2048), 768), Reproduceable5seq(range(0, 2048), 1024), Reproduceable5seq(range(0, 2048), 1280), Reproduceable5seq(range(0, 2048), 1536), Reproduceable5seq(range(0, 2048), 1792), Reproduceable5seq(range(0, 2048), 2048)], size7apparent=2049, curr_max_size7physical=16, curr_step=256, last_step=256)










>>> history0 = Reproduceable5seq(range(160), 0)
>>> saver = SparseHistorySaver(2, 8, 64)
>>> saver.append(history0)
>>> saver.fills7unlimit_()
>>> saver.validate()
>>> saver
SparseHistorySaver(2, 8, 64, history_array=[Reproduceable5seq(range(0, 160), 0), Reproduceable5seq(range(0, 160), 16), Reproduceable5seq(range(0, 160), 32), Reproduceable5seq(range(0, 160), 48), Reproduceable5seq(range(0, 160), 63)], size7apparent=64, curr_max_size7physical=8, curr_step=16, last_step=15)

>>> saver.clear_but_last_()
>>> saver.fills7unlimit_()
>>> saver.validate()
>>> saver
SparseHistorySaver(2, 8, 64, history_array=[Reproduceable5seq(range(0, 160), 63), Reproduceable5seq(range(0, 160), 79), Reproduceable5seq(range(0, 160), 95), Reproduceable5seq(range(0, 160), 111), Reproduceable5seq(range(0, 160), 126)], size7apparent=64, curr_max_size7physical=8, curr_step=16, last_step=15)

>>> saver.clear_but_last_()
>>> saver.fills7unlimit_()
>>> saver.validate()
>>> saver
SparseHistorySaver(2, 8, 64, history_array=[Reproduceable5seq(range(0, 160), 126), Reproduceable5seq(range(0, 160), 134), Reproduceable5seq(range(0, 160), 142), Reproduceable5seq(range(0, 160), 150), Reproduceable5seq(range(0, 160), 158), Reproduceable5seq(range(0, 160), 160)], size7apparent=35, curr_max_size7physical=8, curr_step=8, last_step=2)




>>> mk_history_saver_(2, 8, 999, -1)
SparseHistorySaver(2, 8, -1, history_array=[], size7apparent=0, curr_max_size7physical=2, curr_step=1, last_step=1)
>>> mk_history_saver_(2, 8, 999, 0)
SparseHistorySaver(2, 8, 1000, history_array=[], size7apparent=0, curr_max_size7physical=2, curr_step=1, last_step=1)
>>> mk_history_saver_(2, 8, 999, 1)
DenseHistorySaver(2, history_array=[])
>>> mk_history_saver_(2, 8, 999, 7)
DenseHistorySaver(8, history_array=[])
>>> mk_history_saver_(2, 8, 999, 8)
SparseHistorySaver(2, 8, 9, history_array=[], size7apparent=0, curr_max_size7physical=2, curr_step=1, last_step=1)
>>> mk_history_saver_(2, 8, 999, 9)
SparseHistorySaver(2, 8, 10, history_array=[], size7apparent=0, curr_max_size7physical=2, curr_step=1, last_step=1)












search7dense_
reversed_search_key_points_
    def reversed_search_key_points_(sf, stZhistory2rank_, op4fold_, st7fold, /, *, offset=0, _max_size7dense_6SparseHistorySaver=2049, _max_size7physical_6SparseHistorySaver=65537):
3%(5*43)
[order_mod_(5;3) == 4 == 2*2]
[order_mod_(43;3) == 42 == 2*3*7]

>>> from math import gcd
>>> from seed.types.Reproduceable import Reproduceable7transform_via_ops, Reproduceable7tmay_prev_oresult# Reproduceable7foldl
>>> from seed.types.Reproduceable import list_fsts4reproduceable_
>>> from seed.types.Reproduceable import the_ops4transform7stated7echo, StatedTransformOps7foldl, StatedTransformOps7fork# StatedTransformOps7flow, StatedTransformOps, StatedTransformOps7rdiff, , StatedTransformOps7fmap, StatedTransformOps7echo, 
>>> tr4snd6result_ = lambda snd6result:[((jmm, _1mm), (j, _01)) for ((jmm, history6jmm, _1mm), (j, history6j, _01)) in snd6result]
>>> tr4result_ = lambda result:(result[0], tr4snd6result_(result[1]))
>>> ops7foldl = StatedTransformOps7foldl(lambda st, oresult6IN, /: pow(st, oresult6IN, M)) #lambda base, exp, /:pow(base, exp, M)
>>> ops7fork = StatedTransformOps7fork(False, [the_ops4transform7stated7echo, ops7foldl])
>>> M = 5*43
>>> #rp8pows = Reproduceable7tmay_prev_oresult([3], Reproduceable7foldl(lambda base, exp, /:pow(base, exp, M), 3, rp8exps))
>>> rp8exps = Reproduceable5seq([2,3,5,7], 0)
>>> rp8pows = Reproduceable7tmay_prev_oresult(((1, 3),), Reproduceable7transform_via_ops(ops7fork, (None, 3), rp8exps))
>>> list_fsts4reproduceable_(rp8pows)
[(2, 9), (3, 84), (5, 54), (7, 44)]
>>> def stZhistory2rank_(st7fold, /):
...     def history2rank_(history, /):
...         base = history.prev_oresult[1]
...         g = gcd(M, -1+pow(base, st7fold[0], M))
...         return -1 if g == 1 else (+1 if g == M else 0)
...     return history2rank_
>>> def op4fold_(prev_offset4key_point, offset4key_point, history6key_point, st7fold, /):
...     exp7key = history6key_point.prev_oresult[0]
...     return (exp7key*st7fold[0], (exp7key, st7fold[1]))
>>> saver = mk_history_saver_(200, 200, 999, -1)
>>> saver.append(rp8pows)
>>> saver.fills7unlimit_()
>>> result = saver.reversed_search_key_points_(stZhistory2rank_, op4fold_ , st7fold:=(1,()), offset=0)
>>> tr4result_(result)
((42, (2, (3, (7, ())))), [((3, -1), (4, 0)), ((1, -1), (2, 0)), ((0, -1), (1, 0))])
>>> result  #doctest: +ELLIPSIS
((42, (2, (3, (7, ())))), [((3, Reproduceable7tmay_prev_oresult(((5, 54),), ...), -1), (4, Reproduceable7tmay_prev_oresult(((7, 44),), ...), 0)), ((1, Reproduceable7tmay_prev_oresult(((2, 9),), ...), -1), (2, Reproduceable7tmay_prev_oresult(((3, 84),), ...), 0)), ((0, Reproduceable7tmay_prev_oresult(((1, 3),), ...), -1), (1, Reproduceable7tmay_prev_oresult(((2, 9),), ...), 0))])


>>> saver = mk_history_saver_(2, 2, 999, -1)
>>> saver.append(rp8pows)
>>> saver.fills7unlimit_()
>>> tr4result_(saver.reversed_search_key_points_(stZhistory2rank_, op4fold_ , st7fold:=(1,()), offset=0))
((42, (2, (3, (7, ())))), [((3, -1), (4, 0)), ((1, -1), (2, 0)), ((0, -1), (1, 0))])
>>> tr4result_(saver.reversed_search_key_points_(stZhistory2rank_, op4fold_ , st7fold:=(1,()), offset=1000))
((42, (2, (3, (7, ())))), [((1003, -1), (1004, 0)), ((1001, -1), (1002, 0)), ((1000, -1), (1001, 0))])





>>> _13s = [13]*1_00_00
>>> _17s = [17]*1_00_00
>>> rp8exps = Reproduceable5seq([*_13s, 2,*_17s,3,*_13s,5,7], 0)
>>> rp8pows = Reproduceable7tmay_prev_oresult(((1, 3),), Reproduceable7transform_via_ops(ops7fork, (None, 3), rp8exps))
>>> #list_fsts4reproduceable_(rp8pows)
>>> saver = mk_history_saver_(2, 2**10, 999, -1)
>>> saver.append(rp8pows)
>>> saver.fills7unlimit_()
>>> tr4result_(saver.reversed_search_key_points_(stZhistory2rank_, op4fold_ , st7fold:=(1,()), offset=0, _max_size7dense_6SparseHistorySaver=1+8, _max_size7physical_6SparseHistorySaver=1+64))
((42, (2, (3, (7, ())))), [((30003, -1), (30004, 0)), ((20001, -1), (20002, 0)), ((10000, -1), (10001, 0))])








>>> seed.types.HistorySaver._debug = False









py_adhoc_call   seed.types.HistorySaver   @f
]]]'''#'''
__all__ = r'''
mk_history_saver_
IHistorySaver
    EmptyError
    FullError
    IHistorySaver__bisect7single_array
        DenseHistorySaver
        SparseHistorySaver


'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.check import check_type_le, check_int_ge, check_int_ge_le, check_uint_lt, check_callable
    from bisect import bisect_right
    from functools import cache
    from itertools import islice
    from seed.types.Reproduceable import IReproduceable
    from seed.types.Reproduceable import iter_snds4reproduceable_ #iter_pairs4reproduceable_, iter_fsts4reproduceable_, 
    from seed.helper.repr_input import repr_helper, repr_helper_ex
    from seed.math.floor_ceil_tools.fc_perfect import perfect_div
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

class FullError(Exception):pass
class EmptyError(Exception):pass
#稀疏快照纟可重演序列
class IHistorySaver(ABC):
    r'''[[[
    '[history :: IReproduceable{record}]'
        history -->?? snapshot|footprint

    [sf.append(history):]
    [stZhistory2rank_ :: st7fold{k} -> history2rank_{k}]
    [history2rank_{k} :: history -> (-1|0|+1)]
    [history2rank_{k}(history{j}) <= history2rank_{k}(history{j})]
    [op4fold_ :: [[history2rank_{k}(history{-1+j}) == -1][history2rank_{k}(history{j}) >= 0]] => prev_history6key_point/history{-1+j} -> j/uint%(offset+size7apparent) -> history6key_point/history{j} -> st7fold{k} -> st7fold{1+k}{[history2rank_{1+k}(history{-1+j}) >= 0]}]
    [may_offsetted_rbegin == (None|offsetted_rbegin)]
    [offsetted_rbegin{k} :: uint{>=offset}{<offset+len(sf)}]
    [[history2rank_{-1+k}(history{offsetted_rbegin{k}}) == -1][history2rank_{k}(history{offsetted_rbegin{k}}) >= 0]]
    [offsetted_rbegin6sparse == offset+apparent_idx{from physical_idx}]
    [rbegin6sparse == apparent_idx{from physical_idx}]
    [may_offsetted_rbegin6sparse == (None|offsetted_rbegin6sparse)]
    [may_extra_output6recursive_ :: may (((offset,IHistorySaver)) -> None)]

    #]]]'''#'''
    __slots__ = ()
    # roll-back snapshot system
    r'''[[[
    ######################
    ######################
    #obsolete:
    ######################
    ######################
    # [history is reproduceable] => sparse ok
    [L:=max_size4storage][T:=max_size4history][step:=len_spacing]:
        bounded_dense_history{L;T:=L;step:=1}
        bounded_sparse_history{L;T:=L**2;step:=L}
        bounded_adaptive_equidistant_history{L;T;step:=T/L}
            [L%2==1]
            del ls[1::2]
                #间距/步长翻倍，保留首尾
        unbounded_adaptive_equidistant_history{L:=T**/2;T;step:=T**/2}
            L0:=step0
            if T0==L0*step0:
                del ls[1::2]
                step1:=2*step0
                    #间距/步长翻倍
                L1:=2*L0
                    #物理容量翻倍
                    #名义容量翻俩番


    #]]]'''#'''
    @property
    @abstractmethod
    def imay_max_size7apparent(sf, /):
        '-> imay uint'
    @property
    @abstractmethod
    def size7physical(sf, /):
        '-> uint'
    @property
    @abstractmethod
    def size7apparent(sf, /):
        '-> uint # [size7discard+size7physical == size7apparent]'
    @abstractmethod
    def _append6underfill_(sf, history, /):
        '[not .full] => history/IReproduceable{record} -> None'
    @abstractmethod
    def clear(sf, /):
        '-> None'
    @property
    @abstractmethod
    def head(sf, /):
        '-> history/IReproduceable{record} | ^EmptyError'
    @property
    @abstractmethod
    def last(sf, /):
        '-> history/IReproduceable{record} | ^EmptyError'

    @abstractmethod
    def _search7sparse_(sf, may_rbegin6sparse, history2rank_, /):
        'may rbegin6sparse/uint%size7physical -> (history -> (-1|0|+1)) -> (uint%6, i, j, may (i,history[i],-1), may (j,history[j],(0|+1)))/((0, i:history:-1, j:history:0)|(1, None, j:history:0)|(2, i:history:-1, j:history:+1)|(3, None, j:history:+1)|(4, i:history:-1, None)|(5, None, None)) # [0 <= i < j < (sf.size7apparent if may_rbegin6sparse is None else 1+rbegin6sparse)]'
    def search7sparse_(sf, history2rank_, /, *, offset=0, may_offsetted_rbegin6sparse=None):
        '(history -> (-1|0|+1)) -> (uint%6, i, j, may (i,history[i],-1), may (j,history[j],(0|+1)))/((0, i:history:-1, j:history:0)|(1, None, j:history:0)|(2, i:history:-1, j:history:+1)|(3, None, j:history:+1)|(4, i:history:-1, None)|(5, None, None)) # [offset+0 <= i < j < (offset+sf.size7apparent if may_offsetted_rbegin6sparse is None else 1+offsetted_rbegin6sparse)] # [may_offsetted_rbegin6sparse :: may offsetted_rbegin6sparse/uint%size7apparent]'
        #old:'(history -> (-1|0|+1)) -> (uint%6, may history, may history)/((0, history/-1, history/0)|(1, None, history/0)|(2, history/-1, history/+1)|(3, None, history/+1)|(4, history/-1, None)|(5, None, None))'
        may_rbegin6sparse = None if None is may_offsetted_rbegin6sparse else may_offsetted_rbegin6sparse -offset
        r = sf._search7sparse_(may_rbegin6sparse, history2rank_)
        if not (offset == 0 or not any(r[1:])):
            r = (r[0], *(((offset+m[0], *m[1:]) if not None is m else m) for m in r[1:]))
        return r

    def __len__(sf, /):
        '-> size7apparent'
        return sf.size7apparent
    @property
    def full(sf, /):
        '-> bool'
        return sf.size7apparent == sf.imay_max_size7apparent
    def append(sf, history, /):
        'history/IReproduceable{record} -> None|^FullError # [sf.last{new} is history][sf.head{new} is (if [sf.size7apparent{old} > 0] then sf.head{old} else history)][sf.size7apparent{new} == 1+sf.size7apparent{old}][[sf.size7physical{old} < 2] -> [sf.size7physical{new} == 1+sf.size7physical{old}]][[sf.size7physical{old} >= 2] -> [sf.size7physical{new} >= 2]]'
        check_type_le(IReproduceable, history)
        if sf.full: raise FullError
        sf._append6underfill_(history)
    def fills_(sf, sz, /):
        'uint -> None|^FullError|^EmptyError'
        check_int_ge(0, sz)
        history = sf.last
            # ^EmptyError
        for history in islice(iter_snds4reproduceable_(history), 0, sz):
            sf.append(history)
                # ^FullError
    def fills7unlimit_(sf, /):
        '-> None|^EmptyError'
        if sf.full: return
        history = sf.last
            # ^EmptyError
        for history in iter_snds4reproduceable_(history):
            sf.append(history)
            if sf.full: return
    def both_fills7unlimit_(sf, ot, /):
        '-> None|^EmptyError # expected: [ot.imay_max_size7apparent == -1]'
        #vs:fills7unlimit_
        history = sf.last
            # ^EmptyError
        _history = ot.last
            # ^EmptyError
        if not history is _history:raise ValueError
        if sf.full: return
        if ot.full: return

        for history in iter_snds4reproduceable_(history):
            sf.append(history)
            ot.append(history)
            if sf.full: return
            if ot.full: return
    def clear_but_last_(sf, /):
        '-> None # [[sf.size7apparent{old} > 0] -> [[sf.head{new} is sf.last{new} is sf.last{old}][sf.size7apparent{new} == 1][sf.size7physical{new} == 1]]] # [extern:offset{sf} += max(0,-1+sf.size7apparent{old})]'
        if sf:
            last = sf.last
            sf.clear()
            sf.append(last)

    def search7dense_(sf, history2rank_, /, *, offset=0, may_offsetted_rbegin6sparse=None, zero6sparse_ok=False, recursive=True, validate6recursive=False, may_extra_output6recursive_=None, _max_size7dense_6SparseHistorySaver=2049, _max_size7physical_6SparseHistorySaver=65537):
        '(history -> (-1|0|+1)) -> (uint%6, i, j, may (i,history[i],-1), may (j,history[j],(0|+1)))/((0, i:history:-1, j:history:0)|(1, None, j:history:0)|(2, i:history:-1, j:history:+1)|(3, None, j:history:+1)|(4, i:history:-1, None)|(5, None, None)) # [offset+0 <= i < j < offset+sf.size7apparent] # [not zero6sparse_ok => [i+1==j]]'
        #old:'(history -> (-1|0|+1)) -> (uint%6, may history, may history)/((0, history/-1, history/0)|(1, None, history/0)|(2, history/-1, history/+1)|(3, None, history/+1)|(4, history/-1, None)|(5, None, None))'
        if not None is may_extra_output6recursive_:
            extra_output6recursive_ = may_extra_output6recursive_
            if not recursive:raise TypeError('[not recursive][not None is may_extra_output6recursive_]')
            #check_callable(extra_output6recursive_)
            extra_output6recursive_((offset, sf))
        # [may_extra_output6recursive_ :: may (((offset,IHistorySaver)) -> None)]
        # old:[may_extra_output6recursive_ :: may (((offset,IHistorySaver,[may_offsetted_rbegin6sparse,may_offsetted_rlast6sparse,may_offsetted_rend6sparse])) -> None)]
        r = sf.search7sparse_(history2rank_, offset=offset, may_offsetted_rbegin6sparse=may_offsetted_rbegin6sparse)
        match r:
            case ((0|2) as k, (i, history7neg_one, _neg_one), (j, history7zero_or_one, _zero_or_one)):
                assert _neg_one == -1
                assert _zero_or_one in (0,+1)
                assert None is may_offsetted_rbegin6sparse or j <= may_offsetted_rbegin6sparse, (sf, offset, r, may_offsetted_rbegin6sparse, j)

                sz = 1+j-i
                assert sz >= 2
                if sz == 2:
                    # [i+1 == j]
                    # base_case:recursive
                    new_r = r
                elif zero6sparse_ok and k == 0:
                    new_r = r
                elif recursive:
                    # recursive{base_case <==> [sz==2]}
                    # =>new API with apparent_idx
                    # =>apparent_idx5physical_idx4history_array_()
                    # =>kw:offset

                    #ot = SparseHistorySaver(2049, 65537, sz)
                        # ^TypeError
                    #ot = SparseHistorySaver(2049, 65537, -1)
                    ot = SparseHistorySaver(_max_size7dense_6SparseHistorySaver, _max_size7physical_6SparseHistorySaver, -1)

                    ot.append(history7neg_one)
                    ot.fills_(sz-1)
                    offset4ot = i
                    new_r = ot.search7dense_(history2rank_, offset=offset4ot, may_offsetted_rbegin6sparse=None, zero6sparse_ok=zero6sparse_ok, recursive=recursive, may_extra_output6recursive_=may_extra_output6recursive_)
                    _k = new_r[0]
                    if not (_k == 0 or _k == k):raise 000
                    if validate6recursive:
                        new_r7non_recursive = sf.search7dense_(history2rank_, offset=offset, may_offsetted_rbegin6sparse=may_offsetted_rbegin6sparse, zero6sparse_ok=zero6sparse_ok, recursive=not recursive, validate6recursive=not validate6recursive)
                        _check_result5search7dense_(may_offsetted_rbegin6sparse, zero6sparse_ok, new_r, new_r7non_recursive)
                else:
                    # not recursive
                    # !! sz{may_offsetted_rbegin6sparse}
                    new_r = _search7dense6non_recursive_(history2rank_, history7neg_one, sz, i, j, _zero_or_one, k)
                new_r
            case _:
                new_r = r
        return new_r
    def reversed_search_key_points_(sf, stZhistory2rank_, op4fold_, st7fold, /, *, offset=0, _max_size7dense_6SparseHistorySaver=2049, _max_size7physical_6SparseHistorySaver=65537):
        '[sf.size7apparent > 0][stZhistory2rank_(st7fold)(sf.last) >= 0] => ... -> (st7fold, [((-1+offset4key_point, history{-1+offset4key_point}, -1), (offset4key_point, history{offset4key_point}, (0|+1)))])'
        #unwind,rollback
        if not sf:raise EmptyError
        # [sf.size7apparent > 0]
        history2rank_ = stZhistory2rank_(st7fold)
        if not (rank_0_6last:=history2rank_(sf.last)) in (0,+1):raise ValueError(sf, sf.last, st7fold, rank_0_6last)
        # [stZhistory2rank_(st7fold)(sf.last) >= 0]



        ls4key_record_ex = []
            # [((-1+j, history{-1+j}, -1), (j, key_point/history{j}), (0|+1))]
        if (rank_0_6head:=history2rank_(sf.head)) in (0,+1):
            return (st7fold, ls4key_record_ex)
        if not rank_0_6head == -1:raise ValueError(sf, sf.head, st7fold, rank_0_6head)
        # [stZhistory2rank_(st7fold)(sf.head) == -1]


        ls4offsetted_saver = []
            # [(offset, IHistorySaver)]
        777;extra_output6recursive_=ls4offsetted_saver.append
        if 0:
            def extra_output6recursive_(x, /):
                (offset4ot, ot) = x
                check_type_is(int, offset4ot)
                check_type_le(IHistorySaver, ot)
                ls4offsetted_saver.append(x)
                return None
        kwds = dict(may_extra_output6recursive_=extra_output6recursive_, zero6sparse_ok=False, recursive=True, validate6recursive=False, _max_size7dense_6SparseHistorySaver=2049, _max_size7physical_6SparseHistorySaver=65537)

        extra_output6recursive_((offset, sf))
        777;may_offsetted_rbegin6sparse = None
        while 1:
            # [len(ls4offsetted_saver) > 0]
            # [-1 == history2rank_(ls4offsetted_saver[-1][-1].head)]
            # [(0|+1) == history2rank_(ls4offsetted_saver[-1][-1].last{@may_offsetted_rbegin6sparse})]
            (offset4ot, ot) = ls4offsetted_saver.pop()
            r = ot.search7dense_(history2rank_, offset=offset4ot, may_offsetted_rbegin6sparse=may_offsetted_rbegin6sparse, **kwds)
            777;ls4offsetted_saver#filled
            # [len(ls4offsetted_saver) > 0]
            assert r[0] < 4, r
            assert r[2] is not None, r
            if r[1] is None:
                assert r[0] in (1,3)
                # [(0|+1) == history2rank_(ls4offsetted_saver[-1][-1].head)]
                (may_offsetted_rbegin6sparse, _) = ls4offsetted_saver.pop()
                # [(0|+1) == history2rank_(ls4offsetted_saver[-1][-1].last{@may_offsetted_rbegin6sparse})]
                while ls4offsetted_saver:
                    if -1 == history2rank_(ls4offsetted_saver[-1][-1].head):break
                    # [(0|+1) == history2rank_(ls4offsetted_saver[-1][-1].head)]
                    (may_offsetted_rbegin6sparse, _) = ls4offsetted_saver.pop()
                    # [(0|+1) == history2rank_(ls4offsetted_saver[-1][-1].last{@may_offsetted_rbegin6sparse})]
                else:
                    return (st7fold, ls4key_record_ex)
                    break
                # [len(ls4offsetted_saver) > 0]
                # [-1 == history2rank_(ls4offsetted_saver[-1][-1].head)]
                # [(0|+1) == history2rank_(ls4offsetted_saver[-1][-1].last{@may_offsetted_rbegin6sparse})]
                continue
            assert r[1] is not None, r
            assert r[0] in (0,2)
            #########
            # found key_point
            #########
            match r:
                case ((0|2), (prev_offset4key_point, prev_history6key_point, -1) as _prev_key_record, (offset4key_point, history6key_point, (0|1)) as _key_record):
                    assert 1+prev_offset4key_point == offset4key_point
                case _:
                    raise Exception(sf, ot, st7fold, r)
            offsetted_rend6sparse = prev_offset4key_point
            offsetted_rlast6sparse = offset4key_point
            ls4key_record_ex.append((_prev_key_record, _key_record))
            #########
            # search prev key_point
            #########
            # !! [offsetted_rbegin6sparse{k round search} = offsetted_rend6sparse{k-1 round search}]
            offsetted_rbegin6sparse = offsetted_rend6sparse
            777;may_offsetted_rbegin6sparse = offsetted_rbegin6sparse
            st7fold = op4fold_(prev_history6key_point, offset4key_point, history6key_point, st7fold)
            history2rank_ = stZhistory2rank_(st7fold)
            if not history2rank_(prev_history6key_point) in (0,1):raise Exception(sf, r, st7fold)
            continue
        raise 000






def _extract_mayidc_result5search7dense_(r, /):
    match r:
        case (_, _, None):
            may_offsetted_rlast6sparse = None
        case (_, _, (offsetted_rlast6sparse, _, _)):
            may_offsetted_rlast6sparse = offsetted_rlast6sparse
        case _:
            raise TypeError(r)
    match r:
        case (_, None, _):
            may_offsetted_rend6sparse = None
        case (_, (offsetted_rend6sparse, _, _), _):
            may_offsetted_rend6sparse = offsetted_rend6sparse
        case _:
            raise TypeError(r)
    return (may_offsetted_rend6sparse, may_offsetted_rlast6sparse)
def _check_result5search7dense_(may_offsetted_rbegin6sparse, zero6sparse_ok, new_r7recursive, new_r7non_recursive, /):
    (k1, (i1, _, _1_neg1), (j1, _, rank1)) = new_r7recursive
    (k2, (i2, _, _2_neg1), (j2, _, rank2)) = new_r7non_recursive
    assert _1_neg1 == -1
    assert _2_neg1 == -1
    assert k1 in (0,2)
    assert k2 in (0,2)
    #assert 0 <= k2 <= k1 <= 2
    assert 0 <= k2 == k1 <= 2
    assert 0 <= rank2 == rank1 <= 1
    assert 0 <= i1 <= i2 == -1+j2 < j2 <= j1
    assert (zero6sparse_ok and rank2 == rank1 == 0) or 0 <= i1 == i2 == -1+j2 < j2 == j1
    assert None is may_offsetted_rbegin6sparse or j2 <= j1 <= may_offsetted_rbegin6sparse
def _search7dense6non_recursive_(history2rank_, history7neg_one, sz, i, j, _zero_or_one, k, /):
    for _j, history in enumerate(islice(iter_snds4reproduceable_(history7neg_one), 0, sz), 1+i):
        rank = history2rank_(history)
        if not -1 == rank: break
        history7neg_one = history
    else:
        raise 000
    if not 0 <= rank <= _zero_or_one:raise 000
    if not i < _j <= j:raise 000
    _i = -1+_j
    _k = 0 if rank == 0 else 2
    if not (_k == 0 or _k == k):raise 000
    new_r = (_k, (_i, history7neg_one, -1), (_j, history, rank))
    return new_r
class IHistorySaver__bisect7single_array(IHistorySaver):
    __slots__ = ()
    @property
    @abstractmethod
    def _history_array_view_(sf, /):
        '-> [history]'
    @abstractmethod
    def _apparent_idx5physical_idx4history_array_(sf, physical_idx, /):
        'physical_idx/uint%size7physical -> apparent_idx/uint%size7apparent'
    @abstractmethod
    def _physical_idx5apparent_idx6sparse4history_array_(sf, apparent_idx6sparse, /):
        'apparent_idx6sparse{from physical_idx}/uint%size7apparent -> physical_idx/uint%size7physical # [apparent_idx6sparse == sf._apparent_idx5physical_idx4history_array_(physical_idx)]'
    @property
    @override
    def head(sf, /):
        ls = sf._history_array_view_
        if not ls:raise EmptyError
        return ls[0]
    @property
    @override
    def last(sf, /):
        ls = sf._history_array_view_
        if not ls:raise EmptyError
        return ls[-1]
    def physical_idx5apparent_idx6sparse4history_array_(sf, apparent_idx6sparse, /):
        'apparent_idx6sparse{from physical_idx}/uint%size7apparent -> physical_idx/uint%size7physical # [apparent_idx6sparse == sf._apparent_idx5physical_idx4history_array_(physical_idx)]'
        check_uint_lt(sf.size7apparent, apparent_idx6sparse)
        physical_idx = sf._physical_idx5apparent_idx6sparse4history_array_(apparent_idx6sparse)
        check_uint_lt(sf.size7physical, physical_idx)
        apparent_idx = sf._apparent_idx5physical_idx4history_array_(physical_idx)
        if not apparent_idx == apparent_idx6sparse:raise Exception(sf, physical_idx, apparent_idx6sparse, apparent_idx)
        return physical_idx
    def apparent_idx5physical_idx4history_array_(sf, physical_idx, /):
        'physical_idx/uint%size7physical -> apparent_idx/uint%size7apparent'
        check_uint_lt(sf.size7physical, physical_idx)
        apparent_idx = sf._apparent_idx5physical_idx4history_array_(physical_idx)
        check_uint_lt(sf.size7apparent, apparent_idx)
        #assert 0 <= physical_idx <= apparent_idx < sf.size7apparent
        return apparent_idx
    @override
    def _search7sparse_(sf, may_rbegin6sparse, history2rank_, /):
        ls = sf._history_array_view_
        j2rank_ = _mk_j2rank_(history2rank_, ls)
        L = len(ls)
        js = range(L)
        end = L if None is may_rbegin6sparse else 1+sf.physical_idx5apparent_idx6sparse4history_array_(may_rbegin6sparse)
        assert 0 <= end <= L
        j = bisect_right(js, -1, begin:=0, end, key=j2rank_)
        #check_uint_lt(1+L, j)
        check_uint_lt(1+end, j)
        if j == end:
            #if j == L:
            m2 = None
            k2 = 4
        else:
            jjj = sf.apparent_idx5physical_idx4history_array_(j)
            r2 = j2rank_(j)
            m2 = (jjj, ls[j], r2)
            match r2:
                case 1:
                    k2 = 2
                case 0:
                    k2 = 0
                case -1:
                    raise 000
                case _:
                    raise 000
        m2, k2
        if j == 0:
            m1 = None
            k1 = 1
        else:
            i = j-1
            iii = sf.apparent_idx5physical_idx4history_array_(i)
            r1 = j2rank_(i)
            m1 = (iii, ls[i], r1)
            match r1:
                case -1:
                    k1 = 0
                case 1:
                    raise 000
                case 0:
                    raise 000
                case _:
                    raise 000
        m1, k1
        return (k2+k1, m1, m2)
def _mk_j2rank_(history2rank_, history_array, /):
    ls = history_array
    @cache
    def j2rank_(j, /):
        history = ls[j]
        check_type_le(IReproduceable, history)
        rank = history2rank_(history)
        check_int_ge_le(-1, +1, rank)
        return rank
    return j2rank_

class DenseHistorySaver(IHistorySaver__bisect7single_array):
    ___no_slots_ok___ = True
    def __init__(sf, max_size7apparent, /):
        check_int_ge(1, max_size7apparent)
        sf._m = max_size7apparent
        sf._ls = []
    def __repr__(sf, /):
        max_size7apparent = sf._m
        history_array = sf._ls
        #return f'DenseHistorySaver({max_size7apparent!r}, history_array = {history_array!r})'
        #return repr_helper(sf, max_size7apparent, history_array=history_array)
        return repr_helper_ex(sf, [max_size7apparent], 'history_array'.split(), {}, ordered_attrs_only=True, compact6kwargs=True, vars4self=locals())
    @property
    @override
    def imay_max_size7apparent(sf, /):
        return sf._m
    @property
    @override
    def size7physical(sf, /):
        return len(sf._ls)
    @property
    @override
    def size7apparent(sf, /):
        return len(sf._ls)
    @override
    def _append6underfill_(sf, history, /):
        sf._ls.append(history)

    @override
    def clear(sf, /):
        sf._ls.clear()
    @property
    @override
    def _history_array_view_(sf, /):
        return sf._ls
    @override
    def _apparent_idx5physical_idx4history_array_(sf, physical_idx, /):
        apparent_idx = physical_idx
        return apparent_idx
    @override
    def _physical_idx5apparent_idx6sparse4history_array_(sf, apparent_idx6sparse, /):
        physical_idx = apparent_idx6sparse
        return physical_idx


_debug = True
_debug = False
class SparseHistorySaver(IHistorySaver__bisect7single_array):
    ___no_slots_ok___ = True
    def __init__(sf, max_size7dense, max_size7physical, imay_max_size7apparent, /):
        check_int_ge(2, max_size7dense)
        check_int_ge(max_size7dense, max_size7physical)
        check_int_ge(-1, imay_max_size7apparent)
        if not -1 == imay_max_size7apparent:
            check_int_ge(max_size7physical, imay_max_size7apparent)
        sf._msz0 = max_size7dense
        sf._msz1 = max_size7physical
        sf._imsz2 = imay_max_size7apparent
        sf._ls = []
        sf.clear()
    @override
    def clear(sf, /):
        sf._ls.clear()
        sf._sz = 0
        sf._msz = sf._msz0
        sf._step = 1
        sf._cn = 1
        if _debug:sf.validate()
    def validate(sf, /):
        # [1 <= _cn <= _step]
        # [0 <= len(ls) <= _msz]
        # [_msz0 <= _msz <= _msz1]
        # [[_imsz2 =!= -1] -> [_sz <= _imsz2]]
        # [_sz == [len(_ls) >= 1] +[len(_ls) >= 2]*(_cn+(len(_ls)-2)*_step)]
        max_size7dense = sf._msz0
        max_size7physical = sf._msz1
        imay_max_size7apparent = sf._imsz2
        history_array = sf._ls
        size7apparent = sf._sz
        curr_max_size7physical = sf._msz
        curr_step = sf._step
        last_step = sf._cn
        assert 1 <= last_step <= curr_step
        assert len(history_array) <= curr_max_size7physical
        assert 2 <= max_size7dense <= curr_max_size7physical <= max_size7physical
        assert imay_max_size7apparent == -1 or size7apparent <= imay_max_size7apparent
        assert size7apparent == (__:=(len(history_array) >= 1)*(1) + (len(history_array) >= 2)*(+last_step +(len(history_array)-2)*curr_step)), (__, size7apparent, (len(history_array), curr_step), last_step)
    def __repr__(sf, /):
        max_size7dense = sf._msz0
        max_size7physical = sf._msz1
        imay_max_size7apparent = sf._imsz2
        history_array = sf._ls
        size7apparent = sf._sz
        curr_max_size7physical = sf._msz
        curr_step = sf._step
        last_step = sf._cn
        #return f'SparseHistorySaver({max_size7dense!r}, {max_size7physical!r}, {imay_max_size7apparent!r}, history_array = {history_array!r}, size7apparent = {size7apparent!r}, curr_max_size7physical = {curr_max_size7physical!r}, curr_step = {curr_step!r}, last_step = {last_step!r})'
        #return repr_helper(sf, max_size7dense, max_size7physical, imay_max_size7apparent, history_array=history_array, size7apparent=size7apparent, curr_max_size7physical=curr_max_size7physical, curr_step=curr_step, last_step=last_step)
        return repr_helper_ex(sf, [max_size7dense, max_size7physical, imay_max_size7apparent], 'history_array,size7apparent,curr_max_size7physical,curr_step,last_step'.split(','), {}, ordered_attrs_only=True, compact6kwargs=True, vars4self=locals())


    @property
    @override
    def imay_max_size7apparent(sf, /):
        return sf._imsz2
    @property
    @override
    def size7physical(sf, /):
        return len(sf._ls)
    @property
    @override
    def size7apparent(sf, /):
        return sf._sz
    @override
    def _append6underfill_(sf, history, /):
        if _debug:sf.validate()
        cn = sf._cn
        ls = sf._ls
        hstep = sf._step
        if cn == hstep:
            if len(ls) == sf._msz:
                odd = 1&len(ls)
                dstep = hstep << 1
                cn = 1 if odd else 1+hstep
                del ls[1::2]
                777;sf._step = dstep
                sf._msz = min(sf._msz1, sf._msz<<1)
            else:
                cn = 1
            # !! [max_size7physical >= 2]
            if len(ls) >= sf._msz: raise 000
            ls.append(history)
        elif not ls:
            # !! [max_size7dense >= 1]
            ls.append(history)
            cn = hstep
        else:
            # !! [max_size7dense >= 2]
            assert len(ls) >= 2
            ls[-1] = history
            cn += 1

        sf._sz += 1
        sf._cn = cn
        if _debug:sf.validate()
    @property
    @override
    def _history_array_view_(sf, /):
        return sf._ls
    @override
    def _apparent_idx5physical_idx4history_array_(sf, physical_idx, /):
        curr_step = sf._step
        last_step = sf._cn
        #bug:apparent_idx = 0 if 0 == physical_idx else last_step + curr_step*(-1+physical_idx)
        apparent_idx = curr_step*physical_idx if not sf.size7physical == 1+physical_idx else last_step + curr_step*(-1+physical_idx)
        #assert 0 <= physical_idx <= apparent_idx < sf.size7apparent
        return apparent_idx
    @override
    def _physical_idx5apparent_idx6sparse4history_array_(sf, apparent_idx6sparse, /):
        curr_step = sf._step
        last_step = sf._cn
        # !! [apparent_idx = curr_step*physical_idx if not sf.size7physical == 1+physical_idx else last_step + curr_step*(-1+physical_idx)]
        physical_idx = perfect_div(apparent_idx6sparse, curr_step) if not sf.size7apparent == 1+apparent_idx6sparse else 1+perfect_div(apparent_idx6sparse-last_step, curr_step)
        return physical_idx
    def validate7apparent_idx(sf, /):
        if not sf:return
        curr_step = sf._step
        last_step = sf._cn
        for physical_idx, apparent_idx in zip(range(sf.size7physical-1), range(0, sf.size7apparent, curr_step)):
            assert apparent_idx == sf.apparent_idx5physical_idx4history_array_(physical_idx)
        physical_idx = sf.size7physical-1
        apparent_idx = len(sf)-1
        assert apparent_idx == sf.apparent_idx5physical_idx4history_array_(physical_idx)

def mk_history_saver_(max_size7dense, max_size7physical, cost_per_detect, imay_detect_period, /):
    check_int_ge(2, max_size7dense)
    check_int_ge(max_size7dense, max_size7physical)
    check_int_ge(1, cost_per_detect)
    check_int_ge(-1, imay_detect_period)
    if 0 == imay_detect_period:
        #auto
        #detect_period = n.bit_length()
        imay_detect_period = detect_period = cost_per_detect

    match imay_detect_period:
        case -1:
            #detect_once6stage1
            imay_max_size7apparent = -1
            history_saver = SparseHistorySaver(max_size7dense, max_size7physical, imay_max_size7apparent)
        case 0:
            raise 000
        case detect_period:
            detect_period
            max_size7apparent = 1+detect_period
                # !! .clear_but_last_()
            if max_size7apparent <= max_size7physical:
                history_saver = DenseHistorySaver(max_size7apparent)
            else:
                history_saver = SparseHistorySaver(max_size7dense, max_size7physical, max_size7apparent)

    return history_saver


__all__
from seed.types.HistorySaver import EmptyError, FullError
from seed.types.HistorySaver import IHistorySaver, IHistorySaver__bisect7single_array
from seed.types.HistorySaver import DenseHistorySaver, SparseHistorySaver, mk_history_saver_
from seed.types.HistorySaver import *
