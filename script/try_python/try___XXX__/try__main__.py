

'''
py -m xxx.yyy
are there modules named "xxx.yyy", "__main__" and "xxx.__main__"?
    there are "xxx.yyy", "__main__" but no "xxx.__main__".
    "__main__"'s __package__ is "xxx" though not named as "xxx.__main__"!!
    ==>> __package__ may not a prefix of __name__!!
'''


import os.path
from importlib import import_module
from .__init__ import *

print("__name__: {!r}; __package__: {!r}".format(__name__, __package__))

if __name__ == "__main__":
    assert __file__
    #assert __package__
    fname = os.path.basename(__file__)
    base, _ = os.path.splitext(fname)
    assert base

    print(base, __package__)
    # bug: xxx_this = import_module(base, __package__)
    def abs_module_name_from_pkg_base(pkg, base):
        return pkg + '.' + base if pkg else base
    module_name = abs_module_name_from_pkg_base(__package__, base)
    module_name_main = abs_module_name_from_pkg_base(__package__, "__main__")

    xxx_this = import_module(module_name)
    if module_name_main != "__main__":
        try:
            xxx_thismain = import_module(module_name_main)
        except ImportError:
            pass
        else:
            raise ...
    builtin_main = import_module("__main__")
    #assert xxx_this is not xxx_thismain
    assert xxx_this is not builtin_main
    #assert xxx_thismain is builtin_main # !!!!!!!!!

    def show_module(m):
        print('module: {!r}; package: {!r}'.format(m, xxx_this.__package__))
    
    show_module(xxx_this)
    show_module(builtin_main)
    


