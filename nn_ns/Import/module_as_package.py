
'''
usage:
    let a module be package
    for "xxx.py" (not "__init__.py"):
        # content of zzz/yyy/xxx.py
        import nn_ns.Import.module_as_package # import me
        __path__ = None
            # __path__ :: (None|[lpath])
            # since __path__ was used by xxx.py, set None is ok
        def ___meta_path_find_spec___(qname, may_parent_lpaths, may_target):
            # may_parent_lpaths is __path__ above
            assert qname.rpartition('.')[0] == __name__
            ...
            return None | module_spec
        # that's all

        # may try to import submodule:
        from zzz.yyy.xxx import aaa
'''









# output nothing
# using this module by:
#   import nn_ns.Import.module_as_package
#   __path__ = None
#   def ___meta_path_find_spec___(...):...
#
__all__ = '''
    '''.split()



'''
meta_path.append(this)
this(qname)
    may_pkg_qname = parent(qname)
    if not may_pkg_qname: return
    parent := modules[may_pkg_qname]
    if hasattr(type(parent), '___meta_path_find_spec___'):
        return type(parent).___meta_path_find_spec___(parent, qname)
    f = getattr(parent, '___meta_path_find_spec___', None)
    if callable(f):
        return f(qname, lpath, may_target)

'''

from importlib.abc import MetaPathFinder
import sys

class ModuleAsPackage(MetaPathFinder):
    def find_spec(self, qname, lpath, may_target=None):
        # qname = xxxx.yyyy
        # lpath :: str|bytes
        # lpath = E:/xxx/ssss
        # may_target :: None | module
        #   target - module to be reloaded
        # -> None | module_spec
        if not qname: return
        may_pkg_qname, sep, last = qname.rpartition('.')
        if not may_pkg_qname: return
        may_parent_pkg = sys.modules.get(may_pkg_qname)
        if may_parent_pkg is None: return
        parent = may_parent_pkg

        if False and forbid_parent_be_pkg:
            lpaths = getattr(parent, '__path__', None)
            if lpaths is not None:
                # parent is __init__.py which is a pkg
                return


        # if the above "if" is not comment out,
        #   then parent is module not package
        args = qname, lpath, may_target
        if hasattr(type(parent), '___meta_path_find_spec___'):
            type(parent).___meta_path_find_spec___(parent, *args)
        f = getattr(parent, '___meta_path_find_spec___', None)
        if callable(f):
            return f(qname, lpath, may_target)

# __path__ is (None|lpaths) to indicate __this__ is a package
# __path__ not exists, then is not a package
#__path__ = ['aasgd', 'age4']
__path__ = None
def ___meta_path_find_spec___(qname, may_parent_lpaths, may_target):
    print(qname, may_parent_lpaths, may_target, file=sys.stderr)
    assert qname.rpartition('.')[0] == __name__
    return None
this = ModuleAsPackage()
sys.meta_path.append(this)
#sys.meta_path.insert(0, this)




#__import__('.'.join([__name__, 'aaaa']))
#import nn_ns.Import.fw.aaaa
r'''#output:
nn_ns.Import.fw.aaaa None None
nn_ns.Import.fw.aaaa None None
Traceback (most recent call last):
  ...
  File "E:\my_data\program_source\python3_src\nn_ns\Import\fw.py", line 77
module>
    import nn_ns.Import.fw.aaaa
  File "E:\my_data\program_source\python3_src\nn_ns\Import\fw.py", line 77
module>
    import nn_ns.Import.fw.aaaa
ModuleNotFoundError: No module named 'nn_ns.Import.fw.aaaa'
'''










