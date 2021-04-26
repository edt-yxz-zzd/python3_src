r"""
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
    'remove empty dir until root #see:os.removedirs/mkdirs/renames'
    filedir_move_ex(from_path=from_path, to_path=to_path, exist_ok=exist_ok)

    remove_dirs(from_path.parent, may_root_dir_path=may_root_dir_path4from, missing_ok=True, target_dir_nonempty_ok=True, target_path_is_file_ok=False, target_dir_path_is_root_dir_path_ok=True)
        #missing_ok=True???

def remove_dirs(target_dir_path, /,*, may_root_dir_path, missing_ok, target_dir_nonempty_ok, target_path_is_file_ok, target_dir_path_is_root_dir_path_ok):
    r'''remove empty dir until root #see:os.removedirs/mkdirs/renames
    os.removedirs until not empty
        but required leaf_dir empty
        and not bounded by root
    #'''
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
        if target_file_or_dir_path.is_dir():
            if not target_dir_nonempty_ok and is_dir_empty(target_file_or_dir_path): raise RuntimeError
            #target_file_or_dir_path is_dir
            _target_dir_path = target_file_or_dir_path
            return_directly = True
        elif target_file_or_dir_path.is_file():
            if not target_path_is_file_ok: raise NotADirectoryError
            _target_file_path = target_file_or_dir_path
            #target_file_or_dir_path is_file
            return_directly = True
        else:
            raise RuntimeError(f'unknown file type: {target_file_or_dir_path!r}')


    ####
    if return_directly:
        leaf_path = target_file_or_dir_path
        #leaf_dir_path = _target_dir_path
        #leaf_file_path = _target_file_path
    else:
        #root_dir_path < target_file_or_dir_path

        filedir_remove(target_file_or_dir_path, missing_ok=missing_ok)

        leaf_dir_path = target_file_or_dir_path.parent
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

    assert leaf_path.samefile(root_dir_path) or (leaf_path.is_file() and leaf_path is target_file_or_dir_path) or (leaf_path.is_dir() and not is_dir_empty(leaf_path))
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


