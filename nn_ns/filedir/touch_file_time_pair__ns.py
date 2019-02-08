
'''
like "touch", but raise if non_exist
    touch will create empty file if non_exist

see: pathlib.Path.touch()
see: os.utime()
https://stackoverflow.com/questions/1158076/implement-touch-using-python
https://stackoverflow.com/questions/6084985/how-to-set-a-files-ctime-with-python


os.utime(path, times=None, *, [ns, ]dir_fd=None, follow_symlinks=True)

statinfo = os.stat('somefile.txt')
statinfo == os.stat_result(st_mode=33188, st_ino=7876932, st_dev=234881026, st_nlink=1, st_uid=501, st_gid=501, st_size=264, st_atime=1297230295, st_mtime=1297230027, st_ctime=1297230027)
statinfo.st_atime_ns
statinfo.st_mtime_ns :: int # nanoseconds
statinfo.st_mtime    :: int # seconds
'''

__all__ = '''
    touch_file_time_pair__ns
    get_file_time_pair__ns
    touch_as
    '''.split()

import os # utime, stat
import os.path


def get_file_time_pair__ns(path):
    'path -> (st_atime_ns, st_mtime_ns)'
    statinfo = os.stat(path)
    return statinfo.st_atime_ns, statinfo.st_mtime_ns

def touch_file_time_pair__ns(path, *
    , access_time_ns, modified_time_ns
    , dir_fd=None, follow_symlinks=True
    ):
    '''

access_time_ns, modified_time_ns :: int # nanoseconds

creation_time can not be changed
ctime(change_time)(time of last status change) can be changed
    but not here

use pathlib.Path.touch() to set to current time
use get_file_time_pair__ns() to get file time pair to be used as default values
'''
    #os.utime(path, times=None, *, [ns, ]dir_fd=None, follow_symlinks=True)
    if not os.path.isfile(path): raise IsADirectoryError(path)

    time_pair__ns = access_time_ns, modified_time_ns
    os.utime(path, ns = time_pair__ns, dir_fd=dir_fd, follow_symlinks=follow_symlinks)




def touch_as(to_path, from_path):
    "touch to_path's (atime, mtime) as from_path"
    if os.path.samefile(to_path, from_path):
        return

    atime, mtime = get_file_time_pair__ns(from_path)

    touch_file_time_pair__ns(to_path
        , access_time_ns=atime, modified_time_ns=mtime)


