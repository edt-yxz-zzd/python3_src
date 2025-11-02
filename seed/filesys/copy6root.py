#__all__:goto
r'''[[[
e ../../python3_src/seed/filesys/copy6root.py
view ../../python3_src/nn_ns/app/copy6root_cmd.py

seed.filesys.copy6root
py -m nn_ns.app.debug_cmd   seed.filesys.copy6root -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.filesys.copy6root:__doc__ -ht # -ff -df

[[
copy6root -to <dst_root_dir> -from <src_root_dir>   -- <relative_paths4both_src_dst...>
    auto mkdir

example:
copy6root   -to script/png/   -from /sdcard/0my_files/tmp/out4py/py_src/  -v -ig  --  site-packages/PIL/_binary.py site-packages/PIL/PngImagePlugin.py site-packages/png/
]]
[[
mkdir $my_tmp/out4cp/trials/
cd $my_tmp/out4cp/trials/
mkdir -p a/b/c/d/e
mkdir -p to
cd a
touch b/c/d/e/null.txt
cp -iv --parents b/c/d/e/null.txt ../to/
  b -> ../to/b
  b/c -> ../to/b/c
  b/c/d -> ../to/b/c/d
  b/c/d/e -> ../to/b/c/d/e
  'b/c/d/e/null.txt' -> '../to/b/c/d/e/null.txt'
cd ..
mkdir -p x/y
cd x/y
cp -iv --parents ../../a/b/c/d/e/null.txt ../../to/
    ../../a -> ../../to/../../a
    ../../a/b -> ../../to/../../a/b
    ../../a/b/c -> ../../to/../../a/b/c
    ../../a/b/c/d -> ../../to/../../a/b/c/d
    ../../a/b/c/d/e -> ../../to/../../a/b/c/d/e
    '../../a/b/c/d/e/null.txt' -> '../../to/../../a/b/c/d/e/null.txt'
ls ../../to/../../a/b/c/d/e/null.txt
ls $my_tmp/out4cp/a/b/c/d/e/null.txt
  ###go to weird place...

]]
[[
view others/app/termux/help/cp.man.txt
       --parents
              use full source file name under DIRECTORY
       -i, --interactive
              prompt before overwrite (overrides a previous -n option)
       -f, --force
              if an existing destination file cannot be opened, remove it and
              try again (this option is ignored when the -n option is also
              used)

       -n, --no-clobber
              do not overwrite an existing file (overrides a previous -i
              option)

       -H     follow command-line symbolic links in SOURCE

       -L, --dereference
              always follow symbolic links in SOURCE

       -P, --no-dereference
              never follow symbolic links in SOURCE

]]



'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.filesys.copy6root   @f
]]]'''#'''
__all__ = r'''
copy6root
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
#import os.path # os.path.relpath

#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__, 'Path:mk_Path'):
    from seed.debug.print_err import print_err
    from seed.filesys.is_absolute_path import check_relative_path #is_relative_path, is_absolute_path, check_relative_path, check_absolute_path, NotARelativePathError, NotAnAbsolutePathError
    from pathlib import Path as mk_Path
    from shutil import copy2, copytree
        #shutil.copy2(src_path, tgt_dir_or_dst_path, *, follow_symlinks=True) -> dst_path{with metadata}
        #shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)

#.#################################
___end_mark_of_excluded_global_names__0___ = ...


__all__




def copy6root(dst_root_dir, src_root_dir, relative_paths4both_src_dst, /, *, dst_root_dir_nonexist_ok=False, skip_when_dst_file_exist=False, overwrite_when_dst_file_exist=False, interactive_when_dst_file_exist=False, verbose=False):
    'dst_root_dir/path -> src_root_dir/path -> relative_paths4both_src_dst/[path] -> None|^Exception/OSError'
    #######
    verbose = bool(verbose)
    skip_when_dst_file_exist = bool(skip_when_dst_file_exist)
    overwrite_when_dst_file_exist = bool(overwrite_when_dst_file_exist)
    interactive_when_dst_file_exist = bool(interactive_when_dst_file_exist)
    if sum([skip_when_dst_file_exist, overwrite_when_dst_file_exist, interactive_when_dst_file_exist]) > 1: raise TypeError
    raise_when_dst_file_exist = not (skip_when_dst_file_exist or overwrite_when_dst_file_exist or interactive_when_dst_file_exist)
    my_kwds = dict(skip_when_dst_file_exist=skip_when_dst_file_exist, overwrite_when_dst_file_exist=overwrite_when_dst_file_exist, interactive_when_dst_file_exist=interactive_when_dst_file_exist, raise_when_dst_file_exist=raise_when_dst_file_exist, verbose=verbose)
    assert sum(my_kwds.values()) == 1+verbose
    #######
    dst_root_dir = mk_Path(dst_root_dir)
    src_root_dir = mk_Path(src_root_dir)
    relative_paths4both_src_dst = tuple(map(mk_Path, relative_paths4both_src_dst))
    #######
    if not src_root_dir.is_dir():
        if src_root_dir.exists():
            raise NotADirectoryError(src_root_dir)
        raise FileNotFoundError(src_root_dir)
    #######
    for relative_path8xxx in relative_paths4both_src_dst:
        check_relative_path(relative_path8xxx)
            # ^NotARelativePathError
    #######
    paths8src = tuple((src_root_dir/relative_path8xxx).absolute() for relative_path8xxx in relative_paths4both_src_dst)
    for j, src_path in enumerate(paths8src):
        if not src_path.exists():
            #.raise FileNotFoundError(src_root_dir, relative_paths4both_src_dst[j])
            raise FileNotFoundError(src_path)
    #######
    #for j, src_path in enumerate(paths8src): os.path.relpath(src_path, start=src_root_dir):
    #######
    if not dst_root_dir.is_dir():
        if dst_root_dir.exists():
            raise NotADirectoryError(dst_root_dir)
        if not dst_root_dir_nonexist_ok:
            raise FileNotFoundError(dst_root_dir)
        dst_root_dir.mkdir(parents=True)
    #######
    assert src_root_dir.is_dir()
    assert dst_root_dir.is_dir()
    if dst_root_dir.samefile(src_root_dir):
        return
    #######
    paths8dst = tuple((dst_root_dir/relative_path8xxx).absolute() for relative_path8xxx in relative_paths4both_src_dst)
    if raise_when_dst_file_exist:
      for j, dst_path in enumerate(paths8dst):
        if dst_path.exists():
            #.raise FileExistsError(dst_root_dir, relative_paths4both_src_dst[j])
            raise FileExistsError(dst_path)
    #######
    dst_path_set = set()
    copy2__with_my_kwds_ = _mk_copy2(dst_path_set, **my_kwds)
    for src_path, dst_path in zip(paths8src, paths8dst):
        dst_dir = dst_path.parent
        if not dst_dir.exists():
            if verbose:print_err(f'mkdir:{dst_dir}')
            dst_dir.mkdir(parents=True)
            if verbose:print_err(f'mkdir:{dst_dir}')

        if src_path.is_dir():
            copytree(src_path, dst_path, dirs_exist_ok=True, copy_function=copy2__with_my_kwds_)
        else:
            copy2__with_my_kwds_(src_path, dst_path)
        #dst_path_set.add(dst_path.resolve())
    #######

def _mk_copy2(dst_path_set, /, *, skip_when_dst_file_exist, overwrite_when_dst_file_exist, interactive_when_dst_file_exist, raise_when_dst_file_exist, verbose):
    def copy2__with_my_kwds_(src_path, dst_path, /, **copy2_kwds):
        #if verbose:print_err(f'???copy???:{src_path} -?-> {dst_path}')
        _overwrite_when_dst_file_exist = False
        _skip_when_dst_file_exist = False
        src_path = mk_Path(src_path)
        if src_path.is_dir():
            raise IsADirectoryError(src_path)
        dst_path = mk_Path(dst_path)
        #bug:_dst_path = dst_path.resolve()
        #   !! dst_path may not exist
        if dst_path.exists():
            if dst_path.is_dir():
                raise IsADirectoryError(dst_path)
            _dst_path = dst_path.resolve()
            if _dst_path in dst_path_set:
                if verbose:print_err(f'duplicated:{dst_path}')
                return dst_path

            #####
            if interactive_when_dst_file_exist:
                while 1:
                    s = input(f'overwrite {dst_path!r}? [#n(skip),y(overwrite)#] (n/y)? ')
                    s = s.lower()
                    match s:
                        case 'y' | 'yes':
                            _overwrite_when_dst_file_exist = True
                        case 'n' | 'no':
                            _skip_when_dst_file_exist = True
                        case _:
                            continue
                    break
            #####
            if skip_when_dst_file_exist or _skip_when_dst_file_exist:
                if verbose:print_err(f'skip:{dst_path}')
                return dst_path
            if raise_when_dst_file_exist:
                # ???data-race???
                raise FileExistsError(dst_path)
            # not duplicated
            # not skip_when_dst_file_exist
            # not raise_when_dst_file_exist
            # not interactive_when_dst_file_exist
            # => overwrite_when_dst_file_exist

            if not (overwrite_when_dst_file_exist or _overwrite_when_dst_file_exist):
                #.raise FileExistsError(dst_path)
                raise 000
            assert (overwrite_when_dst_file_exist or _overwrite_when_dst_file_exist)
        assert (overwrite_when_dst_file_exist or _overwrite_when_dst_file_exist) or not dst_path.exists()
        r = copy2(src_path, dst_path, **copy2_kwds)
        if verbose:print_err(f'copy:{src_path} --> {dst_path}')
        dst_path_set.add(_dst_path:=dst_path.resolve())
        return r
    return copy2__with_my_kwds_












__all__
from seed.filesys.copy6root import copy6root
from seed.filesys.copy6root import *
