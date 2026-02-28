#__all__:goto
r'''[[[
e ../../python3_src/seed/types/Range7float.py

seed.types.Range7float
py -m nn_ns.app.debug_cmd   seed.types.Range7float -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.types.Range7float:__doc__ -ht # -ff -df
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %seed.types.Range7float:cls@T    =T   +exclude_attrs5listed_in_cls_doc
#######

[[
used in:
    view ../../python3_src/seed/for_libs/for_colorsys/calibrated_RGB/white_and_primary_chromaticities.py
        list color between R~G or R~B or G~B
            Type4CIE_XYZ_with_WP.iter_weighted_average__2_
            Type4CIE_Lab_with_WP.iter_weighted_average__2_
            Type4CIE_Luv_with_WP.iter_weighted_average__2_
]]


'#'; __doc__ = r'#'
>>>



py_adhoc_call   seed.types.Range7float   @f

]]]'''#'''
__all__ = r'''
Range7float

check_float_
    check_normalized_float_

check_float_near_enough_
round_float_if_near_enough_
    round_floats_if_near_enough_
    round_floatss_if_near_enough_

IWeightedAverage
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from functools import cached_property
from seed.tiny_.check import check_type_is, check_int_ge

from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.helper.repr_input import repr_helper
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

__all__

def check_float_(u, /):
    check_type_is(float, u)
def check_normalized_float_(u, max0=1.0, /):
    check_type_is(float, u)
    if not 0.0 <= u <= max0:raise TypeError(u, max0, u-max0)


def round_floats_if_near_enough_(RGB, /):
    return tuple(map(round_float_if_near_enough_, RGB))
def round_floatss_if_near_enough_(RGBs, /):
    return tuple(map(round_floats_if_near_enough_, RGBs))
def round_float_if_near_enough_(x, /, *, tolerance=1e-6):
    expected = float(round(x))
    if abs(x-expected) < tolerance:
        x = expected
    return x
def check_float_near_enough_(expected, x, /, *, tolerance=1e-9):
    assert abs(x-expected) < tolerance

class IWeightedAverage(ABC):
    __slots__ = ()
    #___no_slots_ok___ = True
    #weighted_sum
    #weighted_average
    @abstractmethod
    def __pos__(sf, /):
        return sf
    @abstractmethod
    def __neg__(sf, /):
        'negatve_value_ok'
    @abstractmethod
    def __sub__(sf, ot, /):
        'negatve_value_ok'
    @abstractmethod
    def __add__(sf, ot, /):
        'negatve_value_ok'
    @abstractmethod
    def __mul__(sf, scale, /):
        'negatve_value_ok'
    @abstractmethod
    def __rmul__(sf, scale, /):
        'negatve_value_ok'

    def weighted_average__2_(sf, ot, weight4ot, /):
        'sf -> ot -> w -> ((1-w)*sf + w*ot) # == (sf +w*(ot-sf))'
        return sf +(ot -sf)*weight4ot
    def weighted_average__3_(A, B, weight4B, C, weight4C, /):
        'sf/A -> B -> wB -> C -> wC -> ((1-wB-wC)*A + wB*B + wC*C) # == (A +wB*(B-A) +wC*(C-A))'
        return A +(B -A)*weight4B +(C -A)*weight4C
    def weighted_average__many_(sf, ot_weight_pairs, /):
        'sf -> pairs/(Iter (ot, w)) -> ((1-sum(map snd pairs))*sf + sum(w*ot for ot,w in pairs) # == (sf +sum(w*(ot-sf) for ot,w in pairs))'
        acc = sf
        for ot, weight4ot in ot_weight_pairs:
            #bug:sf = sf.weighted_average__2_(ot, weight4ot)
            acc += (ot -sf)*weight4ot
        return acc
    def iter_weighted_average__2_(sf, ot, weights4ot, /):
        'sf -> ot -> ws/(Iter w) -> (weighted_average__2_(sf, ot, w) for w in ws)'
        df = ot -sf
        for w in weights4ot:
            yield sf + df*w

IWeightedAverage.iter_weighted_average__2_
class Range7float:
    def __init__(sf, offset, scale, rng7int, /):
        check_float_(offset)
        check_float_(scale)
        check_type_is(range, rng7int)
        sf._k = scale
        sf._b = offset
        sf._js = rng7int
    def __repr__(sf, /):
        return repr_helper(sf, sf._b, sf._k, sf._js)
    def __len__(sf, /):
        return len(sf._js)
    def iter_(sf, /, *, reverse:bool):
        f = reversed if reverse else iter
        it = f(sf._js)
        if not sf._k == 1.0:
            it = map(sf._k.__mul__, it)
        if not sf._b == 0.0:
            it = map(sf._b.__add__, it)
        return it
    def __iter__(sf, /):
        return sf.iter_(reverse=False)
    def __reversed__(sf, /):
        return sf.iter_(reverse=True)
    def __getitem__(sf, x, /):
        y = sf._js[x]
        if type(y) is int:
            return sf._b + sf._k * y
        if type(y) is range:
            return __class__(sf._b, sf._k, y)
        raise 000
        raise TypeError(type(y))
    @cached_property
    def start(sf, /):
        #bug:return sf[0]
        return sf._b + sf._k * sf._js.start
    @cached_property
    def stop(sf, /):
        return sf._b + sf._k * sf._js.stop
    @cached_property
    def step(sf, /):
        return         sf._k * sf._js.step
    @classmethod
    def mk5OSSSS_(cls, /, offset, scale, start, stop, step):
        return cls(float(offset), float(scale), range(start, stop, step))
    #.def mk5SSS_(cls, /, start, stop, step):
        #.q, r = divmod(stop-start, step)
        #.scale = float(step)
        #.777;step = 1

        #.start = floor(start//scale)
        #.x = floor(stop//scale)

















__all__
from seed.types.Range7float import check_float_, check_normalized_float_, check_float_near_enough_
from seed.types.Range7float import round_float_if_near_enough_, round_floats_if_near_enough_, round_floatss_if_near_enough_
from seed.types.Range7float import Range7float
from seed.types.Range7float import IWeightedAverage

from seed.types.Range7float import *
