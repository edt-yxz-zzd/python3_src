#HHHHH
r'''

filedir_cmp_utils__repository__fsys_mapping
nn_ns.filedir.backup_tools.filedir_cmp_utils__repository__fsys_mapping
py -m nn_ns.app.debug_cmd nn_ns.filedir.backup_tools.filedir_cmp_utils__repository__fsys_mapping

main:
    def dir_cmp__relative__with_IRepositorySetting__rhs_is_real_fsys(lhs_repository_setting:IRepositorySetting, lhs_branch_name, lhs_may_signed_branch_idx, lhs_relative_path:'relative PurePosixPath', rhs_path, /,*, kwargs4MkIsSameFile, kwargs4dir_cmp__relative):
        kwargs4dir_cmp__relative
            #except:ignore_relative_path
            ignore_basename, max_depth
        kwargs4MkIsSameFile
            always_tribool_as_is_or_not_same_file:'tribool', size_eq_as_same_file:bool, size_hash0_eq_as_same_file:bool, hash_eq_as_same_file:bool, mtime_eq_as_same_file:bool, mtime_ne_as_not_same_file:bool, imay_max_size_threshold4cmp_content:int, _block_size
    def mk_commit_and_push__rhs_is_real_fsys(result_of_dir_cmp__relative, lhs_repository_setting, lhs_branch_name, lhs_may_signed_branch_idx, lhs_relative_path, rhs_root_path, /):
    def mk_commit_and_push__rhs_is_IRepositorySetting(result_of_dir_cmp__relative, lhs_repository_setting, lhs_branch_name, lhs_may_signed_branch_idx, lhs_relative_path, rhs_repository_setting, rhs_branch_name, rhs_may_signed_branch_idx, rhs_relative_path, /):
    def mk_empty_repository_branch(lhs_repository_setting, lhs_branch_name, /):#, lhs_may_signed_branch_idx
    def extract_branch(lhs_repository_setting, lhs_branch_name, lhs_branch_idx, rhs_real_fsys_root_dir_path4output, /):



_dict
    _mapping
    fsys_dict
        -->> fsys_mapping



======================mkdirs-->makedirs
AttributeError: module 'os' has no attribute 'mkdirs'

cd /sdcard/0my_files/git_repos/python3_src/nn_ns/filedir/
grep '\(^\|[^a-zA-Z0-9_]\)mkdirs' -r . -l

./backup_tools/filedir_cmp_utils__repository__fsys_mapping.py
./backup_tools/IRepositorySetting.py
./filedir_ops.py
no use os.makedirs:
    ./backup_tools/main.py
    ./backup_tools/FileSystem4update.py
    ./backup_tools/fsys_mapping_ex.py
    ./backup_tools/fsys_mapping_patch.py

==========
TypeError: len_inf_dir() missing 1 required keyword-only argument: 'level'

grep '\(^\|[^a-zA-Z0-9_]\)len_inf_dir' -r . -l


./inf_dir.py
./backup_tools/IRepositorySetting.py
no use len_inf_dir:
    ./backup_tools/filedir_cmp_utils__repository__fsys_mapping.py
    ./backup_tools/FileSystem4update.py
    ./backup_tools/imports.py





======================



#'''







__all__ = '''
    access_path__fsys_mapping
    DirViewer__fsys_mapping
    AccessFile4MkIsSameFile__backup_util_repository__fsys_mapping__IRepositorySetting
    mk_args4dir_cmp__with_IRepositorySetting
    access_file2open_ignorefile_text_ifile
    mk_args_ex4dir_cmp__with_IRepositorySetting
    dir_cmp__relative__with_IRepositorySetting
    dir_cmp__relative__with_IRepositorySetting__rhs_is_real_fsys
    IVisit_result_of_dir_cmp__relative
    Visit_result_of_dir_cmp__relative
    IRun_file_diff_over_result_of_dir_cmp__relative
    IRun_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes
    IRun_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes__using_file_cmp_file_diff_ver1
    IRun_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes__using_IRepositorySetting
    IRun_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes__using_file_cmp_file_diff_ver1__using_IRepositorySetting
    Run_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes__using_file_cmp_file_diff_ver1__using_IRepositorySetting__rhs_is_real_fsys
    Run_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes__using_file_cmp_file_diff_ver1__using_IRepositorySetting__rhs_is_IRepositorySetting
    mk_commit_and_push__rhs_is_real_fsys
    mk_commit_and_push__rhs_is_IRepositorySetting
    mk_empty_repository_branch
    extract_branch
    '''.split()


___begin_mark_of_excluded_global_names__0___ = ...

from nn_ns.filedir.backup_tools.fsys_mapping_ex import using_FrozenDict_as_valueonly_fsys_mapping_ex, get_tmay_sub_fsys_mapping_or_patch_idx, check_fsys_mapping, pseudo_virtual_file_reprobj_checker_cls4fsys_patch_mapping, deepcopy_fsys_mapping_ex
from nn_ns.filedir.backup_tools.IRepositorySetting import IRepositorySetting, metadata_keys_setting
from nn_ns.filedir.backup_tools.IRepositorySetting__using_IFileSystem4update__fsys_delta import IRepositorySetting__using_IFileSystem4update__fsys_delta
from nn_ns.filedir.dir_cmp import dir_cmp__relative, IDirViewer, IAccessFile4MkIsSameFile, MkIsSameFile, get_str_mtime4real_fsys, DirViewer__fsys, AccessFile4MkIsSameFile__fsys#, mk_filter_basenames_ex
from nn_ns.filedir.file_cmp import file_diff
from nn_ns.filedir.inf_dir import inf_dir_idx2user_data_relative_path
from nn_ns.filedir.relative_path_ops import relative_path2parts, empty_relative_path



from seed.helper.check.checkers import check_uint, check_tuple, check_instance
from seed.math.calc_hash_digest import calc_SHA256__file
from seed.abc.abc import override
from seed.types.FrozenDict import FrozenDict

import io
import copy
import os.path
from abc import ABC, abstractmethod

BLOCK_SIZE = 2**20
___end_mark_of_excluded_global_names__0___ = ...






def access_path__fsys_mapping(root_fsys_mapping_or_patch_idx, relative_path:'PurePosixPath&not is_absolute()', /,*, with_case:bool, with_exc:bool, with_args:bool):
    '(fsys_mapping|patch_idx) -> relative PurePosixPath -> (with_case,with_exc,with_args:bool) -> (("not_exists"|"is_file"|"is_dir")?<<==with_case?, (FileNotFoundError|NotADirectoryError|IsADirectoryError)?<<==with_exc, *(root_fsys_mapping_or_patch_idx,relative_path)?<<==with_args?, (|patch_idx|fsys_mapping))'
    assert not relative_path.is_absolute()

    m = get_tmay_sub_fsys_mapping_or_patch_idx(root_fsys_mapping_or_patch_idx, relative_path)
    if not m:
        r = ('not_exists', FileNotFoundError, root_fsys_mapping_or_patch_idx, relative_path)
        #raise FileNotFoundError
    else:
        [sub_fsys_mapping_or_patch_idx] = m
        if type(sub_fsys_mapping_or_patch_idx) is int:
            sub_patch_idx = sub_fsys_mapping_or_patch_idx
            r = ('is_file', NotADirectoryError, root_fsys_mapping_or_patch_idx, relative_path, sub_patch_idx)
            #raise NotADirectoryError
        else:
            sub_fsys_mapping = sub_fsys_mapping_or_patch_idx
            r = ('is_dir', IsADirectoryError, root_fsys_mapping_or_patch_idx, relative_path, sub_fsys_mapping)
            #raise IsADirectoryError
    r

    ls = []
    if with_case:
        ls.extend(r[0:1])
    if with_exc:
        ls.extend(r[1:2])
    if with_args:
        ls.extend(r[2:4])
    ls.extend(r[4:])
    return tuple(ls)








#HHHHH
class DirViewer__fsys_mapping(IDirViewer):
    r'''
    #path::Path
    path::relative PurePosixPath
    #'''
    def __init__(sf, fsys_mapping, /):
        check_fsys_mapping(fsys_mapping, None)
        sf.fsys_mapping = fsys_mapping

    @override
    def ___is_file___(sf, path, /):
        'path -> (bool|raise FileNotFoundError)'
        if 1:
            assert not path.is_absolute()
            root_fsys_mapping_or_patch_idx = sf.fsys_mapping
            relative_path = path
            r = access_path__fsys_mapping(root_fsys_mapping_or_patch_idx, relative_path, with_case=True, with_exc=True, with_args=False)
            case, exc, *m = r
            if case=='not_exists':
                raise exc
            elif case=='is_file':
                return True
            elif case=='is_dir':
                return False
            else:
                raise logic-err
            raise logic-err
            return
        else:
            assert not path.is_absolute()
            m = get_tmay_sub_fsys_mapping_or_patch_idx(sf.fsys_mapping, path)
            if not m: raise FileNotFoundError
            [root_fsys_mapping_or_patch_idx] = m
            return type(root_fsys_mapping_or_patch_idx) is int

    @override
    def ___dir_iter___(sf, dir_path, /):
        'dir_path -> (Iter basename | raise FileNotFoundError/NotADirectoryError)'
        if 1:
            assert not dir_path.is_absolute()
            root_fsys_mapping_or_patch_idx = sf.fsys_mapping
            relative_path = dir_path
            r = access_path__fsys_mapping(root_fsys_mapping_or_patch_idx, relative_path, with_case=True, with_exc=True, with_args=False)
            case, exc, *m = r
            if case=='not_exists':
                raise exc
            elif case=='is_file':
                raise exc
            elif case=='is_dir':
                [sub_fsys_mapping] = m
                return iter(sub_fsys_mapping)
            else:
                raise logic-err
            raise logic-err
            return
        else:
            assert not dir_path.is_absolute()
            m = get_tmay_sub_fsys_mapping_or_patch_idx(sf.fsys_mapping, dir_path)
            if not m: raise FileNotFoundError
            [root_fsys_mapping_or_patch_idx] = m
            if type(root_fsys_mapping_or_patch_idx) is int:
                patch_idx = root_fsys_mapping_or_patch_idx
                raise NotADirectoryError
            else:
                fsys_mapping = root_fsys_mapping_or_patch_idx
                return iter(fsys_mapping)

    @override
    def ___exists___(sf, path, /):
        'path -> bool'
        assert not path.is_absolute()
        return bool(get_tmay_sub_fsys_mapping_or_patch_idx(sf.fsys_mapping, path))


#HHHHH
class AccessFile4MkIsSameFile__backup_util_repository__fsys_mapping__IRepositorySetting(IAccessFile4MkIsSameFile):
    r'''
    for MkIsSameFile
    #path::Path
    virtual_file_path :: relative PurePosixPath
    #'''
    def __init__(sf, repository_setting:IRepositorySetting, fsys_mapping, /):
        if not isinstance(repository_setting, IRepositorySetting):raise TypeError
        check_fsys_mapping(fsys_mapping, None)

        sf.repository_setting = repository_setting
        sf.fsys_mapping = fsys_mapping
        sf.metadata_cache = {}

    def virtual_file_path2real_user_data_dir_path(sf, virtual_file_path, /):
        'virtual file_path@fsys_mapping -> real user_data_dir_path@fsys'
        patch_idx = sf.virtual_file_path2patch_idx(virtual_file_path)
        user_data_dir_path = sf.patch_idx2real_user_data_dir_path(patch_idx)
        return user_data_dir_path

    def patch_idx2real_user_data_dir_path(sf, patch_idx, /):
        'patch_idx -> real user_data_dir_path@fsys'
        return sf.repository_setting.patch_idx2user_data_dir_path(patch_idx)

    def virtual_file_path2patch_idx(sf, virtual_file_path, /):
        'virtual file_path@fsys_mapping -> patch_idx'
        assert not virtual_file_path.is_absolute()
        fsys_mapping_or_patch_idx = sf.fsys_mapping
        relative_path = virtual_file_path
        r = access_path__fsys_mapping(fsys_mapping_or_patch_idx, relative_path, with_case=True, with_exc=True, with_args=False)
        case, exc, *m = r
        if case=='not_exists':
            raise exc
        elif case=='is_file':
            [sub_patch_idx] = m
            return sub_patch_idx
        elif case=='is_dir':
            raise exc
        else:
            raise logic-err
        raise logic-err
        return





    def get_metadata(sf, virtual_file_path, /):
        'virtual_file_path -> metadata'
        assert not virtual_file_path.is_absolute()
        patch_idx = sf.virtual_file_path2patch_idx(virtual_file_path)
        def reur(depth, /):
            m = sf.metadata_cache_lookup(patch_idx)
            if m:
                [metadata] = m
                return metadata
            if depth: raise logic-err

            metadata = sf.repository_setting.patch_idx2metadata(patch_idx)
            sf.metadata_cache_put(patch_idx, metadata)
            return reur(1)
        metadata = reur(0)
        return metadata


    @override
    def get_file_size(sf, virtual_file_path, /):
        'virtual_file_path -> uint # unit:byte'
        assert not virtual_file_path.is_absolute()
        metadata = sf.get_metadata(virtual_file_path)
        return metadata[metadata_keys_setting.key4file_size]
    @override
    def get_may_hash_method_uppercase_std_name2upper_hex_digest(sf, virtual_file_path, /):
        'virtual_file_path -> (None|hash_method_uppercase_std_name2upper_hex_digest::{name:hex}) #name <- {SHA256, MD5, ...}'
        assert not virtual_file_path.is_absolute()
        metadata = sf.get_metadata(virtual_file_path)
        may_hash_method_uppercase_std_name2upper_hex_digest = metadata[metadata_keys_setting.key4may_hash_method_uppercase_std_name2upper_hex_digest] #must exist, but can be empty or None!
        if not may_hash_method_uppercase_std_name2upper_hex_digest:
            may_hash_method_uppercase_std_name2upper_hex_digest = None
        return may_hash_method_uppercase_std_name2upper_hex_digest
    @override
    def get_may_str_mtime(sf, virtual_file_path, /):
        r'''virtual_file_path -> (None|str_time) # %Y%m%d_%H%M%S_%z # == STR_TIME_FORMAT
    # ends with constant %z == +0000
        #'''
        assert not virtual_file_path.is_absolute()
        metadata = sf.get_metadata(virtual_file_path)
        may_str_mtime = metadata[metadata_keys_setting.key4may_str_mtime] #must exist, but can be empty or None!
        if not may_str_mtime:
            may_str_mtime = None
        return may_str_mtime
    #def _float_time2str_time(float_time, /):


    def metadata_cache_lookup(sf, patch_idx, /):
        '-> tmay metadata'
        try:
            metadata = sf.metadata_cache[patch_idx]
        except KeyError:
            tmay_metadata = ()
        else:
            tmay_metadata = (metadata,)
        return copy.deepcopy(tmay_metadata)
    def metadata_cache_put(sf, patch_idx, metadata, /):
        sf.metadata_cache[patch_idx] = metadata

    @override
    def open(sf, virtual_file_path, /):
        'virtual_file_path -> IPseudoFile4MkIsSameFile'
        assert not virtual_file_path.is_absolute()
        patch_idx = sf.virtual_file_path2patch_idx(virtual_file_path)
        _, pseudo_ifile = sf.repository_setting.open_patch_idx_ex(patch_idx, with_metadata=False)
        return pseudo_ifile












def mk_args4dir_cmp__with_IRepositorySetting(repository_setting:IRepositorySetting, branch_name, may_signed_branch_idx, /,*, may_working_root_dir_path, may_open_ignorefile_text_ifile):
    r'''
    :: IRepositorySetting -> branch_name -> (None|branch_idx|neg_inf_dir_end_based_branch_idx) -> (may_working_root_dir_path::None|path) -> (may_open_ignorefile_text_ifile::may(working_root_dir_path -> ignorefile_relative_path -> (encoding:str) -> text_ifile)) -> (dir_viewer::IDirViewer, access_file::IAccessFile4MkIsSameFile, may_ignore_relative_path::(None|relative_path->bool), branch_idx::uint)

    prepare args for dir_cmp__relative/dir_cmp

    may_signed_branch_idx :: (None|int)
        None ==>> -1
        neg ==>> end-based branch_idx
    assert (may_ignore_relative_path is None) is (may_working_root_dir_path is None)
    ===========================
    (lhs_dir_viewer, lhs_access_file, ignore_relative_path, lhs_branch_idx) = mk_args4dir_cmp__with_IRepositorySetting(lhs_repository_setting, lhs_branch_name, lhs_may_signed_branch_idx, may_working_root_dir_path=working_root_dir_path, may_open_ignorefile_text_ifile=open_ignorefile_text_ifile)
    ===========================
    (rhs_dir_viewer, rhs_access_file, _, rhs_branch_idx) = mk_args4dir_cmp__with_IRepositorySetting(rhs_repository_setting, rhs_branch_name, rhs_may_signed_branch_idx, may_working_root_dir_path=None, may_open_ignorefile_text_ifile=None)
    ===========================

see: mk_args_ex4dir_cmp__with_IRepositorySetting
see: dir_cmp__relative__with_IRepositorySetting
    for continue usage
    ##################################
    def dir_cmp__relative(is_same_file, lhs_dir_viewer, lhs_path, rhs_dir_viewer, rhs_path, /,*, ignore_relative_path, ignore_basename, max_depth):
    ##################################
    is_same_file = MkIsSameFile
        def __init__(sf, lhs_access_file, rhs_access_file, /, *, always_tribool_as_is_or_not_same_file:'tribool', size_eq_as_same_file:bool, size_hash0_eq_as_same_file:bool, hash_eq_as_same_file:bool, mtime_eq_as_same_file:bool, mtime_ne_as_not_same_file:bool, imay_max_size_threshold4cmp_content:int, _block_size):
    ##################################
    #'''
    branch_idx = repository_setting.resolve_may_signed_branch_idx(branch_name, may_signed_branch_idx)

    may_root_fsys_frozendict = repository_setting.extract_may_root_fsys_frozendict_at_branch_time({}, branch_name, branch_idx)

    if may_root_fsys_frozendict is None: raise RuntimeError(f'branch_time={(branch_name, branch_idx)!r} not exist')
    root_fsys_frozendict = may_root_fsys_frozendict

    dir_viewer = DirViewer__fsys_mapping(root_fsys_frozendict)
    access_file = AccessFile4MkIsSameFile__backup_util_repository__fsys_mapping__IRepositorySetting(repository_setting, root_fsys_frozendict)

    if may_working_root_dir_path is None:
        may_ignore_relative_path = None
    else:
        working_root_dir_path = may_working_root_dir_path
        ignore_relative_path = repository_setting.mk_relative_path2is_ignore(working_root_dir_path, may_open_ignorefile_text_ifile)
        may_ignore_relative_path = ignore_relative_path
    may_ignore_relative_path

    return (dir_viewer, access_file, may_ignore_relative_path, branch_idx)


def access_file2open_ignorefile_text_ifile(access_file4working_root_dir:IAccessFile4MkIsSameFile, /):
    def open_ignorefile_text_ifile(working_root_dir_path, ignorefile_relative_path, /,*, encoding):
        with access_file4working_root_dir.open(working_root_dir_path/ignorefile_relative_path) as bfin:
            bs = bfin.read(-1)
        s = bs.decode(encoding)
        return io.StringIO(s)
    return open_ignorefile_text_ifile

def mk_args_ex4dir_cmp__with_IRepositorySetting(lhs_repository_setting:IRepositorySetting, lhs_branch_name, lhs_may_signed_branch_idx, rhs_access_file:IAccessFile4MkIsSameFile, rhs_path, not_mk_is_same_file:bool=False, /,    **kwargs4MkIsSameFile):
    r'''
    -> (may is_same_file, lhs_dir_viewer, lhs_access_file, ignore_relative_path, open_ignorefile_text_ifile, lhs_branch_idx)
    =====
    (is_same_file, lhs_dir_viewer, lhs_access_file, ignore_relative_path, open_ignorefile_text_ifile, lhs_branch_idx) = mk_args_ex4dir_cmp__with_IRepositorySetting(lhs_repository_setting, lhs_branch_name, lhs_may_signed_branch_idx, rhs_access_file, rhs_path, **kwargs4MkIsSameFile)
    =====
    (_, lhs_dir_viewer, lhs_access_file, ignore_relative_path, open_ignorefile_text_ifile, lhs_branch_idx) = mk_args_ex4dir_cmp__with_IRepositorySetting(lhs_repository_setting, lhs_branch_name, lhs_may_signed_branch_idx, rhs_access_file, rhs_path, True)
    #'''
    working_root_dir_path = rhs_path
    access_file4working_root_dir = rhs_access_file
    open_ignorefile_text_ifile = access_file2open_ignorefile_text_ifile(access_file4working_root_dir)
    (lhs_dir_viewer, lhs_access_file, may_ignore_relative_path, lhs_branch_idx) = mk_args4dir_cmp__with_IRepositorySetting(lhs_repository_setting, lhs_branch_name, lhs_may_signed_branch_idx, may_working_root_dir_path=working_root_dir_path, may_open_ignorefile_text_ifile=open_ignorefile_text_ifile)
    assert may_ignore_relative_path is not None
    ignore_relative_path = may_ignore_relative_path

    if not_mk_is_same_file:
        may_is_same_file = None
    else:
        is_same_file = MkIsSameFile(lhs_access_file, rhs_access_file, **kwargs4MkIsSameFile)
        may_is_same_file = is_same_file
    may_is_same_file

    return (may_is_same_file, lhs_dir_viewer, lhs_access_file, ignore_relative_path, open_ignorefile_text_ifile, lhs_branch_idx)

def dir_cmp__relative__with_IRepositorySetting(lhs_repository_setting:IRepositorySetting, lhs_branch_name, lhs_may_signed_branch_idx, lhs_relative_path:'relative PurePosixPath', rhs_dir_viewer:IDirViewer, rhs_access_file:IAccessFile4MkIsSameFile, rhs_path, /,*, kwargs4MkIsSameFile, kwargs4dir_cmp__relative):
    r'''->result_of_dir_cmp__relative
    #'''
    (is_same_file, lhs_dir_viewer, lhs_access_file, ignore_relative_path, open_ignorefile_text_ifile, lhs_branch_idx) = mk_args_ex4dir_cmp__with_IRepositorySetting(lhs_repository_setting, lhs_branch_name, lhs_may_signed_branch_idx, rhs_access_file, rhs_path, **kwargs4MkIsSameFile)
    return dir_cmp__relative(is_same_file, lhs_dir_viewer, lhs_relative_path, rhs_dir_viewer, rhs_path, ignore_relative_path=ignore_relative_path, **kwargs4dir_cmp__relative)
def dir_cmp__relative__with_IRepositorySetting__rhs_is_real_fsys(lhs_repository_setting:IRepositorySetting, lhs_branch_name, lhs_may_signed_branch_idx, lhs_relative_path:'relative PurePosixPath', rhs_path, /,*, kwargs4MkIsSameFile, kwargs4dir_cmp__relative):
    r'''->result_of_dir_cmp__relative

    kwargs4dir_cmp__relative
        #except:ignore_relative_path
        ignore_basename, max_depth
    kwargs4MkIsSameFile
        always_tribool_as_is_or_not_same_file:'tribool', size_eq_as_same_file:bool, size_hash0_eq_as_same_file:bool, hash_eq_as_same_file:bool, mtime_eq_as_same_file:bool, mtime_ne_as_not_same_file:bool, imay_max_size_threshold4cmp_content:int, _block_size
    #'''
    rhs_dir_viewer = DirViewer__fsys()
    rhs_access_file = AccessFile4MkIsSameFile__fsys()
    result_of_dir_cmp__relative = dir_cmp__relative__with_IRepositorySetting(lhs_repository_setting, lhs_branch_name, lhs_may_signed_branch_idx, lhs_relative_path, rhs_dir_viewer, rhs_access_file, rhs_path, kwargs4MkIsSameFile=kwargs4MkIsSameFile, kwargs4dir_cmp__relative=kwargs4dir_cmp__relative)
    return result_of_dir_cmp__relative






class IVisit_result_of_dir_cmp__relative(ABC):
    @abstractmethod
    def xhs_relative_filedir_path2is_ignore(sf, xhs_relative_filedir_path, /):
        'xhs_relative_filedir_path -> bool #see:mk_relative_path2is_ignore'
    @abstractmethod
    def get_rhs_dir_viewer(sf, /):
        '-> rhs_dir_viewer'
    @abstractmethod
    def get_rhs_root_path(sf, /):
        '-> rhs_root_path'
    def on_diff_file(sf, xhs_relative_file_path, /):
        '#overwrite_file_by_file'

    def on_right_only_new_file(sf, rhs_relative_file_path, /):
        '.visit() not call on_new_file_under_new_dir'
    #to_skip from [on_right_only_new_top_dir__enter, on_remove_file_and_new_top_dir__enter, on_new_top_dir__enter, on_new_dir__enter]
    #   ???for what??? apply ignorefile???
    def on_right_only_new_top_dir__enter(sf, rhs_relative_dir_path, /):
        r'''-> to_skip:bool
        if to_skip==True: not call inside & exit
        else: '.visit() call on_new_top_dir__enter/on_new_top_dir__exit'
        #'''
        #return__to_skip
        ##bug:return
        to_skip = False
        return to_skip
    def on_right_only_new_top_dir__exit(sf, rhs_relative_dir_path, /):
        ''
    def on_new_top_dir__enter(sf, rhs_relative_dir_path, /):
        r'''-> to_skip:bool
        if to_skip==True: not call inside & exit
        else: '.visit() call on_new_dir__enter/on_new_dir__exit'
        #'''
        #return__to_skip
        ##bug:return
        to_skip = False
        return to_skip
    def on_new_top_dir__exit(sf, rhs_relative_dir_path, /):
        ''
    def on_new_dir__enter(sf, rhs_relative_dir_path, /):
        r'''-> to_skip:bool
        if to_skip==True: not call inside & exit
        else: '.visit() call on_new_file_under_new_dir/recur call on_new_dir__enter/on_new_dir__exit'
        #'''
        #return__to_skip
        ##bug:return
        to_skip = False
        return to_skip
    def on_new_dir__exit(sf, rhs_relative_dir_path, /):
        ''
    def on_new_file_under_new_dir(sf, rhs_relative_file_path, /):
        'only call between on_new_dir__enter/on_new_dir__exit; not with on_right_only_new_file'

    def on_remove_file_or_top_dir(sf, lhs_relative_file_path, /):
        ''
    def on_remove_top_dir_and_new_file(sf, xhs_relative_filedir_path, /):
        '.visit() not call on_new_file_under_new_dir;  #overwrite_dir_by_file'
    def on_remove_file_and_new_top_dir__enter(sf, xhs_relative_filedir_path, /):
        r'''-> to_skip:bool     #overwrite_file_by_dir
        if to_skip==True: not call inside & exit
        else: '.visit() call on_new_top_dir__enter/on_new_top_dir__exit'
        #'''
        #return__to_skip
        ##bug:return
        to_skip = False
        return to_skip
    def on_remove_file_and_new_top_dir__exit(sf, xhs_relative_filedir_path, /):
        ''







    def visit(sf, result_of_dir_cmp__relative, /):
        rhs_dir_viewer = sf.get_rhs_dir_viewer()
        rhs_root_path = sf.get_rhs_root_path()
        #to_skip from [on_right_only_new_top_dir__enter, on_remove_file_and_new_top_dir__enter, on_new_top_dir__enter, on_new_dir__enter]
        def _test_to_skip(to_skip, /):
            #print(type(to_skip))
            if type(to_skip) is not bool: raise TypeError
            return to_skip
        def _is_file(xhs_relative_filedir_path, /):
            return rhs_dir_viewer.is_file(rhs_root_path/xhs_relative_filedir_path)

        def _on_new_filedir(xhs_relative_filedir_path, /):
            if sf.xhs_relative_filedir_path2is_ignore(xhs_relative_filedir_path): return
            if _is_file(xhs_relative_filedir_path):
                f = sf.on_new_file_under_new_dir
            else:
                f = _on_new_dir
            f(xhs_relative_filedir_path)
        def _on_new_dir(xhs_relative_dir_path, /):
            f = sf.on_new_dir__enter
            to_skip = f(xhs_relative_dir_path)
            if _test_to_skip(to_skip): return

            if 1:
                basenames = rhs_dir_viewer.dir_iter(rhs_root_path/xhs_relative_dir_path)
                for basename in basenames:
                    f = _on_new_filedir
                    f(xhs_relative_dir_path/basename)
            else:
                pass
            f = sf.on_new_dir__exit
            f(xhs_relative_dir_path)
        #end of def _on_new_dir(xhs_relative_dir_path, /):
        def _on_new_top_dir(xhs_relative_dir_path, /):
            gs = [sf.on_new_top_dir__enter
                ,_on_new_dir
                ,sf.on_new_top_dir__exit
                ]
            _run(gs, xhs_relative_dir_path)
        #end of def _on_new_top_dir(xhs_relative_dir_path, /):
        def _run(gs, xhs_relative_filedir_path, /):
            assert gs
            if len(gs) == 1:
                [g] = gs
                g(xhs_relative_filedir_path)
            else:
                [g_enter, *gs] = gs
                to_skip = g_enter(xhs_relative_filedir_path)
                if not _test_to_skip(to_skip):
                    for g in gs:
                        g(xhs_relative_filedir_path)
        #end of def _run(gs, xhs_relative_filedir_path, /):



        def _main():
            for case, xhs_relative_filedir_path in result_of_dir_cmp__relative:
                if case == 0:
                    gs = [sf.on_diff_file]
                elif case == -1:
                    #left only
                    gs = [sf.on_remove_file_or_top_dir]
                elif case == +1:
                    #right only
                    if _is_file(xhs_relative_filedir_path):
                        gs = [sf.on_right_only_new_file]
                    else:

                        gs = [sf.on_right_only_new_top_dir__enter
                            ,_on_new_top_dir
                            ,sf.on_right_only_new_top_dir__exit
                            ]
                elif case == -2:
                    #left dir & right file
                    gs = [sf.on_remove_top_dir_and_new_file]
                elif case == +2:
                    #left file & right dir
                    gs = [sf.on_remove_file_and_new_top_dir__enter
                        ,_on_new_top_dir
                        ,sf.on_remove_file_and_new_top_dir__exit
                        ]
                else:
                    raise ValueError('not result_of_dir_cmp__relative')
                gs

                _run(gs, xhs_relative_filedir_path)
        #end of def _main():
        _main()
        return
    pass
#end of class IVisit_result_of_dir_cmp__relative(ABC):

class Visit_result_of_dir_cmp__relative(IVisit_result_of_dir_cmp__relative):
    @override
    def xhs_relative_filedir_path2is_ignore(sf, xhs_relative_filedir_path, /):
        'xhs_relative_filedir_path -> bool #see:mk_relative_path2is_ignore'
        return sf.__ignore_relative_path(xhs_relative_filedir_path)
    @override
    def get_rhs_dir_viewer(sf, /):
        '-> rhs_dir_viewer'
        return sf.__rhs_dir_viewer
    @override
    def get_rhs_root_path(sf, /):
        '-> rhs_root_path'
        return sf.__rhs_root_path

    def __init__(sf, rhs_dir_viewer:IDirViewer, rhs_root_path, ignore_relative_path, /):
        'ignore_relative_path # see: dir_cmp.mk_relative_path2is_ignore'
        if not isinstance(rhs_dir_viewer, IDirViewer): raise TypeError
        if not callable(ignore_relative_path): raise TypeError
        sf.__rhs_dir_viewer = rhs_dir_viewer
        sf.__rhs_root_path = rhs_root_path
        sf.__ignore_relative_path = ignore_relative_path

    pass
#end of class Visit_result_of_dir_cmp__relative(IVisit_result_of_dir_cmp__relative):

class IRun_file_diff_over_result_of_dir_cmp__relative(Visit_result_of_dir_cmp__relative):
    def __init__(sf, lhs_access_file:IAccessFile4MkIsSameFile, lhs_root_path, rhs_dir_viewer:IDirViewer, rhs_access_file:IAccessFile4MkIsSameFile, rhs_root_path, ignore_relative_path, /):
        'ignore_relative_path # see: dir_cmp.mk_relative_path2is_ignore'
        sf.lhs_access_file = lhs_access_file
        sf.lhs_root_path = lhs_root_path
        #sf.rhs_dir_viewer = rhs_dir_viewer
        sf.rhs_access_file = rhs_access_file
        #sf.rhs_root_path = rhs_root_path
        #sf.ignore_relative_path = ignore_relative_path
        sf.__overwrite_file_by_dir = ...
        super().__init__(rhs_dir_viewer, rhs_root_path, ignore_relative_path)
    @property
    def rhs_dir_viewer(sf, /):
        return sf.get_rhs_dir_viewer()
    @property
    def rhs_root_path(sf, /):
        return sf.get_rhs_root_path()
    @abstractmethod
    def run_file_diff(sf, lhs_root_path, rhs_root_path, xhs_relative_file_path, lhs_pseudo_ifile, rhs_pseudo_ifile, /):
        ''
    @abstractmethod
    def create_file(sf, may_lhs_root_path, rhs_root_path, xhs_relative_filedir_path, rhs_pseudo_ifile, /):
        ''
    @abstractmethod
    def create_dir(sf, may_lhs_root_path, rhs_root_path, xhs_relative_filedir_path, /):
        ''
    @abstractmethod
    def remove_filedir(sf, lhs_root_path, xhs_relative_filedir_path, /):
        ''

    r'''
    def on_diff_file
    def on_right_only_new_file
    def on_new_file_under_new_dir
    def on_new_dir__enter
    def on_remove_file_or_top_dir
    def on_remove_file_and_new_top_dir__enter
    def on_remove_top_dir_and_new_file
    def on_right_only_new_top_dir__enter
    #'''
    def on_diff_file(sf, xhs_relative_file_path, /):
        '#overwrite_file_by_file'
        lhs_root_path = sf.lhs_root_path
        rhs_root_path = sf.rhs_root_path
        lhs_file_path = lhs_root_path/xhs_relative_file_path
        rhs_file_path = rhs_root_path/xhs_relative_file_path
        if 0:
            #bug: should be "with file:"
            lhs_pseudo_ifile = sf.lhs_access_file.open(lhs_file_path)
            #bug:rhs_pseudo_ifile = sf.rhs_access_file.open(lhs_file_path)
            rhs_pseudo_ifile = sf.rhs_access_file.open(rhs_file_path)

        with sf.lhs_access_file.open(lhs_file_path) as lhs_pseudo_ifile, sf.rhs_access_file.open(rhs_file_path) as rhs_pseudo_ifile:
            sf.run_file_diff(lhs_root_path, rhs_root_path, xhs_relative_file_path, lhs_pseudo_ifile, rhs_pseudo_ifile)

        sf.__overwrite_file_by_dir = ...

    def _on_new_file(sf, to_overwrite:bool, rhs_relative_file_path, /):
        if to_overwrite:
            may_lhs_root_path = sf.lhs_root_path
        else:
            may_lhs_root_path = None
        rhs_root_path = sf.rhs_root_path
        rhs_file_path = rhs_root_path/rhs_relative_file_path
        #bug: rhs_pseudo_ifile = sf.rhs_access_file.open(rhs_file_path)
        #   using "with"
        with sf.rhs_access_file.open(rhs_file_path) as rhs_pseudo_ifile:
            xhs_relative_filedir_path = rhs_relative_file_path
            sf.create_file(may_lhs_root_path, rhs_root_path, xhs_relative_filedir_path, rhs_pseudo_ifile)

    def on_right_only_new_file(sf, rhs_relative_file_path, /):
        '.visit() not call on_new_file_under_new_dir'
        sf._on_new_file(False, rhs_relative_file_path)
    def on_new_file_under_new_dir(sf, rhs_relative_file_path, /):
        'only call between on_new_dir__enter/on_new_dir__exit; not with on_right_only_new_file'
        sf._on_new_file(False, rhs_relative_file_path)
    @override
    def on_new_dir__enter(sf, rhs_relative_dir_path, /):
        r'''-> to_skip:bool
        if to_skip==True: not call inside & exit
        else: '.visit() call on_new_file_under_new_dir/recur call on_new_dir__enter/on_new_dir__exit'
        #'''
        if sf.__overwrite_file_by_dir:
            sf.__overwrite_file_by_dir = False
            may_lhs_root_path = sf.lhs_root_path
        else:
            may_lhs_root_path = None
        rhs_root_path = sf.rhs_root_path
        sf.create_dir(may_lhs_root_path, rhs_root_path, rhs_relative_dir_path)
        #return__to_skip
        ##bug:return
        to_skip = False
        return to_skip

    def on_remove_file_or_top_dir(sf, lhs_relative_file_path, /):
        ''
        sf.remove_filedir(sf.lhs_root_path, lhs_relative_file_path)

    def on_remove_top_dir_and_new_file(sf, xhs_relative_filedir_path, /):
        '.visit() not call on_new_file_under_new_dir;  #overwrite_dir_by_file'
        sf._on_new_file(True, xhs_relative_filedir_path)

    def on_remove_file_and_new_top_dir__enter(sf, xhs_relative_filedir_path, /):
        r'''-> to_skip:bool     #overwrite_file_by_dir
        if to_skip==True: not call inside & exit
        else: '.visit() call on_new_top_dir__enter/on_new_top_dir__exit'
        #'''
        sf.__overwrite_file_by_dir = True
        #return__to_skip
        ##bug:return
        to_skip = False
        return to_skip

    @override
    def on_right_only_new_top_dir__enter(sf, rhs_relative_dir_path, /):
        r'''-> to_skip:bool
        if to_skip==True: not call inside & exit
        else: '.visit() call on_new_top_dir__enter/on_new_top_dir__exit'
        #'''
        sf.__overwrite_file_by_dir = False
        #return__to_skip
        ##bug:return
        to_skip = False
        return to_skip


#end of class IRun_file_diff_over_result_of_dir_cmp__relative(Visit_result_of_dir_cmp__relative):





class IRun_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes(IRun_file_diff_over_result_of_dir_cmp__relative):
    @abstractmethod
    def update_fsys_patch_mapping__mk_dir(sf, xhs_relative_file_path, /):
        'update underlying fsys_patch_mapping - subcase:mk_dir'
    @abstractmethod
    def update_fsys_patch_mapping__remove_filedir(sf, xhs_relative_file_path, /):
        'update underlying fsys_patch_mapping - subcase:remove_filedir'
    @abstractmethod
    def update_fsys_patch_mapping__update_file(sf, xhs_relative_file_path, pseudo_virtual_file_reprobj, /):
        'update underlying fsys_patch_mapping - subcase:update_file #new/patch'

    @abstractmethod
    def lhs_file_path2pseudo_virtual_file_reprobj4fsys_mapping_ex(sf, lhs_root_path, xhs_relative_file_path, /):
        '-> old_pseudo_virtual_file_reprobj # old~parent'
    @abstractmethod
    def ___read_rhs_file_metadata___(sf, rhs_root_path, xhs_relative_file_path, /):
        '-> rhs_file_metadata#see: mk_basic_rhs_file_metadata/read_rhs_file_metadata/___read_rhs_file_metadata___/___try_to_get_rhs_file_str_mtime___'
        basic_rhs_file_metadata = sf.mk_basic_rhs_file_metadata(rhs_root_path, xhs_relative_file_path)
        rhs_file_metadata = basic_rhs_file_metadata
        return rhs_file_metadata
    @abstractmethod
    def ___try_to_get_rhs_file_str_mtime___(sf, rhs_root_path, xhs_relative_file_path, /):
        '-> may_str_mtime #see: mk_basic_rhs_file_metadata/read_rhs_file_metadata/___read_rhs_file_metadata___/___try_to_get_rhs_file_str_mtime___'

    @abstractmethod
    def push_store_contentfile_bytes_and_mk_pseudo_virtual_file_reprobj4fsys_mapping_ex(sf, may_lhs_root_path, tmay_old_pseudo_virtual_file_reprobj, rhs_root_path, xhs_relative_file_path, rhs_file_metadata, contentfile_bytes, /):
        r'''->new_pseudo_virtual_file_reprobj
        what to do in this method?
            e.g. @IRepositorySetting: tmp push/store (imay_parent_idx, contentfile_bytes, rhs_file_metadata) into file_stack_dir_path to be moved to file_patch_forest_dir_path

        may_lhs_root_path
            used to distinguish lhs=(not_exists|filedir)
            may not (may_lhs_root_path is None) is (tmay_old_pseudo_virtual_file_reprobj == ())
            when lhs is (not exists|dir|file):
                may_lhs_root_path is (None|lhs_root_path|lhs_root_path)
                tmay_old_pseudo_virtual_file_reprobj is (()|()|(old_pseudo_virtual_file_reprobj,))
        tmay_old_pseudo_virtual_file_reprobj
            used to distinguish contentfile_bytes=either original_file_bytes or patch_file_bytes
            old_pseudo_virtual_file_reprobj
                e.g. parent_idx@imay_parent_idx@IRepositorySetting
        xhs_relative_file_path
            used to find latest lhs_file info
                e.g. imay_parent_idx@IRepositorySetting
        new_pseudo_virtual_file_reprobj
            pseudo_virtual_file_reprobj@fsys_mapping_ex
            e.g. patch_idx@IRepositorySetting
                patch_idx := new_pseudo_virtual_file_reprobj
                parent_idx := old_pseudo_virtual_file_reprobj
        #'''
    @abstractmethod
    def file_diff__file_bytes(sf, lhs_file_bytes, rhs_file_bytes, /):
        '-> patch_file_bytes'


    def read_rhs_file_metadata(sf, rhs_root_path, xhs_relative_file_path, /):
        '-> rhs_file_metadata#see: mk_basic_rhs_file_metadata/read_rhs_file_metadata/___read_rhs_file_metadata___/___try_to_get_rhs_file_str_mtime___ #fill str_mtime&SHA256'
        rhs_file_path = rhs_root_path/xhs_relative_file_path
        rhs_file_metadata = type(sf).___read_rhs_file_metadata___(sf, rhs_root_path, xhs_relative_file_path)

        may_str_mtime = rhs_file_metadata[metadata_keys_setting.key4may_str_mtime] #must exist, but can be empty or None!
            #
        if may_str_mtime is None or may_str_mtime == '':
            may_str_mtime = type(sf).___try_to_get_rhs_file_str_mtime___(sf, rhs_file_path)
        if may_str_mtime is None or may_str_mtime == '':
            may_str_mtime = None
        rhs_file_metadata[metadata_keys_setting.key4may_str_mtime] = may_str_mtime


        may_hash_method_uppercase_std_name2upper_hex_digest = rhs_file_metadata[metadata_keys_setting.key4may_hash_method_uppercase_std_name2upper_hex_digest] #must exist, but can be empty or None!
        if may_hash_method_uppercase_std_name2upper_hex_digest is None:
            hash_method_uppercase_std_name2upper_hex_digest = {}
        else:
            hash_method_uppercase_std_name2upper_hex_digest = may_hash_method_uppercase_std_name2upper_hex_digest
        rhs_file_metadata[metadata_keys_setting.key4may_hash_method_uppercase_std_name2upper_hex_digest] = hash_method_uppercase_std_name2upper_hex_digest

        if 'SHA256' not in hash_method_uppercase_std_name2upper_hex_digest:
            with sf.rhs_access_file.open(rhs_file_path) as bfin:
                digest_upper_hex_str = calc_SHA256__file(bfin, hex=True, upper=True)
            hash_method_uppercase_std_name2upper_hex_digest['SHA256'] = digest_upper_hex_str
        return rhs_file_metadata
 


    def mk_basic_rhs_file_metadata(sf, rhs_root_path, xhs_relative_file_path, /):
        '-> rhs_file_metadata#see: mk_basic_rhs_file_metadata/read_rhs_file_metadata/___read_rhs_file_metadata___/___try_to_get_rhs_file_str_mtime___'
        rhs_file_path = rhs_root_path / xhs_relative_file_path
        file_size = sf.rhs_access_file.get_file_size(rhs_file_path)
        may_str_mtime = sf.rhs_access_file.get_may_str_mtime(rhs_file_path)
        may_hash_method_uppercase_std_name2upper_hex_digest = sf.rhs_access_file.get_may_hash_method_uppercase_std_name2upper_hex_digest(rhs_file_path)
        metadata = {metadata_keys_setting.key4file_size: file_size, metadata_keys_setting.key4may_str_mtime: may_str_mtime, metadata_keys_setting.key4may_hash_method_uppercase_std_name2upper_hex_digest: may_hash_method_uppercase_std_name2upper_hex_digest}
        rhs_file_metadata = metadata
        return rhs_file_metadata


    @override
    def run_file_diff(sf, lhs_root_path, rhs_root_path, xhs_relative_file_path, lhs_pseudo_ifile, rhs_pseudo_ifile, /):
        ''
        rhs_file_metadata = sf.read_rhs_file_metadata(rhs_root_path, xhs_relative_file_path)
        old_pseudo_virtual_file_reprobj = sf.lhs_file_path2pseudo_virtual_file_reprobj4fsys_mapping_ex(lhs_root_path, xhs_relative_file_path)
            #old~parent

        lhs_file_bytes = lhs_pseudo_ifile.read(-1)
        rhs_file_bytes = rhs_pseudo_ifile.read(-1)
        #bug:patch_file_bytes = sf.file_diff__file_bytes(lhs_file_bytes, rhs_file_bytes, ver=1)
        patch_file_bytes = sf.file_diff__file_bytes(lhs_file_bytes, rhs_file_bytes)
        contentfile_bytes = patch_file_bytes

        may_lhs_root_path = lhs_root_path
        tmay_old_pseudo_virtual_file_reprobj = (old_pseudo_virtual_file_reprobj,)
        new_pseudo_virtual_file_reprobj = sf.push_store_contentfile_bytes_and_mk_pseudo_virtual_file_reprobj4fsys_mapping_ex(may_lhs_root_path, tmay_old_pseudo_virtual_file_reprobj, rhs_root_path, xhs_relative_file_path, rhs_file_metadata, contentfile_bytes)
        sf.update_fsys_patch_mapping__update_file(xhs_relative_file_path, new_pseudo_virtual_file_reprobj)

    @override
    def create_file(sf, may_lhs_root_path, rhs_root_path, xhs_relative_filedir_path, rhs_pseudo_ifile, /):
        ''
        rhs_relative_file_path = xhs_relative_filedir_path
        rhs_file_metadata = sf.read_rhs_file_metadata(rhs_root_path, rhs_relative_file_path)
        rhs_bytes = rhs_pseudo_ifile.read(-1)
        original_file_bytes = rhs_bytes
        contentfile_bytes = original_file_bytes
        tmay_old_pseudo_virtual_file_reprobj = ()
        new_pseudo_virtual_file_reprobj = sf.push_store_contentfile_bytes_and_mk_pseudo_virtual_file_reprobj4fsys_mapping_ex(may_lhs_root_path, tmay_old_pseudo_virtual_file_reprobj, rhs_root_path, rhs_relative_file_path, rhs_file_metadata, contentfile_bytes)
        sf.update_fsys_patch_mapping__update_file(rhs_relative_file_path, new_pseudo_virtual_file_reprobj)


    @override
    def create_dir(sf, may_lhs_root_path, rhs_root_path, xhs_relative_filedir_path, /):
        ''
        sf.update_fsys_patch_mapping__mk_dir(xhs_relative_filedir_path)

    @override
    def remove_filedir(sf, lhs_root_path, xhs_relative_filedir_path, /):
        ''
        sf.update_fsys_patch_mapping__remove_filedir(xhs_relative_filedir_path)

#end of class IRun_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes(IRun_file_diff_over_result_of_dir_cmp__relative):

class IRun_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes__using_file_cmp_file_diff_ver1(IRun_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes):
    @property
    @abstractmethod
    def lcp_threshold(sf, /):
        '->lcp_threshold::uint @nn_ns.filedir.file_cmp.file_diff'
    @override
    def file_diff__file_bytes(sf, lhs_file_bytes, rhs_file_bytes, /):
        '-> patch_file_bytes'
        patch_bytes_ex4file_diff = file_diff(sf.lcp_threshold, lhs_file_bytes, rhs_file_bytes, ver=1)
        patch_file_bytes = patch_bytes_ex4file_diff
        return patch_file_bytes
#end of class IRun_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes__using_file_cmp_file_diff_ver1(IRun_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes):
class IRun_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes__using_IRepositorySetting(IRun_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes):
    r'''
    + def finish_visit/mk_commit/mk_commit_and_push/main

    @abstractmethod
        def file_diff__file_bytes(sf, lhs_file_bytes, rhs_file_bytes, /):
        def ___read_rhs_file_metadata___(sf, rhs_root_path, xhs_relative_file_path, /):
        def ___try_to_get_rhs_file_str_mtime___(sf, rhs_root_path, xhs_relative_file_path, /):
    #'''
    def main(sf, result_of_dir_cmp__relative, /):
        sf.mk_commit_and_push(result_of_dir_cmp__relative)
    r'''
    @override
    file_diff__file_bytes
        <<== IRun_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes__using_file_cmp_file_diff_ver1

    #'''

    def __init__(sf, lhs_repository_setting:IRepositorySetting, lhs_branch_name, lhs_may_signed_branch_idx, lhs_relative_path:'lhs_root_path', rhs_dir_viewer:IDirViewer, rhs_access_file:IAccessFile4MkIsSameFile, rhs_root_path, /):
        rhs_path = rhs_root_path
        (_, lhs_dir_viewer, lhs_access_file, ignore_relative_path, open_ignorefile_text_ifile, lhs_branch_idx) = mk_args_ex4dir_cmp__with_IRepositorySetting(lhs_repository_setting, lhs_branch_name, lhs_may_signed_branch_idx, rhs_access_file, rhs_path, True)

        sf.lhs_repository_setting = lhs_repository_setting
        sf.lhs_branch_name = lhs_branch_name
        sf.lhs_branch_idx = lhs_branch_idx
        sf.__offsetted_fsys_patch_mapping = {}
            #offset by lhs_root_path=lhs_relative_path@IRepositorySetting
        sf._lhs_dir_viewer = lhs_dir_viewer
        sf.__next_new_patch_idx = lhs_repository_setting.get_len_inf_dir_of_file_patch_forest()
        sf.__move_cmds = []
        if 1:
            sf.__file_stack_dir_sz = 0
            sf.lhs_repository_setting.clean_updating_root_dir()
            file_stack_dir_path = sf.lhs_repository_setting.get_file_stack_dir_path()
            os.makedirs(file_stack_dir_path, exist_ok=False)


        lhs_root_path = lhs_relative_path
        super().__init__(lhs_access_file, lhs_root_path, rhs_dir_viewer, rhs_access_file, rhs_root_path, ignore_relative_path)
    def _alloc_patch_idx(sf, /):
        new_patch_idx = sf.__next_new_patch_idx
        sf.__next_new_patch_idx += 1
        return new_patch_idx
    def _mkdirs_to_parent_and_return_with_basename(sf, xhs_relative_filedir_path, /):
        '-> sub_fsys_patch_mapping'
        parts = relative_path2parts(xhs_relative_filedir_path)
        if not parts: raise ValueError('empty xhs_relative_filedir_path')
        d = sf.__offsetted_fsys_patch_mapping
        for basename in parts[:-1]:
            d = d.setdefault(basename, {})
            if not type(d) is dict: raise logic-err
        basename = parts[-1]
        if basename in d: raise logic-err

        assert type(d) is dict
        assert basename not in d
        return d, basename
    @override
    def update_fsys_patch_mapping__mk_dir(sf, xhs_relative_file_path, /):
        'update underlying fsys_patch_mapping - subcase:mk_dir'
        d, basename = sf._mkdirs_to_parent_and_return_with_basename(xhs_relative_file_path)
        assert basename not in d
        d[basename] = {}
    @override
    def update_fsys_patch_mapping__remove_filedir(sf, xhs_relative_file_path, /):
        'update underlying fsys_patch_mapping - subcase:remove_filedir'
        d, basename = sf._mkdirs_to_parent_and_return_with_basename(xhs_relative_file_path)
        assert basename not in d
        d[basename] = None
    @override
    def update_fsys_patch_mapping__update_file(sf, xhs_relative_file_path, pseudo_virtual_file_reprobj, /):
        'update underlying fsys_patch_mapping - subcase:update_file #new/patch'
        patch_idx = pseudo_virtual_file_reprobj
        #print(patch_idx)
        check_uint(patch_idx)

        d, basename = sf._mkdirs_to_parent_and_return_with_basename(xhs_relative_file_path)
        assert basename not in d
        d[basename] = patch_idx


    @override
    def lhs_file_path2pseudo_virtual_file_reprobj4fsys_mapping_ex(sf, lhs_root_path, xhs_relative_file_path, /):
        '-> old_pseudo_virtual_file_reprobj # old~parent'
        lhs_file_path = sf.lhs_root_path/xhs_relative_file_path
        lhs_relative_file_path4IRepositorySetting = lhs_file_path
        patch_idx = sf.lhs_access_file.virtual_file_path2patch_idx(lhs_relative_file_path4IRepositorySetting)
        old_pseudo_virtual_file_reprobj = parent_idx = patch_idx
        return old_pseudo_virtual_file_reprobj
    @override
    def push_store_contentfile_bytes_and_mk_pseudo_virtual_file_reprobj4fsys_mapping_ex(sf, may_lhs_root_path, tmay_old_pseudo_virtual_file_reprobj, rhs_root_path, xhs_relative_file_path, rhs_file_metadata, contentfile_bytes, /):
        r'''->new_pseudo_virtual_file_reprobj
        what to do in this method?
            e.g. @IRepositorySetting: tmp push/store (imay_parent_idx, contentfile_bytes, rhs_file_metadata) into file_stack_dir_path to be moved to file_patch_forest_dir_path

        may_lhs_root_path
            used to distinguish lhs=(not_exists|filedir)
            may not (may_lhs_root_path is None) is (tmay_old_pseudo_virtual_file_reprobj == ())
            when lhs is (not exists|dir|file):
                may_lhs_root_path is (None|lhs_root_path|lhs_root_path)
                tmay_old_pseudo_virtual_file_reprobj is (()|()|(old_pseudo_virtual_file_reprobj,))
        tmay_old_pseudo_virtual_file_reprobj
            used to distinguish contentfile_bytes=either original_file_bytes or patch_file_bytes
            old_pseudo_virtual_file_reprobj
                e.g. parent_idx@imay_parent_idx@IRepositorySetting
        xhs_relative_file_path
            used to find latest lhs_file info
                e.g. imay_parent_idx@IRepositorySetting
        new_pseudo_virtual_file_reprobj
            pseudo_virtual_file_reprobj@fsys_mapping_ex
            e.g. patch_idx@IRepositorySetting
                patch_idx := new_pseudo_virtual_file_reprobj
                parent_idx := old_pseudo_virtual_file_reprobj
        #'''
        if tmay_old_pseudo_virtual_file_reprobj:
            [old_pseudo_virtual_file_reprobj] = tmay_old_pseudo_virtual_file_reprobj
            parent_idx = old_pseudo_virtual_file_reprobj
            check_uint(parent_idx)
            imay_parent_idx = parent_idx
            patch_file_bytes = contentfile_bytes
        else:
            imay_parent_idx = -1
            original_file_bytes = contentfile_bytes
        imay_parent_idx

        #to store ... into file_stack_dir_path->file_patch_forest_dir_path/**/user_data_dir_path
        imay_parent_idx
        contentfile_bytes
        rhs_file_metadata

        # whole not per, do when finish:
            #to mk fsys_delta to store into file_stack_dir_path->branch_history_dir_path
            #to mk command_history_cmd to store into file_stack_dir_path->command_history_dir_path


        new_patch_idx = sf._alloc_patch_idx()
        idx4file_patch_forest = new_patch_idx
        move_cmd_target = 'move_into_file_patch_forest'
        idx4move_cmd_target = idx4file_patch_forest
        ls = [
            ('parent', imay_parent_idx, sf.lhs_repository_setting.write_imay_parent_idx)
            ,('content', contentfile_bytes, lambda binary_ofile, contentfile_bytes: binary_ofile.write(contentfile_bytes))
            ,('metadata', rhs_file_metadata, sf.lhs_repository_setting.write_metadata)
            ]
        for user_data_file__virtual_name, data, write_func in ls:
            move_cmd_target_args = (user_data_file__virtual_name,)
            sf._push_store_py_obj_and_mk_move_cmd(write__binary_ofile__py_obj=write_func, py_obj=data, move_cmd_target=move_cmd_target, move_cmd_target_args=move_cmd_target_args, idx4move_cmd_target=idx4move_cmd_target)

        ##
        #bug:return
        new_pseudo_virtual_file_reprobj = new_patch_idx
        return new_pseudo_virtual_file_reprobj
    def _mk_offsetted_fsys_patch_frozendict_ex(sf, /):

        offsetted_fsys_patch_frozendict = deepcopy_fsys_mapping_ex(dst_mapping_type_from_dict=FrozenDict, src_fsys_mapping_ex=sf.__offsetted_fsys_patch_mapping, may_mapping_types_or_check_mapping_type=(dict,), pseudo_virtual_file_reprobj_checker_cls=pseudo_virtual_file_reprobj_checker_cls4fsys_patch_mapping)
        lhs_dst_dir_relative_path4IRepositorySetting = sf.lhs_root_path
        return lhs_dst_dir_relative_path4IRepositorySetting, offsetted_fsys_patch_frozendict
        r'''bug: relative_path__str in offsetted_fsys_patch_frozendict is not unoffsetted
        parts = relative_path2parts(lhs_dst_dir_relative_path4IRepositorySetting)
        for basename in reversed(parts):
            offsetted_fsys_patch_frozendict = FrozenDict([(basename, offsetted_fsys_patch_frozendict)])
        unoffsetted_fsys_patch_frozendict = offsetted_fsys_patch_frozendict
        return lhs_dst_dir_relative_path4IRepositorySetting, offsetted_fsys_patch_frozendict, unoffsetted_fsys_patch_frozendict
        #'''

    def mk_commit_and_push(sf, result_of_dir_cmp__relative, /):
        sf.mk_commit(result_of_dir_cmp__relative)
        sf.lhs_repository_setting.clean_updating_root_dir()
    def mk_commit(sf, result_of_dir_cmp__relative, /):
        'see: IRepositorySetting.clean_updating_root_dir'
        #fill updating/file_stack/
        sf.visit(result_of_dir_cmp__relative)
        move_cmds = sf.finish_visit()

        #mk TODO_list4move_cmd_file
        sf.lhs_repository_setting.check_move_cmds(move_cmds)
        TODO_list4move_cmd_file_path = sf.lhs_repository_setting.get_TODO_list4move_cmd_file_path()
        with open(TODO_list4move_cmd_file_path, 'xb') as binary_ofile:
            sf.lhs_repository_setting.write_move_cmds(binary_ofile, move_cmds)

        #mk commit_completed_file #empty
        commit_completed_file_path = sf.lhs_repository_setting.get_commit_completed_file_path()
        with open(commit_completed_file_path, 'xb') as binary_ofile:
            #close === mk empty file
            pass
        return


    def finish_visit(sf, /):
        '-> [move_cmd]'
        #to mk command_history_cmd to store into file_stack_dir_path->command_history_dir_path
        #to mk fsys_delta to store into file_stack_dir_path->branch_history_dir_path
        #       fsys_deltas should be last one to push
        #       ==>> first one to pop into branch_history_dir, hence assert branch_idx is latest
        lhs_dst_dir_relative_path4IRepositorySetting, offsetted_fsys_patch_frozendict = sf._mk_offsetted_fsys_patch_frozendict_ex()
        fsys_deltas = sf.mk_fsys_deltas(lhs_dst_dir_relative_path4IRepositorySetting, offsetted_fsys_patch_frozendict)
        check_tuple(fsys_deltas)
        if 1:
            #FrozenDict -> dict for ast.literal_eval
            #now using read_branch_history_deltas/write_branch_history_deltas
            pass

        #read_repred_py_obj
        #write_py_obj_as_repr
        #command_history_cmd = (new branch_time, new len_inf_dir_of_file_patch_forest, [high_level_user_command__str])
        #next_branch_time = (sf.branch_name, sf.branch_idx+1)
        next_branch_time = (sf.lhs_branch_name, sf.lhs_branch_idx+1)
        expected_len_inf_dir_of_file_patch_forest = sf.__next_new_patch_idx
        high_level_user_command__strs = ('dir_cmp__relative',)
        command_history_cmd = next_branch_time, expected_len_inf_dir_of_file_patch_forest, high_level_user_command__strs
        #check lhs_branch_idx is latest/correct
        latest_branch_idx = sf.lhs_repository_setting.resolve_may_signed_branch_idx(sf.lhs_branch_name, -1)
        if not sf.lhs_branch_idx == latest_branch_idx: raise ValueError

        if 1:
            move_cmd_target = 'push_into_command_history'
            move_cmd_target_args = ()
            idx4move_cmd_target = sf.lhs_repository_setting.get_len_inf_dir_of_command_history()
            py_obj = command_history_cmd
            write__binary_ofile__py_obj = sf.lhs_repository_setting.write_command_history_cmd
            sf._push_store_py_obj_and_mk_move_cmd(write__binary_ofile__py_obj=write__binary_ofile__py_obj, py_obj=py_obj, move_cmd_target=move_cmd_target, move_cmd_target_args=move_cmd_target_args, idx4move_cmd_target=idx4move_cmd_target)
            ##
        if 1:
            #should be last push of curr commit
            move_cmd_target = 'push_into_branch_fsys_history'
            move_cmd_target_args = (next_branch_time[0],)
            idx4move_cmd_target = next_branch_time[1]
            py_obj = fsys_deltas
            write__binary_ofile__py_obj = sf.lhs_repository_setting.write_branch_history_deltas
            sf._push_store_py_obj_and_mk_move_cmd(write__binary_ofile__py_obj=write__binary_ofile__py_obj, py_obj=py_obj, move_cmd_target=move_cmd_target, move_cmd_target_args=move_cmd_target_args, idx4move_cmd_target=idx4move_cmd_target)
            ##
        #bug:move_cmds = tuple(sf.__move_cmds)
        move_cmds = tuple(reversed(sf.__move_cmds))
        sf.lhs_repository_setting.check_move_cmds(move_cmds)
        return move_cmds

    def _push_store_py_obj_and_mk_move_cmd(sf, /,*, write__binary_ofile__py_obj, py_obj, move_cmd_target, move_cmd_target_args, idx4move_cmd_target):
        (idx4file_stack, binary_ofile) = sf._open_new_file_and_push_into_file_stack_dir()
        with binary_ofile:
            write__binary_ofile__py_obj(binary_ofile, py_obj)
        move_cmd = (idx4file_stack, move_cmd_target, move_cmd_target_args, idx4move_cmd_target)
        sf.lhs_repository_setting.check_move_cmd(move_cmd)
        sf.__move_cmds.append(move_cmd)
    def _open_new_file_and_push_into_file_stack_dir(sf, /):
        '-> (idx4file_stack, binary_ofile) #idx4file_stack to mk move_cmd'
        idx4file_stack = sf.__file_stack_dir_sz
        sf.__file_stack_dir_sz += 1
        file_path = sf.lhs_repository_setting.get_file_stack_dir_path() / inf_dir_idx2user_data_relative_path(idx4file_stack, dir_size=sf.lhs_repository_setting.get_dir_size())
        dir_path = file_path.parent
        os.makedirs(dir_path, exist_ok=True)
        binary_ofile = open(file_path, 'xb')
            #shouldnot be "wb" to avoid unclean updating commit: see:IRepositorySetting.clean_updating_root_dir()
        return idx4file_stack, binary_ofile




    #@abstractmethod
    @override
    def mk_fsys_deltas(sf, lhs_dst_dir_relative_path4IRepositorySetting, offsetted_fsys_patch_frozendict, /):
        r'''-> tuple<fsys_delta>
see: nn_ns.filedir.backup_tools.FileSystem4update
    command_history_cmd = (new branch_time, new len_inf_dir_of_file_patch_forest, [high_level_user_command__str])
    fsys_delta = fsys_update_cmd | branch_history_cmd
        #'''
        return sf._mk_fsys_deltas__cmd__update_fsys(lhs_dst_dir_relative_path4IRepositorySetting, offsetted_fsys_patch_frozendict)
    def _mk_fsys_deltas__cmd__update_fsys(sf, lhs_dst_dir_relative_path4IRepositorySetting, offsetted_fsys_patch_frozendict, /):
        r'''-> tuple<fsys_delta>
        see: mk_fsys_deltas
        for fsys_update_cmd/branch_history_cmd

        ('update_fsys', dst_dir_relative_path, offsetted_fsys_patch_frozendict)
        #'''
        dst_dir_relative_path = lhs_dst_dir_relative_path4IRepositorySetting
        cmd = ('update_fsys', dst_dir_relative_path, offsetted_fsys_patch_frozendict)
        fsys_delta = cmd
        fsys_deltas = (fsys_delta,)
        return fsys_deltas

#end of class IRun_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes__using_IRepositorySetting(IRun_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes):

_common_base4Run = (IRun_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes__using_IRepositorySetting, IRun_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes__using_file_cmp_file_diff_ver1)
class IRun_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes__using_file_cmp_file_diff_ver1__using_IRepositorySetting(*_common_base4Run):
    #def __init__(sf, lhs_repository_setting:IRepositorySetting, lhs_branch_name, lhs_may_signed_branch_idx, lhs_relative_path:'lhs_root_path', rhs_dir_viewer:IDirViewer, rhs_access_file:IAccessFile4MkIsSameFile, rhs_root_path):
    pass

#end of class IRun_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes__using_file_cmp_file_diff_ver1__using_IRepositorySetting(IRun_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes__using_IRepositorySetting, IRun_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes__using_file_cmp_file_diff_ver1):




class Run_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes__using_file_cmp_file_diff_ver1__using_IRepositorySetting__rhs_is_real_fsys(IRun_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes__using_file_cmp_file_diff_ver1__using_IRepositorySetting):
    def __init__(sf, lhs_repository_setting, lhs_branch_name, lhs_may_signed_branch_idx, lhs_relative_path, rhs_root_path, /,*, lcp_threshold):
        rhs_dir_viewer = DirViewer__fsys()
        rhs_access_file = AccessFile4MkIsSameFile__fsys()
        super().__init__(lhs_repository_setting, lhs_branch_name, lhs_may_signed_branch_idx, lhs_relative_path, rhs_dir_viewer, rhs_access_file, rhs_root_path)
        if not lcp_threshold >= 1: raise ValueError
        sf.__lcp_threshold = lcp_threshold
    @property
    @override
    def lcp_threshold(sf, /):
        '->lcp_threshold::uint @nn_ns.filedir.file_cmp.file_diff'
        return sf.__lcp_threshold


    @override
    def ___read_rhs_file_metadata___(sf, rhs_root_path, xhs_relative_file_path, /):
        '-> rhs_file_metadata#see: mk_basic_rhs_file_metadata/read_rhs_file_metadata/___read_rhs_file_metadata___/___try_to_get_rhs_file_str_mtime___'
        basic_rhs_file_metadata = sf.mk_basic_rhs_file_metadata(rhs_root_path, xhs_relative_file_path)
        rhs_file_metadata = basic_rhs_file_metadata
        return rhs_file_metadata
    @override
    def ___try_to_get_rhs_file_str_mtime___(sf, rhs_root_path, xhs_relative_file_path, /):
        '-> may_str_mtime #see: mk_basic_rhs_file_metadata/read_rhs_file_metadata/___read_rhs_file_metadata___/___try_to_get_rhs_file_str_mtime___'
        rhs_file_path = rhs_root_path / xhs_relative_file_path
        str_mtime = get_str_mtime4real_fsys(rhs_file_path)
        return str_mtime
#end of class Run_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes__using_file_cmp_file_diff_ver1__using_IRepositorySetting__rhs_is_real_fsys(IRun_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes__using_file_cmp_file_diff_ver1__using_IRepositorySetting):



class Run_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes__using_file_cmp_file_diff_ver1__using_IRepositorySetting__rhs_is_IRepositorySetting(IRun_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes__using_file_cmp_file_diff_ver1__using_IRepositorySetting):
    def __init__(sf, lhs_repository_setting, lhs_branch_name, lhs_may_signed_branch_idx, lhs_relative_path, rhs_repository_setting, rhs_branch_name, rhs_may_signed_branch_idx, rhs_relative_path, /):
        (rhs_dir_viewer, rhs_access_file, _, rhs_branch_idx) = mk_args4dir_cmp__with_IRepositorySetting(rhs_repository_setting, rhs_branch_name, rhs_may_signed_branch_idx, may_working_root_dir_path=None, may_open_ignorefile_text_ifile=None)

        sf.rhs_repository_setting = rhs_repository_setting
        sf.rhs_branch_name = rhs_branch_name
        sf.rhs_branch_idx = rhs_branch_idx

        rhs_root_path = rhs_relative_path
        super().__init__(lhs_repository_setting, lhs_branch_name, lhs_may_signed_branch_idx, lhs_relative_path, rhs_dir_viewer, rhs_access_file, rhs_root_path)


    @override
    def ___read_rhs_file_metadata___(sf, rhs_root_path, xhs_relative_file_path, /):
        '-> rhs_file_metadata#see: mk_basic_rhs_file_metadata/read_rhs_file_metadata/___read_rhs_file_metadata___/___try_to_get_rhs_file_str_mtime___'
        rhs_file_path = rhs_root_path / xhs_relative_file_path
        virtual_file_path = rhs_file_path
        rhs_file_metadata = sf.rhs_access_file.get_metadata(virtual_file_path)
        return rhs_file_metadata
    @override
    def ___try_to_get_rhs_file_str_mtime___(sf, rhs_root_path, xhs_relative_file_path, /):
        '-> may_str_mtime #see: mk_basic_rhs_file_metadata/read_rhs_file_metadata/___read_rhs_file_metadata___/___try_to_get_rhs_file_str_mtime___'
        may_str_mtime = None
        return may_str_mtime
#end of class Run_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes__using_file_cmp_file_diff_ver1__using_IRepositorySetting__rhs_is_IRepositorySetting(IRun_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes__using_file_cmp_file_diff_ver1__using_IRepositorySetting):



def mk_commit_and_push__rhs_is_real_fsys(result_of_dir_cmp__relative, lhs_repository_setting, lhs_branch_name, lhs_may_signed_branch_idx, lhs_relative_path, rhs_root_path, /,*, lcp_threshold):
    sf = Run_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes__using_file_cmp_file_diff_ver1__using_IRepositorySetting__rhs_is_real_fsys(lhs_repository_setting, lhs_branch_name, lhs_may_signed_branch_idx, lhs_relative_path, rhs_root_path, lcp_threshold=lcp_threshold)
    sf.mk_commit_and_push(result_of_dir_cmp__relative)

def mk_commit_and_push__rhs_is_IRepositorySetting(result_of_dir_cmp__relative, lhs_repository_setting, lhs_branch_name, lhs_may_signed_branch_idx, lhs_relative_path, rhs_repository_setting, rhs_branch_name, rhs_may_signed_branch_idx, rhs_relative_path, /):
    sf = Run_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes__using_file_cmp_file_diff_ver1__using_IRepositorySetting__rhs_is_IRepositorySetting(lhs_repository_setting, lhs_branch_name, lhs_may_signed_branch_idx, lhs_relative_path, rhs_repository_setting, rhs_branch_name, rhs_may_signed_branch_idx, rhs_relative_path)
    sf.mk_commit_and_push(result_of_dir_cmp__relative)


def mk_empty_repository_branch(lhs_repository_setting, lhs_branch_name, /):#, lhs_may_signed_branch_idx
    check_instance(IRepositorySetting__using_IFileSystem4update__fsys_delta, lhs_repository_setting)
    if 1:
        #IRepositorySetting__using_IFileSystem4update__fsys_delta.mk_empty_fsys_updater
        branch_name2min_extracting_branch_idx = {}
        fsys_updater = lhs_repository_setting.mk_empty_fsys_updater(branch_name2min_extracting_branch_idx)
        fsys_delta__init_empty_branch = fsys_updater.mk_fsys_delta4init_empty_branch()
        fsys_delta__remove_branch = fsys_updater.mk_fsys_delta4remove_branch()


    if 1:
        #mk branch dir
        lhs_branch_dir = lhs_repository_setting.get_branch_history_dir_path(lhs_branch_name)
        os.makedirs(lhs_branch_dir, exist_ok=True)

        #bug:lhs_branch_sz = lhs_repository_setting.resolve_may_signed_branch_idx(lhs_branch_name, -1/0/xxx) xxx !!!
        lhs_branch_sz = lhs_repository_setting.get_len_inf_dir_of_branch_history(lhs_branch_name)
        if lhs_branch_sz != 0:
            fsys_delta__remove_branch
            raise NotImplementedError(f'branch[{lhs_branch_name!r}] not empty. existed? should check prev fsys_delta is del-cmd')



    #mk/rm order: IRepositorySetting.clean_updating_root_dir
    #IRun_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes__using_IRepositorySetting.finish_visit:: move_cmd_target = 'push_into_command_history'/ move_cmd_target = 'push_into_branch_fsys_history'



    __move_cmds = []
    if 1:
        __file_stack_dir_sz = 0
        lhs_repository_setting.clean_updating_root_dir()
        file_stack_dir_path = lhs_repository_setting.get_file_stack_dir_path()
        os.makedirs(file_stack_dir_path, exist_ok=False)

    #.finish_visit
    if 1:
        #next_branch_time = (lhs_branch_name, lhs_branch_idx+1)
        next_branch_time = (lhs_branch_name, lhs_branch_sz)
        expected_len_inf_dir_of_file_patch_forest = 2 #one for cmd, another for branch[empty]
        high_level_user_command__strs = (f'init_empty_branch[{lhs_branch_name!r}]',)
        command_history_cmd = next_branch_time, expected_len_inf_dir_of_file_patch_forest, high_level_user_command__strs
        #check lhs_branch_idx is latest/correct
        if lhs_branch_sz:
            #bug: empty branch shouldnot use resolve_may_signed_branch_idx
            latest_branch_idx = lhs_repository_setting.resolve_may_signed_branch_idx(lhs_branch_name, -1)
            if not lhs_branch_sz == latest_branch_idx: raise ValueError
        #lhs_branch_sz = lhs_repository_setting.get_len_inf_dir_of_branch_history(lhs_branch_name)

        command_history_cmd
        #fsys_deltas = mk_fsys_deltas(lhs_dst_dir_relative_path4IRepositorySetting, offsetted_fsys_patch_frozendict)
        #fsys_delta = ('mk_empty_fsys',)
        #fsys_delta = ('init_as_empty',)
        fsys_deltas = (fsys_delta__init_empty_branch,)
        check_tuple(fsys_deltas)

        command_history_cmd
        fsys_deltas

        command_history_cmd
        if 1:
            move_cmd_target = 'push_into_command_history'
            move_cmd_target_args = ()
            idx4move_cmd_target = lhs_repository_setting.get_len_inf_dir_of_command_history()
            py_obj = command_history_cmd
            write__binary_ofile__py_obj = lhs_repository_setting.write_command_history_cmd
            __file_stack_dir_sz = _push_store_py_obj_and_mk_move_cmd(lhs_repository_setting, __file_stack_dir_sz, __move_cmds, write__binary_ofile__py_obj=write__binary_ofile__py_obj, py_obj=py_obj, move_cmd_target=move_cmd_target, move_cmd_target_args=move_cmd_target_args, idx4move_cmd_target=idx4move_cmd_target)
            ##

        fsys_deltas
        if 1:
            #should be last push of curr commit
            move_cmd_target = 'push_into_branch_fsys_history'
            move_cmd_target_args = (next_branch_time[0],)
            idx4move_cmd_target = next_branch_time[1]
            py_obj = fsys_deltas
            write__binary_ofile__py_obj = lhs_repository_setting.write_branch_history_deltas
            __file_stack_dir_sz = _push_store_py_obj_and_mk_move_cmd(lhs_repository_setting, __file_stack_dir_sz, __move_cmds, write__binary_ofile__py_obj=write__binary_ofile__py_obj, py_obj=py_obj, move_cmd_target=move_cmd_target, move_cmd_target_args=move_cmd_target_args, idx4move_cmd_target=idx4move_cmd_target)
            ##
        #bug:move_cmds = tuple(__move_cmds)
        move_cmds = tuple(reversed(__move_cmds))
        lhs_repository_setting.check_move_cmds(move_cmds)
        #return move_cmds
    move_cmds

    #.mk_commit
    move_cmds
    if 1:
        #mk TODO_list4move_cmd_file
        lhs_repository_setting.check_move_cmds(move_cmds)
        bfout = io.BytesIO()
        lhs_repository_setting.write_move_cmds(bfout, move_cmds)

        TODO_list4move_cmd_file_path = lhs_repository_setting.get_TODO_list4move_cmd_file_path()
        with open(TODO_list4move_cmd_file_path, 'xb') as binary_ofile:
            #lhs_repository_setting.write_move_cmds(binary_ofile, move_cmds)
            binary_ofile.write(bfout.getvalue())

        #mk commit_completed_file #empty
        commit_completed_file_path = lhs_repository_setting.get_commit_completed_file_path()
        with open(commit_completed_file_path, 'xb') as binary_ofile:
            #close === mk empty file
            pass
        #return
    #.mk_commit_and_push
    if 1:
        lhs_repository_setting.clean_updating_root_dir()
    return
#end of def mk_empty_repository_branch(lhs_repository_setting, lhs_branch_name, /):#, lhs_may_signed_branch_idx

if 1:
    def _push_store_py_obj_and_mk_move_cmd(lhs_repository_setting, __file_stack_dir_sz, __move_cmds, /,*, write__binary_ofile__py_obj, py_obj, move_cmd_target, move_cmd_target_args, idx4move_cmd_target):
        '-> __file_stack_dir_sz'
        (idx4file_stack, binary_ofile), __file_stack_dir_sz = _open_new_file_and_push_into_file_stack_dir(lhs_repository_setting, __file_stack_dir_sz)
        with binary_ofile:
            write__binary_ofile__py_obj(binary_ofile, py_obj)
        move_cmd = (idx4file_stack, move_cmd_target, move_cmd_target_args, idx4move_cmd_target)
        lhs_repository_setting.check_move_cmd(move_cmd)
        __move_cmds.append(move_cmd)
        return __file_stack_dir_sz
    def _open_new_file_and_push_into_file_stack_dir(lhs_repository_setting, __file_stack_dir_sz, /):
        '-> ((idx4file_stack, binary_ofile), __file_stack_dir_sz) #idx4file_stack to mk move_cmd'
        idx4file_stack = __file_stack_dir_sz
        __file_stack_dir_sz += 1
        file_path = lhs_repository_setting.get_file_stack_dir_path() / inf_dir_idx2user_data_relative_path(idx4file_stack, dir_size=lhs_repository_setting.get_dir_size())
        dir_path = file_path.parent
        os.makedirs(dir_path, exist_ok=True)
        binary_ofile = open(file_path, 'xb')
            #shouldnot be "wb" to avoid unclean updating commit: see:IRepositorySetting.clean_updating_root_dir()
        return (idx4file_stack, binary_ofile), __file_stack_dir_sz




def extract_branch(lhs_repository_setting, lhs_branch_name, lhs_branch_idx, rhs_real_fsys_root_dir_path4output, /):
    if not rhs_real_fsys_root_dir_path4output.exists(): raise FileNotFoundError
    if not rhs_real_fsys_root_dir_path4output.is_dir(): raise NotADirectoryError

    may_root_fsys_frozendict = lhs_repository_setting.extract_may_root_fsys_frozendict_at_branch_time({}, lhs_branch_name, lhs_branch_idx)
    if may_root_fsys_frozendict is None: raise ValueError(f'branch[{(lhs_branch_name, lhs_branch_idx)!r} not exists!]')
    lhs_root_fsys_frozendict = may_root_fsys_frozendict

    lhs_may_signed_branch_idx = lhs_branch_idx
    #(rhs_dir_viewer, rhs_access_file, _, rhs_branch_idx) = mk_args4dir_cmp__with_IRepositorySetting(rhs_repository_setting, rhs_branch_name, rhs_may_signed_branch_idx, may_working_root_dir_path=None, may_open_ignorefile_text_ifile=None)
    (lhs_dir_viewer, lhs_access_file, _, lhs_branch_idx) = mk_args4dir_cmp__with_IRepositorySetting(lhs_repository_setting, lhs_branch_name, lhs_may_signed_branch_idx, may_working_root_dir_path=None, may_open_ignorefile_text_ifile=None)


    lhs_root_fsys_frozendict
    lhs_dir_viewer
    lhs_access_file

    lhs_root_path = lhs_relative_path = empty_relative_path
    rhs_root_path = rhs_real_fsys_root_dir_path4output
    existing_dir_pairs = [(lhs_root_path, rhs_root_path)]
    while existing_dir_pairs:
        lhs_dir_path, rhs_dir_path = existing_dir_pairs.pop()
        for basename in lhs_dir_viewer.dir_iter(lhs_dir_path):
            lhs_path = lhs_dir_path / basename
            rhs_path = rhs_dir_path / basename
            if lhs_dir_viewer.is_dir(lhs_path):
                os.mkdir(rhs_path)
                existing_dir_pairs.append((lhs_path, rhs_path))
            else:
                with lhs_access_file.open(lhs_path) as bfin, open(rhs_path, 'xb') as bfout:
                    while 1:
                        bs = bfin.read(BLOCK_SIZE)
                        if not bs: break
                        bfout.write(bs)


    return
#end of def extract_branch(lhs_repository_setting, lhs_branch_name, lhs_branch_idx, rhs_real_fsys_root_dir_path4output, /):





r"""
class IRepositorySetting__user_data_dir_path(ABC):
    def read_metadata(sf, metadata_ifile, /):
    def read_imay_parent_idx(sf, imay_parent_idx_ifile, /):


class IRepositorySetting(IRepositorySetting__working_root_dir_path, IRepositorySetting__repository_root_dir_path, IRepositorySetting__user_data_dir_path):
    def patch_idx2metadata(sf, patch_idx, /):
    def patch_idx2imay_parent_idx(sf, patch_idx, /):
    def patch_idx2user_data_dir_path(sf, patch_idx, /):
    def open_patch_idx_ex(sf, patch_idx, /):
    def move_cmd_target__user_data_file__virtual_name2relative_path_under_user_data_dir(sf, user_data_file__virtual_name, /):
    def read_move_cmds(sf, TODO_list4move_cmd_binary_ifile, /):
    def extract_may_root_fsys_frozendict_at_branch_time(sf, branch_name2min_extracting_branch_idx, branch_name, branch_idx, /):


#"""
