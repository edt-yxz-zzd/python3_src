

# functools.reduce(function, iterable[, initializer]) 

r'''
key:
    keys = map_if(key, iterable)
key2start:
    key0, keys = head_ex(keys)
    start = call_if(key2start, key0)
func: # bin_op
    func(lhs, rhs)
foldl: # left
    lhs = func(lhs, rhs)
    start = func(start, key_)
    for key_ in keys:
        start = func(start, key_)

maybe X = () | (X,)
minmax is nonefficient.
'''

__all__ = '''
    map_if call_if
    maybe_foldl1 foldl0
    curry

    lmin2 rmin2 lmax2 rmax2
    
    maybe_lmin1 maybe_lmax1 maybe_rmin1 maybe_rmax1
    lmin0 lmax0 rmin0 rmax0
    
    maybe_lminlmax1 maybe_lminrmax1 maybe_rminlmax1 maybe_rminrmax1
    lminlmax0 lminrmax0 rminlmax0 rminrmax0

    min0 max0 minmax0
    maybe_min maybe_max maybe_minmax
'''.split()
from .map_if import map_if



def call_if(func, x):
    'func can be None; take one arg'
    if func is None:
        return x
    return func(x)

def maybe_foldl1(func, iterable, *, key=None, key2start=None):
    '''return a tuple of len < 2;

keys = map(key, iterable)
start = key2start(keys[0]); some times start and key are of different types
'''
    value2key = key; del key
    keys = map_if(value2key, iterable); del iterable
    for key0 in keys:
        #start = call_if(key, start)
        start = call_if(key2start, key0)
        break
    else:
        return ()
    return (foldl0(func, start, keys, key=None),) # None !!!!!!!

def foldl0(func, start, iterable, *, key=None):
    'foldl f x ls'
    for x in map_if(key, iterable):
        start = func(start, x)
    return start

class curry:
    def __init__(self, func, arg0):
        self.func = func
        self.arg0 = arg0
    def __call__(self, *args, **kwargs):
        # what if 'self' in kwargs??
        return self.func(self.arg0, *args, **kwargs)
    

class curry_maybe_foldl1:
    def __init__(self, func):
        self.func = func
    def __call__(self, iterable, *, key=None, key2start=None):
        return maybe_foldl1(self.func, iterable, key=key, key2start=key2start)
class curry_foldl0:
    def __init__(self, func):
        self.func = func
    def __call__(self, start, iterable, *, key=None):
        return foldl0(self.func, start, iterable, key=key)




def lmin2(lhs, rhs):
    'left first; lhs if lhs <= rhs else rhs'
    if lhs is rhs:
        return lhs
    if rhs < lhs:
        return rhs
    return lhs
def rmin2(lhs, rhs):
    'right first; lhs if lhs < rhs else rhs'
    return lmin2(rhs, lhs)

def lmax2(lhs, rhs):
    'left first; lhs if lhs >= rhs else rhs'
    # lhs if not lhs < rhs else rhs
    # rhs if lhs < rhs else lhs

    if lhs is rhs:
        return lhs
    if lhs < rhs:
        return rhs
    return lhs
def rmax2(lhs, rhs):
    'right first; lhs if lhs > rhs else rhs'
    return lmax2(rhs, lhs)

class minmax2:
    def __init__(self, min2_max2):
        'min2_max2 - pair of bin_op'
        self.min2_max2 = min2_max2
    def __call__(self, min_max, rhs):
        'min_max - pair of lhs-value'
        min2, max2 = self.min2_max2
        min, max = min_max
        return min2(min, rhs), max2(max, rhs)

#def lminlmax2(min_max, x):
    
# fail !! : assert () is not ()
*a, = (1,)
assert a == [1]
del a

def _test_XmXX2():
    eq_args = ([], [])
    lt_args = (0, 1)
    *ids, = map(id, eq_args)
    func__eq_idx__lt_value__ls = [
        [lmin2, 0, 0],
        [rmin2, 1, 0],
        [lmax2, 0, 1],
        [rmax2, 1, 1],
        ]
    
    for func, eq_idx, lt_value in func__eq_idx__lt_value__ls:
        x = func(*eq_args)
        assert ids.index(id(x)) == eq_idx

        x = func(*lt_args)
        assert x == lt_value
_test_XmXX2()
    
maybe_lmin1 = curry_maybe_foldl1(lmin2)
lmin0 = curry_foldl0(lmin2)
maybe_lmax1 = curry_maybe_foldl1(lmax2)
lmax0 = curry_foldl0(lmax2)

maybe_rmin1 = curry_maybe_foldl1(rmin2)
rmin0 = curry_foldl0(rmin2)
maybe_rmax1 = curry_maybe_foldl1(rmax2)
rmax0 = curry_foldl0(rmax2)

def _test_maybe_XmXX1__XmXX0():
    fmt1 = 'maybe_{pre}{func}1'
    fmt0 = '{pre}{func}0'
    def get_func(fmt, pre, func):
        return globals()[fmt.format(pre=pre, func=func)]
    pres = 'lr'
    funcs = ['min', 'max']
    def get(pre, func):
        return get_func(fmt, pre, func)

    def get_id1(ls):
        x, = get(pre, func)(ls)
        return find_id(ls, x)
    def get_id0(ls):
        start = ls[0]
        x = get(pre, func)(start, ls)
        if x is start:
            return 0
        return find_id(ls, x)
    
    def find_id(ls, obj):
        #print(ls, obj)
        *ls, = map(id, ls)
        return ls.index(id(obj))
    
    eqs = [[] for _ in range(5)]
    *lts, = range(5)
    for fmt, get_id in [(fmt1, get_id1), (fmt0, get_id0)]:
        for pre in pres:
            for func in funcs:
                idx = get_id(eqs)
                assert idx == 0 if pre == 'l' else len(eqs) - 1
                idx = get_id(lts)
                assert idx == 0 if func == 'min' else len(lts) - 1

    
    
                
_test_maybe_XmXX1__XmXX0()


class build_maybe_minmax1:
    def __init__(self, min2_max2):
        self.minmax2 = minmax2(min2_max2)
    def __call__(self, iterable, *, key=None, key2start=None):
        def _key2start(x):
            x = call_if(key2start, x)
            return (x, x) # (min, max)
        return maybe_foldl1(self.minmax2,
                            iterable, key=key, key2start=_key2start)
class build_minmax0:
    def __init__(self, min2_max2):
        self.minmax2 = minmax2(min2_max2)
    def __call__(self, start, iterable, *, key=None):
        start = (start, start)
        return foldl0(self.minmax2, start, iterable, key=key)
    
maybe_lminlmax1 = build_maybe_minmax1((lmin2, lmax2))
maybe_lminrmax1 = build_maybe_minmax1((lmin2, rmax2))
maybe_rminlmax1 = build_maybe_minmax1((rmin2, lmax2))
maybe_rminrmax1 = build_maybe_minmax1((rmin2, rmax2))
    
lminlmax0 = build_minmax0((lmin2, lmax2))
lminrmax0 = build_minmax0((lmin2, rmax2))
rminlmax0 = build_minmax0((rmin2, lmax2))
rminrmax0 = build_minmax0((rmin2, rmax2))


minmax0 = lminlmax0
maybe_minmax = maybe_lminlmax1
min0 = lmin0
max0 = lmax0
maybe_min = maybe_lmin1
maybe_max = maybe_lmax1


def _test_maybe_XminYmax1__XminYmax0():
    fmt1 = 'maybe_{pre0}min{pre1}max1'
    fmt0 = '{pre0}min{pre1}max0'
    def get_func(fmt, pre0, pre1):
        return globals()[fmt.format(pre0=pre0, pre1=pre1)]
    pres = 'lr'
    def get(pre0, pre1):
        return get_func(fmt, pre0, pre1)

    def get_id1(ls):
        x, = get(pre0, pre1)(ls)
        return find_id(ls, x)
    def get_id0(ls):
        start = ls[0]
        x = get(pre0, pre1)(start, ls)
        if x is start:
            return 0
        return find_id(ls, x)
    def find_id(ls, pair):
        #print(ls, obj)
        *ls, = map(id, ls)
        x, y = map(id, pair)
        return ls.index(x), ls.index(y)
    
    eqs = [[] for _ in range(5)]
    *lts, = range(5)
    try:
        for fmt, get_id in [(fmt1, get_id1), (fmt0, get_id0)]:
            for pre0 in pres:
                for pre1 in pres:
                    idcs = get_id(eqs)
                    for pre, func, idx in zip([pre0, pre1], ['min', 'max'], idcs):
                        assert idx == 0 if pre == 'l' else len(eqs) - 1
                        
                    idcs = get_id(lts)
                    for pre, func, idx in zip([pre0, pre1], ['min', 'max'], idcs):
                        assert idx == 0 if func == 'min' else len(lts) - 1

    except:
        print(dict((name, obj) for name, obj in locals().items()
                   if type(obj) is not type(get_id)))
        raise


    
    
                
_test_maybe_XminYmax1__XminYmax0()


