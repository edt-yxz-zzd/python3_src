
#from seed.types.ABC import *
#from seed.meta.ABC import *
__all__ = '''
    ABC
    not_implemented
'''.split()

from functools import wraps
from abc import abstractmethod, ABC #, ABCMeta


ABC = ABC
    # orinial seed.types.ABC.ABC
    #   fetch data-property instead of cls member object
#not_implemented = abstractmethod
    # v.s. orinial seed.types.ABC.not_implemented
    #   replace the method body by "raise NotImplementedError"

def not_implemented(func):
    @abstractmethod
    @wraps(func)
    def f(*args, **kwargs):
        raise NotImplementedError
    return f



