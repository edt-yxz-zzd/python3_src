#__all__:goto
r'''[[[
e ../../python3_src/seed/math/continued_fraction/continued_fraction_ops.py
doctest____begin:goto
doctest____end:goto


seed.math.continued_fraction.continued_fraction_ops
py -m nn_ns.app.debug_cmd   seed.math.continued_fraction.continued_fraction_ops -x
py -m nn_ns.app.doctest_cmd seed.math.continued_fraction.continued_fraction_ops:__doc__ -ff -v
py -m nn_ns.app.doctest_cmd seed.math.continued_fraction.continued_fraction_ops:__doc__ -ht
py_adhoc_call   seed.math.continued_fraction.continued_fraction_ops   @f
from seed.math.continued_fraction.continued_fraction_ops import *



[cf_digits :: half_std_cf]:
    #sure_cf_digits_be_half_std()
    empty => ^ContinuedFractionError__inf__no_cf0
    fst :: int
    other :: pint == int{>=1}
    #but not require [[finite]->[last >= 2]]
    #   since cut-off: islice(cf_digits, sz)
    #####
    upcoming_cf_digit <- [+oo,1..]

        [cf_eqv(cf_digits, cf_digits++[+oo, ...])]
        [cf([]) == cf([+oo]) == +oo]
        [cf([a;]) == cf([a;+oo]) == a]



cf :: cf_digits -> (+oo|Real)

[[[
lazy惰性求值，按需动态精度
===
cf_inv:
cf_neg:
cf_sub:
cf_add:
cf_divmod:
cf_truediv:
cf_mul:
pow__cf__int_:
cf_pow_:fail
cf_log_:
cf_ge_: #limit_denominator?
cf_le_:
cf_gt_:
cf_lt_:
cf_cmp_:
cf_ne_:
cf_eq_:
===
cf_inv(cf_digits):
    * [cf0==0]:
        -> cf_digits[1:] # may be +oo
    * [cf0>0]:
        -> [0]++cf_digits
    * [cf0<0]:
        -> cf_neg(cf_inv(cf_neg(cf_digits)))

===
cf_neg(cf_digits):
    * [len(cf_digits)==1]:
        -> [-cf0;]
                # cf_neg__case1
                # <==> [cf_digits==[cf0;]]
    * [len(cf_digits)==2][cf1==1]:
        -> [-1-cf0;]
                # cf_neg__case2
                # <==> [cf_digits==[cf0;1]]
    * [[len(cf_digits)>=3][cf1==1]]:
        -> [-1-cf0;cf2+1,*cf_digits[3:]]
                # cf_neg__case3
                # <==> [cf_digits==[cf0;1,cf2,...]]
    * [[len(cf_digits)>=2][cf1>=2]]:
        -> [-1-cf0;1,cf1-1,*cf_digits[2:]]
                # cf_neg__case4
    ########
    [[proof:
    [cf0:=cf_digits[0]][x:=cf(cf_digits[1:])]:
        [cf(cf_digits) == (cf0+1/x)]
        [[x==+oo]or[[x :: Real][x>=1.0]]]
        [-(cf0+1/x) == -cf0-1/x == ???:
        * [x==+oo]:
            # <==> [len(cf_digits)==1]
            == -cf0
                # cf_neg__case1
                # <==> [len(cf_digits)==1]
        * [x :: Real][x>=1.0]:
            # <==> [len(cf_digits)>=2]
            * [x == 1]:
                # <==> [cf_digits==[cf0;1]]
                == -cf0-1
                    # cf_neg__case2
                    # <==> [cf_digits==[cf0;1]]
            * [x :: Real][x>1.0]:
                # <==> [[len(cf_digits)>2]or[cf1>1]]
                == -(cf0+1) +(1-1/x)
                !! [x>1.0]
                #  [0.0 < 1/x < 1.0]
                #  [0.0 < 1-1/x < 1.0]
                !! [x:=cf(cf_digits[1:])]
                #  [1/x==cf(cf_inv(cf_digits[1:])) == [0;*cf_digits[1:]]]
                #  [-1/x==cf(cf_neg([0;*cf_digits[1:]]))]
                == -(cf0+1) +(1+cf(recur~cf_neg(cf_digits[1:])))
                    #useless
                #####restart:
                == -(cf0+1) +(1-1/x)
                == -(cf0+1) +1/(1/(1-1/x))
                !! [x>1.0]
                #  [0.0 < 1/x < 1.0]
                #  [0.0 < 1-1/x < 1.0]
                #  [1/(1-1/x) > 1.0]
                == cf([-cf0-1;*to_cf_digits(1/(1-1/x))])
                #  [1/(1-1/x) = x/(x-1) = 1+1/(x-1)]
                == cf([-cf0-1;*to_cf_digits(1+1/(x-1))])
                * [cf1==1]:
                    # <==> [[len(cf_digits)>=3][cf1==1]]
                    !! [x>1.0]
                    # [len(cf_digits)>=3]
                    !! [x:=cf(cf_digits[1:])]
                    # [(x-1) == cf [0;*cf_digits[2:]]]
                    # [1/(x-1) == cf cf_digits[2:]]
                    # [1+1/(x-1) == cf([1+cf2]++cf_digits[3:])]
                    == cf([-cf0-1;*to_cf_digits(1+1/(x-1))])
                    == cf([-cf0-1;cf2+1,*cf_digits[3:]])
                        # cf_neg__case3
                        # <==> [[len(cf_digits)>=3][cf1==1]]
                * [cf1>=2]:
                    # <==> [[len(cf_digits)>=2][cf1>=2]]
                    # [x >= 2.0]
                    # [x-1 >= 1.0]
                    [1/(x-1) <= 1.0]
                    !! [x:=cf(cf_digits[1:])]
                    # [(x-1) == [cf1-1;*cf_digits[2:]]]
                    !! [cf1>=2]
                    #  [cf1-1 >= 1]
                    # [1/(x-1) == [0;cf1-1,*cf_digits[2:]]]
                    # [1+1/(x-1) == [1;cf1-1,*cf_digits[2:]]]
                    == cf([-cf0-1;*to_cf_digits(1+1/(x-1))])
                    == cf([-cf0-1;1,cf1-1,*cf_digits[2:]])
                        # cf_neg__case4
                        # <==> [[len(cf_digits)>=2][cf1>=2]]
        ]
    DONE
    ]]
    ########
===
cf_sub(lhs, rhs):
    -> cf_add(lhs, cf_neg(rhs))
===
cf_add(lhs, rhs):
    #update:针对整数优化
    双变量模式y,z
    st4cf_add.init := (0 + 1*y + 1*z + (cf0L+cf0R)*y*z)/(0 + 0*y + 0*z + y*z)
        #init
        #ContinuedFractionState__2vars
    while 1:
        while not 四组合向下取整是否一致:
            展开y,z
            if 有一个操作数有限长并首先结束:
                切换到 单变量模式y
        cf0 := nyz/dyz
            # == flr(++) #flr()定义
            # == flr(??) #一致
        yield cf0
        st4cf_add -= cf0
        if st4cf_add == 0:break
        st4cf_add := 1/st4cf_add

[[
    vivi:ContinuedFractionFoldState
    [st4cf_add =[def]= (n1+ny*y+nz*z+nyz*y*z)/(d1+dy*y+dz*z+dyz*y*z)]
    [y := the remain tail of lhs cf_digits]
    [z := the remain tail of rhs cf_digits]
    [n1,ny,nz,nyz :: int]  #allow neg!!
    [d1,dy,dz,dyz :: uint] #almost pint
    [y <- [1.0 .. =+oo]]
    [z <- [1.0 .. =+oo]]
    ########
    init:
    [cf0L+1/y := cf(lhs)]
    [cf0R+1/z := cf(rhs)]
    [st4cf_add
    == cf(lhs) + cf(rhs) # <<== cf_add def
    == cf0L+cf0R + (y+z)/(y*z)
    == ((y+z) + (cf0L+cf0R)*y*z)/(y*z)
    == (0 + 1*y + 1*z + (cf0L+cf0R)*y*z)/(0 + 0*y + 0*z + y*z)
    ]

    ########
    feed one lhs cf_digit K:
    [y == K+1/g]:
        [st4cf_add
        == (n1+ny*y+nz*z+nyz*y*z)/(d1+dy*y+dz*z+dyz*y*z)
        # mul g
        # [y*g == K*g+1]
        == (n1*g+ny*(1+K*g)+nz*z*g+nyz*(1+K*g)*z)/(d1*g+dy*(1+K*g)+dz*z*g+dyz*(1+K*g)*z)
        == (n1*g+ny+ny*K*g+nz*z*g+nyz*z+nyz*K*g*z)/(d1*g+dy*(1+K*g)+dz*z*g+dyz*(1+K*g)*z)
        == (ny+(n1+ny*K)*g+nyz*z+(nz+nyz*K)*g*z)/(dy+(d1+dy*K)*g+dyz*z+(dz+dyz*K)*g*z)
        ]
    ==>>:
    左展开更新公式:[y == K+1/g]:
        [n1' := ny]
        [ny' := (n1+ny*K)]
        [nz' := nyz]
        [nyz' := (nz+nyz*K)]
        [d1' := dy]
        [dy' := (d1+dy*K)]
        [dz' := dyz]
        [dyz' := (dz+dyz*K)]
    同理==>>:
    右展开更新公式:[z == K+1/s]:
        [n1' := nz]
        [ny' := nyz]
        [nz' := (n1+nz*K)]
        [nyz' := (ny+nyz*K)]
        [d1' := dz]
        [dy' := dyz]
        [dz' := (d1+dz*K)]
        [dyz' := (dy+dyz*K)]
    每次更新，八个参数中，四个值 只是移动
    ########
    偏导，极值:
    [y <- [1.0 .. =+oo]][z <- [1.0 .. =+oo]]:
        [st4cf_add(y,z) -> Real]
        [Dy st4cf_add(y,z)
        # [nnnn/dddd := st4cf_add(y,z)]
        == (Dy nnnn)/dddd + nnnn*(Dy 1/dddd)
        == (Dy nnnn)/dddd - nnnn/dddd**2 *(Dy dddd)
        == ((Dy nnnn)*dddd - nnnn*(Dy dddd))/dddd**2
        ]
        [Dynndd := ((Dy nnnn)*dddd - nnnn*(Dy dddd))]
        [sign_of(Dy st4cf_add(y,z))
        == sign_of(((Dy nnnn)*dddd - nnnn*(Dy dddd))/dddd**2)
        == sign_of((Dy nnnn)*dddd - nnnn*(Dy dddd))
        == sign_of(Dynndd)
        ]
        [sign_of(Dy st4cf_add(y,z)) == sign_of(Dynndd)]
        同理:
        [Dznndd := ((Dz nnnn)*dddd - nnnn*(Dz dddd))]
        [sign_of(Dz st4cf_add(y,z)) == sign_of(Dznndd)]


        [(Dy nnnn)
        == Dy (n1+ny*y+nz*z+nyz*y*z)
        == (ny+nyz*z)
        ]
        [(Dy nnnn)*dddd
        == (ny+nyz*z)*(d1+dy*y+dz*z+dyz*y*z)
        == ((ny*d1+ny*dy*y+ny*dz*z+ny*dyz*y*z) + (nyz*z*d1+nyz*z*dy*y+nyz*z*dz*z+nyz*z*dyz*y*z))
        ==(
            +ny*d1
            +ny*dy*y
            +(ny*dz+nyz*d1)*z
            +(ny*dyz+nyz*dy)*y*z
            +nyz*dz*z*z
            +nyz*dyz*y*z*z
            )
        ]
        [nnnn*(Dy dddd)
        ==(
            +n1*dy
            +ny*dy*y
            +(nz*dy+n1*dyz)*z
            +(nyz*dy+ny*dyz)*y*z
            +nz*dyz*z*z
            +nyz*dyz*y*z*z
            )
        ]
        [Dynndd
        == ((Dy nnnn)*dddd - nnnn*(Dy dddd))
        ==(
            +ny*d1
            +ny*dy*y
            +(ny*dz+nyz*d1)*z
            +(ny*dyz+nyz*dy)*y*z
            +nyz*dz*z*z
            +nyz*dyz*y*z*z
            -n1*dy
            -ny*dy*y
            -(nz*dy+n1*dyz)*z
            -(nyz*dy+ny*dyz)*y*z
            -nz*dyz*z*z
            -nyz*dyz*y*z*z
            )
        ==(
            +ny*d1
            -n1*dy
            +ny*dy*y   #
            -ny*dy*y   #
            +(ny*dz+nyz*d1)*z
            -(nz*dy+n1*dyz)*z
            +(ny*dyz+nyz*dy)*y*z  #
            -(nyz*dy+ny*dyz)*y*z  #
            +nyz*dz*z*z
            -nz*dyz*z*z
            +nyz*dyz*y*z*z   #
            -nyz*dyz*y*z*z   #
            )
        ==(
            +ny*d1
            -n1*dy
            +(ny*dz+nyz*d1)*z
            -(nz*dy+n1*dyz)*z
            +nyz*dz*z*z
            -nz*dyz*z*z
            )
        ==(
            +(ny*d1 -n1*dy)
            +(ny*dz+nyz*d1 -nz*dy-n1*dyz)*z
            +(nyz*dz -nz*dyz)*z*z
            )
        ]
        [Dynndd == (+(ny*d1 -n1*dy) +(ny*dz+nyz*d1 -nz*dy-n1*dyz)*z +(nyz*dz -nz*dyz)*z*z)]
        [Dynndd == ((ny +nyz*z)*(d1 +dz*z) -(dy +dyz*z)*(n1 +nz*z))]
        同理==>>:
        [Dznndd == (+(nz*d1 -n1*dz) +(nz*dy+nyz*d1 -ny*dz-n1*dyz)*y +(nyz*dy -ny*dyz)*y*y)]
        [Dznndd == ((nz +nyz*y)*(d1 +dy*y) -(dz +dyz*y)*(n1 +ny*y))]
            :s/y/g/g
            :s/z/y/g
            :s/g/z/g
            :s/zy/yz/g
        !! [Dynndd := ((Dy nnnn)*dddd - nnnn*(Dy dddd))]
        !! [Dznndd := ((Dz nnnn)*dddd - nnnn*(Dz dddd))]
        !! [sign_of(Dy st4cf_add(y,z)) == sign_of(Dynndd)]
        !! [sign_of(Dz st4cf_add(y,z)) == sign_of(Dznndd)]
        !! [Dynndd == (+(ny*d1 -n1*dy) +(ny*dz+nyz*d1 -nz*dy-n1*dyz)*z +(nyz*dz -nz*dyz)*z*z)]
        !! [Dznndd == (+(nz*d1 -n1*dz) +(nz*dy+nyz*d1 -ny*dz-n1*dyz)*y +(nyz*dy -ny*dyz)*y*y)]
        !! [Dynndd == ((ny +nyz*z)*(d1 +dz*z) -(dy +dyz*z)*(n1 +nz*z))]
        !! [Dznndd == ((nz +nyz*y)*(d1 +dy*y) -(dz +dyz*y)*(n1 +ny*y))]
        [sign_of(Dy st4cf_add(y,z)) == sign_of(+(ny*d1 -n1*dy) +(ny*dz+nyz*d1 -nz*dy-n1*dyz)*z +(nyz*dz -nz*dyz)*z*z)]
        [sign_of(Dz st4cf_add(y,z)) == sign_of(+(nz*d1 -n1*dz) +(nz*dy+nyz*d1 -ny*dz-n1*dyz)*y +(nyz*dy -ny*dyz)*y*y)]
        ####
        #[A*x**2+B*x+C==0][B**2-4*A*C==?]
        Dy<z>:
        [(ny*dz+nyz*d1 -nz*dy-n1*dyz)**2 - 4*(nyz*dz -nz*dyz)*(ny*d1 -n1*dy)
            #[B**2-4*A*C==?] for Dy<z>:
        ==(
            -2*(ny*dz+nyz*d1)*(nz*dy+n1*dyz)
            +(ny*dz-nyz*d1)**2  # + --> -
            +(nz*dy-n1*dyz)**2  # + --> -
            +4*nyz*dz*n1*dy
            +4*nz*dyz*ny*d1
            )
        ==(
            +(n1*dyz)**2
            +(ny*dz)**2
            +(nz*dy)**2
            +(nyz*d1)**2
            -2*n1*ny*dz*dyz
            -2*n1*nz*dy*dyz
            -2*n1*nyz*d1*dyz
            +4*n1*nyz*dy*dz
            +4*ny*nz*d1*dyz
            -2*ny*nz*dy*dz
            -2*ny*nyz*d1*dz
            -2*nz*nyz*d1*dy
            )
        ]
        ####
    ####
    对于 加法 而言，极值应当出现在 边界(二次函数虚根或两根<1.0)
    [y,z <- {1.0,+oo}]:
        共4种组合
        求floor
        4组合floor一致时，不必再展开
        不一致时，展开谁？
        按 分母大小？
        !! [st4cf_add =[def]= (n1+ny*y+nz*z+nyz*y*z)/(d1+dy*y+dz*z+dyz*y*z)]
        * [y==+oo][z==+oo]:
            # mul (1/y)(1/z)
            [st4cf_add == nyz/dyz]
        * [y==1.0][z==+oo]:
            # mul (1/z)
            [st4cf_add == (nz+nyz)/(dz+dyz)]
        * [y==+oo][z==1.0]:
            # mul (1/y)
            [st4cf_add == (ny+nyz)/(dy+dyz)]
        * [y==1.0][z==1.0]:
            [st4cf_add == (n1+ny+nz+nyz)/(d1+dy+dz+dyz)]
        左展开更新公式:[y == K+1/g]:goto
        右展开更新公式:[z == K+1/s]:goto
        [flr(b0?,b1?) =[def]= floor(st4cf_add<y=+oo if b0 else 1.0,z=+oo if b1 else 1.0>)]
        [flr(--) =!= flr(-+)]:
            不一致，展开谁感觉都行
            还是 展开z后 一致的概率更大
        展开y if:
            * [flr(--) =!= flr(+-)]
            * [flr(-+) =!= flr(++)]
        展开z if:
            * [flr(--) =!= flr(-+)]
            * [flr(+-) =!= flr(++)]
        同时展开y,z
    ####
    输出cf0之后更新:
    [st4cf_add' =[def]= 1/(st4cf_add - cf0)]
    [st4cf_add'
    == 1/(st4cf_add - cf0)
    !! [st4cf_add =[def]= (n1+ny*y+nz*z+nyz*y*z)/(d1+dy*y+dz*z+dyz*y*z)]
    == (d1+dy*y+dz*z+dyz*y*z)/((n1+ny*y+nz*z+nyz*y*z) - cf0*(d1+dy*y+dz*z+dyz*y*z))
    == (d1+dy*y+dz*z+dyz*y*z)/((n1-cf0*d1) +(ny-cf0*dy)*y +(nz-cf0*dz)*z +(nyz-cf0*dyz)*y*z)
    ]
    向下取整辗转更新公式:[st4cf_add == cf0 + 1/st4cf_add']
        [n1' := d1]
        [ny' := dy]
        [nz' := dz]
        [nyz' := dyz]
        [d1' := n1-cf0*d1]
        [dy' := ny-cf0*dy]
        [dz' := nz-cf0*dz]
        [dyz' := nyz-cf0*dyz]
    ####
    有一个操作数有限长并首先结束:
    [z == +oo]:
        [st4cf_add == (nz+nyz*y)/(dz+dyz*y)]
        辗转相除
        * 要么[y==+oo]
        * 要么yield from y
        * 要么 无限？这种情形是否可能？
    ####
    有一个输入是整数，是否特化实现？
    有一个输入是分数，是否特化实现？
    ####

]]

===
cf_divmod(lhs, rhs):
    q := cf_truediv(lhs, rhs)[0]
    r := lhs - cf_mul(q, rhs)
    -> (q,r)
===
cf_truediv(lhs, rhs):
    -> cf_mul(lhs, cf_inv(rhs))
===
cf_mul(lhs, rhs):
    有一个输入是整数，是否特化实现？
    有一个输入是分数，是否特化实现？
    ########
    [st4cf_mul =[def]= (n1+ny*y+nz*z+nyz*y*z)/(d1+dy*y+dz*z+dyz*y*z)]
    ########
    init:
    [cf0L+1/y := cf(lhs)]
    [cf0R+1/z := cf(rhs)]
    [st4cf_mul
    == cf(lhs) * cf(rhs) # <<== cf_mul def
    == cf0L*cf0R + cf0R/y + cf0L/z + 1/(y*z)
    == (1 + cf0L*y + cf0R*z + (cf0L*cf0R)*y*z)/(0 + 0*y + 0*z + y*z)
    ]

    ########st4cf_mul,st4cf_add are the same, diff only at init()!!!
    左展开更新公式:[y == K+1/g]:goto
    右展开更新公式:[z == K+1/s]:goto
===
pow__cf__int_ b x
===
cf_pow_(lhs, rhs):
    fail
    [rhs::int]:
        pow__cf__int_
    [rhs::Fraction]:
        ???
    [rhs :: cf_digits]:
        ???fail
    ########fail
cf_pow_ b x
    #require floor_pow_
    | [x <- int] = pow__cf__int_ b x
    # [not [x <- int]]
    # <==> [to_cf_digits(x) =!= [cf0R;1]]
    | b < 0 = _L
    | b == 0 = [0;]
    | b == 1 = [1;]
    # [b > 0][b =!= 1][to_cf_digits(x) =!= [cf0R;1]]
    | b < 1 = cf_pow_(1/b, cf_neg(x))
        !! [[b**x == y] -> [(1/b)**(-x) == y]]

    # [b > 1][to_cf_digits(x) =!= [cf0R;1]]
    | b > 1 = cf0 : ??? where
        cf0 = floor_pow_(b;x)
        #####
        !! [cf0 := floor_pow_(b;x)]
        [cf0 <= b**x < (cf0+1)]
        [0 <= b**x-cf0 < 1.0]
        [b**x == y]:
            !! [0.0 <= b**x-cf0 < 1.0]
            * [b**x-cf0 == 0.0]:
                [y == cf0]
                [y == cf([cf0;])]
            * [0.0 < b**x-cf0 < 1.0]
                [1/(b**x-cf0) > 1.0]
                ???fail
===
cf_log_(lhs, rhs):
cf_log_ b y
    #require floor_log_/floor_log_ex_
    | y <= 0 = _L
    | b <= 0 = _L
    | b == 1 = _L
    | y == 1 = [0;] # ===0

    # [b > 0][b =!= 1][y > 0][y =!= 1]
    | b < 1 = cf_log_(1/b, 1/y)
        !! [[b**x == y] <-> [(1/b)**x == 1/y]]
    # [b > 1][y > 0][y =!= 1]
    | y < 1 = -cf_log_(b, 1/y)
        !! [[b**x == y] <-> [b**(-x) == 1/y]]

    # [b > 1][y > 1]
    | otherwise = cf0 : if _b == 1 then [] else cf_log_(_b; b) where
        cf0 = floor_log_(b;y)
        _b = (y/b**cf0)
        #####
        !! [cf0 := floor_log_(b;y)]
        !! [b > 1]
        [b**cf0 <= y < b**(cf0+1)]
        [1 <= y/b**cf0 < b]
        [b**x == y]:
            [b**(x-cf0) == y/b**cf0]
            !! [1 <= y/b**cf0 < b]
            [1 <= b**(x-cf0) < b]
            !! [b > 1]
            [0 <= (x-cf0) < 1.0]
            !! [1 <= y/b**cf0 < b]
            * [(y/b**cf0) == 1]:
                [(x-cf0) == 0.0]
                [x == cf0] #continued_fraction is finite.
                [x == cf([cf0;])]
                [x == cf([cf0; +oo, ...])]
            * [1 < (y/b**cf0) < b]:
                [0 <= (x-cf0) < 1]
                [1/(x-cf0) > 1.0]
                [b == (y/b**cf0) ** (1/(x-cf0))]
                [(1/(x-cf0)) == log_((y/b**cf0); b)]
                [x == cf([cf0; *recur~cf_log_((y/b**cf0); b)])]
                    #NOTE:  [1 < y/b**cf0 < b]


===
cf_ge_(lhs, rhs):
    -> not cf_lt_(lhs, rhs)
===
cf_le_(lhs, rhs):
    -> not cf_gt_(lhs, rhs)
===
cf_gt_(lhs, rhs):
    -> cf_lt_(rhs, lhs)
===
cf_lt_(lhs, rhs):
    -> cf_cmp_(lhs, rhs) == -1
===
cf_cmp_(lhs, rhs):
    -> _cf_cmp_(False, lhs, rhs)
_cf_cmp_(_not, cf_digitsL, cf_digitsR):
    * [cf_digitsL == [] == cf_digitsR]:
        -> 0 # eq
    * [cf_digitsL == [] =!= cf_digitsR]:
        # [+oo > not +oo]
        -> -1 if _not else +1
    * [cf_digitsL =!= [] == cf_digitsR]:
        # [not +oo < +oo]
        -> +1 if _not else -1
    * [cf0L == cf0R]:
        -> _cf_cmp_(not _not, cf_digitsL[1:], cf_digitsR[1:])
    * [cf0L > cf0R]:
        -> _cf_cmp_(not _not, cf_digitsR, cf_digitsL)
    # [cf0L < cf0R]:
    * [cf0L + 1 == cf0R][cf_digitsL==[cf0L,1]][cf_digitsR==[cf0R]]:
        -> 0 # eq
    * otherwise:
        # [lhs < rhs]
        -> +1 if _not else -1
===
cf_ne_(lhs, rhs):
    -> not cf_eq_(lhs, rhs)
===
cf_eq_(lhs, rhs):
    -> cf_cmp_(lhs, rhs) == 0
===
]]]

from:
view ../../python3_src/seed/math/continued_fraction/continued_fraction_of_log_.py
def floor_log_ex_(base, y, /, *, _guess_first, with_remain):
[[[
[[base > 0][base=!=1][y > 0]]:
    [floor_log_(base;y) =[def]= floor(log_(base;y))]

    [floor_log_ex_(base;y) =[def]= (e, exact, y_remain) where [[e := floor_log_(base;y)][exact := [y_remain==1]][y_remain := y/base**e]]]

    [(e, exact, y_remain) := floor_log_ex_(base;y)]:
        !! [[e := floor_log_(base;y)][exact := [y_remain==1]][y_remain := y/base**e]]
        * [base > 1]:
            [base**e <= y < base**(e+1)]
            [1 <= y/base**e < base]
            [1 <= y_remain < base]
        * [base < 1]:
            [base**e >= y > base**(e+1)]
            [1 >= y_remain > base]
        [[1 <= y_remain < base]xor[1 >= y_remain > base]]

[[base > 1][y > 1]]:
    [floor_log_ex__gt1_(base;y) =[def]= floor_log_ex_(base;y)]

floor_log_(base;y) = floor_log_ex_(base;y)[0]


[[reshape_output:here
[[base > 0][base=!=1][y > 0]]:
    floor_log_ex_(base;y) = (e, exact, y_remain) where:
    [exact := exact_]
    [to_neg := [base < 1]xor[y < 1]]
    [e := if to_neg then -[not exact_]-e_ else e_]
    [y_remainM := if [y < 1] then 1/y_remain_ else y_remain_]
    [y_remain := y_remainM * if to_negand [not exact_] then base else 1]
    <<==:
    * [base < 1][y < 1]:
        (e_, exact_, y_remain_) = floor_log_ex__gt1_(1/base;1/y)
        [exact := exact_]
        [e := e_]
        [y_remain := 1/y_remain_]
    * [base < 1][y > 1]
        (e_, exact_, y_remain_) = floor_log_ex__gt1_(1/base;y)
        [exact := exact_]
        [e := -[not exact_]-e_]
        [y_remain := y_remain_*base**[not exact_]]
    * [base > 1][y < 1]:
        (e_, exact_, y_remain_) = floor_log_ex__gt1_(base;1/y)
        [exact := exact_]
        [e == -[not exact_]-e_]
        [y_remain == 1/y_remain_ *base**[not exact_]]
    * [base > 1][y > 1]:
        (e_, exact_, y_remain_) = floor_log_ex__gt1_(base;y)
        [exact := exact_]
        [e := e_]
        [y_remain := y_remain_]
]] <<==:
[[
floor_log_ex_(base;y)
    | not [[base > 0][base=!=1][y > 0]] = _L
    | [base < 1][y < 1] = (e, exact, y_remain) where
        (e_, exact_, y_remain_) = floor_log_ex__gt1_(1/base;1/y)
        [exact := exact_]
        [e := e_]
        [y_remain := 1/y_remain_]
        ######
        [[proof:
        [[e := floor_log_(base;y)][exact := [y_remain==1]][y_remain := y/base**e]]
        [[e_ := floor_log_(1/base;1/y)][exact_ := [y_remain_==1]][y_remain_ := (1/y)/(1/base)**e_]]
        [e_
        == floor_log_(1/base;1/y)
        == floor(log_(1/base;1/y))
        == floor(log_(base;y))
        == floor_log_(base;y)
        == e
        ]
        [e == e_]
        [y_remain_
        == (1/y)/(1/base)**e_
        == (1/y)/(1/base)**e
        == 1/(y/base**e)
        == 1/y_remain
        ]
        [y_remain == 1/y_remain_]
        [exact_
        == [y_remain_==1]
        == [1/y_remain==1]
        == [y_remain==1]
        == exact
        ]
        [exact == exact_]
        ]]
    | [base < 1][y > 1] = (e, exact, y_remain) where
        (e_, exact_, y_remain_) = floor_log_ex__gt1_(1/base;y)
        [exact := exact_]
        [e := -[not exact_]-e_]
        [y_remain := y_remain_*base**[not exact_]]
        ######
        [[proof:
        [[e := floor_log_(base;y)][exact := [y_remain==1]][y_remain := y/base**e]]
        [[e_ := floor_log_(1/base;y)][exact_ := [y_remain_==1]][y_remain_ := y/(1/base)**e_]]
        [e_
        == floor_log_(1/base;y)
        == floor(log_(1/base;y))
        == floor(-log_(base;y))
        == -[not exact_]-floor_log_(base;y)
        == -[not exact_]-e
        ]
        [e == -[not exact_]-e_]
        [y_remain_
        == y/(1/base)**e_
        == y/(1/base)**(-[not exact_]-e_)
        == y/base**([not exact_]+e_)
        == y/base**e /base**[not exact_]
        == y_remain /base**[not exact_]
        ]
        [y_remain == y_remain_*base**[not exact_]]
        * [y_remain_==1]:
            [exact_ == [y_remain_==1] == 1]
            [y_remain == y_remain_*base**[not exact_] == y_remain_ == 1]
        * [y_remain_=!=1]:
            [exact_ == [y_remain_==1] == 0]
            [y_remain == y_remain_*base**[not exact_] == y_remain_*base]
            !! [[1 <= y_remain < base]xor[1 >= y_remain > base]]
            [[1 <= y_remain_ < 1/base]xor[1 >= y_remain_ > 1/base]]
            !! [base < 1]
            [1 <= y_remain_ < 1/base]
            !! [y_remain_=!=1]
            [1 < y_remain_ < 1/base]
            [y_remain_*base > 1]
            [y_remain == y_remain_*base > 1]
        [[y_remain==1] == [y_remain_==1]]
        [exact == exact_]
        ]]
    | [base > 1][y < 1] = (e, exact, y_remain) where
        (e_, exact_, y_remain_) = floor_log_ex__gt1_(base;1/y)
        [exact := exact_]
        [e := -[not exact_]-e_]
        [y_remain := 1/y_remain_ *base**[not exact_]]
        ######
        [[proof:
        [[e := floor_log_(base;y)][exact := [y_remain==1]][y_remain := y/base**e]]
        [[e_ := floor_log_(base;1/y)][exact_ := [y_remain_==1]][y_remain_ := (1/y)/base**e_]]
        [e_
        == floor_log_(base;1/y)
        == floor(log_(base;1/y))
        == floor(-log_(base;y))
        == -[not exact_]-floor_log_(base;y)
        == -[not exact_]-e
        ]
        [e == -[not exact_]-e_]
        [y_remain_
        == (1/y)/base**e_
        == (1/y)/base**(-[not exact_]-e)
        == 1/(y/base**e) *base**[not exact_]
        == 1/y_remain *base**[not exact_]
        ]
        [y_remain == 1/y_remain_ *base**[not exact_]]
        * [y_remain_==1]:
            [exact_ == [y_remain_==1] == 1]
            [y_remain == 1/y_remain_*base**[not exact_] == 1/y_remain_ == 1]
        * [y_remain_=!=1]:
            [exact_ == [y_remain_==1] == 0]
            [y_remain == 1/y_remain_*base**[not exact_] == 1/y_remain_*base]
            !! [[1 <= y_remain < base]xor[1 >= y_remain > base]]
            [[1 <= y_remain_ < base]xor[1 >= y_remain_ > base]]
            !! [base > 1]
            [1 <= y_remain_ < base]
            !! [y_remain_=!=1]
            [1 < y_remain_ < base]
            [1/y_remain_*base > 1]
            [y_remain == 1/y_remain_*base > 1]
        [[y_remain==1] == [y_remain_==1]]
        [exact == exact_]

        ]]
    | [base > 1][y > 1] = floor_log_ex__gt1_(base;y)
]]


    #]]]


doctest____begin:here
>>> list(cf_neg([]))
Traceback (most recent call last):
    ...
seed.math.continued_fraction.continued_fraction_fold.ContinuedFractionError__inf__no_cf0
>>> list(cf_neg([0]))
[0]
>>> list(cf_neg([0, 1]))
[-1]
>>> list(cf_neg([0, 2]))
[-1, 1, 1]
>>> list(cf_neg([0, 1, 1]))
[-1, 2]
>>> list(cf_neg([0, 1, 2]))
[-1, 3]
>>> list(cf_neg([0, 2, 1]))
[-1, 1, 1, 1]
>>> list(cf_neg([0, 2, 2]))
[-1, 1, 1, 2]

>>> list(cf_neg([-1]))
[1]
>>> list(cf_neg([-1, 1, 1]))
[0, 2]
>>> list(cf_neg([-1, 2]))
[0, 1, 1]
>>> list(cf_neg([-1, 3]))
[0, 1, 2]
>>> list(cf_neg([-1, 1, 1, 1]))
[0, 2, 1]
>>> list(cf_neg([-1, 1, 1, 2]))
[0, 2, 2]



>>> list(cf_inv([]))
Traceback (most recent call last):
    ...
seed.math.continued_fraction.continued_fraction_fold.ContinuedFractionError__inf__no_cf0
>>> list(cf_inv([0]))
[]
>>> list(cf_inv([0, 1]))
[1]
>>> list(cf_inv([0, 2]))
[2]

>>> list(cf_inv([1]))
[0, 1]
>>> list(cf_inv([1, 1]))
[0, 1, 1]
>>> list(cf_inv([1, 2]))
[0, 1, 2]
>>> list(cf_inv([2]))
[0, 2]
>>> list(cf_inv([2, 1]))
[0, 2, 1]
>>> list(cf_inv([2, 2]))
[0, 2, 2]

>>> list(cf_inv([-1]))
[-1]
>>> list(cf_inv([-1, 1]))
Traceback (most recent call last):
    ...
seed.math.continued_fraction.continued_fraction_fold.ContinuedFractionError__inf__no_cf0
>>> list(cf_inv([-1, 2]))
[-2]
>>> list(cf_inv([-2]))
[-1, 1, 1]
>>> list(cf_inv([-2, 1]))
[-1]
>>> list(cf_inv([-2, 2]))
[-1, 2, 1]






>>> echo(cf_floor_([]))
Traceback (most recent call last):
    ...
seed.math.continued_fraction.continued_fraction_fold.ContinuedFractionError__inf__no_cf0
>>> echo(cf_floor_([0]))
0
>>> echo(cf_floor_([0, 1]))
1
>>> echo(cf_floor_([0, 2]))
0
>>> echo(cf_floor_([1]))
1
>>> echo(cf_floor_([1, 1]))
2
>>> echo(cf_floor_([1, 2]))
1
>>> echo(cf_floor_([-1]))
-1
>>> echo(cf_floor_([-1, 1]))
0
>>> echo(cf_floor_([-1, 2]))
-1






iter_cf_digitsO__if_determined_by_1_and_inf_
>>> list(cf_add([], []))
[]
>>> list(cf_add([], [0]))
[]

Traceback (most recent call last):
    ...
seed.math.continued_fraction.continued_fraction_fold.ContinuedFractionError__inf__no_cf0
>>> list(cf_add([0], []))
[]

Traceback (most recent call last):
    ...
seed.math.continued_fraction.continued_fraction_fold.ContinuedFractionError__inf__no_cf0
>>> list(cf_add([0], [0]))
[0]
>>> list(cf_add([0, 1], [0], _optimize_on_int=False))
[1]
>>> list(cf_add([0, 1], [0], _optimize_on_int=True))
[0, 1]
>>> list(cf_add([-2, 1,3,4,2], [0,4,2,2,1]))
[-2, 1, 89, 1, 1, 1, 1, 2]
>>> from seed.math.continued_fraction.continued_fraction_fold import iter_continued_fraction_digits5ND_, iter_approximate_fractions5continued_fraction_
>>> list(iter_approximate_fractions5continued_fraction_([-2, 1,3,4,2]))[-1]
Fraction(-47, 38)
>>> list(iter_approximate_fractions5continued_fraction_([0,4,2,2,1]))[-1]
Fraction(7, 31)
>>> list(iter_approximate_fractions5continued_fraction_([-2, 1, 89, 1, 1, 1, 1, 2]))[-1]
Fraction(-1191, 1178)
>>> Fraction(-47, 38) + Fraction(7, 31)
Fraction(-1191, 1178)







>>> list(cf_mul([], []))
[]
>>> list(cf_mul([], [0])) # ??? [+oo*0 == +oo]
[]
>>> list(cf_mul([0], []))
[]
>>> list(cf_mul([0, 1], [0]))
[0]
>>> list(cf_mul([0, 1], [1]))
[1]
>>> list(cf_mul([-2, 1,3,4,2], [0,4,2,2,1]))
[-1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 10]
>>> list(iter_approximate_fractions5continued_fraction_([-1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 10]))[-1]
Fraction(-329, 1178)
>>> Fraction(-47, 38) * Fraction(7, 31)
Fraction(-329, 1178)



>>> echo(cf_cmp_([], []))
0
>>> echo(cf_cmp_([], [0]))
1
>>> echo(cf_cmp_([0], []))
-1
>>> echo(cf_cmp_([0], [0]))
0
>>> echo(cf_cmp_([0], [1]))
-1
>>> echo(cf_cmp_([1], [0]))
1
>>> echo(cf_cmp_([0, 1], [1]))
0
>>> echo(cf_cmp_([1], [0, 1]))
0
>>> echo(cf_cmp_([1, 1], [1, 1]))
0
>>> echo(cf_cmp_([1, 1], [1, 2]))
1
>>> echo(cf_cmp_([1, 2], [1, 1]))
-1
>>> echo(cf_cmp_([1, 1, 1], [1, 1]))
-1
>>> echo(cf_cmp_([1, 1], [1, 1, 1]))
1
>>> echo(cf_cmp_([1, 1, 1], [1, 2]))
0
>>> echo(cf_cmp_([1, 2], [1, 1, 1]))
0
>>> echo(cf_cmp_([1, 1, 2], [1, 1]))
-1
>>> echo(cf_cmp_([1, 1], [1, 1, 2]))
1
>>> echo(cf_cmp_([1, 1, 2], [1, 1, 1]))
1
>>> echo(cf_cmp_([1, 1, 1], [1, 1, 2]))
-1
>>> echo(cf_cmp_([1, 1, 2], [1, 1, 1, 1]))
0
>>> echo(cf_cmp_([1, 1, 1, 1], [1, 1, 2]))
0
>>> echo(cf_cmp_([1, 1, 2], [1, 1, 1, 1, 2]))
1
>>> echo(cf_cmp_([1, 1, 1, 1, 2], [1, 1, 2]))
-1



>>> list(iter_approximate_fractions5continued_fraction_([4,2,3,5]))[-1]
Fraction(164, 37)
>>> list(iter_approximate_fractions5continued_fraction_([1,7,2,3]))[-1]
Fraction(59, 52)
>>> Fraction(164, 37) / Fraction(59, 52)
Fraction(8528, 2183)
>>> list(iter_approximate_fractions5continued_fraction_([3, 1, 9, 1, 2, 2, 1, 9, 2]))[-1]
Fraction(8528, 2183)
>>> divmod(Fraction(164, 37), Fraction(59, 52))
(3, Fraction(1979, 1924))
>>> list(iter_approximate_fractions5continued_fraction_([1, 34, 1, 54]))[-1]
Fraction(1979, 1924)
>>> list(cf_truediv([4,2,3,5], [1,7,2,3]))
[3, 1, 9, 1, 2, 2, 1, 9, 2]
>>> len(cf_divmod([4,2,3,5], [1,7,2,3]))
2
>>> echo(cf_divmod([4,2,3,5], [1,7,2,3])[0])
3
>>> list(cf_divmod([4,2,3,5], [1,7,2,3])[1])
[1, 34, 1, 54]


>>> echo(cf_lt_([1], [1]))
False
>>> echo(cf_lt_([1], [2]))
True
>>> echo(cf_lt_([2], [1]))
False

>>> echo(cf_gt_([1], [1]))
False
>>> echo(cf_gt_([1], [2]))
False
>>> echo(cf_gt_([2], [1]))
True

>>> echo(cf_le_([1], [1]))
True
>>> echo(cf_le_([1], [2]))
True
>>> echo(cf_le_([2], [1]))
False

>>> echo(cf_ge_([1], [1]))
True
>>> echo(cf_ge_([1], [2]))
False
>>> echo(cf_ge_([2], [1]))
True

>>> echo(cf_eq_([1], [1]))
True
>>> echo(cf_eq_([1], [2]))
False
>>> echo(cf_eq_([2], [1]))
False

>>> echo(cf_ne_([1], [1]))
False
>>> echo(cf_ne_([1], [2]))
True
>>> echo(cf_ne_([2], [1]))
True


>>> 0**0 #ZeroDivisionError
1
>>> 0**-2 #ZeroDivisionError
Traceback (most recent call last):
    ...
ZeroDivisionError: 0.0 cannot be raised to a negative power

doctest____end:here

#]]]'''
__all__ = r'''
ContinuedFractionState__1var
ContinuedFractionState__2vars
    cf_add
    cf_mul
    NaN

cf_neg
    cf_inv

cf_add
    cf_sub

MutableLazySeq
ImmutableLazySeq
    to_MutableLazySeq
    to_ImmutableLazySeq
CachedIterator

cf_is_int_
cf_floor_
cf_ceil_
cf_floor_ex_
    icf_floor_ex_
cf_mul
    cf_truediv
        cf_divmod

to_PeekableIterator
cf_cmp_
    cf_lt_
        cf_ge_
        cf_le_
        cf_gt_
    cf_eq_
        cf_ne_

ContinuedFraction

'''.split()#'''
__all__
from fractions import Fraction
from itertools import chain, islice, count as _count_
import itertools # count


from seed.tiny import check_type_is
from seed.tiny_.check import check_uint, check_int_ge
from seed.tiny import echo, null_iter, is_iterable
from seed.tiny import print_err, mk_fprint, mk_assert_eq_f, expectError
from seed.math.PowSeq import PowSeq
from seed.math.divs import is_even
from seed.iters.PeekableIterator import PeekableIterator
    #view ../../python3_src/seed/iters/PeekableIterator.py
from seed.math.continued_fraction.continued_fraction_fold import ContinuedFractionError__inf__no_cf0
#from seed.math.continued_fraction.continued_fraction_fold import ContinuedFractionFoldState, continued_fraction_fold_state0
from seed.math.continued_fraction.continued_fraction_fold import iter_continued_fraction_digits5ND_, iter_approximate_fractions5continued_fraction_

from seed.helper.repr_input import repr_helper
from seed.types.NamedReadOnlyProperty import NamedReadOnlyProperty, set_NamedReadOnlyProperty4cls_, set_NamedReadOnlyProperty4sf_
from seed.types.exc.UnsupportedOperation import Attr4UnsupportedOperation

NaN = object()
class ContinuedFractionState__2vars:
    '[st_2vars=st4cf_add=st4cf_mul =[def]= (n1+ny*y+nz*z+nyz*y*z)/(d1+dy*y+dz*z+dyz*y*z)]'
        #N:numerator
        #D:denominator
    _attr_nms = r'''
    n1 ny nz nyz
    d1 dy dz dyz
    '''.split()#'''
    def get_args(sf, /):
        return tuple(getattr(sf, nm) for nm in __class__._attr_nms)
    def __repr__(sf, /):
        args = sf.get_args()
        return repr_helper(sf, *args)
    def __init__(sf, n1, ny, nz, nyz, d1, dy, dz, dyz, /):
        ########init sf:
        set_NamedReadOnlyProperty4sf_(sf, __class__._attr_nms, locals())
    def step_cf_digitL_(sf, Ky, /):
        (n1, ny, nz, nyz, d1, dy, dz, dyz) = sf.get_args()
        #左展开更新公式
        n1_ = ny
        ny_ = (n1+ny*Ky)
        nz_ = nyz
        nyz_ = (nz+nyz*Ky)
        d1_ = dy
        dy_ = (d1+dy*Ky)
        dz_ = dyz
        dyz_ = (dz+dyz*Ky)
        return __class__(n1_, ny_, nz_, nyz_, d1_, dy_, dz_, dyz_)
    def step_cf_digitR_(sf, Kz, /):
        (n1, ny, nz, nyz, d1, dy, dz, dyz) = sf.get_args()
        #右展开更新公式
        n1_ = nz
        ny_ = nyz
        nz_ = (n1+nz*Kz)
        nyz_ = (ny+nyz*Kz)
        d1_ = dz
        dy_ = dyz
        dz_ = (d1+dz*Kz)
        dyz_ = (dy+dyz*Kz)
        return __class__(n1_, ny_, nz_, nyz_, d1_, dy_, dz_, dyz_)
    def __():
        from seed.math.continued_fraction.continued_fraction_fold import ContinuedFractionFoldState, continued_fraction_fold_state0
        #ContinuedFractionFoldState: def _check_args(prevN, prevD, currN, currD, /):
        #   too strict to use here
        # using ContinuedFractionState__1var instead
        @classmethod
        def step_cf_digitO__1var_(cls, st:ContinuedFractionFoldState, cf0, /):
            # [z==+oo]
            #ContinuedFractionFoldState:def __new__(cls, prevN, prevD, currN, currD, /, *, validate_completely_by_reproduct=False):
            #bug:(nz, nyz, dz, dyz) = st.get_args()
            (nz, dz, nyz, dyz) = st.get_args()
            #向下取整辗转更新公式
            nz_ = dz
            nyz_ = dyz
            dz_ = nz-cf0*dz
            dyz_ = nyz-cf0*dyz
            #bug:return type(st)(nz_, nyz_, dz_, dyz_)
            return type(st)(nz_, dz_, nyz_, dyz_)
        def to_ContinuedFractionFoldState__if_rhs_tail_is_empty(sf, /):
            #bug:st = ContinuedFractionFoldState(sf.nz, sf.nyz, sf.dz, sf.dyz)
            st = ContinuedFractionFoldState(sf.nz, sf.dz, sf.nyz, sf.dyz)
            return st
    def to_ContinuedFractionState__1var__if_rhs_tail_is_empty(sf, /):
        st = ContinuedFractionState__1var(sf.nz, sf.nyz, sf.dz, sf.dyz)
        return st
    def step_cf_digitO_(sf, cf0, /):
        (n1, ny, nz, nyz, d1, dy, dz, dyz) = sf.get_args()
        #向下取整辗转更新公式
        n1_ = d1
        ny_ = dy
        nz_ = dz
        nyz_ = dyz
        d1_ = n1-cf0*d1
        dy_ = ny-cf0*dy
        dz_ = nz-cf0*dz
        dyz_ = nyz-cf0*dyz
        return __class__(n1_, ny_, nz_, nyz_, d1_, dy_, dz_, dyz_)
    def swapLR(sf, /):
        (n1, ny, nz, nyz, d1, dy, dz, dyz) = sf.get_args()
        ny, nz = nz, ny
        dy, dz = dz, dy
        return __class__(n1, ny, nz, nyz, d1, dy, dz, dyz)
    def eval_at_1_or_inf_(sf, y_is_1_vs_oo:bool, z_is_1_vs_oo:bool, /, *, to_floor:bool, _ND=False):
        if to_floor and _ND:raise TypeError
        #see:flr
        if y_is_1_vs_oo:
            # [y==+oo]
            if z_is_1_vs_oo:
                # [z==+oo]
                N = sf.nyz
                D = sf.dyz
            else:
                # [z==1.0]
                N = sf.ny + sf.nyz
                D = sf.dy + sf.dyz
        else:
            # [y==1.0]
            if z_is_1_vs_oo:
                # [z==+oo]
                N = sf.nz + sf.nyz
                D = sf.dz + sf.dyz
            else:
                # [z==1.0]
                N = sf.n1 + sf.ny + sf.nz + sf.nyz
                D = sf.d1 + sf.dy + sf.dz + sf.dyz
        if to_floor:
            if D == 0:
                return NaN
            return N//D
        return (N, D) if _ND else Fraction(N, D)

    def iter_cf_digitsO__if_determined_by_1_and_inf_(sf, y, z, /):
        'y/tail-cf_digitsL -> z/tail-cf_digitsR -> cf_digitsO'
        y = to_PeekableIterator(y)
        z = to_PeekableIterator(z)
        while not z.is_empty():
            if y.is_empty():
                sf = sf.swapLR()
                y, z = z, y
                continue


            if sf.dyz == 0:
                to_step_y = True
                to_step_z = True
                    #init
            else:
                _1_1 = sf.eval_at_1_or_inf_(False, False, to_floor=True)
                _1_oo = sf.eval_at_1_or_inf_(False, True, to_floor=True)
                _oo_1 = sf.eval_at_1_or_inf_(True, False, to_floor=True)
                _oo_oo = sf.eval_at_1_or_inf_(True, True, to_floor=True)
                #see:flr
                # 展开y if:
                #     * [flr(--) =!= flr(+-)]
                #     * [flr(-+) =!= flr(++)]
                # 展开z if:
                #     * [flr(--) =!= flr(-+)]
                #     * [flr(+-) =!= flr(++)]
                # 同时展开y,z
                to_step_y = not (_1_1 == _oo_1 and _1_oo == _oo_oo)
                to_step_z = not (_1_1 == _1_oo and _oo_1 == _oo_oo)
            to_step_y
            to_step_z


            if to_step_y:
                Ky = y.read1()
                sf = sf.step_cf_digitL_(Ky)
            #
            if to_step_z:
                Kz = z.read1()
                sf = sf.step_cf_digitR_(Kz)

            if not (to_step_y or to_step_z):
                cf0 = _1_oo
                yield cf0
                sf = sf.step_cf_digitO_(cf0)
        #end-while
        assert z.is_empty()
        # [z==+oo]
        #ContinuedFractionState__1var
        st = sf.to_ContinuedFractionState__1var__if_rhs_tail_is_empty()
        yield from st.iter_cf_digitsO__if_determined_by_1_and_inf_(y)
        return
        st = sf.to_ContinuedFractionFoldState__if_rhs_tail_is_empty()
        1;  del sf
        while not y.is_empty():
            if st.currD == 0:
                to_step_y = True
                all_int_ok = True
                    #init
            else:
                all_int_ok = False

                _1_oo = st.step_(1).get_curr_floor()
                _oo_oo = st.get_curr_floor()
                #print_err(_1_oo)
                #print_err(_oo_oo)
                #print_err(st)
                to_step_y = not (_1_oo == _oo_oo)
                #print_err(_1_oo, _oo_oo)
            to_step_y, all_int_ok


            if to_step_y:
                Ky = y.read1()
                st = st.step_(Ky, all_int_ok=all_int_ok)
            else:
                cf0 = _1_oo
                yield cf0
                #print_err(cf0)
                #print_err(st)
                st = __class__.step_cf_digitO__1var_(st, cf0)
                #print_err(st)
                #raise 000
        #end-while
        assert y.is_empty()
        # [z==+oo]
        # [y==+oo]
        (N,D) = st.get_currND()
        if not D == 0:
            yield from iter_continued_fraction_digits5ND_(N, D)
        else:
            # [+oo]?
            pass
        return
if 1:
    set_NamedReadOnlyProperty4cls_(ContinuedFractionState__2vars, ContinuedFractionState__2vars._attr_nms)
#end-class ContinuedFractionState__2vars:









class ContinuedFractionState__1var:
    '[st_1var =[def]= (nz+nyz*y)/(dz+dyz*y)]'
    '~~ ContinuedFractionFoldState without gcd???'
    #
    # [z==+oo]
    _attr_nms = r'''
    nz nyz
    dz dyz
    '''.split()#'''
    def get_args(sf, /):
        return tuple(getattr(sf, nm) for nm in __class__._attr_nms)
    def __repr__(sf, /):
        args = sf.get_args()
        return repr_helper(sf, *args)

    def __init__(sf, nz, nyz, dz, dyz, /):
        ########init sf:
        set_NamedReadOnlyProperty4sf_(sf, __class__._attr_nms, locals())
    def step_cf_digitL_(sf, Ky, /):
        (nz, nyz, dz, dyz) = sf.get_args()
        #左展开更新公式
        nz_ = nyz
        nyz_ = (nz+nyz*Ky)
        dz_ = dyz
        dyz_ = (dz+dyz*Ky)
        return __class__(nz_, nyz_, dz_, dyz_)
    def step_cf_digitO_(sf, cf0, /):
        (nz, nyz, dz, dyz) = sf.get_args()
        #向下取整辗转更新公式
        nz_ = dz
        nyz_ = dyz
        dz_ = nz-cf0*dz
        dyz_ = nyz-cf0*dyz
        return __class__(nz_, nyz_, dz_, dyz_)

    def eval_at_1_or_inf_(sf, y_is_1_vs_oo:bool, /, *, to_floor:bool, _ND=False):
        #see:flr
        if to_floor and _ND:raise TypeError
        # [z==+oo]
        if y_is_1_vs_oo:
            # [y==+oo]
            # [z==+oo]
            N = sf.nyz
            D = sf.dyz
        else:
            # [y==1.0]
            # [z==+oo]
            N = sf.nz + sf.nyz
            D = sf.dz + sf.dyz
        if to_floor:
            if D == 0:
                return NaN
            return N//D
        return (N, D) if _ND else Fraction(N, D)
    def iter_cf_digitsO__if_determined_by_1_and_inf_(sf, y, /):
        'y/tail-cf_digitsL -> cf_digitsO'
        # [z==+oo]
        y = to_PeekableIterator(y)
        while not y.is_empty():
            if sf.dyz == 0:
                to_step_y = True
                    #init
            else:
                _1_oo = sf.eval_at_1_or_inf_(False, to_floor=True)
                _oo_oo = sf.eval_at_1_or_inf_(True, to_floor=True)
                to_step_y = not (_1_oo == _oo_oo)
            to_step_y


            if to_step_y:
                Ky = y.read1()
                sf = sf.step_cf_digitL_(Ky)
            else:
                cf0 = _1_oo
                yield cf0
                sf = sf.step_cf_digitO_(cf0)
        #end-while
        assert y.is_empty()
        # [z==+oo]
        # [y==+oo]
        (N,D) = _oo_oo = sf.eval_at_1_or_inf_(True, to_floor=False, _ND=True)
        if not D == 0:
            yield from iter_continued_fraction_digits5ND_(N, D)
        else:
            # [+oo]?
            pass
        return



r"""[[[
class ContinuedFractionState__0var:
    '[st_0var =[def]= nyz/dyz]'
    '~~ Fraction without gcd???'


class ZZZ:
    _attr_nms = r'''
    aaa
    '''.split()#'''

    def get_args(sf, /):
        return tuple(getattr(sf, nm) for nm in __class__._attr_nms)
    def __repr__(sf, /):
        args = sf.get_args()
        return repr_helper(sf, *args)
    def __init__(sf, aaa, /):
        ########init sf:
        set_NamedReadOnlyProperty4sf_(sf, __class__._attr_nms, locals())
if 1:
    set_NamedReadOnlyProperty4cls_(ZZZ, ZZZ._attr_nms)
#end-class ZZZ:



#]]]"""#"""


def cf_inv(cf_digits, /):
    cf_digits = iter(cf_digits)
    for cf0 in cf_digits:
        break
    else:
        raise ContinuedFractionError__inf__no_cf0
    _1_cf_digits = cf_digits
    1;  del cf_digits
    if cf0 == 0:
        return _1_cf_digits # may be +oo
    elif cf0 > 0:
        return chain([0,cf0], _1_cf_digits)
    else:
        return cf_neg(cf_inv(cf_neg(chain([cf0], _1_cf_digits))))

def cf_neg(cf_digits, /):
    cf_digits = iter(cf_digits)
    for cf0 in cf_digits:
        break
    else:
        raise ContinuedFractionError__inf__no_cf0
    _1_cf_digits = cf_digits
    1;  del cf_digits
    cf0, _1_cf_digits

    for cf1 in _1_cf_digits:
        break
    else:
        # cf_neg__case1
        # <==> [cf_digits==[cf0;]]
        return iter([-cf0])
    _2_cf_digits = _1_cf_digits
    1;  del _1_cf_digits
    cf0, cf1, _2_cf_digits

    if cf1 >= 2:
        # cf_neg__case4
        return chain([-1-cf0, 1, cf1-1], _2_cf_digits)
    assert cf1 == 1

    for cf2 in _2_cf_digits:
        break
    else:
        # cf_neg__case2
        # <==> [cf_digits==[cf0;1]]
        return iter([-1-cf0])
    _3_cf_digits = _2_cf_digits
    1;  del _2_cf_digits
    cf0, cf1, cf2, _3_cf_digits

    if 1:
        # cf_neg__case3
        # <==> [cf_digits==[cf0;1,cf2,...]]
        return chain([-1-cf0, cf2+1], _3_cf_digits)

def cf_sub(lhs, rhs, /, *, _optimize_on_int=None):
    return cf_add(lhs, cf_neg(rhs), _optimize_on_int=_optimize_on_int)
def _cf_add__optimize_on_int(lhs, rhs, /):
    j2xhs = [lhs, rhs]
    #bug:for lhs, rhs in [(rhs, lhs), (lhs, rhs)]:
    #   cannot restore original value: lhs/rhs
    for j4rhs in (0, 1):
        j4lhs = 1-j4rhs
        lhs = j2xhs[j4lhs]
        rhs = j2xhs[j4rhs]
        try:
            (lhs, (is_int4lhs, floor4lhs)) = icf_floor_ex_(lhs)
        except ContinuedFractionError__inf__no_cf0:
            return (done:=True, result:=null_iter)
        j2xhs[j4lhs] = lhs
            #restore original value: lhs/rhs
        if not is_int4lhs:
            continue
        i8lhs = floor4lhs
        rhs = iter(rhs)
        for cf0 in rhs:
            break
        else:
            return (done:=True, result:=null_iter)
            raise ContinuedFractionError__inf__no_cf0
        _1_rhs = rhs; rhs = None
        i8lhs, cf0, _1_rhs
        result = chain([i8lhs+cf0], _1_rhs)
        return (done:=True, result)
    [lhs, rhs] = j2xhs
        #restore original value: lhs/rhs
    return (done:=False, j2xhs)
#_optimize_on_int4cf_add = True
_optimize_on_int4cf_add = False
def cf_add(lhs, rhs, /, *, _optimize_on_int=None):
    'st4cf_add := (0 + 1*y + 1*z + (cf0L+cf0R)*y*z)/(0 + 0*y + 0*z + y*z)'
    ######################
    if _optimize_on_int is None:
        _optimize_on_int = _optimize_on_int4cf_add

    if _optimize_on_int:
        (done, x) = _cf_add__optimize_on_int(lhs, rhs)
        if done:
            return x
        [lhs, rhs] = x
    ######################
    #st4cf_add = ContinuedFractionState__2vars(0,1,1,cf0L+cf0R,  0,0,0,1)
    st4cf_add = ContinuedFractionState__2vars(0,1,1,0,  1,0,0,0)
    return st4cf_add.iter_cf_digitsO__if_determined_by_1_and_inf_(lhs, rhs)
def cf_is_int_(cf_digits, /):
    (is_int, cf0_x) = cf_floor_ex_(cf_digits)
    return is_int
def cf_floor_(cf_digits, /):
    (is_int, cf0_x) = cf_floor_ex_(cf_digits)
    return cf0_x
def cf_ceil_(cf_digits, /):
    (is_int, cf0_x) = cf_floor_ex_(cf_digits)
    return cf0_x if is_int else cf0_x+1
def icf_floor_ex_(cf_digits, /):
    cf_digits = CachedIterator(cf_digits)
    (is_int, cf0_x) = cf_floor_ex_(cf_digits)
    cf_digits = cf_digits.chain_detach()
    return (cf_digits, (is_int, cf0_x))
def cf_floor_ex_(cf_digits, /):
    cf_digits = iter(cf_digits)
    for cf0 in cf_digits:
        break
    else:
        raise ContinuedFractionError__inf__no_cf0
    _1_cf_digits = cf_digits
    1;  del cf_digits
    cf0, _1_cf_digits
    #bug:return cf0

    for cf1 in _1_cf_digits:
        break
    else:
        # <==> [cf_digits==[cf0;]]
        is_int = True
        return is_int, cf0
    _2_cf_digits = _1_cf_digits
    1;  del _1_cf_digits
    cf0, cf1, _2_cf_digits

    if cf1 >= 2:
        is_int = False
        return is_int, cf0
    assert cf1 == 1

    for cf2 in _2_cf_digits:
        break
    else:
        # <==> [cf_digits==[cf0;1]]
        is_int = True
        return is_int, 1+cf0
    _3_cf_digits = _2_cf_digits
    1;  del _2_cf_digits
    cf0, cf1, cf2, _3_cf_digits

    is_int = False
    return is_int, cf0


class _BaseLazySeq:
    def __init__(sf, it, /):
        sf._ls = []
        sf._it = iter(it)
    def __getitem__(sf, i, /):
        check_uint(i)
        ls = sf._ls
        if not i < len(ls):
            ls.extend(islice(sf._it, i+1-len(ls)))
        return ls[i]
        if not i < len(ls):
            raise IndexError(i)
        return ls[i]
    def __iter__(sf, /):
        try:
            for i in itertools.count(0):
                yield sf[i]
        except IndexError:
            pass
        return
class ImmutableLazySeq(_BaseLazySeq):
    pass
class MutableLazySeq(_BaseLazySeq):
    def chain_detach(sf, /):
        'like detach, but chain the output'
        ls, it = sf.detach()
        it = chain(ls, it) if ls else it

        return it

    def detach(sf, /):
        'remove and return (underlying_cache_list, underlying_iterator)'
        ls = sf._ls
        it = sf._it
        sf._ls = []
        sf._it = null_iter
        return ls, it
def to_MutableLazySeq(it, /):
    if isinstance(it, MutableLazySeq):
        seq = it
    else:
        seq = MutableLazySeq(it)
    return it
def to_ImmutableLazySeq(it, /):
    '-> tuple/ImmutableLazySeq'
    if (type(it) is tuple or isinstance(it, ImmutableLazySeq)):
        seq = it
    else:
        seq = ImmutableLazySeq(it)
    return seq


class CachedIterator:
    def __init__(sf, it, /):
        sf._ls = []
        sf._it = iter(it)
    def __iter__(sf, /):
        return sf
    def __next__(sf, /):
        x = next(sf._it)
        sf._ls.append(x)
        return x
    def chain_detach(sf, /):
        'like detach, but chain the output'
        ls, it = sf.detach()
        it = chain(ls, it) if ls else it

        return it

    def detach(sf, /):
        'remove and return (underlying_cache_list, underlying_iterator)'
        ls = sf._ls
        it = sf._it
        sf._ls = []
        sf._it = null_iter
        return ls, it


def cf_divmod(lhs, rhs, /):
    #bug:without CachedIterator/MutableLazySeq
    if 1:
        lhs = CachedIterator(lhs)
        rhs = CachedIterator(rhs)
    elif 1:
        lhs = MutableLazySeq(lhs)
        rhs = MutableLazySeq(rhs)
    elif 0:
        #bug:
        #why not to_MutableLazySeq? .chain_detach() below broken globally
        lhs = to_MutableLazySeq(lhs)
        rhs = to_MutableLazySeq(rhs)
    elif 0:
        #why not to_ImmutableLazySeq? waste memory...
        lhs = to_ImmutableLazySeq(lhs)
        rhs = to_ImmutableLazySeq(rhs)
    else:
        raise 000
    iq = cf_floor_(cf_truediv(lhs, rhs))
    cf8q = [iq]
    lhs = lhs.chain_detach()
    rhs = rhs.chain_detach()
    r = cf_sub(lhs, cf_mul(cf8q, rhs))
    return (iq,r)
def cf_truediv(lhs, rhs, /):
    return cf_mul(lhs, cf_inv(rhs))
def cf_mul(lhs, rhs, /):
    'st4cf_mul := (1 + cf0L*y + cf0R*z + (cf0L*cf0R)*y*z)/(0 + 0*y + 0*z + y*z)'
    #st4cf_mul = ContinuedFractionState__2vars(1,cf0L,cf0R,cf0L*cf0R,  0,0,0,1)
    st4cf_mul = ContinuedFractionState__2vars(0,0,0,1,  1,0,0,0)
    return st4cf_mul.iter_cf_digitsO__if_determined_by_1_and_inf_(lhs, rhs)



def to_PeekableIterator(it, /):
    if not isinstance(it, PeekableIterator):
        it = PeekableIterator(it)
    return it
def cf_ge_(lhs, rhs, /):
    return not cf_lt_(lhs, rhs)
def cf_le_(lhs, rhs, /):
    return not cf_gt_(lhs, rhs)
def cf_gt_(lhs, rhs, /):
    return cf_lt_(rhs, lhs)
def cf_lt_(lhs, rhs, /):
    return cf_cmp_(lhs, rhs) == -1
#def _cf_lt_(_not, cf_digitsL, cf_digitsR, /):
def _result_with_not_(_not, r, /):
    return -r if _not else r
def cf_cmp_(lhs, rhs, /):
    '-> [-1,0,+1]'
    cf_digitsL = to_PeekableIterator(lhs)
    cf_digitsR = to_PeekableIterator(rhs)
    return _cf_cmp_(False, cf_digitsL, cf_digitsR)
def _cf_cmp_(_not, cf_digitsL, cf_digitsR, /):
    while 1:
        nullL = cf_digitsL.is_empty()
        nullR = cf_digitsR.is_empty()
        if nullL and nullR:
            return 0 # eq
        elif nullL and not nullR:
            # [+oo > not +oo]
            return _result_with_not_(_not, +1)
        elif not nullL and nullR:
            # [not +oo < +oo]
            return _result_with_not_(_not, -1)
        cf0L = cf_digitsL.peek1()
        cf0R = cf_digitsR.peek1()
        if cf0L == cf0R:
            cf_digitsL.read1()
            cf_digitsR.read1()
            _1_cf_digitsL = cf_digitsL
            _1_cf_digitsR = cf_digitsR
            #return _cf_cmp_(not _not, _1_cf_digitsL, _1_cf_digitsR)
            _not = not _not
            cf_digitsL = _1_cf_digitsL
            cf_digitsR = _1_cf_digitsR
            continue
        elif cf0L > cf0R:
            #return _cf_cmp_(not _not, cf_digitsR, cf_digitsL)
            _not = not _not
            cf_digitsL, cf_digitsR = cf_digitsR, cf_digitsL
            continue

        # [cf0L < cf0R]
        elif cf0L + 1 == cf0R and cf_digitsR.peek_le(2) == (cf0R,) and cf_digitsL.peek_le(3) == (cf0L,1):
            return 0 # eq
        else:
            # [lhs < rhs]
            return _result_with_not_(_not, -1)
def cf_ne_(lhs, rhs, /):
    return not cf_eq_(lhs, rhs)
def cf_eq_(lhs, rhs, /):
    return cf_cmp_(lhs, rhs) == 0

r'''[[[
TODO:
def pow__cf__int_(cf_digits, e, /):
    bin
cf_log_(lhs, rhs, /):
#]]]'''#'''


#class ContinuedFraction(ImmutableLazySeq):
class ContinuedFraction:
    _attr_nms = r'''
    _cf_digits
    '''.split()#'''
    __bool__ = Attr4UnsupportedOperation()
    __len__ = Attr4UnsupportedOperation()
    __contains__ = Attr4UnsupportedOperation()

    if 0:
        def get_args(sf, /):
            return tuple(getattr(sf, nm) for nm in __class__._attr_nms)
        def __repr__(sf, /):
            args = sf.get_args()
            return repr_helper(sf, *args)
    def __new__(cls, cf_digits__or__int__or__Fraction, /):
        if is_iterable(cf_digits__or__int__or__Fraction):
            cf_digits = cf_digits__or__int__or__Fraction
        elif type(cf_digits__or__int__or__Fraction) is int:
            cf0 = cf_digits__or__int__or__Fraction
            cf_digits = [cf0]
        else:
            rational = cf_digits__or__int__or__Fraction
            fr = Fraction(rational)
            cf_digits = iter_continued_fraction_digits5ND_(*fr.as_integer_ratio())
        cf_digits

        if isinstance(cf_digits, __class__):
            sf = cf_digits
        else:
            sf = super(__class__, cls).__new__(cls)
            sf._init_(cf_digits)
        return sf
    def _init_(sf, _cf_digits, /):
        _cf_digits = to_ImmutableLazySeq(_cf_digits)
        ########init sf:
        set_NamedReadOnlyProperty4sf_(sf, __class__._attr_nms, locals())
    def __getitem__(sf, i, /):
        check_uint(i)
        u = sf._cf_digits[i]
        if u == 0:
            cf0 = u
            check_type_is(int, cf0)
        else:
            check_int_ge(1, u)
        return u
    def __iter__(sf, /):
        it = iter(sf._cf_digits)
        for cf0 in it:
            break
        else:
            raise ContinuedFractionError__inf__no_cf0
        check_type_is(int, cf0)
        yield cf0
        for u in it:
            check_int_ge(1, u)
            yield u

    def is_int(sf, /):
        return cf_is_int_(sf)
    def __floor__(sf, /):
        return cf_floor_(sf)
    def __ceil__(sf, /):
        return cf_ceil_(sf)
    def _cmp_(sf, ot, /):
        ot = __class__(ot)
        return cf_cmp_(sf, ot)
    def __eq__(sf, ot, /):
        return sf._cmp_(ot) == 0
    def __lt__(sf, ot, /):
        return sf._cmp_(ot) == -1
    def __gt__(sf, ot, /):
        return sf._cmp_(ot) == +1

    def __ne__(sf, ot, /):
        return not sf == ot
    def __le__(sf, ot, /):
        return not sf > ot
    def __ge__(sf, ot, /):
        return not sf < ot

    def __abs__(sf, /):
        if sf < 0:
            return -sf
        return sf
    def __pos__(sf, /):
        return sf
    def __neg__(sf, /):
        return __class__(cf_neg(sf))
    def inv_(sf, /):
        return __class__(cf_inv(sf))
    def __add__(sf, ot, /):
        ot = __class__(ot)
        if ot == 0:
            return sf
        if sf == 0:
            return ot
        return __class__(cf_add(sf, ot))
    def __mul__(sf, ot, /):
        ot = __class__(ot)
        if ot == 1:
            return sf
        if sf == 1:
            return ot
        if sf == 0:
            return sf
        if ot == 0:
            return ot
        if ot == -1:
            return -sf
        if sf == -1:
            return -ot
        return __class__(cf_mul(sf, ot))

    def __sub__(sf, ot, /):
        if sf is ot:
            return cf_0
        ot = __class__(ot)
        return sf + (-ot)
    def __truediv__(sf, ot, /):
        if sf is ot:
            return cf_1
        ot = __class__(ot)
        return sf * ot.inv_()

    def __divmod__(sf, ot, /):
        if sf is ot:
            return (cf_1, cf_0)
        ot = __class__(ot)
        iq, r = cf_divmod(sf, ot)
        return iq, __class__(r)
    def __mod__(sf, ot, /):
        #ot = __class__(ot)
        iq, r = divmod(sf, ot)
        return r
    def __floordiv__(sf, ot, /):
        #ot = __class__(ot)
        iq, r = divmod(sf, ot)
        return iq
    def __pow__(sf, e, /):
        check_type_is(int, e)
        #return __class__(pow__cf__int_(sf, e))
        if e == 2:
            return sf*sf
        if sf == 1:
            return sf
        if sf == -1:
            return -sf if is_even(e) else sf
        if sf == 0:
            if e == 0:
                return cf_1
                raise ZeroDivisionError('0**0')
            if e < 0:
                raise ZeroDivisionError('0**0')
            return sf

        if e < 5:
            if e < 0:
                return (sf**(-e)).inv_()
            elif e < 2:
                if e == 0:
                    return cf_1
                elif e == 1:
                    return sf
                else:
                    raise 000
            elif e == 2:
                return sf*sf
            elif e == 3:
                return sf*sf*sf
            elif e == 4:
                sf_2 = (sf*sf)
                return sf_2*sf_2
            else:
                raise 000
        pows = PowSeq(sf, None, cf_1)
        return pows.get_pow_(e)

if 1:
    set_NamedReadOnlyProperty4cls_(ContinuedFraction, ContinuedFraction._attr_nms)
#end-class ContinuedFraction:

cf_0 = ContinuedFraction(0)
cf_1 = ContinuedFraction(1)
cf_neg1 = ContinuedFraction(-1)

if __name__ == "__main__":
    pass
__all__


from seed.math.continued_fraction.continued_fraction_ops import ContinuedFraction
from seed.math.continued_fraction.continued_fraction_ops import *
