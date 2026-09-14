#__all__:goto
#TODO:goto
#print_methods7py:goto
#_debug:goto
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
[[
come_from:
e ../../python3_src/seed/algo/rho_method__7iter7batch.py

@20260906
DONE:IHistorySaver7immutable:
    * used to resume@KeyboardInterrupt@rho_method
    * finer search IIdiffs intead of "bad_state"@[1==gcd(IIdiffs{batch},modulus)]
view ../../python3_src/seed/types/SinglyLinkedList.py
]]



%s/^SparseHistorySaver(\(\d\+, \d\+, -\?\d\+\), history_array=\[\], size7apparent=\(\d\+\), curr_max_size7physical=\(\d\+\), curr_step=\(\d\+\), last_step=\(\d\+\))/SparseHistorySaver(\1)
%s/^SparseHistorySaver(\(\d\+, \d\+, -\?\d\+\), history_array=\([^=]*\), size7apparent=\(\d\+\), curr_max_size7physical=\(\d\+\), curr_step=\(\d\+\), last_step=\(\d\+\))/SparseHistorySaver(\1, (\2, \3, \4, \5, \6))
    [payload :: may (history_array, size7apparent, curr_max_size7physical, curr_step, last_step)]

%s/^DenseHistorySaver(\(\d\+\), history_array=\[\])/DenseHistorySaver(\1)
%s/^DenseHistorySaver(\(\d\+\), history_array=\(\[[^=]*\]\))/DenseHistorySaver(\1, \2)

++danger_mark
%s/^DenseHistorySaver(\(\d\+\), \(\[.*\]\))/DenseHistorySaver(\1, '!', \2)
%s/^SparseHistorySaver(\(\d\+, \d\+, -\?\d\+\), \((.*)\))/SparseHistorySaver(\1, '!', \2)

%s/^SparseHistorySaver7immutable((\([^()]*\)), \((.*)\))/SparseHistorySaver7immutable(\1, '!', \2)


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
DenseHistorySaver(4, '!', [Reproduceable5seq('0123456789', 0), Reproduceable5seq('0123456789', 1), Reproduceable5seq('0123456789', 2), Reproduceable5seq('0123456789', 3)])
>>> saver.clear_but_last_()
>>> saver.fills_(3)
>>> saver
DenseHistorySaver(4, '!', [Reproduceable5seq('0123456789', 3), Reproduceable5seq('0123456789', 4), Reproduceable5seq('0123456789', 5), Reproduceable5seq('0123456789', 6)])
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
SparseHistorySaver(2, 3, -1, '!', ([Reproduceable5seq('0123456789', 0), Reproduceable5seq('0123456789', 2), Reproduceable5seq('0123456789', 3)], 4, 3, 2, 1))
>>> saver.fills_(3)
>>> saver
SparseHistorySaver(2, 3, -1, '!', ([Reproduceable5seq('0123456789', 0), Reproduceable5seq('0123456789', 4), Reproduceable5seq('0123456789', 6)], 7, 3, 4, 2))
>>> saver.fills_(2)
>>> saver
SparseHistorySaver(2, 3, -1, '!', ([Reproduceable5seq('0123456789', 0), Reproduceable5seq('0123456789', 4), Reproduceable5seq('0123456789', 8)], 9, 3, 4, 4))
>>> saver.fills_(2)
>>> saver
SparseHistorySaver(2, 3, -1, '!', ([Reproduceable5seq('0123456789', 0), Reproduceable5seq('0123456789', 8), Reproduceable5seq('0123456789', 10)], 11, 3, 8, 2))

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
SparseHistorySaver(2, 4, -1, '!', ([Reproduceable5seq('0123456789', 0), Reproduceable5seq('0123456789', 2), Reproduceable5seq('0123456789', 3)], 4, 4, 2, 1))
>>> saver.fills_(3)
>>> saver
SparseHistorySaver(2, 4, -1, '!', ([Reproduceable5seq('0123456789', 0), Reproduceable5seq('0123456789', 2), Reproduceable5seq('0123456789', 4), Reproduceable5seq('0123456789', 6)], 7, 4, 2, 2))
>>> saver.fills_(2)
>>> saver
SparseHistorySaver(2, 4, -1, '!', ([Reproduceable5seq('0123456789', 0), Reproduceable5seq('0123456789', 4), Reproduceable5seq('0123456789', 8)], 9, 4, 4, 4))
>>> saver.fills_(2)
>>> saver
SparseHistorySaver(2, 4, -1, '!', ([Reproduceable5seq('0123456789', 0), Reproduceable5seq('0123456789', 4), Reproduceable5seq('0123456789', 8), Reproduceable5seq('0123456789', 10)], 11, 4, 4, 2))

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
SparseHistorySaver(2, 17, -1, '!', ([Reproduceable5seq(range(0, 2048), 0), Reproduceable5seq(range(0, 2048), 128), Reproduceable5seq(range(0, 2048), 256), Reproduceable5seq(range(0, 2048), 384), Reproduceable5seq(range(0, 2048), 512), Reproduceable5seq(range(0, 2048), 640), Reproduceable5seq(range(0, 2048), 768), Reproduceable5seq(range(0, 2048), 896), Reproduceable5seq(range(0, 2048), 1024), Reproduceable5seq(range(0, 2048), 1152), Reproduceable5seq(range(0, 2048), 1280), Reproduceable5seq(range(0, 2048), 1408), Reproduceable5seq(range(0, 2048), 1536), Reproduceable5seq(range(0, 2048), 1664), Reproduceable5seq(range(0, 2048), 1792), Reproduceable5seq(range(0, 2048), 1920), Reproduceable5seq(range(0, 2048), 2048)], 2049, 17, 128, 128))
>>> saver.fills7unlimit_()


>>> history0 = Reproduceable5seq(range(2**11), 0)
>>> saver = SparseHistorySaver(2, 16, -1)
>>> saver.append(history0)
>>> saver.fills_(2**11)
>>> saver.validate()
>>> saver
SparseHistorySaver(2, 16, -1, '!', ([Reproduceable5seq(range(0, 2048), 0), Reproduceable5seq(range(0, 2048), 256), Reproduceable5seq(range(0, 2048), 512), Reproduceable5seq(range(0, 2048), 768), Reproduceable5seq(range(0, 2048), 1024), Reproduceable5seq(range(0, 2048), 1280), Reproduceable5seq(range(0, 2048), 1536), Reproduceable5seq(range(0, 2048), 1792), Reproduceable5seq(range(0, 2048), 2048)], 2049, 16, 256, 256))










>>> history0 = Reproduceable5seq(range(160), 0)
>>> saver = SparseHistorySaver(2, 8, 64)
>>> saver.append(history0)
>>> saver.fills7unlimit_()
>>> saver.validate()
>>> saver
SparseHistorySaver(2, 8, 64, '!', ([Reproduceable5seq(range(0, 160), 0), Reproduceable5seq(range(0, 160), 16), Reproduceable5seq(range(0, 160), 32), Reproduceable5seq(range(0, 160), 48), Reproduceable5seq(range(0, 160), 63)], 64, 8, 16, 15))

>>> saver.clear_but_last_()
>>> saver.fills7unlimit_()
>>> saver.validate()
>>> saver
SparseHistorySaver(2, 8, 64, '!', ([Reproduceable5seq(range(0, 160), 63), Reproduceable5seq(range(0, 160), 79), Reproduceable5seq(range(0, 160), 95), Reproduceable5seq(range(0, 160), 111), Reproduceable5seq(range(0, 160), 126)], 64, 8, 16, 15))

>>> saver.clear_but_last_()
>>> saver.fills7unlimit_()
>>> saver.validate()
>>> saver
SparseHistorySaver(2, 8, 64, '!', ([Reproduceable5seq(range(0, 160), 126), Reproduceable5seq(range(0, 160), 134), Reproduceable5seq(range(0, 160), 142), Reproduceable5seq(range(0, 160), 150), Reproduceable5seq(range(0, 160), 158), Reproduceable5seq(range(0, 160), 160)], 35, 8, 8, 2))




>>> mk_history_saver_(2, 8, 999, -1)
SparseHistorySaver(2, 8, -1)
>>> mk_history_saver_(2, 8, 999, 0)
SparseHistorySaver(2, 8, 1000)
>>> mk_history_saver_(2, 8, 999, 1)
DenseHistorySaver(2)
>>> mk_history_saver_(2, 8, 999, 7)
DenseHistorySaver(8)
>>> mk_history_saver_(2, 8, 999, 8)
SparseHistorySaver(2, 8, 9)
>>> mk_history_saver_(2, 8, 999, 9)
SparseHistorySaver(2, 8, 10)












search7dense_
backward_search_key_points_
    def backward_search_key_points_(sf, stZhistory2rank_, op4fold_, st7fold, /, *, offset=0, _max_size7dense_6SparseHistorySaver=2049, _max_size7physical_6SparseHistorySaver=65537):
3%(5*43)
[order_mod_(5;3) == 4 == 2*2]
[order_mod_(43;3) == 42 == 2*3*7]

>>> from math import gcd
>>> from seed.types.Reproduceable import Reproduceable7transform_via_ops, Reproduceable7tmay_prev_oresult# Reproduceable7foldl
>>> from seed.types.Reproduceable import list_fsts4reproduceable_
>>> from seed.types.Reproduceable import the_ops4transform7stated7echo, StatedTransformOps7foldl, StatedTransformOps7fork
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
>>> result = saver.backward_search_key_points_(stZhistory2rank_, op4fold_ , st7fold:=(1,()), offset=0)
>>> tr4result_(result)
((42, (2, (3, (7, ())))), [((3, -1), (4, 0)), ((1, -1), (2, 0)), ((0, -1), (1, 0))])
>>> result  #doctest: +ELLIPSIS
((42, (2, (3, (7, ())))), [((3, Reproduceable7tmay_prev_oresult(((5, 54),), ...), -1), (4, Reproduceable7tmay_prev_oresult(((7, 44),), ...), 0)), ((1, Reproduceable7tmay_prev_oresult(((2, 9),), ...), -1), (2, Reproduceable7tmay_prev_oresult(((3, 84),), ...), 0)), ((0, Reproduceable7tmay_prev_oresult(((1, 3),), ...), -1), (1, Reproduceable7tmay_prev_oresult(((2, 9),), ...), 0))])


>>> saver = mk_history_saver_(2, 2, 999, -1)
>>> saver.append(rp8pows)
>>> saver.fills7unlimit_()
>>> tr4result_(saver.backward_search_key_points_(stZhistory2rank_, op4fold_ , st7fold:=(1,()), offset=0))
((42, (2, (3, (7, ())))), [((3, -1), (4, 0)), ((1, -1), (2, 0)), ((0, -1), (1, 0))])
>>> tr4result_(saver.backward_search_key_points_(stZhistory2rank_, op4fold_ , st7fold:=(1,()), offset=1000))
((42, (2, (3, (7, ())))), [((1003, -1), (1004, 0)), ((1001, -1), (1002, 0)), ((1000, -1), (1001, 0))])





>>> _13s = [13]*1_00_00
>>> _17s = [17]*1_00_00
>>> rp8exps = Reproduceable5seq([*_13s, 2,*_17s,3,*_13s,5,7], 0)
>>> rp8pows = Reproduceable7tmay_prev_oresult(((1, 3),), Reproduceable7transform_via_ops(ops7fork, (None, 3), rp8exps))
>>> #list_fsts4reproduceable_(rp8pows)
>>> saver = mk_history_saver_(2, 2**10, 999, -1)
>>> saver.append(rp8pows)
>>> saver.fills7unlimit_()
>>> tr4result_(saver.backward_search_key_points_(stZhistory2rank_, op4fold_ , st7fold:=(1,()), offset=0, _max_size7dense_6SparseHistorySaver=1+8, _max_size7physical_6SparseHistorySaver=1+64))
((42, (2, (3, (7, ())))), [((30003, -1), (30004, 0)), ((20001, -1), (20002, 0)), ((10000, -1), (10001, 0))])









@20260905
fmap_
>>> history0 = Reproduceable5seq(range(160), 0)
>>> saver = SparseHistorySaver(2, 8, 64)
>>> saver.append(history0)
>>> saver.fills7unlimit_()
>>> saver.validate()
>>> saver
SparseHistorySaver(2, 8, 64, '!', ([Reproduceable5seq(range(0, 160), 0), Reproduceable5seq(range(0, 160), 16), Reproduceable5seq(range(0, 160), 32), Reproduceable5seq(range(0, 160), 48), Reproduceable5seq(range(0, 160), 63)], 64, 8, 16, 15))
>>> new_saver = saver.fmap_(lambda rp: Reproduceable5seq(rp.seq, 80+rp.xidx))
>>> new_saver.validate()
>>> new_saver
SparseHistorySaver(2, 8, 64, '!', ([Reproduceable5seq(range(0, 160), 80), Reproduceable5seq(range(0, 160), 96), Reproduceable5seq(range(0, 160), 112), Reproduceable5seq(range(0, 160), 128), Reproduceable5seq(range(0, 160), 143)], 64, 8, 16, 15))




>>> history0 = Reproduceable5seq(range(160), 0)
>>> saver = DenseHistorySaver(5)
>>> saver.append(history0)
>>> saver.fills7unlimit_()
>>> saver.validate()
>>> saver
DenseHistorySaver(5, '!', [Reproduceable5seq(range(0, 160), 0), Reproduceable5seq(range(0, 160), 1), Reproduceable5seq(range(0, 160), 2), Reproduceable5seq(range(0, 160), 3), Reproduceable5seq(range(0, 160), 4)])
>>> new_saver = saver.fmap_(lambda rp: Reproduceable5seq(rp.seq, 80+rp.xidx))
>>> new_saver.validate()
>>> new_saver
DenseHistorySaver(5, '!', [Reproduceable5seq(range(0, 160), 80), Reproduceable5seq(range(0, 160), 81), Reproduceable5seq(range(0, 160), 82), Reproduceable5seq(range(0, 160), 83), Reproduceable5seq(range(0, 160), 84)])




>>> seed.types.HistorySaver._debug = False




'#'; __doc__ = r'#'
>>> import seed.types.HistorySaver
>>> seed.types.HistorySaver._debug = True


@20260907
SparseHistorySaver7immutable
fmap_
>>> from seed.types.Reproduceable import Reproduceable5seq
>>> history0 = Reproduceable5seq(range(160), 0)
>>> saver0 = SparseHistorySaver7immutable(8, 64)
>>> saver0
SparseHistorySaver7immutable(8, 64)
>>> saver1 = saver0.oo_append(history0)
>>> saver1
SparseHistorySaver7immutable(8, 64, '!', (Reproduceable5seq(range(0, 160), 0), mk_rglnkls_(), 1, 1, 1, 0))
>>> saver = saver1.oo_fills7unlimit_()
>>> saver.validate()
>>> saver
SparseHistorySaver7immutable(8, 64, '!', (Reproduceable5seq(range(0, 160), 0), mk_rglnkls_([Reproduceable5seq(range(0, 160), 16), Reproduceable5seq(range(0, 160), 32), Reproduceable5seq(range(0, 160), 48), Reproduceable5seq(range(0, 160), 63)]), 5, 64, 16, 1))
>>> new_saver = saver.fmap_(lambda rp: Reproduceable5seq(rp.seq, 80+rp.xidx))
>>> new_saver.validate()
>>> new_saver
SparseHistorySaver7immutable(8, 64, '!', (Reproduceable5seq(range(0, 160), 80), mk_rglnkls_([Reproduceable5seq(range(0, 160), 96), Reproduceable5seq(range(0, 160), 112), Reproduceable5seq(range(0, 160), 128), Reproduceable5seq(range(0, 160), 143)]), 5, 64, 16, 1))

>>> new_saver.head
Reproduceable5seq(range(0, 160), 80)
>>> new_saver.last
Reproduceable5seq(range(0, 160), 143)

    #overrided abstract methods:
    __eq__
    __hash__
    ['__getnewargs__', '__getstate__', '__setstate__', '_apparent_idx5physical_idx4history_array_', '_oo_append6underfill_', '_physical_idx5apparent_idx6sparse4history_array_', '_view_or_gmk_cached_list4history_array_', 'fmap_', 'head', 'imay_max_size7apparent', 'last', 'oo_clear', 'size7apparent', 'size7physical']
>>> import pickle
>>> bs = pickle.dumps(saver)
>>> _saver = pickle.loads(bs)
>>> #_saver
>>> str(_saver.head) == str(saver.head)
True
>>> _saver.head == saver.head
True
>>> str(_saver) == str(saver)
True
>>> _saver == saver
True
>>> _saver in {saver}
True
>>> not _saver in {new_saver}
True

>>> saver.oo_clear()
SparseHistorySaver7immutable(8, 64)
>>> saver.size7physical
5
>>> saver.size7apparent
64
>>> saver.max_size7physical
8
>>> saver.imay_max_size7apparent
64
>>> saver.head
Reproduceable5seq(range(0, 160), 0)
>>> saver.last
Reproduceable5seq(range(0, 160), 63)
>>> saver._view_or_gmk_cached_list4history_array_() is saver._view_or_gmk_cached_list4history_array_()
True
>>> saver._view_or_gmk_cached_list4history_array_()
(Reproduceable5seq(range(0, 160), 0), Reproduceable5seq(range(0, 160), 16), Reproduceable5seq(range(0, 160), 32), Reproduceable5seq(range(0, 160), 48), Reproduceable5seq(range(0, 160), 63))
>>> saver1._view_or_gmk_cached_list4history_array_()
(Reproduceable5seq(range(0, 160), 0),)
>>> saver0._view_or_gmk_cached_list4history_array_()
()

IHistorySaver7immutable
    #default concrete methods:
    __ne__
    oo_append
    oo_fills_
    oo_fills7unlimit_
    ii_both_fills7unlimit_
    oo_clear_but_last_
>>> saver
SparseHistorySaver7immutable(8, 64, '!', (Reproduceable5seq(range(0, 160), 0), mk_rglnkls_([Reproduceable5seq(range(0, 160), 16), Reproduceable5seq(range(0, 160), 32), Reproduceable5seq(range(0, 160), 48), Reproduceable5seq(range(0, 160), 63)]), 5, 64, 16, 1))
>>> saver != saver
False
>>> saver != saver.oo_clear()
True
>>> saver7offset_eq63 = saver.oo_clear_but_last_()
>>> saver7offset_ge63_le64 = saver7offset_eq63.oo_append(next(iter_snds4reproduceable_(saver7offset_eq63.last)))
>>> saver7offset_eq63.oo_fills_(0) is saver7offset_eq63
True
>>> saver7offset_ge63_le64 == saver7offset_eq63.oo_fills_(1)
True
>>> saver7offset_ge63_le64
SparseHistorySaver7immutable(8, 64, '!', (Reproduceable5seq(range(0, 160), 63), mk_rglnkls_([Reproduceable5seq(range(0, 160), 64)]), 2, 2, 1, 0))
>>> saver7offset_ge63_le125 = saver7offset_eq63.oo_fills_(62)
>>> saver7offset_ge63_le126 = saver7offset_ge63_le125.oo_fills_(1)
>>> saver7offset_ge63_le126.oo_fills_(1)
Traceback (most recent call last):
    ...
seed.types.HistorySaver.FullError: SparseHistorySaver7immutable(8, 64, '!', (Reproduceable5seq(range(0, 160), 63), mk_rglnkls_([Reproduceable5seq(range(0, 160), 79), Reproduceable5seq(range(0, 160), 95), Reproduceable5seq(range(0, 160), 111), Reproduceable5seq(range(0, 160), 126)]), 5, 64, 16, 1))
>>> saver7offset_eq63.oo_fills_(64)
Traceback (most recent call last):
    ...
seed.types.HistorySaver.FullError: SparseHistorySaver7immutable(8, 64, '!', (Reproduceable5seq(range(0, 160), 63), mk_rglnkls_([Reproduceable5seq(range(0, 160), 79), Reproduceable5seq(range(0, 160), 95), Reproduceable5seq(range(0, 160), 111), Reproduceable5seq(range(0, 160), 126)]), 5, 64, 16, 1))
>>> saver7offset_eq63.oo_fills7unlimit_() == saver7offset_ge63_le126
True
>>> saver7offset_eq64 = saver7offset_ge63_le64.oo_clear_but_last_()
>>> saver7offset_eq64
SparseHistorySaver7immutable(8, 64, '!', (Reproduceable5seq(range(0, 160), 64), mk_rglnkls_(), 1, 1, 1, 0))
>>> saver7offset_ge64_le126 = saver7offset_eq64.oo_fills_(62)
>>> not saver7offset_ge63_le126.head == saver7offset_ge64_le126.head
True
>>> saver7offset_ge63_le126.last == saver7offset_ge64_le126.last  # "=="
True
>>> not saver7offset_ge63_le64.head == saver7offset_eq64.head
True
>>> saver7offset_ge63_le64.last is saver7offset_eq64.last  # "is"
True
>>> saver7offset_ge63_le64.ii_both_fills7unlimit_(saver7offset_eq64) == (saver7offset_ge63_le126, saver7offset_ge64_le126)
True
>>> saver7offset_eq64.ii_both_fills7unlimit_(saver7offset_ge63_le64) == (saver7offset_ge64_le126, saver7offset_ge63_le126)
True



IHistorySaverBase
    #default concrete methods:
    __len__
    full
    search7sparse_
    search7dense_
    backward_search_key_points_


>>> from seed.math.sign_of import sign_of
>>> def jZhistory2rank_(j, /):
...     def history2rank_(history, /):
...         return sign_of(history.xidx - j)
...     return history2rank_
>>> saver
SparseHistorySaver7immutable(8, 64, '!', (Reproduceable5seq(range(0, 160), 0), mk_rglnkls_([Reproduceable5seq(range(0, 160), 16), Reproduceable5seq(range(0, 160), 32), Reproduceable5seq(range(0, 160), 48), Reproduceable5seq(range(0, 160), 63)]), 5, 64, 16, 1))
>>> saver7offset_eq63
SparseHistorySaver7immutable(8, 64, '!', (Reproduceable5seq(range(0, 160), 63), mk_rglnkls_(), 1, 1, 1, 0))
>>> len(saver)
64
>>> saver.full
True
>>> saver7offset_eq63.full
False


def search7sparse_(sf, history2rank_, /, *, offset=0, may_offsetted_rbegin6sparse=None):
>>> saver.search7sparse_(jZhistory2rank_(32-1))
(2, (16, Reproduceable5seq(range(0, 160), 16), -1), (32, Reproduceable5seq(range(0, 160), 32), 1))
>>> saver.search7sparse_(jZhistory2rank_(32+0))
(0, (16, Reproduceable5seq(range(0, 160), 16), -1), (32, Reproduceable5seq(range(0, 160), 32), 0))
>>> saver.search7sparse_(jZhistory2rank_(32+1))
(2, (32, Reproduceable5seq(range(0, 160), 32), -1), (48, Reproduceable5seq(range(0, 160), 48), 1))

>>> saver.search7sparse_(jZhistory2rank_(0-1))
(3, None, (0, Reproduceable5seq(range(0, 160), 0), 1))
>>> saver.search7sparse_(jZhistory2rank_(0+0))
(1, None, (0, Reproduceable5seq(range(0, 160), 0), 0))
>>> saver.search7sparse_(jZhistory2rank_(0+1))
(2, (0, Reproduceable5seq(range(0, 160), 0), -1), (16, Reproduceable5seq(range(0, 160), 16), 1))

>>> saver.search7sparse_(jZhistory2rank_(63-1))
(2, (48, Reproduceable5seq(range(0, 160), 48), -1), (63, Reproduceable5seq(range(0, 160), 63), 1))
>>> saver.search7sparse_(jZhistory2rank_(63+0))
(0, (48, Reproduceable5seq(range(0, 160), 48), -1), (63, Reproduceable5seq(range(0, 160), 63), 0))
>>> saver.search7sparse_(jZhistory2rank_(63+1))
(4, (63, Reproduceable5seq(range(0, 160), 63), -1), None)



>>> saver.search7sparse_(jZhistory2rank_(32+0), offset=1000)
(0, (1016, Reproduceable5seq(range(0, 160), 16), -1), (1032, Reproduceable5seq(range(0, 160), 32), 0))
>>> saver.search7sparse_(jZhistory2rank_(32+0), may_offsetted_rbegin6sparse=32)
(0, (16, Reproduceable5seq(range(0, 160), 16), -1), (32, Reproduceable5seq(range(0, 160), 32), 0))
>>> saver.search7sparse_(jZhistory2rank_(32+0), may_offsetted_rbegin6sparse=32-1)
Traceback (most recent call last):
    ...
seed.math.floor_ceil_tools.fc_perfect.NotPerfectError__div
>>> saver.search7sparse_(jZhistory2rank_(32+0), may_offsetted_rbegin6sparse=16)
(4, (16, Reproduceable5seq(range(0, 160), 16), -1), None)



def search7dense_(sf, history2rank_, /, *, offset=0, may_offsetted_rbegin6sparse=None, zero6sparse_ok=False, recursive=True, validate6recursive=False, may_extra_output6recursive_=None, _max_size7dense_6SparseHistorySaver=2049, _max_size7physical_6SparseHistorySaver=65537):
>>> saver.search7dense_(jZhistory2rank_(32-0))
(0, (31, Reproduceable5seq(range(0, 160), 31), -1), (32, Reproduceable5seq(range(0, 160), 32), 0))
>>> saver.search7dense_(jZhistory2rank_(32-6))
(0, (25, Reproduceable5seq(range(0, 160), 25), -1), (26, Reproduceable5seq(range(0, 160), 26), 0))
>>> saver.search7dense_(jZhistory2rank_(32-6), offset=1000)
(0, (1025, Reproduceable5seq(range(0, 160), 25), -1), (1026, Reproduceable5seq(range(0, 160), 26), 0))
>>> saver.search7dense_(jZhistory2rank_(32-6), may_offsetted_rbegin6sparse=32)
(0, (25, Reproduceable5seq(range(0, 160), 25), -1), (26, Reproduceable5seq(range(0, 160), 26), 0))
>>> saver.search7dense_(jZhistory2rank_(32-6), may_offsetted_rbegin6sparse=16)
(4, (16, Reproduceable5seq(range(0, 160), 16), -1), None)
>>> saver.search7dense_(jZhistory2rank_(32-6), zero6sparse_ok=True)
(0, (25, Reproduceable5seq(range(0, 160), 25), -1), (26, Reproduceable5seq(range(0, 160), 26), 0))




# @20260908:++kw:may_offsetted_begin6sparse
# @20260908:++kw:left_vs_right7transition
def search7sparse_
>>> saver.search7sparse_(jZhistory2rank_(32-1), left_vs_right7transition=True)
(-3, (16, Reproduceable5seq(range(0, 160), 16), -1), (32, Reproduceable5seq(range(0, 160), 32), 1))
>>> saver.search7sparse_(jZhistory2rank_(32+0), left_vs_right7transition=True)
(-1, (32, Reproduceable5seq(range(0, 160), 32), 0), (48, Reproduceable5seq(range(0, 160), 48), 1))
>>> saver.search7sparse_(jZhistory2rank_(32+1), left_vs_right7transition=True)
(-3, (32, Reproduceable5seq(range(0, 160), 32), -1), (48, Reproduceable5seq(range(0, 160), 48), 1))

>>> saver.search7sparse_(jZhistory2rank_(0-1), left_vs_right7transition=True)
(-5, None, (0, Reproduceable5seq(range(0, 160), 0), 1))
>>> saver.search7sparse_(jZhistory2rank_(0+0), left_vs_right7transition=True)
(-1, (0, Reproduceable5seq(range(0, 160), 0), 0), (16, Reproduceable5seq(range(0, 160), 16), 1))
>>> saver.search7sparse_(jZhistory2rank_(0+1), left_vs_right7transition=True)
(-3, (0, Reproduceable5seq(range(0, 160), 0), -1), (16, Reproduceable5seq(range(0, 160), 16), 1))

>>> saver.search7sparse_(jZhistory2rank_(63-1), left_vs_right7transition=True)
(-3, (48, Reproduceable5seq(range(0, 160), 48), -1), (63, Reproduceable5seq(range(0, 160), 63), 1))
>>> saver.search7sparse_(jZhistory2rank_(63+0), left_vs_right7transition=True)
(-2, (63, Reproduceable5seq(range(0, 160), 63), 0), None)
>>> saver.search7sparse_(jZhistory2rank_(63+1), left_vs_right7transition=True)
(-4, (63, Reproduceable5seq(range(0, 160), 63), -1), None)



>>> saver.search7sparse_(jZhistory2rank_(32+0), offset=1000, left_vs_right7transition=True)
(-1, (1032, Reproduceable5seq(range(0, 160), 32), 0), (1048, Reproduceable5seq(range(0, 160), 48), 1))
>>> saver.search7sparse_(jZhistory2rank_(32+0), may_offsetted_rbegin6sparse=32, left_vs_right7transition=True)
(-2, (32, Reproduceable5seq(range(0, 160), 32), 0), None)
>>> saver.search7sparse_(jZhistory2rank_(32+0), may_offsetted_rbegin6sparse=16, left_vs_right7transition=True)
(-4, (16, Reproduceable5seq(range(0, 160), 16), -1), None)

>>> saver.search7sparse_(jZhistory2rank_(32+0), may_offsetted_begin6sparse=16, left_vs_right7transition=True)
(-1, (32, Reproduceable5seq(range(0, 160), 32), 0), (48, Reproduceable5seq(range(0, 160), 48), 1))
>>> saver.search7sparse_(jZhistory2rank_(32+0), may_offsetted_begin6sparse=32, left_vs_right7transition=True)
(-1, (32, Reproduceable5seq(range(0, 160), 32), 0), (48, Reproduceable5seq(range(0, 160), 48), 1))
>>> saver.search7sparse_(jZhistory2rank_(32+0), may_offsetted_begin6sparse=48, left_vs_right7transition=True)
(-5, None, (48, Reproduceable5seq(range(0, 160), 48), 1))


>>> saver.search7sparse_(jZhistory2rank_(32+0), may_offsetted_begin6sparse=48)
(3, None, (48, Reproduceable5seq(range(0, 160), 48), 1))
>>> saver.search7sparse_(jZhistory2rank_(32+0), may_offsetted_begin6sparse=32)
(1, None, (32, Reproduceable5seq(range(0, 160), 32), 0))
>>> saver.search7sparse_(jZhistory2rank_(32+0), may_offsetted_begin6sparse=16)
(0, (16, Reproduceable5seq(range(0, 160), 16), -1), (32, Reproduceable5seq(range(0, 160), 32), 0))



# @20260908:++kw:may_offsetted_begin6sparse
# @20260908:++kw:left_vs_right7transition
def search7dense_
>>> saver.search7dense_(jZhistory2rank_(32-0), left_vs_right7transition=True)
(-1, (32, Reproduceable5seq(range(0, 160), 32), 0), (33, Reproduceable5seq(range(0, 160), 33), 1))
>>> saver.search7dense_(jZhistory2rank_(32-6), left_vs_right7transition=True)
(-1, (26, Reproduceable5seq(range(0, 160), 26), 0), (27, Reproduceable5seq(range(0, 160), 27), 1))
>>> saver.search7dense_(jZhistory2rank_(32-6), offset=1000, left_vs_right7transition=True)
(-1, (1026, Reproduceable5seq(range(0, 160), 26), 0), (1027, Reproduceable5seq(range(0, 160), 27), 1))
>>> saver.search7dense_(jZhistory2rank_(32-6), may_offsetted_rbegin6sparse=32, left_vs_right7transition=True)
(-1, (26, Reproduceable5seq(range(0, 160), 26), 0), (27, Reproduceable5seq(range(0, 160), 27), 1))
>>> saver.search7dense_(jZhistory2rank_(32-6), may_offsetted_rbegin6sparse=16, left_vs_right7transition=True)
(-4, (16, Reproduceable5seq(range(0, 160), 16), -1), None)

>>> saver.search7dense_(jZhistory2rank_(32-6), zero6sparse_ok=True, left_vs_right7transition=True)
(-3, (16, Reproduceable5seq(range(0, 160), 16), -1), (32, Reproduceable5seq(range(0, 160), 32), 1))

>>> saver.search7dense_(jZhistory2rank_(32-6), may_offsetted_begin6sparse=32)
(3, None, (32, Reproduceable5seq(range(0, 160), 32), 1))
>>> saver.search7dense_(jZhistory2rank_(32-6), may_offsetted_begin6sparse=16)
(0, (25, Reproduceable5seq(range(0, 160), 25), -1), (26, Reproduceable5seq(range(0, 160), 26), 0))












def backward_search_key_points_(sf, stZhistory2rank_, op4fold_, st7fold, /, *, offset=0, _max_size7dense_6SparseHistorySaver=2049, _max_size7physical_6SparseHistorySaver=65537):
    [op4fold_ :: [[history2rank_{k}(history{-1+j}) == -1][history2rank_{k}(history{j}) >= 0]] => prev_history6key_point/history{-1+j} -> j/uint%(offset+size7apparent) -> history6key_point/history{j} -> st7fold{k} -> st7fold{1+k}{[history2rank_{1+k}(history{-1+j}) >= 0]}]
>>> #ls4IIps = [1,2,6,30,210,2310]
>>> #history0 = Reproduceable5seq([u for IIps in ls4IIps for u in [IIps]*9], 0)
>>> ps = [2,3,5,7,11,13]
>>> ps = [p for p in ps for p in [p]*9]
>>> ps
[2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7, 7, 7, 7, 7, 7, 7, 7, 7, 11, 11, 11, 11, 11, 11, 11, 11, 11, 13, 13, 13, 13, 13, 13, 13, 13, 13]
>>> history0 = Reproduceable5seq(ps, 0)
>>> _saver0 = SparseHistorySaver7immutable(8, 64)
>>> _saver1 = _saver0.oo_append(history0)
>>> _saver = _saver1.oo_fills7unlimit_()
>>> #_saver

>>> def history2tmay_prev_u_(history, /):
...     us = history.seq
...     end = history.xidx
...     tmay_u = us[-1+end:end]
...     return tmay_u
>>> def history2prev_us_(history, /):
...     us = history.seq
...     end = history.xidx
...     us = set(us[:end])
...     return us
>>> def stZhistory2rank_(st7fold, /):
...     (js, us7tgt) = st7fold
...     def history2rank_(history, /):
...         prev_us = history2prev_us_(history)
...         tmay_prev_u = history2tmay_prev_u_(history)
...         return -1 if not (us7tgt <= prev_us) else (0 if tmay_prev_u and {*tmay_prev_u} <= us7tgt else +1)
...     return history2rank_
>>> def op4fold_(prev_offset4key_point, offset4key_point, history6key_point, st7fold, /):
...     (js, us7tgt) = st7fold
...     tmay_prev_u = history2tmay_prev_u_(history6key_point)
...     js = (offset4key_point, *js)
...     #xxx:us7tgt -= {*tmay_prev_u}
...     us7tgt = us7tgt -{*tmay_prev_u}
...     return (js, us7tgt)
>>> result = _saver.backward_search_key_points_(stZhistory2rank_, op4fold_ , st7fold:=([],{2,7}), offset=0)
>>> result #doctest: +ELLIPSIS
(((1, 28), set()), [((27, Reproduceable5seq(..., 27), -1), (28, Reproduceable5seq(..., 28), 0)), ((0, Reproduceable5seq(..., 0), -1), (1, Reproduceable5seq(..., 1), 0))])
>>> (ps[-1+1], ps[-1+28])
(2, 7)
>>> [*enumerate(ps, 1)]
[(1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2), (10, 3), (11, 3), (12, 3), (13, 3), (14, 3), (15, 3), (16, 3), (17, 3), (18, 3), (19, 5), (20, 5), (21, 5), (22, 5), (23, 5), (24, 5), (25, 5), (26, 5), (27, 5), (28, 7), (29, 7), (30, 7), (31, 7), (32, 7), (33, 7), (34, 7), (35, 7), (36, 7), (37, 11), (38, 11), (39, 11), (40, 11), (41, 11), (42, 11), (43, 11), (44, 11), (45, 11), (46, 13), (47, 13), (48, 13), (49, 13), (50, 13), (51, 13), (52, 13), (53, 13), (54, 13)]
>>> _saver.backward_search_key_points_(stZhistory2rank_, op4fold_ , st7fold:=([],{2,7,-1}), offset=0) #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
ValueError: ('not satisfied precondition:[-1 =!= history2rank_{k:=0}(sf.last)]', SparseHistorySaver7immutable(...), ([], {2, -1, 7}), -1)
>>> _saver.backward_search_key_points_(stZhistory2rank_, op4fold_ , st7fold:=([],{*[]}), offset=0)
(([], set()), [])





@20260908:++forward_search_key_points_()
DONE:test:forward_search_key_points_(),backward_search_key_points_()
using:
    _max_size7dense_6SparseHistorySaver
    _max_size7physical_6SparseHistorySaver
    __setstate__???
    validate
    class DupRange:instead of Reproduceable5seq
        [1]*k,[2]*k,...
        --> u/%d
    ts = [a<b<c]
        backward_search:
            sign_of(u -ts[-1])
        forward_search
            sign_of(u-minmax(ts))

>>> history0 = Reproduceable5seq(range(3000), 0)
>>> _saver0 = SparseHistorySaver7immutable(3, -1)
>>> _saver1 = _saver0.oo_append(history0)
>>> _saver = _saver1.oo_fills7unlimit_()
>>> #_saver
>>> kwds = dict(_max_size7dense_6SparseHistorySaver=3, _max_size7physical_6SparseHistorySaver=3)


>>> def history2u_(history, /):
...     u = history.xidx
...     return u//10
>>> def mk__stZhistory2rank_(bwd_vs_fwd):
...   def stZhistory2rank_(st7fold, /):
...     (js, us7tgt, default) = st7fold
...     min_u7tgt = min(us7tgt, default=default)
...     max_u7tgt = max(us7tgt, default=default)
...     def history2rank7bwd_(history, /):
...         u = history2u_(history)
...         return (-1 if (u < max_u7tgt) else (+1 if (u > max_u7tgt) else 0))
...     def history2rank7fwd_(history, /):
...         u = history2u_(history)
...         return (-1 if (u < min_u7tgt) else (+1 if (u > max_u7tgt) else 0))
...     history2rank_ = history2rank7bwd_ if not bwd_vs_fwd else history2rank7fwd_
...     return history2rank_
...   return stZhistory2rank_
>>> stZhistory2rank7bwd_ = mk__stZhistory2rank_(bwd_vs_fwd=False)
>>> stZhistory2rank7fwd_ = mk__stZhistory2rank_(bwd_vs_fwd=True)
>>> def op4fold_(prev_offset4key_point, offset4key_point, history6key_point, st7fold, /):
...     (js, us7tgt, default) = st7fold
...     u = history2u_(history6key_point)
...     js = (*js, offset4key_point)
...     assert u in us7tgt, (u, us7tgt)
...     #xxx:us7tgt -= {u}
...     us7tgt = us7tgt -{u}
...     return (js, us7tgt, default)


>>> result = _saver.backward_search_key_points_(stZhistory2rank7bwd_, op4fold_ , st7fold:=([],{2,7,99},-9999999), offset=0, **kwds)
>>> result #doctest: +ELLIPSIS
(((990, 70, 20), set(), -9999999), [((989, Reproduceable5seq(range(0, 3000), 989), -1), (990, Reproduceable5seq(range(0, 3000), 990), 0)), ((69, Reproduceable5seq(range(0, 3000), 69), -1), (70, Reproduceable5seq(range(0, 3000), 70), 0)), ((19, Reproduceable5seq(range(0, 3000), 19), -1), (20, Reproduceable5seq(range(0, 3000), 20), 0))])
>>> #kw:_ok__noneZzero_as_left_transition:goto
>>> _saver.backward_search_key_points_(stZhistory2rank7bwd_, op4fold_ , st7fold:=([],{2,7,-1},-9999999), offset=0, **kwds) #doctest: +ELLIPSIS
(((70, 20), {-1}, -9999999), [((69, Reproduceable5seq(range(0, 3000), 69), -1), (70, Reproduceable5seq(range(0, 3000), 70), 0)), ((19, Reproduceable5seq(range(0, 3000), 19), -1), (20, Reproduceable5seq(range(0, 3000), 20), 0))])
>>> _saver.backward_search_key_points_(stZhistory2rank7bwd_, op4fold_ , st7fold:=([],{*[]},-9999999), offset=0, **kwds)
(([], set(), -9999999), [])


#-9999999 --> +9999999
>>> result = _saver.forward_search_key_points_(stZhistory2rank7fwd_, op4fold_ , st7fold:=([],{2,7,99},+9999999), offset=0, **kwds)
>>> result #doctest: +ELLIPSIS
(((20, 70, 990), set(), 9999999), [((19, Reproduceable5seq(range(0, 3000), 19), -1), (20, Reproduceable5seq(range(0, 3000), 20), 0)), ((69, Reproduceable5seq(range(0, 3000), 69), -1), (70, Reproduceable5seq(range(0, 3000), 70), 0)), ((989, Reproduceable5seq(range(0, 3000), 989), -1), (990, Reproduceable5seq(range(0, 3000), 990), 0))])
>>> _saver.forward_search_key_points_(stZhistory2rank7fwd_, op4fold_ , st7fold:=([],{2,7,-1},+9999999), offset=0) #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
ValueError: ('not satisfied precondition:[-1 == history2rank_{k:=0}(sf.head)]', SparseHistorySaver7immutable(...), Reproduceable5seq(range(0, 3000), 0), ([], {2, -1, 7}, 9999999), 0)
>>> _saver.forward_search_key_points_(stZhistory2rank7fwd_, op4fold_ , st7fold:=([],{2,7,1.5},+9999999), offset=0, **kwds) #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
Exception: ('op4fold7fwd_() not satisfied postcondition:[op4fold7fwd_ :: [[history2rank_{k}(history{-1+j}) == -1][history2rank_{k}(history{j}) >= 0]] => prev_history6key_point/history{-1+j} -> j/uint%(offset+size7apparent) -> history6key_point/history{j} -> st7fold{k} -> st7fold{1+k}{[history2rank_{1+k}(history{j}) == -1]}]', SparseHistorySaver7immutable(...), (0, (19, Reproduceable5seq(range(0, 3000), 19), -1), (20, Reproduceable5seq(range(0, 3000), 20), 0)), ((20,), {1.5, 7}, 9999999))
>>> _saver.forward_search_key_points_(stZhistory2rank7fwd_, op4fold_ , st7fold:=([],{2,7,303},+9999999), offset=0, **kwds) #doctest: +ELLIPSIS
(((20, 70), {303}, 9999999), [((19, Reproduceable5seq(range(0, 3000), 19), -1), (20, Reproduceable5seq(range(0, 3000), 20), 0)), ((69, Reproduceable5seq(range(0, 3000), 69), -1), (70, Reproduceable5seq(range(0, 3000), 70), 0))])
>>> _saver.forward_search_key_points_(stZhistory2rank7fwd_, op4fold_ , st7fold:=([],{*[]},+9999999), offset=0, **kwds)
(([], set(), 9999999), [])










>>> seed.types.HistorySaver._debug = False



'#'; __doc__ = r'#'
@20260909
DONE:test:kw:non_reproduceable_ok,may_iter_subsequents_
    [may_iter_subsequents_ :: may (item{i} -> Iter item[j]{j>i})]
    @fills_/fills7unlimit_/oo_fills_/both_fills7unlimit_/oo_fills7unlimit_/ii_both_fills7unlimit_/search7dense_/backward_search_key_points_/forward_search_key_points_

>>> from seed.math.sign_of import sign_of
>>> from itertools import count



===
SparseHistorySaver
>>> saver = SparseHistorySaver(5, 5, -1)
>>> saver.append(10000)
Traceback (most recent call last):
    ...
TypeError: <class 'int'>
>>> saver.append(10000, non_reproduceable_ok=True)
>>> saver
SparseHistorySaver(5, 5, -1, '!', ([10000], 1, 5, 1, 1))
>>> saver.fills_(10, may_iter_subsequents_=lambda u,/:count(1+u))
>>> saver
SparseHistorySaver(5, 5, -1, '!', ([10000, 10004, 10008, 10010], 11, 5, 4, 2))
>>> saver.fills7unlimit_(may_iter_subsequents_=lambda u,/:iter(range(1+u, 11+u)))
>>> saver
SparseHistorySaver(5, 5, -1, '!', ([10000, 10008, 10016, 10020], 21, 5, 8, 4))
>>> _saver = SparseHistorySaver(5, 5, -1)
>>> _saver.append(saver.last, non_reproduceable_ok=True)
>>> saver.both_fills7unlimit_(_saver, may_iter_subsequents_=lambda u,/:iter(range(1+u, 11+u)))
>>> saver
SparseHistorySaver(5, 5, -1, '!', ([10000, 10008, 10016, 10024, 10030], 31, 5, 8, 6))
>>> _saver
SparseHistorySaver(5, 5, -1, '!', ([10020, 10024, 10028, 10030], 11, 5, 4, 2))
>>> _saver.clear_but_last_() #using append
>>> _saver
SparseHistorySaver(5, 5, -1, '!', ([10030], 1, 5, 1, 1))
>>> saver.fmap_(lambda u:100*u)
SparseHistorySaver(5, 5, -1, '!', ([1000000, 1000800, 1001600, 1002400, 1003000], 31, 5, 8, 6))



===
SparseHistorySaver7immutable
>>> saver = SparseHistorySaver7immutable(5, -1)
>>> saver.oo_append(10000)
Traceback (most recent call last):
    ...
TypeError: <class 'int'>
>>> saver = saver.oo_append(10000, non_reproduceable_ok=True)
>>> saver
SparseHistorySaver7immutable(5, -1, '!', (10000, mk_rglnkls_(), 1, 1, 1, 0))
>>> saver = saver.oo_fills_(10, may_iter_subsequents_=lambda u,/:count(1+u))
>>> saver
SparseHistorySaver7immutable(5, -1, '!', (10000, mk_rglnkls_([10004, 10008, 10010]), 4, 11, 4, 2))
>>> saver = saver.oo_fills7unlimit_(may_iter_subsequents_=lambda u,/:iter(range(1+u, 11+u)))
>>> saver
SparseHistorySaver7immutable(5, -1, '!', (10000, mk_rglnkls_([10008, 10016, 10020]), 4, 21, 8, 4))
>>> _saver = SparseHistorySaver7immutable(5, -1)
>>> _saver = _saver.oo_append(saver.last, non_reproduceable_ok=True)
>>> (saver, _saver) = saver.ii_both_fills7unlimit_(_saver, may_iter_subsequents_=lambda u,/:iter(range(1+u, 11+u)))
>>> saver
SparseHistorySaver7immutable(5, -1, '!', (10000, mk_rglnkls_([10008, 10016, 10024, 10030]), 5, 31, 8, 2))
>>> _saver
SparseHistorySaver7immutable(5, -1, '!', (10020, mk_rglnkls_([10024, 10028, 10030]), 4, 11, 4, 2))
>>> _saver.oo_clear_but_last_() #using oo_append
SparseHistorySaver7immutable(5, -1, '!', (10030, mk_rglnkls_(), 1, 1, 1, 0))
>>> saver.fmap_(lambda u:100*u)
SparseHistorySaver7immutable(5, -1, '!', (1000000, mk_rglnkls_([1000800, 1001600, 1002400, 1003000]), 5, 31, 8, 2))



>>> kwds = dict(may_iter_subsequents_=lambda u,/:count(1+u), _max_size7dense_6SparseHistorySaver=3, _max_size7physical_6SparseHistorySaver=3)
>>> def jZhistory2rank_(j, /):
...     def history2rank_(history, /):
...         return sign_of(history - j)
...     return history2rank_
>>> saver.search7dense_(jZhistory2rank_(10018), **kwds)
(0, (17, 10017, -1), (18, 10018, 0))




>>> def history2u_(history, /):
...     u = history
...     return u//10
>>> def mk__stZhistory2rank_(bwd_vs_fwd):
...   def stZhistory2rank_(st7fold, /):
...     (js, us7tgt, default) = st7fold
...     min_u7tgt = min(us7tgt, default=default)
...     max_u7tgt = max(us7tgt, default=default)
...     def history2rank7bwd_(history, /):
...         u = history2u_(history)
...         return (-1 if (u < max_u7tgt) else (+1 if (u > max_u7tgt) else 0))
...     def history2rank7fwd_(history, /):
...         u = history2u_(history)
...         return (-1 if (u < min_u7tgt) else (+1 if (u > max_u7tgt) else 0))
...     history2rank_ = history2rank7bwd_ if not bwd_vs_fwd else history2rank7fwd_
...     return history2rank_
...   return stZhistory2rank_
>>> stZhistory2rank7bwd_ = mk__stZhistory2rank_(bwd_vs_fwd=False)
>>> stZhistory2rank7fwd_ = mk__stZhistory2rank_(bwd_vs_fwd=True)
>>> def op4fold_(prev_offset4key_point, offset4key_point, history6key_point, st7fold, /):
...     (js, us7tgt, default) = st7fold
...     u = history2u_(history6key_point)
...     js = (*js, offset4key_point)
...     assert u in us7tgt, (u, us7tgt)
...     #xxx:us7tgt -= {u}
...     us7tgt = us7tgt -{u}
...     return (js, us7tgt, default)


>>> result = saver.backward_search_key_points_(stZhistory2rank7bwd_, op4fold_ , st7fold:=([],{1000,1001,1002},-9999999), offset=0, **kwds)
>>> result #doctest: +ELLIPSIS
(((20, 10), {1000}, -9999999), [((19, 10019, -1), (20, 10020, 0)), ((9, 10009, -1), (10, 10010, 0))])

#-9999999 --> +9999999
>>> result = saver.forward_search_key_points_(stZhistory2rank7fwd_, op4fold_ , st7fold:=([],{1001,1002,1003},+9999999), offset=0, **kwds)
>>> result #doctest: +ELLIPSIS
(((10, 20, 30), set(), 9999999), [((9, 10009, -1), (10, 10010, 0)), ((19, 10019, -1), (20, 10020, 0)), ((29, 10029, -1), (30, 10030, 0))])




'#'; __doc__ = r'#'
@20260910
++copy/mk_empty_/mk_solo_
++extend/oo_extend

===
DenseHistorySaver
>>> saver = DenseHistorySaver(5, '!', [1, 2, 3])
>>> _saver = saver.copy()
>>> len(saver) == 3 == len(_saver)
True
>>> _saver.append(4, non_reproduceable_ok=True)
>>> len(saver) == 3 < 4 == len(_saver)
True
>>> saver
DenseHistorySaver(5, '!', [1, 2, 3])
>>> _saver
DenseHistorySaver(5, '!', [1, 2, 3, 4])
>>> _saver = saver.mk_empty_()
>>> len(saver) == 3 > 0 == len(_saver)
True
>>> _saver
DenseHistorySaver(5)
>>> _saver = saver.mk_solo_(-1, non_reproduceable_ok=True)
>>> len(saver) == 3 > 1 == len(_saver)
True
>>> _saver.last == -1
True
>>> _saver
DenseHistorySaver(5, '!', [-1])
>>> saver
DenseHistorySaver(5, '!', [1, 2, 3])



===
SparseHistorySaver
>>> #bug:saver = SparseHistorySaver(5, 9, -1, '!', [1, 2, 3])
>>> SparseHistorySaver(5, 9, -1, '!', ([1, 2, 3], 3, 5, 1, 1))
SparseHistorySaver(5, 9, -1, '!', ([1, 2, 3], 3, 5, 1, 1))
>>> saver = SparseHistorySaver(5, 9, -1)
>>> saver.extend([1, 2, 3], non_reproduceable_ok=True)
>>> _saver = saver.copy()
>>> len(saver) == 3 == len(_saver)
True
>>> _saver.append(4, non_reproduceable_ok=True)
>>> len(saver) == 3 < 4 == len(_saver)
True
>>> saver
SparseHistorySaver(5, 9, -1, '!', ([1, 2, 3], 3, 5, 1, 1))
>>> _saver
SparseHistorySaver(5, 9, -1, '!', ([1, 2, 3, 4], 4, 5, 1, 1))
>>> _saver = saver.mk_empty_()
>>> len(saver) == 3 > 0 == len(_saver)
True
>>> _saver
SparseHistorySaver(5, 9, -1)
>>> _saver = saver.mk_solo_(-1, non_reproduceable_ok=True)
>>> len(saver) == 3 > 1 == len(_saver)
True
>>> _saver.last == -1
True
>>> _saver
SparseHistorySaver(5, 9, -1, '!', ([-1], 1, 5, 1, 1))
>>> saver
SparseHistorySaver(5, 9, -1, '!', ([1, 2, 3], 3, 5, 1, 1))




===
SparseHistorySaver7immutable
>>> #bug:saver = SparseHistorySaver7immutable((5, -1), '!', [1, 2, 3])
>>> SparseHistorySaver7immutable(5, -1, '!', (1, mk_rglnkls_([2, 3]), 3, 3, 1, 0))
SparseHistorySaver7immutable(5, -1, '!', (1, mk_rglnkls_([2, 3]), 3, 3, 1, 0))
>>> saver = SparseHistorySaver7immutable(5, -1).oo_extend([1, 2, 3], non_reproduceable_ok=True)
>>> _saver = saver.copy()
>>> _saver is saver
True
>>> len(saver) == 3 == len(_saver)
True
>>> _saver = _saver.oo_append(4, non_reproduceable_ok=True)
>>> len(saver) == 3 < 4 == len(_saver)
True
>>> saver
SparseHistorySaver7immutable(5, -1, '!', (1, mk_rglnkls_([2, 3]), 3, 3, 1, 0))
>>> _saver
SparseHistorySaver7immutable(5, -1, '!', (1, mk_rglnkls_([2, 3, 4]), 4, 4, 1, 0))
>>> _saver = saver.mk_empty_()
>>> len(saver) == 3 > 0 == len(_saver)
True
>>> _saver
SparseHistorySaver7immutable(5, -1)
>>> _saver = saver.mk_solo_(-1, non_reproduceable_ok=True)
>>> len(saver) == 3 > 1 == len(_saver)
True
>>> _saver.last == -1
True
>>> _saver
SparseHistorySaver7immutable(5, -1, '!', (-1, mk_rglnkls_(), 1, 1, 1, 0))
>>> saver
SparseHistorySaver7immutable(5, -1, '!', (1, mk_rglnkls_([2, 3]), 3, 3, 1, 0))





'#'; __doc__ = r'#'














py_adhoc_call   seed.types.HistorySaver   @f
]]]'''#'''
__all__ = r'''
mk_history_saver_
IHistorySaver
    EmptyError
    FullError
    IHistorySaver__bisect7single_array_view
        DenseHistorySaver
        SparseHistorySaver



IHistorySaverBase
    IHistorySaverBase__bisect7single_array__7view_or_gmk_cached_list
        IHistorySaverBase__bisect7single_array_view

    IHistorySaver7immutable
        IHistorySaver7immutable__bisect7single_array__7view_or_gmk_cached_list
            SparseHistorySaver7immutable
    IHistorySaver7mutable   IHistorySaver
        IHistorySaver7mutable__bisect7single_array_view     IHistorySaver__bisect7single_array_view
            DenseHistorySaver
            SparseHistorySaver



cached_version5history2rank_
wrap4history2rank_
wrap4result4search8transition_
    check_case6result4search8transition_
        check_case6result4search8transition7L_
        check_case6result4search8transition7R_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.check import check_type_is, check_type_le, check_int_ge, check_int_ge_lt, check_int_ge_le, check_uint_lt, check_callable, check_non_ABC
    from seed.tiny_.check import check_danger_mark_
    from bisect import bisect_right
    from functools import cache
    from itertools import islice
    from seed.types.Reproduceable import IReproduceable
    from seed.types.Reproduceable import iter_snds4reproduceable_
    from seed.helper.ifNone import ifNone, ifNonef
    from seed.helper.repr_input import repr_helper, repr_helper_ex
    from seed.math.floor_ceil_tools.fc_perfect import perfect_div

    # IHistorySaver7immutable
    from seed.types.SinglyLinkedList import mk_rglnkls_
    from seed.types.SinglyLinkedList import top6_, oo_pop_, oo_push_, mk5iter7up_, list7up_, len7count_, fmap7force_
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

__all__
#_debug = True
_debug = False

class FullError(Exception):pass
class EmptyError(Exception):pass
class IHistorySaverBase(ABC):
    #common_part == immutable_part&&mutable_part
    r'''[[[
    default:[history :: IReproduceable{record}]
        history -->?? snapshot|footprint
    ...
    when not [history :: IReproduceable{record}]i
        fmap_ # convert to IReproduceable
        or:
        @20260909:++kw:non_reproduceable_ok,may_iter_subsequents_
            [may_iter_subsequents_ :: may (item{i} -> Iter item[j]{j>i})]
            @fills_/fills7unlimit_/oo_fills_/both_fills7unlimit_/oo_fills7unlimit_/ii_both_fills7unlimit_/search7dense_/backward_search_key_points_/forward_search_key_points_


    [[sf.size7apparent > 0] => [sf.append(history) or sf.oo_append(history) : expected:[history == xnext4reproduceable_(sf.last).oresult]]]

    [left_vs_right7transition :: bool]
        # left_transition: rank:(-1-->0)
        # right_transition: rank:(0-->+1)
    # search:always target:left_transition
    [stZhistory2rank_ :: st7fold{k} -> history2rank_{k}]
        # stZhistory2rank7bwd_
        # stZhistory2rank7fwd_
    [history2rank_{k} :: history -> (-1|0|+1)]
    [backward_search => [history2rank_{k}(history{j}) <= history2rank_{1+k}(history{j})]]
    [forward_search => [history2rank_{k}(history{j}) >= history2rank_{1+k}(history{j})]]
        # history2rank7bwd_
        # history2rank7fwd_

    [op4fold_{(backward_search|forward_search)} :: [[history2rank_{k}(history{-1+j}) == -1][history2rank_{k}(history{j}) >= 0]] => prev_history6key_point/history{-1+j} -> j/uint%(offset+size7apparent) -> history6key_point/history{j} -> st7fold{k} -> st7fold{1+k}{backward_search => [history2rank_{1+k}(history{-1+j}) >= 0]}{forward_search => [history2rank_{1+k}(history{j}) == -1]}]
        # op4fold7bwd_
        # op4fold7fwd_


    [may_offsetted_rbegin == (None|offsetted_rbegin)]
    [offsetted_rbegin{k} :: uint{>=offset}{<offset+len(sf)}]
    [backward_search => [[history2rank_{-1+k}(history{offsetted_rbegin{k}}) == -1][history2rank_{k}(history{offsetted_rbegin{k}}) >= 0]]]

    [may_offsetted_begin == (None|offsetted_begin)]
    [offsetted_begin{k} :: uint{>=offset}{<offset+len(sf)}]
    [forward_search => [[history2rank_{-1+k}(history{offsetted_begin{k}}) >= 0][history2rank_{k}(history{offsetted_begin{k}}) == -1]]]

    #rbegin: begin{backward_search}
    [rbegin6sparse :: apparent_idx{from physical_idx}]
    [offsetted_rbegin6sparse == offset+rbegin6sparse]
    [may_offsetted_rbegin6sparse == (None|offsetted_rbegin6sparse)]

    #begin: begin{forward_search}
    [begin6sparse :: apparent_idx{from physical_idx}]
    [offsetted_begin6sparse == offset+begin6sparse]
    [may_offsetted_begin6sparse == (None|offsetted_begin6sparse)]

    [may_extra_output6recursive_ :: may (((offset,IHistorySaver)) -> None)]

    #]]]'''#'''
    __slots__ = ()

    def __len__(sf, /):
        '-> size7apparent'
        return sf.size7apparent
    @property
    def full(sf, /):
        '-> bool'
        return sf.size7apparent == sf.imay_max_size7apparent


    @abstractmethod
    def copy(sf, /):
        raise NotImplementedError
        import copy#copy{shallow},deepcopy
        ot = copy.copy(sf) # history_array not copied...
        ot = copy.deepcopy(sf) # history_lnkls&&inner history/reproduceable be copied
        #slow version:deepcopy
        import pickle
        bs = pickle.dumps(sf)
        ot = pickle.loads(bs)
        return ot
    @abstractmethod
    def mk_empty_(sf, /):
        'sf/cls -> ot/cls # [0 == len(ot)]'
    @abstractmethod
    def mk_solo_(sf, head, /, *, non_reproduceable_ok=False):
        'sf/cls -> head/last/IReproduceable -> ot/cls # [1 == len(ot)][head is ot.head is ot.last]'

    @abstractmethod
    def __getnewargs__(sf, /):
        '-> args{@__new__}'
        #pickle
        #fmap_
    @abstractmethod
    def __getstate__(sf, /):
        '-> st4pickle'
        #pickle
        #fmap_
    @abstractmethod
    def __setstate__(sf, st4pickle, /):
        'st4pickle -> None'
        #pickle
        #fmap_
    @abstractmethod
    def fmap_(sf, transform4reproduceable, /):
        'self/IHistorySaver{historyI} -> (historyI -> historyO) -> other/IHistorySaver{historyO} # [historyI :: IReproduceable{recordI}][historyO :: IReproduceable{recordO}] # [[historyI be not IReproduceable] => [self.search7sparse_():ok][self.search7dense_():not ok][[historyO be IReproduceable] -> [other.search7dense_():ok]]]'
        #@20260905:++fmap_
        #   fmap to change internal st:eg: [0==M%N][HistorySaver{rp}%M --> HistorySaver{rp}%N][]
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
    @property
    @abstractmethod
    def head(sf, /):
        '-> history/IReproduceable{record} | ^EmptyError'
    @property
    @abstractmethod
    def last(sf, /):
        '-> history/IReproduceable{record} | ^EmptyError'

    @abstractmethod
    def _search7sparse_(sf, may_begin6sparse, may_rbegin6sparse, history2rank_, /):
        r'''
        [0 <= begin6sparse <= rbegin6sparse < sf.size7apparent] => may begin6sparse/uint%size7physical -> may rbegin6sparse/uint%size7physical -> (history -> (-1|0|+1)) -> (uint%6, may (i,history[i],-1), may (j,history[j],(0|+1)))/((0, i:history:-1, j:history:0)|(1, None, j:history:0)|(2, i:history:-1, j:history:+1)|(3, None, j:history:+1)|(4, i:history:-1, None)|(5, None, None))

        [left_vs_right7transition===False]
            #see:check_case6result4search8transition7L_
            # [search left_transition/(-1-->(0|+1)): search leftmost (0|+1)/rank, search right most -1/rank]
        [may_rbegin6sparse :: may rbegin6sparse/uint%size7apparent]
        [may_begin6sparse :: may begin6sparse/uint%size7apparent]
        '''#'''

    def search7sparse_(sf, history2rank_, /, *, offset=0, may_offsetted_begin6sparse=None, may_offsetted_rbegin6sparse=None, left_vs_right7transition=False):
        r'''
        [[i occurs] => [i :: sparse_idx]]
        [[j occurs] => [j :: sparse_idx]]
        * [left_vs_right7transition:=False]:
            :: (history -> (-1|0|+1)) -> (uint%6, may (i,history[i],-1), may (j,history[j],(0|+1)))/((0, i:history:-1, j:history:0)|(1, None, j:history:0)|(2, i:history:-1, j:history:+1)|(3, None, j:history:+1)|(4, i:history:-1, None)|(5, None, None))
            #see:check_case6result4search8transition7L_
            # [search left_transition/(-1-->(0|+1)): search leftmost (0|+1)/rank, search right most -1/rank]

        * [left_vs_right7transition:=True]:
            # useless
            # weird:[offset+begin6sparse <= j <= offset+rbegin6sparse]
            :: (history -> (-1|0|+1)) -> (int@[-6..=-1], may (i,history[i],(-1|0)), may (j,history[j],+1))/((-1, i:history:0, j:history:+1)|(-2, i:history:0, None)|(-3, i:history:-1, j:history:+1)|(-4, i:history:-1, None)|(-5, None, j:history:+1)|(-6, None, None))
            #see:check_case6result4search8transition7R_
            # [search right_transition/((-1|0)-->+1): search right most (-1|0)/rank, search leftmost +1/rank]

        [[j not occurs] => [asif:[j == (sf.size7apparent if may_offsetted_rbegin6sparse is None else 1+offset+rbegin6sparse)]]]
        [[i not occurs] => [asif:[i+1 == (0 if may_offsetted_begin6sparse is None else offset+begin6sparse)]]]
        [[j occurs][i occurs] => [0 <= i < j]]
        [[j occurs][i not occurs] => [0 <= j]]
        [[j occurs] => [(0 if may_offsetted_begin6sparse is None else 0+offset+begin6sparse) <= j < (sf.size7apparent if may_offsetted_rbegin6sparse is None else 1+offset+rbegin6sparse)]]



        [may_offsetted_rbegin6sparse :: may (offset+rbegin6sparse/uint%size7apparent)]
        [may_offsetted_begin6sparse :: may (offset+begin6sparse/uint%size7apparent)]

        '''#'''

        #old:'(history -> (-1|0|+1)) -> (uint%6, may history, may history)/((0, history/-1, history/0)|(1, None, history/0)|(2, history/-1, history/+1)|(3, None, history/+1)|(4, history/-1, None)|(5, None, None))'
        original__history2rank_ = history2rank_
        cached_original__history2rank_ = cached_version5history2rank_(original__history2rank_)
        history2rank_ = wrap4history2rank_(left_vs_right7transition, cached_original__history2rank_)

        may_rbegin6sparse = None if None is may_offsetted_rbegin6sparse else may_offsetted_rbegin6sparse -offset
        may_begin6sparse = None if None is may_offsetted_begin6sparse else may_offsetted_begin6sparse -offset
        if may_begin6sparse is not None is not may_rbegin6sparse and not 0 <= may_begin6sparse <= may_rbegin6sparse < (sf.size7apparent):raise ValueError(0, may_begin6sparse, may_rbegin6sparse, (sf.size7apparent))

        r = sf._search7sparse_(may_begin6sparse, may_rbegin6sparse, history2rank_)
        if not (offset == 0 or not any(r[1:])):
            r = (r[0], *(((offset+m[0], *m[1:]) if not None is m else m) for m in r[1:]))
        r
        r = wrap4result4search8transition_(left_vs_right7transition, cached_original__history2rank_, r)
        return r


    def search7dense_(sf, history2rank_, /, *, offset=0, may_offsetted_begin6sparse=None, may_offsetted_rbegin6sparse=None, zero6sparse_ok=False, recursive=True, validate6recursive=False, may_extra_output6recursive_=None, _max_size7dense_6SparseHistorySaver=2049, _max_size7physical_6SparseHistorySaver=65537, left_vs_right7transition=False, may_iter_subsequents_=None):
        r'''
        [[i,j occurs][zero6sparse_ok:=False] => [i+1==j]]
        [[i occurs][zero6sparse_ok:=True] => [i :: sparse_idx{some recursive level}]]
        [[j occurs][zero6sparse_ok:=True] => [j :: sparse_idx{some recursive level}]]
        * [left_vs_right7transition:=False]:
            :: (history -> (-1|0|+1)) -> (uint%6, may (i,history[i],-1), may (j,history[j],(0|+1)))/((0, i:history:-1, j:history:0)|(1, None, j:history:0)|(2, i:history:-1, j:history:+1)|(3, None, j:history:+1)|(4, i:history:-1, None)|(5, None, None))
            #see:check_case6result4search8transition7L_
            # [search left_transition/(-1-->(0|+1)): search leftmost (0|+1)/rank, search right most -1/rank]

        * [left_vs_right7transition:=True]:
            # useless
            # weird:[offset+begin6sparse <= j <= offset+rbegin6sparse]
            :: (history -> (-1|0|+1)) -> (int@[-6..=-1], may (i,history[i],(-1|0)), may (j,history[j],+1))/((-1, i:history:0, j:history:+1)|(-2, i:history:0, None)|(-3, i:history:-1, j:history:+1)|(-4, i:history:-1, None)|(-5, None, j:history:+1)|(-6, None, None))
            #see:check_case6result4search8transition7R_
            # [search right_transition/((-1|0)-->+1): search right most (-1|0)/rank, search leftmost +1/rank]


        [[j not occurs] => [asif:[j == (sf.size7apparent if may_offsetted_rbegin6sparse is None else 1+offset+rbegin6sparse)]]]
        [[i not occurs] => [asif:[i+1 == (0 if may_offsetted_begin6sparse is None else offset+begin6sparse)]]]
        [[j occurs][i occurs] => [0 <= i < j]]
        [[j occurs][i not occurs] => [0 <= j]]
        [[j occurs] => [(0 if may_offsetted_begin6sparse is None else 0+offset+begin6sparse) <= j < (sf.size7apparent if may_offsetted_rbegin6sparse is None else 1+offset+rbegin6sparse)]]




        #
        # @20260908:++kw:may_offsetted_begin6sparse
        # @20260908:++kw:left_vs_right7transition:
        #       False/default => search for ((-1),(0|+1))
        #       True => search for ((-1|0),(+1))
        #
        # for result_type@[left_vs_right7transition:=True] see: check_case6result4search8transition7R_()
        #
        '''#'''
        #
        #old:'(history -> (-1|0|+1)) -> (uint%6, may history, may history)/((0, history/-1, history/0)|(1, None, history/0)|(2, history/-1, history/+1)|(3, None, history/+1)|(4, history/-1, None)|(5, None, None))'
        original__history2rank_ = history2rank_
        cached_original__history2rank_ = cached_version5history2rank_(original__history2rank_)
        history2rank_ = wrap4history2rank_(left_vs_right7transition, cached_original__history2rank_)

        if not None is may_extra_output6recursive_:
            extra_output6recursive_ = may_extra_output6recursive_
            if not recursive:raise TypeError('[not recursive][not None is may_extra_output6recursive_]')
            #check_callable(extra_output6recursive_)
            extra_output6recursive_((offset, sf))
        # [may_extra_output6recursive_ :: may (((offset,IHistorySaver)) -> None)]
        # old:[may_extra_output6recursive_ :: may (((offset,IHistorySaver,[may_offsetted_rbegin6sparse,may_offsetted_rlast6sparse,may_offsetted_rend6sparse])) -> None)]
        r = sf.search7sparse_(history2rank_, offset=offset, may_offsetted_begin6sparse=may_offsetted_begin6sparse, may_offsetted_rbegin6sparse=may_offsetted_rbegin6sparse)
        match r:
            case ((0|2) as k, (i, history7neg_one, _neg_one), (j, history7zero_or_one, _zero_or_one)):
                assert _neg_one == -1
                assert _zero_or_one in (0,+1)
                assert None is may_offsetted_rbegin6sparse or j <= may_offsetted_rbegin6sparse, (sf, offset, r, may_offsetted_rbegin6sparse, j)
                assert None is may_offsetted_begin6sparse or j >= may_offsetted_begin6sparse, (sf, offset, r, may_offsetted_begin6sparse, j)

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
                    check_int_ge(3, _max_size7dense_6SparseHistorySaver)
                        # otherwise 2-->2 cause deadloop
                    ot = SparseHistorySaver(_max_size7dense_6SparseHistorySaver, _max_size7physical_6SparseHistorySaver, -1)

                    777;non_reproduceable_ok = not may_iter_subsequents_ is None
                    ot.append(history7neg_one, non_reproduceable_ok=non_reproduceable_ok)
                    ot.fills_(sz-1, may_iter_subsequents_=may_iter_subsequents_)
                    offset4ot = i
                    new_r = ot.search7dense_(history2rank_, offset=offset4ot, may_offsetted_begin6sparse=None, may_offsetted_rbegin6sparse=None, zero6sparse_ok=zero6sparse_ok, recursive=recursive, may_extra_output6recursive_=may_extra_output6recursive_, may_iter_subsequents_=may_iter_subsequents_)
                    _k = new_r[0]
                    if not (_k == 0 or _k == k):raise 000
                    if validate6recursive:
                        new_r7non_recursive = sf.search7dense_(history2rank_, offset=offset, may_offsetted_begin6sparse=may_offsetted_begin6sparse, may_offsetted_rbegin6sparse=may_offsetted_rbegin6sparse, zero6sparse_ok=zero6sparse_ok, recursive=not recursive, validate6recursive=not validate6recursive, may_iter_subsequents_=may_iter_subsequents_)
                        _check_result5search7dense_(may_offsetted_begin6sparse, may_offsetted_rbegin6sparse, zero6sparse_ok, new_r, new_r7non_recursive)
                else:
                    # not recursive
                    # !! [2 <= sz{may_offsetted_begin6sparse,may_offsetted_rbegin6sparse}]
                    new_r = _search7dense6non_recursive_(may_iter_subsequents_, history2rank_, history7neg_one, sz, i, j, _zero_or_one, k)
                new_r
            case _:
                new_r = r
        new_r
        new_r = wrap4result4search8transition_(left_vs_right7transition, cached_original__history2rank_, new_r)
        return new_r

    def search_key_points_(sf, stZhistory2rank_, op4fold_, st7fold, /, *, backward_vs_forward:bool, offset=0, _max_size7dense_6SparseHistorySaver=2049, _max_size7physical_6SparseHistorySaver=65537, may_iter_subsequents_=None):
        'see: backward_search_key_points_,forward_search_key_points_'
        return (sf.backward_search_key_points_ if not backward_vs_forward else sf.forward_search_key_points_)(stZhistory2rank_, op4fold_, st7fold, offset=offset, _max_size7dense_6SparseHistorySaver=_max_size7dense_6SparseHistorySaver, _max_size7physical_6SparseHistorySaver=_max_size7physical_6SparseHistorySaver, may_iter_subsequents_=may_iter_subsequents_)

    def backward_search_key_points_(sf, stZhistory2rank7bwd_, op4fold7bwd_, st7fold7bwd, /, *, offset=0, _max_size7dense_6SparseHistorySaver=2049, _max_size7physical_6SparseHistorySaver=65537, _ok__noneZzero_as_left_transition=False, may_iter_subsequents_=None):
        '[sf.size7apparent > 0][stZhistory2rank_(st7fold)(sf.last) >= 0] => ... -> (st7fold, [((-1+offset4key_point, history{-1+offset4key_point}, -1), (offset4key_point, history{offset4key_point}, (0|+1)))]) | ^EmptyError@{not$[sf.size7apparent > 0]} | ^ValueError@{not$[stZhistory2rank_(st7fold)(sf.last) >= 0]} # typing{args}:see above:IHistorySaverBase.__doc__ # [op4fold7bwd_::op4fold_{backward_search}]'
        # @20260908:++kw:_ok__noneZzero_as_left_transition
        #
        #unwind,rollback
        #old name:reversed_search_key_points_ --> new name:backward_search_key_points_
        #
        #vs:
        #   ===
        #   backward_search_key_points_:usage:to progressively search last prime factor of mul_order of base
        #       view ../../python3_src/seed/math/factor_pint/smooth_group_order_method.py
        #
        #   ===
        #   forward_search_key_points_:usage:to progressively search first factor of modulus
        #       view ../../python3_src/seed/algo/rho_method__7iter7batch.py
        #   ===
        #
        #
        ###########################
        # [left_vs_right7transition := False]
        ###########################
        if not sf:raise EmptyError
        # [sf.size7apparent > 0]
        (stZhistory2rank_, op4fold_, st7fold) = (stZhistory2rank7bwd_, op4fold7bwd_, st7fold7bwd)

        history2rank_ = stZhistory2rank_(st7fold)
            # history2rank_{k:=0}
        if not (rank_0_6last:=history2rank_(sf.last)) in (0,+1):raise ValueError('not satisfied precondition:[-1 =!= history2rank_{k:=0}(sf.last)]', sf, sf.last, st7fold, rank_0_6last)
        # [stZhistory2rank_(st7fold)(sf.last) >= 0]



        ls4key_record_ex = []
            # [((-1+j, history{-1+j}, -1), (j, key_point/history{j}), (0|+1))]

        #.if (rank_0_6head:=history2rank_(sf.head)) in (0,+1):
        #.    # ???TODO:probable_bug__noneZzero_as_left_transition: (None-->0) may be useful
        #.    return (st7fold, ls4key_record_ex)
        #.if not rank_0_6head == -1:raise 000 #ValueError(sf, sf.head, st7fold, rank_0_6head)
        #.# useless:[stZhistory2rank_(st7fold)(sf.head) == -1]
        #.#       head_rank_neednot_be_neg1:goto



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
        kwds = dict(may_extra_output6recursive_=extra_output6recursive_, zero6sparse_ok=False, recursive=True, validate6recursive=False, _max_size7dense_6SparseHistorySaver=_max_size7dense_6SparseHistorySaver, _max_size7physical_6SparseHistorySaver=_max_size7physical_6SparseHistorySaver, may_iter_subsequents_=may_iter_subsequents_)

        extra_output6recursive_((offset, sf))
        777;may_offsetted_rbegin6sparse = None
        # [len(ls4offsetted_saver) == 1]
        # xxx:!! [stZhistory2rank_(st7fold)(sf.head) == -1]
        # !! [stZhistory2rank_(st7fold)(sf.last) >= 0]
        # xxx:[-1 == history2rank_(ls4offsetted_saver[-1][-1].head)]
        # [(0|+1) == history2rank_(ls4offsetted_saver[-1][-1].last{@may_offsetted_rbegin6sparse})]
        while 1:
            # [len(ls4offsetted_saver) > 0]
            # xxx:[-1 == history2rank_(ls4offsetted_saver[-1][-1].head)]
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
                #       head_rank_neednot_be_neg1:here
                (may_offsetted_rbegin6sparse, _) = ls4offsetted_saver.pop()
                # [(0|+1) == history2rank_(ls4offsetted_saver[-1][-1].last{@may_offsetted_rbegin6sparse})]
                while ls4offsetted_saver:
                    if -1 == history2rank_(ls4offsetted_saver[-1][-1].head):break
                    # [(0|+1) == history2rank_(ls4offsetted_saver[-1][-1].head)]
                    (may_offsetted_rbegin6sparse, _) = ls4offsetted_saver.pop()
                    # [(0|+1) == history2rank_(ls4offsetted_saver[-1][-1].last{@may_offsetted_rbegin6sparse})]
                else:
                    # ???TODO:probable_bug__noneZzero_as_left_transition: (None-->0) may be useful
                    if _ok__noneZzero_as_left_transition:
                        raise NotImplementedError('[_ok__noneZzero_as_left_transition:=True]:unknown howto handle this case : maybe prepare history_saver such that history_saver.head is dummy useless node hence (rank:None-->0) is always useless')
                    return (st7fold, ls4key_record_ex)
                    break
                #end-while ls4offsetted_saver:
                # [len(ls4offsetted_saver) > 0]
                # [-1 == history2rank_(ls4offsetted_saver[-1][-1].head)]
                # [(0|+1) == history2rank_(ls4offsetted_saver[-1][-1].last{@may_offsetted_rbegin6sparse})]
                continue #@while 1:
            #end-if r[1] is None:
            # [-1 == history2rank_(ls4offsetted_saver[-1][-1].head)]
            # [(0|+1) == history2rank_(ls4offsetted_saver[-1][-1].last{@may_offsetted_rbegin6sparse})]
            # => left_transition
            assert r[1] is not None, r
            assert r[0] in (0,2)

            #########
            # found key_point/left_transition
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
            # !! [offsetted_rbegin6sparse{k round search} == offsetted_rend6sparse{k-1 round search}]
            offsetted_rbegin6sparse = offsetted_rend6sparse
            777;may_offsetted_rbegin6sparse = offsetted_rbegin6sparse
            st7fold = op4fold_(prev_history6key_point, offset4key_point, history6key_point, st7fold)
            history2rank_ = stZhistory2rank_(st7fold)
                # history2rank_{k:=1+k}
            if not history2rank_(prev_history6key_point) in (0,1):raise Exception('op4fold7bwd_() not satisfied postcondition:[op4fold7bwd_ :: [[history2rank_{k}(history{-1+j}) == -1][history2rank_{k}(history{j}) >= 0]] => prev_history6key_point/history{-1+j} -> j/uint%(offset+size7apparent) -> history6key_point/history{j} -> st7fold{k} -> st7fold{1+k}{[history2rank_{1+k}(history{-1+j}) >= 0]}]', sf, r, st7fold)
            # [(0|+1) == history2rank_(ls4offsetted_saver[-1][-1].last{@may_offsetted_rbegin6sparse})]
            # xxx:[-1 =?= history2rank_(ls4offsetted_saver[-1][-1].head)]
            continue
        raise 000
    #end-def backward_search_key_points_(sf, stZhistory2rank_, op4fold_, st7fold, /, *, offset=0, _max_size7dense_6SparseHistorySaver=2049, _max_size7physical_6SparseHistorySaver=65537):







    def forward_search_key_points_(sf, stZhistory2rank7fwd_, op4fold7fwd_, st7fold7fwd, /, *, offset=0, _max_size7dense_6SparseHistorySaver=2049, _max_size7physical_6SparseHistorySaver=65537, may_iter_subsequents_=None):
        ###########################
        # code base upon backward_search_key_points_():
        ###########################
        '[sf.size7apparent > 0][stZhistory2rank_(st7fold)(sf.head) == -1] => ... -> (st7fold, [((-1+offset4key_point, history{-1+offset4key_point}, -1), (offset4key_point, history{offset4key_point}, (0|+1)))]) | ^EmptyError@{not$[sf.size7apparent > 0]} | ^ValueError@{not$[stZhistory2rank_(st7fold)(sf.head) == -1]} # typing{args}:see above:IHistorySaverBase.__doc__ # [op4fold7fwd_::op4fold_{forward_search}]'
        ###########################
        # [left_vs_right7transition := False]
        ###########################
        if not sf:raise EmptyError
        # [sf.size7apparent > 0]
        (stZhistory2rank_, op4fold_, st7fold) = (stZhistory2rank7fwd_, op4fold7fwd_, st7fold7fwd)

        history2rank_ = stZhistory2rank_(st7fold)
            # history2rank_{k:=0}
        if not (rank_0_6head:=history2rank_(sf.head)) == -1:raise ValueError('not satisfied precondition:[-1 == history2rank_{k:=0}(sf.head)]', sf, sf.head, st7fold, rank_0_6head)
        # [stZhistory2rank_(st7fold)(sf.head) == -1]



        ls4key_record_ex = []
            # [((-1+j, history{-1+j}, -1), (j, key_point/history{j}), (0|+1))]




        ls4offsetted_saver = []
            # [(offset, IHistorySaver)]
        777;extra_output6recursive_=ls4offsetted_saver.append
        kwds = dict(may_extra_output6recursive_=extra_output6recursive_, zero6sparse_ok=False, recursive=True, validate6recursive=False, _max_size7dense_6SparseHistorySaver=_max_size7dense_6SparseHistorySaver, _max_size7physical_6SparseHistorySaver=_max_size7physical_6SparseHistorySaver, may_iter_subsequents_=may_iter_subsequents_)

        extra_output6recursive_((offset, sf))
        777;may_offsetted_begin6sparse = None
        # [len(ls4offsetted_saver) == 1]
        # !! [stZhistory2rank_(st7fold)(sf.head) == -1]
        # [-1 == history2rank_(ls4offsetted_saver[-1][-1].head{@may_offsetted_begin6sparse})]
        while 1:
            # [len(ls4offsetted_saver) > 0]
            # [-1 == history2rank_(ls4offsetted_saver[-1][-1].head{@may_offsetted_begin6sparse})]
            # xxx:[(0|+1) == history2rank_(ls4offsetted_saver[-1][-1].last)]
            (offset4ot, ot) = ls4offsetted_saver.pop()
            r = ot.search7dense_(history2rank_, offset=offset4ot, may_offsetted_begin6sparse=may_offsetted_begin6sparse, **kwds)
            777;ls4offsetted_saver#filled
            # [len(ls4offsetted_saver) > 0]
            assert r[0]&1 == 0, r
            assert r[1] is not None, r
            if r[2] is None:
                assert r[0] == 4
                # [-1 == history2rank_(ls4offsetted_saver[-1][-1].last)]
                (may_offsetted_begin6sparse, _) = ls4offsetted_saver.pop()
                # [-1 == history2rank_(ls4offsetted_saver[-1][-1].head{@may_offsetted_begin6sparse})]
                while ls4offsetted_saver:
                    if not -1 == history2rank_(ls4offsetted_saver[-1][-1].last):break
                    # [-1 == history2rank_(ls4offsetted_saver[-1][-1].last)]
                    (may_offsetted_begin6sparse, _) = ls4offsetted_saver.pop()
                    # [-1 == history2rank_(ls4offsetted_saver[-1][-1].head{@may_offsetted_begin6sparse})]
                else:
                    # (-1-->None) MUST BE useless
                    return (st7fold, ls4key_record_ex)
                    break
                #end-while ls4offsetted_saver:
                # [len(ls4offsetted_saver) > 0]
                # [-1 == history2rank_(ls4offsetted_saver[-1][-1].head{@may_offsetted_begin6sparse})]
                # [(0|+1) == history2rank_(ls4offsetted_saver[-1][-1].last)]
                continue #@while 1:
            #end-if r[2] is None:
            # [-1 == history2rank_(ls4offsetted_saver[-1][-1].head{@may_offsetted_begin6sparse})]
            # [(0|+1) == history2rank_(ls4offsetted_saver[-1][-1].last)]
            # => left_transition
            assert r[2] is not None, r
            assert r[0] in (0,2)

            #########
            # found key_point/left_transition
            #########
            match r:
                case ((0|2), (prev_offset4key_point, prev_history6key_point, -1) as _prev_key_record, (offset4key_point, history6key_point, (0|1)) as _key_record):
                    assert 1+prev_offset4key_point == offset4key_point
                case _:
                    raise Exception(sf, ot, st7fold, r)
            offsetted_last6sparse = prev_offset4key_point
            offsetted_end6sparse = offset4key_point
            ls4key_record_ex.append((_prev_key_record, _key_record))
            #########
            # search next key_point
            #########
            # !! [offsetted_begin6sparse{k round search} == offsetted_end6sparse{k-1 round search}]
            offsetted_begin6sparse = offsetted_end6sparse
            777;may_offsetted_begin6sparse = offsetted_begin6sparse
            st7fold = op4fold_(prev_history6key_point, offset4key_point, history6key_point, st7fold)
            history2rank_ = stZhistory2rank_(st7fold)
                # history2rank_{k:=1+k}
            if not history2rank_(history6key_point) == -1:raise Exception('op4fold7fwd_() not satisfied postcondition:[op4fold7fwd_ :: [[history2rank_{k}(history{-1+j}) == -1][history2rank_{k}(history{j}) >= 0]] => prev_history6key_point/history{-1+j} -> j/uint%(offset+size7apparent) -> history6key_point/history{j} -> st7fold{k} -> st7fold{1+k}{[history2rank_{1+k}(history{j}) == -1]}]', sf, r, st7fold)
            # [-1 == history2rank_(ls4offsetted_saver[-1][-1].head{@may_offsetted_begin6sparse})]
            # xxx:[(0|+1) =?= history2rank_(ls4offsetted_saver[-1][-1].last)]
            continue
        raise 000
    #end-def forward_search_key_points_(sf, stZhistory2rank_, op4fold_, st7fold, /, *, offset=0, _max_size7dense_6SparseHistorySaver=2049, _max_size7physical_6SparseHistorySaver=65537):






def cached_version5history2rank_(original__history2rank_, /):
    'history2rank_ -> cached-history2rank_'
    addr2h_rank = {}
    def cached_original__history2rank_(history, /):
        k = id(history)
        if not k in addr2h_rank:
            rank = original__history2rank_(history)
            addr2h_rank[k] = (history, rank)
                # hold history => addr valid
        return addr2h_rank[k][1]
    return cached_original__history2rank_
def wrap4history2rank_(left_vs_right7transition, original__history2rank_, /):
    'left_vs_right7transition/bool -> history2rank_{search:left_transition} -> history2rank_{search:left_vs_right7transition}'
    if not left_vs_right7transition:
        # {search:left_transition}
        return original__history2rank_
    # {search:right_transition}
    def history2rank_(history, /):
        rank = original__history2rank_(history)
        assert -1 <= rank <= +1
        _rank = max(-1, -1+rank)
        assert -1 <= _rank <= 0
        return _rank
    return history2rank_
def _restore_rank_(cached_original__history2rank_, may_i_h_k, /):
    'may_i_h_k -> (old_vs_new, may_i_h_k)'
    # see:wrap4history2rank_{search:right_transition}
    old_vs_new = False
    match may_i_h_k:
        case None:
            pass
        case (i, history, rank):
            _rank = +1 if rank == 0 else cached_original__history2rank_(history)
            if not _rank == rank:
                may_i_h_k = (i, history, _rank)
                old_vs_new = True
        case _:
            raise Exception(may_i_h_k)
    # False/old <==> (None --> None)|(-1 --> -1)|(+1 --> +1)
    # True/new <==> (-1 --> 0)|(0 --> +1)
    return (old_vs_new, may_i_h_k)
def _may_at2_(may_i_h_k, /):
    return None if may_i_h_k is None else may_i_h_k[2]
def wrap4result4search8transition_(left_vs_right7transition, cached_original__history2rank_, result4search8transition, /):
    'left_vs_right7transition/bool -> (history->(-1|0|+1)) -> result4search8transition{left_transition} -> result4search8transition{left_vs_right7transition}'
    check_case6result4search8transition7L_(result4search8transition)
    if not left_vs_right7transition:
        # {search:left_transition}
        return result4search8transition
    _result4search8transition = result4search8transition
    777;result4search8transition = None
    # {search:right_transition}
    (_case, _may_i_h_k, _may_j_h_k) = _result4search8transition
        # (uint%6, may (i,history[i],-1), may (j,history[j],(0|+1)))
    (old_vs_new7i, may_i_h_k) = _restore_rank_(cached_original__history2rank_, _may_i_h_k)
    (old_vs_new7j, may_j_h_k) = _restore_rank_(cached_original__history2rank_, _may_j_h_k)
        # False/old <==> (None --> None)|(-1 --> -1)|(+1 --> +1)
        # True/new <==> (-1 --> 0)|(0 --> +1)
    _mki = _may_at2_(_may_i_h_k)
    _mkj = _may_at2_(_may_j_h_k)
    mki = _may_at2_(may_i_h_k)
    mkj = _may_at2_(may_j_h_k)
    if old_vs_new7i:
        # i{new}
        assert _mki == -1
        assert mki == 0
    else:
        # i{old}
        assert _mki is None or _mki == -1
        assert mki == _mki

    if old_vs_new7j:
        # j{new}
        assert _mkj == 0
        assert mkj == +1
    else:
        # j{old}
        assert _mkj is None or _mkj == +1
        assert mkj == _mkj

    match (_case, old_vs_new7i, _mki, mki, old_vs_new7j, _mkj, mkj):
        # result4search{left_transition}:((0, i:history:-1, j:history:0)|(1, None, j:history:0)|(2, i:history:-1, j:history:+1)|(3, None, j:history:+1)|(4, i:history:-1, None)|(5, None, None))
        #   0:-1,0
        #   1:None,0
        #   2:-1,+1
        #   3:None,+1
        #   4:-1,None
        #   5:None,None
        #
        # result4search{right_transition}:((-1, i:history:0, j:history:+1)|(-2, i:history:0, None)|(-3, i:history:-1, j:history:+1)|(-4, i:history:-1, None)|(-5, None, j:history:+1)|(-6, None, None))
        #   -1:0,+1
        #   -2:0,None
        #   -3:-1,+1
        #   -4:-1,None
        #   -5:None,+1
        #   -6:None,None
        #
        # False/old <==> (None --> None)|(-1 --> -1)|(+1 --> +1)
        # True/new <==> (-1 --> 0)|(0 --> +1)
        case (0, False, -1, -1, True, 0, 1):
            case = -3
        case (0, True, -1, 0, True, 0, 1):
            case = -1
        case (1, False, None, None, True, 0, 1):
            case = -5
        case (2, False, -1, -1, False, 1, 1):
            case = -3
        case (2, True, -1, 0, False, 1, 1):
            case = -1
        case (3, False, None, None, False, 1, 1):
            case = -5
        case (4, False, -1, -1, False, None, None):
            case = -4
        case (4, True, -1, 0, False, None, None):
            case = -2
        case (5, False, None, None, False, None, None):
            case = -6
        case bad:
            raise Exception(bad)
    result4search8transition = (case, may_i_h_k, may_j_h_k)
    check_case6result4search8transition7R_(result4search8transition)
    return result4search8transition
def check_case6result4search8transition_(left_vs_right7transition, result4search8transition, /):
    if not left_vs_right7transition:
        # left
        check_case6result4search8transition7L_(result4search8transition)
    else:
        # right
        check_case6result4search8transition7R_(result4search8transition)
def check_case6result4search8transition7L_(result4search8transition, /):
    r'''
    # result4search{left_transition}:((0, i:history:-1, j:history:0)|(1, None, j:history:0)|(2, i:history:-1, j:history:+1)|(3, None, j:history:+1)|(4, i:history:-1, None)|(5, None, None))
    #   0:-1,0
    #   1:None,0
    #   2:-1,+1
    #   3:None,+1
    #   4:-1,None
    #   5:None,None
    #
    '''#'''
    match result4search8transition:
        case (0, (_, _, -1), (_, _, 0)):pass
        case (1, None, (_, _, 0)):pass
        case (2, (_, _, -1), (_, _, 1)):pass
        case (3, None, (_, _, 1)):pass
        case (4, (_, _, -1), None):pass
        case (5, None, None):pass
        case _:
            raise TypeError(result4search8transition)
def check_case6result4search8transition7R_(result4search8transition, /):
    r'''
    # result4search{right_transition}:((-1, i:history:0, j:history:+1)|(-2, i:history:0, None)|(-3, i:history:-1, j:history:+1)|(-4, i:history:-1, None)|(-5, None, j:history:+1)|(-6, None, None))
    #   -1:0,+1
    #   -2:0,None
    #   -3:-1,+1
    #   -4:-1,None
    #   -5:None,+1
    #   -6:None,None
    #
    '''#'''
    match result4search8transition:
        case (-1, (_, _, 0), (_, _, 1)):pass
        case (-2, (_, _, 0), None):pass
        case (-3, (_, _, -1), (_, _, 1)):pass
        case (-4, (_, _, -1), None):pass
        case (-5, None, (_, _, 1)):pass
        case (-6, None, None):pass
        case _:
            raise TypeError(result4search8transition)


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
def _check_result5search7dense_(may_offsetted_begin6sparse, may_offsetted_rbegin6sparse, zero6sparse_ok, new_r7recursive, new_r7non_recursive, /):
    (k1, (i1, _, _1_neg1), (j1, _, rank1)) = new_r7recursive#maybe zero6sparse_ok
    (k2, (i2, _, _2_neg1), (j2, _, rank2)) = new_r7non_recursive
    assert _1_neg1 == -1
    assert _2_neg1 == -1
    assert k1 in (0,2)
    assert k2 in (0,2)
    #assert 0 <= k2 <= k1 <= 2
    assert 0 <= k2 == k1 <= 2
    assert 0 <= rank2 == rank1 <= 1
    assert 0 <= i1 <= i2 == -1+j2 < j2 <= j1 # !! zero6sparse_ok
    assert (zero6sparse_ok and rank2 == rank1 == 0) or 0 <= i1 == i2 == -1+j2 < j2 == j1
    assert None is may_offsetted_rbegin6sparse or j2 <= j1 <= may_offsetted_rbegin6sparse
    assert None is may_offsetted_begin6sparse or may_offsetted_begin6sparse <= j2 <= j1
def _search7dense6non_recursive_(may_iter_subsequents_, history2rank_, history7neg_one, sz, i, j, _zero_or_one, k, /):
    iter_subsequents_ = ifNone(may_iter_subsequents_, iter_snds4reproduceable_)
    777;non_reproduceable_ok = not may_iter_subsequents_ is None
    for _j, history in enumerate(islice(iter_subsequents_(history7neg_one), 0, sz), 1+i):
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
class IHistorySaverBase__bisect7single_array__7view_or_gmk_cached_list(IHistorySaverBase):
    # gmk - get or make
    __slots__ = ()
    @abstractmethod
    def _view_or_gmk_cached_list4history_array_(sf, /):
        '-> (view [history]|cached [history])'
    @abstractmethod
    def _apparent_idx5physical_idx4history_array_(sf, physical_idx, /):
        'physical_idx/uint%size7physical -> apparent_idx/uint%size7apparent'
    @abstractmethod
    def _physical_idx5apparent_idx6sparse4history_array_(sf, apparent_idx6sparse, /):
        'apparent_idx6sparse{from physical_idx}/uint%size7apparent -> physical_idx/uint%size7physical # [apparent_idx6sparse == sf._apparent_idx5physical_idx4history_array_(physical_idx)]'
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
    def _search7sparse_(sf, may_begin6sparse, may_rbegin6sparse, history2rank_, /):
        #.ls = sf._history_array_view_
        ls = sf._view_or_gmk_cached_list4history_array_()
        j2rank_ = _mk_j2rank_(history2rank_, ls)
        L = len(ls)
        js = range(L)
        end = L if None is may_rbegin6sparse else 1+sf.physical_idx5apparent_idx6sparse4history_array_(may_rbegin6sparse)
        begin = 0 if None is may_begin6sparse else 0+sf.physical_idx5apparent_idx6sparse4history_array_(may_begin6sparse)
        assert 0 <= end <= L # <<== [L==0]
        assert 0 <= begin <= L # <<== [L==0]
        if L > 0:
            assert 1 <= end <= L
            assert 0 <= begin < L
        else:
            assert begin == 0 == end
            assert may_begin6sparse is None is may_rbegin6sparse

        j = bisect_right(js, -1, begin, end, key=j2rank_)
        #check_uint_lt(1+L, j)
        #check_uint_lt(1+end, j)
        check_int_ge_lt(begin, 1+end, j)
        # [begin <= j <= end == 1+rbegin]
        # [0 <= begin <= j <= 1+rbegin]
        # [-1 <= -1+begin <= i == j-1 <= rbegin]
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
        if j == begin:
            # if j == 0:
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
        # !! non_reproduceable_ok{not None is may_iter_subsequents_}
        #.check_type_le(IReproduceable, history)
        rank = history2rank_(history)
        check_int_ge_le(-1, +1, rank)
        return rank
    return j2rank_

class IHistorySaverBase__bisect7single_array_view(IHistorySaverBase__bisect7single_array__7view_or_gmk_cached_list):
    __slots__ = ()
    @property
    @abstractmethod
    def _history_array_view_(sf, /):
        '-> [history]'
    @override
    def _view_or_gmk_cached_list4history_array_(sf, /):
        '-> (view [history]|cached [history])'
        return sf._history_array_view_
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


class IHistorySaver7immutable(IHistorySaverBase):
    # vivi:IHistorySaver
    __slots__ = ()
    # immutable_part
    @abstractmethod
    def __hash__(sf, /):
        '!! immutable'
    @abstractmethod
    def __eq__(sf, ot, /):
        '!! immutable'
    @abstractmethod
    def _oo_append6underfill_(sf, history, /):
        '[not .full] => IHistorySaver7immutable{settings}{len==sz<max_size7apparent} -> history/IReproduceable{record} -> IHistorySaver7immutable{settings}{len==1+sz<=max_size7apparent}'
    @abstractmethod
    def oo_clear(sf, /):
        'IHistorySaver7immutable{settings} -> IHistorySaver7immutable{settings}{empty}'
        #vs:clear()


    @override
    def copy(sf, /):
        return sf
    @override
    def mk_empty_(sf, /):
        'sf/cls -> ot/cls # [0 == len(ot)]'
        #vs:mk_empty_
        return sf.oo_clear()
    @override
    def mk_solo_(sf, head, /, *, non_reproduceable_ok=False):
        'sf/cls -> head/last/IReproduceable -> ot/cls # [1 == len(ot)][head is ot.head is ot.last]'
        if len(sf) == 1 and sf.head is head:
            ot = sf
        else:
            ot = sf.oo_clear().oo_append(head, non_reproduceable_ok=non_reproduceable_ok)
        return ot

    def __ne__(sf, ot, /):
        return not sf == ot
    def oo_extend(sf, iter4history, /, *, non_reproduceable_ok=False):
        'sf/IHistorySaver7immutable -> Iter history/IReproduceable{record} -> IHistorySaver7immutable|^FullError'
        ot = sf
        for history in iter4history:
            ot = ot.oo_append(history, non_reproduceable_ok=non_reproduceable_ok)
                # ^FullError
        return ot
    def oo_append(sf, history, /, *, non_reproduceable_ok=False):
        'sf/IHistorySaver7immutable -> history/IReproduceable{record} -> ot/IHistorySaver7immutable|^FullError{sf} # [ot.last{new} is history][ot.head{new} is (if [sf.size7apparent{old} > 0] then sf.head{old} else history)][ot.size7apparent{new} == 1+sf.size7apparent{old}][[sf.size7physical{old} < 2] -> [ot.size7physical{new} == 1+sf.size7physical{old}]][[sf.size7physical{old} >= 2] -> [ot.size7physical{new} >= 2]]'
        if non_reproduceable_ok:
            pass
        else:
            check_type_le(IReproduceable, history)

        if sf.full: raise FullError(sf)
        ot = sf._oo_append6underfill_(history)
        return ot
    def oo_fills_(sf, max4sz, /, *, may_iter_subsequents_=None):
        'sf/IHistorySaver7immutable -> uint -> ot/IHistorySaver7immutable|^FullError{ot}|^EmptyError'
        #vs:fills_
        check_int_ge(0, max4sz)
        history = sf.last
            # ^EmptyError
        iter_subsequents_ = ifNone(may_iter_subsequents_, iter_snds4reproduceable_)
        777;non_reproduceable_ok = not may_iter_subsequents_ is None
        it = islice(iter_subsequents_(history), 0, max4sz)
        ot = sf.oo_extend(it, non_reproduceable_ok=non_reproduceable_ok)
            # ^FullError
        return ot

        ot = sf
        for history in it:
            ot = ot.oo_append(history, non_reproduceable_ok=non_reproduceable_ok)
                # ^FullError{ot}
        return ot
    def oo_fills7unlimit_(sf, /, *, may_iter_subsequents_=None):
        'sf/IHistorySaver7immutable -> ot/IHistorySaver7immutable|^EmptyError'
        if sf.full: return sf
        history = sf.last
            # ^EmptyError
        iter_subsequents_ = ifNone(may_iter_subsequents_, iter_snds4reproduceable_)
        777;non_reproduceable_ok = not may_iter_subsequents_ is None
        ot = sf
        for history in iter_subsequents_(history):
            ot = ot.oo_append(history, non_reproduceable_ok=non_reproduceable_ok)
                # ^FullError{ot}
            if ot.full: break
        return ot
    def ii_both_fills7unlimit_(sf, ot, /, *, may_iter_subsequents_=None):
        'sf/IHistorySaver7immutable -> ot/IHistorySaver7immutable -> (new_sf/IHistorySaver7immutable, new_ot/IHistorySaver7immutable)|^EmptyError # [sf.last is ot.last] # expected: [ot.imay_max_size7apparent == -1]'
        #vs:oo_fills7unlimit_
        #vs:both_fills7unlimit_
        history = sf.last
            # ^EmptyError
        _history = ot.last
            # ^EmptyError
        if not history is _history:raise ValueError('[sf.last is not ot.last]@sf.ii_both_fills7unlimit_(ot)')
        if sf is ot:raise ValueError('[sf is ot]@sf.both_fills7unlimit_(ot)')
        if sf.full: return (sf, ot)
        if ot.full: return (sf, ot)

        iter_subsequents_ = ifNone(may_iter_subsequents_, iter_snds4reproduceable_)
        777;non_reproduceable_ok = not may_iter_subsequents_ is None
        for history in iter_subsequents_(history):
            sf = sf.oo_append(history, non_reproduceable_ok=non_reproduceable_ok)
            ot = ot.oo_append(history, non_reproduceable_ok=non_reproduceable_ok)
            if sf.full: return (sf, ot)
            if ot.full: return (sf, ot)
        return (sf, ot)
    def oo_clear_but_last_(sf, /):
        'sf/IHistorySaver7immutable -> ot/IHistorySaver7immutable # [[sf.size7apparent{old} > 0] -> [[ot.head{new} is ot.last{new} is sf.last{old}][ot.size7apparent{new} == 1][ot.size7physical{new} == 1]]] # [extern:offset{ot} = offset{sf} +max(0,-1+sf.size7apparent{old})]'
        #vs:clear_but_last_()
        #vs:oo_clear()
        #vs:clear()
        if len(sf) >= 2:
            last = sf.last
            ot = sf.oo_clear()
            ot = ot.oo_append(last, non_reproduceable_ok=True)
        else:
            ot = sf
        return ot


#稀疏快照纟可重演序列
class IHistorySaver7mutable(IHistorySaverBase):
    # == IHistorySaver
    # vs:IHistorySaver7immutable
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
    # mutable_part
    @abstractmethod
    def _append6underfill_(sf, history, /):
        '[not .full] => history/IReproduceable{record} -> None'
    @abstractmethod
    def clear(sf, /):
        '-> None'


    @override
    def mk_solo_(sf, head, /, *, non_reproduceable_ok=False):
        'sf/cls -> head/last/IReproduceable -> ot/cls # [1 == len(ot)][head is ot.head is ot.last]'
        ot = sf.mk_empty_()
        ot.append(head, non_reproduceable_ok=non_reproduceable_ok)
        return ot
    def extend(sf, iter4history, /, *, non_reproduceable_ok=False):
        'Iter history/IReproduceable{record} -> None|^FullError'
        for history in iter4history:
            sf.append(history, non_reproduceable_ok=non_reproduceable_ok)
                # ^FullError
    def append(sf, history, /, *, non_reproduceable_ok=False):
        'history/IReproduceable{record} -> None|^FullError # [sf.last{new} is history][sf.head{new} is (if [sf.size7apparent{old} > 0] then sf.head{old} else history)][sf.size7apparent{new} == 1+sf.size7apparent{old}][[sf.size7physical{old} < 2] -> [sf.size7physical{new} == 1+sf.size7physical{old}]][[sf.size7physical{old} >= 2] -> [sf.size7physical{new} >= 2]]'
        if non_reproduceable_ok:
            pass
        else:
            check_type_le(IReproduceable, history)
        if sf.full: raise FullError
        sf._append6underfill_(history)
    def fills_(sf, max4sz, /, *, may_iter_subsequents_=None):
        'uint -> None|^FullError|^EmptyError'
        check_int_ge(0, max4sz)
        history = sf.last
            # ^EmptyError
        iter_subsequents_ = ifNone(may_iter_subsequents_, iter_snds4reproduceable_)
        777;non_reproduceable_ok = not may_iter_subsequents_ is None
        it = islice(iter_subsequents_(history), 0, max4sz)
        sf.extend(it, non_reproduceable_ok=non_reproduceable_ok)
            # ^FullError
        return

        for history in it:
            sf.append(history, non_reproduceable_ok=non_reproduceable_ok)
                # ^FullError
    def fills7unlimit_(sf, /, *, may_iter_subsequents_=None):
        '-> None|^EmptyError'
        if sf.full: return
        history = sf.last
            # ^EmptyError
        iter_subsequents_ = ifNone(may_iter_subsequents_, iter_snds4reproduceable_)
        777;non_reproduceable_ok = not may_iter_subsequents_ is None
        for history in iter_subsequents_(history):
            sf.append(history, non_reproduceable_ok=non_reproduceable_ok)
            if sf.full: return
    def both_fills7unlimit_(sf, ot, /, *, may_iter_subsequents_=None):
        '-> None|^EmptyError # [sf.last is ot.last] # expected: [ot.imay_max_size7apparent == -1]'
        #vs:fills7unlimit_
        history = sf.last
            # ^EmptyError
        _history = ot.last
            # ^EmptyError
        if not history is _history:raise ValueError('[sf.last is not ot.last]@sf.both_fills7unlimit_(ot)')
        if sf is ot:raise ValueError('[sf is ot]@sf.both_fills7unlimit_(ot)')
        if sf.full: return
        if ot.full: return

        iter_subsequents_ = ifNone(may_iter_subsequents_, iter_snds4reproduceable_)
        777;non_reproduceable_ok = not may_iter_subsequents_ is None
        for history in iter_subsequents_(history):
            sf.append(history, non_reproduceable_ok=non_reproduceable_ok)
            ot.append(history, non_reproduceable_ok=non_reproduceable_ok)
            if sf.full: return
            if ot.full: return
    def clear_but_last_(sf, /):
        '-> None # [[sf.size7apparent{old} > 0] -> [[sf.head{new} is sf.last{new} is sf.last{old}][sf.size7apparent{new} == 1][sf.size7physical{new} == 1]]] # [extern:offset{sf} += max(0,-1+sf.size7apparent{old})]'
        if len(sf) >= 2:
            last = sf.last
            sf.clear()
            sf.append(last, non_reproduceable_ok=True)

IHistorySaver = IHistorySaver7mutable
class IHistorySaver7mutable__bisect7single_array_view(IHistorySaverBase__bisect7single_array_view, IHistorySaver7mutable):
    __slots__ = ()
IHistorySaver__bisect7single_array_view = IHistorySaver7mutable__bisect7single_array_view

class IHistorySaver7immutable__bisect7single_array__7view_or_gmk_cached_list(IHistorySaverBase__bisect7single_array__7view_or_gmk_cached_list, IHistorySaver7immutable):
    __slots__ = ()

class DenseHistorySaver(IHistorySaver__bisect7single_array_view):
    ___no_slots_ok___ = True
    #def __init__(sf, max_size7apparent, /):
    #   !! pickle
    def __new__(cls, max_size7apparent, danger_mark='!', may_history_array=None, /, *, no_copy=False):
        #see:__new__,__getnewargs__,__repr__,fmap_,copy
        check_danger_mark_(danger_mark)
        check_int_ge(1, max_size7apparent)
        sf = super(__class__, cls).__new__(cls)
        if None is may_history_array:
            history_array = []
        else:
            history_array = may_history_array
            if not len(history_array) <= max_size7apparent:raise TypeError(max_size7apparent, len(history_array))
            if no_copy:
                # arbitrary seq ok
                #   eg:tuple, but then not allow ops7mutable{append...}
                pass
            else:
                history_array = list(history_array)
            history_array
        history_array

        sf._m = max_size7apparent
        sf._ls = history_array
        return sf
    @override
    def mk_empty_(sf, /):
        'sf/cls -> ot/cls # [0 == len(ot)]'
        cls = type(sf)
        max_size7apparent = sf._m
        return cls(max_size7apparent)
    @override
    def copy(sf, /):
        cls = type(sf)
        args = cls.__getnewargs__(sf)
        return cls(*args, no_copy=False)
    def __repr__(sf, /):
        cls = type(sf)
        args = cls.__getnewargs__(sf)
        return repr_helper(sf, *args)
        max_size7apparent = sf._m
        history_array = sf._ls
        #return f'DenseHistorySaver({max_size7apparent!r}, history_array = {history_array!r})'
        #return repr_helper(sf, max_size7apparent, history_array=history_array)
        return repr_helper_ex(sf, [max_size7apparent], 'history_array'.split(), {}, ordered_attrs_only=True, compact6kwargs=True, vars4self=locals())
    def validate(sf, /):
        max_size7apparent = sf._m
        history_array = sf._ls
        check_int_ge(1, max_size7apparent)
        assert len(history_array) <= max_size7apparent
    @override
    def __getnewargs__(sf, /):
        max_size7apparent = sf._m
        history_array = sf._ls # [no_copy:=True]
        if not sf:
            args = (max_size7apparent,)
        else:
            args = (max_size7apparent, '!', history_array)
        return args
        ###############
        #old_version7separated:
        ###############
        max_size7apparent = sf._m
        args = (max_size7apparent,)
        return args
    @override
    def __getstate__(sf, /):
        return None
        ###############
        #old_version7separated:
        ###############
        history_array = sf._ls
        st4pickle = tuple(history_array)
        return st4pickle
    @override
    def __setstate__(sf, st4pickle, /):
        raise 000
        ###############
        #old_version7separated:
        ###############
        history_array = st4pickle
        sf._ls[:] = history_array
    @override
    def fmap_(sf, transform4reproduceable, /):
        if not sf:
            return sf.copy()
        max_size7apparent = sf._m
        history_array = sf._ls # [no_copy:=True]
        if not sf:
            args = (max_size7apparent,)
        else:
            history_array = list(map(transform4reproduceable, history_array))
                # !! [no_copy:=True]
                # => list()
            args = (max_size7apparent, '!', history_array)
        args
        cls = type(sf)
        ot = cls(*args, no_copy=True)
        return ot
        ###############
        #old_version7separated:
        ###############
        cls = type(sf)
        st4pickle = cls.__getstate__(sf)
        history_array = st4pickle
        history_array = tuple(map(transform4reproduceable, history_array))
        st4pickle = history_array
        args = cls.__getnewargs__(sf)
        ot = cls(*args)
        ot.__setstate__(st4pickle)
        return ot
        max_size7apparent = sf._m
        history_array = sf._ls
        ot = DenseHistorySaver(max_size7apparent)
        ot._ls = [*map(transform4reproduceable, history_array)]
        return ot
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


class SparseHistorySaver(IHistorySaver__bisect7single_array_view):
    ___no_slots_ok___ = True
    #def __init__(sf, max_size7dense, max_size7physical, imay_max_size7apparent, /):
    #   !! pickle
    def __new__(cls, max_size7dense, max_size7physical, imay_max_size7apparent, danger_mark='!', payload=None, /, *, no_copy=False):
        #see:__new__,__getnewargs__,__repr__,fmap_,copy
        r'''
        recommend:[1 == max_size7physical%2]
        [payload :: may (history_array, size7apparent, curr_max_size7physical, curr_step, last_step)]
        '''#'''
        check_danger_mark_(danger_mark)
        check_int_ge(2, max_size7dense)
        check_int_ge(max_size7dense, max_size7physical)
        check_int_ge(-1, imay_max_size7apparent)
        if not -1 == imay_max_size7apparent:
            check_int_ge(max_size7physical, imay_max_size7apparent)
        sf = super(__class__, cls).__new__(cls)
        sf._msz0 = max_size7dense
        sf._msz1 = max_size7physical
        sf._imsz2 = imay_max_size7apparent
        sf._ls = history_array = []
        sf.clear()
        if not None is payload:
            sf._set_payload_(payload, no_copy=no_copy)
        return sf
    @override
    def clear(sf, /):
        sf._ls.clear()#history_array
        sf._sz = size7apparent = 0
        sf._msz = curr_max_size7physical = max_size7dense = sf._msz0
        sf._step = curr_step = 1
        sf._cn = last_step = 1
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
    @override
    def mk_empty_(sf, /):
        'sf/cls -> ot/cls # [0 == len(ot)]'
        cls = type(sf)
        settings = sf._get_settings_()
        return cls(*settings)
    @override
    def copy(sf, /):
        cls = type(sf)
        args = cls.__getnewargs__(sf)
        return cls(*args, no_copy=False)
    def __repr__(sf, /):
        cls = type(sf)
        args = cls.__getnewargs__(sf)
        return repr_helper(sf, *args)
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


    @override
    def __getnewargs__(sf, /):
        settings = sf._get_settings_()
        if not sf:
            args = settings
        else:
            # !! __repr__
            payload = sf._get_payload_(no_copy=True)
            args = (*settings, '!', payload)
        return args
        ###############
        #old_version7separated:
        ###############
        return sf._0_getnewargs_0_()
    def _get_settings_(sf, /):
        return sf._0_getnewargs_0_()
    def _0_getnewargs_0_(sf, /):
        max_size7dense = sf._msz0
        max_size7physical = sf._msz1
        imay_max_size7apparent = sf._imsz2
        args = (max_size7dense, max_size7physical, imay_max_size7apparent)
        return args
    @override
    def __getstate__(sf, /):
        #see:clear(),validate()
        return None
        ###############
        #old_version7separated:
        ###############
        return sf._0_getstate_0_(no_copy=False)
    def _get_payload_(sf, /, *, no_copy):
        return sf._0_getstate_0_(no_copy=no_copy)
    def _0_getstate_0_(sf, /, *, no_copy):
        history_array = sf._ls
        size7apparent = sf._sz
        curr_max_size7physical = sf._msz
        curr_step = sf._step
        last_step = sf._cn

        history_array = history_array if no_copy else tuple(history_array)
        curr_params = (size7apparent, curr_max_size7physical, curr_step, last_step)
        st4pickle = (history_array, *curr_params)
        return st4pickle
    @override
    def __setstate__(sf, st4pickle, /):
        raise 000
        ###############
        #old_version7separated:
        ###############
        sf._0_setstate_0_(st4pickle, no_copy=False)
    def _set_payload_(sf, payload, /, *, no_copy):
        sf._0_setstate_0_(payload, no_copy=no_copy)
    def _0_setstate_0_(sf, st4pickle, /, *, no_copy):
        (history_array, *curr_params) = st4pickle
        (size7apparent, curr_max_size7physical, curr_step, last_step) = curr_params
        # .,.+4s/\(\w\+\) = sf\.\(\w\+\)/sf.\2 = \1
        if no_copy:
            sf._ls = history_array
        else:
            sf._ls[:] = history_array
        sf._sz = size7apparent
        sf._msz = curr_max_size7physical
        sf._step = curr_step
        sf._cn = last_step
        if _debug:sf.validate()
    @override
    def fmap_(sf, transform4reproduceable, /):
        if not sf:
            return sf.copy()
        cls = type(sf)
        settings = sf._get_settings_()
        if not sf:
            args = settings
        else:
            payload = sf._get_payload_(no_copy=True)
            (history_array, *curr_params) = payload
            history_array = list(map(transform4reproduceable, history_array))
                # !! [no_copy:=True]
                # => list()
            payload = (history_array, *curr_params)
            args = (*settings, '!', payload)
        ot = cls(*args, no_copy=True)
        return ot
        ###############
        #old_version7separated:
        ###############
        cls = type(sf)
        st4pickle = cls.__getstate__(sf)
        (history_array, *curr_params) = st4pickle
        history_array = tuple(map(transform4reproduceable, history_array))
        st4pickle = (history_array, *curr_params)
        args = cls.__getnewargs__(sf)
        ot = cls(*args)
        ot.__setstate__(st4pickle)
        return ot
        max_size7dense = sf._msz0
        max_size7physical = sf._msz1
        imay_max_size7apparent = sf._imsz2
        history_array = sf._ls
        ot = SparseHistorySaver(max_size7dense, max_size7physical, imay_max_size7apparent)
        ot._ls = [*map(transform4reproduceable, history_array)]
        #see:clear()
        ot._sz = sf._sz
        ot._msz = sf._msz
        ot._step = sf._step
        ot._cn = sf._cn
        return ot
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
                    # SparseHistorySaver7immutable:fixed_bug4remain_size4last_step:goto
                    #   => recommend:[1 == max_size7physical%2]
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





class SparseHistorySaver7immutable(IHistorySaver7immutable__bisect7single_array__7view_or_gmk_cached_list):
    ___no_slots_ok___ = True
    r'''[[[
    def __new__(cls, max_size7physical__or__settings, imay_max_size7apparent__or__data, /):
        match (max_size7physical__or__settings, imay_max_size7apparent__or__data):
            case ((max_size7physical, imay_max_size7apparent), data):
                pass
            case (max_size7physical, imay_max_size7apparent):
                data = _gmk_data0_()
        ####################
        (max_size7physical, imay_max_size7apparent)
        data
        ####################
    #]]]'''#'''
    def __new__(cls, max_size7physical, imay_max_size7apparent, danger_mark='!', data=None, /):
        #see:__new__,__getnewargs__,__repr__,fmap_,copy
        #__new__.__doc__:see below
        #'recommend:[1 == max_size7physical%2]'
        # !! pickle
        # no:__init__
        check_danger_mark_(danger_mark)
        data = ifNonef(data, _gmk_data0_)

        ####################
        (max_size7physical, imay_max_size7apparent)
        data
        ####################
        check_int_ge(2, max_size7physical)
        check_int_ge(-1, imay_max_size7apparent)
        if not -1 == imay_max_size7apparent:
            max_size7apparent = imay_max_size7apparent
            #check_int_ge(max_size7physical, max_size7apparent)
            check_int_ge(2, max_size7apparent)
            max_size7physical = min(max_size7physical, max_size7apparent)
        check_int_ge(2, max_size7physical)
        if not -1 == imay_max_size7apparent:
            check_int_ge(max_size7physical, max_size7apparent)
        sf = super(__class__, cls).__new__(cls)
        sf._settings = (max_size7physical, imay_max_size7apparent)
        sf._data = data
        if _debug:sf.validate()
        return sf
    def validate(sf, /):
        settings = sf._settings
        data = sf._data
        args = (settings, data)
        (max_size7physical, imay_max_size7apparent) = sf._settings
        (may_head, history_lnkls, size7physical, size7apparent, curr_size4step, remain_size4last_step) = sf._data
        assert 2 <= max_size7physical
        assert 0 <= size7physical <= max_size7physical
        assert 0 <= size7physical <= size7apparent
        if not -1 == imay_max_size7apparent:
            max_size7apparent = imay_max_size7apparent
            assert 2 <= max_size7physical <= max_size7apparent
            assert 0 <= size7physical <= size7apparent <= max_size7apparent
        assert 1 <= curr_size4step
        assert 1 == curr_size4step.bit_count()
        assert 0 <= remain_size4last_step < curr_size4step
        assert not size7physical <= 2 or size7physical == size7apparent and curr_size4step == 1 and remain_size4last_step == 0
        assert (size7physical-1)*curr_size4step == (-1+size7apparent+remain_size4last_step), (settings, data)
            # ^AssertionError: ((8, 64), (Reproduceable5seq(range(0, 160), 0), mk_rglnkls_([Reproduceable5seq(range(0, 160), 2), Reproduceable5seq(range(0, 160), 4), Reproduceable5seq(range(0, 160), 6), Reproduceable5seq(range(0, 160), 8)]), 5, 9, 2, 1))
            # _oo_append6underfill_
            # fixed_bug4remain_size4last_step:goto
        assert not size7physical == 0 or may_head is None and not history_lnkls
        assert not size7physical >= 1 or size7physical == 1 + len7count_(history_lnkls)
        # [2 <= max_size7physical <= (+oo if -1==imay_max_size7apparent else max_size7apparent)]
        # [0 <= size7physical <= max_size7physical]
        # [0 <= size7apparent <= (+oo if -1==imay_max_size7apparent else max_size7apparent)]
        # [0 <= size7physical <= size7apparent]
        # [log2(curr_size4step)%1 == 0]
        # [curr_size4step >= 1]
        # [0 <= remain_size4last_step < curr_size4step]

        # [[size7physical <= 2] <-> [size7apparent <= 2] -> [size7physical == size7apparent][curr_size4step == 1][remain_size4last_step == 0]]
        # [size7physical >= 2] => [(size7physical-1)*curr_size4step == (-1+size7apparent+remain_size4last_step)]
        # !! ok@[size7physical <= 2]
        # => [(size7physical-1)*curr_size4step == (-1+size7apparent+remain_size4last_step)]
        # => [size7apparent == 1+(size7physical-1)*curr_size4step -remain_size4last_step]
        # [[size7physical == 0] -> [may_head is None][len7count_(history_lnkls) == 0]]
        # [[size7physical >= 1] -> [size7physical == 1+len7count_(history_lnkls)]]
    #end-def validate(sf, /):
    def __repr__(sf, /):
        cls = type(sf)
        args = cls.__getnewargs__(sf)
        return repr_helper(sf, *args)
        if not sf:
            (max_size7physical, imay_max_size7apparent) = sf._settings
            return repr_helper(sf, max_size7physical, imay_max_size7apparent)
        settings = sf._settings
        data = sf._data
        return repr_helper(sf, settings, data)
        (max_size7physical, imay_max_size7apparent) = sf._settings
        (may_head, history_lnkls, size7physical, size7apparent, curr_size4step, remain_size4last_step) = sf._data
        return repr_helper_ex(sf, [max_size7physical, imay_max_size7apparent], 'may_head, history_lnkls, size7physical, size7apparent, curr_size4step, remain_size4last_step'.split(', '), {}, ordered_attrs_only=True, compact6kwargs=True, vars4self=locals())


    @override
    def __eq__(sf, ot, /):
        #if not isinstance(ot, __class__): return NotImplemented
        return type(sf) is type(ot) and sf._settings == ot._settings and sf._data[::-1] == ot._data[::-1]
    @override
    def __hash__(sf, /):
        cls = type(sf)
        settings = sf._settings
        data = sf._data
        return hash((cls, settings, data))
    __eq__
    __hash__
    ['__getnewargs__', '__getstate__', '__setstate__', '_apparent_idx5physical_idx4history_array_', '_oo_append6underfill_', '_physical_idx5apparent_idx6sparse4history_array_', '_view_or_gmk_cached_list4history_array_', 'fmap_', 'head', 'imay_max_size7apparent', 'last', 'oo_clear', 'size7apparent', 'size7physical']
    @override
    def __getnewargs__(sf, /):
        #see:,validate(),__new__()
        #used by:pickle, __repr__()
        settings = sf._settings
        data = sf._data
        #bug:args = settings if sf else (settings, data)
        #old:args = settings if not sf else (settings, data)
        args = settings if not sf else (*settings, '!', data)
        return args
    @override
    def __getstate__(sf, /):
        return None
    @override
    def __setstate__(sf, st4pickle, /):
        raise 000
    @override
    def fmap_(sf, transform4reproduceable, /):
        if not sf:
            return sf
            return sf.copy()
        # [bool(sf)]

        cls = type(sf)
        settings = sf._settings
        data = sf._data

        # !! [bool(sf)]
        (head, history_lnkls, *curr_params) = data
        head = transform4reproduceable(head)
        history_lnkls = fmap7force_(history_lnkls, transform4reproduceable)
        data = (head, history_lnkls, *curr_params)
        #old:ot = cls(settings, data)
        ot = cls(*settings, '!', data)
        return ot

    @property
    #@new_method
    def max_size7physical(sf, /):
        return sf._settings[0]
    @property
    @override
    def imay_max_size7apparent(sf, /):
        return sf._settings[1]
    # (may_head, history_lnkls, size7physical, size7apparent, curr_size4step, remain_size4last_step) = sf._data
    @property
    @override
    def size7physical(sf, /):
        return sf._data[2]
    @property
    @override
    def size7apparent(sf, /):
        return sf._data[3]
    @property
    @override
    def head(sf, /):
        if not sf:raise EmptyError
        return sf._data[0]
    @property
    @override
    def last(sf, /):
        match len(sf):
            case 0:
                raise EmptyError
            case 1:
                return sf._data[0] # head
        history_lnkls = sf._data[1]
        return top6_(history_lnkls)


    @override
    def _oo_append6underfill_(sf, history, /):
        '[not .full] => IHistorySaver7immutable{settings}{len==sz<max_size7apparent} -> history/IReproduceable{record} -> IHistorySaver7immutable{settings}{len==1+sz<=max_size7apparent}'
        # precondition:[size7apparent < max_size7apparent]
        cls = type(sf)
        settings = sf._settings
        data = sf._data
        (max_size7physical, imay_max_size7apparent) = settings
        (may_head, history_lnkls, size7physical, size7apparent, curr_size4step, remain_size4last_step) = data
        max_size7apparent = max_size7physical+size7apparent if -1 == imay_max_size7apparent else imay_max_size7apparent
        # [pseudo:max_size7apparent]
        assert size7apparent < max_size7apparent
        # [size7apparent < max_size7apparent]
        if size7apparent < 2:
            # [size7apparent < 2]
            match size7apparent:
                case 0:
                    may_head = history
                case 1:
                    history_lnkls = oo_push_(history_lnkls, history)
                case _:
                    raise 000
            777; size7physical += 1
            777; size7apparent += 1
            # [size7apparent <= 2]
            # !! [[size7physical <= 2] <-> [size7apparent <= 2] -> [size7physical == size7apparent][curr_size4step == 1][remain_size4last_step == 0]]
            data = (may_head, history_lnkls, size7physical, size7apparent, curr_size4step, remain_size4last_step)
            # [pseudo:max_size7apparent]
            #old:ot = cls(settings, data)
            ot = cls(*settings, '!', data)
            return ot
        # [size7apparent >= 2]
        # !! [[size7physical <= 2] <-> [size7apparent <= 2] -> [size7physical == size7apparent][curr_size4step == 1][remain_size4last_step == 0]]
        # [size7physical >= 2]
        # [2 <= size7apparent < max_size7apparent]


        # [0 <= remain_size4last_step < curr_size4step]
        if not remain_size4last_step == 0:
            # [1 <= remain_size4last_step < curr_size4step]
            # !! [[size7physical <= 2] <-> [size7apparent <= 2] -> [size7physical == size7apparent][curr_size4step == 1][remain_size4last_step == 0]]
            # [size7physical > 2]
            history_lnkls = oo_pop_(history_lnkls)
            777; size7physical -= 1
            # [2 <= size7physical < max_size7physical]
            # [1 <= remain_size4last_step < curr_size4step]
        else:
            # [remain_size4last_step == 0]
            # [size7physical >= 2]
            if not size7physical == max_size7physical:
                # [2 <= size7physical < max_size7physical]
                # [remain_size4last_step == 0]
                pass
            else:
                # [2 <= size7physical == max_size7physical]
                # thinning
                # !! [max_size7physical >= 2]
                # [size7apparent >= size7physical == max_size7physical >= 2]
                # [may_head is head]
                ls = list7up_(history_lnkls)
                # [len(ls) == -1+size7physical >= 1]
                assert ls
                # [len(ls) > 0]
                odd8old_len4ls = len(ls)&1 == 1
                # !! [head not in history_lnkls]
                # => not:del ls[1::2]
                del ls[0::2]
                777;curr_size4step7old = curr_size4step
                777;curr_size4step <<= 1 # ok:[remain_size4last_step == 0]
                if odd8old_len4ls:
                    # [ls{old}[-1] deleted]
                    # fixed_bug4remain_size4last_step:here
                    #   => recommend:[1 == max_size7physical%2]
                    # to maintain:[(size7physical-1)*curr_size4step == (-1+size7apparent+remain_size4last_step)]
                    # [remain_size4last_step == curr_size4step -curr_size4step7old == curr_size4step7old]
                    remain_size4last_step = curr_size4step7old
                    # [1 <= remain_size4last_step < curr_size4step]
                else:
                    # [ls{old}[-1] not deleted]
                    # ok:[remain_size4last_step == 0]
                    pass
                # [0 <= remain_size4last_step < curr_size4step]
                # !! [len(ls{old}) > 0]
                # => [ls{old}[0] deleted]
                # => [len(ls{new}) < len(ls{old})]
                history_lnkls = mk5iter7up_(type(history_lnkls), ls)
                # !! [may_head is head]
                # [size7physical >= 1]
                # !! [[size7physical >= 1] -> [size7physical == 1+len7count_(history_lnkls)]]
                # [size7physical == 1+len7count_(history_lnkls)]
                size7physical = 1+len(ls)
                # [1 <= size7physical]
                # !! [len(ls{new}) < len(ls{old})]
                # [size7physical{new} < size7physical{old} == max_size7physical]
                # [1 <= size7physical < max_size7physical]
            assert 1 <= size7physical < max_size7physical
            # [1 <= size7physical < max_size7physical]
            # [0 <= remain_size4last_step < curr_size4step]
            if remain_size4last_step == 0:
                remain_size4last_step = curr_size4step
                # to maintain:[(size7physical-1)*curr_size4step == (-1+size7apparent+remain_size4last_step)]
                #   !! [size7physical will "+= 1"][size7apparent will "+= 1"][remain_size4last_step will "-= 1"]
                if _debug: assert (size7physical-00000)*curr_size4step == (-1+size7apparent+remain_size4last_step), (settings, data)
            # [1 <= remain_size4last_step <= curr_size4step]
            # [1 <= size7physical < max_size7physical]
        assert 1 <= size7physical < max_size7physical
        assert 1 <= remain_size4last_step <= curr_size4step
        # [1 <= remain_size4last_step <= curr_size4step]
        # [1 <= size7physical < max_size7physical]
        # [2 <= size7apparent < max_size7apparent]
        history_lnkls = oo_push_(history_lnkls, history)
        777; size7physical += 1
        777; size7apparent += 1
        777; remain_size4last_step -= 1
        # [3 <= size7apparent <= max_size7apparent]
        # [2 <= size7physical <= max_size7physical]
        # [0 <= remain_size4last_step < curr_size4step]
        data = (may_head, history_lnkls, size7physical, size7apparent, curr_size4step, remain_size4last_step)
        # [pseudo:max_size7apparent]
        #old:ot = cls(settings, data)
        ot = cls(*settings, '!', data)
        return ot
    @override
    def oo_clear(sf, /):
        settings = sf._settings
        cls = type(sf)
        return cls(*settings)
    @override
    def _view_or_gmk_cached_list4history_array_(sf, /):
        '-> (view [history]|cached [history])'
        d = vars(sf)
        try:
            return d['__ls4h']
        except KeyError:
            pass
        (may_head, history_lnkls) = sf._data[0:2]
        if not sf:
            ls = ()
        else:
            head = may_head
            ls = (head, *list7up_(history_lnkls))
        ls
        d['__ls4h'] = ls
        return sf._view_or_gmk_cached_list4history_array_()

    @override
    def _apparent_idx5physical_idx4history_array_(sf, physical_idx, /):
        'physical_idx/uint%size7physical -> apparent_idx/uint%size7apparent'
        if physical_idx == 0:
            return 0
        data = sf._data
        (may_head, history_lnkls, size7physical, size7apparent, curr_size4step, remain_size4last_step) = data
        if curr_size4step == 1:
            assert size7physical == size7apparent
            apparent_idx = physical_idx
            return apparent_idx
        if physical_idx == -1+size7physical:
            # last_step may be incomplete
            return -1+size7apparent
        # complete steps:
        apparent_idx = physical_idx*curr_size4step
        return apparent_idx
    @override
    def _physical_idx5apparent_idx6sparse4history_array_(sf, apparent_idx6sparse, /):
        'apparent_idx6sparse{from physical_idx}/uint%size7apparent -> physical_idx/uint%size7physical # [apparent_idx6sparse == sf._apparent_idx5physical_idx4history_array_(physical_idx)]'
        if apparent_idx6sparse == 0:
            return 0
        data = sf._data
        (may_head, history_lnkls, size7physical, size7apparent, curr_size4step, remain_size4last_step) = data
        if curr_size4step == 1:
            assert size7physical == size7apparent
            physical_idx = apparent_idx6sparse
            return physical_idx
        if apparent_idx6sparse == -1+size7apparent:
            # last_step may be incomplete
            return -1+size7physical
        # complete steps:
        physical_idx = perfect_div(apparent_idx6sparse, curr_size4step)
        return physical_idx

if 0:SparseHistorySaver7immutable.__new__.__doc__ = '''\
#recommend:[1 == max_size7physical%2]
SparseHistorySaver7immutable(max_size7physical, imay_max_size7apparent)
SparseHistorySaver7immutable(settings, data)
    [settings == (max_size7physical, imay_max_size7apparent)]
    [data == (may_head, history_lnkls, size7physical, size7apparent, curr_size4step, remain_size4last_step)]
'''#'''
SparseHistorySaver7immutable.__new__.__doc__ = '''\
#recommend:[1 == max_size7physical%2]
SparseHistorySaver7immutable(max_size7physical, imay_max_size7apparent, danger_mark='!', data=None)
    [data == (may_head, history_lnkls, size7physical, size7apparent, curr_size4step, remain_size4last_step)]
    [danger_mark === '!']
'''#'''
check_non_ABC(SparseHistorySaver7immutable)

if 0:
    _data0 = ...
def _gmk_data0_():
    global _data0
    try:
        return _data0
    except NameError:
        pass
    may_head = None
    history_lnkls = mk_rglnkls_()
    size7physical = 0
    size7apparent = 0
    curr_size4step = 1
    remain_size4last_step = 0
    _data0 = (may_head, history_lnkls, size7physical, size7apparent, curr_size4step, remain_size4last_step)
    return _gmk_data0_()
    return _data0






__all__
r'''[[[
print_methods7py:here
===
print_methods7py seed.types.HistorySaver IHistorySaverBase

print_methods7py seed.types.HistorySaver IHistorySaver7mutable
print_methods7py seed.types.HistorySaver SparseHistorySaver

print_methods7py seed.types.HistorySaver IHistorySaver7immutable
print_methods7py seed.types.HistorySaver SparseHistorySaver7immutable


===
===
===
print_methods7py seed.types.HistorySaver IHistorySaverBase

new_abstract_methods:
    `copy
    `mk_empty_
    `mk_solo_
    `__getnewargs__
    `__getstate__
    `__setstate__
    `fmap_
    `imay_max_size7apparent
    `size7physical
    `size7apparent
    `head
    `last
    `_search7sparse_
new_concrete_methods:
    __len__
    full
    search7sparse_
    search7dense_
    search_key_points_
    backward_search_key_points_
    forward_search_key_points_



===
===
print_methods7py seed.types.HistorySaver IHistorySaver7mutable

new_abstract_methods:
    `_append6underfill_
    `clear

new_concrete_methods:
    mk_solo_
    extend
    append
    fills_
    fills7unlimit_
    both_fills7unlimit_
    clear_but_last_

===
print_methods7py seed.types.HistorySaver SparseHistorySaver

new_abstract_methods:

new_concrete_methods:
    ___no_slots_ok___
    __new__
    clear
    validate
    mk_empty_
    copy
    __repr__
    __getnewargs__
    __getstate__
    __setstate__
    fmap_
    imay_max_size7apparent
    size7physical
    size7apparent
    _append6underfill_
    _history_array_view_
    _apparent_idx5physical_idx4history_array_
    _physical_idx5apparent_idx6sparse4history_array_
    validate7apparent_idx




===
===
print_methods7py seed.types.HistorySaver IHistorySaver7immutable

new_abstract_methods:
    `__hash__
    `__eq__
    `_oo_append6underfill_
    `oo_clear

new_concrete_methods:
    copy
    mk_empty_
    mk_solo_
    __ne__
    oo_extend
    oo_append
    oo_append
    oo_fills_
    oo_fills7unlimit_
    ii_both_fills7unlimit_
    oo_clear_but_last_

===
print_methods7py seed.types.HistorySaver SparseHistorySaver7immutable

new_abstract_methods:

new_concrete_methods:
    ___no_slots_ok___
    __new__
    validate
    __repr__
    __eq__
    __hash__
    __getnewargs__
    __getstate__
    __setstate__
    fmap_
    max_size7physical
    imay_max_size7apparent
    size7physical
    size7apparent
    head
    last
    _oo_append6underfill_
    oo_clear
    _view_or_gmk_cached_list4history_array_
    _apparent_idx5physical_idx4history_array_
    _physical_idx5apparent_idx6sparse4history_array_

===

#]]]'''#'''




__all__
#print_methods7py:goto
from seed.types.HistorySaver import EmptyError, FullError
from seed.types.HistorySaver import IHistorySaver, IHistorySaver__bisect7single_array_view
from seed.types.HistorySaver import DenseHistorySaver, SparseHistorySaver, mk_history_saver_
from seed.types.HistorySaver import SparseHistorySaver7immutable
#
#def mk_history_saver_(max_size7dense, max_size7physical, cost_per_detect, imay_detect_period, /):
#
#DenseHistorySaver(max_size7apparent, danger_mark='!', may_history_array=None, /, *, no_copy=False)
#   [danger_mark === '!']
#
#SparseHistorySaver(max_size7dense, max_size7physical, imay_max_size7apparent, danger_mark='!', payload=None, /, *, no_copy=False)
#   recommend:[1 == max_size7physical%2]
#   [payload :: may (history_array, size7apparent, curr_max_size7physical, curr_step, last_step)]
#   [danger_mark === '!']
#
#SparseHistorySaver7immutable(max_size7physical, imay_max_size7apparent, danger_mark='!', data=None)
#   [data == (may_head, history_lnkls, size7physical, size7apparent, curr_size4step, remain_size4last_step)]
#   [danger_mark === '!']
#

from seed.types.HistorySaver import *
