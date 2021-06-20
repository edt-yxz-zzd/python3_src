
r'''
see:
    nn_ns.filedir.dir_cmp
        py::filecmp.dircmp/cmp/cmpfiles
    nn_ns.filedir.file_cmp #diff/patch/delta, O(n)
        py::difflib.restore/context_diff/Differ.compare/ndiff/unified_diff/diff_bytes
            O(n^2)
    nn_ns.filedir.inf_dir
    nn_ns.filedir.backup_util
py -m nn_ns.app.debug_cmd nn_ns.filedir.dir_cmp

TODO:
    DONE: ignore/skip by pattern/glob

nn_ns.filedir.dir_cmp
from nn_ns.filedir.dir_cmp import dir_cmp, dir_cmp__relative, mk_filter_basenames_ex, path2str, path2str4dir_cmp_result, inv__path2str4result_of_dir_cmp__relative, path2str4result_of_dir_cmp__relative, path2str4result_of_dir_cmp, the_empty_dir_viewer, the_fsys_dir_viewer, DirViewer__fsys, DirViewer__empty_root_dir, is_same_file__True, STR_TIME_FORMAT, get_str_mtime4real_fsys, mk_is_same_file, MkIsSameFile, the_empty_access_file, the_fsys_access_file, AccessFile4MkIsSameFile__fsys, AccessFile4MkIsSameFile__empty_root_dir, bytes2PseudoFile4MkIsSameFile, binary_ifile2PseudoFile4MkIsSameFile
from nn_ns.filedir.dir_cmp import Glob4IDirViewer, IDirViewer, IPseudoFile4MkIsSameFile, IAccessFile4MkIsSameFile
from nn_ns.filedir.dir_cmp import to_std_onoff_patterns_list, onoff_patterns_lists2ignore_str, onoff_patterns_list2ignore_str, read_ignorefile, iter_read_ignorefile, read_ignorefile__text, write_ignorefile, write_ignorefile__text


py -m nn_ns.filedir.dir_cmp
py -m nn_ns.app.debug_cmd nn_ns.filedir.dir_cmp
py -m nn_ns.filedir.dir_cmp -r ../../python3_src/nn_ns/filedir/_dir_cmp__test_data/lhs/ ../../python3_src/nn_ns/filedir/_dir_cmp__test_data/rhs/
py -m nn_ns.filedir.dir_cmp -r ../../python3_src/nn_ns/filedir/_dir_cmp__test_data/lhs/ ../../python3_src/nn_ns/filedir/_dir_cmp__test_data/rhs/ -ls -pp
py -m nn_ns.filedir.dir_cmp -r ../../python3_src/nn_ns/filedir/_dir_cmp__test_data/lhs/ ../../python3_src/nn_ns/filedir/_dir_cmp__test_data/rhs/ -t
py -m nn_ns.filedir.dir_cmp -r ../../python3_src/nn_ns/filedir/_dir_cmp__test_data/lhs/ ../../python3_src/nn_ns/filedir/_dir_cmp__test_data/rhs/ --size_eq_as_same_file
py -m nn_ns.filedir.dir_cmp -r ../../python3_src/nn_ns/filedir/_dir_cmp__test_data/lhs/ ../../python3_src/nn_ns/filedir/_dir_cmp__test_data/rhs/ --mtime_eq_as_same_file
py -m nn_ns.filedir.dir_cmp -r ../../python3_src/nn_ns/filedir/_dir_cmp__test_data/lhs/ ../../python3_src/nn_ns/filedir/_dir_cmp__test_data/rhs/ --mtime_ne_as_not_same_file



cat /sdcard/0my_files/tmp/xxx/a.txt | grep "\([.]pyc\|[/]__pycache__\)')$\|/__pycache__/" -v
py -m nn_ns.filedir.dir_cmp -r /sdcard/0my_files/git_repos/python3_src/ /mnt/m_external_sd/000edt/0my_files/git_repos/python3_src/ | grep "\([.]pyc\|[/]__pycache__\)')$\|/__pycache__/" -v
py -m nn_ns.filedir.dir_cmp -r /sdcard/0my_files/git_repos/txt_phone/txt/ /mnt/m_external_sd/000edt/0my_files/git_repos/txt_phone/txt/ | grep "\([.]pyc\|[/]__pycache__\)')$\|/__pycache__/" -v
py -m nn_ns.filedir.dir_cmp -r /sdcard/0my_files/p/ /mnt/m_external_sd/000edt/0my_files/p/
py -m nn_ns.filedir.dir_cmp -r /sdcard/0my_files/git_repos/txt_phone/ /mnt/m_external_sd/000edt/0my_files/git_repos/txt_phone/ | grep "\([.]pyc\|[/]__pycache__\)')$\|/__pycache__/" -v






path::Path
relative_path :: PurePosixPath



[[[fnmatch/glob

from seed.for_libs.for_glob.glob_match import glob_match, glob_match_, GlobMatcher, path2std_path_parts, to_std_path_parts, check_basename, check_path, check_path__str, check_path__PurePath, is_path_always_dir, is_path_always_dir__PurePath, is_path_always_dir__str
from seed.for_libs.for_glob.IGlob import IGlob, the_glob4real_fsys


py::fnmatch
    fnmatch'*' <==> regex'.*'
        * matches everything

    fnmatch'?' <==> regex'.'
        ?  matches any single character

    fnmatch'[abc]' <==> regex'[abc]'
        [seq] matches any character in seq

    fnmatch'[!abc]' <==> regex'[^abc]'
        [!seq] matches any character not in seq

    escape char:
        fnmatch'[*]' <==> regex'\*'
        fnmatch'[?]' <==> regex'\?'
        fnmatch'[[]' <==> regex'\['
        ???
            err:fnmatch'[]]' <==> regex'\]'
            err:fnmatch'[!]' <==> regex'!'
                glob.escape(pathname)
                    Escape all special characters ('?', '*' and '[').
                glob using the os.scandir() and fnmatch.fnmatch()
                    glob'*' <==> regex'[^/]'
                    glob'**' with (recursive=True) <==> regex'[^/]'


fnmatch.fnmatch(filename, pattern)
    Test whether the filename string matches the pattern string, returning True or False. Both parameters are case-normalized using os.path.normcase(). fnmatchcase() can be used to perform a case-sensitive comparison, regardless of whether that’s standard for the operating system.

fnmatch.fnmatchcase(filename, pattern)
    Test whether filename matches pattern, returning True or False; the comparison is case-sensitive and does not apply os.path.normcase().

fnmatch.filter(names, pattern)
    Return the subset of the list of names that match pattern. It is the same as [n for n in names if fnmatch(n, pattern)], but implemented more efficiently.

fnmatch.translate(pattern)
    Return the shell-style pattern converted to a regular expression for using with re.match().
]]]




[[[termux:
cd ~
view ../usr/lib/python3.8/glob.py
cp -t /sdcard/0my_files/tmp/src/ ~/../usr/lib/python3.8/glob.py

===droidvim:
view /sdcard/0my_files/tmp/src/glob.py

view ../../python3_src/seed/for_libs/for_glob/IGlob.py
view ../../python3_src/seed/for_libs/for_glob/glob@py-3-8-0.py
]]]

#'''

__all__ = '''
    STR_TIME_FORMAT

    dir_cmp
        dir_cmp__relative
        mk_filter_basenames_ex
        path2str
        path2str4dir_cmp_result
            path2str4result_of_dir_cmp__relative
                inv__path2str4result_of_dir_cmp__relative
            path2str4result_of_dir_cmp

    Glob4IDirViewer
    IDirViewer
        DirViewer__fsys
            the_fsys_dir_viewer
        DirViewer__empty_root_dir
            the_empty_dir_viewer

    is_same_file__True
    mk_is_same_file
        MkIsSameFile
            IPseudoFile4MkIsSameFile
                bytes2PseudoFile4MkIsSameFile
                binary_ifile2PseudoFile4MkIsSameFile
            IAccessFile4MkIsSameFile
                STR_TIME_FORMAT
                AccessFile4MkIsSameFile__fsys
                    the_fsys_access_file
                AccessFile4MkIsSameFile__empty_root_dir
                    the_empty_access_file
                get_str_mtime4real_fsys

    to_std_onoff_patterns_list
    onoff_patterns_list2ignore_str
        onoff_patterns_lists2ignore_str
    read_ignorefile
        iter_read_ignorefile
        read_ignorefile__text
    write_ignorefile
        write_ignorefile__text
    '''.split()

___begin_mark_of_excluded_global_names__0___ = ...
import fnmatch
import glob
import re
import ast
import io
from pathlib import Path, PurePosixPath
import os.path
import time
from abc import ABC, abstractmethod
from collections.abc import Set
from seed.abc.abc import override
#from seed.abc.abc import ABC, abstractmethod, override, not_implemented, ABCMeta
from seed.tiny import fprint, fst, snd
from seed.iters.group_by import group_by
from seed.tiny import assert_eq_f
from seed.types.TriBoolOps import TriBoolOps
#from seed.helper.check.checkers import check_uint, check_all, check_str, check_int, check_tuple
from seed.helper.check.checkers import check_uint_imay, check_uint, check_type_is
#from nn_ns.filedir.relative_path_ops import relative_path_ops, check_relative_path, is_relative_path_empty, relative_path2parts #avoid relative_path.parts
from nn_ns.filedir.relative_path_ops import empty_relative_path, is_relative_path_empty, check_relative_path
from seed.abc.ISingleton import ISingleton


#from seed.for_libs.for_glob.glob_match import glob_match, glob_match_, GlobMatcher, path2std_path_parts, to_std_path_parts, check_basename, check_path, check_path__str, check_path__PurePath, is_path_always_dir, is_path_always_dir__PurePath, is_path_always_dir__str
from seed.for_libs.for_glob.glob_match import check_basename, glob_match
from seed.for_libs.for_glob.IGlob import IGlob#, the_glob4real_fsys
___end_mark_of_excluded_global_names__0___ = ...


class Glob4IDirViewer(IGlob):
    def __init__(sf, dir_viewer, /):
        if not isinstance(dir_viewer, IDirViewer): raise TypeError
        sf.__dir_viewer = dir_viewer

    @override
    def ___os_path_lexists___(sf, pathname, /):
        '-> bool'
        return sf.__dir_viewer.exists(pathname)
    @override
    def ___os_path_isdir___(sf, pathname, /):
        '-> bool'
        return sf.__dir_viewer.is_dir(pathname)
    @override
    def ___iter_child_basenames_of_dir___(sf, dirname, /):
        '-> Iter<basename>'
        return sf.__dir_viewer.dir_iter(dirname)
    @override
    def ___get_os_curdir___(sf, /):
        '-> curr_dirname'
        return empty_relative_path
        raise NotImplementedError



class IDirViewer(ABC):
    r'''
    path::Path
    #'''
    @abstractmethod
    def ___is_file___(sf, path):
        'path -> (bool|raise FileNotFoundError)'
    @abstractmethod
    def ___dir_iter___(sf, dir_path):
        'dir_path -> (Iter basename | raise FileNotFoundError/NotADirectoryError)'
    @abstractmethod
    def ___exists___(sf, path):
        'path -> bool'

    def exists(sf, path):
        'path -> bool'
        b = type(sf).___exists___(sf, path)
        if not type(b) is bool: raise TypeError
        return b
    def dir_iter(sf, dir_path):
        'dir_path -> (Iter basename | raise FileNotFoundError/NotADirectoryError)'
        it = type(sf).___dir_iter___(sf, dir_path)
        if not it is iter(it): raise TypeError
        for basename in it:
            check_basename(basename)
            yield basename

    def __is_file(sf, path):
        'path -> bool'
        b = type(sf).___is_file___(sf, path)
        if type(b) is not bool: raise TypeError
        return b
    def is_file(sf, path):
        'path -> bool'
        return sf.__is_file(path)
    def is_dir(sf, path):
        'path -> bool'
        return not sf.__is_file(path)

def is_same_file__True(lhs_file_path, rhs_file_path):
    r'''-> True
    precondition: both exist and are files
    used when only want to cmp fsys tree structure, e.g. nn_ns.filedir.inf_dir copy manually
    #'''
    return True
#path.relative_to + PurePosixPath
def dir_cmp__relative(is_same_file, lhs_dir_viewer, lhs_path, rhs_dir_viewer, rhs_path, /, *, ignore_relative_path, ignore_basename, max_depth):
    r'''-> Iter (case, xhs_relative_filedir_path)
    -> Iter ((-1, lhs_relative_path)|(+1, rhs_relative_path)|(0, xhs_relative_file_path)|(-2, xhs_relative_filedir_path)|(+2, xhs_relative_filedir_path))
    see: dir_cmp
    #'''
    result_of_dir_cmp = dir_cmp(is_same_file, lhs_dir_viewer, lhs_path, rhs_dir_viewer, rhs_path, ignore_basename=ignore_basename, ignore_relative_path=ignore_relative_path, max_depth=max_depth)
    for case, xhs_relative_filedir_path, data in result_of_dir_cmp:
        yield case, xhs_relative_filedir_path

def path2str(path):
    #bug:return str(path)
    return path.as_posix()
def inv__path2str4result_of_dir_cmp__relative(result_of_dir_cmp__relative__str):
    for case, y in result_of_dir_cmp__relative__str:
        x = PurePosixPath(y)
        yield case, x
def path2str4result_of_dir_cmp__relative(result_of_dir_cmp__relative):
    for case, x in result_of_dir_cmp__relative:
        y = path2str(x)
        yield case, y
def path2str4result_of_dir_cmp(result_of_dir_cmp):
    for case, p, x in result_of_dir_cmp:
        z = path2str(p)
        if type(x) is tuple:
            y = tuple(map(path2str, x))
        else:
            y = path2str(x)
        yield case, z, y
inv__path2str4result_of_dir_cmp__relative
path2str4result_of_dir_cmp__relative
path2str4result_of_dir_cmp
def path2str4dir_cmp_result(dir_cmp_result, /,*, relative:bool):
    'dir_cmp_result = result of dir_cmp/dir_cmp__relative'
    f = path2str4result_of_dir_cmp__relative if relative else path2str4result_of_dir_cmp
    return f(dir_cmp_result)

def match__cased_pattern(pattern_case, pattern, s):
    r'''pattern_case -> pattern -> str -> bool
    cased_pattern
        see: dir_cmp
    #'''
    if pattern_case not in ('fnmatch', 'glob', 're'): raise ValueError
    if pattern_case == 're':
        return re.fullmatch(pattern, s)
    elif pattern_case == 'fnmatch':
        return fnmatch.fnmatchcase(s, pattern)
    elif pattern_case == 'glob':
        if 0:
            #err:return glob.iglob(s, recursive=True)
            raise NotImplementedError
        else:
            return glob_match(pattern, s, is_path_dir__tribool=..., match_dir_only=False, ignore_case=False, recursive=True)
    else:
        raise logic-err
def match__OR(cased_patterns, s):
    r'''cased_patterns -> str -> bool
    cased_patterns
        see: dir_cmp
    #'''
    cased_patterns
    return any(match__cased_pattern(pattern_case, pattern, s)
            for pattern_case, pattern in cased_patterns
            )

def to_std_onoff_patterns_list(onoff_patterns_list):
    'tuple/frozen/hashable'
    _onoff_patterns_list = tuple((onoff_case, tuple((pattern_case, pattern) for pattern_case, pattern in cased_patterns)) for onoff_case, cased_patterns in onoff_patterns_list)

    if onoff_patterns_list not in [_onoff_patterns_list]:
        onoff_patterns_list = _onoff_patterns_list
    return onoff_patterns_list


def onoff_patterns_lists2ignore_str(onoff_patterns_lists, /):
    r'''Iter onoff_patterns_list -> (str->bool)
    onoff_patterns_list
        see: dir_cmp/onoff_patterns_list2ignore_str
    ignore_str
        like ignore_basename/ignore_relative_path

    use scene:
        many ignorefiles

        read_ignorefile/read_ignorefile__text
            ignorefile -> onoff_patterns_list
        [ignorefile] -> [onoff_patterns_list]
        default ignore=False
            ==>> fold by "or" instead of "and"
    #'''
    ignore_str_tpl = tuple(map(onoff_patterns_list2ignore_str, onoff_patterns_lists))
    def ignore_str4many_ignorefiles__any(s):
        return any(ignore_str(s) for ignore_str in ignore_str_tpl)
    return ignore_str4many_ignorefiles__any

def onoff_patterns_list2ignore_str(onoff_patterns_list):
    r'''onoff_patterns_list -> (str->bool)
    onoff_patterns_list
        see: dir_cmp
    ignore_str
        like ignore_basename/ignore_relative_path
    #'''
    onoff_patterns_list
    onoff_patterns_list = to_std_onoff_patterns_list(onoff_patterns_list)

    def ignore_str(s):
        ignore = ...
        for onoff_case, cased_patterns in reversed(onoff_patterns_list):
            if onoff_case not in ('-', '+'): raise ValueError
            if match__OR(cased_patterns, s):
                ignore = onoff_case == '-'
                return ignore
        ignore = False
        return ignore
    return ignore_str


def mk_filter_basenames_ex(*, ignore_basename, ignore_relative_path):
    r'''-> (xhs_relative_dir_path -> basenames -> set<basename>)
    =====
    never ignore '.' #empty_relative_path
        impl by split out xhs_relative_dir_path
    =====
    #kwargs from dir_cmp
    ignore_basename :: None|(basename::str -> bool)|onoff_patterns_list
    ignore_relative_path :: None|(xhs_relative_filedir_path::Path -> bool)|onoff_patterns_list
        see: dir_cmp
    =====
    filter_basenames_ex = mk_filter_basenames_ex(ignore_basename=ignore_basename, ignore_relative_path=ignore_relative_path)
    del ignore_basename, ignore_relative_path
    #'''
    if 1:
        #def about ignore
        def not_ignore(*args):
            return False
        #ignore_basename =
        if ignore_basename is None:
            ignore_basename = not_ignore
        elif callable(ignore_basename):
            pass
        else:
            onoff_patterns_list = ignore_basename
            ignore_basename = onoff_patterns_list2ignore_str(onoff_patterns_list)

        #ignore_relative_path =
        if ignore_relative_path is None:
            ignore_relative_path = not_ignore
        elif callable(ignore_relative_path):
            pass
        else:
            onoff_patterns_list = ignore_relative_path
            ignore_relative_path__str = onoff_patterns_list2ignore_str(onoff_patterns_list)
            def ignore_relative_path(relative_path):
                return ignore_relative_path__str(path2str(relative_path))
        ####

        assert callable(ignore_basename)
        assert callable(ignore_relative_path)
        def filter_basenames(basenames):
            '-> Iter<basename>'
            return (basename for basename in basenames if not ignore_basename(basename))

        def filter_relative_path(xhs_relative_dir_path, basenames):
            '-> Iter<basename>'
            return (basename for basename in basenames if not ignore_relative_path(xhs_relative_dir_path/basename))

        def filter_basenames_ex(xhs_relative_dir_path, basenames):
            '-> set<basename>'
            basenames = filter_basenames(basenames)
            basenames = filter_relative_path(xhs_relative_dir_path, basenames)
            return set(basenames)
    return filter_basenames_ex
    filter_basenames_ex = mk_filter_basenames_ex(ignore_basename=ignore_basename, ignore_relative_path=ignore_relative_path)
    del ignore_basename, ignore_relative_path
    #

def dir_cmp(is_same_file, lhs_dir_viewer, lhs_path, rhs_dir_viewer, rhs_path, /, *, ignore_basename, ignore_relative_path, max_depth):
    r'''#stable ordered output by sorted basenames
    -> Iter ([-2..+2], xhs_relative_filedir_path, payload)
    -> Iter ((-1, xhs_relative_filedir_path, lhs_path)|(+1, xhs_relative_filedir_path, rhs_path)|(0, xhs_relative_filedir_path, (lhs_file_path, rhs_file_path))|(-2, xhs_relative_filedir_path, (lhs_dir_path, rhs_file_path))|(+2, xhs_relative_filedir_path, (lhs_file_path, rhs_dir_path)))
    # diff = extra lhs_path | extra rhs_path | diff file content | mismatch dir/file

    is_same_file :: lhs_file_path -> rhs_file_path -> bool
        'precondition: both exist and are files'
    lhs_dir_viewer :: IDirViewer
    lhs_path :: Path
    rhs_dir_viewer :: IDirViewer
    rhs_path :: Path
    ignore_basename :: None|(basename::str -> bool)|onoff_patterns_list
    ignore_relative_path :: None|(xhs_relative_filedir_path::Path -> bool)|onoff_patterns_list
        xhs_relative_filedir_path :: relative PurePosixPath
            #see: nn_ns.filedir.relative_path_ops
        pattern from fnmatch/glob/re
        onoff_patterns_list :: [(onoff_case, [cased_pattern])]
            onoff_case = ('-'|'+')
            cased_pattern = (pattern_case, pattern)
                pattern_case = ('fnmatch'|'glob'|'re')

    max_depth :: None|[-1..]
        -1 <==> None <==> recur inf
        0 - not inspect "into" dir
        1 - only dir itself and direct children

    =============
    =============
    =============
    left/right file system may be diff
        e.g.
            svn
            zip
            local-filesys
            remote-filesys
    ======
    never ignore '.' #empty_relative_path

    #'''
    if not lhs_dir_viewer.exists(lhs_path): raise FileNotFoundError(lhs_path)
    if not rhs_dir_viewer.exists(rhs_path): raise FileNotFoundError(rhs_path)

    #max_depth =
    if max_depth is not None:
        if type(max_depth) is not int: raise TypeError
        if not max_depth >= -1: raise ValueError
        if max_depth == -1:
            max_depth = None


    filter_basenames_ex = mk_filter_basenames_ex(ignore_basename=ignore_basename, ignore_relative_path=ignore_relative_path)
    del ignore_basename, ignore_relative_path



    # main loop

    #may_path_pairs = [(lhs_path, rhs_path)]
    #depth_mlpath_mrpath_triples = [(0, lhs_path, rhs_path)]
    depth_xpath_mlpath_mrpath_tpl4_ls = [(0, empty_relative_path, lhs_path, rhs_path)]
        #never ignore '.' #empty_relative_path
    lhs_root = lhs_path
    rhs_root = rhs_path
    while depth_xpath_mlpath_mrpath_tpl4_ls:
        (depth, xhs_relative_filedir_path, may_lhs_path, may_rhs_path) = depth_xpath_mlpath_mrpath_tpl4_ls.pop()
        assert may_lhs_path is None or may_lhs_path == lhs_root / xhs_relative_filedir_path
        assert may_rhs_path is None or may_rhs_path == rhs_root / xhs_relative_filedir_path

        if 1:
            if may_lhs_path is None is may_rhs_path:
                raise logic-err
            elif may_rhs_path is None:
                lhs_path = may_lhs_path
                yield -1, xhs_relative_filedir_path, lhs_path
                continue
            elif may_lhs_path is None:
                rhs_path = may_rhs_path
                yield +1, xhs_relative_filedir_path, rhs_path
                continue
            else:
                pass

        (lhs_path, rhs_path) = (may_lhs_path, may_rhs_path)
        lb = lhs_dir_viewer.is_file(lhs_path)
        rb = rhs_dir_viewer.is_file(rhs_path)
        if lb and rb:
            (lhs_file_path, rhs_file_path) = (lhs_path, rhs_path)
            if is_same_file(lhs_file_path, rhs_file_path):
                pass#do nothing
            else:
                yield 0, xhs_relative_filedir_path, (lhs_file_path, rhs_file_path)
        elif not lb and rb:
            (lhs_dir_path, rhs_file_path) = (lhs_path, rhs_path)
            yield -2, xhs_relative_filedir_path, (lhs_dir_path, rhs_file_path)
        elif lb and not rb:
            (lhs_file_path, rhs_dir_path) = (lhs_path, rhs_path)
            yield +2, xhs_relative_filedir_path, (lhs_file_path, rhs_dir_path)
        else:
            assert not lb and not rb
            (lhs_dir_path, rhs_dir_path) = (lhs_path, rhs_path)
            if max_depth is not None and not depth < max_depth:
                #skip/ignore
                pass
            else:
                lnames = set(lhs_dir_viewer.dir_iter(lhs_dir_path))
                rnames = set(rhs_dir_viewer.dir_iter(rhs_dir_path))
                common = lnames & rnames
                lonly = lnames - common
                ronly = rnames - common

                xhs_relative_dir_path = xhs_relative_filedir_path #PurePosixPath(lhs_dir_path.relative_to(lhs_root))
                common = filter_basenames_ex(xhs_relative_dir_path, common)
                lonly = filter_basenames_ex(xhs_relative_dir_path, lonly)
                ronly = filter_basenames_ex(xhs_relative_dir_path, ronly)

                #all_names = sorted(lnames | rnames, reverse=True)
                filtered_all_names = sorted(common | lonly | ronly, reverse=True)
                for name in filtered_all_names:
                    #why not yield directly?
                    #   common must recur, but I flatten by stack
                    #   to keep order, non-common should push too
                    if name in common:
                        pair = lhs_dir_path/name, rhs_dir_path/name
                    elif name in lonly:
                        pair = lhs_dir_path/name, None
                    elif name in ronly:
                        pair = None, rhs_dir_path/name
                    else:
                        raise logic-err
                    depth_xpath_mlpath_mrpath_tpl4_ls.append((depth+1, xhs_relative_dir_path/name, *pair))




class DirViewer__empty_root_dir(IDirViewer, ISingleton):
    'path::relative PurePosixPath'
    @override
    def ___exists___(sf, path):
        'path -> bool'
        check_relative_path(path)
        return is_relative_path_empty(path)

    @override
    def ___is_file___(sf, path):
        'path -> (bool|raise FileNotFoundError)'
        check_relative_path(path)
        if is_relative_path_empty(path): return False
        raise FileNotFoundError(path)
    @override
    def ___dir_iter___(sf, dir_path):
        'dir_path -> (Iter basename | raise FileNotFoundError/NotADirectoryError)'
        check_relative_path(dir_path)
        if is_relative_path_empty(dir_path):
            return;yield
        raise FileNotFoundError(dir_path)
the_empty_dir_viewer = DirViewer__empty_root_dir()
assert the_empty_dir_viewer is DirViewer__empty_root_dir()


class DirViewer__fsys(IDirViewer, ISingleton):
    @override
    def ___exists___(sf, path):
        'path -> bool'
        return path.exists()
    @override
    def ___is_file___(sf, path):
        'path -> (bool|raise FileNotFoundError)'
        return path.is_file()
    @override
    def ___dir_iter___(sf, dir_path):
        'dir_path -> (Iter basename | raise FileNotFoundError/NotADirectoryError)'
        yield from os.listdir(dir_path)
        return
        for path in dir_path.iterdir():
            yield path.name
the_fsys_dir_viewer = DirViewer__fsys()
assert the_fsys_dir_viewer is DirViewer__fsys()

if 0:
    path = ... #to s.t. forgots
    path.samefile
    path.stat().st_size
    os.path.getsize
    os.listdir
    os.scandir
if 0:
    ops = DirViewer__fsys()
    print(list(ops.dir_iter(Path('.'))))


class IPseudoFile4MkIsSameFile(ABC):
    r'''
    for MkIsSameFile
    path::Path

    NOTE:io.binary_ifile.read(0) -> b'' !!!
        avoid .read(0)

    see:
        bytes2PseudoFile4MkIsSameFile
        binary_ifile2PseudoFile4MkIsSameFile
    #'''
    @abstractmethod
    def ___read_all_remain_bytes___(sf, /):
        '-> remain_bytes'
    @abstractmethod
    def ___read_le_positive___(sf, num_bytes__ge1, /):
        'num_bytes{>=1} -> remain_bytes[:num_bytes]'
    def read(sf, imay_num_bytes, /):
        r'''uint_imay -> bytes# -1 ==>> read all, 0 ==>> raise ValueError

        NOTE:io.binary_ifile.read(0) -> b'' !!!
            avoid .read(0)
        #'''
        #bug:不兼容标准库:'uint -> bytes# 0 ==>> read all'
        check_uint_imay(imay_num_bytes)
        if imay_num_bytes == -1:
            bs = type(sf).___read_all_remain_bytes___(sf)
        elif imay_num_bytes == 0: raise ValueError
        else:
            assert imay_num_bytes > 0
            num_bytes__ge1 = imay_num_bytes
            assert num_bytes__ge1 >= 1
            bs = type(sf).___read_le_positive___(sf, num_bytes__ge1)
            assert 0 <= len(bs) <= num_bytes__ge1
        check_type_is(bytes, bs)
        return bs

    #context manager
    @abstractmethod
    def __enter__(sf, /):
        pass
    @abstractmethod
    def __exit__(sf, exc_type, exc_value, traceback, /):
        pass
#HHHHH
IPseudoFile4MkIsSameFile
class bytes2PseudoFile4MkIsSameFile(IPseudoFile4MkIsSameFile):
    r'''
    for MkIsSameFile
    path::Path

    vs
        io.BytesIO
        bytes2PseudoFile4MkIsSameFile
        binary_ifile2PseudoFile4MkIsSameFile
    #'''
    def __init__(sf, bs:bytes, /):
        sf.__bs = bs
        sf.__pos = 0

    @override
    def ___read_all_remain_bytes___(sf, /):
        '-> remain_bytes'
            #read all
        bs = sf.__bs[sf.__pos:]
        sf.__pos += len(bs)
        return bs
    @override
    def ___read_le_positive___(sf, num_bytes__ge1, /):
        'num_bytes{>=1} -> remain_bytes[:num_bytes]'
        bs = sf.__bs[sf.__pos:sf.__pos+num_bytes__ge1]
        sf.__pos += len(bs)
        return bs


    #context manager
    @override
    def __enter__(sf, /):
        return sf
    @override
    def __exit__(sf, exc_type, exc_value, traceback, /):
        pass
    pass
pass

#HHHHH
IPseudoFile4MkIsSameFile
class binary_ifile2PseudoFile4MkIsSameFile(IPseudoFile4MkIsSameFile):
    r'''
    for MkIsSameFile
    path::Path

    vs
        io.BytesIO
        bytes2PseudoFile4MkIsSameFile
        binary_ifile2PseudoFile4MkIsSameFile
    #'''
    def __init__(sf, binary_ifile, /):
        sf.__bfin = binary_ifile
        sf.__pos = 0

    @override
    def ___read_all_remain_bytes___(sf, /):
        '-> remain_bytes'
        return sf.__bfin.read()
    @override
    def ___read_le_positive___(sf, num_bytes__ge1, /):
        'num_bytes{>=1} -> remain_bytes[:num_bytes]'
        return sf.__bfin.read(num_bytes__ge1)


    #context manager
    @override
    def __enter__(sf, /):
        bfin = sf.__bfin
        return type(bfin).__enter__(bfin)
    @override
    def __exit__(sf, exc_type, exc_value, traceback, /):
        bfin = sf.__bfin
        return type(bfin).__exit__(bfin, exc_type, exc_value, traceback)
    pass
pass




STR_TIME_FORMAT = '%Y%m%d_%H%M%S_%z'
    # ends with constant %z == +0000
class IAccessFile4MkIsSameFile(ABC):
    r'''
    for MkIsSameFile
    path::Path
    #'''
    @abstractmethod
    def open(sf, file_path):
        'file_path -> IPseudoFile4MkIsSameFile'
    @abstractmethod
    def get_file_size(sf, file_path):
        'file_path -> uint # unit:byte'
    @abstractmethod
    def get_may_hash_method_uppercase_std_name2upper_hex_digest(sf, file_path):
        'file_path -> (None|hash_method_uppercase_std_name2upper_hex_digest::{name:hex}) #name <- {SHA256, MD5, ...}'
    @abstractmethod
    def get_may_str_mtime(sf, file_path):
        r'''file_path -> (None|str_time) # %Y%m%d_%H%M%S_%z # == STR_TIME_FORMAT
        # ends with constant %z == +0000
        #'''

    @staticmethod
    def _float_time2str_time(float_time):
        struct_time = time.gmtime(float_time)
        str_time = time.strftime(STR_TIME_FORMAT, struct_time)
        assert str_time.endswith('+0000')
        return str_time

    r'''
float_time = os.path.getmtime(file_path)
struct_time = time.gmtime(float_time)
str_time = time.strftime(STR_TIME_FORMAT, struct_time)
assert str_time.endswith('+0000')
str_mtime = str_time

====
time.strftime :: format -> struct_time -> str_time
    %Y%m%d_%H%M%S_%z
    <->time.strptime :: format -> str_time -> struct_time
time.gmtime :: float_time -> struct_time
    <->calendar.timegm :: struct_time <-> float_time
    mk %z be +0000 forever
os.path.getmtime :: path -> (mtime::float_time | raise OSError)
    Return the time of last modification of path. The return value is a floating point number giving the number of seconds since the epoch (see the time module). Raise OSError if the file does not exist or is inaccessible.

====
#   >>> import time as t
#   >>> fmt='%Y%m%d_%H%M%S_%z'
#   >>> t.strftime(fmt)
#   '20210408_065949_+0800'
#   >>> t.strftime(fmt)
#   '20210408_070011_+0800'
#   >>> t.strftime(fmt, t.gmtime())
#   '20210407_230122_+0000'

    #'''

def raise_on_file_path__empty_root_dir(file_path, /):
    'path::relative PurePosixPath'
    check_relative_path(file_path)
    if is_relative_path_empty(file_path): raise IsADirectoryError('root dir is not file')
    raise FileNotFoundError(file_path)
class AccessFile4MkIsSameFile__empty_root_dir(IAccessFile4MkIsSameFile, ISingleton):
    r'''
    for MkIsSameFile
    path::relative PurePosixPath
    #'''
    def __raise_on_file_path(sf, file_path, /):
        raise raise_on_file_path__empty_root_dir(file_path)

    @override
    def open(sf, file_path):
        'file_path -> IPseudoFile4MkIsSameFile'
        raise sf.__raise_on_file_path(file_path)
    @override
    def get_file_size(sf, file_path):
        'file_path -> uint # unit:byte'
        raise sf.__raise_on_file_path(file_path)
    @override
    def get_may_hash_method_uppercase_std_name2upper_hex_digest(sf, file_path):
        'file_path -> (None|hash_method_uppercase_std_name2upper_hex_digest::{name:hex}) #name <- {SHA256, MD5, ...}'
        raise sf.__raise_on_file_path(file_path)
    @override
    def get_may_str_mtime(sf, file_path):
        raise sf.__raise_on_file_path(file_path)
the_empty_access_file = AccessFile4MkIsSameFile__empty_root_dir()
assert the_empty_access_file is AccessFile4MkIsSameFile__empty_root_dir()


class AccessFile4MkIsSameFile__fsys(IAccessFile4MkIsSameFile, ISingleton):
    @override
    def get_file_size(sf, file_path):
        'file_path -> uint # unit:byte'
        return os.path.getsize(file_path)
    @override
    def open(sf, file_path):
        'file_path -> IPseudoFile4MkIsSameFile'
        binary_ifile = open(file_path, 'rb')
        return binary_ifile2PseudoFile4MkIsSameFile(binary_ifile)
    @override
    def get_may_hash_method_uppercase_std_name2upper_hex_digest(sf, file_path):
        'file_path -> (None|hash_method_uppercase_std_name2upper_hex_digest::{name:hex}) #name <- {SHA256, MD5, ...}'
        return None
    @override
    def get_may_str_mtime(sf, file_path):
        r'''file_path -> (None|str_time) # %Y%m%d_%H%M%S_%z # == STR_TIME_FORMAT
        # ends with constant %z == +0000
        #'''
        str_mtime = get_str_mtime4real_fsys(file_path)
        return str_mtime
the_fsys_access_file = AccessFile4MkIsSameFile__fsys()
assert the_fsys_access_file is AccessFile4MkIsSameFile__fsys()


def get_str_mtime4real_fsys(file_path, /):
    r'''file_path -> str_time # %Y%m%d_%H%M%S_%z # == STR_TIME_FORMAT
    # ends with constant %z == +0000
    #'''
    float_mtime = os.path.getmtime(file_path)
    float_time = float_mtime
    str_time = IAccessFile4MkIsSameFile._float_time2str_time(float_time)

    str_mtime = str_time
    return str_mtime


class MkIsSameFile:
    r'''
    for is_same_file
    path::Path
    #'''
    def __init__(sf, lhs_access_file, rhs_access_file, /, *, always_tribool_as_is_or_not_same_file:'tribool', size_eq_as_same_file:bool, size_hash0_eq_as_same_file:bool, hash_eq_as_same_file:bool, mtime_eq_as_same_file:bool, mtime_ne_as_not_same_file:bool, imay_max_size_threshold4cmp_content:int, _block_size):
        'IAccessFile4MkIsSameFile -> IAccessFile4MkIsSameFile -> MkIsSameFile'
        if not isinstance(lhs_access_file, IAccessFile4MkIsSameFile):raise TypeError
        if not isinstance(rhs_access_file, IAccessFile4MkIsSameFile):raise TypeError
        if type(_block_size) is not int:raise TypeError
        if not _block_size >= 1: raise ValueError
        if type(imay_max_size_threshold4cmp_content) is not int:raise TypeError
        if not imay_max_size_threshold4cmp_content >= -1: raise ValueError
        check_uint_imay(imay_max_size_threshold4cmp_content)

        if not TriBoolOps.is_tribool(always_tribool_as_is_or_not_same_file):raise TypeError
        if not (always_tribool_as_is_or_not_same_file is ... or type(always_tribool_as_is_or_not_same_file) is bool):raise TypeError

        if type(size_eq_as_same_file) is not bool:raise TypeError
        if type(size_hash0_eq_as_same_file) is not bool:raise TypeError
        if type(hash_eq_as_same_file) is not bool:raise TypeError
        if type(mtime_eq_as_same_file) is not bool:raise TypeError
        if type(mtime_ne_as_not_same_file) is not bool:raise TypeError

        sf.lhs_access_file = lhs_access_file
        sf.rhs_access_file = rhs_access_file
        sf._block_size = _block_size
        sf.imay_max_size_threshold4cmp_content = imay_max_size_threshold4cmp_content
        sf.always_tribool_as_is_or_not_same_file = always_tribool_as_is_or_not_same_file
        sf.size_eq_as_same_file = size_eq_as_same_file
        sf.size_hash0_eq_as_same_file = size_hash0_eq_as_same_file
        sf.hash_eq_as_same_file = hash_eq_as_same_file
        sf.mtime_eq_as_same_file = mtime_eq_as_same_file
        sf.mtime_ne_as_not_same_file = mtime_ne_as_not_same_file

    def __call__(sf, lhs_file_path, rhs_file_path):
        'is_same_file :: lhs_file_path -> rhs_file_path -> bool #precondition: both exist and are files'
        r = type(sf).___is_same_file___(sf, lhs_file_path, rhs_file_path)
        if type(r) is not bool:raise TypeError
        return r
    def ___is_same_file___(sf, lhs_file_path, rhs_file_path):
        'is_same_file :: lhs_file_path -> rhs_file_path -> bool #precondition: both exist and are files'
        #def _half_impl___is_same_file___(sf, lhs_file_path, rhs_file_path):
        if sf.always_tribool_as_is_or_not_same_file is not ...:
            return sf.always_tribool_as_is_or_not_same_file

        lsz = sf.lhs_access_file.get_file_size(lhs_file_path)
        rsz = sf.rhs_access_file.get_file_size(rhs_file_path)
        if lsz != rsz:
            return False
        elif sf.size_eq_as_same_file:
            return True

        lmay_hash_dict = sf.lhs_access_file.get_may_hash_method_uppercase_std_name2upper_hex_digest(lhs_file_path)
        rmay_hash_dict = sf.rhs_access_file.get_may_hash_method_uppercase_std_name2upper_hex_digest(rhs_file_path)
        if lmay_hash_dict is not None is not rmay_hash_dict:
            common_hash_names = set(lmay_hash_dict) & set(rmay_hash_dict)
            if not all(lmay_hash_dict[nm] == rmay_hash_dict[nm] for nm in common_hash_names):
                return False
            #elif sf.size_hash0_eq_as_same_file:
             #   return True
            elif common_hash_names and sf.hash_eq_as_same_file:
                return True
        ## no matter: hash dict is None or not common_hash_names
        if sf.size_hash0_eq_as_same_file:
            return True

        if sf.mtime_eq_as_same_file or sf.mtime_ne_as_not_same_file:
            lmay_str_mtime = sf.lhs_access_file.get_may_str_mtime(lhs_file_path)
            rmay_str_mtime = sf.rhs_access_file.get_may_str_mtime(rhs_file_path)

            if lmay_str_mtime is None or rmay_str_mtime is None:
                #raise TypeError
                pass
            else:
                lstr_mtime = lmay_str_mtime
                rstr_mtime = rmay_str_mtime
                if lstr_mtime == rstr_mtime:
                    if sf.mtime_eq_as_same_file:
                        return True
                else:
                    if sf.mtime_ne_as_not_same_file:
                        return False



        if sf.imay_max_size_threshold4cmp_content != -1:
            max_size_threshold4cmp_content = sf.imay_max_size_threshold4cmp_content

            assert lsz == rsz
            assert max_size_threshold4cmp_content >= 0
            if lsz > max_size_threshold4cmp_content:
                #skip cmp since too big
                return True
        with sf.lhs_access_file.open(lhs_file_path) as lfin, sf.rhs_access_file.open(rhs_file_path) as rfin:
            lfin
            rfin
            BLOCK_SIZE = sf._block_size
            while True:
                lbs = lfin.read(BLOCK_SIZE)
                if not lbs:
                    break
                rbs = rfin.read(BLOCK_SIZE)
                if lbs != rbs:
                    return False
            return True

def mk_is_same_file(lhs_access_file, rhs_access_file, /, *, always_tribool_as_is_or_not_same_file:'tribool'=..., size_eq_as_same_file:bool=False, size_hash0_eq_as_same_file:bool=False, hash_eq_as_same_file:bool=False, mtime_eq_as_same_file:bool=False, mtime_ne_as_not_same_file:bool=False, imay_max_size_threshold4cmp_content:int=-1, _block_size=2**8):
    r'''IAccessFile4MkIsSameFile -> IAccessFile4MkIsSameFile -> (is_same_file::MkIsSameFile)

    mk_is_same_file vs MkIsSameFile:
        * MkIsSameFile all kwargs except "_block_size" are required
        * mk_is_same_file all kwargs have default values
    #'''
    is_same_file = MkIsSameFile(lhs_access_file, rhs_access_file
        , always_tribool_as_is_or_not_same_file=always_tribool_as_is_or_not_same_file
        , size_eq_as_same_file=size_eq_as_same_file
        , size_hash0_eq_as_same_file=size_hash0_eq_as_same_file
        , hash_eq_as_same_file=hash_eq_as_same_file
        , mtime_eq_as_same_file=mtime_eq_as_same_file
        , mtime_ne_as_not_same_file=mtime_ne_as_not_same_file
        , imay_max_size_threshold4cmp_content=imay_max_size_threshold4cmp_content
        , _block_size=_block_size
        )
    return is_same_file

if __name__ == "__main__":
    xhs_access_file = AccessFile4MkIsSameFile__fsys()
    is_same_file = mk_is_same_file(xhs_access_file, xhs_access_file)
    xhs_dir_viewer = DirViewer__fsys()

    if 0:
        lhs_path = rhs_path = Path(r'/sdcard/0my_files/git_repos/python3_src/seed/verify/')
        print(list(dir_cmp(is_same_file, xhs_dir_viewer, lhs_path, xhs_dir_viewer, rhs_path, ignore_basename=None, ignore_relative_path=None, max_depth=None)))
        rhs_path = Path(r'/sdcard/0my_files/git_repos/python3_src/seed/debug/')
        print(list(dir_cmp(is_same_file, xhs_dir_viewer, lhs_path, xhs_dir_viewer, rhs_path, ignore_basename=None, ignore_relative_path=None, max_depth=None)))

    if 1:
        test_data_path = Path(__file__).parent/'_dir_cmp__test_data'

        lhs_path = test_data_path/'lhs'
        rhs_path = test_data_path/'rhs'

        ls = list(path2str4result_of_dir_cmp__relative(dir_cmp__relative(is_same_file, xhs_dir_viewer, lhs_path, xhs_dir_viewer, rhs_path, ignore_basename=None, ignore_relative_path=None, max_depth=None)))
        if 0:
            print(ls)
            from pprint import pprint
            pprint(ls)
        expected = \
            [(0, 'z/diff.txt')
            ,(-2, 'z/ld_rf')
            ,(2, 'z/lf_rd')
            ,(-1, 'z/lonlyd')
            ,(-1, 'z/lonlyf')
            ,(1, 'z/ronlyd')
            ,(1, 'z/ronlyf')
            ]
        assert ls == expected

        ls = list(path2str4result_of_dir_cmp__relative(dir_cmp__relative(is_same_file, xhs_dir_viewer, lhs_path, xhs_dir_viewer, rhs_path, ignore_basename=None, ignore_relative_path=None, max_depth=2)))
        assert ls == expected

        ls = list(path2str4result_of_dir_cmp__relative(dir_cmp__relative(is_same_file, xhs_dir_viewer, lhs_path, xhs_dir_viewer, rhs_path, ignore_basename=None, ignore_relative_path=None, max_depth=1)))
        assert ls != expected
        assert not ls

        ls = list(path2str4result_of_dir_cmp__relative(dir_cmp__relative(is_same_file, xhs_dir_viewer, lhs_path, xhs_dir_viewer, rhs_path, ignore_basename=[('-', [('fnmatch', r'*only*')])], ignore_relative_path=None, max_depth=None)))
        expected__ignore__only = \
            [(0, 'z/diff.txt')
            ,(-2, 'z/ld_rf')
            ,(2, 'z/lf_rd')
            ]
        assert ls == expected__ignore__only

        ls = list(path2str4result_of_dir_cmp__relative(dir_cmp__relative(is_same_file, xhs_dir_viewer, lhs_path, xhs_dir_viewer, rhs_path, ignore_basename=[('-', [('fnmatch', r'*only*'), ('re', r'lf.*')]), ('+', [('fnmatch', r'lonly*')])], ignore_relative_path=None, max_depth=None)))
        expected__ignore__only__but = \
            [(0, 'z/diff.txt')
            ,(-2, 'z/ld_rf')
            ,(-1, 'z/lonlyd')
            ,(-1, 'z/lonlyf')
            ]
        assert ls == expected__ignore__only__but

        ls = list(path2str4result_of_dir_cmp__relative(dir_cmp__relative(is_same_file, xhs_dir_viewer, lhs_path, xhs_dir_viewer, rhs_path, ignore_basename=None, ignore_relative_path=[('-', [('fnmatch', r'*only*'), ('re', r'lf.*')]), ('+', [('fnmatch', r'lonly*')])], max_depth=None)))
        assert ls == expected__ignore__only




ignorefile_line_regex = re.compile(r'\s*(?P<nonblank>(?:(?P<comment>#.*)|(?P<onoff_case>[-+])\s*(?P<pattern_case>\w+)\s*:(?P<pattern>.*)))?\n?')

def read_ignorefile(fin, /, *, may_pattern_case_set):
    r'''fin -> onoff_patterns_list
    line= \s*
        | \s*#.*
        | \s*[-+]{pattern_case!s}:{pattern!r}
    may_pattern_case_set:
        limit pattern_case
        e.g. "glob" -> NotImplementedError
        e.g. "re" -> py::re::syntax is too complex
            not good to be used at external file format, otherwise can only be read by.python!!!
        hence:
            may_pattern_case_set={'fnmatch'}
    #'''
    it = iter_read_ignorefile(fin, may_pattern_case_set=may_pattern_case_set)
    onoff_patterns_list = tuple(group_by(it, key=fst, container=lambda ps: tuple(map(snd, ps))))

    assert onoff_patterns_list == to_std_onoff_patterns_list(onoff_patterns_list)
    return onoff_patterns_list

def iter_read_ignorefile(fin, /, *, may_pattern_case_set):
    r'''fin -> Iter<(onoff_case, cased_pattern)>
    see: read_ignorefile
    #'''
    is_good_pattern_case = may_pattern_case_set2is_good_pattern_case(may_pattern_case_set)
    for line in fin:
        m = ignorefile_line_regex.fullmatch(line)
        if not m:
            raise ValueError(f'not ignorefile line: {line!r}')

        may_onoff_case = m.group('onoff_case')
        if may_onoff_case is None: continue
        onoff_case = m.group('onoff_case')
        pattern_case = m.group('pattern_case')
        if not is_good_pattern_case(pattern_case): raise ValueError((pattern_case, may_pattern_case_set))

        pattern = m.group('pattern')
        pattern = pattern.strip()
        pattern = ast.literal_eval(pattern)
        if type(pattern) is not str: raise TypeError
        cased_pattern = (pattern_case, pattern)
        yield (onoff_case, cased_pattern)


def read_ignorefile__text(text, /, *, may_pattern_case_set):
    fin = io.StringIO(text)
    onoff_patterns_list = read_ignorefile(fin, may_pattern_case_set=may_pattern_case_set)
    return onoff_patterns_list
def write_ignorefile__text(onoff_patterns_list, /, *, may_pattern_case_set):
    'see: read_ignorefile/write_ignorefile'
    onoff_patterns_list = to_std_onoff_patterns_list(onoff_patterns_list)

    fout = fin = io.StringIO()
    pos0 = fin.tell()

    write_ignorefile(fout, onoff_patterns_list, may_pattern_case_set=may_pattern_case_set)
    fin = fout

    if 0:
        fin.seek(pos0)
        assert_eq_f(onoff_patterns_list, read_ignorefile, fin, may_pattern_case_set=may_pattern_case_set)
    fin.seek(pos0)
    assert onoff_patterns_list == read_ignorefile(fin, may_pattern_case_set=may_pattern_case_set)
    text = fout.getvalue()
    return text

Set
def may_pattern_case_set2is_good_pattern_case(may_pattern_case_set):
    if may_pattern_case_set is None:
        def is_good_pattern_case(pattern_case):
            return type(pattern_case) is str
            return True
    else:
        pattern_case_set = may_pattern_case_set
        assert isinstance(pattern_case_set, Set)
        def is_good_pattern_case(pattern_case):
            return type(pattern_case) is str and pattern_case in pattern_case_set
    return is_good_pattern_case

def write_ignorefile(fout, onoff_patterns_list, /, *, may_pattern_case_set):
    'see: read_ignorefile'
    is_good_pattern_case = may_pattern_case_set2is_good_pattern_case(may_pattern_case_set)

    for onoff_case, cased_patterns in onoff_patterns_list:
        for pattern_case, pattern in cased_patterns:
            if not is_good_pattern_case(pattern_case): raise ValueError((pattern_case, may_pattern_case_set))
            fprint(f'{onoff_case!s}{pattern_case!s}:{pattern!r}', file=fout)
        fprint(file=fout)

if __name__ == "__main__":
    #test
    onoff_patterns_list = [('-', [('fnmatch', r'*only*'), ('re', r'lf.*')]), ('+', [('fnmatch', r'lonly*')])]
    text = write_ignorefile__text(onoff_patterns_list, may_pattern_case_set=None)
    assert read_ignorefile__text(text, may_pattern_case_set=None) == to_std_onoff_patterns_list(onoff_patterns_list)



def main(args=None):
    import argparse
    from seed.io.may_open import may_open_stdout

    parser = argparse.ArgumentParser(
        description='directory compare'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('lhs_path', type=Path#, required=True
                        , help='input lhs path')
    parser.add_argument('rhs_path', type=Path#, required=True
                        , help='input rhs path')

    parser.add_argument('-d', '--max_depth', type=int, default=None
                        , help='max_depth >= -1; if max_depth==-1(default) then no limits else file/dir whose depth > max_depth will be ignored')
    parser.add_argument('-ig', '--ignorefile', type=str, default=None
                        , help='ignorefile path')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-ige', '--ignorefile_encoding', type=str
                        , default='utf8'
                        , help='ignorefile encoding')
    parser.add_argument('-oe', '--output_file_encoding', type=str
                        , default='utf8'
                        , help='output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    parser.add_argument('-r', '--relative', action='store_true'
                        , default = False
                        , help='output one relative_path per entry payload')
    parser.add_argument('-ls', '--list', action='store_true'
                        , default = False
                        , help='output one python list object repr; default: output one entry per line')
    parser.add_argument('-pp', '--pprint', action='store_true'
                        , default = False
                        , help='if "--list", output one python list object repr as pprint; default: output in single line')
    parser.add_argument('--print_Path', action='store_true'
                        , default = False
                        , help='show path as Path object; default: convert to str')
    parser.add_argument('-t', '--cmp_fsys_tree_only', action='store_true'
                        , default = False
                        , help='donot cmp file contents')
    parser.add_argument('--size_eq_as_same_file', action='store_true'
                        , default = False
                        , help='one of mk_is_same_file kwargs')
    parser.add_argument('--size_hash0_eq_as_same_file', action='store_true'
                        , default = False
                        , help='one of mk_is_same_file kwargs')
    parser.add_argument('--hash_eq_as_same_file', action='store_true'
                        , default = False
                        , help='one of mk_is_same_file kwargs')
    parser.add_argument('--mtime_eq_as_same_file', action='store_true'
                        , default = False
                        , help='one of mk_is_same_file kwargs')
    parser.add_argument('--mtime_ne_as_not_same_file', action='store_true'
                        , default = False
                        , help='one of mk_is_same_file kwargs')
    parser.add_argument('--max_size_threshold4cmp_content', type=int, default=-1
                        , help='max_size_threshold4cmp_content >= -1; if max_size_threshold4cmp_content==-1(default) then no limits else file whose size > max_size_threshold4cmp_content will be skip cmp content')

    args = parser.parse_args(args)
    max_depth = args.max_depth
    imay_max_size_threshold4cmp_content = args.max_size_threshold4cmp_content
    igencoding = args.ignorefile_encoding
    oencoding = args.output_file_encoding
    omode = 'wt' if args.force else 'xt'
    g = dir_cmp__relative if args.relative else dir_cmp
    if args.print_Path:
        f = g
    else:
        def f(*_args, **kwargs):
            #bug:return path2str4dir_cmp_result(g(*_args, relative=args.relative, **kwargs))
            return path2str4dir_cmp_result(g(*_args, **kwargs), relative=args.relative)

    if args.cmp_fsys_tree_only:
        is_same_file = is_same_file__True
    else:
        r'''
        size_eq_as_same_file
        size_hash0_eq_as_same_file
        hash_eq_as_same_file
        mtime_eq_as_same_file
        mtime_ne_as_not_same_file
        imay_max_size_threshold4cmp_content
        #'''
        xhs_access_file = AccessFile4MkIsSameFile__fsys()
        is_same_file = mk_is_same_file(
            xhs_access_file
            , xhs_access_file
            , size_eq_as_same_file=args.size_eq_as_same_file
            , size_hash0_eq_as_same_file=args.size_hash0_eq_as_same_file
            , hash_eq_as_same_file=args.hash_eq_as_same_file
            , mtime_eq_as_same_file=args.mtime_eq_as_same_file
            , mtime_ne_as_not_same_file=args.mtime_ne_as_not_same_file
            #, imay_max_size_threshold4cmp_content=args.imay_max_size_threshold4cmp_content
            , imay_max_size_threshold4cmp_content=args.max_size_threshold4cmp_content
            )
    is_same_file


    xhs_dir_viewer = DirViewer__fsys()

    may_ignorefile_path = args.ignorefile
    if may_ignorefile_path is None:
        ignore_relative_path = None
    else:
        ignorefile_path = may_ignorefile_path
        with open(ignorefile_path, 'rt', encoding=igencoding) as fin:
            onoff_patterns_list = read_ignorefile(fin, may_pattern_case_set=None)
        ignore_relative_path = onoff_patterns_list
    ignore_relative_path

    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=oencoding) as fout:
        it = f(is_same_file, xhs_dir_viewer, args.lhs_path, xhs_dir_viewer, args.rhs_path, ignore_basename=None, ignore_relative_path=ignore_relative_path, max_depth=max_depth)
        if args.list:
            if args.pprint:
                i = -1
                for i, x in enumerate(it):
                    h = '[' if i == 0 else ','
                    fprint(f'{h!s}{x!r}', file=fout)
                else:
                    i += 1
                if i:
                    fprint(']', file=fout)
                else:
                    fprint('[]', file=fout)
            else:
                ls = list(it)
                fprint(ls, file=fout)
        else:
            for x in it:
                fprint(x, file=fout)




def _t():
    r'''
    #try fnmatch to match __pycache__ .git ...
    #
    #onoff_patterns_list2ignore_str

=======
python3_src/./
python3_src/../
python3_src/.git/
python3_src/.gitignore
view ../../python3_src/.gitignore
=======
# exclude everything except directory foo/bar
#    /*
#    !/foo
#    /foo/*
#    !/foo/bar
#
#python cache
/**/__pycache__
/java_src/**/*.class
#
#ply PLY yacc output
/**/parsetab.py
/**/parser.out
#
#mypy - static typing information
/**/.mypy_cache

=======

    #'''

    may_pattern_case_set = {'fnmatch'}
    onoff_patterns_list = [('-', [('fnmatch', '__pycache__'), ('fnmatch', '__pycache__/*'), ('fnmatch', '*/__pycache__'), ('fnmatch', '*/__pycache__/*'),    ('fnmatch', '.?*'), ('fnmatch', '.?*/*'), ('fnmatch', '*/.?*'), ('fnmatch', '*/.?*/*')])]
    onoff_patterns_list = [('-', [('fnmatch', '__pycache__'), ('fnmatch', '__pycache__/*'), ('fnmatch', '*/__pycache__'), ('fnmatch', '*/__pycache__/*'),    ('fnmatch', '.?*'), ('fnmatch', '*/.?*')])]
    ignore_str = onoff_patterns_list2ignore_str(onoff_patterns_list)

    ls = [
        '.'
        ,'..'
        ,'wgit'
        ,'.git'
        ,'x/.git'
        ,'x/.git/y'
        ,'.git/'
        ,'/.git/'
        ,'./.git/'
        ]
    holds = ['.', 'wgit']
    for s in ls:
        if ignore_str(s):
            #print(fr'ignore: {s!r}')
            assert s not in holds
        else:
            #print(fr'hold: {s!r}')
            assert s in holds
_t()

if __name__ == "__main__":
    main()

