
moving code

#HHHHH
r'''
backup_util
py -m nn_ns.filedir.backup_tools.backup_util

see:
    nn_ns.filedir.dir_cmp
        py::filecmp.dircmp/cmp/cmpfiles
    nn_ns.filedir.file_cmp #diff/patch/delta, O(n)
        py::difflib.restore/context_diff/Differ.compare/ndiff/unified_diff/diff_bytes
            O(n^2)
    nn_ns.filedir.inf_dir
    nn_ns.filedir.backup_tools.backup_util



backup_util vivi git
  why not use git directly?
    scene:
        my phone:
            cannot access Internet to backup to github.com
            can only backup to TF-card
            two storages:
                /mnt/m_internal_storage
                    editable by droidvim/termux
                    where text, source files and git repository are put
                /mnt/m_external_sd
                    readonly by droidvim/termux
                    can be modified only via the phone file manager by copy/delete manually
                    where backup data be store
    backup_util should have these features:
        * backup data grow only, never be deleted, never be modified (except dir growing)
        * very easy to copy manually (neednot overwrite, num files/dirs which need to be copied is very small)



{working_root_dir}/
    #which to be backup
{repository_extra_cache_root_dir}/
    #see:repository_extra_cache_root_dir_path
    #to cache dir_cmp eq result:
    #   patch_idx@fsys_dict ~eq~ {relative_path:{mtime}}@fsys/{working_root_dir}

{backup_data_root/repository_root_dir}/
    grow_only/
        command_history/
            == inf_dir<user_data=delta4command_history>
        branches/
            fsys_history-{branch_name}/
                == inf_dir<user_data=delta4branch_fsys>
        file_patch_forest/
            == inf_dir<user_data=user_data_dir>
    updating/
        file_stack/
            == inf_dir<user_data=any_file_to_be_moved_into_the_grow_only_dir>
        TODO_list4move_cmd
            pop from updating/file_stack to push into other inf_dir under the grow_only_dir
        commit_completed
            #empty file
            #exists or not == commit completed/success or fail/rollback

###
history is a linear in_tree
forest is [in_tree]
in_tree vs out_tree:
    in_tree:  leaf point to root
    out_tree: root point to leaf

command_history
    :: inf_dir<(parent, content)>
fsys_history-{branch_name}
    :: inf_dir<(parent, content)>
    branch_name can include '/' but not '\'
    branch_name can not include space
file_patch_forest
    :: inf_dir<(parent, content, metadata)>
    metadata = (size, str_mtime?, hash_method_uppercase_std_name2digest?)
        to support fast is_same_file beyond is_same_file__True:
        dir_cmp.STR_TIME_FORMAT = '%Y%m%d_%H%M%S_%z'
            # ends with constant %z == +0000

0-level-finite_dir_or_file = user_data
user_data/
    parent :: [-1..]
        ascii text store imay_uint/imay_parent_idx
    content :: bytes
        binary file
        original_file if parent==-1 else patch_file
        ###
        howto patch?
            * command_history.patch_file append to parent patched file
            * file_patch_forest.patch_file using nn_ns.filedir.file_cmp
            * file_patch_forest.patch_file using nn_ns.filedir.file_cmp
#'''




























#HHHHH
__all__ = '''
    RepositorySetting__using_IFileSystem4update__fsys_delta_is_fsys_update_cmd
    RepositorySetting__using_IFileSystem4update__fsys_delta_is_branch_history_cmd
    DirViewer__fsys_dict
    AccessFile4MkIsSameFile__backup_util_repository__fsys_dict__IRepositorySetting





    inf_dir_idx2iter_imay_parent_idx_user_data_dir_path_pairs__inf_dir_as_forest
        inf_dir_idx2iter_imay_parent_idx_content_path_pairs__inf_dir_as_forest
            inf_dir_idx2iter_imay_parent_idx_content_bytes_pairs__inf_dir_as_forest
        inf_dir_idx2iter_imay_parent_idx_content_path_metadata_path_pair_pairs__inf_dir_as_forest

    case2is_patch__case_is_imay_parent_idx
    reversed_case_either_bytes_pairs2original_file_bytes_ordered_patch_file_bytes_ls_pair
        reversed_case_either_bytes_pairs2latest_file_bytes
            reversed_case_either_bytes_pairs2latest_file_bytes__forest__file_cmp__ver1

    fsys_dict_patch
    fsys_dict_or_patch_idx_merge
        _Visit__fsys_patch_mapping4fsys_dict_patch
        _Visit__fsys_mapping4fsys_dict_merge

    Visit__fsys_mapping
        Visit__fsys_patch_mapping
        Visit__fsys_mapping4func
            Visit__fsys_patch_mapping4func

        may_mapping_types_or_check_mapping_type2check_mapping_type
            check_fsys_patch_dict
            check_fsys_dict
                check_fsys_dict_or_patch_idx

                copy_fsys_dict
                    copy_fsys_dict_or_patch_idx

    read_repred_py_obj
    RecurView__fsys_mapping_ex
    merge_case2skip_or_replace_ops
    check_cmd
    IFileSystem4update__fsys_delta
        IFileSystem4update__fsys_delta_is_cmd
            FileSystem4update__fsys_delta_is_fsys_update_cmd
            FileSystem4update__fsys_delta_is_branch_history_cmd

    check_path
    IRepositorySetting__user_data_dir_path
        IRepositorySetting
            IRepositorySetting__cache_min_len_inf_dir
            IRepositorySetting__branches_together
            IRepositorySetting__init_constants
                IRepositorySetting__init_constants__branches_together
                    IRepositorySetting__init_constants__branches_together__cache_min_len_inf_dir__init_caches

                        RepositorySetting__using_IFileSystem4update__fsys_delta_is_fsys_update_cmd
                        RepositorySetting__using_IFileSystem4update__fsys_delta_is_branch_history_cmd

            IRepositorySetting__using_IFileSystem4update__fsys_delta
                IRepositorySetting__using_IFileSystem4update__fsys_delta_is_branch_history_cmd
                    RepositorySetting__using_IFileSystem4update__fsys_delta_is_branch_history_cmd
                IRepositorySetting__using_IFileSystem4update__fsys_delta_is_fsys_update_cmd
                    RepositorySetting__using_IFileSystem4update__fsys_delta_is_fsys_update_cmd


    cd_to_sub_fsys_dict_or_patch_idx_ex_as_deep_as_possible
        get_tmay_sub_fsys_dict_or_patch_idx
            access_path__fsys_dict

    DirViewer__fsys_dict
    AccessFile4MkIsSameFile__backup_util_repository__fsys_dict__IRepositorySetting
        bytes2PseudoFile4MkIsSameFile

    '''.split()
    #_Visit__fsys_patch_mapping4fsys_dict_patch
    #_Visit__fsys_mapping4fsys_dict_merge



from nn_ns.filedir.backup_tools.imports import *














































#HHHHH

#def read_imay_parent__user_data(parent_path):
#       see:user_data_dir_path_setting.read_imay_parent_idx
def _read_imay_parent__user_data(parent_path):
    '-> [-1..] # imay'
    s = parent_path.read_text(encoding='ascii')
    imay_parent_idx = ast.literal_eval(s)
    check_uint_imay(imay_parent_idx)
    return imay_parent_idx


def case2is_patch__case_is_imay_parent_idx(case):
    imay_parent_idx = case
    return imay_parent_idx == -1

def reversed_case_either_bytes_pairs2latest_file_bytes__forest__file_cmp__ver1(reversed_case_either_bytes_pairs, *, case2is_patch):
    'see:reversed_case_either_bytes_pairs2latest_file_bytes'
    def patch(old_file_bytes, patch_file_bytes, /):
        patch_bytes_ex = patch_file_bytes
        return file_patch(old_file_bytes, patch_bytes_ex, ver=1)
    return reversed_case_either_bytes_pairs2latest_file_bytes(reversed_case_either_bytes_pairs, case2is_patch=case2is_patch, init=echo, patch=patch)

def inf_dir_idx2iter_imay_parent_idx_content_bytes_pairs__inf_dir_as_forest(inf_dir_path, inf_dir_idx, /, *, dir_size, user_data_dir_path_setting):
    'inf_dir_path -> uint -> Iter<([-1..], content_bytes)>{nonempty, endby imay_parent_idx==-1}'
    def content_path2bytes(content_path):
        content_bytes = content_path.read_bytes()
        return content_bytes
    return inf_dir_idx2iter_imay_parent_idx_content_path_pairs__inf_dir_as_forest(inf_dir_path, inf_dir_idx, dir_size=dir_size, content_path2value=content_path2bytes, user_data_dir_path_setting=user_data_dir_path_setting)

def inf_dir_idx2iter_imay_parent_idx_content_path_pairs__inf_dir_as_forest(inf_dir_path, inf_dir_idx, /, *, dir_size, content_path2value, user_data_dir_path_setting):
    'inf_dir_path -> uint -> (dir_size) -> (content_path2value::content_path->value) -> Iter<([-1..], value=f(content_path))>{nonempty, endby imay_parent_idx==-1}'
    if content_path2value is None:
        content_path2value = echo
    if not callable(content_path2value): raise TypeError
    def user_data_dir_path2value(user_data_dir_path):
        content_path = user_data_dir_path/user_data_dir_path_setting.get_contentfile_relative_path_under_user_data_dir() # 'content'
        return content_path2value(content_path)
    return inf_dir_idx2iter_imay_parent_idx_user_data_dir_path_pairs__inf_dir_as_forest(inf_dir_path, inf_dir_idx, dir_size=dir_size, user_data_dir_path2value=user_data_dir_path2value, user_data_dir_path_setting=user_data_dir_path_setting)

def inf_dir_idx2iter_imay_parent_idx_user_data_dir_path_pairs__inf_dir_as_forest(inf_dir_path, inf_dir_idx, /, *, dir_size, user_data_dir_path2value, user_data_dir_path_setting):
    'inf_dir_path -> uint -> (dir_size) -> (user_data_dir_path2value::user_data_dir_path->value) -> Iter<([-1..], value=f(user_data_dir_path))>{nonempty, endby imay_parent_idx==-1}'
    if type(inf_dir_idx) is not int: raise TypeError
    if not inf_dir_idx >= 0: raise ValueError
    if user_data_dir_path2value is None:
        user_data_dir_path2value = echo
    if not callable(user_data_dir_path2value): raise TypeError

    imay_parent_idx = inf_dir_idx
    while imay_parent_idx != -1:
        inf_dir_idx = imay_parent_idx
        ###next round:
        inf_dir_idx_relative_path = inf_dir_idx2user_data_relative_path(inf_dir_idx, dir_size=dir_size)
        user_data_dir_path = inf_dir_path/inf_dir_idx_relative_path
        parent_path = user_data_dir_path/user_data_dir_path_setting.get_parentfile_relative_path_under_user_data_dir() # 'parent'
        value = user_data_dir_path2value(user_data_dir_path)
        imay_parent_idx = user_data_dir_path_setting.read_imay_parent_idx(parent_path) # read_imay_parent__user_data(parent_path)
        yield (imay_parent_idx, value)



def inf_dir_idx2iter_imay_parent_idx_content_path_metadata_path_pair_pairs__inf_dir_as_forest(inf_dir_path, inf_dir_idx, /, *, dir_size, content_path2value, metadata_path2value, user_data_dir_path_setting):
    'inf_dir_path -> uint -> (dir_size) -> (content_path2value::content_path->content_value) -> (metadata_path2value::metadata_path->metadata_value) -> Iter<([-1..], (content_value=f(content_path), metadata_value=g(metadata_path)))>{nonempty, endby imay_parent_idx==-1}'
    user_data_dir_path_setting.read_metadata
    if content_path2value is None:
        content_path2value = echo
    if metadata_path2value is None:
        metadata_path2value = echo
    if not callable(content_path2value): raise TypeError
    if not callable(metadata_path2value): raise TypeError

    def user_data_dir_path2value(user_data_dir_path):
        content_path = user_data_dir_path/user_data_dir_path_setting.get_contentfile_relative_path_under_user_data_dir() # 'content'
        metadata_path = user_data_dir_path/user_data_dir_path_setting.get_metadatafile_relative_path_under_user_data_dir() # 'metadata'
        content_value = content_path2value(content_path)
        metadata_value = metadata_path2value(metadata_path)
        return content_value, metadata_value
    return inf_dir_idx2iter_imay_parent_idx_user_data_dir_path_pairs__inf_dir_as_forest(inf_dir_path, inf_dir_idx, dir_size=dir_size, user_data_dir_path2value=user_data_dir_path2value, user_data_dir_path_setting=user_data_dir_path_setting)





r'''
see: extract_may_root_fsys_dict_at_branch_time
def reversed_case_either_bytes_pairs2latest_file_bytes__command_history__append(reversed_case_either_bytes_pairs, *, case2is_patch):
    (original_file_bytes, ordered_patch_file_bytes_ls) = reversed_case_either_bytes_pairs2original_file_bytes_ordered_patch_file_bytes_ls_pair(reversed_case_either_bytes_pairs, case2is_patch=case2is_patch)
    latest_file_bytes = b''.join(original_file_bytes, *ordered_patch_file_bytes_ls)
    return latest_file_bytes
#'''

r'''
see: IRepositorySetting__using_IFileSystem4update__fsys_delta.mk_fsys_updater/iter_read_fsys_delta_objs
def reversed_case_either_bytes_pairs2latest_file_bytes__branch_history__fsys_update(reversed_case_either_bytes_pairs, *, case2is_patch):
    'see:reversed_case_either_bytes_pairs2latest_file_bytes'
    return reversed_case_either_bytes_pairs2latest_file_bytes(reversed_case_either_bytes_pairs, case2is_patch=case2is_patch, init=read_fsys_obj__bytes, patch=fsys_patch)
#'''


def reversed_case_either_bytes_pairs2original_file_bytes_ordered_patch_file_bytes_ls_pair(reversed_case_either_bytes_pairs, *, case2is_patch):
    r'''Iter<(case, either_bytes=patch_file_bytes if case2is_patch(case) else original_file_bytes)>{latest bytes come first, contains original_file_bytes} -> (case2is_patch::case->bool) -> (original_file_bytes, [patch_file_bytes]{not reversed})
    #'''
    ls = []
    for case, either_bytes in reversed_case_either_bytes_pairs:
        if case2is_patch(case):
            patch_file_bytes = either_bytes
            ls.append(patch_file_bytes)
        else:
            original_file_bytes = either_bytes
            break
    else:
        raise ValueError('not contains original_file_bytes')
    original_file_bytes
    ls.reverse()
    ordered_patch_file_bytes_ls = ls
    return (original_file_bytes, ordered_patch_file_bytes_ls)

def reversed_case_either_bytes_pairs2latest_file_bytes(reversed_case_either_bytes_pairs, *, case2is_patch, init, patch):
    r'''Iter<(case, either_bytes=patch_file_bytes if case2is_patch(case) else original_file_bytes)>{latest bytes come first, contains original_file_bytes} -> (case2is_patch::case->bool) -> (init::original_file_bytes->result_obj) -> (patch::old_result_obj->patch_file_bytes->new_result_obj) -> latest_result_obj
    #'''
    (original_file_bytes, ordered_patch_file_bytes_ls) = reversed_case_either_bytes_pairs2original_file_bytes_ordered_patch_file_bytes_ls_pair(reversed_case_either_bytes_pairs, case2is_patch=case2is_patch)

    result_obj = init(original_file_bytes)
    for patch_file_bytes in ordered_patch_file_bytes_ls:
        old_result_obj = result_obj
        new_result_obj = patch(old_result_obj, patch_file_bytes)
        result_obj = new_result_obj
    latest_result_obj = result_obj
    return latest_result_obj





def check_fsys_patch_dict(fsys_patch_dict):
    'fsys_patch_dict = dict<basename, (fsys_patch_dict|patch_idx|None|src_relative_path__str)>'
    may_mapping_types_or_check_mapping_type = mapping_types_or_check_mapping_type
    check_mapping_type = may_mapping_types_or_check_mapping_type2check_mapping_type(may_mapping_types_or_check_mapping_type, _check_mapping_type__dict)

    v = Visit__fsys_patch_mapping4func(check_mapping_type=check_mapping_type, on_fsys_mapping_ex_enter=None, on_fsys_mapping_ex_exit=None, on_patch_idx=None, on_remove=None, on_copy_from_internal=None)
    v.visit()#check inside


def check_fsys_dict_or_patch_idx(fsys_dict_or_patch_idx):
    check_fsys_mapping_or_patch_idx(fsys_dict_or_patch_idx, _check_mapping_type__dict)
    return
def check_fsys_mapping_or_patch_idx(fsys_mapping_or_patch_idx, /, may_mapping_types_or_check_mapping_type):
    if type(fsys_mapping_or_patch_idx) is int:
        patch_idx = fsys_mapping_or_patch_idx
        if not patch_idx >= 0: raise ValueError
    else:
        fsys_mapping = fsys_mapping_or_patch_idx
        check_fsys_mapping(fsys_mapping, may_mapping_types_or_check_mapping_type)

TODO rename Visit__fsys_mapping: as Visit__fsys_mapping





r'''
class _Visit__fsys_mapping4fsys_dict_merge(_Visit__fsys_patch_mapping4fsys_dict_patch):
    'used by fsys_dict_or_patch_idx_merge internally'
    @override#change API!!!
    #def visit(sf, /,*, valueonly_fsys_patch_mapping):
    def visit(sf, /,*, valueonly_fsys_mapping):
        check_valueonly_fsys_mapping(valueonly_fsys_mapping)
        # valueonly_fsys_mapping <: valueonly_fsys_patch_mapping
        valueonly_fsys_patch_mapping = valueonly_fsys_mapping
        super().visit(valueonly_fsys_patch_mapping=valueonly_fsys_patch_mapping)
r'''

TODO
    rename dict -> mapping
        now pass _Visit__fsys_patch_mapping4fsys_dict_patch

def copy_fsys_dict_or_patch_idx(fsys_dict_or_patch_idx):
    check_fsys_dict_or_patch_idx(fsys_dict_or_patch_idx)
    return copy.deepcopy(fsys_dict_or_patch_idx)
def copy_fsys_dict(fsys_dict):
    'vs:copy_fsys_dict/deepcopy_fsys_mapping_as_fsys_dict'
    check_fsys_dict(fsys_dict)
    return copy.deepcopy(fsys_dict)





r'''
fsys_update_cmd__is__branch_history_cmd = False
    #TODO here: support both on-fly
    # put into IRepositorySetting
    #fsys_delta = fsys_update_cmd | branch_history_cmd
def read_fsys_obj__bytes(bs):
    'bytes -> fsys_obj'
    if fsys_update_cmd__is__branch_history_cmd:
        ###
        # fsys_update_cmd == branch_history_cmd
        patch_file_bytes = original_file_bytes = bs

        old_fsys_obj = FileSystem4update()
        new_fsys_obj = fsys_patch(old_fsys_obj, patch_file_bytes)
        return new_fsys_obj

    else:
        ###
        # fsys_update_cmd != branch_history_cmd
        s = bs.decode('utf8')
        fsys_dict = ast.literal_eval(s)
        check_fsys_dict(fsys_dict)
        fsys_obj = FileSystem4update(fsys_dict)
        return fsys_obj
#'''

r'''
def fsys_patch(old_fsys_obj, patch_file_bytes, /):
    'old_fsys_obj -> patch_file_bytes -> new_fsys_obj'
    if fsys_update_cmd__is__branch_history_cmd:
        ###
        # fsys_update_cmd == branch_history_cmd
        s = patch_file_bytes.decode('utf8')
        branch_history_cmds = ast.literal_eval(s)
        if type(branch_history_cmds) is not tuple:raise TypeError
        for branch_history_cmd in branch_history_cmds:
            if type(branch_history_cmd) is not tuple:raise TypeError
            if not branch_history_cmd: raise TypeError
            if type(branch_history_cmd[0]) is not str:raise TypeError
        for branch_history_cmd in branch_history_cmds:
            old_fsys_obj.exec_branch_history_cmd(branch_history_cmd)
        new_fsys_obj = old_fsys_obj
        return new_fsys_obj
    else:
        ###
        # fsys_update_cmd != branch_history_cmd
        s = patch_file_bytes.decode('utf8')
        fsys_update_cmds = ast.literal_eval(s)
        if type(fsys_update_cmds) is not tuple:raise TypeError
        for fsys_update_cmd in fsys_update_cmds:
            if type(fsys_update_cmd) is not tuple:raise TypeError
            if not fsys_update_cmd: raise TypeError
            if type(fsys_update_cmd[0]) is not str:raise TypeError
        for fsys_update_cmd in fsys_update_cmds:
            old_fsys_obj.exec_fsys_update_cmd(fsys_update_cmd)
        new_fsys_obj = old_fsys_obj
        return new_fsys_obj
#'''




#HHHHH
def mk_fsys_dict_view_or_patch_idx(fsys_mapping_or_patch_idx):
    if type(fsys_mapping_or_patch_idx) is int:
        patch_idx = fsys_mapping_or_patch_idx
        fsys_dict_view_or_patch_idx = patch_idx
    else:
        fsys_mapping = fsys_mapping_or_patch_idx
        fsys_mapping_ex_view = mk_fsys_mapping_view(fsys_mapping)
        fsys_dict_view_or_patch_idx = fsys_mapping_ex_view
    fsys_dict_view_or_patch_idx

    return fsys_dict_view_or_patch_idx


TODO
    using FrozenDict instead of RecurView__fsys_mapping_ex

    mk_fsys_dict_view/mk_fsys_dict_view_or_patch_idx call with is_valueonly
    RecurView__fsys_mapping_ex[] set is_valueonly
    mk RecurView__fsys_patch_dict
    check input valueonly arg is indeed valueonly
    visit
        .check pseudo_virtual_file_reprobj
        rename on_error -> on_unknown_case
    on_copy_from_internal
        on_copy_from_internal__no_overwrite
        ...
        add src_relative_path__str
            beside src_relative_path
            or assert src_relative_path.as_posix()==src_relative_path__str
            or assert PurePosixPath('').as_posix()==''




r'''
see: deepcopy_fsys_mapping_ex(fsys_mapping_ex, /, pseudo_virtual_file_reprobj_checker_clss):
def deepcopy_fsys_mapping_as_fsys_dict(fsys_mapping, /):
    'vs:copy_fsys_dict/deepcopy_fsys_mapping_as_fsys_dict'
    #check_fsys_mapping(fsys_mapping)
    fsys_dict = deepcopy_fsys_mapping_ex_as_fsys_dict_ex(fsys_mapping, [pseudo_virtual_file_reprobj_checker_cls4fsys_mapping])
    return fsys_dict
def deepcopy_fsys_mapping_ex_as_fsys_dict_ex(fsys_mapping_ex, /, pseudo_virtual_file_reprobj_checker_clss):
    pseudo_virtual_file_reprobj_checker_clss = itertools.chain([pseudo_virtual_file_reprobj_checker_cls4fsys_mapping_ex], pseudo_virtual_file_reprobj_checker_clss)
    may_mapping_types_or_check_mapping_type = None
    v = _Visit__fsys_mapping_ex4deepcopy_fsys_mapping_ex_as_fsys_dict_ex(may_mapping_types_or_check_mapping_type, pseudo_virtual_file_reprobj_checker_clss)
    v.visit(fsys_mapping_ex)
    [fsys_dict_ex] = v.fsys_dict_exs
    return fsys_dict_ex

class _Visit__fsys_mapping_ex4deepcopy_fsys_mapping_ex_as_fsys_dict_ex(Visit__fsys_mapping_ex):
    'deepcopy_fsys_mapping_ex_as_fsys_dict_ex/deepcopy_fsys_mapping_as_fsys_dict/...'
    def __init__(sf, /, may_mapping_types_or_check_mapping_type, pseudo_virtual_file_reprobj_checker_clss):
        sf.fsys_dict_exs = [{}]
        sf._check_mapping_type = may_mapping_types_or_check_mapping_type2check_mapping_type(may_mapping_types_or_check_mapping_type, _check_mapping_type__do_nothing)
        sf.__checker_cls_set = {pseudo_virtual_file_reprobj_checker_cls4fsys_mapping_ex, *pseudo_virtual_file_reprobj_checker_clss}

    @override
    def check_mapping_type(sf, mapping_type):
        sf._check_mapping_type(mapping_type)

    @override
    def on_fsys_mapping_ex_enter(sf, ancestors_view, fsys_mapping_ex):
        '-> to_skip::bool # if to_skip then not enter and not call on_fsys_mapping_ex_exit'
        if ancestors_view:
            basename = ancestors_view[-1]
            child_fsys_dict = {}
            sf.fsys_dict_exs[-1][basename] = child_fsys_dict
            sf.fsys_dict_exs.append(child_fsys_dict)
        return False
    @override
    def on_fsys_mapping_ex_exit(sf, ancestors_view, fsys_mapping_ex):
        if ancestors_view:
            sf.fsys_dict_exs.pop()
        ''
    @override
    def on_pseudo_virtual_file_reprobj(sf, ancestors_view, basename, pseudo_virtual_file_reprobj):
        check_pseudo_virtual_file_reprobj__by_checker_cls_set(sf.__checker_cls_set, pseudo_virtual_file_reprobj)
        sf.fsys_dict_exs[-1][basename] = pseudo_virtual_file_reprobj
        ''
#'''

def check_pseudo_virtual_file_reprobj__by_checker_cls_set(checker_clss, pseudo_virtual_file_reprobj):
    for checker_cls in checker_clss:
        checker_cls.check(pseudo_virtual_file_reprobj)

TODO deepcopy_fsys_mapping_ex_as_fsys_dict_ex
    Visit__fsys_mapping_ex
        check pseudo_virtual_file_reprobj
        get pseudo_virtual_file_reprobj_checker_clss
#RecurView__fsys_dict
#RecurView__fsys_mapping
#RecurView__fsys_mapping_ex
useless
class RecurView__fsys_mapping_ex(Mapping):
    def deepcopy_as_fsys_dict_ex(sf, /):
        return deepcopy_fsys_mapping_ex_as_fsys_dict_ex(sf, None, [])
        return deepcopy_fsys_mapping_as_fsys_dict(sf)
        return deepcopy_fsys_mapping_as_fsys_dict(sf.__d)

    def update_pseudo_virtual_file_reprobj_checker_clss(sf, pseudo_virtual_file_reprobj_checker_clss, /,*, force:bool):
        if not type(force) is bool: raise TypeError
        checker_cls_set = set(pseudo_virtual_file_reprobj_checker_clss)
        if checker_cls_set <= sf.__checker_cls_set:
            pass
        elif force:
            sf.__checker_cls_set |= checker_cls_set
        elif not checker_cls_set <= sf.__checker_cls_set and not force: raise ValueError
        else:
            raise logic-err
    def turn_on_valueonly(sf, /,*, force:bool):
        'cannot/should be turnoff.since some value depend on the immutable property'
        if not type(force) is bool: raise TypeError
        if sf.__is_valueonly:
            pass
        elif force:
            sf.__is_valueonly = True
        elif not sf.__is_valueonly and not force: raise ValueError
        else:
            raise logic-err

    def __init__(sf, fsys_mapping_ex, is_valueonly:bool, pseudo_virtual_file_reprobj_checker_clss, /):
        #if type(fsys_dict) is not dict:raise TypeError
        if not isinstance(fsys_mapping_ex, Mapping):raise TypeError
        if isinstance(fsys_mapping_ex, RecurView__fsys_mapping_ex):raise TypeError('use mk_fsys_mapping_view instead of directly calling RecurView__fsys_mapping_ex')
        if not type(is_valueonly) is bool: raise TypeError

        sf.__d = fsys_mapping_ex
        sf.__is_valueonly = is_valueonly
        sf.__checker_cls_set = {pseudo_virtual_file_reprobj_checker_cls4fsys_mapping_ex, *pseudo_virtual_file_reprobj_checker_clss}

    def is_valueonly(sf):
        return sf.__is_valueonly
    def iter_pseudo_virtual_file_reprobj_checker_clss(sf):
        return iter(sf.__checker_cls_set)

    def __getitem__(sf, basename):
        fsys_mapping_ex_or_pseudo_virtual_file_reprobj = sf.__d[basename]
        if isinstance(fsys_mapping_ex_or_pseudo_virtual_file_reprobj, Mapping):
            fsys_mapping_ex = fsys_mapping_ex_or_pseudo_virtual_file_reprobj
            #return __class__(fsys_mapping_ex, sf.is_valueonly())
            return mk_fsys_mapping_view(fsys_mapping_ex, iter(sf.__checker_cls_set), is_valueonly=sf.is_valueonly())
        else:
            pseudo_virtual_file_reprobj = fsys_mapping_ex_or_pseudo_virtual_file_reprobj
            check_pseudo_virtual_file_reprobj__by_checker_cls_set(sf.__checker_cls_set, pseudo_virtual_file_reprobj)
            #hashable & immutable
            return pseudo_virtual_file_reprobj
    def __iter__(sf):
        return iter(sf.__d)
    def __len__(sf):
        return len(sf.__d)

#mk_fsys_dict_view
#mk_fsys_mapping_view
def mk_fsys_mapping_view(fsys_mapping, /,*, is_valueonly:bool, force:bool=False):
    fsys_mapping_view = mk_fsys_mapping_ex_view(fsys_mapping, [pseudo_virtual_file_reprobj_checker_cls4fsys_mapping_ex, pseudo_virtual_file_reprobj_checker_cls4fsys_patch_mapping, pseudo_virtual_file_reprobj_checker_cls4fsys_mapping], is_valueonly=is_valueonly, force=force)
    return fsys_mapping_view

def mk_fsys_patch_mapping_view(fsys_patch_mapping, /,*, is_valueonly:bool, force:bool=False):
    fsys_patch_mapping_view = mk_fsys_mapping_ex_view(fsys_patch_mapping, [pseudo_virtual_file_reprobj_checker_cls4fsys_mapping_ex, pseudo_virtual_file_reprobj_checker_cls4fsys_patch_mapping], is_valueonly=is_valueonly, force=force)
    return fsys_patch_mapping_view

def mk_fsys_mapping_ex_view(fsys_mapping_ex, pseudo_virtual_file_reprobj_checker_clss, /,*, is_valueonly:bool, force:bool=False):
    '-> fsys_mapping_ex_view'
    if not isinstance(fsys_mapping_ex, Mapping):raise TypeError
    if not type(is_valueonly) is bool: raise TypeError
    if not type(force) is bool: raise TypeError

    if isinstance(fsys_mapping_ex, RecurView__fsys_mapping_ex):
        fsys_mapping_ex_view = fsys_mapping_ex
        if not (force or not is_valueonly or fsys_mapping_ex_view.is_valueonly()): raise ValueError
        fsys_mapping_ex_view.update_pseudo_virtual_file_reprobj_checker_clss(pseudo_virtual_file_reprobj_checker_clss, force=force)
            # may raise
        try:
            #protected by above: if not (force or not is_valueonly or fsys_mapping_ex_view.is_valueonly()): raise ValueError
            #   shouldnot raise
            if is_valueonly:
                fsys_mapping_ex_view.turn_on_valueonly(force=force)
        except:
            raise logic-err


    else:
        fsys_mapping_ex_view = RecurView__fsys_mapping_ex(fsys_mapping_ex, is_valueonly, pseudo_virtual_file_reprobj_checker_clss)
    fsys_mapping_ex_view

    return fsys_mapping_ex_view





get_tmay_sub_fsys_mapping_or_patch_idx
get_tmay_sub_fsys_dict_or_patch_idx


removing code here
#HHHHH











r'''
IDirViewer
    fsys_dict
IPseudoFile4MkIsSameFile
IAccessFile4MkIsSameFile
    fsys_dict
    IRepositorySetting
ast.literal_eval('...')
#'''



#HHHHH
r'''
class AccessPath__fsys_dict:
    def access_path(sf, root_fsys_dict_or_patch_idx, relative_path:'PurePosixPath&not is_absolute()'):
        assert not relative_path.is_absolute()
        m = get_tmay_sub_fsys_dict_or_patch_idx(root_fsys_dict_or_patch_idx, relative_path)
        if not m:
            sf.on_not_exists(root_fsys_dict_or_patch_idx, relative_path)
        else:
            [sub_fsys_dict_or_patch_idx] = m
            if type(sub_fsys_dict_or_patch_idx) is int:
                sub_patch_idx = sub_fsys_dict_or_patch_idx
                sf.on_is_file(root_fsys_dict_or_patch_idx, relative_path, sub_patch_idx)
            else:
                sub_fsys_dict = sub_fsys_dict_or_patch_idx
                sf.on_is_dir(root_fsys_dict_or_patch_idx, relative_path, sub_fsys_dict)

    def on_not_exists(sf, root_fsys_dict_or_patch_idx, relative_path):
        raise FileNotFoundError
    def on_is_file(sf, root_fsys_dict_or_patch_idx, relative_path, sub_patch_idx):
        raise NotADirectoryError
    def on_is_dir(sf, root_fsys_dict_or_patch_idx, relative_path, sub_fsys_dict):
        raise IsADirectoryError

class AccessPath__fsys_dict4func(AccessPath__fsys_dict):
    def __init__(sf, /,*, on_not_exists, on_is_file, on_is_dir):
        if on_not_exists is not None:
            sf.on_not_exists = on_not_exists
        if on_is_file is not None:
            sf.on_is_file = on_is_file
        if on_is_dir is not None:
            sf.on_is_dir = on_is_dir
#'''


#'''
TODO here
IRepositorySetting__user_data_dir_path
dir_cmp__relative result -> make commit [fsys_delta]
    one fsys_update_cmd
    seq branch_history_cmd
    make patch file & rollback commit at fail #double save
    may_ignorefile_relative_path
    [ignorefile_relative_path]
        relative_to working_root_dir
        these file themself should never be ignored
        ignore = any(ignores)
        since any([])==False==default
    updating_root_dir_path
        clean first before do anything

        file_stack_inf_dir for [patch file] & delta command_history & delta branch fsys
            push
            pop - move to
        move command TODO_list4move_cmd
            search until first unpop yet file to move or mid-dir to del
            or rollback
        commit_completed? file
            if commit_completed:
                then recover with continue updating
            else recover with clean updating i.e. rollback/cancel incomplete commit
    repository_init
        mkdir for ...
#'''


#HHHHH
if __name__ == '__main__':
    from seed.helper.print_global_names import print_global_names
    print_global_names(globals())



#HHHHH
