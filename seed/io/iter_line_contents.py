
r'''
example:
    >>> from seed.io.iter_line_contents import filter_line_contents \
    ...     , all_spaces, is_sharp_comment \
    ...     , filter_py_line_contents
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


import re
from seed.iters.filters import filters

def filter_line_contents(file, pred_exs):
    # pred_exs : see seed.iters.filters::filters
    it = iter_line_contents(file)
    it = filters(it, pred_exs)
    return it
def iter_line_contents(file):
    return map(line2content, file)
def line2content(line):
    if line.endswith('\n'):
        line = line[:-1]
    return line

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
def filter_py_line_contents(file):
    return filter_line_contents(file, py_style_pred_exs)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

