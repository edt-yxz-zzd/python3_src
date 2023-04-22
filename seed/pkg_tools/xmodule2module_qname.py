#__all__:goto
r'''[[[
e ../../python3_src/seed/pkg_tools/xmodule2module_qname.py

py -m seed.pkg_tools.xmodule2module_qname
py -m nn_ns.app.debug_cmd  seed.pkg_tools.xmodule2module_qname
py -m nn_ns.app.adhoc_argparser__main__call8module  seed.pkg_tools.xmodule2module_qname


>>> from seed.pkg_tools.xmodule2module_qname import xmodule2module_qname, xmodule2module_obj
>>> import seed.pkg_tools as seed__pkg_tools__
>>> import seed as seed__

>>> xmodule2module_qname(seed__pkg_tools__)
'seed.pkg_tools'
>>> xmodule2module_qname('seed.pkg_tools')
'seed.pkg_tools'
>>> xmodule2module_qname('.pkg_tools', seed__)
'seed.pkg_tools'
>>> xmodule2module_qname('.pkg_tools', 'seed')
'seed.pkg_tools'


>>> xmodule2module_obj(seed__pkg_tools__) is seed__pkg_tools__
True
>>> xmodule2module_obj('seed.pkg_tools') is seed__pkg_tools__
True
>>> xmodule2module_obj('.pkg_tools', seed__) is seed__pkg_tools__
True
>>> xmodule2module_obj('.pkg_tools', 'seed') is seed__pkg_tools__
True




#]]]'''
__all__ = r'''
'''.split()#'''
__all__


from importlib import import_module

def xmodule2module_qname(module_obj_or_qname_or_dot_name, may_xpkg=None, /):
    'xmodule/(module_obj|qname|dot_name) -> may_xpkg/(None|pkg_obj|qname) -> module_qname'
    xmodule = module_obj_or_qname_or_dot_name
    if type(xmodule) is str:
        module_xname = xmodule
        if not module_xname: raise TypeError('module_xname is empty')

        if module_xname.startswith('.'):
            module_relative_name = module_dot_name = module_xname
            if may_xpkg is None: raise TypeError('may_xpkg is None and module_xname is module_relative_name')
            xpkg = may_xpkg
            pkg_qname = xmodule2module_qname(xpkg)
            module_qname = pkg_qname + module_relative_name
        else:
            module_qname = module_xname
        module_qname
    elif type(xmodule) is tuple:raise TypeError
    elif xmodule is None:raise TypeError
    else:
        module_obj = xmodule
        module_qname = module_obj.__name__
    module_qname

    return module_qname

def xmodule2module_obj(module_obj_or_qname_or_dot_name, may_xpkg=None, /):
    'xmodule/(module_obj|qname|dot_name) -> may_xpkg/(None|pkg_obj|qname) -> module_obj'
    xmodule = module_obj_or_qname_or_dot_name
    if type(xmodule) is str:
        module_xname = xmodule
        if not module_xname: raise TypeError('module_xname is empty')

        if module_xname.startswith('.'):
            module_relative_name = module_dot_name = module_xname
            if may_xpkg is None:
                may_pkg_qname = None
                    #import_module() will raise
            else:
                xpkg = may_xpkg
                pkg_qname = xmodule2module_qname(xpkg)
                may_pkg_qname = pkg_qname
            may_pkg_qname
            module_relative_name
        else:
            module_qname = module_xname
            may_pkg_qname = None
        may_pkg_qname
        module_xname
        module_obj = import_module(module_xname, may_pkg_qname)
    elif type(xmodule) is tuple:raise TypeError
    elif xmodule is None:raise TypeError
    else:
        module_obj = xmodule
    module_obj
    if 0:
        #可能是 拟模块对象pseudo_module_obj, 类似ECHO
        if not hasattr(module_obj, '__dict__'): raise TypeError
        if not hasattr(module_obj, '__name__'): raise TypeError
    return module_obj



from seed.pkg_tools.xmodule2module_qname import xmodule2module_qname, xmodule2module_obj
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +IGNORE_EXCEPTION_DETAIL

