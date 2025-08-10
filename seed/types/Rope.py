#__all__:goto
r'''[[[
e ../../python3_src/seed/types/Rope.py

seed.types.Rope
py -m nn_ns.app.debug_cmd   seed.types.Rope -x
py -m nn_ns.app.doctest_cmd seed.types.Rope:__doc__ -ht
py_adhoc_call   seed.types.Rope   @f



>>> Rope()
Rope()
>>> Rope() is null_rope
True
>>> len(Rope())
0
>>> Rope(1)
Traceback (most recent call last):
    ...
TypeError: <class 'int'>
>>> Rope([1])
Traceback (most recent call last):
    ...
TypeError: <class 'list'>
>>> Rope((1,))
Rope((1,))
>>> len(Rope((1,)))
1
>>> Rope((2,3))
Rope((2, 3))
>>> len(Rope((2,3)))
2
>>> Rope((4,5,6,7))
Rope((4, 5, 6, 7))
>>> Rope((1,), (), null_rope, Rope((2,3)), (4,5,6,7), Rope((8,),(9,)))
Rope((1,), (2, 3), (4, 5, 6, 7), Rope((8,), (9,)))
>>> len(Rope((1,), (), null_rope, Rope((2,3)), (4,5,6,7), Rope((8,),(9,))))
9
>>> [*iter(Rope((1,), (), null_rope, Rope((2,3)), (4,5,6,7), Rope((8,),(9,))))]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> [*reversed(Rope((1,), (), null_rope, Rope((2,3)), (4,5,6,7), Rope((8,),(9,))))]
[9, 8, 7, 6, 5, 4, 3, 2, 1]


>>> Rope((), (1,2), (3,))
Rope((1, 2), (3,))
>>> mk_Rope([(), (1,2), (3,)])
Rope((1, 2), (3,))



#]]]'''
__all__ = r'''
Rope
    null_rope
    mk_Rope
'''.split()#'''
__all__

#from seed.tiny_.check import check_type_is, check_int_ge
from seed.helper.repr_input import repr_helper
from seed.tiny_.containers import mk_tuple, null_tuple

class Rope:
    r'''[[[
    'accumulator for args of partial-func'
    node kinds:
        * leaf: nonempty_tuple
        * root{odeg==0}:null_rope
        * root{odeg==1}:rope(nonempty_tuple)
        * node{odeg>=2}:rope(nonempty_node, nonempty_node, ...)

    ]]]'''#'''
    _node_types4Rope_ = ('Rope', tuple)
    _leaf_types4Rope_ = (tuple,)
    def __repr__(sf, /):
        return repr_helper(sf, *sf._args)
    def __new__(cls, /, *ls_of__tpl_or_rope):
        return cls.from_iterable(ls_of__tpl_or_rope)
    @classmethod
    def from_iterable(cls, iter__tpl_or_rope, /):
        ls_of__tpl_or_rope = mk_tuple(iter__tpl_or_rope)
        if cls is __class__ and not any(ls_of__tpl_or_rope):
            try:
                return null_rope
            except NameError:
                pass
        for typ in map(type, ls_of__tpl_or_rope):
            if not typ in cls._node_types4Rope_:
                raise TypeError(typ)
        args = ls_of__tpl_or_rope
        #args = tuple(filter(bool, args)) if not all(args) else args
        ls = []
            # [(nonempty_tpl | rope_of_odeg_ge2)]
        changed = False
        for x in args:
            if not x:
                changed = True
                continue
            #nonempty_node
            #nonempty_tpl|rope_of_sz_ge1
            #nonempty_tpl|rope_of_odeg_ge1
            if type(x) in cls._leaf_types4Rope_:
                tpl = x
                ls.append(tpl)
                    #nonempty_tpl
                continue
            rope = x
            #rope_of_odeg_ge1
            odeg = rope.odeg
            if odeg == 1:
                changed = True
                [tpl] = rope._args
                if not type(tpl) in cls._leaf_types4Rope_: raise TypeError('logic-err')
                if not tpl:raise TypeError('logic-err')
                ls.append(tpl)
                    #nonempty_tpl
            else:
                assert odeg >= 2, rope
                assert len(rope) >= 2
                ls.append(rope)
                    #rope_of_odeg_ge2

        args = mk_tuple(ls) if changed else args
        if len(args) == 1 and type(args[0]) is cls:
            [sf] = args
            assert sf
        else:
            sf = super(__class__, cls).__new__(cls)
            sf._args = args
            sf._sz = sum(map(len, args))
            assert bool(sf._sz) == bool(args)
        if cls is __class__ and not args:
            if not sf is globals().setdefault('null_rope', sf):raise TypeError('logic-err')
            if not sf is cls():raise TypeError('logic-err')
        return sf
    @property
    def odeg(sf, /):
        return len(sf._args)
    def __len__(sf, /):
        return sf._sz
    def __iter__(sf, /):
        for x in sf._args:
            yield from x
    def __reversed__(sf, /):
        for x in reversed(sf._args):
            yield from reversed(x)

Rope._node_types4Rope_ = (Rope, tuple)
null_rope = Rope()
mk_Rope = Rope.from_iterable


__all__
from seed.types.Rope import Rope, null_rope, mk_Rope
from seed.types.Rope import *
