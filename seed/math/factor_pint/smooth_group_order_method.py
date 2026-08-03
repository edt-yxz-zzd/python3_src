#__all__:goto
r'''[[[
e ../../python3_src/seed/math/factor_pint/smooth_group_order_method.py

seed.math.factor_pint.smooth_group_order_method
py -m nn_ns.app.debug_cmd   seed.math.factor_pint.smooth_group_order_method -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.factor_pint.smooth_group_order_method:__doc__ -ht # -ff -df
#######

[[
move_from:
e ../../python3_src/seed/math/factor_pint/factor_pint__smooth_group_order_method.py
]]


'#'; __doc__ = r'#'
>>> raw_search_the_last_used_prime_6stage2_6smooth_group_order_method_(7, 11, 1)
11
>>> raw_search_the_last_used_prime_6stage2_6smooth_group_order_method_(7, 17, 1)
11
>>> raw_search_the_last_used_prime_6stage2_6smooth_group_order_method_(7, 17, 2)
13
>>> raw_search_the_last_used_prime_6stage2_6smooth_group_order_method_(7, 17, 3)
17
>>> raw_search_the_last_used_prime_6stage2_6smooth_group_order_method_(7, 17, 4)
Traceback (most recent call last):
    ...
ValueError: (7, 17, 4)












    def search6stage1_(sf, to_search_exps8factors4order6found, detect_period, max4exp6stage1, may_reproduceable4exps6stage1, pt0, /):
    def search6stage2__7detect_per_step_(sf, max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage2, pt7final6stage1, /):
    def search6stage2__7ring_(sf, detect_period, max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage2, pt7final6stage1, /):
    def search6stage12__7ring_(sf, to_search_exps8factors4order6found, detect_period, max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage1, may_reproduceable4exps6stage2, pt0, /):
>>> from seed.types.Reproduceable import Reproduceable5seq
>>> M = 5*43
>>> ops = Ops6stage12_4smooth_group_order_method7ring__7uint_mod(M)
>>> ops
Ops6stage12_4smooth_group_order_method7ring__7uint_mod(215)
>>> #default_search6stage1_(ops, True, 1, 7, Reproduceable5seq([2,3,5,7], 0), 3, _verbose=True)
>>> ops.search6stage1_(False, 1, 7, Reproduceable5seq([2,3,5,7], 0), 3)
(0, (0, 54, 7), (1, 44), None)
>>> ops.search6stage1_(True, 1, 7, Reproduceable5seq([2,3,5,7], 0), 3)
(0, (3, 54, 7), (4, 44), ((2, 3, 7), (0, 44)))

>>> ops.search6stage1_(False, 1, 7, Reproduceable5seq([2,2], 0), 3)
(0, (0, 9, 2), (1, 81), None)
>>> ops.search6stage1_(True, 1, 7, Reproduceable5seq([2,2], 0), 3)
(0, (1, 9, 2), (2, 81), ((2, 2), (0, 81)))








>>> [-1+2**67 == 193707721*761838257287]
[True]
>>> [-1+193707721 == 2**3 * 3**3 *5 *67 *2677]
[True]
>>> M67 = (-1+2**67)
>>> ops = Ops6stage12_4smooth_group_order_method7ring__7uint_mod(M67)
>>> ops
Ops6stage12_4smooth_group_order_method7ring__7uint_mod(147573952589676412927)
>>> ops.search6stage1_(True, 1, 7, Reproduceable5seq([2,2,2,3,3,3,5,67,2677], 0), 5)
(0, (8, 40340592636112533364, 2677), (9, 75891667378750673489), ((3, 3, 5, 67, 2677), (0, 22318898449504561380)))
>>> pow(5, II((3, 3, 5, 67, 2677)), M67)
22318898449504561380
>>> gcd(M67, -1+22318898449504561380)
193707721
>>> gcd(M67, -1+75891667378750673489)
193707721
>>> gcd(M67, -1+74226990646063851499)
193707721



>>> rp8exps6stage1 = mk_Reproduceable7dup_xprimes__ver2_(67, 67, case=2)
>>> rp8exps6stage2 = mk_Reproduceable7xprimes_(2677, min4xprime=1+67, case=2)
>>> ops.search6stage12__7ring_(False, 128, 67, 2677, rp8exps6stage1, rp8exps6stage2, 5)
(203, 0, 74226990646063851499, 2677)
>>> ops.search6stage12__7ring_(True, 128, 67, 2677, rp8exps6stage1, rp8exps6stage2, 5) # [ver==(0|1)]
(207, 0, 74226990646063851499, ((3, 3, 5, 67, 2677), (0, 22318898449504561380)))




>>> rp8exps6stage1 = mk_Reproduceable7dup_xprimes__ver2_(66, 66, case=2)
>>> rp8exps6stage2 = mk_Reproduceable7xprimes_(2677, min4xprime=1+67, case=2)
>>> ops.search6stage12__7ring_(True, 128, 66, 2677, rp8exps6stage1, rp8exps6stage2, 5)
(202, -1, (-1, (27, 23909194385231561362)), (-1, (2677, 369, 54861179224756581747)))

>>> rp8exps6stage1 = mk_Reproduceable7dup_xprimes__ver2_(2677, 2677, case=2)
>>> rp8exps6stage2 = Reproduceable5seq([], 0)
>>> ops.search6stage12__7ring_(False, 128, 2677, 2677, rp8exps6stage1, rp8exps6stage2, 5)
(103, 0, 8424091205966200624, 2677)
>>> ops.search6stage12__7ring_(True, 128, 2677, 2677, rp8exps6stage1, rp8exps6stage2, 5)
(107, 0, 8424091205966200624, ((3, 3, 5, 67, 2677), (0, 22318898449504561380)))

>>> rp8exps6stage1 = Reproduceable5seq([], 0)
>>> rp8exps6stage2 = Reproduceable5seq([], 0)
>>> ops.search6stage12__7ring_(False, 128, 1, 1, rp8exps6stage1, rp8exps6stage2, 193707721)
(202, -1, (-1, (0, 193707721)), (-1, (1, 0, 193707721)))
>>> ops.search6stage12__7ring_(False, 128, 1, 1, rp8exps6stage1, rp8exps6stage2, 1+193707721)
(101, 0, 193707722, None)




>>> M = 29*43
>>> M
1247
>>> pow(3,4*3,1247)
219
>>> pow(219,7,1247)
1
>>> pt0 = 3
>>> ops = Ops6stage12_4smooth_group_order_method7ring__7uint_mod(M)

>>> rp8exps6stage1 = Reproduceable5seq([2,2,3,7], 0)
>>> rp8exps6stage2 = Reproduceable5seq([], 0)
>>> ops.search6stage12__7ring_(False, 999, 7, 7, rp8exps6stage1, rp8exps6stage2, pt0)
(103, 1, 1, 7)
>>> ops.search6stage12__7ring_(True, 999, 7, 7, rp8exps6stage1, rp8exps6stage2, pt0) #old output:(107, 1, 1, (2, 2, 7)) # ==>>:patch0001
(107, 1, 1, ((2, 2, 7), (0, 436)))
>>> pow(pt0, II((2, 2, 7)), M)
436


>>> rp8exps6stage1 = Reproduceable5seq([2,2,3], 0)
>>> rp8exps6stage2 = Reproduceable5seq([7], 0)
>>> ops.search6stage12__7ring_(False, 999, 7, 7, rp8exps6stage1, rp8exps6stage2, pt0)
(203, 1, 1, 7)
>>> ops.search6stage12__7ring_(True, 999, 7, 7, rp8exps6stage1, rp8exps6stage2, pt0)
(207, 1, 1, ((2, 2, 7), (0, 436)))

[ver==0]:
(207, 0, 436, ((2, 2, 7), (0, 436)))




















py_adhoc_call   seed.math.factor_pint.smooth_group_order_method   @f

]]]'''#'''
__all__ = r'''

ICommonOps4smooth_group_order_method
    IOps6stage1_4smooth_group_order_method
        default_search6stage1_
    IOps6stage2_4smooth_group_order_method
        default_search6stage2__7detect_per_step_
        IOps6stage2_4smooth_group_order_method7ring
            default_search6stage2__7ring_

    IOps6stage12_4smooth_group_order_method
        default_search6stage12_
    IOps6stage12_4smooth_group_order_method7ring
        default_search6stage12__7ring_



ICommonOps4smooth_group_order_method__7default_mixin
    IOps6stage1_4smooth_group_order_method__7default_mixin
        IOps6stage12_4smooth_group_order_method__7default_mixin
            IOps6stage12_4smooth_group_order_method7ring__7default_mixin
                IOps6stage12_4smooth_group_order_method7ring__7uint_mod
                    Ops6stage12_4smooth_group_order_method7ring__7uint_mod




smooth_group_order_method_
    search_the_last_used_prime_6stage2_6smooth_group_order_method_
        raw_search_the_last_used_prime_6stage2_6smooth_group_order_method_





mk_square5may_
mk_pow5may_
CachedPow
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.floor_ceil_tools.fc_log import floor_log2
    from seed.tiny_.check import check_type_le, check_type_is, check_int_ge, check_callable, check_may_, check_ABC
    from seed.tiny_.funcs import echo

    from seed.types.Reproduceable import Reproduceable7foldl, Reproduceable7rdiff, Reproduceable7tmay_prev_oresult, Reproduceable7fmap
    from seed.types.HistorySaver import mk_history_saver_
    from seed.math.primality_test.reproduceable7probable_primes import mk_Reproduceable7xprimes_
    from seed.math.primality_test.reproduceable7probable_primes import mk_Reproduceable7dup_xprimes__ver2_
    #def mk_Reproduceable7dup_xprimes__ver2_(max4xprime, max4xprime_power, /, *, case=None, mid_args=()):
    from seed.types.Reproduceable import iter_pairs4reproduceable_, iter_fsts4reproduceable_, iter_snds4reproduceable_
    from seed.math.prime_sieve.primes_ge_lt import iter_primes__ge_lt_# iter_filter4primes_ge_lt_, list_primes__ge_lt_
    from itertools import islice


    from seed.math.II import II
    from seed.data_funcs.lnkls import get_empty_lflnkls, lflnkls_ipush_left, lflnkls2iterable
    from seed.types.Reproduceable import StatedTransformOps7fork, StatedTransformOps7flow, StatedTransformOps7rdiff, StatedTransformOps7foldl, StatedTransformOps7fmap, get_ops4transform7stated7echo_
    from seed.types.Reproduceable import Reproduceable7transform_via_ops
    from seed.types.Reproduceable import IReproduceable
    from seed.math.power.power_ import power_, std_exp_
    #def power_(mul_, may_inv_, may_eq_zero_, eq_one_, one, imay_group_order, e, x0, /):
    from math import gcd
    from seed.helper.repr_input import repr_helper
    from seed.debug.print_err import print_err
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

def _show(d, nm, /):
    #_debug7list_all
    v = d[nm]
    print(nm, list(iter_fsts4reproduceable_(v)), sep=':')
    print(nm, v, sep='=')

def mk_square5may_(mul_, may_square_, /):
    if may_square_ is None:
        def square_(pt, /):
            return mul_(pt, pt)
    else:
        square_ = may_square_
        check_callable(square_)
    return square_
def mk_pow5may_(mul_, may_square_, may_pow_, one, /):
    if may_pow_ is None:
        sq_ = mk_square5may_(mul_, may_square_)
        def pow_(pt, e, /):
            pw = one
            for b in map(int, f'{e:b}'):
                pw = sq_(pw)
                if b:
                    pw = mul_(pt, pw)
            return pw
    else:
        pow_ = may_pow_
        check_callable(pow_)
    return pow_

class CachedPow:
    'cached_pow_'
    def __init__(sf, mul_, square_, pow_, one, pt, max4exp7cached, /):
        sf.one = one
        sf.mul_ = mul_
        sf.square_ = square_
        sf.pow_ = pow_
        max_sz = max(5,1+max4exp7cached)
        len_window = floor_log2(max_sz)
        max_sz = max(max_sz, 1+(1<<len_window))
        sf._max_sz = max_sz
        sf._w = len_window
        sf._e2pw4pt = [one, pt]
            # [pt**e | [e:<-[0..<max_sz]]]
        #sf._e2pw4radix = [one]
            # [(pt**2**len_window)**e | [e:<-[0..]]]
        sf._lb_e2pw4pt = [pt]
            # [pt**2**lb_e | [lb_e:<-[0..]]]
    def __getitem__(sf, e, /):
        assert e >= 0
        max_sz = sf._max_sz
        if e < max_sz:
            return sf._getitem5low_exp_(e)
        len_window = sf._w
        s = f'{e:b}'
        L = len(s)
        assert L > len_window
        mul_ = sf.mul_
        MSB = sf._getitem5lb_exp_(L-1) #force filling
        777;get_ = sf._lb_e2pw4pt.__getitem__
        bits = list(map(int, reversed(s)))
        _s_ = s[L-len_window:]
        assert len(_s_) == len_window
        #bug:_e_ = int(_s_)
        _e_ = int(_s_, 2)
        pw = sf._getitem5low_exp_(_e_)
        for lb_e, bit in enumerate(bits[len_window:], len_window):
            if bit:
                pw = mul_(pw, get_(lb_e))
        return pw
        r'''[[[
        mul_ = sf.mul_
        pow_ = sf.pow_
        e4radix = 1<<len_window
        radix = sf._getitem5low_exp_(e4radix) #force filling low block
        777;get4pt_ = sf._e2pw4pt.__getitem__
        (q, r) = divmod(L, len_window)
        if r == 0:
            r = len_window
            q -= 1
        assert q > 0
        i = 0
        pw = one = get4pt_(0)
        for j in range(r, 1+L, len_window):
            _s_ = s[i:j]
            _e_ = int(_s_, 2)
            _pw4pt_ = get4pt_(_e_)
            pw = mul_(pow_(pw, e4radix), _pw4pt_)
            i = j
        assert i == j == L
        return pw
        #]]]'''#'''

    def _fill(sf, e, /):
        e2pw4pt = sf._e2pw4pt
        assert len(e2pw4pt) <= e < sf._max_sz, (len(e2pw4pt), e, sf._max_sz)
        mul_ = sf.mul_
        pt = e2pw4pt[1]
        for _ in range(1+e-len(e2pw4pt)):
            e2pw4pt.append(mul_(pt, e2pw4pt[-1]))
    def _fill2(sf, lb_e, /):
        lb_e2pw4pt = sf._lb_e2pw4pt
        assert len(lb_e2pw4pt) <= lb_e
        square_ = sf.square_
        for _ in range(1+lb_e-len(lb_e2pw4pt)):
            lb_e2pw4pt.append(square_(lb_e2pw4pt[-1]))

    def _getitem5low_exp_(sf, e, /):
        e2pw4pt = sf._e2pw4pt
        if not e < len(e2pw4pt):
            sf._fill(e)
        return e2pw4pt[e]
    def _getitem5lb_exp_(sf, lb_e, /):
        lb_e2pw4pt = sf._lb_e2pw4pt
        if not lb_e < len(lb_e2pw4pt):
            sf._fill2(lb_e)
        return lb_e2pw4pt[lb_e]


r'''[[[
view ../../python3_src/seed/math/prime_gens.py.note.txt
e ../../python3_src/seed/math/primality_test/reproduceable7probable_primes.py
    from seed.helper.Echo import theEcho

include_fst=False
    vs:chain(outs, ...)
st_0 -> (st_j->IN_j->(OUT_j,st_jpp)) -> IReproduceable{IN} -> IReproduceable{OUT}
    * [y_0mm:=st_0][y_jmm:=st_j][y_j:=IN_j][OUT_j:=dy_j{y_j-y_jmm}][st_jpp:=y_j]
    * [x_0mm:=st_0][x_jmm:=st_j][y_j:=IN_j][OUT_j:=x_j][st_jpp:=x_j]
y_0mm -> (y_jmm->y_j->dy_j) -> IReproduceable{y} -> IReproduceable{dy}
x_0mm -> (x_jmm->y_j->x_j) -> IReproduceable{y} -> IReproduceable{x}
    f(x,y):=pow_(x,y)
        # @stage1
    g(x,y):=mul_(x,cached_pow_(x_0mm,y))
        # @stage2
sparse_vs_dense -> history2rank_ -> nonempty-IHistorySaver{IReproduceable{x}} -> (kind, may prev/(-1),may curr/(0|+1))
    prev,curr::IReproduceable{x} #{(kind, last/-1, None) | (kind, may_prev/(-1),curr/(0|+1))}
from seed.math.prime_sieve.PrimeList import PrimeList7ge_lt
PrimeList7ge_lt+Reproduceable5seq



class FullError(Exception):pass
class NonFullError(Exception):pass
class IHistorySaver(ABC):
    @property
    @abstractmethod
    def full(sf, /):
        '-> bool'
    @property
    @abstractmethod
    def append(sf, x, /):
        'x -> None|^FullError'
    @property
    @abstractmethod
    def clear(sf, /):
        '-> None'
    @property
    @abstractmethod
    def size7physical(sf, x, /):
        '-> uint'
    @property
    @abstractmethod
    def size7apparent(sf, x, /):
        '-> uint # [size7discard+size7physical == size7apparent]'
    @property
    @abstractmethod
    def __len__(sf, x, /):
        '-> size7apparent'
    @property
    @abstractmethod
    def bisect(sf, /):
        '-> None'


class State4exps6stage1:
    '((B1, p, max4ep), ep)'
    def reproduce(sf, /):
        '-> Iter (st4exp, prime)'
class State4pow4pt6stage1:
    '(pt0, State4exps6stage1, pt)'
    def reproduce(sf, /):
        '-> Iter (st4pow, pt)'
class StateTracer6stage1:
    '(offset, IHistorySaver(State4pow4pt6stage1))'

#]]]'''#'''


#################################
# ver1:functional
#################################
__all__
def search_the_last_used_prime_6stage2_6smooth_group_order_method_(bound4stage1, bound4pow4stage1, bound4stage2, offset1, offset2, /):
    return raw_search_the_last_used_prime_6stage2_6smooth_group_order_method_(bound4stage1, bound4stage2, offset2-offset1)
def raw_search_the_last_used_prime_6stage2_6smooth_group_order_method_(bound4stage1, bound4stage2, delta4offset, /):
    check_int_ge(1, bound4stage1)
    check_int_ge(1, delta4offset)
    ps = iter_primes__ge_lt_(1+bound4stage1, 1+bound4stage2)
    sz = 0
    for sz, p in enumerate(islice(ps, 0, delta4offset), 1):pass
    if sz == 0:raise ValueError(bound4stage1, bound4stage2)
    if sz < delta4offset:raise ValueError(bound4stage1, bound4stage2, delta4offset)
    if not sz == delta4offset:raise 000
    return p

def smooth_group_order_method_(bound4stage1, bound4pow4stage1, bound4stage2, diff_one_, detect_, mul_, may_square_, may_pow_, one, pt0, /, *, num_muls_per_detect, imay_detect_period=0, case4xprimes=None, max_size7dense=2049, max_size7physical=65537, _debug7list_all=False):
    #smooth_group_order_method_.__doc__:goto

    #imay_num_steps4detect --> imay_detect_period
    #max_size7dense = 2
    check_int_ge(2, max_size7dense)
    check_int_ge(max_size7dense, max_size7physical)
    check_int_ge(1, num_muls_per_detect)
    check_int_ge(-1, imay_detect_period)

    check_int_ge(1, bound4stage1)
    check_int_ge(1, bound4pow4stage1)
    check_int_ge(1, bound4stage2)
    check_callable(diff_one_)
    check_callable(detect_)
    check_callable(mul_)
    check_may_(check_callable, may_square_)
    check_may_(check_callable, may_pow_)
    ###############
    B1a = B1 = bound4stage1
    B1b = bound4pow4stage1
    B2 = bound4stage2
    B2 = max(B1, B2)
    B1b = max(B1a, B1b)
    square_ = mk_square5may_(mul_, may_square_)
    pow_ = mk_pow5may_(mul_, square_, may_pow_, one)
    ###############
    ###############
    ###############
    #stage1:
    ###############
    ###############
    max4xprime = B1a
    max4xprime_power = B1b
    as_dup_ps = mk_Reproduceable7dup_xprimes__ver2_(B1a, B1b, case=case4xprimes)
    ###############
    _as_pts6stage1 = Reproduceable7foldl(pow_, pt0, as_dup_ps)
    #as_pts6stage1 = Reproduceable7chain5iterable([Reproduceable5seq([pt0]), _as_pts6stage1])
    as_pts6stage1 = Reproduceable7tmay_prev_oresult((pt0,), _as_pts6stage1)
    ###############
    if _debug7list_all:
        _show(locals(), 'as_dup_ps')
        _show(locals(), 'as_pts6stage1')

    ###############
    offset0 = 0
    r1 = _search(max_size7dense, max_size7physical, num_muls_per_detect, imay_detect_period, diff_one_, detect_, offset0, pt0, 'stage1', as_pts6stage1)
    match r1:
        case (b_stop, (ok, may_output, (offset1, pt1), extra1)):
            _result1 = (may_output, (((offset1, pt1), extra1),))
        case _:
            raise TypeError(r1)
    _result1
    match (b_stop, ok):
        case (True, True):
            result = (+10, *_result1)
            return result
        case (True, False):
            result = (-11, *_result1)
            return result
        case (False, False):
            #result = (-12, *_result1)
            pass
        case _:
            raise 000
    ###############
    ((offset1, pt1), extra1)
    ###############
    ###############
    #stage2:
    ###############
    ###############
    offset1, pt1
    ###############
    max4xprime6stage1 = B1
    max4xprime6stage2 = B2
    as_ps = mk_Reproduceable7xprimes_(max4xprime6stage2, min4xprime=1+max4xprime6stage1, case=case4xprimes)
    ###############
    #as_zps = Reproduceable7tmay_prev_oresult((0,), as_ps)
    as_dps = Reproduceable7rdiff(int.__rsub__, 0, as_ps)
        # [q-p]
        # [delta_p]
        # [dp]
    ###############
    e2pw = CachedPow(mul_, square_, pow_, one, pt1, max4exp7cached:=3*(B1.bit_length()+B2.bit_length()))
    777;cached_pow_ = e2pw.__getitem__
    as_dpws = Reproduceable7fmap(cached_pow_, as_dps)
        # [pt1**delta_p]
        # [dpw]
    as_pws = Reproduceable7foldl(mul_, one, as_dpws)
        # [pt1**p]
        # [pw]
    as_pwmms = Reproduceable7fmap(diff_one_, as_pws)
        # [diff_one_(pt1**p)]
        # [pwmm]
    _as_pts6stage2 = Reproduceable7foldl(mul_, one, as_pwmms)
        # [II[diff_one_(pt1**q) | q...]...]
    pseudo_diff_one_ = echo
    pseudo_pt1 = diff_one_(pt1)
    as_pts6stage2 = Reproduceable7tmay_prev_oresult((pseudo_pt1,), _as_pts6stage2)
        # [II[diff_one_(pt1**q) | 1,q...]...]
    ###############
    if _debug7list_all:
        _show(locals(), 'as_ps')
        _show(locals(), 'as_dps')
        _show(locals(), 'as_dpws')
        _show(locals(), 'as_pws')
        _show(locals(), 'as_pwmms')
        _show(locals(), 'as_pts6stage2')

    ###############
    r2 = _search(max_size7dense, max_size7physical, num_muls_per_detect, imay_detect_period, pseudo_diff_one_, detect_, offset1, pseudo_pt1, 'stage2', as_pts6stage2)
    match r2:
        case (b_stop, (ok, may_output, (offset2, pseudo_pt2), extra2)):
            _result2 = (may_output, (((offset1, pt1), extra1), ((offset2, pseudo_pt2), extra2)))
        case _:
            raise TypeError(r2)
    _result2
    match (b_stop, ok):
        case (True, True):
            result = (+20, *_result2)
            return result
        case (True, False):
            result = (-22, *_result2)
            return result
        case (False, False):
            result = (-23, *_result2)
            return result
        #case (False, (False, None, (offset2, pseudo_pt2), extra2) as result2):
            #old:return result2
            # [pt1 is more important than pt2]
            #   esp:[pseudo_pt2 =!= pt1**q]
            #   now:[pseudo_pt2 === II[diff_one_(pt1**q) | q...]]
        case _:
            raise 000
    raise 000
    ###############


def _search(max_size7dense, max_size7physical, num_muls_per_detect, imay_detect_period, diff_one_, detect_, offset0, pt0, tag4stage1, as_pts6stage1, /):
    # -> (b_stop, payload)
    # -> (b_stop, result)
    # -> (ok, may_output, (data4next_stage/last_record/(offset1,pt1)), extra1)
    ###############
    history_saver = mk_history_saver_(max_size7dense, max_size7physical, num_muls_per_detect, imay_detect_period)
    history_saver.append(as_pts6stage1)
    ###############
    if 0:b_stop = False
    offset = offset0
    while 1:
        detect_result = detect_(diff_one_(history_saver.last.prev_oresult))
        match detect_result:
            case (-1, None):
                #move_fwd
                pass
            case (1, None):
                #move_bwd
                b_stop = True
                break
            case (0, output):
                b_stop = True
                break
            case bad:
                raise TypeError(detect_result)
        offset += -1 +len(history_saver)
        777;history_saver.clear_but_last_()
        sz0 = len(history_saver)
        assert sz0 == 1
        history_saver.fills7unlimit_()
        sz1 = len(history_saver)
        if sz1 == sz0:
            b_stop = False
            # goto stage2
            break
    b_stop
    history_saver
    ###############
    if b_stop:
        def history2rank_(history, /):
            detect_result = detect_(diff_one_(history.prev_oresult))
            rank = detect_result[0]
            #if rank == 0:
            return rank
        search_result = history_saver.search7dense_(history2rank_, zero6sparse_ok=True, offset=offset)
            # '(history -> (-1|0|+1)) -> (uint%6, may i:history:-1, may j:history:(0|1))/((0, ::-1, ::0)|(1, None, ::0)|(2, ::-1, ::+1)|(3, None, ::+1)|(4, ::-1, None)|(5, None, None))'
    else:
        assert 1 == len(history_saver)
        777;offset1 = offset
        pt1 = history_saver.last.prev_oresult
        search_result = (4, (offset1, pt1, -1), None)
    search_result
    extra1 = (tag4stage1, (offset0, pt0), search_result)
    # -> (ok, may_output, (data4next_stage/last_record), extra1)
    if b_stop:
        # -> (ok, may output, last_record, extra1)
        def on01_(j, h0, /):
            offset1 = j
            pt1 = h0.prev_oresult
            match detect_(diff_one_(pt1)):
                case (0, output):
                    return (b_stop, (ok:=True, output, (offset1, pt1), extra1))
            raise 000
        def on23_(j, h1, /):
            offset1 = j
            pt1 = h1.prev_oresult
            return (b_stop, (ok:=False, None, (offset1, pt1), extra1))
        match search_result:
            case (0, (i, h1n, -1),  (j, h0, 0)):
                return on01_(j, h0)
            case (1, None,          (j, h0, 0)):
                return on01_(j, h0)
            case (2, (i, h1n, -1),  (j, h1, 1)):
                return on23_(j, h1)
            case (3, None,          (j, h1, 1)):
                return on23_(j, h1)
            case (4, (i, h1n, -1),  None):
                raise 000
            case (5, None,          None):
                raise 000
            case _:
                raise TypeError(search_result)
        raise 000
    else:
        # -> (ok, None, data4next_stage, extra1)
        return (b_stop, (ok:=False, None, (offset1, pt1), extra1))
    raise 000
smooth_group_order_method_.__doc__ =\
r'''[[[
-> (ocase, may_output, [((offset{stage}, pseudo-pt{offset{stage}}), extra{stage})]{len=stage})


output:
    [ocase <- [+10,-11, +20,-22,-23]]
    [extra1 == ('stage1', (offset0, pt0), search_result{stage1})]
    [extra2 == ('stage2', (offset1, pt1), search_result{stage2})]
    [search_result : see:result{IHistorySaver.search7dense_()}]


input:
    [bound4stage1 :: uint{>=1}]
    [bound4pow4stage1 :: uint{>=1}]
    [bound4stage2 :: uint{>=1}]
    [num_muls_per_detect :: uint{>=1}]
        used only [imay_detect_period==0]
    [imay_detect_period :: uint{>=-1}]
        if imay_detect_period==0:
            detect_period := num_muls_per_detect
        elif imay_detect_period==-1:
            detect_period := +oo
        else:
            detect_period := imay_detect_period
        detect_period => how often detect_() be called



    [diff_one_ :: pt -> pt]
    [detect_ :: pt -> ((-1|0|+1), may output)/((-1, None)/move_fwd|(+1/move_bwd{#imay_num_steps4detect#},None)|(0/stop, output))]

    # group ops:mul_,may_square_,may_square
    [mul_ :: pt -> pt -> pt]
    [may_square_ :: may (pt -> pt)]
    [may_pow_ :: may (pt -> uint -> pt)]

    # group elements:one,pt0
    [one, pt0 :: pt]


#]]]'''#'''
    #old:'[detect_ :: pt -> ((0, None)/move_fwd|(-1/move_bwd{#imay_num_steps4detect#},None)|(1/stop, output))][imay_num_steps4detect == (-1/detect_once6stage1|0/auto|uint{>0})]'







r'''[[[
class stage1(IReproduceable):
    __slots__ = ()
    @abstractmethod
    def layer1_state2may_xprime_ex_(sf, st6layer1, /):
        'st6layer1 -> may (xprime, st6layer1)'
    @abstractmethod
    def layer2_stated_xprime2num_dups_ex_(sf, st6layer2, xprime, /):
        'st6layer2 -> xprime -> (num_dups, st6layer2)'
    @abstractmethod
    def layer3_state2may_xprime_ex_(sf, st6layer3, /):
        'st6layer3 -> may (xprime, st6layer3)'
    @abstractmethod
    def layer4_stated_xprime2pow4point_ex_(sf, st6layer4, xprime, /):
        'st6layer4{pt} -> xprime -> (pow4pt/pt, st6layer4{pow4pt})'
    @abstractmethod
    def mk_state6layer3_to_continue_(sf, st6layer3, xprime, num_dups, /):
        'st6layer3 -> xprime -> num_dups -> st6layer3'
    @abstractmethod
    def get_point6layer4_stater(sf, st6layer4, /):
        'st6layer4 -> pt'
    @property
    @abstractmethod
    def max4xprime(sf, /):
        '-> uint'
    @property
    @abstractmethod
    def state6layer1(sf, /):
        '-> st6layer1'
    @property
    @abstractmethod
    def state6layer2(sf, /):
        '-> st6layer2'
    @property
    @abstractmethod
    def state6layer3(sf, /):
        '-> st6layer3'
    @property
    @abstractmethod
    def state6layer4(sf, /):
        '-> st6layer4'
    @property
    def point(sf, /):
        '-> pt'
    @abstractmethod
    def mk5states6layer1_2_3_4_(sf, st6layer1, st6layer2, st6layer3, st6layer4, /):
        'st6layer1 -> st6layer2 -> st6layer3 -> st6layer4 -> __class__'

    def _xnext6layer1_(sf, /):
        match sf.layer1_state2may_xprime_ex_(sf.st6layer1):
            case (xprime, st6layer1):
                return (xprime, st6layer1)
            case None:
                return None
        raise 000
    def _xnext6layer2_(sf, /):
        match sf._xnext6layer1_():
            case (xprime, st6layer1):
                (num_dups, st6layer2) = sf.layer2_stated_xprime2num_dups_ex_(sf.st6layer2, xprime):
                return (xprime, num_dups, st6layer1, st6layer2)
            case None:
                return None
        raise 000
    def _xnext6layer3_(sf, /):
        st12 = (sf.state6layer1, sf.state6layer2)
        st6layer3 = sf.state6layer3
        while 1:
            match sf.layer3_state2may_xprime_ex_(st6layer3):
                case (xprime, st6layer3):
                    st123 = (*st12, st6layer3)
                    return (xprime, st123)
                case None:
                    match sf._xnext6layer2_():
                        case (xprime, num_dups, st6layer1, st6layer2):
                            st6layer3 = sf.mk_state6layer3_to_continue_(state6layer3, xprime, num_dups)
                            st12 = (st6layer1, st6layer2)
                            continue
                        case None:
                            return None
                    raise 000
            raise 000
        raise 000
    def _xnext6layer4_(sf, /):
        match sf._xnext6layer3_():
            case (xprime, st123):
                (pow4pt, st6layer4)= sf.layer4_stated_xprime2pow4point_ex_(sf.st6layer4, xprime)
                st1234 = (*st123, st6layer4)
                return (pow4pt, st1234)
            case None:
                return None
        raise 000
    @override
    def ___xnext4reproduceable___(sf, /):
        'IReproduceable{x} -> (NextEx(x, IReproduceable{x}) | StopEx(exit_status))'
        match sf._xnext6layer4_():
            case (pow4pt, st1234):
                ot = sf.mk5states6layer1_2_3_4_(*st1234)
                return NextEx(pow4pt, ot)
            case None:
                return StopEx(None)
        raise 000

data7reconstruct#reload
data7selected
core :: st -> IN -> (OUT, st)
wrap :: (st,a) -> (IN,b) -> ((OUT,c), (st,d))
wrap :: st_ex -> IN_ex -> (OUT_ex, st_ex)
    td1 :: st_ex -> (st,a) #decompose_outer_state
    td2 :: IN_ex -> (IN,b) #decompose_lower_output

    mk3456 :: a -> b -> (OUT, st) -> (OUT_ex, st_ex)
        mg3 :: (OUT, st) -> ex_args4cd
        mk4 :: a -> b -> *ex_args4cd -> (c,d)
        mk5 :: OUT -> c -> OUT_ex
        mk6 :: st -> d -> st_ex

#]]]'''#'''









#################################
r'''[[[
max4exp6stage1
max4exp6stage2
reproduceable4exps6stage1#neednot ascending
    [2 <= exp{j} <= max4exp6stage1]
    #xxx:[exp{j} <= exp{1+j}]
reproduceable4exps6stage2#strictly increasing
    [2 <= exp{j} <= max4exp6stage2]
    [exp{j} < exp{1+j}]

stage1:
    pt0
    detect_partial_one_
    [detect_partial_one_(pt) <- {-1,0,+1}]
        # [-1:not_one]
        # [0:partial_one]
        # [+1:one]
    [detect_partial_one_(pt) <= detect_partial_one_(pt**exp)]
        # sink@pow_
        #ascending
    [pt{j} == pt{-1+j}**exp{j}]
    -> pt7final6stage1
stage2:
    pt7final6stage1
    pow_
    mul_
    [pt{j} == pt{-1+j}*pt7final6stage1**(exp{j}-exp{-1+j})]

    detect_partial_one_#must check per step:eg:BinaryQuadraticForm class group is not Ring
    or:
    diff_one_
    detect_partial_zero_
    [detect_partial_zero_(pt) <- {-1,0,+1}]
        # [-1:not_zero]
        # [0:partial_zero]
        # [+1:zero]
    [detect_partial_one_(pt) == detect_partial_zero_(diff_one_(pt))]
    [detect_partial_zero_(ptA) <= detect_partial_zero_(ptA*ptB)]
        # sink@mul_
    -> pt7final6stage2

#]]]'''#'''
#################################
# ver2:?OO?
#################################
__all__
class ICommonOps4smooth_group_order_method(ABC):
    __slots__ = ()
    @abstractmethod
    def detect_partial_one_(sf, pt, /):
        'pt -> (-1/not_one|0/partial_one|+1/one) # [detect_partial_one_(pt) <= detect_partial_one_(pow_(pt,exp))]'
    @abstractmethod
    def pow_(sf, pt, exp, /):
        'pt -> exp/uint -> pt'
    @abstractmethod
    def square_(sf, pt, /):
        'pt -> pt'
    @abstractmethod
    def mul_(sf, pt8lhs, pt8rhs, /):
        'pt -> pt -> pt'
    @abstractmethod
    def eq_one_(sf, pt, /):
        'pt -> bool'
    @property
    @abstractmethod
    def one(sf, /):
        '-> pt'

class IOps6stage1_4smooth_group_order_method(ICommonOps4smooth_group_order_method):
    __slots__ = ()
    def prepare_exps4search6stage1_(sf, max4exp6stage1, may_reproduceable4exps6stage1, /):
        'max4exp6stage1/uint{>0} -> may IReproduceable{exp/uint{>=2}{<=max4exp6stage1}} -> IReproduceable{exp/uint{>=2}{<=max4exp6stage1}}'
        reproduceable4exps6stage1 = may_reproduceable4exps6stage1 if not None is may_reproduceable4exps6stage1 else sf._prepare_exps4search6stage1_(max4exp6stage1)
        check_type_le(IReproduceable, reproduceable4exps6stage1)
        return reproduceable4exps6stage1
    @abstractmethod
    def _prepare_exps4search6stage1_(sf, max4exp6stage1, /):
        'max4exp6stage1/uint{>0} -> IReproduceable{exp/uint{>=2}{<=max4exp6stage1}}'
        rp8dup_ps = mk_Reproduceable7dup_xprimes__ver2_(max4exp6stage1, max4exp6stage1, case=None)
        return rp8dup_ps
    @abstractmethod
    def search6stage1_(sf, to_search_exps8factors4order6found, detect_period, max4exp6stage1, may_reproduceable4exps6stage1, pt0, /):
        'to_search_exps8factors4order6found/bool -> detect_period/uint{>0} -> max4exp6stage1/uint{>0} -> IReproduceable{exp/uint{>=2}{<=max4exp6stage1}} -> pt0/pt -> ((-1, offset:pt7final6stage1/pt{not_one})|((0|+1), may offset:pt7prev{not_one}:exp, offset:pt7found6stage1{partial_one|one}{==pow_(pt7prev,exp)}, may [exp]{iff to_search_exps8factors4order6found}))'
        return default_search6stage1_(sf, to_search_exps8factors4order6found, detect_period, max4exp6stage1, may_reproduceable4exps6stage1, pt0, max_size7dense=2049, max_size7physical=65537)


class IOps6stage2_4smooth_group_order_method(ICommonOps4smooth_group_order_method):
    __slots__ = ()
    def prepare_exps4search6stage2_(sf, max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage2, /):
        'max4exp6stage1/uint{>0} -> max4exp6stage2/uint{>0} -> may IReproduceable{exp/uint{>=2}{<=max4exp6stage2}} -> IReproduceable{exp/uint{>=2}{<=max4exp6stage2}}'
        reproduceable4exps6stage2 = may_reproduceable4exps6stage2 if not None is may_reproduceable4exps6stage2 else sf._prepare_exps4search6stage2_(max4exp6stage1, max4exp6stage2)
        check_type_le(IReproduceable, reproduceable4exps6stage2)
        return reproduceable4exps6stage2
    @abstractmethod
    def _prepare_exps4search6stage2_(sf, max4exp6stage1, max4exp6stage2, /):
        'max4exp6stage1/uint{>0} -> max4exp6stage2/uint{>0} -> IReproduceable{exp/uint{>=2}{<=max4exp6stage2}}'
        rp8ps = mk_Reproduceable7xprimes_(max4exp6stage2, min4xprime=1+max4exp6stage1, case=None)
        return rp8ps
    @abstractmethod
    def search6stage2__7detect_per_step_(sf, max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage2, pt7final6stage1, /):
        'max4exp6stage1/uint{>0} -> max4exp6stage2/uint{>0} -> IReproduceable{exp/uint{>=2}{<=max4exp6stage2}}{strictly_increasing} -> pt7final6stage1/pt -> ((-1|0|+1), exp_or1:offset:(pt7final6stage2/pt{not_one}|pt7found6stage2{partial_one|one}){==pow_(pt7final6stage1,exp_or1)}) # detect_per_step:[detect_period==1]'
        return default_search6stage2__7detect_per_step_(sf, max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage2, pt7final6stage1)
class IOps6stage2_4smooth_group_order_method7ring(IOps6stage2_4smooth_group_order_method):
    __slots__ = ()
    @override
    def detect_partial_one_(sf, pt, /):
        return sf.detect_partial_zero_(sf.diff_one_(pt))
    @override
    def search6stage2__7detect_per_step_(sf, max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage2, pt7final6stage1, /):
        return sf.search6stage2__7ring_(detect_period:=1, max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage2, pt7final6stage1)
    @abstractmethod
    def eq_zero_(sf, pt, /):
        'pt -> bool'
    @property
    @abstractmethod
    def zero(sf, /):
        '-> pt'
    @abstractmethod
    def detect_partial_zero_(sf, pt, /):
        'pt -> (-1/not_zero|0/partial_zero|+1/zero) # [detect_partial_zero_(ptA) <= detect_partial_zero_(mul_(ptA,ptB))] # [detect_partial_one_(pt) == detect_partial_zero_(diff_one_(pt))]'
    @abstractmethod
    def diff_one_(sf, pt, /):
        'pt -> pt'

    @abstractmethod
    def search6stage2__7ring_(sf, detect_period, max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage2, pt7final6stage1, /):
        'detect_period/uint{>0} -> max4exp6stage1/uint{>0} -> max4exp6stage2/uint{>0} -> IReproduceable{exp/uint{>=2}{<=max4exp6stage2}}{strictly_increasing} -> pt7final6stage1/pt -> ((-1|0|+1), exp_or1:offset:(pt7final6stage2/pt{not_one}|pt7found6stage2{partial_one|one}){==pow_(pt7final6stage1,exp_or1)})'
        return default_search6stage2__7ring_(sf, detect_period, max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage2, pt7final6stage1, max_size7dense=2049, max_size7physical=65537)
#################################
class IOps6stage12_4smooth_group_order_method(IOps6stage2_4smooth_group_order_method, IOps6stage1_4smooth_group_order_method):
    __slots__ = ()
    @abstractmethod
    def search6stage12_(sf, to_search_exps8factors4order6found, detect_period, max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage1, may_reproduceable4exps6stage2, pt0, /):
        'see:default_search6stage12_'
        return default_search6stage12_(sf, to_search_exps8factors4order6found, detect_period, max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage1, may_reproduceable4exps6stage2, pt0)
class IOps6stage12_4smooth_group_order_method7ring(IOps6stage2_4smooth_group_order_method7ring, IOps6stage12_4smooth_group_order_method):
    __slots__ = ()
    @abstractmethod
    def search6stage12__7ring_(sf, to_search_exps8factors4order6found, detect_period, max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage1, may_reproduceable4exps6stage2, pt0, /):
        'see:default_search6stage12__7ring_'
        return default_search6stage12__7ring_(sf, to_search_exps8factors4order6found, detect_period, max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage1, may_reproduceable4exps6stage2, pt0)
def default_search6stage12__7ring_(ops7stage12_7ring, to_search_exps8factors4order6found, detect_period, max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage1, may_reproduceable4exps6stage2, pt0, /, *, ver=1):
    'see:default_search6stage12_'
    return default_search6stage12_(ops7stage12_7ring, to_search_exps8factors4order6found, detect_period, max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage1, may_reproduceable4exps6stage2, pt0, _is_ring=True, ver=ver)
def default_search6stage12_(ops7stage12, to_search_exps8factors4order6found, detect_period, max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage1, may_reproduceable4exps6stage2, pt0, /, *, _is_ring=False, ver=1):
    assert ver in (0, 1)
    search6stage2__7XXX_ = ops7stage12.search6stage2__7ring_ if _is_ring else ops7stage12.search6stage2__7detect_per_step_
    extra_args6stage2 = (detect_period,) if _is_ring else ()

    reproduceable4exps6stage1 = ops7stage12.prepare_exps4search6stage1_(max4exp6stage1, may_reproduceable4exps6stage1)
    reproduceable4exps6stage2 = ops7stage12.prepare_exps4search6stage2_(max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage2)

    to_search_exps8factors4order6found = bool(to_search_exps8factors4order6found)
    if ver == 0 or not to_search_exps8factors4order6found:
        r1 = ops7stage12.search6stage1_(to_search_exps8factors4order6found, detect_period, max4exp6stage1, reproduceable4exps6stage1, pt0)
    else:
        assert ver == 1
        assert to_search_exps8factors4order6found
        (r1, (history_saver, offset7first, offset7last)) = default_search6stage1_(ops7stage12, to_search_exps8factors4order6found, detect_period, max4exp6stage1, reproduceable4exps6stage1, pt0, to_output_history_saver=True)
        # !! to_search_exps8factors4order6found
        (history_saver7oo, offset7first7oo, offset7last7oo) = (history_saver, offset7first, offset7last)
    match (to_search_exps8factors4order6found, r1):
        case (_, (-1, (offset1, pt1))):
            pass
        #case (False, ((0|1) as _01, (None|(offset7prev, pt7prev, exp7key7last)), (offset7found6stage1, pt7found6stage1), may_exps7key_patch)):
        case (True, ((0|1) as _01, _, (offset7found6stage1, pt7found6stage1), exps7key_patch)):
            assert len(exps7key_patch) == 2
            return (107, _01, pt7found6stage1, exps7key_patch)
        case (False, ((0|1) as _01, (offset7prev, pt7prev, exp7key7last), (offset7found6stage1, pt7found6stage1), None)):
            return (103, _01, pt7found6stage1, exp7key7last)
        case (False, ((0|1) as _01, None, (offset7found6stage1, pt7found6stage1), None)):
            return (101, _01, pt7found6stage1, None)
        case _:
            raise TypeError(r1)
    (offset1, pt1)
    #r2 = ops7stage12.search6stage2__7detect_per_step_(max4exp6stage1, max4exp6stage2, reproduceable4exps6stage2, pt1)
    r2 = search6stage2__7XXX_(*extra_args6stage2, max4exp6stage1, max4exp6stage2, reproduceable4exps6stage2, pt1)
    match (to_search_exps8factors4order6found, r2):
        #case ((-1|0,1) as _n101, (exp_or1, offset2, pt2)):
        case (_, (-1, (exp_or1, offset7final6stage2, pt7final6stage2))):
            return (202, -1, r1, r2)
        case (False, ((0|1) as _01, (exp7key7last, offset7found6stage2, pt7found6stage2))):
            return (203, _01, pt7found6stage2, exp7key7last)
        case (True, ((0|1) as _01, (exp7key7last, offset7found6stage2, pt7found6stage2))):
            pass
        case _:
            raise TypeError(r2)
    # (_n101, (exp_or1, offset2, pt2))
    assert to_search_exps8factors4order6found
    _01, (exp7key7last, offset7found6stage2, pt7found6stage2)
    if not ver == 0:
        ######################
        #new version:
        assert ver == 1
        assert to_search_exps8factors4order6found
        (history_saver7oo, offset7first7oo, offset7last7oo)
        stZhistory2rank_ = _mk_stZhistory2rank_(ops7stage12.detect_partial_one_, ops7stage12.pow_)
        op4fold_ = _op4fold
        st7fold = (exp7key7last, (exp7key7last, ()))
        # [st7fold :: (II(exps7key), lflnkls{exps7key})]
        (st7fold, ls4record_pair) = history_saver7oo.reversed_search_key_points_(stZhistory2rank_, op4fold_, st7fold, offset=offset7first7oo)
        (IIexps7key, lflnkls8exps7key) = st7fold
        exps7key = tuple(lflnkls2iterable(lflnkls8exps7key))
        assert II(exps7key) == IIexps7key
        assert exps7key[-1] == exp7key7last
        _exps7key = exps7key
        patch0001 = _mk_patch0001_(ops7stage12.detect_partial_one_, ops7stage12.pow_, pt0, IIexps7key)
        _exps7key_patch = (_exps7key, patch0001)
        return (207, _01, pt7found6stage2, _exps7key_patch)


    else:
        ######################
        #old version:
        assert ver == 0
        assert to_search_exps8factors4order6found
        pt0_6stage2 = ops7stage12.pow_(pt0, exp7key7last)
        r1_6stage2 = ops7stage12.search6stage1_(to_search_exps8factors4order6found, detect_period, max4exp6stage1, reproduceable4exps6stage1, pt0_6stage2)
        match r1_6stage2:
            case (-1, (offset1_6stage2, pt1_6stage2)):
                raise Exception(r1_6stage2)
            case ((0|1) as _01, _, (offset7found6stage1_6stage2, pt7found6stage1_6stage2), (exps7key, patch0001) as exps7key_patch):
                _exps7key = (*exps7key, exp7key7last)
                _exps7key_patch = (_exps7key, patch0001)
                return (207, _01, pt7found6stage1_6stage2, _exps7key_patch)
            case _:
                raise TypeError(r1_6stage2)
        raise 000
    raise 000
default_search6stage12_.__doc__ = \
r'''[[[
* -> (case6fail/202, detect_result6fail/-1, search_result6stage1, search_result6stage2)
* -> (case6ok, detect_result6ok, pt, may (exp7key7last|exps7key_patch))
    * -> (107, (0|+1), pt7found6stage1, exps7key_patch) #@to_search_exps8factors4order6found
    * -> (103, (0|+1), pt7found6stage1, exp7key7last)
    * -> (101, (0|+1), pt7found6stage1, None)
    * -> (203, (0|+1), pt7found6stage1, exp7key7last)
    * -> (207, (0|+1), pt7found6stage1, exps7key_patch) #@to_search_exps8factors4order6found
[exps7key_patch == (exps7key/[exp7key], patch0001/((0|+1),pt7found6stage1_5exps7key))]

#]]]'''#'''
default_search6stage12__7ring_.__doc__ = default_search6stage12_.__doc__

#################################
def default_search6stage2__7ring_(ops7stage2_7ring, detect_period, max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage2, pt7final6stage1, /, *, _debug7list_all=False, max_size7dense=2049, max_size7physical=65537):
    '-> ((-1|0|+1), exp_or1:offset:(pt7final6stage2/pt{not_one}|pt7found6stage2{partial_one|one}){==pow_(pt7final6stage1,exp_or1)}) # see:search6stage2__7ring_'
    if detect_period == 1:
        return default_search6stage2__7detect_per_step_(ops7stage2_7ring, max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage2, pt7final6stage1)

    mul_ = ops7stage2_7ring.mul_
    square_ = ops7stage2_7ring.square_
    pow_ = ops7stage2_7ring.pow_
    detect_partial_one_ = ops7stage2_7ring.detect_partial_one_
    detect_partial_zero_ = ops7stage2_7ring.detect_partial_zero_
    diff_one_ = ops7stage2_7ring.diff_one_
    reproduceable4exps6stage2 = ops7stage2_7ring.prepare_exps4search6stage2_(max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage2)

    B2 = max4exp6stage2
    pt1 = pt7final6stage1
    one = pow_(pt1, 0)
    rp8exps6stage2 = reproduceable4exps6stage2
    CachedPow
    e2pw = CachedPow(mul_, square_, pow_, one, pt1, max4exp7cached:=6*B2.bit_length())
    777;cached_pow_ = e2pw.__getitem__
    ops7rdiff = StatedTransformOps7rdiff(int.__rsub__)
    ops7fmap7pow = StatedTransformOps7fmap(cached_pow_)
    ops7foldl = StatedTransformOps7foldl(mul_)
    ops7fmap7diff1 = StatedTransformOps7fmap(diff_one_)
    #ops7flow = StatedTransformOps7flow(False, [ops7rdiff, ops7fmap7pow, ops7foldl, ops7fmap7diff1, ops7foldl])
    #ops7flow7pow = StatedTransformOps7flow(False, [ops7rdiff, ops7fmap7pow, ops7foldl])
    ops7flow7IIdiff1 = StatedTransformOps7flow(False, [ops7fmap7diff1, ops7foldl])
    ops7fork7echo_IIdiff1 = StatedTransformOps7fork(False, [get_ops4transform7stated7echo_(), ops7flow7IIdiff1])
    ops7flow7pow_IIpowmm = StatedTransformOps7flow(False, [ops7rdiff, ops7fmap7pow, ops7foldl, ops7fork7echo_IIdiff1])

    ops7fork = StatedTransformOps7fork(False, [get_ops4transform7stated7echo_(), ops7flow7pow_IIpowmm])
        # IReproduceable{(exp, (pt1**exp, IIprev_pows * (-1+pt1**exp)))}
    rp8exp_pow_pairs6stage2 = Reproduceable7tmay_prev_oresult(((1, (pt1, diff_one_(pt1))),), Reproduceable7transform_via_ops(ops7fork, (None, (0, None, one, (None, (None, one)))), rp8exps6stage2))

    ###############
    if _debug7list_all:
        _show(locals(), 'rp8exps6stage2')
        _show(locals(), 'rp8exp_pow_pairs6stage2')

    ###############
    def detect_partial_zero6snd_(pow_IIpowmm, /):
        (pw, IIpwmm) = pow_IIpowmm
        return detect_partial_zero_(IIpwmm)
    ###############
    offset1 = 0
    (b_stop, history_saver, detect_result, offset7first, offset7last) = _search8base(max_size7dense, max_size7physical, detect_period, detect_partial_zero6snd_, offset1, rp8exp_pow_pairs6stage2)
    if detect_period == 1 or detect_result == -1:
        (exp_or1, (pt7last, _)) = history_saver.last.prev_oresult
        return (detect_result, (exp_or1, offset7last, pt7last))
    else:
        def history2rank_(history, /):
            pow_IIpowmm = history.prev_oresult[1]
            return detect_partial_zero6snd_(pow_IIpowmm)
        r = history_saver.search7dense_(history2rank_, zero6sparse_ok=False, offset=offset1)
        # !! b_stop
        assert r[0] < 4
        match r:
            case (_, _, (j, rp6j, _01)):
                offset7found6stage2 = j
                (exp_or1, (pw, IIpwmm)) = rp6j.prev_oresult
                pt7found6stage2 = pw
                _01
            case _:
                raise 000
        _01
        return (_01, (exp_or1, offset7found6stage2, pt7found6stage2))
    raise 000





def default_search6stage2__7detect_per_step_(ops7stage2, max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage2, pt7final6stage1, /, *, _debug7list_all=False):
    '-> ((-1|0|+1), exp_or1:offset:(pt7final6stage2/pt{not_one}|pt7found6stage2{partial_one|one}){==pow_(pt7final6stage1,exp_or1)}) # detect_per_step:[detect_period==1] # see:search6stage2__7detect_per_step_'
    mul_ = ops7stage2.mul_
    square_ = ops7stage2.square_
    pow_ = ops7stage2.pow_
    detect_partial_one_ = ops7stage2.detect_partial_one_
    reproduceable4exps6stage2 = ops7stage2.prepare_exps4search6stage2_(max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage2)

    B2 = max4exp6stage2
    pt1 = pt7final6stage1
    one = pow_(pt1, 0)
    rp8exps6stage2 = reproduceable4exps6stage2
    CachedPow
    #square_ = mk_square5may_(mul_, may_square_)
    #pow_ = mk_pow5may_(mul_, square_, may_pow_, one)
    e2pw = CachedPow(mul_, square_, pow_, one, pt1, max4exp7cached:=6*B2.bit_length())
    777;cached_pow_ = e2pw.__getitem__
    ops7rdiff = StatedTransformOps7rdiff(int.__rsub__)
    ops7fmap = StatedTransformOps7fmap(cached_pow_)
    ops7foldl = StatedTransformOps7foldl(mul_)
    ops7flow = StatedTransformOps7flow(False, [ops7rdiff, ops7fmap, ops7foldl])

    ops7fork = StatedTransformOps7fork(False, [get_ops4transform7stated7echo_(), ops7flow])
    rp8exp_pow_pairs6stage2 = Reproduceable7tmay_prev_oresult(((1, pt1),), Reproduceable7transform_via_ops(ops7fork, (None, (0, None, one)), rp8exps6stage2))

    ###############
    if _debug7list_all:
        _show(locals(), 'rp8exps6stage2')
        _show(locals(), 'rp8exp_pow_pairs6stage2')

    ###############
    offset1 = 0
    (b_stop, history_saver, detect_result, offset7first, offset7last) = _search8base(max_size7dense:=2, max_size7physical:=2, detect_period:=1, detect_partial_one_, offset1, rp8exp_pow_pairs6stage2)
    (exp_or1, pt7last) = history_saver.last.prev_oresult
    # !! [detect_period==1]
    return (detect_result, (exp_or1, offset7last, pt7last))


def default_search6stage1_(ops7stage1, to_search_exps8factors4order6found, detect_period, max4exp6stage1, may_reproduceable4exps6stage1, pt0, /, *, _debug7list_all=False, _verbose=False, max_size7dense=2049, max_size7physical=65537, to_output_history_saver=False):
    '-> ((-1, offset:pt7final6stage1/pt{not_one})|((0|+1), may offset:pt7prev{not_one}:exp, offset:pt7found6stage1{partial_one|one}{==pow_(pt7prev,exp)}, may ([exp], patch0001/((0|+1),pt7found6stage1_5exps7key)){iff to_search_exps8factors4order6found})) #see:search6stage1_'
    pow_ = ops7stage1.pow_
    detect_partial_one_ = ops7stage1.detect_partial_one_
    reproduceable4exps6stage1 = ops7stage1.prepare_exps4search6stage1_(max4exp6stage1, may_reproduceable4exps6stage1)

    rp8exps6stage1 = reproduceable4exps6stage1
    ops7foldl = StatedTransformOps7foldl(pow_)
    ops7fork = StatedTransformOps7fork(False, [get_ops4transform7stated7echo_(), ops7foldl])
    rp8exp_pow_pairs6stage1 = Reproduceable7tmay_prev_oresult(((1, pt0),), Reproduceable7transform_via_ops(ops7fork, (None, pt0), rp8exps6stage1))

    ###############
    if _debug7list_all:
        _show(locals(), 'rp8exps6stage1')
        _show(locals(), 'rp8exp_pow_pairs6stage1')

    ###############
    offset0 = 0
    (b_stop, history_saver, detect_result, offset7first, offset7last, *ex) = _search8base(max_size7dense, max_size7physical, detect_period, detect_partial_one_, offset0, rp8exp_pow_pairs6stage1, to_search_exps8factors4order6found=to_search_exps8factors4order6found)
    if to_search_exps8factors4order6found:
        [(history_saver7oo, offset7first7oo, offset7last7oo)] = ex
        (history_saver, offset7first, offset7last) = (history_saver7oo, offset7first7oo, offset7last7oo)
            # to_search_exps8factors4order6found
            # to_output_history_saver
    else:
        [] = ex

    if not b_stop:
        assert detect_result == -1
        pt7final6stage1 = history_saver.last.prev_oresult[1]
        offset1 = offset7last
        search_result6stage1 = (-1, (offset1, pt7final6stage1))
        if to_output_history_saver:
            return (search_result6stage1, (history_saver, offset7first, offset7last))
        return search_result6stage1
    assert detect_result in (0, +1)

    patch0001 = None
    if to_search_exps8factors4order6found:
        stZhistory2rank_ = _mk_stZhistory2rank_(detect_partial_one_, pow_)
        op4fold_ = _op4fold
        #st7fold = (1, ())
        st7fold = (1, get_empty_lflnkls())
        # [st7fold :: (II(exps7key), lflnkls{exps7key})]
        (st7fold, ls4record_pair) = history_saver.reversed_search_key_points_(stZhistory2rank_, op4fold_, st7fold, offset=offset7first)

        if _verbose:
            print_err('st7fold', st7fold)
            print_err('ls4record_pair', ls4record_pair)
            #raise Exception(st7fold, ls4record_pair)
        (IIexps7key, lflnkls8exps7key) = st7fold
        exps7key = tuple(lflnkls2iterable(lflnkls8exps7key))
        assert II(exps7key) == IIexps7key
        may_exps7key = exps7key
        match ls4record_pair:
            case []:
                (j, rp6j, _01) = (offset0, rp8exp_pow_pairs6stage1, detect_result)
                pair = (None, (j, rp6j, _01))
            case [((jmm, rp6jmm, -1), (j, rp6j, _01)), *_]:
                # !! 『reversed』@『reversed_search_key_points_()』
                pair = ((jmm, rp6jmm, -1), (j, rp6j, _01))
                if 'patch0001':
                    # !! ops{%1247}.search6stage12__7ring_(True, 999, 7, 7, rp8exps6stage1{==[2,2,3,7]}, rp8exps6stage2{==[]}, pt0:=3)->(107, 1, 1, (2, 2, 7)) # ==>>:patch0001
                    patch0001 = _mk_patch0001_(detect_partial_one_, pow_, pt0, IIexps7key)
            case _:
                raise 000
        pair
        may_exps7key
    else:
        may_exps7key = None
        def history2rank_(history, /):
            base = history.prev_oresult[1]
            return detect_partial_one_(base)
        r = history_saver.search7dense_(history2rank_, zero6sparse_ok=False, offset=offset0)
        # !! b_stop
        assert r[0] < 4
        pair = r[1:]
    pair
    may_exps7key
    match pair:
        case ((jmm, rp6jmm, -1), (j, rp6j, _01)):
            (exp, pt7found6stage1) = rp6j.prev_oresult
            pt7prev = rp6jmm.prev_oresult[1]
            may_dat6prev_key = (jmm, pt7prev, exp)
            dat6key = (j, pt7found6stage1)
            _01
        case (None, (j, rp6j, _01)):
            assert 1 == len(history_saver)
            assert history_saver.last is rp8exp_pow_pairs6stage1
            assert j == offset7last == offset0
            may_dat6prev_key = None
            dat6key = (offset0, pt0)
            _01
        case _:
            raise 000
    may_dat6prev_key
    dat6key
    _01
    may_exps7key, patch0001
    #old:return (_01, may_dat6prev_key, dat6key, may_exps7key)
        # ((0|+1), may offset:pt7prev:exp, offset:pt7found6stage1, may [exp])
    assert (None is may_exps7key) is (None is patch0001)
    if not None is may_exps7key:
        assert not None is patch0001
        may_exps7key_patch = (exps7key, patch0001)
    else:
        assert None is patch0001
        may_exps7key_patch = None
    search_result6stage1 = (_01, may_dat6prev_key, dat6key, may_exps7key_patch)
    if to_output_history_saver:
        return (search_result6stage1, (history_saver, offset7first, offset7last))
    return search_result6stage1
def _mk_patch0001_(detect_partial_one_, pow_, pt0, IIexps7key, /):
    #if 'patch0001':
    # !! ops{%1247}.search6stage12__7ring_(True, 999, 7, 7, rp8exps6stage1{==[2,2,3,7]}, rp8exps6stage2{==[]}, pt0:=3)->(107, 1, 1, (2, 2, 7)) # ==>>:patch0001
    pt00 = pow_(pt0, IIexps7key)
    _01_4pt00 = detect_partial_one_(pt00)
    assert _01_4pt00 in (0,1)
    patch0001 = (_01_4pt00, pt00)
    return patch0001




def _mk_stZhistory2rank_(detect_partial_one_, pow_, /):
    def stZhistory2rank_(st7fold, /):
        (IIexps7key, lflnkls8exps7key) = st7fold
        def history2rank_(history, /):
            base = history.prev_oresult[1]
            return detect_partial_one_(pow_(base, IIexps7key))
        return history2rank_
    return stZhistory2rank_
def _op4fold(prev_offset4key_point, offset4key_point, history6key_point, st7fold, /):
    # [st7fold :: (II(exps7key), lflnkls{exps7key})]
    exp7key = history6key_point.prev_oresult[0]
    (IIexps7key, lflnkls8exps7key) = st7fold
    IIexps7key *= exp7key
    (lflnkls8exps7key, _None) = lflnkls_ipush_left(lflnkls8exps7key, exp7key)
    st7fold = (IIexps7key, lflnkls8exps7key)
    return st7fold

def _search8base(max_size7dense, max_size7physical, detect_period, detect_partial_one_, offset0, rp8exp_pow_pairs6stage1, /, *, to_search_exps8factors4order6found=False):
    check_int_ge(1, detect_period)
    both = bool(to_search_exps8factors4order6found)
    history_saver = mk_history_saver_(max_size7dense, max_size7physical, num_muls_per_detect:=1, imay_detect_period:=detect_period)
    777;history_saver.append(rp8exp_pow_pairs6stage1)
    if both:
        history_saver7oo = mk_history_saver_(max_size7dense, max_size7physical, num_muls_per_detect:=1, imay_detect_period:=-1)
        777;history_saver7oo.append(rp8exp_pow_pairs6stage1)
        offset7first7oo = offset0
    ###############
    if 0:
        b_stop = False
        detect_result = -1
    offset = offset0
    while 1:
        detect_result = detect_partial_one_(history_saver.last.prev_oresult[1])
        match detect_result:
            case -1:
                #move_fwd
                pass
            case 1:
                #move_bwd
                b_stop = True
                break
            case 0:
                b_stop = True
                break
            case bad:
                raise TypeError(detect_result)
        offset += -1 +len(history_saver)
        777;history_saver.clear_but_last_()
        sz0 = len(history_saver)
        assert sz0 == 1
        if both:
            history_saver.both_fills7unlimit_(history_saver7oo)
        else:
            history_saver.fills7unlimit_()
        sz1 = len(history_saver)
        if sz1 == sz0:
            b_stop = False
            # goto next stage
            # goto stage2
            break
    b_stop
    history_saver
    detect_result
    if not b_stop:
        assert 1 == len(history_saver)
    offset7first = offset
    offset7last = offset + -1+len(history_saver)
    if both:
        #return (b_stop, offset7last, detect_result, (history_saver, offset7first), (history_saver7oo, offset7first7oo))
        offset7last7oo = offset7last
        return (b_stop, history_saver, detect_result, offset7first, offset7last, (history_saver7oo, offset7first7oo, offset7last7oo))
    return (b_stop, history_saver, detect_result, offset7first, offset7last)
    ###############


#################################
class ICommonOps4smooth_group_order_method__7default_mixin(ICommonOps4smooth_group_order_method):
    __slots__ = ()
    @override
    def pow_(sf, pt, exp, /):
        'pt -> exp/uint -> pt'
        check_int_ge(0, exp)
        #.pow_ = mk_pow5may_(sf.mul_, sf.square_, may_pow_:=None, sf.one)
        #.return pow_(pt, exp)
        return power_(sf.mul_, may_inv_:=None, may_eq_zero_:=None, sf.eq_one_, sf.one, imay_group_order:=-1, exp, pt)
    @override
    def square_(sf, pt, /):
        'pt -> pt'
        return sf.mul_(pt, pt)
    @override
    def eq_one_(sf, pt, /):
        'pt -> bool'
        return sf.one == pt
class IOps6stage1_4smooth_group_order_method__7default_mixin(ICommonOps4smooth_group_order_method__7default_mixin, IOps6stage1_4smooth_group_order_method):
    __slots__ = ()
    @override
    def _prepare_exps4search6stage1_(sf, max4exp6stage1, /):
        rp8dup_ps = mk_Reproduceable7dup_xprimes__ver2_(max4exp6stage1, max4exp6stage1, case=None)
        return rp8dup_ps
    @override
    def search6stage1_(sf, to_search_exps8factors4order6found, detect_period, max4exp6stage1, may_reproduceable4exps6stage1, pt0, /):
        return default_search6stage1_(sf, to_search_exps8factors4order6found, detect_period, max4exp6stage1, may_reproduceable4exps6stage1, pt0, max_size7dense=2049, max_size7physical=65537)
class IOps6stage12_4smooth_group_order_method__7default_mixin(IOps6stage1_4smooth_group_order_method__7default_mixin, IOps6stage12_4smooth_group_order_method):
    __slots__ = ()
    @override
    def _prepare_exps4search6stage2_(sf, max4exp6stage1, max4exp6stage2, /):
        rp8ps = mk_Reproduceable7xprimes_(max4exp6stage2, min4xprime=1+max4exp6stage1, case=None)
        return rp8ps
    @override
    def search6stage2__7detect_per_step_(sf, max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage2, pt7final6stage1, /):
        return default_search6stage2__7detect_per_step_(sf, max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage2, pt7final6stage1)
    @override
    def search6stage12_(sf, to_search_exps8factors4order6found, detect_period, max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage1, may_reproduceable4exps6stage2, pt0, /):
        'see:default_search6stage12_'
        return default_search6stage12_(sf, to_search_exps8factors4order6found, detect_period, max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage1, may_reproduceable4exps6stage2, pt0)
class IOps6stage12_4smooth_group_order_method7ring__7default_mixin(IOps6stage12_4smooth_group_order_method__7default_mixin, IOps6stage12_4smooth_group_order_method7ring):
    __slots__ = ()
    @override
    def eq_zero_(sf, pt, /):
        'pt -> bool'
        return sf.zero == pt

    @override
    def search6stage2__7ring_(sf, detect_period, max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage2, pt7final6stage1, /):
        return default_search6stage2__7ring_(sf, detect_period, max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage2, pt7final6stage1, max_size7dense=2049, max_size7physical=65537)
    @override
    def search6stage12__7ring_(sf, to_search_exps8factors4order6found, detect_period, max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage1, may_reproduceable4exps6stage2, pt0, /):
        'see:default_search6stage12_'
        return default_search6stage12__7ring_(sf, to_search_exps8factors4order6found, detect_period, max4exp6stage1, max4exp6stage2, may_reproduceable4exps6stage1, may_reproduceable4exps6stage2, pt0)
#################################

class IOps6stage12_4smooth_group_order_method7ring__7uint_mod(IOps6stage12_4smooth_group_order_method7ring__7default_mixin):
    '[pt :: uint%modulus]'
    __slots__ = ()
    @property
    @abstractmethod
    def modulus(sf, /):
        '-> uint{>=2}'
    #@override
    zero = 0
    one = 1
    @override
    def pow_(sf, pt, exp, /):
        return pow(pt, exp, sf.modulus)
    @override
    def square_(sf, pt, exp, /):
        return pow(pt, 2, sf.modulus)
    @override
    def mul_(sf, pt8lhs, pt8rhs, /):
        return pt8lhs * pt8rhs %sf.modulus
    @override
    def diff_one_(sf, pt, /):
        return pt-1 if pt else sf.modulus-1
    @override
    def detect_partial_zero_(sf, pt, /):
        g = gcd(pt, sf.modulus)
        return -1 if g == 1 else (+1 if g == sf.modulus else 0)
check_ABC(IOps6stage12_4smooth_group_order_method7ring__7uint_mod, 'modulus'.split())
class Ops6stage12_4smooth_group_order_method7ring__7uint_mod(IOps6stage12_4smooth_group_order_method7ring__7uint_mod):
    ___no_slots_ok___ = True
    def __init__(sf, modulus, /):
        check_int_ge(2, modulus)
        sf._M = modulus
    @property
    @override
    def modulus(sf, /):
        return sf._M
    def __repr__(sf, /):
        return repr_helper(sf, sf.modulus)
#################################






__all__
from seed.math.factor_pint.smooth_group_order_method import smooth_group_order_method_
#def smooth_group_order_method_(bound4stage1, bound4pow4stage1, bound4stage2, diff_one_, detect_, mul_, may_square_, may_pow_, one, pt0, /, *, num_muls_per_detect, imay_detect_period=0, case4xprimes=None, max_size7dense=2049, max_size7physical=65537):
from seed.math.factor_pint.smooth_group_order_method import search_the_last_used_prime_6stage2_6smooth_group_order_method_, raw_search_the_last_used_prime_6stage2_6smooth_group_order_method_
#def search_the_last_used_prime_6stage2_6smooth_group_order_method_(bound4stage1, bound4pow4stage1, bound4stage2, offset1, offset2, /):
#def raw_search_the_last_used_prime_6stage2_6smooth_group_order_method_(bound4stage1, bound4stage2, delta4offset, /):



from seed.math.factor_pint.smooth_group_order_method import ICommonOps4smooth_group_order_method
from seed.math.factor_pint.smooth_group_order_method import IOps6stage1_4smooth_group_order_method, IOps6stage2_4smooth_group_order_method, IOps6stage2_4smooth_group_order_method7ring, IOps6stage12_4smooth_group_order_method, IOps6stage12_4smooth_group_order_method7ring
from seed.math.factor_pint.smooth_group_order_method import default_search6stage1_, default_search6stage2__7detect_per_step_, default_search6stage2__7ring_, default_search6stage12_, default_search6stage12__7ring_

from seed.math.factor_pint.smooth_group_order_method import ICommonOps4smooth_group_order_method__7default_mixin, IOps6stage1_4smooth_group_order_method__7default_mixin, IOps6stage12_4smooth_group_order_method__7default_mixin, IOps6stage12_4smooth_group_order_method7ring__7default_mixin
from seed.math.factor_pint.smooth_group_order_method import IOps6stage12_4smooth_group_order_method7ring__7uint_mod, Ops6stage12_4smooth_group_order_method7ring__7uint_mod
from seed.math.factor_pint.smooth_group_order_method import *
