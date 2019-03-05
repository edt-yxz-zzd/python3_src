
__all__ = '''
    generater_elements_of_ordered_coordinate_only
    generaters2all_elements

    generater2powers
    generater_products_of_reversed_pair_powers_of_ordered_coordinate_only
    '''.split()
import operator
import itertools # combinations, product
from seed.types.pair_based_leftward_list import (
    leftward_list2list
    ,iter_leftward_list
    )
from seed.math.II import II


def generater2powers(generater, *, one, mul):
    '''
mul :: g->g->g
generater :: Hashable
    __eq__
'''
    #assert generater != one
    last = one
    powers = [last]
    while True:
        last = mul(generater, last)
        if last == one:
            break
        powers.append(last)
    assert mul(powers[-1], generater) == one
    return tuple(powers)


def maybe_mul2mul(maybe_mul):
    if maybe_mul is None:
        mul = operator.__mul__
    else:
        mul = maybe_mul
    return mul

def generater_products_of_reversed_pair_powers_of_ordered_coordinate_only(
    generaters, *, one, maybe_mul):
    '''
{gs[j]^ej*gs[i]^ei : [((j,ej),(i,ei))] | i < j, 1<=ei<order(gs[i]), 1<=ej<order(gs[j])}
'''
    mul = maybe_mul2mul(maybe_mul)
    generater_powerss = [generater2powers(g, one=one, mul=mul)
                        for g in generaters
                        ]

    L = len(generaters)
    g2gidx_exp_pair_pairs = {}
    for i,j in itertools.combinations(range(L), 2):
        assert 0 <= i < j < L
        gi_powers = generater_powerss[i]
        gj_powers = generater_powerss[j]
        ei_rng = range(1, len(gi_powers))
        ej_rng = range(1, len(gj_powers))
        for ei, ej in itertools.product(ei_rng, ej_rng):
            gi_power = gi_powers[ei]
            gj_power = gj_powers[ej]
            #bug: g = mul(gi_power, gj_power)
            g = mul(gj_power, gi_power)
            pairpairs = g2gidx_exp_pair_pairs.setdefault(g, [])
            pairpairs.append(((j,ej), (i,ei)))
    return g2gidx_exp_pair_pairs

def generater_elements_of_ordered_coordinate_only(
    generaters, *, one, maybe_mul):
    '''
finite group; result is a subset not subgroup
generater_elements_of_ordered_coordinate_only one gs =
    {g:[es | es :: [UInt], 0 <= es[i] < order(gs[i]), g = II gs[i]^es[i] {i}]
    | g <- Gen<gs...>
    , es::[UInt]
    , g = II gs[i]^es[i] {i}
    }

maybe_mul :: None | (g->g->g)
generater :: Hashable
result :: Map g nonempty[[UInt]]
'''
    mul = maybe_mul2mul(maybe_mul)
    generater_powerss = [generater2powers(g, one=one, mul=mul)
                        for g in generaters
                        ]

    element2expss = {}
    #for powers in itertools.product(*generater_powers):
    for exps in itertools.product(*map(range, map(len, generater_powerss))):
        coor_powers = [powers[exp] for powers, exp in zip(generater_powerss, exps)]
        g = II(coor_powers, one=one, mul=mul)
        expss = element2expss.setdefault(g, [])
        expss.append(exps)
    return element2expss

def generaters2all_elements(
    generaters, *, one, maybe_mul, to_list=False):
    '''
finite group
generaters2all_elements one gs = {g: [leftward_list g] | g <- Gen<gs...>}
generaters2all_elements one gs to_list=True = {g: [[g]] | g <- Gen<gs...>}
    for k, lsls in result.items():
        for ls in lsls:
            assert k == II ls

maybe_mul :: None | (g->g->g)
generater :: Hashable
'''
    assert len(generaters) == len(set(generaters))
    assert one not in generaters
    to_list = bool(to_list)

    mul = maybe_mul2mul(maybe_mul)

    # {g : [[g]]}
    # {g : [LinkList g]}
    # LinkList g = () | (g, LinkList g)
    element2products = {one:[()]}
    assert all(mul(g, one) == g for g in generaters)

    old_all_keys = set()
    while len(old_all_keys) < len(element2products):
        all_keys = set(element2products)
        new_keys = all_keys - old_all_keys
        for k in new_keys:
            lls = element2products[k][0]
            for g in generaters:
                k_ = mul(g, k)
                lls_ = element2products.setdefault(k_, [])
                lls_.append((g, lls))
        old_all_keys = all_keys
    assert len(old_all_keys) == len(element2products)

    if to_list:
        for products in element2products.values():
            for i, lls in enumerate(products):
                products[i] = leftward_list2list(lls)

    if __debug__:
        g2IIs = element2products
        iter_II = iter if to_list else iter_leftward_list
        assert all(g == II(gs, one=one, mul=mul) for g, IIs in g2IIs.items() for gs in map(iter_II, IIs))

    return element2products



def _t():
    from .FinitePermutation import FinitePermutation, sort_disjoint_cycles
    mk = FinitePermutation.from_disjoint_cycles
    to = lambda self: sort_disjoint_cycles(self.to_disjoint_cycles())
    one = mk(())
    g1 = mk(((0,1,2),))
    g2 = mk(((0,1,2,3,4),))
    generaters2 = [g1, g2]
    g2IIs = generaters2all_elements(generaters2, one=one, maybe_mul=None, to_list=True)
    g2name = {g1:'r3', g2:'r5'}
    g2IIs = {to(k): ['*'.join([g2name[v] for v in ls]) for ls in lsls] for k, lsls in g2IIs.items()}
    assert len(g2IIs) == 60
    #print(g2IIs)
    print('='*20, 'Alt5.g2IIs', '='*20)
    print(f'generaters = {generaters2}')
    print(len(g2IIs))
    for k, lsls in g2IIs.items():
        print(k, '\n\t', lsls)
    #return g2IIs

    g3 = mk(((0,2), (1,3)))
    g2expss = generater_elements_of_ordered_coordinate_only([g3,g1,g2], one=one,maybe_mul=None)
    g2expss = {to(g):expss for g, expss in g2expss.items()}
    #print(len(g2expss))
    assert len(g2expss) == 30
    where_g4 = map(mk, set(g2IIs) - set(g2expss))
    where_g4 = {g for g in where_g4 if g*g == one}
    where_g4 = {g4 for g4 in where_g4 if len(generater_elements_of_ordered_coordinate_only([g4,g3,g1,g2], one=one,maybe_mul=None))==60}
    #print(where_g4)
    assert len(where_g4) == 2
    g4 = mk(((0,1), (2,3)))
    g4_ = mk(((0,3), (1,2)))
    assert {g4, g4_} == where_g4
    generaters4 = [g4,g3,g1,g2]
    g2expss = generater_elements_of_ordered_coordinate_only(generaters4, one=one,maybe_mul=None)
    g2expss = {to(g):expss for g, expss in g2expss.items()}
    print('='*20, 'Alt5.g2expss', '='*20)
    print(f'generaters = {generaters4}')
    print(len(g2expss))
    for g, expss in g2expss.items():
        print(g, '\n\t', expss)
    assert len(g2expss) == len(g2IIs)

    g2pairpairs = generater_products_of_reversed_pair_powers_of_ordered_coordinate_only(generaters4, one=one, maybe_mul=None)
    g2pairpairs = {to(g):pairpairs for g,pairpairs in g2pairpairs.items()}
    print('='*20, 'Alt5.g2pairpairs', '='*20)
    for g, pairpairs in g2pairpairs.items():
        print(g)
        print(f'\t[((j,ej),(i,ei))] = {pairpairs}')
        print(f'\t[es] = {g2expss[g]}')

    return g2IIs, g2expss, g2pairpairs
def does_Alt5_has_subgroups_of_order_15():
    '''
    does G=Alt[5] has a subgroup H of order 15??
        |Alt[5]| = 60 = 4*15
    if H exists:
        H has g1^3=1, g2^5=1
    '''
    from .FinitePermutation import FinitePermutation, sort_disjoint_cycles
    from itertools import combinations

    mk = FinitePermutation.from_disjoint_cycles
    to = lambda self: sort_disjoint_cycles(self.to_disjoint_cycles())
    one = mk(())

    g2 = mk(((0,1,2,3,4),))
    g1 = mk(((0,1,2),))
    for a,b in combinations(range(1,5), 2):
        assert 0 < a < b
        r3 = ((0,a,b),)
        g1 = mk(r3)
        g2IIs = generaters2all_elements([g1, g2], one=one, maybe_mul=None, to_list=True)
        assert len(g2IIs) == 60
        if len(g2IIs) != 60:
            print(r3)
            if len(g2IIs) == 15:
                return True
            assert len(g2IIs) == 30
    else:
        return False


if __name__ == "__main__":
    assert not does_Alt5_has_subgroups_of_order_15()
    _t()
    #perm((0, 2, 1, 3, 4),) == 'r5*r3' == exps(0, 1, 2, 1)

    '''
==================== Alt5.g2IIs ====================
generaters = [FinitePermutation({2: 0, 0: 1, 1: 2}), FinitePermutation({4: 0, 0: 1, 1: 2, 2: 3, 3: 4})]
60
()
         ['', 'r3*r3*r3', 'r5*r5*r5*r5*r5']
((0, 1, 2),)
         ['r3', 'r5*r5*r5*r5*r5*r3']
((0, 1, 2, 3, 4),)
         ['r5', 'r3*r3*r3*r5']
((0, 2, 1),)
         ['r3*r3', 'r5*r5*r3*r5*r5']
((0, 2, 1, 3, 4),)
         ['r5*r3', 'r3*r3*r3*r5*r3']
((0, 2, 3, 4, 1),)
         ['r3*r5', 'r5*r5*r5*r5*r5*r3*r5']
((0, 2, 4, 1, 3),)
         ['r5*r5', 'r3*r3*r3*r5*r5']
((1, 3), (2, 4))
         ['r3*r5*r5', 'r5*r5*r5*r3*r3']
((0, 3, 1, 4, 2),)
         ['r5*r5*r5', 'r3*r5*r5*r3']
((2, 3, 4),)
         ['r3*r3*r5', 'r5*r5*r3*r5*r5*r5']
((0, 3), (2, 4))
         ['r5*r3*r5', 'r3*r3*r3*r5*r3*r5']
((1, 3, 4),)
         ['r3*r5*r3', 'r5*r3*r3*r5*r3*r5*r5*r5']
((0, 3), (1, 4))
         ['r5*r5*r3', 'r3*r3*r5*r5*r5']
((0, 3, 4),)
         ['r5*r3*r3', 'r3*r3*r3*r5*r3*r3']
((0, 3, 4, 1, 2),)
         ['r3*r5*r3*r3', 'r5*r3*r5*r3*r3*r5*r3*r5*r3']
((0, 4, 1, 2, 3),)
         ['r5*r5*r3*r3', 'r3*r3*r5*r5*r5*r3']
((0, 1, 2, 4, 3),)
         ['r5*r3*r3*r5', 'r3*r5*r5*r5*r5*r3']
((0, 4, 2, 3, 1),)
         ['r5*r5*r5*r3', 'r3*r5*r5*r3*r3']
((0, 3, 2, 1, 4),)
         ['r3*r5*r5*r5', 'r5*r5*r5*r3*r3*r5']
((0, 4, 3, 2, 1),)
         ['r5*r5*r5*r5', 'r3*r5*r5*r3*r5']
((0, 1, 3, 4, 2),)
         ['r3*r3*r5*r3', 'r5*r5*r3*r5*r5*r5*r3']
((0, 1, 4, 2, 3),)
         ['r5*r3*r5*r3', 'r3*r3*r3*r5*r3*r5*r3']
((0, 1, 3, 2, 4),)
         ['r3*r3*r5*r5', 'r5*r5*r3*r5*r5*r5*r5']
((0, 1, 4, 3, 2),)
         ['r5*r3*r5*r5', 'r3*r5*r5*r3*r5*r3*r3']
((0, 3, 1, 2, 4),)
         ['r3*r5*r3*r5', 'r5*r5*r5*r3*r5*r3*r3*r5*r5']
((0, 4, 3, 1, 2),)
         ['r5*r5*r3*r5', 'r3*r3*r5*r5*r5*r5']
((0, 2, 3, 1, 4),)
         ['r3*r5*r3*r5*r3', 'r5*r3*r5*r5*r5*r3*r5']
((0, 2, 4, 3, 1),)
         ['r5*r5*r3*r5*r3', 'r3*r5*r3*r3*r5']
((0, 3, 2, 4, 1),)
         ['r3*r3*r5*r3*r5', 'r5*r3*r5*r3*r5*r3']
((0, 4, 1, 3, 2),)
         ['r5*r3*r5*r3*r5', 'r3*r3*r5*r3*r5*r3*r3']
((0, 4, 3),)
         ['r3*r5*r5*r5*r5', 'r5*r3*r3*r5*r3*r3']
((1, 3, 2),)
         ['r5*r5*r5*r3*r5', 'r3*r5*r5*r3*r3*r5']
((0, 4), (2, 3))
         ['r3*r5*r5*r5*r3', 'r5*r5*r3*r5*r3*r5*r5']
((2, 4, 3),)
         ['r5*r5*r5*r5*r3', 'r3*r5*r5*r3*r5*r3']
((0, 2), (1, 3))
         ['r5*r5*r3*r3*r5', 'r3*r3*r5*r5*r5*r3*r5']
((0, 4, 1),)
         ['r5*r3*r5*r5*r5', 'r3*r3*r3*r5*r3*r5*r5*r5']
((0, 2), (1, 4))
         ['r5*r3*r3*r5*r5', 'r3*r5*r5*r5*r5*r3*r5']
((0, 3, 4, 2, 1),)
         ['r3*r3*r5*r3*r3', 'r5*r5*r3*r3*r5*r5']
((0, 4, 2, 1, 3),)
         ['r5*r3*r5*r3*r3', 'r3*r5*r3*r5*r3*r5']
((0, 2, 1, 4, 3),)
         ['r3*r5*r3*r5*r5', 'r5*r3*r3*r5*r3']
((1, 2, 3),)
         ['r5*r3*r5*r5*r5*r5', 'r3*r5*r5*r3*r5*r3*r3*r5*r5']
((1, 4), (2, 3))
         ['r3*r3*r5*r3*r5*r3', 'r5*r3*r5*r3*r5*r3*r3']
((1, 2, 4),)
         ['r5*r3*r5*r5*r5*r3', 'r3*r3*r5*r3*r3*r5*r3*r5*r3']
((1, 4, 2),)
         ['r3*r5*r3*r3*r5*r5', 'r5*r5*r3*r5*r3*r5']
((0, 4, 2),)
         ['r3*r5*r3*r5*r5*r5', 'r5*r3*r3*r5*r3*r5']
((0, 4), (1, 3))
         ['r3*r5*r3*r5*r3*r3', 'r5*r3*r5*r5*r5*r3*r5*r3']
((1, 4, 3),)
         ['r5*r5*r3*r5*r3*r3', 'r3*r3*r5*r3*r5*r5']
((0, 3, 1),)
         ['r5*r3*r5*r3*r5*r5', 'r3*r3*r5*r5*r5*r3*r5*r3']
((0, 3, 2),)
         ['r5*r5*r5*r3*r5*r3', 'r3*r5*r3*r5*r3*r5*r5']
((0, 1, 3),)
         ['r3*r5*r5*r5*r3*r5', 'r5*r5*r3*r5*r3*r5*r5*r5']
((0, 1, 4),)
         ['r5*r5*r5*r5*r3*r5', 'r3*r3*r5*r3*r3*r5*r5']
((0, 4), (1, 2))
         ['r3*r3*r5*r3*r5*r5*r5', 'r5*r5*r5*r5*r3*r5*r3']
((1, 2), (3, 4))
         ['r5*r3*r5*r3*r5*r5*r5', 'r3*r3*r5*r3*r5*r3*r3*r5*r5']
((0, 1), (2, 4))
         ['r5*r3*r3*r5*r3*r5*r3', 'r3*r5*r3*r5*r5*r5*r3']
((0, 1), (2, 3))
         ['r5*r5*r5*r3*r5*r3*r3', 'r3*r5*r3*r5*r5*r5*r5']
((0, 3), (1, 2))
         ['r3*r5*r5*r5*r3*r5*r3', 'r5*r3*r5*r3*r5*r3*r3*r5*r5']
((0, 1), (3, 4))
         ['r5*r3*r5*r3*r3*r5*r5', 'r3*r5*r3*r5*r3*r5*r5*r5']
((0, 2), (3, 4))
         ['r3*r5*r3*r5*r3*r3*r5*r5', 'r5*r5*r3*r3*r5*r3*r5*r3']
((0, 2, 3),)
         ['r5*r5*r3*r5*r3*r3*r5*r5', 'r3*r5*r5*r5*r3*r5*r3*r3']
((0, 2, 4),)
         ['r3*r5*r3*r3*r5*r3*r5*r3', 'r5*r5*r5*r5*r3*r5*r3*r3']
==================== Alt5.g2expss ====================
generaters = [FinitePermutation({1: 0, 0: 1, 3: 2, 2: 3}), FinitePermutation({2: 0, 0: 2, 3: 1, 1: 3}), FinitePermutation({2: 0, 0: 1, 1: 2}), FinitePermutation({4: 0, 0: 1, 1: 2, 2: 3, 3: 4})]
60
()
         [(0, 0, 0, 0)]
((0, 1, 2, 3, 4),)
         [(0, 0, 0, 1)]
((0, 2, 4, 1, 3),)
         [(0, 0, 0, 2)]
((0, 3, 1, 4, 2),)
         [(0, 0, 0, 3)]
((0, 4, 3, 2, 1),)
         [(0, 0, 0, 4)]
((0, 1, 2),)
         [(0, 0, 1, 0)]
((0, 2, 3, 4, 1),)
         [(0, 0, 1, 1)]
((1, 3), (2, 4))
         [(0, 0, 1, 2)]
((0, 3, 2, 1, 4),)
         [(0, 0, 1, 3)]
((0, 4, 3),)
         [(0, 0, 1, 4)]
((0, 2, 1),)
         [(0, 0, 2, 0)]
((2, 3, 4),)
         [(0, 0, 2, 1)]
((0, 1, 3, 2, 4),)
         [(0, 0, 2, 2)]
((0, 3), (1, 4))
         [(0, 0, 2, 3)]
((0, 4, 3, 1, 2),)
         [(0, 0, 2, 4)]
((0, 2), (1, 3))
         [(0, 1, 0, 0)]
((0, 3, 4, 2, 1),)
         [(0, 1, 0, 1)]
((2, 4, 3),)
         [(0, 1, 0, 2)]
((0, 1, 4),)
         [(0, 1, 0, 3)]
((0, 4, 1, 2, 3),)
         [(0, 1, 0, 4)]
((0, 3, 1),)
         [(0, 1, 1, 0)]
((1, 2), (3, 4))
         [(0, 1, 1, 1)]
((0, 2, 4),)
         [(0, 1, 1, 2)]
((0, 1, 4, 2, 3),)
         [(0, 1, 1, 3)]
((0, 4, 1, 3, 2),)
         [(0, 1, 1, 4)]
((1, 2, 3),)
         [(0, 1, 2, 0)]
((0, 2, 1, 3, 4),)
         [(0, 1, 2, 1)]
((0, 3), (2, 4))
         [(0, 1, 2, 2)]
((0, 1, 4, 3, 2),)
         [(0, 1, 2, 3)]
((0, 4, 1),)
         [(0, 1, 2, 4)]
((0, 1), (2, 3))
         [(1, 0, 0, 0)]
((1, 3, 4),)
         [(1, 0, 0, 1)]
((0, 3, 1, 2, 4),)
         [(1, 0, 0, 2)]
((0, 2, 1, 4, 3),)
         [(1, 0, 0, 3)]
((0, 4, 2),)
         [(1, 0, 0, 4)]
((1, 3, 2),)
         [(1, 0, 1, 0)]
((0, 3, 4),)
         [(1, 0, 1, 1)]
((0, 1, 2, 4, 3),)
         [(1, 0, 1, 2)]
((0, 2), (1, 4))
         [(1, 0, 1, 3)]
((0, 4, 2, 3, 1),)
         [(1, 0, 1, 4)]
((0, 3, 2),)
         [(1, 0, 2, 0)]
((0, 1), (3, 4))
         [(1, 0, 2, 1)]
((1, 2, 4),)
         [(1, 0, 2, 2)]
((0, 2, 3, 1, 4),)
         [(1, 0, 2, 3)]
((0, 4, 2, 1, 3),)
         [(1, 0, 2, 4)]
((0, 3), (1, 2))
         [(1, 1, 0, 0)]
((0, 2), (3, 4))
         [(1, 1, 0, 1)]
((0, 1), (2, 4))
         [(1, 1, 0, 2)]
((1, 4), (2, 3))
         [(1, 1, 0, 3)]
((0, 4), (1, 3))
         [(1, 1, 0, 4)]
((0, 2, 3),)
         [(1, 1, 1, 0)]
((0, 1, 3, 4, 2),)
         [(1, 1, 1, 1)]
((0, 3, 2, 4, 1),)
         [(1, 1, 1, 2)]
((1, 4, 3),)
         [(1, 1, 1, 3)]
((0, 4), (1, 2))
         [(1, 1, 1, 4)]
((0, 1, 3),)
         [(1, 1, 2, 0)]
((0, 3, 4, 1, 2),)
         [(1, 1, 2, 1)]
((0, 2, 4, 3, 1),)
         [(1, 1, 2, 2)]
((1, 4, 2),)
         [(1, 1, 2, 3)]
((0, 4), (2, 3))
         [(1, 1, 2, 4)]
==================== Alt5.g2pairpairs ====================
((0, 3), (1, 2))
        [((j,ej),(i,ei))] = [((1, 1), (0, 1))]
        [es] = [(1, 1, 0, 0)]
((0, 2, 3),)
        [((j,ej),(i,ei))] = [((2, 1), (0, 1))]
        [es] = [(1, 1, 1, 0)]
((1, 2, 3),)
        [((j,ej),(i,ei))] = [((2, 2), (0, 1))]
        [es] = [(0, 1, 2, 0)]
((0, 2, 4),)
        [((j,ej),(i,ei))] = [((3, 1), (0, 1))]
        [es] = [(0, 1, 1, 2)]
((0, 3, 4, 1, 2),)
        [((j,ej),(i,ei))] = [((3, 2), (0, 1))]
        [es] = [(1, 1, 2, 1)]
((0, 4, 2, 1, 3),)
        [((j,ej),(i,ei))] = [((3, 3), (0, 1))]
        [es] = [(1, 0, 2, 4)]
((1, 4, 3),)
        [((j,ej),(i,ei))] = [((3, 4), (0, 1))]
        [es] = [(1, 1, 1, 3)]
((1, 3, 2),)
        [((j,ej),(i,ei))] = [((2, 1), (1, 1))]
        [es] = [(1, 0, 1, 0)]
((0, 1, 3),)
        [((j,ej),(i,ei))] = [((2, 2), (1, 1))]
        [es] = [(1, 1, 2, 0)]
((0, 3, 2, 1, 4),)
        [((j,ej),(i,ei))] = [((3, 1), (1, 1))]
        [es] = [(0, 0, 1, 3)]
((0, 4, 1),)
        [((j,ej),(i,ei))] = [((3, 2), (1, 1))]
        [es] = [(0, 1, 2, 4)]
((2, 3, 4),)
        [((j,ej),(i,ei))] = [((3, 3), (1, 1))]
        [es] = [(0, 0, 2, 1)]
((0, 1, 2, 4, 3),)
        [((j,ej),(i,ei))] = [((3, 4), (1, 1))]
        [es] = [(1, 0, 1, 2)]
((0, 2, 1, 3, 4),)
        [((j,ej),(i,ei))] = [((3, 1), (2, 1))]
        [es] = [(0, 1, 2, 1)]
((0, 3), (1, 4))
        [((j,ej),(i,ei))] = [((3, 2), (2, 1))]
        [es] = [(0, 0, 2, 3)]
((0, 4, 2, 3, 1),)
        [((j,ej),(i,ei))] = [((3, 3), (2, 1))]
        [es] = [(1, 0, 1, 4)]
((2, 4, 3),)
        [((j,ej),(i,ei))] = [((3, 4), (2, 1))]
        [es] = [(0, 1, 0, 2)]
((0, 3, 4),)
        [((j,ej),(i,ei))] = [((3, 1), (2, 2))]
        [es] = [(1, 0, 1, 1)]
((0, 4, 1, 2, 3),)
        [((j,ej),(i,ei))] = [((3, 2), (2, 2))]
        [es] = [(0, 1, 0, 4)]
((1, 3), (2, 4))
        [((j,ej),(i,ei))] = [((3, 3), (2, 2))]
        [es] = [(0, 0, 1, 2)]
((0, 1, 4, 3, 2),)
        [((j,ej),(i,ei))] = [((3, 4), (2, 2))]
        [es] = [(0, 1, 2, 3)]
'''
