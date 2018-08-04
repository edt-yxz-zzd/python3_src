
__all__ = ['run_all']
#from collections.abc import Iterator

def run_all(iterator):
    'iterator is iterable but iterable may not be iterator'
    next(iterator, None) # check whether a iterator
    for _ in iterator: pass
    return

    if not hasattr(iterator, '__next__'):
        raise TypeError('not iterator')

    
