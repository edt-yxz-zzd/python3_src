#__all__:goto
r'''[[[
e ../../python3_src/seed/math/RhoDetector.py
rho_detector

seed.math.RhoDetector
py -m nn_ns.app.debug_cmd   seed.math.RhoDetector -x
py -m nn_ns.app.doctest_cmd seed.math.RhoDetector:__doc__ -ff -v
py_adhoc_call   seed.math.RhoDetector   @f
[[
view /sdcard/0my_files/tmp/out4py/py_src/sympy-ntheory-factor_.py
    pollard_rho(...)
    #Pollard's rho method
view /sdcard/0my_files/tmp/out4py/py_src/sympy-ntheory-generate.py
    cycle_length()
    loop_length >= 1
    leader_length >= 0
]]


######################
>>> _obj2next_ = lambda x: (x*x +1)%51

######################
>>> [*iterate(_obj2next_, 4, 10)] # 10 == 3+6+1
[4, 17, 35, 2, 5, 26, 14, 44, 50, 2]
>>> [*RhoLeaderFinder(_obj2next_).iterate_(4, 10)]
[4, 17, 35, 2, 5, 26, 14, 44, 50, 2]
>>> [*islice(RhoLeaderFinder(_obj2next_).iterate_(4), 10)]
[4, 17, 35, 2, 5, 26, 14, 44, 50, 2]

######################
>>> RhoLeaderFinder(_obj2next_).search_rho_leader_and_loop_length_(4)
(3, 6)

######################
>>> search_rho_leader_and_loop_length_(_obj2next_, 4)
(3, 6)

>>> search_rho_loop_length_(_obj2next_, 4)
6

>>> search_rho_leader_length_(_obj2next_, 4, 0)
3
>>> search_rho_leader_length_(_obj2next_, 4, 6)
3

######################
>>> imay_search_rho_leader_length_(_obj2next_, 4, 6, None)
3
>>> imay_search_rho_leader_length_(_obj2next_, 4, 6, 10) # 10 == 3+1+6 # calc_necessary_min_num_enumerate4rho_leader_length__known_period_
3
>>> imay_search_rho_leader_length_(_obj2next_, 4, 6, 9)
-1

>>> omay_search_rho_loop_length_(_obj2next_, 4, None)
6
>>> omay_search_rho_loop_length_(_obj2next_, 4, 14) # 14 == 8+6 == ceil_zpow_(max{6,1+3})+6 # calc_necessary_min_num_enumerate4period_
6
>>> omay_search_rho_loop_length_(_obj2next_, 4, 13)
0

>>> may_search_rho_leader_and_loop_length_(_obj2next_, 4, None)
(3, 6)
>>> may_search_rho_leader_and_loop_length_(_obj2next_, 4, 14)
(3, 6)
>>> may_search_rho_leader_and_loop_length_(_obj2next_, 4, 13) is None
True


######################
>>> x0 = 0
>>> mk_obj2next_ = lambda rho_leader_length, period, /: lambda x: rho_leader_length if x+1 == rho_leader_length+period else x+1 # <<== [x0==0]
>>> def validate_(rho_leader_length, period, /):
...     # O(rho_leader_length+period)
...     assert rho_leader_length >= 0
...     assert period >= 1
...     _obj2next_ = mk_obj2next_(rho_leader_length, period)
...     assert (result := search_rho_leader_and_loop_length_(_obj2next_, x0)) == (rho_leader_length, period), ((rho_leader_length, period), result)
...         # O(necessary_min_num_enumerate4period<x0>)*(_obj2next_+eq4obj)
...         # O(rho_leader_length+period)*(_obj2next_+eq4obj)
...         # O(NNN)*(_obj2next_+eq4obj)
...     necessary_min_num_enumerate4rho_leader_length__known_period = calc_necessary_min_num_enumerate4rho_leader_length__known_period_(rho_leader_length, period)
...     necessary_min_num_enumerate4period = calc_necessary_min_num_enumerate4period_(rho_leader_length, period)
...     assert 2 <= necessary_min_num_enumerate4rho_leader_length__known_period <= necessary_min_num_enumerate4period
...     assert imay_search_rho_leader_length_(_obj2next_, x0, period, necessary_min_num_enumerate4rho_leader_length__known_period) == rho_leader_length
...     assert imay_search_rho_leader_length_(_obj2next_, x0, period, necessary_min_num_enumerate4rho_leader_length__known_period-1) == -1
...     assert omay_search_rho_loop_length_(_obj2next_, x0, necessary_min_num_enumerate4period) == period
...     assert omay_search_rho_loop_length_(_obj2next_, x0, necessary_min_num_enumerate4period-1) == 0
>>> def validates_(NNN, /):
...     # O(NNN**3)
...     for rho_leader_length in range(NNN):
...         for period in range(1, NNN):
...             validate_(rho_leader_length, period)
...                 # O(NNN)
>>> validates_(18) # [3*18**3 == 17496]     #doctest: +SKIP
>>> validates_(10) # [3*10**3 == 3000]

######################
>>> calc_necessary_min_num_enumerate4period_(63, 64)
128
>>> calc_necessary_min_num_enumerate4period_(63+1, 64)
192
>>> calc_necessary_min_num_enumerate4period_(63, 64+1)
193
>>> calc_necessary_min_num_enumerate4period_(63, 64-1)
127
>>> calc_necessary_min_num_enumerate4period_(63, 64-63) == 128-63
True
>>> calc_necessary_min_num_enumerate4period_(63-1, 64)
128
>>> calc_necessary_min_num_enumerate4period_(0, 64)
128
>>> validate_(63, 64)
>>> validate_(63+1, 64)
>>> validate_(63, 64+1)
>>> validate_(0, 64)
>>> validate_(63, 1)

######################

#]]]'''
__all__ = r'''
RhoPeriodDetector
RhoLeaderFinder
    search_rho_leader_and_loop_length_
    search_rho_loop_length_
    search_rho_leader_length_

    calc_necessary_min_num_enumerate4rho_leader_length__known_period_
        imay_search_rho_leader_length_
    calc_necessary_min_num_enumerate4period_
        omay_search_rho_loop_length_
        may_search_rho_leader_and_loop_length_


RhoCommon__key
    RhoPeriodDetector
        RhoPeriodDetector__5RhoCommon__key
    IRhoCommon__next
        IRhoLeaderFinder
            RhoLeaderFinder
Error
    Error__feed_after_finish
    Error__feed0_after_feed
    Error__feed1_before_feed0

'''.split()#'''
__all__



from itertools import islice
from seed.iters.iterate import iterate

from seed.tiny import check_type_le
from seed.tiny_.check import check_int_ge
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.helper.repr_input import repr_helper
from seed.math.floor_ceil import ceil_log2 as ceil_log2_

class RhoCommon__key:
    __slots__ = ()
    def _obj2key_(sf, x, /):
        'x -> k'
        k = x
        return k
    def _eq4key_(sf, lkey, rkey, /):
        '__eq__<k>'
        return lkey == rkey
    def eq4obj(sf, xL, xR, /):
        x2k = sf._obj2key_
        return sf._eq4key_(x2k(xL), x2k(xR))
class IRhoCommon__next(RhoCommon__key, ABC):
    __slots__ = ()
    @abstractmethod
    def _obj2next_(sf, x, /):
        'x -> x'
        _x = x
        return _x



class Error(Exception):pass
class Error__feed_after_finish(Error):pass
class Error__feed0_after_feed(Error):pass
class Error__feed1_before_feed0(Error):pass

def calc_necessary_min_num_enumerate4rho_leader_length__known_period_(rho_leader_length, period, /):
    necessary_min_num_enumerate4rho_leader_length__known_period = rho_leader_length + 1 + period
    return necessary_min_num_enumerate4rho_leader_length__known_period
def calc_necessary_min_num_enumerate4period_(rho_leader_length, period, /):
    # [:howto_calc_necessary_min_num_enumerate4period]:goto
        # [necessary_min_num_enumerate_(rho_leader_length, period) == period + 2**ceil_log2_(max(period,1+rho_leader_length))]
    necessary_min_num_enumerate4period = period + (1 << ceil_log2_(max(period,1+rho_leader_length)))
    return necessary_min_num_enumerate4period

class RhoPeriodDetector(RhoCommon__key):
    r'''[[[
    rho_period_detector
    ######################
    [sz4saved_x == 1+i4saved_x]
    [i4saved_x0 := 0]
    [sz4saved_x0 == 1]
    ######################
    [period > max_period4saved_x]:
        [new_i4saved_x := old_i4saved_x + old_max_period4saved_x]
        [new_max_period4saved_x := 2*old_max_period4saved_x]
    ######################
    n   i4saved_x<n>    max_period4saved_x<n>
    0   0               1
    1   1               2
    2   3               4
    ...
    ==>> [max_period4saved_x == i4saved_x+1]
    !! [sz4saved_x == 1+i4saved_x]
    [max_period4saved_x == i4saved_x+1 == sz4saved_x == 2**?] #zpow
    [max_period4saved_x == sz4saved_x]
    ######################
    !! [new_i4saved_x := old_i4saved_x + old_max_period4saved_x]
    !! [sz4saved_x == 1+i4saved_x]
    [new_sz4saved_x == old_sz4saved_x + old_max_period4saved_x]
    !! [max_period4saved_x == sz4saved_x]
    [old_max_period4saved_x == old_sz4saved_x]
    [new_sz4saved_x == 2*old_sz4saved_x]
    [[n :<- [0..]] -> [sz4saved_x<n+1> == 2*sz4saved_x<n>]]
    !! [sz4saved_x0 == 1]
    [[n :<- [0..]] -> [sz4saved_x<n> == 2**n]]
    !! [sz4saved_x == 1+i4saved_x]
    [[n :<- [0..]] -> [i4saved_x<n> == 2**n -1]]
    ######################
    necessary_min_num_enumerate_(rho_leader_length, period)
    [sz4saved_x<n+1> >= sz4curr_x > sz4saved_x<n> >= 1]
    [sz4curr_x == necessary_min_num_enumerate_(rho_leader_length, period)]:
        !! [necessary min ...]
        [sz4curr_x == sz4saved_x<n> + period]
        !! [sz4saved_x<n+1> >= sz4curr_x > sz4saved_x<n> >= 1]
        [sz4saved_x<n+1> >= sz4saved_x<n> + period > sz4saved_x<n> >= 1]
        [sz4saved_x<n+1> -sz4saved_x<n> >= period > 0]
        !! [[n :<- [0..]] -> [sz4saved_x<n> == 2**n]]
        [0 < period <= 2**n]
        !! [no more new_sz4saved_x]
        [period <= max_period4saved_x]
        !! [max_period4saved_x == sz4saved_x]
        [period <= sz4saved_x<n> == 2**n]
        !! [saved_x MUST be in loop/cycle]
        [rho_leader_length < sz4saved_x<n>]
        [sz4saved_x<n> >= max(period,1+rho_leader_length)]
        !! [[n :<- [0..]] -> [sz4saved_x<n> == 2**n]]
        !! [necessary min ...]
        [n == ceil_log2_(max(period,1+rho_leader_length))]
        [sz4saved_x<n> == 2**ceil_log2_(max(period,1+rho_leader_length))]
        !! [sz4curr_x == sz4saved_x<n> + period]
        [sz4curr_x == period + 2**ceil_log2_(max(period,1+rho_leader_length))]
        !! [sz4curr_x == necessary_min_num_enumerate_(rho_leader_length, period)]
        [necessary_min_num_enumerate_(rho_leader_length, period) == period + 2**ceil_log2_(max(period,1+rho_leader_length))]
    [necessary_min_num_enumerate_(rho_leader_length, period) == period + 2**ceil_log2_(max(period,1+rho_leader_length))]
        # [:howto_calc_necessary_min_num_enumerate4period]:here
    ######################
    ######################
    #]]]'''#'''
    @property
    def omay_period(sf, /):
        return sf._omay_period
    def __init__(sf, /):
        sf.restart()
    def restart(sf, /):
        '-> None'
        sf._sz = 0
        sf._omay_period = 0
        sf._x_sz_k = None
    def _feed0(sf, x0, /):
        # O(1)*_obj2key_
        if sf.is_finished_(): raise Error__feed_after_finish
        if sf.is_started_(): raise Error__feed0_after_feed
        ######################
        k0 = sf._obj2key_(x0)
        max_period4x0 = sz4x0 = 1
        ######################
        sf._omay_period = 0
        sf._sz = sz4x0
        sf._x_sz_k = (x0, sz4x0, k0)
            # (x_, sz_, k_)
            #   #saved version #snapshot
            # (x, sz, k) => [x is xs[sz-1]][k == _obj2key_(x)]
        ######################

    def is_finished_(sf, /):
        return not sf.omay_period == 0
    def is_started_(sf, /):
        return not sf._x_sz_k is None


    def feeds(sf, xs, /, *, restart=False):
        '-> omay_period/uint/(0|period/loop_length/pint) | noreturn/endless_enumerate'
        # O(min{len(xs), necessary_min_num_enumerate4period<saved_x0> -sf._sz})*eq4obj
        xs = iter(xs)
        if restart:
            sf.restart()

        if not sf.is_finished_():
            for x in xs:
                # --> endless_enumerate
                #print(f'x={x}')
                if sf.feed(x):
                    # O(1)*eq4obj
                    #print(x, sf.omay_period)
                    break
        return sf.omay_period

    def feed(sf, x, /):
        '-> omay_period/uint/(0|period/loop_length/pint)'
        # O(1)*eq4obj
        if sf.is_finished_(): raise Error__feed_after_finish
        if not sf.is_started_():
            sf._feed0(x)
                # O(1)*_obj2key_
            assert not sf.is_finished_()
        else:
            sf._feed1(x)
                # O(1)*eq4obj
        return sf.omay_period

    def _feed1(sf, x, /):
        # O(1)*eq4obj
        if sf.is_finished_(): raise Error__feed_after_finish
        if not sf.is_started_(): raise Error__feed1_before_feed0
        (x_, sz_, k_) = sf._x_sz_k
            # None => raise ...

        k = sf._obj2key_(x)
        same = sf._eq4key_(k_, k)
        i = sf._sz # [x is xs[i]]
        sz = sf._sz = i+1
        if same:
            period = sz - sz_
            assert period > 0
            sf._omay_period = period
        elif sz == (sz_<<1):
            #print(f'(x, sz, k)={(x, sz, k)}')
            sf._x_sz_k = (x, sz, k)
        return
class RhoPeriodDetector__5RhoCommon__key(RhoPeriodDetector):
    @override
    def _obj2key_(sf, x, /):
        'x -> k'
        k = sf._key4rho._obj2key_(x)
        return k
    @override
    def _eq4key_(sf, lkey, rkey, /):
        '__eq__<k>'
        return sf._key4rho._eq4key_(lkey, rkey)
    def __init__(sf, a_RhoCommon__key, /):
        check_type_le(RhoCommon__key, a_RhoCommon__key)
            #e.g. IRhoLeaderFinder
        sf._key4rho = a_RhoCommon__key
        super().__init__()

class IRhoLeaderFinder(IRhoCommon__next):
    #rho_leader_finder
    #required:period
    __slots__ = ()
    def iterate_(sf, x0, /, *args4islice):
        return iterate(sf._obj2next_, x0, *args4islice)

    def omay_search_rho_loop_length_(sf, x0, may_max_num_enumerate, /):
        'x0 -> may_max_num_enumerate -> omay_period/uint | noreturn/endless_enumerate'
        # O(min{ifNone(may_max_num_enumerate, inf), necessary_min_num_enumerate4period<x0>})*(_obj2next_+eq4obj)
        xs = sf.iterate_(x0, may_max_num_enumerate)
            #islice
            # O(min{ifNone(may_max_num_enumerate, inf), necessary_min_num_enumerate4period<x0>})*_obj2next_
        omay_period = RhoPeriodDetector__5RhoCommon__key(sf).feeds(xs)
            # --> endless_enumerate
            # O(min{ifNone(may_max_num_enumerate, inf), necessary_min_num_enumerate4period<x0>})*eq4obj
        assert omay_period >= 0
        return omay_period
    def imay_search_rho_leader_length_(sf, x0, period, may_max_num_enumerate, /):
        'x0 -> period/pint -> may_max_num_enumerate -> imay rho_leader_length/[-1..] | noreturn/endless_enumerate'
        # O(min{ifNone(may_max_num_enumerate, inf), rho_leader_length<x0>+1+period})*_obj2next_ +O(min{ifNone(may_max_num_enumerate, inf), rho_leader_length<x0>+1})*eq4obj
        check_int_ge(1, period)
        xs = sf.iterate_(x0, may_max_num_enumerate)
        _xs = islice(xs, period, None)
            # O(min{ifNone(may_max_num_enumerate, inf), necessary_min_num_enumerate4rho_leader_length__known_period<x0>})*_obj2next_
            # O(min{ifNone(may_max_num_enumerate, inf), rho_leader_length<x0>+1+period})*_obj2next_

        #xxx:None:xs = sf.iterate_(x0, may_max_num_enumerate-period)
        xs = sf.iterate_(x0, may_max_num_enumerate)
            # O(min{ifNone(may_max_num_enumerate, inf), necessary_min_num_enumerate4rho_leader_length__known_period<x0> -period})*_obj2next_
            # O(min{ifNone(may_max_num_enumerate, inf), rho_leader_length<x0>+1})*_obj2next_
        for i, stop in enumerate(map(sf.eq4obj, xs, _xs)):
            # --> endless_enumerate
            # O(min{ifNone(may_max_num_enumerate, inf), rho_leader_length<x0>+1})*eq4obj
            if stop:
                rho_leader_length = i
                imay_rho_leader_length = rho_leader_length
                break
        else:
            imay_rho_leader_length = -1
        return imay_rho_leader_length
    def may_search_rho_leader_and_loop_length_(sf, x0, may_max_num_enumerate, /):
        'x0 -> may_max_num_enumerate -> may (rho_leader_length/uint, period/pint) | noreturn/endless_enumerate'
        # O(min{ifNone(may_max_num_enumerate, inf), necessary_min_num_enumerate4period<x0>})*(_obj2next_+eq4obj)
        omay_period = sf.omay_search_rho_loop_length_(x0, may_max_num_enumerate)
            # --> endless_enumerate
            # O(min{ifNone(may_max_num_enumerate, inf), necessary_min_num_enumerate4period<x0>})*(_obj2next_+eq4obj)
        if not omay_period == 0:
            period = omay_period
            rho_leader_length = sf.imay_search_rho_leader_length_(x0, period, may_max_num_enumerate)
                # MUST stop
                # O(rho_leader_length<x0>+1+period)*_obj2next_ +(rho_leader_length<x0>+1)*eq4obj
            assert rho_leader_length >= 0
            return (rho_leader_length, period)
        else:
            return None

    def search_rho_loop_length_(sf, x0, /):
        'x0 -> period/pint | noreturn/endless_enumerate'
        # O(necessary_min_num_enumerate4period<x0>)*(_obj2next_+eq4obj)
        period = sf.omay_search_rho_loop_length_(x0, None)
            # --> endless_enumerate
            # O(min{ifNone(may_max_num_enumerate, inf), necessary_min_num_enumerate4period<x0>})*(_obj2next_+eq4obj)
        assert period > 0
        return period
    def search_rho_leader_length_(sf, x0, omay_period, /):
        'x0 -> omay_period/uint -> rho_leader_length/uint | noreturn/endless_enumerate'
        # [omay_period > 0] => O(rho_leader_length<x0>+1+period)*_obj2next_ +(rho_leader_length<x0>+1)*eq4obj
        # [omay_period == 0] => O(necessary_min_num_enumerate4period<x0>)*(_obj2next_+eq4obj)
        check_int_ge(0, omay_period)
        if omay_period == 0:
            period = sf.search_rho_loop_length_(x0)
                # --> endless_enumerate
                # O(necessary_min_num_enumerate4period<x0>)*(_obj2next_+eq4obj)
        else:
            period = omay_period
        assert period > 0
        rho_leader_length = sf.imay_search_rho_leader_length_(x0, period, None)
            # --> endless_enumerate
            # O(rho_leader_length<x0>+1+period)*_obj2next_ +(rho_leader_length<x0>+1)*eq4obj
        assert rho_leader_length > 0
        return rho_leader_length
    def search_rho_leader_and_loop_length_(sf, x0, /):
        'x0 -> (rho_leader_length/uint, period/pint) | noreturn/endless_enumerate'
        # O(necessary_min_num_enumerate4period<x0>)*(_obj2next_+eq4obj)
        (rho_leader_length, period) = sf.may_search_rho_leader_and_loop_length_(x0, None)
            # --> endless_enumerate
            # O(necessary_min_num_enumerate4period<x0>)*(_obj2next_+eq4obj)
        return (rho_leader_length, period)

        period = sf.search_rho_loop_length_(x0)
            # --> endless_enumerate
        rho_leader_length = sf.search_rho_leader_length_(x0, period)
            # MUST stop
        return (rho_leader_length, period)

class RhoLeaderFinder(IRhoLeaderFinder):
    ___no_slots_ok___ = True
    def __init__(sf, _obj2next_, /):
        sf._obj2next = _obj2next_
    @property
    @override
    #def _obj2next_(sf, x, /):
    def _obj2next_(sf, /):
        'x -> x'
        return sf._obj2next
def search_rho_leader_and_loop_length_(_obj2next_, x0, /):
    'Eq x => (x -> x) -> x0 -> (rho_leader_length/uint, period/pint) | noreturn/endless_enumerate'
    # O(necessary_min_num_enumerate4period<x0>)*(_obj2next_+eq4obj)
    sf = RhoLeaderFinder(_obj2next_)
    (rho_leader_length, period) = sf.search_rho_leader_and_loop_length_(x0)
        # --> endless_enumerate
    return (rho_leader_length, period)
def search_rho_loop_length_(_obj2next_, x0, /):
    'Eq x => (x -> x) -> x0 -> period/pint | noreturn/endless_enumerate'
    # O(necessary_min_num_enumerate4period<x0>)*(_obj2next_+eq4obj)
    sf = RhoLeaderFinder(_obj2next_)
    period = sf.search_rho_loop_length_(x0)
        # --> endless_enumerate
    return period
def search_rho_leader_length_(_obj2next_, x0, omay_period, /):
    'Eq x => (x -> x) -> x0 -> omay_period/uint -> rho_leader_length/uint | noreturn/endless_enumerate'
    # [omay_period > 0] => O(rho_leader_length<x0>+1+period)*_obj2next_ +(rho_leader_length<x0>+1)*eq4obj
    # [omay_period == 0] => O(necessary_min_num_enumerate4period<x0>)*(_obj2next_+eq4obj)
    sf = RhoLeaderFinder(_obj2next_)
    rho_leader_length = sf.search_rho_leader_length_(x0, omay_period)
        # --> endless_enumerate
    return rho_leader_length




def omay_search_rho_loop_length_(_obj2next_, x0, may_max_num_enumerate, /):
    'Eq x => (x -> x) -> x0 -> may_max_num_enumerate -> omay_period/uint | noreturn/endless_enumerate'
    # O(min{ifNone(may_max_num_enumerate, inf), necessary_min_num_enumerate4period<x0>})*(_obj2next_+eq4obj)
    sf = RhoLeaderFinder(_obj2next_)
    omay_period = sf.omay_search_rho_loop_length_(x0, may_max_num_enumerate)
        # --> endless_enumerate
    return omay_period
def imay_search_rho_leader_length_(_obj2next_, x0, period, may_max_num_enumerate, /):
    'Eq x => (x -> x) -> x0 -> period/pint -> may_max_num_enumerate -> imay rho_leader_length/[-1..] | noreturn/endless_enumerate'
    # O(min{ifNone(may_max_num_enumerate, inf), rho_leader_length<x0>+1+period})*_obj2next_ +O(min{ifNone(may_max_num_enumerate, inf), rho_leader_length<x0>+1})*eq4obj
    sf = RhoLeaderFinder(_obj2next_)
    imay_rho_leader_length = sf.imay_search_rho_leader_length_(x0, period, may_max_num_enumerate)
        # --> endless_enumerate
    return imay_rho_leader_length
def may_search_rho_leader_and_loop_length_(_obj2next_, x0, may_max_num_enumerate, /):
    'Eq x => (x -> x) -> x0 -> may_max_num_enumerate -> may (rho_leader_length/uint, period/pint) | noreturn/endless_enumerate'
    # O(min{ifNone(may_max_num_enumerate, inf), necessary_min_num_enumerate4period<x0>})*(_obj2next_+eq4obj)
    sf = RhoLeaderFinder(_obj2next_)
    may_rho_pair = sf.may_search_rho_leader_and_loop_length_(x0, may_max_num_enumerate)
        # --> endless_enumerate
    return may_rho_pair


r'''[[[
class IRhoDetector(ABC):
    #raise NotImplementedError
    #___no_slots_ok___ = True
    def __repr__(sf, /):
        #return repr_helper(sf, *args, **kwargs)
        #return repr_helper_ex(sf, args, ordered_attrs, kwargs, ordered_attrs_only=False)
        ...
#]]]'''#'''
if __name__ == "__main__":
    pass
__all__


from seed.math.RhoDetector import RhoPeriodDetector, RhoLeaderFinder
from seed.math.RhoDetector import search_rho_loop_length_, search_rho_leader_length_, search_rho_leader_and_loop_length_
from seed.math.RhoDetector import omay_search_rho_loop_length_, imay_search_rho_leader_length_, may_search_rho_leader_and_loop_length_
from seed.math.RhoDetector import calc_necessary_min_num_enumerate4period_, calc_necessary_min_num_enumerate4rho_leader_length__known_period_

from seed.math.RhoDetector import *
