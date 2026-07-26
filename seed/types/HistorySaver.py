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
>>>
>>> from seed.math.sign_of import sign_of
>>> def mk_history2rank_(j, /):
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
>>> saver.search7dense_(mk_history2rank_(5), zero6sparse_ok=True, validate6recursive=True)
(0, (1, Reproduceable5seq('0123456789', 4), -1), (2, Reproduceable5seq('0123456789', 5), 0))

(0, Reproduceable5seq('0123456789', 4), Reproduceable5seq('0123456789', 5))

>>> saver.search7sparse_(mk_history2rank_(2))
(3, None, (0, Reproduceable5seq('0123456789', 3), 1))

(3, None, Reproduceable5seq('0123456789', 3))
>>> saver.search7sparse_(mk_history2rank_(3))
(1, None, (0, Reproduceable5seq('0123456789', 3), 0))

(1, None, Reproduceable5seq('0123456789', 3))
>>> saver.search7sparse_(mk_history2rank_(5))
(0, (1, Reproduceable5seq('0123456789', 4), -1), (2, Reproduceable5seq('0123456789', 5), 0))

(0, Reproduceable5seq('0123456789', 4), Reproduceable5seq('0123456789', 5))
>>> saver.search7sparse_(mk_history2rank_(6))
(0, (2, Reproduceable5seq('0123456789', 5), -1), (3, Reproduceable5seq('0123456789', 6), 0))

(0, Reproduceable5seq('0123456789', 5), Reproduceable5seq('0123456789', 6))
>>> saver.search7sparse_(mk_history2rank_(7))
(4, (3, Reproduceable5seq('0123456789', 6), -1), None)

(4, Reproduceable5seq('0123456789', 6), None)

>>> saver.search7sparse_(mk_history2rank_(5.5))
(2, (2, Reproduceable5seq('0123456789', 5), -1), (3, Reproduceable5seq('0123456789', 6), 1))

(2, Reproduceable5seq('0123456789', 5), Reproduceable5seq('0123456789', 6))

>>> saver.search7dense_(mk_history2rank_(2), validate6recursive=True)
(3, None, (0, Reproduceable5seq('0123456789', 3), 1))

(3, None, Reproduceable5seq('0123456789', 3))
>>> saver.search7dense_(mk_history2rank_(3), validate6recursive=True)
(1, None, (0, Reproduceable5seq('0123456789', 3), 0))

(1, None, Reproduceable5seq('0123456789', 3))
>>> saver.search7dense_(mk_history2rank_(5), validate6recursive=True)
(0, (1, Reproduceable5seq('0123456789', 4), -1), (2, Reproduceable5seq('0123456789', 5), 0))

(0, Reproduceable5seq('0123456789', 4), Reproduceable5seq('0123456789', 5))
>>> saver.search7dense_(mk_history2rank_(6), validate6recursive=True)
(0, (2, Reproduceable5seq('0123456789', 5), -1), (3, Reproduceable5seq('0123456789', 6), 0))

(0, Reproduceable5seq('0123456789', 5), Reproduceable5seq('0123456789', 6))
>>> saver.search7dense_(mk_history2rank_(7), validate6recursive=True)
(4, (3, Reproduceable5seq('0123456789', 6), -1), None)

(4, Reproduceable5seq('0123456789', 6), None)

>>> saver.search7dense_(mk_history2rank_(5.5), validate6recursive=True)
(2, (2, Reproduceable5seq('0123456789', 5), -1), (3, Reproduceable5seq('0123456789', 6), 1))

(2, Reproduceable5seq('0123456789', 5), Reproduceable5seq('0123456789', 6))

>>> saver.clear()
>>> saver.search7sparse_(mk_history2rank_(5.5))
(5, None, None)
>>> saver.search7dense_(mk_history2rank_(5.5), validate6recursive=True)
(5, None, None)





>>> import seed.abc.IReproduceable
>>> seed.abc.IReproduceable._debug = True

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

>>> saver.search7dense_(mk_history2rank_(5.5), validate6recursive=True)
(2, (5, Reproduceable5seq('0123456789', 5), -1), (6, Reproduceable5seq('0123456789', 6), 1))

(2, Reproduceable5seq('0123456789', 5), Reproduceable5seq('0123456789', 6))
>>> saver.search7sparse_(mk_history2rank_(5.5))
(2, (0, Reproduceable5seq('0123456789', 0), -1), (8, Reproduceable5seq('0123456789', 8), 1))

(2, Reproduceable5seq('0123456789', 0), Reproduceable5seq('0123456789', 8))

>>> saver.search7dense_(mk_history2rank_(5), zero6sparse_ok=True, validate6recursive=True)
(0, (4, Reproduceable5seq('0123456789', 4), -1), (5, Reproduceable5seq('0123456789', 5), 0))

(0, Reproduceable5seq('0123456789', 4), Reproduceable5seq('0123456789', 5))
>>> saver.search7dense_(mk_history2rank_(8), zero6sparse_ok=True, validate6recursive=True)
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

>>> saver.search7dense_(mk_history2rank_(5.5), validate6recursive=True)
(2, (5, Reproduceable5seq('0123456789', 5), -1), (6, Reproduceable5seq('0123456789', 6), 1))

(2, Reproduceable5seq('0123456789', 5), Reproduceable5seq('0123456789', 6))
>>> saver.search7sparse_(mk_history2rank_(5.5))
(2, (4, Reproduceable5seq('0123456789', 4), -1), (8, Reproduceable5seq('0123456789', 8), 1))

(2, Reproduceable5seq('0123456789', 4), Reproduceable5seq('0123456789', 8))

>>> saver.search7dense_(mk_history2rank_(5), zero6sparse_ok=True, validate6recursive=True)
(0, (4, Reproduceable5seq('0123456789', 4), -1), (5, Reproduceable5seq('0123456789', 5), 0))

(0, Reproduceable5seq('0123456789', 4), Reproduceable5seq('0123456789', 5))
>>> saver.search7dense_(mk_history2rank_(8), zero6sparse_ok=True, validate6recursive=True)
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









>>> seed.abc.IReproduceable._debug = False









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
    from seed.tiny_.check import check_type_le, check_int_ge, check_int_ge_le, check_uint_lt
    from bisect import bisect_right
    from functools import cache
    from itertools import islice
    from seed.abc.IReproduceable import IReproduceable, Reproduceable5seq
    from seed.abc.IReproduceable import iter_pairs4reproduceable_, iter_fsts4reproduceable_, iter_snds4reproduceable_
    from seed.helper.repr_input import repr_helper, repr_helper_ex
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

class FullError(Exception):pass
class EmptyError(Exception):pass
#稀疏快照纟可重演序列
class IHistorySaver(ABC):
    '[history :: IReproduceable{record}]'
    __slots__ = ()
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
    def _search7sparse_(sf, history2rank_, /):
        '(history -> (-1|0|+1)) -> (uint%6, i, j, may (i,history[i],-1), may (j,history[j],(0|+1)))/((0, i:history:-1, j:history:0)|(1, None, j:history:0)|(2, i:history:-1, j:history:+1)|(3, None, j:history:+1)|(4, i:history:-1, None)|(5, None, None)) # [0 <= i < j < sf.size7apparent]'
    def search7sparse_(sf, history2rank_, /, *, offset=0):
        '(history -> (-1|0|+1)) -> (uint%6, i, j, may (i,history[i],-1), may (j,history[j],(0|+1)))/((0, i:history:-1, j:history:0)|(1, None, j:history:0)|(2, i:history:-1, j:history:+1)|(3, None, j:history:+1)|(4, i:history:-1, None)|(5, None, None)) # [offset+0 <= i < j < offset+sf.size7apparent]'
        #old:'(history -> (-1|0|+1)) -> (uint%6, may history, may history)/((0, history/-1, history/0)|(1, None, history/0)|(2, history/-1, history/+1)|(3, None, history/+1)|(4, history/-1, None)|(5, None, None))'
        r = sf._search7sparse_(history2rank_)
        if not (offset == 0 or not any(r[1:])):
            r = (r[0], *(((offset+m[0], *m[1:]) if not None is m else m) for m in r[1:]))
        return r
    def search7dense_(sf, history2rank_, /, *, zero6sparse_ok=False, recursive=True, validate6recursive=False, offset=0):
        '(history -> (-1|0|+1)) -> (uint%6, i, j, may (i,history[i],-1), may (j,history[j],(0|+1)))/((0, i:history:-1, j:history:0)|(1, None, j:history:0)|(2, i:history:-1, j:history:+1)|(3, None, j:history:+1)|(4, i:history:-1, None)|(5, None, None)) # [offset+0 <= i < j < offset+sf.size7apparent] # [not zero6sparse_ok => [i+1==j]]'
        #old:'(history -> (-1|0|+1)) -> (uint%6, may history, may history)/((0, history/-1, history/0)|(1, None, history/0)|(2, history/-1, history/+1)|(3, None, history/+1)|(4, history/-1, None)|(5, None, None))'
        r = sf.search7sparse_(history2rank_, offset=offset)
        match r:
            case ((0|2) as k, (i, history7neg_one, _neg_one), (j, history7zero_or_one, _zero_or_one)):
                assert _neg_one == -1
                assert _zero_or_one in (0,+1)
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
                    ot = SparseHistorySaver(2049, 65537, -1)
                    ot.append(history7neg_one)
                    ot.fills_(sz-1)
                    new_r = ot.search7dense_(history2rank_, zero6sparse_ok=zero6sparse_ok, recursive=recursive, offset=i)
                    _k = new_r[0]
                    if not (_k == 0 or _k == k):raise 000
                    if validate6recursive:
                        new_r7non_recursive = sf.search7dense_(history2rank_, zero6sparse_ok=zero6sparse_ok, recursive=not recursive, validate6recursive=not validate6recursive, offset=offset)
                        _check_result5search7dense_(zero6sparse_ok, new_r, new_r7non_recursive)
                else:
                    # not recursive
                    new_r = _search7dense6non_recursive_(history2rank_, history7neg_one, sz, i, j, _zero_or_one, k)
                new_r
            case _:
                new_r = r
        return new_r

    def __len__(sf, /):
        '-> size7apparent'
        return sf.size7apparent
    @property
    def full(sf, /):
        '-> bool'
        return sf.size7apparent == sf.imay_max_size7apparent
    def append(sf, history, /):
        'history/IReproduceable{record} -> None|^FullError'
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
    def clear_but_last_(sf, /):
        '-> None'
        if sf:
            last = sf.last
            sf.clear()
            sf.append(last)

def _check_result5search7dense_(zero6sparse_ok, new_r7recursive, new_r7non_recursive, /):
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
    def apparent_idx5physical_idx4history_array_(sf, physical_idx, /):
        'physical_idx/uint%size7physical -> apparent_idx/uint%size7apparent'
        check_uint_lt(sf.size7physical, physical_idx)
        apparent_idx = sf._apparent_idx5physical_idx4history_array_(physical_idx)
        check_uint_lt(sf.size7apparent, apparent_idx)
        #assert 0 <= physical_idx <= apparent_idx < sf.size7apparent
        return apparent_idx
    @override
    def _search7sparse_(sf, history2rank_, /):
        ls = sf._history_array_view_
        j2rank_ = _mk_j2rank_(history2rank_, ls)
        L = len(ls)
        js = range(L)
        j = bisect_right(js, -1, key=j2rank_)
        check_uint_lt(1+L, j)
        if j == L:
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
    def _apparent_idx5physical_idx4history_array_(sf, physical_idx, /):
        apparent_idx = physical_idx
        return apparent_idx


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
    def _apparent_idx5physical_idx4history_array_(sf, physical_idx, /):
        curr_step = sf._step
        last_step = sf._cn
        #bug:apparent_idx = 0 if 0 == physical_idx else last_step + curr_step*(-1+physical_idx)
        apparent_idx = curr_step*physical_idx if not sf.size7physical == 1+physical_idx else last_step + curr_step*(-1+physical_idx)
        #assert 0 <= physical_idx <= apparent_idx < sf.size7apparent
        return apparent_idx
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
