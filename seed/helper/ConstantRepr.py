#__all__:goto
r'''[[[
e ../../python3_src/seed/helper/ConstantRepr.py
see:
    view ../../python3_src/seed/tiny_/HexReprInt.py
    view ../../python3_src/seed/helper/ConstantRepr.py


seed.helper.ConstantRepr
py -m nn_ns.app.debug_cmd   seed.helper.ConstantRepr -x
py -m nn_ns.app.doctest_cmd seed.helper.ConstantRepr:__doc__ -ff -v

>>> from seed.helper.ConstantRepr import ConstantRepr, repr_as_3dot
>>> repr(repr_as_3dot) == '...'
True
>>> ConstantRepr(hex(0xABCD))
0xabcd



#]]]'''
__all__ = r'''
ConstantRepr
    repr_as_3dot
'''.split()#'''
__all__


from seed.tiny_.check import check_type_is

class ConstantRepr:
    def __init__(sf, s, /):
        check_type_is(str, s)
        sf._s = s
    def __repr__(sf, /):
        return sf._s

repr_as_3dot = ConstantRepr('...')




from seed.helper.ConstantRepr import ConstantRepr, repr_as_3dot
from seed.helper.ConstantRepr import *
