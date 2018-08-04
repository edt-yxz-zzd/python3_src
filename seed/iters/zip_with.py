
__all__ = '''
    zip_with
    starzip_with
'''.split()

from itertools import chain
def zip_from_iterable(iterables):
    return zip(*iterables)

def __inputf2func_pre_post(f):
    pre_args = post_args = None
    if callable(f):
        pass
    if len(f) == 2:
        f, pre_args = f
    elif len(f) == 3:
        f, pre_args, post_args = f
    else:
        raise TypeError('f should be func | (func, pre_args) | (func, pre_args, post_args)')

    pre_args = () if pre_args is None else tuple(pre_args)
    post_args = () if post_args is None else tuple(post_args)
    return f, pre_args, post_args
def zip_with(f, *iterables, **kwargs):
    'f :: func | (func, pre_args) | (func, pre_args, post_args); args::None|iterable'
    return starzip_with(f, zip(*iterables), **kwargs)
        
        
def starzip_with(f, iterable, **kwargs):
    'f :: func | (func, pre_args) | (func, pre_args, post_args); args::None|iterable'
    f, pre_args, post_args = __inputf2func_pre_post(f)
    for mid_args in iterable:
        args = chain(pre_args, mid_args, post_args)
        yield f(*args, **kwargs)






