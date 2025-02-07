#__all__:goto
r'''[[[
e ../../python3_src/seed/math/modular_arithmetic/IUIntMod.py

seed.math.modular_arithmetic.IUIntMod
py -m nn_ns.app.debug_cmd   seed.math.modular_arithmetic.IUIntMod -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.modular_arithmetic.IUIntMod:__doc__ -ht # -ff -df

[[
modular_arithmetic of same modulus
to be used in:
    pow_mod_
        primality_test
    finite_field

<<==:
view others/数学/power-ladder.txt
'Prime numbers-A Computational Perspective(2ed)(2005)(Pomerance).pdf'
===
除了初始化之外，所有 mod+div 使用 乘法+加法+减法+位操作 实现
  R-进制数的(%M)取模操作


计算:(x*R**-1%M)
  只使用:预先计算的缓存值+乘法+加法+减法+右移位操作+位与操作
  不使用:取模,除法
[M,R :<- [1..]][gcd(M,R)==1][x::int]:
  # M - modulus - 整数运算:mod,div
  # R - radix   - 位操作:   &, >>
  [CACHE_neg_invM_modR := ((-M)**-1%R)]
    #precomputed_value
    # => [y(x) == x + M*(x*CACHE_neg_invM_modR%R)]
  [y(x) =[def]= x + M*(x*(-M)**-1%R)]
  [y(x)%M == x%M]
    # 表达x于%M，溢出
  [y(x)%R == 0]
    # 可除=>移位替代除法
  [y(x)///R%M == x*R**-1%M]
    # 移位替代除法
    # 即: y(x)代表的是x，同时又能极快地整除以R，并且结果范围合理

  [R == 2**lbR][mask4R:=R-1][1-R <= x <= M*R+M-1]:
    整个计算:使用(>>lbR)模拟(/R)于(%M)之中
      divR_modM_(R,M; x)
      divR_modM_(R,M,lbR,mask4R:,CACHE_neg_invM_modR; x)
    [(y(x)///R) == (((x*CACHE_neg_invM_modR) & mask4R)*M+x) >> lbR]
    #极简后处理:
    !! [[1-R <= x <= M*R+M-1] -> [((y(x)///R) - (x*R**-1%M)) <- {0,M}]]
    [(x*R**-1%M) == (y(x)///R) -[(y(x)///R) >= M]M]

  #极简后处理:输入输出范围推导纟后处理:
  [diff := ((y(x)///R) - (x*R**-1%M))]
  !! [y(x)///R%M == x*R**-1%M]
  [diff%M == 0]
  [diff///M < 2]
      <==> [diff < 2*M]
      !! [y(x) <= x + M*(R-1)]
      <<== [(x + M*(R-1))/R - [x%M=!=0] < 2*M]
      <==> [x + M*(R-1) < 2*M*R + [x%M=!=0]R]
      <==> [x < M*R +M + [x%M=!=0]R]
      <<== [x < M*R +M]
  [[x < M*R +M] -> [diff///M < 2]]

  [x == M*R +M]:
    [y(x) == x +M*(R-1) == 2*M*R]
    [diff == 2*M*R///R - 0 == 2*M]
    [diff///M == 2]
  [[x == M*R +M] -> [diff///M == 2]]

  [diff///M >= 0]
      <==> [diff///M > -1]
      <==> [diff > -M]
      !! [y(x) >= x + [x%R=!=0]M]
      <<== [(x + [x%R=!=0]M)/R - (M-1) > -M]
      <==> [(x + [x%R=!=0]M) > -R]
      <==> [x > -R]
  [[x > -R] -> [diff///M >= 0]]

  [x == -R]:
    [y(x) == x +M*0 == -R]
    [diff == -R///R - (M-1) == -M]
    [diff///M == -1]
  [[x == -R] -> [diff///M == -1]]

  ==>>:
  [[x < M*R +M] -> [diff///M < 2]]
  [[x == M*R +M] -> [diff///M == 2]]
  [[x > -R] -> [diff///M >= 0]]
  [[x == -R] -> [diff///M == -1]]
  ==>>:
  [[1-R <= x <= M*R+M-1] -> [diff///1 <- {0,1}]]
  [[1-R <= x <= M*R+M-1] -> [((y(x)///R) - (x*R**-1%M)) <- {0,M}]]
    # 每次运算之后，检查是否需要(-M)
  要求纟极简后处理:[1-R <= x <= M*R+M-1]

  [(M-1)*(M-1) <= M*R+M-1]
    <==> [(M-1)*(M-1) < M*R+M]
    <==> [M*M+1 < M*R+3*M]
    <==> [M+1/M < R+3]
    !! [M>0]
    <==> [M+[M==1] < R+3]
    <==> [M+[M==1] <= R+2]
    !! [R>0]
    <==> [[[M==1][R>=1]]or[2<=M<=R+2]]
    <==> [1<=M<=R+2]
  [[R,M>=1] -> [[(M-1)*(M-1) <= M*R+M-1] <-> [1<=M<=R+2]]]
  要求纟嵌套使用:[1<=M<=R+2]


  用途:
    [mulR_modM_(x) := x*R%M][mulR_modM_(a*b) == divR_modM_(mulR_modM_(a)*mulR_modM_(b))]
    嵌套使用:只有初始化mulR_modM_需要mod:
      [mulR_modM_(a*b*c) == divR_modM_(divR_modM_(mulR_modM_(a)*mulR_modM_(b))*mulR_modM_(c))]
      [(a*b*c%M) == divR_modM_(mulR_modM_(a*b*c)) == divR_modM_(divR_modM_(divR_modM_(mulR_modM_(a)*mulR_modM_(b))*mulR_modM_(c)))]

    前提:[[R>=1][M>=1][gcd(M,R)==1]]
    嵌套使用=>要求:[1<=M<=R+2]
    极简后处理=>要求:[1-R <= x <= M*R+M-1]
    高效位操作=>[R==radix**floor_log_(radix;R)] #[R==2**lbR] #或者 其他进制数基数radix
    总要求{divR_modM_}:[[R>=1][M>=1][gcd(M,R)==1][1-R <= x <= M*R+M-1][1<=M<=R+2][R==radix**floor_log_(radix;R)]]

def divR_modM_(R,M,lbR,mask4R,CACHE_neg_invM_modR; x, /):
    '[[R>=1][M>=1][gcd(M,R)==1][1-R <= x <= M*R+M-1][R==2**lbR==mask4R+1][CACHE_neg_invM_modR==(-M)**-1%R]] => R -> M, lbR -> mask4R -> CACHE_neg_invM_modR -> x -> x*R**-1%M # [嵌套使用=>要求:[1<=M<=R+2]]'
    #
    y = (((x*CACHE_neg_invM_modR) & mask4R)*M+x) >> lbR
    #要求纟极简后处理:[1-R <= x <= M*R+M-1]
    #极简后处理:
    if y >= M:
        y -= M
    return y



===
]]

py_adhoc_call   seed.math.modular_arithmetic.IUIntMod   @f
from seed.math.modular_arithmetic.IUIntMod import *
]]]'''#'''
__all__ = r'''
IUIntMod
    IUIntMod__mixin__R_is_zpow
        UIntMod__mixin__R_is_u64__M_is_u64_neg59
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.lang.class_property import __0initialized0__, cached_class_property, cached_class_property4non_ABC, static_property, class_property
from seed.tiny_.check import check_type_is, check_int_ge, check_non_ABC, check_ABC
from operator import __index__
#.from itertools import islice
#.
from seed.abc.abc__ver1 import abstractmethod, override, ABC
from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...

class IUIntMod(ABC):
    r'''[[[
    [R>=1][M>=1][gcd(M,R)==1][1<=M<=R+2]
    [R==radix**floor_log_(radix;R)]


    not subclass of py.int to avoid confusing
    cls has no __lt__()
    cls own the modulus
        * init: (x*R)%modulus
        * save space
        * check both operator types are "same" # subclass are forbidden
        # * ?cache<modulus>
    modulus may be not a int
        eg: special form: (2**ez+small)

    总要求{divR_modM_}:[[R>=1][M>=1][gcd(M,R)==1][1-R <= x <= M*R+M-1][1<=M<=R+2][R==radix**floor_log_(radix;R)]]
    ]]]'''#'''
    __slots__ = ()
    @classmethod
    @abstractmethod
    def _full_range_raw_mulR_modM_(cls, i, /):
        'i/int{full-range} -> (i*R)%M'
        # mulR_modM_
        # vs:divR_modM_
    @classmethod
    @abstractmethod
    def _raw_divR_modM_(cls, i, /):
        'i/int{[1-R..<=M*R+M-1]} -> (i*R**-1)%M'
        # divR_modM_
        # vs:mulR_modM_
    @classmethod
    @abstractmethod
    def _raw_pow_modM_(cls, u, e, /):
        'u/int{[0..<M]} -> e/int{neg ok} -> (u**e)%M'
    @classmethod
    @abstractmethod
    def _raw_inv_modM_(cls, u, /):
        'u/int{[0..<M]} -> (u**-1)%M'
    @classmethod
    #@abstractmethod
    def from_raw_int_(cls, i, /):
        'i/int -> sf/cls #vs:_wrap5uint_xR_'
        xR = cls._full_range_raw_mulR_modM_(i)
            # mulR_modM_
        return cls._wrap5uint_xR_(xR)
    #@abstractmethod
    def to_raw_uint_(sf, /):
        'sf -> u/uint # require nontrival computation #vs:_uint_xR_'
        xR = sf._uint_xR_
        cls = type(sf)
        return cls._raw_divR_modM_(xR)

    @classmethod
    @abstractmethod
    def _wrap5uint_xR_(cls, xR, /):
        'xR/uint%M -> sf/cls # [xR == (x*R)%M] # vs:from_raw_int_'
    #.@abstractmethod
    #.def _unwrap2uint_xR_(sf, /):
    #.    'sf/cls -> xR/uint%M # [xR == (x*R)%M] # vs:to_raw_uint_'
    @property
    @abstractmethod
    def _uint_xR_(sf, /):
        '-> xR/uint%M # [xR == (x*R)%M] # vs:to_raw_uint_'

    @class_property
    @abstractmethod
    def _modulus_(cls, /):
        '-> M/modulus/[#may be not int#]'
    @class_property
    @abstractmethod
    def _radix_(cls, /):
        '-> R/radix/[#may be not int#]'
    @class_property
    @abstractmethod
    def _neg_invM_modR_(cls, /):
        '-> CACHE_neg_invM_modR/((-M**-1)%R)/uint%R'
        #CACHE_neg_invM_modR

    @class_property
    @abstractmethod
    def _one_xR_(cls, /):
        '-> one_xR/(1*R%M)/uint%M # may be [0==1==-1]'
    @class_property
    @abstractmethod
    def _neg_one_xR_(cls, /):
        '-> neg_one_xR/((-1*R)%M)/uint%M # may be [0==1==-1]'
    @class_property
    @abstractmethod
    def _zero_xR_(cls, /):
        '-> zero_xR/(0*R%M)/uint%M # may be [0==1==-1]'
    #._zero_xR_ = 0

    #.@class_property
    #.@abstractmethod
    #.def zero(sf, /):
    #.    '-> zero/cls'
    #.@class_property
    #.@abstractmethod
    #.def one(cls, /):
    #.    '-> one/cls'
    #.@class_property
    #.@abstractmethod
    #.def neg_one(cls, /):
    #.    '-> neg_one/cls'


    @cached_class_property4non_ABC
    def zero(cls, /, _zero_xR_):
        '-> zero/cls'
        return cls._wrap5uint_xR_(cls._zero_xR_)
        check_non_ABC(cls)
        cls.zero = cls._wrap5uint_xR_(cls._zero_xR_)
        return cls.zero
    @cached_class_property4non_ABC
    def one(cls, /, _zero_xR_, _one_xR_):
        '-> one/cls'
        if cls._one_xR_ == cls._zero_xR_:
            return cls.zero
        else:
            return cls._wrap5uint_xR_(cls._one_xR_)
        raise 000
        check_non_ABC(cls)
        if cls._one_xR_ == cls._zero_xR_:
            cls.one = cls.zero
        else:
            cls.one = cls._wrap5uint_xR_(cls._one_xR_)
        return cls.one
    @cached_class_property4non_ABC
    def neg_one(cls, /, _zero_xR_, _neg_one_xR_):
        '-> neg_one/cls'
        if cls._neg_one_xR_ == cls._zero_xR_:
            return cls.zero
        else:
            return cls._wrap5uint_xR_(cls._neg_one_xR_)
        raise 000
        check_non_ABC(cls)
        if cls._neg_one_xR_ == cls._zero_xR_:
            cls.neg_one = cls.zero
        else:
            cls.neg_one = cls._wrap5uint_xR_(cls._neg_one_xR_)
        return cls.neg_one



    @property
    def is_zero(sf, /):
        return (sf._uint_xR_ == sf._zero_xR_)
        return (sf._uint_xR_ == 0)
    @property
    def is_one(sf, /):
        return (sf._uint_xR_ == sf._one_xR_)
    @property
    def is_neg_one(sf, /):
        return (sf._uint_xR_ == sf._neg_one_xR_)
    def __bool__(sf, /):
        return not sf.is_zero
        return bool(sf._uint_xR_)
    def __hash__(sf, /):
        return (id(type(sf)) ^ sf._uint_xR_)
    def __eq__(sf, ot, /):
        return sf is ot or _op_(_eq, sf, ot)
    def __ne__(sf, ot, /):
        return not sf == ot
    #no:def __lt__(sf, ot, /):

    def __neg__(sf, /):
        if not sf:
            return sf
        cls = type(sf)
        #bug:xR = cls._modulus_ -sf._uint_xR_ -1
        a_xR = sf._uint_xR_
        # [0 <= a_xR < (M-1)]
        # [sf =!= 0]
        # [0 < a_xR < (M-1)]
        # [0 < M-a_xR < (M-1)]
        xR = cls._modulus_ - a_xR
        return cls._wrap5uint_xR_(xR)
    def __pos__(sf, /):
        return sf
    #no:def __abs__(sf, /):
    def __add__(sf, ot, /):
        return _op_(_add, sf, ot)
    def __sub__(sf, ot, /):
        return _op_(_sub, sf, ot)
    def __mul__(sf, ot, /):
        return _op_(_mul, sf, ot)
    def __truediv__(sf, ot, /):
        return _op_(_div, sf, ot)
    #no:def __floordiv__(sf, ot, /):
    #no:def __mod__(sf, ot, /):
    #no:def __divmod__(sf, ot, /):
    @property
    def square(sf, /):
        'sf -> sf**2'
        return _square(sf)
    @property
    def inv(sf, /):
        'sf -> sf**-1'
        return _inv(sf)
    def __pow__(sf, i, /):
        'sf -> i/int -> sf**i'
        i = __index__(i)
        return _pow(sf, i)

#mid-class IUIntMod(ABC):
def _eq(cls, sf, ot, /):
    return sf._uint_xR_ == ot._uint_xR_
    #return sf is ot or sf._uint_xR_ == ot._uint_xR_
def _square(sf, /):
    if sf.is_one:
        return sf
    if sf.is_zero:
        return sf
    cls = type(sf)
    if sf.is_neg_one:
        return cls.one
    aa_xRR = sf._uint_xR_**2
    # [0 <= aa_xRR <= (M-1)**2 < M*R]
    aa_xR = cls._raw_divR_modM_(aa_xRR)
    # [0 <= aa_xR <= (M-1)]
    return cls._wrap5uint_xR_(aa_xR)
    return sf*sf
def _inv(sf, /):
    #if a_xR == 0 and M == 1:
    if sf.is_one:
        return sf
    if sf.is_neg_one:
        return sf
    if sf.is_zero:
        #is_zero after is_one <<== [modulus==1]
        # [0 =!= 1]
        # 1/0
        raise 1//0
    cls = type(sf)
    divR_ = cls._raw_divR_modM_
    a_xR = sf._uint_xR_
    # [0 <= a_xR <= (M-1)]
    a = divR_(a_xR)
    # [0 <= a <= (M-1)]
    a_divR = divR_(a)
    # [0 <= a_divR <= (M-1)]
    invA_xR = cls._raw_inv_modM_(a_divR)
    # [0 <= invA_xR <= (M-1)]
    return cls._wrap5uint_xR_(invA_xR)
def _pow(sf, i, /):
    cls = type(sf)
    if sf.is_one:
        return sf
    if sf.is_neg_one:
        if i&1:
            # (-1)**odd
            return sf
        # (-1)**even
        return cls.one
    # [sf !<- {-1,+1}]
    if i == 0:
        # [0**0 == 1]
        return cls.one
    # [i =!= 0]

    # [sf !<- {-1,+1}]
    if sf.is_zero:
        #is_zero after is_one <<== [modulus==1]
        # [0 == sf !<- {-1,+1}]
        # [0 =!= 1]
        # !! [i =!= 0]
        # 0**nonzero
        if i < 0:
            raise 1//0
        return sf
    # [sf !<- {-1,0,+1}]
    # [i =!= 0]
    if i < 0:
        # [i < 0]
        sf = sf.inv
        i = -i
        # [i > 0]
    # [i > 0]
    # [sf !<- {-1,0,+1}]
    #.if i == 1:
    #.    return sf
    #.if i == 2:
    #.    return sf.square
    s = f'{i:b}'
    it = iter(s)
    ot = sf
    777; next(it)
    for b in it:
        ot = ot.square
        if b == '1':
            ot *= sf
    ot
    return ot

def _op_(op, sf, ot, /):
    if not (cls:=type(sf)) is type(ot):
        return NotImplemented
    return op(cls, sf, ot)
def _add(cls, sf, ot, /):
    M = cls._modulus_
    xR = _adjust(M, sf._uint_xR_ + ot._uint_xR_)
    return cls._wrap5uint_xR_(xR)
def _sub(cls, sf, ot, /):
    xR = sf._uint_xR_ - ot._uint_xR_
    if xR < 0:
        xR += cls._modulus_
    return cls._wrap5uint_xR_(xR)

def _mul(cls, sf, ot, /):
    if not sf:
        return sf
    if not ot:
        return ot
    if sf.is_one:
        return ot
    if sf.is_neg_one:
        return -ot
    if ot.is_one:
        return sf
    if ot.is_neg_one:
        return -sf

    a_xR = sf._uint_xR_
    b_xR = ot._uint_xR_
    # [0 <= a_xR <= (M-1)]
    # [0 <= b_xR <= (M-1)]
    a_mulB_xRR = a_xR * b_xR
    # [0 <= a_mulB_xRR <= (M-1)**2 < M*R]
    a_mulB_xR = cls._raw_divR_modM_(a_mulB_xRR)
    # [0 <= a_mulB_xR <= (M-1)]
    return cls._wrap5uint_xR_(a_mulB_xR)
def _div(cls, sf, ot, /):
    if not ot:
        raise 1//0
    if not sf:
        # 0/nonzero
        return sf
    if sf == ot:
        return cls.one
    if sf == -ot:
        return cls.neg_one
    return sf * ot.inv
    ######################
    #.if not ot:
    #.    raise 1//0
    #.if not sf:
    #.    # 0/nonzero
    #.    return sf
    #.if ot.is_one:
    #.    return sf
    #.if ot.is_neg_one:
    #.    return -sf
    #.if sf.is_one:
    #.    return ot.inv
    #.if sf.is_neg_one:
    #.    return -ot.inv
    #.#M = cls._modulus_
    #.a_xR = sf._uint_xR_
    #.b_xR = ot._uint_xR_
    #.# [0 <= a_xR <= (M-1)]
    #.# [0 <= b_xR <= (M-1)]
    #.divR_ = cls._raw_divR_modM_
    #.b = divR_(b_xR)
    #.# [0 <= b <= (M-1)]
    #.if 1:
    #.    # [0 <= b <= (M-1)]
    #.    b_divR = divR_(b)
    #.    # [0 <= b_divR <= (M-1)]
    #.    invB_xR = cls._raw_inv_modM_(b_divR)
    #.    # [0 <= invB_xR <= (M-1)]
    #.    a_divB_xRR = a_xR * invB_xR
    #.    # [0 <= a_divB_xRR <= (M-1)**2 < M*R]
    #.    a_divB_xR = divR_(a_divB_xRR)
    #.    # [0 <= a_divB_xR <= (M-1)]
    #.else:
    #.    # [0 <= b <= (M-1)]
    #.    invB = cls._raw_inv_modM_(b)
    #.    # [0 <= invB <= (M-1)]
    #.    _a_divB_xR = a_xR * invB
    #.    # [0 <= _a_divB_xR <= (M-1)**2]
    #.    # not:[0 <= a_divB_xR <= (M-1)]
    #.    raise 000
    #.# [0 <= a_divB_xR <= (M-1)]
    #.return cls._wrap5uint_xR_(a_divB_xR)
    ######################


def _adjust(M, u, /):
    'u/int/[0..<2*M] -> (u%M)'
    if u >= M:
        u -= M
    assert 0 <= u < M, (u, M)
    return u
#end-class IUIntMod(ABC):
_adjust #used by IUIntMod__mixin__R_is_zpow._raw_divR_modM_
def _inv_mod_(M, i, /):
    return pow(i, -1, M)
class IUIntMod__mixin__R_is_zpow(IUIntMod):
    '[M%2==1][R == 2**lbR][lbR>=1][1<=M<=R+2]'
    ___no_slots_ok___ = True
    @class_property
    @abstractmethod
    def _log2_R_(cls, /):
        '-> log2(R)/lbR/lgR/ez4R/uint{==log2(R)}'

    #.if 0:
    #.  def __init_subclass__(cls, /, *args, **kwds):
    #.    raise 000-mine_ABC_not_support___init_subclass__--see*__0initialized0__
    #.    super(__class__, cls).__init_subclass__(cls, *args, **kwds)
    #.    M = cls._modulus_
    #.    lbR = cls._log2_R_
    #.    R = 1<<lbR
    #.    cls._mask4R_ = R-1
    #.    #@override
    #.    cls._zero_xR_ = zero_xR = 0%M
    #.    #@override
    #.    cls._one_xR_ = one_xR = R%M
    #.    #@override
    #.    cls._neg_one_xR_ = neg_one_xR = (M-one_xR-1)
    #.        # may be [0==1==-1]
    #.    #@override
    #.    cls._radix_ = R
    #.    #@override
    #.    cls._neg_invM_modR_ = _inv_mod_(R, -M)

    @cached_class_property4non_ABC
    #@new_method
    def _mask4R_(cls, /, _radix_):
        '-> (R-1)/uint'
        return cls._radix_-1
    @cached_class_property4non_ABC
    @override
    def _radix_(cls, /, _log2_R_):
        '-> R/radix/[#may be not int#]'
        return 1 << cls._log2_R_
    @cached_class_property4non_ABC
    @override
    def _neg_invM_modR_(cls, /, _modulus_, _radix_):
        '-> CACHE_neg_invM_modR/((-M**-1)%R)/uint%R'
        #CACHE_neg_invM_modR
        return _inv_mod_(cls._radix_, -cls._modulus_)

    @cached_class_property4non_ABC
    @override
    def _one_xR_(cls, /, _radix_, _modulus_):
        '-> one_xR/(1*R%M)/uint%M # may be [0==1==-1]'
        return (_radix_)%cls._modulus_
    @cached_class_property4non_ABC
    @override
    def _neg_one_xR_(cls, /, _radix_, _modulus_):
        '-> neg_one_xR/((-1*R)%M)/uint%M # may be [0==1==-1]'
        return (-_radix_)%_modulus_
        return _modulus_ -cls._one_xR_ if _modulus_ >= 2 else cls._one_xR_
        #bug:return cls._modulus_ -1-cls._one_xR_
    @cached_class_property4non_ABC
    @override
    def _zero_xR_(cls, /, _radix_, _modulus_):
        '-> zero_xR/(0*R%M)/uint%M # may be [0==1==-1]'
        return (0)%cls._modulus_
    #._zero_xR_ = 0


    @classmethod
    @override
    def _wrap5uint_xR_(cls, xR, /):
        'xR/uint%M -> sf/cls # [xR == (x*R)%M] # vs:from_raw_int_'
        assert 0 <= xR < cls._modulus_, (xR, cls._modulus_)
        sf = super(__class__, cls).__new__(cls)
        sf._xR = xR
        return sf
    @property
    @override
    def _uint_xR_(sf, /):
        'sf/cls -> xR/uint%M # [xR == (x*R)%M] # vs:to_raw_uint_'
        return sf._xR

    def __str__(sf, /):
        s = repr_helper(sf, sf.to_raw_uint_())
        M = sf._modulus_
        a = sf._uint_xR_
        sa = str(a)
        b = a - M
        sb = f'({b})'
        sx = min(sa, sb, key=len)

        return s[:-1] + f', *[{sx}%{M}]*0' + s[-1]
    def __repr__(sf, /):
        return repr_helper(sf, sf.to_raw_uint_())
    def __new__(cls, x, /):
        T = type(x)
        if T is cls:
            sf = x
        elif T is int:
            i = x
            sf = cls.from_raw_int_(i)
            if 0b0001:assert i%cls._modulus_ == sf.to_raw_uint_(), (i, sf, str(sf))
        else:
            raise TypeError(T)
        return sf

    @classmethod
    @override
    def _full_range_raw_mulR_modM_(cls, i, /):
        'i/int{full-range} -> (i*R)%M'
        # mulR_modM_
        # vs:divR_modM_
        M = cls._modulus_
        u_xR = (i*cls._one_xR_)%M
        return u_xR
    @classmethod
    @override
    def _raw_divR_modM_(cls, i, /):
        'i/int{[1-R..<=M*R+M-1]} -> (i*R**-1)%M'
        # divR_modM_
        # vs:mulR_modM_
        # [(y(x)///R) == (((x*CACHE_neg_invM_modR) & mask4R)*M+x) >> lbR]
        M = cls._modulus_
        lbR = cls._log2_R_
        u = (((i*cls._neg_invM_modR_) & cls._mask4R_)*M + i) >> lbR
        return _adjust(M, u)

    @classmethod
    @override
    def _raw_pow_modM_(cls, u, e, /):
        'u/int{[0..<M]} -> e/int{neg ok} -> (u**e)%M'
        return pow(u, e, cls._modulus_)
    @classmethod
    @override
    def _raw_inv_modM_(cls, u, /):
        'u/int{[0..<M]} -> (u**-1)%M'
        return cls._raw_pow_modM_(u, -1)
#IUIntMod__mixin__R_is_zpow.__0initialized0__ = True
check_ABC(IUIntMod__mixin__R_is_zpow, ['_log2_R_', '_modulus_'])
#check_non_ABC(IUIntMod__mixin__R_is_zpow)

#view script/搜索冫伪素数牜临近幂方.py..header.2.1-_.sz4.2_3_5_7-SPRP.out.txt
#   2**2-1 / +1
#   2**3-1 / +3
#   2**4-3 / +1
#   2**7-1 / +3
#   2**8-5 / +1
#   2**15-19 / +3
#   2**16-15 / +1
#   2**31-1 / +11
#   2**32-5 / +15
#   2**63-25 / +29
#   2**64-59 / +13
#   2**127-1 / +29
#   2**128-159 / +51
class UIntMod__mixin__R_is_u64__M_is_u64_neg59(IUIntMod__mixin__R_is_zpow):
    _log2_R_ = 64
    _modulus_ = (1<<64)-59
UIntMod__mixin__R_is_u64__M_is_u64_neg59.__0initialized0__ = True#requored by cached_class_property4non_ABC

check_non_ABC(UIntMod__mixin__R_is_u64__M_is_u64_neg59)
def __(T, /):
    def assert_eq_(z, i, /):
        assert z == T.from_raw_int_(i), (str(z), i, i%T._modulus_, str(T.from_raw_int_(i)))
        assert i%T._modulus_ == z.to_raw_uint_(), (i, z, str(z))
    def assert_op1_eqs_(i, /):
        x = T.from_raw_int_(i)
        assert_eq_(x, i)
        assert_eq_(-x, -i)
        assert_eq_(+x, +i)
        assert_eq_(x.inv.inv, i)
        assert_eq_(x.inv*x, 1)
        assert_eq_(x*x, i*i)
        assert_eq_(x**2, i**2)
        assert_eq_(x.square, i**2)
        assert_eq_(x**+0b100110, pow(i, +0b100110, T._modulus_))
        assert_eq_(x**-0b100110, pow(i, -0b100110, T._modulus_))
        assert_eq_(x**-1, _inv_mod_(T._modulus_, i))
        assert_eq_(x.inv, _inv_mod_(T._modulus_, i))
    def assert_op2_eqs_(i, j, /):
        x = T.from_raw_int_(i)
        y = T.from_raw_int_(j)
        assert_eq_(x + y, i + j)
        assert_eq_(x - y, i - j)
        assert_eq_(x * y, i * j)
        assert_eq_(x / y, i * _inv_mod_(T._modulus_, j))
    assert_op1_eqs_(3)
    assert_op1_eqs_(-7)
    assert_op2_eqs_(3, -7)
    assert_op2_eqs_(0, -7)
    assert_op2_eqs_(1, -7)
    assert_op2_eqs_(-1, -7)
    assert_op2_eqs_(-3, -1)
    assert_op2_eqs_(-3, 1)
    assert_op2_eqs_(-3, 1)

__(UIntMod__mixin__R_is_u64__M_is_u64_neg59)

#.class __():
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError

__all__
from seed.math.modular_arithmetic.IUIntMod import *
