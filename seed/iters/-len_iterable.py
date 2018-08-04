

'''
see:
    len_of_iterator
    len_of_iterable

'''


__all__ = '''
    len_iterable
'''.split()

from .len_of_iterator import len_of_iterable

def len_iterable(iterable):
    try:
        return len(iterable)
    except TypeError:
        i = -1
        for i, _ in enumerate(iterable):
            pass
        return i + 1

len_iterable = len_of_iterable

assert len_iterable([]) == 0
assert len_iterable(iter([])) == 0
assert len_iterable([1]) == 1
assert len_iterable(iter([1])) == 1
