
'''
like slice
'''

__all__ = ['Indices']


import collections
import itertools
IndicesBase = collections.namedtuple(
    'IndicesBase', 'length start step'.split())
class Indices(IndicesBase):
    __slots__ = ()
    def __new__(cls, length, start = 0, step = 1):
        '''represent a slice; immutable

---- begin :      end          : step
old: start : start+length*step : step
new:   0   :    length         :  1

example:
    >>> Indices(5)
    Indices(5, 0, 1)
    >>> Indices(5, 20)
    Indices(5, 20, 1)
    >>> Indices(5, 8, -2)
    Indices(5, 8, -2)
    >>> _.old_end()
    -2
    >>> Indices(0, -2, -2)
    Indices(0, -2, -2)


    >>> Indices(-1)
    Traceback (most recent call last):
        ...
    ValueError: length < 0
    >>> Indices(5, 20, 0)
    Traceback (most recent call last):
        ...
    ValueError: step == 0
    >>> Indices(5, -1)
    Traceback (most recent call last):
        ...
    ValueError: start < 0 < step
    >>> Indices(0, -3, -2)
    Traceback (most recent call last):
        ...
    ValueError: start < step < 0
    >>> Indices(5, 7, -2)
    Traceback (most recent call last):
        ...
    ValueError: end < step < 0

'''
        if not all(map(isinstance,
                       [length, start, step],
                       itertools.repeat(int))
                   ):
            raise ValueError('length start step: not all int')

        if length < 0:
            raise ValueError('length < 0')
        if step == 0:
            raise ValueError('step == 0')
        if start < 0 < step:
            raise ValueError('start < 0 < step')
        if start < step < 0:
            raise ValueError('start < step < 0')

        self = super(Indices, cls).__new__(cls, length, start, step)
        if self.old_end() < step < 0:
            raise ValueError('end < step < 0')
        return self

    def __get_args(self):
        return self.__getnewargs__()
    def __repr__(self):
        return '{}{}'.format(type(self).__name__, self.__get_args())




    def to_old_range(self):
        return range(self.old_begin(), self.old_end(), self.old_step())
    def to_new_range(self):
        return range(self.length)




    # index

    def to_old_index(self, new_idx):
        return self.start + new_idx * self.step

    def to_new_index(self, old_idx):
        new_idx, zero = divmod(old_idx - self.start, self.step)
        if zero != 0:
            raise ValueError('not old_idx')
        return new_idx

    def old_begin(self):
        return self.to_old_index(self.new_begin())
    def old_end(self):
        return self.to_old_index(self.new_end())
    def old_step(self):
        return self.step

    def new_begin(self):
        return 0
    def new_end(self):
        return self.length
    def new_step(self):
        return 1



    # slice
    def to_slice(self):
        '''covert to slice

example:
    >>> Indices(4).to_slice()
    slice(0, 4, 1)
    >>> Indices(4, 2, 3).to_slice()
    slice(2, 14, 3)
    >>> Indices(4, 7, -1).to_slice()
    slice(7, 3, -1)
'''
        return slice(self.old_begin(), self.old_end(), self.old_step())

    def slice2indices(self, slice):
        return self.from_slice(self.length, slice)
    @staticmethod
    def from_slice(length, slice):
        return Indices.from_indices_of_slice(slice.indices(length))
    @staticmethod
    def from_indices_of_slice(indices_of_slice):
        '''indices_of_slice is output of slice.indices(...)'''
        (start, stop, stride) = indices_of_slice
        assert stride

        total = stop - start
        step = stride # may < 0
        if stride < 0:
            total = -total
            stride = -stride

        if total < 0:
            total = 0

        assert total >= 0
        assert stride > 0
        length = (total + stride-1) // stride
        indices = Indices(length, start, step)
        return indices


    def try_to_make_slice_from(self, sth):
        if isinstance(sth, slice):
            pass
        elif isinstance(sth, Indices):
            sth = sth.to_slice()
        else:
            sth = None # unknown
        return sth
    def raise_or_make_slice_from(self, sth, err = ''):
        r = self.try_to_make_slice_from(sth)
        if r == None:
            raise NotImplementedError(err)
        return r
    def __mul__(self, indices_or_slice):
        '''to merge slices
seq[(indices1 * slice2 * slice3).to_slice()]
== seq[slice1][slice2][slice3]
where indices1 = Indices.from_slice(len(seq), slice1)

example:
    >>> Indices(5) * slice(None, None, -2)
    Indices(3, 4, -2)
    >>> _ * slice(0)
    Indices(0, 4, -2)
    >>> _ * slice(2, 4, -2)
    Indices(0, 6, 4)
    >>> slice(2, 4, -2).indices(0)
    (-1, -1, -2)


    >>> Indices(5) * Indices(5)
    Indices(5, 0, 1)
    >>> _ * Indices(6)
    Indices(5, 0, 1)
    >>> _ * Indices(2)
    Indices(2, 0, 1)


'''
        # to_slice
        other = self.raise_or_make_slice_from(indices_or_slice)

        assert isinstance(other, slice)
        other = self.slice2indices(other) # now other in rng [0,len)
        old_step = other.old_step() * self.old_step()
        old_begin = self.to_old_index(other.old_begin())
        length = other.length

        return Indices(length, old_begin, old_step)
    def __imul__(self, other):
        return self * other


    def _getitem_(self, i):
        if isinstance(i, int):
            if i < 0:
                i += self.length
            v = self.get(i)
            if v == None:
                raise IndexError('index out of range')
            return v

        # i is sth like slice
        return self * i

    def _iter_(self):
        return self.to_old_range()

    def get(self, i, default = None):
        if 0 <= i < self.length:
            return self.to_old_index(i)
        else:
            return default








    # but I'm a tuple !!!
    # can I define a new len???
##    def __len__(self):
##        return self.length


    # since namedtuple is iterable
##    def __iter__(self):
##        return self.to_old_range()
##
##    def __getitem__(self, i):
##        return self._getitem_(i)

    # since iter(self) not return keys()
##    def items(self):
##        return enumerate(self)
##    def keys(self):
##        return self.to_new_range()
##    def values(self):
##        return self.to_old_range()

def test_Indices():
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()





