
r'''[[[
e ../../python3_src/seed/types/view/SeqLeftRotateView.py

py -m seed.types.view.SeqLeftRotateView

from seed.types.view.SeqLeftRotateView import SeqLeftRotateView


#]]]'''

__all__ = '''
    SeqLeftRotateView
    '''.split()

from collections.abc import Sequence
from seed.helper.repr_input import repr_helper


class SeqLeftRotateView(Sequence):
    r'''[[[
    >>> from seed.types.view.SeqLeftRotateView import SeqLeftRotateView
    >>> SeqLeftRotateView(range(9), 3)[:]
    (3, 4, 5, 6, 7, 8, 0, 1, 2)
    >>> SeqLeftRotateView(range(9), 3)[5::2]
    (8, 1)
    >>> SeqLeftRotateView(SeqLeftRotateView(range(9), -5), 3)[:]
    (7, 8, 0, 1, 2, 3, 4, 5, 6)
    >>> SeqLeftRotateView(SeqLeftRotateView(range(9), -5), 3)[5::2]
    (3, 5)

    #]]]'''
    def __init__(self, seq, k):
        ':: [a] -> int -> [a]'
        if not isinstance(seq, Sequence): raise TypeError
        if not isinstance(k, int): raise TypeError

        if isinstance(seq, __class__):
            other = seq
            seq = other.__seq
            k += other.__k

        self.__k = k
        self.__seq = seq
        self.__L = None
        self.__rng = None
        self.__refresh()
    def __refresh(self, /):
        if not self.__L == len(self.__seq):
            self.__L = len(self.__seq)
            neg_k_mod_L = (-self.__k) % self.__L if self.__L else 0
            self.__rng = range(-neg_k_mod_L, self.__L-neg_k_mod_L)
            return
            #bug:
            __k_mod_L = self.__k % self.__L if self.__L else 0
            self.__rng = range(-__k_mod_L, self.__L-__k_mod_L)

    def __getitem__(self, i):
        self.__refresh()
        j = self.__rng[i]
        if isinstance(j, range):
            assert type(i) is slice
            rng = j
            return tuple(map(self.__seq.__getitem__, rng))

            ls = self.__seq
            return tuple(ls[i] for i in rng)
        else:
            assert type(i) is not slice
            assert type(j) is int
            #bug: return self.__seq[i]
            return self.__seq[j]


    def __repr__(self):
        return repr_helper(self, self.__seq, self.__k)



    def __len__(self):
        return len(self.__seq)

    def __iter__(self):
        self.__refresh()
        return map(self.__seq.__getitem__, self.__rng)
    def __reversed__(self):
        self.__refresh()
        return map(self.__seq.__getitem__, reversed(self.__rng))
















'''
Sequence.register(int)
Sequence.register(range)
assert not isinstance(int, Sequence)
assert isinstance(range, Sequence) ??????? why fail????
'''

def t():
    ls = SeqLeftRotateView([1,2,3,4,5,6,7], 89)
    ls2 = SeqLeftRotateView(ls, -3)
    assert repr(ls2) == 'SeqLeftRotateView([1, 2, 3, 4, 5, 6, 7], 86)'

if __name__ == "__main__":
    t()
    import doctest
    doctest.testmod()





