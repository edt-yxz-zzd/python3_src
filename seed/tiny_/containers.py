#from seed.tiny_.containers import null_str, null_bytes, null_int, null_tuple, null_frozenset, null_mapping_view, null_iter, mk_frozenset, mk_tuple
__all__ = '''
    mk_frozenset
    mk_tuple

    null_str
    null_bytes
    null_int
    null_tuple
    null_frozenset
    null_mapping_view
    null_iter
    '''.split()
from types import MappingProxyType as MapView

def mk_frozenset(iterable, /):
    return _mk_immutable(frozenset, null_frozenset, iterable)
def mk_tuple(iterable, /):
    return _mk_immutable(tuple, null_tuple, iterable)
def _mk_immutable(ImmutableType, null, iterable, /):
    if type(iterable) is ImmutableType:
        x = iterable
    else:
        x = ImmutableType(iterable)
    if not x:
        x = null
    return x



null_str = ''
null_bytes = b''
null_int = 0
null_tuple = ()
null_frozenset = frozenset()
null_mapping_view = MapView({})
null_iter = iter(null_str)#iter(())

assert mk_tuple([]) is null_tuple
assert mk_frozenset([]) is null_frozenset
assert null_str == ''
assert null_bytes == b''
assert null_int == 0
assert null_tuple == ()
assert null_frozenset == frozenset()
assert type(null_mapping_view) is MapView and not null_mapping_view
assert iter(null_iter) is null_iter
assert next(null_iter, [..., {}]) == [..., {}]
assert next(null_iter, None) is None


