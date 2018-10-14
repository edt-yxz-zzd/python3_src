
__all__ = '''
    IReprImmutableHelper
    '''.split()

from .IReprHelper import IReprHelper
from .IImmutableHelper import IImmutableHelper

class IReprImmutableHelper(IReprHelper, IImmutableHelper):
    __slots__ = ()


