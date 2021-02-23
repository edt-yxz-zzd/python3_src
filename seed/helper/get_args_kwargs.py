
r'''

py -m seed.helper.get_args_kwargs

from seed.helper.get_args_kwargs import mk_GetArgsKwargs, xcall

>>> g = mk_GetArgsKwargs(3, 2, 1, b=4, a=5)
>>> g
mk_GetArgsKwargs(3, 2, 1, a = 5, b = 4)

>>> g.args
(3, 2, 1)
>>> type(g.kwargs)
<class 'seed.types.FrozenDict.FrozenDict'>
>>> g.kwargs
FrozenDict({'b': 4, 'a': 5})
>>> g._replace([7,8])
Traceback (most recent call last):
    ...
TypeError: _replace() takes 1 positional argument but 2 were given
>>> g._replace(args=[7,8])
Traceback (most recent call last):
    ...
TypeError

>>> g._replace(args=(7,8))
mk_GetArgsKwargs(7, 8, a = 5, b = 4)
>>> g.iupdate([9])
mk_GetArgsKwargs(9, 2, 1, a = 5, b = 4)
>>> g.iupdate([10], [11])
mk_GetArgsKwargs(10, 11, 1, a = 5, b = 4)
>>> g.iupdate([12], [])
mk_GetArgsKwargs(12, 2, 1, a = 5, b = 4)
>>> g.iupdate([], [], [13])
mk_GetArgsKwargs(3, 2, 13, a = 5, b = 4)
>>> g.iupdate([], [], [], [14])
mk_GetArgsKwargs(3, 2, 1, 14, a = 5, b = 4)
>>> g.iupdate(b=15,c=16)
mk_GetArgsKwargs(3, 2, 1, a = 5, b = 15, c = 16)

#>>> dir(_)
#>>> help(_._make)
>>> type(_)._make(([], {}))
Traceback (most recent call last):
    ...
TypeError

#'''



__all__ = '''
    mk_GetArgsKwargs
    mk_GetArgsKwargs__convert
    GetArgsKwargs
    xcall
    called_by
    get_args_kwargs
    '''.split()


from collections import namedtuple
#from seed.types.view.View import MapView

from seed.types.FrozenDict import FrozenDict
from seed.helper.repr_input import repr_helper_ex
#from seed.helper.repr_input import repr_helper

def get_args_kwargs(*args, **kwargs):
    return args, kwargs

def xcall(f, x, *, kwarg=None):
    return called_by(x, f, kwarg=kwarg)
def called_by(x, f, *, kwarg=None):
    t = type(x)
    h = getattr(t, '__called_by__', None)
    if h is None:
        if not kwarg:
            return f(x)
        else:
            return f(**{kwarg:x})
    else:
        return h(x, f)

def mk_GetArgsKwargs(*args, **kwargs):
    return mk_GetArgsKwargs__convert(args, kwargs)

def mk_GetArgsKwargs__convert(args, kwargs):
    if type(args) is not tuple:
        args = tuple(args)
    if type(kwargs) is not FrozenDict:
        kwargs = FrozenDict(kwargs)
    self = GetArgsKwargs(args, kwargs)
    return self

def _g_check(args, kwargs):
    if type(args) is not tuple: raise TypeError
    if type(kwargs) is not FrozenDict: raise TypeError
_GetArgsKwargs = namedtuple('_GetArgsKwargs', 'args kwargs'.split())
class GetArgsKwargs(_GetArgsKwargs):
    #def __new__(cls, *args, **kwargs):
    def __new__(cls, args, kwargs):
        _g_check(args, kwargs)
        #kwargs = MapView(kwargs)
        #kwargs = FrozenDict(kwargs)
        self = super().__new__(cls, args, kwargs)
        self._check()
        return self
    def __init__(self, args, kwargs):
        _g_check(args, kwargs)
        self._check()
    def _check(self):
        _g_check(self.args, self.kwargs)

    def __called_by__(self, f):
        return f(*self.args, **self.kwargs)
    @classmethod
    def _make(cls, iterable):
        return cls(*iterable)
    def _replace(__self, **kws):
        self = __self
        #d = dict(args=self.args, kwargs=self.kwargs)
        d = self._asdict()
        d.update(kws)
        return type(self)(**d)

    def iupdate(__self, *may_new_args, **kwargs):
        r'''
        usage: other = self.iupdate([], [x], [y], k=z, w=w)
        #'''
        self = __self
        if not may_new_args and not kwargs:
            return self
        if not may_new_args:
            new_args = self.args
        else:
            ls = []
            for may_new_arg, old_arg in zip(may_new_args, self.args):
                if may_new_arg:
                    [new_arg] = may_new_arg
                else:
                    new_arg = old_arg
                ls.append(new_arg)
            n = len(may_new_args) - len(self.args)
            if n > 0:
                remains = may_new_args[-n:]
                assert remains
                for may_new_arg in remains:
                    [new_arg] = may_new_arg
                    ls.append(new_arg)
            elif n < 0:
                remains = self.args[n:]
                assert remains
                for old_arg in remains:
                    new_arg = old_arg
                    ls.append(new_arg)
            if len(ls) == len(self.args) and all(new_arg is old_arg for new_arg, old_arg in zip(ls, self.args)):
                new_args = self.args
            else:
                new_args = tuple(ls)
        if not kwargs:
            new_kwargs = self.kwargs
        else:
            d = dict(self.kwargs)
            d.update(kwargs)
            new_kwargs = FrozenDict(d)
        return type(self)(args=new_args, kwargs=new_kwargs)
    def __repr__(self):
        #return repr_helper(self, *args, **kwargs)
        return repr_helper_ex('mk_GetArgsKwargs', self.args, [], self.kwargs, name_only=True)


    r'''
    def __init__(self, *args, **kwargs):
        self.__args = args
        self.__kwargs = MapView(kwargs)
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
#xcall = GetArgsKwargs.xcall



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):



