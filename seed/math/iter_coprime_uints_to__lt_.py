#__all__:goto
r'''[[[
e ../../python3_src/seed/math/iter_coprime_uints_to__lt_.py

seed.math.iter_coprime_uints_to__lt_
py -m nn_ns.app.debug_cmd   seed.math.iter_coprime_uints_to__lt_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.iter_coprime_uints_to__lt_:__doc__ -ht # -ff -df
#######

[[
used by:
view script/设计冫乘法群牜不可交换.py
]]
[[
[@[c,B::uint][c >= 2][B >= 1][@[p::prime][B%p==0][p < c] -> [c%p=!=0]] -> [[[gcd(c,B) =!= 1] <-> [gcd(c,B) == c] <-> [B%c==0]][[B%c=!=0] -> [gcd(c,B) == 1]][[B%c==0] -> [[gcd(c,B) =!= 1][gcd(c,B) == c][is_prime_(c)]]]]]
    [[proof:
    [c,B::uint][c >= 2][B >= 1][@[p::prime][B%p==0][p < c] -> [c%p=!=0]]:
        [@[p::prime][B%p==0][p < c] -> [gcd(c,B)%p=!=0]]

        !! [c >= 2]
        [gcd(c,B) <= c]
        [q::prime][gcd(c,B)%q == 0]:
            [B%q==0][c%q==0]
            [q < c]:
                !! [@[p::prime][B%p==0][p < c] -> [gcd(c,B)%p=!=0]]
                !! [q::prime][B%q==0][q < c]
                [gcd(c,B)%q=!=0]
                _L
            [not [q < c]]
            [q >= c]

            !! [c >= 2][c%q==0]
            [q <= c]
            !! [q >= c]
            [q == c]
            !! [q::prime]
            [is_prime_(c)]

            !! [gcd(c,B)%q == 0]
            !! [q == c]
            [gcd(c,B) == c]
            [B%c==0]
        [@[q::prime][gcd(c,B)%q == 0] -> [[q == c][is_prime_(c)][gcd(c,B) == c][B%c==0]]]
        [gcd(c,B) =!= 1]:
            [gcd(c,B) >= 2]
            ?q :=> [q::prime][gcd(c,B)%q == 0]
            !! [@[q::prime][gcd(c,B)%q == 0] -> [[q == c][is_prime_(c)][gcd(c,B) == c][B%c==0]]]
            [[is_prime_(c)][gcd(c,B) == c][B%c==0]]
        [[gcd(c,B) =!= 1] -> [[is_prime_(c)][gcd(c,B) == c][B%c==0]]]

        !! [c >= 2]
        [[B%c==0] -> [gcd(c,B) == c]]

        !! [c >= 2]
        [[gcd(c,B) == c] -> [gcd(c,B) =!= 1]]


        !! [[B%c==0] -> [gcd(c,B) == c]]
        !! [[gcd(c,B) == c] -> [gcd(c,B) =!= 1]]
        !! [[gcd(c,B) =!= 1] -> [[is_prime_(c)][gcd(c,B) == c][B%c==0]]]
        [[gcd(c,B) =!= 1] <-> [gcd(c,B) == c] <-> [B%c==0]]
        [[B%c=!=0] -> [gcd(c,B) == 1]]
        [[B%c==0] -> [[gcd(c,B) =!= 1][gcd(c,B) == c][is_prime_(c)]]]
    ok
    end-proof
    ]]

]]


'#'; __doc__ = r'#'
>>> [*iter_coprime_uints_to__lt_(3, 6)]
[1]
>>> [*iter_coprime_uints_to__lt_(20, 6)]
[1, 5, 7, 11, 13, 17, 19]
>>> [*takewhile((3).__gt__, iter_coprime_uints_to_(6))]
[1]
>>> [*takewhile((20).__gt__, iter_coprime_uints_to_(6))]
[1, 5, 7, 11, 13, 17, 19]
>>> from seed.math.gcd import gcd, are_coprime
>>> def test1_(M, B, /):
...     result2 = [*takewhile(M.__gt__, iter_coprime_uints_to_(B))]
...     result = [*iter_coprime_uints_to__lt_(M, B)]
...     answer = [c for c in range(M) if are_coprime(c,B)]
...     if not result2 == result == answer: print((M, B, result2, result, answer))
>>> def tests_(max4M, max4B, /):
...     for M in range(-1, 1+max4M):
...         for B in range(-1, 1+max4B):
...             test1_(M, B)
>>> tests_(20, 20)



py_adhoc_call   seed.math.iter_coprime_uints_to__lt_   @f
]]]'''#'''
__all__ = r'''
iter_coprime_uints_to__lt_
    iter_coprimes_mod_
    iter_coprime_uints_to_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.tiny_.check import check_type_is, check_int_ge
from itertools import count, takewhile
___end_mark_of_excluded_global_names__0___ = ...


def iter_coprimes_mod_(M, /):
    'M/int -> Iter c/uint # [0 <= c < M][gcd(c,M) == 1]'
    check_type_is(int, M)
    return iter_coprime_uints_to__lt_(M, M)
def iter_coprime_uints_to_(B, /):
    'B/int -> Iter c/uint # [c >= 0][gcd(c,B) == 1]'
    return iter_coprime_uints_to__lt_(M:=None, B)

def _drop_prime_power_(p, n, /):
    while 1:
        (q, r) = divmod(n, p)
        if not r == 0:
            return n
        n = q
def _special_case4iter_coprime_uints_to__lt_(M, B, /):
    # [[M < 2]or[B < 2]]
    M_eq_inf = M is None

    if B == 0:
        # [B == 0]
        # !! [gcd(c,B) == 1]
        # [gcd(c,0) == 1]
        # [abs(c) == 1]
        # !! [0 <= c < M]
        # [1 == c < M]
        # [1 < M]
        if M_eq_inf or 1 < M:
            # [1 == c < M]
            # [B == 0]
            yield 1
        else:
            # _L
            # no any c
            pass
        return
    # [B >= 1]
    if B == 1:
        # [B == 1]
        # !! [gcd(c,1) == 1]
        # [gcd(c,B) == 1]
        if 0:
            for c in range(M):
                # [0 <= c < M]
                # [gcd(c,B) == 1]
                yield c
        yield from count(0) if M_eq_inf else range(M)
        return
    # [B >= 2]

    if not M_eq_inf and M < 1:
        # [M <= 0]
        # !! [0 <= c < M]
        # [0 <= c < 0]
        # [0 < 0]
        # _L
        # no any c
        return
    # [M >= 1]

    # [B >= 2]
    # [M >= 1]
    if not M_eq_inf and M == 1:
        # !! [0 <= c < M]
        # [0 <= c < 1]
        # [c == 0]
        # !! [gcd(c,B) == 1]
        # [abs(B) == 1]
        # !! [B >= 2]
        # _L
        # no any c
        return
    # [M >= 2]
    # [B >= 2]
    # !! [[M < 2]or[B < 2]]
    # _L
    raise 000


def iter_coprime_uints_to__lt_(M, B, /):
    'may M/int -> B/int -> Iter c/uint # [0 <= c < ifNone(M, +oo)][gcd(c,B) == 1]'
    M_eq_inf = M is None
    M_eq_inf or check_type_is(int, M)
    check_type_is(int, B)

    B = abs(B)
    # [B >= 0]
    if not (B >= 2 and (M_eq_inf or M >= 2)):
        # [[M < 2]or[B < 2]]
        yield from _special_case4iter_coprime_uints_to__lt_(M, B)
        return
    # [B >= 2]
    # [M >= 2]
    # [gcd(0,B) == B >= 2]
    # !! [gcd(c,B) == 1]
    # [c =!= 0]
    # !! [0 <= c < M]
    # [1 <= c < M]


    # [c == 1]:
    #   !! [gcd(1,B) == 1]
    #   [gcd(c,B) == 1]
    #   !! [M >= 2]
    #   [1 <= c < M]
    yield 1
    # [2 <= c < M]


    # [B >= 2]
    # [M >= 2]
    # [2 <= c < M]


    c = 2
    # !! [c == 2]
    # !! [M >= 2]
    # [2 <= c <= M]
    _B = B
    # !! [c == 2]
    # !! [B >= 2]
    # [_B >= c]
    ps4B = []
    # !! [c == 2]
    # [[] == [p | [p::prime][p < c]]]
    # [[] == [p | [p::prime][B%p==0][p < c]]]
    # [ps4B == [] == [p | [p::prime][B%p==0][p < c]]]
    # [ps4B == [p | [p::prime][B%p==0][p < c]]]

    # !! [_B == B]
    # !! [ps4B == []]
    # [@[p::prime][B%p==0] -> [[_B%p=!=0] <-> [p<-ps4B]]]

    # !! [_B == B]
    # !! [B >= 2]
    # [B%_B == 0]


    # [B,M :: immutable]
    # [c,_B :: mutable]
    # [B >= 2]
    # [M >= 2]
    # [2 <= c <= M]
    # [_B >= c]
    # [B%_B == 0]
    # [ps4B == [p | [p::prime][B%p==0][p < c]]]
    # [@[p::prime][B%p==0] -> [[_B%p=!=0] <-> [p<-ps4B]]]
    while 1:
        # [2 <= c <= M]
        # [_B >= c]
        # [B%_B == 0]
        # [ps4B == [p | [p::prime][B%p==0][p < c]]]
        # [@[p::prime][B%p==0] -> [[_B%p=!=0] <-> [p<-ps4B]]]
        if c == M:
            #if not M_eq_inf and c == M:
            # [c == M]
            # !! [_B >= c]
            # !! [2 <= c <= M]
            # [_B >= 2]
            # [_B =!= 1]
            ##########
            # [_B =!= 1][c == M <= _B]
            ##########
            break#break7halt
        # [2 <= c < M]

        bad4c = False
        for p in ps4B:
            # [p <- ps4B]
            # !! [ps4B == [p | [p::prime][B%p==0][p < c]]]
            # [is_prime_(p)][B%p == 0][p < c]
            # !! [@[p::prime][B%p==0] -> [[_B%p=!=0] <-> [p<-ps4B]]]
            # [_B%p=!=0]
            if c%p == 0:
                # [c%p == 0]
                ##################
                # !! [c%p == 0]
                # !! [B%p == 0]
                # [gcd(c,B)%p == 0]
                # [gcd(c,B) >= p > 1]
                # [gcd(c,B) =!= 1]
                # bad c
                #bug:continue
                p
                # [is_prime_(p)][B%p == 0][p < c]
                # [c%p == 0]
                # [gcd(c,B) =!= 1]
                bad4c = True
                break#break7bad_c
        if bad4c:
            #from "break7bad_c"
            p
            # [is_prime_(p)][B%p == 0][p < c]
            # [c%p == 0]
            # [gcd(c,B) =!= 1]
            ##################
            # !! [c%p == 0]
            # !! [is_prime_(p)][p < c]
            # [2 <= p < c =!= p]
            # !! [c%p == 0]
            # [not is_prime_(c)]
            ##################
            # !! [ps4B == [p | [p::prime][B%p==0][p < c]]]
            # !! [not is_prime_(c)]
            #  [ps4B == [p | [p::prime][B%p==0][p < c+1]]]
            ##################
            # !! [_B%p=!=0]
            # !! [c%p == 0]
            # [c =!= _B]
            # !! [_B >= c]
            # [_B > c]
            # [_B >= (c+1)]


            ##################
            # !! [gcd(c,B) =!= 1]
            # this c value is not ok # not yield
            ##################
            # !! [@[p::prime][B%p==0] -> [[_B%p=!=0] <-> [p<-ps4B]]]
            # !! [ps4B == [p | [p::prime][B%p==0][p < c+1]]]
            # !! [B%_B == 0]
            # !! [_B >= (c+1)]
            # !! [2 <= c < M]
            c += 1
            # [2 <= c <= M]
            # [_B >= c]
            # [B%_B == 0]
            # [ps4B == [p | [p::prime][B%p==0][p < c]]]
            # [@[p::prime][B%p==0] -> [[_B%p=!=0] <-> [p<-ps4B]]]
            continue
            ##################
        # [@[p:<-ps4B] -> [c%p=!=0]]
        # !! [ps4B == [p | [p::prime][B%p==0][p < c]]]
        # [@[p::prime][B%p==0][p < c] -> [c%p=!=0]]
        # [@[p::prime][B%p==0][p < c] -> [gcd(c,B)%p=!=0]]

        # !! [@[c,B::uint][c >= 2][B >= 1][@[p::prime][B%p==0][p < c] -> [c%p=!=0]] -> [[[gcd(c,B) =!= 1] <-> [gcd(c,B) == c] <-> [B%c==0]][[B%c=!=0] -> [gcd(c,B) == 1]][[B%c==0] -> [[gcd(c,B) =!= 1][gcd(c,B) == c][is_prime_(c)]]]]]
        # [[gcd(c,B) =!= 1] <-> [gcd(c,B) == c] <-> [B%c==0]]
        # [[B%c=!=0] -> [gcd(c,B) == 1]]
        # [[B%c==0] -> [[gcd(c,B) =!= 1][gcd(c,B) == c][is_prime_(c)]]]

        # !! [@[p:<-ps4B] -> [c%p=!=0]]
        # [@[p::prime][c%p==0] -> [not$[p <- ps4B]]]
        # !! [@[p::prime][B%p==0] -> [[_B%p=!=0] <-> [p<-ps4B]]]
        # [@[p::prime][B%p==0][c%p==0] -> [_B%p==0]]
        # [@[p::prime][gcd(B,c)%p==0] -> [_B%p==0]]
        # [[gcd(B,c) =!= 1] -> [gcd(_B,c) =!= 1]]

        # !! [B%_B == 0]
        # [[gcd(_B,c) =!= 1] -> [gcd(B,c) =!= 1]]
        # !! [[gcd(B,c) =!= 1] -> [gcd(_B,c) =!= 1]]
        # [[gcd(_B,c) =!= 1] <-> [gcd(B,c) =!= 1]]
        # !! [[gcd(c,B) =!= 1] <-> [gcd(c,B) == c] <-> [B%c==0]]
        # [[gcd(_B,c) =!= 1] <-> [B%c==0]]
        # !! [[B%c==0] -> [[gcd(c,B) =!= 1][gcd(c,B) == c][is_prime_(c)]]]
        # [[gcd(_B,c) =!= 1] -> [is_prime_(c)]]
        # [[gcd(_B,c) =!= 1] -> [_B%c==0]]
        # !! [[gcd(_B,c) =!= 1] <-> [B%c==0]]
        # [[B%c==0] -> [_B%c==0]]

        # !! [B%_B == 0]
        # [[_B%c==0] -> [B%c==0]]
        # !! [[B%c==0] -> [_B%c==0]]
        # [[_B%c==0] <-> [B%c==0]]
        if _B%c == 0:
            # [_B%c == 0]
            # !! [[_B%c==0] <-> [B%c==0]]
            # [B%c == 0]
            # !! [[B%c==0] -> [[gcd(c,B) =!= 1][gcd(c,B) == c][is_prime_(c)]]]
            # [gcd(c,B) =!= 1]
            # [is_prime_(c)]

            ##################
            # !! [@[p::prime][B%p==0] -> [[_B%p=!=0] <-> [p<-ps4B]]]
            # !! [_B%c == 0]
            # !! [ps4B == [p | [p::prime][B%p==0][p < c]]]
            # !! [is_prime_(c)]
            # !! [B%c == 0]
            ps4B.append(c)
            # [ps4B == [p | [p::prime][B%p==0][p < c+1]]]
            # [@[p::prime][B%p==0] -> [[_B%p=!=0]+[p==c] == [p<-ps4B]]]
            _Bnew = _drop_prime_power_(c, _B)
            # [_Bnew%c =!= 0]
            # [_B%_Bnew == 0]
            # [@[p::prime][_B%p==0] -> [[_Bnew%p=!=0] <-> [p==c]]]


            # !! [@[p::prime][_B%p==0] -> [[_Bnew%p=!=0] <-> [p==c]]]
            # [@[p::prime] -> [[_Bnew%p==0]+[p==c] == [_B%p==0]]]
            # [@[p::prime] -> [[_Bnew%p=!=0] == [_B%p=!=0]+[p==c]]]
            # !! [@[p::prime][B%p==0] -> [[_B%p=!=0]+[p==c] == [p<-ps4B]]]
            # [@[p::prime][B%p==0] -> [[_Bnew%p=!=0] == [p<-ps4B]]]

            # !! [_B%_Bnew == 0]
            # !! [B%_B == 0]
            # [B%_Bnew == 0]

            # !! [_B%_Bnew == 0]
            # [_B >= _Bnew]
            # [_B >= c]
            # MAY_NOT_HAS:[_Bnew >= c]
            # [_Bnew < c+1][p::prime][_Bnew%p==0]:
            #   [p <= _Bnew < c+1]
            #   !! [B%_Bnew == 0]
            #   [B%p == 0]
            #   !! [ps4B == [p | [p::prime][B%p==0][p < c+1]]]
            #   [p <- ps4B]
            #   !! [B%p == 0]
            #   !! [@[p::prime][B%p==0] -> [[_Bnew%p=!=0] == [p<-ps4B]]]
            #   [_Bnew%p=!=0]
            #   _L
            # [[_Bnew < c+1] -> [_Bnew == 1]]
            # [[_Bnew =!= 1] -> [_Bnew >= c+1]]

            # !! [@[p::prime][B%p==0] -> [[_Bnew%p=!=0] == [p<-ps4B]]]
            # !! [B%_Bnew == 0]
            # !! [_Bnew%c =!= 0]
            # [[_Bnew =!= 1] -> [_Bnew >= c+1]]
            _B = _Bnew
            # [@[p::prime][B%p==0] -> [[_B%p=!=0] == [p<-ps4B]]]
            # [B%_B == 0]
            # [_B%c =!= 0]
            # [[_B =!= 1] -> [_B >= c+1]]

            #==>>:
            ps4B
            _B
            # [ps4B == [p | [p::prime][B%p==0][p < c+1]]]
            # [@[p::prime][B%p==0] -> [[_B%p=!=0] == [p<-ps4B]]]
            # [B%_B == 0]
            ##################
            # !! [[gcd(c,B) =!= 1]
            # this c value is not ok # not yield
            ##################
            # !! [2 <= c < M]
            # MAY_NOT_HAS:[_Bnew >= c]
            # [[_B =!= 1] -> [_B >= c+1]]
            # !! [B%_B == 0]
            # !! [ps4B == [p | [p::prime][B%p==0][p < c+1]]]
            # !! [@[p::prime][B%p==0] -> [[_B%p=!=0] <-> [p<-ps4B]]]
            c += 1
            # [2 <= c <= M]
            # MAY_NOT_HAS:[_B >= c]
            # [[_B =!= 1] -> [_B >= c]]
            # [B%_B == 0]
            # [ps4B == [p | [p::prime][B%p==0][p < c]]]
            # [@[p::prime][B%p==0] -> [[_B%p=!=0] <-> [p<-ps4B]]]
            if not _B == 1:
                # !! [[_B =!= 1] -> [_B >= c]]
                # [_B >= c]
                continue
            # [_B == 1]
            # !! [@[p::prime][B%p==0] -> [[_B%p=!=0] <-> [p<-ps4B]]]
            # [@[p::prime][B%p==0] -> [p<-ps4B]]
            # !! [ps4B == [p | [p::prime][B%p==0][p < c]]]
            # [ps4B == [p | [p::prime][B%p==0]]]
            break#break7B_completely_factorized
            ##################
        else:
            # [_B%c =!= 0]
            # !! [[_B%c==0] <-> [B%c==0]]
            # [B%c =!= 0]
            # !! [[B%c=!=0] -> [gcd(c,B) == 1]]
            # [gcd(c,B) == 1]
            ##################
            # !! [[gcd(c,B) =!= 1]
            # !! [2 <= c < M]
            yield c
            ##################
            # !! [ps4B == [p | [p::prime][B%p==0][p < c]]]
            # [B%c =!= 0]
            # [ps4B == [p | [p::prime][B%p==0][p < c+1]]]

            ##################
            # !! [_B%c =!= 0]
            # [_B =!= c]
            # !! [_B >= c]
            # [_B > c]
            # [_B >= c+1]
            ##################
            # !! [2 <= c < M]
            # !! [_B >= c+1]
            # !! [B%_B == 0]
            # !! [ps4B == [p | [p::prime][B%p==0][p < c+1]]]
            # !! [@[p::prime][B%p==0] -> [[_B%p=!=0] <-> [p<-ps4B]]]
            c += 1
            # [2 <= c <= M]
            # [_B >= c]
            # [B%_B == 0]
            # [ps4B == [p | [p::prime][B%p==0][p < c]]]
            # [@[p::prime][B%p==0] -> [[_B%p=!=0] <-> [p<-ps4B]]]
            continue
            ##################
    #end-while 1:
    if not _B == 1:
        #from "break7halt"
        # [_B =!= 1][c == M <= _B]
        assert c == M <= _B
        return
    #from "break7B_completely_factorized"
    # [_B == 1]
    # [2 <= c <= M]
    # [ps4B == [p | [p::prime][B%p==0]]]
    yield from _iter_coprime_uints_to_primes__ge_lt_(c, M, ps4B)
def _iter_coprime_uints_to_primes__ge_lt_(c0, M, ps4B, /):
    # [2 <= c0 <= M]
    # [ps4B == [p | [p::prime][B%p==0]]]
    M_eq_inf = M is None
    cs = count(c0) if M_eq_inf else range(c0, M)
    for c in cs:
        # [2 <= c0 <= c <= M]
        bad4c = False
        for p in ps4B:
            # [p <- ps4B]
            # !! [ps4B == [p | [p::prime][B%p==0]]]
            # [B%p==0]
            if c%p == 0:
                # [c%p==0]
                # !! [B%p==0]
                # [gcd(c,B) =!= 1]
                # bad c
                #bug:continue
                bad4c = True
                break#break7bad_c
        if bad4c:
            #from "break7bad_c"
            continue
        # [@[p:<-ps4B] -> [c%p=!=0]]
        # !! [ps4B == [p | [p::prime][B%p==0]]]
        # [gcd(c,B) == 1]
        # !! [2 <= c0 <= c <= M]
        yield c


__all__
from seed.math.iter_coprime_uints_to__lt_ import iter_coprime_uints_to__lt_, iter_coprime_uints_to_, iter_coprimes_mod_
from seed.math.iter_coprime_uints_to__lt_ import *
