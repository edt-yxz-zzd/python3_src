

'''
example:
    >>> GroupBy(key=snd).keyed_groups([(3,2),(0,2),(4,1)])
    [(2, [(3, 2), (0, 2)]), (1, [(4, 1)])]
    >>> GroupBy(key=snd, value=fst).keyed_groups([(3,2),(0,2),(4,1)])
    [(2, [3, 0]), (1, [4])]

    >>> unique_keys([1,1,0,0,2,2,1,1])
    [1, 0, 2, 1]
'''

__all__ = '''
    GroupBy
    unique_keys
    '''.split()

from .echo import echo, echo_ifNone, snd, fst, ifNone
from itertools import repeat, chain, starmap
from operator import __eq__


def unique_keys(iterable, *, key=None):
    # key :: obj -> equal_able
    # unique_keys :: iter<obj> -> [key]
    return GroupBy(key=key).keys(iterable)

class GroupBy:
    def __init__(self, *, key=None, value=None, eq=None):
        # key :: obj -> equal_able
        # value :: obj -> val
        self.key = echo_ifNone(key)
        self.value = echo_ifNone(value)
        self.eq = ifNone(__eq__, eq)

    def __call__(self, __objs):
        return self.keyed_groups(__objs)

    def groups(self, __objs):
        # output: [[val]]
        return list(self.iter_groups(__objs))
    def keys(self, __objs):
        # output: [key]
        return list(self.iter_keys(__objs))

    def iter_groups(self, __objs):
        # output: iter<[val]>
        return map(snd, self.iter_keyed_groups(__objs))
    def iter_keys(self, __objs):
        # output: iter<[key]>
        return map(fst, self.iter_keyed_groups(__objs))

    def keyed_groups(self, __objs):
        # output: [(key, [val])]
        return list(self.iter_keyed_groups(__objs))

    def iter_keyed_groups(self, __objs):
        # output: iter<(key, [val])>
        key = self.key
        value = self.value
        eq = self.eq
        nothing = []

        it = iter(__objs)
        head = next(it, nothing)
        if head is nothing: return
        prev_key = key(head)
        group = [value(head)]

        for obj in it:
            curr_key = key(obj)
            if not eq(curr_key, prev_key):
                yield (prev_key, group)
                prev_key = curr_key
                group = []
            val = value(obj)
            group.append(val)
        else:
            yield (prev_key, group)
        return
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()


