
r'''
Numerical_Recipes(3rd_2007).pdf
[page1168] 22.4 Cyclic Redundancy and Other Checksums
'''


__all__ = '''
    CRC_Info
    CRC32_generator__zlib
    CRC32_generator__Ethernet
    reverse_uint
    reverse_bitorder_per_byte
    uint2expsLE

    find_CRC_argss
    from_bytes2crc

    ogg_CRC32
    ogg_crc32
    zlib_CRC32
    zlib_crc32
    '''.split()

import functools
from itertools import islice, chain
from seed.helper.check_utils import to_uint, to_pint
from seed.int_tools.uint_bits_utils import\
    (memoryview_B1D
    ,uint2expsLE
    ,uint2bitsLE
    ,uint2bitsBE
    ,bitsBE2uint
    ,uint8s2bitsBE
    ,uint8s2bitsLE
    ,reverse_uint
    ,reverse_uint8
    ,reverse_uint32
    ,uint8_to_bitsBE
    ,uint8_to_bitsLE
    ,byte_MSB_first_to_uint8XE2uint8BE
    ,uint8_to_reversed_byte
    ,uint8_to_reversed_uint8
    ,reverse_bitorder_per_byte
    ,std_data_bitorder
    )
from seed.int_tools.uint_bits_utils import \
    (byte_MSB_first_to_uint8XE2uint8BE
        as global_byte_MSB_first_to_uint8XE2uint8BE
    ,std_data_bitorder as std_data
    )


from seed.math.Field2xPolynomial import\
    (field2x_mod
    ,field2x_mod__bytes
    ,Field2xPolynomial
    )

'''
from sand.small.uint_bits_utils
    memoryview_B1D

    uint2expsLE
    uint2bitsLE
    uint2bitsBE
    bitsBE2uint
    uint8s2bitsBE
    uint8s2bitsLE


    reverse_uint
    reverse_uint8
    reverse_uint32
    uint8_to_bitsBE
    uint8_to_bitsLE
    byte_MSB_first_to_uint8XE2uint8BE

    uint8_to_reversed_byte
    uint8_to_reversed_uint8
    reverse_bitorder_per_byte
    std_data_bitorder

    field2x_mod
    field2x_mod__bytes
'''

#memoryview = memoryview_B1D

def CRC_generator2exps(generator):
    'generator is uint > 0; frame_length = generator.bit_length()-1'
    generator = to_pint(generator, 'generator')
    #frame_length = generator.bit_length()-1
    return uint2expsLE(generator)







#assert 0x04c11db7 .bit_length() == 32
assert 0x04c11db7 < 1<<32
CRC32_generator__Ethernet = CRC32_generator__IEEE_802_3 = 0x04c11db7 | (1<<32)
assert CRC_generator2exps(CRC32_generator__Ethernet) == \
       [0, 1, 2, 4, 5, 7, 8, 10, 11, 12, 16, 22, 23, 26, 32]

CRC32_generator__zlib = CRC32_generator__Ethernet

r'''
CRC32_generator__zip = 0xdebb20e3 | (1<<32)
crc_init = 0xffffffff
'''






def field2x_invmod(x, M):
    x = to_uint(x, 'x')
    M = to_pint(M, 'M')
##    assert x >= 0
##    assert M > 0
    x = field2x_mod(x, M)
    return field2x_invmod__plain(x, M)
def field2x_invmod__bytes(x_in_bytes, M, byte_MSB_first):
    M = to_pint(M, 'M')
    #assert M > 0
    x = field2x_mod__bytes(x_in_bytes, M, byte_MSB_first)
    return field2x_invmod__plain(x, M)

def _get__poly_utils__sympy(x=[]): # old version
    if not x:
        import sympy
        #from sympy import sympify
    ##    sympy.polys.polytools.invert(f, g, *gens, **args)
    ##    Invert f modulo g when possible.
        # modulus=2
        from sympy.abc import z
        class PolyUtils:
            @staticmethod
            def uint2poly(u):
                assert u >= 0
                exps = uint2expsLE(u)
                p = sum((z**e for e in exps), sympy.sympify(0))
                return sympy.poly(p, z, modulus=2)
            @staticmethod
            def poly2uint(poly):
                exps2coeff = poly.as_dict()
                u = 0
                for [exp], coeff in exps2coeff.items():
                    assert coeff == 1
                    u |= 1 << exp
                return u
            @staticmethod
            def invert(f, MOD):
                return sympy.invert(f, MOD)
            @staticmethod
            def gcd(f, g):
                return sympy.gcd(f, g)
        x.append(PolyUtils)
    poly_utils, = x
    return poly_utils

def _get__poly_utils__Field2xPolynomial(x=[]): # new version
    if not x:
        class PolyUtils:
            @staticmethod
            def uint2poly(u):
                assert u >= 0
                return Field2xPolynomial(u)
            @staticmethod
            def poly2uint(poly):
                return poly.as_uint()
            @staticmethod
            def invert(f, MOD):
                return f.invmod(MOD)
            @staticmethod
            def gcd(f, g):
                return f.gcd(g)
        x.append(PolyUtils)
    poly_utils, = x
    return poly_utils

_get__poly_utils = _get__poly_utils__Field2xPolynomial # __sympy or __Field2xPolynomial

def field2x_invmod__plain(x, M):
    assert 0 <= x < M
    assert M > 0
    #plain no: x = field2x_mod(x, M)

    poly_utils = _get__poly_utils()
    fx, fM = map(poly_utils.uint2poly, [x, M])
    finv = poly_utils.invert(fx, fM)
    assert (finv * fx) % fM == poly_utils.poly2uint(1)
    inv = poly_utils.poly2uint(finv)

    assert 0 <= inv < M
    return inv


def find_CRC_argss(
    generater, byte_MSB_first, data_crc_pairs, verify=False):
    r'''return [args...] or None
-> [(generater, frame_length,
     initial, xor_filter,
     byte_MSB_first, crc_MSB_first)]
   or None
see also CRC_Info.from_bytes2crc


CRC_Info.from_bytes2crc : given function, calc args
find_CRC_argss : given generater and examples, calc args
example:
    >>> import zlib
    >>> datas = [b'', b'q353', b'3234', b'34']
    >>> data_crc_pairs = [(data, zlib.crc32(data)&((1<<32)-1)) for data in datas]
    >>> generater, byte_MSB_first = 0x04c11db7 | (1<<32), False
    >>> argss = find_CRC_argss(
    ...    generater, byte_MSB_first, data_crc_pairs, verify=True)
    >>> list(CRC_Info(*args) for args in argss)
    [CRC_Info(0x104c11db7, 32, 0x0, 0xffffffff, False, False)]
'''
    verify = bool(verify)
    if verify:
        data_crc_pairs = list(data_crc_pairs)
    it = iter(data_crc_pairs)
    try:
        data_crc_pair1 = next(it)
    except StopIteration:
        raise ValueError('too few data_crc_pairs : at least 2')

    data_crc_pair2 = None
    for data_crc_pair2 in it:
        argss = _find_CRC_argss_2pairs(generater, byte_MSB_first,
              data_crc_pair1, data_crc_pair2)
        if argss is not None:
            break
    else:
        if data_crc_pair2 is None:
            raise ValueError('too few data_crc_pairs : at least 2')
        return None

    assert len(argss) == 2
    if verify:
        ls = []
        for args in argss:
            info = CRC_Info(*args)
            for data, crc in data_crc_pairs:
                if info.bytes2crc(data) != crc:
                    break
            else:
                ls.append(args)
        argss = ls

    assert 0 <= len(argss) <= 2
    return argss # of len 0~2

def _find_CRC_argss_2pairs(generater, byte_MSB_first,
                   data_crc_pair1, data_crc_pair2):
    '''return [args...] or None
-> [(generater, frame_length,
     initial, xor_filter,
     byte_MSB_first, crc_MSB_first)]
   or None
'''
    generater = int(generater)
    assert generater > 0
    assert generater & 1
    frame_length = generater.bit_length() - 1
    MSB = 1 << frame_length
    org_byte_MSB_first = byte_MSB_first = bool(byte_MSB_first)

    def std_pair(data_crc_pair):
        data, crc = data_crc_pair
        data, crc = std_data(data, byte_MSB_first), int(crc)
        assert crc >= 0
        assert crc < MSB
        return data, crc
    data1, _crc1 = std_pair(data_crc_pair1)
    data2, _crc2 = std_pair(data_crc_pair2)
    # now byte_MSB_first == True
    byte_MSB_first = True

    datas = [data1, data2]
    def std_crc(crc):
        if not crc_MSB_first:
            crc = reverse_uint(frame_length, crc)
        return crc

    poly_utils = _get__poly_utils()
    def poly2uint_mod(poly):
        u = poly_utils.poly2uint(poly)
        return field2x_mod(u, divisor)

    divisor = generater
    data2DL = lambda data: len(data)*8
    data2x_pow_DL_bytes = lambda data: b'\x01' + b'\x00'*len(data)
    data2x_pow_DL = lambda data: \
                    field2x_mod__bytes(data2x_pow_DL_bytes(data), divisor, True)
    DL1, DL2 = map(data2DL, datas)
    # x_pow_DL1 = 1 << DL1 mod divisor
    x_pow_DL1, x_pow_DL2 = map(data2x_pow_DL, datas)
    x_pow_DL_poly1 = poly_utils.uint2poly(x_pow_DL1)
    # x_pow_DL1_sub_x_pow_DL2
    diff_x_pow_DL = x_pow_DL1 ^ x_pow_DL2


    divisor_poly = poly_utils.uint2poly(divisor)
    diff_x_pow_DL_poly = poly_utils.uint2poly(diff_x_pow_DL)
    poly_one = poly_utils.uint2poly(1)
    poly_zero = poly_utils.uint2poly(0)
    if poly_one != poly_utils.gcd(diff_x_pow_DL_poly, divisor_poly):
        return None


    inv_diff_x_pow_DL_poly = poly_utils.invert(
        diff_x_pow_DL_poly, divisor_poly)

    if 1 or shifted_diff_data_int:
        def calc_shifted_data_int(data):
            i = field2x_mod__bytes(data, divisor, byte_MSB_first)
            i <<= frame_length
            return field2x_mod(i, divisor)
        shifted_data_int1, shifted_data_int2 = map(calc_shifted_data_int, datas)
        shifted_diff_data_int = shifted_data_int1 ^ shifted_data_int2


    ls = []
    for crc_MSB_first in [False, True]:
        crc1, crc2 = map(std_crc, [_crc1, _crc2])
        remainder1, remainder2 = crcs = crc1, crc2

        diff_remainder = remainder1 ^ remainder2
        diff_Adiff_DL_int = diff_remainder ^ shifted_diff_data_int
        diff_Adiff_DL_poly = poly_utils.uint2poly(diff_Adiff_DL_int)

        A_poly = inv_diff_x_pow_DL_poly * diff_Adiff_DL_poly
        A = poly2uint_mod(A_poly)

        # B == remainder_poly1 - A * x**DL1 + data_poly1 * x**frame_length
        # B == remainder_poly1 - A * x**DL1 + shifted_data_poly1
        B = remainder1 ^ poly2uint_mod(A_poly * x_pow_DL_poly1) ^ shifted_data_int1


        xor_filter = B
        initial = A ^ xor_filter
        args =  (generater, frame_length,
                 initial, xor_filter,
                 org_byte_MSB_first, crc_MSB_first)
        ls.append(args)


    return ls


    r'''
    shifted_diff_data_poly = (data_poly1-data_poly2) * x**frame_length mod divisor_poly
    diff_Adiff_DL_poly = remainder_poly1 - remainder_poly2 + shifted_diff_data_poly
    if gcd((x**DL1 - x**DL2), divisor_poly) == 1:
        A mod divisor_poly == diff_Adiff_DL_poly * (x**DL1 - x**DL2)**-1 mod divisor_poly
            == FA(1, 2)
        [mod divisor_poly]:
            A * x**DL1 == remainder_poly1 - B + data_poly1 * x**frame_length
            B == remainder_poly1 - A * x**DL1 + data_poly1 * x**frame_length
        B mod divisor_poly == remainder_poly1 - (A mod divisor_poly) * x**DL1 + data_poly1 * x**frame_length
            == remainder_poly1 - FA(1, 2) * x**DL1 + data_poly1 * x**frame_length
            == FB(1,2)
        since frame_length < len(crc_bits):
            A = (A mod divisor_poly) == FA(1, 2)
            B = (B mod divisor_poly) == FB(1, 2)
    '''


@functools.total_ordering
class CRC_Info:
    r'''base class for CRC calc


algorithm:
    input: data_bits, generater, initial_bits, xor_filter_bits
    output: crc_bits
    # int value of initial_bits/xor_filter_bits/crc_bits depends on crc_MSB_first
    # how to convert data_bytes to data_bits depends on byte_MSB_first

    divisor_bits = uint2bitsBE(generater)
    divisor_poly = bits2polynomialBE(divisor_bits)
    frame_length = len(divisor_bits) - 1
    assert len(xor_filter_bits) == frame_length # default: [0]*frame_length
    assert len(initial_bits) == frame_length # default: [0]*frame_length

    dividend_bits = data_bits + xor_filter_bits
    dividend_bits[:frame_length] ^= initial_bits ^ xor_filter_bits
    dividend_poly = bits2polynomialBE(dividend_bits)
    remainder_poly = dividend_poly % divisor_poly # over field F2[x]
    crc_bits = polynomial2bitsBE(remainder_poly, frame_length)
    assert len(crc_bits) == frame_length
    return crc_bits

    ######################## inv ########################
    # dividend_poly == (initial_poly+xor_filter_poly) * x**len(data_bits)
    #                + data_poly * x**frame_length
    #                + xor_filter_poly
    if given generater and [(data_bits, crc_bits), ...]
        that is known divisor_poly and [(data_poly, remainder_poly), ...]
    can we find out initial_bits/xor_filter_bits??
    let A = (initial_poly+xor_filter_poly), B = xor_filter_poly
    dividend_poly = A * x**len(data_bits) + B + data_poly * x**frame_length
    remainder_poly = dividend_poly % divisor_poly
    let DL = len(data_bits) # known
    A * x**DL = dividend_poly - B + data_poly * x**frame_length
    A * (x**DL1 - x**DL2) = dividend_poly1 - dividend_poly2 + (data_poly1-data_poly2) * x**frame_length
    (A * (x**DL1 - x**DL2)) % divisor_poly == remainder_poly1 - remainder_poly2 + (data_poly1-data_poly2) * x**frame_length mod divisor_poly
        == diff_Adiff_DL_poly
    if gcd((x**DL1 - x**DL2), divisor_poly) == 1:
        A mod divisor_poly == diff_Adiff_DL_poly * (x**DL1 - x**DL2)**-1 mod divisor_poly
            == FA(1, 2)
        [mod divisor_poly]:
            A * x**DL1 == remainder_poly1 - B + data_poly1 * x**frame_length
            B == remainder_poly1 - A * x**DL1 + data_poly1 * x**frame_length
        B mod divisor_poly == remainder_poly1 - (A mod divisor_poly) * x**DL1 + data_poly1 * x**frame_length
            == remainder_poly1 - FA(1, 2) * x**DL1 + data_poly1 * x**frame_length
            == FB(1,2)
        since frame_length < len(crc_bits):
            A = (A mod divisor_poly) == FA(1, 2)
            B = (B mod divisor_poly) == FB(1, 2)




terms:
    BE, LE, XE - big-endian, little-endian, runtime-determined-endian(BE/LE)
    MSB, LSB - most/least-significant-bit
    MSBYTE, LSBYTE - most/least-significant-byte
    CRC - cyclic redundancy check

create:
    CRC_Info(0x04c11db7 | (1<<32))
    CRC_Info(0x04c11db7 | (1<<32), 32)
    CRC_Info(0x04c11db7, 32, fixed_MSB=True)

initial:
    def calc_crc(data, crc=initial):...

byte_MSB_first:
    if LSB first per byte:
        '\x80' ==>> 0000 0001
        '\x01' ==>> 1000 0000
        '\x01\xF0' ==>> 1000 0000 1000 1111

crc_MSB_first:
    if not crc_MSB_first:
        crc16 == 0x0f ==>> bits of crc16 == 1111 0000 0000 0000

xor_filter:
    def crc_plain(data, crc):...
    def crc_with_xor_filter(data, crc):
        crc ^= xor_filter
        crc = crc_plain(data, crc)
        crc ^= xor_filter
        return crc

useful methods:
    from_bytes2crc
    bytes2crc
    bits2crc
    __repr__
example:
    >>> info = CRC_Info(0x04c11db7 | (1<<32))
    >>> info == CRC_Info(0x04c11db7 | (1<<32), 32)
    True
    >>> info == CRC_Info(0x04c11db7, 32, fixed_MSB=True)
    True
    >>> info == eval(repr(info))
    True
    >>> import zlib
    >>> calculator = zlib.crc32
    >>> info = CRC_Info.from_bytes2crc(32, calculator)
    >>> info
    CRC_Info(0x104c11db7, 32, 0x0, 0xffffffff, False, False)
'''
    # XE is BE if byte_MSB_first else LE
    byte_MSB_first_to_generator_to_uint8XE2crcBE = ({}, {})
    byte_MSB_first_to_uint8XE2uint8BE = \
        global_byte_MSB_first_to_uint8XE2uint8BE


    @property
    def uint8XE2uint8BE(self):
        return self.byte_MSB_first_to_uint8XE2uint8BE[self.byte_MSB_first]
    @property
    def uint8XE2bits(self):
        return uint8_to_bitsBE if self.byte_MSB_first else uint8_to_bitsLE
    @property
    def uint8XEs2iter_bits(self):
        return uint8s2bitsBE if self.byte_MSB_first else uint8s2bitsLE
    @property
    def CRC_generator_to_uint8XE2crcBE(self):
        return type(self).byte_MSB_first_to_generator_to_uint8XE2crcBE\
               [self.byte_MSB_first]


    def build_uint8XE2crcBE(self):
        it = (self.bits2crcBE(bits, crcBE=0)
              for bits in self.uint8XE2bits)
        return tuple(it)

    def get_uint8XE2crcBE(self):
        g = self.CRC_generator
        d = self.CRC_generator_to_uint8XE2crcBE
        if g not in d:
            d[g] = self.build_uint8XE2crcBE()
        return d[g]

    def __to_default_crc(self, crc, MSB, default, name):

        if crc is None:
            crc = default
        crc = int(crc)
        if not 0 <= crc < MSB:
            raise ValueError('not 0 <= {} < MSB'.format(name))
        return crc

    def __init__(self,
                 generator,            # uint<frame_length+1>BE
                 frame_length=None,    # MSB = 1 << frame_length
                 initial=None,         # init_crcXE
                 xor_filter=None,      # crcXE
                 byte_MSB_first=False, # uint8LE or uint8BE
                 crc_MSB_first=False,  # crcLE or crcBE
                 *, fixed_MSB=False):
        generator = int(generator) # in MSB_first order; not care crc_MSB_first
        byte_MSB_first = bool(byte_MSB_first) # so, None -> False
        crc_MSB_first = bool(crc_MSB_first)

        if fixed_MSB:
            if frame_length is None:
                raise ValueError('fixed_MSB and frame_length is None')

            frame_length = int(frame_length)
            if not frame_length > 0:
                raise ValueError('fixed_MSB and not frame_length > 0')
            MSB = 1 << frame_length
            if not 0 <= generator < MSB:
                raise ValueError('fixed_MSB and not 0 <= input_generator < MSB')
            generator |= MSB

        if not generator > 0:
            raise ValueError('not CRC_generator > 0')
        if not generator & 1:
            raise ValueError('not CRC_generator & 1')
        M = generator.bit_length() - 1
        if frame_length is not None:
            if M != frame_length:
                raise ValueError('frame_length != CRC_generator.bit_length() - 1')

        frame_length = M
        MSB = 1 << frame_length

        initial = self.__to_default_crc(initial, MSB, 0, 'initial')
        xor_filter = self.__to_default_crc(xor_filter, MSB, 0, 'xor_filter')
        self.__args = (generator, frame_length, initial, xor_filter,
                       byte_MSB_first, crc_MSB_first)
        self.__exps = None

    def __repr__(self):
        G, L, I, X, bMf, cMf = self.__args
        return '{}({}, {}, {}, {}, {}, {})'.format(
            type(self).__name__, hex(G), L, hex(I), hex(X), bMf, cMf)
    def __hash__(self):
        return hash(self.__args)
    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.__args == other.__args

    def __lt__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.__args < other.__args

    @property
    def CRC_generator(self):
        return self.__args[0]
    @property
    def CRC_frame_length(self):
        return self.__args[1]
    @property
    def CRC_MSB(self):
        return 1 << self.CRC_frame_length
    @property
    def CRC_initial(self):
        return self.__args[2]
    @property
    def CRC_xor_filter(self):
        return self.__args[3]
    @property
    def byte_MSB_first(self):
        'MSB_first_per_byte'
        return self.__args[4]
    @property
    def crc_MSB_first(self):
        'MSB_first_per_byte'
        return self.__args[5]

    @property
    def CRC_exps(self):
        if self.__exps is None:
            self.__exps = tuple(CRC_generator2exps(self.CRC_generator))
        return self.__exps

    def __reverse_crc_if_required(self, crc):
        'XE2BE or BE2XE'
        if not self.crc_MSB_first:
            crc = self.__reverse_crc(crc)
        return crc
    def __reverse_crc(self, crc):
        return reverse_uint(self.CRC_frame_length, crc)
    def __std_crc(self, crcXE):
        'may reverse crc -> result crc in MSB first bit order'
        crcXE = self.__to_default_crc(crcXE, self.CRC_MSB, self.CRC_initial, 'crc')
        crcXE ^= self.CRC_xor_filter
        crcBE = self.__reverse_crc_if_required(crcXE)
        return crcBE

    def __output_crc(self, crcBE):
        crcXE = self.__reverse_crc_if_required(crcBE)
        crcXE ^= self.CRC_xor_filter
        return crcXE
    def calc_crc_from_bits(self, bits, crc=None):
        crcXE = crc
        crcBE = self.__std_crc(crcXE)
        del crc
        crcBE = self.bits2crcBE(bits, crcBE)
        return self.__output_crc(crcBE) # reverse crc if needed
    bits2crc = calc_crc_from_bits

    def bits2crcBE(self, bits, crcBE=None):
        'crcBE not xor the xor_filter'
        if crcBE is None:
            crcBE = self.__std_crc(None)

        frame_length = self.CRC_frame_length
        bits = chain(bits, [False]*frame_length)
        prev_tail_bits = islice(bits, frame_length)
        prev_tail = bitsBE2uint(prev_tail_bits) # previous calc set this value as 0
        crcBE ^= prev_tail

        MSB = self.CRC_MSB
        MASK = MSB - 1
        G = self.CRC_generator
        assert 0 <= crcBE < MSB

        for bit in bits:
            crcBE <<= 1
            if bit:
                crcBE |= 1
            if crcBE & MSB:
                crcBE ^= G # NOTE: THIS CLEAR MSB OF CRC

        assert 0 <= crcBE < MSB
        return crcBE


    def __calc_crc_from_bytes(self, data, crc=None):
        bits = self.uint8XEs2iter_bits(memoryview_B1D(data))
        return self.calc_crc_from_bits(bits, crc)
    def calc_crc_from_bytes(self, data, crc=None):
        window_size, remainder = divmod(self.CRC_frame_length, 8)

        if remainder != 0: # i.e. CRC12
            return self.__calc_crc_from_bytes(data, crc)
        del remainder

        I = crcXE = crc
        crcBE = self.__std_crc(crcXE) # to MSB_first bit order
        del crc, crcXE
        data = memoryview_B1D(data)

        uint8XEs = chain(data, [0]*window_size)

        # previous calc set prev_tail as 0
        # prev_tail_bytes = bytes(islice(uint8s, window_size))
        # bug: prev_tail = int.from_bytes(prev_tail_bytes, 'big')
        prev_tail_bits = self.uint8XEs2iter_bits(islice(uint8XEs, window_size))
        prev_tail = bitsBE2uint(prev_tail_bits)
        crcBE ^= prev_tail

        MSB = self.CRC_MSB
        MASK = MSB - 1
        assert 0 <= crcBE < MSB
        L = self.CRC_frame_length - 8


        uint8XE2crcBE = self.get_uint8XE2crcBE()
        uint8BE2uint8XE = uint8XE2uint8BE = self.uint8XE2uint8BE
        # instead of MSB
        #_2_uint8XEs = islice(data, window_size, None)
        #_1_uint8BEs = crcBE.to_bytes(window_size, 'big')[:len(data)]
        #_1_uint8XEs = (uint8BE2uint8XE[u] for u in _1_uint8BEs) # reverse back
        # bug: MSBYTE_XEs = chain(_1_uint8XEs, _2_uint8XEs)
        #   _2_uint8XEs is not MSBYTE !!!!!!!!
        new_LSBYTE_XEs = uint8XEs
        for new_LSBYTE_XE in new_LSBYTE_XEs:
            new_LSBYTE_BE = uint8XE2uint8BE[new_LSBYTE_XE]
            MSBYTE_BE = crcBE >> L
            MSBYTE_XE = uint8BE2uint8XE[MSBYTE_BE]

            crcBE <<= 8
            crcBE &= MASK
            crcBE |= new_LSBYTE_BE
            crcBE ^= uint8XE2crcBE[MSBYTE_XE]
        #assert not list(new_LSBYTE_XEs)

        crcXE = self.__output_crc(crcBE) # reverse or not
        #assert crcXE == self.__calc_crc_from_bytes(data, I) ######## del me
        return crcXE
    bytes2crc = calc_crc_from_bytes


    @classmethod
    def from_bits2crc(cls, frame_length, bits2crc, byte_MSB_first=False):
        byte_MSB_first = bool(byte_MSB_first)
        uint8XEs2iter_bits = (uint8s2bitsBE if byte_MSB_first else uint8s2bitsLE)
        def bytes2crc(data, crc):
            data = memoryview_B1D(data)
            bits = uint8XEs2iter_bits(data)
            return bits2crc(bits, crc)
        return cls.from_bytes2crc(frame_length, bytes2crc)

        # byte_MSB_first = ??
        # crc_MSB_first = ??
        # xor_filter = ??
        crc1 = bits2crc([True], 0)
        crc0 = bits2crc([False], 0)
        dgenerator = crc1 ^ crc0
        initial = bits2crc([])
        return cls(dgenerator, frame_length, initial, fixed_MSB=True)

    @classmethod
    def from_bytes2crc(cls, frame_length, bytes2crc):
        '''given frame_length and crc calculator, find out CRC generator

calculator(data::bytes[, crc::int])->crc::int

example:
    >>> import zlib
    >>> calculator = zlib.crc32
    >>> info = CRC_Info.from_bytes2crc(32, calculator)
    >>> info.CRC_generator == 0x04c11db7 | (1<<32)
    True
    >>> data = b'adfasfdddg4446'
    >>> info.calc_crc_from_bytes(data) == calculator(data)
    True
    >>> calculator = info.calc_crc_from_bytes
    >>> frame_length = info.CRC_frame_length
    >>> info2 = CRC_Info.from_bytes2crc(frame_length, calculator)
    >>> info2 == info
    True

    >>> G = 0x333 | (1<<32)
    >>> info3 = CRC_Info(G, 32, 0x444)
    >>> calculator = info3.calc_crc_from_bytes
    >>> frame_length = info3.CRC_frame_length
    >>> info4 = CRC_Info.from_bytes2crc(frame_length, calculator)
    >>> info4 == info3
    True
'''
        initial = bytes2crc(b'')

        byte00 = b'\x00'
        crc00 = bytes2crc(byte00, 0)

        def calc_info(xor_filter, crc_MSB_first, byte_MSB_first, byte01):
            crc01 = bytes2crc(byte01, 0)
            generator = crc00 ^ crc01
            if not crc_MSB_first:
                generator = reverse_uint(frame_length, generator)
            if not generator & 1:
                return None

            info = cls(generator, frame_length, initial, xor_filter,
                       byte_MSB_first, crc_MSB_first, fixed_MSB=True)
            this_bytes2crc = info.calc_crc_from_bytes
            _crc01 = this_bytes2crc(byte01, 0)

            if _crc01 == crc01:
                if all(this_bytes2crc(bs) == bytes2crc(bs)
                       for bs in [b'\x00', b'\x01', b'\x80']):
                    return info

            return None

        # the bits are : 0000 0001
        # try      # LSB first
        # then try # MSB first
        MSB = 1<<frame_length
        ALL_1s = MSB-1
        for xor_filter in [0, ALL_1s]:
            for crc_MSB_first in [False, True]:
                for byte_MSB_first, byte01 in [(False, b'\x80'), (True, b'\x01')]:
                    info = calc_info(xor_filter, crc_MSB_first, byte_MSB_first, byte01)
                    if info is not None:
                        return info
        raise logic-error-NO


    @classmethod
    def find_CRC_argss(cls, generater, byte_MSB_first, data_crc_pairs, verify=False):
        return find_CRC_argss(generater, byte_MSB_first, data_crc_pairs, verify=verify)


from_bytes2crc = CRC_Info.from_bytes2crc





import zlib
zlib_CRC32 = CRC_Info(0x04c11db7 | (1 << 32), 32, xor_filter=0xffffffff)
ogg_CRC32 = CRC_Info(0x04c11db7 | (1 << 32), 32, byte_MSB_first=True, crc_MSB_first=True)

def zlib_crc32(data, crc=None):
    if crc is None:
        crc = 0
    return zlib.crc32(data, crc) & 0xffffffff

def ogg_crc32(data, crc=None):
    if crc is None:
        crc = 0

    ALL_1s = 0xffffffff
    data = reverse_bitorder_per_byte(data)
    crc = (zlib.crc32(data, crc^ALL_1s) & ALL_1s) ^ ALL_1s
    crc = reverse_uint(32, crc)
    return crc

assert zlib_CRC32 == CRC_Info.from_bytes2crc(32, zlib_crc32)
assert ogg_CRC32 == CRC_Info.from_bytes2crc(32, ogg_crc32)


#############################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()



def t():
    ZCRC = zlib_CRC32
    #print(ZCRC)
    bss = [b'ab', b'afdsafdssdf', b'\x80', b'\x40', b'\x01', b'\x02', b'\xff', ]
    for bs in bss:
        r = zlib.crc32(bs)
        #print(bs, r)
        r2 = ZCRC.calc_crc_from_bytes(bs)
        assert r == r2



    assert all(zlib.crc32(bs) == ZCRC.calc_crc_from_bytes(bs)
               for i in range(0x100) for bs in [bytes([i])])

t()














