

__all__ = '''
    forbids
    allows
    '''.split()

#gs = set(globals().keys()) # to avoid 'pprint'
from pprint import pprint
#pprint(gs); print('\n'*3)
{'__annotations__',
 '__builtins__',
 '__cached__',
 '__doc__',
 '__file__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__'}


import builtins
assert builtins is __builtins__
assert not hasattr(builtins, '__all__')
# hence use 'dir' instead of __all__
bs = set(dir(builtins))
#pprint(bs); print('\n'*3)





def mk_subset_names(names, pred):
    # -> set name
    # pred :: obj -> bool
    return {name for name in names for obj in [getattr(builtins, name)] if pred(obj)}


__bs__ = {name for name in bs if name[:2] == '__' == name[-2:]}
bs_normal = bs - __bs__
if any(name[:1] == '_' or '_' == name[-1:] for name in bs_normal):
    raise logic-error
bs_types = mk_subset_names(bs_normal, lambda obj: isinstance(obj, type))
bs_excepts = mk_subset_names(bs_types, lambda obj: issubclass(obj, BaseException))
bs_nonexcepts = bs_types - bs_excepts

bs_nontypes = bs_normal - bs_types
bs_callables = mk_subset_names(bs_nontypes, callable)
bs_noncallables = bs_nontypes - bs_callables

def is_set_partition(whole, subsets):
    subsets = tuple(subsets)
    empty = whole - whole
    return len(whole) == sum(map(len, subsets)) and empty.union(*subsets) == whole
#assert bs == __bs__ | bs_excepts | bs_nonexcepts | bs_callables | bs_noncallables
assert is_set_partition(bs,
                [ __bs__
                , bs_excepts
                , bs_nonexcepts
                , bs_callables
                , bs_noncallables
                ])





def show__bs__():
    for name in __bs__:
        print(name)
        print('\t', getattr(builtins, name))
    '''
__debug__
         True
__loader__
         <class '_frozen_importlib.BuiltinImporter'>
__build_class__
         <built-in function __build_class__>
__doc__
         Built-in functions, exceptions, and other objects.

Noteworthy: None is the `nil' object; Ellipsis represents `...' in slices.
__name__
         builtins
__spec__
         ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)
__import__
         <built-in function __import__>
__package__
'''
#show__bs__()
#pprint(__bs__); print('\n'*3)
{'__build_class__', # remove
 '__debug__',
 '__doc__',
 '__import__',      # remove
 '__loader__',      # remove
 '__name__',
 '__package__',
 '__spec__'         # remove
 }
allow___bs__ = \
    {'__debug__'
    ,'__doc__'
    ,'__name__'
    ,'__package__'
    }
forbid___bs__ = \
    {'__build_class__'  # remove
    ,'__import__'       # remove
    ,'__loader__'       # remove
    ,'__spec__'         # remove
    }

def show_others():
    print('bs_nonexcepts'); pprint(bs_nonexcepts); print('\n'*3)
    print('bs_callables'); pprint(bs_callables); print('\n'*3)
    print('bs_noncallables'); pprint(bs_noncallables); print('\n'*3)
#show_others()
'''
bs_nonexcepts
{'bool',
 'bytearray',
 'bytes',
 'classmethod',
 'complex',
 'dict',
 'enumerate',
 'filter',
 'float',
 'frozenset',
 'int',
 'list',
 'map',
 'memoryview',
 'object',
 'property',
 'range',
 'reversed',
 'set',
 'slice',
 'staticmethod',
 'str',
 'super',
 'tuple',
 'type',
 'zip'}




bs_callables
{'abs',
 'all',
 'any',
 'ascii',
 'bin',
 'callable',
 'chr',
 'compile',     # remove
 'copyright',   # remove
 'credits',     # remove
 'delattr',     # remove
 'dir',
 'divmod',
 'eval',        # remove
 'exec',        # remove
 'exit',        # remove
 'format',
 'getattr',     # remove
 'globals',     # remove
 'hasattr',
 'hash',
 'help',        # remove
 'hex',
 'id',
 'input',       # remove
 'isinstance',
 'issubclass',
 'iter',
 'len',
 'license',     # remove
 'locals',      # remove
 'max',
 'min',
 'next',
 'oct',
 'open',        # remove
 'ord',
 'pow',
 'print',       # remove
 'quit',        # remove
 'repr',
 'round',
 'setattr',     # remove
 'sorted',
 'sum',
 'vars'}




bs_noncallables
{'None', 'True', 'False', 'Ellipsis', 'NotImplemented'}
'''

forbid_bs_callables = \
    {'compile'      # remove
    ,'copyright'    # remove
    ,'credits'      # remove
    ,'delattr'      # remove
    ,'eval'         # remove
    ,'exec'         # remove
    ,'exit'         # remove
    ,'getattr'      # remove
    ,'globals'      # remove
    ,'help'         # remove
    ,'input'        # remove
    ,'license'      # remove
    ,'locals'       # remove
    ,'open'         # remove
    ,'print'        # remove
    ,'quit'         # remove
    ,'setattr'      # remove
    }
allow_bs_callables = \
    {'abs'
    ,'all'
    ,'any'
    ,'ascii'
    ,'bin'
    ,'callable'
    ,'chr'
    ,'dir'
    ,'divmod'
    ,'format'
    ,'hasattr'
    ,'hash'
    ,'hex'
    ,'id'
    ,'isinstance'
    ,'issubclass'
    ,'iter'
    ,'len'
    ,'max'
    ,'min'
    ,'next'
    ,'oct'
    ,'ord'
    ,'pow'
    ,'repr'
    ,'round'
    ,'sorted'
    ,'sum'
    ,'vars'}

forbids = forbid___bs__ | forbid_bs_callables
allows = allow___bs__ | allow_bs_callables | bs_types | bs_noncallables
assert not (forbids & allows)
if not is_set_partition(bs, [forbids, allows]):
    unknown_new_names = (bs - forbids - allows)
    raise Exception(f'need to update constant variables "forbid_.*" and "allow_.*": {unknown_new_names}')




