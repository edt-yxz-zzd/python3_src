
######## all results are qual_name
__all__ = '''
    guess_package_name
    module2guess_package_name
    module_name2guess_package_name

    script_fname2module_name
    folder2package_name
    path2package_or_module_name
    '''.split()



from .is_valid_python_id import is_valid_python_id
import os.path
import inspect

def top_package_path(fname):
    '''
path, basenames = top_package_path(__file__)
    assert path is driver or not exist(path/__init__.py)
    assert not basenames or exists(join(path, *basenames[:i])/__init__.py) for i > 0
    assert exists(subpath/__init__.py) for subpath between path and __file__

'''
    fname = os.path.abspath(fname)
    dirname = os.path.dirname(fname)
    return top_package_path_from_folder(dirname)
def top_package_path_from_folder(folder):
    assert os.path.isdir(folder)
    dirname = folder
    init_basename = '__init__.py'
    to_init_fname = lambda path: os.path.join(path, init_basename)

    path = dirname
    basenames = []
    while os.path.exists(to_init_fname(path)):
        next_path, basename = os.path.split(path)
        #_path = os.path.abspath(join(path, '..'))
        if next_path == path:
            # path is driver
            if not path == os.path.abspath(join(path, '..')):
                raise logic-error
            break
        assert basename
        basenames.append(basename)
        path = next_path

    basenames.reverse()
    assert os.path.join(path, *basenames) == dirname
    #print(basenames, fname, dirname)
    return path, basenames


def guess_package_name(fname):
    'may return ""'
    fname = os.path.abspath(fname)
    dirname = os.path.dirname(fname)
    return guess_package_name_from_folder(dirname)
def guess_package_name_from_folder(folder):
    'may return ""'
    assert os.path.isdir(folder)
    path, basenames = top_package_path_from_folder(folder)
    idc = [i for i, basename in enumerate(basenames)
           if not is_valid_python_id(basename)]
    if idc:
        basenames = basenames[max(idc)+1:]
    return '.'.join(basenames) # can be ''
    if not basenames:
        return ''

def module_name2guess_package_name(module_name):
    module = import_module(module_name)
    return module2guess_package_name(module)
def module2guess_package_name(module):
    '''not use __package__ if not __package__
return _pkg_; if not _pkg_, means fail to find one
'''
    _pkg_ = getattr(module, '__package__', '')
    if not _pkg_:
        if hasattr(module, '__file__'):
            _pkg_ = guess_package_name(module.__file__) # maybe '' here
    return _pkg_

def script_fname2module_name(script_fname):
    fname = os.path.abspath(script_fname)
    if os.path.isdir(fname):
        fname = os.path.join(fname, '__main__.py')
    pkg = guess_package_name(fname)
    base = inspect.getmodulename(fname)
    if base is None:
        return None
        raise ValueError('not a legal module_name')
    module_name = '.'.join([pkg, base]) if pkg else base
    return module_name

def folder2package_name(folder):
    'may return ""'
    assert os.path.isdir(folder)
    pkg = guess_package_name_from_folder(folder)
    return pkg

def path2package_or_module_name(path):
    assert os.path.exists(path)
    if os.path.isdir(path):
        return folder2package_name(path)
    return script_fname2module_name(path)




