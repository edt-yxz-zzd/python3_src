
__all__ = '''
    let_be_all_staticmethods
    '''.split()
from types import FunctionType
from .all_decorated_by_if import all_decorated_by_if

def is_FunctionType(obj):
    return isinstance(obj, FunctionType)
def let_be_all_staticmethods(prefix):
    if type(prefix) is not str: raise TypeError
    return all_decorated_by_if(
        lambda name, obj:name.startswith(prefix) and is_FunctionType(obj)
        , staticmethod
        )
