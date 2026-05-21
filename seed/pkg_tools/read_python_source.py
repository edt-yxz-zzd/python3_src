r'''[[[
e ../../python3_src/seed/pkg_tools/read_python_source.py
seed.pkg_tools.read_python_source

#]]]'''#'''

__all__ = '''
    read_python_source
    read_python_source_from_module_qname
    '''.split()


from seed.pkg_tools.module_qname2source_file_path import module_qname2source_file_path
import tokenize


def read_python_source(path):
    with tokenize.open(path) as fin:
        return fin.read()
def read_python_source_from_module_qname(qname):
    return module_qname2source_file_path(qname)


from seed.pkg_tools.read_python_source import read_python_source, read_python_source_from_module_qname
from seed.pkg_tools.read_python_source import *
