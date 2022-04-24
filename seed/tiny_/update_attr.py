

__all__ = '''
    update_attr
    iupdate_attrs
    set_attrs
    fwd_call

    prepare4set_attrs
    '''.split()

from seed.helper.Echo import echo
from seed.mapping_tools.dict_op import subset_keys__immutable

def update_attr(obj, nm, f, /):
    old = getattr(obj, nm)
    new = f(old)
    setattr(obj, nm, new)

def iupdate_attrs(obj, nms, f, d, /):
    for nm in nms:
        old = getattr(obj, nm)
        new = f(old, d[nm])
        setattr(obj, nm, new)

def prepare4set_attrs(nms, d, may_nm2key__or__dropped_prefix, /):
    if may_nm2key__or__dropped_prefix is None:
        nm2key = echo
    elif type(may_nm2key__or__dropped_prefix) is str:
        dropped_prefix = may_nm2key__or__dropped_prefix
        def nm2key(nm, /):
            if not nm.startswith(dropped_prefix): raise ValueError('not {nm!r}.startswith({dropped_prefix!r))')
            key = nm[len(dropped_prefix)]
            return key
    elif callable(may_nm2key__or__dropped_prefix):
        nm2key = may_nm2key__or__dropped_prefix
    else:
        raise TypeError('may_nm2key__or__dropped_prefix should be None/str/callable: {may_nm2key__or__dropped_prefix!r}')
    nm2key


    for nm in nms:
        k = nm2key(nm)
        new = d[k]
        yield (nm, new)

def set_attrs(obj, nms, d, may_nm2key__or__dropped_prefix, /):
    r'''
    usage:
        def __init__(sf, x, y, /):
            set_attrs(sf, "_x _y".split(), locals(), '_')
    #'''
    iter_pairs = prepare4set_attrs(nms, d, may_nm2key__or__dropped_prefix)
    for nm, new in iter_pairs:
        setattr(obj, nm, new)

def fwd_call(f, kwds, locals_, /):
    'usage: fwd_call(f, "a b".split(), locals())'
    kwargs = subset_keys__immutable(locals_, kwds)
    return f(**kwargs)

from seed.tiny_.update_attr import update_attr, iupdate_attrs, set_attrs, prepare4set_attrs, fwd_call


