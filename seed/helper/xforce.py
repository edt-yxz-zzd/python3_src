#__all__:goto
r'''[[[
e ../../python3_src/seed/helper/xforce.py

seed.helper.xforce
py -m nn_ns.app.debug_cmd   seed.helper.xforce -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.helper.xforce:__doc__ -ht # -ff -df
#######

[[
used in:
    view script/clean_w3schools_pages.py
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.helper.xforce   @f
]]]'''#'''
__all__ = r'''
check_xforce_
explain_xforce_
b_skip5xforce_opath4file_
mk_xforce_
    RAISE
    FORCE
    SKIP
    INTERACTIVE

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.helper.ask4bool import ask4bool_
from seed.tiny_.check import check_type_is
from pathlib import Path
from seed.tiny_.check_path import check_file_path_, check_path_not_exists_
___end_mark_of_excluded_global_names__0___ = ...


_xforces = (False, True, ..., None)
RAISE = False
FORCE = True
SKIP = ...
INTERACTIVE = None
_xforces = (RAISE, FORCE, SKIP, INTERACTIVE)
def check_xforce_(xforce, /):
    'xforce/(may emay force) -> None|^TypeError'
    #if not xforce in _xforces: raise TypeError(type(xforce))
    if not any(xforce is x for x in _xforces): raise TypeError(type(xforce))

def explain_xforce_(xforce, /):
    'xforce/(may emay force) -> (b_raise, b_force, b_skip, b_interactive)|^TypeError'
    check_xforce_(xforce)
    (b_raise, b_force, b_skip, b_interactive) = [False]*4
    if xforce is RAISE:
        b_raise = True
    elif xforce is FORCE:
        b_force = True
    elif xforce is SKIP:
        b_skip = True
    elif xforce is INTERACTIVE:
        b_interactive = True
    else:
        raise 000
    return (b_raise, b_force, b_skip, b_interactive)

#def test_opath4file_against_xforce_(xforce, opath4file, /, *, fmt4prompt='?overwrite: {!r} (y/n)?'):
def b_skip5xforce_opath4file_(xforce, opath4file, /, *, fmt4prompt='?overwrite: {!r} (y/n)?'):
    'xforce/(may emay force) -> opath{file} -> bool|^TypeError'
    opath4file = Path(opath4file)
    #check_xforce_(xforce)
    (b_raise, b_force, b_skip, b_interactive) = explain_xforce_(xforce)
    if b_raise:
        check_path_not_exists_(opath4file)
        pass#b_skip = False
    elif not opath4file.exists():
        b_skip = False
    else:
        check_file_path_(opath4file)
        if b_force:
            pass#b_skip = False
        elif b_skip:
            pass#b_skip = True
        elif b_interactive:
            b_force = ask4bool_(fmt4prompt.format(opath4file))
            b_skip = not b_force
        else:
            raise 000
        b_skip
    b_skip
    return b_skip
def mk_xforce_(b_raise=False, b_force:bool=False, b_skip:bool=False, b_interactive:bool=False):
    '(b_raise, b_force, b_skip, b_interactive) -> xforce/(may emay force)|^TypeError'
    #check_may_([check_type_is, bool], b_raise)
    check_type_is(bool, b_raise)
    check_type_is(bool, b_force)
    check_type_is(bool, b_skip)
    check_type_is(bool, b_interactive)
    if not sum([b_raise, b_force, b_skip, b_interactive]) <= 1: raise TypeError('[b_raise, b_force, b_skip, b_interactive] SHALL BE exclusive')
    if b_force:
        xforce = FORCE
    elif b_skip:
        xforce = SKIP
    elif b_interactive:
        xforce = INTERACTIVE
    else:
        xforce = RAISE
    xforce
    return xforce




__all__
from seed.helper.xforce import check_xforce_, explain_xforce_, b_skip5xforce_opath4file_, mk_xforce_
from seed.helper.xforce import RAISE, FORCE, SKIP, INTERACTIVE
from seed.helper.xforce import *
