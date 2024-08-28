#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo_/_test.py

seed.recognize.recognizer_LLoo_._test
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo_._test -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo_._test:__doc__ -ht
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo_._test:__doc__ -ht 2>&1 | more

def mk_forkable_char_stream5ipath(global_runtime_info, ipath, /, *, encoding):
def mk_forkable_char_stream5txt(global_runtime_info, fname, txt, /):

def parse__via_IRecognizerLLoo(recognizer_LLoo, inputter4whole, /):
    def mk_LLoo__traced(sf, rgnr, /, *, may_label6enter=None, may_label6hdr_sgnl=None, may_label6err=None, may_label6ok=None, may_label6exit=None):

#>>> inputter = mk_forkable_char_stream5ipath(..., __file__, encoding='u8')
>>> inputter = mk_forkable_char_stream5txt(..., __file__, '#__all__:goto\nr')
>>> rgnr4NL = factory4LLoo__char_stream.mk_LLoo__match_constant_tkey('\n')
>>> rgnr4sharp = factory4LLoo__char_stream.mk_LLoo__match_constant_tkey('#')
>>> rgnr4underscore = factory4LLoo__char_stream.mk_LLoo__match_constant_tkey('_')
>>> rgnr4alnum = factory4LLoo__char_stream.recognizer_LLoo__isalnum

>>> _rgnr4NL = factory4LLoo__char_stream.mk_LLoo__traced__simple('NL', rgnr4NL)
>>> _rgnr4sharp = factory4LLoo__char_stream.mk_LLoo__traced__simple('#', rgnr4sharp)
>>> _rgnr4underscore = factory4LLoo__char_stream.mk_LLoo__traced__simple('_', rgnr4underscore)
>>> _rgnr4alnum = factory4LLoo__char_stream.mk_LLoo__traced__simple('alnum', rgnr4alnum)

>>> (_rgnr4NL, _rgnr4sharp, _rgnr4underscore, _rgnr4alnum) = (rgnr4NL, rgnr4sharp, rgnr4underscore, rgnr4alnum)

>>> rgnr4w = factory4LLoo__char_stream.mk_LLoo__the_first_one([_rgnr4alnum, _rgnr4underscore])

>>> _rgnr4w = factory4LLoo__char_stream.mk_LLoo__traced__simple('w', rgnr4w)

>>> (_rgnr4w,) = (rgnr4w,)

>>> rgnr4word = factory4LLoo__char_stream.mk_LLoo__many(_rgnr4w, min_loops=1)
>>> rgnr4suffix = factory4LLoo__char_stream.mk_LLoo__match_constant_tkeys(':goto')


>>> _rgnr4word = factory4LLoo__char_stream.mk_LLoo__traced__simple('w+', rgnr4word)
>>> _rgnr4suffix = factory4LLoo__char_stream.mk_LLoo__traced__simple('suffix', rgnr4suffix)

>>> (_rgnr4word, _rgnr4suffix) = (rgnr4word, rgnr4suffix)

>>> rgnr4fstline = factory4LLoo__char_stream.mk_LLoo__tuple([rgnr4sharp], [_rgnr4word, rgnr4suffix, rgnr4NL])

>>> rgnr4fstline
RecognizerLLoo__tuple(1, (RecognizerLLoo__match_constant_tkey('#'), RecognizerLLoo__many(1, -1, 1, RecognizerLLoo__the_first_one((RecognizerLLoo__tkey_set(CharTokenKeySetQuery__using_py_str_method(False, 'isalnum')), RecognizerLLoo__match_constant_tkey('_')))), RecognizerLLoo__match_constant_tkeys(':goto'), RecognizerLLoo__match_constant_tkey('\n')))


#>>> reply4LLoo = parse__via_IRecognizerLLoo(factory4LLoo__char_stream.recognizer_LLoo__any_tkey, inputter)
#>>> reply4LLoo = parse__via_IRecognizerLLoo(rgnr4sharp, inputter)
#>>> reply4LLoo = parse__via_IRecognizerLLoo(_rgnr4sharp, inputter)
>>> reply4LLoo = parse__via_IRecognizerLLoo(rgnr4fstline, inputter)
>>> reply4LLoo  #doctest: +ELLIPSIS
Reply4IRecognizerLLoo(TmpSnapshot4Inputter(ForkableForwardInputStream__using_LazyListIter(Ellipsis, PositionInfo4Gap__text_file('/sdcard/0my_files/git_repos/python3_src/seed/recognize/recognizer_LLoo_/_test.py', None, 14, LinenoColumn(2, 1), 14), <seed.types.LazyList._LazyListIter object at 0x...>), _may_stamp = <seed.types.LazyList._Stamp object at 0x...>), Either(True, (('#',), (('_',), ('_',), 'a', 'l', 'l', ('_',), ('_',)), (':', 'g', 'o', 't', 'o'), ('\n',))))
>>> 
>>> 

grep -F '' -r ../../python3_src/seed/recognize/recognizer_LLoo_/ -l | grep '[.]py$'
grep -F 'peek' -r ../../python3_src/seed/recognize/recognizer_LLoo_/ -l | grep '[.]py$'

#]]]'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...

from seed.recognize.recognizer_LLoo_._common import (check_non_ABC

,bind_gi_with_the_following_first_value4send, mk_gi4either8xresult, mk_gi4xresult_xexception, detach_asif_new_gi_wrapper
,BoxedHalfwayResult, BoxedException__halfway, BoxedException__final, BoxedException__through, Escaped, BoxedTailRecur, BoxedFinalResult
,EFlowControl, EFinal, EHalfway, mk_boxed_EFinal, mk_boxed_EHalfway
,recur5yield__list__echo__echo
,Cased, Either, mk_Left, mk_Right

,check_may_, check_not_
,check_non_ABC
,check_type_is, check_type_le, check_int_ge
,null_iter, null_tuple, mk_tuple, mk_immutable_seq

,IForkable, IForkable__stamp
,IGeneratorIterator

,abstractmethod, override, ABC, ABC__no_slots
,repr_helper, _Base4repr #sf._args4repr = (...)
)


from seed.recognize.recognizer_LLoo_.stream._common import (IToken
,IForkableForwardInputStream, ForkableForwardInputStream__using_LazyListIter
,mk_forkable_char_stream5txt, mk_forkable_char_stream5ipath, mk_forkable_char_stream5ifile, iter_char_tokens5ifile


,IBaseToken, IToken, BaseToken, Token__char
,IBasePositionInfo, IPositionInfo4Gap, IPositionInfo4Span
,LinenoColumn, PositionInfo4Gap, PositionInfo4Gap__text_file, PositionInfo4Span, PositionInfo4Span__text_file
,Token__char, PositionInfo4Span__text_file, PositionInfo4Gap__text_file, LinenoColumn
)

from seed.recognize.recognizer_LLoo_.IRecognizerLLoo import parse__via_IRecognizerLLoo, mk_gi4skip_header_signal, mk_gi4header_signal_at_beginning, mk_gi4patch_header_signal_if_ok, mk_gi4validate_two_phases

from seed.recognize.recognizer_LLoo_.Factory4RecognizerLLoo import factory4LLoo__basic, factory4LLoo__token_stream, factory4LLoo__char_stream

from io import StringIO

___end_mark_of_excluded_global_names__0___ = ...



__all__
from seed.recognize.recognizer_LLoo_._test import *
