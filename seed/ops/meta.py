#__all__:goto
#main_body_src_code:goto
#HHHHH
#[[[__doc__:begin
r'''
seed.ops.meta
    e ../../python3_src/seed/ops/meta.py
py -m    seed.ops.meta
py -m nn_ns.app.debug_cmd   seed.ops.meta

from seed.ops.meta import ...



type.__call__(cls, ...):
    <==> cls(...)
    sf = cls.__new__(cls, ...)
    cls.__init__(sf)
    return sf
    type(cls) -> cls.__class__
    type(name:str, bases, kwargs, body_ns) -> new cls
my framework:
    start:
        standardize/convert input to property
        check input property
    init:
        random delta init
        + optional property
        + nonlazy cached property # via input or calc by other property
    finally: check sf
        check multi-property
    dynamic check per batch-update-commit
        if error then rollback
        sf+shadow_updating? property internal structure???

    method call with env:
        global-env[immutable]
        local-call-recur-subtree-env[affect-local]
    get property:
        data -> cls
        level_up = cls.__dict__[symbol4level_up]
        cls_ = cls
        tower = [data]
        for _ in range(level_up):
            ops = cls_.__dict__[symbol4ops]
            tower.append(ops)
            cls_ = type(ops)
        assert len(tower) == level_up+1
        pseudo_ops = cls_.__dict__[symbol4pseudo_ops]
        pseudo_ops handle tower ...

        if 

use unhashable symbol/SymbolLeadingPath?
    data maybe mapping!!!
ops[:?symbol//..., kw:arg]]
module_.xxx.yyy[class_.T.C[def_.fff[kw_.kkk]]]
build_Symbol[module__].xxx.yyy[attrs__].T.C[keys, k0, k1].fff[inner__].T.fff[kw__:kkk]
    ??? 到底是 描述 mk_new_Symbol 返回值 保存/输出 的地址 pkg+qname 还是 描述 概念出处 如 函数的kw
        一起！
        symbol(extension<pkg, qname4storage, qname4auto_generate>, intension<pkg,qname, ((keys,qname)|func_body-qname)*, kw?>)
            one = pkg qname (key|qname)* kw?
                qname qname ==>> qname func_body-qname
                isinstance(xxx, EqById)
                    .register
            complex = one override one | ...
        get_or_mk_Symbol? xxx
            get_Symbol(extension)
            mk_new_Symbol(extension, intension)
                intension.___get_or_mk_eqv_wrapped_obj___
                    type2get_or_mk_eqv_wrapped_obj[type(intension)]
                        storage4attachment
                            ___get_storage4attachment___
                    get_or_mk_eqv_wrapped_obj
    local-func-api:
    @???args_kwargs_api = (symbol..., kw=symbol)
    def f(..., symbol2arg, arg0...argN, /,*, kw...)
mk => mk_new, get_or_mk/_gk


design:
    #pseudo_ops_cls <: IPseudoOps
        #___ops_get_member___(pseudo_ops, obj_tower, pseudo_ops_level, target_ops_level, section_name, namespace_name, symbol) -> member
    ops_public_section_wrapper_cls <: IOpsPublicSection
        ___ops_get_public_member___(ops_public_section_wrapper, obj_tower, ops_level, target_level, namespace_name, symbol) -> member
    #no: ops_cls <: pseudo_ops_cls
    #ops_cls(IOps, metaclass=OpsMeta))
    data_cls(metaclass=DataMeta))
        ___upper_ops_get_public_member___
            ops_cls.wrapper4ops_public_section.___ops_get_public_member___
        __getitem__
            ___upper_ops_get_public_member___
            -> member | member(...)


    ops_obj/data_obj :: ops_cls :: ops_meta
    pseudo_ops_cls:
        * (pseudo_ops_cls :: ops_meta)
        * (pseudo_ops_cls <: IPseudoOps)
        ops_cls || IPseudoOps
        assert





object.__new__
type.__new__
 |  type(object) -> the object's type
 |  type(name, bases, dict) -> a new type
 |

#[[[py38_doc:begin
#Dynamic_Type_Creation:goto
#Customizing_Class_Creation:Metaclasses:goto
#wwwzzz:goto


#[[[Dynamic_Type_Creation:begin
types.new_class(name, bases=(), kwds=None, exec_body=None) -> cls
    'class {name!s}(*bases, **kwds): exec_body(locals())'
    bases2 = types.resolve_bases(bases)
    (metaclass, namespace, kwds2) = types.prepare_class(name, bases2, kwds)
    cls = metaclass(name, bases2, namespace, **kwds2)
types.prepare_class(name, bases=(), kwds=None) -> (metaclass, namespace, kwds2)
    metaclass = kwds['metaclass']
    kwds2 = kwds\-\'metaclass'
    ns = namespace = locals = metaclass.__prepare__(name, bases2, **kwds2)
types.resolve_bases(bases)
    -> [*itertools.chain.from_iterable(([pseudo_cls] if isinstance(pseudo_cls, type) or not hasattr(type(pseudo_cls), '__mro_entries__') else [*type(pseudo_cls).__mro_entries__(pseudo_cls)]) for pseudo_cls in bases)]


types — Dynamic type creation and names for built-in types

Dynamic Type Creation

types.new_class(name, bases=(), kwds=None, exec_body=None)

    Creates a class object dynamically using the appropriate metaclass.

    The first three arguments are the components that make up a class definition header: the class name, the base classes (in order), the keyword arguments (such as metaclass).

    The exec_body argument is a callback that is used to populate the freshly created class namespace. It should accept the class namespace as its sole argument and update the namespace directly with the class contents. If no callback is provided, it has the same effect as passing in lambda ns: ns.

    New in version 3.3.

types.prepare_class(name, bases=(), kwds=None)

    Calculates the appropriate metaclass and creates the class namespace.

    The arguments are the components that make up a class definition header: the class name, the base classes (in order) and the keyword arguments (such as metaclass).

    The return value is a 3-tuple: metaclass, namespace, kwds

    metaclass is the appropriate metaclass, namespace is the prepared class namespace and kwds is an updated copy of the passed in kwds argument with any 'metaclass' entry removed. If no kwds argument is passed in, this will be an empty dict.

    New in version 3.3.

    Changed in version 3.6: The default value for the namespace element of the returned tuple has changed. Now an insertion-order-preserving mapping is used when the metaclass does not have a __prepare__ method.

    See also
        Metaclasses
            Full details of the class creation process supported by these functions

        PEP 3115 - Metaclasses in Python 3000
            Introduced the __prepare__ namespace hook


types.resolve_bases(bases)

    Resolve MRO entries dynamically as specified by PEP 560.

    This function looks for items in bases that are not instances of type, and returns a tuple where each such object that has an __mro_entries__ method is replaced with an unpacked result of calling this method. If a bases item is an instance of type, or it doesn’t have an __mro_entries__ method, then it is included in the return tuple unchanged.

    New in version 3.7.

    See also
        PEP 560 - Core support for typing module and generic types



#]]]Dynamic_Type_Creation:end

#[[[Customizing_Class_Creation:Metaclasses:begin
3. Data model
3.3.3. Customizing class creation

    Whenever a class inherits from another class, __init_subclass__ is called on that class. This way, it is possible to write classes which change the behavior of subclasses. This is closely related to class decorators, but where class decorators only affect the specific class they’re applied to, __init_subclass__ solely applies to future subclasses of the class defining the method.

classmethod object.__init_subclass__(cls)

    This method is called whenever the containing class is subclassed. cls is then the new subclass. If defined as a normal instance method, this method is implicitly converted to a class method.

    Keyword arguments which are given to a new class are passed to the parent’s class __init_subclass__. For compatibility with other classes using __init_subclass__, one should take out the needed keyword arguments and pass the others over to the base class, as in:

    class Philosopher:
        def __init_subclass__(cls, /, default_name, **kwargs):
            super().__init_subclass__(**kwargs)
            cls.default_name = default_name

    class AustralianPhilosopher(Philosopher, default_name="Bruce"):
        pass

    The default implementation object.__init_subclass__ does nothing, but raises an error if it is called with any arguments.

    Note

    The metaclass hint metaclass is consumed by the rest of the type machinery, and is never passed to __init_subclass__ implementations. The actual metaclass (rather than the explicit hint) can be accessed as type(cls).

    New in version 3.6.


3.3.3.1. Metaclasses
class Meta(type):
    pass

class MyClass(metaclass=Meta):
    pass

class MySubclass(MyClass):
    pass

When a class definition is executed, the following steps occur:
    MRO entries are resolved;
    the appropriate metaclass is determined;
    the class namespace is prepared;
    the class body is executed;
    the class object is created.

3.3.3.2. Resolving MRO entries

    If a base that appears in class definition is not an instance of type, then an __mro_entries__ method is searched on it. If found, it is called with the original bases tuple. This method must return a tuple of classes that will be used instead of this base. The tuple may be empty, in such case the original base is ignored.

    See also
        PEP 560 - Core support for typing module and generic types


3.3.3.3. Determining the appropriate metaclass

    The appropriate metaclass for a class definition is determined as follows:

        if no bases and no explicit metaclass are given, then type() is used;

        if an explicit metaclass is given and it is not an instance of type(), then it is used directly as the metaclass;

        if an instance of type() is given as the explicit metaclass, or bases are defined, then the most derived metaclass is used.

    The most derived metaclass is selected from the explicitly specified metaclass (if any) and the metaclasses (i.e. type(cls)) of all specified base classes. The most derived metaclass is one which is a subtype of all of these candidate metaclasses. If none of the candidate metaclasses meets that criterion, then the class definition will fail with TypeError.


3.3.3.4. Preparing the class namespace

    Once the appropriate metaclass has been identified, then the class namespace is prepared. If the metaclass has a __prepare__ attribute, it is called as namespace = metaclass.__prepare__(name, bases, **kwds) (where the additional keyword arguments, if any, come from the class definition).

    If the metaclass has no __prepare__ attribute, then the class namespace is initialised as an empty ordered mapping.

    See also
        PEP 3115 - Metaclasses in Python 3000
            Introduced the __prepare__ namespace hook


3.3.3.5. Executing the class body

    The class body is executed (approximately) as exec(body, globals(), namespace). The key difference from a normal call to exec() is that lexical scoping allows the class body (including any methods) to reference names from the current and outer scopes when the class definition occurs inside a function.

    However, even when the class definition occurs inside the function, methods defined inside the class still cannot see names defined at the class scope. Class variables must be accessed through the first parameter of instance or class methods, or through the implicit lexically scoped __class__ reference described in the next section.


3.3.3.6. Creating the class object

    Once the class namespace has been populated by executing the class body, the class object is created by calling metaclass(name, bases, namespace, **kwds) (the additional keywords passed here are the same as those passed to __prepare__).

    This class object is the one that will be referenced by the zero-argument form of super(). __class__ is an implicit closure reference created by the compiler if any methods in a class body refer to either __class__ or super. This allows the zero argument form of super() to correctly identify the class being defined based on lexical scoping, while the class or instance that was used to make the current call is identified based on the first argument passed to the method.

    CPython implementation detail: In CPython 3.6 and later, the __class__ cell is passed to the metaclass as a __classcell__ entry in the class namespace. If present, this must be propagated up to the type.__new__ call in order for the class to be initialised correctly. Failing to do so will result in a RuntimeError in Python 3.8.

    When using the default metaclass type, or any metaclass that ultimately calls type.__new__, the following additional customisation steps are invoked after creating the class object:

        first, type.__new__ collects all of the descriptors in the class namespace that define a __set_name__() method;

        second, all of these __set_name__ methods are called with the class being defined and the assigned name of that particular descriptor;

        finally, the __init_subclass__() hook is called on the immediate parent of the new class in its method resolution order.

    After the class object is created, it is passed to the class decorators included in the class definition (if any) and the resulting object is bound in the local namespace as the defined class.

    When a new class is created by type.__new__, the object provided as the namespace parameter is copied to a new ordered mapping and the original object is discarded. The new copy is wrapped in a read-only proxy, which becomes the __dict__ attribute of the class object.

    See also

    PEP 3135 - New super

        Describes the implicit __class__ closure reference

3.3.3.7. Uses for metaclasses

    The potential uses for metaclasses are boundless. Some ideas that have been explored include enum, logging, interface checking, automatic delegation, automatic property creation, proxies, frameworks, and automatic resource locking/synchronization.


#]]]Customizing_Class_Creation:Metaclasses:end
#[[[wwwzzz:begin
#]]]wwwzzz:end
#]]]py38_doc:end


#[[[doctest_examples:begin
>>>
...
#]]]doctest_examples:end

#'''
#]]]__doc__:end

#################################
#HHHHH
__all__ = '''

    '''.split()

#################################
#HHHHH
___begin_mark_of_excluded_global_names__0___ = ...
from seed.tiny import str2__all__
#__all__ = str2__all__(r'''#)
    #(''')
from seed.abc.abc import ABC, abstractmethod, override#, not_implemented, ABCMeta
from seed.tiny import echo, print_err, mk_fprint, mk_assert_eq_f, expectError
from seed.tiny import echo_args_kwargs, slice2triple
from seed.helper.get_args_kwargs import mk_GetArgsKwargs as mkG, xcall
from seed.helper.check.check import mk_checker, Checker__Mapping, Checker__slice, Checker__type_is, the_pass_checker, the_checker__is_None
from seed.helper.check.checkers import check_pair, check_type_is, check_seq, checker4pseudo_identifier
#from seed.helper.repr_input import repr_helper
#from seed.helper.repr_input import repr_helper__str
from seed.tiny import MapView, null_mapping_view
from collections.abc import Sequence

if 0b00:#[01_to_turn_off]
    #0b01
    print(fr'x={x}')
    from seed.tiny import print_err
    print_err(fr'x={x}')
    from pprint import pprint
    pprint(x)
___end_mark_of_excluded_global_names__0___ = ...

#HHHHH
#[[[main_body_src_code:begin
#_t:goto
#OpsMeta:goto
#SymbolLeadingPath:goto
#zzzwww:goto


object.__new__
type.__new__
 #|  type(object) -> the object's type
 #|  type(name, bases, dict) -> a new type
 #|

#[[[_t:begin
def _t():
    dir(object)
    dir(object())
    dir(type)
    dir(type('T', (), {}))
    ls = [dir(object)
        ,dir(object())
        ,dir(type)
        ,dir(type('T', (), {}))
        ]
    #for s in ls: print(sorted(s))
    assert ls[0]==ls[1]!=ls[2]!=ls[3]!=ls[1]

    assert ls[1:] == \
        [['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
        ,['__abstractmethods__', '__base__', '__bases__', '__basicsize__', '__call__', '__class__', '__delattr__', '__dict__', '__dictoffset__', '__dir__', '__doc__', '__eq__', '__flags__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__instancecheck__', '__itemsize__', '__le__', '__lt__', '__module__', '__mro__', '__name__', '__ne__', '__new__', '__prepare__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasscheck__', '__subclasses__', '__subclasshook__', '__text_signature__', '__weakrefoffset__', 'mro']
        ,['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
        ]
#]]]_t:end





#[[[SymbolLeadingPath:begin
def symbol_leading_path2may_pair(symbol_leading_path, /):
    cls = type(symbol_leading_path)

    may_pair = cls.___to_may_pair___(symbol_leading_path)
    assert may_pair is None or (type(may_pair) is tuple and len(may_pair)==2)
    return may_pair

class _SymbolLeadingPathBase(ABC):
    def __floordiv__(lhs, rhs, /):
        return SymbolLeadingPathAppend(lhs, rhs)
    def __truediv__(lhs, rhs, /):
        return lhs/None/rhs
    def __reversed__(sf, /):
        path = sf
        while 1:
            may_pair = symbol_leading_path2may_pair(path)
            if may_pair is None:
                yield path
                return
            (path, last_part) = may_pair
            yield last_part

    @abstractmethod
    def ___to_may_pair___(sf, /):
        '-> None|(inits_part, last_part)'
    @abstractmethod
    def __repr__(sf, /):
        ...
def check_qname(qname, /, *, empty_ok):
    check_type_is(str, qname)
    if not type(qname) is str: raise TypeError
    if not all(name.isidentifier() for name in qname.split('.')):raise ValueError
    if not empty_ok and not qname: raise ValueError

#from seed.helper.unique_immutable_value import UniquePoint
#from seed.types.AddrAsHash import AddrAsHash as EqById
#from seed.abc.eq_by_id.AddrAsHash import AddrAsHash as EqById
#from seed.mapping_tools.fdefault import mapping_set__new_or_pass__cased_, mapping_get__tmay__get_Nothing
#import weakref
from seed.helper.unique_immutable_value import UniqueWrapper4tuple, UniqueWrapper4str, IWrapperBase4UniqueHashable
from seed.abc.wrapper.IWrapper import get_the_wrapped_obj
    # checker4qual_name ~ checker4identifier
    # check_qname ~ checker4pseudo_identifier
    #from seed.helper.check.checkers import checks, checkers, check_funcs
    #view ../../python3_src/seed/helper/check/checkers.py

class Symbol(IWrapperBase4UniqueHashable, _SymbolLeadingPathBase):
    #class Symbol(EqById, _SymbolLeadingPathBase):
    #_unique_point = UniquePoint()
    #_unique_point = weakref.WeakValueDictionary()
    #simplify_the_wrapped_obj2args_kwargs4repr, type4the_wrapped_obj
    type4the_wrapped_obj = UniqueWrapper4tuple

    @classmethod
    @override
    def simplify_the_wrapped_obj2args_kwargs4repr(cls, the_wrapped_obj, /):
        args = (*map(get_the_wrapped_obj, the_wrapped_obj),)
        return args, {}
    if 0:
        r'''
      def __new__(cls, pkg, qname, /):
        d = cls._unique_point
        k = UniqueWrapper4tuple(UniqueWrapper4str(pkg), UniqueWrapper4str(qname))
        def fdefault():
            check_qname(pkg, empty_ok=False)
            check_qname(qname, empty_ok=False)
            sf = super(__class__, cls).__new__(cls)
            sf.__pair = k
            return sf
        (is_old_sf, sf) = mapping_set__new_or_pass__cased_(d, k, 0, fdefault, try_vs_Nothing_vs_in=None)
        return sf
        #################################
        #################################
        d = cls._unique_point
        k = (pkg, qname)
        def fdefault():
            check_qname(pkg, empty_ok=False)
            check_qname(qname, empty_ok=False)
            sf = super(__class__, cls).__new__(cls)
            sf.__pkg = pkg
            sf.__qname = qname
            return sf
        (is_old_sf, sf) = mapping_set__new_or_pass__cased_(d, k, 0, fdefault, try_vs_Nothing_vs_in=None)
        return sf
        #################################
        #################################
    @override
    def __repr__(sf, /):
        return repr_helper(sf, sf.pkg_part, sf.qname_part)
    @override
    def __repr__(sf, /):
        return repr_helper__str(f'{type(sf).__name__!s}._gk', sf.pkg_part, sf.qname_part)
        #'''

    @property
    def pkg_part(sf, /):
        return get_the_wrapped_obj(sf)[0]
        return sf.__pair[0]
        return sf.__pkg
    @property
    def qname_part(sf, /):
        return get_the_wrapped_obj(sf)[1]
        return sf.__pair[1]
        return sf.__qname

    @override
    def ___to_may_pair___(sf, /):
        '-> None|(inits_part, last_part)'
        return None
    @classmethod
    @override
    def ___check_the_wrapped_obj___(cls, the_wrapped_obj, /):
        check_type_is(UniqueWrapper4tuple, the_wrapped_obj)
        check_pair(get_the_wrapped_obj(the_wrapped_obj))
        w_pkg, w_qname = the_wrapped_obj
        check_qname(get_the_wrapped_obj(w_pkg), empty_ok=False)
        check_qname(get_the_wrapped_obj(w_qname), empty_ok=False)

    @classmethod
    @override
    def get_or_mk_eqv_wrapped_obj(cls, /, *args, **kwargs):
    #def mk(cls, /, *args, **kwargs):
        if not kwargs and len(args)==2:
            return get_or_mk_the_wrapped_obj4Symbol_ex(*args, **kwargs)
        return super().get_or_mk_eqv_wrapped_obj(*args, **kwargs)

def mk_new_Symbol(pkg, qname, /):
    return get_or_mk_Symbol(pkg, qname, exist_ok=False)
    return Symbol.mk_new(pkg, qname)
def get_or_mk_Symbol(pkg, qname, /, *, exist_ok=True):
    if exist_ok:
        return Symbol.get_or_mk(pkg, qname)
    else:
        return Symbol.mk_new(pkg, qname)

def get_or_mk_the_wrapped_obj4Symbol_ex(pkg, qname, /):
    the_wrapped_obj = UniqueWrapper4tuple.get_or_mk((UniqueWrapper4str.get_or_mk(pkg), UniqueWrapper4str.get_or_mk(qname)))
    return the_wrapped_obj
r'''
def get_or_mk_Symbol_ex(pkg, qname, /):
    is_new, sf = Symbol.get_or_mk_ex(pkg, qname)
    return is_new, sf
r'''

assert get_or_mk_Symbol('a', 'b') is get_or_mk_Symbol('a', 'b')
assert get_or_mk_Symbol('a', 'b') is eval(repr(get_or_mk_Symbol('a', 'b')))
expectError(RuntimeError, lambda:
    [mk_new_Symbol('a', 'b'), mk_new_Symbol('a', 'b')]
    )

checker4args_kwargs_pair = mk_checker(('t', Sequence, Checker__Mapping(checker4pseudo_identifier, mk_checker(True))))
#checker4args_kwargs_pair = mk_checker(('t', check_seq, Checker__Mapping(checker4pseudo_identifier, mk_checker(True))))
    #Sequence ~ check_type_is?check_type_le
    #   ???used check_seq instead
checker4symbol_arg_slices = mk_checker(('us', Checker__slice(Checker__type_is(Symbol), the_pass_checker, the_checker__is_None)))


class SymbolLeadingPathAppend(_SymbolLeadingPathBase):
    def __init__(sf, symbol_leading_path, obj, /):
        check_SymbolLeadingPath(symbol_leading_path)
        sf.__inits = symbol_leading_path
        sf.__last = obj
    @property
    def inits_part(sf, /):
        return sf.__inits
    @property
    def last_part(sf, /):
        return sf.__last
    @override
    def ___to_may_pair___(sf, /):
        '-> None|(inits_part, last_part)'
        return sf.inits_part, sf.last_part

    @override
    def __repr__(sf, /):
        ss = [*map(repr, reversed(sf))]
        #move after clean: ss.reverse()
        #   'symbol//None' not 'symbol/None/'
        #pre_is_empty = False
        pre_is_empty = True
        for i in range(len(ss)):
            if ss[i] == 'None':
                if pre_is_empty:
                    pass
                else:
                    ss[i] = ''
                pre_is_empty = not pre_is_empty
            else:
                pre_is_empty = False
        ss.reverse()
        assert ss[-1]
        assert ss[0]
        assert all(ss[i] or ss[i+1] for i in range(len(ss)-1))
        internal = '/'.join(ss)
        return f'({internal!s})'

SymbolLeadingPath = (Symbol, SymbolLeadingPathAppend)
def check_SymbolLeadingPath(symbol_leading_path, /):
    if not type(symbol_leading_path) in SymbolLeadingPath: raise TypeError

__new__ = mk_new_Symbol('_', '__new__')


#]]]SymbolLeadingPath:end



#[[[OpsMeta:begin

class OpsMeta(type):
    r'''
    #Dynamic_Type_Creation:goto
    bases2 = types.resolve_bases(bases)
    (metaclass, namespace, kwds2) = types.prepare_class(name, bases2, kwds)
    cls = metaclass(name, bases2, namespace, **kwds2)
    #'''
    class key4namespace4OpsMeta:pass
    class key4ops_wrapper4OpsMeta:pass
    class key4bases4OpsMeta:pass
    def __new__(metaclass, name, bases2, namespace, /, *, ops_wrapper, **kwds2):
        d = {'__slots__':('__OpsMeta__cls__sf__私有数据',), __class__.key4ops_wrapper4OpsMeta:ops_wrapper, __class__.key4namespace4OpsMeta:namespace, __class__.key4bases4OpsMeta:bases2}

        sf_as_cls = super(__class__, metaclass).__new__(metaclass, name, (), d, **kwds2)
        return sf_as_cls
    #@classmethod
    #def __get_ops__(metaclass, sf_as_cls, /):
    def __get_ops__(sf_as_cls, /):
        ops_wrapper = sf_as_cls.__dict__[__class__.key4ops_wrapper4OpsMeta]
        return ops_wrapper

    #__dict__
    #__dir__
    r'''
    def ___cmp_halfway___(sf_as_cls, rhs, /):
        if not isinstance(rhs, type):
            rhs = type(rhs)
            if rhs is sf_as_cls: raise TypeError
        if not isinstance(rhs, type): raise logic-err
        return id(sf_as_cls), id(rhs)
    def __lt__(sf_as_cls, rhs, /):
        a, b = type(sf_as_cls).___cmp_halfway___(sf_as_cls, rhs)
        return a < b
    def __gt__(sf_as_cls, rhs, /):
        a, b = type(sf_as_cls).___cmp_halfway___(sf_as_cls, rhs)
        return a > b
    def __le__(sf_as_cls, rhs, /):
        a, b = type(sf_as_cls).___cmp_halfway___(sf_as_cls, rhs)
        return a <= b
    def __ge__(sf_as_cls, rhs, /):
        a, b = type(sf_as_cls).___cmp_halfway___(sf_as_cls, rhs)
        return a >= b
    #'''

    @abstractmethod
    def __getitem__(sf_as_cls, symbol_leading_path_or_symbol_leading_path_and_kwargs, /):
        if type(symbol_leading_path_or_symbol_leading_path_and_kwargs) is tuple:
            to_call = True
            symbol_leading_path_and_kwargs = symbol_leading_path_or_symbol_leading_path_and_kwargs
            L = len(symbol_leading_path_and_kwargs)
            if L < 2:
                symbol_leading_path_and_kwargs += (__new__, ((), {}))[L:]
                L = len(symbol_leading_path_and_kwargs)
                assert L == 2
            assert L >= 2
            #bug: (symbol_leading_path, args_kwargs_pair, *symbol_arg_slices) = symbol_leading_path_and_kwargs
            #   symbol_arg_slices :: list
            #
            (symbol_leading_path, args_kwargs_pair) = symbol_leading_path_and_kwargs[:2]
            symbol_arg_slices = symbol_leading_path_and_kwargs[2:]
            check_SymbolLeadingPath(symbol_leading_path)
            checker4args_kwargs_pair(args_kwargs_pair)
            checker4symbol_arg_slices(symbol_arg_slices)
            symbol2arg = {symbol_as_kw:arg for symbol_as_kw, arg, _ in map(slice2triple, symbol_arg_slices)}
            if len(symbol2arg) != len(symbol_arg_slices): raise KeyError('duplicates')
            (symbol_leading_path, args_kwargs_pair, symbol2arg)

        else:
            to_call = False
            symbol_leading_path = symbol_leading_path_or_symbol_leading_path_and_kwargs
            check_SymbolLeadingPath(symbol_leading_path)
        member = ... #TODO:get ... symbol_leading_path
        if to_call:
            (symbol_leading_path, args_kwargs_pair, symbol2arg)
            args, kwargs = args_kwargs_pair
            result = member(sf_as_cls, symbol2arg, *args, **kwargs)
        else:
            result = member
        return result

    def __call__(sf_as_cls, symbol2arg=None, /, *args, **kwargs):
        if symbol2arg is None:
            symbol2arg = null_mapping_view
        sf_as_ops = sf_as_cls[(__new__, (args, kwargs), *(slice(symbol, arg) for symbol, arg in symbol2arg.items()),)]
        check_type_is(sf_as_ops, sf_as_cls)
        return sf_as_ops
        r'''
>>> {}[:]
Traceback (most recent call last):
    ...
TypeError: unhashable type: 'slice'
>>> s=slice(1,2)
>>> s
slice(1, 2, None)
>>> s.stop=3
Traceback (most recent call last):
    ...
AttributeError: readonly attribute
        #'''
        metaclass = type(sf_as_cls)
        metaclass.___is_abstract_class___(sf_as_cls)
        sf_as_ops = object.__new__(sf_as_cls)
        #sf_as_ops.__dict__ = MapView({})
        #sf_as_ops.__dict = MapView({})
        #print(dir(sf_as_ops))
        #   TypeError: '<' not supported between instances of 'type' and 'str'
        #   eg. key4ops_wrapper4OpsMeta...
        #print(sf_as_ops.__dir__())
        object.__setattr__(sf_as_ops, f'_{sf_as_cls.__name__!s}__OpsMeta__cls__sf__私有数据', MapView({}))
        return sf_as_ops


def _t2():
    class C(metaclass=OpsMeta, ops_wrapper=None):
        pass
    sf = C()
    try:
        sf.xxx=1
    except AttributeError:
        #AttributeError: 'C' object has no attribute 'xxx'
        pass
    else:
        raise logic-err
_t2()

#]]]OpsMeta:end

#[[[zzzwww:begin
#]]]zzzwww:end
#]]]main_body_src_code:end


#HHHHH
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #<BLANKLINE>
    #Traceback (most recent call last):

#################################



