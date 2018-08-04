
'''
SSLLH uint encoding

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
        bits"1{size-1}0(?P<leading_0s_and_uint_bits>[01]{7*size})"
        ==>> uint.bit_length() <= 7*size
    2) SMALL1_CASE:
        bits"1{size}0(?P<leading_0s_and_uint_bits>[01]{7*size-1})"
        ==>> uint.bit_length() <= 7*size-1
    3) LARGE_CASE:
        large_case_const_prefix_bits+bits"1{num_layers-offset}0(?P<first_layer_bits>[01]{8-(len(const_prefix_bits)+(num_layers-offset)+1)%8))})" + bytes"(?P<nth_layer_bytes>.{(n-1)th_uint}){num_layers-1}"
    4) LARGE1_CASE:
        large_case_const_prefix_bits+bits"1{num_layers-offset+1}0(?P<first_layer_bits>[01]{8-(len(const_prefix_bits)+(num_layers-offset+1)+1)%8))})" + bytes"(?P<nth_layer_bytes>.{(n-1)th_uint}){num_layers-1}"
    5) HUGE_CASE:
        begin_byte + (?P<nth_layer_bytes>.{(n-1)th_layer_uint})* + end_byte
        if len(nth_layer_bytes) != 0:
            nth_layer_bytes[0] != end_byte
        len(first_layer_bytes) == 1

requires:
    1) use one byte to encode ascii char
        that is encode uint in [0, 128) into one byte
        ==>> using SMALL_CASE
    2) encode any unicode char no more than 3 bytes
        that is encode uint in [0, 0x110000) into 1~3 byte
        NOTE:
            max bit_length(unicode_char) == 21
            ==>> there are only 3 extra bits in 3 bytes : 3*8 - 21 = 3 bits
            ==>> using SMALL_CASE
    so, bits"1{0,2}0.*" are encoded in SMALL_CASE

    let bits"1{4,}0.*" to be encoded in SMALL1_CASE
    let bits"1110.*" to be encoded in non-SMALL_CASE
        let bits"11101{0,2}0.*" to be encoded in LARGE_CASE
            large_case_const_prefix_bits == bits"1110"
            0 <= num_layers - offset <= 2
            0 == min num_layers - offset
            num_layers >= 2
            ==>> min num_layers == 2
            ==>> offset == 2
            in LARGE_CASE, 2 <= num_layers <= 4:
                at most 3 layers in HUGE_CASE
            
        let bits"11101{4,}0.*" to be encoded in LARGE1_CASE
        let bits"11101110.*" to be encoded in HUGE_CASE

how to choose a case for a given uint?
    prefer to min len(uint_bytes)
    we may try all cases to encode uint and then choose the best one
    but, to ease encoding and decoding, we do not force a standard form

    i.e. we can choose like below:
        LARGE_CASE/LARGE1_CASE use at least 1 non-last_layer bytes
        HUGE_CASE use at least 2 non-layers bytes
    if when SMALL_CASE/SMALL1_CASE use >=8 prefix bits, we switch to large_case:
        ==>> uint.bit_length() >= (7*7-1) + 1 == 49 bits # now in SMALL1_CASE
        <==> uint.byte_length() >= 7
        LARGE_CASE bits"11100.*" has 3bits/1byte for first layer and 0~7 bytes for second/last layer
            efficiency <= 7/8
        if uint.byte_length() == 7:
            that is 49 <= uint.bit_length() <= 56
            ==>> efficiency(LARGE_CASE) == 7/8 == efficiency(SMALL_CASE) > efficiency(SMALL1_CASE)
            ==>> prefer to LARGE_CASE than SMALL1_CASE
        but if uint.byte_length() > 7:
            LARGE_CASE/LARGE1_CASE use at least 2 non-uint bytes
            worse than SMALL_CASE/SMALL1_CASE
    if when SMALL_CASE/SMALL1_CASE use >=16 prefix bits, we switch to large_case:
        ==>> uint.bit_length() >= (7*15-1) + 1 == 105 bits # now in SMALL1_CASE
        <==> uint.byte_length() >= 14
        LARGE_CASE use 2 extra bytes
    if when LARGE_CASE/LARGE1_CASE use >=16 prefix bits, we switch to huge_case:
        ==>> len(large_case_const_prefix_bits) + (num_layers-offset+1) + 1 >= 16
        ==>> 4 + (num_layers-2+1) + 1 >= 16
        ==>> num_layers >= 12
        assume num_layers == 12 in LARGE_CASE/LARGE1_CASE \
               and first_layer_uint == 1 \
               and second_layer_uint > 1
        ==>> 11 layers in HUGE_CASE and first_layer_uint >= 2

    conclusion:
        let B = uint.bit_length()
        let L, F = get num_layers and first_layer_uint from encode<HUGE_CASE>(uint)
        if L > 11 layers or (L == 11 and F > 1):
            use HUGE_CASE
        elif L >= 4:
            use LARGE1_CASE
        elif uint.byte_length() == 7 or >= 14:
            use LARGE_CASE
        elif uint.bit_length() >= 22:
            use SMALL1_CASE
        else:
            use SMALL_CASE

        # or
        if B <= 21:
            use SMALL_CASE
        elif B <= 48 or 56 < B <= 104:
            use SMALL1_CASE
        elif L <= 3:
            use LARGE_CASE
        elif L < 11 or (L == 11 and F == 1):
            use LARGE1_CASE
        else:
            use HUGE_CASE

        
    
    
            
        
    
'''
