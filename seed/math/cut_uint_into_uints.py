
r'''
py -m seed.math.cut_uint_into_uints
from seed.math.cut_uint_into_uints import Helper4cut_uint_into_uints, calc_lowerbound_of_inf_compact_domain_rng4cut_uint_into_uints


cut_uint_into_uints :: (part_uints::set<uint_ge2>) -> (u::uint) -> ((part_uint2count::map<uint_ge2, uint_ge1>) | raise ValueError)
    postcondition:
        set(part_uint2count) <= part_uints
        u == sum(part_uint*count for part_uint, count in part_uint2count.items())

???min uint lowbd s.t. all [lowbd..] can be cut_uint_into_uints???
    let mu = min set<uint_ge2>
    [x is lowbd] <==> [x>=mu>=2][x-1 can be cut_uint_into_uints][all [x..x+mu-1] can be cut_uint_into_uints]
cut_uint_into_uints case 2 uints:
    [a,b>=2][gcd(a,b)==1][x,y>0][x*a-y*b==1][x<b][y<a]:
        [a != b]
        let m = lcm(a,b) = a*b >= 6
        y*b < a*b == m
        [r <- [0..m-1]]:
            r*x*a-r*y*b==r
            r*x*a+((m-1)*m-r*y*b)==(m-1)*m+r
            r*x*a+((m-1)*a-r*y)*b==(m-1)*m+r
            ==>> lowbd <= (m-1)*m
        lowbd <= (m-1)*m

        [r <- [0..m-1]]:
            r*x*a-r*y*b==r
            let (q,k) = r*y /% a
            r*y == q*a+k
            q >= 0
            k >= 0
            r >= 0
            r == r*x*a-r*y*b
                == r*x*a-(q*a+k)*b
                == r*x*a-q*a*b -k*b
                == (r*x-q*b)*a -k*b
            (r*x-q*b)*a ==r+k*b >= 0
            (r*x-q*b) >= 0
            #0 <= (r*x-q*b)
            #    == (r*x - r*y //a *b) *a//a
            #    == (r*x*a - r*y //a *a *b)//a

            0 <= k < a
            (r*x-q*b) == (r+k*b)/a
                <= (m-1+(a-1)*b)//a
                    == (2*m-1-b)//a
                    < 2*b
            k*b + r == (r*x-q*b)*a +0*b
            k*m + r == (r*x-q*b)*a +k*(a-1)*b
            ==>> lowbd <= (a-1)*m
        lowbd <= (a-1)*m




#'''



__all__ = '''
    Helper4cut_uint_into_uints
    calc_lowerbound_of_inf_compact_domain_rng4cut_uint_into_uints
    '''.split()
from seed.helper.check.checkers import check_uint
from seed.math.gcd import gcd_many
from seed.math.lcm import lcm_many
from seed.math.floor_ceil import offsetted_divmod

from seed.types.FrozenDict import FrozenDict
from collections import defaultdict


gcd_many
lcm_many


class Helper4cut_uint_into_uints:
    r'''
    possible_parts_of
    calc_lowerbound_of_inf_compact_domain_rng
    cut_uint_into_uints__greedy
    cut_uint_into_uints__greedy_last__ordered_part_uints
    #'''
    def __init__(sf, uint_ge2_set_sz_ge2, /):
        sf.__us = _check_uint_ge2_set_sz_ge2(uint_ge2_set_sz_ge2)
        sf.__sorted_us = tuple(sorted(sf.__us))
        sf.__min = min(sf.__us)
        sf.__max = max(sf.__us)
        sf.__u2us = [set() for _ in range(sf.__max+1)]
        for u in sf.__us:
            sf.__u2us[u].add(u)
        sf.__end = 0
        sf.__acc = 0
        sf.__lowbound = 0
        sf.__us2us = {}
    def calc_lowerbound_of_inf_compact_domain_rng(sf, /):
        if not sf.__lowbound:
            us = sf.__us
            upperbound = _calc_upperbound(us)
            sf.possible_parts_of(upperbound)
            if not sf.__lowbound:
                raise logic-err--cannot-findout-lowbound-lt-assumed-upperbound
        lowbd = sf.__lowbound
        assert lowbd
        return lowbd

    def __getitem__(sf, u, /):
        'uint -> frozenset{uint}'
        check_uint(u)
        u2us = sf.__u2us
        end = sf.__end
        if not (u < end or sf.__lowbound):
            begin = end
            end = u+1
            acc = sf.__acc
            u2us.extend(set() for v in range(len(u2us), end+sf.__max))

            for v in range(begin, end):
                us = u2us[v]
                us = frozenset(us)
                us = sf.__us2us.setdefault(us, us)
                u2us[v] = us

                us = u2us[v]
                if us:
                    acc += 1
                    if acc == sf.__max+1:
                        #bug: len(us) == sf.__max
                        assert len(us) == len(sf.__us)
                        end = v+1
                        del u2us[end:]
                        sf.__lowbound = lowbd = end - acc
                        assert lowbd >= 2
                        assert not u2us[lowbd-1]
                        assert all(u2us[lowbd:])
                        assert len(u2us[lowbd:]) == sf.__max+1
                        assert lowbd == calc_lowerbound_of_inf_compact_domain_rng4cut_uint_into_uints(sf.__us)
                        break
                    for k in sf.__us:
                        u2us[v+k].add(k)
                else:
                    acc = 0
            sf.__end = end
            sf.__acc = acc



        assert (u < end or sf.__lowbound)
        if u < end:
            us = u2us[u]
        elif sf.__lowbound:
            assert 2 <= sf.__lowbound < len(u2us) == end <= u
            us = u2us[-1]
            assert len(us) == len(sf.__us)
        else:
            raise logic-err
        return us
    def possible_parts_of(sf, u, /):
        'uint -> frozenset{uint}'
        return sf[u]
    def cut_uint_into_uints__greedy(sf, u, /):
        'uint -> FrozenDict{uint:count}|raise ValueError'
        return sf.cut_uint_into_uints__greedy_last__ordered_part_uints(None, u)

    def cut_uint_into_uints__greedy_last__ordered_part_uints(sf, may_ordered_part_uints, u, /):
        'may[part_uint] -> uint -> FrozenDict{uint:count}|raise ValueError'
        saved_u = u
        if may_ordered_part_uints is None:
            ordered_part_uints = sf.__sorted_us
        else:
            ordered_part_uints = may_ordered_part_uints
        it = reversed(ordered_part_uints)#last first
        def get_last(it, us):
            for last in it:
                if last in us: break
            else:
                raise ValueError(f'ordered_part_uints is not complete part_uints')
            return last

        u2count = defaultdict(int)
        us = sf.possible_parts_of(u)
        if not us: raise ValueError(f'cannot cut_uint_into_uints({sorted(sf.__us)}, {u})')

        last = get_last(it, us)
        may_lowbd = sf.__lowbound
        if may_lowbd:
            lowbd = may_lowbd
            if 1:
                #greedy
                #d = sf.__max
                d = last
            if lowbd+d <= u:
                (pq, pr) = offsetted_divmod(lowbd, u,d)
                assert lowbd <= pr < lowbd+d
                assert u == pq*d +pr
                assert pq > 0
                u2count[d] += pq
                u = pr
                us = sf.possible_parts_of(u)

        while us:
            if 1:
                #greedy
                #v = max(us)
                if last not in us:
                    last = get_last(it, us)
                v = last
            u2count[v] += 1
            u -= v
            us = sf.possible_parts_of(u)
        u2count = FrozenDict(u2count)

        assert type(u2count) is FrozenDict
        assert saved_u == sum(u*count for u, count in u2count.items())
        assert all(u2count.values())
        assert set(u2count) <= sf.__us
        return u2count
#end of class Helper4cut_uint_into_uints:



def _check_uint_ge2_set_sz_ge2(uint_ge2_set_sz_ge2, /):
    if type(uint_ge2_set_sz_ge2) is frozenset:
        us = uint_ge2_set_sz_ge2
    else:
        us = frozenset(uint_ge2_set_sz_ge2)
    us; del uint_ge2_set_sz_ge2

    if not len(us) >= 2: raise ValueError
    if not all(type(u) is int for u in us): raise TypeError
    if gcd_many(us) != 1: raise ValueError

    if not all(u >= 2 for u in us): raise ValueError
    return us

def _calc_upperbound(us):
    _lcm = lcm_many(us)
    upperbound = len(us)*_lcm**2
    return upperbound
def calc_lowerbound_of_inf_compact_domain_rng4cut_uint_into_uints(uint_ge2_set_sz_ge2):
    us = _check_uint_ge2_set_sz_ge2(uint_ge2_set_sz_ge2)
    upperbound = _calc_upperbound(us)

    u2decomposable = []
    def put(u):
        n = u+1
        u2decomposable.extend([0]*(n-len(u2decomposable)))
        u2decomposable[u] = 1
    mu = min(us)
    acc = 0
    for u in us: put(u)
    for u in range(upperbound):
        b = u2decomposable[u]
        if b:
            acc += 1
            if acc == mu:
                lowbd = u+1-mu
                break
            for d in us: put(u+d)
        else:
            acc = 0
    else:
        raise logic-err--cannot-findout-lowbound-lt-assumed-upperbound
    assert lowbd >= 2
    assert lowbd >= mu >= 2
    assert not u2decomposable[lowbd-1]
    assert all(u2decomposable[u] for u in range(lowbd, lowbd+mu))
    return lowbd
#end of def _check_uint_ge2_set_sz_ge2(uint_ge2_set_sz_ge2, /):


_test_data = \
    [([2,3], 2)
    ,([2,5], 4)
    ,([2,5,4], 4)
    ,([2,5,3], 2)
    ,([2,7], 6)
    ,([2,7,4], 6)
    ,([3,4], 6)
    ,([3,4,5], 3)
    ,([4,5], 12)
    ]
def _t(calc_lowerbound_of_inf_compact_domain_rng4cut_uint_into_uints):
    for us, lowbd in _test_data:
        assert lowbd == calc_lowerbound_of_inf_compact_domain_rng4cut_uint_into_uints(us)

if 1:
    _t(calc_lowerbound_of_inf_compact_domain_rng4cut_uint_into_uints)
    _t(lambda us:Helper4cut_uint_into_uints(us).calc_lowerbound_of_inf_compact_domain_rng())

def _t2():
    for us, lowbd in _test_data:
        #rint(us, lowbd)
        h = Helper4cut_uint_into_uints(us)
        assert lowbd == h.calc_lowerbound_of_inf_compact_domain_rng()

        upperbound = _calc_upperbound(us)
        #us = set(us)
        #for u in range(lowbd, upperbound):
        for u in range(lowbd, lowbd+lcm_many(us)+sum(us)+1):
            #rint(f'    {u}')
            h.cut_uint_into_uints__greedy(u)
                #check inside
if 1:
    _t2()



