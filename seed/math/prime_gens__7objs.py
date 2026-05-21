#__all__:goto
r'''[[[
e ../../python3_src/seed/math/prime_gens__7objs.py

seed.math.prime_gens__7objs
py -m nn_ns.app.debug_cmd   seed.math.prime_gens__7objs -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.prime_gens__7objs:__doc__ -ht # -ff -df
#######

[[
move from:
e ../../python3_src/seed/math/prime_gens.py
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.math.prime_gens__7objs   @f


]]]'''#'''
__all__ = r'''
hold_all_weakrefs4caches_
    prime_gen
    prime_gen__Miller_Rabin_primality_test
    min_prime_factor_gen
    all_prime_factors_gen


GlobalControl4PrimeGenerator__Eratosthenes_sieve
    prime_gen__Eratosthenes_sieve
    prime_gen

GlobalControl4PrimeGenerator__Miller_Rabin_primality_test
    prime_gen__Miller_Rabin_primality_test

GlobalControl4MinPrimeFactorGenerator__Eratosthenes_sieve
    min_prime_factor_gen__Eratosthenes_sieve
    min_prime_factor_gen

GlobalControl4AllPrimeFactorsGenerator__Eratosthenes_sieve
    all_prime_factors_gen__Eratosthenes_sieve
    all_prime_factors_gen

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...




from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__, 'ref:_ref,count:_count'):
    #from operator import __index__
    from weakref import ref as _ref
    from itertools import count as _count
    from itertools import islice, chain


    from seed.debug.print_err import print_err
    from seed.tiny_.funcs import snd
    from seed.tiny_.check import check_type_is, check_int_ge



    from seed.types.LazySeq import LazySeq


    if 1:from seed.math.prime_sieve.sieve_lt import _iter__lt_

    from seed.math.prime_sieve.sieve_lt import raw_iter_all_strict_sorted_primes_, raw_iter_all_strict_sorted_ints__ge2__with_min_prime_factor_

    from seed.math.primality_test.strong_probable_prime import is_prime__tribool_, prime_filter__using_primality_test_
    from seed.math.primality_test.errors import Bool5TriboolFail__probably_prime
        # !! except OverflowError__Miller_Rabin_primality_test__A014233:
        # !! lazy import
        # => not add to __all__ ok


#.#################################
___end_mark_of_excluded_global_names__0___ = ...

class _IBaseGlobalControl4LazySeq:
    #_may_singleton = None
    #_may_wref_singleton = None

    #@abstractmethod
    def _mk_new_lazy_seq_(sf, /):
        raise 000
    def __new__(cls, /):
        #if not cls is __class__: raise TypeError
        while 1:
            try:
                return cls._sf
            except AttributeError:
                pass
            sf = cls._sf = object.__new__(cls)
            sf._may_singleton = None
            sf._may_wref_singleton = None
    def remove_global_singleton_(sf, /):
        'del strong ref to the global lazy_seq if exist'
        sf._may_singleton = None
        #hold sf._may_wref_singleton
    def get_or_mk_global_singleton_(sf, /, *, not_set_global=False):
        '-> LazySeq<x> # get if weak ref exist else mk new lazy_seq (store as strong ref unless not_set_global=True)'
        while 1:
            m = sf._may_singleton
            if not m is None:
                lazy_seq = m
                return lazy_seq
            while 1:
                w = sf._may_wref_singleton
                if not (w is None or w() is None):
                    lazy_seq = w()
                    break
                #weak_ref = w
                #if no_make: return None
                #rebuild:
                lazy_seq = sf._mk_new_lazy_seq_()
                sf._may_wref_singleton = _ref(lazy_seq)
            #end-inner-while 1:
            assert lazy_seq is not None
            if not_set_global:
                return lazy_seq
            sf._may_singleton = lazy_seq
    def get_or_mk_lazy_seq_(sf, /):
        '-> LazySeq<x> # get if weak ref exist else mk new lazy_seq (not store as strong ref)'
        '-> LazySeq<x>'
        lazy_seq = sf.get_or_mk_global_singleton_(not_set_global=True)
        return lazy_seq
    def __call__(sf, /):
        '-> LazySeq<x> # === get_or_mk_lazy_seq_'
        return sf.get_or_mk_lazy_seq_()
    def iter__sized_(sf, sz, /):
        '-> Iter<,>{len=sz}'
        return islice(iter(sf), sz)
    def __bool__(sf, /):
        return True
    #__bool__ = ...
    __len__ = ...
    __contains__ = ...

    def __iter__(sf, /):
        '-> Iter<x>{len=+oo}'
        return iter(sf[...]) #del lazy_seq, hold LazyList tail only
        return iter(sf()) # hold lazy_seq
    def __getitem__(sf, i_or_sl_or_3dot, /):
        'i -> x; i:j -> [x]; ... -> LazyList<x>'
        if i_or_sl_or_3dot is ...:
            return sf().the_lazylist
        i_or_sl = i_or_sl_or_3dot
        return sf()[i_or_sl]
        if type(i_or_sl) is slice:
            sl = i_or_sl
            return sf()[sl]
        if type(i_or_sl) is int:
            i = i_or_sl
            return sf()[i]
        raise TypeError(type(i_or_sl))
class _IBaseGlobalControl4PrimeGenerator(_IBaseGlobalControl4LazySeq):
    #_may_singleton = None
    #_may_wref_singleton = None

    #@abstractmethod
    #def _mk_new_lazy_seq_(sf, /):
    ...

    def get_or_mk_lazy_prime_seq_(sf, /):
        '-> LazySeq<prime> # get if weak ref exist else mk new lazy_prime_seq (not store as strong ref)'
        '-> LazySeq<prime>'
        lazy_seq = sf.get_or_mk_lazy_seq_()
        return lazy_seq
    def iter__lt_(sf, end, /):
        '-> Iter<prime{<end}>'
        return _iter__lt_(end, iter(sf))
    def iter__ge_(sf, begin, /):
        '-> Iter<prime{>=begin}>'
        check_type_is(int, begin)
        if begin <= 2:
            return iter(sf)
        lazylist = sf[...]
        it = lazylist.iter__hardwork(to_iter_pairs=True)
        for prime, tail in it:
            if not prime < begin:
                break
            lazylist = tail # del lazylist to free memory
        return iter(lazylist)
    def __bool__(sf, /):
        return True
    __len__ = ...
    def __contains__(sf, x, /):
        'using is_prime__using_A014233_/is_prime__tribool_'
        check_type_is(int, x)
        #r = is_prime__tribool_(x, case=Case4is_prime__tribool_.II_prime_basis_gtN)
        r = is_prime__tribool_(x, case=None)
        if r is ...:
            raise Bool5TriboolFail__probably_prime(x)
        return r

class GlobalControl4PrimeGenerator__Eratosthenes_sieve(_IBaseGlobalControl4PrimeGenerator):
    'using Eratosthenes_sieve'
    #@override
    def _mk_new_lazy_seq_(sf, /):
        it = raw_iter_all_strict_sorted_primes_(to_cache_only_busy_primes_plus_next=True, may_primes=None)
        lazy_seq = LazySeq(it)
        return lazy_seq

class GlobalControl4PrimeGenerator__Miller_Rabin_primality_test(_IBaseGlobalControl4PrimeGenerator):
    'using Miller_Rabin_primality_test; not inf long, halt between [2**81..<2**82]'
    #@override
    def _mk_new_lazy_seq_(sf, /):
        it = prime_filter__using_primality_test_(_count(2))
        lazy_seq = LazySeq(it)
        return lazy_seq



prime_gen__Eratosthenes_sieve = GlobalControl4PrimeGenerator__Eratosthenes_sieve()
prime_gen__Miller_Rabin_primality_test = GlobalControl4PrimeGenerator__Miller_Rabin_primality_test()
prime_gen = prime_gen__Eratosthenes_sieve





#class StableReprDict(dict):
#    def __repr__(sf, /):
#        return stable_repr(dict(sf))

class GlobalControl4MinPrimeFactorGenerator__Eratosthenes_sieve(_IBaseGlobalControl4LazySeq):
    'using Eratosthenes_sieve'
    #see:GlobalControl4PrimeGenerator__Eratosthenes_sieve
    #@override
    def _mk_new_lazy_seq_(sf, /):
        it = raw_iter_all_strict_sorted_ints__ge2__with_min_prime_factor_(to_cache_only_busy_primes_plus_next=True, may_primes=None)
        it = map(snd, it)
        it = chain([None, None], it)
        lazy_seq = LazySeq(it)
        return lazy_seq
    def __bool__(sf, /):
        return True
    def get_or_mk_lazy_min_prime_factor_seq_(sf, /):
        '-> LazySeq<may min_prime_factor> # get if weak ref exist else mk new lazy_seq (not store as strong ref)'
        lazy_seq = sf.get_or_mk_lazy_seq_()
        return lazy_seq
min_prime_factor_gen__Eratosthenes_sieve = GlobalControl4MinPrimeFactorGenerator__Eratosthenes_sieve()
min_prime_factor_gen = min_prime_factor_gen__Eratosthenes_sieve


class GlobalControl4AllPrimeFactorsGenerator__Eratosthenes_sieve(_IBaseGlobalControl4LazySeq):
    'using Eratosthenes_sieve'
    #see:GlobalControl4MinPrimeFactorGenerator__Eratosthenes_sieve
    #@override
    def _mk_new_lazy_seq_(sf, /):
        def u2ps_(u, /):
            #优化冫复用小对象
            #assert sf() is lazy_seq, (sf(), lazy_seq)
            ps4u = lazy_seq[u]
            #print_err(u, ps4u, sep=':')
            return ps4u

        it = raw_iter_all_strict_sorted_ints__ge2__with_min_prime_factor_(to_cache_only_busy_primes_plus_next=True, may_primes=None, to_export_all_prime_factors=True, may_uint2all_prime_factors_=u2ps_)
            #bug:why fail to pass u2ps_? bug@LazySeq fixed
        it = map(snd, it)
        it = chain([None, ()], it)
        lazy_seq = LazySeq(it)
        return lazy_seq
    def __bool__(sf, /):
        return True
    def get_or_mk_lazy_all_prime_factors_seq_(sf, /):
        '-> LazySeq<may all_prime_factors> # get if weak ref exist else mk new lazy_seq (not store as strong ref)'
        lazy_seq = sf.get_or_mk_lazy_seq_()
        return lazy_seq
all_prime_factors_gen__Eratosthenes_sieve = GlobalControl4AllPrimeFactorsGenerator__Eratosthenes_sieve()
all_prime_factors_gen = all_prime_factors_gen__Eratosthenes_sieve








#class









######################
#@20250419
def _filter4globals_(is_ok_, _globals=None, /):
    nms = []
    xs = []
    if _globals is None:
        _globals = globals()
    for nm, x in sorted(_globals.items()):
        if not is_ok_(nm, x):
            continue
        nms.append(nm)
        xs.append(x)
    nms = tuple(nms)
    xs = tuple(xs)
    return (nms, xs)
_IBaseGlobalControl4LazySeq.get_or_mk_lazy_seq_
def _prepare4hold_all_weakrefs4caches_():
    'all:instance:_IBaseGlobalControl4LazySeq'
    def is_ok_(nm, x, /):
        return isinstance(x, _IBaseGlobalControl4LazySeq)
    (nms, xs) = _filter4globals_(is_ok_)
    for x in xs:
        x.get_or_mk_lazy_seq_()
    return (nms, xs)
if 0:
    _data4hold_all_weakrefs4caches_ = _prepare4hold_all_weakrefs4caches_()
    assert (__:='\n'.join(_data4hold_all_weakrefs4caches_[0])) == (r'''
all_prime_factors_gen
all_prime_factors_gen__Eratosthenes_sieve
min_prime_factor_gen
min_prime_factor_gen__Eratosthenes_sieve
prime_gen
prime_gen__Eratosthenes_sieve
prime_gen__Miller_Rabin_primality_test
'''.strip()), __
    ('all_prime_factors_gen', 'all_prime_factors_gen__Eratosthenes_sieve', 'min_prime_factor_gen', 'min_prime_factor_gen__Eratosthenes_sieve', 'prime_gen', 'prime_gen__Eratosthenes_sieve', 'prime_gen__Miller_Rabin_primality_test')
    assert (__:=len(_data4hold_all_weakrefs4caches_[0])) == 7, __
_data4hold_all_weakrefs4caches_ = (r'''
    prime_gen
    prime_gen__Miller_Rabin_primality_test
    min_prime_factor_gen
    all_prime_factors_gen
'''.split()#'''
,
    (prime_gen
    ,prime_gen__Miller_Rabin_primality_test
    ,min_prime_factor_gen
    ,all_prime_factors_gen
    )
)
assert (__:=len(_data4hold_all_weakrefs4caches_[0])) == 4, __
#@20250419
def hold_all_weakrefs4caches_():
    '-> tuple<weakref<lazy_seq>> # to replace 『lazy_prime_seq = prime_gen.get_or_mk_lazy_prime_seq_()』' \
    ' # all:instance:_IBaseGlobalControl4LazySeq.get_or_mk_lazy_seq_'
    (nms, xs) = _data4hold_all_weakrefs4caches_
    ws = tuple(x.get_or_mk_lazy_seq_() for x in xs)
    return ws
#hold_all_weakrefs4caches_()






__all__
if 1:from seed.math.prime_gens__7objs import _filter4globals_
    #used in seed.math.prime_gens:_helper4renaming_probable_prime_()
from seed.math.prime_gens__7objs import (
hold_all_weakrefs4caches_
,   prime_gen
,   prime_gen__Miller_Rabin_primality_test
,   min_prime_factor_gen
,   all_prime_factors_gen
#
#
,GlobalControl4PrimeGenerator__Eratosthenes_sieve
,   prime_gen__Eratosthenes_sieve
,   prime_gen
#
,GlobalControl4PrimeGenerator__Miller_Rabin_primality_test
,   prime_gen__Miller_Rabin_primality_test
#
,GlobalControl4MinPrimeFactorGenerator__Eratosthenes_sieve
,   min_prime_factor_gen__Eratosthenes_sieve
,   min_prime_factor_gen
#
,GlobalControl4AllPrimeFactorsGenerator__Eratosthenes_sieve
,   all_prime_factors_gen__Eratosthenes_sieve
,   all_prime_factors_gen
)

from seed.math.prime_gens__7objs import hold_all_weakrefs4caches_, prime_gen, prime_gen__Miller_Rabin_primality_test, min_prime_factor_gen, all_prime_factors_gen

from seed.math.prime_gens__7objs import *
