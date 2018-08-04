
'''
why?
    1) ops, obj
    2) mro

    1) ops, obj:
        like Haskell, we may defined an Ops class to operate obj
        class XxxOps:
            def f1(self, obj, ...):pass
            ...
        def func(ops, obj, ...):
            ...
        but, if obj is immutable but requires update,
            obj = ops.modifier(obj, ...) # replace the old obj by new one
            that is too tedious
            
        goback to define a Wrap class to hold referece to obj
        class Wrap:
            def __init__(self, ops, obj):
                self.ops = ops
                self.obj = obj

            def f1(self, ...other):
                other = other.obj
                ...other, others = self.ops(self.obj, ...other)
                other = Wrap(self.ops, other)
                return ...other
        hence why we use ops/obj on earth, just using Wrap/ABC!!??
            package with functions can be overrided
            ????????????
        Ops/Wrap/ABC may be growing class without bound
        we fall to create Mixins
    2) mro
        class MixinC(MixinA, MixinB...) may cause mro error
        we need to reorder them by hand, and sometimes there are no suitable order
        move bases into __mixin_depends__
        class MixinC:
            __mixin_depends__ = (...)
            # donot allow __init__, __new__
            # otherwise is not a mixin anymore; i.e. a concrete class
            
        @NonMinxin
        class A(MixinC, ...):
            ...
                
                
with local2root_module(locals()):
    from ops import ...
with obj2root_module(ops):
    import ...
with local2curr_module(globals(), locals()):
    from .ops import ...
with obj2curr_module(globals(), ops):
    from . import ...
    
'''
'''
other solution:
    @mixins
    class C:pass

'''
from abc import *
from seed.types.ToProcess import UnorderedSetOnce
from seed.graph.U2Vtc_To_DigraphABC import ObjU2Vtc_To_Digraph as Graph
from seed.graph.ordering import postfix_dfs_ordering
from seed.graph.DAG import find_one_cycle, is_DAG


def override(f):
    '''used when there are conflict between base and __class__

class A(B, metaclass=InterfaceMeta):
    # if B.f exists, then override is required
    @override
    def f(self):...
    # if B.g does not exist, then override is forbidden
    def g(self):...
    
'''
    f.__override__ = True
def using(subclass):
    '''used when there are conflicts between bases

class A(B, C, metaclass=InterfaceMeta):
    # if B.f and C.f both exist and "B.__dict__['f'] is not C.__dict__.['f']"
    @using(C)
    def f():pass # here, f just to provide a name
    
'''
    def _(f):
        f.__using__ = subclass
    return f
##def is_abstractmethod(func):
##    return getattr(func, '__isabstractmethod__', False)

def has_abstractmethod(cls, name):
    return name in getattr(cls, '__abstractmethods__', ())

class InterfaceMeta(ABCMeta):
    ''' just copy methods of bases, and discard bases

class Ixxx(A, B, metaclass=InterfaceMeta):
    @override # if A.f or B.f
    def f(self):
        # Ixxx.f
    @using(A) # if A.f and B.f
    def f(self):... # discard
    
    def f(self):... # no A.f or B.f

    @abstractmethod
    def h(self):... # no A.f or B.f

@Ixxx
class C(metaclass=ABCMeta):pass

# if Ixxx.f and Ixxx.g conflict with C.f and C.g
@Ixxx(usings=('f'), deletes=['g']) # but need not h; since it is abstract
class C(metaclass=ABCMeta):
    def f(self):...
    def g(self):...
    def h(self):...

'''
    

    def mro(self):
        return self, object
    def __new__(mcls, name, bases, namespace, **kwds):
        if not all(isinstance(base, __class__) or base is object for base in bases):
            raise TypeError
        self = super().__new__(mcls, name, bases, namespace, **kwds)
        self.__subclasses = set(bases)
        self.__subclasses.update(base.__subclasses for base in bases if base is not object)
        return self
    @classmethod
    def __prepare__(mcls, name, bases, **kwds):
        # staticmethod(if without @) or classmethod
        namespace = {}
        for base in reversed(bases):
            if base is object:
                continue
            namespace.update(vars(base))
        bases = ()
        namespace.update(super().__prepare__(name, bases, **kwds))
        return namespace

    def __subclasscheck__(self, cls):
        return cls in self.__subclasses
    def __call__(self, cls=None, *, usings=(), deletes=()):
        '''
usings = [str]  ; if conflict, use self.f
deletes = [str] ; if confilct, use cls.f
'''
        decorator = self.__make_decorator(usings, deletes)
        if cls is None:
            return decorator
        return decorator(cls)
        # self as decorator ??
        # yes, __call__ takes over __init__ and __new__...
        if not isinstance(cls, ABCMeta):
            # self has some abstractmethods that may be assigned to cls
            # so, cls should be a ABCMeta
            raise TypeError('not abstract class')
    def __make_decorator(self, usings, deletes):
        usings = set(usings)
        deletes = set(deletes)
        if usings & deletes:
            raise ValueError('usings is not disjoint with deletes: {}'
                             .format(usings & deletes))
        
        def decorator(cls):
            given_abstractmethods = set() # names
            for name, value in vars(self).items():
                if not hasattr(cls, name) or name in usings:
                    setattr(cls, name, value)
                    if has_abstractmethod(self, name):
                        given_abstractmethods.add(name)
                elif name in deletes or has_abstractmethod(self, name):
                    # cls.f override abstract self.f
                    pass
                else:
                    raise NameError('name conflict: already exists: {!r}'
                                    .format(name))
            if given_abstractmethods:
                cls.__abstractmethods__ += given_abstractmethods
            self.__subclasses.add(cls)
            return cls
        return decorator
    

class A(metaclass=InterfaceMeta):
    @abstractmethod
    def f(self):pass
class B(A):pass
class C(A, B):pass
print(vars(C))
assert C.__bases__ == (A,B) # (object,)

try:
    C()
    # TypeError: __call__() missing 1 required positional argument: 'cls'
except TypeError:pass
else: raise logic-error
##print(vars(C))
##print(dir(C))
##class C:pass
##print(dir(C))
##print(dir(C()))
##
##def mro(bases):
##    class C:pass
##    C.__bases__ = tuple(bases)
##    return type.mro(C)
##
##print(mro([int, str]))


override_name = '__override_base_pairs__'
def get___override_base_pairs___or_None(cls):
    pairs = getattr(cls, override_name, None)
    if pairs is None:
        # in __new__, no such attr yet
        # but found in __dict__
        pairs = vars(cls).get(override_name, None)
    return pairs
def class2override_base_pairs(cls):
    # pairs = getattr(cls, override_name, None)
    pairs = get___override_base_pairs___or_None(cls)
    if pairs is None or pairs is ...:
        bases = cls.__bases__
        pairs = frozenset(zip(bases, bases[1:]))
        
    return pairs


def class2depend_edges(cls):
    return iter((cls, base) for base in cls.__bases__)


def class2dedges(cls):
    edge_set = set()
    def update(cls):
        edge_set.update(class2depend_edges(cls))
        edge_set.update(class2override_base_pairs(cls))
        return cls.__bases__
    todo = UnorderedSetOnce([cls])
    todo.apply(update)
    #print(edge_set)
    return edge_set

def dedges2mro(root, dedges):
    g = G.from_vertex_pairs(dedges, ())
    if not is_DAG(g):
        raise ValueError('not DAG: {}'.format(find_one_cycle(g)))
    vtc = list(postfix_dfs_ordering(g, [root]))
    vtc.reverse()
    return vtc
    

    



def bases2dedges(bases):
    raise
    # baseclass -> follow_baseclasses only if prev one override some methods
    # NOTE:
    #   dir(cls) : attr from bases and mcls ...
    #   vars(cls) : __weakref__, __doc__, __dict__, _abc_cache, __module__,...
    #   namespace : __doc__, __qualname__, __module__, ...
    d = {}
    es = []
    for base in reversed(bases):
        for name in vars(base): # dir(base):
            
            if name in d:
                # isroutine??????
                es.append(base, d[name])
            d[name] = base
    return es



class MixinMeta(ABCMeta):
    # if just copy methods of bases, and discard bases
    #    then we cannot override and call super().f()
    '''
usage:
    class C(A, B, metaclass=MixinMeta):
        __override_base_pairs__ = ... # as normal
        __override_base_pairs__ = [(B, A)] # __mro__ = C, ..B, ..A, ..object
        __override_base_pairs__ = () # __mro__ : A, B in any order unless A is subclass of B or vice versa

    
mro:
    rules:
    1) subclass -> baseclass
    2) baseclass -> succ_baseclass
        related to ==>>
            baseclass -> follow_baseclasses only if prev one override some methods
    3) should be DAG # lattice

reversed . postfix_dfs_ordering $ DAG


'''
    def mro(self):
        cls = self
        return dedges2mro(cls, class2dedges(cls))
    def __new__(mcls, name, bases, namespace, **kwds):
        # bases are unorder except those in __override_base_pairs__
        # __override_base_pairs__ = [(prev,succ)]
        pairs_name = override_name
        if pairs_name in namespace:
            if namespace[pairs_name] is not ...:
                namespace[pairs_name] = frozenset((a,b) for a,b in namespace[pairs_name])
        else:
            namespace[pairs_name] = ()
        self = super().__new__(mcls, name, bases, namespace, **kwds)
        return self
##    def __init__(self, name, bases, namespace, **kwds):
##        #bases = ()
##        super().__init__(name, bases, namespace, **kwds)
##
##    @property
##    def __override_base_pairs__(self):
##        return 
    
class NotMixinMetaObjT:
    def __call__(self, name, bases, namespace, **kwds):
        if namespace.get(override_name, ...) is not ...:
            raise ValueError('__override_base_pairs__ should be "..."')
        namespace[override_name] = ...
        return MixinMeta(name, bases, namespace, **kwds)
NotMixinMeta = NotMixinMetaObjT()

    
class A(metaclass=MixinMeta):
    @abstractmethod
    def f(self):pass
class B(A):pass
class C(A, B):pass

assert C.__mro__ == (C, B, A, object)
try:
    C()
except:pass
else:raise ...
    

try:
    class D(A, B, metaclass=NotMixinMeta):pass
except: pass
else:
    raise logic-error

class D(B, A, metaclass=NotMixinMeta):pass
assert type(D) is MixinMeta
class D(metaclass=InterfaceMeta):pass
try:
    class E(D, A, metaclass=NotMixinMeta):pass
except: pass
else:
    raise logic-error















