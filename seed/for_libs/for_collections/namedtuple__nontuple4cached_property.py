#__all__:goto
r'''[[[
e ../../python3_src/seed/for_libs/for_collections/namedtuple__nontuple4cached_property.py

seed.for_libs.for_collections.namedtuple__nontuple4cached_property
py -m nn_ns.app.debug_cmd   seed.for_libs.for_collections.namedtuple__nontuple4cached_property -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.for_libs.for_collections.namedtuple__nontuple4cached_property:__doc__ -ht # -ff -df

[[
namedtuple work with cached_property:
    from functools import cached_property
    from collections import namedtuple

cp -iv -t /sdcard/0my_files/tmp/out4py/py_src/ ~/../usr/lib/python3.11/collections/*.py
rm -iv -r /sdcard/0my_files/tmp/out4py/py_src/collections/__pycache__
view /sdcard/0my_files/tmp/out4py/py_src/collections/__init__.py
]]

]]]'''#'''
__all__ = r'''
mk_named_pseudo_tuple_
'''.split()#'''
    #_IBase4named_pseudo_tuple
__all__
___begin_mark_of_excluded_global_names__0___ = ...
import sys # intern
from keyword import iskeyword
from operator import itemgetter
from collections.abc import Sequence
from abc import abstractmethod
#from functools import cached_property
#from collections import namedtuple
#namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)

#.from itertools import islice
#.from seed.tiny_.check import check_type_is, check_int_ge
#.
#.from seed.abc.abc__ver1 import abstractmethod, override, ABC
from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_
repr_helper = lazy_import4func_('seed.helper.repr_input', 'repr_helper', __name__)
lazy_import4funcs_('seed.tiny', 'mk_tuple,print_err', __name__)
if 0:from seed.tiny import mk_tuple,print_err
#.from seed.helper.repr_input import repr_helper
#.from seed.tiny_._Base4repr import _Base4repr
        #sf._reset4repr(may_args4repr, may_kwds4repr)
        #sf._init4repr(*args4repr, **kwds4repr)
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError

class _IBase4named_pseudo_tuple(Sequence):
    #__slots__ = '__dict__ __weakref__'.split()
    #@class_property
    @property
    @abstractmethod
    def _fields(cls, /):
        'class_property{field_names}'
    def __new__(cls, /, *args, **kwds):
        field_names = cls._fields
        if not len(field_names) == len(args) + len(kwds):raise TypeError
        if kwds:
            if not dict(nms:=field_names[-len(kwds):]) == kwds.keys():raise TypeError
            args = (*args, *(kwds[nm] for nm in nms))
        del kwds
        args
        return cls._make(args)#using: ._check6make_
    def __repr__(sf, /):
        return repr_helper(sf, *sf._0_args)
    def _check6make_(sf, /):
        '-> None # called by cls._make()'
        pass
    @classmethod
    def _make(cls, iterable, /):
        args = mk_tuple(iterable)
        if not len(args) == len(cls._fields):
            raise TypeError(f'Expected {len(cls._fields)} arguments, got {len(args)}')
        sf = super(__class__, cls).__new__(cls)
        sf._0_args = args
        #sf._check6make_()
        cls._check6make_(sf)
        return sf
    def _replace(sf, /, **kwds):
        ot = sf._make(map(kwds.pop, sf._fields, sf._0_args))
        if kwds:
            raise ValueError(f'Got unexpected field names: {sorted(kwds)!r}')
        return ot

    def _asdict(sf, /):
        return dict(zip(sf._fields, sf._0_args))
    def __getnewargs__(sf, /):
        return sf._0_args
    def __bool__(sf, /):
        return bool(sf._0_args)
    def __len__(sf, /):
        return len(sf._0_args)
    def __iter__(sf, /):
        return iter(sf._0_args)
    def __reversed__(sf, /):
        return reversed(sf._0_args)
    def __getitem__(sf, k, /):
        return sf._0_args[k]
#end-class _IBase4named_pseudo_tuple(Sequence):
#def namedtuple(typename, field_names, *, rename=False, defaults=None, module=None):
#def namedtuple(typename, field_names, *, rename=False, defaults=None, module=None):
#def mk_named_pseudo_tuple_(typename, field_names, /, *, module=None):
def mk_named_pseudo_tuple_(__module__,typename, field_names, /):
    #defaults:'_field_defaults': field_defaults,
    #   __new__.__defaults__ = defaults
    if type(field_names) is str:
        field_names = field_names.replace(',', ' ').split()
    field_names = list(map(str, field_names))
    #######
    for nm in field_names:
        if not nm.isidentifier():raise TypeError
    for nm in field_names:
        if nm.startswith('_') and not nm.isdigit():raise TypeError
    for nm in field_names:
        if iskeyword(nm):raise TypeError
    if not len(set(field_names)) == len(field_names):raise TypeError
    #######

    typename = sys.intern(str(typename))
    field_names = tuple(map(sys.intern, field_names))
    #.module = module if module else ''
    #.class_namespace = dict(__module__=module, __match_args__=field_names)
    #.class_namespace = dict(__match_args__=field_names)
    param_list__str = ', '.join(field_names)
    class_namespace = dict(__module__=__module__, _fields=field_names, __match_args__=field_names, __doc__=f'{typename}({param_list__str})')
    for index, name in enumerate(field_names):
        class_namespace[name] = property(itemgetter(index), doc=f'[sf.{name} =[def]= sf[{index}]]')
    class_namespace

    T = type(typename, (_IBase4named_pseudo_tuple,), class_namespace)
    return T

    #.# For pickling to work, the __module__ variable needs to be set to the frame where the named tuple is created.
    #.if module is None:
    #.    try:
    #.        module = sys._getframe(1).f_globals.get('__name__', '__main__')
    #.    except (AttributeError, ValueError):
    #.        pass
    #.if module is not None:
    #.    T.__module__ = module

    #.return T
#def mk_named_pseudo_tuple_(typename, field_names, /, *, module=None):



r'''[[[
copy from:~/../usr/lib/python3.11/collections/__init__.py
    view /sdcard/0my_files/tmp/out4py/py_src/collections/__init__.py
######################
### namedtuple
######################
try:
    from _collections import _tuplegetter
except ImportError:
    _tuplegetter = lambda index, doc: property(_itemgetter(index), doc=doc)

def namedtuple(typename, field_names, *, rename=False, defaults=None, module=None):
    """Returns a new subclass of tuple with named fields.

    >>> Point = namedtuple('Point', ['x', 'y'])
    >>> Point.__doc__                   # docstring for the new class
    'Point(x, y)'
    >>> p = Point(11, y=22)             # instantiate with positional args or keywords
    >>> p[0] + p[1]                     # indexable like a plain tuple
    33
    >>> x, y = p                        # unpack like a regular tuple
    >>> x, y
    (11, 22)
    >>> p.x + p.y                       # fields also accessible by name
    33
    >>> d = p._asdict()                 # convert to a dictionary
    >>> d['x']
    11
    >>> Point(**d)                      # convert from a dictionary
    Point(x=11, y=22)
    >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
    Point(x=100, y=22)

    """

    # Validate the field names.  At the user's option, either generate an error
    # message or automatically replace the field name with a valid name.
    if isinstance(field_names, str):
        field_names = field_names.replace(',', ' ').split()
    field_names = list(map(str, field_names))
    typename = _sys.intern(str(typename))

    if rename:
        seen = set()
        for index, name in enumerate(field_names):
            if (not name.isidentifier()
                or _iskeyword(name)
                or name.startswith('_')
                or name in seen):
                field_names[index] = f'_{index}'
            seen.add(name)

    for name in [typename] + field_names:
        if type(name) is not str:
            raise TypeError('Type names and field names must be strings')
        if not name.isidentifier():
            raise ValueError('Type names and field names must be valid '
                             f'identifiers: {name!r}')
        if _iskeyword(name):
            raise ValueError('Type names and field names cannot be a '
                             f'keyword: {name!r}')

    seen = set()
    for name in field_names:
        if name.startswith('_') and not rename:
            raise ValueError('Field names cannot start with an underscore: '
                             f'{name!r}')
        if name in seen:
            raise ValueError(f'Encountered duplicate field name: {name!r}')
        seen.add(name)

    field_defaults = {}
    if defaults is not None:
        defaults = tuple(defaults)
        if len(defaults) > len(field_names):
            raise TypeError('Got more default values than field names')
        field_defaults = dict(reversed(list(zip(reversed(field_names),
                                                reversed(defaults)))))

    # Variables used in the methods and docstrings
    field_names = tuple(map(_sys.intern, field_names))
    num_fields = len(field_names)
    arg_list = ', '.join(field_names)
    if num_fields == 1:
        arg_list += ','
    repr_fmt = '(' + ', '.join(f'{name}=%r' for name in field_names) + ')'
    tuple_new = tuple.__new__
    _dict, _tuple, _len, _map, _zip = dict, tuple, len, map, zip

    # Create all the named tuple methods to be added to the class namespace

    namespace = {
        '_tuple_new': tuple_new,
        '__builtins__': {},
        '__name__': f'namedtuple_{typename}',
    }
    code = f'lambda _cls, {arg_list}: _tuple_new(_cls, ({arg_list}))'
    __new__ = eval(code, namespace)
    __new__.__name__ = '__new__'
    __new__.__doc__ = f'Create new instance of {typename}({arg_list})'
    if defaults is not None:
        __new__.__defaults__ = defaults

    @classmethod
    def _make(cls, iterable):
        result = tuple_new(cls, iterable)
        if _len(result) != num_fields:
            raise TypeError(f'Expected {num_fields} arguments, got {len(result)}')
        return result

    _make.__func__.__doc__ = (f'Make a new {typename} object from a sequence '
                              'or iterable')

    def _replace(self, /, **kwds):
        result = self._make(_map(kwds.pop, field_names, self))
        if kwds:
            raise ValueError(f'Got unexpected field names: {list(kwds)!r}')
        return result

    _replace.__doc__ = (f'Return a new {typename} object replacing specified '
                        'fields with new values')

    def __repr__(self):
        'Return a nicely formatted representation string'
        return self.__class__.__name__ + repr_fmt % self

    def _asdict(self):
        'Return a new dict which maps field names to their values.'
        return _dict(_zip(self._fields, self))

    def __getnewargs__(self):
        'Return self as a plain tuple.  Used by copy and pickle.'
        return _tuple(self)

    # Modify function metadata to help with introspection and debugging
    for method in (
        __new__,
        _make.__func__,
        _replace,
        __repr__,
        _asdict,
        __getnewargs__,
    ):
        method.__qualname__ = f'{typename}.{method.__name__}'

    # Build-up the class namespace dictionary
    # and use type() to build the result class
    class_namespace = {
        '__doc__': f'{typename}({arg_list})',
        '__slots__': (),
        '_fields': field_names,
        '_field_defaults': field_defaults,
        '__new__': __new__,
        '_make': _make,
        '_replace': _replace,
        '__repr__': __repr__,
        '_asdict': _asdict,
        '__getnewargs__': __getnewargs__,
        '__match_args__': field_names,
    }
    for index, name in enumerate(field_names):
        doc = _sys.intern(f'Alias for field number {index}')
        class_namespace[name] = _tuplegetter(index, doc)

    result = type(typename, (tuple,), class_namespace)

    # For pickling to work, the __module__ variable needs to be set to the frame
    # where the named tuple is created.  Bypass this step in environments where
    # sys._getframe is not defined (Jython for example) or sys._getframe is not
    # defined for arguments greater than 0 (IronPython), or where the user has
    # specified a particular module.
    if module is None:
        try:
            module = _sys._getframe(1).f_globals.get('__name__', '__main__')
        except (AttributeError, ValueError):
            pass
    if module is not None:
        result.__module__ = module

    return result

######################
#end:namedtuple
######################
#]]]'''#'''

__all__
#[mk_named_pseudo_tuple_] = lazy_import4funcs_('seed.for_libs.for_collections.namedtuple__nontuple4cached_property', 'mk_named_pseudo_tuple_', __name__)
from seed.for_libs.for_collections.namedtuple__nontuple4cached_property import mk_named_pseudo_tuple_
#def mk_named_pseudo_tuple_(__module__,typename, field_names, /):
#    def _check6make_(sf, /):

from seed.for_libs.for_collections.namedtuple__nontuple4cached_property import *
