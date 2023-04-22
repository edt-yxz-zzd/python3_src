r'''
e ../../python3_src/seed/pkg_tools/import_object.py

seed.pkg_tools.import_object

from seed.pkg_tools.import_object import import_object, import4qobject

#'''

__all__ = '''
    import_object
    import4qobject
    '''.split()



import builtins
from importlib import import_module
from operator import attrgetter



def import_object(qual_name, module_obj=None, /):
    '''

example:
    >>> _Set = import_object('collections.abc.Set')
    >>> from collections.abc import Set
    >>> _Set is Set
    True

    >>> import collections.abc as cabc
    >>> _Set = import_object('collections.abc.Set', cabc)
    >>> _Set is Set
    True

    >>> _int = import_object('int')
    >>> _int is int
    True

    >>> _len = import_object('__len__', [])
    >>> _len()
    0

    >>> _len = import_object('__len__', list)
    >>> _len is list.__len__
    True

    >>> this = import_object
    >>> this_name = 'import_object'
    >>> this_name == this.__name__
    True

    >>> this_qname = '.'.join([__name__, this_name])
    >>> import_object(this_qname) is this
    True

    >>> this_module = import_module(__name__)
    >>> import_object(this_qname, this_module) is this
    True
'''
    module_qname, sep, obj_name = qual_name.rpartition('.')
    if not module_qname:
        if sep:
            raise ValueError('must be qual_name, not relative name')

        if module_obj is None:
            module_obj = builtins
    else:
        if module_obj is not None:
            if module_obj.__name__ != module_qname:
                raise ValueError(f'{module_qname!r}==module_qname != module_obj.__name__ == {module_obj.__name__!r}')
        else:
            module_obj = import_module(module_qname)
    return getattr(module_obj, obj_name)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    import sys
    this_module = sys.modules['__main__']
    if __package__:
        err_qname = __package__ + '.' + '__main__'
        assert err_qname not in sys.modules

def check_may_str(may_s, /):
    if not (may_s is None or type(may_s) is str): raise TypeError

def import4qobject(may_qname4module, may_qname4obj, /):
    check_may_str(may_qname4obj)
    check_may_str(may_qname4module)
    if may_qname4module:
        qname4module = may_qname4module
        module_obj = import_module(qname4module)
    else:
        module_obj = builtins

    if may_qname4obj:
        qname4obj = may_qname4obj
        obj = attrgetter(qname4obj)(module_obj)
    else:
        obj = module_obj
    return obj

from seed.pkg_tools.import_object import import_object, import4qobject

