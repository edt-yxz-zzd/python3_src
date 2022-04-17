r'''
see also:
    py::csv

    view /storage/emulated/0/0my_files/git_repos/python3_src/seed/io/iter_row_based_Z_delimited_text_file.py
    view /storage/emulated/0/0my_files/git_repos/python3_src/seed/io/iter_line_contents.py

seed.io.FieldedLineHandler
from seed.io.FieldedLineHandler import FieldedLineHandler, IFieldedLineHandler
e ../../python3_src/seed/io/FieldedLineHandler.py

used in:
    view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/reformat__Unihan_Variants_txt.py

#'''

__all__ = '''
    IFieldedLineHandler
        FieldedLineHandler
    '''.split()

from abc import ABC, abstractmethod
from seed.tiny import check_type_is, echo

class IFieldedLineHandler(ABC):
    __slots__ = ()
    @abstractmethod
    def clean_lines(sf, lines, /):
        'Iter line -> Iter line'
    @abstractmethod
    def lines2fieldss(sf, lines, /):
        'Iter line -> Iter [field]'
class FieldedLineHandler(IFieldedLineHandler):
    def __init__(sf, /, *, remove_empty_lines, line_strip, field_strip, line_comment_prefix, line_tail_comment_prefix, field_sep):
        #line_comment_prefix, line_tail_comment_prefix, field_sep may be ''
        check_type_is(bool, remove_empty_lines)
        check_type_is(bool, line_strip)
        check_type_is(bool, field_strip)
        check_type_is(str, line_comment_prefix)
        check_type_is(str, line_tail_comment_prefix)
        check_type_is(str, field_sep)

        sf._remove_empty_lines = remove_empty_lines
        sf._line_strip = line_strip
        sf._field_strip = field_strip
        sf._line_comment_prefix = line_comment_prefix
        sf._line_tail_comment_prefix = line_tail_comment_prefix
        sf._field_sep = field_sep

    def clean_lines(sf, lines, /):
        'Iter line -> Iter line'
        ######################
        if sf._line_tail_comment_prefix:
            line_tail_comment_prefix = sf._line_tail_comment_prefix
            def f__remove_tail_comment(s, /):
                r, _, _ = s.partition(line_tail_comment_prefix)
                return r
        else:
            f__remove_tail_comment = echo
        ######################
        if sf._line_strip:
            f__strip_line = str.strip
        else:
            f__strip_line = echo
        ######################
        if sf._line_comment_prefix:
            line_comment_prefix = sf._line_comment_prefix
            def pred__is_comment(s, /):

                return not s.startswith(line_comment_prefix)
        else:
            def pred__is_comment(s, /):
                return True
        ######################
        if sf._remove_empty_lines:
            pred__is_fielded_line = bool
        else:
            def pred__is_fielded_line(s, /):
                return True
        ######################
        lines = map(f__remove_tail_comment, lines)
            #tail_comment
        lines = map(f__strip_line, lines)
            #strip
        lines = filter(pred__is_comment, lines)
            #comment
        lines = filter(pred__is_fielded_line, lines)
            #empty_line
        return lines
    def lines2fieldss(sf, lines, /):
        'Iter line -> Iter [field]'
        ######################
        if sf._field_sep:
            field_sep = sf._field_sep
            def f__split_line(s, /):
                fields = s.split(field_sep)
                return fields
        else:
            def f__split_line(s, /):
                fields = [s]
                return fields
        ######################
        if sf._field_strip:
            f__strip_field = str.strip
        else:
            f__strip_field = echo
        ######################
        # f__line2fields = f__split_line >>> f__strip_field
        def f__line2fields(line, /):
            fields = f__split_line(line)
            fields = map(f__strip_field, fields)
            return fields
        ######################
        lines = sf.clean_lines(lines)
        fieldss = map(f__line2fields, lines)
        fieldss = map(tuple, fieldss)
        return fieldss





