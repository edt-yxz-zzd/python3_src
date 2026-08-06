#__all__:goto
#TODO:goto
#Qfb__x__smooth_group_order_method:goto
#证明冫二二型倒数公式:goto
#证明冫二二型歧型平方必为幺元:goto
#调整冫二二型中部牜保持等价类:goto
#整数分解牜二二型歧型:goto
#数据实验冫群规模规律:goto
#无法分解素幂分量乊整数分解牜二二型歧型:goto
#   ???好像不能证明 => 『此方案无效:[D:=n2D_(k * n**2)]』
#   #view ../../python3_src/seed/math/factor_pint/factor_pint__smooth_group_order_method__7py_adhoc_call.py
#       #发现冫平方因子使得群规模包含素幂的环乘阶:goto
#       #发现冫四次因子使得群规模直接包含该素因子:goto
#goto:实证:四次方因子=>群规模包含((P+(P%4-2))*P) ~= phi_(sqrt(P**4))
#goto:实证:[0 == ((4*qfbclassno(-4*k*p^2))%(p+(p%4-2)*Jacobi_symbol(p,k)))]
#   证明 => 『此方案无效:[D:=n2D_(k * n**2)]』
#goto:乘四影响不大，乘二影响很大
r'''[[[
e ../../python3_src/seed/math/BinaryQuadraticForm.py

seed.math.BinaryQuadraticForm
py -m nn_ns.app.debug_cmd   seed.math.BinaryQuadraticForm -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.BinaryQuadraticForm:__doc__ -ht # -ff -df
#######

[[
come_from:
view ../../python3_src/seed/math/factor_pint/factor_pint__smooth_group_order_method.py
]]
[[
#整数分解牜二二型歧型:here
#无法分解素幂分量乊整数分解牜二二型歧型:here
整数分解:ambiguous_form:
    [n%2==1][n>0]
    [D == (-n|-4*n)]
    n的分解 转化为 D的分解
    或:
    [n%2==1][n>0] [k%2==1][k>0]
    [D == (-k*n|-4*k*n)]
    n的分解 转化为 (k*n)的分解 再转化为 D的分解
[bqf==Qfb(a,b,a)]:
    [D == b**2 -4*a**2 == (b-2*a)*(b+2*a)]
    [gcd((b-2*a),(b+2*a))
    == gcd(2*b,(b+2*a))
    == 2**-ez*gcd(2*b,2*(b+2*a))
    == 2**-ez*gcd(2*b,4*a)
    == 2**(1-ez)*gcd(b,2*a)
    !! [is_primitive7Qfb_(a,b,a)]
    => [1 == gcd(a,b)]
    == 2**(1-ez)**gcd(b,2)
    <- {2**(1-ez),2**(2-ez)}
    ]
    [gcd((b-2*a),(b+2*a)) <- {1,2,4}]
    !! [n%2 == 1]
    [1 == gcd(n,gcd((b-2*a),(b+2*a)))]
    [不能分解:素幂分量]
[bqf==Qfb(a,a,c)]:
    [D == a**2 -4*a*c == a*(a-4*c)]
    [gcd(a,(a-4*c))
    == gcd(a,(-4*c))
    == 2**ez*gcd(a,c)
    !! [is_primitive7Qfb_(a,a,c)]
    => [1 == gcd(a,c)]
    == 2**ez
    ]
    [gcd(a,(a-4*c)) <- {1,2,4}]
    !! [n%2 == 1]
    [1 == gcd(n,gcd(a,(a-4*c)))]
    [不能分解:素幂分量]
[bqf==Qfb(a,0,c)]:
    [D == -4*a*c]
    [gcd(a,c)
    !! [is_primitive7Qfb_(a,0,c)]
    => [1 == gcd(a,c)]
    == 1
    ]
    [gcd(a,c) == 1]
    !! [n%2 == 1]
    [1 == gcd(n,gcd(a,c))]
    [不能分解:素幂分量]
[不能分解:素幂分量]
    ???好像不能证明 => 『此方案无效:[D:=n2D_(k * n**2)]』

证明 => 『此方案无效:[D:=n2D_(k * n**2)]』
    !! goto:实证:[0 == ((4*qfbclassno(-4*k*p^2))%(p+(p%4-2)*Jacobi_symbol(p,k)))]

#证明冫二二型歧型平方必为幺元:goto
#数据实验冫群规模规律:goto
]]



'#'; __doc__ = r'#'



is_primitive7Qfb_
is_reduced7Qfb7negD_
reduce4Qfb7negD_
is_ambiguous_form_7Qfb7negD7reduced_
>>> is_primitive7Qfb_(3*5, 5*7, 7*3)
True
>>> is_primitive7Qfb_(3*5, 5*7, 7*3*5)
False


>>> is_reduced7Qfb7negD_(3, 0, 2)
False
>>> is_reduced7Qfb7negD_(3, 0, 3)
True
>>> is_reduced7Qfb7negD_(3, -1, 3)
False
>>> is_reduced7Qfb7negD_(3, +1, 3)
True
>>> is_reduced7Qfb7negD_(3, -1, 4)
True
>>> is_reduced7Qfb7negD_(3, -2, 4)
True
>>> is_reduced7Qfb7negD_(3, -3, 4)
False
>>> is_reduced7Qfb7negD_(3, +3, 4)
True
>>> is_reduced7Qfb7negD_(3, +4, 4)
False
>>> is_reduced7Qfb7negD_(3, +4, 5)
False


>>> reduce4Qfb7negD_(777, 34, 66)
(66, -34, 777)
>>> reduce4Qfb7negD_(7, +34, 66)
(7, 6, 26)
>>> reduce4Qfb7negD_(7, -34, 66)
(7, -6, 26)


>>> is_ambiguous_form_7Qfb7negD7reduced_(999, 47, 999)
True
>>> is_ambiguous_form_7Qfb7negD7reduced_(47, 47, 999)
True
>>> is_ambiguous_form_7Qfb7negD7reduced_(47, 0, 999)
True
>>> is_ambiguous_form_7Qfb7negD7reduced_(47, 1, 999)
False


>>> check_discriminant7Qfb_(-3)
>>> check_discriminant7Qfb_(-4)
>>> check_discriminant7Qfb_(1)
Traceback (most recent call last):
    ...
TypeError: 1
>>> check_discriminant7Qfb_(0)
Traceback (most recent call last):
    ...
TypeError: 0
>>> check_discriminant7Qfb_(-1)
Traceback (most recent call last):
    ...
TypeError: -1
>>> check_discriminant7Qfb_(-2)
Traceback (most recent call last):
    ...
TypeError: -2
>>> check_discriminant7Qfb_(-5)
Traceback (most recent call last):
    ...
TypeError: -5
>>> check_discriminant7Qfb_(-6)
Traceback (most recent call last):
    ...
TypeError: -6




D5ABC_
C5DAB_
>>> D5ABC_(3, 5, 7)
-59
>>> C5DAB_(-59, 3, 5)
7
>>> C5DAB_(-59, 2, 5)
Traceback (most recent call last):
    ...
seed.math.floor_ceil_tools.fc_perfect.NotPerfectError__div

n2D_
    nk2D_
D2A_ge_
>>> nk2D_(3, 3)
Traceback (most recent call last):
    ...
ValueError: (3, 3, 3)
>>> nk2D_(6, 5)
Traceback (most recent call last):
    ...
ValueError: 6
>>> nk2D_(5, 6)
Traceback (most recent call last):
    ...
ValueError: 6
>>> nk2D_(-3, 5)
Traceback (most recent call last):
    ...
TypeError: -3
>>> nk2D_(3, -5)
Traceback (most recent call last):
    ...
TypeError: -5
>>> nk2D_(3, 5)
-15
>>> nk2D_(9, 1)
-36
>>> nk2D_(11, 1)
-11
>>> nk2D_(1, 9)
-36
>>> nk2D_(1, 11)
-11
>>> n2D_(9)
-36
>>> n2D_(11)
-11
>>> D2A_ge_(-36, -9999999)
5
>>> D2A_ge_(-11, -9999999)
3

>>> D2A_ge_(-11, 16)
23
>>> D2A_ge_(-11, 40)
47
>>> D2A_ge_(-11, 72)
89
>>> D2A_ge_(-11, 40, avoid_A_mod8_eq1=True)
47
>>> D2A_ge_(-11, 72, avoid_A_mod8_eq1=True)
103

>>> D2A_ge_(1-2**67, 1040)
1049
>>> D2A_ge_(1-2**67, 1040, avoid_A_mod8_eq1=True)
1061




>>> D2Qfb7A_ge_(-36, -9999999)
mk4Qfb_class_group5ABC_(2, 2, 5)
>>> D2Qfb7A_ge_(-11, -9999999)
mk4Qfb_class_group5ABC_(1, 1, 3)

>>> D2Qfb7A_ge_(1-2**67, 1040)
mk4Qfb_class_group5ABC_(1049, 61, 35170150760170738)
>>> D2Qfb7A_ge_(1-2**67, 1040, avoid_A_mod8_eq1=True)
mk4Qfb_class_group5ABC_(1061, 717, 34772373371742914)

>>> D2Qfb7A_ge_(1-2**67, 1040, avoid_A_mod8_eq1=True, with_A7repr=True)
(1061, mk4Qfb_class_group5ABC_(1061, 717, 34772373371742914))
>>> D2Qfb7A_ge_(1-2**67, 2**34, avoid_A_mod8_eq1=True, with_A7repr=True)
(17179869263, mk4Qfb_class_group5ABC_(2244236926, 1909940287, 16845572624))


>>> D2QfbPow7A_ge_(-36, 1, -9999999)
mk4Qfb_class_group5ABC_(2, 2, 5)
>>> D2QfbPow7A_ge_(-11, 1, -9999999)
mk4Qfb_class_group5ABC_(1, 1, 3)

>>> D2QfbPow7A_ge_(1-2**67, 1, 1040)
mk4Qfb_class_group5ABC_(1049, 61, 35170150760170738)
>>> D2QfbPow7A_ge_(1-2**67, 1, 1040, avoid_A_mod8_eq1=True)
mk4Qfb_class_group5ABC_(1061, 717, 34772373371742914)




>>> n2QfbPow7A_ge_(9, 1, -9999999)
mk4Qfb_class_group5ABC_(2, 2, 5)
>>> n2QfbPow7A_ge_(9, 1, -9999999)**2
mk4Qfb_class_group5ABC_(1, 0, 9)
>>> n2QfbPow7A_ge_(9, 2, -9999999)
mk4Qfb_class_group5ABC_(1, 0, 9)
>>> n2QfbPow7A_ge_(11, 1, -9999999)
mk4Qfb_class_group5ABC_(1, 1, 3)

>>> n2QfbPow7A_ge_(-1+2**67, 1, 1040)
mk4Qfb_class_group5ABC_(1049, 61, 35170150760170738)
>>> n2QfbPow7A_ge_(-1+2**67, 1, 1040, avoid_A_mod8_eq1=True)
mk4Qfb_class_group5ABC_(1061, 717, 34772373371742914)





mk4Qfb_class_group5ABC_
mk_one6Qfb_class_group5D_
>>> mk4Qfb_class_group5ABC_(111, 0, 113, to_reduce=False)
mk4Qfb_class_group5ABC_(111, 0, 113)
>>> bqf = mk4Qfb_class_group5ABC_(111, 0, 113)
>>> bqf
mk4Qfb_class_group5ABC_(111, 0, 113)
>>> bqf.inv
mk4Qfb_class_group5ABC_(111, 0, 113)
>>> 1/bqf
mk4Qfb_class_group5ABC_(111, 0, 113)
>>> bqf/bqf
mk4Qfb_class_group5ABC_(1, 0, 12543)
>>> bqf.one
mk4Qfb_class_group5ABC_(1, 0, 12543)
>>> bqf**-1
mk4Qfb_class_group5ABC_(111, 0, 113)
>>> bqf**2
mk4Qfb_class_group5ABC_(1, 0, 12543)
>>> bqf**-2
mk4Qfb_class_group5ABC_(1, 0, 12543)



>>> bqf = n2QfbPow7A_ge_(-1+2**67, 1, 77777)
>>> bqf
mk4Qfb_class_group5ABC_(77783, 71695, 474313000896136)
>>> bqf.inv
mk4Qfb_class_group5ABC_(77783, -71695, 474313000896136)
>>> 1/bqf
mk4Qfb_class_group5ABC_(77783, -71695, 474313000896136)
>>> bqf/bqf
mk4Qfb_class_group5ABC_(1, 1, 36893488147419103232)
>>> bqf.one
mk4Qfb_class_group5ABC_(1, 1, 36893488147419103232)
>>> bqf**-1
mk4Qfb_class_group5ABC_(77783, -71695, 474313000896136)
>>> bqf**2
mk4Qfb_class_group5ABC_(6050195089, 1695585529, 6216698828)
>>> bqf**-2
mk4Qfb_class_group5ABC_(6050195089, -1695585529, 6216698828)

>>> bqf**(1<<2)
mk4Qfb_class_group5ABC_(2084119397, 698918375, 17760791404)
>>> bqf**(1<<3)
mk4Qfb_class_group5ABC_(1368606368, -276738689, 26970964834)
>>> bqf**(1<<4)
mk4Qfb_class_group5ABC_(3463141424, 2479907199, 11097142268)
>>> bqf**(1<<5)
mk4Qfb_class_group5ABC_(3859539034, -2968040591, 10129656428)
>>> bqf**(1<<6)
mk4Qfb_class_group5ABC_(75500074, -4776729, 488655068758)



>>> n2QfbPow7A_ge_(-1+2**67, 5788240250//2, 77777)
mk4Qfb_class_group5ABC_(193707721, 193707721, 190507991252)
>>> (-1+2**67) == 193707721*761838257287
True






???(a,b,a)未必是sqrt4one???
    #证明冫二二型歧型平方必为幺元:goto
>>> mk4Qfb_class_group5ABC_(7,1,7)**2
mk4Qfb_class_group5ABC_(1, 1, 49)
>>> mk4Qfb_class_group5ABC_(999,47,999)**2
mk4Qfb_class_group5ABC_(1, 1, 997449)
>>> _.eq_one_()
True



>>> mk4Qfb_class_group5ABC_(999,47,999).whether_ambiguous
True
>>> mk4Qfb_class_group5ABC_(47,47,999).whether_ambiguous
True
>>> mk4Qfb_class_group5ABC_(47,0,999).whether_ambiguous
True
>>> mk4Qfb_class_group5ABC_(47,1,999).whether_ambiguous
False

>>> mk4Qfb_class_group5ABC_(999,47,999).try_factor_D6ambiguous_form_()
2045
>>> mk4Qfb_class_group5ABC_(47,47,999).try_factor_D6ambiguous_form_()
47
>>> mk4Qfb_class_group5ABC_(47,0,999).try_factor_D6ambiguous_form_()
47
>>> mk4Qfb_class_group5ABC_(47,1,999).try_factor_D6ambiguous_form_()
Traceback (most recent call last):
    ...
ValueError: mk4Qfb_class_group5ABC_(47, 1, 999)


__hash__
__eq__
__repr__
__reduce__
    using:binary_quadratic_form7repr
>>> import pickle

>>> bqf = mk4Qfb_class_group5ABC_(999,1,47, to_reduce=False)
>>> {bqf}
{mk4Qfb_class_group5ABC7repr_(999, 1, 47)}
>>> bqf in {bqf}
True
>>> bs = pickle.dumps(bqf)
>>> bs
b'\x80\x04\x95M\x00\x00\x00\x00\x00\x00\x00\x8c\x1dseed.math.BinaryQuadraticForm\x94\x8c\x1cmk4Qfb_class_group5ABC7repr_\x94\x93\x94M\xe7\x03K\x01K/\x87\x94R\x94.'
>>> _bqf = pickle.loads(bs)
>>> _bqf
mk4Qfb_class_group5ABC7repr_(999, 1, 47)
>>> bqf == _bqf
True



>>> bqf = mk4Qfb_class_group5ABC_(999,1,47)
>>> {bqf}
{mk4Qfb_class_group5ABC_(47, -1, 999)}
>>> bqf in {bqf}
True
>>> bs = pickle.dumps(bqf)
>>> bs
b'\x80\x04\x95K\x00\x00\x00\x00\x00\x00\x00\x8c\x1dseed.math.BinaryQuadraticForm\x94\x8c\x17mk4Qfb_class_group5ABC_\x94\x93\x94K/J\xff\xff\xff\xffM\xe7\x03\x87\x94R\x94.'
>>> _bqf = pickle.loads(bs)
>>> _bqf
mk4Qfb_class_group5ABC_(47, -1, 999)
>>> bqf == _bqf
True

















[[
py_adhoc_call   seed.math.BinaryQuadraticForm   @n2QfbPow7A_ge_ ='-1+2**67' =1 =77777
    mk4Qfb_class_group5ABC_(77783, 71695, 474313000896136)
py_adhoc_call   seed.math.BinaryQuadraticForm   @n2QfbPow7A_ge_ ='-1+2**67' ='5788240250//2' =77777
    mk4Qfb_class_group5ABC_(193707721, 193707721, 190507991252)
]]


py_adhoc_call   seed.math.BinaryQuadraticForm   @f
]]]'''#'''
__all__ = r'''
BinaryQuadraticForm
EqvCls4BinaryQuadraticForm
    mk4Qfb_class_group5ABC_
        default4kw7to_reduce
        mk4Qfb_class_group5ABC7repr_
    mk_one6Qfb_class_group5D_
    D5ABC_
    C5DAB_
    check_discriminant7Qfb_
        n2D_
            nk2D_
        D2A_ge_
        D2Qfb7A_ge_
        D2QfbPow7A_ge_
        n2QfbPow7A_ge_



is_primitive7Qfb_
is_reduced7Qfb7negD_
reduce4Qfb7negD_
is_ambiguous_form_7Qfb7negD7reduced_
'''.split()#'''
__all__
r'''[[[
[[
binary_quadratic_form:基础知识:
[A,B,C,x,y::int]:
    [eval4bqf_(A,B,C;x,y) := (A*x**2+B*x*y+C*y**2)]
[A,B,C::int]:
    [bqf2int_set_(A,B,C) := {eval4bqf_(A,B,C;x,y) | [x,y::int]}]
        # 绑定一个整数集合，作为 等价标识 #但似乎由特别排除 [det(T)==-1]
        #       #{由于[A==C]，所以也算使用[det(T)==+1]}[误解:『但但 算法里 却使用了[det(T)==-1]』]
        #       Tp必要性:若允许Tn则[(C,B,A) ~=~ (A,B,C)]即 全都是sqrt4one #好像也没太严重的后果，最多就是ambiguous_form的定义改改#不对！首先 (<*>)是否还合理？其次 不能用 幂方法 分解整数
        # 对(x,y)作可逆变换，只能是 二维线性变换牜整数牜可逆
        # 由于bqf已然允许表达所有二次项，所以(x,y)线性变换后仍是bqf，而且 绑定的整数集合不变

[[T::N-维线性变换牜整数牜可逆] -> [det(T) <- {-1,+1}]]
    proof:
    [det(T) :: int]
    !! [(T**-1) exists]
    [det(T**-1) :: int]
    [det(T)*det(T**-1) == det(T*T**-1) == det(Eye) == 1]
    [det(T) <- {-1,+1}]
[[T::二维线性变换牜整数牜可逆] -> [det(T) <- {-1,+1}]]

[det([a,b;c,d]) == a*d-b*c]
[det(T) == -1]:
    [[Tt:=[1,0;0,-1]] -> [(A,B,C) --> (A,-B,C)]]
    [[Tf:=[0,1;1,0]] -> [(A,B,C) --> (C,B,A)]]
[@[Tn::二维线性变换牜整数牜可逆][det(Tn) == -1] -> ?[Tp::二维线性变换牜整数牜可逆][det(Tp) == +1] -> [Tn==Tt*Tp]]
[@[Tn::二维线性变换牜整数牜可逆][det(Tn) == -1] -> ?[Tp::二维线性变换牜整数牜可逆][det(Tp) == +1] -> [Tn==Tf*Tp]]
[[T::unimodular] <-> [det(T) == +1]]
    # 『Make the unimodular change of variables [_x;_y]:=T*[x;y]』

[(bqf1 ~=~ bqf2) =[def]= [?[Tp::二维线性变换牜整数牜可逆][det(Tp) == +1] -> [bqf1==applyTp4bqf_(Tp;bqf2)]]]

[A,B,C,x,y::int][det(T) == +1][T==[u,w;m,n]]:
    [u*n-w*m==+1]
    [T**-1 == [n,-w;-m,u]]

    [[s,t]~ := T*[x,y]~]
    [s==+u*x+w*y]
    [t==+m*x+n*y]

    [x==+n*s-w*t]
    [y==-m*s+u*t]

    [eval4bqf_(A,B,C;x,y)
    == (A*x**2+B*x*y+C*y**2)
    == (A*(n*s-w*t)**2+B*(n*s-w*t)*(-m*s+u*t)+C*(-m*s+u*t)**2)
    == (C*u^2 - B*w*u + A*w^2)*t^2 + ((B*n - 2*C*m)*u + (-2*A*w*n + B*m*w))*s*t + (A*n^2 - B*m*n + C*m^2)*s^2
    == (C*u^2 - B*w*u + A*w^2)*t^2 + (B*(n*u+m*w) -2*C*m*u -2*A*w*n)*s*t + (A*n^2 - B*m*n + C*m^2)*s^2
    == eval4bqf_(A,-B,C;w,u)*t^2 + (B*(n*u+m*w) -2*C*m*u -2*A*w*n)*s*t + eval4bqf_(A,-B,C;n,m)*s^2
    == eval4bqf_(A,-B,C;n,m)*s^2 + (B*(2*n*u-1) -2*C*m*u -2*A*w*n)*s*t + eval4bqf_(A,-B,C;w,u)*t^2
    == eval4bqf_(A,-B,C;n,m)*s^2 + (-B +2*B*n*u -2*C*m*u -2*A*w*n)*s*t + eval4bqf_(A,-B,C;w,u)*t^2
    == eval4bqf_(eval4bqf_(A,-B,C;n,m),(-B +2*B*n*u -2*C*m*u -2*A*w*n),eval4bqf_(A,-B,C;w,u);s,t)
    ]
    [_A:=eval4bqf_(A,-B,C;n,m)]
    [_B:=(-B +2*B*n*u -2*C*m*u -2*A*w*n)]
    [_C:=eval4bqf_(A,-B,C;w,u)]
    [_B^2-4*_A*_C == B^2-4*A*C]
[[A,B,C,k::int] -> [Qfb(A,B,C) ~=~ Qfb(C, -B, A)]]
    # 调换冫二二型头尾部牜保持等价类
    待定系数:
    _A:
        [n==0]
        [m^2==1]
    _B:
        [n*u==0]
        [m*u==0]
        [w*n==0]
    _C:
        [w^2==1]
        [u==0]
    unimodular:
        [n*u-w*m == +1]
    ==>>:
        [Tp:=[0,1;-1,0]]
        or:[Tp:=[0,-1;1,0]]
    证明:
        [Qfb(C, -B, A) == applyTp4bqf_([0,1;-1,0];Qfb((A,B,C))]

[[A,B,C,k::int] -> [Qfb(A,B,C) ~=~ Qfb(A,B+2*k*A,C+k*(B+k*A))]]
    # [(C+k*(B+k*A)) == eval4bqf_(A,BC;k,1)]
    # 调整冫二二型中部牜保持等价类
    待定系数:
    _A:
        [n^2==1]
        [m==0]
    _B:
        [n*u==1]
        [m*u==0]
        [w*n==-k]
    _C:
        [u==1]
        [w==-k]
    unimodular:
        [n*u-w*m == +1]
    ==>>:
        [Tp:=[1,-k;0,1]]
    证明:
        [Qfb(A,B+2*k*A,C+k*(B+k*A)) == applyTp4bqf_([1,-k;0,1];Qfb((A,B,C))]

A=varlower('A)
B=varlower('B)
C=varlower('C)
s=varhigher('s)
t=varhigher('t)
(A*(n*s-w*t)^2+B*(n*s-w*t)*(-m*s+u*t)+C*(-m*s+u*t)^2)
    (C*u^2 - B*w*u + A*w^2)*t^2 + ((B*n - 2*C*m)*u + (-2*A*w*n + B*m*w))*s*t + (A*n^2 - B*m*n + C*m^2)*s^2
        # => (_A,_B,_C)
((-B +2*B*n*u -2*C*m*u -2*A*w*n)^2 -4*(A*n^2 - B*m*n + C*m^2)*(C*u^2 - B*w*u + A*w^2))%(u*n-w*m-1)
    -4*C*A + B^2
        # => [_B^2-4*_A*_C == B^2-4*A*C]
使用原值:
(((B*n - 2*C*m)*u + (-2*A*w*n + B*m*w))^2 -4*(A*n^2 - B*m*n + C*m^2)*(C*u^2 - B*w*u + A*w^2))
    (-4*C*A + B^2)*n^2*u^2 + (8*C*A - 2*B^2)*m*w*n*u + (-4*C*A + B^2)*m^2*w^2
(((B*n - 2*C*m)*u + (-2*A*w*n + B*m*w))^2 -4*(A*n^2 - B*m*n + C*m^2)*(C*u^2 - B*w*u + A*w^2)) == (B^2-4*C*A)*(n*u-w*m)^2
    1
        # 使用原值=> (%(u*n-w*m-1)) 是必要的
==>>:
[A,B,C::int][det(T) == +1][T==[u,w;m,n]]:
    [_A:=eval4bqf_(A,-B,C;n,m)]
    [_B:=(-B +2*B*n*u -2*C*m*u -2*A*w*n)]
    [_C:=eval4bqf_(A,-B,C;w,u)]
    [applyTp4bqf_(T;bqf@(A,B,C)) := (_A,_B,_C)]
[eqv4bqf_(bqfL, bqfR) := [?[Tp::二维线性变换牜整数牜可逆][det(Tp) == +1] -> [bqfL==applyTp4bqf_(Tp,bqfR)]]]
    [Qfb(1,1,4) ~=!=~ Qfb(2,1,2)]
        [D==-15]
        [1 == eval4bqf_(1,1,4;1,0)]
        [1 < 2 == min(bqf2int_set_(2,1,2) \-\{0})]
        [1 !<- bqf2int_set_(2,1,2)]
标准形态纟等价类:distinguished_form/reduced_form #见下面:二二型等价类中简化型唯一
    to find distinguished form: This is particularly easy to do in the case of binary quadratic forms of negative discriminant.
[D > 0]:
    bqf2int_set_ 同时包含 正负数
        ((2*A*x+B*y)**2 -D)///(4*A)
[D == 0]:
    bqf2int_set_ 只包含 平方数///常量系数
        (2*A*x+B*y)**2///(4*A)
[D < 0]:
    bqf2int_set_ 不能同时包含 正负数
        ((2*A*x+B*y)**2 +(-D))///(4*A)
    !! [B^2-4*A*C == D < 0]
    [A*C > 0] # A,C 同号
    [[0==min(bqf2int_set_(A,B,C))] <-> [0==max(bqf2int_set_(-A,-B,-C))]]
        # [[bqf2int_set_(A,B,C)不含 负数] <-> [bqf2int_set_(-A,-B,-C)不含 正数]]


只考虑:[D<0][A>0]
    => [C>0]

[A,B,C::int][A,C>0][B^2-4*A*C == D < 0]:
    [is_reduced7Qfb7negD_(Qfb(A,B,C)) := ([C>A>=B>-A]+[C==A>=B>=0])]

Algorithm 5.6.2 (Reduction for negative discriminant).
1.  [Replacement loop]
    # [A,C > 0][D < 0]
    while(A > C or B > A or B <= −A) {
        # [A,C > 0][D < 0]
        if(A > C) {(A,B,C) := (C,−B,A);} // "Type (1)" move.
            # applyTp4bqf_(Tt*Tf;...)
            # !! 调换冫二二型头尾部牜保持等价类:[Qfb(C, -B, A) == applyTp4bqf_([0,1;-1,0];Qfb((A,B,C))]
            # A下降,A保正
        # [0 < A <= C]
        if(A <= C and (B > A or B <= −A)) {
            Find Bx,Cx such that the three conditions:
                [Bx =[%(2*A)]= B]
                [−A < Bx <= A]
                [Bx^2-4*A*Cx= B^2-4*A*C]
                hold;
            # !! 调整冫二二型中部牜保持等价类:[Qfb(A,B+2*k*A,C+k*(B+k*A)) == applyTp4bqf_([1,-k;0,1];Qfb((A,B,C))]
            # [Bx := -(A-1) +(B+A-1)%(2*A)]
            # [Cx := (Bx**2-D)///(4*A)]
            # [−A < Bx <= A <= C]
            (A,B,C) := (A,Bx,Cx); // "Type (2)" move.
            # [−A < B <= A]
            # A不变
        }
        # A只降不升,A保正=>循环必止
    }
    # not (A > C or B > A or B <= −A)
    # [−A < B <= A <= C]

2.  [Final adjustment]
    if(A == C and −A < B < 0) {(A,B,C) := (A,−B,C);}
            # applyTp4bqf_(Tt;...)
            # ???这里使用了[det(T) == -1]
            # <==> if(A == C and −A < B < 0) {(A,B,C) := (C,−B,A);}
            # <==>applyTp4bqf_(Tt*Tf;...)
            # 这里使用了[det(T) == +1]
    return (A,B,C);

Moves of type (2) leave the initial coordinate A unchanged, while a move of type (1) reduces it.
    So there can be at most finitely many type (1) moves.
    Further, we never do two type (2) moves in a row.
    Thus the algorithm terminates for each input.

[A,B,C::int][A,C>0][B^2-4*A*C == D < 0]:
    # !! 调整冫二二型中部牜保持等价类:[Qfb(A,B+2*k*A,C+k*(B+k*A)) == applyTp4bqf_([1,-k;0,1];Qfb((A,B,C))]
    # !! 调换冫二二型头尾部牜保持等价类:[Qfb(C, -B, A) == applyTp4bqf_([0,1;-1,0];Qfb((A,B,C))]
    [_reduce4Qfb7negD__7Type1_(bqf@Qfb(A,B,C)) := (if [A<=C] then bqf else Qfb(C,-B,A))]
    [_reduce4Qfb7negD__7Type2_(bqf@Qfb(A,B,C)) := (if [−A < B <= A] then bqf else let [k:=(B+(A-1))//(2*A)] in Qfb(A,B-2*k*A,C-k*(B-k*A)))]
    [_reduce4Qfb7negD__7FinalAdjustment(bqf@Qfb(A,B,C)) := (if [A==C][B < 0] then Qfb(C,-B,A) else bqf)]
    [reduce4Qfb7negD_(bqf@Qfb(A,B,C)) := if [−A < B <= A <= C] then _reduce4Qfb7negD__7FinalAdjustment(bqf) else reduce4Qfb7negD_(_reduce4Qfb7negD__7Type2_(_reduce4Qfb7negD__7Type1_(bqf)))]

[[bqf.D < 0][bqf.A > 0][is_reduced7Qfb7negD_(bqf)] -> @[Tp::二维线性变换牜整数牜可逆][det(Tp) == +1] -> [_bqf:=applyTp4bqf_(Tp;bqf.A)] -> [bqf.A <= _bqf.A][[bqf.A == _bqf.A] -> [bqf.C <= _bqf.C]][[bqf.A == _bqf.A][bqf.C == _bqf.C] -> [[bqf.B==_bqf.B] + [bqf.B==-_bqf.B][bqf.A<-{bqf.B,bqf.C}]]]]
    # 二二型等价类中简化型头部最小+二二型等价类耂头部最小耂子集中简化型尾部最小+二二型等价类耂头尾部词典序最小耂子集不止包含简化型则简化型耂头部中部尾部三值中必有两者相同
    [[proof:
    [Qfb(A,B,C) := bqf]
    [Qfb(_A,_B,_C) := _bqf]
    [[u,w;m,n] := Tp]

    [A>0]
    [C>0]
    !! [is_reduced7Qfb7negD_(bqf)]
    [C>=A>=abs(B)]

    [_A==eval4bqf_(A,-B,C;n,m)]
    [_C==eval4bqf_(A,-B,C;w,u)]
    [_B==(-B +2*B*n*u -2*C*m*u -2*A*w*n)]

    * [n==0==m]:
        !! [det(Tp) == +1]
        [(n,m) =!= (0,0)]
        _L
    * [m==0][n=!=0]:
        [n^2>0]
        !! [A>0]
        [_A==A*n^2 >= A]
        [[_A>=C] <-> [m==0][C<=A*n^2]]
        [[_A==C] <-> [m==0][C==A*n^2]]
        [[_A==A] <-> [m==0][abs(n) == 1]]
    * [n==0][m=!=0]:
        [m^2>0]
        !! [C>0]
        !! [C>=A]
        [_A==C*m^2 >= C >= A]
        [_A >= C]
        [[_A>=C] <-> [n==0][m=!=0]]
        [[_A==C] <-> [n==0][abs(m) == 1]]
        [[_A==A] <-> [C==A][n==0][abs(m) == 1]]
    * [n=!=0][m=!=0][abs(n)>=abs(m)]:
        [m^2>0]
        [_A==(A*n^2-B*n*m+C*m^2)
        >= (A*n^2-abs(B*n*m)+C*m^2)
        !! [A>=abs(B)]
        >= (A*n^2-abs(A*n*m)+C*m^2)
        == abs(A*n)*(abs(n)-abs(m))+C*m^2
        !! [abs(n)>=abs(m)]
        >= C*m^2
        !! [m^2>0]
        !! [C>0]
        >= C
        !! [C>=A]
        >= A
        ]
        [_A >= C]
        [_A >= A]
        [[_A>=C] <-> [n=!=0][m=!=0][abs(n)>=abs(m)]]
        [[_A==C] <-> [A==abs(B)][abs(m) == 1 == abs(n)][(B*n*m) > 0]]
        [[_A==A] <-> [C==A==abs(B)][abs(m) == 1 == abs(n)][(B*n*m) > 0]]
        [A==abs(B)]:
            !! [is_reduced7Qfb7negD_(bqf)]
            [([C>A>=B>-A]+[C==A>=B>=0])]
            [B > -A]
            !! [A==abs(B)]
            [B == A]
        [[A==abs(B)] -> [B == A]]
        !! [[_A==C] <-> [A==abs(B)][abs(m) == 1 == abs(n)][(B*n*m) > 0]]
        [[_A==C] <-> [A==B][abs(m) == 1 == abs(n)][(n*m) > 0]]
        [[_A==C] <-> [A==B][abs(m) == 1][n == m]]
        [[_A==A] <-> [A==B==C][abs(m) == 1][n == m]]
    * [n=!=0][m=!=0][abs(n)<abs(m)]:
        [n^2>0]
        [_A==(A*n^2-B*n*m+C*m^2)
        >= (A*n^2-abs(B*n*m)+C*m^2)
        !! [C>=abs(B)]
        >= A*n^2+(C*m^2-abs(C*n*m))
        == A*n^2+abs(C*m)*(abs(m)-abs(n))
        !! [abs(n)<abs(m)]
        !! [C>0]
        !! [m=!=0]
        >= A*n^2+C
        !! [n^2>0]
        >= A + C
        !! [A>0]
        > C
        !! [C>=A]
        >= A
        ]
        [_A > C]
        [[_A>=C] <-> [n=!=0][m=!=0][abs(n)<abs(m)]]
        [[_A==C] -> _L]
        [[_A==A] -> _L]
        [_A >= C]
        [_A >= A]
    ==>>:
    [_A >= A]
    [[_A >= C] <-> [[m=!=0] + [m==0][C<=A*n^2]]]
    [[_A==C] <-> [[C==A][m==0][abs(n) == 1] + [n==0][abs(m) == 1] + [A==B][abs(m) == 1][n == m]]]
    [[_A==A] <-> [[m==0][abs(n) == 1] + [C==A][n==0][abs(m) == 1] + [A==B==C][abs(m) == 1][n == m]]]

    [[_A==A] -> [[m==0][abs(n) == 1] + [C==A][abs(n) <= abs(m) == 1]][n <- {0,m}]]

    !! 同理
    [_C >= A]
    [[_C >= C] <-> [[u=!=0] + [u==0][C<=A*w^2]]]
    [[_C==C] <-> [[C==A][u==0][abs(w) == 1] + [w==0][abs(u) == 1] + [A==B][abs(u) == 1][w == u]]]
    [[_C==A] <-> [[u==0][abs(w) == 1] + [C==A][w==0][abs(u) == 1] + [A==B==C][abs(u) == 1][w == u]]]

    [[_C==A] -> [[u==0][abs(w) == 1] + [C==A][abs(w) <= abs(u) == 1]][w <- {0,u}]]

    [_A == A]:
        !! [[_A==A] <-> [[m==0][abs(n) == 1] + [C==A][n==0][abs(m) == 1] + [A==B==C][abs(m) == 1][n == m]]]
        [[m==0][abs(n) == 1] + [C==A][abs(n) <= abs(m) == 1][n <- {0,m}]]
        * [m==0][abs(n) == 1]:
            !! [det(Tp) == +1]
            [u*n-w*m == +1]
            !! [m==0]
            [u*n-w*0 == +1]
            [u*n == +1]
            [u == n]
            [Tp == [u,w;0,u]]
            !! [abs(n) == 1]
            [abs(u) == 1]
            [u =!= 0]
            !! [[_C >= C] <-> [[u=!=0] + [u==0][C<=A*w^2]]]
            [_C >= C]
            [_C == C]:
                !! [[_C==C] <-> [[C==A][u==0][abs(w) == 1] + [w==0][abs(u) == 1] + [A==B][abs(u) == 1][w == u]]]
                !! [abs(u) == 1]
                [[w==0] + [A==B][w == u]]
                * [w==0]:
                    [Tp == [u,0;0,u]]
                    [bqf == _bqf]
                    [_B == B]
                * [A==B][w == u]:
                    [Tp == [w,w;0,w]]
                    !! [_B==(-B +2*B*n*u -2*C*m*u -2*A*w*n)]
                    [_B==-B][B==A]
                    # [(x+y)^2 -(x+y)*y == x^2 +x*y]
                    # [(x-y)^2 +(x-y)*y == x^2 -x*y]
                [[_B==B] + [_B==-B][B==A]]
            [_C == C]:
                [[_B==B] + [_B==-B][B==A]]
        * [C==A][abs(n) <= abs(m) == 1][n <- {0,m}][[C==A][n==0][abs(m) == 1] + [A==B==C][abs(m) == 1][n == m]]:
            !! [_C >= A]
            [_C >= A == C]
            [_C >= C]
            [n <- {0,m}]
            [abs(m) == 1]
            [C==A]
            * [C==A][n==0][abs(m) == 1]:
                !! [det(Tp) == +1]
                !! [n==0]
                [w == -m]
                [w =!= 0]
                !! [n==0]
                [Tp == [u,w;-w,0]]
                [_C == C]:
                    !! [_A == A][C==A][_C == C]
                    [_A==_C==A==C]
                    !! [[_C==C] <-> [[C==A][u==0][abs(w) == 1] + [w==0][abs(u) == 1] + [A==B][abs(u) == 1][w == u]]]
                    !! [w =!= 0]
                    [[C==A][u==0][abs(w) == 1] + [A==B][abs(u) == 1][w == u]]
                    * [C==A][u==0][abs(w) == 1]:
                        [Tp == [0,w;-w,0]]
                        [_bqf == Qfb(C,-B,A)]
                        !! [_A==_C==A==C]
                        [_bqf == Qfb(A,-B,C)]
                        [_B==-B][C==A]
                    * [A==B][abs(u) == 1][w == u]:
                        !! [_A==_C==A==C]
                        !! [A==B]
                        [_A==_C==A==C==B]
                        [Tp == [w,w;-w,0]]
                        !! [_B==(-B +2*B*n*u -2*C*m*u -2*A*w*n)]
                        [_B==-B+2*C==B==A]
                        [_B==B==A]
                        [_bqf == bqf]
                    [[_B==-B][C==A] + [_B==B]]
                [_C == C]:
                    [[_B==-B][C==A] + [_B==B]]
            * [A==B==C][abs(m) == 1][n == m]:
                [Tp == [u,w;m,m]]
                !! [det(Tp) == +1]
                [u*m-w*m == +1]
                [(u-w)*m == +1]
                [(u-w) == m]
                [u == w+m]
                [Tp == [w+m,w;m,m]]
                !! [abs(m) == 1]
                !! [(u-w) == m]
                [u=!=w]
                [_C == C]:
                    !! [_A == A][C==A][_C == C][A==B==C]
                    [_A==_C==A==C==B]
                    !! [[_C==C] <-> [[C==A][u==0][abs(w) == 1] + [w==0][abs(u) == 1] + [A==B][abs(u) == 1][w == u]]]
                    !! [u=!=w]
                    [[C==A][u==0][abs(w) == 1] + [w==0][abs(u) == 1]]
                    * [C==A][u==0][abs(w) == 1]:
                        !! [(u-w) == m]
                        [w == -m]
                        [Tp == [0,-m;m,m]]
                        !! [_A==_C==A==C==B]
                        !! [_B==(-B +2*B*n*u -2*C*m*u -2*A*w*n)]
                        [_B==-B+2*A==B==A]
                        [_B==B==A]
                        [_bqf == bqf]
                    * [w==0][abs(u) == 1]:
                        !! [(u-w) == m]
                        [u == m]
                        [Tp == [m,0;m,m]]
                        !! [_A==_C==A==C==B]
                        !! [_B==(-B +2*B*n*u -2*C*m*u -2*A*w*n)]
                        [_B==-B][B==A]
                    [[_B==B] + [_B==-B][B==A]]
                [_C == C]:
                    [[_B==B] + [_B==-B][B==A]]
            [_C == C]:
                [[_B==-B][C==A] + [_B==B]]or[[_B==B] + [_B==-B][B==A]]
                [[_B==B] + [_B==-B][A<-{B,C}]]
            [_C == C]:
                [[_B==B] + [_B==-B][A<-{B,C}]]
        ==>>:
        [_C >= C]
        [_C == C]:
            [[_B==B] + [_B==-B][B==A]]or[[_B==B] + [_B==-B][A<-{B,C}]]
            [[_B==B] + [_B==-B][A<-{B,C}]]
            [abs(_B) == abs(B)]
    [[_A==A] -> [_C >= C]]
    [[_A==A][_C == C] -> [[_B==B] + [_B==-B][A<-{B,C}]]]

    DONE
    ]]
[[bqf1.D < 0][bqf1.A > 0][is_reduced7Qfb7negD_(bqf1)] -> [bqf2.D < 0][bqf2.A > 0][is_reduced7Qfb7negD_(bqf2)] -> [bqf1 ~=~ bqf2] -> [bqf1 == bqf2]]
    #二二型等价类中简化型唯一
    [[proof:
    !! [bqf1 ~=~ bqf2]
    ?[Tp::二维线性变换牜整数牜可逆][det(Tp) == +1] :=> [bqf1==applyTp4bqf_(Tp;bqf2)]
    !! 二二型等价类中简化型头部最小
    [bqf2.A <= bqf1.A]
    !! 同理
    [bqf1.A <= bqf2.A]
    !! [bqf2.A <= bqf1.A]
    [bqf1.A == bqf2.A]

    !! 二二型等价类耂头部最小耂子集中简化型尾部最小
    !! [bqf1.A == bqf2.A]
    [bqf2.C <= bqf1.C]
    !! 同理
    [bqf1.C <= bqf2.C]
    !! [bqf2.C <= bqf1.C]
    [bqf1.C == bqf2.C]

    !! [bqf1 ~=~ bqf2]
    [bqf1.D == bqf2.D]
    !! [bqf1.A == bqf2.A]
    !! [bqf1.C == bqf2.C]
    [bqf1.B^2 == bqf2.B^2]
    [abs(bqf1.B) == abs(bqf2.B)]
    [bqf1.B =!= bqf2.B]:
        [0 =!= bqf1.B == -bqf2.B]
        [[bqf1.B < 0]or[bqf2.B < 0]]
        !! 二二型等价类耂头尾部词典序最小耂子集不止包含简化型则简化型耂头部中部尾部三值中必有两者相同
        !! [is_reduced7Qfb7negD_(bqf1)]
        [A <- {C, bqf1.B}]
        !! 同理
        [A <- {C, bqf2.B}]
        !! [0 =!= bqf1.B == -bqf2.B]
        [A <- {C, bqf1.B}/-\{C, bqf2.B} == {C}]
        [A == C]
        * [bqf1.B < 0]:
            [Qfb(A,B,C) := bqf1]
            [B < 0]
            !! [is_reduced7Qfb7negD_(bqf1)]
            [([C>A>=B>-A]+[C==A>=B>=0])]
            !! [B < 0]
            [C>A>=B>-A]
            !! [A == C]
            _L
        * [bqf2.B < 0]:
            !! 同上
            _L
        _L
    [bqf1.B == bqf2.B]
    [bqf1 == bqf2]
    DONE
    ]]


[[bqf.D < 0][is_reduced7Qfb7negD_(bqf)] -> [0 < bqf.A <= sqrt(-D/3)]]
    proof:
    [Qfb(A,B,C) := bqf]
    !! [is_reduced7Qfb7negD_(bqf)]
    [A,C>0>D][([C>A>=B>-A]+[C==A>=B>=0])]
    [abs(B) <= A <= C]
    !! [D == B**2-4*A*C]
    [-D == 4*A*C-B**2 >= 4*A*A-A**2 == 3*A**2]
    [-D >= 3*A**2]
    !! [A > 0]
    [0 < A <= sqrt(-D/3)]


5.6.3 Composition and the class group

[D::int7nonsquare][bqf1:=Qfb(A1,B0,C1)][bqf2:=Qfb(A2,B0,C2)][bqf1.D == D][bqf2.D == D][A1*A2 =!= 0]:
    # ???这里不要求 [D < 0]
    # 这里要求 [B0 贯同]
    !! [B0^2-4*A1*C1 == D == B0^2-4*A2*C2]
    [A1*C1 == A2*C2]
    !! [A1*A2 =!= 0]
    [C1/A2 == C2/A1] #未必整除
    [A3:=(A1*A2)]
    [C3:=(C1/A2)]
    [x3:=(x1*x2 -(C1/A2)*y1*y2)]
    [y3:=(A1*x1*y2+A2*x2*y1+B0*y1*y2)]
    [eval4bqf_(A1,B0,C1;x1,y1)*eval4bqf_(A2,B0,C2;x2,y2) =[%(A1*C1-A2*C2)]= eval4bqf_(A3,B0,C3;x3,y3)] # 二二型乘法合理性冫注入相应整数集合
    [C1%A2==0]:
        [bqf3:=Qfb(A3,B0,C3)]
        [bqf3==Qfb(A1*A2,B0,C1///A2)]
        [bqf2int_set_(bqf1) :*: bqf2int_set_(bqf2) |<=| bqf2int_set_(bqf3)]
B0='B0
A1='A1
C1='C1
x1='x1
y1='y1
A2='A2
C2='C2
x2='x2
y2='y2

C2=varhigher('C2,'x1)
C1=varhigher('C1,'x1)
A2=varhigher('A2,'x1)
A1=varhigher('A1,'x1)
B0=varhigher('B0,'x1)

eval4bqf_(A,B,C,x,y) = (A*x^2+B*x*y+C*y^2)
f=eval4bqf_(A1,B0,C1,x1,y1)*eval4bqf_(A2,B0,C2,x2,y2)
    (y2^2*y1*x1*B0 + (y2^2*x1^2*A1 + y2^2*y1^2*C1))*C2 + ((x2^2*y1*x1*B0 + (x2^2*x1^2*A1 + x2^2*y1^2*C1))*A2 + (y2*x2*y1*x1*B0^2 + (y2*x2*x1^2*A1 + y2*x2*y1^2*C1)*B0))

polcoef(f,1,B0)
    y2^2*y1*x1*C2 + (x2^2*y1*x1*A2 + (y2*x2*x1^2*A1 + y2*x2*y1^2*C1))
polcoef(f,2,B0)
    y2*x2*y1*x1

g=f%(A1*C1-A2*C2)
    ((x2^2*y1*x1*B0 + (x2^2*x1^2*A1 + x2^2*y1^2*C1))*A2^2 + (y2*x2*y1*x1*B0^2 + (y2*x2*x1^2*A1 + y2*x2*y1^2*C1)*B0)*A2 + (y2^2*y1*x1*C1*A1*B0 + (y2^2*x1^2*C1*A1^2 + y2^2*y1^2*C1^2*A1)))/A2
polcoef(g,1,B0)
    (x2^2*y1*x1*A2^2 + (y2*x2*x1^2*A1 + y2*x2*y1^2*C1)*A2 + y2^2*y1*x1*C1*A1)/A2
polcoef(g,2,B0)
    y2*x2*y1*x1

fail:polcoef(g,1,A1*A2)
fail:divrem(g,A1*A2)
polcoef(polcoef(g,1,A1),1,A2)
    x2^2*x1^2
polcoef(polcoef(g,1,C1),-1,A2)
    y2^2*y1*x1*A1*B0 + y2^2*x1^2*A1^2
h = g -eval4bqf_((A1*A2),B0,(C1/A2),(x2*x1),(y2*x1*A1))
    ((x2^2*y1*x1*B0 + x2^2*y1^2*C1)*A2^2 + (y2*x2*y1*x1*B0^2 + y2*x2*y1^2*C1*B0)*A2 + (y2^2*y1*x1*C1*A1*B0 + y2^2*y1^2*C1^2*A1))/A2
    ...还是直接抄书吧

A3=(A1*A2)
C3=(C1/A2)
x3=(x1*x2 -(C1/A2)*y1*y2)
y3=(A1*x1*y2+A2*x2*y1+B0*y1*y2)
0==(eval4bqf_(A1,B0,C1,x1,y1)*eval4bqf_(A2,B0,C2,x2,y2) - eval4bqf_(A3,B0,C3,x3,y3))%(A1*C1-A2*C2)
    1
        #证明:二二型乘法合理性冫注入相应整数集合

#重点是:B0^2
x3*y1*y2+C3*(y1*y2)^2
    y2*x2*y1*x1
        # polcoef(f,2,B0)

???(+B * -B)???
fn=eval4bqf_(A1,+B0,C1,x1,y1)*eval4bqf_(A2,-B0,C2,x2,y2)
    (y2^2*y1*x1*B0 + (y2^2*x1^2*A1 + y2^2*y1^2*C1))*C2 + ((x2^2*y1*x1*B0 + (x2^2*x1^2*A1 + x2^2*y1^2*C1))*A2 + (-y2*x2*y1*x1*B0^2 + (-y2*x2*x1^2*A1 - y2*x2*y1^2*C1)*B0))
fc=(f+fn)/2
    (y2^2*y1*x1*B0 + (y2^2*x1^2*A1 + y2^2*y1^2*C1))*C2 + (x2^2*y1*x1*B0 + (x2^2*x1^2*A1 + x2^2*y1^2*C1))*A2
fd=(f-fn)/2
    y2*x2*y1*x1*B0^2 + (y2*x2*x1^2*A1 + y2*x2*y1^2*C1)*B0
f==fc+fd
    1
fn==fc-fd
    1

# [D::int7nonsquare][bqf1:=Qfb(A1,B0,C1)][bqf2:=Qfb(A2,B0,C2)][bqf1.D == D][bqf2.D == D][A1*A2 =!= 0][C1%A2==0]:
[bqf1,bqf2::Qfb][bqf1.B == bqf2.B][bqf1.D == bqf2.D][Qfb(A1,B0,C1):=bqf1][Qfb(A2,B0,C2):=bqf2][C1%A2==0]:
    [(bqf1 <*> bqf2) =[def]= Qfb(A1*A2,B0,C1///A2)]



[A,B,C::int]:
    [is_primitive7Qfb_(A,B,C) := [gcd(A,B,C) == 1]] #not:are_pairwise_coprime
[D::int7nonsquare][D%4 < 2]:
    [eqvcls7Qfb{D;bqf} =[def]= {_bqf | [_bqf::Qfb][_bqf.D == D][_bqf ~=~ bqf]}]
        # [_bqf ~=~ bqf] ==>> [bqf2int_set_(_bqf) == bqf2int_set_(bqf)]
        # 记为:『{<Qfb(A,B,C)>}』
    [[D<0] -> [eqvcls7Qfb{D;bqf} == {_bqf | [_bqf::Qfb][_bqf.D == D][reduce4Qfb7negD_(_bqf) ~=~ reduce4Qfb7negD_(bqf)]}]]
    [CC{D} =[def]= {eqvcls7Qfb{D;bqf} | [bqf::Qfb][bqf.D == D][is_primitive7Qfb_(bqf)]}]
        the set of equivalence classes of primitive binary quadratic forms of discriminant D;
            where each class is the set of those forms equivalent to a given form.
            We shall use the notation <a,b,c> for the equivalence class containing the form (a,b,c).

[[bqf11,bqf12,bqf21,bqf22::Qfb] -> [bqf11 ~=~ bqf12][bqf21 ~=~ bqf22][bqf11.D == bqf21.D] -> [bqf11.B == bqf21.B][bqf12.B == bqf22.B] -> [bqf11.C % bqf21.A == 0][bqf12.C % bqf22.A == 0] -> [(bqf11 <*> bqf21) ~=~ (bqf12 <*> bqf22)]]
    #二二型乘法合理性冫等价类乘法合理
    TODO:proof:???没头绪
        #Tp必要性:若允许Tn则[(C,B,A) ~=~ (A,B,C)]即 全都是sqrt4one #首先 (<*>)是否还合理？其次 不能用 幂方法 分解整数
    要不直接忽略B，即 同时允许使用{Tp,Tn}:
        Qfb(A,B,C)-->_Qfb(D,A,C) or __Qfb(D,CA,A)
        因为 _A,_C 特别简单:
            [_A:=eval4bqf_(A,-B,C;n,m)]
            [_C:=eval4bqf_(A,-B,C;w,u)]
        applyTp4bqf_ --> applyTpTn4bqf_
        [is_reduced7Qfb7negD_(Qfb(A,B,C)) := ([C>A>=B>-A]+[C==A>=B>=0])]
        -->:
        [is_reduced7Qfb7negD_(Qfb(A,B,C)) := [C>=A>=B>=0]]
        [B==+sqrt(D+4*A*C)]
            [eval4bqf7DCA_(D,CA,A;x,y) := eval4bqf_(A,-sqrt(D+4*CA),CA/A;x,y)]
            [_A:=eval4bqf7DCA_(D,CA,A;n,m)]
            [_C:=eval4bqf7DCA_(D,CA,A;w,u)]
    ==>>:
eval4bqf7DCA_(D,CA,A,x,y) = eval4bqf_(A,-sqrt(D+4*CA),CA/A,x,y)
n4T5duwm_(det,u,w,m) = ((det+w*m)/u)
applyTpTn4bqf_(det,u,w,m,D,CA,A) = {
    ;local(n,Ax,Cx,CAx)
    ;n=n4T5duwm_(det,u,w,m)
    ;Ax=eval4bqf7DCA_(D,CA,A,n,m)
    ;Cx=eval4bqf7DCA_(D,CA,A,w,u)
    ;CAx=Cx*Ax
    ;return([D,CAx,Ax])
}





[@[bqf11,bqf21::Qfb][bqf11.D == bqf21.D][is_primitive7Qfb_(bqf11)][is_primitive7Qfb_(bqf21)] -> ?[bqf12,bqf22::Qfb] -> [bqf11 ~=~ bqf12][bqf21 ~=~ bqf22][bqf12.B == bqf22.B][1==gcd(bqf12.A, bqf22.A)]]
    #no:[bqf11.B == bqf21.B]
    #二二型乘法实现步骤冫转化为可乘
    [Qfb(A11,B11,C11) := bqf11]
    [Qfb(A21,B21,C21) := bqf21]
    [Qfb(A12,B12,C12) := bqf12]
    [Qfb(A22,B22,C22) := bqf22]

    !! [1==gcd(bqf12.A, bqf22.A)]
    [1==gcd(A12, A22)]
        #no:[1==gcd(A11, A21)]
    !! [bqf12.B == bqf22.B]
    [B12 == B22]
        #no:[B11 == B21]
    [B00 := B22]



    [ps4A11:=factorization{bqf11.A}.keys()]
    [ps4A21:=factorization{bqf21.A}.keys()]
    [ps4C11:=factorization{bqf11.C}.keys()]
    [ps4C21:=factorization{bqf21.C}.keys()]

    !! D,B相同
    [A12*C12 == A22*C22]
        #no:[B11 == B21]
        #bug:[A11*C11 == A21*C21]
    # 分解:原文:[A21==m1*m2*m3]
    #   感觉不太对:少了m4
    #       改正: m1--m1m4 或者 m2-->m2m4
    ?m1,m2,m3,m4 :=> [A21==m1*m2*m3*m4] &&:
        [ps4m1 := (ps4A21 /-\ (ps4A11 \-\ ps4C11))]
        [ps4m2 := (ps4A21 /-\ (ps4C11 \-\ ps4A11))]
        [ps4m3 := (ps4A21 /-\ (ps4A11 /-\ ps4C11))]
        [ps4m4 := (ps4A21 \-\ (ps4A11 \-/ ps4C11))]
        ==>>:
        [ps4m2m4 := (ps4A21 \-\ ps4A11)]
        ==>>:
        [m2m4:=coprime_part_of_to_(A21,A11)]
        [m1:=noncoprime_part_of_to_(A21,coprime_part_of_to_(A11,C11))]
        [m3:=noncoprime_part_of_to_(A21,gcd(A11,C11))]

    ?x1,y1 :=> [1==gcd(A21,eval4bqf_(bqf11;x1,y1))][y1%x1 == 1]
        [m2m4 := m2*m4]
        !! [1==gcd(m1,(A21///m1))]
        ?u1,v1 :=> [1==u1*m1+v1*(A21///m1)]
        [1==gcd(u1,(A21///m1))]
        [1==gcd(u1,m2m4)]
        !! [1==gcd(m2m4,(A21///m2m4))]
        [1==gcd(m2m4,u1*(A21///m2m4))]
        ?u2,v2 :=> [1==u2*m2m4+v2*(u1*(A21///m2m4))]
        [x1:=u1*m1]
        [y1:=u2*m2m4]

        !! [1==u1*m1+v1*(A21///m1)]
        [1==x1+v1*(A21///m1)]
        [x1%(A21///m1) == 1]
        [x1%(m2*m3*m4) == 1]
        [x1%m3 == 1]
        [x1%m2m4 == 1]
        [x1%m1 == 0]

        !! [1==u2*m2m4+v2*(u1*(A21///m2m4))]
        [1==y1+v2*(u1*(A21///m2m4))]
        [y1%(u1*(A21///m2m4)) == 1]
        [y1%(u1*m1 * m3) == 1]
        [y1%m3 == 1]
        [y1%x1 == 1]
        [y1%m1 == 1]
        [y1%m2m4 == 0]

        [z11 := eval4bqf_(bqf11;x1,y1)]
        !! [x1%m2m4 == 1]
        !! [y1%m2m4 == 0]
        [eval4bqf_(bqf11;x1,y1) =[%m2m4]= A11]
        [z11 =[%m2m4]= A11]
        !! [1==gcd(m2m4, A11)]
        [1==gcd(m2m4,z11)]

        !! [y1%x1 == 1]
        [eval4bqf_(bqf11;x1,y1) =[%x1]= C11]
        [z11 =[%x1]= C11]
        !! [x1%m1 == 0]
        [z11 =[%m1]= C11]
        !! [1==gcd(m1, C11)]
        [1==gcd(m1,z11)]
        !! [1==gcd(m2m4,z11)]
        [1==gcd(m1*m2m4,z11)]

        !! [x1%m3 == 1]
        !! [y1%m3 == 1]
        [eval4bqf_(bqf11;x1,y1) =[%m3]= (A11+B11+C11)]
        [z11 =[%m3]= (A11+B11+C11)]

        [p::prime][m3%p==0]:
            !! [@[p::prime][m3%p==0] -> [A11%p==0][C11%p==0]]
            [A11%p==0][C11%p==0]
            [gcd(A11,C11)%p == 0]

            !! [is_primitive7Qfb_(bqf11)]
            [1==gcd(A11,B11,C11)]
            [1==gcd(B11,gcd(A11,C11))]
            !! [gcd(A11,C11)%p == 0]
            [1==gcd(B11,p)]
            [B11%p=!=0]
            !! [A11%p==0][C11%p==0]
            [(A11+B11+C11)%p=!=0]
        [@[p::prime][m3%p==0] -> [(A11+B11+C11)%p=!=0]]
        [1==gcd(m3,(A11+B11+C11))]
        !! [z11 =[%m3]= (A11+B11+C11)]
        [1==gcd(m3,z11)]
        !! [1==gcd(m1*m2m4,z11)]
        [1==gcd(m1*m2m4*m3,z11)]
        [1==gcd(A21,z11)]
        [1==gcd(A21,eval4bqf_(bqf11;x1,y1))]
            #DONE

        !! [1==u2*m2m4+v2*(u1*(A21///m2m4))]
        [1==y1+v2*(u1*(A21///m2m4))]
        [1==y1+v2*(u1*m1 * m3)]
        [1==y1+v2*(x1 * m3)]
        [1==x1*(v2*m3) -y1*(-1)]
        [Tp := [x1,-1;y1,v2*m3]][det(Tp) == +1]
            #extra export:
    !! [y1%x1 == 1]
    [v2m3 := (1-y1)///x1]
    [1==x1*v2m3 -y1*(-1)]
    #xxx:[Tp := [x1,-1;y1,v2m3]]
        #原文:[旧变量{bqf11}:=Tp*新变量{_bqf12}]
        #我:[新变量{_bqf12}:=Tp*旧变量{bqf11}]
    [1==x1*v2m3 -1*(-y1)]
    [Tp := [v2m3,+1;-y1,x1]]
    [det(Tp) == +1]
    [_bqf12:=applyTp4bqf_(Tp;bqf11)]
    [Qfb(_A12,_B12,_C12) := _bqf12]
    !! [_A:=eval4bqf_(A,-B,C;n,m)]
    #xxx:[_A12 == eval4bqf_(A11,-B11,C11;v2m3,y1)]
    [_A12 == eval4bqf_(A11,-B11,C11;x1,-y1)]
    [_A12 == eval4bqf_(A11,B11,C11;x1,y1)] #z11
    [1==gcd(A21,_A12)] #预备:对准(_B12,B21)
    ?_k12,k21 :=> [1 == _k12*_A12 + k21*A21]
    !! [_B12%2 == D%2 == B21%2]
    [k_A12:=(_k12*(B21-_B12)///2)]
    [kA21:=(-k21*(B21-_B12)///2)]
    !! [Qfb(A,B+2*k*A,C+k*(B+k*A)) == applyTp4bqf_([1,-k;0,1];Qfb((A,B,C))] # 调整冫二二型中部牜保持等价类
    [B12:=_B12+2*k_A12*_A12]
    [B22:=B21+2*kA21*A21]
    [B12
    ==_B12+2*k_A12*_A12
    ==_B12+2*(_k12*(B21-_B12)///2)*_A12
    ==_B12+(_k12*_A12)*(B21-_B12)
    !! [1 == _k12*_A12 + k21*A21]
    ==_B12+(1-k21*A21)*(B21-_B12)
    ==k21*A21*_B12+(1-k21*A21)*B21
    ==B21 -(k21*A21)*(B21-_B12)
    ==B21 -(k21*(B21-_B12))*A21
    ==B21 +2*(-k21*(B21-_B12)///2)*A21
    ==B21 +2*kA21*A21
    ==B22
    ]
    [B12 == B22]
    [A12:=_A12]
    [A22:=A21]
    !! [1==gcd(A21,_A12)]
    [1==gcd(A12,A22)]

    !! [B12 == B22][D12 == D22]
    [A12*C12 == A22*C22]
    [(A12*C12)%A22 == 0]
    !! [1==gcd(A12,A22)]
    [C12%A22 == 0]
    #至此:完成:对准冫二二型中部
    #至此:完成:二二型乘法牜预备工作
二二型乘法群相关数据:
#幺元公式:D_mod4_eq0:
[[D%4==0] -> [one{<*>;D} == {<Qfb(1,0,-D///4)>}]]
#幺元公式:D_mod4_eq1:
[[D%4==1] -> [one{<*>;D} == {<Qfb(1,1,(1-D)///4)>}]]

#倒数公式:Tn版:
[[D%4<2] -> [{<bqf>} :<- CC{D}] -> [{<bqf>}**-1 == {<applyTn4bqf_([0,1;1,0];bqf)>}]]
    ???Tn???
    等价类内部才要求Tp
    等价类之间大概率不存在T关联
#倒数公式:反转版:
[[D%4<2] -> [{<Qfb(A,B,C)>} :<- CC{D}] -> [{<Qfb(A,B,C)>}**-1 == {<Qfb(C,B,A)>}]]
#倒数公式:负中版:
[[D%4<2] -> [{<Qfb(A,B,C)>} :<- CC{D}] -> [{<Qfb(A,B,C)>}**-1 == {<Qfb(A,-B,C)>}]]
#倒数公式:简型版:
[[D%4<2] -> [{<Qfb(A,B,C)>} :<- CC{D}] -> [{<Qfb(A,B,C)>}**-1 == if [C==A] then {<Qfb(A,B,C)>} elif [B==A] then {<Qfb(A,A,C)>} else {<Qfb(A,-B,C)>}]]
#倒数公式:歧型版:
[[D%4<2] -> [{<Qfb(A,B,C)>} :<- CC{D}] -> [{<Qfb(A,B,C)>}**-1 == if [C==A]or[A==B]or[B==0] then {<Qfb(A,B,C)>} else {<Qfb(A,-B,C)>}]]
[[D%4<2] -> [{<Qfb(A,B,C)>} :<- CC{D}] -> [{<Qfb(A,B,C)>}**-1 == if is_ambiguous_form_(A,B,C) then {<Qfb(A,B,C)>} else {<Qfb(A,-B,C)>}]]

"class_group":
    #OEIS没头没尾地叫"class_group"
    『(<*>) is a well-defined binary operation on CC{D}』
    We thus have that CC{D} is an abelian group under (<*>).
    This is called the class group of primitive binary quadratic forms of discriminant D.

[[
证明冫二二型倒数公式:here
[[is_primitive7Qfb_(Qfb(A,B,C))] -> [Qfb(A,B,C) := bqf] -> [bqf**-1 ~=~ Qfb(C,B,A)]]
<==>
[[is_primitive7Qfb_(Qfb(A,B,C))] -> [(Qfb(A,B,C) <*> Qfb(C,B,A)) ~=~ one{D}]]
<==>
[[is_primitive7Qfb_(Qfb(A,B,C))] -> [(Qfb(A,B,C) <*> Qfb(C,B,A)).reduced_form.A == 1]]
    [[proof:
    [lhs.C%rhs.C == C%C == 0]
    [lhs.B == B == rhs.B[
    !! [is_primitive7Qfb_(Qfb(A,B,C))]
    [lhs,rhs已然 对准，可以 直接作乘法]
    [(lhs<*>rhs).C == lhs.C///rhs.A == C/C == 1]
    [(lhs<*>rhs).C == 1]
    [(lhs<*>rhs).reduced_form.A == 1]
    DONE
    ]]


]]
[[
证明冫二二型歧型平方必为幺元:here
    通过 倒数
!! [[D%4<2] -> [{<Qfb(A,B,C)>} :<- CC{D}] -> [{<Qfb(A,B,C)>}**-1 == {<Qfb(C,B,A)>}]]
[bqf==Qfb(a,b,a)]:
    [bqf**-1 == Qfb(a,b,a) == bqf]
    [bqf**-1 == bqf]
[bqf==Qfb(a,a,c)]:
    [bqf**-1
    == Qfb(c,a,a)
    == Qfb(a,-a,c)
    !! [[A,B,C,k::int] -> [Qfb(A,B,C) ~=~ Qfb(A,B+2*k*A,C+k*(B+k*A))]] # 调整冫二二型中部牜保持等价类
    # [k:=1]
    == Qfb(a,-a+2*a,c+(-a)+a)
    == Qfb(a,a,c)

    == bqf
    ]
    [bqf**-1 == bqf]
[bqf==Qfb(a,0,c)]:
    [bqf**-1
    == Qfb(c,0,a)
    == Qfb(a,-0,c)
    == Qfb(a,0,c)
    == bqf
    ]
    [bqf**-1 == bqf]


]]


Algorithm 5.6.7 (Composition of forms).
    We are given two primitive quadratic forms (a1,b1,c1),(a2,b2,c2) of the same negative discriminant.
    This algorithm computes integers (a3,b3,c3) such that:
        [{<Qfb(a1,b1,c1)>} <*> {<Qfb(a2,b2,c2)>} == {<Qfb(a3,b3,c3)>}]

前提:[D < 0][1==gcd(a1,b1,c1)][1==gcd(a2,b2,c2)]
1.  [Extended Euclid operation]
    g = gcd(a1,a2,(b1+b2)///2);
    Find u,v,w such that:
        [u*a1+ v*a2+ w*(b1+b2)///2 = g]
            #see:gcdext_many
    # [1 == u*(a1///g) +v*(a2///g) +w*((b1+b2)///(2*g))]
2.  [Final assignment]
    [a3 := (a1///g)*(a2///g)]
    [b3 := b2 +2*(a2///g)*((b1-b2)///2 *v -c2*w)]
    #原文bug:[c3 := (b3^2-g)///(4*a3)]
    [c3 := (b3^2-D)///(4*a3)]
    Return (a3,b3,c3)

证明:b3表达式的对称另述:
    [(b2 +2*(a2///g)*((b1-b2)///2 *v -c2*w)) -(b1 +2*(a1///g)*((b2-b1)///2 *u -c1*w))
    == ((b2-b1) -2*a2_g*(b2-b1)///2 *v -2*a2_g*c2*w -2*a1_g*(b2-b1)///2 *u +2*a1_g*c1*w)
    == (b2-b1)*(1 -a2_g*v -a1_g*u) +2*w*(a1_g*c1 -a2_g*c2)
    !! [1 == u*(a1///g) +v*(a2///g) +w*((b1+b2)///(2*g))]
    == (b2-b1)*w*((b1+b2)///(2*g)) +2*w*(a1_g*c1 -a2_g*c2)
    == ((b2-b1)*(b1+b2) +4*g*(a1_g*c1 -a2_g*c2)) ///(2*g) *w
    == ((b2**2-b1**2) +(4*a1*c1 -4*a2*c2)) ///(2*g) *w
    == ((b2**2-4*a2*c2) -(b1**2-4*a1*c1)) ///(2*g) *w
    == (D -D) ///(2*g) *w
    == 0
    ]
    !! [b3 == (b2 +2*(a2///g)*((b1-b2)///2 *v -c2*w))] # b3表达式
    => [b3 == (b1 +2*(a1///g)*((b2-b1)///2 *u -c1*w))] # b3表达式的对称另述

TODO:如何证明算法正确性？感觉跟前面证明存在性时的算法大不同
逆推似乎有:
    猜测:[Qfb(a1,b1,c1) ~=~ Qfb((a1///g),b3,_)]
    猜测:[Qfb(a2,b2,c2) ~=~ Qfb((a2///g),b3,_)]
        感觉不太对

    [k2:=((b1-b2)///2 *v -c2*w)]
    [b3 == (b2 + 2*k2*a2_g)]
    [Qfb(a2_g,b3,_)
    == Qfb(a2_g,(b2 + 2*k2*a2_g),_)
    !! [[A,B,C,k::int] -> [Qfb(A,B,C) ~=~ Qfb(A,B+2*k*A,C+k*(B+k*A))]] # 调整冫二二型中部牜保持等价类
    ~=~ Qfb(a2_g,b2,_)
    ]
    [Qfb(a2_g,b3,_) ~=~ Qfb(a2_g,b2,_)]
    !! 猜测:[Qfb(a2,b2,c2) ~=~ Qfb((a2///g),b3,_)]
    => 猜测:[Qfb(a2,b2,c2) ~=~ Qfb((a2///g),b2,_)]
        g = gcd(a1,a2,(b1+b2)///2)
            ???g可以是a2的任何因子???
        感觉不太对


[A::odd_prime]:
    #最好有:[A%8=!=1]
    !! [[A,B,C,k::int] -> [Qfb(A,B,C) ~=~ Qfb(A,B+2*k*A,C+k*(B+k*A))]] # 调整冫二二型中部牜保持等价类
    => B%(2*A) 等价
    !! [B%2 == D%2]
    !! [A%2 == 1]
    [(B+A)%2 =!= D%2]
    [(B+A)不是合法B{D}]
    [(+/-B+/-A)不是合法B{D}]
    [(-B)是合法B{D}]
        B --> -B 倒数
            # Qfb(A,B,C) --> Qfb(A,-B,_)]
            # Qfb(A,A+B,C) --> Qfb(A,A-B,_)]
    [one == Qfb(A,B,C) <*> Qfb(A,-B,_)]
    [??? == Qfb(A,B,C) <*> Qfb(A,A+B,Cx)]:
        [B**2-4*A*C == D == (A+B)**2-4*A*Cx]
        [-4*A*C == A*(A+2*B)-4*A*Cx]
        [-4*C == (A+2*B)-4*Cx]
    [??? == Qfb(A,B,C) <*> Qfb(A,A-B,Cy)]:

]]


[[
整数分解:平方碰撞:类似 平方筛
[D==(B**2-4*A*C)][gcd(n,y) == 1][n>0][(A*x**2+B*x*y+C*y**2) == n]:
    [4*A*(A*x**2+B*x*y+C*y**2) == 4*A*n]
    [((2*A*x)**2+2*(2*A*x)*B*y+(B*y)**2) == 4*A*n+(B*y)**2-4*A*C*y**2]
    !! [D==(B**2-4*A*C)]
    [(2*A*x+B*y)**2 == 4*A*n+D*y**2]
    [(2*A*x+B*y)**2 =[%(4*n)]= D*y**2]
    #??? [D =[%(4*n)]= (2*A*x/y+B)**2]
    !! [gcd(n,y) == 1]
    [D =[%n]= (2*A*x/y+B)**2]
        # 平方碰撞
    [u:=(2*A*x+B*y)]
    [v:=y]
    [u**2-D*v**2 == 4*A*n]
    [D < 0][Qfb(A,B,C) reuced][u>=0][已知D因子:p2e4D][@[p::prime][n%p==0] -> [p**2 > -D]]:
        # 搜索其他(u,v)
        !! [Qfb(A,B,C) reuced]
        [1 <= A <= sqrt(-D/3)]
        !! [D < 0][A,n>0]
        !! [u**2-D*v**2 == 4*A*n]
        [u**2 == D*v**2 + 4*A*n <= 4*A*n]
        !! [u>=0]
        [0 <= u <= sqrt(4*A*n)]
        [u**2 =[%D]= 4*A*n]
        !! [已知D因子:p2e4D]
        [容易列出:sqrts_mod_(p{D};4*A*n)]
        [sqrt((u**2-4*A*n)///D)%1 == 0]
        [v:=sqrt((u**2-4*A*n)///D)]
        # 每个u%D@A，数量上限:ceil(1+sqrt(4*A*n)/-D)
        # u%D@A的解的数量:大约2**len(p2e4D)，记为:(-D)**err
        # A总数:sqrt(-D/3)
        # u@A总数:ceil(1+sqrt(4*A*n)/-D)*(-D)**err
        # u总数:sum[u@A总数 | [1 <= A <= sqrt(-D/3)]] ~= O((-D)**err * D**/2 + sqrt(4*n)*(-D)**(err-1) * (sqrt(-D/3))**(1+1/2)) == O((-D)**(err+1/2) + sqrt(4*n)*(-D)**(err-1/4))
        # [(-D)**(err+1/2) ~= sqrt(4*n)*(-D)**(err-1/4)] => [(-D)**(3/4) ~= n**(1/2)][(-D) ~= n**(2/3)]
        # u总数@[(-D) ~= n**(2/3)]: ~= O(n**(1/3+err*2/3))

[h**2=[%4*n]=D]:
    [A:=(h**2-D)///(4*n)]
    [D==h**2-4*A*n]
    [B:=h]
    [C:=n]
]]

[[
grep -I -r others/数学 -e 'b000924' -F -l

view others/数学/class_number/class_number.txt
A000003
du -bh 'others/数学/class_number/a000003-Generalized Euler and class numbers(1967)(D. Shanks)[Annotated scanned copy].pdf'
    768K
        ...泛化...无用...
du -bh 'others/数学/class_number/a000924-class number theory(2005)(Steven R. Finch).pdf'
    230K
        基础知识
        但不含 群规模耂计算公式

Group-theoretic properties of H{m} and the efficient computation of h{m} have attracted much attention in recent years.
It turns out that the abelian group of classes of primitive binary quadratic forms of discriminant D is isomorphic to the narrow class group H^+{m}, where the interplay m <-> D was described earlier.
    In particular, Gaussian composition of forms can be elegantly written using ideals and h^+(D) == h^+{m}; see Tables 2 and 3 [10].
    By the same reasoning, we have h(D) == h{m}
    but no interpretation of ˆhˆ(D) in ideal class theory seems to be useful.
    Our convention for treating the discriminant D as an argument and the radicand m as a subscript is perhaps new.

定义:ideal的等价关系:
[R::Ring][I,J::Ideal{R}]
    [[I ~=~ J] =[def]= [?[a,b::R] -> [[a*I == b*J][norm(a*b) > 0]]]]
定义:ideal的等价类:
    {=ideal=}
[eval4bqf_(A,B,C;x,y) == (A*x**2+B*x*y+C*y**2) == ((2*A*x+B*y)**2 -D*y**2)/(4*A)]
定义:ideal的等价类乘法:
    ???平方 好像不能用 ideal表达...
    xxx {=(ideal{1}**2 -D*ideal{1}**2)=} * {=(ideal{1}**2 -D*ideal{1}**2)=}

m <-> D:
    # D:discriminant # B**2-4*A*C
    # m:radicand # sqrt(m)
    #???[m :: squarefree]
    [m%4 =!= 0]
    [D%4 < 2]
    [D == m if m%4 == 1 else 4*m]
    [m == D if D%4 == 1 else D///4]
    [(ZZ+ZZ*((D+sqrt(D))/2)) === (ZZ+ZZ*((1+sqrt(m))/2)) if m%4 == 1 else (ZZ+ZZ*(sqrt(m)/2))]

[m>=2][m::squarefree]:
    m:正整数,无平方因子,非平方{特别是1}
    fundamental_unit{m}:指数级规模

    fundamental unit:
        can be exponentially large in m
    [fundamental_unit{m} == O(exp(m))]
    [unit{m} =[def]= ...[1==abs(norm(this))]]
    [fundamental_unit{m} =[def]= ...[1==abs(norm(this))][@[x::unit{m}] -> ?[e::uint] -> [x == (+/-1)*this**e]]]
    [fundamental_unit{m} == ((a+b*sqrt(m))/k)
        where
            k := 2 if m%4 == 1 else 2
            (a,b) := head [(a,b) | [b:<-[1..]][a:<-[1..]][k**2 == abs(a**2-m*b**2)]]
                # min b
                # !! [m > 0]
                # !! [k**2 == abs(a**2-m*b**2)]
                # => ???min a??? 不太对
    ]
    [fundamental_unit{m} == ((x+y*sqrt(D{m}))/2)
        where
            (x,y) := head [(x,y) | [y:<-[1..]][x:<-[1..]][4 == abs(x**2-D*y**2)]]
                # min y
    ]

    let (A[j]/B[j]) be the j-th convergent of sqrt(m)
        [A[0] == floor_sqrt(m)]
        [B[0] == 1]
        连分数...
    Let L denote the period length of the continued fraction expansion for sqrt(m).
        It can be proved that,
        [[m%8 =!= 5] -> [fundamental_unit{m} == ((A[L-1]+B[L-1]*sqrt(m))/1)]]
            ???难道不是:[m%8 == 1]:[k==2]
        [[m%8 == 5] -> [((A[L-1]+B[L-1]*sqrt(m))/1) <- {fundamental_unit{m}, fundamental_unit{m}**3}]]
            ???难道不是:[m%4 == 1]:[k==2]
]]

[[
整数分解:群规模小因子:类似 减一法
===
@20260727
copy to:
    e others/app/termux/help/gp-example-binary_quadratic_form.txt
copy from:
    view ../../python3_src/seed/math/BinaryQuadraticForm.py
===
Qfb__x__smooth_group_order_method:here

view ../../python3_src/nn_ns/math_nn/numbers/b000003-class_number_of_the_quadratic_order_of_discriminant_(-4n)__fst_20000.txt
view ../../python3_src/nn_ns/math_nn/numbers/b000924-class_number_of_QQ(sqrt(n_th_neg_squarefree))__fst_10000.txt

===
[n%2==0][n>0]:
    [D := [n%4==3]*-n + [n%4==1]*-4*n]
    [B**2-4*A*C == D]
    [-B**2+4*A*C == -D]
    [p::prime][p%2==1][A%p==0]:
        [D%p == (B**2-4*A*C)%p == B**2%p]
        [Jacobi_symbol(p;D)==+1]
        [B%p <- sqrts_mod_(p;D)]
        [B%2 == B**2%2 == (D+4*A*C)%2 == D%2]
        [B%2 == D%2]
    [p::prime][p%2==1][Jacobi_symbol(p;D)==+1][A:=p]:
        [xB6p := sqrts_mod_(p;D)[0]]
        [B := B6p if B6p%2 == D%2 else (p-B6p)]
        [C:=(B**2-D)///(4*A)]
    [n%4==3]:
        [-B**2+4*A*C == -D == n]
        [4*A*C == n+B**2]
        [B%2 == 1]
        [B:=1][A:=1][C:=(1+n)///4] => trivial_factorization#class_group{D}.one
        [B:=3][A:=1][C:=(9+n)///4] => ???
    [n%4==1]:
        [-B**2+4*A*C == -D == 4*n]
        [4*A*C == 4*n+B**2]
        [B%2 == 0]
        [A*C == n+(B///2)**2]
        [B:=0][A:=1][C:=n] => trivial_factorization#class_group{D}.one
        [B:=2][A:=2][C:=(n+1)///2] => trivial_factorization
        [B:=2][A:=1][C:=n+1] => ???

    factor n:
        [qfb :<- class_group{D}][h(D) == (1+2*k)*2**ez][gcd(e,h(D)) == (1+2*k)][g:=(qfb**e)][[g==class_group{D}.1]or[?[j:<-[0..<ez]] -> [is_ambiguous_form_(g**2**j)]]]
<<==:
binary quadratic form
[D<0][D%4 <= 1]:
  [h(D) =[def]= len(class_group{D})]
  [h(D) < sqrt(-D)*ln(-D)]


===
page248[259/604]
5.6.4 Ambiguous forms and factorization
[D<0][D%4 <= 1]:
  [class_group{D}.1 == [D%4==0](1,0,-D/4) + [D%4==1](1,1,(1-D)/4)]
  [is_ambiguous_form_(D;qfb) =[def]= [is_reduced_form_(D;qfb)][qfb**2 == 1]]
    #sqrt4one
        #证明冫二二型歧型平方必为幺元:goto
  [class_group{D}.ambiguous_form <- (a,0,c)|(a,a,c)|(a,b,a)]
#Lemma 5.6.8.Suppose D is a negative discriminant....
    # 注意下面:[u*v==-D///4] | [u*v==-D] 即 整数分解
    # [n%2==1] => [D == -n if n%4==3 else -4*n]
    [[D<0][D%4 <= 1] -> [D%4==0] -> [class_group{D}.ambiguous_form_set == ({(u,0,v) | [[u,v::uint][0 < u <= v][u*v==-D///4][gcd(u,v)==1]]} \-/ {((u+v)///2,v-u,(u+v)///2) | [[u,v::uint][u < v <= 3*u][u*v==-D///4][gcd(u,v)<=2][(u+v)%4 == 2]]} \-/ {(2*u,2*u,(u+v)///2) | [[u,v::uint][0 < 3*u < v][u*v==-D///4][gcd(u,v)<=2][(u+v)%4 == 2]]})]]
        # [(u+v)%4 == 2]
        # [{u,v}%4 == {1}|{3}|{0,2}]
        # [(u*v)%4 == 1|0]
    [[D<0][D%4 <= 1] -> [D%4==1] -> [class_group{D}.ambiguous_form_set == ({((u+v)///4,(v-u)///2,(u+v)///4) | [[u,v::uint][u <= v <= 3*u][u*v==-D][gcd(u,v)==1]]} \-/ {(u,u,(u+v)///4) | [[u,v::uint][0 < 3*u <= v][u*v==-D][gcd(u,v)==1]]})]]
        # [(u+v)%4 == 0]
        # [(u*v)%4 == 3]
        # [{u,v}%4 == {1,3}]



===
TODO:
binary quadratic form
  [D == [n%4==3]*-n + [n%4==1]*-4*n]
  [h(D) < sqrt(-D)*ln(-D)]
  [bqf**odd then **2 to found ambiguous forms maybe yield nontrivial factorizations]
  [[bqf**2 == 1] <-> [bqf is ambiguous form]]



===
? qfbclassno(1-2^67)
5788240250
? default('output,0)
? factorint(5788240250)~
[2,5,13,149,11953;1,3,1,1,1]

===fail:1:
B=1
A=2^5
C=2^60
D=B^2-4*A*C
D==1-2^67
    1
bqf=Qfb(A,B,C)
    Qfb(32,1,1152921504606846976)
bqf==qfbred(bqf)
    1
x=qfbpow(bqf,5788240250/2)
    Qfb(1,1,36893488147419103232)
        #one
x==qfbpow(x,2)
    1

===ok:2:
B=3
AC=(B^2-D)/4
    36893488147419103234
D==B^2-4*AC
    1
factorint(36893488147419103234)~
    [2,274177,67280421310721;1,1,1]
A=274177
C=AC/A
    134560842621442
D==B^2-4*A*C
    1
x=qfbpow(Qfb(A,B,C),5788240250/2)
    Qfb(193707721,193707721,190507991252)
        (u,u,(u+v)///4)
        [u*v==-D]
x==qfbred(x)
    1
qfbpow(x,2)
    Qfb(1,1,36893488147419103232)
        #one




===fail:3:
A=2
C=AC/A
    18446744073709551617
D==B^2-4*A*C
    1
x=qfbpow(Qfb(A,B,C),5788240250/2)
    Qfb(1,1,36893488147419103232)
        #one


===::4
issquare(Mod(2,7))
    1
issquare(Mod(D,7))
    0
issquare(Mod(D,11))
    1
sqrt(Mod(D,11))
    Mod(4,11)
D%11
    5
4^2%11
    5


A=11
B=11-4
    7
AC=(B^2-D)/4
    36893488147419103244
C=AC/A
    3353953467947191204
D==B^2-4*A*C
    1
x=qfbpow(Qfb(A,B,C),5788240250/2)
    Qfb(1,1,36893488147419103232)
        #one

===
D2A_ge_(D,min4A)={
    forprime(A=min4A
    ,
    , if(issquare(Mod(D,A)),return(A),)
    )
}

A=D2A_ge_(D,563889)
    563947
issquare(Mod(D,A))
    1
rt=sqrt(Mod(D,A))
    Mod(253301,563947)
A==rt.mod
    1
B=lift(rt)
    253301
if(B%2,,B=A-B)
if(B%2,,error("000"))
AC=(B^2-D)/4
    36893488163459452382
C=AC/A
    65420133742106
D==B^2-4*A*C
    1
x=qfbpow(Qfb(A,B,C),5788240250/2)
    Qfb(193707721,193707721,190507991252)


===
assert(b, msg="000")={
    if(b,,error(msg))
}
n2D_(n)={
    ;local(D)
    ;assert(n>0)
    ;assert(n%2==1)
    ;D=if(n%4==3,-n,-n*4)
    ;return(D)
}

D2Qfb7A_ge_(D,min4A)={
    ;local(A,rt,B,AC,C,bqf)
    ;A=D2A_ge_(D,min4A)
    ;assert(issquare(Mod(D,A)))
    ;rt=sqrt(Mod(D,A))
    ;B=lift(rt)
    ;\\ bug:if(B%2,,B=A-B)
    ;\\     fixed@20260729
    ;if(B%2==D%2,,B=A-B)
    ;assert(B%2==D%2,"000")
    ;AC=(B^2-D)/4
    ;C=AC/A
    ;assert(D==B^2-4*A*C)
    ;bqf=Qfb(A,B,C)
    ;return(bqf)
}
D2QfbPow7A_ge_(D,exp,min4A)={
    ;local(bqf)
    ;bqf=D2Qfb7A_ge_(D,min4A)
    ;return(qfbpow(bqf,exp))
}

n2QfbPow7A_ge_(n,exp,min4A)={
    ;local(D,bqf)
    ;D=n2D_(n)
    ;bqf=D2Qfb7A_ge_(D,min4A)
    ;return(qfbpow(bqf,exp))
}


D2QfbPow7A_ge_(D,5788240250/2,563889)
    Qfb(193707721,193707721,190507991252)

D2QfbPow7A_ge_(D,5788240250/2,77777)
    Qfb(193707721,193707721,190507991252)

n2QfbPow7A_ge_(-1+2^67,5788240250/2,77777)
    Qfb(193707721,193707721,190507991252)

n2QfbPow7A_ge_(-1+2^67,5788240250/2,88888)
    Qfb(1,1,36893488147419103232)
        #one
n2QfbPow7A_ge_(-1+2^67,5788240250/2,66666)
    Qfb(193707721,193707721,190507991252)
? x=%
    Qfb(193707721,193707721,190507991252)
? component(x,1)
193707721
? component(x,2)
193707721
? component(x,3)
190507991252
? component(x,4)
-147573952589676412927
? x.disc
-147573952589676412927
? x
Qfb(193707721,193707721,190507991252)


===
]]
[[
===
view ../../python3_src/seed/math/factor_pint/DATA4TESTING.py
    M67 == -1+2**67
    [-1+2**67 == 147573952589676412927 == 193707721*761838257287]
    [193707721 == +1+2**3 * 3**3 *5 *67 *2677 == -1+2*13*7450297]
        #7450297:23bit
    [761838257287 == +1+2 *3**2 *29 *67 *2551 *8539 == -1+2**3 *67927 *1401943]
===
]]
[[
===
default('output,0)
search_p_mod8_eq_(r, min4p, max4p, threshold)={
    ;local(pes4Pmm,pes4Ppp)
    ;forprime(p=min4p,max4p
        ,if(p%8==r
        ,pes4Pmm=factorint(p-1)~
            ;pes4Ppp=factorint(p+1)~
            ;if(pes4Pmm[1,][length(pes4Pmm)] >= threshold
                || pes4Ppp[1,][length(pes4Ppp)] >= threshold
            ,printsep(":", p%8, p, pes4Pmm, pes4Ppp)
            ,
            )
        ,
        )
    )
}

search_p_mod8_eq_(1, 999, 2000, 200)
    ... ...
    1:1873:[2,3,13;4,2,1]:[2,937;1,1]
    1:1913:[2,239;3,1]:[2,3,11,29;1,1,1,1]
    ... ...
search_p_mod8_eq_(3, 999, 2000, 200)
    ... ...
    3:1867:[2,3,311;1,1,1]:[2,467;2,1]
    3:1907:[2,953;1,1]:[2,3,53;2,2,1]
    ... ...
search_p_mod8_eq_(5, 999, 2000, 200)
    ... ...
    5:1933:[2,3,7,23;2,1,1,1]:[2,967;1,1]
    5:1949:[2,487;2,1]:[2,3,5,13;1,1,2,1]
    ... ...
search_p_mod8_eq_(7, 999, 2000, 200)
    ... ...
    7:1783:[2,3,11;1,4,1]:[2,223;3,1]
    7:1823:[2,911;1,1]:[2,3,19;5,1,1]
    ... ...

p%8 --> (p+/-1)
    1-1
    3+1
    5-1
    7+1
p%4 --> (p+/-1)
    1-1
    3+1

here:实证:四次方因子=>群规模包含((P+(P%4-2))*P) ~= phi_(sqrt(P**4))
[(1873*1913*1867*1907*1933*1949*1783*1823) == 156217420867353535342512793]
[44448664 == 156217420867353535342512793%82867879]
qfbclassno(-4*(1873*1913*1867*1907*1933*1949*1783*1823))
    5897541212672
factorint(5897541212672)~
    [2,139,82867879;9,1,1]
factor(82867879-1)~
    [2,3,67,68713;1,2,1,1]
factor(82867879+1)~
    [2,5,43,48179;3,1,1,1]
factor(44448664)~
    [2,13,257,1663;3,1,1,1]

qfbclassno(-4*(1873*1913*1867*1907*1933*1949*1783*1823)^2)
    78115054048894138196164608
factorint(78115054048894138196164608)~
    [2,3,7,13,19,23,53,223,239,467,487;22,6,1,1,1,1,1,1,1,1,1]

qfbclassno(-4*(1873*1913*1867*1907*1933*1949*1783*1823)^3)
    921298677702544366879229308104893712896
factorint(921298677702544366879229308104893712896)~
    [2,139,1783,1823,1867,1873,1907,1913,1933,1949,82867879;9,1,1,1,1,1,1,1,1,1,1]

qfbclassno(-4*(1873*1913*1867*1907*1933*1949*1783*1823)^4)
    12202932274432164414908087899925946025585601773830144
factorint(12202932274432164414908087899925946025585601773830144)~
    [2,3,7,13,19,23,53,223,239,467,487,1783,1823,1867,1873,1907,1913,1933,1949;22,6,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]




===
排除:1823
[(1873*1913*1867*1907*1933*1949*1783) == 85692496361685976600391 == 156217420867353535342512793/1823]
qfbclassno(-(1873*1913*1867*1907*1933*1949*1783))
    205661274624
factorint(205661274624)~
    [2,3,13,53,211,307;9,2,1,1,1,1]

qfbclassno(-(1873*1913*1867*1907*1933*1949*1783)^3)
    17623628027456820465262651356777984
factorint(17623628027456820465262651356777984)~
    [2,3,13,53,211,307,1783,1867,1873,1907,1913,1933,1949;9,2,1,1,1,1,1,1,1,1,1,1,1]

qfbclassno(-4*(1873*1913*1867*1907*1933*1949*1783)^2)
    42826235772420031905792
factorint(42826235772420031905792)~
    [2,3,7,13,23,53,223,239,467,487;17,5,1,1,1,1,1,1,1,1]

qfbclassno(-4*(1873*1913*1867*1907*1933*1949*1783)^4)
    3669887053112809403873292980268554948942364672
factorint(3669887053112809403873292980268554948942364672)~
    [2,3,7,13,23,53,223,239,467,487,1783,1867,1873,1907,1913,1933,1949;17,5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

qfbclassno(-4*(1873*1913*1867*1907*1933*1949*1783)^6)
    314481782946667890208412008265834126591295073420168620490695139786752
factorint(314481782946667890208412008265834126591295073420168620490695139786752)~
    [2,3,7,13,23,53,223,239,467,487,1783,1867,1873,1907,1913,1933,1949;17,5,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2]

qfbclassno(-(1873*1913*1867*1907*1933*1949*1783)^5)
    1510212680622550592244980453208216015091541869099674591744
factorint(1510212680622550592244980453208216015091541869099674591744)~
    [2,3,13,53,211,307,1783,1867,1873,1907,1913,1933,1949;9,2,1,1,1,1,2,2,2,2,2,2,2]


===
放大:1867
qfbclassno(-1867)
    5
qfbclassno(-1867^3)
    9335
factorint(9335)~
    [5,1867;1,1]
qfbclassno(-1867^5)
    17428445
factorint(17428445)~
    [5,1867;1,2]

qfbclassno(-4*1867^2)
    934
factorint(934)~
    [2,467;1,1]
        (P+1)
qfbclassno(-4*1867^4)
    1743778
factorint(1743778)~
    [2,467,1867;1,1,1]
        (P+1)*P
qfbclassno(-4*1867^6)
    3255633526
factorint(3255633526)~
    [2,467,1867;1,1,2]
        (P+1)*P^2

qfbclassno(-5*1867)
    98
qfbclassno(-9*1867)
    20
qfbclassno(-13*1867)
    74
qfbclassno(-4*3*1867)
    60
qfbclassno(-4*7*1867)
    60
qfbclassno(-4*11*1867)
    164

qfbclassno(-5^2*1867)
    30
qfbclassno(-9^2*1867)
    60
qfbclassno(-13^2*1867)
    70
qfbclassno(-3^2*1867)
    20
qfbclassno(-7^2*1867)
    30
qfbclassno(-11^2*1867)
    50
qfbclassno(-4*3^2*1867)
    60
qfbclassno(-4*7^2*1867)
    90
qfbclassno(-4*11^2*1867)
    150

qfbclassno(-4*1*1867)
    15
qfbclassno(-4*5*1867)
    98
qfbclassno(-4*9*1867)
    60
qfbclassno(-4*13*1867)
    74


qfbclassno(-4*k41*P43^2)
qfbclassno(-k43*P43^2)
统一:qfbclassno(-4*k*P43^2)
    [P43%4==3]:
        [k%P=!=0]:(P+1) if issquare(Mod(k,P)) else (P-1)
        [0 == 群规模{D:=-4*k*P43^2}%(P43+Jacobi_symbol(P43;k)])


qfbclassno(-4*1*1867^2)
    934
        (P+1)
qfbclassno(-4*5*1867^2)
    3732
        (P-1)
qfbclassno(-4*9*1867^2)
    3736
factorint(3736)~
    [2,467;3,1]
        (P+1)
qfbclassno(-4*13*1867^2)
    3732
factorint(3732)~
    [2,3,311;2,1,1]
        (P-1)
qfbclassno(-4*17*1867^2)
    7464
        (P-1)
qfbclassno(-4*21*1867^2)
    7464
factorint(7464)~
    [2,3,311;3,1,1]
        (P-1)
qfbclassno(-4*25*1867^2)
    3736
        (P+1)
qfbclassno(-4*29*1867^2)
    11196
factorint(11196)~
    [2,3,311;2,2,1]
        (P-1)
qfbclassno(-4*33*1867^2)
    7464
        (P-1)
qfbclassno(-4*37*1867^2)
    3732
        (P-1)
qfbclassno(-4*41*1867^2)
    14928
factorint(14928)~
    [2,3,311;4,1,1]
        (P-1)
qfbclassno(-4*57*1867^2)
    7472
        (P+1)


qfbclassno(-3*1867^2)
    622
factorint(622)~
    [2,311;1,1]
        (P-1)
qfbclassno(-7*1867^2)
    1868
        (P+1)
qfbclassno(-11*1867^2)
    1868
        (P+1)
factorint(1868)~
    [2,467;2,1]
        (P+1)
qfbclassno(-15*1867^2)
    3736
        (P+1)
qfbclassno(-19*1867^2)
    1866
factorint(1866)~
    [2,3,311;1,1,1]
        (P-1)
qfbclassno(-23*1867^2)
    5598
factorint(5598)~
    [2,3,311;1,2,1]
        (P-1)
qfbclassno(-27*1867^2)
    1866
        (P-1)
qfbclassno(-31*1867^2)
    5598
        (P-1)
qfbclassno(-35*1867^2)
    3732
        (P-1)
qfbclassno(-39*1867^2)
    7472
factorint(7472)~
    [2,467;4,1]
        (P+1)
qfbclassno(-43*1867^2)
    1868
        (P+1)
qfbclassno(-47*1867^2)
    9330
factorint(9330)~
    [2,3,5,311;1,1,1,1]
        (P-1)
qfbclassno(-4*47*1867^2)
    9330
        (P-1)
qfbclassno(-4*43*1867^2)
    5604
factorint(5604)~
    [2,3,467;2,1,1]
        (P+1)

list_issquare_modP_(p,min4u,max4u)=forstep(u=min4u,max4u,4,printsep(":",issquare(Mod(u,p)),u))

list_issquare_modP_(1867,1,57)
    1:1
    0:5
    1:9
    0:13
    0:17
    0:21
    1:25
    0:29
    0:33
    0:37
    0:41
    0:45
    1:49
    0:53
    1:57

list_issquare_modP_(1867,3,59)
    0:3
    1:7
    1:11
    1:15
    0:19
    0:23
    0:27
    0:31
    0:35
    1:39
    1:43
    0:47
    1:51
    0:55
    1:59

===
Jacobi_symbol(M,a)={
    ;if(gcd(M,a) > 1,0
    ,if(issquare(Mod(a,M)),+1,-1)
    )
}
both_7D_eq_neg4kPP_(p,k)=[4*qfbclassno(-4*k*p^2), (p+(p%4-2)*Jacobi_symbol(p,k))]
check_7D_eq_neg4kPP_(p,k)=(((4*qfbclassno(-4*k*p^2))%(p+(p%4-2)*Jacobi_symbol(p,k))) == 0)
checks_7D_eq_neg4kPP_(p,min4k,max4k)=for(k=min4k,max4k,if(0==check_7D_eq_neg4kPP_(p,k),printsep(":",p,k)))

here:实证:[0 == ((4*qfbclassno(-4*k*p^2))%(p+(p%4-2)*Jacobi_symbol(p,k)))]

[(1873*1913*1867*1907*1933*1949*1783*1823) == 156217420867353535342512793]
checks_7D_eq_neg4kPP_(1867,1,2000)
    all ok!
checks_7D_eq_neg4kPP_(1949,1,2000)
    all ok!
foreach([1873,1913,1867,1907,1933,1949,1783,1823],p,checks_7D_eq_neg4kPP_(p,1,2000))
    all ok!

===
===
default('output,0)
factorint(-1+2^67)~
    [193707721,761838257287;1,1]

qfbclassno(-4*761838257287)
    493511
qfbclassno(-761838257287)
    493511
factorint(493511)~
    [23,43,499;1,1,1]

qfbclassno(-4*193707721)
    6636
factorint(6636)~
    [2,3,7,79;2,1,1,1]

qfbclassno(-3*193707721)
    6756
factorint(6756)~
    [2,3,563;2,1,1]

qfbclassno((1-2^67)*5)
    11433868900
factorint(11433868900)~
    [2,5,114338689;2,2,1]

qfbclassno((1-2^67)*13)
    8115272784
factorint(8115272784)~
    [2,3,1993,28277;4,2,1,1]

qfbclassno((1-2^67)*17)
    73374108492
factorint(73374108492)~
    [2,3,11261,542981;2,1,1,1]

qfbclassno((1-2^67)*31*4)
    30670287312
factorint(30670287312)~
    [2,3,7,19,307,15649;4,1,1,1,1,1]

qfbclassno((1-2^67)*127*4)
    58741710096
factorint(58741710096)~
    [2,3,4549,269023;4,1,1,1]

qfbclassno((1-2^67)*129)
    82090587248
factorint(82090587248)~
    [2,1543,3325121;4,1,1]

qfbclassno((1-2^67)*41)
    65003407472
factorint(65003407472)~
    [2,31,83,1578979;4,1,1,1]

qfbclassno((1-2^67)*37)
    13030066528
factorint(13030066528)~
    [2,61,347,19237;5,1,1,1]

qfbclassno((1-2^67)*67*4)
    44696455688
factorint(44696455688)~
    [2,5587056961;3,1]

qfbclassno((1-2^67)*61)
    16286254736
factorint(16286254736)~
    [2,23,31,1427617;4,1,1,1]

qfbclassno((1-2^67)*53)
    37579788180
factorint(37579788180)~
    [2,3,5,11,18979691;2,2,1,1,1]

qfbclassno((1-2^67)*153)
    146748216984
factorint(146748216984)~
    [2,3,11261,542981;3,1,1,1]

qfbclassno((1-2^67)*157)
    42706924196
factorint(42706924196)~
    [2,31,103,109,30677;2,1,1,1,1]

qfbclassno((1-2^67)*173)
    69739403080
factorint(69739403080)~
    [2,5,23,227,14519;3,1,2,1,1]

qfbclassno((1-2^67)*181)
    29913283224
factorint(29913283224)~
    [2,3,11,4513,8369;3,2,1,1,1]
#乘四
qfbclassno((1-2^67)*181*4)
    89739849672
factorint(89739849672)~
    [2,3,11,4513,8369;3,3,1,1,1]
[89739849672 == 3 *29913283224]
qfbclassno((1-2^67)*181*2^4)
    179479699344
factorint(179479699344)~
    [2,3,11,4513,8369;4,3,1,1,1]
qfbclassno((1-2^67)*181*2^6)
    358959398688
[179479699344 == 2 *89739849672 == 2*3 *29913283224]
[358959398688 == 2 *179479699344]
#乘二
qfbclassno((1-2^67)*181*2^3)
    293748880912
factorint(293748880912)~
    [2,17,31,34837391;4,1,1,1]
qfbclassno((1-2^67)*181*2^5)
    587497761824
factorint(587497761824)~
    [2,17,31,34837391;5,1,1,1]
[587497761824 == 2 *293748880912]
=>乘四影响不大，乘二影响很大


qfbclassno((1-2^67)*4*35)
    61536569536
factorint(61536569536)~
    [2,13,17,37,59,1993;6,1,1,1,1,1]

qfbclassno((1-2^67)^3)
    854193492231156747779681711750
qfbclassno(-4*(1-2^67)^4)
    10889035685270582506687461136192300827360
qfbclassno(-4*(1-2^67)^2)
    73786975914015931680
qfbclassno(1-2^67)
    5788240250
factorint(5788240250)~
    M67**1
    [2,5,13,149,11953;1,3,1,1,1]
factorint(73786975914015931680)~
    [2,3,5,67,2677,67927,1401943;5,3,1,1,1,1,1]
    M67**2
    奇怪:不同:
        (-1+193707721)
        (+1+761838257287)
        [193707721%8 == 1]
        [761838257287%8 == 7]
factorint(10889035685270582506687461136192300827360)~
    M67**4
    [2,3,5,67,2677,67927,1401943,193707721,761838257287;5,3,1,1,1,1,1,1,1]
        (-1+193707721)*193707721
        (+1+761838257287)*761838257287
factorint(854193492231156747779681711750)~
    M67**3
    [2,5,13,149,11953,193707721,761838257287;1,3,1,1,1,1,1]


==>>:
#数据实验冫群规模规律:here
群规模:平方因子部分 大约:注入 phi_(sqrt((P**2)**e)), 但是 可能是(P-1)也可能是(P+1)
    见上面:M67**2
    见上面:M67**3
    见上面:M67**4
    见上面:实证:...
群规模:难点在于squarefree部分，平方因子部分的影响十分浅显
    见上面:乘四影响不大，乘二影响很大
群规模变化无常，与因子的群规模无明显关联，难以控制，好处是 比 椭圆曲线法 更有希望
    {bug:但:平方因子影响群规模，但似乎并不影响群规模耂最大素因子}
        !! {只因k远小于n => 群规模{-4*k**2*n}确实不太影响 最大素因子}
    从数据上看，放大n后，通常 最大素因子也变大，变得更糟
    有例外:变得更好
        [n:=M67*181][群规模==29913283224][群规模.最大素因子==8369<11953]
        #发现更佳:放大系数:=23,35:
        #   见下面:nk2Qfb_group_order_ex_().输出
        [n:=M67*23][群规模==70390053120][群规模.最大素因子==2339<11953]
        [n:=M67*35][群规模==61536569536][群规模.最大素因子==1993<11953]

        #追加:
        #   见下面:nIIps2Qfb_group_order_ex_():
        [n:=M67*II(PRIMES[1:1+4])][群规模==238544566272][群规模.最大素因子==2969<11953]
        [n:=M67*II(PRIMES[1:1+6])][群规模==3813672763648][群规模.最大素因子==2437<11953]
#   #view ../../python3_src/seed/math/factor_pint/factor_pint__smooth_group_order_method__7py_adhoc_call.py
#       #发现冫平方因子使得群规模包含素幂的环乘阶:goto
#       #发现冫四次因子使得群规模直接包含该素因子:goto

===
/;.*[2-9].*[2-9]
    发现 群规模.素因子.指数 很小，超过1的都是[2,3,5]
        <<==见下面:nk2Qfb_group_order_ex_().输出

===
n2Qfb_group_order_ex_(n)={
    ;local(D,sz,max_p4sz,p2e4sz)
    ;D=n2D_(n)
    ;sz=qfbclassno(D)
    ;p2e4sz=factorint(sz)~
    ;max_p4sz=p2e4sz[1,length(p2e4sz)]
    ;return([n,D,sz,max_p4sz,p2e4sz])
}
nk2Qfb_group_order_ex_(n,min_k,max_k)={
    ;for(k=min_k,max_k
    ,if(k%2==1,print([n,k,n2Qfb_group_order_ex_(n*k)]))
    )
}

n2Qfb_group_order_ex_(-1+2^34)
    [17179869183,-17179869183,63424,991,[2,991;6,1]]

===
nk2Qfb_group_order_ex_(37*67,1,19)
    [2479, 1, [2479, -2479, 24, 3, [2, 3; 3, 1]]]
    [2479, 3, [7437, -29748, 64, 2, [2; 6]]]
    [2479, 5, [12395, -12395, 36, 3, [2, 3; 2, 2]]]
    [2479, 7, [17353, -69412, 48, 3, [2, 3; 4, 1]]]
    [2479, 9, [22311, -22311, 96, 3, [2, 3; 5, 1]]]
    [2479, 11, [27269, -109076, 176, 11, [2, 11; 4, 1]]]
    [2479, 13, [32227, -32227, 28, 7, [2, 7; 2, 1]]]
    [2479, 15, [37185, -148740, 96, 3, [2, 3; 5, 1]]]
    [2479, 17, [42143, -42143, 224, 7, [2, 7; 5, 1]]]
    [2479, 19, [47101, -188404, 168, 7, [2, 3, 7; 3, 1, 1]]]

===
nk2Qfb_group_order_ex_(377*677,1,19)
    [255229, 1, [255229, -1020916, 368, 23, [2, 23; 4, 1]]]
    [255229, 3, [765687, -765687, 624, 13, [2, 3, 13; 4, 1, 1]]]
    [255229, 5, [1276145, -5104580, 1536, 3, [2, 3; 9, 1]]]
    [255229, 7, [1786603, -1786603, 168, 7, [2, 3, 7; 3, 1, 1]]]
    [255229, 9, [2297061, -9188244, 1472, 23, [2, 23; 6, 1]]]
    [255229, 11, [2807519, -2807519, 1416, 59, [2, 3, 59; 3, 1, 1]]]
    [255229, 13, [3317977, -13271908, 672, 7, [2, 3, 7; 5, 1, 1]]]
    [255229, 15, [3828435, -3828435, 352, 11, [2, 11; 5, 1]]]
    [255229, 17, [4338893, -17355572, 1568, 7, [2, 7; 5, 2]]]
    [255229, 19, [4849351, -4849351, 1496, 17, [2, 11, 17; 3, 1, 1]]]

===
nk2Qfb_group_order_ex_(-1+2^67,1,19)
    [147573952589676412927, 1, [147573952589676412927, -147573952589676412927, 5788240250, 11953, [2, 5, 13, 149, 11953; 1, 3, 1, 1, 1]]]
    [147573952589676412927, 3, [442721857769029238781, -1770887431076116955124, 20793981816, 288805303, [2, 3, 288805303; 3, 2, 1]]]
    [147573952589676412927, 5, [737869762948382064635, -737869762948382064635, 11433868900, 114338689, [2, 5, 114338689; 2, 2, 1]]]
    [147573952589676412927, 7, [1033017668127734890489, -4132070672510939561956, 19888037984, 621501187, [2, 621501187; 5, 1]]]
    [147573952589676412927, 9, [1328165573307087716343, -1328165573307087716343, 23152961000, 11953, [2, 5, 13, 149, 11953; 3, 3, 1, 1, 1]]]
    [147573952589676412927, 11, [1623313478486440542197, -6493253913945762168788, 34471571120, 61556377, [2, 5, 7, 61556377; 4, 1, 1, 1]]]
    [147573952589676412927, 13, [1918461383665793368051, -1918461383665793368051, 8115272784, 28277, [2, 3, 1993, 28277; 4, 2, 1, 1]]]
    [147573952589676412927, 15, [2213609288845146193905, -8854437155380584775620, 23585286480, 100999, [2, 3, 5, 7, 139, 100999; 4, 1, 1, 1, 1, 1]]]
    [147573952589676412927, 17, [2508757194024499019759, -2508757194024499019759, 73374108492, 542981, [2, 3, 11261, 542981; 2, 1, 1, 1]]]
    [147573952589676412927, 19, [2803905099203851845613, -11215620396815407382452, 19882179216, 46023563, [2, 3, 46023563; 4, 3, 1]]]

===
nk2Qfb_group_order_ex_(-1+2^67,21,49)
    [147573952589676412927, 21, [3099053004383204671467, -3099053004383204671467, 7851919424, 106591, [2, 1151, 106591; 6, 1, 1]]]
    [147573952589676412927, 23, [3394200909562557497321, -13576803638250229989284, 70390053120, 2339, [2, 3, 5, 17, 461, 2339; 8, 1, 1, 1, 1, 1]]]
    [147573952589676412927, 25, [3689348814741910323175, -3689348814741910323175, 34729441500, 11953, [2, 3, 5, 13, 149, 11953; 2, 1, 3, 1, 1, 1]]]
    [147573952589676412927, 27, [3984496719921263149029, -15937986879685052596116, 62381945448, 288805303, [2, 3, 288805303; 3, 3, 1]]]
    [147573952589676412927, 29, [4279644625100615974883, -4279644625100615974883, 12589883724, 183067, [2, 3, 11, 521, 183067; 2, 1, 1, 1, 1]]]
    [147573952589676412927, 31, [4574792530279968800737, -18299170121119875202948, 30670287312, 15649, [2, 3, 7, 19, 307, 15649; 4, 1, 1, 1, 1, 1]]]
    [147573952589676412927, 33, [4869940435459321626591, -4869940435459321626591, 55452159816, 14831, [2, 3, 43, 3623, 14831; 3, 1, 1, 1, 1]]]
    [147573952589676412927, 35, [5165088340638674452445, -20660353362554697809780, 61536569536, 1993, [2, 13, 17, 37, 59, 1993; 6, 1, 1, 1, 1, 1]]]
    [147573952589676412927, 37, [5460236245818027278299, -5460236245818027278299, 13030066528, 19237, [2, 61, 347, 19237; 5, 1, 1, 1]]]
    [147573952589676412927, 39, [5755384150997380104153, -23021536603989520416612, 36496512448, 106451, [2, 11, 487, 106451; 6, 1, 1, 1]]]
    [147573952589676412927, 41, [6050532056176732930007, -6050532056176732930007, 65003407472, 1578979, [2, 31, 83, 1578979; 4, 1, 1, 1]]]
    [147573952589676412927, 43, [6345679961356085755861, -25382719845424343023444, 43849979184, 83049203, [2, 3, 11, 83049203; 4, 1, 1, 1]]]
    [147573952589676412927, 45, [6640827866535438581715, -6640827866535438581715, 22867737800, 114338689, [2, 5, 114338689; 3, 2, 1]]]
    [147573952589676412927, 47, [6935975771714791407569, -27743903086859165630276, 138558466176, 957107, [2, 3, 13, 29, 957107; 7, 1, 1, 1, 1]]]
    [147573952589676412927, 49, [7231123676894144233423, -7231123676894144233423, 46305922000, 11953, [2, 5, 13, 149, 11953; 4, 3, 1, 1, 1]]]

===
# !! [平方因子基本不影响 群规模耂最大素因子]
# => 最好有:[is_squarefree_(k)]
view ../../python3_src/seed/math/iter_unsorted_squarefree_uints.py
    from seed.math.iter_unsorted_squarefree_uints import iter_unsorted_squarefree_uints_

更多因子如何？群规模 有增有减，看不出趋势

nIIps2Qfb_group_order_ex_(n,min_p,num_ps)={
    ;local(ls,j,m=n)
    ;ls=vector(num_ps)
    ;j=1
    ;if(j>num_ps,return())
    ;forprime(p=max(3,min_p)
    ,
    ,m*=p
    ;ls[j]=p
    ;print([n,j,vecextract(ls,Str("1..", j)),n2Qfb_group_order_ex_(m)])
    ;j+=1
    ;if(j>num_ps,break())
    )
}

nIIps2Qfb_group_order_ex_(35,3,2)

nIIps2Qfb_group_order_ex_((-1+2^67),3,10)
    [147573952589676412927, 1, [3], [442721857769029238781, -1770887431076116955124, 20793981816, 288805303, [2, 3, 288805303; 3, 2, 1]]]
    [147573952589676412927, 2, [3, 5], [2213609288845146193905, -8854437155380584775620, 23585286480, 100999, [2, 3, 5, 7, 139, 100999; 4, 1, 1, 1, 1, 1]]]
    [147573952589676412927, 3, [3, 5, 7], [15495265021916023357335, -15495265021916023357335, 84492713568, 732833, [2, 3, 1201, 732833; 5, 1, 1, 1]]]
    [147573952589676412927, 4, [3, 5, 7, 11], [170447915241076256930685, -681791660964305027722740, 238544566272, 2969, [2, 3, 1453, 2969; 11, 3, 1, 1]]]
    [147573952589676412927, 5, [3, 5, 7, 11, 13], [2215822898133991340098905, -8863291592535965360395620, 993314685824, 3384331, [2, 2293, 3384331; 7, 1, 1]]]
    [147573952589676412927, 6, [3, 5, 7, 11, 13, 17], [37668989268277852781681385, -150675957073111411126725540, 3813672763648, 2437, [2, 11, 263, 2113, 2437; 8, 1, 1, 1, 1]]]
    [147573952589676412927, 7, [3, 5, 7, 11, 13, 17, 19], [715710796097279202851946315, -715710796097279202851946315, 6278911412736, 4087832951, [2, 3, 4087832951; 9, 1, 1]]]
    [147573952589676412927, 8, [3, 5, 7, 11, 13, 17, 19, 23], [16461348310237421665594765245, -65845393240949686662379060980, 76752826226688, 12492321977, [2, 3, 12492321977; 11, 1, 1]]]
    [147573952589676412927, 9, [3, 5, 7, 11, 13, 17, 19, 23, 29], [477379100996885228302248192105, -1909516403987540913208992768420, 462588898222080, 179264671, [2, 3, 5, 7, 179264671; 13, 2, 1, 1, 1]]]
    ^C # ...31?太久

===
]]

#]]]'''#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.power.power_ import power_, std_exp_
    #def power_(mul_, may_inv_, may_eq_zero_, eq_one_, one, imay_group_order, e, x0, /):
    from seed.math.gcd import noncoprime_part_of_to_, coprime_part_of_to_
    from seed.math.gcd import gcdext, gcdext_many # -> (gcd, [(coeff4int, int///gcd)])
    from seed.math.gcd import are_coprime, gcd, gcd_many
    #from seed.math.are_pairwise_coprime import are_pairwise_coprime, check_pairwise_coprime
    from seed.helper.repr_input import repr_helper, repr_helper__str
    from seed.types.CachedProperty import CachedProperty, mk_cached_propertyT_
    from seed.for_libs.for_collections.namedtuple__nontuple4cached_property import mk_named_pseudo_tuple_
    #def mk_named_pseudo_tuple_(__module__,typename, field_names, /):
    #    def _check6make_(sf, /):
    from seed.for_libs.for_collections.override_repr4namedtuple import mk_namedtuple_, mk_namedtuple__check6make_
    #def mk_namedtuple_(__module__, nm, nms_or_str, /, *args, **kwds):
    #def mk_namedtuple__check6make_(__module__, nm, nms_or_str, /, *args, **kwds):
    #    def _check6make_(sf, /):
    from seed.tiny_.check import check_type_is, check_int_ge
    from seed.math.prime_sieve.primes_ge_lt import list_primes__ge_lt_, iter_primes__ge_lt_, iter_filter4primes_ge_lt_
    from seed.math.Jacobi_symbol import Jacobi_symbol
    from seed.math.sqrts_mod_ import iter_sqrts_mod_prime_
    from seed.math.floor_ceil_tools.fc_perfect import perfect_div
    from seed.math.max_power_of_base_as_factor_of_ import factor_pint_out_power_of_base_

#.#################################
___end_mark_of_excluded_global_names__0___ = ...
__all__

_bypass_ = True

def C5DAB_(D, A, B, /):
    if not D&1 == B&1:raise ValueError
    _4AC = B**2 -D
    if not _4AC&3 == 0:raise ValueError
    AC = _4AC >> 2
    C = perfect_div(AC, A)
    return C
def D5ABC_(A, B, C, /):
    return (B**2-4*A*C)
def is_primitive7Qfb_(A, B, C, /):
    #xxx:return are_coprime(A, B, ...) only 2 input
    return 1 == gcd_many([A,B,C]) #not:are_pairwise_coprime
def is_ambiguous_form_7Qfb7negD7reduced_(A, B, C, /):
    'is_reduced7Qfb7negD_(A,B,C) => A->B->C->bool'
    r'''[[[

    [is_ambiguous_form_(D;qfb) =[def]= [is_reduced_form_(D;qfb)][qfb**2 == 1]]
        #sqrt4one
        #证明冫二二型歧型平方必为幺元:goto
    [class_group{D}.ambiguous_form <- (a,0,c)|(a,a,c)|(a,b,a)]
    #]]]'''#'''
    #return B == 0 or B == A or A == C
    return C == A or A == B or B == 0
def is_reduced7Qfb7negD_(A, B, C, /):
    '# [[D < 0] -> [reduced_form <- distinguished_form]]'
    return (C > A >= B > -A) or (C == A >= B >= 0)
def reduce4Qfb7negD_(A, B, C, /):
    assert A > 0
    assert C > 0
    r'''[[[
[A,B,C::int][A,C>0][B^2-4*A*C == D < 0]:
    # !! 调整冫二二型中部牜保持等价类:[Qfb(A,B+2*k*A,C+k*(B+k*A)) == applyTp4bqf_([1,-k;0,1];Qfb((A,B,C))]
    # !! 调换冫二二型头尾部牜保持等价类:[Qfb(C, -B, A) == applyTp4bqf_([0,1;-1,0];Qfb((A,B,C))]
    [_reduce4Qfb7negD__7Type1_(bqf@Qfb(A,B,C)) := (if [A<=C] then bqf else Qfb(C,-B,A))]
    [_reduce4Qfb7negD__7Type2_(bqf@Qfb(A,B,C)) := (if [−A < B <= A] then bqf else let [k:=(B+(A-1))//(2*A)] in Qfb(A,B-2*k*A,C-k*(B-k*A)))]
    [_reduce4Qfb7negD__7FinalAdjustment(bqf@Qfb(A,B,C)) := (if [A==C][B < 0] then Qfb(C,-B,A) else bqf)]
    [reduce4Qfb7negD_(bqf@Qfb(A,B,C)) := if [−A < B <= A <= C] then _reduce4Qfb7negD__7FinalAdjustment(bqf) else reduce4Qfb7negD_(_reduce4Qfb7negD__7Type2_(_reduce4Qfb7negD__7Type1_(bqf)))]
    #]]]'''#'''
    while 1: #not (C >= A >= B > -A):
        if not C >= A:
            # [C < A]
            # !! [Qfb(C, -B, A) == applyTp4bqf_([0,1;-1,0];Qfb((A,B,C))]
            (A, B, C) = (C, -B, A)
            # [C > A]
        # [C >= A]
        if A >= B > -A:
            # [C >= A >= B > -A]
            break
        # !! [Qfb(A,B+2*k*A,C+k*(B+k*A)) == applyTp4bqf_([1,-k;0,1];Qfb((A,B,C))]
        k = (B+(A-1))//(2*A)
        (B, C) = (B-2*k*A, C-k*(B-k*A))
        # [C <?> A >= B > -A]
        assert A >= B > -A
    # [C >= A >= B > -A]
    if C == A and B < 0:
        # [C == A >= B > -A]
        # !! [Qfb(C, -B, A) == applyTp4bqf_([0,1;-1,0];Qfb((A,B,C))]
        (A, B, C) = (C, -B, A)
        # [C == A >= B >= 0]
    else:
        # [C > A >= B > -A]
        pass
    # [[C == A >= B >= 0] + [C > A >= B > -A]]
    return (A, B, C)

_Qfb = mk_named_pseudo_tuple_(__name__, '_Qfb', 'A B C')
#class Qfb
class BinaryQuadraticForm(_Qfb):
    'invariants:[D<0][A>0][gcd(A,B,C)==1]' # => [C>0]
    def _check6make_(sf, /):
        (A, B, C) = sf
        check_type_is(int, B)
        check_int_ge(1, A)
        check_int_ge(1, C)

        D = sf.D
        check_discriminant7Qfb_(D)
        if 0:
            # !! [[D < 0] -> [reduced_form <- distinguished_form]]
            if not D < 0:raise TypeError

            # !! [(B**2-4*A*C)%4 < 2]
            if not D&3 < 2:raise TypeError

        #if not sf.whether_primitive:raise TypeError
        if not is_primitive7Qfb_(A,B,C):raise TypeError
    @CachedProperty
    def D(sf, /):
        '-> discriminant/int{==(B**2-4*A*C)}'
        return D5ABC_(*sf)
    #@CachedProperty
    @property
    def whether_primitive(sf, /):
        return True
        return is_primitive7Qfb_(*sf)
    @CachedProperty
    def whether_reduced(sf, /):
        return is_reduced7Qfb7negD_(*sf)
    @CachedProperty
    def reduced_form(sf, /):
        if sf.whether_reduced:
            return sf
        return __class__(*reduce4Qfb7negD_(*sf))
    #@CachedProperty
    @property
    def whether_ambiguous(sf, /):
        if not sf.whether_reduced:raise TypeError('not reduced_form')
        return is_ambiguous_form_7Qfb7negD7reduced_(*sf)

#end-class BinaryQuadraticForm:

class EqvCls4BinaryQuadraticForm:
    'invariants:[D<0][A>0][gcd(A,B,C)==1]' # => [C>0]
    def __new__(cls, bqf, /):
        check_type_is(BinaryQuadraticForm, bqf)
        'invariants:[D<0][A>0][gcd(A,B,C)==1]' # => [C>0]
        sf = super(__class__, cls).__new__(cls)
        sf._bqf = bqf
        return sf
    def __reduce__(sf, /):
        if 0:
            #bug: !! (mkr, args, __dict__)
            (mkr, args, kwds) = sf._4repr_ver1()
            return (mkr, args, kwds)
        (mkr, args) = sf._4repr_ver2()
        return (mkr, args)
    if 0:
        def __getnewargs__(sf, /):
            bqf = sf.binary_quadratic_form7repr
            args = (bqf,)
            return args
        def __getstate__(sf, /):
            return None
    def __repr__(sf, /):
        if 0:
            return repr_helper(sf, sf.binary_quadratic_form7repr)
        if 0:
            (mkr, args, kwds) = sf._4repr_ver1()
            nm = mkr.__name__
            return repr_helper__str(nm, *args, **kwds)
        (mkr, args) = sf._4repr_ver2()
        nm = mkr.__name__
        return repr_helper__str(nm, *args)
    def _4repr_ver2(sf, /):
        (mkr, args, kwds) = sf._4repr_ver1()
        if kwds:
            mkr = mk4Qfb_class_group5ABC7repr_
        return (mkr, args)
    def _4repr_ver1(sf, /):
        bqf = sf.binary_quadratic_form7repr
        to_reduce = False
        if default4kw7to_reduce and not bqf.whether_reduced:
            # [default4kw7to_reduce is True][bqf not reduced]
            kwds = dict(to_reduce=to_reduce)
        else:
            # [default4kw7to_reduce is False] or [bqf reduced]
            # [[default4kw7to_reduce is True] -> [bqf reduced]]
            kwds = {}
        kwds
        args = tuple(bqf)
        mkr = mk4Qfb_class_group5ABC_
        return (mkr, args, kwds)
    @property
    def binary_quadratic_form7repr(sf, /):
        return sf._bqf
    @property
    def binary_quadratic_form7reduced(sf, /):
        return sf._bqf.reduced_form
    @property
    def D(sf, /):
        return sf._bqf.D
    @property
    def whether_ambiguous(sf, /):
        return sf.binary_quadratic_form7reduced.whether_ambiguous
    def __hash__(sf, /):
        return hash((__class__, sf.binary_quadratic_form7reduced))
    def __eq__(sf, ot, /):
        if sf is ot:
            return True
        if not isinstance(ot, __class__):
            return NotImplemented
        return sf.binary_quadratic_form7reduced == ot.binary_quadratic_form7reduced

    def is_ambiguous_form_(sf, /):
        return sf.whether_ambiguous
    def eq_one_(sf, /):
        return sf.binary_quadratic_form7reduced.A == 1
    def mk_one6Qfb_class_group_(sf, /):
        if _bypass_:
            if sf.eq_one_():return sf
        return mk_one6Qfb_class_group5D_(sf.D)
    def mk_inv6Qfb_class_group_(sf, /):
        if _bypass_:
            if sf.is_ambiguous_form_():return sf
        (A, B, C) = sf.binary_quadratic_form7reduced
        #return mk4Qfb_class_group5ABC_(C, B, A, D=sf.D, to_reduce=True)
        return mk4Qfb_class_group5ABC_(A, -B, C, D=sf.D, to_reduce=True)
    @property
    def one(sf, /):
        return sf.mk_one6Qfb_class_group_()
    @property
    def inv(sf, /):
        return sf.mk_inv6Qfb_class_group_()
    def __truediv__(sf, ot, /):
        if not isinstance(ot, __class__):
            return NotImplemented
        if _bypass_:
            if sf == ot: return sf.one
        # sf/ot
        return sf * ot.inv
    def __rtruediv__(sf, ot, /):
        # ot/sf
        if ot in [1]:
            # 1/sf
            return sf.inv
        if not isinstance(ot, __class__):
            return NotImplemented
        if _bypass_:
            if sf == ot: return sf.one
        # ot/sf
        return sf.inv * ot
    def __pow__(sf, exp, /):
        check_type_is(int, exp)
        if sf.eq_one_():
            return sf
        if exp == 0:
            return sf.one
        if exp < 0:
            exp = -exp
            sf = sf.inv
        assert exp > 0
        if exp == 1:
            return sf
        # [exp >= 2]
        if _bypass_:
            if sf.is_ambiguous_form_():
                match exp&1:
                    case 0:
                        return sf.one
                    case 1:
                        return sf
                raise 000
        assert exp >= 2
        # [exp >= 2]
        return power_(mul_:=type(sf).__mul__, may_inv_:=None, may_eq_zero_:=None, eq_one_:=lambda ot:ot==sf.one, sf.one, imay_group_order:=-1, exp, sf)
    def __mul__(sf, ot, /):
        if not isinstance(ot, __class__):
            return NotImplemented
        if _bypass_:
            if ot.eq_one_(): return sf
            if sf.eq_one_(): return ot
            if sf.inv == ot: return sf.one
        D1 = sf.D
        D2 = ot.D
        if not D1 == D2:raise ValueError((sf.D, ot.D), (sf, ot))
        D = D1

        bqf11 = sf.binary_quadratic_form7reduced
        bqf21 = ot.binary_quadratic_form7reduced
        'invariants:[D<0][A>0][gcd(A,B,C)==1]' # => [C>0]
        #if not bqf11.whether_primitive.
        (A11, B11, C11) = bqf11
        (A21, B21, C21) = bqf21
        assert B11&1 == D&1 == B21&1
        (g, [(u, A11_g), (v, A21_g), (w, _)]) = gcdext_many([A11, A21, (B11+B21)>>1])
        A3 = A11_g*A21_g
        B3 = B21 +2*A21_g*(((B11-B21)>>1)*v -C21*w)
        C3 = C5DAB_(D, A3, B3)
            #bug: (B3^2-D)//(4*A3)
            #   --> (B3**2-D)//(4*A3)
        out = mk4Qfb_class_group5ABC_(A3, B3, C3, D=D, to_reduce=True)
        return out
        r'''[[[
        [class_group{D}.ambiguous_form <- (a,0,c)|(a,a,c)|(a,b,a)]
        证明冫二二型歧型平方必为幺元:goto
        [sf == ot == Qfb(a,0,c)]:
            [D==-4*a*c]
            [g == a]
            [A11_g == A21_g == 1]
            [A3 == 1]
            [u == 0][v == 1][w == 0]
            [B3 == 0]
            [C3 == a*c == -D///4]
            -> Qfb(1,0,-D///4) == one
        [sf == ot == Qfb(a,a,c)]:
            [D==a**2-4*a*c == (a-2*c)**2 -4*c**2 == a*(a-4*c)]
            [D%2 == a**2%2 == a%2]
            [g == a]
            [A11_g == A21_g == 1]
            [A3 == 1]
            # ???bug???:two diff output:No! since not reduced_form
            [u == 0][v == 0][w == 1]:
                [B3 == a-2*c]
                [C3 == c**2]
                [B3 <= -c <= -a <= -A3] #not reduced_form
                !! [[A,B,C,k::int] -> [Qfb(A,B,C) ~=~ Qfb(A,B+2*k*A,C+k*(B+k*A))]] #调整冫二二型中部牜保持等价类
                [k:=-(B3//2)]
                [A4:=A3]
                [B4:=B3%2]
                [B4==a%2==D%2]
                [A4==1]
                -> Qfb(1,D%2,(D%2-D)///4) == one
            [u == 1][v == 0][w == 0]:
                [B3 == a]
                [C3 == a*c]
                [B3 == a >= 1 == A3]
                [a > 1]:
                    [B3 == a >= A3] #not reduced_form
                    同上，[A3==1] => 调整后:输出one
                [a == 1]:
                    [B3 == a == 1] #reduced_form
                    [D==1-4*c]
                    [C3 == c == (1-D)///4]
                    -> Qfb(1,1,(1-D)///4) == one
        [sf == ot == Qfb(a,b,a)]:
            [D==b**2-4*a**2 == (b-2*a)*(b+2*a)]
            [g == gcd(a,b)]
            [A11_g == A21_g == a///gcd(a,b)]
            [A3 =?= 1] #未必是1
            ???未必是sqrt4one
            [u == 0][v == ?][w == ?]
            [v*a+w*b == gcd(a,b)]
            [B3 == b +2*(a///g)*(-a*w)]
            上面是根据代码，但:若直接使用已对准的[B11==b==B21][C11%A21==a%a==0]:
                -> (a**2,b,1)
                -> (1,-b,a**2)
                同上，[a==1] => 调整后:输出one
        #]]]'''#'''
    #end-def __mul__(sf, ot, /):
    def try_factor_D6ambiguous_form_(sf, /):
        '-> zmay_nontrivial_odd_factor4D/(0|nontrivial_odd_factor{D})'
        if sf.eq_one_():
            return 0
        if not sf.is_ambiguous_form_():raise ValueError(sf)
        r'''[[[
        #整数分解牜二二型歧型:goto
        [bqf==Qfb(a,b,a)]:
            [D == b**2 -4*a**2 == (b-2*a)*(b+2*a)]
        [bqf==Qfb(a,a,c)]:
            [D == a**2 -4*a*c == a*(a-4*c)]
        [bqf==Qfb(a,0,c)]:
            [D == -4*a*c]

        ==>>:
        [a == 2]:
            ???
        [a == 2][bqf==Qfb(a,b,a)]:
            [D == b**2 -4*a**2 == (b-2*a)*(b+2*a)]
            [c==a >= b >= 0]
            [2 >= b >= 0]
            [b==2]:
                [gcd(a,b,a) == 2 > 1]
                !! is_primitive7Qfb_
                _L
            [0 <= b <= 1]
            [b == 0]:
                [D == -16]
                even factor
            [b == 1]:
                [D == -15 == -3*5]
        [a == 2][bqf==Qfb(a,a,c)]:
            [D == a**2 -4*a*c == a*(a-4*c)]
            [D == 2*(2-4*c)]
            even factor
        [a == 2][bqf==Qfb(a,0,c)]:
            [D == -4*a*c]
            even factor &?maybe trivial_odd_factor
        #]]]'''#'''
        bqf = sf.binary_quadratic_form7reduced
        (A, B, C) = bqf
        assert A >= 1, sf
        assert A >= B >= 0, sf
        if A == C:
            # [D == b**2 -4*a**2 == (b-2*a)*(b+2*a)]
            factor4D = (B+2*A)
        elif A == B:
            # [D == a**2 -4*a*c == a*(a-4*c)]
            factor4D = A
        elif B == 0:
            # [D == -4*a*c]
            factor4D = A
        else:
            raise 000
        factor4D
        assert factor4D > 0
        (_ez, odd) = factor_pint_out_power_of_base_(2, factor4D)
        odd
        assert odd > 0
        assert odd&1 == 1
        assert bqf.D %odd == 0
        return odd if not odd == 1 else 0
    #end-def try_factor_D6ambiguous_form_(sf, /):
#end-class EqvCls4BinaryQuadraticForm:


def mk_one6Qfb_class_group5D_(D, /):
    match D&3:
        case 0:
            return mk4Qfb_class_group5ABC_(1, 0, -D//4, D=D, to_reduce=True)
        case 1:
            return mk4Qfb_class_group5ABC_(1, 1, (1-D)//4, D=D, to_reduce=True)
        case _:
            raise ValueError('not [D%4 < 2]', D)
    raise 000

def mk4Qfb_class_group5ABC7repr_(A, B, C, /, *, D=None):
    '# [to_reduce:=False]'
    return mk4Qfb_class_group5ABC_(A, B, C, D=D, to_reduce=False)
default4kw7to_reduce = True
def mk4Qfb_class_group5ABC_(A, B, C, /, *, D=None, to_reduce=default4kw7to_reduce):
    if to_reduce:
        (A, B, C) = reduce4Qfb7negD_(A, B, C)
    bqf = EqvCls4BinaryQuadraticForm(BinaryQuadraticForm(A, B, C))
    if not None is D:
        if not bqf.D == D:raise ValueError(D, bqf.D, bqf)

    return bqf


def check_discriminant7Qfb_(D, /):
    # !! [[D < 0] -> [reduced_form <- distinguished_form]]
    if not D < 0:raise TypeError(D)

    # !! [(B**2-4*A*C)%4 < 2]
    if not D&3 < 2:raise TypeError(D)

def nk2D_(n, k4D, /):
    'n/int{>=1}{%2==1} -> k4D/int{>=1}{%2==1}{[gcd(n,k4D) == 1]} -> D/int{<0}{%4<2}'
    check_int_ge(1, n)
    check_int_ge(1, k4D)
    if not n&1:raise ValueError(n)
    if not k4D&1:raise ValueError(k4D)
    if 1 < (g:=gcd(n,k4D)):raise ValueError(n, k4D, g)
    nk = n*k4D
    D = n2D_(nk)
    return D
def n2D_(n, /):
    check_int_ge(1, n)
    if n&1 == 0:raise ValueError
    match n&3:
        case 3:
            D = -n
        case 1:
            D = -4*n
        case _:
            raise 000
    D
    check_discriminant7Qfb_(D)
    return D

def D2A_ge_(D, min4A, /, *, avoid_A_mod8_eq1=False):
    'D -> min4A -> A/odd_prime{>=min4A}{[Jacobi_symbol(A;D) == +1]}'
    check_discriminant7Qfb_(D)
    # [D < 0]
    # [D%4 < 2]
    for A in iter_filter4primes_ge_lt_(max(3, min4A), 1<<81):
        if avoid_A_mod8_eq1 and A&7 == 1:
            continue
        # !! [D == B**2 -4*A*C]
        # [D =[%A]= B**2]
        if 1 == Jacobi_symbol(A, D):
            # [Jacobi_symbol(A;D) == +1]
            # [A :: prime][A >= min_A >= 3][Jacobi_symbol(A;D) == +1]
            # !! [(1+8*_)型素数 开平方更难:需要 平方非剩余]
            # => 最好避免:[A%8 == 1] # ++kw:avoid_A_mod8_eq1
            # => 或者:[gde_(2;A-1) <= max_ez4Amm]
            #       # O((log2(p)+log2(p///odd4p)**(3/2))*log2(p)**2)
            return A
    raise ValueError('iter_filter4primes_ge_lt_:overflow', min4A)
def D2Qfb7A_ge_(D, min4A, /, *, avoid_A_mod8_eq1=False, with_A7repr=False):
    A = D2A_ge_(D, min4A, avoid_A_mod8_eq1=avoid_A_mod8_eq1)
    # [D < 0]
    # [D%4 < 2]
    # [A :: odd_prime]
    # [A >= min4A]
    # [Jacobi_symbol(A;D) == +1]
    for B in iter_sqrts_mod_prime_(A, D):
        # [B**2 =[%A]= D]
        # !! [D == B**2 -4*A*C]
        # [D =[%2]= B**2]
        # [D =[%2]= B]
        if B&1 == D&1:
            # [B%2 == D%2]
            break
    else:
        raise 000
    # [B**2 =[%A]= D]
    # [B%2 == D%2]
    C = C5DAB_(D, A, B)
    bqf7reduced = mk4Qfb_class_group5ABC_(A, B, C, D=D, to_reduce=True)
    777;A7repr = A
    return bqf7reduced if not with_A7repr else (A7repr, bqf7reduced)

def D2QfbPow7A_ge_(D, exp, min4A, /, *, avoid_A_mod8_eq1=False):
    bqf = D2Qfb7A_ge_(D, min4A, avoid_A_mod8_eq1=avoid_A_mod8_eq1)
    return bqf**exp


def n2QfbPow7A_ge_(n, exp, min4A, /, *, avoid_A_mod8_eq1=False):
    D = n2D_(n)
    return D2QfbPow7A_ge_(D, exp, min4A, avoid_A_mod8_eq1=avoid_A_mod8_eq1)




__all__
from seed.math.BinaryQuadraticForm import BinaryQuadraticForm, EqvCls4BinaryQuadraticForm, mk4Qfb_class_group5ABC_, mk4Qfb_class_group5ABC7repr_, mk_one6Qfb_class_group5D_, D5ABC_, C5DAB_
from seed.math.BinaryQuadraticForm import nk2D_, n2D_, D2A_ge_, D2Qfb7A_ge_, D2QfbPow7A_ge_, n2QfbPow7A_ge_ # ++kw:avoid_A_mod8_eq1, kw:with_A7repr
    # [A :: prime][A >= min_A >= 3][Jacobi_symbol(A;D) == +1]
    # !! [(1+8*_)型素数 开平方更难:需要 平方非剩余]
    # => 最好避免:[A%8 == 1] # ++kw:avoid_A_mod8_eq1
    # => 或者:[gde_(2;A-1) <= max_ez4Amm]
    #       # O((log2(p)+log2(p///odd4p)**(3/2))*log2(p)**2)
from seed.math.BinaryQuadraticForm import check_discriminant7Qfb_



from seed.math.BinaryQuadraticForm import *
