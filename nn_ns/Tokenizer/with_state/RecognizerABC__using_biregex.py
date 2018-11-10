
__all__ = '''
    RecognizerABC__using_biregex
    RecognizerABC__using_biregex__directly
    may_recognize1_helper
    '''.split()

from ..class_property import class_property
from ..biregex.IBiRegex import IBiRegex
from .errors import BadBiRegexError, TokenizerFailError_with_tail
from .IRecognizer import IRecognizer
from .abc import ABC, abstractmethod, final, override
import inspect
    # auto
    #.make_token(terminal_name, token_value, **token_named_values) -> token
class RecognizerABC__using_biregex(IRecognizer):
    '''

# state should not be callable or None
# any object has below attrs and s.t. IRecognizer be a RecognizerABC__using_biregex
    # user provide
    .biregex
    .to_state
        None        - not change state
        callable    - .to_state(state, regex_match_result) -> state
        st          - result state
    .iter_tokens(regex_match_result) -> Iter token
'''
    __slots__ = ()
    @property
    @abstractmethod
    def biregex(self):
        # :: IBiRegex
        raise NotImplementedError

    @property
    @abstractmethod
    def to_state(self):
        # :: None|callable|succ_state
        # state should not be callable or None
        raise NotImplementedError

    @abstractmethod
    def iter_tokens(self, regex_match_result):
        # :: Iterable token
        raise NotImplementedError

    @final
    @override
    def may_recognize1(self, state, source, begin, end):
        # -> None|(tokens, succ_state, middle)
        return may_recognize1_helper(self, state, source, begin, end)

class RecognizerABC__using_biregex__directly(IRecognizer):
    __slots__ = ()

    def __init_subclass__(cls, **kwargs):
        if not inspect.isabstract(cls):
            _cls = cls.recognizer_dict.setdefault(cls.name, cls)
            if _cls is not cls:
                raise Exception('{cls.name!r} recognizer already exists')
        super().__init_subclass__()

    @class_property
    @abstractmethod
    def recognizer_dict(cls):
        # :: {name: recognizer}
        # mutable
        raise NotImplementedError

    @class_property
    @override
    def name(cls):
        return cls.__name__

    @class_property
    @abstractmethod
    def biregex(cls):
        # :: IBiRegex
        raise NotImplementedError

    @class_property
    @abstractmethod
    def to_state(cls):
        # :: None|callable|succ_state
        # state should not be callable or None
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def iter_tokens(cls, regex_match_result):
        # :: Iterable token
        raise NotImplementedError

    @classmethod
    @final
    @override
    def may_recognize1(cls, state, source, begin, end):
        # -> None|(tokens, succ_state, middle)
        return may_recognize1_helper(cls, state, source, begin, end)
assert RecognizerABC__using_biregex__directly.name == 'RecognizerABC__using_biregex__directly'

def may_recognize1_helper(self, state, source, begin, end):
    # -> None|(tokens, succ_state, middle)
    m1 = self.biregex.rough_regex.match(source, begin, end)
    if m1 is None:
        return None
    m2 = self.biregex.precise_regex.match(source, begin, end)
    if m2 is None:
        err_position = begin
        err_msg = f'recognizer {self.name!r}: may_recognize1 fail: trap by biregex {self.biregex.name!r}'
        raise TokenizerFailError_with_tail(err_msg, err_position, source, begin, end)
    if m2.end() != m1.end():
        raise BadBiRegexError('result from precise_regex is diff with that from rough_regex: {self.biregex.name!r}')


    tokens = self.iter_tokens(m2)
    middle = m2.end()

    to_state = self.to_state
    if to_state is None:
        succ_state = state
    elif callable(to_state):
        succ_state = to_state(state, m2)
    else:
        succ_state = to_state
    return tokens, succ_state, middle




