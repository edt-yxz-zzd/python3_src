

r'''
field2x_polynomial
    uint as polynomial over Field[2,x]
'''



__all__ = '''
    Field2xPolynomial
    field2x_mod
    field2x_mod__bytes
    field2x_divmod
    field2x_divmod__bytes
'''.split()


import functools
from numbers import Integral
from seed.helper.check_utils import to_uint, to_pint
from seed.int_tools.uint_bits_utils import std_data_bitorder, bitseqLE2uint




@functools.total_ordering
class Field2xPolynomial:
    r'''uint as polynomial over Field[2,x]

>>> Field2xPolynomial(5) + Field2xPolynomial(1)
Field2xPolynomial(4)
>>> Field2xPolynomial(5) * Field2xPolynomial(1)
Field2xPolynomial(5)
>>> Field2xPolynomial(5) * Field2xPolynomial(3)
Field2xPolynomial(15)
>>> Field2xPolynomial(5) * Field2xPolynomial(5)
Field2xPolynomial(17)
>>> Field2xPolynomial(5) % Field2xPolynomial(1)
Field2xPolynomial(0)
>>> Field2xPolynomial(5) % Field2xPolynomial(3)
Field2xPolynomial(0)
>>> Field2xPolynomial(5) % Field2xPolynomial(5)
Field2xPolynomial(0)
>>> Field2xPolynomial(5) % Field2xPolynomial(2)
Field2xPolynomial(1)
>>> Field2xPolynomial(5) % Field2xPolynomial(4)
Field2xPolynomial(1)
>>> divmod(Field2xPolynomial(5), Field2xPolynomial(4))
(Field2xPolynomial(1), Field2xPolynomial(1))
>>> divmod(Field2xPolynomial(5), Field2xPolynomial(3))
(Field2xPolynomial(3), Field2xPolynomial(0))
>>> Field2xPolynomial(5) // Field2xPolynomial(1)
Field2xPolynomial(5)
>>> Field2xPolynomial(5) / Field2xPolynomial(3)
Field2xPolynomial(3)
>>> Field2xPolynomial(5).gcd(Field2xPolynomial(3))
Field2xPolynomial(3)
>>> Field2xPolynomial(5).gcd_ex(Field2xPolynomial(4))
(Field2xPolynomial(1), (Field2xPolynomial(1), Field2xPolynomial(1)))
>>> Field2xPolynomial(5).invmod(Field2xPolynomial(4))
Field2xPolynomial(1)
>>> Field2xPolynomial(5) << 3
Field2xPolynomial(40)
>>> Field2xPolynomial(5) >> 3
Field2xPolynomial(0)
'''
    __slots__ = ('__u',)
    def __init__(self, u=0):
        self.__u = to_uint(u, 'u')

    def is_one(self):
        return self.__u == 1
    def is_zero(self):
        return self.__u == 0

    def from_uint(self, u):
        return type(self)(u)
    def as_uint(self):
        return self.__u
    def __repr__(self):
        return '{}({})'.format(type(self).__name__, self.__u)
    def __hash__(self):
        return hash(self.__u)

    def __known(self, other):
        return isinstance(other, type(self))
    def __eq__(self, other):
        if not self.__known(other):
            return NotImplemented
        return self.__u == other.__u
    def __lt__(self, other):
        if not self.__known(other):
            return NotImplemented
        return self.__u < other.__u

    def __lshift__(self, i):
        u = self.__u << i
        return self.from_uint(u)

    def __rshift__(self, i):
        u = self.__u >> i
        return self.from_uint(u)




    def gcd(self, other):
        if not self.__known(other):
            raise NotImplementedError
        return self.__gcd(other)

    def __gcd(lhs, rhs):
        from_uint = lhs.from_uint
        while rhs:
            lhs, rhs = rhs, lhs % rhs
        return from_uint(lhs.__u)

    def ginvmod(self, other):
        'gcd, ginv ==>> (ginv*self mod other) == gcd'
        gcd, (A, B) = self.gcd_ex(other)
        return gcd, A
    def try_invmod(self, other):
        'return invmod if gcd==1 else None'
        gcd, ginv = self.ginvmod(other)
        if not gcd.is_one():
            return None
        return ginv
    def invmod(self, other):
        'inv ==>> (inv*self mod other) == 1 ==>> inv == (self**-1 mod other)'
        inv = self.try_invmod(other)
        if inv is None:
            raise ValueError('not gcd.is_one()')
        return inv

    def gcd_ex(self, other):
        'gcd, (A, B) ==>> A*self + B*other == gcd'
        if not self.__known(other):
            raise NotImplementedError
        return self.__gcd_ex(other)

    def __gcd_ex(lhs, rhs):
        from_uint = lhs.from_uint
        copy = lambda x: from_uint(x.__u)
        L, R = lhs, rhs
        # at end: lhs == gcd; rhs == 0;
        # lhs == A*L + B*R
        # rhs == C*L + D*R
        A, B = map(from_uint, [1, 0])
        C, D = map(from_uint, [0, 1])
        while rhs:
            q, r = divmod(lhs, rhs)
            # lhs = q*rhs + r
            # r = q*rhs - lhs = (q*C-A)*L + (q*D-B)*R
            # rhs' = r = C'*L + D'*R
            # C', D' = (q*C-A), (q*D-B)
            # lhs' = rhs = A'*L + B'*R
            # A', B' = C, D

            A, B, C, D = C, D, (q*C-A), (q*D-B)
            lhs, rhs = rhs, r

        gcd, A, B = map(copy, [lhs, A, B])
        return gcd, (A, B)



    def __bool__(self):
        return bool(self.__u)
    def __add__(self, other):
        if not self.__known(other):
            return NotImplemented
        return self.from_uint(self.__u ^ other.__u)

    __sub__ = __add__

    def __truediv__(self, other):
        'exactly divided'
        if not self.__known(other):
            return NotImplemented
        q, r = self.__divmod(other)
        if r:
            raise ValueError('other not divides self')
        return q
    def __floordiv__(self, other):
        if not self.__known(other):
            return NotImplemented
        q, r = self.__divmod(other)
        return q

    def __divmod__(self, other):
        if not self.__known(other):
            return NotImplemented
        return self.__divmod(other)
    def __divmod(self, other):
        a, b = self.__u, other.__u
        if not b:
            raise ZeroDivisionError('x % zero_polynomial')
        q, r = field2x_divmod(a, b)

##        us = _get__poly_utils__sympy()
##        a, b = map(us.uint2poly, [a,b])
##        c,d = divmod(a,b)
##        c,d = map(us.poly2uint, [c,d])
##        if not (c,d) == (q, r):
##            print((self.__u, other.__u), (c,d), (q, r))
##        #assert (c,d) == (q, r)
        return self.from_uint(q), self.from_uint(r)

    def __mod__(self, other):
        if not self.__known(other):
            return NotImplemented
        a, b = self.__u, other.__u
        if not b:
            raise ZeroDivisionError('x % zero_polynomial')
        r = field2x_mod(a, b)

##        us = _get__poly_utils__sympy()
##        a, b = map(us.uint2poly, [a,b])
##        c = a%b
##        c = us.poly2uint(c)
##        assert c == r
        return self.from_uint(r)

    def __mul__(self, other):
        if not self.__known(other):
            if isinstance(other, Integral):
                i = other
                prod = self.__u if i & 1 else 0
                self.from_uint(prod)

            return NotImplemented
        a, b = self.__u, other.__u
        prod = field2x_mul(a,b)

##        us = _get__poly_utils__sympy()
##        a, b = map(us.uint2poly, [a,b])
##        c = a*b
##        c = us.poly2uint(c)
##        assert c == prod
        return self.from_uint(prod)

del functools

##def _get__poly_utils__sympy():
##    from sand.big.CRC import _get__poly_utils__sympy
##    return _get__poly_utils__sympy()
##

#############################################################################
#############################################################################
################################# field[2,x] ################################
#############################################################################
#############################################################################

def field2x_mul(lhs, rhs):
    a = to_uint(lhs, 'lhs')
    b = to_uint(rhs, 'rhs')
    if a and b:
        sa = bin(a)
        sb = bin(b)
        a1s = sa.count('1')
        b1s = sb.count('1')

        if not a1s <= b1s:
            sa, sb = sb, sa
            a1s, b1s = b1s, a1s
            a, b = b, a
        assert a1s <= b1s

        old_i = 0
        pos = sa.index('1')
        prod = b
        while True:
            xpos = sa.find('1', pos+1)
            if xpos == -1:
                prod <<= (len(sa) - pos - 1)
                break
            prod <<= (xpos - pos)
            prod ^= b
            pos = xpos
    else:
        prod = 0
    return prod


def field2x_mod(dividend, divisor):
    '''uint as polynomial over field[2,x]

>>> field2x_mod(3, 5)
3
>>> field2x_mod(4, 5) # == 4^5
1
>>> field2x_mod(5, 5) # == 5^5
0
>>> field2x_mod(12, 5) # == 12^(5<<1)^5
3
>>> field2x_mod(4, 1) # == 4^(1<<2)
0
'''
##    assert dividend >= 0
##    assert divisor > 0

    dividend = to_uint(dividend, 'dividend')
    divisor = to_pint(divisor, 'divisor')

    D = divisor.bit_length()
    L = dividend.bit_length()
    if L <= D*1*8:
        return field2x_mod__plain(dividend, divisor)

    bs = dividend.to_bytes((L+8-1)//8, 'big')
    #assert int.from_bytes(bs, 'big') == dividend
    return _field2x_mod__bytes(bs, divisor)

def field2x_mod__bytes(dividend_in_bytes, divisor, byte_MSB_first):
    r'''bytes as uint; uint as polynomial over field[2,x]

>>> field2x_mod__bytes(b'\x03', 5, True)
3
>>> field2x_mod__bytes(b'\xc0', 5, False)
3
>>> field2x_mod__bytes(b'\x00\x03', 5, True)
3
'''
    divisor = to_pint(divisor, 'divisor')
    #assert divisor > 0
    byte_MSB_first = bool(byte_MSB_first)
    dividend_in_bytes = std_data_bitorder(dividend_in_bytes, byte_MSB_first)
    return _field2x_mod__bytes(dividend_in_bytes, divisor)




def _field2x_mod__bytes(dividend_in_bytes, divisor):
    r'''bytes as uint; uint as polynomial over field[2,x]
byte_MSB_first = True


>>> _field2x_mod__bytes(b'\x03', 5)
3
>>> _field2x_mod__bytes(b'\x00\x03', 5)
3
'''
    # byte_MSB_first = True
    assert divisor > 0
    global uint2bytes

    D = divisor.bit_length()
    L = D*1*8

    #divisor_size = (D+8-1)//8
    L_in_bytes = L//8
    prefix = 0
    for i in range(0, len(dividend_in_bytes), L_in_bytes):
        block = dividend_in_bytes[i:i+L_in_bytes] # postfix
        assert block # len(block) <= L_in_bytes
        bs = uint2bytes(prefix) + block
        u = int.from_bytes(bs, 'big')
        # u = prefix | postfix
        prefix = field2x_mod__plain(u, divisor)
    return prefix

    ###################### old version #####################
    for i in range(0, len(dividend_in_bytes), L_in_bytes):
        block = dividend_in_bytes[i:i+L_in_bytes]
        assert block
        L_in_bits = len(block)*8
        prefix <<= L_in_bits
        postfix = int.from_bytes(block, 'big')
        u = prefix | postfix
        assert u & ((1<<L_in_bits)-1) == postfix
        prefix = field2x_mod__plain(u, divisor)
    return prefix


def field2x_mod__plain(dividend, divisor):
    '''dividend, divisor ::= uint representing bits in big-endian
divide over Field[2, x]
'''
    assert dividend >= 0
    assert divisor > 0
##    dividend = to_uint(dividend, 'dividend')
##    divisor = to_pint(divisor, 'divisor')

    remainder = dividend
    org_L = L = remainder.bit_length() if remainder else 0
    assert bool(remainder) == bool(L)
    MSB = 1 << (L-1) if L else None

    D = divisor.bit_length()
    assert L >= 0
    assert D > 0
    shifted_divisor = divisor << (L-D) if L-D >= 0 else None


    for _ in range(L-D+1):
        assert L >= D
        # assert MSB & shifted_divisor
##        if MSB & remainder:
##            remainder ^= shifted_divisor
        try_div = remainder ^ shifted_divisor
        if try_div < remainder: # NOTE : NOT !! remainder >= shifted_divisor
            remainder = try_div
        else:
            assert remainder < shifted_divisor # MSB & remainder == 0
        MSB >>= 1
        L -= 1
        shifted_divisor >>= 1

    assert L < D
    if org_L >= D: # NOTE: NOT !! dividend >= divisor
        assert L == D-1
        assert divisor >> 1 == shifted_divisor
        if not MSB == (1 << (D-1))>>1:
            raise logic-error
    else:
        assert remainder == dividend

    assert 0 <= remainder < divisor
    return remainder

























def uint2bytes(u):
    if not u:
        return b''
    size = (u.bit_length()+7)//8
    bs = u.to_bytes(size, 'big')
    return bs









def field2x_divmod(dividend, divisor):
    '''uint as polynomial over field[2,x]

>>> field2x_divmod(3, 5)
(0, 3)
>>> field2x_divmod(4, 5) # == 4^5
(1, 1)
>>> field2x_divmod(5, 5) # == 5^5
(1, 0)
>>> field2x_divmod(12, 5) # == 12^(5<<1)^5
(3, 3)
>>> field2x_divmod(4, 1) # == 4^(1<<2)
(4, 0)
'''
##    assert dividend >= 0
##    assert divisor > 0

    dividend = to_uint(dividend, 'dividend')
    divisor = to_pint(divisor, 'divisor')

    D = divisor.bit_length()
    L = dividend.bit_length()
    if L <= D*1*8:
        return field2x_divmod__plain(dividend, divisor)

    bs = dividend.to_bytes((L+8-1)//8, 'big')
    return _field2x_divmod__bytes(bs, divisor)

def field2x_divmod__bytes(dividend_in_bytes, divisor, byte_MSB_first):
    r'''bytes as uint; uint as polynomial over field[2,x]

>>> field2x_divmod__bytes(b'\x03', 5, True)
(0, 3)
>>> field2x_divmod__bytes(b'\xc0', 5, False)
(0, 3)
>>> field2x_divmod__bytes(b'\x00\x03', 5, True)
(0, 3)
'''
    divisor = to_pint(divisor, 'divisor')
    #assert divisor > 0
    byte_MSB_first = bool(byte_MSB_first)
    dividend_in_bytes = std_data_bitorder(dividend_in_bytes, byte_MSB_first)
    return _field2x_divmod__bytes(dividend_in_bytes, divisor)



def _field2x_divmod__bytes(dividend_in_bytes, divisor):
    r'''bytes as uint; uint as polynomial over field[2,x]
byte_MSB_first = True


>>> _field2x_divmod__bytes(b'\x03', 5)
(0, 3)
>>> _field2x_divmod__bytes(b'\x00\x03', 5)
(0, 3)
'''
    # byte_MSB_first = True
    assert divisor > 0
    global uint2bytes

    D = divisor.bit_length()
    L = D*1*8

    #divisor_size = (D+8-1)//8
    L_in_bytes = L//8
    prefix = 0
    quotient = []
    for i in range(0, len(dividend_in_bytes), L_in_bytes):
        block = dividend_in_bytes[i:i+L_in_bytes] # postfix
        assert block # len(block) <= L_in_bytes
        bs = uint2bytes(prefix) + block
        u = int.from_bytes(bs, 'big')
        # u = prefix | postfix
        q, prefix = field2x_divmod__plain(u, divisor)
        q = q.to_bytes(len(block), 'big')
        quotient.append(q)
    quotient = b''.join(quotient)
    quotient = int.from_bytes(quotient, 'big')
    return quotient, prefix


def field2x_divmod__plain(dividend, divisor):
    '''dividend, divisor ::= uint representing bits in big-endian
divide over Field[2, x]
'''
    assert dividend >= 0
    assert divisor > 0

    remainder = dividend
    org_L = L = remainder.bit_length() if remainder else 0
    assert bool(remainder) == bool(L)
    MSB = 1 << (L-1) if L else None

    D = divisor.bit_length()
    assert L >= 0
    assert D > 0
    shifted_divisor = divisor << (L-D) if L-D >= 0 else None

    quotient = [] # big-endian bits
    for _ in range(L-D+1):
        assert L >= D
        # assert MSB & shifted_divisor
        try_div = remainder ^ shifted_divisor
        if try_div < remainder: # NOTE : NOT !! remainder >= shifted_divisor
            remainder = try_div
            quotient.append(True)
        else:
            assert remainder < shifted_divisor # MSB & remainder == 0
            quotient.append(False)
        MSB >>= 1
        L -= 1
        shifted_divisor >>= 1

    assert L < D
    if org_L >= D: # NOTE: NOT !! dividend >= divisor
        assert L == D-1
        assert divisor >> 1 == shifted_divisor
        if not MSB == (1 << (D-1))>>1:
            raise logic-error
    else:
        assert remainder == dividend

    quotient.reverse() # little-endian
    quotient = bitseqLE2uint(quotient)
    assert 0 <= remainder < divisor
    return quotient, remainder








if __name__ == "__main__":
    import doctest
    doctest.testmod()
