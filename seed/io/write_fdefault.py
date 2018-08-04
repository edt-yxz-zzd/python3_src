

'''
write_fdefault
    if file exist:
        return file.read()
    else:
        data = fdefault()
        write(data)
        data2 = file.read()
        assert data == data2
        return data2

'''

__all__ = '''
    read
    read_or_xwrite
    xwrite
    overwrite

    write_fdefault
    bin_write_fdefault
    '''.split()

import operator

def bin_write_fdefault(fdefault, path, *, **kwargs):
    # kwargs:
    #   see: write_fdefault # but without "encoding/binary"
    return write_fdefault(fdefault, path
            , encoding=None, binary=True, **kwargs)


def xwrite(fdefault, path, **kwargs):
    # kwargs:
    #   see: write_fdefault # but without "writeonly/overwrite"
    assert fdefault is not None
    return write_fdefault(fdefault, path
            , writeonly=True, overwrite=False, **kwargs)
def overwrite(fdefault, path, **kwargs):
    # kwargs:
    #   see: write_fdefault # but without "writeonly/overwrite"
    assert fdefault is not None
    return write_fdefault(fdefault, path
            , writeonly=True, overwrite=True, **kwargs)
def read_or_xwrite(fdefault, path, **kwargs):
    # kwargs:
    #   see: write_fdefault # but without "writeonly/overwrite"
    return write_fdefault(fdefault, path
            , writeonly=False, overwrite=False, **kwargs)
def read(path, **kwargs):
    # kwargs:
    #   see: write_fdefault # but without "writeonly/overwrite"
    return write_fdefault(None, path
            , writeonly=False, overwrite=False, **kwargs)



def write_fdefault(fdefault, path
        , *, encoding, binary=False, eq=None
        , writeonly=False, overwrite=False
        , **kwargs):
    # write_fdefault - the name comes from dict.setdefault
    #
    # fdefault:
    #   if fdefault is None then readonly
    #   elif FileNotFoundError: then write fdefault() to file
    # if overwrite:
    #   then writeonly
    # eq:
    #   verify read/write are compatible
    # kwargs:
    #   see: open # but no "mode"
    #
    # readonly; xwriteonly; overwriteonly; read_xwrite
    #   readonly:       fdefault is None # assert writeonly==False
    #   read_xwrite:    fdefault is not None and writeonly==False
    #   xwriteonly:     fdefault is not None and writeonly==True and overwrite==False
    #   overwriteonly:  fdefault is not None and writeonly==True and overwrite=True
    mode = 'b' if binary else 'r'
    if eq is None:
        eq = operator.eq

    readonly = fdefault is None:
    writeonly = bool(writeonly)
    overwrite = bool(overwrite)
    if readonly and writeonly: raise ValueError

    def write(data, x_or_w):
        assert x_or_w in ['x', 'w']
        with open(path, x_or_w+mode, encoding=encoding, **kwargs) as fout:
            return fout.write(data)
    def read():
        with open(path, 'r'+mode, encoding=encoding, **kwargs) as fin:
            return fin.read()

    def write_read_verify(x_or_w):
        ####### calc
        ####### xwrite
        ####### verify
        data = fdefault()
        write(data, x_or_w)
        data2 = read()
        if not eq(data, data2):
            raise AssertionError('kwargs make read/write incompatible!')
        return data2
    return write_read()

    if readonly:
        return read()
    if writeonly:
        if overwrite:
            return write_read_verify('w')
        else:
            return write_read_verify('x')

    try:
        ####### read
        return read()
    except FileNotFoundError:
        return write_read_verify('x')

