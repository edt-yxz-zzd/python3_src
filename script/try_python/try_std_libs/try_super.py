
'''
1) super(type, type) ==>> super(type, type as subcls not subobj)
2) ERROR: def f():return super()
'''


#################
class A:
    def f():pass
    def h():pass
class B(A):pass
class C:
    def f():pass
class D(C,B):pass


a = A()
b = B()
c = C()
d = D()

#fail: f = super(D).f
assert C.f is super(D, D).f
assert A.f is super(C, D).f




##################
ls = []
class D1(dict):
    def __setitem__(self, key, value):
        print('D1'); ls.append(1)
        super().__setitem__(key, value)
class D2(dict):
    def __setitem__(self, key, value):
        print('D2'); ls.append(2)
        super().__setitem__(key, value)
class D3(D2, D1):
    def __setitem__(self, key, value):
        print('D3'); ls.append(3)
        super().__setitem__(key, value)
        # will print 'D3 D2 D1'


D3()[4] = 6
assert ls == [3,2,1]





##################

from abc import ABCMeta
# super(supercls, obj) v.s. super(supercls, cls)
# it seems to treat as cls before obj
assert super(type, type).__repr__ is object.__repr__
assert super(type, ABCMeta).__repr__ is object.__repr__


from collections.abc import Mapping, Set, Hashable
# d = super(Mapping, {'a':3})
#   TypeError: super(type, obj): obj must be an instance or subtype of type
#assert isinstance(d, Mapping)




#################

old_super = super
def _t():
    # def super(): return old_super() # RuntimeError: super(): no arguments

    class U:
        @classmethod
        def f(cls):return 1
    class V(U):
        @classmethod
        def f(cls):return super().f()+1
        @classmethod
        def g(cls):return super(__class__, cls).f()+1
    class W(V):
        @classmethod
        def f(cls):return super().f()+1
        @classmethod
        def g(cls):return super(__class__, cls).f()+1
    assert W().f() == 3
    assert W().g() == 3
_t()



