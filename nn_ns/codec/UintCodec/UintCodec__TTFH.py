
r'''
TTFH uint encoding
    trilayers/trilayers0
    FIXED-LENGTH
    HUGE

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
    1) TRILAYERS_CASE:
        '1{num_delta_bits}0(?P<delta_bits>[01]{num_delta_bits})(?P<uint_bits>[01]{8*(2**num_delta_bits+delta_uint)-2*num_delta_bits-1})'
        for size in [1..3]
        for num_delta_bits in [0..1]
    2) TRILAYERS0_CASE:
        bits'1{num_delta_bits}00(?P<delta_bits>[01]{num_delta_bits})(?P<uint_bits>[01]{8*(2**num_delta_bits+delta_uint)-2*num_delta_bits-2})'
        for size >= 4
        for num_delta_bits >= 2

        ######
        bits"0[01]{7}"
            to support ascii
        bits"10(0)(?P<uint_bits>[01]{2*8-3})"
        bits"10(1)(?P<uint_bits>[01]{3*8-3})"
            to support unicode
        bits"1100([01]{2}).*" ==>> TRILAYERS0_CASE
        bits"1101.*" ==>> FIXED_LENGTH_CASE
        
    3) FIXED_LENGTH_CASE:
        bits"11010(?P<K-4>[01]{8-4-1})(?P<uint_bits>[01]{8*2**K})"
        for K in range(4, 12) # [4..11] # 2KB
        since TRILAYERS_CASE supports K in [0..2]
        since TRILAYERS0_CASE supports K == 3 # up to 15 bytes, so not include K==4
        
            
    
    4) HUGE_CASE:
        begin_byte = bits"11111101" # 0xFD
        end_byte = 0x00
        uint == 0 ==>> begin_byte end_byte
        uint >  0 ==>> begin_byte first_layer_byte (?<nth_layer_bytes>.{(n-1)th_layer_uint})* end_byte
            len(nth_layer_bytes) > 0 ==>> nth_layer_bytes[0] != 0x00 == end_byte
    5) UNDEFINED_CASE:
        bits"1{L}01[01]*" for L in range(3, 6) and L >= 7 # [3..5] and [7..]
        a non-extended decoder should not accept them
        a non-extended encoder should not generate them
    6) RESERVED_CASE:
        bits"11011[01]*"
        may use to extend FIXED_LENGTH_CASE
        
        




how to choose a case for a given uint?
    prefer to min len(uint_bytes)
    if encoded bytess are of same length:
        prefer order: FIXED_LENGTH_CASE > HUGE_CASE > TRILAYERS_CASE > TRILAYERS0_CASE
    we may try all cases to encode uint and then choose the best one
    but, to ease encoding/decoding and testing, we do not enforce a standard form
        decoder should accept different represent of a same uint
            i.e. uint 0 can be encoded as
                1) b'\x00', b'\x80\x00', b'\xA0\x00\x00', ...
                2) b'\xD0' + b'\x00'*16, ...
                3) b'\xFD\x00'
            i.e. uint 1 can be encoded as:
                1) b'\x01', b'\x80\x01', b'\xA0\x00\x01', ...
                2) b'\xD0' + b'\x00'*15 + b'\x01', ...
                3) b'\xFD\x01\x00', b'\xFD\x01\x01\x00', ...
            

    i.e. we can choose like below:
        FIXED_LENGTH_CASE use 1 non-last_layer bytes and some leading zero bytes in last_layer
        HUGE_CASE use at least 2 non-layers bytes; normally 3, 5 or 6 bytes non-last_layer bytes
        

    if when TRILAYERS_CASE/TRILAYERS0_CASE use >=48 prefix bits, we switch to HUGE_CASE:
        ==>> uint.bit_length() >= (2**23-1)*8 - 46 + 1 == 67108811 bits # now in TRILAYERS0_CASE
        # ~= 8388602 bytes
    if u.bit_length() in [8*2**K-2*K-1..8*2**K] for K in [4..11], we switch to FIXED_LENGTH_CASE


    conclusion:
        let B = uint.bit_length()
        if B <= 21:
            use TRILAYERS_CASE
        elif B >= 67108811:
            use HUGE_CASE
        elif B in [8*2**K-2*K-1..8*2**K] for K in [4..11]:
            use FIXED_LENGTH_CASE
        else:
            use TRILAYERS0_CASE

    
'''

MIN_K = 4
MAX_K = 11



def num_bits2num_bytes(num_bits):
    return (num_bits+7)//8



def num_bits2all_layers_bytes(num_bits):
    num_last_layer_bytes = num_bits2num_bytes(num_bits)
    return num_bytes2all_layers_bytes(num_last_layer_bytes)
def num_bytes2all_layers_bytes(num_last_layer_bytes):
    if not num_last_layer_bytes:
        return 0
    
    num_curr_layer_bytes = num_last_layer_bytes
    total = 0
    while num_curr_layer_bytes > 1:
        total += num_curr_layer_bytes
        num_bits = num_curr_layer_bytes.bit_length()
        num_prev_layer_bytes = num_bits2num_bytes(num_bits)

        # for next round
        num_curr_layer_bytes = num_prev_layer_bytes
    total += num_curr_layer_bytes
    return total

def _try_num_bits2all_layers_bytes():
    for num_bits in [0, 8, 255*8, 0xffff*8]:
        for num_bits in range(num_bits, num_bits+2):
            print(num_bits, num_bits2num_bytes(num_bits), num_bits2all_layers_bytes(num_bits))
    
    '''
0 0 0
1 1 1
8 1 1
9 2 3
2040 255 256
2041 256 259
524280 65535 65538
524281 65536 65540
'''

def num_uint_bits2total_bytes__T0(num_uint_bits):
    if num_uint_bits == 0:
        return 1

    pure_payload_length = num_uint_bits

##    total >= 1
##    len_of_length_field = total.bit_length() - 1
##    len_of_leading_1s = len_of_length_field
##    len_of_pure_prefix = len_of_leading_1s + 2 + len_of_length_field
##        == total.bit_length() * 2
##    len_of_leading_pad_0s = 7-(len_of_pure_prefix + pure_payload_length -1)%8
##    8*total == len_of_pure_prefix + len_of_leading_pad_0s + pure_payload_length
##        == total.bit_length() * 2
##         + len_of_leading_pad_0s
##         + pure_payload_length
##        == (total.bit_length() * 2 + pure_payload_length + 7)//8 *8
##    total == (total.bit_length() * 2 + pure_payload_length + 7)//8

    
    total = 0
    while True:
        next_total = (total.bit_length() * 2 + pure_payload_length + 7)//8
        
        if next_total > total:
            total = next_total
        elif next_total == total:
            break
        else:
            print(pure_payload_length)
            raise logic-error
    return total

assert num_uint_bits2total_bytes__T0(8*2**(MIN_K-1)) == 1+2**(MIN_K-1)
assert num_uint_bits2total_bytes__T0(8*2**MIN_K) > 1+2**MIN_K
def num_uint_bits2total_bytes__H(num_uint_bits):
    num_last_layer_bytes = num_bits2num_bytes(num_uint_bits)
    return total_bytes__H(num_last_layer_bytes)
def num_uint_bits2total_bytes__F(num_uint_bits):
    num_last_layer_bytes = num_bits2num_bytes(num_uint_bits)
    return total_bytes__F(num_last_layer_bytes)

def total_bytes__H(num_last_layer_bytes):
    total = 1 + num_bytes2all_layers_bytes(num_last_layer_bytes) + 1
    return total

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






def when_using_F_instead_of_T0(K): # in bits
    assert MIN_K <= K < MAX_K+1
    total_payload_bits_F = 2**K * 8
    num_bits_F = total_payload_bits_F + 8
    for uint_bit_length in range(total_payload_bits_F, -1, -1):
        #num_wasted_bits_F = num_bits_F - uint_bit_length
        total_bytes__F = num_uint_bits2total_bytes__F(uint_bit_length)
        total_bytes__T0 = num_uint_bits2total_bytes__T0(uint_bit_length)
        #num_wasted_bits_S = num_bits_S - uint_bit_length
        if total_bytes__T0 < total_bytes__F:
##            print(K, uint_bit_length)
##            print(total_bytes__T0, total_bytes__F)
            break
    return uint_bit_length + 1

def when_using_H_instead_of_T0(max_num_uint_bits=67108811+1000): # in bits
    # 67108811?
    for uint_bit_length in range(max_num_uint_bits, -1, -1):
        #num_wasted_bits_F = num_bits_F - uint_bit_length
        total_bytes__H = num_uint_bits2total_bytes__H(uint_bit_length)
        total_bytes__T0 = num_uint_bits2total_bytes__T0(uint_bit_length)
        #num_wasted_bits_S = num_bits_S - uint_bit_length
        if total_bytes__T0 < total_bytes__H:
##            print(K, uint_bit_length)
##            print(total_bytes__T0, total_bytes__H)
            break
    return uint_bit_length + 1

#print(when_using_H_instead_of_T0(), 'bits')
assert 67108811 == when_using_H_instead_of_T0()

def show_all_bits_when_F_over_T0():
    for K in range(MIN_K, MAX_K+1):
        print(K, '[{}..{}] bits'.format(when_using_F_instead_of_T0(K), 2**K * 8))

    '''

4 [119..128] bits
5 [245..256] bits
6 [499..512] bits
7 [1009..1024] bits
8 [2031..2048] bits
9 [4077..4096] bits
10 [8171..8192] bits
11 [16361..16384] bits

[8*2**K-2*K-1..8*2**K]
'''

#show_all_bits_when_F_over_T0()










def when_using_F_instead_of_H(K): # in bytes
    assert MIN_K <= K <= MAX_K
    total_payload_bytes_F = 2**K
    num_bytes_F = 1 + total_payload_bytes_F
    for num_last_layer_bytes in range(total_payload_bytes_F, -1, -1):
        tF = total_bytes__F(num_last_layer_bytes)
        num_bytes_H = total_bytes__H(num_last_layer_bytes)
        if num_bytes_H < num_bytes_F:
            break
    return num_last_layer_bytes + 1


def show_all_bytes_when_F_over_H():
    for K in range(MIN_K, MAX_K+1):
        print(K, '[{}..{}] bytes'.format(when_using_F_instead_of_H(K), 2**K))





    




