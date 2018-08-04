
from os import stat, chmod
from stat import S_IREAD, filemode, S_IWRITE, S_IWGRP, S_IWUSR, S_IWOTH

print(*map(bin, [S_IWRITE, S_IWGRP, S_IWUSR, S_IWOTH]))
S_IW = S_IWRITE | S_IWGRP | S_IWUSR | S_IWOTH


fname = './test_data/try_os_stat_READONLY.txt'

def get_mode(fname):
    return stat(fname).st_mode
def show_mode(fname):
    mode = get_mode(fname)
    print(mode, filemode(mode))

chmod(fname, get_mode(fname) | S_IW)
show_mode(fname)
chmod(fname, get_mode(fname) & ~S_IW)
show_mode(fname)

from sand import set_path_immutable, set_path_mutable
set_path_mutable(fname)
show_mode(fname)
set_path_immutable(fname)
show_mode(fname)

'''
0b10000000 0b10000 0b10000000 0b10
33206 -rw-rw-rw-
33060 -r--r--r--
33206 -rw-rw-rw-
33060 -r--r--r--
'''

