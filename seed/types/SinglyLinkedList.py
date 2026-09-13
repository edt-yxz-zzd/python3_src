#__all__:goto
r'''[[[
e ../../python3_src/seed/types/SinglyLinkedList.py
see:
    view ../../python3_src/seed/data_funcs/lnkls.py
    view ../../python3_src/seed/types/pair_based_leftward_list.py
    view ../../python3_src/seed/data_funcs/finger_tree/ft23_7sized_seq.py
    view ../../python3_src/seed/types/linked_list.py
        DoublyLinkedList

seed.types.SinglyLinkedList
py -m nn_ns.app.debug_cmd   seed.types.SinglyLinkedList -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.types.SinglyLinkedList:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>> import pickle


>>> type(mk_lflnkls7force_([])) is SinglyLinkedList7LeftPush
True
>>> mk_lflnkls7force_([]) is mk_lflnkls7force_()
True
>>> mk_lflnkls7force_()
mk_lflnkls7force_()
>>> mk_lflnkls7force_([1])
mk_lflnkls7force_([1])
>>> mk_lflnkls7force_([1, 2])
mk_lflnkls7force_([1, 2])
>>> mk_lflnkls7force_([1, 2, 3])
mk_lflnkls7force_([1, 2, 3])
>>> mk_lflnkls7force_([1, 2, 3], mk_lflnkls7force_([4, 5]))
mk_lflnkls7force_([1, 2, 3, 4, 5])
>>> class A(SinglyLinkedList7LeftPush):pass
>>> A()
A()
>>> A(1, A(2, A()))
A([1, 2], False)
>>> A([1, 2, 3], False)
A([1, 2, 3], False)
>>> A([1, 2, 3], True)
A([3, 2, 1], False)
>>> mk_lflnkls7force_([1, 2, 3], A())
A([1, 2, 3], False)
>>> mk_lflnkls7force_(A, [1, 2, 3])
A([1, 2, 3], False)
>>> mk_lflnkls7force_(A)
A()


>>> a = mk_lflnkls7force_(A, [1, 2, 3])
>>> a.head
1
>>> a.tail
A([2, 3], False)
>>> a.to_list_()
[1, 2, 3]
>>> a.to_reversed_list_()
[3, 2, 1]


>>> a.ir_pushL_(0)
(A([0, 1, 2, 3], False), None)
>>> a.ir_popL_()
(A([2, 3], False), 1)
>>> a.oo_pushL_(0)
A([0, 1, 2, 3], False)
>>> a.oo_popL_()
A([2, 3], False)


stack_ops:
    ir_push_
    ir_pop_
    oo_push_
    oo_pop_
    low6_
    top6_
    __bool__
    is_empty_
    mk7empty_
    mk5iter7up_
    mk5iter7down7force_
    ir_pushs5iter7up_
    ir_pushs5iter7down7force_
    oo_pushs5iter7up_
    oo_pushs5iter7down7force_
    iter_ir_pops_
    iter7down_
    iter7up7force_
    list_ir_pops_
    list7down_
    list7up_
>>> a.ir_push_(0)
(A([0, 1, 2, 3], False), None)
>>> a.ir_pop_()
(A([2, 3], False), 1)
>>> a.oo_push_(0)
A([0, 1, 2, 3], False)
>>> a.oo_pop_()
A([2, 3], False)
>>> a.low6_()
A([2, 3], False)
>>> a.top6_()
1
>>> A().top6_()
Traceback (most recent call last):
    ...
seed.types.SinglyLinkedList.EmptyError: empty
>>> bool(a)
True
>>> bool(A())
False
>>> a.is_empty_()
False
>>> A().is_empty_()
True
>>> A.mk7empty_()
A()
>>> A.mk5iter7down7force_([1, 2, 3])
A([1, 2, 3], False)
>>> A.mk5iter7up_([1, 2, 3])
A([3, 2, 1], False)
>>> a.list_ir_pops_()
[(A([2, 3], False), 1), (A([3], False), 2), (A(), 3)]
>>> [*a.iter7down_()]
[1, 2, 3]
>>> [*a.iter7up7force_()]
[3, 2, 1]
>>> a.list7down_()
[1, 2, 3]
>>> a.list7up_()
[3, 2, 1]
>>> a.ir_pushs5iter7up_([4, 5])
(A([5, 4, 1, 2, 3], False), 2)
>>> a.ir_pushs5iter7down7force_([4, 5])
(A([4, 5, 1, 2, 3], False), 2)
>>> a.oo_pushs5iter7up_([4, 5])
A([5, 4, 1, 2, 3], False)
>>> a.oo_pushs5iter7down7force_([4, 5])
A([4, 5, 1, 2, 3], False)


    ir_push_
    ir_pop_
    oo_push_
    oo_pop_
    low6_
    top6_
    is_empty_
    mk7empty_
    mk5iter7up_
    ir_pushs5iter7up_
    oo_pushs5iter7up_
    iter_ir_pops_
    iter7down_
    list_ir_pops_
    list7down_
    list7up_
>>> ir_push_(a, 0)
(A([0, 1, 2, 3], False), None)
>>> ir_pop_(a)
(A([2, 3], False), 1)
>>> oo_push_(a, 0)
A([0, 1, 2, 3], False)
>>> oo_pop_(a)
A([2, 3], False)
>>> low6_(a)
A([2, 3], False)
>>> top6_(a)
1
>>> top6_(A())
Traceback (most recent call last):
    ...
seed.types.SinglyLinkedList.EmptyError: empty
>>> is_empty_(a)
False
>>> is_empty_(A())
True
>>> mk7empty_(A)
A()
>>> mk5iter7up_(A, [1, 2, 3], force_reverse=True)
A([1, 2, 3], False)
>>> mk5iter7up_(A, [1, 2, 3])
A([3, 2, 1], False)
>>> list_ir_pops_(a)
[(A([2, 3], False), 1), (A([3], False), 2), (A(), 3)]
>>> list_ir_pops_(a, reverse=True)
[(A(), 3), (A([3], False), 2), (A([2, 3], False), 1)]
>>> [*iter7down_(a)]
[1, 2, 3]
>>> [*iter7down_(a, force_reverse=True)]
[3, 2, 1]
>>> [*iter7down_(a, with_low=True)]
[(A([2, 3], False), 1), (A([3], False), 2), (A(), 3)]
>>> list7down_(a)
[1, 2, 3]
>>> list7down_(a, reverse=True)
[3, 2, 1]
>>> list7down_(a, with_low=True)
[(A([2, 3], False), 1), (A([3], False), 2), (A(), 3)]
>>> list7up_(a)
[3, 2, 1]
>>> list7up_(a, reverse=True)
[1, 2, 3]
>>> list7up_(a, with_low=True)
[(A(), 3), (A([3], False), 2), (A([2, 3], False), 1)]
>>> ir_pushs5iter7up_(a, [4, 5], force_reverse=True)
(A([4, 5, 1, 2, 3], False), 2)
>>> ir_pushs5iter7up_(a, [4, 5])
(A([5, 4, 1, 2, 3], False), 2)
>>> oo_pushs5iter7up_(a, [4, 5])
A([5, 4, 1, 2, 3], False)
>>> oo_pushs5iter7up_(a, [4, 5], force_reverse=True)
A([4, 5, 1, 2, 3], False)



    mk5iter7down7force_
    ir_pushs5iter7down7force_
    oo_pushs5iter7down7force_
    iter7up7force_
>>> mk5iter7down7force_(A, [1, 2, 3])
A([1, 2, 3], False)
>>> mk5iter7down7force_(A, [1, 2, 3], reverse=True)
A([3, 2, 1], False)
>>> ir_pushs5iter7down7force_(a, [4, 5])
(A([4, 5, 1, 2, 3], False), 2)
>>> ir_pushs5iter7down7force_(a, [4, 5], reverse=True)
(A([5, 4, 1, 2, 3], False), 2)
>>> oo_pushs5iter7down7force_(a, [4, 5], reverse=True)
A([5, 4, 1, 2, 3], False)
>>> oo_pushs5iter7down7force_(a, [4, 5])
A([4, 5, 1, 2, 3], False)
>>> [*iter7up7force_(a)]
[3, 2, 1]
>>> [*iter7up7force_(a, reverse=True)]
[1, 2, 3]
>>> [*iter7up7force_(a, with_low=True)]
[(A(), 3), (A([3], False), 2), (A([2, 3], False), 1)]



    len7count_
    ir_reverse7force_
    oo_reverse7force_
    fold7down_
    fold7up7force_
    fmap7force_
    fmap7reverse_
>>> len7count_(a)
3
>>> ir_reverse7force_(a)
(A([3, 2, 1], False), None)
>>> oo_reverse7force_(a)
A([3, 2, 1], False)
>>> oo_reverse7force_(a, reverse=True) is a
True
>>> fold7down_(a, lambda st,x:f'{st}:{x}', '#')
'#:1:2:3'
>>> fold7up7force_(a, lambda st,x:f'{st}:{x}', '#')
'#:3:2:1'
>>> fmap7force_(a, lambda x:f'{x}')
A(['1', '2', '3'], False)
>>> fmap7reverse_(a, lambda x:f'{x}')
A(['3', '2', '1'], False)





>>> bs = pickle.dumps(a)
Traceback (most recent call last):
    ...
_pickle.PicklingError: Can't pickle <class 'seed.types.SinglyLinkedList.A'>: attribute lookup A on seed.types.SinglyLinkedList failed
>>> a = mk_lflnkls7force_(SinglyLinkedList7LeftPush, [1, 2, 3])
>>> bs = pickle.dumps(a)
>>> bs
b'\x80\x04\x95X\x00\x00\x00\x00\x00\x00\x00\x8c\x1bseed.types.SinglyLinkedList\x94\x8c\x19SinglyLinkedList7LeftPush\x94\x93\x94K\x01h\x02K\x02h\x02K\x03h\x02)\x81\x94\x86\x94\x81\x94\x86\x94\x81\x94\x86\x94\x81\x94.'
>>> _a = pickle.loads(bs)
>>> _a == a
True
>>> _a
mk_lflnkls7force_([1, 2, 3])










>>> type(mk_rglnkls_([])) is SinglyLinkedList7RightPush
True
>>> mk_rglnkls_([]) is mk_rglnkls_()
True
>>> mk_rglnkls_()
mk_rglnkls_()
>>> mk_rglnkls_([1])
mk_rglnkls_([1])
>>> mk_rglnkls_([1, 2])
mk_rglnkls_([1, 2])
>>> mk_rglnkls_([1, 2, 3])
mk_rglnkls_([1, 2, 3])
>>> mk_rglnkls_(mk_rglnkls_([1, 2, 3]), [4, 5])
mk_rglnkls_([1, 2, 3, 4, 5])
>>> class B(SinglyLinkedList7RightPush):pass
>>> B()
B()
>>> B(B(B(), 1), 2)
B(False, [1, 2])
>>> B(False, [1, 2, 3])
B(False, [1, 2, 3])
>>> B(True, [1, 2, 3])
B(False, [3, 2, 1])
>>> mk_rglnkls_(B(), [1, 2, 3])
B(False, [1, 2, 3])
>>> mk_rglnkls_(B, [1, 2, 3])
B(False, [1, 2, 3])
>>> mk_rglnkls_(B)
B()


>>> b = mk_rglnkls_(B, [1, 2, 3])
>>> b.lead
B(False, [1, 2])
>>> b.last
3
>>> b.to_list_()
[1, 2, 3]
>>> b.to_reversed_list_()
[3, 2, 1]

>>> b.ir_pushR_(0)
(B(False, [1, 2, 3, 0]), None)
>>> b.ir_popR_()
(B(False, [1, 2]), 3)
>>> b.oo_pushR_(0)
B(False, [1, 2, 3, 0])
>>> b.oo_popR_()
B(False, [1, 2])



stack_ops:
    ir_push_
    ir_pop_
    oo_push_
    oo_pop_
    low6_
    top6_
    __bool__
    is_empty_
    mk7empty_
    mk5iter7up_
    mk5iter7down7force_
    ir_pushs5iter7up_
    ir_pushs5iter7down7force_
    oo_pushs5iter7up_
    oo_pushs5iter7down7force_
    iter_ir_pops_
    iter7down_
    iter7up7force_
    list_ir_pops_
    list7down_
    list7up_
>>> b.ir_push_(0)
(B(False, [1, 2, 3, 0]), None)
>>> b.ir_pop_()
(B(False, [1, 2]), 3)
>>> b.oo_push_(0)
B(False, [1, 2, 3, 0])
>>> b.oo_pop_()
B(False, [1, 2])
>>> b.low6_()
B(False, [1, 2])
>>> b.top6_()
3
>>> B().top6_()
Traceback (most recent call last):
    ...
seed.types.SinglyLinkedList.EmptyError: empty
>>> bool(b)
True
>>> bool(B())
False
>>> b.is_empty_()
False
>>> B().is_empty_()
True
>>> B.mk7empty_()
B()
>>> B.mk5iter7down7force_([1, 2, 3])
B(False, [3, 2, 1])
>>> B.mk5iter7up_([1, 2, 3])
B(False, [1, 2, 3])
>>> b.list_ir_pops_()
[(B(False, [1, 2]), 3), (B(False, [1]), 2), (B(), 1)]
>>> [*b.iter7down_()]
[3, 2, 1]
>>> [*b.iter7up7force_()]
[1, 2, 3]
>>> b.list7down_()
[3, 2, 1]
>>> b.list7up_()
[1, 2, 3]
>>> b.ir_pushs5iter7up_([4, 5])
(B(False, [1, 2, 3, 4, 5]), 2)
>>> b.ir_pushs5iter7down7force_([4, 5])
(B(False, [1, 2, 3, 5, 4]), 2)
>>> b.oo_pushs5iter7up_([4, 5])
B(False, [1, 2, 3, 4, 5])
>>> b.oo_pushs5iter7down7force_([4, 5])
B(False, [1, 2, 3, 5, 4])



    ir_push_
    ir_pop_
    oo_push_
    oo_pop_
    low6_
    top6_
    is_empty_
    mk7empty_
    mk5iter7up_
    ir_pushs5iter7up_
    oo_pushs5iter7up_
    iter_ir_pops_
    iter7down_
    list_ir_pops_
    list7down_
    list7up_
>>> ir_push_(b, 0)
(B(False, [1, 2, 3, 0]), None)
>>> ir_pop_(b)
(B(False, [1, 2]), 3)
>>> oo_push_(b, 0)
B(False, [1, 2, 3, 0])
>>> oo_pop_(b)
B(False, [1, 2])
>>> low6_(b)
B(False, [1, 2])
>>> top6_(b)
3
>>> top6_(B())
Traceback (most recent call last):
    ...
seed.types.SinglyLinkedList.EmptyError: empty
>>> is_empty_(b)
False
>>> is_empty_(B())
True
>>> mk7empty_(B)
B()
>>> mk5iter7up_(B, [1, 2, 3], force_reverse=True)
B(False, [3, 2, 1])
>>> mk5iter7up_(B, [1, 2, 3])
B(False, [1, 2, 3])
>>> list_ir_pops_(b)
[(B(False, [1, 2]), 3), (B(False, [1]), 2), (B(), 1)]
>>> list_ir_pops_(b, reverse=True)
[(B(), 1), (B(False, [1]), 2), (B(False, [1, 2]), 3)]
>>> [*iter7down_(b)]
[3, 2, 1]
>>> [*iter7down_(b, force_reverse=True)]
[1, 2, 3]
>>> [*iter7down_(b, with_low=True)]
[(B(False, [1, 2]), 3), (B(False, [1]), 2), (B(), 1)]
>>> list7down_(b)
[3, 2, 1]
>>> list7down_(b, reverse=True)
[1, 2, 3]
>>> list7down_(b, with_low=True)
[(B(False, [1, 2]), 3), (B(False, [1]), 2), (B(), 1)]
>>> list7up_(b)
[1, 2, 3]
>>> list7up_(b, reverse=True)
[3, 2, 1]
>>> list7up_(b, with_low=True)
[(B(), 1), (B(False, [1]), 2), (B(False, [1, 2]), 3)]
>>> ir_pushs5iter7up_(b, [4, 5])
(B(False, [1, 2, 3, 4, 5]), 2)
>>> oo_pushs5iter7up_(b, [4, 5])
B(False, [1, 2, 3, 4, 5])
>>> oo_pushs5iter7up_(b, [4, 5], force_reverse=True)
B(False, [1, 2, 3, 5, 4])




    mk5iter7down7force_
    ir_pushs5iter7down7force_
    oo_pushs5iter7down7force_
    iter7up7force_
>>> mk5iter7down7force_(B, [1, 2, 3])
B(False, [3, 2, 1])
>>> mk5iter7down7force_(B, [1, 2, 3], reverse=True)
B(False, [1, 2, 3])
>>> ir_pushs5iter7down7force_(b, [4, 5])
(B(False, [1, 2, 3, 5, 4]), 2)
>>> ir_pushs5iter7down7force_(b, [4, 5], reverse=True)
(B(False, [1, 2, 3, 4, 5]), 2)
>>> oo_pushs5iter7down7force_(b, [4, 5], reverse=True)
B(False, [1, 2, 3, 4, 5])
>>> oo_pushs5iter7down7force_(b, [4, 5])
B(False, [1, 2, 3, 5, 4])
>>> [*iter7up7force_(b)]
[1, 2, 3]
>>> [*iter7up7force_(b, reverse=True)]
[3, 2, 1]
>>> [*iter7up7force_(b, with_low=True)]
[(B(), 1), (B(False, [1]), 2), (B(False, [1, 2]), 3)]




    len7count_
    ir_reverse7force_
    oo_reverse7force_
    fold7down_
    fold7up7force_
    fmap7force_
    fmap7reverse_
>>> len7count_(b)
3
>>> ir_reverse7force_(b)
(B(False, [3, 2, 1]), None)
>>> oo_reverse7force_(b)
B(False, [3, 2, 1])
>>> oo_reverse7force_(b, reverse=True) is b
True
>>> fold7down_(b, lambda st,x:f'{st}:{x}', '#')
'#:3:2:1'
>>> fold7up7force_(b, lambda st,x:f'{st}:{x}', '#')
'#:1:2:3'
>>> fmap7force_(b, lambda x:f'{x}')
B(False, ['1', '2', '3'])
>>> fmap7reverse_(b, lambda x:f'{x}')
B(False, ['3', '2', '1'])






>>> bs = pickle.dumps(b)
Traceback (most recent call last):
    ...
_pickle.PicklingError: Can't pickle <class 'seed.types.SinglyLinkedList.B'>: attribute lookup B on seed.types.SinglyLinkedList failed
>>> b = mk_rglnkls_(SinglyLinkedList7RightPush, [1, 2, 3])
>>> bs = pickle.dumps(b)
>>> bs
b'\x80\x04\x95Y\x00\x00\x00\x00\x00\x00\x00\x8c\x1bseed.types.SinglyLinkedList\x94\x8c\x1aSinglyLinkedList7RightPush\x94\x93\x94h\x02h\x02h\x02)\x81\x94K\x01\x86\x94\x81\x94K\x02\x86\x94\x81\x94K\x03\x86\x94\x81\x94.'
>>> _b = pickle.loads(bs)
>>> _b == b
True
>>> _b
mk_rglnkls_([1, 2, 3])















py_adhoc_call   seed.types.SinglyLinkedList   @f
]]]'''#'''
__all__ = r'''
mk_lflnkls7force_
mk_rglnkls_

IStack7Immutable
    LPshLsy     SinglyLinkedList7LeftPush
    RPshLsy     SinglyLinkedList7RightPush

IStack7Immutable
    ir_push_
    ir_pop_
    oo_push_
    oo_pop_
    low6_
    top6_
    is_empty_
    mk7empty_
    mk5iter7up_
    ir_pushs5iter7up_
    oo_pushs5iter7up_
    iter7down_
    list7down_
    list7up_
    iter_ir_pops_
    list_ir_pops_

    mk5iter7down7force_
    ir_pushs5iter7down7force_
    oo_pushs5iter7down7force_
    iter7up7force_

    len7count_
    ir_reverse7force_
    oo_reverse7force_
    fold7down_
    fold7up7force_
    fmap7force_
    fmap7reverse_


EmptyError
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from abc import update_abstractmethods
    from seed.helper.repr_input import repr_helper, repr_helper__str
    from seed.seq_tools.force_reversed import force_reversed
    from seed.tiny_.check import check_type_is, check_non_ABC
    from seed.iters.fold import foldl0
#.#################################
___end_mark_of_excluded_global_names__0___ = ...











###############################
# head, tail
# lead, last #lead/lead/fore/front,last/last/aft/heel/back/rear/rearward
def _checkL(cls, x8head, xs8tail, /):
    check_type_is(cls, xs8tail)
def _checkR(cls, xs8lead, x8last, /):
    check_type_is(cls, xs8lead)
def _new(cls, args, L_vs_R, _checkX, _mk5xs, /):
    match (L_vs_R, args):
        case (False, (xs, bool() as reverse)):
            # L
            return _mk5xs(cls, xs, reverse=reverse)
        case (True, (bool() as force_reverse, xs)):
            # R
            return _mk5xs(cls, xs, force_reverse=force_reverse)
    match args:
        case (a, b):
            _checkX(cls, a, b)
        case ():
            pass
        case _:
            raise TypeError('[len(args) !<- {0,2}]', len(args))
    if not args:
        try:
            return vars(cls)['_null_lnkls']
        except KeyError:
            pass
    sf = tuple.__new__(cls, args)
    if not args:
        cls._null_lnkls = sf
        assert sf is vars(cls)['_null_lnkls']
        return cls()
    return sf
###############################





###############################
def _repr(sf, __class__, L_vs_R, _mk5xs, /):
    nm = _mk5xs.__name__
    ls = sf.to_list_()
    T = type(sf)
    if not T is __class__:
        #.return repr_helper__str(nm, T, ls)
        if not sf:
            return repr_helper(sf)
        if L_vs_R:
            # R
            return repr_helper(sf, False, ls)
        else:
            # L
            return repr_helper(sf, ls, False)
    if not sf:
        return repr_helper__str(nm)
    return repr_helper__str(nm, ls)
###############################











###############################
def mk_lflnkls7force_(xs_or_may_type=None, may_tail_or_xs=None, /, *, reverse=False):
    '((xs -> TL) | (xs{head} -> may tail/T -> T) | (may T/type -> xs -> T) | (may T/type -> T)) # [xs :: Iter x][T <: TL is SinglyLinkedList7LeftPush] #for delta4size:see:ir_pushs5iter7up_()'
    TL = SinglyLinkedList7LeftPush
    match (xs_or_may_type, may_tail_or_xs):
        case (None, may_xs):
            T = TL
            tail = T()
            xs = '' if None is may_xs else may_xs
        case (type() as T, may_xs):
            if not issubclass(T, TL):raise TypeError(T)
            tail = T()
            xs = '' if None is may_xs else may_xs
        case (xs, None):
            T = TL
            tail = T()
            iter(xs)
        case (xs, TL() as tail):
            T = type(tail)
            iter(xs)
        case (xs, may_tail):
            raise TypeError(may_tail)
    T, tail, xs
    rv_xs = force_reversed(xs) if not reverse else iter(xs)
    for x in rv_xs:
        tail = T(x, tail)
    return tail
###############################










###############################
def mk_rglnkls_(xs_or_lead_or_may_type=None, may_xs=None, /, *, force_reverse=False):
    '((xs -> TR) | (lead -> xs{last} -> TR) | (may T/type -> may xs -> TR) | (may T/type -> TR)) # [xs :: Iter x][T <: TR is SinglyLinkedList7RightPush] #for delta4size:see:ir_pushs5iter7up_()'
    TR = SinglyLinkedList7RightPush
    match (xs_or_lead_or_may_type, may_xs):
        case (None, may_xs):
            T = TR
            lead = T()
            xs = '' if None is may_xs else may_xs
        case (type() as T, may_xs):
            if not issubclass(T, TR):raise TypeError(T)
            lead = T()
            xs = '' if None is may_xs else may_xs
        case (xs, None):
            T = TR
            lead = T()
            iter(xs)
        case (TR() as lead, xs):
            T = type(lead)
            iter(xs)
        case (_lead, xs):
            raise TypeError(_lead, xs)
    T, lead, xs

    xs = force_reversed(xs) if force_reverse else iter(xs)
    for x in xs:
        lead = T(lead, x)
    return lead
###############################






###############################
class EmptyError(Exception):pass

class IStack7Immutable(ABC):
    __slots__ = ()
    ###########################
    #stack_ops:
    #IStack7Immutable:
    # "ir" - (I,result) # vivi:method(sf, *args)
    # "oo" - object-only
    ###########################
    #abstract:
    #   oo_push_,oo_pop_,top6_,__bool__,mk7empty_
    ###########################
    @abstractmethod
    def oo_push_(sf, x, /):
        'IStack7Immutable -> x -> IStack7Immutable'
        #return sf.ir_push_(x)[0]

    @abstractmethod
    def oo_pop_(sf, /):
        'IStack7Immutable -> IStack7Immutable | ^EmptyError'
        #.return sf.ir_pop_()[0]
    @abstractmethod
    def top6_(sf, /):
        'IStack7Immutable -> x|^EmptyError'
        #vs:low6_
        # ir_pop_ <==> top6_+oo_pop_/low6_
        #.return sf.ir_pop_()[1]

    @abstractmethod
    def __bool__(sf, /):
        'IStack7Immutable -> nonempty/bool'
        try:
            sf.top6_()
        except EmptyError:
            return False
        return True
    @classmethod
    @abstractmethod
    def mk7empty_(cls, /):
        'cls/type -> IStack7Immutable'
        #.return cls.mk5iter7up_()
        #.return cls()




    ###########################
    #concrete:
    ###########################
    #@abstractmethod
    def ir_push_(sf, x, /):
        'IStack7Immutable -> x -> (IStack7Immutable, None)'
        return (sf.oo_push_(x), None)
    #@abstractmethod
    def ir_pop_(sf, /):
        'IStack7Immutable -> (IStack7Immutable, x) | ^EmptyError'
        top = sf.top6_()
            # ^EmptyError
        ot = lows = sf.oo_pop_() # = sf.low6_()
        return (ot, top)
    #@abstractmethod
    def low6_(sf, /):
        'IStack7Immutable -> IStack7Immutable | ^EmptyError'
        #vs:top6_
        #.return sf.ir_pop_()[0]
        return sf.oo_pop_()
    #@abstractmethod
    def is_empty_(sf, /):
        'IStack7Immutable -> empty/bool'
        return not sf
    @classmethod
    #@abstractmethod
    def mk5iter7up_(cls, may_xs7up=None, /, *, force_reverse=False):
        'cls/type -> may (Iter x){top last} -> IStack7Immutable'
        return cls.mk7empty_().oo_pushs5iter7up_(may_xs7up, force_reverse=force_reverse)
    @classmethod
    #@abstractmethod
    def mk5iter7down7force_(cls, may_xs7down=None, /, *, reverse=False):
        'cls/type -> may (Iter x){top first} -> IStack7Immutable'
        return cls.mk5iter7up_(may_xs7down, force_reverse=not reverse)
    #@abstractmethod
    def oo_pushs5iter7up_(sf, may_xs7up=None, /, *, force_reverse=False):
        'IStack7Immutable -> may (Iter x){top last} -> IStack7Immutable'
        return sf.ir_pushs5iter7up_(may_xs7up, force_reverse=force_reverse)[0]
    #@abstractmethod
    def ir_pushs5iter7up_(sf, may_xs7up=None, /, *, force_reverse=False):
        'IStack7Immutable -> may (Iter x){top last} -> (IStack7Immutable, delta4size/uint)'
        xs7up = '' if None is may_xs7up else may_xs7up
        xs7up = force_reversed(xs7up) if force_reverse else iter(xs7up)
        sz = 0
        for sz, x in enumerate(xs7up, 1):
            sf = sf.oo_push_(x)
        return (sf, sz)
    #@abstractmethod
    def ir_pushs5iter7down7force_(sf, may_xs7down=None, /, *, reverse=False):
        'IStack7Immutable -> may (Iter x){top first} -> (IStack7Immutable, delta4size/uint)'
        return sf.ir_pushs5iter7up_(may_xs7down, force_reverse=not reverse)

    #@abstractmethod
    def oo_pushs5iter7down7force_(sf, may_xs7down=None, /, *, reverse=False):
        'IStack7Immutable -> may (Iter x){top first} -> IStack7Immutable'
        return sf.oo_pushs5iter7up_(may_xs7down, force_reverse=not reverse)
    #@abstractmethod
    def iter7down_(sf, /, *, with_low=False, force_reverse=False):
        'IStack7Immutable -> (Iter x){top first}'
        #.return map(snd, sf.iter_ir_pops_())
        if force_reverse:
            return reversed(sf.list7down_(with_low=with_low))
        pairs = sf.iter_ir_pops_()
        rs = pairs if with_low else (x for ot, x in pairs)
        if force_reverse:
            rs = force_reversed(rs)
        return rs
    #@abstractmethod
    def iter7up7force_(sf, /, *, with_low=False, reverse=False):
        'IStack7Immutable -> (Iter x){top last}'
        return sf.iter7down_(with_low=with_low, force_reverse=not reverse)
    #@abstractmethod
    def iter_ir_pops_(sf, /):
        'IStack7Immutable -> (Iter (IStack7Immutable, x)){top first}'
        #.return sf.iter7down_(sf, with_low=True)
        while sf:
            (sf, top) = ir = sf.ir_pop_()
            yield ir
        return
    #@abstractmethod
    def list_ir_pops_(sf, /, *, reverse=False):
        'IStack7Immutable -> [(IStack7Immutable, x)]{top first}'
        return sf.list7down_(with_low=True, reverse=reverse)
    #@abstractmethod
    def list7down_(sf, /, *, with_low=False, reverse=False):
        'IStack7Immutable -> [x]{top first}'
        ls = list(sf.iter7down_(with_low=with_low))
        if reverse:
            ls.reverse()
        return ls
    #@abstractmethod
    def list7up_(sf, /, *, with_low=False, reverse=False):
        'IStack7Immutable -> [x]{top last}'
        return sf.list7down_(with_low=with_low, reverse=not reverse)
    ###########################
    def len7count_(sf, /):
        'IStack7Immutable -> size/uint # O(size)'
        xs7down = sf.iter7down_()
        sz = 0
        for sz, _ in enumerate(xs7down, 1):pass
        return sz
    def ir_reverse7force_(sf, /, *, reverse=False):
        'IStack7Immutable -> (IStack7Immutable, None)'
        ot = sf.oo_reverse7force_(reverse=reverse)
        return (ot, None)
    def oo_reverse7force_(sf, /, *, reverse=False):
        'IStack7Immutable -> IStack7Immutable'
        if reverse:
            return sf
        ys7up = rv_ys7down = sf.iter7down_()
        return type(sf).mk5iter7up_(ys7up)

    def fold7down_(sf, merge_st_x_, st, /, *, force_reverse=False):
        'IStack7Immutable{x} -> (st->x->st) -> st -> st'
        xs7down = sf.iter7down_(force_reverse=force_reverse)
        return foldl0(merge_st_x_, st, xs7down)
    def fold7up7force_(sf, merge_st_x_, st, /, *, reverse=False):
        'IStack7Immutable{x} -> (st->x->st) -> st -> st'
        return sf.fold7down_(merge_st_x_, st, force_reverse=not reverse)
    def fmap7force_(sf, x2y_, /, *, reverse=False):
        'IStack7Immutable{x} -> (x->y) -> IStack7Immutable{y}'
        xs7up = sf.iter7down_(force_reverse=not reverse)
        ys7up = map(x2y_, xs7up)
        return type(sf).mk5iter7up_(ys7up)
    def fmap7reverse_(sf, x2y_, /, *, force_reverse=False):
        'IStack7Immutable{x} -> (x->y) -> reversed-IStack7Immutable{y}'
        return sf.fmap7force_(x2y_, reverse=not force_reverse)
    ###########################
###############################











###############################
class SinglyLinkedList7LeftPush(tuple, IStack7Immutable):
    '[lflnkls == ()|(head/x, tail/lflnkls)]'
    ___no_slots_ok___ = True
    #...using tuple method:
    #def __eq__(sf, /):
    #def __hash__(sf, /):
    #def __bool__(sf, /):
    #def __len__(sf, /):
    #def __iter__(sf, /):
    #def __reversed__(sf, /):
    def __getstate__(sf, /):
        #pickle
        return None
    def __getnewargs__(sf, /):
        #pickle
        if not sf:
            return ()
        (a, b) = sf
        return (a, b)
    def __new__(cls, /, *args):
        return _new(cls, args, False, _checkL, mk_lflnkls7force_)
    def iter_(sf, /, *, with_tail=False):
        return sf.iter7down_(with_low=with_tail)
    if 0b000:
      def iter_(sf, /, *, with_tail=False):
        while sf:
            (h, sf) = sf
            yield h if not with_tail else (sf, h)
                # vs:ir_pop_()
                # vivi:.method(sf, *args)
    def to_list_(sf, /, *, with_tail=False, reverse=False):
        return sf.list7down_(with_low=with_tail, reverse=reverse)
        ls = list(sf.iter_(with_tail=with_tail))
        if reverse:
            ls.reverse()
        return ls
    def to_reversed_list_(sf, /, *, with_tail=False, reverse=False):
        return sf.list7up_(with_low=with_tail, reverse=reverse)
        return sf.to_list_(with_tail=with_tail, reverse=not reverse)
    def __repr__(sf, /):
        return _repr(sf, __class__, False, mk_lflnkls7force_)
    @property
    def head(sf, /):
        if not sf:raise EmptyError('empty')
        return sf[0]
    @property
    def tail(sf, /):
        if not sf:raise EmptyError('empty')
        return sf[1]

    # "ir" - (I,result) # vivi:method(sf, *args)
    # "oo" - object-only
    def ir_pushL_(sf, x, /):
        ot = type(sf)(x, sf)
        return (ot, None)
    def ir_popL_(sf, /):
        if not sf:raise EmptyError('empty')
        (x, ot) = sf
        return (ot, x)
    def oo_pushL_(sf, x, /):
        return sf.ir_pushL_(x)[0]
    def oo_popL_(sf, /):
        return sf.ir_popL_()[0]
    ###########################
    #stack_ops:
    #IStack7Immutable:
    #ir_push_ = ir_pushL_
    if 0b0001:ir_pop_ = ir_popL_
    oo_push_ = oo_pushL_
    oo_pop_ = oo_popL_
    #__bool__ = object.__bool__
    #__bool__ = tuple.__bool__
        # ^AttributeError: type object 'tuple' has no attribute '__bool__'. Did you mean: '__doc__'?
    def __bool__(sf, /):
        return bool(len(sf))
    #is_empty_
    def top6_(sf, /):
        return sf.head
    @classmethod
    def mk7empty_(cls, /):
        return cls()
    ###########################
    if 0b000:
      @classmethod
      def mk5iter7up_(cls, may_xs7up=None, /, *, force_reverse=False):
        may_rv_xs = may_xs7up
        return mk_lflnkls7force_(cls, may_rv_xs, reverse=not force_reverse)
    #mk5iter7up_
    #mk5iter7down7force_
    if 0b000:
      def oo_pushs5iter7up_(sf, may_xs7up=None, /, *, force_reverse=False):
        may_rv_xs = may_xs7up
        tail = sf
        return mk_lflnkls7force_(may_rv_xs, tail, reverse=not force_reverse)
    #ir_pushs5iter7up_
    #ir_pushs5iter7down7force_
    #oo_pushs5iter7up_
    #oo_pushs5iter7down7force_
    if 0b000:
      def iter7down_(sf, /, *, with_low=False):
        return sf.iter_(with_tail=with_low)
    #iter_ir_pops_
    #iter7down_
    #list_ir_pops_
    #list7down_
    #list7up_
    ###########################
SinglyLinkedList7LeftPush.__new__.__doc__ = r'''[TL:=SinglyLinkedList7LeftPush]
* () -> TL
* head -> tail/TL -> TL
* Iter x -> reverse/bool -> TL
'''#'''
LPshLsy = SinglyLinkedList7LeftPush
###############################



















###############################
class SinglyLinkedList7RightPush(tuple, IStack7Immutable):
    '[rglnkls == ()|(lead/rglnkls, last/x)]'
    ___no_slots_ok___ = True
    #...using tuple method:
    #def __eq__(sf, /):
    #def __hash__(sf, /):
    #def __bool__(sf, /):
    #def __len__(sf, /):
    #def __iter__(sf, /):
    #def __reversed__(sf, /):
    def __getnewargs__(sf, /):
        #pickle
        if not sf:
            return ()
        (a, b) = sf
        return (a, b)
    def __new__(cls, /, *args):
        return _new(cls, args, True, _checkR, mk_rglnkls_)
    def reversed_(sf, /, *, with_lead=False):
        return sf.iter7down_(with_low=with_lead)
    if 0b000:
      def reversed_(sf, /, *, with_lead=False):
        while sf:
            (sf, t) = sf
            yield t if not with_lead else (sf, t)
                # vs:ir_pop_()
                # vivi:.method(sf, *args)
    def to_list_(sf, /, *, with_lead=False, reverse=False):
        return sf.list7up_(with_low=with_lead, reverse=reverse)
        return sf.to_reversed_list_(with_lead=with_lead, reverse=not reverse)
    def to_reversed_list_(sf, /, *, with_lead=False, reverse=False):
        return sf.list7down_(with_low=with_lead, reverse=reverse)
        ls = list(sf.reversed_(with_lead=with_lead))
        if reverse:
            ls.reverse()
        return ls
    def __repr__(sf, /):
        return _repr(sf, __class__, True, mk_rglnkls_)
    @property
    def lead(sf, /):
        if not sf:raise EmptyError('empty')
        return sf[0]
    @property
    def last(sf, /):
        if not sf:raise EmptyError('empty')
        return sf[1]

    # "ir" - (I,result) # vivi:method(sf, *args)
    # "oo" - object-only
    def ir_pushR_(sf, x, /):
        ot = type(sf)(sf, x)
        return (ot, None)
    def ir_popR_(sf, /):
        if not sf:raise EmptyError('empty')
        (ot, x) = sf
        return (ot, x)
    def oo_pushR_(sf, x, /):
        return sf.ir_pushR_(x)[0]
    def oo_popR_(sf, /):
        return sf.ir_popR_()[0]
    ###########################
    #stack_ops:
    #IStack7Immutable:
    #ir_push_ = ir_pushR_
    if 0b0001:ir_pop_ = ir_popR_
    oo_push_ = oo_pushR_
    oo_pop_ = oo_popR_
    #__bool__ = object.__bool__
    #__bool__ = tuple.__bool__
        # ^AttributeError: type object 'tuple' has no attribute '__bool__'. Did you mean: '__doc__'?
    def __bool__(sf, /):
        return bool(len(sf))
    #is_empty_
    def top6_(sf, /):
        return sf.last
    @classmethod
    def mk7empty_(cls, /):
        return cls()
    ###########################
    if 0b000:
      @classmethod
      def mk5iter7up_(cls, may_xs7up=None, /, *, force_reverse=False):
        may_xs = may_xs7up
        return mk_rglnkls_(cls, may_xs, force_reverse=force_reverse)
    #mk5iter7up_
    #mk5iter7down7force_
    if 0b000:
      def oo_pushs5iter7up_(sf, may_xs7up=None, /, *, force_reverse=False):
        may_xs = may_xs7up
        lead = sf
        return mk_rglnkls_(lead, may_xs, force_reverse=force_reverse)
    #ir_pushs5iter7up_
    #ir_pushs5iter7down7force_
    #oo_pushs5iter7up_
    #oo_pushs5iter7down7force_
    if 0b000:
      def iter7down_(sf, /, *, with_low=False):
        return sf.reversed_(with_lead=with_low)
    #iter_ir_pops_
    #iter7down_
    #list_ir_pops_
    #list7down_
    #list7up_
    ###########################
SinglyLinkedList7RightPush.__new__.__doc__ = r'''[TR:=SinglyLinkedList7RightPush]
* () -> TR
* lead/TR -> last -> TR
* force_reverse/bool -> Iter x -> TR
'''#'''
RPshLsy = SinglyLinkedList7RightPush
###############################




if 0b0000:
    update_abstractmethods(LPshLsy)
    update_abstractmethods(RPshLsy)

    check_non_ABC(LPshLsy)
    check_non_ABC(RPshLsy)




###############################
#stack_ops:
#   old:exclude: mk5iter7down7force_, ir_pushs5iter7down7force_, oo_pushs5iter7down7force_, iter7up7force_
#   no:__len__
###############################
# "ir" - (I,result) # vivi:method(sf, *args)
# "oo" - object-only
###############################
def ir_push_(sf, x, /):
    'IStack7Immutable -> x -> (IStack7Immutable, None)'
    return sf.ir_push_(x)
def ir_pop_(sf, /):
    'IStack7Immutable -> (IStack7Immutable, x) | ^EmptyError'
    return sf.ir_pop_()
def oo_push_(sf, x, /):
    'IStack7Immutable -> x -> IStack7Immutable'
    return sf.oo_push_(x)
def oo_pop_(sf, /):
    'IStack7Immutable -> IStack7Immutable | ^EmptyError'
    return sf.oo_pop_()
def low6_(sf, /):
    'IStack7Immutable -> IStack7Immutable | ^EmptyError'
    return sf.low6_()
def top6_(sf, /):
    'IStack7Immutable -> x|^EmptyError'
    return sf.top6_()
def is_empty_(sf, /):
    'IStack7Immutable -> empty/bool'
    return sf.is_empty_()
def mk7empty_(cls, /):
    'cls/type -> IStack7Immutable # [cls <: IStack7Immutable]'
    return cls.mk7empty_()
def mk5iter7up_(cls, may_xs7up=None, /, *, force_reverse=False):
    'cls/type -> may (Iter x){top last} -> IStack7Immutable # [cls <: IStack7Immutable]'
    return cls.mk5iter7up_(may_xs7up, force_reverse=force_reverse)
def ir_pushs5iter7up_(sf, may_xs7up=None, /, *, force_reverse=False):
    'IStack7Immutable -> may (Iter x){top last} -> (IStack7Immutable, delta4size/uint)'
    return sf.ir_pushs5iter7up_(may_xs7up, force_reverse=force_reverse)
def oo_pushs5iter7up_(sf, may_xs7up=None, /, *, force_reverse=False):
    'IStack7Immutable -> may (Iter x){top last} -> IStack7Immutable'
    return sf.oo_pushs5iter7up_(may_xs7up, force_reverse=force_reverse)
def iter7down_(sf, /, *, with_low=False, force_reverse=False):
    'IStack7Immutable -> (Iter x){top first}'
    return sf.iter7down_(with_low=with_low, force_reverse=force_reverse)
def iter_ir_pops_(sf, /):
    'IStack7Immutable -> (Iter (IStack7Immutable, x)){top first}'
    return sf.iter_ir_pops_()
def list_ir_pops_(sf, /, *, reverse=False):
    'IStack7Immutable -> [(IStack7Immutable, x)]{top first}'
    return sf.list_ir_pops_(reverse=reverse)
def list7down_(sf, /, *, with_low=False, reverse=False):
    'IStack7Immutable -> [x]{top first}'
    return sf.list7down_(with_low=with_low, reverse=reverse)
def list7up_(sf, /, *, with_low=False, reverse=False):
    'IStack7Immutable -> [x]{top last}'
    return sf.list7up_(with_low=with_low, reverse=reverse)

###############################
def mk5iter7down7force_(cls, may_xs7down=None, /, *, reverse=False):
    'cls/type -> may (Iter x){top first} -> IStack7Immutable # [cls <: IStack7Immutable]'
    return cls.mk5iter7down7force_(may_xs7down, reverse=reverse)
def ir_pushs5iter7down7force_(sf, may_xs7down=None, /, *, reverse=False):
    'IStack7Immutable -> may (Iter x){top first} -> (IStack7Immutable, delta4size/uint)'
    return sf.ir_pushs5iter7down7force_(may_xs7down, reverse=reverse)
def oo_pushs5iter7down7force_(sf, may_xs7down=None, /, *, reverse=False):
    'IStack7Immutable -> may (Iter x){top first} -> IStack7Immutable'
    return sf.oo_pushs5iter7down7force_(may_xs7down, reverse=reverse)
def iter7up7force_(sf, /, *, with_low=False, reverse=False):
    'IStack7Immutable -> (Iter x){top last}'
    return sf.iter7up7force_(with_low=with_low, reverse=reverse)
###############################
def len7count_(sf, /):
    'IStack7Immutable -> size/uint # O(size)'
    return sf.len7count_()
def ir_reverse7force_(sf, /, *, reverse=False):
    'IStack7Immutable -> (IStack7Immutable, None)'
    return sf.ir_reverse7force_(reverse=reverse)
def oo_reverse7force_(sf, /, *, reverse=False):
    'IStack7Immutable -> IStack7Immutable'
    return sf.oo_reverse7force_(reverse=reverse)

def fold7down_(sf, merge_st_x_, st, /, *, force_reverse=False):
    'IStack7Immutable{x} -> (st->x->st) -> st -> st'
    return sf.fold7down_(merge_st_x_, st, force_reverse=force_reverse)
def fold7up7force_(sf, merge_st_x_, st, /, *, reverse=False):
    'IStack7Immutable{x} -> (st->x->st) -> st -> st'
    return sf.fold7up7force_(merge_st_x_, st, reverse=reverse)
def fmap7force_(sf, x2y_, /, *, reverse=False):
    'IStack7Immutable{x} -> (x->y) -> IStack7Immutable{y}'
    return sf.fmap7force_(x2y_, reverse=reverse)
def fmap7reverse_(sf, x2y_, /, *, force_reverse=False):
    'IStack7Immutable{x} -> (x->y) -> reversed-IStack7Immutable{y}'
    return sf.fmap7reverse_(x2y_, force_reverse=force_reverse)

###############################







__all__
from seed.types.SinglyLinkedList import EmptyError
from seed.types.SinglyLinkedList import mk_lflnkls7force_, mk_rglnkls_
from seed.types.SinglyLinkedList import LPshLsy, RPshLsy
from seed.types.SinglyLinkedList import SinglyLinkedList7LeftPush, SinglyLinkedList7RightPush

from seed.types.SinglyLinkedList import IStack7Immutable
from seed.types.SinglyLinkedList import ir_push_, ir_pop_, oo_push_, oo_pop_, low6_, top6_, is_empty_, mk7empty_, mk5iter7up_, ir_pushs5iter7up_, oo_pushs5iter7up_, iter7down_, list7down_, list7up_, iter_ir_pops_, list_ir_pops_
from seed.types.SinglyLinkedList import mk5iter7down7force_, ir_pushs5iter7down7force_, oo_pushs5iter7down7force_, iter7up7force_
from seed.types.SinglyLinkedList import len7count_, ir_reverse7force_, oo_reverse7force_, fold7down_, fold7up7force_, fmap7force_, fmap7reverse_





from seed.types.SinglyLinkedList import *
