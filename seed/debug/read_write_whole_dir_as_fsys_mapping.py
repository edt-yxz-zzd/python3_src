
r'''
seed.debug.read_write_whole_dir_as_fsys_mapping
py -m nn_ns.filedir.backup_tools._debug
py -m seed.debug.read_write_whole_dir_as_fsys_mapping

from seed.debug.read_write_whole_dir_as_fsys_mapping import read_whole_dir_as_fsys_mapping_ex, build_whole_dir_as_fsys_mapping_ex, eqv__fsys_mapping_ex


py::tempfile + read_whole_dir_as_fsys_mapping_ex + build_whole_dir_as_fsys_mapping_ex

usage:
    from seed.debug.read_write_whole_dir_as_fsys_mapping import read_whole_dir_as_fsys_mapping_ex, build_whole_dir_as_fsys_mapping_ex, eqv__fsys_mapping_ex
    from pathlib import Path
    import tempfile
    ###
    initial__fsys_mapping_ex = ... ...
    expected__fsys_mapping_ex = ... ...
    modify_dir = ... ...
    ###
    with tempfile.TemporaryDirectory(suffix=None, prefix=None, dir=None) as dir_name:
        dir_path = Path(dir_name)
        assert dir_path.is_dir()

        #setup
        build_whole_dir_as_fsys_mapping_ex(dir_path, initial__fsys_mapping_ex)
        if 1:
            ... test ... modify dir_path ...
            modify_dir(dir_path)
        result__fsys_mapping_ex = read_whole_dir_as_fsys_mapping_ex(dir_path)
        #teardown @with.exit
    assert eqv__fsys_mapping_ex(result__fsys_mapping_ex, expected__fsys_mapping_ex)





[doc]
tempfile.TemporaryDirectory(suffix=None, prefix=None, dir=None)

    This function securely creates a temporary directory using the same rules as mkdtemp(). The resulting object can be used as a context manager (see Examples). On completion of the context or destruction of the temporary directory object the newly created temporary directory and all its contents are removed from the filesystem.

    The directory name can be retrieved from the "name" attribute of the returned object. When the returned object is used as a context manager, the name will be assigned to the target of the as clause in the with statement, if there is one.

    The directory can be explicitly cleaned up by calling the "cleanup()" method.

    Raises an auditing event tempfile.mkdtemp with argument fullpath.

    New in version 3.2.
#'''

__all__ = '''
    read_whole_dir_as_fsys_mapping_ex
    build_whole_dir_as_fsys_mapping_ex
    eqv__fsys_mapping_ex
    '''.split()


___begin_mark_of_excluded_global_names__0___ = ...
import tempfile
from pathlib import Path
import os
from collections.abc import Mapping
import operator
___end_mark_of_excluded_global_names__0___ = ...

def read_whole_dir_as_fsys_mapping_ex(dir_path, /,*, items2mapping=dict):
    r'''
    fsys_mapping_ex<mapping> = mapping<basename::str, (bytes|fsys_mapping_ex<mapping>)>
        #pseudo_virtul_file_obj = file_content::bytes
        #   not:
        #       None=>del, patch_idx::uint=>address4file_content
        #       see:
        #           nn_ns.filedir.backup_tools.fsys_mapping_ex
        #           nn_ns.filedir.backup_tools.fsys_mapping_patch

    #'''
    if items2mapping is None:
        items2mapping = dict
    assert callable(items2mapping)

    dir_path = Path(dir_path)
    if not dir_path.exists(): raise FileNotFoundError
    if not dir_path.is_dir(): raise NotADirectoryError
    #stack::[(dir_path, iter_remain_child_paths, items::[(basename::str, (bytes|fsys_mapping_ex))])]
    #   iter_remain_basenames -> iter_remain_child_paths
    stack = []
    def put(dir_path):
        iter_remain_child_paths = dir_path.iterdir()
        assert iter_remain_child_paths is iter(iter_remain_child_paths)
        items = []
        x = (dir_path, iter_remain_child_paths, items)
        stack.append(x)
        #(dir_path, dir_path.iterdir(), [])
        return
    def main():
        while stack:
            (dir_path, iter_remain_child_paths, items) = stack[-1]
            #for basename in iter_remain_basenames:
                #path = dir_path / basename
                #assert path.name == basename
            for path in iter_remain_child_paths:
                basename = path.name
                if path.is_dir():
                    break
                else:
                    bs = path.read_bytes()
                    items.append((basename, bs))
            #end of for-loop
            else:
                #pop stack
                fsys_mapping_ex = items2mapping(items)
                stack.pop()
                if not stack:
                    return fsys_mapping_ex
                else:
                    stack[-1][-1].append((dir_path.name, fsys_mapping_ex))
                    continue #while stack:
            #end of for-loop-else
            new_dir_path = path
            put(new_dir_path)
        #end of while stack:
        else:
            raise logic-err
        #end of while stack:-else
        return
    #end of def main():

    put(dir_path)
    fsys_mapping_ex = main()
    assert fsys_mapping_ex is not None
    return fsys_mapping_ex


def _mapping2items(mapping):
    return mapping.items()
def build_whole_dir_as_fsys_mapping_ex(dir_path, fsys_mapping_ex, /,*, mapping2items=None, top_dir_exist_ok=False):
    if mapping2items is None:
        mapping2items = _mapping2items
    assert callable(mapping2items)

    dir_path = Path(dir_path)

    if top_dir_exist_ok:
        os.makedirs(dir_path, exist_ok=True)
        for basename, child_fsys_mapping_ex in mapping2items(fsys_mapping_ex):
            _build_whole_dir_as_fsys_mapping_ex(dir_path/basename, child_fsys_mapping_ex, mapping2items=mapping2items)
    else:
        _build_whole_dir_as_fsys_mapping_ex(dir_path, fsys_mapping_ex, mapping2items=mapping2items)

def _build_whole_dir_as_fsys_mapping_ex(dir_path, fsys_mapping_ex, /,*, mapping2items):
    if dir_path.exists(): raise FileExistsError
    #os.makedirs(dir_path, exist_ok=False)
    os.makedirs(dir_path.parent, exist_ok=True)
    stack = [] #[(dir_path, iter_remain_items)]
    def put(dir_path, fsys_mapping_ex):
        #no exist_ok: os.mkdir(dir_path, exist_ok=False)
        os.mkdir(dir_path) #FileExistsError
        iter_remain_items = iter(mapping2items(fsys_mapping_ex))
        x = (dir_path, iter_remain_items)
        stack.append(x)
        return
    def main():
        while stack:
            (dir_path, iter_remain_items) = stack.pop()
            for basename, bytes_or_fsys_mapping_ex in iter_remain_items:
                path = dir_path / basename
                if type(bytes_or_fsys_mapping_ex) is bytes:
                    bs = bytes_or_fsys_mapping_ex
                    with open(path, 'xb') as fout:
                        fout.write(bs)
                else:
                    fsys_mapping_ex = bytes_or_fsys_mapping_ex
                    new_dir_path = path
                    put(new_dir_path, fsys_mapping_ex)

    put(dir_path, fsys_mapping_ex)
    main()
    if __debug__:
        fsys_mapping_ex__dict = read_whole_dir_as_fsys_mapping_ex(dir_path)
        assert eqv__fsys_mapping_ex(fsys_mapping_ex__dict, fsys_mapping_ex)
    return


def eqv__fsys_mapping_ex(lhs_fsys_mapping_ex, rhs_fsys_mapping_ex, /,*, eqv__pseudo_virtul_file_obj=None):
    '-> bool'
    if eqv__pseudo_virtul_file_obj is None:
        eqv__pseudo_virtul_file_obj = operator.__eq__
    assert callable(eqv__pseudo_virtul_file_obj)

    stack = []
    def put(lhs_fsys_mapping_ex, rhs_fsys_mapping_ex):
        '-> bool'
        if len(lhs_fsys_mapping_ex) != len(rhs_fsys_mapping_ex): return False
        if set(lhs_fsys_mapping_ex) != set(rhs_fsys_mapping_ex): return False

        x = (lhs_fsys_mapping_ex, rhs_fsys_mapping_ex)
        stack.append(x)
        return True
    def main():
        '-> bool'
        while stack:
            (lhs_fsys_mapping_ex, rhs_fsys_mapping_ex) = stack.pop()
            for key in lhs_fsys_mapping_ex:
                x = lhs_fsys_mapping_ex[key]
                y = rhs_fsys_mapping_ex[key]
                bx = isinstance(x, Mapping)
                by = isinstance(y, Mapping)
                if bx is not by: return False
                if bx:
                    if not put(x, y): return False
                else:
                    if not eqv__pseudo_virtul_file_obj(x, y): return False
        else:
            return True
    #end of def main():


    if not put(lhs_fsys_mapping_ex, rhs_fsys_mapping_ex): return False
    b = main()
    assert type(b) is bool
    return b


def _prepare__name2fsys_mapping_ex():
    empty_file = b''
    file_0 = b'4321'
    file_1 = b'abcd'
    empty_dir = {}

    dir_0 = {'a':empty_dir}
    dir_1 = {'b':empty_file}
    dir_2 = {'c':file_0}
    dir_3 = {'d':file_1}
    dir_4 = dict(
        e = empty_dir
        ,f = empty_file
        ,g = file_0
        ,h = file_1
        )

    dir_5 = dict(
        e = empty_dir
        ,f = empty_file
        ,g = file_0
        ,h = file_1
        ,i = dir_0
        ,j = dir_1
        ,k = dir_2
        ,l = dir_3
        ,m = dir_4
        )

    dir_lhs = dict(
        same = dir_5
        ,diff_dir=dir_0
        ,diff_file=file_0
        ,lonly_dir=dir_0
        ,lonly_file=file_0
        ,ldir_rfile=dir_0
        ,lfile_rdir=file_0
        )
    dir_rhs = dict(
        same = dir_5
        ,diff_dir=dir_1
        ,diff_file=file_1
        ,ronly_dir=dir_1
        ,ronly_file=file_1
        ,ldir_rfile=file_1
        ,lfile_rdir=dir_1
        )
    d = dict(locals())
    for nm in 'empty_file file_0 file_1'.split():
        del d[nm]

    name2fsys_mapping_ex = d
    return name2fsys_mapping_ex


def _t(tmp_dir):
    name2fsys_mapping_ex = _prepare__name2fsys_mapping_ex()
    if 1:
        #################################
        #################################
        #################################
        for lhs_name, lhs_fsys_mapping_ex in name2fsys_mapping_ex.items():
            for rhs_name, rhs_fsys_mapping_ex in name2fsys_mapping_ex.items():
                assert (lhs_name==rhs_name) is eqv__fsys_mapping_ex(lhs_fsys_mapping_ex, rhs_fsys_mapping_ex)

    with tempfile.TemporaryDirectory(suffix=None, prefix='tmp_dir4test__', dir=tmp_dir) as dir_name:
        dir_path = Path(dir_name)
        assert dir_path.is_dir()

        #################################
        #################################
        #################################
        for name, fsys_mapping_ex in name2fsys_mapping_ex.items():
            assert eqv__fsys_mapping_ex(fsys_mapping_ex, fsys_mapping_ex)
            build_whole_dir_as_fsys_mapping_ex(dir_path/name, fsys_mapping_ex)
                #check inside via read_whole_dir_as_fsys_mapping_ex


if __name__ == "__main__":
    tmp_dir = r'/sdcard/0my_files/tmp/for-test/'
    _t(tmp_dir)

