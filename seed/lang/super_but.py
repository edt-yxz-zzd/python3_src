


'''
# How to Incorporate a Non-cooperative Class
adapter class
class Root:
    def f(self, x, y):pass
class B:
    def f(self, x):pass
class C(B,Root):
    def f(self, x,y):...
# error:
    class D(B,Root):
        def f(self, x,y):
            # Error:
            #   super().f(x,y)
            #       # B.f(x,y) raise
            #   super(B).f(x,y)
            #       # if type(self)==E: super(B).f is Root.f instead of C.f
class _B(B):
    def f(self, x,y):
        f = super().f
        if f is B.f:
            f = super(B).f
        return f(x,y)
class D(_B, Root):
    def f(self, x,y):
        return super().f(x,y)
class E(D,C):pass

'''

from weakref import WeakKeyDictionary
#from seed.helper.repr_input import repr_helper



__getattribute__ = object.__getattribute__
def getattribute(obj, name):
    return type(obj).__getattribute__(obj, name)

# cache for make_clean_type
meta_cls2supercls2but_types2clean_type = WeakKeyDictionary()
def _setdefault(d, key, f, *args):
    if key in d:
        return d[key]
    r = d[key] = f(*args)
    return r
def _get(metacls, cls, supercls, but_types, f):
    d = meta_cls2supercls2but_types2clean_type
    d = _setdefault(d, (metacls, cls), WeakKeyDictionary)
    d = _setdefault(d, supercls, dict)
    r = _setdefault(d, but_types, _make_clean_type, metacls, cls, supercls, but_types)
    return r
def make_clean_type(metacls, cls, supercls, but_types):
    if not issubclass(cls, supercls): raise TypeError
    but_types = frozenset(but_types)
    return _get(metacls, cls, supercls, but_types)
def _make_clean_type(metacls, cls, supercls, but_types):
    # assert issubclass(cls, supercls)
    # assert supercls is not object
    # need not: but_types <= mro
    assert type(but_types) is frozenset

    mro = cls.__mro__ # (..., object)
    i = mro.index(supercls)
    cleared_mro = (t for t in mro[i+1:] if t not in but_types)
    clean_type = metacls('T', cleared_mro, {})
    return clean_type
def clean_type_super_get(clean_type):
    return super(clean_type, clean_type).__getattribute__
class SuperBut:
    def __init__(self, metacls, cls, supercls, but_types):
        #type2prev_sibling = dict(zip(mro[1:], mro))
        # clean_type, but_types = make_clean_type_ex(cls, supercls, but_types)
        clean_type = make_clean_type(metacls, cls, supercls, but_types)

        self.clean_type_super_get = clean_type_super_get(clean_type)
        '''
        self.cls = cls
        self.supercls = supercls
        self.but_types = but_types
        '''
    def __getattribute__(self, name):
        get = __getattribute__(self, 'clean_type_super_get')
        return get(name)
    '''
    def get_cls(self):
        return self.__dict__['cls']
    def get_supercls(self):
        return self.__dict__['supercls']
    def get_but_types(self):
        return self.__dict__['but_types']
    def get_args(self):
        d = __getattribute__(self, '__dict__')
        return (d['cls'], d['supercls'], d['but_types'])
    def __repr__(self):
        return repr_helper(self, *self.get_args())
    '''


def super_get_but(cls, supercls, but_types, *, metacls=None):
    if metacls is None: metacls = type(cls)
    clean_type = make_clean_type(metacls, cls, supercls, but_types)
    super_get = clean_type_super_get(clean_type)
    return super_get
def super_but(cls, supercls, but_types, *, metacls=None):
    if metacls is None: metacls = type(cls)
    return SuperBut(metacls, cls, supercls, but_types)



