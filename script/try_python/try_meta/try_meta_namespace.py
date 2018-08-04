

class Meta(type):
    def __new__(mcls, name, bases, namespace, **kwds):
        self = super().__new__(mcls, name, bases, namespace, **kwds)
        print(namespace)
        return self

class A(metaclass=Meta):
    ''
    def f(self):pass

##
##{'f': <function A.f at 0x0000000003750840>,
## '__module__': '__main__',
## '__qualname__': 'A'}
