
r'''
find c:/windows -path *zm*
'''

import os, re
from sand import read_or_calc_xwrite__txt, exactly_matched
#def read_or_calc_xwrite__txt(fname, txt_f, encoding):
    
def iter_all_file_basenames(path):
    for root, dirs, files in os.walk(path):
        yield from files


def all_file_basenames(path, fmt=None):
    it = iter_all_file_basenames(path)
    it2 = it if fmt is None else map(fmt, it)
    return set(it2)


txt_f = lambda: all_file_basenames('c:/windows', lambda name: name.lower())

#txt_f = lambda: repr(s)
fname = './c_windows_files.u8'
files = eval(read_or_calc_xwrite__txt(fname, txt_f, encoding='u8'))
assert len(files) == 44382

def find_re(rex, iterable):
    rex = re.compile(rex)
    for s in iterable:
        if exactly_matched(rex, s):
            yield s

s = set(find_re('.*zm.*', files))






