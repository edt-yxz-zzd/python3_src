
__all__ = '''
    replace_path_ext
    split_path_ext
    remove_path_ext
    '''.split()


import os.path;
from .common import is_ext


def replace_path_ext(path, new_ext, *, old_ext=None, max_num_dots=None):
    assert old_ext is None or old_ext == '' or is_ext(old_ext)
    if not is_ext(new_ext):
        raise Exception(f"{new_ext!r} is not a file ext")
        raise Exception(f"path's ext should startswith '.': {new_ext!r}")

    if (old_ext is not None and old_ext == new_ext
        and len(path) > len(new_ext) and path.endswith(new_ext)):
        return path

    root = remove_path_ext(path, old_ext=old_ext, max_num_dots=max_num_dots)
    new_path = root + new_ext
    return new_path

def split_path_ext(path, *, max_num_dots=None):
    root = remove_path_ext(path, max_num_dots=max_num_dots)
    ext = path[len(root):]

    assert root + ext == path
    assert ext == '' or is_ext(ext)
    return root, ext

def remove_path_ext(path, *, old_ext=None, max_num_dots=None):
    # use max_num_dots if old_ext is None
    # old_ext == '.tar.gz'
    assert old_ext is None or old_ext == '' or is_ext(old_ext)
    assert max_num_dots is None or max_num_dots >= 1
    if old_ext is not None:
        #max_num_dots = None
        del max_num_dots
    elif max_num_dots is None:
        # old_ext is None:
        max_num_dots = 1
    elif max_num_dots < 1: raise ValueError

    if old_ext is not None:
        if old_ext == '':
            pass
        elif old_ext[0] != '.':
            raise Exception(f"path's ext should startswith '.': {old_ext!r}")
        elif not path.endswith(old_ext):
            raise Exception(f"path's ext is not {old_ext!r}: {path!r}")
        elif len(path) == len(old_ext):
            assert path == old_ext
            raise Exception("path == old_ext == {path!r}")
        root = path[:-len(old_ext)]
    else:
        assert old_ext is None

        root = path
        for _ in range(max_num_dots):
            root, ext = os.path.splitext(root)
            if not ext: break
    return root


