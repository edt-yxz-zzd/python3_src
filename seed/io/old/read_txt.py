
from .read_or_calc_xwrite import read_or_calc_xwrite


''' bugs: \n -> \n\r!!!
def read_txt(fname, encoding, join_str='', *, errors=None):
    #ls = []
    with open(fname, encoding=encoding, errors=errors) as fin:
        if join_str:
            return join_str.join(fin)
        else:
            return fin.read() # will read all
def write_txt(fname, txt, encoding):
    with open(fname, 'x', encoding=encoding) as fout:
        fout.write(txt)
'''

def read_txt(fname, encoding):
    return read_bin(fname).decode(encoding)
def write_txt(fname, txt, encoding):
    return write_bin(fname, txt.encode(encoding))


def read_bin(fname):
    with open(fname, 'rb') as fin:
        return fin.read()



def write_bin(fname, data):
    with open(fname, 'xb') as fout:
        fout.write(data)


def read_or_calc_xwrite__txt(fname, txt_f, encoding):
    rw_f = (lambda fname: read_txt(fname, encoding),
            lambda txt, fname: write_txt(fname, txt, encoding))
    
    return read_or_calc_xwrite(fname, txt_f, rw_f=rw_f)

def read_or_calc_xwrite__bin(fname, bin_f):
    rw_f = (read_bin,
            lambda data, fname: write_bin(fname, data))
    
    return read_or_calc_xwrite(fname, bin_f, rw_f=rw_f)








