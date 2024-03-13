
r"""
from seed.io.iter_row_based_Z_delimited_text_file import iter_TSV__file, iter_TSV__path


e /storage/emulated/0/0my_files/git_repos/python3_src/seed/io/iter_row_based_Z_delimited_text_file.py
view /storage/emulated/0/0my_files/git_repos/python3_src/seed/io/iter_line_contents.py
def iter_line_contents_(input, *, raw_line2content, case:'stream|path|data', encoding):
#"""

__all__ = '''
    bare_iter_row_based_Z_delimited_text_file__
        iter_row_based_Z_delimited_text_file__
            iter_row_based_Z_delimited_text_file_
                iter_TSV_
                    iter_TSV__path
                    iter_TSV__file
    '''.split()

from seed.io.iter_line_contents import iter_line_contents_, raw_line2content
from seed.tiny import echo, print_err, check_type_is


def iter_TSV__path(path, *, encoding, case='path', **kw):
    r"-> Iter ((line_number, raw_line, line_content), parts)"
    return iter_TSV_(path, case=case, encoding=encoding, **kw)
def iter_TSV__file(fin, *, case='stream', encoding=None, **kw):
    r"-> Iter ((line_number, raw_line, line_content), parts)"
    return iter_TSV_(fin, case=case, encoding=encoding, **kw)

def iter_TSV_(input, *, sep='\t', case:'stream|path|data', encoding, **kw):
    r"-> Iter ((line_number, raw_line, line_content), parts)"
    return iter_row_based_Z_delimited_text_file_(input, sep=sep, case=case, encoding=encoding, **kw)
def iter_row_based_Z_delimited_text_file_(input, *, sep, case:'stream|path|data', encoding, skip_empty_lines=False, skip_space_lines=False, line_number_offset=0, smay_comment_prefix='', turnon__tail_comment=False):
    r"-> Iter ((line_number, raw_line, line_content), parts)"
    # supply defaults
    return iter_row_based_Z_delimited_text_file__(**locals())
def iter_row_based_Z_delimited_text_file__(input, *, sep:str, case:'stream|path|data', encoding, skip_empty_lines:bool, skip_space_lines:bool, line_number_offset:int, smay_comment_prefix:str, turnon__tail_comment:bool):
    r"-> Iter ((line_number, raw_line, line_content), parts)"
    check_type_is(bool, skip_empty_lines)
    check_type_is(bool, skip_space_lines)
    check_type_is(bool, turnon__tail_comment)
    check_type_is(str, smay_comment_prefix)

    ######################
    if skip_space_lines:
        def _skip(line_content):
            return not line_content or line_content.isspace()
    elif skip_empty_lines:
        def _skip(line_content):
            return not line_content
    else:
        def _skip(line_content):
            return False
    _skip

    ######################
    if smay_comment_prefix:
        comment_prefix = smay_comment_prefix
        _skip0 = _skip
        def _skip(line_content):
            return line_content.startswith(comment_prefix) or _skip0(line_content)
    _skip

    ######################
    strip_tail_comment_ = echo
    if smay_comment_prefix:
        if turnon__tail_comment:
            def strip_tail_comment_(line_content):
                imay = line_content.find(comment_prefix)
                if not imay < 0:
                    i = imay
                    line_content = line_content[:i]
                return line_content
        else:
            strip_tail_comment_
        strip_tail_comment_
    strip_tail_comment_

    ######################
    it = bare_iter_row_based_Z_delimited_text_file__(input, sep=sep, case=case, encoding=encoding)
    it = enumerate(it, line_number_offset)
    for line_number, (raw_line, line_content, parts) in it:
        line_content = strip_tail_comment_(line_content)
        if _skip(line_content): continue
        yield ((line_number, raw_line, line_content), parts)
def bare_iter_row_based_Z_delimited_text_file__(input, *, sep, case:'stream|path|data', encoding):
    r"-> Iter (raw_line, line_content, parts)"
    it = iter_line_contents_(input, raw_line2content=echo, case=case, encoding=encoding)
    for raw_line in it:
        line_content = raw_line2content(raw_line)
        parts = line_content.split(sep)
        yield raw_line, line_content, parts

