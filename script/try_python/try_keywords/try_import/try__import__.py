########################
# it seems __this__.__import__ and builtins.__import__ both affect import

import importlib
import builtins, operator

class overwrite__import__:
    __builtins = builtins
    __builtins_import = importlib.__import__
    def __init__(self, new__import__, builtins=None, *, reversed_obj=None):
        if builtins is None:
            builtins = self.__builtins
        self.new__import__ = new__import__
        self.old__import__ = builtins.__import__
        self.builtins = builtins

        if reversed_obj is None:
            reversed_obj = __class__(self.old__import__, builtins)
            reversed_obj.old__import__ = self.new__import__
        if reversed_obj.old__import__ is not self.new__import__ or\
           reversed_obj.new__import__ is not self.old__import__:
            raise ValueError('not a reversed_obj')
        self.reversed_obj = reversed_obj
    def __enter__(self):
        self.builtins.__import__ = self.new__import__
        return self.new__import__
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.builtins.__import__ = self.old__import__
        return None
class wrap__import__(overwrite__import__):
    def __init__(self, builtins=None):
        new__import__ = self._import_
        self.__init__(new__import__, builtins)
    def _import_(self, name, globals=None, locals=None, fromlist=(), level=0):
        with overwrite__import__(self.old__import__) as old__import__:
            self._pre_import_(name, globals, locals, fromlist, level)
            module_or_pkg = old__import__(name, globals, locals, fromlist, level)
            module = module_or_pkg
            if not len(fromlist):
                pkg = module_or_pkg
                _, sep, attr = name.partition('.')
                module = operator.attrgetter(pkg, attr) if sep else pkg

                
            self._post_import_(module_or_pkg, module, name, globals, locals, fromlist, level)
            return module_or_pkg

    def _pre_import_(self, name, globals=None, locals=None, fromlist=(), level=0):
        pass
    def _post_import_(self, module_or_pkg, module, name, globals=None, locals=None, fromlist=(), level=0):
        pass






org_import = builtins.__import__
print(org_import)



  
import os.path
assert os is __import__('os.path') # not importlib.import_module()
assert os.path is importlib.import_module('os.path')
assert 'path' not in globals()

assert os.path is __import__('os.path', fromlist=['exists'])
assert 'path' not in globals()
assert 'exists' not in globals()
assert os.path is __import__('os.path', fromlist=['existssfafadfsafsdsfasf'])
# fromlist is useless!!!!!!!!!!!


def __import__(*args, **kwargs):
    # call me to find parent ??
    #print(args, kwargs)
    raise Exception('call __this__.__import__(*{}, **{})'.format(args, kwargs))
    pass # NOT BE USED
import os # not call __this__.__import__
print('import os')
import re
print('import re')
try:
    import os.path # call __this__.__import__ !!!!!!!!!!!!!!!!!!!!!!!!!!!
    # why !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    print('import os.path')
except Exception as e:
    # call __this__.__import__
    print('fail to import os.path: ', e)
    




try:
    import nn_ns.try_python.try_import.empty
except Exception as e:
    # call __this__.__import__
    print('fail to import nn_ns.try_python.try_import.empty: ', e)


def __import__(name, globals=None, locals=None, fromlist=(), level=0):
    print('__this__.__import__ :', name)
    return org_import(name, globals, locals, fromlist, level)

import os.path
import nn_ns.try_python.try_import.empty
'''
__this__.__import__ : os
__this__.__import__ : nn_ns.try_python.try_import
__this__.__import__ : nn_ns
'''



del __import__
print('\n', 'del __import__')

def _import_ver1_(name, globals=None, locals=None, fromlist=(), level=0):
    print('set builtins.__import__ = _import_ver1_ :', name)
    return org_import(name, globals, locals, fromlist, level)

def _import_ver2_(name, globals=None, locals=None, fromlist=(), level=0):
    with overwrite__import__(org_import) as new__import__:
        print('set builtins.__import__ = _import_ver2_ :', name)
        assert (new__import__ is builtins.__import__ is org_import)
        return new__import__(name, globals, locals, fromlist, level)

    
import sys
def del_xxx():
    print('\n'*3)
    del sys.modules['os.path']
    del sys.modules['os']
    del sys.modules['nn_ns.try_python.try_import.empty']
    del sys.modules['nn_ns.try_python.try_import']
    del sys.modules['nn_ns.try_python']
    del sys.modules['nn_ns']
    print('del os. ... to ... .path')
    print('del nn_ns. ... to ... .empty')

def using_import(_import_):
    with overwrite__import__(_import_):
        del_xxx()
        import os.path
        print('import os.path')
        import nn_ns.try_python.try_import.empty
        print('import nn_ns.try_python.try_import.empty')

        print('\n\n######################## import again ########################')
        import os.path
        print('import os.path')
        import nn_ns.try_python.try_import.empty
        print('import nn_ns.try_python.try_import.empty')

using_import(_import_ver1_)
using_import(_import_ver2_) 






