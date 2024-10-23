#__all__:goto
r'''[[[
e ../../python3_src/seed/tiny_/HashedPair.py

seed.tiny_.HashedPair
py -m nn_ns.app.debug_cmd   seed.tiny_.HashedPair -x
py -m nn_ns.app.doctest_cmd seed.tiny_.HashedPair:__doc__ -ht
py_adhoc_call   seed.tiny_.HashedPair   @f
#]]]'''
__all__ = r'''
HashedPair
Solo
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...


#class HashedPair(tuple):
        #return tuple.__new__(cls, [fst, snd])
class HashedPair:
    def __new__(cls, fst, snd, /):
        sf = super(__class__, cls).__new__(cls)
        sf._fst = fst
        sf._snd = snd
        sf._h = None
        return sf
    def __repr__(sf, /):
        return repr_helper(sf, sf._fst, sf._snd)
    __match_args__ = ('fst', 'snd')
    @property
    def fst(sf, /):
        return sf._fst
    @property
    def snd(sf, /):
        return sf._snd
    def __hash__(sf, /):
        if not sf._h is None:
            return sf._h
        sf._h = hash((id(type(sf)), sf._fst, sf._snd))
        return hash(sf)
    def __eq__(sf, ot, /):
        'match hash()'
        return ((sf is ot)
            or (type(sf) is type(ot)
                and (sf._h is None or ot._h is None or sf._h == ot._h)
                and sf._fst == ot._fst
                and sf._snd == ot._snd
                )
            )
        ##if not type(ot) is __class__:
        ##    return NotImplemented
class Solo:
    def __init__(sf, x, /):
        sf._x = x
        sf._h = None
    def __repr__(sf, /):
        return repr_helper(sf, sf._x)
    __match_args__ = ('payload',)
    @property
    def payload(sf, /):
        return sf._x
    def __hash__(sf, /):
        if not sf._h is None:
            return sf._h
        sf._h = hash((id(type(sf)), sf._x))
        return hash(sf)
    def __eq__(sf, ot, /):
        'match hash()'
        return ((sf is ot)
            or (type(sf) is type(ot)
                and (sf._h is None or ot._h is None or sf._h == ot._h)
                and sf._x == ot._x
                )
            )






__all__
from seed.tiny_.HashedPair import HashedPair, Solo
from seed.tiny_.HashedPair import *
