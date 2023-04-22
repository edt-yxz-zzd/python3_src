
class BaseTuple(tuple):
    __slots__ = ()
    def __new__(cls, /, *args):
        sf = super(__class__, cls).__new__(cls, args)
        return sf

from seed.tiny_.BaseTuple import BaseTuple

