#__all__:goto
r'''[[[
e ../../python3_src/seed/filesys/fnmatch_.py

seed.filesys.fnmatch_
py -m nn_ns.app.debug_cmd   seed.filesys.fnmatch_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.filesys.fnmatch_:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.filesys.fnmatch_   @f
]]]'''#'''
__all__ = r'''
fnmatch_
    list_filter_paths_via_patterns4fname__
match_path_with_pattern_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.tiny_.group__partition import partition_xs_by_bool_
from pathlib import Path
from fnmatch import fnmatch as _fnmatch_ignorecase, fnmatchcase as _fnmatch_case
#fnmatchcase(name, pat)
#Path.glob(pattern, *, case_sensitive=None)
#PurePath.match(pattern, *, case_sensitive=None)
___end_mark_of_excluded_global_names__0___ = ...

try:
    Path('').match('', case_sensitive=True)
except TypeError:
    #TypeError: PurePath.match() got an unexpected keyword argument 'case_sensitive'
    #   !! kw:case_sensitive@ver3.12
    #from os.path import normcase as _norm_case
    def match_path_with_pattern_(path, pattern, /, *, case_sensitive=None):
        if case_sensitive is None:
           return  path.match(pattern)
        elif case_sensitive:
            return _fnmatch_case(path, pattern)
        else:
            #path = _norm_case(path)
            #pattern = _norm_case(pattern)
            return _fnmatch_ignorecase(path, pattern)
else:
    def match_path_with_pattern_(path, pattern, /, *, case_sensitive=None):
       return  path.match(pattern, case_sensitive=case_sensitive)
match_path_with_pattern_

def fnmatch_(may_case_sensitive, pattern, name, /):
    #return Path(name).match(pattern, case_sensitive=may_case_sensitive)
    if may_case_sensitive is None:
       return  Path(name).match(pattern)
    elif may_case_sensitive:
        return _fnmatch_case(name, pattern)
    else:
        #name = _norm_case(name)
        #pattern = _norm_case(pattern)
        return _fnmatch_ignorecase(name, pattern)


def list_filter_paths_via_patterns4fname__(may_case_sensitive, patterns4fname, paths, /):
    paths7ok = []
    paths7bad = [*paths]
    777;del paths
    for pattern in patterns4fname:
        #predicator = lambda path:path.match(pattern)
        #predicator = lambda path:Path(path.name).match(pattern, case_sensitive=may_case_sensitive)
        predicator = lambda path:fnmatch_(may_case_sensitive, pattern, path.name)
        (paths7bad, oks) = partition_xs_by_bool_(predicator, paths7bad)
        paths7ok.extend(oks)
        if not paths7bad:break
    paths7ok
    return (paths7bad, paths7ok)



__all__
from seed.filesys.fnmatch_ import fnmatch_, list_filter_paths_via_patterns4fname__
from seed.filesys.fnmatch_ import *
