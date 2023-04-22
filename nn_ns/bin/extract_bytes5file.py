#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/bin/extract_bytes5file.py
since:
    * hexdump:
        show hex
        donot extract bytes
    * snippet
        (py -m nn_ns.bin.get_file_chunks "$@")
        donot extract bytes


nn_ns.bin.extract_bytes5file
py -m nn_ns.app.debug_cmd   nn_ns.bin.extract_bytes5file -x
py -m nn_ns.app.doctest_cmd nn_ns.bin.extract_bytes5file:__doc__ -v
py -m nn_ns.app.doctest_cmd nn_ns.bin.extract_bytes5file!

from nn_ns.bin.extract_bytes5file import extract_bytes5file, Err__file_size_too_small


py_adhoc_call   nn_ns.bin.extract_bytes5file   @extract_bytes5file --ipath:../../python3_src/seed/io/__init__.py --opath:../../python3_src/seed/io/__init__.py +force --addr=0x0  --size=0x0
ValueError: ipath,opath are same file

py_adhoc_call   nn_ns.bin.extract_bytes5file   @extract_bytes5file --ipath:../../python3_src/seed/io/__init__.py --opath:../../python3_src/seed/io/__init__.py --addr=0x0  --size=0x0
FileExistsError: ../../python3_src/seed/io/__init__.py

py_adhoc_call   nn_ns.bin.extract_bytes5file   @extract_bytes5file --ipath:../../python3_src/seed/io/__init__.py --opath=None --addr=0x0  --size=0x0
    #nop

py_adhoc_call   nn_ns.bin.extract_bytes5file   @extract_bytes5file --ipath=None --opath=None --addr=0x0  --size=0x0
TypeError: expected str, bytes or os.PathLike object, not NoneType


py_adhoc_call   nn_ns.bin.extract_bytes5file   @extract_bytes5file --ipath:../../python3_src/seed/io/__init__.py --opath=None --addr=0x0  --size=0x1
no enough bytes
$ echo $?
2

py_adhoc_call   nn_ns.bin.extract_bytes5file   @extract_bytes5file --ipath:../../python3_src/seed/io/__init__.py --opath=None --addr=0x0  --size=0x1 -strict
    #nop

py_adhoc_call   nn_ns.bin.extract_bytes5file   @extract_bytes5file --ipath:../../python3_src/seed/io/__init__.py --opath=None --addr=0x1  --size=0x0 -strict
addr > file size
$ echo $?
1





#]]]'''
__all__ = r'''
    extract_bytes5file
    Err__file_size_too_small
'''.split()#'''
__all__
from pathlib import Path
from seed.tiny import check_type_is, check_uint, print_err
from seed.io.may_open import open4w, open4w_err, open4r
from seed.io.get_size_of_ibfile import get_size_of_ibfile

class Err__file_size_too_small(SystemExit, Exception):pass
Err__file_size_too_small(1)
Err__file_size_too_small()
def extract_bytes5file(*, ipath, opath, addr, size, force=False, strict=True):
    check_type_is(bool, strict)
    check_type_is(bool, force)
    check_uint(addr)
    check_uint(size)
    ipath = Path(ipath) #cannot be None, using .seek()!
    if not opath is None:
        opath = Path(opath)
        if not force and opath.exists():raise FileExistsError(opath)
        if force and opath.exists() and ipath.exists() and opath.samefile(ipath):raise ValueError('ipath,opath are same file')
    with open4r(ipath, xencoding=None) as ibfile:
        fsz = get_size_of_ibfile(ibfile)
        if 1:
            if fsz < addr:
                print_err('addr > file size')
                raise Err__file_size_too_small(1)
        if strict:
            if fsz < addr+size:
                print_err('no enough bytes')
                raise Err__file_size_too_small(2)
        ibfile.seek(addr)
        bs = ibfile.read(size)
    bs
    if strict:
        if not len(bs) == size:raise logic-err
    assert len(bs) <= size
    with open4w(opath, force=force, xencoding=None) as obfile:
        #??opath==ipath??#
        obfile.write(bs)
    return


from nn_ns.bin.extract_bytes5file import extract_bytes5file, Err__file_size_too_small
from nn_ns.bin.extract_bytes5file import *
