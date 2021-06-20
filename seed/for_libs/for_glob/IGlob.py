r'''
seed.for_libs.for_glob.IGlob
    #src code base on py-3.8.0::glob.py
see:
    nn_ns.filedir.dir_cmp::Glob4IDirViewer(IGlob)

py -m seed.for_libs.for_glob.IGlob
py -m nn_ns.app.debug_cmd seed.for_libs.for_glob.IGlob

from seed.for_libs.for_glob.IGlob import IGlob, the_glob4real_fsys
#'''

___begin_mark_of_excluded_global_names__0___ = ...
__all__ = '''
    IGlob
        Glob4real_fsys
            the_glob4real_fsys
    '''.split()

#from seed.for_libs.for_glob.glob_match import glob_match, glob_match_, GlobMatcher, path2std_path_parts, to_std_path_parts, check_basename, check_path, check_path__str, check_path__PurePath, is_path_always_dir, is_path_always_dir__PurePath, is_path_always_dir__str
from seed.for_libs.for_glob.glob_match import check_basename
from seed.abc.ISingleton import ISingleton
check_basename
ISingleton

##################################
##################################
##################################
    #src code base on py-3.8.0::glob.py
##################################
##################################
##################################
"""Filename globbing utility."""

import os
import re
import fnmatch
###import sys

###__all__ = ["glob", "iglob", "escape"]

from abc import ABC, abstractmethod
from seed.abc.abc import override

r'''
lexists
isdir
curdir
scandir
    if os.path.lexists(pathname):
    if os.path.isdir(dirname):
    dirname = bytes(os.curdir, 'ASCII')
    with os.scandir(dirname) as it:
_iglob
_glob0
_iterdir

iglob
_glob1
glob0
_rlistdir

glob
glob1
_glob2
#'''

def glob(sf, pathname, *, recursive=False):
    """Return a list of paths matching a pathname pattern.

    The pattern may contain simple shell-style wildcards a la
    fnmatch. However, unlike fnmatch, filenames starting with a
    dot are special cases that are not matched by '*' and '?'
    patterns.

    If recursive is true, the pattern '**' will match any files and
    zero or more directories and subdirectories.
    """
    return list(sf.iglob(pathname, recursive=recursive))

def iglob(sf, pathname, *, recursive=False):
    """Return an iterator which yields the paths matching a pathname pattern.

    The pattern may contain simple shell-style wildcards a la
    fnmatch. However, unlike fnmatch, filenames starting with a
    dot are special cases that are not matched by '*' and '?'
    patterns.

    If recursive is true, the pattern '**' will match any files and
    zero or more directories and subdirectories.
    """
    it = sf._iglob(pathname, recursive, False)
    if recursive and _isrecursive(pathname):
        s = next(it)  # skip empty string
        assert not s
    return it

def _iglob(sf, pathname, recursive, dironly):
    #sys.audit("glob.glob", pathname, recursive)
    dirname, basename = os.path.split(pathname)
    if not has_magic(pathname):
        assert not dironly
        if basename:
            if sf.os_path_lexists(pathname):
                yield pathname
        else:
            # Patterns ending with a slash should match only directories
            if sf.os_path_isdir(dirname):
                yield pathname
        return
    if not dirname:
        if recursive and _isrecursive(basename):
            yield from sf._glob2(dirname, basename, dironly)
        else:
            yield from sf._glob1(dirname, basename, dironly)
        return
    # `os.path.split()` returns the argument itself as a dirname if it is a
    # drive or UNC path.  Prevent an infinite recursion if a drive or UNC path
    # contains magic characters (i.e. r'\\?\C:').
    if dirname != pathname and has_magic(dirname):
        dirs = sf._iglob(dirname, recursive, True)
    else:
        dirs = [dirname]
    if has_magic(basename):
        if recursive and _isrecursive(basename):
            glob_in_dir = sf._glob2
        else:
            glob_in_dir = sf._glob1
    else:
        glob_in_dir = sf._glob0
    for dirname in dirs:
        for name in glob_in_dir(dirname, basename, dironly):
            yield os.path.join(dirname, name)

# These 2 helper functions non-recursively glob inside a literal directory.
# They return a list of basenames.  _glob1 accepts a pattern while _glob0
# takes a literal basename (so it only has to check for its existence).

def _glob1(sf, dirname, pattern, dironly):
    names = list(sf._iterdir(dirname, dironly))
    if not _ishidden(pattern):
        names = (x for x in names if not _ishidden(x))
    return fnmatch.filter(names, pattern)

def _glob0(sf, dirname, basename, dironly):
    if not basename:
        # `os.path.split()` returns an empty basename for paths ending with a
        # directory separator.  'q*x/' should match only directories.
        if sf.os_path_isdir(dirname):
            return [basename]
    else:
        if sf.os_path_lexists(os.path.join(dirname, basename)):
            return [basename]
    return []

# Following functions are not public but can be used by third-party code.

def glob0(sf, dirname, pattern):
    return sf._glob0(dirname, pattern, False)

def glob1(sf, dirname, pattern):
    return sf._glob1(dirname, pattern, False)

# This helper function recursively yields relative pathnames inside a literal
# directory.

def _glob2(sf, dirname, pattern, dironly):
    assert _isrecursive(pattern)
    yield pattern[:0]
    yield from sf._rlistdir(dirname, dironly)

# If dironly is false, yields all file names inside a directory.
# If dironly is true, yields only directory names.
def _iterdir(sf, dirname, dironly):
    if not dirname:
        if isinstance(dirname, bytes):
            dirname = bytes(sf.os_curdir, 'ASCII')
            dirname = bytes(sf.os_curdir, 'ASCII')
        else:
            dirname = sf.os_curdir
    try:
        if 0:
            with sf.os_scandir(dirname) as it:
                for entry in it:
                    try:
                        if not dironly or entry.is_dir():
                            yield entry.name
                    except OSError:
                        pass
        else:
            it = sf.iter_child_basenames_of_dir(dirname)
            if 1:
                for child_basename in it:
                    child_pathname = os.path.join(dirname, child_basename)
                    try:
                        child_is_dir = sf.os_path_isdir(child_pathname)
                            #os.path.isdir(child_pathname)
                    except OSError:
                        pass
                    else:
                        if not dironly or child_is_dir:
                            yield child_basename
    except OSError:
        return

# Recursively yields relative pathnames inside a literal directory.
def _rlistdir(sf, dirname, dironly):
    names = list(sf._iterdir(dirname, dironly))
    for x in names:
        if not _ishidden(x):
            yield x
            path = os.path.join(dirname, x) if dirname else x
            for y in sf._rlistdir(path, dironly):
                yield os.path.join(x, y)


magic_check = re.compile('([*?[])')
magic_check_bytes = re.compile(b'([*?[])')

def has_magic(s):
    if isinstance(s, bytes):
        match = magic_check_bytes.search(s)
    else:
        match = magic_check.search(s)
    return match is not None

def _ishidden(path):
    return path[0] in ('.', b'.'[0])

def _isrecursive(pattern):
    if isinstance(pattern, bytes):
        return pattern == b'**'
    else:
        return pattern == '**'

def escape(pathname):
    """Escape all special characters.
    """
    # Escaping is done by wrapping any of "*?[" between square brackets.
    # Metacharacters do not work in the drive part and shouldn't be escaped.
    drive, pathname = os.path.splitdrive(pathname)
    if isinstance(pathname, bytes):
        pathname = magic_check_bytes.sub(br'[\1]', pathname)
    else:
        pathname = magic_check.sub(r'[\1]', pathname)
    return drive + pathname


_d = dict(
    _iglob=_iglob
    ,_glob0=_glob0
    ,_iterdir=_iterdir

    ,iglob=iglob
    ,_glob1=_glob1
    ,glob0=glob0
    ,_rlistdir=_rlistdir

    ,glob=glob
    ,glob1=glob1
    ,_glob2=_glob2
)
___end_mark_of_excluded_global_names__0___ = ...

class IGlob(ABC):
    _iglob=_d['_iglob']
    _glob0=_d['_glob0']
    _iterdir=_d['_iterdir']

    iglob=_d['iglob']
    _glob1=_d['_glob1']
    glob0=_d['glob0']
    _rlistdir=_d['_rlistdir']

    glob=_d['glob']
    glob1=_d['glob1']
    _glob2=_d['_glob2']

    @abstractmethod
    def ___os_path_lexists___(sf, pathname, /):
        '-> bool'
        return os.path.lexists(pathname)
    def os_path_lexists(sf, pathname, /):
        '-> bool'
        b = type(sf).___os_path_lexists___(sf, pathname)
        if not type(b) is bool: raise TypeError
        return b
    @abstractmethod
    def ___os_path_isdir___(sf, pathname, /):
        '-> bool'
        return os.path.isdir(pathname)
    def os_path_isdir(sf, pathname, /):
        '-> bool'
        b = type(sf).___os_path_isdir___(sf, pathname)
        if not type(b) is bool: raise TypeError
        return b

    if 0:
        @abstractmethod
        def ___os_scandir___(sf, dirname, /):
            '-> context_manager<iter<{.name, .is_dir}>>'
            return os.scandir(dirname)
        def os_scandir(sf, dirname, /):
            #bug: not iterator but context_manager!!!
            raise NotImplementedError
            it = type(sf).___os_scandir___(sf, dirname)
            if not it is iter(it): raise TypeError
            for entry in it:
                if not (hasattr(entry, 'name') and hasattr(entry, 'is_dir')): raise TypeError
                yield entry
    else:
        @abstractmethod
        def ___iter_child_basenames_of_dir___(sf, dirname, /):
            '-> Iter<basename>'
            with os.scandir(dirname) as entry:
                yield entry.name
        def iter_child_basenames_of_dir(sf, dirname, /):
            '-> Iter<basename>'
            it = type(sf).___iter_child_basenames_of_dir___(sf, dirname)
            if not it is iter(it): raise TypeError
            for basename in it:
                check_basename(basename)
                yield basename
    @abstractmethod
    def ___get_os_curdir___(sf, /):
        '-> curr_dirname'
        return os.curdir
    @property
    def os_curdir(sf, /):
        '-> curr_dirname'
        dirname = type(sf).___get_os_curdir___(sf)
        if not sf.os_path_isdir(dirname): raise ValueError
        return dirname

class Glob4real_fsys(IGlob, ISingleton):
    @override
    def ___os_path_lexists___(sf, pathname, /):
        '-> bool'
        return IGlob.___os_path_lexists___(sf, pathname)
    @override
    def ___os_path_isdir___(sf, pathname, /):
        '-> bool'
        return IGlob.___os_path_isdir___(sf, pathname)
    @override
    def ___iter_child_basenames_of_dir___(sf, dirname, /):
        '-> Iter<basename>'
        return IGlob.___iter_child_basenames_of_dir___(sf, dirname)
    @override
    def ___get_os_curdir___(sf, /):
        '-> curr_dirname'
        return IGlob.___get_os_curdir___(sf)

the_glob4real_fsys = Glob4real_fsys()
assert the_glob4real_fsys is Glob4real_fsys()


