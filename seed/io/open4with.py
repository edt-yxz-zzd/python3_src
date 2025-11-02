#__all__:goto
r'''[[[
e ../../python3_src/seed/io/open4with.py
view ../../python3_src/seed/io/InputFile.py

seed.io.open4with
py -m nn_ns.app.debug_cmd   seed.io.open4with -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.io.open4with:__doc__ -ht # -ff -df
#######

[[
used by:
    view script/png/simple_reader_writer4png.py

usage:
    with open4rb_(may_ibfile_or_ipath) as ibfile:
        ...
    with open4wb_(may_obfile_or_opath, force=False) as obfile:
        ...
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.io.open4with   @f
]]]'''#'''
__all__ = r'''
open4rb_
open4wb_

open4rt_
open4wt_



NoClose
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
import sys
___end_mark_of_excluded_global_names__0___ = ...


__all__


class NoClose:
    def __init__(sf, tgt, /):
        sf._tgt = tgt
    def __enter__(sf, /):
        return sf._tgt
    def __exit__(sf, /, *args):
        return



def open4rb_(may_ibfile_or_ipath, /):
    if may_ibfile_or_ipath is None:
        ibfile = sys.stdin.buffer
        to_close = False
    elif hasattr(may_ibfile_or_ipath, 'read'):
        ibfile = may_ibfile_or_ipath
        to_close = False
    else:
        ipath = may_ibfile_or_ipath
        ibfile = open(ipath, 'rb')
        to_close = True
    (to_close, ibfile)
    r = NoClose(ibfile) if not to_close else ibfile
    return r
def open4wb_(may_obfile_or_opath, /, *, force:bool):
    #.if 0b00001:assert force
    if may_obfile_or_opath is None:
        obfile = sys.stdout.buffer
        to_close = False
    elif hasattr(may_obfile_or_opath, 'write'):
        obfile = may_obfile_or_opath
        to_close = False
    else:
        opath = may_obfile_or_opath
        obfile = open(opath, 'wb' if force else 'xb')
        to_close = True
    (to_close, obfile)
    r = NoClose(obfile) if not to_close else obfile
    return r



def open4rt_(may_ifile_or_ipath, /):
    if may_ifile_or_ipath is None:
        ifile = sys.stdin
        to_close = False
    elif hasattr(may_ifile_or_ipath, 'read'):
        ifile = may_ifile_or_ipath
        to_close = False
    else:
        ipath = may_ifile_or_ipath
        ifile = open(ipath, 'rt')
        to_close = True
    (to_close, ifile)
    r = NoClose(ifile) if not to_close else ifile
    return r
def open4wt_(may_ofile_or_opath, /, *, force:bool):
    #.if 0b00001:assert force
    if may_ofile_or_opath is None:
        ofile = sys.stdout
        to_close = False
    elif hasattr(may_ofile_or_opath, 'write'):
        ofile = may_ofile_or_opath
        to_close = False
    else:
        opath = may_ofile_or_opath
        ofile = open(opath, 'wt' if force else 'xt')
        to_close = True
    (to_close, ofile)
    r = NoClose(ofile) if not to_close else ofile
    return r






















__all__
from seed.io.open4with import open4rb_, open4wb_
    #.with open4rb_(may_ibfile_or_ipath) as ibfile:
    #.with open4wb_(may_obfile_or_opath, force=False) as obfile:
from seed.io.open4with import open4rt_, open4wt_
    #.with open4rt_(may_ifile_or_ipath) as ifile:
    #.with open4wt_(may_ofile_or_opath, force=False) as ofile:
from seed.io.open4with import *
