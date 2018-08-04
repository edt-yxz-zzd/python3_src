
'''
class XXX_ABC(metaclass=ABCMeta):...
    is too tedious and sometimes make error:
    class XXX_ABC(ABCMeta):...

now, we have:
    class XXX_ABC(ABC):...

TODO:
    class A:
        @not_implemented
        def g(self):pass
    help(A.g)
    
    Help on function g in module __main__:

    g(self, *args, **kwargs)

    how to print "g(self)" ??
'''
__all__ = '''
    ABC
    ABCMeta
    abstractmethod
    not_implemented
'''.split()
from abc import ABCMeta, abstractmethod
import functools

class ABC(metaclass=ABCMeta):pass
##def not_implemented(f):
##    @abstractmethod
##    @functools.wraps(f)
##    def _(self, *args, **kwargs):
##        raise NotImplemented
##    return _

def not_implemented(f):
    # f.__code__ = code which raise NotImplementedError and has same signature
    g = abstractmethod(func2not_implemented(f))
    assert g is f
    return g




STAR_ARGS_FLAG = 0x4
STAR_KWDS_FLAG = 0x8
def code2vars(code):
    return {name : getattr(code, name) for name in dir(code) if name.startswith('co_')}


#####################  version1 #########################

# should be in one line
#   when catched will show the wrapped func
def not_implemented_func(): raise NotImplementedError

def code2not_implemented_code(code):
    # from old code :
    #   co_argcount, co_flags[&0x4, &0x8], co_kwonlyargcount, co_varnames # arg names
    #   co_filename, co_firstlineno # debug
    #   co_consts[0] # doc
    #   co_name
    
    ## |  code(argcount, kwonlyargcount, nlocals, stacksize, flags, codestring,
    ## |        constants, names, varnames, filename, name, firstlineno,
    ## |        lnotab[, freevars[, cellvars]])
    # codestring is co_code!!
    from types import CodeType
    print(dir(type(code)))
    help(type(code).__new__)
    new_code = not_implemented_func.__code__
    old_code = code ; del code
    old_parameter_flags = old_code.co_flags & (STAR_ARGS_FLAG | STAR_KWDS_FLAG)
    assert new_code.co_flags & old_parameter_flags == 0

    assert old_code.co_consts
    assert new_code.co_consts
    old_doc_new_const = old_code.co_consts[:1] + new_code.co_consts[1:]
    code = \
        CodeType(old_code.co_argcount,
                 old_code.co_kwonlyargcount,
                 new_code.co_nlocals,
                 new_code.co_stacksize,
                 old_parameter_flags | new_code.co_flags, # co_flags,
                 new_code.co_code,
                 old_doc_new_const, # constants
                 new_code.co_names,
                 old_code.co_varnames,
                 old_code.co_filename,
                 old_code.co_name,
                 old_code.co_firstlineno,
                 new_code.co_lnotab,
                 new_code.co_freevars,
                 new_code.co_cellvars)
    return code

    # from modulefinder.py::replace_paths_in_code:
##        return types.CodeType(co.co_argcount, co.co_nlocals, co.co_stacksize,
##                         co.co_flags, co.co_code, tuple(consts), co.co_names,
##                         co.co_varnames, new_filename, co.co_name,
##                         co.co_firstlineno, co.co_lnotab,
##                         co.co_freevars, co.co_cellvars)

def func2not_implemented(func):
    from types import FunctionType
    code = func.__code__
    code = code2not_implemented_code(code)
    
    ## |  function(code, globals[, name[, argdefs[, closure]]])
    ## |  
    ## |  Create a function object from a code object and a dictionary.
    ## |  The optional name string overrides the name from the code object.
    ## |  The optional argdefs tuple specifies the default argument values.
    ## |  The optional closure tuple supplies the bindings for free variables.

    # constructor: no __kwdefaults__??
    new_func = FunctionType(code, func.__globals__, func.__name__,
                            func.__defaults__)
    new_func.__kwdefaults__ = func.__kwdefaults__
    return new_func








#####################  version2 #########################



def code2parameter_namess(code):
    args_begin = 0
    star_args_begin = args_end = args_begin + code.co_argcount
    kwds_begin = star_args_end = star_args_begin + bool(code.co_flags & STAR_ARGS_FLAG)
    star_kwds_begin = kwds_end = kwds_begin + code.co_kwonlyargcount
    num_parameters = star_kwds_end = star_kwds_begin + bool(code.co_flags & STAR_KWDS_FLAG)

    parameter_names = code.co_varnames[:num_parameters]
    rngs = ([args_begin, args_end], [star_args_begin, star_args_end],
            [kwds_begin, kwds_end], [star_kwds_begin, star_kwds_end])
    arg_names, star_arg_names, kwds_names, star_kwds_names = \
               (parameter_names[begin:end] for begin, end in rngs)
    pos_only_names = ()
    return pos_only_names, arg_names, star_arg_names, kwds_names, star_kwds_names
def parameter_namess2signature_str(namess):
    pos_only_names, arg_names, star_arg_names, kwds_names, star_kwds_names = namess
    ls = []
    pos_names = pos_only_names + arg_names
    if pos_names:
        ls.append(', '.join(pos_names))

    between_stars = star_arg_names + kwds_names
    if between_stars:
        ls.append('*')
        ls.append(', '.join(between_stars))
        
    if star_kwds_names:
        star_kwd, = star_kwds_names
        ls.append('**' + star_kwd)

    return '({})'.format(', '.join(ls))

def signature_str2not_implemented_func(sig_str):
    # func body should be in same line to ease debug
    # when raise, show up wrapped func signature
    src = 'def _{}: raise NotImplementedError'.format(sig_str)
    g = {}
    exec(src, g)
    return g['_']

#help(signature_str2not_implemented('(a=1, *, k=2)'))

def func2parameter_namess(func):
    from inspect import signature, Parameter
    params = list(signature(func).parameters.values())
    pos_only_names, pos_kwd_names, var_pos_names, kwd_only_names, var_kwd_names \
                    = ([] for _ in range(5))
    outputs = [pos_only_names, pos_kwd_names, var_pos_names,
               kwd_only_names, var_kwd_names]
    kinds = [Parameter.POSITIONAL_ONLY,
            Parameter.POSITIONAL_OR_KEYWORD,
            Parameter.VAR_POSITIONAL, 
            Parameter.KEYWORD_ONLY,
            Parameter.VAR_KEYWORD]

    while params:
        param = params[-1]
        if param.kind == kinds[-1]:
            outputs[-1].append(param.name)
            params.pop()
        else:
            kinds.pop()
            outputs.pop()
    return pos_only_names, pos_kwd_names, var_pos_names, kwd_only_names, var_kwd_names
            
def set_func_not_implemented(func):
    # namess = code2parameter_namess(func.__code__)
    namess = func2parameter_namess(func)
    sig_str = parameter_namess2signature_str(namess)
    new = signature_str2not_implemented_func(sig_str)
    func.__code__ = new.__code__
    return None
    new.__defaults__ = func.__defaults__
    new.__kwdefaults__ = func.__kwdefaults__
    new.__doc__ = func.__doc__
    new.__name__ = func.__name__
    new.__qualname__ = func.__qualname__
    new.__module__ = func.__module__
    new.__annotations__ = func.__annotations__
    new.__dict__ = dict(func.__dict__)
    return new

def func2not_implemented(func):
    set_func_not_implemented(func)
    return func
    



    

def test_func2not_implemented():
    def g(a=1, *, k=2):
        return 3
    
    h = func2not_implemented(g)
    fs = [lambda:h(), lambda:h(2)]
    for f in fs:
        try:
            f()
        except NotImplementedError as e:
            pass
        else: raise ...
    
    fs = [lambda:h(1,3), lambda:h(c=3)]
    for f in fs:
        try:
            f()
        except TypeError as e:
            pass
        else: raise ...

def _():
    
    class A:
        @not_implemented
        def g(self):pass

    nonlocal2 = 3
    def f(pos1, kw1, *args, kwdoy1, **kwds):
        var1 = 1
        var2 = ()
        nonlocal nonlocal2
        global glob3
        glob3 = ""
        raise NotImplemented
    import inspect
    from pprint import pprint
    print(f.__code__.co_code)
    
    pprint(code2vars(f.__code__))
    # from old code :
    #   co_argcount, co_flags[&0x4, &0x8], co_kwonlyargcount, co_varnames # arg names
    #   co_filename, co_firstlineno # debug
    #   co_consts[0] # doc

    from types import CodeType, MethodType, FunctionType
    help(CodeType)
## |  code(argcount, kwonlyargcount, nlocals, stacksize, flags, codestring,
## |        constants, names, varnames, filename, name, firstlineno,
## |        lnotab[, freevars[, cellvars]])
    help(MethodType)
    # method(function, instance)
    























def test_not_implemented():
    class C(ABC):
        @not_implemented
        def f(self):
            return 1
        try:
            f(1)
        except NotImplementedError:pass
        else: raise ...
    
    try:
        C()
    except TypeError:pass
    else:raise ...

    class D(C):
        def f(self):
            return super().f()
    f = D().f
    try:
        f()
    except NotImplementedError:pass
    else: raise ...



test_func2not_implemented()
test_not_implemented()







