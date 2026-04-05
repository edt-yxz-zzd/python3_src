#__all__:goto
r'''[[[
e ../../python3_src/seed/pkg_tools/iter_py_source_paths_.py

seed.pkg_tools.iter_py_source_paths_
py -m nn_ns.app.debug_cmd   seed.pkg_tools.iter_py_source_paths_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.pkg_tools.iter_py_source_paths_:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.pkg_tools.iter_py_source_paths_   @f
]]]'''#'''
__all__ = r'''
iter_py_source_paths_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#from pathlib import Path
import os
from os.path import join
from seed.filesys.relative_to import relative_to
___end_mark_of_excluded_global_names__0___ = ...

#.def iter_py_source_paths_(dir8py_pkg, /, *, ex=False):
#.    for path in Path(dir8py_pkg).rglob('*.py'):
#.        if not path.stem.isidentifier():
#.            continue
#.        rpath = relative_to(dir8py_pkg, path)
#.        if not all(map(str.isidentifier, rpath.parent.parts)):
#.            continue
#.        yield (rpath, path) if ex else path
def iter_py_source_paths_(dir8py_pkg, /, *, ex=False, leading_underscore_ok=False):
    for parent, children7dir, children7file in os.walk(dir8py_pkg):
        ok_dirs = [*filter(str.isidentifier, children7dir)]
        if not leading_underscore_ok:
            ok_dirs = [basename for basename in ok_dirs if not basename.startswith('_')]
        if not len(ok_dirs) == len(children7dir):
            children7dir[:] = ok_dirs
        ok_files = [basename for basename in children7file if basename.endswith('.py') and basename[:-3].isidentifier()]
        if not leading_underscore_ok:
            ok_files = [basename for basename in ok_files if not basename.startswith('_')]

        for basename in ok_files:
            path = join(parent, basename)
            if ex:
                rpath = relative_to(dir8py_pkg, path)
                yield (rpath, path)
            else:
                yield path




__all__
from seed.pkg_tools.iter_py_source_paths_ import iter_py_source_paths_
from seed.pkg_tools.iter_py_source_paths_ import *
