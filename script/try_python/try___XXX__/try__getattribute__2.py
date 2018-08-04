

'''

conclusion:
    * builtins functions (e.g. iter, type, getattr...) will passby C..__getattribute__
        to get '__iter__', 'mro', '__getattribute__',...
            not via __getattribute__ !!!!!!!!
    * how to get C..__getattribute__???????
        # fail: inspect.getattr_static

    * instance dict and class dict should be seperated, see below __f__

implicit lookup those builtins special methods by builtins functions
    (the special method must be set on the class object itself in order to be consistently invoked by the interpreter)
    but how? like D(C)?
        copy C..__iter__ to D..__iter__, but not to D..__dict__['__iter__']??


####################
let x..f be 'f' in x??

class Meta(type, metaclass=MetaMeta)
         MetaMeta..mro(Meta)
class B(metaclass=Meta)
         MetaMeta..__getattribute__(Meta, '__prepare__')
         Meta..mro(B)
         ######### mro not via __getattribute__ !!!!!!!!
class C(B)
         MetaMeta..__getattribute__(Meta, '__prepare__')
         Meta..mro(C)
class D(C)
         MetaMeta..__getattribute__(Meta, '__prepare__')
         Meta..mro(D)
c.__dict__
         C..__getattribute__(self, '__dict__')
         ######### __getattribute__ not via __getattribute__ !!!!!!!!
c.__getattribute__
         C..__getattribute__(self, '__getattribute__')
c.__iter__()
         C..__getattribute__(self, '__iter__')
         C..__iter__(self)
c.__getattribute__(__iter__)()
         C..__getattribute__(self, '__getattribute__')
         C..__getattribute__(self, '__iter__')
         C..__iter__(self)
getattr(c, __iter__)()
         C..__getattribute__(self, '__iter__')
         C..__iter__(self)
iter(c)
         C..__iter__(self)
         ######### __iter__ not via __getattribute__ !!!!!!!!

c.f()
         C..__getattribute__(self, 'f')
         C..f(self)
getattr(c, __getattribute__)
         C..__getattribute__(self, '__getattribute__')
inspect.getattr_static(C, __getattribute__)
         Meta..__getattribute__(C, '__dict__')
inspect.getattr_static(D, __getattribute__)
         Meta..__getattribute__(D, '__dict__')
         Meta..__getattribute__(C, '__dict__')
iter(d)
         C..__iter__(self)
d.__dict__
         C..__getattribute__(self, '__dict__')
assert not d.__dict__
         C..__getattribute__(self, '__dict__')

c.__f__
         C..__getattribute__(self, '__f__')
         C..__f__(self); not override by Meta..__f__
C.__f__(c)
         Meta..__getattribute__(C, '__f__')
         Meta..__f__(C); override self..__f__
         Meta..__f__..__f__(instance)
         # this the normal usage of __f__
         # but Meta itself may require __f__ (no as property)
         # so instance dict and class dict should be seperated
'''


def get_name(cls):
    # to avoid __getattribute__ when cls.__name__
    qname = repr(cls).split("'")[1]
    name = qname.split('.')[-1]
    return name

__iter__ = '__iter__'
__getattribute__ = '__getattribute__'
old_print = print
def print_tab(*args):
    old_print('\t', *args)
print = print_tab


class MetaMeta(type):
    def __getattribute__(self, name):
        print("MetaMeta..__getattribute__({self}, {name!r})"
            .format(self=get_name(self), name=name))
        return type.__getattribute__(self, name)
    def mro(self):
        print("MetaMeta..mro({self})"
            .format(self=get_name(self)))
        return super().mro()



old_print('class Meta(type, metaclass=MetaMeta)')
class Meta(type, metaclass=MetaMeta):
    def __getattribute__(self, name):
        print("Meta..__getattribute__({self}, {name!r})"
            .format(self=get_name(self), name=name))
        return type.__getattribute__(self, name)
    def __iter__(self):
        print("Meta..__iter__({self})"
            .format(self=get_name(self)))
        return iter('')
    def f(self):
        print("Meta..f({self})"
            .format(self=get_name(self)))
    def mro(self):
        print("Meta..mro({self})"
            .format(self=get_name(self)))
        return super().mro()
    @property
    def __f__(self):
        print("Meta..__f__({self}); override self..__f__"
            .format(self=get_name(self)))
        def __f__(instance):
            print('Meta..__f__..__f__(instance)')
            return
        return __f__

old_print('class B(metaclass=Meta)')
class B(metaclass=Meta):pass

old_print('class C(B)')
class C(B):
    def __getattribute__(self, name):
        print("C..__getattribute__(self, {name!r})".format(name=name))
        return object.__getattribute__(self, name)
    def __iter__(self):
        print("C..__iter__(self)")
        return iter('')
    def f(self):
        print("C..f(self)")
    def __f__(self):
        print("C..__f__(self); not override by Meta..__f__")
        return
old_print('class D(C)')
class D(C):pass



def t1():
    print = old_print
    c = C()
    print('c.__dict__')
    c.__dict__

    print('c.__getattribute__')
    c.__getattribute__

    print('c.__iter__()')
    c.__iter__()

    print('c.__getattribute__(__iter__)()')
    c.__getattribute__(__iter__)()

    print('getattr(c, __iter__)()')
    getattr(c, __iter__)()

    print('iter(c)')
    iter(c)

    print('c.f()')
    c.f()

    print('getattr(c, __getattribute__)')
    getattr(c, __getattribute__)

    import inspect
    print('inspect.getattr_static(C, __getattribute__)')
    inspect.getattr_static(C, __getattribute__)

    print('inspect.getattr_static(D, __getattribute__)')
    inspect.getattr_static(D, __getattribute__)


    d = D()
    print('iter(d)')
    iter(d)

    print('d.__dict__')
    d.__dict__
    print('assert not d.__dict__')
    assert not d.__dict__


    print('c.__f__')
    c.__f__()

    print('C.__f__(c)')
    C.__f__(c)

t1()











































