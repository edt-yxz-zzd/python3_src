
#e ../../python3_src/seed/tiny_/types5py.py
from types import MappingProxyType as MapView, SimpleNamespace as kwargs2Attrs, MethodType as curry1
if 1:
    #bug:
    curry1(curry1, 1)
    try:
        curry1(curry1, None)
    except TypeError:
        #TypeError: instance must not be None
        pass
    else:
        raise 000
_curry1 = curry1
def curry1(f, x, /):
    try:
        return _curry1(f, x)
    except TypeError:
        if not callable(f):raise
    return lambda *args, **kwds:f(x, *args, **kwds)
if 1:
    #now ok
    curry1(curry1, None)

def mk_MapView(d, /):
    if not type(d) is MapView:
        d = MapView(d)
    assert type(d) is MapView
    return d
assert repr(MapView({})) == 'mappingproxy({})'
assert repr(mk_MapView({})) == 'mappingproxy({})'
assert repr(MapView(MapView({}))) == 'mappingproxy(mappingproxy({}))'
assert repr(mk_MapView(mk_MapView({}))) == 'mappingproxy({})'

from seed.tiny_.types5py import mk_MapView, MapView, kwargs2Attrs, curry1
  #SimpleNamespace(**kw)

