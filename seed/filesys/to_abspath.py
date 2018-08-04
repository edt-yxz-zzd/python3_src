
__all__ = '''
    to_abspath
    to_dirname where
    to_basename
'''.split()

from os.path import abspath as _abspath, join as _join, \
     dirname as _dirname, basename as _basename

'''
os.path.abspath(path)
== normpath(join(os.getcwd(), path))

'''

def to_abspath(*paths):
    return _abspath(_join(*paths))

def to_dirname(*paths):
    return _dirname(to_abspath(*paths))

def to_basename(*paths):
    return _basename(to_abspath(*paths))

where = to_dirname









