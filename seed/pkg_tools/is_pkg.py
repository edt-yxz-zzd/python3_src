
#e ../../python3_src/seed/pkg_tools/is_pkg.py
from inspect import ismodule as is_module_

def is_pkg_(module_obj, /):
    return is_module_(module_obj) and hasattr(module_obj, '__path__')

from seed.pkg_tools.is_pkg import is_pkg_, is_module_
