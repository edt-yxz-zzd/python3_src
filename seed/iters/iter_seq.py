

__all__ = '''
    iter_seq
    IterSeq
'''.split()

#from .. import identity

identity = lambda x:x
def iter_seq(seq, reversed=False, reversed_in=False):
    return IterSeq(seq, reversed_out=reversed, reversed_in=reversed_in)


class IterSeq_Slices:
    def __init__(self, aIterSeq, slices):
        self.__a = aIterSeq
        self.__s = slices
    def __iter__(self):
        return self.__a.iter(self.__s)
    def __reversed__(self):
        return self.__a.iter(self.__s, True)
class IterSeq:
    '''

IterSeq(seq, reversed_out=True, ...)[...]
    == reversed(IterSeq(seq, reversed_out=False, ...)[...])
IterSeq(seq, reversed_in=True, ...)[...]
    == IterSeq(reversed(seq), reversed_in=False, ...)[...]

IterSeq(seq, True)[::, :-1]
'''
    __slots__ = ('__seq', '__reversed_out', '__reversed_in')
    @property
    def seq(self):
        return self.__seq
    @property
    def reversed_out(self):
        return self.__reversed_out
    @property
    def reversed_in(self):
        return self.__reversed_in
    def __init__(self, seq, reversed_out=False, reversed_in=False):
        self.__seq = seq
        self.__reversed_out = bool(reversed_out)
        self.__reversed_in = bool(reversed_in)
    def __getitem__(self, slices):
        return IterSeq_Slices(self, slices)
    def iter(self, slices, reversed_out=False, reversed_in=False):
        
        'slices :: int | slice | tuple<int|slice>'
        if not isinstance(slices, tuple):
            slices = (slices,)
        'slices :: tuple<int|slice>'
        
        reversed_out = bool(reversed_out)
        reversed_out ^= self.reversed_out
        reversed_in = bool(reversed_in)
        reversed_in ^= self.reversed_in
        
        seq = self.seq
        L = len(seq)
        f = reversed if reversed_out else identity
        if reversed_in:
            i2elem = lambda i: seq[L-1-i] # bug: forgot -1
        else:
            i2elem = lambda i: seq[i]
            
        for sl in f(slices):
            'slices :: tuple<int|slice>'
            if not isinstance(sl, slice):
                i = sl
                yield i2elem(i)
                continue
            
            for i in f(range(*sl.indices(L))):
                yield i2elem(i)
        

assert list(iter_seq(list(range(7)))[2:6:3]) == [2, 5]
assert list(iter_seq(list(range(7)))[2,3]) == [2, 3]
assert list(iter_seq(list(range(7)), True)[2:6:3]) == [5, 2]
assert list(iter_seq(list(range(7)), True)[2,3]) == [3, 2]

##print(list(iter_seq(list(range(7)), reversed_in=True)[2:6:3]))
##print(list(iter_seq(list(reversed(range(7))))[2:6:3]))
assert list(iter_seq(list(range(7)), reversed_in=True)[2:6:3]) == [4, 1]
assert list(iter_seq(list(range(7)), reversed_in=True)[2,3]) == [4, 3]
assert list(iter_seq(list(range(7)), True, True)[2:6:3]) == [1, 4]
assert list(iter_seq(list(range(7)), True, True)[2,3]) == [3, 4]


