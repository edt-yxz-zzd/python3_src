#__all__:goto
r'''[[[
e ../../python3_src/seed/for_libs/for_importlib.py

cp -iv -r /data/data/com.termux/files/usr/lib/python3.11/importlib/ /sdcard/0my_files/tmp/py_lib_src/
[naming@importlib is confusing...]


seed.for_libs.for_importlib
py -m nn_ns.app.debug_cmd   seed.for_libs.for_importlib -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.for_libs.for_importlib:__doc__ -ht # -ff -df




view /sdcard/0my_files/unzip/py_doc/python-3.12.4-docs-text/library/importlib.txt
    /sdcard/0my_files/unzip/py_doc/python-3.12.4-docs-html/library/importlib.html
    http://127.0.0.1:3124/index.html
    <<==:
[[
view others/app/termux/web_server.txt
# [:using____httpd_conf__py_doc_html]:here
httpd -f /sdcard/0my_files/git_repos/txt_phone/lots/NOTE/html/httpd-confs/httpd.conf-sdcard_0my_files-unzip-py_doc-python_3_12_4_docs_html
lynx http://127.0.0.1:3124/index.html
  py3.12.4
lynx http://127.0.0.1:3081/index.html
  py3.8.1
httpd -k stop -f /sdcard/0my_files/git_repos/txt_phone/lots/NOTE/html/httpd-confs/httpd.conf-sdcard_0my_files-unzip-py_doc-python_3_12_4_docs_html
]]
[[
cp -iv -r /data/data/com.termux/files/usr/lib/python3.11/importlib/ /sdcard/0my_files/tmp/py_lib_src/
view /sdcard/0my_files/tmp/py_lib_src/importlib/_abc.py
    Loader-->ILoader
]]
[[
http://127.0.0.1:3124/library/importlib.html
importlib.abc
ABC hierarchy:

object
 +-- MetaPathFinder
 +-- PathEntryFinder
 +-- Loader
      +-- ResourceLoader --------+
      +-- InspectLoader          |
           +-- ExecutionLoader --+
                                 +-- FileLoader
                                 +-- SourceLoader


===
2 places to inject:
    sys.meta_path
    sys.path_hooks
2 places to set path:
    pkg_obj.__path__
    sys.path
4 kind mdl:
    * file-module:
        * source-module
            .py+?pyc?   # SourceFileLoader
        * bytecode-module
            .pyc        # SourcelessFileLoader
        * builtin_module
            .so         # ExtensionFileLoader
    * package:
        * namespace-package
            # NamespaceLoader
        * directory-package
            __doc__
                :: may str
            __file__
                .../__init__.py
            __cached__
                .../__pycache__/__init__.???.pyc
                    # .../__pycache__/__init__.cpython-311.pyc')
            __loader__
                .__spec__.__loader__
                SourceFileLoader
            __name__
                :: qnm
            __package__
                .__name__
            __path__
                :: [path]
            __spec__
                :: ModuleSpec
            ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__']
#ModuleSpec(name, loader, *, origin=None, loader_state=None, is_package=None){has_location/_set_fileattr::bool}
===

===
FileLoader(fullname, path):
    SourceFileLoader(fullname, path)
          path to the extension module.
    SourcelessFileLoader(fullname, path)
          path to the bytecode file.
    ?ExtensionFileLoader(fullname, path)
          path to the extension module.
    # ??? see:IFileLoader.get_data()=> [ExtensionFileLoader <: IFileLoader] ???


===
ResourceLoader vs InspectLoader
    * many rsc under pkg
    * py/pyc of mdl

===
FileLoader vs SourceLoader
    * (.qnm4mdl, .path4mdl)
        #readonly
        * .py
        * .pyc
        * .so
    * py/pyc of mdl
        .py #readonly
            get_source()
        (optional) .pyc#cache-readwrite
            get_data()
            set_data()
            path_stats()
===
ILoader
    .get_resource_reader
    .create_module
    .exec_module

    IInspectLoader
        .get_code
        .get_source
        .is_package
        .source_to_code

        IExecutionLoader
            .get_filename

            IFileLoader
            ISourceLoader
    IResourceLoader
        .get_data
            IFileLoader
                .name
                .path
            ISourceLoader
                .set_data
                .path_stats
                .path_mtime

===

]]







py_adhoc_call   seed.for_libs.for_importlib   @f
from seed.for_libs.for_importlib import *
#]]]'''
__all__ = r'''
IMetaPathFinder
IPathEntryFinder
ILoader
    IResourceLoader
IResourceReader
    ITraversableResources
ITraversable



ILoader
    IInspectLoader
        IExecutionLoader
            IFileLoader
            ISourceLoader
    IResourceLoader
            IFileLoader
            ISourceLoader

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#from seed.tiny_.check import check_type_le, check_type_is, check_int_ge
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from importlib.abc import (
MetaPathFinder, PathEntryFinder, Loader
, ResourceLoader
    # [ResourceLoader is deprecated by ResourceReader/TraversableResources]
, InspectLoader, ExecutionLoader
, FileLoader, SourceLoader
)
from importlib.resources.abc import (
ResourceReader
    # [ResourceReader is deprecated by TraversableResources]
, Traversable
    # [Traversable <: pathlib.Path]
, TraversableResources
    # [TraversableResources <: ResourceReader]
    # [TraversableResources has_a Traversable]
)

from io import open_code, FileIO, BufferedReader, TextIOWrapper
from typing import BinaryIO
    # TextIOWrapper@ITraversable.open()
    # BufferedReader@ITraversableResources.open_resource()
    # BinaryIO@IResourceReader.open_resource()
    # open_code/FileIO@FileLoader.get_data()
#open_code(path)
#    Opens the provided file with the intent to import the contents.
#    This may perform extra validation beyond open(), but is otherwise interchangeable with calling open(path, 'rb').

from typing import NoReturn, Iterator, Iterable, Optional, Any, Text
from typing import Union
from os import PathLike
StrPath = Union[str, PathLike[str]]

from importlib.machinery import (
#_register:goto
BuiltinImporter, FrozenImporter, PathFinder, WindowsRegistryFinder
    # [... <: MetaPathFinder]
, FileFinder
    # [... <: PathEntryFinder]
, BuiltinImporter, FrozenImporter, NamespaceLoader
    # [... <: InspectLoader]
, ExtensionFileLoader
    # [... <: ExecutionLoader]
    # ??? see:IFileLoader.get_data()=> [ExtensionFileLoader <: IFileLoader] ???
, SourcelessFileLoader
    # [... <: FileLoader]
, SourceFileLoader
    # [... <: (FileLoader&SourceLoader)]
)
___end_mark_of_excluded_global_names__0___ = ...

class IMetaPathFinder(MetaPathFinder, ABC):
    r"""Abstract base class for import finders on sys.meta_path.

sys.meta_path
    :: [IMetaPathFinder]
    #
    # [isinstance(PathFinder, IMetaPathFinder)]
    #   treat the type-PathFinder as an instance of IMetaPathFinder
    #   !! ducktype
    #
[PathFinder <- IMetaPathFinder]
[PathFinder <: IMetaPathFinder]
    !! all classmethod

>>> import sys
>>> sys.meta_path[-1]
<class '_frozen_importlib_external.PathFinder'>
>>> sys.meta_path
[<class '_frozen_importlib.BuiltinImporter'>, <class '_frozen_importlib.FrozenImporter'>, <class '_frozen_importlib_external.PathFinder'>]

>>> import importlib.machinery
>>> sys.meta_path[-1] is importlib.machinery.PathFinder
True

    """#"""
    __slots__ = ()

    @abstractmethod
    def invalidate_caches(self, /):
        r"""
        :: -> None

        An optional method which, when called, should invalidate any internal cache used by the finder.
        Used by importlib.invalidate_caches() when invalidating the caches of all finders on sys.meta_path.
        """#"""
        return None

    @abstractmethod
    def find_spec(self, fullname, may_paths6parent, target=None, /):
        r"""
        :: qnm4mdl -> may [path6parenth]/parent.__path__ -> may mdl_obj -> may spec | ^ImportError

        An abstract method for finding a spec for the specified module.
        If this is a top-level import, may_paths6parent will be None. Otherwise, this is a search for a subpackage or module and may_paths6parent will be the value of __path__ from the parent package.
        If a spec cannot be found, None is returned. When passed in, target is a module object that the finder may use to make a more educated guess about what spec to return.
        importlib.util.spec_from_loader() may be useful for implementing concrete MetaPathFinders.
        """#"""

class IPathEntryFinder(PathEntryFinder, ABC):
    r"""An abstract base class representing a *path entry finder*.
    Though it bears some similarities to "MetaPathFinder", "PathEntryFinder" is meant for use only within the path-based import subsystem
   provided by "importlib.machinery.PathFinder".

pkg_obj.__path__
    :: [path]
sys.path
    :: [path]
sys.path_hooks
    :: [path_hook]
    [path_hook :: (path -> may? IPathEntryFinder|^ImportError)]
sys.path_importer_cache
    :: {path:may IPathEntryFinder}

[FileFinder <: IPathEntryFinder]

>>> import sys
>>> sys.path            #doctest: +SKIP
[''
, '/sdcard/0my_files/git_repos/python3_src'
, '/sdcard/0my_files/unzip/python3_src-master'
, '/storage/emulated/0/0my_files/git_repos/txt_phone/txt'
, '/data/data/com.termux/files/usr/lib/python311.zip'
, '/data/data/com.termux/files/usr/lib/python3.11'
, '/data/data/com.termux/files/usr/lib/python3.11/lib-dynload'
, '/data/data/com.termux/files/usr/lib/python3.11/site-packages'
]
>>> sys.path_hooks      #doctest: +SKIP
[<class 'zipimport.zipimporter'>, <function FileFinder.path_hook.<locals>.path_hook_for_FileFinder at 0x77ca2e42c0>]
>>> sys.path_importer_cache #doctest: +SKIP
{'/sdcard/0my_files/git_repos/python3_src'
: FileFinder('/sdcard/0my_files/git_repos/python3_src')
, '/sdcard/0my_files/unzip/python3_src-master'
: None
, '/storage/emulated/0/0my_files/git_repos/txt_phone/txt'
: FileFinder('/storage/emulated/0/0my_files/git_repos/txt_phone/txt')
, '/data/data/com.termux/files/usr/lib/python311.zip'
: None
, '/data/data/com.termux/files/usr/lib/python3.11'
: FileFinder('/data/data/com.termux/files/usr/lib/python3.11')
, '/data/data/com.termux/files/usr/lib/python3.11/encodings'
: FileFinder('/data/data/com.termux/files/usr/lib/python3.11/encodings')
, '/data/data/com.termux/files/usr/lib/python3.11/lib-dynload'
: FileFinder('/data/data/com.termux/files/usr/lib/python3.11/lib-dynload')
, '/data/data/com.termux/files/usr/lib/python3.11/site-packages'
: FileFinder('/data/data/com.termux/files/usr/lib/python3.11/site-packages')
, '/data/data/com.termux/files/usr/lib/python3.11/collections'
: FileFinder('/data/data/com.termux/files/usr/lib/python3.11/collections')
, '/data/data/com.termux/files/usr/lib/python3.11/re'
: FileFinder('/data/data/com.termux/files/usr/lib/python3.11/re')
}

>>> import importlib.abc
>>> import importlib.machinery
>>> importlib.machinery.FileFinder
<class '_frozen_importlib_external.FileFinder'>
>>> importlib.machinery.FileFinder.__mro__
(<class '_frozen_importlib_external.FileFinder'>, <class 'object'>)
>>> issubclass(importlib.machinery.FileFinder, importlib.abc.PathEntryFinder)
True

    """#"""
    __slots__ = ()
    @abstractmethod
    def invalidate_caches(self, /):
        r"""
        :: -> None

        An optional method which, when called, should invalidate any internal cache used by the finder.
        Used by "importlib.machinery.PathFinder.invalidate_caches()" when invalidating the caches of all cached finders.
        """#"""
        return None

    @abstractmethod
    def find_spec(self, fullname, target=None, /):
        r"""
        :: qnm4mdl -> may mdl_obj -> may spec | ^ImportError

        An abstract method for finding a *spec* for the specified module.
        The finder will search for the module only within the *path entry* to which it is assigned.
        If a spec cannot be found, "None" is returned.
        When passed in, "target" is a module object that the finder may use to make a more educated guess about what spec to return.
        "importlib.util.spec_from_loader()" may be useful for implementing concrete "PathEntryFinder"s.
        """#"""






class ILoader(Loader, ABC):
    r"""Abstract base class for import loaders.
    An abstract base class for a *loader*. See **PEP 302** for the exact definition for a loader.

    Loaders that wish to support resource reading should implement a "get_resource_reader()" method as specified by "importlib.resources.abc.ResourceReader".

    Changed in version 3.7: Introduced the optional "get_resource_reader()" method.
        but [#ResourceReader is deprecated by TraversableResources#]


flow<reload>:
    ######################
    #_init_module_attrs >>> ?exec_module
    ######################
    module
    _init_module_attrs(spec, module, override=True)
        # .__name__, ..., .__spec__
    if spec.loader is None and spec.submodule_search_locations is not None:
        #namespace package
        pass
    else:
        spec.loader.exec_module(module)
    ######################
flow<import>:
    ######################
    #create_module/_new_module >>> _init_module_attrs >>> ?exec_module
    ######################
    spec
    module = spec.loader.create_module(spec)
    if module is None:
        #module = _new_module(spec.name)
        module = types.ModuleType(spec.name)
    _init_module_attrs(spec, module, override=False)
        # .__name__, ..., .__spec__
    if spec.loader is None and spec.submodule_search_locations is not None:
        #namespace package
        pass
    else:
        spec.loader.exec_module(module)
    ######################
NOTE:lock@thread

    """#"""
    __slots__ = ()
    @abstractmethod
    #@optional
    def get_resource_reader(self, fullname, /):
        'qnm4mdl -> may (ITraversableResources|IResourceReader){fullname not package => None}[#ResourceReader is deprecated by TraversableResources#]'
        raise NotImplementedError('@optional')
        return None

    @abstractmethod
    def create_module(self, spec, /):
        r"""
        :: spec -> may empty-mdl_obj[#neednot set attrs4mdl#] | ^ImportError

        Return a module to initialize and into which to load.

        This method should raise ImportError if anything prevents it from creating a new module.
        It may return None to indicate that the spec should create the new module.
        """#"""
        # By default, defer to default semantics for the new module.
        return None
        raise ImportError

    @abstractmethod
    def exec_module(self, module, /):
        r"""
        :: initialized-mdl_obj{mdl.attributes be set}[#eg:reload()#] -> None
        precondition:
            [attrs4mdl have been set]
            mdl_obj:
                .__name__
                    :: str/qnm4mdl
                    spec.name
                ?.__file__ if not built-in module
                    :: may (path4py|path4pyc)
                        == may path4mdl\-\path4so
                        [path4py over path4pyc]
                    .py|.pyc
                    ?? :: may path4py
                    ?? :: may path4py
                    ?? .py
                        # but: [(SourceLoader|?ExtensionFileLoader?|SourcelessFileLoader) <: IFileLoader]
                        #   get_filename
                    ?? :: may path4mdl
                    ?? .py|?.so?(builtin unset)|?.pyc?(@.__cached__)
                     None if namespace package
                     spec.origin if spec.has_location or namespace package
                     [namespace package <==> [not spec.has_location][spec.submodule_search_locations is not None]]
                     [namespace package -> [spec.origin is None]]
                ?.__cached__ if not built-in module
                    :: may path4pyc
                    .pyc
                    spec.cached if spec.cached is not None
                ?.__path__ if package
                    :: [path6parent]
                    spec.submodule_search_locations if spec.submodule_search_locations is not None
                .__package__
                    :: smay qnm
                    spec.parent
                    * package -> __name__
                    * top-level module -> ''
                    * nontop-level module -> parent.__name__
                .__loader__
                    :: may ILoader
                    * NamespaceLoader if spec.loader is None and spec.submodule_search_locations is not None #=>namespace package
                    * None if spec.loader is None and spec.submodule_search_locations is None
                    * spec.loader otherwise
                .__spec__
                    :: IModuleSpec

        An abstract method that executes the module in its own namespace when a module is imported or reloaded.
        The module should already be initialized when "exec_module()" is called.
        When this method exists, "create_module()" must be defined.

        """#"""

    r"""
   load_module(fullname)

      A legacy method for loading a module.  If the module cannot be
      loaded, "ImportError" is raised, otherwise the loaded module is
      returned.

      If the requested module already exists in "sys.modules", that
      module should be used and reloaded. Otherwise the loader should
      create a new module and insert it into "sys.modules" before any
      loading begins, to prevent recursion from the import.  If the
      loader inserted a module and the load fails, it must be removed
      by the loader from "sys.modules"; modules already in
      "sys.modules" before the loader began execution should be left
      alone.

      The loader should set several attributes on the module (note
      that some of these attributes can change when a module is
      reloaded):

      * "__name__"
           The module's fully qualified name. It is "'__main__'" for
           an executed module.

      * "__file__"
           The location the *loader* used to load the module. For
           example, for modules loaded from a .py file this is the
           filename. It is not set on all modules (e.g. built-in
           modules).

      * "__cached__"
           The filename of a compiled version of the module's code. It
           is not set on all modules (e.g. built-in modules).

      * "__path__"
           The list of locations where the package's submodules will
           be found. Most of the time this is a single directory. The
           import system passes this attribute to "__import__()" and
           to finders in the same way as "sys.path" but just for the
           package. It is not set on non-package modules so it can be
           used as an indicator that the module is a package.

      * "__package__"
           The fully qualified name of the package the module is in
           (or the empty string for a top-level module). If the module
           is a package then this is the same as "__name__".

      * "__loader__"
           The *loader* used to load the module.

      When "exec_module()" is available then backwards-compatible
      functionality is provided.

      Changed in version 3.4: Raise "ImportError" when called instead
      of "NotImplementedError".  Functionality provided when
      "exec_module()" is available.

      Deprecated since version 3.4: The recommended API for loading a
      module is "exec_module()" (and "create_module()").  Loaders
      should implement it instead of "load_module()".  The import
      machinery takes care of all the other responsibilities of
      "load_module()" when "exec_module()" is implemented.


    """#"""



######################
######################
######################
######################

class IResourceLoader(ResourceLoader, ILoader):
    r"""
    ResourceLoader is deprecated by importlib.resources.abc.ResourceReader
        but [#ResourceReader is deprecated by TraversableResources#]

    Abstract base class for loaders which can return data from their
    back-end storage.

    This ABC represents one of the optional protocols specified by PEP 302.
    """#"""
    __slots__ = ()

    @abstractmethod
    def get_data(self, path4rsc, /):
        r"""
        :: path4rsc/str -> data/bytes | ^OSError
        #xxx :: path4pyc/?mdl.__cached__?/str -> data/bytes | ^OSError

        Abstract method which when implemented should return the bytes for the specified path.
        The path must be a str.

        An abstract method to return the bytes for the data located at *path*.
        Loaders that have a file-like storage back-end that allows storing arbitrary data can implement this abstract method to give direct access to the data stored.
        "OSError" is to be raised if the *path* cannot be found.
        The *path* is expected to be constructed using a module's "__file__" attribute or an item from a package's "__path__".
        """#"""
        raise OSError


#grep get_resource_reader -r /sdcard/0my_files/tmp/py_lib_src/importlib/
class IResourceReader(ResourceReader, ABC):
    r"""
    #ResourceReader is deprecated by TraversableResources

    Abstract base class for loaders to provide resource reading support.


    *Superseded by TraversableResources*

    An *abstract base class* to provide the ability to read *resources*.

    From the perspective of this ABC, a *resource* is a binary artifact that is shipped within a package.
    Typically this is something like a data file that lives next to the "__init__.py" file of the package.
    The purpose of this class is to help abstract out the accessing of such data files so that it does not matter if the package and its data file(s) are stored in a e.g. zip file versus on the file system.

    For any of methods of this class, a *resource* argument is expected to be a *path-like object* which represents conceptually just a file name.
    This means that no subdirectory paths should be included in the *resource* argument. This is because the location of the package the reader is for, acts as the "directory".
    Hence the metaphor for directories and file names is packages and resources, respectively.
    This is also why instances of this class are expected to directly correlate to a specific package (instead of potentially representing multiple packages or a module).

    Loaders that wish to support resource reading are expected to provide a method called "get_resource_reader(fullname)" which returns an object implementing this ABC's interface.
    If the module specified by fullname is not a package, this method should return "None". An object compatible with this ABC should only be returned when the specified module is a package.

    Added in version 3.7.

    Deprecated since version 3.12, will be removed in version 3.14: Use "importlib.resources.abc.TraversableResources" instead.

    """#"""
    __slots__ = ()

    @abstractmethod
    def open_resource(self, resource: Text) -> BinaryIO:
        r"""
        basename4rsc/str -> BinaryIO | ^FileNotFoundError


        Return an opened, file-like object for binary reading.

        The 'resource' argument is expected to represent only a file name.
        If the resource cannot be found, FileNotFoundError is raised.
        """#"""
        # This deliberately raises FileNotFoundError instead of
        # NotImplementedError so that if this method is accidentally called,
        # it'll still do the right thing.
        raise FileNotFoundError

    @abstractmethod
    def resource_path(self, resource: Text) -> Text:
        r"""
        basename4rsc/str -> path4rsc/str | ^FileNotFoundError

        Return the file system path to the specified resource.

        The 'resource' argument is expected to represent only a file name.
        If the resource does not exist on the file system, raise
        FileNotFoundError.
        """#"""
        # This deliberately raises FileNotFoundError instead of
        # NotImplementedError so that if this method is accidentally called,
        # it'll still do the right thing.
        raise FileNotFoundError

    @abstractmethod
    def is_resource(self, basename4item: Text) -> bool:
        r"""
        basename4item/str -> bool/{basename4item is basename4rsc} # [basename4rsc is not directory]

        Return True if the named 'basename4item' is a resource.

        Files are resources, directories are not.
        """#"""
        raise FileNotFoundError

    @abstractmethod
    def contents(self) -> Iterable[str]:
        r"""
        :: -> Iter basename4item/str

        Return an iterable of entries in `package`.

        Returns an *iterable* of strings over the contents of the package.
        Do note that it is not required that all names returned by the iterator be actual resources, e.g. it is acceptable to return names for which "is_resource()" would be false.

        Allowing non-resource names to be returned is to allow for situations where how a package and its resources are stored are known a priori and the non-resource names would be useful.
        For instance, returning subdirectory names is allowed so that when it is known that the package and resources are stored on the file system then those subdirectory names can be used directly.

        The abstract method returns an iterable of no items.


        """#"""
        return;yield#mine
        raise FileNotFoundError#???py3_11_9



#@runtime_checkable
#class Traversable(Protocol):
#class ITraversable(Traversable, ABC):
#   TypeError: metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases
#
class ITraversable(ABC):
    r"""
    [Traversable <: pathlib.Path]

    An object with a subset of pathlib.Path methods suitable for traversing directories and opening files.

    Any exceptions that occur when accessing the backing resource may propagate unaltered.
    """#"""
    __slots__ = ()

    @abstractmethod
    def iterdir(self) -> Iterator["ITraversable"]:
        r"""
        :: -> Iter ITraversable

        Yield Traversable objects in self
        """#"""

    def read_bytes(self) -> bytes:
        r"""
        :: -> bytes

        Read contents of self as bytes
        """#"""
        with self.open('rb') as strm:
            return strm.read()

    def read_text(self, encoding: Optional[str] = None) -> str:
        r"""
        :: -> str

        Read contents of self as text
        """#"""
        with self.open(encoding=encoding) as strm:
            return strm.read()

    @abstractmethod
    def is_dir(self) -> bool:
        r"""
        :: -> bool

        Return True if self is a directory
        """#"""

    @abstractmethod
    def is_file(self) -> bool:
        r"""
        :: -> bool

        Return True if self is a file
        """#"""

    @abstractmethod
    def joinpath(self, *descendants: StrPath) -> "ITraversable":
        r"""
        :: (*[path_segment/str]) -> ITraversable

        Return Traversable resolved with any descendants applied.

        Each descendant should be a path segment relative to self
        and each may contain multiple levels separated by
        ``posixpath.sep`` (``/``).
        """#"""

    def __truediv__(self, child: StrPath) -> "ITraversable":
        r"""
        :: path_segment/str -> ITraversable

        Return Traversable child in self
        """#"""
        return self.joinpath(child)

    @abstractmethod
    def open(self, mode='r', *args, **kwargs) -> TextIOWrapper:
        r"""
        mode may be 'r' or 'rb' to open as text or binary. Return a handle
        suitable for reading (same as pathlib.Path.open).

        When opening as text, accepts encoding parameters such as those
        accepted by io.TextIOWrapper.
        """#"""

    @property
    @abstractmethod
    def name(self) -> str:
        r"""
        :: -> basename4item

        The base name of this object without any parent references.
        """#"""
#assert issubclass(ITraversable, Traversable)
    # TypeError: Protocols with non-method members don't support issubclass()
    # !! [Traversable@runtime_checkable <: Protocol]

class ITraversableResources(TraversableResources, ITraversable, IResourceReader, ABC):
    r"""
    [TraversableResources <: ResourceReader]
    [TraversableResources has_a Traversable]

    The required interface for providing traversable resources.
    """#"""
    __slots__ = ()

    @abstractmethod
    def files(self) -> "ITraversable":
        r"""
        :: -> ITraversable

        Return a Traversable object for the loaded package."""
        """#"""

    @override
    def open_resource(self, resource: StrPath) -> BufferedReader:
        return self.files().joinpath(resource).open('rb')

    @abstractmethod
    @override
    def resource_path(self, resource: Any) -> NoReturn:
        raise FileNotFoundError(resource)

    @override
    def is_resource(self, path4item: StrPath) -> bool:
        return self.files().joinpath(path4item).is_file()

    @override
    def contents(self) -> Iterator[str]:
        return (item.name for item in self.files().iterdir())


















































######################
######################
######################
######################

class IInspectLoader(InspectLoader, ILoader):
    r"""
    Abstract base class for loaders which support inspection about the
    modules they can load.

    This ABC represents one of the optional protocols specified by PEP 302.


    """#"""
    __slots__ = ()
    @abstractmethod
    def get_code(self, fullname):
        r"""
        :: qnm4mdl -> may CodeType | ^ImportError

        Method which returns the code object for the module.

        The fullname is a str.
        Returns a types.CodeType if possible, else returns None if a code object does not make sense (e.g. built-in module).
        Raises ImportError if the module cannot be found.

        Note:
            While the method has a default implementation, it is suggested that it be overridden if possible for performance.
        """#"""
        source = self.get_source(fullname)
        if source is None:
            return None
        return self.source_to_code(source)

    @abstractmethod
    def get_source(self, fullname):
        r"""
        :: qnm4mdl -> may source4mdl{universal_newline}/str | ^ImportError

        An abstract method to return the source of a module.
        It is returned as a text string using *universal newlines*, translating all recognized line separators into "'\n'" characters.
        Returns "None" if no source is available (e.g. a built-in module).
        Raises "ImportError" if the loader cannot find the module specified.
        """#"""
        raise ImportError

    @abstractmethod
    #@optional
    def is_package(self, fullname):
        r"""
        :: qnm4mdl -> bool | ^ImportError

        Optional method which when implemented should return whether the module is a package.
        The fullname is a str.
        Returns a bool.
        Raises ImportError if the module cannot be found.

        """#"""
        raise NotImplementedError('@optional')
        raise ImportError


    @staticmethod
    def source_to_code(data, path4py='<string>'):
        r"""
        :: source4mdl/(str|bytes|???) -> path4mdl/path4py/?mdl.__file__?/?spec.origin?/str -> CodeType

        Create a code object from Python source.

        The *data* argument can be whatever the "compile()" function supports (i.e. string or bytes).
        The *path* argument should be the "path" to where the source code originated from, which can be an abstract concept (e.g. location in a zip file).

        With the subsequent code object one can execute it in a module by running "exec(code, module.__dict__)".
        """#"""
        return compile(data, path4py, 'exec', dont_inherit=True)




class IExecutionLoader(ExecutionLoader, IInspectLoader):

    r"""Abstract base class for loaders that wish to support the execution of modules as scripts.

    This ABC represents one of the optional protocols specified in PEP 302.

    """#"""
    __slots__ = ()

    @abstractmethod
    def get_filename(self, fullname):
        r"""
        :: qnm4mdl -> may path4mdl/mdl.__file__[#builtin=>None#][#path4py over path4pyc#][#.py over .pyc#] | ^ImportError

        An abstract method that is to return the value of "__file__" for the specified module.
        If no path is available, "ImportError" is raised.

        If source code is available, then the method should return the path to the source file, regardless of whether a bytecode was used to load the module.
        """#"""
        raise ImportError

    @abstractmethod
    @override#++path@source_to_code()
    def get_code(self, fullname):
        r"""
        :: qnm4mdl -> may CodeType | ^ImportError

        Method to return the code object for fullname.

        Should return None if not applicable (e.g. built-in module).
        Raise ImportError if the module cannot be found.

        Note:
            While the method has a default implementation, it is suggested that it be overridden if possible for performance.
        """#"""
        source = self.get_source(fullname)
        if source is None:
            return None
        try:
            path4py = self.get_filename(fullname)
        except ImportError:
            return self.source_to_code(source)
        else:
            return self.source_to_code(source, path4py)



class IFileLoader(FileLoader, IResourceLoader, IExecutionLoader):
    r"""
    Abstract base class partially implementing the ResourceLoader and ExecutionLoader ABCs.

    An abstract base class which inherits from "ResourceLoader" and "ExecutionLoader", providing concrete implementations of "ResourceLoader.get_data()" and "ExecutionLoader.get_filename()".

    """#"""
    ___no_slots_ok___ = True
    #__slots__ = ()

    def __init__(self, fullname, path4mdl, /):
        """Cache the module name and the path to the file found by the
        finder."""
        self._name = fullname
        self._path4mdl = path4mdl

    @property
    def name(sf, /):
        '-> qnm4mdl'
        return sf._name
    @property
    def path(sf, /):
        '-> path4mdl/mdl.__file__'
        return sf._path4mdl

    def __eq__(self, other):
        return (type(self) is type(other)
            and self.name == other.name
            and self._path4mdl == other._path4mdl
            )

    def __hash__(self):
        return hash(self.name) ^ hash(self._path4mdl)

    @override
    def get_filename(self, fullname=None):
        'qnm4mdl -> path4mdl/mdl.__file__[#.py#] | ^ImportError'

        assert fullname is None or fullname == self.name
        return self._path4mdl

    @override
    def get_data(self, path4rsc, /):
        'path4rsc/str -> data/bytes4pyc/bytes | ^OSError'
        # path4rsc = Path(sf._path4mdl).parent/basename4rsc
        #   see:FileReader<path4parent/path4pkg>
        if isinstance(self, (SourceLoader, ExtensionFileLoader)):
            path4pyc = path4rsc
            with open_code(str(path4pyc)) as file:
                return file.read()
        else:
            with FileIO(path4rsc, 'r') as file:
                # [FileIO <: RawIOBase]
                return file.read() #bytes

    @override
    def get_resource_reader(self, fullname=None):
        'qnm4mdl -> may (ITraversableResources|IResourceReader){fullname not package => None}[#ResourceReader is deprecated by TraversableResources#]'
        from importlib.readers import FileReader
        return FileReader(self)

#.class FileReader(abc.TraversableResources):
#.    def __init__(self, loader):
#.        self.path = pathlib.Path(loader.path).parent
#.
#.    def resource_path(self, resource):
#.        """
#.        Return the file system path to prevent
#.        `resources.path()` from creating a temporary
#.        copy.
#.        """
#.        return str(self.path.joinpath(resource))
#.
#.    def files(self):
#.        return self.path
#.

#IFileLoader('seed', 'aaa')
    # TypeError: Can't instantiate abstract class IFileLoader with abstract methods create_module, get_code, get_source, is_package




class ISourceLoader(SourceLoader, IResourceLoader, IExecutionLoader):

    r"""Abstract base class for loading source code (and optionally any
    corresponding bytecode).

    To support loading from source code, the abstractmethods inherited from
    ResourceLoader and ExecutionLoader need to be implemented. To also support
    loading from bytecode, the optional methods specified directly by this ABC
    is required.

    Inherited abstractmethods not implemented in this ABC:

        * ResourceLoader.get_data
        * ExecutionLoader.get_filename


class importlib.abc.SourceLoader
    An abstract base class for implementing source (and optionally bytecode) file loading.
    The class inherits from both "ResourceLoader" and "ExecutionLoader", requiring the implementation of:

        * "ResourceLoader.get_data()"

        * "ExecutionLoader.get_filename()"
            Should only return the path to the source file; sourceless loading is not supported.

    The abstract methods defined by this class are to add optional bytecode file support.
    Not implementing these optional methods (or causing them to raise "NotImplementedError") causes the loader to only work with source code.
    Implementing the methods allows the loader to work with source *and* bytecode files; it does not allow for *sourceless* loading where only bytecode is provided.
    Bytecode files are an optimization to speed up loading by removing the parsing step of Python's compiler, and so no bytecode-specific API is exposed.

    optional=>:
        raise NotImplementedError('@optional')
        --> OSError

   path_stats(path)

      Optional abstract method which returns a "dict" containing metadata about the specified path.
      Supported dictionary keys are:

      * "'mtime'" (mandatory): an integer or floating-point number
        representing the modification time of the source code;

      * "'size'" (optional): the size in bytes of the source code.

      Any other keys in the dictionary are ignored, to allow for future extensions.
      If the path cannot be handled, "OSError" is raised.

      Added in version 3.3.

      Changed in version 3.4: Raise "OSError" instead of "NotImplementedError".

   path_mtime(path)

      Optional abstract method which returns the modification time for the specified path.

      Deprecated since version 3.3: This method is deprecated in favour of "path_stats()".
      You don't have to implement it, but it is still available for compatibility purposes.
      Raise "OSError" if the path cannot be handled.

      Changed in version 3.4: Raise "OSError" instead of "NotImplementedError".

   set_data(path4rsc, data)

      Optional abstract method which writes the specified bytes to a file path.
      Any intermediate directories which do not exist are to be created automatically.

      When writing to the path fails because the path is read-only ("errno.EACCES"/"PermissionError"), do not propagate the exception.

      Changed in version 3.4: No longer raises "NotImplementedError" when called.

   get_code(fullname)

      Concrete implementation of "InspectLoader.get_code()".

   exec_module(module)

      Concrete implementation of "Loader.exec_module()".

      Added in version 3.4.

   load_module(fullname)

      Concrete implementation of "Loader.load_module()".

      Deprecated since version 3.4: Use "exec_module()" instead.

   get_source(fullname)

      Concrete implementation of "InspectLoader.get_source()".

   is_package(fullname)

      Concrete implementation of "InspectLoader.is_package()".
      A module is determined to be a package if its file path (as provided by "ExecutionLoader.get_filename()") is a file named "__init__" when the file extension is removed **and** the module name itself does not end in "__init__".


    """#"""
    __slots__ = ()

    #@abstractmethod
    #@optional
    def path_mtime(self, path4rsc):
        r"""Return the (int) modification time for the path4rsc (str)."""
        return int(self.path_stats(path4rsc)['mtime'])
        #.if type(self).path_stats is __class__.path_stats:
        #.    raise OSError
        #.return int(self.path_stats(path4rsc)['mtime'])

    @abstractmethod
    #@optional
    def path_stats(self, path4rsc):
        r"""Return a metadata dict for the source pointed to by the path4rsc (str).
        Possible keys:
        - 'mtime' (mandatory) is the numeric timestamp of last source
          code modification;
        - 'size' (optional) is the size in bytes of the source code.
        """#"""
        raise OSError
            #xxx:raise NotImplementedError('@optional')
        #.if type(self).path_mtime is __class__.path_mtime:
        #.    raise OSError
        #.return {'mtime': self.path_mtime(path4rsc)}

    @abstractmethod
    #@optional
    def set_data(self, path4rsc, data):
        r"""
        -> None{ignore fails...}

        Write the bytes to the path4rsc (if possible).

        Accepts a str path and data as bytes.

        Any needed intermediary directories are to be created. If for some
        reason the file cannot be written because of permissions, fail
        silently.
        """#"""
        return None
            #xxx:raise NotImplementedError('@optional')



#   _LoaderBasics-parts => class SourceLoader(_LoaderBasics):
#.    def is_package(self, fullname):
#.        """Concrete implementation of InspectLoader.is_package by checking if
#.        the path returned by get_filename has a filename of '__init__.py'."""
#.        filename = _path_split(self.get_filename(fullname))[1]
#.        filename_base = filename.rsplit('.', 1)[0]
#.        tail_name = fullname.rpartition('.')[2]
#.        return filename_base == '__init__' and tail_name != '__init__'
#.
#.    def create_module(self, spec):
#.        """Use default semantics for module creation."""
#.
#.    def exec_module(self, module):
#.        """Execute the module."""
#.        code = self.get_code(module.__name__)
#.        if code is None:
#.            raise ImportError('cannot load module {!r} when get_code() '
#.                              'returns None'.format(module.__name__))
#.        _bootstrap._call_with_frames_removed(exec, code, module.__dict__)
#.
#.    def load_module(self, fullname):
#.        """This method is deprecated."""
#.        # Warning implemented in _load_module_shim().
#.        return _bootstrap._load_module_shim(self, fullname)
#.
#.
#.
#.    def get_source(self, fullname):
#.        """Concrete implementation of InspectLoader.get_source."""
#.        path = self.get_filename(fullname)
#.        try:
#.            source_bytes = self.get_data(path)
#.        except OSError as exc:
#.            raise ImportError('source not available through get_data()',
#.                              name=fullname) from exc
#.        return decode_source(source_bytes)
#.
#.    def source_to_code(self, data, path, *, _optimize=-1):
#.        """Return the code object compiled from source.
#.
#.        The 'data' argument can be any object type that compile() supports.
#.        """
#.        return _bootstrap._call_with_frames_removed(compile, data, path, 'exec',
#.                                        dont_inherit=True, optimize=_optimize)
#.
#.    def get_code(self, fullname):
#.        """Concrete implementation of InspectLoader.get_code.
#.
#.        Reading of bytecode requires path_stats to be implemented. To write
#.        bytecode, set_data must also be implemented.
#.
#.        """
#.        source_path = self.get_filename(fullname)
#.        source_mtime = None
#.        source_bytes = None
#.        source_hash = None
#.        hash_based = False
#.        check_source = True
#.        try:
#.            bytecode_path = cache_from_source(source_path)
#.        except NotImplementedError:
#.            bytecode_path = None
#.        else:
#.            try:
#.                st = self.path_stats(source_path)
#.            except OSError:
#.                pass
#.            else:
#.                source_mtime = int(st['mtime'])
#.                try:
#.                    data = self.get_data(bytecode_path)
#.                except OSError:
#.                    pass
#.                else:
#.                    exc_details = {
#.                        'name': fullname,
#.                        'path': bytecode_path,
#.                    }
#.                    try:
#.                        flags = _classify_pyc(data, fullname, exc_details)
#.                        bytes_data = memoryview(data)[16:]
#.                        hash_based = flags & 0b1 != 0
#.                        if hash_based:
#.                            check_source = flags & 0b10 != 0
#.                            if (_imp.check_hash_based_pycs != 'never' and
#.                                (check_source or
#.                                 _imp.check_hash_based_pycs == 'always')):
#.                                source_bytes = self.get_data(source_path)
#.                                source_hash = _imp.source_hash(
#.                                    _RAW_MAGIC_NUMBER,
#.                                    source_bytes,
#.                                )
#.                                _validate_hash_pyc(data, source_hash, fullname,
#.                                                   exc_details)
#.                        else:
#.                            _validate_timestamp_pyc(
#.                                data,
#.                                source_mtime,
#.                                st['size'],
#.                                fullname,
#.                                exc_details,
#.                            )
#.                    except (ImportError, EOFError):
#.                        pass
#.                    else:
#.                        _bootstrap._verbose_message('{} matches {}', bytecode_path,
#.                                                    source_path)
#.                        return _compile_bytecode(bytes_data, name=fullname,
#.                                                 bytecode_path=bytecode_path,
#.                                                 source_path=source_path)
#.        if source_bytes is None:
#.            source_bytes = self.get_data(source_path)
#.        code_object = self.source_to_code(source_bytes, source_path)
#.        _bootstrap._verbose_message('code object from {}', source_path)
#.        if (not sys.dont_write_bytecode and bytecode_path is not None and
#.                source_mtime is not None):
#.            if hash_based:
#.                if source_hash is None:
#.                    source_hash = _imp.source_hash(source_bytes)
#.                data = _code_to_hash_pyc(code_object, source_hash, check_source)
#.            else:
#.                data = _code_to_timestamp_pyc(code_object, source_mtime,
#.                                              len(source_bytes))
#.            try:
#.                self._cache_bytecode(source_path, bytecode_path, data)
#.            except NotImplementedError:
#.                pass
#.        return code_object
#.    #end-def get_code(self, fullname):





def _register(abstract_cls, *classes):
    for cls in classes:
        abstract_cls.register(cls)

_register(IMetaPathFinder, BuiltinImporter, FrozenImporter, PathFinder, WindowsRegistryFinder)
_register(IPathEntryFinder, FileFinder)
_register(IInspectLoader, BuiltinImporter, FrozenImporter, NamespaceLoader)
_register(IExecutionLoader, ExtensionFileLoader)
if 0b0000:_register(IFileLoader, ExtensionFileLoader)
    # ??? see:IFileLoader.get_data()=> [ExtensionFileLoader <: IFileLoader] ???
_register(IFileLoader, SourceFileLoader, SourcelessFileLoader)
_register(ISourceLoader, SourceFileLoader)


######################
######################
######################
######################
r'''[[[
FileLoader:
    SourceFileLoader(fullname, path)
          path to the extension module.
    SourcelessFileLoader(fullname, path)
          path to the bytecode file.
    ExtensionFileLoader(fullname, path)
          path to the extension module.
    # ??? see:IFileLoader.get_data() => [ExtensionFileLoader <: IFileLoader] ???
######################
importlib.machinery:
    BuiltinImporter
    FrozenImporter
    [Deprecated]WindowsRegistryFinder
    PathFinder
    FileFinder(path, *loader_details)
    SourceFileLoader(fullname, path)
    SourcelessFileLoader(fullname, path)
    ExtensionFileLoader(fullname, path)
    NamespaceLoader(name, path, path_finder)
    ModuleSpec(name, loader, *, origin=None, loader_state=None, is_package=None)
        #ModuleSpec(name, loader, *, origin=None, loader_state=None, is_package=None){has_location/_set_fileattr::bool}
######################
importlib.util:
    LazyLoader(loader)
######################



######################
######################
class importlib.machinery.BuiltinImporter

   An *importer* for built-in modules. All known built-in modules are
   listed in "sys.builtin_module_names". This class implements the
   "importlib.abc.MetaPathFinder" and "importlib.abc.InspectLoader"
   ABCs.

   Only class methods are defined by this class to alleviate the need
   for instantiation.

   Changed in version 3.5: As part of **PEP 489**, the builtin
   importer now implements "Loader.create_module()" and
   "Loader.exec_module()"

######################
class importlib.machinery.FrozenImporter

   An *importer* for frozen modules. This class implements the
   "importlib.abc.MetaPathFinder" and "importlib.abc.InspectLoader"
   ABCs.

   Only class methods are defined by this class to alleviate the need
   for instantiation.

   Changed in version 3.4: Gained "create_module()" and
   "exec_module()" methods.

######################
class importlib.machinery.WindowsRegistryFinder
   Deprecated since version 3.6: Use "site" configuration instead.
   Future versions of Python may not enable this finder by default.

######################
class importlib.machinery.PathFinder
    [PathFinder <- IMetaPathFinder]
    [PathFinder <: IMetaPathFinder]
        !! all classmethod

   A *Finder* for "sys.path" and package "__path__" attributes. This
   class implements the "importlib.abc.MetaPathFinder" ABC.

   Only class methods are defined by this class to alleviate the need
   for instantiation.

   classmethod find_spec(fullname, path=None, target=None)

      Class method that attempts to find a *spec* for the module
      specified by *fullname* on "sys.path" or, if defined, on *path*.
      For each path entry that is searched, "sys.path_importer_cache"
      is checked. If a non-false object is found then it is used as
      the *path entry finder* to look for the module being searched
      for. If no entry is found in "sys.path_importer_cache", then
      "sys.path_hooks" is searched for a finder for the path entry
      and, if found, is stored in "sys.path_importer_cache" along with
      being queried about the module. If no finder is ever found then
      "None" is both stored in the cache and returned.

      Added in version 3.4.

      Changed in version 3.5: If the current working directory --
      represented by an empty string -- is no longer valid then "None"
      is returned but no value is cached in "sys.path_importer_cache".

   classmethod invalidate_caches()

      Calls "importlib.abc.PathEntryFinder.invalidate_caches()" on all
      finders stored in "sys.path_importer_cache" that define the
      method. Otherwise entries in "sys.path_importer_cache" set to
      "None" are deleted.

      Changed in version 3.7: Entries of "None" in
      "sys.path_importer_cache" are deleted.

   Changed in version 3.4: Calls objects in "sys.path_hooks" with the
   current working directory for "''" (i.e. the empty string).

######################
class importlib.machinery.FileFinder(path, *loader_details)

   A concrete implementation of "importlib.abc.PathEntryFinder" which
   caches results from the file system.

   The *path* argument is the directory for which the finder is in
   charge of searching.

   The *loader_details* argument is a variable number of 2-item tuples
   each containing a loader and a sequence of file suffixes the loader
   recognizes. The loaders are expected to be callables which accept
   two arguments of the module's name and the path to the file found.

   The finder will cache the directory contents as necessary, making
   stat calls for each module search to verify the cache is not
   outdated. Because cache staleness relies upon the granularity of
   the operating system's state information of the file system, there
   is a potential race condition of searching for a module, creating a
   new file, and then searching for the module the new file
   represents. If the operations happen fast enough to fit within the
   granularity of stat calls, then the module search will fail. To
   prevent this from happening, when you create a module dynamically,
   make sure to call "importlib.invalidate_caches()".

   Added in version 3.3.

   path

      The path the finder will search in.

   find_spec(fullname, target=None)

      Attempt to find the spec to handle *fullname* within "path".

      Added in version 3.4.

   invalidate_caches()

      Clear out the internal cache.

   classmethod path_hook(*loader_details)

      A class method which returns a closure for use on
      "sys.path_hooks". An instance of "FileFinder" is returned by the
      closure using the path argument given to the closure directly
      and *loader_details* indirectly.

      If the argument to the closure is not an existing directory,
      "ImportError" is raised.

######################
class importlib.machinery.SourceFileLoader(fullname, path)

   A concrete implementation of "importlib.abc.SourceLoader" by
   subclassing "importlib.abc.FileLoader" and providing some concrete
   implementations of other methods.

   Added in version 3.3.

   name

      The name of the module that this loader will handle.

   path

      The path to the source file.

   is_package(fullname)

      Return "True" if "path" appears to be for a package.

   path_stats(path)

      Concrete implementation of
      "importlib.abc.SourceLoader.path_stats()".

   set_data(path, data)

      Concrete implementation of
      "importlib.abc.SourceLoader.set_data()".

   load_module(name=None)

      Concrete implementation of "importlib.abc.Loader.load_module()"
      where specifying the name of the module to load is optional.

      Deprecated since version 3.6: Use
      "importlib.abc.Loader.exec_module()" instead.

######################
class importlib.machinery.SourcelessFileLoader(fullname, path)

   A concrete implementation of "importlib.abc.FileLoader" which can
   import bytecode files (i.e. no source code files exist).

   Please note that direct use of bytecode files (and thus not source
   code files) inhibits your modules from being usable by all Python
   implementations or new versions of Python which change the bytecode
   format.

   Added in version 3.3.

   name

      The name of the module the loader will handle.

   path

      The path to the bytecode file.

   is_package(fullname)

      Determines if the module is a package based on "path".

   get_code(fullname)

      Returns the code object for "name" created from "path".

   get_source(fullname)

      Returns "None" as bytecode files have no source when this loader
      is used.

   load_module(name=None)

   Concrete implementation of "importlib.abc.Loader.load_module()"
   where specifying the name of the module to load is optional.

   Deprecated since version 3.6: Use
   "importlib.abc.Loader.exec_module()" instead.

######################
class importlib.machinery.ExtensionFileLoader(fullname, path)

   A concrete implementation of "importlib.abc.ExecutionLoader" for
   extension modules.

   The *fullname* argument specifies the name of the module the loader
   is to support. The *path* argument is the path to the extension
   module's file.

   Note that, by default, importing an extension module will fail in
   subinterpreters if it doesn't implement multi-phase init (see **PEP
   489**), even if it would otherwise import successfully.

   Added in version 3.3.

   Changed in version 3.12: Multi-phase init is now required for use
   in subinterpreters.

   name

      Name of the module the loader supports.

   path

      Path to the extension module.

   create_module(spec)

      Creates the module object from the given specification in
      accordance with **PEP 489**.

      Added in version 3.5.

   exec_module(module)

      Initializes the given module object in accordance with **PEP
      489**.

      Added in version 3.5.

   is_package(fullname)

      Returns "True" if the file path points to a package's "__init__"
      module based on "EXTENSION_SUFFIXES".

   get_code(fullname)

      Returns "None" as extension modules lack a code object.

   get_source(fullname)

      Returns "None" as extension modules do not have source code.

   get_filename(fullname)

      Returns "path".

      Added in version 3.4.

######################
class importlib.machinery.NamespaceLoader(name, path, path_finder)

   A concrete implementation of "importlib.abc.InspectLoader" for
   namespace packages.  This is an alias for a private class and is
   only made public for introspecting the "__loader__" attribute on
   namespace packages:

      >>> from importlib.machinery import NamespaceLoader
      >>> import my_namespace
      >>> isinstance(my_namespace.__loader__, NamespaceLoader)
      True
      >>> import importlib.abc
      >>> isinstance(my_namespace.__loader__, importlib.abc.Loader)
      True

   Added in version 3.11.

######################
class importlib.machinery.ModuleSpec(name, loader, *, origin=None, loader_state=None, is_package=None)

   A specification for a module's import-system-related state.  This
   is typically exposed as the module's "__spec__" attribute.  In the
   descriptions below, the names in parentheses give the corresponding
   attribute available directly on the module object, e.g.
   "module.__spec__.origin == module.__file__".  Note, however, that
   while the *values* are usually equivalent, they can differ since
   there is no synchronization between the two objects.  For example,
   it is possible to update the module's "__file__" at runtime and
   this will not be automatically reflected in the module's
   "__spec__.origin", and vice versa.

   Added in version 3.4.

   name

   ("__name__")

   The module's fully qualified name. The *finder* should always set
   this attribute to a non-empty string.

   loader

   ("__loader__")

   The *loader* used to load the module. The *finder* should always
   set this attribute.

   origin

   ("__file__")

   The location the *loader* should use to load the module. For
   example, for modules loaded from a .py file this is the filename.
   The *finder* should always set this attribute to a meaningful value
   for the *loader* to use.  In the uncommon case that there is not
   one (like for namespace packages), it should be set to "None".

   submodule_search_locations

   ("__path__")

   The list of locations where the package's submodules will be found.
   Most of the time this is a single directory. The *finder* should
   set this attribute to a list, even an empty one, to indicate to the
   import system that the module is a package.  It should be set to
   "None" for non-package modules.  It is set automatically later to a
   special object for namespace packages.

   loader_state

   The *finder* may set this attribute to an object containing
   additional, module-specific data to use when loading the module.
   Otherwise it should be set to "None".

   cached

   ("__cached__")

   The filename of a compiled version of the module's code. The
   *finder* should always set this attribute but it may be "None" for
   modules that do not need compiled code stored.

   parent

   ("__package__")

   (Read-only) The fully qualified name of the package the module is
   in (or the empty string for a top-level module). If the module is a
   package then this is the same as "name".

   has_location

   "True" if the spec's "origin" refers to a loadable location,
      "False" otherwise.  This value impacts how "origin" is
      interpreted and how the module's "__file__" is populated.


######################
######################
######################
"importlib.util" -- Utility code for importers
==============================================

**Source code:** Lib/importlib/util.py

======================================================================

This module contains the various objects that help in the construction
of an *importer*.

importlib.util.MAGIC_NUMBER

   The bytes which represent the bytecode version number. If you need
   help with loading/writing bytecode then consider
   "importlib.abc.SourceLoader".

   Added in version 3.4.

importlib.util.cache_from_source(path, debug_override=None, *, optimization=None)

   Return the **PEP 3147**/**PEP 488** path to the byte-compiled file
   associated with the source *path*.  For example, if *path* is
   "/foo/bar/baz.py" the return value would be
   "/foo/bar/__pycache__/baz.cpython-32.pyc" for Python 3.2. The
   "cpython-32" string comes from the current magic tag (see
   "get_tag()"; if "sys.implementation.cache_tag" is not defined then
   "NotImplementedError" will be raised).

   The *optimization* parameter is used to specify the optimization
   level of the bytecode file. An empty string represents no
   optimization, so "/foo/bar/baz.py" with an *optimization* of "''"
   will result in a bytecode path of
   "/foo/bar/__pycache__/baz.cpython-32.pyc". "None" causes the
   interpreter's optimization level to be used. Any other value's
   string representation is used, so "/foo/bar/baz.py" with an
   *optimization* of "2" will lead to the bytecode path of
   "/foo/bar/__pycache__/baz.cpython-32.opt-2.pyc". The string
   representation of *optimization* can only be alphanumeric, else
   "ValueError" is raised.

   The *debug_override* parameter is deprecated and can be used to
   override the system's value for "__debug__". A "True" value is the
   equivalent of setting *optimization* to the empty string. A "False"
   value is the same as setting *optimization* to "1". If both
   *debug_override* an *optimization* are not "None" then "TypeError"
   is raised.

   Added in version 3.4.

   Changed in version 3.5: The *optimization* parameter was added and
   the *debug_override* parameter was deprecated.

   Changed in version 3.6: Accepts a *path-like object*.

importlib.util.source_from_cache(path)

   Given the *path* to a **PEP 3147** file name, return the associated
   source code file path.  For example, if *path* is
   "/foo/bar/__pycache__/baz.cpython-32.pyc" the returned path would
   be "/foo/bar/baz.py".  *path* need not exist, however if it does
   not conform to **PEP 3147** or **PEP 488** format, a "ValueError"
   is raised. If "sys.implementation.cache_tag" is not defined,
   "NotImplementedError" is raised.

   Added in version 3.4.

   Changed in version 3.6: Accepts a *path-like object*.

importlib.util.decode_source(source_bytes)

   Decode the given bytes representing source code and return it as a
   string with universal newlines (as required by
   "importlib.abc.InspectLoader.get_source()").

   Added in version 3.4.

importlib.util.resolve_name(name, package)

   Resolve a relative module name to an absolute one.

   If  **name** has no leading dots, then **name** is simply returned.
   This allows for usage such as "importlib.util.resolve_name('sys',
   __spec__.parent)" without doing a check to see if the **package**
   argument is needed.

   "ImportError" is raised if **name** is a relative module name but
   **package** is a false value (e.g. "None" or the empty string).
   "ImportError" is also raised if a relative name would escape its
   containing package (e.g. requesting "..bacon" from within the
   "spam" package).

   Added in version 3.3.

   Changed in version 3.9: To improve consistency with import
   statements, raise "ImportError" instead of "ValueError" for invalid
   relative import attempts.

importlib.util.find_spec(name, package=None)

   Find the *spec* for a module, optionally relative to the specified
   **package** name. If the module is in "sys.modules", then
   "sys.modules[name].__spec__" is returned (unless the spec would be
   "None" or is not set, in which case "ValueError" is raised).
   Otherwise a search using "sys.meta_path" is done. "None" is
   returned if no spec is found.

   If **name** is for a submodule (contains a dot), the parent module
   is automatically imported.

   **name** and **package** work the same as for "import_module()".

   Added in version 3.4.

   Changed in version 3.7: Raises "ModuleNotFoundError" instead of
   "AttributeError" if **package** is in fact not a package (i.e.
   lacks a "__path__" attribute).

importlib.util.module_from_spec(spec)

   Create a new module based on **spec** and
   "spec.loader.create_module".

   If "spec.loader.create_module" does not return "None", then any
   pre-existing attributes will not be reset. Also, no
   "AttributeError" will be raised if triggered while accessing
   **spec** or setting an attribute on the module.

   This function is preferred over using "types.ModuleType" to create
   a new module as **spec** is used to set as many import-controlled
   attributes on the module as possible.

   Added in version 3.5.

importlib.util.spec_from_loader(name, loader, *, origin=None, is_package=None)

   A factory function for creating a "ModuleSpec" instance based on a
   loader.  The parameters have the same meaning as they do for
   ModuleSpec.  The function uses available *loader* APIs, such as
   "InspectLoader.is_package()", to fill in any missing information on
   the spec.

   Added in version 3.4.

importlib.util.spec_from_file_location(name, location, *, loader=None, submodule_search_locations=None)

   A factory function for creating a "ModuleSpec" instance based on
   the path to a file.  Missing information will be filled in on the
   spec by making use of loader APIs and by the implication that the
   module will be file-based.

   Added in version 3.4.

   Changed in version 3.6: Accepts a *path-like object*.

importlib.util.source_hash(source_bytes)

   Return the hash of *source_bytes* as bytes. A hash-based ".pyc"
   file embeds the "source_hash()" of the corresponding source file's
   contents in its header.

   Added in version 3.7.

importlib.util._incompatible_extension_module_restrictions(*, disable_check)

   A context manager that can temporarily skip the compatibility check
   for extension modules.  By default the check is enabled and will
   fail when a single-phase init module is imported in a
   subinterpreter. It will also fail for a multi-phase init module
   that doesn't explicitly support a per-interpreter GIL, when
   imported in an interpreter with its own GIL.

   Note that this function is meant to accommodate an unusual case;
   one which is likely to eventually go away.  There's is a pretty
   good chance this is not what you were looking for.

   You can get the same effect as this function by implementing the
   basic interface of multi-phase init (**PEP 489**) and lying about
   support for multiple interpreters (or per-interpreter GIL).

   Warning:

     Using this function to disable the check can lead to unexpected
     behavior and even crashes.  It should only be used during
     extension module development.

   Added in version 3.12.

######################
class importlib.util.LazyLoader(loader)

   A class which postpones the execution of the loader of a module
   until the module has an attribute accessed.

   This class **only** works with loaders that define "exec_module()"
   as control over what module type is used for the module is
   required. For those same reasons, the loader's "create_module()"
   method must return "None" or a type for which its "__class__"
   attribute can be mutated along with not using *slots*. Finally,
   modules which substitute the object placed into "sys.modules" will
   not work as there is no way to properly replace the module
   references throughout the interpreter safely; "ValueError" is
   raised if such a substitution is detected.

   Note:

     For projects where startup time is critical, this class allows
     for potentially minimizing the cost of loading a module if it is
     never used. For projects where startup time is not essential then
     use of this class is **heavily** discouraged due to error
     messages created during loading being postponed and thus
     occurring out of context.

   Added in version 3.5.

   Changed in version 3.6: Began calling "create_module()", removing
   the compatibility warning for "importlib.machinery.BuiltinImporter"
   and "importlib.machinery.ExtensionFileLoader".

   classmethod factory(loader)

      A class method which returns a callable that creates a lazy
      loader. This is meant to be used in situations where the loader
      is passed by class instead of by instance.

         suffixes = importlib.machinery.SOURCE_SUFFIXES
         loader = importlib.machinery.SourceFileLoader
         lazy_loader = importlib.util.LazyLoader.factory(loader)
         finder = importlib.machinery.FileFinder(path, (lazy_loader, suffixes))


Examples
========


Importing programmatically
--------------------------

To programmatically import a module, use "importlib.import_module()".

   import importlib

   itertools = importlib.import_module('itertools')


Checking if a module can be imported
------------------------------------

If you need to find out if a module can be imported without actually
doing the import, then you should use "importlib.util.find_spec()".

Note that if "name" is a submodule (contains a dot),
"importlib.util.find_spec()" will import the parent module.

   import importlib.util
   import sys

   # For illustrative purposes.
   name = 'itertools'

   if name in sys.modules:
       print(f"{name!r} already in sys.modules")
   elif (spec := importlib.util.find_spec(name)) is not None:
       # If you chose to perform the actual import ...
       module = importlib.util.module_from_spec(spec)
       sys.modules[name] = module
       spec.loader.exec_module(module)
       print(f"{name!r} has been imported")
   else:
       print(f"can't find the {name!r} module")


Importing a source file directly
--------------------------------

To import a Python source file directly, use the following recipe:

   import importlib.util
   import sys

   # For illustrative purposes.
   import tokenize
   file_path = tokenize.__file__
   module_name = tokenize.__name__

   spec = importlib.util.spec_from_file_location(module_name, file_path)
   module = importlib.util.module_from_spec(spec)
   sys.modules[module_name] = module
   spec.loader.exec_module(module)


Implementing lazy imports
-------------------------

The example below shows how to implement lazy imports:

   >>> import importlib.util
   >>> import sys
   >>> def lazy_import(name):
   ...     spec = importlib.util.find_spec(name)
   ...     loader = importlib.util.LazyLoader(spec.loader)
   ...     spec.loader = loader
   ...     module = importlib.util.module_from_spec(spec)
   ...     sys.modules[name] = module
   ...     loader.exec_module(module)
   ...     return module
   ...
   >>> lazy_typing = lazy_import("typing")
   >>> #lazy_typing is a real module object,
   >>> #but it is not loaded in memory yet.
   >>> lazy_typing.TYPE_CHECKING
   False


Setting up an importer
----------------------

For deep customizations of import, you typically want to implement an
*importer*. This means managing both the *finder* and *loader* side of
things. For finders there are two flavours to choose from depending on
your needs: a *meta path finder* or a *path entry finder*. The former
is what you would put on "sys.meta_path" while the latter is what you
create using a *path entry hook* on "sys.path_hooks" which works with
"sys.path" entries to potentially create a finder. This example will
show you how to register your own importers so that import will use
them (for creating an importer for yourself, read the documentation
for the appropriate classes defined within this package):

   import importlib.machinery
   import sys

   # For illustrative purposes only.
   SpamMetaPathFinder = importlib.machinery.PathFinder
   SpamPathEntryFinder = importlib.machinery.FileFinder
   loader_details = (importlib.machinery.SourceFileLoader,
                     importlib.machinery.SOURCE_SUFFIXES)

   # Setting up a meta path finder.
   # Make sure to put the finder in the proper location in the list in terms of
   # priority.
   sys.meta_path.append(SpamMetaPathFinder)

   # Setting up a path entry finder.
   # Make sure to put the path hook in the proper location in the list in terms
   # of priority.
   sys.path_hooks.append(SpamPathEntryFinder.path_hook(loader_details))


Approximating "importlib.import_module()"
-----------------------------------------

Import itself is implemented in Python code, making it possible to
expose most of the import machinery through importlib. The following
helps illustrate the various APIs that importlib exposes by providing
an approximate implementation of "importlib.import_module()":

   import importlib.util
   import sys

   def import_module(name, package=None):
       """An approximate implementation of import."""
       absolute_name = importlib.util.resolve_name(name, package)
       try:
           return sys.modules[absolute_name]
       except KeyError:
           pass

       path = None
       if '.' in absolute_name:
           parent_name, _, child_name = absolute_name.rpartition('.')
           parent_module = import_module(parent_name)
           path = parent_module.__spec__.submodule_search_locations
       for finder in sys.meta_path:
           spec = finder.find_spec(absolute_name, path)
           if spec is not None:
               break
       else:
           msg = f'No module named {absolute_name!r}'
           raise ModuleNotFoundError(msg, name=absolute_name)
       module = importlib.util.module_from_spec(spec)
       sys.modules[absolute_name] = module
       spec.loader.exec_module(module)
       if path is not None:
           setattr(parent_module, child_name, module)
       return module

######################

#]]]'''#'''
######################
######################
######################
#.class ModuleSpec:
#.    """The specification for a module, used for loading.
#.
#.    A module's spec is the source for information about the module.  For
#.    data associated with the module, including source, use the spec's
#.    loader.
#.
#.    `name` is the absolute name of the module.  `loader` is the loader
#.    to use when loading the module.  `parent` is the name of the
#.    package the module is in.  The parent is derived from the name.
#.
#.    `is_package` determines if the module is considered a package or
#.    not.  On modules this is reflected by the `__path__` attribute.
#.
#.    `origin` is the specific location used by the loader from which to
#.    load the module, if that information is available.  When filename is
#.    set, origin will match.
#.
#.    `has_location` indicates that a spec's "origin" reflects a location.
#.    When this is True, `__file__` attribute of the module is set.
#.
#.    `cached` is the location of the cached bytecode file, if any.  It
#.    corresponds to the `__cached__` attribute.
#.
#.    `submodule_search_locations` is the sequence of path entries to
#.    search when importing submodules.  If set, is_package should be
#.    True--and False otherwise.
#.
#.    Packages are simply modules that (may) have submodules.  If a spec
#.    has a non-None value in `submodule_search_locations`, the import
#.    system will consider modules loaded from the spec as packages.
#.
#.    Only finders (see importlib.abc.MetaPathFinder and
#.    importlib.abc.PathEntryFinder) should modify ModuleSpec instances.
#.
#.    """
#.
#.    def __init__(self, name, loader, *, origin=None, loader_state=None,
#.                 is_package=None):
#.        self.name = name
#.        self.loader = loader
#.        self.origin = origin
#.        self.loader_state = loader_state
#.        self.submodule_search_locations = [] if is_package else None
#.        self._uninitialized_submodules = []
#.
#.        # file-location attributes
#.        self._set_fileattr = False
#.        self._cached = None
#.
#.    def __repr__(self):
#.        args = ['name={!r}'.format(self.name),
#.                'loader={!r}'.format(self.loader)]
#.        if self.origin is not None:
#.            args.append('origin={!r}'.format(self.origin))
#.        if self.submodule_search_locations is not None:
#.            args.append('submodule_search_locations={}'
#.                        .format(self.submodule_search_locations))
#.        return '{}({})'.format(self.__class__.__name__, ', '.join(args))
#.
#.    def __eq__(self, other):
#.        smsl = self.submodule_search_locations
#.        try:
#.            return (self.name == other.name and
#.                    self.loader == other.loader and
#.                    self.origin == other.origin and
#.                    smsl == other.submodule_search_locations and
#.                    self.cached == other.cached and
#.                    self.has_location == other.has_location)
#.        except AttributeError:
#.            return NotImplemented
#.
#.    @property
#.    def cached(self):
#.        if self._cached is None:
#.            if self.origin is not None and self._set_fileattr:
#.                if _bootstrap_external is None:
#.                    raise NotImplementedError
#.                self._cached = _bootstrap_external._get_cached(self.origin)
#.        return self._cached
#.
#.    @cached.setter
#.    def cached(self, cached):
#.        self._cached = cached
#.
#.    @property
#.    def parent(self):
#.        """The name of the module's parent."""
#.        if self.submodule_search_locations is None:
#.            return self.name.rpartition('.')[0]
#.        else:
#.            return self.name
#.
#.    @property
#.    def has_location(self):
#.        return self._set_fileattr
#.
#.    @has_location.setter
#.    def has_location(self, value):
#.        self._set_fileattr = bool(value)
#.
#.
#.def spec_from_loader(name, loader, *, origin=None, is_package=None):
#.    """Return a module spec based on various loader methods."""
#.    if origin is None:
#.        origin = getattr(loader, '_ORIGIN', None)
#.
#.    if not origin and hasattr(loader, 'get_filename'):
#.        if _bootstrap_external is None:
#.            raise NotImplementedError
#.        spec_from_file_location = _bootstrap_external.spec_from_file_location
#.
#.        if is_package is None:
#.            return spec_from_file_location(name, loader=loader)
#.        search = [] if is_package else None
#.        return spec_from_file_location(name, loader=loader,
#.                                       submodule_search_locations=search)
#.
#.    if is_package is None:
#.        if hasattr(loader, 'is_package'):
#.            try:
#.                is_package = loader.is_package(name)
#.            except ImportError:
#.                is_package = None  # aka, undefined
#.        else:
#.            # the default
#.            is_package = False
#.
#.    return ModuleSpec(name, loader, origin=origin, is_package=is_package)
#.
#.
#.def _spec_from_module(module, loader=None, origin=None):
#.    # This function is meant for use in _setup().
#.    try:
#.        spec = module.__spec__
#.    except AttributeError:
#.        pass
#.    else:
#.        if spec is not None:
#.            return spec
#.
#.    name = module.__name__
#.    if loader is None:
#.        try:
#.            loader = module.__loader__
#.        except AttributeError:
#.            # loader will stay None.
#.            pass
#.    try:
#.        location = module.__file__
#.    except AttributeError:
#.        location = None
#.    if origin is None:
#.        if loader is not None:
#.            origin = getattr(loader, '_ORIGIN', None)
#.        if not origin and location is not None:
#.            origin = location
#.    try:
#.        cached = module.__cached__
#.    except AttributeError:
#.        cached = None
#.    try:
#.        submodule_search_locations = list(module.__path__)
#.    except AttributeError:
#.        submodule_search_locations = None
#.
#.    spec = ModuleSpec(name, loader, origin=origin)
#.    spec._set_fileattr = False if location is None else (origin == location)
#.    spec.cached = cached
#.    spec.submodule_search_locations = submodule_search_locations
#.    return spec


#grep '\(_set_fileattr\|has_location\).*=' -r /sdcard/0my_files/tmp/py_lib_src/importlib/

#.# Module specifications #######################################################
#.
#._POPULATE = object()
#.
#.
#.def spec_from_file_location(name, location=None, *, loader=None,
#.                            submodule_search_locations=_POPULATE):
#.    """Return a module spec based on a file location.
#.
#.    To indicate that the module is a package, set
#.    submodule_search_locations to a list of directory paths.  An
#.    empty list is sufficient, though its not otherwise useful to the
#.    import system.
#.
#.    The loader must take a spec as its only __init__() arg.
#.
#.    """
#.    if location is None:
#.        # The caller may simply want a partially populated location-
#.        # oriented spec.  So we set the location to a bogus value and
#.        # fill in as much as we can.
#.        location = '<unknown>'
#.        if hasattr(loader, 'get_filename'):
#.            # ExecutionLoader
#.            try:
#.                location = loader.get_filename(name)
#.            except ImportError:
#.                pass
#.    else:
#.        location = _os.fspath(location)
#.        if not _path_isabs(location):
#.            try:
#.                location = _path_join(_os.getcwd(), location)
#.            except OSError:
#.                pass
#.
#.    # If the location is on the filesystem, but doesn't actually exist,
#.    # we could return None here, indicating that the location is not
#.    # valid.  However, we don't have a good way of testing since an
#.    # indirect location (e.g. a zip file or URL) will look like a
#.    # non-existent file relative to the filesystem.
#.
#.    spec = _bootstrap.ModuleSpec(name, loader, origin=location)
#.    spec._set_fileattr = True
#.
#.    # Pick a loader if one wasn't provided.
#.    if loader is None:
#.        for loader_class, suffixes in _get_supported_file_loaders():
#.            if location.endswith(tuple(suffixes)):
#.                loader = loader_class(name, location)
#.                spec.loader = loader
#.                break
#.        else:
#.            return None
#.
#.    # Set submodule_search_paths appropriately.
#.    if submodule_search_locations is _POPULATE:
#.        # Check the loader.
#.        if hasattr(loader, 'is_package'):
#.            try:
#.                is_package = loader.is_package(name)
#.            except ImportError:
#.                pass
#.            else:
#.                if is_package:
#.                    spec.submodule_search_locations = []
#.    else:
#.        spec.submodule_search_locations = submodule_search_locations
#.    if spec.submodule_search_locations == []:
#.        if location:
#.            dirname = _path_split(location)[0]
#.            spec.submodule_search_locations.append(dirname)
#.
#.    return spec


#ModuleSpec(name, loader, *, origin=None, loader_state=None, is_package=None){has_location/_set_fileattr::bool}


######################
######################
#view /sdcard/0my_files/tmp/py_lib_src/importlib/_bootstrap_external.py
######################
#.######################
#.class _LoaderBasics:
#.    #see:above: class ISourceLoader(SourceLoader, IResourceLoader, IExecutionLoader):
#.    def is_package(self, fullname):
#.    def create_module(self, spec):
#.        return None
#.    def exec_module(self, module):
#.    def load_module(self, fullname):
#.######################
#.class SourceLoader(_LoaderBasics):
#.    def path_mtime(self, path):
#.    def path_stats(self, path):
#.    def set_data(self, path, data):
#.    def get_source(self, fullname):
#.    def source_to_code(self, data, path, *, _optimize=-1):
#.    def get_code(self, fullname):
#.######################
#.class FileLoader:
#.    def __init__(self, fullname, path):
#.    def __eq__(self, other):
#.    def __hash__(self):
#.    def get_filename(self, fullname):
#.    def load_module(self, fullname):
#.    def get_data(self, path):
#.    def get_resource_reader(self, module):
#.######################
#.class SourceFileLoader(FileLoader, SourceLoader):
#.    def path_stats(self, path):
#.    def set_data(self, path, data, *, _mode=0o666):
#.######################
#.class SourcelessFileLoader(FileLoader, _LoaderBasics):
#.    def get_code(self, fullname):
#.    def get_source(self, fullname):
#.######################
#.class ExtensionFileLoader(FileLoader, _LoaderBasics):
#.    def __init__(self, name, path):
#.    def __eq__(self, other):
#.    def __hash__(self):
#.    def create_module(self, spec):
#.    def exec_module(self, module):
#.    def is_package(self, fullname):
#.    def get_code(self, fullname):
#.        return None
#.    def get_source(self, fullname):
#.        return None
#.    def get_filename(self, fullname):
#.        return sf.path
#.######################
#.class NamespaceLoader:
#.    def __init__(self, name, path, path_finder):
#.        self._path = _NamespacePath(name, path, path_finder)
#.
#.    @staticmethod
#.    def module_repr(module):
#.        """Return repr for the module.
#.
#.        The method is deprecated.  The import machinery does the job itself.
#.
#.        """
#.        _warnings.warn("NamespaceLoader.module_repr() is deprecated and "
#.                       "slated for removal in Python 3.12", DeprecationWarning)
#.        return '<module {!r} (namespace)>'.format(module.__name__)
#.
#.    def is_package(self, fullname):
#.        return True
#.
#.    def get_source(self, fullname):
#.        return ''
#.
#.    def get_code(self, fullname):
#.        return compile('', '<string>', 'exec', dont_inherit=True)
#.
#.    def create_module(self, spec):
#.        """Use default semantics for module creation."""
#.        return None
#.
#.    def exec_module(self, module):
#.        pass
#.
#.    def load_module(self, fullname):
#.        """Load a namespace module.
#.
#.        This method is deprecated.  Use exec_module() instead.
#.
#.        """
#.        # The import system never calls this method.
#.        _bootstrap._verbose_message('namespace module loaded with path {!r}',
#.                                    self._path)
#.        # Warning implemented in _load_module_shim().
#.        return _bootstrap._load_module_shim(self, fullname)
#.
#.    def get_resource_reader(self, module):
#.        from importlib.readers import NamespaceReader
#.        return NamespaceReader(self._path)
#.######################
######################
######################




######################
######################
######################
__all__
from seed.for_libs.for_importlib import *
