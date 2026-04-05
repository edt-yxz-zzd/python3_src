#__all__:goto
r'''[[[
e ../../python3_src/seed/lang/read_py_source.py

seed.lang.read_py_source
py -m nn_ns.app.debug_cmd   seed.lang.read_py_source -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.lang.read_py_source:__doc__ -ht # -ff -df
#######

[[
py_source
[py_source :: (str|bytes|AST)]

TypeError: compile() arg 1 must be a string, bytes or AST object
help(ast.parse)
    parse(source, filename='<unknown>', mode='exec', *, type_comments=False, feature_version=None)
        <==> compile(source, filename, mode, PyCF_ONLY_AST)
help(compile)
    compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1, *, _feature_version=-1)

]]


'#'; __doc__ = r'#'
>>> detect_encoding4py_source5path_(__file__)
'utf-8'
>>> type(open_py_source5path_(__file__))
<class '_io.TextIOWrapper'>
>>> read_py_source5path_(__file__)[:6]
'#__all'
>>> ibfile = open(__file__, 'rb')
>>> read_py_source5ibfile_(ibfile)[:6]
'#__all'
>>> ibfile.closed
False
>>> ibfile.close()
>>> ibfile.closed
True



py_adhoc_call   seed.lang.read_py_source   @f
]]]'''#'''
__all__ = r'''
detect_encoding4py_source5path_
    detect_encoding4py_source5ibfile_
open_py_source5path_
    open_py_source5ibfile_
read_py_source5path_
    read_py_source5ibfile_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from tokenize import detect_encoding
from io import TextIOWrapper
___end_mark_of_excluded_global_names__0___ = ...

def detect_encoding4py_source5path_(py_source_path, /):
    with open(py_source_path, 'rb') as ibfile:
        encoding = detect_encoding4py_source5ibfile_(ibfile)
    return encoding
def detect_encoding4py_source5ibfile_(ibfile, /):
    (encoding, bytess7read) = detect_encoding(ibfile.readline)
    return encoding


def open_py_source5path_(py_source_path, /):
    ibfile = open(py_source_path, 'rb')
    try:
        return open_py_source5ibfile_(ibfile)
    except:
        ibfile.close()
        raise
def open_py_source5ibfile_(ibfile, /):
    ibfile.seek(0)
    encoding = detect_encoding4py_source5ibfile_(ibfile)
    ibfile.seek(0)
    ifile = TextIOWrapper(ibfile, encoding=encoding)
    return ifile


def read_py_source5path_(py_source_path, /):
    with open_py_source5path_(py_source_path) as ifile:
        return ifile.read()

def read_py_source5ibfile_(ibfile, /):
    ifile = open_py_source5ibfile_(ibfile)
    py_source = ifile.read()
    ifile.detach()
    return py_source


__all__
from seed.lang.read_py_source import detect_encoding4py_source5path_, detect_encoding4py_source5ibfile_
from seed.lang.read_py_source import open_py_source5path_, open_py_source5ibfile_
from seed.lang.read_py_source import read_py_source5path_, read_py_source5ibfile_
from seed.lang.read_py_source import *
