

'''
>>> PySort(reverse=True)([1,3,2])
[3, 2, 1]

'''

__all__ = '''
    PySort
    '''.split()

from .ISortBase import ISortBase_Key_Reverse

class PySort(ISortBase_Key_Reverse):
    def __init__(self, *, key=None, reverse=False):
        ISortBase_Key_Reverse.__init__(self, key=key, reverse=reverse)
    def __call__(self, __objs):
        return self.py_sort(__objs)
    def py_sort(self, __objs):
        return sorted(__objs, key=self.key, reverse=self.reverse)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

