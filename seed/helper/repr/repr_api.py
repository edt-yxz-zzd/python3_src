
r'''
e ../../python3_src/seed/helper/repr/repr_api.py
py -m seed.helper.repr.repr_api


#allow eq obj with diff repr
# 0.0 == -0.0
# sorted by obj and sorted by repr_result are diff!!!
#   sorted by repr_result is used for std repr of unordered collection

repr_handler :: object -> IReprResult
IReprResult <: Ord
IReprResult <: Hash

obj is not recur
IReprResult obj is not recur

IReprHandler <: Hash
IReprHandler obj is not recur, but should mimic recur

view ../../python3_src/seed/helper/check/check.py
#'''

from seed.abc.IComparable import IComparable, compare, ITypeComparable, type_compare, check_compare_result, int2compare_result, compare_by_lt_eq
from seed.abc.IGetArgsKwargs import IGetArgsKwargs
from seed.abc.IImmutableHelper import IImmutableHelper
from seed.abc.IReprImmutableHelper import IReprImmutableHelper
from seed.abc.abc import abstractmethod, override, not_implemented
from seed.lang.class_property import class_property
from seed.tiny import is_iterator, is_reiterable, fst, snd, MapView




from seed.types.Tester import is_good, ITester, the_Tester_True
from seed.types.SinkTester import SinkTester
from seed.types.SinkTester import BaseTester, base_assert, base_test
from seed.types.SinkTester import BaseTesterError, BaseTesterError4then, BaseTesterError4if



from seed.math.complex import unbox_complex, std_float, std_complex


import inspect#isabstract
import math, cmath #isfinite, isnan, isinf
import cmath #inf, infj, nan, nanj :: float
import math #inf, nan :: float
import keyword



from collections.abc import Mapping, Set, Sequence
from collections.abc import Container, Iterable
from seed.helper.check.check import IChecker, mk_checker, check, verify, CheckFail, CheckError, CheckException
from seed.helper.check.check import mk_checker__point, mk_checker__pair
from seed.helper.check.check import (
    check_int
    ,check_instance
    ,check_instance_all
    ,check_type_is
    ,check_tuple

    #,check_Lookupable
    #,check_namedtuple_type
    #,check_has_attrs
    #,check_callable
    #,check_subclass

    #,check_len_eq
    #,check_iterable
    #,check_type_tree
    )


from seed.helper.check.checkers import (
    checkers
    ,checks
    ,check_
    ,check_int_ge_neg1
    ,check_bool
    ,check_uint
    ,check_iterator

    ,check_type_is
    ,check_instance
    ,check_instance_all
    ,check_instance_or_None
    ,check_mapping
    ,check_tuple

    ,check_pairs_of
    ,check_sorted
    ,check_all
    ,check_pair
    ,check_int
    ,check_str
    ,check_bytes
    ,check_float
    ,check_complex
    ,check_finite_float #math.isfinite
    ,check_finite_complex #cmath.isfinite
    )


###################




check_
check_int_ge_neg1
check_bool
check_uint
check_iterator

check_type_is
check_instance
check_instance_all
check_instance_or_None
check_mapping
check_tuple

check_pairs_of
check_sorted
check_all
check_pair
check_int
check_str
check_bytes
check_float
check_complex
check_finite_float #math.isfinite
check_finite_complex #cmath.isfinite





check_depth = check_int_ge_neg1
check_identifier = checkers.identifier # <: check_module <: check_str

fst, snd
MapView
the_Tester_True
Mapping

def check_key2repr_handler(key2repr_handler4recur):
    check_mapping(key2repr_handler4recur)
    check_instance_all(IReprHandler, key2repr_handler4recur.values())








def _mk_repr_result_(repr_handler, id2ancestor, key2repr_handler4recur, obj):
    return type(repr_handler)._mk_repr_result_(repr_handler, id2ancestor, key2repr_handler4recur, obj)
def _verify__depth_(repr_handler, id2ancestor, key2repr_handler4recur, depth, obj):
    return type(repr_handler)._verify__depth_(repr_handler, id2ancestor, key2repr_handler4recur, depth, obj)

class IReprHandler(IReprImmutableHelper):
    r'''
    repr worker

    depth: -1 +inf recur; 0 only self shallow

    why verify not check?
        since id2ancestor

    to impl ___verify__depth___
        call globals._verify__depth_ inside ___verify__depth___ for recur
    recur:
        ___verify__depth___
            globals._verify__depth_
        ___mk_repr_result___
            globals._mk_repr_result_
        ##above work on outer data which may recur
        ___iter_imported_keys__may_repeat__depth___
            recur on handler, not deref ref
            since handler is immutable, it can not recur to self, depth finite

    #'''
    #def ___get_args_kwargs___(sf):
    @abstractmethod
    def ___verify__depth___(sf, id2ancestor, key2repr_handler4recur, depth, obj):
        'id2ancestor -> key2repr_handler4recur -> [-1..] -> obj -> bool'
    r'''
    why verify not check?
        since id2ancestor
    @abstractmethod
    def ___check__depth___(sf, id2ancestor, key2repr_handler4recur, depth, obj):
        'id2ancestor -> key2repr_handler4recur -> [-1..] -> obj -> None|raise CheckFail'
    #'''
    @abstractmethod
    def ___iter_imported_keys__may_repeat__depth___(sf, depth):
        '[-1..] -> Iter key'
    @abstractmethod
    def ___mk_repr_result___(sf, id2ancestor, key2repr_handler4recur, obj):
        'id2ancestor -> key2repr_handler4recur -> obj -> IReprResult'



    def verify__shallow(sf, key2repr_handler4recur, obj):
        'key2repr_handler4recur -> obj -> bool'
        return sf.verify__depth(key2repr_handler4recur, 0, obj)
    def verify__deep(sf, key2repr_handler4recur, obj):
        'key2repr_handler4recur -> obj -> bool'
        return sf.verify__depth(key2repr_handler4recur, -1, obj)
    def verify__depth(sf, key2repr_handler4recur, depth, obj):
        'key2repr_handler4recur -> [-1..] -> obj -> bool'
        check_depth(depth)
        id2ancestor = {}
        b = _verify__depth_(sf, id2ancestor, key2repr_handler4recur, depth, obj)
        assert not id2ancestor
        check_bool(b)
        return b
    def _verify__depth_(sf, id2ancestor, key2repr_handler4recur, depth, obj):
        'id2ancestor -> key2repr_handler4recur -> [-1..] -> obj -> bool'
        me = id(sf)
        if me in id2ancestor: raise ValueError('obj recur')
        id2ancestor[me] = sf
        try:
            return type(sf).___verify__depth___(sf, id2ancestor, key2repr_handler4recur, depth, obj)
        finally:
            del id2ancestor[me]
    def iter_imported_keys__may_repeat__shallow(sf):
        '-> Iter key'
        return sf.iter_imported_keys__may_repeat__depth(0)
    def iter_imported_keys__may_repeat__deep(sf):
        '-> Iter key'
        return sf.iter_imported_keys__may_repeat__depth(-1)
    def iter_imported_keys__may_repeat__depth(sf, depth):
        '[-1..] -> Iter key'
        check_depth(depth)
        it = type(sf).___iter_imported_keys__may_repeat__depth___(sf, depth)
        check_iterator(it)
        return it
    def mk_repr_result(sf, key2repr_handler4recur, obj):
        'key2repr_handler4recur -> obj -> IReprResult'
        check_key2repr_handler(key2repr_handler4recur)
        check_(sf.verify__deep, key2repr_handler4recur, obj)
        id2ancestor = {}
        repr_result = _mk_repr_result_(sf, id2ancestor, key2repr_handler4recur, obj)
        assert not id2ancestor
        check_instance(IReprResult, repr_result)
        return repr_result
    def _mk_repr_result_(sf, id2ancestor, key2repr_handler4recur, obj):
        'id2ancestor -> key2repr_handler4recur -> obj -> IReprResult'
        me = id(sf)
        if me in id2ancestor: raise ValueError('obj recur')
        id2ancestor[me] = sf
        try:
            return type(sf).___mk_repr_result___(sf, id2ancestor, key2repr_handler4recur, obj)
        finally:
            del id2ancestor[me]
class ReprHandler__ref(IReprHandler):
    r'''
    ref = key
    #'''
    def __init__(sf, key):
        sf.__ref = key
    @property
    def ref(sf):
        return sf.__ref
    @override
    def ___get_args_kwargs___(sf):
        return [sf.__ref], {}

    def get_repr_handler(sf, key2repr_handler4recur):
        'key2repr_handler4recur -> IReprHandler'
        keys = set()
        while 1:
            key = sf.ref
            if key in keys: raise ValueError(f'recur ReprHandler__ref: {key!r}')
            keys.add(key)

            repr_handler = key2repr_handler4recur[key]
            if isinstance(repr_handler, __class__):
                sf = repr_handler
            elif not isinstance(repr_handler, IReprHandler): raise TypeError
            else:
                return repr_handler

    @override
    def ___verify__depth___(sf, id2ancestor, key2repr_handler4recur, depth, obj):
        'id2ancestor -> key2repr_handler4recur -> [-1..] -> obj -> bool'
        repr_handler = sf.get_repr_handler(key2repr_handler4recur)
        return _verify__depth_(repr_handler, id2ancestor, key2repr_handler4recur, depth, obj)

    @override
    def ___iter_imported_keys__may_repeat__depth___(sf, depth):
        '[-1..] -> Iter key'
        yield sf.ref
    @override
    def ___mk_repr_result___(sf, id2ancestor, key2repr_handler4recur, obj):
        'id2ancestor -> key2repr_handler4recur -> obj -> IReprResult'
        repr_handler = sf.get_repr_handler(key2repr_handler4recur)
        return _mk_repr_result_(repr_handler, id2ancestor, key2repr_handler4recur, obj)


class IReprHandler__not_ref(IReprHandler):
    @abstractmethod
    def ___iter_repr_handlers__may_repeat__shallow___(sf):
        '-> Iter IReprHandler; depth==0'
    @override
    def ___iter_imported_keys__may_repeat__depth___(sf, depth):
        '[-1..] -> Iter key'
        if depth > 0:
            depth -= 1
        elif depth == 0:
            return

        it = type(sf).___iter_repr_handlers__may_repeat__shallow___(sf)
        for repr_handler in it:
            yield from repr_handler.iter_imported_keys__may_repeat__depth(depth)


BaseTester
base_test

class ReprHandler__union(IReprHandler__not_ref):
    r'''
    [(BaseTester, IReprHandler)]
    ordered, test from left to right, take first
    #'''
    def __init__(sf, tester_handler_pairs):
        check_tuple(tester_handler_pairs)
        check_pairs_of(BaseTester, IReprHandler, tester_handler_pairs)
        sf.__ps = tester_handler_pairs
    @property
    def tester_handler_pairs(sf):
        return sf.__ps

    @override
    def ___get_args_kwargs___(sf):
        return [sf.__ps], {}
    def get_may_repr_handler(sf, obj):
        for base_tester, repr_handler in sf.tester_handler_pairs:
            if base_test(base_tester, obj):
                break
        else:
            return ()
        return (repr_handler,)
    @override
    def ___iter_repr_handlers__may_repeat__shallow___(sf):
        '-> Iter IReprHandler'
        return map(snd, sf.tester_handler_pairs)
    @override
    def ___verify__depth___(sf, id2ancestor, key2repr_handler4recur, depth, obj):
        'id2ancestor -> key2repr_handler4recur -> [-1..] -> obj -> bool'
        may_repr_handler = sf.get_may_repr_handler(obj)
        if may_repr_handler:
            [repr_handler] = may_repr_handler
        else:
            return False

        repr_handler
        if depth > 0:
            depth -= 1
        elif depth == 0:
            return True

        return _verify__depth_(repr_handler, id2ancestor, key2repr_handler4recur, depth, obj)

    @override
    def ___mk_repr_result___(sf, id2ancestor, key2repr_handler4recur, obj):
        'id2ancestor -> key2repr_handler4recur -> obj -> IReprResult'
        may_repr_handler = sf.get_may_repr_handler(obj)
        if may_repr_handler:
            [repr_handler] = may_repr_handler
        else:
            raise TypeError

        repr_handler
        return _mk_repr_result_(repr_handler, id2ancestor, key2repr_handler4recur, obj)



class ReprHandler__dict(IReprHandler__not_ref):
    'arbitrary Mapping show as py builtin dict'
    def __init__(sf, may_item_tester, key_repr_handler, value_repr_handler):
        if may_item_tester is None:
            item_tester = the_Tester_True
        else:
            item_tester = may_item_tester
            check_instance(BaseTester, item_tester)
        del item_tester

        check_instance(IReprHandler, key_repr_handler)
        check_instance(IReprHandler, value_repr_handler)
        sf.__may_item_tester = may_item_tester
        sf.__key_repr_handler = key_repr_handler
        sf.__value_repr_handler = value_repr_handler
    @property
    def may_item_tester(sf):
        return sf.__may_item_tester
    @property
    def key_repr_handler(sf):
        return sf.__key_repr_handler
    @property
    def value_repr_handler(sf):
        return sf.__value_repr_handler
    def get_item_tester(sf):
        may_item_tester = sf.__may_item_tester
        if may_item_tester is None:
            item_tester = the_Tester_True
        else:
            item_tester = may_item_tester
        return item_tester

    @override
    def ___get_args_kwargs___(sf):
        return [sf.may_item_tester, sf.key_repr_handler, sf.value_repr_handler], {}

    @override
    def ___iter_repr_handlers__may_repeat__shallow___(sf):
        '-> Iter IReprHandler'
        yield sf.key_repr_handler
        yield sf.value_repr_handler

    @override
    def ___verify__depth___(sf, id2ancestor, key2repr_handler4recur, depth, obj):
        'id2ancestor -> key2repr_handler4recur -> [-1..] -> obj -> bool'
        item_tester = sf.get_item_tester()
        if not isinstance(obj, Mapping):
            return False
        if not (isinstance(item_tester, Tester_True) or all(base_test(item_tester, item) for item in obj.items())):
            return False

        if depth > 0:
            depth -= 1
        elif depth == 0:
            return True

        handlers = [sf.key_repr_handler, sf.value_repr_handler]
        xss = [obj.keys(), obj.values()]
        for repr_handler, xs in zip(handlers, xss):
            _verify__depth_ = type(repr_handler)._verify__depth_
            if not all(
                _verify__depth_(repr_handler, id2ancestor, key2repr_handler4recur, depth, x)
                for x in xs):
                return False
        return True

    @override
    def ___mk_repr_result___(sf, id2ancestor, key2repr_handler4recur, obj):
        'id2ancestor -> key2repr_handler4recur -> obj -> IReprResult'
        kh = sf.key_repr_handler
        vh = sf.value_repr_handler
        items = [
            (_mk_repr_result_(kh, id2ancestor, key2repr_handler4recur, k)
            ,_mk_repr_result_(vh, id2ancestor, key2repr_handler4recur, v)
            )
            for k, v in obj.items()
            ]
        items.sort()
        sorted_items = (*items,)
        return ReprResult__dict(sorted_items)


































class IReprToken(IReprImmutableHelper):
    r'''
    ReprToken__literal
    ReprToken__open
    ReprToken__close
    ReprToken__sep  ,.:=
    ReprToken__op
        ReprToken__op_kw # if/else
        ReprToken__op_not_kw # ^/&/...
    #number sign is neither op nor sep; should have no space follows
    #'''

class IReprToken_one_arg(IReprToken):
    def __new__(cls, s:str):
        check_str(s)
        sf = super().__new__(cls)
        sf.__s = s
    @property
    def arg(sf):
        return sf.__s
    @override
    def ___get_args_kwargs___(sf):
        return [sf.__s], {}
class ReprToken__literal(IReprToken_one_arg):pass
class ReprToken__open(IReprToken_one_arg):pass
class ReprToken__close(IReprToken_one_arg):pass
class ReprToken__sep(IReprToken_one_arg):pass



def _mk_TOKEN():
    d = {
        ReprToken__open:'([{'
        ,ReprToken__close:')]}'
        ,ReprToken__sep:'.,:='
        }
    r = {}
    for mk, s in d.items():
        for ch in s:
            token = mk(ch)
            r[ch] = token
    return MapView(r)
TOKEN = _mk_TOKEN()

def compare_repr_result(lhs, rhs):
    'IReprResult -> IReprResult -> [-1..+1]'
    check_instance(IReprResult, lhs)
    check_instance(IReprResult, rhs)
    return compare(lhs, rhs)

def compare_ordered_repr_results(ls0, ls1):
    diff = len(ls0) - len(ls1)
    if diff:
        return int2compare_result(diff)
    for z, c in zip(ls0, ls1):
        r = compare(z, c)
        if r:
            return r
    return 0


def get_type_idx4repr_sort(cls):
    'type -> uint'
    assert issubclass(cls, IReprResult)
    idx = cls.___get_type_idx4repr_sort___()
    check_uint(idx)
    return idx



#def ___iter_repr_tokens__atom___(sf):
def iter_repr_tokens__atom(repr_result):
    return type(repr_result).___iter_repr_tokens__atom___(repr_result)
#def ___iter_repr_tokens__dot___(sf):
def iter_repr_tokens__dot(repr_result):
    return type(repr_result).___iter_repr_tokens__dot___(repr_result)
#def ___iter_repr_tokens__free___(sf):
def iter_repr_tokens__free(repr_result):
    return type(repr_result).___iter_repr_tokens__free___(repr_result)


iter_repr_tokens__atom
iter_repr_tokens__dot
iter_repr_tokens__free
r'''
def show_inline_normal_(attr, repr_result):
    'repr_result -> str'
    assert isinstance(repr_result, IReprResult)
    cls = type(repr_result)
    s = getattr(cls, attr)(repr_result)
    check_str(s)
    return s
def show_inline_normal(repr_result):
    'repr_result -> str'
    attr = '___show_inline_normal___'
    return show_inline_normal_(attr, repr_result)
def show_inline_normal__atom(repr_result):
    'repr_result -> str'
    attr = '___show_inline_normal__atom___'
    return show_inline_normal_(attr, repr_result)
def show_inline_normal_when_followed_by_dot(repr_result):
    'repr_result -> str'
    attr = '___show_inline_normal_when_followed_by_dot___'
    return show_inline_normal_(attr, repr_result)
#'''

def _get_args(obj):
    args, kwargs = type(obj).___get_args_kwargs___(obj)
    if kwargs: raise logic-err
    return tuple(args)




_IReprResult_subcls2idx = {}
_IReprResult_idx2subcls = {}
class IReprResult(IReprImmutableHelper, ITypeComparable):
    r'''
    result datatype of repr_handler
    #'''
    #def ___get_args_kwargs___(sf):
    #def ___same_type_compare___(sf, other):

    #def ___show_inline_normal___(sf):
    #def ___show_inline_normal_when_followed_by_dot___(sf):
    #def ___show_inline_normal__atom___(cls):

    #def ___iter_repr_tokens__atom___(sf):
    #def ___iter_repr_tokens__free___(sf):
    #def ___iter_repr_tokens__dot___(sf):

    def ___iter_repr_tokens__free___(sf):
        '-> Iter IReprToken'
        return iter_repr_tokens__atom(sf)
    def ___iter_repr_tokens__dot___(sf):
        '-> Iter IReprToken'
        r'''
        1 .xxx
            -> '(1)'
        (-1).xxx
            -> '(-1)'
        >>> -1 .__abs__()
        -1

    should override:
        ReprResult__int
        ReprResult__finite_float
        ReprResult__finite_complex
        #'''
        return iter_repr_tokens__atom(sf)

        #yield from iter_repr_tokens__atom(sf)
        #yield ReprToken__sep('.')

    @abstractmethod
    def ___iter_repr_tokens__atom___(sf):
        '-> Iter IReprToken'
        r'''
        expr(...)
        expr[...]
        -1 ==>> (-1)
        ReprResult__int
        ReprResult__finite_float
        ReprResult__finite_complex
        #'''

    @classmethod
    @abstractmethod
    def ___get_type_idx4repr_sort___(cls):
        '-> uint'
    @classmethod
    @override
    def ___type_compare___(this_cls, other_cls):
        if not issubclass(other_cls, __class__):
            return NotImplemented
        this_idx = get_type_idx4repr_sort(this_cls)
        other_idx = get_type_idx4repr_sort(other_cls)
        r = int2compare_result(this_idx - other_idx)
        #if r == 0 and this_cls is not other_cls:
        return r

    def __init_subclass__(cls, /, **kwargs):
        super().__init_subclass__(**kwargs)
        if not inspect.isabstract(cls):
            idx = get_type_idx4repr_sort(cls)
            if cls in _IReprResult_subcls2idx: raise Exception(cls, idx)
            if idx in _IReprResult_idx2subcls: raise Exception(cls, idx)
            _IReprResult_idx2subcls[idx] = cls
            _IReprResult_subcls2idx[cls] = idx

class IReprResultMixin__idx_by_name(IReprResult):
    __names = '''

    ReprResult____debug__
    ReprResult__None
    ReprResult__False
    ReprResult__True

    ReprResult__module
    ReprResult__var
    ReprResult__attr

    ReprResult__str
    ReprResult__bytes
    ReprResult__int
    ReprResult__finite_float
    ReprResult__finite_complex

    ReprResult__tuple_len_eq_0
    ReprResult__tuple_len_eq_1
    ReprResult__tuple_len_gt_1
    ReprResult__list
    ReprResult__nonempty_set_with_ordered_keys
    ReprResult__nonempty_set
    ReprResult__dict_with_ordered_keys
    ReprResult__dict

    ReprResult__call
    ReprResult__map_key
    ReprResult__map_slice
    ReprResult__map_tuple
        '''.split()
    #ReprResult__empty_set
    #ReprResult__empty_frozenset
    @classmethod
    @override
    def ___get_type_idx4repr_sort___(cls):
        '-> uint'
        return cls.__type_idx4repr_sort

    def __init_subclass__(cls, /, **kwargs):
        if not inspect.isabstract(cls):
            name = cls.__name__
            idx = __class__.__names.index(name)
            cls.__type_idx4repr_sort = idx
        super().__init_subclass__(**kwargs)





class IReprResult4builtins_collection(IReprResultMixin__idx_by_name):
    r'''
    tuple
    list
    nonempty_set
    nonempty_set_with_ordered_keys
    dict
    dict_with_ordered_keys
    #'''
    #not: set()/frozenset()
class ReprResult__dict_with_ordered_keys(IReprResult4builtins_collection):
    def __init__(sf, ordered_repr_result_pairs):
        check_tuple(ordered_repr_result_pairs)
        check_pairs_of(IReprResult, IReprResult, ordered_repr_result_pairs)
        sf.__ps = ordered_repr_result_pairs
    @property
    def ordered_repr_result_pairs(sf):
        return sf.__ps
    @override
    def ___get_args_kwargs___(sf):
        return [sf.__ps], {}
    @override
    def ___same_type_compare___(sf, other):
        ps0 = sf.ordered_repr_result_pairs
        ps1 = other.ordered_repr_result_pairs
        diff = len(ps0) - len(ps1)
        if diff:
            return int2compare_result(diff)
        for xy, ab in zip(ps0, ps1):
            for z, c in zip(xy, ab):
                r = compare(z, c)
                if r:
                    return r
        return 0
    @override
    def ___iter_repr_tokens__atom___(sf):
        '-> Iter IReprToken'
        lsep = TOKEN[',']
        tsep = TOKEN[':']
        f = iter_repr_tokens__free

        yield TOKEN['{']
        if 1:
            ps = sf.ordered_repr_result_pairs
            for i, (k, v) in enumerate(ps):
                if i: yield lsep
                yield from f(k)
                yield tsep
                yield from f(v)
        yield TOKEN['}']
class ReprResult__dict(ReprResult__dict_with_ordered_keys):
    def __init__(sf, sorted_repr_result_pairs):
        super().__init__(sorted_repr_result_pairs)
        check_sorted(sorted_repr_result_pairs)
    @property
    def sorted_repr_result_pairs(sf):
        return sf.ordered_repr_result_pairs

class IReprResult__ordered_repr_results(IReprResult4builtins_collection):
    @classmethod
    @abstractmethod
    def ___get_open_close___(cls):
        '-> (open, closes1)'
    def __init__(sf, ordered_repr_results):
        check_tuple(ordered_repr_results)
        check_instance_all(IReprResult, ordered_repr_results)
        sf.__ls = ordered_repr_results
    @property
    def ordered_repr_results(sf):
        return sf.__ls
    @override
    def ___get_args_kwargs___(sf):
        return [sf.__ls], {}
    @override
    def ___same_type_compare___(sf, other):
        ls0 = sf.ordered_repr_results
        ls1 = other.ordered_repr_results
        return compare_ordered_repr_results(ls0, ls1)
    @override
    def ___iter_repr_tokens__atom___(sf):
        '-> Iter IReprToken'
        lsep = TOKEN[',']
        f = iter_repr_tokens__free
        cls = type(sf)
        (open, closes1) = cls.___get_open_close___()
        assert len(open) == 1
        assert 1 <= len(closes1) <= 2

        yield TOKEN[open]
        if 1:
            ls = sf.ordered_repr_results
            for i, k in enumerate(ls):
                if i: yield lsep
                yield from f(k)
        for close in closes1:
            yield TOKEN[close]



class ReprResult__nonempty_set_with_ordered_keys(IReprResult__ordered_repr_results):
    @classmethod
    @override
    def ___get_open_close___(cls):
        '-> (open, closes1)'
        return ('{', '}')
    def __init__(sf, ordered_repr_results):
        super().__init__(ordered_repr_results)
        if not ordered_repr_results: raise TypeError
class ReprResult__nonempty_set(ReprResult__nonempty_set_with_ordered_keys):
    def __init__(sf, sorted_repr_results):
        super().__init__(sorted_repr_results)
        check_sorted(sorted_repr_results)
    @property
    def sorted_repr_results(sf):
        return sf.ordered_repr_results
class ReprResult__list(IReprResult__ordered_repr_results):
    @classmethod
    @override
    def ___get_open_close___(cls):
        '-> (open, closes1)'
        return ('[', ']')
class ReprResult__tuple_len_eq_0(IReprResult__ordered_repr_results):
    @classmethod
    @override
    def ___get_open_close___(cls):
        '-> (open, closes1)'
        return ('(', ')')
    def __init__(sf):
        super().__init__(())
r'''
class ReprResult__empty_set(IReprResult__ordered_repr_results):
    @classmethod
    @override
    def ___get_open_close___(cls):
        '-> (open, closes1)'
        return ('set(', ')')
    def __init__(sf):
        super().__init__(())
#'''

class ReprResult__tuple_len_gt_1(IReprResult__ordered_repr_results):
    @classmethod
    @override
    def ___get_open_close___(cls):
        '-> (open, closes1)'
        return ('(', ')')
    def __init__(sf, ordered_repr_results):
        super().__init__(ordered_repr_results)
        if not 1 < len(ordered_repr_results): raise TypeError
class ReprResult__tuple_len_eq_1(IReprResult__ordered_repr_results):
    @classmethod
    @override
    def ___get_open_close___(cls):
        '-> (open, closes1)'
        return ('(', ',)')
    def __init__(sf, ordered_repr_results):
        super().__init__(ordered_repr_results)
        if 1 != len(ordered_repr_results): raise TypeError












class IReprResult4builtins_prime(IReprResultMixin__idx_by_name):
    r'''
    str
    bytes
    int
    finite_float
    finite_complex
    #'''
    #(1+2j) not (1 + 2j)
    #not: +- inf|nan    ==>> float('-inf')
    #not: +- infj|nanj  ==>> complex('-inf+nanj')


class ReprResult__str(IReprResult4builtins_prime):
    def __init__(sf, s):
        check_str(s)
        sf.__s = s
    @property
    def str(sf):
        return sf.__s
    @override
    def ___get_args_kwargs___(sf):
        return [sf.__s], {}
    @override
    def ___same_type_compare___(sf, other):
        s0 = sf.str
        s1 = other.str
        return compare_by_lt_eq(s0, s1)
    @override
    def ___iter_repr_tokens__atom___(sf):
        '-> Iter IReprToken'
        yield ReprToken__literal(repr(sf.str))


class ReprResult__bytes(IReprResult4builtins_prime):
    def __init__(sf, s):
        check_bytes(s)
        sf.__s = s
    @property
    def bytes(sf):
        return sf.__s
    @override
    def ___get_args_kwargs___(sf):
        return [sf.__s], {}
    @override
    def ___same_type_compare___(sf, other):
        s0 = sf.bytes
        s1 = other.bytes
        return compare_by_lt_eq(s0, s1)
    @override
    def ___iter_repr_tokens__atom___(sf):
        '-> Iter IReprToken'
        yield ReprToken__literal(repr(sf.bytes))

class ReprResult__int(IReprResult4builtins_prime):
    def __init__(sf, x):
        check_int(x)
        sf.__x = x
    @property
    def int(sf):
        return sf.__x
    @override
    def ___get_args_kwargs___(sf):
        return [sf.__x], {}
    @override
    def ___same_type_compare___(sf, other):
        x0 = sf.int
        x1 = other.int
        return int2compare_result(x0 - x1)
    @override
    def ___iter_repr_tokens__free___(sf):
        '-> Iter IReprToken'
        x = sf.int
        s = f'{x!r}'
        t = ReprToken__literal(s)
        yield t
    @override
    def ___iter_repr_tokens__dot___(sf):
        '-> Iter IReprToken'
        x = sf.int
        #s = f'({x!r}).' # avoid 1.kkk
        s = f'{x!r}'
        t = ReprToken__literal(s)
        yield TOKEN['(']
        yield t
        yield TOKEN[')']
    @override
    def ___iter_repr_tokens__atom___(sf):
        '-> Iter IReprToken'
        x = sf.int
        return _num2tokens(x)
def _num2tokens(x):
    s = f'{x!r}'
    t = ReprToken__literal(s)
    if s.startswith("-"):
        yield TOKEN['(']
        yield t
        yield TOKEN[')']
    else:
        if '-' in s or '+' in s: raise logic-err
        yield t
    #if not (s.startswith("(") or ('-' not in s and '+' not in s)): raise logic-err



class ReprResult__finite_float(IReprResult4builtins_prime):
    def __init__(sf, x):
        check_finite_float(x) #math.isfinite
        #sf.__x = std_float(x)
        sf.__x = (x)
            #allow eq obj with diff repr
            # 0.0 == -0.0
    @property
    def float(sf):
        return sf.__x
    @override
    def ___get_args_kwargs___(sf):
        return [sf.__x], {}
    @override
    def ___same_type_compare___(sf, other):
        x0 = sf.float
        x1 = other.float
        return compare_by_lt_eq(x0, x1)
    @override
    def ___iter_repr_tokens__free___(sf):
        '-> Iter IReprToken'
        x = sf.float
        s = f'{x!r}'
        t = ReprToken__literal(s)
        yield t
    @override
    def ___iter_repr_tokens__atom___(sf):
        '-> Iter IReprToken'
        x = sf.float
        # '-0.0'
        return _num2tokens(x)


class ReprResult__finite_complex(IReprResult4builtins_prime):
    def __init__(sf, x):
        check_finite_complex(x) #cmath.isfinite
        #sf.__x = std_complex(x)
        sf.__x = (x)
            #allow eq obj with diff repr
            # 0.0 == -0.0
    @property
    def complex(sf):
        return sf.__x
    @override
    def ___get_args_kwargs___(sf):
        return [sf.__x], {}
    @override
    def ___same_type_compare___(sf, other):
        x0 = unbox_complex(sf.complex)
        x1 = unbox_complex(other.complex)
        return compare_by_lt_eq(x0, x1)
    @override
    def ___iter_repr_tokens__atom___(sf):
        '-> Iter IReprToken'
        z = sf.complex
        s = f'{z!r}'
        if not (s.startswith("(") or ('-' not in s and '+' not in s and s.endswith("j"))): raise logic-err
        t = ReprToken__literal(s)
        yield t





class ReprResult__module(IReprResultMixin__idx_by_name):
    def __init__(sf, may_module_repr_result, var_repr_result):
        check_instance_or_None(ReprResult__module, may_module_repr_result)
        check_instance(ReprResult__var, var_repr_result)
        sf.__may_pkg = may_module_repr_result
        sf.__nm = var_repr_result
    @property
    def may_module_repr_result(sf):
        return sf.__may_pkg
    @property
    def var_repr_result(sf):
        return sf.__nm
    @override
    def ___get_args_kwargs___(sf):
        return [sf.__may_pkg, sf.__nm], {}
    def __linear(sf):
        m, v = _get_args(sf)
        return (_nmay2tmay(m), v)
    @override
    def ___same_type_compare___(sf, other):
        x0 = sf.__linear()
        x1 = other.__linear()
        return compare_by_lt_eq(x0, x1)


    def __ls_vars(sf):
        it = sf.__iter_reversed_vars()
        ls = [*it]
        ls.reverse()
        return ls
    def __iter_reversed_vars(sf):
        m = sf
        while m is not None:
            m, v = _get_args(m)
            yield v
    @override
    def ___iter_repr_tokens__atom___(sf):
        '-> Iter IReprToken'
        vs = sf.__ls_vars()
        assert vs
        dot = TOKEN['.']
        for i, v in enumerate(vs):
            if i: yield dot
            t = ReprToken__literal(v.var)
            yield t

        #if not s: s = '__builtins__'



class ReprResult__var(IReprResultMixin__idx_by_name):
    r'''identifier/arg/global-var/nonlocal-var/attr
    ELLIPSIS
    NotImplemented
    type
        bool
        BaseException
    builtins_func
    #'''
    if 0:
        def __new__(sf, var:str):
            if var in IReprResult4builtins_constant.names:
                raise ValueError(var)
                #return globals()[f'ReprResult__{var!s}']()
            ...
    def __init__(sf, var:str):
        check_identifier(var)
        sf.__x = var
        if var in IReprResult4builtins_constant.names or keyword.iskeyword(var):
            raise ValueError(var)
    @property
    def var(sf):
        return sf.__x
    @override
    def ___get_args_kwargs___(sf):
        return [sf.__x], {}
    @override
    def ___same_type_compare___(sf, other):
        x0 = (sf.var)
        x1 = (other.var)
        return compare_by_lt_eq(x0, x1)
    @override
    def ___iter_repr_tokens__atom___(sf):
        '-> Iter IReprToken'
        yield ReprToken__literal(sf.var)


class ReprResult__attr(IReprResultMixin__idx_by_name):
    r'''
    module.identifier
    expr.attr
    #qual_name = identifier.attr...
    eg. cmath.nanj
    #'''
    def __init__(sf, baseobj_repr_result, var_repr_result):
        check_instance(IReprResult, baseobj_repr_result)
        check_instance(ReprResult__var, var_repr_result)
        sf.__e = baseobj_repr_result
        sf.__v = var_repr_result
    @property
    def baseobj_repr_result(sf):
        return sf.__e
    @property
    def var_repr_result(sf):
        return sf.__v
    @property
    def attr(sf):
        return sf.__v.var
    @override
    def ___get_args_kwargs___(sf):
        return [sf.__e, sf.__v], {}
    @override
    def ___same_type_compare___(sf, other):
        x0 = _get_args(sf)
        x1 = _get_args(other)
        return compare_by_lt_eq(x0, x1)
    @override
    def ___iter_repr_tokens__atom___(sf):
        '-> Iter IReprToken'
        dot = TOKEN['.']
        f = iter_repr_tokens__dot
        yield from f(sf.baseobj_repr_result)
        yield dot
        yield from f(sf.var_repr_result)
        #yield ReprToken__literal(sf.attr)


class IReprResult4builtins_constant(IReprResultMixin__idx_by_name):
    r'''
    #no "..." # ELLIPSIS
    __debug__
    None
    False
    True
    #'''
    names = tuple('__debug__ None False True'.split())
    #
    @class_property
    #@not_implemented
    #@classmethod
    @abstractmethod
    def the_constant_name(cls):
        raise NotImplementedError
    @override
    def ___get_args_kwargs___(sf):
        return [], {}
    @override
    def ___same_type_compare___(sf, other):
        return 0
    @override
    def ___iter_repr_tokens__atom___(sf):
        '-> Iter IReprToken'
        cls = type(sf)
        yield ReprToken__literal(cls.the_constant_name)


class ReprResult____debug__(IReprResult4builtins_constant):
    the_constant_name = '__debug__'
class ReprResult__None(IReprResult4builtins_constant):
    the_constant_name = 'None'
class ReprResult__False(IReprResult4builtins_constant):
    the_constant_name = 'False'
class ReprResult__True(IReprResult4builtins_constant):
    the_constant_name = 'True'


class ReprResult__call(IReprResultMixin__idx_by_name):
    r'''
    expr(*args, **kwargs)
    #'''
    def __init__(sf, func_repr_result, arg_repr_results, ordered_kwarg_pairs):
        check_instance(IReprResult, func_repr_result)

        check_tuple(arg_repr_results)
        check_instance_all(IReprResult, arg_repr_results)

        check_tuple(ordered_kwarg_pairs)
        check_pairs_of(str, IReprResult, ordered_kwarg_pairs)
            # kw can be arbitrary str!!!
            # but when repr, "kw=arg", require identifier
        check_all(check_identifier, map(fst, ordered_kwarg_pairs))

        sf.__f = func_repr_result
        sf.__xs = arg_repr_results
        sf.__ps = ordered_kwarg_pairs
    @property
    def func_repr_result(sf):
        return sf.__f
    @property
    def arg_repr_results(sf):
        return sf.__xs
    @property
    def ordered_kwarg_pairs(sf):
        return sf.__ps
    @override
    def ___get_args_kwargs___(sf):
        return [sf.__f, sf.__xs, sf.__ps], {}
    @override
    def ___same_type_compare___(sf, other):
        x0 = _get_args(sf)
        x1 = _get_args(other)
        return compare_by_lt_eq(x0, x1)
    @override
    def ___iter_repr_tokens__atom___(sf):
        '-> Iter IReprToken'
        lsep = TOKEN[',']
        eq = TOKEN['=']
        g = iter_repr_tokens__atom
        yield from g(sf.func_repr_result)
        del g

        f = iter_repr_tokens__free
        yield TOKEN['(']
        if 1:
            i = -1
            for i, x in enumerate(sf.arg_repr_results):
                if i: yield lsep
                yield from f(x)
            else:
                i += 1

            for i, (k,v) in enumerate(sf.ordered_kwarg_pairs, i):
                if i: yield lsep
                yield from f(k)
                yield eq
                yield from f(v)
        yield TOKEN[')']



    r'''
class IReprResult4attr(IReprResultMixin__idx_by_name):
    expr.attr
    see: ReprResult__attr
    #'''

class ReprResult__map_key(IReprResultMixin__idx_by_name):
    r'''
    expr[key]
        see: ReprResult__map_key
    expr[?:?:?] #slice
        see: ReprResult__map_slice
    expr[?:?:?, ...] #tuple
        see: ReprResult__map_tuple

>>> class Echo:
...     def __getitem__(sf, k):
...             return k
...
>>> echo = Echo()
>>> echo[1:2,3,4:5,6::7]
(slice(1, 2, None), 3, slice(4, 5, None), slice(6, None, 7))
>>> echo[1]
1
>>> echo[1:]
slice(1, None, None)
>>> echo[:,:]
(slice(None, None, None), slice(None, None, None))
>>> echo[:,]
(slice(None, None, None),)

    #'''
    def __init__(sf, baseobj_repr_result, key_repr_result):
        check_instance(IReprResult, baseobj_repr_result)
        check_instance(IReprResult, key_repr_result)
        sf.__e = baseobj_repr_result
        sf.__k = key_repr_result
    @property
    def baseobj_repr_result(sf):
        return sf.__e
    @property
    def key_repr_result(sf):
        return sf.__k
    @override
    def ___get_args_kwargs___(sf):
        return [sf.__e, sf.__k], {}
    @override
    def ___same_type_compare___(sf, other):
        x0 = _get_args(sf)
        x1 = _get_args(other)
        return compare_by_lt_eq(x0, x1)
    @override
    def ___iter_repr_tokens__atom___(sf):
        '-> Iter IReprToken'
        g = iter_repr_tokens__atom
        yield from g(sf.baseobj_repr_result)
        del g

        f = iter_repr_tokens__free
        yield TOKEN['[']
        yield from f(sf.key_repr_result)
        yield TOKEN[']']



class ReprResult__map_slice(IReprResultMixin__idx_by_name):
    r'''
    expr[key]
        see: ReprResult__map_key
    expr[?:?:?] #slice
        see: ReprResult__map_slice
    expr[?:?:?, ...] #tuple
        see: ReprResult__map_tuple
    #'''
    def __init__(sf, baseobj_repr_result, may_start_repr_result, may_stop_repr_result, may_step_repr_result):
        check_instance(IReprResult, baseobj_repr_result)
        check_instance_or_None(IReprResult, may_start_repr_result)
        check_instance_or_None(IReprResult, may_stop_repr_result)
        check_instance_or_None(IReprResult, may_step_repr_result)

        sf.__x = baseobj_repr_result
        sf.__0 = may_start_repr_result
        sf.__1 = may_stop_repr_result
        sf.__2 = may_step_repr_result
    @property
    def baseobj_repr_result(sf):
        return sf.__x
    @property
    def may_start_repr_result(sf):
        return sf.__0
    @property
    def may_stop_repr_result(sf):
        return sf.__1
    @property
    def may_step_repr_result(sf):
        return sf.__2
    @override
    def ___get_args_kwargs___(sf):
        return [sf.__x, sf.__0, sf.__1, sf.__2], {}
    def __linear(sf):
        x, *ls = _get_args(sf)
        return (x, *map(_nmay2tmay, ls))
    @override
    def ___same_type_compare___(sf, other):
        x0 = sf.__linear()
        x1 = other.__linear()
        return compare_by_lt_eq(x0, x1)

    @override
    def ___iter_repr_tokens__atom___(sf):
        '-> Iter IReprToken'
        g = iter_repr_tokens__atom
        yield from g(sf.baseobj_repr_result)
        del g

        _, *triple = _get_args(sf)

        yield TOKEN['[']
        yield from _slice_triple2tokens(triple)
        yield TOKEN[']']


class ReprResult__map_tuple(IReprResultMixin__idx_by_name):
    r'''
    expr[key]
        see: ReprResult__map_key
    expr[?:?:?] #slice
        see: ReprResult__map_slice
    expr[?:?:?, ...] #tuple
        see: ReprResult__map_tuple


    key1_or_slice3_seq :: [(IReprResult,)|((None|IReprResult),)*3]
    #'''
    def __init__(sf, baseobj_repr_result, key1_or_slice3_seq):
        check_instance(IReprResult, baseobj_repr_result)
        check_tuple(key1_or_slice3_seq)
        check_all(check_tuple, key1_or_slice3_seq)
        if not all(len(ks) in (1,3) for ks in key1_or_slice3_seq): raise TypeError
        for ks in key1_or_slice3_seq:
            L = len(ks)
            if L == 1:
                [key] = ks
                check_instance(IReprResult)
            elif L == 3:
                triple = ks
                for m in triple:
                    check_instance_or_None(IReprResult, m)
            else:
                raise logic-err


        sf.__x = baseobj_repr_result
        sf.__kss = key1_or_slice3_seq
    @property
    def baseobj_repr_result(sf):
        return sf.__x
    @property
    def key1_or_slice3_seq(sf):
        return sf.__kss
    @override
    def ___get_args_kwargs___(sf):
        return [sf.__x, sf.__kss], {}
    def __linear(sf):
        x, kss = _get_args(sf)
        ksss = tuple(((),)+tuple(map(_nmay2tmay, ks)) if len(ks)==3 else (ks,) for ks in kss)
        return (x, len(ksss), ksss)
    @override
    def ___same_type_compare___(sf, other):
        x0 = sf.__linear()
        x1 = other.__linear()
        return compare_by_lt_eq(x0, x1)

    @override
    def ___iter_repr_tokens__atom___(sf):
        '-> Iter IReprToken'
        g = iter_repr_tokens__atom
        yield from g(sf.baseobj_repr_result)
        del g

        kss = (sf.key1_or_slice3_seq)
        f = iter_repr_tokens__free
        lsep = TOKEN[',']
        sz = len(kss)

        yield TOKEN['[']
        if sz == 0:
            yield TOKEN['(']
            yield TOKEN[')']
        else:
            for i, ks in enumerate(kss):
                if i: yield lsep
                if len(ks)==1:
                    [k] = ks
                    yield from f(k)
                else:
                    triple = ks
                    yield from _slice_triple2tokens(triple)
            if sz == 1: yield lsep
        yield TOKEN[']']





def _nmay2tmay(m):
    return () if m is None else (m,)
def _slice_triple2tokens(triple):
    (may_start_repr_result, may_stop_repr_result, may_step_repr_result) = triple
    f = iter_repr_tokens__free
    tsep = TOKEN[':']

    if may_start_repr_result is not None:
        start_repr_result = may_start_repr_result
        yield from f(start_repr_result)

    yield tsep
    if may_stop_repr_result is not None:
        stop_repr_result = may_stop_repr_result
        yield from f(stop_repr_result)

    if may_step_repr_result is not None:
        step_repr_result = may_step_repr_result
        yield tsep
        yield from f(step_repr_result)

r"""
class IReprResult4unary_op(IReprResultMixin__idx_by_name):
    r'''
    (op expr)
    #'''
class IReprResult4binary_op(IReprResultMixin__idx_by_name):
    r'''
    (expr op expr)
    #'''
class IReprResult4trinary_op(IReprResultMixin__idx_by_name):
    r'''
    (expr if expr else expr)
    #'''
class IReprResult4lambda(IReprResultMixin__idx_by_name):
    r'''
    (lambda *args, **kwargs: expr)
    #'''
#"""
#HHHHH
if 1:
    if __name__ == '__main__':
        from seed.helper.print_global_names import print_global_names
        print_global_names(globals())




if __name__ == "__main__":
    import doctest
    doctest.testmod()

#HHHHH




