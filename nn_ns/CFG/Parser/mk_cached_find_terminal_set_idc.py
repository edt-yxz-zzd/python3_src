
__all__ = '''
    CachedFindTerminalSetIdc
    mk_cached_find_terminal_set_idc
    '''.split()
from weakref import WeakKeyDictionary

def _t():
    d = WeakKeyDictionary()
    d[[]] = 1
    assert not d
try:
    _t()
    #TypeError: cannot create weak reference to 'list' object
    #int/str/...
except TypeError:
    pass
else:
    raise logic-error --python-updated
del _t



class CachedFindTerminalSetIdc:
    '''
since some object donot support weakref
    , now I requires cfg::CFG to determine
        the unique terminal_set_idx2terminal_set
'''
    def __init__(self, cfg, find_terminal_set_idc):
        self.find_terminal_set_idc = find_terminal_set_idc
        self.cfg = cfg
        self.cache = {}
    def __call__(self, terminal_set_idx2terminal_set, terminal_name):
        if terminal_set_idx2terminal_set is not self.cfg.terminal_set_idx2terminal_set:
            raise ValueError('not the same terminal_set_idx2terminal_set')
        cache = self.cache
        try:
            return cache[terminal_name]
        except KeyError:
            idc = cache[terminal_name] = self.find_terminal_set_idc(
                terminal_set_idx2terminal_set, terminal_name)
            return idc




class CachedFindTerminalSetIdc__ver1:
    def __init__(self, find_terminal_set_idc):
        self.find_terminal_set_idc = find_terminal_set_idc
        self.array2cache = WeakKeyDictionary()
    def __call__(self, terminal_set_idx2terminal_set, terminal_name):
        cache = self.array2cache.setdefault(terminal_set_idx2terminal_set, {})
        may_idc = cache.get(terminal_name)
        if may_idc is None:
            idc = self.find_terminal_set_idc(terminal_set_idx2terminal_set, terminal_name)
            cache[terminal_name] = tuple(idc)
        else:
            idc = may_idc
        return idc

mk_cached_find_terminal_set_idc = CachedFindTerminalSetIdc


