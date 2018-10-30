

__all__ = '''
    all_decorated_by_if
    let_be_all_staticmethod
    '''.split()

from types import FunctionType

def is_FunctionType(obj):
    return isinstance(obj, FunctionType)
def all_decorated_by_if(pred, decorator):
    def class_decorator(cls):
        d = cls.__dict__
        for name, obj in list(d.items()):
            if pred(name, obj):
                #d[name] = decorator(obj)
                setattr(cls, name, decorator(obj))
        return cls
    return class_decorator
def let_be_all_staticmethod(prefix):
    if type(prefix) is not str: raise TypeError
    return all_decorated_by_if(
        lambda name, obj:name.startswith(prefix) and is_FunctionType(obj)
        , staticmethod
        )

