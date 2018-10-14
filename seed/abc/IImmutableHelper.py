
__all__ = '''
    IImmutableHelper
    '''.split()

from .IGetArgsKwargs import IGetArgsKwargs

class IImmutableHelper(IGetArgsKwargs):
    __slots__ = ()
    def __eq__(self, other):
        if self is other: return True

        cls = type(self)
        if cls is not type(other): return False
        get = cls.___get_std_args_sorted_kwargs_items___
        return get(self) == get(other)

    def __hash__(self):
        cls = type(self)
        args, sorted_items = cls.___get_std_args_sorted_kwargs_items___(self)
        return hash((cls, args, sorted_items))


