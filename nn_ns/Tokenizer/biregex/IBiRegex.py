
__all__ = '''
    IBiRegex
    '''.split()

from .abc import ABC, abstractmethod, final

class IBiRegex(ABC):
    '''

# any object has below attrs be a IBiRegex
biregx:
    .rough_regex
        trap into
        (?!biregx.rough_regex.pattern)
    .precise_regex
        exactly
        (?=biregx.precise_regex.pattern)
'''
    __slots__ = ()
    @property
    @abstractmethod
    def rough_regex(self):
        # :: regex
        raise NotImplementedError
    @property
    @abstractmethod
    def precise_regex(self):
        # :: regex
        raise NotImplementedError

