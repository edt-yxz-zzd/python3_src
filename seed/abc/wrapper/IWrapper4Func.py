#[[[__doc__:begin
r'''
seed.abc.wrapper.IWrapper4Func
py -m    seed.abc.wrapper.IWrapper4Func
py -m nn_ns.app.debug_cmd   seed.abc.wrapper.IWrapper4Func

from seed.abc.wrapper.IWrapper4Func import IWrapper4Func, Wrapper4Func__using_slots, Wrapper4Func__no_slots
from seed.abc.wrapper.IWrapper4Func__using_storage import IWrapper4Func__using_storage, Wrapper4Func__using_storage


#'''
#]]]__doc__:end






__all__ = '''
    IWrapper4Func
        Wrapper4Func__using_slots
        Wrapper4Func__no_slots
    '''.split()


from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots

class IWrapper4Func(ABC):
    __slots__ = ()
    @property
    def __func__(sf, /):
        '-> callable'
        f = type(sf).___get_func___(sf)
        assert callable(f)
        return f
    @abstractmethod
    def ___get_func___(sf, /):
        '-> callable #__func__'
class Wrapper4Func__using_slots(IWrapper4Func):
    __slots__ = ('__func',)
    def __init__(sf, __func__, /):
        if not callable(__func__):raise TypeError
        sf.__func = __func__
        super(__class__, type(sf)).__init__(sf)
    @override
    def ___get_func___(sf, /):
        '-> callable #__func__'
        return sf.__func
class Wrapper4Func__no_slots(IWrapper4Func, ABC__no_slots):
    ###__slots__ = ('__func',)
    ###__slots__ = ('__dict__',)
    #__slots__ = None
    def __init__(sf, __func__, /):
        if not callable(__func__):raise TypeError
        sf.__func = __func__
        super(__class__, type(sf)).__init__(sf)
    @override
    def ___get_func___(sf, /):
        '-> callable #__func__'
        return sf.__func

