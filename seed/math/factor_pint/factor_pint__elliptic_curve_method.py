#__all__:goto
#TODO:goto
#   实现:补丁:更多失败信息:
#       1. ctx{FoundTrivialFactor} verbose print_err;
#       2. stage1结束，stage2起始ctx 即使还未实现stage2，方便未来断点重启
#
#   实现: [X:Z] 省略Y，且齐次无需inv6N_()
#   实现:第二阶段:额外一个大素数
r'''[[[
e ../../python3_src/seed/math/factor_pint/factor_pint__elliptic_curve_method.py
ECM

seed.math.factor_pint.factor_pint__elliptic_curve_method
py -m nn_ns.app.debug_cmd   seed.math.factor_pint.factor_pint__elliptic_curve_method -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.math.factor_pint.factor_pint__elliptic_curve_method:__doc__ -ht # -ff -df
#######

[[
]]


'#'; __doc__ = r'#'
>>> for u in range(1, 35):print(u, try_factor_pint__elliptic_curve_method_(u), sep=':')
1:None
2:None
3:None
4:2
5:None
6:2
7:None
8:2
9:3
10:2
11:None
12:2
13:None
14:2
15:3
16:2
17:None
18:2
19:None
20:2
21:3
22:2
23:None
24:2
25:5
26:2
27:3
28:2
29:None
30:2
31:None
32:2
33:3
34:2

>>> s = set()
>>> while len(s) < 3:s.add(try_factor_pint__elliptic_curve_method_(35))
>>> s == {None, 5, 7}
True


>>> try_factor_pint__elliptic_curve_method_(31, with_ctx=True)
>>> try_factor_pint__elliptic_curve_method_(31, with_ctx=True, result6fail='fail')
'fail'
>>> try_factor_pint__elliptic_curve_method_(34, with_ctx=True)
2
>>> for _ in range(9):try_factor_pint__elliptic_curve_method_(35, with_ctx=True, result6fail=False)   #doctest: +SKIP
(5, ((0, 10000), (0, 2), (Ops4EllipticPseudocurve(35, 5, 8), Pt4EC(-17, 15)), (Ops4EllipticPseudocurve(35, 5, 8), 30)))
False
(7, ((0, 10000), (0, 2), (Ops4EllipticPseudocurve(35, 7, 6), Pt4EC(-12, 7)), (Ops4EllipticPseudocurve(35, 7, 6), 14)))
(5, ((0, 10000), (-1, None), (None, pt_O), (35, 12, 8)))
(5, ((0, 10000), (0, 2), (Ops4EllipticPseudocurve(35, -9, 5), Pt4EC(-5, -10)), (Ops4EllipticPseudocurve(35, -9, 5), -20)))
(7, ((0, 10000), (-1, None), (None, pt_O), (35, 29, 16)))
False
(7, ((0, 10000), (-1, None), (None, pt_O), (35, 16, -12)))
False




>>> for _ in range(9):try_factor_pint__elliptic_curve_method_((-1+2**67), with_ctx=True, result6fail=False)   #doctest: +SKIP
False
False
False
False
False
False
False
(193707721, ((0, 10000), (92, 181), (Ops4EllipticPseudocurve(147573952589676412927, -65329900703389147398, 61110624153339716918), Pt4EC(34206251627092302792, 62573895624016379251)), (Ops4EllipticPseudocurve(147573952589676412927, -65329900703389147398, 61110624153339716918), 5240554684677003330)))
(193707721, ((0, 10000), (155, 571), (Ops4EllipticPseudocurve(147573952589676412927, -43218562940503950175, -48142509726347098493), Pt4EC(-15492791477142507109, -38181994672106652297)), (Ops4EllipticPseudocurve(147573952589676412927, -43218562940503950175, -48142509726347098493), 84961549451557299714)))



















































































py_adhoc_call   seed.math.factor_pint.factor_pint__elliptic_curve_method   @f

]]]'''#'''
__all__ = r'''
try_factor_pint__elliptic_curve_method_
    default__ks5n_and_B_or_ks_
        default__ks5n_and_B_


Ops4EllipticPseudocurve
    Pt4EC
    ZeroPt4EC
        pt_O
    FoundFactor
        FoundNonTrivialFactor
        FoundTrivialFactor


'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.math.prime_sieve.sieve_ge_le import iter_sieve4primes_ge_lt_
    from seed.math.floor_ceil_tools.fc_log import ceil_log_, floor_log_
    from seed.math.factor_pint.perfect_power.detect_perfect_power import factor_pint_as_perfect_power_
    from seed.math.inv_mod__py_ import inv_mod__py_
    from seed.math.hrem_ import hrem_, mk_hrem_
    from seed.math.gcd import gcd, are_coprime
    from seed.tiny_.check import check_type_is, check_int_ge, check_callable
    from seed.for_libs.for_collections.override_repr4namedtuple import mk_namedtuple_, mk_namedtuple__check6make_
    #def mk_namedtuple_(__module__, nm, nms_or_str, /, *args, **kwds):
    #def mk_namedtuple__check6make_(__module__, nm, nms_or_str, /, *args, **kwds):
    #    def _check6make_(sf, /):

    #from seed.tiny_.singleton import mk_SingletonClass
    #def mk_SingletonClass(module_qname, type_qname, /, *bases, **kw):

    from random import randrange
    from seed.helper.ifNone import ifNone


    from itertools import repeat
#.    from functools import cached_property
#.#################################
___end_mark_of_excluded_global_names__0___ = ...
#e script/整数分解牜凑平方牜凑整除幂.py



class FoundFactor(BaseException):
    def __init__(sf, n, ft, ctx=None, /):
        check_int_ge(1, ft)
        check_int_ge(ft, n)
        if not n%ft == 0:raise ValueError(n, ft, ctx)
        sf._n = n
        sf._ft = ft
        sf._ctx = ctx
        super().__init__(n, ft, ctx)
        assert ft == sf.factor
        assert ft == sf.args[1]
    @property
    def N(sf, /):
        return sf._n
    @property
    def factor(sf, /):
        return sf._ft
    @property
    def ctx(sf, /):
        return sf._ctx

class FoundNonTrivialFactor(FoundFactor):pass
class FoundTrivialFactor(FoundFactor):pass

Pt4EC = mk_namedtuple_(__name__, 'Pt4EC', 'x y')
class ZeroPt4EC:
    def __new__(cls, /):
        try:
            return pt_O
        except NameError:
            pass
        sf = super(__class__, cls).__new__(cls)
        return sf
    def __repr__(sf, /):
        return 'pt_O'
    def __reduce__(sf, /):
        return 'seed.math.factor_pint.factor_pint__elliptic_curve_method.pt_O'
pt_O = ZeroPt4EC()
assert pt_O is ZeroPt4EC()

r'''[[[
[Y**2 =[%n]= X**3+a*X+b]
[gcd(n,(4*a**3+27*b**2)) == 1]

[Y**2 =[%n]= X**3+C*X**2+A*X+B]
[g=!=0][h=!=0]:
    [twist_EC{g,EC} := [g*Y**2 =[%n]= X**3+C*X**2+A*X+B]]
    [twist_EC{g,EC} ~=~ twist_EC{g*h**2,EC}]
    [Y:=_Y/g**2][X:=_X/g]
    [_Y**2 =[%n]= _X**3+g*C*_X**2+g**2*A*_X+g**3*B]
[Y**2*Z =[%n]= X**3+C*X**2*Z+A*X*Z**2+B*Z**3]
    [O == (0,1,0)]
        #the point at infinity
[gcd(n,(4*A**3+27*B**2-18*A*B*C-A**2*C**2+4*B*C**3)) == 1]
[-O == O]
[-P == (P.x,-P.y)]
[O+P == P]
[-P+P == O]
[[Q =!= -P] -> [P+Q == R] -> [slope:=if P.x == Q.x then (3*P.x**2+2*C*P.x+A)/(2*P.y) else (P.y-Q.y)/(P.x-Q.x)] -> [R.x==slope**2-C-P.x-Q.x][R.y==-(P.y+slope*(R.x-P.x))]]
    #注意:负号:斜率+镜像 得 -R.y
    #B? 无用？
    # [g==1]
    [Q =!= -P][P.x==Q.x]:
        [P==Q]
        [slope**2 == (3*x**2+2*C*x+A)**2/(4*y**2) ==  (3*x**2+2*C*x+A)**2/4/(x**3+C*x**2+A*x+B)] #无y
    [Q =!= -P][P.x=!=Q.x]:
        [P=!=Q]
        [slope**2 == dy**2/dx**2 == ???y似乎不可避免...]
        [y1**2 -y2**2 == (x1**3 -x2**3) +a*(x1-x2) == fff(x1,x2)]
        [slope == (y1-y2)/(x1-x2) == (x1**2 +x1*x2 +x2**2 +a)/(y1+y2)]
        其实是要求提供更多参数:
            [addh_(P,Q,P-Q) := ...]
        [slope{P+Q}*slope{P-Q} == (yP**2 -yQ**2)/(xP-xQ)**2]
        [slope{P+Q}**2 == fff(x1,x2)**2/(xP-xQ)**4 /slope{P-Q}**2]
        [x{P+Q}==slope{P+Q}**2-C-xP-xQ]
        [x{P-Q}==slope{P-Q}**2-C-xP-xQ]
        [slope{P+Q}**2 == x{P+Q}+C+xP+xQ]
        [slope{P-Q}**2 == x{P-Q}+C+xP+xQ]

    ##################
    [g*Y**2 =[%n]= X**3+C*X**2+A*X+B][Q =!= -P][P.x=!=Q.x]:
        [P=!=Q]
        [Y:=_Y/g**2][X:=_X/g]
        [_Y**2 =[%n]= _X**3+g*C*_X**2+g**2*A*_X+g**3*B]
        ==>>:
        [_slope{P+Q} == ((_yP-_yQ)/(_xP-_xQ))]
        [_slope{P-Q} == ((_yP+_yQ)/(_xP-_xQ))]
        [_x{P+Q} == _slope{P+Q}**2-g*C-_xP-_xQ]
        [_x{P-Q} == _slope{P-Q}**2-g*C-_xP-_xQ]
        ==>>:
        [_slope{P+Q}/g == ((_yP/g**2-_yQ/g**2)/(_xP/g-_xQ/g)) == ((yP-yQ)/(xP-xQ)) == slope{P+Q}]
        [_slope{P-Q}/g == ((_yP/g**2+_yQ/g**2)/(_xP/g-_xQ/g)) == ((yP+yQ)/(xP-xQ)) == slope{P-Q}]
        [x{P+Q} == _x{P+Q}/g == g*(_slope{P+Q}/g)**2-C-_xP/g-_xQ/g == g*slope{P+Q}**2-C-xP-xQ]]
        [x{P-Q} == _x{P-Q}/g == g*(_slope{P-Q}/g)**2-C-_xP/g-_xQ/g == g*slope{P-Q}**2-C-xP-xQ]]
        ==>>:
        [x{P+Q} == g*slope{P+Q}**2-C-xP-xQ]]
        [x{P-Q} == g*slope{P-Q}**2-C-xP-xQ]]
        [slope{P+Q} == ((yP-yQ)/(xP-xQ))]
        [slope{P-Q} == ((yP+yQ)/(xP-xQ))]
        ==>>:

        [x{P+Q} +x{P-Q}
        == g*slope{P+Q}**2 +g*slope{P-Q}**2 -2*C -2*(xP+xQ)
        == 2*(g*yP**2+g*yQ**2)/(xP-xQ)**2 -2*C -2*(xP+xQ)
        == 2*((xP**3+C*xP**2+A*xP+B)+(xQ**3+C*xQ**2+A*xQ+B) -C*(xP-xQ)**2 -(xP+xQ)*(xP-xQ)**2)/(xP-xQ)**2
        == 2*(A*(xP+xQ)+2*B +2*C*xP*xQ +xP*xQ*(xP+xQ))/(xP-xQ)**2
        == 2*(((xP*xQ)+A)*(xP+xQ)+2*(C*(xP*xQ)+B))/(xP-xQ)**2
            # == 2*((M+A)*H+2*(C*M+B))/S**2
        ]
        [x{P+Q} +x{P-Q} == 2*(A*(xP+xQ)+2*B +2*C*xP*xQ +xP*xQ*(xP+xQ))/(xP-xQ)**2]
            #formula4edgecase4addh_:here

        [x{P+Q} * x{P-Q}
        == (g*slope{P+Q}**2 -C -(xP+xQ))*(g*slope{P-Q}**2 -C -(xP+xQ))
        == (g*slope{P+Q}*slope{P-Q})**2 -(C +(xP+xQ))*(g*slope{P+Q}**2+g*slope{P-Q}**2) +(C +(xP+xQ))**2
        == ((g*yP**2-g*yQ**2)/(xP-xQ)**2)**2 -(C +(xP+xQ))*2*(g*yP**2+g*yQ**2)/(xP-xQ)**2 +(C +(xP+xQ))**2
        # (g,yP,yQ)都消失！
        == (((xP**3+C*xP**2+A*xP+B)-(xQ**3+C*xQ**2+A*xQ+B))/(xP-xQ)**2)**2 -(C +(xP+xQ))*2*((xP**3+C*xP**2+A*xP+B)+(xQ**3+C*xQ**2+A*xQ+B))/(xP-xQ)**2 +(C +(xP+xQ))**2
        == (((xP+xQ)**2-xP*xQ+C*(xP+xQ)+A)/(xP-xQ))**2 -(C +(xP+xQ))*2*((xP+xQ)**3-3*xP*xQ*(xP+xQ)+C*(xP+xQ)**2-2*C*xP*xQ+A*(xP+xQ)+2*B)/(xP-xQ)**2 +(C +(xP+xQ))**2
        :> [S:=(xP-xQ)][H:=(xP+xQ)][M:=(xP*xQ)]
        == ((H**2-M+C*H+A)/S)**2 -(C+H)*2*(H**3-3*M*H+C*H**2-2*C*M+A*H+2*B)/S**2 +(C+H)**2
        !! [S**2 == (H**2-4*M)]
        == ((H**2-M+C*H+A)**2 -(C+H)*2*(H**3-3*M*H+C*H**2-2*C*M+A*H+2*B) +(C+H)**2*(H**2-4*M))/S**2
        !! PARI_GP:[((H^2-M+C*H+A)^2 -(C+H)*2*(H^3-3*M*H+C*H^2-2*C*M+A*H+2*B) +(C+H)^2*(H^2-4*M)) == (-4*B*H + (M^2 - 2*A*M + (-4*B*C + A^2)))]
        == (-4*B*H + M**2 -2*A*M -4*B*C +A**2)/S**2
        == ((M-A)**2 -4*B*(H+C))/S**2
        == (((xP*xQ)-A)**2 -4*B*((xP+xQ)+C))/(xP-xQ)**2
        ]
        [x{P+Q} * x{P-Q} == (((xP*xQ)-A)**2 -4*B*((xP+xQ)+C))/(xP-xQ)**2]
        [[B==0] -> [x{P+Q} * x{P-Q} == (((xP*xQ)-A)**2)/(xP-xQ)**2]]
    ##################
    [g*Y**2 =[%n]= X**3+C*X**2+A*X+B][Q =!= -P][P.x==Q.x]:
        [P==Q] # => doubleh_()
        !! [Q =!= -P]
        [2*P == P+P == P+Q =!= P+(-P) == O]
        [2*P =!= O]
        [P.y==0]:
            [-P == P == Q]
            !! [Q =!= -P]
            _L
        [P.y=!=0]
        [yP=!=0]
        [Y:=_Y/g**2][X:=_X/g]
        [_Y**2 =[%n]= _X**3+g*C*_X**2+g**2*A*_X+g**3*B]
        [_yP == g*yP =!=0]
        ==>>:
        [P-Q == O]
        [_slope{P+Q} == ((3*_xP**2+2*g*C*_xP+g**2*A)/(2*_yP))]
        [_x{P+Q} == _slope{P+Q}**2-g*C-_xP-_xQ]
        ==>>:
        [_slope{P+Q} == ((3*(_xP/g)**2+2*C*_xP/g+A)/(2*_yP/g**2)) == ((3*xP**2+2*C*xP+A)/(2*yP)) == slope{P+Q}]
        [x{P+Q} == _x{P+Q}/g == _slope{P+Q}**2/g -C-_xP/g-_xQ/g == slope{P+Q}**2/g -C-xP-xQ]
        ==>>:
        [slope{P+Q} == ((3*xP**2+2*C*xP+A)/(2*yP))]
        [x{P+Q} == slope{P+Q}**2/g -C-2*xP]
        ==>>:
        [x{P+Q}
        == slope{P+Q}**2/g -C-2*xP
        == ((3*xP**2+2*C*xP+A)/(2*yP))**2/g -C-2*xP
        == ((3*xP**2+2*C*xP+A)**2/(4*g*yP**2)) -C-2*xP
        # (g,yP,yQ)都消失！
        == ((3*xP**2+2*C*xP+A)**2/4/(xP**3+C*xP**2+A*xP+B)) -C-2*xP
        == ((3*xP**2+2*C*xP+A)**2 -(C+2*xP)*4*(xP**3+C*xP**2+A*xP+B))/4/(xP**3+C*xP**2+A*xP+B)
        !! PARI_GP:[((3*xP^2+2*C*xP+A)^2 -(C+2*xP)*4*(xP^3+C*xP^2+A*xP+B))== (-4*B*C + (A^2 - 2*xP^2*A + (-8*xP*B + xP^4)))]
        == (-4*B*C -8*xP*B +A**2 -2*xP**2*A +xP**4)/4/(xP**3+C*xP**2+A*xP+B)
        == ((xP**2+A)**2 -4*B*(2*xP+C))/4/(xP**3+C*xP**2+A*xP+B)
        ]
        [x{P+Q} == ((xP**2+A)**2 -4*B*(2*xP+C))/4/(xP**3+C*xP**2+A*xP+B)]
        [P-Q == O]
        [[B==0] -> [x{P+Q} == ((xP**2+A)**2)/4/(xP**3+C*xP**2+A*xP+B)]]
    ##################
    综上:
    ##################
    [g*Y**2 =[%n]= X**3+C*X**2+A*X+B][Q =!= -P][P.x=!=Q.x]:
        [P=!=Q]
        [x{P+Q} * x{P-Q} == (((xP*xQ)-A)**2 -4*B*((xP+xQ)+C))/(xP-xQ)**2]
        [[B==0] -> [x{P+Q} * x{P-Q} == (((xP*xQ)-A)**2)/(xP-xQ)**2]]
    [g*Y**2 =[%n]= X**3+C*X**2+A*X+B][Q =!= -P][P.x==Q.x]:
        [P==Q] # => doubleh_()
        [2*P =!= O]
        [P-Q == O]
        [x{P+Q} == ((xP**2+A)**2 -4*B*(2*xP+C))/4/(xP**3+C*xP**2+A*xP+B)]
        [[B==0] -> [x{P+Q} == ((xP**2+A)**2)/4/(xP**3+C*xP**2+A*xP+B)]]
    ##################
    [g*(Y/Z)**2 =[%n]= (X/Z)**3+C*(X/Z)**2+A*(X/Z)+B]
    [g*Y**2*Z =[%n]= X**3+C*X**2*Z+A*X*Z**2+B*Z**3]
    [g*Y**2*Z =[%n]= X**3+C*X**2*Z+A*X*Z**2+B*Z**3][Q =!= -P][xP/zP=!=xQ/zQ]:
        [P=!=Q][xPzQ=!=xQzP]
        [x{P+Q}/z{P+Q} * x{P-Q}/z{P-Q} == (((xP/zP*xQ/zQ)-A)**2 -4*B*((xP/zP+xQ/zQ)+C))/(xP/zP-xQ/zQ)**2]
        [x{P+Q} / z{P+Q} == z{P-Q}*(((xP*xQ)-A*(zP*zQ))**2 -4*B*((xP*zQ+xQ*zP)+C*(zP*zQ))*(zP*zQ)) / (x{P-Q}*(xP*zQ-xQ*zP)**2)]
        #formula4main4addh_:here
        [x{P+Q} / z{P+Q} == z{P-Q}*((xPxQ-A*zPzQ)**2 -4*B*((xPzQ+xQzP)+C*zPzQ)*zPzQ) / (x{P-Q}*(xPzQ-xQzP)**2)]
        [[B==0] -> [x{P+Q} / z{P+Q} == z{P-Q}*((xPxQ-A*zPzQ)**2) / (x{P-Q}*(xPzQ-xQzP)**2)]]
            # better:[A:=1]
        前提:[x{P-Q}*z{P-Q} =!= 0]

    [g*Y**2*Z =[%n]= X**3+C*X**2*Z+A*X*Z**2+B*Z**3][Q =!= -P][xP/zP==xQ/zQ]:
        [P==Q][xPzQ==xQzP] # => doubleh_()
        [2*P =!= O]
        [P-Q == O]
        [x{P+Q}/z{P+Q} == (((xP/zP)**2+A)**2 -4*B*(2*xP/zP+C))/4/((xP/zP)**3+C*(xP/zP)**2+A*xP/zP+B)]
        [x{P+Q} / z{P+Q} == ((xPxP+A*zPzP)**2 -4*B*(2*xPzP+C*zPzP)*zPzP) / (4*((xPxP*xPzP)+C*xPzP**2+A*(xPzP*zPzP)+B*zPzP**2))]
        #formula4doubleh_:here
        [x{P+Q} / z{P+Q} == ((xPxP+A*zPzP)**2 -4*B*(2*xPzP+C*zPzP)*zPzP) / (4*((xPxP+C*xPzP+A*zPzP)*xPzP+B*zPzP**2))]
        [[B==0] -> [x{P+Q} / z{P+Q} == ((xPxP+A*zPzP)**2) / (4*((xPxP+C*xPzP+A*zPzP)*xPzP))]]
            # [A_zPzP:=A*zPzP]
            # better:[A:=1]
        无前提
    ##################
    def doubleh_(P) -> (2*P):
        #formula4doubleh_:goto
        ... ...
    def addh_(P, Q, P-Q) -> (P+Q):
        #the “h” in the function name emphasizing the homogeneous nature of each [X : Z] pair.
        # (P-Q)用以校准方向，类似super(__class__, cls)
        #   实际上 可通过 一元二次方程 得到函数:[[xP/zP =!= xQ/zQ] => (xP/zP, xQ/zQ) -> {x{P-Q},x{P+Q}}]
        #   (x{P-Q} + x{P+Q})见:formula4edgecase4addh_:goto
        #   (x{P-Q} * x{P+Q})见:formula4main4addh_:goto
        # eg: [(2+2*k)*P := addh_((1+k)*P, (1+k)*P, O) == doubleh_((1+2*k)*P)]
        # eg: [(1+2*k)*P := addh_((1+k)*P, (0+k)*P, P)]
        # eg: [(0+2*k)*P := addh_((0+k)*P, (0+k)*P, O) == doubleh_((2*k)*P)]
        [(xP / zP) := P]
        [(xQ / zQ) := Q]
        [(x{P-Q} / z{P-Q}) := P-Q]
        if zP==0:
            # [P == O]
            return Q
        if zQ==0:
            # [Q == O]
            return P
        if z{P-Q}==0:
            # [P-Q == O]
            # [P == Q]
            # [xPzQ==xQzP]
            return doubleh_(P)
        # [P =!= O]
        # [Q =!= O]
        # [P =!= Q]
        # [xPzQ=!=xQzP]
        if xPzQ == -xQzP:
            # [xPzQ==-xQzP]
            # [P == -Q]
            # [P+Q == O]
            return O
        # [P =!= -Q]
        if x{P-Q}==0:
            ???undefined???
            #低效:formula4edgecase4addh_:goto
            #分解整数时用不上，因为[P-Q===pt6init][pt6init=!=O][另需初始化指派:[pt6init.x =!= 0]]
            raise 000
        # now: 符合前提:[x{P-Q}*z{P-Q} =!= 0]
        #formula4main4addh_:goto
        ... ...
    ##################


3 points on the curve are collinear if and only if they sum to 0.
    This interpretation is generalized to allow for a double intersection at a point of tangency
        (unless it is an inflection point, in which case it is a triple intersection).
    Finally, the geometrical interpretation takes the view that vertical lines intersect the curve at the point at infinity.

[@[p::prime{>3}] -> @[k::uint{>=1}] -> ?[d1,d2::uint{>=1}] -> [EC{FF{p**k}} ~=~ ZZ%d1 * ZZ%d2][gcd(d2, -1+p**k)%d1 == 0]]
    # [d1==1] => cyclic group

[@[p::prime{>3}] -> @[k::uint{>=1}] -> [(len(EC{FF{p**k}}) -(1+p**k))**2 <= 4*p**k]]
    [@[p::prime{>3}] -> @[k::uint{>=1}] -> [abs(len(EC{FF{p**k}}) -(1+p**k)) <= 2*p**(k/2)]]
    当[k%2==1]时，等号不成立:
    [@[p::prime{>3}] -> [(len(EC{ZZ%p}) -(1+p))**2 < 4*p]]
    [@[p::prime{>3}] -> [abs(len(EC{ZZ%p}) -(1+p)) < 2*sqrt(p)]]
    [@[p::prime{>3}] -> [abs(len(EC{ZZ%p}) -(1+p)) <= 2*floor_sqrt(p)]]
    [@[p::prime{>3}] -> [(1+p) -2*floor_sqrt(p) <= len(EC{ZZ%p}) <= (1+p) +2*floor_sqrt(p)]]
        强:只要在此范围内，必然存在某相应曲线#但分布应当是不均匀的
        [m:=len(EC{ZZ%p})]
        What the Deuring theorem actually says is that the number of curves—up to isomorphism—of order m is the so-called Kronecker class number of ((p+1−m)**2−4*m).

affine coordinates:(x,y)|O
    generally involving an inversion for a curve operation.
projective coordinates:(X,Y,Z)
    avoid inversions.
    (X,Y,0) ~ (0,1,0) # vs:O
    (X,Y,Z) ~ (X/Z,Y/Z,1) # vs:(x,y)
modified projective coordinates:(X,Y,Z)
    avoid inversions.
    has a lower operation count than projective coordinates.
    (X,Y,0) ~ (0,1,0) # vs:O
    (X,Y,Z) ~ (X/Z**2,Y/Z**3,1) # vs:(x,y)
    [(Y/Z**3)**2 =[%n]= (X/Z**2)**3 +a*(X/Z**2) +b]
    [Y**2 =[%n]= X**3 +a*X*Z**4 +b*Z**6]
    [O:=[0,1,0]]
    [double_([_,_,0]) == O]
    [double_([_,0,_]) == O]
        ???why???即便(ZZ%p)而非(ZZ%n)，也可能有3个不同根x。
            !! [[P.Y==0] -> [P == -P]]
            !! [[P == -P] -> [2*P == O]]
            [[P.Y==0] -> [2*P == O]]
    [double_([X,Y{=!=0},Z{=!=0}]) == let [M:=3*X**2+a*Z**4][S:=4*X*Y**2][_X:=M**2-2*S][_Y:=M*(S-_X)][_Z:=2*Y*Z] in [_X,_Y,_Z]]
        #原文bug:『[_Y:=M*(S-X2)]』
        #fixed:通过观察:以Z为单位: X:2,Y:3,Z:1,M:4,S:8,_X:8,_Y:12,_Z:4 => 『X2』应当是『_X』或『X**4』
    [add_(O,P) == P]
    [add_(P,O) == P]
    [add_(P{=!=O},Q{=!=O}) == let [[(xP,yP,zP):=P][(xQ,yQ,zQ):=Q][uP:=xQ*zP**2][uQ:=xP*zQ**2][sP:=yQ*zP**3][sQ:=yP*zQ**3][du:=uP-uQ][ds:=sP-sQ][u2:=uP+uQ][s2:=sP+sQ]] in if [du==0==ds] then double_(P) elif [du==0=!=ds] then (if [s2==0] then O else ^gcd) else let [tmp:=u2*du**2][_X:=ds**2-tmp][_Y:=2**-1 *((tmp-2*_X)*ds -s2*du**3)][_Z:=zP*zQ*du] in (_X,_Y,_Z)]
        #以Z为单位: X:2,Y:3,Z:1,u:4,s:6,tmp:12,_X:12,_Y:18,_Z:6
Montgomery coordinates:(X,Z)
    (X,0) ~ (0,1,0) # vs:O
    (X,Z) ~ (X/Z,?,1) # vs:(x,y)
    !! 使用了特别的形式:[g*Y**2 == X**3+C*X**2+X]
    which are the same as the projective coordinates [X,Y,Z], but with "Y" dropped.
    One can recover the x coordinate of the affine point when Z =!= 0 as x = X/Z.
        There are generally two possibilities for y, and this is left ambiguous.
    This option tends to work well in elliptic multiplication and when y-coordinates are not needed at any stage
        #{见上面:addh_()}:y似乎不可避免，而且:如何区分 2*P vs P+(-P) 如何区分P+Q vs P-Q
        ####？P+Q vs P-Q:加减法得到同样的X坐标值？非是，而是增添参数(P-Q)以甄别: #formula4main4addh_:goto
        , as sometimes happens in certain factorization and cryptography work, or when the elliptic algebra must be carried out in higher domains where coordinates themselves can be polynomials.

Theorem 7.4.3 (ECM curve construction)
    [d !<- {0,1,5}]
    [u:=d**2-5]
    [v:=d*4]
    [C(d):=-2 +(v-u)**3*(3*u+v)/(4*u**3*v)]
    [EC{d;ZZ%p} := [Y**2 =[%p]= X**3+C(d)*X**2+X]]
    [len(EC{d;ZZ%p})%12 == 0]
    [?[pt :: point{x==(u/v)**3}] -> [pt <- (EC{d;ZZ%p} | EC{d;ZZ%p}.twist)]]
        What is more, we do not even care whether an initial point is on E or its twist, again because y-coordinate ignorance is allowed.
        初始点:[X/Z == u**3/v**3] 忽略Y值，不在意用的是(EC{d;ZZ%p} | EC{d;ZZ%p}.twist)

stage1:第一阶段:
    [P1:=II(ks{B1})*P0]
        default__ks5n_and_B_()
stage2:第二阶段:
    TODO
    前提:P1幸存，没有^FoundNonTrivialFactor
    经验:占比{第二阶段耗时/总耗时} <- [1/4 ~ 1/2]
        [B2 := 100*B1]
    [P{k,P1} =[def]= k*P1]
    [q1 := next_prime_(1+B1)]
    [P{q1,P1} := q1*P1]
    for q1,q2 in pairwise(primes_ge_lt(q1,1+B2)):
        [dq := (q2-q1)]
        [P{dq,P1} := cached(dq*P1)]
        [P{q2,P1} := P{q1,P1} +P{dq,P1}]
            但只需检测:gcd(n,(P{q1,P1}.X*P{dq,P1}.Z -P{q1,P1}.Z*P{dq,P1}.X))
            [X1*Zd -Z1*Xd == (X1-Xd)*(Z1+Zd) -X1*Z1 +Xd*Zd]
            少量{q1}+大量{dq}足以覆盖全部可能素数:检测累积gcd(n,II(...{q1}))

Algorithm 7.2.7 (Elliptic multiplication: Montgomery method).
    (X:Z)表达
    TODO
Algorithm 7.4.4 (Inversionless ECM)
    TODO


实例一:
    [n := M667 = -1+2**667]
    [d := 8689346476060549]
    [B1 := 11000000 = 11*10**6]
    [B2 := 100*B1]
    [M667 == (1943118631 * 531132717139346021081 * 978146583988637765536217 * 53625112691923843508117942311516428173021903300344567 * some_a_PRIME)]
    [p53{M667} := 53625112691923843508117942311516428173021903300344567]
    [len(EC{d;ZZ%p53{M667}}) == (2**4 * 3**9 * 3079 * 152077 * 172259 * 1067063 * 3682177 * 3815423 * 8867563 * 15880351)]
    [[8867563 < B1 < 15880351 < B2] -> [p53{M667} 发现于 第二阶段]]
实例二:
    [n := F15 = 1+2**2**15]
    [d := 253301772]
    [B1 :=  = 10**7]
    [B2 := 50*B1]
    [p33{F15} := 168768817029516972383024127016961]
    [len(EC{d;ZZ%p33{F15}}) == (2**5 * 3 * 1889 * 5701 * 9883 * 11777 * 5909317 * 91704181)]
    [[5909317 < B1 < 91704181 < B2] -> [p33{F15} 发现于 第二阶段]]

    [p27{F16} := 188981757975021318420037633]
        原文bug:F15因子33位188...633
        到底是F15还是F16?
        view others/数学/prime/Fermat_primes.txt
            F15= 1214251009 · 2327042503868417 · 168768817029516972383024127016961 · C
            F16= 825753601 · 188981757975021318420037633 · C


#]]]'''#'''
#elliptic pseudocurve
class Ops4EllipticPseudocurve:
    'ops4elliptic_pseudocurve #[Y**2 =[%n]= X**3+a*X+b][n :: uint{>=2}][gcd(n,6) == 1][a,b::int][gcd(n,(4*a**3+27*b**2)) == 1]'
    def __init__(sf, n, a, b, /):
        check_int_ge(10, n)
        check_type_is(int, a)
        check_type_is(int, b)
        # [n >= 10]
        if not 1 == (g:=gcd(n, 6)):
            # !! [n >= 10]
            raise FoundNonTrivialFactor(n, g)
        hrem6N_ = mk_hrem_(n)
        a = hrem6N_(a)
        b = hrem6N_(b)
        if not 1 == (g:=gcd(n, discriminant:=(4*a**3+27*b**2))):
            ctx = (n, a, b)
            if 1 < g < n:
                raise FoundNonTrivialFactor(n, g, ctx)
            assert g == n, (n, g)
            raise FoundTrivialFactor(n, g, ctx)
        sf._hrem6N_ = hrem6N_
        sf._n = n
        sf._a = a
        sf._b = b
        sf._args = (n, a, b)
    @classmethod
    def mk_ex5n__7random_(cls, n, may_random_uint_mod_=None, /):
        check_int_ge(10, n)
        # [n >= 10]
        if not 1 == (g:=gcd(n, 6)):
            # !! [n >= 10]
            raise FoundNonTrivialFactor(n, g)

        random_uint_mod_ = ifNone(may_random_uint_mod_, randrange)
        check_callable(random_uint_mod_)
        hrem6N_ = mk_hrem_(n)
        while 1:
            x = random_uint_mod_(n)
            y = random_uint_mod_(n)
            a = random_uint_mod_(n)
            yy = hrem6N_(y**2)
            xx = hrem6N_(x**2)
            xxx = hrem6N_(x*xx)
            ax = hrem6N_(x*a)
            b = hrem6N_(yy -xxx -ax)
            if not 1 == (g:=gcd(n, discriminant:=(4*a**3+27*b**2))):
                ctx = (n, a, b)
                if 1 < g < n:
                    raise FoundNonTrivialFactor(n, g, ctx)
                assert g == n, (n, g)
                continue
            break
        sf = cls(n, a, b)
        pt = sf.mk_point_(x, y)
        return (sf, pt)
    @property
    def params4elliptic_pseudocurve(sf, /):
        '-> (n, a, b)'
        return sf._args
    def __repr__(sf, /):
        nab = (n, a, b) = sf._args
        return f'Ops4EllipticPseudocurve{nab}'
    def __eq__(sf, ot, /):
        if not isinstance(ot, __class__):return NotImplemented
        return sf is ot or sf._args == ot._args
    def mk_point_(sf, x, y, /):
        'int -> int -> pt'
        hrem6N_ = sf._hrem6N_
        x = hrem6N_(x)
        y = hrem6N_(y)
        pt = Pt4EC(x, y)
        return pt

    @property
    def zero(sf, /):
        return pt_O
    def eq_zero_(sf, pt, /):
        return pt is pt_O
    def eq_(sf, pt6lhs, pt6rhs, /):
        match (pt6lhs, pt6rhs):
            case (sf.zero, sf.zero):
                return True
            case (Pt4EC(), Pt4EC()):
                return pt6lhs == pt6rhs
        raise TypeError(type(pt6lhs), type(pt6rhs))
    def neg_(sf, pt, /):
        match pt:
            case sf.zero:
                return pt
            case Pt4EC(x=x, y=y):
                # !! hrem6N_ && [n :: odd]
                return Pt4EC(x, -y)
        raise TypeError(type(pt))
    def double_(sf, pt, /):
        return sf.add_(pt, pt)
    def sub_(sf, pt6lhs, pt6rhs, /):
        return sf.add_(pt6lhs, sf.neg_(pt6rhs))
    def add_(sf, pt6lhs, pt6rhs, /):
        match (pt6lhs, pt6rhs):
            case (sf.zero, pt):
                return pt
            case (pt, sf.zero):
                return pt
            case (Pt4EC(x=xL, y=yL), Pt4EC(x=xR, y=yR)):
                # (n, a, b) = sf._args
                a = sf._a
                hrem6N_ = sf._hrem6N_
                # [[Q =!= -P] -> [P+Q == R] -> [slope:=if P.x == Q.x then (3*P.x**2+2*C*P.x+A)/(2*P.y) else (P.y-Q.y)/(P.x-Q.x)] -> [R.x==slope**2-C-P.x-Q.x][R.y==-(P.y+slope*(R.x-P.x))]]
                if xL == xR:
                    if yL == -yR:
                        # [pt6lhs == -pt6rhs]
                        return sf.zero
                    #assert yL == yR, (sf, pt6lhs, pt6rhs)
                    if not yL == yR:
                        ctx = (sf, pt6lhs, pt6rhs)
                        n = sf._n
                        ft = gcd(n, yL-yR)
                        if 1 < ft < n:
                            raise FoundNonTrivialFactor(n, ft, ctx)
                        assert ft == n, (n, ft)
                        raise ValueError('non-std point:should use .mk_point_():', ctx)
                    # [pt6lhs == pt6rhs]
                    # double_()
                    # !! [C==0]
                    slope = hrem6N_(hrem6N_(3*xL**2 +a) *sf.inv6N_(yL<<1))
                else:
                    slope = hrem6N_((yL-yR)*sf.inv6N_(xL-xR))
                slope
                # !! [C==0]
                _x = hrem6N_(slope**2 -(xL+xR))
                _y = hrem6N_(-(yL+slope*(_x-xL)))
                pt = sf.mk_point_(_x, _y)
                return pt
        raise TypeError(type(pt6lhs), type(pt6rhs))
    def inv6N_(sf, x, /):
        n = sf._n
        try:
            r = inv_mod__py_(n, x)
        except ValueError:
            ctx = (sf, x)
            ft = gcd(n, x)
            if 1 < ft < n:
                raise FoundNonTrivialFactor(n, ft, ctx)
            assert ft == n, (n, ft)
            raise FoundTrivialFactor(n, ft, ctx)
        hrem6N_ = sf._hrem6N_
        return hrem6N_(r)
    def mul_(sf, k, pt, /):
        out = sf.zero
        if k < 0:
            ot = sf.neg_(pt)
            k = -k
        for b in map(int, f'{k:b}'):
            out = sf.double_(out)
            if b:
                out = sf.add_(out, pt)
        return out

#end-class Ops4EllipticPseudocurve:

def default__ks5n_and_B_(n, B, /):
    for p in iter_sieve4primes_ge_lt_(2, 1+B):
        ep = floor_log_(p, B)
        yield from repeat(p, ep)
def default__ks5n_and_B_or_ks_(n, B_or_ks, /):
    match B_or_ks:
        case int() as B:
            check_int_ge(2, B)
            ks = default__ks5n_and_B_(n, B)
            ks = iter(ks)
        case ks:
            ks = iter(ks)
        #case _: raise TypeError(type(B_or_ks))
    return ks
def try_factor_pint__elliptic_curve_method_(n, Bs_or_kss=None, ks5n_and_B_or_ks_=None, /, *, random_uint_mod_=None, with_ctx=False, result6fail=None):
    'n/uint{>=1} -> Iter (B/uint{>=2}|ks/(Iter k/uint{>=2})) -> may (n -> (B|ks) -> ks) -> may non_trivial_factor{n} # [ks are multiplier => II(ks)*pt] # [B is smooth bound => ks:=chains(repeat(p,floor_log_(p,B)) for p in primes_lt(1+B))] # [[p::prime][n%p==0][1==gcd(n,[1..<p])] -> [best:B1:=exp((1/sqrt2+o(1))*sqrt(ln(p)*lnln(p)))]]'
    check_int_ge(1, n)
    if n < 4:
        return result6fail#None
    if n&1 == 0:
        return 2
    if n%3 == 0:
        return 3
    # [1 == gcd(n, 6)]
    (rt, e) = factor_pint_as_perfect_power_(n)
    if 1 < rt < n:
        return rt
    # [not$is_perfect_power_(n)]
    # [1 == gcd(n, 6)]

    # [n::prime]or[n>=35]
    if n < 35:
        return result6fail#None
    # [n >= 35]

    Bs_or_kss = ifNone(Bs_or_kss, [1_00_00])
    ks5n_and_B_or_ks_ = ifNone(ks5n_and_B_or_ks_, default__ks5n_and_B_or_ks_)
    check_callable(ks5n_and_B_or_ks_)
    random_uint_mod_ = ifNone(random_uint_mod_, randrange)
    check_callable(random_uint_mod_)

    try:
        #########
        #for:ctx:
        (j4ks, B_or_ks) = (-1, None)
        (j4k, k) = (-1, None)
        (ops4EPC, pt) = (None, pt_O)
        #########
        for (j4ks, B_or_ks) in enumerate(Bs_or_kss):
            ks = ks5n_and_B_or_ks_(n, B_or_ks)
            (ops4EPC, pt) = Ops4EllipticPseudocurve.mk_ex5n__7random_(n, random_uint_mod_)
            _pt = pt
            mul_ = ops4EPC.mul_
            for (j4k, k) in enumerate(ks):
                try:
                    _pt = mul_(k, _pt)
                except FoundTrivialFactor:
                    'from:inv6N_()'
                    break
            #########
            #for:ctx:
            (j4k, k) = (-1, None)
            (ops4EPC, pt) = (None, pt_O)
            #########
    except FoundNonTrivialFactor as exc:
        if exc.N == n:
            ft = exc.factor
            ctx = ((j4ks, B_or_ks), (j4k, k), (ops4EPC, pt), exc.ctx)
            return ft if not with_ctx else (ft, ctx)
        raise
    return result6fail#None


__all__
from seed.math.factor_pint.factor_pint__elliptic_curve_method import try_factor_pint__elliptic_curve_method_
#def try_factor_pint__elliptic_curve_method_(n, Bs_or_kss=None, ks5n_and_B_or_ks_=None, /, *, random_uint_mod_=None, with_ctx=False, result6fail=None):
from seed.math.factor_pint.factor_pint__elliptic_curve_method import *
