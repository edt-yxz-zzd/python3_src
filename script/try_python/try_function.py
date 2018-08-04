
# type or __call__
# __code__, getmembers, signature

from inspect import getmembers, signature
from inspect import *
from operator import attrgetter

class T:
    def t(a,b,*af,g,**k):pass


def t1(sdfs,b,*af,g,**k):
    afsf = 11
    return afsf

t2 = lambda afsdf,b,*af,g,**k:3
fs = [T.t, t1, t2]
    
s1 = signature(t1) # may not exist for builtin funcs
for arg_name, info in s1.parameters.items():
    print(arg_name) # may be None if POSITIONAL_ONLY
    print(info.annotation, info.default) # Parameter.empty ==>> void
    print(info.kind, type(info.kind)) # POSITIONAL_ONLY...

if 0:
    ##ms = getmembers(t1)
    ##if 'sdfs' in str(ms):
    ##    print('here')
    c = t1.__code__
    get = attrgetter(*'co_name co_argcount co_consts co_nlocals co_names co_varnames'.split())
    for f in [t1, t2]:
        c = f.__code__
        ls = get(c)
        print(ls)



