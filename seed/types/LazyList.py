#__all__:goto
r'''[[[
e ../../python3_src/seed/types/LazyList.py
see:
    view ../../python3_src/seed/iters/PeekableIterator.py
        PeekableIterator
    view ../../python3_src/seed/math/continued_fraction/continued_fraction_ops.py
        MutableLazySeq
        ImmutableLazySeq
            to_MutableLazySeq
            to_ImmutableLazySeq
        CachedIterator
        ContinuedFraction
    view ../../python3_src/seed/types/LazyList.py
        LazyList




seed.types.LazyList
py -m nn_ns.app.debug_cmd   seed.types.LazyList -x
py -m nn_ns.app.doctest_cmd seed.types.LazyList:__doc__ -ff -v
py_adhoc_call   seed.types.LazyList   @f





>>> from seed.types.LazyList import LazyList, LazyListError
>>> LazyList()
LazyList()
>>> LazyList(None)
LazyList()
>>> LazyList([])
Traceback (most recent call last):
    ...
TypeError: not iterator
>>> LazyList([], non_iterator_ok=True)
LazyList([<...>])


>>> null_lazylist = LazyList()
>>> _5 = LazyList(range(5), non_iterator_ok=True)
>>> null_lazylist
LazyList()
>>> _5
LazyList([<...>])
>>> null_lazylist.is_empty__hardwork()
True
>>> _5.is_empty__hardwork()
False
>>> _5
LazyList([0, <...>])

>>> _1 = LazyList(-1, null_lazylist)
>>> _6 = LazyList(-1, _5)
>>> _1
LazyList([-1])
>>> _6
LazyList([-1, 0, <...>])
>>> null_lazylist
LazyList()
>>> _5
LazyList([0, <...>])


#may_unpack__relax,may_unpack
>>> _5 = LazyList(range(5), non_iterator_ok=True)
>>> _5
LazyList([<...>])
>>> _5.may_unpack__relax()
Ellipsis
>>> _5
LazyList([<...>])
>>> _5.may_unpack()
(0, LazyList([<...>]))
>>> _5
LazyList([0, <...>])
>>> _5.may_unpack()
(0, LazyList([<...>]))
>>> _5
LazyList([0, <...>])
>>> _5.may_unpack__relax()
(0, LazyList([<...>]))
>>> _5
LazyList([0, <...>])
>>> _5.may_unpack() is _5.may_unpack() is _5.may_unpack__relax()
True
>>> _, _4 = _5.may_unpack()





>>> null_lazylist.extract_tmay_head()
()
>>> _5.extract_tmay_head()
(0,)

>>> null_lazylist.extract_tmay_tail()
()
>>> _5.extract_tmay_tail() == (_4,)
True



>>> null_lazylist.unpack_or_raise()
Traceback (most recent call last):
    ...
seed.types.LazyList.LazyListError__unpack_empty_lazylist
>>> _5.unpack_or_raise() == (0, _4)
True

>>> null_lazylist.extract_head_or_raise()
Traceback (most recent call last):
    ...
seed.types.LazyList.LazyListError__unpack_empty_lazylist
>>> _5.extract_head_or_raise()
0

>>> null_lazylist.extract_tail_or_raise()
Traceback (most recent call last):
    ...
seed.types.LazyList.LazyListError__unpack_empty_lazylist
>>> _5.extract_tail_or_raise() is _4
True




>>> _5
LazyList([0, <...>])
>>> _4
LazyList([<...>])
>>> null_lazylist
LazyList()

# relax
>>> [*_5.iter__relax()]
[0]
>>> [*_4.iter__relax()]
[]
>>> [*null_lazylist.iter__relax()]
[]
>>> [*_5.iter__relax(with_end_state=True)]
[0, Ellipsis]
>>> [*_4.iter__relax(with_end_state=True)]
[Ellipsis]
>>> [*null_lazylist.iter__relax(with_end_state=True)]
[None]
>>> [*_5.iter__relax(with_tail=True)] == [0, (Ellipsis, _4)]
True
>>> [*_5.iter__relax(with_tail=True)]
[0, (Ellipsis, LazyList([<...>]))]
>>> [*_4.iter__relax(with_tail=True)]
[(Ellipsis, LazyList([<...>]))]
>>> [*null_lazylist.iter__relax(with_tail=True)]
[(None, LazyList())]
>>> [*_5.iter__relax(to_iter_pairs=True)] == [(0, _4)]
True
>>> [*_5.iter__relax(to_iter_pairs=True)]
[(0, LazyList([<...>]))]
>>> [*_4.iter__relax(to_iter_pairs=True)]
[]
>>> [*null_lazylist.iter__relax(to_iter_pairs=True)]
[]
>>> [*_5.iter__relax(with_tail=True, to_iter_pairs=True)] == [(0, _4), (Ellipsis, _4)]
True
>>> [*_5.iter__relax(with_tail=True, to_iter_pairs=True)]
[(0, LazyList([<...>])), (Ellipsis, LazyList([<...>]))]
>>> [*_4.iter__relax(with_tail=True, to_iter_pairs=True)]
[(Ellipsis, LazyList([<...>]))]
>>> [*null_lazylist.iter__relax(with_tail=True, to_iter_pairs=True)]
[(None, LazyList())]
>>> [*_5.iter__le(None, relax=True)]
[0]
>>> _5.extract_prefix__le(None, relax=True)
(0,)
>>> [*_5.iter__le(None, relax=True, to_iter_pairs=True)] == [(0, _4)]
True
>>> [*_5.iter__le(None, relax=True, to_iter_pairs=True)]
[(0, LazyList([<...>]))]
>>> _5.extract_prefix__le(None, relax=True, to_iter_pairs=True) == ((0, _4),)
True
>>> _5.extract_prefix__le(None, relax=True, to_iter_pairs=True)
((0, LazyList([<...>])),)



>>> _5
LazyList([0, <...>])
>>> _4
LazyList([<...>])
>>> null_lazylist
LazyList()

>>> _5.is_empty__tribool()
False
>>> _4.is_empty__tribool()
Ellipsis
>>> null_lazylist.is_empty__tribool()
True

>>> _5
LazyList([0, <...>])
>>> _4
LazyList([<...>])
>>> null_lazylist
LazyList()


>>> _5.extract_prefix__le(2, relax=False)
(0, 1)
>>> _5
LazyList([0, 1, <...>])
>>> _4
LazyList([1, <...>])
>>> [*_5.iter__le(None, relax=False)]
[0, 1, 2, 3, 4]
>>> _5
LazyList([0, 1, 2, 3, 4])
>>> _4
LazyList([1, 2, 3, 4])
>>> [*_5.iter__relax()]
[0, 1, 2, 3, 4]
>>> [*_5.iter__relax(with_end_state=True)]
[0, 1, 2, 3, 4, None]


>>> _5 = LazyList(range(5), non_iterator_ok=True)
>>> _5
LazyList([<...>])
>>> [*_5.iter__hardwork()]
[0, 1, 2, 3, 4]
>>> _5
LazyList([0, 1, 2, 3, 4])

>>> _5 = LazyList(range(5), non_iterator_ok=True)
>>> _5
LazyList([<...>])
>>> [*_5.iter__hardwork(to_iter_pairs=True)]
[(0, LazyList([1, 2, 3, 4])), (1, LazyList([2, 3, 4])), (2, LazyList([3, 4])), (3, LazyList([4])), (4, LazyList())]
>>> _5
LazyList([0, 1, 2, 3, 4])

>>> _5 = LazyList(range(5), non_iterator_ok=True)
>>> _5
LazyList([<...>])
>>> [*_5]
[0, 1, 2, 3, 4]
>>> _5
LazyList([0, 1, 2, 3, 4])
>>> [*_5.iter__le(8, relax=True)]
[0, 1, 2, 3, 4]
>>> [*_5.iter__le(2, relax=True)]
[0, 1]
>>> [*_5.iter__le(3, relax=True, to_iter_pairs=True)]
[(0, LazyList([1, 2, 3, 4])), (1, LazyList([2, 3, 4])), (2, LazyList([3, 4]))]
>>> _5.extract_prefix__le(8, relax=True)
(0, 1, 2, 3, 4)
>>> _5.extract_prefix__le(2, relax=True)
(0, 1)
>>> _5.extract_prefix__le(3, relax=True, to_iter_pairs=True)
((0, LazyList([1, 2, 3, 4])), (1, LazyList([2, 3, 4])), (2, LazyList([3, 4])))
>>> _5.extract_prefix_with_tail__le(3, relax=True)
((0, 1, 2), LazyList([3, 4]))
>>> _5.extract_prefix_with_tail__le(0, relax=True)
((), LazyList([0, 1, 2, 3, 4]))
>>> _5 = LazyList(range(5), non_iterator_ok=True)
>>> _5.extract_prefix_with_tail__le(3, relax=True)
((), LazyList([<...>]))


>>> _5 = LazyList(range(5), non_iterator_ok=True)
>>> LazyList(999, _5)
LazyList([999, <...>])
>>> LazyList([], _5)
LazyList([[], <...>])
>>> LazyList([], _5, head__vs__initial_iterator__vs__initial_seq=True)
LazyList([<...>])
>>> LazyList([], _5, head__vs__initial_iterator__vs__initial_seq=True) is _5
True
>>> LazyList([999], _5)
LazyList([[999], <...>])
>>> LazyList([999], _5).may_unpack() == ([999], _5)
True
>>> LazyList([999], _5, head__vs__initial_iterator__vs__initial_seq=True)
LazyList([999, <...>])
>>> LazyList([999, 666], _5, head__vs__initial_iterator__vs__initial_seq=True)
LazyList([999, 666, <...>])
>>> LazyList([999, 666], _5, head__vs__initial_iterator__vs__initial_seq=True, initial_seq_is_reversed=True)
LazyList([666, 999, <...>])
>>> LazyList.concat_initial_seq_([999, 666], _5)
LazyList([999, 666, <...>])
>>> LazyList.concat_initial_seq_([999, 666], _5, initial_seq_is_reversed=True)
LazyList([666, 999, <...>])
>>> LazyList.concat_head_(999, _5)
LazyList([999, <...>])

>>> LazyList.concat_initial_seq_([999, 666], _5).extract_prefix__relax()
(999, 666)
>>> LazyList.concat_initial_seq_([999, 666], _5).extract_prefix__relax(with_end_state=True)
((999, 666), Ellipsis)
>>> LazyList.concat_initial_seq_([999, 666], null_lazylist).extract_prefix__relax(with_end_state=True)
((999, 666), None)
>>> LazyList.concat_initial_seq_([999, 666], _5).extract_prefix__relax(with_tail=True)
((999, 666), Ellipsis, LazyList([<...>]))
>>> LazyList.concat_initial_seq_([999, 666], null_lazylist).extract_prefix__relax(with_tail=True)
((999, 666), None, LazyList())


input_raise_ToConcatLazyList_ok
head__vs__initial_iterator__vs__initial_seq
concat_initial_iterator_
LazyList.concat_initial_iterator_()
decorator4protocol4ToConcatLazyList_


>>> import seed.types.LazyList as M
>>> M._log = M._dummy_log
>>> M._log = M.print_err
>>> M._log = M._inc # restore:goto

>>> cg = M._mk4clr_get(iter4protocol4ToConcatLazyList_, concat4protocol4ToConcatLazyList_)
>>> cg.clrs()
>>> [*iter4protocol4ToConcatLazyList_([999, 666], prohibit=True)]
[999, 666]
>>> cg.gets_then_clrs()
(1, 0)
>>> [*iter4protocol4ToConcatLazyList_([999, 666], prohibit=False)]
[999, 666]
>>> cg.gets_then_clrs()
(1, 0)
>>> cg.gets_then_clrs()
(0, 0)


>>> _5 = LazyList(range(5), non_iterator_ok=True)
>>> cg.gets_then_clrs()
(1, 0)
>>> [*concat4protocol4ToConcatLazyList_([999, 666], _5, prohibit=False)]
Traceback (most recent call last):
    ...
seed.types.LazyList.ToConcatLazyList: LazyList([<...>])
>>> cg.gets_then_clrs()
(1, 1)
>>> [*concat4protocol4ToConcatLazyList_([999, 666], _5, prohibit=True)]
Traceback (most recent call last):
    ...
seed.types.LazyList.ToConcatLazyList: LazyList([<...>])
>>> cg.gets_then_clrs()
(1, 1)

>>> _5 = LazyList(range(5), non_iterator_ok=True)
>>> cg.gets_then_clrs()
(1, 0)
>>> _5 = LazyList(range(5), non_iterator_ok=True, input_raise_ToConcatLazyList_ok=True)
>>> cg.gets_then_clrs()
(0, 0)
>>> LazyList.concat_initial_iterator_([999, 666], _5)
Traceback (most recent call last):
    ...
TypeError: not iterator
>>> cg.gets_then_clrs()
(0, 0)
>>> LazyList.concat_initial_iterator_(iter([999, 666]), _5)
LazyList([<...>])
>>> cg.gets_then_clrs()
(1, 1)
>>> [*LazyList.concat_initial_iterator_([999, 666], _5, non_iterator_ok=True)]
[999, 666, 0, 1, 2, 3, 4]
>>> cg.gets_then_clrs()
(1, 1)


>>> _5 = LazyList(range(5), non_iterator_ok=True, input_raise_ToConcatLazyList_ok=True)
>>> _7 = LazyList.concat_initial_iterator_(iter([999, 666]), _5)
>>> ls = _7.extract_prefix__le(3, relax=False, to_iter_pairs=True)
>>> ls
((999, LazyList([666, 0, <...>])), (666, LazyList([0, <...>])), (0, LazyList([<...>])))
>>> ls[-2][1] is _5
False
>>> ls[-1][1] is _5.extract_tail_or_raise()
True
>>> cg.gets_then_clrs()
(1, 1)

>>> @decorator4protocol4ToConcatLazyList_
... def mk_LazyList__concat(it, tail_lazylist, /):
...     yield from it
...     raise ToConcatLazyList(tail_lazylist)
>>> _5 = LazyList(range(5), non_iterator_ok=True, input_raise_ToConcatLazyList_ok=True)
>>> sf = mk_LazyList__concat(range(-9,-6), _5)
>>> [*sf]
[-9, -8, -7, 0, 1, 2, 3, 4]
>>> ps = sf.extract_prefix__le(None, relax=True, to_iter_pairs=True)
>>> ps[3][1] is _5.extract_tail_or_raise()
True
>>> ps[2][1] is _5
False


# restore:here
>>> M._log = M._dummy_log

#]]]'''
__all__ = r'''
LazyListError
    LazyListError__unpack_empty_lazylist

LazyList
    null_lazylist

ToConcatLazyList
    Error4ToConcatLazyList
    iter4protocol4ToConcatLazyList_
    concat4protocol4ToConcatLazyList_
    decorator4protocol4ToConcatLazyList_

'''.split()#'''
    #repr_as_lt_3dot_gt
__all__

from seed.tiny import check_type_is, null_tuple, mk_tuple, check_type_le  # null_iter
from seed.tiny import echo as basic_method, is_iterator, print_err
from seed.helper.repr_input import repr_helper
from seed.helper.ConstantRepr import ConstantRepr, repr_as_3dot
from itertools import islice
import functools
from functools import wraps

class _mk4clr_get:
    def __init__(sf, /, *fs):
        sf.fs = fs
    def clrs(sf, /):
        for f in sf.fs:
            _clr(f)
    def gets(sf, /):
        return (*map(_get, sf.fs),)
    def gets_then_clrs(sf, /):
        r = sf.gets()
        sf.clrs()
        return r

def _clr(f, /):
    f._acc_ = 0
def _inc(f, /):
    f._acc_ += 1
    #print_err(f, f._acc_)
def _get(f, /):
    return f._acc_

def _dummy_log(*args, **kwds):pass
_log = _dummy_log

repr_as_lt_3dot_gt = ConstantRepr('<...>')
class _LazyListRelaxIter:
    def __init__(sf, lazylist, /, *, with_end_state, with_tail, to_iter_pairs):
        check_type_is(LazyList, lazylist)
        check_type_is(bool, to_iter_pairs)
        sf._ls = lazylist
        sf._w = with_end_state, with_tail
        sf._ps = to_iter_pairs
    def __iter__(sf, /):
        return sf
    def __next__(sf, /):
        m = sf._ls.may_unpack(relax=True)
        if m is None or m is ...:
            if len(sf._w) == 2:
            #if sf._w:
                with_end_state, with_tail = sf._w
                tail = sf._ls
                sf._ls = null_lazylist
                end_state = m
                #sf._w = False
                sf._w = ((end_state, tail),)
                if with_tail:
                    return end_state, tail
                if with_end_state:
                    return end_state
            else:
                [(end_state, tail)] = sf._w
            raise StopIteration((end_state, tail))
        (x, lazylist) = m
        #check_type_is(LazyList, lazylist)
        sf._ls = lazylist
        if sf._ps:
            return m
        return x


class _LazyListIter:
    def __init__(sf, lazylist, /, *, to_iter_pairs):
        check_type_is(LazyList, lazylist)
        check_type_is(bool, to_iter_pairs)
        sf._ls = lazylist
        sf._ps = to_iter_pairs
    def __iter__(sf, /):
        return sf
    def __next__(sf, /):
        m = sf._ls.may_unpack()
        if m is None:
            raise StopIteration
        (x, lazylist) = m
        #check_type_is(LazyList, lazylist)
        sf._ls = lazylist
        if sf._ps:
            return m
        return x

class ToConcatLazyList(BaseException):
    r'''[[[
    protocol4ToConcatLazyList
        replace StopIteration when stop iter, to concat tail_lazylist
    see:
        + iter4protocol4ToConcatLazyList_
            used in LazyList._init1_
            used in concat4protocol4ToConcatLazyList_
            if prohibit:
                translate ToConcatLazyList to Error4ToConcatLazyList
        + concat4protocol4ToConcatLazyList_
            used in LazyList._init2__initial_iterator_
            to raise ToConcatLazyList to be catched by LazyList.may_unpack
        + LazyList.may_unpack
            catch ToConcatLazyList raised by concat4protocol4ToConcatLazyList_
        + decorator4protocol4ToConcatLazyList_
            used in op on two LazyList
                e.g. continued_fraction add/mul
    #]]]'''#'''
    def __repr__(sf, /):
        return repr_helper(sf, sf._t)
    def __init__(sf, tail_lazylist, /):
        check_type_le(LazyList, tail_lazylist)
        sf._t = tail_lazylist
        super().__init__(tail_lazylist)
    @property
    def tail_lazylist(sf, /):
        return sf._t
class Error4ToConcatLazyList(Exception):pass

def iter4protocol4ToConcatLazyList_(iterable, /, *, prohibit:bool):
    _log(iter4protocol4ToConcatLazyList_)
    check_type_is(bool, prohibit)
    iter(iterable) #check
    return _iter4protocol4ToConcatLazyList_(iterable, prohibit=prohibit)
def _iter4protocol4ToConcatLazyList_(iterable, /, *, prohibit:bool):
    while 1:
        try:
            yield from iterable
        except ToConcatLazyList as e:
            if prohibit:
                raise Error4ToConcatLazyList from e
            iterable = e.tail_lazylist
            del e
            continue
        return
    pass
def concat4protocol4ToConcatLazyList_(initial_iterator, tail_lazylist, /, *, prohibit:bool):
    _log(concat4protocol4ToConcatLazyList_)
    check_type_le(LazyList, tail_lazylist)
    initial_iterator = iter4protocol4ToConcatLazyList_(initial_iterator, prohibit=prohibit)
    return _concat4protocol4ToConcatLazyList_(initial_iterator, tail_lazylist)
def _concat4protocol4ToConcatLazyList_(initial_iterator, tail_lazylist, /):
    yield from initial_iterator
    raise ToConcatLazyList(tail_lazylist)


def decorator4protocol4ToConcatLazyList_(iter_xs_, /):
    @functools.wraps(iter_xs_)
    def mk_LazyList(*args, **kwds):
        it = iter_xs_(*args, **kwds)
        return LazyList(it, non_iterator_ok=False, input_raise_ToConcatLazyList_ok=True)
    return mk_LazyList

class LazyListError(Exception):pass
class LazyListError__unpack_empty_lazylist(LazyListError):pass

class LazyList:
    'vivi Haskell.List'
    r'''[[[
    sf._z :: (None | (x, LazyList x) | Iterator x)
        * None
            empty
        * (x, LazyList x)
            nonempty
        * (Iterator x)
            unknown yet

    #]]]'''#'''
    @classmethod
    def concat_head_(cls, head, tail_lazylist, /):
        check_type_le(LazyList, tail_lazylist)
        return cls(head, tail_lazylist)
    @classmethod
    def concat_initial_iterator_(cls, initial_iterator, tail_lazylist, /, *, non_iterator_ok=False, input_raise_ToConcatLazyList_ok=False):
        '# lazy # === concat__lazy_'
        check_type_le(LazyList, tail_lazylist)
        return cls(initial_iterator, tail_lazylist, non_iterator_ok=non_iterator_ok, head__vs__initial_iterator__vs__initial_seq=..., input_raise_ToConcatLazyList_ok=input_raise_ToConcatLazyList_ok)
    @classmethod
    def concat_initial_seq_(cls, initial_seq, may_tail_lazylist, /, *, initial_seq_is_reversed=False, input_raise_ToConcatLazyList_ok=False):
        '# strict # === concat__strict_'
        if may_tail_lazylist is None:
            tail_lazylist = null_lazylist
        else:
            tail_lazylist = may_tail_lazylist
        check_type_le(LazyList, tail_lazylist)
        return cls(initial_seq, tail_lazylist, head__vs__initial_iterator__vs__initial_seq=True, initial_seq_is_reversed=initial_seq_is_reversed, input_raise_ToConcatLazyList_ok=input_raise_ToConcatLazyList_ok)
    concat__strict_ = concat_initial_seq_
    concat__lazy_ = concat_initial_iterator_

    #def __init__(sf, may_xs=None, /, *, non_iterator_ok=False):
    #def __new__(cls, lazylist_or_may_xs=None, /, *, non_iterator_ok=False):
    def __new__(cls, lazylist_or_may_xs_or_head_or_initial_xs=None, may_tail_lazylist=None, /, *, non_iterator_ok=False, head__vs__initial_iterator__vs__initial_seq=False, initial_seq_is_reversed=False, input_raise_ToConcatLazyList_ok=False):
        if not may_tail_lazylist is None:
            tail_lazylist = may_tail_lazylist
            head_or_initial_xs = lazylist_or_may_xs_or_head_or_initial_xs
            sf = cls._new2_(cls, head_or_initial_xs, tail_lazylist, non_iterator_ok=non_iterator_ok, head__vs__initial_iterator__vs__initial_seq=head__vs__initial_iterator__vs__initial_seq, initial_seq_is_reversed=initial_seq_is_reversed, input_raise_ToConcatLazyList_ok=input_raise_ToConcatLazyList_ok)
        else:
            lazylist_or_may_xs = lazylist_or_may_xs_or_head_or_initial_xs
            sf = cls._new1_(cls, lazylist_or_may_xs, non_iterator_ok=non_iterator_ok, input_raise_ToConcatLazyList_ok=input_raise_ToConcatLazyList_ok)

        return sf
    @basic_method
    #@classmethod
    def _new1_(cls, lazylist_or_may_xs, /, *, non_iterator_ok, input_raise_ToConcatLazyList_ok):
        if isinstance(lazylist_or_may_xs, __class__):
            lazylist = lazylist_or_may_xs
            sf = lazylist
        elif isinstance(lazylist_or_may_xs, _LazyListIter):
            #not _LazyListRelaxIter
            lazylist_iter = lazylist_or_may_xs
            lazylist = lazylist_iter._ls
            sf = lazylist
        else:
            may_xs = lazylist_or_may_xs
            sf = super(__class__, cls).__new__(cls)
            sf._init1_(may_xs, non_iterator_ok=non_iterator_ok, input_raise_ToConcatLazyList_ok=input_raise_ToConcatLazyList_ok)
        return sf
    @basic_method
    #@classmethod
    def _new2_(cls, head_or_initial_xs, tail_lazylist, /, *, non_iterator_ok, head__vs__initial_iterator__vs__initial_seq, initial_seq_is_reversed, input_raise_ToConcatLazyList_ok):
        #if not isinstance(tail_lazylist, __class__):raise TypeError
        check_type_le(__class__, tail_lazylist)
        if False is head__vs__initial_iterator__vs__initial_seq:
            head = head_or_initial_xs
            sf = super(__class__, cls).__new__(cls)
            sf._init2__head_(head, tail_lazylist)
        elif True is head__vs__initial_iterator__vs__initial_seq:
            # .concat_head_()
            initial_seq = head_or_initial_xs
            if is_iterator(initial_seq):raise TypeError
            reversed(initial_seq)
                # check
            # .concat_initial_seq_()
            if initial_seq_is_reversed:
                reversed_initial_seq = iter(initial_seq)
            else:
                reversed_initial_seq = reversed(initial_seq)
                r'''[[[
                try:
                    reversed_initial_seq = reversed(initial_seq)
                except TypeError:
                    reversed_initial_seq = reversed([*initial_seq])
                #]]]'''#'''
            reversed_initial_seq
            reversed_initial_seq = iter4protocol4ToConcatLazyList_(reversed_initial_seq, prohibit=not input_raise_ToConcatLazyList_ok)

            for x in reversed_initial_seq:
                sf = super(__class__, cls).__new__(cls)
                sf._init2__head_(x, tail_lazylist)
                tail_lazylist = sf
            sf = tail_lazylist
        elif ... is head__vs__initial_iterator__vs__initial_seq:
            # .concat_initial_iterator_()
            initial_iterator = head_or_initial_xs
            sf = super(__class__, cls).__new__(cls)
            sf._init2__initial_iterator_(initial_iterator, tail_lazylist, non_iterator_ok=non_iterator_ok, input_raise_ToConcatLazyList_ok=input_raise_ToConcatLazyList_ok)
        else:
            raise TypeError(f'not tribool: type(head__vs__initial_iterator__vs__initial_seq) is {type(head__vs__initial_iterator__vs__initial_seq)}')
        sf
        return sf

    @basic_method
    def _init2__head_(sf, head, tail_lazylist, /):
        #if not isinstance(tail_lazylist, __class__):raise TypeError
        #check_type_le(__class__, tail_lazylist)
        sf._z = (head, tail_lazylist)
        return
    @basic_method
    def _init2__initial_iterator_(sf, initial_iterator, tail_lazylist, /, *, non_iterator_ok, input_raise_ToConcatLazyList_ok):
        if not (non_iterator_ok or is_iterator(initial_iterator)):raise TypeError('not iterator')
        sf._z = concat4protocol4ToConcatLazyList_(initial_iterator, tail_lazylist, prohibit=not input_raise_ToConcatLazyList_ok)
            #vs: _init1_
        return
    @basic_method
    def _init1_(sf, may_xs, /, *, non_iterator_ok, input_raise_ToConcatLazyList_ok):

        sf._z = None
        if may_xs is None:
            z = None
        else:
            xs = may_xs
            iter(xs) #check
            if not (non_iterator_ok or is_iterator(xs)):raise TypeError('not iterator')
            #bug:it = iter4protocol4ToConcatLazyList_(xs, prohibit=not input_raise_ToConcatLazyList_ok)
            prohibit = not input_raise_ToConcatLazyList_ok
            if prohibit:
                it = iter4protocol4ToConcatLazyList_(xs, prohibit=True)
                    #vs: _init2__initial_iterator_
            else:
                it = iter(xs)
            z = it
        sf._z = z
    @basic_method
    def may_unpack(sf, /, *, relax=False):
        'LazyList x -> (may (x, LazyList x)) if not relax else (... | may (x, LazyList x))'
        z = sf._z
        if type(z) is tuple:
            #unpacked already
            #nonempty
            return z
        if z is None:
            #unpacked already
            #empty
            return None
        #not unpacked yet
        #iterator
        if relax:
            #donot unpack actually
            return ...
        #unpacking...
        it = z
        try:
            x = next(it)
        except ToConcatLazyList as e:
            ot = e.tail_lazylist
            z = ot.may_unpack()
        except StopIteration:
            z = None
        else:
            #bug:z = (x, LazyList(it))
            z = (x, LazyList(it, non_iterator_ok=False, input_raise_ToConcatLazyList_ok=True))
        sf._z = z
        return sf.may_unpack()
        return z
    def may_unpack__relax(sf, /):
        'LazyList x -> (... | may (x, LazyList x))'
        return sf.may_unpack(relax=True)
    #@basic_method
    #   depend upon .may_unpack() only
    def iter__relax(sf, /, *, with_end_state=False, with_tail=False, to_iter_pairs=False):
        'LazyList x -> Iter ((x, LazyList x) if to_iter_pairs else x) ++ ([(end_state,tail)] if with_tail else ([end_state] if with_end_state else [])) # [relax =[def]= call .may_unpack(relax=True)]'
        return _LazyListRelaxIter(sf, with_end_state=with_end_state, with_tail=with_tail, to_iter_pairs=to_iter_pairs)
    #@basic_method
    #   depend upon .may_unpack() only
    def iter__hardwork(sf, /, *, to_iter_pairs=False):
        'LazyList x -> Iter ((x, LazyList x) if to_iter_pairs else x) # [hardwork =[def]= call .may_unpack(relax=False)]'
        return _LazyListIter(sf, to_iter_pairs=to_iter_pairs)
    def __iter__(sf, /):
        return sf.iter__hardwork()
    __iter__ = iter__hardwork
    __bool__ = ...
    __len__ = ...
    __contains__ = ...
    # %s/\<is_empty\>/is_empty__hardwork/g
    def is_empty__hardwork(sf, /):
        'LazyList x -> bool # side-effect:may_unpack()'
        return sf.is_empty_(relax=False)
        return None is sf.may_unpack()
    def is_empty__tribool(sf, /):
        'LazyList x -> (bool | ...) # no-side-effect'
        return sf.is_empty_(relax=True)
    def is_empty_(sf, /, *, relax):
        'LazyList x -> (bool | ...) if relax else bool'
        m = sf.may_unpack(relax=relax)
        if m is ...:
            return ...
        return m is None

    def __repr__(sf, /):
        #return repr_helper(sf, sf._z)
        xs_ = [*sf.iter__relax(with_end_state=True)]
        end_state = xs_.pop()

        if end_state is ...:
            #bug:xs_.append(xs_) #to show '...'
            #   fail: LazyList([[...]])
            #xs_.append(repr_as_3dot) #to show '...'
            xs_.append(repr_as_lt_3dot_gt) #to show '...'
        elif not xs_:
            assert end_state is None
            return repr_helper(sf)
        assert xs_

        s = repr_helper(sf, xs_)
        xs_.clear() # break cyclic ref
        return s


    def iter__le(sf, may_max_sz, /, *, relax, to_iter_pairs=False):
        'LazyList x -> may max_sz/uint -> Iter<x>{len<=max_sz}'
        if relax:
            f = sf.iter__relax
        else:
            f = sf.iter__hardwork

        it = f(to_iter_pairs=to_iter_pairs)
        if not may_max_sz is None:
            max_sz = may_max_sz
            it = islice(it, max_sz)
        return it
    # %s/\<slice_prefix__le\>/extract_prefix__le/g
    def extract_prefix_with_tail__le(sf, may_max_sz, /, *, relax):
        'LazyList x -> may max_sz/uint -> (prefix, tail)/(tuple<x>{len<=max_sz}, LazyList x)'
        ps = sf.iter__le(may_max_sz, relax=relax, to_iter_pairs=True)
        prefix = []
        tail = sf
        for x, tail in ps:
            prefix.append(x)
        prefix = mk_tuple(prefix)
        return (prefix, tail)
    def extract_prefix__le(sf, may_max_sz, /, *, relax, to_iter_pairs=False):
        'LazyList x -> may max_sz/uint -> tuple<x>{len<=max_sz}'
        return mk_tuple(sf.iter__le(may_max_sz, relax=relax, to_iter_pairs=to_iter_pairs))
    def extract_prefix__relax(sf, /, *, with_end_state=False, with_tail=False):
        '-> if with_tail then (prefix, end_state, tail) elif with_end_state then (prefix, end_state) else prefix'
        xs_ = [*sf.iter__relax(with_end_state=with_end_state, with_tail=with_tail)]
        if with_tail:
            end_state, tail = xs_.pop()
            ex = end_state, tail
        elif with_end_state:
            end_state = xs_.pop()
            ex = [end_state]
        else:
            ex = []
        prefix = mk_tuple(xs_)
        if ex:
            return (prefix, *ex)
        return prefix

    # %s/get_/extract_/g
    def extract_tmay_head(sf, /):
        'LazyList x -> may x'
        m = sf.may_unpack()
        if m is None:
            return null_tuple
        return m[:1]
    def extract_tmay_tail(sf, /):
        'LazyList x -> may (LazyList x)'
        m = sf.may_unpack()
        if m is None:
            return null_tuple
        return m[1:]

    def unpack_or_raise(sf, /):
        'LazyList x -> (x, LazyList x) | ^LazyListError'
        m = sf.may_unpack()
        if m is None:
            raise LazyListError__unpack_empty_lazylist
        return m
    def extract_head_or_raise(sf, /):
        'LazyList x -> may x'
        return sf.unpack_or_raise()[0]
    def extract_tail_or_raise(sf, /):
        'LazyList x -> may (LazyList x)'
        return sf.unpack_or_raise()[1]
null_lazylist = LazyList(None)
    # used in _LazyListRelaxIter

if __name__ == "__main__":
    pass
__all__


from seed.types.LazyList import ToConcatLazyList, decorator4protocol4ToConcatLazyList_
from seed.types.LazyList import LazyList, LazyListError
from seed.types.LazyList import *
