
__all__ = ['set_path_immutable', 'set_path_mutable']


import os # stat, chmod
from stat import S_IREAD, filemode, S_IWRITE, S_IWGRP, S_IWUSR, S_IWOTH
#print(*map(bin, [S_IWRITE, S_IWGRP, S_IWUSR, S_IWOTH]))
S_IW = S_IWRITE | S_IWGRP | S_IWUSR | S_IWOTH

def get_mode(path, *, dir_fd=None, follow_symlinks=True):
    return os.stat(path, dir_fd=dir_fd, follow_symlinks=follow_symlinks).st_mode

def change_os_stat_mode(modifier, path,
                        *, dir_fd=None, follow_symlinks=True):
    mode0 = get_mode(path, dir_fd=dir_fd, follow_symlinks=follow_symlinks)
    mode1 = modifier(mode0)
    if mode1 != mode0:
        os.chmod(path, mode1, dir_fd=dir_fd, follow_symlinks=follow_symlinks)

    return

def clear_os_stat_modeflag(modeflag, path,
                           *, dir_fd=None, follow_symlinks=True):
    modifier = lambda mode: mode & ~modeflag
    change_os_stat_mode(modifier, path, dir_fd=dir_fd, follow_symlinks=follow_symlinks)

def set_os_stat_modeflag(modeflag, path,
                           *, dir_fd=None, follow_symlinks=True):
    modifier = lambda mode: mode | modeflag
    change_os_stat_mode(modifier, path, dir_fd=dir_fd, follow_symlinks=follow_symlinks)


def set_path_immutable(path, *, dir_fd=None, follow_symlinks=True):
    # clear writable flag
    clear_os_stat_modeflag(S_IW, path, dir_fd=dir_fd, follow_symlinks=follow_symlinks)

def set_path_mutable(path, *, dir_fd=None, follow_symlinks=True):
    # set writable flag
    set_os_stat_modeflag(S_IWRITE, path, dir_fd=dir_fd, follow_symlinks=follow_symlinks)




