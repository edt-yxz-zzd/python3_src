

'''
require MRO_MetaBase
will update builtins.super
'''


__all__ = '''
    SuperSubCls
    SuperSubObj
    super
    __old_super__
    '''.split()
from ?? import MRO_MetaBase
import builtins


# super(cls, x)         # x in cls or x <= cls
super(type, type)       # type   in type;   type   <= type
#super(object, object)  # object in object; object <= object
super(type, object)     # object in type;   not (object <= type)
#super(object, type)    # type in object;   type <= object
super(int, bool)        # not (bool in int); bool <= int
super(int, 0)           # 0 in int;         not (0 <= int)
assert super(type, type).__eq__ is object.__eq__ is not None
assert super(type, type).__eq__(1,1)
#assert super(object, object).__eq__(1,1)
#assert super(object, type).__eq__(1,1) # object has no super
# so the second type is cls instead of obj
#   super(cls, first subcls then subobj)
assert super(type, object).__eq__(object) # the object is obj

# __self__, __self_class__, __thisclass__

class SuperSubCls(super):
    def __new__(T, cls, subcls):
        if subcls not in MRO_MetaBase: raise TypeError
        if not (subcls <= cls): raise TypeError
        self = super(__class__, T).__new__(T, cls, subcls)
        assert self.__self__ is subcls
        assert self.__self_class__ is subcls
        assert self.__thisclass__ is cls
        return self
    def __getattribute__(self, attr):
        raise AttributeError
class SuperSubObj(super):
    def __new__(T, cls, subobj):
        if type(subobj) not in MRO_MetaBase: raise TypeError
        if not isinstance(subobj, cls): raise TypeError
        self = super(__class__, T).__new__(T, cls, subobj)
        assert self.__self__ is subobj
        assert self.__self_class__ is type(subobj)
        assert self.__thisclass__ is cls
        return self
    def __getattribute__(self, attr):
        raise AttributeError


############################
__old_super__ = super
#def super(cls, subcls_or_subobj):
def super(*args):
    # super(cls, first subcls then subobj)
    o = __old_super__(*args) # RuntimeError: super(): no arguments
    raise
    cls = o.__thisclass__
    subcls_or_subobj = o.__self__
    subcls = o.__self_class__
    if subcls not in MRO_MetaBase: return o
    if args:
        x = __old_super__()
        if cls is not x.__thisclass__ or subcls is not x.__self_class__:
            raise TypeError('MRO_MetaBase only support super()')
    T = SuperSubCls if subcls is subcls_or_subobj else SuperSubObj
    return T(cls, subcls_or_subobj)

'''
def super(cls, subcls_or_subobj):
    # super(cls, first subcls then subobj)
    if issubclass(subcls_or_subobj, cls):
        subcls = subcls_or_subobj
        if subcls in MRO_MetaBase:
            return SuperSubCls(cls, subcls)
        return __old_super__(cls, subcls)
    elif isinstance(subcls_or_subobj, cls):
        subobj = subcls_or_subobj
        if type(subobj) in MRO_MetaBase:
            return SuperSubObj(cls, subobj)
        return __old_super__(cls, subobj)
    else:
        __old_super__(cls, subcls_or_subobj) # should raise here
        raise logic-error
'''

builtins.super = super

