#__all__:goto
r'''[[[
e ../../python3_src/seed/pkg_tools/load_resource.py
see:
    view ../../python3_src/seed/io/may_open.py
        from seed.io.may_open import open4w, open4w_err, open4r

    view ../../python3_src/seed/io/make_mode_ex4open.py
        from seed.io.make_mode_ex4open import is_binary_mode5xencoding, xencoding2may_encoding, mk_mode_ex4open4w, mk_mode_ex4open4r



seed.pkg_tools.load_resource
py -m nn_ns.app.debug_cmd   seed.pkg_tools.load_resource
py -m nn_ns.app.adhoc_argparser__main__call8module   seed.pkg_tools.load_resource   @f
py -m nn_ns.app.doctest_cmd seed.pkg_tools.load_resource:__doc__ -v

from seed.pkg_tools.load_resource import open_under_pkg_, read_under_pkg_

from seed.pkg_tools.load_resource import list_potential_basenames_under_pkg_, sorted_potential_basenames_under_pkg_, iter_potential_basenames_under_pkg_, does_exist_under_pkg_, with_path_under_pkg_


>>> read_under_pkg_('seed.pkg_tools', 'load_resource.py', xencoding='')[:7]
b'#__all_'
>>> read_under_pkg_('seed.pkg_tools', 'load_resource.py', xencoding=None)[:7]
b'#__all_'
>>> read_under_pkg_('seed.pkg_tools', 'load_resource.py', xencoding='u8')[:7]
'#__all_'


>>> _list_potential_basenames('seed.pkg_tools')
['__init__.py', '_forgot_import.py', 'app.guess_package_name.txt', 'detect_all_unbound_names.py', 'get_python_object.py', 'import_object.py', 'iter_submodules.py', 'load_as_module.py', 'module_qname2source_file_path.py', 'read_python_source.py', 'see pkgutil.txt', '__pycache__', 'module2export_names.py', 'load_resource.py', 'xmodule2module_qname.py', 'load_resources.py']
>>> list_potential_basenames_under_pkg_('seed.pkg_tools') == _list_potential_basenames('seed.pkg_tools')
True
>>> sorted_potential_basenames_under_pkg_('seed.pkg_tools') == sorted(list_potential_basenames_under_pkg_('seed.pkg_tools'))
True
>>> sorted(iter_potential_basenames_under_pkg_('seed.pkg_tools')) == sorted_potential_basenames_under_pkg_('seed.pkg_tools')
True

>>> does_exist_under_pkg_('seed.pkg_tools', 'load_resource.py')
True

>>> with with_path_under_pkg_('seed.pkg_tools', 'load_resource.py') as tmp_path, open(tmp_path, 'rt', encoding='u8') as fin:
...     fin.read(7)
'#__all_'
>>> with open_under_pkg_('seed.pkg_tools', 'load_resource.py', xencoding='u8') as fin:
...     fin.read(7)
'#__all_'







[[
view ../../python3_src/py_stdlib_api.txt


[importlib__resources]#goto
  虚拟路径、基本文件名
  枚举子文件子文件夹、过滤掉子文件夹、临时文件
importlib.resources.open_binary(package, resource)->BinaryIO
importlib.resources.open_text(package, resource, encoding='utf-8', errors='strict')->TextIO
importlib.resources.read_binary(package, resource)->bytes
importlib.resources.read_text(package, resource, encoding='utf-8', errors='strict')->str
  虚拟路径、基本文件名
  package = pkg_qname|pkg_obj
  resource :: basename
      it may not contain path separators
      it may not have sub-resources (i.e. it cannot be a directory).

importlib.resources.path(package, resource)->context_manager<tmp_path>
importlib.resources.is_resource(package, name)->bool
importlib.resources.contents(package)->Iter<name/resource-or-not>#目录
  枚举子文件子文件夹、过滤掉子文件夹、临时文件

[[[
importlib.resources – Resources¶

#>>> import importlib.resources
#>>> help(importlib.resources)
#>>> import pkg_resources
#>>> help(pkg_resources)
  不是标准库: /data/data/com.termux/files/usr/lib/python3.10/site-packages/pkg_resources/__init__.py



This module leverages Python’s import system to provide access to resources within packages.  If you can import a package, you can access resources within that package.  Resources can be opened or read, in either binary or text mode.
Resources are roughly akin to files inside directories, though it’s important to keep in mind that this is just a metaphor.
    Resources and packages do not have to exist as physical files and directories on the file system.

Note
This module provides functionality similar to pkg_resources Basic Resource Access without the performance overhead of that package.
This makes reading resources included in packages easier, with more stable and consistent semantics.
The standalone backport of this module provides more information on using importlib.resources and migrating from pkg_resources to importlib.resources.

Loaders that wish to support resource reading should implement a get_resource_reader(fullname) method as specified by importlib.abc.ResourceReader.




The following types are defined.
*importlib.resources.Package¶
  The Package type is defined as Union[str, ModuleType].
    This means that where the function describes accepting a Package, you can pass in either a string or a module.
      Module objects must have a resolvable __spec__.submodule_search_locations that is not None.



*importlib.resources.Resource¶
  This type describes the resource names passed into the various functions in this package.
      This is defined as Union[str, os.PathLike].
      #basename?



[importlib__resources]#here
The following functions are available.

importlib.resources.open_binary(package, resource)->BinaryIO
importlib.resources.open_text(package, resource, encoding='utf-8', errors='strict')->TextIO
importlib.resources.read_binary(package, resource)->bytes
importlib.resources.read_text(package, resource, encoding='utf-8', errors='strict')->str
  虚拟路径、基本文件名
  package = pkg_qname|pkg_obj
  resource :: basename
      it may not contain path separators
      it may not have sub-resources (i.e. it cannot be a directory).












importlib.resources.path(package, resource)->context_manager<tmp_path>
  Return the path to the resource as an actual file system path.
  This function returns a context manager for use in a with statement.
  The context manager provides a pathlib.Path object.
  Exiting the context manager cleans up any temporary file created when the resource needs to be extracted from e.g. a zip file.



importlib.resources.is_resource(package, name)->bool
  Return True if there is a resource named name in the package, otherwise False.
  Remember that directories are not resources!



importlib.resources.contents(package)->Iter<name/resource-or-not>#目录
  Return an iterable over the named items within the package.
  The iterable returns str resources (e.g. files) and non-resources (e.g. directories).
  The iterable does not recurse into subdirectories.
  枚举子文件子文件夹、过滤掉子文件夹、临时文件
]]]

]]

potential 潜在的

#]]]'''
__all__ = r'''
    open_under_pkg_
    read_under_pkg_

    list_potential_basenames_under_pkg_
    sorted_potential_basenames_under_pkg_
    iter_potential_basenames_under_pkg_
    does_exist_under_pkg_
    with_path_under_pkg_
'''.split()#'''
__all__

from importlib.resources import open_binary, open_text, read_binary, read_text
from importlib.resources import path as _with_path, is_resource as _does_exist, contents as _list_potential_basenames
from seed.io.make_mode_ex4open import xencoding2may_encoding

#def open_under_pkg_(pkg, basename, /, *, encoding, **kwds):
def open_under_pkg_(pkg, basename, /, *, xencoding, **kwds):
    'binary-mode <==> [not xencoding]'
    may_encoding = xencoding2may_encoding(xencoding)
    is_b = may_encoding is None
    #if encoding:
    if not is_b:
        return open_text(pkg, basename, encoding=xencoding, **kwds)
    return open_binary(pkg, basename, **kwds)
#def read_under_pkg_(pkg, basename, /, *, encoding, **kwds):
def read_under_pkg_(pkg, basename, /, *, xencoding, **kwds):
    'binary-mode <==> [not xencoding]'
    may_encoding = xencoding2may_encoding(xencoding)
    is_b = may_encoding is None
    #if encoding:
    if not is_b:
        return read_text(pkg, basename, encoding=xencoding, **kwds)
    return read_binary(pkg, basename, **kwds)
def sorted_potential_basenames_under_pkg_(pkg, /):
    'contents(...)->[basename]'
    ls = _list_potential_basenames(pkg)
    return sorted(ls)
def list_potential_basenames_under_pkg_(pkg, /):
    'contents(...)->[basename]'
    ls = _list_potential_basenames(pkg)
    if not type(ls) is list:
        ls = [*ls]
    assert type(ls) is list
    return ls
def iter_potential_basenames_under_pkg_(pkg, /):
    'contents(...)->Iter<basename>'
    return iter(_list_potential_basenames(pkg))
def does_exist_under_pkg_(pkg, basename, /):
    'is_resource(...)->bool'
    return _does_exist(pkg, basename)
def with_path_under_pkg_(pkg, basename, /):
    'path(...)->context_manager<tmp_path'
    return _with_path(pkg, basename)



from seed.pkg_tools.load_resource import open_under_pkg_, read_under_pkg_

from seed.pkg_tools.load_resource import list_potential_basenames_under_pkg_, sorted_potential_basenames_under_pkg_, iter_potential_basenames_under_pkg_, does_exist_under_pkg_, with_path_under_pkg_
