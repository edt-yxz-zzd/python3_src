
__all__ = '''
    is_file_EOF__by_seek
    is_file_EOF__by_read_seek
    '''.split()

import os
def is_file_EOF__by_seek(file):
    begin_pos = file.tell()
    #file.seek(offset=0, whence=os.SEEK_END)
    file.seek(0, os.SEEK_END)
    end_pos = file.tell()
    file.seek(begin_pos)
    return begin_pos == end_pos

def is_file_EOF__by_read_seek(file):
    begin_pos = file.tell()
    s = file.read(1)
    file.seek(begin_pos)
    return not s


