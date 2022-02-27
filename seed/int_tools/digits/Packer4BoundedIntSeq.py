

#r"""[[[

r'''
py -m seed.int_tools.digits.Packer4BoundedIntSeq
from seed.int_tools.digits.Packer4BoundedIntSeq import pack_from_bounded_int_seq, Packer4BoundedIntSeq, Packer4BoundedIntSeq__little_endian, Packer4BoundedIntSeq__big_endian

e ../../python3_src/seed/int_tools/digits/Packer4BoundedIntSeq.py





#'''



_doc_test4big_endian = r'''[[[

#################################
>>> from seed.int_tools.digits.Packer4BoundedIntSeq import pack_from_bounded_int_seq, Packer4BoundedIntSeq, Packer4BoundedIntSeq__little_endian, Packer4BoundedIntSeq__big_endian


#################################
#################################
>>> pack_from_bounded_int_seq([1,5,7,3], int_lower_bound=0, int_upper_bound=9, is_big_endian=True)
Packer4BoundedIntSeq__big_endian(4, 1573, int_lower_bound = 0, int_upper_bound = 9)
>>> _.unpack()
(1, 5, 7, 3)
>>> Packer4BoundedIntSeq__big_endian(4, 1573, int_lower_bound = 0, int_upper_bound = 9).unpack()
(1, 5, 7, 3)



#################################
>>> pack_from_bounded_int_seq([0,0,0,1,5,7,3,0,0], int_lower_bound=0, int_upper_bound=9, is_big_endian=True)
Packer4BoundedIntSeq__big_endian(9, 157300, int_lower_bound = 0, int_upper_bound = 9)
>>> _.unpack()
(0, 0, 0, 1, 5, 7, 3, 0, 0)
>>> Packer4BoundedIntSeq__big_endian(9, 157300, int_lower_bound = 0, int_upper_bound = 9).unpack()
(0, 0, 0, 1, 5, 7, 3, 0, 0)



#################################
>>> pack_from_bounded_int_seq([-8,-8,-8,-7,-3,-1,-5,-8,-8], int_lower_bound=-8, int_upper_bound=1, is_big_endian=True)
Packer4BoundedIntSeq__big_endian(9, 157300, int_lower_bound = -8, int_upper_bound = 1)
>>> _.unpack()
(-8, -8, -8, -7, -3, -1, -5, -8, -8)
>>> Packer4BoundedIntSeq__big_endian(9, 157300, int_lower_bound = -8, int_upper_bound = 1).unpack()
(-8, -8, -8, -7, -3, -1, -5, -8, -8)


#################################
#################################
#################################
>>> pack_from_bounded_int_seq([], int_lower_bound=0, int_upper_bound=0, is_big_endian=True)
Packer4BoundedIntSeq__big_endian(0, 0, int_lower_bound = 0, int_upper_bound = 0)
>>> _.unpack()
()
>>> Packer4BoundedIntSeq__big_endian(0, 0, int_lower_bound = 0, int_upper_bound = 0).unpack()
()


>>> pack_from_bounded_int_seq([0], int_lower_bound=0, int_upper_bound=0, is_big_endian=True)
Packer4BoundedIntSeq__big_endian(1, 0, int_lower_bound = 0, int_upper_bound = 0)
>>> _.unpack()
(0,)
>>> Packer4BoundedIntSeq__big_endian(1, 0, int_lower_bound = 0, int_upper_bound = 0).unpack()
(0,)


>>> pack_from_bounded_int_seq([0,0], int_lower_bound=0, int_upper_bound=0, is_big_endian=True)
Packer4BoundedIntSeq__big_endian(2, 0, int_lower_bound = 0, int_upper_bound = 0)
>>> _.unpack()
(0, 0)
>>> Packer4BoundedIntSeq__big_endian(2, 0, int_lower_bound = 0, int_upper_bound = 0).unpack()
(0, 0)


#################################
>>> pack_from_bounded_int_seq([], int_lower_bound=-99, int_upper_bound=-99, is_big_endian=True)
Packer4BoundedIntSeq__big_endian(0, 0, int_lower_bound = -99, int_upper_bound = -99)
>>> _.unpack()
()
>>> Packer4BoundedIntSeq__big_endian(0, 0, int_lower_bound = -99, int_upper_bound = -99).unpack()
()


>>> pack_from_bounded_int_seq([-99], int_lower_bound=-99, int_upper_bound=-99, is_big_endian=True)
Packer4BoundedIntSeq__big_endian(1, 0, int_lower_bound = -99, int_upper_bound = -99)
>>> _.unpack()
(-99,)
>>> Packer4BoundedIntSeq__big_endian(1, 0, int_lower_bound = -99, int_upper_bound = -99).unpack()
(-99,)


>>> pack_from_bounded_int_seq([-99,-99], int_lower_bound=-99, int_upper_bound=-99, is_big_endian=True)
Packer4BoundedIntSeq__big_endian(2, 0, int_lower_bound = -99, int_upper_bound = -99)
>>> _.unpack()
(-99, -99)
>>> Packer4BoundedIntSeq__big_endian(2, 0, int_lower_bound = -99, int_upper_bound = -99).unpack()
(-99, -99)




#]]]'''
_doc_test4little_endian = (
        _doc_test4big_endian
        .replace('Packer4BoundedIntSeq__big_endian', 'Packer4BoundedIntSeq__little_endian')
        .replace('True', 'False')
        .replace('157300,', '3751000,')
        .replace('1573,', '3751,')
        )
__doc__ += _doc_test4big_endian
__doc__ += _doc_test4little_endian
if 0:
    from seed.tiny import print_err
    print_err(__doc__)

__all__ = '''
    pack_from_bounded_int_seq

    Packer4BoundedIntSeq
    Packer4BoundedIntSeq__little_endian
    Packer4BoundedIntSeq__big_endian
    '''.split()


from seed.int_tools.digits.ConvertBoundedIntSeqToUIntWithLen import ConvertBoundedIntSeqToUIntWithLen
from seed.helper.check.checkers import check_uint, check_int, check_bool
from seed.helper.repr_input import repr_helper_ex



def pack_from_bounded_int_seq(bounded_int_seq, /,*, int_lower_bound, int_upper_bound, is_big_endian, _may_merge_ver=None):
    cls = Packer4BoundedIntSeq__big_endian if is_big_endian else Packer4BoundedIntSeq__little_endian
    sf = cls.pack(bounded_int_seq, int_lower_bound=int_lower_bound, int_upper_bound=int_upper_bound, is_big_endian=is_big_endian, _may_merge_ver=_may_merge_ver)
    return sf


class Packer4BoundedIntSeq:
    (*_ordered_attrs4repr,) = 'int_lower_bound int_upper_bound is_big_endian'.split()
    @classmethod
    def pack(cls, bounded_int_seq, /,*, int_lower_bound, int_upper_bound, is_big_endian, _may_merge_ver=None):
        (len_, uint) = ConvertBoundedIntSeqToUIntWithLen(int_lower_bound=int_lower_bound, int_upper_bound=int_upper_bound, is_big_endian=is_big_endian).convert_bounded_int_seq_to_uint_with_len(bounded_int_seq, _may_merge_ver=_may_merge_ver)
        return cls(len_, uint, int_lower_bound=int_lower_bound, int_upper_bound=int_upper_bound, is_big_endian=is_big_endian)
    ###
    def __init__(sf, len_, uint, /,*, int_lower_bound, int_upper_bound, is_big_endian):
        check_int(int_lower_bound)
        check_int(int_upper_bound, min=int_lower_bound)
        check_bool(is_big_endian)
        #check_int(_split_ver, min=0, max=1)
        check_uint(len_)
        check_uint(uint)

        sf.len_ = len_
        sf.uint = uint
        sf._a_ConvertBoundedIntSeqToUIntWithLen = ConvertBoundedIntSeqToUIntWithLen(int_lower_bound=int_lower_bound, int_upper_bound=int_upper_bound, is_big_endian=is_big_endian)
    def unpack(sf, /,*, _may_split_ver=None):
        bounded_int_seq = sf._a_ConvertBoundedIntSeqToUIntWithLen.convert_bounded_int_seq_from_uint_with_len(sf.len_, sf.uint, _may_split_ver=_may_split_ver)
        return bounded_int_seq
    def __repr__(sf, /):
        return repr_helper_ex(sf
                    , (sf.len_, sf.uint)
                    , sf._ordered_attrs4repr
                    , {}
                    , ordered_attrs_only=True
                    )

    @property
    def int_lower_bound(sf, /):
        return sf._a_ConvertBoundedIntSeqToUIntWithLen.int_lower_bound
    @property
    def int_upper_bound(sf, /):
        return sf._a_ConvertBoundedIntSeqToUIntWithLen.int_upper_bound
    @property
    def is_big_endian(sf, /):
        return sf._a_ConvertBoundedIntSeqToUIntWithLen.is_big_endian

class Packer4BoundedIntSeq__little_endian(Packer4BoundedIntSeq):
    (*_ordered_attrs4repr,) = 'int_lower_bound int_upper_bound'.split()
    is_big_endian = False
    @classmethod
    def pack(cls, bounded_int_seq, /,*, int_lower_bound, int_upper_bound, is_big_endian=is_big_endian, _may_merge_ver=None):
        if is_big_endian is not cls.is_big_endian: raise TypeError
        return super().pack(bounded_int_seq, int_lower_bound=int_lower_bound, int_upper_bound=int_upper_bound, is_big_endian=is_big_endian, _may_merge_ver=_may_merge_ver)
    def __init__(sf, len_, uint, /,*, int_lower_bound, int_upper_bound, is_big_endian=is_big_endian):
        if is_big_endian is not type(sf).is_big_endian: raise TypeError
        super().__init__(len_, uint, int_lower_bound=int_lower_bound, int_upper_bound=int_upper_bound, is_big_endian=is_big_endian)
class Packer4BoundedIntSeq__big_endian(Packer4BoundedIntSeq):
    (*_ordered_attrs4repr,) = 'int_lower_bound int_upper_bound'.split()
    is_big_endian = True
    @classmethod
    def pack(cls, bounded_int_seq, /,*, int_lower_bound, int_upper_bound, is_big_endian=is_big_endian, _may_merge_ver=None):
        if is_big_endian is not cls.is_big_endian: raise TypeError
        return super().pack(bounded_int_seq, int_lower_bound=int_lower_bound, int_upper_bound=int_upper_bound, is_big_endian=is_big_endian, _may_merge_ver=_may_merge_ver)
    def __init__(sf, len_, uint, /,*, int_lower_bound, int_upper_bound, is_big_endian=is_big_endian):
        if is_big_endian is not type(sf).is_big_endian: raise TypeError
        super().__init__(len_, uint, int_lower_bound=int_lower_bound, int_upper_bound=int_upper_bound, is_big_endian=is_big_endian)

def _t4():
    pass
if __name__ == '__main__':
    _t4()
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


#]]]"""

