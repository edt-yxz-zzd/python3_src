

__all__ = '''
    IWrapper
    IWrapperInit
    ISingletonWrapper
    ISingletonWrapperInit
    '''.split()

######################################################
from abc import ABCMeta, abstractmethod, ABC
from collections.abc import Sequence
from .View import MapView, SeqView
from seed.iters.put import put
def attrss_to_attrs_attr2index(attrss):
    attr2index = {}
    attrs = []
    output_index2attrs_to_attrs_attr2index(attrss, attrs, attr2index)
    return tuple(attrs), MapView(attr2index)
def output_attrss_to_attrs_attr2index(attrss, attrs, attr2index):
    # Iterable (Iterable a) -> ([a], Map a int)
    d = attr2index
    for idx, attrs in enumerate(attrs):
        for attr in attrs:
            if attr in d: raise ValueError(f'duplicate attr: {attr!r}')
            d[attr] = idx
            attrs.append(attr)
    pass

def get_num_wrapped_objects(wrapper):
    return type(wrapper).__num_wrapped_objects__()
def get_attr2index(wrapper):
    return type(wrapper).__attr2index__()
def get_wrapped_objs(wrapper):
    return type(wrapper).__wrapped_objs__(wrapper)
def get_wrapped_object(wrapper):
    return type(wrapper).__wrapped_object__(wrapper)
def get_wrapped_attrs(wrapper):
    return type(wrapper).__wrapped_attrs__()

def may_isinstance(obj, may_cls):
    if may_cls is None: return True
    return isinstance(obj, may_cls)
def may_super(may_cls, obj):
    # may_cls :: {None} | type
    if may_cls is None: return obj
    return super(may_cls, obj)
def may_supers(may_clss, objs):
    # may_clss :: Iterable ({None} | type)
    may_clss = tuple(may_clss)
    objs = tuple(objs)
    if len(objs) != len(may_clss): raise TypeError
    if not all(may_isinstance(obj, may_cls)
                for obj, may_cls in zip(objs, may_clss)):
        raise TypeError
    return tuple(map(may_super, may_clss, objs))


class IWrapper(ABC):
    # like super, forward mehtods
    @classmethod
    @abstractmethod
    # return a [str]
    def __wrapped_attrs__(cls): pass
    @classmethod
    @abstractmethod
    # return a dict<str, int>
    #   value <- [0..__num_wrapped_objects__-1]
    def __attr2index__(cls): pass
    @classmethod
    @abstractmethod
    # return a uint
    def __num_wrapped_objects__(cls): pass
    @classmethod
    @abstractmethod
    def from_iterable(cls, objs):pass
    @abstractmethod
    def __wrapped_objs__(self):pass

    def __getattribute__(self, attr):
        i = get_attr2index(self).get(attr)
        if i is None: raise AttributeError(attr)
        obj = get_wrapped_objs(self)[i]
        return getattr(obj, attr)

class IWrapperInit(IWrapper):
    @classmethod
    def from_iterable(cls, objs, with_self=False, may_cls=None):
        return cls(objs)
    def __init__(self, objs, with_self=False, may_cls=None):
        # Wrapper(may_supers(may_clss, objs))
        if with_self:
            objs = put(may_super(may_cls, self), objs)
        self.__objs = objs = tuple(objs)
        if len(objs) != get_num_wrapped_objects(self): raise TypeError
    def __wrapped_objs__(self):
        return object.__getattribute__(self, '__objs')


class ISingletonWrapper(IWrapper):
    @classmethod
    @abstractmethod
    def from_object(cls, obj):pass
    @abstractmethod
    def __wrapped_object__(self):pass

    '''
    @classmethod
    def __attr2index__(cls):
        # to be overrided
        return dict.fromkeys(cls.__wrapped_attrs__(), 0)
    '''

    @classmethod
    def from_iterable(cls, objs):
        [obj] = objs
        return cls.from_object(obj)
    def __wrapped_objs__(self):
        return (get_wrapped_object(self),)
    @classmethod
    def __num_wrapped_objects__(cls): return 1
    def __getattr__(self, attr):
        if attr not in get_wrapped_attrs(self): raise AttributeError(attr)
        obj = get_wrapped_object(self)
        return getattr(obj, attr)


class ISingletonWrapperInit(ISingletonWrapper):
    def __init__(self, obj):
        # no super().__init__
        self.__obj = obj
    @classmethod
    def from_object(cls, obj): return cls(obj)
    def __wrapped_object__(self):
        return object.__getattribute__(self, '__obj')


def attrs_str_to_attrs_attr2index(attrs_str):
    return attrs_to_attrs_attr2index(attrs_str.split())
def attrs_strs_to_attrs_attr2index_num_objs(*attrs_strs):
    return attrss_to_attrs_attr2index_num_objs(map(str.split, attrs_strs))
def attrs_to_attrs_attr2index(attrs):
    return attrss_to_attrs_attr2index([attrs])
def attrss_to_attrs_attr2index_num_objs(attrss):
    attrss = tuple(attrss)
    attrs, attr2index = attrss_to_attrs_attr2index(attrss)
    return attrs, attr2index, len(attrss)

'''
class _FrozenSeq(IWrapperInit, Sequence):
    __attrs, __attr2index, __num_objs = \
        attrs_strs_to_attrs_attr2index_num_objs(
            '__getitem__'
            , '__len__ __contains__  __iter__  __reversed__  index  count')
    def __init__(self, seq):
        super().__init__([seq], with_self=True)
    @classmethod
    def __wrapped_attrs__(cls):
        return cls.__attrs
    @classmethod
    def __attr2index__(cls):
        return cls.__attr2index
    @classmethod
    def __num_wrapped_objects__(cls):
        return cls.__num_objs

    def __getitem__(self, i):
        r = get_wrapped_object(self)[i]
        t = type(i)
        if t is slice or isinstance(i, Sequence):
            if isinstance(r, Sequence):
                return type(self).from_object(r)
        return r
'''
######################################################





