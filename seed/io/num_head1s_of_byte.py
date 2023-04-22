#__all__:goto
r'''[[[
e ../../python3_src/seed/io/num_head1s_of_byte.py
seed.io.num_head1s_of_byte


py -m nn_ns.app.debug_cmd seed.io.num_head1s_of_byte
py -m nn_ns.app.adhoc_argparser__main__call8module seed.io.num_head1s_of_byte
py -m seed.io.num_head1s_of_byte

TODO:
    ByteDecoder__1s0
    ByteDecoder__201
    ByteDecoder__302x1
    ByteDecoder__312x0
  unicode 0x11_0000 共 1+5*4==21bits
    1s0   : 7*Lw   : 7,14,21    : [1..=3]
    201   : 7*Lw-2 : _,12,19,26  : [2..=4]
    302x1 : 7*Lw-4 : 6,10,17,24 : [1..=4]
    312x0 : 6*Lw-2 : 7,10,16,22 : [1..=4]
    至少对于unicode而言，优至劣次序:1s0 > 312x0 > 302x1 > 201
  =====TODO:解码 已有，接下来 是 编码


e ../../python3_src/seed/io/num_head1s_of_byte.py
  view others/数学/编程/TODO_list/整数编码.txt
      201 - 纯1前缀的长度，因为除最长外之后附加0，变成212
        11_ 0_* 10_*
        ==>> 见下面:IByteDecoder/ByteDecoder__201

  view others/数学/编程/TODO_list/整数编码-多单元联合前缀-再设计.txt
      编码五[W==8][u==n==2]
          编码五:仅使用首比特:11 (01)* 00
          编码五:字节示意:1_ 1_ (0_ 1_)* 0_ 0_


  大概是？view others/数学/编程/TODO_list/整数编码-多单元联合前缀-完全序号.txt
    [编码五囗退化囗对称囗囗扩展囗任意格式 =[def]= 所有 (1{z} ([01]* 除去 [01]* (1{z} | 0{z}) [01]*) 0{z}) 类型的码]
    计算 编码五囗退化囗对称囗囗扩展囗任意格式 的 完全累计序号
    枚举囗完全累计序号囗囗多单元首比特联合编码方案囗首尾纯色相反囗囗扩展囗任意格式囗
    枚举囗完全累计序号囗囗多单元首比特联合编码方案囗首尾纯色相反囗囗扩展囗任意格式囗囗字长为一囗


在本模块中重命名:
    编码五-->多单元首比特联合编码方案囗首尾纯色相反
    编码四-->多单元首比特联合编码方案囗首尾纯色相同
    ==>>
    首比特囗类别
    基类囗多单元首比特联合编码方案
    多单元首比特联合编码方案囗首尾纯色相反
    多单元首比特联合编码方案囗首尾纯色相同
[[[[
view others/数学/编程/TODO_list/整数编码-多单元联合前缀-再设计.txt
======================
编码约束
编码四
编码五
负载比特数与字数的关系囗囗计算框架
负载比特数与字数的关系
    字数之负载比特数囗囗编码四囗
    负载比特数之字数囗囗编码四囗

    字数之负载比特数囗囗编码五囗退化囗对称囗
    负载比特数之字数囗囗编码五囗退化囗对称囗


    字数之位置之该字首比特类别囗囗编码四囗
    字数之位置之该字首比特类别囗囗编码五囗退化囗对称囗

使用囗计算框架囗实现囗负载比特数之字数囗囗编码四囗
    负载比特数之字数囗囗编码四囗
使用囗计算框架囗实现囗负载比特数之字数囗囗编码五囗退化囗对称囗
    负载比特数之字数囗囗编码五囗退化囗对称囗
======================
======================
======================
编码约束
  * 允许同码首尾交叠
  * 禁止异码尾首交叠
  * 禁止异码尾首交叠囗囗约定囗囗首比特流始于一终于零
======================
======================
======================
[[[编码四:[字长==W>=1][编码参数n>=1]
  * 首定位符:
    (10 1{n} 0)
  * 尾定位符:
    (1{n} 00)
  =====================编码格式:
  * (10 1{n} 00)
        #总长度 <- [n+4]
  * [n==1]:(1010) (11 [01])* 1{,2} 1 (100)
        #总长度 <- [8..]
  * [n>=2]:(10 1{n} 0) 1 (1{n} 00)
        #总长度 <- [2*n+6]
  * [n>=2]:(10 1{n} 0) 1 ([01]{n-2} 0 [01])* [01]{,n-1} 1 (1{n} 00)
        #总长度 <- [2*n+7..]
  ==>>
        #总长度 <- [n+4,2*n+6,2*n+7..]
  =====================编码参数设置:
  [字长==W>=1]
  [编码参数n >= 1]
  [编码的最小总长度==n+4 >=5]
  [最高负载率的极限=中部负载率=(n*W-1)/(n*W)==(1-1/W/n) if n>=2 else (1-2/3/W)]

  [[W==8][n==2] -> [最高负载率的极限=15/16]]
  [[W==8][n==1] -> [最高负载率的极限=11/12]]
  =====================编码四:end
]]]
======================
======================
======================
[[[编码五:退化囗对称:[字长==W>=1][编码参数:z>=2]
  * 首定位符:
    (1{z} 0)
  * 尾定位符:
    (1 0{z})
  =============================退化囗对称[u==n>=2][z:=u]:
  * (1{z} 0{z})
  * (1{z} 0) ([01]{z-2} 10)* [01]{,z-2} (1 0{z})
  * [z>=3]:(1{z} 0) ([01]{z-2} 10)* [01]{z-3} (01 | 10) (1 0{z})
        #余部-([01]{z-3} (01 | 10)) 等效于 ([01]{z-2} F)
  ==>>
        #[z>=3]总长度 <- [2*z..] \\ [2*z+1]
        #[z==2]总长度 <- [4,6..]
  =====================编码参数设置:
  [字长==W>=1]
  [编码参数z>=2]
  [编码的最小总长度==2*z >=4]

  [[W==8][z==4] -> [最高负载率的极限=15/16]]
  [[W==8][z==3] -> [最高负载率的极限=11/12]]
  [[W==8][z==2] -> [最高负载率的极限=7/8]]
  =====================编码五:退化囗对称:end
]]]


[[[负载比特数与字数的关系囗囗计算框架:
#负载比特数与字数的关系:计算框架
[字长==W>=1]

[Lw:=字数]#总长度
[Lb:=负载比特数]
[Lhb:=负载首比特数]
[Lnhb:=非负载首比特数]
[Lb == Lhb + (W-1)*Lw == W*Lw - Lnhb]
[Lnhb + Lhb == Lw]
[(W-1)*Lw <= Lb <= W*Lw]
[Lw >= Lb/W]
[最低负载率 <= Lb/(W*Lw) <= 最高负载率的极限]
[Lb/最高负载率的极限 <= (W*Lw) <= Lb/最低负载率]
[Lb/W/最高负载率的极限 <= Lw <= Lb/W/最低负载率]
[ceil(Lb/W/最高负载率的极限) <= Lw <= floor(Lb/W/最低负载率)]
# [W==1] ==>> [最低负载率 == 1-1/W == 0] 不好用
[Lw__lowbound := max(最小总长度,ceil(Lb/W/最高负载率的极限))]


=============计算框架:
#数据
[首比特囗类别 :=
  [负载比特囗值自由
  ,格式比特囗值一
  ,格式比特囗值零
  ,格式比特囗值相反于前比特
  ,格式比特囗值相同于前比特
  ]]


#抽象方法:
[编码参数是否合法囗<编码方案>(W,编码参数;) :: bool]
  #abstractmethod
[最高负载率的极限囗<编码方案>(W,编码参数;) :: 负载率/分数]
  #abstractmethod
[最小总长度囗<编码方案>(W,编码参数;) :: Lw]
  #abstractmethod
[总长度是否合法囗<编码方案>(W,编码参数;) :: Lw -> bool]
  #abstractmethod
[字数之负载比特数囗<编码方案>(W,编码参数;) :: Lw -> Lb]
  #abstractmethod
[字数之位置之该字首比特类别囗<编码方案>(W,编码参数;) :: Lw -> idx/[0..<Lw] -> 首比特囗类别]
  #abstractmethod


#可覆盖囗具象方法:
[枚举囗合法总长度囗囗大于等于囗<编码方案>(W,编码参数;) :: Lw__lowbound -> [Lw]]
[字数之正向枚举各字首比特类别囗<编码方案>(W,编码参数;) :: Lw -> [首比特囗类别]{len=Lw}]


#具象方法:
[负载比特数之字数下界估计囗<编码方案>(W,编码参数;) :: Lb -> Lw__lowbound]
[负载比特数之字数过滤器囗<编码方案>(W,编码参数;) :: Lb -> [Lw] -> [Lw]]
[负载比特数之字数囗<编码方案>(W,编码参数;) :: Lb -> Lw]





[枚举囗合法总长度囗囗大于等于囗<编码方案>(W,编码参数;Lw__lowbound) :=
  let [Lw0 := max(最小总长度囗<编码方案>(W,编码参数;), Lw__lowbound)]
  in [Lw | [Lw :<- [Lw0..]][总长度是否合法囗<编码方案>(W,编码参数;Lw)]]
  ]

[负载比特数之字数下界估计囗<编码方案>(W,编码参数;Lb) := max(最小总长度囗<编码方案>(W,编码参数;), ceil(Lb/W/最高负载率的极限囗<编码方案>(W,编码参数;)))] #Lw__lowbound
[负载比特数之字数过滤器囗<编码方案>(W,编码参数;Lb,Lw_ls) := [Lw | [Lw :<- Lw_ls][总长度是否合法囗<编码方案>(W,编码参数;Lw)][Lb <= 字数之负载比特数囗<编码方案>(W,编码参数;Lw)]]]
[负载比特数之字数囗<编码方案>(W,编码参数;Lb) :=
  assert (W>=1 and 编码参数是否合法囗<编码方案>(W,编码参数;)) $
  assert (Lb>=0) $
  assert (Lb==0 or 最高负载率的极限囗<编码方案>(W,编码参数;)=!=0) $
  let [Lw__lowbound := 负载比特数之字数下界估计囗<编码方案>(W,编码参数;Lb)]
      # [Lw_ls := [Lw__lowbound..]]
      [Lw_ls := 枚举囗合法总长度囗囗大于等于囗<编码方案>(W,编码参数;Lw__lowbound)]
      [Lw := head $ 负载比特数之字数过滤器囗<编码方案>(W,编码参数;Lb,Lw_ls)]
  in  Lw
  ]
[字数之正向枚举各字首比特类别囗(W,编码参数;Lw) :=
  [字数之位置之该字首比特类别囗<编码方案>(W,编码参数;Lw,idx) | [idx :<- [0..<Lw]]]
  ]

]]]
[[负载比特数与字数的关系

#字数->负载比特数
[字数之负载比特数囗囗编码四囗(W,n;Lw) :=
  assert (W>=1 and n>=1 and (Lw==n+4 or Lw>=2*n+6)) $
  if Lw<=2*n+7 then (W-1)*Lw
  elif n==1 then (W-1)*Lw + (Lw-8)//3
  else W*Lw - (Lw-7)//n - 2*n -5
  ]

#负载比特数->字数
[负载比特数之字数囗囗编码四囗(W,n;Lb) := ???见下面???]



#字数之负载比特数囗囗编码五:退化囗对称:
#字数->负载比特数
[字数之负载比特数囗囗编码五囗退化囗对称囗(W,z;Lw) :=
  assert (W>=1 and z>=2 and Lw>=2*z and Lw =!= 2*z+1 and (z>=3 or Lw%2 == 0)) $
  if Lw <- [2*z,2*z+2] or z==2 then (W-1)*Lw else
  #分支:[[z>=3][Lw>=2*z+3]]
  let [(q,r):=(Lw-(2*z+2))/%z] in
  assert [[r=!=z-1]or[z>=3]] $
  let [Lnhb:=(2*z+2) +q*2 +[r==z-1]] in
  W*Lw -Lnhb
  ]


#负载比特数之字数囗囗编码五:退化囗对称:
#负载比特数->字数
[负载比特数之字数囗囗编码五囗退化囗对称囗(W,z;Lb) := ???见下面???]





===============================
===============================
#字数之位置之该字首比特类别囗:编码四
#字数->位置->首比特囗类别
[字数之位置之该字首比特类别囗囗编码四囗(W,n;Lw,idx) :=
  assert (W>=1 and n>=1 and (Lw==n+4 or Lw>=2*n+6)) $
  assert (0 <= idx < Lw) $
  if idx < n+3 then
      if (idx == 1 or idx == n+2)
      then 首比特囗类别.格式比特囗值零
      else 首比特囗类别.格式比特囗值一
  elif not idx+n+3 < Lw then
      # (idx+n+3) 代替 (idx+n+2)
      #     因为 除最短情形，其他一致为1
      if not idx+2 < Lw
      then 首比特囗类别.格式比特囗值零
      else 首比特囗类别.格式比特囗值一
  #now: [Lw > 2*n+6][(n+3) <= idx < Lw-(n+3)]
  elif n==1 then
      let [ir := (idx-(n+3))%3] in
      if ir==2
      then 首比特囗类别.负载比特囗值自由
      else 首比特囗类别.格式比特囗值一
  elif n>=2 then
      if idx==n+3 then 首比特囗类别.格式比特囗值一 else
      let [ir := (idx-(n+4))%n] in
      if (ir==n-2 and not idx+n+4==Lw)
      then 首比特囗类别.格式比特囗值零
      else 首比特囗类别.负载比特囗值自由
  else error 'logic-err'
  ]


===============================
===============================
#字数之位置之该字首比特类别囗:编码五囗退化囗对称
#字数->位置->首比特囗类别
[字数之位置之该字首比特类别囗囗编码五囗退化囗对称囗(W,z;Lw,idx) :=
  assert (W>=1 and z>=2 and Lw>=2*z and Lw =!= 2*z+1 and (z>=3 or Lw%2 == 0)) $
  assert (0 <= idx < Lw) $
  if idx < z then 首比特囗类别.格式比特囗值一
  elif not idx+z < Lw then 首比特囗类别.格式比特囗值零
  #now: [Lw > 2*z][z <= idx < Lw-z]
  #bug:elif idx==z+1 then 首比特囗类别.格式比特囗值零
  elif idx==z then 首比特囗类别.格式比特囗值零
  elif idx+z+1 == Lw then 首比特囗类别.格式比特囗值一
  #now: [Lw > 2*z+2][(z+1) <= idx < Lw-(z+1)]
  else let
      [ir := (idx-(z+1))%z]
  in
  if ir < z-2 then 首比特囗类别.负载比特囗值自由
  elif (idx+z+2 == Lw and z>=3 and ir==z-2)
      then 首比特囗类别.格式比特囗值相反于前比特
  elif ir == z-2 then 首比特囗类别.格式比特囗值一
  elif ir == z-1 then 首比特囗类别.格式比特囗值零
  else error 'logic-err'
  ]
===============================
===============================

]]负载比特数与字数的关系:end

[使用囗计算框架囗实现囗负载比特数之字数囗囗编码四囗
#使用:计算框架<<==需要:字数之负载比特数囗囗编码四囗

#override:抽象方法:
[编码参数是否合法囗<编码四>(W,n;) := (W>=1 and n>=1)]
[最高负载率的极限囗<编码四>(W,n;) := Fraction((1-1/W/n) if n>=2 else (1-2/3/W))]
[最小总长度囗<编码四>(W,n;) := n+4]
    #编码的最小总长度
[总长度是否合法囗<编码四>(W,n;Lw) := (W>=1 and n>=1 and (Lw==n+4 or Lw>=2*n+6))]
    !! [总长度 <- [n+4,2*n+6,2*n+7..]]
[字数之负载比特数囗<编码四>(W,n;Lw) := 字数之负载比特数囗囗编码四囗(W,n;Lw)]

#override:可覆盖囗具象方法:
[枚举囗合法总长度囗囗大于等于囗<编码四>(W,n;Lw__lowbound) := if Lw__lowbound <= n+4 then [n+4,2*n+6,2*n+7..] else [max(Lw__lowbound,2*n+6)..]]


#调用 具象方法 实现
[负载比特数之字数囗囗编码四囗(W,n;Lb) := 负载比特数之字数囗<编码四>(W,n;Lb)]

]
[使用囗计算框架囗实现囗负载比特数之字数囗囗编码五囗退化囗对称囗
#使用:计算框架<<==需要:字数之负载比特数囗囗编码五囗退化囗对称囗

#override:抽象方法:
[编码参数是否合法囗<编码五囗退化囗对称>(W,z;) := (W>=1 and z>=2)]
[最高负载率的极限囗<编码五囗退化囗对称>(W,z;) := Fraction(1-2/W/z)]
[最小总长度囗<编码五囗退化囗对称>(W,z;) := 2*z]
    #编码的最小总长度
[总长度是否合法囗<编码五囗退化囗对称>(W,z;Lw) := (W>=1 and z>=2 and Lw>=2*z and Lw =!= 2*z+1 and (z>=3 or Lw%2 == 0))]
    !! [[z>=3] -> [总长度 <- [2*z..] \\ [2*z+1]]]
    !! [[z==2] -> [总长度 <- [4,6..]]]
[字数之负载比特数囗<编码五囗退化囗对称>(W,z;Lw) := 字数之负载比特数囗囗编码五囗退化囗对称囗(W,z;Lw)]

#override:可覆盖囗具象方法:
[枚举囗合法总长度囗囗大于等于囗<编码五囗退化囗对称>(W,z;Lw__lowbound) :=
    let [step := 1+(z==2)] in
    if Lw__lowbound <= 2*z then [2*z]++count(2*z+2,step) else count(max(Lw__lowbound,2*z+2),step)
    ]


#调用 具象方法 实现
[负载比特数之字数囗囗编码五囗退化囗对称囗(W,z;Lb) := 负载比特数之字数囗<编码五囗退化囗对称>(W,z;Lb)]

]

]]]]






>>> from seed.io.num_head1s_of_byte import byte2num_head1s
>>> from seed.io.num_head1s_of_byte import Case4ByteDecoder, ByteDecoder__1s0, ByteDecoder__201, ByteDecoder__302x1, ByteDecoder__312x0
>>> len(byte2num_head1s)
256
>>> sorted(byte2num_head1s) == list(byte2num_head1s)
True
>>> sorted({*byte2num_head1s}) == list(range(9))
True
>>> [*map(byte2num_head1s.index, range(9))]
[0, 128, 192, 224, 240, 248, 252, 254, 255]
>>> [*map(byte2num_head1s.rindex, range(9))]
[127, 191, 223, 239, 247, 251, 253, 254, 255]
>>> [*map(byte2num_head1s.count, range(9))]
[128, 64, 32, 16, 8, 4, 2, 1, 1]
>>> all(byte2num_head1s.count(nbits) == byte2num_head1s.rindex(nbits)+1 -byte2num_head1s.index(nbits) for nbits in range(9))
True
>>> byte2num_head1s
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x04\x04\x04\x04\x04\x04\x04\x04\x05\x05\x05\x05\x06\x06\x07\x08'


>>> len(num_head1s2tail_mask)
9
>>> [*num_head1s2tail_mask]
[255, 127, 63, 31, 15, 7, 3, 1, 0]
>>> num_head1s2tail_mask
b'\xff\x7f?\x1f\x0f\x07\x03\x01\x00'







>>> from seed.io.num_head1s_of_byte import 首比特囗类别, 基类囗多单元首比特联合编码方案, 多单元首比特联合编码方案囗首尾纯色相反, 多单元首比特联合编码方案囗首尾纯色相同
>>> from seed.io.num_head1s_of_byte import _kind2nm, 字数之首比特类别昵称字符串囗, 检查囗首比特类别昵称字符串囗囗首尾纯色相反
>>> from seed.io.num_head1s_of_byte import 枚举囗完全累计序号囗囗多单元首比特联合编码方案囗首尾纯色相反囗囗扩展囗任意格式囗, 枚举囗完全累计序号囗囗多单元首比特联合编码方案囗首尾纯色相反囗囗扩展囗任意格式囗囗字长为一囗

>>> codec5_W1_z2 = 多单元首比特联合编码方案囗首尾纯色相反(1,2)
>>> codec5_W1_z3 = 多单元首比特联合编码方案囗首尾纯色相反(1,3)
>>> codec5_W2_z2 = 多单元首比特联合编码方案囗首尾纯色相反(2,2)
>>> codec5_W8_z2 = 多单元首比特联合编码方案囗首尾纯色相反(8,2)
>>> codec5_W8_z3 = 多单元首比特联合编码方案囗首尾纯色相反(8,3)
>>> codec5_W8_z4 = 多单元首比特联合编码方案囗首尾纯色相反(8,4)

>>> codec4_W1_n1 = 多单元首比特联合编码方案囗首尾纯色相同(1,1)
>>> codec4_W1_n2 = 多单元首比特联合编码方案囗首尾纯色相同(1,2)
>>> codec4_W2_n1 = 多单元首比特联合编码方案囗首尾纯色相同(2,1)
>>> codec4_W8_n1 = 多单元首比特联合编码方案囗首尾纯色相同(8,1)
>>> codec4_W8_n2 = 多单元首比特联合编码方案囗首尾纯色相同(8,2)
>>> codec4_W8_n3 = 多单元首比特联合编码方案囗首尾纯色相同(8,3)



最高负载率的极限囗
>>> codec5_W1_z2.最高负载率的极限囗()
Fraction(0, 1)
>>> codec5_W1_z3.最高负载率的极限囗()
Fraction(1, 3)
>>> codec5_W2_z2.最高负载率的极限囗()
Fraction(1, 2)
>>> codec5_W8_z2.最高负载率的极限囗()
Fraction(7, 8)
>>> codec5_W8_z3.最高负载率的极限囗()
Fraction(11, 12)
>>> codec5_W8_z4.最高负载率的极限囗()
Fraction(15, 16)


>>> codec4_W1_n1.最高负载率的极限囗()
Fraction(1, 3)
>>> codec4_W1_n2.最高负载率的极限囗()
Fraction(1, 2)
>>> codec4_W2_n1.最高负载率的极限囗()
Fraction(2, 3)
>>> codec4_W8_n1.最高负载率的极限囗()
Fraction(11, 12)
>>> codec4_W8_n2.最高负载率的极限囗()
Fraction(15, 16)
>>> codec4_W8_n3.最高负载率的极限囗()
Fraction(23, 24)


codec5s
codec4s
>>> codec5s = [codec5_W1_z2, codec5_W1_z3, codec5_W2_z2, codec5_W8_z2, codec5_W8_z3, codec5_W8_z4]
>>> codec4s = [codec4_W1_n1, codec4_W1_n2, codec4_W2_n1, codec4_W8_n1, codec4_W8_n2, codec4_W8_n3]


字数之负载比特数囗
负载比特数之字数囗
>>> [*islice(codec5_W1_z3.枚举囗合法总长度囗囗大于等于囗(0), 4)]
[6, 8, 9, 10]
>>> def show1(codecs, /, *args4islice4Lws):
...     for c in codecs:
...         print(c.所有构造编码方案的参数囗())
...         for Lw in islice(c.枚举囗合法总长度囗囗大于等于囗(0), *args4islice4Lws):
...             Lb = c.字数之负载比特数囗(Lw)
...             print(f'{Lw}:{Lb}')
>>> show1(codec5s, 0, 8)
(1, 2)
4:0
6:0
8:0
10:0
12:0
14:0
16:0
18:0
(1, 3)
6:0
8:0
9:1
10:1
11:1
12:2
13:2
14:2
(2, 2)
4:4
6:6
8:8
10:10
12:12
14:14
16:16
18:18
(8, 2)
4:28
6:42
8:56
10:70
12:84
14:98
16:112
18:126
(8, 3)
6:42
8:56
9:64
10:71
11:78
12:86
13:93
14:100
(8, 4)
8:56
10:70
11:78
12:86
13:93
14:100
15:108
16:116
>>> show1(codec4s, 0, 8)
(1, 1)
5:0
8:0
9:0
10:0
11:1
12:1
13:1
14:2
(1, 2)
6:0
10:0
11:0
12:1
13:1
14:2
15:2
16:3
(2, 1)
5:5
8:8
9:9
10:10
11:12
12:13
13:14
14:16
(8, 1)
5:35
8:56
9:63
10:70
11:78
12:85
13:92
14:100
(8, 2)
6:42
10:70
11:77
12:85
13:92
14:100
15:107
16:115
(8, 3)
7:49
12:84
13:91
14:99
15:107
16:114
17:122
18:130


codec5s
codec4s
>>> codec5s_z_ = [codec5_W1_z2, codec5_W1_z3, codec5_W8_z4]
>>> codec4s_n_ = [codec4_W1_n1, codec4_W1_n2, codec4_W8_n3]

字数之位置之该字首比特类别囗
字数之正向枚举各字首比特类别囗
字数之首比特类别昵称字符串囗
检查囗首比特类别昵称字符串囗囗首尾纯色相反
>>> def show2(codecs, /, *args4islice4Lws):
...     for c in codecs:
...         print(c.所有构造编码方案的参数囗())
...         for Lw in islice(c.枚举囗合法总长度囗囗大于等于囗(0), *args4islice4Lws):
...             print((Lw, 字数之首比特类别昵称字符串囗(c,Lw)))
>>> show2(codec5s_z_, 0, 16)
(1, 2)
(4, '1100')
(6, '110100')
(8, '11010100')
(10, '1101010100')
(12, '110101010100')
(14, '11010101010100')
(16, '1101010101010100')
(18, '110101010101010100')
(20, '11010101010101010100')
(22, '1101010101010101010100')
(24, '110101010101010101010100')
(26, '11010101010101010101010100')
(28, '1101010101010101010101010100')
(30, '110101010101010101010101010100')
(32, '11010101010101010101010101010100')
(34, '1101010101010101010101010101010100')
(1, 3)
(6, '111000')
(8, '11101000')
(9, '1110X1000')
(10, '1110X~1000')
(11, '1110X101000')
(12, '1110X10X1000')
(13, '1110X10X~1000')
(14, '1110X10X101000')
(15, '1110X10X10X1000')
(16, '1110X10X10X~1000')
(17, '1110X10X10X101000')
(18, '1110X10X10X10X1000')
(19, '1110X10X10X10X~1000')
(20, '1110X10X10X10X101000')
(21, '1110X10X10X10X10X1000')
(22, '1110X10X10X10X10X~1000')
(8, 4)
(8, '11110000')
(10, '1111010000')
(11, '11110X10000')
(12, '11110XX10000')
(13, '11110XX~10000')
(14, '11110XX1010000')
(15, '11110XX10X10000')
(16, '11110XX10XX10000')
(17, '11110XX10XX~10000')
(18, '11110XX10XX1010000')
(19, '11110XX10XX10X10000')
(20, '11110XX10XX10XX10000')
(21, '11110XX10XX10XX~10000')
(22, '11110XX10XX10XX1010000')
(23, '11110XX10XX10XX10X10000')
(24, '11110XX10XX10XX10XX10000')
>>> show2(codec4s_n_, 0, 16)
(1, 1)
(5, '10100')
(8, '10101100')
(9, '101011100')
(10, '1010111100')
(11, '101011X1100')
(12, '101011X11100')
(13, '101011X111100')
(14, '101011X11X1100')
(15, '101011X11X11100')
(16, '101011X11X111100')
(17, '101011X11X11X1100')
(18, '101011X11X11X11100')
(19, '101011X11X11X111100')
(20, '101011X11X11X11X1100')
(21, '101011X11X11X11X11100')
(22, '101011X11X11X11X111100')
(1, 2)
(6, '101100')
(10, '1011011100')
(11, '10110111100')
(12, '101101X11100')
(13, '1011010X11100')
(14, '1011010XX11100')
(15, '1011010X0X11100')
(16, '1011010X0XX11100')
(17, '1011010X0X0X11100')
(18, '1011010X0X0XX11100')
(19, '1011010X0X0X0X11100')
(20, '1011010X0X0X0XX11100')
(21, '1011010X0X0X0X0X11100')
(22, '1011010X0X0X0X0XX11100')
(23, '1011010X0X0X0X0X0X11100')
(24, '1011010X0X0X0X0X0XX11100')
(8, 3)
(7, '1011100')
(12, '101110111100')
(13, '1011101111100')
(14, '1011101X111100')
(15, '1011101XX111100')
(16, '1011101X0X111100')
(17, '1011101X0XX111100')
(18, '1011101X0XXX111100')
(19, '1011101X0XX0X111100')
(20, '1011101X0XX0XX111100')
(21, '1011101X0XX0XXX111100')
(22, '1011101X0XX0XX0X111100')
(23, '1011101X0XX0XX0XX111100')
(24, '1011101X0XX0XX0XXX111100')
(25, '1011101X0XX0XX0XX0X111100')
(26, '1011101X0XX0XX0XX0XX111100')









枚举囗完全累计序号囗囗多单元首比特联合编码方案囗首尾纯色相反囗囗扩展囗任意格式囗
枚举囗完全累计序号囗囗多单元首比特联合编码方案囗首尾纯色相反囗囗扩展囗任意格式囗囗字长为一囗
>>> def show3(W, z, /, *args4islice4Lws):
...     for (Lw, acc_total4Lw_W, total4Lw_W, (acc_total4Lw, total4Lw, xcount2acc)) in islice(枚举囗完全累计序号囗囗多单元首比特联合编码方案囗首尾纯色相反囗囗扩展囗任意格式囗(W,z), *args4islice4Lws):
...         print((Lw, acc_total4Lw_W, total4Lw_W, (acc_total4Lw, total4Lw, xcount2acc)))

>>> show3(1, 2,     0, 16)
(2, 0, 0, (0, 0, [0, 0, 1]))
(3, 0, 0, (0, 0, [1, 0, 0]))
(4, 1, 1, (1, 1, [0, 1, 1]))
(5, 1, 0, (1, 0, [1, 0, 0]))
(6, 2, 1, (2, 1, [0, 1, 1]))
(7, 2, 0, (2, 0, [1, 0, 0]))
(8, 3, 1, (3, 1, [0, 1, 1]))
(9, 3, 0, (3, 0, [1, 0, 0]))
(10, 4, 1, (4, 1, [0, 1, 1]))
(11, 4, 0, (4, 0, [1, 0, 0]))
(12, 5, 1, (5, 1, [0, 1, 1]))
(13, 5, 0, (5, 0, [1, 0, 0]))
(14, 6, 1, (6, 1, [0, 1, 1]))
(15, 6, 0, (6, 0, [1, 0, 0]))
(16, 7, 1, (7, 1, [0, 1, 1]))
(17, 7, 0, (7, 0, [1, 0, 0]))

>>> show3(1, 3,     0, 16)
(3, 0, 0, (0, 0, [0, 0, 0, 0, 1]))
(4, 0, 0, (0, 0, [1, 0, 0, 0, 0]))
(5, 0, 0, (0, 0, [0, 1, 0, 1, 0]))
(6, 1, 1, (1, 1, [1, 0, 1, 1, 1]))
(7, 1, 0, (1, 0, [2, 1, 0, 1, 1]))
(8, 2, 1, (2, 1, [2, 2, 1, 3, 1]))
(9, 4, 2, (4, 2, [4, 2, 2, 4, 3]))
(10, 6, 2, (6, 2, [7, 4, 2, 6, 4]))
(11, 10, 4, (10, 4, [10, 7, 4, 11, 6]))
(12, 17, 7, (17, 7, [17, 10, 7, 17, 11]))
(13, 27, 10, (27, 10, [28, 17, 10, 27, 17]))
(14, 44, 17, (44, 17, [44, 28, 17, 45, 27]))
(15, 72, 28, (72, 28, [72, 44, 28, 72, 45]))
(16, 116, 44, (116, 44, [117, 72, 44, 116, 72]))
(17, 188, 72, (188, 72, [188, 117, 72, 189, 116]))
(18, 305, 117, (305, 117, [305, 188, 117, 305, 189]))

>>> show3(1, 4,     0, 16)
(4, 0, 0, (0, 0, [0, 0, 0, 0, 0, 0, 1]))
(5, 0, 0, (0, 0, [1, 0, 0, 0, 0, 0, 0]))
(6, 0, 0, (0, 0, [0, 1, 0, 0, 1, 0, 0]))
(7, 0, 0, (0, 0, [1, 0, 1, 0, 1, 1, 0]))
(8, 1, 1, (1, 1, [2, 1, 0, 1, 2, 1, 1]))
(9, 1, 0, (1, 0, [4, 2, 1, 0, 3, 2, 1]))
(10, 2, 1, (2, 1, [6, 4, 2, 1, 7, 3, 2]))
(11, 4, 2, (4, 2, [12, 6, 4, 2, 12, 7, 3]))
(12, 8, 4, (8, 4, [22, 12, 6, 4, 22, 12, 7]))
(13, 14, 6, (14, 6, [41, 22, 12, 6, 40, 22, 12]))
(14, 26, 12, (26, 12, [74, 41, 22, 12, 75, 40, 22]))
(15, 48, 22, (48, 22, [137, 74, 41, 22, 137, 75, 40]))
(16, 89, 41, (89, 41, [252, 137, 74, 41, 252, 137, 75]))
(17, 163, 74, (163, 74, [464, 252, 137, 74, 463, 252, 137]))
(18, 300, 137, (300, 137, [852, 464, 252, 137, 853, 463, 252]))
(19, 552, 252, (552, 252, [1568, 852, 464, 252, 1568, 853, 463]))

>>> show3(2, 2,     0, 16)
(2, 0, 0, (0, 0, [0, 0, 1]))
(3, 0, 0, (0, 0, [1, 0, 0]))
(4, 16, 16, (1, 1, [0, 1, 1]))
(5, 16, 0, (1, 0, [1, 0, 0]))
(6, 80, 64, (2, 1, [0, 1, 1]))
(7, 80, 0, (2, 0, [1, 0, 0]))
(8, 336, 256, (3, 1, [0, 1, 1]))
(9, 336, 0, (3, 0, [1, 0, 0]))
(10, 1360, 1024, (4, 1, [0, 1, 1]))
(11, 1360, 0, (4, 0, [1, 0, 0]))
(12, 5456, 4096, (5, 1, [0, 1, 1]))
(13, 5456, 0, (5, 0, [1, 0, 0]))
(14, 21840, 16384, (6, 1, [0, 1, 1]))
(15, 21840, 0, (6, 0, [1, 0, 0]))
(16, 87376, 65536, (7, 1, [0, 1, 1]))
(17, 87376, 0, (7, 0, [1, 0, 0]))

>>> show3(2, 3,     0, 16)
(3, 0, 0, (0, 0, [0, 0, 0, 0, 1]))
(4, 0, 0, (0, 0, [1, 0, 0, 0, 0]))
(5, 0, 0, (0, 0, [0, 1, 0, 1, 0]))
(6, 64, 64, (1, 1, [1, 0, 1, 1, 1]))
(7, 64, 0, (1, 0, [2, 1, 0, 1, 1]))
(8, 320, 256, (2, 1, [2, 2, 1, 3, 1]))
(9, 1344, 1024, (4, 2, [4, 2, 2, 4, 3]))
(10, 3392, 2048, (6, 2, [7, 4, 2, 6, 4]))
(11, 11584, 8192, (10, 4, [10, 7, 4, 11, 6]))
(12, 40256, 28672, (17, 7, [17, 10, 7, 17, 11]))
(13, 122176, 81920, (27, 10, [28, 17, 10, 27, 17]))
(14, 400704, 278528, (44, 17, [44, 28, 17, 45, 27]))
(15, 1318208, 917504, (72, 28, [72, 44, 28, 72, 45]))
(16, 4201792, 2883584, (116, 44, [117, 72, 44, 116, 72]))
(17, 13638976, 9437184, (188, 72, [188, 117, 72, 189, 116]))
(18, 44309824, 30670848, (305, 117, [305, 188, 117, 305, 189]))

>>> show3(2, 4,     0, 16)
(4, 0, 0, (0, 0, [0, 0, 0, 0, 0, 0, 1]))
(5, 0, 0, (0, 0, [1, 0, 0, 0, 0, 0, 0]))
(6, 0, 0, (0, 0, [0, 1, 0, 0, 1, 0, 0]))
(7, 0, 0, (0, 0, [1, 0, 1, 0, 1, 1, 0]))
(8, 256, 256, (1, 1, [2, 1, 0, 1, 2, 1, 1]))
(9, 256, 0, (1, 0, [4, 2, 1, 0, 3, 2, 1]))
(10, 1280, 1024, (2, 1, [6, 4, 2, 1, 7, 3, 2]))
(11, 5376, 4096, (4, 2, [12, 6, 4, 2, 12, 7, 3]))
(12, 21760, 16384, (8, 4, [22, 12, 6, 4, 22, 12, 7]))
(13, 70912, 49152, (14, 6, [41, 22, 12, 6, 40, 22, 12]))
(14, 267520, 196608, (26, 12, [74, 41, 22, 12, 75, 40, 22]))
(15, 988416, 720896, (48, 22, [137, 74, 41, 22, 137, 75, 40]))
(16, 3675392, 2686976, (89, 41, [252, 137, 74, 41, 252, 137, 75]))
(17, 13374720, 9699328, (163, 74, [464, 252, 137, 74, 463, 252, 137]))
(18, 49288448, 35913728, (300, 137, [852, 464, 252, 137, 853, 463, 252]))
(19, 181409024, 132120576, (552, 252, [1568, 852, 464, 252, 1568, 853, 463]))







#]]]'''
__all__ = r'''
byte2num_head1s
Case4ByteDecoder
IByteDecoder
    ByteDecoder__1s0
    ByteDecoder__201
    ByteDecoder__302x1
    ByteDecoder__312x0

首比特囗类别
    字数之首比特类别昵称字符串囗
    检查囗首比特类别昵称字符串囗囗首尾纯色相反
基类囗多单元首比特联合编码方案
    多单元首比特联合编码方案囗首尾纯色相反
    多单元首比特联合编码方案囗首尾纯色相同

枚举囗完全累计序号囗囗多单元首比特联合编码方案囗首尾纯色相反囗囗扩展囗任意格式囗





byte2num_head1s
    num_bits4byte
    upperbound4byte
    max4byte
num_head1s2tail_mask
Case4ByteDecoder
IByteDecoder
    IByteDecoder__using_num_head1s
        IByteDecoder__using_max_num_head1s
            ByteDecoder__1s0
            ByteDecoder__201
            ByteDecoder__302x1
            ByteDecoder__312x0



EOF_Error
BOF_Error

TokenError
  TokenEncodeError
  TokenDecodeError
    TokenBrokenError
        InvalidFirstByte4Token
        InvalidLastByte4Token
        TokenMissFirstByte
            TokenMissFirstByte__LFL
            TokenMissFirstByte__SFL
            TokenMissFirstByte__BOF
        TokenMissLastByte
            TokenMissLastByte__FFF
            TokenMissLastByte__FFS
            TokenMissLastByte__EOF

首比特囗类别
基类囗多单元首比特联合编码方案
    多单元首比特联合编码方案囗首尾纯色相反
    多单元首比特联合编码方案囗首尾纯色相同

枚举囗完全累计序号囗囗多单元首比特联合编码方案囗首尾纯色相反囗囗扩展囗任意格式囗
    枚举囗完全累计序号囗囗多单元首比特联合编码方案囗首尾纯色相反囗囗扩展囗任意格式囗囗字长为一囗

'''.split()#'''
__all__
from seed.tiny_.check import check_uint_lt, check_int_ge_lt, check_int_ge, check_int_ge_le
from seed.tiny_.check import check_type_is
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.mapping_tools.dict_op import inv__k2v_to_v2k
from seed.tiny import snd
#from seed.tiny_.check import check_uint
from seed.helper.repr_input import repr_helper

from enum import auto, Enum #, Flag
from io import UnsupportedOperation
from os import SEEK_END
from itertools import count, chain, islice
from math import ceil
from fractions import Fraction
import re



num_bits4byte = 8
upperbound4byte = 2**num_bits4byte
max4byte = upperbound4byte -1

def _():
    num_bits4byte
    upperbound4byte
    max4byte
    byte2num_head1s = [None]*upperbound4byte
    for u in range(upperbound4byte):
        if u == max4byte:
            byte2num_head1s[u] = num_bits4byte
        else:
            s = f'{u:0>8b}0'
            i = s.index('0')
            L = num_bits4byte+1
            #L = len(s)
            assert L == len(s)
            byte2num_head1s[u] = i
    byte2num_head1s = bytes(byte2num_head1s)
    return byte2num_head1s
def _():
    num_bits4byte
    upperbound4byte
    byte2num_head1s = []
    sz = upperbound4byte
    for nbits in range(num_bits4byte):
        sz >>= 1
        byte2num_head1s += [nbits]*sz
    byte2num_head1s += [num_bits4byte]
    byte2num_head1s = bytes(byte2num_head1s)
    return byte2num_head1s
byte2num_head1s = _()

#assert byte2num_head1s == b'', byte2num_head1s
assert len(byte2num_head1s) == 1<<8
assert byte2num_head1s[0] == 0
assert byte2num_head1s[127] == 0
assert byte2num_head1s[128] == 1
assert byte2num_head1s[191] == 1
assert byte2num_head1s[192] == 2
assert byte2num_head1s[254] == 7
assert byte2num_head1s[255] == 8





def _():
    num_bits4byte
    max4byte
    num_head1s2tail_mask = []
    tail_mask = max4byte
    for nbits in range(num_bits4byte+1):
        num_head1s2tail_mask.append(tail_mask)
        tail_mask >>= 1
    num_head1s2tail_mask = bytes(num_head1s2tail_mask)
    return num_head1s2tail_mask
num_head1s2tail_mask = _()
assert len(num_head1s2tail_mask) == 1+8
assert num_head1s2tail_mask[0] == 255
assert num_head1s2tail_mask[1] == 127
assert num_head1s2tail_mask[7] == 1
assert num_head1s2tail_mask[8] == 0
#assert num_head1s2tail_mask == b'', num_head1s2tail_mask


class EOF_Error(Exception):pass
class BOF_Error(Exception):pass


class TokenError(Exception):pass
class TokenEncodeError(TokenError):pass
class TokenDecodeError(TokenError):pass


class TokenBrokenError(TokenDecodeError):pass
class InvalidFirstByte4Token(TokenBrokenError):pass
class InvalidLastByte4Token(TokenBrokenError):pass

class TokenMissFirstByte(TokenBrokenError):pass
class TokenMissFirstByte__LFL(TokenMissFirstByte):pass
class TokenMissFirstByte__SFL(TokenMissFirstByte):pass
class TokenMissFirstByte__BOF(TokenMissFirstByte, BOF_Error):pass

class TokenMissLastByte(TokenBrokenError):pass
class TokenMissLastByte__FFF(TokenMissLastByte):pass
class TokenMissLastByte__FFS(TokenMissLastByte):pass
class TokenMissLastByte__EOF(TokenMissLastByte, EOF_Error):pass
class Case4ByteDecoder(Enum):
#class Case4ByteDecoder(Flag):
    #isolated
    singleton=auto()
    #head
    #begin
    first=auto()
    #body
    fragment=auto()
    #tail
    #end
    last=auto()
assert len(Case4ByteDecoder) == 4
#assert len(Case4ByteDecoder) == 16

def _peak_case_at(sf, addr, ibstream, lazy_exc=EOF_Error, /):
    ibstream.seek(addr)
    bs = ibstream.peek(1)
    if not bs:
        #EOF
        raise lazy_exc()
    [u] = bs
    (byte_case, payload) = sf.decode_uint8byte__case(u)
    return byte_case
class IByteDecoder(ABC):
    r'''[[[
    iter_payloadss4token__forward
    iter_payloadss4token__backward
        iter_tokens__forward
        iter_tokens__backward

    seek_to_last_of_curr_token4decode
        seek_to_first_of_next_token4decode_
    seek_to_first_of_curr_token4decode
        seek_to_last_of_prev_token4decode_
            seek_to_first_of_prev_token4decode_
    #]]]'''
    __slots__ = ()
    @abstractmethod
    def token5payloads(sf, payloads, /):
        'payloads -> token'
    @abstractmethod
    def token5payloads(sf, payloads, /):
        'payloads -> token'
    @abstractmethod
    def decode_uint8byte__case(sf, u, /):
        '[0..<256] -> (byte_case, payload) #payload :: uint'
    @abstractmethod
    def does_support_forward_decode(sf, /):
        '-> bool'
    @abstractmethod
    def does_support_backward_decode(sf, /):
        '-> bool'
    def does_support_bidirectional_decode(sf, /):
        '-> bool'
        return sf.does_support_forward_decode() and sf.does_support_backward_decode()
    def seek_to_first_of_curr_token4decode(sf, ibstream, /):
        'seekable-ibstream{non-EOF,on valid token} -> addr4first4token{.==ibstream.tell()} |^EOF_Error|^TokenMissFirstByte__LFL|^TokenMissFirstByte__SFL|^TokenMissFirstByte__BOF|^UnsupportedOperation'
        if not sf.does_support_backward_decode(): raise UnsupportedOperation
        if not sf.seekable(): raise UnsupportedOperation
        addr0 = ibstream.tell()
        for addr in reversed(range(addr0+1)):
            byte_case = _peak_case_at(sf, addr, ibstream)
                # ^EOF_Error
            if byte_case is Case4ByteDecoder.fragment:
                continue
            elif byte_case is Case4ByteDecoder.last:
                if addr==addr0:
                    continue
                raise TokenMissFirstByte__LFL('LFL:pattern: last fragment* ( fragment | last )')
            elif byte_case is Case4ByteDecoder.singleton:
                if addr==addr0:
                    break
                raise TokenMissFirstByte__SFL('SFL:pattern: singleton fragment* ( fragment | last )')
            elif byte_case is Case4ByteDecoder.first:
                break
            else:
                raise TypeError(f'unknown case: {byte_case!r}')
        else:
            raise TokenMissFirstByte__BOF('BOF:pattern: ^ fragment* ( fragment | last )')
        assert ibstream.tell()==addr
        return addr
    def seek_to_last_of_curr_token4decode(sf, ibstream, /):
        'seekable-ibstream{non-EOF,on valid token} -> addr4last4token{.==ibstream.tell()} |^EOF_Error|^TokenMissLastByte__FFF|^TokenMissLastByte__FFS|^UnsupportedOperation'
        if not sf.does_support_forward_decode(): raise UnsupportedOperation
        if not sf.seekable(): raise UnsupportedOperation
        addr0 = ibstream.tell()
        lazy_exc = lambda:EOF_Error if addr==addr0 else TokenMissLastByte__EOF('EOF:pattern: ( first | fragment ) fragment* $')
        for addr in count(addr0):
            byte_case = _peak_case_at(sf, addr, ibstream, lazy_exc)
                # ^EOF_Error
            if byte_case is Case4ByteDecoder.fragment:
                continue
            elif byte_case is Case4ByteDecoder.first:
                if addr==addr0:
                    continue
                raise TokenMissLastByte__FFF('FFF:pattern: ( first | fragment ) fragment* first')
            elif byte_case is Case4ByteDecoder.singleton:
                if addr==addr0:
                    break
                raise TokenMissLastByte__FFS('FFS:pattern: ( first | fragment ) fragment* singleton')
            elif byte_case is Case4ByteDecoder.last:
                break
            else:
                raise TypeError(f'unknown case: {byte_case!r}')
        else:
            #raise TokenMissLastByte__EOF('EOF:pattern: ( first | fragment ) fragment* $')
            raise logic-err
        assert ibstream.tell()==addr
        return addr

    def seek_to_begin_of_curr_token4decode(sf, ibstream, /):
        '-> addr4first4token/addr4begin4token'
        return sf.seek_to_first_of_curr_token4decode(ibstream)
    def seek_to_end_of_curr_token4decode(sf, ibstream, /):
        '-> addr4end4token'
        addr4last4token = sf.seek_to_last_of_curr_token4decode(ibstream)
        addr4end4token = addr4last4token+1
        ibstream.seek(addr4end4token)
        return addr4end4token
    def seek_to_first_of_prev_token4decode_(sf, valid, ibstream, /):
        '-> addr4first4prev/addr4begin4prev'
        addr4last4prev = sf.seek_to_last_of_prev_token4decode_(valid, ibstream)
        addr4first4prev = sf.seek_to_first_of_curr_token4decode(ibstream)
        return addr4first4prev
    def seek_to_begin_of_next_token4decode_(sf, valid, ibstream, /):
        '-> addr4first4next/addr4begin4next'
        return sf.seek_to_first_of_next_token4decode_(valid, ibstream)
    def seek_to_first_of_next_token4decode_(sf, valid, ibstream, /):
        'valid -> ibstream -> addr4first4next|^EOF_Error|^InvalidFirstByte4Token'
        addr4end4token = sf.seek_to_end_of_curr_token4decode(ibstream)
        if valid:
            if not sf.is_on_first_of_token4decode(ibstream): raise InvalidFirstByte4Token#++EOF_Error

        addr4first4next = addr4end4token
        return addr4first4next
    def seek_to_end_of_prev_token4decode(sf, ibstream, /):
        '-> addr4end4prev'
        return sf.seek_to_begin_of_curr_token4decode(ibstream)
    def seek_to_last_of_prev_token4decode_(sf, valid, ibstream, /):
        'valid -> ibstream -> addr4last4prev|^BOF_Error|^InvalidLastByte4Token'
        addr4end4prev = sf.seek_to_end_of_prev_token4decode(ibstream)
        if addr4end4prev == 0:raise BOF_Error
        addr4last4prev = addr4end4prev-1
        assert 0 <= addr4last4prev < addr4end4prev
        ibstream.seek(addr4last4prev)
        if valid:
            if not sf.is_on_last_of_token4decode(ibstream): raise InvalidLastByte4Token
        return addr4last4prev
    def is_on_last_of_token4decode(sf, ibstream, /):
        '-> bool|^EOF_Error'
        addr = ibstream.tell()
        byte_case = _peak_case_at(sf, addr, ibstream)
            # ^EOF_Error
        return byte_case is Case4ByteDecoder.singleton or byte_case is Case4ByteDecoder.last or (not sf.does_support_forward_decode())
    def is_on_first_of_token4decode(sf, ibstream, /):
        '-> bool|^EOF_Error'
        addr = ibstream.tell()
        byte_case = _peak_case_at(sf, addr, ibstream)
            # ^EOF_Error
        return byte_case is Case4ByteDecoder.singleton or byte_case is Case4ByteDecoder.first or (not sf.does_support_backward_decode())
        #eg:ByteDecoder__1s0

    def iter_tokens__forward(sf, ibstream, /):
        '-> Iter<token>'
        tokens = map(sf.token5payloads, sf.iter_payloadss4token__forward(ibstream))
        return tokens
    def iter_tokens__backward(sf, ibstream, /):
        '-> Iter<token>'
        tokens = map(sf.token5payloads, sf.iter_payloadss4token__backward(ibstream))
        return tokens
    def iter_payloadss4token__forward(sf, ibstream, /):
        '-> Iter<[payload]>/Iter<bytes>'
        addr4begin = ibstream.tell()
        addr4EOF = ibstream.seek(0, SEEK_END)
        ibstream.seek(addr4begin)
        while not addr4begin == addr4EOF:
            try:
                if not sf.is_on_first_of_token4decode(ibstream): raise InvalidFirstByte4Token#++EOF_Error
            except EOF_Error:
                raise logic-err
                return
            addr4end = sf.seek_to_end_of_curr_token4decode(ibstream)
            ibstream.seek(addr4begin)
            payloads = _read_payloads_between(sf, ibstream, addr4begin, addr4end)
            yield payloads
            addr4begin = addr4end


    def iter_payloadss4token__backward(sf, ibstream, /):
        '-> Iter<[payload]>/Iter<bytes>'
        addr4end = ibstream.tell()
        valid = True
        while not addr4end == 0:
            addr4begin = sf.seek_to_first_of_prev_token4decode_(valid, ibstream)
            payloads = _read_payloads_between(sf, ibstream, addr4begin, addr4end)
            yield payloads
            addr4end = addr4begin
            ibstream.seek(addr4end)

def _read_payloads_between(sf, ibstream, addr4begin, addr4end, /):
    # %s/ibstream/ibbstream/g
    # buffered binary input stream ==>> .read(sz) greedy
    assert ibstream.tell() == addr4begin
    sz = addr4end - addr4begin
    assert sz > 0
    bs = ibstream.read(sz)
    if not len(bs)==sz:raise logic-err

    payloads = map(snd, map(sf.decode_uint8byte__case, bs))
    payloads = bytes(payloads)
    assert ibstream.tell() == addr4end
    return payloads

class IByteDecoder__using_num_head1s(IByteDecoder):
    __slots__ = ()
    @abstractmethod
    def num_head1s2byte_case(sf, num_head1s, /):
        'num_head1s/[0..=8] -> byte_case/Case4ByteDecoder'
    @abstractmethod
    def decode_uint8byte__num_head1s(sf, u, /):
        '[0..<256] -> (num_head1s, payload) #num_head1s :: [0..=8] #payload :: uint'
    @override
    def decode_uint8byte__case(sf, u, /):
        '[0..<256] -> (byte_case, payload) #payload :: uint'
        (num_head1s, payload) = sf.decode_uint8byte__num_head1s(u)
        byte_case = sf.num_head1s2byte_case(num_head1s)
        check_type_is(byte_case)
        return (byte_case, payload)

class IByteDecoder__using_max_num_head1s(IByteDecoder__using_num_head1s):
    __slots__ = ()
    @abstractmethod
    def get_max_num_head1s(sf, /):
        '-> max_num_head1s/[0..=8]'
    @override
    def decode_uint8byte__num_head1s(sf, u, /):
        '[0..<256] -> (num_head1s, payload) #num_head1s :: uint%max_num_head1s #payload :: uint'
        check_int_ge_lt(0, 256, u)
        num_head1s = byte2num_head1s[u]
        num_head1s = min(num_head1s, sf.get_max_num_head1s())
        tail_mask = num_head1s2tail_mask[num_head1s]
        payload = u&tail_mask
        return (num_head1s, payload)
    r'''
    def __init__(sf, max_num_head1s, /):
        check_int_ge_le(0, 8, max_num_head1s)
        sf.max_num_head1s = max_num_head1s
    #'''
class _ByteDecoder(IByteDecoder__using_max_num_head1s):
    __slots__ = ()
    #@abstractmethod
    _max_num_head1s_ = 0
    #@abstractmethod
    _num_head1s2byte_case_ = {}
    #@abstractmethod
    _byte_case2num_head1s_ = {}
    @override
    def num_head1s2byte_case(sf, num_head1s, /):
        'num_head1s/[0..=8] -> byte_case/Case4ByteDecoder'
        cls = type(sf)
        return cls._num_head1s2byte_case_[num_head1s]
    @override
    def get_max_num_head1s(sf, /):
        '-> max_num_head1s/[0..=8]'
        cls = type(sf)
        return cls._max_num_head1s_
    @override
    def does_support_forward_decode(sf, /):
        '-> bool'
        return Case4ByteDecoder.last in sf._num_head1s2byte_case_.values()
    @override
    def does_support_backward_decode(sf, /):
        '-> bool'
        return Case4ByteDecoder.first in sf._num_head1s2byte_case_.values()
    @override
    def token5payloads(sf, payloads, /):
        'payloads -> token/uint/big_endian'
        #
        #sf.does_support_bidirectional_decode
        fwd = sf.does_support_forward_decode()
        bwd = sf.does_support_backward_decode()
        bid = fwd and bwd
        if not (fwd or bwd): raise logic-err

        L = len(payloads)
        assert L > 0
        cls = type(sf)
        c2n = cls._byte_case2num_head1s_
        if bid and L == 1:
            byte_case = Case4ByteDecoder.singleton
            num_head1s = c2n[byte_case]
            [u] = payloads
        else:
            if bid:
                assert L >= 2
            m = cls._max_num_head1s_
            if bwd:
                n0 = c2n[Case4ByteDecoder.first]
                t0 = num_bits4byte-n1-(n0<m)
            if 1:
                n1 = c2n[Case4ByteDecoder.fragment]
                t1 = num_bits4byte-n1-(n1<m)
            if fwd:
                n2 = c2n[Case4ByteDecoder.last]
                t2 = num_bits4byte-n2-(n2<m)

            if bwd:
                u0 = payloads[0]
                u = u0
                t = t0
            else:
                u = 0
                t = 0

            mid_begin = 0+bool(bwd)
            mid_end = L - bool(fwd)
            mids = payloads[mid_begin:mid_end]
            for u1 in mids:
                u <<= t1
                u ^= u1
            t += t1*len(mids)

            if fwd:
                u2 = payloads[-1]
                u <<= t2
                u ^= u2
                t += t2
        u, t
        token = u
        return token


class ByteDecoder__1s0(_ByteDecoder):
    __slots__ = ()
    #@override
    _max_num_head1s_ = 1
    #@override
    _num_head1s2byte_case_ = (
        {1:Case4ByteDecoder.fragment
        ,0:Case4ByteDecoder.last
        })
    #@override
    _byte_case2num_head1s_ = inv__k2v_to_v2k(_num_head1s2byte_case_)


class ByteDecoder__201(_ByteDecoder):
    __slots__ = ()
    #@override
    _max_num_head1s_ = 2
    #@override
    _num_head1s2byte_case_ = (
        {2:Case4ByteDecoder.first
        ,0:Case4ByteDecoder.fragment
        ,1:Case4ByteDecoder.last
        })
    #@override
    _byte_case2num_head1s_ = inv__k2v_to_v2k(_num_head1s2byte_case_)

class ByteDecoder__302x1(_ByteDecoder):
    __slots__ = ()
    #@override
    _max_num_head1s_ = 3
    #@override
    _num_head1s2byte_case_ = (
        {3:Case4ByteDecoder.first
        ,0:Case4ByteDecoder.fragment
        ,2:Case4ByteDecoder.last
        ,1:Case4ByteDecoder.singleton
        })
    #@override
    _byte_case2num_head1s_ = inv__k2v_to_v2k(_num_head1s2byte_case_)

class ByteDecoder__312x0(_ByteDecoder):
    __slots__ = ()
    #@override
    _max_num_head1s_ = 3
    #@override
    _num_head1s2byte_case_ = (
        {3:Case4ByteDecoder.first
        ,1:Case4ByteDecoder.fragment
        ,2:Case4ByteDecoder.last
        ,0:Case4ByteDecoder.singleton
        })
    #@override
    _byte_case2num_head1s_ = inv__k2v_to_v2k(_num_head1s2byte_case_)









class 首比特囗类别(Enum):
    负载比特囗值自由 = auto()
    格式比特囗值一 = auto()
    格式比特囗值零 = auto()
    格式比特囗值相反于前比特 = auto()
    格式比特囗值相同于前比特 = auto()
_kind2nm = (
    {首比特囗类别.负载比特囗值自由:'X'
    ,首比特囗类别.格式比特囗值零:'0'
    ,首比特囗类别.格式比特囗值一:'1'
    ,首比特囗类别.格式比特囗值相反于前比特:'~'
    ,首比特囗类别.格式比特囗值相同于前比特:'='
    }
)

#
#首比特类别昵称字符串:基本样式:
_ptn__OIXEFs = r'^1[01X=~]*0$'
    #禁止异码尾首交叠囗囗约定囗囗首比特流始于一终于零
_rex__OIXEFs = re.compile(_ptn__OIXEFs)
_ptn__to_mk_OIs_or_XYs = r'([01][01=~]*|[X][=~]*)'
_rex__to_mk_OIs_or_XYs = re.compile(_ptn__to_mk_OIs_or_XYs)
_ptn__OIs_or_XYs = r'([01]+|X[XY]*)'
_rex__OIs_or_XYs = re.compile(_ptn__OIs_or_XYs)
_ptn__to_get_lens4OIs_or_XYs = r'(0+|1+|X+|Y+)'
_rex__to_get_lens4OIs_or_XYs = re.compile(_ptn__to_get_lens4OIs_or_XYs)
def _check__OIXEFs(首比特类别昵称字符串, /):
    if not _rex__OIXEFs.fullmatch(首比特类别昵称字符串): raise TypeError
def _check__OIs_or_XYs(OIs_or_XYs, /):
    if not _rex__OIs_or_XYs.fullmatch(OIs_or_XYs): raise TypeError
#首比特串 拆成 多个 独立块
def _split_into__cased_lens__list(首比特类别昵称字符串, /):
    'OIXEFs -> [cased_lens]/[(case/[0..=2], lens/[pint])]'
    ls = _split_into__OIs_or_XYs__list(首比特类别昵称字符串)
    ls = [*map(cased_lens_from_OIs_or_XYs, ls)]
    return ls
def _split_into__OIs_or_XYs__list(首比特类别昵称字符串, /):
    'OIXEFs -> [(OIs|XYs)]'
    _check__OIXEFs(首比特类别昵称字符串)
    ls = _rex__to_mk_OIs_or_XYs.split(首比特类别昵称字符串)
    if not len(ls)%2==1: raise logic-err
    if any(ls[::2]): raise logic-err
    ls = ls[1::2]
    if not all(ls): raise logic-err


    s0_2_oi = {'1':'01', '0':'10', 'X':'YX'}
    def ch2oi_(oi, ch, /):
        if ch in '01':
            oi = s0_2_oi[ch]
        elif ch in '=~':
            oi = oi if ch=='=' else oi[::-1]
        else:
            if not ch in '01=~': raise logic-err
            raise logic-err
        return oi
    def f(s, /):
        s0 = s[0]
        oi = s0_2_oi[s0]

        assert oi[1]==s0
        yield oi[1]

        for ch in s[1:]:
            oi = ch2oi_(oi, ch)
            yield oi[1]
    def g(s, /):
        return ''.join(f(s))
    ls = [*map(g, ls)]
    return ls
def cased_lens_from_OIs_or_XYs(OIs_or_XYs, /):
    '(OIs|XYs) -> (case/[0..=2], lens/[pint])'
    _check__OIs_or_XYs(OIs_or_XYs)
    ch = OIs_or_XYs[0]
    case = '01X'.index(ch)

    ls = _rex__to_get_lens4OIs_or_XYs.split(OIs_or_XYs)
    if not len(ls)%2==1: raise logic-err
    if any(ls[::2]): raise logic-err
    ls = ls[1::2]
    if not all(ls): raise logic-err

    lens = [*map(len, ls)]
    if not lens: raise logic-err
    if not all(lens): raise logic-err
    return (case, lens)




if 0:
    #多单元首比特联合编码方案囗首尾纯色相反:首比特串囗正则表达式
    _c5__afterI = r'(?:=*~=*~)*(P<numI_neg1>[1X=]*)'
    _c5__1_afterI = fr'[1X]{_c5__afterI!s}'
    _c5__0f_afterI = fr'[0X]=*~{_c5__afterI!s}'

    _c5__afterO = r'(?:=*~=*~)*(P<numI_neg1>[0X=]*)'
    _c5__0_afterO = fr'[0X]{_c5__afterO!s}'
    _c5__1f_afterO = fr'[1X]=*~{_c5__afterO!s}'
def 囗字数之首比特类别昵称字符串囗(sf, Lw, /):
    if not sf.总长度是否合法囗(Lw):raise TypeError
    首比特类别昵称字符串 = ''.join(_kind2nm[kind] for kind in sf.字数之正向枚举各字首比特类别囗(Lw))

    if not len(首比特类别昵称字符串)==Lw: raise logic-err
    if not (首比特类别昵称字符串.count(_kind2nm[首比特囗类别.负载比特囗值自由])+(sf.字长囗()-1)*Lw == sf.字数之负载比特数囗(Lw)): raise logic-err
    return 首比特类别昵称字符串
def 字数之首比特类别昵称字符串囗(sf, Lw, /):
    首比特类别昵称字符串 = 囗字数之首比特类别昵称字符串囗(sf, Lw)
    if type(sf) is 多单元首比特联合编码方案囗首尾纯色相反:
        try:
            检查囗首比特类别昵称字符串囗囗首尾纯色相反(sf, 首比特类别昵称字符串)
        except Exception as e:
            raise Exception((e, sf, Lw, 首比特类别昵称字符串))
    return 首比特类别昵称字符串
def 检查囗首比特类别昵称字符串囗囗首尾纯色相反(sf, 首比特类别昵称字符串, /):
    if not type(sf) is 多单元首比特联合编码方案囗首尾纯色相反: raise TypeError

    z = sf._z
    if not z >= 2: raise TypeError
    if not 首比特类别昵称字符串.startswith('1'*z+'0'): raise TypeError
    if not 首比特类别昵称字符串.endswith('1'+'0'*z): raise TypeError
    cased_lens__list4find_z1_or_z0 = _split_into__cased_lens__list(首比特类别昵称字符串[1:-1])
    ps = [(0, cased_lens__list4find_z1_or_z0), (1, cased_lens__list4find_z1_or_z0)]
    for (case4first, lens) in cased_lens__list4find_z1_or_z0:
        if not max(lens) < z: raise TypeError

    for case4target in [0,1]:
      case4nontarget = 1^case4target
      acc = 0
      for (case4first, lens) in cased_lens__list4find_z1_or_z0:
        if case4first == case4nontarget:
            acc = 0
        else:
            acc += lens[0]
            if not acc < z: raise TypeError
        L = len(lens)
        if L==1:
            continue
        if case4first == 2:
            #X
            acc = lens[-1]
        else:
            odd = L&1
            case4last = 1^odd^case4first
            if case4last == case4target:
                acc = lens[-1]
            else:
                acc = 0
#end-def 检查囗首比特类别昵称字符串囗囗首尾纯色相反(sf, 首比特类别昵称字符串, /):




class 基类囗多单元首比特联合编码方案(ABC):
    r'''[[[
see:负载比特数与字数的关系囗囗计算框架

    #]]]'''
    __slots__ = ()
    #抽象方法:
    @abstractmethod
    def 所有构造编码方案的参数囗(sf, /):
        '[所有构造编码方案的参数囗<编码方案>(W,编码参数;) :: (W,编码参数...)]'
    @abstractmethod
    def 字长囗(sf, /):
        '[字长囗<编码方案>(W,编码参数;) :: W]'
    @abstractmethod
    def 编码参数是否合法囗(sf, /):
        '[编码参数是否合法囗<编码方案>(W,编码参数;) :: bool]'
    @abstractmethod
    def 最高负载率的极限囗(sf, /):
        '[最高负载率的极限囗<编码方案>(W,编码参数;) :: 负载率/分数]'
    @abstractmethod
    def 最小总长度囗(sf, /):
        '[最小总长度囗<编码方案>(W,编码参数;) :: Lw]'
    @abstractmethod
    def 总长度是否合法囗(sf, Lw, /):
        '[总长度是否合法囗<编码方案>(W,编码参数;) :: Lw -> bool]'
    @abstractmethod
    def 字数之负载比特数囗(sf, Lw, /):
        '[字数之负载比特数囗<编码方案>(W,编码参数;) :: Lw -> Lb]'
    @abstractmethod
    def 字数之位置之该字首比特类别囗(sf, Lw, idx, /):
        '[字数之位置之该字首比特类别囗<编码方案>(W,编码参数;) :: Lw -> idx/[0..<Lw] -> 首比特囗类别]'



    #可覆盖囗具象方法:
    def 枚举囗合法总长度囗囗大于等于囗(sf, Lw__lowbound, /):
        '[枚举囗合法总长度囗囗大于等于囗<编码方案>(W,编码参数;) :: Lw__lowbound -> [Lw]]'
        Lw0 = max(sf.最小总长度囗(), Lw__lowbound)
        return filter(sf.总长度是否合法囗, count(Lw0))

    def 字数之正向枚举各字首比特类别囗(sf, Lw, /):
        '[字数之正向枚举各字首比特类别囗<编码方案>(W,编码参数;) :: Lw -> [首比特囗类别]{len=Lw}]'
        for idx in range(Lw):
            yield sf.字数之位置之该字首比特类别囗(Lw, idx)



    #具象方法:
    def __repr__(sf, /):
        args = sf.所有构造编码方案的参数囗()
        return repr_helper(sf, *args)
    def 负载比特数之字数下界估计囗(sf, Lb, /):
        '[负载比特数之字数下界估计囗<编码方案>(W,编码参数;) :: Lb -> Lw__lowbound]'
        W = sf.字长囗()
        最高负载率的极限 = sf.最高负载率的极限囗()
        check_type_is(Fraction, 最高负载率的极限)
        Lw__lowbound = ceil(Lb/最高负载率的极限/W)
        Lw__lowbound = max(sf.最小总长度囗(), Lw__lowbound)
        return Lw__lowbound


    def 负载比特数之字数过滤器囗(sf, Lb, Lw_ls, /):
        '[负载比特数之字数过滤器囗<编码方案>(W,编码参数;) :: Lb -> [Lw] -> [Lw]]'
        it = filter(sf.总长度是否合法囗, Lw_ls)
        return (Lw for Lw in it if Lb <= sf.字数之负载比特数囗(Lw))

    def 负载比特数之字数囗(sf, Lb, /):
        '[负载比特数之字数囗<编码方案>(W,编码参数;) :: Lb -> Lw]'
        check_int_ge(0, Lb)
        W = sf.字长囗()
        最高负载率的极限 = sf.最高负载率的极限囗()
        check_type_is(Fraction, 最高负载率的极限)
        if not (Lb==0 or 最高负载率的极限 > 0): raise TypeError
        Lw__lowbound = sf.负载比特数之字数下界估计囗(Lb)
        Lw_ls = sf.枚举囗合法总长度囗囗大于等于囗(Lw__lowbound)
        Lw_ls = sf.负载比特数之字数过滤器囗(Lb, Lw_ls)
        for Lw in Lw_ls:
            break
        else:
            raise logic-err
        return Lw

class 多单元首比特联合编码方案囗首尾纯色相反(基类囗多单元首比特联合编码方案):
    r'''[[[
编码五-->多单元首比特联合编码方案囗首尾纯色相反
see:负载比特数与字数的关系囗囗计算框架
see:字数之负载比特数囗囗编码五囗退化囗对称囗
see:使用囗计算框架囗实现囗负载比特数之字数囗囗编码五囗退化囗对称囗
see:字数之位置之该字首比特类别囗囗编码五囗退化囗对称囗

    #]]]'''
    __slots__ = '_W _z'.split()
    def __init__(sf, W, z, /):
        sf._W = W
        sf._z = z
        sf.编码参数是否合法囗()

    #抽象方法:
    @override
    def 所有构造编码方案的参数囗(sf, /):
        '[所有构造编码方案的参数囗<编码方案>(W,编码参数;) :: (W,编码参数...)]'
        W = sf._W
        z = sf._z
        return (W, z)
    @override
    def 字长囗(sf, /):
        '[字长囗<编码方案>(W,编码参数;) :: W]'
        W = sf._W
        return W
    @override
    def 编码参数是否合法囗(sf, /):
        '[编码参数是否合法囗<编码方案>(W,编码参数;) :: bool]'
        W = sf._W
        z = sf._z
        check_int_ge(1, W)
        check_int_ge(2, z)
    @override
    def 最高负载率的极限囗(sf, /):
        '[最高负载率的极限囗<编码方案>(W,编码参数;) :: 负载率/分数]'
        W = sf._W
        z = sf._z
        return 1- Fraction(2,W*z)
    @override
    def 最小总长度囗(sf, /):
        '[最小总长度囗<编码方案>(W,编码参数;) :: Lw]'
        z = sf._z
        return 2*z
    @override
    def 总长度是否合法囗(sf, Lw, /):
        '[总长度是否合法囗<编码方案>(W,编码参数;) :: Lw -> bool]'
        z = sf._z
        return (Lw>=2*z and not Lw == 2*z+1 and (z>=3 or Lw%2 == 0))
    @override
    def 字数之负载比特数囗(sf, Lw, /):
        '[字数之负载比特数囗<编码方案>(W,编码参数;) :: Lw -> Lb]'
        #see:字数之负载比特数囗囗编码五囗退化囗对称囗
        if not sf.总长度是否合法囗(Lw):raise TypeError((sf, Lw))
        W = sf._W
        z = sf._z
        if Lw in [2*z,2*z+2] or z==2:
            return (W-1)*Lw

        #分支:[[z>=3][Lw>=2*z+3]]
        (q,r) = divmod(Lw-(2*z+2), z)
        assert z>=3 or not r==z-1
        Lnhb = (2*z+2) +q*2 +(r==z-1)
        return W*Lw -Lnhb
    @override
    def 字数之位置之该字首比特类别囗(sf, Lw, idx, /):
        '[字数之位置之该字首比特类别囗<编码方案>(W,编码参数;) :: Lw -> idx/[0..<Lw] -> 首比特囗类别]'
        #see:字数之位置之该字首比特类别囗囗编码五囗退化囗对称囗
        if not sf.总长度是否合法囗(Lw):raise TypeError
        check_int_ge_lt(0,Lw, idx)
        W = sf._W
        z = sf._z
        if idx < z:
            return 首比特囗类别.格式比特囗值一
        if not idx+z < Lw:
            return 首比特囗类别.格式比特囗值零
        #now: [Lw > 2*z][z <= idx < Lw-z]
        if idx==z:
            return 首比特囗类别.格式比特囗值零
        if idx+z+1 == Lw:
            return 首比特囗类别.格式比特囗值一
        #now: [Lw > 2*z+2][(z+1) <= idx < Lw-(z+1)]
        ir = (idx-(z+1))%z
        if ir < z-2:
            return 首比特囗类别.负载比特囗值自由
        if (idx+z+2 == Lw and z>=3 and ir==z-2):
            return 首比特囗类别.格式比特囗值相反于前比特
        if ir == z-2:
            return 首比特囗类别.格式比特囗值一
        if ir == z-1:
            return 首比特囗类别.格式比特囗值零
        raise logic-err



    #可覆盖囗具象方法:
    @override
    def 枚举囗合法总长度囗囗大于等于囗(sf, Lw__lowbound, /):
        '[枚举囗合法总长度囗囗大于等于囗<编码方案>(W,编码参数;) :: Lw__lowbound -> [Lw]]'
        z = sf._z
        step = 1+(z==2)
        if Lw__lowbound <= 2*z:
            return chain([2*z], count(2*z+2, step))
        else:
            return count(max(Lw__lowbound,2*z+2), step)
        raise logic-err
        pass
        if Lw__lowbound <= 2*z:
            Lw0 = 2*z
        elif Lw__lowbound <= 2*z+2:
            Lw0 = 2*z+2
        else:
            Lw0 = Lw__lowbound
        Lw1 = Lw0+(Lw0%2) if z==2 else Lw0

        if Lw1 == 2*z:
            return chain([Lw1], count(Lw1+2, 1+(z==2)))
        return count(Lw1, 1+(z==2))




class 多单元首比特联合编码方案囗首尾纯色相同(基类囗多单元首比特联合编码方案):
    r'''[[[
编码四-->多单元首比特联合编码方案囗首尾纯色相同
see:负载比特数与字数的关系囗囗计算框架
see:字数之负载比特数囗囗编码四囗
see:使用囗计算框架囗实现囗负载比特数之字数囗囗编码四囗
see:字数之位置之该字首比特类别囗囗编码四囗


    #]]]'''
    __slots__ = '_W _n'.split()
    def __init__(sf, W, n, /):
        sf._W = W
        sf._n = n
        sf.编码参数是否合法囗()

    #抽象方法:
    @override
    def 所有构造编码方案的参数囗(sf, /):
        '[所有构造编码方案的参数囗<编码方案>(W,编码参数;) :: (W,编码参数...)]'
        W = sf._W
        n = sf._n
        return (W, n)
    @override
    def 字长囗(sf, /):
        '[字长囗<编码方案>(W,编码参数;) :: W]'
        W = sf._W
        return W
    @override
    def 编码参数是否合法囗(sf, /):
        '[编码参数是否合法囗<编码方案>(W,编码参数;) :: bool]'
        W = sf._W
        n = sf._n
        check_int_ge(1, W)
        check_int_ge(1, n)
    @override
    def 最高负载率的极限囗(sf, /):
        '[最高负载率的极限囗<编码方案>(W,编码参数;) :: 负载率/分数]'
        W = sf._W
        n = sf._n
        N,D = ((2, 3*W) if n==1 else (1, W*n))
        return 1- Fraction(N,D)
    @override
    def 最小总长度囗(sf, /):
        '[最小总长度囗<编码方案>(W,编码参数;) :: Lw]'
        n = sf._n
        return n+4
    @override
    def 总长度是否合法囗(sf, Lw, /):
        '[总长度是否合法囗<编码方案>(W,编码参数;) :: Lw -> bool]'
        n = sf._n
        return (Lw==n+4 or Lw>=2*n+6)
    @override
    def 字数之负载比特数囗(sf, Lw, /):
        '[字数之负载比特数囗<编码方案>(W,编码参数;) :: Lw -> Lb]'
        #see:字数之负载比特数囗囗编码四囗
        if not sf.总长度是否合法囗(Lw):raise TypeError
        W = sf._W
        n = sf._n
        if Lw<=2*n+7:
            return (W-1)*Lw
        elif n==1:
            return (W-1)*Lw + (Lw-8)//3
        else:
            return W*Lw - (Lw-7)//n - 2*n -5
        pass
    @override
    def 字数之位置之该字首比特类别囗(sf, Lw, idx, /):
        '[字数之位置之该字首比特类别囗<编码方案>(W,编码参数;) :: Lw -> idx/[0..<Lw] -> 首比特囗类别]'
        #see:字数之位置之该字首比特类别囗囗编码四囗
        if not sf.总长度是否合法囗(Lw):raise TypeError
        check_int_ge_lt(0,Lw, idx)
        W = sf._W
        n = sf._n
        if idx < n+3:
            if (idx == 1 or idx == n+2):
                return 首比特囗类别.格式比特囗值零
            else:
                return 首比特囗类别.格式比特囗值一
        if not idx+n+3 < Lw:
            # (idx+n+3) 代替 (idx+n+2)
            #     因为 除最短情形，其他一致为1
            if not idx+2 < Lw:
                return 首比特囗类别.格式比特囗值零
            else:
                return 首比特囗类别.格式比特囗值一
        #now: [Lw > 2*n+6][(n+3) <= idx < Lw-(n+3)]
        if n==1:
            ir = (idx-(n+3))%3
            if ir==2:
                return 首比特囗类别.负载比特囗值自由
            else:
                return 首比特囗类别.格式比特囗值一
        if n>=2:
            if idx==n+3:
                return 首比特囗类别.格式比特囗值一
            ir = (idx-(n+4))%n
            if (ir==n-2 and not idx+n+4==Lw):
                return 首比特囗类别.格式比特囗值零
            else:
                return 首比特囗类别.负载比特囗值自由
        raise logic-err



    #可覆盖囗具象方法:
    @override
    def 枚举囗合法总长度囗囗大于等于囗(sf, Lw__lowbound, /):
        '[枚举囗合法总长度囗囗大于等于囗<编码方案>(W,编码参数;) :: Lw__lowbound -> [Lw]]'
        n = sf._n
        if Lw__lowbound <= n+4:
            return chain([n+4], count(2*n+6))
        else:
            return count(max(Lw__lowbound,2*n+6))
        pass



多单元首比特联合编码方案囗首尾纯色相反(1,2)
多单元首比特联合编码方案囗首尾纯色相同(1,1)



def 枚举囗完全累计序号囗囗多单元首比特联合编码方案囗首尾纯色相反囗囗扩展囗任意格式囗(W, z, /):
    r'''[[[
:: W -> z -> Iter (Lw, acc_total4Lw_W, total4Lw_W, vars4Weq1/(acc_total4Lw, total4Lw, xcount2acc))
:: W/[1..] -> z/[2..] -> Iter (Lw/[z..], acc_total4Lw_W/[0..], total4Lw_W/[0..], vars4Weq1/(acc_total4Lw/[0..], total4Lw/[0..], xcount2acc/[uint]{len=2*z-1}))
[total4Lw_W==total4Lw*2**((W-1)*Lw)]
[[Lw>=z][0<=total4Lw<=acc_total4Lw][sum(xcount2acc) >= 1][total4Lw == xcount2acc[z-1]]]
[[num_tail_0s <- [1..=z]] -> [total_for_num_tail_0s_1s__(W,z;num_tail_0s,0) == xcount2acc[num_tail_0s-1]]]
[[num_tail_1s <- [1..=z-1]] -> [total_for_num_tail_0s_1s__(W,z;0,num_tail_1s) == xcount2acc[z+num_tail_1s-1]]]


[xcount <- [0..=2*z-2]]
[num_tail_0s <- [0..=z]]
[num_tail_1s <- [0..=z-1]]
[(num_tail_1s==0)=!=(num_tail_0s==0)]
[num_tail_0s == 1+xcount if xcount<z else 0]
[num_tail_1s == 0 if xcount<z else xcount-z+1]
#]]]'''
    check_int_ge(1, W)
    acc_total4Lw_W = 0
    for (Lw, acc_total4Lw, total4Lw, xcount2acc) in 枚举囗完全累计序号囗囗多单元首比特联合编码方案囗首尾纯色相反囗囗扩展囗任意格式囗囗字长为一囗(z):
        total4Lw_W = total4Lw << ((W-1)*Lw)
        acc_total4Lw_W += total4Lw_W
        vars4Weq1 = (acc_total4Lw, total4Lw, xcount2acc)
        yield (Lw, acc_total4Lw_W, total4Lw_W, vars4Weq1)
def 枚举囗完全累计序号囗囗多单元首比特联合编码方案囗首尾纯色相反囗囗扩展囗任意格式囗囗字长为一囗(z, /):
    r'''[[[
:: z -> Iter (Lw, acc_total4Lw, total4Lw, xcount2acc)
:: z/[2..] -> Iter (Lw/[z..], acc_total4Lw/[0..], total4Lw/[0..], xcount2acc/[uint]{len=2*z-1})
[[W==1][Lw>=z][0<=total4Lw<=acc_total4Lw][sum(xcount2acc) >= 1][total4Lw == xcount2acc[z-1]]]
[[num_tail_0s <- [1..=z]] -> [total_for_num_tail_0s_1s__(W=1,z;num_tail_0s,0) == xcount2acc[num_tail_0s-1]]]
[[num_tail_1s <- [1..=z-1]] -> [total_for_num_tail_0s_1s__(W=1,z;0,num_tail_1s) == xcount2acc[z+num_tail_1s-1]]]



[W==1]
[xcount <- [0..=2*z-2]]
[num_tail_0s <- [0..=z]]
[num_tail_1s <- [0..=z-1]]
[(num_tail_1s==0)=!=(num_tail_0s==0)]
[num_tail_0s == 1+xcount if xcount<z else 0]
[num_tail_1s == 0 if xcount<z else xcount-z+1]
#]]]'''
    check_int_ge(2, z)
    idx_rng4num_tail_0s = range(0,z)
    idx_rng4num_tail_1s = range(z,2*z-1)
    xcount2acc = [0]*(2*z-1)
    xcount2acc[-1] = 1
    Lw = z
    acc_total4Lw = 0
    while 1:
        total4Lw = xcount2acc[z-1]
        #if total4Lw:
        if 1:
            acc_total4Lw += total4Lw
            yield (Lw, acc_total4Lw, total4Lw, xcount2acc)
        ######################
        #acc for append 0
        new_xcount2acc = [sum(xcount2acc[z:]), *xcount2acc[:z-1]]
        ######################
        #acc for append 1
        new_xcount2acc += [sum(xcount2acc[:z-1]), *xcount2acc[z:-1]]
        assert len(new_xcount2acc)==len(xcount2acc)
        ######################
        Lw += 1
        xcount2acc = new_xcount2acc
#end-def 枚举囗完全累计序号囗囗多单元首比特联合编码方案囗首尾纯色相反囗囗扩展囗任意格式囗囗字长为一囗(z, /):
#end-def 枚举囗完全累计序号囗囗多单元首比特联合编码方案囗首尾纯色相反囗囗扩展囗任意格式囗(W, z, /):





from seed.io.num_head1s_of_byte import byte2num_head1s
from seed.io.num_head1s_of_byte import Case4ByteDecoder, ByteDecoder__1s0, ByteDecoder__201, ByteDecoder__302x1, ByteDecoder__312x0


from seed.io.num_head1s_of_byte import 首比特囗类别, 基类囗多单元首比特联合编码方案, 多单元首比特联合编码方案囗首尾纯色相反, 多单元首比特联合编码方案囗首尾纯色相同
from seed.io.num_head1s_of_byte import _kind2nm, 字数之首比特类别昵称字符串囗, 检查囗首比特类别昵称字符串囗囗首尾纯色相反
from seed.io.num_head1s_of_byte import 枚举囗完全累计序号囗囗多单元首比特联合编码方案囗首尾纯色相反囗囗扩展囗任意格式囗, 枚举囗完全累计序号囗囗多单元首比特联合编码方案囗首尾纯色相反囗囗扩展囗任意格式囗囗字长为一囗

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +IGNORE_EXCEPTION_DETAIL

