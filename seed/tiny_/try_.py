

#from seed.tiny_.try_ import try_
#from seed.tiny_.mk_fdefault import mk_tmay_from_try_fvalue

def try_(f, /, *args, **kwds):
    '-> tmay result'
    try:
        r = f(*args, **kwds)
    except:
        tmay_r = ()
    else:
        tmay_r = (r,)
    return tmay_r

from seed.tiny_.try_ import try_

