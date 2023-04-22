

__all__ = r'''
    nmay5star_tmay_
    nmay5tmay_
    nmay2tmay_
'''.split()#'''


from seed.debug.expectError import expectError
from seed.tiny_.containers import null_tuple
from seed.tiny_.check import check_tmay, check_bool

def nmay5star_tmay_(*tmay_x, mix_ok=False):
    '(*tmay x) -> (mix_ok=False) -> may x | ^TypeError # [mix_ok or not x is None]'
    return nmay5tmay_(tmay_x, mix_ok=mix_ok)
def nmay5tmay_(tmay_x, /, *, mix_ok=False):
    'tmay x -> (mix_ok=False) -> may x | ^TypeError # [mix_ok or not x is None]'
    check_bool(mix_ok)
    check_tmay(tmay_x)

    if tmay_x:
        [x] = tmay_x
        if not (mix_ok or not x is None): raise TypeError('tmay None -> may None')
        may_x = x
    else:
        [] = tmay_x
        may_x = None
    may_x
    return may_x

def nmay2tmay_(may_x, /):
    'may x -> tmay x'
    if may_x is None:
        return null_tuple
    x = may_x
    return (x,)

assert expectError(TypeError, lambda:nmay5star_tmay_(None))
assert expectError(TypeError, lambda:nmay5star_tmay_(999, 777))
assert 999 == nmay5star_tmay_(999)
assert None is nmay5star_tmay_()
assert None is nmay5star_tmay_(None, mix_ok=True)

assert expectError(TypeError, lambda:nmay5tmay_((None,)))
assert expectError(TypeError, lambda:nmay5tmay_([999]))
assert expectError(TypeError, lambda:nmay5tmay_((999, 777)))
assert 999 == nmay5tmay_((999,))
assert None is nmay5tmay_(())
assert None is nmay5tmay_((None,), mix_ok=True)
assert () == nmay2tmay_(None)
assert (999,) == nmay2tmay_(999)

from seed.tiny_.nmay5tmay import nmay5star_tmay_, nmay5tmay_, nmay2tmay_
#def nmay5star_tmay_(*tmay_x, mix_ok=False):
#    '(*tmay x) -> (mix_ok=False) -> may x | ^TypeError # [mix_ok or not x is None]'
#def nmay5tmay_(tmay_x, /, *, mix_ok=False):
#    'tmay x -> (mix_ok=False) -> may x | ^TypeError # [mix_ok or not x is None]'
#def nmay2tmay_(may_x, /):
#    'may x -> tmay x'
from seed.tiny_.nmay5tmay import *
