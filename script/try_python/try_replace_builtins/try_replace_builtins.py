
assert globals()['__builtins__'] is __builtins__
print(__builtins__)
old_list = list
old_builtins = __builtins__


class M:
    __builtins__ = {'list', tuple}
    assert list is old_list
    assert type([]) is old_list

#from seed.lang.has_no_nonlocals import getclosure
from inspect import getclosurevars
    # ClosureVars(nonlocals, globals, builtins, unbound)
from types import SimpleNamespace
def copy_as_namespace(obj):
    return SimpleNamespace(**{attr: getattr(obj, attr) for attr in dir(obj)})
__builtins__ = copy_as_namespace(__builtins__)
__builtins__.list = tuple
print(getclosurevars(lambda:[]))
assert list is old_list
assert type([]) is old_list


if 0:
    # fail!!!
    assert list is tuple
    assert type([]) is tuple
if 0:
    # fail!!!
    exec(r'''assert list is tuple''')

if 0:
    # fail!!!
    exec(r'''
assert list is tuple
assert type([]) is tuple
    '''
    , globals()
    )

old_builtins.list = tuple
assert list is tuple        # OK
assert type([]) is tuple    # fail

