#__all__:goto
    bug:too!!!__iter__/popitem = O(len(dels))!!!
    !!!obsolete
r'''[[[
e ../../python3_src/seed/mapping_tools/SandBoxDict.py
sandbox
shadow
trace
summary


seed.mapping_tools.SandBoxDict
py -m nn_ns.app.debug_cmd   seed.mapping_tools.SandBoxDict -x
py -m nn_ns.app.doctest_cmd seed.mapping_tools.SandBoxDict:__doc__ --ndiff -ff -v
py_adhoc_call   seed.mapping_tools.SandBoxDict   @f
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.mapping_tools.SandBoxDict:XXX@T    =T      ++exclude_prefixes:_
from seed.mapping_tools.SandBoxDict import *


>>> (d := SandBoxDict(ddd := {}))
SandBoxDict(mappingproxy({}))
>>> d.summary__dels__updates_()
(set(), {})
>>> d.view__dels__updates_()
(SetView(set()), mappingproxy({}))
>>> (d := SandBoxDict(ddd := {111:222, 333:444, 555:666}))
SandBoxDict(mappingproxy({111: 222, 333: 444, 555: 666}))
>>> len(d)
3
>>> sorted(d)
[111, 333, 555]
>>> 111 in d
True
>>> d[111]
222
>>> del d[111]
>>> d
SandBoxDict(mappingproxy({111: 222, 333: 444, 555: 666}), dels = {111})
>>> len(d)
2
>>> sorted(d)
[333, 555]
>>> 111 in d
False
>>> d[111]
Traceback (most recent call last):
    ...
KeyError: 111
>>> d[333] = -444
>>> d
SandBoxDict(mappingproxy({111: 222, 333: 444, 555: 666}), dels = {111}, updates = {333: -444})
>>> len(d)
2
>>> sorted(d)
[333, 555]
>>> 333 in d
True
>>> d[333]
-444
>>> d[111] = -222
>>> d
SandBoxDict(mappingproxy({111: 222, 333: 444, 555: 666}), updates = {333: -444, 111: -222})
>>> len(d)
3
>>> sorted(d)
[111, 333, 555]
>>> 111 in d
True
>>> d[111]
-222
>>> 777 in d
False
>>> d[777] = -888
>>> d
SandBoxDict(mappingproxy({111: 222, 333: 444, 555: 666}), updates = {333: -444, 111: -222, 777: -888})
>>> len(d)
4
>>> sorted(d)
[111, 333, 555, 777]
>>> 777 in d
True
>>> d[777]
-888
>>> d
SandBoxDict(mappingproxy({111: 222, 333: 444, 555: 666}), updates = {333: -444, 111: -222, 777: -888})
>>> d.summary__dels__updates_()
(set(), {333: -444, 111: -222, 777: -888})
>>> del d[111]
>>> d
SandBoxDict(mappingproxy({111: 222, 333: 444, 555: 666}), dels = {111}, updates = {333: -444, 777: -888})
>>> d.summary__dels__updates_()
({111}, {333: -444, 777: -888})
>>> del d[777]
>>> d
SandBoxDict(mappingproxy({111: 222, 333: 444, 555: 666}), dels = {111}, updates = {333: -444})
>>> d.summary__dels__updates_()
({111}, {333: -444})
>>> del d[555]
>>> d
SandBoxDict(mappingproxy({111: 222, 333: 444, 555: 666}), dels = {555, 111}, updates = {333: -444})
>>> d.summary__dels__updates_()
({555, 111}, {333: -444})
>>> del d[333]
>>> d
SandBoxDict(mappingproxy({111: 222, 333: 444, 555: 666}), dels = {555, 333, 111})
>>> d.summary__dels__updates_()
({555, 333, 111}, {})


#]]]'''
__all__ = r'''
    SandBoxDict
    Error__not_disjoint_dels_updates
'''.split()#'''
__all__
from seed.tiny import MapView, null_tuple, ifNonef
from seed.types.view.View import MapView, SetView
from collections.abc import MutableMapping
from seed.helper.repr_input import repr_helper

def __():
  class SandBoxDict___O_N(MutableMapping):
    #__iter__/popitem = O(len(dels))!!!
    '__len__ <<== assume the input mapping unchanged'
    def __init__(sf, mapping, /):
        sf._d0 = MapView(mapping)
        sf._sz = len(mapping)
        sf._d1 = {}
            # {k:tmay v}
    def __len__(sf, /):
        return sf._sz
    def __iter__(sf, /):
        d1 = sf._d1
        for k, v in d1.items():
            if v:
                v = None
                yield k
            else:
                #deleted
                pass
        for k in sf._d0:
            if not k in d1:
                yield k
            else:
                #overwrited
                pass
    def __contains__(sf, k, /):
        if not None is (tm := sf._d1.get(k)):
            return bool(tm)
        return k in sf._d0
    def __getitem__(sf, k, /):
        if not None is (tm := sf._d1.get(k)):
            if not tm:
                raise KeyError(k)
            [v] = tm
            return v
        Nothing = []
        m = sf._d0.get(k, Nothing)
        if m is Nothing:
            raise KeyError(k)
        return m
            # <<== defaultdict!!!
        return sf._d0[k]
    def __delitem__(sf, k, /):
        if not k in sf:
            raise KeyError(k)
        sf._d1[k] = null_tuple
        sf._sz -= 1
    def __setitem__(sf, k, v, /):
        new = not k in sf
        sf._d1[k] = v
        if new:
            sf._sz += 1
    def get(sf, k, default=None, /):
        if not None is (tm := sf._d1.get(k)):
            if not tm:
                return default
            [v] = tm
            return v
        return sf._d0.get(k, default)
#end-class SandBoxDict___O_N:


class Error__not_disjoint_dels_updates(Exception):pass

class SandBoxDict:
    #bug:too!!!__iter__/popitem = O(len(dels))!!!
    '__len__ <<== assume the input mapping unchanged'
    def __repr__(sf, /):
        kwds = dict(updates=sf._d1, dels=sf._ks4del)
        kwds = {k:v for k,v in kwds.items() if v}
        return repr_helper(sf, sf._d0, **kwds)
        return repr_helper(sf, sf._d0, updates=sf._d1, dels=sf._ks4del)
        return repr_helper(sf, sf._d0)
    def summary__dels__updates_(sf, /):
        return sf.tell__dels__updates_(view_vs_copy=True)
    def view__dels__updates_(sf, /):
        return sf.tell__dels__updates_(view_vs_copy=False)
    def tell__dels__updates_(sf, /, *, view_vs_copy):
        '-> (deleted_key_set, updated_item_dict)'
        if view_vs_copy:
            #copy
            f = set
            g = dict
        else:
            #view
            f = SetView
            g = MapView
        return (f(sf._ks4del), g(sf._d1))
    def __init__(sf, mapping, /, *, updates=None, dels=None):
        sf._d0 = MapView(mapping)
        sf._sz = len(mapping)
        sf._d1 = ifNonef(updates, dict)
            # {k:v}
        sf._ks4del = ifNonef(dels, set)
            # {k}
        if not sf._ks4del.isdisjoint(sf._d1.keys()):
            raise Error__not_disjoint_dels_updates
    def __len__(sf, /):
        return sf._sz
    def __iter__(sf, /):
        d1 = sf._d1
        yield from d1

        ks4del = sf._ks4del
        for k in sf._d0:
            if k in ks4del:
                #deleted
                pass
            elif k in d1:
                #overwrited
                pass
            else:
                #fallback
                yield k
    def __contains__(sf, k, /):
        if k in sf._ks4del:
            #deleted
            return False
        elif k in sf._d1:
            #overwrited
            return True
        else:
            #fallback
            return k in sf._d0
    def __getitem__(sf, k, /):
        if k in sf._ks4del:
            #deleted
            raise KeyError(k)
        Nothing = []
        m = sf._d1.get(k, Nothing)
        if not m is Nothing:
            return m
        m = sf._d0.get(k, Nothing)
        if not m is Nothing:
            return m
        raise KeyError(k)
            # <<== defaultdict!!!
        return sf._d0[k]
    def __delitem__(sf, k, /):
        if k in sf._ks4del:
            #deleted
            raise KeyError(k)
        elif k in sf._d1:
            #overwrited
            del sf._d1[k]
            shadow = k in sf._d0
        elif k in sf._d0:
            #fallback
            shadow = True
        else:
            raise KeyError(k)
        if shadow:
            sf._ks4del.add(k)
        sf._sz -= 1
    def __setitem__(sf, k, v, /):
        if k in sf._ks4del:
            #deleted
            sf._ks4del.remove(k)
            new = True
        elif k in sf._d1:
            #overwrited
            new = False
        else:
            #fallback
            new = not k in sf._d0
        sf._d1[k] = v
        if new:
            sf._sz += 1


    def get(sf, k, default=None, /):
        if k in sf._ks4del:
            #deleted
            return default
        Nothing = []
        m = sf._d1.get(k, Nothing)
        if not m is Nothing:
            #overwrited
            return m
        else:
            #fallback
            return sf._d0.get(k, default)
#end-class SandBoxDict:



def __():
    from seed.tiny import ifNonef, ifNone, echo
    from seed.tiny import check_type_is, fst, snd, at
    from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
    from seed.tiny import print_err, mk_fprint, mk_assert_eq_f, expectError
    from seed.func_tools.fmapT.fmapT__tiny import dot, fmapT__dict, fmapT__list, fmapT__iter
    from seed.helper.repr_input import repr_helper

def __():
    from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
    from seed.helper.repr_input import repr_helper
    class _(ABC):
        __slots__ = ()
        raise NotImplementedError
        ___no_slots_ok___ = True
        def __repr__(sf, /):
            #return repr_helper(sf, *args, **kwargs)
            #return repr_helper_ex(sf, args, ordered_attrs, kwargs, ordered_attrs_only=False)
            ...
if __name__ == "__main__":
    pass
__all__


from seed.mapping_tools.SandBoxDict import SandBoxDict
from seed.mapping_tools.SandBoxDict import *
