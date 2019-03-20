
__all__ = '''
    IIterNeighboursOf
        IterNeighboursOf__8
        IterNeighboursOf__4
        IterNeighboursOf
    '''.split()
    #iter_neighbours_of__prime
    #iter_neighbours_of_ex

from abc import ABC, abstractmethod

_dx_ls = (-1, 0, +1)
_dxy_ls__8 = tuple((dx, dy)
    for dx in _dx_ls
    for dy in _dx_ls
    if dx or dy
    )


class IIterNeighboursOf(ABC):
    __slots__ = ()

    @abstractmethod
    def iter_dxy_of_neighbours_of(self):
        '-> Iter (dx::int, dy::int)'
    def iter_neighbours_of__prime(self, i, j):
        return ((i+dx, j+dy) for dx, dy in self.iter_dxy_of_neighbours_of())
    def iter_neighbours_of_ex(self, i, j, *, num_rows, num_columns):
        for i, j in self.iter_neighbours_of__prime(i,j):
            if i < 0 or j < 0 or i >= num_rows or j >= num_columns:
                continue
            yield (i, j)
class IterNeighboursOf__8(IIterNeighboursOf):
    __slots__ = ()
    __dxy_ls = _dxy_ls__8
    def iter_dxy_of_neighbours_of(self):
        return iter(self.__dxy_ls)
class IterNeighboursOf__4(IIterNeighboursOf):
    __slots__ = ()
    __dxy_ls = ((+1, 0), (-1, 0), (0, -1), (0, +1))
    def iter_dxy_of_neighbours_of(self):
        return iter(self.__dxy_ls)
class IterNeighboursOf(IIterNeighboursOf):
    def __init__(self, *, case:'8|4'):
        if case not in (4, 8): raise ValueError
        if case == 4:
            self.aIterNeighboursOf = IterNeighboursOf__4()
        elif case == 8:
            self.aIterNeighboursOf = IterNeighboursOf__8()
        else:
            raise logic-error
    def iter_dxy_of_neighbours_of(self):
        return self.aIterNeighboursOf.iter_dxy_of_neighbours_of()



