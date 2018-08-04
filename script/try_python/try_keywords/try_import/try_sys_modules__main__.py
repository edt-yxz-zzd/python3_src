

'''
py -m xxx.yyy
__main__ and xxx.yyy are both refer to the same module

try cmd:
    pym try*__.py
    py -m nn_ns.try_python.try_import.try_sys_modules__main__
'''

#xxx print(__qualname__)
print(__name__)
assert __name__ == '__main__'

import importlib, sys
m = importlib.import_module(__name__)
for name, module in sys.modules.items():
    if m is module:
        print(name)
import nn_ns.try_python.try_import.try_sys_modules__main__ as m2
assert m2 is m



