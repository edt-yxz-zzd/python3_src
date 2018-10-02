
__all__ = '''
    DependsFileExt
    JavaFileExt
    ClassFileExt

    is_ext
    is_qname
    make_make_iter_classpaths


    java_pseudo_iqname2iqname
    is_java_pseudo_iqname
    is_java_iqname
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








###################
def java_pseudo_iqname2iqname(pseudo_iqname):
    return pseudo_iqname.replace('/', '.')

positive_digits_pattern = r'(?:[1-9][0-9]*)'
java_identity_char_pattern = r'[0-9a-zA-Z_]'
java_identity_pattern = fr'(?:[a-zA-Z]{java_identity_char_pattern}*|_{java_identity_char_pattern}+)'
java_inner_identity_pattern = fr'(?:{positive_digits_pattern}|{java_identity_pattern})'
java_iqname_regex = re.compile(
    #r'(?a)\w+(?:\.\w+)*(?:\$(?:\w+|\d+))*'
    fr'(?a){java_identity_pattern}(?:\.{java_identity_pattern})*(?:\${java_inner_identity_pattern})*'
    )

def is_java_pseudo_iqname(pseudo_iqname):
    iqname = pseudo_iqname.replace('/', '.')
    return is_java_iqname(iqname)
def is_java_iqname(iqname):
    m = java_iqname_regex.fullmatch(iqname)
    return bool(m)


