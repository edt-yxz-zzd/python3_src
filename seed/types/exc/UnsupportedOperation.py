#__all__:goto
r'''[[[
e ../../python3_src/seed/types/exc/UnsupportedOperation.py


seed.types.exc.UnsupportedOperation
py -m nn_ns.app.debug_cmd   seed.types.exc.UnsupportedOperation -x
py -m nn_ns.app.doctest_cmd seed.types.exc.UnsupportedOperation:__doc__ -ht
py_adhoc_call   seed.types.exc.UnsupportedOperation   @f
from seed.types.exc.UnsupportedOperation import *

>>> class X:
...     __bool__ = Attr4UnsupportedOperation()
>>> X.__bool__
Traceback (most recent call last):
    ...
seed.types.exc.UnsupportedOperation.UnsupportedOperation: UnsupportedOperation:'__bool__'
>>> X().__bool__
Traceback (most recent call last):
    ...
seed.types.exc.UnsupportedOperation.UnsupportedOperation: UnsupportedOperation:'__bool__'
>>> bool(X())
Traceback (most recent call last):
    ...
seed.types.exc.UnsupportedOperation.UnsupportedOperation: UnsupportedOperation:'__bool__'
>>> hasattr(X, '__bool__')
False
>>> hasattr(X(), '__bool__')
False

#]]]'''
__all__ = r'''
UnsupportedOperation
Attr4UnsupportedOperation
'''.split()#'''
__all__

from io import UnsupportedOperation as __
from seed.tiny_.check import check_smay_pseudo_identifier, check_pseudo_identifier
from seed.abc.IDescriptor import INonDataDescriptor
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots


class UnsupportedOperation(Exception):pass
class UnsupportedOperation(AttributeError):pass
class Attr4UnsupportedOperation(INonDataDescriptor, ABC__no_slots):
    def __init__(sf, smay_nm='', /):
        check_smay_pseudo_identifier(smay_nm)
        sf._smay_nm = smay_nm

    @override
    def __get__(sf, may_instance, may_owner=None, /):
        err_msg = f'UnsupportedOperation:{sf._smay_nm!r}'
        raise UnsupportedOperation(err_msg)
        raise AttributeError(err_msg)
    @override
    def __set_name__(sf, owner, name, /):
        check_pseudo_identifier(name)
        if not sf._smay_nm:
            sf._smay_nm = name
    @property
    @override
    def __isabstractmethod__(sf, /):
        'play with @abc.abstractmethod'
        return False
Attr4UnsupportedOperation()



__all__
from seed.types.exc.UnsupportedOperation import UnsupportedOperation
from seed.types.exc.UnsupportedOperation import Attr4UnsupportedOperation
from seed.types.exc.UnsupportedOperation import *

