#__all__:goto
r'''[[[
e ../../python3_src/seed/math/discrete_logarithm.py
view others/数学/整数分解/sqrts_mod_.txt
view ../../python3_src/seed/math/find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_.py


seed.math.discrete_logarithm
py -m nn_ns.app.debug_cmd   seed.math.discrete_logarithm -x
py -m nn_ns.app.doctest_cmd seed.math.discrete_logarithm:__doc__ -ht # -ff -v
py_adhoc_call   seed.math.discrete_logarithm   @f


from seed.math.discrete_logarithm import discrete_logarithm__coprime_
    #def discrete_logarithm__coprime_(modulus, base, order_of_base, factorization_of_order_of_base, y, /)

**2 %17:
    2,15@-2 --> 4 --> 16 --> 1
    3,14@-3 --> 9@-8 --> 13@-4
    5,12@-5 --> 8
    6,11@-6 --> 2
    7,10@-7 --> 15@-2
    1; 16; 4,13; 2,15,8,9; 6,11,7,10,5,12,3,14.
>>> discrete_logarithm__coprime_(17, 3, 16, {2:4}, 3)
1
>>> discrete_logarithm__coprime_(17, 3, 16, {2:4}, 14)
9
>>> discrete_logarithm__coprime_(17, 3, 16, {2:4}, 12)
13
>>> discrete_logarithm__coprime_(17, 3, 16, {2:4}, 9)
2
>>> discrete_logarithm__coprime_(17, 3, 16, {2:4}, 2)
14
>>> discrete_logarithm__coprime_(17, 3, 16, {2:4}, 4)
12
>>> discrete_logarithm__coprime_(17, 3, 16, {2:4}, 13)
4
>>> discrete_logarithm__coprime_(17, 3, 16, {2:4}, 16)
8
>>> discrete_logarithm__coprime_(17, 3, 16, {2:4}, 1)
0

>>> all(pow(3, discrete_logarithm__coprime_(17, 3, 16, {2:4}, y), 17) == y for y in range(1,17))
True


>>> [*_iter_sorted_primitive_roots_mod_prime_(17, {2:4})]
[3, 5, 6, 7, 10, 11, 12, 14]
>>> _find_arbitrary_one_primitive_root_mod_prime_(17, {2:4})
3
>>> [*_iter_sorted_primitive_roots_mod_prime_(101, {2:2, 5:2})]
[2, 3, 7, 8, 11, 12, 15, 18, 26, 27, 28, 29, 34, 35, 38, 40, 42, 46, 48, 50, 51, 53, 55, 59, 61, 63, 66, 67, 72, 73, 74, 75, 83, 86, 89, 90, 93, 94, 98, 99]
>>> _find_arbitrary_one_primitive_root_mod_prime_(101, {2:2, 5:2})
2

>>> discrete_logarithm__coprime_(101, 2, 100, {2:2, 5:2}, 66)
83
>>> all(pow(55, discrete_logarithm__coprime_(101, 55, 100, {2:2, 5:2}, y), 101) == y for y in range(1,101))
True



view ../../python3_src/seed/math/_output_/seed.math.iter_sorted_products_of_uints..iter_unsorted_primes_lt__prime_eq_one_plus_product_generated_by_strict_sorted_pairwise_coprime_uints_.2-3-5.out.txt
9001
1459
11251
65537
2552526178459920315627553
###>>> from seed.math.load_data.some_smooth_primes import SmoothPrime__base_2_3_5__lt_3317044064679887385962123 as SmP #.smooth_primes__sorted, .prime_bases, .smooth_prime__cofactorization__pairs____sorted, .maxpp
###>>> ps = SmP.smooth_prime__cofactorization__pairs____sorted
###>>> first_ = lambda i:max(ps, key=lambda pair:pair[1][i])
###>>> last_ = lambda i:max(ps, key=lambda pair:(pair[1][i], pair[0]))
###>>> for i,p in enumerate(SmP.prime_bases):(p, first_(i), last_(i))
###(2, (188894659314785808547841, (75, 0, 1)), (188894659314785808547841, (75, 0, 1)))
###(3, (2552526178459920315627553, (5, 48, 0)), (2552526178459920315627553, (5, 48, 0)))
###(5, (698491930961608886718751, (1, 1, 33)), (698491930961608886718751, (1, 1, 33)))
>>> 2**75 * 3**0 * 5**1  +1
188894659314785808547841
>>> 2**5 * 3**48 * 5**0  +1
2552526178459920315627553
>>> 2**1 * 3**1 * 5**33  +1
698491930961608886718751
>>> _find_arbitrary_one_primitive_root_mod_prime_(188894659314785808547841, {2:75, 5:1})
3
>>> _find_arbitrary_one_primitive_root_mod_prime_(2552526178459920315627553, {2:5, 3:48})
5
>>> _find_arbitrary_one_primitive_root_mod_prime_(698491930961608886718751, {2:1, 3:1, 5:33})
7

>>> discrete_logarithm__coprime_(188894659314785808547841, 3, 188894659314785808547841-1, {2:75, 5:1}, 2)
121786100960625210227710
>>> discrete_logarithm__coprime_(2552526178459920315627553, 5, 2552526178459920315627553-1, {2:5, 3:48}, 2)
290768012625521935241520
>>> discrete_logarithm__coprime_(698491930961608886718751, 7, 698491930961608886718751-1, {2:1, 3:1, 5:33}, 2)
584743671391082143362096

>>> pow(3, 121786100960625210227710, 188894659314785808547841)
2
>>> pow(5, 290768012625521935241520, 2552526178459920315627553)
2
>>> pow(7, 584743671391082143362096, 698491930961608886718751)
2


#]]]'''
__all__ = r'''
discrete_logarithm__coprime_
    uint2iter_idc4two_pows_

IDefaultLookupable
    IDefaultLookupable__generate
        Lookupable__bijection
        IDefaultLookupable__seq
            Lookupable__pows
            Lookupable__Tpows
            Lookupable__Ppows_2pows

'''.split()#'''
#find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_
#    find_the_min_primitive_root_mod_prime__using_factorization_of_pmm_
#        iter_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_
#
#_find_arbitrary_one_primitive_root_mod_prime_
#    _find_the_min_primitive_root_mod_prime_
#        _iter_sorted_primitive_roots_mod_prime_
__all__
___begin_mark_of_excluded_global_names__0___ = ...

#from math import isqrt as floor_sqrt_
from seed.tiny import print_err, mk_fprint, mk_assert_eq_f, expectError
from seed.math.floor_ceil import floor_sqrt as floor_sqrt_
from seed.math.floor_ceil import floor_log2

from seed.math.II import II, II_mod, II__p2e_
from seed.math.inv_mod_ import inv_mod_

from seed.math.Chinese_Remainder_Theorem import CRT, ECRT, mk_CRT, apply_CRT, apply_CRT__pairs, check_CRT_ans, CRT_Answer_Error
from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le

#move to: view ../../python3_src/seed/math/find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_.py
if 1:from seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_ import _find_arbitrary_one_primitive_root_mod_prime_, _find_the_min_primitive_root_mod_prime_, _iter_sorted_primitive_roots_mod_prime_
#from seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_ import find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_, find_the_min_primitive_root_mod_prime__using_factorization_of_pmm_, iter_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_
___end_mark_of_excluded_global_names__0___ = ...

def _API():
    #API:
    def find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, may_p=None, /):
        'factorization{p-1} -> may p -> arbitrary primitive_root%p'
    def find_the_min_primitive_root_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, may_p=None, /):
        'factorization{p-1} -> may p -> min primitive_root%p'
    def iter_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_(factorization_of_pmm, may_p=None, /):
        'factorization{p-1} -> may p -> sorted-Iter primitive_root%p'


    def _find_arbitrary_one_primitive_root_mod_prime_(p, factorization_of_pmm, /):
        'p -> factorization{p-1} -> arbitrary primitive_root%p'
    def _find_the_min_primitive_root_mod_prime_(p, factorization_of_pmm, /):
        'p -> factorization{p-1} -> min primitive_root%p'
    def _iter_sorted_primitive_roots_mod_prime_(p, factorization_of_pmm, /):
        'p -> factorization{p-1} -> sorted-Iter primitive_root%p'
_API




def _detect_easy_case4discrete_logarithm__coprime_(modulus, base, order_of_base, y, /):
    '-> (x|...)'
    while 1: # not loop, just for 'break'
        if y == 1:
            x = 0
            break
        # [y =!= 1]
        # !! [y >= 1]
        # [y >= 2]
        # !! [y < modulus]
        # [modulus >= 3]

        # !! [y =!= 1]
        # [x =!= 0]
        # !! [0 <= x < order_of_base]
        # [1 <= x < order_of_base]
        # [order_of_base >= 2]
        assert order_of_base >= 2

        if y == modulus -1:
            # !! [modulus >= 3]
            # [order_mod_(modulus; -1) == 2]
            # !! [y == modulus -1]
            # [order_mod_(modulus; y) == 2]
            # !! [y**order_of_base %modulus == 1]
            # [order_of_base%2 == 0]
            assert order_of_base&1 == 0, (modulus, base, order_of_base, y)
            x = order_of_base >> 1
            break
        # [2 <= y <= modulus -2]
        # [modulus >= 4]
        if y == base:
            x = 1
            break
        # [x =!= 1]
        # !! [1 <= x < order_of_base]
        # [2 <= x < order_of_base]
        # [order_of_base >= 3]
        # [1 <= (order_of_base >> 1) <= order_of_base-2]
        # [0 <= (order_of_base >> 1) -1 < (order_of_base >> 1) +1 <= order_of_base-1]
        if y == modulus -base:
            assert order_of_base&1 == 0
            # !! [0 <= (order_of_base >> 1) -1 < (order_of_base >> 1) +1 <= order_of_base-1]
            x = (order_of_base >> 1) +1
            break


        yb = y*base %modulus
        if yb == 1:
            x = order_of_base -1
            break
        # [x =!= order_of_base -1]
        # !! [2 <= x < order_of_base]
        # [2 <= x <= order_of_base-2]
        # [order_of_base >= 4]
        if yb == modulus -1:
            assert order_of_base&1 == 0
            # !! [0 <= (order_of_base >> 1) -1 < (order_of_base >> 1) +1 <= order_of_base-1]
            x = (order_of_base >> 1) -1
            break
        # [2 <= y <= modulus -2]
        # [modulus >= 4]
        # [2 <= x <= order_of_base-2]
        # [order_of_base >= 4]
        assert 2 <= y <= modulus -2
        assert order_of_base >= 4
        return ...
    #end-while 1: # not loop, just for 'break'
    return x
#end-def _detect_easy_case4discrete_logarithm__coprime_(modulus, base, order_of_base, y, /):

def discrete_logarithm__coprime_(modulus, base, order_of_base, factorization_of_order_of_base, y, /):
    r'''[[[
    :: modulus -> base -> order_of_base -> factorization_of_order_of_base -> y -> x/int%order_of_base

    precondition:
        [modulus >= 2]
        [1 <= base < modulus]
        [1 <= order_of_base <= phi(M) < M]
        [factorization_of_order_of_base :: {prime:exp/int{>=1}}]
        [1 <= y < modulus]
        [gcd(modulus, base) == 1]
        [gcd(modulus, y) == 1]
        [@[e :<- [1..<order_of_base]] -> [base**e %modulus =!= 1]]
        [base**order_of_base %modulus == 1]
        [phi(M)%order_of_base == 0]
        [order_of_base == II__p2e_(factorization_of_order_of_base)]
        ######################
        [y**order_of_base %modulus == 1]
        [?[e :<- [1..=order_of_base]] -> [base**e %modulus == y]]
        ######################

    postcondition:
        [0 <= x < order_of_base]
        [base**x %modulus == y]


    SPACE = O(max((p + ep + ep**(1/2) *log2(p)) for p,ep in factorization_of_order_of_base.items())) *space_per_word<modulus>
        # _discrete_logarithm__coprime__order_of_base_is_odd_prime_power_:
        # p_pows => O(ep)
        # y_Ppows => O(ep)
        # y_000_2exp/y_000_5exp => O(p)
        # idcs4patch_P2pows => O(max_sz_per_block *log2(p))
        #   # if [num_blocks ~= max_sz_per_block ~= k1**0.5]: [O(size(idcs4patch_P2pows)) ~= O(k1**0.5 *log2(p)) <= O(ep**0.5 *log2(p))]
        # patch_P2pows => O(k1*log2(p)) <= O(ep*log2(p))
        #

    TIME = O(sum((p + ep**(3/2) *log2(p)) for p,ep in factorization_of_order_of_base.items())) *time_per_mul_mod<modulus>
        # _discrete_logarithm__coprime__order_of_base_is_odd_prime_power_:
        #   [k1 <= ep]
        #
        #   init p_pows, y_Ppows, y_000_2exp/y_000_5exp => O(ep+p)
        # _cut__num_blocks_(num_blocks, k1)
        #   outer loop: total num_blocks rounds
        #   inner loop: total k1 rounds
        #   inner body: per round: O(size(idcs4patch_P2pows))
        #   outer body exclude inner loop: per round: O(size(idcs4patch_P2pows) + size(patch_P2pows))
        # total ~= O(init) + num_blocks*O(size(idcs4patch_P2pows) + size(patch_P2pows)) + k1*O(size(idcs4patch_P2pows))
        #
        #   [size(patch_P2pows) ~= O(k1*log2(p))]
        #   [size(idcs4patch_P2pows) ~= O(max_sz_per_block*log2(p))]
        #   [0 <= max_sz_per_block*num_blocks - k1 < min(max_sz_per_block, num_blocks)]
        # total ~= O(ep+p) + num_blocks*O(max_sz_per_block*log2(p) + k1*log2(p)) + k1*O(max_sz_per_block*log2(p))
        # total ~= O(ep+p) + O((k1+num_blocks)*max_sz_per_block + num_blocks*k1)*log2(p)
        # total ~= O(ep+p) + O((k1+num_blocks)*(k1/num_blocks) + num_blocks*k1)*log2(p)
        # total ~= O(ep+p) + O(k1**2/num_blocks + (1+num_blocks)*k1)*log2(p)
        # if [num_blocks ~= O(k1**0.5)]:
        #   total ~= O(ep+p) + O(k1**1.5)*log2(p)
        #   total ~= O(p + ep**1.5*log2(p))
        #
        #
        # if [num_blocks ~= O(log2(p**k1)**0.5)]:
        #   total ~= O(p + (log2(p**ep)**1.5))
        #


    #]]]'''#'''
    check_int_ge(2, modulus)
    check_int_ge_lt(1, modulus, base)
    check_int_ge_lt(1, modulus, order_of_base)
    check_int_ge_lt(1, modulus, y)
    for p, ep in factorization_of_order_of_base.items():
        check_int_ge_le(2, order_of_base, p)
        check_int_ge_lt(1, order_of_base, ep)
    for p in factorization_of_order_of_base:
        if not ((p&1) == 1 or p==2): raise ValueError(p)

    if not II__p2e_(factorization_of_order_of_base) == order_of_base: raise ValueError((order_of_base, factorization_of_order_of_base))

    p2e = factorization_of_order_of_base
    while 1: # not loop, just for 'break'
        ######################
        x_or_3dot = _detect_easy_case4discrete_logarithm__coprime_(modulus, base, order_of_base, y)
        if not x_or_3dot is ...:
            x = x_or_3dot
            break
        # [2 <= y <= modulus -2]
        # [modulus >= 4]
        # [2 <= x <= order_of_base-2]
        # [order_of_base >= 4]
        ######################


        assert factorization_of_order_of_base
        pe_xp_pairs = []
        if 2 in p2e:
            e2 = p2e[2]
            e_ = order_of_base>>e2
            g_ = pow(base, e_, modulus)
            y_ = pow(y, e_, modulus)
            x2 = _discrete_logarithm__coprime__order_of_base_is_even_prime_power_(modulus, g_, e2, y_)
            pe = 1<<e2
            pe_xp_pairs.append((pe, x2))

        for p, ep in sorted(factorization_of_order_of_base.items()):
            if p == 2: continue
            pe = p**ep
            e_ = order_of_base //pe
            g_ = pow(base, e_, modulus)
            y_ = pow(y, e_, modulus)
            xp = _discrete_logarithm__coprime__order_of_base_is_odd_prime_power_(modulus, g_, pe, p, ep, y_)
            pe_xp_pairs.append((pe, xp))
        pe_xp_pairs
        assert pe_xp_pairs
        assert len(pe_xp_pairs) == len(p2e)
        if len(pe_xp_pairs) == 1:
            [(pe, xp)] = pe_xp_pairs
            x = xp
        else:
            x = apply_CRT__pairs(pe_xp_pairs, extended=False)
        x

        break
    #end-while 1: # not loop, just for 'break'
    x

    if 0b01:
        assert 0 <= x < order_of_base
        assert pow(base, x, modulus) == y
    check_int_ge_lt(0, order_of_base, x)
    return x
#end-def discrete_logarithm__coprime_(modulus, base, order_of_base, factorization_of_order_of_base, y, /):
def _discrete_logarithm__coprime__order_of_base_is_even_prime_power_(modulus, base, e2, y, /):
    '[order_of_base == 2**e2]'
    assert e2 > 0
    p = 2
    order_of_base = 1<<e2
    while 1: # not loop, just for 'break'
        ######################
        x_or_3dot = _detect_easy_case4discrete_logarithm__coprime_(modulus, base, order_of_base, y)
        if not x_or_3dot is ...:
            x = x_or_3dot
            break
        # [2 <= y <= modulus -2]
        # [modulus >= 4]
        # [2 <= x <= order_of_base-2]
        # [order_of_base >= 4]
        ######################

        if y == 1:
            x = 0
            break
        # [y =!= 1]

        def get_patch_2pows_(e, /):
            assert 0 <= e < k1
            return patch_2pows[e]
        def get_y_2pows_(e, /):
            assert 0 <= e <= e2
            return y_2pows[e]
        def get_patch_(e, /):
            ls = [get_patch_2pows_(k+e) for k in idc4patch_2pows]
            patch_ = II_mod(modulus, ls)
            #   patch_ is shifted patch
            return patch_
        def get_y_000_(e, /):
            y_ = get_y_2pows_(e)
            # [y_ == y**(2**e) %M]
            patch_ = get_patch_(e)
            y_000_ = y_ * patch_ %modulus
            # [y_000 == (y*patch_base**sum(2**k for k in idc4patch_2pows)) %M]
            #   y_000 is patched y
            # [y_000_ == y_000**(2**e) %M]
            #   y_000_ is shifted (patched y)
            return y_000_
        y_2pows = Lookupable__Tpows([y], e2+1, modulus, 2)

        # !! [y**order_of_base %modulus == 1]
        if not 1 == get_y_2pows_(e2): raise ValueError((modulus, e2, y))
        k1 = y_2pows._lookupable_.index(1)
        # !! [y =!= 1]
        # [k1 =!= 0]
        # [1 <= k1 <= e2]
        max_sz_per_block = floor_sqrt_(k1)
        assert max_sz_per_block >= 1


        exp4patch_base = 1 << (e2-k1)
        patch_base = pow(base, exp4patch_base, modulus)
        patch_2pows = Lookupable__Tpows([patch_base], k1, modulus, 2)
            # [patch_base == patch_2pows[0] == base**exp4patch_base %modulus]
        idc4patch_2pows = []
            #idc8patch

        if 0b00:
            assert patch_base == patch_2pows[0] == pow(base, exp4patch_base, modulus)
        for begin, szX in _cut__max_sz_per_block_(max_sz_per_block, k1):
            for j in range(begin, begin+szX):
                e = k1-1-j
                y_000_ = get_y_000_(e)
                if y_000_ == 1:
                    continue
                #patch:
                #idx4y_2pows = j+(e2-k1)
                idx4y_2pows = j
                idc4patch_2pows.append(idx4y_2pows)
                if 0b01:
                    assert 1 == get_y_000_(e)
            if idc4patch_2pows:
                # y patched
                if len(idc4patch_2pows) >= 2 or j==k1-1:
                    patch = get_patch_(0)
                    patch_base = patch
                    patch_2pows = Lookupable__Tpows([patch_base], k1, modulus, 2)
                    exp4patch_base = exp4patch_base * sum(1 << k for k in idc4patch_2pows) %order_of_base
                        # [patch_base == patch_2pows[0] == base**exp4patch_base %modulus]
                    if 0b00:
                        assert patch_base == patch_2pows[0] == pow(base, exp4patch_base, modulus), (base, exp4patch_base, pow(base, exp4patch_base, modulus), patch_base, patch_2pows)
                    idc4patch_2pows = [0]
                        # y patched
                    if 0b01:
                        assert 1 == get_y_000_(e)


        if idc4patch_2pows:
            # y patched
            if 0b00:
                assert idc4patch_2pows == [0]
                assert 1 == get_y_000_(e)
            assert 0 < exp4patch_base < order_of_base
            x = order_of_base -exp4patch_base
            assert 0 < x < order_of_base
        else:
            x = 0
            # !! [y =!= 1]
            raise 000
        break
    #end-while 1: # not loop, just for 'break'
    x
    if 0b01:
        assert 0 <= x < order_of_base
        assert pow(base, x, modulus) == y, ((base, x, modulus), pow(base, x, modulus), y)
    return x
#end-def _discrete_logarithm__coprime__order_of_base_is_even_prime_power_(modulus, base, e2, y, /):
def uint2iter_idc4two_pows_(exp, /):
    bs = bin(exp)[:1:-1]
    for i, b in enumerate(bs):
        if b == '1':
            yield i
assert [*uint2iter_idc4two_pows_(0)] == []
assert [*uint2iter_idc4two_pows_(1)] == [0]
assert [*uint2iter_idc4two_pows_(0b10)] == [1]
assert [*uint2iter_idc4two_pows_(0b11)] == [0,1]
assert [*uint2iter_idc4two_pows_(0b100)] == [2]
assert [*uint2iter_idc4two_pows_(0b101)] == [0,2]
def _cut__num_blocks_(num_blocks, n, /):
    assert num_blocks >= 0
    assert n >= 0
    assert (n == 0) is (num_blocks == 0)
    if num_blocks == 0:
        ps = []
    else:
        sz0, num1 = divmod(n, num_blocks)
        sz1 = sz0+1
        num0 = num_blocks-num1
        assert sz0*num0 +sz1*num1 == n
        max_sz_per_block = (n-1)//num_blocks +1
        assert max(max_sz_per_block*(num_blocks-1), (max_sz_per_block-1)*num_blocks) < n <= max_sz_per_block*num_blocks
        assert num0 + num1 == num_blocks == (n-1)//max_sz_per_block +1
        assert 0 < sz0 < sz1 == max_sz_per_block if num1 else 0 < sz0 == max_sz_per_block < sz1
        ps = [(num0, sz0), (num1, sz1)]
            # num1 may be 0
    begin = 0
    for numX, szX in ps:
        for _ in range(numX):
            yield begin, szX
            begin += szX
    return

def _cut__max_sz_per_block_(max_sz_per_block, n, /):
    assert max_sz_per_block > 0
    assert n >= 0
    num_blocks = (n-1)//max_sz_per_block +1
    return _cut__num_blocks_(num_blocks, n)

class IDefaultLookupable:
    r'''[[[
    _generate_
    _lookupable_
    _args_
    _kwds_
    #]]]'''#'''
    def __len__(sf, /):
        return len(sf._lookupable_)
    def __getitem__(sf, k, /):
        try:
            return sf._lookupable_[k]
        except LookupError:
            sf._generate_(k, sf._lookupable_, *sf._args_, **sf._kwds_)
        return sf._lookupable_[k]
    if 0:
        @property
        def _lookupable_(sf, /):
            raise 000
        @property
        def _args_(sf, /):
            raise 000
        @property
        def _kwds_(sf, /):
            raise 000
        def _generate_(sf, k, _lookupable_, /, *_args_, **_kwds_):
            raise 000
class IDefaultLookupable__generate(IDefaultLookupable):
    r'''[[[
    _generate_
    #]]]'''#'''
    def __init__(sf, _lookupable_, /, *_args_, **_kwds_):
        sf._lookupable_ = _lookupable_
        sf._args_ = _args_
        sf._kwds_ = _kwds_


r'''[[[
class DefaultLookupable(IDefaultLookupable):
    def __init__(sf, _generate_, _lookupable_, /, *_args_, **_kwds_):
        sf._generate_ = _generate_
        sf._lookupable_ = _lookupable_
        sf._args_ = _args_
        sf._kwds_ = _kwds_
#]]]'''#'''

class IDefaultLookupable__seq(IDefaultLookupable__generate):
    r'''[[[
    _mk_next_
    #]]]'''#'''
    def __init__(sf, ls, maxpp4k, /, *_args_, **_kwds_):
        super().__init__(ls, maxpp4k, *_args_, **_kwds_)
    def _generate_(sf, k, ls, maxpp4k, /, *_args_, **_kwds_):
        if not 0 <= k < maxpp4k: raise LookupError(k)
        if not k < len(ls):
            for _ in range(k+1-len(ls)):
                xxx = sf._mk_next_(ls, *_args_, **_kwds_)
                ls.append(xxx)
        #return ls[k]
    def _mk_next_(sf, ls, /, *_args_, **_kwds_):
        raise 000

class Lookupable__pows(IDefaultLookupable__seq):
    def __init__(sf, ls, maxpp4k, modulus, /):
        ls[1]
        super().__init__(ls, maxpp4k, modulus)
    def _mk_next_(sf, ls, modulus, /):
        xxx = ls[1]
        return ((ls[-1]*xxx)% modulus)

class Lookupable__bijection(IDefaultLookupable__generate):
    #y_000_2exp
    def __init__(sf, inv_dict, ls, /):
        if not isinstance(ls, IDefaultLookupable__seq): raise TypeError
        if not len(ls) == len(inv_dict): raise ValueError
        super().__init__(inv_dict, ls)
    def _generate_(sf, zzz, inv_dict, ls, /):
        if not len(ls) == len(inv_dict): raise logic-err
        #while len(ls) < maxpp4k:
        while 1:
            xxx = ls[len(ls)]
            inv_dict[xxx] = len(inv_dict)
            if not len(ls) == len(inv_dict): raise logic-err
            if zzz == xxx:
                break
        #return ls[k]





class Lookupable__Tpows(IDefaultLookupable__seq):
    def __init__(sf, ls, maxpp4k, modulus, T, /):
        assert T >= 2
        ls[0]
        super().__init__(ls, maxpp4k, modulus, T)
    def _mk_next_(sf, ls, modulus, T, /):
        return pow(ls[-1], T, modulus)



class Lookupable__Ppows_2pows(IDefaultLookupable__seq):
    def __init__(sf, lsls, maxpp4kp, modulus, p, /):
        assert p >= 3
        lsls[0][0]
        bit_idc4p = (*uint2iter_idc4two_pows_(p),)
        maxpp4k2 = bit_idc4p[-1] +1
        assert maxpp4k2 == floor_log2(p) +1
        #maxpp4k2 = floor_log2(p) +1
        #xxx_Ppows = Lookupable__Tpows([ls[0] for ls in lsls], maxpp4kp, modulus, p)
        for i in range(len(lsls)):
            ls = lsls[i]
            if not isinstance(ls, Lookupable__Tpows):
                lsls[i] = Lookupable__Tpows(ls, maxpp4k2, modulus, 2)
        super().__init__(lsls, maxpp4kp, modulus, p, maxpp4k2, bit_idc4p)
    def _mk_next_(sf, lsls, modulus, p, maxpp4k2, bit_idc4p, /):
        ls = lsls[-1]
        us = (ls[i] for i in bit_idc4p)
        xxx_P_kp_ = II_mod(modulus, us)
                # == ls[0]**p %M
                # == lsls[0][0]**(p**kp) %M
                # == xxx**(p**kp) %M
        zzz_2pows = Lookupable__Tpows([xxx_P_kp_], maxpp4k2, modulus, 2)
        return zzz_2pows



def _discrete_logarithm__coprime__order_of_base_is_odd_prime_power_(modulus, base, order_of_base, p, ep, y, /):
    '[order_of_base == p**ep]'
    assert p&1
    while 1: # not loop, just for 'break'
        ######################
        x_or_3dot = _detect_easy_case4discrete_logarithm__coprime_(modulus, base, order_of_base, y)
        if not x_or_3dot is ...:
            x = x_or_3dot
            break
        # [2 <= y <= modulus -2]
        # [modulus >= 4]
        # [2 <= x <= order_of_base-2]
        # [order_of_base >= 4]
        ######################

        if y == 1:
            x = 0
            break
        # [y =!= 1]


        def iter_get_patch_P2pows_(e, idcs4patch_P2pows, /):
            # [@[kp :<- [0..<k1]] -> @[k2 :<- [0..=floor_log2(p)]] -> [patch_P2pows[kp][k2] == patch_base**((p**kp)*(2**k2))]]
            #see:get_patch_()
            assert 0 <= e < k1
            assert 0 <= e+len(idcs4patch_P2pows) <= k1
            assert all(0 <= idx <= floor_log2_p for kp, idc in idcs4patch_P2pows for idx in idc)
                    # inout___idcs4patch_P2pows
            #for kp, idc in enumerate(idcs4patch_P2pows, e):
            for kp, idc in idcs4patch_P2pows:
                    # inout___idcs4patch_P2pows
                ls = patch_P2pows[kp+e]
                for k2 in idc:
                    yield ls[k2]
        def get_y_Ppows_(e, /):
            assert 0 <= e <= ep
            return y_Ppows[e]
        def get_p_pows_(e, /):
            assert 0 <= e <= ep # [1 <= k1 <= ep]
                # p_k1 = get_p_pows_(k1) # == p**k1
                # p_j = get_p_pows_(idx4y_Ppows) # == p**j
            return p_pows[e]

        def get_patch_(e, /):
            #idc4patch_2pows --> idcs4patch_P2pows
            us = iter_get_patch_P2pows_(e, idcs4patch_P2pows)
            patch_ = II_mod(modulus, us)
            #   patch_ is shifted patch
            return patch_
        def get_y_000_(e, /):
            y_ = get_y_Ppows_(e)
            # [y_ == y**(p**e) %M]
            patch_ = get_patch_(e)
            y_000_ = y_ * patch_ %modulus
            # [y_000 == (y*patch_base**sum(p**kp * 2**k2 for kp, idc in enumerate(idcs4patch_P2pows) for k2 in idc)) %M]
            #   y_000 is patched y
            # [y_000_ == y_000**(p**e) %M]
            #   y_000_ is shifted (patched y)
            return y_000_


        def exp5y_000_(y_000_, /):
            assert not y_000_ == 1
            return y_000_2exp[y_000_]

        p_pows = Lookupable__pows([1, p], ep+1, modulus)
        y_Ppows = Lookupable__Tpows([y], ep+1, modulus, p)

        base_Pepmm = pow(base, get_p_pows_(ep-1), modulus) # == base**(p**(ep-1))
        y_000_2exp = Lookupable__bijection({1:0, base_Pepmm:1}, Lookupable__pows([1, base_Pepmm], p, modulus))

        # !! [y**order_of_base %modulus == 1]
        if not 1 == get_y_Ppows_(ep): raise ValueError((modulus, ep, y))
        k1 = y_Ppows._lookupable_.index(1)
        # !! [y =!= 1]
        # [k1 =!= 0]
        # [1 <= k1 <= ep]
        ######################
        #below setting [num_blocks := k1**0.5]
        ######################
        # [1 <= k1 <= ep]
        num_blocks = floor_sqrt_(k1)
        # !! [k1 >= 1]
        # [1 <= num_blocks <= k1]
        # [num_blocks ~= O(k1**0.5)]
        max_sz_per_block = (k1-1)//num_blocks +1
        # [max_sz_per_block == ceil(k1/num_blocks)]
        # !! [1 <= num_blocks <= k1]
        # [max_sz_per_block >= 1]
        assert max_sz_per_block >= 1
        assert num_blocks >= 1
        assert max_sz_per_block >= num_blocks >= 1
        assert 0 <= max_sz_per_block*num_blocks -k1 < min(max_sz_per_block, num_blocks)

        # [max_sz_per_block ~= O(k1/k1**0.5) ~= O(k1**0.5) ~= num_blocks]

        floor_log2_p = floor_log2(p)
        idcs4patch_P2pows = []
            #idc8patch
        assert len(idcs4patch_P2pows) <= max_sz_per_block
            # [len(idcs4patch_P2pows) <= max_sz_per_block]
            # @k. [len(idcs4patch_P2pows[k]) <= floor_log2_p]
            # [size(idcs4patch_P2pows) ~= O(max_sz_per_block*log2(p))]




        ######################
        exp4patch_base0 = get_p_pows_(ep-k1) # == p**(ep-k1)
        patch_base0 = pow(base, exp4patch_base0, modulus)
            # [patch_base0 === base**exp4patch_base0 %modulus]
            # [exp4patch_base0 === p**(ep-k1)]
            # [patch_base0 === base**(p**(ep-k1)) %modulus]

        exp4patch_base = exp4patch_base0
        patch_base = patch_base0

        patch_P2pows = Lookupable__Ppows_2pows([[patch_base]], k1, modulus, p)
            # [@[kp :<- [0..<k1]] -> @[k2 :<- [0..=floor_log2(p)]] -> [patch_P2pows[kp][k2] == patch_base**((p**kp)*(2**k2))]]
            # [patch_base == patch_P2pows[0][0] == base**exp4patch_base %modulus]
            # [exp4patch_base%exp4patch_base0 == 0][exp4patch_base///exp4patch_base0 %p =!= 0]
            # [patch_base == patch_base0**(exp4patch_base///exp4patch_base0) %modulus]
            #
        exp4patch5patch_base = 0
            # [patch == patch_base**exp4patch5patch_base %modulus]
        inv_exp0 = 1
            # final-constraint: [inv_exp0 == inv_mod_(p;(exp4patch_base///p**(ep-k1))%p)]
            #   <<== source-constraint: @u. [base**(p**(ep-1) *u) =[%modulus]= patch_base**(p**(k1-1) *u*inv_exp0)]
            ######################
            # @u. [base**(p**(ep-1) *u) =[%modulus]= patch_base**(p**(k1-1) *u*inv_exp0)]
            # !! [patch_base == base**exp4patch_base %modulus]
            # [base**(p**(ep-1) *u) =[%modulus]= base**(p**(k1-1) *u*inv_exp0*exp4patch_base)]
            # [(p**(ep-1) *u) =[%order_of_base]= (p**(k1-1) *u*inv_exp0*exp4patch_base)]
            # !! [order_of_base == p**ep]
            # [(p**(ep-1) *u) =[%p**ep]= (p**(k1-1) *u*inv_exp0*exp4patch_base)]
            # !! [exp4patch_base%exp4patch_base0 == 0]
            # !! [exp4patch_base0 === p**(ep-k1)]
            # [(p**(ep-1) *u) =[%p**ep]= (p**(ep-1) *u*inv_exp0*(exp4patch_base///exp4patch_base0))]
            # [(u) =[%p]= (u*inv_exp0*(exp4patch_base///exp4patch_base0))]
            # !! u is arbitrary
            # [1 =[%p]= (inv_exp0*(exp4patch_base///exp4patch_base0))]
            # !! [exp4patch_base%exp4patch_base0 == 0][exp4patch_base///exp4patch_base0 %p =!= 0]
            # [inv_exp0 == inv_mod_(p;(exp4patch_base///exp4patch_base0)%p)]
            # [inv_exp0 == inv_mod_(p;(exp4patch_base///p**(ep-k1))%p)]
            #
        if 0b00:
            assert patch_base == patch_P2pows[0][0] == pow(base, exp4patch_base, modulus)
        for begin, szX in _cut__num_blocks_(num_blocks, k1):
            assert 0 <= max_sz_per_block -szX <= 1
            for j in range(begin, begin+szX):
                e = k1-1-j
                y_000_ = get_y_000_(e)
                if y_000_ == 1:
                    assert not j == 0
                    continue
                #patch:
                idx4y_Ppows = j
                p_j = get_p_pows_(idx4y_Ppows) # == p**j

                exp4y_000_5base = exp5y_000_(y_000_)
                # [1 <= exp4y_000_5base < p]
                delta_exp4patch5base = p -exp4y_000_5base
                # [1 <= delta_exp4patch5base < p]
                # [delta_exp4patch5base%p =!= 0]

                # !! @u. [base**(p**(ep-1) *u) =[%modulus]= patch_base**(p**(k1-1) *u*inv_exp0)]
                #   [u := delta_exp4patch5base]
                digit = (delta_exp4patch5base*inv_exp0 %p)
                delta_exp4patch5patch_base = digit *p_j
                # !! [inv_exp0 == inv_mod_(p;(exp4patch_base///p**(ep-k1))%p)]
                # [inv_exp0%p =!= 0]
                # !! [delta_exp4patch5base%p =!= 0]
                # [delta_exp4patch5patch_base///p**j %p =!= 0]
                # [[j==0] <-> [delta_exp4patch5patch_base%p =!= 0]]

                old = exp4patch5patch_base, idcs4patch_P2pows
                # !! [[j==0] <-> [old-exp4patch5patch_base%p == 0]]
                # !! [[j==0] <-> [delta_exp4patch5patch_base%p =!= 0]]
                assert 0 <= exp4patch5patch_base < p_j
                exp4patch5patch_base = (exp4patch5patch_base + delta_exp4patch5patch_base) # %p_k1
                    # [patch == patch_base**exp4patch5patch_base %modulus]
                #assert p_j <= exp4patch5patch_base < p_k1
                # [new-exp4patch5patch_base%p =!= 0]

                assert len(idcs4patch_P2pows) <= j + (idcs4patch_P2pows[:1] == [(0, [0])])
                idcs4patch_P2pows.append((j, [*uint2iter_idc4two_pows_(digit)]))
                    # inout___idcs4patch_P2pows

                assert len(idcs4patch_P2pows) <= max_sz_per_block + (idcs4patch_P2pows[:1] == [(0, [0])])
                    # [len(idcs4patch_P2pows) <= max_sz_per_block]
                assert len(idcs4patch_P2pows[-1][-1]) <= floor_log2_p
                    # inout___idcs4patch_P2pows
                    # @k. [len(idcs4patch_P2pows[k]) <= floor_log2_p]

                if 0b01:
                    # old := exp4patch5patch_base, idcs4patch_P2pows
                    assert 1 == get_y_000_(e)
            #end-for j in range(begin, begin+szX):
            #outer loop: regenerate patch_P2pows<new-patch_base>
            if idcs4patch_P2pows:
                # y patched
                if len(idcs4patch_P2pows) >= 2 or j==k1-1:
                #if 1:
                    to_update__inv_exp0 = patch_base is patch_base0
                    patch = get_patch_(0)
                    patch_base = patch
                    patch_P2pows = Lookupable__Ppows_2pows([[patch_base]], k1, modulus, p)
                    exp4patch_base = exp4patch_base * exp4patch5patch_base %order_of_base
                        # [patch_base == patch_P2pows[0][0] == base**exp4patch_base %modulus]
                    assert not exp4patch5patch_base %p == 0
                        # !! [new-exp4patch5patch_base%p =!= 0]
                        # [exp4patch_base%exp4patch_base0 == 0][exp4patch_base///exp4patch_base0 %p =!= 0]
                    exp4patch5patch_base = 1
                        # [patch == patch_base**exp4patch5patch_base %modulus]
                    if 0b00:
                        assert patch_base == patch_P2pows[0][0] == pow(base, exp4patch_base, modulus), (base, exp4patch_base, pow(base, exp4patch_base, modulus), patch_base, patch_P2pows)
                    idcs4patch_P2pows = [(0, [0])]
                        # inout___idcs4patch_P2pows
                        # y patched
                    assert len(idcs4patch_P2pows) <= max_sz_per_block
                        # [len(idcs4patch_P2pows) <= max_sz_per_block]
                    if 0b01:
                        assert 1 == get_y_000_(e)
                    if to_update__inv_exp0:
                        #"update inv_exp0" at most once
                        inv_exp0 = inv_mod_(p, (exp4patch_base//exp4patch_base0)%p)


        if idcs4patch_P2pows:
        #if exp4patch5patch_base:
            # y patched
            if 0b00:
                #bug:assert idcs4patch_P2pows == [0]
                #   old: if len(idcs4patch_P2pows) >= 2:
                #   now: if len(idcs4patch_P2pows) >= 2 or j==k1-1:
                #   bug fixed!
                assert idcs4patch_P2pows == [(0, [0])], ((modulus, base, order_of_base, y), idcs4patch_P2pows)
                    # inout___idcs4patch_P2pows
                assert 1 == get_y_000_(e)
            assert 0 < exp4patch_base < order_of_base
            x = order_of_base -exp4patch_base
            assert 0 < x < order_of_base
        else:
            x = 0
            # !! [y =!= 1]
            raise 000
        break
    #end-while 1: # not loop, just for 'break'
    x
    if 0b01:
        assert 0 <= x < order_of_base
        assert pow(base, x, modulus) == y, ((base, x, modulus), pow(base, x, modulus), y)
    return x
#end-def _discrete_logarithm__coprime__order_of_base_is_odd_prime_power_(modulus, base, order_of_base, p, ep, y, /):


__all__


from seed.math.discrete_logarithm import discrete_logarithm__coprime_
    #def discrete_logarithm__coprime_(modulus, base, order_of_base, factorization_of_order_of_base, y, /)
if 1:from seed.math.discrete_logarithm import _find_arbitrary_one_primitive_root_mod_prime_, _find_the_min_primitive_root_mod_prime_, _iter_sorted_primitive_roots_mod_prime_
    #from seed.math.discrete_logarithm import find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_, find_the_min_primitive_root_mod_prime__using_factorization_of_pmm_, iter_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_
#from seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_ import _find_arbitrary_one_primitive_root_mod_prime_, _find_the_min_primitive_root_mod_prime_, _iter_sorted_primitive_roots_mod_prime_
#from seed.math.find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_ import find_arbitrary_one_primitive_root_mod_prime__using_factorization_of_pmm_, find_the_min_primitive_root_mod_prime__using_factorization_of_pmm_, iter_sorted_primitive_roots_mod_prime__using_factorization_of_pmm_

from seed.math.discrete_logarithm import *
