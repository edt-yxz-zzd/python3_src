r'''
usage:
    import xxx.yyy
    zzz = load_as_package('xxx.yyy.zzz', 'path/to/zzz__init__.py')
    XXX = load_as_module('xxx.yyy.XXX', 'path/to/XXX.py')
    YYY = load_as_module('xxx.yyy.zzz.YYY', 'path/to/YYY.py')

    import xxx.yyy.zzz as zzz_
    assert zzz_ is zzz
    import xxx.yyy.XXX as XXX_
    assert XXX_ is XXX
    import xxx.yyy.YYY as YYY_
    assert YYY_ is YYY

    ###or:
    import importlib
    importlib.import_module('xxx.yyy')
    load_as_module_or_package('xxx.yyy.zzz', 'path/to/zzz__init__.py', is_package=True)
    load_as_module_or_package('xxx.yyy.XXX', 'path/to/XXX.py', is_package=False)
    load_as_module_or_package('xxx.yyy.zzz.YYY', 'path/to/YYY.py', is_package=False)

'''
r'''
#################
py36 - 31.5.6.3. Importing a source file directly
https://stackoverflow.com/questions/19009932/import-arbitrary-python-source-file-python-3-3



#spec = spec_from_loader("xxx.XXX", SourceFileLoader("xxx.XXX", "/path/to/XXX.weird_extension"), is_package=???)

#################
importlib.machinery.SOURCE_SUFFIXES
    .append('') # allow any suffixes???
    .append('.exe_py') # my suffix
    see:
        "NOTE/Python/howto/python startup configuration.txt"
see:
    "NOTE/Python/howto/python source extension and load as module.txt"
    "NOTE/Python/howto/python source extension and load as module.py"
'''

__all__ = '''
    load_as_package
    load_as_module
    load_as_module_or_package
    load_as_module_or_package_ex
    '''.split()

from importlib.util import (spec_from_loader, spec_from_file_location, module_from_spec)
from importlib.machinery import SourceFileLoader
from importlib import import_module
import sys
from pathlib import Path


if False:
    assert Path('.').resolve() != Path('.')
    assert str(Path('.').resolve()) != str(Path('.'))
    assert Path('.').resolve().samefile(Path('.'))

def load_as_package(
    pkg_qname, pkg_source_path):
    #assert submodule_search_locations is not None
    return load_as_module_or_package(
            pkg_qname, pkg_source_path, is_package=True)

def load_as_module(module_qname, module_source_path):
    return load_as_module_or_package(
            module_qname, module_source_path, is_package=False)
def load_as_module_or_package(
    qname, source_path, *, is_package:bool):
    #assert maybe_submodule_search_locations is None or iter(maybe_submodule_search_locations)
    assert type(qname) is str
    if not (qname and qname[0] != '.'): raise ValueError

    if qname in sys.modules:
        try:
            return sys.modules[qname]
        except KeyError:
            pass


    def make_maybe_parent_bare(may_qname):
        if not may_qname: return None
        qname = may_qname
        maybe_parent_package_qname, may_sep, bare_name = qname.rpartition('.')
        # maybe_parent_package_qname may be ''
        if not maybe_parent_package_qname:
            maybe_parent_package_qname = None
        assert bare_name
        assert '.' not in bare_name
        return maybe_parent_package_qname, bare_name


    #is_package = maybe_submodule_search_locations is not None
    is_package = bool(is_package)
    maybe_submodule_search_locations = [] if is_package else None

    maybe_parent_package_qname, bare_name = make_maybe_parent_bare(qname)
    Nothing = object()
    if maybe_parent_package_qname:
        parent_package_qname = maybe_parent_package_qname
        if parent_package_qname not in sys.modules:
            # before exec_module to support relative import
            raise ImportError(f'import module_or_package={qname!r}, but parent_package={parent_package_qname!r} was not imported yet')

        parent_package = sys.modules[parent_package_qname]
        if getattr(parent_package, bare_name, Nothing) is not Nothing:
            raise ImportError(f'import module_or_package={qname!r}, but parent_package={parent_package_qname!r} has attribute {bare_name!r}')


    spec = spec_from_file_location(qname
                                , source_path
                                , submodule_search_locations
                                  = maybe_submodule_search_locations
                                )
    module = module_from_spec(spec)

    if is_package:
        submodule_search_locations = maybe_submodule_search_locations
        assert iter(submodule_search_locations)
        __package__ = qname
        __path__ = submodule_search_locations
    else:
        __package__ = maybe_parent_package_qname
        __path__ = None
    #rint(f'{module.__package__} == {__package__}')
    assert module.__package__ == __package__
    assert getattr(module, '__path__', None) is __path__
    if is_package:
        [parent_folder] = module.__path__
        assert Path(source_path).parent.samefile(Path(parent_folder))


    #sys.modules[qname] = module
    new_module = sys.modules.setdefault(qname, module)
        # before exec_module to support recursive import
        # before exec_module to support relative import if is_package
    if new_module is not module:
        return new_module
    try:
        if maybe_parent_package_qname:
            assert getattr(parent_package, bare_name, Nothing) is Nothing
            setattr(parent_package, bare_name, module)
        assert sys.modules[qname] is module
        assert not maybe_parent_package_qname or getattr(parent_package, bare_name, Nothing) is module

        try:
            spec.loader.exec_module(module)
        except:
            delattr(parent_package, bare_name)
            raise
    except:
        sys.modules.pop(qname)
        raise
    return module

def load_as_module_or_package_ex(
    may_qname_using_normal_import
    , bare_name_source_path_pairs
    , *, is_package:bool
    ):
    '''(None|str) -> [(bare_name, source_path)] -> (is_package:bool) -> (module_obj|package_obj)

may_qname_using_normal_import
    None | '' | 'xxx' | 'xxx.yyy' | ...
bare_name_source_path_pairs
    [('zzz', 'path/to/zzz.py')] | [('zzz', 'path/to/zzz.py'), ('aaa', 'path/to/aaa.py')] | ...

load_as_module_or_package_ex(
    'xxx.yyy'
    ,[('zzz', 'path/to/zzz.py'), ('aaa', 'path/to/aaa.py')]
    ,is_package=???
    )
    <==>
    importlib.import_module('xxx.yyy')
    load_as_package('xxx.yyy.zzz', 'path/to/zzz.py')
    load_as_module_or_package('xxx.yyy.zzz.aaa', 'path/to/aaa.py')

'''
    is_package = bool(is_package)
    may_qname = may_qname_using_normal_import
    assert may_qname is None or type(may_qname) is str

    if may_qname:
        qname = may_qname
        #module_obj = import_module(qname)
        import_module(qname)


    it = iter(bare_name_source_path_pairs)
    for bare_name, source_path in it:
        break
    else:
        raise Exception('no bare_names')
        if not may_qname:
            raise Exception('no qname and no bare_names')
        if is_package and getattr(module_obj, '__path__', None) is None:
            raise Exception(f'is_package=True, no bare_names, but the original qname is a module not package: {qname!r}')
        return module_obj

    for next_bare_name, next_source_path in it:
        assert bare_name.isidentifier()
        qname = f'{qname}.{bare_name}'
        load_as_package(qname, source_path)

        bare_name, source_path = next_bare_name, next_source_path

    assert bare_name.isidentifier()
    qname = f'{qname}.{bare_name}'
    return load_as_module_or_package(qname, source_path, is_package=is_package)



def _f():
    import seed
    pkg_source_path = Path(seed.__file__).parent / "abc/__init__.py"
    pkg_qname = 'seed.abc'
    module_source_path = Path(seed.__file__).parent / "abc/abc.py"
    module_qname = 'seed.abc.abc'

    try:
        seed.abc
    except:
        pass
    else:
        raise logic-error

    m = load_as_package(pkg_qname, pkg_source_path)
    print(m)
    print(m.__path__)

    seed.abc

    m = load_as_module(module_qname, module_source_path)
    print(m)
    print(getattr(m, '__path__', None))
    seed.abc.abc


if __name__ == '__main__':
    _f()
