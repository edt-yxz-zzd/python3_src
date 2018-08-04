

from abc import ABCMeta, abstractmethod
# what about classproperty ??

classproperty = property
class C(metaclass=ABCMeta):
    __slots__ = ()
    @property
    @abstractmethod
    def p(self):
        ...


class D(C):
    __slots__ = ()
    p = 'p'

d = D() # not abc?? yes
# d.p = 'af' # read-only
# d.a = 'adf' # test abc.__dict__ no attribute 'a'

# C() # abc Can't instantiate



class SomeTpl(type):
    __slots__ = ()
    @property
    def required_classproperty(self):
        return 'required_classproperty'


class C(metaclass=SomeTpl):
    __slots__ = ()

print(C.required_classproperty) # required_classproperty
#print(C.afsf) # no attribute


c = C()
#print(type(C)) # SomeTpl
#print(dir(c))
#print(c.required_classproperty) # no attribute 




# what is __abstractmethods__??

class myMeta(type):
    def __new__(mcls, name, bases, namespace):
        cls = super().__new__(mcls, name, bases, namespace)

        # no doc for __abstractmethods__ !!!
        cls.__abstractmethods__ = frozenset(['af'])
        return cls


class C(metaclass=myMeta):
    __slots__ = ()


# C() # Can't instantiate


class alias_attr:
    def __init__(self, attr):
        #self.obj = obj
        self.attr = attr
    def __get__(self, obj, owner):
        if obj is None:
            #print('obj is None')
            # at type(obj).attr
            # but .__dict__ not call me!!
            return self
        else:
            #print('get attr', self.attr)
            return getattr(obj, self.attr)
    def __set__(self, obj, value):
        return setattr(obj, self.attr, value)
    def __delete__(self, obj):
        return delattr(obj, self.attr)
        
class alias_class_attr:
    def __init__(self, attr):
        #self.obj = obj
        self.attr = attr
    def __get__(self, obj, owner):
        return getattr(owner, self.attr)
    def __set__(self, obj, value):
        return setattr(obj, self.attr, value)
    def __delete__(self, obj):
        return delattr(obj, self.attr)
    
    

class InstantiateHook(ABCMeta):
    #__slots__ = ('____abstractmethods__',)
    _dict = {}
    __dict__ = when_obj_is_None = alias_attr('_dict')
    def _set(self_type, x):
        self_type.at_set()
        #self_type.__dict__['__abstractmethods__'] = x
        vars(self_type)['__abstractmethods__'] = x
        # recur: setattr(self_type, '__abstractmethods__', x)
        self_type.____abstractmethods__ = x
        
    def _del(self_type):
        self_type.at_del()
        del vars(self_type)['__abstractmethods__']
        del self_type.____abstractmethods__
    def _get(self_type):
        self_type.at_get()
        return self_type.____abstractmethods__
    __abstractmethods__ = property(_get, _set, _del)

    def at_set(self_type):
        print('_set')
    def at_get(self_type):
        print('_get')
    def at_del(self_type):
        print('_del')
    def __new__(mcls, name, bases, namespace):
        cls = super().__new__(mcls, name, bases, namespace)
        cls.__dict__ = dict(vars(cls))
        return cls
##        #cls.____abstractmethods__ =

assert InstantiateHook.when_obj_is_None is None
# fail !!! assert InstantiateHook.__dict__ is None
print('InstantiateHook.__dict__', InstantiateHook.__dict__)
classproperty = property
class C(metaclass=InstantiateHook):
    __slots__ = ()
    @property
    @abstractmethod
    def p(self):
        ...

print(type(C))
assert C.__abstractmethods__ == frozenset({'p'})
print('why success')
C() # why success ??? should be in __dict__????
C.__abstractmethods__ = frozenset({'p'})
C()
class D(C):
    __slots__ = ()
    p = 'p'

print(type(D))
d = D() # not abc?? yes
D.__abstractmethods__ = frozenset({'p'})
D()














class SomeTpl(type):
    __slots__ = ()
    def __new__(mcls, name, bases, namespace):
        cls = super().__new__(mcls, name, bases, namespace)
        # Compute set of required classproperty names

        decorateds_name = '__classproperties__'
        is_decorated = lambda obj: getattr(obj, "__isclassproperty__", False)
        get_decorateds = lambda Base: getattr(Base, decorateds_name, set())
        decorated_attr_names = {name for name, value in namespace.items()
                                if is_decorated(value)}
        for base in bases:
            for attr_name in get_decorateds(base):
                value = getattr(cls, attr_name, None)
                if is_decorated(value):
                    decorated_attr_names.add(attr_name)

        decorated_attr_names = frozenset(decorated_attr_names)
        setattr(cls, decorateds_name, decorated_attr_names)
        cls.__abstractmethods__ = decorated_attr_names
        
class C(metaclass=SomeTpl):
    __slots__ = ()



        




