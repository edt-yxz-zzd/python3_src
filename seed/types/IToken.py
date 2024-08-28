#__all__:goto
r'''[[[
e ../../python3_src/seed/types/IToken.py

seed.types.IToken
py -m nn_ns.app.debug_cmd   seed.types.IToken -x
py -m nn_ns.app.doctest_cmd seed.types.IToken:__doc__ -ht
py_adhoc_call   seed.types.IToken   @f
#]]]'''
__all__ = r'''
IBaseToken
    IToken
        BaseToken
            Token__char
            Token__keyed

IBasePositionInfo
    IPositionInfo4Gap
    IPositionInfo4Span


IBasePositionInfo
    LinenoColumn
    IPositionInfo4Gap
        PositionInfo4Gap__file
            PositionInfo4Gap__text_file
        PositionInfo4Gap__higher_level
    IPositionInfo4Span
        PositionInfo4Span
            PositionInfo4Span__text_file
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.abc.IHashable import IHashable
#from seed.abc.ITotalOrdering import ITotalOrdering5le
from seed.abc.IComparable import IComparable, compare# ITypeComparable, type_compare, check_compare_result, real2compare_result, int2compare_result, compare_by_lt_eq
from seed.tiny_.check import check_type_is, check_type_le, check_int_ge, check_char
#from seed.helper.repr_input import repr_helper
from seed.tiny_._Base4repr import _Base4repr #sf._args4repr = (...)

#see:from seed.types.ForkableForwardInputStream import IForkable, IForkable__stamp, IForkableForwardInputStream, ForkableForwardInputStream__using_LazyListIter

from seed.math.sign_of import sign_of

from seed.types.Either import Cased# Either


___end_mark_of_excluded_global_names__0___ = ...


class IBasePositionInfo(IComparable, IHashable, ABC):
    #class IBasePositionInfo(ITotalOrdering5le, IHashable, ABC):
    __slots__ = ()
    @abstractmethod
    def __hash__(sf, /):
        '-> int'
    @abstractmethod
    def __eq__(sf, ot, /):
        '-> bool'
    def __ne__(sf, ot):
        return not sf == ot
    @abstractmethod
    def ___compare___(sf, ot, /):
        'obj -> ([-1..+1]|NotImplemented)'
    #@abstractmethod
    #def __le__(sf, ot, /):
    #    if not type(ot) is type(sf):
    #        return NotImplemented
    #    raise NotImplementedError
class IPositionInfo4Gap(IBasePositionInfo):
    '#TODO:???:used in:IForkableForwardInputStream.tell_gap_position_info() #eg:(fname,idx6bytes,idx6chars,lineno_column_pair,idx4token)'
    __slots__ = ()
    @property
    @abstractmethod
    def idx4gap(sf, /):
        '-> idx4gap/uint'

class IPositionInfo4Span(IBasePositionInfo):
    'used in:IToken.token_span_position_info #eg:(fname,idx_rng4bytes,idx_rng4chars,lineno_column_pair_rng,idx4token) #[idx4span == begin_gap_position_info.idx4gap == end_gap_position_info.idx4gap-1]'
    __slots__ = ()
    @property
    @abstractmethod
    def begin_gap_position_info(sf, /):
        '-> begin_position_info4gap/IPositionInfo4Gap'
    @property
    @abstractmethod
    def end_gap_position_info(sf, /):
        '-> end_position_info4gap/IPositionInfo4Gap'

    @property
    def idx4span(sf, /):
        '-> idx4span/uint'
        return sf.begin_gap_position_info.idx4gap




class IBaseToken(ABC):
    'used in:IForkableForwardInputStream<IBaseToken>'
    __slots__ = ()
    @property
    #@abstractmethod
    def token_key(sf, /):
        '[Eq tkey =>]: -> tkey/token_key'
        return sf.token_keyed_data.case
    @property
    #@abstractmethod
    def token_data(sf, /):
        '-> tdat/token_data'
        return sf.token_keyed_data.payload
    @property
    @abstractmethod
    def token_keyed_data(sf, /):
        '-> tkd/Cased<tkey,tdat>'
        return Cased(sf.token_key, sf.token_data)

class IToken(IBaseToken):
    #class IToken__with_tspan(IBaseToken):
    'tpstn/tspan/tposition_info/token_span_position_info/IPositionInfo4Span #[idx4token == token_begin_position_info.idx4gap == token_end_position_info.idx4gap-1]'
    __slots__ = ()
    @property
    @abstractmethod
    def token_span_position_info(sf, /):
        '[Eq tspan =>]: -> tspan/token_span_position_info/IPositionInfo4Span'
    @property
    def token_idx(sf, /):
        '-> idx4token/uint'
        return sf.token_span_position_info.idx4span
    @property
    def token_begin_position_info(sf, /):
        '-> tgbegin/begin_position_info4token/IPositionInfo4Gap'
        return sf.token_span_position_info.begin_gap_position_info
    @property
    def token_end_position_info(sf, /):
        '-> tgend/end_position_info4token/IPositionInfo4Gap'
        return sf.token_span_position_info.end_gap_position_info

class BaseToken(IToken, _Base4repr):
    ___no_slots_ok___ = True
    _basetype4tspan_ = IPositionInfo4Span
    @classmethod
    def _check_tkey_(cls, tkey, /):
        '-> None | ^TypeError'
    @classmethod
    def _check_tdat_(cls, tdat, /):
        '-> None | ^TypeError'
    def __init__(sf, tspan, tkd_or_tkey, /, *tmay_tdat):
        if tmay_tdat:
            sf._init__tkey_tdat_(tspan, tkey:=tkd_or_tkey, *tmay_tdat)
        else:
            sf._init__tkd_(tspan, tkd:=tkd_or_tkey)
    def _init__tkey_tdat_(sf, tspan, tkey, tdat, /):
        tkd = Cased(tkey, tdat)
        sf._init__tkd_(tspan, tkd)
    def _init__tkd_(sf, tspan, tkd, /):
        check_type_le(Cased, tkd)
        (tkey, tdat) = tkd
        cls = type(sf)
        check_type_le(cls._basetype4tspan_, tspan)
        cls._check_tkey_(tkey)
        cls._check_tdat_(tdat)
        sf._tspan = tspan
        #sf._tkey = tkey
        #sf._tdat = tdat
        sf._tkd = tkd
        #sf._args4repr = (tspan, tkey, tdat)
        sf._args4repr = (tspan, tkd)
    @property
    @override
    def token_span_position_info(sf, /):
        '[Eq tspan =>]: -> tspan/token_span_position_info/IPositionInfo4Span'
        return sf._tspan
    @property
    @override
    def token_keyed_data(sf, /):
        '-> tkd/Cased<tkey,tdat>'
        return sf._tkd
    #@property
    #@override
    #def token_key(sf, /):
    #    '[Eq tkey =>]: -> tkey/token_key'
    #    return sf._tkey
    #@property
    #@override
    #def token_data(sf, /):
    #    '-> tdat/token_data'
    #    return sf._tdat


class LinenoColumn(IBasePositionInfo, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, jrow, jcolumn, /):
        check_int_ge(1, jrow)
        check_int_ge(1, jcolumn)
        sf._jr = jrow
        sf._jc = jcolumn
        sf._args4repr = (jrow, jcolumn)
    @property
    def lineno(sf, /):
        return sf._jr
    @property
    def column(sf, /):
        return sf._jc
    def ifeed_char(sf, char, /):
        '-> LinenoColumn'
        if char == '\n':
            jrow = 1+sf.lineno
            jcolumn = 1
        else:
            jrow = sf.lineno
            jcolumn = 1+sf.column
        return type(sf)(jrow, jcolumn)
    @override
    def __hash__(sf, /):
        '-> int'
        return hash((type(sf), sf.lineno, sf.column))
    @override
    def __eq__(sf, ot, /):
        '-> bool'
        if sf is ot:
            return True
        return (type(sf) is type(ot)
        and sf.lineno == ot.lineno
        and sf.column == ot.column
        )
    @override
    def ___compare___(sf, ot, /):
        'obj -> ([-1..+1]|NotImplemented)'
        if sf is ot:
            return True
        if not type(ot) is type(sf):
            return NotImplemented
        s = sign_of(sf.lineno - ot.lineno)
        if s == 0:
            s = sign_of(sf.column - ot.column)
        return s

class PositionInfo4Gap__file(IPositionInfo4Gap, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, fname, idx4gap, /):
        check_type_is(str, fname)
        check_int_ge(0, idx4gap)
        sf._fnm = fname
        sf._ig = idx4gap
        sf._args4repr = (fname, idx4gap)
    @property
    def args(sf, /):
        return sf._args4repr
    @property
    def fname(sf, /):
        '-> str'
        return sf._fnm
    @property
    @override
    def idx4gap(sf, /):
        '-> idx4gap/uint'
        return sf._ig
    @override
    def __hash__(sf, /):
        '-> int'
        return hash((type(sf), sf._args4repr))
    @override
    def __eq__(sf, ot, /):
        '-> bool'
        if sf is ot:
            return True
        return (type(sf) is type(ot)
        and sf.idx4gap == ot.idx4gap #move to begin
        and sf._args4repr == ot._args4repr
        )
    @override
    def ___compare___(sf, ot, /):
        'obj -> ([-1..+1]|NotImplemented)'
        if sf is ot:
            return True
        if not type(ot) is type(sf):
            return NotImplemented
        if not sf.fname == ot.fname:raise ValueError((sf.fname, ot.fname))
        return sign_of(sf.idx4gap - ot.idx4gap)


class PositionInfo4Gap__text_file(PositionInfo4Gap__file):
    def __init__(sf, fname, may_idx6bytes, idx6chars, lineno_column, idx4gap, /):
        if not None is may_idx6bytes:
            idx6bytes = may_idx6bytes
            check_int_ge(0, idx6bytes)
        check_int_ge(0, idx6chars)
        check_type_is(LinenoColumn, lineno_column)
        super().__init__(fname, idx4gap)
        sf._args4repr = (fname, may_idx6bytes, idx6chars, lineno_column, idx4gap)
    #def ifeed_char(sf, char, /):
    #    '-> PositionInfo4Gap__text_file'



class PositionInfo4Gap__higher_level(IPositionInfo4Gap, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, low_lvl_gap, idx4gap, /):
        check_type_le(IPositionInfo4Gap, low_lvl_gap)
        check_int_ge(0, idx4gap)
        sf._gp = low_lvl_gap
        sf._ig = idx4gap
        sf._args4repr = (low_lvl_gap, idx4gap)
    @property
    def args(sf, /):
        return sf._args4repr
    @property
    def low_lvl_gap(sf, /):
        '-> IPositionInfo4Gap'
        return sf._gp
    @property
    @override
    def idx4gap(sf, /):
        '-> idx4gap/uint'
        return sf._ig
    @override
    def __hash__(sf, /):
        '-> int'
        return hash((type(sf), sf._args4repr))
    @override
    def __eq__(sf, ot, /):
        '-> bool'
        if sf is ot:
            return True
        return (type(sf) is type(ot)
        and sf.idx4gap == ot.idx4gap #move to begin
        and sf._args4repr == ot._args4repr
        )
    @override
    def ___compare___(sf, ot, /):
        'obj -> ([-1..+1]|NotImplemented)'
        if sf is ot:
            return True
        if not type(ot) is type(sf):
            return NotImplemented
        return sign_of(sf.idx4gap - ot.idx4gap)






class PositionInfo4Span(IPositionInfo4Span, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, tgbegin, tgend, /):
        check_type_le(IPositionInfo4Gap, tgbegin)
        check_type_le(IPositionInfo4Gap, tgend)
        if not tgbegin.idx4gap + 1 == tgend.idx4gap:raise ValueError
        sf._b = tgbegin
        sf._e = tgend
        sf._args4repr = (tgbegin, tgend)
    @property
    @override
    def begin_gap_position_info(sf, /):
        '-> begin_position_info4gap/IPositionInfo4Gap'
        return sf._b
    @property
    @override
    def end_gap_position_info(sf, /):
        '-> end_position_info4gap/IPositionInfo4Gap'
        return sf._e

    @override
    def __hash__(sf, /):
        '-> int'
        return hash((type(sf), sf._args4repr))
    @override
    def __eq__(sf, ot, /):
        '-> bool'
        if sf is ot:
            return True
        return (type(sf) is type(ot)
        and sf._args4repr == ot._args4repr
        )
    @override
    def ___compare___(sf, ot, /):
        'obj -> ([-1..+1]|NotImplemented)'
        if sf is ot:
            return True
        if not type(ot) is type(sf):
            return NotImplemented
        return compare(sf.begin_gap_position_info, ot.end_gap_position_info)

class PositionInfo4Span__text_file(PositionInfo4Span):
    def __init__(sf, tgbegin, tgend, /):
        check_type_is(PositionInfo4Gap__text_file, tgbegin)
        check_type_is(PositionInfo4Gap__text_file, tgend)
        super().__init__(tgbegin, tgend)



def __():
    gap0 = PositionInfo4Gap__text_file('', 0, 0, LinenoColumn(1,1), 0)
    gap1 = PositionInfo4Gap__text_file('', 0, 0, LinenoColumn(1,1), 1)
    span0 = PositionInfo4Span__text_file(gap0, gap1)
__()




class Token__char(BaseToken):
    'char'
    _basetype4tspan_ = PositionInfo4Span__text_file
    @classmethod
    def _check_tkey_(cls, tkey, /):
        '-> None | ^TypeError'
        #ord(tkey)
        check_char(tkey)

class Token__keyed(BaseToken):
    'keyed/Cased'



__all__
from seed.types.IToken import IBaseToken, IToken, BaseToken, Token__char, Token__keyed
from seed.types.IToken import IBasePositionInfo, IPositionInfo4Gap, IPositionInfo4Span
from seed.types.IToken import LinenoColumn, PositionInfo4Gap__file, PositionInfo4Gap__text_file, PositionInfo4Gap__higher_level, PositionInfo4Span, PositionInfo4Span__text_file
from seed.types.IToken import Token__char, PositionInfo4Span__text_file, PositionInfo4Gap__text_file, LinenoColumn
from seed.types.IToken import *
