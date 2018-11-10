

__all__ = '''
    BadRecognizerError
    BadBiRegexError
    TokenizerFailError_with_tail
    '''.split()
from ..ITokenizer import TokenizerBaseError, TokenizerFailError

class BadRecognizerError(TokenizerBaseError):pass
class BadBiRegexError(TokenizerBaseError):pass
class TokenizerFailError_with_tail(TokenizerFailError):
    def __init__(self, err_msg, err_position, source, begin, end):
        assert type(err_position) is int
        sepline = '='*60
        tail = source[err_position:end]
        init = source[begin:err_position]
        super().__init__(f'{err_msg}\n@{err_position}\n{sepline}\n{init}\n{sepline}\n{tail!s}\n{sepline}\n')




