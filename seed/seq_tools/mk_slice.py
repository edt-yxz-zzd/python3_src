
__all__ = '''
    mk_slice
    '''.split()

class MkSlice:
    '''helper to make slice object

example:
    >>> mk_slice[::]
    slice(None, None, None)
    >>> mk_slice[1:2]
    slice(1, 2, None)
'''
    __slots__ = ()
    def __getitem__(self, sl):
        if type(sl) is not slice: raise TypeError
        return sl
mk_slice = MkSlice()

if __name__ == "__main__":
    import doctest
    doctest.testmod()



