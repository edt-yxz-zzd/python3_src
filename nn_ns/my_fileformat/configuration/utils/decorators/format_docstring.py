

__all__ = '''
    format_docstring
    '''.split()

import re
# {1} should {{1}}
bad_fmt_prefix_regex = re.compile(r'(?:[^{]|[{](?=[^0-9])[\w{])*(?P<bad>[{](?=[^\w{]|[0-9])[^}]*[}]?)')
#bad_fmt_prefix_regex = re.compile(r'(?:[^{]|[{][\w{])*(?P<bad>[{](?=[^\w{]))')

def format_docstring(**kwargs):
    r'''format the docstring of ...

usage:
@format_docstring(at_line_begin=r'(?<![^\n])')
def t_XXX(t):
    r'{at_line_begin}(?:a{{4}}...)'
    return t

see:
    useful_regex_patterns_decorator.py
'''
    def decorator(f):
        doc_fmt = f.__doc__
        try:
            f.__doc__ = doc_fmt.format(**kwargs)
        except IndexError:
            if type(doc_fmt) is not str:
                raise
            m = bad_fmt_prefix_regex.match(doc_fmt)
            if not m:
                #print(doc_fmt)
                raise
            bad = m.group('bad')
            raise IndexError(f'format string syntax error: {bad!r} from {doc_fmt!r} : ### {{1}} ==>> {{{{1}}}}')
        return f
    return decorator
