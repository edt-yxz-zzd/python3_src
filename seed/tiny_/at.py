#vivi fst, snd
#from seed.tiny_.at import at
__all__ = '''
    at
    '''.split()

class _At:
    def __new__(cls, /):
        try:
            return at
        except NameError:
            return super().__new__(cls)
    def __getitem__(sf, k, /):
        return At(k)
    def __call__(sf, k, /):
        return At(k)
    def __repr__(sf, /):
        return f'at'
class At:
    def __init__(sf, i, /):
        sf.__i = i
    def __call__(sf, x, /):
        return x[sf.__i]
    def __repr__(sf, /):
        return f'At({sf.__i!r})'
at = _At()
assert at is _At()
assert at[1]('ab') == 'b'
assert at(1)('ab') == 'b'
assert {at}
assert {at[0]}

from seed.tiny_.at import at
