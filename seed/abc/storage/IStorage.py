e ../../python3_src/seed/types/OpaqueInstanceStorage.py
e ../../python3_src/seed/abc/storage/IStorage.py
e ../../python3_src/seed/types/attr/CachedLazyProperty.py
r'''
id(x)
    3055850592
hash(id(x))
    908366945
3055850592
908366945
bin(3055850592)
bin(908366945)
bin(3055850592-908366945)

seed.abc.storage.IStorage
py -m seed.abc.storage.IStorage
py -m nn_ns.app.debug_cmd   seed.abc.storage.IStorage

from seed.abc.storage.IStorage import ... IStorage4Cache, Storage4CacheMixin, ops4Storage4Cache, init_symbol_keyed_cached_property, get_symbol_keyed_cached_property

#'''
__all__ = '''
    IStorage
        StorageMixin
    ops4Storage
        init_symbol_keyed_property
        get_symbol_keyed_property
    '''.split()

from seed.abc.abc import abstractmethod, override, ABC
from seed.abc.eq_by_id.AddrAsHash import BaseAddrAsHash, AddrAsHash as EqById
#from seed.abc.storage.IOps4Storage4XXX import Ops4Storage4XXX

from seed.types.OpaqueInstanceStorage import OpaqueStorage, get_opaque_storage4instance, IGetOpaqueStorage, WithOpaqueStorage
from seed.types.OpaqueInstanceStorage import Protocol4OpaqueStorage__using_permission_access
read key view?value? diff write key overwrite/del/init...
    sys:
        repr-stable?-clean?
        view-deep/shallow
简繁 对称字
external-starage, attached method...
    lazy readonly property-ex
        exception_vs_lazy_vs_value
    readonly property-ex
        exception_vs_value
    writable property-ex
        exception_vs_value
    lazy readonly attribute
        lazy_vs_value
    readonly attribute
        value
    writable attribute
        value
        ++check0 alter action-case
        ++check0 alter tmay_old_value lazy_tmay_lazy_new_value
        ++check1 alter tmay_old_value tmay_lazy_new_value
        ++check2 alter tmay_old_value tmay_new_value
    unorder+order iter Weakable
key_path:
    who-getset(obj/private/subclass/external/public)
    storage usage (attachment/cache/tmp...)
    instance treat as (level_as_ops)
    property name (symbol)




class KeyWithDescriptor(EqById):
class IOps4InstanceStorage(ABC):
    def get(sf, )
    @abstractmethod
    def ___get_storage4cache___(sf, level_as_ops, section_path, /):
        #level_as_ops:distinguish obj.f vs cls.f, 碰撞 是 必然性的
        #section_path:public/protected/cache, overrideable...
        #cache: (permanent-key, lazy-readonly-property--derived-from-other-lazy~nonlazy-readonly-property) eg. super(cls) 搜索 cls.__dict__, cls.__cache__, super.__dict__(但不含 super.__cache__)
        #external-attachment: eg. graph-dfs coloring using tmp-Weakable-key for each dfs-iter
        pass
    def ___get_storage4 extensional attachment(sf, section, level_as_ops, /):
    split IXxx Xxx IDescriptor/IStorage4Attachment/OpaquePseudoMapping/AddrAsHash...
    add IStorage4Attachment, IStorage4PublicProperty, IStorage4PrivateProperty
      IStorage4Property/IStorage4Cache/IStorage4Attachment using OpaquePseudoMapping
      OpaquePseudoMapping using object.repr to avoid leak info
class IStorage(ABC):
    @abstractmethod
    def ___get_ops4instance_storage___(sf, /):
        '-> IOps4InstanceStorage'
        pass


ops4Storage4Cache = Ops4Storage4XXX('___get_storage4cache___')
init_symbol_keyed_cached_property = ops4Storage4Cache.init_symbol_keyed_property
get_symbol_keyed_cached_property = ops4Storage4Cache.get_symbol_keyed_property



