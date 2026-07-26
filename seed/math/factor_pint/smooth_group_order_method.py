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
>>>



py_adhoc_call   seed.math.factor_pint.smooth_group_order_method   @f

]]]'''#'''
__all__ = r'''
smooth_group_order_method_



mk_square5may_
mk_pow5may_
CachedPow
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.floor_ceil_tools.fc_log import floor_log2
    from seed.tiny_.check import check_type_is, check_int_ge, check_callable, check_may_
    from seed.tiny_.funcs import echo

    from seed.abc.IReproduceable import Reproduceable7foldl, Reproduceable7rdiff, Reproduceable7tmay_prev_oresult, Reproduceable7fmap
    from seed.types.HistorySaver import mk_history_saver_
    from seed.math.primality_test.reproduceable7probable_primes import mk_Reproduceable7xprimes_
    from seed.math.primality_test.reproduceable7probable_primes import mk_Reproduceable7dup_xprimes__ver2_
    #def mk_Reproduceable7dup_xprimes__ver2_(max4xprime, max4xprime_power, /, *, case=None, mid_args=()):
    from seed.abc.IReproduceable import iter_pairs4reproduceable_, iter_fsts4reproduceable_, iter_snds4reproduceable_
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

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
    if _debug7list_all:
        def _show(d, nm, /):
            v = d[nm]
            print(nm, list(iter_fsts4reproduceable_(v)), sep=':')
            print(nm, v, sep='=')
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
    cached_pow_ = e2pw.__getitem__
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





__all__
from seed.math.factor_pint.smooth_group_order_method import smooth_group_order_method_
#def smooth_group_order_method_(bound4stage1, bound4pow4stage1, bound4stage2, diff_one_, detect_, mul_, may_square_, may_pow_, one, pt0, /, *, num_muls_per_detect, imay_detect_period=0, case4xprimes=None, max_size7dense=2049, max_size7physical=65537):
from seed.math.factor_pint.smooth_group_order_method import *
