

class ToValueBase:
    # Value is ModM or Uint
    
    
    @classmethod
    def is_finite(cls):
        if issubclass(cls, ValueBase):
            raise NotImplementedError()

        assert issubclass(cls.V, ValueBase)
        if cls is not cls.V:
            return cls.V.is_finite()
        else:
            raise logic-error
        
        raise NotImplementedError()
    
    @classmethod
    def from_value(cls, v):
        assert isinstance(v, cls.V)
        return cls._from_value(v)
    
    def to_value(self):
        v = self._to_value()
        assert isinstance(v, cls.V)
        return v
    
    @classmethod
    def _from_value(cls, v):
        raise NotImplementedError()
    
    def _to_value(self):
        raise NotImplementedError()
    
    pass

class ValueBase:
    
    @classmethod
    def _from_value(cls, v):
        return v
    def _to_value(self):
        return self


    def __eq__(self, other):
        if type(self) is not type(other):
            raise NotImplemented
        return self.n == other.n
    def __ne__(self, other):
        return not (self == other)


class ModBase(ValueBase):pass
Mod_basename = 'Mod'
Mod_name_tpl = '{basename}{M}'
Mod_constructor_tpl = '{basename}({M})'
Mod_class_tpl = r'''
class {name}(ModBase, ToValueBase):
    __slots__ = ('n',)
    M = {M}
    V = None #{name}
    constructor_str = {constructor!r}
    
    assert M > 0
    
    def __init__(self, n):
        assert 0 <= n < self.M
        self.n = n
        pass

    @classmethod
    def is_finite(cls):
        return True

    def __repr__(self):
        return self.constructor_str + '({{}})'.format(self.n)
    pass

    
{name}.V = {name}
    
'''

def make_class(name_tpl, constructor_tpl, class_tpl, **kwargs):
    name = name_tpl.format(**kwargs)
    g = globals()
    
    if name not in g:
        constructor = constructor_tpl.format(name=name, **kwargs)
        print(constructor)
        print(kwargs)
        src = class_tpl.format(name=name, constructor=constructor, **kwargs)
        print(src)
        exec(src, g)

    t = g[name]
    return t

def Mod(M):
    assert M > 0
    return make_class(Mod_name_tpl, Mod_constructor_tpl, Mod_class_tpl,
                      M=M, basename=Mod_basename)



#print(make_ModN_class(6))
print(Mod(6))

class Uint(ValueBase, ToValueBase):
    __slots__ = ('n',)
    V = None
    constructor_str = 'Uint'
    
    def __init__(self, n):
        assert 0 <= n
        self.n = n
        return

    
    
    @classmethod
    def is_finite(cls):
        return False
    
    pass
Uint.V = Uint


Array_basename = 'Array'
Array_name_tpl = '{basename}{N}_{T.__name__}'
Array_constructor_tpl = '{basename}({N}, {T.__name__})'
Array_class_tpl_head = r'''

class {name}(ToValueBase):
    __slots__ = ('ts',)
    T = {T.__name__}
    N = {N}
    V = {V.__name__}
    constructor_str = {constructor!r}
    
    def __init__(self, ts):
        self.ts = tuple(ts)
        assert len(self.ts) == self.N
        assert all(isintance(t, T.__name__) for t in self.ts)
        return
        
    def __repr__(self):
        return self.constructor_str + '({{}})'.format(self.ts)
'''

Array_N0_class_tpl_tail = r'''
    assert N == 0
    assert V is Mod(1)
    @classmethod
    def _from_value(cls, v):
        return cls(())
    def _to_value(self):
        return self.V(0)
    
'''

Array_finite_class_tpl_tail = r'''
    assert N > 0
    assert V.is_finite()
    assert T.is_finite()
    
    @classmethod
    def _from_value(cls, v):
        assert cls.T.V.M == v.M
        us = uint2radix(cls.N, v.M, v.n)
        ts = tuple(cls.T.from_value(cls.T.V(u)) for u in us)
        return {name}(ts)
        
    def _to_value(self):
        us = tuple(t.to_value().n for t in self.ts)
        v = radix2uint(self.N, cls.T.V.M, us)
        return v
    
'''


Array_infinite_class_tpl_tail = r'''
    assert N > 0
    assert not V.is_finite()
    assert not T.is_finite()
    Vec = Vector(Uint, 0, N+1)
    
    @classmethod
    def _from_value(cls, v):
        vec = Vec.from_value(v)
        us = [t.n for t in vec.ts]
        if us: us[-1] += 1
        us += [0] * (cls.N - len(us))
        
        ts = tuple(cls.T.from_value(cls.T.V(u)) for u in us)
        return {name}(ts)
        
    def _to_value(self):
        us = [t.to_value().n for t in self.ts]
        while us and not us[-1]: us.pop()
        if us: us[-1] -= 1
        
        ts = tuple(Vec.T.from_value(Vec.T.V(u)) for u in us)
        vec = Vec(ts)
        v = vec.to_value()
        return v
    
'''


def uint2radix(L, base, n):
    assert L >= 0
    assert base >= 1
    assert 0 <= n < base**L

    if L == 0:
        return []
    if base == 1:
        return [0] * L
        
    ls = []
    while n:
        n, r = divmod(n, base)
        ls.append(r)

    assert len(ls) <= L
    ls += [0] * (L - len(ls))

    return ls

def radix2uint(L, base, ns):
    assert len(ns) == L
    assert all(0 <= n < base for n in ns)

    u = 0
    iter_ns = reversed(ns)
    for n in iter_ns:
        if n:break
    else:
        return u

    for n in iter_ns:
        u *= base
        u += n
    return u


def Array(N, T):
    assert N >= 0

    is_finite = N == 0 or T.is_finite()

    if N == 0:
        Array_class_tpl_tail = Array_N0_class_tpl_tail
        m = 1
        V = Mod(m)
    elif is_finite:
        Array_class_tpl_tail = Array_finite_class_tpl_tail
        m = T.V.M ** N
        V = Mod(m)
    else:
        Array_class_tpl_tail = Array_infinite_class_tpl_tail
        V = Uint

    Array_class_tpl = Array_class_tpl_head + Array_class_tpl_tail
    return make_class(Array_name_tpl, Array_constructor_tpl, Array_class_tpl,
                      N=N, T=T, V=V,
                      basename=Array_basename, is_finite=is_finite)

def Vector(T, L=0, U=None):
    assert L >= 0
    assert U is None or L < U
    is_finite = U == 1 or (U is not None and T.is_finite())

print(Array(N=3, T=Uint))
print(Array(N=3, T=Uint)([Uint(2)]*3))

    
