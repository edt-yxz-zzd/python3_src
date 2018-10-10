
__all__ = ['IOps']
from .abc import ABC, abstractmethod, override, not_implemented, ABCMeta


class IOps(ABC):
    __slots__ = ()

    @not_implemented
    def __hash__(self):
        raise NotImplementedError
    @not_implemented
    def __eq__(self):
        raise NotImplementedError

