

class A:
    def __init__(self, a):
        pass


class B:
    def __init__(self, a, b):
        pass


class C(A,B):pass
class D(B,A):pass

C(1)
#C(1,2) # TypeError: __init__() takes 2 positional arguments but 3 were given
#D(1) # TypeError: __init__() missing 1 required positional argument: 'b'
D(1,2)
##help(C) # __init__(self, a)
##help(D) # __init__(self, a, b)

assert super(C,C).__init__ is A.__init__
assert super(D,D).__init__ is B.__init__

assert C.__init__ is A.__init__


############### __new__ ###############
class E(tuple):pass


print(object.__new__)
print(C.__new__)
print(E.__new__)
##help(E) # __new__ no __init__
assert E.__new__ is super(E,E).__new__

class F(tuple):
    def __init__(self, *, a):
        pass

##help(F) # __init__ and tuple.__new__
#F(a=1) # TypeError: 'a' is an invalid keyword argument for this function
#F(1) # TypeError: 'int' object is not iterable ; calling tuple.__new__ first




import inspect


def using_inherited_init(type_):
    return is_inherited_attr(type_, '__init__')
def using_inherited_new(type_):
    return is_inherited_attr(type_, '__new__')

def using_object_init(type_):
    return is_object_attr(type_, '__init__')
def using_object_new(type_):
    return is_object_attr(type_, '__new__')

def is_object_attr(type_, attr):
    super_ = object
    return is_same_attr(type_, attr, super_)

def is_inherited_attr(type_, attr):
    super_ = type_ if type_ is object else super(type_, type_)
    return is_same_attr(type_, attr, super_)

def is_same_attr(type_, attr, super_):
    if type_ is super_:
        getattr(type_, attr) # check
        return True
    if not hasattr(super_, attr):
        return False
    return getattr(type_, attr) is getattr(super_, attr)

class TypeInit:
    __slots__ = ('type_',)
    def __init__(self, type_):
        self.type_ = type_
    def init(self, *args, **kwargs):
        type_ = self.type_
        obj = type_.__new__(*args, **kwargs)
        if type(obj) == type_:
            obj.__init__(*args, **kwargs)
        return obj

def get_type_init_or_new(type_):
    if not isinstance(type_, type):
        raise TypeError('not type')
    if using_object_init(type_):
        f = type_.__new__
    else:
        f = type_.__init__
    return f


def type_signature(type_):
    'fail for built-in type'
    return inspect.signature(type_)
def type_signature_code(type_):
    'fail ...'
    f = get_type_init_or_new(type_)

    # ValueError: no signature found for builtin function
    # inspect.signature(f)
    
    # AttributeError: 'builtin_function_or_method' object has no attribute '__code__'
    # f.__code__
    
    # AttributeError: 'builtin_function_or_method' object has no attribute '__func__'
    # f.__func__.__code__
    return f


c = type_signature_code(int)
print(c)
print(inspect.getmembers(c, lambda name: name=='__func__'))

class V:
    def __int__(self):
        print('__int__')
        raise ValueError()
    def __repr__(self):
        print('here')


print('ismethod', inspect.ismethod(c))
print('isfunction', inspect.isfunction(c))
try:
    # cannot get 'code' of int()
    int(V()) # cannot get the frame where int() exec
except:
    frames = inspect.trace()
    #frames = inspect.getinnerframes(tb, context=1)
    print(len(frames))
    for frame, *infos in frames:
        print(frame)
        print(infos)
        filename, lineno, function, code_context, index = inspect.getframeinfo(frame)
        print(function)

        print(frame.f_code)
        code = frame.f_code
        if 1:
            print(code.co_argcount, code.co_kwonlyargcount)
            vararg, varkw = (int(bool(code.co_flags & i)) for i in [4,8])
            n = code.co_argcount + code.co_kwonlyargcount + vararg + varkw
            print(code.co_varnames[:n])
        print('back', frame.f_back)








