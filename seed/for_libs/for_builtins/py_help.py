#__all__:goto
r'''[[[
e ../../python3_src/seed/for_libs/for_builtins/py_help.py
    e ../../python3_src/nn_ns/app/py_help.py

help(math)
    交互对话式，太长就难以复制
    py -c 'import math;help(math)' | cat
      #输出到文件
    ---
    py -m nn_ns.app.py_help  nn_ns.app.py_help:py_help_
    py_help  xxx.yyy:CCC.MMM.fff


view ../../python3_src/seed/pkg_tools/import_object.py


seed.for_libs.for_builtins.py_help
py -m nn_ns.app.debug_cmd   seed.for_libs.for_builtins.py_help
py -m nn_ns.app.adhoc_argparser__main__call8module   seed.for_libs.for_builtins.py_help   @str.py_help :seed.for_libs.for_builtins.py_help :py_help_
from seed.for_libs.for_builtins.py_help import py_help_, py_help
#]]]'''
__all__ = r'''
    py_help_
    py_help
'''.split()#'''
__all__

from contextlib import redirect_stdout
import sys
from io import StringIO
from seed.pkg_tools.import_object import import_object, import4qobject

def py_help_(obj, /):
    'py_help_(obj) -> help_str4obj'
    with redirect_stdout(StringIO()) as fout:
        help(obj)
    return fout.getvalue()
#####ild version:
    fout = StringIO()
    saved = sys.stdout
    try:
        sys.stdout = fout
        help(obj)
    finally:
        sys.stdout = saved
    return fout.getvalue()
def py_help(may_qname4module, may_qname4obj, /):
    'py_help(may_qname4module, may_qname4obj) -> help_str4obj'
    obj = import4qobject(may_qname4module, may_qname4obj)
    return py_help_(obj)

#def main(opath, may_qname4module, may_qname4obj, /):


from seed.for_libs.for_builtins.py_help import py_help_, py_help
if __name__ == "__main__":
    pass

