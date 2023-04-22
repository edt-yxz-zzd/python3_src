#__all__:goto
r'''[[[
e ../../python3_src/seed/io/IBaseIO.py
view ../../python3_src/seed/tiny_/null_dev.py


seed.io.IBaseIO
py -m nn_ns.app.debug_cmd   seed.io.IBaseIO -x
py -m nn_ns.app.doctest_cmd seed.io.IBaseIO:__doc__ -ff -v
py -m nn_ns.app.doctest_cmd seed.io.IBaseIO!
py_adhoc_call   seed.io.IBaseIO   @f
from seed.io.IBaseIO import *
#]]]'''
__all__ = r'''
'''.split()#'''
__all__
from seed.io.null_dev import NullFileBase, NullOutputFile, null_dev, ParameterizedNullFileBase
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from io import IOBase, RawIOBase, BufferedIOBase, TextIOBase

class IBaseIO(ABC):NullFileBase??
    __slots__ = ()
class IRawIO(IBaseIO):
    __slots__ = ()
class IBufferedIO(IBaseIO):
    __slots__ = ()
class ITextIO(IBaseIO):
    __slots__ = ()

def __():
    from seed.tiny import check_type_is, fst, snd, at
    from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
    from seed.tiny import echo, print_err, mk_fprint, mk_assert_eq_f, expectError
    from seed.func_tools.fmapT.fmapT__tiny import dot, fmapT__dict, fmapT__list, fmapT__iter
    from seed.helper.repr_input import repr_helper

def __():
  class _(ABC):
    __slots__ = ()
    raise NotImplementedError
    ___no_slots_ok___ = True
    def __repr__(sf, /):
        return repr_helper(sf, *args, **kwargs)
        return repr_helper_ex(sf, args, ordered_attrs, kwargs, ordered_attrs_only=False)
    from seed.helper.repr_input import repr_helper_ex
    from seed.helper.repr_input import repr_helper
  if __name__ == "__main__":
    pass
__all__


from seed.io.IBaseIO import *
