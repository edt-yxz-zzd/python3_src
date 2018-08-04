
'''
mro:
    rules:
    1) subclass -> baseclass
    2) prev_baseclass of topmost -> succ_baseclass of topmost
    3) should be DAG
    
'''

from seed.debug.assert_except import assert_except
from abc import *

def test1():
    class A:pass
    class B(A):pass
    def f():
        class C(A, B):pass
        ##    class C(A, B):pass
        ##TypeError: Cannot create a consistent method resolution
        ##order (MRO) for bases A, B

    assert_except(TypeError, f)
test1()

def test2():
    class A(metaclass=ABCMeta):pass
    class B(A):pass
    def f():
        class C(A, B):pass
        ##    class C(A, B):pass
        ##TypeError: Cannot create a consistent method resolution
        ##order (MRO) for bases A, B

    assert_except(TypeError, f)
test2()

def test3():
    class A(metaclass=ABCMeta):pass
    class B(A):pass
    class C(A):pass
    class D(B,C):pass
    #print(D.mro())
    assert D.mro() == [D, B, C, A, object]

test3()

def test4():
    class A(metaclass=ABCMeta):pass
    class B(A):pass
    class C(A):pass
    class D(B,C):pass
    class E(C,B):pass
    #class F(D, E):pass
    def f():
        class F(D, E):pass
    assert_except(TypeError, f)
##        TypeError: Cannot create a consistent method resolution
##        order (MRO) for bases B, C

test4()
