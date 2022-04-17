
r'''
from seed.func_tools.dot2 import dot
NOTE:
    use dot[[...],] instead of dot[[...]]
        which <==> partial(...)

dot[f,g](*args, **kwargs)
    =[def]= f(g(*args, **kwargs))

dot[[f, arg...], g](*args, **kwargs)
    =[def]= f(args..., g(*args, **kwargs))

dot[[f, a...]:kw, g](*args, **kwargs)
    =[def]= f(a..., g(*args, **kwargs), **kw)

dot[[f, a...]:kw:[b...], g](*args, **kwargs)
    =[def]= f(a..., g(*args, **kwargs), b..., **kw)

dot[[f, a...]::[b...], g](*args, **kwargs)
    =[def]= f(a..., g(*args, **kwargs), b...)

    >>> assert dot[tuple, list, map](int, '0123') == (0,1,2,3)
    >>> assert dot[tuple, [map, lambda a,b:a+b, [1,2,3]], echo_args](2,4,6) == (3,6,9)
    >>> assert dot[str, int:{'base':16}]('A') == '10'

#'''


__all__ = '''
    dot
    '''.split()
#from itertools
from functools import partial
from seed.tiny import ifNone, echo

def pseudo_func2func_last_args(pseudo_func):
    if type(pseudo_func) is slice:
        pseudo_funcB = pseudo_func.start
        if pseudo_funcB is None: raise TypeError
        f, args = pseudo_funcB2func(pseudo_funcB)
        may_kwargs = pseudo_func.stop
        may_last_args = pseudo_func.step
    else:
        pseudo_funcB = pseudo_func
        f, args = pseudo_funcB2func(pseudo_funcB)
        may_kwargs = None
        may_last_args = None
    kwargs = ifNone(may_kwargs, {})
    last_args = ifNone(may_last_args, ())
    last_args = tuple(last_args)

    f = partial(f, *args, **kwargs)
    return f, last_args

def pseudo_funcB2func(pseudo_funcB):
    if callable(pseudo_funcB):
        return pseudo_funcB, ()
    if len(pseudo_funcB) < 2:
        raise TypeError
    f = pseudo_funcB[0]
    if callable(f):
        return f, pseudo_funcB[1:]
    raise TypeError


class Dot:
    # pseudo_funcs = callable | tuple[pseudo_func]{2..}
    # pseudo_func   = slice(pseudo_funcB, may_kwargs, may_last_args)
    #               | pseudo_funcB
    # pseudo_funcB  = callable | [callable, object...]
    def __init__(self, __pseudo_funcs):
        pseudo_funcs = __pseudo_funcs
        if 0:
            r'''
            deprecated:updated to support:
                dot[[f, x, y]]
                dot[f:x:y]
            deprecated by:
                dot[[f, x, y],]
                dot[f:kw:zs,]
            #'''
            if callable(pseudo_funcs):
                f = pseudo_funcs
                last_args = ()
                pairs = ((f, last_args),)
            else:
                if not type(pseudo_funcs) is tuple:
                    x = pseudo_funcs
                    pseudo_funcs = (x,)
                assert type(pseudo_funcs) is tuple
                pairs = tuple(map(pseudo_func2func_last_args, pseudo_funcs))
                if not pairs:
                    pairs = (echo, ()),
        else:
            if type(pseudo_funcs) is tuple:
                pairs = tuple(map(pseudo_func2func_last_args, pseudo_funcs))
                if not pairs:
                    pairs = (echo, ()),
            elif callable(pseudo_funcs):
                f = pseudo_funcs
                last_args = ()
                pairs = (f, last_args),
            else:
                raise TypeError

        self.__func_last_args_pairs = pairs
        if False and len(pairs) < 2:
            # why?
            #   dot[x,y...]
            #   dot[]       # syntax error; dot[()]?
            #   dot[x]      # input is not a tuple
            #   dot[x,y]    # fine
            raise TypeError('too few funcs')
    def __call__(self, *args, **kwargs):
        pairs = self.__func_last_args_pairs
        it = reversed(pairs)
        for f, last_args in it:
            r = f(*args, *last_args, **kwargs)
            break
        else: raise logic-error
        for f, last_args in it:
            r = f(r, *last_args)
        return r
class _dot:
    def __getitem__(self, __pseudo_funcs):
        pseudo_funcs = __pseudo_funcs
        return Dot(pseudo_funcs)
dot = _dot()

def echo_args(*args):
    return args

def _t():
    assert dot[tuple, list, map](int, '0123') == (0,1,2,3)
    assert dot[tuple, [map, lambda a,b:a+b, [1,2,3]], echo_args](2,4,6) == (3,6,9)
    assert dot[str, int:{'base':16}]('A') == '10'

if __name__ == "__main__":
    _t()
    import doctest
    doctest.testmod()









