
__all__ = '''
    get_pylike_encoding_from_path
    get_pylike_encoding
'''.split()

import tokenize
def get_pylike_encoding_from_path(path):
    with open(path, 'rb') as fin:
        return get_pylike_encoding(fin.readline)

def get_pylike_encoding(readline):
    '''parse python encoding declaration; return encoding

diff with tokenize.detect_encoding by:
    will ignore SyntaxError
encoding is utf-8 or using python encoding declarations
    # -*- coding: <encoding-name> -*-
    encoding has to be compatible with ascii

readline:
    i.e. 
    
    see __doc__ of tokenize.tokenize(readline):
    
    The tokenize() generator requires one argument, readline,
    which must be a callable object which provides the same interface
    as the io.IOBase.readline() method of file objects.
    Each call to the function should return one line of input as bytes.

example:
    with open(path, 'rb') as fin:
        encoding = get_pylike_encoding(fin.readline)
'''
    try:
        return tokenize.detect_encoding(readline)
    except:
        return 'utf-8'















