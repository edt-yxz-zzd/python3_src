
__all__ = '''
    IReprHelper
    '''.split()

from seed.helper.repr_input import repr_helper
from .IGetArgsKwargs import IGetArgsKwargs

class IReprHelper(IGetArgsKwargs):
    __slots__ = ()
    def __repr__(self):
        args, kwargs = type(self).___get_args_kwargs___(self)
        return repr_helper(self, *args, **kwargs)


