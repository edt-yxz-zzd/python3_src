#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo_/stream/char_stream.py

seed.recognize.recognizer_LLoo_.stream.char_stream
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo_.stream.char_stream -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo_.stream.char_stream:__doc__ -ht
py_adhoc_call   seed.recognize.recognizer_LLoo_.stream.char_stream   @f
from seed.recognize.recognizer_LLoo_.stream.char_stream import *
#]]]'''
__all__ = r'''
ICharTokenKeySetQuery
    ICharTokenKeySetQuery__wrapper
        CharTokenKeySetQuery__not
        CharTokenKeySetQuery__and
        CharTokenKeySetQuery__or
    ICharTokenKeySetQuery__using_regex
        CharTokenKeySetQuery__using_regex
    ICharTokenKeySetQuery__using_py_str_method
        CharTokenKeySetQuery__using_py_str_method




regex5or_pattern
CharTokenKeySetQuery__using_regex
    char_set_query__regex__w
    char_set_query__regex__W
    char_set_query__regex__s
    char_set_query__regex__S
    char_set_query__regex__d
    char_set_query__regex__D



CharTokenKeySetQuery__using_py_str_method
    char_set_query__isalnum
    char_set_query__not_isalnum
    char_set_query__isalpha
    char_set_query__not_isalpha
    char_set_query__isascii
    char_set_query__not_isascii
    char_set_query__isdecimal
    char_set_query__not_isdecimal
    char_set_query__isdigit
    char_set_query__not_isdigit
    char_set_query__isidentifier
    char_set_query__not_isidentifier
    char_set_query__islower
    char_set_query__not_islower
    char_set_query__isnumeric
    char_set_query__not_isnumeric
    char_set_query__isprintable
    char_set_query__not_isprintable
    char_set_query__isspace
    char_set_query__not_isspace
    char_set_query__istitle
    char_set_query__not_istitle
    char_set_query__isupper
    char_set_query__not_isupper






recognizer_LLoo__regex__w
recognizer_LLoo__regex__W
recognizer_LLoo__regex__s
recognizer_LLoo__regex__S
recognizer_LLoo__regex__d
recognizer_LLoo__regex__D


recognizer_LLoo__isalnum
recognizer_LLoo__not_isalnum
recognizer_LLoo__isalpha
recognizer_LLoo__not_isalpha
recognizer_LLoo__isascii
recognizer_LLoo__not_isascii
recognizer_LLoo__isdecimal
recognizer_LLoo__not_isdecimal
recognizer_LLoo__isdigit
recognizer_LLoo__not_isdigit
recognizer_LLoo__isidentifier
recognizer_LLoo__not_isidentifier
recognizer_LLoo__islower
recognizer_LLoo__not_islower
recognizer_LLoo__isnumeric
recognizer_LLoo__not_isnumeric
recognizer_LLoo__isprintable
recognizer_LLoo__not_isprintable
recognizer_LLoo__isspace
recognizer_LLoo__not_isspace
recognizer_LLoo__istitle
recognizer_LLoo__not_istitle
recognizer_LLoo__isupper
recognizer_LLoo__not_isupper


'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
import re
from seed.abc.IChar import IChar
from seed.recognize.recognizer_LLoo_.stream.token_stream import ITokenKeySetQuery, ITokenKeySetQuery__wrapper, TokenKeySetQuery__not
from seed.recognize.recognizer_LLoo_.stream.token_stream import RecognizerLLoo__tkey_set# _mk_LLoo__token_set

from seed.recognize.recognizer_LLoo_.stream.token_stream import _ITokenKeySetQuery__op__init, TokenKeySetQuery__and, TokenKeySetQuery__or

from seed.recognize.recognizer_LLoo_._common import (check_non_ABC
,check_non_ABC
,check_type_is, check_type_le, check_int_ge
,mk_tuple, mk_immutable_seq

,abstractmethod, override, ABC, ABC__no_slots
,repr_helper, _Base4repr #sf._args4repr = (...)
)

from seed.recognize.recognizer_LLoo_.stream._common import (IToken
,IForkableForwardInputStream
)

from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import IRecognizerLLoo, Signal__HeaderCompleted, Reply4IRecognizerLLoo
from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import IRecognizerLLoo__leaf, IRecognizerLLoo__no_ref
from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import IDependentTreeNode, IDependentTreeNode__no_ref, IDependentTreeNode__no_children, IDependentTreeNode__leaf, IDependentTreeNode__ref
___end_mark_of_excluded_global_names__0___ = ...

class ICharTokenKeySetQuery(ITokenKeySetQuery):
    #class ITokenKeySetQuery__tkey_is_char(ITokenKeySetQuery):
    'char_set@char_stream'
    __slots__ = ()
    #@override
    _base_type4tkey_ = IChar
    @override
    def __invert__(sf, /):
        '-> ICharTokenKeySetQuery'
        return CharTokenKeySetQuery__not(sf)
    def __and__(sf, ot, /):
        '-> ITokenSetQuery'
        if isinstance(ot, ICharTokenKeySetQuery):
            return CharTokenKeySetQuery__and([sf, ot])
        return super().__and__(ot)
    def __or__(sf, ot, /):
        '-> ITokenSetQuery'
        if isinstance(ot, ICharTokenKeySetQuery):
            return CharTokenKeySetQuery__or([sf, ot])
        return super().__or__(ot)

class _ICharTokenKeySetQuery__op__init(_ITokenKeySetQuery__op__init, ICharTokenKeySetQuery):
    #@override
    _base_type4arg4op_ = ICharTokenKeySetQuery
    #@override
    _is_good_token_ = ICharTokenKeySetQuery._is_good_token_
    #@override
    __invert__ = ICharTokenKeySetQuery.__invert__
    #@override
    __and__ = ICharTokenKeySetQuery.__and__
    #@override
    __or__ = ICharTokenKeySetQuery.__or__

class CharTokenKeySetQuery__and(TokenKeySetQuery__and, _ICharTokenKeySetQuery__op__init):
    #@override
    _base_type4tkey_ = ICharTokenKeySetQuery._base_type4tkey_
    #@override
    __invert__ = ICharTokenKeySetQuery.__invert__
    #@override
    __and__ = ICharTokenKeySetQuery.__and__
    #@override
    __or__ = ICharTokenKeySetQuery.__or__

class CharTokenKeySetQuery__or(TokenKeySetQuery__or, _ICharTokenKeySetQuery__op__init):
    #@override
    _base_type4tkey_ = ICharTokenKeySetQuery._base_type4tkey_
    #@override
    __invert__ = ICharTokenKeySetQuery.__invert__
    #@override
    __and__ = ICharTokenKeySetQuery.__and__
    #@override
    __or__ = ICharTokenKeySetQuery.__or__


class ICharTokenKeySetQuery__wrapper(ITokenKeySetQuery__wrapper, ICharTokenKeySetQuery):
    __slots__ = ()
    #@override
    _base_type4tkey_ = ICharTokenKeySetQuery._base_type4tkey_
    #@override
    _base_type4wrapped_obj_ = ICharTokenKeySetQuery

class CharTokenKeySetQuery__not(TokenKeySetQuery__not, ICharTokenKeySetQuery__wrapper):
    #@override
    _base_type4tkey_ = ICharTokenKeySetQuery._base_type4tkey_
    #@override
    _base_type4wrapped_obj_ = ICharTokenKeySetQuery
    @override
    def __invert__(sf, /):
        '-> ICharTokenKeySetQuery'
        return sf.the_wrapped_obj
    #@override
    __and__ = ICharTokenKeySetQuery.__and__
    #@override
    __or__ = ICharTokenKeySetQuery.__or__
check_non_ABC(CharTokenKeySetQuery__not)




##def mk_LLoo__char_set(char_set_query, /, *, to_invert=False):
##    'ICharTokenKeySetQuery -> IRecognizerLLoo'
##    return _mk_LLoo__token_set(RecognizerLLoo__char_set, char_set_query, to_invert=to_invert)
##


class ICharTokenKeySetQuery__using_regex(ICharTokenKeySetQuery):
    'char_set{using_regex}@char_stream'
    __slots__ = ()
    @property
    @abstractmethod
    def _invert_bad_good_(sf, /):
        '-> bool'
    @property
    @abstractmethod
    def _regex_(sf, /):
        '-> py.regex'
    @override
    def _is_good_tkey_(sf, tkey, /):
        '-> bool'
        return (not None is sf._regex_.fullmatch(tkey)) ^ sf._invert_bad_good_

_type4regex = type(re.compile(''))
def regex5or_pattern(regex_or_pattern, /):
    cls = type(regex_or_pattern)
    if cls is str:
        pattern = regex_or_pattern
        regex = re.compile(pattern)
    elif cls is _type4regex:
        regex = regex_or_pattern
    else:
        raise TypeError(cls)
    regex
    check_type_is(_type4regex, regex)
    return regex
class CharTokenKeySetQuery__using_regex(ICharTokenKeySetQuery__using_regex, IDependentTreeNode__leaf, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, _invert_bad_good_, regex_or_pattern, /):
        check_type_is(bool, _invert_bad_good_)
        regex = regex5or_pattern(regex_or_pattern)
        sf._inv = _invert_bad_good_
        sf._rex = regex
        sf._args4repr = (_invert_bad_good_, regex_or_pattern)
            #_Base4repr
    @property
    @override
    def _invert_bad_good_(sf, /):
        '-> bool'
        return sf._inv
    @property
    @override
    def _regex_(sf, /):
        '-> py.regex'
        return sf._rex
check_non_ABC(CharTokenKeySetQuery__using_regex)


r'\w'
char_set_query__regex__w = CharTokenKeySetQuery__using_regex(False, r'\w')
char_set_query__regex__W = CharTokenKeySetQuery__using_regex(True, r'\w')

r'\s'
char_set_query__regex__s = CharTokenKeySetQuery__using_regex(False, r'\s')
char_set_query__regex__S = CharTokenKeySetQuery__using_regex(True, r'\s')

r'\d'
char_set_query__regex__d = CharTokenKeySetQuery__using_regex(False, r'\d')
char_set_query__regex__D = CharTokenKeySetQuery__using_regex(True, r'\d')



class ICharTokenKeySetQuery__using_py_str_method(ICharTokenKeySetQuery):
    'char_set{using_py_str_method}@char_stream'
    __slots__ = ()
    @property
    @abstractmethod
    def _invert_bad_good_(sf, /):
        '-> bool'
    @property
    @abstractmethod
    def _name4py_str_method_(sf, /):
        '-> nm/str'
    @override
    def _is_good_tkey_(sf, tkey, /):
        '-> bool'
        return getattr(str, sf._name4py_str_method_)(tkey) ^ sf._invert_bad_good_

class CharTokenKeySetQuery__using_py_str_method(ICharTokenKeySetQuery__using_py_str_method, IDependentTreeNode__leaf, _Base4repr):
    ___no_slots_ok___ = True
    def __init__(sf, _invert_bad_good_, _name4py_str_method_, /):
        check_type_is(bool, _invert_bad_good_)
        check_type_is(str, _name4py_str_method_)
        check_type_is(bool, getattr(str, _name4py_str_method_)('x'))
        if not _name4py_str_method_.startswith('is'):raise ValueError

        sf._inv = _invert_bad_good_
        sf._nm = _name4py_str_method_
        sf._args4repr = (_invert_bad_good_, _name4py_str_method_)
            #_Base4repr
    @property
    @override
    def _invert_bad_good_(sf, /):
        '-> bool'
        return sf._inv
    @property
    @override
    def _name4py_str_method_(sf, /):
        '-> nm/str'
        return sf._nm
check_non_ABC(CharTokenKeySetQuery__using_py_str_method)


r'''[[[

regex__w
regex__W
regex__s
regex__S
regex__d
regex__D



isalnum
not_isalnum
isalpha
not_isalpha
isascii
not_isascii
isdecimal
not_isdecimal
isdigit
not_isdigit
isidentifier
not_isidentifier
islower
not_islower
isnumeric
not_isnumeric
isprintable
not_isprintable
isspace
not_isspace
istitle
not_istitle
isupper
not_isupper
#]]]'''#'''
######################
######################
######################
#%s/^zzz = '\(\w*\)'$/'\1'\rchar_set_query__\1 = CharTokenKeySetQuery__using_py_str_method(False, '\1')\rchar_set_query__not_\1 = CharTokenKeySetQuery__using_py_str_method(True, '\1')\r
'isalnum'
char_set_query__isalnum = CharTokenKeySetQuery__using_py_str_method(False, 'isalnum')
char_set_query__not_isalnum = CharTokenKeySetQuery__using_py_str_method(True, 'isalnum')

'isalpha'
char_set_query__isalpha = CharTokenKeySetQuery__using_py_str_method(False, 'isalpha')
char_set_query__not_isalpha = CharTokenKeySetQuery__using_py_str_method(True, 'isalpha')

'isascii'
char_set_query__isascii = CharTokenKeySetQuery__using_py_str_method(False, 'isascii')
char_set_query__not_isascii = CharTokenKeySetQuery__using_py_str_method(True, 'isascii')

'isdecimal'
char_set_query__isdecimal = CharTokenKeySetQuery__using_py_str_method(False, 'isdecimal')
char_set_query__not_isdecimal = CharTokenKeySetQuery__using_py_str_method(True, 'isdecimal')

'isdigit'
char_set_query__isdigit = CharTokenKeySetQuery__using_py_str_method(False, 'isdigit')
char_set_query__not_isdigit = CharTokenKeySetQuery__using_py_str_method(True, 'isdigit')

'isidentifier'
char_set_query__isidentifier = CharTokenKeySetQuery__using_py_str_method(False, 'isidentifier')
char_set_query__not_isidentifier = CharTokenKeySetQuery__using_py_str_method(True, 'isidentifier')

'islower'
char_set_query__islower = CharTokenKeySetQuery__using_py_str_method(False, 'islower')
char_set_query__not_islower = CharTokenKeySetQuery__using_py_str_method(True, 'islower')

'isnumeric'
char_set_query__isnumeric = CharTokenKeySetQuery__using_py_str_method(False, 'isnumeric')
char_set_query__not_isnumeric = CharTokenKeySetQuery__using_py_str_method(True, 'isnumeric')

'isprintable'
char_set_query__isprintable = CharTokenKeySetQuery__using_py_str_method(False, 'isprintable')
char_set_query__not_isprintable = CharTokenKeySetQuery__using_py_str_method(True, 'isprintable')

'isspace'
char_set_query__isspace = CharTokenKeySetQuery__using_py_str_method(False, 'isspace')
char_set_query__not_isspace = CharTokenKeySetQuery__using_py_str_method(True, 'isspace')

'istitle'
char_set_query__istitle = CharTokenKeySetQuery__using_py_str_method(False, 'istitle')
char_set_query__not_istitle = CharTokenKeySetQuery__using_py_str_method(True, 'istitle')

'isupper'
char_set_query__isupper = CharTokenKeySetQuery__using_py_str_method(False, 'isupper')
char_set_query__not_isupper = CharTokenKeySetQuery__using_py_str_method(True, 'isupper')












######################
######################
######################
RecognizerLLoo__tkey_set

#.+1,.+26s/^\w\+$/recognizer_LLoo__\0 = RecognizerLLoo__tkey_set(char_set_query__\0)
recognizer_LLoo__isalnum = RecognizerLLoo__tkey_set(char_set_query__isalnum)
recognizer_LLoo__not_isalnum = RecognizerLLoo__tkey_set(char_set_query__not_isalnum)
recognizer_LLoo__isalpha = RecognizerLLoo__tkey_set(char_set_query__isalpha)
recognizer_LLoo__not_isalpha = RecognizerLLoo__tkey_set(char_set_query__not_isalpha)
recognizer_LLoo__isascii = RecognizerLLoo__tkey_set(char_set_query__isascii)
recognizer_LLoo__not_isascii = RecognizerLLoo__tkey_set(char_set_query__not_isascii)
recognizer_LLoo__isdecimal = RecognizerLLoo__tkey_set(char_set_query__isdecimal)
recognizer_LLoo__not_isdecimal = RecognizerLLoo__tkey_set(char_set_query__not_isdecimal)
recognizer_LLoo__isdigit = RecognizerLLoo__tkey_set(char_set_query__isdigit)
recognizer_LLoo__not_isdigit = RecognizerLLoo__tkey_set(char_set_query__not_isdigit)
recognizer_LLoo__isidentifier = RecognizerLLoo__tkey_set(char_set_query__isidentifier)
recognizer_LLoo__not_isidentifier = RecognizerLLoo__tkey_set(char_set_query__not_isidentifier)
recognizer_LLoo__islower = RecognizerLLoo__tkey_set(char_set_query__islower)
recognizer_LLoo__not_islower = RecognizerLLoo__tkey_set(char_set_query__not_islower)
recognizer_LLoo__isnumeric = RecognizerLLoo__tkey_set(char_set_query__isnumeric)
recognizer_LLoo__not_isnumeric = RecognizerLLoo__tkey_set(char_set_query__not_isnumeric)
recognizer_LLoo__isprintable = RecognizerLLoo__tkey_set(char_set_query__isprintable)
recognizer_LLoo__not_isprintable = RecognizerLLoo__tkey_set(char_set_query__not_isprintable)
recognizer_LLoo__isspace = RecognizerLLoo__tkey_set(char_set_query__isspace)
recognizer_LLoo__not_isspace = RecognizerLLoo__tkey_set(char_set_query__not_isspace)
recognizer_LLoo__istitle = RecognizerLLoo__tkey_set(char_set_query__istitle)
recognizer_LLoo__not_istitle = RecognizerLLoo__tkey_set(char_set_query__not_istitle)
recognizer_LLoo__isupper = RecognizerLLoo__tkey_set(char_set_query__isupper)
recognizer_LLoo__not_isupper = RecognizerLLoo__tkey_set(char_set_query__not_isupper)




#.+1,.+7s/^\w\+$/recognizer_LLoo__\0 = RecognizerLLoo__tkey_set(char_set_query__\0)
recognizer_LLoo__regex__w = RecognizerLLoo__tkey_set(char_set_query__regex__w)
recognizer_LLoo__regex__W = RecognizerLLoo__tkey_set(char_set_query__regex__W)
recognizer_LLoo__regex__s = RecognizerLLoo__tkey_set(char_set_query__regex__s)
recognizer_LLoo__regex__S = RecognizerLLoo__tkey_set(char_set_query__regex__S)
recognizer_LLoo__regex__d = RecognizerLLoo__tkey_set(char_set_query__regex__d)
recognizer_LLoo__regex__D = RecognizerLLoo__tkey_set(char_set_query__regex__D)













######################
######################
######################
__all__
from seed.recognize.recognizer_LLoo_.stream.char_stream import \
(ICharTokenKeySetQuery
,    ICharTokenKeySetQuery__wrapper
,        CharTokenKeySetQuery__not
,    ICharTokenKeySetQuery__using_regex
,        CharTokenKeySetQuery__using_regex
,    ICharTokenKeySetQuery__using_py_str_method
,        CharTokenKeySetQuery__using_py_str_method
)


from seed.recognize.recognizer_LLoo_.stream.char_stream import \
(char_set_query__regex__w
,char_set_query__regex__W
,char_set_query__regex__s
,char_set_query__regex__S
,char_set_query__regex__d
,char_set_query__regex__D
)

from seed.recognize.recognizer_LLoo_.stream.char_stream import \
(char_set_query__isalnum
,char_set_query__not_isalnum
,char_set_query__isalpha
,char_set_query__not_isalpha
,char_set_query__isascii
,char_set_query__not_isascii
,char_set_query__isdecimal
,char_set_query__not_isdecimal
,char_set_query__isdigit
,char_set_query__not_isdigit
,char_set_query__isidentifier
,char_set_query__not_isidentifier
,char_set_query__islower
,char_set_query__not_islower
,char_set_query__isnumeric
,char_set_query__not_isnumeric
,char_set_query__isprintable
,char_set_query__not_isprintable
,char_set_query__isspace
,char_set_query__not_isspace
,char_set_query__istitle
,char_set_query__not_istitle
,char_set_query__isupper
,char_set_query__not_isupper
)







from seed.recognize.recognizer_LLoo_.stream.char_stream import \
(recognizer_LLoo__regex__w
,recognizer_LLoo__regex__W
,recognizer_LLoo__regex__s
,recognizer_LLoo__regex__S
,recognizer_LLoo__regex__d
,recognizer_LLoo__regex__D
)

from seed.recognize.recognizer_LLoo_.stream.char_stream import \
(recognizer_LLoo__isalnum
,recognizer_LLoo__not_isalnum
,recognizer_LLoo__isalpha
,recognizer_LLoo__not_isalpha
,recognizer_LLoo__isascii
,recognizer_LLoo__not_isascii
,recognizer_LLoo__isdecimal
,recognizer_LLoo__not_isdecimal
,recognizer_LLoo__isdigit
,recognizer_LLoo__not_isdigit
,recognizer_LLoo__isidentifier
,recognizer_LLoo__not_isidentifier
,recognizer_LLoo__islower
,recognizer_LLoo__not_islower
,recognizer_LLoo__isnumeric
,recognizer_LLoo__not_isnumeric
,recognizer_LLoo__isprintable
,recognizer_LLoo__not_isprintable
,recognizer_LLoo__isspace
,recognizer_LLoo__not_isspace
,recognizer_LLoo__istitle
,recognizer_LLoo__not_istitle
,recognizer_LLoo__isupper
,recognizer_LLoo__not_isupper
)


from seed.recognize.recognizer_LLoo_.stream.char_stream import *
