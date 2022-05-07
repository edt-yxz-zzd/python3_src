r'''
see:
    view others/数学/编程/TODO_list/周期长度为二的对称加密.txt

py -m nn_ns.app.crypt.UnitSqrtCipher.unit_sqrt_cipher
py -m nn_ns.app.debug_cmd   nn_ns.app.crypt.UnitSqrtCipher.unit_sqrt_cipher

e ../../python3_src/nn_ns/app/crypt/UnitSqrtCipher/unit_sqrt_cipher.py

from nn_ns.app.crypt.UnitSqrtCipher.unit_sqrt_cipher import ...

TODO:
    pack old2new+new2old
    cache Cipher_mod__permutation_partition.tmp_slots offset

[[DONE:mv to nn_ns
py script/unit_sqrt_cipher.py
e script/unit_sqrt_cipher.py
!mkdir ../../python3_src/nn_ns/app/crypt/UnitSqrtCipher/
!mv script/unit_sqrt_cipher.py ../../python3_src/nn_ns/app/crypt/UnitSqrtCipher/
e ../../python3_src/nn_ns/app/crypt/UnitSqrtCipher/unit_sqrt_cipher.py
]]

#'''

from seed.abc.abc__ver0 import override
from seed.seq_tools.inverse_uint_bijection_array import inverse_uint_bijection_array
from seed.seq_tools.is_inverse_uint_bijection_array_of import is_inverse_uint_bijection_array_of
from seed.math.floor_ceil import floor_log2
from seed.helper.repr_input import repr_helper
from seed.func_tools.fmapT.filterT__tiny import filterT__dict
#from seed.func_tools.fmapT.fmapT__tiny import fmapT__tuple
from seed.func_tools.fmapT.predT__tiny import predT__tuple, pred__True, predT__NOT, type_isT, dot, predT__AND, is_str#, is_char
from seed.func_tools.fmapT.checkT__tiny import check_uint, check_int, check_str, check_char, check_uint, checkT__pattern_list, checkT__type_is, check_tuple, check_callable, checkT__type_le, checkT__issubclass__any, checkT__issubclass__all, checkT__eq, checkT__AND
from nn_ns.math_nn.integer.mod import invmod
#from seed.tiny_.check import check_str, check_char, check_uint, check_type_is
from seed.tiny_.check import check_uint_lt#, check_int_ge_lt, check_int_ge, check_int_ge_le
#from seed.tiny_.verify import type_is, is_str, is_char
from seed.tiny import mk_tuple

from seed.seq_tools.seq_as_mapping import SeqAsMapping
from seed.seq_tools.seq_as_mapping import pseudo_seq2idc, pseudo_seq2iter_idc, pseudo_seq2iter_values, pseudo_seq2iter_items, pseudo_seq__enumerate
from seed.seq_tools.seq_as_mapping import pseudo_seq2idc_, pseudo_seq2iter_idc_, pseudo_seq2iter_values_, pseudo_seq2iter_items_, pseudo_seq__enumerate_
from seed.seq_tools.seq_as_mapping import pseudo_seq__get, mk_subseq5slice_range__tuple
from seed.mapping_tools.mapping_as_seq import MappingAsSeq
from seed.data_funcs.rngs import len_of__rng, len_of__rng__neg_as0
from seed.data_funcs.rngs import check_input4isomorphism_mapping__RangeBased, isomorphism_mapping__RangeBased
from seed.data_funcs.rngs import make_Ranges, sorted_ints_to_iter_nontouch_ranges, detect_iter_ranges, StackStyleSimpleIntSet, StackStyleSimpleIntMapping, TouchRangeBasedIntMapping
from seed.data_funcs.rngs import NonTouchRanges, TouchRanges, make_NonTouchRanges, make_TouchRanges, ranges5char_pairs__str
from seed.data_funcs.rngs import len_of__rng, len_of__rng__neg_as0

from nn_ns.Bijection.BijectiveNumeration import bidigits2uint__little_endian, uint2bidigits__little_endian

from seed.int_tools.digits.uint2radix_repr import uint2radix_repr
from seed.int_tools.digits.radix_repr2uint import radix_repr2uint
#def radix_repr2uint(radix_or_an_IRadixRepr2Uint, digits, /,*, is_big_endian:bool, _merge_ver:'0|1|2'=0, input_is_an_IRadixRepr2Uint_not_radix=False):
#def uint2radix_repr(radix_or_an_IUint2RadixRepr, uint, /,*, is_big_endian:bool, _split_ver:'0|1'=1, min_len=0, imay_max_len=-1, input_is_an_IUint2RadixRepr_not_radix=False):


from seed.seq_tools.bisearch import bisearch





from abc import ABC, abstractmethod
from math import factorial, comb as C
    #math.comb(n, k) n! / (k! * (n - k)!)
from random import randrange, getrandbits
from random import Random
from secrets import randbelow, randbits
from itertools import accumulate, chain
import operator


#bug:check_uint_tuple = dot[checkT__pattern_list(check_uint), check_tuple]
check_uint_tuple = checkT__AND(check_tuple, checkT__pattern_list(check_uint))

def perform_permutation__inv__uint8bits(new2old, len_bits, u, /):
    bs = uint2bits(len_bits, u)
    bs = ''.join(iter_perform_permutation__inv(new2old, bs))
    v = int(bs, 2)
    return v
def uint2bits(len_bits, u, /):
    bs = f'{u:b}'
    dL = len_bits - len(bs)
    bs = '0'*dL + bs
    return bs
def iter_perform_permutation__inv(new2old, ls, /):
    return (ls[old_idx] for old_idx in new2old)
if 0:
    r'''
    def mk_permutation(sz, mk_random_mod, /):
    M = factorial(sz)
    m = mk_random_mod(M)
    us = [*range(sz)]
    def swap(i, /):
        us[i], us[L-1] = us[L-1], us[i]
    L = len(us)
    while L:
        m, i = divmod(m, L)
        swap(i)
        L -= 1
    assert m == 0
    assert i == 0
    assert {*us} == {*range(sz)}
    permutation = (*us,)
    return permutation
    #'''
def mk_permutation(sz, mk_random_mod, /):
    us = [*range(sz)]
    def swap(i, /):
        us[i], us[L-1] = us[L-1], us[i]
    L = len(us)
    while L:
        i = mk_random_mod(L)
        swap(i)
        L -= 1
    assert i == 0
    assert {*us} == {*range(sz)}
    permutation = (*us,)
    return permutation



class IEase_repr(ABC):
#class ICipher__easy_repr(ICipher):
    def __repr__(sf, /):
        kwargs = _filter4kw(sf.__dict__)

        return repr_helper(sf, **kwargs)

    def __new__(cls, /, **kwargs):
        sf = super(__class__, cls).__new__(cls)
        sf.__dict__.update(**kwargs)
        return sf


    #%s/def mk(/def _mk_kwargs4init_(/g
    #%s/        '-> sf'/        '-> __init__.kwargs'
    #%s/return cls(/return dict(

        #))))
    @classmethod
    def mk(cls, /, *args, **kwargs):
        '-> sf'
        return cls(**cls.mk_kwargs4init(*args, **kwargs))
    @classmethod
    @abstractmethod
    def _mk_kwargs4init_(cls, /, *args, **kwargs):
        '-> __init__.kwargs'
        raise NotImplementedError
    @classmethod
    def mk_kwargs4init(cls, /, *args, **kwargs):
        #bug:return {**cls._mk_kwargs4init_(*args, **kwargs)}
        return dict(**cls._mk_kwargs4init_(*args, **kwargs))
        r'''
    @classmethod
    def mk_kwargs4init(cls, /, *args, **kwargs):
        bounded_mk = cls.mk
        checkT__type_is(MethodType)(bounded_mk)
        mk = bounded_mk.__func__
        #checkT__type_is(classmethod)(mk)
        cls = dict
        return mk(dict, *args, **kwargs)
        #'''
class IEase_repr_init(IEase_repr):
#class ICipher__easy_init(IEase_repr):
    #def __init__(sf, /, *, key):
    @classmethod
    @override
    def _mk_kwargs4init_(cls, /, **kwargs):
        '-> __init__.kwargs'
        return dict(**kwargs)


r'''
class ICipher__easy_init(ICipher):
    #def __init__(sf, prefix4key, /, **kwargs):
    def __new__(cls, /, *, charset4clear_text, charset4cipher_text, prefix4key **kwargs):
        super(cls, __class__).__new__(cls)
        #sf.prefix4key = prefix4key
        sf.__dict__.update(charset4clear_text=charset4clear_text, charset4cipher_text=charset4cipher_text, prefix4key=prefix4key, **kwargs)
        return sf
#'''


class IOrderedCharset(ABC):
    @abstractmethod
    def __len__(sf, /):
        '-> sz'
    @abstractmethod
    def _char2idx_(sf, char, /):
        'char -> idx|raise LookupError'
    @abstractmethod
    def _idx2char_(sf, idx, /):
        'idx -> char'

    def char2idx(sf, char, /):
        'char -> idx|raise LookupError'
        check_char(char)
        idx = sf._char2idx_(char)
        sf.check_idx(idx)
        return idx
    def _contains__char_(sf, char, /):
        try:
            sf.char2idx(char)
        except LookupError:
            return False
        return True

    def idx2char(sf, idx, /):
        'idx -> idx|raise IndexError'
        sf.check_idx(idx)
        char = sf._idx2char_(idx)
        check_char(char)
        return char
    def check_idx(sf, idx, /):
        #check_uint_lt(len(sf), idx)
        check_uint(idx)
        if not idx < len(sf): raise IndexError(idx)#TypeError
    def contains__idx(sf, idx, /):
        check_uint(idx)
        return idx < len(sf)
    def contains__char(sf, char, /):
        return sf._contains__char_(char)
    def iter_chars2iter_idc(sf, iter_chars, /):
        return map(sf.char2idx, iter_chars)
    def iter_chars5iter_idc(sf, iter_idc, /):
        return map(sf.idx2char, iter_idc)
    def __iter__(sf, /):
        return sf.iter_chars5iter_idc(range(len(sf)))

    def str2iter_idc(sf, s, /):
        return sf.iter_chars2iter_idc(s)
    def str5iter_idc(sf, iter_idc, /):
        return ''.join(sf.iter_chars5iter_idc(iter_idc))

    def str2uint_with_len__via_digits__big_endian(sf, s, /, *, validate):
        'modulo = radix**L; used in modulo arithmetic; not used in conversion between diff IOrderedCharset'
        radix = len(sf)
        L = len(s)
        [*digits] = sf.str2iter_idc(s)
        u = radix_repr2uint(radix, digits, is_big_endian=True)
        uint_with_len = u, L

        if validate:
            if not s == sf.str5uint_with_len__via_digits__big_endian(uint_with_len, validate=False):raise logic-err
        return uint_with_len

    def str5uint_with_len__via_digits__big_endian(sf, uint_with_len, /, *, validate):
        'modulo = radix**L; used in modulo arithmetic; not used in conversion between diff IOrderedCharset'
        radix = len(sf)
        u, L = uint_with_len
        [*digits] = uint2radix_repr(radix, u, is_big_endian=True, min_len=L, imay_max_len=L+1)
        if len(digits) > L: raise TypeError('overflow')
        if not len(digits) == L: raise logic-err

        s = sf.str5iter_idc(digits)
        assert L == len(s)

        if validate:
            if not (u, L) == sf.str2uint_with_len__via_digits__big_endian(s, validate=False):raise logic-err
        return s


    def convert_to(src_IOrderedCharset, dst_IOrderedCharset, src_str, /, *, validate):
        u = src_IOrderedCharset.str2uint__via_bidigits__little_endian(src_str)
        dst_str = dst_IOrderedCharset.str5uint__via_bidigits__little_endian(u)
        if validate:
            if not dst_IOrderedCharset.convert_to(src_IOrderedCharset, dst_str, validate=False):raise logic-err
        return dst_str

    def str2uint__via_bidigits__little_endian(sf, s, /, *, validate):
        'used in conversion between diff IOrderedCharset; not used in modulo arithmetic'
        radix = len(sf)
        [*bidigits] = sf.str2iter_idc(s)
        u = bidigits2uint__little_endian(radix, bidigits)
        if validate:
            if not s == sf.str5uint__via_bidigits__little_endian(u, validate=False):raise logic-err
        return u
    def str5uint__via_bidigits__little_endian(sf, u, /, *, validate):
        'used in conversion between diff IOrderedCharset; not used in modulo arithmetic'
        radix = len(sf)
        bidigits = uint2bidigits__little_endian(radix, u)
        #check_tuple(bidigits)
        s = sf.str5iter_idc(bidigits)
        if validate:
            if not u == sf.str2uint__via_bidigits__little_endian(s, validate=False):raise logic-err
        return s
    def __contains__(sf, char_or_idx, /):
        return sf.contains__char_or_idx(char_or_idx)
    def __getitem__(sf, char_or_idx, /):
        return sf.get__char_or_idx(char_or_idx)
    def get__char_or_idx(sf, char_or_idx, /):
        if type(char_or_idx) is str:
            char = char_or_idx
            return sf.char2idx(char)
        else:
            idx = char_or_idx
            return sf.idx2char(idx)

    def contains__char_or_idx(sf, char_or_idx, /):
        if type(char_or_idx) is str:
            char = char_or_idx
            return sf.contains__char(char)
        else:
            idx = char_or_idx
            return sf.contains__idx(idx)



class IOrderedCharset__lookup(IEase_repr, IOrderedCharset):
    def __init__(sf, /, *, _idx2char, _char2idx, _check):
        if not len(_idx2char) == len(_char2idx):raise TypeError
        if not _check: return
        L = len(_idx2char)
        #idcL = pseudo_seq2idc(_idx2char)
        idcL = list(range(L)) #vs idcR
        charsL = set(pseudo_seq2iter_values(_idx2char))
        idcR = sorted(_char2idx.values())
        charsR = set(_char2idx)
        if not len(charsR) == L:raise TypeError

        if not charsR == charsL:raise TypeError
        if not idcR == idcL:raise TypeError
        if not all(_char2idx[char]==idx for idx, char in pseudo_seq__enumerate(_idx2char)):raise TypeError

        checkT__pattern_list(check_char)(charsL)
        checkT__pattern_list(check_char)(charsR)

        checkT__pattern_list(check_uint)(idcL)
        checkT__pattern_list(check_uint)(idcR)


    @override
    def __len__(sf, /):
        '-> sz'
        return len(sf._idx2char)
    @override
    def _char2idx_(sf, char, /):
        'char -> idx|raise LookupError'
        return sf._char2idx[char]
    @override
    def _idx2char_(sf, idx, /):
        'idx -> char'
        return sf._idx2char[idx]

class OrderedCharset__str(IOrderedCharset__lookup):
    @classmethod
    @override
    def _mk_kwargs4init_(cls, str8set, /):
        '-> __init__.kwargs'
        check_str(str8set)
        _idx2char = str8set
        _char2idx = {char:idx for idx, char in enumerate(_idx2char)}
        #print(_char2idx)
        return dict(_idx2char=_idx2char, _char2idx=_char2idx, _check=True)


binary___ordered_charset__str = OrderedCharset__str.mk('01')
hex___ordered_charset__str = OrderedCharset__str.mk('0123456789ABCDEF')

class OrderedCharset__RangeBased(IEase_repr, IOrderedCharset):
    @classmethod
    @override
    def _mk_kwargs4init_(cls, char_pt_rngs, /):
        '-> __init__.kwargs'
        if type(char_pt_rngs) is str:
            char_pairs__str = char_pt_rngs
            char_pt_rngs = ranges5char_pairs__str(char_pairs__str).to_NonTouchRanges()
        else:
            char_pt_rngs = make_NonTouchRanges(char_pt_rngs)

        #bug:lens_rngs = (*map(len, char_pt_rngs.iter_rngs()),)
        lens_rngs = (*map(len_of__rng, char_pt_rngs.iter_rngs()),)
        end_idc = (*accumulate(lens_rngs),)
        begin_idc = (0, *end_idc[:-1])[:len(end_idc)]
        idx_rngs = (*zip(begin_idc, end_idc),)
        idx_rngs = TouchRanges(idx_rngs)
        ######################
        idx_rngs
        char_pt_rngs
        return dict(idx_rngs=idx_rngs, char_pt_rngs=char_pt_rngs, _check=True)

        d = StackStyleSimpleIntMapping()
        d.push_rng_value_pairs(zip(char_pt_rngs.iter_rngs(), begin_idc))

    def __init__(sf, /, *, idx_rngs, char_pt_rngs, _check):
        checkT__type_is(NonTouchRanges)(char_pt_rngs)
        checkT__type_is(TouchRanges)(idx_rngs)
        check_input4isomorphism_mapping__RangeBased(src_ranges=char_pt_rngs, dst_ranges=idx_rngs, dst_ranges__is__idc4seq=True, full_check=_check)

    @override
    def __len__(sf, /):
        '-> sz'
        return sf.idx_rngs.len_ints()
    @override
    def _char2idx_(sf, char, /):
        'char -> idx|raise LookupError'
        ichar = ord(char)
        idx = isomorphism_mapping__RangeBased(LookupError, ichar, sf.char_pt_rngs, sf.idx_rngs)
        return idx
    @override
    def _idx2char_(sf, idx, /):
        'idx -> char'
        ichar = isomorphism_mapping__RangeBased(lambda:logic-err, idx, sf.idx_rngs, sf.char_pt_rngs)
        char = chr(ichar)
        return char
check_input4isomorphism_mapping__RangeBased
isomorphism_mapping__RangeBased
binary___ordered_charset__RangeBased = OrderedCharset__RangeBased.mk('01')
hex___ordered_charset__RangeBased = OrderedCharset__RangeBased.mk('09AF')


























class IHas__modulo(ABC):
    @abstractmethod
    def _get_modulo_(sf, /):
        '-> modulo/uint'
    def get_modulo(sf, /):
        modulo = sf._get_modulo_()
        check_uint(modulo)
        return modulo
class IHas__modulo__bits(IHas__modulo):
    r'''
    modulo =[def]= 2**len_bits
    #'''
    @abstractmethod
    def _get_len_bits_(sf, /):
        '-> len_bits/uint'
    def get_len_bits(sf, /):
        len_bits = sf._get_len_bits_()
        check_uint(len_bits)
        return len_bits
    @override
    def _get_modulo_(sf, /):
        '-> modulo/uint'
        return 1 << sf.get_len_bits()














class IInnerIndexablePartition(ABC):
    r'''
    accumulate sz && permutation eqvcls
    see:Cipher_mod__permutation_partition


    offset4eqvcls<0> =[def]= 0
    offset4eqvcls<idx8eqvcls+1>
        =[def]= offset4eqvcls<idx8eqvcls> + num_elements<idx8eqvcls>
    # offset4eqvcls<num_eqvclss> = total_num_elements
    # idx8eqvcls2offset=(0, *accumulate(idx8eqvcls2num_elements))[:-1]
    #

    #'''

    @abstractmethod
    def _get_num_eqvclss_(sf, /):
        '-> num_eqvclss/uint'
    @abstractmethod
    def _get_num_elements_at_(sf, idx8eqvcls, /):
        '-> num_elements<eqvclss[idx8eqvcls]>/uint'
    @abstractmethod
    def _get_total_num_elements_(sf, /):
        '-> total_num_elements/uint'
        return sf._calc_total_num_elements()
    @abstractmethod
    def _get_offset4eqvcls_at_(sf, idx8eqvcls, /):
        'idx8eqvcls -> offset4eqvcls #offset4eqvcls<idx8eqvcls> := sum num_elements<eqvclss[i]> {i<-[0..idx8eqvcls-1]}'
        return sf._calc_offset4eqvcls_at_ex(idx8eqvcls)

    @abstractmethod
    def _element2idx8eqvcls_idx8inner_(sf, element, /):
        '-> (idx8eqvcls, idx8inner)'
    @abstractmethod
    def _element5idx8eqvcls_idx8inner_(sf, idx8eqvcls, idx8inner, /):
        '-> element'
    def _check_element_(sf, element, /):
        pass



    def get_num_eqvclss(sf, /):
        num_eqvclss = sf._get_num_eqvclss_()
        check_uint(num_eqvclss)
        return num_eqvclss
    def check_idx8eqvcls_ex(sf, idx8eqvcls_ex, /):
        num_eqvclss = sf.get_num_eqvclss()
        check_uint_lt(num_eqvclss+1, idx8eqvcls_ex)
    def check_idx8eqvcls(sf, idx8eqvcls, /):
        num_eqvclss = sf.get_num_eqvclss()
        check_uint_lt(num_eqvclss, idx8eqvcls)

    def get_num_elements_at(sf, idx8eqvcls, /):
        sf.check_idx8eqvcls(idx8eqvcls)
        num_elements = sf._get_num_elements_at_(idx8eqvcls)
        check_uint(num_elements)
        return num_elements
    def get_total_num_elements(sf, /):
        total_num_elements = sf._get_total_num_elements_()
        check_uint(total_num_elements)
        return total_num_elements
    def get_offset4eqvcls_at(sf, idx8eqvcls, /):
        sf.check_idx8eqvcls(idx8eqvcls)
        offset4eqvcls = sf._get_offset4eqvcls_at_(idx8eqvcls)
        check_uint_lt(sf.get_total_num_elements()+1, offset4eqvcls)
        return offset4eqvcls
    def _calc_offset4eqvcls_at_ex(sf, idx8eqvcls_ex, /):
        sf.check_idx8eqvcls_ex(idx8eqvcls_ex)
        return sum(map(sf.get_num_elements_at, range(idx8eqvcls_ex)), start=0)
    def _calc_total_num_elements(sf, /):
        num_eqvclss = sf.get_num_eqvclss()
        idx8eqvcls_ex = num_eqvclss
        total_num_elements = sf._calc_offset4eqvcls_at_ex(idx8eqvcls_ex)
        return total_num_elements
    def verify_total_num_elements(sf, /):
        if not sf.get_total_num_elements() == sf._calc_total_num_elements():raise logic-err
    def verify_all_offset4eqvcls(sf, /):
        num_eqvclss = sf.get_num_eqvclss()
        for idx8eqvcls in range(num_eqvclss):
            if not sf.get_offset4eqvcls_at(idx8eqvcls) == sf._calc_offset4eqvcls_at_ex(idx8eqvcls):raise logic-err





    def check_element(sf, element, /):
        sf._check_element_(element)
    def check_idx8eqvcls_idx8inner(sf, idx8eqvcls, idx8inner, /):
        num_elements = sf.get_num_elements_at(idx8eqvcls)
        check_uint_lt(num_elements, idx8inner)



    def element2idx8eqvcls_idx8inner(sf, element, /, *, validate):
        sf.check_element(element)
        (idx8eqvcls, idx8inner) = sf._element2idx8eqvcls_idx8inner_(element)
        sf.check_idx8eqvcls_idx8inner(idx8eqvcls, idx8inner)

        if validate:
            if not element==sf.element5idx8eqvcls_idx8inner(idx8eqvcls, idx8inner, validate=False):raise logic-err
        return (idx8eqvcls, idx8inner)
    def element5idx8eqvcls_idx8inner(sf, idx8eqvcls, idx8inner, /, *, validate):
        sf.check_idx8eqvcls_idx8inner(idx8eqvcls, idx8inner)
        element = sf._element5idx8eqvcls_idx8inner_(idx8eqvcls, idx8inner)
        sf.check_element(element)

        if validate:
            if not (idx8eqvcls, idx8inner)==sf.element2idx8eqvcls_idx8inner(element, validate=False):raise logic-err
        return element

#end-class IInnerIndexablePartition(ABC):




















def count_1s_ex(u, /):
    bs = f'{u:b}'
    num_1s = bs.count('1')
    return bs, num_1s
def count_1s(u, /):
    return bin(u).count('1')


class IInnerIndexablePartition_mod(IHas__modulo, IInnerIndexablePartition):
    r'''
    element :: uint%modulo
    modulo =[def]= total_num_elements

    see:IInnerIndexablePartition_mod
    see:Cipher_mod__permutation_partition
    see:Cipher_bits__permutation
    #'''
    @override
    def _check_element_(sf, element, /):
        super()._check_element_(element)
        modulo = sf.get_modulo()
        check_uint_lt(modulo, element)
    @override
    def _get_modulo_(sf, /):
        '-> modulo/uint'
        total_num_elements = sf.get_total_num_elements()
        modulo = total_num_elements
        return modulo

class IInnerIndexablePartition_mod__lookup_table(IInnerIndexablePartition_mod):
    r'''
    .idx8eqvcls2num_elements
    .idx8eqvcls2offset
    #'''
    @abstractmethod
    def _get_idx8eqvcls2num_elements_(sf, /):
        '-> idx8eqvcls2num_elements'
    @abstractmethod
    def _get_idx8eqvcls2offset_(sf, /):
        '-> idx8eqvcls2offset'
    def get_idx8eqvcls2num_elements(sf, /):
        return sf._get_idx8eqvcls2num_elements_()
    def get_idx8eqvcls2offset(sf, /):
        return sf._get_idx8eqvcls2offset_()

    @override
    def _get_total_num_elements_(sf, /):
        '-> total_num_elements/uint'
        idx8eqvcls2num_elements = sf.get_idx8eqvcls2num_elements()
        idx8eqvcls2offset = sf.get_idx8eqvcls2offset()
        if idx8eqvcls2num_elements:
            last_sz = idx8eqvcls2num_elements[-1]
            last_offset = idx8eqvcls2offset[-1]
            total_num_elements = last_offset + last_sz
        else:
            total_num_elements = 0
        return total_num_elements

    @override
    def _get_num_eqvclss_(sf, /):
        '-> num_eqvclss/uint'
        idx8eqvcls2num_elements = sf.get_idx8eqvcls2num_elements()
        return len(idx8eqvcls2num_elements)

    @override
    def _get_num_elements_at_(sf, idx8eqvcls, /):
        '-> num_elements<eqvclss[idx8eqvcls]>/uint'
        idx8eqvcls2num_elements = sf.get_idx8eqvcls2num_elements()
        return idx8eqvcls2num_elements[idx8eqvcls]

    @override
    def _get_offset4eqvcls_at_(sf, idx8eqvcls, /):
        'idx8eqvcls -> offset4eqvcls #offset4eqvcls<idx8eqvcls> := sum num_elements<eqvclss[i]> {i<-[0..idx8eqvcls-1]}'
        idx8eqvcls2offset = sf.get_idx8eqvcls2offset()
        return idx8eqvcls2offset[idx8eqvcls]

class IInnerIndexablePartition_mod__rng8eqvcls(IInnerIndexablePartition_mod__lookup_table):
    r'''
    .origin4rngs #base_point #rng0.begin
    ---
    .idx8eqvcls2num_elements
    .idx8eqvcls2offset
    ===



    rng<idx8eqvcls>.begin =[def]= origin4rngs+offset4eqvcls<idx8eqvcls>
    rng<idx8eqvcls>.end =[def]= rng<idx8eqvcls+1>.begin

    element<idx8eqvcls, idx8inner> =[def]= rng<idx8eqvcls>.begin + idx8inner


    #'''
    @abstractmethod
    def _get_origin4rngs_(sf, /):
        '-> origin4rngs'
    def get_origin4rngs(sf, /):
        origin4rngs = sf._get_origin4rngs_()
        modulo = sf.get_modulo()
        check_uint_lt(modulo, origin4rngs)
        return origin4rngs
    def get_rng_begin_at(sf, idx8eqvcls, /):
        offset4eqvcls = sf.get_offset4eqvcls_at(idx8eqvcls)
        origin4rngs = sf.get_origin4rngs()
        rng_begin = origin4rngs + offset4eqvcls
        modulo = sf.get_modulo()
        rng_begin %= modulo
        return rng_begin

    @override
    def _element2idx8eqvcls_idx8inner_(sf, element, /):
        '-> (idx8eqvcls, idx8inner)'
        modulo = sf.get_modulo()
        origin4rngs = sf.get_origin4rngs()
        shifted_element = (element - origin4rngs)%modulo

        idx8eqvcls2offset = sf.get_idx8eqvcls2offset()
        _, j = bisearch(shifted_element, idx8eqvcls2offset)
        idx8eqvcls = j-1

        offset4eqvcls = idx8eqvcls2offset[idx8eqvcls]
        idx8inner = shifted_element - offset4eqvcls

        num_elements = sf.get_idx8eqvcls2num_elements()
        assert 0 <= idx8inner < num_elements[idx8eqvcls]
        return idx8eqvcls, idx8inner

    @override
    def _element5idx8eqvcls_idx8inner_(sf, idx8eqvcls, idx8inner, /):
        '-> element'
        rng_begin = sf.get_rng_begin_at(idx8eqvcls)
        element = rng_begin + idx8inner

        modulo = sf.get_modulo()
        element %= modulo
        return element


    @staticmethod
    def _mk_tables(origin4rngs, idx8eqvcls2num_elements, /):
        check_uint(origin4rngs)
        check_uint_tuple(idx8eqvcls2num_elements)

        (idx8eqvcls_ex2offset, idx8eqvcls2offset, total_num_elements) = derived5idx8eqvcls2num_elements(idx8eqvcls2num_elements)

        modulo = total_num_elements
        origin4rngs = mod__double_width_(modulo, origin4rngs)
        return {**locals()}
    pass
def mod__double_width_(modulo, u):
    check_uint(modulo)
    if not -modulo <= u <= modulo:
        u %= modulo
        v = u-modulo
        if u > abs(v):
            u = v
    return u



class IInnerIndexablePartition_bits__count_1s(IHas__modulo__bits, IInnerIndexablePartition_mod__lookup_table):
    r'''
    idx8eqvcls =[def]= num_1s
    num_eqvclss =[def]= len_bits+1
    modulo =[def]= 2**len_bits
    #'''
    if 1:
        #!!!conflict!!!
        IHas__modulo__bits._get_modulo_
        IInnerIndexablePartition_mod__lookup_table._get_modulo_
            #IInnerIndexablePartition_mod._get_modulo_

    _get_modulo_ = IHas__modulo__bits._get_modulo_
    _get_total_num_elements_ = IHas__modulo__bits._get_modulo_

    @override
    def _get_num_eqvclss_(sf, /):
        '-> num_eqvclss/uint'
        len_bits = sf.get_len_bits()
        num_eqvclss = len_bits +1
        return num_eqvclss

    @override
    def _get_len_bits_(sf, /):
        '-> len_bits/uint'
        num_eqvclss = IInnerIndexablePartition_mod__lookup_table._get_num_eqvclss_(sf)
        len_bits = num_eqvclss -1

        if 1:
            total_num_elements = IInnerIndexablePartition_mod__lookup_table._get_total_num_elements_(sf)
            if not total_num_elements==1<<len_bits: raise logic-err

        return len_bits
        return sf.get_num_eqvclss()-1
        return sf.len_bits

    r'''
    @override
    def _get_num_elements_at_(sf, idx8eqvcls, /):
        '-> num_elements<eqvclss[idx8eqvcls]>/uint'
        return sf.idx8eqvcls2num_elements[idx8eqvcls]
        num_1s = idx8eqvcls
        len_bits = sf.get_len_bits()
        #!!!slow!!!
        return C(len_bits, num_1s)

    @override
    def _get_offset4eqvcls_at_(sf, idx8eqvcls, /):
        'idx8eqvcls -> offset4eqvcls #offset4eqvcls<idx8eqvcls> := sum num_elements<eqvclss[i]> {i<-[0..idx8eqvcls-1]}'
        return sf.idx8eqvcls2offset[idx8eqvcls]
        #!!!slow!!!
        return super()._get_offset4eqvcls_at_(idx8eqvcls)
        return sf._calc_offset4eqvcls_at_ex(idx8eqvcls)
    #'''

    @override
    def _element2idx8eqvcls_idx8inner_(sf, element, /):
        '-> (idx8eqvcls, idx8inner)'
        if 0:
            #bug:
            r'''
            idx8eqvcls2offset = sf.get_idx8eqvcls2offset()
            (i, j) = bisearch(element, idx8eqvcls2offset)
            idx8eqvcls = j-1

            offset4eqvcls = idx8eqvcls2offset[idx8eqvcls]
            #'''
        u = element
        bs, num_1s = count_1s_ex(u)
        idx8eqvcls = num_1s

        bs = [*reversed(bs)]
        len_bits = len(bs)
        acc = 0
        while num_1s:
            b = bs.pop()
            if not b=='1':continue
            len_bits = len(bs)
                #may: [num_1s==len_bits+1]==>>[weight==0]
            weight = C(len_bits, num_1s)
            num_1s -= 1
            assert 0 <= num_1s <= len_bits

            acc += weight
        idx8inner = acc
            ## '1'*k + '0'*(n-k) ==>> C(n,k)-1 == idx8inner == sum C(n-1-i,k-i) {i<-[0..k-1]}
        return idx8eqvcls, idx8inner




    @override
    def _element5idx8eqvcls_idx8inner_(sf, idx8eqvcls, idx8inner, /):
        '-> element'
        num_1s = idx8eqvcls
        len_bits = sf.get_len_bits()
        bs = ['0']*len_bits

        acc = idx8inner
        while num_1s:
            _, j = bisearch(acc, range(len_bits), key=lambda i:C(i, num_1s))
                # virtual array = [C(i, num_1s) | i<-[0..len_bits-1]]
            i = j-1
            bs[i] = '1'
            weight = C(i, num_1s)
            len_bits = i
            num_1s -= 1
            acc -= weight
        if not acc == 0:raise logic-err
        bs = ''.join(reversed(bs))
        u = int(bs, 2)
        return u


    @staticmethod
    def _mk_tables(len_bits, /):
        check_uint(len_bits)
        num_eqvclss = len_bits+1

        idc8eqvcls = range(num_eqvclss)
        idx8eqvcls2num_elements = tuple(C(len_bits, num_1s) for num_1s in idc8eqvcls)
        (idx8eqvcls_ex2offset, idx8eqvcls2offset, total_num_elements) = derived5idx8eqvcls2num_elements(idx8eqvcls2num_elements)
        if not total_num_elements == 1<<len_bits:raise logic-err

        return {**locals()}
        return (len_bits, num_eqvclss, total_num_elements, idc8eqvcls), (idx8eqvcls2num_elements, idx8eqvcls2offset)


def derived5idx8eqvcls2num_elements(idx8eqvcls2num_elements, /):
    #bug:idx8eqvcls2offset = (*accumulate(idx8eqvcls2num_elements),)
    idx8eqvcls_ex2offset = (0, *accumulate(idx8eqvcls2num_elements),)
    idx8eqvcls2offset = idx8eqvcls_ex2offset[:-1]
    total_num_elements = idx8eqvcls_ex2offset[-1]
    return (idx8eqvcls_ex2offset, idx8eqvcls2offset, total_num_elements)





class InnerIndexablePartition_mod__rng8eqvcls(IEase_repr_init, IInnerIndexablePartition_mod__rng8eqvcls):

    def __init__(sf, /, *, origin4rngs, idx8eqvcls2num_elements):
        check_uint(origin4rngs)
        check_uint_tuple(idx8eqvcls2num_elements)
        d = IInnerIndexablePartition_mod__rng8eqvcls._mk_tables(origin4rngs, idx8eqvcls2num_elements)

        checkT__eq(d['origin4rngs'])(origin4rngs)
        sf._idx8eqvcls2offset = d['idx8eqvcls2offset']

    @override
    def _get_origin4rngs_(sf, /):
        '-> origin4rngs'
        return sf.origin4rngs
    @override
    def _get_idx8eqvcls2num_elements_(sf, /):
        '-> idx8eqvcls2num_elements'
        return sf.idx8eqvcls2num_elements
    @override
    def _get_idx8eqvcls2offset_(sf, /):
        '-> idx8eqvcls2offset'
        return sf._idx8eqvcls2offset

InnerIndexablePartition_mod__rng8eqvcls.mk(origin4rngs=3, idx8eqvcls2num_elements=(3,4,5))




class InnerIndexablePartition_bits__count_1s(IEase_repr_init, IInnerIndexablePartition_bits__count_1s):
    def __init__(sf, /, *, len_bits):
        check_uint(len_bits)
        d = IInnerIndexablePartition_bits__count_1s._mk_tables(len_bits)
        #sf.__dict__.update(d)
        sf._idx8eqvcls2num_elements = d['idx8eqvcls2num_elements']
        sf._idx8eqvcls2offset = d['idx8eqvcls2offset']
        assert len_bits == sf.get_len_bits()

    r'''
    @override
    def _get_len_bits_(sf, /):
        '-> len_bits/uint'
        return sf.len_bits
    #'''

    @override
    def _get_idx8eqvcls2num_elements_(sf, /):
        '-> idx8eqvcls2num_elements'
        return sf._idx8eqvcls2num_elements
    @override
    def _get_idx8eqvcls2offset_(sf, /):
        '-> idx8eqvcls2offset'
        return sf._idx8eqvcls2offset

InnerIndexablePartition_bits__count_1s.mk(len_bits=6)



































class ICipherKeyGenerator(ABC):
    @abstractmethod
    def _get_prefix4key_(sf, /):
        '-> prefix4key/str'
    def get_prefix4key(sf, /):
        return sf._get_prefix4key_()
    @abstractmethod
    def _get_state4key_(sf, /):
        '-> state4key'
    def get_state4key(sf, /):
        return sf._get_state4key_()
    @abstractmethod
    def _get_state4branch_(sf, /):
        '-> state4branch'
    def get_state4branch(sf, /):
        return sf._get_state4branch_()
    @abstractmethod
    def _update_state4key_(sf, /):
        '-> None  # eg. state4key+=1'
    def update_state4key(sf, /):
        state4key = sf.get_state4key()
        sf._update_state4key_()
        if state4key == sf.get_state4key(): raise logic-err
        return
    @abstractmethod
    def _update_state4branch_(sf, /):
        '-> None  # eg. state4branch+=1'
    def update_state4branch(sf, /):
        state4branch = sf.get_state4branch()
        sf._update_state4branch_()
        if state4branch == sf.get_state4branch(): raise logic-err
        return

    @classmethod
    @abstractmethod
    def _make_stated_key_(cls, prefix4key, state4key, /):
        '-> stated_key/str'
    def _make_stated_key(sf, /):
        prefix4key = sf.get_prefix4key()
        state4key = sf.get_state4key()
        return type(sf)._make_stated_key_(prefix4key, state4key)

    def make_next_stated_key(sf, /):
        _1state4key = sf.get_state4key()
        _1stated_key = sf._make_stated_key()
        if not _1state4key == sf.get_state4key(): raise logic-err

        sf.update_state4key()
        _2state4key = sf.get_state4key()
        _2stated_key = sf._make_stated_key()
        if not _2state4key == sf.get_state4key(): raise logic-err



        if _2state4key == _1state4key: raise logic-err
        if _2stated_key == _1stated_key: raise logic-err

        next_stated_key = _2stated_key
        return next_stated_key

    @classmethod
    @abstractmethod
    def _make_new_brach_(cls, state4branch, stated_key, /):
        'state4branch -> stated_key -> ICipherKeyGenerator'
    def make_next_brach(sf, /):
        state4branch = sf.get_state4branch()
        stated_key = sf._make_stated_key()
        new_brach = type(sf)._make_new_brach_(state4branch, stated_key)
        sf.update_state4branch()
        if state4branch == sf.get_state4branch(): raise logic-err

        next_brach = new_brach
        return next_brach

    @classmethod
    @abstractmethod
    def _generate_key__uints_mod_(cls, iter_next_stated_keys, M, num_uints, /):
        'Iter next_stated_key -> M/uint -> num_uints -> [uint%M]{len=num_uints}'
    def generate_next_key__uints_mod(sf, M, num_uints, /):
        'M/uint -> num_uints -> [uint%M]{len=num_uints}'
        def iter_next_stated_keys():
            while 1:
                next_stated_key = sf.make_next_stated_key()
                yield next_stated_key
        iter_next_stated_keys = iter_next_stated_keys()
        return type(sf)._generate_key__uints_mod_(iter_next_stated_keys, M, num_uints)
    def generate_next_key__uint_mod(sf, M, /):
        'M/uint -> uint%M'
        [u] = sf.generate_next_key__uints_mod(M, 1)
        return u
    def generate_next_key__permutation(sf, sz, /):
        'sz/uint -> permutation/[uint%sz]{len=sz}'
        mk_random_mod = sf.generate_next_key__uint_mod
        permutation = mk_permutation(sz, mk_random_mod)
        return permutation
#end-class ICipherKeyGenerator(ABC):

























class ICipher(ABC):
    @abstractmethod
    def _encrypt_(sf, clear_text, /):
        'clear_text -> cipher_text'
    @abstractmethod
    def _decrypt_(sf, cipher_text, /):
        'cipher_text -> clear_text'
    def encrypt(sf, clear_text, /, *, validate):
        cipher_text = sf._encrypt_(clear_text)
        if validate:
            if not clear_text == sf._decrypt_(cipher_text):raise logic-err
        return cipher_text
    def decrypt(sf, cipher_text, /):
        'no kw"validate", since may add random paddings when encrypt'
        clear_text = sf._decrypt_(cipher_text)
        return clear_text



class IUnitSqrtCipher(ICipher):
    'decrypt===encrypt; encrypt . encrypt === echo; encrypt===sqrt(echo)'
    @abstractmethod
    def _en_de_cipher_op_(sf, a, /):
        'a -> a'
    def en_de_cipher_op(sf, a, /, *, validate):
        return sf.encrypt(a, validate=validate)
    @override
    def _encrypt_(sf, clear_text, /):
        'clear_text -> cipher_text'
        a = clear_text
        return sf._en_de_cipher_op_(a)
    @override
    def _decrypt_(sf, cipher_text, /):
        'cipher_text -> clear_text'
        a = cipher_text
        return sf._en_de_cipher_op_(a)

#bug:_filter4kw = filterT__dict(predT__tuple(dot[lambda s: not str.startswith(s, '_'), type_isT(str)], pred__True))
_filter4kw = filterT__dict(predT__tuple(predT__AND(type_isT(str), lambda s: not str.startswith(s, '_')), pred__True))

class ICipher__with_cipher_key_generator(ICipher):
    @abstractmethod
    def _get_cipher_key_generator_(sf, /):
        '-> ICipherKeyGenerator/str'
    def get_cipher_key_generator(sf, /):
        return sf._get_cipher_key_generator_()
    def get_prefix4key(sf, /):
        return sf.get_cipher_key_generator().get_prefix4key()





class ICipher_mod(IHas__modulo, ICipher):
    @abstractmethod
    def _encrypt_mod_(sf, u, /):
        'uint%M -> uint%M'
    @abstractmethod
    def _decrypt_mod_(sf, v, /):
        'uint%M -> uint%M'
    @override
    def _encrypt_(sf, clear_text, /):
        'clear_text -> cipher_text'
        u = clear_text
        modulo = sf.get_modulo()
        check_uint_lt(modulo, u)

        v = sf._encrypt_mod_(u)
        check_uint_lt(modulo, v)

        cipher_text = v
        return cipher_text

    @override
    def _decrypt_(sf, cipher_text, /):
        'cipher_text -> clear_text'
        v = cipher_text
        modulo = sf.get_modulo()
        check_uint_lt(modulo, v)

        u = sf._decrypt_mod_(v)
        check_uint_lt(modulo, u)

        clear_text = u
        return clear_text
class IUnitSqrtCipher_mod(ICipher_mod, IUnitSqrtCipher):
    @abstractmethod
    def _en_de_cipher_op_mod_(sf, u, /):
        'uint%M -> uint%M'
    #def en_de_cipher_op_mod(sf, u, /, *, validate): return sf.encrypt(u, validate=validate)
    @override
    def _en_de_cipher_op_(sf, a, /):
        'a -> a'
        return sf._en_de_cipher_op_mod_(a)
    @override
    def _encrypt_mod_(sf, u, /):
        'uint%M -> uint%M'
        return sf._en_de_cipher_op_mod_(u)
    @override
    def _decrypt_mod_(sf, v, /):
        'uint%M -> uint%M'
        return sf._en_de_cipher_op_mod_(v)

class ICipher_bits(IHas__modulo__bits, ICipher_mod):
    pass

class Cipher__chain(IEase_repr, ICipher):
    @classmethod
    @override
    def _mk_kwargs4init_(cls, /, *, ciphers):
        '-> __init__.kwargs'
        return dict(ciphers=mk_tuple(ciphers))
    def __init__(sf, /, *, ciphers):
        check_tuple(ciphers)
        if not all(isinstance(cipher, ICipher) for cipher in ciphers):raise TypeError

    @override
    def _encrypt_(sf, clear_text, /):
        'clear_text -> cipher_text'
        a = clear_text
        for cipher in reversed(sf.ciphers):
            a = cipher.encrypt(a, validate=False)
        cipher_text = a
        return cipher_text

    @override
    def _decrypt_(sf, cipher_text, /):
        'cipher_text -> clear_text'
        a = cipher_text
        for cipher in iter(sf.ciphers):
            a = cipher.decrypt(a)
        clear_text = a
        return clear_text

#class Cipher_mod__chain(Cipher__chain, ICipher_mod):
class Cipher_mod__chain(Cipher__chain, IEase_repr, ICipher_mod):
    _encrypt_ = ICipher_mod._encrypt_
    _decrypt_ = ICipher_mod._decrypt_
    _encrypt_mod_ = Cipher__chain._encrypt_
    _decrypt_mod_ = Cipher__chain._decrypt_

    def __init__(sf, /, *, ciphers):
        super().__init__(ciphers=ciphers)

        if not all(isinstance(cipher, ICipher_mod) for cipher in ciphers):raise TypeError
        if not ciphers:raise TypeError
        M = ciphers[0].get_modulo()
        if not all(cipher.get_modulo()==M for cipher in ciphers):raise TypeError


    @override
    def _get_modulo_(sf, /):
        '-> modulo/uint'
        return sf.ciphers[0].get_modulo()


class UnitSqrtCipher__chain(IEase_repr, IUnitSqrtCipher):
    'not subclass of Cipher__chain'
    @classmethod
    def mk_Cipher__chain(cls, ciphers, /):
        cipherR = Cipher__chain.mk(ciphers=ciphers)
        return cipherR
    @classmethod
    @override
    def _mk_kwargs4init_(cls, /, *, unit_sqrt_cipher, ciphersR):
        '-> __init__.kwargs'
        cipherR = cls.mk_Cipher__chain(ciphersR)
        return dict(unit_sqrt_cipher=unit_sqrt_cipher, cipherR=cipherR)

    def __init__(sf, /, *, unit_sqrt_cipher, cipherR):
        if not isinstance(unit_sqrt_cipher, IUnitSqrtCipher):raise TypeError
        if not isinstance(cipherR, ICipher):raise TypeError

    @override
    def _en_de_cipher_op_(sf, a, /):
        'a -> a'
        b = sf.cipherR.encrypt(a, validate=False)
        c = sf.unit_sqrt_cipher.en_de_cipher_op(b, validate=False)
        d = sf.cipherR.decrypt(c)
        return d



class UnitSqrtCipher_mod__chain(UnitSqrtCipher__chain, IEase_repr, IUnitSqrtCipher_mod):
    _en_de_cipher_op_ = IUnitSqrtCipher_mod._en_de_cipher_op_
    _en_de_cipher_op_mod_ = UnitSqrtCipher__chain._en_de_cipher_op_

    @classmethod
    @override
    def mk_Cipher__chain(cls, ciphers, /):
        cipherR = Cipher_mod__chain.mk(ciphers=ciphers)
        return cipherR

    def __init__(sf, /, *, unit_sqrt_cipher, cipherR):
        super().__init__(unit_sqrt_cipher=unit_sqrt_cipher, cipherR=cipherR)

        unit_sqrt_cipher_mod = unit_sqrt_cipher
        cipherR_mod = cipherR
        del unit_sqrt_cipher, cipherR

        if not isinstance(unit_sqrt_cipher_mod, IUnitSqrtCipher_mod):raise TypeError
        if not isinstance(cipherR_mod, ICipher_mod):raise TypeError
        if not unit_sqrt_cipher_mod.get_modulo()==cipherR_mod.get_modulo():raise TypeError

    @override
    def _get_modulo_(sf, /):
        '-> modulo/uint'
        return sf.unit_sqrt_cipher.get_modulo()





class UnitSqrtCipher_mod__subtracted_by(IEase_repr_init, IUnitSqrtCipher_mod):
    @classmethod
    @override
    def _mk_kwargs4init_(cls, /, *, modulo, minuend_or_ver='ver1__mul1573div1987'):
        '-> __init__.kwargs'
        if is_str(minuend_or_ver):
            ver = minuend_or_ver
            minuend = cls.mk_minuend(modulo, ver=ver)
        else:
            minuend = minuend_or_ver
        return dict(minuend=minuend, modulo=modulo)
    @classmethod
    def mk_minuend(cls, modulo, /, *, ver):
        r'''
        [x =[%M]= m-x]
        <==> [2*x =[%M]= m]
        ==>> [M%2==1]or[m%2==0]
        #'''
        if ver == 'ver1__mul1573div1987':
            minuend = modulo*1573//1987
            if modulo%2==0 and minuend%2==0:
                minuend += 1
            minuend -= modulo
        else:
            cls
            raise NotImplementedError(f'{cls}.ver=={ver!r}')
        return minuend
    def __init__(sf, /, *, minuend, modulo):
        check_uint(modulo)
        check_int(minuend)
        if not -modulo <= minuend <= modulo:raise TypeError
            # to allow (-1) instead of (M-1)
        pass
    @override
    def _get_modulo_(sf, /):
        '-> modulo/uint'
        return sf.modulo
    @override
    def _en_de_cipher_op_mod_(sf, u, /):
        'uint%M -> uint%M'
        #v = sf.modulo -1 -u
        v = (sf.minuend-u) %sf.modulo
        return v


class Cipher_mod__mask(IEase_repr_init, ICipher_mod):
    def __init__(sf, /, *, cipher_mod, modulo):
        checkT__type_le(ICipher_mod)(cipher_mod)
        check_uint(modulo)
        if not cipher_mod.get_modulo() <= modulo:raise TypeError
            # "<=": cut data_space into low/high parts, low part transform, high leave unchanged
    @override
    def _get_modulo_(sf, /):
        '-> modulo/uint'
        return sf.modulo
    @override
    def _encrypt_mod_(sf, u, /):
        'uint%M -> uint%M'
        cipher_mod = sf.cipher_mod
        m = cipher_mod.get_modulo()
        if u < m:
            v = cipher_mod.encrypt(u, validate=False)
        else:
            v = u
        return v

    @override
    def _decrypt_mod_(sf, v, /):
        'uint%M -> uint%M'
        cipher_mod = sf.cipher_mod
        m = cipher_mod.get_modulo()
        if v < m:
            u = cipher_mod.decrypt(v)
        else:
            u = v
        return u



class Cipher_mod__add_then_mul(IEase_repr, ICipher_mod):
    @classmethod
    @override
    def _mk_kwargs4init_(cls, /, *, key4add, key4mul, modulo):
        '-> __init__.kwargs'
        inv4key4mul = invmod(key4mul, modulo)
        return dict(key4add=key4add, key4mul=key4mul, inv4key4mul=inv4key4mul, modulo=modulo)

    def __init__(sf, /, *, key4add, key4mul, inv4key4mul, modulo):
        if not key4mul*inv4key4mul%modulo == 1:raise TypeError
        pass
    @override
    def _get_modulo_(sf, /):
        '-> modulo/uint'
        return sf.modulo
    @override
    def _encrypt_mod_(sf, u, /):
        'uint%M -> uint%M'
        v = (u+sf.key4add)*sf.key4mul%sf.modulo
        return v

    @override
    def _decrypt_mod_(sf, v, /):
        'uint%M -> uint%M'
        u = (v*sf.inv4key4mul-sf.key4add)%sf.modulo
        return u

class Cipher_mod__rotate(IEase_repr, ICipher_mod):
    @classmethod
    def mk_N1_N2(cls, modulo, /, *, N_or_ver):
        if is_str(N_or_ver):
            ver = N_or_ver
            if ver == 'ver1__mul233div377':
                N = modulo *233 //377
            else:
                cls
                raise NotImplementedError(f'{cls}.ver=={ver!r}')
        else:
            N = N_or_ver
        N %= modulo
        N_ = modulo - N
            # N=0, N_=M
        N1 = min(N, N_)
        N2 = max(N, N_)
        assert 0 <= N1 <= N2 <= N1+N2 == modulo
        return N1, N2

    @classmethod
    @override
    def _mk_kwargs4init_(cls, /, *, modulo, N_or_ver='ver1__mul233div377'):
        '-> __init__.kwargs'
        N1, N2 = cls.mk_N1_N2(modulo, N_or_ver=N_or_ver)
        if not 2 < N1 < N1+2 <= N2 < N2+2 <modulo:raise ValueError(f'modulo too small?: {modulo!r}: {N2},{N1}')
        return dict(N1 = N1, N2 = N2, modulo = modulo)
    def __init__(sf, /, *, N1, N2, modulo):
        if not N1+N2 == modulo:raise TypeError
        if not 2 < N1 < N1+2 <= N2 < N2+2 <modulo:raise TypeError

    @override
    def _get_modulo_(sf, /):
        '-> modulo/uint'
        return sf.modulo
    @override
    def _encrypt_mod_(sf, u, /):
        'uint%M -> uint%M'
        N1 = sf.N1
        N2 = sf.N2
        M = sf.modulo

        if u < N1:
            v = u+N2
        elif u < N2:
            v = N2-1-u
        else:
            v = 2*N2-1-u
        return v

    @override
    def _decrypt_mod_(sf, v, /):
        'uint%M -> uint%M'
        N1 = sf.N1
        N2 = sf.N2
        M = sf.modulo

        if v >= N2:
            u = v-N2
        elif v < N2-N1:
            u = N2-1-v
        else:
            u = 2*N2-1-v
        return u

class Cipher_mod__permutation_partition(IEase_repr, ICipher_mod):
    r'''
    see:IInnerIndexablePartition_mod
    see:Cipher_mod__permutation_partition
    see:Cipher_bits__permutation
    #'''
    @classmethod
    @override
    def _mk_kwargs4init_(cls, /, *, inner_indexable_partition_mod, permutation):
        '-> __init__.kwargs'
        old2new = permutation
        new2old = inverse_uint_bijection_array(old2new)
        return dict(inner_indexable_partition_mod=inner_indexable_partition_mod, new2old = (*new2old,), old2new = (*old2new,))
    def __init__(sf, /, *, inner_indexable_partition_mod, old2new, new2old):
        checkT__type_le(IInnerIndexablePartition_mod)(inner_indexable_partition_mod)
        check_tuple(old2new)
        check_tuple(new2old)

        if not len(old2new) == len(new2old):raise TypeError
        if not is_inverse_uint_bijection_array_of(old2new, new2old):raise TypeError


        if not len(old2new) == inner_indexable_partition_mod.get_num_eqvclss():raise TypeError


    @override
    def _get_modulo_(sf, /):
        '-> modulo/uint'
        return sf.inner_indexable_partition_mod.get_modulo()

    @override
    def _encrypt_mod_(sf, u, /):
        'uint%M -> uint%M'
        old2new = sf.old2new
        new2old = sf.new2old
        pn = sf.inner_indexable_partition_mod

        (old_idx8eqvcls, old_idx8inner) = pn.element2idx8eqvcls_idx8inner(u, validate=False)
        new_idx8tmp_slots = old2new[old_idx8eqvcls]
        def f(inew, /):
            iold = new2old[inew]
            return pn.get_num_elements_at(iold)
        new_offset8tmp_slots = sum(map(f, range(new_idx8tmp_slots)))
        v = new_offset8tmp_slots + old_idx8inner
        return v
    @override
    def _decrypt_mod_(sf, v, /):
        'uint%M -> uint%M'
        old2new = sf.old2new
        new2old = sf.new2old
        pn = sf.inner_indexable_partition_mod
        def _mk_it():
            for iold in pseudo_seq2iter_values(new2old):
                yield pn.get_num_elements_at(iold)

        curr_offset8tmp_slots = 0
        for new_idx8tmp_slots, next_offset8tmp_slots in enumerate(accumulate(_mk_it())):
            if v < next_offset8tmp_slots:
                break
            curr_offset8tmp_slots = next_offset8tmp_slots
        else:
            raise logic-err
        old_idx8inner = v - curr_offset8tmp_slots
        old_idx8eqvcls = new2old[new_idx8tmp_slots]
        u = pn.element5idx8eqvcls_idx8inner(old_idx8eqvcls, old_idx8inner, validate=False)
        return u
#end-class Cipher_mod__permutation_partition(IEase_repr_init, ICipher_mod):


class Cipher_bits__permutation(IEase_repr, ICipher_bits):
    r'''
    defect:all 0s/1s are fixed point
    defect:uniform sampling of permutations are not good to be used as shuffle
    #
    see:IInnerIndexablePartition_mod
    see:Cipher_mod__permutation_partition
    see:Cipher_bits__permutation
    #'''
    @classmethod
    @override
    def _mk_kwargs4init_(cls, /, *, permutation):
        '-> __init__.kwargs'
        old2new = permutation
        new2old = inverse_uint_bijection_array(old2new)
        return dict(new2old = (*new2old,), old2new = (*old2new,))
    def __init__(sf, /, *, old2new, new2old):
        check_tuple(old2new)
        check_tuple(new2old)

        if not len(old2new) == len(new2old):raise TypeError
        if not is_inverse_uint_bijection_array_of(old2new, new2old):raise TypeError

    @override
    def _get_len_bits_(sf, /):
        '-> len_bits/uint'
        return len(sf.old2new)

    @override
    def _encrypt_mod_(sf, u, /):
        'uint%M -> uint%M'
        len_bits = sf.get_len_bits()
        v = perform_permutation__inv__uint8bits(sf.new2old, len_bits, u)
        return v

    @override
    def _decrypt_mod_(sf, v, /):
        'uint%M -> uint%M'
        len_bits = sf.get_len_bits()
        u = perform_permutation__inv__uint8bits(sf.old2new, len_bits, v)
        return u
class Cipher_bits__xor(IEase_repr_init, ICipher_bits):
    r'''
    defect:uniform distribution is not good to be used as cipher
        n = randrange(L*23//61, L*43//61)
        permutate/shuffle('0'*n+'1'*(L-n))
            #always roughly half 0s and half 1s
    #'''
    def __init__(sf, /, *, key4xor:'uint8bits', len_bits):
        assert 0 <= key4xor < 1<<len_bits

    @override
    def _get_len_bits_(sf, /):
        '-> len_bits/uint'
        return sf.len_bits

    @override
    def _encrypt_mod_(sf, u, /):
        'uint%M -> uint%M'
        v = u ^ sf.key4xor
        return v

    @override
    def _decrypt_mod_(sf, v, /):
        'uint%M -> uint%M'
        u = v ^ sf.key4xor
        return u


#已有permutation:class Cipher_bits__rotate(IEase_repr, ICipher_bits):
class Cipher_bits__accumulate_xor_reversed(IEase_repr_init, ICipher_bits):
    r'''
    defect:all 0s are fixed point
    #'''
    def __init__(sf, /, *, len_bits):
        pass

    @override
    def _get_len_bits_(sf, /):
        '-> len_bits/uint'
        return sf.len_bits

    @override
    def _encrypt_mod_(sf, u, /):
        'uint%M -> uint%M'
        r'''
        bit8st[0] := xor~ initial_bits
        bits8key
        bits8input
        bits8ouput
        ==>>
        bits8ouput[0] = xor{bit8st[0], bits8key[0], bits8input[0]}

        bit8st[1] := xor {bit8st[0]保持, bits8ouput[0]进入, initial_bits[0]退出}
            === xor{bits8key[0], bits8input[0], initial_bits[0]}
        bits8ouput[1] = xor{bit8st[1], bits8key[1], bits8input[1]}
            === xor{bits8key[0], bits8input[0], initial_bits[0], bits8key[1], bits8input[1]}

        bit8st[2] := xor {bit8st[1]保持, bits8ouput[1]进入, initial_bits[1]退出}
            === xor {bits8key[1], bits8input[1], initial_bits[1]}

        ====
        其实真正有意义的，只有accumulate(bits8input)

        #'''

        len_bits = sf.get_len_bits()
        bs = uint2bits(len_bits, u)
        _01s = map(int, reversed(bs))
        _01s = accumulate(_01s, operator.__xor__)
        bs = ''.join(map(str, _01s))
        v = int(bs, 2)
        return v

    @override
    def _decrypt_mod_(sf, v, /):
        'uint%M -> uint%M'
        len_bits = sf.get_len_bits()
        bs = uint2bits(len_bits, v)
        _01s = map(int, reversed(bs))
        def iter_diff_01s(_01s, /):
            for x01 in _01s:
                pre = x01
                break
            else:
                return
            for x01 in _01s:
                yield pre ^ x01
                pre = x01
            else:
                last = pre
                yield last

        _01s = iter_diff_01s(_01s)
        bs = ''.join(map(str, _01s))
        u = int(bs, 2)
        return u
def _test_ICipher_mod(cls, /, **kwargs):
    print(cls, kwargs)
    sf = cls.mk(**kwargs)
    print(sf)

    M = sf.get_modulo()
    len_bits = (M-1).bit_length() if M else 1
    for u in range(M):
        v = sf.encrypt(u, validate=True)
        print(u, v)
        print('  ', uint2bits(len_bits, u))
        print('  ', uint2bits(len_bits, v))
        if not u == sf.decrypt(v): raise logic-err

def _test_Cipher_mod__rotate():
    cls = Cipher_mod__rotate
    _test_ICipher_mod(cls, modulo=15)
def _test_Cipher_mod__add_then_mul():
    cls = Cipher_mod__add_then_mul
    _test_ICipher_mod(cls, modulo=15, key4add=7, key4mul=2)#, inv4key4mul=8
_test_Cipher_mod__rotate()
_test_Cipher_mod__add_then_mul()

def _test_Cipher_bits__permutation():
    cls = Cipher_bits__permutation
    len_bits = 4
    permutation = mk_permutation(len_bits, randrange)
    _test_ICipher_mod(cls, permutation=permutation)
    permutation = mk_permutation(len_bits, randbelow)
    _test_ICipher_mod(cls, permutation=permutation)
def _test_Cipher_bits__xor():
    cls = Cipher_bits__xor
    len_bits = 4
    key4xor = getrandbits(len_bits)
    _test_ICipher_mod(cls, key4xor=key4xor, len_bits=len_bits)
    key4xor = randbits(len_bits)
    _test_ICipher_mod(cls, key4xor=key4xor, len_bits=len_bits)
def _test_Cipher_bits__accumulate_xor_reversed():
    cls = Cipher_bits__accumulate_xor_reversed
    len_bits = 4
    _test_ICipher_mod(cls, len_bits=len_bits)

_test_Cipher_bits__permutation()
_test_Cipher_bits__xor()
_test_Cipher_bits__accumulate_xor_reversed()
def _test_Cipher_mod__mask():
    cls = Cipher_mod__mask
    len_bits = 4
    cipher_mod = Cipher_bits__accumulate_xor_reversed.mk(len_bits=len_bits)
    _test_ICipher_mod(cls, cipher_mod=cipher_mod, modulo=31)
_test_Cipher_mod__mask()

def _test_Cipher_mod__chain():
    cls = Cipher_mod__chain
    len_bits = 4
    cipher_bits__accumulate_xor_reversed = Cipher_bits__accumulate_xor_reversed.mk(len_bits=len_bits)

    M = cipher_bits__accumulate_xor_reversed.get_modulo()
    cipher_mod__rotate = Cipher_mod__rotate.mk(modulo=M)

    ciphers = (cipher_mod__rotate, cipher_bits__accumulate_xor_reversed)
    _test_ICipher_mod(cls, ciphers=ciphers)
_test_Cipher_mod__chain()


def _test_UnitSqrtCipher_mod__subtracted_by():
    cls = UnitSqrtCipher_mod__subtracted_by
    _test_ICipher_mod(cls, modulo=15)
_test_UnitSqrtCipher_mod__subtracted_by()


def _test_UnitSqrtCipher_mod__chain():
    cls = UnitSqrtCipher_mod__chain

    len_bits = 4
    cipher_bits__accumulate_xor_reversed = Cipher_bits__accumulate_xor_reversed.mk(len_bits=len_bits)

    M = cipher_bits__accumulate_xor_reversed.get_modulo()
    cipher_mod__rotate = Cipher_mod__rotate.mk(modulo=M)

    ciphersR = (cipher_mod__rotate, cipher_bits__accumulate_xor_reversed)

    unit_sqrt_cipher_mod = UnitSqrtCipher_mod__subtracted_by.mk(modulo=M)

    _test_ICipher_mod(cls, unit_sqrt_cipher=unit_sqrt_cipher_mod, ciphersR=ciphersR)
_test_UnitSqrtCipher_mod__chain()

def _test_Cipher_mod__permutation_partition():
    cls = Cipher_mod__permutation_partition
    origin4rngs = 4
    idx8eqvcls2num_elements = (1, 2, 3, 4, 5, 3)
    num_eqvclss = len(idx8eqvcls2num_elements)
    permutation = mk_permutation(num_eqvclss, randrange)
    pn = InnerIndexablePartition_mod__rng8eqvcls.mk(origin4rngs=origin4rngs, idx8eqvcls2num_elements=idx8eqvcls2num_elements)
    _test_ICipher_mod(cls, inner_indexable_partition_mod=pn, permutation=permutation)

    len_bits = 4
    num_eqvclss = len_bits+1
    permutation = mk_permutation(num_eqvclss, randrange)
    pn = InnerIndexablePartition_bits__count_1s.mk(len_bits=len_bits)
    _test_ICipher_mod(cls, inner_indexable_partition_mod=pn, permutation=permutation)


_test_Cipher_mod__permutation_partition()

class Cipher__charset(IEase_repr_init, ICipher):
    def __init__(sf, /, *, ordered_charset, mk_ICipher5modulo):
        check_callable(mk_ICipher5modulo)
        checkT__type_le(IOrderedCharset)(ordered_charset)
        pass

    def _check_cipher_mod_(sf, cipher_mod, /):
        checkT__type_le(ICipher_mod)(cipher_mod)
    def check_cipher_mod(sf, cipher_mod, /):
        sf._check_cipher_mod_(cipher_mod)
    def _preprocess(sf, s, /):
        ordered_charset = sf.ordered_charset
        u, L = ordered_charset.str2uint_with_len__via_digits__big_endian(s, validate=False)
        radix = len(ordered_charset)
        modulo = radix**L
        assert 0 <= u < modulo
        cipher_mod = sf.mk_ICipher5modulo(modulo)
        sf.check_cipher_mod(cipher_mod)
        if not cipher_mod.get_modulo()==modulo: raise TypeError
        return u, L, cipher_mod
    def _postprocess(sf, u, L, /):
        ordered_charset = sf.ordered_charset
        s = ordered_charset.str5uint_with_len__via_digits__big_endian((u, L), validate=False)
        return s

    @override
    def _encrypt_(sf, clear_text, /):
        'clear_text -> cipher_text'
        u, L, cipher_mod = sf._preprocess(clear_text)
        v = cipher_mod.encrypt(u, validate=False)
        cipher_text = sf._postprocess(v, L)
        return cipher_text

    @override
    def _decrypt_(sf, cipher_text, /):
        'cipher_text -> clear_text'
        v, L, cipher_mod = sf._preprocess(cipher_text)
        u = cipher_mod.decrypt(v)
        clear_text = sf._postprocess(u, L)
        return clear_text

#def _mk_ICipher5modulo(modulo, /):


def _test_le_Cipher__charset(cls, /, *, mk_ICipher5modulo):
    checkT__issubclass__any(Cipher__charset)(cls)
    print(cls)
    ordered_charset = hex___ordered_charset__RangeBased
    clear_text = '000AF9C0010'
    cipher__charset = cls(ordered_charset=ordered_charset, mk_ICipher5modulo=mk_ICipher5modulo)
    print(cipher__charset)


    cipher_text = cipher__charset.encrypt(clear_text, validate=True)
    if not cipher__charset.decrypt(cipher_text)==clear_text:raise logic-err

    print('   ', repr(clear_text))
    print('   ', repr(cipher_text))


class UnitSqrtCipher__charset(Cipher__charset, IUnitSqrtCipher):
    _encrypt_ = IUnitSqrtCipher._encrypt_
    _decrypt_ = IUnitSqrtCipher._decrypt_
    _en_de_cipher_op_ = Cipher__charset._decrypt_

    def _check_cipher_mod_(sf, cipher_mod, /):
        super()._check_cipher_mod_(cipher_mod)
        #checkT__type_le(IUnitSqrtCipher)(cipher_mod)
        #   偶然关联？
        checkT__type_le(IUnitSqrtCipher_mod)(cipher_mod)

def _test_Cipher__charset():
    cls = Cipher__charset
    def _mk_ICipher5modulo(modulo, /):
        return Cipher_mod__rotate.mk(modulo=modulo)

    _test_le_Cipher__charset(cls, mk_ICipher5modulo = _mk_ICipher5modulo)
def _test_UnitSqrtCipher__charset():
    cls = UnitSqrtCipher__charset
    def _mk_ICipher5modulo(modulo, /):
        return UnitSqrtCipher_mod__subtracted_by.mk(modulo=modulo)

    _test_le_Cipher__charset(cls, mk_ICipher5modulo = _mk_ICipher5modulo)
_test_Cipher__charset()
_test_UnitSqrtCipher__charset()

