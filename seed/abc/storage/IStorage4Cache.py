r'''
seed.abc.storage.IStorage4Cache
py -m seed.abc.storage.IStorage4Cache
py -m nn_ns.app.debug_cmd   seed.abc.storage.IStorage4Cache

from seed.abc.storage.IStorage4Cache import IStorage4Cache, Storage4CacheMixin, ops4Storage4Cache, init_symbol_keyed_cached_property, get_symbol_keyed_cached_property

#'''
__all__ = '''
    IStorage4Cache
        Storage4CacheMixin
    ops4Storage4Cache
        init_symbol_keyed_cached_property
        get_symbol_keyed_cached_property
    '''.split()

from seed.abc.abc import abstractmethod, override, ABC
from seed.abc.storage.IOps4Storage4XXX import Ops4Storage4XXX





class IStorage4Cache(ABC):
    @abstractmethod
    def ___get_storage4cache___(sf, /):
        pass
class Storage4CacheMixin(IStorage4Cache):
    @override
    def ___get_storage4cache___(sf, /):
        return sf.__dict__


ops4Storage4Cache = Ops4Storage4XXX('___get_storage4cache___')
init_symbol_keyed_cached_property = ops4Storage4Cache.init_symbol_keyed_property
get_symbol_keyed_cached_property = ops4Storage4Cache.get_symbol_keyed_property



