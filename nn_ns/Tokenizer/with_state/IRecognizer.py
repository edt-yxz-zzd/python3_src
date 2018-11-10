
__all__ = '''
    IRecognizer
    '''.split()

from .abc import ABC, abstractmethod

class IRecognizer(ABC):
    '''see: Tokenizer_with_state

# any object has below attrs be a recognizer
recognizer:
    .name :: Hashable&Comparable
        e.g. str
    .may_recognize1(state, source, begin, end) -> None|(tokens, succ_state, middle)
        tokens :: Iterable token
            may or may not be iterator
    .allow_empty :: bool
    .precondition_states :: {state} | None
        None - any state
'''
    __slots__ = ()
    @property
    @abstractmethod
    def name(self):
        # :: Hashable&Comparable
        raise NotImplementedError
    @abstractmethod
    def may_recognize1(self, state, source, begin, end):
        # -> None|(tokens, succ_state, middle)
        raise NotImplementedError
    @property
    @abstractmethod
    def allow_empty(self):
        # :: bool
        raise NotImplementedError
    @property
    @abstractmethod
    def precondition_states(self):
        # :: Set state
        raise NotImplementedError


