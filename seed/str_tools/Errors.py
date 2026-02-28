
__all__ = r'''
BaseError
    Fail
    ParamError
'''.split()#'''

class BaseError(Exception):pass
class Fail(BaseError):pass
class ParamError(BaseError):pass

assert issubclass(Fail, Exception)
from seed.str_tools.Errors import BaseError, Fail, ParamError
