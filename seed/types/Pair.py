

__all__ = '''
    Pair
    '''.split()


from collections import namedtuple
PairBase = namedtuple('PairBase', 'fst snd'.split())
class Pair(PairBase):
    '''immutable Pair
'''
    __slots__ = ()

    '''
    def __init__(self, fst, snd):
        self.fst = fst
        self.snd = snd
        '''


p = Pair(1,2)
assert list(reversed(p)) == [2,1]
assert list(p) == [1,2]
del p


