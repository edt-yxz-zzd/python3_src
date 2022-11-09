#__all__:goto
#定理推导:goto
#   [@[p,q::int] -> [xballot_number(q;p) == [0 <= p <= q]*(C(q+p-1;p)-C(q+p-1;p-2)) == [0 <= p <= q]*(C(q+p;p) - C(q+p;p-1)) == [0 <= p <= q]*(C(p+q;p)*(q+1-p)///(q+1))]]
#   [@[n::int] -> [区别左右的二叉树的总数囗(叶节点的总数:=n) == [n>=1]*(C(2*n-3;n-2)-C(2*n-3;n-3)) == [1<=n<3]*1 + [n>=3]*(2*C(2*n-3;n-3)///(n-2)) == [n==1]*1 + [n>=2]*(2*C(2*n-3;n-2)///n) == [n==1]*1 + [n>=2]*(C(2*n-2;n)///(n-1)) == [n>=1]*(C(2*(n-1);n-1)///n)]]
#       Catalan_number
#   [g1_xballot_number(k;q;p) == [[k>=0][q>=0][0<=p<=q+k]]*(C(q+p;p) - C(q+p;p-k-1))]
r'''[[[[[[[
##################
[[[20221103-20221104
py -m nn_ns.math_nn.numbers.ballot_number table 10
[[1], [1, 1], [1, 2, 2], [1, 3, 5, 5], [1, 4, 9, 14, 14], [1, 5, 14, 28, 42, 42], [1, 6, 20, 48, 90, 132, 132], [1, 7, 27, 75, 165, 297, 429, 429], [1, 8, 35, 110, 275, 572, 1001, 1430, 1430], [1, 9, 44, 154, 429, 1001, 2002, 3432, 4862, 4862]]
py -m nn_ns.math_nn.numbers.ballot_number series 0 0
B= 0 N0= 0
[1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]

结合律打括号不同方式的数量囗(括号对的总数) #输入>=1
区别左右的二叉树的总数囗(叶节点的总数) #输入>=1
起点(0,0)讫点(N,N)的、所有节点(x,y)满足条件[0<=x<=y<=N]的、所有边((x0,y0)->(x1,y1))满足条件[x0<=x1][y0<=y1][(x0,y0)=!=(x1,y1)]的 栅格路径的总数囗(N+1) #输入>=1 #N>=0
N:?
0:1
1:1 1
2:1 2 2
3:1 3 5 5
4:1 4 9 14 14
5:1 5 14 28 42 42
6:1 6 20 48 90 132 132
7:1 7 27 75 165 297 429 429
8:1 8 35 110 275 572 1001 1430 1430
9:1 9 44 154 429 1001 2002 3432 4862 4862
C(N;0):1...
C(N;1):0,1,2,3,...
C(N-1;0)-C(N-1;-2):1...
C(N+0;1)-C(N+0;-1):0,1,2,3,...
C(N+1;2)-C(N+1;0):-1,0,2,5,9,14,20,27,35,44
C(N+2;3)-C(N+2;1):-2,-2,0,5,14,28,48,75,110,154
    C(N+2;3):0,1,4,10,20,35,56,84
    f(N;3):   0,0,0,5,14,28,48,75,110,154
    C(.)-f(.): 0,1,4,5,6, 7, 8, 9...
N:C(N;i)
-1:1,-1,1,-1,...
0:1
1:1 1
2:1 2 1
3:1 3 3 1
4:1 4 6 4 1
5:1 5 10 10 5 1
6:1 6 15 20 15 6 1
7:1 7 21 35 35 21 7 1
8:1 8 28 56 70 56 28 8 1
9:1 9 36 84 126 126 84 36 9 1
view ../../python3_src/nn_ns/math_nn/numbers/choose.py
py -m nn_ns.math_nn.numbers.choose
>>> import nn_ns.math_nn.numbers.choose as cc
>>> c = cc.choose
C = cc.C
>>> C = cc.C
>>> C(-1,0)
1
>>> C(-1,1)
-1
>>> C(-1,2)
1
>>> C(-1,3)
-1
>>> C(-1,-1)
0
>>> C(-1,-2)
0
>>>

定理推导:[[
[g(N;i) =[def]= C(N+i-1;i)-C(N+i-1;i-2)]
???[g(N;i) == g(N;i-1)+g(N-1;i)]???
    [[proof:
    [rhs
    = g(N;i-1)+g(N-1;i)
    = C(N+i-2;i-1)-C(N+i-2;i-3)
    + C(N+i-2;i)-C(N+i-2;i-2)
    !![C(N;i)==C(N-1;i-1)+C(N-1;i)]
    = C(N+i-1;i)-C(N+i-1;i-2)
    = lhs
    ]
    DONE
    ]]
[g(N;i) == g(N;i-1)+g(N-1;i)]

@[p,q::int]:
    [xballot_number(q;p) =[def]= [0 <= p <= q]*([q==0]*1 + [q=!=0]*(xballot_number(q;p-1)+xballot_number(q-1;p)))]
[@[p,q::int] -> [q>=0] -> [-1 <= p <= q+1] -> [xballot_number(q;p) == g(q;p)]]
    [[proof:
    !![g(N;i) =[def]= C(N+i-1;i)-C(N+i-1;i-2)]
    [g(1;1) = C(1;1)-C(1;-1) = 1-0 = 1 = xballot_number(1;1)]
    [0<=q][p==q+1]:
        [g(q;p) = g(q;q+1) = C(2*q;q+1)-C(2*q;q-1) = 0 = xballot_number(q;q+1) = xballot_number(q;p)]
    [0<=q][p==-1]:
        [g(q;p) = g(q;-1) = C(q-2;-1)-C(q-2;-1) = 0-0 = 0 = xballot_number(q;-1) = xballot_number(q;p)]
    [0 <= p <= q]+归纳法:
        [xballot_number(q;p)
        !![xballot_number(q;p) =[def]= [0 <= p <= q]*([q==0]*1 + [q=!=0]*(xballot_number(q;p-1)+xballot_number(q-1;p)))]
        = (xballot_number(q;p-1)+xballot_number(q-1;p))
        = (g(q;p-1)+g(q-1;p))
        !![g(N;i) == g(N;i-1)+g(N-1;i)]
        = (g(q;p)
        ]
    DONE
    ]]
[@[p,q::int] -> [0 <= p <= q] -> [xballot_number(q;p) == g(q;p)]]
[@[p,q::int] -> [0 <= p <= q] -> [xballot_number(q;p) == C(q+p-1;p)-C(q+p-1;p-2)]]
[@[p,q::int] -> [xballot_number(q;p) == [0 <= p <= q]*(C(q+p-1;p)-C(q+p-1;p-2)) == [0 <= p <= q]*(C(q+p;p) - C(q+p;p-1)) == [0 <= p <= q]*(C(p+q;p)*(q+1-p)///(q+1))]]
    #最后两个等号，见下面:『原来以前已经有了:定理推导』
[@[q::int] -> [q>=1] -> [xballot_number(q;q-1) == xballot_number(q;q) == C(2*q-1;q)-C(2*q-1;q-2)]]
    [[proof:
    [xballot_number(q;q)
    =[p:=q]= (C(q+p-1;p)-C(q+p-1;p-2))
    = C(2*q-1;q)-C(2*q-1;q-2)
    ]
    [xballot_number(q;q-1)
    =[p:=q-1]= (C(q+p-1;p)-C(q+p-1;p-2))
    = C(2*q-2;q-1)-C(2*q-2;q-3)
    ]
    [xballot_number(q;q) - xballot_number(q;q-1)
    = (C(2*q-1;q)-C(2*q-1;q-2))
    - (C(2*q-2;q-1)-C(2*q-2;q-3))
    = (C(2*q-1;q)-C(2*q-2;q-1))
    - (C(2*q-1;q-2)-C(2*q-2;q-3))
    !![C(N;i)==C(N-1;i-1)+C(N-1;i)]
    = C(2*q-2;q)
    - C(2*q-2;q-2)
    = 0
    ]
    DONE
    ]]
[@[n::int] -> [n>=1] -> [区别左右的二叉树的总数囗(叶节点的总数:=n) == xballot_number(n-1;n-1) == (C(2*n-3;n-1)-C(2*n-3;n-3)) == (C(2*n-3;n-2)-C(2*n-3;n-3)) == [1<=n<3]*1 + [n>=3]*(2*C(2*n-3;n-3)///(n-2)) == [n==1]*1 + [n>=2]*(2*C(2*n-3;n-2)///n) == [n==1]*1 + [n>=2]*(C(2*n-2;n)///(n-1)) == [n>=1]*(C(2*(n-1);n-1)///n)]]
    [[
    [n >= 2]:
        [n >= 1][2*n>=3]
        [(C(2*n-3;n-1)-C(2*n-3;n-3))
        =(C(2*n-3;n-1)-C(2*n-3;n))
        !![n >= 1][2*n>=3]
        = II{2*n-3-(n-1)+1..=2*n-3}/II{1..=n-1}
        - II{2*n-3-(n-0)+1..=2*n-3}/II{1..=n-0}
        = II{n-1..=2*n-3}/II{1..=n-1}
        - II{n-2..=2*n-3}/II{1..=n}
        = (1 - (n-2)/n) * II{n-1..=2*n-3}/II{1..=n-1}
        = (2/n) * C(2*n-3;n-1)
        = (2*C(2*n-3;n-1)///n)
        = (2*C(2*n-3;n-2)///n)
        ]
    [n >= 3]:
        [n >= 3][2*n>=3]
        [(C(2*n-3;n-1)-C(2*n-3;n-3))
        =(C(2*n-3;n-2)-C(2*n-3;n-3))
        !![n >= 3][2*n>=3]
        = II{2*n-3-(n-2)+1..=2*n-3}/II{1..=n-2}
        - II{2*n-3-(n-3)+1..=2*n-3}/II{1..=n-3}
        = II{n..=2*n-3}/II{1..=n-2}
        - II{n+1..=2*n-3}/II{1..=n-3}
        = (n/(n-2) - 1) * II{n+1..=2*n-3}/II{1..=n-3}
        = (2/(n-2)) * C(2*n-3;n-3)
        = (2*C(2*n-3;n-3))///(n-2)
        ]
    ]]
[@[n::int] -> [区别左右的二叉树的总数囗(叶节点的总数:=n) == [n>=1]*(C(2*n-3;n-2)-C(2*n-3;n-3)) == [1<=n<3]*1 + [n>=3]*(2*C(2*n-3;n-3)///(n-2)) == [n==1]*1 + [n>=2]*(2*C(2*n-3;n-2)///n) == [n==1]*1 + [n>=2]*(C(2*n-2;n)///(n-1)) == [n>=1]*(C(2*(n-1);n-1)///n)]]
    view ../../python3_src/nn_ns/RMQ/LeftBiasedRMQ/ballot_number/Catalan_number.py
    Catalan number
    [Catalan_number(n) == C(2n, n)/(n+1) == xballot_number(n,n)]
叶节点的总数:区别左右的二叉树的总数
n:C(2*n-3;n-1)-C(2*n-3;n-3)
1:1     =C(-1;0)-C(-1;-2)=1-0
2:1     =C(1;1)-C(1;-1)=1-0
3:2     =C(3;2)-C(3;0)=3-1
4:5     =C(5;3)-C(5;1)=10-5
5:14    =C(7;4)-C(7;2)=35-21
6:42    =C(9;5)-C(9;3)=126-84
7:132   =C(11;6)-C(11;4)=462-330
8:429   =C(13;7)-C(13;5)=1716-1287
9:1430  =C(15;8)-C(15;6)=6435-5005
10:4862 =C(17;9)-C(17;7)=24310-19448
>>> [C(2*n-3,n-1)-C(2*n-3,n-3) for n in range(1,10+1)]
[1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]
>>> [C(2*n-3,n-1) for n in range(1,10+1)]
[1, 1, 3, 10, 35, 126, 462, 1716, 6435, 24310]
>>> [C(2*n-3,n-3) for n in range(1,10+1)]
[0, 0, 1, 5, 21, 84, 330, 1287, 5005, 19448]
>>>
]]定理推导

原来以前已经有了:定理推导:[[
view ../../python3_src/nn_ns/RMQ/LeftBiasedRMQ/ballot_number/ballot_number.py
view ../../python3_src/nn_ns/RMQ/LeftBiasedRMQ/ballot_number/ballot_number\ -\ 1.\ def\ ballot_number\ by\ good_paths.txt

num_paths__0_le_p_le_q(q;p)
num_paths__p_ge_0_le_q(q;p)
[num_paths__p_ge_0_le_q__some_not_0_le_p_le_q(q;p) =[def]= num_paths__p_ge_0_le_q(q;p) - num_paths__0_le_p_le_q(q;p)]
[num_paths__p_ge_0_le_q(q;p) == C(q+p;p)]
[[0<=p<=q] -> [num_paths__p_ge_0_le_q__some_not_0_le_p_le_q(q;p) == num_paths__p_ge_0_le_q(q+1;p-1) == C(q+p;p-1)]]
    [[proof:
    * [p==0]:
        [lhs == 0 == rhs]
    * [p > 0]:
        默认:[#所有(x,y)满足[0 <= x <= p][0 <= y <= q]#]
        路径:[(p,q), ...[#存在(x,y)满足[x>y]#], (0,0)]
        必有:[(p,q), ..., (m,n), ..., (0,0)]
            [0 <= n <= m <= p <= q]
        必有:[(p,q), ..., (m,m-1), ..., (0,0)]
            [0 <= 1 <= m <= p <= q]
        必有:[(p,q), ...[#所有(x,y)满足[x<=y]#], (m,m), (m,m-1), ..., (0,0)]
            [0 <= 1 <= m <= p <= q]
        一一对应，数量相等:
            <==> [(p,q), ...[#所有(x,y)满足[x<=y]#], (m,m)]++[(m,m-1), ..., (0,0)]
            <==> [(p,q), ...[#所有(x,y)满足[x<=y]#], (m,m)]++变换{(x,y) :-> (y+1,x-1)}[#关于直线[x-y==1]的镜像#]([(m,m-1), ..., (0,0)])
            <==> [(p,q), ...[#所有(x,y)满足[x<=y]#], (m,m)]++[(m,m-1), ..., (1,-1)]
            <==> [(p,q), ..., (1,-1)]
            <==> [(p-1,q+1), ..., (0,0)]
    DONE
    ]]
[[0<=p<=q] -> [xballot_number(q;p) == num_paths__0_le_p_le_q(q;p) == num_paths__p_ge_0_le_q(q;p) - num_paths__p_ge_0_le_q__some_not_0_le_p_le_q(q;p) == C(q+p;p) - C(q+p;p-1) == ((q-p+1)/(q+1))*C(q+p;p)]]
    [[
    [p > 0]:
        [C(q+p;p) - C(q+p;p-1)
        = ((q+1)/p - 1)*C(q+p;p-1)
        = ((q-p+1)/p)*C(q+p;p-1)
        ]
    [q >= 0]:
        [C(q+p;p) - C(q+p;p-1)
        = (1 - p/(q+1))*C(q+p;p)
        = ((q-p+1)/(q+1))*C(q+p;p)
        ]
    ]]


对比:
    #以前:
    [@[p,q::int] -> [xballot_number(q;p) == [0<=p<=q]*(C(p+q,p) * (q+1 - p)/(q+1))]]
    #本文件:
    [@[p,q::int] -> [xballot_number(q;p) == [0 <= p <= q]*(C(q+p-1;p)-C(q+p-1;p-2))]]
???[@[p,q::int] -> [0 <= p <= q] -> [(C(q+p-1;p)-C(q+p-1;p-2)) == (C(p+q,p)*(q+1-p)/(q+1))]]???
    [[proof:
    !![0 <= p <= q]:
    * [0 <= p <= q == 0]:
        [q == p == 0]
        [q+p-1 == -1]
        [lhs = 1-0 = 1 = rhs]
    * [0 <= p <= q =!= 0]:
        [q >= 1]
        [q+p-1 >= p >= 0]
        * [p < 2]:
            [lhs = C(q+p-1;p) -0 = [p==0]*1 + [p==1]*q]
            [rhs = (C(p+q,p) * (q+1 - p)/(q+1)) = [p==0]*1*(q+1)/(q+1) + [p==1]*(q+1)*q/(q+1) = [p==0]*1 + [p==1]*q = lhs]
        * [p >= 2]:
            [lhs
            = C(q+p-1;p) -C(q+p-1;p-2)
            = II{q..=q+p-1}/II{1..=p} -II{q+2..=q+p-1}/II{1..=p-2}
            = (q*(q+1)/(p-1)/p-1)*C(q+p-1;p-2)
            = ((q*q+q-p*p+p)/(p-1)/p)*C(q+p-1;p-2)
            = ((q+p)*(q-p+1)/(p-1)/p)*C(q+p-1;p-2)
            = (q-p+1)/p * (q+p)/(p-1)*C(q+p-1;p-2)
            = (q-p+1)/p * C(q+p;p-1)
            = (q-p+1)/(q+1) * (q+1)/p * C(q+p;p-1)
            = (q-p+1)/(q+1) * C(q+p;p)
            = rhs
            ]
    DONE
    ]]
]]原来以前已经有了:定理推导

泛化:移动对角线禁限:定理推导:[[
@[k,p,q::int]:
    [g1_xballot_number(k;q;p) =[def]= [k >= 0][q >= 0][0 <= p <= q+k]*([p==q==0]*1 + [q=!=0]*(g1_xballot_number(k;q;p-1)+g1_xballot_number(k;q-1;p)))]
@[m,w,p,q::int]:
    [g2_xballot_number(m,w;q;p) =[def]= [m >= 0][w >= 0][0 <= p <= q+w][0 <= q <= p+m]*([p==q==0]*1 + [q=!=0]*(g2_xballot_number(k;q;p-1)+g2_xballot_number(k;q-1;p)))]
    # [-m <= p-q <= w]

num_paths__rectangle(q;p)
    #without:k,m,w
num_paths__g1_miss_corner(k;q;p)
[num_paths__g1_hit_corner(k;q;p) =[def]= num_paths__rectangle(q;p) - num_paths__g1_miss_corner(k;q;p)]

[num_paths__rectangle(q;p) == C(q+p;p)]
[[[k>=0][q>=0][0<=p<=q+k]] -> [num_paths__g1_hit_corner(k;q;p) == num_paths__rectangle(q+k+1;p-k-1) == C(q+p;p-k-1)]]
    [[proof:
    路径:[(p,q), ..., (0,0)]
    (0,0) 关于直线 [x==y+k+1][#(0,-k-1)~(k+1,0)#] 的 镜像 是 (k+1,-k-1)
    <->路径:[(p,q), ..., (k+1,-k-1)]
    <->路径:[(p-k-1,q+k+1), ..., (0,0)]
    DONE
    ]]
[[[k>=0][q>=0][0<=p<=q+k]] -> [g1_xballot_number(k;q;p) == num_paths__g1_miss_corner(k;q;p) == num_paths__rectangle(q;p) - num_paths__g1_hit_corner(k;q;p) == C(q+p;p) - C(q+p;p-k-1)]]
[g1_xballot_number(k;q;p) == [[k>=0][q>=0][0<=p<=q+k]]*(C(q+p;p) - C(q+p;p-k-1))]
    [[验证:
    [k==1]:
        #q:
        0:1,1
        1:1,2,2
        2:1,3,5,5
        3:1,4,9,14,14
        4:1,5,14,28,42,42
        [g1_xballot_number(1;q;p) == [q>=0]*xballot_number(q+1;p)]
        [xballot_number(q+1;p)
        = (C(q+1+p;p) - C(q+1+p;p-1))
        = (C(q+p;p) - C(q+p;p-2))
        ]
        [g1_xballot_number(1;q;p)
        = (C(q+p;p) - C(q+p;p-1-1))
        ]
        ok!
    [k==2]:
        #q:
        0:1,1,1
        1:1,2,3,3
        2:1,3,6,9,9
        3:1,4,10,19,28,28
        4:1,5,15,34,62,90,90
        5:1,6,21,55,117,207,297,297
        6:1,7,28,83,200,407,704,1001,1001
        [117=g1_xballot_number(2;5;4)
        =?= (C(q+p;p) - C(q+p;p-2-1))
        = (C(9;4) - C(9;4-3))
        = 9*8*7*6/4/3/2 - 9
        = 9*2*7 - 9
        = 9*13
        = 117#ok
        ]
        [407=g1_xballot_number(2;6;5)
        =?= (C(11;5) - C(11;5-3))
        = 11*10*9*8*7/5/4/3/2 -55
        = 11*3*2*7 -55
        = 11*(3*2*7 -5)
        = 11*37
        = 407#ok
        ]

    ]]
[@[p,q,s::int] -> [0 <= s <= p+q] -> [g1_xballot_number(k;q;p) == sum{g1_xballot_number(k;y;x)*g1_xballot_number(k+y-x;q-y;p-x) | [x,y::int][x+y==s]}]]
    # 起讫点 中转于 完整流量 的 一个 截流点集
[@[p,q,s::int] -> [0 <= s <= p+q] -> [g1_xballot_number(k;q;p) == sum{g1_xballot_number(k;y;x)*g1_xballot_number(k+y-x;q-y;p-x) | [x,y::int][x+y==s][y>=0][0<=x<=y+k]}]]

!![g1_xballot_number(k_;q_;p_) == ([[k_>=0][q_>=0][0<=p_<=q_+k_]]*(C(q_+p_;p_) - C(q_+p_;p_-k_-1)))]
[@[p,q,s::int] -> [0 <= s <= p+q] -> [
    [g1_xballot_number(k;q;p) == sum{g1_xballot_number(k;y;x)*g1_xballot_number(k+y-x;q-y;p-x) | [x,y::int][x+y==s]}]
    [[[k>=0][q>=0][0<=p<=q+k]]*(C(q+p;p) - C(q+p;p-k-1))
    == sum{[k>=0][y>=0][0<=x<=y+k]*[k+y-x>=0][q-y>=0][0<=p-x<=q-y+k+y-x]*(C(y+x;x) - C(y+x;x-k-1))*(C(q-y+p-x;p-x) - C(q-y+p-x;p-x-(k+y-x)-1)) | [x,y::int][x+y==s]}
    == sum{[k>=0][q>=y>=0][0<=x<=y+k][x<=p<=q+k]*(C(s;x) - C(s;x-k-1))*(C(q+p-s;p-x) - C(q+p-s;p-y-k-1)) | [x,y::int][x+y==s]}
    ]
    [[[k>=0][q>=0][0<=p<=q+k]] -> [
        [(C(q+p;p) - C(q+p;p-k-1))
        == sum{[k>=0][q>=y>=0][0<=x<=y+k][x<=p<=q+k]*(C(s;x) - C(s;x-k-1))*(C(q+p-s;p-x) - C(q+p-s;p-y-k-1)) | [x,y::int][x+y==s]}
        == sum{[q>=y>=0][0<=x<=y+k][x<=p]*(C(s;x) - C(s;x-k-1))*(C(q+p-s;p-x) - C(q+p-s;p-y-k-1)) | [x,y::int][x+y==s]}
        == sum{[q>=(s-i)>=0][0<=i<=(s-i)+k][i<=p]*(C(s;i) - C(s;i-k-1))*(C(q+p-s;p-i) - C(q+p-s;p-(s-i)-k-1)) | [i::int]}
            [#
            [q>=(s-i)>=0][0<=i<=(s-i)+k][i<=p]
            = [q+i>=s>=i][0<=i<=(s+k)/2][i<=p]
            = [s-q<=i<=s][0<=i<=(s+k)/2][i<=p]
            = [max{0,s-q} <= i <= min{p,s,(s+k)/2}]
            #]
        == sum{(C(s;i) - C(s;i-k-1))*(C(q+p-s;p-i) - C(q+p-s;p+i-s-k-1)) | [i::int][max{0,s-q} <= i <= min{p,s,(s+k)/2}]}
        ]
        ]]
    ]]
[@[p,q,s::int] -> [0 <= s <= p+q] -> [
    [[[k>=0][q>=0][0<=p<=q+k]] -> [
        [(C(q+p;p) - C(q+p;p-k-1))
        == sum{(C(s;i) - C(s;i-k-1))*(C(q+p-s;p-i) - C(q+p-s;p+i-s-k-1)) | [i::int][max{0,s-q} <= i <= min{p,s,(s+k)/2}]}
        ]
        ]]
    ]]


num_paths__rectangle(q;p)
    #without:k,m,w
num_paths__g2_miss_corner(m,w;q;p)
    路径:点(p,q)->点(0,0)
    允许范围:[0<=x<=p][0<=y<=q][y<=x+m][x<=y+w]
        代入(0,0)与(p,q)，得:
            [0<=0<=p][0<=0<=q][0<=0+m][0<=0+w]
            [0<=p<=p][0<=q<=q][q<=p+m][p<=q+w]
            <==> [[m>=0][w>=0][0<=p<=q+w][0<=q<=p+m]]
    允许范围:左上角:
        * [m>=q]:
            左上角=点(0,q)
        * [0<=m<q]:
            左上角=点(0,m)~点(q-m,q)
    允许范围:右下角:
        * [w>=p]:
            右下角=点(p,0)
        * [0<=w<p]:
            右下角=点(w,0)~点(p,p-w)
num_paths__g2_hit_both_corner(m,w;q;p)
[[[m>=0][w>=0][0<=p<=q+w][0<=q<=p+m]] -> [[0<=m<q][0<=w<p][q-m-1<=w+1][p-w-1<=m+1]] -> [num_paths__g2_hit_both_corner(m,w;q;p) == [q-m-1==w+1] + [p-w-1==m+1]]]

[num_paths__g2_hit_corner(m,w;q;p) =[def]= num_paths__rectangle(q;p) - num_paths__g2_miss_corner(m,w;q;p)]

num_paths__g2_hit_both_corner(m,w;q;p)


#bug:[[[m>=0][w>=0][0<=p<=q+w][0<=q<=p+m]] -> [num_paths__g2_hit_corner(m,w;q;p) == num_paths__rectangle(p+m+1;q-m-1) + num_paths__g1_miss_corner(m;q+w+1;p-w-1) == C(q+p;q-m-1) + [[m>=0][q+w+1>=0][0<=p-w-1<=q+w+1+m]]*(C(q+p;p-w-1) - C(q+p;p-w-1-m-1)) == C(q+p;q-m-1) + [w+1<=p<=q+2*w+2+m]*(C(q+p;p-w-1) - C(q+p;p-w-2-m)) == (C(q+p;q-m-1) + C(q+p;p-w-1) - C(q+p;p-w-2-m))]]
#   意图:过左上角+过右下角而不过左上角
#   但实际表达式为:过左上角+过右下角且之后不过左上角(之前可能已经经过左上角)
#   这样结果应该变大，为何下面验证确反而变小？
#       没错，hit变大，miss变小

#bug:继承性:[[[m>=0][w>=0][0<=p<=q+w][0<=q<=p+m]] -> [g2_xballot_number(m,w;q;p) == num_paths__g2_miss_corner(m,w;q;p) == num_paths__rectangle(q;p) - num_paths__g2_hit_corner(m,w;q;p) == (C(q+p;p) +C(q+p;p-w-2-m) -C(q+p;q-m-1) -C(q+p;p-w-1))]]
#bug:继承性:[g2_xballot_number(m,w;q;p) == [[m>=0][w>=0][0<=p<=q+w][0<=q<=p+m]]*(C(q+p;p) +C(q+p;p-w-2-m) -C(q+p;q-m-1) -C(q+p;p-w-1))]
    bug:C(q+p;p-w-2-m)不对称！有毛病！

    [[验证:
    [m==2][w==1]:
        #q:
        0:1,1
        1:1,2,2
        2:1,3,5,5
        3:0,3,8,13,13
        4:0,0,8,21,34,34
        5:0,0,0,21,55,89,89
        6:0,0,0,0,55,144,233,233
        [144=g2_xballot_number(2,1;6;5)
        =?=(C(q+p;p) +C(q+p;p-w-2-m) -C(q+p;q-m-1) -C(q+p;p-w-1))
        =(C(11;5) +C(11;5-5) -C(11;6-3) -C(11;5-2))
        =(11*3*2*7 +1 -11*5*3 -11*5*3)
        =11*(3*2*7-5*3*2) +1
        =11*3*2*(7-5) +1
        =11*12 +1
        =133#bug!
        ]
    ]]
???[[[m>=0][w>=0][0<=p<=q+w][0<=q<=p+m]] -> [
    [num_paths__g2_hit_both_corner(m,w;q;p)
    == num_paths__g2_hit_corner(m+2*w,m;q+w+1;p-w-1)
    == num_paths__g2_hit_corner(w+2*m,w;p+m+1;q-m-1)
    ]
    [num_paths__g2_hit_corner(m,w;q;p)
    == num_paths__rectangle(p+m+1;q-m-1) + num_paths__rectangle(q+w+1;p-w-1) - num_paths__g2_hit_both_corner(m,w;q;p)
    == num_paths__rectangle(q;p) - num_paths__g2_miss_corner(m,w;q;p)
    == num_paths__rectangle(p+m+1;q-m-1) + num_paths__g2_miss_corner(m+2*w,m;q+w+1;p-w-1)
    ]
    [num_paths__g2_miss_corner(m,w;q;p)
    == num_paths__rectangle(q;p) - num_paths__rectangle(p+m+1;q-m-1) - num_paths__g2_miss_corner(m+2*w,m;q+w+1;p-w-1)
    == C(q+p;p) - C(q+p;q-m-1) - num_paths__g2_miss_corner(m+2*w,m;q+w+1;p-w-1)
    == C(q+p;p) - C(q+p;q-m-1) - [[w+1<=p][q<=p+m-2]]*num_paths__g2_miss_corner(m+2*w,m;q+w+1;p-w-1)
        [#
        [[m>=0][w>=0][0<=p<=q+w][0<=q<=p+m]]:
            [[m+2*w>=0][m>=0][0<=p-w-1<=q+w+1+m][0<=q+w+1<=p-w-1+m+2*w]]
                <==>[[w+1<=p<=q+2*w+2+m][-w-1<=q<=p-2+m]]
                <==>[[w+1<=p][q<=p+m-2]]
        #]
    == (C(q+p;p) - C(q+p;q-m-1) - [[w+1<=p][q<=p+m-2]]*(C(q+p;p-w-1) - C(q+p;q+w+1-m-2*w-1) - [[m+1<=p-w-1][q+w+1<=p-w-1+m+2*w-2]]*num_paths__g2_miss_corner(m+2*w+2*m,m+2*w;q+w+1+m+1;p-w-1-m-1)))

    == (C(q+p;p) - C(q+p;q-m-1) - [[w+1<=p][q<=p+m-2]]*(C(q+p;p-w-1) - C(q+p;q-m-w) - [[m+w+2<=p][q<=p+m-4]]*num_paths__g2_miss_corner(3*m+2*w,m+2*w;q+w+2+m;p-w-2-m)))
    ]
    ]]



]]定理推导
]]] #20221103-20221104
##################
[[[20221104-?
边界条件 + 递推关系 ==>> 泛化边界:[[
    * binomial_number=C:[[
        * 边界条件:
            [@[n::int] -> [n>=0] -> [C(n,0)==1]]
            [@[n::int] -> [n>=0] -> [C(n,n+1)==0]]
        * 递推关系:
            [@[n,k::int] -> [C(n,k) == C(n-1,k-1) + C(n-1,k)]]
            # 互推 小三角:
                *-*
                 \|
                  *
        * 泛化边界:
            !! [互推 小三角 <==> 泛化边界 大三角]
            !! [有定义边界 {(n,0) | [n>=0]} 突破 大三角 斜边]
            !! [有定义边界 {(n,n+1) | [n>=0]} 突破 大三角 纵边]
            [只剩 大三角 横边{(0,k) | [k::int]}]
            [C(n,k) 定义域 为 [n>=0][k::int]]
        ]]
    * gxballot_number=G:[[
        #不是 xballot_number
        #按 互推 小三角 泛化，而非 置零
        * 边界条件:
            [@[n::int] -> [n>=0] -> [G(n,0)==1]]
            [@[n::int] -> [n>=0] -> [G(n,n+1)==0]]
            # G 与 C 的 边界条件 完全相同
        * 递推关系:
            [@[n,k::int] -> [G(n,k) == G(n,k-1) + G(n-1,k)]]
            # 互推 小三角:
                  *
                 /|
                *-*
        * 泛化边界:
            !! [互推 小三角 <==> 泛化边界 大三角]
            !! [有定义边界 {(n,0) | [n>=0]} 突破 大三角 横边]
            !! [有定义边界 {(n,n+1) | [n>=0]} 突破 大三角 纵边]
            [只剩 大三角 斜边{(n,-n) | [n::int]}]
            [G(n,k) 定义域 为 [n,k::int][n+k>=0]]
        ]]
    ]]
递推关系 变形:[[
    [@[n,k::int] -> [A(n,k) == A(n-1,k-1) + A(n-1,k)]]
    [@[n,k::int] -> [B(n,k) == B(n,k-1) + B(n-1,k)]]
    # 考虑:从A变到B
    [A(n,k) == B(n-k,k)]:
        [A(n+k,k) == B(n,k)]
        !! [B(n,k) == B(n,k-1) + B(n-1,k)]
        [A(n+k,k) == A(n+k-1,k-1) + A(n+k-1,k)]
        [A(n,k) == A(n-1,k-1) + A(n-1,k)]
    [A(n,k) 的 边界条件 与 C(n,k)相同]:[[
        A(n,k) 的 边界条件:
            [@[n::int] -> [n>=0] -> [A(n,0)==1]]
            [@[n::int] -> [n>=0] -> [A(n,n+1)==0]]
        B(n,k) 的 边界条件:
            [@[n::int] -> [n>=0] -> [B(n,0)==1]]
            [@[n::int] -> [n>=0] -> [B(-1,n+1)==0]]
        ]]
    [B(n,k) 的 边界条件 与 G(n,k)相同]:[[
        B(n,k) 的 边界条件:
            [@[n::int] -> [n>=0] -> [B(n,0)==1]]
            [@[n::int] -> [n>=0] -> [B(n,n+1)==0]]
        A(n,k) 的 边界条件:
            [@[n::int] -> [n>=0] -> [A(n,0)==1]]
            [@[n::int] -> [n>=0] -> [A(2*n+1,n+1)==0]]
        ]]
    ]]
]]] #20221104-?


##################
##################

xballot_number(q,p) = ballot_number(p,q)
    | 0 <= p <= q != 0  = ballot_number(p-1,q) + ballot_number(p,q-1)
    | 0 == p == q       = 1
    | otherwise         = 0

##################

# what if : {+w0,+w1..., -h0,-h1,...}; B<=partial_sum<=U;

seq of {+w, -h}, [ZZ w,h], but assume gcd(w,h)=1, w>0, h>0, below if not specified
L = sum(seq) maybe <= 0
partial_sum(seq) >= B, that is sum(seq[:i])>=B for i>0
    w >= [w or -h] = sum(seq[0:1]) >= B
    L = sum(seq) >= B
    B may <= 0
B <= min(w,L)


S +w's and T -h's
S*w - T*h = sum(seq) = L

N = len(seq) = S+T >= 0
let m = w+h
N(n) = N0+m*n, [NN n]
    S+T = N
    S*w - T*h = L ; S = (T*h+L)/w
    w*N-L = (w+h)T ==>> T=(w*N-L)/(w+h) >= 0 ==>> N>=L/w
    h*N+L = (w+h)S ==>> S=(h*N+L)/(w+h)
    T*h == -L mod w ==>> T == -L*h^-1 mod w
    T*h >= 0
    T0 = (-L*h^-1 mod w)
    N0 = (m*T0+L)/w
    S0 = (T0*h+L)/w !!!!! != ((-L mod w*h)+L)/w = ceil(L/w/h)*h
    NOTE: T0*h = (-L*h^-1 mod w)h != (-L mod w*h)
        T0*h = (-L*(h^-1 mod w) mod w)h = (-L*h(h^-1 mod w)) mod (w*h)
    S*w == L mod h ==>> S == L*w^-1 mod h
    S*w = L + T*h >= L
    ?? x: [x*w >= x0; x == r mod M; w>0]:
        x = a*M+r
        a*M*w+r*w >= x0
        a*M*w >= x0-r*w
        a >= (x0-r*w + M*w-1)//(M*w)
        x >= (x0-r*w + M*w-1)//(M*w) M + r
    S >= S0 = (L-(L*w^-1 mod h)*w + h*w-1)//(h*w) *h + (L*w^-1 mod h)
    [L < w+h]: S0 = (L*w^-1 -1 mod h) + 1 # see below


    w=7 h=3 m=10
    L=5
    7S-3T=5
    h^-1 mod w = 1/3 mod 7 = 5
    T0 = -5*5 mod 7 = 3
    N0 = 35/7 = 5
    S0 = 2; T0*h=9 != (-L mod w*h)=16


number of such seq
X(w,h,L,B, N) = [N>=0][L=S*w+T*(-h)][N=S+T][NN S,T][N=0 or B<=min(L,max(w,-h))] X(w,h,L,B, N)
    = X(-h,-w, L,B, N)
    [L=S*w-T*h][N=S+T] = [w+h!=0][S=(h*N+L)/(w+h)][T=(w*N-L)/(w+h)] + [w+h=0][L=w*N]


if not [N>=0]([w+h!=0][S=(h*N+L)/(w+h)][T=(w*N-L)/(w+h)][NN S,T] + [w+h=0][L=w*N])[N=0 or B<=min(L,max(w,-h))]:
    X(w,h,L,B, N) = 0
elif [N=0]:
    X(w,h,L,B, N) = [L=0]
elif [w=-h]:
    X(w,h,L,B, N) = [L=w*N][B<=min(L,w)]
elif [w*h <= 0][w<-h]:
    X(w,h,L,B, N) = [B<=L]([B<=w]C(N,T) + [w<B<=-h]C(N-1,T-1))
elif [w*h <= 0][w>-h]:
    X(w,h,L,B, N) = [B<=L]([B<=-h]C(N,T) + [-h<B<=w]C(N-1,T))
elif [w<0][h<0]:
    let X(w,h,L,B, N) = X(-h,-w,L,B, N)
elif [w>0][h>0][g = gcd(w,h) > 1]:
    g = gcd(w,h) > 1:
    X(w,h,L,B, N) = X(w/g,h/g,L/g,B/g, N) = X(w/g,h/g,L/g,ceil(B/g), N)
elif [w>0][h>0][gcd(w,h)=1]:
    [N>0]:
        X(w,h,L,B, N) = [B<=w]X(w,h,L-w,B-w, N-1) + [B<=-h]X(w,h,L+h,B+h, N-1)
        [-h<B<=w]: X(w,h,L,B, N) = X(w,h,L-w,B-w, N-1)
        [-w-h<B-w<=0]: X(w,h,L-w+w,B-w+w, N) = X(w,h,L-w,B-w, N-1)
    [-w-h<B<=0]: X(w,h,L,B, N) = X(w,h,L+w,B+w, N+1) # (n0,k0)->(n0-1,k0)
    X(w,h,L,B, N) = [N=0][L=0]+[B<=w]X(w,h,L-w,B-w, N-1) + [B<=-h]X(w,h,L+h,B+h, N-1)

    [B<=-T*h]: X(w,h,L,B, N) = C(N,T)

assume [w>0][h>0][gcd(w,h)=1]:

[N<0]: X(w,h,L,B, N)=0
[N=0]: X(w,h,L,B, 0)=[L=0]  # even for B>w, B>L
[B>w]+[B>L]: X(w,h,L,B, N)=[N=0][L=0]


def FX(w,h,L,B, z) = sum X(w,h,L,B, i)*z**i {NN i}




[B>w]+[B>L]:
    X(w,h,L,B, N) = [N=0][L=0]
    FX(w,h,L,B, z) = [L=0]
[B=w]:
    X(w,h,L,w, N) = [N>0]X(w,h,L-w,0, N-1) + [N=0][L=0]
        = X(w,h,L-w,0, N-1) + [N=0][L=0]
    FX(w,h,L,w, z) = z*FX(w,h,L-w,0, z) + [L=0]
    if L<B=w:
        left = [L=0] =?= right = z*[L-w=0] + [L=0] = [L=0]= left; yes
[B<w]:
    [N>0][B<L]:
        X(w,h,L,B, N) = X(w,h,L,B+1, N) + sum X(w,h,B+h,B+1,N'-1)*X(w,h,L-B,0,N-N') {N'}
    [N>0][B=L]: right= [N=0][L=0] + sum ... = 0 + sum; yes
    [N>0][B>L]: left=[N=0][L=0]=0 =?= right= 0+sum ?*[L-B=0][N-N'=0] {} = 0; yes
    [N=0]: left=[L=0] =?= right=[L=0] + sum X(...,N'-1)*X(...,0-N') {N'}
        = [L=0] + 0 ; yes
    [N<0]: left = 0 = right ; yes
    FX(w,h,L,B, z) = FX(w,h,L,B+1, z) + z*FX(w,h,L-B,0, z)*FX(w,h,B+h,B+1, z)



    [0<=B<w]:
        X(w,h,L,B, N) = X(w,h,L-w,B-w, N-1) + [N=0][L=0]
        assume B<0???
    [B<0]:
        [N>0][B<L]:
            X(w,h,L,B, N) = X(w,h,L,B+1, N) + sum X(h,w,-B,1,N')*X(w,h,L-B,0,N-N') {N'}
        [N>0][B=L]: right = [N=0][L=0] + sum ... ; yes
        [N>0][B>L]: left=[N=0][L=0]=0 =?= right= 0+sum ?*[L-B=0][N-N'=0] {} = 0; yes
        [N=0]: left=[L=0] =?= right=[L=0] + X(h,w,-B,1,0)*X(w,h,L-B,0,0)
            = [L=0] + [-B=0][L-B=0] = [L=0]; yes since B<0
        [N<0]: left = 0 = right ; yes
    [0<=B<=w]: FX(w,h,L,B, z) = z*FX(w,h,L-w,B-w, z) + [L=0]
    [B<0]: FX(w,h,L,B, z) = FX(w,h,L,B+1, z) + FX(w,h,L-B,0, z)*FX(h,w,-B,1, z)
        = sum FX(w,h,L-b,0, z)*FX(h,w,-b,1, z) {b=B..-1} + FX(w,h,L,0, z)
        = sum FX(w,h,L-b,0, z)*FX(h,w,-b,1, z) {b=B..0}




    FX(w,h,L,B, z) = FX(w,h,L,B+1, z) + z*FX(w,h,L-B,0, z)*FX(w,h,B+h,B+1, z)
    [B=w]:
        left= z*FX(w,h,L-w,0, z) + [L=0]
        right= [L=0] + z*FX(w,h,L-B,0, z)[B+h=0] = [L=0] != left !!!!!
    [B>w]:
        left= [L=0] =?= right= [L=0]+z*FX(w,h,L-B,0, z)[B+h=0] = [L=0]; yes
    FX(w,h,B+h+q,B+d, z) = FX(w,h,B+h+q,B+d+1, z) + z*FX(w,h,h-(d-q),0, z)*FX(w,h,B+h+d,B+d+2, z)
    G(q,d)=FX(w,h,B+h+q,B+d, z); K(i)=z*FX(w,h,h-i,0, z)
    G(q,d) = G(q,d+1)+K(d-q)*G(d,d+2) for [B+d<w] <==> [d<w-B]
    G(q,d+1) = G(q,d+2)+K(d+1-q)*G(d+1,d+1+2)
    G(q,w-B-1) = G(q,w-B)+K(w-B-1-q)*G(w-B-1,w-B+1)
    G(q,d) = G(q,w-B)+ sum K(i-q)G(i,i+2) {i=d->w-B}
        = G(q,w-B)+ sum K(i+d-q)G(i+d,i+d+2) {i=0->w-B-d} for [d<=w-B]
    G(q,w-B) = FX(w,h,B+h+q,w, z) = z*FX(w,h,B+h+q-w,0, z) + [B+h+q=0]
        = z*G(q-w,-B) + [q=-(B+h)]
    [d>w-B]: G(q,d)=FX(w,h,B+h+q,>w, z)=[B+h+q=0]=[q=-(B+h)]

    G(i,i+c) = G(i,i+c+1)+K(c)*G(i+c,i+c+2) for [i+c<w-B]
    H(q,d,c) = sum K(i-q)G(i,i+c) {i+c=d+c..w-B}
        # H(q,d,c=2) = G(q,d)-G(q,w-B)-K(w-B-1-q)G(w-B-1,w-B-1+2)
        = sum ... {i+c=d+c..w-B-1} + [d+c<=w-B]K(i-q)G(i,i+c)|:i+c=w-B
        = ... + [d+c<=w-B]K(w-B-c-q)G(w-B-c,w-B)
        = sum K(i-q)G(i,i+c) {i+c=d+c..w-B-1} + ...
        = sum K(i-q)G(i,i+c+1) + K(i-q)K(c)*G(i+c,i+c+2) {i+c=d+c..w-B-1} + ...
        = sum K(i-q)G(i,i+c+1) {i+c=d+c..w-B-1} + sum K(i-q)K(c)*G(i+c,i+c+2) {i+c=d+c..w-B-1} + ...
        = sum K(i-q)G(i,i+c+1) {i+c+1=d+c+1..w-B} + ... + ...
        = H(q,d,c+1) + ... + ...
        = ... + sum K(i-q)K(c)*G(i+c,i+c+2) {i+c=d+c..w-B-1} + ...
        = ... + K(c)*sum K(i-c-q)G(i,i+2) {i=d+c..w-B-1} + ...
        = ... + K(c)*sum K(i-c-q)G(i,i+2) {i+2=(d+c)+2..w-B-1+2} + ...
        = ... + K(c)*sum K(i-(c+q))G(i,i+2) {i+2=(d+c)+2..w-B} + [d+c+2<=w-B+1]K(c)K(i-(c+q))G(i,i+2)|:i+2->w-B+1 + ...
        = ... + K(c)*H(c+q,d+c,2)+ [d+c+2<=w-B+1]K(c)K(w-B-1-(c+q))G(w-B-1,w-B-1+2) + ...
        = ... + ...+ [d+c+2<=w-B+1]K(c)K(w-B-1-(c+q))[w-B-1=-(B+h)] + ...
        = ... + ...+ [d+c<=w-B-1]K(c)K(w-B-1-(c+q))[w+h-1=0] + ...
        = ... + ...+ 0 + ...
        = H(q,d,c+1) + K(c)*H(c+q,d+c,2) + [d+c<=w-B]K(w-B-c-q)G(w-B-c,w-B)
    let t(q,c) = K(w-B-c-q)G(w-B-c,w-B)
    [d+c>w-B]: H(q,d,c) = 0
    [d+c=w-B]: H(q,d,c) = K(w-B-c-q)G(w-B-c,w-B)
    [d+c<=w-B]: H(q,d,c) = H(q,d,c+1) + K(c)*H(c+q,d+c,2) + t(q,c)
        sum H(q,d,c+i) {i=0..w-B-(d+c)} = sum H(q,d,c+1+i) + K(c+i)*H(c+i+q,d+c+i,2) + t(q,c+i) {i=0..w-B-(d+c)}
            = sum H(q,d,c+1+i) {i=0..w-B-(d+c)} + sum K(c+i)*H(c+i+q,d+c+i,2) + t(q,c+i) {i=0..w-B-(d+c)}
            = sum H(q,d,c+i) {i=1..w-B-(d+c)+1} + ...
        H(q,d,c)- H(q,d,c+w-B-(d+c)+1) = ...
        H(q,d,c)-0 = sum K(c+i)*H(c+i+q,d+c+i,2) + t(q,c+i) {i=0..w-B-(d+c)}
            = sum K(c+i)*H(c+i+q,d+c+i,2) {NN i} + sum t(q,c+i) {i=0..w-B-(d+c)}
    let T(q,d,c) = sum t(q,c+i) {i=0..w-B-(d+c)} # = 0 if d+c>w-B
    H(q,d,c) = sum K(c+i)*H(q+c+i,d+c+i,2) {NN i} + T(q,d,c)
    H(q,d,2) = sum K(2+i)*H(2+q+i,2+d+i,2) {NN i} + T(q,d,2)
    let TT(q,p) = T(q,q+p,2); T(q,d,2) = TT(q,d-q)
    let HH(q,p) = H(q,q+p,2); H(q,d,2) = HH(q,d-q)
    HH(q,d-q) = sum K(2+i)*HH(2+q+i,d-q) {NN i} + TT(q,d-q)
    HH(q,d) = sum K(2+i)*HH(2+q+i,d) {NN i} + TT(q,d)
        = sum K(2+i)*sum K(2+j)*HH(2+2+q+i+j,d) {NN j}
            + K(2+i)*TT(2+q+i,d) {NN i} + TT(q,d)
        = sum sum K(2+i)*K(2+j)*HH(2+2+q+i+j,d) {NN j} {NN i}
        + sum K(2+i)*TT(2+q+i,d) {NN i} + TT(q,d)
        = sum sum K(2+i)*K(2+j)*sum K(2+k)*HH(2+2+2+q+i+j+k,d) {NN k} {NN j} {NN i}
        + sum sum K(2+i)*K(2+j)* TT(2+2+q+i+j,d) {NN j} {NN i} + ... + ...
        = sum^U II K(2+i[u]) {u} * HH(2*U+q+sum i[u] {u}, d) {i[u]}^U
        + sum sum^v II K(2+i[u]) {u=1..v} TT(2*v+q+sum i[u] {u=1..v},d) {i[u]}^v {v=0..U-1}
        [U large enough]:
        = 0 + ...






[B<=L]: X(w,h,L,B, N) = [0<B<=w][N>0]X(h,w,w-L,B-L, N-1) + [B>0][N=0][L=0] + [B<=0]X(h,w,-L,B-L, N)
    [B<=0]: X(w,h,L,B, N) = X(h,w,-L,B-L, N) # NOTE:B-L<=0
        [-w-h<B-L<=0]:
            # <==> L-B>w+h <==> B <= L < B+w+h
            = X(h,w,-L+h,B-L+h, N+1)
            # B-L+h <= 0 ==>> L>=B+h
            = X(w,h,L-h,B, N+1)
    [B<=0][B+h <= L < B+w+h]: X(w,h,L,B, N) = X(w,h,L-h,B, N+1) # (n,k)->(n,k+1)
    [-w-h<B<=w][B <= L < B+w+h]:
        B->-w+1..0; L -> B..B+h-1 -> 1-w..h-1;
        B+w->1..w; L+w-> 1..w+h-1
        br = (B mod w); B=br+w*bq; br = B-w*bq
        lbr = L-B mod h; L-B=lbr+h*lbq; B+lbr=L-h*lbq
        X(w,h,L,B, N) = X(w,h,L-h*lbq,B, N+lbq)
            = X(w,h,L-h*lbq-w*bq,br, N+lbq-bq)
            = X(w,h,B+lbr-w*bq,br, N+lbq-bq)
            = X(w,h,lbr+br,br, N+lbq-bq)
            = X(w,h,(L-B mod h)+(B mod w),(B mod w), N+lbq-bq)



# X(w,h,L,B, N) = [N=0][L=0]+[B<=w]X(w,h,L-w,B-w, N-1) + [B<=-h]X(w,h,L+h,B+h, N-1)
FX(w,h,L,B, z) = [L=0] + [B<=w]z*FX(w,h,L-w,B-w, z) + [B<=-h]z*FX(w,h,L+h,B+h, z)
    [-h<B<=w]: FX(w,h,L,B, z) = [L=0] + z*FX(w,h,L-w,B-w, z)

# [B<=0][B<=L]: X(w,h,L,B, N) = X(h,w,-L,B-L, N) # NOTE:B-L<=0
[B<=0][B<=L]: FX(w,h,L,B, z) = FX(h,w,-L,B-L, z)
    [-h<B<=w][B<=L]:
        FX(w,h,L,B, z) = [L=0] + z*FX(w,h,L-w,B-w, z)
            = [L=0] + z*FX(h,w,-(L-w),(B-w)-(L-w), z)
            = [L=0] + z*FX(h,w,w-L,B-L, z)
    [-h<B<=w][B<=L]: FX(w,h,L,B, z) = [L=0] + z*FX(h,w,w-L,B-L, z)
    [-h<B+w-L<=w][B+w-L<=w-L]: FX(w,h,w-L,B+w-L, z) = [w-L=0] + z*FX(h,w,w-(w-L),(B+w-L)-(w-L), z)
    [-w-h<B-L<=0][B<=0]: z*FX(w,h,L,B, z) = FX(h,w,h-L,B+h-L, z) - [h-L=0]

    [B<=0][B<=L][-w<B-L<=h]: FX(w,h,L,B, z) = FX(h,w,-L,B-L, z)
        = [-L=0] + z*FX(h,w,-L-h,B-L-h, z)
        = [L=0] + z*FX(w,h,L+h,B, z)
    [B<=0][L-w<B<=L]: FX(w,h,L,B, z) = [L=0] + z*FX(w,h,L+h,B, z)




###################################
FX(w,h,L,B, 0) = [L=0]
[B>w]+[B>L]: FX(w,h,L,B, z) = [L=0]
[B<0]: FX(w,h,L,B, z) = FX(w,h,L,B+1, z) + FX(h,w,-B,1, z)*FX(w,h,L-B,0, z)
FX(w,h,L,B, z) = [L=0] + [B<=w]z*FX(w,h,L-w,B-w, z) + [B<=-h]z*FX(w,h,L+h,B+h, z)
    [-h<B<=w]: FX(w,h,L,B, z) = [L=0] + z*FX(w,h,L-w,B-w, z)
[B<=0][B<=L]: FX(w,h,L,B, z) = FX(h,w,-L,B-L, z)
    [L>=0]: FX(w,h,L,0, z) = FX(h,w,-L,-L, z)
    [B<=0]: FX(w,h,0,B, z) = FX(h,w,0,B, z)
    FX(w,h,0,0, z) = FX(h,w,0,0, z)
    [B<=0][L-w<B<=L]: FX(w,h,L,B, z) = [L=0] + z*FX(w,h,L+h,B, z)

    [-h<B<=w][B<=L]: FX(w,h,L,B, z) = [L=0] + z*FX(h,w,w-L,B-L, z)
    [B<0]: FX(h,w,-B,1, z) = z*FX(w,h,h+B,1+B, z)

    [B<0]: FX(w,h,L,B, z) = FX(w,h,L,B+1, z) + FX(h,w,-B,1, z)*FX(w,h,L-B,0, z)
        = FX(w,h,L,B+1, z) + z*FX(w,h,B+h,B+1, z)*FX(w,h,L-B,0, z)
    [0<=B<w]: FX(w,h,L,B, z) = [L=0] + z*FX(w,h,L-w,B-w, z)
        = [L=0] + z*FX(w,h,L-w,B-w+1, z) + z*z*FX(w,h,B-w+h,B-w+1, z)*FX(w,h,L-B,0, z)
        = FX(w,h,L,B+1, z) + (FX(w,h,B+h,B+1, z)-[B+h=0])*z*FX(w,h,L-B,0, z)
        = FX(w,h,L,B+1, z) + z*FX(w,h,B+h,B+1, z)*FX(w,h,L-B,0, z)
    [B<w]: FX(w,h,L,B, z) = FX(w,h,L,B+1, z) + z*FX(w,h,B+h,B+1, z)*FX(w,h,L-B,0, z)










###########
FX(1,h,L,0, z)
    # [L>=0]: =?= z**L*Catalan(1+h,z**(1+h))**(L+1) where Catalan(m,z)=z*Catalan(m,z)**m+1
    # [L=0]: =?= f(h,0,z) = (z*f(h,0,z))**(1+h) + 1; yes
    # [L>=0]: =?= z*f(h,L,z) = (z*f(h,0,z))**(L+1); yes
    #
    # [B<w]: FX(w,h,L,B, z) = FX(w,h,L,B+1, z) + z*FX(w,h,B+h,B+1, z)*FX(w,h,L-B,0, z)
    = FX(1,h,L,1, z) + z*FX(1,h,h,1, z)*FX(1,h,L,0, z)
    # [-h<B<=w]: FX(w,h,L,B, z) = [L=0] + z*FX(w,h,L-w,B-w, z)
    = [L=0] + z*FX(1,h,L-1,0, z) + z*z*FX(1,h,h-1,0, z)*FX(1,h,L,0, z)
    [L=0]: = 1 + 0 + z*z*FX(1,h,h-1,0, z)*FX(1,h,0,0, z)
        = 1/(1-z*z*FX(1,h,h-1,0, z))
    [L>0]: = z*FX(1,h,L-1,0, z) + z*z*FX(1,h,h-1,0, z)*FX(1,h,L,0, z)
        = z/(1-z*z*FX(1,h,h-1,0, z)) *FX(1,h,L-1,0, z)
        = (z/(1-z*z*FX(1,h,h-1,0, z)))**L *FX(1,h,0,0, z)
    = z**L * FX(1,h,0,0, z)**(L+1) ; --------- 2
    [L=h-1]: = z**(h-1) * FX(1,h,0,0, z)**h = (FX(1,h,0,0, z)-1)/z/z/FX(1,h,0,0, z)
    ==>> FX(1,h,0,0, z) = 1+ (z*FX(1,h,0,0, z))**(1+h) ; ------- 1



FX(2,h,L,0, z) =
    # [B<w]: FX(w,h,L,B, z) = FX(w,h,L,B+1, z) + z*FX(w,h,B+h,B+1, z)*FX(w,h,L-B,0, z)
    = FX(2,h,L,1, z) + z*FX(2,h,h,1, z)*FX(2,h,L,0, z)
    = FX(2,h,L,2, z) + z*FX(2,h,h+1,2, z)*FX(2,h,L-1,0, z)
    + z*(FX(2,h,h,2, z) + z*FX(2,h,h+1,2, z)*FX(2,h,h-1,0, z))*FX(2,h,L,0, z)
    = FX(2,h,L,2, z)
    + z*FX(2,h,h+1,2, z)*(FX(2,h,L-1,0, z)+z*FX(2,h,h-1,0, z)*FX(2,h,L,0, z))
    + z*FX(2,h,h,2, z)*FX(2,h,L,0, z)
    # [-h<B<=w]: FX(w,h,L,B, z) = [L=0] + z*FX(w,h,L-w,B-w, z)
    = [L=0] + z*FX(2,h,L-2,0, z)
    + z*z*FX(2,h,h-1,0, z)*(FX(2,h,L-1,0, z)+z*FX(2,h,h-1,0, z)*FX(2,h,L,0, z))
    + z*z*FX(2,h,h-2,0, z)*FX(2,h,L,0, z)
    # let f(L) = FX(2,h,L,0, z)
    = [L=0] + z*f(L-2)
    + z*z*f(h-1)*f(L-1)
    + z*z*(z*f(h-1)*f(h-1)+f(h-2))*f(L)
    = [L=0] + z*f(L-2) + A*f(L-1) + B*f(L)
    [L=0]: = 1 + 0 + 0 + B*f(0) = 1/(1-B)
    [L=1]: = 0 + 0 + A*f(0) + B*f(1) = A/(1-B) *f(0) = A*f(0)**2
    [L>1]: = 0+ z*f(L-2) + A*f(L-1) + B*f(L) = (z*f(L-2) + A*f(L-1))*f(0)
    # let g(L) = f(L)*(1-B)**(L+1)
    g(0) = 1; g(1) = A; [L>1]: g(L) = z(1-B)g(L-2) + A*g(L-1)
    A = z*z*f(h-1); B = z*z*(z*f(h-1)*f(h-1)+f(h-2))
    [h=1]:
        f(h-1) = f(0); f(h-2)=0
        A = z*z*f(0); B=z*z*z*f(0)*f(0)
        f(0) = 1/(1-B) ==>> f(0) = B*f(0)+1 = (z*f(0))**3+1
        f(1) = A*f(0)**2 = z**2*f(0)**3
        let D = z**f(0); [L>1]: f(L) = D*f(L-2) + D**2*f(L-1)
        f(1) = D**2*f(0)
        f(2) = D*f(0) + D**2*f(1) = (D+D**4)f(0)
        f(3)/f(0) = D**3 *2 + D**6
        4|: = D**2 + D**5 *3 + D**8










[B=1][w=1]:
    u=0; N0 = L
    N = L+m*n; n=(N-L)/(h+1)
    X(1,h,L,1, N) = Catalan(n, m, L) = C(N, (N-L)/(h+1)) L/N

[B=1][L=1]:
    total(N) = C(N,T)

    S*w - T*h = L = 1 ==>> gcd(S,T) = 1
    ==>> seq has no periods
    ==>> total_ignoreshift(N) = C(N,u+w*n)/N


    [B=1][L=1] ==>> each seq has exactly one shift s.t. those conditions
    X(w,h,L,B, N) = C(N,T)/N = C(N,(w*N-L)/(w+h))/N

[B=1]([w=1]+[L=1]): X(w,h,L,1, N(n)) = C(N(n),T(n)) L/N(n)
    [w=1]: = w*Catalan(n=T, m=m/w, L=L/w) = C(N, T) L/N
    # Catalan(n, m, L) = C(m*n+L, n) L/(m*n+L)


see below:
    [0<B<=w][0<=L-B<w+h]:
        X(w,h,L,B, N) = X(h,w,w-L,B-L, N-1) = X(h,w,w+h-L,B-L+h, N)
        [B=1][L<w+h]([h=1]+[L=w+h-1]):
            X(w,h, L, 1, N) = C(N,T+1) (w+h-L)/N
            # N = (m*T0+L)/w + m*n = (m*T+L)/w = m/w*(T+1) + (L-m)/w
            = (w+h-L)w/(L-m) * Catalan(n=T+1, m=m/w, L=(L-m)/w)


X(w,h,L,0,N) = [N>=0]X(w,h,L+w,w,N+1)
    X(w,h,L,0,N) = X(w,h,L,1, N) + sum X(w,h,h,1,N'-1)*X(w,h,L,0,N-N') {N'}
    FX(w,h,L,0, z) = FX(w,h,L,1, z) + z*FX(w,h,L,0, z)*FX(w,h,h,1, z)
        = FX(w,h,L,1, z)/(1+z*FX(w,h,h,1, z))
    # [0<=B<=w]: FX(w,h,L,B, z) = z*FX(w,h,L-w,B-w, z) + [L=0]
    # [0<=B+w<=w]: FX(w,h,L+w,B+w, z) = z*FX(w,h,L,B, z) + [L+w=0]
    [-w<=B<=0]: FX(w,h,L,B, z) = FX(w,h,L+w,B+w, z)/z - [L+w=0]/z

FX(w,h,L,1, z) = ??
    [B<0]: FX(w,h,L,B, z) = FX(w,h,L,B+1, z) + FX(w,h,L-B,0, z)*FX(h,w,-B,1, z)
        FX(w,h,L,-w, z) = FX(w,h,L,-w+1, z) + FX(w,h,L+w,0, z)*FX(h,w,w,1, z)
        FX(w,h,L,-w, z) = FX(w,h,L+w,0, z)/z - [L+w=0]/z
        FX(w,h,L,-w+1, z) = FX(w,h,L+w,1, z)/z - [L+w=0]/z
    FX(w,h,L+w,0, z) = FX(w,h,L+w,1, z) + z*FX(w,h,L+w,0, z)*FX(h,w,w,1, z)
    FX(w,h,L,0, z) = FX(w,h,L,1, z) + z*FX(w,h,L,0, z)*FX(h,w,w,1, z)
    FX(h,w,w,1, z) =?= FX(w,h,h,1, z) ???????????


#]]]]]]]'''







r'''[[[[[[[
ballot_number

from (n,k) goto (0,0) (or (-1,0))
allow path are:
    (n,k)->(n,k-1)
    (n,k)->(n-1, k)
all nodes (n,k) should s.t. 0<=k<=n # two lines: k>=0; n-k>=0



B(n,k) = 1 if 0==k==n else B(n, k-1) + B(n-1, k) if 0 <= k <= n else 0

[n>=0]:
    B(n,n) = Catalan_number[n] = C(2n,n)/(n+1)
    B(n,0) = 1


extend
ex_ballot_number(w1, h1, w2, h2, n, k) # width, height
two lines: w1*n - h1*k <= 0; w2*n - h2*k >= 0;
[int w1, h1, w2, h2 >= 0][w1*h2 < w2*h1] # [h1, w2>0]
default (w1,h1) = (0,1)
(w2, h2) = (1,0) ==>> binomial
(w2, h2) = (1,1) ==>> ballot_number

[(w1,h1) = (0,1)] or [(w2, h2) = (1,0)], otherwise zero everywhere except (0,0)
these two cases are the same

redef : ex_ballot_number(w,h, n,k, n0=0,k0=0)
    one lines: w*n - h*k >= 0;


A(Area, n,k, n0,k0) = number of paths from (n,k) goto (n0,k0)
                    and [[(n',k') in path-{(n0,k0)}]-->> Area(n,k)]
    = 1 if (n,k) = (n0,k0)
    = 0 elif [not Area(n,k)]
    = 0 elif n+k <= n0+k0
    = A(Area, n,k-1, n0,k0) + A(Area, n-1,k, n0,k0) else
        = sum A(Area, n,k, i,d-i)*A(Area, i,d-i, n0,k0) {i} for [d=n0+k0..n+k]
= [(n,k)=(n0,k0)] + [n+k>n0+k0][Area(n,k)](A(Area, n,k-1, n0,k0) + A(Area, n-1,k, n0,k0))



E(w,h, n,k, n0,k0) = A(\n,k:[w*n-h*k >= 0], n,k, n0,k0)
    E(1,0, n,k, n0,k0) = E(1,0, n,k-k0, n0,0)
        = 0 if [n+k<n0+k0]
        = C(n+k-(n0+k0), n-n0) elif [n0>=0]
        = [(n,k)=(n0,k0)] + E(1,0, n,k, 0,k0)*E(1,0, 0,k0, n0,k0) else
            = [(n,k)=(n0,k0)] + E(1,0, n,k, 0,k0)[n0=-1]
    E(1,0, n,k) = [n+k>=0]C(n+k,n)


[k<k0]+[n<n0]: A(Area, n,k, n0,k0) = 0
[Area(n,k)]:
    A(Area, n,k, n-1,k) = A(Area, n,k-1, n-1,k) + A(Area, n-1,k, n-1,k) = 0+1 = 1
    A(Area, n,k, n,k-1) = A(Area, n,k-1, n,k-1) + A(Area, n-1,k, n,k-1) = 1+0 = 1
[[n'=n0..n][k'=k0..k][(n',k')!=(n0,k0)] -->> Area(n',k')]:
    A(Area, n,k, n0,k0) = E(1,0, n-n0,k-k0)
        = [n+k>=n0+k0]C(n+k-(n0+k0), n-n0)


[w*n0-h*k >= 0]:
    let Area = \n,k:[w*n-h*k >= 0]
    ==>> Area(n0,k) >= 0
    ==>> [[n'=n0..n][k'=k0..k][(n',k')!=(n0,k0)] -->> Area(n',k')]
    E(w,h, n,k, n0,k0) = E(1,0, n-n0,k-k0)
[w*n0-h*k < 0][w*n-h*k >= 0][n+k>n0+k0]:
    E(w,h, n,k, n0,k0) = sum E(w,h, n,k, i,d-i)*E(w,h, i,d-i, n0,k0) {i} for [d=n0+k0..n+k]
        = sum E(w,h, n,k, i,d-i)*E(w,h, i,d-i, n0,k0) {i:n0<=i<=n, k0<=d-i<=k} for [d=n0+k0..n+k]
        # max(n0,d-k) <= i <= min(n,d-k0)
        # if <<-- w*i-h*k>=0 <--> i >= h*k/w: then h*k/w <= max(n0,d-k)
        # ==>> n0 >= h*k/w or d >= h*k/w+k
        = sum E(w,h, n,k, i,d-i)*E(w,h, i,d-i, n0,k0) {i:d-k<=i<=min(n,d-k0)} for [d=h*k/w+k..n+k]
        = sum E(1,0, n-i,k-(d-i)) E(w,h, i,d-i, n0,k0){i>=d-k} for [d=h*k/w+k..n+k]
        = sum C(n+k-d,n-i) E(w,h, i,d-i, n0,k0){i>=d-k} for [d=h*k/w+k..n+k]
        = sum C(n+k-d,n-i) E(w,h, i,d-i, n0,k0){i} for [d=h*k/w+k..n+k]




E(w,h, n,k, n0,k0) = E(a*w,a*h, n,k, n0,k0) for [NN a > 0]
E(w,h, n,k, n0,k0) = E(w,h, n+a*h,k+a*w, n0+a*h,k0+a*w) for [ZZ a]
    E(w,h, n,k, n0,a*w+r) = E(w,h, n-a*h,k-a*w, n0-a*h,r) for [ZZ a]



E(1,0, n-n0,k-k0) = sum E(w,h, n,k, n',k')*E(1,0, n'-1-n0,k'-k0) {n',k': w*n'-h*k'>=0>w*(n'-1)-h*k'}
    0 <= w*n'-h*k' < w
    0 <= n' - h*k'/w < 1 ==>> n' = floor(h*k'/w)
    let k' = w*q+kr, n' = floor(h*kr/w) + h*q = nr+h*q, kr=0..w-1
    E(w,h, n,k, n',k') = E(w,h, n-h*q,k-w*q, nr,kr)
    E(1,0, n-n0,k-k0) = sum sum [nr=floor(h*kr/w)]
        * E(w,h, n-h*q,k-w*q, nr,kr)*E(1,0, nr+h*q-1-n0,w*q+kr-k0) {kr=0..w-1}{q}
        = sum [nr=floor(h*kr/w)]
            sum E(w,h, n-h*q,k-w*q, nr,kr)
                *[(w+h)*q+nr+kr-n0-k0-1>=0]C((w+h)*q+nr+kr-n0-k0-1,w*q+kr-k0) {q}
          {kr=0..w-1}
        = sum [nr=floor(h*kr/w)]
            sum E(w,h, n-h*q,k-w*q, nr,kr)*C((w+h)*q+nr+kr-n0-k0-1,w*q+kr-k0)
            {q>=max((n0+1-nr)/h, (k0-kr)/w)} # q<=min((n-nr)/h, (k-kr)/w)
          {kr=0..w-1}


[w>0][h>0]:
    map : (a*h,a*w) -> (0,0); (0,0) -> (a*w,a*h); (a*h,0)->(a*w,0)
        # (n,k)->(k,n) . (n,k)->(a*h-n, a*w-k) (n,k) =
        #    = (n,k)->(k,n) (a*h-n, a*w-k)
        #    = (a*w-k, a*h-n)
        # (n,k)->(k,n) . (n,k)->(a*h-n, a*w-k) = (n,k)->(a*w-k, a*h-n)
        that is map (n,k)=(a*w-k, a*h-n)
    E(w,h, a*h,a*w, n0,k0) = E(h,w, map (n0,k0), map (a*h,a*w))
        = E(h,w, (a*w-k0, a*h-n0), 0,0)
        = E(h,w, a*w-k0, a*h-n0)

    def M (n,k) = (-k,-n)
        w*n-h*k >= 0 <==> h(-k) - w*(-n) >= 0
        (n,k)->(n-1,k) vaild; (reverse (-k,-n)->(-k,1-n)) vaild
        (n,k)->(n,k-1) vaild; (reverse (-k,-n)->(1-k,-n)) vaild
        [w*n-h*k>=0][w*n0-h*k0>=0]:
            E(w,h, n,k, n0,k0) = E(h,w, -k0,-n0, -k,-n)
                left hand: last path may be (n0+1,k0)->(n0,k0)
                    after map: (-k0,-n0)->(-k0,-1-n0)
                    if [Area(w,h, n0+1,k0)][not Area(w,h, n0,k0)]:
                        then count the first 1 but second 0
                    require: not [Area(w,h, n0+1,k0)][not Area(w,h, n0,k0)]
                    = not [w(n0+1)-h*k0>=0][w*n0-h*k0<0]
                    = not [-w<= w*n0-h*k0 <0]
                right hand the same: not [-h<= h*-k-w*-n <0] = not [-h<= w*n-h*k <0]
            holds for:
                [not [n>=n0][k>=k0]*([-w<= w*n0-h*k0 <0][w*n-h*k>=0]
                                    + [-h<= w*n-h*k <0][w*n0-h*k0>=0])]



    [gcd(w,h)=1][w*n-h*k>=0][w*n0-h*k0>=-w]:
        # w*n0 >= h*k0-w; n0 >= ceil(h*k0/w)-1
        E(w,h, n,k, n0,k0) =
            seq of element in {+w, -h}, (n-n0) +w's and (k-k0) -h's
            and partial sums of seq are >= 0 -(w*n0-h*k0) = B
            = number of such seqs if [n-n0>=0][k-k0>=0] else 0

        B = -(w*n0-h*k0) <= w
        L = sum(seq) = w(n-n0) - h(k-k0)
            = (w*n-h*k)-(w*n0-h*k0) = (w*n-h*k) + B >= B
        B <= min(w,L)

        let N = (n-n0) + (k-k0)
        let (k-k0) = T=(w*N-L)/(w+h);
        let (n-n0) = S=(h*N+L)/(w+h)
        w*n-h*k = L-B;
        w*n0-h*k0 = -B; k0 == B*h^-1 mod w;
        let k0 = r + w*q; n0 = (h*r-B)/w + h*q


        E(w,h, n,k, n0,k0) = X(w,h,L,B, N)
            = X(w,h, (w*n-h*k)-(w*n0-h*k0), -(w*n0-h*k0), (n-n0) + (k-k0))
            = E(w,h, S+(h*r-B)/w + h*q, T+r + w*q, (h*r-B)/w + h*q, r + w*q)

            = E(w,h, n,k, n0,k0)
            [-w<= w*n0-h*k0 <0][w*n-h*k>=0]:
                = E(w,h, n,k, n0+1,k0)
                = E(h,w, -k0,-1-n0, -k,-n)
                    # <==> 0 < B = -(w*n0-h*k0) <= w
                    L' = -((w*n-h*k)-(w*(n0+1)-h*k0)) = w-L
                    B' = -(w*n-h*k) <= 0;
                    B'-B=L'-w=-L ==>> B'=B-L = L'+B-w <= L'
                    N' = (n-n0-1) + (k-k0) = N-1 == -1???????????
                    T' = (h*N'-L')/(w+h) = (h*N-h+L-w)/(w+h) = S-1
                    S' = (w*N'+L')/(w+h) = (w*N-w+w-L)/(w+h) = T
                    N'>=0 ==>> -1-n0>=-n ==>> n>=n0+1; N>0
                [0<B<=w][N>0]: = X(h,w,w-L,B-L, N-1) # NOTE: B-L<=0
                [0<B<=w][N=0]: = [L=0][0<B<=L] = 0

            [w*n0-h*k0 >=0][w*n-h*k>=0]:
                = E(h,w, -k0,-n0, -k,-n)
                    B = -(w*n0-h*k0) <= 0 !!!
                    L' = -((w*n-h*k)-(w*n0-h*k0)) = -L !!!!!!!!!!!!!
                    B' = -(w*n-h*k) <= 0;
                    B'-B=L'=-L ==>> B'=B-L = L'+B <= L'
                    N' = (n-n0) + (k-k0) = N
                    T' = (h*N'-L')/(w+h) = (h*N+L)/(w+h) = S
                    S' = T
                [B<=0]: = X(h,w,-L,B-L, N)

        X(w,h,L,B, N) = [0<B<=w][N>0]X(h,w,w-L,B-L, N-1) + [B<=0]X(h,w,-L,B-L, N)
            B-L = -(w*n-h*k) <= 0
            [0<B<=w]: X(w,h,L,B, N) = X(h,w,w-L,B-L, N-1)
                = [B-L<=0]X(w,h,-(w-L),(B-L)-(w-L), N-1)
                = X(w,h,L-w,B-w, N-1) # -w-h < B-w
            [-h-w< B-L <=0]:???????????????????? TODO ???????????????????????????????????
                <==> (w*n-h*k)-(w+h) = w(n-1)-h(k-1) < 0
                <==> L-B < w+h
                # [B<=0][B+h <= L < B+w+h]: X(w,h,L,B, N) = X(w,h,L-h,B, N+1)
                # [-w-h<B<=0]: X(w,h,L,B, N) = X(w,h,L+w,B+w, N+1)
                [0<B<=w][N>0]: # -w-h<B-L<=0
                    X(w,h,L,B, N) = X(h,w,w-L,B-L, N-1) = X(h,w,w+h-L,B-L+h, N)
                        = X(h,w,w+h*a-L,B-L+h*a, N-1+a) for [a>=0][B-L+h(a-1)<=0]
                        for 0 <= a <= (L-B)/h+1
                    [L=B=w]: X(w,h,w,w, N) = X(h,w, h, h, N)

            [w-L-w<B-L<=w-L][B-L<=0]: X(w,h,w-(w-L),B-L-(w-L)+w, N) = X(h,w,w-L,B-L, N-1)
                [L-w<B<=L][B<=0]: X(w,h,w-L,B-L+w, N+1) = X(h,w,L,B, N)
                [L-h<B<=L][B<=0]: X(w,h,L,B, N) = X(h,w,-L+,B-L+h, N+1)
            [B-L<=-L][B-L<=0]: X(w,h,-(-L),B-L-(-L), N) = X(h,w,-L,B-L, N)
                [B<=L][B<=0]: X(w,h,-L,B-L, N) = X(h,w,L,B, N)
            [L-w<B<=L][B<=0]: X(w,h,w-L,B-L+w, N+1) =?= X(w,h,-L,B-L, N)?? yes
            [B<=L][B<=0]: X(w,h,L,B, N) =?= X(h,w,-L,B-L, N)



        [B=1]([w=1]+[L=1]): # B=w-(w*n0-h*k0)
            <==> [w*n0-h*k0=w-1]([w=1]+[L=1])

            E(w,h, n,k, n0,k0) = X(w,h,L,B, N)
            = C(N(g),T(g)) L/N(g)
            = C(n-n0+1+k-k0, k-k0) (w+(w*n-h*k)-(w*n0-h*k0))/(n-n0+1+k-k0)

            [(n0,k0)=(0,0)]:
                ==>> w=B+0=1, L = 1+n-h*k
                E(1,h, n,k) = C(n+1+k, k) L/(n+1+k)
                    # (h+1)*k+L = n+1+k
                    = C((h+1)*k+L, k) L/((h+1)*k+L)
                    = Catalan(n=k,m=h+1,L=L)

                check: E(1,1, k,k) = Catalan(n=k, m=2, L=1) = ballot(k,k); yes

        E(g,g*h, n,k) = E(1,h, n,k)
        Catalan(n=k, m=m, L=L) = E(1,m-1, (m-1)*k+L-1,k)
        [fixed L]:
            L = +w + w(n-n0) - h(k-k0)
            w*n = h * k + (L-w + w*n0-h*k0) ==>> n = h/w * k + ()/w
            let k = w*i+kr ==>> n = h*i + (()+h*kr)/w
            let n = h*i+nr ==>> nr = (h*kr  +  L-w + w*n0-h*k0)/w
            let f i = E(w,h, h*i+nr, w*i+kr, n0,k0)

            L = +w + w(h*i+nr-n0) - h(w*i+kr-k0) = w + w(nr-n0) - h(kr-k0)
            E(w,h, h*i+nr, w*i+kr, n0,k0) = ??

[w>0][h>0]:
    g = gcd(w,h)
    E(w,h, h/g*i+nr, w/g*i+kr, n0,k0) = E(w/g,h/g, h/g*i+nr, w/g*i+kr, n0,k0) = ??
    L = +w + w(h/g*i+nr-n0) - h(w/g*i+kr-k0) = +w + w(nr-n0) - h(kr-k0)
        = (w*nr-h*kr) + w - (w*n0-h*k0)
    L/g = w/g + w/g(nr-n0) - h/g(kr-k0)

    N = (n-n0)+1+(k-k0) = (h/g*i+nr + w/g*i+kr) + 1 - (n0+k0)
        = (h+w)/g*i + (nr+kr+1) - (n0+k0)


#]]]]]]]'''


__all__ = '''
    ballot_number
    xballot_number



    XBallotNumberEx1
    XBallotNumberEx2

    direct_calc__xballot_number
    direct_calc__total_oriented_binary_tree
    '''.split()

import functools
import fractions
#from .Catalan_number import CatalanNumber
from .IXBallotNumberLike import IXBallotNumberLike
from .INumberTable import INumberTable__table__concrete_mixins
from .numbers_common import\
    (ABC, optional_method, abstract_method, override, define)
from nn_ns.math_nn.numbers.choose import C #used@direct_calc__xballot_number




def ballot_number(p, q):
    return xballot_number(q, p)


_data = [[1], [1, 1], [1, 2, 2], [1, 3, 5, 5], [1, 4, 9, 14, 14], [1, 5, 14, 28, 42, 42]
]

class _impl_XBallotNumberEx1(
        IXBallotNumberLike, INumberTable__table__concrete_mixins):
    __slots__ = '__w __h table'.split()

    @override
    def __please_add_table_to_slots__(self):pass
    @override
    def __init__(self, w, h):
        assert w > 0
        assert h > 0 # if h == 0, row_len = inf

        self.__w = w
        self.__h = h
        super().__init__([[1]])

    @override
    def row_len(self, n):
        '''w*n - h*k >= 0; k>=0; ==>> k <= w*n/h'''
        max_k = self.__w * n // self.__h
        return max_k + 1
        raise NotImplementedError()

    def _calc_pos_xballot_like(self, n, k, n_k1, n1_k):
        '''_calc_pos_xballot_like(n, k, table[n][k-1], table[n-1][k]) -> table[n][k]

'''
        return n_k1 + n1_k
        raise NotImplementedError


class _impl_XBallotNumberEx2(
        IXBallotNumberLike, INumberTable__table__concrete_mixins):
    __slots__ = '__w __h __B table'.split()

    @override
    def __please_add_table_to_slots__(self):pass
    @override
    def __init__(self, w, h, B):# n0, k0):
        assert w > 0
        assert h > 0 # if h == 0, row_len = inf

        self.__w = w
        self.__h = h
        self.__B = B # 0-(w*n0-h*k0)
        super().__init__([[1]*self.row_len(0)])

    @override
    def row_len(self, dn):
        '''w*(dn+n0) - h*(dk+k0) >= 0; dk+k0>=0;

==>> w*(dn+n0) - h*(dk+k0) = w*dn-h*dk-B >= 0
==>> 0 <= dk <= (w*dn-B)/h
'''
        max_dk = (self.__w * dn - self.__B)// self.__h
        if max_dk < 0 and dn == 0:
            max_dk = 0

        return max_dk + 1
        raise NotImplementedError()

    def _calc_pos_xballot_like(self, n, k, n_k1, n1_k):
        '''_calc_pos_xballot_like(n, k, table[n][k-1], table[n-1][k]) -> table[n][k]

'''
        return n_k1 + n1_k
        raise NotImplementedError


def to_coprime(width, height):
    fr = fractions.Fraction(width, height)
    width, height = fr.numerator, fr.denominator
    assert height > 0
    return  width, height


def XBallotNumberEx1(width = 1, height = 1):
    width, height = to_coprime(width, height)
    assert width > 0
    return _cached_XBallotNumberEx1(width, height)

@functools.lru_cache(maxsize=None, typed=False)
def _cached_XBallotNumberEx1(width, height):
    return _impl_XBallotNumberEx1(width, height)


def XBallotNumberEx2(width = 1, height = 1, B=0):
    width, height = to_coprime(width, height)
    assert width > 0
    return _cached_XBallotNumberEx2(width, height, B)

@functools.lru_cache(maxsize=None, typed=False)
def _cached_XBallotNumberEx2(width, height, B):
    return _impl_XBallotNumberEx2(width, height, B)






xballot_number = XBallotNumberEx1(1,1)
#print(xballot_number.get_first(6))
assert xballot_number.get_first(len(_data)) == _data
assert xballot_number(0,0) == 1

# Catalan(n=k, m=m, L=L) = E(1,m-1, (m-1)*k+L-1,k)
def _test(max_m=5, max_L=3, max_n=10):
    print('test: Catalan(n=k, m=m, L=L) = C(m*k+L, u) L/(m*k+L) =?= E(1,m-1, (m-1)*k+L-1,k)')
    for m in range(2, max_m+1):
        ess = XBallotNumberEx1(1, m-1)
        for L in range(1, max_L+1):
            cs = CatalanNumber(m, L)
            for k in range(max_n+1):
                #print(cs(k), ess((m-1)*k+L-1,k))
                assert cs(k) == ess((m-1)*k+L-1,k)

























#################### [[[ 20221103-20221104
#[@[p,q::int] -> [xballot_number(q;p) == [0 <= p <= q]*(C(q+p-1;p)-C(q+p-1;p-2)) == [0 <= p <= q]*(C(q+p;p) - C(q+p;p-1)) == [0 <= p <= q]*(C(p+q;p)*(q+1-p)///(q+1))]]
#[@[n::int] -> [区别左右的二叉树的总数囗(叶节点的总数:=n) == [n>=1]*(C(2*n-3;n-2)-C(2*n-3;n-3)) == [1<=n<3]*1 + [n>=3]*(2*C(2*n-3;n-3)///(n-2)) == [n==1]*1 + [n>=2]*(2*C(2*n-3;n-2)///n) == [n==1]*1 + [n>=2]*(C(2*n-2;n)///(n-1)) == [n>=1]*(C(2*(n-1);n-1)///n)]]
#def direct_calc(self, n, k):
def direct_calc__xballot_number(q, p, /):
    if not 0 <= p <= q:
        return 0
    return (C(q+p-1,p)-C(q+p-1,p-2))
    return (C(q+p,p)-C(q+p,p-1))
direct_calc__xballot_number
xballot_number
def direct_calc__total_oriented_binary_tree(n, /):
    if not n >= 1:
        return 0
    #######
    if __debug__:
        (q,r) = divmod(C(2*n-2,n-1), n)
        assert r == 0
        return q
    raise NotImplementedError
    #######
    if not n >= 2:
        return 1
    if __debug__:
        #(q,r) = divmod(2*C(2*n-3,n-2), n)
        (q,r) = divmod(2*C(2*n-3,n-1), n)
        assert r == 0
        return q
    raise NotImplementedError
    #######
    if not n >= 2:
        return 1
    if __debug__:
        (q,r) = divmod(C(2*n-2,n), (n-1))
        assert r == 0
        return q
    raise NotImplementedError
    #######
    if not n >= 2:
        return 1
    if __debug__:
        (q,r) = divmod(2*C(2*n-3,n-2), n)
        assert r == 0
        return q
    raise NotImplementedError
    #######
    if not n >= 3:
        return 1
    if __debug__:
        (q,r) = divmod(2*C(2*n-3,n-3), (n-2))
        assert r == 0
        return q
    raise NotImplementedError
    #######
    return (2*C(2*n-3,n-3)//(n-2))
def _test__direct_calc__xballot_number():
    us = range(-2, 100+1)
        #_fill_when_neg: raise NotImplementedError
    us = range(0, 100+1)
    for q in us:
        for p in us:
            assert direct_calc__xballot_number(q,p) == xballot_number(q,p)
def _test__direct_calc__total_oriented_binary_tree():
    us = range(1, 100+1)
    for n in us:
        assert direct_calc__total_oriented_binary_tree(n) == xballot_number(n-1,n-1), (n, direct_calc__total_oriented_binary_tree(n), xballot_number(n-1,n-1))
if __name__ == '__main__':
    _test__direct_calc__xballot_number()
    _test__direct_calc__total_oriented_binary_tree()
#################### ]]] 20221103-20221104


#################### cmd




class xballot_ex_number2:
    '''
diff with XBallotNumberEx2:
knows n0,k0, so use (n,k) to query instead of (dn,dk)
'''
    def __init__(self, w,h, n0,k0):
        B = 0-(w*n0-h*k0)
        self.ns = XBallotNumberEx2(w,h,B)
        self.n0 = n0
        self.k0 = k0
    def __call__(self, n,k):
        dn = n-self.n0
        dk = k-self.k0
        return self.ns(dn,dk)
    def show(self):
        print(self.ns.table)


r'''[[[[[[[
from .Pascal_number_like import PascalNumberLike
class BallotNumberLike(PascalNumberLike): # not that likely
    def _calc_pos_pascal_like(self, n, k, n1_k1, n1_k):
        n_k1 = 0 if k == 0 else self.table[n][k-1]
        return n_k1 + n1_k
        raise NotImplementedError()
    def _calc_neg(self, n, k, table):
        return 0
        raise NotImplementedError()
    def direct_calc(self, n, k):
        raise NotImplementedError()
#]]]]]]]'''


_old_print = print

def main(args=None):
    import argparse
    from pprint import pprint

    parser = argparse.ArgumentParser(description='calc ex_ballot_number')

    parser.add_argument('-pp', '--pprint', action='store_true',
                        default=False,
                        help='use pprint instead of print'
                        )
    parser.add_argument('-W', '--width', type=int, default=1,
                        help='for line w*row - h*col >= 0')
    parser.add_argument('-H', '--height', type=int, default=1,
                        help='for line w*row - h*col >= 0')
##    parser.add_argument('size', type=int, default=0, nargs='?',
##                        help='table size')

    r'''[[[[[[[
    parser.add_argument('-t', '--test', action='store_true',
                        default=False,
                        help=('test(max_m, max_L, max_n) and exit')
                        )

    parser.add_argument('-tM', '--max_m', type=int,
                        default=5,
                        help='set max_m using in test')

    parser.add_argument('-tL', '--max_L', type=int,
                        default=3,
                        help='set max_L using in test')

    parser.add_argument('-tN', '--max_n', type=int,
                        default=10,
                        help='set max_n using in test')



    parser.add_argument('-s', '--size', type=int,
                        nargs='?', default=None,
                        help='len(table); if not assign ROW, show table')
    parser.add_argument('row', type=int,
                        nargs='?', default=None,
                        help='row index')
    parser.add_argument('col', type=int,
                        nargs='?', default=None, #required=False,
                        help='colomn index')
    #]]]]]]]'''

    subparsers = parser.add_subparsers(dest='subs', help='sub-command help')
    parser_table = subparsers.add_parser('table', help='show table')
    parser_table.add_argument('size', type=int,
                              help='len(table)')

    parser_row = subparsers.add_parser('row',
                                       help='show table[row] or table[row][col]')
    parser_row.add_argument('row', type=int, help='row index')
    parser_row.add_argument('col', type=int, help='colomn index',
                            nargs='?', default=None) #required=False,


    parser_test = subparsers.add_parser('test', help='test(max_m, max_L, max_n)')

    parser_test.add_argument('max_m', type=int,
                             nargs='?', default=5,
                             help='set max_m using in test; height=m-1; width=1;')

    parser_test.add_argument('max_L', type=int,
                             nargs='?', default=3,
                             help='set max_L using in test; L=1 + w*? - h*n')

    parser_test.add_argument('max_n', type=int,
                             nargs='?', default=10,
                             help='set max_n using in test; n=0..max_n')


    parser_guess = subparsers.add_parser('guess',
        help=('print E(w,h, h/g*i+nr, w/g*i+kr) for i=0..max_i '
              'where g = gcd(w,h);'))

    parser_guess.add_argument('nr', type=int, help='set nr')
    parser_guess.add_argument('kr', type=int, help='set kr')
    parser_guess.add_argument('-I', '--max_i', type=int,
                              default=10,
                              help='len(result)-1')


    parser_series = subparsers.add_parser('series',
        help=('print X(w,h, L,B, N0+(w+h)*i) for i=0..max_i '))

    parser_series.add_argument('L', type=int, help='total sum')
    parser_series.add_argument('B', type=int, help='low bound for partial sum')
    parser_series.add_argument('-I', '--max_i', type=int,
                              default=10,
                              help='len(result)-1')




    print = oprint = _old_print

    args = parser.parse_args(args)
    #print(args)
    if args.pprint:
        print = pprint
    w,h = args.width, args.height
    ns = XBallotNumberEx1(w,h)

    subs = args.subs
##    if subs is None:
##        subs = 'table'

    if subs == 'test':
        _test(args.max_m, args.max_L, args.max_n)
    elif subs == 'table':
        print(ns.get_first(args.size))
    elif subs == 'row':
        print(ns(args.row, args.col))
    elif subs == 'guess':

        'L = (w*nr-h*kr) + w - (w*n0-h*k0)'
        'N = (h+w)/g*i + (nr+kr+1) - (n0+k0)'

        nr = args.nr
        kr = args.kr
        wg, hg = to_coprime(w,h)

        Is = list(range(args.max_i+1))
        Es = [ns(hg*i+nr, wg*i+kr) for i in Is]

        L = (w*nr-h*kr) + w
        Ns = [(hg+wg)*i + (nr+kr+1) for i in Is]
        #print(Es)
        #oprint('L={L};Ns={Ns};'.format(L=L, Ns=Ns))

        _args = dict(w=w, h=h, nr=nr, kr=kr)

        _guess(Es, L, Ns, _args)

    elif subs == 'series':
        _series(w,h, args.L, args.B, args.max_i)
    parser.exit()



def _N2ST(w,h,L, N):
    'S+T=N; S*w+T*(-h)=L;'
    S=(h*N+L)//(w+h)
    T=(w*N-L)//(w+h)
    return S,T
def _N0(w,h,L):
    for N in range(w+h):
        S,T = _N2ST(w,h,L, N)
        if S + T == N:
            assert S*w - T*h == L
            return N
    raise logic-error

def _series(w,h,L,B, max_I):
    'X(w,h,L,B,~N) = E'

    #from .. import ginvmod
    from nn_ns.math_nn.integer.mod import ginvmod

    assert w>0
    assert h>0

    N0 = _N0(w,h,L); max_N = N0+(w+h)*(max_I-1)
    S0, T0 = _N2ST(w,h,L, N0)
    t,s,g = ginvmod(h,w)
    assert g==1
    r=k0 = B*t % w
    n0 = (h*r-B)//w
    ns = xballot_ex_number2(w,h, n0,k0)
    n = S0+n0
    k = T0+k0

    print('B=', B, 'N0=', N0)

    ls = []
    for N in range(N0, max_N+1, w+h):
        #S, T = _N2ST(w,h,L, N)
        #print((n0,k0), (n,k))

        ls.append(ns(n,k))
        n += h; k+=w

    print(ls)

    r'''[[[[[[[
    let N = (n-n0) + (k-k0)
    let (k-k0) = T=(w*N-L)/(w+h);
    let (n-n0) = S=(h*N+L)/(w+h)
    w*n-h*k = L-B;
    w*n0-h*k0 = -B; k0 == B*h^-1 mod w;
    let k0 = r + w*q; n0 = (h*r-B)/w + h*q


    E(w,h, n,k, n0,k0) = X(w,h,L,B, N)
        = X(w,h, (w*n-h*k)-(w*n0-h*k0), -(w*n0-h*k0), (n-n0) + (k-k0))
        = E(w,h, S+(h*r-B)/w + h*q, T+r + w*q, (h*r-B)/w + h*q, r + w*q)
    #]]]]]]]'''

def _guess(Es, L, Ns, args):
    from sympy import factorint

    ps = [max(factorint(x) or [None]) for x in Es]
    print('args =', args)
    print('L =', L)
    print('Es =', Es)
    print('[max factor x for x in Es] =', ps)
    #print(Ns)

r'''[[[[[[[
args = {'kr': 0, 'nr': 0, 'w': 2, 'h': 3}
L = 2
Es = [1, 2, 23, 377, 7229, 151491, 3361598, 77635093,
    1846620581, 44930294909, 1113015378438]
[max factor x for x in Es] = [None, 2, 23, 29, 7229,
    50497, 45427, 77635093, 10926749, 56809, 17681]

not a term in form : II ai! / II bi!

#]]]]]]]'''


if __name__ == '__main__':
    #_test()
    main()






