
__all__ = '''
    DependsFileExt
    JavaFileExt
    ClassFileExt

    is_ext
    is_qname
    make_make_iter_classpaths
    '''.split()

import re
from glob import iglob
from itertools import chain

DependsFileExt = '.depends'
JavaFileExt = '.java'
ClassFileExt = '.class'

qname_pattern = r'(?a)\w+(?:\.\w+)*'
qname_regex = re.compile(qname_pattern, flags=re.ASCII)

def is_ext(ext):
    # ".tar.gz"
    # ".rar.001"
    return ext and ext[0] == '.' != ext[-1]

def is_qname(s):
    return bool(qname_regex.fullmatch(s))


def make_make_iter_classpaths(classpath_glob_patterns):
    # [classpath_glob_pattern] -> (() -> Iter classpath)
    len(classpath_glob_patterns) # seq

    def make_iter_classpaths():
        return chain.from_iterable(map(iglob, classpath_glob_patterns))
    return make_iter_classpaths

