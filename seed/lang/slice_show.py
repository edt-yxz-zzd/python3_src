
#e ../../python3_src/seed/lang/slice_show.py

def _f(m, /):
    return '' if m is None else repr(m)
def show_slice_(sl, /):
    s = ':'.join(map(_f, [sl.start, sl.stop, sl.step]))
    if s[-1] == ':':
        s = s[:-1]
    return s
from seed.lang.slice_show import show_slice_


