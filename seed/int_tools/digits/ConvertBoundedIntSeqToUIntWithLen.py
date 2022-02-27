
#r"""[[[

r'''
py -m seed.int_tools.digits.ConvertBoundedIntSeqToUIntWithLen
from seed.int_tools.digits.ConvertBoundedIntSeqToUIntWithLen import ConvertBoundedIntSeqToUIntWithLen

e ../../python3_src/seed/int_tools/digits/ConvertBoundedIntSeqToUIntWithLen.py
#'''
__all__ = '''
    ConvertBoundedIntSeqToUIntWithLen
    '''.split()


from seed.int_tools.digits.uint2radix_repr import uint2radix_repr
from seed.int_tools.digits.radix_repr2uint import radix_repr2uint

from seed.helper.check.checkers import check_uint, check_int, check_bool
import itertools


class ConvertBoundedIntSeqToUIntWithLen:
    def __init__(sf, /,*, int_lower_bound, int_upper_bound, is_big_endian, _merge_ver=1, _split_ver=1):
        check_int(int_lower_bound)
        check_int(int_upper_bound, min=int_lower_bound)
        check_bool(is_big_endian)
        check_int(_merge_ver, min=0, max=2)
        check_int(_split_ver, min=0, max=1)

        one_or_radix = int_upper_bound+1-int_lower_bound
        if not one_or_radix >= 1: raise ValueError('not int_upper_bound+1-int_lower_bound >= 1')
        sf.int_lower_bound = int_lower_bound
        sf.int_upper_bound = int_upper_bound
        sf.one_or_radix = one_or_radix
        sf.is_big_endian = is_big_endian
        sf._merge_ver = _merge_ver
        sf._split_ver = _split_ver
    def mk_bounded_int_seq_from_iterable(sf, ints, /):
        return (*ints,)
    def convert_bounded_int_seq_from_uint_with_len(sf, len_, uint, /,*, _may_split_ver=None):
        bounded_int_seq = sf._convert_bounded_int_seq_from_uint_with_len(len_, uint, _may_split_ver=_may_split_ver)
        if __debug__:
            assert (len_, uint) == sf._convert_bounded_int_seq_to_uint_with_len(bounded_int_seq, _may_merge_ver=None)
        return bounded_int_seq
    def _convert_bounded_int_seq_from_uint_with_len(sf, len_, uint, /,*, _may_split_ver):
        check_uint(len_)
        check_uint(uint)
        if sf.one_or_radix==1:
            if not uint == 0: raise ValueError
            bounded_int_seq = sf.mk_bounded_int_seq_from_iterable(itertools.repeat(sf.int_lower_bound, len_))
        else:
            radix = sf.one_or_radix
            if _may_split_ver is None:
                _split_ver = sf._split_ver
            else:
                _split_ver = _may_split_ver
                check_int(_split_ver, min=0, max=1)
            _split_ver
            iter_digits = uint2radix_repr(radix, uint, is_big_endian=sf.is_big_endian, _split_ver=_split_ver, min_len=len_, imay_max_len=len_+1)
            bounded_int_seq = sf.mk_bounded_int_seq_from_iterable(sf.int_lower_bound+digit for digit in iter_digits)
            #if 0b1:print(len(bounded_int_seq), len_)
            if len(bounded_int_seq) != len_: raise ValueError
        assert  len(bounded_int_seq) == len_
        return bounded_int_seq
    def convert_bounded_int_seq_to_uint_with_len(sf, bounded_int_seq, /,*, _may_merge_ver=None):
        len(bounded_int_seq)
        (len_, uint) = sf._convert_bounded_int_seq_to_uint_with_len(bounded_int_seq, _may_merge_ver=_may_merge_ver)
        if __debug__:
            if 0b00:
                print((len_, uint), bounded_int_seq)
                print(sf.mk_bounded_int_seq_from_iterable(bounded_int_seq))
                print(sf._convert_bounded_int_seq_from_uint_with_len(len_, uint, _may_split_ver=None))
            assert sf.mk_bounded_int_seq_from_iterable(bounded_int_seq) == sf._convert_bounded_int_seq_from_uint_with_len(len_, uint, _may_split_ver=None)
        return (len_, uint)
    def _convert_bounded_int_seq_to_uint_with_len(sf, bounded_int_seq, /,*, _may_merge_ver):
        len_ = len(bounded_int_seq)
        if not all(type(i) is int for i in bounded_int_seq):raise TypeError
        if not all(sf.int_lower_bound <= i <= sf.int_upper_bound for i in bounded_int_seq):raise ValueError
        if sf.one_or_radix==1:
            #uint = len_
            uint = 0
        else:
            radix = sf.one_or_radix
            if _may_merge_ver is None:
                _merge_ver = sf._merge_ver
            else:
                _merge_ver = _may_merge_ver
                check_int(_merge_ver, min=0, max=2)
            _merge_ver
            digits = (i-sf.int_lower_bound for i in bounded_int_seq)
            uint = radix_repr2uint(radix, digits, is_big_endian=sf.is_big_endian, _merge_ver=_merge_ver)
        return len_, uint

def _t3_xxx():
    radix = 2
    len_ = 5
    uint = 16
    is_big_endian = True
    if 1:
            iter_digits = uint2radix_repr(radix, uint, is_big_endian=is_big_endian, _split_ver=1, min_len=len_, imay_max_len=len_+1)
    [*digits] = iter_digits
    #print(digits)
    assert len(digits) == len_
_t3_xxx()

def _t3():
    from seed.debug.assert_eq import assert_eq, assert_eq_f, mk_assert_eq_f
    def f(radix):
        if radix==1:
            uint = 0
            for len_ in range(15):
                yield len_, uint
        else:
            L = 1000
            for len_ in range(15):
                end = radix**len_
                for uint in range(max(0,end-L), end):
                    yield len_, uint
                for uint in range(min(L, end)):
                    yield len_, uint
    for radix in range(1, 11):
        for int_lower_bound in range(-3,4):
            int_upper_bound = int_lower_bound + radix-1
            for is_big_endian in (True, False):
                sf = ConvertBoundedIntSeqToUIntWithLen(int_lower_bound=int_lower_bound, int_upper_bound=int_upper_bound, is_big_endian=is_big_endian)
                for len_, uint in f(radix):
                    #if 0b1:print(radix, len_, uint)
                    try:
                        us = sf.convert_bounded_int_seq_from_uint_with_len(len_, uint)
                    except:
                        print(locals())
                        raise
                    #if 0b1:print(radix, len_, uint, us)
                    #assert (len_, uint) == sf.convert_bounded_int_seq_to_uint_with_len(us)
                    mk_assert_eq_f(radix=radix, int_lower_bound=int_lower_bound, int_upper_bound=int_upper_bound, is_big_endian=is_big_endian, len_=len_, uint=uint)((len_, uint), sf.convert_bounded_int_seq_to_uint_with_len, us)
if __name__ == '__main__':
    _t3()
    pass
#]]]"""

