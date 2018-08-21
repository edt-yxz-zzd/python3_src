


'''
incompatible - means the read and write are incompatible
                for newline handle (universal newlines mode?)


'''

__all__ = '''
    incompatible_read
    incompatible_write

    free_read
    free_write
    '''.split()

from .may_open import may_open_stdin, may_open_stdout

def free_read(file):
    return file.read()
def free_write(file, data):
    file.write(data)





def incompatible_read(
        may_file, *, encoding
        , read=None, binary=False, **kwargs):
    # incompatible with write
    # read :: fin -> R
    # kwargs:
    #   see: open # but no "mode"
    mode = 'rb' if binary else 'rt'
    if read is None:
        read = free_read

    with may_open_stdin(may_file, mode, encoding=encoding, **kwargs) as fin:
        return read(fin)




def incompatible_write(
        may_file, data, *, encoding
        , write=None, binary=False, force=False, append=False
        , **kwargs):
    # incompatible with read
    # write :: fout -> data -> R
    # kwargs:
    #   see: open # but no "mode"
    mode1 = 'a' if append else ('w' if force else 'x')
    mode2 = 'b' if binary else 't'
    mode = mode1 + mode2
    if write is None:
        write = free_write

    with may_open_stdout(may_file, mode, encoding=encoding, **kwargs) as fout:
        return write(fout, data)





