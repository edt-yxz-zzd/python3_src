#__all__:goto
        TODO
r'''[[[
e ../../python3_src/seed/math/float/IFloatNumber.py
view script/开方冫整数.py

view others/数学/float/浮点数运算.txt
see:py.decimal
    from decimal import Decimal
    cp -iv ~/../usr/lib/python3.11/*decimal* /sdcard/0my_files/tmp/py_lib_src/
    view /sdcard/0my_files/tmp/py_lib_src/_pydecimal.py




seed.math.float.IFloatNumber
py -m nn_ns.app.debug_cmd   seed.math.float.IFloatNumber -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.float.IFloatNumber:__doc__ -ht # -ff -df




[[
源起:
    发现 指数函数 的 误差极大
    泰勒展开 的 尾项 还好，主要是 误差纟输入+截断误差纟计算级数
    故此:
        + 假设输入值是精确值
        + 将浮点数表达为区间，计算级数纟泰勒展开时同时求出其上下限，以此确认误差，若精度不足，则 增加级数项 或 要求提高输入精度(=>表达式 优于 非精确值)
        + 将输入表达为表达式，以自适应输出端精度

设计思路:
    * 假设纟输入:
        假设输入值是精确值
    * 输出控制:
        #区间==上下限
        #精度: [precision=len(digits)][digits[0] >= 1][0 <= digit < radix]
        + 下限丷上限丷区间
            [下限 <= 目标值 <= 上限]
            分别输出:
                * 下限
                * 上限
                * (下限,上限)
        + 精度牜保底
            但 内部精度不足 可能 导致 输出精度不足 => 抛出异常 中止计算
        + 精度牜截断
            [绝对误差纟截断 = abs(目标值-输出值) <= 1/2*radix**(1-precision)*radix**floor_log_(radix;输出值)]
            [目标值==abc.vvvvvv][precision==5]:
                [abc.xy(z) == 输出值] # 5位数+1估计位
                [100.00(0) == radix**floor_log_(radix;输出值)] # 最高位:置1，余者:置0
                [000.01(0) == radix**(1-precision)*radix**floor_log_(radix;输出值)] # 最低位:置1，余者:置0
            毛病??估计位 有必要??
            [目标值==100.000000][precision==5]:
                [100.00(3) == 上限冃输出值]
                [100.00(0) == radix**floor_log_(radix;上限冃输出值)]
                [000.01(0) == radix**(1-precision)*radix**floor_log_(radix;上限冃输出值)]
                #######
                [99.999(8) == 下限冃输出值]
                [10.000(0) == radix**floor_log_(radix;下限冃输出值)]
                [00.001(0) == radix**(1-precision)*radix**floor_log_(radix;下限冃输出值)]
                #######
    * 表达/保存:
        + radix
        + 值:
            * 表达式:(函数/算法,[参数],),?最高精度纟输出
            * 非精确值:区间,精度
            * 精确值:
                * 分数
                * 浮点数
######################
raise ...(mid+/-1)*2**exp不太行，应该是 (low+(0|err))*2**exp, 但这样一来，需得显式控制precision:(low.bit_length,err.bit_length)
    context.add/mul...
    加减法 变成 三参数操作符
######################
边界-独立类
    区间 控制 两个 边界
    边界 含 精度#bit_length
        vs区间 => 误差
    边界:0 | 奇数整数*2**指数,精度+小侧丷大侧=>判断乘法是否合法(大小侧不相乘)+自动裁剪 [bit_length <= 精度]
    区间:小侧,大侧,欤合法
interval
    (小侧,大侧) # 小侧 <= 大侧
    正号,负号
    伸侧,缩侧 #趋向无穷侧vs趋向0 #==>>ceil vs floor
        # 取决于 (小侧,大侧)与0,oo的次序
    小侧&正号 => 缩侧
    小侧&负号 => 伸侧
    大侧&正号 => 伸侧
    大侧&负号 => 缩侧
    乘法=>大侧*大侧,小侧*小侧，不混淆
        至多1小侧,可能2大侧
            !! 小正大负 不合法
                小负大正
                小正大正
                小负大负
                .小正大负 不能正确处理:
                    若是零除零，只有 大侧 除 大侧，涵盖所有实数
                    若是 倒数纟零，只有 缩侧，乘以零，只有 伸侧 乘 缩侧，涵盖所有实数

]]




py_adhoc_call   seed.math.float.IFloatNumber   @f
from seed.math.float.IFloatNumber import *
]]]'''#'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from itertools import islice
from seed.tiny_.check import check_type_is, check_int_ge

from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_power_of_base_
from seed.math.floor_ceil import floor_div, ceil_div
from seed.math.floor_ceil import floor_div_, ceil_div_

from seed.abc.abc__ver1 import abstractmethod, override, ABC
from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...

class IContext4FloatNumberBoundary(ABC):
    __slots__ = ()
    @property
    @abstractmethod
    def radix(sf, /):
        '-> uint{>=2}'
    @property
    @abstractmethod
    def imay_precision(sf, /):
        '-> int{>=-1} # [precision>=1]'
class IContext4FloatNumber(ABC):
    __slots__ = ()
    @property
    @abstractmethod
    def context4boundary(sf, /):
        '-> ctx4bnd/IContext4FloatNumberBoundary'

@totalordering
class IFloatNumberBoundary(ABC):
    '[float(sf) =[def]= sign*mantissa*radix**exponent]'
    __slots__ = ()
    @property
    @abstractmethod
    def radix(sf, /):
        '-> uint{>=2}'
    @property
    @abstractmethod
    def exponent(sf, /):
        '-> int'
    @property
    @abstractmethod
    def mantissa(sf, /):
        '-> Integer{>=0} # uint'
    @property
    @abstractmethod
    def signed_mantissa(sf, /):
        '-> Integer # int'
        return apply_sign_(sf.sign, sf.mantissa)
        m = sf.mantissa
        return -m if sf.sign == -1 else m
    @abstractmethod
    #def rshift_mantissa_then_mod_pow_(sf, num_digits4rshift, imay_exp4modulus, /):
    def slice_mantissa_(sf, num_digits4rshift, imay_exp4modulus, /):
        'uint -> int{>=-1} -> (fragment4mantissa/Integer{>=0}, exp4lshift/uint)'
        m = sf.mantissa
        r = sf.radix
        m //= r**num_digits4rshift
        if not imay_exp4modulus == -1:
            exp4modulus = imay_exp4modulus
            pw = r**exp4modulus
            m %= pw
        e, m = factor_pint_out_power_of_base_(radix, m)
        return (m, e)
        e = 0
        while not m == 0 and m%r == 0:
            m //= r
            777; e += 1
        return (m, e)
    @property
    @abstractmethod
    def len_digits(sf, /):
        '-> uint # [[mantissa=!=0]*radix**(len_digits-1) <= mantissa < radix**len_digits] # [len_digits == 0 if mantissa==0 else 1+floor_log_(radix;mantissa)]'
    @property
    @abstractmethod
    def digits(sf, /):
        '-> [uint%radix] # little_endian # [mantissa == sum(d*radix**e for e, d in enumerate(digits))][len(digits) == 0 or digits[-1] > 0][len(digits) == len_digits]'
    @property
    @abstractmethod
    def sign(sf, /):
        '-> (-1|0|1)'
    @property
    @abstractmethod
    def low_vs_exact_vs_up(sf, /):
        '-> (-1|0|1) # (lower_bound|both_bound|upper_bound) # for iter_add4bnd'
    @property
    def floor_vs_exact_vs_ceil(sf, /):
        '-> (-1|0|+1) # [how to truncate mantissa when iter_mul4bnd]'
        # !! reduced_boundaries used in naive_mul4IFloatNumberBoundary
        r = sf.low_vs_exact_vs_up
        s = sf.sign
        return r if not s else s * r
        return sf.sign * sf.low_vs_exact_vs_up
    @property
    def is_exact(sf, /):
        '-> bool'
        return sf.low_vs_exact_vs_up==0


    #@abstractmethod
    def iter_add4bnd(sf, ot, ctx4bnd, /):
        'IFloatNumberBoundary{radix} -> IFloatNumberBoundary{radix} -> IContext4FloatNumberBoundary{radix,precision} -> (Iter IFloatNumberBoundary{radix,len_digits<=precision}){len<-[0..=2]}'
        a, b = sf.low_vs_exact_vs_up, ot.low_vs_exact_vs_up
        if -1 == a*b: return
        low_vs_exact_vs_up = a or b
        ts = [-1,+1] if low_vs_exact_vs_up == 0 else [low_vs_exact_vs_up]
        for low_vs_up in ts:
            assert abs(low_vs_up) == 1
            (is_exact, sign, mantissa, exponent) = naive_add4IFloatNumberBoundary(sf.radix, ctx4bnd.imay_precision, low_vs_up, sf.sign_mantissa_exponent_triple, ot.sign_mantissa_exponent_triple)
            yield sf._mk5self_and_sign_mantissa_exponent_(sign, mantissa, exponent, low_vs_exact_vs_up if is_exact else low_vs_up)
            if is_exact:break
    #@abstractmethod
    def iter_mul4bnd(sf, ot, ctx4bnd, /):
        'IFloatNumberBoundary{radix} -> IFloatNumberBoundary{radix} -> IContext4FloatNumberBoundary{radix,precision} -> (Iter IFloatNumberBoundary{radix,len_digits<=precision}){len<-[0..=2]}'
        a, b = sf.floor_vs_exact_vs_ceil, ot.floor_vs_exact_vs_ceil
        if -1 == a*b: return
        floor_vs_exact_vs_ceil = a or b
        ts = [-1,+1] if floor_vs_exact_vs_ceil == 0 else [floor_vs_exact_vs_ceil]
        _sign = sf.sign*ot.sign
        _exponent = sf.exponent + ot.exponent
        for floor_vs_ceil in ts:
            assert abs(floor_vs_ceil) == 1
            (is_exact, mantissa, exp4lshift) = naive_mul4IFloatNumberBoundary(sf.radix, ctx4bnd.imay_precision, floor_vs_ceil, sf.mantissa, ot.mantissa)
            sign = _sign if mantissa else 0
                # [mantissa may be 0 since truncated by precision]
            exponent = _exponent + exp4lshift if mantissa else 0
            yield sf._mk5self_and_sign_mantissa_exponent_(sign, mantissa, exponent, floor_vs_exact_vs_ceil if is_exact else floor_vs_ceil)
            if is_exact:break
    @abstractmethod
    def _mk5self_and_sign_mantissa_exponent_(sf, sign, mantissa, exponent, floor_vs_exact_vs_ceil, /):
        'sf -> sign/(-1|0|1) -> mantissa/Integer{>=0} -> exponent/int -> floor_vs_exact_vs_ceil/(-1|0|1) -> IFloatNumberBoundary'
    @property
    def sign_mantissa_exponent_triple(sf, /):
        '-> ((-1|0|1), Integer{>=0}, int)'
        return (sf.sign, sf.mantissa, sf.exponent)
    def __eq__(sf, ot, /):
        'IFloatNumberBoundary{radix} -> IFloatNumberBoundary{radix} -> bool'
        if not isinstance(ot, IFloatNumberBoundary):return NotImplemented
        if not sf.radix == ot.radix:return NotImplemented
        return sf.sign_mantissa_exponent_triple == ot.sign_mantissa_exponent_triple
    def __lt__(sf, ot, /):
        'IFloatNumberBoundary{radix} -> IFloatNumberBoundary{radix} -> bool'
        if not isinstance(ot, IFloatNumberBoundary):return NotImplemented
        if not sf.radix == ot.radix:return NotImplemented
        s0 = sf.sign
        s1 = ot.sign
        if not s0 == s1:
            return s0 < s1
        if s0 == 0:
            return False
        sz0 = sf.len_digits
        sz1 = ot.len_digits
        e0 = sf.exponent
        e1 = ot.exponent
        L0 = sz0+e0
        L1 = sz1+e1
        neg = s0 < 0
        if not L0 == L1:
            return (L0 < L1) ^ neg
        m0 = sf.mantissa
        m1 = ot.mantissa
        if sz0 == sz1:
            return (m0 < m1) ^ neg
        min_sz = min(sz0, sz1)
        m0 = sf.slice_mantissa_(sz0-min_sz, -1)
        m1 = sf.slice_mantissa_(sz1-min_sz, -1)
        return ((m0, sz0) < (m1, sz1)) ^ neg

#detach,split
def detach_sign_(signed_mantissa, /):
    sign = sign_of(signed_mantissa)
    mantissa = abs(signed_mantissa)
    return (sign, mantissa)
def apply_sign_(sign, mantissa, /):
    '-> signed_mantissa'
    return -mantissa if sign == -1 else mantissa
def naive_add4IFloatNumberBoundary(radix, imay_precision, low_vs_up, lhs_sign_mantissa_exponent_triple, rhs_sign_mantissa_exponent_triple)
    '-> (is_exact, sign, mantissa, exponent)'
    (lhs_sign, lhs_mantissa, lhs_exponent) = lhs_sign_mantissa_exponent_triple
    (rhs_sign, rhs_mantissa, rhs_exponent) = rhs_sign_mantissa_exponent_triple
    if not lhs_sign:
        (sign, mantissa, exponent) = rhs_sign_mantissa_exponent_triple
    elif not rhs_sign:
        (sign, mantissa, exponent) = lhs_sign_mantissa_exponent_triple
    else:
        d = lhs_exponent - rhs_exponent
        #alignment
        # need to be optimized: since shift by d waste time if precision is small
        #   naive here
        if d < 0:
            exponent = lhs_exponent
            lm = lhs_mantissa
            rm = rhs_mantissa << -d
        else:
            exponent = rhs_exponent
            rm = rhs_mantissa
            lm = lhs_mantissa << d
        exponent
        lm, rm
        lv = apply_sign_(lhs_sign, lm)
        rv = apply_sign_(rhs_sign, rm)
        v = lv + rv
        (sign, mantissa) = detach_sign_(v)
    (sign, mantissa, exponent)
    sign
    floor_vs_ceil = low_vs_up ^ (sign == -1)
    (is_exact, mantissa, exp4lshift) = truncate(radix, imay_precision, floor_vs_ceil, mantissa)
    exponent += exp4lshift
    return (is_exact, sign, mantissa, exponent)

def naive_mul4IFloatNumberBoundary(radix, imay_precision, floor_vs_ceil, lhs_mantissa, rhs_mantissa, /):
    '-> (is_exact, mantissa, exp4lshift)'
    # need to be optimized: since full mul waste time if precision is small
    #   naive here
    m = lhs_mantissa*rhs_mantissa
    return truncate(radix, imay_precision, floor_vs_ceil, mantissa)
def truncate(radix, imay_precision, floor_vs_ceil, mantissa, /):
    '-> (is_exact, mantissa, exp4lshift)'
    m = mantissa
    if m == 0 or imay_precision==-1:
        return (True, m, 0)
    precision = imay_precision
    len_digits = 1+floor_log_(radix, m)
    if len_digits <= precision:
        return (True, m, 0)
    is_exact = False
    _div = floor_div if not floor_vs_ceil else ceil_div
    m = _div(m, radix**(len_digits-precision))
    assert m > 0
    e, m = factor_pint_out_power_of_base_(radix, m)
    return (is_exact, m, e)
#def default_mul4IFloatNumberBoundary(imay_precision, floor_vs_ceil, lhs_boundary, rhs_boundary, /):
#    '-> (mantissa, exp4modulus)'
class IFloatNumber(ABC):
    __slots__ = ()
    @property
    @abstractmethod
    def radix(sf, /):
        '-> uint{>=2}'
    @property
    @abstractmethod
    def boundaries(sf, /):
        '-> (lower_boundary, upper_boundary)/(IFloatNumberBoundary{radix,-abs(low_vs_exact_vs_up)}, IFloatNumberBoundary{radix,abs(low_vs_exact_vs_up)})'
    @property
    @abstractmethod
    def reduced_boundaries(sf, /):
        '-> (lower_boundary, upper_boundary) if not is_exact else (lower_boundary,)'
        return sf.boundaries if not sf.is_exact else (sf.lower_boundary,)
    @property
    def lower_boundary(sf, /):
        '-> IFloatNumberBoundary{radix,-abs(low_vs_exact_vs_up)}'
        return sf.boundaries[0]
    @property
    def upper_boundary(sf, /):
        '-> IFloatNumberBoundary{radix,abs(low_vs_exact_vs_up)}'
        return sf.boundaries[-1]
    #@abstractmethod
    def add4flt(sf, ot, ctx4flt, /):
        'IFloatNumber{radix} -> IFloatNumber{radix} -> IContext4FloatNumber{radix,precision} -> IFloatNumber{radix,len_digits<=precision}'
        ctx4bnd = ctx4flt.context4boundary
        (lower_boundary, upper_boundary) = naive_add4IFloatNumber(ctx4bnd, sf, ot)
        return sf._mk5self_and_boundaries_(lower_boundary, upper_boundary)
    #@abstractmethod
    def mul4flt(sf, ot, ctx4flt, /):
        'IFloatNumber{radix} -> IFloatNumber{radix} -> IContext4FloatNumber{radix,precision} -> IFloatNumber{radix,len_digits<=precision}'
        ctx4bnd = ctx4flt.context4boundary
        (lower_boundary, upper_boundary) = naive_mul4IFloatNumber(ctx4bnd, sf, ot)
        return sf._mk5self_and_boundaries_(lower_boundary, upper_boundary)
    @abstractmethod
    def _mk5self_and_boundaries_(sf, lower_boundary, upper_boundary, /):
        'sf -> IFloatNumberBoundary{radix} -> IFloatNumberBoundary{radix} -> IFloatNumber{radix}'
    @property
    def is_exact(sf, /):
        '-> bool'
        return sf.lower_boundary.is_exact
        return sf.lower_boundary.low_vs_exact_vs_up==0
        (lower_boundary, upper_boundary) = sf.boundaries
        return lower_boundary == upper_boundary
        return lower_boundary.sign_mantissa_exponent_triple == upper_boundary.sign_mantissa_exponent_triple
    @property
    def does_cross_zero(sf, /):
        '-> bool # include both negative&positive real number'
        (lower_boundary, upper_boundary) = sf.boundaries
        return lower_boundary.sign * upper_boundary.sign == -1


def naive_add4IFloatNumber(ctx4bnd, lhs_float, rhs_float, /):
    '-> boundaries/(lower_boundary, upper_boundary)/(IFloatNumberBoundary, IFloatNumberBoundary)'
    ls = []
    it = zip(lhs_float.reduced_boundaries, rhs_float.reduced_boundaries) if lhs_float.is_exact and rhs_float.is_exact else zip(lhs_float.boundaries, rhs_float.boundaries)
    for (lhs_XB, rhs_XB) in enumerate(it):
        ls.extend(lhs_XB.iter_add4bnd(rhs_XB, ctx4bnd))
    ls
    # [1 <= len(ls) <= 2]
    res_LB = ls[0]
    res_UB = ls[-1] # NOT ls[1]
    return (res_LB, res_UB)


def naive_mul4IFloatNumber(ctx4bnd, lhs_float, rhs_float, /):
    '-> boundaries/(lower_boundary, upper_boundary)/(IFloatNumberBoundary, IFloatNumberBoundary)'
    ls = []
    for j, (lhs_XB, rhs_XB) in enumerate(product(lhs_float.reduced_boundaries, rhs_float.reduced_boundaries)):
        # !! reduced_boundaries
        # !! new-version:floor_vs_exact_vs_ceil
        ls.extend(lhs_XB.iter_mul4bnd(rhs_XB, ctx4bnd))
    ls
    res_LB = min(ls)
    res_UB = max(ls)
    return (res_LB, res_UB)


class IFloatNumberExpr(ABC):
    __slots__ = ()
    #___no_slots_ok___ = True
    @property
    @abstractmethod
    def radix(sf, /):
        '-> uint{>=2}'
    @abstractmethod
    def _eval_(sf, low_vs_up_vs_both:'(1|2|3)', precision4raise, precision4trunc, /):
        '-> IFloatNumber'
    def __repr__(sf, /):
        return repr_helper(sf, *args, **kwargs)
class IFloatNumberInterval(IFloatNumberExpr):
class IFloatNumberExact(IFloatNumberInterval):


__all__
from seed.math.float.IFloatNumber import *
