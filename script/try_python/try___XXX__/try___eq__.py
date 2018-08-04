
class A:
    def __eq__(self, other): return NotImplemented

a = A()
b = A()
assert (a == a) is True
assert (a != a) is False

assert (a == b) is False
assert (a != b) is True

assert (a == 1) is False
assert (a != 1) is True



class C:
    def __eq__(self, other):
        raise TypeError
    def __hash__(self):
        return id(self)
c = C()
try:
    c == c
except TypeError:
    pass
else:
    raise logic-error

assert c in {c}


class C:
    def __eq__(self, other):
        raise Exception
    def __hash__(self):
        return id(self)
c = C()
assert c in {c}


class C:
    def __eq__(self, other):
        raise BaseException
    def __hash__(self):
        return id(self)
c = C()
assert c in {c}

try:
    raise BaseException
except:
    pass
else:
    raise logic-error

