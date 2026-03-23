#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/text_recognizer/TextRecognizer__util.py
view ../../python3_src/seed/recognize/text_recognizer/ITextRecognizer.py
view ../../python3_src/seed/recognize/text_recognizer/ITextRecognizer__doctest.py

py -m seed.recognize.text_recognizer.TextRecognizer__util
py -m nn_ns.app.debug_cmd   seed.recognize.text_recognizer.TextRecognizer__util -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.recognize.text_recognizer.TextRecognizer__util:__doc__ -ht # -ff -df
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.recognize.text_recognizer.TextRecognizer__util:cls@T    =T   +exclude_attrs5listed_in_cls_doc
#######

[[
come_from:
e ../../python3_src/seed/math/power/addition_chain/shortest/may_optimal_addition_chain5target_uint7generally_solved_small_step_cases.py

used in:
e ../../python3_src/seed/math/power/addition_chain/shortest/may_optimal_addition_chain5target_uint7generally_solved_small_step_cases__7data7prepare.py
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.recognize.text_recognizer.TextRecognizer__util   @f
]]]'''#'''
__all__ = r'''
txt_rgnrs
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from operator import call
from functools import cached_property
from seed.for_libs.for_functools.cached_property import cached_property
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.bmk_pairs import bmk_pairs
    from seed.recognize.text_recognizer.ITextRecognizer import parse_text_
        #def parse_text_(txt_rgnr, env, txt, begin, end, /):
        #   'ITextRecognizer -> env -> txt/str -> begin/uint%(1+len(txt)) -> end/uint%(1+len(txt)) -> ParseResult/(OResult|Errmsg)'
        #   Errmsg(errmsg,end,severe){ok:=False}{ko:=True}
        #   OResult(oresult,end){ok:=True}{ko:=False}

with mk_ctx4lazy_import4funcs_(__name__):
    from seed.recognize.text_recognizer.ITextRecognizer import (
#after:_BaseTextRecognizer__ops4mkr
#   other_mkrs:goto
ITextRecognizer
,mk_tagged_txt_rgnr_fallback_
,mk_ignorable_txt_rgnr_serial_
,mk_txt_rgnr__regex_#kw:as_regex
,mk_txt_rgnr__text_#kw:as_regex
,mk_txt_rgnr__oresult_
,mk_txt_rgnr__errmsg_
#_BaseTextRecognizer__ops4mkr::
#   .on_ok_
#   .on_ko_
#   .on_errmsg6ko_
#   .named_#kw:global_vs_local,to_tag
#   .tagnamed_#kw:global_vs_local,to_tag
#
#   .enclosed_by_#kw:as_regex
#   .end_by_#kw:cased
#   .many0_#kw:cased
#   .many1_#kw:cased
#   .many_#kw:cased
#   .optional_#kw:cased
#   .sep_by_#kw:cased
#   .sep_end_by_#kw:cased
#
#   #tag for kw:cased
#   .tag7echo_
#   .tag7ignore_
#   .tag7unpack_
#   .__neg__ = tag7ignore_
#   .__pos__ = tag7echo_
#   .__invert__ = tag7unpack_
#   .__matmul__ = then_tag_
#
#   .then_#kw:cased
#   .then_box_
#   .then_getitem_
#   .then_tag_
#   .then_to_finger_tree_seq_
#   .then_to_tuple_
#   .then_unbox_
#
#   .else_
#   .else_trial_
)

#.#################################
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError(Exception, StopIteration)

__all__



def _int5signed_uint(signed_uint, /):
    (sign, uint) = signed_uint
    return sign * uint
def _int5hex(s, /):
    return int(s, 16)




def __():
    txt_rgnr__spaces1 = mk_txt_rgnr__regex_(r'\s+', 0).named_('spaces1')
    txt_rgnr__digits1 = mk_txt_rgnr__regex_(r'[0-9]+', 0).named_('digits1')
    txt_rgnr__hexdigits1 = mk_txt_rgnr__regex_(r'[0-9A-Fa-f]+', 0).named_('hexdigits1')
    txt_rgnr__signspaces0 = mk_txt_rgnr__regex_(r'[-+ \s]*', 0).named_('signspaces0')


    txt_rgnr__spaces0 = txt_rgnr__spaces1.optional_().named_('spaces0')
    txt_rgnr__sign = txt_rgnr__signspaces0.on_ok_(lambda s:(-1)**s.count('-')).named_('sign')
        #txt_rgnr__sign = txt_rgnr__signspaces0.on_ok_(lambda m:(-1)**m.group(0).count('-')).named_('sign')
    txt_rgnr__decimal_uint = txt_rgnr__digits1.on_ok_(int).named_('decimal_uint')
    txt_rgnr__hexadecimal_uint = txt_rgnr__digits1.on_ok_(_int5hex).named_('hexadecimal_uint')
    txt_rgnr__decimal_int = txt_rgnr__sign.then_(txt_rgnr__decimal_uint, cased=False).on_ok_(_int5signed_uint).named_('decimal_int')
    txt_rgnr__hexadecimal_int = txt_rgnr__sign.then_(txt_rgnr__hexadecimal_uint, cased=False).on_ok_(_int5signed_uint).named_('hexadecimal_int')









#.@call
#.class txt_rgnrs:
#.    # .,.+9s/^    \(\w\+\) = \(.*\)/@cached_property\rdef \1(sf, \/):\r    return \2
#.    @cached_property
#.    def txt_rgnr__spaces1(sf, /):
#.        return mk_txt_rgnr__regex_(r'\s+', 0).named_('spaces1')

@call
class txt_rgnrs:
    # .+1,.+12s/^    \(\w\+\) = \(.*\)/\r    \1 = cached_property(lambda sf, \/: \2)
    #       ...++sf.
    txt_rgnr__spaces1 = cached_property(lambda sf, /: mk_txt_rgnr__regex_(r'\s+', 0).named_('spaces1'))

    txt_rgnr__digits1 = cached_property(lambda sf, /: mk_txt_rgnr__regex_(r'[0-9]+', 0).named_('digits1'))

    txt_rgnr__hexdigits1 = cached_property(lambda sf, /: mk_txt_rgnr__regex_(r'[0-9A-Fa-f]+', 0).named_('hexdigits1'))

    txt_rgnr__signspaces0 = cached_property(lambda sf, /: mk_txt_rgnr__regex_(r'[-+ \s]*', 0).named_('signspaces0'))



    txt_rgnr__spaces0 = cached_property(lambda sf, /: sf.txt_rgnr__spaces1.optional_().named_('spaces0'))

    txt_rgnr__sign = cached_property(lambda sf, /: sf.txt_rgnr__signspaces0.on_ok_(lambda s:(-1)**s.count('-')).named_('sign'))
        #txt_rgnr__sign = cached_property(lambda sf, /: sf.txt_rgnr__signspaces0.on_ok_(lambda m:(-1)**m.group(0).count('-')).named_('sign'))

    txt_rgnr__decimal_uint = cached_property(lambda sf, /: sf.txt_rgnr__digits1.on_ok_(int).named_('decimal_uint'))

    txt_rgnr__hexadecimal_uint = cached_property(lambda sf, /: sf.txt_rgnr__digits1.on_ok_(_int5hex).named_('hexadecimal_uint'))

    txt_rgnr__decimal_int = cached_property(lambda sf, /: sf.txt_rgnr__sign.then_(sf.txt_rgnr__decimal_uint, cased=False).on_ok_(_int5signed_uint).named_('decimal_int'))

    txt_rgnr__hexadecimal_int = cached_property(lambda sf, /: sf.txt_rgnr__sign.then_(sf.txt_rgnr__hexadecimal_uint, cased=False).on_ok_(_int5signed_uint).named_('hexadecimal_int'))




#.txt_rgnrs = txt_rgnrs()
if __name__ == "__main__":
    def __():
        print(__name__, 'txt_rgnrs.*', dir(txt_rgnrs))
        for nm in dir(txt_rgnrs):
            print(nm)
    __()
    #txt_rgnr__decimal_int
    #txt_rgnr__decimal_uint
    #txt_rgnr__digits1
    #txt_rgnr__hexadecimal_int
    #txt_rgnr__hexadecimal_uint
    #txt_rgnr__hexdigits1
    #txt_rgnr__sign
    #txt_rgnr__signspaces0
    #txt_rgnr__spaces0
    #txt_rgnr__spaces1




__all__
from seed.recognize.text_recognizer.TextRecognizer__util import txt_rgnrs
from seed.recognize.text_recognizer.TextRecognizer__util import *
