#__all__:goto
r'''[[[
e ../../python3_src/seed/for_libs/for_tempfile.py

seed.for_libs.for_tempfile
py -m nn_ns.app.debug_cmd   seed.for_libs.for_tempfile -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.for_libs.for_tempfile:__doc__ -ht # -ff -df

[[
from tempfile import NamedTemporaryFile, TemporaryFile, SpooledTemporaryFile, TemporaryDirectory, mkstemp, mkdtemp, mktemp as _unsafe__mktemp, TMP_MAX, tempdir as TMP_DIR, gettempdir, gettempdirb, gettempprefix, gettempprefixb

TemporaryDirectory(suffix=None, prefix=None, dir=None, ignore_cleanup_errors=False)
    .cleanup(self)
    auto_del_all
SpooledTemporaryFile(max_size=0, mode='w+b', buffering=-1, encoding=None, newline=None, suffix=None, prefix=None, dir=None, *, errors=None)
    .name
    ?? .rollover(self)
    temporary file wrapper, specialized to switch from BytesIO or StringIO to a real file when it exceeds a certain size or  when a fileno is needed.
TemporaryFile(mode='w+b', buffering=-1, encoding=None, newline=None, suffix=None, prefix=None, dir=None, *, errors=None)
    has_no_name
    auto_del
NamedTemporaryFile(mode='w+b', buffering=-1, encoding=None, newline=None, suffix=None, prefix=None, dir=None, delete=True, *, errors=None)
    .name
    auto_del iff (kw:delete)
mkstemp(suffix=None, prefix=None, dir=None, text=False) -> (fd, fname)
    # s - safe? vs unsafe"mktemp"
    fd = os.open(...)
    caller is responsible for deleting the file when done with it.
mkdtemp(suffix=None, prefix=None, dir=None) -> path
    caller is responsible for deleting the directory when done with it.
tempdir#TMP_DIR
gettempdir() -> str{TMP_DIR}
gettempdirb() -> bytes{TMP_DIR}
gettempprefix() -> str{default_prefix4temporary_directories}
gettempprefixb() -> bytes{default_prefix4temporary_directories}

]]


>>> from seed.for_libs.for_tempfile import Path, mk_temp_dir_ctx_
>>> with mk_temp_dir_ctx_() as tmpdir:
...     assert type(tmpdir) is str
...     p0 = Path(tmpdir)/'0tmp0.txt'
...     with open(p0, 'xt', encoding='ascii') as f0:
...         print('0abc012', file=f0)
...     with open(p0, 'rt', encoding='ascii') as f0:
...         for line in f0:
...             print(repr(line))
'0abc012\n'
>>> with open(p0, 'rt', encoding='ascii') as f0:pass  #doctest: +ELLIPSIS
Traceback (most recent call last):
    ...
FileNotFoundError: ...

FileNotFoundError: [Errno 2] No such file or directory: '/data/data/com.termux/files/usr/tmp/tmp8buurgxt/0tmp0.txt'

py_adhoc_call   seed.for_libs.for_tempfile   @f

]]]'''#'''
__all__ = r'''
Path
mk_temp_dir_ctx_
'''.split()#'''
__all__
from pathlib import Path

___begin_mark_of_excluded_global_names__0___ = ...
from pathlib import Path
import tempfile
from tempfile import NamedTemporaryFile, TemporaryFile, SpooledTemporaryFile, TemporaryDirectory, mkstemp, mkdtemp, mktemp as _unsafe__mktemp, TMP_MAX, tempdir as TMP_DIR, gettempdir, gettempdirb, gettempprefix, gettempprefixb
#assert type(TMP_DIR) is Path, type(TMP_DIR)
assert (TMP_DIR) is None, type(TMP_DIR)
assert (tempfile.tempdir) is None, type(TMP_DIR)

#from itertools import islice
#from seed.tiny_.check import check_type_is, check_int_ge

#from seed.abc.abc__ver1 import abstractmethod, override, ABC
#from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError

Path = Path
mk_temp_dir_ctx_ = TemporaryDirectory

__all__
from seed.for_libs.for_tempfile import Path, mk_temp_dir_ctx_
from seed.for_libs.for_tempfile import *
