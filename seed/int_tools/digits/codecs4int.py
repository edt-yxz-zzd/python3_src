#__all__:goto
doing...
r'''[[[
e ../../python3_src/seed/int_tools/digits/codecs4int.py
view others/数学/编程/设计/自定义字符编码.txt

seed.int_tools.digits.codecs4int
py -m nn_ns.app.debug_cmd   seed.int_tools.digits.codecs4int -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.int_tools.digits.codecs4int:__doc__ -ht # -ff -df



[[
view others/数学/编程/设计/自定义字符编码.txt
本模块所有编码器满足以下约束:
    支持词典序#lexicographic order
    分级前置长度#逐步推进分级前置长度型编码方案
    ++{受控范围内胞串内部向外识别两端边界,双端内敛,字节串搜索,字节串词典序}

]]
[[
@20250615
简化设计:
    ===
    假设:充分大之后，尾部为二幂胞串:
        [[充分大] => [尾部::[uint%(2**C)]]]
    ===
    假设:充分大之后，整体分为五部分(只有两层长度):
        [[充分大] => [整编码==固定头部牜充分大(可能含动态爻元=>计入固定偏移量)++动态爻元计数用胞串(长度纟长度纟尾部)++?混合胞?(可能混合含半胞纟动态爻元丶半胞纟长度纟尾部)++胞串纟长度纟负载++胞串纟负载]]
            # [尾部==后四部分|后两部分(没有混合胞)]
            # * [尾部==后两部分]:比如:[码胞::[uint%10]][尾胞::uint%8][用『9』来做动态爻元][没有混合胞]
    ===
]]





py_adhoc_call   seed.int_tools.digits.codecs4int   @f
from seed.int_tools.digits.codecs4int import *
]]]'''#'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from itertools import islice
from seed.tiny_.check import check_type_is, check_int_ge

from seed.abc.abc__ver1 import abstractmethod, override, ABC
from seed.helper.repr_input import repr_helper

___end_mark_of_excluded_global_names__0___ = ...

#.class IPlugin(ABC):
#.    __slots__ = ()
#.    @property
#.    @abstractmethod
#.    def used_num_words6immediate(sf, /):
#.        '-> uint{>0}'
#.    @property
#.    @abstractmethod
#.    def offset4stored_uint(sf, /):
#.        '-> uint'
#.    @abstractmethod
#.    def uint2cells_ex_(sf, u, num_bits4u, /):
#.        'offsetted_stored_uint/u/uint -> num_bits4u/uint -> (icase/uint%used_num_words6immediate, num_cells/uint, Iter cell) # [num_bits4u == u.bit_length()]'
#.    @abstractmethod
#.    def uint5cells_ex_(sf, icase, cells, /):
#.        'icase/uint%used_num_words6immediate -> Iter cell -> (num_cells/uint, offsetted_stored_uint/u/uint)'
#.class IPlugin4FiniteInterval(IPlugin):
#.    __slots__ = ()
#.    @property
#.    @abstractmethod
#.    def either_max_unoffsetted_stored_uint_or_its_num_bits(sf, /):
#.        '-> (bool, uint)/((False, max_unoffsetted_stored_uint{may be non-2-power})|(True, max_num_bits4unoffsetted_stored_uint{max_unoffsetted_stored_uint==2**max_num_bits4unoffsetted_stored_uint-1}))'
#.    assert (0).bit_length() == 0
#.    def is_uint_in_range_(sf, u, num_bits4u, /):
#.        'offsetted_stored_uint/u/uint -> num_bits4u/uint -> bool # [num_bits4u == u.bit_length()]'
#.        # # [num_bits4u == 0 if u==0 else u.bit_length()]
#.        assert u >= 0
#.        (is_num_bits, x) = sf.either_max_unoffsetted_stored_uint_or_its_num_bits
#.        offset = sf.offset4stored_uint
#.        v = u -offset
#.            # u == offsetted_stored_uint
#.            # v == unoffsetted_stored_uint
#.
#.        if v < 0:
#.            return False
#.        if not is_num_bits:
#.            max_unoffsetted_stored_uint = x
#.            return v <= max_unoffsetted_stored_uint
#.        max_num_bits4unoffsetted_stored_uint = x
#.
#.        if offset == 0:
#.            num_bits4v = num_bits4u
#.        else:
#.            num_bits4v = v.bit_length()
#.        num_bits4v
#.        return num_bits4v <= max_num_bits4unoffsetted_stored_uint
#.
#.
#.class IPlugin4InfiniteInterval(IPlugin):
#.    __slots__ = ()
#.    @property
#.    @abstractmethod
#.    def min_num_layers(sf, /):
#.        '-> uint'
#.    @property
#.    @abstractmethod
#.    def whether_supported_infinite_reserved_space(sf, /):
#.        '-> bool'
#.
#.class ICodec4SInt__zpow_based__lexicographic_order_reserved(ABC):
#.    'si'
#.class ICodec4UInt__zpow_based__lexicographic_order_reserved(ABC):
#.    'ui'
#.    __slots__ = ()
#.    @property
#.    @abstractmethod
#.    def num_words6macro_header(sf, /):
#.        '-> uint'
#.    @property
#.    @abstractmethod
#.    def num_bits4cell6body(sf, /):
#.        '-> uint'
#.    @property
#.    @abstractmethod
#.    def seq4plugin4finite_interval(sf, /):
#.        '-> [IPlugin4FiniteInterval]'
#.    @property
#.    @abstractmethod
#.    def plugin4infinite_interval(sf, /):
#.        '-> IPlugin4InfiniteInterval'
#.
#.    def encode4uint_ex_(sf, u, /):
#.        'offsetted_stored_uint/u/uint -> (num_cells/uint, (Iter cell){nonempty})'
#.        check_int_ge(0, u)
#.        num_bits4u == u.bit_length()
#.        offset4icase = 0
#.        for plgn in sf.seq4plugin4finite_interval:
#.            if plgn.is_uint_in_range_(u, num_bits4u):
#.                break
#.            offset4icase += plgn.used_num_words6immediate
#.        else:
#.            plgn = sf.plugin4infinite_interval
#.        offset4icase, plgn
#.        (icase, _num_cells, _cells) = plgn.uint2cells_ex_(u, num_bits4u)
#.        head = offset4icase + icase
#.        return (1+_num_cells, chain([head], _cells))
#.    def dencode4uint_ex_(sf, cells, /):
#.        '(Iter cell){nonempty} -> (num_cells/uint, offsetted_stored_uint/u/uint)'
#.        cells = iter(cells)
#.        for head in cells:
#.            _cells = cells; del cells
#.            break
#.        else:
#.            raise ValueError('null iter')
#.        head, _cells
#.        check_int_ge(0, head)
#.
#.        offset4icase = 0
#.        for plgn in sf.seq4plugin4finite_interval:
#.            _offset4icase = offset4icase + plgn.used_num_words6immediate
#.            if head < _offset4icase:
#.                break
#.        else:
#.            plgn = sf.plugin4infinite_interval
#.            _offset4icase = offset4icase + plgn.used_num_words6immediate
#.            if not head < _offset4icase:
#.                raise ValueError('head cell too big')
#.        offset4icase, plgn
#.        icase = head -offset4icase
#.        (_num_cells, offsetted_stored_uint) = plgn.uint5cells_ex_(icase, _cells)
#.        return (1+_num_cells, offsetted_stored_uint)
#.
#.#num_words4cell6head
#.#num_words4cell6body
#.num_words6macro_header#num_words6macro_cell8logical_header
#.num_bits4cell6body
#.#finite_plugin:
#.(used_num_words6immediate, offset4stored_uint, nbits_vs_uint, (max_num_bits4unoffsetted_stored_uint|max_unoffsetted_stored_uint))
#.  #非 0层-立即数 => (num_storage_bits6immediate爻+)首层{min_..=max_}num_body_cells4fst_layer体符
#.  #######
#.  * (num_layers6append, multiplicity, num_storage_bits6immediate, num_body_cells4fst_layer, offset4stored_uint)
#.      [used_num_words6immediate := multiplicity*2**num_storage_bits6immediate]
#.      [max_unoffsetted_stored_uint := multiplicity*(iterate (\len -> 2**len-1) (2**(num_storage_bits6immediate+num_bits4cell6body*num_body_cells4fst_layer)-1) !! num_layers6append)]
#.  #######
#.  * (num_layers6append, num_storage_bits6immediate, min_num_body_cells4fst_layer, max_num_body_cells4fst_layer, offset4stored_uint)
#.      [used_num_words6immediate := (max_num_body_cells4fst_layer+1-min_num_body_cells4fst_layer)*2**num_storage_bits6immediate]
#.      [max_num_bits4unoffsetted_stored_uint := if num_layers6append == 0 then num_storage_bits6immediate else iterate (\num_bits4len -> 2**num_bits4len-1) (num_storage_bits6immediate+num_bits4cell6body*max_num_body_cells4fst_layer) !! (num_layers6append-1)]
#.  #######
#.###super_dybl_layers
#.#infinite_plugin:
#.(min_num_layers, whether_supported_infinite_reserved_space)
#.
#.
#.
#.
#.
#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError
#.



__all__
from seed.int_tools.digits.codecs4int import *
