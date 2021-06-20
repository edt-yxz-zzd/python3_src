
from pathlib import PurePosixPath
from abc import ABC, abstractmethod
from seed.abc.abc import override

#from seed.helper.check.checkers import check_uint_imay, check_uint, check_all, check_str, check_int, check_tuple, check_nmay, check_pair
from seed.helper.check.checkers import check_type_is, check_iterator

class IPseudoFileSystem(ABC):
    r'''
    path :: PurePosixPath

    exists
    is_dir/is_file
    dir_iter

    mk_dir #exist_ok?
    rm_dir #recursive?
    cp_dir_into #skip/overwrite/raise

    rm_file #unlink
    cp_file

    #filedir
    mv_into
    rename_lshift #left most replace?
    rename_lrotate
    mk_prefix4tmp_basename_of
    mk_suffix4tmp_basename_of #prefix suffix


    get_dir_num_children
    get_file_size
    get_file_mtime
    get_may_file_digest #hash_name
    truncate_file #size
    append_file #file/bytes
        ==>> overwrite_file #bytes

    get_curr_time #for mtime

    #IPseudoFileObj:
        tell4read
        tell4write
        seek4read
        seek4write
        seekable4read
        seekable4write

        seq_read > random_read
        seq_append > random_write
        truncate
        get_file_size
        ??get_file_mtime

        create_at_begnning
        clear_at_begnning
        seek_begin_at_begnning4read
        seek_begin_at_begnning4write
        seek_end_at_begnning4read
        seek_end_at_begnning4write

    open_binary_file4seq_read
    open_binary_file4random_read

    open_binary_file4seq_append
    open_binary_file4clear_then_seq_append

    open_binary_file4seq_append_seq_read
    open_binary_file4clear_then_seq_append_seq_read

    open_binary_file4seq_append_random_read
    open_binary_file4clear_then_seq_append_random_read

    private:
        #impl
        lock dir/file
FileExistsError
FileNotFoundError
IsADirectoryError
NotADirectoryError
PermissionError
    #'''
    @abstractmethod
    def ___exists___(sf, path):
        '-> bool'
    @abstractmethod
    def ___is_dir___(sf, path):
        '-> bool'
    @abstractmethod
    def ___dir_iter___(sf, dir_path):
        '-> Iter basename'

    def exists(sf, path):
        '-> bool'
        check_type_is(PurePosixPath, path)
        b = type(sf).___exists___(sf, path)
        check_type_is(bool, b)
        return b
    def is_dir(sf, path):
        '-> bool|raise FileNotFoundError'
        #check_type_is(PurePosixPath, path)
        if not sf.exists(path): raise FileNotFoundError
        b = type(sf).___is_dir___(sf, path)
        check_type_is(bool, b)
        return b
    def is_file(sf, path):
        '-> bool|raise FileNotFoundError'
        return not sf.is_dir(path)
    def dir_iter(sf, dir_path):
        '-> Iter basename|raise FileNotFoundError|NotADirectoryError'
        if not sf.is_dir(dir_path): raise NotADirectoryError
        it = type(sf).___dir_iter___(sf, dir_path)
        check_iterator(it)
        if it is not iter(it): raise TypeError
        for basename in it:
            check_type_is(str, basename)
            yield basename
        return
