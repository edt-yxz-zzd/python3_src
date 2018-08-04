

__all__ = '''
    IGetArgsKwargs
    '''.split()

from . import ABC, abstractmethod


class IGetArgsKwargs(ABC):
    __slots__ = ()
    @abstractmethod
    def ___get_args_kwargs___(self):pass

