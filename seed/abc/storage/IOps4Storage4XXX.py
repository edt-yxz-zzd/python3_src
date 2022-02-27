r'''
seed.abc.storage.IOps4Storage4XXX
py -m seed.abc.storage.IOps4Storage4XXX
py -m nn_ns.app.debug_cmd   seed.abc.storage.IOps4Storage4XXX

from seed.abc.storage.IOps4Storage4XXX import IOps4Storage4XXX, Ops4Storage4XXX

#'''
__all__ = '''
    IOps4Storage4XXX
    Ops4Storage4XXX
    '''.split()


from seed.abc.abc import abstractmethod, override, ABC
from seed.tiny import MapView
from seed.types.mapping.OpaquePseudoMapping import OpaquePseudoMappingView, MutableOpaquePseudoMappingWrapper__init_new_key_only

#from seed.mapping_tools.fdefault import mapping_set__new_or_raise__return_

class IOps4Storage4XXX(ABC):
    def init_symbol_keyed_property(ops, sf, obj_as_symbol, value, /):
        d = ops._get_storage4xxx_(sf, mutable=True)
        #mapping_set__new_or_raise__return_(mapping, key, -1, value, try_vs_Nothing_vs_in=True, mk_Exception=lambda x:KeyError(x[0]))
        if obj_as_symbol in d: raise KeyError(obj_as_symbol)#AttributeError
        else:
            d[obj_as_symbol] = value
        return
    def get_symbol_keyed_property(ops, sf, obj_as_symbol, /):
        d = ops.get_view_of_storage4xxx(sf)
        return d[obj_as_symbol]#KeyError
    def get_view_of_storage4xxx(ops, sf, /):
        d = ops._get_storage4xxx_(sf, mutable=False)
        return d
        return OpaquePseudoMappingView(d)
        return MapView(d)
    def _get_storage4xxx_(ops, sf, /,*, mutable:bool):
        d = type(ops).___get_storage4xxx___(ops, sf)
        if mutable:
            return MutableOpaquePseudoMappingWrapper__init_new_key_only(d)
        else:
            return OpaquePseudoMappingView(d)
        pass
    @abstractmethod
    def ___get_storage4xxx___(ops, sf, /):
        '_get_storage4xxx_'
        pass
class Ops4Storage4XXX(IOps4Storage4XXX):
    def __init__(sf, ___get_storage4xxx___, /):
        assert type(___get_storage4xxx___) is str
        sf._attr = ___get_storage4xxx___

    @override
    def ___get_storage4xxx___(ops, sf, /):
        #assert isinstance(sf, Storage4PropertyMixin)
        #d = type(sf).___get_storage4property___(sf)

        cls = type(sf)
        if 1:
            get = getattr(cls, ops._attr)
            d = get(sf)
        else:
            try:
                #get = cls.___get_storage4property___
                #get = getattr(cls, ___get_storage4xxx___)
                get = getattr(cls, ops._attr)
            except AttributeError:
                d = object.__getattribute__(sf, '__dict__')
            else:
                d = get(sf)
        #assert isinstance(d, Mapping)
        if 0:
            print(d)
            print(type(d))
        return d
        #return MapView(d)

