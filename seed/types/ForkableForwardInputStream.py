#__all__:goto
r'''[[[
e ../../python3_src/seed/types/ForkableForwardInputStream.py
view ../../python3_src/seed/types/LazyList.py
    from seed.types.LazyList import to_LazyList, to_LazyListIter
view ../../python3_src/seed/types/IForkable.py

[[
why? to make a simple parser for py literal data
  view ../../python3_src/seed/recognize/xml/Visitor4ParseResult4XML.py
    #load parse result:
        # literal_eval crash for nodes<ucd.unihan.flat.xml>
        #   try:eval==>>eval crash too
]]
[[
ForkableForwardInputStream vs io/ifile:
  forkable forward inputter
    diff from file.tell/seek
    inputter.fork ~= file.tell
      save state
      inputter.tell_gap_position_info #no seek
    inputter.read ~= file.read
      inplace mutable method
    inputter has no assignment/rollback  vs file.seek
      inplace mutable method
      vs:
        * forward only oneway access
        * random access
]]




seed.types.ForkableForwardInputStream
py -m nn_ns.app.debug_cmd   seed.types.ForkableForwardInputStream -x
py -m nn_ns.app.doctest_cmd seed.types.ForkableForwardInputStream:__doc__ -ht
py_adhoc_call   seed.types.ForkableForwardInputStream   @f
#]]]'''
__all__ = r'''
IForkable
    IForkable__stamp
    IForkable__tell_gap_position_info
    IForkableForwardInputStream__peek_only
        IBaseForkableForwardInputStream
            BaseForkableForwardInputStream__using_LazyListIter

            IForkableForwardInputStream
                ForkableForwardInputStream__using_LazyListIter


iter_char_tokens5ifile
    mk_forkable_char_stream5txt
    mk_forkable_char_stream5ipath
    mk_forkable_char_stream5ifile

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...

from seed.types.IToken import IBaseToken, IToken, BaseToken
from seed.types.IToken import IBasePositionInfo, IPositionInfo4Gap, IPositionInfo4Span

from seed.types.IForkable import IForkable, IForkable__stamp

from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.helper.repr_input import repr_helper
from seed.tiny import null_iter, null_tuple, mk_tuple
from seed.tiny_.check import check_type_is, check_type_le, check_int_ge
from seed.types.LazyList import to_LazyList, to_LazyListIter

from itertools import islice




######################
######################
from pathlib import Path
from seed.types.LazyList import to_LazyList, to_LazyListIter
from seed.types.IToken import Token__char, PositionInfo4Span__text_file, PositionInfo4Gap__text_file, LinenoColumn
######################
######################

___end_mark_of_excluded_global_names__0___ = ...


class IForkable__tell_gap_position_info(IForkable):
    'tell_gap_position_info'
    __slots__ = ()
    @abstractmethod
    def tell_gap_position_info(sf, /):
        '-> prev_tgend/prev_token_end_gap_position_info/IPositionInfo4Gap #immutable_method'


def _check_elements_(cls, sz, xs, /):
    if not len(xs) <= sz:raise 000
    xs[:0]
    for x in xs:
        cls._check_element_(x)
class IForkableForwardInputStream__peek_only(IForkable):
    'no 『read.*』 #useless?<<==.fork()'
    __slots__ = ()
    @classmethod
    @abstractmethod
    def _check_element_(cls, element, /):
        '-> None | ^TypeError #immutable_method'
    @abstractmethod
    def _iter_elements__immutable_(sf, /):
        '-> Iter element #immutable_method'
    @abstractmethod
    def _peek_le_(sf, sz, /):
        '-> [element]{len<=sz} #immutable_method'
    def peek_le(sf, sz, /):
        '-> [element]{len<=sz} #immutable_method'
        check_int_ge(0, sz)
        xs = sf._peek_le_(sz)
        _check_elements_(sf, sz, xs)
        return xs
    def iter_elements__immutable(sf, /):
        '-> Iter element #immutable_method'
        for x in sf._iter_elements__immutable_():
            sf._check_element_(x)
            yield x
    def peek1(sf, /, *, exc=None):
        '-> element | ^EOFError #immutable_method'
        ot = sf.fork()
        return ot.read1(exc=exc)
    @property
    def head(sf, /):
        '-> element | ^EOFError #immutable_method'
        return sf.peek1()
    @property
    def eof(sf, /):
        '-> bool #immutable_method'
        return not sf.peek_le(1)
IForkableForwardInputStream__peek_only
class IBaseForkableForwardInputStream(IForkableForwardInputStream__peek_only):
    'use 『.fork()』 to hold/cache curr state # has no 『.seek()』'
    __slots__ = ()
    _basetype4stream_element_ = object
    @classmethod
    @override
    def _check_element_(cls, element, /):
        '-> None | ^TypeError #immutable_method'
        if not object is (T := cls._basetype4stream_element_):
            check_type_le(T, element)
    #@abstractmethod
    #def fork(sf, /):
    #    '-> ot/IBaseForkableForwardInputStream #immutable_method'
    @abstractmethod
    def _read_le_(sf, sz, /):
        '-> [element]{len<=sz} #inplace_mutable_method'
    def read_le(sf, sz, /):
        '-> [element]{len<=sz} #inplace_mutable_method'
        check_int_ge(0, sz)
        xs = sf._read_le_(sz)
        _check_elements_(sf, sz, xs)
        return xs
    @override
    def _peek_le_(sf, sz, /):
        '-> [element]{len<=sz} #immutable_method'
        ot = sf.fork()
        return ot._read_le_(sz)
    def read1(sf, /, *, exc=None):
        '-> element | ^EOFError #inplace_mutable_method'
        tmay_x = sf.read_le(1)
        if not tmay_x:
            raise EOFError if exc is None else exc
        [x] = tmay_x
        return x
    def iter_elements_(sf, /, *, fork_first:bool):
        '-> Iter element #[immutable_method if fork_first else inplace_mutable_method]'
        if fork_first:
            sf = sf.fork()
        tmay_x = sf.read_le(1)
        while tmay_x:
            [head] = tmay_x
            yield head
            tmay_x = sf.read_le(1)
        return
    def iter_elements__mutable(sf, /):
        '-> Iter element #inplace_mutable_method'
        return sf.iter_elements_(fork_first=False)

    @override
    def _iter_elements__immutable_(sf, /):
        '-> Iter element #immutable_method'
        return sf.iter_elements_(fork_first=True)
        ot = sf.fork()
        return ot.mutable_iter_elements()
    @override
    def iter_elements__immutable(sf, /):
        '-> Iter element #immutable_method'
        return sf.iter_elements_(fork_first=True)

_LazyListIter = type(to_LazyListIter(null_iter))
class BaseForkableForwardInputStream__using_LazyListIter(IBaseForkableForwardInputStream, IForkable__stamp):
    ___no_slots_ok___ = True
    def __init__(sf, lazylist_iter, /):
        #if not lazylist_iter is iter(lazylist_iter) is to_LazyListIter(lazylist_iter):
            #bug:since:to_LazyListIter() 'to use "iterator.fork()"'
        #if not type(lazylist_iter) is _LazyListIter: raise TypeError(type(lazylist_iter))
        check_type_is(_LazyListIter, lazylist_iter)
        sf._it = lazylist_iter
    def __repr__(sf, /):
        return repr_helper(sf, sf._it)
    @override
    def get_stamp(sf, /):
        '-> stamp'
        return sf._it.get_stamp()
    @override
    def has_changed_since_stamp_(sf, stamp, /):
        'stamp -> changed/bool'
        return sf._it.has_changed_since_stamp_(stamp)
    @override
    def were(sf, ot, /):
        'sf/IForkable -> ot/IForkable -> bool #immutable_method'
        return ((sf is ot)
        or (type(sf) is type(ot)
            and sf._it.were(ot._it)
            )
        )
    @override
    def fork(sf, /):
        '-> ot/IBaseForkableForwardInputStream #immutable_method'
        return type(sf)(sf._it.fork())
    @override
    def _read_le_(sf, sz, /):
        '-> [element]{len<=sz} #inplace_mutable_method'
        return mk_tuple(islice(sf._it, sz))
BaseForkableForwardInputStream__using_LazyListIter(to_LazyListIter(null_iter))





class IForkableForwardInputStream(IBaseForkableForwardInputStream, IForkable__tell_gap_position_info):
    #class IForkableForwardInputStream__token(IBaseForkableForwardInputStream, IForkable__tell_gap_position_info):
    '(prev_token_end_gap_position_info,stream<IToken>)'
    __slots__ = ()
    #@override
    _basetype4stream_element_ = IToken

class ForkableForwardInputStream__using_LazyListIter(IForkableForwardInputStream, IForkable__tell_gap_position_info, IForkable__stamp):
    '(IPositionInfo4Gap,_LazyListIter<IToken>)'
    ___no_slots_ok___ = True
    def __init__(sf, global_runtime_info, prev_token_end_gap_position_info, lazylist_iter, /):
        check_type_le(IPositionInfo4Gap, prev_token_end_gap_position_info)
        check_type_is(_LazyListIter, lazylist_iter)
        sf._d = global_runtime_info
        sf._g = prev_token_end_gap_position_info
        sf._it = lazylist_iter
    def __repr__(sf, /):
        return repr_helper(sf, sf._d, sf._g, sf._it)
    @override
    def get_curr_lazylist(sf, /):
        '-> remain_tail/LazyList'
        return sf._it.get_curr_lazylist()
    @override
    def get_stamp(sf, /):
        '-> stamp'
        return sf._it.get_stamp()
    @override
    def has_changed_since_stamp_(sf, stamp, /):
        'stamp -> changed/bool'
        return sf._it.has_changed_since_stamp_(stamp)
    @override
    def were(sf, ot, /):
        'sf/IForkable -> ot/IForkable -> bool #immutable_method'
        return ((sf is ot)
        or (type(sf) is type(ot)
            and sf._it.were(ot._it)
            and (sf._d is ot._d)
            and (sf._g == ot._g)
            )
        )
    @override
    def fork(sf, /):
        '-> ot/IBaseForkableForwardInputStream #immutable_method'
        return type(sf)(sf._d, sf._g, sf._it.fork())
    @override
    def _read_le_(sf, sz, /):
        '-> [element]{len<=sz} #inplace_mutable_method'
        xs = mk_tuple(islice(sf._it, sz))
        if xs:
            token = xs[-1]
            sf._g = token.token_end_position_info
        return xs
    @override
    def tell_gap_position_info(sf, /):
        '-> prev_tgend/prev_token_end_gap_position_info/IPositionInfo4Gap #immutable_method'
        return sf._g
    @property
    def global_runtime_info(sf, /):
        return sf._d

def __():
    from seed.types.IToken import LinenoColumn, PositionInfo4Gap__text_file, PositionInfo4Span, PositionInfo4Span__text_file
    gap0 = PositionInfo4Gap__text_file('', 0, 0, LinenoColumn(1,1), 0)
    gap1 = PositionInfo4Gap__text_file('', 0, 0, LinenoColumn(1,1), 1)
    span0 = PositionInfo4Span__text_file(gap0, gap1)
    tkn0 = BaseToken(span0, 'aaa', None)
    global_runtime_info = None
    inputter = ForkableForwardInputStream__using_LazyListIter(global_runtime_info, gap0, to_LazyListIter(iter([tkn0])))
    assert inputter.tell_gap_position_info() is gap0
    assert inputter.head is tkn0
    assert inputter.tell_gap_position_info() is gap0
    assert inputter.read1() is tkn0
    assert inputter.tell_gap_position_info() is gap1
    assert not inputter.read_le(1)
__()














def mk_gap_position_info_at_ifile_begin(fname, /):
    may_idx6bytes = None
    idx6chars = 0
    lineno_column = LinenoColumn(1,1)
    idx4gap = 0
    gap_position_info = PositionInfo4Gap__text_file(fname, may_idx6bytes, idx6chars, lineno_column, idx4gap)
    return gap_position_info
def mk_forkable_char_stream5txt(global_runtime_info, fname, txt, /):
    '-> ForkableForwardInputStream__using_LazyListIter<Token__char>'
    from io import StringIO
    ifile = StringIO(txt)
    prev_token_end_gap_position_info = mk_gap_position_info_at_ifile_begin(fname)
    return mk_forkable_char_stream5ifile(global_runtime_info, prev_token_end_gap_position_info, ifile)
def mk_forkable_char_stream5ipath(global_runtime_info, ipath, /, *, encoding):
    '-> ForkableForwardInputStream__using_LazyListIter<Token__char>'
    ipath = Path(ipath).resolve()
    fname = ipath.as_posix()
    #xxx:idx6bytes = ifile.tell()
    #xxx:assert idx6bytes == end_gap.may_idx6bytes
    prev_token_end_gap_position_info = mk_gap_position_info_at_ifile_begin(fname)
    r = None
    ifile = open(ipath, 'rt', encoding=encoding)
    try:
        r = mk_forkable_char_stream5ifile(global_runtime_info, prev_token_end_gap_position_info, ifile)
        return r
    finally:
        if r is None:ifile.close()
def mk_forkable_char_stream5ifile(global_runtime_info, prev_token_end_gap_position_info, ifile, /):
    '-> ForkableForwardInputStream__using_LazyListIter<Token__char>'
    r = None
    try:
        it = iter_char_tokens5ifile(prev_token_end_gap_position_info, ifile)
        lazylist_iter = to_LazyListIter(it)
        forkable_char_stream = ForkableForwardInputStream__using_LazyListIter(global_runtime_info, prev_token_end_gap_position_info, lazylist_iter)
        return (r:=forkable_char_stream)
    finally:
        if r is None:ifile.close()
def iter_char_tokens5ifile(prev_token_end_gap_position_info, ifile, /):
    '-> Iter<Token__char>'
    r = None
    try:
        it = _iter_char_tokens5ifile(prev_token_end_gap_position_info, ifile)
        for _ in it:break
        return (r:=it)
    finally:
        if r is None:ifile.close()
def _iter_char_tokens5ifile(prev_token_end_gap_position_info, ifile, /):
    '-> Iter<None;Token__char...>'
    with ifile:
        check_type_is(PositionInfo4Gap__text_file, prev_token_end_gap_position_info)
        yield None
        end_gap = prev_token_end_gap_position_info
        (fname, may_idx6bytes, idx6chars, lineno_column, _idx4gap) = end_gap.args
        may_idx6bytes = None
        while (ch := ifile.read(1)):
            begin_gap = end_gap
            idx6chars += 1
            lineno_column = lineno_column.ifeed_char(ch)
            end_gap = PositionInfo4Gap__text_file(fname, may_idx6bytes, idx6chars, lineno_column, idx6chars)
            tspan = PositionInfo4Span__text_file(begin_gap, end_gap)
            chr_tkn = Token__char(tspan, ch, None)
            yield chr_tkn







__all__
from seed.types.ForkableForwardInputStream import IForkable, IForkable__stamp, IForkable__tell_gap_position_info, IBaseForkableForwardInputStream, BaseForkableForwardInputStream__using_LazyListIter

from seed.types.ForkableForwardInputStream import IForkableForwardInputStream, ForkableForwardInputStream__using_LazyListIter

from seed.types.ForkableForwardInputStream import mk_forkable_char_stream5txt, mk_forkable_char_stream5ipath, mk_forkable_char_stream5ifile, iter_char_tokens5ifile
from seed.types.ForkableForwardInputStream import *
