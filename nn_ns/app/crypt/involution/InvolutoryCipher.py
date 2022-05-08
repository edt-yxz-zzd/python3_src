#__all__:goto
#main_body_src_code:goto
#HHHHH
r'''
[[cmds:
py -m nn_ns.app.crypt.involution.involutory_cipher_cmd
py -m nn_ns.app.crypt.involution.involutory_cipher_cmd -iEOL OFF -oEOL ON --charset4txt alnum -k ++--/// -i 207eygA --core_involutory_cipher subtracted_by
py -m nn_ns.app.crypt.involution.involutory_cipher_cmd -iEOL OFF -oEOL ON --charset4txt alnum -k ++--/// -i 207eygA --core_involutory_cipher flip_parity
py -m nn_ns.app.crypt.involution.involutory_cipher_cmd -iEOL OFF -oEOL ON --charset4txt printable_ascii -k ++--/// -i '~' --core_involutory_cipher flip_parity
py -m nn_ns.app.crypt.involution.involutory_cipher_cmd -iEOL OFF -oEOL ON --charset4txt nonspace_printable_ascii -k ++--/// -i '~' --core_involutory_cipher flip_parity
py -m nn_ns.app.crypt.involution.involutory_cipher_cmd -iEOL OFF -oEOL ON --charset4txt alnum -k ++--/// -i 345dfyy --core_involutory_cipher fmap_bit_op_on_tail_bits

py -m nn_ns.app.debug_cmd   nn_ns.app.crypt.involution.InvolutoryCipher
py -m nn_ns.app.crypt.involution.InvolutoryCipher
py -m nn_ns.app.crypt.involution.InvolutoryCipher > /sdcard/0my_files/tmp/_.txt
view /sdcard/0my_files/tmp/_.txt

e ../../python3_src/nn_ns/app/crypt/involution/InvolutoryCipher.py
e ../../python3_src/nn_ns/app/crypt/involution/involutory_cipher_cmd.py

from nn_ns.app.crypt.involution.InvolutoryCipher import ...
]]



[[释义:
自逆加密
    InvolutoryCipher
    self-inverse function
    involutory function
.+1,$s/InvolutionCipher/InvolutoryCipher/g


roots of unity (not "unit"!)
square root of unity


see:
  view others/数学/involution自逆函数.txt.
  view others/数学/编程/TODO_list/周期长度为二的对称加密.txt
    view ../../python3_src/nn_ns/app/crypt/InvolutoryCipher.py
  ===
  involution
  https://handwiki.org/wiki/Involution_(mathematics)
    In mathematics, an involution, involutory function, or self-inverse function[1] is a function f that is its own inverse,

        f(f(x)) = x

    for all x in the domain of f.[2] Equivalently, applying f twice produces the original value.


[f is invertible function] =[def]=
  [?g. @x. g(f(x))===x]
  let f**-1 =[def]= g

[f is involution] =[def]=
  [@x. f(f(x)) === x]
  [f . f === echo]
  [f === f**-1]




]]





#HHHHH
copied from ./0exlpain.txt
[[[
endofunction
  ?自函数
    翻译来自：https://hongjiang.info/understand-monad-5-what-is-endofunctor/
  内射函数/自射
    我自己的翻译
involution
  ?自逆函数/++回旋函数
    我自己的翻译
  n. 卷绕,内卷,回旋
    来自：https://cdict.net/q/involution

idempotent function 幂等函数
bijection双射
injection单射
surjection满射
permutation置换函数#排列/置换
  来自：https://cdict.net/q/permutation
identity恒等映射
  来自：https://zhidao.baidu.com/question/166982901.html

[f is endofunction]
    =[def]= [f is function][domain<f> === codomain<f>]

[f is involution]
    = [f is involutory function]
    =[def]= [f is endofunction][f . f === echo]

[f is idempotent function]
    =[def]= [f is endofunction][f . f === f]

[f is permutation]
    = [f is permutatory/permutative function]
    =[def]= [f is bijective/invertible endofunction]
    = [f is endofunction][f is bijection]

[f is bijection]
  = [f is bijective function]
  = [f is one-to-one correspondence function]
  =[def]= [f is injection][f is surjection]

[f is injection]
  = [f is injective function]
  = [f is invertible function]
  = [f is one-to-one function]
  =[def]= [f is function][?g<-function. @(x,y)<-f. [x===g(y)]]

[f is surjection]
  = [f is surjective function]
  = [f is onto function]
  =[def]= [f is function][codomain<f> === image<f>]


identity

]]]















[[renamed to InvolutoryCipher.py:

[old:
py -m nn_ns.app.debug_cmd   nn_ns.app.crypt.UnitSqrtCipher.unit_sqrt_cipher
py -m nn_ns.app.crypt.UnitSqrtCipher.unit_sqrt_cipher
py -m nn_ns.app.crypt.UnitSqrtCipher.unit_sqrt_cipher > /sdcard/0my_files/tmp/_.txt
view /sdcard/0my_files/tmp/_.txt

e ../../python3_src/nn_ns/app/crypt/UnitSqrtCipher/unit_sqrt_cipher.py

from nn_ns.app.crypt.UnitSqrtCipher.unit_sqrt_cipher import ...
]

e ../../python3_src/nn_ns/app/crypt/UnitSqrtCipher/unit_sqrt_cipher.py
!mkdir ../../python3_src/nn_ns/app/crypt/involution/
!mv ../../python3_src/nn_ns/app/crypt/UnitSqrtCipher/unit_sqrt_cipher.py ../../python3_src/nn_ns/app/crypt/involution/InvolutoryCipher.py
e ../../python3_src/nn_ns/app/crypt/involution/InvolutoryCipher.py


.+1,$s/UnitSqrtCipher/InvolutoryCipher/g
.+1,$s/unit_sqrt_cipher/involutory_cipher/g

]]





#HHHHH

TODO:
    to fill:_4main.mk_ICipher5modulus

    xxxx TODO ....
        ......  ...... dynamic property instead of py-type
        so that Cipher__chain determine its dynamic type at runtime depend on derived info from input args
        ==>> I/O type
            let Cipher__chain verify whether match, eg modulus==?


    ###to turnoff print() unconditionaly or move out main()...
      DONE
        not call main() here
        mk: nn_ns.app.involutory_cipher

    ++自逆加密:
        bits-xor (pseudo_random_bits)
        mod-xor1-parity-flip(odd<->even, exclude overflow)
        mod-fmap layers on bits
/InvolutoryCipher
.+1,$s/Cipher_bits__xor/InvolutoryCipher_bits__xor/g

TODO:
    main()
        * charset DONE:
            .ordered_charset4*
                eg .ordered_charset4binary
            ===
            binary
            digit
            hex
            alpha
            alnum
            nonspace_printable_ascii
                #exclude ' '
                #include '\\' "'" '"'
            cjk_common_subset_2513_trivial_TS_2227
            cjk_common_subset_2513
            nonspace_printable_gb2312

        * convert between diff charset:
            IOrderedCharset.convert_to :: sf8src_charset -> dst_charset -> src_txt -> dst_txt

        * cipher for text/human:
            Cipher__charset
                InvolutoryCipher__charset
                    #the primacy target

        * cipher for chain:
            Cipher__chain
                Cipher_mod__chain
            InvolutoryCipher__chain
                InvolutoryCipher_mod__chain

            Cipher__chain.mk(ciphers=[a, b, c])
                encrypt := a.E . b.E . c.E
                decrypt := c.D . b.D . a.D

            InvolutoryCipher__chain.mk(involutory_cipher=u, ciphersR=[a, b, c])
                encrypt=decrypt := c.D . b.D . a.D . u.U . a.E . b.E . c.E

        * cipher%modulus for modular arithmetic
            * cipher%2**num_bits for combination




==============
modulo 求模函数
modulus 模参数
modular arithmetic 模算术体系？
.+1,$s/modulo/modulus/g

len ~ len() ~ function ~ not noun
    len_ints/len_rngs
    iter_ints/iter_rngs
.+1,$s/len_bits/num_bits/g

#'''

#HHHHH
__all__ = '''
    count_1s_ex
    count_1s
    uint2bits

    mod__double_width_


    check_uint_tuple
    check_basic_permutation
    perform_basic_permutation__inv__uint8bits
    iter_perform_basic_permutation__inv
    mk_bipermutation
    mk_basic_permutation


    IEase_repr
        IEase_repr_init
            BiPermutation


    IOrderedCharset
        IOrderedCharset__lookup
            OrderedCharset__str
                binary___ordered_charset__str
                hex___ordered_charset__str
        OrderedCharset__RangeBased
            binary___ordered_charset__RangeBased
            hex___ordered_charset__RangeBased


    ordered_charset4binary
    ordered_charset4digit
    ordered_charset4hex

    ordered_charset4alpha
    ordered_charset4alnum

    ordered_charset4printable_ascii
    ordered_charset4printable_gb2312

    ordered_charset4nonspace_printable_ascii
    ordered_charset4nonspace_printable_gb2312

    ordered_charset4cjk_common_subset_2513_trivial_TS_2227
    ordered_charset4cjk_common_subset_2513

    full_name2ordered_charset
    short_name2ordered_charset









    ICipherKeyGenerator


    IHas__modulus
        IHas__modulus__bits




    IInnerIndexablePartition
        IInnerIndexablePartition_mod
            IInnerIndexablePartition_mod__lookup_table
                derived5idx8eqvcls2num_elements
                IInnerIndexablePartition_mod__rng8eqvcls
                    InnerIndexablePartition_mod__rng8eqvcls
                IInnerIndexablePartition_bits__count_1s
                    InnerIndexablePartition_bits__count_1s





    ICipher
        ICipher__with_cipher_key_generator
        IEndoCipher
            IPermutatoryCipher
                ICipher_mod
                    ICipher_bits
                IInvolutoryCipher
                    IInvolutoryCipher_mod
                        IInvolutoryCipher_bits

    Cipher__chain
        Cipher_mod__chain
    InvolutoryCipher__chain
        InvolutoryCipher_mod__chain

    InvolutoryCipher_mod__flip_parity
    InvolutoryCipher_mod__subtracted_by
    InvolutoryCipher_mod__modulus_is_1
        involutory_cipher_mod__modulus_is_1
    Cipher_mod__fmap_bit_op_on_tail_bits
        InvolutoryCipher_mod__fmap_bit_op_on_tail_bits

    Cipher_mod__mask
    Cipher_mod__add_then_mul
    Cipher_mod__rotate
    Cipher_mod__permutation_partition
        Cipher_mod__permutation_partition_fmap

    Cipher_bits__permutation
    InvolutoryCipher_bits__xor
    Cipher_bits__accumulate_xor_reversed


    Cipher__charset
        InvolutoryCipher__charset

    '''.split()

___begin_mark_of_excluded_global_names__0___ = ...
if 0: from nn_ns.CJK.cjk_subsets.hanzi import (
cjk_common_subset_2513
    ,共享汉字字集
,cjk_common_subset_2513_trivial_TS_2227
    ,平凡繁简囗共享汉字字集
)
from nn_ns.CJK.cjk_subsets.hanzi import cjk_common_subset_2513_trivial_TS_2227, cjk_common_subset_2513
from seed.text.mk_char_pt_ranges5predicator import printable_ascii_char_pt_ranges, printable_ascii_sorted_chars, alnum_ascii_sorted_chars
from seed.text.mk_char_pt_ranges5predicator import is_printable_ascii_char, is_printable_ascii_str
from nn_ns.app.register_xor import printable_ascii_gb2312_char_pt_ranges, printable_ascii_gb2312_sorted_chars
from seed.mapping_tools.dict_op import inv__k2v_to_v2k#, inv__k2v_to_v2ks, inv__k2vs_to_v2k, inv__k2vs_to_v2ks
from seed.tiny import MapView#, mk_tuple, check_type_is

assert printable_ascii_sorted_chars in printable_ascii_gb2312_sorted_chars
assert printable_ascii_char_pt_ranges < printable_ascii_gb2312_char_pt_ranges
assert 7539 == (len(printable_ascii_gb2312_sorted_chars))
assert 7539 == (printable_ascii_gb2312_char_pt_ranges.len_ints())
assert 3631 == printable_ascii_gb2312_char_pt_ranges.len_rngs()
    # too sparse to make char_pt_ranges efficient.


#printable_ascii_char2idx4sorted_chars = MapView(inv__k2v_to_v2k(dict(enumerate(printable_ascii_sorted_chars))))



######################
######################
######################
######################
######################
######################
######################
######################



#HHHHH
from seed.abc.abc__ver0 import override, final
from seed.seq_tools.inverse_uint_bijection_array import inverse_uint_bijection_array
from seed.seq_tools.is_inverse_uint_bijection_array_of import is_inverse_uint_bijection_array_of
from seed.math.floor_ceil import floor_log2
from seed.helper.repr_input import repr_helper
from seed.func_tools.fmapT.filterT__tiny import filterT__dict
from seed.func_tools.fmapT.fmapT__tiny import fmapT__dict#fmapT__tuple
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

_saved_print = print
if __name__ == '__main__':
    pass
else:
    #turnoff print if as package
    def _print(*args, **kwargs):
        pass
    globals()['print'] = _print
___end_mark_of_excluded_global_names__0___ = ...
#main_body_src_code:begin




#HHHHH
def count_1s_ex(u, /):
    check_uint(u)
    bs = f'{u:b}'
    num_1s = bs.count('1')
    return bs, num_1s
def count_1s(u, /):
    check_uint(u)
    return bin(u).count('1')
def uint2bits(num_bits, u, /):
    check_uint(u)
    check_uint(num_bits)
    bs = f'{u:b}'
    dL = num_bits - len(bs)
    bs = '0'*dL + bs
    return bs


def mod__double_width_(modulus, u):
    'to allow (-1) instead of (M-1)'
    check_uint(modulus)
    check_int(u)
    if not -modulus <= u <= modulus:
        u %= modulus
        v = u-modulus
        if u > abs(v):
            u = v
    return u





#bug:check_uint_tuple = dot[checkT__pattern_list(check_uint), check_tuple]
check_uint_tuple = checkT__AND(check_tuple, checkT__pattern_list(check_uint))


def check_basic_permutation(old2new, /):
    check_uint_tuple(old2new)
    sz = len(old2new)
    checkT__eq({*range(sz)})({*old2new})
    return
def perform_basic_permutation__inv__uint8bits(new2old, num_bits, u, /):
    bs = uint2bits(num_bits, u)
    bs = ''.join(iter_perform_basic_permutation__inv(new2old, bs))
    v = int(bs, 2)
    return v
def iter_perform_basic_permutation__inv(new2old, ls, /):
    return (ls[old_idx] for old_idx in new2old)
if 0:
    r'''
    def mk_basic_permutation(sz, mk_random_mod, /):
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
    basic_permutation = (*us,)
    return basic_permutation
    #'''
def mk_bipermutation(sz, mk_random_mod, /):
    'sz/uint -> (modulus->pseudo_random%modulus) -> BiPermutation<sz>'
    old2new = mk_basic_permutation(sz, mk_random_mod)
    bipermutation = BiPermutation.mk(old2new=old2new)
    return bipermutation
def mk_basic_permutation(sz, mk_random_mod, /):
    'sz/uint -> (modulus->pseudo_random%modulus) -> old2new/basic_permutation/[uint%sz]{len=sz}'
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
    old2new = basic_permutation = (*us,)
    return old2new






#HHHHH

#bug:_filter4kw = filterT__dict(predT__tuple(dot[lambda s: not str.startswith(s, '_'), type_isT(str)], pred__True))
_filter4kw = filterT__dict(predT__tuple(predT__AND(type_isT(str), lambda s: (not str.startswith(s, '_')) or str.startswith(s, '_IN_'), str.isidentifier), pred__True))

class IEase_repr(ABC):
    r'''

    special attr prefix:
        # other identifier startswith '_' will not showed by __repr__
        #

        _O_:
            not input args ==>> not showed by __repr__
            but: sf._O_xxx can be accessed by sf.xxx
            see:__getattr__

        _IN_:
            is input args ==>> showed by __repr__
            why? to avoid conflict with method name
            see:__repr__::_filter4kw
    #'''
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
    def __getattr__(sf, nm, /):
        _O_nm = f'_O_{nm}'
        d = sf.__dict__
        if _O_nm in d:
            return d[_O_nm]
        raise AttributeError(nm)
class IEase_repr_init(IEase_repr):
#class ICipher__easy_init(IEase_repr):
    #def __init__(sf, /, *, key):
    @classmethod
    @override
    def _mk_kwargs4init_(cls, /, **kwargs):
        '-> __init__.kwargs'
        return dict(**kwargs)



class BiPermutation(IEase_repr_init):
    def __init__(sf, /, *, old2new):
        new2old = inverse_uint_bijection_array(old2new)
        new2old = mk_tuple(new2old)
        sf._O_new2old = new2old
        assert sf.new2old is new2old



r'''
class ICipher__easy_init(ICipher):
    #def __init__(sf, prefix4key, /, **kwargs):
    def __new__(cls, /, *, charset4clear_text, charset4cipher_text, prefix4key **kwargs):
        super(cls, __class__).__new__(cls)
        #sf.prefix4key = prefix4key
        sf.__dict__.update(charset4clear_text=charset4clear_text, charset4cipher_text=charset4cipher_text, prefix4key=prefix4key, **kwargs)
        return sf
#'''
























#HHHHH
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
        'modulus = radix**L; used in modular arithmetic; not used in conversion between diff IOrderedCharset'
        radix = len(sf)
        L = len(s)
        [*digits] = sf.str2iter_idc(s)
        u = radix_repr2uint(radix, digits, is_big_endian=True)
        uint_with_len = u, L

        if validate:
            if not s == sf.str5uint_with_len__via_digits__big_endian(uint_with_len, validate=False):raise logic-err
        return uint_with_len

    def str5uint_with_len__via_digits__big_endian(sf, uint_with_len, /, *, validate):
        'modulus = radix**L; used in modular arithmetic; not used in conversion between diff IOrderedCharset'
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
        'used in conversion between diff IOrderedCharset; not used in modular arithmetic'
        radix = len(sf)
        [*bidigits] = sf.str2iter_idc(s)
        u = bidigits2uint__little_endian(radix, bidigits)
        if validate:
            if not s == sf.str5uint__via_bidigits__little_endian(u, validate=False):raise logic-err
        return u
    def str5uint__via_bidigits__little_endian(sf, u, /, *, validate):
        'used in conversion between diff IOrderedCharset; not used in modular arithmetic'
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
    def __init__(sf, /, *, _IN_idx2char, _IN_char2idx, _IN_check):
        if not len(_IN_idx2char) == len(_IN_char2idx):raise TypeError
        if not _IN_check: return
        L = len(_IN_idx2char)
        #idcL = pseudo_seq2idc(_IN_idx2char)
        idcL = list(range(L)) #vs idcR
        charsL = set(pseudo_seq2iter_values(_IN_idx2char))
        idcR = sorted(_IN_char2idx.values())
        charsR = set(_IN_char2idx)
        if not len(charsR) == L:raise TypeError

        if not charsR == charsL:raise TypeError
        if not idcR == idcL:raise TypeError
        if not all(_IN_char2idx[char]==idx for idx, char in pseudo_seq__enumerate(_IN_idx2char)):raise TypeError

        checkT__pattern_list(check_char)(charsL)
        checkT__pattern_list(check_char)(charsR)

        checkT__pattern_list(check_uint)(idcL)
        checkT__pattern_list(check_uint)(idcR)


    @override
    def __len__(sf, /):
        '-> sz'
        return len(sf._IN_idx2char)
    @override
    def _char2idx_(sf, char, /):
        'char -> idx|raise LookupError'
        return sf._IN_char2idx[char]
    @override
    def _idx2char_(sf, idx, /):
        'idx -> char'
        return sf._IN_idx2char[idx]

class OrderedCharset__str(IOrderedCharset__lookup):
    @classmethod
    @override
    def _mk_kwargs4init_(cls, str8set, /):
        '-> __init__.kwargs'
        check_str(str8set)
        _IN_idx2char = str8set
        _IN_char2idx = {char:idx for idx, char in enumerate(_IN_idx2char)}
        #print(_IN_char2idx)
        return dict(_IN_idx2char=_IN_idx2char, _IN_char2idx=_IN_char2idx, _IN_check=True)


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
        return dict(idx_rngs=idx_rngs, char_pt_rngs=char_pt_rngs, _IN_check=True)

        d = StackStyleSimpleIntMapping()
        d.push_rng_value_pairs(zip(char_pt_rngs.iter_rngs(), begin_idc))

    def __init__(sf, /, *, idx_rngs, char_pt_rngs, _IN_check):
        checkT__type_is(NonTouchRanges)(char_pt_rngs)
        checkT__type_is(TouchRanges)(idx_rngs)
        check_input4isomorphism_mapping__RangeBased(src_ranges=char_pt_rngs, dst_ranges=idx_rngs, dst_ranges__is__idc4seq=True, full_check=_IN_check)

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






#printable_ascii_char2idx4sorted_chars = MapView(inv__k2v_to_v2k(dict(enumerate(printable_ascii_sorted_chars))))
def _mk_all_ordered_charsets(to_show, /):
    str2ordered_charset = OrderedCharset__str.mk
    #ordered_charset
    prefix = 'sorted_chars4'
    for nm, v in _4mk_all_ordered_charsets.__dict__.items():
        if nm.startswith(prefix):
            if not [*v]==sorted(v): raise ValueError(v)
            if not len({*v})==len(v): raise ValueError(v)
            suffix = nm[len(prefix):]
            if to_show:
                print(f'ordered_charset4{suffix} = OrderedCharset__str.mk(_4mk_all_ordered_charsets.{nm})')

#HHHHH
class _4mk_all_ordered_charsets:
    sorted_chars4alnum = alnum_ascii_sorted_chars
    sorted_chars4binary = alnum_ascii_sorted_chars[:2]
    sorted_chars4digit = alnum_ascii_sorted_chars[:10]
    sorted_chars4hex = alnum_ascii_sorted_chars[:16]
    sorted_chars4alpha = alnum_ascii_sorted_chars[10:]

    assert 10+26*2 == len(sorted_chars4alnum)
    assert sorted_chars4alnum[0]=='0'
    assert sorted_chars4alnum[10]=='A'
    assert sorted_chars4alnum[36]=='a'
    assert sorted_chars4alnum[-1]=='z'

    assert sorted_chars4digit[0]=='0'
    assert sorted_chars4digit[-1]=='9'

    assert sorted_chars4hex[0]=='0'
    assert sorted_chars4hex[-1]=='F'

    assert sorted_chars4alpha[0]=='A'
    assert sorted_chars4alpha[-1]=='z'


    sorted_chars4printable_ascii = printable_ascii_sorted_chars
    sorted_chars4printable_gb2312 = printable_ascii_gb2312_sorted_chars
    assert sorted_chars4printable_ascii < sorted_chars4printable_gb2312
    assert sorted_chars4printable_ascii[0] == ' '

    sorted_chars4nonspace_printable_ascii = sorted_chars4printable_ascii[1:]
        #exclude ' '
        #include '\\' "'" '"'
    sorted_chars4nonspace_printable_gb2312 = sorted_chars4printable_gb2312[1:]
    assert sorted_chars4printable_gb2312.split() == [sorted_chars4nonspace_printable_gb2312]
    assert '　' == '\u3000'
    assert '\u3000' not in sorted_chars4nonspace_printable_gb2312
    assert not '\u3000'.isprintable()

    sorted_chars4cjk_common_subset_2513_trivial_TS_2227 = cjk_common_subset_2513_trivial_TS_2227
    sorted_chars4cjk_common_subset_2513 = cjk_common_subset_2513

    #sorted_chars4test_unsorted = '10'
    #sorted_chars4test_duplicated = '11'
_mk_all_ordered_charsets(0)

ordered_charset4binary = OrderedCharset__str.mk(_4mk_all_ordered_charsets.sorted_chars4binary)
ordered_charset4digit = OrderedCharset__str.mk(_4mk_all_ordered_charsets.sorted_chars4digit)
ordered_charset4hex = OrderedCharset__str.mk(_4mk_all_ordered_charsets.sorted_chars4hex)

ordered_charset4alpha = OrderedCharset__str.mk(_4mk_all_ordered_charsets.sorted_chars4alpha)
ordered_charset4alnum = OrderedCharset__str.mk(_4mk_all_ordered_charsets.sorted_chars4alnum)

ordered_charset4printable_ascii = OrderedCharset__str.mk(_4mk_all_ordered_charsets.sorted_chars4printable_ascii)
ordered_charset4printable_gb2312 = OrderedCharset__str.mk(_4mk_all_ordered_charsets.sorted_chars4printable_gb2312)

ordered_charset4nonspace_printable_ascii = OrderedCharset__str.mk(_4mk_all_ordered_charsets.sorted_chars4nonspace_printable_ascii)
ordered_charset4nonspace_printable_gb2312 = OrderedCharset__str.mk(_4mk_all_ordered_charsets.sorted_chars4nonspace_printable_gb2312)

ordered_charset4cjk_common_subset_2513_trivial_TS_2227 = OrderedCharset__str.mk(_4mk_all_ordered_charsets.sorted_chars4cjk_common_subset_2513_trivial_TS_2227)
ordered_charset4cjk_common_subset_2513 = OrderedCharset__str.mk(_4mk_all_ordered_charsets.sorted_chars4cjk_common_subset_2513)


_prefix4nm4ordered_charset = 'ordered_charset4'
full_name2ordered_charset = MapView({nm:v for nm, v in globals().items() if is_str(nm) and nm.isidentifier() and nm.startswith(_prefix4nm4ordered_charset)})
#brief name
short_name2ordered_charset = MapView({nm[len(_prefix4nm4ordered_charset):]:v for nm, v in full_name2ordered_charset.items()})















#HHHHH
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
        'sz/uint -> pseudo_random:BiPermutation<sz>'
        mk_random_mod = sf.generate_next_key__uint_mod
        bipermutation = mk_bipermutation(sz, mk_random_mod)
        return bipermutation
#end-class ICipherKeyGenerator(ABC):












#HHHHH
class IHas__modulus(ABC):
    @abstractmethod
    def _get_modulus_(sf, /):
        '-> modulus/uint'
    def get_modulus(sf, /):
        modulus = sf._get_modulus_()
        check_uint(modulus)
        return modulus
class IHas__modulus__bits(IHas__modulus):
    r'''
    modulus =[def]= 2**num_bits
    #'''
    @abstractmethod
    def _get_num_bits_(sf, /):
        '-> num_bits/uint'
    def get_num_bits(sf, /):
        num_bits = sf._get_num_bits_()
        check_uint(num_bits)
        return num_bits
    @override
    def _get_modulus_(sf, /):
        '-> modulus/uint'
        return 1 << sf.get_num_bits()














#HHHHH
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






















class IInnerIndexablePartition_mod(IHas__modulus, IInnerIndexablePartition):
    r'''
    element :: uint%modulus
    modulus =[def]= total_num_elements

    see:IInnerIndexablePartition_mod
    see:Cipher_mod__permutation_partition
    see:Cipher_mod__permutation_partition_fmap
    see:Cipher_bits__permutation
    #'''
    @override
    def _check_element_(sf, element, /):
        super()._check_element_(element)
        modulus = sf.get_modulus()
        check_uint_lt(modulus, element)
    @override
    def _get_modulus_(sf, /):
        '-> modulus/uint'
        total_num_elements = sf.get_total_num_elements()
        modulus = total_num_elements
        return modulus

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

def derived5idx8eqvcls2num_elements(idx8eqvcls2num_elements, /):
    #bug:idx8eqvcls2offset = (*accumulate(idx8eqvcls2num_elements),)
    idx8eqvcls_ex2offset = (0, *accumulate(idx8eqvcls2num_elements),)
    idx8eqvcls2offset = idx8eqvcls_ex2offset[:-1]
    total_num_elements = idx8eqvcls_ex2offset[-1]
    return (idx8eqvcls_ex2offset, idx8eqvcls2offset, total_num_elements)



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
        modulus = sf.get_modulus()
        check_uint_lt(modulus, origin4rngs)
        return origin4rngs
    def get_rng_begin_at(sf, idx8eqvcls, /):
        offset4eqvcls = sf.get_offset4eqvcls_at(idx8eqvcls)
        origin4rngs = sf.get_origin4rngs()
        rng_begin = origin4rngs + offset4eqvcls
        modulus = sf.get_modulus()
        rng_begin %= modulus
        return rng_begin

    @override
    def _element2idx8eqvcls_idx8inner_(sf, element, /):
        '-> (idx8eqvcls, idx8inner)'
        modulus = sf.get_modulus()
        origin4rngs = sf.get_origin4rngs()
        shifted_element = (element - origin4rngs)%modulus

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

        modulus = sf.get_modulus()
        element %= modulus
        return element


    @staticmethod
    def _mk_tables(origin4rngs, idx8eqvcls2num_elements, /):
        check_uint(origin4rngs)
        check_uint_tuple(idx8eqvcls2num_elements)

        (idx8eqvcls_ex2offset, idx8eqvcls2offset, total_num_elements) = derived5idx8eqvcls2num_elements(idx8eqvcls2num_elements)

        modulus = total_num_elements
        origin4rngs = mod__double_width_(modulus, origin4rngs)
        return {**locals()}
    pass


class IInnerIndexablePartition_bits__count_1s(IHas__modulus__bits, IInnerIndexablePartition_mod__lookup_table):
    r'''
    idx8eqvcls =[def]= num_1s
    num_eqvclss =[def]= num_bits+1
    modulus =[def]= 2**num_bits
    #'''
    if 1:
        #!!!conflict!!!
        IHas__modulus__bits._get_modulus_
        IInnerIndexablePartition_mod__lookup_table._get_modulus_
            #IInnerIndexablePartition_mod._get_modulus_

    _get_modulus_ = IHas__modulus__bits._get_modulus_
    _get_total_num_elements_ = IHas__modulus__bits._get_modulus_

    @override
    def _get_num_eqvclss_(sf, /):
        '-> num_eqvclss/uint'
        num_bits = sf.get_num_bits()
        num_eqvclss = num_bits +1
        return num_eqvclss

    @override
    def _get_num_bits_(sf, /):
        '-> num_bits/uint'
        num_eqvclss = IInnerIndexablePartition_mod__lookup_table._get_num_eqvclss_(sf)
        num_bits = num_eqvclss -1

        if 1:
            total_num_elements = IInnerIndexablePartition_mod__lookup_table._get_total_num_elements_(sf)
            if not total_num_elements==1<<num_bits: raise logic-err

        return num_bits
        return sf.get_num_eqvclss()-1
        return sf.num_bits

    r'''
    @override
    def _get_num_elements_at_(sf, idx8eqvcls, /):
        '-> num_elements<eqvclss[idx8eqvcls]>/uint'
        return sf.idx8eqvcls2num_elements[idx8eqvcls]
        num_1s = idx8eqvcls
        num_bits = sf.get_num_bits()
        #!!!slow!!!
        return C(num_bits, num_1s)

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
        num_bits = len(bs)
        acc = 0
        while num_1s:
            b = bs.pop()
            if not b=='1':continue
            num_bits = len(bs)
                #may: [num_1s==num_bits+1]==>>[weight==0]
            weight = C(num_bits, num_1s)
            num_1s -= 1
            assert 0 <= num_1s <= num_bits

            acc += weight
        idx8inner = acc
            ## '1'*k + '0'*(n-k) ==>> C(n,k)-1 == idx8inner == sum C(n-1-i,k-i) {i<-[0..k-1]}
        return idx8eqvcls, idx8inner




    @override
    def _element5idx8eqvcls_idx8inner_(sf, idx8eqvcls, idx8inner, /):
        '-> element'
        num_1s = idx8eqvcls
        num_bits = sf.get_num_bits()
        bs = ['0']*num_bits

        acc = idx8inner
        while num_1s:
            _, j = bisearch(acc, range(num_bits), key=lambda i:C(i, num_1s))
                # virtual array = [C(i, num_1s) | i<-[0..num_bits-1]]
            i = j-1
            bs[i] = '1'
            weight = C(i, num_1s)
            num_bits = i
            num_1s -= 1
            acc -= weight
        if not acc == 0:raise logic-err
        bs = ''.join(reversed(bs))
        u = int(bs, 2)
        return u


    @staticmethod
    def _mk_tables(num_bits, /):
        check_uint(num_bits)
        num_eqvclss = num_bits+1

        idc8eqvcls = range(num_eqvclss)
        idx8eqvcls2num_elements = tuple(C(num_bits, num_1s) for num_1s in idc8eqvcls)
        (idx8eqvcls_ex2offset, idx8eqvcls2offset, total_num_elements) = derived5idx8eqvcls2num_elements(idx8eqvcls2num_elements)
        if not total_num_elements == 1<<num_bits:raise logic-err

        return {**locals()}
        return (num_bits, num_eqvclss, total_num_elements, idc8eqvcls), (idx8eqvcls2num_elements, idx8eqvcls2offset)






class InnerIndexablePartition_mod__rng8eqvcls(IEase_repr_init, IInnerIndexablePartition_mod__rng8eqvcls):

    def __init__(sf, /, *, origin4rngs, idx8eqvcls2num_elements):
        check_uint(origin4rngs)
        check_uint_tuple(idx8eqvcls2num_elements)
        d = IInnerIndexablePartition_mod__rng8eqvcls._mk_tables(origin4rngs, idx8eqvcls2num_elements)

        checkT__eq(d['origin4rngs'])(origin4rngs)
        sf._O_idx8eqvcls2offset = d['idx8eqvcls2offset']

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
        return sf._O_idx8eqvcls2offset

InnerIndexablePartition_mod__rng8eqvcls.mk(origin4rngs=3, idx8eqvcls2num_elements=(3,4,5))




class InnerIndexablePartition_bits__count_1s(IEase_repr_init, IInnerIndexablePartition_bits__count_1s):
    def __init__(sf, /, *, num_bits):
        check_uint(num_bits)
        d = IInnerIndexablePartition_bits__count_1s._mk_tables(num_bits)
        #sf.__dict__.update(d)
        sf._O_idx8eqvcls2num_elements = d['idx8eqvcls2num_elements']
        sf._O_idx8eqvcls2offset = d['idx8eqvcls2offset']
        assert num_bits == sf.get_num_bits()

    r'''
    @override
    def _get_num_bits_(sf, /):
        '-> num_bits/uint'
        return sf.num_bits
    #'''

    @override
    def _get_idx8eqvcls2num_elements_(sf, /):
        '-> idx8eqvcls2num_elements'
        return sf._O_idx8eqvcls2num_elements
    @override
    def _get_idx8eqvcls2offset_(sf, /):
        '-> idx8eqvcls2offset'
        return sf._O_idx8eqvcls2offset

InnerIndexablePartition_bits__count_1s.mk(num_bits=6)



























































#HHHHH
class ICipher(ABC):
    r'''
    encrypt is invertible/injective
        but decrypt... may be not injective
    decrypt is surjective

    eg.
        encrypt ::int -> int
        encrypt i = 2*i
        decrypt ::int -> int
        decrypt i = n//2

    #'''

    @abstractmethod
    def _encrypt_(sf, clear_text, /):
        'clear_text -> cipher_text'
    @abstractmethod
    def _decrypt_(sf, cipher_text, /):
        'cipher_text -> clear_text'
    def _check_clear_text_(sf, clear_text, /):
        pass
    def _check_cipher_text_(sf, cipher_text, /):
        pass




    def encrypt(sf, clear_text, /, *, validate):
        sf.check_clear_text(clear_text)
        cipher_text = sf._encrypt_(clear_text)
        sf.check_cipher_text(cipher_text)

        if validate:
            if not clear_text == sf._decrypt_(cipher_text):raise logic-err
        return cipher_text

    def decrypt(sf, cipher_text, /):
        'no kw"validate", since may add random paddings when encrypt'
        sf.check_cipher_text(cipher_text)
        clear_text = sf._decrypt_(cipher_text)
        sf.check_clear_text(clear_text)
        return clear_text

    def check_clear_text(sf, clear_text, /):
        sf._check_clear_text_(clear_text)
    def check_cipher_text(sf, cipher_text, /):
        sf._check_cipher_text_(cipher_text)




class ICipher__with_cipher_key_generator(ICipher):
    @abstractmethod
    def _get_cipher_key_generator_(sf, /):
        '-> ICipherKeyGenerator/str'
    def get_cipher_key_generator(sf, /):
        return sf._get_cipher_key_generator_()
    def get_prefix4key(sf, /):
        return sf.get_cipher_key_generator().get_prefix4key()


#check subtype: domain>=codomain
class IEndoCipher(ICipher):
    r'''
    encrypt :: a -> a

    image<encrypt> |<=| codomain<encrypt> === domain<encrypt>
        Set<cipher_text> |<=| Set<clear_text>


    encrypt is invertible/injective
    endofunction =?= surjective endofunction
        No.
        encrypt :: int -> int
        encrypt i = 2*i
        encrypt is endofunction
        encrypt is not surjective
        image<encrypt> === even |<| int === codomain<encrypt>

    #'''
    @override
    def _check_cipher_text_(sf, cipher_text, /):
        super()._check_cipher_text_(cipher_text)
        sf._check_clear_text_(cipher_text)
        sf._check_cipher_text_finer_than_clear_text_(cipher_text)
    def _check_cipher_text_finer_than_clear_text_(sf, cipher_text, /):
        pass


#check subtype: domain==image/range
class IPermutatoryCipher(IEndoCipher):
#class ISurjectiveEndoCipher(IEndoCipher):
    r'''
    encrypt :: a -> a

    image<encrypt> |==| codomain<encrypt> === domain<encrypt>
        Set<cipher_text> |==| Set<clear_text>


    encrypt is invertible/injective
    surjective endofunction =?= permutation
        No.
        f :: int -> int
        f i = i//2
        f is surjective endofunction
        f is not injective
        f is not permutatory
    but since encrypt is injective:
    ==>> encrypt is permutation

    IPermutatoryCipher===ISurjectiveEndoCipher


    #'''

    @final
    @override
    def _check_cipher_text_(sf, cipher_text, /):
        #bug:super()._check_cipher_text_(cipher_text)
        sf._check_clear_text_(cipher_text)

    @final
    @override
    def _check_cipher_text_finer_than_clear_text_(sf, cipher_text, /):
        raise logic-err



#HHHHH
class ICipher_mod(IHas__modulus, IPermutatoryCipher):
    @override
    def _check_clear_text_(sf, clear_text, /):
        super()._check_clear_text_(clear_text)
        u = clear_text
        modulus = sf.get_modulus()
        check_uint_lt(modulus, u)
        return

    r'''
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
        v = sf._wrap_op_with_mod_check(sf._encrypt_mod_, u)
        cipher_text = v
        return cipher_text

    @override
    def _decrypt_(sf, cipher_text, /):
        'cipher_text -> clear_text'
        v = cipher_text
        u = sf._wrap_op_with_mod_check(sf._decrypt_mod_, v)
        clear_text = u
        return clear_text

.+1,$s/def _encrypt_mod_(/def _encrypt_(/g
    #))
.+1,$s/def _decrypt_mod_(/def _decrypt_(/g
    #))
    #'''

class ICipher_bits(IHas__modulus__bits, ICipher_mod):
    pass

#HHHHH
class IInvolutoryCipher(IPermutatoryCipher):
    'involution: decrypt===encrypt'
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


class IInvolutoryCipher_mod(IInvolutoryCipher, ICipher_mod):
    ''
    if 0: r'''
    if 1:
        #!!!conflict!!!
        IInvolutoryCipher_mod._encrypt_
        IInvolutoryCipher_mod._decrypt_
        ICipher_mod._encrypt_
        ICipher_mod._decrypt_

    _encrypt_ = ICipher_mod._encrypt_
    _decrypt_ = ICipher_mod._decrypt_
    _encrypt_mod_ = IInvolutoryCipher_mod._encrypt_
    _decrypt_mod_ = IInvolutoryCipher_mod._decrypt_

    @abstractmethod
    def _en_de_cipher_op_mod_(sf, u, /):
        'uint%M -> uint%M'
    #def en_de_cipher_op_mod(sf, u, /, *, validate): return sf.encrypt(u, validate=validate)
    @override
    def _en_de_cipher_op_(sf, a, /):
        'a -> a'
        a = sf._wrap_op_with_mod_check(sf._en_de_cipher_op_mod_, a)
        return a
        return sf._en_de_cipher_op_mod_(a)
    #'''

class IInvolutoryCipher_bits(IInvolutoryCipher_mod, ICipher_bits):
    ''























#HHHHH
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
    ''
    #xxxx TODO ....
    #......  ...... dynamic property instead of py-type
    if 0: r'''
    _encrypt_ = ICipher_mod._encrypt_
    _decrypt_ = ICipher_mod._decrypt_
    _encrypt_mod_ = Cipher__chain._encrypt_
    _decrypt_mod_ = Cipher__chain._decrypt_
    #'''

    def __init__(sf, /, *, ciphers):
        super().__init__(ciphers=ciphers)

        if not all(isinstance(cipher, ICipher_mod) for cipher in ciphers):raise TypeError
        if not ciphers:raise TypeError
        M = ciphers[0].get_modulus()
        if not all(cipher.get_modulus()==M for cipher in ciphers):raise TypeError


    @override
    def _get_modulus_(sf, /):
        '-> modulus/uint'
        return sf.ciphers[0].get_modulus()


class InvolutoryCipher__chain(IEase_repr, IInvolutoryCipher):
    'not subclass of Cipher__chain'
    @classmethod
    def mk_Cipher__chain(cls, ciphers, /):
        cipherR = Cipher__chain.mk(ciphers=ciphers)
        return cipherR
    @classmethod
    @override
    def _mk_kwargs4init_(cls, /, *, involutory_cipher, ciphersR):
        '-> __init__.kwargs'
        cipherR = cls.mk_Cipher__chain(ciphersR)
        return dict(involutory_cipher=involutory_cipher, cipherR=cipherR)

    def __init__(sf, /, *, involutory_cipher, cipherR):
        if not isinstance(involutory_cipher, IInvolutoryCipher):raise TypeError
        if not isinstance(cipherR, ICipher):raise TypeError

    @override
    def _en_de_cipher_op_(sf, a, /):
        'a -> a'
        b = sf.cipherR.encrypt(a, validate=False)
        c = sf.involutory_cipher.en_de_cipher_op(b, validate=False)
        d = sf.cipherR.decrypt(c)
        return d



class InvolutoryCipher_mod__chain(InvolutoryCipher__chain, IEase_repr, IInvolutoryCipher_mod):
    if 0: r'''
    _en_de_cipher_op_ = IInvolutoryCipher_mod._en_de_cipher_op_
    _en_de_cipher_op_mod_ = InvolutoryCipher__chain._en_de_cipher_op_
    #'''

    @classmethod
    @override
    def mk_Cipher__chain(cls, ciphers, /):
        cipherR = Cipher_mod__chain.mk(ciphers=ciphers)
        return cipherR

    def __init__(sf, /, *, involutory_cipher, cipherR):
        super().__init__(involutory_cipher=involutory_cipher, cipherR=cipherR)

        involutory_cipher_mod = involutory_cipher
        cipherR_mod = cipherR
        del involutory_cipher, cipherR

        if not isinstance(involutory_cipher_mod, IInvolutoryCipher_mod):raise TypeError
        if not isinstance(cipherR_mod, ICipher_mod):raise TypeError
        if not involutory_cipher_mod.get_modulus()==cipherR_mod.get_modulus():raise TypeError

    @override
    def _get_modulus_(sf, /):
        '-> modulus/uint'
        return sf.involutory_cipher.get_modulus()





#HHHHH
class InvolutoryCipher_mod__flip_parity(IEase_repr_init, IInvolutoryCipher_mod):
    'even <-> old'
    def __init__(sf, /, *, modulus):
        check_uint(modulus)

    @override
    def _get_modulus_(sf, /):
        '-> modulus/uint'
        return sf.modulus
    @override
    def _en_de_cipher_op_(sf, u, /):
        'uint%M -> uint%M'
        v = u ^ 1
        if v == sf.modulus:
            v = u
        #_saved_print(sf.modulus, u, v)
        return v



class InvolutoryCipher_mod__subtracted_by(IEase_repr, IInvolutoryCipher_mod):
    'o =[%M]= k - i'
    @classmethod
    @override
    def _mk_kwargs4init_(cls, /, *, modulus, minuend_or_ver='ver1__mul1573div1987'):
        '-> __init__.kwargs'
        if is_str(minuend_or_ver):
            ver = minuend_or_ver
            minuend = cls.mk_minuend(modulus, ver=ver)
        else:
            minuend = minuend_or_ver
        return dict(minuend=minuend, modulus=modulus)
    @classmethod
    def mk_minuend(cls, modulus, /, *, ver):
        r'''
        [x =[%M]= m-x]
        <==> [2*x =[%M]= m]
        ==>> [M%2==1]or[m%2==0]
        #'''
        if ver == 'ver1__mul1573div1987':
            minuend = modulus*1573//1987
            if modulus%2==0 and minuend%2==0:
                minuend += 1
            minuend -= modulus
        else:
            cls
            raise NotImplementedError(f'{cls}.ver=={ver!r}')
        return minuend
    def __init__(sf, /, *, minuend, modulus):
        check_uint(modulus)
        check_int(minuend)
        if not -modulus <= minuend <= modulus:raise TypeError
            # to allow (-1) instead of (M-1)
            # see:mod__double_width_
        pass
    @override
    def _get_modulus_(sf, /):
        '-> modulus/uint'
        return sf.modulus
    @override
    def _en_de_cipher_op_(sf, u, /):
        'uint%M -> uint%M'
        #v = sf.modulus -1 -u
        v = (sf.minuend-u) %sf.modulus
        return v

class InvolutoryCipher_mod__modulus_is_1(IEase_repr_init, IInvolutoryCipher_mod):
    def __init__(sf, /):
        pass
    @override
    def _get_modulus_(sf, /):
        '-> modulus/uint'
        return 1
    @override
    def _en_de_cipher_op_(sf, u, /):
        'uint%M -> uint%M'
        checkT__eq(0)(u)
        v = u
        return v
involutory_cipher_mod__modulus_is_1 = InvolutoryCipher_mod__modulus_is_1()

class Cipher_mod__fmap_bit_op_on_tail_bits(IEase_repr_init, ICipher_mod):
    def __init__(sf, /, *, mk_ICipher5len_bits, modulus):
        check_uint(modulus)
        check_callable(mk_ICipher5len_bits)
    @override
    def _get_modulus_(sf, /):
        '-> modulus/uint'
        return sf.modulus


    def _check_cipher_mod_(sf, len_bits, modulus, cipher_mod, /):
        checkT__type_le(ICipher_mod)(cipher_mod)
        checkT__eq(modulus)(cipher_mod.get_modulus())

    def check_cipher_mod(sf, len_bits, modulus, cipher_mod, /):
        sf._check_cipher_mod_(len_bits, modulus, cipher_mod)



    def _preprocess(sf, w, /):
        M = sf.modulus
        _1_masked_tail_bits = w ^ M
        assert _1_masked_tail_bits
        len_bits = floor_log2(_1_masked_tail_bits)
        MSB = 1 << len_bits
        _masked_tail_bits = MSB ^ _1_masked_tail_bits
        assert 0 <= _masked_tail_bits < MSB

        if not MSB == 1:
            cipher_mod = sf.mk_ICipher5len_bits(len_bits)
        else:
            cipher_mod = involutory_cipher_mod__modulus_is_1

        sf.check_cipher_mod(len_bits, MSB, cipher_mod)
        if not cipher_mod.get_modulus()==MSB: raise TypeError
        return _masked_tail_bits, len_bits, MSB, cipher_mod

    def _postprocess(sf, _masked_tail_bits, len_bits, MSB, cipher_mod, /):
        M = sf.modulus
        _1_masked_tail_bits = MSB ^ _masked_tail_bits
        w = _1_masked_tail_bits ^ M
        return w

    @override
    def _encrypt_(sf, u, /):
    #def _encrypt_mod_(sf, u, /):
        'uint%M -> uint%M'
        u_masked_tail_bits, len_bits, MSB, cipher_mod = sf._preprocess(u)

        v_masked_tail_bits = cipher_mod.encrypt(u_masked_tail_bits, validate=False)

        v = sf._postprocess(v_masked_tail_bits, len_bits, MSB, cipher_mod)
        return v

    @override
    def _decrypt_(sf, v, /):
    #def _decrypt_mod_(sf, v, /):
        'uint%M -> uint%M'
        v_masked_tail_bits, len_bits, MSB, cipher_mod = sf._preprocess(v)

        u_masked_tail_bits = cipher_mod.decrypt(v_masked_tail_bits)

        u = sf._postprocess(u_masked_tail_bits, len_bits, MSB, cipher_mod)
        return u

class InvolutoryCipher_mod__fmap_bit_op_on_tail_bits(Cipher_mod__fmap_bit_op_on_tail_bits, IInvolutoryCipher_mod):
    _encrypt_ = IInvolutoryCipher._encrypt_
    _decrypt_ = IInvolutoryCipher._decrypt_
    _en_de_cipher_op_ = Cipher_mod__fmap_bit_op_on_tail_bits._decrypt_

    @override
    def _check_cipher_mod_(sf, len_bits, modulus, cipher_mod, /):
        super()._check_cipher_mod_(len_bits, modulus, cipher_mod)
        #checkT__type_le(IInvolutoryCipher)(cipher_mod)
        #   偶然关联？
        checkT__type_le(IInvolutoryCipher_mod)(cipher_mod)

    r'''
    @override
    def _en_de_cipher_op_(sf, u, /):
        'uint%M -> uint%M'
        return v
    #'''








#HHHHH
class Cipher_mod__mask(IEase_repr_init, ICipher_mod):
    def __init__(sf, /, *, cipher_mod, modulus):
        checkT__type_le(ICipher_mod)(cipher_mod)
        check_uint(modulus)
        if not cipher_mod.get_modulus() <= modulus:raise TypeError
            # "<=": cut data_space into low/high parts, low part transform, high leave unchanged
    @override
    def _get_modulus_(sf, /):
        '-> modulus/uint'
        return sf.modulus
    @override
    def _encrypt_(sf, u, /):
        'uint%M -> uint%M'
        cipher_mod = sf.cipher_mod
        m = cipher_mod.get_modulus()
        if u < m:
            v = cipher_mod.encrypt(u, validate=False)
        else:
            v = u
        return v

    @override
    def _decrypt_(sf, v, /):
        'uint%M -> uint%M'
        cipher_mod = sf.cipher_mod
        m = cipher_mod.get_modulus()
        if v < m:
            u = cipher_mod.decrypt(v)
        else:
            u = v
        return u



class Cipher_mod__add_then_mul(IEase_repr, ICipher_mod):
    @classmethod
    @override
    def _mk_kwargs4init_(cls, /, *, key4add, key4mul, modulus):
        '-> __init__.kwargs'
        inv4key4mul = invmod(key4mul, modulus)
        return dict(key4add=key4add, key4mul=key4mul, inv4key4mul=inv4key4mul, modulus=modulus)

    def __init__(sf, /, *, key4add, key4mul, inv4key4mul, modulus):
        if not key4mul*inv4key4mul%modulus == 1:raise TypeError
        pass
    @override
    def _get_modulus_(sf, /):
        '-> modulus/uint'
        return sf.modulus
    @override
    def _encrypt_(sf, u, /):
        'uint%M -> uint%M'
        v = (u+sf.key4add)*sf.key4mul%sf.modulus
        return v

    @override
    def _decrypt_(sf, v, /):
        'uint%M -> uint%M'
        u = (v*sf.inv4key4mul-sf.key4add)%sf.modulus
        return u

class Cipher_mod__rotate(IEase_repr, ICipher_mod):
    @classmethod
    def mk_N1_N2(cls, modulus, /, *, N_or_ver):
        if is_str(N_or_ver):
            ver = N_or_ver
            if ver == 'ver1__mul233div377':
                N = modulus *233 //377
            else:
                cls
                raise NotImplementedError(f'{cls}.ver=={ver!r}')
        else:
            N = N_or_ver
        N %= modulus
        N_ = modulus - N
            # N=0, N_=M
        N1 = min(N, N_)
        N2 = max(N, N_)
        assert 0 <= N1 <= N2 <= N1+N2 == modulus
        return N1, N2

    @classmethod
    @override
    def _mk_kwargs4init_(cls, /, *, modulus, N_or_ver='ver1__mul233div377'):
        '-> __init__.kwargs'
        N1, N2 = cls.mk_N1_N2(modulus, N_or_ver=N_or_ver)
        if not 2 < N1 < N1+2 <= N2 < N2+2 <modulus:raise ValueError(f'modulus too small?: {modulus!r}: {N2},{N1}')
        return dict(N1 = N1, N2 = N2, modulus = modulus)
    def __init__(sf, /, *, N1, N2, modulus):
        if not N1+N2 == modulus:raise TypeError
        if not 2 < N1 < N1+2 <= N2 < N2+2 <modulus:raise TypeError

    @override
    def _get_modulus_(sf, /):
        '-> modulus/uint'
        return sf.modulus
    @override
    def _encrypt_(sf, u, /):
        'uint%M -> uint%M'
        N1 = sf.N1
        N2 = sf.N2
        M = sf.modulus

        if u < N1:
            v = u+N2
        elif u < N2:
            v = N2-1-u
        else:
            v = 2*N2-1-u
        return v

    @override
    def _decrypt_(sf, v, /):
        'uint%M -> uint%M'
        N1 = sf.N1
        N2 = sf.N2
        M = sf.modulus

        if v >= N2:
            u = v-N2
        elif v < N2-N1:
            u = N2-1-v
        else:
            u = 2*N2-1-v
        return u

class Cipher_mod__permutation_partition(IEase_repr_init, ICipher_mod):
    r'''
    see:IInnerIndexablePartition_mod
    see:Cipher_mod__permutation_partition
    see:Cipher_mod__permutation_partition_fmap
    see:Cipher_bits__permutation
    #'''
    def __init__(sf, /, *, inner_indexable_partition_mod, bipermutation):
        checkT__type_le(IInnerIndexablePartition_mod)(inner_indexable_partition_mod)
        checkT__type_is(BiPermutation)(bipermutation)

        if not len(bipermutation.old2new) == inner_indexable_partition_mod.get_num_eqvclss():raise TypeError

        old2new = sf.bipermutation.old2new
        new2old = sf.bipermutation.new2old
        pn4eqvcls = sf.inner_indexable_partition_mod
        #old/eqvcls <-> new/slot
        idx8tmp_slot2num_elements = (*map(pn4eqvcls.get_num_elements_at, new2old),)
        sf._O_pn4tmp_slot = InnerIndexablePartition_mod__rng8eqvcls.mk(origin4rngs=0, idx8eqvcls2num_elements=idx8tmp_slot2num_elements)
        pn4tmp_slot = sf.pn4tmp_slot



    @override
    def _get_modulus_(sf, /):
        '-> modulus/uint'
        return sf.inner_indexable_partition_mod.get_modulus()

    @override
    def _encrypt_(sf, u, /):
        'uint%M -> uint%M'
        old2new = sf.bipermutation.old2new
        new2old = sf.bipermutation.new2old
        pn4eqvcls = sf.inner_indexable_partition_mod
        pn4tmp_slot = sf.pn4tmp_slot

        (old_idx8eqvcls, old_idx8inner) = pn4eqvcls.element2idx8eqvcls_idx8inner(u, validate=False)

        new_idx8tmp_slot = old2new[old_idx8eqvcls]
        if 0:
            new_idx8inner = old_idx8inner
            #here can insert a fmapT Cipher_mod<old_idx8eqvcls, %num_elements<old_idx8eqvcls>>
        else:
            new_idx8inner = sf._encrypt_mod4eqvcls_at_(old_idx8eqvcls, old_idx8inner)

        v = pn4tmp_slot.element5idx8eqvcls_idx8inner(new_idx8tmp_slot, new_idx8inner, validate=False)
        new_offset8tmp_slot = pn4tmp_slot.get_offset4eqvcls_at(new_idx8tmp_slot)
        v = new_offset8tmp_slot + new_idx8inner
        return v

    def _encrypt_mod4eqvcls_at_(sf, old_idx8eqvcls, old_idx8inner, /):
        '-> new_idx8inner'
        new_idx8inner = old_idx8inner
        return new_idx8inner

    def _decrypt_mod4eqvcls_at_(sf, old_idx8eqvcls, new_idx8inner, /):
        '-> old_idx8inner'
        old_idx8inner = new_idx8inner
        return old_idx8inner

    @override
    def _decrypt_(sf, v, /):
        'uint%M -> uint%M'
        old2new = sf.bipermutation.old2new
        new2old = sf.bipermutation.new2old
        pn4eqvcls = sf.inner_indexable_partition_mod
        pn4tmp_slot = sf.pn4tmp_slot
        (new_idx8tmp_slot, new_idx8inner) = pn4tmp_slot.element2idx8eqvcls_idx8inner(v, validate=False)

        old_idx8eqvcls = new2old[new_idx8tmp_slot]
        if 0:
            old_idx8inner = new_idx8inner
            #here can insert a fmapT Cipher_mod<old_idx8eqvcls, %num_elements<old_idx8eqvcls>>
        else:
            old_idx8inner = sf._decrypt_mod4eqvcls_at_(old_idx8eqvcls, new_idx8inner)

        u = pn4eqvcls.element5idx8eqvcls_idx8inner(old_idx8eqvcls, old_idx8inner, validate=False)
        return u
#end-class Cipher_mod__permutation_partition(IEase_repr_init, ICipher_mod):

class Cipher_mod__permutation_partition_fmap(Cipher_mod__permutation_partition):
    def __init__(sf, /, *, inner_indexable_partition_mod, bipermutation, idx8eqvcls2may_cipher_mod4fmap):
        super().__init__(inner_indexable_partition_mod=inner_indexable_partition_mod, bipermutation=bipermutation)
        check_tuple(idx8eqvcls2may_cipher_mod4fmap)
        #checkT__pattern_list(checkT__type_le(ICipher_mod))(idx8eqvcls2may_cipher_mod4fmap)
        pn4eqvcls = sf.inner_indexable_partition_mod
        num_eqvclss = pn4eqvcls.get_num_eqvclss()
        if not len(idx8eqvcls2may_cipher_mod4fmap)==num_eqvclss:raise TypeError

        for idx8eqvcls, may_cipher_mod_at in enumerate(idx8eqvcls2may_cipher_mod4fmap):
            if may_cipher_mod_at is None: continue
            cipher_mod_at = may_cipher_mod_at
            checkT__type_le(ICipher_mod)(cipher_mod_at)

            num_elements_at = pn4eqvcls.get_num_elements_at(idx8eqvcls)
            modulus_at = num_elements_at
            if not cipher_mod_at.get_modulus() == modulus_at:raise TypeError

    @override
    def _encrypt_mod4eqvcls_at_(sf, old_idx8eqvcls, old_idx8inner, /):
        '-> new_idx8inner'
        may_cipher_mod_at = sf.idx8eqvcls2may_cipher_mod4fmap[old_idx8eqvcls]
        if may_cipher_mod_at is None:
            new_idx8inner = old_idx8inner
        else:
            cipher_mod_at = may_cipher_mod_at
            new_idx8inner = cipher_mod_at.encrypt(old_idx8inner, validate=False)
        return new_idx8inner

    @override
    def _decrypt_mod4eqvcls_at_(sf, old_idx8eqvcls, new_idx8inner, /):
        '-> old_idx8inner'
        may_cipher_mod_at = sf.idx8eqvcls2may_cipher_mod4fmap[old_idx8eqvcls]
        if may_cipher_mod_at is None:
            old_idx8inner = new_idx8inner
        else:
            cipher_mod_at = may_cipher_mod_at
            old_idx8inner = cipher_mod_at.decrypt(new_idx8inner)
        return old_idx8inner
#end-class Cipher_mod__permutation_partition_fmap(Cipher_mod__permutation_partition):




#HHHHH
class Cipher_bits__permutation(IEase_repr_init, ICipher_bits):
    r'''
    defect:all 0s/1s are fixed point
    defect:uniform sampling of permutations are not good to be used as shuffle
    #
    see:IInnerIndexablePartition_mod
    see:Cipher_mod__permutation_partition
    see:Cipher_bits__permutation
    #'''
    def __init__(sf, /, *, bipermutation):
        checkT__type_is(BiPermutation)(bipermutation)

    @override
    def _get_num_bits_(sf, /):
        '-> num_bits/uint'
        return len(sf.bipermutation.old2new)

    @override
    def _encrypt_(sf, u, /):
        'uint%M -> uint%M'
        num_bits = sf.get_num_bits()
        v = perform_basic_permutation__inv__uint8bits(sf.bipermutation.new2old, num_bits, u)
        return v

    @override
    def _decrypt_(sf, v, /):
        'uint%M -> uint%M'
        num_bits = sf.get_num_bits()
        u = perform_basic_permutation__inv__uint8bits(sf.bipermutation.old2new, num_bits, v)
        return u
class InvolutoryCipher_bits__xor(IEase_repr_init, IInvolutoryCipher_bits):
#class InvolutoryCipher_bits__xor(IEase_repr_init, ICipher_bits):
    r'''
    defect:uniform distribution is not good to be used as cipher
        n = randrange(L*23//61, L*43//61)
        permutate/shuffle('0'*n+'1'*(L-n))
            #always roughly half 0s and half 1s
    #'''
    def __init__(sf, /, *, key4xor:'uint8bits', num_bits):
        assert 0 <= key4xor < 1<<num_bits

    @override
    def _get_num_bits_(sf, /):
        '-> num_bits/uint'
        return sf.num_bits
    @override
    def _en_de_cipher_op_(sf, a, /):
        'a -> a'
        b = a ^ sf.key4xor
        return b

    r'''
    @override
    def _encrypt_(sf, u, /):
        'uint%M -> uint%M'
        v = u ^ sf.key4xor
        return v

    @override
    def _decrypt_(sf, v, /):
        'uint%M -> uint%M'
        u = v ^ sf.key4xor
        return u
    #'''


#已有permutation:class Cipher_bits__rotate(IEase_repr, ICipher_bits):
class Cipher_bits__accumulate_xor_reversed(IEase_repr_init, ICipher_bits):
    r'''
    defect:all 0s are fixed point
    #'''
    def __init__(sf, /, *, num_bits):
        pass

    @override
    def _get_num_bits_(sf, /):
        '-> num_bits/uint'
        return sf.num_bits

    @override
    def _encrypt_(sf, u, /):
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

        num_bits = sf.get_num_bits()
        bs = uint2bits(num_bits, u)
        _01s = map(int, reversed(bs))
        _01s = accumulate(_01s, operator.__xor__)
        bs = ''.join(map(str, _01s))
        v = int(bs, 2)
        return v

    @override
    def _decrypt_(sf, v, /):
        'uint%M -> uint%M'
        num_bits = sf.get_num_bits()
        bs = uint2bits(num_bits, v)
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





































#HHHHH
def _test_ICipher_mod(cls, /, **kwargs):
    print(cls, kwargs)
    sf = cls.mk(**kwargs)
    print(sf)

    M = sf.get_modulus()
    num_bits = (M-1).bit_length() if M else 1
    for u in range(M):
        v = sf.encrypt(u, validate=True)
        print(u, v)
        print('  ', uint2bits(num_bits, u))
        print('  ', uint2bits(num_bits, v))
        if not u == sf.decrypt(v): raise logic-err

def _test_Cipher_mod__rotate():
    cls = Cipher_mod__rotate
    _test_ICipher_mod(cls, modulus=15)
def _test_Cipher_mod__add_then_mul():
    cls = Cipher_mod__add_then_mul
    _test_ICipher_mod(cls, modulus=15, key4add=7, key4mul=2)#, inv4key4mul=8
_test_Cipher_mod__rotate()
_test_Cipher_mod__add_then_mul()

def _test_Cipher_bits__permutation():
    cls = Cipher_bits__permutation
    num_bits = 4
    bipermutation = mk_bipermutation(num_bits, randrange)
    _test_ICipher_mod(cls, bipermutation=bipermutation)
    bipermutation = mk_bipermutation(num_bits, randbelow)
    _test_ICipher_mod(cls, bipermutation=bipermutation)
def _test_InvolutoryCipher_bits__xor():
    cls = InvolutoryCipher_bits__xor
    num_bits = 4
    key4xor = getrandbits(num_bits)
    _test_ICipher_mod(cls, key4xor=key4xor, num_bits=num_bits)
    key4xor = randbits(num_bits)
    _test_ICipher_mod(cls, key4xor=key4xor, num_bits=num_bits)
def _test_Cipher_bits__accumulate_xor_reversed():
    cls = Cipher_bits__accumulate_xor_reversed
    num_bits = 4
    _test_ICipher_mod(cls, num_bits=num_bits)

_test_Cipher_bits__permutation()
_test_InvolutoryCipher_bits__xor()
_test_Cipher_bits__accumulate_xor_reversed()
def _test_Cipher_mod__mask():
    cls = Cipher_mod__mask
    num_bits = 4
    cipher_mod = Cipher_bits__accumulate_xor_reversed.mk(num_bits=num_bits)
    _test_ICipher_mod(cls, cipher_mod=cipher_mod, modulus=31)
_test_Cipher_mod__mask()

def _test_Cipher_mod__chain():
    cls = Cipher_mod__chain
    num_bits = 4
    cipher_bits__accumulate_xor_reversed = Cipher_bits__accumulate_xor_reversed.mk(num_bits=num_bits)

    M = cipher_bits__accumulate_xor_reversed.get_modulus()
    cipher_mod__rotate = Cipher_mod__rotate.mk(modulus=M)

    ciphers = (cipher_mod__rotate, cipher_bits__accumulate_xor_reversed)
    _test_ICipher_mod(cls, ciphers=ciphers)
_test_Cipher_mod__chain()


def _test_InvolutoryCipher_mod__flip_parity():
    cls = InvolutoryCipher_mod__flip_parity
    _test_ICipher_mod(cls, modulus=15)
_test_InvolutoryCipher_mod__flip_parity()


def _test_InvolutoryCipher_mod__subtracted_by():
    cls = InvolutoryCipher_mod__subtracted_by
    _test_ICipher_mod(cls, modulus=15)
_test_InvolutoryCipher_mod__subtracted_by()


def _test_Cipher_mod__fmap_bit_op_on_tail_bits():
    cls = Cipher_mod__fmap_bit_op_on_tail_bits
    def _mk_ICipher5len_bits(len_bits, /):
        return Cipher_mod__add_then_mul.mk(modulus=1<<len_bits, key4add=3, key4mul=5)
        return Cipher_mod__rotate.mk(modulus=1<<len_bits)
    _test_ICipher_mod(cls, modulus=15, mk_ICipher5len_bits=_mk_ICipher5len_bits)
_test_Cipher_mod__fmap_bit_op_on_tail_bits()

def _default_mk_InvolutoryCipher5len_bits(len_bits, /):
    return InvolutoryCipher_mod__subtracted_by.mk(modulus=1<<len_bits)
def _test_InvolutoryCipher_mod__fmap_bit_op_on_tail_bits():
    cls = InvolutoryCipher_mod__fmap_bit_op_on_tail_bits
    _test_ICipher_mod(cls, modulus=15, mk_ICipher5len_bits=_default_mk_InvolutoryCipher5len_bits)
_test_InvolutoryCipher_mod__fmap_bit_op_on_tail_bits()



def _test_InvolutoryCipher_mod__chain():
    cls = InvolutoryCipher_mod__chain

    num_bits = 4
    cipher_bits__accumulate_xor_reversed = Cipher_bits__accumulate_xor_reversed.mk(num_bits=num_bits)

    M = cipher_bits__accumulate_xor_reversed.get_modulus()
    cipher_mod__rotate = Cipher_mod__rotate.mk(modulus=M)

    ciphersR = (cipher_mod__rotate, cipher_bits__accumulate_xor_reversed)

    involutory_cipher_mod = InvolutoryCipher_mod__subtracted_by.mk(modulus=M)

    _test_ICipher_mod(cls, involutory_cipher=involutory_cipher_mod, ciphersR=ciphersR)
_test_InvolutoryCipher_mod__chain()

def _test_Cipher_mod__permutation_partition():
    cls = Cipher_mod__permutation_partition
    origin4rngs = 4
    idx8eqvcls2num_elements = (1, 2, 3, 4, 5, 3)
    num_eqvclss = len(idx8eqvcls2num_elements)
    bipermutation = mk_bipermutation(num_eqvclss, randrange)
    pn = InnerIndexablePartition_mod__rng8eqvcls.mk(origin4rngs=origin4rngs, idx8eqvcls2num_elements=idx8eqvcls2num_elements)
    _test_ICipher_mod(cls, inner_indexable_partition_mod=pn, bipermutation=bipermutation)

    num_bits = 4
    num_eqvclss = num_bits+1
    bipermutation = mk_bipermutation(num_eqvclss, randrange)
    pn = InnerIndexablePartition_bits__count_1s.mk(num_bits=num_bits)
    _test_ICipher_mod(cls, inner_indexable_partition_mod=pn, bipermutation=bipermutation)
_test_Cipher_mod__permutation_partition()


def _test_Cipher_mod__permutation_partition_fmap():
    cls = Cipher_mod__permutation_partition_fmap
    origin4rngs = 4
    idx8eqvcls2num_elements = (1, 2, 3, 4, 5, 3)
    may_ciphers_mod = (None, InvolutoryCipher_mod__subtracted_by.mk(modulus=2), None, InvolutoryCipher_mod__subtracted_by.mk(modulus=4), None, None)
    num_eqvclss = len(idx8eqvcls2num_elements)
    bipermutation = mk_bipermutation(num_eqvclss, randrange)
    pn = InnerIndexablePartition_mod__rng8eqvcls.mk(origin4rngs=origin4rngs, idx8eqvcls2num_elements=idx8eqvcls2num_elements)
    _test_ICipher_mod(cls, inner_indexable_partition_mod=pn, bipermutation=bipermutation, idx8eqvcls2may_cipher_mod4fmap=may_ciphers_mod)

    num_bits = 4
    num_eqvclss = num_bits+1
    may_ciphers_mod = (None, InvolutoryCipher_mod__subtracted_by.mk(modulus=4), InvolutoryCipher_mod__subtracted_by.mk(modulus=6), InvolutoryCipher_mod__subtracted_by.mk(modulus=4), None)
    bipermutation = mk_bipermutation(num_eqvclss, randrange)
    pn = InnerIndexablePartition_bits__count_1s.mk(num_bits=num_bits)
    _test_ICipher_mod(cls, inner_indexable_partition_mod=pn, bipermutation=bipermutation, idx8eqvcls2may_cipher_mod4fmap=may_ciphers_mod)
_test_Cipher_mod__permutation_partition_fmap()














#HHHHH
class Cipher__charset(IEase_repr_init, ICipher):
    def __init__(sf, /, *, ordered_charset, mk_ICipher5modulus):
        check_callable(mk_ICipher5modulus)
        checkT__type_le(IOrderedCharset)(ordered_charset)
        pass

    def _check_cipher_mod_(sf, modulus, cipher_mod, /):
        checkT__type_le(ICipher_mod)(cipher_mod)
        checkT__eq(modulus)(cipher_mod.get_modulus())
    def check_cipher_mod(sf, modulus, cipher_mod, /):
        sf._check_cipher_mod_(modulus, cipher_mod)

    def _preprocess(sf, s, /):
        ordered_charset = sf.ordered_charset
        u, L = ordered_charset.str2uint_with_len__via_digits__big_endian(s, validate=False)
        radix = len(ordered_charset)
        modulus = radix**L
        assert 0 <= u < modulus
        cipher_mod = sf.mk_ICipher5modulus(modulus)
        sf.check_cipher_mod(modulus, cipher_mod)
        if not cipher_mod.get_modulus()==modulus: raise TypeError
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

#def _mk_ICipher5modulus(modulus, /):


def _test_le_Cipher__charset(cls, /, *, mk_ICipher5modulus):
    checkT__issubclass__any(Cipher__charset)(cls)
    print(cls)
    ordered_charset__hex1 = hex___ordered_charset__str
    ordered_charset__hex2 = hex___ordered_charset__RangeBased

    clear_text__hex = '000AF9C0010'
    ps = [
        (ordered_charset__hex1, clear_text__hex)
        ,(ordered_charset__hex2, clear_text__hex)
        ]
    for ordered_charset, clear_text in ps:
        cipher__charset = cls(ordered_charset=ordered_charset, mk_ICipher5modulus=mk_ICipher5modulus)
        print(cipher__charset)


        cipher_text = cipher__charset.encrypt(clear_text, validate=True)
        if not cipher__charset.decrypt(cipher_text)==clear_text:raise logic-err

        print('   ', repr(clear_text))
        print('   ', repr(cipher_text))


#HHHHH
class InvolutoryCipher__charset(Cipher__charset, IInvolutoryCipher):
    #if 0: r'''
    _encrypt_ = IInvolutoryCipher._encrypt_
    _decrypt_ = IInvolutoryCipher._decrypt_
    _en_de_cipher_op_ = Cipher__charset._decrypt_
    #'''

    def _check_cipher_mod_(sf, modulus, cipher_mod, /):
        super()._check_cipher_mod_(modulus, cipher_mod)
        #checkT__type_le(IInvolutoryCipher)(cipher_mod)
        #   偶然关联？
        checkT__type_le(IInvolutoryCipher_mod)(cipher_mod)

def _test_Cipher__charset():
    cls = Cipher__charset
    def _mk_ICipher5modulus(modulus, /):
        return Cipher_mod__rotate.mk(modulus=modulus)

    _test_le_Cipher__charset(cls, mk_ICipher5modulus = _mk_ICipher5modulus)
def _test_InvolutoryCipher__charset():
    cls = InvolutoryCipher__charset
    def _mk_ICipher5modulus(modulus, /):
        return InvolutoryCipher_mod__subtracted_by.mk(modulus=modulus)

    _test_le_Cipher__charset(cls, mk_ICipher5modulus = _mk_ICipher5modulus)
_test_Cipher__charset()
_test_InvolutoryCipher__charset()

#main_body_src_code:end





































































































#HHHHH
_prefix4nm4core_involutory_cipher_type = 'InvolutoryCipher_mod__'
    # InvolutoryCipher_bits__xor is not available for arbitrary modulus
    #
_excluded_full_name4core_involutory_cipher_type = {'InvolutoryCipher_mod__chain'}
full_name2core_involutory_cipher_type = MapView({nm:v for nm, v in globals().items() if is_str(nm) and nm.isidentifier() and nm.startswith(_prefix4nm4core_involutory_cipher_type) and nm not in _excluded_full_name4core_involutory_cipher_type})

#brief name
short_name2core_involutory_cipher_type = MapView({nm[len(_prefix4nm4core_involutory_cipher_type):]:v for nm, v in full_name2core_involutory_cipher_type.items()})

_short_name2may_extra_kwargs4core_involutory_cipher_type = MapView(fmapT__dict(MapView)(dict(
    fmap_bit_op_on_tail_bits=dict(
        mk_ICipher5len_bits=_default_mk_InvolutoryCipher5len_bits
        )
    )))


def _4main():
    def mkT_ICipher5modulus(cls_nm, key, /):
        cls = short_name2core_involutory_cipher_type[cls_nm]
        extra_kwargs = _short_name2may_extra_kwargs4core_involutory_cipher_type.get(cls_nm, {})
        #InvolutoryCipher_mod__subtracted_by
        #InvolutoryCipher_mod__flip_parity
        #InvolutoryCipher_mod__fmap_bit_op_on_tail_bits
        #
        def mk_ICipher5modulus(modulus, /):
            involutory_cipher_mod = cls.mk(modulus=modulus, **extra_kwargs)
            #TODO
            import warnings
            warnings.warn('not using the key, use simple encrypt()')
            return involutory_cipher_mod
        return mk_ICipher5modulus

    def main_cipher_op(cls_nm, ordered_charset4txt, /, *, txt, key, validate):
        '-> txt'
        tyt = txt; del txt
        involutory_cipher__charset = InvolutoryCipher__charset(ordered_charset=ordered_charset4txt, mk_ICipher5modulus=mkT_ICipher5modulus(cls_nm, key))
        tzt = involutory_cipher__charset.en_de_cipher_op(tyt, validate=validate)
        return tzt
    return {**locals()}
class _4main:
    locals().update(_4main())

#HHHHH
def main(args=None, /):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout


    parser = argparse.ArgumentParser(
        description='InvolutoryCipher: self-inverse: encrypt===decrypt (hence no option to indicate D/E)'
        , formatter_class=argparse.RawDescriptionHelpFormatter
        , epilog=r'''
example: how to input arbitrary str (text or key)?
    $ echo $'\x30\n\u4E00'
    0
    一

#'''
        )

    def sorted__nm(nms, /):
        return sorted(nms, key=lambda nm:(len(nm), nm))

    parser.add_argument('--just_show_charset4txt', action='store_true'
                        , default = False
                        , help='display size and all chars of the selected charset4txt')
    parser.add_argument('--core_involutory_cipher', required=True, choices = sorted__nm(short_name2core_involutory_cipher_type)
                        , help='select the core involutory cipher algorithm')
    parser.add_argument('-k', '--key', required=True, type=str
                        , help='cipher key; arbitrary str')

    parser.add_argument('--charset4txt', required=True, choices = sorted__nm(short_name2ordered_charset)
                        , help='charset of input/output text; (not for key, key can be arbitrary str)')

    parser.add_argument('--input_is_path', action='store_true'
                        , default = False
                        , help='treat -i/--input as path instead of text')
    parser.add_argument('-i', '--input', type=str, default=None
                        , help='input text or input file path')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-ie', '--iencoding', type=str
                        , default='utf8'
                        , help='input file encoding')
    parser.add_argument('-oe', '--oencoding', type=str
                        , default='utf8'
                        , help='output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    binary_choices = 'ON OFF on off'.split()
    parser.add_argument('-iEOL', '--input__drop__new_line', required=True, choices = binary_choices
                        , help='drop new_line at end of input ')

    parser.add_argument('-oEOL', '--output__append__new_line', required=True, choices = binary_choices
                        , help='print new_line at end of output ')


    args = parser.parse_args(args)
    iencoding = args.iencoding
    oencoding = args.oencoding
    omode = 'wt' if args.force else 'xt'

    _binary_choice2bool = dict(ON=True, OFF=False)
    def is_ON(binary_choice, /):
        return _binary_choice2bool[binary_choice.upper()]
    input__drop__new_line = is_ON(args.input__drop__new_line)
    output__append__new_line = is_ON(args.output__append__new_line)


    #bug:nm4charset4txt = _prefix4nm4ordered_charset+args.charset4txt
    nm4charset4txt = args.charset4txt
    ordered_charset4txt = short_name2ordered_charset[nm4charset4txt]

    cls_nm = args.core_involutory_cipher

    if args.just_show_charset4txt:
        #stdout not fout?
        _saved_print(ordered_charset4txt)
        return

    may_ifname = args.input
    if args.input_is_path or may_ifname is None:
        with may_open_stdin(may_ifname, 'rt', encoding=iencoding) as fin:
            tyt_ = fin.read()
    else:
        tyt_ = may_ifname

    tyt_
    if input__drop__new_line:
        if tyt_[-1:] == '\n':
            tyt = tyt_[:-1]
        else:
            raise ValueError('input[-1:] != "\n"')
    else:
        tyt = tyt_
    del tyt_
    tyt



    tzt = _4main.main_cipher_op(cls_nm, ordered_charset4txt, txt=tyt, key=args.key, validate=True)
    if output__append__new_line:
        tzt_ = tzt + '\n'
    else:
        tzt_ = tzt
    del tzt
    tzt_

    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=oencoding) as fout:
        if 1:
            _saved_print(tzt_, end='', file=fout)
        else:
            fout.write(tzt_) #no \n??

if __name__ == "__main__":
    #not to call main() here
    # see: nn_ns.app.involutory_cipher
    print('py -m nn_ns.app.crypt.involution.involutory_cipher_cmd')
    import nn_ns.app.crypt.involution.involutory_cipher_cmd






#HHHHH
