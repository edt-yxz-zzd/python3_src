#__all__:goto
r'''[[[
e ../../python3_src/seed/math/continued_fraction/convert_to_ContinuedFraction_.py

seed.math.continued_fraction.convert_to_ContinuedFraction_
py -m nn_ns.app.debug_cmd   seed.math.continued_fraction.convert_to_ContinuedFraction_ -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.continued_fraction.convert_to_ContinuedFraction_:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.math.continued_fraction.convert_to_ContinuedFraction_   @f
from seed.math.continued_fraction.convert_to_ContinuedFraction_ import *
]]]'''#'''
__all__ = r'''
mk_ND5or_rational_
convert_to_ContinuedFraction_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
#from seed.helper.lazy_import__func import force_lazy_imported_func_
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from fractions import Fraction
    from seed.tiny_.verify import is_iterator
    from seed.math.continued_fraction.continued_fraction5ND import iter_continued_fraction_digits5ND_
    from seed.math.continued_fraction.prepare_continued_fraction_from_string import prepare_continued_fraction_from_string_
    #def prepare_continued_fraction_from_string_(s, /):
    #    'str/(cf_digits_list_repr|Fraction_repr) -> cf_digits__or__int__or__Fraction/(cf_digits|int|Fraction)'
    from seed.types.LazyList import LazyList
    from seed.math.continued_fraction.continued_fraction_ops____using_LazyList import ContinuedFraction
    from numbers import Rational


#.#################################
___end_mark_of_excluded_global_names__0___ = ...

def mk_ND5or_rational_(rational_or_ND, /):
    '((N,D)|Rational) -> (N,D)'
    #see:convert_to_ContinuedFraction_
    cls = type(rational_or_ND)
    if cls is tuple:
        ND = rational_or_ND
        N, D = ND
    elif cls is int or isinstance(rational_or_ND, Rational):
        rational = rational_or_ND
        ND = rational.as_integer_ratio()
    else:
        raise TypeError(cls)
    ND = Fraction(*ND).as_integer_ratio()
        #std...
    #mk_tuple
    return ND


def convert_to_ContinuedFraction_(rational_or_pair_or_list_or_iterator, /, *, str_ok=False):
    'cf_like/(Rational|(N,D)|[int]|(Iterator int)|(LazyList int)|ContinuedFraction|[str_ok]=>str/(cf_digits_list_repr|Fraction_repr)) -> cf/ContinuedFraction'
    #see:mk_ND5or_rational_
    x = rational_or_pair_or_list_or_iterator
    cls = type(x)
    if cls is str:
        if not str_ok:raise TypeError(cls, 'str_ok:=False')
        s = x
        x = cf_digits__or__int__or__Fraction = prepare_continued_fraction_from_string_(s)
        cls = type(x)
    x, cls
    #.if cls is LazyList or cls is ContinuedFraction:
    if isinstance(x, (ContinuedFraction, LazyList)):
        #or:force_lazy_imported_func_
        cf_digits = x
    elif cls is list:
        cf_digits = iter(x)
    elif cls is tuple:
        pair = x
        if not len(pair) == 2: raise TypeError
        N, D = pair
        cf_digits = iter_continued_fraction_digits5ND_(N, D)
    elif cls is int or isinstance(x, Rational):
        N, D = x.as_integer_ratio()
        cf_digits = iter_continued_fraction_digits5ND_(N, D)
    elif is_iterator(x):
        cf_digits = x
    else:
        raise TypeError(cls)
    #cf_digits = LazyList(cf_digits)
    cf = ContinuedFraction(cf_digits)
    return cf

__all__
from seed.math.continued_fraction.convert_to_ContinuedFraction_ import mk_ND5or_rational_, convert_to_ContinuedFraction_
from seed.math.continued_fraction.convert_to_ContinuedFraction_ import *
