'''

len(obj) is not obj.__len__() # since __len__ may in __dict__
    def is_special_name(name):
        return '__' == name[:2] == name[-2:]
    def call_method(obj, name, ...):
        if is_special_name(name):
            return getattr(type(obj), name)(obj, ...)
        return getattr(obj, name)(...)

x.name == getattr(x, 'name')

def getattr(obj, name):
    if obj is type:
        try:
            return the builtin-funcs[name]
        except KeyError:
            raise AttributeError()
    try:
        return getattr(type(obj), '__getattribute__', 
                        default_getattribute)(x, name)
    except AttributeError:
        return getattr(type(obj), '__getattr__')(x, name)

def default_getattribute(obj, name):
    dict = get_slot(obj, '__dict__', {}) # __dict__ not in __dict__
    if name in dict:
        return dict[name]
    elif name is a attr of supertypes of type(obj):
        r = that type attr
        if isfunction(r):
            r = bind(r, x)
        return r
    raise AttributeError()
    


    

'''
class Meta(type):
   def __getattribute__(*args):
      print("Metaclass getattribute invoked")
      # print(args) self, name where self is a class
      return type.__getattribute__(*args)

class C(object, metaclass=Meta):
    def __(self):
        return 10
    def ___(self):
        return 10
    def ____len____(self):
        return 10
    def __len__(self):
        return 10
    def __getattribute__(*args):
        print("Class getattribute invoked")
        return object.__getattribute__(*args)

c = C()
c.__len__()                 # Explicit lookup via instance
#Class getattribute invoked

C.__len__
#Metaclass getattribute invoked
type(c).__len__(c)
#Metaclass getattribute invoked


class C(object, metaclass=Meta):
    __ = 'cls.__'

c = C()
assert c.__ == 'cls.__'
c.__ = 'dict.__'
assert c.__ == 'dict.__'


class C(object, metaclass=Meta):
    ____ = 'cls.____'

c = C()
assert c.____ == 'cls.____'
c.____ = 'dict.____'
assert c.____ == 'dict.____'


class C(object, metaclass=Meta):
    __x__ = 'cls.__x__'
    __len__ = 'cls.__len__'

c = C()
assert c.__x__ == 'cls.__x__'
c.__x__ = 'dict.__x__'
assert c.__x__ == 'dict.__x__'
assert c.__len__ == 'cls.__len__'
c.__len__ = 'dict.__len__'
assert c.__len__ == 'dict.__len__'



raise








def show_ret(s):
    print(s)
    return s



def qual(self, this_class, func_name, attr_name):
    return '.'.join(
        [type(self).__class__.__name__, this_class.__name__,
         func_name, attr_name])
    
class A:
    cls = 'cls_attr'
    def __getattr__(self, name):
        s = qual(self, __class__, '__getattr__', name)
        return show_ret(s)
    

class B(A):
    cls = 'cls_attr'
    def __getattribute__(self, name):
        s = qual(self, __class__, '__getattribute__', name)
        return show_ret(s)

    def __getattr__(self, name):
        s = qual(self, __class__, '__getattr__', name)
        return show_ret(s)

class C(A):
    def __getattribute__(self, name):
        s = qual(self, __class__, '__getattribute__', name)
        print(s, 'AttributeError')
        raise AttributeError()

class D(B):
    def __getattribute__(self, name):
        s = qual(self, __class__, '__getattribute__', name)
        print(s, 'AttributeError')
        raise AttributeError()

class E(A):
    def __getattribute__(self, name):
        s = qual(self, __class__, '__getattribute__', name)
        print(s, 'AttributeError')
        raise AttributeError()
    def __getattr__(self, name):
        s = qual(self, __class__, '__getattr__', name)
        return show_ret(s)

class F(B):
    def __getattribute__(self, name):
        s = qual(self, __class__, '__getattribute__', name)
        print(s, 'AttributeError')
        raise AttributeError()
    def __getattr__(self, name):
        s = qual(self, __class__, '__getattr__', name)
        return show_ret(s)
    


for cls in [A, B, C, D, E, F]:
    o = cls()
    print(cls)
    o.dict = 'dict_attr'
    print('.cls =', o.cls)
    print('.dict =', o.dict)
    print('.missing =', o.missing)

    o.cls = 'dict_over_cls_attr'
    print('.cls (dict_over_cls) =', o.cls)
    print('\n'*2)












































