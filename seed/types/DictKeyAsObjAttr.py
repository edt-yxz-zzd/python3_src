#__all__:goto
r'''[[[
py -m nn_ns.app.debug_cmd   seed.types.DictKeyAsObjAttr
py -m seed.types.DictKeyAsObjAttr

from seed.types.DictKeyAsObjAttr import DictKeyAsObjAttr, DictKeyAsObjAttrAndAsMapping, SetAsNamespace, SetAsNamespaceAndAsMapping, namespace5iterable, namespace5names_str


#]]]'''
__all__ = r'''
    DictKeyAsObjAttr
    DictKeyAsObjAttrAndAsMapping
    SetAsNamespace
    SetAsNamespaceAndAsMapping
    namespace5iterable
    namespace5names_str
'''.split()#'''
__all__



from seed.helper.repr_input import repr_helper


class DictKeyAsObjAttr:
    __slots__ = '_g'
    def __repr__(self, /):
        d = _get(self)
        return repr_helper(self, d)
    def __init__(self, mapping, /):
        #self.mapping = mapping
        _set(self, mapping)
    def __setattr__(self, name, value, /):
        raise AttributeError(name)
    def __delattr__(self, name, /):
        raise AttributeError(name)
    def __getattribute__(self, name, /):
        #d = object.__getattribute__(self, 'mapping')
        d = _get(self)
        try:
            return d[name]
        except KeyError:
            raise AttributeError(name)
    def __dir__(self, /):
        #d = object.__getattribute__(self, 'mapping')
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
        #d = object.__getattribute__(self, 'mapping')
        d = _get(self)
        return d[key]
    def __contains__(self, key, /):
        #d = object.__getattribute__(self, 'mapping')
        d = _get(self)
        return key in d
    def __len__(self, /):
        #d = object.__getattribute__(self, 'mapping')
        d = _get(self)
        return len(d)
    def __bool__(self, /):
        #d = object.__getattribute__(self, 'mapping')
        d = _get(self)
        return bool(d)
    def __iter__(self, /):
        #d = object.__getattribute__(self, 'mapping')
        d = _get(self)
        return iter(d)

assert 'a' not in DictKeyAsObjAttrAndAsMapping({})
assert 'a' in DictKeyAsObjAttrAndAsMapping({'a':1})
assert 1 == DictKeyAsObjAttrAndAsMapping({'a':1}).a
assert 1 == DictKeyAsObjAttrAndAsMapping({'a':1})['a']

class SetAsNamespace:
    __slots__ = '_g'
class SetAsNamespaceAndAsMapping(SetAsNamespace):
    r'''
    no: .keys(), .values(), .items()
    #'''
    __slots__ = ()
def _():
    def __repr__(self, /):
        s = _get(self)
        return repr_helper(self, s)
    def __init__(self, names, /):
        _set(self, names)
    def __setattr__(self, name, value, /):
        raise AttributeError(name)
    def __delattr__(self, name, /):
        raise AttributeError(name)
    def __getattribute__(self, name, /):
        s = _get(self)
        if name in s:
            return name
        raise AttributeError(name)
    def __dir__(self, /):
        s = _get(self)
        return sorted(k for k in s if k.isidentifier())

    def _(cls, /, **d):
        for nm, f in d.items():
            if nm == '_': continue
            setattr(cls, nm, f)
    _(SetAsNamespace, **locals())

    def __getitem__(self, key, /):
        s = _get(self)
        if key in s:
            return key
        raise KeyError(key)
    def __contains__(self, key, /):
        s = _get(self)
        return key in s
    def __len__(self, /):
        s = _get(self)
        return len(s)
    def __bool__(self, /):
        s = _get(self)
        return bool(s)
    def __iter__(self, /):
        s = _get(self)
        return iter(s)

    _(SetAsNamespaceAndAsMapping, **locals())
    del _

    _g = SetAsNamespace._g
    del SetAsNamespace._g
    _get = _g.__get__
    _set = _g.__set__
    del _g
_()
del _

assert 'a' not in SetAsNamespaceAndAsMapping({})
assert 'a' in SetAsNamespaceAndAsMapping('ab')
assert 'a' == SetAsNamespaceAndAsMapping('ab').a
assert 'a' == SetAsNamespaceAndAsMapping('ab')['a']
assert [*SetAsNamespaceAndAsMapping('ab')] == ['a', 'b']
assert len(SetAsNamespaceAndAsMapping('ab')) == 2
assert bool(SetAsNamespaceAndAsMapping('ab'))
assert not (SetAsNamespaceAndAsMapping(''))

def namespace5iterable(iterable, /):
    return SetAsNamespaceAndAsMapping(frozenset(iterable))

def namespace5names_str(names_str, /):
    if not type(names_str) is str: raise TypeError
    return namespace5iterable(names_str.split())




from seed.types.DictKeyAsObjAttr import DictKeyAsObjAttr, DictKeyAsObjAttrAndAsMapping, SetAsNamespace, SetAsNamespaceAndAsMapping, namespace5iterable, namespace5names_str

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +IGNORE_EXCEPTION_DETAIL
