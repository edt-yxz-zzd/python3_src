
'''
why?
    hook1 never be called!
    even I delete sys.meta_path/sys.path_hooks!!!!

# these two line work!!!
sys.path_hooks[:]=[]
sys.path_importer_cache.clear()


conclusion:
    use meth_path instead of PathEntryFinder


'''


'''
find_spec(qname, maybe_parent_pkg_paths, may_reload_module):
    lpaths = maybe_parent_pkg_paths or sys.path
    hooks = sys.path_hooks

    # now #####################################
        # it seem this was correct
        # see: importlib._bootstrap_external.PathFinder._path_hooks
    for lpath in lpaths:
        for hook in hooks:
    # or  #####################################
    for hook in hooks:
        for lpath in lpaths:



'''
from importlib.abc import PathEntryFinder
from seed.tiny import expectError

class PathEntryFinderFail1(PathEntryFinder):
    def find_spec(self, qname, target=None):
        print('finder1', qname)
        return None
class PathEntryFinderFail2(PathEntryFinder):
    def find_spec(self, qname, target=None):
        print('finder2', qname)
        return None
class PathEntryFinderFail3(PathEntryFinder):
    def find_spec(self, qname, target=None):
        print('finder3', qname)
        return None
p1 = PathEntryFinderFail1()
p2 = PathEntryFinderFail2()
p3 = PathEntryFinderFail3()
def hook1(lpath):
    print('hook1', lpath)
    raise ImportError # pass control to hook2
    return p1
def hook2(lpath):
    print('hook2', lpath) # hiding hook3, even p2.find_spec return None
    return p2
def hook3(lpath):
    print('hook3', lpath)
    return p3


def donot_work():
    import sys
    #sys.path_hooks[:]=[]
    #sys.path_importer_cache.clear()
    print(len(sys.path_hooks))
    print(len(sys.path_importer_cache))
    sys.path_hooks.insert(0, hook1)
    sys.path_hooks.insert(0, hook2)
    #sys.path_hooks.append(hook1)
    #sys.path_hooks.append(hook2)
    try: import xxx
    except:
        print(len(sys.path_hooks))
        print(len(sys.path_importer_cache))
        raise
def work():
    import sys
    sys.path_hooks[:]=[]
    sys.path_importer_cache.clear()
    sys.path_hooks.append(hook1)
    sys.path_hooks.append(hook2)
    sys.path_hooks.append(hook3)
    import xxx
work() ; r'''
we can see the loop is
    for hook in path_hooks:
        try:
            return hook(lpath) # hook2 return; hide hook3
        except ImportError:
            continue # from hook1 to hook2
    else:
        return None

hook1 E:\my_data\program_source\python3_src\nn_ns\try_python\try_keywords\try_import
hook2 E:\my_data\program_source\python3_src\nn_ns\try_python\try_keywords\try_import
finder2 xxx
hook1 C:\Python36\python36.zip
hook2 C:\Python36\python36.zip
finder2 xxx
hook1 C:\Python36\DLLs
hook2 C:\Python36\DLLs
finder2 xxx
hook1 C:\Python36\lib
hook2 C:\Python36\lib
finder2 xxx
hook1 C:\Python36
hook2 C:\Python36
finder2 xxx
hook1 C:\Python36\lib\site-packages
hook2 C:\Python36\lib\site-packages
finder2 xxx
hook1 E:\my_data\program_source\python3_src
hook2 E:\my_data\program_source\python3_src
finder2 xxx
hook1 C:\Python36\lib\site-packages\win32
hook2 C:\Python36\lib\site-packages\win32
finder2 xxx
hook1 C:\Python36\lib\site-packages\win32\lib
hook2 C:\Python36\lib\site-packages\win32\lib
finder2 xxx
hook1 C:\Python36\lib\site-packages\Pythonwin
hook2 C:\Python36\lib\site-packages\Pythonwin
finder2 xxx
hook1 E:\my_data\program_source\python3_src\nn_ns\try_python\try_keywords
hook2 E:\my_data\program_source\python3_src\nn_ns\try_python\try_keywords
finder2 xxx
Traceback (most recent call last):
  File "C:\Python36\lib\runpy.py", line 193, in _run_module_as_main
'''

from importlib.machinery import PathFinder
PathFinder.invalidate_caches()
sys.meta_path[0:2] = []
import xxx













from sys import path_hooks, path_importer_cache, modules, meta_path
import sys
PathFinder.invalidate_caches()
path_hooks.clear()
print(path_hooks)
sys.path_hooks.insert(0, hook1) # insert useless??
print(sys.path_hooks)
print(__import__)
print(meta_path)
#meta_path.pop()
del meta_path[0:2]
print(meta_path)
del meta_path[:]
import aflafafsfs
#print(modules)
path_hooks.insert(0, hook1) # append useless??
path_hooks.insert(0, hook2) # append useless??
path_hooks.append(hook1) # append useless??
path_hooks.append(hook2) # append useless??
print(path_hooks)
print(meta_path)

try:
    import aflasfadljgaj
except ImportError as e:
    print(e)
    pass
else:
    raise logic-error

'''
print(path_importer_cache)
del path_importer_cache['aflasfadljgaj']
'''
del modules['aflasfadljgaj']
import aflasfadljgaj





