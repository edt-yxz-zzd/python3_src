r'''[[[
e ../../python3_src/seed/helper/hash4set.py


seed.helper.hash4set
py -m nn_ns.app.debug_cmd   seed.helper.hash4set -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.helper.hash4set:__doc__ -ht # -ff -df


[[
less ~/../usr/lib/python3.11/_collections_abc.py
tail -n +632 ~/../usr/lib/python3.11/_collections_abc.py | head -n 32 > /sdcard/0my_files/tmp/-1tmp
view /sdcard/0my_files/tmp/-1tmp
===
class Set(Collection):
    ... ...
    def _hash(self):
        ... ...
        MAX = sys.maxsize
        MASK = 2 * MAX + 1
        n = len(self)
        h = 1927868237 * (n + 1)
        h &= MASK
        for x in self:
            hx = hash(x)
            h ^= (hx ^ (hx << 16) ^ 89869747)  * 3644798167
            h &= MASK
        h ^= (h >> 11) ^ (h >> 25)
        h = h * 69069 + 907133923
        h &= MASK
        if h > MAX:
            h -= MASK + 1
        if h == -1:
            h = 590923713
        return h
===
class Mapping(Collection):
    has no ._hash()
===
]]

==>>:
        h &= MASK
        # [0 <= h <= MASK == 1+2*MAX]
        # [0 <= h <= MAX] or [1+MAX <= h <= MASK == 1+2*MAX]
        if h > MAX:
            h -= MASK + 1 # h -= 2+2*MAX
        # [0 <= h <= MAX] or [-(1+MAX) <= h <= -1]
        # [-(1+MAX) <= h <= MAX]
        if h == -1:
            h = 590923713



>>> import sys
>>> sys.maxsize
9223372036854775807
>>> sys.maxsize.bit_count()
63
>>> sys.maxsize.bit_length()
63
>>> bin(sys.maxsize)
'0b111111111111111111111111111111111111111111111111111111111111111'
>>> sys.maxsize == -1+2**63
True
>>> 1+2*sys.maxsize == -1+2**64
True

>>> u=(590923713)
>>> u.bit_length()
30
>>> u.bit_count()
14
>>> bin(u)
'0b100011001110001100011111000001'





>>> hash5set_(frozenset(range(8)))
574461802094412880
>>> hash(frozenset(range(8)))
574461802094412880





]]]'''#'''
__all__ = r'''
hash5set_
    hash5setII_
perhash5elem6set_
    perhash5hash4elem6set_
'''.split()#'''

___begin_mark_of_excluded_global_names__0___ = ...
import sys
MAX = sys.maxsize
MASK = 2 * MAX + 1
assert MAX.bit_count() == MAX.bit_length()
assert MASK.bit_count() == MASK.bit_length()
___end_mark_of_excluded_global_names__0___ = ...


def perhash5elem6set_(x, /):
    'x -> perhash4elem6set{x}/int'
    hx = hash(x)
    return perhash5hash4elem6set_(hx)
def perhash5hash4elem6set_(hx, /):
    'hash4elem6set{:=hash(x)} -> perhash4elem6set{x}/int'
    return ((hx ^ (hx << 16) ^ 89869747)  * 3644798167) & MASK

def hash5set_(a_set, /):
    return hash5setII_(len(a_set), map(perhash5elem6set_, a_set))
def hash5setII_(len_set, iter_perhashs4elem6set, /):
    'len_set{:=len(set)} -> (Iter int){:=map(perhash5elem6set_, set)} -> hash4set/int'
    n = len_set
    h = 1927868237 * (n + 1)
    h &= MASK
    for ph in iter_perhashs4elem6set:
        h ^= ph
        h &= MASK
    h ^= (h >> 11) ^ (h >> 25)
    h = h * 69069 + 907133923
    h &= MASK
    if h > MAX:
        h -= MASK + 1
    if h == -1:
        h = 590923713
    return h

from seed.helper.hash4set import hash5set_, hash5setII_, perhash5elem6set_, perhash5hash4elem6set_
