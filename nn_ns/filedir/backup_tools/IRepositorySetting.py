
r'''

copy...dict
    copy_fsys_dict
        echo_valueonly_fsys_mapping
__dict__

fsys_dict
    -->> fsys_frozendict
    extract_may_root_fsys_dict_at_branch_time
        -->> extract_may_root_fsys_frozendict_at_branch_time



===============





#'''




__all__ = '''
    echo_valueonly_fsys_mapping
    metadata_keys_setting
    reopen_bin2txt
    read_repred_py_obj
    write_py_obj_as_repr
    check_metadata
    IRepositorySetting__user_data_dir_path
    IRepositorySetting__repository_root_dir_path
    check_ignorefile_relative_path_encoding_pairs
    IRepositorySetting__working_root_dir_path
    IRepositorySetting
    IRepositorySetting__branches_together
    check_path
    IRepositorySetting__cache_min_len_inf_dir
    IRepositorySetting__init_caches
    IRepositorySetting__init_constants
    IRepositorySetting__init_constants__branches_together
    IRepositorySetting__init_constants__branches_together__cache_min_len_inf_dir__init_caches
    uint_pattern
    branch_name_char_pattern
    branch_name_pattern
    user_data_file__virtual_name__pattern
    push2command_history_pattern
    push2branch_fsys_history_pattern
    move2file_patch_forest_pattern
    move_cmd_line_pattern
    move2file_patch_forest_regex
    branch_name_regex
    check_branch_name
    check_branch_time
    IRepositorySetting__default_move_cmd_line_fmt
    '''.split()


___begin_mark_of_excluded_global_names__0___ = ...
from nn_ns.filedir.backup_tools.fsys_mapping_ex import using_FrozenDict_as_valueonly_fsys_mapping_ex, check_fsys_frozendict
from nn_ns.filedir.relative_path_ops import check_relative_path, str2relative_path, check_relative_path__str, relative_path2str
from nn_ns.filedir.inf_dir import pop_from_inf_dir_and_move, pop_from_inf_dir_and_push_into_another, inf_dir_remove_tail_empty_dirs, len_inf_dir, inf_dir_idx2user_data_relative_path, mk_target_path_under_inf_dir, inf_dir_end_based_idx2begin_based_idx
from nn_ns.filedir.filedir_ops import is_dir_empty
from nn_ns.filedir.dir_cmp import IPseudoFile4MkIsSameFile


from seed.for_libs.for_io.stream_obj_converter import binary_stream_obj2text_stream_obj

from seed.helper.check.checkers import check_uint_imay, check_uint, check_all, check_str, check_int, check_tuple, check_nmay, check_pair
from seed.tiny import echo, fst

import re
import shutil
import ast
import os.path
from pathlib import Path
from abc import ABC, abstractmethod
from seed.abc.abc import override

___end_mark_of_excluded_global_names__0___ = ...


if using_FrozenDict_as_valueonly_fsys_mapping_ex:
    #echo_valueonly_fsys_mapping_or_patch_idx = echo
    echo_valueonly_fsys_mapping = echo




#HHHHH
class metadata_keys_setting:
    #must exist, but can be empty or None!
    key4may_hash_method_uppercase_std_name2upper_hex_digest = 'may_hash_method_uppercase_std_name2upper_hex_digest'
    key4may_str_mtime = 'may_str_mtime'
    key4file_size = 'whole_file_size'


def reopen_bin2txt(binary_ifile, /,*, encoding, buffered_case):
    text_ifile = binary_stream_obj2text_stream_obj(binary_ifile, encoding=encoding, buffered_case=buffered_case, kwargs4buffered_binary_stream={}, kwargs4text_stream={})
    return text_ifile

def read_repred_py_obj(binary_ifile, /):
    text_ifile = reopen_bin2txt(binary_ifile, encoding='utf8', buffered_case='read')
    s = text_ifile.read()
    obj = ast.literal_eval(s)
    return obj
def write_py_obj_as_repr(binary_ofile, obj, /):
    'see:read_repred_py_obj'
    s = repr(obj)
    if ast.literal_eval(obj) != obj: raise ValueError
    text_ofile = reopen_bin2txt(binary_ofile, encoding='utf8', buffered_case='write')
    text_ofile.write(s)
    return

def check_metadata(metadata, /):
    'see?: metadata_keys_setting'
    #check_dict(check_str, None, metadata)
    if not type(metadata) is dict: raise TypeError
    if not all(type(k) is str for k in metadata): raise TypeError
    attrs = dir(metadata_keys_setting)
    for attr in attrs:
        if attr.startswith('key4'):
            key = getattr(metadata_keys_setting, attr)
            if key not in metadata: raise ValueError(f'missing key@metadata: {key!r}')


#HHHHH
class IRepositorySetting__user_data_dir_path(ABC):
    r'''
    user_data_dir_path_setting
    user_data_dir is the inf_dir element of file_patch_forest_dir
    below relative_path are relative_to any user_data_dir
    #'''

    @abstractmethod
    def get_parentfile_relative_path_under_user_data_dir(sf, /):
        '-> parentfile_relative_path'
        return str2relative_path('parent')
    @abstractmethod
    def get_contentfile_relative_path_under_user_data_dir(sf, /):
        '-> contentfile_relative_path'
        return str2relative_path('content')
    @abstractmethod
    def get_metadatafile_relative_path_under_user_data_dir(sf, /):
        '-> metadatafile_relative_path'
        return str2relative_path('metadata')


    #no read/write contentfile !
    #   since vary cases

    @abstractmethod
    def read_metadata(sf, metadata_ifile, /):
        'input_binary_file -> metadata'
    @abstractmethod
    def write_metadata(sf, metadata_ofile, metadata, /):
        'output_binary_file -> metadata -> None'
    @abstractmethod
    def read_imay_parent_idx(sf, imay_parent_idx_ifile, /):
        'input_binary_file -> [-1..] # imay'
        #return _read_imay_parent__user_data(imay_parent_idx_ifile)
        #s = parent_path.read_text(encoding='ascii')
        #bs = imay_parent_idx_ifile.read()
        #s = bs.decode(encoding='ascii')
        imay_parent_idx = read_repred_py_obj(imay_parent_idx_ifile)
        check_uint_imay(imay_parent_idx)
        return imay_parent_idx

    @abstractmethod
    def write_imay_parent_idx(sf, imay_parent_idx_ofile, imay_parent_idx, /):
        'output_binary_file -> [-1..] -> None # imay'

#HHHHH
class IRepositorySetting__repository_root_dir_path(ABC):
    r'''
    repository_root_dir_path_setting
    repository_root_dir is the root dir to backup to
    below relative_path are relative_to the repository_root_dir
    #'''



    @abstractmethod
    def get_repository_root_dir_path(sf, /):
        '-> repository_root_dir_path'

    #updating/
    @abstractmethod
    def get_file_stack_dir_relative_path(sf, /):
        '-> file_stack_dir_relative_path'
        return str2relative_path('updating/file_stack')
    @abstractmethod
    def get_TODO_list4move_cmd_file_relative_path(sf, /):
        '-> TODO_list4move_cmd_file_relative_path'
        return str2relative_path('updating/TODO_list4move_cmd')
    @abstractmethod
    def get_commit_completed_file_relative_path(sf, /):
        '-> commit_completed_file_relative_path'
        return str2relative_path('updating/commit_completed')


    #grow_only/
    @abstractmethod
    def get_command_history_dir_relative_path(sf, /):
        '-> command_history_dir_relative_path'
        return str2relative_path('grow_only/command_history')
    @abstractmethod
    def get_file_patch_forest_dir_relative_path(sf, /):
        '-> file_patch_forest_dir_relative_path'
        return str2relative_path('grow_only/file_patch_forest')
    @abstractmethod
    def get_branch_history_dir_relative_path(sf, branch_name, /):
        'branch_name -> branch_history_dir_relative_path'


    #get len_inf_dir of grow_only/...
    #   cache a min value
    #   not include updating/file_stack which will pop
    #
    @abstractmethod
    def get_len_inf_dir_of_command_history(sf, /):
        '-> len(command_history)=len_inf_dir(command_history_dir_path)'
    @abstractmethod
    def get_len_inf_dir_of_file_patch_forest(sf, /):
        '-> len(file_patch_forest)=len_inf_dir(file_patch_forest_dir_path)'
    @abstractmethod
    def get_len_inf_dir_of_branch_history(sf, branch_name, /):
        'branch_name -> len(branch_name2branch_history[branch_name])=len_inf_dir(branch_history_dir_path)'








    #grow_only
    def get_command_history_dir_path(sf, /):
        '-> command_history_dir_path'
        return sf.get_repository_root_dir_path() / sf.get_command_history_dir_relative_path()
    def get_file_patch_forest_dir_path(sf, /):
        '-> file_patch_forest_dir_path'
        return sf.get_repository_root_dir_path() / sf.get_file_patch_forest_dir_relative_path()
    def get_branch_history_dir_path(sf, branch_name, /):
        '-> branch_history_dir_path'
        return sf.get_repository_root_dir_path() / sf.get_branch_history_dir_relative_path(branch_name)


    #updating
    def get_file_stack_dir_path(sf, /):
        '-> file_stack_dir_path'
        return sf.get_repository_root_dir_path() / sf.get_file_stack_dir_relative_path()
    def get_TODO_list4move_cmd_file_path(sf, /):
        '-> TODO_list4move_cmd_file_path'
        return sf.get_repository_root_dir_path() / sf.get_TODO_list4move_cmd_file_relative_path()
    def get_commit_completed_file_path(sf, /):
        '-> commit_completed_file_path'
        return sf.get_repository_root_dir_path() / sf.get_commit_completed_file_relative_path()


    def repository_root_dir_init(sf, /):
        dir_paths = \
            [sf.get_file_patch_forest_dir_path()
            ,sf.get_command_history_dir_path()
            #,sf.get_branch_history_dir_path(branch_name)
            ]

        for dir_path in dir_paths:
            os.mkdirs(dir_path, exist_ok=False)




#HHHHH
def check_ignorefile_relative_path_encoding_pairs(ignorefile_relative_path_encoding_pairs, /):
    check_tuple(ignorefile_relative_path_encoding_pairs)
    for pair in ignorefile_relative_path_encoding_pairs:
        check_pair(pair)
        ignorefile_relative_path, encoding = pair
        check_str(encoding) #not None
        check_relative_path(ignorefile_relative_path)
class IRepositorySetting__working_root_dir_path(ABC):
    r'''
    working_root_dir_path_setting
    working_root_dir is the root dir to backup from
    below relative_path are relative_to the dynamic given working_root_dir
    #'''


    @abstractmethod
    #get_ignorefile_relative_paths_under_working_root_dir
    def get_ignorefile_relative_path_encoding_pairs_under_working_root_dir(sf, /):
        r'''-> [(ignorefile_relative_path, encoding)] # any(ignores) #fold(or, ignores)
        ###
        ignorefile_relative_path_encoding_pairs
        may be empty, default ignore=False #i.e. not ignore
        each ignorefile+path_relative_to_working_root_dir ==>> (ignore::bool)
        fold op False ignores
            ==>> any(ignores)
            ==>> op==or
        ###
        these ignorefile_relative_paths themself are never be ignored
        ###
        encoding shouldnot be None, must be a name
        #'''
    @abstractmethod
    def ___mk_relative_path__str2is_ignore___(sf, ignorefile_text_ifile, /):
        r'''text_ifile -> (std_relative_path__str -> bool)
        see:mk_relative_path2is_ignore
        see:dir_cmp.read_ignorefile/read_ignorefile__text/onoff_patterns_list2ignore_str/onoff_patterns_lists2ignore_str
        #'''

    def mk_relative_path2is_ignore(sf, working_root_dir_path, may_open_ignorefile_text_ifile, /):
        r'''working_root_dir_path -> may(working_root_dir_path -> ignorefile_relative_path -> (encoding:str) -> text_ifile) -> (relative_path -> bool)
        ignorefile_relative_paths should never be ignored!
            any ancestors of ignorefile_relative_paths should never be ignored!
            empty_relative_path should never be ignored!
        default not ignore any files
            ==>> fold by "or" ==>> "any"

        see:dir_cmp.dir_cmp kwargs
        see:dir_cmp.read_ignorefile/read_ignorefile__text/onoff_patterns_list2ignore_str/onoff_patterns_lists2ignore_str
        #'''
        ignorefile_relative_path_encoding_pairs = sf.get_ignorefile_relative_path_encoding_pairs_under_working_root_dir()
        ignorefile_relative_path_encoding_pairs = tuple(ignorefile_relative_path_encoding_pairs)
        check_ignorefile_relative_path_encoding_pairs(ignorefile_relative_path_encoding_pairs)
        ignorefile_relative_path_set = frozenset(map(fst, ignorefile_relative_path_encoding_pairs))
        never_ignored_path_set = ignorefile_relative_path_set.union(ignorefile_relative_path.parents for ignorefile_relative_path in ignorefile_relative_path_set)
        del ignorefile_relative_path_set

        if may_open_ignorefile_text_ifile is None:
            def open_ignorefile_text_ifile(working_root_dir_path, ignorefile_relative_path, /,*, encoding):
                return open(working_root_dir_path/ignorefile_relative_path, 'rt', encoding=encoding)
        else:
            open_ignorefile_text_ifile = may_open_ignorefile_text_ifile
        open_ignorefile_text_ifile

        preds = []
        for ignorefile_relative_path, encoding in ignorefile_relative_path_encoding_pairs:
            with open_ignorefile_text_ifile(working_root_dir_path, ignorefile_relative_path, encoding=encoding) as fin:
                relative_path__str2is_ignore = type(sf).___mk_relative_path__str2is_ignore___(sf, fin)
            preds.append(relative_path__str2is_ignore)


        def dir_cmp__kw__ignore_relative_path(relative_path, /):
            check_relative_path(relative_path)
            if relative_path in never_ignored_path_set:
                ignore = False
            else:
                relative_path__str = relative_path2str(relative_path)
                ignore = any(relative_path__str2is_ignore(relative_path__str) for relative_path__str2is_ignore in preds)
            return ignore
        return dir_cmp__kw__ignore_relative_path


#HHHHH
class IRepositorySetting(IRepositorySetting__working_root_dir_path, IRepositorySetting__repository_root_dir_path, IRepositorySetting__user_data_dir_path):
    r'''repository_setting
    #'''

    @abstractmethod
    def ___open_patch_idx___(sf, iter_tpl5s, /):
        r'''Iter (patch_idx, imay_parent_idx, user_data_dir_path, contentfile_path, content_binary_ifile) -> IPseudoFile4MkIsSameFile
        see: open_patch_idx_ex
        allow to close content_binary_ifile
        #'''

    @abstractmethod
    def ___read_move_cmds___(sf, TODO_list4move_cmd_binary_ifile, /):
        r'''binary_ifile -> move_cmds::[(idx4file_stack, move_cmd_target, move_cmd_target_args, idx4move_cmd_target)]
        see: read_move_cmds
        #'''
    @abstractmethod
    def ___write_move_cmds___(sf, TODO_list4move_cmd_binary_ofile, move_cmds, /):
        r'''
        see: write_move_cmds
        #'''


    @abstractmethod
    def check_branch_history_delta(sf, branch_history_delta, /):
        'branch_history_delta #e.g. FileSystem4update~fsys_delta (= fsys_update_cmd | branch_history_cmd)'
    @abstractmethod
    def ___read_branch_history_deltas___(sf, branch_history_deltas_binary_ifile, /):
        r'''-> branch_history_deltas
        see: read_branch_history_deltas
        #'''
    @abstractmethod
    def ___write_branch_history_deltas___(sf, branch_history_deltas_binary_ofile, branch_history_deltas, /):
        r'''
        see: write_branch_history_deltas
        #'''




    @abstractmethod
    def ___extract_may_root_fsys_frozendict_at_branch_time___(sf, branch_name2min_extracting_branch_idx, branch_name, branch_idx, /):
        r'''
        branch_name2min_extracting_branch_idx -> branch_name -> branch_idx -> (None|root fsys_frozendict)'
        see: extract_may_root_fsys_frozendict_at_branch_time
        #'''
    @abstractmethod
    def get_cache__branch_time2root_fsys_frozendict(sf, /):
        r'''-> branch_time2root_fsys_frozendict #{(branch_name, branch_idx):root_fsys_frozendict}
        to impl: extract_may_root_fsys_frozendict_at_branch_time
        #'''
        #many cache: AccessFile4MkIsSameFile__backup_util_repository__fsys_frozendict__IRepositorySetting.metadata_cache_lookup
        #many cache: IRepositorySetting.get_cache__branch_time2root_fsys_frozendict

    @abstractmethod
    def get_dir_size(sf, /):
        '-> dir_size'
    @abstractmethod
    def get_lcp_threshold(sf, /):
        '-> lcp_threshold'
    @abstractmethod
    def get_repository_extra_cache_root_dir_path(sf, /):
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
                    virtual_file@fsys_frozendict = patch_idx
                    real_file@fsys
                when eq:
                    cache real_file.mtime
                        may not eq virtual_file.metadata.mtime
                    #virtual_file.metadata save mtime
                    #virtual_file.metadata save hash
        #'''

    def patch_idx2metadata(sf, patch_idx, /):
        user_data_dir_path = sf.patch_idx2user_data_dir_path(patch_idx)
        metadatafile_path = user_data_dir_path / sf.get_metadatafile_relative_path_under_user_data_dir()
        with open(metadatafile_path, 'rb') as metadata_ifile:
            metadata = sf.read_metadata(metadata_ifile)
        check_metadata(metadata)
        return metadata


    def patch_idx2imay_parent_idx(sf, patch_idx, /):
        user_data_dir_path = sf.patch_idx2user_data_dir_path(patch_idx)
        parentfile_path = user_data_dir_path / sf.get_parentfile_relative_path_under_user_data_dir()
        with open(parentfile_path, 'rb') as imay_parent_idx_ifile:
            imay_parent_idx = sf.read_imay_parent_idx(imay_parent_idx_ifile)
        check_uint_imay(imay_parent_idx)
        assert type(imay_parent_idx) is int
        assert imay_parent_idx >= -1
        return imay_parent_idx


    def patch_idx2user_data_dir_path(sf, patch_idx, /):
        'patch_idx -> real user_data_dir_path@fsys'
        dir_size = sf.get_dir_size()
        user_data_dir_relative_path = inf_dir_idx2user_data_relative_path(patch_idx, dir_size=dir_size)

        file_patch_forest_dir_path = sf.get_file_patch_forest_dir_path()

        user_data_dir_path = file_patch_forest_dir_path / user_data_dir_relative_path
        return user_data_dir_path

    def open_patch_idx_ex(sf, patch_idx, /,*, with_metadata:bool=True):
        'patch_idx -> (with_metadata=True) -> ((None|metadata), (pseudo_ifile::IPseudoFile4MkIsSameFile))'
        #.___open_patch_idx___ :: Iter (patch_idx, imay_parent_idx, user_data_dir_path, contentfile_path, content_binary_ifile) -> IPseudoFile4MkIsSameFile
        check_uint(patch_idx)

        if with_metadata:
            metadata = sf.patch_idx2metadata(patch_idx)
            may_metadata = metadata
        else:
            may_metadata = None
        may_metadata

        iter_tpl5s = sf._iter_tpl5s_for_open_patch_idx_ex(patch_idx)
        pseudo_ifile = type(sf).___open_patch_idx___(sf, iter_tpl5s)
        if not isinstance(pseudo_ifile, IPseudoFile4MkIsSameFile): raise TypeError

        return may_metadata, pseudo_ifile


    def _mk_tpl3_for_open_patch_idx_ex(sf, patch_idx, /):
        ' patch_idx -> (imay_parent_idx, user_data_dir_path, contentfile_path, content_binary_ifile) # see:_iter_tpl5s_for_open_patch_idx_ex/open_patch_idx_ex/___open_patch_idx___'
        imay_parent_idx = sf.patch_idx2imay_parent_idx(patch_idx)
        user_data_dir_path = sf.patch_idx2user_data_dir_path(patch_idx)
        contentfile_relative_path = sf.get_contentfile_relative_path_under_user_data_dir()
        contentfile_path = user_data_dir_path / contentfile_relative_path
        return (imay_parent_idx, user_data_dir_path, contentfile_path)
    def _iter_tpl5s_for_open_patch_idx_ex(sf, patch_idx, /):
        ' patch_idx -> Iter (patch_idx, imay_parent_idx, user_data_dir_path, contentfile_path, content_binary_ifile) # see:open_patch_idx_ex/___open_patch_idx___'
        while 1:
            check_uint(patch_idx)
            (imay_parent_idx, user_data_dir_path, contentfile_path) = sf._mk_tpl3_for_open_patch_idx_ex(patch_idx)
            with open(contentfile_path, 'rb') as content_binary_ifile:
                yield (patch_idx, imay_parent_idx, user_data_dir_path, contentfile_path, content_binary_ifile)

            if imay_parent_idx == -1:break
            patch_idx = imay_parent_idx









    def move_cmd_target__user_data_file__virtual_name2relative_path_under_user_data_dir(sf, user_data_file__virtual_name, /):
        if not user_data_file__virtual_name in sf.move_cmd_target__user_data_file__virtual_names: raise ValueError
        #attr = 'get_metadatafile_relative_path_under_user_data_dir'
        attr = f'get_{user_data_file__virtual_name!s}file_relative_path_under_user_data_dir'
        return getattr(sf, attr)()
    move_cmd_targets = ('push_into_command_history', 'push_into_branch_fsys_history', 'move_into_file_patch_forest')
    move_cmd_target__user_data_file__virtual_names = ('parent', 'content', 'metadata')
    def read_move_cmds(sf, TODO_list4move_cmd_binary_ifile, /):
        r'''binary_ifile -> [(idx4file_stack, move_cmd_target, move_cmd_target_args, idx4move_cmd_target)]

    ###
    move_cmd_target + args
        = 'push_into_command_history'
            ()
        | 'push_into_branch_fsys_history'
            (branch_name,)
        | 'move_into_file_patch_forest'
            (user_data_file__virtual_name,)
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
        #push_into_branch_fsys_history - push last/pop first
        #   to prevent writing branch_time is not latest by pop_from_inf_dir_and_push_into_another(..., imay_inf_dir_idx4assert4into=idx4move_cmd_target)

        * pop updating/file_stack[{i}] -> push_into grow_only/command_history[{j}]

        * pop updating/file_stack[{i}] -> push_into grow_only/branches/{branch_name}[{j}]

        * pop updating/file_stack[{i}] -> move_to parent @ grow_only/file_patch_forest[{j}]
        * pop updating/file_stack[{i}] -> move_to content @ grow_only/file_patch_forest[{j}]
        * pop updating/file_stack[{i}] -> move_to metadata @ grow_only/file_patch_forest[{j}]
        #'''
        move_cmds = type(sf).___read_move_cmds___(sf, TODO_list4move_cmd_binary_ifile)
        sf.check_move_cmds(move_cmds)
        return move_cmds
    def check_move_cmds(sf, move_cmds, /):
        check_tuple(move_cmds)
        for move_cmd in move_cmds:
            sf.check_move_cmd(move_cmd)
        idc4file_stack = tuple(map(fst, move_cmds))

        #reversed
        if not idc4file_stack == tuple(reversed(range(len(idc4file_stack)))): raise ValueError

        if not len(move_cmds) >= 2: raise ValueError
        if not move_cmds[0][0] == 'push_into_branch_fsys_history': raise ValueError
            # ensure branch_time is latest/correct
        if not move_cmds[1][0] == 'push_into_command_history': raise ValueError
        if not all(move_cmd[0] == 'move_into_file_patch_forest' for move_cmd in move_cmds[2:]): raise ValueError

    def check_move_cmd(sf, move_cmd, /):
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
            [branch_name] = move_cmd_target_args
            check_branch_name(branch_name)
        elif move_cmd_target == 'move_into_file_patch_forest':
            if not len(move_cmd_target_args) == 1: raise TypeError
            [user_data_file__virtual_name] = move_cmd_target_args
            sf.check_user_data_file__virtual_name(user_data_file__virtual_name)
        else:
            raise logic-err


    def check_user_data_file__virtual_name(sf, user_data_file__virtual_name, /):
        check_str(user_data_file__virtual_name)
        if not user_data_file__virtual_name in sf.move_cmd_target__user_data_file__virtual_names: raise ValueError

    def clean_updating_root_dir(sf, /):
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
            if not is_dir_empty(file_stack_dir_path): raise logic-err
            commit_completed_file_path.unlink() #remove file == os.remove
            TODO_list4move_cmd_file_path.unlink()#should exists
            file_stack_dir_path.rmdir()#should be empty
        else:
            assert not commit_completed_file_path.exists()
            TODO_list4move_cmd_file_path.unlink(missing_ok=True)#may not exists
            if file_stack_dir_path.exists():
                shutil.rmtree(file_stack_dir_path)#may not empty


    def __continue_flush_commit(sf, /):
        file_stack_dir_path = sf.get_file_stack_dir_path()
        TODO_list4move_cmd_file_path = sf.get_TODO_list4move_cmd_file_path()
        commit_completed_file_path = sf.get_commit_completed_file_path()
        if not commit_completed_file_path.exists(): raise FileNotFoundError

        if 1:
            dir_size = sf.get_dir_size()
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

        if not is_dir_empty(file_stack_dir_path): raise logic-err

    def exec_move_cmd(sf, move_cmd, /):
        sf.check_move_cmd(move_cmd)
        (idx4file_stack, move_cmd_target, move_cmd_target_args, idx4move_cmd_target) = move_cmd
        dir_size = sf.get_dir_size()
        file_stack_dir_path = sf.get_file_stack_dir_path()


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

    def write_move_cmds(sf, TODO_list4move_cmd_binary_ofile, move_cmds, /):
        'see:read_move_cmds'
        sf.check_move_cmds(move_cmds)
        type(sf).___write_move_cmds___(sf, TODO_list4move_cmd_binary_ofile, move_cmds)
        return

    def read_branch_history_deltas(sf, branch_history_deltas_binary_ifile, /):
        branch_history_deltas = type(sf).___read_branch_history_deltas___(sf, branch_history_deltas_binary_ifile)
        sf.check_branch_history_deltas(branch_history_deltas)
        return branch_history_deltas
    def write_branch_history_deltas(sf, branch_history_deltas_binary_ofile, branch_history_deltas, /):
        'see:read_branch_history_deltas'
        sf.check_branch_history_deltas(branch_history_deltas)
        type(sf).___write_branch_history_deltas___(sf, branch_history_deltas_binary_ofile, branch_history_deltas)
        return
    def check_branch_history_deltas(sf, branch_history_deltas, /):
        check_tuple(branch_history_deltas)
        check_all(sf.check_branch_history_delta, branch_history_deltas)
    def check_command_history_cmd(sf, command_history_cmd, /):
        'see: FileSystem4update~command_history_cmd = (branch_time, [high_level_user_command__str])'
        check_pair(command_history_cmd)
        branch_time, high_level_user_command__strs = command_history_cmd
        check_branch_time(branch_time)
        check_tuple(high_level_user_command__strs)
        check_all(check_str, high_level_user_command__strs)
    def read_command_history_cmd(sf, command_history_cmd_binary_ifile, /):
        r'''-> command_history_cmd
        #'''
        command_history_cmd = read_repred_py_obj(command_history_cmd_binary_ifile)
        sf.check_command_history_cmd(command_history_cmd)
        return command_history_cmd
    def write_command_history_cmd(sf, command_history_cmd_binary_ofile, command_history_cmd, /):
        r'''
        see:read_command_history_cmd
        #'''
        sf.check_command_history_cmd(command_history_cmd)
        write_py_obj_as_repr(command_history_cmd_binary_ofile, command_history_cmd)
        return









    def resolve_may_signed_branch_idx(sf, /, branch_name, may_signed_branch_idx):
        r'''
        :: may_signed_branch_idx -> branch_idx

        may_signed_branch_idx :: (None|int)
            None ==>> -1
            neg ==>> end-based branch_idx
        #'''
        check_nmay(check_int, may_signed_branch_idx)
        if may_signed_branch_idx is None:
            signed_branch_idx = -1
        else:
            signed_branch_idx = may_signed_branch_idx
        if signed_branch_idx < 0:
            # end-based
            inf_dir_end_based_idx = signed_branch_idx

            inf_dir_end_based_idx2begin_based_idx
            dir_size = sf.get_dir_size()
            inf_dir_path = sf.get_branch_history_dir_path(branch_name)
            branch_idx = inf_dir_end_based_idx2begin_based_idx(inf_dir_path, inf_dir_end_based_idx, dir_size=dir_size, min_len=0, imay_inf_dir_idx4assert=-1, negative_begin_based_idx_ok=False, positive_end_based_idx_ok=False)
        else:
            # begin-based
            inf_dir_begin_based_idx = signed_branch_idx
            branch_idx = inf_dir_begin_based_idx
        branch_idx
        return branch_idx

    def extract_may_root_fsys_frozendict_at_branch_time(sf, branch_name2min_extracting_branch_idx, branch_name, branch_idx, /):
        r'''
        branch_name2min_extracting_branch_idx -> branch_name -> branch_idx -> (None|root fsys_frozendict)'

        #####
        donot move to IFileSystem4update__fsys_delta
        #####
        should cache result when success
        #####

        required:
            get_cache__branch_time2root_fsys_frozendict
            ___extract_may_root_fsys_frozendict_at_branch_time___
        #'''
        check_str(branch_name)
        check_uint(branch_idx)
        branch_time = (branch_name, branch_idx)
        branch_time2root_fsys_frozendict = sf.get_cache__branch_time2root_fsys_frozendict()

        def this_func(depth, /):
            try:
                root_fsys_frozendict = branch_time2root_fsys_frozendict[branch_time]
            except KeyError:
                pass
            else:
                #return copy_fsys_dict(root_fsys_dict)
                return echo_valueonly_fsys_mapping(root_fsys_frozendict)
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

            f = type(sf).___extract_may_root_fsys_frozendict_at_branch_time___
            push()
            try:
                may_root_fsys_frozendict = f(sf, branch_name2min_extracting_branch_idx, branch_name, branch_idx)
            finally:
                pop()

            if may_root_fsys_frozendict is not None:
                root_fsys_frozendict = may_root_fsys_frozendict
                check_fsys_frozendict(root_fsys_frozendict)
                v = branch_time2root_fsys_frozendict.setdefault(branch_time, root_fsys_frozendict)
                if v is not root_fsys_frozendict: raise logic-err
                r = this_func(depth+1)
                if r is not root_fsys_frozendict: raise logic-err
                return r
            else:
                return None
            return may_root_fsys_frozendict
        #end:def this_func(depth, /):
        return this_func(0)

#end of class IRepositorySetting(IRepositorySetting__working_root_dir_path, IRepositorySetting__repository_root_dir_path, IRepositorySetting__user_data_dir_path):



class IRepositorySetting__branches_together(IRepositorySetting):
    @abstractmethod
    def get_branches_dir_relative_path(sf, /):
        '-> branches_dir_relative_path'
        return str2relative_path('grow_only/branches')
    @override
    def get_branch_history_dir_relative_path(sf, branch_name, /):
        'branch_name -> branch_history_dir_relative_path'
        return sf.get_branches_dir_relative_path() / branch_name

def check_path(path, /):
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
    def get_len_inf_dir_of_command_history(sf, /):
        '-> len(command_history)=len_inf_dir(command_history_dir_path)'
        sz = len_inf_dir(sf.get_command_history_dir_path(), dir_size=sf.get_dir_size(), min_len=sf.min_len_command_history_dir)
        sf.min_len_command_history_dir = sz
        return sz
    @override
    def get_len_inf_dir_of_file_patch_forest(sf, /):
        '-> len(file_patch_forest)=len_inf_dir(file_patch_forest_dir_path)'
        sz = len_inf_dir(sf.get_file_patch_forest_dir_path(), dir_size=sf.get_dir_size(), min_len=sf.min_len_file_patch_forest_dir)
        sf.min_len_file_patch_forest_dir = sz
        return sz
    @override
    def get_len_inf_dir_of_branch_history(sf, branch_name, /):
        'branch_name -> len(branch_name2branch_history[branch_name])=len_inf_dir(branch_history_dir_path)'
        sz = len_inf_dir(sf.get_branch_history_dir_path(branch_name), dir_size=sf.get_dir_size(), min_len=sf.branch_name2min_len_branch_history_dir.get(branch_name, 0))
        sf.branch_name2min_len_branch_history_dir[branch_name] = sz
        return sz

class IRepositorySetting__init_caches(IRepositorySetting):
    def __init__(sf, /):
        sf.branch_time2root_fsys_frozendict = {}
    @override
    def get_cache__branch_time2root_fsys_frozendict(sf, /):
        r'''-> branch_time2root_fsys_frozendict #{(branch_name, branch_idx):root_fsys_frozendict}
        to impl: extract_may_root_fsys_frozendict_at_branch_time
        #'''
        return sf.branch_time2root_fsys_frozendict
class IRepositorySetting__init_constants(IRepositorySetting):
    def __init__(sf, /,*, ignorefile_relative_path_encoding_pairs, parentfile_relative_path, contentfile_relative_path, metadatafile_relative_path, dir_size, lcp_threshold, repository_root_dir_path, repository_extra_cache_root_dir_path, command_history_dir_relative_path, file_patch_forest_dir_relative_path):
        sf.__dict__.update(locals())
        del sf.__dict__['sf']


        check_int(dir_size, min=2)
        check_uint(lcp_threshold)


        check_ignorefile_relative_path_encoding_pairs(ignorefile_relative_path_encoding_pairs)


        check_path(repository_root_dir_path)
        check_path(repository_extra_cache_root_dir_path)


        check_relative_path(parentfile_relative_path)
        check_relative_path(contentfile_relative_path)
        check_relative_path(metadatafile_relative_path)
        check_relative_path(command_history_dir_relative_path)
        check_relative_path(file_patch_forest_dir_relative_path)

    @override
    def get_ignorefile_relative_path_encoding_pairs_under_working_root_dir(sf, /):
        '-> [ignorefile_relative_path] # or(ignores)'
        return sf.ignorefile_relative_path_encoding_pairs

    @override
    def get_parentfile_relative_path_under_user_data_dir(sf, /):
        '-> parentfile_relative_path'
        return sf.parentfile_relative_path
    @override
    def get_contentfile_relative_path_under_user_data_dir(sf, /):
        '-> contentfile_relative_path'
        return sf.contentfile_relative_path
    @override
    def get_metadatafile_relative_path_under_user_data_dir(sf, /):
        '-> metadatafile_relative_path'
        return sf.metadatafile_relative_path
    @override
    def get_dir_size(sf, /):
        '-> dir_size'
        return sf.dir_size
    @override
    def get_lcp_threshold(sf, /):
        '-> lcp_threshold'
        return sf.lcp_threshold
    @override
    def get_repository_root_dir_path(sf, /):
        '-> repository_root_dir_path'
        return sf.repository_root_dir_path
    @override
    def get_repository_extra_cache_root_dir_path(sf, /):
        '-> repository_extra_cache_root_dir_path'
        return sf.repository_extra_cache_root_dir_path
    @override
    def get_command_history_dir_relative_path(sf, /):
        '-> command_history_dir_relative_path'
        return sf.command_history_dir_relative_path
    @override
    def get_file_patch_forest_dir_relative_path(sf, /):
        '-> file_patch_forest_dir_relative_path'
        return sf.file_patch_forest_dir_relative_path

class IRepositorySetting__init_constants__branches_together(IRepositorySetting__init_constants, IRepositorySetting__branches_together):
    def __init__(sf, /,*, branches_dir_relative_path, ignorefile_relative_path_encoding_pairs, parentfile_relative_path, contentfile_relative_path, metadatafile_relative_path, dir_size, lcp_threshold, repository_root_dir_path, repository_extra_cache_root_dir_path, command_history_dir_relative_path, file_patch_forest_dir_relative_path):
        check_relative_path(branches_dir_relative_path)
        sf.branches_dir_relative_path = branches_dir_relative_path
        d = dict(locals())
        del d['sf']
        del d['branches_dir_relative_path']

        super().__init__(**d)
    @override
    def get_branches_dir_relative_path(sf, /):
        '-> branches_dir_relative_path'
        return sf.branches_dir_relative_path
class IRepositorySetting__init_constants__branches_together__cache_min_len_inf_dir__init_caches(IRepositorySetting__init_caches, IRepositorySetting__init_constants__branches_together, IRepositorySetting__cache_min_len_inf_dir):
    def __init__(sf, /,*, min_len_command_history_dir, min_len_file_patch_forest_dir, branch_name2min_len_branch_history_dir, branches_dir_relative_path, ignorefile_relative_path_encoding_pairs, parentfile_relative_path, contentfile_relative_path, metadatafile_relative_path, dir_size, lcp_threshold, repository_root_dir_path, repository_extra_cache_root_dir_path, command_history_dir_relative_path, file_patch_forest_dir_relative_path):
        d = dict(locals())
        del d['sf']

        def f(min_len_command_history_dir, min_len_file_patch_forest_dir, branch_name2min_len_branch_history_dir, /, **kw):
            del kw
            IRepositorySetting__cache_min_len_inf_dir.__init__(sf, **locals())

        def g(branches_dir_relative_path, ignorefile_relative_path_encoding_pairs, parentfile_relative_path, contentfile_relative_path, metadatafile_relative_path, dir_size, lcp_threshold, repository_root_dir_path, repository_extra_cache_root_dir_path, command_history_dir_relative_path, file_patch_forest_dir_relative_path, /, **kw):
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
branch_name_regex = re.compile(branch_name_pattern)
def check_branch_name(branch_name, /):
    check_str(branch_name)
    if branch_name_regex.fullmatch(branch_name) is None:raise ValueError
    check_relative_path__str(branch_name, empty_ok=False)
def check_branch_time(branch_time, /):
    check_pair(branch_time)
    branch_name, branch_idx = branch_time
    check_branch_name(branch_name)
    check_uint(branch_idx)

class IRepositorySetting__default_move_cmd_line_fmt(IRepositorySetting):
    r'''
    read_move_cmds
    ___read_move_cmds___
    write_move_cmds
    ___write_move_cmds___

    default_move_cmd_line_fmt:
        move_cmd_line_fmt from IRepositorySetting.read_move_cmds.__doc__

        * pop updating/file_stack[{i}] -> push_into grow_only/command_history[{j}]

        * pop updating/file_stack[{i}] -> push_into grow_only/branches/{branch_name}[{j}]

        * pop updating/file_stack[{i}] -> move_to parent @ grow_only/file_patch_forest[{j}]
        * pop updating/file_stack[{i}] -> move_to content @ grow_only/file_patch_forest[{j}]
        * pop updating/file_stack[{i}] -> move_to metadata @ grow_only/file_patch_forest[{j}]
    #'''

    @override
    def ___read_move_cmds___(sf, TODO_list4move_cmd_binary_ifile, /):
        r'''binary_ifile -> [(idx4file_stack, move_cmd_target, move_cmd_target_args, idx4move_cmd_target)]
        see: read_move_cmds
        #'''
        return tuple(sf.__iter_read_move_cmds(TODO_list4move_cmd_binary_ifile))
    def __iter_read_move_cmds(sf, TODO_list4move_cmd_binary_ifile, /):
        binary_ifile = TODO_list4move_cmd_binary_ifile
        text_ifile = reopen_bin2txt(binary_ifile, encoding='utf8', buffered_case='read')
        for line in text_ifile:
            line = line.strip()
            if line[:1] in '#': continue
            move_cmd = sf._parse_default_move_cmd_line_fmt(line)
            yield move_cmd

    def _parse_default_move_cmd_line_fmt(sf, line, /):
        '-> move_cmd'
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
            check_branch_name(branch_name)

            move_cmd_target = 'push_into_branch_fsys_history'
            move_cmd_target_args = (branch_name,)
        else:
            raise logic-err
        move_cmd_target
        move_cmd_target_args

        move_cmd = (idx4file_stack, move_cmd_target, move_cmd_target_args, idx4move_cmd_target)
        sf.check_move_cmd(move_cmd)
        return move_cmd

    @override
    def ___write_move_cmds___(sf, TODO_list4move_cmd_binary_ofile, move_cmds, /):
        r'''
        see: write_move_cmds
        #'''
        binary_ofile = TODO_list4move_cmd_binary_ofile
        text_ofile = reopen_bin2txt(binary_ofile, encoding='utf8', buffered_case='write')
        for move_cmd in move_cmds:
            sf.__write_move_cmd(text_ofile, move_cmd)
    def __write_move_cmd(sf, text_ofile, move_cmd, /):
        s = sf._show_default_move_cmd_line_fmt(move_cmd)
        print(text_ofile, s)
    def _show_default_move_cmd_line_fmt(sf, move_cmd, /):
        'move_cmd -> str'
        (idx4file_stack, move_cmd_target, move_cmd_target_args, idx4move_cmd_target) = move_cmd
        i = idx4file_stack
        j = idx4move_cmd_target
        if move_cmd_target == 'move_into_file_patch_forest':
            (user_data_file__virtual_name,) = move_cmd_target_args
            s = f'pop updating/file_stack[{i}] -> move_to {user_data_file__virtual_name!s} @ grow_only/file_patch_forest[{j}]'
        elif move_cmd_target == 'push_into_branch_fsys_history':
            (branch_name,) = move_cmd_target_args
            s = f'pop updating/file_stack[{i}] -> push_into grow_only/branches/{branch_name}[{j}]'
        elif move_cmd_target == 'push_into_command_history':
            () = move_cmd_target_args
            s = f'pop updating/file_stack[{i}] -> push_into grow_only/command_history[{j}]'
        else:
            raise logic-err
        s

        _move_cmd = sf._parse_default_move_cmd_line_fmt(s)
        if move_cmd != _move_cmd: raise logic-err
        return s





