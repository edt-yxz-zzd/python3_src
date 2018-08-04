
'''
1) ABC
    class XXX_ABC(metaclass=ABCMeta):...
        is too tedious and sometimes make error:
        class XXX_ABC(ABCMeta):...

    now, we have:
        class XXX_ABC(ABC):...

2) not_implemented
    class A:
        @abstractmethod
        def g(self):
            raise NotImplentedError # to prevent subclass call this method

        # we can use a decorator to redefined the function as above
        @not_implemented 
        def g(self):pass
        
'''
__all__ = '''
    ABC
    not_implemented
    
    ABCMeta
    abstractmethod
'''.split()
from abc import ABCMeta, abstractmethod
import functools
from inspect import signature, getattr_static
from collections import ChainMap
from types import FunctionType, CodeType

from _weakrefset import WeakSet
@abstractmethod
def _abstract():...
class PatchedABCMeta(ABCMeta):
    # to support class non-data decorator
    
    # patch ABCMeta.__new__
    #   begin new {...} end new
    def __new__(mcls, name, bases, namespace):
        cls = super(ABCMeta, mcls).__new__(mcls, name, bases, namespace)
        # Compute set of abstract method names
        abstracts = {name
                     for name, value in namespace.items()
                     if getattr(value, "__isabstractmethod__", False)}
        # old
##        for base in bases:
##            for name in getattr(base, "__abstractmethods__", set()):
##                value = getattr(cls, name, None)
##                if getattr(value, "__isabstractmethod__", False):
##                    abstracts.add(name)
        # begin new
        names = set().union(*(getattr(base, "__abstractmethods__", set()) for base in bases))
        names -= set(abstracts)
        if 0:
            d = ChainMap(*map(vars, cls.__mro__))
            for name in names:
                # get decorator first; then attr
                value = d.get(name, None)
                if not getattr(value, "__isabstractmethod__", False):
                    # get attr
                    if hasattr(value, "__get__"):
                        value = getattr(cls, name)
                if getattr(value, "__isabstractmethod__", False):
                    abstracts.add(name)
        else:
            for name in names:
                # get decorator first; then attr
                value = getattr_static(cls, name, None)
                if not getattr(value, "__isabstractmethod__", False):
                    # get attr
                    if hasattr(value, "__get__"):
                        value = getattr(cls, name)
                if getattr(value, "__isabstractmethod__", False):
                    abstracts.add(name)
            
        # end new
        
        cls.__abstractmethods__ = frozenset(abstracts)
        # Set up inheritance registry
        cls._abc_registry = WeakSet()
        cls._abc_cache = WeakSet()
        cls._abc_negative_cache = WeakSet()
        cls._abc_negative_cache_version = ABCMeta._abc_invalidation_counter
        return cls



class ABC(metaclass=PatchedABCMeta):
    __slots__ = ()


##def not_implemented(f):
##    @abstractmethod
##    @functools.wraps(f)
##    def _(self, *args, **kwargs):
##        raise NotImplemented
##    return _

def not_implemented(f):
    # f.__code__ = code which raise NotImplementedError and has same signature
    g = abstractmethod(func2not_implemented(f))
    # fail : assert g is f
    return g




def func2clean_signature_str(func) ->\
    'without __annotations__, __defaults__, __kwdefaults__':
        
    ## |  function(code, globals[, name[, argdefs[, closure]]])
    ## |  
    ## |  Create a function object from a code object and a dictionary.
    ## |  The optional name string overrides the name from the code object.
    ## |  The optional argdefs tuple specifies the default argument values.
    ## |  The optional closure tuple supplies the bindings for free variables.
    if 1:
        code = func.__code__
        closure = code.co_freevars
        try:
            _clean = FunctionType(code, {}, closure=func.__closure__)
        except:
            print(func.__closure__)
            raise
    else:
        # fail when func contains freevars:
        def _clean():
            # to provide a clean env to extract signature string
            # used by func2code_signature_str
            pass
        _clean.__code__ = func.__code__
    sig = signature(_clean)
    return str(sig)
assert func2clean_signature_str(func2clean_signature_str) == '(func)'
assert str(signature(func2clean_signature_str)) == \
       "(func) -> 'without __annotations__, __defaults__, __kwdefaults__'"


cache__sig_str2code = {}
#cache__not_implemented_codes = set()

def signature_str2not_implemented_func(sig_str):
    # func body should be in same line to ease debug
    # when raise, show up wrapped func signature
    #    require more : using old_code.co_lnotab
    #    otherwise: e.g. raise, show "@classmethod"
    src = 'def _{}: raise NotImplementedError'.format(sig_str)
    g = {}
    exec(src, g)
    return g['_']

def set_func_not_implemented(func):
    # func.__code__ should match func.__closure__
    # func.__closure__ is read-only
    raise
    #
    # namess = code2parameter_namess(func.__code__)
    sig_str = func2clean_signature_str(func)
    if sig_str not in cache__sig_str2code:
        code = signature_str2not_implemented_func(sig_str).__code__
        cache__sig_str2code[sig_str] = code # code really depends on sig_str
        #cache__not_implemented_codes.add(code)
        #print('cache__not_implemented_codes', len(cache__not_implemented_codes))
    else:
        code = cache__sig_str2code[sig_str]
    func.__code__, func.__closure__ = _replace_codestring(func.__code__, code)
    return None

def func2not_implemented(func):
    sig_str = func2clean_signature_str(func)
    if sig_str not in cache__sig_str2code:
        code = signature_str2not_implemented_func(sig_str).__code__
        cache__sig_str2code[sig_str] = code # code really depends on sig_str
        #cache__not_implemented_codes.add(code)
        #print('cache__not_implemented_codes', len(cache__not_implemented_codes))
    else:
        code = cache__sig_str2code[sig_str]
    code_without_freevars = _replace_codestring(func.__code__, code)
    new = FunctionType(code_without_freevars, globals())
    new.__dict__.update(vars(func))

    new.__defaults__ = func.__defaults__
    new.__kwdefaults__ = func.__kwdefaults__
    new.__doc__ = func.__doc__
    new.__name__ = func.__name__
    new.__qualname__ = func.__qualname__
    new.__module__ = func.__module__
    new.__annotations__ = func.__annotations__
    new.__dict__ = dict(func.__dict__)
    return new
    set_func_not_implemented(func)
    return func




def _replace_codestring(old_code, new_code):
    # new_code should have same clean signature as old_code
    
    ## |  code(argcount, kwonlyargcount, nlocals, stacksize, flags, codestring,
    ## |        constants, names, varnames, filename, name, firstlineno,
    ## |        lnotab[, freevars[, cellvars]])
    # codestring is co_code!!
    #from types import CodeType
    old_doc_new_const = old_code.co_consts[:1] + new_code.co_consts[1:]
    code = \
        CodeType(new_code.co_argcount,
                 new_code.co_kwonlyargcount,
                 new_code.co_nlocals,
                 new_code.co_stacksize,
                 new_code.co_flags,
                 new_code.co_code, # codestring,
                 old_doc_new_const, # new_code.co_constants,
                 new_code.co_names,
                 new_code.co_varnames,
                 old_code.co_filename,
                 old_code.co_name,
                 old_code.co_firstlineno,
                 old_code.co_lnotab,
                 new_code.co_freevars,
                 new_code.co_cellvars)
    return code


















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







