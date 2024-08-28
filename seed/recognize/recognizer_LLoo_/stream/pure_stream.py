#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo_/stream/pure_stream.py
view ../../python3_src/seed/recognize/recognizer_LLoo_/stream/token_stream.py

[inputter :: pure_stream/IForkableForwardInputStream<object>]

seed.recognize.recognizer_LLoo_.stream.pure_stream
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo_.stream.pure_stream -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo_.stream.pure_stream:__doc__ -ht
#]]]'''
__all__ = r'''
recognizer_LLoo__eof
recognizer_LLoo__any_token
mk_LLoo__token_set

Case4TokenExtraction
IRecognizerLLoo__token_related

RecognizerLLoo__eof
    recognizer_LLoo__eof
IRecognizerLLoo__token_set
    IRecognizerLLoo__token_set__oresult_is_token
        RecognizerLLoo__any_token
            recognizer_LLoo__any_token
        RecognizerLLoo__token_set

ITokenSetQuery
    ITokenSetQuery__leaf
        _ITokenSetQuery__op__init
            TokenSetQuery__and
            TokenSetQuery__or
        TokenSetQuery__not
        TokenSetQuery__any_token
            token_set_query__any_token
    ITokenSetQuery__wrapper
        ITokenSetQuery__ref
            TokenSetQuery__ref
'''.split()#'''
    #IRecognizerLLoo__token_set__oresult_is_tkey
    #_IRecognizerLLoo__token_set__init

__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.recognize.recognizer_LLoo_._common import (IGeneratorIterator
,BoxedFinalResult
,Either

,check_non_ABC
,check_type_is, check_type_le
,mk_tuple#,null_iter

,abstractmethod, override, ABC, ABC__no_slots
,repr_helper, _Base4repr # sf._args4repr = (...)
)

from seed.recognize.recognizer_LLoo_.stream._common import IToken, IForkableForwardInputStream


from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import IRecognizerLLoo, Reply4IRecognizerLLoo, IWrapper, IScene

from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import IDependentTreeNode, IDependentTreeNode__leaf, IDependentTreeNode__ref, IDependentTreeNode__no_ref #, IDependentTreeNode__no_children

from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import IRecognizerLLoo__leaf, IRecognizerLLoo__no_ref, IRecognizerLLoo__no_children

from enum import Enum

___end_mark_of_excluded_global_names__0___ = ...

class ITokenSetQuery(IDependentTreeNode):
    __slots__ = ()
    #@property
    _base_type4token_ = object #pure_stream
        #_base_type4token_ = IToken #token_stream
    def _check_token_(sf, token, /):
        '-> None | ^TypeError'
        if not (T := sf._base_type4token_) is object:
            check_type_le(T, token)
    @abstractmethod
    def _is_good_token_(sf, token, /):
        '-> bool'
    def is_good_token(sf, token, /):
        '-> bool'
        #check_type_le(object, token)#pure_stream
        #check_type_le(IToken, token)#token_stream
        sf._check_token_(token)
            # ^TypeError
        r = sf._is_good_token_(token)
        check_type_is(bool, r)
        return r
    def __invert__(sf, /):
        '-> ITokenSetQuery'
        return TokenSetQuery__not(sf)
    def __and__(sf, ot, /):
        '-> ITokenSetQuery'
        return TokenSetQuery__and([sf, ot])
    def __or__(sf, ot, /):
        '-> ITokenSetQuery'
        return TokenSetQuery__or([sf, ot])
    def __sub__(sf, ot, /):
        '-> ITokenSetQuery'
        return sf & ~ot

class _ITokenSetQuery__op__init(ITokenSetQuery, IDependentTreeNode__no_ref, _Base4repr):
    ___no_slots_ok___ = True
    _base_type4arg4op_ = ITokenSetQuery
    def __init__(sf, ls4token_set_query, /):
        ls4token_set_query = mk_tuple(ls4token_set_query)
        for token_set_query in ls4token_set_query:
            check_type_le(sf._base_type4arg4op_, token_set_query)
        sf._tqs = ls4token_set_query
        sf._args4repr = (ls4token_set_query,)
    @property
    def _ls4token_set_query_(sf, /):
        return sf._tqs
    @override
    def _iter_direct_child_dependent_tree_nodes_(sf, /):
        '-> Iter IDependentTreeNode'
        return iter(sf._tqs)
class TokenSetQuery__and(_ITokenSetQuery__op__init):
    @override
    def _is_good_token_(sf, token, /):
        '-> bool'
        return all(tq.is_good_token(token) for tq in sf._ls4token_set_query_)
class TokenSetQuery__or(_ITokenSetQuery__op__init):
    @override
    def _is_good_token_(sf, token, /):
        '-> bool'
        return any(tq.is_good_token(token) for tq in sf._ls4token_set_query_)
check_non_ABC(TokenSetQuery__and)
check_non_ABC(TokenSetQuery__or)

class ITokenSetQuery__leaf(ITokenSetQuery, IDependentTreeNode__leaf):
    #class ITokenSetQuery__no_ref(ITokenSetQuery):
    __slots__ = ()
class TokenSetQuery__any_token(ITokenSetQuery__leaf):
    'any_token ok'
    __slots__ = ()
    def __repr__(sf, /):
        return repr_helper(sf)
    @override
    def _is_good_token_(sf, token, /):
        '-> bool'
        return True
token_set_query__any_token = TokenSetQuery__any_token()

class ITokenSetQuery__wrapper(ITokenSetQuery, IWrapper):
    __slots__ = ()
    @property
    #@override
    def _base_type4token_(sf, /):
        return sf.the_wrapped_obj._base_type4token_
    #@override
    _base_type4wrapped_obj_ = ITokenSetQuery
    @override
    def _is_good_token_(sf, token, /):
        '-> bool'
        return sf.the_wrapped_obj._is_good_token_(token)


class TokenSetQuery__not(ITokenSetQuery__wrapper, IDependentTreeNode__no_ref, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, token_set_query, /):
        check_type_le(sf._base_type4wrapped_obj_, token_set_query)
        sf._tq = token_set_query
        sf._args4repr = (token_set_query,)
    @property
    @override
    def the_wrapped_obj(sf, /):
        return sf._tq

    @override
    def _is_good_token_(sf, token, /):
        '-> bool'
        return not sf.the_wrapped_obj.is_good_token(token)
    @override
    def _iter_direct_child_dependent_tree_nodes_(sf, /):
        '-> Iter IDependentTreeNode'
        check_type_le(ITokenSetQuery, sf.the_wrapped_obj)
        yield sf.the_wrapped_obj
        return
    @override
    def __invert__(sf, /):
        '-> ITokenSetQuery'
        return sf.the_wrapped_obj
check_non_ABC(TokenSetQuery__not)


class ITokenSetQuery__ref(ITokenSetQuery__wrapper, IDependentTreeNode__ref):
    __slots__ = ()
class TokenSetQuery__ref(ITokenSetQuery__ref, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, scene, kinded_name, /):
        check_type_le(IScene, scene)
        sf._sc = scene
        sf._knm = kinded_name
        sf._args4repr = (scene, kinded_name)

    @property
    @override
    def its_kinded_name(sf, /):
        '-> knm/kinded_name/(hashable&&immutable)'
        return sf._knm
    @property
    @override
    def scene(sf, /):
        '-> IScene'
        return sf._sc
check_non_ABC(TokenSetQuery__ref)
















































class RecognizerLLoo__eof(IRecognizerLLoo__leaf):
    'eof@pure_stream'
    __slots__ = ()
    def __repr__(sf, /):
        return repr_helper(sf)
    #@property
    #@override
    ___666_tribool_skip4serial4LLoo_999___ = True # False-append;True-skip;...-extend

    @override
    def _iter4two_phases_recognize_(sf, inputter4whole, /):
        check_type_le(IForkableForwardInputStream, inputter4whole) #pure_stream
        eresult = Either(inputter4whole.eof, None)
        reply4LLoo = Reply4IRecognizerLLoo(inputter4whole, eresult)
        return BoxedFinalResult(reply4LLoo)
        777;    yield
check_non_ABC(RecognizerLLoo__eof)

#\<\(_token_vs_tkey_\|token_vs_tkey\|tkeys_vs_tokens\|_tkeys_vs_tokens_\|_tkey_vs_token_\|tkey_vs_token\)\>
#   replace:bool --> Case4TokenExtraction
Case4TokenExtraction = Enum('Case4TokenExtraction', 'token tkey tdat tkd')
def _token5token_(token, /):
    'token -> token'
    # may not:[token <: IToken]
    #   !! pure
    return token
def _tkey5token_(token, /):
    'token -> tkey'
    check_type_le(IToken, token)
    return token.token_key
def _tdat5token_(token, /):
    'token -> tdat'
    check_type_le(IToken, token)
    return token.token_data
def _tkd5token_(token, /):
    'token -> tkd'
    check_type_le(IToken, token)
    return token.token_keyed_data
Case4TokenExtraction.token._extract_token_ = _token5token_
Case4TokenExtraction.tkey._extract_token_ = _tkey5token_
Case4TokenExtraction.tdat._extract_token_ = _tdat5token_
Case4TokenExtraction.tkd._extract_token_ = _tkd5token_

class IRecognizerLLoo__token_related(IRecognizerLLoo):
    '@(pure_stream if _case4token_extraction_ is Case4TokenExtraction.token else token_stream)'
    __slots__ = ()
    @property
    @abstractmethod
    def _case4token_extraction_(sf, /):
        '-> case4token_extraction/Case4TokenExtraction #howto extract info from token'
class IRecognizerLLoo__token_set(IRecognizerLLoo__token_related, IRecognizerLLoo__no_ref):
    #bug:class IRecognizerLLoo__token_set(IRecognizerLLoo__leaf):
    'token_set@(pure_stream|token_stream)'
    __slots__ = ()
    ##@property
    ##@abstractmethod
    ##def _token_vs_tkey_(sf, /):
    ##    '-> bool'
        #replaced by _case4token_extraction_
    @property
    @abstractmethod
    def _token_set_query_(sf, /):
        '-> ITokenSetQuery'
    #@property
    #@override
    ___666_tribool_skip4serial4LLoo_999___ = False # False-append;True-skip;...-extend
    @override
    def _iter_direct_child_dependent_tree_nodes_(sf, /):
        '-> Iter IDependentTreeNode'
        yield sf._token_set_query_
        return

    @override
    def _iter4two_phases_recognize_(sf, inputter4whole, /):
        check_type_le(IForkableForwardInputStream, inputter4whole) #(pure_stream|token_stream)
        #bug:tmay_token = inputter4whole.peek_le(1)
        tmay_token = inputter4whole.read_le(1)
        eof = not tmay_token
        if eof:
            case = False
            payload = 'eof'
        else:
            [token] = tmay_token
            if not sf._token_set_query_.is_good_token(token):
                # ^TypeError
                case = False
                payload = 'non_good_token'
            else:
                case = True
                payload = sf._case4token_extraction_._extract_token_(token)
            case, payload
        case, payload
        eresult = Either(case, payload)
        reply4LLoo = Reply4IRecognizerLLoo(inputter4whole, eresult)
        return BoxedFinalResult(reply4LLoo)
        777;    yield
class IRecognizerLLoo__token_set__oresult_is_token(IRecognizerLLoo__token_set):
    'token_set{oresult==token}@(pure_stream|token_stream)'
    __slots__ = ()
    #@property
    #@override
    _case4token_extraction_ = Case4TokenExtraction.token
        #_token_vs_tkey_ = False
#IRecognizerLLoo__token_set__oresult_is_tkey
class _IRecognizerLLoo__any_token(IRecognizerLLoo__token_set):
    __slots__ = ()
    def __repr__(sf, /):
        return repr_helper(sf)
    #@override
    _token_set_query_ = token_set_query__any_token

class RecognizerLLoo__any_token(_IRecognizerLLoo__any_token, IRecognizerLLoo__token_set__oresult_is_token):
    'any_token@pure_stream'
    __slots__ = ()
check_non_ABC(RecognizerLLoo__any_token)



recognizer_LLoo__eof = RecognizerLLoo__eof()
recognizer_LLoo__any_token = RecognizerLLoo__any_token()





class _IRecognizerLLoo__token_set__init(IRecognizerLLoo__token_set, _Base4repr):
    'token_set@(pure_stream|token_stream) #see:TokenSetQuery__not'
    __slots__ = ()
    def __init__(sf, token_set_query, /):
        check_type_le(ITokenSetQuery, token_set_query)
        sf._tq = token_set_query
        sf._args4repr = (token_set_query,)
    #@property
    #@override
    #_case4token_extraction_ = ???
        #_token_vs_tkey_ = ???
    @property
    @override
    def _token_set_query_(sf, /):
        '-> ITokenSetQuery'
        return sf._tq
    ######################
class RecognizerLLoo__token_set(_IRecognizerLLoo__token_set__init, IRecognizerLLoo__token_set__oresult_is_token):
    'token_set@(pure_stream|token_stream) #see:TokenSetQuery__not'
check_non_ABC(RecognizerLLoo__token_set)



recognizer_LLoo__eof
recognizer_LLoo__any_token

def mk_LLoo__token_set(token_set_query, /, *, to_invert=False):
    'ITokenSetQuery -> IRecognizerLLoo'
    return _mk_LLoo__token_set(RecognizerLLoo__token_set, token_set_query, to_invert=to_invert)
def _mk_LLoo__token_set(T, token_set_query, /, *, to_invert=False):
    'ITokenSetQuery -> IRecognizerLLoo'
    check_type_le(ITokenSetQuery, token_set_query)
    check_type_is(bool, to_invert)
    if to_invert:
        token_set_query = ~token_set_query
    return T(token_set_query)


__all__
from seed.recognize.recognizer_LLoo_.stream.pure_stream import RecognizerLLoo__eof, RecognizerLLoo__any_token
from seed.recognize.recognizer_LLoo_.stream.pure_stream import recognizer_LLoo__eof, recognizer_LLoo__any_token, mk_LLoo__token_set
from seed.recognize.recognizer_LLoo_.stream.pure_stream import IRecognizerLLoo__token_set, IRecognizerLLoo__token_set__oresult_is_token


from seed.recognize.recognizer_LLoo_.stream.pure_stream import ITokenSetQuery, ITokenSetQuery__leaf, ITokenSetQuery__wrapper, ITokenSetQuery__ref, TokenSetQuery__ref

from seed.recognize.recognizer_LLoo_.stream.pure_stream import token_set_query__any_token

from seed.recognize.recognizer_LLoo_.stream.pure_stream import Case4TokenExtraction, IRecognizerLLoo__token_related
from seed.recognize.recognizer_LLoo_.stream.pure_stream import *
