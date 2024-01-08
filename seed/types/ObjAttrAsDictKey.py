#__all__:goto
r'''[[[
e ../../python3_src/seed/types/ObjAttrAsDictKey.py
e ../../python3_src/seed/for_libs/for_builtins/for_eval_exec.py
    view ../../python3_src/seed/tiny_/types5py.py
        kwargs2Attrs := py.types::SimpleNamespace
    ######################
    view ../../python3_src/seed/mapping_tools/key_as_attr.py
    view ../../python3_src/seed/types/DictKeyAsObjAttr.py


used as env/locals/globals for eval/exec/safe_eval
    view ../../python3_src/seed/helper/safe_eval.py
used in:
    ##view ../../python3_src/seed/math/GaussInteger.py
    view ../../python3_src/seed/math/right_angled_triangle_infos__sorted_by.py
        safe_eval(output_fmt, locals=record_env)




seed.types.ObjAttrAsDictKey
py -m nn_ns.app.debug_cmd   seed.types.ObjAttrAsDictKey -x
py -m nn_ns.app.doctest_cmd seed.types.ObjAttrAsDictKey:__doc__ -ff -v
py_adhoc_call   seed.types.ObjAttrAsDictKey   @f


>>> from seed.tiny import kwargs2Attrs
>>> obj = kwargs2Attrs(a=222, b=999)
>>> env = ObjAsEnv__readonly(obj)
>>> eval('(a,b)', env)
Traceback (most recent call last):
    ...
TypeError: globals must be a real dict; try eval(expr, {}, mapping)
>>> eval('(a,b)', {}, env)
(222, 999)
>>> eval('(a:=b)', {}, env)
Traceback (most recent call last):
    ...
KeyError: 'a'
>>> obj
namespace(a=222, b=999)
>>> env = ObjAsEnv__mutable(obj)
>>> eval('(a,b)', env)
Traceback (most recent call last):
    ...
TypeError: globals must be a real dict; try eval(expr, {}, mapping)
>>> eval('(a,b)', {}, env)
(222, 999)
>>> obj
namespace(a=222, b=999)
>>> eval('(a:=b)', {}, env)
999
>>> obj
namespace(a=999, b=999)
>>> eval('(a,b)', {}, env)
(999, 999)


>>> obj = kwargs2Attrs(a=222, b=999)
>>> env = ObjAsEnv__readonly_dict(obj)
>>> eval('(a,b)', env)
(222, 999)
>>> eval('(a:=b)', env)
Traceback (most recent call last):
    ...
KeyError: 'a'
>>> obj
namespace(a=222, b=999)
>>> env = ObjAsEnv__mutable_dict(obj)
>>> eval('(a,b)', env)
(222, 999)
>>> obj
namespace(a=222, b=999)
>>> eval('(a:=b)', env)
999
>>> obj
namespace(a=999, b=999)
>>> eval('(a,b)', env)
(999, 999)


>>> obj = kwargs2Attrs(a=222, b=999)
>>> env = ObjAsEnv__readonly_dict(obj)
>>> eval('(a,b)', env)
(222, 999)
>>> eval('(a:=b)', env)
Traceback (most recent call last):
    ...
KeyError: 'a'
>>> obj
namespace(a=222, b=999)
>>> env = ObjAsEnv__mutable_dict(obj)
>>> eval('(a,b)', env)
(222, 999)
>>> obj
namespace(a=222, b=999)
>>> eval('(a:=b)', env)
999


#]]]'''
__all__ = r'''
BaseAttrAsKey
    AttrAsKey__mutable      ObjAsEnv__mutable
    AttrAsKey__readonly     ObjAsEnv__readonly
    BaseAttrAsKey__dict
        AttrAsKey__mutable_dict     ObjAsEnv__mutable_dict
        AttrAsKey__readonly_dict    ObjAsEnv__readonly_dict
'''.split()#'''
__all__


#]]]'''
__all__ = r'''
BaseAttrAsKey
    AttrAsKey__mutable      ObjAsEnv__mutable
    AttrAsKey__readonly     ObjAsEnv__readonly
    BaseAttrAsKey__dict
        AttrAsKey__mutable_dict     ObjAsEnv__mutable_dict
        AttrAsKey__readonly_dict    ObjAsEnv__readonly_dict
'''.split()#'''
__all__

class BaseAttrAsKey:#(dict):
    def __init__(sf, obj, /):
        sf.obj = obj
    def __delitem__(sf, nm, /):
        raise KeyError(nm)
    def __contains__(sf, nm, /):
        raise KeyError(nm)
    def __getitem__(sf, nm, /):
        raise KeyError(nm)
    def __setitem__(sf, nm, v, /):
        raise KeyError(nm)
class BaseAttrAsKey__dict(BaseAttrAsKey, dict): pass
class AttrAsKey__mutable(BaseAttrAsKey):
    def __delitem__(sf, nm, /):
        try:
            return delattr(sf.obj, nm)
        except AttributeError:
            pass
        raise KeyError(nm)
    def __contains__(sf, nm, /):
        return hasattr(sf.obj, nm)
    def __getitem__(sf, nm, /):
        try:
            return getattr(sf.obj, nm)
        except AttributeError:
            pass
        raise KeyError(nm)
    def __setitem__(sf, nm, v, /):
        try:
            return setattr(sf.obj, nm, v)
        except AttributeError:
            pass
        raise KeyError(nm)
class AttrAsKey__readonly(BaseAttrAsKey):
    __contains__ = AttrAsKey__mutable.__contains__
    __getitem__ = AttrAsKey__mutable.__getitem__

class AttrAsKey__mutable_dict(AttrAsKey__mutable, BaseAttrAsKey__dict): pass
class AttrAsKey__readonly_dict(AttrAsKey__readonly, BaseAttrAsKey__dict): pass

ObjAsEnv__readonly = AttrAsKey__readonly
ObjAsEnv__mutable = AttrAsKey__mutable
ObjAsEnv__readonly_dict = AttrAsKey__readonly_dict
ObjAsEnv__mutable_dict = AttrAsKey__mutable_dict

__all__


from seed.types.ObjAttrAsDictKey import ObjAsEnv__readonly_dict, ObjAsEnv__mutable_dict
from seed.types.ObjAttrAsDictKey import ObjAsEnv__readonly, ObjAsEnv__mutable
from seed.types.ObjAttrAsDictKey import *
