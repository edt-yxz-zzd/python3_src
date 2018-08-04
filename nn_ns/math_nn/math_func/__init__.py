
_submodules = (\
    'math_func_of_float', 'math_func_of_int', 'math_func_of_vector', 'power',
    )

for _sub in _submodules:
    exec('from .{} import *'.format(_sub))

