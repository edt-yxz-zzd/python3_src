r'''
seed.helper.unique_immutable_value
see:
    seed.abc.eq_by_id.AddrAsHash
    seed.abc.eq_by_id.AddrAsHashWrapper
    seed.helper.reduce_number_of_objects_with_same_value


py -m seed.helper.unique_immutable_value
py -m nn_ns.app.debug_cmd   seed.helper.unique_immutable_value


from seed.helper.unique_immutable_value import UniqueWrapper4bytes, UniqueWrapper4str, UniqueWrapper4int, UniqueWrapper4tuple, UniqueWrapper4frozenset, UniqueWrapper4FrozenDict

from seed.helper.unique_immutable_value import the_unique_wrapper4null_tuple, the_unique_wrapper4null_frozenset, the_unique_wrapper4null_FrozenDict



unified
unification
    e ../../python3_src/seed/abc/storage/IOps4Storage4XXX.py
    e ../../python3_src/seed/abc/storage/IStorage4Property.py
    e ../../python3_src/seed/abc/storage/IStorage4Cache.py
    e ../../python3_src/seed/abc/wrapper/IWrapper.py

数据唯一化
    唯一化 的 优点:
        * 减少存储空间
        * 减少运算量
            * immutable_value 可能含有 cache
                * graph
                    .is_planar
                    .maybe_a_planar_embedding
                * hash
                * lambda_expr
                    .free_vars
                    .free_var2lambda_expr2lambda_expr
                        #替换后的值
            * unique_immutable_value 的 eq/hash 可以使用 AddrAsHash/EqById

    * reduce_number_of_objects_with_same_value
        只针对 底层/单层 数据
        使用AddrAsHashWrapper<T>，令数据可被弱引用
        WeakKeyDictionary<AddrAsHashWrapper<T>,T> 不行
        WeakValueDictionary<T,AddrAsHashWrapper<T> > 行
        但:
            * 用户必须 保存 AddrAsHashWrapper<T> 而非 T，使用起来 有麻烦
            * 多层次的数据唯一化 容易错漏，使用也麻烦
    * unique_immutable_value
        针对多层数据，但无法保持数据原貌
        使用AddrAsHash
        用户使用 newT 而非 T
        T -> newT(AddrAsHash, T)
            unique_immutable_value inside newT.__new__()
        WeakValueDictionary<ValueHashWrapper<newT>,newT>
    fail:
        class UniqueTuple(UniqueBase, tuple):
            weakref.ref(sf)
            TypeError: cannot create weak reference to 'UniqueTuple' object
        class UniqueTuple(UniqueBase, tuple):
            __slots__ = ('__dict__',)
            TypeError: nonempty __slots__ not supported for subtype of 'tuple'
    ==>>
        T -> newT(AddrAsHash, Wrapper<T>, IConcept<T>)
        WeakValueDictionary<T, newT>
            key=value.underlying_obj



#>>> UniqueTuple([2, 4, 8, 16])
>>> UniqueWrapper4tuple.get_or_mk([2, 4, 8, 16])
UniqueWrapper4tuple._gk([2, 4, 8, 16])
>>> UniqueWrapper4tuple.get_or_mk()
UniqueWrapper4tuple._gk()


>>> UniqueWrapper4tuple.mk_new([2, 4, 8, 16])
UniqueWrapper4tuple._gk([2, 4, 8, 16])
>>> UniqueWrapper4tuple.mk_new()
Traceback (most recent call last):
    ...
LookupError: mk_new():already-exists: UniqueWrapper4tuple._gk() <--- UniqueWrapper4tuple.mk_new()

>>> UniqueWrapper4tuple.from_wrapped_obj_ex((2, 4, 8, 16)) #since the tmp var "_"
(False, UniqueWrapper4tuple._gk([2, 4, 8, 16]))
>>> _
(False, UniqueWrapper4tuple._gk([2, 4, 8, 16]))
>>> del _; UniqueWrapper4tuple.from_wrapped_obj_ex((2, 4, 8, 16))
Traceback (most recent call last):
    ...
NameError: name '_' is not defined
>>> UniqueWrapper4tuple.from_wrapped_obj_ex(()) #the_unique_wrapper4null_tuple
(False, UniqueWrapper4tuple._gk())
>>> UniqueWrapper4tuple.from_wrapped_obj_ex((2, 4, 8, 16))
(True, UniqueWrapper4tuple._gk([2, 4, 8, 16]))



>>> UniqueWrapper4tuple.get_or_mk() is  UniqueWrapper4tuple.from_wrapped_obj_ex(())[1]
True
>>> UniqueWrapper4tuple.get_or_mk([2, 4, 8, 16]) is  UniqueWrapper4tuple.from_wrapped_obj_ex((2, 4, 8, 16))[1]
True


>>> UniqueWrapper4tuple.get_or_mk() is  eval(repr(UniqueWrapper4tuple.get_or_mk()))
True
>>> UniqueWrapper4tuple.get_or_mk([2, 4, 8, 16]) is  eval(repr(UniqueWrapper4tuple.get_or_mk([2, 4, 8, 16])))
True

>>> x = UniqueWrapper4frozenset.get_or_mk([2, 4, 8, 16])
>>> type(x).__hash__(x) == id(x)
True

#>>> hash(x) == id(x)
False
>>> x == frozenset([2, 4, 8, 16])
False
>>> UniqueWrapper4tuple.from_wrapped_obj_ex((2, 4, 8, 16)) == (2, 4, 8, 16)
False
>>> UniqueWrapper4tuple.from_wrapped_obj_ex(()) == ()
False



#'''



__all__ = '''
    IWrapperBase4UniqueHashable
        IUniqueWrapper4ByteString
            UniqueWrapper4bytes
            UniqueWrapper4str
        UniqueWrapper4int
        UniqueWrapper4tuple
            the_unique_wrapper4null_tuple
        UniqueWrapper4frozenset
            the_unique_wrapper4null_frozenset
        UniqueWrapper4FrozenDict
            the_unique_wrapper4null_FrozenDict
    IUniquePoint
        UniquePoint4unique_key
        UniquePoint4value_key

    '''.split()



from seed.abc.abc import abstractmethod, override, ABC
from seed.abc.eq_by_id.AddrAsHash import AddrAsHash as EqById
from seed.helper.repr_input import repr_helper, repr_helper__str
from seed.types.FrozenDict import FrozenDict, empty_FrozenDict
from seed.tiny import null_frozenset, null_tuple, null_str, null_bytes, null_int, check_type_is, check_type_le
from seed.helper.check.checkers import checker4pseudo_identifier #check_pair, check_type_is, check_seq, 
from seed.mapping_tools.fdefault import mapping_set__new_or_pass__cased_, mapping_get__tmay__get_Nothing

from seed.abc.wrapper.IWrapper import init_the_wrapped_obj, get_the_wrapped_obj, MkWrapperMixin, SequenceWrapperMixin, ByteStringWrapperMixin, MappingWrapperMixin, ISetWrapperMixin
import weakref



#from seed.tiny import MapView
#from seed.abc.storage.IStorage4Cache import IStorage4Cache, Storage4CacheMixin, ops4Storage4Cache, init_symbol_keyed_cached_property, get_symbol_keyed_cached_property
#from seed.abc.storage.IStorage4Property import IStorage4Property, Storage4PropertyMixin, ops4Storage4Property, init_symbol_keyed_property, get_symbol_keyed_property

#from seed.abc.abc import abstractmethod, override, ABC
#from collections.abc import Sequence, Mapping, Set, ByteString
#from seed.abc.wrapper.IWrapper import IWrapper, init_the_wrapped_obj, get_the_wrapped_obj, WrapperMixin, _IMkWrapper, _MkWrapperMixin, IMkWrapper, MkWrapperMixin, ISequenceWrapper, SequenceWrapperMixin, IByteStringWrapper, ByteStringWrapperMixin, IMappingWrapper, MappingWrapperMixin, ISetWrapper, ISetWrapperMixin










__type4the_wrapped_value_hash_obj2type4the_unique_wrapper = {}
__type_pair2unique_point = {}
def _type_pair2unique_point(type4the_wrapped_obj, type4the_unique_wrapper, /):
    #why not export? should be {(type4the_wrapped_obj, type4the_unique_wrapper):unique_point}
    if __type4the_wrapped_value_hash_obj2type4the_unique_wrapper.get(type4the_wrapped_obj) not in [None, type4the_unique_wrapper]: raise TypeError('type4the_wrapped_value_hash_obj should use unique unique_point, ie. wrapped by unique type4the_unique_wrapper')
    if issubclass(type4the_wrapped_obj, EqById):
        _UniquePoint = UniquePoint4unique_key
    else:
        _UniquePoint = UniquePoint4value_key
        type4the_wrapped_value_hash_obj = type4the_wrapped_obj
        if __type4the_wrapped_value_hash_obj2type4the_unique_wrapper.setdefault(type4the_wrapped_value_hash_obj, type4the_unique_wrapper) is not type4the_unique_wrapper: raise logic-err

    key = T = type4the_wrapped_obj, type4the_unique_wrapper
    mapping = __type_pair2unique_point
    (is_old_value, unique_point) = mapping_set__new_or_pass__cased_(mapping, key, 0, _UniquePoint, try_vs_Nothing_vs_in=None)
    assert type(unique_point) is _UniquePoint
    return unique_point
class IUniquePoint(ABC):
    r'''
    UniquePoint4value_key vs UniquePoint4unique_key:
        UniquePoint4value_key<value_key, _>
            each concrete value type should use only one wrapper!!
        UniquePoint4unique_key<unique_key, _>
            eg. Symbol<pkg, qname> = wrapper<UniqueWrapper4tuple<UniqueWrapper4str, UniqueWrapper4str> >
                unique_key is UniqueWrapper4tuple
    #'''
    @abstractmethod
    def the_wrapped_obj2tmay_unique_wrapper(sf, the_wrapped_obj, /):
        'detect id(the_wrapped_obj)'
    @abstractmethod
    def eqv_wrapped_obj2tmay_unique_wrapper(sf, eqv_wrapped_obj, /):
        'mapping.get value(eqv_wrapped_obj)'
    @abstractmethod
    def set_fdefault___eqv_wrapped_obj2unique_wrapper(sf, eqv_wrapped_obj, wrapped_obj2wrapper, /):
        'mapping.set_fdefault value(eqv_wrapped_obj) mk_value_from_key'
class UniquePoint4unique_key(IUniquePoint):
    def __init__(sf, /):
        sf._wrapped_obj2wrapper = weakref.WeakValueDictionary()
        super().__init__()
    @override
    def the_wrapped_obj2tmay_unique_wrapper(sf, the_wrapped_obj, /):
        tmay_unique_wrapper = sf.eqv_wrapped_obj2tmay_unique_wrapper(the_wrapped_obj)
            #eqv_wrapped_obj is the_wrapped_obj
        return tmay_unique_wrapper
    @override
    def eqv_wrapped_obj2tmay_unique_wrapper(sf, eqv_wrapped_obj, /):
        tmay_unique_wrapper = mapping_get__tmay__get_Nothing(sf._wrapped_obj2wrapper, eqv_wrapped_obj)
        return tmay_unique_wrapper
    @override
    def set_fdefault___eqv_wrapped_obj2unique_wrapper(sf, eqv_wrapped_obj, wrapped_obj2wrapper, /):
        #wrapped_obj2wrapper is not cls4wrapper
        #   since be used in cls4wrapper.__new__
        tmay_unique_wrapper = sf.eqv_wrapped_obj2tmay_unique_wrapper(eqv_wrapped_obj)
        if not tmay_unique_wrapper:
            #if not isinstance(eqv_wrapped_obj, EqById): raise TypeError
            check_type_le(EqById, eqv_wrapped_obj)
            unique_wrapper = wrapped_obj2wrapper(eqv_wrapped_obj)
            assert get_the_wrapped_obj(unique_wrapper) is eqv_wrapped_obj

            sf._wrapped_obj2wrapper[eqv_wrapped_obj] = unique_wrapper
            #bug:del unique_wrapper
            #       should move after eval tmay_unique_wrapper
            tmay_unique_wrapper = sf.eqv_wrapped_obj2tmay_unique_wrapper(eqv_wrapped_obj)
            del unique_wrapper #tmay_unique_wrapper hold ref
        if not tmay_unique_wrapper: raise logic-err
        [unique_wrapper] = tmay_unique_wrapper
        return unique_wrapper


class UniquePoint4value_key(IUniquePoint):
    def __init__(sf, /):
        sf._wrapped_obj2wrapper = weakref.WeakValueDictionary()
        sf._wrapped_obj_id2wrapper = weakref.WeakValueDictionary()
        super().__init__()
    @override
    def the_wrapped_obj2tmay_unique_wrapper(sf, the_wrapped_obj, /):
        tmay_unique_wrapper = mapping_get__tmay__get_Nothing(sf._wrapped_obj_id2wrapper, id(the_wrapped_obj))
        return tmay_unique_wrapper
    @override
    def eqv_wrapped_obj2tmay_unique_wrapper(sf, eqv_wrapped_obj, /):
        tmay_unique_wrapper = sf.the_wrapped_obj2tmay_unique_wrapper(eqv_wrapped_obj)
            #eqv_wrapped_obj may be the_wrapped_obj
        if not tmay_unique_wrapper:
            tmay_unique_wrapper = mapping_get__tmay__get_Nothing(sf._wrapped_obj2wrapper, eqv_wrapped_obj)
        return tmay_unique_wrapper
    @override
    def set_fdefault___eqv_wrapped_obj2unique_wrapper(sf, eqv_wrapped_obj, wrapped_obj2wrapper, /):
        #wrapped_obj2wrapper is not cls4wrapper
        #   since be used in cls4wrapper.__new__
        tmay_unique_wrapper = sf.eqv_wrapped_obj2tmay_unique_wrapper(eqv_wrapped_obj)
        if not tmay_unique_wrapper:
            unique_wrapper = wrapped_obj2wrapper(eqv_wrapped_obj)
            assert get_the_wrapped_obj(unique_wrapper) is eqv_wrapped_obj

            sf._wrapped_obj_id2wrapper[id(eqv_wrapped_obj)] = unique_wrapper
            sf._wrapped_obj2wrapper[eqv_wrapped_obj] = unique_wrapper
            #bug:del unique_wrapper
            #       should move after eval tmay_unique_wrapper
            tmay_unique_wrapper = sf.eqv_wrapped_obj2tmay_unique_wrapper(eqv_wrapped_obj)
            del unique_wrapper #tmay_unique_wrapper hold ref
        if not tmay_unique_wrapper: raise logic-err
        [unique_wrapper] = tmay_unique_wrapper
        return unique_wrapper


class IWrapperBase4UniqueHashable(EqById, MkWrapperMixin, ABC):
    #class WrapperBase4UniqueHashable(MkWrapperMixin, IWrapperBase4UniqueHashable):
    @abstractmethod
    class type4the_wrapped_obj:pass
    may_mk_wrapped_obj = None
    #class _symbol4unique_point:pass
    @classmethod
    def from_wrapped_obj_ex(cls, wrapped_obj, /):
        '-> (is_new, sf)'
        #is_new, sf = cls(wrapped_obj)
        #is_new, sf = cls.___new___(wrapped_obj)
        is_new, sf = cls.___new___(cls, wrapped_obj)
        check_type_is(bool, is_new)
        check_type_is(cls, sf)
        return is_new, sf
    @classmethod
    @override
    def from_wrapped_obj(cls, wrapped_obj, /):
        '-> sf'
        is_new, sf = cls.from_wrapped_obj_ex(wrapped_obj)
        return sf

    @classmethod
    def get_or_mk_ex(cls, /, *args, **kwargs):
        '-> (is_new, sf)'
        eqv_wrapped_obj = cls.get_or_mk_eqv_wrapped_obj(*args, **kwargs)
        return cls.from_wrapped_obj_ex(eqv_wrapped_obj)
    @classmethod
    def get_or_mk(cls, /, *args, **kwargs):
        '-> sf'
        is_new, sf = cls.get_or_mk_ex(*args, **kwargs)
        return sf
    @classmethod
    def mk_new(cls, /, *args, **kwargs):
        '-> sf'
        is_new, sf = cls.get_or_mk_ex(*args, **kwargs)
        if not is_new:
            s = repr_helper__str(f'{cls.__name__!s}.mk_new', *args, **kwargs)
            raise LookupError(f'mk_new():already-exists: {sf!r} <--- {s!s}')
        return sf
    @classmethod
    def _gk(cls, /, *args, **kwargs):
        '-> sf   #==get_or_mk#_gk used in __repr__ result, user should use get_or_mk/mk_new instead'
        sf = cls.get_or_mk(*args, **kwargs)
        return sf
    @classmethod
    def get_or_mk_eqv_wrapped_obj(cls, /, *args, **kwargs):
        if not kwargs and len(args)==1 and type(*args) is cls.type4the_wrapped_obj:
            [eqv_wrapped_obj] = args
        else:
            may_mk_wrapped_obj = cls.may_mk_wrapped_obj
            if may_mk_wrapped_obj is not None:
                mk_wrapped_obj = may_mk_wrapped_obj
            else:
                mk_wrapped_obj = cls.type4the_wrapped_obj
                if issubclass(cls.type4the_wrapped_obj, __class__):
                    mk_wrapped_obj = cls.type4the_wrapped_obj.get_or_mk
            mk_wrapped_obj
            eqv_wrapped_obj = mk_wrapped_obj(*args, **kwargs)
        #if type(eqv_wrapped_obj) is not cls.type4the_wrapped_obj: raise TypeError
        check_type_is(cls.type4the_wrapped_obj, eqv_wrapped_obj)
        return eqv_wrapped_obj
    simplify_the_wrapped_obj2args_kwargs4repr = None
    @classmethod
    @abstractmethod
    def simplify_the_wrapped_obj2args_kwargs4repr(cls, the_wrapped_obj, /):
        '-> (args, kwargs)'
    def __repr__(sf, /):
        cls = type(sf)
        the_wrapped_obj = get_the_wrapped_obj(sf)
        if cls.simplify_the_wrapped_obj2args_kwargs4repr is None:
            return repr_helper(sf, the_wrapped_obj)
        else:
            (args, kwargs) = cls.simplify_the_wrapped_obj2args_kwargs4repr(the_wrapped_obj)
            return repr_helper__str(f'{cls.__name__!s}._gk', *args, **kwargs)





    r'''
    #def __new__(cls, /, *the_wrapped_obj_then_args, **kwargs):
    def __new__(cls, /, *tmay_the_wrapped_obj):
        #tmay_the_wrapped_obj = the_wrapped_obj_then_args[:1]
        #args = the_wrapped_obj_then_args[1:]
        if tmay_the_wrapped_obj:
            [the_wrapped_obj] = tmay_the_wrapped_obj
        else:
            the_wrapped_obj = cls.type4the_wrapped_obj()
    #'''
    def __new__(cls, the_wrapped_obj, /):
        ABC.__new__(cls)
            #check whether abstractclass
        if type(the_wrapped_obj) is cls:
            sf = the_wrapped_obj
            return sf
        raise Exception(f'shouldnot call {cls}.__new__(), use .get_or_mk()/.mk_new ##{__class__.__name__}')
    def __init__(_sf, the_wrapped_obj, /):
        if type(the_wrapped_obj) is type(_sf):
            sf = the_wrapped_obj
            if sf is _sf:
                return
        raise Exception(f'shouldnot call {cls}.__init__(), see .get_or_mk_eqv_wrapped_obj()/.get_or_mk()/.mk_new ##{__class__.__name__}')
    #@classmethod
    #   ###
    #   why not classmethod?
    #       since super(__class__, cls).__new__(cls, ...) ==>> __new__ is not classmethod
    #   ###
    #   ### xxx cancel: now ok via .__func__
    #   ###
    #   why not classmethod?
    #    see below __init_subclass__: if cls.___new___ is not __class__.___new___:raise logic-err
    #   ###
    def ___new___(cls, the_wrapped_obj, /):
        #=== .from_wrapped_obj_ex
        ABC.__new__(cls)
            #check whether abstractclass
        if type(the_wrapped_obj) is not cls.type4the_wrapped_obj: raise TypeError(f'type(the_wrapped_obj) is not cls.type4the_wrapped_obj: {type(the_wrapped_obj)} is not {cls.type4the_wrapped_obj}')

        if 1:
            d = cls._unique_point
        else:
            #d = get_symbol_keyed_property(cls, __class__._symbol4unique_point)
            d = cls.__dict__[__class__._symbol4unique_point]

        def wrapped_obj2wrapper(the_wrapped_obj, /):
            #sf = super().__new__(cls, *args, **kwargs)
            _sf = super(__class__, cls).__new__(cls)
            #if type(_sf) is not cls: raise TypeError
            check_type_is(cls, _sf)
            init_the_wrapped_obj(_sf, the_wrapped_obj)
            #super(__class__, _sf).__init__()
            object.__init__(_sf)
            #sf = type(cls).__call__(super(__class__, cls))
            sf = type(cls).__call__(cls, _sf)
            #if type(sf) is not cls: raise TypeError
            check_type_is(cls, sf)
            if sf is not _sf: raise TypeError
            if __debug__:
                try:
                    sf.____xxx = ...
                        #expectError
                except AttributeError:
                    pass
                else:
                    raise logic-err
            return sf

        is_new = not d.eqv_wrapped_obj2tmay_unique_wrapper(the_wrapped_obj)
        if is_new:
            cls.___check_the_wrapped_obj___(the_wrapped_obj)
        sf = d.set_fdefault___eqv_wrapped_obj2unique_wrapper(the_wrapped_obj, wrapped_obj2wrapper)
        #if type(sf) is not cls: raise TypeError
        check_type_is(cls, sf)
        if is_new:
            cls.___check_after_new___(sf)
        return is_new, sf


    def __setattr__(sf, attr, obj, /):
        raise AttributeError(attr)
    @classmethod
    def ___check_the_wrapped_obj___(cls, the_wrapped_obj, /):
        pass
    def ___check_after_new___(sf, /):
        pass


    def __init_subclass__(cls, /,*args, **kwargs):
        if cls.__init__ is not __class__.__init__:raise logic-err
        if cls.__new__ is not __class__.__new__:raise logic-err
        if cls.___new___ is not __class__.___new___:raise logic-err
        #if cls.___new___.__func__ is not __class__.___new___.__func__:raise logic-err

        #d = weakref.WeakValueDictionary()
        #d = UniquePoint4value_key()
        #bug:d = _type_pair2unique_point(cls)
        if cls.type4the_wrapped_obj is not __class__.type4the_wrapped_obj:
            #bug:if cls.type4the_wrapped_obj is not __class__.type4the_wrapped_obj and cls.type4the_wrapped_obj is not super(cls).type4the_wrapped_obj:
            #   since cls is part of key
            #
            d = _type_pair2unique_point(cls.type4the_wrapped_obj, cls)
            if 1:
                cls._unique_point = d
            else:
                #init_symbol_keyed_property(cls, __class__._symbol4unique_point, d)
                cls.__dict__[__class__._symbol4unique_point] = d
                #    TypeError: 'mappingproxy' object does not support item assignment
        else:
            pass
        super(__class__, cls).__init_subclass__(*args, **kwargs)
        #super(__class__, cls).__init_subclass__()

def _t():
    class C(EqById, MkWrapperMixin, ABC):
        @abstractmethod
        def f(sf, /):pass
        def __init_subclass__(cls, /,*args, **kwargs):
            pass
        def __new__(cls, /,*args, **kwargs):
            pass
    C()
    assert issubclass(IWrapperBase4UniqueHashable, ABC)
    assert IWrapperBase4UniqueHashable.__abstractmethods__
    print(IWrapperBase4UniqueHashable.__abstractmethods__)
def _t():
    try:
        IWrapperBase4UniqueHashable(1)
        #IWrapperBase4UniqueHashable(IWrapperBase4UniqueHashable.type4the_wrapped_obj())
    except TypeError as e:
        #print(repr(e))
        assert repr(e) == r'''TypeError("Can't instantiate abstract class IWrapperBase4UniqueHashable with abstract methods simplify_the_wrapped_obj2args_kwargs4repr, type4the_wrapped_obj")'''
    else:
        raise logic-err
_t()

class _IUniqueWrapper__single_arg(IWrapperBase4UniqueHashable):
    @abstractmethod
    class simplified_type4the_wrapped_obj:pass

    @classmethod
    @override
    def simplify_the_wrapped_obj2args_kwargs4repr(cls, the_wrapped_obj, /):
        if the_wrapped_obj:
            arg = cls.simplified_type4the_wrapped_obj(the_wrapped_obj)
            args = (arg,)
        else:
            args = ()
        kwargs = {}
        return args, kwargs

class UniqueWrapper4tuple(_IUniqueWrapper__single_arg, SequenceWrapperMixin):
    #@override
    type4the_wrapped_obj = tuple
    #@override
    simplified_type4the_wrapped_obj = list


UniqueWrapper4tuple.get_or_mk()
UniqueWrapper4tuple.from_wrapped_obj_ex(())
assert UniqueWrapper4tuple.get_or_mk() is  UniqueWrapper4tuple.from_wrapped_obj_ex(())[1]


class IUniqueWrapper4ByteString(IWrapperBase4UniqueHashable, ByteStringWrapperMixin):
    #@override
    simplify_the_wrapped_obj2args_kwargs4repr = None
    pass
class UniqueWrapper4bytes(IUniqueWrapper4ByteString):
    #@override
    type4the_wrapped_obj = bytes
class UniqueWrapper4str(IUniqueWrapper4ByteString):
    #@override
    type4the_wrapped_obj = str
UniqueWrapper4str.get_or_mk()
UniqueWrapper4str.from_wrapped_obj_ex('')
assert UniqueWrapper4str.get_or_mk() is  UniqueWrapper4str.from_wrapped_obj_ex('')[1]
UniqueWrapper4bytes.get_or_mk()
UniqueWrapper4bytes.from_wrapped_obj_ex(b'')
assert UniqueWrapper4bytes.get_or_mk() is  UniqueWrapper4bytes.from_wrapped_obj_ex(b'')[1]
class UniqueWrapper4int(IWrapperBase4UniqueHashable):
    'hash diff with int so...'
    #@override
    simplify_the_wrapped_obj2args_kwargs4repr = None
    #@override
    type4the_wrapped_obj = int
    def __index__(sf, /):
        '__index__ present ==>> integral-numeric-type;    but hash diff with int????'
        return get_the_wrapped_obj(sf)
    def as_integer_ratio(sf, /):
        return (get_the_wrapped_obj(sf), 1)
UniqueWrapper4int.get_or_mk()
UniqueWrapper4int.from_wrapped_obj_ex(0)
assert UniqueWrapper4int.get_or_mk() is  UniqueWrapper4int.from_wrapped_obj_ex(0)[1]


class UniqueWrapper4frozenset(_IUniqueWrapper__single_arg, ISetWrapperMixin):
    #@override
    type4the_wrapped_obj = frozenset
    #@override
    simplified_type4the_wrapped_obj = set

    @classmethod
    @override
    def _from_iterable(cls, xs, /):
        'override Set::_from_iterable'
        return cls.get_or_mk(xs)

UniqueWrapper4frozenset.get_or_mk()
UniqueWrapper4frozenset.from_wrapped_obj_ex(frozenset())
assert UniqueWrapper4frozenset.get_or_mk() is  UniqueWrapper4frozenset.from_wrapped_obj_ex(frozenset())[1]


class UniqueWrapper4FrozenDict(_IUniqueWrapper__single_arg, MappingWrapperMixin):
    #@override
    type4the_wrapped_obj = FrozenDict
    #@override
    simplified_type4the_wrapped_obj = dict


UniqueWrapper4FrozenDict.get_or_mk()
UniqueWrapper4FrozenDict.from_wrapped_obj_ex(FrozenDict())
assert UniqueWrapper4FrozenDict.get_or_mk() is  UniqueWrapper4FrozenDict.from_wrapped_obj_ex(FrozenDict())[1]




the_unique_wrapper4null_FrozenDict = UniqueWrapper4FrozenDict.from_wrapped_obj_ex(empty_FrozenDict)[1]
the_unique_wrapper4null_frozenset = UniqueWrapper4frozenset.from_wrapped_obj_ex(null_frozenset)[1]
the_unique_wrapper4null_tuple = UniqueWrapper4tuple.from_wrapped_obj_ex(null_tuple)[1]
the_unique_wrapper4null_str = UniqueWrapper4str.from_wrapped_obj_ex('')[1]
the_unique_wrapper4null_bytes = UniqueWrapper4bytes.from_wrapped_obj_ex(b'')[1]
the_unique_wrapper4null_int = UniqueWrapper4int.from_wrapped_obj_ex(0)[1]


assert UniqueWrapper4tuple.get_or_mk() is the_unique_wrapper4null_tuple
assert UniqueWrapper4frozenset.get_or_mk() is the_unique_wrapper4null_frozenset
assert UniqueWrapper4FrozenDict.get_or_mk() is the_unique_wrapper4null_FrozenDict

assert get_the_wrapped_obj(UniqueWrapper4tuple.get_or_mk()) is null_tuple
assert get_the_wrapped_obj(UniqueWrapper4frozenset.get_or_mk()) is null_frozenset
assert get_the_wrapped_obj(UniqueWrapper4FrozenDict.get_or_mk()) is empty_FrozenDict




class UniqueWrapper4identifier(IUniqueWrapper4ByteString):
    type4the_wrapped_obj = UniqueWrapper4str
    @classmethod
    def ___check_the_wrapped_obj___(cls, the_wrapped_obj, /):
        assert type(the_wrapped_obj) is cls.type4the_wrapped_obj is UniqueWrapper4str
        unique_wrapper4str = the_unique_wrapper4null_tuple
        s = get_the_wrapped_obj(unique_wrapper4str)
        #check_type_is(str, s)
        checker4pseudo_identifier(s)
        super(__class__, cls).___check_the_wrapped_obj___(the_wrapped_obj)
        pass

UniqueWrapper4identifier.get_or_mk_ex
class IAddrAsHash2ValueTree(AddrAsHash, ABC):
    def ___value_tree_from_AddrAsHash___(sf, env, /):
        '-> value_tree'
class IValueTree2AddrAsHash(ABC):
    def ___value_tree_to_AddrAsHash___(sf, recur, /):
        '-> IAddrAsHash2ValueTree <: AddrAsHash'


class IPlaceholder(IWrapper):
    #placeholder4future_ancestor_recur_data
    @abstractmethod
    def set_once(sf, the_wrapped_obj, /):
class Placeholder(IPlaceholder):
class IFramework4ValueGraphConverter(ABC):
    @abstractmethod
    def try_enter(sf, value_node, /):
        '-> (case, payload) #(None, None) | (True, cached_result) | (False, placeholder) # False=>mk-placeholder=>may raise; None=>enter=>recur...=>exit_with_noncached_result'
    @abstractmethod
    def exit_with_noncached_result(sf, value_node, noncached_result, /):
        'called only after .try_enter() -> (None, None)'
    def recur_convert(sf, local_env, value_node, /):
        sf.try_enter()

class IValueGraphConverter(ABC):
    def convert_value_graph(sf__framework_env, arg4framework, local_env, value_graph, /):
        sf = sf__framework_env
        framework = sf.mk_IFramework4ValueGraphConverter(arg4framework)
        check_type_le(IFramework4ValueGraphConverter, framework)
        ..
        def recur_convert(local_env, value_graph, /):
    @abstractmethod
    def mk_IFramework4ValueGraphConverter(sf, arg4framework, /):
        arg4framework.case__data_recur
class ValueGraphConverter(Mixin4ValueGraphConverter, IValueGraphConverter):
class IMixin4ValueGraphConverter(IValueGraphConverter):
    def mk_Framework4ValueGraphConverter___DAG__nocache(sf, arg4framework, /):
        return Framework4ValueGraphConverter___DAG__nocache()
    def mk_Framework4ValueGraphConverter___DAG__cache(sf, arg4framework, /):
        return Framework4ValueGraphConverter___DAG__cache()
    def mk_Framework4ValueGraphConverter___raise__nocache(sf, arg4framework, /):
        return Framework4ValueGraphConverter___raise__nocache()
    def mk_Framework4ValueGraphConverter___raise__cache(sf, arg4framework, /):
        return Framework4ValueGraphConverter___raise__cache()
    def mk_Framework4ValueGraphConverter___future__nocache(sf, arg4framework, /):
        return Framework4ValueGraphConverter___future__nocache(arg4framework.may_mk_placeholder4future_ancestor_recur_data)
    def mk_Framework4ValueGraphConverter___future__cache(sf, arg4framework, /):
        return Framework4ValueGraphConverter___future__cache(arg4framework.may_mk_placeholder4future_ancestor_recur_data)
    def mk_IFramework4ValueGraphConverter(sf, case__data_recur, arg4framework, /):
        case = arg4framework.case__data_recur
        data_recur__raise_vs_DAG_vs_future
        data_recur__forbid_vs_none_vs_allow
            case:
                FORBID_data_recur__raise
                    False
                NO_data_recur__DAG
                    None
                ALLOW_data_recur__placeholder4future
                    True
        no_recur<==>DAG
        forbid_recur==>>cache__ancestor_value_node_id2node+raise
        allow_recur==>>cache__ancestor_value_node_id2n_ps_pair<node,[placeholder4future_ancestor_recur_data.set_once]>
        setting__cache_result==>>non_tree+cache__value_node_id2n_r_pair<node, result>
        if sf.known__value_graph_is_tree or ((sf.known__value_graph_is_DAG or case.NO_data_recur__DAG) and not setting__cache_result):
            #treat value_graph as tree
            T = sf.mk_Framework4ValueGraphConverter___DAG__nocache
        else:
            if sf.known__value_graph_is_DAG or case.NO_data_recur__DAG:
                #neednot cache-ancestor
                assert setting__cache_result
            T = sf.mk_Framework4ValueGraphConverter___DAG__cache
            else:
                assert not sf.known__value_graph_is_tree
                assert not sf.known__value_graph_is_DAG
                assert not case.NO_data_recur__DAG
                if case.FORBID_data_recur__raise:
                    cache__ancestor_value_node_id2node
                    if setting__cache_result::
                        T = sf.mk_Framework4ValueGraphConverter___raise__cache
                    else:
                        T = sf.mk_Framework4ValueGraphConverter___raise__nocache
                elif case.ALLOW_data_recur__placeholder4future:
                    cache__ancestor_value_node_id2n_ps_pair<node,[placeholder4future_ancestor_recur_data.set_once]>
                    if setting__cache_result::
                        T = sf.mk_Framework4ValueGraphConverter___future__cache
                    else:
                        T = sf.mk_Framework4ValueGraphConverter___future__nocache
                else:
                    raise Exception
        return T(arg4framework)

    def is_DAG
    def is_tree
    def detect_recur
    def setting__cache_result
    def known__value_graph_is_tree
    def known__value_graph_is_DAG
class Framework4ValueGraphConverter___DAG__nocache(IFramework4ValueGraphConverter):
class Framework4ValueGraphConverter___DAG__cache(IFramework4ValueGraphConverter):
class Framework4ValueGraphConverter___raise__nocache(IFramework4ValueGraphConverter):
class Framework4ValueGraphConverter___raise__cache(IFramework4ValueGraphConverter):
class IFramework4ValueGraphConverter___future__(IFramework4ValueGraphConverter):
    @abstractmethod
    def mk_placeholder4future_ancestor_recur_data(sf, /):
class Framework4ValueGraphConverter___future__nocache(IFramework4ValueGraphConverter___future__):
class Framework4ValueGraphConverter___future__cache(IFramework4ValueGraphConverter___future__):
    arg4framework.may_mk_placeholder4future_ancestor_recur_data

_value_tree_type2AddrAsHash
value_tree_to_AddrAsHash
def value_tree_to_AddrAsHash(value_tree, env, /):
  def recur(value_tree, /):
    may_pair = tmp_cache__value_tree_id2pair.get(id(value_tree))
    if may_pair is not None:
        value_tree_, obj4AddrAsHash = may_pair
        assert value_tree_ is value_tree
    else:
        via_default_pass = False
        value_tree_type = type(value_tree)
        may_get_or_mk_AddrAsHash = env.value_tree_type2get_or_mk_AddrAsHash.get(value_tree_type)
        if may_get_or_mk_AddrAsHash is None:
            if issubclass(value_tree_type, IValueTree2AddrAsHash):
                #value_tree may be AddrAsHash too.
                obj4AddrAsHash = value_tree_type.___value_tree_to_AddrAsHash___(value_tree, recur)
                check_type_le(IAddrAsHash2ValueTree, obj4AddrAsHash)
                #check_type_le(AddrAsHash, obj4AddrAsHash)
            elif issubclass(value_tree_type, AddrAsHash):
                if env.default_pass_ok and not issubclass(value_tree_type, IAddrAsHash2ValueTree):
                    obj4AddrAsHash = value_tree
                    via_default_pass = True
                else:
                    obj4AddrAsHash = =wrap(value_tree)
                    check_type_le(IAddrAsHash2ValueTree, obj4AddrAsHash)
        else:
            get_or_mk_AddrAsHash = may_get_or_mk_AddrAsHash
            obj4AddrAsHash = get_or_mk_AddrAsHash(value_tree, recur)
            check_type_le(, obj4AddrAsHash)
        pass
        if not via_default_pass:
            check_type_le(IAddrAsHash2ValueTree, obj4AddrAsHash)
        check_type_le(AddrAsHash, obj4AddrAsHash)
        pair = (value_tree, obj4AddrAsHash)
        tmp_cache__value_tree_id2pair.setdefault(id(value_tree), pair)
    check_type_le(AddrAsHash, obj4AddrAsHash)
    return obj4AddrAsHash
  def main():
    if tmp_cache__value_tree_id2pair: raise logic-err
    obj4AddrAsHash = recur(value_tree)
    tmp_cache__value_tree_id2pair.clear()
    if __debug__:
        value_tree_ = value_tree_from_AddrAsHash(obj4AddrAsHash, env)
        assert value_tree_ == value_tree:
    check_type_le(AddrAsHash, obj4AddrAsHash)
    return obj4AddrAsHash
  if 1:
    #tmp_cache__value_tree_id2pair = env.tmp_cache__value_tree_id2pair
    tmp_cache__value_tree_id2pair = {}
    detect data-recur
        placeholder4future_ancestor_recur_data
            set_data_once tmay_the_wrapped_obj
    return main()
def value_tree_from_AddrAsHash(obj4AddrAsHash, env, /):
    #if not isinstance(obj4AddrAsHash, AddrAsHash): raise TypeError
    check_type_le(AddrAsHash, obj4AddrAsHash)
    env.tmp_cache__obj4AddrAsHash2value_tree
        ...
    subcls4AddrAsHash = type(obj4AddrAsHash)
    may_get_or_mk_value_tree = env.subcls4AddrAsHash2get_or_mk_value_tree.get(subcls4AddrAsHash)
    if may_get_or_mk_value_tree:
    if isinstance(obj4AddrAsHash, IAddrAsHash2ValueTree):
    check_type_le(IAddrAsHash2ValueTree, obj4AddrAsHash)
    cls = type(obj4AddrAsHash)
    value_tree = cls.___value_tree_from_AddrAsHash___(obj4AddrAsHash, env)
    return value_tree




r'''

from seed.abc.eq_by_id.AddrAsHash import AddrAsHash as EqById, value_hash, value_eq
class ValueHashWrapper:
    def __init__(sf, x, /):
        assert isinstance(x, EqById)
        sf.__weakref = weakref.ref(x)
        sf.__hash = value_hash(x)
    def __hash__(sf, /):
        return sf.__hash
    def __eq__(sf, ot, /):
        if type(sf) is not type(ot): return NotImplemented
        x = sf.__weakref()
        y = ot.__weakref()
        #return type(x).___value_eq___(y)
        return value_eq(x, y)


#cls2unique_point = {}
    #{cls<newT>:WeakValueDictionary{ValueHashWrapper<newT>:newT}}
class UniqueBase(EqById):
    def ___init___(sf, /):
        pass
    def __init_subclass__(cls, /,*args, **kwargs):
        if cls.__init__ is not __class__.__init__:raise logic-err
        cls.unique_point = weakref.WeakValueDictionary()
        super().__init_subclass__(*args, **kwargs)
    def __new__(cls, /,*args, **kwargs):
        #bug:sf = super().__new__(*args, **kwargs)
        sf = super().__new__(cls, *args, **kwargs)
        assert type(sf) is cls
        cls.___init___(sf, *args, **kwargs)
        #unique_point = cls2unique_point[cls]
        unique_point = cls.unique_point
        #sf = unique_point.setdefault(ValueHashWrapper(sf), sf)
        #   会不会替换掉key，却保留旧value?
        k = ValueHashWrapper(sf)
        if k not in unique_point:
            unique_point[k] = sf
        else:
            _sf = unique_point[k]
            assert _sf is not sf
            if 0:
                k.__weakref = weakref.ref(sf)
                assert k.__hash == value_hash(sf)
        del k
        assert type(sf) is cls
        return sf
    def __repr__(sf, /):
        s = super().__repr__()
        #return repr_helper(sf, *args, **kwargs)
        cls = type(sf)
        return f'{cls.__name__!s}({s!s})'
    def ___value_hash___(sf, /):
        return super().__hash__()
        raise NotImplementedError
        return id(sf)
    def ___value_eq___(sf, ot, /):
        return super().__eq__(ot)
        raise NotImplementedError
        return sf is ot
class UniqueTuple(UniqueBase, tuple):
    __slots__ = ('__dict__',)
    #unique_point = weakref.WeakValueDictionary()
    #___init___ = tuple.__init__
    def ___init___(sf, /,*args):
        super().___init___()
        print(len(sf))
        print((sf))
        #assert len(sf) == len(args)
    #___value_hash___ = tuple.__hash__
    #___value_eq___ = tuple.__eq__
    pass
#'''


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):


