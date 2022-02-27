#[[[__doc__:begin
r'''
seed.abc.wrapper.IWrapper4Func__using_storage
py -m    seed.abc.wrapper.IWrapper4Func__using_storage
py -m nn_ns.app.debug_cmd   seed.abc.wrapper.IWrapper4Func__using_storage

from seed.abc.wrapper.IWrapper4Func import IWrapper4Func, Wrapper4Func__using_slots, Wrapper4Func__no_slots
from seed.abc.wrapper.IWrapper4Func__using_storage import IWrapper4Func__using_storage, Wrapper4Func__using_storage


#'''
#]]]__doc__:end






__all__ = '''
    IWrapper4Func__using_storage
        Wrapper4Func__using_storage
    '''.split()


from seed.abc.abc__ver1 import abstractmethod, override, ABC
from seed.abc.wrapper.IWrapper4Func import IWrapper4Func


from seed.abc.storage.IStorage4Property import IStorage4Property, Storage4PropertyMixin, ops4Storage4Property, init_symbol_keyed_property, get_symbol_keyed_property
class IWrapper4Func__using_storage(IWrapper4Func, IStorage4Property):
    __slots__ = ()

class Wrapper4Func__using_storage(Storage4Property, IWrapper4Func__using_storage):
    __slots__ = ()
    def __init__(sf, __func__, /):
        if not callable(__func__):raise TypeError
        init_symbol_keyed_property(sf, IWrapper4Func, __func__)
        super(__class__, type(sf)).__init__(sf)
    @override
    def ___get_func___(sf, /):
        '-> callable #__func__'
        return get_symbol_keyed_property(sf, IWrapper4Func)
Wrapper4Func__using_storage(id)

