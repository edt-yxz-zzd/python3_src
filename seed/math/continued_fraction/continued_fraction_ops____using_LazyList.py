#__all__:goto
r'''[[[
e ../../python3_src/seed/math/continued_fraction/continued_fraction_ops____using_LazyList.py
see:
    view ../../python3_src/seed/types/LazyList.py
    view ../../python3_src/seed/math/continued_fraction/continued_fraction_ops.py
    view ../../python3_src/seed/math/continued_fraction/continued_fraction_ops____using_LazyList.py
    view ../../python3_src/seed/math/binary_float/binary_float_ops____using_LazyList.py
    view ../../python3_src/seed/math/continued_fraction/iter_continued_fraction_of_log__truncated_.py
        from seed.math.continued_fraction.iter_continued_fraction_of_log__truncated_ import cf_log_, cf_ln_




[[
!cp ../../python3_src/seed/math/continued_fraction/continued_fraction_ops.py ../../python3_src/seed/math/continued_fraction/continued_fraction_ops____using_LazyList.py
.+1,$s/\<continued_fraction_ops\>/continued_fraction_ops____using_LazyList/g

e ../../python3_src/seed/math/continued_fraction/continued_fraction_ops____using_LazyList.py
]]

doctest____begin:goto
doctest____end:goto


seed.math.continued_fraction.continued_fraction_ops____using_LazyList
py -m nn_ns.app.debug_cmd   seed.math.continued_fraction.continued_fraction_ops____using_LazyList -x
py -m nn_ns.app.doctest_cmd seed.math.continued_fraction.continued_fraction_ops____using_LazyList:__doc__ -ff -v
py_adhoc_call   seed.math.continued_fraction.continued_fraction_ops____using_LazyList   @f

from seed.math.continued_fraction.continued_fraction_ops____using_LazyList import ContinuedFraction



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


cf_log_(lhs, rhs):
    = cf_truediv(cf_log2(lhs), cf_log2(rhs))
cf_log2(y):
    | 0 >= y = error
    | 1 > y = -cf_log2(cf_inv(y))
    | 1 == y = 0
    | 2 <= y = let gde2 = floor_log2(cf_floor_(y)) in cf_add(cf([gde2;]) + cf_log2(cf_truediv(y, 2**gde2)))
    | 1 < y < 2 = cf5float_ $ float_log2_cf__gt1_lt2(y)
#cf_log2__gt1_lt2(y)
float_log2_cf__gt1_lt2(y):
    | 1 < y < 2 = let y2 = cf_mul(y,y) in if y2 < 2 then 0:float_log2_cf__gt1_lt2(y2) else 1:float_log2_cf__gt1_lt2(cf_truediv(y2,2))
    | otherwise = error
fraction_log_(lhs, rhs):
    = (pint_log2(lhs)/pint_log2(rhs))
    = sum(exp*pint_log2(ft) for exp,ft in coprime_semifactor_(rhs;lhs))/sum(exp*pint_log2(ft) for exp,ft in coprime_semifactor_(lhs;rhs))
pint_log2(p):
    = cf_log2(cf([p;]))
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
_cf_cmp_(to_flip, cf_digitsL, cf_digitsR):
    * [cf_digitsL == [] == cf_digitsR]:
        -> 0 # eq
    * [cf_digitsL == [] =!= cf_digitsR]:
        # [+oo > not +oo]
        -> -1 if to_flip else +1
    * [cf_digitsL =!= [] == cf_digitsR]:
        # [not +oo < +oo]
        -> +1 if to_flip else -1
    * [cf0L == cf0R]:
        -> _cf_cmp_(not to_flip, cf_digitsL[1:], cf_digitsR[1:])
    * [cf0L > cf0R]:
        -> _cf_cmp_(not to_flip, cf_digitsR, cf_digitsL)
    # [cf0L < cf0R]:
    * [cf0L + 1 == cf0R][cf_digitsL==[cf0L,1]][cf_digitsR==[cf0R]]:
        -> 0 # eq
    * otherwise:
        # [lhs < rhs]
        -> +1 if to_flip else -1
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
    [y_remain := y_remainM * if to_neg and [not exact_] then base else 1]
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

.+1,1078s/\<cf_\w*\>(\[\@=/\0mk
.+1,1078s/\<cf_\w*\>(.*\],\s*\[\@=/\0mk
%s/mk\[\]/mk[()]/g
>>> class MkLazyList:
...     def __getitem__(sf, xs, /):
...         try:
...             it = iter(xs)
...         except TypeError:
...             x = xs
...             it = iter([x])
...         return LazyList(it)
>>> mk = MkLazyList()
>>> list(cf_neg(mk[()]))
Traceback (most recent call last):
    ...
seed.math.continued_fraction.continued_fraction_fold.ContinuedFractionError__inf__no_cf0
>>> list(cf_neg(mk[0]))
[0]
>>> list(cf_neg(mk[0, 1]))
[-1]
>>> list(cf_neg(mk[0, 2]))
[-1, 1, 1]
>>> list(cf_neg(mk[0, 1, 1]))
[-1, 2]
>>> list(cf_neg(mk[0, 1, 2]))
[-1, 3]
>>> list(cf_neg(mk[0, 2, 1]))
[-1, 1, 1, 1]
>>> list(cf_neg(mk[0, 2, 2]))
[-1, 1, 1, 2]

>>> list(cf_neg(mk[-1]))
[1]
>>> list(cf_neg(mk[-1, 1, 1]))
[0, 2]
>>> list(cf_neg(mk[-1, 2]))
[0, 1, 1]
>>> list(cf_neg(mk[-1, 3]))
[0, 1, 2]
>>> list(cf_neg(mk[-1, 1, 1, 1]))
[0, 2, 1]
>>> list(cf_neg(mk[-1, 1, 1, 2]))
[0, 2, 2]



>>> list(cf_inv(mk[()]))
Traceback (most recent call last):
    ...
seed.math.continued_fraction.continued_fraction_fold.ContinuedFractionError__inf__no_cf0
>>> list(cf_inv(mk[0]))
[]
>>> list(cf_inv(mk[0, 1]))
[1]
>>> list(cf_inv(mk[0, 2]))
[2]

>>> list(cf_inv(mk[1]))
[0, 1]
>>> list(cf_inv(mk[1, 1]))
[0, 1, 1]
>>> list(cf_inv(mk[1, 2]))
[0, 1, 2]
>>> list(cf_inv(mk[2]))
[0, 2]
>>> list(cf_inv(mk[2, 1]))
[0, 2, 1]
>>> list(cf_inv(mk[2, 2]))
[0, 2, 2]

>>> list(cf_inv(mk[-1]))
[-1]
>>> list(cf_inv(mk[-1, 1]))
Traceback (most recent call last):
    ...
seed.math.continued_fraction.continued_fraction_fold.ContinuedFractionError__inf__no_cf0
>>> list(cf_inv(mk[-1, 2]))
[-2]
>>> list(cf_inv(mk[-2]))
[-1, 1, 1]
>>> list(cf_inv(mk[-2, 1]))
[-1]
>>> list(cf_inv(mk[-2, 2]))
[-1, 2, 1]






>>> echo(cf_floor_(mk[()]))
Traceback (most recent call last):
    ...
seed.math.continued_fraction.continued_fraction_fold.ContinuedFractionError__inf__no_cf0
>>> echo(cf_floor_(mk[0]))
0
>>> echo(cf_floor_(mk[0, 1]))
1
>>> echo(cf_floor_(mk[0, 2]))
0
>>> echo(cf_floor_(mk[1]))
1
>>> echo(cf_floor_(mk[1, 1]))
2
>>> echo(cf_floor_(mk[1, 2]))
1
>>> echo(cf_floor_(mk[-1]))
-1
>>> echo(cf_floor_(mk[-1, 1]))
0
>>> echo(cf_floor_(mk[-1, 2]))
-1






iter_cf_digitsO__if_determined_by_1_and_inf_
>>> list(cf_add(mk[()], mk[()]))
[]
>>> list(cf_add(mk[()], mk[0]))
[]

Traceback (most recent call last):
    ...
seed.math.continued_fraction.continued_fraction_fold.ContinuedFractionError__inf__no_cf0
>>> list(cf_add(mk[0], mk[()]))
[]

Traceback (most recent call last):
    ...
seed.math.continued_fraction.continued_fraction_fold.ContinuedFractionError__inf__no_cf0
>>> list(cf_add(mk[0], mk[0]))
[0]
>>> list(cf_add(mk[0, 1], mk[0]))
[1]
>>> list(cf_add(mk[-2, 1,3,4,2], mk[0,4,2,2,1]))
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






>>> list(cf_mul(mk[()], mk[()]))
[]
>>> list(cf_mul(mk[()], mk[0])) # ??? [+oo*0 == +oo]
[]
>>> list(cf_mul(mk[0], mk[()]))
[]
>>> list(cf_mul(mk[0, 1], mk[0]))
[0]
>>> list(cf_mul(mk[0, 1], mk[1]))
[1]
>>> list(cf_mul(mk[-2, 1,3,4,2], mk[0,4,2,2,1]))
[-1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 10]
>>> list(iter_approximate_fractions5continued_fraction_([-1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 10]))[-1]
Fraction(-329, 1178)
>>> Fraction(-47, 38) * Fraction(7, 31)
Fraction(-329, 1178)



>>> echo(cf_cmp_(mk[()], mk[()]))
0
>>> echo(cf_cmp_(mk[()], mk[0]))
1
>>> echo(cf_cmp_(mk[0], mk[()]))
-1
>>> echo(cf_cmp_(mk[0], mk[0]))
0
>>> echo(cf_cmp_(mk[0], mk[1]))
-1
>>> echo(cf_cmp_(mk[1], mk[0]))
1
>>> echo(cf_cmp_(mk[0, 1], mk[1]))
0
>>> echo(cf_cmp_(mk[1], mk[0, 1]))
0
>>> echo(cf_cmp_(mk[1, 1], mk[1, 1]))
0
>>> echo(cf_cmp_(mk[1, 1], mk[1, 2]))
1
>>> echo(cf_cmp_(mk[1, 2], mk[1, 1]))
-1
>>> echo(cf_cmp_(mk[1, 1, 1], mk[1, 1]))
-1
>>> echo(cf_cmp_(mk[1, 1], mk[1, 1, 1]))
1
>>> echo(cf_cmp_(mk[1, 1, 1], mk[1, 2]))
0
>>> echo(cf_cmp_(mk[1, 2], mk[1, 1, 1]))
0
>>> echo(cf_cmp_(mk[1, 1, 2], mk[1, 1]))
-1
>>> echo(cf_cmp_(mk[1, 1], mk[1, 1, 2]))
1
>>> echo(cf_cmp_(mk[1, 1, 2], mk[1, 1, 1]))
1
>>> echo(cf_cmp_(mk[1, 1, 1], mk[1, 1, 2]))
-1
>>> echo(cf_cmp_(mk[1, 1, 2], mk[1, 1, 1, 1]))
0
>>> echo(cf_cmp_(mk[1, 1, 1, 1], mk[1, 1, 2]))
0
>>> echo(cf_cmp_(mk[1, 1, 2], mk[1, 1, 1, 1, 2]))
1
>>> echo(cf_cmp_(mk[1, 1, 1, 1, 2], mk[1, 1, 2]))
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
>>> list(cf_truediv(mk[4,2,3,5], mk[1,7,2,3]))
[3, 1, 9, 1, 2, 2, 1, 9, 2]
>>> len(cf_divmod(mk[4,2,3,5], mk[1,7,2,3]))
2
>>> echo(cf_divmod(mk[4,2,3,5], mk[1,7,2,3])[0])
3
>>> list(cf_divmod(mk[4,2,3,5], mk[1,7,2,3])[1])
[1, 34, 1, 54]


>>> echo(cf_lt_(mk[1], mk[1]))
False
>>> echo(cf_lt_(mk[1], mk[2]))
True
>>> echo(cf_lt_(mk[2], mk[1]))
False

>>> echo(cf_gt_(mk[1], mk[1]))
False
>>> echo(cf_gt_(mk[1], mk[2]))
False
>>> echo(cf_gt_(mk[2], mk[1]))
True

>>> echo(cf_le_(mk[1], mk[1]))
True
>>> echo(cf_le_(mk[1], mk[2]))
True
>>> echo(cf_le_(mk[2], mk[1]))
False

>>> echo(cf_ge_(mk[1], mk[1]))
True
>>> echo(cf_ge_(mk[1], mk[2]))
False
>>> echo(cf_ge_(mk[2], mk[1]))
True

>>> echo(cf_eq_(mk[1], mk[1]))
True
>>> echo(cf_eq_(mk[1], mk[2]))
False
>>> echo(cf_eq_(mk[2], mk[1]))
False

>>> echo(cf_ne_(mk[1], mk[1]))
False
>>> echo(cf_ne_(mk[1], mk[2]))
True
>>> echo(cf_ne_(mk[2], mk[1]))
True


>>> 0**0 #ZeroDivisionError
1
>>> 0**-2 #ZeroDivisionError
Traceback (most recent call last):
    ...
ZeroDivisionError: 0.0 cannot be raised to a negative power











decorator4protocol4ToConcatLazyList_
ContinuedFraction
is_int
math.floor
math.ceil
abs + - inv_
+ * - / % // divmod pow
== !=
> < >= <=


>>> cf_0
ContinuedFraction(LazyList([<...>]))
>>> bool(cf_0)
Traceback (most recent call last):
    ...
TypeError: 'ellipsis' object is not callable
>>> len(cf_0)
Traceback (most recent call last):
    ...
TypeError: 'ellipsis' object is not callable
>>> 0 in cf_0
Traceback (most recent call last):
    ...
TypeError: 'ellipsis' object is not callable

>>> cf_0 == cf_0
True
>>> cf_0 != cf_0
False
>>> cf_0 < cf_0
False
>>> cf_0 <= cf_0
True
>>> cf_0 > cf_0
False
>>> cf_0 >= cf_0
True

>>> cf_0 == cf_1
False
>>> cf_0 != cf_1
True
>>> cf_0 < cf_1
True
>>> cf_0 <= cf_1
True
>>> cf_0 > cf_1
False
>>> cf_0 >= cf_1
False

>>> cf_21_over_13 = ContinuedFraction(Fraction(21, 13))
>>> cfs = [cf_e, cf_golden_ratio_phi, cf_sqrt2, cf_pi__prefix2001, cf_0, cf_1, cf_neg1, cf_21_over_13]
>>> cfs.sort()
>>> cfs
[ContinuedFraction(LazyList([-1])), ContinuedFraction(LazyList([0])), ContinuedFraction(LazyList([1])), ContinuedFraction(LazyList([1, 2, 2, <...>])), ContinuedFraction(LazyList([1, 1, 1, 1, 1, 2])), ContinuedFraction(LazyList([1, 1, 1, 1, 1, 1, 1, 1, <...>])), ContinuedFraction(LazyList([2, 1, <...>])), ContinuedFraction(LazyList([3, 7, <...>]))]
>>> [cf.is_int() for cf in cfs]
[True, True, True, False, False, False, False, False]
>>> import math
>>> [math.floor(cf) for cf in cfs]
[-1, 0, 1, 1, 1, 1, 2, 3]
>>> [math.ceil(cf) for cf in cfs]
[-1, 0, 1, 2, 2, 2, 3, 4]
>>> cfs # cf_e: [2,1,...] --> [2,1,2,...]
[ContinuedFraction(LazyList([-1])), ContinuedFraction(LazyList([0])), ContinuedFraction(LazyList([1])), ContinuedFraction(LazyList([1, 2, 2, <...>])), ContinuedFraction(LazyList([1, 1, 1, 1, 1, 2])), ContinuedFraction(LazyList([1, 1, 1, 1, 1, 1, 1, 1, <...>])), ContinuedFraction(LazyList([2, 1, 2, <...>])), ContinuedFraction(LazyList([3, 7, <...>]))]
>>> [abs(cf) for cf in cfs]
[ContinuedFraction(LazyList([1])), ContinuedFraction(LazyList([0])), ContinuedFraction(LazyList([1])), ContinuedFraction(LazyList([1, 2, 2, <...>])), ContinuedFraction(LazyList([1, 1, 1, 1, 1, 2])), ContinuedFraction(LazyList([1, 1, 1, 1, 1, 1, 1, 1, <...>])), ContinuedFraction(LazyList([2, 1, 2, <...>])), ContinuedFraction(LazyList([3, 7, <...>]))]
>>> [+cf for cf in cfs]
[ContinuedFraction(LazyList([-1])), ContinuedFraction(LazyList([0])), ContinuedFraction(LazyList([1])), ContinuedFraction(LazyList([1, 2, 2, <...>])), ContinuedFraction(LazyList([1, 1, 1, 1, 1, 2])), ContinuedFraction(LazyList([1, 1, 1, 1, 1, 1, 1, 1, <...>])), ContinuedFraction(LazyList([2, 1, 2, <...>])), ContinuedFraction(LazyList([3, 7, <...>]))]
>>> [-cf for cf in cfs]
[ContinuedFraction(LazyList([1])), ContinuedFraction(LazyList([0])), ContinuedFraction(LazyList([-1])), ContinuedFraction(LazyList([-2, 1, 1, 2, <...>])), ContinuedFraction(LazyList([-2, 2, 1, 1, 2])), ContinuedFraction(LazyList([-2, 2, 1, 1, 1, 1, 1, <...>])), ContinuedFraction(LazyList([-3, 3, <...>])), ContinuedFraction(LazyList([-4, 1, 6, <...>]))]
>>> [cf.inv_() for cf in cfs if not cf == cf_0]
[ContinuedFraction(LazyList([-1])), ContinuedFraction(LazyList([0, 1])), ContinuedFraction(LazyList([0, 1, 2, 2, <...>])), ContinuedFraction(LazyList([0, 1, 1, 1, 1, 1, 2])), ContinuedFraction(LazyList([0, 1, 1, 1, 1, 1, 1, 1, 1, <...>])), ContinuedFraction(LazyList([0, 2, 1, 2, <...>])), ContinuedFraction(LazyList([0, 3, 7, <...>]))]
>>> cf_0.inv_()
ContinuedFraction(LazyList())

>>> from itertools import islice
>>> fr_pi__apprx0_9 = [*islice(cf_pi__prefix2001.iter_approximate_fractions_(), 9)]
>>> fr_pi__apprx0_9
[Fraction(3, 1), Fraction(22, 7), Fraction(333, 106), Fraction(355, 113), Fraction(103993, 33102), Fraction(104348, 33215), Fraction(208341, 66317), Fraction(312689, 99532), Fraction(833719, 265381)]
>>> cf_355_over_113 = ContinuedFraction(Fraction(355, 113))
>>> cf_355_over_113.to_Fraction_or_dead_loop_()
Fraction(355, 113)
>>> cf_355_over_113
ContinuedFraction(LazyList([3, 7, 16]))
>>> cf_21_over_13
ContinuedFraction(LazyList([1, 1, 1, 1, 1, 2]))
>>> sum_ = cf_355_over_113 + cf_21_over_13
>>> product_ = cf_355_over_113 * cf_21_over_13
>>> sum_
ContinuedFraction(LazyList([<...>]))
>>> product_
ContinuedFraction(LazyList([<...>]))
>>> sum_.to_Fraction_or_dead_loop_()
Fraction(6988, 1469)
>>> product_.to_Fraction_or_dead_loop_()
Fraction(7455, 1469)
>>> sum_
ContinuedFraction(LazyList([4, 1, 3, 8, 1, 2, 2, 2, 2]))
>>> product_
ContinuedFraction(LazyList([5, 13, 2, 1, 4, 1, 1, 3]))
>>> cf_355_over_113.to_Fraction_or_dead_loop_() + cf_21_over_13.to_Fraction_or_dead_loop_()
Fraction(6988, 1469)
>>> cf_355_over_113.to_Fraction_or_dead_loop_() * cf_21_over_13.to_Fraction_or_dead_loop_()
Fraction(7455, 1469)


>>> diff_ = cf_355_over_113 - cf_21_over_13
>>> ratio_ = cf_355_over_113 / cf_21_over_13
>>> rem_ = cf_355_over_113 % cf_21_over_13
>>> quo_ = cf_355_over_113 // cf_21_over_13
>>> diff_
ContinuedFraction(LazyList([<...>]))
>>> ratio_
ContinuedFraction(LazyList([<...>]))
>>> rem_
ContinuedFraction(LazyList([<...>]))
>>> quo_
1
>>> diff_.to_Fraction_or_dead_loop_()
Fraction(2242, 1469)
>>> ratio_.to_Fraction_or_dead_loop_()
Fraction(4615, 2373)
>>> rem_.to_Fraction_or_dead_loop_()
Fraction(2242, 1469)
>>> diff_
ContinuedFraction(LazyList([1, 1, 1, 9, 25, 1, 2]))
>>> ratio_
ContinuedFraction(LazyList([1, 1, 17, 8, 1, 2, 1, 3]))
>>> rem_
ContinuedFraction(LazyList([1, 1, 1, 9, 25, 1, 2]))
>>> cf_355_over_113.to_Fraction_or_dead_loop_() - cf_21_over_13.to_Fraction_or_dead_loop_()
Fraction(2242, 1469)
>>> cf_355_over_113.to_Fraction_or_dead_loop_() / cf_21_over_13.to_Fraction_or_dead_loop_()
Fraction(4615, 2373)
>>> cf_355_over_113.to_Fraction_or_dead_loop_() % cf_21_over_13.to_Fraction_or_dead_loop_()
Fraction(2242, 1469)
>>> cf_355_over_113.to_Fraction_or_dead_loop_() // cf_21_over_13.to_Fraction_or_dead_loop_()
1

>>> (quo_, rem_) == divmod(cf_355_over_113, cf_21_over_13)
True

#>>> for exp in range(-10, 11):(exp, pow(cf_21_over_13.to_Fraction_or_dead_loop_(), exp))
>>> for exp in range(-10, 11):(exp, pow(cf_21_over_13, exp).to_Fraction_or_dead_loop_())
(-10, Fraction(137858491849, 16679880978201))
(-9, Fraction(10604499373, 794280046581))
(-8, Fraction(815730721, 37822859361))
(-7, Fraction(62748517, 1801088541))
(-6, Fraction(4826809, 85766121))
(-5, Fraction(371293, 4084101))
(-4, Fraction(28561, 194481))
(-3, Fraction(2197, 9261))
(-2, Fraction(169, 441))
(-1, Fraction(13, 21))
(0, Fraction(1, 1))
(1, Fraction(21, 13))
(2, Fraction(441, 169))
(3, Fraction(9261, 2197))
(4, Fraction(194481, 28561))
(5, Fraction(4084101, 371293))
(6, Fraction(85766121, 4826809))
(7, Fraction(1801088541, 62748517))
(8, Fraction(37822859361, 815730721))
(9, Fraction(794280046581, 10604499373))
(10, Fraction(16679880978201, 137858491849))

#>>> all(pow(cf_21_over_13, exp).to_Fraction_or_dead_loop_() == pow(cf_21_over_13.to_Fraction_or_dead_loop_(), exp) for exp in range(-40, 41))
>>> all(pow(cf_21_over_13, exp).to_Fraction_or_dead_loop_() == pow(cf_21_over_13.to_Fraction_or_dead_loop_(), exp) for exp in range(-10, 11))
True

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


cf_is_int_
cf_floor_
cf_ceil_
cf_floor_ex_
cf_mul
    cf_truediv
        cf_divmod

cf_cmp_
    cf_lt_
        cf_ge_
        cf_le_
        cf_gt_
    cf_eq_
        cf_ne_

ContinuedFraction
    cf_0
    cf_1
    cf_neg1

    cf_e
        cf_the_natural_logarithm_base_e
        raw_iter_cf_digits4e_the_natural_logarithm_base_
    cf_phi
        cf_golden_ratio_phi
        raw_iter_cf_digits4phi_the_golden_ratio_
    cf_sqrt2
        cf_square_root_of_2
        raw_iter_cf_digits4sqrt2_
    cf_pi__prefix2001
        cf_circumference_diameter_ratio_pi__prefix2001

'''.split()#'''
    #chain__strict_
    #cf_unpack_or_raise
__all__
from seed.types.LazySeq import LazySeq
from seed.types.LazyList import decorator4protocol4ToConcatLazyList_, ToConcatLazyList
from seed.types.LazyList import LazyList, LazyListError

from fractions import Fraction
#from itertools import chain, islice, count as _count_
    # chain__strict_
#import itertools # count


from seed.tiny import check_type_is
from seed.tiny_.check import check_uint, check_int_ge
from seed.tiny import echo, null_iter, is_iterable, is_iterator
from seed.tiny import print_err, mk_fprint, mk_assert_eq_f, expectError
from seed.math.PowSeq import PowSeq
from seed.math.divs import is_even
#from seed.iters.PeekableIterator import PeekableIterator
    #view ../../python3_src/seed/iters/PeekableIterator.py
from seed.math.continued_fraction.continued_fraction_fold import ContinuedFractionError__inf__no_cf0
#from seed.math.continued_fraction.continued_fraction_fold import ContinuedFractionFoldState, continued_fraction_fold_state0
from seed.math.continued_fraction.continued_fraction_fold import iter_continued_fraction_digits5ND_, iter_approximate_fractions5continued_fraction_

from seed.helper.repr_input import repr_helper
from seed.types.NamedReadOnlyProperty import NamedReadOnlyProperty, set_NamedReadOnlyProperty4cls_, set_NamedReadOnlyProperty4sf_

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

    #def iter_cf_digitsO__if_determined_by_1_and_inf_(sf, y, z, /):
    @decorator4protocol4ToConcatLazyList_
    def mk_cf_digitsO__if_determined_by_1_and_inf_(sf, y, z, /):
        'y/tail-cf_digitsL -> z/tail-cf_digitsR -> cf_digitsO'
        check_type_is(LazyList, y)
        check_type_is(LazyList, z)
        while not z.is_empty__hardwork():
            if y.is_empty__hardwork():
                sf = sf.swapLR()
                y, z = z, y
                continue
            # [nonempty y,z]


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
                # !! [nonempty y,z]
                Ky, y = y.may_unpack()
                sf = sf.step_cf_digitL_(Ky)
            #
            if to_step_z:
                # !! [nonempty y,z]
                Kz, z = z.may_unpack()
                sf = sf.step_cf_digitR_(Kz)

            if not (to_step_y or to_step_z):
                cf0 = _1_oo
                yield cf0
                sf = sf.step_cf_digitO_(cf0)
        #end-while
        assert z.is_empty__hardwork()
        # [z==+oo]
        #ContinuedFractionState__1var
        st = sf.to_ContinuedFractionState__1var__if_rhs_tail_is_empty()
        raise ToConcatLazyList(st.mk_cf_digitsO__if_determined_by_1_and_inf_(y))
        return
        yield from st.iter_cf_digitsO__if_determined_by_1_and_inf_(y)
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
    #def iter_cf_digitsO__if_determined_by_1_and_inf_(sf, y, /):
    @decorator4protocol4ToConcatLazyList_
    def mk_cf_digitsO__if_determined_by_1_and_inf_(sf, y, /):
        'y/tail-cf_digitsL -> cf_digitsO'
        # [z==+oo]
        check_type_is(LazyList, y)
        while not y.is_empty__hardwork():
            # [nonempty y]

            if sf.dyz == 0:
                to_step_y = True
                    #init
                if sf.nz == 0 and sf.dz == sf.nyz != 0:
                    # [sf == y]
                    raise ToConcatLazyList(y)
            else:
                _1_oo = sf.eval_at_1_or_inf_(False, to_floor=True)
                _oo_oo = sf.eval_at_1_or_inf_(True, to_floor=True)
                to_step_y = not (_1_oo == _oo_oo)
            to_step_y


            if to_step_y:
                # !! [nonempty y]
                Ky, y = y.may_unpack()
                sf = sf.step_cf_digitL_(Ky)
            else:
                cf0 = _1_oo
                yield cf0
                sf = sf.step_cf_digitO_(cf0)
        #end-while
        assert y.is_empty__hardwork()
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

__all__

'cf_digits :: LazyList<int>{fst int; others pint}'
if 0:
    def chain__strict_(xs, cf_digits, /):
        for x in reversed(xs):
            cf_digits = LazyList(x, cf_digits)
        return cf_digits
chain__strict_ = LazyList.concat_initial_seq_
#chain__lazy_ = LazyList.concat_initial_iterator_

def cf_unpack_or_raise(cf_digits, /):
    'cf_digits :: LazyList<int>{fst int; others pint}'
    m = cf_digits.may_unpack()
    if m is None:
        raise ContinuedFractionError__inf__no_cf0
    return m

def cf_inv(cf_digits, /):
    cf0, _1_cf_digits = cf_unpack_or_raise(cf_digits)
    1;  del cf_digits
    if cf0 == 0:
        return _1_cf_digits # may be +oo
    elif cf0 > 0:
        return chain__strict_([0,cf0], _1_cf_digits)
    else:
        return cf_neg(cf_inv(cf_neg(chain__strict_([cf0], _1_cf_digits))))

def cf_neg(cf_digits, /):
    cf0, _1_cf_digits = cf_unpack_or_raise(cf_digits)
    1;  del cf_digits
    cf0, _1_cf_digits

    m = _1_cf_digits.may_unpack()
    if m is None:
        # cf_neg__case1
        # <==> [cf_digits==[cf0;]]
        return chain__strict_([-cf0], None)
        return LazyList(iter([-cf0]))
    cf1, _2_cf_digits = m
    1;  del _1_cf_digits
    cf0, cf1, _2_cf_digits

    if cf1 >= 2:
        # cf_neg__case4
        return chain__strict_([-1-cf0, 1, cf1-1], _2_cf_digits)
    assert cf1 == 1

    m = _2_cf_digits.may_unpack()
    if m is None:
        # cf_neg__case2
        # <==> [cf_digits==[cf0;1]]
        return chain__strict_([-1-cf0], None)
        return LazyList(iter([-1-cf0]))
    cf2, _3_cf_digits = m
    1;  del _2_cf_digits
    cf0, cf1, cf2, _3_cf_digits

    if 1:
        # cf_neg__case3
        # <==> [cf_digits==[cf0;1,cf2,...]]
        return chain__strict_([-1-cf0, cf2+1], _3_cf_digits)

def cf_sub(lhs, rhs, /):
    return cf_add(lhs, cf_neg(rhs))
def cf_add(lhs, rhs, /):
    'st4cf_add := (0 + 1*y + 1*z + (cf0L+cf0R)*y*z)/(0 + 0*y + 0*z + y*z)'

    #st4cf_add = ContinuedFractionState__2vars(0,1,1,cf0L+cf0R,  0,0,0,1)
    st4cf_add = ContinuedFractionState__2vars(0,1,1,0,  1,0,0,0)
    cf_digits = st4cf_add.mk_cf_digitsO__if_determined_by_1_and_inf_(lhs, rhs)
    check_type_is(LazyList, cf_digits)
    return cf_digits
    return LazyList(st4cf_add.iter_cf_digitsO__if_determined_by_1_and_inf_(lhs, rhs))
def cf_is_int_(cf_digits, /):
    (is_int, cf0_x) = cf_floor_ex_(cf_digits)
    return is_int
def cf_floor_(cf_digits, /):
    (is_int, cf0_x) = cf_floor_ex_(cf_digits)
    return cf0_x
def cf_ceil_(cf_digits, /):
    (is_int, cf0_x) = cf_floor_ex_(cf_digits)
    return cf0_x if is_int else cf0_x+1
def cf_floor_ex_(cf_digits, /):
    cf0, _1_cf_digits = cf_unpack_or_raise(cf_digits)
    1;  del cf_digits
    cf0, _1_cf_digits
    #bug:return cf0
    #   non-std form from slice may cause last item be 1: [cf0; 1]

    m = _1_cf_digits.may_unpack()
    if m is None:
        # <==> [cf_digits==[cf0;]]
        is_int = True
        return is_int, cf0
    cf1, _2_cf_digits = m
    1;  del _1_cf_digits
    cf0, cf1, _2_cf_digits

    if cf1 >= 2:
        is_int = False
        return is_int, cf0
    assert cf1 == 1

    m = _2_cf_digits.may_unpack()
    if m is None:
        # <==> [cf_digits==[cf0;1]]
        is_int = True
        return is_int, 1+cf0
    cf2, _3_cf_digits = m
    1;  del _2_cf_digits
    cf0, cf1, cf2, _3_cf_digits

    is_int = False
    return is_int, cf0




def cf_divmod(lhs, rhs, /):
    iq = cf_floor_(cf_truediv(lhs, rhs))
    #cf8q = LazyList(iter([iq]))
    cf8q = chain__strict_([iq], None)
    r = cf_sub(lhs, cf_mul(cf8q, rhs))
    return (iq,r)
def cf_truediv(lhs, rhs, /):
    return cf_mul(lhs, cf_inv(rhs))
def cf_mul(lhs, rhs, /):
    'st4cf_mul := (1 + cf0L*y + cf0R*z + (cf0L*cf0R)*y*z)/(0 + 0*y + 0*z + y*z)'
    #st4cf_mul = ContinuedFractionState__2vars(1,cf0L,cf0R,cf0L*cf0R,  0,0,0,1)
    st4cf_mul = ContinuedFractionState__2vars(0,0,0,1,  1,0,0,0)
    cf_digits = st4cf_mul.mk_cf_digitsO__if_determined_by_1_and_inf_(lhs, rhs)
    check_type_is(LazyList, cf_digits)
    return cf_digits
    return LazyList(st4cf_mul.iter_cf_digitsO__if_determined_by_1_and_inf_(lhs, rhs))



def cf_ge_(lhs, rhs, /):
    return not cf_lt_(lhs, rhs)
def cf_le_(lhs, rhs, /):
    return not cf_gt_(lhs, rhs)
def cf_gt_(lhs, rhs, /):
    return cf_lt_(rhs, lhs)
def cf_lt_(lhs, rhs, /):
    return cf_cmp_(lhs, rhs) == -1
#def _cf_lt_(to_flip, cf_digitsL, cf_digitsR, /):
def _result_with_flip_(to_flip, r, /):
    return -r if to_flip else r
def cf_cmp_(lhs, rhs, /):
    '-> [-1,0,+1]'
    return _cf_cmp_(False, lhs, rhs)
def _cf_cmp_(to_flip, cf_digitsL, cf_digitsR, /):
    while 1:
        nullL = cf_digitsL.is_empty__hardwork()
        nullR = cf_digitsR.is_empty__hardwork()
        if nullL and nullR:
            return 0 # eq
        elif nullL and not nullR:
            # [+oo > not +oo]
            return _result_with_flip_(to_flip, +1)
        elif not nullL and nullR:
            # [not +oo < +oo]
            return _result_with_flip_(to_flip, -1)
        # [nonempty cf_digitsL, cf_digitsR]
        cf0L, _1_cf_digitsL = cf_digitsL.may_unpack()
        cf0R, _1_cf_digitsR = cf_digitsR.may_unpack()
        if cf0L == cf0R:
            #return _cf_cmp_(not to_flip, _1_cf_digitsL, _1_cf_digitsR)
            to_flip = not to_flip
            cf_digitsL = _1_cf_digitsL
            cf_digitsR = _1_cf_digitsR
            continue
        elif cf0L > cf0R:
            #return _cf_cmp_(not to_flip, cf_digitsR, cf_digitsL)
            to_flip = not to_flip
            cf_digitsL, cf_digitsR = cf_digitsR, cf_digitsL
            continue

        # [cf0L < cf0R]
        elif cf0L + 1 == cf0R and cf_digitsR.extract_prefix__le(2, relax=False) == (cf0R,) and cf_digitsL.extract_prefix__le(3, relax=False) == (cf0L,1):
            return 0 # eq
        else:
            # [lhs < rhs]
            return _result_with_flip_(to_flip, -1)
def cf_ne_(lhs, rhs, /):
    return not cf_eq_(lhs, rhs)
def cf_eq_(lhs, rhs, /):
    return cf_cmp_(lhs, rhs) == 0

r'''[[[
TODO:
def pow__cf__int_(cf_digits, e, /):
    bin
cf_log_(lhs, rhs, /):
view ../../python3_src/seed/math/continued_fraction/iter_continued_fraction_of_log__truncated_.py
#]]]'''#'''


class ContinuedFraction(LazySeq):
    r'''[[[
    __bool__ is forbidden
        sf == cf_0
        len(sf.the_lazylist) > 0
    __len__ is forbidden
    __contains__ is forbidden


    cf([cf0; tail0...])
        [cf0 :: int]
        [tail0 :: [pint]]

    #]]]'''#'''
    @property
    def _cf_digits(sf, /):
        return sf.the_lazylist
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
            sf = super(__class__, cls).__new__(cls, cf_digits)
        return sf
    if 0:
        #@override
        def _check_on_no_more_extend_(sf, _init_seq, _tails, /):
            super()._check_on_no_more_extend_(_init_seq, _tails)
            if not _init_seq:
                raise ContinuedFractionError__inf__no_cf0
    #@override
    def _check_post__extend_more_(sf, _init_seq, begin4init_seq, _tails, begin4tails, /):
        super()._check_post__extend_more_(_init_seq, begin4init_seq, _tails, begin4tails)
        for i, u in enumerate(_init_seq[begin4init_seq:], begin4init_seq):
            if i == 0:
                cf0 = u
                check_type_is(int, cf0)
            else:
                check_int_ge(1, u)

    def __iter__(sf, /):
        it = super(__class__, sf).__iter__()
        #it = iter(sf._cf_digits)
        del sf # to free memory as soon as possible: _cf_digits,_ls,_tmay_tail
        return __class__._iter(it)
    def _iter(it, /):
        'detect again besides ._check_on_no_more_extend_() since .__iter__() bypass .extend_more_()'
        if not is_iterator(it): raise logic-err
        for cf0 in it:
            break
        else:
            raise ContinuedFractionError__inf__no_cf0
        check_type_is(int, cf0)
        yield cf0
        del cf0

        if 0:
            yield from it
        else:
            for u in it:
                check_int_ge(1, u)
                yield u

    def to_Fraction_or_dead_loop_(sf, /):
        frs = sf.iter_approximate_fractions_()
        del sf
        fr = Nothing = []
        for fr in frs:
            pass
        if fr is Nothing:
            raise logic-err
            raise ContinuedFractionError__inf__no_cf0
        return fr
    def iter_approximate_fractions_(sf, /):
        it = iter(sf)
        del sf
        return iter_approximate_fractions5continued_fraction_(it)
    def is_int(sf, /):
        return cf_is_int_(sf._cf_digits)
    def __floor__(sf, /):
        return cf_floor_(sf._cf_digits)
    def __ceil__(sf, /):
        return cf_ceil_(sf._cf_digits)
    def _cmp_(sf, ot, /):
        ot = __class__(ot)
        return cf_cmp_(sf._cf_digits, ot._cf_digits)
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
        if sf < cf_0:
            return -sf
        return sf
    def __pos__(sf, /):
        return sf
    def __neg__(sf, /):
        return __class__(cf_neg(sf._cf_digits))
    def inv_(sf, /):
        return __class__(cf_inv(sf._cf_digits))
    def __add__(sf, ot, /):
        ot = __class__(ot)
        if ot == cf_0:
            return sf
        if sf == cf_0:
            return ot
        return __class__(cf_add(sf._cf_digits, ot._cf_digits))
    def __mul__(sf, ot, /):
        ot = __class__(ot)
        if ot == cf_1:
            return sf
        if sf == cf_1:
            return ot
        if sf == cf_0:
            return sf
        if ot == cf_0:
            return ot
        if ot == cf_neg1:
            return -sf
        if sf == cf_neg1:
            return -ot
        return __class__(cf_mul(sf._cf_digits, ot._cf_digits))

    def __sub__(sf, ot, /):
        ot = __class__(ot)
        if sf._cf_digits is ot._cf_digits:
            return cf_0
        return sf + (-ot)
    def __truediv__(sf, ot, /):
        ot = __class__(ot)
        if ot == cf_0:
            raise ZeroDivisionError
            raise ContinuedFractionError__inf__no_cf0
        if sf._cf_digits is ot._cf_digits:
            return cf_1
        return sf * ot.inv_()

    def __divmod__(sf, ot, /):
        ot = __class__(ot)
        if ot == cf_0:
            raise ZeroDivisionError
        if sf._cf_digits is ot._cf_digits:
            return (cf_1, cf_0)
        iq, r = cf_divmod(sf._cf_digits, ot._cf_digits)
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
        if sf == cf_1:
            return sf
        if sf == cf_neg1:
            return cf_1 if is_even(e) else cf_neg1
        if sf == cf_0:
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

#end-class ContinuedFraction:

cf_0 = ContinuedFraction(0)
cf_1 = ContinuedFraction(1)
cf_neg1 = ContinuedFraction(-1)

r'''[[[
the base of the natural logarithm e = [1+1;1,2,  1,1,4,  1,1,6...1,1,2n,...]

golden ratio phi = [1;1...]

square root of 2 = [1;2,2...]

e = [2;1,2,1,1,4,1,1,6,1,1,8,...] = 1+[1;1,2,   1,1,4,   1,1,6...] = [2;  1,2,1, 1,4,1,  1,6,1,  1,8,...]
http://oeis.org/A001203

Continued fraction expansion of Pi

cf_pi[:98] =:
[3,7,15,1,292,1,1,1,2,1,3,1,14,2,1,1,2,2,2,2,1,84,
 2,1,1,15,3,13,1,4,2,6,6,99,1,2,2,6,3,5,1,1,6,8,1,
 7,1,2,3,7,1,2,1,1,12,1,1,1,3,1,1,8,1,1,2,1,6,1,1,
 5,2,2,3,1,2,4,4,16,1,161,45,1,22,1,2,2,1,4,1,2,24,
 1,2,1,3,1,2,1]

ratio of the circumference of a circle to its diameter
circumference_diameter_ratio_pi
view ../../../unzip/e_book/连分数/continued_fraction_pi/continued_fraction_pi_100term_per_line_omit_zeroth_term.txt
cf_pi[:1+100*??!] =: [
3,
7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, 1, 1, 2, 2, 2, 2, 1, 84, 2, 1, 1, 15, 3, 13, 1, 4, 2, 6, 6, 99, 1, 2, 2, 6, 3, 5, 1, 1, 6, 8, 1, 7, 1, 2, 3, 7, 1, 2, 1, 1, 12, 1, 1, 1, 3, 1, 1, 8, 1, 1, 2, 1, 6, 1, 1, 5, 2, 2, 3, 1, 2, 4, 4, 16, 1, 161, 45, 1, 22, 1, 2, 2, 1, 4, 1, 2, 24, 1, 2, 1, 3, 1, 2, 1, 1, 10, 2,
...
]

#]]]'''#'''
def raw_iter_cf_digits4e_the_natural_logarithm_base_():
    'natural logarithm base e = 1+[1;1,2,   1,1,4,   1,1,6...] = [2;  1,2,1, 1,4,1,  1,6,1,  1,8,...]'
    yield 2
    x = 0
    while 1:
        yield 1
        x += 2
        yield x
        yield 1

cf_e = cf_the_natural_logarithm_base_e = ContinuedFraction(raw_iter_cf_digits4e_the_natural_logarithm_base_())
def raw_iter_cf_digits4phi_the_golden_ratio_():
    'golden ratio phi = [1;1...]'
    while 1:
        yield 1
cf_phi = cf_golden_ratio_phi = ContinuedFraction(raw_iter_cf_digits4phi_the_golden_ratio_())
def raw_iter_cf_digits4sqrt2_():
    'square root of 2 = [1;2,2...]'
    yield 1
    while 1:
        yield 2
cf_sqrt2 = cf_square_root_of_2 = ContinuedFraction(raw_iter_cf_digits4sqrt2_())

cf_pi__prefix2001 = (
3,
7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, 1, 1, 2, 2, 2, 2, 1, 84, 2, 1, 1, 15, 3, 13, 1, 4, 2, 6, 6, 99, 1, 2, 2, 6, 3, 5, 1, 1, 6, 8, 1, 7, 1, 2, 3, 7, 1, 2, 1, 1, 12, 1, 1, 1, 3, 1, 1, 8, 1, 1, 2, 1, 6, 1, 1, 5, 2, 2, 3, 1, 2, 4, 4, 16, 1, 161, 45, 1, 22, 1, 2, 2, 1, 4, 1, 2, 24, 1, 2, 1, 3, 1, 2, 1, 1, 10, 2,
5, 4, 1, 2, 2, 8, 1, 5, 2, 2, 26, 1, 4, 1, 1, 8, 2, 42, 2, 1, 7, 3, 3, 1, 1, 7, 2, 4, 9, 7, 2, 3, 1, 57, 1, 18, 1, 9, 19, 1, 2, 18, 1, 3, 7, 30, 1, 1, 1, 3, 3, 3, 1, 2, 8, 1, 1, 2, 1, 15, 1, 2, 13, 1, 2, 1, 4, 1, 12, 1, 1, 3, 3, 28, 1, 10, 3, 2, 20, 1, 1, 1, 1, 4, 1, 1, 1, 5, 3, 2, 1, 6, 1, 4, 1, 120, 2, 1, 1, 3,
1, 23, 1, 15, 1, 3, 7, 1, 16, 1, 2, 1, 21, 2, 1, 1, 2, 9, 1, 6, 4, 127, 14, 5, 1, 3, 13, 7, 9, 1, 1, 1, 1, 1, 5, 4, 1, 1, 3, 1, 1, 29, 3, 1, 1, 2, 2, 1, 3, 1, 1, 1, 3, 1, 1, 10, 3, 1, 3, 1, 2, 1, 12, 1, 4, 1, 1, 1, 1, 7, 1, 1, 2, 1, 11, 3, 1, 7, 1, 4, 1, 48, 16, 1, 4, 5, 2, 1, 1, 4, 3, 1, 2, 3, 1, 2, 2, 1, 2, 5,
20, 1, 1, 5, 4, 1, 436, 8, 1, 2, 2, 1, 1, 1, 1, 1, 5, 1, 2, 1, 3, 6, 11, 4, 3, 1, 1, 1, 2, 5, 4, 6, 9, 1, 5, 1, 5, 15, 1, 11, 24, 4, 4, 5, 2, 1, 4, 1, 6, 1, 1, 1, 4, 3, 2, 2, 1, 1, 2, 1, 58, 5, 1, 2, 1, 2, 1, 1, 2, 2, 7, 1, 15, 1, 4, 8, 1, 1, 4, 2, 1, 1, 1, 3, 1, 1, 1, 2, 1, 1, 1, 1, 1, 9, 1, 4, 3, 15, 1, 2,
1, 13, 1, 1, 1, 3, 24, 1, 2, 4, 10, 5, 12, 3, 3, 21, 1, 2, 1, 34, 1, 1, 1, 4, 15, 1, 4, 44, 1, 4, 20776, 1, 1, 1, 1, 1, 1, 1, 23, 1, 7, 2, 1, 94, 55, 1, 1, 2, 1, 1, 3, 1, 1, 32, 5, 1, 14, 1, 1, 1, 1, 1, 3, 50, 2, 16, 5, 1, 2, 1, 4, 6, 3, 1, 3, 3, 1, 2, 2, 2, 5, 2, 2, 2, 28, 1, 1, 13, 1, 5, 43, 1, 4, 3, 5, 3, 1, 4, 1, 1,
2, 2, 1, 1, 19, 2, 7, 1, 72, 3, 1, 2, 3, 7, 11, 1, 2, 1, 1, 2, 2, 1, 1, 2, 1, 1, 1, 1, 1, 33, 7, 19, 1, 19, 3, 1, 4, 1, 1, 1, 1, 2, 3, 1, 3, 2, 2, 2, 2, 4, 1, 1, 1, 4, 2, 3, 1, 1, 1, 1, 11, 1, 1, 2, 1, 2, 1, 2, 2, 1, 7, 2, 27, 1, 1, 6, 2, 1, 9, 6, 26, 1, 1, 3, 2, 1, 1, 1, 1, 1, 15, 1, 36, 4, 2, 2, 1, 22, 2, 1,
106, 2, 2, 1, 3, 1, 12, 10, 7, 1, 2, 1, 1, 1, 1, 8, 2, 4, 5, 3, 2, 1, 4, 23, 1, 18, 2, 10, 3, 1, 6, 6, 13, 8, 6, 2, 2, 2, 2, 1, 1, 1, 3, 1, 7, 17, 1, 1, 1, 2, 5, 5, 1, 1, 2, 11, 1, 6, 1, 6, 1, 29, 4, 29, 3, 5, 3, 1, 141, 1, 2, 7, 7, 2, 2, 7, 1, 1, 7, 1, 7, 1, 2, 4, 1, 1, 1, 30, 1, 12, 4, 18, 10, 2, 8, 1, 2, 2, 2, 4,
13, 1, 5, 4, 1, 6, 1, 1, 11, 2, 4, 2, 1, 1, 3, 3, 12, 1, 1, 39, 5, 1, 1, 16, 125, 1, 4, 1, 2, 1, 19, 1, 4, 1, 1, 2, 1, 4, 1, 10, 1, 4, 2, 1, 1, 1, 5, 10, 4, 14, 1, 13, 41, 1, 4, 1, 8, 1, 1, 2, 1, 3, 1, 6, 1, 3, 2, 2, 2, 1, 4, 1, 14, 1, 2, 8, 1, 8, 3, 3, 3, 1, 37, 4, 2, 4, 1, 3, 4, 25, 4, 27, 2, 7, 1, 1, 2, 6, 1, 1,
1, 12, 1, 2, 2, 2, 13, 12, 1, 3, 1, 6, 1, 1, 33, 1, 5, 3, 1, 5, 15, 8, 8, 47, 1, 3, 2, 12, 2, 12, 1, 12, 1, 2, 5, 3, 1, 1, 1, 1, 2, 3, 5, 4, 2, 1, 1, 5, 1, 9, 14, 1, 1, 3, 2, 1, 9, 3, 22, 13, 1, 1, 3, 20, 1, 1, 61, 1, 376, 2, 107, 1, 10, 3, 2, 2, 31, 1, 2, 10, 2, 2, 62, 2, 2, 7, 4, 5, 6, 1, 1, 1, 1, 2, 8, 2, 73, 3, 5, 42,
1, 3, 2, 1, 1, 59, 6, 1, 1, 1, 5, 1, 6, 1, 2, 6, 1, 1, 1, 1, 3, 2, 1, 3, 1, 8, 1, 4, 2, 5, 4, 7, 1, 4, 2, 2, 6, 1, 1, 2, 2, 1, 1, 1, 1, 1, 2, 1, 2, 2, 5, 1, 2, 1, 1, 10, 1, 6, 1, 129, 1, 4, 65, 2, 4, 4, 3, 2, 3, 1, 1, 5, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1, 1, 2, 2, 1, 2, 3, 1, 2, 1, 2, 4, 2, 1, 2, 27, 6, 2, 1,
193, 1, 3, 9, 1, 3, 35, 2, 1, 8, 1, 1, 1, 1, 9, 3, 56, 1, 6, 6, 2, 8, 1, 8, 1, 2, 3, 6, 3, 1, 3, 1, 1, 1, 2, 13, 1, 1, 1, 1, 13, 2, 1, 3, 1, 3, 15, 2, 1, 1, 2, 4, 1, 4, 5, 2, 2, 1, 2, 1, 6, 1, 4, 12, 1, 1, 1, 1, 13, 1, 3, 4, 1, 1, 1, 2, 9, 1, 7, 1, 1, 1, 1, 4, 1, 3, 4, 1, 1, 4, 3, 1, 39, 2, 1, 1, 1, 1, 1, 4,
7, 2, 2, 2, 1, 1, 1, 1, 2, 114, 12, 4, 1, 3, 2, 1, 19, 1, 1, 2, 1, 1, 3, 4, 1, 60, 3, 72, 2, 1, 1, 1, 50, 1, 1, 1, 1, 3, 1, 1, 2, 2, 1, 4, 1, 7, 3, 1, 2, 1, 5, 1, 1, 1, 2, 6, 2, 21, 2, 6, 1, 6, 1, 1, 2, 1, 7, 1, 8, 1, 1, 5, 4, 1, 1, 1, 1, 1, 1, 1, 1, 4, 1, 11, 2, 4, 10, 2, 1, 1, 13, 1, 1, 7, 15, 1, 1, 1, 2, 3,
15, 8, 8, 2, 1, 13, 3, 5, 1, 2, 1, 6, 1, 10, 123, 3, 1, 4, 59, 4, 156, 88, 1, 5, 4, 1, 3, 1, 4, 2, 9, 1, 7, 4, 2, 1, 2, 3, 2, 1, 2, 11, 1, 13, 7, 7, 1, 63, 37, 12, 86, 1, 1, 1, 1, 2, 2, 4, 2, 18, 1, 1, 1, 41, 2, 1, 1, 12, 1, 2, 1, 1, 2, 10, 1, 1, 1, 5, 1, 1, 3, 1, 7, 5, 1, 9, 1, 2, 2, 7, 1, 1, 5, 2, 1, 3, 3, 5, 2, 1,
11, 3, 1, 3, 2, 1, 1, 2, 1, 14, 5, 2, 2, 1, 1, 1, 1, 3, 1, 3, 3, 2, 2, 1, 3, 2, 1, 2, 1, 4, 1, 14, 1, 1, 58, 7, 1, 2, 1, 1, 5, 1, 2, 1, 5, 18, 1, 4, 3, 1, 1, 1, 4, 1, 1, 2, 5, 1, 148, 1, 9, 2, 1, 2, 1, 5, 4, 93, 1, 1, 2, 4, 1, 2, 73, 1, 1, 3, 1, 1, 1, 1, 2, 1, 34, 1, 5, 6, 1, 2, 1, 3, 4, 1, 16, 28, 17, 2, 5, 5,
26, 1, 1, 4, 12, 1, 3, 2, 1, 5, 1, 2, 9, 3, 2, 41, 1, 16, 2, 2, 20, 1, 17, 1, 6, 16, 3, 3, 2, 2, 2, 18, 15, 1, 1, 51, 4, 9, 5, 2, 2, 1, 2, 1, 45, 3, 1, 1, 3, 1, 2, 1, 3, 1, 1, 3, 5, 1, 2, 3, 8, 2, 47, 2, 3, 1, 1, 1, 15, 9, 1, 8, 2, 1, 4, 2, 4, 14, 1, 12, 2, 1, 161, 1, 26, 2, 1, 2, 1, 1, 1, 1, 2, 2, 1, 18, 528, 12, 4, 1,
5, 16, 3, 1, 1, 1, 1, 1, 5, 1, 2, 1, 63, 1, 97, 1, 4, 4, 10, 5, 9, 5, 2, 3, 2, 5, 7, 1, 32, 13, 1, 5, 4, 1, 7, 1, 3, 12, 1, 3, 9, 1, 7, 1, 102, 53, 1, 1, 1, 3, 4, 2, 15, 2, 8, 2, 2, 3, 1, 2, 4, 1, 1, 3, 2, 3, 1, 1, 2, 3, 1, 1, 6, 1, 1, 14, 1, 80, 11, 1, 1, 1, 1, 22, 1, 2, 3, 1, 3, 26, 2, 24, 2, 2, 4, 3, 1, 1, 1, 1,
3, 1, 63, 1, 1, 1, 25, 1, 1, 1, 8, 1, 3, 3, 1, 10, 5, 6, 2, 1, 1, 3, 1, 1, 1, 1, 2, 2, 1, 2, 8, 12, 1, 53, 1, 2, 1, 1, 5, 1, 1, 3, 1, 39, 1, 12, 1, 3, 14, 18, 9, 3, 2, 2, 2, 1, 1, 3, 1, 4, 4, 7, 1, 17, 1, 14, 1, 1, 1, 1, 3, 1, 1, 10, 1, 2, 2, 3, 1, 2, 1, 2, 2, 2, 12, 1, 3, 44, 2, 10, 1, 14, 1, 2, 1, 43, 4, 1, 7, 3,
4, 1, 1, 2, 2, 1, 34, 1, 2, 5, 8, 3, 2, 1, 2, 13, 4, 3, 2, 1, 1, 1, 1, 25, 1, 5, 1, 94, 2, 4, 3, 4, 5, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 41, 1, 5, 1, 4, 4, 1, 155, 1, 8, 1, 1, 1, 1, 4, 1, 1, 2, 9, 2, 1, 2, 1, 1, 1, 6, 23, 1, 2, 3, 5, 2, 1, 1, 1, 1, 7, 67, 5, 7, 1, 23, 3, 3, 1, 6, 1, 11, 1, 57,
1, 4, 1, 5, 1, 1, 8, 1, 1, 2, 5, 2, 10, 1, 1, 2, 1, 1, 3, 1, 2, 1, 3, 1, 11, 2, 10, 1, 4, 18, 1, 2, 3, 1, 1, 6, 3, 6, 4, 31, 3, 4, 1, 18, 3, 9, 7, 5, 1, 2, 2, 1, 7, 1, 23, 2, 217, 1, 2, 1, 4, 1, 54, 2, 196, 10, 3, 1, 32, 1, 40, 55, 1, 5, 1, 3, 3, 1, 2, 2, 1, 3, 6, 3, 16, 1, 31, 1, 5, 6, 1, 4, 42, 4, 1, 10, 1, 3, 1, 3,
3, 1, 2, 1, 1, 1, 4, 1, 13, 1, 88, 1, 1, 1, 14, 3, 27, 3, 1, 1, 16, 4, 1, 2, 4, 1, 4, 1, 1, 17, 2, 4, 1, 1, 9, 2, 1, 1, 3, 1, 1, 30, 1, 1, 3, 2, 2, 1, 1, 4, 10, 1, 7, 1, 6, 1, 35, 1, 1, 2, 3, 6, 1, 1, 2, 4, 4, 24, 1, 1, 1, 1, 1, 1, 3, 1, 1, 2, 1, 2, 1, 6, 6, 2, 1, 1, 10, 6, 4, 2, 1, 3, 9, 1, 2, 16, 1, 5, 1, 1,
)
assert len(cf_pi__prefix2001) == 2001
cf_pi__prefix2001 = cf_circumference_diameter_ratio_pi__prefix2001 = ContinuedFraction(cf_pi__prefix2001)

if __name__ == "__main__":
    pass
__all__


from seed.math.continued_fraction.continued_fraction_ops____using_LazyList import ContinuedFraction
from seed.math.continued_fraction.continued_fraction_ops____using_LazyList import *
