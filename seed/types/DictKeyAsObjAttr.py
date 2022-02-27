
# from seed.types.DictKeyAsObjAttr import DictKeyAsObjAttr, DictKeyAsObjAttrAndAsMapping

__all__ = '''
    DictKeyAsObjAttr
    DictKeyAsObjAttrAndAsMapping
    '''.split()

class DictKeyAsObjAttr:
    __slots__ = '_g'
    def __init__(self, globals, /):
        #self.globals = globals
        _set(self, globals)
    def __setattr__(self, name, value, /):
        raise AttributeError(name)
    def __getattribute__(self, name, /):
        #d = object.__getattribute__(self, 'globals')
        d = _get(self)
        try:
            return d[name]
        except KeyError:
            raise AttributeError(name)
    def __dir__(self, /):
        #d = object.__getattribute__(self, 'globals')
        d = _get(self)
        return sorted(k for k in d if k.isidentifier())
_g = DictKeyAsObjAttr._g
del DictKeyAsObjAttr._g
_get = _g.__get__
_set = _g.__set__
del _g

class DictKeyAsObjAttrAndAsMapping(DictKeyAsObjAttr):
    r'''
    no: .keys(), .values(), .items()
    #'''
    __slots__ = ()
    def __getitem__(self, key, /):
        #d = object.__getattribute__(self, 'globals')
        d = _get(self)
        return d[key]
    def __contains__(self, key, /):
        #d = object.__getattribute__(self, 'globals')
        d = _get(self)
        return key in d
    def __len__(self, /):
        #d = object.__getattribute__(self, 'globals')
        d = _get(self)
        return len(d)
    def __bool__(self, /):
        #d = object.__getattribute__(self, 'globals')
        d = _get(self)
        return bool(d)
    def __iter__(self, /):
        #d = object.__getattribute__(self, 'globals')
        d = _get(self)
        return iter(d)

assert 'a' not in DictKeyAsObjAttrAndAsMapping({})
assert 'a' in DictKeyAsObjAttrAndAsMapping({'a':1})

from seed.types.DictKeyAsObjAttr import DictKeyAsObjAttr, DictKeyAsObjAttrAndAsMapping

