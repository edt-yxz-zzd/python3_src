#__all__:goto
r'''[[[
e ../../python3_src/seed/abc/IReproduceable.py
view ../../python3_src/seed/types/HistorySaver.py
view ../../python3_src/seed/math/primality_test/reproduceable7probable_primes.py

seed.abc.IReproduceable
py -m nn_ns.app.debug_cmd   seed.abc.IReproduceable -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.abc.IReproduceable:__doc__ -ht # -ff -df
#######

[[
come_from:
e ../../python3_src/seed/math/factor_pint/factor_pint__smooth_group_order_method.py
]]


'#'; __doc__ = r'#'
>>> Reproduceable5seq('0123456789', 0)
Reproduceable5seq('0123456789', 0)
>>> iter_pairs4reproduceable_(Reproduceable5seq('0123456789', 0))
Iter4IReproduceable(Reproduceable5seq('0123456789', 0))
>>> [*iter_pairs4reproduceable_(Reproduceable5seq('0123456789', 0))]
[('0', Reproduceable5seq('0123456789', 1)), ('1', Reproduceable5seq('0123456789', 2)), ('2', Reproduceable5seq('0123456789', 3)), ('3', Reproduceable5seq('0123456789', 4)), ('4', Reproduceable5seq('0123456789', 5)), ('5', Reproduceable5seq('0123456789', 6)), ('6', Reproduceable5seq('0123456789', 7)), ('7', Reproduceable5seq('0123456789', 8)), ('8', Reproduceable5seq('0123456789', 9)), ('9', Reproduceable5seq('0123456789', 10))]



>>> [*iter_pairs4reproduceable_(Reproduceable5seq('0123456789', 7))]
[('7', Reproduceable5seq('0123456789', 8)), ('8', Reproduceable5seq('0123456789', 9)), ('9', Reproduceable5seq('0123456789', 10))]
>>> [*iter_fsts4reproduceable_(Reproduceable5seq('0123456789', 7))]
['7', '8', '9']
>>> [*iter_snds4reproduceable_(Reproduceable5seq('0123456789', 7))]
[Reproduceable5seq('0123456789', 8), Reproduceable5seq('0123456789', 9), Reproduceable5seq('0123456789', 10)]






>>> rp7null = Reproduceable5seq('', 0)
>>> rp03 = Reproduceable5seq('012', 0)
>>> rp34 = Reproduceable5seq('3', 0)
>>> rp_ls = [rp7null, rp7null, rp03, rp7null, rp7null, rp34, rp7null, rp7null]

Reproduceable7chain5iterable
Reproduceable7chain5reproduceable
>>> rp = Reproduceable7chain5iterable(iter(rp_ls))
>>> rp
Reproduceable7chain5iterable([Reproduceable5seq('', 0), Reproduceable5seq('', 0), Reproduceable5seq('012', 0), Reproduceable5seq('', 0), Reproduceable5seq('', 0), Reproduceable5seq('3', 0), Reproduceable5seq('', 0), Reproduceable5seq('', 0)])
>>> [*iter_fsts4reproduceable_(rp)]
['0', '1', '2', '3']


>>> rp = Reproduceable7chain5reproduceable(None, Reproduceable5seq(rp_ls, 0))
>>> rp
Reproduceable7chain5reproduceable(None, Reproduceable5seq([Reproduceable5seq('', 0), Reproduceable5seq('', 0), Reproduceable5seq('012', 0), Reproduceable5seq('', 0), Reproduceable5seq('', 0), Reproduceable5seq('3', 0), Reproduceable5seq('', 0), Reproduceable5seq('', 0)], 0))
>>> [*iter_fsts4reproduceable_(rp)]
['0', '1', '2', '3']



Reproduceable7fmap
Reproduceable7transform
>>> rp = Reproduceable7fmap(int, rp03)
>>> rp
Reproduceable7fmap(<class 'int'>, Reproduceable5seq('012', 0))
>>> [*iter_fsts4reproduceable_(rp)]
[0, 1, 2]

>>> rp = Reproduceable7transform(lambda st,ch:(f'{st}:{ch}', st-1), 999, rp03)
>>> rp #doctest: +ELLIPSIS
Reproduceable7transform(<function <lambda> at 0x...>, 999, Reproduceable5seq('012', 0))
>>> [*iter_fsts4reproduceable_(rp)]
['999:0', '998:1', '997:2']




Reproduceable7rdiff
Reproduceable7foldl
>>> rp = Reproduceable7rdiff(int.__rsub__, 40, Reproduceable5seq(range(5), 0))
>>> rp
Reproduceable7rdiff(<slot wrapper '__rsub__' of 'int' objects>, 40, Reproduceable5seq(range(0, 5), 0))
>>> [*iter_fsts4reproduceable_(rp)]
[-40, 1, 1, 1, 1]


>>> rp = Reproduceable7foldl(int.__add__, 40, Reproduceable5seq(range(5), 0))
>>> rp
Reproduceable7foldl(<slot wrapper '__add__' of 'int' objects>, 40, Reproduceable5seq(range(0, 5), 0))
>>> [*iter_fsts4reproduceable_(rp)]
[40, 41, 43, 46, 50]





>>> class C:
...     def ___xnext4reproduceable___(sf, /):return 66666
>>> issubclass(C, IReproduceable)
True
>>> isinstance(C(), IReproduceable)
True
>>> is_reproduceable_(C())
True
>>> check_reproduceable_(C())
>>> xnext4reproduceable_(C())
66666
>>> xnext4reproduceable7check_(C())
Traceback (most recent call last):
    ...
TypeError: <class 'int'>






>>> rp = Reproduceable5seq(range(5), 0)
>>> xnext4reproduceable_(rp)
NextEx(0, Reproduceable5seq(range(0, 5), 1))
>>> check_result5xnext4reproduceable_(xnext4reproduceable_(rp))
>>> xnext4reproduceable7check_(rp)
NextEx(0, Reproduceable5seq(range(0, 5), 1))



>>> rp = Reproduceable5seq('', 0)
>>> xnext4reproduceable_(rp)
StopEx(0)
>>> check_result5xnext4reproduceable_(xnext4reproduceable_(rp))
>>> xnext4reproduceable7check_(rp)
StopEx(0)

>>> next(iter_pairs4reproduceable_(Reproduceable5seq('', 0)))
Traceback (most recent call last):
    ...
StopIteration: 0
>>> next(iter_fsts4reproduceable_(Reproduceable5seq('', 0)))
Traceback (most recent call last):
    ...
StopIteration: 0
>>> next(iter_snds4reproduceable_(Reproduceable5seq('', 0)))
Traceback (most recent call last):
    ...
StopIteration: 0













>>> from itertools import islice

Reproduceable7repeat
>>> rp = Reproduceable7repeat(999, 3)
>>> rp
Reproduceable7repeat(999, 3)
>>> [*iter_fsts4reproduceable_(rp)]
[999, 999, 999]
>>> [*iter_snds4reproduceable_(rp)]
[Reproduceable7repeat(999, 2), Reproduceable7repeat(999, 1), Reproduceable7repeat(999, 0)]

>>> rp = Reproduceable7repeat(999, -1)
>>> rp
Reproduceable7repeat(999, -1)
>>> [*islice(iter_fsts4reproduceable_(rp), 5)]
[999, 999, 999, 999, 999]
>>> [*islice(iter_snds4reproduceable_(rp), 5)]
[Reproduceable7repeat(999, -1), Reproduceable7repeat(999, -1), Reproduceable7repeat(999, -1), Reproduceable7repeat(999, -1), Reproduceable7repeat(999, -1)]


Reproduceable7customized_repr
>>> rp = Reproduceable7customized_repr(lambda rp:f'<{rp!r}>', Reproduceable7repeat(999, 3))
>>> rp
<Reproduceable7repeat(999, 3)>
>>> str(rp) #doctest: +ELLIPSIS
'Reproduceable7customized_repr(<function <lambda> at 0x...>, Reproduceable7repeat(999, 3))'
>>> [*iter_fsts4reproduceable_(rp)]
[999, 999, 999]
>>> [*iter_snds4reproduceable_(rp)]
[<Reproduceable7repeat(999, 2)>, <Reproduceable7repeat(999, 1)>, <Reproduceable7repeat(999, 0)>]





Reproduceable7cached_oresult
Reproduceable7tmay_prev_oresult
>>> rp0 = Reproduceable7cached_oresult(Reproduceable5seq(range(2), 0))
>>> rp0
Reproduceable7cached_oresult(Reproduceable5seq(range(0, 2), 0))
>>> rp0.oresult
0
>>> [*iter_fsts4reproduceable_(rp0)]
[0, 1]
>>> (oresult0, rp1) = xnext4reproduceable_(rp0)
>>> (oresult1, rp2) = xnext4reproduceable_(rp1)
>>> rp1.oresult
1
>>> rp2.exit_status
2
>>> rp2.oresult
Traceback (most recent call last):
    ...
ValueError
>>> rp1.exit_status
Traceback (most recent call last):
    ...
ValueError


>>> rp0 = Reproduceable7tmay_prev_oresult((), Reproduceable5seq(range(2), 0))
>>> rp0
Reproduceable7tmay_prev_oresult((), Reproduceable5seq(range(0, 2), 0))
>>> rp0.prev_oresult
Traceback (most recent call last):
    ...
ValueError
>>> [*iter_fsts4reproduceable_(rp0)]
[0, 1]
>>> (oresult0, rp1) = xnext4reproduceable_(rp0)
>>> (oresult1, rp2) = xnext4reproduceable_(rp1)
>>> rp1.prev_oresult
0
>>> rp2.prev_oresult
1
>>> rp1
Reproduceable7tmay_prev_oresult((0,), Reproduceable5seq(range(0, 2), 1))











py_adhoc_call   seed.abc.IReproduceable   @f
]]]'''#'''
__all__ = r'''
IReproduceable
    is_reproduceable_
        check_reproduceable_

    xnext4reproduceable_
        xnext4reproduceable7check_
        check_result5xnext4reproduceable_
            ResultTypes4xnext
                NextEx
                StopEx

    iter_pairs4reproduceable_
        iter_fsts4reproduceable_
        iter_snds4reproduceable_
        Iter4IReproduceable

IReproduceable
    Reproduceable5seq


    Reproduceable7chain5iterable
    Reproduceable7chain5reproduceable
    IReproduceable7fmap
        Reproduceable7fmap
    IReproduceable7transform
        Reproduceable7transform

        IReproduceable7transform7init
        IReproduceable7rdiff
            Reproduceable7rdiff
        IReproduceable7foldl
            Reproduceable7foldl

    Reproduceable7repeat
    IReproduceable7wrapper
        Reproduceable7customized_repr

    Reproduceable7cached_oresult
    Reproduceable7tmay_prev_oresult
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.check import check_type_le, check_type_is, check_may_, check_callable, check_type_in, check_int_ge, check_tmay
    from seed.helper.repr_input import repr_helper
    from seed.tiny_.funcs import fst, snd
    from seed.data_funcs.lnkls import get_empty_lflnkls, lflnkls_ipush_left, lflnkls_ipop_left, lflnkls2iterable, lflnkls5reversed_iterable
    from seed.seq_tools.force_reversed import force_reversed

    from seed.types.CachedProperty import CachedProperty
    from seed.for_libs.for_collections.override_repr4namedtuple import mk_namedtuple_, mk_namedtuple__check6make_
    #def mk_namedtuple_(__module__, nm, nms_or_str, /, *args, **kwds):
    #def mk_namedtuple__check6make_(__module__, nm, nms_or_str, /, *args, **kwds):
    #    def _check6make_(sf, /):

#.    from seed.for_libs.for_collections.namedtuple__nontuple4cached_property import mk_named_pseudo_tuple_
#.    #def mk_named_pseudo_tuple_(__module__,typename, field_names, /):
#.    #    def _check6make_(sf, /):
#.    from seed.for_libs.for_collections.namedtuple__nontuple4cached_property import collect_tuple_subclasses_with_cached_property
#.    #assert not (__:=collect_tuple_subclasses_with_cached_property(globals(), to_print_err=True)), __
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

_NextEx = mk_namedtuple__check6make_(__name__, '_NextEx', 'oresult,tail')
    #followup,following,subsequent
    #tail_reproduceable
class NextEx(_NextEx):
    stopped = False
    def _check6make_(sf, /):
        #check_type_le(IReproduceable, tail_reproduceable)
        check_type_le(IReproduceable, sf.tail)
_StopEx = mk_namedtuple__check6make_(__name__, '_StopEx', 'exit_status')
class StopEx(_StopEx):
    #def _check6make_(sf, /): pass
    stopped = True
class _Type4ResultTypes4xnext(tuple):
    NextEx = NextEx
    StopEx = StopEx
ResultTypes4xnext = _Type4ResultTypes4xnext((NextEx, StopEx))
    #used:check_type_in
    #used:match-case * lazy_import__func7context{arbitrary_ok=True}
assert NextEx is ResultTypes4xnext.NextEx
assert StopEx is ResultTypes4xnext.StopEx

class IReproduceable(ABC):
    'reproduceable'
    __slots__ = ()
    @abstractmethod
    def ___xnext4reproduceable___(sf, /):
        'IReproduceable{x} -> (NextEx(x, IReproduceable{x}) | StopEx(exit_status))'
        #'IReproduceable{x} -> ((True, x, IReproduceable{x}) | (False, exit_status))'
    @classmethod
    def __subclasshook__(cls, cls7testing, /):
        #return _is_reproduceable_type_(cls)
        if cls is __class__:
            if any("___xnext4reproduceable___" in B.__dict__ for B in cls7testing.__mro__):
                return True
        return NotImplemented

#class StopReprodution(BaseException)
def check_result5xnext4reproduceable_(r, /):
    check_type_in(ResultTypes4xnext, r)
    return
r'''[[[
    match r:
        case tuple([bool(True), oresult, IReproduceable() as tail_reproduceable]):
            pass
        case tuple([bool(False), exit_status]):
            pass
        case bad:
            raise TypeError('xnext4reproduceable_()->???', bad)
    return
#]]]'''#'''

def is_reproduceable_(reproduceable, /):
    cls = type(reproduceable)
    return _is_reproduceable_type_(cls)
def _is_reproduceable_type_(cls, /):
    try:
        cls.___xnext4reproduceable___
    except AttributeError:
        return False
    return True
def _gcheck_reproduceable_(reproduceable, /):
    cls = type(reproduceable)
    try:
        return cls.___xnext4reproduceable___
    except AttributeError:
        raise TypeError('not IReproduceable:', cls)
def check_reproduceable_(reproduceable, /):
    _gcheck_reproduceable_(reproduceable)
        # ^TypeError
def xnext4reproduceable_(reproduceable, /, *, to_check=False):
    'IReproduceable{x} -> (NextEx(x, IReproduceable{x}) | StopEx(exit_status))'
    #'IReproduceable{x} -> ((True, x, IReproduceable{x}) | (False, exit_status))'
    ___xnext4reproduceable___ = _gcheck_reproduceable_(reproduceable)
        # ^TypeError
    r = ___xnext4reproduceable___(reproduceable)
    if to_check:
        check_result5xnext4reproduceable_(r)
    return r
def xnext4reproduceable7check_(reproduceable, /, *, to_check=True):
    'IReproduceable{x} -> (NextEx(x, IReproduceable{x}) | StopEx(exit_status))'
    #'IReproduceable{x} -> ((True, x, IReproduceable{x}) | (False, exit_status))'
    return xnext4reproduceable_(reproduceable, to_check=to_check)
def iter_fsts4reproduceable_(reproduceable, /):
    return map(fst, iter_pairs4reproduceable_(reproduceable))
def iter_snds4reproduceable_(reproduceable, /):
    return map(snd, iter_pairs4reproduceable_(reproduceable))
def iter_pairs4reproduceable_(reproduceable, /):
    #old:return iter(reproduceable)
    return Iter4IReproduceable(reproduceable)


r'''[[[
%s/def \zs\<xnext_\>\ze/___xnext4reproduceable___/g
%s/\([a-zA-Z_.]\+\)\.\<xnext_\>()/xnext4reproduceable_(\1)/g
0|1 --> bool --> NextEx|StopEx

TODO:只保留___xnext4reproduceable___
    StopReprodution(BaseException)
    iter_pairs4reproduceable_
    iter_fsts4reproduceable_
    iter_snds4reproduceable_
    check_result5xnext4reproduceable_
    check_reproduceable_ hasattr
    from seed.helper.Echo import theEcho
old:
    @abstractmethod
    def xnext_(sf, /):
        'IReproduceable{x} -> ((True, x, IReproduceable{x}) | (False, exit_status))'
    def __iter__(sf, /):
        '-> (Iter (x, IReproduceable)){return:exit_status}'
        return Iter4IReproduceable(sf)
    def iter_fsts_(sf, /):
        return map(fst, iter(sf))
    def iter_snds_(sf, /):
        return map(snd, iter(sf))
    def iter_pairs_(sf, /):
        return iter(sf)
#]]]'''#'''
class Iter4IReproduceable:
    def __init__(sf, reproduceable, /):
        check_type_le(IReproduceable, reproduceable)
        sf._rp = reproduceable
    def __repr__(sf, /):
        reproduceable = sf._rp
        return repr_helper(sf, reproduceable)
    def __iter__(sf, /):
        return sf
    def __next__(sf, /):
        match xnext4reproduceable_(sf._rp):
            case NextEx(x, rp):
                #case (True, x, IReproduceable() as rp):
                sf._rp = rp
                return (x, rp)
            case StopEx(exit_status):
                #case (False, exit_status):
                raise StopIteration(exit_status)
            case bad:
                raise TypeError('xnext4reproduceable_()->???', bad)

class Reproduceable5seq(IReproduceable):
    '[x] -> IReproduceable{x}'
    ___no_slots_ok___ = True
    @classmethod
    def mk5seq_and_xidx_(cls, seq, j, /):
        return cls(seq, j)
    def __init__(sf, seq, j, /):
        assert 0 <= j <= len(seq)
        sf._ls = seq
        sf._j = j
    def __repr__(sf, /):
        return repr_helper(sf, sf.seq, sf.xidx)
    @property
    def seq(sf, /):
        return sf._ls
    @property
    def xidx(sf, /):
        return sf._j
    @override
    def ___xnext4reproduceable___(sf, /):
        ls = sf.seq
        j = sf.xidx
        if j == len(ls):
            return StopEx(j)
        cls = type(sf)
        ot = cls.mk5seq_and_xidx_(ls, 1+j)
        return NextEx(ls[j], ot)


class Reproduceable7chain5iterable(IReproduceable):
    'Iter IReproduceable{x} -> IReproduceable{x}'
    ###############
    #vs:Reproduceable7chain5iterable
    #vs:Reproduceable7chain5reproduceable
    ###############
    ___no_slots_ok___ = True
    @classmethod
    def mk5lflnkls4reproduceable_(cls, lflnkls4reproduceable, /):
        return cls(lflnkls4reproduceable, is_lflnkls=True)
    def __init__(sf, reproduceables, /, *, is_lflnkls=False):
        lflnkls4reproduceable = reproduceables if is_lflnkls else lflnkls5reversed_iterable(force_reversed(reproduceables))
        sf._s = lflnkls4reproduceable
    def __repr__(sf, /):
        return repr_helper(sf, sf.list_reproduceables_())
    @property
    def _lflnkls4reproduceable_(sf, /):
        return sf._s
    def iter_reproduceables_(sf, /):
        return lflnkls2iterable(sf._lflnkls4reproduceable_)
    def list_reproduceables_(sf, /):
        return list(sf.iter_reproduceables_())
    @CachedProperty
    def _hway_xnext_(sf, /):
        _0_lflnk = sf._lflnkls4reproduceable_
        y = None
        while _0_lflnk:
            (_1_lflnk, rp) = lflnkls_ipop_left(_0_lflnk)
            match xnext4reproduceable_(rp):
                case NextEx(x, _rp):
                    #bug:_2_lflnk = lflnkls_ipush_left(_1_lflnk, _rp)
                    (_2_lflnk, _None) = lflnkls_ipush_left(_1_lflnk, _rp)
                    return (x, _2_lflnk)
                case StopEx(y):
                    _0_lflnk = _1_lflnk
                    continue
                case bad:
                    raise TypeError(bad)
            #end-match xnext4reproduceable_(rp):
            raise 000
        #end-while 1:
        return (y,)
    @override
    def ___xnext4reproduceable___(sf, /):
        match sf._hway_xnext_:
            case (x, _2_lflnk):
                cls = type(sf)
                ot = cls.mk5lflnkls4reproduceable_(_2_lflnk)
                return NextEx(x, ot)
            case (y,):
                return StopEx(y)
        raise 000
class Reproduceable7chain5reproduceable(IReproduceable):
    'IReproduceable{IReproduceable{x}} -> IReproduceable{x}'
    ###############
    #vs:Reproduceable7chain5iterable
    #vs:Reproduceable7chain5reproduceable
    ###############
    # use Reproduceable5seq => [IReproduceable{x}] -> IReproduceable{IReproduceable{x}}
    # use Reproduceable7fmap => (a -> IReproduceable{x}) -> IReproduceable{a} -> IReproduceable{IReproduceable{x}}
    ___no_slots_ok___ = True
    @classmethod
    def mk5may_head_and_tail_reproduceable_(cls, may_head_reproduceable, tail_reproduceable4reproduceable, /):
        return cls(may_head_reproduceable, tail_reproduceable4reproduceable)
    def __init__(sf, may_head_reproduceable, tail_reproduceable4reproduceable, /):
        check_may_([check_type_le, IReproduceable], may_head_reproduceable)
        check_type_le(IReproduceable, tail_reproduceable4reproduceable)
        sf._mh = may_head_reproduceable
        sf._tl = tail_reproduceable4reproduceable
    def __repr__(sf, /):
        return repr_helper(sf, sf.may_head_reproduceable, sf.tail_reproduceable4reproduceable)
    @property
    def may_head_reproduceable(sf, /):
        return sf._mh
    @property
    def tail_reproduceable4reproduceable(sf, /):
        return sf._tl
    def list_reproduceables_(sf, /):
        return list(sf.iter_reproduceables_())
    def iter_reproduceables_(sf, /):
        if not None is (head_reproduceable:=sf.may_head_reproduceable):
            yield head_reproduceable
        yield from iter_fsts4reproduceable_(sf.tail_reproduceable4reproduceable)
        return
    def iter_head_and_tail_reproduceable_pairs_(sf, /):
        if not None is (head_reproduceable:=sf.may_head_reproduceable):
            yield (head_reproduceable, sf.tail_reproduceable4reproduceable)
        yield from iter_pairs4reproduceable_(sf.tail_reproduceable4reproduceable)
        return
    @CachedProperty
    def _hway_xnext_(sf, /):
        y = None
        for (head, tail) in sf.iter_head_and_tail_reproduceable_pairs_():
            match xnext4reproduceable_(head):
                case NextEx(x, _head):
                    return (x, _head, tail)
                case StopEx(y):
                    continue
                case bad:
                    raise TypeError(bad)
            #end-match xnext4reproduceable_(head):
            raise 000
        #end-for...:
        return (y,)
    @override
    def ___xnext4reproduceable___(sf, /):
        match sf._hway_xnext_:
            case (x, _head, tail):
                cls = type(sf)
                ot = cls.mk5may_head_and_tail_reproduceable_(_head, tail)
                    # [_head never be None]
                    # i.e. [head be None => at beginning]
                return NextEx(x, ot)
            case (y,):
                return StopEx(y)
        raise 000

class IReproduceable7fmap(IReproduceable):
    '(x->y) -> IReproduceable{x} -> IReproduceable{y}'
    __slots__ = ()
    '(IN[j]->OUT[j]) -> IReproduceable{as IN[0:]} -> IReproduceable{as OUT[0:]}'
    @property
    @abstractmethod
    def reproduceable8input(sf, /):
        '-> IReproduceable{as IN[0:]} # vs: [sf :: IReproduceable{as OUT[0:]}]'
    @abstractmethod
    def transform7fmap_(sf, IN_j, /):
        'IN[j] -> OUT[j]'
        # vs:transform7stated_
        # vs:transform7fmap_#stateless
    @abstractmethod
    def mk5reproduceable8tail_input_(sf, reproduceable8tail_input, /):
        'IReproduceable{as IN[j:]} -> IReproduceable{as OUT[j:]}'
    def transform4result7fmap_(sf, result, /):
        'result6IN -> result6OUT'
        return result
    @override
    def ___xnext4reproduceable___(sf, /):
        rp = sf.reproduceable8input
        match xnext4reproduceable_(rp):
            case NextEx(x, _rp):
                y = sf.transform7fmap_(x)
                ot = sf.mk5reproduceable8tail_input_(_rp)
                return NextEx(y, ot)
            case StopEx(z):
                _z = sf.transform4result7fmap_(z)
                return StopEx(_z)
            case bad:
                raise TypeError(bad)
        #end-match xnext4reproduceable_(rp):
        raise 000




class IReproduceable7transform(IReproduceable):
    'st -> (st->x->(y,st)) -> IReproduceable{x} -> IReproduceable{y}'
    __slots__ = ()
    r'''[[[
    #########
    use Reproduceable7chain5iterable+Reproduceable5seq to include st_0/(x_0mm|y_0mm)
    #########
    st_0 -> (st_j->IN_j->(OUT_j,st_jpp)) -> IReproduceable{IN} -> IReproduceable{OUT}
        * [y_0mm:=st_0][y_jmm:=st_j][y_j:=IN_j][OUT_j:=dy_j{y_j-y_jmm}][st_jpp:=y_j]
        * [x_0mm:=st_0][x_jmm:=st_j][y_j:=IN_j][OUT_j:=x_j][st_jpp:=x_j]
    #########
    ==>>:
    y_0mm -> (y_jmm->y_j->dy_j) -> IReproduceable{y} -> IReproduceable{dy}
    x_0mm -> (x_jmm->y_j->x_j) -> IReproduceable{y} -> IReproduceable{x}
        f(x,y):=pow_(x,y)
            # @stage1
        g(x,y):=mul_(x,cached_pow_(x_0mm,y))
            # @stage2
    #########

    #]]]'''#'''
    @property
    @abstractmethod
    def reproduceable8input(sf, /):
        '-> IReproduceable{as IN[0:]} # vs: [sf :: IReproduceable{as OUT[0:]}]'
    @property
    @abstractmethod
    def initial_state(sf, /):
        '-> st[0]'
    @abstractmethod
    def transform7stated_(sf, st_j, IN_j, /):
        'st[j] -> IN[j] -> (OUT[j], st[1+j])'
        # vs:transform7stated_
        # vs:transform7fmap_#stateless
    @abstractmethod
    def mk5tail_state_and_reproduceable8tail_input_(sf, tail_state, reproduceable8tail_input, /):
        'st[j] -> IReproduceable{as IN[j:]} -> IReproduceable{as OUT[j:]}'
    def transform4result7stated_(sf, st, result, /):
        'st -> result6IN -> result6OUT'
        return (st, result)
    @override
    def ___xnext4reproduceable___(sf, /):
        st_0 = sf.initial_state
        rp = sf.reproduceable8input
        match xnext4reproduceable_(rp):
            case NextEx(x, _rp):
                (y, st_1) = sf.transform7stated_(st_0, x)
                ot = sf.mk5tail_state_and_reproduceable8tail_input_(st_1, _rp)
                return NextEx(y, ot)
            case StopEx(z):
                _z = sf.transform4result7stated_(st_0, z)
                return StopEx(_z)
            case bad:
                raise TypeError(bad)
        #end-match xnext4reproduceable_(rp):
        raise 000
class IReproduceable7rdiff(IReproduceable7transform):
    'x -> (x->x->dx) -> IReproduceable{x} -> IReproduceable{dx} # flip __sub__'
    __slots__ = ()
    @abstractmethod
    def rdiff_(sf, IN_jmm, IN_j, /):
        'IN[j-1] -> IN[j] -> OUT[j]'
        return IN_j -IN_jmm
    @override
    def transform7stated_(sf, st_j, IN_j, /):
        'st[j] -> IN[j] -> (OUT[j], st[1+j])'
        IN_jmm = st_j
        OUT_j = sf.rdiff_(IN_jmm, IN_j)
        st_jpp = IN_j
        return (OUT_j, st_jpp)


class IReproduceable7foldl(IReproduceable7transform):
    'z -> (z->x->z) -> IReproduceable{x} -> IReproduceable{z}'
    __slots__ = ()
    @abstractmethod
    def ljoin_(sf, OUT_jmm, IN_j, /):
        'OUT[j-1] -> IN[j] -> OUT[j]'
        return OUT_jmm +IN_j
    @override
    def transform7stated_(sf, st_j, IN_j, /):
        'st[j] -> IN[j] -> (OUT[j], st[1+j])'
        OUT_jmm = st_j
        OUT_j = sf.ljoin_(OUT_jmm, IN_j)
        st_jpp = OUT_j
        return (OUT_j, st_jpp)

class IReproduceable7transform7init(IReproduceable7transform):
    ___no_slots_ok___ = True
    def __init__(sf, _op_, initial_state, reproduceable8input, /):
        check_callable(_op_)
        check_type_le(IReproduceable, reproduceable8input)
        sf._f = _op_
        sf._st = initial_state
        sf._rp = reproduceable8input
    @property
    @override
    def reproduceable8input(sf, /):
        return sf._rp
    @property
    @override
    def initial_state(sf, /):
        return sf._st
    @property
    @override
    def _op_(sf, /):
        return sf._f
    def __repr__(sf, /):
        return repr_helper(sf, sf._op_, sf.initial_state, sf.reproduceable8input)
    @override
    def mk5tail_state_and_reproduceable8tail_input_(sf, tail_state, reproduceable8tail_input, /):
        cls = type(sf)
        return cls(sf._op_, tail_state, reproduceable8tail_input)





class Reproduceable7fmap(IReproduceable7fmap):
    '(x->y) -> IReproduceable{x} -> IReproduceable{y}'
    #vs:Reproduceable7fmap
    #vs:Reproduceable7transform
    ___no_slots_ok___ = True
    def __init__(sf, transform7fmap_, reproduceable8input, /):
        check_callable(transform7fmap_)
        check_type_le(IReproduceable, reproduceable8input)
        sf._f = transform7fmap_
        sf._rp = reproduceable8input
    @property
    @override
    def reproduceable8input(sf, /):
        return sf._rp
    @property
    @override
    def transform7fmap_(sf, /):
        return sf._f
    def __repr__(sf, /):
        return repr_helper(sf, sf.transform7fmap_, sf.reproduceable8input)
    @override
    def mk5reproduceable8tail_input_(sf, reproduceable8tail_input, /):
        cls = type(sf)
        return cls(sf.transform7fmap_, reproduceable8tail_input)

class Reproduceable7transform(IReproduceable7transform7init):
    'st -> (st->x->(y,st)) -> IReproduceable{x} -> IReproduceable{y}'
    #vs:Reproduceable7fmap
    #vs:Reproduceable7transform
    ___no_slots_ok___ = True
    @property
    @override
    def transform7stated_(sf, /):
        return sf._op_


class Reproduceable7rdiff(IReproduceable7transform7init, IReproduceable7rdiff):
    'x -> (x->x->dx) -> IReproduceable{x} -> IReproduceable{dx} # flip __sub__'
    ___no_slots_ok___ = True
    @property
    @override
    def rdiff_(sf, /):
        return sf._op_
class Reproduceable7foldl(IReproduceable7transform7init, IReproduceable7foldl):
    'z -> (z->x->z) -> IReproduceable{x} -> IReproduceable{z}'
    ___no_slots_ok___ = True
    @property
    @override
    def ljoin_(sf, /):
        return sf._op_


class Reproduceable7repeat(IReproduceable):
    'z -> imay uint -> IReproduceable{z}'
    ___no_slots_ok___ = True
    def __init__(sf, OUT, imay_size, /):
        check_int_ge(-1, imay_size)
        sf._o = OUT
        sf._im = imay_size
    @property
    def the_oresult(sf, /):
        return sf._o
    @property
    def imay_size(sf, /):
        return sf._im
    def __repr__(sf, /):
        return repr_helper(sf, sf.the_oresult, sf.imay_size)
    def mk5imay_size_(sf, imay_size, /):
        cls = type(sf)
        return cls(sf.the_oresult, imay_size)
    @override
    def ___xnext4reproduceable___(sf, /):
        OUT = sf.the_oresult
        imay_size = sf.imay_size
        if imay_size > 0:
            ot = sf.mk5imay_size_(imay_size-1)
        elif imay_size == 0:
            return StopEx(OUT)
        else:
            # [imay_size == -1]
            ot = sf
        ot
        return NextEx(OUT, ot)



class IReproduceable7wrapper(IReproduceable):
    __slots__ = ()
    @property
    @abstractmethod
    def the_wrapped_reproduceable(sf, /):
        '-> IReproduceable{as OUT[0:]}'
    @abstractmethod
    def mk5tail_reproduceable7wrapped_(sf, tail_reproduceable7wrapped, /):
        'IReproduceable{as OUT[j:]} -> IReproduceable{as OUT[j:]}'
    @override
    def ___xnext4reproduceable___(sf, /):
        r = xnext4reproduceable_(sf.the_wrapped_reproduceable)
        match r:
            case NextEx(x, tail7wrapped):
                tail = sf.mk5tail_reproduceable7wrapped_(tail7wrapped)
                return r if tail is tail7wrapped else NextEx(x, tail)
            case _:
                return r
        raise 000
class Reproduceable7customized_repr(IReproduceable7wrapper):
    ___no_slots_ok___ = True
    def __init__(sf, repr4reproduceable7wrapped_, reproduceable7wrapped, /):
        check_callable(repr4reproduceable7wrapped_)
        check_type_le(IReproduceable, reproduceable7wrapped)
        sf._f = repr4reproduceable7wrapped_
        sf._rp = reproduceable7wrapped
    @property
    def repr4reproduceable7wrapped_(sf, /):
        return sf._f
    @property
    @override
    def the_wrapped_reproduceable(sf, /):
        return sf._rp
    def __repr__(sf, /):
        s = sf.repr4reproduceable7wrapped_(sf.the_wrapped_reproduceable)
        check_type_is(str, s)
        return s
    def __str__(sf, /):
        return repr_helper(sf, sf.repr4reproduceable7wrapped_, sf.the_wrapped_reproduceable)
    @override
    def mk5tail_reproduceable7wrapped_(sf, tail_reproduceable7wrapped, /):
        cls = type(sf)
        return cls(sf.repr4reproduceable7wrapped_, tail_reproduceable7wrapped)

class Reproduceable7cached_oresult(IReproduceable7wrapper):
    ___no_slots_ok___ = True
    def __init__(sf, reproduceable7wrapped, /):
        check_type_le(IReproduceable, reproduceable7wrapped)
        sf._m = None#(Either exit_status, oresult)
        sf._rp = reproduceable7wrapped
    #@CachedProperty
    @property
    def xresult(sf, /):
        m = sf._m
        if None is m:
            xnext4reproduceable_(sf)
            m = sf._m
        return m
    @property
    def tmay_oresult(sf, /):
        match sf.xresult:
            case (True, oresult):
                return (oresult,)
            case (False, exit_status):
                return ()
        raise 000
    @property
    def tmay_exit_status(sf, /):
        match sf.xresult:
            case (True, oresult):
                return ()
            case (False, exit_status):
                return (exit_status,)
        raise 000
    @property
    def exit_status(sf, /):
        for exit_status in sf.tmay_exit_status:
            return exit_status
        raise ValueError
    @property
    def oresult(sf, /):
        for oresult in sf.tmay_oresult:
            return oresult
        raise ValueError
    @property
    @override
    def the_wrapped_reproduceable(sf, /):
        return sf._rp
    def __repr__(sf, /):
        return repr_helper(sf, sf.the_wrapped_reproduceable)
    @override
    def mk5tail_reproduceable7wrapped_(sf, tail_reproduceable7wrapped, /):
        cls = type(sf)
        return cls(tail_reproduceable7wrapped)
    @override
    def ___xnext4reproduceable___(sf, /):
        r = super().___xnext4reproduceable___()
        if None is sf._m:
            match r:
                case NextEx(oresult):
                    either = (True, oresult)
                case StopEx(exit_status):
                    either = (False, exit_status)
                case bad:
                    raise TypeError(bad)
            either
            sf._m = either
        return r

class Reproduceable7tmay_prev_oresult(IReproduceable):
    ___no_slots_ok___ = True
    def __init__(sf, tmay_prev_oresult, reproduceable7wrapped, /):
        check_tmay(tmay_prev_oresult)
        check_type_le(IReproduceable, reproduceable7wrapped)
        #sf._pv = prev_oresult
        sf._tm_pv = tmay_prev_oresult
        sf._rp = reproduceable7wrapped
    def __repr__(sf, /):
        return repr_helper(sf, sf.tmay_prev_oresult, sf.the_wrapped_reproduceable)
    @property
    def tmay_prev_oresult(sf, /):
        return sf._tm_pv
    @property
    def prev_oresult(sf, /):
        for prev_oresult in sf.tmay_prev_oresult:
            return prev_oresult
        raise ValueError
    @property
    def the_wrapped_reproduceable(sf, /):
        '-> IReproduceable{as OUT[0:]}'
        return sf._rp
    def mk5curr_oresult_and_tail_reproduceable7wrapped_(sf, curr_oresult, tail_reproduceable7wrapped, /):
        'IReproduceable{as OUT[j:]} -> IReproduceable{as OUT[j:]}'
        cls = type(sf)
        return cls((curr_oresult,), tail_reproduceable7wrapped)
    @override
    def ___xnext4reproduceable___(sf, /):
        r = xnext4reproduceable_(sf.the_wrapped_reproduceable)
        match r:
            case NextEx(x, tail7wrapped):
                tail = sf.mk5curr_oresult_and_tail_reproduceable7wrapped_(x, tail7wrapped)
                return NextEx(x, tail)
            case _:
                return r
        raise 000


__all__
from seed.abc.IReproduceable import is_reproduceable_, check_reproduceable_
from seed.abc.IReproduceable import xnext4reproduceable_, xnext4reproduceable7check_, check_result5xnext4reproduceable_
from seed.abc.IReproduceable import NextEx, StopEx, ResultTypes4xnext

from seed.abc.IReproduceable import iter_pairs4reproduceable_, iter_fsts4reproduceable_, iter_snds4reproduceable_
from seed.abc.IReproduceable import Iter4IReproduceable
from seed.abc.IReproduceable import IReproduceable, IReproduceable7fmap, IReproduceable7transform, IReproduceable7transform7init, IReproduceable7rdiff, IReproduceable7foldl, IReproduceable7wrapper
from seed.abc.IReproduceable import Reproduceable5seq, Reproduceable7chain5iterable, Reproduceable7chain5reproduceable, Reproduceable7fmap, Reproduceable7transform, Reproduceable7rdiff, Reproduceable7foldl, Reproduceable7repeat, Reproduceable7customized_repr, Reproduceable7cached_oresult, Reproduceable7tmay_prev_oresult
from seed.abc.IReproduceable import *
