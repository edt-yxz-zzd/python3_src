r"""
nn_ns.filedir.filedir_ops
see:
    seed.for_libs.for_glob.glob_match

from nn_ns.filedir.filedir_ops import mk_Path, path_partial_cmp, path_lt, path_le, is_dir_empty, remove_dirs, filedir_move_then_remove_dirs, filedir_move_ex, filedir_replace, filedir_remove, filedir_move, filedir_copy

#"""


__all__ = '''
    mk_Path
    path_partial_cmp
    path_lt
    path_le

    is_dir_empty
    remove_dirs


    filedir_move_then_remove_dirs
    filedir_move_ex
    filedir_replace
    filedir_remove
    filedir_move
    filedir_copy
    '''.split()



from pathlib import Path, PurePosixPath #as_posix
import os.path
import shutil

from seed.iters.calc_common_prefix_length import calc_common_prefix_length
from seed.tiny import sign_of

def mk_Path(path, /):
    if type(path) is not Path:
        path = Path(path)
    return path

def path_partial_cmp(lhs_path, rhs_path, /):
    '->(-1|0|+1|None)'
    lhs_path = mk_Path(lhs_path)
    rhs_path = mk_Path(rhs_path)

    strict = False
    lhs_path = lhs_path.resolve(strict=strict)
    rhs_path = rhs_path.resolve(strict=strict)
    lhs_path_parts = lhs_path.parts
    rhs_path_parts = rhs_path.parts

    L = calc_common_prefix_length(lhs_path_parts, rhs_path_parts)
    lsz = len(lhs_path_parts)
    rsz = len(rhs_path_parts)

    if L != min(lsz, rsz):
        return None
    else:
        return sign_of(lsz - rsz)

def path_lt(lhs_path, rhs_path, /):
    return path_partial_cmp(lhs_path, rhs_path) == -1
def path_le(lhs_path, rhs_path, /):
    return path_partial_cmp(lhs_path, rhs_path) in (-1, 0)

    lhs_path = mk_Path(lhs_path)
    rhs_path = mk_Path(rhs_path)
    try:
        rhs_path.relative_to(lhs_path)
    except ValueError:
        return False
    else:
        return True
def is_dir_empty(path, /):
    path = mk_Path(path)

    for _ in path.iterdir():
        return False
    else:
        return True
#filedir_moves
#filedir_move_then_remove_dirs
def filedir_move_then_remove_dirs(*, to_path, from_path, may_root_dir_path4from, exist_ok):
    'remove empty dir until root #see:os.removedirs/makedirs/renames'
    filedir_move_ex(from_path=from_path, to_path=to_path, exist_ok=exist_ok)

    if 1:
        remove_dirs(from_path.parent, may_root_dir_path=may_root_dir_path4from, missing_ok=False, target_dir_nonempty_ok2halt=True, target_dir_nonempty_ok2remove=False, target_path_is_file_ok2remove=False, target_path_is_file_ok2halt=False, target_dir_path_is_root_dir_path_ok=True)
        #   from_path be moved, from_path.parent exist==>>missing_ok=False,target_dir_nonempty_ok2halt=True,target_dir_path_is_root_dir_path_ok=True,target_path_is_file_ok2halt=False
            #
            #not bug:target_dir_nonempty_ok2halt=True

    else:
        remove_dirs(from_path, may_root_dir_path=may_root_dir_path4from, missing_ok=True, target_dir_nonempty_ok2halt=False, target_dir_nonempty_ok2remove=False, target_path_is_file_ok2remove=False, target_path_is_file_ok2halt=False, target_dir_path_is_root_dir_path_ok=False)
        #   required: may_root_dir_path4from < from_path==>>target_dir_path_is_root_dir_path_ok=False
        #   from_path be moved, not exist==>>missing_ok=True,target_dir_nonempty_ok2halt=False,target_dir_path_is_root_dir_path_ok=False,target_path_is_file_ok2halt=False

def remove_dirs(target_dir_path, /,*, may_root_dir_path, missing_ok, target_dir_nonempty_ok2halt, target_dir_nonempty_ok2remove, target_path_is_file_ok2halt, target_path_is_file_ok2remove, target_dir_path_is_root_dir_path_ok):
    r'''remove empty dir until root #see:os.removedirs/makedirs/renames
    os.removedirs until not empty
        but required leaf_dir empty
        and not bounded by root

    if target_dir_nonempty_ok2halt=True and target_file_or_dir_path.is_dir() and not is_dir_empty(target_file_or_dir_path): cancel remove_dirs
    if target_dir_nonempty_ok2remove=True and target_file_or_dir_path.is_dir() and not is_dir_empty(target_file_or_dir_path): clear target_dir_path first

    #'''
    if target_dir_nonempty_ok2halt and target_dir_nonempty_ok2remove: raise ValueError
    if target_path_is_file_ok2halt and target_path_is_file_ok2remove: raise ValueError
    if target_dir_path_is_root_dir_path_ok and target_dir_nonempty_ok2remove: raise ValueError


    target_file_or_dir_path = target_dir_path
    del target_dir_path
    target_file_or_dir_path = mk_Path(target_file_or_dir_path)

    return_directly = False
    if may_root_dir_path is not None:
        root_dir_path = may_root_dir_path
    else:
        root_dir_path = target_file_or_dir_path.anchor
    ##
    root_dir_path = mk_Path(root_dir_path)
    if not root_dir_path.is_dir(): raise NotADirectoryError
    pcmp = path_partial_cmp(root_dir_path, target_file_or_dir_path)
    if pcmp == 0:
        #root_dir_path == target_file_or_dir_path
        #target_file_or_dir_path is_dir
        _target_dir_path = target_file_or_dir_path
        return_directly = True

    if target_dir_path_is_root_dir_path_ok:
        if not pcmp in (-1, 0): raise ValueError('target_file_or_dir_path not under root_dir_path')
    else:
        if not pcmp == -1: raise ValueError('target_file_or_dir_path not under root_dir_path')
        #target_file_or_dir_path is not root_dir_path

    if not target_file_or_dir_path.exists():
        if not missing_ok: raise FileNotFoundError
    else:
        #exists
        if target_file_or_dir_path.is_dir():
            #bug?:if not target_dir_nonempty_ok2halt and is_dir_empty(target_file_or_dir_path): raise RuntimeError
            if not (target_dir_nonempty_ok2halt or target_dir_nonempty_ok2remove or is_dir_empty(target_file_or_dir_path)): raise RuntimeError
                #not to remove nonempty target dir  or   to remove empty target dir
            if target_dir_nonempty_ok2remove or is_dir_empty(target_file_or_dir_path):
                #to remove empty/nonempty target dir
                #target_file_or_dir_path is_dir
                _target_dir_path = target_file_or_dir_path
                pass
            else:
                #nonempty only
                #not to remove nonempty target dir
                assert target_dir_nonempty_ok2halt
                return_directly = True
        elif target_file_or_dir_path.is_file():
            if not (target_path_is_file_ok2halt or target_path_is_file_ok2remove): raise NotADirectoryError
            _target_file_path = target_file_or_dir_path
            #target_file_or_dir_path is_file
            if target_path_is_file_ok2halt:
                return_directly = True
            else:
                assert target_path_is_file_ok2remove
        else:
            raise RuntimeError(f'unknown file type: {target_file_or_dir_path!r}')


    ####
    if return_directly:
        leaf_path = target_file_or_dir_path
        #leaf_dir_path = _target_dir_path
        #leaf_file_path = _target_file_path
    else:
        #root_dir_path < target_file_or_dir_path

        assert (not target_file_or_dir_path.exists() and missing_ok)  or  (target_file_or_dir_path.is_file() and not target_path_is_file_ok2halt and target_path_is_file_ok2remove)  or  (target_file_or_dir_path.is_dir() and (is_dir_empty(target_file_or_dir_path) or (target_dir_nonempty_ok2remove and not target_dir_nonempty_ok2halt)))

        #assert (not target_file_or_dir_path.exists() and missing_ok)  or  (target_file_or_dir_path.is_dir() and is_dir_empty(target_file_or_dir_path))
            #not file  and not nonempty dir
        filedir_remove(target_file_or_dir_path, missing_ok=missing_ok)

        leaf_dir_path = target_file_or_dir_path.parent
        if not root_dir_path.exists():
            #return_directly
            return
            # <<== path.samefile(path) -> FileNotFoundError #both should exist
        while not leaf_dir_path.exists():
            leaf_dir_path = leaf_dir_path.parent
        #while not leaf_dir_path.samefile(root_dir_path) and is_dir_empty(leaf_dir_path):
        while not leaf_dir_path.samefile(root_dir_path):
            if leaf_dir_path.exists():
                if is_dir_empty(leaf_dir_path):
                    os.rmdir(leaf_dir_path)
                else:
                    break
            else:
                pass
            leaf_dir_path = leaf_dir_path.parent
        assert leaf_dir_path.samefile(root_dir_path) or not is_dir_empty(leaf_dir_path)
        leaf_path = leaf_dir_path
    leaf_path

    try:
        assert leaf_path.samefile(root_dir_path) or (leaf_path.is_file() and leaf_path is target_file_or_dir_path) or (leaf_path.is_dir() and not is_dir_empty(leaf_path))# or (not leaf_path.exists())
    except AssertionError:
        from seed.tiny import print_err
        print_err(fr'leaf_path={leaf_path!r}')
        print_err(fr'root_dir_path={root_dir_path!r}')
        print_err(fr'target_file_or_dir_path={target_file_or_dir_path!r}')
        if leaf_path.is_file():
            print_err(fr'(leaf_path is target_file_or_dir_path)={(leaf_path is target_file_or_dir_path)!r}')
        elif leaf_path.is_dir():
            print_err(fr'[*leaf_path.iterdir()]={[*leaf_path.iterdir()]!r}')
        #print_err(fr'x={x!r}')
        raise
    return
    if 1:
        from seed.tiny import print_err
        print_err(fr'leaf_path={leaf_path!r}')
        print_err(fr'root_dir_path={root_dir_path!r}')
        print_err(fr'target_file_or_dir_path={target_file_or_dir_path!r}')
        #print_err(fr'x={x!r}')


    def is_same_path(lhs_path, rhs_path):

        #?not true???return lhs_path.samefile(rhs_path)
        #from nn_ns.filedir.relative_path_ops import is_relative_path_empty
        #return is_relative_path_empty(lhs_path.relative_to(rhs_path))
        return (lhs_path.relative_to(rhs_path)).as_posix() == '.'
    assert (leaf_path.as_posix()==root_dir_path.as_posix())
    assert is_same_path(leaf_path, root_dir_path)
    #assert leaf_path.samefile(root_dir_path) or (leaf_path.is_file() and leaf_path is target_file_or_dir_path) or (leaf_path.is_dir() and not is_dir_empty(leaf_path))
    assert is_same_path(leaf_path, root_dir_path) or (leaf_path.is_file() and leaf_path is target_file_or_dir_path) or (leaf_path.is_dir() and not is_dir_empty(leaf_path))
    return



def filedir_move_ex(*, from_path, to_path, exist_ok):
    if exist_ok:
        filedir_replace(from_path=from_path, to_path=to_path, missing_ok=True)
    else:
        filedir_move(from_path=from_path, to_path=to_path)

def filedir_replace(*, from_path, to_path, missing_ok):
    #os.replace???
    from_path = mk_Path(from_path)
    to_path = mk_Path(to_path)
    if not from_path.exists(): raise FileNotFoundError

    if not to_path.exists():
        if not (to_path.exists() or missing_ok): raise FileNotFoundError
        filedir_move(from_path=from_path, to_path=to_path)
    #elif to_path.samefile(from_path): pass
    else:
        if path_partial_cmp(from_path, to_path) is not None:
            from_path.replace(to_path)
        else:

            filedir_remove(to_path, missing_ok=False)
            filedir_move(from_path=from_path, to_path=to_path)

def filedir_remove(path, /,*, missing_ok):
    path = mk_Path(path)
    if not path.exists():
        if not missing_ok: raise FileNotFoundError
    elif path.is_dir():
        shutil.rmtree(path)
    else:
        os.unlink(path)
    if path.exists(): raise RuntimeError


def filedir_move(*, from_path, to_path):
    from_path = mk_Path(from_path)
    to_path = mk_Path(to_path)
    if to_path.exists(): raise FileExistsError
    if not from_path.exists(): raise FileNotFoundError
    os.makedirs(to_path.parent, exist_ok=True)

    dst = shutil.move(from_path, to_path)
        #if to_path is dir
        #then move into!!!
        #if to_path is file
        #then overwrite!!!
    if not to_path.samefile(dst): raise RuntimeError
        # check not dst is to_path/<???>
    if from_path.exists(): raise RuntimeError
    return None
    return dst
def filedir_copy(*, from_path, to_path):
    from_path = mk_Path(from_path)
    to_path = mk_Path(to_path)
    if to_path.exists(): raise FileExistsError
    if not from_path.exists(): raise FileNotFoundError
    os.makedirs(to_path.parent, exist_ok=True)

    dst = shutil.copy(from_path, to_path)
        #if to_path is dir
        #then copy into!!!
        #if to_path is file
        #??? not say: then overwrite
    if not to_path.samefile(dst): raise RuntimeError
        # check not dst is to_path/<???>
    return None
    return dst


