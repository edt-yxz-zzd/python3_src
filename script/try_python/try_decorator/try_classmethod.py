

class C:
    @classmethod
    def f(cls, a):
        return a


assert C.f(1) == 1 # instead of C.f(C, a) !!

assert type(C()).f(1) == 1

