
__all__ = '''
    join_lines
    '''.split()



from .write_lines import write_lines
from io import StringIO


def join_lines(lines, *, line_prefix='\t', line_sep='\n', line_suffix=''):
    r'''

example:
    >>> join_lines([])
    ''
    >>> lines = 'abc'
    >>> join_lines(lines)
    '\ta\n\tb\n\tc'
    >>> join_lines(lines, line_prefix='P', line_sep='-', line_suffix='S')
    'PaS-PbS-PcS'

'''
    fout = StringIO()
    write_lines(fout, lines
        , line_prefix=line_prefix
        , line_sep=line_sep
        , line_suffix=line_suffix)
    out = fout.getvalue()
    fout.close()
    return out

if __name__ == '__main__':
    import doctest
    doctest.testmod()

