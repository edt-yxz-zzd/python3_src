#__all__:goto
r'''[[[
e ../../python3_src/seed/types/Namespace.py
view ../../python3_src/seed/types/DictKeyAsObjAttr.py

seed.types.Namespace
py -m nn_ns.app.debug_cmd   seed.types.Namespace
py -m seed.types.Namespace


from seed.types.Namespace import namespace2items, namespace2keys, namespace2values

from seed.types.Namespace import MutabilityFlag4Namespace, mutability_flag2namespace_type

from seed.types.Namespace import Namespace, NamespaceSetOnce, NamespaceForbidOverwriteImplicitly, NamespaceForbidNewKey, NamespaceForbidSetitem, NamespaceForbidDelitem, NamespaceForbidAlterKeySet, NamespaceForbidModify



>>> from seed.types.Namespace import namespace2items, namespace2keys, namespace2values

>>> from seed.types.Namespace import MutabilityFlag4Namespace, mutability_flag2namespace_type

>>> from seed.types.Namespace import Namespace, NamespaceSetOnce, NamespaceForbidOverwriteImplicitly, NamespaceForbidNewKey, NamespaceForbidSetitem, NamespaceForbidDelitem, NamespaceForbidAlterKeySet, NamespaceForbidModify



>>> d = Namespace()
>>> d
Namespace()

>>> d.aaa = 999         #setnew
>>> d
Namespace({'aaa': 999})
>>> d.aaa = 111         #overwrite
>>> d
Namespace({'aaa': 111})
>>> d.aaa
111
>>> d['aaa']
111
>>> del d.aaa
>>> d
Namespace()
>>> d.aaa
Traceback (most recent call last):
    ...
AttributeError: aaa
>>> del d.aaa
Traceback (most recent call last):
    ...
AttributeError: aaa


>>> d
Namespace()
>>> d[222] = 333        #setnew
>>> d
Namespace({222: 333})
>>> d[222] = 444        #overwrite
>>> d
Namespace({222: 444})
>>> d[222]
444
>>> del d[222]
>>> d
Namespace()
>>> d[222]
Traceback (most recent call last):
    ...
KeyError: 222
>>> del d[222]
Traceback (most recent call last):
    ...
KeyError: 222





>>> d = NamespaceSetOnce()
>>> d
NamespaceSetOnce()

>>> d.aaa = 111         #setnew
>>> d
NamespaceSetOnce({'aaa': 111})
>>> d.aaa = 999         #overwrite
Traceback (most recent call last):
    ...
AttributeError: aaa
>>> d
NamespaceSetOnce({'aaa': 111})
>>> d.aaa
111
>>> d['aaa']
111
>>> del d.aaa
Traceback (most recent call last):
    ...
AttributeError: aaa
>>> d.bbb
Traceback (most recent call last):
    ...
AttributeError: bbb
>>> del d.bbb
Traceback (most recent call last):
    ...
AttributeError: bbb
>>> d
NamespaceSetOnce({'aaa': 111})


>>> d = NamespaceSetOnce()
>>> d
NamespaceSetOnce()
>>> d[222] = 444        #setnew
>>> d
NamespaceSetOnce({222: 444})
>>> d[222] = 333        #overwrite
Traceback (most recent call last):
    ...
KeyError: 222
>>> del d[222]
Traceback (most recent call last):
    ...
KeyError: 222
>>> d
NamespaceSetOnce({222: 444})
>>> d[222]
444

>>> d[555]
Traceback (most recent call last):
    ...
KeyError: 555
>>> del d[555]
Traceback (most recent call last):
    ...
KeyError: 555






>>> d = NamespaceForbidOverwriteImplicitly()
>>> d
NamespaceForbidOverwriteImplicitly()

>>> d.aaa = 111         #setnew
>>> d
NamespaceForbidOverwriteImplicitly({'aaa': 111})
>>> d.aaa = 999         #overwrite
Traceback (most recent call last):
    ...
AttributeError: aaa
>>> d
NamespaceForbidOverwriteImplicitly({'aaa': 111})
>>> d.aaa
111
>>> d['aaa']
111
>>> del d.aaa
>>> d.bbb
Traceback (most recent call last):
    ...
AttributeError: bbb
>>> del d.bbb
Traceback (most recent call last):
    ...
AttributeError: bbb
>>> d
NamespaceForbidOverwriteImplicitly()


>>> d = NamespaceForbidOverwriteImplicitly()
>>> d
NamespaceForbidOverwriteImplicitly()
>>> d[222] = 444        #setnew
>>> d
NamespaceForbidOverwriteImplicitly({222: 444})
>>> d[222] = 333        #overwrite
Traceback (most recent call last):
    ...
KeyError: 222
>>> d[222]
444
>>> del d[222]
>>> d
NamespaceForbidOverwriteImplicitly()

>>> d[555]
Traceback (most recent call last):
    ...
KeyError: 555
>>> del d[555]
Traceback (most recent call last):
    ...
KeyError: 555



>>> d = NamespaceForbidNewKey()
>>> d
NamespaceForbidNewKey()

>>> d.aaa = 111         #setnew
Traceback (most recent call last):
    ...
AttributeError: aaa
>>> d = NamespaceForbidNewKey(aaa=111)
>>> d
NamespaceForbidNewKey({'aaa': 111})
>>> d.aaa = 999         #overwrite
>>> d
NamespaceForbidNewKey({'aaa': 999})
>>> d.aaa
999
>>> d['aaa']
999
>>> del d.aaa
>>> d.bbb
Traceback (most recent call last):
    ...
AttributeError: bbb
>>> del d.bbb
Traceback (most recent call last):
    ...
AttributeError: bbb
>>> d
NamespaceForbidNewKey()


>>> d = NamespaceForbidNewKey()
>>> d
NamespaceForbidNewKey()
>>> d[222] = 444        #setnew
Traceback (most recent call last):
    ...
KeyError: 222
>>> d = NamespaceForbidNewKey({222: 444})
>>> d
NamespaceForbidNewKey({222: 444})
>>> d[222] = 333        #overwrite
>>> d[222]
333
>>> del d[222]
>>> d
NamespaceForbidNewKey()

>>> d[555]
Traceback (most recent call last):
    ...
KeyError: 555
>>> del d[555]
Traceback (most recent call last):
    ...
KeyError: 555



>>> ns = Namespace(aaa=111)
>>> ns.items()
Traceback (most recent call last):
    ...
AttributeError: items
>>> namespace2items(ns)
dict_items([('aaa', 111)])
>>> namespace2keys(ns)
dict_keys(['aaa'])
>>> namespace2values(ns)
dict_values([111])

>>> namespace2items(ns).mapping
mappingproxy(Namespace({'aaa': 111}))

>>> ns.items = 222
>>> ns.keys = 333
>>> ns.values = 444
>>> sorted(namespace2items(ns))
[('aaa', 111), ('items', 222), ('keys', 333), ('values', 444)]
>>> sorted(namespace2keys(ns))
['aaa', 'items', 'keys', 'values']
>>> sorted(namespace2values(ns))
[111, 222, 333, 444]


#>>> dir(namespace2items(ns)) == dir(namespace2keys(ns))
True
#>>> dir(namespace2keys(ns))
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'isdisjoint', 'mapping']
#>>> dir(namespace2values(ns))
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'mapping']



>>> [*MutabilityFlag4Namespace]
[<MutabilityFlag4Namespace.SetNew: 1>, <MutabilityFlag4Namespace.OverWrite: 2>, <MutabilityFlag4Namespace.Delete: 4>]
>>> [*map(print, mutability_flag2namespace_type.items())] and None
(<MutabilityFlag4Namespace.Delete|OverWrite|SetNew: 7>, <class 'seed.types.Namespace.Namespace'>)
(<MutabilityFlag4Namespace.SetNew: 1>, <class 'seed.types.Namespace.NamespaceSetOnce'>)
(<MutabilityFlag4Namespace.Delete|SetNew: 5>, <class 'seed.types.Namespace.NamespaceForbidOverwriteImplicitly'>)
(<MutabilityFlag4Namespace.Delete|OverWrite: 6>, <class 'seed.types.Namespace.NamespaceForbidNewKey'>)
(<MutabilityFlag4Namespace.Delete: 4>, <class 'seed.types.Namespace.NamespaceForbidSetitem'>)
(<MutabilityFlag4Namespace.OverWrite|SetNew: 3>, <class 'seed.types.Namespace.NamespaceForbidDelitem'>)
(<MutabilityFlag4Namespace.OverWrite: 2>, <class 'seed.types.Namespace.NamespaceForbidAlterKeySet'>)
(<MutabilityFlag4Namespace.0: 0>, <class 'seed.types.Namespace.NamespaceForbidModify'>)




#]]]'''
__all__ = r'''

namespace2items
    namespace2keys
    namespace2values

MutabilityFlag4Namespace
    mutability_flag2namespace_type

Namespace
NamespaceSetOnce
NamespaceForbidOverwriteImplicitly
NamespaceForbidNewKey
NamespaceForbidSetitem
NamespaceForbidDelitem
NamespaceForbidAlterKeySet
NamespaceForbidModify

'''.split()#'''
__all__


from enum import Flag
from collections import OrderedDict
from seed.helper.repr_input import repr_helper
from seed.tiny_.types5py import MapView


_get = dict.__getitem__
_set = dict.__setitem__
_del = dict.__delitem__
namespace2items = dict.items
namespace2keys = dict.keys
namespace2values = dict.values

MutabilityFlag4Namespace = Flag('MutabilityFlag4Namespace', 'SetNew OverWrite Delete')

class _fs:
    setitem = _set
    def setnew(self, name, value, /):
        if name in self: raise KeyError(name)
        return _set(self, name, value)
    def overwrite(self, name, value, /):
        if name not in self: raise KeyError(name)
        return _set(self, name, value)
    def forbid_setitem(self, name, value, /):
        raise KeyError(name)

    delitem = _del
    def forbid_delitem(self, name, /):
        raise KeyError(name)
_M = MutabilityFlag4Namespace
_fset2flag = (
{_fs.setitem:_M.SetNew | _M.OverWrite
,_fs.setnew:_M.SetNew
,_fs.overwrite:_M.OverWrite
,_fs.forbid_setitem:_M.SetNew ^ _M.SetNew
})
_fdel2flag = (
{_fs.delitem:_M.Delete
,_fs.forbid_delitem:_M.Delete ^ _M.Delete
})


_clss = []
class _BaseNamespace(dict):
    __slots__ = ()
    def __init_subclass__(cls, /, *args, **kwargs):
        super(__class__, cls).__init_subclass__(*args, **kwargs)
        _clss.append(cls)
    def __repr__(self, /):
        if not self:
            return repr_helper(self)
        return repr_helper(self, {**self})
    def __getattribute__(self, name, /):
        try:
            return self[name]
            return _get(self, name)
        except KeyError:
            raise AttributeError(name)
    def __setattr__(self, name, value, /):
        try:
            self[name] = value
            return
            return _set(self, name, value)
        except KeyError:
            raise AttributeError(name)
    def __delattr__(self, name, /):
        try:
            del self[name]
            return
            return _del(self, name)
        except KeyError:
            raise AttributeError(name)

    def __dir__(self, /):
        return [*self]

class Namespace(_BaseNamespace):
    __slots__ = ()
    __mutability_flag__ = _M.SetNew | _M.OverWrite | _M.Delete
    __setitem__ = _fs.setitem
    __delitem__ = _fs.delitem
class NamespaceSetOnce(_BaseNamespace):
    __slots__ = ()
    __mutability_flag__ = _M.SetNew
    __setitem__ = _fs.setnew
    __delitem__ = _fs.forbid_delitem

class NamespaceForbidOverwriteImplicitly(_BaseNamespace):
    'forbid implicitly overwrite, allow delete'
    #NamespaceDeletionExplicit
    __slots__ = ()
    __mutability_flag__ = _M.SetNew | _M.Delete
    __setitem__ = _fs.setnew
    __delitem__ = _fs.delitem


class NamespaceForbidNewKey(_BaseNamespace):
    'forbid setnew, allow delete'
    __slots__ = ()
    __mutability_flag__ = _M.OverWrite | _M.Delete
    __setitem__ = _fs.overwrite
    __delitem__ = _fs.delitem
class NamespaceForbidSetitem(_BaseNamespace):
    __slots__ = ()
    __mutability_flag__ = _M.Delete
    __setitem__ = _fs.forbid_setitem
    __delitem__ = _fs.delitem
class NamespaceForbidDelitem(_BaseNamespace):
    __slots__ = ()
    __mutability_flag__ = _M.SetNew | _M.OverWrite
    __setitem__ = _fs.setitem
    __delitem__ = _fs.forbid_delitem
class NamespaceForbidAlterKeySet(_BaseNamespace):
    __slots__ = ()
    __mutability_flag__ = _M.OverWrite
    __setitem__ = _fs.overwrite
    __delitem__ = _fs.forbid_delitem
class NamespaceForbidModify(_BaseNamespace):
    __slots__ = ()
    __mutability_flag__ = _M.SetNew ^ _M.SetNew
    __setitem__ = _fs.forbid_setitem
    __delitem__ = _fs.forbid_delitem





del _BaseNamespace.__init_subclass__
_clss
def _t():
    #print([*_M])
    for cls in _clss:
        assert cls is not _BaseNamespace
        flg = cls.__mutability_flag__
        #print(flg, cls)
        assert _fset2flag[cls.__setitem__] == (flg & ~_M.Delete)
        assert _fdel2flag[cls.__delitem__] == (flg & _M.Delete)
    assert len(_clss) == len({cls.__mutability_flag__ for cls in _clss})
    assert len(_clss) == 8




from seed.types.Namespace import _t, _clss
_t()
mutability_flag2namespace_type = MapView(OrderedDict([(cls.__mutability_flag__, cls) for cls in _clss]))


from seed.types.Namespace import namespace2items, namespace2keys, namespace2values

from seed.types.Namespace import MutabilityFlag4Namespace, mutability_flag2namespace_type

from seed.types.Namespace import Namespace, NamespaceSetOnce, NamespaceForbidOverwriteImplicitly, NamespaceForbidNewKey, NamespaceForbidSetitem, NamespaceForbidDelitem, NamespaceForbidAlterKeySet, NamespaceForbidModify




from seed.types.Namespace import *

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +IGNORE_EXCEPTION_DETAIL

