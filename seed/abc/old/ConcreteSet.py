
from collections.abc import Set

class ConcreteSet(Set):
    # should contains objects
    #   not abstract set
    #   non-concrete set example:
    #      in regualar expression: [^x]
    #         we may use a set ComplementSet({x}) to represent universal_set - {x}
    #      in FSM: {[a..b]:state}
    #         CompactOrderedMap
    # the most import method is "get_element", which indicates "concrete"

    # from Set:
    """A set is a finite, iterable container.

    This class provides concrete generic implementations of all
    methods except for __contains__, __iter__ and __len__.

    To override the comparisons (presumably for speed, as the
    semantics are fixed), all you have to do is redefine __le__ and
    then the other operations will automatically follow suit.
    """

    def left_biased_union(self, other):
        return self._from_iterable(chain(self, (x for x in other if x not in self)))
    def right_biased_union(self, other) :
        return self._from_iterable(chain(other, (x for x in self if x not in other)))
    def left_biased_intersection(self, other):
        return self._from_iterable(x for x in self if x in other)
        if len(other) < len(self):
            small, big = other, self
        else:
            small, big = self, other
        return self._from_iterable(self.get_element(x) for x in small if x in big)
    def right_biased_intersection(self, other):
        return self._from_iterable(x for x in other if x in self)
        if len(other) < len(self):
            small, big = other, self
        else:
            small, big = self, other
        return self._from_iterable(other.get_element(x) for x in small if x in big)
    
    
    def get_element(self, e):
        assert e in self
        for x in self:
            if x == e:
                return x
        raise KeyError(e)
    



