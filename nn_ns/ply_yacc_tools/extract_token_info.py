
'''
used by :lex_error_handle/token_error_handle
'''
__all__ = '''
    extract_token_info
    '''.split()

from .overflow_xfind import overflow_rfind, overflow_find
def extract_token_info(t:'ply.lex.LexToken', **kwargs):
    pos = t.lexpos
    lineno = t.lineno
    lexer = t.lexer
    source_string = lexer.lexdata
    #assert '\r' not in source_string
    #columnno = pos - source_string.rfind('\n', 0, pos)

    L = len(source_string)
    i = overflow_rfind('\n\r', source_string, 0, pos)
    j = overflow_find('\n\r', source_string, pos, L)

    columnno = pos - i
    current_line_begin = i+1
    current_line_end = j
    current_line = source_string[current_line_begin:current_line_end]
    good_half = source_string[current_line_begin:pos]
    bad_half = source_string[pos:current_line_end]
    d = dict(
        error_pos = pos
        ,may_error_char = source_string[pos:pos+1]
        ,lineno = lineno
        ,columnno = columnno

        ,good_half = good_half
        ,bad_half = bad_half
        ,current_line = current_line
        ,token_value = t.value
        ,token_type = t.type
        )
    if kwargs:
        d = {**kwargs, **d}
    return d


