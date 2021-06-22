
r'''

nn_ns.filedir.backup_tools.main
    see: nn_ns.filedir.backup_tools._test_main
py -m nn_ns.filedir.backup_tools.main
    {init_repository,get_branch_names,get_branch_size,init_branch,cmp_branch_dir,update_branch,extract_branch}                                      ...
py -m unittest nn_ns.filedir.backup_tools._test_main


py -m nn_ns.filedir.backup_tools.main -h
py -m nn_ns.filedir.backup_tools.main init_branch -h

cd /sdcard/0my_files/tmp/for-test/backup_tools/
py -m nn_ns.filedir.backup_tools.main init_repository -cache ./extra -repos ./repos
py -m nn_ns.filedir.backup_tools.main init_branch -cache ./extra -repos ./repos -name master
py -m nn_ns.filedir.backup_tools.main cmp_branch_dir -cache ./extra -repos ./repos -name master -workdir ./src-empty
=====
('master', 0)
=====
[]
=====
[]
=====


touch ./src/empty.txt
py -m nn_ns.filedir.backup_tools.main cmp_branch_dir -cache ./extra -repos ./repos -name master -workdir ./src
=====
('master', 0)
=====
[]
=====
[(1, 'empty.txt')
,]
=====


py -m nn_ns.filedir.backup_tools.main cmp_branch_dir -cache ./extra -repos ./repos -name master -workdir ./src | py -m nn_ns.filedir.backup_tools.main update_branch -cache ./extra -repos ./repos -name master -workdir ./src

py -m nn_ns.filedir.backup_tools.main extract_branch -cache ./extra -repos ./repos -name master -workdir ./src-extract





mkdir ./src/empty_dir/
py -m nn_ns.filedir.backup_tools.main cmp_branch_dir -cache ./extra -repos ./repos -name master -workdir ./src
=====
('master', 1)
=====
[]
=====
[(1, 'empty_dir')
,]
=====


py -m nn_ns.filedir.backup_tools.main cmp_branch_dir -cache ./extra -repos ./repos -name master -workdir ./src | py -m nn_ns.filedir.backup_tools.main update_branch -cache ./extra -repos ./repos -name master -workdir ./src

py -m nn_ns.filedir.backup_tools.main extract_branch -cache ./extra -repos ./repos -name master -workdir ./src-extract


py -m nn_ns.filedir.backup_tools.main cmp_branch_dir -cache ./extra -repos ./repos -name master -workdir ./src

=====
('master', 2)
=====
[]
=====
[]
=====





debug:
    TypeError: Can't instantiate abstract class Run_file_diff_over_result_of_dir_cmp__relative__using_fsys_patch_mapping__using_file_diff__file_bytes__using_file_cmp_file_diff_ver1__using_IRepositorySetting__rhs_is_real_fsys with abstract methods mk_fsys_deltas

    TypeError: Can't instantiate abstract class RepositorySetting__using_dir_cmp__ignorefile__using_file_cmp__file_patch_ver1__using_IFileSystem4update__fsys_delta_is_branch_history_cmd with abstract methods get_TODO_list4move_cmd_file_relative_path, get_commit_completed_file_relative_path, get_file_stack_dir_relative_path, read_imay_parent_idx, read_metadata, write_imay_parent_idx, write_metadata
    cd /sdcard/0my_files/git_repos/python3_src/nn_ns/filedir/backup_tools/
    grep 'def get_file_stack_dir_relative_path' -r .
    grep 'def read_imay_parent_idx' -r .









# copy to python3_src/my_convention/backup_cmds.txt

[[[working_cmds4loop
#################################
#################################
##### working cmds for loop #####
#################################
#################################

=====init-loop-for-src

export src_from=/sdcard/0my_files/git_repos/python3_src/
export src_to=/sdcard/0my_files/my_backup/python3_src/
export tmp=/sdcard/0my_files/tmp/
export src_to4manual=/mnt/m_external_sd/000edt/0my_files/my_backup/python3_src/
export branch_name=my_src


export xxx_from=$src_from
export xxx_to=$src_to
export xxx_to4manual=$src_to4manual
export my_xxx=$branch_name

=====init-loop-for-txt

export txt_from=/sdcard/0my_files/git_repos/txt_phone/txt/
export txt_to=/sdcard/0my_files/my_backup/txt_phone__txt/
export tmp=/sdcard/0my_files/tmp/
export txt_to4manual=/mnt/m_external_sd/000edt/0my_files/my_backup/txt_phone__txt/
export branch_name=my_txt


export xxx_from=$txt_from
export xxx_to=$txt_to
export xxx_to4manual=$txt_to4manual
export my_xxx=$branch_name


=====begin-loop

echo $xxx_from
echo $xxx_to
echo $tmp
echo $xxx_to4manual
echo $my_xxx
cd $tmp/


py -m nn_ns.filedir.backup_tools.main cmp_branch_dir -cache $xxx_to/extra -repos $xxx_to/repos -name $my_xxx -workdir $xxx_from -oX $tmp/$my_xxx/out__result_of_dir_cmp__relative__extended.txt -encoding_ignorefile4workdir :utf8@___ignorefile4dir_cmp___ --mtime_eq_as_same_file -f
view $tmp/$my_xxx/out__result_of_dir_cmp__relative__extended.txt

py -m nn_ns.filedir.backup_tools.main update_branch -cache $xxx_to/extra -repos $xxx_to/repos -name $my_xxx -workdir $xxx_from -iX $tmp/$my_xxx/out__result_of_dir_cmp__relative__extended.txt


py -m nn_ns.filedir.dir_cmp $xxx_to4manual $xxx_to --cmp_fsys_tree_only
py -m nn_ns.filedir.dir_cmp $xxx_to4manual $xxx_to --size_eq_as_same_file

=====end-loop

#################################
#################################
#################################
#################################
#################################
]]]#working_cmds4loop










[[[working_cmds:
#################################
#################################
#####      working cmds     #####
#################################
#################################
=====
python3_src/___ignorefile4dir_cmp___:
=====
-glob:'**/.git/**'
-glob:'**/__pycache__/**'
-glob:'java_src/**/*.class'
-glob:'**/parsetab.py'
-glob:'**/parser.out'
-glob:'**/parser.out/**'
-glob:'**/.mypy_cache'
-glob:'**/.mypy_cache/**'
=====



export src_from=/sdcard/0my_files/git_repos/python3_src/
export src_to=/sdcard/0my_files/my_backup/python3_src/
export tmp=/sdcard/0my_files/tmp/
export src_to4manual=/mnt/m_external_sd/000edt/0my_files/my_backup/python3_src/
    #copy manually, since termux has no write permission

echo $src_from
echo $src_to
echo $tmp
echo $src_to4manual
cd $tmp/
    #proof from misused relative_path

mkdir $src_to
mkdir $tmp/my_src/

py -m nn_ns.filedir.backup_tools.main init_repository -cache $src_to/extra -repos $src_to/repos
py -m nn_ns.filedir.backup_tools.main init_branch -cache $src_to/extra -repos $src_to/repos -name my_src
py -m nn_ns.filedir.backup_tools.main cmp_branch_dir -cache $src_to/extra -repos $src_to/repos -name my_src -workdir $src_from -oX $tmp/my_src/out__result_of_dir_cmp__relative__extended.txt -encoding_ignorefile4workdir :utf8@___ignorefile4dir_cmp___
view $tmp/my_src/out__result_of_dir_cmp__relative__extended.txt

py -m nn_ns.filedir.backup_tools.main update_branch -cache $src_to/extra -repos $src_to/repos -name my_src -workdir $src_from -iX $tmp/my_src/out__result_of_dir_cmp__relative__extended.txt

mkdir $tmp/my_src/extract/
py -m nn_ns.filedir.backup_tools.main extract_branch -cache $src_to/extra -repos $src_to/repos -name my_src -workdir $tmp/my_src/extract/


py -m nn_ns.filedir.dir_cmp $src_from $tmp/my_src/extract/ -ige utf8 -ig $src_from/___ignorefile4dir_cmp___

py -m nn_ns.filedir.dir_cmp $src_to4manual $src_to --size_eq_as_same_file


=====
=====
=====
export txt_from=/sdcard/0my_files/git_repos/txt_phone/txt/
export txt_to=/sdcard/0my_files/my_backup/txt_phone__txt/
export tmp=/sdcard/0my_files/tmp/
export txt_to4manual=/mnt/m_external_sd/000edt/0my_files/my_backup/txt_phone__txt/
    #copy manually, since termux has no write permission

echo $txt_from
echo $txt_to
echo $tmp
echo $txt_to4manual
cd $tmp/
    #proof from misused relative_path

mkdir $txt_to
mkdir $tmp/my_txt/

py -m nn_ns.filedir.backup_tools.main init_repository -cache $txt_to/extra -repos $txt_to/repos
py -m nn_ns.filedir.backup_tools.main init_branch -cache $txt_to/extra -repos $txt_to/repos -name my_txt
py -m nn_ns.filedir.backup_tools.main cmp_branch_dir -cache $txt_to/extra -repos $txt_to/repos -name my_txt -workdir $txt_from -oX $tmp/my_txt/out__result_of_dir_cmp__relative__extended.txt
    #neednot -encoding_ignorefile4workdir :utf8@___ignorefile4dir_cmp___
view $tmp/my_txt/out__result_of_dir_cmp__relative__extended.txt

py -m nn_ns.filedir.backup_tools.main update_branch -cache $txt_to/extra -repos $txt_to/repos -name my_txt -workdir $txt_from -iX $tmp/my_txt/out__result_of_dir_cmp__relative__extended.txt

mkdir $tmp/my_txt/extract/
py -m nn_ns.filedir.backup_tools.main extract_branch -cache $txt_to/extra -repos $txt_to/repos -name my_txt -workdir $tmp/my_txt/extract/


py -m nn_ns.filedir.dir_cmp $txt_from $tmp/my_txt/extract/

py -m nn_ns.filedir.dir_cmp $txt_to4manual $txt_to --size_eq_as_same_file

#################################
#################################
#################################
#################################
#################################
]]]#working_cmds











TODO
    rhs is branch_time|real_path


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
        * mkdirs/makedirs
    * extract branch_time



=====
$

#'''

___begin_mark_of_excluded_global_names__0___ = ...
from nn_ns.filedir.backup_tools.RepositorySetting import RepositorySetting__using_dir_cmp__ignorefile__using_file_cmp__file_patch_ver1__using_IFileSystem4update__fsys_delta_is_branch_history_cmd
if 1:
    from nn_ns.filedir.backup_tools.IRepositorySetting import IRepositorySetting__init_constants__branches_together__cache_min_len_inf_dir__init_caches

from nn_ns.filedir.backup_tools.filedir_cmp_utils__repository__fsys_mapping import dir_cmp__relative__with_IRepositorySetting__rhs_is_real_fsys, mk_commit_and_push__rhs_is_real_fsys, mk_empty_repository_branch, extract_branch
from nn_ns.filedir.relative_path_ops import empty_relative_path, str2relative_path, relative_path2str
from nn_ns.filedir.dir_cmp import inv__path2str4result_of_dir_cmp__relative, path2str4result_of_dir_cmp__relative

from seed.helper.check.checkers import check_uint, check_str
from seed.abc.abc import override
from abc import ABC, abstractmethod
import ast
import re
import os
import io
from pathlib import Path, PurePosixPath
BLOCK_SIZE = 2**16
___end_mark_of_excluded_global_names__0___ = ...

r'''
RepositorySetting__using_dir_cmp__ignorefile__using_file_cmp__file_patch_ver1__using_IFileSystem4update__fsys_delta_is_branch_history_cmd.__init__ is:
class IRepositorySetting__init_constants__branches_together__cache_min_len_inf_dir__init_caches(IRepositorySetting__init_caches, IRepositorySetting__init_constants__branches_together, IRepositorySetting__cache_min_len_inf_dir):
    def __init__(sf, /,*, min_len_command_history_dir, min_len_file_patch_forest_dir, branch_name2min_len_branch_history_dir, branches_dir_relative_path, ignorefile_relative_path_encoding_pairs, parentfile_relative_path, contentfile_relative_path, metadatafile_relative_path, dir_size, lcp_threshold, repository_root_dir_path, repository_extra_cache_root_dir_path, command_history_dir_relative_path, file_patch_forest_dir_relative_path):

def dir_cmp__relative__with_IRepositorySetting__rhs_is_real_fsys(lhs_repository_setting:IRepositorySetting, lhs_branch_name, lhs_may_signed_branch_idx, lhs_relative_path:'relative PurePosixPath', rhs_path, /,*, kwargs4MkIsSameFile, kwargs4dir_cmp__relative):

def mk_commit_and_push__rhs_is_real_fsys(result_of_dir_cmp__relative, lhs_repository_setting, lhs_branch_name, lhs_may_signed_branch_idx, lhs_relative_path, rhs_root_path, /):

def mk_empty_repository_branch(lhs_repository_setting, lhs_branch_name, /):#, lhs_may_signed_branch_idx

def extract_branch(lhs_repository_setting, lhs_branch_name, lhs_branch_idx, rhs_real_fsys_root_dir_path4output, /):

#'''

class IMain4subcmds(ABC):
    @abstractmethod
    def on_init_repository(sf, /,*, lhs_repository_extra_cache_root_dir_path, lhs_repository_root_dir_path):
        '-> None'
    @abstractmethod
    def on_get_branch_names(sf, /,*, lhs_repository_extra_cache_root_dir_path, lhs_repository_root_dir_path):
        '-> [lhs_branch_name]'
    @abstractmethod
    def on_get_branch_size(sf, /,*, lhs_repository_extra_cache_root_dir_path, lhs_repository_root_dir_path, lhs_branch_name):
        '-> lhs_branch_sz #lhs_branch_idx4next==lhs_branch_idx4old+1'
    @abstractmethod
    def on_init_empty_branch(sf, /,*, lhs_repository_extra_cache_root_dir_path, lhs_repository_root_dir_path, lhs_branch_name):
        '-> None'
    @abstractmethod
    def on_dir_cmp__relative(sf, /,*, lhs_repository_extra_cache_root_dir_path, lhs_repository_root_dir_path, lhs_branch_name, rhs_real_fsys_root_dir_path, rhs_ignorefile_relative_path_encoding_pairs, kwargs4MkIsSameFile, kwargs4dir_cmp__relative):
        '-> (lhs_branch_idx4old, result_of_dir_cmp__relative)'
    @abstractmethod
    def on_update_lhs_branch(sf, /,*, lhs_repository_extra_cache_root_dir_path, lhs_repository_root_dir_path, lhs_branch_name, lhs_branch_idx4old, rhs_real_fsys_root_dir_path, rhs_ignorefile_relative_path_encoding_pairs, result_of_dir_cmp__relative, lcp_threshold):
        '-> None'
    @abstractmethod
    def on_extract_lhs_branch(sf, /,*, lhs_repository_extra_cache_root_dir_path, lhs_repository_root_dir_path, lhs_branch_name, lhs_may_signed_branch_idx, rhs_real_fsys_root_dir_path4output):
        '-> None'
class Main4subcmds(IMain4subcmds):
    RepositorySetting = RepositorySetting__using_dir_cmp__ignorefile__using_file_cmp__file_patch_ver1__using_IFileSystem4update__fsys_delta_is_branch_history_cmd
    def mk_lhs_repository_setting(sf, /,*, lhs_repository_extra_cache_root_dir_path, lhs_repository_root_dir_path, rhs_ignorefile_relative_path_encoding_pairs):
        P = Path
        P = PurePosixPath
        lhs_repository_setting = type(sf).RepositorySetting(
                min_len_command_history_dir=0, min_len_file_patch_forest_dir=0, branch_name2min_len_branch_history_dir={}
                , dir_size=10, lcp_threshold=64, repository_root_dir_path=lhs_repository_root_dir_path, repository_extra_cache_root_dir_path=lhs_repository_extra_cache_root_dir_path
                , ignorefile_relative_path_encoding_pairs=rhs_ignorefile_relative_path_encoding_pairs, parentfile_relative_path=P('parent'), contentfile_relative_path=P('content'), metadatafile_relative_path=P('metadata')
                , branches_dir_relative_path=P('grow_only/branches')
                , command_history_dir_relative_path=P('grow_only/command_history'), file_patch_forest_dir_relative_path=P('grow_only/file_patch_forest')
                , file_stack_dir_relative_path=P('updating/file_stack'), TODO_list4move_cmd_file_relative_path=P('updating/TODO_list4move_cmd'), commit_completed_file_relative_path=P('updating/commit_completed')
                )
        return lhs_repository_setting

    @override
    def on_init_repository(sf, /,*, lhs_repository_extra_cache_root_dir_path, lhs_repository_root_dir_path):
        '-> None'
        rhs_ignorefile_relative_path_encoding_pairs = ()
        lhs_repository_setting = sf.mk_lhs_repository_setting(lhs_repository_extra_cache_root_dir_path=lhs_repository_extra_cache_root_dir_path, lhs_repository_root_dir_path=lhs_repository_root_dir_path, rhs_ignorefile_relative_path_encoding_pairs=rhs_ignorefile_relative_path_encoding_pairs)
        paths = [lhs_repository_extra_cache_root_dir_path
                ,lhs_repository_root_dir_path
                ,lhs_repository_setting.get_command_history_dir_path()
                ,lhs_repository_setting.get_file_patch_forest_dir_path()
                ,lhs_repository_root_dir_path / lhs_repository_setting.get_branches_dir_relative_path()
                ]
        for dir_path in paths:
            os.makedirs(dir_path, exist_ok=True)

        return
    @override
    def on_get_branch_names(sf, /,*, lhs_repository_extra_cache_root_dir_path, lhs_repository_root_dir_path):
        '-> [lhs_branch_name]'
        rhs_ignorefile_relative_path_encoding_pairs = ()
        lhs_repository_setting = sf.mk_lhs_repository_setting(lhs_repository_extra_cache_root_dir_path=lhs_repository_extra_cache_root_dir_path, lhs_repository_root_dir_path=lhs_repository_root_dir_path, rhs_ignorefile_relative_path_encoding_pairs=rhs_ignorefile_relative_path_encoding_pairs)
        lhs_branches_dir_path = lhs_repository_root_dir_path / lhs_repository_setting.get_branches_dir_relative_path()
        #bug:basenames = (lhs_branches_dir_path.iterdir())
        child_paths = (lhs_branches_dir_path.iterdir())
        basenames = [child_path.name for child_path in child_paths if child_path.is_dir()]
            #filter dir only?
        basenames.sort()
        return tuple(basenames)
    @override
    def on_get_branch_size(sf, /,*, lhs_repository_extra_cache_root_dir_path, lhs_repository_root_dir_path, lhs_branch_name):
        '-> lhs_branch_sz #lhs_branch_idx4next==lhs_branch_idx4old+1'
        rhs_ignorefile_relative_path_encoding_pairs = ()
        lhs_repository_setting = sf.mk_lhs_repository_setting(lhs_repository_extra_cache_root_dir_path=lhs_repository_extra_cache_root_dir_path, lhs_repository_root_dir_path=lhs_repository_root_dir_path, rhs_ignorefile_relative_path_encoding_pairs=rhs_ignorefile_relative_path_encoding_pairs)
        #lhs_may_signed_branch_idx = -1
        #bug:lhs_branch_idx = lhs_repository_setting.resolve_may_signed_branch_idx(lhs_branch_name, lhs_may_signed_branch_idx)
        lhs_branch_sz = lhs_repository_setting.get_len_inf_dir_of_branch_history(lhs_branch_name)
        return lhs_branch_sz

    @override
    def on_init_empty_branch(sf, /,*, lhs_repository_extra_cache_root_dir_path, lhs_repository_root_dir_path, lhs_branch_name):
        '-> None'
        rhs_ignorefile_relative_path_encoding_pairs = ()
        lhs_repository_setting = sf.mk_lhs_repository_setting(lhs_repository_extra_cache_root_dir_path=lhs_repository_extra_cache_root_dir_path, lhs_repository_root_dir_path=lhs_repository_root_dir_path, rhs_ignorefile_relative_path_encoding_pairs=rhs_ignorefile_relative_path_encoding_pairs)
        mk_empty_repository_branch(lhs_repository_setting, lhs_branch_name)
        return

    @override
    def on_dir_cmp__relative(sf, /,*, lhs_repository_extra_cache_root_dir_path, lhs_repository_root_dir_path, lhs_branch_name, rhs_real_fsys_root_dir_path, rhs_ignorefile_relative_path_encoding_pairs, kwargs4MkIsSameFile, kwargs4dir_cmp__relative):
        '-> (lhs_branch_idx4old, result_of_dir_cmp__relative)'
        lhs_repository_setting = sf.mk_lhs_repository_setting(lhs_repository_extra_cache_root_dir_path=lhs_repository_extra_cache_root_dir_path, lhs_repository_root_dir_path=lhs_repository_root_dir_path, rhs_ignorefile_relative_path_encoding_pairs=rhs_ignorefile_relative_path_encoding_pairs)

        #branch_idx = repository_setting.resolve_may_signed_branch_idx(branch_name, may_signed_branch_idx)
        lhs_may_signed_branch_idx = -1
        lhs_branch_idx = lhs_repository_setting.resolve_may_signed_branch_idx(lhs_branch_name, lhs_may_signed_branch_idx)
        lhs_relative_path = empty_relative_path #'.'
        rhs_path = rhs_real_fsys_root_dir_path
        result_of_dir_cmp__relative = dir_cmp__relative__with_IRepositorySetting__rhs_is_real_fsys(lhs_repository_setting, lhs_branch_name, lhs_may_signed_branch_idx, lhs_relative_path, rhs_path, kwargs4MkIsSameFile=kwargs4MkIsSameFile, kwargs4dir_cmp__relative=kwargs4dir_cmp__relative)
        return lhs_branch_idx, result_of_dir_cmp__relative

    @override
    def on_update_lhs_branch(sf, /,*, lhs_repository_extra_cache_root_dir_path, lhs_repository_root_dir_path, lhs_branch_name, lhs_branch_idx4old, rhs_real_fsys_root_dir_path, rhs_ignorefile_relative_path_encoding_pairs, result_of_dir_cmp__relative, lcp_threshold):
        '-> None'
        lhs_repository_setting = sf.mk_lhs_repository_setting(lhs_repository_extra_cache_root_dir_path=lhs_repository_extra_cache_root_dir_path, lhs_repository_root_dir_path=lhs_repository_root_dir_path, rhs_ignorefile_relative_path_encoding_pairs=rhs_ignorefile_relative_path_encoding_pairs)
        lhs_may_signed_branch_idx = lhs_branch_idx4old
        lhs_relative_path = empty_relative_path #'.'
        rhs_root_path = rhs_real_fsys_root_dir_path
        mk_commit_and_push__rhs_is_real_fsys(result_of_dir_cmp__relative, lhs_repository_setting, lhs_branch_name, lhs_may_signed_branch_idx, lhs_relative_path, rhs_root_path, lcp_threshold=lcp_threshold)
        return

    @override
    def on_extract_lhs_branch(sf, /,*, lhs_repository_extra_cache_root_dir_path, lhs_repository_root_dir_path, lhs_branch_name, lhs_may_signed_branch_idx, rhs_real_fsys_root_dir_path4output):
        '-> None'
        rhs_ignorefile_relative_path_encoding_pairs = ()
        lhs_repository_setting = sf.mk_lhs_repository_setting(lhs_repository_extra_cache_root_dir_path=lhs_repository_extra_cache_root_dir_path, lhs_repository_root_dir_path=lhs_repository_root_dir_path, rhs_ignorefile_relative_path_encoding_pairs=rhs_ignorefile_relative_path_encoding_pairs)
        lhs_branch_idx = lhs_repository_setting.resolve_may_signed_branch_idx(lhs_branch_name, lhs_may_signed_branch_idx)
            #signed_branch_idx
            #lhs_branch_idx
        if 0:#[01_to_turn_off]
            print(fr'lhs_branch_idx={lhs_branch_idx}')
            print(fr'rhs_real_fsys_root_dir_path4output={rhs_real_fsys_root_dir_path4output}')

        extract_branch(lhs_repository_setting, lhs_branch_name, lhs_branch_idx, rhs_real_fsys_root_dir_path4output)
        return


r'''
TODO
    rhs is branch_time/real_path
    ... ...
from
    def repository_root_dir_init(sf, /):

#'''


















































#_decode_str2pair
_line_sep = '====='
def _pairs__str2rpath(rhs_ignorefile_relative_path_encoding_pairs__str):
    # vs str2rpath_encoding_pair
    '[(str, encoding)] -> tuple<(PurePosixPath, encoding)>'
    S2RP = str2relative_path
    assert type(rhs_ignorefile_relative_path_encoding_pairs__str) is list
    rhs_ignorefile_relative_path_encoding_pairs__rpath = tuple((S2RP(s), e) for s, e in rhs_ignorefile_relative_path_encoding_pairs__str)
    return rhs_ignorefile_relative_path_encoding_pairs__rpath
def _pairs__rpath2str(rhs_ignorefile_relative_path_encoding_pairs__rpath):
    'tuple<(PurePosixPath, encoding)> -> [(str, encoding)]'
    assert type(rhs_ignorefile_relative_path_encoding_pairs__rpath) is tuple
    RP2S = relative_path2str
    rhs_ignorefile_relative_path_encoding_pairs__str = [(RP2S(p), e) for p, e in rhs_ignorefile_relative_path_encoding_pairs__rpath]
    return rhs_ignorefile_relative_path_encoding_pairs__str

def write__file4result_of_dir_cmp__relative__extended(fout, lhs_branch_name, lhs_branch_idx4old, rhs_ignorefile_relative_path_encoding_pairs, result_of_dir_cmp__relative):
    #see:[location4fmt_of_file4result_of_dir_cmp__relative__extended]
    saved_fout = fout
    fout = io.StringIO()
    begin = fout.tell()
    result_of_dir_cmp__relative = list(result_of_dir_cmp__relative)
    ###################
    ###################
    ###################

    from seed.tiny import mk_fprint
    fprint = mk_fprint(fout)

    fprint(_line_sep)
    if 1:
        fprint(f'{(lhs_branch_name, lhs_branch_idx4old)!r}')
    fprint(_line_sep)
    if 1:
        fprint(f'{_pairs__rpath2str(rhs_ignorefile_relative_path_encoding_pairs)!r}')
    fprint(_line_sep)
    if 1:
        fprint('[', end='')
        for case, relative_path__str in path2str4result_of_dir_cmp__relative(result_of_dir_cmp__relative):
            fprint(f'{(case, relative_path__str)!r}\n,', end='')
        fprint(']')
    fprint(_line_sep)

    ###################
    ###################
    ###################
    s = fout.getvalue()
    fout.seek(begin); fin = fout; del fout
    #print(lhs_branch_name, lhs_branch_idx4old, rhs_ignorefile_relative_path_encoding_pairs, result_of_dir_cmp__relative)
    #print(read__file4result_of_dir_cmp__relative__extended(fin))
    t = read__file4result_of_dir_cmp__relative__extended(fin)
    t = (*t[:-1], list(t[-1]))
    if (lhs_branch_name, lhs_branch_idx4old, rhs_ignorefile_relative_path_encoding_pairs, result_of_dir_cmp__relative) != t: raise logic-err
    if s != fin.getvalue(): raise logic-err
    saved_fout.write(s)
    return
def read__file4result_of_dir_cmp__relative__extended(fin):
    '-> (lhs_branch_name, lhs_branch_idx4old, rhs_ignorefile_relative_path_encoding_pairs, result_of_dir_cmp__relative)'
    #see:[location4fmt_of_file4result_of_dir_cmp__relative__extended]
    newline = '\n'
    txt = fin.read()
    if not txt.startswith(_line_sep+newline): raise ValueError
    if not txt.endswith(newline+_line_sep+newline): raise ValueError
    _txt_ = txt[len(_line_sep+newline):-len(newline+_line_sep+newline)]
    ls = _txt_.split(newline+_line_sep+newline)
    if len(ls) != 3: raise ValueError
    lhs_branch_time, rhs_ignorefile_relative_path_encoding_pairs__str, result_of_dir_cmp__relative__str = map(ast.literal_eval, ls)

    lhs_branch_name, lhs_branch_idx4old = lhs_branch_time
    check_str(lhs_branch_name)
    check_uint(lhs_branch_idx4old)

    rhs_ignorefile_relative_path_encoding_pairs__str
    rhs_ignorefile_relative_path_encoding_pairs = _pairs__str2rpath(rhs_ignorefile_relative_path_encoding_pairs__str)

    result_of_dir_cmp__relative = inv__path2str4result_of_dir_cmp__relative(result_of_dir_cmp__relative__str)
    #result_of_dir_cmp__relative = list(result_of_dir_cmp__relative)
    return (lhs_branch_name, lhs_branch_idx4old, rhs_ignorefile_relative_path_encoding_pairs, result_of_dir_cmp__relative)

def str2rpath_encoding_pair(s):
    #see:pairs_option
    '[str] -> tuple<(PurePosixPath, encoding)>'
    #_decode_str2pair
    m = re.fullmatch('^:(?P<encoding>[^@]+)@(?P<relative_path__str>.+)$', s)
    if not m: raise ValueError(f'bad fmt for encoding+relative_path__str:fmt=":{{encoding}}@{{ignorefile}}" : input={s!r}')
    encoding = m['encoding']
    relative_path__str = m['relative_path__str']
    relative_path = str2relative_path(relative_path__str)
    return relative_path, encoding
class _Main:
    if 1:
        _main4subcmds = Main4subcmds()
        'on_init_repository on_get_branch_names on_get_branch_size on_init_empty_branch on_dir_cmp__relative on_update_lhs_branch on_extract_lhs_branch'
    if 1:
        'init_repository get_branch_names get_branch_size init_branch cmp_branch_dir update_branch extract_branch'
    if 1:
        #[location4fmt_of_file4result_of_dir_cmp__relative__extended]
        _help_tail = r'''
=======
    result_of_dir_cmp__relative+lhs_branch_name+lhs_branch_idx4old+rhs_ignorefile_relative_path_encoding_pairs
    fmt of file4result_of_dir_cmp__relative__extended
        =====
        {(lhs_branch_name, lhs_branch_idx4old)!r}
        =====
        {[(p, e) for p, e in rhs_ignorefile_relative_path_encoding_pairs]!r}
        =====
        {result_of_dir_cmp__relative!list}
        #'''

    def on_subcmd__init_repository(sf, subcmd_name, parsed_args):
        type(sf)._main4subcmds.on_init_repository(lhs_repository_extra_cache_root_dir_path=parsed_args.lhs_repository_extra_cache_root_dir_path, lhs_repository_root_dir_path=parsed_args.lhs_repository_root_dir_path)
        return
    def on_subcmd__get_branch_names(sf, subcmd_name, parsed_args):
        lhs_branch_names = type(sf)._main4subcmds.on_get_branch_names(lhs_repository_extra_cache_root_dir_path=parsed_args.lhs_repository_extra_cache_root_dir_path, lhs_repository_root_dir_path=parsed_args.lhs_repository_root_dir_path)

        #print(lhs_branch_names)
        parsed_args.output
        from seed.io.may_open import may_open_stdin, may_open_stdout
        may_ofname = parsed_args.output
        encoding = parsed_args.encoding
        omode = 'wt' if parsed_args.force else 'xt'
        with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
            print(lhs_branch_names, file=fout)
        return
    def on_subcmd__get_branch_size(sf, subcmd_name, parsed_args):
        lhs_branch_sz = type(sf)._main4subcmds.on_get_branch_size(lhs_repository_extra_cache_root_dir_path=parsed_args.lhs_repository_extra_cache_root_dir_path, lhs_repository_root_dir_path=parsed_args.lhs_repository_root_dir_path, lhs_branch_name=parsed_args.lhs_branch_name)

        #print(lhs_branch_sz)
        parsed_args.output
        from seed.io.may_open import may_open_stdin, may_open_stdout
        may_ofname = parsed_args.output
        encoding = parsed_args.encoding
        omode = 'wt' if parsed_args.force else 'xt'
        with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
            print(lhs_branch_sz, file=fout)
        return
    def on_subcmd__init_branch(sf, subcmd_name, parsed_args):
        type(sf)._main4subcmds.on_init_empty_branch(lhs_repository_extra_cache_root_dir_path=parsed_args.lhs_repository_extra_cache_root_dir_path, lhs_repository_root_dir_path=parsed_args.lhs_repository_root_dir_path, lhs_branch_name=parsed_args.lhs_branch_name)
        return
    def on_subcmd__cmp_branch_dir(sf, subcmd_name, parsed_args):
        #see:[location4setting4the_two_kwargs]
        #always_tribool_as_is_or_not_same_file
        #bug:PP = _pairs__str2rpath
        #   see:str2rpath_encoding_pair
        #
        PP = tuple

        kwargs4MkIsSameFile = dict(
            always_tribool_as_is_or_not_same_file=ast.literal_eval(parsed_args.always_tribool_as_is_or_not_same_file)
            , size_hash0_eq_as_same_file=parsed_args.size_hash0_eq_as_same_file
            , mtime_eq_as_same_file=parsed_args.mtime_eq_as_same_file
            , imay_max_size_threshold4cmp_content=parsed_args.imay_max_size_threshold4cmp_content
            ###########
            , size_eq_as_same_file=False
            , hash_eq_as_same_file=False
            , mtime_ne_as_not_same_file=False
            , _block_size=BLOCK_SIZE
            )
        kwargs4dir_cmp__relative = dict(
            ignore_basename=None
            , max_depth=None
            )
        (lhs_branch_idx4old, result_of_dir_cmp__relative) = type(sf)._main4subcmds.on_dir_cmp__relative(lhs_repository_extra_cache_root_dir_path=parsed_args.lhs_repository_extra_cache_root_dir_path, lhs_repository_root_dir_path=parsed_args.lhs_repository_root_dir_path, lhs_branch_name=parsed_args.lhs_branch_name, rhs_real_fsys_root_dir_path=parsed_args.rhs_real_fsys_root_dir_path, rhs_ignorefile_relative_path_encoding_pairs=PP(parsed_args.rhs_ignorefile_relative_path_encoding_pairs), kwargs4MkIsSameFile=kwargs4MkIsSameFile, kwargs4dir_cmp__relative=kwargs4dir_cmp__relative)

        parsed_args.output
        from seed.io.may_open import may_open_stdin, may_open_stdout
        may_ofname = parsed_args.output
        encoding = parsed_args.encoding
        omode = 'wt' if parsed_args.force else 'xt'
        with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
            #see:[location4fmt_of_file4result_of_dir_cmp__relative__extended]
            write__file4result_of_dir_cmp__relative__extended(fout, parsed_args.lhs_branch_name, lhs_branch_idx4old, PP(parsed_args.rhs_ignorefile_relative_path_encoding_pairs), result_of_dir_cmp__relative)
        return

    def on_subcmd__update_branch(sf, subcmd_name, parsed_args):
        parsed_args.input
        from seed.io.may_open import may_open_stdin, may_open_stdout
        may_ifname = parsed_args.input
        encoding = parsed_args.encoding
        with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:
            #see:[location4fmt_of_file4result_of_dir_cmp__relative__extended]
            (lhs_branch_name, lhs_branch_idx4old, rhs_ignorefile_relative_path_encoding_pairs, result_of_dir_cmp__relative) = read__file4result_of_dir_cmp__relative__extended(fin)
        #options_update_branch
        if lhs_branch_name != parsed_args.lhs_branch_name: raise ValueError
        #if lhs_branch_idx4old != parsed_args.lhs_branch_idx: raise ValueError

        type(sf)._main4subcmds.on_update_lhs_branch(lhs_repository_extra_cache_root_dir_path=parsed_args.lhs_repository_extra_cache_root_dir_path, lhs_repository_root_dir_path=parsed_args.lhs_repository_root_dir_path, lhs_branch_name=lhs_branch_name, lhs_branch_idx4old=lhs_branch_idx4old, rhs_real_fsys_root_dir_path=parsed_args.rhs_real_fsys_root_dir_path, rhs_ignorefile_relative_path_encoding_pairs=rhs_ignorefile_relative_path_encoding_pairs, result_of_dir_cmp__relative=result_of_dir_cmp__relative, lcp_threshold=parsed_args.lcp_threshold)
        return
    def on_subcmd__extract_branch(sf, subcmd_name, parsed_args):
        type(sf)._main4subcmds.on_extract_lhs_branch(lhs_repository_extra_cache_root_dir_path=parsed_args.lhs_repository_extra_cache_root_dir_path, lhs_repository_root_dir_path=parsed_args.lhs_repository_root_dir_path, lhs_branch_name=parsed_args.lhs_branch_name, lhs_may_signed_branch_idx=parsed_args.lhs_may_signed_branch_idx, rhs_real_fsys_root_dir_path4output=parsed_args.rhs_real_fsys_root_dir_path)
        return
    def on_no_subcmd(sf, subcmd_name, parsed_args):
        sf.parser.print_help()
        print(sf._help_tail)
        quit()
        raise NotImplementedError
    @classmethod
    def _mk_option_config_(cls):
        '-> ([parent::ArgParserPrepare], [common_option::GetArgsKwargs], {group_name:{subcmd:ArgParserPrepare}})'
        #return [], [], {'subcmd':_mk_subcmd2prepare()}

        #below copy from seed.for_libs.for_argparse.subcmd
        Get, Pack = cls.Get, cls.Pack

        'on_init_repository on_get_branch_names on_get_branch_size on_init_empty_branch on_dir_cmp__relative on_update_lhs_branch on_extract_lhs_branch'
        'init_repository get_branch_names get_branch_size init_branch cmp_branch_dir update_branch extract_branch'
        common_options = (
    [Get('-cache', '--lhs_repository_extra_cache_root_dir_path', type=Path, required=True, help='dir path for extra metadata(e.g. multi-mtime for kwargs4MkIsSameFile::mtime_eq_as_same_file), tmp file...')
    ,Get('-repos', '--lhs_repository_root_dir_path', type=Path, required=True, help='dir path for repository data')
    ,Get('-name', '--lhs_branch_name', type=str, required=True, help='branch name')
        ])

        #branch_idx_option = Get('-idx', '--lhs_branch_idx', type=int, required=True, help='branch idx to extract')
        branch_idx_option = Get('-idx', '--lhs_may_signed_branch_idx', type=int, required=False, default=-1, help='branch idx to extract')
        lcp_threshold_option = Get('--lcp_threshold', type=int, required=False, default=64, help='lcp_threshold@nn_ns.filedir.file_cmp.file_diff; lcp_threshold>=1')
        workdir_option = Get('-workdir', '--rhs_real_fsys_root_dir_path', type=Path, required=True, help='dir path for working data')

        pairs_option=Get('-encoding_ignorefile4workdir', '--rhs_ignorefile_relative_path_encoding_pairs', type=str2rpath_encoding_pair, nargs='+', default=[], help='encoding and ignorefile path relative to working dir; fmt=":{encoding}@{ignorefile}"')#, action='append'
            #see:str2rpath_encoding_pair
        ioX_encoding_option = Get('-e', '--encoding', type=str, default='utf8', help='input/output file encoding for result_of_dir_cmp__relative+lhs_branch_name+lhs_branch_idx4old+rhs_ignorefile_relative_path_encoding_pairs')
        inputX_option = Get('-iX', '--input', type=str, default=None, help='input file path for result_of_dir_cmp__relative+lhs_branch_name+lhs_branch_idx4old+rhs_ignorefile_relative_path_encoding_pairs')
        forceX_option = Get('-f', '--force', action='store_true', default = False, required=False, help='open mode for output file for result_of_dir_cmp__relative+lhs_branch_name+lhs_branch_idx4old+rhs_ignorefile_relative_path_encoding_pairs')
        outputX_option = Get('-oX', '--output', type=str, default=None, help='output file path for result_of_dir_cmp__relative+lhs_branch_name+lhs_branch_idx4old+rhs_ignorefile_relative_path_encoding_pairs')
        oV_encoding_option = Get('-e', '--encoding', type=str, default='utf8', help='output file encoding for STDOUT')
        forceV_option = Get('-f', '--force', action='store_true', default = False, required=False, help='open mode for output file for STDOUT')
        outputV_option = Get('-oV', '--output', type=str, default=None, help='output file path for STDOUT')

        #################################
        #################################
        options_init_repository = (
    [*common_options[:-1]
        ])
        options_get_branch_names = (
    [*common_options[:-1]
    ,oV_encoding_option
    ,forceV_option
    ,outputV_option
        ])
        options_get_branch_size = (
    [*common_options
    ,oV_encoding_option
    ,forceV_option
    ,outputV_option
        ])

        options_init_branch = (
    [*common_options
        ])

        r'''
    #[location4setting4the_two_kwargs]
    kwargs4dir_cmp__relative
        (none...)
        ===
        #except:ignore_relative_path
        ignore_basename, max_depth
    kwargs4MkIsSameFile
        always_tribool_as_is_or_not_same_file
        size_hash0_eq_as_same_file
        mtime_eq_as_same_file
        imay_max_size_threshold4cmp_content
        ===
        always_tribool_as_is_or_not_same_file:'tribool', size_eq_as_same_file:bool, size_hash0_eq_as_same_file:bool, hash_eq_as_same_file:bool, mtime_eq_as_same_file:bool, mtime_ne_as_not_same_file:bool, imay_max_size_threshold4cmp_content:int, _block_size
        #'''
        options_cmp_branch_dir = (
    [*common_options
    ,workdir_option
    ,pairs_option
    #outfile4result_of_dir_cmp__relative__extended
    ,outputX_option
    ,forceX_option
    ,ioX_encoding_option
    ####
    #below for kwargs4MkIsSameFile,kwargs4dir_cmp__relative... ...
    ,Get('--size_hash0_eq_as_same_file', action='store_true', default = False, required=False, help='kwargs4MkIsSameFile::size_hash0_eq_as_same_file')
    ,Get('--mtime_eq_as_same_file', action='store_true', default = False, required=False, help='kwargs4MkIsSameFile::mtime_eq_as_same_file')
    ,Get('--imay_max_size_threshold4cmp_content', type=int, default = -1, required=False, help='kwargs4MkIsSameFile::imay_max_size_threshold4cmp_content')
    ,Get('--always_tribool_as_is_or_not_same_file', choices='True ... False'.split(), default = '...', required=False, help='kwargs4MkIsSameFile::imay_max_size_threshold4cmp_content')
        ])

        options_update_branch = (
    [*common_options
    #,branch_idx_option
    ,workdir_option
    ,inputX_option
    ,ioX_encoding_option
    ,lcp_threshold_option
        ])

        options_extract_branch = (
    [*common_options
    ,branch_idx_option
    ,workdir_option
        ])



        prepare_init_repository = Pack([], options_init_repository, {})
        prepare_get_branch_names = Pack([], options_get_branch_names, {})
        prepare_get_branch_size = Pack([], options_get_branch_size, {})
        prepare_init_branch = Pack([], options_init_branch, {})
        prepare_cmp_branch_dir = Pack([], options_cmp_branch_dir, {})
        prepare_update_branch = Pack([], options_update_branch, {})
        prepare_extract_branch = Pack([], options_extract_branch, {})

        subcmd2prepare_GROUP_A = (dict
            (init_repository=prepare_init_repository
            ,get_branch_names=prepare_get_branch_names
            ,get_branch_size=prepare_get_branch_size
            ,init_branch=prepare_init_branch
            ,cmp_branch_dir=prepare_cmp_branch_dir
            ,update_branch=prepare_update_branch
            ,extract_branch=prepare_extract_branch
            ))
        group_name2subcmd2prepare = (dict
            (GROUP_A=subcmd2prepare_GROUP_A
            ))
        return [], [], group_name2subcmd2prepare
def main(args=None):
    from seed.for_libs.for_argparse.subcmd import Main4subcmd
    class Main(_Main, Main4subcmd):
        pass
    return Main(description='backup via growingonly repository for manually copy directly', subcmd_dest_name='subcmd').main(args)
if __name__ == "__main__":
    main()



