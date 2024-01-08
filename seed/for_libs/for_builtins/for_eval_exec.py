r'''[[[
e ../../python3_src/seed/for_libs/for_builtins/for_eval_exec.py
view ../../python3_src/seed/types/ObjAttrAsDictKey.py

usage:
    eval(expr, {}, ObjAsEnv__readonly(env_obj))
    eval(expr, {}, ObjAsEnv__mutable(env_obj))
        # non-subclas-py.dict can be used as locals, but cannot be globals

    eval(expr, ObjAsEnv__readonly_dict(env_obj))
    eval(expr, ObjAsEnv__mutable_dict(env_obj))
        # subclas-py.dict can be used as locals/globals

#]]]'''#'''

from seed.types.ObjAttrAsDictKey import ObjAsEnv__readonly, ObjAsEnv__mutable
from seed.types.ObjAttrAsDictKey import ObjAsEnv__readonly_dict, ObjAsEnv__mutable_dict




from seed.for_libs.for_builtins.for_eval_exec import ObjAsEnv__readonly, ObjAsEnv__mutable
from seed.for_libs.for_builtins.for_eval_exec import ObjAsEnv__readonly_dict, ObjAsEnv__mutable_dict
from seed.for_libs.for_builtins.for_eval_exec import *
