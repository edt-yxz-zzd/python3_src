
def test_from_freefunc():
    class A:pass
    def f(self):
        return 3

    A.g = f
    a = A()
    assert a.g() == 3 
test_from_freefunc() # success!!

def test_from_other_method():
    class A:pass
    class B:
        def f(self):
            return 3

    A.g = B.f
    a = A()
    assert a.g() == 3 

test_from_other_method() # success!!
