

'''
FinitePermutation
permutation
k-cycle
'''

__all__ = '''
    IFinitePermutation
        FinitePermutationABC__mapping
            FinitePermutation


    is_disjoint_cycles
    is_2cycles
    is_cycles
        is_cycle
        is_2cycle
        are_cycles_disjoint
    is_permutation_mapping

    is_permutation_even__2cycles
    is_permutation_even__cycles

    permutation_cycles_to_2cycles
    permutation_cycles2mapping
    permutation_disjoint_cycles2mapping
    permutation_mapping2disjoint_cycles

    sort_disjoint_cycles
        sort_cycle

    is_permutation_even__mapping
    inv_permutation_mapping
    pow__permutation_mapping
        eval_pow_to_1__disjoint_cycles
    call__permutation_mapping
    mul__permutation_mapping

    '''.split()

'''
tools:
    override
    is_tuple
    is_even
    sort_inner_cycles
'''

from abc import ABC, abstractmethod
from types import MappingProxyType
from seed.types.CachedProperty import CachedProperty
from seed.math.lcm import lcm_many
from seed.math.power_of import power_of
from seed.helper.repr_input import repr_helper


def override(f): return f

#def is_sequence
def is_tuple(obj):
    return type(obj) is tuple
def is_cycle(cycle):
    return is_tuple(cycle) and len(set(cycle)) == len(cycle)
def is_2cycle(cycle):
    return is_cycle(cycle) and len(cycle) == 2
def _is_cycles(cycles, *, all_2cycles):
    return is_tuple(cycles) and all(map(is_2cycle if all_2cycles else is_cycle, cycles))
def are_cycles_disjoint(cycles):
    'precondition: is_cycles(cycles)'
    return len(set({a for cycle in cycles for a in cycle})) == sum(map(len, cycles)) and all(L >= 2 for L in map(len, cycles))
def is_disjoint_cycles(cycles):
    return _is_cycles(cycles, all_2cycles=False) and are_cycles_disjoint(cycles)
def is_2cycles(cycles):
    return _is_cycles(cycles, all_2cycles=True)
def is_cycles(cycles, *, all_2cycles=False):
    return _is_cycles(cycles, all_2cycles=all_2cycles)
def is_permutation_mapping(m):
    'precondition: m is a mapping'
    return set(m.keys()) == set(m.values()) and all(k != v for k, v in m.items())

def is_even(n):
    return not (n&1)
def is_permutation_even__2cycles(_2cycles):
    'precondition: is_2cycles(_2cycles)'
    return is_even(len(_2cycles))
def is_permutation_even__cycles(cycles):
    'precondition: is_cycles(cycles); (a,) is even; (a, b) is odd'
    n = sum(len(cycle) - 1 for cycle in cycles if cycle)
    return is_even(n)
def permutation_disjoint_cycles2mapping(disjoint_cycles):
    'precondition: is_disjoint_cycles'
    assert is_disjoint_cycles(disjoint_cycles)

    m = {}
    def put(k, v):
        L = len(m)
        m[k] = v
        if not len(m) > L:
            raise ValueError('not disjoint_cycles')
    for cycle in disjoint_cycles:
        assert len(cycle) >= 2
        #raise ValueError('not disjoint_cycles')
        a0 = cycle[-1]

        k = a0
        for v in cycle:
            put(k, v)
            k = v

    assert is_permutation_mapping(m)
    return m

def permutation_cycles_to_2cycles(cycles):
    r'''precondition: is_cycles

(a, b, c, d) = (a,d)(a,c)(a,b)
'''
    assert is_cycles(cycles)

    _2cycles = []
    for cycle in cycles:
        if len(cycle) < 2: continue
        a = cycle[0]
        #bug: _2cycles.extend((a, x) for x in cycle[-1::-1])
        #   should exclude the first one
        _2cycles.extend((a, x) for x in cycle[-1:0:-1])

    _2cycles = tuple(_2cycles)
    #print_err(_2cycles)
    assert is_2cycles(_2cycles)
    return _2cycles



def permutation_cycles2mapping(cycles):
    r'''precondition: is_cycles

r = (As...,v,v_)(Bs...,k,v)
    As /-\ Bs == {}
    r(k) = v_
    r(v_) = As[0]
    r(v) = Bs[0]
    r = (k,v_,As...,v,Bs...)
         ^^^        ^^^

'''
    assert is_cycles(cycles)

    m = {}
    tmp = {}
    def put(k, v):
        v_ = m.get(v, v)
        tmp[k] = v_
    for cycle in cycles:
        if len(cycle) < 2: continue
        a0 = cycle[-1]

        k = a0
        for v in cycle:
            put(k, v)
            k = v
        m.update(tmp)
        tmp.clear()

    #print_err(m)
    assert is_permutation_mapping(m)
    return m


def permutation_mapping2disjoint_cycles(permutation_mapping):
    'precondition: is_permutation_mapping'
    # (a, b) is odd permutation
    assert is_permutation_mapping(permutation_mapping)

    s = set()
    disjoint_cycles = []
    for k, v in permutation_mapping.items():
        if k in s: continue

        k0 = k
        cycle = []
        while True:
            cycle.append(k)
            s.add(k)

            if v == k0: break
            k = v
            v = permutation_mapping[k]

        if not len(cycle) >= 2: raise ValueError('not permutation_mapping')
        disjoint_cycles.append(tuple(cycle))
    disjoint_cycles = tuple(disjoint_cycles)

    #print_err(permutation_mapping)
    #print_err(disjoint_cycles)
    assert is_disjoint_cycles(disjoint_cycles)
    return disjoint_cycles

def is_permutation_even__mapping(permutation_mapping):
    'precondition: is_permutation_mapping'
    disjoint_cycles = permutation_mapping2disjoint_cycles(permutation_mapping)
    return is_permutation_even__cycles(disjoint_cycles)



def eval_pow_to_1__disjoint_cycles(disjoint_cycles):
    '''-> PInt
precondition: disjoint_cycles

eval_pow_to_1__disjoint_cycles permutation = min {i >= 1 | permutation^i == 1}
'''
    Ls = set(map(len, disjoint_cycles))
    exp = lcm_many(Ls)
    assert exp >= 1
    return exp




def inv_permutation_mapping(permutation_mapping):
    return {v:k for k, v in permutation_mapping.items()}
def pow__permutation_mapping(permutation_mapping, exp, pow_to_1):
    return power_of(permutation_mapping, exp, one={}, mul=mul__permutation_mapping, power_modulus=pow_to_1)

def call__permutation_mapping(permutation_mapping, k):
    return permutation_mapping.get(k, k)
def mul__permutation_mapping(lhs, rhs):
    "lhs * rhs = lhs . rhs where a' = lhs . rhs $ a"
    m = {}
    s = set()
    for k, v in rhs.items():
        v_ = lhs.get(v, v); s.add(v)
        if k != v_:
            m[k] = v_

    ks = set(lhs) - s
    m.update((k, lhs[k]) for k in ks)

    assert is_permutation_mapping(m)
    return m

class IFinitePermutation(ABC):
    '''
element :: a
permutation_mapping :: Map a a
    assert (k != v for k, v in permutation_mapping.items())
_2cycle :: (a, a)
    two-element swap
cycle :: [a]
_2cycles :: [(a, a)]
cycles :: [[a]]
disjoint_cycles :: [[a]]
    assert len({a for cycle in disjoint_cycles for a in cycle}) == sum(map(len, disjoint_cycles))
    assert all(L >= 2 for L in map(len, cycles))

even permutation
    permutation obtainable from an even number of two-element swaps
'''
    __slots__ = ()

    #NO def from_disjoint_2cycles(cls, _2cycles):
    @classmethod
    @abstractmethod
    def from_2cycles(cls, _2cycles):
        '[(a,a)] -> IFinitePermutation<a>'
    @classmethod
    @abstractmethod
    def from_disjoint_cycles(cls, disjoint_cycles):
        '[[a]] -> IFinitePermutation<a>'
    @classmethod
    @abstractmethod
    def from_cycles(cls, cycles):
        '[[a]] -> IFinitePermutation<a>'
    @classmethod
    @abstractmethod
    def from_permutation_mapping(cls, element2element_mapping):
        'Map a a -> IFinitePermutation<a>'

    @abstractmethod
    def to_2cycles(self):
        '-> [(a,a)]'
    @abstractmethod
    def to_disjoint_cycles(self):
        '-> [[a]]'
    @abstractmethod
    def to_permutation_mapping(self):
        '-> Map a a'


    @abstractmethod
    def to_inv_2cycles(self):
        '-> [(a,a)]'
    @abstractmethod
    def to_inv_disjoint_cycles(self):
        '-> [[a]]'
    @abstractmethod
    def to_inv_permutation_mapping(self):
        '-> Map a a'

    @abstractmethod
    def __call__(self, element):
        'a -> a'
    @abstractmethod
    def __mul__(self, other):
        '-> IFinitePermutation'
    @abstractmethod
    def __pow__(self, exp):
        '-> IFinitePermutation'
    @abstractmethod
    def __invert__(self):
        '-> IFinitePermutation'


    @abstractmethod
    def is_permutation_even(self):
        '-> Bool'
    @abstractmethod
    def get_pow_to_1(self):
        '-> PInt'

    @abstractmethod
    def __eq__(self, other):
        raise NotImplementedError
    @abstractmethod
    def __hash__(self):
        raise NotImplementedError

    '''
    @abstractmethod
    def repr_as_2cycles(self):
        '-> str'
    @abstractmethod
    def repr_as_disjoint_cycles(self):
        '-> str'
    '''

class FinitePermutationABC__mapping(IFinitePermutation):
    '''
abstractmethod:
    from_permutation_mapping
    to_permutation_mapping
'''
    __slots__ = ()

    #NO def from_disjoint_2cycles(cls, _2cycles):
    @classmethod
    @override
    def from_2cycles(cls, _2cycles):
        '[(a,a)] -> IFinitePermutation<a>'
        return cls.from_cycles(_2cycles)
    @classmethod
    @override
    def from_disjoint_cycles(cls, disjoint_cycles):
        '[[a]] -> IFinitePermutation<a>'
        #return cls.from_cycles(disjoint_cycles)
        m = permutation_disjoint_cycles2mapping(disjoint_cycles)
        return cls.from_permutation_mapping(m)
    @classmethod
    @override
    def from_cycles(cls, cycles):
        '[[a]] -> IFinitePermutation<a>'
        m = permutation_cycles2mapping(cycles)
        return cls.from_permutation_mapping(m)
    '''
    @classmethod
    @abstractmethod
    def from_permutation_mapping(cls, element2element_mapping):
        'Map a a -> IFinitePermutation<a>'
    '''

    @override
    def to_2cycles(self):
        '-> [(a,a)]'
        disjoint_cycles = self.to_disjoint_cycles()
        _2cycles = permutation_cycles_to_2cycles(disjoint_cycles)
        return _2cycles

    @override
    def to_disjoint_cycles(self):
        '-> [[a]]'
        m = self.to_permutation_mapping()
        disjoint_cycles = permutation_mapping2disjoint_cycles(m)
        return disjoint_cycles

    '''
    @abstractmethod
    def to_permutation_mapping(self):
        '-> Map a a'
    '''


    @override
    def to_inv_2cycles(self):
        '-> [(a,a)]'
        inv_disjoint_cycles = self.to_inv_disjoint_cycles()
        inv__2cycles = permutation_cycles_to_2cycles(inv_disjoint_cycles)
        return inv__2cycles

    @override
    def to_inv_disjoint_cycles(self):
        '-> [[a]]'
        m = self.to_inv_permutation_mapping()
        inv_disjoint_cycles = permutation_mapping2disjoint_cycles(m)
        return inv_disjoint_cycles

    @override
    def to_inv_permutation_mapping(self):
        '-> Map a a'
        m = self.to_permutation_mapping()
        return inv_permutation_mapping(m)

    @override
    def __call__(self, element):
        'a -> a'
        m = self.to_permutation_mapping()
        return call__permutation_mapping(m, element)
    @override
    def __mul__(self, other):
        '-> IFinitePermutation'
        lhs = self.to_permutation_mapping()
        rhs = other.to_permutation_mapping()
        m = mul__permutation_mapping(lhs, rhs)
        return type(self).from_permutation_mapping(m)
    @override
    def __pow__(self, exp):
        '-> IFinitePermutation'
        pow_to_1 = self.get_pow_to_1()
        exp %= pow_to_1
        _exp = pow_to_1 - exp
        if _exp < exp:
            exp = _exp
            m = self.to_inv_permutation_mapping()
        else:
            m = self.to_permutation_mapping()
        m = pow__permutation_mapping(m, exp, pow_to_1)
        return type(self).from_permutation_mapping(m)

    @override
    def __invert__(self):
        '-> IFinitePermutation'
        m = self.to_inv_permutation_mapping()
        return type(self).from_permutation_mapping(m)



    @override
    def is_permutation_even(self):
        '-> Bool'
        m = self.to_permutation_mapping()
        return is_permutation_even__mapping(m)
    @override
    def get_pow_to_1(self):
        '-> PInt'
        disjoint_cycles = self.to_disjoint_cycles()
        exp = eval_pow_to_1__disjoint_cycles(disjoint_cycles)
        return exp


    @override
    def __eq__(self, other):
        lhs = self.to_permutation_mapping()
        rhs = other.to_permutation_mapping()
        return lhs == rhs

    @override
    def __hash__(self):
        m = self.to_permutation_mapping()
        return hash(frozenset(m.items()))



def sort_cycle(cycle):
    i = cycle.index(min(cycle))
    cycle = cycle[i:] + cycle[:i]
    return cycle
def _iter_sort_inner_cycles(cycles):
    # -> Iter
    return map(sort_cycle, cycles)
def sort_inner_cycles(cycles):
    # -> tuple
    assert is_cycles(cycles)
    return tuple(_iter_sort_inner_cycles(cycles))

def sort_disjoint_cycles(disjoint_cycles):
    # -> tuple
    assert is_disjoint_cycles(disjoint_cycles)
    disjoint_cycles = _sort_disjoint_cycles(disjoint_cycles)
    return tuple(disjoint_cycles)
def _sort_disjoint_cycles(disjoint_cycles):
    # -> list
    disjoint_cycles = sorted(_iter_sort_inner_cycles(disjoint_cycles))
    # not bug: disjoint_cycles.sort() # since disjoint!!!
    return disjoint_cycles

class FinitePermutation(FinitePermutationABC__mapping):
    '''

>>> mk = FinitePermutation.from_disjoint_cycles
>>> to = lambda self: list(sort_disjoint_cycles(self.to_disjoint_cycles()))
>>> p1 = mk(((0,1,2),))
>>> p2 = mk(((0,1,2,3,4),))
>>> to(p1*p2)
[(0, 2, 3, 4, 1)]
>>> to(p2*p1)
[(0, 2, 1, 3, 4)]


>>> to(p1**2)
[(0, 2, 1)]
>>> p1**2 == p1**(-1) == ~p1
True
>>> to(p2**2)
[(0, 2, 4, 1, 3)]
>>> p2**4 == p2**(-1) == ~p2
True


# __repr__
>>> p0 = mk(())
>>> p0
FinitePermutation({})


# from_cycles # above is from_disjoint_cycles
>>> p3 = FinitePermutation.from_cycles(((), (1,), (2,3), (3,4,5), (2,4)))
>>> to(p3)
[(2, 5), (3, 4)]
>>> p4 = FinitePermutation.from_cycles(((), (1,), (2,3), (3,4,5), (2,4), (1,2)))
>>> to(p4)
[(1, 5, 2), (3, 4)]


# is_permutation_even
>>> p0.is_permutation_even()
True
>>> p1.is_permutation_even()
True
>>> p2.is_permutation_even()
True
>>> p3.is_permutation_even()
True
>>> p4.is_permutation_even()
False


# to_2cycles/from_2cycles/to_inv_2cycles
>>> cs = p4.to_2cycles()
>>> is_2cycles(cs)
True
>>> FinitePermutation.from_2cycles(cs) == p4
True

>>> cs = p4.to_inv_2cycles()
>>> is_2cycles(cs)
True
>>> FinitePermutation.from_2cycles(cs) * p4 == p0
True


#to_inv_disjoint_cycles
>>> sort_disjoint_cycles(p4.to_inv_disjoint_cycles())
((1, 2, 5), (3, 4))

#to_inv_permutation_mapping
>>> mul__permutation_mapping(p4.to_inv_permutation_mapping(), p4.to_permutation_mapping())
{}

>>> ~p4 * p4
FinitePermutation({})


# __call__
>>> list(map(p4, [1,5,2,3,4]))
[5, 2, 1, 4, 3]

# __eq__
>>> p4 == p4
True
>>> p4 != p1
True

# __hash__
>>> len({p4, p3, p1, p0})
4

'''
    def __init__(self, permutation_mapping):
        self.__permutation_mapping = MappingProxyType(dict(permutation_mapping))

    @classmethod
    @override
    def from_permutation_mapping(cls, permutation_mapping):
        return cls(permutation_mapping)
    @override
    def to_permutation_mapping(self):
        return self.__permutation_mapping


    #############
    def __repr__(self):
        return repr_helper(self, dict(self.to_permutation_mapping()))


    #################### cache
    @CachedProperty
    def _hash_value(self):
        return FinitePermutationABC__mapping.__hash__(self)
    @CachedProperty
    def _is_permutation_even(self):
        return FinitePermutationABC__mapping.is_permutation_even(self)
    @CachedProperty
    def _inv_permutation_mapping(self):
        return MappingProxyType(FinitePermutationABC__mapping.to_inv_permutation_mapping(self))
    @CachedProperty
    def _disjoint_cycles(self):
        return FinitePermutationABC__mapping.to_disjoint_cycles(self)

    @override
    def __hash__(self):
        return self._hash_value
    @override
    def is_permutation_even(self):
        return self._is_permutation_even
    @override
    def to_inv_permutation_mapping(self):
        return self._inv_permutation_mapping
    @override
    def to_disjoint_cycles(self):
        return self._disjoint_cycles




def _t():
    mk = FinitePermutation.from_disjoint_cycles
    to = lambda self: sort_disjoint_cycles(self.to_disjoint_cycles())
    p1 = mk(((0,1,2),))
    p2 = mk(((0,1,2,3,4),))
    assert to(p1*p2) == [(0, 2, 3, 4, 1)]
    assert to(p2*p1) == [(0, 2, 1, 3, 4)]

    print(~p1)

#_t()


if __name__ == "__main__":
    from seed.tiny import print_err
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):

if __name__ == '__main__':
    from seed.helper.print_global_names import print_global_names
    #print_global_names(globals())

