#__all__:goto
r'''[[[
e ../../python3_src/seed/io/open8ibfile__3to1_.py
view ../../python3_src/seed/io/InputFile.py

seed.io.open8ibfile__3to1_
py -m nn_ns.app.debug_cmd   seed.io.open8ibfile__3to1_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.io.open8ibfile__3to1_:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.io.open8ibfile__3to1_   @f
]]]'''#'''
__all__ = r'''
open8ibfile__3to1_
    open8ibfile__3to2_
    open8ibfile__2to1_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
#.from seed.tiny_.check import check_type_is, check_int_ge
from seed.io.IBaseIO import InputStream5Bytes
___end_mark_of_excluded_global_names__0___ = ...

def open8ibfile__3to2_(input_case, ipath_or_ibfile_or_bytes, /):
    '-> (input_case, ipath_or_ibfile)'
    match input_case:
        case 'bytes':
            bs = ipath_or_ibfile_or_bytes
            ibfile = InputStream5Bytes(bs)
            ipath_or_ibfile = ibfile
            input_case = 'ibfile'
        case 'ipath' | 'ibfile':
            ipath_or_ibfile = ipath_or_ibfile_or_bytes
        case _:
            raise Exception('unknown input_case:', input_case)
    return (input_case, ipath_or_ibfile)

def open8ibfile__2to1_(input_case, ipath_or_ibfile, /):
    '-> ibfile'
    match input_case:
        case 'ipath':
            ipath = ipath_or_ibfile
            ibfile = open(ipath, 'rb')
        case 'ibfile':
            ibfile = ipath_or_ibfile
        case _:
            raise Exception('unknown input_case:', input_case)
    return ibfile

def open8ibfile__3to1_(input_case, ipath_or_ibfile_or_bytes, /):
    '-> ibfile'
    (input_case, ipath_or_ibfile) = open8ibfile__3to2_(input_case, ipath_or_ibfile_or_bytes)
    ibfile = open8ibfile__2to1_(input_case, ipath_or_ibfile)
    return ibfile



__all__
from seed.io.open8ibfile__3to1_ import open8ibfile__3to1_, open8ibfile__3to2_, open8ibfile__2to1_
from seed.io.open8ibfile__3to1_ import *
