
from .UintBytesCodec import bigEndianUintBytesCodec


class SintUintCodec:
    def sint2uint(self, i):
        raise NotImplementedError
    def uint2sint(self, u):
        raise NotImplementedError
class SintUintCodec__Neg2Odd(SintUintCodec):
    'negative integer map to odd integer'
    def sint2uint(self, i):
        return 2*i if i >= 0 else -2*i-1
    def uint2sint(self, u):
        return -((u+1)//2) if u & 1 else u//2
class SintUintCodec__Neg2Odd_but1(SintUintCodec):
    'negative integer map to odd integer except 1'
    def sint2uint(self, i):
        return 2*i if i >= 0 else -2*i+1
    def uint2sint(self, u):
        if u == 1:
            raise ValueError('uint == 1')
        return -(u//2) if u & 1 else u//2
class SintUintCodec__msb_2nd(SintUintCodec):
    'insert the sign bit after MSB of abs(sint)'
    def sint2uint(self, i):
        if i >= 0:
            u = i
            L = u.bit_length()
            msb = 1 << (L-1) if L else 0
            u += msb # move msb left 1 bit
            # u == 0 or bit-pattern"10[01]*"
        else:
            u = -i - 1
            L = u.bit_length()
            u += 1 << L # prefix with bit'1'
            # u == 1 or bit-pattern"11[01]*"
        return u
    
    def uint2sint(self, u):
        assert u >= 0
        if u < 2:
            # 0, 1 ==>> 0, -1
            return -u
        L = u.bit_length()
        msb_2nd = 1 << (L-2)
        is_neg = bool(msb_2nd & u)
        if is_neg:
            msb = 1 << (L-1)
            return msb - u - 1
        else:
            return u - msb_2nd # move msb right 1 bit


aSintUintCodec__Neg2Odd = SintUintCodec__Neg2Odd()
aSintUintCodec__Neg2Odd_but1 = SintUintCodec__Neg2Odd_but1()

class SintUintCodec__Neg2Odd_but1_of_1stByte(SintUintCodec):
    'Neg2Odd_but1(first byte in big-endian bytes of abs)'
    def sint2uint(self, i):
        uint2bytes = bigEndianUintBytesCodec.uint2bytes
        bytes2uint = bigEndianUintBytesCodec.bytes2uint
        sint2uint = aSintUintCodec__Neg2Odd_but1.sint2uint
        
        ui = abs(i)
        ibs = uint2bytes(ui)
        if ibs:
            b = ibs[0]
            sb = -b if i < 0 else b
            ub = sint2uint(sb)
            bs12 = uint2bytes(ub)
            assert len(bs12) == 1 or (len(bs12) == 2 and (bs12[0] == 1))

            ubs = bs12 + ibs[1:]
        else:
            ubs = ibs
        u = bytes2uint(ubs)
        return u
    def uint2sint(self, u):
        uint2bytes = bigEndianUintBytesCodec.uint2bytes
        bytes2uint = bigEndianUintBytesCodec.bytes2uint
        uint2sint = aSintUintCodec__Neg2Odd_but1.uint2sint
        
        ubs = uint2bytes(u)
        if ubs:
            b = ubs[0]
            if b == 1:
                bs12 = ubs[:2] # maybe of len 1 if len(ubs)==1
            else:
                bs12 = ubs[:1]

            assert len(bs12) == 1 or (len(bs12) == 2 and (bs12[0] == 1))
            ub = bytes2uint(bs12)
            sb = uint2sint(ub)
            b = abs(sb)
            assert 0 <= b <= 0xff
            ibs1 = bytes([b])
            assert len(ibs1) == 1

            ibs = ibs1 + ubs[len(bs12):]
            ui = bytes2uint(ibs)
            i = -ui if sb < 0 else ui
        else:
            i = u
            
        return i

aSintUintCodec__Neg2Odd_but1_of_1stByte = SintUintCodec__Neg2Odd_but1_of_1stByte()
def test_SintUintCodec():
    for SintUintCodecT in [SintUintCodec__msb_2nd,
                           SintUintCodec__Neg2Odd,
                           SintUintCodec__Neg2Odd_but1,
                           SintUintCodec__Neg2Odd_but1_of_1stByte,
                           ]:
        aSintUintCodec = SintUintCodecT()
        _test_SintUintCodec(aSintUintCodec, range(-1000, 1000))
        _test_SintUintCodec(aSintUintCodec, [i for L in range(300)
                                               for u in [1<<L]
                                               for i in [u, -u, u+1, -u-1]])
                            
def _test_SintUintCodec(aSintUintCodec, rng):
    c = aSintUintCodec
    for i in rng:
        try:
            assert i == c.uint2sint(c.sint2uint(i))
        except:
            print("testing i={}; type={}".format(i, type(c)))
            u = c.sint2uint(i)
            i_from_u = c.uint2sint(u)
            print("sint2uint(i={})={}".format(i, u))
            print("uint2sint(u={})={}".format(u, i_from_u))
            raise
                  

test_SintUintCodec()
