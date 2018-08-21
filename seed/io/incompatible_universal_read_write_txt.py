
'''
it is hard to make read_txt and write_txt be compatible when enable universal newline
    so I name it incompatible_universal_read_txt

see: compatible_read_write.py
see: incompatible_read_write.py
# this file: incompatible_universal_read_write_txt.py

'''
__all__ = '''
    incompatible_universal_read_txt
    incompatible_universal_write_txt
    incompatible_universal_write_txt__force
    '''.split()

from .incompatible_read_write import incompatible_read, incompatible_write

r'''
def incompatible_universal_read_txt(__path, *, encoding, errors=None):
    with open(__path, 'rt', newline=None
            , encoding=encoding, errors=errors) as fin:
        return fin
def incompatible_universal_write_txt(__path, *, text, encoding, force=False):
    mode = 'wt' if force else 'xt'
    with open(fname, mode, newline='\n'
            , encoding=encoding) as fout:
        fout.write(txt)
'''

def incompatible_universal_read_txt(__may_path, *, encoding, errors=None):
    return incompatible_read(__may_path
            , read=None, binary=False
            , newline=None, encoding=encoding, errors=errors)
def incompatible_universal_write_txt(__may_path, *, text, encoding, force=False):
    return incompatible_write(__may_path, text
            , write=None, binary=False, force=force, append=False
            , newline='\n', encoding=encoding)

def incompatible_universal_write_txt__force(__may_path, *, text, encoding):
    return incompatible_universal_write_txt(
            __may_path, text=text, encoding=encoding, force=True)

