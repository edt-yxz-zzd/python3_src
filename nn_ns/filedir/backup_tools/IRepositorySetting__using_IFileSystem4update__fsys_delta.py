r'''

fsys_frozendict
_dict
fsys_dict
    -->> fsys_frozendict
    extract_may_root_fsys_frozendict_at_branch_time
        -->> extract_may_root_fsys_frozendict_at_branch_time

search deepcopy/copy/_dict
    #.deepcopy_may_root_fsys_dict
    may_root_fsys_frozendict = fsys_updater.get_may_root_fsys_frozendict()

========

    , IRepositorySetting__using_IFileSystem4update__fsys_delta
    , IRepositorySetting__using_IFileSystem4update__fsys_delta_is_branch_history_cmd
    , IRepositorySetting__using_IFileSystem4update__fsys_delta_is_fsys_update_cmd

#'''


__all__ = '''
    IRepositorySetting__using_IFileSystem4update__fsys_init__fsys_delta
    IRepositorySetting__using_IFileSystem4update__fsys_delta
    IRepositorySetting__using_IFileSystem4update__fsys_delta_is_branch_history_cmd
    IRepositorySetting__using_IFileSystem4update__fsys_delta_is_fsys_update_cmd
    '''.split()


___begin_mark_of_excluded_global_names__0___ = ...

from nn_ns.filedir.backup_tools.IRepositorySetting import IRepositorySetting, read_repred_py_obj

from nn_ns.filedir.backup_tools.FileSystem4update import check_cmd, FileSystem4update__fsys_delta_is_branch_history_cmd, FileSystem4update__fsys_delta_is_fsys_update_cmd

from nn_ns.filedir.inf_dir import open_under_inf_dir




from abc import ABC, abstractmethod
from seed.abc.abc import override

___end_mark_of_excluded_global_names__0___ = ...








#HHHHH
class IRepositorySetting__using_IFileSystem4update__fsys_init__fsys_delta(IRepositorySetting):
    'fsys_init+fsys_delta'

    @abstractmethod
    def mk_fsys_updater(sf, branch_name2min_extracting_branch_idx, fsys_delta_init_ifile, /):
        '{branch_name:min_extracting_branch_idx} -> binary_ifile -> IFileSystem4update__fsys_delta'

    @abstractmethod
    def iter_read_fsys_delta_objs(sf, fsys_delta_seq_ifile, /):
        'binary_ifile -> Iter fsys_delta'
        obj = read_repred_py_obj(fsys_delta_seq_ifile)
        return iter(obj) or iter([obj])


    def _fsys_updater_iadd(sf, fsys_updater, fsys_delta_seq_ifile, /):
        'fsys_updater -> binary_ifile -> None'
        it = sf.iter_read_fsys_delta_objs(fsys_delta_seq_ifile)
        for fsys_delta in it:
            fsys_updater.apply_fsys_delta(fsys_delta)


    @override
    def ___extract_may_root_fsys_frozendict_at_branch_time___(sf, branch_name2min_extracting_branch_idx, branch_name, branch_idx, /):
        r'''
        branch_name2min_extracting_branch_idx -> branch_name -> branch_idx -> (None|root fsys_frozendict)'
        see: extract_may_root_fsys_frozendict_at_branch_time
        #'''
        branch_history_dir_path = sf.get_branch_history_dir_path(branch_name)
        inf_dir_path = branch_history_dir_path
        dir_size = sf.get_dir_size()
        def open_idx(inf_dir_idx, /):
            return open_under_inf_dir(dir_size, inf_dir_path, inf_dir_idx, None, 'rb')

        with open_idx(0) as fsys_delta_init_ifile:
            fsys_updater = sf.mk_fsys_updater(branch_name2min_extracting_branch_idx, fsys_delta_init_ifile)

        for i in range(1, branch_idx+1):
            with open_idx(i) as fsys_delta_seq_ifile:
                sf._fsys_updater_iadd(fsys_updater, fsys_delta_seq_ifile)
        #.deepcopy_may_root_fsys_dict
        may_root_fsys_frozendict = fsys_updater.get_may_root_fsys_frozendict()
        return may_root_fsys_frozendict


#end of class IRepositorySetting__using_IFileSystem4update__fsys_init__fsys_delta(IRepositorySetting):


class IRepositorySetting__using_IFileSystem4update__fsys_delta(IRepositorySetting__using_IFileSystem4update__fsys_init__fsys_delta):
    'fsys_delta_init_ifile is fsys_delta_seq_ifile  #e.g. fsys_delta = fsys_update_cmd | branch_history_cmd'

    @abstractmethod
    def mk_empty_fsys_updater(sf, branch_name2min_extracting_branch_idx, /):
        '{branch_name:min_extracting_branch_idx} -> IFileSystem4update__fsys_delta'
    @override
    def mk_fsys_updater(sf, branch_name2min_extracting_branch_idx, fsys_delta_init_ifile, /):
        '{branch_name:min_extracting_branch_idx} -> binary_ifile -> IFileSystem4update__fsys_delta'
        fsys_updater = sf.mk_empty_fsys_updater(branch_name2min_extracting_branch_idx)
        fsys_delta_seq_ifile = fsys_delta_init_ifile
        sf._fsys_updater_iadd(fsys_updater, fsys_delta_seq_ifile)
        return fsys_updater
    @override
    def iter_read_fsys_delta_objs(sf, fsys_delta_seq_ifile, /):
        'binary_ifile -> Iter fsys_delta'
        fsys_deltas_binary_ifile = fsys_delta_seq_ifile
        fsys_updater = sf.mk_empty_fsys_updater({})
        fsys_deltas = type(fsys_updater).___read_fsys_deltas___(fsys_updater, fsys_deltas_binary_ifile)
        for fsys_delta in fsys_deltas:
            fsys_updater.check_fsys_delta(fsys_delta)
            yield fsys_delta

    @override
    def check_branch_history_delta(sf, branch_history_delta, /):
        'branch_history_delta #e.g. FileSystem4update~fsys_delta (= fsys_update_cmd | branch_history_cmd)'
        fsys_delta = branch_history_delta
        fsys_updater = sf.mk_empty_fsys_updater({})
        fsys_updater.check_fsys_delta(fsys_delta)
    @override
    def ___read_branch_history_deltas___(sf, branch_history_deltas_binary_ifile, /):
        r'''-> branch_history_deltas
        see: read_branch_history_deltas
        #'''
        fsys_deltas_binary_ifile = branch_history_deltas_binary_ifile
        fsys_updater = sf.mk_empty_fsys_updater({})
        fsys_deltas = type(fsys_updater).___read_fsys_deltas___(fsys_updater, fsys_deltas_binary_ifile)
        branch_history_deltas = fsys_deltas
        return branch_history_deltas
    @override
    def ___write_branch_history_deltas___(sf, branch_history_deltas_binary_ofile, branch_history_deltas, /):
        r'''
        see: write_branch_history_deltas
        #'''
        fsys_deltas_binary_ofile = branch_history_deltas_binary_ofile
        fsys_deltas = branch_history_deltas
        fsys_updater = sf.mk_empty_fsys_updater({})
        type(fsys_updater).___write_fsys_deltas___(fsys_updater, fsys_deltas_binary_ofile, fsys_deltas)


#end of class IRepositorySetting__using_IFileSystem4update__fsys_delta(IRepositorySetting__using_IFileSystem4update__fsys_init__fsys_delta):

read_repred_py_obj
#HHHHH
class IRepositorySetting__using_IFileSystem4update__fsys_delta_is_branch_history_cmd(IRepositorySetting__using_IFileSystem4update__fsys_delta):
    @override
    def mk_empty_fsys_updater(sf, branch_name2min_extracting_branch_idx, /):
        '{branch_name:min_extracting_branch_idx} -> IFileSystem4update__fsys_delta'
        T = FileSystem4update__fsys_delta_is_fsys_update_cmd
        T = FileSystem4update__fsys_delta_is_branch_history_cmd
        repository_setting = sf
        fsys_updater = T(branch_name2min_extracting_branch_idx, repository_setting)
        return fsys_updater


    r'''
    @override
    def iter_read_fsys_delta_objs(sf, fsys_delta_seq_ifile, /):
        'binary_ifile -> Iter fsys_delta'
        cmds = read_repred_py_obj(fsys_delta_seq_ifile)
        if not type(cmds) is tuple: raise TypeError
        for cmd in cmds:
            check_cmd(cmd)
        return iter(cmds)
    #'''



#HHHHH
class IRepositorySetting__using_IFileSystem4update__fsys_delta_is_fsys_update_cmd(IRepositorySetting__using_IFileSystem4update__fsys_delta):
    @override
    def mk_empty_fsys_updater(sf, branch_name2min_extracting_branch_idx, /):
        '{branch_name:min_extracting_branch_idx} -> IFileSystem4update__fsys_delta'
        T = FileSystem4update__fsys_delta_is_branch_history_cmd
        T = FileSystem4update__fsys_delta_is_fsys_update_cmd
        repository_setting = sf
        fsys_updater = T()
        return fsys_updater


    r'''
    @override
    def iter_read_fsys_delta_objs(sf, fsys_delta_seq_ifile, /):
        'binary_ifile -> Iter fsys_delta'
        cmd = read_repred_py_obj(fsys_delta_seq_ifile)
        check_cmd(cmd)
        cmds = [cmd]
        return iter(cmds)
    #'''







