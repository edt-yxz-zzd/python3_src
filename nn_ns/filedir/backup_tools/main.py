
r'''

TODO
    rhs is branch_time/real_path


high_level_user_command:
    * init repository root dir
    * create branch
        * fork from internal
        * init from external
    * delete branch
    * dir_cmp__relative branch_time branch_time/real_path -> result_of_dir_cmp__relative
    * push result_of_dir_cmp__relative branch_time branch_time/real_path
    * fsys ops
        * copy from internal
        * move from internal
        * remove
        * mkdirs
    * extract branch_time

#'''

from nn_ns.filedir.backup_tools.RepositorySetting import RepositorySetting__using_dir_cmp__ignorefile__using_file_cmp__file_patch_ver1__using_IFileSystem4update__fsys_delta_is_branch_history_cmd

from nn_ns.filedir.backup_tools.filedir_cmp_utils__repository__fsys_mapping import dir_cmp__relative__with_IRepositorySetting__rhs_is_real_fsys, mk_commit_and_push__rhs_is_real_fsys
r'''
RepositorySetting__using_dir_cmp__ignorefile__using_file_cmp__file_patch_ver1__using_IFileSystem4update__fsys_delta_is_branch_history_cmd
    def __init__(sf, /,*, min_len_command_history_dir, min_len_file_patch_forest_dir, branch_name2min_len_branch_history_dir, branches_dir_relative_path, ignorefile_relative_path_encoding_pairs, parentfile_relative_path, contentfile_relative_path, metadatafile_relative_path, dir_size, lcp_threshold, repository_root_dir_path, repository_extra_cache_root_dir_path, command_history_dir_relative_path, file_patch_forest_dir_relative_path):

def dir_cmp__relative__with_IRepositorySetting__rhs_is_real_fsys(lhs_repository_setting:IRepositorySetting, lhs_branch_name, lhs_may_signed_branch_idx, lhs_relative_path:'relative PurePosixPath', rhs_path, /,*, kwargs4MkIsSameFile, kwargs4dir_cmp__relative):

def mk_commit_and_push__rhs_is_real_fsys(result_of_dir_cmp__relative, lhs_repository_setting, lhs_branch_name, lhs_may_signed_branch_idx, lhs_relative_path, rhs_root_path, /):
#'''
TODO
    rhs is branch_time/real_path
    ... ...
from
    def repository_root_dir_init(sf, /):
