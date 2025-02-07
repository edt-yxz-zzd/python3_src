#__all__:goto
r'''[[[
e ../../python3_src/seed/iters/generator_iterator2result_.py
    functional
view ../../python3_src/seed/iters/generator_iterator_capturer.py
    class

seed.iters.generator_iterator2result_
py -m nn_ns.app.debug_cmd   seed.iters.generator_iterator2result_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.iters.generator_iterator2result_:__doc__ -ht # -ff -df

[[
]]

>>> def f(x, /):
...     return x; yield
>>> generator_iterator2result_(gi:=f(999))
999
>>> None is generator_iterator2result_(gi)
True
>>> generator_iterator2result_([])
Traceback (most recent call last):
    ...
TypeError: 'list' object is not an iterator

]]]'''#'''
__all__ = r'''
generator_iterator2result_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
___end_mark_of_excluded_global_names__0___ = ...

def generator_iterator2result_(gi, /):
    'Iterator -> StopIteration.value # [only the input generator_iterator not yet stopped][hence second call will get None]'
    try:
        while 1:
            next(gi)
    except StopIteration as e:
        return e.value
        return

__all__
from seed.iters.generator_iterator2result_ import generator_iterator2result_
from seed.iters.generator_iterator2result_ import *
