

__all__ = '''
    SeqSliceView

    length_slice_to_range
    range2args
    range2slice
    getitem_from_range
    check_range
    '''.split()

from collections.abc import Sequence
from seed.helper.repr_input import repr_helper
#from .View import SeqView

def length_slice_to_range(length, sl):
    '''UInt -> slice -> range

example:
    >>> sl = slice(None, None, None)
    >>> length_slice_to_range(4, sl)
    range(0, 4)
    >>> sl = slice(None, -1)
    >>> length_slice_to_range(4, sl)
    range(0, 3)
    >>> sl = slice(-1, None, -1)
    >>> length_slice_to_range(4, sl)
    range(3, -1, -1)
'''
    assert type(length) is int
    assert type(sl) is slice
    start, stop, step = sl.indices(length)
    return range(start, stop, step)
def range2args(rng):
    return (rng.start, rng.stop, rng.step)
def check_range(rng):
    '''
negative number in slice is relative position
but number in range is absolute position
    see: slice.indices # see example below

example:
    >>> sl = slice(-1,None, -1)
    >>> sl.indices(4)
    (3, -1, -1)
'''
    if not rng.start >= 0: raise ValueError
    if not (rng.stop >= 0 or rng.step <= rng.stop): raise ValueError
def range2slice(rng):
    check_range(rng)
    start, stop, step = (rng.start, rng.stop, rng.step)
    if stop < 0:
        assert step < 0
        stop = None
    return slice(start, stop, step)
def getitem_from_range(seq, rng):
    '''use range as slice to getitem

example:
    #range <: Sequence
    #>>> isinstance(range, Sequence)
    #True
    >>> getitem_from_range([1,2,3], range(1,3))
    [2, 3]
    >>> getitem_from_range(range(-10,0), range(1,3))
    range(-9, -7)
    >>> getitem_from_range([1,2,3], range(1,-1, -1))
    [2, 1]
    >>> getitem_from_range(range(-10,-2), range(3,-1, -1))
    range(-7, -11, -1)

    >>> getitem_from_range(range(1, 6, 2), range(2, -1, -1))
    range(5, -1, -2)
'''
    #assert isinstance(seq, (Sequence, range))
    #L = len(seq)
    # bug: return seq[rng.start : rng.stop : rng.step]
    #   when stop < 0 and step < 0

    #check_range(rng)
    return seq[range2slice(rng)]


class SeqSliceView(Sequence):
    '''[a] -> (range|None|slice) -> [a]



see: check_range
    indices in range must be non-negative
        rng.start >= 0
        rng.stop >= 0 or rng.step <= rng.stop


example:
    >>> ls = SeqSliceView([1,2,3,4,5,6,7], range(1,6,2))
    >>> ls
    SeqSliceView([1, 2, 3, 4, 5, 6, 7], range(1, 6, 2))
    >>> len(ls)
    3
    >>> list(ls)
    [2, 4, 6]
    >>> list(reversed(ls))
    [6, 4, 2]

    # __getitem__
    >>> ls[1]
    4
    >>> ls[1:]
    SeqSliceView([1, 2, 3, 4, 5, 6, 7], range(3, 7, 2))
    >>> ls[-1::-1]
    SeqSliceView([1, 2, 3, 4, 5, 6, 7], range(5, -1, -2))
    >>> SeqSliceView(ls, slice(-1, None, -1))
    SeqSliceView([1, 2, 3, 4, 5, 6, 7], range(5, -1, -2))

see: SeqTransformView
see: mk_slice
'''
    __slots__ = ('__rng', '__seq')

    def __init__(self, seq, range_or_slice):
        ':: [a] -> range -> [a]'
        if not isinstance(seq, Sequence): raise TypeError

        if range_or_slice is None:
            rng = range(len(seq))
        elif isinstance(range_or_slice, range):
            rng = range_or_slice
        elif isinstance(range_or_slice, slice):
            sl = range_or_slice
            #print(sl)
            rng = length_slice_to_range(len(seq), sl)
            #print(rng)
        else:
            raise TypeError('range_or_slice must be slice or range')

        if not rng.stop <= len(seq): raise ValueError
        #rng = getitem_from_range(range(len(seq)), rng)
        check_range(rng)

        if isinstance(seq, __class__):
            other = seq
            seq = other.__seq
            #print(other.__rng)
            #print(rng)
            rng = getitem_from_range(other.__rng, rng)
            #print(rng)

        self.__rng = rng
        self.__seq = seq

    def __getitem__(self, i):
        j = self.__rng[i]
        if isinstance(j, range):
            assert type(i) is slice
            return type(self).from_sequence_range(self.__seq, j)
        else:
            assert type(i) is not slice
            assert type(j) is int
            #bug: return self.__seq[i]
            return self.__seq[j]


    def __repr__(self):
        return repr_helper(self, self.__seq, self.__rng)

    @classmethod
    def from_sequence(cls, seq): return cls.from_sequence_range(seq, None)
    @classmethod
    def from_sequence_range(cls, seq, range_or_slice): return cls(seq, range_or_slice)


    def __len__(self):
        return len(self.__rng)

    def __iter__(self):
        return map(self.__seq.__getitem__, self.__rng)
    def __reversed__(self):
        return map(self.__seq.__getitem__, reversed(self.__rng))
















'''
Sequence.register(int)
Sequence.register(range)
assert not isinstance(int, Sequence)
assert isinstance(range, Sequence) ??????? why fail????
'''

def t():
    ls = SeqSliceView([1,2,3,4,5,6,7], range(1,6,2))
    ls2 = SeqSliceView(ls, slice(-1, None, -1))
    assert repr(ls2) == 'SeqSliceView([1, 2, 3, 4, 5, 6, 7], range(5, -1, -2))'

if __name__ == "__main__":
    t()
    import doctest
    doctest.testmod()



