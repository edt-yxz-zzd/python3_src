
__all__ = '''
    unjust

    Nothing
    Just
    is_Maybe
    is_Just
    is_Nothing
'''.split()

'''
not export:
    nothing
    just
    is_maybe
    is_just
    is_nothing
'''

from ..Newtype import Newtype
from ._unjust import unjust

class Maybe(Newtype):
    def __init__(self, iterable):
        super().__init__(tuple(iterable))
        if len(self) > 1:
            raise TypeError('len(maybe) > 1')
        return

    def __repr__(self):
        return 'Nothing' if not self else 'Just({})'.format(unjust(self))
    def __iter__(self):
        return iter(self.unbox())
    def __len__(self):
        return len(self.unbox())
    def __contains__(self, x):
        return x in self.unbox()

    '''
    @staticmethod
    def Nothing():
        return Nothing
    @staticmethod
    def Just(x):
        return Just(x)
    @staticmethod
    def is_Maybe(obj):
        return is_Maybe(obj)
    @staticmethod
    def is_Just(obj):
        return is_Just(obj)
    @staticmethod
    def is_Nothing(obj):
        return is_Nothing(obj)

    def unjust(self):
        [x] = self
        return x
    '''

def is_Maybe(obj):
    return type(obj) is Maybe
def is_Just(obj):
    return is_Maybe(obj) and bool(obj)
def is_Nothing(obj):
    return is_Maybe(obj) and not bool(obj)

Nothing = Maybe([])
def Just(a):
    return Maybe([a])






nothing = Nothing
just = Just

is_maybe = is_Maybe
is_just = is_Just
is_nothing = is_Nothing



assert nothing != ()
assert () != nothing == nothing != just(1) == just(1) != (1,)

