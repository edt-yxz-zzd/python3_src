
r'''
case, encoding
    see: with_text_input_file_


example:
    >>> from seed.io.iter_line_contents import filter_line_contents, all_spaces, is_sharp_comment, filter_py_line_contents
    >>> import io
    >>> fin = io.StringIO(' \n # \n first line \n 2nd')
    >>> it = filter_line_contents(fin, [])
    >>> list(it)
    [' ', ' # ', ' first line ', ' 2nd']
    >>> _ = fin.seek(0);
    >>> it = filter_line_contents(fin, [(all_spaces, True), (is_sharp_comment, True)])
    >>> list(it)
    [' first line ', ' 2nd']
    >>> _ = fin.seek(0);
    >>> it = filter_py_line_contents(fin)
    >>> list(it)
    [' first line ', ' 2nd']
'''


__all__ = '''
    filter_py_line_contents
        filter_line_contents
        iter_line_contents

        filter_py_line_contents_
        filter_line_contents_
        iter_line_contents_
        raw_line2content

    beginswith_regex
        beginswith_spaces_digit
    all_spaces_or_is_sharp_comment
        all_spaces
        is_sharp_comment
    '''.split()

import re
from seed.iters.filters import filters
import io
from seed.io.with_text_input_file import with_text_input_file_


def raw_line2content(line):
    if line and line[-1] in '\n\r':
        n = 0
        if line.endswith('\r\n'):
            n = 2
        elif line.endswith('\n\r'):
            n = 2
        elif line.endswith('\n'):
            n = 1
        elif line.endswith('\r'):
            n = 1
        else:
            raise logic-error
        if n:
            line = line[:-n]
    return line


def filter_line_contents(input, pred_exs, *, raw_line2content=raw_line2content, case:'stream|path|data'='stream', encoding=''):
    return filter_line_contents_(input, pred_exs, raw_line2content=raw_line2content, case=case, encoding=encoding)

def iter_line_contents(input, *, raw_line2content=raw_line2content, case:'stream|path|data'='stream', encoding=''):
    return iter_line_contents_(input, raw_line2content=raw_line2content, case=case, encoding=encoding)

def filter_py_line_contents(input, *, raw_line2content=raw_line2content, case:'stream|path|data'='stream', encoding=''):
    return filter_py_line_contents_(input, raw_line2content=raw_line2content, case=case, encoding=encoding)








def filter_line_contents_(input, pred_exs, *, raw_line2content, case:'stream|path|data', encoding):
    # pred_exs : see seed.iters.filters::filters
    it = iter_line_contents_(input, raw_line2content=raw_line2content, case=case, encoding=encoding)
    it = filters(it, pred_exs)
    return it

def iter_line_contents_(input, *, raw_line2content, case:'stream|path|data', encoding):
    def f(tfile):
        return map(raw_line2content, tfile)
    return with_text_input_file_(input, f, None, encoding=encoding, case=case, yield_from=True)
    r"""
    _input = kwargs2tuple4with_text_input_file(input, encoding=encoding, case=case)
    did_open, tfile = open_ex4with_text_input_file(_input)
    return map(raw_line2content, tfile)
    #"""









def all_spaces(line):
    # r'\s*'
    return not line or line.isspace()
assert all_spaces('')
assert all_spaces('\n')
assert all_spaces('\n\t ')
assert not all_spaces('\n\t 1 ')
def all_spaces_or_is_sharp_comment(line):
    # r'\s*(#.*)?'
    i = line.find('#')
    if i == -1:
        i = len(line)
        spaces = line
    else:
        assert i >= 0
        spaces = line[:i]
    return all_spaces(spaces)

def is_sharp_comment(line):
    # r'\s*#.*'
    spaces, sharp, comment = line.partition('#')
    return sharp and all_spaces(spaces)

def beginswith_regex(rex_or_pattern):
    rex = re.compile(rex_or_pattern)
    def test_beginswith(s):
        return bool(rex.match(s))
    return test_beginswith
beginswith_spaces_digit = beginswith_regex(r'\s*\d')


py_style_pred_exs = [(all_spaces, True), (is_sharp_comment, True)]
def filter_py_line_contents_(input, *, raw_line2content, case:'stream|path|data', encoding):
    return filter_line_contents_(input, py_style_pred_exs, raw_line2content=raw_line2content, case=case, encoding=encoding)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

