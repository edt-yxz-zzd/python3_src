

__all__ = '''
    arbitrary_radix_reprBE2number
    number2arbitrary_radix_reprLE
    number2iter_arbitrary_radix_reprLE

    arbitrary_radix_repr_maypairLE2number
    number2arbitrary_radix_repr_maypairLE
    '''.split()
# ArbitraryRadixNumber
# arbitrary_radix_reprBE
# arbitrary_radix_reprLE
from itertools import chain

def arbitrary_radix_reprBE2number(iter_numbers, radix, zero):
    # number can be any thing
    # no "0 <= digit < radix"
    # no "0 < radix"
    n = zero
    for digit in iter_numbers:
        n *= radix
        n += digit
    return n

def arbitrary_radix_repr_maypairLE2number(may_numbers_head, radix, zero):
    if may_numbers_head == ():
        return zero
    tail, head = may_numbers_head
    numbers = chain([head], reversed(tail))
    return arbitrary_radix_reprBE2number(numbers, radix, zero)

'''
def arbitrary_radix_reprLE2number(iter_numbers, radix, zero, one):
    # number can be any thing
    # no "0 <= digit < radix"
    # no "0 < radix"
    n = zero
    weight = one
    for digit in iter_numbers:
        n += weight * digit
        weight *= radix
    return n
'''

def number2arbitrary_radix_repr_maypairLE(u, radix, zero, divmodArb, TailType=tuple):
    ls = number2arbitrary_radix_reprLE(u, radix, zero, divmodArb, ReturnType=tuple)
    if not ls: return ()
    return TailType(ls[:-1]), ls[-1]

def number2arbitrary_radix_reprLE(u, radix, zero, divmodArb, ReturnType=tuple):
    return ReturnType(
            number2iter_arbitrary_radix_reprLE(u, radix, zero, divmodArb))
def number2iter_arbitrary_radix_reprLE(q, radix, zero, divmodArb):
    while q != zero:
        q, r = divmodArb(q, radix)
        yield r

