
'''
can an object pretend to be an instance of any class??
what is the class of an object creating?
assume object has no class at all
    class system is a optional subsystem

attribute is not property
    obj.object_attribute
    cls@.class_attribute

    consider how to document them
        (0) only object have docstring, so we document object only

        obj.attribute is an arbitrary object
        cls@@..descriptor is an descriptor, may be a property descriptor
            NOTE: cls@.attribute is an arbitrary object

        attribute is just a reference(or say a name) in the object's namespace,
            it is not a object, and can not have a docstring
                unless we document the keys of the namespace
                new_key = hash_fst(old_key, docstring)
                dict[old_key] = obj # donot override the original key
                dict[new_key] = obj # set non-exist key or override the original key
                should have different syntax
                dict{old_key} = obj

        property is a descriptor object
            named by a reference in the namespace of the class object
            (i.e. the object itself is a class)
            the descriptor may have docstring

        [class attribute] cls@.attribute  # not cls@@..descriptor
            cls is obj, so cls has attributes: cls.attributes
            normally, cls.f is not cls@.f
            cls.f is got via meta if any, but cls@.f is not.
            we can modify meta, so that for some f: cls.f =[def]= cls@.f
                but that is a bad idea
                how to use ops/cls?
                    1) wrap(zcls) -> zops
                        need not wrap
                        class zops:
                            # all classmethods
                            # zobj appear if f is instance method in zcls
                            @classmethod
                            def f(this_zops, zobj, ...):pass
                        def use(ops_or_cls, zobj, ...):
                            ops_or_cls@f(zobj, ...)
                    2) wrap(zops, zobj, interface) -> proxy_zobj
                        return a proxy; which is a duck of interface
                        proxy_zobj.f =[def]= zops@.f(zobj)
                        # no: proxy_zobj@.f =[def]= ?????

        conceptually, we may document class_attribute but not object_attribute
        in Python, a "class object"'s "class attribute" and "object attribute" are in same namespace, make it impossible to document them


defining Z language
assume the underlying language is Y
now, we distinguish zobj and yobj although zobj/yobj may actually yobj/zobj
    e.g. yobj <<- IPzthonObjectInPython will be zobj.
    (<<- is_duck_of; duck_type relationship)



'''

__all__ = '''
    IClassGetattrImplicitInPython
    IDataTypeProtocolInPython
    PzthonObjectGlobalOpsInPython

    IPzthonObjectInPythonBase
        IPzthonObjectInPython
        IPythonObjectAsPzthonObject
            python_class2data_type_protocol
    '''.split()

from collections.abc import Callable
from abc import ABC, abstractmethod

class _A:pass
class _B:pass
class INotPythonCallable(ABC):
    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if issubclass(cls, Callable): raise TypeError
    def __subclasshook__(cls, C):
        if issubclass(C, Callable):
            return False
        return NotImplemented
    pass

class IPzthonObjectInPythonBase(INotPythonCallable, _B, _A):pass
class Non_IPzthonObjectInPython(_A, _B):
    # should not be a IPzthonObjectInPython; hence the "_A", "_B"
    pass
class IClassGetattrImplicitInPython(ABC, Non_IPzthonObjectInPython):
    # "implicit" means these below methods donot go through zcls
    #   hence can be used to get attr of zcls/zinstance
    # all return a bound member in Pzthon
    #   how to get non-bound member???
    #   unless the class system implement that
    '''
    def non_instance_first_getattr(self, zobj, name):
        # zobj??????.?????????_attribute
        try:
            return self.__object_getattr__(zobj, name)
        except AttributeError:
            return self.__instance_getattr__(zobj, name)
    '''
    def instance_getattr(self, zobj, name):
        # zobj.instance_attribute
        # zobj.object_attribute
        data_type_protocol = PzthonObjectGlobalOpsInPython.get_data_type_protocol(zobj)
        may_zcls = data_type_protocol.get_may_class(zobj)
        if may_zcls is None:
            return self.__object_getattr__(zobj, name)
        zinstance = zobj
        return self.__instance_getattr__(zinstance, name)

    def __object_getattr__(self, zobj, name):
        # zobj.f where zobj may not be zinstance
        raise AttributeError
    @abstractmethod
    def __instance_getattr__(self, zinstance, name):
        # treat zinstance as a Pzthon instance has class zcls/None
        # zinstance.f
        #
        # possible implement:
        #   zcls = zinstance^^.get_may_class()
        #   assert zcls is not None
        #   return curry_if_instance_method zcls@.name zinstance
        #   or return zcls@@..name as f in f.get(zcls, zinstance)
        pass
    @abstractmethod
    def instance_getattr_private(self, zinstance, zsupercls name):
        # treat zinstance as a Pzthon instance has class zsupercls
        # zinstance$zsupercls@$.f
        # zinstance$@$.f == zinstance$__class__@$.f
        pass
    @abstractmethod
    def class_getattr(self, zcls, name):
        # treat zcls as a Pzthon class
        # zcls@.f
        pass
    @abstractmethod
    def class_getattr_private(self, zcls, name):
        # treat zcls as a Pzthon class
        # zcls@$.f
        pass
class IDataTypeProtocolInPython(ABC, Non_IPzthonObjectInPython):
    # assume zobj...data_type_protocol is a IDataTypeProtocolInPython
    @abstractmethod
    def get_may_class(self, zobj):
        # self -> zobj -> (yNone | zobj)
        pass
    @abstractmethod
    def class_getattr_implicit(self, zobj):
        # self -> zobj -> IClassGetattrImplicitInPython
        # zobj not zcls, since zobj may have no zcls
        pass
    def __object_getattr__(self, zobj, name):
        raise AttributeError
    def object_getattr(self, zobj, may_zcls, dot_name):
        # self -> zobj -> dot_name -> zobj
        # dot_name = dot + name
        # dot not in ['...', '^^.', '^^@.']
        # dot in ['..', '.', '@.', '$@$.', '@$.']
        #
        # dot = regex'\W*.(?=\w)' when tokenizing
        # dot_name = regex'\W*.\w+'
        hdot, tdot, name = dot_name.rpartition('.')
        if not tdot: raise AttributeError
        dot = hdot+tdot
        if dot == '$@$.': assert may_zcls is not None
        implicit = self.class_getattr_implicit(zobj)
        d = { '..': lambda: getattr(implicit, name)
            , '.': lambda: implicit.instance_getattr(zobj, name)
            , '@.': lambda: implicit.class_getattr(zobj, name)
            , '$@$.': lambda: implicit.instance_getattr_private(zobj, may_zcls, name)
            , '@$.': lambda: implicit.class_getattr(zobj, name)
            }
        if dot not in d: raise AttributeError
        return d[dot]()
    pass
class IPzthonObjectInPython(IPzthonObjectInPythonBase):
    # below exprs assumed in Pzthon language on top Python
    # zobj is Pzthon object; yobj is Python object
    # py :: zobj -> yobj
    # yobj....f = py_getattr(py(zobj), 'f')
    # zobj...f = py(zobj)....f
    #   f = data_type_protocol | ...
    #       members of IPzthonObjectInPython
    # zobj^^@.f = py(zobj)....data_type_protocol....f
    # zobj^^.f = zobj^^@.f zobj
    #   f = get_may_class | class_getattr_implicit | ...
    #       members of IDataTypeProtocolInPython
    # descriptor subsystem(optional)
    #   zcls@@...f = v.s zcls@.f but not curry the zcls, the result maybe the original descriptor
    #   zcls@@..f = zcls@@...f as f in f if f is a descriptor else wrap_as_descriptor(f)
    ##################
    # below exprs assumed in Pzthon language
    # zobj..f = zobj^^.class_getattr_implicit....f zobj
    #   f = instance_getattr | class_getattr | instance_getattr_private | class_getattr_private
    #       members of IClassGetattrImplicitInPython
    # zinstance.f = zinstance..instance_getattr('f')
    # zcls@.f = zcls..class_getattr('f')
    # zinstance$zcls@$.f = zinstance..instance_getattr_private('f')
    #   zinstance$@$.f = zinstance$__class__@$.f
    # zcls@$.f = zcls..class_getattr_private('f')
    #
    # expr as var in ... =[def]= let var = expr in ...
    # continuation: # keyword cor
    #   continuation = tail :: a -> r
    #   cps :: continuation -> r # CPS r a # missing a tail
            # (a->r)->r # <=[as-if]=> (r | a | (a,a,a, r->r->r->r->r->r)|...)
    #       continuation = lambda a: r
    #       cps = lambda continuation: continuation(a)
    #   def a2mb(a): mb # a -> CPS r b # a -> (b->r) -> r # <=[as-if]=> a -> b
    #   mb = ma >>= a2mb # @ma \n def mb(a): mb
    #       = lambda b2r: ma(lambda a: a2mb(a)(b2r))
    #   callCC :: ((a -> CPS r b) -> CPS r a) -> CPS r a
    #       # == CPS (CPS r a) (a -> CPS r b)
    #       # <=[as-if]=> (a -> CPS r b)
    #       # <=[as-if]=> (a -> CPS r AnyThing)
    #   callCC f = (\k -> (f (\a -> (\_ -> k a))) k)
    #   callCC a2bEr_to_aEr = aEr@(\a2r -> r@(a2r_to_r@aEr@(a2bEr_to_aEr a2bEr@(\a -> bEr@b2r_to_r@(\_b2r -> a2r a))) a2r))
    #   but in Pzthon:
    #   tail :: r_middle -> r
    #   continuation :: () -> r
    #   # ctail :: (() -> r_middle) -> r
    #   cps :: continuation -> r # (()->r)->r
    #   cps(continuation) = r
    #   cps // continuation1 = continuation2 = lambda: cps(continuation1)
    #   cps1 ** cps2 = cps3 = lambda continuation: cps1(cps2 // continuation)
    #       cps ** (cps ** (...))
    #   tail1 >> tail2 >> tail3 = tail = lambda x: tail3(tail2(tail1(x)))
    #       ((...) >> tail) >> tail
    #   continuation1 >> tail = continuation2 = lambda: tail(continuation1())
    #   0) cps cor cps  # a cps again
    #       a cor b cor c = a ** b ** c
    #   1) cps cor: lazy_expr         # a normal value = cps(lambda: lazy_expr)
    #       cps1 cor: cps2 cor: expr = cps1(lambda: cps2(lambda:expr))
    #       val = dict.cps_get(key) cor: eval_default()
    #   2) return cps cor:
    #      body # no indent
    #
    @property
    @abstractmethod
    def data_type_protocol(self):
        # zobj -> IDataTypeProtocolInPython
        # zobj...data_type_protocol =[def]= py(zobj)....data_type_protocol
        pass
    pass


class PzthonObjectGlobalOpsInPython:
    # to be used as global Pzthon builtins
    # an zobj may be an IPzthonObjectInPython or an IPythonObjectAsPzthonObject
    # should avoid call py(zobj)....data_type_protocol directly
    #   use PzthonObjectGlobalOpsInPython.get_data_type_protocol(zobj) instead
    @staticmethod
    def get_data_type_protocol(zobj):
        if isinstance(zobj, IPzthonObjectInPython):
            return zobj.data_type_protocol
        if isinstance(zobj, IPythonObjectAsPzthonObject):
            return IPythonObjectAsPzthonObject.get_data_type_protocol(zobj)
    pass



class IPythonObjectAsPzthonObject(IPzthonObjectInPythonBase):
    # to be used in PzthonObjectGlobalOpsInPython
    # no containers: tuple/dict...???
    # str, int, bool, callable, None, Exception...
    #       callable ==>> IPzthonObjectInPythonBase is NotPythonCallable
    @staticmethod
    def is_element(yobj):
        ycls = type(yobj)
        return ycls in python_class2data_type_protocol
    @staticmethod
    def get_data_type_protocol(yobj):
        # for some builtin ycls
        ycls = type(yobj)
        may = python_class2data_type_protocol.get(ycls)
        if may is None:
            raise TypeError(ycls)
        return may
    pass


# Map ycls IDataTypeProtocolInPython
python_class2data_type_protocol = make_python_class2data_type_protocol()
def make_python_class2data_type_protocol():
    raise

'''
# TODO
class PzthonOpsAsPzthonPseudoCls(IPzthonObjectInPython, metaduck_type = IDuckType):
    # zops -> duck_type -> pseudo_zcls
    #   a pseudo_zcls can be use as a class:
    #       pseudo_zcls@.f = zops.f
    #       pseudo_zcls.f = raise Exception
    #       isinstance/issubclass -> ??
    #           <-/<: may fail, but should support duck_type: <<-/<<:
    def __init__(self, zops, duck_type):
        raise
'''

































######################## old



'''
data_type_protocol/data_type/raw are all not object
data_type_protocol:
    get_data_type$ :: DataTypeProtocol$ -> DataType$
    raw_init$ :: (p$ <- DataTypeProtocol$) -> (get_data_type$ p$) -> args -> ()
    raw_getattr$ :: (p$ <- DataTypeProtocol$) -> (get_data_type$ p$) -> name -> object
data_type:
    new$ :: (d$ <- DataType$) -> d$
object = (p$ <- DataTypeProtocol$, get_data_type$ p$)

def make_object(data_type_protocol$, args):
    raw$ = new$ (get_data_type$ data_type_protocol$)
    raw_init$ data_type_protocol$ raw$ args
    object = (data_type_protocol$, raw$)
    return object

obj.f
    raw_getattr$ (fst$ obj) (snd$ obj) 'f'


'''





'''
obj...f
    physical get
cls..f
    class_getattr_implicit(cls, 'f')
    at least: {__instance_getattr__, __class_getattr__} <= Domain f
    may __instance_getattr_private__, __class_getattr_private__
get_class :: obj -> MayNone cls
None
get_data_type_info :: obj -> IDataTypeInfo
get_data_type_protocol :: IDataTypeInfo -> IDataTypeProtocol
get_data_type :: IDataTypeProtocol -> IDataType




public system
    instance.f
        instance_getattr(instance, 'f')
    cls@.f
        class_getattr(cls, 'f')

private system
    instance$cls@$.f
        instance_getattr_private(instance, cls, 'f')
    instance$@$.f
        instance_getattr_private(instance, __class__, 'f')
    cls@$.f
        class_getattr_private(cls, 'f')


data_type_protocol system
    object^^.f(args)
        get_data_type_protocol(get_data_type_info(object)).f(object, args)
    object^^@.f
        get_data_type_protocol(get_data_type_info(object)).f

'''

builtins
    is_builtin_object(obj)
    is_instance_of_builtin_class(obj, cls)
    get_data_type_info
    get_data_type_protocol


    # now assume a "space call", "static typed" sublanguage
    # obj@ is an object in original language
    get_data_type_info :: IObject@ -> Either DataTypeInfo IDataTypeInfo@
    get_data_type_protocol :: DataTypeInfo -> DataTypeProtocol
    wrap_data_type_info :: DataTypeInfo -> IDataTypeInfo@
    get_class_via_builtin_data_type_protocol :: IObject@ -> MayNone IClass@
    class_getattr_implicit_via_builtin_data_type_protocol :: IClass@ -> IString@ -> IObject@
    def get_data_type_info@(obj@) -> IDataTypeInfo@:
        case get_data_type_info obj@ of
            Left data_type_info -> wrap_data_type_info data_type_info
            Right i_data_type_info@ -> i_data_type_info@

    struct BuiltinObject{
        DataTypeInfo*;

        # Dict object_namespace;
        Dict instance_namespace;
        Dict class_namespace;
    }
    struct DataTypeInfo
    DataTypeProtocol
    DataType


def get_data_type_protocol(data_type_info):
    return data_type_info.get_data_type_protocol()
def get_class(obj):
    info = get_data_type_info(obj)
    i_data_type_protocol = get_data_type_protocol(info)
    if is_instance_of_builtin_class(i_data_type_protocol, DataTypeProtocol):
        # builtins...
        # bypass...
        return get_class_via_builtin_data_type_protocol$ obj
    return i_data_type_protocol.get_class(obj)
def class_getattr_implicit(cls, name):
    # should accept name in {__instance_getattr__, __class_getattr__}
    assert cls in IClass
    info = get_data_type_info(cls)
    i_data_type_protocol = get_data_type_protocol(info)
    if is_instance_of_builtin_class(i_data_type_protocol, DataTypeProtocol):
        # builtins...
        # bypass...
        return class_getattr_implicit_via_builtin_data_type_protocol$ cls name
    return i_data_type_protocol.class_getattr_implicit(cls, name)








################################

def instance_getattr(object, name):
    # instance.f
    may_cls = get_class(object)
    if may_cls is None:
        return object^^.object_getattr(name)
    cls, instance = may_cls, object
    get = class_getattr_implicit(cls, '__instance_getattr__')
    return get(instance, name)

def class_getattr(cls, name):
    # cls@.f
    assert cls in IClass
    get = class_getattr_implicit(cls, '__class_getattr__')
    return get(cls, name)


# TODO: def instance_getattr_private and class_getattr_private





class IObject:
    # builtin: def get_data_type_info(self):pass
    pass
class IDataTypeInfo:
    def get_data_type_protocol(self):pass
class IDataTypeProtocol:
    def get_data_type(self):pass
    def class_getattr_implicit(self, cls, name):pass
    def get_class(self, obj):pass
    def object_getattr(self, obj, name):pass



