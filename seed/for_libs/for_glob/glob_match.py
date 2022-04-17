
r'''
seed.for_libs.for_glob.glob_match

py -m seed.for_libs.for_glob.glob_match
py -m nn_ns.app.debug_cmd seed.for_libs.for_glob.glob_match

from seed.for_libs.for_glob.glob_match import glob_match, glob_match_, GlobMatcher, path2std_path_parts, to_std_path_parts, check_basename, check_path, check_path__str, check_path__PurePath, is_path_always_dir, is_path_always_dir__PurePath, is_path_always_dir__str


#'''


___begin_mark_of_excluded_global_names__0___ = ...
__all__ = '''
    glob_match
        glob_match_
            GlobMatcher

    path2std_path_parts
        to_std_path_parts

    check_basename
    check_path
        check_path__str
        check_path__PurePath

    is_path_always_dir
        is_path_always_dir__PurePath
        is_path_always_dir__str

    '''.split()

from pathlib import PurePath #PurePosixPath
import os
import fnmatch #fnmatchcase
import glob
___end_mark_of_excluded_global_names__0___ = ...


def _t():
    p = PurePath('/a/x/') #remove last '/'
    #print(p)
    assert str(p) == '/a/x'
    #print(os.path.split(p))
    assert os.path.split(p) == ('/a', 'x')

    #print(os.path.split('/a/x/'))
    assert os.path.split('/a/x/') == ('/a/x', '')

    s2ans = {
        'a':('', 'a')
        ,'.':('', '.')
        ,'/':('/', '')
        }
    for s, ans in s2ans.items():
        p = PurePath(s)
        #print(os.path.split(p))
        assert os.path.split(p) == ans

_t()

def check_std_path_parts(path_parts, /):
    if not type(path_parts) is tuple: raise TypeError
    for driver_or_basename in path_parts[:1]:
        check_driver_or_basename(driver_or_basename)
    for basename in path_parts[1:]:
        check_basename(basename)
def check_driver_or_basename(driver_or_basename, /):
    check_path__str(driver_or_basename)
    if not driver_or_basename: raise ValueError
    if not os.path.split(driver_or_basename) in [('', driver_or_basename), (driver_or_basename, '')]: raise ValueError(fr'driver_or_basename={driver_or_basename!r}')
def check_basename(basename, /):
    check_path__str(basename)
    if not basename: raise ValueError
    if not ('', basename) == os.path.split(basename): raise ValueError(fr'basename={basename!r}')

def check_path__str(path, /):
    if not type(path) is str: raise TypeError
    if not path: raise ValueError
def check_path__PurePath(path, /):
    if not isinstance(path, PurePath): raise TypeError


def check_path(path, /):
    if type(path) is str:
        f = check_path__str
    else:
        f = check_path__PurePath
    f(path)
def is_path_always_dir(path, /):
    if type(path) is str:
        f = is_path_always_dir__str
    else:
        f = is_path_always_dir__PurePath
    b = f(path)
    if not type(b) is bool: raise TypeError
    return b

def is_path_always_dir__PurePath(path, /):
    check_path__PurePath(path)
    return is_path_always_dir__str(str(path))

def is_path_always_dir__str(path, /):
    check_path__str(path)
    dirname, basename = os.path.split(path)
    #if not basename: return True
    return basename in '..' # ('', '.', '..')

def glob_match(glob_pattern:str, path, /, *,, is_path_dir__tribool, match_dir_only:bool, ignore_case:bool, recursive:bool):
    '-> bool #match or not #is_path_dir__tribool may come from os.isdir(path)'
    check_path__str(glob_pattern)



    if match_dir_only:
        pass
    elif 0:
        pattern_dirname, pattern_basename = os.path.split(glob_pattern)
        #err@'/a/x/'-->('/a/x', ''): if not (pattern_dirname == pathname) is (not pattern_basename): raise logic-err
        match_dir_only = False
        if os.path.glob_pattern[-1:] in ('/', '\\') or not pattern_basename:
             match_dir_only = True
    else:
        match_dir_only = is_path_always_dir(glob_pattern)
    match_dir_only

    if is_path_always_dir(path):
        if is_path_dir__tribool is False and is_path_always_dir(path): raise ValueError
        is_path_dir__tribool = True

    glob_pattern_parts = path2std_path_parts(glob_pattern)
    path_parts = path2std_path_parts(path)
    return glob_match_(glob_pattern_parts, path_parts, is_path_dir__tribool=is_path_dir__tribool, match_dir_only=match_dir_only, ignore_case=ignore_case, recursive=recursive)
def to_std_path_parts(path_parts, /):
    std_path_parts = tuple(path_parts)
    check_std_path_parts(std_path_parts)
    return std_path_parts
def path2std_path_parts(path, /):
    if 0:
        ###ver1: bad for '.' ==>> ()
        if type(path) is str:
            path = PurePath(path)
        return to_std_path_parts(path.parts)
    else:
        ###ver2
        if type(path) is str:
            ls = []
            while path:
                dirname, basename = os.path.split(path)
                if dirname == path:
                    driver = dirname
                    ls.append(driver)
                    break
                ls.append(basename)#may be empty str
                path = dirname
            ls.reverse()
            if ls and not ls[-1]:
                ls.pop()
                assert ls
                assert ls[-1]
            assert all(ls)
            return to_std_path_parts(ls)
        else:
            return to_std_path_parts(path.parts)

def glob_match_(glob_pattern_parts:'[str]', path_parts:'[str]', /, *,, is_path_dir__tribool, match_dir_only:bool, ignore_case:bool, recursive:bool):
    '-> bool #match or not #is_path_dir__tribool may come from os.isdir(path)'
    if not id(is_path_dir__tribool) in [*map(id, [..., True, False])]: raise TypeError
    if match_dir_only and is_path_dir__tribool is False: return False


    path_parts = to_std_path_parts(path_parts)
    matcher = GlobMatcher(glob_pattern_parts, ignore_case=ignore_case, recursive=recursive)

    return matcher.match(path_parts)


class GlobMatcher:
    r'''
    st :: frozenset<idx4glob_pattern_parts>
    #'''

    def __init__(sf, glob_pattern_parts:'[str]', /, *,, ignore_case:bool, recursive:bool):
        if not type(recursive) is bool: raise TypeError
        if not type(ignore_case) is bool: raise TypeError

        glob_pattern_parts = to_std_path_parts(glob_pattern_parts)
        for glob_pattern_part in glob_pattern_parts:
            if '**' in glob_pattern_part and not (len(glob_pattern_part) == 2 and recursive): raise ValueError
        #

        #remove duplicate neibourhood '**'
        ls = []
        is_prev_starstar = False
        for glob_pattern_part in glob_pattern_parts:
            is_curr_starstar = glob_pattern_part == '**'
            if is_curr_starstar and is_prev_starstar:
                #skip append <==> remove
                continue
            else:
                is_prev_starstar = is_curr_starstar
                ls.append(glob_pattern_part)
        sf.glob_pattern_parts = to_std_path_parts(ls)
        sf.ignore_case = ignore_case
        sf.__has_states_always_success = sf._has_states_always_success()
    def _complete_state(sf, idc, /):
        idc = set(idc)
        sf.check_incomplete_state(frozenset(idc))

        st = set()
        ls = sf.glob_pattern_parts
        L = len(ls)

        while idc:
            # idc & st === {/}
            i = idc.pop()
            if not 0 <= i <= L: raise ValueError
            st.add(i)
            if i < L and ls[i] == '**':
                j = i+1
                if j not in st:
                    idc.add(j)
        return frozenset(st)
    def is_state_fail(sf, st, /):
        return not st
    def is_state_success(sf, st, /):
        L = len(sf.glob_pattern_parts)
        return L in st
    def is_state_always_success(sf, st, /):
        if not sf.has_states_always_success(): raise logic-err#--should-test-first
        L = len(sf.glob_pattern_parts)
        return L in st and (L-1) in st
    def has_states_always_success(sf, /):
        return sf.__has_states_always_success
    def _has_states_always_success(sf, /):
        ls = sf.glob_pattern_parts
        return ls and ls[-1] == '**'
    def check_incomplete_state(sf, st, /):
        if not type(st) is frozenset: raise TypeError
        if not all(type(i) is int for i in st): raise TypeError
        L = len(sf.glob_pattern_parts)
        if not all(0 <= i <= L for i in st): raise ValueError

    def get_init_state(sf, /):
        st0 = sf._complete_state([0])
        sf.check_incomplete_state(st0)
        return st0
    def match(sf, path_parts, /):
        it = iter(path_parts)

        for path_part in it:
            st = sf.feed__first(path_part)
            break
        else:
            st = sf.get_init_state()

        if sf.has_states_always_success():
            is_state_always_success = sf.is_state_always_success
        else:
            def is_state_always_success(st):
                return False

        for path_part in it:
            #not:if sf.is_state_always_success(st): break
            if is_state_always_success(st): break
            if sf.is_state_fail(st):break
            st = sf.feed__not_first(st, path_part)
        return sf.is_state_success(st)
    def feed__first(sf, path_part, /):
        '-> st'
        st0 = sf.get_init_state()
        new_st = sf.feed(st0, path_part, is_first_feed=True)
        return new_st
    def feed__not_first(sf, st, path_part, /):
        '-> st'
        new_st = sf.feed(st, path_part, is_first_feed=False)
        return new_st
    def feed(sf, st, path_part, /, *,, is_first_feed:bool):
        '-> st'
        if is_first_feed:
            check_driver_or_basename(path_part)
        else:
            check_basename(path_part)
        sf.check_incomplete_state(st)

        ls = sf.glob_pattern_parts
        L = len(ls)
        fnmatch_ = fnmatch.fnmatch if sf.ignore_case else fnmatch.fnmatchcase

        idc = []
        for i in st:
            if i == L: continue
            glob_pattern_part = ls[i]
            if glob_pattern_part == '**':
                if i+1 not in st: raise ValueError(fr'incomplete_state@feed')
                matched = True
                idc.append(i) #not step
            else:
                fnmatch_pattern = glob_pattern_part
                matched = fnmatch_(path_part, fnmatch_pattern)
            #
            if matched:
                idc.append(i+1)
        new_st = sf._complete_state(idc)
        sf.check_incomplete_state(new_st)
        return new_st


def _t():
    pattern2paths = {
        }
    d = dict(is_path_dir__tribool=..., match_dir_only=False, ignore_case=False, recursive=True)
    assert glob_match('/a/**/b/**/c', '/a/b/c', **d)
    assert glob_match('/a/**/b/**/c', '/a/x/b/c', **d)
    assert glob_match('/a/**/b/**/c', '/a/x/w/b/y/z/c', **d)
    assert glob_match('/a/**/b/**/c', '/a/b/y/z/c', **d)
    assert not glob_match('/a/**/b/**/c', '/a/bx/y/z/c', **d)
    assert glob_match('**', '/a/b/y/z/c', **d)

    assert glob_match('**', '/', **d)
    assert glob_match('**', '.', **d)
    assert glob_match('**', 'a', **d)

    assert glob_match('**/', '/', **d)
    assert glob_match('**/', '.', **d)
    assert glob_match('**/', 'a', **d)

    if 1:
        assert fnmatch.fnmatch('.', '?')
        #!!!using path_parts has some problem
        if 0:
            #ver1@path2std_path_parts
            assert not glob_match('**/?/**', '.', **d)
            assert not glob_match('?', '.', **d)
        else:
            assert not glob_match('**/?/**', PurePath('.'), **d)
            assert not glob_match('?', PurePath('.'), **d)
            assert glob_match('**/?/**', '.', **d)
            assert glob_match('?', '.', **d)

    assert glob_match('**/?/**', '/', **d)
    assert glob_match('**/?/**', 'a', **d)
    assert glob_match('**/?/**', 'xx/xxx/a/xxx/xxx', **d)

_t()
