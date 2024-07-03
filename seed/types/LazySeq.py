#__all__:goto
r'''[[[
e ../../python3_src/seed/types/LazySeq.py


seed.types.LazySeq
py -m nn_ns.app.debug_cmd   seed.types.LazySeq -x
py -m nn_ns.app.doctest_cmd seed.types.LazySeq:__doc__ -ff -v
py_adhoc_call   seed.types.LazySeq   @f



>>> from seed.types.LazySeq import LazySeq
>>> _5 = LazySeq(range(5, 10))
>>> _5
LazySeq(LazyList([<...>]))
>>> _5.get_len__relax__no_extend()
0
>>> _5.get_len__relax__extend()
0
>>> _5
LazySeq(LazyList([<...>]))
>>> _5.extract_pair_at_(2)
(7, LazyList([<...>]))
>>> _5
LazySeq(LazyList([5, 6, 7, <...>]))
>>> _5[2]
7
>>> _5[1]
6
>>> _5.extract_tail_lazylist_at_(1)
LazyList([7, <...>])
>>> _5.extract_whole_lazylist_at_(2)
LazyList([7, <...>])
>>> _5.extract_whole_lazylist_at_(2) is _5.extract_tail_lazylist_at_(1)
True
>>> _5.get_len__relax__no_extend()
3
>>> _5.get_len__relax__extend()
3
>>> _5
LazySeq(LazyList([5, 6, 7, <...>]))
>>> _5.extract_whole_lazylist_at_(2).extract_prefix__le(2, relax=False)
(7, 8)
>>> _5
LazySeq(LazyList([5, 6, 7, 8, <...>]))
>>> _5.get_len__relax__no_extend()
3
>>> _5.get_len__relax__extend()
4
>>> _5.get_len__relax__no_extend()
4
>>> _5
LazySeq(LazyList([5, 6, 7, 8, <...>]))
>>> [*_5]
[5, 6, 7, 8, 9]


>>> _5 = LazySeq(range(5, 10))
>>> _5[:...]
()
>>> _5[2:4]
(7, 8)
>>> _5[:...]
(5, 6, 7, 8)
>>> _5.extract_elements_with_last_tail_between_nonempty_range_(None, 999)
((5, 6, 7, 8, 9), LazyList())
>>> _5.extract_elements_between_(None, 999)
(5, 6, 7, 8, 9)
>>> _5.extract_pairs_between_(3, 999)
((8, LazyList([9])), (9, LazyList()))

#]]]'''
__all__ = r'''
    LazySeq
'''.split()#'''
__all__

from seed.types.LazyList import LazyList, LazyListError

from seed.tiny import check_type_is
from seed.tiny_.check import check_uint, check_int_ge
from seed.tiny import echo, null_iter, is_iterable, null_tuple
from seed.helper.repr_input import repr_helper
from seed.types.NamedReadOnlyProperty import NamedReadOnlyProperty, set_NamedReadOnlyProperty4cls_, set_NamedReadOnlyProperty4sf_
from seed.types.exc.UnsupportedOperation import Attr4UnsupportedOperation


class LazySeq:
    _attr_nms = r'''
    _init_seq
    _tails
    _eof
    '''.split()#'''
    #   xxx ._lazylist
    # [len(_tails) == len(_init_seq)+1]
    @property
    def the_lazylist(sf, /):
        return sf._tails[0]

    if 0:
        def get_args(sf, /):
            return tuple(getattr(sf, nm) for nm in __class__._attr_nms)
    def __repr__(sf, /):
        return repr_helper(sf, sf.the_lazylist)
    def __new__(cls, xs, /):
        if not is_iterable(xs): raise TypeError

        if isinstance(xs, __class__):
            sf = xs
        else:
            sf = super(__class__, cls).__new__(cls)
            sf._init_(xs)
        return sf
    def _init_(sf, _lazylist, /):
        _lazylist = LazyList(_lazylist, non_iterator_ok=True)
        _init_seq = []
        _tails = [_lazylist]
        # [len(_tails) == len(_init_seq)+1]
        _eof = _tails[-1].is_empty__tribool() is True
        ########init sf:
        set_NamedReadOnlyProperty4sf_(sf, __class__._attr_nms, locals())
    def _destroy_on_bad_format_(sf, /):
        sf.__dict__.clear()
    def _check_on_no_more_extend_(sf, _init_seq, _tails, /):
        pass
    def _check_post__extend_more_(sf, _init_seq, begin4init_seq, _tails, begin4tails, /):
        pass
    def extend_more_(sf, may_max_sz4extend, /, *, relax:bool):
        'may uint -> None # call .may_unpack(relax=relax)'
        _init_seq = sf._init_seq
        _tails = sf._tails
        ps = _tails[-1].extract_prefix__le(may_max_sz4extend, relax=relax, to_iter_pairs=True)
        if ps:
            begin4init_seq = len(_init_seq)
            begin4tails = len(_tails)
            for x, tail in ps:
                _init_seq.append(x)
                _tails.append(tail)
                # [len(_tails) == len(_init_seq)+1]
            try:
                sf._check_post__extend_more_(_init_seq, begin4init_seq, _tails, begin4tails)
            except:
                sf._destroy_on_bad_format_()
                raise
        if not sf._eof:
            _eof = _tails[-1].is_empty__tribool() is True
            if _eof:
                set_NamedReadOnlyProperty4sf_(sf, ['_eof'], locals())
                assert sf._eof
                try:
                    sf._check_on_no_more_extend_(_init_seq, _tails)
                except:
                    sf._destroy_on_bad_format_()
                    raise
        return None
    def extend_more__hardwork_(sf, may_max_sz4extend, /):
        'may uint -> None # call .may_unpack(relax=False)'
        sf.extend_more_(may_max_sz4extend, relax=False)
    def extend_more__relax_(sf, may_max_sz4extend, /):
        'may uint -> None # call .may_unpack(relax=True)'
        sf.extend_more_(may_max_sz4extend, relax=True)
    def get_len__relax_(sf, /, *, to_extend:bool):
        '-> uint # call .may_unpack(relax=True) if to_extend else donot call .may_unpack()'
        if to_extend:
            sf.extend_more__relax_(None)
        return len(sf._init_seq)
        if to_extend:
            return sf.get_len__relax__extend()
        return sf.get_len__relax__no_extend()
    def get_len__relax__no_extend(sf, /):
        '-> uint # donot call .may_unpack()'
        return sf.get_len__relax_(to_extend=False)
    def get_len__relax__extend(sf, /):
        '-> uint # call .may_unpack(relax=True)'
        return sf.get_len__relax_(to_extend=True)

    def __getitem__(sf, i_or_sl, /):
        if type(i_or_sl) is slice:
            sl = i_or_sl
            if not sl.step is None:raise TypeError
            begin = sl.start
            end = sl.stop
            xs = sf.extract_elements_between_(begin, end)
            return xs
        i = i_or_sl
        (x, tail) = sf.extract_pair_at_(i)
        return x
    def extract_tail_lazylist_at_(sf, i, /):
        '[[tail_lazylist@i === whole_lazylist@(i+1)][whole_lazylist@i === LazyList.concat_head_(x@i, tail_lazylist@i)]]'
        (x, tail) = sf.extract_pair_at_(i)
        return tail
    def extract_whole_lazylist_at_(sf, i, /):
        '[[tail_lazylist@i === whole_lazylist@(i+1)][whole_lazylist@i === LazyList.concat_head_(x@i, tail_lazylist@i)]]'

        check_uint(i)
        if i == 0:
            return sf.the_lazylist
            return sf._tails[0]
        return sf.extract_tail_lazylist_at_(i-1)
    def extract_pair_at_(sf, i, /):
        'LazySeq x -> i/uint -> (x, tail/LazyList x) #(x@i, tail_lazylist@i===whole_lazylist@(i+1)))'
        sf._prepare4extract_at_(i)
        x = sf._init_seq[i]
        tail = sf._tails[i+1]
        #sf._check_type4getitem_(i, x)
        return x, tail
    def extract_elements_with_last_tail_between_nonempty_range_(sf, begin, end, /):
        'LazySeq x -> begin/(uint|None) -> end/(uint|...) -> ([x], last_tail/LazyList x)'
        return sf.extract_pairs_between_(begin, end, elements_only=True, elements_with_last_tail=True)
    def extract_elements_between_(sf, begin, end, /, *, elements_with_last_tail=False):
        'LazySeq x -> begin/(uint|None) -> end/(uint|...) -> [x]'
        return sf.extract_pairs_between_(begin, end, elements_only=True, elements_with_last_tail=elements_with_last_tail)
    def extract_pairs_between_(sf, begin, end, /, *, elements_only=False, elements_with_last_tail=False):
        'LazySeq x -> begin/(uint|None) -> end/(uint|...) -> [(x, tail/LazyList x)] #(x@i, tail_lazylist@i===whole_lazylist@(i+1))) where [i :<- [begin..<end]'
        if begin is None:
            begin = 0
        if end is ...:
            #<==> relax
            #bug:end = len(sf._tails)
            #   should be: end = len(sf._tails) -1
            end = len(sf._init_seq)
        check_uint(begin)
        check_uint(end)
        if not begin < end:
            if elements_with_last_tail:
                raise IndexError('elements_with_last_tail:but empty range')
            return null_tuple
        sf._prepare4extract_at_(end-1, not_enough_ok=True)
        xs = sf._init_seq[begin:end]
        if elements_with_last_tail:
            if end < len(sf._tails):
                last_tail = sf._tails[end]
            else:
                last_tail = sf._tails[-1]
            xs = (*xs,)
            return xs, last_tail
        if elements_only:
            xs = (*xs,)
            return xs
        tails = sf._tails[begin+1:end+1]
        ps = (*zip(xs, tails),)
        return ps
    def _prepare4extract_at_(sf, i, /, *, not_enough_ok=False):
        check_uint(i)
        ls = sf._init_seq
        if not i < len(ls):
            sz = i+1 -len(ls)
            sf.extend_more__hardwork_(sz)
        if not i < len(ls):
            assert sf._tails[-1].is_empty__tribool() is True
            if not_enough_ok:
                pass
            else:
                raise IndexError(i)
        return

    def __iter__(sf, /):
        it = iter(sf.the_lazylist)
        del sf # to free memory as soon as possible: _lazylist,_init_seq,_tails
        return it
    __bool__ = ...
    __len__ = ...
    __contains__ = ...
    __bool__ = Attr4UnsupportedOperation()
    __len__ = Attr4UnsupportedOperation()
    __contains__ = Attr4UnsupportedOperation()


if 1:
    set_NamedReadOnlyProperty4cls_(LazySeq, LazySeq._attr_nms)
#end-class LazySeq:



if __name__ == "__main__":
    pass
__all__


from seed.types.LazySeq import LazySeq
from seed.types.LazySeq import *
