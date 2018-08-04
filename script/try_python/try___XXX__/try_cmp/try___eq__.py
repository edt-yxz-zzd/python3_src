
class A:
    def __eq__(self, other):
        print('A.__eq__')
        return NotImplemented
    def __ne__(self, other):
        print('A.__ne__')
        return NotImplemented


class B:
    def __eq__(self, other):
        print('B.__eq__')
        return NotImplemented
    def __ne__(self, other):
        print('B.__ne__')
        return NotImplemented

class C:
    def __eq__(self, other):
        print('C.__eq__')
        return self is other
    def __ne__(self, other):
        print('C.__ne__')
        return self is not other


print('A() == B()', A() == B())
print('A() == C()', A() == C())
print('A() != B()', A() != B())
print('A() != C()', A() != C())

