#__all__:goto
r'''[[[
e ../../python3_src/seed/types/IToken.py

seed.types.IToken
py -m nn_ns.app.debug_cmd   seed.types.IToken -x
py -m nn_ns.app.doctest_cmd seed.types.IToken:__doc__ -ht

[ITokenQuerySet is not subclass of IXQuerySet]
[rawstream := (prev_token_end_gap_position_info, tokens)]

DONE:++noise
    denoise_rawstream_#filter
        PositionInfo4Span
        PositionInfo4Gap__noisy
    <<==:
    ??token_idx/idx4token,idx4gap,idx4span
        PositionInfo4Span:
            '[tgbegin.idx4gap + 1 == tgend.idx4gap]'
        PositionInfo4Gap__higher_level --> PositionInfo4Gap__noisy












[rawstream := (prev_token_end_gap_position_info, tokens)]
>>> def list_rawstream_(rawstream, /):
...     (prev_token_end_gap_position_info, tokens) = rawstream
...     assert tokens is iter(tokens)
...     tokens = [*tokens]
...     return (prev_token_end_gap_position_info, tokens)

>>> list_rawstream_(mk_token_rawstream__5xs__idx_(990, 'ab', 777, tkey_vs_tdat_vs_tkd=0))
(PositionInfo4Gap__idx(990), [BaseToken(PositionInfo4Span(PositionInfo4Gap__idx(990), PositionInfo4Gap__idx(991)), Cased('a', 777)), BaseToken(PositionInfo4Span(PositionInfo4Gap__idx(991), PositionInfo4Gap__idx(992)), Cased('b', 777))])
>>> list_rawstream_(mk_token_rawstream__5xs__idx_(990, 'ab', 777, tkey_vs_tdat_vs_tkd=1))
(PositionInfo4Gap__idx(990), [BaseToken(PositionInfo4Span(PositionInfo4Gap__idx(990), PositionInfo4Gap__idx(991)), Cased(777, 'a')), BaseToken(PositionInfo4Span(PositionInfo4Gap__idx(991), PositionInfo4Gap__idx(992)), Cased(777, 'b'))])
>>> list_rawstream_(mk_token_rawstream__5xs__idx_(990, '', 777, tkey_vs_tdat_vs_tkd=2))
Traceback (most recent call last):
    ...
TypeError: 777
>>> list_rawstream_(mk_token_rawstream__5xs__idx_(990, '', None, tkey_vs_tdat_vs_tkd=2))
(PositionInfo4Gap__idx(990), [])




#>>> from seed.tiny import echo
>>> list_rawstream_(mk_token_rawstream__5xs__idx_(990, 'ab', str.upper, tkey_vs_tdat_vs_tkd=0))
(PositionInfo4Gap__idx(990), [BaseToken(PositionInfo4Span(PositionInfo4Gap__idx(990), PositionInfo4Gap__idx(991)), Cased('a', 'A')), BaseToken(PositionInfo4Span(PositionInfo4Gap__idx(991), PositionInfo4Gap__idx(992)), Cased('b', 'B'))])
>>> list_rawstream_(mk_token_rawstream__5xs__idx_(990, 'ab', str.upper, tkey_vs_tdat_vs_tkd=1))
(PositionInfo4Gap__idx(990), [BaseToken(PositionInfo4Span(PositionInfo4Gap__idx(990), PositionInfo4Gap__idx(991)), Cased('A', 'a')), BaseToken(PositionInfo4Span(PositionInfo4Gap__idx(991), PositionInfo4Gap__idx(992)), Cased('B', 'b'))])

#]]]'''
__all__ = r'''
mk_token_rawstream__5xs__idx_


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
        PositionInfo4Gap__idx
        PositionInfo4Gap__file
            PositionInfo4Gap__text_file
        PositionInfo4Gap__higher_level
        PositionInfo4Gap__noisy
    IPositionInfo4Span
        PositionInfo4Span
            PositionInfo4Span__text_file














denoise_rawstream_
    mk_high_lvl_rawstream5low_high_low_triples_
        mk_rawstream5alternative_gap_tkd_
            mk_rawstream5alternative_gap_tkn_
            alternative_gap_tkn5alternative_gap_tkd_


mk_token_rawstream__5xs__idx_
    iter_tkds__5tkeys_
    iter_tkds__5tdats_
    mk_end_gap_position_info__idx_
    mk_token_rawstream__5tkds_

mk_token_rawstream__5xs__idx_
    mk_token_rawstream__5tkds_
        mk_token_rawstream__5tspan_tkd_pairs_
            attach_tspan_
                attach_tspan__attached_tgend_
                attach_tgend_
                iter_tkds__5tkeys_
                iter_tkds__5tdats_











ITokenQuerySet
    ITokenKeyedDataQuerySet
        ITokenKeyQuerySet
        ITokenDataQuerySet
is_good_token_
    is_good_token_keyed_data_
        is_good_token_key_
        is_good_token_data_













ITokenQuerySet
    TokenQuerySet5xqset
        tkn_qset__empty
        tkn_qset__whole

    ITokenKeyedDataQuerySet
        TokenKeyedDataQuerySet5xqset
            tkd_qset__empty
            tkd_qset__whole

        ITokenKeyQuerySet
            TokenKeyQuerySet5xqset
                tkey_qset__empty
                tkey_qset__whole

        ITokenDataQuerySet
            TokenDataQuerySet5xqset
                tdat_qset__empty
                tdat_qset__whole



is_good
always_tri_test
IXQuerySet  ITester
    XQuerySet__complementary
    XQuerySet5predicator
    XQuerySet5container
    mk_XQuerySet__always
    XQuerySet__named
    CharQuerySet__using_py_str_method
    StrQuerySet__using_py_regex_fullmatch
    StrQuerySet__using_py_regex_match_prefix
    StrQuerySet__using_py_regex_search


XQuerySet__named
    empty_xqset
    whole_xqset
    truth_test_xqset
    falsity_test_xqset
CharQuerySet__using_py_str_method
    char_qset__py_regex__w
    char_qset__py_regex__W
    char_qset__py_regex__s
    char_qset__py_regex__S
    char_qset__py_regex__d
    char_qset__py_regex__D
StrQuerySet__using_py_regex_fullmatch
    char_qset__isalnum
    char_qset__not_isalnum
    char_qset__isalpha
    char_qset__not_isalpha
    char_qset__isascii
    char_qset__not_isascii
    char_qset__isdecimal
    char_qset__not_isdecimal
    char_qset__isdigit
    char_qset__not_isdigit
    char_qset__isidentifier
    char_qset__not_isidentifier
    char_qset__islower
    char_qset__not_islower
    char_qset__isnumeric
    char_qset__not_isnumeric
    char_qset__isprintable
    char_qset__not_isprintable
    char_qset__isspace
    char_qset__not_isspace
    char_qset__istitle
    char_qset__not_istitle
    char_qset__isupper
    char_qset__not_isupper
'''.split()#'''
r'''[[[
deprecated:
.IXQuerySet
.    XQuerySet__complementary
.    XQuerySet5predicator
.    XQuerySet5container
.    IXQuerySet__always
.        XQuerySet__always
.    IXQuerySet5key__init
.        IXQuerySet5mapping_key__init
.        IXQuerySet5obj_attr__init
.            CharQuerySet__using_py_str_method
.    XQuerySet__named
.    StrQuerySet__using_py_regex_fullmatch

#]]]'''#'''
r'''[[[
deprecated:
.ITokenQuerySet
.    ITokenXQuerySet
.        TokenXQuerySet5predicator
.        TokenXQuerySet5container
.
.    ITokenKeyedDataQuerySet
.        ITokenKeyedDataXQuerySet
.            TokenKeyedDataXQuerySet5predicator
.            TokenKeyedDataXQuerySet5container
.
.        ITokenKeyQuerySet
.            ITokenKeyXQuerySet
.                TokenKeyXQuerySet5predicator
.                TokenKeyXQuerySet5container
.
.        ITokenDataQuerySet
.            ITokenDataXQuerySet
.                TokenDataXQuerySet5predicator
.                TokenDataXQuerySet5container


#]]]'''#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#import re
#from collections.abc import Container
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.abc.IHashable import IHashable
#from seed.abc.ITotalOrdering import ITotalOrdering5le
from seed.abc.IComparable import IComparable, compare# ITypeComparable, type_compare, check_compare_result, real2compare_result, int2compare_result, compare_by_lt_eq
from seed.tiny_.check import check_type_is, check_type_le, check_int_ge, check_char, check_non_ABC, check_callable# check_pseudo_qual_name
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

class PositionInfo4Gap__idx(IPositionInfo4Gap, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, idx4gap, /):
        check_int_ge(0, idx4gap)
        sf._ig = idx4gap
        sf._args4repr = (idx4gap,)
    def __add__(sf, offset, /):
        return type(sf)(sf.idx4gap + offset)
    @property
    @override
    def idx4gap(sf, /):
        '-> idx4gap/uint'
        return sf._ig
    @override
    def __hash__(sf, /):
        '-> int'
        return hash((type(sf), sf.idx4gap))
    @override
    def __eq__(sf, ot, /):
        '-> bool'
        if sf is ot:
            return True
        if not type(ot) is type(sf):
            return NotImplemented
        return (type(sf) is type(ot)
        and sf.idx4gap == ot.idx4gap
        )
    @override
    def ___compare___(sf, ot, /):
        'obj -> ([-1..+1]|NotImplemented)'
        if sf is ot:
            return True
        if not type(ot) is type(sf):
            return NotImplemented
        return sign_of(sf.idx4gap - ot.idx4gap)


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
#end-class PositionInfo4Gap__higher_level(IPositionInfo4Gap, _Base4repr):



class PositionInfo4Gap__noisy(IPositionInfo4Gap, _Base4repr):
    'higher_level-asif_pseudo_noisy_low_lvl_span(no:idx4span) <<== IPositionInfo4Span:[tgbegin.idx4gap + 1 == tgend.idx4gap]'
    ___no_slots_ok___ = True
    def __init__(sf, idx4gap, low_lvl_tgbegin, may_low_lvl_tgend, /):
        check_type_le(IPositionInfo4Gap, low_lvl_tgbegin)
        if not may_low_lvl_tgend is None:
            low_lvl_tgend = may_low_lvl_tgend
            check_type_le(IPositionInfo4Gap, low_lvl_tgend)
            if low_lvl_tgend == low_lvl_tgbegin:
                may_low_lvl_tgend = None
                    #for:_args4repr
        ######################
        if may_low_lvl_tgend is None:
            low_lvl_tgend = low_lvl_tgbegin
        ######################
        check_int_ge(0, idx4gap)
        sf._tgb = low_lvl_tgbegin
        sf._tge = low_lvl_tgend
        sf._ig = idx4gap
        sf._args4repr = (idx4gap, low_lvl_tgbegin, may_low_lvl_tgend)
    @property
    def args(sf, /):
        return sf._args4repr
    @property
    def low_lvl_tgbegin(sf, /):
        '-> IPositionInfo4Gap'
        return sf._tgb
    @property
    def low_lvl_tgend(sf, /):
        '-> IPositionInfo4Gap'
        return sf._tge
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

#end-class PositionInfo4Gap__noisy(IPositionInfo4Gap, _Base4repr):



class PositionInfo4Span(IPositionInfo4Span, _Base4repr):
    '[tgbegin.idx4gap + 1 == tgend.idx4gap]'
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





















######################
######################
######################
######################
######################
######################
######################
######################
def denoise_rawstream_(high_lvl_offset, denoiser, low_lvl_rawstream, /):
    'uint -> denoiser/(low_lvl_rawstream -> low_high_low_triples/(Iter (tgbegin/low_lvl-IPositionInfo4Gap, high_lvl-tkd/Cased, tgend/low_lvl-IPositionInfo4Gap))) -> low_lvl_rawstream/(low_lvl-IPositionInfo4Gap, Iter low_lvl-IToken) -> high_lvl_rawstream/(high_lvl-IPositionInfo4Gap, Iter high_lvl-IToken)'
    check_callable(denoiser)
    (low_lvl_prev_token_end_gap_position_info, low_lvl_tokens) = low_lvl_rawstream
    low_high_low_triples = denoiser(low_lvl_rawstream)
    high_lvl_rawstream = mk_high_lvl_rawstream5low_high_low_triples_(high_lvl_offset, low_lvl_prev_token_end_gap_position_info, low_high_low_triples)
    return high_lvl_rawstream
def mk_high_lvl_rawstream5low_high_low_triples_(high_lvl_offset, low_lvl_prev_token_end_gap_position_info, low_high_low_triples, /):
    'uint -> low_lvl-IPositionInfo4Gap -> low_high_low_triples/(Iter (tgbegin/low_lvl-IPositionInfo4Gap, high_lvl-tkd/Cased, tgend/low_lvl-IPositionInfo4Gap)) -> high_lvl_rawstream/(high_lvl-IPositionInfo4Gap, Iter high_lvl-IToken)'
    check_int_ge(0, high_lvl_offset)
    check_type_le(IPositionInfo4Gap, low_lvl_prev_token_end_gap_position_info)
    low_high_low_triples = iter(low_high_low_triples)

    prev_low_lvl_tgend4tokens = low_lvl_prev_token_end_gap_position_info
    low_lvl_tgbegin4noises = prev_low_lvl_tgend4tokens
    high_lvl_rawstream = _4mk_high_lvl_rawstream5LHL(high_lvl_offset, low_lvl_tgbegin4noises, low_high_low_triples)
        #high_lvl_rawstream = (high_lvl_prev_token_end_gap_position_info, high_lvl_tokens)
    return high_lvl_rawstream
def _4mk_high_lvl_rawstream5LHL(high_lvl_offset, low_lvl_tgbegin4noises, low_high_low_triples, /):
    '-> high_lvl_rawstream'
    assert low_high_low_triples is iter(low_high_low_triples)
    alternative_gap_tkd = _high_lvl_GTG5LHL(high_lvl_offset, low_lvl_tgbegin4noises, low_high_low_triples)
    ######################
    #below are all high_lvl
    ######################
    return mk_rawstream5alternative_gap_tkd_(alternative_gap_tkd)
def mk_rawstream5alternative_gap_tkd_(alternative_gap_tkd, /):
    '-> Iter (gap|tkd){alternative}{len>=1}{odd len} -> rawstream/(gap, Iter tkn) # [gap, tkn, gap, tkn, gap, ..., gap]'
    alternative_gap_tkn = alternative_gap_tkn5alternative_gap_tkd_(alternative_gap_tkd)
    return mk_rawstream5alternative_gap_tkn_(alternative_gap_tkn)
def mk_rawstream5alternative_gap_tkn_(alternative_gap_tkn, /):
    '-> Iter (gap|tkn){alternative}{len>=1}{odd len} -> rawstream/(gap, Iter tkn) # [gap, tkn, gap, tkn, gap, ..., gap]'
    it = _4mk_rawstream5GTG_(alternative_gap_tkn)
    prev_token_end_gap_position_info = next(it)
    tokens = it
    rawstream = (prev_token_end_gap_position_info, tokens)
    return rawstream
def _4mk_rawstream5GTG_(alternative_gap_tkn, /):
    it = iter(alternative_gap_tkn)
    777;    del alternative_gap_tkn

    tgbegin = next(it)
    yield tgbegin
    for tkn in it:
        tgend = next(it)
        yield tkn
        ######################
        tgbegin = tgend
    return


def alternative_gap_tkn5alternative_gap_tkd_(alternative_gap_tkd, /):
    '-> Iter (gap|tkd){alternative}{len>=1}{odd len} -> Iter (gap|token){alternative}{len>=1}{odd len} # [gap, tkn, gap, tkn, gap, ..., gap]'
    it = iter(alternative_gap_tkd)
    777;    del alternative_gap_tkd

    tgbegin = next(it)
    yield tgbegin
    for tkd in it:
        tgend = next(it)
        tspan = PositionInfo4Span(tgbegin, tgend)
        #Token__keyed
        tkn = BaseToken(tspan, tkd)
        yield tkn
        yield tgend
        ######################
        tgbegin = tgend
    return

def _high_lvl_GTG5LHL(high_lvl_offset, low_lvl_tgbegin4noises, low_high_low_triples, /):
    '-> Iter (high_lvl_gap|high_lvl_tkd){alternative} # [gap, tkd, gap, tkd, gap, ..., gap]{len>=1}{odd len}'
    assert low_high_low_triples is iter(low_high_low_triples)

    low_lvl_tgbegin4noises
    for (low_lvl_tgbegin4tokens, high_lvl_tkd, low_lvl_tgend4tokens) in low_high_low_triples:
        #low_lvl_tgbegin4noises
        low_lvl_tgend4noises = low_lvl_tgbegin4tokens
        high_lvl_token_end_gap_position_info = PositionInfo4Gap__noisy(idx4gap:=high_lvl_offset, low_lvl_tgbegin4noises, low_lvl_tgend4noises)
        yield high_lvl_token_end_gap_position_info
        yield high_lvl_tkd
        ######################
        high_lvl_offset += 1
        low_lvl_tgbegin4noises = low_lvl_tgend4tokens
        ######################

    else:
        #low_lvl_tgbegin4noises
        low_lvl_tgend4noises = low_lvl_tgbegin4noises
        high_lvl_token_end_gap_position_info = PositionInfo4Gap__noisy(idx4gap:=high_lvl_offset, low_lvl_tgbegin4noises, None)
        yield high_lvl_token_end_gap_position_info
        #no:tkd
            #high_lvl_offset += 1
            #low_lvl_tgbegin4noises = low_lvl_tgend4tokens
    return


######################
######################
######################
def mk_token_rawstream__5tspan_tkd_pairs_(prev_token_end_gap_position_info, tspan_tkd_pairs, /):
    'IPositionInfo4Gap -> Iter (tspan, tkd) -> rawstream/(IPositionInfo4Gap, Iter IToken)'
    check_type_le(IPositionInfo4Gap, prev_token_end_gap_position_info)
    tspan_tkd_pairs = iter(tspan_tkd_pairs)
    tokens = _mk_tail4rawstream__tspan_tkd_pair(tspan_tkd_pairs)
    rawstream = (prev_token_end_gap_position_info, tokens)
    return rawstream
def _mk_tail4rawstream__tspan_tkd_pair(tspan_tkd_pairs, /):
    for (tspan, tkd) in tspan_tkd_pairs:
        yield BaseToken(tspan, tkd)


def attach_tgend_(mk_end_gap_position_info_, prev_token_end_gap_position_info, xs, /):
    '(IPositionInfo4Gap -> x -> IPositionInfo4Gap) -> IPositionInfo4Gap -> Iter x -> Iter (x, tgend)/(x, IPositionInfo4Gap)'
    xs = iter(xs)
    tgend = prev_token_end_gap_position_info
    for x in xs:
        #tgbegin = tgend
        tgend = mk_end_gap_position_info_(tgend, x)
        yield (x, tgend)
def attach_tspan__attached_tgend_(prev_token_end_gap_position_info, x_tgend_pairs, /):
    'IPositionInfo4Gap -> Iter (x, IPositionInfo4Gap) -> Iter (tspan, x)/(IPositionInfo4Span, x)'
    x_tgend_pairs = iter(x_tgend_pairs)
    tgbegin = prev_token_end_gap_position_info
    for x, tgend in x_tgend_pairs:
        tspan = PositionInfo4Span(tgbegin, tgend)
        yield (tspan, x)
        tgbegin = tgend
def attach_tspan_(mk_end_gap_position_info_, prev_token_end_gap_position_info, xs, /):
    '(IPositionInfo4Gap -> x -> IPositionInfo4Gap) -> IPositionInfo4Gap -> Iter x -> Iter (tspan, x)/(IPositionInfo4Span, x)'
    xs = iter(xs)
    x_tgend_pairs = attach_tgend_(mk_end_gap_position_info_, prev_token_end_gap_position_info, xs)
    tspan_x_pairs = attach_tspan__attached_tgend_(prev_token_end_gap_position_info, x_tgend_pairs)
    return tspan_x_pairs

def mk_token_rawstream__5tkds_(mk_end_gap_position_info_, prev_token_end_gap_position_info, tkds, /):
    '(IPositionInfo4Gap -> x -> IPositionInfo4Gap) -> IPositionInfo4Gap -> Iter tkd -> rawstream/(IPositionInfo4Gap, Iter IToken)'
    #check_type_le(IPositionInfo4Gap, prev_token_end_gap_position_info)
    tkds = iter(tkds)
    tspan_tkd_pairs = attach_tspan_(mk_end_gap_position_info_, prev_token_end_gap_position_info, tkds)
    rawstream = mk_token_rawstream__5tspan_tkd_pairs_(prev_token_end_gap_position_info, tspan_tkd_pairs)
    return rawstream


def iter_tkds__5tkeys_(tkeys, tkey2tdat__or__tdat=None, /):
    'Iter tkey -> ((tkey -> tdat)|tdat/non_callable) -> Iter tkd/Cased(tkey,tdat)'
    tkeys = iter(tkeys)
    if callable(tkey2tdat__or__tdat):
        tkey2tdat = tkey2tdat__or__tdat
    else:
        _tdat = tkey2tdat__or__tdat
        def tkey2tdat(tkey, /):
            return _tdat
    tkey2tdat
    return _iter_tkds__5tkeys_(tkeys, tkey2tdat)
def _iter_tkds__5tkeys_(tkeys, tkey2tdat, /):
    for tkey in tkeys:
        tdat = tkey2tdat(tkey)
        tkd = Cased(tkey, tdat)
        yield tkd


def iter_tkds__5tdats_(tdats, tdat2tkey__or__tkey=None, /):
    'Iter tdat -> ((tdat -> tkey)|tkey/non_callable) -> Iter tkd/Cased(tkey,tdat)'
    tdats = iter(tdats)
    if callable(tdat2tkey__or__tkey):
        tdat2tkey = tdat2tkey__or__tkey
    else:
        _tkey = tdat2tkey__or__tkey
        def tdat2tkey(tdat, /):
            return _tkey
    tdat2tkey
    return _iter_tkds__5tdats_(tdats, tdat2tkey)
def _iter_tkds__5tdats_(tdats, tdat2tkey, /):
    for tdat in tdats:
        tkey = tdat2tkey(tdat)
        tkd = Cased(tkey, tdat)
        yield tkd

def mk_end_gap_position_info__idx_(tgbegin, x, /):
    r'''[[[
    # [mk_end_gap_position_info_ :: (IPositionInfo4Gap -> x -> IPositionInfo4Gap)]
    specialized:
        [mk_end_gap_position_info_ :: (PositionInfo4Gap__idx -> x -> PositionInfo4Gap__idx)]

    #]]]'''#'''
    check_type_is(PositionInfo4Gap__idx, tgbegin)
    tgend = tgbegin + 1
    return tgend

def mk_token_rawstream__5xs__idx_(offset, xs, ex_arg=None, /, *, tkey_vs_tdat_vs_tkd:'(0|1|2)'):
    'uint -> Iter (tkey|tdat|tkd) -> (((tkey -> tdat)|tdat/non_callable)|((tdat -> tkey)|tkey/non_callable)|None) -> (tkey_vs_tdat_vs_tkd/(0|1|2)) -> rawstream/(IPositionInfo4Gap, Iter IToken)'
    check_type_is(int, tkey_vs_tdat_vs_tkd)
    xs = iter(xs)
    prev_token_end_gap_position_info = PositionInfo4Gap__idx(offset)
    ##############
    match tkey_vs_tdat_vs_tkd:
        case 0:
            #tkey
            tkey2tdat__or__tdat = ex_arg
            tkds = iter_tkds__5tkeys_(xs, tkey2tdat__or__tdat)
        case 1:
            #tdat
            tdat2tkey__or__tkey = ex_arg
            tkds = iter_tkds__5tdats_(xs, tdat2tkey__or__tkey)
        case 2:
            #tkd
            if not ex_arg is None:raise TypeError(ex_arg)
            tkds = xs
        case _:
            raise TypeError(tkey_vs_tdat_vs_tkd)
    ##############
    tkds
    prev_token_end_gap_position_info
    rawstream = mk_token_rawstream__5tkds_(mk_end_gap_position_info__idx_, prev_token_end_gap_position_info, tkds)
    return rawstream

######################
######################
######################
######################
######################
######################









######################
######################
######################
from seed.types.Tester import is_good, always_tri_test
from seed.types.Tester import (ITester
,IXQuerySet
,   XQuerySet__complementary
,   XQuerySet5predicator
,   XQuerySet5container
,   mk_XQuerySet__always
,   XQuerySet__named
,   CharQuerySet__using_py_str_method
,   StrQuerySet__using_py_regex_fullmatch
,   StrQuerySet__using_py_regex_match_prefix
,   StrQuerySet__using_py_regex_search
#
#
,XQuerySet__named
,   empty_xqset
,   whole_xqset
,   truth_test_xqset
,   falsity_test_xqset
,CharQuerySet__using_py_str_method
,   char_qset__py_regex__w
,   char_qset__py_regex__W
,   char_qset__py_regex__s
,   char_qset__py_regex__S
,   char_qset__py_regex__d
,   char_qset__py_regex__D
,StrQuerySet__using_py_regex_fullmatch
,   char_qset__isalnum
,   char_qset__not_isalnum
,   char_qset__isalpha
,   char_qset__not_isalpha
,   char_qset__isascii
,   char_qset__not_isascii
,   char_qset__isdecimal
,   char_qset__not_isdecimal
,   char_qset__isdigit
,   char_qset__not_isdigit
,   char_qset__isidentifier
,   char_qset__not_isidentifier
,   char_qset__islower
,   char_qset__not_islower
,   char_qset__isnumeric
,   char_qset__not_isnumeric
,   char_qset__isprintable
,   char_qset__not_isprintable
,   char_qset__isspace
,   char_qset__not_isspace
,   char_qset__istitle
,   char_qset__not_istitle
,   char_qset__isupper
,   char_qset__not_isupper
)
assert IXQuerySet is ITester
r'''[[[
view ../../python3_src/seed/types/Tester.py
deprecated IXQuerySet by ITester



.class IXQuerySet(ABC):
.    'xqset#just for __init__'
.    __slots__ = ()
.    @abstractmethod
.    def _is_good_(sf, x, /):
.        'x -> bool'
.    def __invert__(sf, /):
.        return XQuerySet__complementary(sf)
.
.class XQuerySet__complementary(IXQuerySet, _Base4repr):
.    'complementary_set<xqet>'
.    ___no_slots_ok___ = True
.    def __init__(sf, xqset, /):
.        check_type_le(IXQuerySet, xqset)
.        sf._xqs = xqset
.        sf._args4repr = (xqset,)
.    @override
.    def _is_good_(sf, x, /):
.        'x -> bool'
.        return not sf._xqs._is_good_(x)
.    @override
.    def __invert__(sf, /):
.        return sf._xqs
.
.class IXQuerySet__always(IXQuerySet):
.    __slots__ = ()
.    @property
.    @abstractmethod
.    def _always_good_(sf, /):
.        '-> bool'
.    @override
.    def _is_good_(sf, x, /):
.        'x -> bool'
.        return sf._always_good_
.
.
.class XQuerySet5predicator(IXQuerySet, _Base4repr):
.    ___no_slots_ok___ = True
.    def __init__(sf, is_good_, /):
.        check_callable(is_good_)
.        sf._pf = is_good_
.        sf._args4repr = (is_good_,)
.    @property
.    @override
.    def _is_good_(sf, /):
.        '-> (x -> bool)'
.        return sf._pf
.
.class IXQuerySet5key__init(XQuerySet5predicator):
.    ___no_slots_ok___ = True
.    @abstractmethod
.    def _lookup4is_good_(sf, key4is_good, /):
.        'key4is_good -> is_good_/(x -> bool)|^LookupError'
.
.    def __init__(sf, key4is_good, /):
.        is_good_ = sf._lookup4is_good_(key4is_good)
.        super().__init__(is_good_)
.        sf._args4repr = (key4is_good,)
.class IXQuerySet5obj_attr__init(IXQuerySet5key__init):
.    '[key4is_good == nm4is_good]'
.    ___no_slots_ok___ = True
.    @abstractmethod
.    def _is_good_name4is_good_(sf, nm4is_good, /):
.        'nm4is_good -> bool'
.    @property
.    @abstractmethod
.    def _obj4is_good_(sf, /):
.        '-> obj # [is_good_ == getattr(obj, nm4is_good)]'
.    @override
.    def _lookup4is_good_(sf, key4is_good, /):
.        'key4is_good -> is_good_/(x -> bool)|^LookupError'
.        nm4is_good = key4is_good
.        if not sf._is_good_name4is_good_(nm4is_good):raise LookupError(nm4is_good)#AttributeError
.        return getattr(sf._obj4is_good_, nm4is_good)
.
.class IXQuerySet5mapping_key__init(IXQuerySet5key__init):
.    '[key4is_good == nm4is_good]'
.    ___no_slots_ok___ = True
.    @property
.    @abstractmethod
.    def _mapping4is_good_(sf, /):
.        '-> mapping # [is_good_ == mapping[key4is_good]]'
.    @override
.    def _lookup4is_good_(sf, key4is_good, /):
.        'key4is_good -> is_good_/(x -> bool)|^LookupError'
.        return sf._mapping4is_good_[key4is_good]
.
.
.
.
.
.class XQuerySet5container(IXQuerySet, _Base4repr):
.    ___no_slots_ok___ = True
.    def __init__(sf, xs, /):
.        check_type_le(Container, xs)
.        sf._xs = xs
.        sf._args4repr = (xs,)
.    @override
.    def _is_good_(sf, x, /):
.        'x -> bool'
.        return x in sf._xs
.
.class XQuerySet__always(IXQuerySet__always, _Base4repr):
.    ___no_slots_ok___ = True
.    def __init__(sf, b, /):
.        check_type_is(bool, b)
.        sf._b = b
.        sf._args4repr = (b,)
.    @property
.    @override
.    def _always_good_(sf, /):
.        '-> bool'
.        return sf._b
.
.
.
.
.class XQuerySet__named(IXQuerySet):
.    ___no_slots_ok___ = True
.    def __init__(sf, qnm, xqset, /):
.        check_type_le(IXQuerySet, xqset)
.        check_pseudo_qual_name(qnm)
.        sf._qnm = qnm
.        sf._xqs = xqset
.    def __str__(sf, /):
.        return repr_helper(sf, sf._qnm, sf._xqs)
.    def __repr__(sf, /):
.        return sf._qnm
.    @property
.    @override
.    def _is_good_(sf, /):
.        '-> (x -> bool)'
.        return sf._xqs._is_good_
.
.empty_xqset = XQuerySet__named('empty_xqset', XQuerySet__always(False))
.whole_xqset = XQuerySet__named('whole_xqset', XQuerySet__always(True))
.
.
.
.
.
.
.#######
._nms6str = set('isalnum isalpha isascii isdecimal isdigit isidentifier islower isnumeric isprintable isspace istitle isupper'.split())
.
.class CharQuerySet__using_py_str_method(IXQuerySet5obj_attr__init):
.    ___no_slots_ok___ = True
.    @override
.    def _is_good_name4is_good_(sf, nm4is_good, /):
.        'nm4is_good -> bool'
.        return nm4is_good in _nms6str
.    #@override
.    _obj4is_good_ = str
.check_non_ABC(CharQuerySet__using_py_str_method)
.
.class StrQuerySet__using_py_regex_fullmatch(IXQuerySet, _Base4repr):
.    ___no_slots_ok___ = True
.    @override
.    def __init__(sf, py_regex_pattern, /):
.        sf._rex = re.compile(py_regex_pattern)
.        sf._args4repr = (py_regex_pattern,)
.    @override
.    def _is_good_(sf, x, /):
.        'x -> bool'
.        return bool(sf._rex.fullmatch(x))
.
.check_non_ABC(StrQuerySet__using_py_regex_fullmatch)
.
.#######
.def _mk4str_method(nm, /):
.    gnm = f'char_qset__{nm}'
.    gcnm = f'char_qset__not_{nm}'
.
.    _xqset = CharQuerySet__using_py_str_method(nm)
.
.    xqset = XQuerySet__named(gnm, _xqset)
.    complementary_xqset = XQuerySet__named(gcnm, ~_xqset)
.
.    return (xqset, complementary_xqset)
.def _mk4py_char_regex(char, /):
.    check_char(char)
.    assert char.isalpha()
.    assert char.islower()
.    nm = char
.    cnm = char.upper()
.    assert not cnm == nm
.    gnm = f'char_qset__py_regex__{nm}'
.    gcnm = f'char_qset__py_regex__{cnm}'
.    _xqset = StrQuerySet__using_py_regex_fullmatch(rf'\{nm}')
.    _cxqset = StrQuerySet__using_py_regex_fullmatch(rf'\{cnm}')
.
.    xqset = XQuerySet__named(gnm, _xqset)
.    complementary_xqset = XQuerySet__named(gcnm, _cxqset)
.    return (xqset, complementary_xqset)
.
.
.#######
.### (char_qset__py_regex__s, char_qset__py_regex__S) = _mk4py_char_regex('s')
.#:.,.+4s/^\(\w\)\(\w\)$/(char_qset__py_regex__\1, char_qset__py_regex__\2) = _mk4py_char_regex('\1')
.(char_qset__py_regex__w, char_qset__py_regex__W) = _mk4py_char_regex('w')
.(char_qset__py_regex__s, char_qset__py_regex__S) = _mk4py_char_regex('s')
.(char_qset__py_regex__d, char_qset__py_regex__D) = _mk4py_char_regex('d')
.
.#######
.### (char_qset__isalnum, char_qset__not_isalnum) = _mk4str_method('isalnum')
.#:.,.+14s/^\w\+$/(char_qset__\0, char_qset__not_\0) = _mk4str_method('\0')
.(char_qset__isalnum, char_qset__not_isalnum) = _mk4str_method('isalnum')
.(char_qset__isalpha, char_qset__not_isalpha) = _mk4str_method('isalpha')
.(char_qset__isascii, char_qset__not_isascii) = _mk4str_method('isascii')
.(char_qset__isdecimal, char_qset__not_isdecimal) = _mk4str_method('isdecimal')
.(char_qset__isdigit, char_qset__not_isdigit) = _mk4str_method('isdigit')
.(char_qset__isidentifier, char_qset__not_isidentifier) = _mk4str_method('isidentifier')
.(char_qset__islower, char_qset__not_islower) = _mk4str_method('islower')
.(char_qset__isnumeric, char_qset__not_isnumeric) = _mk4str_method('isnumeric')
.(char_qset__isprintable, char_qset__not_isprintable) = _mk4str_method('isprintable')
.(char_qset__isspace, char_qset__not_isspace) = _mk4str_method('isspace')
.(char_qset__istitle, char_qset__not_istitle) = _mk4str_method('istitle')
.(char_qset__isupper, char_qset__not_isupper) = _mk4str_method('isupper')

#]]]'''#'''
#######

######################
######################
######################
class ITokenQuerySet(ABC):
    'tkn_qset # [ITokenQuerySet is not subclass of IXQuerySet]'
    __slots__ = ()
    @abstractmethod
    def _is_good_token_(sf, tkn, /):
        'token/IToken -> bool'
class ITokenKeyedDataQuerySet(ITokenQuerySet):
    'tkd_qset'
    __slots__ = ()
    @abstractmethod
    def _is_good_token_keyed_data_(sf, tkd, /):
        'tkd/Cased<tkey,tdat> -> bool'
    @override
    def _is_good_token_(sf, tkn, /):
        'token/IToken -> bool'
        return sf._is_good_token_keyed_data_(tkd:=tkn.token_keyed_data)


class ITokenKeyQuerySet(ITokenKeyedDataQuerySet):
    'tkey_qset'
    __slots__ = ()
    @abstractmethod
    def _is_good_token_key_(sf, tkey, /):
        'tkey -> bool'
    @override
    def _is_good_token_keyed_data_(sf, tkd, /):
        'tkd/Cased<tkey,tdat> -> bool'
        return sf._is_good_token_key_(tkey:=tkd.case)

class ITokenDataQuerySet(ITokenKeyedDataQuerySet):
    'tdat_qset'
    __slots__ = ()
    @abstractmethod
    def _is_good_token_data_(sf, tdat, /):
        'tdat -> bool'
    @override
    def _is_good_token_keyed_data_(sf, tkd, /):
        'tkd/Cased<tkey,tdat> -> bool'
        return sf._is_good_token_data_(tdat:=tkd.payload)



def is_good_token_(tkn_qset, tkn, /):
    'ITokenQuerySet -> tkn/IToken -> bool'
    check_type_le(IToken, tkn)
    b = tkn_qset._is_good_token_(tkn)
    check_type_is(bool, b)
    return b
def is_good_token_keyed_data_(tkd_qset, tkd, /):
    'ITokenKeyedDataQuerySet -> tkd/Cased<tkey,tdat> -> bool'
    check_type_is(Cased, tkd)
    b = tkd_qset._is_good_token_keyed_data_(tkd)
    check_type_is(bool, b)
    return b
def is_good_token_key_(tkey_qset, tkey, /):
    'ITokenKeyQuerySet -> tkey -> bool'
    b = tkey_qset._is_good_token_key_(tkey)
    check_type_is(bool, b)
    return b
def is_good_token_data_(tdat_qset, tdat, /):
    'ITokenDataQuerySet -> tdat -> bool'
    b = tdat_qset._is_good_token_data_(tdat)
    check_type_is(bool, b)
    return b




######################
######################
######################
class _T5xqset__init(_Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, xqset, /):
        check_type_le(IXQuerySet, xqset)
        sf._xqs = xqset
        sf._args4repr = (xqset,)


class TokenQuerySet5xqset(_T5xqset__init, ITokenQuerySet):
    ___no_slots_ok___ = True
    @override
    def _is_good_token_(sf, tkn, /):
        'token/IToken -> bool'
        #return sf._xqs._is_good_(tkn)
        return is_good(sf._xqs, tkn)
class TokenKeyedDataQuerySet5xqset(_T5xqset__init, ITokenKeyedDataQuerySet):
    ___no_slots_ok___ = True
    @override
    def _is_good_token_keyed_data_(sf, tkd, /):
        'tkd/Cased<tkey,tdat> -> bool'
        #return sf._xqs._is_good_(tkd)
        return is_good(sf._xqs, tkd)
class TokenKeyQuerySet5xqset(_T5xqset__init, ITokenKeyQuerySet):
    ___no_slots_ok___ = True
    @override
    def _is_good_token_key_(sf, tkey, /):
        'tkey -> bool'
        #return sf._xqs._is_good_(tkey)
        return is_good(sf._xqs, tkey)
class TokenDataQuerySet5xqset(_T5xqset__init, ITokenDataQuerySet):
    ___no_slots_ok___ = True
    @override
    def _is_good_token_data_(sf, tdat, /):
        'tdat -> bool'
        #return sf._xqs._is_good_(tdat)
        return is_good(sf._xqs, tdat)
check_non_ABC(TokenQuerySet5xqset)
check_non_ABC(TokenKeyedDataQuerySet5xqset)
check_non_ABC(TokenKeyQuerySet5xqset)
check_non_ABC(TokenDataQuerySet5xqset)

tkn_qset__empty = TokenQuerySet5xqset(empty_xqset)
tkd_qset__empty = TokenKeyedDataQuerySet5xqset(empty_xqset)
tkey_qset__empty = TokenKeyQuerySet5xqset(empty_xqset)
tdat_qset__empty = TokenDataQuerySet5xqset(empty_xqset)

tkn_qset__whole = TokenQuerySet5xqset(whole_xqset)
tkd_qset__whole = TokenKeyedDataQuerySet5xqset(whole_xqset)
tkey_qset__whole = TokenKeyQuerySet5xqset(whole_xqset)
tdat_qset__whole = TokenDataQuerySet5xqset(whole_xqset)


######################
######################
######################
r'''[[[
.
.class ITokenXQuerySet(ITokenQuerySet, IXQuerySet):
.    'tkn_xqset'
.    __slots__ = ()
.    @override
.    def _is_good_token_(sf, tkn, /):
.        'token/IToken -> bool'
.        return sf._is_good_(tkn)
.class ITokenKeyedDataXQuerySet(ITokenKeyedDataQuerySet, IXQuerySet):
.    'tkd_xqset'
.    __slots__ = ()
.    @override
.    def _is_good_token_keyed_data_(sf, tkd, /):
.        'tkd/Cased<tkey,tdat> -> bool'
.        return sf._is_good_(tkd)
.class ITokenKeyXQuerySet(ITokenKeyQuerySet, IXQuerySet):
.    'tkey_xqset'
.    __slots__ = ()
.    @override
.    def _is_good_token_key_(sf, tkey, /):
.        'tkey -> bool'
.        return sf._is_good_(tkey)
.class ITokenDataXQuerySet(ITokenDataQuerySet, IXQuerySet):
.    'tdat_xqset'
.    __slots__ = ()
.    @override
.    def _is_good_token_data_(sf, tdat, /):
.        'tdat -> bool'
.        return sf._is_good_(tdat)
.
.
.
.
.class TokenXQuerySet5predicator(XQuerySet5predicator, ITokenXQuerySet):pass
.class TokenKeyedDataXQuerySet5predicator(XQuerySet5predicator, ITokenKeyedDataXQuerySet):pass
.class TokenKeyXQuerySet5predicator(XQuerySet5predicator, ITokenKeyXQuerySet):pass
.class TokenDataXQuerySet5predicator(XQuerySet5predicator, ITokenDataXQuerySet):pass
.
.check_non_ABC(TokenXQuerySet5predicator)
.check_non_ABC(TokenKeyedDataXQuerySet5predicator)
.check_non_ABC(TokenKeyXQuerySet5predicator)
.check_non_ABC(TokenDataXQuerySet5predicator)
.
.
.class TokenXQuerySet5container(XQuerySet5container, ITokenXQuerySet):pass
.class TokenKeyedDataXQuerySet5container(XQuerySet5container, ITokenKeyedDataXQuerySet):pass
.class TokenKeyXQuerySet5container(XQuerySet5container, ITokenKeyXQuerySet):pass
.class TokenDataXQuerySet5container(XQuerySet5container, ITokenDataXQuerySet):pass
.
.check_non_ABC(TokenXQuerySet5container)
.check_non_ABC(TokenKeyedDataXQuerySet5container)
.check_non_ABC(TokenKeyXQuerySet5container)
.check_non_ABC(TokenDataXQuerySet5container)
.
.
.class TokenXQuerySet__always(XQuerySet__always, ITokenXQuerySet):pass
.class TokenKeyedDataXQuerySet__always(XQuerySet__always, ITokenKeyedDataXQuerySet):pass
.class TokenKeyXQuerySet__always(XQuerySet__always, ITokenKeyXQuerySet):pass
.class TokenDataXQuerySet__always(XQuerySet__always, ITokenDataXQuerySet):pass
.
.check_non_ABC(TokenXQuerySet__always)
.check_non_ABC(TokenKeyedDataXQuerySet__always)
.check_non_ABC(TokenKeyXQuerySet__always)
.check_non_ABC(TokenDataXQuerySet__always)
.
.tkn_xqset__empty = TokenXQuerySet__always(False)
.tkd_xqset__empty = TokenKeyedDataXQuerySet__always(False)
.tkey_xqset__empty = TokenKeyXQuerySet__always(False)
.tdat_xqset__empty = TokenDataXQuerySet__always(False)
.
.tkn_xqset__whole = TokenXQuerySet__always(True)
.tkd_xqset__whole = TokenKeyedDataXQuerySet__always(True)
.tkey_xqset__whole = TokenKeyXQuerySet__always(True)
.tdat_xqset__whole = TokenDataXQuerySet__always(True)
.
#]]]'''#'''
######################
######################
######################


######################
######################
######################
__all__
from seed.types.IToken import IBaseToken, IToken, BaseToken, Token__char, Token__keyed
from seed.types.IToken import IBasePositionInfo, IPositionInfo4Gap, IPositionInfo4Span
from seed.types.IToken import LinenoColumn, PositionInfo4Gap__idx, PositionInfo4Gap__file, PositionInfo4Gap__text_file, PositionInfo4Gap__higher_level, PositionInfo4Gap__noisy, PositionInfo4Span, PositionInfo4Span__text_file
from seed.types.IToken import Token__char, PositionInfo4Span__text_file, PositionInfo4Gap__text_file, LinenoColumn

from seed.types.IToken import mk_token_rawstream__5xs__idx_



from seed.types.IToken import (
ITokenQuerySet
,   ITokenKeyedDataQuerySet
,       ITokenKeyQuerySet
,       ITokenDataQuerySet

,is_good_token_
,   is_good_token_keyed_data_
,       is_good_token_key_
,       is_good_token_data_
)

from seed.types.Tester import is_good, always_tri_test
from seed.types.Tester import ITester, IXQuerySet
from seed.types.IToken import (ITokenQuerySet
,TokenQuerySet5xqset
,TokenKeyedDataQuerySet5xqset
,TokenKeyQuerySet5xqset
,TokenDataQuerySet5xqset
)

from seed.types.IToken import (ITokenQuerySet
,tkn_qset__empty
,tkn_qset__whole
#
,tkd_qset__empty
,tkd_qset__whole
#
,tkey_qset__empty
,tkey_qset__whole
#
,tdat_qset__empty
,tdat_qset__whole
)


from seed.types.IToken import *
