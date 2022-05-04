r'''[[[
see also:
    py::csv

    seed.io.iter_row_based_Z_delimited_text_file
        view /storage/emulated/0/0my_files/git_repos/python3_src/seed/io/iter_row_based_Z_delimited_text_file.py
    seed.io.iter_line_contents
        view /storage/emulated/0/0my_files/git_repos/python3_src/seed/io/iter_line_contents.py
    seed.io.FieldedLineHandler
        view /storage/emulated/0/0my_files/git_repos/python3_src/seed/io/FieldedLineHandler.py

used with:
    seed.func_tools.fmapT
        view ../../python3_src/seed/func_tools/fmapT/fmapT__tiny.py
        view /sdcard/0my_files/git_repos/python3_src/seed/func_tools/fmapT/filterT__tiny.py
        view /sdcard/0my_files/git_repos/python3_src/seed/func_tools/fmapT/predT__tiny.py
        view ../../python3_src/seed/func_tools/fmapT/_xxxT__tiny.py

used in:
    view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/parse__CJKRadicals_txt.py








seed.io.fielded_line_utils
py -m nn_ns.app.debug_cmd   seed.io.fielded_line_utils
e ../../python3_src/seed/io/fielded_line_utils.py

from seed.io.fielded_line_utils import txt2lines__split, txt2lines__splitlines, txt2iter_lines__regex_search, txt2lines__StringIO

from seed.io.fielded_line_utils import line_remove_EOL, line_remove_comment, line_remove_py_comment, line_strip, line_rstrip, line_split, line_remove_prefix, line_remove_suffix

from seed.io.fielded_line_utils import is_all_spaces, hex2int, hex2char

from seed.io.fielded_line_utils import mk_fT, line_remove_commentT, line_stripT, line_rstripT, line_splitT, line_remove_prefixT, line_remove_suffixT

from seed.io.fielded_line_utils import lines_handler2txt_handler, fielded_lines_parserT__tuple, fielded_lines_preprocesserT, lines_preprocesserT


from seed.io.fielded_line_utils import example4lines_parser4UCD_CJKRadicals_txt, example4txt_parser4UCD_CJKRadicals_txt


======================
view /sdcard/0my_files/unzip/e_book/unicode_13__UCD/CJKRadicals.txt
# There is one line per CJK radical number. Each line contains three
# fields, separated by a semicolon (';'). The first field is the
# CJK radical number. The second field is the CJK radical character.
# The third field is the CJK unified ideograph.
#
# CJK radical numbers match the regular expression [1-9][0-9]{0,2}\'?
# and in particular they can end with a U+0027 ' APOSTROPHE.
#
1; 2F00; 4E00
90; 2F59; 723F
90'; 2EA6; 4E2C
214; 2FD5; 9FA0
======================


#]]]'''

__all__ = '''
    txt2lines__splitlines
        txt2lines__split
        txt2iter_lines__regex_search
        txt2lines__StringIO

    line_remove_EOL
    line_remove_comment
        line_remove_py_comment
    line_strip
    line_rstrip
    line_split
    line_remove_prefix
    line_remove_suffix

    is_all_spaces
    hex2int
    hex2char

    mk_fT
        line_remove_commentT
        line_stripT
        line_rstripT
        line_splitT
        line_remove_prefixT
        line_remove_suffixT

    lines_handler2txt_handler
        fielded_lines_parserT__tuple
        fielded_lines_preprocesserT
        lines_preprocesserT


        example4lines_parser4UCD_CJKRadicals_txt
        example4txt_parser4UCD_CJKRadicals_txt
    '''.split()

___begin_mark_of_excluded_global_names__0___ = ...
from seed.tiny import check_type_is, echo
import re
from io import StringIO
from seed.func_tools.fmapT.fmapT__tiny import dot, fmapT__tuple, fmapT__list
from seed.func_tools.fmapT.filterT__tiny import filterT__list
from seed.func_tools.fmapT.predT__tiny import predT__NOT
___end_mark_of_excluded_global_names__0___ = ...



_regex4decimal_digit1s = re.compile(r'(?:[0-9]+)')
_chars4EOL = '\r\n'
_regex4EOL = re.compile(r'(?:\n\r?|\r\n?)')
_regex4EOLs = re.compile(r'(?:[\n\r]+)')
def txt2lines__split(txt, /):
    return txt.split('\n')
def txt2lines__splitlines(txt, /, keepends=False):
    r'''

 str.splitlines([keepends])

    Return a list of the lines in the string, breaking at line boundaries. Line breaks are not included in the resulting list unless keepends is given and true.

    This method splits on the following line boundaries. In particular, the boundaries are a superset of universal newlines.

Changed in version 3.2: \v and \f added to list of line boundaries.

Representation:Description

\n:Line Feed

\r:Carriage Return

\r\n:Carriage Return + Line Feed

\v or \x0b:Line Tabulation

\f or \x0c:Form Feed

\x1c:File Separator

\x1d:Group Separator

\x1e:Record Separator

\x85:Next Line (C1 Control Code)

\u2028:Line Separator

\u2029:Paragraph Separator

    #'''
    return txt.splitlines(keepends)
def txt2iter_lines__regex_search(txt, /, *, begin=None, end=None, exclude_empty_tail_line=False, regex4EOL=None):
    if begin is None:
        begin = 0
    if end is None:
        end = len(txt)
    if regex4EOL is None:
        regex4EOL = _regex4EOL

    for m in regex4EOL.finditer(txt, begin, end):
        _end = m.start()
        _begin = m.end()
        yield txt[begin:_end]
        begin = _begin
    tail_line = txt[begin:end]
    if tail_line or not exclude_empty_tail_line:

        yield tail_line
    return

def txt2lines__StringIO(txt, /, newline=None):
    '[newline=None]<==>[universal newline@read]'
    ls = StringIO(txt).readlines()
    check_type_is(list, ls)
    return ls


def line_remove_EOL(line, /):
    return line.rstrip(_chars4EOL)
    ######################
    if not line[-1:] in _chars4EOL:
        return line
    for i in reversed(range(len(line))):
        if not line[i] in _chars4EOL:
            break
    else:
        i = -1
    end = i+1
    return line[:-1]


def line_remove_comment(line, line_tail_comment_prefix, /):
    (line, _, _) = line.partition(line_tail_comment_prefix)
    return line
def line_remove_py_comment(line, /):
    return line_remove_comment(line, '#')

def line_strip(line, chars=None, /):
    return line.strip(chars)
def line_rstrip(line, chars=None, /):
    return line.rstrip(chars)

def line_split(line, sep, /, *, maxsplit=-1):
    return line.split(sep, maxsplit=maxsplit)



def line_remove_prefix(line, prefix, /):
    if not line.startswith(prefix): raise ValueError(f'not startswith: {line!r} :  {prefix!r}')
    return line[len(prefix):]
def line_remove_suffix(line, suffix, /):
    if not line.endswith(suffix): raise ValueError(f'not endswith: {line!r} :  {suffix!r}')
    return line[:len(line)-len(suffix)]


def is_all_spaces(txt, /):
    return (not txt) or txt.isspace()
def hex2int(s, /):
    return int(s, 16)
hex2char = dot[chr, hex2int]
def decimal_nondecimal_str2int_tail_pair(decimal_nondecimal_str, /):
    m = _regex4decimal_digit1s.match(decimal_nondecimal_str)
    if not m: raise ValueError(f'not startswith decimal_digit1s: {decimal_nondecimal_str!r}')
    assert m.start() == 0
    L = m.end()
    decimal_digit1s = decimal_nondecimal_str[:L]
    tail = decimal_nondecimal_str[L:]
    u = int(decimal_digit1s)
    return (u, tail)

def mk_fT(f, /):
    def fT(*args, **kwargs):
        def _f(x, /):
            return f(x, *args, **kwargs)
        return _f
    return fT



line_remove_EOL
line_remove_py_comment
line_remove_commentT = mk_fT(line_remove_comment)
line_stripT = mk_fT(line_strip)
line_rstripT = mk_fT(line_rstrip)
line_splitT = mk_fT(line_split)

line_remove_prefixT = mk_fT(line_remove_prefix)
line_remove_suffixT = mk_fT(line_remove_suffix)




def lines_handler2txt_handler(lines_handler, /):
    r'([line]->r) -> (txt->r)'
    txt_handler = dot[lines_handler, txt2lines__splitlines]
    return txt_handler

def fielded_lines_parserT__tuple(field_separator, line_tail_comment_prefix, field_parsers, /, *, keep_space_lines, keep_bifix_spaces4field):
    fielded_lines_preprocesser = fielded_lines_preprocesserT(field_separator, line_tail_comment_prefix, keep_space_lines=keep_space_lines, keep_bifix_spaces4field=keep_bifix_spaces4field)
    fields_parser = fmapT__tuple(*field_parsers)
    #bug:fielded_lines_parser = dot[fields_parser, fielded_lines_preprocesser]
    #   ([field]->r) . ([line]->[[field]])
    fieldss_parser = fmapT__list(fields_parser)
    fielded_lines_parser = dot[fieldss_parser, fielded_lines_preprocesser]
    #   ([[field]]->r) . ([line]->[[field]])
    return fielded_lines_parser

def fielded_lines_preprocesserT(field_separator, line_tail_comment_prefix, /, *, keep_space_lines, keep_bifix_spaces4field):
    fielded_lines_preprocesser = dot[
        fmapT__list(dot[
            echo if keep_bifix_spaces4field
                else fmapT__list(line_strip)
            ,line_splitT(field_separator)
            ])
        ,lines_preprocesserT(line_tail_comment_prefix, keep_space_lines=keep_space_lines)
        ]
    return fielded_lines_preprocesser
def lines_preprocesserT(line_tail_comment_prefix, /, *, keep_space_lines):
    lines_preprocesser = dot[
        echo if keep_space_lines
            else filterT__list(predT__NOT(is_all_spaces))
        ,fmapT__list(dot[
            line_remove_commentT(line_tail_comment_prefix)
            ,line_remove_EOL
            ])
        ]
    return lines_preprocesser

example4lines_parser4UCD_CJKRadicals_txt = fielded_lines_parserT__tuple(';', '#', [decimal_nondecimal_str2int_tail_pair, hex2char, hex2char], keep_space_lines=False, keep_bifix_spaces4field=False)
example4txt_parser4UCD_CJKRadicals_txt = lines_handler2txt_handler(example4lines_parser4UCD_CJKRadicals_txt)

