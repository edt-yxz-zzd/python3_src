#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo_/stream/token_stream.py
[inputter :: token_stream/IForkableForwardInputStream<IToken>]

seed.recognize.recognizer_LLoo_.stream.token_stream
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo_.stream.token_stream -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo_.stream.token_stream:__doc__ -ht
py_adhoc_call   seed.recognize.recognizer_LLoo_.stream.token_stream   @f
#]]]'''
__all__ = r'''
mk_LLoo__any_tkey
mk_LLoo__tkey_set

mk_LLoo__match_constant_tkeys
mk_LLoo__match_constant_tkey
mk_LLoo__match_one_of_tkeys
mk_LLoo__raw_string
mk_LLoo__trace
mk_LLoo__traced
mk_LLoo__traced__simple


ITokenKeySetQuery
    ITokenKeySetQuery__wrapper
        TokenKeySetQuery__not
        _ITokenKeySetQuery__op__init
            TokenKeySetQuery__and
            TokenKeySetQuery__or



IRecognizerLLoo__token_set__oresult_is_tkey
    RecognizerLLoo__any_tkey
        recognizer_LLoo__any_tkey
    RecognizerLLoo__tkey_set
IRecognizerLLoo__token_set__oresult_is_tdat
    RecognizerLLoo__any_tdat
        recognizer_LLoo__any_tdat
    RecognizerLLoo__tdat_set
IRecognizerLLoo__token_set__oresult_is_tkd
    RecognizerLLoo__any_tkd
        recognizer_LLoo__any_tkd
    RecognizerLLoo__tkd_set





IRecognizerLLoo__tkey_set
    IRecognizerLLoo__tkey_set__oresult_is_token
    IRecognizerLLoo__tkey_set__oresult_is_tkey
    IRecognizerLLoo__tkey_set__oresult_is_tdat
    IRecognizerLLoo__tkey_set__oresult_is_tkd





RecognizerLLoo__match_constant_tokens
RecognizerLLoo__match_constant_tkeys
RecognizerLLoo__match_constant_tdats
RecognizerLLoo__match_constant_tkds

RecognizerLLoo__match_constant_token
RecognizerLLoo__match_constant_tkey
RecognizerLLoo__match_constant_tdat
RecognizerLLoo__match_constant_tkd


RecognizerLLoo__match_one_of_tokens
RecognizerLLoo__match_one_of_tkeys
RecognizerLLoo__match_one_of_tdats
RecognizerLLoo__match_one_of_tkds


IRecognizerLLoo__raw_string
    RecognizerLLoo__raw_string

IRecognizerLLoo__traced
    RecognizerLLoo__traced
    IRecognizerLLoo__trace
        RecognizerLLoo__trace










tkns2tkns
tkns2tkeys
tkns2tdats
tkns2tkds
'''.split()#'''
#news:
#   mk_LLoo__any_tkey
#   IRecognizerLLoo__token_set__oresult_is_tdat
#   IRecognizerLLoo__token_set__oresult_is_tkd
#   RecognizerLLoo__any_tdat
#   RecognizerLLoo__any_tkd
#   recognizer_LLoo__any_tdat
#   recognizer_LLoo__any_tkd
#   RecognizerLLoo__tdat_set
#   RecognizerLLoo__tkd_set
#   IRecognizerLLoo__tkey_set__oresult_is_tdat
#   IRecognizerLLoo__tkey_set__oresult_is_tkd
#   RecognizerLLoo__match_constant_tdats
#   RecognizerLLoo__match_constant_tkds
#   RecognizerLLoo__match_constant_tdat
#   RecognizerLLoo__match_constant_tkd
#   RecognizerLLoo__match_one_of_tdats
#   RecognizerLLoo__match_one_of_tkds
#   tkns2tkns
#   tkns2tdats
#   tkns2tkds
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.recognize.recognizer_LLoo_._common import (check_non_ABC
,BoxedHalfwayResult, BoxedFinalResult
,mk_Left, mk_Right

,check_non_ABC
,check_type_is, check_type_le, check_int_ge
,mk_tuple, mk_immutable_seq

,IForkable, IForkable__stamp

,abstractmethod, override, ABC, ABC__no_slots
,repr_helper, _Base4repr #sf._args4repr = (...)
)

from seed.recognize.recognizer_LLoo_.stream._common import (IToken
,IForkableForwardInputStream
)

from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import IRecognizerLLoo, Signal__HeaderCompleted, Reply4IRecognizerLLoo
from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import IRecognizerLLoo__leaf, IRecognizerLLoo__no_ref
from seed.recognize.recognizer_LLoo_.combinator_LLoo__wrapper import IRecognizerLLoo__wrapper, _IRecognizerLLoo__wrapper_base__single_ref, recognizer_LLoo__ignore
from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import IDependentTreeNode__no_ref

from seed.tiny import print_err



from seed.recognize.recognizer_LLoo_.stream.pure_stream import \
(_IRecognizerLLoo__any_token
,IRecognizerLLoo__token_set
,IRecognizerLLoo__token_set__oresult_is_token
    #,RecognizerLLoo__token_set
,ITokenSetQuery
,ITokenSetQuery__wrapper
    ,TokenSetQuery__not
    ,_ITokenSetQuery__op__init
        ,TokenSetQuery__and
        ,TokenSetQuery__or

,_IRecognizerLLoo__token_set__init
,_mk_LLoo__token_set
,Case4TokenExtraction
,IRecognizerLLoo__token_related
,recognizer_LLoo__any_token
,RecognizerLLoo__token_set
)
#IRecognizerLLoo__token_set__oresult_is_tkey

___end_mark_of_excluded_global_names__0___ = ...


class IRecognizerLLoo__token_set__oresult_is_tkey(IRecognizerLLoo__token_set):
    'token_set{oresult==tkey}@token_stream'
    __slots__ = ()
    #@override
    _basetype4token_ = IToken #token_stream
    #@property
    #@override
    _case4token_extraction_ = Case4TokenExtraction.tkey
        #_token_vs_tkey_ = True

class IRecognizerLLoo__token_set__oresult_is_tdat(IRecognizerLLoo__token_set):
    'token_set{oresult==tdat}@token_stream'
    __slots__ = ()
    #@override
    _basetype4token_ = IToken #token_stream
    #@property
    #@override
    _case4token_extraction_ = Case4TokenExtraction.tdat

class IRecognizerLLoo__token_set__oresult_is_tkd(IRecognizerLLoo__token_set):
    'token_set{oresult==tkd}@token_stream'
    __slots__ = ()
    #@override
    _basetype4token_ = IToken #token_stream
    #@property
    #@override
    _case4token_extraction_ = Case4TokenExtraction.tkd



class RecognizerLLoo__any_tkey(_IRecognizerLLoo__any_token, IRecognizerLLoo__token_set__oresult_is_tkey):
    'any_tkey@token_stream'
    __slots__ = ()
class RecognizerLLoo__any_tdat(_IRecognizerLLoo__any_token, IRecognizerLLoo__token_set__oresult_is_tdat):
    'any_tdat@token_stream'
    __slots__ = ()
class RecognizerLLoo__any_tkd(_IRecognizerLLoo__any_token, IRecognizerLLoo__token_set__oresult_is_tkd):
    'any_tkd@token_stream'
    __slots__ = ()
check_non_ABC(RecognizerLLoo__any_tkey)
check_non_ABC(RecognizerLLoo__any_tdat)
check_non_ABC(RecognizerLLoo__any_tkd)
recognizer_LLoo__any_tkey = RecognizerLLoo__any_tkey()

recognizer_LLoo__any_tdat = RecognizerLLoo__any_tdat()

recognizer_LLoo__any_tkd = RecognizerLLoo__any_tkd()




class RecognizerLLoo__tkey_set(_IRecognizerLLoo__token_set__init, IRecognizerLLoo__token_set__oresult_is_tkey):
    'tkey_set@token_stream #see:TokenSetQuery__not/TokenKeySetQuery__not'
class RecognizerLLoo__tdat_set(_IRecognizerLLoo__token_set__init, IRecognizerLLoo__token_set__oresult_is_tdat):
    'tdat_set@token_stream #see:TokenSetQuery__not/TokenKeySetQuery__not'
class RecognizerLLoo__tkd_set(_IRecognizerLLoo__token_set__init, IRecognizerLLoo__token_set__oresult_is_tkd):
    'tkd_set@token_stream #see:TokenSetQuery__not/TokenKeySetQuery__not'
check_non_ABC(RecognizerLLoo__tkey_set)
check_non_ABC(RecognizerLLoo__tdat_set)
check_non_ABC(RecognizerLLoo__tkd_set)





















class ITokenKeySetQuery(ITokenSetQuery):
    'tkey_set@token_stream'
    __slots__ = ()
    #@property
    _base_type4tkey_ = object
    _base_type4token_ = IToken #token_stream
    def _check_tkey_(sf, token, /):
        '-> None | ^TypeError'
        if not (T := sf._base_type4tkey_) is object:
            check_type_le(T, token)
    #@override
    def _check_token_(sf, token, /):
        '-> None | ^TypeError'
        super()._check_token_(token)
        sf._check_tkey_(token.token_key)

    @abstractmethod
    def _is_good_tkey_(sf, tkey, /):
        '-> bool'

    #@override
    _basetype4token_ = IToken #token_stream
    @override
    def _is_good_token_(sf, token, /):
        '-> bool'
        return sf._is_good_tkey_(token.token_key)
    @override
    def __invert__(sf, /):
        '-> ITokenKeySetQuery'
        return TokenKeySetQuery__not(sf)
    def __and__(sf, ot, /):
        '-> ITokenSetQuery'
        T = TokenKeySetQuery__and if isinstance(ot, ITokenKeySetQuery) else TokenSetQuery__and
        return T([sf, ot])
    def __or__(sf, ot, /):
        '-> ITokenSetQuery'
        T = TokenKeySetQuery__or if isinstance(ot, ITokenKeySetQuery) else TokenSetQuery__or
        return T([sf, ot])

    def is_good_tkey(sf, tkey, /):
        '-> bool'
        sf._check_tkey_(tkey)
            # ^TypeError
        r = sf._is_good_tkey_(tkey)
        check_type_is(bool, r)
        return r

class _ITokenKeySetQuery__op__init(_ITokenSetQuery__op__init, ITokenKeySetQuery):
    #@override
    _base_type4arg4op_ = ITokenKeySetQuery
    #@override
    _is_good_token_ = ITokenKeySetQuery._is_good_token_
    #@override
    __invert__ = ITokenKeySetQuery.__invert__
    #@override
    __and__ = ITokenKeySetQuery.__and__
    #@override
    __or__ = ITokenKeySetQuery.__or__

class TokenKeySetQuery__and(TokenSetQuery__and, _ITokenKeySetQuery__op__init):
    #@override
    _is_good_token_ = ITokenKeySetQuery._is_good_token_
    @override
    def _is_good_tkey_(sf, tkey, /):
        '-> bool'
        return all(tq.is_good_tkey(tkey) for tq in sf._ls4token_set_query_)

class TokenKeySetQuery__or(TokenSetQuery__or, _ITokenKeySetQuery__op__init):
    #@override
    _is_good_token_ = ITokenKeySetQuery._is_good_token_
    @override
    def _is_good_tkey_(sf, tkey, /):
        '-> bool'
        return any(tq.is_good_tkey(tkey) for tq in sf._ls4token_set_query_)

class ITokenKeySetQuery__wrapper(ITokenSetQuery__wrapper, ITokenKeySetQuery):
    __slots__ = ()
    #@override
    _base_type4wrapped_obj_ = ITokenKeySetQuery
    #@override
    _is_good_token_ = ITokenKeySetQuery._is_good_token_
    @override
    def _is_good_tkey_(sf, tkey, /):
        '-> bool'
        return sf.the_wrapped_obj._is_good_tkey_(tkey)

class TokenKeySetQuery__not(TokenSetQuery__not, ITokenKeySetQuery__wrapper):
    #@override
    _is_good_token_ = ITokenKeySetQuery._is_good_token_
    #@override
    _base_type4wrapped_obj_ = ITokenKeySetQuery
    @override
    def _is_good_tkey_(sf, tkey, /):
        '-> bool'
        return not sf.the_wrapped_obj.is_good_tkey(tkey)
    @override
    def __invert__(sf, /):
        '-> ITokenKeySetQuery'
        return sf.the_wrapped_obj
    #@override
    __and__ = ITokenKeySetQuery.__and__
    #@override
    __or__ = ITokenKeySetQuery.__or__
check_non_ABC(TokenKeySetQuery__not)






class IRecognizerLLoo__tkey_set(IRecognizerLLoo__token_set):
    'tkey_set@token_stream'
    __slots__ = ()
    @property
    @abstractmethod
    def _tkey_set_query_(sf, /):
        '-> ITokenKeySetQuery'
    @property
    @override
    def _token_set_query_(sf, /):
        '-> ITokenSetQuery'
        tkey_set_query = sf._tkey_set_query_
        check_type_le(ITokenKeySetQuery)
        return tkey_set_query


class IRecognizerLLoo__tkey_set__oresult_is_token(IRecognizerLLoo__tkey_set, IRecognizerLLoo__token_set__oresult_is_token):
    'tkey_set{oresult==token}@token_stream'
    __slots__ = ()

class IRecognizerLLoo__tkey_set__oresult_is_tkey(IRecognizerLLoo__tkey_set, IRecognizerLLoo__token_set__oresult_is_tkey):
    'tkey_set{oresult==tkey}@token_stream'
    __slots__ = ()

class IRecognizerLLoo__tkey_set__oresult_is_tdat(IRecognizerLLoo__tkey_set, IRecognizerLLoo__token_set__oresult_is_tdat):
    'tkey_set{oresult==tdat}@token_stream'
    __slots__ = ()

class IRecognizerLLoo__tkey_set__oresult_is_tkd(IRecognizerLLoo__tkey_set, IRecognizerLLoo__token_set__oresult_is_tkd):
    'tkey_set{oresult==tkd}@token_stream'
    __slots__ = ()




























class _IRecognizerLLoo__match_constant_tkeys(IRecognizerLLoo__token_related, IRecognizerLLoo__leaf):
    'match_constant_tkeys@token_stream'
    __slots__ = ()
    #@property
    #@override
    ___666_tribool_skip4serial4LLoo_999___ = False # False-append;True-skip;...-extend
    ##@property
    ##@abstractmethod
    ##def _tkeys_vs_tokens_(sf, /):
    ##    '-> bool'
        #replaced by:_case4token_extraction_
    @property
    @abstractmethod
    def _to_unbox_tkeys_(sf, /):
        '-> bool'
    @property
    @abstractmethod
    def _tkeys_(sf, /):
        '-> tkeys/[tkey]'

    @override
    def _iter4two_phases_recognize_(sf, inputter4whole, /):
        check_type_le(IForkableForwardInputStream, inputter4whole) #token_stream
        tkeys = sf._tkeys_
        #tkeys_vs_tokens = sf._tkeys_vs_tokens_
        extract_token = sf._case4token_extraction_._extract_token_
        ts = []
        for j, tkey in enumerate(tkeys):
            tmay_token = inputter4whole.read_le(1)
            eof = not tmay_token
            if eof:
                eresult = mk_Left('eof')
                break
            [tkn] = tmay_token
            check_type_le(IToken, tkn)
            _tkey = tkn.token_key
            if not _tkey == tkey:
                eresult = mk_Left((j, tkey, _tkey))
                break
            #t = _tkey if tkeys_vs_tokens is False else tkn
            t = extract_token(tkn)
            ts.append(t)
        else:
            if sf._to_unbox_tkeys_:
                [oresult] = ts
            else:
                oresult = mk_tuple(ts)
            eresult = mk_Right(oresult)
        eresult
        reply4LLoo = Reply4IRecognizerLLoo(inputter4whole, eresult)
        #assert inputter4whole is reply4LLoo.the_inputter4end
        return BoxedFinalResult(reply4LLoo)
        777;    yield


class _IRecognizerLLoo__match_constant_tkeys__init(_IRecognizerLLoo__match_constant_tkeys, _Base4repr):
    'match_constant_tkeys@token_stream'
    ___no_slots_ok___ = True
    def __init__(sf, tkeys, /):
        tkeys = mk_immutable_seq(tkeys)
        sf._ks = tkeys
        sf._args4repr = (tkeys,)
    #@property
    #@override
    _to_unbox_tkeys_ = False
    @property
    @override
    def _tkeys_(sf, /):
        '-> tkeys/[tkey]'
        return sf._ks

class _IRecognizerLLoo__match_constant_tkey__init(_IRecognizerLLoo__match_constant_tkeys__init):
    'match_constant_tkey@token_stream'
    ___no_slots_ok___ = True
    def __init__(sf, tkey, /):
        tkeys = (tkey,)
        super().__init__(tkeys)
        sf._args4repr = tkeys#(tkey,)
    #@property
    #@override
    _to_unbox_tkeys_ = True




class RecognizerLLoo__match_constant_tkeys(_IRecognizerLLoo__match_constant_tkeys__init):
    'match_constant_tkeys@token_stream'
    #@property
    #@override
    _case4token_extraction_ = Case4TokenExtraction.tkey
        #_tkeys_vs_tokens_ = False

class RecognizerLLoo__match_constant_tokens(_IRecognizerLLoo__match_constant_tkeys__init):
    'match_constant_tokens@token_stream'
    #@property
    #@override
    _case4token_extraction_ = Case4TokenExtraction.token
        #_tkeys_vs_tokens_ = True

class RecognizerLLoo__match_constant_tdats(_IRecognizerLLoo__match_constant_tkeys__init):
    'match_constant_tdats@token_stream'
    #@property
    #@override
    _case4token_extraction_ = Case4TokenExtraction.tdat
class RecognizerLLoo__match_constant_tkds(_IRecognizerLLoo__match_constant_tkeys__init):
    'match_constant_tkds@token_stream'
    #@property
    #@override
    _case4token_extraction_ = Case4TokenExtraction.tkd

class RecognizerLLoo__match_constant_tkey(_IRecognizerLLoo__match_constant_tkey__init):
    'match_constant_tkey@token_stream'
    #@property
    #@override
    _case4token_extraction_ = Case4TokenExtraction.tkey
        #_tkeys_vs_tokens_ = False

class RecognizerLLoo__match_constant_token(_IRecognizerLLoo__match_constant_tkey__init):
    'match_constant_token@token_stream'
    #@property
    #@override
    _case4token_extraction_ = Case4TokenExtraction.token
        #_tkeys_vs_tokens_ = True

class RecognizerLLoo__match_constant_tdat(_IRecognizerLLoo__match_constant_tkey__init):
    'match_constant_tdat@token_stream'
    #@property
    #@override
    _case4token_extraction_ = Case4TokenExtraction.tdat
class RecognizerLLoo__match_constant_tkd(_IRecognizerLLoo__match_constant_tkey__init):
    'match_constant_tkd@token_stream'
    #@property
    #@override
    _case4token_extraction_ = Case4TokenExtraction.tkd

check_non_ABC(RecognizerLLoo__match_constant_token)
check_non_ABC(RecognizerLLoo__match_constant_tkey)
check_non_ABC(RecognizerLLoo__match_constant_tdat)
check_non_ABC(RecognizerLLoo__match_constant_tkd)

check_non_ABC(RecognizerLLoo__match_constant_tokens)
check_non_ABC(RecognizerLLoo__match_constant_tkeys)
check_non_ABC(RecognizerLLoo__match_constant_tdats)
check_non_ABC(RecognizerLLoo__match_constant_tkds)























RecognizerLLoo__match_constant_tkey
RecognizerLLoo__match_constant_token

class _IRecognizerLLoo__match_one_of_tkeys(IRecognizerLLoo__token_related, IRecognizerLLoo__leaf):
    __slots__ = ()
    #@property
    #@override
    ___666_tribool_skip4serial4LLoo_999___ = False # False-append;True-skip;...-extend
    ##@property
    ##@abstractmethod
    ##def _tkey_vs_token_(sf, /):
    ##    '-> bool'
        #replaced by:_case4token_extraction_
    @property
    @abstractmethod
    def _tkeys_(sf, /):
        '-> tkeys/[tkey]'

    @override
    def _iter4two_phases_recognize_(sf, inputter4whole, /):
        check_type_le(IForkableForwardInputStream, inputter4whole) #token_stream
        tkeys = sf._tkeys_
        #tkey_vs_token = sf._tkey_vs_token_
        extract_token = sf._case4token_extraction_._extract_token_
        tmay_token = inputter4whole.read_le(1)
        eof = not tmay_token
        while 1:
            if eof:
                eresult = mk_Left('eof')
                break
            [tkn] = tmay_token
            check_type_le(IToken, tkn)
            _tkey = tkn.token_key
            if not _tkey in tkeys:
                eresult = mk_Left((tkeys, _tkey))
                break
            #t = _tkey if tkey_vs_token is False else tkn
            t = extract_token(tkn)
            eresult = mk_Right(t)
            break
        eresult
        reply4LLoo = Reply4IRecognizerLLoo(inputter4whole, eresult)
        return BoxedFinalResult(reply4LLoo)
        777;    yield



class _IRecognizerLLoo__match_one_of_tkeys__init(_IRecognizerLLoo__match_one_of_tkeys):
    ___no_slots_ok___ = True
    def __init__(sf, tkeys, /):
        tkeys.__contains__
        #tkeys = mk_immutable_seq(tkeys)
        #??set(tkeys)??
        sf._ks = tkeys
        sf._args4repr = (tkeys,)
    @property
    @override
    def _tkeys_(sf, /):
        '-> tkeys/[tkey]'
        return sf._ks




class RecognizerLLoo__match_one_of_tkeys(_IRecognizerLLoo__match_one_of_tkeys__init):
    #@property
    #@override
    _case4token_extraction_ = Case4TokenExtraction.tkey
        #_tkey_vs_token_ = False

class RecognizerLLoo__match_one_of_tokens(_IRecognizerLLoo__match_one_of_tkeys__init):
    #@property
    #@override
    _case4token_extraction_ = Case4TokenExtraction.token
        #_tkey_vs_token_ = True
class RecognizerLLoo__match_one_of_tdats(_IRecognizerLLoo__match_one_of_tkeys__init):
    #@property
    #@override
    _case4token_extraction_ = Case4TokenExtraction.tdat
class RecognizerLLoo__match_one_of_tkds(_IRecognizerLLoo__match_one_of_tkeys__init):
    #@property
    #@override
    _case4token_extraction_ = Case4TokenExtraction.tkd

check_non_ABC(RecognizerLLoo__match_one_of_tokens)
check_non_ABC(RecognizerLLoo__match_one_of_tkeys)
check_non_ABC(RecognizerLLoo__match_one_of_tdats)
check_non_ABC(RecognizerLLoo__match_one_of_tkds)








def tkns2tkns(tkns, /):
    tkns = mk_tuple(tkns)
    return tkns
def tkns2tkeys(tkns, /):
    tkeys = mk_tuple(tkn.token_key for tkn in tkns)
    return tkeys
def tkns2tdats(tkns, /):
    tdats = mk_tuple(tkn.token_data for tkn in tkns)
    return tdats
def tkns2tkds(tkns, /):
    tkds = mk_tuple(tkn.token_keyed_data for tkn in tkns)
    return tkds

class IRecognizerLLoo__raw_string(IRecognizerLLoo__token_related):
    #class IRecognizerLLoo__raw_string(IRecognizerLLoo):
    'raw_string@token_stream #format: regex"(?P<tag>[^{sep8open}{sep8end}]*?){sep8open}.*?{sep8end}(?P=tag)"'
    __slots__ = ()
    _validated_args4raw_string_LLoo_ = False
    ##def _validate_args4raw_string_LLoo_(sf, tkeys_vs_tokens, oresult_with_tag4raw_string, set4sep8open, set4sep8close, set4token6tag, /):
    ##    check_type_is(bool, tkeys_vs_tokens)
    def _validate_args4raw_string_LLoo_(sf, case4token_extraction, oresult_with_tag4raw_string, set4sep8open, set4sep8close, set4token6tag, /):
        check_type_is(Case4TokenExtraction, case4token_extraction)
        check_type_is(bool, oresult_with_tag4raw_string)
        check_type_le(ITokenKeySetQuery, set4sep8open)
        check_type_le(ITokenKeySetQuery, set4sep8close)
        check_type_le(ITokenKeySetQuery, set4token6tag)

    ##@property
    ##@abstractmethod
    ##def _tkeys_vs_tokens_(sf, /):
    ##    '-> bool'
        #replaced by:_case4token_extraction_
    @property
    @abstractmethod
    def _oresult_with_tag4raw_string_(sf, /):
        '-> bool'
    @property
    @abstractmethod
    def _set4sep8open4tag4raw_string_(sf, /):
        '-> set4sep8open/ITokenKeySetQuery'
    @property
    @abstractmethod
    def _set4sep8close4tag4raw_string_(sf, /):
        '-> set4sep8close/ITokenKeySetQuery'
    @property
    @abstractmethod
    def _set4token6tag4raw_string_(sf, /):
        '-> set4token6tag/ITokenKeySetQuery'
    ##@property
    ##@abstractmethod
    ##def _rgnr4open_tag4raw_string_(sf, /):
    ##    '-> rgnr4open_tag/IRecognizerLLoo{oresult::(([tkey]|[token]),(tkey|token))}'
    ##    rgnr4sep8open = sf._rgnr4sep8open4tag4raw_string_
    ##    rgnr4sep8end = sf._rgnr4sep8end4tag4raw_string_
    ##    rgnr4token6tag = sf._rgnr4token6tag4raw_string_
    ##    #ls = [rgnr4sep8open, rgnr4sep8end] if not rgnr4sep8open is rgnr4sep8end else [rgnr4sep8open]
    ##    #the_first_one__tagged(ls)
    ##    t = _unpack(_tuple(_not_followed_by(rgnr4sep8end),_pack(rgnr4token6tag))) if not rgnr4sep8open is rgnr4sep8end else _pack(rgnr4token6tag)
    ##    rgnr4open_tag = _post(partition_last, _end_by(_pack(rgnr4sep8open), t))
    ##        # partition_last :: [a]{len>=1} -> ([a], a)
    ##    return rgnr4open_tag
    ##def _mk_rgnr4close_tag4raw_string_(sf, tkeys4tag, /):
    ##    '-> rgnr4close_tag/IRecognizerLLoo{oresult::((tkey|token),([tkey]|[token]))}'
    ##    rgnr4sep8end = sf._rgnr4sep8end4tag4raw_string_
    ##    rgnr4close_tag = _tuple(_pack(rgnr4sep8end), _pack(match_constant_tkeys(tkeys4tag)))
    ##        # partition_first :: [a]{len>=1} -> (a, [a])
    ##    return rgnr4close_tag

    @override
    def _iter4two_phases_recognize_(sf, inputter4whole, /):
        check_type_le(IForkableForwardInputStream, inputter4whole) #token_stream
        #tkeys_vs_tokens = sf._tkeys_vs_tokens_
        case4token_extraction = sf._case4token_extraction_
        extract_token = case4token_extraction._extract_token_
        oresult_with_tag4raw_string = sf._oresult_with_tag4raw_string_

        set4sep8open = sf._set4sep8open4tag4raw_string_
        set4sep8close = sf._set4sep8close4tag4raw_string_
        set4token6tag = sf._set4token6tag4raw_string_

        if not sf._validated_args4raw_string_LLoo_:
            #sf._validate_args4raw_string_LLoo_(tkeys_vs_tokens, oresult_with_tag4raw_string, set4sep8open, set4sep8close, set4token6tag)
            sf._validate_args4raw_string_LLoo_(case4token_extraction, oresult_with_tag4raw_string, set4sep8open, set4sep8close, set4token6tag)


        inputter = inputter4whole
        del inputter4whole
        tkns8open_tag = []
        while 1:
            if inputter.eof:
                return BoxedFinalResult(Reply4IRecognizerLLoo(inputter, mk_Left('eof')))
            tkn = inputter.read1()
            tkey = tkn.token_key
            if set4sep8open.is_good_tkey(tkey):
                tkn8open = tkn
                break
            # [tkn !<- (set4sep8open)]
            elif set4sep8close is not set4sep8open and set4sep8close.is_good_tkey(tkey):
                return BoxedFinalResult(Reply4IRecognizerLLoo(inputter, mk_Left(('sep4end before sep4open', tkn))))
            # [tkn !<- (set4sep8open\-/set4sep8close)]
            elif not set4token6tag.is_good_tkey(tkey):
                # [tkn !<- (set4sep8open\-/set4sep8close\-/set4token6tag)]
                return BoxedFinalResult(Reply4IRecognizerLLoo(inputter, mk_Left(('not in (set4sep8open\-/set4sep8close\-/set4token6tag)', tkn))))
            # [tkn !<- (set4sep8open\-/set4sep8close)][tkn <- set4token6tag]
            tkns8open_tag.append(tkn)
        tkn8open
        tkns8open_tag = mk_tuple(tkns8open_tag)
        tkeys8open_tag = tkns2tkeys(tkns8open_tag)
        if case4token_extraction is Case4TokenExtraction.token:
            infos8open_tag = tkns8open_tag
        elif case4token_extraction is Case4TokenExtraction.tkey:
            infos8open_tag = tkeys8open_tag
        else:
            infos8open_tag = mk_tuple(map(extract_token, tkns8open_tag))
        infos8open_tag

        ######################
        ######################
        ######################
        tkns8open_tag, tkeys8open_tag, infos8open_tag
        tkn8open
        info8open = extract_token(tkn8open)
        hresult = (infos8open_tag, info8open)
        ##if tkeys_vs_tokens is False:
        ##    tkey8open = tkn8open.token_key
        ##    hresult = (tkeys8open_tag, tkey8open)
        ##else:
        ##    hresult = (tkns8open_tag, tkn8open)
        ##hresult
        yield BoxedHalfwayResult(Signal__HeaderCompleted(inputter, hresult))
        ######################
        ######################
        ######################

        tkns8raw_string = []
        ending = False
        L = len(tkeys8open_tag)
        remain_tkn = False
        while not (ending and len(tkns8end_tag) == L):
            if remain_tkn:
                remain_tkn = False
                assert not ending
                tkn
            else:
                if inputter.eof:
                    return BoxedFinalResult(Reply4IRecognizerLLoo(inputter, mk_Left('eof')))
                tkn = inputter.read1()
            tkn
            tkey = tkn.token_key
            if not ending:
                if set4sep8close.is_good_tkey(tkey):
                    tkn8end = tkn
                    tkns8end_tag = []
                    ending = True
                else:
                    # [tkn !<- (set4sep8close)]
                    tkns8raw_string.append(tkn)
                del tkn
                continue
            idx6tkeys = len(tkns8end_tag)
            tkey = tkeys8open_tag[idx6tkeys]
            if not tkn.token_key == tkey:
                tkns8raw_string.append(tkn8end)
                tkns8raw_string += tkns8end_tag
                del tkn8end, tkns8end_tag
                ending = False
                remain_tkn = True
                    #xxx:tkns8raw_string.append(tkn)
                    #xxx:del tkn
                continue
            tkns8end_tag.append(tkn)
            del tkn
        assert not remain_tkn


        tkn8end
        tkns8end_tag = mk_tuple(tkns8end_tag)
        tkns8raw_string = mk_tuple(tkns8raw_string)
        ######################
        ######################
        ######################
        tkns8open_tag, tkeys8open_tag, infos8open_tag
        tkn8open, info8open
        tkns8raw_string
        tkn8end
        tkns8end_tag
        ######################
        if case4token_extraction is Case4TokenExtraction.token:
            infos8raw_string = tkns8raw_string
            info8end = tkn8end
            infos8end_tag = tkns8end_tag
        else:
            infos8raw_string = mk_tuple(map(extract_token, tkns8raw_string))
            info8end = extract_token(tkn8end)
            infos8end_tag = mk_tuple(map(extract_token, tkns8end_tag))
        oresult = (infos8open_tag, info8open, infos8raw_string, info8end, infos8end_tag)
        ##if tkeys_vs_tokens is False:
        ##    tkeys8open_tag
        ##    tkey8open
        ##    tkeys8raw_string = tkns2tkeys(tkns8raw_string)
        ##    tkey8end = tkn8end.token_key
        ##    tkeys8end_tag = tkns2tkeys(tkns8end_tag)
        ##    oresult = (tkeys8open_tag, tkey8open, tkeys8raw_string, tkey8end, tkeys8end_tag)
        ##else:
        ##    oresult = (tkns8open_tag, tkn8open, tkns8raw_string, tkn8end, tkns8end_tag)
        ##oresult
        if not oresult_with_tag4raw_string:
            oresult = oresult[2] #raw_string
        oresult
        eresult = mk_Right(oresult)
        reply4LLoo = Reply4IRecognizerLLoo(inputter, eresult)
        return BoxedFinalResult(reply4LLoo)
        777;    yield
        ######################

    @override
    def _iter_direct_child_dependent_tree_nodes_(sf, /):
        '-> Iter IDependentTreeNode'
        set4sep8open = sf._set4sep8open4tag4raw_string_
        set4sep8close = sf._set4sep8close4tag4raw_string_
        set4token6tag = sf._set4token6tag4raw_string_
        yield set4sep8open
        yield set4sep8close
        yield set4token6tag
        return
    #@property
    #@override
    ___666_tribool_skip4serial4LLoo_999___ = False # False-append;True-skip;...-extend


def nm_or2case4token_extraction(nm_or_case4token_extraction, /):
    '(nm/str|Case4TokenExtraction) -> Case4TokenExtraction'
    if type(nm_or_case4token_extraction) is str:
        nm = nm_or_case4token_extraction
        try:
            case4token_extraction = Case4TokenExtraction[nm]
        except KeyError:
            raise TypeError(KeyError(nm))
    else:
        case4token_extraction = nm_or_case4token_extraction
    check_type_is(Case4TokenExtraction, case4token_extraction)
    return case4token_extraction

class RecognizerLLoo__raw_string(IRecognizerLLoo__raw_string, IRecognizerLLoo__no_ref, _Base4repr):
    'raw_string@token_stream #format: regex"(?P<tag>[^{sep8open}{sep8end}]*?){sep8open}.*?{sep8end}(?P=tag)"'
    ___no_slots_ok___ = True
    def __init__(sf, nm_or_case4token_extraction, oresult_with_tag4raw_string, set4sep8open, set4sep8close, set4token6tag, /):
        case4token_extraction = nm_or2case4token_extraction(nm_or_case4token_extraction)
        sf._validate_args4raw_string_LLoo_(case4token_extraction, oresult_with_tag4raw_string, set4sep8open, set4sep8close, set4token6tag)
        args = (case4token_extraction, oresult_with_tag4raw_string, set4sep8open, set4sep8close, set4token6tag)
        args__nm = (case4token_extraction.name, oresult_with_tag4raw_string, set4sep8open, set4sep8close, set4token6tag)

        sf._args4raw_string = args
        sf._args4repr = args__nm

    #@override
    _validated_args4raw_string_LLoo_ = True
    ##@property
    ##@override
    ##def _tkeys_vs_tokens_(sf, /):
    ##    '-> bool'
    ##    return sf._args4raw_string[0]
    @property
    @override
    def _case4token_extraction_(sf, /):
        '-> Case4TokenExtraction'
        return sf._args4raw_string[0]
    @property
    @override
    def _oresult_with_tag4raw_string_(sf, /):
        '-> bool'
        return sf._args4raw_string[1]
    @property
    @override
    def _set4sep8open4tag4raw_string_(sf, /):
        '-> set4sep8open/ITokenKeySetQuery'
        return sf._args4raw_string[2]
    @property
    @override
    def _set4sep8close4tag4raw_string_(sf, /):
        '-> set4sep8close/ITokenKeySetQuery'
        return sf._args4raw_string[3]
    @property
    @override
    def _set4token6tag4raw_string_(sf, /):
        '-> set4token6tag/ITokenKeySetQuery'
        return sf._args4raw_string[4]
check_non_ABC(RecognizerLLoo__raw_string)





class IRecognizerLLoo__traced(IRecognizerLLoo__wrapper):
    r'''[[[
    trace/traced:print_err
    parserTrace:print_err(pos)@beginning
    parserTraced:print_err(pos)@beginning +@err
    #]]]'''#'''
    __slots__ = ()
    @property
    @abstractmethod
    def _may_label6enter4trace4LLoo_(sf, /):
        '-> may label6enter/str'
    @property
    @abstractmethod
    def _may_label6hdr_sgnl4trace4LLoo_(sf, /):
        '-> may label6hdr_sgnl/str'
    @property
    @abstractmethod
    def _may_label6err4trace4LLoo_(sf, /):
        '-> may label6err/str'
    @property
    @abstractmethod
    def _may_label6ok4trace4LLoo_(sf, /):
        '-> may label6ok/str'
    @property
    @abstractmethod
    def _may_label6exit4trace4LLoo_(sf, /):
        '-> may label6exit/str'





    def _6enter4trace4LLoo_(sf, inputter4whole, /):
        'inputter4whole -> (state, inputter4whole)'
        label6enter = sf._may_label6enter4trace4LLoo_
        prev_token_end_gap_position_info = inputter4whole.tell_gap_position_info()
        print_err(f'{label6enter}:{prev_token_end_gap_position_info}')
        return BoxedFinalResult((None, inputter4whole))
        777;    yield
    def _6hdr_sgnl4trace4LLoo_(sf, state, hdr_sgnl, tail_gi_after_hdr_sgnl, /):
        'state -> hdr_sgnl/Signal__HeaderCompleted -> tail_gi_after_hdr_sgnl -> (state, may hdr_sgnl, tail_gi_after_hdr_sgnl)'
        label6hdr_sgnl = sf._may_label6hdr_sgnl4trace4LLoo_
        prev_token_end_gap_position_info = hdr_sgnl.the_inputter4body.tell_gap_position_info()
        print_err(f'{label6hdr_sgnl}:{prev_token_end_gap_position_info}')
        return BoxedFinalResult((state, hdr_sgnl, tail_gi_after_hdr_sgnl))
        777;    yield
    def _6exit4trace4LLoo_(sf, state, reply4LLoo, /):
        'state -> Reply4IRecognizerLLoo -> Reply4IRecognizerLLoo'
        prev_token_end_gap_position_info = reply4LLoo.the_inputter4end.tell_gap_position_info()
        if not reply4LLoo.ok:
            if not None is (label6err := sf._may_label6err4trace4LLoo_):
                print_err(f'{label6err}:{prev_token_end_gap_position_info}')
        else:
            if not None is (label6ok := sf._may_label6ok4trace4LLoo_):
                print_err(f'{label6ok}:{prev_token_end_gap_position_info}')
        if not None is (label6exit := sf._may_label6exit4trace4LLoo_):
            print_err(f'{label6exit}:{prev_token_end_gap_position_info}')
        return BoxedFinalResult(reply4LLoo)
        777;    yield


    @property
    @override
    def may_preprocess(sf, /):
        '-> may preprocess/YS_GI(inputter4whole -> (state, inputter4whole))'
        return None if None is (label6enter := sf._may_label6enter4trace4LLoo_) else sf._6enter4trace4LLoo_
    @property
    @override
    def may_header_signal_process(sf, /):
        '-> may header_signal_process/YS_GI(state -> hdr_sgnl/Signal__HeaderCompleted -> tail_gi_after_hdr_sgnl -> (state, may hdr_sgnl, tail_gi_after_hdr_sgnl))'
        return None if None is (label6hdr_sgnl := sf._may_label6hdr_sgnl4trace4LLoo_) else sf._6hdr_sgnl4trace4LLoo_
    @property
    @override
    def may_postprocess(sf, /):
        '-> may postprocess/YS_GI(state -> Reply4IRecognizerLLoo -> Reply4IRecognizerLLoo)'
        return (None
        if (None is sf._may_label6err4trace4LLoo_)
        and (None is sf._may_label6ok4trace4LLoo_)
        and (None is sf._may_label6exit4trace4LLoo_)
        else sf._6exit4trace4LLoo_
        )


class IRecognizerLLoo__trace(IRecognizerLLoo__traced, IDependentTreeNode__no_ref):
    __slots__ = ()
    @property
    @abstractmethod
    def _label4trace4LLoo_(sf, /):
        '-> label/str'
    @property
    @override
    def _may_label6enter4trace4LLoo_(sf, /):
        '-> may label6enter/str'
        return sf._label4trace4LLoo_
    #@override
    _may_label6hdr_sgnl4trace4LLoo_ = None
    #@override
    _may_label6err4trace4LLoo_ = None
    #@override
    _may_label6ok4trace4LLoo_ = None
    #@override
    _may_label6exit4trace4LLoo_ = None
    #@override
    the_wrapped_obj = recognizer_LLoo__ignore
    @override
    def _iter_direct_child_dependent_tree_nodes_(sf, /):
        '-> Iter IDependentTreeNode'
        yield sf.the_wrapped_obj
        return


class RecognizerLLoo__trace(IRecognizerLLoo__trace, _Base4repr):
    'trace:print_err:debug'
    ___no_slots_ok___ = True
    def __init__(sf, label, /):
        check_type_is(str, label)
        sf._s = label
        sf._args4repr = (label,)
    @property
    @override
    def _label4trace4LLoo_(sf, /):
        '-> label/str'
        return sf._s
check_non_ABC(RecognizerLLoo__trace)




class RecognizerLLoo__traced(_IRecognizerLLoo__wrapper_base__single_ref, IRecognizerLLoo__traced):
    'traced:print_err:debug'
    ___no_slots_ok___ = True
    def __init__(sf, _may_label6enter4trace4LLoo_, _may_label6hdr_sgnl4trace4LLoo_, _may_label6err4trace4LLoo_, _may_label6ok4trace4LLoo_, _may_label6exit4trace4LLoo_, rgnr, /):
        args = (_may_label6enter4trace4LLoo_, _may_label6hdr_sgnl4trace4LLoo_, _may_label6err4trace4LLoo_, _may_label6ok4trace4LLoo_, _may_label6exit4trace4LLoo_, rgnr)
        for may_label in args[:-1]:
            if not None is (label := may_label):
                check_type_is(str, label)
        check_type_le(IRecognizerLLoo, rgnr)

        super().__init__(*args)
        sf._args4trace = args
        sf._args4repr = args


    @property
    @override
    def _may_label6enter4trace4LLoo_(sf, /):
        '-> may label6enter/str'
        return sf._args4trace[0]
    @property
    @override
    def _may_label6hdr_sgnl4trace4LLoo_(sf, /):
        '-> may label6hdr_sgnl/str'
        return sf._args4trace[1]
    @property
    @override
    def _may_label6err4trace4LLoo_(sf, /):
        '-> may label6err/str'
        return sf._args4trace[2]
    @property
    @override
    def _may_label6ok4trace4LLoo_(sf, /):
        '-> may label6ok/str'
        return sf._args4trace[3]
    @property
    @override
    def _may_label6exit4trace4LLoo_(sf, /):
        '-> may label6exit/str'
        return sf._args4trace[4]
check_non_ABC(RecognizerLLoo__traced)













#.+1,$s/^RecognizerLLoo__\(\w*\)\n    def __init__(sf, \(.*\), \/):$/def mk_LLoo__\1(\2, \/):\r    return RecognizerLLoo__\1(\2)

#.,.+22s/\<_\(\w*\)_\>/\1/g
recognizer_LLoo__any_tkey
recognizer_LLoo__any_tdat
recognizer_LLoo__any_tkd
def mk_LLoo__any_tkey(nm_or_case4token_extraction='tkey', /):
    '(nm/str|Case4TokenExtraction) -> IRecognizerLLoo'
    case4token_extraction = nm_or2case4token_extraction(nm_or_case4token_extraction)
    #check_type_is(Case4TokenExtraction, case4token_extraction)
    rgnr = _4any_tkey[case4token_extraction]
    return rgnr
def mk_LLoo__tkey_set(token_set_query, /, *, to_invert=False, nm_or_case4token_extraction='tkey'):
    'ITokenSetQuery -> IRecognizerLLoo'
    check_type_is(bool, to_invert)
    case4token_extraction = nm_or2case4token_extraction(nm_or_case4token_extraction)
    #check_type_is(Case4TokenExtraction, case4token_extraction)
    T = _4tkey_set[case4token_extraction]
    return _mk_LLoo__token_set(T, token_set_query, to_invert=to_invert)
    #return _mk_LLoo__token_set(RecognizerLLoo__tkey_set, token_set_query, to_invert=to_invert)

_4any_tkey = (
{Case4TokenExtraction.token
:recognizer_LLoo__any_token
,Case4TokenExtraction.tkey
:recognizer_LLoo__any_tkey
,Case4TokenExtraction.tdat
:recognizer_LLoo__any_tdat
,Case4TokenExtraction.tkd
:recognizer_LLoo__any_tkd
})
_4tkey_set = (
{Case4TokenExtraction.token
:RecognizerLLoo__token_set
,Case4TokenExtraction.tkey
:RecognizerLLoo__tkey_set
,Case4TokenExtraction.tdat
:RecognizerLLoo__tdat_set
,Case4TokenExtraction.tkd
:RecognizerLLoo__tkd_set
})
_4match_constant_tkey = (
{Case4TokenExtraction.token
:RecognizerLLoo__match_constant_token
,Case4TokenExtraction.tkey
:RecognizerLLoo__match_constant_tkey
,Case4TokenExtraction.tdat
:RecognizerLLoo__match_constant_tdat
,Case4TokenExtraction.tkd
:RecognizerLLoo__match_constant_tkd
})
_4match_constant_tkeys = (
{Case4TokenExtraction.token
:RecognizerLLoo__match_constant_tokens
,Case4TokenExtraction.tkey
:RecognizerLLoo__match_constant_tkeys
,Case4TokenExtraction.tdat
:RecognizerLLoo__match_constant_tdats
,Case4TokenExtraction.tkd
:RecognizerLLoo__match_constant_tkds
})

_4match_one_of_tkeys = (
{Case4TokenExtraction.token
:RecognizerLLoo__match_one_of_tokens
,Case4TokenExtraction.tkey
:RecognizerLLoo__match_one_of_tkeys
,Case4TokenExtraction.tdat
:RecognizerLLoo__match_one_of_tdats
,Case4TokenExtraction.tkd
:RecognizerLLoo__match_one_of_tkds
})
def mk_LLoo__match_constant_tkeys(tkeys, /, *, nm_or_case4token_extraction='tkey'):
    #def mk_LLoo__match_constant_tkeys(tkeys, /, *, tkeys_vs_tokens=False):
    '[tkey] -> IRecognizerLLoo'
    #T = RecognizerLLoo__match_constant_tkeys if not tkeys_vs_tokens else RecognizerLLoo__match_constant_tokens
    case4token_extraction = nm_or2case4token_extraction(nm_or_case4token_extraction)
    #check_type_is(Case4TokenExtraction, case4token_extraction)
    T = _4match_constant_tkeys[case4token_extraction]
    return T(tkeys)
def mk_LLoo__match_constant_tkey(tkey, /, *, nm_or_case4token_extraction='tkey'):
    #def mk_LLoo__match_constant_tkey(tkey, /, *, tkey_vs_token=False):
    'tkey -> IRecognizerLLoo'
    #T = RecognizerLLoo__match_constant_tkey if not tkey_vs_token else RecognizerLLoo__match_constant_token
    case4token_extraction = nm_or2case4token_extraction(nm_or_case4token_extraction)
    #check_type_is(Case4TokenExtraction, case4token_extraction)
    T = _4match_constant_tkey[case4token_extraction]
    return T(tkey)

def mk_LLoo__match_one_of_tkeys(tkeys, /, *, nm_or_case4token_extraction='tkey'):
    #def mk_LLoo__match_one_of_tkeys(tkeys, /, *, tkey_vs_token=False):
    '[tkey] -> IRecognizerLLoo'
    #T = RecognizerLLoo__match_one_of_tkeys if not tkey_vs_token else RecognizerLLoo__match_one_of_tokens
    case4token_extraction = nm_or2case4token_extraction(nm_or_case4token_extraction)
    #check_type_is(Case4TokenExtraction, case4token_extraction)
    T = _4match_one_of_tkeys[case4token_extraction]
    return T(tkeys)

def mk_LLoo__raw_string(set4sep8open, set4sep8close, set4token6tag, /, *, nm_or_case4token_extraction='tkey', oresult_with_tag4raw_string=False):
    #def mk_LLoo__raw_string(set4sep8open, set4sep8close, set4token6tag, /, *, tkeys_vs_tokens=False, oresult_with_tag4raw_string=False):
    'ITokenKeySetQuery -> ITokenKeySetQuery -> ITokenKeySetQuery -> IRecognizerLLoo'
    return RecognizerLLoo__raw_string(nm_or_case4token_extraction, oresult_with_tag4raw_string, set4sep8open, set4sep8close, set4token6tag)


def mk_LLoo__trace(label, /):
    'str -> IRecognizerLLoo'
    return RecognizerLLoo__trace(label)
def mk_LLoo__traced(rgnr, /, *, may_label6enter=None, may_label6hdr_sgnl=None, may_label6err=None, may_label6ok=None, may_label6exit=None):
    'IRecognizerLLoo -> IRecognizerLLoo'
    d = dict(locals())
    del d['rgnr']
    if all(None is m for m in d.values()):
        return rgnr
    return RecognizerLLoo__traced(may_label6enter, may_label6hdr_sgnl, may_label6err, may_label6ok, may_label6exit, rgnr)

#.,.+9s/\<_may_label6\(\w*\)4trace4LLoo_\>/may_label6\1/g
#def mk_LLoo__traced(rgnr, /, *, _may_label6enter4trace4LLoo_=None, _may_label6hdr_sgnl4trace4LLoo_=None, _may_label6err4trace4LLoo_=None, _may_label6ok4trace4LLoo_=None, _may_label6exit4trace4LLoo_=None):
#    return RecognizerLLoo__traced(_may_label6enter4trace4LLoo_, _may_label6hdr_sgnl4trace4LLoo_, _may_label6err4trace4LLoo_, _may_label6ok4trace4LLoo_, _may_label6exit4trace4LLoo_, rgnr)

def mk_LLoo__traced__simple(label, rgnr, /):
    'str -> IRecognizerLLoo -> IRecognizerLLoo'
    check_type_is(str, label)
    return mk_LLoo__traced(rgnr
    ,may_label6enter=f'6enter:{label}'
    ,may_label6hdr_sgnl=f'6hdr_sgnl:{label}'
    ,may_label6err=f'6err:{label}'
    ,may_label6ok=f'6ok:{label}'
    ,may_label6exit=f'6exit:{label}'
    )















__all__
from seed.recognize.recognizer_LLoo_.stream.token_stream import \
(ITokenKeySetQuery
    ,ITokenKeySetQuery__wrapper
        ,TokenKeySetQuery__not

,IRecognizerLLoo__token_set__oresult_is_tkey
    ,RecognizerLLoo__any_tkey
        ,recognizer_LLoo__any_tkey


,IRecognizerLLoo__tkey_set
    ,IRecognizerLLoo__tkey_set__oresult_is_token
    ,IRecognizerLLoo__tkey_set__oresult_is_tkey


,RecognizerLLoo__match_constant_tkeys
,RecognizerLLoo__match_constant_tokens
,RecognizerLLoo__match_constant_tkey
,RecognizerLLoo__match_constant_token


,RecognizerLLoo__match_one_of_tkeys
,RecognizerLLoo__match_one_of_tokens


,IRecognizerLLoo__raw_string
    ,RecognizerLLoo__raw_string

,IRecognizerLLoo__traced
    ,RecognizerLLoo__traced
    ,IRecognizerLLoo__trace
        ,RecognizerLLoo__trace
)

from seed.recognize.recognizer_LLoo_.stream.token_stream import \
(recognizer_LLoo__any_tkey
,mk_LLoo__tkey_set
,mk_LLoo__match_constant_tkeys
,mk_LLoo__match_constant_tkey
,mk_LLoo__match_one_of_tkeys
,mk_LLoo__raw_string
,mk_LLoo__trace
,mk_LLoo__traced
,mk_LLoo__traced__simple
)
from seed.recognize.recognizer_LLoo_.stream.token_stream import *
