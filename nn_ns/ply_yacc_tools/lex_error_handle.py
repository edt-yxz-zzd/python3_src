
'''
usage:
    see: nn_ns.my_fileformat.configuration.MyConfiguration2_lex
'''


__all__ = '''
    LexError
    token_error_handle
    lex_error_handle
    '''.split()


from .extract_token_info import extract_token_info

class LexError(SyntaxError):
    def __init__(self, d, *, token):
        super().__init__(d)
        self.token = token
    pass

def token_error_handle(t, ErrorType, err_msg:str, *args, **kwargs):
    # t is from rough_pattern
    #   but precise_pattern do not accept it.
    # ErrorType=SyntaxError/IndentationError
    d = extract_token_info(t, err_msg=err_msg, **kwargs)
    # weird error:
    #   SyntaxError(d, t)
    #       TypeError: 'LexToken' object is not iterable
    #   SyntaxError(t, d)
    #       IndexError: tuple index out of range
    def f():
        e = ErrorType(d)
        e.args = (d, t, *args)
        raise e
    if ErrorType in (SyntaxError, IndentationError):
        raise f()
    try:
        raise ErrorType(d, t, *args)
    except TypeError:
        raise f()

def lex_error_handle(t, state):
    # lexer cannot found a match token for remain_source_string
    #   t.value is the remain_source_string
    d = extract_token_info(t, state=state)
    del d['token_value']

    assert len(t.value) == len(t.lexer.lexdata) - d['error_pos']
    remain_source_string = t.value
    raise LexError(d, token = t)


