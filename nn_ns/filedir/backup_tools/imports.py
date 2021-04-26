
#HHHHH

from nn_ns.filedir.dir_cmp import dir_cmp, dir_cmp__relative, path2str, path2str4dir_cmp_result, DirViewer__fsys, is_same_file__True, STR_TIME_FORMAT, mk_is_same_file, MkIsSameFile, AccessFile4MkIsSameFile__fsys, bytes2PseudoFile4MkIsSameFile, binary_ifile2PseudoFile4MkIsSameFile
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


