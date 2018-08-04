
'''
version 2
apply_ver2([f1, f2...], *args, **kwargs)
appls = apply_ver2

version 1
all(map(callable, funcs))
print(list(map(abs, range(4)))) ==>> print . list . map abs range(4)
==>> dot(print, list, map, abs)(range(4))
    or apply(print, list, map, ..., abs, range(4))

example from _big_data_should_be_removed_.py:
def show_big_files_in_package(module, size=50*K,
                              *, print=pprint, relpath=True,
                              dict=dict):
    root = module2root(module)
    if relpath == True:
        rel = lambda path: os.path.relpath(path, root)
    else:
        rel = identity
    #apply(print, list, map, ..., rel, files_of_size_gt(size, root))
        
    path2rel_size = lambda path: (rel(path), get_file_size(path))
    apply(print, dict, map, ..., path2rel_size, files_of_size_gt(size, root))
'''

from seed.special_funcs import identity

__all__ = '''
    identity
    
    Dot
    dot
    
    apply
    appls
    
    ls_map pdot papp
'''.split()





class Dot(tuple):
    '''Dot([all, map])(callable, funcs) ::= all(map(callable, funcs))'''
    __slots__ = ()
    @staticmethod
    #@abstractmethod
    def _IsMutable__is_mutable():
        # return False if all base classes are immutable
        #                 and have plain __init__
        return False
    
    def __new__(cls, funcs):
        if isinstance(funcs, cls) \
           and not funcs._IsMutable__is_mutable():
            self = funcs
            return self
        
        funcs = list(funcs)
        funcs.reverse()
        if not all(map(callable, funcs)):
            raise TypeError('all(map(callable, funcs))')
        self = super(__class__, cls).__new__(cls, funcs)
        return self
    
    def __call__(self, *args, **kwargs):
        #print(args, kwargs)
        funcs = iter(self)
        for f in funcs:
            break
        else:
            f = identity
        r = f(*args, **kwargs)
        for f in funcs:
            r = f(r)
        return r

    def __str__(self):
        return '{!s}([{!s}])'.format(type(self).__name__,
                                     ', '.join(f.__name__ for f in self))
    def __repr__(self):
        return '{!s}({!s})'.format(type(self).__name__, tuple.__repr__(self))
    
def dot(*funcs):
    '''dot(all, map)(callable, funcs) ::= all(map(callable, funcs))'''
    return Dot(funcs)
    
def apply(*funcs_ellipsis_args, **kwargs):
    'apply(all, map, ..., callable, funcs) ::= all(map(callable, funcs))'
    
    ls = []
    funcs_ellipsis = args = iter(funcs_ellipsis_args)
    for f in funcs_ellipsis:
        if f is ...:
            break
        ls.append(f)
    #print(ls)
    return Dot(ls)(*args, **kwargs)

ls_map = dot(list, map)
assert str(ls_map) == 'Dot([map, list])'
assert repr(ls_map) == "Dot((<class 'map'>, <class 'list'>))"


def pdot(*funcs):
    'dot(print, *funcs)'
    return dot(print, *funcs)

def papp(*funcs_ellipsis_args, **kwargs):
    'apply(print, *funcs_ellipsis_args, **kwargs)'
    return apply(print, *funcs_ellipsis_args, **kwargs)


def appls(funcs, *args, **kwargs):
    return Dot(funcs)(*args, **kwargs)




