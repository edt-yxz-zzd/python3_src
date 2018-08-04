
r'''
BBF uint encoding
    B  :  BITS_BITSS_BYTES_CASE #bits_layers_and_bytes_layer
    B0 :  BITS0_BITSS_BYTES_CASE #0bits_layers_and_bytes_layer
    F  :  FIXED_LENGTH




dynamic length encoding of uint
functions:
    1) encode uint to file
    2) decode from file without knowing the length of encoded bytes
requires:
    0) should be efficient; unit 'byte'
        a) space efficiency
            bits'1{uint}0{8-uint%8}':
                O(uint) is not allowed
            hex or base64+space:
                efficiency ~= 4/8 or 6/8
                not efficient enough
            bytes'[\x80-\xff]*[\x00-\x7f]':
                efficiency = 7/8
                not efficient enough for large uint
        a') space efficiency - support unicode
            i) use one byte to encode any ascii char
                that is encode uint in [0, 128) into one byte
            ii) use no more than 3 bytes to encode any unicode char 
                that is encode uint in [0, 0x110000) into 1~3 byte
                NOTE:
                    max bit_length(unicode_char) == 21
                    ==>> there are only 3 extra bits in 3 bytes : 3*8 - 21 = 3 bits
        a'') space efficiency - support word of size 2**K bytes
            for K in range(8):
                # 8, 16, 32, 64,   128, 256, 512, 1024   bits
                use no more than (2**K + 1) bytes to encode any word<2**K * 8bits>
            the more K values >= 8 supported, the better
        
            
        b) time efficiency:
            to fasten encode/decode time,
                should present the majority of uint bytes (in little/big-endian)
                directly in the final encoded bytes

                assume the platform supports C language
                ==>> the machine word, that is 'unsigned int' in C,
                    using a pure binary representation @[6.2.6.2 Integer types]
                    

            bytes'[\x00-\xfe]*\xff' is to slow to encode/decode
    

cases:
    uint
    uint_bytes = encode_uint_to_bytes(uint) # in big-endian
    size = len(uint_bytes) >= 1
    uint_bits = bin(uint)[len(bin(uint))-uint.bit_length():]
    
    1) BITS_BITSS_BYTES_CASE
        bits'1{,1}0.*'
        # last_layer using unit BYTE
        # using bits_layers to encoding total bytes
        # sized total bytes scheme

        NOTE:
            in bits_layers, should not begin with 0bit (>=1) since end_bit==0bit
            like the dynamic bytes case, we extract the first bit of each bits_layer into prefix bits


        def bits_layer2uint(bits):
            return uint_big_endian(bits) + 2**len(bits)
        bits'(?P<bits_part>1{num_bits_layers}0(?P<nth_bits_layer>[01]{bits_layer2uint((n-1)th_bits_layer)}){num_bits_layers})(?<bytes_part>[01]{8*bits_layer2uint(last_bits_layer)-len(bits_part)})'
        num_bits_layers does not count 0th_bits_layer
        assume 0th_bits_layer = bits''
        ==>> 0th_bits_layer_uint == 1
        bits'(0 )([01]{8*1-1})' # '' ==>> 1 ==>> 1  # xxx ==>> 1xxx ==>> 0b1xxx
        bits'(10 0)([01]{8*2-3})' # 0 ==>> 10 ==>> 2 # worse than DynamicBytes
        bits'(10 1)([01]{8*3-3})'
        bits'(110 0 00)([01]{8*4-6})' # worse than DynamicBytes
        bits'(110 0 01)([01]{8*5-6})' # worse than DynamicBytes
        bits'(110 0 10)([01]{8*6-6})'
        bits'(110 0 11)([01]{8*7-6})'
        bits'(110 1 000)([01]{8*8-7})' # 000 ==>> 1000 ==>> 8
        bits'(110 1 001)([01]{8*9-7})' # 001 ==>> 1001 ==>> 9
        ...
        bits'(110 1 111)([01]{8*15-7})'
        bits'(1110 0 00 0000)([01]{8*16-11})'
        bits'(1110 0 00 1111)([01]{8*31-11})'
        bits'(1110 0 01 00000)([01]{8*32-12})'
        bits'(1110 0 01 11111)([01]{8*63-12})'
        bits'(1110 0 10 000000)([01]{8*64-13})'
        bits'(1110 0 10 111111)([01]{8*127-13})'
        bits'(1110 0 11 0000000)([01]{8*128-14})'
        bits'(1110 0 11 1111111)([01]{8*255-14})'
        bits'(1110 1 000 00000000)([01]{8*256-16})'
        bits'(1110 1 000 11111111)([01]{8*511-16})'
        bits'(1110 1 111 111111111111111)([01]{8*65535-23})'

    2) BITS0_BITSS_BYTES_CASE
        bits"1{2,}00.*"
        # using bits'00' instead of bits'0' to terminate the bits represented num_bits_layers.
        bits'(?P<bits_part>1{num_bits_layers}00(?P<nth_bits_layer>[01]{bits_layer2uint((n-1)th_bits_layer)}){num_bits_layers})(?<bytes_part>[01]{8*bits_layer2uint(last_bits_layer)-len(bits_part)})'
        # -------------------------------    ^^    ----------------------------


        bits'(1100 0 00)([01]{8*4-7})' # worse than DynamicBytes
        bits'(1100 0 01)([01]{8*5-7})' # worse than DynamicBytes
        bits'(1100 0 10)([01]{8*6-7})' # worse than DynamicBytes
        bits'(1100 0 11)([01]{8*7-7})'
        bits'(1100 1 000)([01]{8*8-8})'
        bits'(1100 1 001)([01]{8*9-8})'

        
    3) FIXED_LENGTH_CASE:
        bits"11010(?P<K-4>[01]{8-4-1})(?P<uint_bits>[01]{8*2**K})"
        for K in range(4, 12) # [4..11] # 2KB
        since bits_layers_and_bytes_layer supports K in [0..1]
        since 0bits_layers_and_bytes_layer supports K in [2..3] # up to 15 bytes, so not include K==4


    5) UNDEFINED_CASE:
        bits"1{L}01[01]*" for L in range(3, 6) and L >= 7 # [3..5] and [7..]
        a non-extended decoder should not accept them
        a non-extended encoder should not generate them
    6) RESERVED_CASE:
        6-1) bits"11011[01]*"
            may use them to extend FIXED_LENGTH_CASE
        6-2) bits"11111101" # 0xFD
            may use it to begin other encoding
        
        
        




how to choose a case for a given uint?
    prefer to min len(uint_bytes)
    if encoded bytess are of same length:
        prefer order: FIXED_LENGTH_CASE > BITS_BITSS_BYTES_CASE/BITS0_BITSS_BYTES_CASE
    we may try all cases to encode uint and then choose the best one
    but, to ease encoding/decoding and testing, we do not enforce a standard form
        decoder should accept different represent of a same uint
            i.e. uint 0 can be encoded as
                1) b'\x00', b'\x80\x00', b'\xA0\x00\x00', ...
                2) b'\xD0' + b'\x00'*16, ...
            i.e. uint 1 can be encoded as:
                1) b'\x01', b'\x80\x01', b'\xA0\x00\x01', ...
                2) b'\xD0' + b'\x00'*15 + b'\x01', ...
            

    conclusion:
        let B = uint.bit_length()
        if B <= 21:
            use BITS_BITSS_BYTES_CASE
        elif B in [8*2**K-K-7..8*2**K] for K in [4..7]:
            use FIXED_LENGTH_CASE
        elif B in [8*2**K-K-8..8*2**K] for K in [8..11]:
            use FIXED_LENGTH_CASE
        else:
            use BITS0_BITSS_BYTES_CASE

    
'''

MIN_K = 4
MAX_K = 11



def num_bits2num_bytes(num_bits):
    return (num_bits+7)//8



def uint_bit_length2total_bytes__B0(uint_bit_length):
    return uint_bit_length2total_bytes__B(uint_bit_length, num_extra_prefix_bits=1)
num_uint_bits2total_bytes__B0 = uint_bit_length2total_bytes__B0
def uint_bit_length2total_bytes__B(uint_bit_length, num_extra_prefix_bits=0):
    uint_byte_length = num_bits2num_bytes(uint_bit_length)
    if uint_byte_length == 0:
        uint_byte_length = 1

    total = uint_byte_length
    while True:
        total_prefix_bits__B = uint_bit_length2total_prefix_bits__B(total.bit_length())
        total_prefix_bits = total_prefix_bits__B + num_extra_prefix_bits
        next_total = (total_prefix_bits + uint_bit_length + 7)//8
        
        if next_total > total:
            total = next_total
        elif next_total == total:
            break
        else:
            print(pure_payload_length)
            raise logic-error
    return total
def uint_bit_length2total_prefix_bits__B(uint_bit_length):
    if uint_bit_length == 0:
        return 1
    num_last_layer_bits = uint_bit_length - 1 # omits the leading 1
    total_layers_bits, num_layers = num_bits2total_layers_bits_and_num_layers(num_last_layer_bits)
    
    return num_layers + 1 + total_layers_bits
def uint_bit_length2total_prefix_bits__B0(uint_bit_length):
    return 1+uint_bit_length2total_prefix_bits__B(uint_bit_length)

def num_bits2total_layers_bits_and_num_layers(num_last_layer_bits):
    # assume num_last_layer_bits omits the leading 1
    # num_layers not include 0th_layer
    if not num_last_layer_bits:
        return (0, 0) 
    
    num_curr_layer_bits = num_last_layer_bits
    total = 0
    num_layers = 0
    while num_curr_layer_bits > 1:
        total += num_curr_layer_bits
        num_prev_layer_bits = num_curr_layer_bits.bit_length() - 1 # omit leading 1

        # for next round
        num_curr_layer_bits = num_prev_layer_bits
        num_layers += 1
    total += num_curr_layer_bits
    num_layers += 1 # not include 0th_layer
    return total, num_layers


assert uint_bit_length2total_bytes__B0(8*2**(MIN_K-1)) == 1+2**(MIN_K-1)
assert uint_bit_length2total_bytes__B0(8*2**MIN_K) > 1+2**MIN_K

def num_uint_bits2total_bytes__F(num_uint_bits):
    num_last_layer_bytes = num_bits2num_bytes(num_uint_bits)
    return total_bytes__F(num_last_layer_bytes)
def total_bytes__F(num_last_layer_bytes):
    # find min K, s.t. 2**K >= num_last_layer_bytes
    K = num_last_layer_bytes.bit_length()
    if K == 0:
        return 1
    if 1 << (K-1) >= num_last_layer_bytes:
        
        K = K-1
        assert 1 << K == num_last_layer_bytes
    assert K > 0

    assert 1 << (K-1) < num_last_layer_bytes

    total = 1 + 2**K
    return total






def when_using_F_instead_of_B0(K): # in bits
    assert MIN_K <= K < MAX_K+1
    total_payload_bits_F = 2**K * 8
    num_bits_F = total_payload_bits_F + 8
    for uint_bit_length in range(total_payload_bits_F, -1, -1):
        #num_wasted_bits_F = num_bits_F - uint_bit_length
        total_bytes__F = num_uint_bits2total_bytes__F(uint_bit_length)
        total_bytes__B0 = num_uint_bits2total_bytes__B0(uint_bit_length)
        #num_wasted_bits_S = num_bits_S - uint_bit_length
        if total_bytes__B0 < total_bytes__F:
##            print(K, uint_bit_length)
##            print(total_bytes__T0, total_bytes__F)
            break
    return uint_bit_length + 1


def show_all_bits_when_F_over_B0():
    for K in range(MIN_K, MAX_K+1):
        low = when_using_F_instead_of_B0(K)
        high = 2**K * 8
        print(K, '[{}..{}] bits'.format(low, high))
        print('\tK = {}, high - low - K == {} bits'.format(K, high - low - K))

    '''
4 [117..128] bits
	K = 4, high - low - K == 7 bits
5 [244..256] bits
	K = 5, high - low - K == 7 bits
6 [499..512] bits
	K = 6, high - low - K == 7 bits
7 [1010..1024] bits
	K = 7, high - low - K == 7 bits
8 [2032..2048] bits
	K = 8, high - low - K == 8 bits
9 [4079..4096] bits
	K = 9, high - low - K == 8 bits
10 [8174..8192] bits
	K = 10, high - low - K == 8 bits
11 [16365..16384] bits
	K = 11, high - low - K == 8 bits

[8*2**K-K-7..8*2**K] for K in [4..7]
[8*2**K-K-8..8*2**K] for K in [8..11]
'''

show_all_bits_when_F_over_B0()









    




