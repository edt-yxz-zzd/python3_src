#__all__:goto
r'''[[[
e ../../python3_src/seed/helper/ask4bool.py
view ../../python3_src/seed/for_libs/raw_input.py

seed.helper.ask4bool
py -m nn_ns.app.debug_cmd   seed.helper.ask4bool -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.helper.ask4bool:__doc__ -ht # -ff -df
#######

[[
usage:
    --interactive:ask whether overwrite file

used in:
    view ../../python3_src/seed/helper/xforce.py
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.helper.ask4bool   @f
]]]'''#'''
__all__ = r'''
ask4bool_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.for_libs.raw_input import raw_input__echo
#.from itertools import islice
#.from seed.tiny_.check import check_type_is, check_int_ge
___end_mark_of_excluded_global_names__0___ = ...

_ans2ok = dict(no=False, yes=True, ok=True, n=False, y=True, false=False, true=True)
def ask4bool_(prompt, /):
    while 1:
        s = raw_input__echo(prompt)
        s = s.lower()
        if s in _ans2ok:
            return _ans2ok[s]



__all__
from seed.helper.ask4bool import ask4bool_
from seed.helper.ask4bool import *
