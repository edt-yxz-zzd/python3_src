
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
from seed.tiny import echo, print_err


def iter_TSV__path(path, *, encoding, case='path', **kw):
    r"-> Iter ((line_number, raw_line, line_content), parts)"
    return iter_TSV_(path, case=case, encoding=encoding, **kw)
def iter_TSV__file(fin, *, case='stream', encoding=None, **kw):
    r"-> Iter ((line_number, raw_line, line_content), parts)"
    return iter_TSV_(fin, case=case, encoding=encoding, **kw)

def iter_TSV_(input, *, sep='\t', case:'stream|path|data', encoding, **kw):
    r"-> Iter ((line_number, raw_line, line_content), parts)"
    return iter_row_based_Z_delimited_text_file_(input, sep=sep, case=case, encoding=encoding, **kw)
def iter_row_based_Z_delimited_text_file_(input, *, sep, case:'stream|path|data', encoding, skip_empty_lines=False, skip_space_lines=False, line_number_offset=0):
    r"-> Iter ((line_number, raw_line, line_content), parts)"
    return iter_row_based_Z_delimited_text_file__(input, line_number_offset=line_number_offset, sep=sep, skip_empty_lines=skip_empty_lines, skip_space_lines=skip_space_lines, case=case, encoding=encoding)
def iter_row_based_Z_delimited_text_file__(input, *, sep:str, case:'stream|path|data', encoding, skip_empty_lines:bool, skip_space_lines:bool, line_number_offset:int):
    r"-> Iter ((line_number, raw_line, line_content), parts)"
    skip_empty_lines = bool(skip_empty_lines)
    skip_space_lines = bool(skip_space_lines)
    if skip_space_lines:
        def _skip(line_content):
            return not line_content or line_content.isspace()
    elif skip_empty_lines:
        def _skip(line_content):
            return not line_content
    else:
        def _skip(line_content):
            return False

    it = bare_iter_row_based_Z_delimited_text_file__(input, sep=sep, case=case, encoding=encoding)
    it = enumerate(it, line_number_offset)
    for line_number, (raw_line, line_content, parts) in it:
        if _skip(line_content): continue
        yield ((line_number, raw_line, line_content), parts)
def bare_iter_row_based_Z_delimited_text_file__(input, *, sep, case:'stream|path|data', encoding):
    r"-> Iter (raw_line, line_content, parts)"
    it = iter_line_contents_(input, raw_line2content=echo, case=case, encoding=encoding)
    for raw_line in it:
        line_content = raw_line2content(raw_line)
        parts = line_content.split(sep)
        yield raw_line, line_content, parts

