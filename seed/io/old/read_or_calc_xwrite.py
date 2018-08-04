

__all__ = ['read_or_calc_xwrite', 'write_value', 'read_value']

import zlib
import io
import os

def encode(string):
    data = string.encode(encoding='utf-8')
    zdata = zlib.compress(data)
    return zdata
    
def decode(zdata):
    data = zlib.decompress(zdata)
    return data.decode(encoding='utf-8')


def write(string, fname):
    zdata = encode(string)
    with open(fname, 'xb') as fout:
        fout.write(zdata)

def read(fname):
    with open(fname, 'rb') as fin:
        data = fin.read()

    return decode(data)

def write_value(value, fname):
    write(repr(value), fname)

def read_value(fname):
    return eval(read(fname))


def read_or_calc_xwrite(fname, calc_f, *,
                        rw_f = (read_value, write_value)):
    (read_value, write_value) = rw_f
    if os.path.exists(fname):
        return read_value(fname)
    value = calc_f()
    try:
        write_value(value, fname)
    except:
        os.remove(fname)
        raise
    return value



