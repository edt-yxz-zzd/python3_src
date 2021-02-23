
r'''
see:
    seed.iters.find
        #search subseq
        #using failure_func
    nn_ns.bin.stream_search
        #search subseq
        #using polynomial hash
    seed.seq_tools.seq_index_if
        #search value
        #using predicator
#'''

__all__ = '''
    iter_search_all
    search_all

    Finder
    Hasher
    hash_str
    hash_str_plus
    '''.split()

from collections import deque
from nn_ns.math_nn.prime2 import mod_pow

r'''
wiki/Multiplicative_group_of_integers_modulo_n#Powers_of_2

k > 2, n = 2^k, U(Z/nZ) is not cyclic
U(Z/nZ) = Gen(2^(k-1)-1 mod n) * Gen(3 mod n) ~=~ Cyclic(2) * Cyclic(2^(k-2))
the powers of 3 are a subgroup of order 2^(k − 2)

U(Z/p^kZ) ~=~
    p = 2, k = 1: Cyclic(1)
    p = 2, k > 1: Cyclic(2) * Cyclic(2^(k-2))
    p is odd prime: Cyclic((p-1)*p^(k-1))

=================================================
n > 1, k > 0, p is an odd prime,
U(Z/nZ) is cyclic iff n = 2, 4, p^k, 2*p^k

=================================================
n = product(p[i]^k[i] for i in N)
Z/nZ ~=~ product Z/p[i]^k[i]Z
U(Z/nZ) ~=~ product U(Z/p[i]^k[i]Z)
NOTE: |U(Z/p^kZ)| = p^(k-1)*(p-1),
    1. if p is odd, then 2|(p-1)
    2. if there is another odd prime q, then I2*I2 ~=~ a subgroup of U(Z/p^kZ)*U(Z/q^tZ)
    3. if p = 2, and k > 1, then 2|2^(k-1)*(2-1), n = 2^k*q^t has not primitive root
    4. if p = 2, and k > 2, then Z/2^kZ is not cyclic
    => U(Z/nZ) is cyclic iff n = 2, 4, p^k, 2*p^k

=================================================
phi(n) = Euler_totient_function(n) = order(U(Z/nZ))
lambda(n) = Carmichael_function(n)
    = min [i for i in [1..n] if unique[a^i mod n for a in U(n)] == [1]]
    where U(n) = [u for u in [1..n] if gcd(u, n) == 1]
U(Z/nZ) is cyclic iff phi(n) = lambda(n)
The single generator in the cyclic case is called a primitive root modulo n.

=================================================
Finding primitive roots
1. n = 2 or 4, g = 3
2. n = p
    primitive_root(p) = min [g for g in [1..p-1]
        if 1 not in [g^((p-1)/q) mod p for q in factors(p-1)]]
3. n = p^k
    primitive_root(p^k)
        | g^(p-1) mod p^2 == 1 = g + p
        | otherwise            = g
        where g = primitive_root(p)
4. n = 2*p^k
    primitive_root(2*p^k)
        | g mod 2 == 0 = g + p^k
        | otherwise    = g
        where g = primitive_root(p^k)


#'''

hash_bit_num = 32
hash_modulo_n = 2**hash_bit_num
hash_base = 3
hash_order= 2**(hash_bit_num - 2)


def search_all(key, fname):
    with open(fname, 'rb') as fin:
        locations = iter_search_all(key, fin)
    return locations


def iter_search_all(key, file_obj):
    finder = Finder(key)
    while True:
        location = finder.search_next(file_obj)
        if location < 0:
            break
        yield location


class Finder:
    def __init__(self, key):
        self.key = key
        length = len(self.key)
        self.key_deque = deque(key, length)
        self.key_hash = Hasher(key).get_hash()

    def search_next(self, file_obj):
        f = file_obj
        length = len(self.key)
        data = f.read(length)
        if not (len(data) == length):
            return -1
        elif data == self.key:
            return f.tell() - length

        block = deque(data, length)
        data_hasher = Hasher(data)
        while True:
            byte = f.read(1)
            if len(byte) != 1:
                break
            old_ibyte = block.popleft()
            new_ibyte = byte[0]
            block.append(new_ibyte)
            data_hash = data_hasher.fifo_hash(old_ibyte, new_ibyte)
            if data_hash == self.key_hash:
                if block == self.key_deque:
                    return f.tell() - length

        return -1


class Hasher:
    def __init__(self, data, modulo_n = hash_modulo_n, base = hash_base, order = hash_order):
        self.modulo_n = modulo_n
        self.base = base
        self.order = order
        self.length = len(data)
        (h, p) = hash_str(data, modulo_n, base, order)
        self.hash = h
        self.patch = p

    def fifo_hash(self, old_ibyte, new_ibyte):
        self.hash = hash_str_plus(self.hash, old_ibyte, new_ibyte
                                  ,self.modulo_n, self.base, self.patch)
        return self.hash

    def get_hash(self):
        return self.hash



def hash_str(data, modulo_n, base, order):
    assert(type(data[0]) == int) # data is of type bytes or bytearray, but not str

    # data[0]*base**(length-1+d) +..+ data[-1]*base**(0+d) mod n
    # base**(length+d) = 1 mod n
    # length+d = 0 mod order
    length = len(data)
    # The modulo operator always yields a result
    # with the same sign as its second operand (or zero);
    # the absolute value of the result is strictly
    # smaller than the absolute value of the second operand.
    d = (-length) % order
    patch = mod_pow(base, d, modulo_n)
    h = 0
    for ibyte in data:
        # a = ord(c)
        h *= base
        h += ibyte
        h %= modulo_n

    h = (h * patch) % modulo_n
    return (h, patch)


def hash_str_plus(data_hash, old_ibyte, new_ibyte, modulo_n, base, patch):
    assert(type(old_ibyte) == int)
    assert(type(new_ibyte) == int)
    h = data_hash * base + (new_ibyte) * patch - (old_ibyte)
    h %= modulo_n
    return h


def test_finder():
    import io
    f = io.BytesIO(b'33af33')
    key = b'33'
    r = [*iter_search_all(key, f)]
    assert r == [0, 4]


test_finder()
