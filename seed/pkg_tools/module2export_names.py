#__all__:goto
r'''[[[
e ../../python3_src/seed/pkg_tools/module2export_names.py
    view ../../python3_src/seed/pkg_tools/xmodule2module_qname.py

to get module_obj.__all__


py -m seed.pkg_tools.module2export_names
py -m nn_ns.app.debug_cmd  seed.pkg_tools.module2export_names
py -m nn_ns.app.adhoc_argparser__main__call8module  seed.pkg_tools.module2export_names

>>> from seed.pkg_tools.module2export_names import is_export_name_by_default_setting__nonstrict, is_export_name_by_default_setting
>>> from seed.pkg_tools.module2export_names import xmodule2export_names, module_obj2export_names

>>> xmodule2export_names('seed.pkg_tools.module2export_names')
['is_export_name_by_default_setting', 'is_export_name_by_default_setting__nonstrict', 'module_obj2export_names', 'xmodule2export_names']
>>> xmodule2export_names('seed.pkg_tools.module2export_names', to_sort=False)
['module_obj2export_names', 'is_export_name_by_default_setting__nonstrict', 'is_export_name_by_default_setting', 'xmodule2export_names', 'module_obj2export_names']



#]]]'''
__all__ = r'''
    module_obj2export_names


    is_export_name_by_default_setting__nonstrict
    is_export_name_by_default_setting
    xmodule2export_names
    module_obj2export_names
'''.split()#'''
__all__


#from seed.tiny import mk_tuple, check_type_is
from seed.pkg_tools.xmodule2module_qname import xmodule2module_obj

def is_export_name_by_default_setting__nonstrict(name, /):
    return is_export_name_by_default_setting(name, strict=False)
def is_export_name_by_default_setting(name, /, *, strict=True):
    ok = (type(name) is str and name and name.isidentifier())
    if strict:
        if not ok: raise TypeError
    else:
        if not ok: return False
    return (not name.startswith('_')) or (name.startswith('__') and name.endswith('__'))

def xmodule2export_names(module_obj_or_qname_or_dot_name, may_xpkg=None, /, *, to_sort=True):
    'xmodule/(module_obj|qname|dot_name) -> may_xpkg/(None|pkg_obj|qname) -> module_qname'
    xmodule = module_obj_or_qname_or_dot_name
    module_obj = xmodule2module_obj(xmodule, may_xpkg)
    export_names = module_obj2export_names(module_obj, to_sort=to_sort)
    return export_names

def module_obj2export_names(module_obj, /, *, to_sort=True):
    may_export_names = getattr(module_obj, '__all__', None)
    if may_export_names is None:
        export_names = vars(module_obj).keys()
    else:
        export_names = may_export_names
        len(export_names) #check
    export_names = filter(is_export_name_by_default_setting__nonstrict, export_names)

    if to_sort:
        export_names = sorted({*export_names})
    else:
        export_names = [*export_names]
    return export_names

from seed.pkg_tools.module2export_names import is_export_name_by_default_setting__nonstrict, is_export_name_by_default_setting
from seed.pkg_tools.module2export_names import xmodule2export_names, module_obj2export_names

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +IGNORE_EXCEPTION_DETAIL

