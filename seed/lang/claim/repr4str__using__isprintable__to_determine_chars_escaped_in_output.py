r'''
e ../../python3_src/seed/lang/claim/repr4str__using__isprintable__to_determine_chars_escaped_in_output.py
from seed.lang.claim.repr4str__using__isprintable__to_determine_chars_escaped_in_output import invariant_char_pt_ranges4py_repr, printable_char_pt_ranges4py
from seed.lang.claim.repr4str__using__isprintable__to_determine_chars_escaped_in_output import is_invariant_char4py_repr, is_printable_char4py

see:
    view ../../python3_src/seed/text/charset_filter.py
    view ../../python3_src/seed/text/mk_char_pt_ranges5predicator.py

#'''

__all__ = '''
    invariant_char_pt_ranges4py_repr
    printable_char_pt_ranges4py

    is_invariant_char4py_repr
    is_printable_char4py
    '''.split()

from seed.text.mk_char_pt_ranges5predicator import mk_char_pt_ranges5predicator

is_invariant_char4py_repr = lambda ch:len(repr(ch)) == 3 or ch == '\\'
def is_invariant_char4py_repr(ch, /):
    return len(repr(ch)) == 3 or ch == '\\'
invariant_char_pt_ranges4py_repr = mk_char_pt_ranges5predicator(is_invariant_char4py_repr)



is_printable_char4py = str.isprintable
def is_printable_char4py(ch, /):
    return len(ch) == 1 and str.isprintable(ch)
printable_char_pt_ranges4py = mk_char_pt_ranges5predicator(is_printable_char4py)



#print(invariant_char_pt_ranges4py_repr)
#print(printable_char_pt_ranges4py)

#print(printable_char_pt_ranges4py - invariant_char_pt_ranges4py_repr)
    #NonTouchRanges(())
#print(invariant_char_pt_ranges4py_repr - printable_char_pt_ranges4py)
    #NonTouchRanges(())

assert invariant_char_pt_ranges4py_repr == printable_char_pt_ranges4py


