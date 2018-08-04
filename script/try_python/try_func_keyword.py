
'''
we can not:
    f(self, a, **kw)
    self.f(a, self=1) # Error
'''

def f(a, **kw):
    return a+kw['a']
try:
    f(1, a=2)
    # TypeError: f() got multiple values for argument 'a'
except TypeError:pass
else: raise

class C:
    def f(a, **kw):
        return a+kw['a']
    def g(self, *a, **kw):
        print(a)
        print(kw)
c = C()
c.g(a=(2,), kw={}) # a=(), kw = {'a': (2,), 'kw': {}}
try:
    c.f(a=(2,))
except TypeError:pass
else: raise
try:
    c.f(a=2)
    # TypeError: f() got multiple values for argument 'a'
except TypeError:pass
else: raise

