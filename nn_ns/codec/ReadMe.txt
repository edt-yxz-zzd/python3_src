# '*' stands for repeating in regex
# \d stands for length of type mask bits
# e.g.
#   "4222" means total 4 bytes (len("4222") == 4)
#       first byte has 4 mask bits
#       other bytes each have 2 mask bits
#   "31*3" means a least 2 bytes
#       len(31*3) == len("3")+len(rex"1*")+len("3") >= 1+0+1 == 2
#       first/last byte has 3 mask bits
#       other bytes each have 1 mask bits
#   "2, 31*3" means there are 2 encode space: "2" | "31*3"
# why:
#   target: to encode any integer
#   1) text
#       "[0-9A-F]+ " ends by space
#       but waste lots of bits: <==> "4+8" -- waste 4 bits per byte!
#   2) (length :: Word, [byte])
#       cannot encode integer > (2**8)**(upper::Word)
#   3) pcode: 1*1 == rex_bytes"[^\00-\7F]*[\00-\7F]"
#       <==> extract all mask bits and put in front of payload bits
#       <==> scode: rex_bits"(1*0[01]*)&([01]{8}+)"
#       <==> (length :: UInt, [byte])
#       but encode UInt into (UInt, [byte])??
#       it suggests a ineffient encoding for UInt at length field.
#   4) UInt --> (length :: UInt, [bytes]) --> ((UInt, [bytes]), [bytes])
#           -->* [[bytes]]
#       recursively encode the length field!
#   but pointer should be fixed length to be useful to be used in array

ascii:
    1
utf32:
    0000

// non-overlapped
    utf8: 
        1, 32, 422, 5222
    ucode:
        1, 32*3
        2, 31*3 # dyncode
        21*2
        2, 22*2
// some codes are suffixes of others
    pcode: 
        1*1 # dynamic_bytes = rex_rb'[^\x00-\x7f]*[\x00-\x7f]'
// overlapped
    scode: // move all mask bits of pcode into front of bits
        (8*[1-8])0{7*len(\g<1>)}
            // begins with bit pattern: rex_bits"1*0"
            // easier to be decoded than pcode




bits/small_uint(word) can be stored in pcode
int can be encoded as a uint: 
    int2uint(i) = i*2 if i >= 0 else -i*2-1
    uint2int(u) = -(u+1)/2 if u % 2 else u/2
bytes can be stored as (uint, bytes) # struct{uint size; byte data[size];};
big_uint can be stored as bytes
uint:
    when small ==>> small_uint
    when big ==>> big_uint

    example 1:
        0~127 ==>> [\x00-\x7f]
        128~2**(8*127)-1 ==>> size:1~127::[\x80-\xfe]-\x7f, data::byte[size]
        2**(8*127)~+oo ==>> \xff, size:128~+oo::pcode+128, data::byte[size]
    example 2:
        SMALL case : pcode of len 1~L
            use \xff as the BIG case, so pcode should not leading with \xff
                use a modify version of pcode, which ::= ([\x80-\xbf][\x80-\xff]*)?[\x00-\x7f]
                length of bits : 7 | 6 + 7 | (6+7*(L-2)) + 7 = 7*L-[L>1]
                not leading with [\xc0-\xff]
            wasting 8*L-(length of bits) = L+[L>1] bits as prefixes
        BIG case : (size::uint, data::bytes)
            leading with [\xc0-\xff]
                use a modify version of pcode, which ::= ([\xc0-\xff][\x80-\xff]*)?[\x00-\x7f]
                at least two bytes, waste 16bits
                so, L+[L>1] <= 16 ==>> 1<= L <= 15
                let L be 14
                    ==>> SMALL case 97bits
                    98bits ==>> 2+ceil(98/8) = 15 bytes; 0.866667 ~ 13/15 > (7*L-1)/(8*L) = 97/112 ~ 0.866071

        note that second bit can be considered as last bit of u::uint,
            what if encode u as int?
            if leading by [\x00-\x7f], read as u::uint
            elif read as x::int
                if x >= 0:
                    u = x
                else:
                    size = -x  # non-std; at least 2 bytes
                    read u from byte[size]
        
        replace pcode by scode





















