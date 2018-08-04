
from .InfoID_SRRTL import *

def toState(*args): return InfoDefineStateID(*args)
def toIf(ID, *args):
    return InfoDefineTypeID(ID, InfoDefineIfClause(*args))

def toNormal(ID, *args):
    assert ID
    return InfoDefineTypeID(ID, InfoNormalDefine(*args))
