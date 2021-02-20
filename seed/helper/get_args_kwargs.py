
__all__ = '''
    get_args_kwargs
    GetArgsKwargs
    xcall
    called_by
    '''.split()


from collections import namedtuple
from types import MappingView

def get_args_kwargs(*args, **kwargs):
    return args, kwargs

def xcall(f, x):
    return called_by(x, f)
def called_by(x, f):
    t = type(x)
    h = getattr(t, '__called_by__', None)
    if h is None:
        return f(x)
    else:
        return h(x, f)

_GetArgsKwargs = namedtuple('_GetArgsKwargs', 'args kwargs'.split())
class GetArgsKwargs(_GetArgsKwargs):
    def __new__(cls, *args, **kwargs):
        kwargs = MappingView(kwargs)
        self = super().__new__(cls, args, kwargs)
        return self

    def __called_by__(self, f):
        return f(*self.args, **self.kwargs)

    r'''
    def __init__(self, *args, **kwargs):
        self.__args = args
        self.__kwargs = MappingView(kwargs)
    @property
    def args(self):
        return self.__args
    @property
    def kwargs(self):
        return self.__kwargs
    def __iter__(self)
    def __len__(self)
    def __getitem__(self, i)
    #'''
xcall = GetArgsKwargs.xcall




