

__all__ = '''
    IGetArgsKwargs
    '''.split()

from . import ABC, abstractmethod


class IGetArgsKwargs(ABC):
    __slots__ = ()
    @abstractmethod
    def ___get_args_kwargs___(self):
        # -> (args:Seq, kwargs:Mapping)
        pass
    def ___get_std_args_sorted_kwargs_items___(self):
        # -> (tuple(args), tuple(sorted(kwargs.items())))
        cls = type(self)
        args, kwargs = cls.___get_args_kwargs___(self)
        return (tuple(args), tuple(sorted(kwargs.items())))

