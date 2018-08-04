
'''
to list all descendants of a package

will actually import package/module
if unwanted, see pkgutil.walk_packages
'''

__all__ = '''
    iter_submodules
    iter_submodules_ex

    '''.split()
from pkgutil import walk_packages
from importlib import import_module
from seed.tiny import snd

def iter_child_modules(package_obj):
    # :: package_obj -> Iter module_obj
    return map(snd, iter_child_modules_ex(package_obj))
def iter_child_modules_ex(package_obj):
    # :: package_obj -> Iter (ispkg, module_obj)
    lpath = package_obj.__path__
    pkg_qname = package_obj.__name__
    #print(f'pkg_qname={pkg_qname!r}')
    for child_module_info in walk_packages(lpath):
        if not child_module_info.name.isidentifier(): continue
        #input(f'{pkg_qname}.{child_module_info.name}')
        ##### it found non-identifier name
        #####   and import it successful!!!!!!
        ##### I assume them to be scripts, and donot import them
        m = module_from_ModuleInfo(pkg_qname, child_module_info)
        yield child_module_info.ispkg, m
    pass

def iter_submodules(package_or_qname, exclude_top_package=False, *, recursive):
    ''':: package -> Iter submodule_or_subpackage_obj

input:
    package_obj
        a module object or package_name will raise
    exclude_top_package :: bool
        used only if recursive = True
        if True: output will include the top package
    recursive :: bool
        recursive or not
'''
    it = iter_submodules_ex(package_or_qname, exclude_top_package, recursive=recursive)
    return map(snd, it)

def iter_submodules_ex(package_or_qname, exclude_top_package=False, *, recursive):
    ''':: package -> Iter (ispkg, submodule_or_subpackage_obj)

input:
    package_obj
        a module object or package_name will raise
    exclude_top_package :: bool
        used only if recursive = True
        if True: output will include the top package
    recursive :: bool
        recursive or not
'''
    if type(package_or_qname) is str:
        pkg_qname = package_or_qname
        pkg_obj = import_module(pkg_qname)
    else:
        pkg_obj = package_or_qname
    lpath = pkg_obj.__path__ # hasattr __path__??
    iter(lpath) # test whether iterable??

    if not recursive:
        yield from iter_child_modules_ex(pkg_obj)
        return

    if not exclude_top_package:
        yield (True, pkg_obj)

    to_process = [pkg_obj] # push after yield
    while to_process:
        pkg_obj = to_process.pop()
        for ispkg, m in iter_child_modules_ex(pkg_obj):
            yield ispkg, m
            if ispkg:
                to_process.append(m)
    return



def module_from_ModuleInfo(pkg_qname, module_info):
    assert pkg_qname # using relative import
    name = module_info.name
    #bug: m = import_module(name, pkg_qname) # abs import
    m = import_module('.'+name, pkg_qname) # relative import
    return m

#################### try walk_packages
def try_walk_packages():
    # module obj will fail
    try:
        walk_packages(__import__(__name__).__path__)
        raise logic-error
    except AttributeError:
        #AttributeError: module '__main__' has no attribute '__path__'
        pass
    pkg_obj = __import__('seed', fromlist=[__name__])
    print(pkg_obj)
    #<module 'seed.test_utils' (namespace)>

    it = walk_packages(pkg_obj.__path__)
    print(it)
    #<generator object walk_packages at 0x0000000002CAD678>

    for m in it:
        print(m)
    '''
    ModuleInfo(module_finder=FileFinder('E:\\my_data\\program_source\\python3_src\\seed\\test_utils'), name='generate_test_data', ispkg=False)
    ModuleInfo(module_finder=FileFinder('E:\\my_data\\program_source\\python3_src\\seed\\test_utils'), name='iter_submodules', ispkg=False)
    '''

def try_iter_submodules_ex():
    pkg_obj = __import__('seed.test_utils', fromlist=[__name__])
    it = iter_submodules_ex(pkg_obj, recursive=False)
    print(it)
    print(list(it))
    it = iter_submodules_ex(pkg_obj, recursive=True)
    print(it)
    print(list(it))

    #<generator object iter_submodules_ex at 0x0000000002A63200>
    #[(True, <module 'seed.test_utils' (namespace)>), (False, <module 'generate_test_data' from 'E:\\my_data\\program_source\\python3_src\\seed\\test_utils\\generate_test_data.py'>), (False, <module 'list_submodules' from 'E:\\my_data\\program_source\\python3_src\\seed\\test_utils\\list_submodules.py'>)]


if __name__ == '__main__':
    try_walk_packages()
    try_iter_submodules_ex()


