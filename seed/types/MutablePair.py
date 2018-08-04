

__all__ = '''
    MutablePair
    '''.split()


class MutablePair:
    '''mutable Pair
'''
    __slots__ = '''
        fst
        snd
        '''.split()
    def __init__(self, fst, snd):
        self.fst = fst
        self.snd = snd
    def __len__(self):
        return 2
    def __iter__(self):
        yield self.fst
        yield self.snd
    def __reversed__(self):
        yield self.snd
        yield self.fst
    def __getitem__(self, idx):
        if idx < 0:
            idx += 2
        if not (0 <= idx < 2): raise IndexError
        return self.fst if not idx else self.snd
    def __setitem__(self, idx, val):
        if idx < 0:
            idx += 2
        if not (0 <= idx < 2): raise IndexError

        if not idx:
            self.fst = val
        else:
            self.snd = val

p = MutablePair(1,2)
assert list(reversed(p)) == [2,1]
assert list(p) == [1,2]
del p


