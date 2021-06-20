r'''
search:
    copy...dict
        copy_fsys_dict
        copy_fsys_dict_or_patch_idx
    inplace

    get_tmay_sub_fsys_dict_or_patch_idx
        -->> get_tmay_sub_fsys_mapping_or_patch_idx
    .get_tmay_sub_fsys_dict_or_patch_idx_from_internal
        -->> .get_tmay_sub_fsys_frozendict_or_patch_idx_from_internal

    cd_to_sub_fsys_dict_or_patch_idx_ex_as_deep_as_possible
        -->> cd_to_sub_fsys_mapping_or_patch_idx_ex_as_deep_as_possible
        -->> cd_to_sub_fsys_mapping_ex_or_pseudo_virtual_file_reprobj_as_deep_as_possible_ex
    extract_may_root_fsys_dict_at_branch_time
        -->> extract_may_root_fsys_frozendict_at_branch_time



=======

    , check_cmd
    , IFileSystem4update__fsys_delta
    , IFileSystem4update__fsys_delta_is_cmd
    , FileSystem4update__fsys_delta_is_fsys_update_cmd
    , FileSystem4update__fsys_delta_is_branch_history_cmd
=======






#'''


__all__ = '''
    echo_valueonly_fsys_mapping_or_patch_idx
    echo_valueonly_fsys_mapping
    check_cmd
    IFileSystem4update__fsys_delta
    IFileSystem4update__fsys_delta_is_cmd
    mk_check_cmd_ex
    check_cmd_checker_table
    checker4relative_paths__ge2
    checker4relative_paths__ge1
    checker4uint_mod_8
    checker4fsys_frozendict
    checker4fsys_patch_frozendict
    checker4fsys_frozendict_or_patch_idx
    checker4branch_name
    checker4branch_idx
    checker4patch_idx
    checker4relative_path
    FileSystem4update__fsys_delta_is_fsys_update_cmd
    FileSystem4update__fsys_delta_is_branch_history_cmd
    '''.split()


___begin_mark_of_excluded_global_names__0___ = ...

from nn_ns.filedir.backup_tools.IRepositorySetting import IRepositorySetting, read_repred_py_obj, write_py_obj_as_repr, check_branch_name
from nn_ns.filedir.backup_tools.fsys_mapping_ex import using_FrozenDict_as_valueonly_fsys_mapping_ex, get_tmay_sub_fsys_mapping_or_patch_idx, check_fsys_frozendict, check_fsys_patch_frozendict, cd_to_sub_fsys_mapping_ex_or_pseudo_virtual_file_reprobj_as_deep_as_possible_ex, check_valueonly_fsys_mapping_or_patch_idx, mkdirs4valueonly_fsys_mapping_ex, deepcopy_fsys_frozendict_ex_as_fsys_dict_ex, deepcopy_fsys_dict_ex_as_fsys_frozendict_ex
    #, check_valueonly_fsys_patch_mapping, check_fsys_mapping, check_valueonly_fsys_mapping, Visit__fsys_patch_mapping, check_fsys_frozendict
from nn_ns.filedir.backup_tools.fsys_mapping_patch import fsys_frozendict_or_patch_idx_merge, fsys_frozendict_patch, merge_case2skip_or_replace_ops, offsetted_fsys_frozendict_patch

from nn_ns.filedir.relative_path_ops import relative_path2parts, is_relative_path_empty, parts2relative_path, check_relative_path, str2relative_path, relative_path2str

from collections.abc import Mapping
from abc import ABC, abstractmethod
from seed.abc.abc import override
from seed.seq_tools.is_prefix_of_seq import is_prefix_of_seq
from seed.helper.check.checkers import check_tmay, check_bool, check_tuple, check_uint, check_int, check_all

from seed.types.FrozenDict import FrozenDict
from seed.tiny import echo


from pathlib import PurePosixPath


if not using_FrozenDict_as_valueonly_fsys_mapping_ex:
    r'''
    from .somewhere import mk_fsys_mapping_view, deepcopy_fsys_mapping_as_fsys_dict
if 0:
    from .nowhere import shouldnot, neednot
    #'''
___end_mark_of_excluded_global_names__0___ = ...

if using_FrozenDict_as_valueonly_fsys_mapping_ex:
    echo_valueonly_fsys_mapping_or_patch_idx = echo
    echo_valueonly_fsys_mapping = echo




def check_cmd(cmd, /):
    if not type(cmd) is tuple: raise TypeError
    if not cmd: raise TypeError
    if not type(cmd[0]) is str: raise TypeError

#HHHHH
class IFileSystem4update__fsys_delta(ABC):
    r'''
    here set/config:
        branch_history_delta@IRepositorySetting := fsys_delta@IFileSystem4update__fsys_delta

    [outdated]:
        once assume underlying obj is fsys_dict, patch/merge inplace
        now FrozenDict, not inplace

    [outdated]:
        # below are outdated by IRepositorySetting+branch_name2min_extracting_branch_idx
        # now use fsys_update_cmd, branch_history_cmd both
        #
        once let fsys patch_file_bytes be branch_history_cmd, but too hard to impl exec_branch_history_cmd / fsys_patch, since 'init_via_branch' requres many settings
            now fsys patch_file_bytes != branch_history_cmd
            remove exec_branch_history_cmd(sf, branch_history_cmd)

    implicit args:
        #command_history: each cmd should contains these args explicitly
        #   command_history_cmd = (this_branch_name, curr_branch_idx) branch_history_cmd
        #       -->> command_history_cmd = next_branch_time, expected_len_inf_dir_of_file_patch_forest, high_level_user_command__strs
        #branch_history: each cmd not contains these args explicitly
        #   branch_history_cmd = (op, ...)
        this_branch_name
        curr_branch_idx <- [0..]
            not exist yet
            after success exec any cmd
            curr_branch_idx save the cmd


branch_time = (branch_name, branch_idx)
command_history_cmd
    #ver4:
    = (new branch_time, new len_inf_dir_of_file_patch_forest, [high_level_user_command__str])
    #ver3:
    #   should store high level user command to examine low level fsys_deltas correctness for debugging
    #       high_level_user_command = dir_cmp | copy_from_internal | move_from_internal | remove | ...
    = (new branch_time, [high_level_user_command__str])
    #ver2:
    #   since data i.e. original_file_bytes/patch_file_bytes are stored in file_patch_forest_dir
    #       fsys_deltas are stored in branch_history_dir<branch_name>
    #   ==>> command_history_dir neednot store any data/fsys_deltas, but only to maintain the order of create time of branch_time of all branch_name
    = branch_time
    = (branch_name, branch_idx)
    #ver1:
    #   NOTE: branch_time is after fsys_deltas be applied
    #       branch_time <- exec(may prev branch_time, fsys_deltas)
    #
    = (branch_time, fsys_deltas)
    = ((branch_name, branch_idx), [fsys_delta]::tuple<fsys_delta>)
fsys_delta = fsys_update_cmd | branch_history_cmd
    add mk_empty_fsys/init_as_empty to impl new_fsys/init_via_copy#except:init_via_branch

fsys_update_cmd:
    #bad: data fsys_frozendict/fsys_patch_frozendict is too big when impl branch_history_cmd::init_via_branch/merge_from_internal/copy_from_internal
    #       ???keep big to seperate branches???
    #           !!! not a delta repository impl !!!
    ('new_fsys', fsys_frozendict)
    ('mk_empty_fsys',)
    ('del_fsys',)
    ('update_fsys', dst_dir_relative_path, offsetted_fsys_patch_frozendict)
branch_history_cmd:
    # new ver:[not cancelled, since to vivi is complicate]
    #   #cancel? this new version! since "remove"/None+"copy_from_internal"/relative_path+"copy_from_external"#???"merge_from_internal"+"merge_from_external"!!!
    #   add cmd "update_fsys" as @fsys_update_cmd to merge the 2 cmd set
    #   rename cmd "patch" to "update_file"
    ##
    #bad: too hard to impl init_via_branch/merge_from_internal/copy_from_internal
    #       solved: now add IRepositorySetting to support
    ('init_via_copy', src_fsys_frozendict)
    ('init_via_branch', src_branch_name, src_branch_idx)
    ('init_as_empty',)
    ('del_branch',)

    ('merge_from_external', uint_mod_8_as_merge_case2skip_or_replace, dst_relative_path, src_fsys_frozendict_or_patch_idx)
    ('merge_from_internal', uint_mod_8_as_merge_case2skip_or_replace, dst_relative_path, src_branch_name, src_branch_idx, src_relative_path)
        skip_or_replace::bool
            replace if skip_or_replace else skip
        merge_case <- [0..2]
        merge_case2skip_or_replace::[bool]{len=3}
            #see: nn_ns.filedir.backup_tools.fsys_mapping_patch.merge_case2skip_or_replace_ops.uint_mod_8_to_merge_case2skip_or_replace
            0: 0b00 file:=file overwrite_file_by_file
            1: 0b01 file:=dir overwrite_file_by_dir
            2: 0b10 dir:=file overwrite_dir_by_file

        vs: merge vs copy
            copy - dst should not exists
            merge - dst may exist
                dir<-dir by recur merge
                file<-dir 0b01, dir<-file 0b10, file<-file 0b00 by replace or skip

    ('mkdirs', dst_relative_path)
        #only use copy_from_external to impl mkdirs, when src_fsys_frozendict is empty
        # dst_relative_path not exist
    ('copy_from_external', dst_relative_path, src_fsys_frozendict_or_patch_idx)
    ('copy_from_internal', dst_relative_path, src_branch_name, src_branch_idx, src_relative_path)
        # never mkdirs dst_relative_path.parent
        #   dst_relative_path.parent exists
        #never copy into dst_relative_path as dir
        #   dst_relative_path is the target path
        #never overwrite dst_relative_path
        #   dst_relative_path should not exists
    ('move_shiftL', dst_relative_path, [src_relative_path])
        #('move', dst_relative_path, src_relative_path)
        #dst/src both in this branch name and idx
        #never move into dst_relative_path as dir
        #   dst_relative_path is the target path
        #never overwrite dst_relative_path
        #   dst_relative_path should not exists
    ('swap_rotateL', [relative_path])
        # move to relative_paths[i-1] from relative_paths[i]
    ('remove', dst_relative_path)

    ('update_file', dst_file_relative_path, src_patch_idx)
        #('patch', dst_file_relative_path, src_patch_idx)
        # assert src_patch_idx.parent==dst_patch_idx
    ('update_fsys', dst_dir_relative_path, offsetted_fsys_patch_frozendict)
        offsetted_fsys_patch_frozendict:
            offsetted by dst_dir_relative_path
            using the dst_dir as root
            relative_path__str inside is relative_to the dst_dir

    ####################################
    ####################################
    where:
        fsys_frozendict = frozendict<basename, (fsys_frozendict|patch_idx)>
        fsys_patch_frozendict = dict<basename, (fsys_patch_frozendict|patch_idx|None|src_relative_path__str)>
            None
                - remove file/dir
            src_relative_path :: tuple<basename>
                - copy/move from src_relative_path to here

        RecurView__fsys_mapping_ex = RecurView fsys_dict = dict_view<basename, (patch_idx | RecurView fsys_dict)>

        fsys_dict <: fsys_mapping
        fsys_mapping_view <: fsys_mapping

    #'''

    @abstractmethod
    def check_fsys_delta(sf, fsys_delta, /):
        'fsys_delta #e.g. FileSystem4update~fsys_delta (= fsys_update_cmd | branch_history_cmd)'
    @abstractmethod
    def ___read_fsys_deltas___(sf, fsys_deltas_binary_ifile, /):
        r'''-> fsys_deltas
        see: read_fsys_deltas
        #'''
    @abstractmethod
    def ___write_fsys_deltas___(sf, fsys_deltas_binary_ofile, fsys_deltas, /):
        r'''
        see: write_fsys_deltas
        #'''





    if not using_FrozenDict_as_valueonly_fsys_mapping_ex:
        r"""
        @abstractmethod
        def get_may_view_of_root_fsys_dict(sf, /):
            '-> (None|RecurView fsys_dict) #may fsys_mapping'
        @abstractmethod
        def deepcopy_may_root_fsys_dict(sf, /):
            '-> (None|fsys_dict)'
        #"""
    else:
        #using_FrozenDict_as_valueonly_fsys_mapping_ex
        @abstractmethod
        def get_may_root_fsys_frozendict(sf, /):
            '-> (None|fsys_frozendict)'
    def mk_fsys_delta4init_empty_branch(sf, /):
        fsys_delta = type(sf).___mk_fsys_delta4init_empty_branch___(sf)
        sf.check_fsys_delta(fsys_delta)
        return fsys_delta
    @abstractmethod
    def ___mk_fsys_delta4init_empty_branch___(sf, /):
        '-> fsys_delta'

    def mk_fsys_delta4remove_branch(sf, /):
        fsys_delta = type(sf).___mk_fsys_delta4remove_branch___(sf)
        sf.check_fsys_delta(fsys_delta)
        return fsys_delta
    @abstractmethod
    def ___mk_fsys_delta4remove_branch___(sf, /):
        '-> fsys_delta'


    @abstractmethod
    def apply_fsys_delta(sf, fsys_delta, /):
        'update underlying may fsys_frozendict'
#end of class IFileSystem4update__fsys_delta(ABC):

class IFileSystem4update__fsys_delta_is_cmd(IFileSystem4update__fsys_delta):
    @classmethod
    @abstractmethod
    def get_cmd_op_names(cls, /):
        '-> frozenset<op_name>'

    def __init__(sf, /):
        sf._may_fsys_frozendict = None

    if not using_FrozenDict_as_valueonly_fsys_mapping_ex:
        r"""
        @override
        def get_may_view_of_root_fsys_dict(sf, /):
            '-> (None|RecurView fsys_dict)'
            m = sf._may_fsys_dict
            if m is None:
                return None
            else:
                fsys_dict = m
                return mk_fsys_mapping_view(fsys_dict)
        @override
        def deepcopy_may_root_fsys_dict(sf, /):
            '-> (None|fsys_dict)'
            if sf._may_fsys_dict is None:
                return None
            else:
                old_root_fsys_dict = sf._may_fsys_dict
                return copy_fsys_dict(old_root_fsys_dict)
        #"""
    else:
        #using_FrozenDict_as_valueonly_fsys_mapping_ex
        @override
        def get_may_root_fsys_frozendict(sf, /):
            '-> (None|fsys_frozendict)'
            return sf._may_fsys_frozendict


    @override
    def apply_fsys_delta(sf, fsys_delta, /):
        'update underlying may fsys_frozendict'
        cmd = fsys_delta
        sf.exec_cmd4apply_fsys_delta(cmd)

    def exec_cmd4apply_fsys_delta(sf, cmd, /):
        'update underlying may fsys_frozendict'
        check_cmd(cmd)

        op = cmd[0]
        op_names = type(sf).get_cmd_op_names()
        if not (op in op_names): raise ValueError(f'unknown fsys_delta-cmd op: {op!r}')
        getattr(sf, op)(*cmd[1:])
        return None
#end of class IFileSystem4update__fsys_delta_is_cmd(IFileSystem4update__fsys_delta):


def mk_check_cmd_ex(cmd_checker_table, /):
    check_cmd_checker_table(cmd_checker_table)
    op_name2checkers = {op_name: checkers for op_name, *checkers in cmd_checker_table}
    def check_cmd_ex(cmd, /):
        check_cmd(cmd)
        op_name, *args = cmd
        may_checkers = op_name2checkers.get(op_name)
        if may_checkers is None:
            raise ValueError(f'unknown op_name={op_name!r}')
        checkers = may_checkers
        if not len(args) == len(checkers): raise TypeError
        for checker, arg in zip(checkers, args):
            checker(arg)
    return check_cmd_ex

def check_cmd_checker_table(cmd_checker_table, /):
    r'''
    cmd_checker_table :: tuple<tuple<op_name, checkers...>>
    #'''
    check_tuple(cmd_checker_table)
    check_all(check_cmd, cmd_checker_table)
    for op_name, *checkers in cmd_checker_table:
        if not all(map(callable, checkers)):raise TypeError

def checker4relative_paths__ge2(relative_paths, /):
    #?? is_not_prefix
    check_tuple(relative_paths)
    check_int(len(relative_paths), min=2)
    check_all(check_relative_path, relative_paths)
def checker4relative_paths__ge1(relative_paths, /):
    #?? is_not_prefix
    check_tuple(relative_paths)
    check_int(len(relative_paths), min=1)
    check_all(check_relative_path, relative_paths)
def checker4uint_mod_8(uint_mod_8, /):
    check_int(uint_mod_8, min=0, max=7)


checker4fsys_frozendict = check_fsys_frozendict
checker4fsys_patch_frozendict = check_fsys_patch_frozendict
checker4fsys_frozendict_or_patch_idx = check_valueonly_fsys_mapping_or_patch_idx

checker4branch_name = check_branch_name
checker4branch_idx = check_uint
checker4patch_idx = check_uint
checker4relative_path = check_relative_path

def _tpl_convert(T, f, tpl, /):
    return tuple(f(x) if type(x) is T else x for x in tpl)
def _args_convert_to_cmd_convert(_args_convert, /):
    def _cmd_convert(cmd, /):
        return (cmd[0], *_args_convert(cmd[1:]))
    return _cmd_convert
def _args_convert__relative_path2str(cmd_args, /):
    T = PurePosixPath
    f = relative_path2str
    return _tpl_convert(T, f, cmd_args)
def _args_convert__str2relative_path(cmd_args, /):
    T = str
    f = str2relative_path
    return _tpl_convert(T, f, cmd_args)
def _cmd_convert__relative_paths2strs(cmd, /):
    T = tuple
    f = _args_convert__relative_path2str
    return _tpl_convert(T, f, cmd)
def _cmd_convert__strs2relative_paths(cmd, /):
    T = tuple
    f = _args_convert__str2relative_path
    return _tpl_convert(T, f, cmd)

def _cmd_convert__dict2frozendict(cmd, /):
    T = dict
    f = deepcopy_fsys_dict_ex_as_fsys_frozendict_ex
    return _tpl_convert(T, f, cmd)
def _cmd_convert__frozendict2dict(cmd, /):
    T = FrozenDict
    f = deepcopy_fsys_frozendict_ex_as_fsys_dict_ex
    return _tpl_convert(T, f, cmd)
def _read_cmds(binary_ifile, /):
    _cmd_convert__str2relative_path = _args_convert_to_cmd_convert(_args_convert__str2relative_path)

    cmds__dict__strs__str = read_repred_py_obj(binary_ifile)
    cmds__dict__strs = tuple(map(_cmd_convert__str2relative_path, cmds__dict__strs__str))
    cmds__dict = tuple(map(_cmd_convert__strs2relative_paths, cmds__dict__strs))
    cmds = tuple(map(_cmd_convert__dict2frozendict, cmds__dict))
    return cmds
def _write_cmds(binary_ofile, cmds, /):
    _cmd_convert__relative_path2str = _args_convert_to_cmd_convert(_args_convert__relative_path2str)

    cmds__dict = tuple(map(_cmd_convert__frozendict2dict, cmds))
    cmds__dict__strs = tuple(map(_cmd_convert__relative_paths2strs, cmds__dict))
    cmds__dict__strs__str = tuple(map(_cmd_convert__relative_path2str, cmds__dict__strs))
    write_py_obj_as_repr(binary_ofile, cmds__dict__strs__str)




checker4relative_path
checker4fsys_frozendict
checker4fsys_patch_frozendict
#HHHHH
class FileSystem4update__fsys_delta_is_fsys_update_cmd(IFileSystem4update__fsys_delta_is_cmd):
    __cmd_checker_table = (
        ('new_fsys', checker4fsys_frozendict)
        ,('mk_empty_fsys',)
        ,('del_fsys',)
        ,('update_fsys', checker4relative_path, checker4fsys_patch_frozendict)
        )
    __check_cmd_ex = mk_check_cmd_ex(__cmd_checker_table)
    def check_fsys_update_cmd(sf, fsys_update_cmd, /):
        'fsys_update_cmd #e.g. FileSystem4update~fsys_delta (= fsys_update_cmd | branch_history_cmd)'
        __class__.__check_cmd_ex(fsys_update_cmd)
    def ___read_fsys_update_cmds___(sf, fsys_update_cmds_binary_ifile, /):
        r'''-> fsys_update_cmds
        see: read_fsys_update_cmds
        #'''
        return _read_cmds(fsys_update_cmds_binary_ifile)
    def ___write_fsys_update_cmds___(sf, fsys_update_cmds_binary_ofile, fsys_update_cmds, /):
        r'''
        see: write_fsys_update_cmds
        #'''
        _write_cmds(fsys_update_cmds_binary_ofile, fsys_update_cmds)

    @override
    def check_fsys_delta(sf, fsys_delta, /):
        'fsys_delta #e.g. FileSystem4update~fsys_delta (= fsys_update_cmd | branch_history_cmd)'
        fsys_update_cmd = fsys_delta
        sf.check_fsys_update_cmd(fsys_update_cmd)

    @override
    def ___read_fsys_deltas___(sf, fsys_deltas_binary_ifile, /):
        r'''-> fsys_deltas
        see: read_fsys_deltas
        #'''
        return type(sf).___read_fsys_update_cmds___(sf, fsys_deltas_binary_ifile)
    @override
    def ___write_fsys_deltas___(sf, fsys_deltas_binary_ofile, fsys_deltas, /):
        r'''
        see: write_fsys_deltas
        #'''
        type(sf).___write_fsys_update_cmds___(sf, fsys_deltas_binary_ofile, fsys_deltas)




    @override
    def ___mk_fsys_delta4init_empty_branch___(sf, /):
        '-> fsys_delta'
        fsys_delta = ('mk_empty_fsys',)
        return fsys_delta
    @override
    def ___mk_fsys_delta4remove_branch___(sf, /):
        '-> fsys_delta'
        fsys_delta = ('del_fsys',)
        return fsys_delta
    @override
    def apply_fsys_delta(sf, fsys_delta, /):
        'update underlying may fsys_frozendict'
        fsys_update_cmd = fsys_delta
        sf.exec_fsys_update_cmd(fsys_update_cmd)
    def exec_fsys_update_cmd(sf, fsys_update_cmd, /):
        'update underlying may fsys_frozendict'
        cmd = fsys_delta = fsys_update_cmd
        sf.exec_cmd4apply_fsys_delta(cmd)

    @classmethod
    @override
    def get_cmd_op_names(cls, /):
        '-> frozenset<op_name>'
        return __class__.__op_names
    __op_names = frozenset(('new_fsys', 'mk_empty_fsys', 'del_fsys', 'update_fsys'))

    if 0:
        r'''
        ('new_fsys', src_fsys_frozendict)
        ('mk_empty_fsys',)
        ('del_fsys',)
        ('update_fsys', dst_dir_relative_path, offsetted_fsys_patch_frozendict)
        #'''

    def new_fsys(sf, src_fsys_frozendict, /):
        if not sf._may_fsys_frozendict is None: raise RuntimeError
        check_fsys_frozendict(src_fsys_frozendict)
        sf._may_fsys_frozendict = fsys_frozendict = echo_valueonly_fsys_mapping(src_fsys_frozendict)# = copy_fsys_dict(src_fsys_dict)
    def mk_empty_fsys(sf, /):
        if not sf._may_fsys_frozendict is None: raise RuntimeError
        sf._may_fsys_frozendict = fsys_frozendict = echo_valueonly_fsys_mapping(FrozenDict())

    def del_fsys(sf, /):
        if sf._may_fsys_frozendict is None: raise RuntimeError
        old_fsys_frozendict = sf._may_fsys_frozendict
        sf._may_fsys_frozendict = None

    r'''
    def update_fsys(sf, fsys_patch_frozendict, /):
        ('update_fsys', fsys_patch_frozendict)
        if sf._may_fsys_frozendict is None: raise RuntimeError
        old_fsys_frozendict = sf._may_fsys_frozendict
        check_fsys_patch_frozendict(fsys_patch_frozendict)
        new_fsys_frozendict = fsys_frozendict_patch(old_fsys_frozendict, fsys_patch_frozendict)
        check_fsys_frozendict(new_fsys_frozendict)
        sf._may_fsys_frozendict = new_fsys_frozendict
    #'''
    def update_fsys(sf, dst_dir_relative_path, offsetted_fsys_patch_frozendict, /):
        if sf._may_fsys_frozendict is None: raise RuntimeError
        old_fsys_frozendict = sf._may_fsys_frozendict

        new_fsys_frozendict = offsetted_fsys_frozendict_patch(old_fsys_frozendict, dst_dir_relative_path, offsetted_fsys_patch_frozendict)
        if 0:#[01_to_turn_off]
            print('@update_fsys')
            print(fr'old_fsys_frozendict={old_fsys_frozendict}')
            print(fr'dst_dir_relative_path={dst_dir_relative_path!r}')
            print(fr'offsetted_fsys_patch_frozendict={offsetted_fsys_patch_frozendict}')
            print(fr'new_fsys_frozendict={new_fsys_frozendict}')
        sf._may_fsys_frozendict = new_fsys_frozendict
        return


#end of class FileSystem4update__fsys_delta_is_fsys_update_cmd(IFileSystem4update__fsys_delta_is_cmd):




checker4fsys_frozendict
checker4branch_name
checker4branch_idx
checker4relative_path
checker4fsys_frozendict_or_patch_idx
checker4relative_paths__ge2#?? is_not_prefix
checker4relative_paths__ge1#?? is_not_prefix
checker4patch_idx
checker4uint_mod_8

#HHHHH
class FileSystem4update__fsys_delta_is_branch_history_cmd(IFileSystem4update__fsys_delta_is_cmd):
    __cmd_checker_table = (
        ('init_via_copy', checker4fsys_frozendict)
        ,('init_via_branch', checker4branch_name, checker4branch_idx)
        ,('init_as_empty',)
        ,('del_branch',)
        ,('merge_from_external', checker4uint_mod_8, checker4relative_path, checker4fsys_frozendict_or_patch_idx)
        ,('merge_from_internal', checker4uint_mod_8, checker4relative_path, checker4branch_name, checker4branch_idx, checker4relative_path)
        ,('mkdirs', checker4relative_path)
        ,('copy_from_external', checker4relative_path, checker4fsys_frozendict_or_patch_idx)
        ,('copy_from_internal', checker4relative_path, checker4branch_name, checker4branch_idx, checker4relative_path)
        ,('move_shiftL', checker4relative_path, checker4relative_paths__ge1)
        ,('swap_rotateL', checker4relative_paths__ge2)
        ,('remove', checker4relative_path)
        ,('update_file', checker4relative_path, checker4patch_idx)
        ,('update_fsys', checker4relative_path, checker4fsys_patch_frozendict)
        )
    __check_cmd_ex = mk_check_cmd_ex(__cmd_checker_table)

    def check_branch_history_cmd(sf, branch_history_cmd, /):
        'branch_history_cmd #e.g. FileSystem4update~fsys_delta (= fsys_update_cmd | branch_history_cmd)'
        __class__.__check_cmd_ex(branch_history_cmd)
    def ___read_branch_history_cmds___(sf, branch_history_cmds_binary_ifile, /):
        r'''-> branch_history_cmds
        see: read_branch_history_cmds
        #'''
        return _read_cmds(branch_history_cmds_binary_ifile)
    def ___write_branch_history_cmds___(sf, branch_history_cmds_binary_ofile, branch_history_cmds, /):
        r'''
        see: write_branch_history_cmds
        #'''
        _write_cmds(branch_history_cmds_binary_ofile, branch_history_cmds)

    @override
    def check_fsys_delta(sf, fsys_delta, /):
        'fsys_delta #e.g. FileSystem4update~fsys_delta (= fsys_update_cmd | branch_history_cmd)'
        branch_history_cmd = fsys_delta
        sf.check_branch_history_cmd(branch_history_cmd)

    @override
    def ___read_fsys_deltas___(sf, fsys_deltas_binary_ifile, /):
        r'''-> fsys_deltas
        see: read_fsys_deltas
        #'''
        return type(sf).___read_branch_history_cmds___(sf, fsys_deltas_binary_ifile)
    @override
    def ___write_fsys_deltas___(sf, fsys_deltas_binary_ofile, fsys_deltas, /):
        r'''
        see: write_fsys_deltas
        #'''
        type(sf).___write_branch_history_cmds___(sf, fsys_deltas_binary_ofile, fsys_deltas)




    def __init__(sf, branch_name2min_extracting_branch_idx, repository_setting:'IRepositorySetting', /):
        r'''
        branch_time_refs/branch_name2min_extracting_branch_idx
            # to avoid cycle
            # :: set<(branch_name, branch_idx)>
            # :: dict<branch_name: min branch_idx>
        repository_setting
            # to access branch_history to impl init_via_branch/copy_from_internal/merge_from_internal
            # :: IRepositorySetting
        #'''
        if not isinstance(branch_name2min_extracting_branch_idx, Mapping): raise TypeError
        if not isinstance(repository_setting, IRepositorySetting): raise TypeError

        sf.branch_name2min_extracting_branch_idx = branch_name2min_extracting_branch_idx
        sf.repository_setting = repository_setting
        super().__init__()
    def exec_branch_history_cmd(sf, branch_history_cmd, /):
        'update underlying may fsys_frozendict'
        cmd = fsys_delta = branch_history_cmd
        sf.exec_cmd4apply_fsys_delta(cmd)

    @override
    def ___mk_fsys_delta4init_empty_branch___(sf, /):
        '-> fsys_delta'
        fsys_delta = ('init_as_empty',)
        return fsys_delta
    @override
    def ___mk_fsys_delta4remove_branch___(sf, /):
        '-> fsys_delta'
        fsys_delta = ('del_branch',)
        return fsys_delta
    @classmethod
    @override
    def get_cmd_op_names(cls, /):
        '-> frozenset<op_name>'
        return __class__.__op_names
    __op_names = frozenset(('init_via_copy', 'init_via_branch', 'init_as_empty', 'del_branch', 'merge_from_external', 'merge_from_internal', 'mkdirs', 'copy_from_external', 'copy_from_internal', 'move_shiftL', 'swap_rotateL', 'remove', 'update_file', 'update_fsys'))

    if 0:
        r'''
        ('init_via_copy', src_fsys_frozendict)
        ('init_via_branch', src_branch_name, src_branch_idx)
        ('init_as_empty',)
        ('del_branch',)
        ('merge_from_external', uint_mod_8_as_merge_case2skip_or_replace, dst_relative_path, src_fsys_frozendict_or_patch_idx)
        ('merge_from_internal', uint_mod_8_as_merge_case2skip_or_replace, dst_relative_path, src_branch_name, src_branch_idx, src_relative_path)
        ('mkdirs', dst_relative_path)
        ('copy_from_external', dst_relative_path, src_fsys_frozendict_or_patch_idx)
        ('copy_from_internal', dst_relative_path, src_branch_name, src_branch_idx, src_relative_path)
        ('move_shiftL', dst_relative_path, [src_relative_path])
        ('swap_rotateL', [relative_path])
        ('remove', dst_relative_path)
        ('update_file', dst_file_relative_path, src_patch_idx)
        ('update_fsys', dst_dir_relative_path, offsetted_fsys_patch_frozendict)
        #'''


    def init_via_copy(sf, src_fsys_frozendict, /):
        if not sf._may_fsys_frozendict is None: raise RuntimeError
        sf._may_fsys_frozendict = fsys_frozendict = echo_valueonly_fsys_mapping(src_fsys_frozendict)# = copy_fsys_dict(src_fsys_dict)
    def init_via_branch(sf, src_branch_name, src_branch_idx, /):
        if not sf._may_fsys_frozendict is None: raise RuntimeError
        # !!!!!too hard to impl here!!!!!
        may_src_root_fsys_frozendict = sf.repository_setting.extract_may_root_fsys_frozendict_at_branch_time(sf.branch_name2min_extracting_branch_idx, src_branch_name, src_branch_idx)
        if may_src_root_fsys_frozendict is None: raise ValueError
        src_root_sys_frozendict = may_src_root_fsys_frozendict
        sf._may_fsys_frozendict = fsys_frozendict = echo_valueonly_fsys_mapping(src_root_sys_frozendict) #= copy_fsys_dict(src_root_fsys_dict)
    def init_as_empty(sf, /):
        if not sf._may_fsys_frozendict is None: raise RuntimeError
        sf._may_fsys_frozendict = fsys_frozendict = echo_valueonly_fsys_mapping(FrozenDict())

    def del_branch(sf, /):
        if sf._may_fsys_frozendict is None: raise RuntimeError
        old_fsys_frozendict = sf._may_fsys_frozendict
        sf._may_fsys_frozendict = None



    def get_tmay_sub_fsys_frozendict_or_patch_idx_from_internal(sf, src_branch_name, src_branch_idx, src_relative_path, /):
        may_src_root_fsys_frozendict = sf.repository_setting.extract_may_root_fsys_frozendict_at_branch_time(sf.branch_name2min_extracting_branch_idx, src_branch_name, src_branch_idx)
        if may_src_root_fsys_frozendict is None: raise ValueError
        src_root_sys_frozendict = may_src_root_fsys_frozendict
        tmay_src_fsys_frozendict_or_patch_idx = get_tmay_sub_fsys_mapping_or_patch_idx(src_root_sys_frozendict, src_relative_path)
        return tmay_src_fsys_frozendict_or_patch_idx

    if not using_FrozenDict_as_valueonly_fsys_mapping_ex:
        r"""
        def __merge_from(sf, merge_case2skip_or_replace, dst_relative_path, src_fsys_frozendict_or_patch_idx, /):
            if sf._may_fsys_frozendict is None: raise RuntimeError
            old_fsys_frozendict = sf._may_fsys_frozendict
            tmay_dst_fsys_frozendict_or_patch_idx = get_tmay_sub_fsys_mapping_or_patch_idx(old_fsys_frozendict, dst_relative_path)
            if not tmay_dst_fsys_frozendict_or_patch_idx: raise ValueError('merge to nothing')
            [dst_fsys_frozendict_or_patch_idx] = tmay_dst_fsys_frozendict_or_patch_idx
            new_fsys_frozendict_or_patch_idx = fsys_frozendict_or_patch_idx_merge(merge_case2skip_or_replace, dst_fsys_frozendict_or_patch_idx, src_fsys_frozendict_or_patch_idx)
            if is_relative_path_empty(dst_relative_path):
                sf._may_fsys_frozendict = new_fsys_frozendict_or_patch_idx
            else:
                tmay_dst_parent_frozendict = get_tmay_sub_fsys_mapping_or_patch_idx(old_fsys_frozendict, dst_relative_path.parent)
                if not tmay_dst_parent_frozendict: raise logic-err
                [dst_parent_frozendict] = tmay_dst_parent_frozendict
                dst_basename = dst_relative_path.name
                assert dst_parent_frozendict[dst_basename] is dst_fsys_frozendict_or_patch_idx
                dst_parent_frozendict[dst_basename] = new_fsys_frozendict_or_patch_idx
                    #inplace
        #"""
    else:
        #using_FrozenDict_as_valueonly_fsys_mapping_ex
        def __merge_from(sf, merge_case2skip_or_replace, dst_relative_path, src_fsys_frozendict_or_patch_idx, /):
            if sf._may_fsys_frozendict is None: raise RuntimeError
            old_fsys_frozendict = sf._may_fsys_frozendict
            (parts, depth, ancestors, sub_fsys_frozendict_or_patch_idx) = cd_to_sub_fsys_mapping_ex_or_pseudo_virtual_file_reprobj_as_deep_as_possible_ex(old_fsys_frozendict, dst_relative_path)
            if not depth == len(parts): raise ValueError('merge to nothing')
            dst_fsys_frozendict_or_patch_idx = sub_fsys_frozendict_or_patch_idx
            new_fsys_frozendict_or_patch_idx = fsys_frozendict_or_patch_idx_merge(merge_case2skip_or_replace, dst_fsys_frozendict_or_patch_idx, src_fsys_frozendict_or_patch_idx)
            if not parts:
                if type(new_fsys_frozendict_or_patch_idx) is int:
                    patch_idx = new_fsys_frozendict_or_patch_idx
                    raise ValueError('merge to root but yield patch_idx')
                else:
                    new_fsys_frozendict = new_fsys_frozendict_or_patch_idx
                    sf._may_fsys_frozendict = new_fsys_frozendict
            else:
                sf.__ireplace_or_remove_via_tmay
                new_fsys_frozendict_or_patch_idx
                dst_ancestor_basename_pair1s = sf.__move_or_swap_or_remove_src2ancestor_basename_pair1s(dst_relative_path)
                    #merge.dst ~ move.src
                assert dst_ancestor_basename_pair1s

                #dst_parent_frozendict[dst_basename] = new_fsys_frozendict_or_patch_idx
                child = echo_valueonly_fsys_mapping_or_patch_idx(new_fsys_frozendict_or_patch_idx)
                tmay_child = (child,)
                sf.__ireplace_or_remove_via_tmay(dst_ancestor_basename_pair1s, tmay_child)
                    #not_inplace



    def merge_from_external(sf, uint_mod_8_as_merge_case2skip_or_replace, dst_relative_path, src_fsys_frozendict_or_patch_idx, /):
        merge_case2skip_or_replace = merge_case2skip_or_replace_ops.uint_mod_8_to_merge_case2skip_or_replace(uint_mod_8_as_merge_case2skip_or_replace)
        sf.__merge_from(merge_case2skip_or_replace, dst_relative_path, src_fsys_frozendict_or_patch_idx)
    def merge_from_internal(sf, uint_mod_8_as_merge_case2skip_or_replace, dst_relative_path, src_branch_name, src_branch_idx, src_relative_path, /):
        merge_case2skip_or_replace = merge_case2skip_or_replace_ops.uint_mod_8_to_merge_case2skip_or_replace(uint_mod_8_as_merge_case2skip_or_replace)
        tmay_src_fsys_frozendict_or_patch_idx = sf.get_tmay_sub_fsys_frozendict_or_patch_idx_from_internal(src_branch_name, src_branch_idx, src_relative_path)
        if not tmay_src_fsys_frozendict_or_patch_idx: raise ValueError('merge from nothing')
        [src_fsys_frozendict_or_patch_idx] = tmay_src_fsys_frozendict_or_patch_idx

        sf.__merge_from(merge_case2skip_or_replace, dst_relative_path, src_fsys_frozendict_or_patch_idx)

    if not using_FrozenDict_as_valueonly_fsys_mapping_ex:
        r'''
        def mkdirs(sf, dst_relative_path, /):
            if sf._may_fsys_frozendict is None: raise RuntimeError
            old_fsys_frozendict = sf._may_fsys_dict
            (parts, depth, ancestors, sub_fsys_frozendict_or_patch_idx) = cd_to_sub_fsys_mapping_ex_or_pseudo_virtual_file_reprobj_as_deep_as_possible_ex(old_fsys_frozendict, dst_relative_path)
            if type(sub_fsys_frozendict_or_patch_idx) is int: raise ValueError('mkdirs: meet file')
            sub_fsys_frozendict = sub_fsys_frozendict_or_patch_idx
            if depth == len(parts): raise ValueError('mkdirs: dir exists')
            assert parts[depth] not in sub_fsys_frozendict
            for basename in parts[depth:]:
                sub_fsys_frozendict[basename] = child = {}
                    #inplace
                sub_fsys_frozendict = child
        #'''
    else:
        #using_FrozenDict_as_valueonly_fsys_mapping_ex
        def mkdirs(sf, dst_relative_path, /):
            sf._mkdirs(dst_relative_path, exist_ok=False)
        def _mkdirs(sf, dst_relative_path, /,*, exist_ok:bool):
            if sf._may_fsys_frozendict is None: raise RuntimeError
            old_fsys_frozendict = sf._may_fsys_frozendict
            valueonly_fsys_mapping_ex_from_dict = FrozenDict
            new_root_fsys_frozendict = mkdirs4valueonly_fsys_mapping_ex(valueonly_fsys_mapping_ex_from_dict, old_fsys_frozendict, dst_relative_path, exist_ok=True)
            sf._may_fsys_frozendict = new_root_fsys_frozendict
            return

            if sf._may_fsys_frozendict is None: raise RuntimeError
            old_fsys_frozendict = sf._may_fsys_frozendict

            (parts, depth, ancestors, sub_fsys_frozendict_or_patch_idx) = cd_to_sub_fsys_mapping_ex_or_pseudo_virtual_file_reprobj_as_deep_as_possible_ex(old_fsys_frozendict, dst_relative_path)
            if not parts: raise ValueError('mkdirs: root exists!')
            if type(sub_fsys_frozendict_or_patch_idx) is int: raise ValueError('mkdirs: meet file')
            sub_fsys_frozendict = sub_fsys_frozendict_or_patch_idx
            if depth == len(parts) and exist_ok: return
            if depth == len(parts): raise ValueError('mkdirs: dir exists')
            assert parts[depth] not in sub_fsys_frozendict

            child = FrozenDict()
            for basename in reversed(parts[depth+1:]):
                parent = FrozenDict({basename:child})
                child = parent

            sf.__ireplace_or_remove_via_tmay
            child
            dst_child_basename = parts[depth]
            src_fsys_frozendict = child
            dst_relative_path = parts2relative_path(parts[:depth+1])

            dst_ancestor_basename_pair1s = sf.__copy_or_move_dst2ancestor_basename_pair1s(dst_relative_path)
            assert dst_ancestor_basename_pair1s

            #dst_parent_frozendict[dst_basename] = src_fsys_frozendict
            child = echo_valueonly_fsys_mapping_or_patch_idx(src_fsys_frozendict)
            tmay_child = (child,)
            sf.__ireplace_or_remove_via_tmay(dst_ancestor_basename_pair1s, tmay_child)
                #not_inplace



    if not using_FrozenDict_as_valueonly_fsys_mapping_ex:
        r"""
        def __move_or_swap_or_remove_src2parent_frozendict_basename_pair(sf, src_relative_path, /):
            r'''
            :: src_relative_path -> (src_parent_frozendict, src_basename)
            # src_relative_path.parent exists #true for last src of move
            # src_relative_path exists
            #'''
            if sf._may_fsys_frozendict is None: raise RuntimeError
            old_fsys_frozendict = sf._may_fsys_frozendict

            (parts, depth, ancestors, sub_fsys_frozendict_or_patch_idx) = cd_to_sub_fsys_mapping_ex_or_pseudo_virtual_file_reprobj_as_deep_as_possible_ex(old_fsys_frozendict, src_relative_path)

            if not parts: raise ValueError('move/swap/remove src_relative_path is empty/root_dir')
            elif depth == len(parts):
                pass
            elif type(sub_fsys_frozendict_or_patch_idx) is int: raise ValueError('move/swap/remove src ancestor_dir be file, hence src not exists')
            elif 0 <= depth < len(parts): raise ValueError('move/swap/remove src not exists')
            else:
                raise logic-err

            src_fsys_frozendict_or_patch_idx = sub_fsys_frozendict_or_patch_idx

            [src_parent_frozendict] = get_tmay_sub_fsys_mapping_or_patch_idx(old_fsys_frozendict, src_relative_path.parent)
            src_basename = src_relative_path.name
            assert src_basename in src_parent_frozendict
            return src_parent_frozendict, src_basename


        def __copy_or_move_dst2parent_frozendict_basename_pair(sf, dst_relative_path, /):
            r'''
            :: dst_relative_path -> (dst_parent_frozendict, dst_basename)
            # dst_relative_path.parent exists, neednot mkdirs
            # dst_relative_path not exists, neednot overwrite #otherwise use merge_from... instead copy_from...
            #   to replace dir by dir instead of merge, ==>> remove then copy
            #'''

            if sf._may_fsys_frozendict is None: raise RuntimeError
            old_fsys_frozendict = sf._may_fsys_frozendict

            (parts, depth, ancestors, sub_fsys_frozendict_or_patch_idx) = cd_to_sub_fsys_mapping_ex_or_pseudo_virtual_file_reprobj_as_deep_as_possible_ex(old_fsys_frozendict, dst_relative_path)

            if not parts: raise ValueError('copy/move dst_relative_path is empty/root_dir')
            elif depth == len(parts): raise ValueError('copy/move dst exists, to replace should use merge cmd or remove cmd')
            elif type(sub_fsys_frozendict_or_patch_idx) is int: raise ValueError('copy/move dst ancestor_dir be file')
            elif 0 <= depth < len(parts)-1: raise ValueError('copy/move into no where, mkdirs first')
            elif 0 <= depth == len(parts)-1:
                pass
            else:
                raise logic-err

            dst_parent_frozendict = sub_fsys_frozendict_or_patch_idx

            dst_basename = dst_relative_path.name
            assert dst_basename = parts[-1]
            assert dst_basename not in dst_parent_frozendict
            return dst_parent_frozendict, dst_basename

        def __copy_from(sf, dst_relative_path, src_fsys_frozendict_or_patch_idx, /):
            (dst_parent_frozendict, dst_basename) = sf.__copy_or_move_dst2parent_frozendict_basename_pair(dst_relative_path)
            dst_parent_frozendict[dst_basename] = copy_fsys_dict_or_patch_idx(src_fsys_dict_or_patch_idx)
                #inplace
        #"""
    else:
        #using_FrozenDict_as_valueonly_fsys_mapping_ex
        #__move_or_swap_or_remove_src2parent_frozendict_basename_pair
        #__move_or_swap_or_remove_src2ancestor_basename_pair1s
        def __move_or_swap_or_remove_src2ancestor_basename_pair1s(sf, src_relative_path, /):
            r'''
            :: src_relative_path -> [(src_ancestor, child_basename)]{len>=1}
            # src_relative_path.parent exists #true for last src of move
            # src_relative_path exists
            #'''
            if sf._may_fsys_frozendict is None: raise RuntimeError
            old_fsys_frozendict = sf._may_fsys_frozendict

            (parts, depth, ancestors, sub_fsys_frozendict_or_patch_idx) = cd_to_sub_fsys_mapping_ex_or_pseudo_virtual_file_reprobj_as_deep_as_possible_ex(old_fsys_frozendict, src_relative_path)

            if not parts: raise ValueError('move/swap/remove src_relative_path is empty/root_dir')
            elif depth == len(parts):
                pass
            elif type(sub_fsys_frozendict_or_patch_idx) is int: raise ValueError('move/swap/remove src ancestor_dir be file, hence src not exists')
            elif 0 <= depth < len(parts): raise ValueError('move/swap/remove src not exists')
            else:
                raise logic-err

            src_fsys_frozendict_or_patch_idx = sub_fsys_frozendict_or_patch_idx

            assert ancestors
            src_parent_frozendict = ancestors[-1]
            src_basename = src_relative_path.name
            assert src_basename == parts[-1]
            assert src_basename in src_parent_frozendict
            return (*zip(ancestors, parts),)


        #__copy_or_move_dst2parent_frozendict_basename_pair
        #__copy_or_move_dst2ancestor_basename_pair1s
        def __copy_or_move_dst2ancestor_basename_pair1s(sf, dst_relative_path, /):
            r'''
            :: dst_relative_path -> [(dst_ancestor, child_basename)]{len>=1}
            # dst_relative_path.parent exists, neednot mkdirs
            # dst_relative_path not exists, neednot overwrite #otherwise use merge_from... instead copy_from...
            #   to replace dir by dir instead of merge, ==>> remove then copy
            #'''

            if sf._may_fsys_frozendict is None: raise RuntimeError
            old_fsys_frozendict = sf._may_fsys_frozendict

            (parts, depth, ancestors, sub_fsys_frozendict_or_patch_idx) = cd_to_sub_fsys_mapping_ex_or_pseudo_virtual_file_reprobj_as_deep_as_possible_ex(old_fsys_frozendict, dst_relative_path)

            if not parts: raise ValueError('copy/move dst_relative_path is empty/root_dir')
            elif depth == len(parts): raise ValueError('copy/move dst exists, to replace should use merge cmd or remove cmd')
            elif type(sub_fsys_frozendict_or_patch_idx) is int: raise ValueError('copy/move dst ancestor_dir be file')
            elif 0 <= depth < len(parts)-1: raise ValueError('copy/move into no where, mkdirs first')
            elif 0 <= depth == len(parts)-1:
                pass
            else:
                raise logic-err

            dst_parent_frozendict = sub_fsys_frozendict_or_patch_idx

            dst_basename = dst_relative_path.name
            assert dst_basename == parts[-1]
            assert dst_basename not in dst_parent_frozendict
            #return dst_parent_frozendict, dst_basename
            return (*zip(ancestors, parts[:-1]), (dst_parent_frozendict, dst_basename))

        def __copy_from(sf, dst_relative_path, src_fsys_frozendict_or_patch_idx, /):
            dst_ancestor_basename_pair1s = sf.__copy_or_move_dst2ancestor_basename_pair1s(dst_relative_path)
            assert dst_ancestor_basename_pair1s

            #dst_parent_frozendict[dst_basename] = src_fsys_frozendict_or_patch_idx
            child = echo_valueonly_fsys_mapping_or_patch_idx(src_fsys_frozendict_or_patch_idx)
            tmay_child = (child,)
            sf.__ireplace_or_remove_via_tmay(dst_ancestor_basename_pair1s, tmay_child)
                #not_inplace

    def copy_from_external(sf, dst_relative_path, src_fsys_frozendict_or_patch_idx, /):
        sf.__copy_from(dst_relative_path, src_fsys_frozendict_or_patch_idx)
    def copy_from_internal(sf, dst_relative_path, src_branch_name, src_branch_idx, src_relative_path, /):
        tmay_src_fsys_frozendict_or_patch_idx = sf.get_tmay_sub_fsys_frozendict_or_patch_idx_from_internal(src_branch_name, src_branch_idx, src_relative_path)
        if not tmay_src_fsys_frozendict_or_patch_idx: raise ValueError('copy from nothing')
        [src_fsys_frozendict_or_patch_idx] = tmay_src_fsys_frozendict_or_patch_idx

        sf.__copy_from(dst_relative_path, src_fsys_frozendict_or_patch_idx)
        return
        #merge_from_internal

    def __move_or_swap_check_no_ancestor_dir(sf, dst_or_src_relative_paths, /):
        sorted_dst_or_src_relative_path_partss = sorted(map(relative_path2parts, dst_or_src_relative_paths))
        if not sorted_dst_or_src_relative_path_partss[0]: raise ValueError('move/swap dst/src is root dir')
        for i in range(1, len(sorted_dst_or_src_relative_path_partss)):
            prev_dst_or_src_relative_path_parts = sorted_dst_or_src_relative_path_partss[i-1]
            curr_dst_or_src_relative_path_parts = sorted_dst_or_src_relative_path_partss[i]
            if is_prefix_of_seq(prev_dst_or_src_relative_path_parts, curr_dst_or_src_relative_path_parts): raise ValueError('move/swap dst/src contain both curr_dir_or_file and its ancestor_dir')


    if not using_FrozenDict_as_valueonly_fsys_mapping_ex:
        r"""
        def __move_shiftL(sf, dst_parent_frozendict, dst_basename, src_parent_frozendict_basename_pairs, /):
            #inplace
            for (src_parent_frozendict, src_basename) in src_parent_frozendict_basename_pairs:
                assert dst_basename not in dst_parent_frozendict
                dst_parent_frozendict[dst_basename] = copy_fsys_dict_or_patch_idx(src_parent_dict[src_basename])
                    #inplace
                del src_parent_frozendict[src_basename]
                    #inplace
                (dst_parent_frozendict, dst_basename) = (src_parent_frozendict, src_basename)


        def move_shiftL(sf, dst_relative_path, src_relative_paths, /):
            if sf._may_fsys_frozendict is None: raise RuntimeError
            old_fsys_frozendict = sf._may_fsys_frozendict
            if not type(src_relative_paths) is tuple: raise TypeError
            if not src_relative_paths: raise ValueError('move_shiftL with no src_relative_paths')

            dst_or_src_relative_paths = [dst_relative_path, *src_relative_paths]
            sf.__move_or_swap_check_no_ancestor_dir(dst_or_src_relative_paths)

            (dst_parent_frozendict, dst_basename) = sf.__copy_or_move_dst2parent_frozendict_basename_pair(dst_relative_path)

            dst_relative_path #checked not exists
            assert dst_basename not in dst_parent_frozendict


            src_parent_frozendict_basename_pairs = tuple(map(sf.__move_or_swap_or_remove_src2parent_frozendict_basename_pair, src_relative_paths))
                #checked exists
            sf.__move_shiftL(dst_parent_frozendict, dst_basename, src_parent_frozendict_basename_pairs)
                #inplace


        def swap_rotateL(sf, relative_paths, /):
            if sf._may_fsys_frozendict is None: raise RuntimeError
            old_fsys_frozendict = sf._may_fsys_frozendict
            if not type(relative_paths) is tuple: raise TypeError
            if not len(relative_paths) >= 2: raise ValueError('swap_rotateL with not enough relative_paths')

            dst_or_src_relative_paths = relative_paths
            sf.__move_or_swap_check_no_ancestor_dir(dst_or_src_relative_paths)

            dst_parent_frozendict = {}
            dst_basename = '0'
            src_parent_frozendict_basename_pairs = (*map(sf.__move_or_swap_or_remove_src2parent_frozendict_basename_pair, relative_paths), (dst_parent_frozendict, dst_basename))
                #checked exists
            sf.__move_shiftL(dst_parent_frozendict, dst_basename, src_parent_frozendict_basename_pairs)
                #inplace
            assert not dst_parent_frozendict
        def remove(sf, dst_relative_path, /):
            if sf._may_fsys_frozendict is None: raise RuntimeError
            old_fsys_frozendict = sf._may_fsys_frozendict

            src_relative_path = dst_relative_path
            src_parent_frozendict_basename_pair = sf.__move_or_swap_or_remove_src2parent_frozendict_basename_pair(src_relative_path)
            dst_parent_frozendict_basename_pair = src_parent_frozendict_basename_pair

            dst_parent_frozendict, dst_basename = dst_parent_frozendict_basename_pair
            assert dst_basename in dst_parent_frozendict
            del dst_parent_frozendict[dst_basename]
                #inplace
        #"""
    else:
        #using_FrozenDict_as_valueonly_fsys_mapping_ex
        def move_shiftL(sf, dst_relative_path, src_relative_paths, /):
            if sf._may_fsys_frozendict is None: raise RuntimeError
            old_fsys_frozendict = sf._may_fsys_frozendict
            if not type(src_relative_paths) is tuple: raise TypeError
            if not src_relative_paths: raise ValueError('move_shiftL with no src_relative_paths')

            dst_or_src_relative_paths = [dst_relative_path, *src_relative_paths]
            sf.__move_or_swap_check_no_ancestor_dir(dst_or_src_relative_paths)

            dst_ancestor_basename_pair1s = sf.__copy_or_move_dst2ancestor_basename_pair1s(dst_relative_path)

            dst_relative_path #checked not exists
            assert dst_ancestor_basename_pair1s
            (dst_parent_frozendict, dst_basename) = dst_ancestor_basename_pair1s[-1]
            assert dst_basename not in dst_parent_frozendict


            src_ancestor_basename_pair1s_ls = tuple(map(sf.__move_or_swap_or_remove_src2ancestor_basename_pair1s, src_relative_paths))
                #checked exists

            dst_ancestor_basename_pair1s_ls = [dst_ancestor_basename_pair1s, *src_ancestor_basename_pair1s_ls]
            dst_exists_ls = [False, *[True]*len(src_relative_paths)]
                # shouldnot pop last src!!!
                # push_left dst
            tmay_src_fsys_frozendict_or_patch_idx__ls = [(src_parent_frozendict[child_basename],) for pair1s in src_ancestor_basename_pair1s_ls for src_parent_frozendict, child_basename in [pair1s[-1]]]
            tmay_src_fsys_frozendict_or_patch_idx__ls.append(())
                #remov last src

            dst_ancestor_basename_pair1s_dst_exists_tmay_src_fsys_frozendict_or_patch_idx_triples = zip(dst_ancestor_basename_pair1s_ls, dst_exists_ls, tmay_src_fsys_frozendict_or_patch_idx__ls)

            old_root_fsys_frozendict = old_fsys_frozendict
            new_root_fsys_frozendict = sf.__move_or_swap_or_remove_main(old_root_fsys_frozendict, dst_ancestor_basename_pair1s_dst_exists_tmay_src_fsys_frozendict_or_patch_idx_triples)
                #not_inplace
            sf._may_fsys_frozendict = new_root_fsys_frozendict






        def swap_rotateL(sf, relative_paths, /):
            if sf._may_fsys_frozendict is None: raise RuntimeError
            old_fsys_frozendict = sf._may_fsys_frozendict
            if not type(relative_paths) is tuple: raise TypeError
            if not len(relative_paths) >= 2: raise ValueError('swap_rotateL with not enough relative_paths')

            dst_or_src_relative_paths = relative_paths
            sf.__move_or_swap_check_no_ancestor_dir(dst_or_src_relative_paths)

            dst_or_src_ancestor_basename_pair1s_ls = tuple(map(sf.__move_or_swap_or_remove_src2ancestor_basename_pair1s, dst_or_src_relative_paths))
                #checked exists

            dst_ancestor_basename_pair1s_ls = dst_or_src_ancestor_basename_pair1s_ls
            dst_exists_ls = [True]*len(dst_or_src_relative_paths)
            tmay_src_fsys_frozendict_or_patch_idx__ls = [(src_parent_frozendict[child_basename],) for pair1s in dst_or_src_ancestor_basename_pair1s_ls for src_parent_frozendict, child_basename in [pair1s[-1]]]
            tmay_src_fsys_frozendict_or_patch_idx__ls = tmay_src_fsys_frozendict_or_patch_idx__ls[1:] + tmay_src_fsys_frozendict_or_patch_idx__ls[:1]
                #shift << 1
            dst_ancestor_basename_pair1s_dst_exists_tmay_src_fsys_frozendict_or_patch_idx_triples = zip(dst_ancestor_basename_pair1s_ls, dst_exists_ls, tmay_src_fsys_frozendict_or_patch_idx__ls)

            old_root_fsys_frozendict = old_fsys_frozendict
            new_root_fsys_frozendict = sf.__move_or_swap_or_remove_main(old_root_fsys_frozendict, dst_ancestor_basename_pair1s_dst_exists_tmay_src_fsys_frozendict_or_patch_idx_triples)
                #not_inplace
            sf._may_fsys_frozendict = new_root_fsys_frozendict



        def remove(sf, dst_relative_path, /):
            if sf._may_fsys_frozendict is None: raise RuntimeError
            old_fsys_frozendict = sf._may_fsys_frozendict

            src_relative_path = dst_relative_path
            src_ancestor_basename_pair1s = sf.__move_or_swap_or_remove_src2ancestor_basename_pair1s(src_relative_path)
            dst_ancestor_basename_pair1s = src_ancestor_basename_pair1s

            assert dst_ancestor_basename_pair1s
            dst_parent_frozendict, dst_basename = dst_ancestor_basename_pair1s[-1]
            assert dst_basename in dst_parent_frozendict

            #del dst_parent_frozendict[dst_basename]
            tmay_child = ()
            sf.__ireplace_or_remove_via_tmay(dst_ancestor_basename_pair1s, tmay_child)
                #not_inplace

        def __ireplace_or_remove_via_tmay(sf, dst_ancestor_basename_pair1s, tmay_child, /):
            #not_inplace
            assert dst_ancestor_basename_pair1s
            assert sf._may_fsys_frozendict is not None
            assert sf._may_fsys_frozendict is dst_ancestor_basename_pair1s[0][0]

            for dst_parent_frozendict, dst_child_basename in reversed(dst_ancestor_basename_pair1s):
                new_parent_frozendict = dst_parent_frozendict.ireplace_or_remove_via_tmay({dst_child_basename: tmay_child})
                    #not_inplace
                tmay_child = (new_parent_frozendict,)
            root_fsys_frozendict = new_parent_frozendict # neednot "= tmay_child" since pair1s
            assert type(root_fsys_frozendict) is FrozenDict
            sf._may_fsys_frozendict = root_fsys_frozendict
                #not_inplace


        def __move_or_swap_or_remove_main(sf, old_root_fsys_frozendict, dst_ancestor_basename_pair1s_dst_exists_tmay_src_fsys_frozendict_or_patch_idx_triples, /):
            r'''
            #not_inplace
            -> new_root_fsys_frozendict

            old_root_fsys_frozendict
            dst_parent_fsys_frozendict must exist!
            [(dst_ancestor_basename_pair1s, dst_exists?, tmay_src_fsys_frozendict_or_patch_idx)]
            assert dst_exists[0][0] is old_root_fsys_frozendict
            assert dst_exists or tmay_src_fsys_frozendict_or_patch_idx
            #'''
            check_tuple(dst_ancestor_basename_pair1s_dst_exists_tmay_src_fsys_frozendict_or_patch_idx_triples)
            all(check_tuple(x, sz=3) or 1 for x in dst_ancestor_basename_pair1s_dst_exists_tmay_src_fsys_frozendict_or_patch_idx_triples)
            for dst_ancestor_basename_pair1s, dst_exists, tmay_src_fsys_frozendict_or_patch_idx in dst_ancestor_basename_pair1s_dst_exists_tmay_src_fsys_frozendict_or_patch_idx_triples:
                assert dst_ancestor_basename_pair1s
                assert dst_ancestor_basename_pair1s[0][0] is old_root_fsys_frozendict
                check_bool(dst_exists)
                check_tmay(tmay_src_fsys_frozendict_or_patch_idx)
                assert dst_exists or tmay_src_fsys_frozendict_or_patch_idx

            d = {} # :: nm2ocv
            out_pseudo__root_basename = 'x'
            r'''
                nm2ocv = {basename:cased_value}
                cased_value
                    = (0, src_fsys_frozendict_or_patch_idx)
                    | (-1, None)
                    | (+1, (old_fsys_frozendict, nm2ocv))
            #'''

            for dst_ancestor_basename_pair1s, dst_exists, tmay_src_fsys_frozendict_or_patch_idx in dst_ancestor_basename_pair1s_dst_exists_tmay_src_fsys_frozendict_or_patch_idx_triples:
                prev_parent__nm2ocv = d
                prev_child_basename = out_pseudo__root_basename
                for dst_ancestor, child_basename in dst_ancestor_basename_pair1s:
                    if prev_child_basename not in prev_parent__nm2ocv:
                        curr_nm2ocv = {}
                        prev_parent__nm2ocv[prev_child_basename] = (+1, (dst_ancestor, curr_nm2ocv))
                    else:
                        pass
                    cased_value = prev_parent__nm2ocv[prev_child_basename]
                    case, value = cased_value
                    if not case == +1: raise logic-err
                    old_fsys_frozendict, curr_nm2ocv = value
                    if not old_fsys_frozendict is dst_ancestor: raise logic-err--is_prefix_of_seq
                    ##
                    prev_parent__nm2ocv = curr_nm2ocv
                    prev_child_basename = child_basename
                #end of cd for
                curr_nm2ocv

                dst_parent_frozendict, dst_basename = dst_ancestor_basename_pair1s[-1]
                assert dst_basename is child_basename
                if not bool(dst_exists) is bool(dst_basename in dst_parent_frozendict):raise logic-err#ValueError

                if tmay_src_fsys_frozendict_or_patch_idx:
                    [src_fsys_frozendict_or_patch_idx] = tmay_src_fsys_frozendict_or_patch_idx
                    cased_value = (0, src_fsys_frozendict_or_patch_idx)
                else:
                    cased_value = (-1, None)
                curr_nm2ocv[dst_basename] = cased_value
            #end of per triple for

            #nm2ocv -> FrozenDict
            #cased_value -> tmay_src_fsys_frozendict_or_patch_idx
            def recur(old_fsys_frozendict, nm2ocv, /):
                d = {**old_fsys_frozendict}
                for basename, cased_value in nm2ocv.items():
                    case, value = cased_value
                    if case == 0:
                        src_fsys_frozendict_or_patch_idx = value
                        d[basename] = src_fsys_frozendict_or_patch_idx
                    elif case == -1:
                        assert value is None
                        del d[basename]
                    elif case == +1:
                        (old_fsys_frozendict, nm2ocv) = value
                        d[basename] = recur(old_fsys_frozendict, nm2ocv)
                return FrozenDict(d)
            new_root_fsys_frozendict = recur(*d[out_pseudo__root_basename][1])
            return new_root_fsys_frozendict






    if not using_FrozenDict_as_valueonly_fsys_mapping_ex:
        r'''
        #patch
        def update_file(sf, dst_file_relative_path, src_patch_idx, /):
            #def patch(sf, dst_file_relative_path, src_patch_idx, /):
            if sf._may_fsys_frozendict is None: raise RuntimeError
            old_fsys_frozendict = sf._may_fsys_frozendict

            tmay_dst_fsys_frozendict_or_patch_idx = get_tmay_sub_fsys_mapping_or_patch_idx(old_fsys_frozendict, dst_file_relative_path)
            if not tmay_dst_fsys_frozendict_or_patch_idx: raise ValueError('patch to nothing')
            [dst_fsys_frozendict_or_patch_idx] = tmay_dst_fsys_frozendict_or_patch_idx
            if not type(dst_fsys_frozendict_or_patch_idx) is int: raise ValueError('patch dst is dir (should be file)')
            dst_patch_idx = dst_fsys_frozendict_or_patch_idx
            src_patch_idx
            #assert src_patch_idx.parent==dst_patch_idx
            src_imay_parent_idx = sf.repository_setting.patch_idx2imay_parent_idx(src_patch_idx)
            if not dst_patch_idx == src_imay_parent_idx: raise ValueError('patch/update_file cmd: src_imay_parent_idx.parent != dst_patch_idx; to replace use remov/copy/merge cmd instead')

            [dst_parent_frozendict] = get_tmay_sub_fsys_mapping_or_patch_idx(old_fsys_frozendict, dst_file_relative_path.parent)
            dst_basename = dst_file_relative_path.basename
            assert dst_parent_frozendict[dst_basename] is dst_patch_idx
            dst_parent_frozendict[dst_basename] = src_patch_idx
                #inplace
        def update_fsys(sf, dst_dir_relative_path, offsetted_fsys_patch_frozendict, /):
            raise NotImplementedError ...
        #'''
    else:
        #using_FrozenDict_as_valueonly_fsys_mapping_ex
        def update_fsys(sf, dst_dir_relative_path, offsetted_fsys_patch_frozendict, /):
            if sf._may_fsys_frozendict is None: raise RuntimeError
            old_fsys_frozendict = sf._may_fsys_frozendict

            new_fsys_frozendict = offsetted_fsys_frozendict_patch(old_fsys_frozendict, dst_dir_relative_path, offsetted_fsys_patch_frozendict)

            if 0:#[01_to_turn_off]
                print('@update_fsys')
                print(fr'old_fsys_frozendict={old_fsys_frozendict}')
                print(fr'dst_dir_relative_path={dst_dir_relative_path!r}')
                print(fr'offsetted_fsys_patch_frozendict={offsetted_fsys_patch_frozendict}')
                print(fr'new_fsys_frozendict={new_fsys_frozendict}')
            sf._may_fsys_frozendict = new_fsys_frozendict
            return


        #patch
        def update_file(sf, dst_file_relative_path, src_patch_idx, /):
            #def patch(sf, dst_file_relative_path, src_patch_idx, /):
            if sf._may_fsys_frozendict is None: raise RuntimeError
            old_fsys_frozendict = sf._may_fsys_frozendict
            check_uint(src_patch_idx)

            tmay_dst_fsys_frozendict_or_patch_idx = get_tmay_sub_fsys_mapping_or_patch_idx(old_fsys_frozendict, dst_file_relative_path)
            if not tmay_dst_fsys_frozendict_or_patch_idx: raise ValueError('patch to nothing')
            [dst_fsys_frozendict_or_patch_idx] = tmay_dst_fsys_frozendict_or_patch_idx
            if not type(dst_fsys_frozendict_or_patch_idx) is int: raise ValueError('patch dst is dir (should be file)')
            dst_patch_idx = dst_fsys_frozendict_or_patch_idx
            src_patch_idx
            #assert src_patch_idx.parent==dst_patch_idx
            src_imay_parent_idx = sf.repository_setting.patch_idx2imay_parent_idx(src_patch_idx)
            if not dst_patch_idx == src_imay_parent_idx: raise ValueError('patch/update_file cmd: src_imay_parent_idx.parent != dst_patch_idx; to replace use remov/copy/merge cmd instead')

            sf.__ireplace_or_remove_via_tmay
            src_patch_idx

            dst_ancestor_basename_pair1s = sf.__move_or_swap_or_remove_src2ancestor_basename_pair1s(dst_file_relative_path)
                #patch/update_file.dst ~ move.src
            assert dst_ancestor_basename_pair1s

            #dst_parent_frozendict[dst_basename] = src_patch_idx
            child = echo_valueonly_fsys_mapping_or_patch_idx(src_patch_idx)
            tmay_child = (child,)
            sf.__ireplace_or_remove_via_tmay(dst_ancestor_basename_pair1s, tmay_child)
                #not_inplace

#end of class FileSystem4update__fsys_delta_is_branch_history_cmd(IFileSystem4update__fsys_delta_is_cmd):



