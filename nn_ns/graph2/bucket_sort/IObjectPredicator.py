

__all__ = '''
    IObjectPredicator
    IElementEq
    are_elements
    '''.split()
from abc import ABC, abstractmethod

class IObjectPredicator(ABC):
    @abstractmethod
    def is_element(self, obj):
        raise NotImplementedError


class IElementEq(IObjectPredicator):
    @abstractmethod
    def element_eq(self, elem1, elem2):
        raise NotImplementedError

def are_elements(iterable, tv):
    assert isinstance(tv, IObjectPredicator)
    return all(map(tv.is_element, iterable))


