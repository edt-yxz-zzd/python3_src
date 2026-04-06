
'''
usage:
    def sort(key=None):
        key = ifNone(key, echo)
'''
__all__ = 'ifNone  ifNonef'.split()

def ifNonef(obj, fdefault):
    if obj is None: return fdefault()
    return obj
def ifNone(obj, default):
    if obj is None: return default
    return obj

from seed.helper.ifNone import ifNone, ifNonef

