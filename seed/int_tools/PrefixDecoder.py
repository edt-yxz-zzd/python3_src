#__all__:goto
r'''[[[
e ../../python3_src/seed/int_tools/PrefixDecoder.py

seed.int_tools.PrefixDecoder
py -m nn_ns.app.debug_cmd   seed.int_tools.PrefixDecoder -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.int_tools.PrefixDecoder:__doc__ -ht # -ff -df

[[
源起:
view ../../python3_src/seed/int_tools/StepDecoder.py
view ../../python3_src/seed/int_tools/digits/codecs4int.py

TODO:IStepDecoder__dynamic_bibits{body_bibit:="10"}
    bibit:two bit
    regex"(10)*(0|11)"
TODO:IStepDecoder__dynamic_nbits{imay_max_num_bits4read,body_nbit}
    nbit:n bit
    [body_nbit:=regex"10{n-1}"]
        regex"(10{n-1})*(0|10{0,n-2}1|1{2,n-1}0|11)"
    =>
    #前缀打断:n种 结束串:
    regex"({<body_nbit>})*({<or:body_nbit[:j]++[~body_nbit[j]] for j in [0..<n]>})"

==>>:
prefix_mapping_tree

[prefix_mapping_tree{radix4digit} =[def]= [child4prefix_mapping_tree{radix4digit}]{len=radix4digit}]
[child4prefix_mapping_tree{radix4digit} =[def]= (Either data prefix_mapping_tree{radix4digit})]

]]



def mk_IPrefixMappingTree_(mkr, radix4digit, may_elem2digit_, sorted_complete_prefix_code_seq, /):
>>> mk_IPrefixMappingTree_(PrefixMappingTree__radix_eq_2, 2, int, '0 10 11'.split())
PrefixMappingTree__radix_eq_2((Either(False, 0), Either(True, PrefixMappingTree__radix_eq_2((Either(False, 1), Either(False, 2))))))

>>> mk_IPrefixMappingTree_(PrefixMappingTree__radix_eq_2, 2, int, '000 001 010 011 10 11'.split())
PrefixMappingTree__radix_eq_2((Either(True, PrefixMappingTree__radix_eq_2((Either(True, PrefixMappingTree__radix_eq_2((Either(False, 0), Either(False, 1)))), Either(True, PrefixMappingTree__radix_eq_2((Either(False, 2), Either(False, 3))))))), Either(True, PrefixMappingTree__radix_eq_2((Either(False, 4), Either(False, 5))))))

>>> mk_IPrefixMappingTree_(PrefixMappingTree__radix_eq_2, 2, int, '0 10 110 1110 1111'.split())
PrefixMappingTree__radix_eq_2((Either(False, 0), Either(True, PrefixMappingTree__radix_eq_2((Either(False, 1), Either(True, PrefixMappingTree__radix_eq_2((Either(False, 2), Either(True, PrefixMappingTree__radix_eq_2((Either(False, 3), Either(False, 4))))))))))))


>>> tree = _
>>> tree.partial_decode_(map(int, '0!'))
(1, Either(False, 0))
>>> tree.partial_decode_(map(int, '10!'))
(2, Either(False, 1))
>>> tree.partial_decode_(map(int, '110!'))
(3, Either(False, 2))
>>> tree.partial_decode_(map(int, '1110!'))
(4, Either(False, 3))
>>> tree.partial_decode_(map(int, '1111!'))
(4, Either(False, 4))



def partial_decode4radix_eq_2_(prefix_mapping_tree, may_prefix_mapping_tree4remain, icode2is_terminal_, rxdigit8bits, /):
>>> icode2is_terminal_ = (0,2).__contains__
>>> def mk_rxdigit8bits5str_(s01, /):
...     return RadixedDigit(ZpowRadixInfo(len(s01)), int(s01, 2))
>>> partial_decode4radix_eq_2_(tree, None, icode2is_terminal_, mk_rxdigit8bits5str_('0'))
([], 0, Either(False, 0), RadixedDigit(ZpowRadixInfo(0), 0))
>>> partial_decode4radix_eq_2_(tree, None, icode2is_terminal_, mk_rxdigit8bits5str_('110'))
([], 0, Either(False, 2), RadixedDigit(ZpowRadixInfo(0), 0))

>>> partial_decode4radix_eq_2_(tree, None, icode2is_terminal_, mk_rxdigit8bits5str_('10110'))
([1], 0, Either(False, 2), RadixedDigit(ZpowRadixInfo(0), 0))
>>> partial_decode4radix_eq_2_(tree, None, icode2is_terminal_, mk_rxdigit8bits5str_('10100'))
([1, 1], 0, Either(False, 0), RadixedDigit(ZpowRadixInfo(0), 0))

>>> partial_decode4radix_eq_2_(tree, None, icode2is_terminal_, mk_rxdigit8bits5str_('1011'))
([1], 2, Either(True, PrefixMappingTree__radix_eq_2((Either(False, 2), Either(True, PrefixMappingTree__radix_eq_2((Either(False, 3), Either(False, 4))))))), RadixedDigit(ZpowRadixInfo(0), 0))
>>> partial_decode4radix_eq_2_(tree, None, icode2is_terminal_, mk_rxdigit8bits5str_('101111'))
([1, 4], 0, Either(True, PrefixMappingTree__radix_eq_2((Either(False, 0), Either(True, PrefixMappingTree__radix_eq_2((Either(False, 1), Either(True, PrefixMappingTree__radix_eq_2((Either(False, 2), Either(True, PrefixMappingTree__radix_eq_2((Either(False, 3), Either(False, 4))))))))))))), RadixedDigit(ZpowRadixInfo(0), 0))
>>> partial_decode4radix_eq_2_(tree, None, icode2is_terminal_, mk_rxdigit8bits5str_('1011111'))
([1, 4], 1, Either(True, PrefixMappingTree__radix_eq_2((Either(False, 1), Either(True, PrefixMappingTree__radix_eq_2((Either(False, 2), Either(True, PrefixMappingTree__radix_eq_2((Either(False, 3), Either(False, 4)))))))))), RadixedDigit(ZpowRadixInfo(0), 0))
>>> partial_decode4radix_eq_2_(tree, None, icode2is_terminal_, mk_rxdigit8bits5str_('10111110'))
([1, 4, 1], 0, Either(True, PrefixMappingTree__radix_eq_2((Either(False, 0), Either(True, PrefixMappingTree__radix_eq_2((Either(False, 1), Either(True, PrefixMappingTree__radix_eq_2((Either(False, 2), Either(True, PrefixMappingTree__radix_eq_2((Either(False, 3), Either(False, 4))))))))))))), RadixedDigit(ZpowRadixInfo(0), 0))
>>> partial_decode4radix_eq_2_(tree, None, icode2is_terminal_, mk_rxdigit8bits5str_('101111100'))
([1, 4, 1], 0, Either(False, 0), RadixedDigit(ZpowRadixInfo(0), 0))




>>> (nonterminal_icodes, num_bits4prefix4incomplete_code, child, rxdigit8remain_bits) = partial_decode4radix_eq_2_(tree, None, icode2is_terminal_, mk_rxdigit8bits5str_('1011111'))
>>> nonterminal_icodes
[1, 4]
>>> partial_decode4radix_eq_2_(tree, child.right, icode2is_terminal_, mk_rxdigit8bits5str_('1110'))
([4], 0, Either(False, 0), RadixedDigit(ZpowRadixInfo(0), 0))







py_adhoc_call   seed.int_tools.PrefixDecoder   @f
]]]'''#'''
__all__ = r'''
mk_IPrefixMappingTree_
IPrefixMappingTree
    IPrefixMappingTree__init_children
    PrefixMappingTree__auto_radix
    PrefixMappingTree__radix_eq_2
        partial_decode4radix_eq_2_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from functools import cached_property
from itertools import pairwise

from seed.int_tools.RadixInfo import IZpowRadixInfo, ZpowRadixInfo, mk_ZpowRadixInfo_
from seed.int_tools.RadixInfo import IRadixInfo, RadixInfo, mk_RadixInfo_
from seed.int_tools.RadixInfo import IRadixedDigit, RadixedDigit, rxdigit8no_bits
from seed.types.Either import Either
from seed.types.Either import mk_Left, mk_Right
from seed.tiny_.check import check_type_le, check_type_is, check_int_ge#no:check_all_
#.
from seed.abc.abc__ver1 import abstractmethod, override, ABC
from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_
repr_helper = lazy_import4func_('seed.helper.repr_input', 'repr_helper', __name__)
lazy_import4funcs_('seed.tiny', 'mk_tuple,print_err,ifNone:ifNone_', __name__)
if 0:from seed.tiny import mk_tuple,print_err,ifNone as ifNone_ #xxx:null_tuple #xxx:echo,fst,snd
echo = lazy_import4func_('seed.tiny', 'echo', __name__)

len_lcp_of2 = lazy_import4func_('seed.seq_tools.lcp_of', 'len_lcp_of2', __name__)
if 0:from seed.seq_tools.lcp_of import len_lcp_of2
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError

#.class IPrefixDecoder(ABC):
#.    __slots__ = ()
#.class PrefixDecoder(IPrefixDecoder):
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)

class IPrefixMappingTree(ABC):
    __slots__ = ()
    @property
    @abstractmethod
    def radix_info4digit(sf, /):
        '-> radix_info4key/IRadixInfo # [mapping.key == digit :: uint%radix4digit] # [radix4digit >= 2]'
    @abstractmethod
    def __getitem__(sf, digit, /):
        'digit/uint%radix4digit -> child4prefix_mapping_tree/(Either data IPrefixMappingTree{radix4digit})'
    def partial_decode_(sf, digits, /):
        'Iter digit/uint%radix4digit -> (len_prefix4digits, child4prefix_mapping_tree/(Either data IPrefixMappingTree{radix4digit}))'
        sz = 0
        for sz, digit in enumerate(digits, 1):
            child = sf[digit]
            if child.is_left:
                break
            sf = child.payload
        if sz == 0:
            child = mk_Right(sf)
        return (sz, child)

class IPrefixMappingTree__init_children(IPrefixMappingTree):
    ___no_slots_ok___ = True
    @property
    def children(sf, /):
        return sf._ls
    def __init__(sf, children, /):
        ls = mk_tuple(children)
        sf._ls = ls
        ### assign before check since PrefixMappingTree__auto_radix
        radix = sf.radix_info4digit.radix
        if not len(ls) == radix:raise TypeError
        #check_all_([check_type_is, Either], ls)
        for x in ls:
            check_type_is(Either, x)
        for x in ls:
            if x.is_right:
                y = x.right
                check_type_le(IPrefixMappingTree, y)
                if not y.radix_info4digit.radix == radix:raise TypeError
    def __repr__(sf, /):
        return repr_helper(sf, sf._ls)
    @override
    def __getitem__(sf, digit, /):
        return sf._ls[digit]

def partial_decode4radix_eq_2_(prefix_mapping_tree, may_prefix_mapping_tree4remain, icode2is_terminal_, rxdigit8bits, /):
    'IPrefixMappingTree{.radix_info4digit.radix==2}{data==icode} -> may prefix_mapping_tree4remain{subtree of the fst one} -> icode2is_terminal_/(icode->bool) -> IRadixedDigit{.radix_info.is_zpow_radix} -> (nonterminal_icodes/[icode/uint], num_bits4prefix4incomplete_code, child4prefix_mapping_tree/(Either terminal_icode prefix_mapping_tree4remain/IPrefixMappingTree{radix4digit==2}), rxdigit8remain_bits) # [two kind digits:bit for prefix_mapping_tree, digit%zpow for rxdigit8bits]'
    if not may_prefix_mapping_tree4remain is None:
        prefix_mapping_tree4remain = may_prefix_mapping_tree4remain
        if not (_ri:=prefix_mapping_tree4remain.radix_info4digit.radix) == 2:raise TypeError(_ri)
        tree = prefix_mapping_tree4remain
    else:
        tree = prefix_mapping_tree
    tree
    _tree = prefix_mapping_tree
    #.def partial_decode4radix_eq_2_(prefix_mapping_tree, icode2is_terminal_, rxdigit8bits, /):
    #.    'IPrefixMappingTree{.radix_info4digit.radix==2}{data==icode} -> icode2is_terminal_/(icode->bool) -> IRadixedDigit{.radix_info.is_zpow_radix} -> (nonterminal_icodes/[icode/uint], num_bits4prefix4incomplete_code, child4prefix_mapping_tree/(Either terminal_icode prefix_mapping_tree4remain/IPrefixMappingTree{radix4digit==2}), rxdigit8remain_bits) # [two kind digits:bit for prefix_mapping_tree, digit%zpow for rxdigit8bits]'
    if not (_ri:=prefix_mapping_tree.radix_info4digit.radix) == 2:raise TypeError(_ri)
    if not (ri:=rxdigit8bits.radix_info).is_zpow_radix:raise TypeError(ri)
    u = ri.radix | rxdigit8bits.digit
    s01 = bin(u)[3:]
    assert len(s01) == ri.num_bits4digit
    it_bits = map(int, s01)
    nonterminal_icodes = []
    acc_nbits = 0
    while 1:
        (num_bits4prefix, child) = tree.partial_decode_(it_bits)
        777;tree = _tree
        777;acc_nbits += num_bits4prefix
        if child.is_right:
            #tree
            #incomplete_code
            num_bits4prefix4incomplete_code = num_bits4prefix
            for _ in it_bits:raise 000
            break
        #complete_code
        icode = data = child.left
        if icode2is_terminal_(icode):
            #terminal
            #no:incomplete_code
            num_bits4prefix4incomplete_code = 0
            #terminal_icode = icode
            break
        #nonterminal_icode = icode
        nonterminal_icodes.append(icode)
    (nonterminal_icodes, num_bits4prefix4incomplete_code, child)
    num_bits4remain = ri.num_bits4digit -acc_nbits
    if acc_nbits == 0:
        rxdigit8remain_bits = rxdigit8bits
    elif num_bits4remain == 0:
        rxdigit8remain_bits = rxdigit8no_bits
    else:
        #_s01 = s01[acc_nbits:]
        #v = int(_s01, 2)
        radix_info4remain = ZpowRadixInfo(num_bits4remain)
        v = u & radix_info4remain.max_digit
        rxdigit8remain_bits = RadixedDigit(radix_info4remain, v)
    rxdigit8remain_bits
    return (nonterminal_icodes, num_bits4prefix4incomplete_code, child, rxdigit8remain_bits)
#end-def partial_decode4radix_eq_2_(prefix_mapping_tree, may_prefix_mapping_tree4remain, icode2is_terminal_, rxdigit8bits, /):

class PrefixMappingTree__radix_eq_2(IPrefixMappingTree__init_children):
    #@property
    #@override
    radix_info4digit = ZpowRadixInfo(1)
class PrefixMappingTree__auto_radix(IPrefixMappingTree__init_children):
    @cached_property
    @override
    def radix_info4digit(sf, /):
        return RadixInfo(len(sf._ls))



def mk_IPrefixMappingTree_(mkr, radix4digit, may_elem2digit_, sorted_complete_prefix_code_seq, /):
    'mkr/(children/[(Either data IPrefixMappingTree{radix4digit})]{len==radix4digit} -> IPrefixMappingTree{radix4digit}) -> radix4digit/uint{>=2} -> may elem2digit_/(x -> digit) -> sorted_complete_prefix_code_seq/sorted[[x]]{len>=radix4digit} -> IPrefixMappingTree{radix4digit}'
    assert len(sorted_complete_prefix_code_seq) >= radix4digit >= 2
    R = radix4digit
    xss = sorted_complete_prefix_code_seq
    x2d_ = ifNone_(may_elem2digit_, echo)
    lens4lcps = [len_lcp_of2(map(x2d_, xs), map(x2d_, ys)) for xs, ys in pairwise(xss)]
    assert len(lens4lcps) == len(xss)-1
    def __():
        for j, xs in enumerate(xss):
            assert len(xs) == 1+max(lens4lcps[max(0,j-1):(j+1)])
    __()
    def recur(len_lcp8tgt, i, k, /):
        '-> child'
        # xss[i:k]
        # => lens4lcps[i:k-1]
        if i == k-1:
            data = i
            child = mk_Left(data)
            return child
        js = [j for j in range(i+1,k) if lens4lcps[j-1] == len_lcp8tgt]
            # !! lens4lcps[i:k-1]
        777;js.insert(0,i)
        777;js.append(k)
        if not len(js) == 1+R: raise ValueError('prefix_code_seq is incomplete')
        _len8tgt = len_lcp8tgt+1
        children = (recur(_len8tgt, _i, _k) for _i,_k in pairwise(js))
        tree = mkr(children)
        child = mk_Right(tree)
        return child
    child = recur(0, 0, len(xss))
    tree = child.right
        # !! [len(sorted_complete_prefix_code_seq) >= radix4digit >= 2]
    return tree



__all__
from seed.int_tools.PrefixDecoder import IPrefixMappingTree, IPrefixMappingTree__init_children
from seed.int_tools.PrefixDecoder import PrefixMappingTree__radix_eq_2, PrefixMappingTree__auto_radix
from seed.int_tools.PrefixDecoder import mk_IPrefixMappingTree_, partial_decode4radix_eq_2_
#[mk_IPrefixMappingTree_, partial_decode4radix_eq_2_] = lazy_import4funcs_('seed.int_tools.PrefixDecoder', 'mk_IPrefixMappingTree_,partial_decode4radix_eq_2_', __name__)
    #def mk_IPrefixMappingTree_(mkr, radix4digit, may_elem2digit_, sorted_complete_prefix_code_seq, /):
    #def partial_decode4radix_eq_2_(prefix_mapping_tree, may_prefix_mapping_tree4remain, icode2is_terminal_, rxdigit8bits, /):
from seed.int_tools.PrefixDecoder import *
