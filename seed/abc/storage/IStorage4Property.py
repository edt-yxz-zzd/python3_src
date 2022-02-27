r'''
seed.abc.storage.IStorage4Property
py -m seed.abc.storage.IStorage4Property
py -m nn_ns.app.debug_cmd   seed.abc.storage.IStorage4Property

from seed.abc.storage.IStorage4Property import IStorage4Property, Storage4PropertyMixin, ops4Storage4Property, init_symbol_keyed_property, get_symbol_keyed_property

#'''
__all__ = '''
    IStorage4Property
        Storage4PropertyMixin
    ops4Storage4Property
        init_symbol_keyed_property
        get_symbol_keyed_property
    '''.split()

from seed.abc.abc import abstractmethod, override, ABC
from seed.abc.storage.IOps4Storage4XXX import Ops4Storage4XXX


class IStorage4Property(ABC):
    #see CachedLazyProperty:def ___get_instance_storage4cache___(sf, instance, intend, /):
    #def ___get_storage4cache___(sf, /):
    @abstractmethod
    def ___get_storage4property___(sf, /):
        pass
class Storage4PropertyMixin(IStorage4Property):
    @override
    def ___get_storage4property___(sf, /):
        return sf.__dict__

ops4Storage4Property = Ops4Storage4XXX('___get_storage4property___')
#def init_symbol_keyed_property(sf, obj_as_symbol, value, /):
#def get_symbol_keyed_property(sf, obj_as_symbol, /):
init_symbol_keyed_property = ops4Storage4Property.init_symbol_keyed_property
get_symbol_keyed_property = ops4Storage4Property.get_symbol_keyed_property




