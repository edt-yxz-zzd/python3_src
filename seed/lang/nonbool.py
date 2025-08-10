#__all__:goto
r'''[[[
e ../../python3_src/seed/lang/nonbool.py

seed.lang.nonbool
py -m nn_ns.app.debug_cmd   seed.lang.nonbool -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.lang.nonbool:__doc__ -ht # -ff -df

[[
源起:
    view ../../python3_src/seed/iters/PeekableIterator.py

    def tmp_peek_iter(self):
        del self.__dq
            # but:assign self.__it after self.__dq, would del self.__it firstly too?
        self.__dq = NotImplemented
            # but:bool(NotImplemented) may be ok
        self.__dq = nonbool
]]

>>> nonbool
nonbool
>>> bool(nonbool)
Traceback (most recent call last):
    ...
Exception: bool(nonbool)



]]]'''#'''
__all__ = r'''
nonbool
Nonbool
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
___end_mark_of_excluded_global_names__0___ = ...


class Nonbool:
    __slots__ = ()
    def __repr__(sf, /):
        return 'nonbool'
    def __bool__(sf, /):
        raise Exception('bool(nonbool)')
nonbool = Nonbool()

__all__
from seed.lang.nonbool import nonbool
from seed.lang.nonbool import *
