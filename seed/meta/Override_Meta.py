

r'''
see: "E:\my_data\my_record_txt\NOTE\other\subclass multi inheritance.txt"


@override
    when define a method:
        if it exists in bases, then require @override
        else can not use @override

@arbitrary_override_order_method
    forbidden super(...).f; only XXX.f(self, ...) allowed
        except f is arbitrary_override_order_method
@not_implemented_abstract_method
    arbitrary_override_order_method and not_implemented_abstract_method
        can not both present for one method
    not_implemented_abstract_method can override
__using_methods__ = {supercls: method_names}
    if two bases has a same method
        and neither is subclass of other.
        and the method is not arbitrary_override_order_method:
        and any method is not_implemented_abstract_method
        must use:
            *) @override to define a new method
            or *) __using_methods__
    can not using not_implemented_abstract_method
@final_method
    if final_method present, then __using_methods__ should use it to disambiguouse

@forbid_method
    abstractmethod tell what must
    forbid_method say what must not
__not_impleneted_abstract_method_andor_blocks__
    descriptor:
        one of __get__/__set__/__delete__
    data-descriptor:
        one of __set__/__delete__
    non-data-descriptor:
        __get__
        forbid_method __set__/__delete__
    require OR(some base classes)
    # NOTE: normal are AND(some base classes)


property/classmethod/staticmethod
    property override property
    classmethod override classmethod
    should not override staticmethod

    .__isabstractmethod__
    staticmethod/classmethod .__func__
    property .fget .fset .fdel
cls.__abstractmethods__ :: frozenset<name>
'''
#types.SimpleNamespace
from abc import ABCMeta, abstractmethod, ABC
from .get_mro import get_mro



###############
class IObjDictOps(ABC):
    @abstractmethod
    def get_dict_name(self):pass
    def get_dict(self, obj, default=None):
        return getattr(obj, self.get_dict_name(), default)
    def get_dict_or_new(self, obj):
        d = self.get_dict(obj)
        if d is None:
            d = {}
            setattr(obj, self.get_dict_name(), d)
        return d

    def get_value(self, obj, attr, default=None):
        d = self.get_dict(obj)
        if d is None: return default
        return d.get(attr, default)
    def set_value(self, obj, attr, value):
        d = self.get_dict_or_new(obj)
        d[attr] = value
class Override_Meta_DictOps(IObjDictOps):
    def get_dict_name(self):
        return '__Override_Meta_namespace__'
override_meta_dict_ops = Override_Meta_DictOps()

__define__ = '__define__'
#@define
def define(f): return f
    override_meta_dict_ops.set_value(f, '__define__', True)
    return f

__override__ = '__override__'
#@override
def override(f):
    override_meta_dict_ops.set_value(f, __override__, True)
    return f

__not_implemented_abstract_method__ = '__not_implemented_abstract_method__'
def not_implemented_abstract_method(f):
    f = abstractmethod(f)
    override_meta_dict_ops.set_value(f, __not_implemented_abstract_method__, True)
    return f

__final_method__ = '__final_method__'
def final_method(f):
    override_meta_dict_ops.set_value(f, __final_method__, True)
    return f



__arbitrary_override_order_method__ = '__arbitrary_override_order_method__'
def arbitrary_override_order_method(f):
    f = define(f)
    override_meta_dict_ops.set_value(f, __arbitrary_override_order_method__, True)
    return f


from .TopMostBases_Meta import TopMostBases_Meta, get_top_most_bases

def union_compatible_dicts(dicts, output=None, handle_incompatible=None):
    # handle_incompatible(output, key, new_val) -> None | raise
    #       where new_val != output[key]
    if output is None: output = {}
    if handle_incompatible is None:
        def handle_incompatible(output, key, new_val):
            raise ValueError(f'{key!r}')

    nothing = []
    for d in dicts:
        for key, val in d.items():
            v = output.get(key, nothing)
            if v is nothing:
                output[key] = val
            elif v == val:
                pass
            else:
                handle_incompatible(output, key, val)
    return output


def get_method_name2base_flag2data_pair(cls):
    '''return method_name2base_flag2data_pair :: Map str (supercls, Map flag data)
'''
    assert isinstance(cls, Override_Meta)
    raise
    return cls.__method_name2
def get_final_method2class(cls):
    assert isinstance(cls, Override_Meta)
    raise
    return cls.__
def class_namespace_to_method_name2flag2data(class_namespace, obj2flag2data):
    '''cls.__dict__ is class_namespace??
class_namespace :: dict
method_name2flag2data :: Map str (Map flag data)
flag may be str; data maybe bool
'''not_implemented_abstract_method
    return {name : obj2flag2data(obj) for name, obj in class_namespace.items()}
class Override_Meta(TopMostBases_Meta):
    '''to use override

1) @define and @override are mutex
2) @define may be omitted
3) final_method can not be override
4) if A(B,C) and B <> C and B.f is not C.f
    and f is not arbitrary_override_order_method, then
    A should override f
    otherwise insert "f = override(not_implemented_abstract_method(f))"
        into the A's namespace as default value
5) arbitrary_override_order_method and not_implemented_abstract_method are mutex
    arbitrary_override_order_method should have one and only one default implement
    @arbitrary_override_order_method <: @define
    not_implemented_abstract_method


self.__method_name2base_cls_flag2data_pair__Override_Meta__
    :: Map str (base_cls, Map flag data)
'''
    def __new__(meta_cls, name, bases, namespace, **kwargs):
        self = super(__class__, meta_cls).__new__(meta_cls, name, bases, namespace, **kwargs)
        #mro = get_mro(self)
        bases = get_top_most_bases(self)
        bases_THIS = [base for base in bases if isinstance(__class__)]
        name2flag2data = self.self_namespace_to_method_name2base_flag2data_pair__Override_Meta()
        # name2flag2data :: Map method_name (Map flag data)
        def all_in(flag2data, *names):
            return all(name in flag2data for name in names)
        base_final_method2cls = union_compatible_dicts(
                map(get_final_method2class, bases_THIS))
        for name, flag2data for name2flag2data.items():
            if __override__ in flag2data:
                if __define__ in flag2data:
                    raise TypeError(f'{name!r}: __override__ & __define__')
                # fine: __final_method__ in flag2data:
                if name in base_final_method2cls:
                    raise TypeError(f'{name!r}: override final_method')
                for base in bases:
                    name_to_base_flag2data = get_method_name2base_flag2data_pair(base)
                    base, flag2data = name_to_base_flag2data.get(name, (None, None))
                    if __final_method__ in flag2data:
                        raise TypeError(f'{name!r}: override final_method')
            if all_in(flag2data, __override__,  __define__):


    def self_namespace_to_method_name2flag2data__Override_Meta(self):
        return class_namespace_to_method_name2flag2data(
                self.__dict__, self.obj2flag2data__Override_Meta)
    @classmethod
    def obj2flag2data__Override_Meta(meta_cls, obj):
        return override_meta_dict_ops.get_dict(obj, {})






'''


'''

