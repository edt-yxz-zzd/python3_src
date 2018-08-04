'''
every class will become a base class of a metaclass.
'''


def t1():
    class B:
        def f(self):pass
    class Meta(B, type):pass
    class M(metaclass=Meta):pass
    class C(M):pass
    class D(B,M):pass

    c = C()
    d = D()
    assert D.f is B.f is Meta.f
    assert M.f is not B.f
    assert C.f is not M.f
    assert C.f is not B.f
    print(C.f, M.f, d.f)
        # <bound method B.f of <class '__main__.C'>>
        # <bound method B.f of <class '__main__.M'>>
        # <bound method B.f of <__main__.D object at 0x00000000037B2A20>>


    d.f
    try:
        c.f # AttributeError: 'C' object has no attribute 'f'
    except AttributeError:pass
    else:  raise
t1()

#################

def t2():
    class B:
        @property
        def data(self):
            return 0
        def f(self):pass
        def __f__(self):return 0
    class Meta(B, type):
        @property
        def data(self):
            return 1
        def f(self):pass
        def __f__(self):return 1
    class M(metaclass=Meta):pass
    class C(B):pass
    class D(B,M):pass
    class E(M,B):pass
    class F(M):pass
    assert B.data is C.data is not D.data == E.data ==     F.data == 1
    assert B.f    is C.f    is     D.f    is E.f    is not F.f
    # C@.data is not D.data is     F.data
    # C@.f    is     D@.f   is not F.f
    #(B.data) # <property object at 0x0000000003785728>
    #(B.f)    # <function t2.<locals>.B.f at 0x0000000003763730>
    #(F.f)    # <bound method t2.<locals>.B.f of <class '__main__.t2.<locals>.F'>>

    b = B()
    c = C()
    d = D()
    e = E()
    f = F()
    assert b.data == c.data == d.data == e.data == 0 # no f.data
    try:
        f.data
    except AttributeError:pass
    else: raise

    ####
    def __f__(obj, *args, **kwargs):
        assert isinstance(obj, B)
        return type(obj).__f__(obj, *args, **kwargs)

    assert             __f__(D) == __f__(E) == __f__(F) == 1 # no __f__(C)
    assert __f__(c) == __f__(d) == __f__(e)             == 0 # no __f__(f)

    try:
        __f__(C) # fail at: isinstance(obj, B)
    except AssertionError:pass
    else: raise
    try:
        __f__(f) # fail at: isinstance(obj, B)
    except AssertionError:pass
    else: raise




    #############
    def __f2__(obj, *args, **kwargs):
        return type(obj).__f__(obj, *args, **kwargs)
    try:
        __f2__(f) # TypeError: __f__() takes 1 positional argument but 2 were given
    except TypeError:pass
    else: raise
t2()


