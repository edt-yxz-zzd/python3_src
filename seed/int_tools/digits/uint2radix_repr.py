
#r"""[[[

r'''
py -m seed.int_tools.digits.uint2radix_repr
from seed.int_tools.digits.uint2radix_repr import uint2radix_repr, IUint2RadixRepr__little_endian__plain, IUint2RadixRepr, Uint2RadixRepr

e ../../python3_src/seed/int_tools/digits/uint2radix_repr.py
#'''
__all__ = '''
    uint2radix_repr

    IUint2RadixRepr__little_endian__plain
        IUint2RadixRepr
            Uint2RadixRepr
                uint2radix_repr
                    uint2radix_repr__little_endian
                    uint2radix_repr__big_endian
    '''.split()
from seed.int_tools.digits._common import _Int, _pow_ge1



from seed.tiny import null_iter
from seed.abc.abc import ABC, abstractmethod, override
from seed.seq_tools.bisearch import bisearch
from seed.helper.check.checkers import check_int, check_uint, check_uint_imay, check_type_is
import itertools

class IUint2RadixRepr__little_endian__plain(ABC):
    r'''
    #'''
    @abstractmethod
    def get_radix(sf, /):
        ...
    @abstractmethod
    def get_zero(sf, /):
        ...
    @abstractmethod
    def is_zero(sf, uint, /):
        ...
    @abstractmethod
    def divmod(sf, lhs, rhs, /):
        r'''
        lhs -> rhs -> (q,r)
        precondition:
            [not is_zero(rhs)]
            [lt__abs(one, rhs)]
        postcondition:
            [lhs == q*rhs+r]
            [lt__abs(r, rhs)]
            [lhs==0]or[lt__abs(q, lhs)]
        #'''
        ...
    #no def uint2radix_repr__big_endian__plain(sf, uint, /,*, min_len, imay_max_len):
    def uint2radix_repr__little_endian__plain(sf, uint, /,*, min_len, imay_max_len):
        r'count little_endian digits: pad_on_underflow, cut_on_overflow'
        #imay_min_len --> min_len
        check_uint(min_len)
        check_uint_imay(imay_max_len)
        assert min_len >= 0
        assert imay_max_len >= -1

        if imay_max_len == -1:
            j0 = -1
            def cut(i):
                return False
        else:
            max_len = imay_max_len
            if not max_len >= min_len: raise ValueError
            j0 = max_len
            def cut(i):
                return i == max_len

        is_zero = sf.is_zero
        _divmod = sf.divmod
        radix = sf.get_radix()
        #i = 0
        j = j0
        #while not (cut(i) or is_zero(uint)):
        while j and not is_zero(uint):
            uint, low_digit = _divmod(uint, radix)
            yield low_digit
            #i += 1
            j -= 1
        if 1:
            sz = j0-j
            if sz < min_len:
                #pad
                zero = sf.get_zero()
                yield from itertools.repeat(zero, min_len-sz)
class IUint2RadixRepr(IUint2RadixRepr__little_endian__plain):
    r'''
    #'''
    @abstractmethod
    def get_one(sf, /):
        ...
    @abstractmethod
    def lt__abs(sf, lhs, rhs, /):
        return sf.lt__abs__via_divmod(lhs, rhs)
    def lt__abs__via_divmod(sf, lhs, rhs, /):
        if sf.is_zero(rhs):
            return False
        elif sf.is_zero(lhs):
            return True
        else:
            q, r = sf.divmod(rhs, lhs)
            return sf.is_zero(q)

    @abstractmethod
    def add(sf, lhs, rhs, /):
        ...
    @abstractmethod
    def mul(sf, lhs, rhs, /):
        ...
    #uint2radix_repr
    #r'''
    def uint2radix_repr(sf, uint, /,*, is_big_endian:bool, _split_ver:'0|1', min_len, imay_max_len):
        f = sf.uint2radix_repr__big_endian if is_big_endian else sf.uint2radix_repr__little_endian
        return f(uint, _split_ver=_split_ver, min_len=min_len, imay_max_len=imay_max_len)
    def uint2radix_repr__big_endian(sf, uint, /,*, _split_ver:'1', min_len, imay_max_len):
        if _split_ver==0:
            #raise NotImplementedError
            return sf.uint2radix_repr__big_endian__plain(uint, min_len=min_len, imay_max_len=imay_max_len)
        elif _split_ver==1:
            return sf.uint2radix_repr__big_endian__split(uint, min_len=min_len, imay_max_len=imay_max_len)#(, _split_ver=_split_ver)
        else:
            raise Exception(f'unknown _split_ver={_split_ver}')
    def uint2radix_repr__little_endian(sf, uint, /,*, _split_ver:'0|1', min_len, imay_max_len):
        if _split_ver==0:
            return sf.uint2radix_repr__little_endian__plain(uint, min_len=min_len, imay_max_len=imay_max_len)
        elif _split_ver==1:
            return sf.uint2radix_repr__little_endian__split(uint, min_len=min_len, imay_max_len=imay_max_len)#(, _split_ver=_split_ver)
        else:
            raise Exception(f'unknown _split_ver={_split_ver}')
    #'''

    def uint2radix_repr__little_endian__split(sf, uint, /,*, min_len, imay_max_len):
        r'count little_endian digits: pad_on_underflow, cut_on_overflow'
        return sf.uint2radix_repr__split(uint, min_len=min_len, imay_max_len=imay_max_len, is_big_endian=False)
    def uint2radix_repr__big_endian__split(sf, uint, /,*, min_len, imay_max_len):
        r'count little_endian digits(not !!!big_endian!!!): pad_on_underflow, cut_on_overflow'
        #no def uint2radix_repr__big_endian__plain(sf, uint, /,*, min_len, imay_max_len):
        return sf.uint2radix_repr__split(uint, min_len=min_len, imay_max_len=imay_max_len, is_big_endian=True)
    uint2radix_repr__big_endian__plain=uint2radix_repr__big_endian__split
    def uint2radix_repr__split(sf, uint, /,*, min_len, imay_max_len, is_big_endian:bool):
        r'count little_endian digits(not !!!big_endian!!!): pad_on_underflow, cut_on_overflow'
        check_uint(min_len)
        check_uint_imay(imay_max_len)
        assert min_len >= -1
        assert imay_max_len >= -1

        if imay_max_len == -1:
            j0 = -1
            def cut(L):
                return False
        else:
            max_len = imay_max_len
            if not max_len >= min_len: raise ValueError
            j0 = max_len
            def cut(L):
                return L > max_len
        if imay_max_len == 0:
            return null_iter
            return
        #imay_max_len != 0

        is_zero = sf.is_zero
        zero = sf.get_zero()
        if is_zero(uint):
            #yield from
            return itertools.repeat(zero, min_len)
            return
        # |uint| != 0
        _divmod = sf.divmod
        lt__abs = sf.lt__abs
        mul = sf.mul
        radix = sf.get_radix()

        weight = radix
        weights = [weight]
        L = 1
        lens = [L]#2**iweight
        # |uint| != 0
        #imay_max_len != 0
        while not cut(L) and not lt__abs(uint, weight):
            weight = mul(weight, weight)
            weights.append(weight)
            L *= 2
            lens.append(L)
        ###
        if cut(L):
            # ==>> cut_on_overflow
            #imay_max_len != 0
            #imay_max_len != -1
            # 1 <= max_len < L
            pow_radix_max_len = _pow_ge1(mul, weights, max_len)#radix**max_len
            #bug:min_len = max_len
            #   should protected by [not |uint| < |pow_radix_max_len|], see below else-branch
            if lt__abs(uint, pow_radix_max_len):
                # 0 < |uint| < |pow_radix_max_len| == |radix**max_len| < |radix**L| == |weights[-1]| == |weight| == |weight[iweight]|
                iweight = len(weights)-1
                # weight is weights[iweight]
                pass
            else:
                # 0 < |uint| > |pow_radix_max_len| == |radix**max_len| < |radix**L| == |weights[-1]| == |weight| == |weight[iweight]|
                _, low = _divmod(uint, pow_radix_max_len)
                uint = low; del low
                min_len = max_len
                #min_len >= 1
                if is_zero(uint):
                    #yield from
                    return itertools.repeat(zero, min_len)
                    return
                # |uint| != 0
                (eqv_begin, eqv_end) = bisearch(uint, weights, __lt__=lt__abs)
                # 0 < |uint| < weights[eqv_end] == radix**(2**eqv_end)
                iweight = eqv_end
                weight = weights[iweight]
                # weight is weights[iweight]
            #break
        else:
            iweight = len(weights)-1
            # weight is weights[iweight]
        weight, iweight, weights, lens; del imay_max_len
        assert weight is weights[iweight]
        # weight is weights[iweight] == radix**(2**iweight)
        assert not is_zero(uint)
        assert lt__abs(uint, weight)
        assert iweight == 0 or not lt__abs(uint, weights[iweight-1])
        # |uint| != 0
        # 0 < |uint| < |weight|
        # [iweight==0]or[not |uint| < |weights[iweight-1]| ]

        f = sf._uint2radix_repr__big_endian__split__tail if is_big_endian else sf._uint2radix_repr__little_endian__split__tail
        return f(uint, min_len=min_len, iweight=iweight, weights=weights, lens=lens)


    def _uint2radix_repr__little_endian__split__tail(sf, uint, /,*, min_len, iweight, weights, lens):
        #is_zero = sf.is_zero
        zero = sf.get_zero()
        _divmod = sf.divmod
        lt__abs = sf.lt__abs
        #radix = sf.get_radix()

        imay_iweight_low_or_num_pad_zeros_pairs = []
            #[(iweight, low) | (-1, num_pad_zeros)]
            # |low| < |weights[iweight]|
            # num_pad_zeros > 0
        high = uint
        # 0 < |high| < |weight|
        sz = 0

        while 1:
            # 0 < |high| < |weight|
            # weight is weights[iweight]
            assert not imay_iweight_low_or_num_pad_zeros_pairs
            (eqv_begin, eqv_end) = bisearch(high, weights, begin=0, end=iweight, __lt__=lt__abs)
            if eqv_end==0:
                # 0 < |high| < |radix|
                high
                yield high
                sz += 1
                break
            iweight = eqv_end-1
            weight = weights[iweight]
            # weight is weights[iweight]
            # |weight| <= |high| < |weight|**2
            high, low = _divmod(high, weight)
            # |low| < |weight|
            # 0 < |high| < |weight|
            #imay_iweight_low_or_num_pad_zeros_pairs.append((iweight, low))
            imay_iweight_low_or_num_pad_zeros_pairs = [(iweight, low)]
            local_sz = lens[iweight]
            sz += local_sz
                #since push low, finally yield
            while imay_iweight_low_or_num_pad_zeros_pairs:
                imay_local_iweight, local_low_or_num_pad_zeros = imay_iweight_low_or_num_pad_zeros_pairs.pop()
                if imay_local_iweight == -1:
                    num_pad_zeros = local_low_or_num_pad_zeros
                    yield from itertools.repeat(zero, num_pad_zeros)
                    local_sz -= num_pad_zeros
                    continue
                local_iweight, local_low = imay_local_iweight, local_low_or_num_pad_zeros
                # 0 <= |local_low| < |weights[local_iweight]|
                #pad leading 0 until total digits = 2**local_iweight
                local_weight = weights[local_iweight]
                # local_weight is weights[local_iweight]
                local_total = lens[local_iweight]#2**local_iweight
                (eqv_begin, eqv_end) = bisearch(local_low, weights, begin=0, end=local_iweight, __lt__=lt__abs)
                if eqv_end==0:
                    # 0 <= |local_low| < |radix|
                    yield local_low
                    yield from itertools.repeat(zero, local_total-1)
                    local_sz -= local_total
                    continue
                local_iweight = eqv_end-1
                local_weight = weights[local_iweight]
                # local_weight is weights[local_iweight]
                # |local_weight| <= |local_low| < |local_weight|**2
                tmp_local_total = lens[eqv_end]#2**eqv_end#2**(1+local_iweight)
                num_pad_zeros = local_total-tmp_local_total
                assert num_pad_zeros >= 0
                if num_pad_zeros:
                    imay_iweight_low_or_num_pad_zeros_pairs.append((-1, num_pad_zeros))
                    #bug:local_sz -= num_pad_zeros
                    #   -= only when yield
                tmp_local_high, tmp_local_low = _divmod(local_low, local_weight)
                # |tmp_local_low| < |local_weight|
                # 0 < |tmp_local_high| < |local_weight|
                imay_iweight_low_or_num_pad_zeros_pairs.append((local_iweight, tmp_local_high))
                imay_iweight_low_or_num_pad_zeros_pairs.append((local_iweight, tmp_local_low))
                #bug:yield from itertools.repeat(zero, local_total-tmp_local_total)
                #   should yield after tmp_local_high, now using num_pad_zeros, see above
            assert local_sz == 0


        if sz < min_len:
            #pad
            yield from itertools.repeat(zero, min_len-sz)
        return
    #end-def _uint2radix_repr__little_endian__split__tail(sf, uint, /,*, min_len, iweight, weights, lens):
    def _uint2radix_repr__big_endian__split__tail(sf, uint, /,*, min_len, iweight, weights, lens):
        is_zero = sf.is_zero
        zero = sf.get_zero()
        _divmod = sf.divmod
        lt__abs = sf.lt__abs
        #radix = sf.get_radix()

        iweight_low_pairs = []
            #[(iweight, low)]
            # |low| < |weights[iweight]|
        high = uint
        # 0 < |high| < |weight|

        while 1:
            # 0 < |high| < |weight|
            # weight is weights[iweight]
            (eqv_begin, eqv_end) = bisearch(high, weights, begin=0, end=iweight, __lt__=lt__abs)
            if eqv_end==0:
                # 0 < |high| < |radix|
                iweight_low_pairs, high
                break
            iweight = eqv_end-1
            weight = weights[iweight]
            # weight is weights[iweight]
            # |weight| <= |high| < |weight|**2
            high, low = _divmod(high, weight)
            # |low| < |weight|
            # 0 < |high| < |weight|
            iweight_low_pairs.append((iweight, low))
        #########
        iweight_low_pairs, high
            # |low| < |weights[iweight]|
            # 0 < |high| < |radix|
        if 1:
            #print(min_len, iweight_low_pairs)
            total4pad = min_len
            total4pad -= sum(lens[iweight] for iweight, low in iweight_low_pairs)
                # total4pad may < 0
            iweight4high = 0
                # 0 < |high| < radix == radix**(2**iweight) where iweight==iweight4high==0
            total4pad -= lens[iweight4high]
                # total4pad may < 0
            total4pad = max(0, total4pad)
            yield from itertools.repeat(zero, total4pad)
                #yield as soon as possible
        total4pad
        del total4pad
        if 0:
            iweight_low_pairs.append((iweight4high, high))
        else:
            MSB = high
            yield MSB
        del high
        #for iweight, low in reversed(iweight_low_pairs):
        while iweight_low_pairs:
            iweight, low = iweight_low_pairs.pop()
            # 0 <= |low| < |weights[iweight]|
            #pad leading 0 until total digits = 2**iweight
            local_total = lens[iweight]#2**iweight
            weight = weights[iweight]
            # weight is weights[iweight]
            (eqv_begin, eqv_end) = bisearch(low, weights, begin=0, end=iweight, __lt__=lt__abs)
            if eqv_end==0:
                # 0 <= |low| < |radix|
                yield from itertools.repeat(zero, local_total-1)
                yield low
                continue
            iweight = eqv_end-1
            weight = weights[iweight]
            # weight is weights[iweight]
            # |weight| <= |low| < |weight|**2

            high, low = _divmod(low, weight)
            assert not is_zero(high)
            # |low| < |weight|
            # 0 < |high| < |weight|
            iweight_low_pairs.append((iweight, low))
            iweight_low_pairs.append((iweight, high))
            tmp_local_total = lens[eqv_end]#2**eqv_end#2**(1+iweight)
            assert local_total >= tmp_local_total
            if local_total > tmp_local_total:
                yield from itertools.repeat(zero, local_total-tmp_local_total)
                    #yield as soon as possible


        return
    #end-def _uint2radix_repr__big_endian__split__tail(sf, uint, /,*, min_len, iweight, weights, lens):




#end-class IUint2RadixRepr(IUint2RadixRepr__little_endian__plain):
class Uint2RadixRepr(IUint2RadixRepr):
    def __init__(sf, radix, /):
        if not sf.lt__abs(sf.get_one(), radix): raise ValueError
        sf.__radix = radix

    @override
    def get_radix(sf, /):
        return sf.__radix
    @override
    def get_zero(sf, /):
        return 0
    @override
    def get_one(sf, /):
        return 1
    @override
    def add(sf, lhs, rhs, /):
        return lhs+rhs
    @override
    def mul(sf, lhs, rhs, /):
        return lhs*rhs
    @override
    def lt__abs(sf, lhs, rhs, /):
        return lhs < rhs
    @override
    def is_zero(sf, uint, /):
        return uint == 0
    @override
    def divmod(sf, lhs, rhs, /):
        r'''
        lhs -> rhs -> (q,r)
        precondition:
            [not is_zero(rhs)]
            [lt__abs(one, rhs)]
        postcondition:
            [lhs == q*rhs+r]
            [lt__abs(r, rhs)]
            [lhs==0]or[lt__abs(q, lhs)]
        #'''
        return divmod(lhs, rhs)



class _Uint2RadixRepr(IUint2RadixRepr):
    def __init__(sf, radix, /):
        check_type_is(_Int, radix)
        check_int(radix.i, min=2)
        sf.__radix = radix

    @override
    def get_radix(sf, /):
        return sf.__radix
    @override
    def get_zero(sf, /):
        return _Int(0)
    @override
    def get_one(sf, /):
        return _Int(1)
    @override
    def add(sf, lhs, rhs, /):
        return _Int(lhs.i+rhs.i)
    @override
    def mul(sf, lhs, rhs, /):
        return _Int(lhs.i*rhs.i)

    @override
    def lt__abs(sf, lhs, rhs, /):
        return lhs.i < rhs.i
    @override
    def is_zero(sf, uint, /):
        return uint.i == 0
    @override
    def divmod(sf, lhs, rhs, /):
        r'''
        lhs -> rhs -> (q,r)
        precondition:
            [not is_zero(rhs)]
            [lt__abs(one, rhs)]
        postcondition:
            [lhs == q*rhs+r]
            [lt__abs(r, rhs)]
            [lhs==0]or[lt__abs(q, lhs)]
        #'''
        q,r = divmod(lhs.i, rhs.i)
        return _Int(q), _Int(r)



def uint2radix_repr__little_endian(radix, digits, /,*, _split_ver:'0|1'=1, min_len=0, imay_max_len=-1):
    return Uint2RadixRepr(radix).uint2radix_repr__little_endian(digits, _split_ver=_split_ver, min_len=min_len, imay_max_len=imay_max_len)
def uint2radix_repr__big_endian(radix, digits, /,*, _split_ver:'0|1'=1, min_len=0, imay_max_len=-1):
    return Uint2RadixRepr(radix).uint2radix_repr__big_endian(digits, _split_ver=_split_ver, min_len=min_len, imay_max_len=imay_max_len)
def uint2radix_repr(radix_or_an_IUint2RadixRepr, digits, /,*, is_big_endian:bool, _split_ver:'0|1'=1, min_len=0, imay_max_len=-1, input_is_an_IUint2RadixRepr_not_radix=False):
    if input_is_an_IUint2RadixRepr_not_radix:
        an_IUint2RadixRepr = radix_or_an_IUint2RadixRepr
    else:
        radix = radix_or_an_IUint2RadixRepr
        an_IUint2RadixRepr = Uint2RadixRepr(radix)
    return an_IUint2RadixRepr.uint2radix_repr(digits, is_big_endian=is_big_endian, _split_ver=_split_ver, min_len=min_len, imay_max_len=imay_max_len)

def _t2():
    radix = 2
    test_data = [
            (5,6,  16, [1,0,0,0,0])
            ]
    _loop4test_uint2radix_repr(radix, test_data)
    ######################
    ######################
    ######################
    #sf = Uint2RadixRepr(10)
    radix = 10
    test_data = [
            (5,6,  16, [0,0,0,1,6])
            ######################
            ,(0,-1,  1573, [1,5,7,3])
            ,(4,-1,  1573, [1,5,7,3])
            ,(5,-1,  1573, [0,1,5,7,3])
            ,(6,-1,  1573, [0,0,1,5,7,3])
            ,(7,-1,  1573, [0,0,0,1,5,7,3])
            ,(8,8,  1573, [0,0,0,0,1,5,7,3])
            ,(4,4,  1573, [1,5,7,3])
            ,(0,4,  1573, [1,5,7,3])
            ,(0,3,  1573, [5,7,3])
            ,(0,2,  1573, [7,3])
            ,(0,1,  1573, [3])
            ,(0,0,  1573, [])
            ######################
            ,(0,-1,  102003000400001573, [1,0,2,0,0,3,0,0,0,4,0,0,0,0,1,5,7,3])
            ,(0,-1,  1020030004000015730, [1,0,2,0,0,3,0,0,0,4,0,0,0,0,1,5,7,3,0])
            ,(0,-1,  10200300040000157300, [1,0,2,0,0,3,0,0,0,4,0,0,0,0,1,5,7,3,0,0])
            ,(0,-1,  102003000400001573000, [1,0,2,0,0,3,0,0,0,4,0,0,0,0,1,5,7,3,0,0,0])
            ,(0,-1,  1020030004000015730000, [1,0,2,0,0,3,0,0,0,4,0,0,0,0,1,5,7,3,0,0,0,0])
            ,(0,-1,  10200300040000157300000, [1,0,2,0,0,3,0,0,0,4,0,0,0,0,1,5,7,3,0,0,0,0,0])
            ]
    #_loop4test_uint2radix_repr(sf, test_data)
    _loop4test_uint2radix_repr(radix, test_data)

    ######################
    ######################
    ######################
    #sf = Uint2RadixRepr(2)
    radix = 2
    def mk_ans__radix2__big(min_len, imay_max_len, uint, /):
        bits = bin(uint)[2:] if uint else ''
        L = len(bits)
        if L <= min_len:
            bits = '0'*(min_len-L) + bits
        elif imay_max_len != -1:
            max_len = imay_max_len
            if L > max_len:
                bits = bits[L-max_len:]
        return [int(bit=='1') for bit in bits]

    test_data = (
        (min_len, imay_max_len, uint, ans)
        for min_len in range(6)
        for imay_max_len  in range(6)
        if imay_max_len==-1 or min_len<=imay_max_len
        for uint in range(2**12+4)
        for ans in [mk_ans__radix2__big(min_len, imay_max_len, uint)]
        )
    #_loop4test_uint2radix_repr(sf, test_data)
    _loop4test_uint2radix_repr(radix, test_data)
    ######################
    ######################
    ######################
def _loop4test_uint2radix_repr(radix, test_data, /):
#def _loop4test_uint2radix_repr(sf, test_data, /):
    #radix = sf.get_radix()
    radix = _Int(radix)
    sf = _Uint2RadixRepr(radix)
    for min_len, imay_max_len, uint, ans in test_data:
        uint = _Int(uint)
        ans = [*map(_Int, ans)]
        ######################
        ######################
        result = [*sf.uint2radix_repr__big_endian__split(uint, min_len=min_len, imay_max_len=imay_max_len)]
        _print4test_uint2radix_repr(method_name='uint2radix_repr__big_endian__split', min_len=min_len, imay_max_len=imay_max_len, uint=uint, ans=ans, result=result)
        ######################
        ######################
        result = [*uint2radix_repr(sf, uint, min_len=min_len, imay_max_len=imay_max_len, is_big_endian=True, _split_ver=1, input_is_an_IUint2RadixRepr_not_radix=True)]
        _print4test_uint2radix_repr(method_name='uint2radix_repr:big_endian:split', min_len=min_len, imay_max_len=imay_max_len, uint=uint, ans=ans, result=result)

    #for min_len, imay_max_len, uint, ans in test_data:
        [*ans] = reversed(ans)
        ######################
        ######################
        result = [*sf.uint2radix_repr__little_endian__split(uint, min_len=min_len, imay_max_len=imay_max_len)]
        _print4test_uint2radix_repr(method_name='uint2radix_repr__little_endian__split', min_len=min_len, imay_max_len=imay_max_len, uint=uint, ans=ans, result=result)
        ######################
        ######################

        result = [*uint2radix_repr(sf, uint, min_len=min_len, imay_max_len=imay_max_len, is_big_endian=False, _split_ver=1, input_is_an_IUint2RadixRepr_not_radix=True)]
        _print4test_uint2radix_repr(method_name='uint2radix_repr:little_endian:split', min_len=min_len, imay_max_len=imay_max_len, uint=uint, ans=ans, result=result)
        ######################
        ######################

        result = [*sf.uint2radix_repr__little_endian__plain(uint, min_len=min_len, imay_max_len=imay_max_len)]
        _print4test_uint2radix_repr(method_name='uint2radix_repr__little_endian__plain', min_len=min_len, imay_max_len=imay_max_len, uint=uint, ans=ans, result=result)
        ######################
        ######################

        result = [*uint2radix_repr(sf, uint, min_len=min_len, imay_max_len=imay_max_len, is_big_endian=False, _split_ver=0, input_is_an_IUint2RadixRepr_not_radix=True)]
        _print4test_uint2radix_repr(method_name='uint2radix_repr:little_endian:plain', min_len=min_len, imay_max_len=imay_max_len, uint=uint, ans=ans, result=result)
        ######################
        ######################
def _print4test_uint2radix_repr(*, method_name, min_len, imay_max_len, uint, ans, result):
    if 1:
        try:
            assert ans == result
        except AssertionError:
            print(f'method_name={method_name}')
            print(f'min_len={min_len}')
            print(f'imay_max_len={imay_max_len}')
            print(f'uint={uint}')
            print(f'ans={ans}')
            print(f'result={result}')
            #print(f'x={x}')
            raise
if __name__ == '__main__':
    _t2()
    pass



#]]]"""


