r'''
seed.abc.wrapper.IStorage4Property
py -m seed.abc.wrapper.IWrapper
py -m nn_ns.app.debug_cmd   seed.abc.wrapper.IWrapper

from seed.abc.wrapper.IWrapper import IWrapper, init_the_wrapped_obj, get_the_wrapped_obj, WrapperMixin, _IMkWrapper, _MkWrapperMixin, IMkWrapper, MkWrapperMixin, ISequenceWrapper, SequenceWrapperMixin, IByteStringWrapper, ByteStringWrapperMixin, IMappingWrapper, MappingWrapperMixin, ISetWrapper, ISetWrapperMixin

#'''
__all__ = '''
    IWrapper
        init_the_wrapped_obj
        get_the_wrapped_obj
        WrapperMixin
    _IMkWrapper
        _MkWrapperMixin
        IMkWrapper
            MkWrapperMixin
            ISetWrapper
                ISetWrapperMixin
        ISequenceWrapper
            SequenceWrapperMixin
        IByteStringWrapper
            ByteStringWrapperMixin
        IMappingWrapper
            MappingWrapperMixin
    '''.split()

from seed.abc.abc import abstractmethod, override, ABC
from seed.abc.storage.IStorage4Property import IStorage4Property, Storage4PropertyMixin, init_symbol_keyed_property, get_symbol_keyed_property
from collections.abc import Sequence, Mapping, Set, ByteString



def init_the_wrapped_obj(sf, the_wrapped_obj, /):
    #assert isinstance(sf, WrapperMixin)
    type(sf).___init_the_wrapped_obj___(sf, the_wrapped_obj)
def get_the_wrapped_obj(sf, /):
    #assert isinstance(sf, WrapperMixin)
    the_wrapped_obj = type(sf).___get_the_wrapped_obj___(sf)
    return the_wrapped_obj
class IWrapper(ABC):
    @abstractmethod
    def ___get_the_wrapped_obj___(sf, /):
        pass
    @abstractmethod
    def ___init_the_wrapped_obj___(sf, the_wrapped_obj, /):
        pass
class WrapperMixin(Storage4PropertyMixin, IWrapper):
    class key4the_wrapped_obj:pass
    @override
    def ___get_the_wrapped_obj___(sf, /):
        the_wrapped_obj = get_symbol_keyed_property(sf, __class__.key4the_wrapped_obj)
        return the_wrapped_obj
    @override
    def ___init_the_wrapped_obj___(sf, the_wrapped_obj, /):
        init_symbol_keyed_property(sf, __class__.key4the_wrapped_obj, the_wrapped_obj)

class _IMkWrapper(IWrapper):
    @abstractmethod
    def _from_wrapped_obj(sf, wrapped_obj, /):
        'not classmethod!!!'
class IMkWrapper(_IMkWrapper):
    @classmethod
    @abstractmethod
    def from_wrapped_obj(cls, wrapped_obj, /):
        #return cls(wrapped_obj)
        pass
    @override
    def _from_wrapped_obj(sf, wrapped_obj, /):
        'not classmethod!!!'
        return type(sf).from_wrapped_obj(wrapped_obj)
class _MkWrapperMixin(WrapperMixin, _IMkWrapper):
    '@abstractmethod __new__'

    @override
    def _from_wrapped_obj(sf, wrapped_obj, /):
        'not classmethod!!!'
        return type(sf)(wrapped_obj)
class MkWrapperMixin(WrapperMixin, IMkWrapper):
    '@abstractmethod __new__'

    @classmethod
    @override
    def from_wrapped_obj(cls, wrapped_obj, /):
        return cls(wrapped_obj)



class ISequenceWrapper(_IMkWrapper, Sequence):
    @override
    def __len__(sf, /):
        return len(get_the_wrapped_obj(sf))
    @override
    def __getitem__(sf, k, /):
        x_or_xs = get_the_wrapped_obj(sf)[k]
        if isinstance(k, slice):
            xs = x_or_xs
            r = type(sf)._from_wrapped_obj(sf, xs)
        else:
            x = x_or_xs
            r = x
        return r
    ##################################
    ##################################
    @override
    def __reversed__(sf, /):
        return reversed(get_the_wrapped_obj(sf))
    @override
    def __iter__(sf, /):
        return iter(get_the_wrapped_obj(sf))
    @override
    def index(sf, /,*args, **kwargs):
        return get_the_wrapped_obj(sf).index(*args, **kwargs)
    ##################################
    ##################################
class SequenceWrapperMixin(_MkWrapperMixin, ISequenceWrapper):pass

SequenceWrapperMixin()
class IByteStringWrapper(ISequenceWrapper, ByteString):pass
class ByteStringWrapperMixin(SequenceWrapperMixin, IByteStringWrapper):
    @override
    def __getitem__(sf, k, /):
        xs = get_the_wrapped_obj(sf)[k]
        r = type(sf)._from_wrapped_obj(sf, xs)
        return r
ByteStringWrapperMixin()

class IMappingWrapper(_IMkWrapper, Mapping):
    @override
    def __len__(sf, /):
        return len(get_the_wrapped_obj(sf))
    @override
    def __iter__(sf, /):
        return iter(get_the_wrapped_obj(sf))
    @override
    def __contains__(sf, k, /):
        return k in get_the_wrapped_obj(sf)
    @override
    def __getitem__(sf, k, /):
        return get_the_wrapped_obj(sf)[k]
class MappingWrapperMixin(_MkWrapperMixin, IMappingWrapper):pass
MappingWrapperMixin()


class ISetWrapper(IMkWrapper, Set):
    'IMkWrapperMixin instead of _IMkWrapperMixin'
    @override
    def __len__(sf, /):
        return len(get_the_wrapped_obj(sf))
    @override
    def __iter__(sf, /):
        return iter(get_the_wrapped_obj(sf))
    @override
    def __contains__(sf, k, /):
        return k in get_the_wrapped_obj(sf)
    ##################################
    ##################################
    @classmethod
    @abstractmethod
    @override
    def _from_iterable(cls, xs, /):
        'override Set::_from_iterable'
        raise NotImplementedError
        return cls.from_wrapped_obj(xs)
        #return cls._from_wrapped_obj(sf, xs)
        return cls._mk(xs)
        return cls(xs)
    @override
    def __ge__(sf, ot, /):
        sf_set = get_the_wrapped_obj(sf)
        if type(ot) is __class__:
            ot_set = get_the_wrapped_obj(ot)
        else:
            ot_set = ot
        return sf_set >= ot_set
    @override
    def __le__(sf, ot, /):
        sf_set = get_the_wrapped_obj(sf)
        if type(ot) is __class__:
            ot_set = get_the_wrapped_obj(ot)
        else:
            ot_set = ot
        return sf_set <= ot_set
    ##################################
    ##################################
class ISetWrapperMixin(MkWrapperMixin, ISetWrapper):
    'MkWrapperMixin instead of _MkWrapperMixin'
if 0:
    ISetWrapperMixin()
        #_from_iterable





