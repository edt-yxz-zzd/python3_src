

__all__ = '''
    len_of_iterable
    len_of_iterator

    '''.split()

def len_of_iterable(iterable):
    '''len_of_iterable

len_of_iterable v.s. len_of_iterator
        len_of_iterable may use __len__
        len_of_iterator always O(n)

example:
    >>> this = len_of_iterable
    >>> this([])
    0
    >>> this(iter([]))
    0
    >>> this([1,2,3])
    3
    >>> this(iter([1,2,3]))
    3
'''
    if hasattr(iterable, '__len__'):
        return len(iterable)
    return len_of_iterator(iterable)

def len_of_iterator(iterable):
    '''len_of_iterator

len_of_iterable v.s. len_of_iterator
        len_of_iterable may use __len__
        len_of_iterator always O(n)

example:
    >>> this = len_of_iterator
    >>> this([])
    0
    >>> this(iter([]))
    0
    >>> this([1,2,3])
    3
    >>> this(iter([1,2,3]))
    3
'''

    i = -1
    for i, _ in enumerate(iterable): pass
    return i+1

if __name__ == "__main__":
    import doctest
    doctest.testmod()


