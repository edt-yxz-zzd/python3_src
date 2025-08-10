#__all__:goto
r'''[[[
e ../../python3_src/seed/int_tools/DigitReader.py

seed.int_tools.DigitReader
py -m nn_ns.app.debug_cmd   seed.int_tools.DigitReader -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.int_tools.DigitReader:__doc__ -ht # -ff -df

[[
源起:
    view ../../python3_src/seed/int_tools/StepDecoder.py
]]

py_adhoc_call   seed.int_tools.DigitReader   @f
]]]'''#'''
__all__ = r'''
IDigitReader
    IDigitReader5iter
    IDigitReader5seq
        IDigitReader5bytes
    IDigitReader5binary_file
    IDigitReader5text_file

IDigitReader
    DigitReader5iter
    DigitReader5seq
    DigitReader5bytes
    DigitReader5binary_file
    DigitReader5text_file

ISubSeq
    SubSeq
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from itertools import islice
from seed.tiny_.check import check_type_is, check_int_ge, check_int_ge_lt
from seed.int_tools.RadixInfo import IRadixInfo, ZpowRadixInfo
from seed.for_libs.for_collections.override_repr4namedtuple import mk_namedtuple_
#.
from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_
#.repr_helper = lazy_import4func_('seed.helper.repr_input', 'repr_helper', __name__)
#.lazy_import4funcs_('seed.tiny', 'mk_tuple,print_err,ifNone:ifNone_', __name__)
#.if 0:from seed.tiny import mk_tuple,print_err,ifNone as ifNone_ #xxx:null_tuple #xxx:echo,fst,snd
#.from seed.helper.repr_input import repr_helper
#.from seed.tiny_._Base4repr import _Base4repr
        #sf._reset4repr(may_args4repr, may_kwds4repr)
        #sf._init4repr(*args4repr, **kwds4repr)
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError


######################
class ISubSeq(ABC):
    'subseq{x} # see:IDigitReader5seq'
    __slots__ = ()
    @property
    @abstractmethod
    def seq(sf, /):
        '-> [x]'
    @property
    @abstractmethod
    def begin(sf, /):
        '-> uint%(1+end)'
    @property
    @abstractmethod
    def end(sf, /):
        '-> uint%(1+len(seq))'
    ######################
    @abstractmethod
    def _advance_begin_(sf, sz, /):
        'sz/uint -> None # [0 <= sz <= end-begin]'
    ######################
    @property
    #@abstractmethod
    def seq_info(sf, /):
        '-> (seq, begin, end)'
        return (sf.seq, sf.begin, sf.end)
    ######################
#end-class ISubSeq(ABC):
######################
class SubSeq(ISubSeq):
    ___no_slots_ok___ = True
    def __init__(sf, /, seq, begin, end):
        check_int_ge(0, begin)
        #bug:check_int_ge_lt(begin, len(seq), end)
        check_int_ge_lt(begin, 1+len(seq), end)
        #sf._t = (seq, begin, end)
        sf._ls = seq
        sf._j = begin
        sf._k = end
    @override
    def _advance_begin_(sf, sz, /):
        'uint -> None'
        sf._j += sz
    @property
    @override
    def seq(sf, /):
        '-> [x]'
        return sf._ls
    @property
    @override
    def begin(sf, /):
        '-> uint%(1+end)'
        return sf._j
    @property
    @override
    def end(sf, /):
        '-> uint%(1+len(seq))'
        return sf._k
#end-class SubSeq(ISubSeq):
######################
######################
class IDigitReader(ABC):
    'digit_reader # [digit :: uint%radix_info4digit.radix]'
    __slots__ = ()
    ######################
    @property
    @abstractmethod
    def radix_info4digit(sf, /):
        '-> IRadixInfo{radix>=2}'
    ######################
    @abstractmethod
    def read_le(sf, sz, /):
        'sz/uint -> [digit]{len<=sz} # [[len<sz] <-> eof]'
    ######################
    def __iter__(sf, /):
        while (tm := sf.read_le(1)):
            [d] = tm
            yield d
    def read_eq(sf, sz, /):
        'sz/uint -> [digit]{len==sz}|^EOFError'
        digits = sf.read_le(sz)
        if not len(digits) == sz:raise EOFError(digits)
        return digits
    ######################
#end-class IDigitReader(ABC):
class IDigitReader5iter(IDigitReader):
    __slots__ = ()
    @property
    @abstractmethod
    def digit_iter(sf, /):
        '-> Iterator digit'
    @override
    def read_le(sf, sz, /):
        check_int_ge(0, sz)
        return tuple(islice(sf.digit_iter, sz))
    @override
    def __iter__(sf, /):
        return sf.digit_iter
class IDigitReader5seq(IDigitReader):
    __slots__ = ()
    @property
    @abstractmethod
    def digit_subseq(sf, /):
        '-> ISubSeq{digit}'
    @property
    def digit_seq(sf, /):
        '-> [digit]'
        return sf.digit_subseq.seq
    @property
    def begin4seq(sf, /):
        '-> uint%(1+end4seq)'
        return sf.digit_subseq.begin
    @property
    def end4seq(sf, /):
        '-> uint%(1+len(digit_seq))'
        return sf.digit_subseq.end
    @property
    def digit_seq_info(sf, /):
        '-> (digit_seq, begin4seq, end4seq)'
        return sf.digit_subseq.seq_info
    @override
    def read_le(sf, sz, /):
        check_int_ge(0, sz)
        (digit_seq, i, k) = sf.digit_seq_info
        j = min(i+sz, k)
        digits = digit_seq[i:j]
        sf.digit_subseq._advance_begin_(len(digits))
        return digits
class IDigitReader5bytes(IDigitReader5seq):
    __slots__ = ()
    #@override
    radix_info4digit = ZpowRadixInfo(8)
class IDigitReader5binary_file(IDigitReader):
    __slots__ = ()
    #@override
    radix_info4digit = ZpowRadixInfo(8)
    @property
    @abstractmethod
    def ibinfile(sf, /):
        '-> input_binary_file'
    @override
    def read_le(sf, sz, /):
        check_int_ge(0, sz)
        return sf.ibinfile.read(sz)
class IDigitReader5text_file(IDigitReader):
    __slots__ = ()
    @property
    @abstractmethod
    def itxtfile(sf, /):
        '-> input_text_file'
    @abstractmethod
    def char2digit_(sf, ch, /):
        'char -> digit'
    def str2digits_(sf, s, /):
        's/str -> [digit]{len==len(s)}'
        return tuple(map(sf.char2digit_, s))
    @override
    def read_le(sf, sz, /):
        check_int_ge(0, sz)
        return sf.str2digits_(sf.itxtfile.read(sz))
######################



mk_namedtuple_

#:.,.+5s/I\(.*\)/_Base\1 = mk_namedtuple_(__name__, 'Base\1', '')\rclass \1(_Base\1, \0):\r    ___no_slots_ok___ = True\r#end-class \1(_Base\1, \0):\r
_BaseDigitReader5iter = mk_namedtuple_(__name__, 'BaseDigitReader5iter', 'radix_info4digit digit_iter')
class DigitReader5iter(_BaseDigitReader5iter, IDigitReader5iter):
    ___no_slots_ok___ = True
    def __new__(cls, /, digit_iter):
        digit_iter = iter(digit_iter)
        return super(__class__, cls).__new__(cls, digit_iter)
#end-class DigitReader5iter(_BaseDigitReader5iter, IDigitReader5iter):

_BaseDigitReader5seq = mk_namedtuple_(__name__, 'BaseDigitReader5seq', 'radix_info4digit digit_subseq')
class DigitReader5seq(_BaseDigitReader5seq, IDigitReader5seq):
    ___no_slots_ok___ = True
#end-class DigitReader5seq(_BaseDigitReader5seq, IDigitReader5seq):

_BaseDigitReader5bytes = mk_namedtuple_(__name__, 'BaseDigitReader5bytes', 'digit_subseq')
class DigitReader5bytes(_BaseDigitReader5bytes, IDigitReader5bytes):
    ___no_slots_ok___ = True
    def __new__(cls, /, digit_subseq):
        check_type_is(bytes, digit_subseq.seq)
        return super(__class__, cls).__new__(cls, digit_subseq)
#end-class DigitReader5bytes(_BaseDigitReader5bytes, IDigitReader5bytes):

_BaseDigitReader5binary_file = mk_namedtuple_(__name__, 'BaseDigitReader5binary_file', 'ibinfile')
class DigitReader5binary_file(_BaseDigitReader5binary_file, IDigitReader5binary_file):
    ___no_slots_ok___ = True
#end-class DigitReader5binary_file(_BaseDigitReader5binary_file, IDigitReader5binary_file):

_BaseDigitReader5text_file = mk_namedtuple_(__name__, 'BaseDigitReader5text_file', 'radix_info4digit itxtfile char2digit_')
class DigitReader5text_file(_BaseDigitReader5text_file, IDigitReader5text_file):
    ___no_slots_ok___ = True
    #char2digit_
#end-class DigitReader5text_file(_BaseDigitReader5text_file, IDigitReader5text_file):


__all__
#[f,g] = lazy_import4funcs_('seed.int_tools.DigitReader', 'f,g', __name__)
from seed.int_tools.DigitReader import ISubSeq, IDigitReader, IDigitReader5iter, IDigitReader5seq, IDigitReader5bytes, IDigitReader5binary_file, IDigitReader5text_file
from seed.int_tools.DigitReader import DigitReader5seq, DigitReader5iter, DigitReader5bytes, DigitReader5binary_file, DigitReader5text_file
from seed.int_tools.DigitReader import SubSeq, DigitReader5seq
from seed.int_tools.DigitReader import *
