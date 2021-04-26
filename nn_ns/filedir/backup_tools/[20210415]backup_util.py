
#HHHHH
r'''
backup_util
py -m nn_ns.filedir.backup_util

see:
    nn_ns.filedir.dir_cmp
        py::filecmp.dircmp/cmp/cmpfiles
    nn_ns.filedir.file_cmp #diff/patch/delta, O(n)
        py::difflib.restore/context_diff/Differ.compare/ndiff/unified_diff/diff_bytes
            O(n^2)
    nn_ns.filedir.inf_dir
    nn_ns.filedir.backup_util



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



































#HHHHH

from nn_ns.filedir.dir_cmp import dir_cmp, dir_cmp__relative, path2str, path2str4dir_cmp_result, DirViewer__fsys, is_same_file__True, MkIsSameFile, AccessFile4MkIsSameFile__fsys
from nn_ns.filedir.dir_cmp import IDirViewer, IPseudoFile4MkIsSameFile, IAccessFile4MkIsSameFile
from nn_ns.filedir.dir_cmp import to_std_onoff_patterns_list, onoff_patterns_list2ignore_str, read_ignorefile, iter_read_ignorefile, read_ignorefile__text, write_ignorefile, write_ignorefile__text



from nn_ns.filedir.file_cmp import uints_diff, bytes_diff, file_diff
from nn_ns.filedir.file_cmp import uints_patch, bytes_patch, file_patch
from nn_ns.filedir.file_cmp import mk_patch_uints, mk_patch_uints__iter, check_result4uints_diff, pack__patch_bytes_ex__ver1
from nn_ns.filedir.file_cmp import uints_patch__iter, unpack__patch_bytes_ex__ver1



from nn_ns.filedir.inf_dir import inf_dir_idx2user_data_uint_relative_path, inf_dir_user_data_uint_relative_path2idx
from nn_ns.filedir.inf_dir import move_and_push_into_inf_dir, copy_and_push_into_inf_dir, pop_from_inf_dir_and_move, pop_from_inf_dir_and_push_into_another, inf_dir_remove_tail_empty_dirs, len_inf_dir, inf_dir_end_based_idx2user_data_path_ex
from nn_ns.filedir.inf_dir import bisearch_child_end, len_finite_dir_or_file, inf_dir_idx2user_data_relative_path, inf_dir_end_based_idx2user_data_relative_path_ex, inf_dir_end_based_idx2begin_based_idx
from nn_ns.filedir.inf_dir import open_under_inf_dir, mk_target_path_under_inf_dir


#


from nn_ns.filedir.relative_path_ops import relative_path_ops, check_relative_path, is_relative_path_empty, relative_path2parts, empty_relative_path, str2relative_path, relative_path2str, check_relative_path__str
    #relative_path2parts: avoid relative_path.parts
    #check_relative_path__str/str2relative_path/relative_path2str: avoid non-std relative_path__str



import itertools
import re
import shutil
import ast
from collections.abc import Mapping
import copy
from pathlib import Path, PurePosixPath
import os.path
import io
from abc import ABC, abstractmethod
from seed.abc.abc import override





from seed.tiny import echo, fst
from seed.types.view.SeqSliceView import SeqSliceView
from seed.types.view.SeqTransformView import SeqTransformView
#from seed.for_libs.for_io.stream_obj_converter import stream_obj2stream_type_name, is_stream_text, is_stream_buffered_binary, is_stream_raw_binary, stream_obj2text_stream_obj, binary_stream_obj2text_stream_obj, buffered_binary_stream_obj2text_stream_obj, binary_stream_obj2buffered_binary_stream_obj, raw_binary_stream_obj2buffered_binary_stream_obj
from seed.for_libs.for_io.stream_obj_converter import binary_stream_obj2text_stream_obj

from seed.seq_tools.is_prefix_of_seq import is_prefix_of_seq, is_suffix_of_seq

from seed.helper.check.checkers import checks, checkers, check_funcs
from seed.helper.check.checkers import check_uint_imay, check_uint, check_all, check_str, check_int, check_tuple















#HHHHH

#def read_imay_parent__user_data(parent_path):
#       see:user_data_dir_path_setting.read_imay_parent_idx
def _read_imay_parent__user_data(parent_path):
    '-> [-1..] # imay'
    s = parent_path.read_text(encoding='ascii')
    imay_parent_idx = ast.literal_eval(s)
    check_uint_imay(imay_parent_idx)
    return imay_parent_idx



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
def inf_dir_idx2iter_imay_parent_idx_content_bytes_pairs__inf_dir_as_forest(inf_dir_path, inf_dir_idx, /, *, dir_size, user_data_dir_path_setting):
    'inf_dir_path -> uint -> Iter<([-1..], content_bytes)>{nonempty, endby imay_parent_idx==-1}'
    def content_path2bytes(content_path):
        content_bytes = content_path.read_bytes()
        return content_bytes
    return inf_dir_idx2iter_imay_parent_idx_content_path_pairs__inf_dir_as_forest(inf_dir_path, inf_dir_idx, dir_size=dir_size, content_path2value=content_path2bytes, user_data_dir_path_setting=user_data_dir_path_setting)

def case2is_patch__case_is_imay_parent_idx(case):
    imay_parent_idx = case
    return imay_parent_idx == -1

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


def reversed_case_either_bytes_pairs2latest_file_bytes__forest__file_cmp__ver1(reversed_case_either_bytes_pairs, *, case2is_patch):
    'see:reversed_case_either_bytes_pairs2latest_file_bytes'
    def patch(old_file_bytes, patch_file_bytes, /):
        patch_bytes_ex = patch_file_bytes
        return file_patch(old_file_bytes, patch_bytes_ex, ver=1)
    return reversed_case_either_bytes_pairs2latest_file_bytes(reversed_case_either_bytes_pairs, case2is_patch=case2is_patch, init=echo, patch=patch)

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





def _mk_check_mapping_type__mapping_types(mapping_types):
    'for may_mapping_types_or_check_mapping_type2check_mapping_type'
    def check_mapping_type(mapping_type, /):
        if not mapping_type in mapping_types: raise TypeError
    return check_mapping_type__mapping_types
def _check_mapping_type__dict(mapping_type):
    'for may_mapping_types_or_check_mapping_type2check_mapping_type.default'
    if mapping_type is not dict: raise TypeError
def _check_mapping_type__do_nothing(mapping_type):
    'for may_mapping_types_or_check_mapping_type2check_mapping_type.default'
    pass#return
def may_mapping_types_or_check_mapping_type2check_mapping_type(may_mapping_types_or_check_mapping_type, /, default):
    'see:_check_mapping_type__do_nothing/check_fsys_mapping'
    if may_mapping_types_or_check_mapping_type is None:
        #mapping_types_or_check_mapping_type = (dict,)
        mapping_types_or_check_mapping_type = default
    else:
        mapping_types_or_check_mapping_type = may_mapping_types_or_check_mapping_type

    if callable(mapping_types_or_check_mapping_type):
        check_mapping_type = mapping_types_or_check_mapping_type
    else:
        mapping_types = mapping_types_or_check_mapping_type
        check_mapping_type = _mk_check_mapping_type__mapping_types(mapping_types)
    check_mapping_type
    return check_mapping_type

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

def check_fsys_dict(fsys_dict):
    'fsys_dict = dict<basename, (fsys_dict|patch_idx)>'
    check_fsys_mapping(fsys_dict, _check_mapping_type__dict)
    return
def check_fsys_mapping(fsys_mapping, /, may_mapping_types_or_check_mapping_type):
    check_mapping_type = may_mapping_types_or_check_mapping_type2check_mapping_type(may_mapping_types_or_check_mapping_type, _check_mapping_type__do_nothing)

    v = Visit__fsys_mapping4func(check_mapping_type=check_mapping_type, on_fsys_mapping_ex_enter=None, on_fsys_mapping_ex_exit=None, on_patch_idx=None)
    v.visit()#check inside



#HHHHH
#Visit__fsys_patch_mapping
#Visit__fsys_mapping
class Visit__fsys_mapping_ex:
  r'''
    fsys_mapping_ex
        fsys_dict_ex
        fsys_mapping_ex_view
            readonly_fsys_mapping_ex
            valueonly_fsys_mapping_ex

        fsys_patch_mapping
            fsys_patch_dict
            fsys_patch_mapping_view
                readonly_fsys_patch_mapping
                valueonly_fsys_patch_mapping

            fsys_mapping
                fsys_dict
                fsys_mapping_view

                    readonly_fsys_mapping
                    valueonly_fsys_mapping

    fsys_mapping_ex = Mapping<basename, (fsys_mapping|pseudo_virtual_file_reprobj)>
        pseudo_virtual_file_reprobj :: immutable & hashable & not Mapping

    fsys_mapping = Mapping<basename, (patch_idx|fsys_mapping)>
    fsys_mapping = fsys_mapping_ex<pseudo_virtual_file_reprobj=patch_idx>
        patch_idx::uint
            - ref to file content

    fsys_patch_mapping = fsys_mapping_ex<pseudo_virtual_file_reprobj=(patch_idx|None|relative_path__str)>
        relative_path__str :: str
            .as_posix() of relative_path :: relative PurePosixPath
            use:
                check_relative_path__str
                str2relative_path
                relative_path2str
            - src of copy/move
        None
            - remove

    fsys_mapping_ex_view = RecurView__fsys_mapping_ex(fsys_mapping)
    readonly_fsys_mapping_ex = fsys_mapping_ex_view
    valueonly_fsys_mapping_ex = fsys_mapping_ex_view +is_valueonly

    fsys_dict = dict<basename, (patch_idx|fsys_dict)>

    readonly vs valueonly
        readonly
            * immutable/frozen/value
            * view
                underlying obj may be changed
        valueonly
            * immutable/frozen/value
            * view
                underlying obj shouldnot be changed
                NOTE: subobj not changed, but subview to subobj can be diff objs
  #'''
    def check_mapping_type(sf, mapping_type, /):
        return
    #on_fsys_mapping_enter
    #on_fsys_mapping_ex_enter
    def on_fsys_mapping_ex_enter(sf, ancestors_view, fsys_mapping_ex, /):
        '-> to_skip::bool # if to_skip then not enter and not call on_fsys_mapping_ex_exit'
        return False
    #on_fsys_mapping_exit
    #on_fsys_mapping_ex_exit
    def on_fsys_mapping_ex_exit(sf, ancestors_view, fsys_mapping_ex, /):
        ''
    #def on_patch_idx(sf, ancestors_view, basename, patch_idx):
    #def on_error__at_fsys_dict(sf, ancestors_view, obj, exc): raise exc
    # on_error__at_XXX with exc -->> on_unknown_case__at_XXX without exc
    def on_pseudo_virtual_file_reprobj(sf, ancestors_view, basename, pseudo_virtual_file_reprobj):
        ''
    def visit(sf, fsys_mapping_ex, /):
      if not isinstance(fsys_mapping_ex, Mapping):raise TypeError

      def recur(ancestors, fsys_mapping_ex):
        sf.check_mapping_type(type(fsys_mapping_ex))

        to_skip = sf.on_fsys_mapping_ex_enter(ancestors_view, fsys_mapping_ex)
        if type(to_skip) is not bool: raise TypeError
        if to_skip: return # without sf.on_fsys_mapping_ex_exit()
        for basename in fsys_mapping_ex:
            if type(basename) is not str:raise TypeError
        for basename, fsys_mapping_ex_or_pseudo_virtual_file_reprobj in fsys_mapping_ex.items():
            if isinstance(fsys_mapping_ex_or_pseudo_virtual_file_reprobj, Mapping):
                fsys_mapping_ex = fsys_mapping_ex_or_pseudo_virtual_file_reprobj
                ancestors.append(basename)
                recur(fsys_mapping_ex)
                ancestors.pop()
            else:
                pseudo_virtual_file_reprobj = fsys_mapping_ex_or_pseudo_virtual_file_reprobj
                if not pseudo_virtual_file_reprobj >= 0: raise ValueError
                sf.on_pseudo_virtual_file_reprobj(ancestors_view, basename, pseudo_virtual_file_reprobj)
        sf.on_fsys_mapping_ex_exit(ancestors_view, fsys_mapping_ex)
        #end recur()

      ancestors = []
      ancestors_view = SeqTransformView(None, ancestors)
      recur(ancestors, fsys_mapping_ex)
      return None


#HHHHH
class Visit__fsys_mapping(Visit__fsys_mapping_ex):
    def on_patch_idx(sf, ancestors_view, basename, patch_idx):
        ''
    def on_unknown_case__at_fsys_mapping(sf, ancestors_view, basename, pseudo_virtual_file_reprobj):
        ''
        raise TypeError
    @override
    def on_pseudo_virtual_file_reprobj(sf, ancestors_view, basename, pseudo_virtual_file_reprobj):
        x = pseudo_virtual_file_reprobj
        if type(x) is int:
            patch_idx = x
            if not patch_idx >= 0: raise ValueError
            sf.on_patch_idx(ancestors_view, basename, patch_idx)
        else:
            sf.on_unknown_case__at_fsys_mapping(ancestors_view, basename, pseudo_virtual_file_reprobj)
            return
        return


class Visit__fsys_patch_mapping(Visit__fsys_mapping_ex):
    def on_patch_idx(sf, ancestors_view, basename, patch_idx):
        ''
    def on_remove(sf, ancestors_view, basename):
        ''
    def on_copy_from_internal(sf, ancestors_view, basename, src_relative_path):
        'relative_path2str/str2relative_path/check_relative_path__str'
    def on_unknown_case__at_fsys_patch_mapping(sf, ancestors_view, basename, pseudo_virtual_file_reprobj):
        ''
        raise TypeError

    @override
    def on_pseudo_virtual_file_reprobj(sf, ancestors_view, basename, pseudo_virtual_file_reprobj):
        x = pseudo_virtual_file_reprobj
        if x is None:
            #remove
            pass
            sf.on_remove(ancestors_view, basename)
        elif type(x) is int:
            patch_idx = x
            if not patch_idx >= 0: raise ValueError
            sf.on_patch_idx(ancestors_view, basename, patch_idx)
        elif type(x) is str:
            #copy from
            #not: copy/move from!!!
            #as_posix
            src_relative_path__str = x
            src_relative_path = str2relative_path(src_relative_path__str)
            if not src_relative_path.as_posix() == src_relative_path__str: raise logic-err
                #to recover src_relative_path__str
            #check_relative_path(src_relative_path__str)
            #check_relative_path__str(src_relative_path)
            if 0:
                #since not merge inplace, old/new are diff, src/dst has no limits
                src_relative_path_parts = relative_path2parts(src_relative_path)
                    #tuple
                dst_relative_path_parts = ancestors
                    #list
                if is_prefix_of_seq(src_relative_path_parts, dst_relative_path_parts): raise ValueError
            sf.on_copy_from_internal(ancestors_view, basename, src_relative_path)
        else:
            sf.on_unknown_case__at_fsys_patch_mapping(ancestors_view, basename, pseudo_virtual_file_reprobj)
            return
        return


    r'''
    def on_error__at_fsys_dict(sf, ancestors_view, obj, exc):
        ''
        if not ancestors_view:
            raise exc
        saved_ancestors_view = ancestors_view

        basename = saved_ancestors_view[-1]
        ancestors = ancestors_view = SeqSliceView(saved_ancestors_view, None)[:-1]

        x = obj
        if x is None:
        ... code moved to on_pseudo_virtual_file_reprobj
        else:
            sf.on_error__at_fsys_dict(saved_ancestors_view, obj, exc)
            return
        return
    def on_error__at_fsys_patch_dict(sf, ancestors_view, obj, exc):
        ''
        raise exc
    #'''


def _set_if_not_None(sf, locals, excludes):
    #_set_if_not_None(sf, locals(), 'sf'.split())
    if type(excludes) is str: raise TypeError
    excludes = set(excludes)
    d = {**locals}
    for nm, val in d.items():
        if val is not None:
            setattr(sf, nm, val)
class Visit__fsys_mapping4func(Visit__fsys_mapping):
    def __init__(sf, /,*, check_mapping_type, on_fsys_mapping_ex_enter, on_fsys_mapping_ex_exit, on_patch_idx, on_unknown_case__at_fsys_mapping):
        _set_if_not_None(sf, locals(), 'sf'.split())

class Visit__fsys_patch_mapping4func(Visit__fsys_mapping4func, Visit__fsys_patch_mapping):
    def __init__(sf, /,*, check_mapping_type, on_fsys_mapping_ex_enter, on_fsys_mapping_ex_exit, on_patch_idx, on_remove, on_copy_from_internal, on_unknown_case__at_fsys_patch_mapping):
        _set_if_not_None(sf, locals(), 'sf'.split())

#HHHHH
class _Visit__fsys_patch_mapping4fsys_dict_patch(Visit__fsys_patch_mapping):
    r'''
    used by fsys_dict_patch/fsys_dict_or_patch_idx_merge internally
        get_new_fsys_mapping
        mk_new_fsys_mapping(valueonly_fsys_patch_mapping)
        deepcopy_new_fsys_mapping_as_fsys_dict
        mk_new_fsys_dict(valueonly_fsys_patch_mapping)

    old_fsys_dict/sf.old_fsys_xdict is wrong named
        , should be old_valueonly_fsys_mapping
    new_fsys_dict/sf._new_fsys_dict is wrong named too
        , upper layers are dict to set item
        , but lower layers are fsys_mapping

    required:
        old_valueonly_fsys_mapping --> old_valueonly_fsys_mapping
        fsys_patch_mapping --> valueonly_fsys_patch_mapping

        #dict -> valueonly_fsys_mapping
        copy_fsys_dict_or_patch_idx(old...fsys_dict_or_patch_idx)
            mk_fsys_dict_view_or_patch_idx
            -->> mk_fsys_dict_view_or_patch_idx(old...fsys_mapping_or_patch_idx)
        copy_fsys_dict(old...fsys_dict)
            #or deepcopy_fsys_mapping_as_fsys_dict
            -->> mk_fsys_mapping_view(old...fsys_mapping)


    #xxx...src_new...yyy: from valueonly_fsys_patch_mapping
    #xxx...src_old...yyy: from old_valueonly_fsys_mapping
    #'''


    def on_inherit(sf, /, ancestors_view, basename, the_parent_old_fsys_xdict, the_src_old_fsys_xdict_or_patch_idx):
        ''
    def on_remove__dir_or_file(sf, /, ancestors_view, basename, the_parent_old_fsys_xdict, the_removed_old_fsys_xdict_or_patch_idx):
        ''
    def on_copy_from_internal__no_overwrite(sf, /, ancestors_view, basename, src_relative_path, the_src_old_fsys_xdict_or_patch_idx, the_into_dst_old_fsys_xdict):
        ''
    #def on_copy_from_internal__overwrite_dir_or_file(sf, /, ancestors_view, basename, src_relative_path, the_src_old_fsys_xdict_or_patch_idx, the_into_dst_old_fsys_xdict, the_overwrited_old_fsys_xdict_or_patch_idx):
    #no: overwrite dir when copy dir
    def on_copy_from_internal__overwrite_dir_or_file__copy_file(sf, /, ancestors_view, basename, src_relative_path, the_src_old_patch_idx, the_into_dst_old_fsys_xdict, the_overwrited_old_fsys_xdict_or_patch_idx, *, to_overwrite_dir_or_file_by_file):
        ''
    def on_copy_from_internal__overwrite_file__copy_dir(sf, /, ancestors_view, basename, src_relative_path, the_src_old_fsys_xdict, the_into_dst_old_fsys_xdict, the_overwrited_old_patch_idx, *, to_overwrite_file_by_dir):
        ''

    #the_src_new_fsys_xdict_or_patch_idx
    #the_src_new_fsys_mapping_or_patch_idx
    def on_copy_from_external__no_overwrite(sf, /, ancestors_view, basename, the_src_new_fsys_mapping_or_patch_idx, the_into_dst_old_fsys_xdict):
        ''
    #src_new: from valueonly_fsys_patch_mapping
    #src_old: from old_valueonly_fsys_mapping

    #def on_copy_from_external__overwrite_dir_or_file(sf, /, ancestors_view, basename, the_src_new_fsys_mapping_or_patch_idx, the_into_dst_old_fsys_xdict, the_overwrited_old_fsys_xdict_or_patch_idx):
    #no: overwrite dir when copy dir
    def on_copy_from_external__overwrite_dir_or_file__copy_file(sf, /, ancestors_view, basename, the_src_new_patch_idx, the_into_dst_old_fsys_xdict, the_overwrited_old_fsys_xdict_or_patch_idx, *, to_overwrite_dir_or_file_by_file):
        ''
    #the_src_new_fsys_xdict
    #the_src_new_fsys_mapping
    def on_copy_from_external__overwrite_file__copy_dir(sf, /, ancestors_view, basename, the_src_new_fsys_mapping, the_into_dst_old_fsys_xdict, the_overwrited_old_patch_idx, *, to_overwrite_file_by_dir):
        ''


    def get_new_fsys_mapping(sf):
        new_fsys_mapping = mk_fsys_mapping_view(sf._new_fsys_dict)
        return new_fsys_mapping
    def mk_new_fsys_mapping(sf, /,*, valueonly_fsys_patch_mapping):
        sf.visit(valueonly_fsys_patch_mapping=valueonly_fsys_patch_mapping)
        new_fsys_mapping = sf.get_new_fsys_mapping()
        return new_fsys_mapping

    def deepcopy_new_fsys_mapping_as_fsys_dict(sf):
        new_fsys_mapping = sf.get_new_fsys_mapping()
        new_fsys_dict = deepcopy_fsys_mapping_as_fsys_dict(new_fsys_mapping)
        return new_fsys_dict
    def mk_new_fsys_dict(sf, /,*, valueonly_fsys_patch_mapping):
        new_fsys_mapping = sf.mk_new_fsys_mapping(valueonly_fsys_patch_mapping=valueonly_fsys_patch_mapping)
        new_fsys_dict = deepcopy_fsys_mapping_as_fsys_dict(new_fsys_mapping)
        return new_fsys_dict

    @override#change API!!!
    def visit(sf, /,*, valueonly_fsys_patch_mapping):
        super().visit(valueonly_fsys_patch_mapping)

    def __init__(sf, /,*, merge_case2skip_or_replace, old_valueonly_fsys_mapping):
        merge_case2skip_or_replace_ops
        sf.merge_case2skip_or_replace = merge_case2skip_or_replace
        sf.old_fsys_xdict = mk_fsys_mapping_view(old_valueonly_fsys_mapping)
        sf._new_fsys_dict = {}
        sf.old_fsys_xdicts = []
        sf.new_fsys_dicts = []
        sf.coping = None #copy from external
    def on_fsys_mapping_ex_enter(sf, ancestors_view, valueonly_fsys_patch_mapping):
        '-> to_skip::bool # if to_skip then not enter and not call on_fsys_mapping_ex_exit'
        if sf.coping is not None: return

        saved_ancestors_view = ancestors_view
        def copy_from_external__may_overwrite(*, overwrite:bool):
            src_fsys_mapping = valueonly_fsys_patch_mapping
            check_fsys_mapping(src_fsys_mapping, None)

            if 1:
                ancestors_view = SeqSliceView(saved_ancestors_view, None)[:-1]
                basename = saved_ancestors_view[-1]
                the_into_dst_old_fsys_xdict = sf.old_fsys_xdicts[-1]
                if overwrite:
                    #copy from external dir,  overwrite file
                    the_src_new_fsys_mapping = src_fsys_mapping
                    the_overwrited_old_patch_idx = old_this_patch_idx
                    to_overwrite_file_by_dir = sf.is_to_overwrite_file_by_dir()
                    sf.on_copy_from_external__overwrite_file__copy_dir(ancestors_view, basename, the_src_new_fsys_mapping, the_into_dst_old_fsys_xdict, the_overwrited_old_patch_idx, to_overwrite_file_by_dir=to_overwrite_file_by_dir)
                    to_copy_src = to_copy_src
                else:
                    #copy from external dir, no overwrite
                    the_src_new_fsys_mapping_or_patch_idx = src_fsys_mapping
                    sf.on_copy_from_external__no_overwrite(ancestors_view, basename, the_src_new_fsys_mapping_or_patch_idx, the_into_dst_old_fsys_xdict)
                    to_copy_src = True

            #deepcopy_fsys_mapping_as_fsys_dict -> mk_fsys_mapping_view
            #copy_fsys_dict_or_patch_idx -> mk_fsys_dict_view_or_patch_idx
            new_parent_dict[basename] = mk_fsys_mapping_view(src_fsys_mapping) if to_copy_src else mk_fsys_dict_view_or_patch_idx(the_overwrited_old_patch_idx)
            to_skip = True
            return to_skip
            sf.coping = len(ancestors_view)

        if not ancestors_view:
            sf.old_fsys_xdicts.append(sf.old_fsys_xdict)
            sf.new_fsys_dicts.append(sf._new_fsys_dict)
            to_skip = False
            return to_skip
        else:
            basename = ancestors_view[-1]

            old_parent_xdict = sf.old_fsys_xdicts[-1]
            new_parent_dict = sf.new_fsys_dicts[-1]
            if basename not in old_parent_xdict:
                #copy from external dir, no overwrite
                return copy_from_external__may_overwrite(overwrite=False)
            else:
                old_this_xdict_or_patch_idx = old_parent_xdict[basename]
                if type(old_this_xdict_or_patch_idx) is int:
                    old_this_patch_idx = old_this_xdict_or_patch_idx
                    #copy from external dir,  overwrite file
                    return copy_from_external__may_overwrite(overwrite=True)
                old_this_xdict = old_this_xdict_or_patch_idx
                new_this_dict = new_parent_dict[basename] = {}
                sf.old_fsys_xdicts.append(old_this_xdict)
                sf.new_fsys_dicts.append(new_this_dict)
                to_skip = False
                return to_skip
    def on_fsys_mapping_ex_exit(sf, ancestors_view, valueonly_fsys_patch_mapping):
        if sf.coping is not None:
            if sf.coping == len(ancestors_view):
                sf.coping = None
        else:
            old_this_xdict = sf.old_fsys_xdicts.pop()
            new_this_dict = sf.new_fsys_dicts.pop()
            #inherit from old
            inherits = set(old_parent_xdict)-set(valueonly_fsys_patch_mapping)
            if 0:
                neednot and shouldnot
                saved_ancestors_view = ancestors_view
                ancestors_view = SeqSliceView(saved_ancestors_view, None)[:-1]
                basename = saved_ancestors_view[-1]

            for basename in inherits:
                the_src_old_fsys_xdict_or_patch_idx = old_this_xdict[basename]
                if 1:
                    the_parent_old_fsys_xdict = old_this_xdict
                    sf.on_inherit(ancestors_view, basename, the_parent_old_fsys_xdict, the_src_old_fsys_xdict_or_patch_idx)

                new_this_dict[basename] = mk_fsys_dict_view_or_patch_idx(the_src_old_fsys_xdict_or_patch_idx)
        if not ancestors_view:
            sf._new_fsys_dict = mk_fsys_mapping_view(sf._new_fsys_dict, is_valueonly=True)

    def is_to_overwrite_file_by_dir(sf):
        to_overwrite_file_by_dir = merge_case2skip_or_replace_ops.is_to_overwrite_file_by_dir(sf.merge_case2skip_or_replace)
        return to_overwrite_file_by_dir

    def is_to_overwrite_dir_or_file_by_file(sf, the_overwrited_old_fsys_xdict_or_patch_idx):
        if type(the_overwrited_old_fsys_xdict_or_patch_idx) is int:
            # file := file
            to_overwrite_file_by_file = merge_case2skip_or_replace_ops.is_to_overwrite_file_by_file(sf.merge_case2skip_or_replace)
            to_overwrite_dir_or_file_by_file = to_overwrite_file_by_file
        else:
            # dir := file
            to_overwrite_dir_by_file = merge_case2skip_or_replace_ops.is_to_overwrite_dir_by_file(sf.merge_case2skip_or_replace)
            to_overwrite_dir_or_file_by_file = to_overwrite_dir_by_file

        return to_overwrite_dir_or_file_by_file

    def on_patch_idx(sf, ancestors_view, basename, patch_idx):
        if sf.coping is not None: return

        #may overwrite!
        #copy or copy&overwrite
        the_into_dst_old_fsys_xdict = sf.old_this_xdicts[-1]
        if basename in the_into_dst_old_fsys_xdict:
            #copy&overwrite
            the_overwrited_old_fsys_xdict_or_patch_idx = the_into_dst_old_fsys_xdict[basename]
            the_src_new_patch_idx = patch_idx
            to_overwrite_dir_or_file_by_file = sf.is_to_overwrite_dir_or_file_by_file(the_overwrited_old_fsys_xdict_or_patch_idx)
            sf.on_copy_from_external__overwrite_dir_or_file__copy_file(ancestors_view, basename, the_src_new_patch_idx, the_into_dst_old_fsys_xdict, the_overwrited_old_fsys_xdict_or_patch_idx, to_overwrite_dir_or_file_by_file=to_overwrite_dir_or_file_by_file)
            to_copy_src = to_overwrite_dir_or_file_by_file
        else:
            #copy, no overwrite
            the_src_new_fsys_mapping_or_patch_idx = patch_idx
            sf.on_copy_from_external__no_overwrite(ancestors_view, basename, the_src_new_fsys_mapping_or_patch_idx, the_into_dst_old_fsys_xdict)
            to_copy_src = True

        sf.new_fsys_dicts[-1][basename] = patch_idx if to_copy_src else mk_fsys_dict_view_or_patch_idx(the_overwrited_old_fsys_xdict_or_patch_idx)
    ''
    def on_remove(sf, ancestors_view, basename):
        if sf.coping is not None: raise ValueError

        the_parent_old_fsys_xdict = sf.old_fsys_xdicts[-1]

        if basename not in the_parent_old_fsys_xdict: raise ValueError('remove nothing')
        the_removed_old_fsys_xdict_or_patch_idx = the_parent_old_fsys_xdict[basename]
        # not assign to new ==>> remove

        sf.on_remove__dir_or_file(ancestors_view, basename, the_parent_old_fsys_xdict, the_removed_old_fsys_xdict_or_patch_idx)
        return
    ''
    def on_copy_from_internal(sf, ancestors_view, basename, src_relative_path):
        'relative_path2str/str2relative_path/check_relative_path__str'
        if sf.coping is not None: raise ValueError


        #copy from internal
        old_fsys_root = sf.old_fsys_xdict #root.old_fsys
        tmay_src__at_old_fsys = get_tmay_sub_fsys_xdict_or_patch_idx(old_fsys_root, src_relative_path)
        if not tmay_src__at_old_fsys:
            raise ValueError('copy from nothing')
        [src__at_old_fsys] = tmay_src__at_old_fsys
        src__at_old_fsys
        the_src_old_fsys_xdict_or_patch_idx = src__at_old_fsys

        the_into_dst_old_fsys_xdict = sf.old_fsys_xdicts[-1]

        if basename in the_into_dst_old_fsys_xdict:
            the_overwrited_old_fsys_xdict_or_patch_idx = the_into_dst_old_fsys_xdict[basename]
            if type(the_src_old_fsys_xdict_or_patch_idx) is int:
                # copy file
                to_overwrite_dir_or_file_by_file = sf.is_to_overwrite_dir_or_file_by_file(the_overwrited_old_fsys_xdict_or_patch_idx)
                the_src_old_patch_idx = the_src_old_fsys_xdict_or_patch_idx
                sf.on_copy_from_internal__overwrite_dir_or_file__copy_file(ancestors_view, basename, src_relative_path, the_src_old_patch_idx, the_into_dst_old_fsys_xdict, the_overwrited_old_fsys_xdict_or_patch_idx, to_overwrite_dir_or_file_by_file=to_overwrite_dir_or_file_by_file)
                to_copy_src = to_overwrite_dir_or_file_by_file
            else:
                # copy dir
                the_src_old_fsys_xdict = the_src_old_fsys_xdict_or_patch_idx
                if type(the_overwrited_old_fsys_xdict_or_patch_idx) is int:
                    the_overwrited_old_patch_idx = the_overwrited_old_fsys_xdict_or_patch_idx
                    to_overwrite_file_by_dir = sf.is_to_overwrite_file_by_dir()
                    sf.on_copy_from_internal__overwrite_file__copy_dir(ancestors_view, basename, src_relative_path, the_src_old_fsys_xdict, the_into_dst_old_fsys_xdict, the_overwrited_old_patch_idx, to_overwrite_file_by_dir=to_overwrite_file_by_dir)
                    to_copy_src = to_overwrite_file_by_dir
                else:
                    raise ValueError('logic-err: copy internal dir to overwrite dir')
        else:
            sf.on_copy_from_internal__no_overwrite(ancestors_view, basename, src_relative_path, the_src_old_fsys_xdict_or_patch_idx, the_into_dst_old_fsys_xdict)
            to_copy_src = True
        to_copy_src

        sf.new_fsys_dicts[-1][basename] = mk_fsys_dict_view_or_patch_idx(src__at_old_fsys) if to_copy_src else mk_fsys_dict_view_or_patch_idx(the_overwrited_old_fsys_xdict_or_patch_idx)
    ''
#end _Visit__fsys_patch_mapping4fsys_dict_patch
class _Visit__fsys_mapping4fsys_dict_merge(_Visit__fsys_patch_mapping4fsys_dict_patch):
    'used by fsys_dict_or_patch_idx_merge internally'
    @override#change API!!!
    #def visit(sf, /,*, valueonly_fsys_patch_mapping):
    def visit(sf, /,*, valueonly_fsys_mapping):
        check_valueonly_fsys_mapping(valueonly_fsys_mapping)
        # valueonly_fsys_mapping <: valueonly_fsys_patch_mapping
        valueonly_fsys_patch_mapping = valueonly_fsys_mapping
        super().visit(valueonly_fsys_patch_mapping=valueonly_fsys_patch_mapping)

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


#HHHHH
def check_valueonly_fsys_mapping(valueonly_fsys_mapping):
    if not isinstance(valueonly_fsys_mapping, RecurView__fsys_mapping_ex): raise TypeError
    if not valueonly_fsys_mapping.is_valueonly(): raise TypeError
    check_fsys_mapping(valueonly_fsys_mapping, None)

def fsys_dict_patch(old_fsys_dict, fsys_patch_dict):
    'old_fsys_dict -> fsys_patch_dict -> new_fsys_dict'
    ... ...
def fsys_mapping_patch(*, old_valueonly_fsys_mapping, valueonly_fsys_patch_mapping):
    'old_valueonly_fsys_mapping -> valueonly_fsys_patch_mapping -> new_valueonly_fsys_mapping'
    copy.deepcopy

    ... ...
    check_valueonly_fsys_mapping(old_valueonly_fsys_mapping)
    check_valueonly_fsys_patch_mapping(valueonly_fsys_patch_mapping)

    check_fsys_dict(old_fsys_dict)
    check_fsys_patch_dict(fsys_patch_dict)

    merge_case2skip_or_replace = merge_case2skip_or_replace_ops.mk_merge_case2skip_or_replace(overwrite_file_by_file=True, overwrite_file_by_dir=True, overwrite_dir_by_file=True)

    v = _Visit__fsys_patch_mapping4fsys_dict_patch(merge_case2skip_or_replace, old_fsys_dict)
    v.visit(fsys_patch_dict)
    new_fsys_dict = v.new_fsys_dict

    check_fsys_dict(new_fsys_dict)
    return new_fsys_dict


r'''
def fsys_dict_merge__inplace(merge_case2skip_or_replace, may_parent_dict_dst_basename_pair, dst_fsys_dict_or_patch_idx, src_fsys_dict_or_patch_idx):
    '[bool]{len=3} -> (None|(dst_parent_dict, dst_basename)) -> dst_fsys_dict_or_patch_idx -> src_fsys_dict_or_patch_idx -> None'
    raise NotImplementedError
    merge_case2skip_or_replace_ops.check_merge_case2skip_or_replace(merge_case2skip_or_replace)
    check_fsys_dict_or_patch_idx(dst_fsys_dict_or_patch_idx)
    check_fsys_dict_or_patch_idx(src_fsys_dict_or_patch_idx)
    if may_parent_dict_dst_basename_pair is None:
        if type(dst_fsys_dict_or_patch_idx) is int: raise TypeError
        dst_fsys_dict = dst_fsys_dict_or_patch_idx
        if type(src_fsys_dict_or_patch_idx) is int and merge_case2skip_or_replace_ops.is_to_overwrite_dir_by_file(merge_case2skip_or_replace): raise TypeError
    else:
        parent_dict_dst_basename_pair = may_parent_dict_dst_basename_pair
        dst_parent_dict, dst_basename = parent_dict_dst_basename_pair
        if not dst_parent_dict.get(dst_basename) is dst_fsys_dict_or_patch_idx: raise ValueError
#'''
#fsys_dict_merge__inplace
#fsys_dict_merge
#fsys_dict_or_patch_idx_merge
#HHHHH
def fsys_dict_or_patch_idx_merge(merge_case2skip_or_replace, dst_fsys_dict_or_patch_idx, src_fsys_dict_or_patch_idx):
    '[bool]{len=3} -> dst_fsys_dict_or_patch_idx -> src_fsys_dict_or_patch_idx -> new_fsys_dict_or_patch_idx'
    fsys_dict_patch
    _Visit__fsys_mapping4fsys_dict_merge

    merge_case2skip_or_replace_ops.check_merge_case2skip_or_replace(merge_case2skip_or_replace)
    check_fsys_dict_or_patch_idx(dst_fsys_dict_or_patch_idx)
    check_fsys_dict_or_patch_idx(src_fsys_dict_or_patch_idx)

    Nothing = object()
    if type(src_fsys_dict_or_patch_idx) is int:
        src_patch_idx = src_fsys_dict_or_patch_idx
        if type(dst_fsys_dict_or_patch_idx) is int:
            dst_patch_idx = dst_fsys_dict_or_patch_idx
            #file:=file
            to_overwrite_file_by_file = merge_case2skip_or_replace_ops.is_to_overwrite_file_by_file(merge_case2skip_or_replace)
            xnew_patch_idx = src_patch_idx if to_overwrite_file_by_file else dst_patch_idx
            xnew_fsys_dict_or_patch_idx = xnew_patch_idx
        else:
            dst_fsys_dict = dst_fsys_dict_or_patch_idx
            #dir:=file
            to_overwrite_dir_by_file = merge_case2skip_or_replace_ops.is_to_overwrite_dir_by_file(merge_case2skip_or_replace)
            xnew_fsys_dict_or_patch_idx = src_patch_idx if to_overwrite_dir_by_file else dst_fsys_dict
    else:
        src_fsys_mapping = src_fsys_dict_or_patch_idx
        if type(dst_fsys_dict_or_patch_idx) is int:
            dst_patch_idx = dst_fsys_dict_or_patch_idx
            #file:=dir
            to_overwrite_file_by_dir = merge_case2skip_or_replace_ops.is_to_overwrite_file_by_dir(merge_case2skip_or_replace)
            xnew_fsys_dict_or_patch_idx = src_fsys_mapping if to_overwrite_file_by_dir else dst_patch_idx
        else:
            dst_fsys_dict = dst_fsys_dict_or_patch_idx
            # merge dir dir
            xnew_fsys_dict_or_patch_idx = Nothing
    xnew_fsys_dict_or_patch_idx

    if xnew_fsys_dict_or_patch_idx is not Nothing:
        new_fsys_dict_or_patch_idx = copy_fsys_dict_or_patch_idx(xnew_fsys_dict_or_patch_idx)
    else:
        # merge dir dir
        src_fsys_mapping
        old_fsys_dict = dst_fsys_dict
        v = _Visit__fsys_mapping4fsys_dict_merge(merge_case2skip_or_replace, old_fsys_dict)
        v.visit(src_fsys_mapping)
        new_fsys_dict = v.new_fsys_dict
        new_fsys_dict_or_patch_idx = new_fsys_dict
    new_fsys_dict_or_patch_idx

    check_fsys_dict_or_patch_idx(new_fsys_dict_or_patch_idx)
    return new_fsys_dict_or_patch_idx
    merge_from_internal
    ('merge_from_external', merge_case2skip_or_replace, dst_relative_path, fsys_dict_or_patch_idx)







#HHHHH
def reopen_bin2txt(binary_ifile, *, encoding):
    text_ifile = binary_stream_obj2text_stream_obj(binary_ifile, encoding=encoding, buffered_case='read', kwargs4buffered_binary_stream={}, kwargs4text_stream={})
    return text_ifile

def read_repred_py_obj(binary_ifile):
    text_ifile = reopen_bin2txt(binary_ifile, encoding='utf8')
    s = text_ifile.read()
    obj = ast.literal_eval(s)
    return obj


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



class pseudo_virtual_file_reprobj_checker_cls4fsys_mapping_ex:
    @classmethod
    def check(cls, pseudo_virtual_file_reprobj):
        hash(pseudo_virtual_file_reprobj)
    r'''neednot copy
    @classmethod
    def check_and_deepcopy(cls, pseudo_virtual_file_reprobj):
        cls.check(pseudo_virtual_file_reprobj)
        return pseudo_virtual_file_reprobj
    #'''

class pseudo_virtual_file_reprobj_checker_cls4fsys_mapping(pseudo_virtual_file_reprobj_checker_cls4fsys_mapping_ex):
    @classmethod
    @override
    def check(cls, pseudo_virtual_file_reprobj):
        patch_idx = pseudo_virtual_file_reprobj
        check_uint(patch_idx)
class pseudo_virtual_file_reprobj_checker_cls4fsys_patch_mapping(pseudo_virtual_file_reprobj_checker_cls4fsys_mapping_ex):
    @classmethod
    @override
    def check(cls, pseudo_virtual_file_reprobj):
        if pseudo_virtual_file_reprobj is None:
            #remove
            pass
        elif type(pseudo_virtual_file_reprobj) is int:
            #ref to file content
            patch_idx = pseudo_virtual_file_reprobj
            check_uint(patch_idx)
        elif type(pseudo_virtual_file_reprobj) is str:
            #copy_from_internal
            relative_path__str = pseudo_virtual_file_reprobj

            check_relative_path__str(relative_path__str)
        elif not (pseudo_virtual_file_reprobj is None or type(pseudo_virtual_file_reprobj) in (int, str)): raise TypeError
        else:
            raise logic-err


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







#HHHHH
class merge_case2skip_or_replace_ops:
    r'''
    merge_case2skip_or_replace.def
        see:IFileSystem4update__fsys_delta
    #'''
    @classmethod
    def mk_merge_case2skip_or_replace(cls, /, overwrite_file_by_file, overwrite_file_by_dir, overwrite_dir_by_file):
         merge_case2skip_or_replace = (overwrite_file_by_file, overwrite_file_by_dir, overwrite_dir_by_file)
         cls.check_merge_case2skip_or_replace(merge_case2skip_or_replace)
         return merge_case2skip_or_replace
    @classmethod
    def check_merge_case2skip_or_replace(cls, merge_case2skip_or_replace, /):
        if not type(merge_case2skip_or_replace) is tuple: raise TypeError
        if not len(merge_case2skip_or_replace) == 3: raise TypeError
        (overwrite_file_by_file, overwrite_file_by_dir, overwrite_dir_by_file) = merge_case2skip_or_replace
        if not type(overwrite_file_by_file) is bool: raise TypeError
        if not type(overwrite_file_by_dir) is bool: raise TypeError
        if not type(overwrite_dir_by_file) is bool: raise TypeError

    @classmethod
    def is_to_overwrite_file_by_file(cls, merge_case2skip_or_replace, /):
        return merge_case2skip_or_replace[0]
    @classmethod
    def is_to_overwrite_file_by_dir(cls, merge_case2skip_or_replace, /):
        return merge_case2skip_or_replace[1]
    @classmethod
    def is_to_overwrite_dir_by_file(cls, merge_case2skip_or_replace, /):
        return merge_case2skip_or_replace[2]

def check_cmd(cmd):
    if not type(cmd) is tuple: raise TypeError
    if not cmd: raise TypeError
    if not type(cmd[0]) is str: raise TypeError

#HHHHH
class IFileSystem4update__fsys_delta(ABC):
    r'''
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
        #branch_history: each cmd not contains these args explicitly
        #   branch_history_cmd = (op, ...)
        this_branch_name
        curr_branch_idx <- [0..]
            not exist yet
            after success exec any cmd
            curr_branch_idx save the cmd

fsys_delta = fsys_update_cmd | branch_history_cmd

fsys_update_cmd:
    #bad: data fsys_dict/fsys_patch_dict is too big when impl branch_history_cmd::init_via_branch/merge_from_internal/copy_from_internal
    #       ???keep big to seperate branches???
    #           !!! not a delta repository impl !!!
    ('new_fsys', fsys_dict)
    ('del_fsys',)
    ('update_fsys', fsys_patch_dict)
branch_history_cmd:
    #bad: too hard to impl init_via_branch/merge_from_internal/copy_from_internal
    #       solved: now add IRepositorySetting to support
    ('init_via_copy', src_fsys_dict)
    ('init_via_branch', src_branch_name, src_branch_idx)
    ('del_branch',)

    ('merge_from_external', merge_case2skip_or_replace, dst_relative_path, src_fsys_dict_or_patch_idx)
    ('merge_from_internal', merge_case2skip_or_replace, dst_relative_path, src_branch_name, src_branch_idx, src_relative_path)
        skip_or_replace::bool
            replace if skip_or_replace else skip
        merge_case <- [0..2]
        merge_case2skip_or_replace::[bool]{len=3}
            0: 0b00 file:=file overwrite_file_by_file
            1: 0b01 file:=dir overwrite_file_by_dir
            2: 0b10 dir:=file overwrite_dir_by_file

        vs: merge vs copy
            copy - dst should not exists
            merge - dst may exist
                dir<-dir by recur merge
                file<-dir 0b01, dir<-file 0b10, file<-file 0b00 by replace or skip

    ('mkdir', dst_relative_path)
        #only use copy_from_external to impl mkdir, when src_fsys_dict is empty
        # dst_relative_path not exist
    ('copy_from_external', dst_relative_path, src_fsys_dict_or_patch_idx)
    ('copy_from_internal', dst_relative_path, src_branch_name, src_branch_idx, src_relative_path)
        # never mkdir dst_relative_path.parent
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

    ('patch', dst_file_relative_path, src_patch_idx)
        # assert src_patch_idx.parent==dst_patch_idx

    ####################################
    ####################################
    where:
        fsys_dict = dict<basename, (fsys_dict|patch_idx)>
        fsys_patch_dict = dict<basename, (fsys_patch_dict|patch_idx|None|src_relative_path__str)>
            None
                - remove file/dir
            src_relative_path :: tuple<basename>
                - copy/move from src_relative_path to here

        RecurView__fsys_mapping_ex = RecurView fsys_dict = dict_view<basename, (patch_idx | RecurView fsys_dict)>

        fsys_dict <: fsys_mapping
        fsys_mapping_view <: fsys_mapping

    #'''
    @abstractmethod
    def get_may_view_of_root_fsys_dict(sf):
        '-> (None|RecurView fsys_dict) #may fsys_mapping'
    @abstractmethod
    def deepcopy_may_root_fsys_dict(sf):
        '-> (None|fsys_dict)'
    @abstractmethod
    def apply_fsys_delta(sf, fsys_delta):
        'update underlying may fsys_dict'

class IFileSystem4update__fsys_delta_is_cmd(IFileSystem4update__fsys_delta):
    @classmethod
    @abstractmethod
    def get_cmd_op_names(cls):
        '-> frozenset<op_name>'

    def __init__(sf):
        sf._may_fsys_dict = None

    @override
    def get_may_view_of_root_fsys_dict(sf):
        '-> (None|RecurView fsys_dict)'
        m = sf._may_fsys_dict
        if m is None:
            return None
        else:
            fsys_dict = m
            return mk_fsys_mapping_view(fsys_dict)
    @override
    def deepcopy_may_root_fsys_dict(sf):
        '-> (None|fsys_dict)'
        if sf._may_fsys_dict is None:
            return None
        else:
            old_root_fsys_dict = sf._may_fsys_dict
            return copy_fsys_dict(old_root_fsys_dict)

    @override
    def apply_fsys_delta(sf, fsys_delta):
        'update underlying may fsys_dict'
        cmd = fsys_delta
        sf.exec_cmd4apply_fsys_delta(cmd)

    def exec_cmd4apply_fsys_delta(sf, cmd):
        'update underlying may fsys_dict'
        check_cmd(cmd)

        op = cmd[0]
        op_names = type(sf).get_cmd_op_names()
        if not (op in op_names): raise ValueError(f'unknown fsys_delta-cmd op: {op!r}')
        getattr(sf, op)(*cmd[1:])
        return None


#HHHHH
class FileSystem4update__fsys_delta_is_fsys_update_cmd(IFileSystem4update__fsys_delta_is_cmd):
    @override
    def apply_fsys_delta(sf, fsys_delta):
        'update underlying may fsys_dict'
        fsys_update_cmd = fsys_delta
        sf.exec_fsys_update_cmd(fsys_update_cmd)
    def exec_fsys_update_cmd(sf, fsys_update_cmd):
        'update underlying may fsys_dict'
        cmd = fsys_delta = fsys_update_cmd
        sf.exec_cmd4apply_fsys_delta(cmd)

    @classmethod
    @override
    def get_cmd_op_names(cls):
        '-> frozenset<op_name>'
        return __class__.__op_names
    __op_names = frozenset(('new_fsys', 'del_fsys', 'update_fsys'))

    if 0:
        ('new_fsys', src_fsys_dict)
        ('del_fsys',)
        ('update_fsys', fsys_patch_dict)

    def new_fsys(sf, src_fsys_dict):
        if not sf._may_fsys_dict is None: raise RuntimeError
        check_fsys_dict(src_fsys_dict)
        sf._may_fsys_dict = fsys_dict = copy_fsys_dict(src_fsys_dict)

    def del_fsys(sf):
        if sf._may_fsys_dict is None: raise RuntimeError
        old_fsys_dict = sf._may_fsys_dict
        sf._may_fsys_dict = None

    def update_fsys(sf, fsys_patch_dict):
        if sf._may_fsys_dict is None: raise RuntimeError
        old_fsys_dict = sf._may_fsys_dict
        check_fsys_patch_dict(fsys_patch_dict)
        new_fsys_dict = fsys_dict_patch(old_fsys_dict, fsys_patch_dict)
        check_fsys_dict(new_fsys_dict)
        sf._may_fsys_dict = new_fsys_dict




#HHHHH
class FileSystem4update__fsys_delta_is_branch_history_cmd(IFileSystem4update__fsys_delta_is_cmd):
    def __init__(sf, branch_name2min_extracting_branch_idx, repository_setting:'IRepositorySetting'):
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
    def exec_branch_history_cmd(sf, branch_history_cmd):
        'update underlying may fsys_dict'
        cmd = fsys_delta = branch_history_cmd
        sf.exec_cmd4apply_fsys_delta(cmd)

    @classmethod
    @override
    def get_cmd_op_names(cls):
        '-> frozenset<op_name>'
        return __class__.__op_names
    __op_names = frozenset(('init_via_copy', 'init_via_branch', 'del_branch', 'merge_from_external', 'merge_from_internal', 'mkdir', 'copy_from_external', 'copy_from_internal', 'move_shiftL', 'swap_rotateL', 'remove', 'patch'))

    if 0:
        ('init_via_copy', src_fsys_dict)
        ('init_via_branch', src_branch_name, src_branch_idx)
        ('del_branch',)
        ('merge_from_external', merge_case2skip_or_replace, dst_relative_path, src_fsys_dict_or_patch_idx)
        ('merge_from_internal', merge_case2skip_or_replace, dst_relative_path, src_branch_name, src_branch_idx, src_relative_path)
        ('mkdir', dst_relative_path)
        ('copy_from_external', dst_relative_path, src_fsys_dict_or_patch_idx)
        ('copy_from_internal', dst_relative_path, src_branch_name, src_branch_idx, src_relative_path)
        ('move_shiftL', dst_relative_path, [src_relative_path])
        ('swap_rotateL', [relative_path])
        ('remove', dst_relative_path)
        ('patch', dst_file_relative_path, src_patch_idx)


    def init_via_copy(sf, src_fsys_dict):
        if not sf._may_fsys_dict is None: raise RuntimeError
        sf._may_fsys_dict = fsys_dict = copy_fsys_dict(src_fsys_dict)
    def init_via_branch(sf, src_branch_name, src_branch_idx):
        if not sf._may_fsys_dict is None: raise RuntimeError
        # !!!!!too hard to impl here!!!!!
        may_src_root_fsys_dict = sf.repository_setting.extract_may_root_fsys_dict_at_branch_time(sf.branch_name2min_extracting_branch_idx, src_branch_name, src_branch_idx)
        if may_src_root_fsys_dict is None: raise ValueError
        src_root_sys_dict = may_src_root_fsys_dict
        sf._may_fsys_dict = fsys_dict = copy_fsys_dict(src_root_fsys_dict)

    def del_branch(sf):
        if sf._may_fsys_dict is None: raise RuntimeError
        old_fsys_dict = sf._may_fsys_dict
        sf._may_fsys_dict = None



    def get_tmay_sub_fsys_dict_or_patch_idx_from_internal(sf, src_branch_name, src_branch_idx, src_relative_path):
        may_src_root_fsys_dict = sf.repository_setting.extract_may_root_fsys_dict_at_branch_time(sf.branch_name2min_extracting_branch_idx, src_branch_name, src_branch_idx)
        if may_src_root_fsys_dict is None: raise ValueError
        src_root_sys_dict = may_src_root_fsys_dict
        tmay_src_fsys_dict_or_patch_idx = get_tmay_sub_fsys_dict_or_patch_idx(src_root_sys_dict, src_relative_path)
        return tmay_src_fsys_dict_or_patch_idx

    def __merge_from(sf, merge_case2skip_or_replace, dst_relative_path, src_fsys_dict_or_patch_idx):
        if sf._may_fsys_dict is None: raise RuntimeError
        old_fsys_dict = sf._may_fsys_dict
        tmay_dst_fsys_dict_or_patch_idx = get_tmay_sub_fsys_dict_or_patch_idx(old_fsys_dict, dst_relative_path)
        if not tmay_dst_fsys_dict_or_patch_idx: raise ValueError('merge to nothing')
        [dst_fsys_dict_or_patch_idx] = tmay_dst_fsys_dict_or_patch_idx
        new_fsys_dict_or_patch_idx = fsys_dict_or_patch_idx_merge(merge_case2skip_or_replace, dst_fsys_dict_or_patch_idx, src_fsys_dict_or_patch_idx)
        if is_relative_path_empty(dst_relative_path):
            sf._may_fsys_dict = new_fsys_dict_or_patch_idx
        else:
            tmay_dst_parent_dict = get_tmay_sub_fsys_dict_or_patch_idx(old_fsys_dict, dst_relative_path.parent)
            if not tmay_dst_parent_dict: raise logic-err
            [dst_parent_dict] = tmay_dst_parent_dict
            dst_basename = dst_relative_path.name
            assert dst_parent_dict[dst_basename] is dst_fsys_dict_or_patch_idx
            dst_parent_dict[dst_basename] = new_fsys_dict_or_patch_idx
                #inplace


    def merge_from_external(sf, merge_case2skip_or_replace, dst_relative_path, src_fsys_dict_or_patch_idx):
        sf.__merge_from(merge_case2skip_or_replace, dst_relative_path, src_fsys_dict_or_patch_idx)
    def merge_from_internal(sf, merge_case2skip_or_replace, dst_relative_path, src_branch_name, src_branch_idx, src_relative_path):
        tmay_src_fsys_dict_or_patch_idx = sf.get_tmay_sub_fsys_dict_or_patch_idx_from_internal(src_branch_name, src_branch_idx, src_relative_path)
        if not tmay_src_fsys_dict_or_patch_idx: raise ValueError('merge from nothing')
        [src_fsys_dict_or_patch_idx] = tmay_src_fsys_dict_or_patch_idx

        sf.__merge_from(merge_case2skip_or_replace, dst_relative_path, src_fsys_dict_or_patch_idx)

    def mkdir(sf, dst_relative_path):
        if sf._may_fsys_dict is None: raise RuntimeError
        old_fsys_dict = sf._may_fsys_dict
        get_tmay_sub_fsys_dict_or_patch_idx
        (parts, depth, sub_fsys_dict_or_patch_idx) = cd_to_sub_fsys_dict_or_patch_idx_ex_as_deep_as_possible(old_fsys_dict, dst_relative_path)
        if type(sub_fsys_dict_or_patch_idx) is int: raise ValueError('mkdir: meet file')
        sub_fsys_dict = sub_fsys_dict_or_patch_idx
        if depth == len(parts): raise ValueError('mkdir: dir exists')
        assert parts[depth] not in sub_fsys_dict
        for basename in parts[depth:]:
            sub_fsys_dict[basename] = child = {}
                #inplace
            sub_fsys_dict = child

    def __move_or_swap_or_remove_src2parent_dict_basename_pair(sf, src_relative_path):
        r'''
        :: src_relative_path -> (src_parent_dict, src_basename)
        # src_relative_path.parent exists
        # src_relative_path exists
        #'''
        if sf._may_fsys_dict is None: raise RuntimeError
        old_fsys_dict = sf._may_fsys_dict

        (parts, depth, sub_fsys_dict_or_patch_idx) = cd_to_sub_fsys_dict_or_patch_idx_ex_as_deep_as_possible(old_fsys_dict, src_relative_path)

        if not parts: raise ValueError('move/swap/remove src_relative_path is empty/root_dir')
        elif depth == len(parts):
            pass
        elif type(sub_fsys_dict_or_patch_idx) is int: raise ValueError('move/swap/remove src ancestor_dir be file, hence src not exists')
        elif 0 <= depth < len(parts): raise ValueError('move/swap/remove src not exists')
        else:
            raise logic-err

        src_fsys_dict_or_patch_idx = sub_fsys_dict_or_patch_idx

        [src_parent_dict] = get_tmay_sub_fsys_dict_or_patch_idx(old_fsys_dict, src_relative_path.parent)
        src_basename = src_relative_path.name
        assert src_basename in src_parent_dict
        return src_parent_dict, src_basename


    def __copy_or_move_dst2parent_dict_basename_pair(sf, dst_relative_path):
        r'''
        :: dst_relative_path -> (dst_parent_dict, dst_basename)
        # dst_relative_path.parent exists, neednot mkdir
        # dst_relative_path not exists, neednot overwrite #otherwise use merge_from... instead copy_from...
        #   to replace dir by dir instead of merge, ==>> remove then copy
        #'''

        if sf._may_fsys_dict is None: raise RuntimeError
        old_fsys_dict = sf._may_fsys_dict

        (parts, depth, sub_fsys_dict_or_patch_idx) = cd_to_sub_fsys_dict_or_patch_idx_ex_as_deep_as_possible(old_fsys_dict, dst_relative_path)

        if not parts: raise ValueError('copy/move dst_relative_path is empty/root_dir')
        elif depth == len(parts): raise ValueError('copy/move dst exists, to replace should use merge cmd or remove cmd')
        elif type(sub_fsys_dict_or_patch_idx) is int: raise ValueError('copy/move dst ancestor_dir be file')
        elif 0 <= depth < len(parts)-1: raise ValueError('copy/move into no where, mkdir first')
        elif 0 <= depth == len(parts)-1:
            pass
        else:
            raise logic-err

        dst_parent_dict = sub_fsys_dict_or_patch_idx

        dst_basename = dst_relative_path.name
        assert dst_basename not in dst_parent_dict
        return dst_parent_dict, dst_basename

    def __copy_from(sf, dst_relative_path, src_fsys_dict_or_patch_idx):
        (dst_parent_dict, dst_basename) = sf.__copy_or_move_dst2parent_dict_basename_pair(dst_relative_path)
        dst_parent_dict[dst_basename] = copy_fsys_dict_or_patch_idx(src_fsys_dict_or_patch_idx)
            #inplace
    def copy_from_external(sf, dst_relative_path, src_fsys_dict_or_patch_idx):
        sf.__copy_from(dst_relative_path, src_fsys_dict_or_patch_idx)
    def copy_from_internal(sf, dst_relative_path, src_branch_name, src_branch_idx, src_relative_path):
        tmay_src_fsys_dict_or_patch_idx = sf.get_tmay_sub_fsys_dict_or_patch_idx_from_internal(src_branch_name, src_branch_idx, src_relative_path)
        if not tmay_src_fsys_dict_or_patch_idx: raise ValueError('copy from nothing')
        [src_fsys_dict_or_patch_idx] = tmay_src_fsys_dict_or_patch_idx

        sf.__copy_from(dst_relative_path, src_fsys_dict_or_patch_idx)
        return
        merge_from_internal

    def __move_or_swap_check_no_ancestor_dir(sf, dst_or_src_relative_paths):
        sorted_dst_or_src_relative_path_partss = sorted(map(relative_path2parts, dst_or_src_relative_paths))
        if not sorted_dst_or_src_relative_path_partss[0]: raise ValueError('move/swap dst/src is root dir')
        for i in range(1, len(sorted_dst_or_src_relative_path_partss)):
            prev_dst_or_src_relative_path_parts = sorted_dst_or_src_relative_path_partss[i-1]
            curr_dst_or_src_relative_path_parts = sorted_dst_or_src_relative_path_partss[i]
            if is_prefix_of_seq(prev_dst_or_src_relative_path_parts, curr_dst_or_src_relative_path_parts): raise ValueError('move/swap dst/src contain both curr_dir_or_file and its ancestor_dir')

    def move_shiftL(sf, dst_relative_path, src_relative_paths):
        if sf._may_fsys_dict is None: raise RuntimeError
        old_fsys_dict = sf._may_fsys_dict
        if not type(src_relative_paths) is tuple: raise TypeError
        if not src_relative_paths: raise ValueError('move_shiftL with no src_relative_paths')

        dst_or_src_relative_paths = [dst_relative_path, *src_relative_paths]
        sf.__move_or_swap_check_no_ancestor_dir(dst_or_src_relative_paths)

        (dst_parent_dict, dst_basename) = sf.__copy_or_move_dst2parent_dict_basename_pair(dst_relative_path)

        dst_relative_path #checked not exists
        assert dst_basename not in dst_parent_dict


        src_parent_dict_basename_pairs = tuple(map(sf.__move_or_swap_or_remove_src2parent_dict_basename_pair, src_relative_paths))
            #checked exists
        sf.__move_shiftL(dst_parent_dict, dst_basename, src_parent_dict_basename_pairs)
            #inplace

    def __move_shiftL(sf, dst_parent_dict, dst_basename, src_parent_dict_basename_pairs):
        #inplace
        for (src_parent_dict, src_basename) in src_parent_dict_basename_pairs:
            assert dst_basename not in dst_parent_dict
            dst_parent_dict[dst_basename] = copy_fsys_dict_or_patch_idx(src_parent_dict[src_basename])
                #inplace
            del src_parent_dict[src_basename]
                #inplace
            (dst_parent_dict, dst_basename) = (src_parent_dict, src_basename)

    def swap_rotateL(sf, relative_paths):
        if sf._may_fsys_dict is None: raise RuntimeError
        old_fsys_dict = sf._may_fsys_dict
        if not type(relative_paths) is tuple: raise TypeError
        if not len(relative_paths) >= 2: raise ValueError('swap_rotateL with not enough relative_paths')

        dst_or_src_relative_paths = relative_paths
        sf.__move_or_swap_check_no_ancestor_dir(dst_or_src_relative_paths)

        dst_parent_dict = {}
        dst_basename = '0'
        src_parent_dict_basename_pairs = (*map(sf.__move_or_swap_or_remove_src2parent_dict_basename_pair, relative_paths), (dst_parent_dict, dst_basename))
            #checked exists
        sf.__move_shiftL(dst_parent_dict, dst_basename, src_parent_dict_basename_pairs)
            #inplace
        assert not dst_parent_dict

    def remove(sf, dst_relative_path):
        if sf._may_fsys_dict is None: raise RuntimeError
        old_fsys_dict = sf._may_fsys_dict

        src_relative_path = dst_relative_path
        src_parent_dict_basename_pair = sf.__move_or_swap_or_remove_src2parent_dict_basename_pair(src_relative_path)
        dst_parent_dict_basename_pair = src_parent_dict_basename_pair

        dst_parent_dict, dst_basename = dst_parent_dict_basename_pair
        assert dst_basename in dst_parent_dict
        del dst_parent_dict[dst_basename]
            #inplace
    def patch(sf, dst_file_relative_path, src_patch_idx):
        if sf._may_fsys_dict is None: raise RuntimeError
        old_fsys_dict = sf._may_fsys_dict

        tmay_dst_fsys_dict_or_patch_idx = get_tmay_sub_fsys_dict_or_patch_idx(old_fsys_dict, dst_file_relative_path)
        if not tmay_dst_fsys_dict_or_patch_idx: raise ValueError('patch to nothing')
        [dst_fsys_dict_or_patch_idx] = tmay_dst_fsys_dict_or_patch_idx
        if not type(dst_fsys_dict_or_patch_idx) is int: raise ValueError('patch dst is dir (should be file)')
        dst_patch_idx = dst_fsys_dict_or_patch_idx
        src_patch_idx
        #assert src_patch_idx.parent==dst_patch_idx
        src_imay_parent_idx = sf.repository_setting.patch_idx2imay_parent_idx(src_patch_idx)
        if not dst_patch_idx == src_imay_parent_idx: raise ValueError('patch cmd: src_imay_parent_idx.parent != dst_patch_idx; to replace use remov/copy/merge cmd instead')

        [dst_parent_dict] = get_tmay_sub_fsys_dict_or_patch_idx(old_fsys_dict, dst_file_relative_path.parent)
        dst_basename = dst_file_relative_path.basename
        assert dst_parent_dict[dst_basename] is dst_patch_idx
        dst_parent_dict[dst_basename] = src_patch_idx
            #inplace













#HHHHH
class IRepositorySetting__user_data_dir_path(ABC):
    r'''
    user_data_dir_path_setting
    user_data_dir is the inf_dir element of file_patch_forest_dir
    below relative_path are relative_to any user_data_dir
    #'''

    @abstractmethod
    def get_parentfile_relative_path_under_user_data_dir(sf):
        '-> parentfile_relative_path'
        return PurePosixPath('parent')
    @abstractmethod
    def get_contentfile_relative_path_under_user_data_dir(sf):
        '-> contentfile_relative_path'
        return PurePosixPath('content')
    @abstractmethod
    def get_metadatafile_relative_path_under_user_data_dir(sf):
        '-> metadatafile_relative_path'
        return PurePosixPath('metadata')


    #no read/write contentfile !
    #   since vary cases

    @abstractmethod
    def read_metadata(sf, metadata_ifile):
        'input_binary_file -> metadata'
    @abstractmethod
    def write_metadata(sf, metadata_ofile, metadata):
        'output_binary_file -> metadata -> None'
    @abstractmethod
    def read_imay_parent_idx(sf, imay_parent_idx_ifile):
        'input_binary_file -> [-1..] # imay'
        #return _read_imay_parent__user_data(imay_parent_idx_ifile)
        #s = parent_path.read_text(encoding='ascii')
        #bs = imay_parent_idx_ifile.read()
        #s = bs.decode(encoding='ascii')
        imay_parent_idx = read_repred_py_obj(imay_parent_idx_ifile)
        check_uint_imay(imay_parent_idx)
        return imay_parent_idx

    @abstractmethod
    def write_imay_parent_idx(sf, imay_parent_idx_ofile, imay_parent_idx):
        'output_binary_file -> [-1..] -> None # imay'

#HHHHH
class IRepositorySetting__repository_root_dir_path(ABC):
    r'''
    repository_root_dir_path_setting
    repository_root_dir is the root dir to backup to
    below relative_path are relative_to the repository_root_dir
    #'''



    @abstractmethod
    def get_repository_root_dir_path(sf):
        '-> repository_root_dir_path'

    #updating/
    @abstractmethod
    def get_file_stack_dir_relative_path(sf):
        '-> file_stack_dir_relative_path'
        return PurePosixPath('updating/file_stack')
    @abstractmethod
    def get_TODO_list4move_cmd_file_relative_path(sf):
        '-> TODO_list4move_cmd_file_relative_path'
        return PurePosixPath('updating/TODO_list4move_cmd')
    @abstractmethod
    def get_commit_completed_file_relative_path(sf):
        '-> commit_completed_file_relative_path'
        return PurePosixPath('updating/commit_completed')


    #grow_only/
    @abstractmethod
    def get_command_history_dir_relative_path(sf):
        '-> command_history_dir_relative_path'
        return PurePosixPath('grow_only/command_history')
    @abstractmethod
    def get_file_patch_forest_dir_relative_path(sf):
        '-> file_patch_forest_dir_relative_path'
        return PurePosixPath('grow_only/file_patch_forest')
    @abstractmethod
    def get_branch_history_dir_relative_path(sf, branch_name):
        'branch_name -> branch_history_dir_relative_path'


    #get len_inf_dir of grow_only/...
    #   cache a min value
    #   not include updating/file_stack which will pop
    #
    @abstractmethod
    def get_len_inf_dir_of_command_history(sf):
        '-> len(command_history)=len_inf_dir(command_history_dir_path)'
    @abstractmethod
    def get_len_inf_dir_of_file_patch_forest(sf):
        '-> len(file_patch_forest)=len_inf_dir(file_patch_forest_dir_path)'
    @abstractmethod
    def get_len_inf_dir_of_branch_history(sf, branch_name):
        'branch_name -> len(branch_name2branch_history[branch_name])=len_inf_dir(branch_history_dir_path)'








    #grow_only
    def get_command_history_dir_path(sf):
        '-> command_history_dir_path'
        return sf.get_repository_root_dir_path() / sf.get_command_history_dir_relative_path()
    def get_file_patch_forest_dir_path(sf):
        '-> file_patch_forest_dir_path'
        return sf.get_repository_root_dir_path() / sf.get_file_patch_forest_dir_relative_path()
    def get_branch_history_dir_path(sf, branch_name):
        '-> branch_history_dir_path'
        return sf.get_repository_root_dir_path() / sf.get_branch_history_dir_relative_path(branch_name)


    #updating
    def get_file_stack_dir_path(sf):
        '-> file_stack_dir_path'
        return sf.get_repository_root_dir_path() / sf.get_file_stack_dir_relative_path()
    def get_TODO_list4move_cmd_file_path(sf):
        '-> TODO_list4move_cmd_file_path'
        return sf.get_repository_root_dir_path() / sf.get_TODO_list4move_cmd_file_relative_path()
    def get_commit_completed_file_path(sf):
        '-> commit_completed_file_path'
        return sf.get_repository_root_dir_path() / sf.get_commit_completed_file_relative_path()




#HHHHH
class IRepositorySetting__working_root_dir_path(ABC):
    r'''
    working_root_dir_path_setting
    working_root_dir is the root dir to backup from
    below relative_path are relative_to the dynamic given working_root_dir
    #'''

    @abstractmethod
    def get_ignorefile_relative_paths_under_working_root_dir(sf):
        r'''-> [ignorefile_relative_path] # or(ignores)
        may be empty, default ignore=False #i.e. not ignore
        each ignorefile+path_relative_to_working_root_dir ==>> (ignore::bool)
        fold op False ignores
            ==>> any(ignores)
            ==>> op==or
        ###
        these ignorefile_relative_paths themself are never be ignored
        #'''

#HHHHH
class IRepositorySetting(IRepositorySetting__working_root_dir_path, IRepositorySetting__repository_root_dir_path, IRepositorySetting__user_data_dir_path):
    r'''repository_setting
    #'''

    @abstractmethod
    def ___read_move_cmds___(sf, TODO_list4move_cmd_ifile):
        r'''binary_ifile -> [(idx4file_stack, move_cmd_target, move_cmd_target_args, idx4move_cmd_target)]
        see: read_move_cmds
        #'''



    @abstractmethod
    def ___extract_may_root_fsys_dict_at_branch_time___(sf, branch_name2min_extracting_branch_idx, branch_name, branch_idx):
        r'''
        branch_name2min_extracting_branch_idx -> branch_name -> branch_idx -> (None|root fsys_dict)'
        see: extract_may_root_fsys_dict_at_branch_time
        #'''
    @abstractmethod
    def get_cache__branch_time2root_fsys_dict(sf):
        r'''-> branch_time2root_fsys_dict #{(branch_name, branch_idx):root_fsys_dict}
        to impl: extract_may_root_fsys_dict_at_branch_time
        #'''
        #many cache: AccessFile4MkIsSameFile__backup_util_repository__fsys_dict__IRepositorySetting.metadata_cache_lookup
        #many cache: IRepositorySetting.get_cache__branch_time2root_fsys_dict

    @abstractmethod
    def get_dir_size(sf):
        '-> dir_size'
    @abstractmethod
    def get_lcp_threshold(sf):
        '-> lcp_threshold'
    @abstractmethod
    def get_repository_extra_cache_root_dir_path(sf):
        r'''
        -> repository_extra_cache_root_dir_path
        only valid on the real working fsys
            xxx * ignorefile_relative_path
            xxx * tmp commit dir to recover or rollback
            xxx * cache len of each inf_dir
                double save
                to recover from crash
            * for dir_cmp:
                cache eq result:
                    virtual_file@fsys_dict = patch_idx
                    real_file@fsys
                when eq:
                    cache real_file.mtime
                        may not eq virtual_file.metadata.mtime
                    #virtual_file.metadata save mtime
                    #virtual_file.metadata save hash
        #'''

    def patch_idx2imay_parent_idx(sf, patch_idx):
        user_data_dir_path = sf.patch_idx2user_data_dir_path(patch_idx)
        parentfile_path = user_data_dir_path / sf.get_parentfile_relative_path_under_user_data_dir()
        with open(parentfile_path, 'rb') as imay_parent_idx_ifile:
            imay_parent_idx = sf.read_imay_parent_idx(imay_parent_idx_ifile)
        assert type(imay_parent_idx) is int
        assert imay_parent_idx >= -1
        return imay_parent_idx


    def patch_idx2user_data_dir_path(sf, patch_idx):
        'patch_idx -> real user_data_dir_path@fsys'
        dir_size = sf.get_dir_size()
        relative_path = inf_dir_idx2user_data_relative_path(patch_idx, dir_size=dir_size)

        file_patch_forest_dir_path = sf.get_file_patch_forest_dir_path()

        user_data_dir_path = file_patch_forest_dir_path / relative_path
        return user_data_dir_path









    def move_cmd_target__user_data_file__virtual_name2relative_path_under_user_data_dir(sf, user_data_file__virtual_name):
        if not user_data_file__virtual_name in sf.move_cmd_target__user_data_file__virtual_names: raise ValueError
        #attr = 'get_metadatafile_relative_path_under_user_data_dir'
        attr = f'get_{user_data_file__virtual_name!s}file_relative_path_under_user_data_dir'
        return getattr(sf, attr)()
    move_cmd_targets = ('push_into_command_history', 'push_into_branch_fsys_history', 'move_into_file_patch_forest')
    move_cmd_target__user_data_file__virtual_names = ('parent', 'content', 'metadata')
    def read_move_cmds(sf, TODO_list4move_cmd_ifile):
        r'''binary_ifile -> [(idx4file_stack, move_cmd_target, move_cmd_target_args, idx4move_cmd_target)]

    ###
    move_cmd_target + args
        = 'push_into_command_history'
            ()
        | 'push_into_branch_fsys_history'
            (branch_name,)
        | 'move_into_file_patch_forest'
            #not (path_relative_to_user_data_dir,)
            #using virtual path name
            (('parent'|'content'|'metadata'),)

    ###
    default_move_cmd_line_fmt:
        # move_cmd_line_fmt from IRepositorySetting.read_move_cmds.__doc__
        # for line in updating/TODO_list4move_cmd
        #sorted(cmds, key=.i, reverse=True)
        #i <- [0..sz-1]
        #i <- [sz-1, sz-2..0]

        * pop updating/file_stack[{i}] -> push_into grow_only/command_history[{j}]

        * pop updating/file_stack[{i}] -> push_into grow_only/branches/{branch_name}[{j}]

        * pop updating/file_stack[{i}] -> move_to parent @ grow_only/file_patch_forest[{j}]
        * pop updating/file_stack[{i}] -> move_to content @ grow_only/file_patch_forest[{j}]
        * pop updating/file_stack[{i}] -> move_to metadata @ grow_only/file_patch_forest[{j}]
        #'''
        move_cmds = type(sf).___read_move_cmds___(sf, TODO_list4move_cmd_ifile)
        sf.check_move_cmds(move_cmds)
        return move_cmds
    def check_move_cmds(sf, move_cmds):
        check_tuple(move_cmds)
        for move_cmd in move_cmds:
            sf.check_move_cmd(move_cmd)
        idc4file_stack = tuple(map(fst, move_cmds))
        if not idc4file_stack == tuple(reversed(range(len(idc4file_stack)))): raise ValueError

    def check_move_cmd(sf, move_cmd):
        check_tuple(move_cmd, sz=4)
        (idx4file_stack, move_cmd_target, move_cmd_target_args, idx4move_cmd_target) = move_cmd
        check_uint(idx4file_stack)
        check_uint(idx4move_cmd_target)
        check_str(move_cmd_target)

        check_tuple(move_cmd_target_args)
        check_int(len(move_cmd_target_args), max=1)
        check_all(check_str, move_cmd_target_args)

        if move_cmd_target not in sf.move_cmd_targets: raise ValueError
        #('push_into_command_history', 'push_into_branch_fsys_history', 'move_into_file_patch_forest')
        if move_cmd_target == 'push_into_command_history':
            if not len(move_cmd_target_args) == 0: raise TypeError
        elif move_cmd_target == 'push_into_branch_fsys_history':
            if not len(move_cmd_target_args) == 1: raise TypeError
        elif move_cmd_target == 'move_into_file_patch_forest':
            if not len(move_cmd_target_args) == 1: raise TypeError
            [user_data_file__virtual_name] = move_cmd_target_args
            if not user_data_file__virtual_name in sf.move_cmd_target__user_data_file__virtual_names: raise ValueError
        else:
            raise logic-err


    def clean_updating_root_dir(sf):
        r'''
        mk/del order:
            mk file_stack_dir
            mk TODO_list4move_cmd_file
            mk commit_completed_file
            ---
            del commit_completed_file
            del TODO_list4move_cmd_file
            del file_stack_dir

        #'''
        file_stack_dir_path = sf.get_file_stack_dir_path()
        TODO_list4move_cmd_file_path = sf.get_TODO_list4move_cmd_file_path()
        commit_completed_file_path = sf.get_commit_completed_file_path()
        if commit_completed_file_path.exists():
            sf.__continue_flush_commit()
            if not is_dir_empty(file_stack_dir_path): raise logic-er
            commit_completed_file_path.unlink() #remove file == os.remove
            TODO_list4move_cmd_file_path.unlink()#should exists
            file_stack_dir_path.rmdir()#should be empty
        else:
            assert not commit_completed_file_path.exists()
            TODO_list4move_cmd_file_path.unlink(missing_ok=True)#may not exists
            if file_stack_dir_path.exists():
                shutil.rmtree(file_stack_dir_path)#may not empty


    def __continue_flush_commit(sf)
        file_stack_dir_path = sf.get_file_stack_dir_path()
        TODO_list4move_cmd_file_path = sf.get_TODO_list4move_cmd_file_path()
        commit_completed_file_path = sf.get_commit_completed_file_path()
        if not commit_completed_file_path.exists(): raise FileNotFoundError

        if 1:
            dir_size = sf.get_dir_size(),
            inf_dir_remove_tail_empty_dirs(file_stack_dir_path, dir_size=dir_size, min_len=0)
            sz = len_inf_dir(file_stack_dir_path)
            move_cmds = sf.read_move_cmds()
            move_cmds = move_cmds[len(move_cmds)-sz:]
            if sz:
                init_idx = sz-1
                assert len(move_cmds) == sz
                if move_cmds[0][0] != init_idx: raise logic-err
                if move_cmds[-1][0] != 0: raise logic-err
            for move_cmd in move_cmds:
                sf.exec_move_cmd(move_cmd)

        if not is_dir_empty(file_stack_dir_path): raise logic-er

    def exec_move_cmd(sf, move_cmd):
        sf.check_move_cmd(move_cmd)
        (idx4file_stack, move_cmd_target, move_cmd_target_args, idx4move_cmd_target) = move_cmd
        if move_cmd_target == 'push_into_command_history':
            () = move_cmd_target_args
            command_history_dir_path = sf.get_command_history_dir_path()
            pop_from_inf_dir_and_push_into_another(inf_dir_path4into=command_history_dir_path, inf_dir_path4from=file_stack_dir_path, dir_size4into=dir_size, dir_size4from=dir_size, min_len4into=max(0, idx4move_cmd_target-1), min_len4from=idx4file_stack, imay_inf_dir_idx4assert4into=idx4move_cmd_target, imay_inf_dir_idx4assert4from=idx4file_stack)
        elif move_cmd_target == 'push_into_branch_fsys_history':
            (branch_name,) = move_cmd_target_args
            branch_history_dir_path = sf.get_branch_history_dir_path(branch_name)
            pop_from_inf_dir_and_push_into_another
            pop_from_inf_dir_and_push_into_another(inf_dir_path4into=branch_history_dir_path, inf_dir_path4from=file_stack_dir_path, dir_size4into=dir_size, dir_size4from=dir_size, min_len4into=max(0, idx4move_cmd_target-1), min_len4from=idx4file_stack, imay_inf_dir_idx4assert4into=idx4move_cmd_target, imay_inf_dir_idx4assert4from=idx4file_stack)
        elif move_cmd_target == 'move_into_file_patch_forest':
            (user_data_file__virtual_name,) = move_cmd_target_args
            #(('parent'|'content'|'metadata'),)
            file_patch_forest_dir_path = sf.get_file_patch_forest_dir_path()
            target_file_relative_path_under_user_data_dir = sf.move_cmd_target__user_data_file__virtual_name2relative_path_under_user_data_dir(user_data_file__virtual_name)
            target_file_path = mk_target_path_under_inf_dir(file_patch_forest_dir_path, idx4move_cmd_target, target_file_relative_path_under_user_data_dir, dir_size=dir_size)
            pop_from_inf_dir_and_move
            pop_from_inf_dir_and_move(to_path=target_file_path, from_inf_dir_path=file_stack_dir_path, dir_size=dir_size, min_len=idx4file_stack, imay_inf_dir_idx4assert=idx4file_stack)
        else:
            raise logic-err






    def extract_may_root_fsys_dict_at_branch_time(sf, branch_name2min_extracting_branch_idx, branch_name, branch_idx):
        r'''
        branch_name2min_extracting_branch_idx -> branch_name -> branch_idx -> (None|root fsys_dict)'

        #####
        donot move to IFileSystem4update__fsys_delta
        #####
        should cache result when success
        #####

        required:
            get_cache__branch_time2root_fsys_dict
            ___extract_may_root_fsys_dict_at_branch_time___
        #'''
        check_str(branch_name)
        check_uint(branch_idx)
        branch_time = (branch_name, branch_idx)
        branch_time2root_fsys_dict = sf.get_cache__branch_time2root_fsys_dict()

        def this_func(depth):
            try:
                root_fsys_dict = branch_time2root_fsys_dict[branch_time]
            except KeyError:
                pass
            else:
                return copy_fsys_dict(root_fsys_dict)
            if depth: raise logic-err


            if not branch_idx < sf.get_len_inf_dir_of_branch_history(branch_name): raise ValueError

            if branch_name in branch_name2min_extracting_branch_idx:
                saved_min_extracting_branch_idx = branch_name2min_extracting_branch_idx[branch_name]
                if branch_idx >= saved_min_extracting_branch_idx: raise ValueError(f'branch_name={branch_name!r}: old_time={saved_min_extracting_branch_idx!r} required new_time={branch_idx!r} : non-DAG, cycle-dependency')
                def pop():
                    branch_name2min_extracting_branch_idx[branch_name] = saved_min_extracting_branch_idx
            else:
                def pop():
                    del branch_name2min_extracting_branch_idx[branch_name]

            def push():
                branch_name2min_extracting_branch_idx[branch_name] = branch_idx

            f = type(sf).___extract_may_root_fsys_dict_at_branch_time___
            push()
            try:
                may_root_fsys_dict = f(sf, branch_name2min_extracting_branch_idx, branch_name, branch_idx)
            finally:
                pop()

            if may_root_fsys_dict is not None:
                root_fsys_dict = may_root_fsys_dict
                check_fsys_dict(root_fsys_dict)
                v = branch_time2root_fsys_dict.setdefault(branch_time, root_fsys_dict)
                if v is not root_fsys_dict: raise logic-err
                r = this_func(depth+1)
                if r is not root_fsys_dict: raise logic-err
                return r
            else:
                return None
            return may_root_fsys_dict
        #end:def this_func(depth):
        return this_func(0)

class IRepositorySetting__branches_together(IRepositorySetting):
    @abstractmethod
    def get_branches_dir_relative_path(sf):
        '-> branches_dir_relative_path'
        return PurePosixPath('grow_only/branches')
    @override
    def get_branch_history_dir_relative_path(sf, branch_name):
        'branch_name -> branch_history_dir_relative_path'
        return sf.get_branches_dir_relative_path() / branch_name

def check_path(path):
    if not isinstance(path, Path): raise TypeError



class IRepositorySetting__cache_min_len_inf_dir(IRepositorySetting):
    def __init__(sf, /,*, min_len_command_history_dir, min_len_file_patch_forest_dir, branch_name2min_len_branch_history_dir):
        check_uint(min_len_command_history_dir)
        check_uint(min_len_file_patch_forest_dir)

        branch_name2min_len_branch_history_dir = dict(branch_name2min_len_branch_history_dir)
        check_all(check_str, branch_name2min_len_branch_history_dir.key())
        check_all(check_uint, branch_name2min_len_branch_history_dir.values())

        sf.__dict__.update(locals())
        del sf.__dict__['sf']

    @override
    def get_len_inf_dir_of_command_history(sf):
        '-> len(command_history)=len_inf_dir(command_history_dir_path)'
        sz = len_inf_dir(sf.get_command_history_dir_path(), dir_size=sf.get_dir_size(), min_len=sf.min_len_command_history_dir)
        sf.min_len_command_history_dir = sz
        return sz
    @override
    def get_len_inf_dir_of_file_patch_forest(sf):
        '-> len(file_patch_forest)=len_inf_dir(file_patch_forest_dir_path)'
        sz = len_inf_dir(sf.get_file_patch_forest_dir_path(), dir_size=sf.get_dir_size(), min_len=sf.min_len_file_patch_forest_dir)
        sf.min_len_file_patch_forest_dir = sz
        return sz
    @override
    def get_len_inf_dir_of_branch_history(sf, branch_name):
        'branch_name -> len(branch_name2branch_history[branch_name])=len_inf_dir(branch_history_dir_path)'
        sz = len_inf_dir(sf.get_branch_history_dir_path(branch_name), dir_size=sf.get_dir_size(), min_len=sf.branch_name2min_len_branch_history_dir.get(branch_name, 0))
        sf.branch_name2min_len_branch_history_dir[branch_name] = sz
        return sz

class IRepositorySetting__init_caches(IRepositorySetting):
    def __init__(sf, /):
        sf.branch_time2root_fsys_dict = {}
    @override
    def get_cache__branch_time2root_fsys_dict(sf):
        r'''-> branch_time2root_fsys_dict #{(branch_name, branch_idx):root_fsys_dict}
        to impl: extract_may_root_fsys_dict_at_branch_time
        #'''
        return sf.branch_time2root_fsys_dict
class IRepositorySetting__init_constants(IRepositorySetting):
    def __init__(sf, /,*, ignorefile_relative_paths, parentfile_relative_path, contentfile_relative_path, metadatafile_relative_path, dir_size, lcp_threshold, repository_root_dir_path, repository_extra_cache_root_dir_path, command_history_dir_relative_path, file_patch_forest_dir_relative_path):
        sf.__dict__.update(locals())
        del sf.__dict__['sf']


        check_int(dir_size, min=2)
        check_uint(lcp_threshold)


        check_tuple(ignorefile_relative_paths)
        check_all(check_relative_path, ignorefile_relative_paths)


        check_path(repository_root_dir_path)
        check_path(repository_extra_cache_root_dir_path)


        check_relative_path(parentfile_relative_path)
        check_relative_path(contentfile_relative_path)
        check_relative_path(metadatafile_relative_path)
        check_relative_path(command_history_dir_relative_path)
        check_relative_path(file_patch_forest_dir_relative_path)

    @override
    def get_ignorefile_relative_paths_under_working_root_dir(sf):
        '-> [ignorefile_relative_path] # or(ignores)'
        return sf.ignorefile_relative_paths

    @override
    def get_parentfile_relative_path_under_user_data_dir(sf):
        '-> parentfile_relative_path'
        return sf.parentfile_relative_path
    @override
    def get_contentfile_relative_path_under_user_data_dir(sf):
        '-> contentfile_relative_path'
        return sf.contentfile_relative_path
    @override
    def get_metadatafile_relative_path_under_user_data_dir(sf):
        '-> metadatafile_relative_path'
        return sf.metadatafile_relative_path
    @override
    def get_dir_size(sf):
        '-> dir_size'
        return sf.dir_size
    @override
    def get_lcp_threshold(sf):
        '-> lcp_threshold'
        return sf.lcp_threshold
    @override
    def get_repository_root_dir_path(sf):
        '-> repository_root_dir_path'
        return sf.repository_root_dir_path
    @override
    def get_repository_extra_cache_root_dir_path(sf):
        '-> repository_extra_cache_root_dir_path'
        return sf.repository_extra_cache_root_dir_path
    @override
    def get_command_history_dir_relative_path(sf):
        '-> command_history_dir_relative_path'
        return sf.command_history_dir_relative_path
    @override
    def get_file_patch_forest_dir_relative_path(sf):
        '-> file_patch_forest_dir_relative_path'
        return sf.file_patch_forest_dir_relative_path

class IRepositorySetting__init_constants__branches_together(IRepositorySetting__init_constants, IRepositorySetting__branches_together):
    def __init__(sf, /,*, branches_dir_relative_path, ignorefile_relative_paths, parentfile_relative_path, contentfile_relative_path, metadatafile_relative_path, dir_size, lcp_threshold, repository_root_dir_path, repository_extra_cache_root_dir_path, command_history_dir_relative_path, file_patch_forest_dir_relative_path):
        check_relative_path(branches_dir_relative_path)
        sf.branches_dir_relative_path = branches_dir_relative_path
        d = dict(locals())
        del d['sf']
        del d['branches_dir_relative_path']

        super().__init__(**d)
    @override
    def get_branches_dir_relative_path(sf):
        '-> branches_dir_relative_path'
        return sf.branches_dir_relative_path
class IRepositorySetting__init_constants__branches_together__cache_min_len_inf_dir__init_caches(IRepositorySetting__init_caches, IRepositorySetting__init_constants__branches_together, IRepositorySetting__cache_min_len_inf_dir):
    def __init__(sf, /,*, min_len_command_history_dir, min_len_file_patch_forest_dir, branch_name2min_len_branch_history_dir, branches_dir_relative_path, ignorefile_relative_paths, parentfile_relative_path, contentfile_relative_path, metadatafile_relative_path, dir_size, lcp_threshold, repository_root_dir_path, repository_extra_cache_root_dir_path, command_history_dir_relative_path, file_patch_forest_dir_relative_path):
        d = dict(locals())
        del d['sf']

        def f(min_len_command_history_dir, min_len_file_patch_forest_dir, branch_name2min_len_branch_history_dir, **kw):
            del kw
            IRepositorySetting__cache_min_len_inf_dir.__init__(sf, **locals())

        def g(branches_dir_relative_path, ignorefile_relative_paths, parentfile_relative_path, contentfile_relative_path, metadatafile_relative_path, dir_size, lcp_threshold, repository_root_dir_path, repository_extra_cache_root_dir_path, command_history_dir_relative_path, file_patch_forest_dir_relative_path, **kw):
            del kw
            IRepositorySetting__init_constants__branches_together.__init__(sf, **locals())
        f(**d)
        g(**d)
        IRepositorySetting__init_caches.__init__(sf)



#HHHHH
re
uint_pattern = fr'(?:0|[1-9][0-9]*)'
branch_name_char_pattern = fr'(?:(?!=\\)\S)' #can include '/' but not '\'
branch_name_pattern = fr'(?:{branch_name_char_pattern}+)' #can include '/' but not '\'
#IRepositorySetting.move_cmd_target__user_data_file__virtual_names
#user_data_file__virtual_name
user_data_file__virtual_name__pattern = branch_name_pattern

push2command_history_pattern = fr'(?:pop updating/file_stack\[(?P<idx4file_stack>{uint_pattern})\] -> push_into (?P<move_cmd_target__virtual_dir>grow_only/command_history)\[(?P<idx4move_cmd_target>{uint_pattern})\])'
#branch_fsys_history, branch_history
push2branch_fsys_history_pattern = fr'(?:pop updating/file_stack\[(?P<idx4file_stack>{uint_pattern})\] -> push_into (?P<move_cmd_target__virtual_dir>grow_only/branches/(?P<branch_name>{branch_name_pattern}))\[(?P<idx4move_cmd_target>{uint_pattern})\])'
move2file_patch_forest_pattern = fr'(?:pop updating/file_stack\[(?P<idx4file_stack>{uint_pattern})\] -> move_to (?P<move_cmd_target__virtual_dir>(?P<user_data_file__virtual_name>{user_data_file__virtual_name__pattern}) @ grow_only/file_patch_forest)\[(?P<idx4move_cmd_target>{uint_pattern})\])'
move_cmd_line_pattern = '(?:{push2command_history_pattern}|{push2branch_fsys_history_pattern}|{move2file_patch_forest_pattern})'
move2file_patch_forest_regex = re.compile(move2file_patch_forest_pattern)

class IRepositorySetting__default_move_cmd_line_fmt(IRepositorySetting):
    r'''
    read_move_cmds
    ___read_move_cmds___

    default_move_cmd_line_fmt:
        move_cmd_line_fmt from IRepositorySetting.read_move_cmds.__doc__

        * pop updating/file_stack[{i}] -> push_into grow_only/command_history[{j}]

        * pop updating/file_stack[{i}] -> push_into grow_only/branches/{branch_name}[{j}]

        * pop updating/file_stack[{i}] -> move_to parent @ grow_only/file_patch_forest[{j}]
        * pop updating/file_stack[{i}] -> move_to content @ grow_only/file_patch_forest[{j}]
        * pop updating/file_stack[{i}] -> move_to metadata @ grow_only/file_patch_forest[{j}]
    #'''

    @override
    def ___read_move_cmds___(sf, TODO_list4move_cmd_ifile):
        r'''binary_ifile -> [(idx4file_stack, move_cmd_target, move_cmd_target_args, idx4move_cmd_target)]
        see: read_move_cmds
        #'''
        return tuple(sf.__iter_read_move_cmds(TODO_list4move_cmd_ifile))
    def __iter_read_move_cmds(sf, TODO_list4move_cmd_ifile):
        text_ifile = reopen_bin2txt(binary_ifile, encoding='utf8')
        for line in text_ifile:
            line = line.strip()
            if line[:1] in '#': continue
            m = move2file_patch_forest_regex.fullmatch(line)
            if not m:
                raise ValueError(f'bad move_cmd_line: {line!r}')
            idx4file_stack = int(m['idx4file_stack'])
            idx4move_cmd_target = int(m['idx4move_cmd_target'])
            move_cmd_target__virtual_dir = m['move_cmd_target__virtual_dir']
            if move_cmd_target__virtual_dir == 'grow_only/command_history':
                move_cmd_target = 'push_into_command_history'
                move_cmd_target_args = ()
            elif move_cmd_target__virtual_dir.endswith('grow_only/file_patch_forest'):
                user_data_file__virtual_name = m['user_data_file__virtual_name']
                _user_data_file__virtual_name, _at, _dir = move_cmd_target__virtual_dir.split()
                assert user_data_file__virtual_name == _user_data_file__virtual_name
                if user_data_file__virtual_name not in sf.move_cmd_target__user_data_file__virtual_names: raise ValueError(f'bad move_cmd_line: unknown user_data_file__virtual_name={user_data_file__virtual_name!r} : line={line!r}')

                move_cmd_target = 'move_into_file_patch_forest'
                move_cmd_target_args = (user_data_file__virtual_name,)
            elif move_cmd_target__virtual_dir.startswith('grow_only/branches/'):
                branch_name = m['branch_name']
                _branch_name = move_cmd_target__virtual_dir[len('grow_only/branches/'):]
                assert branch_name == _branch_name

                move_cmd_target = 'push_into_branch_fsys_history'
                move_cmd_target_args = (branch_name,)
            else:
                raise logic-err
            move_cmd_target
            move_cmd_target_args

            yield (idx4file_stack, move_cmd_target, move_cmd_target_args, idx4move_cmd_target)



#HHHHH
class IRepositorySetting__using_IFileSystem4update__fsys_delta(IRepositorySetting):
    'fsys_delta = fsys_update_cmd | branch_history_cmd'

    @abstractmethod
    def mk_fsys_updater(sf, branch_name2min_extracting_branch_idx, fsys_delta_init_ifile):
        '{branch_name:min_extracting_branch_idx} -> binary_ifile -> IFileSystem4update__fsys_delta'

    @abstractmethod
    def iter_read_fsys_delta_objs(sf, fsys_delta_seq_ifile):
        'binary_ifile -> Iter fsys_delta'
        obj = read_repred_py_obj(fsys_delta_seq_ifile)
        return iter(obj) or iter([obj])


    def _fsys_updater_iadd(sf, fsys_updater, fsys_delta_seq_ifile):
        'fsys_updater -> binary_ifile -> None'
        it = sf.iter_read_fsys_delta_objs(fsys_delta_seq_ifile)
        for fsys_delta in it:
            fsys_updater.apply_fsys_delta(fsys_delta)


    @override
    def ___extract_may_root_fsys_dict_at_branch_time___(sf, branch_name2min_extracting_branch_idx, branch_name, branch_idx):
        r'''
        branch_name2min_extracting_branch_idx -> branch_name -> branch_idx -> (None|root fsys_dict)'
        see: extract_may_root_fsys_dict_at_branch_time
        #'''
        branch_history_dir_path = sf.get_branch_history_dir_path(branch_name)
        inf_dir_path = branch_history_dir_path
        dir_size = sf.get_dir_size()
        def open_idx(inf_dir_idx):
            return open_under_inf_dir(dir_size, inf_dir_path, inf_dir_idx, None, 'rb')

        with open_idx(0) as fsys_delta_init_ifile:
            fsys_updater = sf.mk_fsys_updater(branch_name2min_extracting_branch_idx, fsys_delta_init_ifile)

        for i in range(1, branch_idx+1):
            with open_idx(i) as fsys_delta_seq_ifile:
                sf._fsys_updater_iadd(fsys_updater, fsys_delta_seq_ifile)
        may_root_fsys_dict = fsys_updater.deepcopy_may_root_fsys_dict()
        return may_root_fsys_dict



ast.literal_eval
read_repred_py_obj
#HHHHH
class IRepositorySetting__using_IFileSystem4update__fsys_delta_is_branch_history_cmd(IRepositorySetting__using_IFileSystem4update__fsys_delta):
    @override
    def mk_fsys_updater(sf, branch_name2min_extracting_branch_idx, fsys_delta_init_ifile):
        '{branch_name:min_extracting_branch_idx} -> binary_ifile -> IFileSystem4update__fsys_delta'
        T = FileSystem4update__fsys_delta_is_fsys_update_cmd
        T = FileSystem4update__fsys_delta_is_branch_history_cmd
        repository_setting = sf
        fsys_updater = T(branch_name2min_extracting_branch_idx, repository_setting)
        fsys_delta_seq_ifile = fsys_delta_init_ifile
        sf._fsys_updater_iadd(fsys_updater, fsys_delta_seq_ifile)
        return fsys_updater


    @override
    def iter_read_fsys_delta_objs(sf, fsys_delta_seq_ifile):
        'binary_ifile -> Iter fsys_delta'
        cmds = read_repred_py_obj(fsys_delta_seq_ifile)
        if not type(cmds) is tuple: raise TypeError
        for cmd in cmds:
            check_cmd(cmd)
        return iter(cmds)



#HHHHH
class IRepositorySetting__using_IFileSystem4update__fsys_delta_is_fsys_update_cmd(IRepositorySetting__using_IFileSystem4update__fsys_delta):
    @override
    def mk_fsys_updater(sf, branch_name2min_extracting_branch_idx, fsys_delta_init_ifile):
        '{branch_name:min_extracting_branch_idx} -> binary_ifile -> IFileSystem4update__fsys_delta'
        T = FileSystem4update__fsys_delta_is_branch_history_cmd
        T = FileSystem4update__fsys_delta_is_fsys_update_cmd
        repository_setting = sf
        fsys_updater = T()
        fsys_delta_seq_ifile = fsys_delta_init_ifile
        sf._fsys_updater_iadd(fsys_updater, fsys_delta_seq_ifile)
        return fsys_updater


    @override
    def iter_read_fsys_delta_objs(sf, fsys_delta_seq_ifile):
        'binary_ifile -> Iter fsys_delta'
        cmd = read_repred_py_obj(fsys_delta_seq_ifile)
        check_cmd(cmd)
        cmds = [cmd]
        return iter(cmds)




class RepositorySetting__using_IFileSystem4update__fsys_delta_is_fsys_update_cmd(IRepositorySetting__using_IFileSystem4update__fsys_delta_is_fsys_update_cmd, IRepositorySetting__default_move_cmd_line_fmt, IRepositorySetting__init_constants__branches_together__cache_min_len_inf_dir__init_caches): pass
class RepositorySetting__using_IFileSystem4update__fsys_delta_is_branch_history_cmd(IRepositorySetting__using_IFileSystem4update__fsys_delta_is_branch_history_cmd, IRepositorySetting__default_move_cmd_line_fmt, IRepositorySetting__init_constants__branches_together__cache_min_len_inf_dir__init_caches): pass




r'''
IDirViewer
    fsys_dict
IPseudoFile4MkIsSameFile
IAccessFile4MkIsSameFile
    fsys_dict
    IRepositorySetting
#'''

ast.literal_eval('...')


#HHHHH
def get_tmay_sub_fsys_dict_or_patch_idx(root_fsys_dict_or_patch_idx, relative_path:'relative PurePosixPath'):
    '(fsys_dict|patch_idx) -> relative PurePosixPath -> (()|((fsys_dict|patch_idx),)) # tmay'
    (parts, depth, sub_fsys_dict_or_patch_idx) = cd_to_sub_fsys_dict_or_patch_idx_ex_as_deep_as_possible(root_fsys_dict_or_patch_idx, relative_path)
    if depth != len(parts):
        return ()
    else:
        return (sub_fsys_dict_or_patch_idx,)
def cd_to_sub_fsys_dict_or_patch_idx_ex_as_deep_as_possible(root_fsys_dict_or_patch_idx, relative_path:'relative PurePosixPath'):
    r'''
    root_fsys_dict_or_patch_idx -> relative_path -> (parts, depth, sub_fsys_dict_or_patch_idx)
    (fsys_dict|patch_idx) -> relative PurePosixPath -> ((parts::tuple<basename>), (depth<-[0..len(parts)]), (fsys_dict|patch_idx))

    sub_fsys_dict_or_patch_idx is cd root_fsys_dict_or_patch_idx parts[:depth]
    0 <= depth <= len(parts)
    [sub_fsys_dict_or_patch_idx is fsys_dict] ==>> [depth==len(parts)]or[parts[depth] not under sub_fsys_dict]
    #'''
    assert not relative_path.is_absolute()
    parts = relative_path2parts(relative_path)
    depth = 0
    curr_fsys_dict_or_patch_idx = root_fsys_dict_or_patch_idx
    Nothing = object()
    for basename in parts:
        if type(curr_fsys_dict_or_patch_idx) is int:
            curr_patch_idx = curr_fsys_dict_or_patch_idx
            #file is not dir
            break
        else:
            #dir/basename
            curr_fsys_dict = curr_fsys_dict_or_patch_idx
            may_child = curr_fsys_dict.get(basename, Nothing)
            if may_child is Nothing:
                break
            else:
                child = may_child
        curr_fsys_dict_or_patch_idx = child
        depth += 1
    sub_fsys_dict_or_patch_idx = curr_fsys_dict_or_patch_idx
    assert 0 <= depth <= len(parts)
    return (parts, depth, sub_fsys_dict_or_patch_idx)

#HHHHH

def access_path__fsys_dict(root_fsys_dict_or_patch_idx, relative_path:'PurePosixPath&not is_absolute()', /,*, with_case:bool, with_exc:bool, with_args:bool):
    '(fsys_dict|patch_idx) -> relative PurePosixPath -> (with_case,with_exc,with_args:bool) -> (("not_exists"|"is_file"|"is_dir")?<<==with_case?, (FileNotFoundError|NotADirectoryError|IsADirectoryError)?<<==with_exc, *(root_fsys_dict_or_patch_idx,relative_path)?<<==with_args?, (|patch_idx|fsys_dict))'
    assert not relative_path.is_absolute()

    m = get_tmay_sub_fsys_dict_or_patch_idx(root_fsys_dict_or_patch_idx, relative_path)
    if not m:
        r = ('not_exists', FileNotFoundError, root_fsys_dict_or_patch_idx, relative_path)
        #raise FileNotFoundError
    else:
        [sub_fsys_dict_or_patch_idx] = m
        if type(sub_fsys_dict_or_patch_idx) is int:
            sub_patch_idx = sub_fsys_dict_or_patch_idx
            r = ('is_file', NotADirectoryError, root_fsys_dict_or_patch_idx, relative_path, sub_patch_idx)
            #raise NotADirectoryError
        else:
            sub_fsys_dict = sub_fsys_dict_or_patch_idx
            r = ('is_dir', IsADirectoryError, root_fsys_dict_or_patch_idx, relative_path, sub_fsys_dict)
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




#HHHHH
class DirViewer__fsys_dict(IDirViewer):
    r'''
    #path::Path
    path::relative PurePosixPath
    #'''
    def __init__(sf, fsys_dict):
        check_fsys_dict(fsys_dict)
        sf.fsys_dict = fsys_dict

    @override
    def __is_file__(sf, path):
        'path -> (bool|raise FileNotFoundError)'
        if 1:
            assert not path.is_absolute()
            root_fsys_dict_or_patch_idx = sf.fsys_dict
            relative_path = path
            r = access_path__fsys_dict(root_fsys_dict_or_patch_idx, relative_path, with_case=True, with_exc=True, with_args=False)
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
            m = get_tmay_sub_fsys_dict_or_patch_idx(sf.fsys_dict, path)
            if not m: raise FileNotFoundError
            [root_fsys_dict_or_patch_idx] = m
            return type(root_fsys_dict_or_patch_idx) is int

    @override
    def dir_iter(sf, dir_path):
        'dir_path -> (Iter basename | raise FileNotFoundError/NotADirectoryError)'
        if 1:
            assert not dir_path.is_absolute()
            root_fsys_dict_or_patch_idx = sf.fsys_dict
            relative_path = dir_path
            r = access_path__fsys_dict(root_fsys_dict_or_patch_idx, relative_path, with_case=True, with_exc=True, with_args=False)
            case, exc, *m = r
            if case=='not_exists':
                raise exc
            elif case=='is_file':
                raise exc
            elif case=='is_dir':
                [sub_fsys_dict] = m
                return iter(sub_fsys_dict)
            else:
                raise logic-err
            raise logic-err
            return
        else:
            assert not dir_path.is_absolute()
            m = get_tmay_sub_fsys_dict_or_patch_idx(sf.fsys_dict, dir_path)
            if not m: raise FileNotFoundError
            [root_fsys_dict_or_patch_idx] = m
            if type(root_fsys_dict_or_patch_idx) is int:
                patch_idx = root_fsys_dict_or_patch_idx
                raise NotADirectoryError
            else:
                fsys_dict = root_fsys_dict_or_patch_idx
                return iter(fsys_dict)

    @override
    def exists(sf, path):
        'path -> bool'
        assert not path.is_absolute()
        return bool(get_tmay_sub_fsys_dict_or_patch_idx(sf.fsys_dict, path))


#HHHHH
class AccessFile4MkIsSameFile__backup_util_repository__fsys_dict__IRepositorySetting(IAccessFile4MkIsSameFile):
    r'''
    for MkIsSameFile
    #path::Path
    virtual_file_path :: relative PurePosixPath
    #'''
    def __init__(sf, repository_setting:IRepositorySetting, fsys_dict):
        if not isinstance(repository_setting, IRepositorySetting):raise TypeError
        check_fsys_dict(fsys_dict)

        sf.repository_setting = repository_setting
        sf.fsys_dict = fsys_dict
        sf.metadata_cache = {}

    def virtual_file_path2real_user_data_dir_path(sf, virtual_file_path):
        'virtual file_path@fsys_dict -> real user_data_dir_path@fsys'
        patch_idx = sf.virtual_file_path2patch_idx(virtual_file_path)
        user_data_dir_path = sf.patch_idx2real_user_data_dir_path(patch_idx)
        return user_data_dir_path

    def patch_idx2real_user_data_dir_path(sf, patch_idx):
        'patch_idx -> real user_data_dir_path@fsys'
        return sf.repository_setting.patch_idx2user_data_dir_path(patch_idx)

    def virtual_file_path2patch_idx(sf, virtual_file_path):
        'virtual file_path@fsys_dict -> patch_idx'
        assert not virtual_file_path.is_absolute()
        fsys_dict_or_patch_idx = sf.fsys_dict
        relative_path = virtual_file_path
        r = access_path__fsys_dict(fsys_dict_or_patch_idx, relative_path, with_case=True, with_exc=True, with_args=False)
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





    def get_metadata(sf, virtual_file_path):
        'virtual_file_path -> metadata'
        assert not virtual_file_path.is_absolute()
        m = sf.metadata_cache_lookup(virtual_file_path)
        if m:
            [metadata] = m
        else:
            metadatafile_path = sf.virtual_file_path2real_user_data_dir_path(virtual_file_path) / sf.repository_setting.get_metadatafile_relative_path_under_user_data_dir()
            with open(metadatafile_path, 'rb') as metadata_ifile:
                metadata = sf.repository_setting.read_metadata(metadata_ifile)
            sf.metadata_cache_put(virtual_file_path, metadata)
            metadata
        metadata
        return metadata


    @override
    def get_file_size(sf, virtual_file_path):
        'virtual_file_path -> uint # unit:byte'
        assert not virtual_file_path.is_absolute()
        metadata = sf.get_metadata(virtual_file_path)
        return metadata['whole_file_size']
    @override
    def get_may_hash_method_uppercase_std_name2digest(sf, virtual_file_path):
        'virtual_file_path -> (None|hash_method_uppercase_std_name2digest::{name:hex}) #name <- {SHA256, MD5, ...}'
        assert not virtual_file_path.is_absolute()
        metadata = sf.get_metadata(virtual_file_path)
        return metadata['may_hash_method_uppercase_std_name2digest']
            #must exist, but can be empty or None!
        return metadata.get('hash_method_uppercase_std_name2digest')
    @override
    def get_may_str_mtime(sf, virtual_file_path):
        r'''virtual_file_path -> (None|str_time) # %Y%m%d_%H%M%S_%z # == STR_TIME_FORMAT
    # ends with constant %z == +0000
        #'''
        assert not virtual_file_path.is_absolute()
        metadata = sf.get_metadata(virtual_file_path)
        return metadata['may_str_mtime']
    #def _float_time2str_time(float_time):


    def metadata_cache_lookup(sf, virtual_file_path):
        '-> tmay metadata'
        if virtual_file_path in sf.metadata_cache:
            return (sf.metadata_cache[virtual_file_path],)
        else:
            return ()
    def metadata_cache_put(sf, virtual_file_path, metadata):
        sf.metadata_cache[virtual_file_path] = metadata

    @override
    def open(sf, virtual_file_path):
        'virtual_file_path -> IPseudoFile4MkIsSameFile'
        assert not virtual_file_path.is_absolute()
        patch_idx = sf.virtual_file_path2patch_idx(virtual_file_path)
        file_patch_forest_dir_path = sf.repository_setting.get_file_patch_forest_dir_path()
        reversed_case_either_bytes_pairs = inf_dir_idx2iter_imay_parent_idx_content_bytes_pairs__inf_dir_as_forest(file_patch_forest_dir_path, patch_idx
            ,dir_size=sf.repository_setting.get_dir_size()
            ,user_data_dir_path_setting=sf.repository_setting
            )

        latest_file_bytes = reversed_case_either_bytes_pairs2latest_file_bytes__forest__file_cmp__ver1(reversed_case_either_bytes_pairs, case2is_patch=case2is_patch__case_is_imay_parent_idx)
        #fin = io.BytesIO(latest_file_bytes)
        fin = bytes2PseudoFile4MkIsSameFile(latest_file_bytes)
        return fin




#HHHHH
IPseudoFile4MkIsSameFile
class bytes2PseudoFile4MkIsSameFile(IPseudoFile4MkIsSameFile):
    r'''
    for MkIsSameFile
    path::Path
    #'''
    def __init__(sf, bs:bytes, /):
        sf.__bs = bs
        sf.__pos = 0

    @override
    def read(sf, num_bytes):
        'uint -> bytes'
        assert num_bytes >= 0
        if num_bytes <= 0:
            bs = sf.__bs[sf.__pos:]
        else:
            bs = sf.__bs[sf.__pos:sf.__pos+num_bytes]
        sf.__pos += len(bs)
        return bs
    #context manager
    @override
    def __enter__(sf):
        return sf
    @override
    def __exit__(self, exc_type, exc_value, traceback):
        pass
    pass
pass









def dir_cmp__relative__with_IRepositorySetting(lhs_repository_setting:IRepositorySetting, lhs_branch_name, lhs_may_branch_idx, lhs_may_relative_path, rhs_path, rhs_dir_viewer:IDirViewer, rhs_access_file, /,*, kwargs4MkIsSameFile, kwargs4dir_cmp__relative):
    r'''
    dir_cmp__relative
def dir_cmp__relative(is_same_file, lhs_dir_viewer, lhs_path, rhs_dir_viewer, rhs_path, /, *, ignore_relative_path, ignore_basename, max_depth):
    is_same_file = MkIsSameFile
        def __init__(sf, lhs_access_file, rhs_access_file, /, *, always_tribool_as_is_or_not_same_file:'tribool', size_eq_as_same_file:bool, size_hash0_eq_as_same_file:bool, hash_eq_as_same_file:bool, mtime_eq_as_same_file:bool, mtime_ne_as_not_same_file:bool, _block_size):

    lhs_access_file = AccessFile4MkIsSameFile__backup_util_repository__fsys_dict__IRepositorySetting
        def __init__(sf, repository_setting:IRepositorySetting, fsys_dict):

    lhs_dir_viewer = DirViewer__fsys_dict
        def __init__(sf, fsys_dict):

    fsys_dict = lhs_repository_setting
        def extract_may_root_fsys_dict_at_branch_time(sf, branch_name2min_extracting_branch_idx, branch_name, branch_idx):
    #'''
    mov bytes2PseudoFile4MkIsSameFile to dir_cmp.py
    RecurView__fsys_mapping_ex.deepcopy_as_fsys_dict_ex ...
    mk_fsys_mapping_view
    fsys_dict < fsys_mapping
    fsys_mapping_view < fsys_mapping


    lhs_branch_idx
        lhs_may_branch_idx
    may_root_fsys_dict = lhs_repository_setting.extract_may_root_fsys_dict_at_branch_time({}, lhs_branch_name, lhs_branch_idx)
    fsys_dict
        may_root_fsys_dict
    lhs_path
        lhs_may_relative_path

    lhs_access_file = AccessFile4MkIsSameFile__backup_util_repository__fsys_dict__IRepositorySetting(lhs_repository_setting, fsys_dict)
    is_same_file = MkIsSameFile(lhs_access_file, rhs_access_file, **kwargs4MkIsSameFile)
    lhs_dir_viewer = DirViewer__fsys_dict(fsys_dict)
    return dir_cmp__relative(is_same_file, lhs_dir_viewer, lhs_path, rhs_dir_viewer, rhs_path, **kwargs4dir_cmp__relative):

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
