
r'''
SSFH uint encoding
    SMALL/SMALL0
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
    1) SMALL_CASE:
        bits"(1{size-1})(0)(?P<uint_bits>[01]{8*size-(size-1)-1)})"
        for size == 1 or size == 3 or size >= 8
    2) SMALL0_CASE:
        bits"(1{size-1})(00)(?P<uint_bits>[01]{8*size-(size-1)-2)})"
        for size == 2 or size in range(4,8) # 2 or [4..7]
        for uint.bit_length() in [14, 28, 35, 42, 49]

        ######
        bits"0[01]{7}" - special
            to support ascii
        bits"1(00)(?P<uint_bits>[01]{2*8-3})"
        bits"1(01).*" ==>> FIXED_LENGTH_CASE
        bits"1(10)(?P<uint_bits>[01]{3*8-3})" - special
            to support unicode
        
    3) FIXED_LENGTH_CASE:
        bits"1(01)0(?P<K-3>[01]{8-3-1})(?P<uint_bits>[01]{8*2**K})"
        for K in range(3, 19) # [3..18]
        since SMALL_CASE supports K in [0..2]
        
            
    
    4) HUGE_CASE:
        begin_byte = bits"11111101" # 0xFD
        end_byte = 0x00
        uint == 0 ==>> begin_byte end_byte
        uint >  0 ==>> begin_byte first_layer_byte (?<nth_layer_bytes>.{(n-1)th_layer_uint})* end_byte
            len(nth_layer_bytes) > 0 ==>> nth_layer_bytes[0] != 0x00 == end_byte
    5) UNDEFINED_CASE:
        bits"1{L}01[01]*" for L in range(3, 6) # [3..5]
    6) RESERVED_CASE:
        bits"1(01)1[01]*"
        may use to extend FIXED_LENGTH_CASE
        
        




how to choose a case for a given uint?
    prefer to min len(uint_bytes)
    if encoded bytess are of same length:
        prefer order: FIXED_LENGTH_CASE > HUGE_CASE > SMALL_CASE
    we may try all cases to encode uint and then choose the best one
    but, to ease encoding and decoding, we do not enforce a standard form
        decoder should accept different represent of same uint
            i.e. uint 0 can be encoded as
                1) b'\x00', b'\x80\x00', b'\xC0\x00\x00', ...
                2) b'\xA0' + b'\x00'*8, ...
                3) b'\xFD\x00'
            i.e. uint 1 can be encoded as:
                1) b'\x01', b'\x80\x01', b'\xC0\x00\x01', ...
                2) b'\xA0' + b'\x00'*7 + b'\x01', ...
                3) b'\xFD\x01\x00', b'\xFD\x01\x01\x00', ...

    i.e. we can choose like below:
        FIXED_LENGTH_CASE use 1 non-last_layer bytes and some leading zero bytes in last_layer
        HUGE_CASE use at least 2 non-layers bytes; normally 3, 5 or 6 bytes non-last_layer bytes
        

    if when SMALL_CASE/SMALL0_CASE use >=24 prefix bits, we switch to HUGE_CASE:
        ==>> uint.bit_length() >= (7*23) + 1 == 162 bits # now in SMALL_CASE
    if u.bit_length() in [57..64] or [113..128], we switch to FIXED_LENGTH_CASE


    conclusion:
        let B = uint.bit_length()
        let L = uint.byte_length()
        if B < 162:
            if B < 57 or 64 < B < 113 or 128 < B < 162:
                if B in [14, 28, 35, 42, 49]:
                    use SMALL0_CASE
                else:
                    use SMALL_CASE
            else:
                use FIXED_LENGTH_CASE
        elif total_bytes__H(L) < total_bytes__F(L):
            use HUGE_CASE
        else:
            use FIXED_LENGTH_CASE



        
    
    
            
        
    
'''



def when_using_F_instead_of_S(K): # in bits
    assert 3 <= K < 19
    total_payload_bits_F = 2**K * 8
    num_bits_F = total_payload_bits_F + 8
    for uint_bit_length in range(total_payload_bits_F, -1, -1):
        #num_wasted_bits_F = num_bits_F - uint_bit_length
        bytes_size_S = (uint_bit_length+6)//7
        num_bits_S = 8*bytes_size_S
        #num_wasted_bits_S = num_bits_S - uint_bit_length
        if num_bits_S < num_bits_F:
            break
    return uint_bit_length + 1

assert when_using_F_instead_of_S(3) == 57

def show_all_bits_when_F_over_S():
    for K in range(3, 19):
        print(K, '[{}..{}] bits'.format(when_using_F_instead_of_S(K), 2**K * 8))

    '''

3 [57..64]
4 [113..128]
5 [225..256]
6 [449..512]
7 [897..1024]
8 [1793..2048]
9 [3585..4096]
10 [7169..8192]
11 [14337..16384]
12 [28673..32768]
13 [57345..65536]
14 [114689..131072]
15 [229377..262144]
16 [458753..524288]
17 [917505..1048576]
18 [1835009..2097152]
'''


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

def when_using_F_instead_of_H(K): # in bytes
    assert 3 <= K < 19
    total_payload_bytes_F = 2**K
    num_bytes_F = 1 + total_payload_bytes_F
    for num_last_layer_bytes in range(total_payload_bytes_F, -1, -1):
        tF = total_bytes__F(num_last_layer_bytes)
        num_bytes_H = total_bytes__H(num_last_layer_bytes)
        if num_bytes_H < num_bytes_F:
            break
    return num_last_layer_bytes + 1
assert when_using_F_instead_of_H(3) == 6

def show_all_bits_when_F_over_H():
    for K in range(3, 19):
        print(K, '[{}..{}] bytes'.format(when_using_F_instead_of_H(K), 2**K))

show_all_bits_when_F_over_H()



    




