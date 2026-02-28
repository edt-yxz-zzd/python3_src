
_BytesTypes = (bytes, bytearray)
def is_bytes_like_object_(x, /):
    if type(x) in _BytesTypes:return True
    try:
        with memoryview(x):pass
    except TypeError:
        return False
    return True
def is_bytes_(x, /):
    return type(x) is bytes
def is_pair_(x, /):
    return type(x) is tuple and len(x) == 2
def _is_sz_bs_pair_(x, /):
    return is_pair_(x) and is_bytes_like_object_(x[1])

from seed.tiny_.is_xxx import is_pair_, is_bytes_, is_bytes_like_object_
