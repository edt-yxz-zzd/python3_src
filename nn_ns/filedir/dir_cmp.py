
r'''
nn_ns.filedir.dir_cmp
py -m nn_ns.filedir.dir_cmp
from nn_ns.filedir.dir_cmp import dir_cmp, dir_cmp__relative, DirViewer__fsys, MkIsSameFile, AccessFile4MkIsSameFile__fsys:
from nn_ns.filedir.dir_cmp import IDirViewer, IPseudoFile4MkIsSameFile, IAccessFile4MkIsSameFile

e ../../python3_src/nn_ns/filedir/dir_cmp.py

path::Path
#'''

__all__ = '''
    dir_cmp
        dir_cmp__relative
    IDirViewer
        DirViewer__fsys
    MkIsSameFile
        IPseudoFile4MkIsSameFile
        IAccessFile4MkIsSameFile
            AccessFile4MkIsSameFile__fsys
    '''.split()

from pathlib import Path
import os.path
from abc import ABC, abstractmethod
from seed.abc.abc import override
#from seed.abc.abc import ABC, abstractmethod, override, not_implemented, ABCMeta

class IDirViewer(ABC):
    r'''
    path::Path
    #'''
    @abstractmethod
    def __is_file__(sf, path):
        'path -> bool'
    @abstractmethod
    def dir_iter(sf, dir_path):
        'dir_path -> [basename]'

    def __is_file(sf, path):
        'path -> bool'
        b = type(sf).__is_file__(sf, path)
        if type(b) is not bool: raise TypeError
        return b
    def is_file(sf, path):
        'path -> bool'
        return sf.__is_file(path)
    def is_dir(sf, path):
        'path -> bool'
        return not sf.__is_file(path)

#path.relative_to
def dir_cmp__relative(is_same_file, lhs_dir_viewer, lhs_path, rhs_dir_viewer, rhs_path):
    r'''-> Iter ((-1, lhs_relative_path)|(+1, rhs_relative_path)|(0, xhs_relative_file_path)|(-2, xhs_relative_path)|(+2, xhs_relative_path))
    see: dir_cmp
    #'''
    lhs_root = lhs_path
    rhs_root = rhs_path
    for case, data in dir_cmp(is_same_file, lhs_dir_viewer, lhs_path, rhs_dir_viewer, rhs_path):
        xhs_root = lhs_root
        if case == +1:
            xhs_root = rhs_root
            xhs_subpath = data
        elif case == -1:
            xhs_subpath = data
        else:
            xhs_subpath, _ = data
        xhs_relative_path = xhs_subpath.relative_to(xhs_root)
        yield case, xhs_relative_path

def dir_cmp(is_same_file, lhs_dir_viewer, lhs_path, rhs_dir_viewer, rhs_path):
    r'''-> Iter ((-1, lhs_path)|(+1, rhs_path)|(0, (lhs_file_path, rhs_file_path))|(-2, (lhs_dir_path, rhs_file_path))|(+2, (lhs_file_path, rhs_dir_path)))
    # diff = extra lhs_path | extra rhs_path | diff file content | mismatch dir/file

    is_same_file :: lhs_file_path -> rhs_file_path -> bool
    lhs_dir_viewer :: IDirViewer
    lhs_path :: Path
    rhs_dir_viewer :: IDirViewer
    rhs_path :: Path

    =============
    =============
    =============
    left/right file system may be diff
        e.g.
            svn
            zip
            local-filesys
            remote-filesys
    #'''
    if not lhs_path.exists(): raise FileNotFoundError(lhs)
    if not rhs_path.exists(): raise FileNotFoundError(rhs)

    may_path_pairs = [(lhs_path, rhs_path)]
    while may_path_pairs:
        (may_lhs_path, may_rhs_path) = may_path_pairs.pop()
        if 1:
            if may_lhs_path is None is may_rhs_path:
                raise logic-err
            elif may_rhs_path is None:
                lhs_path = may_lhs_path
                yield -1, lhs_path
                continue
            elif may_lhs_path is None:
                rhs_path = may_rhs_path
                yield +1, rhs_path
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
                yield 0, (lhs_file_path, rhs_file_path)
        elif not lb and rb:
            (lhs_dir_path, rhs_file_path) = (lhs_path, rhs_path)
            yield -2, (lhs_dir_path, rhs_file_path)
        elif lb and not rb:
            (lhs_file_path, rhs_dir_path) = (lhs_path, rhs_path)
            yield +2, (lhs_file_path, rhs_dir_path)
        else:
            assert not lb and not rb
            (lhs_dir_path, rhs_dir_path) = (lhs_path, rhs_path)
            lnames = set(lhs_dir_viewer.dir_iter(lhs_dir_path))
            rnames = set(rhs_dir_viewer.dir_iter(rhs_dir_path))
            common = lnames & rnames
            lonly = lnames - rnames
            ronly = rnames - lnames
            all_names = sorted(lnames | rnames, reverse=True)
            for name in all_names:
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
                may_path_pairs.append(pair)






class DirViewer__fsys(IDirViewer):
    @override
    def __is_file__(sf, path):
        'path -> bool'
        return path.is_file()
    @override
    def dir_iter(sf, dir_path):
        'dir_path -> Iter basename'
        yield from os.listdir(dir_path)
        return
        for path in dir_path.iterdir():
            yield path.name
if 0:
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
    #'''
    @abstractmethod
    def read(sf, num_bytes):
        'uint -> bytes'
    #context manager
    @abstractmethod
    def __enter__(sf):
        pass
    @abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        pass
class IAccessFile4MkIsSameFile(ABC):
    r'''
    for MkIsSameFile
    path::Path
    #'''
    @abstractmethod
    def get_file_size(sf, file_path):
        'file_path -> uint # unit:byte'
    @abstractmethod
    def open(sf, file_path):
        'file_path -> IPseudoFile4MkIsSameFile'

class AccessFile4MkIsSameFile__fsys(IAccessFile4MkIsSameFile):
    @override
    def get_file_size(sf, file_path):
        'file_path -> uint # unit:byte'
        return os.path.getsize(file_path)
    @override
    def open(sf, file_path):
        'file_path -> IPseudoFile4MkIsSameFile'
        return open(file_path, 'rb')


class MkIsSameFile:
    r'''
    for is_same_file
    path::Path
    #'''
    def __init__(sf, lhs_access_file, rhs_access_file, _block_size=512):
        'IAccessFile4MkIsSameFile -> IAccessFile4MkIsSameFile -> MkIsSameFile'
        sf.lhs_access_file = lhs_access_file
        sf.rhs_access_file = rhs_access_file
        sf._block_size = _block_size
    def __call__(sf, lhs_file_path, rhs_file_path):
        'is_same_file :: lhs_file_path -> rhs_file_path -> bool'
        lsz = sf.lhs_access_file.get_file_size(lhs_file_path)
        rsz = sf.rhs_access_file.get_file_size(rhs_file_path)
        if lsz != rsz:
            return False
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


if __name__ == "__main__":
    xhs_access_file = AccessFile4MkIsSameFile__fsys()
    is_same_file = MkIsSameFile(xhs_access_file, xhs_access_file)
    xhs_dir_viewer = DirViewer__fsys()

    if 0:
        lhs_path = rhs_path = Path(r'/sdcard/0my_files/git_repos/python3_src/seed/verify/')
        print(list(dir_cmp(is_same_file, xhs_dir_viewer, lhs_path, xhs_dir_viewer, rhs_path)))
        rhs_path = Path(r'/sdcard/0my_files/git_repos/python3_src/seed/debug/')
        print(list(dir_cmp(is_same_file, xhs_dir_viewer, lhs_path, xhs_dir_viewer, rhs_path)))

    if 1:
        test_data_path = Path(__file__).parent/'_dir_cmp__test_data'

        lhs_path = test_data_path/'lhs'
        rhs_path = test_data_path/'rhs'

        ls = list(dir_cmp__relative(is_same_file, xhs_dir_viewer, lhs_path, xhs_dir_viewer, rhs_path))
        if 0:
            print(ls)
            from pprint import pprint
            pprint(ls)
        PosixPath = Path
        expected = \
            [(0, PosixPath('z/diff.txt')),
             (-2, PosixPath('z/ld_rf')),
             (2, PosixPath('z/lf_rd')),
             (-1, PosixPath('z/lonlyd')),
             (-1, PosixPath('z/lonlyf')),
             (1, PosixPath('z/ronlyd')),
             (1, PosixPath('z/ronlyf'))]
        assert ls == expected








