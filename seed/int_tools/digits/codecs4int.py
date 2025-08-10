#__all__:goto
doing...
TODO:goto
r'''[[[
e ../../python3_src/seed/int_tools/digits/codecs4int.py
view others/数学/编程/设计/自定义字符编码.txt
view others/数学/编程/设计/自定义字符编码-兼容utf8.txt
view others/数学/编程/设计/自定义编码之要点.txt

seed.int_tools.digits.codecs4int
py -m nn_ns.app.debug_cmd   seed.int_tools.digits.codecs4int -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.int_tools.digits.codecs4int:__doc__ -ht # -ff -df



[[
view others/数学/编程/设计/自定义字符编码.txt
本模块所有编码器满足以下约束:
    支持词典序#lexicographic order
    分级前置长度#逐步推进分级前置长度型编码方案
    ++{受控范围内胞串内部向外识别两端边界,双端内敛,字节串搜索,字节串词典序}

]]
[[
@20250615
简化设计:
    ===
    假设:充分大之后，躯部为二幂胞串:
        [[充分大] => [躯部::[uint%(2**C)]]]
    ===
    假设:充分大之后，整体分为五部分(只有两层长度):
        [[充分大] => [整编码==固定头部牜充分大(可能含动态爻元=>计入固定偏移量)++动态爻元计数用胞串(长度纟长度纟躯部)++?混合胞?(可能混合含半胞纟动态爻元丶半胞纟长度纟躯部)++胞串纟长度纟负载++胞串纟负载]]
            # [躯部==后四部分|后两部分(没有混合胞)]
            # * [躯部==后两部分]:比如:[码胞::[uint%10]][躯胞::uint%8][用『9』来做动态爻元][没有混合胞]
    ===
]]
[[
@20250708
[编码==宏头胞++躯部]
[宏头胞 :: uint%H]
[躯部 :: [躯胞]]
[躯胞 :: uint%R]
#初版:[分区表纟宏头胞 :: [(总层数/uint,数目/uint,映射)]]
[分区表纟宏头胞 :: [(总层数/uint,数目/uint,[(层序数/uint,映射)])]]
    [映射 :: (偏移量/uint|离散映射表/[uint])]
    [偏移扌(映射;uint%数目) =[def]= ((uint%数目+偏移量)|离散映射表[(uint%数目)])]
        #偏移于某些层
[H==表达空间规模纟宏头胞==sum(map(snd,分区表纟宏头胞))]
    #第0层=>偏移扌(映射;uint%数目) 是 立即数
    #第n+1层=>偏移扌(映射;uint%数目) 是 长度{第n层}
    #以上是 不规则的有限区
    #第-1层=>偏移扌(映射;uint%数目) 是 动态扩展(宏头胞)/规则的无限区
    #   ？自动扩展方案？
    #第-2层=>特殊值区(比如:无穷大)
[编码空间规模纟不规则的有限区 =[def]= 1+max(最大值纟表达{第n层} for n in [0..])]
    作为 阈值 分隔 有限区、无限区
[分区表纟躯胞冃颈胞 :: [(总层数/uint,数目/uint,映射)]]
    => 自动扩展方案
为啥区分出『宏头胞』？
    1. 比如:采用『数字+英文字母』作字母表:
        为避免标识名，令 头胞 为数字
        为避免全数字，简单点，令 颈胞 为字母
        => regex"([69][A-Z])[0-578A-Z]*"
        其中:
            regex"([69][A-Z])" 是 宏头胞(==头胞+颈胞)
            regex"[0-578A-Z]" 是 躯胞
            #若 二幂 => 考虑改动:([0-578A-Z] --> [0-5A-Z]or[0-578A-X])
    2. 为了 前刹(左端内敛)，简单点，令  符集纟头胞 与 符集纟非头胞 无交集。
        或:
        => regex"([89][A-Y])[1-7A-Y]*"
            # 保留[0Z] # 正负无穷大
            # [A-Y]:25:0b11001==16+8+1
        #不简单的方案，比如:多单元联合前缀-单端版
]]
[[
如何表达 任意基数的进位数制？
    基数任意大 => 数字 必须要能 表达 任意自然数
    数字的编码 必须 内敛(前刹&&后刹)
==>>:
radix_digit的一个编码方案:
    字母表:[0-9A-Za-z]
    # [10+26*2==62==30+32==(16+8+4+2)+32]
    头胞集:[0-9A-T] #30
    躯胞集:[U-Za-z] #32
        #颈身躯胞
    # regex"[0-9A-T][U-Za-z]*"
    单胞码: regex"[0-9A-F]"
        # 16==10+6==2**4
    双胞码: regex"[G-N][U-Za-z]"
        # 256==8*32==2**8
    三胞码: regex"[O-R][U-Za-z][U-Za-z]"
        # 4096==4*32*32==2**12
    三层码: regex"[ST][U-Za-z]+"
        # 见下面:『动态爻元 vs 动态苞元』
        # !! 使用 动态爻元 而非 动态苞元
        regex"S([U-Za-z])[U-Za-z]{len==第一层数}"
        regex"S([U-Za-z][U-Za-z]{0})[U-Za-z]{len==第一层数}"
            # [0..<32**31]
            # [0..<2**155]
        [n>=0]:
            # !! 动态爻元
            # 32==16+8+4+2+1+1
            # [U-Za-z]==[U-Za-j]+[k-r]+[s-v]+[wx]+[y]+[z]
            regex"(Tz{n})([U-Za-j][U-Za-z]{(1+5*n+1)-(n+1)})[U-Za-z]{len==第一层数}"
                # [0..<32**(16*32**(4*n+1)-1)]
                # [0..<32**(2**(20*n+9)-1)]
            regex"(Tz{n})([klmnopqr][U-Za-z]{(1+5*n+2)-(n+1)})[U-Za-z]{len==第一层数}"
                # [0..<32**(8*32**(4*n+2)-1)]
                # [0..<32**(2**(20*n+13)-1)]
            regex"(Tz{n})([stuv][U-Za-z]{(1+5*n+3)-(n+1)})[U-Za-z]{len==第一层数}"
                # [0..<32**(4*32**(4*n+3)-1)]
                # [0..<32**(2**(20*n+17)-1)]
            regex"(Tz{n})([wx][U-Za-z]{(1+5*n+4)-(n+1)})[U-Za-z]{len==第一层数}"
                # [0..<32**(2*32**(4*n+4)-1)]
                # [0..<32**(2**(20*n+21)-1)]
            regex"(Tz{n})(y[U-Za-z]{(1+5*n+5)-(n+1)})[U-Za-z]{len==第一层数}"
                # [0..<32**(1*32**(4*n+5)-1)]
                # [0..<32**(2**(20*n+25)-1)]
    => ...
]]
[[
又一个自然数编码:
词典序
字母表:94#ASCII.alnum+punct
    # [printable%95 == alnum%(10+26*2==62) | punctuation%32 | space%1]
    #   view ../../python3_src/seed/text/mk_char_pt_ranges5predicator.py
躯胞集:64==2**6
头胞集:30==94-64==16+8+4+2

[20902: [一-龥] ~ [4E00..9FA5]]
    [2**15==32769 > 20902]
    但发现 在 词典序 前提下 不能优先支持 基位面汉字区:
        !! [ord('龥')==40869>32769==2**15]
            #8000多
        !! [ord('一')==19968<32769==2**15]
            #12000多

偏好支持统合码{字节&基位面}:
    双胞码:4*64==2**8
    三胞码:16*64*64==2**16
    四胞码:4*64*64*64==2**20
    单胞码:4==2**2
    三层码{4}:2*64**?
偏好支持八进制数{字节&基位面}:
    单胞码:8==2**3
    双胞码:4*64==2**8
    三胞码:16*64*64==2**16
    三层码{3}:2*64**?
        或:跳过 四胞码:
            五胞码:1*64*64*64*64==2**24
            三层码{5}:1*64**?
偏好支持十六进制数{字节&xxx基位面汉字区}:
    单胞码:16==2**4
    双胞码:4*64==2**8
    三胞码:8*64*64==2**15
    三层码{3}:2*64**?
        或:跳过 四胞码:
            五胞码:1*64*64*64*64==2**24
            三层码{5}:1*64**?
偏好支持十进制数{字节&xxx基位面汉字区}:
    单胞码:10
    双胞码:4*64==2**8
    三胞码:8*64*64==2**15
    四胞码:6*64*64*64==2**20+2**19
    三层码{4}:2*64**?
<有限:局限于基位面>偏好支持十进制数{字节&基位面}:
    单胞码:10
    双胞码:4*64==2**8
    三胞码:16*64*64==2**16
    <完>

==>>:
细化:三层码{3|4|5}:(1|2)*64**?
三层码{偏移量纟解压值纟宏头胞}:2*64**?
宏头胞集:2==2**1 or 1==2**0
躯胞集:64==2**6
[偏移量纟解压值纟宏头胞 <- {3,4,5}]
    #非 偏移量纟存储值纟宏头胞/offset4macro_head_digit
]]
[[
动态爻元 vs 动态苞元:
    源起:『radix_digit的一个编码方案』从 动态苞元 改为 动态爻元
==>>:
动态爻元 vs 动态苞元:
动态爻元 vs 大步动态爻元 vs 动态苞元:
动态爻元 vs 大步动态爻元 vs 动态苞元 vs 殿后动态苞元:
#######
发现:编码方案{殿后动态苞元}还不错，缺点 可能就是 初始开销占比大
    => 编码方案{偏殿后动态苞元} 以改善 初始开销
    ++变体:融合 大步 => 编码方案{大步偏殿后动态苞元}
    ++变体:动态爻元  => 编码方案{大步固殿后动态爻元}
        ++变体:变长  => 编码方案{变步变殿后动态爻元}
see:IPlugin4InfiniteInterval
#######
前导长度的极限编码效率(由高至低):
    [L:=爻元数纟躯胞]
    [H:=爻元数纟前半躯胞][1<=H<=L]
    [E:=爻元数纟殿后爻元][E>=0] #允许[E>L]
    [step:=步长][step>=1]
    编码方案{变步变殿后动态爻元}
    编码方案{大步固殿后动态爻元}:
        (1-2**-E/(step*L))*L (单位:爻元/躯胞)
    编码方案{大步偏殿后动态苞元}:
        (1-2**-H/(step-(step-1)*2**-H))*L (单位:爻元/躯胞)
    编码方案{殿后动态苞元}
        (1-2**-L)*L (单位:爻元/躯胞)
    编码方案{偏殿后动态苞元}:
        (1-2**-H)*L (单位:爻元/躯胞)
    编码方案{大步动态爻元}:
        (1-1/(step*L))*L (单位:爻元/躯胞)
    编码方案{动态爻元}:
        (1-1/L)*L (单位:爻元/躯胞)
    编码方案{动态苞元}:
        (1-1/2)*L (单位:爻元/躯胞)
<<==:
#######
编码方案{动态爻元}:
    regex"【固定前缀】【最大躯胞】{n}(【躯胞:i动态爻元+k负载爻元】【躯胞】{(n*L+i)-(n+1)+C})【躯胞】{len==第一层数}"
    [L:=爻元数纟躯胞]
    [i+k==L][i>=0][k>0]
    重调次序:
    regex"【固定前缀】(【最大躯胞】{n}【躯胞:i动态爻元+k负载爻元】【躯胞】{n*(L-1)+i})【躯胞】{C-1}【躯胞】{len==第一层数}"
    重调次序，忽略前后缀:
    regex"(【最大躯胞】{n}【躯胞:i动态爻元+(L-i)负载爻元】【躯胞】{n*(L-1)+i})"
    重调次序，忽略前后缀，打散成爻元:
    regex"【动态爻元】{n*L+i}【负载爻元】{(n*(L-1)+i)*L+(L-i)}"
    regex"【动态爻元】{n*L+i}【负载爻元】{(n*L+i)*(L-1)+L}"
    重调次序，忽略前后缀，打散成爻元，再重调次序:
    regex"【动态爻元】{n*L+i}【负载爻元】{(n*L+i)*(L-1)}【负载爻元】{L}"
    regex"(【动态爻元】【负载爻元】{L-1}){n*L+i}【负载爻元】{L}"
    重调次序，忽略前后缀，打散成爻元，再重调次序，忽略后缀:
    regex"(【动态爻元】【负载爻元】{L-1}){n*L+i}"
    => 每L爻元 中 只有(L-1)个 爻元 提供 有效负载
    => 每L躯胞 中 只有(L-1)个 躯胞 提供 有效负载
#######
编码方案{大步动态爻元}:
    regex"【固定前缀】【最大躯胞】{n}(【躯胞:i动态爻元+k负载爻元】【躯胞】{step*(n*L+i)-(n+1)+C})【躯胞】{len==第一层数}"
    [L:=爻元数纟躯胞]
    [i+k==L][i>=0][k>0]
    [step:=步长][step>=1]
    => 每增加step*L爻元 中 只有(step*L-1)个 新增爻元 提供 有效负载
    => 每step*L躯胞 中 只有(step*L-1)个 躯胞 提供 有效负载
#######
编码方案{动态苞元}:
    regex"【固定前缀】【最大躯胞】{n}(【非最大躯胞】【躯胞】{n+C-1})【躯胞】{len==第一层数}"
    重调次序:
    regex"【固定前缀】(【最大躯胞】{n}【躯胞】{n})【非最大躯胞】【躯胞】{C-1}【躯胞】{len==第一层数}"
    重调次序，忽略前后缀:
    regex"(【最大躯胞】{n}【躯胞】{n})"
    重调次序，忽略前后缀，再重调次序，:
    regex"(【最大躯胞】【躯胞】){n}"
    => 每2躯胞 中 只有1个 躯胞 提供 有效负载
#######
编码方案{殿后动态苞元}:
    regex"【固定前缀】(【最大躯胞】{n}【非最大躯胞:值d】)(【躯胞】{(n*(R-1)+d)+C})【躯胞】{len==第一层数}"
    [R:=空间规模纟躯胞][R>=2]
    [0<=d<=R-2]
    重调次序:
    regex"【固定前缀】(【最大躯胞】{n}【非最大躯胞:值d】【躯胞】{(n*(R-1)+d)})【躯胞】{C}【躯胞】{len==第一层数}"
    重调次序，忽略前后缀:
    regex"(【最大躯胞】{n}【非最大躯胞:值d】【躯胞】{(n*(R-1)+d)})"
    => 每((n+1)+(n*(R-1)+d))躯胞 中 只有(n*(R-1)+d)个 躯胞 提供 有效负载
#######
编码方案{偏殿后动态苞元}:
    regex"【固定前缀】(【最大躯胞】{n}【非最大前半躯胞:值d+后半躯胞】)(【躯胞】{(n*(D-1)+d)+C-1})【躯胞】{len==第一层数}"
    [R:=空间规模纟躯胞]
    [D:=空间规模纟前半躯胞]
    [R>=D>=2][R%D==0]
    [0<=d<=D-2]
    重调次序:
    regex"【固定前缀】(【最大躯胞】{n}【非最大躯胞:值d】【躯胞】{(n*(D-1)+d)})【躯胞】{C-1}【躯胞】{len==第一层数}"
    重调次序，忽略前后缀:
    regex"(【最大躯胞】{n}【非最大躯胞:值d】【躯胞】{(n*(D-1)+d)})"
    => 每((n+1)+(n*(D-1)+d))躯胞 中 只有(n*(D-1)+d)个 躯胞 提供 有效负载
#######
编码方案{大步偏殿后动态苞元}:
    regex"【固定前缀】(【最大躯胞】{n}【非最大前半躯胞:值d+后半躯胞】)(【躯胞】{step*(n*(D-1)+d)+C-1})【躯胞】{len==第一层数}"
    [R:=空间规模纟躯胞]
    [D:=空间规模纟前半躯胞]
    [R>=D>=2][R%D==0]
    [0<=d<=D-2]
    [step:=步长][step>=1]
    重调次序:
    regex"【固定前缀】(【最大躯胞】{n}【非最大躯胞:值d】【躯胞】{step*(n*(D-1)+d)})【躯胞】{C-1}【躯胞】{len==第一层数}"
    重调次序，忽略前后缀:
    regex"(【最大躯胞】{n}【非最大躯胞:值d】【躯胞】{step*(n*(D-1)+d)})"
    => 每((n+1)+step*(n*(D-1)+d))躯胞 中 只有step*(n*(D-1)+d)个 躯胞 提供 有效负载
#######
编码方案{大步固殿后动态爻元}:
    regex"【固定前缀】【最大躯胞】{n}(【m个?躯胞:i动态爻元+E殿后爻元(值d)+k负载爻元】【躯胞】{step*((n*L+i)*2**E+d)-(n+m)+C})【躯胞】{len==第一层数}"
    [L:=爻元数纟躯胞]
    [E:=爻元数纟殿后爻元][E>=0] #允许[E>L]
    [0<=i<L]
    [m:=ceil_div(i+E+1,L)]
    [m <= ceil_div((L-1)+E+1,L) == 1+ceil_div(E,L)]
    [k:=m*L-(i+E)]
    [i+E+k==m*L][0<k<=L]
    [0<=d<2**E]
    [step:=步长][step>=1]
    => 每增加step*L*2**E爻元 中 只有(step*L*2**E-1)个 新增爻元 提供 有效负载
    => 每step*L*2**E躯胞 中 只有(step*L*2**E-1)个 躯胞 提供 有效负载
#######
编码方案{变步变殿后动态爻元}:
    regex"【固定前缀】【最大躯胞】{n}(【m_(n*L+i)个?躯胞:i动态爻元+E_(n*L+i)殿后爻元(值d)+k_(n*L+i)负载爻元】【躯胞】{step_(n*L+i)*(offset_(n*L+i)+d)-(n+m_(n*L+i))+C})【躯胞】{len==第一层数}"
    [L:=爻元数纟躯胞]
    # [w==数目纟动态爻元==(n*L+i)]
    [E_(w):=爻元数纟殿后爻元{w}][E_(w)>=0] #允许[E_(w)>L]
    [offset_(w):=sum{2**E_(y) | [y:<-[0..<w]]}]
    [0<=i<L]
    [m_(w):=let [i:=w%L] in ceil_div(i+E_(w)+1,L)]
    [m_(w) <= ceil_div((L-1)+E_(w)+1,L) == 1+ceil_div(E_(w),L)]
    [k_(w):=let [i:=w%L] in m_(w)*L-(i+E_(w))]
        let [i:=w%L] in [i+E_(w)+k_(w)==m_(w)*L][0<k_(w)<=L]
    [0<=d<2**E_(w)]
    [step_(w):=步长][step_(w)>=1]
    => ...???
#######
==>>:
    [前导长度的极限编码效率{动态爻元} == (爻元数纟躯胞-1) (单位:爻元/躯胞)]
        # == L (爻元/躯胞) *(L-1)胞 /(L胞)
        # == L (爻元/躯胞) *(1-1/L)
    [前导长度的极限编码效率{大步动态爻元} == (爻元数纟躯胞-1/步长) (单位:爻元/躯胞)]
        # == L (爻元/躯胞) *(step*L-1)胞 /(step*L胞)
        # == L (爻元/躯胞) *(1-1/(step*L))
    [前导长度的极限编码效率{动态苞元} == (爻元数纟躯胞/2) (单位:爻元/躯胞)]
    [前导长度的极限编码效率{殿后动态苞元} == (爻元数纟躯胞*(1-2**-爻元数纟躯胞)) (单位:爻元/躯胞)]
        # == limit{(L (爻元/躯胞) *(n*(R-1)+d)胞 /(((n+1)+(n*(R-1)+d))胞)) | n-->+oo}
        # == L(爻元/躯胞) / (1/(R-1) +1)
        # == L(爻元/躯胞) *(R-1)/R
        # == L(爻元/躯胞) *(1-1/R)
        # == L(爻元/躯胞) *(1-2**-L)
    [前导长度的极限编码效率{偏殿后动态苞元} == (爻元数纟躯胞*(1-2**-爻元数纟前半躯胞)) (单位:爻元/躯胞)]
        # == limit{(L (爻元/躯胞) *(n*(D-1)+d)胞 /(((n+1)+(n*(D-1)+d))胞)) | n-->+oo}
        # == L(爻元/躯胞) / (1/(D-1) +1)
        # == L(爻元/躯胞) *(D-1)/D
        # == L(爻元/躯胞) *(1-1/D)
        # :> [H:=爻元数纟前半躯胞]
        # == L(爻元/躯胞) *(1-2**-H)
    [前导长度的极限编码效率{大步偏殿后动态苞元} == (爻元数纟躯胞*(1-2**-爻元数纟前半躯胞/(步长-(步长-1)*2**-爻元数纟前半躯胞))) (单位:爻元/躯胞)]
        # == limit{(L (爻元/躯胞) *step*(n*(D-1)+d)胞 /(((n+1)+step*(n*(D-1)+d))胞)) | n-->+oo}
        # == L(爻元/躯胞) / (1/(step*(D-1)) +1)
        # == L(爻元/躯胞) *(1-1/(1+step*(D-1)))
        # == L(爻元/躯胞) *(1-1/(step*D-(step-1)))
        # :> [H:=爻元数纟前半躯胞]
        # == L(爻元/躯胞) *(1-1/(step*2**H-(step-1)))
        # == L(爻元/躯胞) *(1-2**-H/(step-(step-1)*2**-H))
    [前导长度的极限编码效率{大步固殿后动态爻元} == (爻元数纟躯胞*(1-2**-爻元数纟殿后爻元/(步长*爻元数纟躯胞))) (单位:爻元/躯胞)]
        # == limit{(L (爻元/躯胞) *(step*((n*L+i)*2**E+d)-(n+m-k/L)+C)胞 /(step*((n*L+i)*2**E+d)胞)) | n-->+oo}
        # == L(爻元/躯胞) *(step*L*2**E-1)/(step*L*2**E)
        # == L(爻元/躯胞) *(1-1/(step*L*2**E))
        # == L(爻元/躯胞) *(1-2**-E/(step*L))
==>>:
    [前导长度的极限编码效率{动态爻元} == 前导长度的极限编码效率{大步动态爻元}{步长==1}]
    [前导长度的极限编码效率{动态苞元}{胞元==爻元} == 前导长度的极限编码效率{大步动态爻元}{步长==2}{胞元==爻元}]
    [前导长度的极限编码效率{动态苞元}{胞元==爻元} == 前导长度的极限编码效率{殿后动态苞元}{胞元==爻元}]
    [前导长度的极限编码效率{偏殿后动态苞元}{爻元数纟前半躯胞==爻元数纟躯胞} == 前导长度的极限编码效率{殿后动态苞元}]
    [前导长度的极限编码效率{大步偏殿后动态苞元}{步长==1} == 前导长度的极限编码效率{偏殿后动态苞元}]
    [前导长度的极限编码效率{大步动态爻元} == 前导长度的极限编码效率{大步固殿后动态爻元}{爻元数纟殿后爻元==0}]
==>>:
[前导长度的极限编码效率{动态爻元} < 前导长度的极限编码效率{动态苞元}]
    <==> [(爻元数纟躯胞-1) < (爻元数纟躯胞/2)]
    <==> [爻元数纟躯胞 < 2]
    <==> [爻元数纟躯胞 == 1]
==>>:
[前导长度的极限编码效率{大步动态爻元} == 前导长度的极限编码效率{殿后动态苞元}]
    <==> [(爻元数纟躯胞-1/步长) == (爻元数纟躯胞*(1-2**-爻元数纟躯胞))]
    <==> [(L-1/步长) == (L*(1-2**-L))]
    <==> [L/(2**L) == 1/步长]
    <==> [步长 == (2**L)/L]
    <==> [b:=log2(L)][L == 2**b][步长 == 2**(L-b)]
    <==> [(爻元数纟躯胞,步长) <- {(1,2), (2,2), (4,4), (8,32), (16,2**12), (32,2**27), ... ...}]
]]
[[
copy from: e ../../python3_src/seed/int_tools/digits/codecs4int.py
copy to:e ../lots/NOTE/abbr/software.txt
copy to:e others/数学/编程/设计/自定义字符编码.txt
===
@20250721
源起:命名有点乱:歧义:
    胞<字<码#cell<word<code
    爻<胞<码#bit<cell<code
重新命名:
    ######################
    具象物理组构体系:(基粒==)孢<(字==符==)荚<码<包#spore<pod<code<packet
    #######
    [包=[def]=编码方案{整数序列}.码元]
    [码=[def]=编码方案{整数}.码元]
    [荚=[def]=具象物理单元/(存储单元|传输单元|编码方案.字母表)]
    [孢=[def]=最小的幂根{荚}]
        #from seed.math.factor_pint_as_pefect_power_ import factor_pint_as_pefect_power_
    #######
    [包==码串::[码]]
    [码.具象物理组构==荚串::[荚]]
    [荚==孢串::[孢]]
    [孢::uint%radix]
        # eg:[孢:=爻元]
        where:
            [not is_perfect_power(radix)]
    ######################
    抽象逻辑组构体系:(胞|宏胞)==苞<码<包#(cell|macro_cell)==bud<code<packet
    #######
    [苞=[def]=(胞|宏胞)]
    [胞=[def]=有效负载空间{荚{某类码元中某个位置}}]
      # eg:将 编码方案.字母表 分为4个不相交的子集:孤符集,头符集,体符集,尾符集
      #     =>2类码元4类胞元:{孤胞码{孤胞},多胞码{头胞+体胞*+尾胞}}
      #     =>不同类的胞元 对应不同的 字母表，有效负载空间也不必相同。
    [宏胞=[def]=有效负载空间{荚串{某类码元中某些位置}}]
      # 人为边界: 将 某些胞 人为组合起来 统一分配/编码
    #######
    [包==码串::[码]]
    [码.抽象逻辑组构==苞串::[苞]]
    ######################
<<==:
#这一部分已删除，可见于: view ../lots/NOTE/abbr/software.txt
]]

重命名:
    尾胞-->躯胞
    尾部-->躯部
    :%s/尾/躯/g
        除了上面:『尾符集...2类码元4类胞元:...尾胞』

重命名:
    以匹配layer0#从零开始
    第一层-->第零层
    第二层-->第一层
    第三层-->第二层
    或许:甲层，乙层，丙层



[[
TODO
[:doc4IPlugin4InfiniteInterval]:here
    move from:IPlugin4InfiniteInterval.__doc__

######################
汇集处纟约束牜非平凡:
    [:约束牜紧凑乊首层]:goto
######################
主打方案:编码方案{变步变殿后动态爻元}
######################
[首层==第零层==layer0==(dynamic_part{len_dynamic_bits}++follower_part{len_dynamic_bits})]
    [len_dynamic_bits :: uint{>=0}]
    [dynamic_part == regex"1*0"/bits]
    [dynamic_part{len_dynamic_bits} == regex"1{len_dynamic_bits}0"/bits]
    [(dynamic_part,follower_part) ~ (序号纟分段,编码空间纟分段)]
        #采用 分段累积法{len_dynamic_bits==序号纟分段}
每一层 都存储一个 自然数:
    分2种形式:
        *[压缩值==物理存储值]
            [压缩值 是 稠密分布的]
                #eg:第零层:采用 分段累积法{len_dynamic_bits}
            [let [len_dynamic_bits:=classify_compressed_uint6layer0(压缩值{第零层})] in [(len_dynamic_bits+1+num_bits4follower4dynamic_part{len_dynamic_bits}+解压值{第零层})%num_bits4cell6body==0]]
                # [:约束牜紧凑乊首层]:here
                # 即 (dynamic_part++follower_part++payload_bit_block)凑成整躯胞串
        *[解压值==逻辑实用值]
            [解压值 可能是 稀疏分布的]
                #有损压缩:偏移+二分搜索/跃迁
            [解压值{末层} 是 稠密分布的]
                #无损压缩:只能偏移
            #记录 目标自然数
            [解压值{末层}==值纟整编码]
            #记录 第一层 爻元数
            [解压值{第零层}
                >=第一层.压缩值.数目纟爻元
                ==第一层.压缩值.bit_length()
            ]
            #记录 第二层诸后 躯胞数
            #   或许 应该 统一为 爻元数
            [解压值{非末层&&非第零层}
                >=下一层.压缩值.数目纟躯胞
                ==1+floor_log_(2**爻元数纟躯胞;下一层.压缩值)
                ==ceil_log_(2**爻元数纟躯胞;1+下一层.压缩值)
                ==ceil_div_(爻元数纟躯胞;ceil_log2_(1+下一层.压缩值))
                ==ceil_div_(爻元数纟躯胞;下一层.压缩值.bit_length())
            ]
######################

]]
[[
TODO
独力单层编解码器
单层编码器
单层解码器
    只能处理一层:动态爻元、动态苞元、定长爻元串、定长躯胞串

#######
单层解码器{爻元串}:动态爻元,定长爻元串
    内禀属性:(爻元数纟躯胞,最大值纟躯胞)
    输入:(爻元数纟宏头胞,?最大值纟宏头胞?;值纟宏头胞,读者牜躯胞;??定长爻元数纟消耗??)
    输出:(值纟读出;爻元数纟消耗;爻元数纟宏头胞{剩余},?最大值纟宏头胞{剩余}?;值纟宏头胞{剩余},读者牜躯胞{剩余})
        #宏头胞{剩余} 来自于 低爻位{原输入宏头胞|最后读出的躯胞}
#######
单层解码器{苞元串}:动态苞元,定长躯胞串
    内禀属性:(爻元数纟躯胞,最大值纟躯胞)
    输入:(?已读出首躯胞?,读者牜躯胞;??定长躯胞数纟消耗??)
    输出:(值纟读出;躯胞数纟消耗;?已读出首躯胞{剩余}?,读者牜躯胞{剩余})
#######
#######
单层编码器{爻元串}:动态爻元,定长爻元串
    内禀属性:(爻元数纟躯胞,最大值纟躯胞)
    [0 <= 爻元数纟追附 < 爻元数纟躯胞]
    输入:(值纟编入,爻元数纟追附,值纟追附;??定长爻元数纟输出??)
    输出:(爻元数纟追附{剩余},值纟追附{剩余},躯胞串纟输出;??爻元数纟输出??)
        编码=>逆向迭代输出 躯胞串
#######
单层编码器{苞元串}:动态苞元,定长躯胞串
    内禀属性:(爻元数纟躯胞,最大值纟躯胞)
    输入:(值纟编入;??定长躯胞数纟输出??)
    输出:(躯胞串纟输出;??躯胞数纟输出??)
#######
]]
[[
插件:
    *有限区
        *有限区牜有限层
    *无限区
        *无限区牜有限层
            首层:动态爻元++变长殿后爻元 冃 次层爻元数
        *无限区牜无限层
            首层:动态爻元++变长殿后爻元 冃 层数&次层爻元数

TODO:新增:无限区牜无限层
!! 三层码 起初可能对头部空间的紧凑性有较高要求，但编码长度极大之后就不那么高要求了，此时可考虑升级换代(变态)
!! 首层:动态爻元++变长殿后爻元 冃 层数&次层爻元数
=>: threshold4inf_layers
    [[解压值{首层} < threshold4inf_layers] -> [[层数{次层诸后}==2][次层爻元数==解压扌(凡层数:=3,序号纟凡层:=凡零层;三凡层之首层.压缩值:=解压值{首层})]]]
        #首层/超层/混零层/凡零层,次层/混一层/凡一层,末层/混二层/凡二层
        #注意:此况态下[混k层==凡k层]
        #注意:『解压扌(凡层数:=3,序号纟凡层:=凡零层;三凡层之首层.压缩值:=...)』在下面况态中也可能会出现，但那时 凡零层 指的却是 次层
    [[解压值{首层} >= threshold4inf_layers] -> [[层数{次层诸后}==3+解压值{首层}-threshold4inf_layers][次层爻元数==爻元数纟躯胞-首层爻元数%爻元数纟躯胞 <- [1..=爻元数纟躯胞]]]]
        #首层/混零层/超层,次层/混一层/凡零层,...
        #注意:此况态下[混(k+1)层==凡k层]
        外大区平滑特性=>取消压缩，统一单位:躯胞
        => [次层爻元数==1]是有意义的，直接不断编码长度直至[01]，没有任何步骤是浪费的！
外大区平滑特性:
    内三层使用压缩:超层等价于不存在时，凡层数不多于三层，此时称为『内三层』
    外大区取消压缩:超层存在，凡层数不少于三层
        超层存在，凡层数等于三层，此时称为『外三层』
        不仅取消压缩，还统一单位:躯胞
    注意:超层 可以 任意复杂(采用:低效率自然数编码方案)，至少可能是(动态爻元+变长殿后爻元)



负一层==末层
无限区牜无限层:编码:反向处理各层:负一层,负二层,...

[[k>=2] -> [解压值{-k} == 压缩值{-k+1}.bit_length()]]
处理 第-k层:解压值{-k} --> 压缩值{-k}
    if [压缩值{-k} <= 最大值纟次层{总层数==k+1}]:
        ...结束
    else:
        [解压值{-k-1} := 压缩值{-k}.bit_length()]
        递归 处理 第-k-1层:解压值{-k-1}
]]
[[
TODO:
@20250723
二幂情形=>统一使用 爻元数 而非 避免混合使用 躯胞数
    #注意:宏头胞 未必是 二幂
并 标明 爻元串边界必须对齐躯胞欤
==>>:
二幂情形=>统一使用 串长带自定义单位
[自定义单位 =[def]= (步长,内置单位)]
[内置单位 =[def]= (爻元|躯胞)]

]]
[[
===
流程:
流程牜二幂情形:
    三种主模态:单凡层(立即数)、多凡层、超凡层
===
常量:
    最小值纟多凡层
    最小爻元数纟值纟超凡层

    最大值纟宏头胞
    最小值纟宏头胞纟多凡层
        # [首辨苞{多凡层vs单凡层}==宏头胞]
    序号纟首辨苞纟超凡层
    最小值纟首辨苞纟超凡层
        # [首辨苞{多凡层vs超凡层} :: (宏头胞|躯胞)]
    最大值纟躯胞
===
解码流程:
    输入:值纟宏头胞,读者牜躯胞
    if not 值纟宏头胞 <= 最大值纟宏头胞:raise OverflowError
    if 值纟宏头胞 < 最小值纟宏头胞纟多凡层:
        return ...自定义插件{立即数}
    if 0==序号纟首辨苞纟超凡层:
        if 值纟宏头胞 < 最小值纟首辨苞纟超凡层:
            return ...挑选-自定义插件{多凡层}
        else:
            return ...唯一内置插件{超凡层}
    elif not 值纟宏头胞 == 最大值纟宏头胞:
        return ...挑选-自定义插件{多凡层}
    else:
        maxs = 读者牜躯胞.read_le_while(序号纟首辨苞纟超凡层-1, 最大值纟躯胞.__eq__)
        if not len(maxs) == 序号纟首辨苞纟超凡层-1:
            return ...挑选-自定义插件{多凡层}{maxs++读者牜躯胞}
        else:
            值纟首辨苞纟超凡层 = 读者牜躯胞.read1()
            if 值纟首辨苞纟超凡层 < 最小值纟首辨苞纟超凡层
                return ...挑选-自定义插件{多凡层}{maxs++[值纟首辨苞纟超凡层]++读者牜躯胞}
            else:
                return ...唯一内置插件{超凡层}{maxs++[值纟首辨苞纟超凡层]++读者牜躯胞}
    raise 000
===
编码流程:
    输入:值纟编入
    if 值纟编入 < 最小值纟多凡层:
        #有限区:单凡层#特点:手写编码，简单快速
        return ...自定义插件{立即数}
    爻元数纟输入:=值纟编入.bit_length()
    if 爻元数纟输入 >= 最小爻元数纟值纟超凡层:
        #无限区:超凡层#特点:内置插件{极简配置}
        return ...唯一内置插件{超凡层}
    #有限区:多凡层#特点:插件多，压缩配置复杂
    return ...挑选-自定义插件{多凡层}
===
]]
[[
独力单层编解码器:
e ../../python3_src/seed/int_tools/StepDecoder.py
]]
[[
@20250726
微调:增加 保留区，导致 超凡层.超层 不是 第零层，而是 推至 第一层
<<==:
编解码:动态爻元分配:
    +非动态爻元前缀的编码区
    +动态爻元前缀的编码区:
        +动态爻元前缀:
            数纟动态爻元前缀->编解码器
            结尾是 超凡层:[数纟动态爻元前缀==动态爻元截止长度-1] => (偏移量纟层数{<=之前最大层数},第一层是动态爻元{->非固定层数}{躯胞数纟第二层==1躯胞}{各层都是整躯胞}{统一单位:躯胞}{统一不作线性变换})
            非结尾则通常是: (固定层数,爻元数纟第一层,各层线性变换牜不含末层{统一单位:爻元数}，k{第几层起整躯胞，但第k层首躯胞必不完整{允空不允整}},末层相关/((偏移量|...{延续之前最大可编码值}),最大爻元数纟末层{偏移之后}))
            注意:多凡层:负二层 的 负载应当不超出 64bit #否则 负一层 即 被编码的自然数的爻元数 至少是 2**64 完全没有必要 出现在 多凡层，应当 推至 超凡层
    +保留区:动态爻元截止长度

==>>:
透明数据化编解码器{自然数}{解码器{侧重头苞分类{并联}{LL1}}}:
    [数据模型==(基数纟宏头胞,基数纟躯胞)]
    +有限区编解码器:
        [有限区编解码器{基数纟头苞}==([基数纟头苞==1]:有限区编解码器深入型|有限区编解码器基础型{基数纟头苞})]
        [有限区编解码器深入型{基数纟头苞:=1}==深入型{有限区编解码器{基数纟头苞:=基数纟躯胞}}]
            #see:IStepDecoder__skip_macro_header
            # 深入型-前置条件:[所占用编码空间纟头苞:=1]
        [有限区编解码器基础型{基数纟头苞}==基础型{[(占地纟头苞,第零层规模,各层线性变换,整躯胞终末的起始层号,隐藏:囿 带单位值{末层压缩值上尾限})]}]
            #see:IStepDecoder__fixed_size_layers
            #see:IStepDecoder__parallel__partition_space4macro_header
            [囿==惰性数据]
            [带单位值{值名}(无单位值,单位/立即数丷爻元数丷躯胞数)]
            #xxx:[占地纟头苞==(所占用编码空间纟头苞,立即数丷爻元数,欤累计偏移量)]
                # 无用:欤累计偏移量
            [占地纟头苞==(所占用编码空间纟头苞,立即数丷爻元数)]
            [第零层规模==(长度纟第零层,躯胞数丷爻元数,欤头苞另计,头苞偏移量)]
                #多凡层:因为 没有 超层，所以 第零层 是 第零凡层
                # 头苞偏移量:比如:+1则有:([0-8][0-9]*) --> ([1-9][0-9]*)
            [各层线性变换==(非末层层号讠线性变换,末层偏移量)]
                #末层偏移量or累积接力居前末层最大值
                #统统硬编码
            整躯胞终末的起始层号:只用作检查
    +无限区编解码器:
        #see:IStepDecoder__truncated_dynamic_bits_with_may_dynamic_bibits
        [无限区编解码器{基数纟头苞}==([基数纟头苞==1]:无限区编解码器深入型|无限区编解码器基础型{基数纟头苞})]
        [无限区编解码器深入型{基数纟头苞:=1}==深入型{无限区编解码器{基数纟头苞:=基数纟躯胞}}]
        [无限区编解码器基础型==基础型{(占地爻元数纟头苞,超层偏移量,动态爻元截止长度)}]
            #有任何不规则需求,统统归入 有限区
            #超层 是 第零层 是 动态爻元(其间插入保留区)
            #爻元数纟第一层 为 不完整的 头苞，0bit 自动偏移+1 {相当于 (总)凡层数-1，并且 第一层 占 1躯胞}
            #动态爻元截止长度:见下面:无限保留区方案
    +不存在:保留区编解码器:
        见上面:无限区编解码器基础型.
==>>:
透明数据化编解码器{自然数}{编码器}:
    [数据模型==(基数纟宏头胞,基数纟躯胞)]
    缓存化:自然数-->缓存化自然数
        [缓存化自然数(自然数冃末层解压值) =[def]= (自然数冃末层解压值,囿 爻元数,囿 躯胞数, 槑 {末层偏移量{>0}:缓存化自然数(末层压缩值:=自然数冃末层解压值-末层偏移量)})]
    编码器外观:(基数纟头苞,欤可编码巛缓存化自然数扌)
    基础型编码器外观参数:(基数纟头苞,末层偏移量,鬽 带单位值{末层压缩值上尾限})
    并联型编码器:[基础型编码器]
]]
[[
@20250728
无限保留区方案:编码方案{超凡层插入无限个保留区}:
#######
超层动态爻元分配:
    超凡层:regex"(01){n}00{多凡层{n}}"
        结束串:00
    保留区:regex"(01){n}1{保留区{n}}"
        结束串:11
    注意:支持词典序:[00{占用} < 01{继续} < 1b{保留}] => [保留区 永远大于 已编码的自然数]
#######
采用参数:动态爻元截止长度
    #see:IStepDecoder__dynamic_bits.max_num_bits4read
    超凡层:regex"1{0<=n<=动态爻元截止长度-2}0{多凡层{n}}|1{动态爻元截止长度-1}(01){n}00{多凡层{动态爻元截止长度-1+n}}"
        结束串:00
    保留区:regex"1{动态爻元截止长度-1}(01){n}1{保留区{n}}"
        结束串:11
分2步读取:
    + IStepDecoder__dynamic_bits
    + IStepDecoder__dynamic_bibits
    [u := 使用:IStepDecoder__dynamic_bits{max_num_bits4read:=动态爻元截止长度}]
    if u == 动态爻元截止长度:
        return (True, 0) # 保留区0
    if u < 动态爻元截止长度-1:
        return (False, offset4super_layer+u) # 凡层数
    if u == 动态爻元截止长度-1:
        # 已读出前缀: regex"1{动态爻元截止长度}0"
        # !! 之前 "0" 结尾，所以 下面是 "(10)*" 而非 "(01)*"
        # 之后:regex"(10)*(0|11)"
        # 之后:regex"(10){v}(0|11)"
        [(_0_vs_11, v) := 使用:IStepDecoder__dynamic_bibits{body_bibit:="10"}]
        if _0_vs_11:
            # ...11
            return (True, 1+v) # 保留区(1+v)
        else:
            return (False, offset4super_layer+u+v) # 凡层数
    raise 000
#######
e others/数学/编程/设计/自定义编码之要点.txt
]]
[[
move to:
view others/数学/编程/设计/自定义字符编码-兼容utf8.txt
===
@20250726
要是 支持词典序、同时重点优化:ASCII+统合码基位面+统合码 的 编码空间，则兼容utf8是个不错的起点
    由于utf8编码效率低，只有5/8，所以后续必须改变编码方案，以逼近极限效率6/8
    最优:{候选方案辛,候选方案壬{偏好},候选方案癸} <<==:
... ...
]]






py_adhoc_call   seed.int_tools.digits.codecs4int   @f
from seed.int_tools.digits.codecs4int import *
]]]'''#'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from itertools import islice
from seed.tiny_.check import check_type_is, check_int_ge

from seed.abc.abc__ver1 import abstractmethod, override, ABC
from seed.helper.repr_input import repr_helper

___end_mark_of_excluded_global_names__0___ = ...

#.class IPlugin(ABC):
#.    __slots__ = ()
#.    @property
#.    @abstractmethod
#.    def used_num_words6immediate(sf, /):
#.        '-> uint{>0}'
#.    @property
#.    @abstractmethod
#.    def offset4stored_uint(sf, /):
#.        '-> uint'
#.    @abstractmethod
#.    def uint2cells_ex_(sf, u, num_bits4u, /):
#.        'offsetted_stored_uint/u/uint -> num_bits4u/uint -> (icase/uint%used_num_words6immediate, num_cells/uint, Iter cell) # [num_bits4u == u.bit_length()]'
#.    @abstractmethod
#.    def uint5cells_ex_(sf, icase, cells, /):
#.        'icase/uint%used_num_words6immediate -> Iter cell -> (num_cells/uint, offsetted_stored_uint/u/uint)'
#.class IPlugin4FiniteInterval(IPlugin):
#.    __slots__ = ()
#.    @property
#.    @abstractmethod
#.    def either_max_unoffsetted_stored_uint_or_its_num_bits(sf, /):
#.        '-> (bool, uint)/((False, max_unoffsetted_stored_uint{may be non-2-power})|(True, max_num_bits4unoffsetted_stored_uint{max_unoffsetted_stored_uint==2**max_num_bits4unoffsetted_stored_uint-1}))'
#.    assert (0).bit_length() == 0
#.    def is_uint_in_range_(sf, u, num_bits4u, /):
#.        'offsetted_stored_uint/u/uint -> num_bits4u/uint -> bool # [num_bits4u == u.bit_length()]'
#.        # # [num_bits4u == 0 if u==0 else u.bit_length()]
#.        assert u >= 0
#.        (is_num_bits, x) = sf.either_max_unoffsetted_stored_uint_or_its_num_bits
#.        offset = sf.offset4stored_uint
#.        v = u -offset
#.            # u == offsetted_stored_uint
#.            # v == unoffsetted_stored_uint
#.
#.        if v < 0:
#.            return False
#.        if not is_num_bits:
#.            max_unoffsetted_stored_uint = x
#.            return v <= max_unoffsetted_stored_uint
#.        max_num_bits4unoffsetted_stored_uint = x
#.
#.        if offset == 0:
#.            num_bits4v = num_bits4u
#.        else:
#.            num_bits4v = v.bit_length()
#.        num_bits4v
#.        return num_bits4v <= max_num_bits4unoffsetted_stored_uint
#.
#.
#.class IPlugin4InfiniteInterval(IPlugin):
#.    __slots__ = ()
#.    @property
#.    @abstractmethod
#.    def min_num_layers(sf, /):
#.        '-> uint'
#.    @property
#.    @abstractmethod
#.    def whether_supported_infinite_reserved_space(sf, /):
#.        '-> bool'
#.
#.class ICodec4SInt__zpow_based__lexicographic_order_reserved(ABC):
#.    'si'
#.class ICodec4UInt__zpow_based__lexicographic_order_reserved(ABC):
#.    'ui'
#.    __slots__ = ()
#.    @property
#.    @abstractmethod
#.    def num_words6macro_header(sf, /):
#.        '-> uint'
#.    @property
#.    @abstractmethod
#.    def num_bits4cell6body(sf, /):
#.        '-> uint'
#.    @property
#.    @abstractmethod
#.    def seq4plugin4finite_interval(sf, /):
#.        '-> [IPlugin4FiniteInterval]'
#.    @property
#.    @abstractmethod
#.    def plugin4infinite_interval(sf, /):
#.        '-> IPlugin4InfiniteInterval'
#.
#.    def encode4uint_ex_(sf, u, /):
#.        'offsetted_stored_uint/u/uint -> (num_cells/uint, (Iter cell){nonempty})'
#.        check_int_ge(0, u)
#.        num_bits4u == u.bit_length()
#.        offset4icase = 0
#.        for plgn in sf.seq4plugin4finite_interval:
#.            if plgn.is_uint_in_range_(u, num_bits4u):
#.                break
#.            offset4icase += plgn.used_num_words6immediate
#.        else:
#.            plgn = sf.plugin4infinite_interval
#.        offset4icase, plgn
#.        (icase, _num_cells, _cells) = plgn.uint2cells_ex_(u, num_bits4u)
#.        head = offset4icase + icase
#.        return (1+_num_cells, chain([head], _cells))
#.    def dencode4uint_ex_(sf, cells, /):
#.        '(Iter cell){nonempty} -> (num_cells/uint, offsetted_stored_uint/u/uint)'
#.        cells = iter(cells)
#.        for head in cells:
#.            _cells = cells; del cells
#.            break
#.        else:
#.            raise ValueError('null iter')
#.        head, _cells
#.        check_int_ge(0, head)
#.
#.        offset4icase = 0
#.        for plgn in sf.seq4plugin4finite_interval:
#.            _offset4icase = offset4icase + plgn.used_num_words6immediate
#.            if head < _offset4icase:
#.                break
#.        else:
#.            plgn = sf.plugin4infinite_interval
#.            _offset4icase = offset4icase + plgn.used_num_words6immediate
#.            if not head < _offset4icase:
#.                raise ValueError('head cell too big')
#.        offset4icase, plgn
#.        icase = head -offset4icase
#.        (_num_cells, offsetted_stored_uint) = plgn.uint5cells_ex_(icase, _cells)
#.        return (1+_num_cells, offsetted_stored_uint)
#.
#.#num_words4cell6head
#.#num_words4cell6body
#.num_words6macro_header#num_words6macro_cell8logical_header
#.num_bits4cell6body
#.#finite_plugin:
#.(used_num_words6immediate, offset4stored_uint, nbits_vs_uint, (max_num_bits4unoffsetted_stored_uint|max_unoffsetted_stored_uint))
#.  #非 0层-立即数 => (num_storage_bits6immediate爻+)首层{min_..=max_}num_body_cells4fst_layer体符
#.  #######
#.  * (num_layers6append, multiplicity, num_storage_bits6immediate, num_body_cells4fst_layer, offset4stored_uint)
#.      [used_num_words6immediate := multiplicity*2**num_storage_bits6immediate]
#.      [max_unoffsetted_stored_uint := multiplicity*(iterate (\len -> 2**len-1) (2**(num_storage_bits6immediate+num_bits4cell6body*num_body_cells4fst_layer)-1) !! num_layers6append)]
#.  #######
#.  * (num_layers6append, num_storage_bits6immediate, min_num_body_cells4fst_layer, max_num_body_cells4fst_layer, offset4stored_uint)
#.      [used_num_words6immediate := (max_num_body_cells4fst_layer+1-min_num_body_cells4fst_layer)*2**num_storage_bits6immediate]
#.      [max_num_bits4unoffsetted_stored_uint := if num_layers6append == 0 then num_storage_bits6immediate else iterate (\num_bits4len -> 2**num_bits4len-1) (num_storage_bits6immediate+num_bits4cell6body*max_num_body_cells4fst_layer) !! (num_layers6append-1)]
#.  #######
#.###super_dybl_layers
#.#infinite_plugin:
#.(min_num_layers, whether_supported_infinite_reserved_space)
#.
#.
#.
#.
#.
#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError
#.

from seed.iters.chains import chains
class IDigitReader(ABC):
    'digit_reader'
    '词典序 => read_eq() instead of read_le()'
    __slots__ = ()
    @property
    @abstractmethod
    def eof(sf, /):
        '-> bool'
    @abstractmethod
    def tell(sf, /):
        '-> position/uint'
    @abstractmethod
    def read1(sf, /, *, peek=False):
        '-> uint|^EOFError'
    @abstractmethod
    def read_eq(sf, sz, /, *, peek=False):
        'uint -> tuple<uint>{len==sz}|^EOFError'
    @abstractmethod
    def read_while(sf, pred, /, *, peek=False):
        '(uint->bool) -> tuple<uint>'
    @abstractmethod
    def drop_eq(sf, sz, /):
        'uint -> None|^EOFError'

    def peek1(sf, /):
        '-> uint|^EOFError'
        return sf.read1(peek=True)
    def peek_eq(sf, sz, /):
        'uint -> tuple<uint>{len==sz}|^EOFError'
        return sf.read_eq(sz, peek=True)
    def peek_while(sf, pred, /):
        '(uint->bool) -> tuple<uint>'
        return sf.read_while(pred, peek=True)
#end-class IDigitReader(ABC):

from seed.seq_tools.mk_seq_rng import mk_seq_rng, mk_seq_rng__len
class DigitReader5seq(IDigitReader):
    ___no_slots_ok___ = True
    def __init__(sf, digit_seq, begin=None, end=None, /):
        (begin, end) = mk_seq_rng(digit_seq, begin, end)
        #sf._args = (digit_seq, begin, end)
        #(digit_seq, begin, end) = sf._args
        #sf._2 = (digit_seq, end)
        sf._0 = digit_seq
        sf._1 = begin
        sf._2 = end
        #sf._sz = end -begin
    @property
    @override
    def eof(sf, /):
        '-> bool'
        #return sf._sz == 0
        return sf._1 == sf._2
    @override
    def tell(sf, /):
        '-> position/uint'
        return sf._1
    @override
    def read1(sf, /, *, peek=False):
        '-> uint|^EOFError'
        if sf.eof:raise EOFError
        ls = sf._0
        i = sf._1
        u = ls[i]
        if not peek:sf._1 = i+1
        return u
    @override
    def read_eq(sf, sz, /, *, peek=False):
        'uint -> tuple<uint>{len==sz}|^EOFError'
        check_int_ge(0, sz)
        if not sz:return ()
        ls = sf._0
        i = sf._1
        k = sf._2

        j = i+sz
        if not j <= k:raise EOFError
        us = ls[i:j]
        if not peek:sf._1 = j
        return us
    @override
    def read_while(sf, pred, /, *, peek=False):
        '(uint->bool) -> tuple<uint>'
        ls = sf._0
        i = sf._1
        k = sf._2
        for j in range(i, k):
            u = ls[j]
            if not pred(u):
                break
        else:
            j = k
        us = ls[i:j]
        if not peek:sf._1 = j
        return us
    @override
    def drop_eq(sf, sz, /):
        'uint -> None|^EOFError'
        check_int_ge(0, sz)
        if not sz:return
        ls = sf._0
        i = sf._1
        k = sf._2
        j = i+sz
        if not j <= k:raise EOFError
        sf._1 = j
        return



from seed.iters.PeekableIterator import PeekableIterator, echo_or_mk_PeekableIterator
class DigitReader5iter(IDigitReader):
    ___no_slots_ok___ = True
    def __init__(sf, digits, offset, /):
        check_int_ge(0, offset)
        sf._it = echo_or_mk_PeekableIterator(digits)
        sf._i = offset
    @property
    @override
    def eof(sf, /):
        '-> bool'
        return sf._it.is_empty()
    @override
    def tell(sf, /):
        '-> position/uint'
        return sf._i
    @override
    def read1(sf, /, *, peek=False):
        '-> uint|^EOFError'
        [u] = sf.read_eq(1, peek=peek)
        return u
    @override
    def read_eq(sf, sz, /, *, peek=False):
        'uint -> tuple<uint>{len==sz}|^EOFError'
        check_int_ge(0, sz)
        if not sz:return ()
        peek = bool(peek)
        it = sf._it
        if not it.len_ge(sz):raise EOFError
        if peek:
            us = it.peek_le(sz)
        else:
            us = it.read_le(sz)
            sf._i += sz
        us
        assert len(us) == sz
        return us
    @override
    def read_while(sf, pred, /, *, peek=False):
        '(uint->bool) -> tuple<uint>'
        it = sf._it
        us = tuple(takewhile(pred, it.tmp_peek_iter()))
        sz = len(us)
        if (not peek) and sz:
            it.drop_le(sz)
            sf._i += sz
        return us
    @override
    def drop_eq(sf, sz, /):
        'uint -> None|^EOFError'
        check_int_ge(0, sz)
        if not sz:return
        it = sf._it
        if not it.len_ge(sz):raise EOFError
        it.drop_le(sz)
        sf._i += sz
        return

class IUIntOffset(IUIntCompressor):
    __slots__ = ()
    #@override
    lossy = False
class UIntEcho(IUIntOffset):
    __slots__ = ()
    #@override
    offset = 0
from bisect import bisect_left
class IUIntCompressor__bisect_left(IUIntCompressor):
    __slots__ = ()
    @property
    @abstractmethod
    def seq4max_uint4interval(sf, /):
        '-> [uint]'
from seed.math.floor_ceil import ceil_div
class IUIntCompressor__ceil_div(IUIntCompressor):
    __slots__ = ()
    @property
    @abstractmethod
    def offset(sf, /):
        '-> uint'
    @property
    @abstractmethod
    def divisor(sf, /):
        '-> uint{>=1}'



#.from seed.int_tools.RadixInfo import IZpowRadixInfo# ZpowRadixInfo, mk_ZpowRadixInfo_
#.from seed.int_tools.RadixInfo import IRadixInfo# RadixInfo, mk_RadixInfo_
#.class IState4StepDecoder4UInt(ABC):
#.    __slots__ = ()
#.    ######################
#.    @abstractmethod
#.    def ireplace_(sf, case, payload, /):
#.        '-> IState4StepDecoder4UInt'
#.    ######################
#.    @property
#.    @abstractmethod
#.    def case(sf, /):
#.        '-> Hashable'
#.    @property
#.    @abstractmethod
#.    def payload(sf, /):
#.        '-> ??? # [[is_final] => [payload is result uint]]'
#.    @property
#.    @abstractmethod
#.    def radix_info4remain8head(sf, /):
#.        '-> IRadixInfo # (.is_zpow_radix|IZpowRadixInfo) => [.radix===2**num_remain_bits8head] # allow [num_remain_bits8head > num_bits4digit]'
#.    @property
#.    @abstractmethod
#.    def remain_digit8head(sf, /):
#.        '-> uint%radix # (.is_zpow_radix|IZpowRadixInfo) => uint%2**num_remain_bits8head'
#.    @property
#.    @abstractmethod
#.    def num_required_digits(sf, /):
#.        '-> uint{>=0} # [is_final==(0==num_required_digits)]'
#.    ######################
#.    @property
#.    def num_remain_bits8head(sf, /):
#.        '-> (uint{>=0} if (.is_zpow_radix|IZpowRadixInfo) else ^AttributeError) # allow [num_remain_bits8head > num_bits4digit]'
#.        return sf.radix_info4remain8head.num_bits4digit
#.    @property
#.    def max_remain_digit8head(sf, /):
#.        '-> uint{==radix-1}'
#.        return sf.radix_info4remain8head.max_digit
#.    @property
#.    def tmay_result_uint(sf, /):
#.        '-> tmay uint # [is_final==bool(tmay_result_uint)]'
#.        return (sf.payload,) if sf.is_final else ()
#.    @property
#.    def is_final(sf, /):
#.        '-> bool'
#.        return not sf.num_required_digits
#.    ######################
#.
#.def max_digit5num_bits_ex_(num_bits, imay_max_digit, /):
#.    'num_bits/uint{>=0} -> imay max_digit -> max_digit/uint{>=0}{==2**num_bits-1}'
#.    return max_digit5num_bits_(num_bits) if imay_max_digit==-1 else imay_max_digit
#.def max_digit5num_bits_(num_bits, /):
#.    'num_bits/uint{>=0} -> max_digit/uint{>=0}{==2**num_bits-1}'
#.    return (1<<num_bits)-1
#.class State4StepDecoder4UInt__plain(IState4StepDecoder4UInt):
#.    ___no_slots_ok___ = True
#.    def __init__(sf, case, payload, radix_info4remain8head, remain_digit8head, num_required_digits, /):
#.        sf._t = (case, payload, radix_info4remain8head, remain_digit8head, num_required_digits)
#.    @override
#.    def ireplace_(sf, case, payload, /):
#.        '-> IState4StepDecoder4UInt'
#.        return __class__(case, payload, *sf._t[2:])
#.    @property
#.    @override
#.    def case(sf, /):
#.        return sf._t[0]
#.    @property
#.    @override
#.    def payload(sf, /):
#.        return sf._t[1]
#.    @property
#.    @override
#.    def radix_info4remain8head(sf, /):
#.        return sf._t[2]
#.    @property
#.    @override
#.    def remain_digit8head(sf, /):
#.        return sf._t[3]
#.    @property
#.    @override
#.    def num_required_digits(sf, /):
#.        return sf._t[4]
#.#end-class State4StepDecoder4UInt__plain(IState4StepDecoder4UInt):
#.
#.
#.class IStepDecoder4UInt(ABC):
#.    # 后刹=>LL1,剩余 不足 1躯胞
#.    __slots__ = ()
#.    ######################
#.    @property
#.    @abstractmethod
#.    def num_bits4digit(sf, /):
#.        '-> uint{>=1}'
#.    @property
#.    @abstractmethod
#.    def max_digit(sf, /):
#.        '-> uint{>=1}'
#.    ######################
#.    @abstractmethod
#.    def start_(sf, num_bits4macro_header, imay_max_digit8macro_header, digit8macro_header, /):
#.        'num_bits4macro_header/uint{>=0} -> imay_max_digit8macro_header/imay uint{==2**num_bits4macro_header-1} -> digit8macro_header/uint%2**num_bits4macro_header -> st/IState4StepDecoder4UInt # allow [num_bits4macro_header > num_bits4digit]'
#.    @abstractmethod
#.    def feed_(sf, st, required_digits, /):
#.        'st/IState4StepDecoder4UInt -> required_digits/[uint%2**num_bits4digit]{len==st.num_required_digits} -> st/IState4StepDecoder4UInt'
#.    ######################
#.
#.
#.from seed.int_tools.count_num_leading1s import count_num_leading1s_, count_num_leading1s_ex_
#.class IStepDecoder4UInt__dynamic_bits(IStepDecoder4UInt):
#.    r'''[[[
#.    '[dynamic_bits =[def]= regex"1*0"]'
#.    [st == State4StepDecoder4UInt__plain(b_final,num_leading1s{acc}, ...)]
#.    #]]]'''#'''
#.    __slots__ = ()
#.    @override
#.    def start_(sf, num_bits4macro_header, imay_max_digit8macro_header, digit8macro_header, /):
#.        return sf._work(0, num_bits4macro_header, imay_max_digit8macro_header, digit8macro_header)
#.    @override
#.    def feed_(sf, st, required_digits, /):
#.        assert not st.case
#.        [digit] = required_digits
#.        return sf._work(st.payload, sf.num_bits4digit, sf.max_digit, digit)
#.
#.    def _work(sf, acc_num_leading1s, num_bits4macro_header, imay_max_digit8macro_header, digit8macro_header, /):
#.        max_digit8macro_header = max_digit5num_bits_ex_(num_bits4macro_header, imay_max_digit8macro_header)
#.        (num_leading1s, imay_num_bits4remain) = count_num_leading1s_ex_(num_bits4macro_header, max_digit8macro_header, digit8macro_header)
#.        acc_num_leading1s += num_leading1s
#.        if -1 == imay_num_bits4remain:
#.            return State4StepDecoder4UInt__plain(False,acc_num_leading1s,   ZpowRadixInfo(0),0,   1)
#.        num_bits4remain = imay_num_bits4remain
#.        max_digit4remain = max_digit5num_bits_(num_bits4remain)
#.        digit4remain = max_digit4remain & digit8macro_header
#.        zpow_radix_info4remain = ZpowRadixInfo(num_bits4remain,max_digit=max_digit4remain)
#.        return State4StepDecoder4UInt__plain(True,acc_num_leading1s,   zpow_radix_info4remain,digit4remain,   0)
#.#end-class IStepDecoder4UInt__dynamic_bits(IStepDecoder4UInt):
#.
#.
#.from seed.int_tools.RadixInfo import ZpowRadixInfo
#.from seed.int_tools.concat_digits2bytes import concat_digits2uint_, concat_digits2bytes_, concat_digits2iter_bytess_
#.#.from seed.types.BitList import BitList
#.#.def bitlist5digit_(zpow8radix, digit, /):
#.#.    payload_uint = zpow8radix | digit
#.#.    return BitList(payload_uint)
#.
#.from itertools import islice
#.from seed.math.floor_ceil import ceil_div
#.class IStepDecoder4UInt__fixed_size_bits(IStepDecoder4UInt):
#.    r'''[[[
#.    '[fixed_size_bits =[def]= regex"[01]{N}"]'
#.    [st == State4StepDecoder4UInt__plain(b_final,(uint|(sz/uint,uint){acc:bit_list}), ...)]
#.    #]]]'''#'''
#.    __slots__ = ()
#.    @property
#.    @abstractmethod
#.    def num_bits4read(sf, /):
#.        '-> uint{>=1} # since always consume at least 1bit instead of lookahead1'
#.
#.    @override
#.    def start_(sf, num_bits4macro_header, imay_max_digit8macro_header, digit8macro_header, /):
#.        return sf._work(sf.num_bits4read, num_bits4macro_header, imay_max_digit8macro_header, digit8macro_header)
#.    @override
#.    def feed_(sf, st, required_digits, /):
#.        assert not st.case
#.        assert st.num_required_digits == len(required_digits)
#.        (num_bits4macro_header,digit8macro_header) = st.payload
#.        num_bits4digit = sf.num_bits4digit
#.        num_bits4remain = num_bits4macro_header +num_bits4digit*len(required_digits) -sf.num_bits4read
#.        assert 0 <= num_bits4remain < num_bits4digit
#.        if num_bits4remain:
#.            digit = required_digits[-1]
#.            max_digit4remain = max_digit5num_bits_(num_bits4remain)
#.            digit4remain = max_digit4remain & digit
#.            last_digit = digit >> num_bits4remain
#.            num_bits4last_digit = num_bits4digit -num_bits4remain
#.            num_mid_digits = len(required_digits)-1
#.        else:
#.            num_mid_digits = len(required_digits)
#.            last_digit = 0
#.            num_bits4last_digit = 0
#.            max_digit4remain = 0
#.            digit4remain = 0
#.        #.radix4digit = 1<<num_bits4digit
#.        #.bs = bitlist5digit_(1<<num_bits4macro_header, digit8macro_header)
#.        #.for digit in islice(required_digits, 0, num_mid_digits)
#.        #.    bs += bitlist5digit_(radix4digit, digit)
#.        #.bs += bitlist5digit_(1<<num_bits4last_digit, last_digit)
#.
#.        #.result = int(bs.to_01str(), 2)
#.        zri4macro_header = ZpowRadixInfo(num_bits4macro_header)
#.        zri4digit = ZpowRadixInfo(num_bits4digit)
#.        zri4last_digit = ZpowRadixInfo(num_bits4last_digit)
#.        def __(zri4digit):
#.            yield (zri4macro_header, digit8macro_header)
#.            for digit in islice(required_digits, 0, num_mid_digits)
#.                yield (zri4digit, digit)
#.            yield (zri4last_digit, digit8last_digit)
#.        result = concat_digits2uint_((-sf.num_bits4read)%8, __(zri4digit))
#.        zpow_radix_info4remain = ZpowRadixInfo(num_bits4remain,max_digit=max_digit4remain)
#.        return State4StepDecoder4UInt__plain(True,result,   zpow_radix_info4remain, ,digit4remain,   0)
#.
#.    def _work(sf, num_bits4read, num_bits4macro_header, imay_max_digit8macro_header, digit8macro_header, /):
#.        num_bits4miss = num_bits4read -num_bits4macro_header
#.        if num_bits4miss > 0:
#.            num_required_digits = ceil_div(num_bits4miss, sf.num_bits4digit)
#.            return State4StepDecoder4UInt__plain(False,(num_bits4macro_header,digit8macro_header),   ZpowRadixInfo(0),0,   num_required_digits)
#.        num_bits4remain = -num_bits4miss
#.        max_digit4remain = max_digit5num_bits_(num_bits4remain)
#.        digit4remain = max_digit4remain & digit8macro_header
#.        result = digit8macro_header >> num_bits4remain
#.        zpow_radix_info4remain = ZpowRadixInfo(num_bits4remain,max_digit=max_digit4remain)
#.        return State4StepDecoder4UInt__plain(True,result,   zpow_radix_info4remain,digit4remain,   0)
#.#end-class IStepDecoder4UInt__fixed_size_bits(IStepDecoder4UInt):
#.class IStepDecoder4UInt__dynamic_bits_with_dependent_size_bits(IStepDecoder4UInt):
#.    r'''[[[
#.    '[dynamic_bits_with_dependent_size_bits =[def]= regex"1*0[01]{len:=???}"]'
#.    [st == State4StepDecoder4UInt__plain(b_final,(uint|st4dybits|st4szbits), ...)]
#.    #]]]'''#'''
#.    __slots__ = ()
#.    @property
#.    @abstractmethod
#.    def step_decoder4uint4dynamic_bits(sf, /):
#.        '-> IStepDecoder4UInt__dynamic_bits'
#.    @abstractmethod
#.    def mk_step_decoder4uint4fixed_size_bits_(sf, num_bits4read, /):
#.        'uint{>=1} -> IStepDecoder4UInt__fixed_size_bits'
#.    @abstractmethod
#.    def mk_result_uint_(sf, uint8dybits, uint8szbits, /):
#.        'uint8dybits/uint{>=0} -> uint8szbits/uint{>=0} -> uint{>=0} # [uint8dybits==len_dynamic_bits{#the 0bit not in count#}][uint8szbits == (0|num_bits4read)]'
#.
#.    @override
#.    def start_(sf, num_bits4macro_header, imay_max_digit8macro_header, digit8macro_header, /):
#.        st4dybits = sf.step_decoder4uint4dynamic_bits.start_(num_bits4macro_header, imay_max_digit8macro_header, digit8macro_header)
#.        zpow_radix_info4remain = ZpowRadixInfo(num_bits4macro_header,max_digit=imay_max_digit8macro_header)
#.        TODO:start_,改成 使用 RadixInfo
#.from seed.int_tools.RadixInfo import IZpowRadixInfo, ZpowRadixInfo, mk_ZpowRadixInfo_
#.from seed.int_tools.RadixInfo import IRadixInfo, RadixInfo, mk_RadixInfo_
#.        return State4StepDecoder4UInt__plain(0,st4dybits,   zpow_radix_info4remain,digit4remain,   0)
#.    @override
#.    def feed_(sf, st, required_digits, /):
#.        assert not st.case
#.        assert st.num_required_digits == len(required_digits)
#.        (num_bits4macro_header,digit8macro_header) = st.payload
#.
#.
#.#end-class IStepDecoder4UInt__dynamic_bits_with_dependent_size_bits(IStepDecoder4UInt):


from functools import cached_property
class IPlugin4UIntInterval(ABC):
    r'''[[[
    'plugin4interval{uint}'

    [macro_head_digit===digit{macro_header} :: uint%radix4macro_header]
    [offsetted_macro_head_digit==macro_head_digit+offset4macro_head_digit]
    [digit_reader{body_digit} :: IDigitReader]
    [body_digit===digit{body_cell} :: uint%radix4body_cell]
    #]]]'''#'''
    __slots__ = ()
    ######################
    @property
    @abstractmethod
    def offset4macro_head_digit(sf, /):
        '-> uint{>=0}'
    @abstractmethod
    def peek_test_digits_(sf, offsetted_macro_head_digit, digit_reader, /):
        'offsetted_macro_head_digit -> IDigitReader -> may byproduct7reader # [None=>not_ok]'
        #.def peek_test_digits_(sf, offsetted_macro_head_digit, num_digits4dropping7macro_header, digit_reader, /):
        #.    'offsetted_macro_head_digit -> num_digits4dropping7macro_header/uint -> IDigitReader -> may byproduct7reader # [None=>not_ok] #[should digit_reader.drop_eq(num_digits4dropping7macro_header) before read/peek]'
        #.def peek_test_digits_(sf, digit_reader, /):
        #.    'IDigitReader -> may byproduct7reader # [None=>not_ok]'
    @abstractmethod
    def decode_digits_ex_(sf, digit_reader, byproduct7reader, /):
        'IDigitReader -> byproduct7reader -> uint|^EOFError|^DecodeError'
    ######################
    def decode_digits_(sf, offsetted_macro_head_digit, digit_reader, /):
        'offsetted_macro_head_digit -> IDigitReader -> uint|^EOFError|^DecodeError'
        #.def decode_digits_(sf, digit_reader, /):
        #.    'IDigitReader -> uint|^EOFError|^DecodeError'
        may_byproduct7reader = sf.peek_test_digits_(offsetted_macro_head_digit, digit_reader)
        if may_byproduct7reader is None: raise EOFError
        byproduct7reader = may_byproduct7reader
        u = sf.decode_digits_ex_(digit_reader, byproduct7reader)
                # |^EOFError|^DecodeError
        return u
    ######################
    @abstractmethod
    def test_uint_(sf, u, /):
        'uint -> may byproduct7uint # [None=>not_ok]'
    @abstractmethod
    def iter_encode_uint_ex_(sf, u, byproduct7uint, /):
        'uint -> byproduct7uint -> digitss/(Iter (Iter Digit{j}))'
    ######################
    def iter_encode_uint_(sf, u, /):
        'uint -> digitss/(Iter (Iter Digit{j}))|^OverflowError'
        check_int_ge(0, u)
        may_byproduct7uint = sf.test_uint_(u)
        if may_byproduct7uint is None: raise OverflowError
        byproduct7uint = may_byproduct7uint
        digitss = sf.iter_encode_uint_ex_(u, byproduct7uint)
        return digitss
    ######################
    # #但:[极大可能:[IPlugin4InfiniteInterval.宏头胞 =!= IPlugin4FiniteInterval.宏头胞]] => [宏头胞 不一致; 未必是二幂]
    # !! IPlugin4InfiniteInterval=>要求:[躯胞 为 二幂]
    # !! [躯部::[躯胞]][]躯部 一致 => 要求:[躯胞 一致]
    # => [躯胞 一致 为 二幂]
    @property
    @abstractmethod
    def num_bits4body_cell(sf, /):
        '-> uint{>=1}'
        #爻元数纟躯胞
    ######################
    @cached_property
    def radix4body_cell(sf, /):
        '-> uint{>=2}'
        return 1<<sf.num_bits4body_cell
    @cached_property
    def max_digit4body_cell(sf, /):
        '-> uint{>=1}'
        return sf.radix4body_cell-1
    ######################
    @property
    @abstractmethod
    def radix4macro_header(sf, /):
        '-> uint{>=1}'
        # not {>=1}: e.g. "+[0-9]+"/[radix4macro_header == 1]
    @cached_property
    def max_digit4macro_header(sf, /):
        '-> uint{>=0}'
        return sf.radix4macro_header-1
    ######################
    @property
    @abstractmethod
    def num_layers(sf, /):
        '-> uint{>=1}'
    @abstractmethod
    def layer_idx2uint_compressor(sf, layer_idx, /):
        'layer_idx/uint%num_layers -> uint_compressor/IUIntCompressor'
    ######################
    ######################
class IPlugin4InfiniteInterval(IPlugin4UIntInterval):
    r'''[[[
    'plugin4infinite_interval{uint}'

    ######################
    [:doc4IPlugin4InfiniteInterval]:goto
    ######################
    主打方案:编码方案{变步变殿后动态爻元}
        [:约束牜紧凑乊首层]:goto
    #]]]'''#'''
        #xxx:*编码方案{大步固殿后动态爻元}
    __slots__ = ()
    ######################
    #第零层:动态层/layer0/(dynamic_part++follower_part)
    @property
    @abstractmethod
    def num_layers(sf, /):
        '-> uint{>=2}'
        #原版:'-> uint{>=1}'
    ######################
    #取消:step/step_(w)
    #   !! 应该归入:ucmprsr0/IUIntCompressor{@0}
    #.# !! 使用 变步变殿后动态爻元 #xxx:大步固殿后动态爻元
    #.@property
    #.@abstractmethod
    #.def step(sf, /):
    #.    '-> uint{>=1}'
    #.    #步长

    #升级:num_bits4follower4dynamic_part-->num_bits4follower5len_dynamic_bits_
    #   !! 使用 变步变殿后动态爻元 而非 大步固殿后动态爻元
    #.@property
    #.@abstractmethod
    #.def num_bits4follower4dynamic_part(sf, /):
    #.    '-> uint{>=0}'
    #.    #num_following_bits4dynamic_bits
    #.    #num_following_bits4dynamic_part
    #.    #爻元数纟殿后爻元
    @abstractmethod
    def num_bits4follower5len_dynamic_bits_(sf, len_dynamic_bits, /):
        'len_dynamic_bits/uint{>=0} -> num_bits4follower4dynamic_part/uint{>=0}' \
        '   # [:约束牜紧凑乊首层]:goto'
        #num_following_bits4dynamic_bits
        #num_following_bits4dynamic_part
        #num_bits4follower4dynamic_part
        #爻元数纟殿后爻元{数目纟动态爻元}
    @abstractmethod
    def classify_compressed_uint6layer0(sf, s_uint0, /):
        'uint{>=0} -> len_dynamic_bits/uint{>=0}'
        #『s_uint0』:
        #   『s』repr small/compressed
        #   『0』repr layer0
        #######
        #大步固殿后动态爻元=>return (s_uint0 // 2**num_bits4follower4dynamic_part)
        #变步变殿后动态爻元=>return max{len_dynamic_bits | [len_dynamic_bits:<-[0..<]][offset4follower4dynamic_part{len_dynamic_bits} <= s_uint0]}
        #   !! 采用 分段累积法
        #######
    @abstractmethod
    def offset4follower5len_dynamic_bits_(sf, len_dynamic_bits, /):
        'len_dynamic_bits/uint{>=0} -> offset4follower4dynamic_part/uint{>=0}'
        #######
        #大步固殿后动态爻元=>return len_dynamic_bits*2**num_bits4follower4dynamic_part
        #变步变殿后动态爻元=>return sum{2**num_bits4follower4dynamic_part{_len_dynamic_bits} | [_len_dynamic_bits:<-[0..<len_dynamic_bits]]}
        #   !! 采用 分段累积法
        #######

    ######################
    # !! 使用 动态爻元 而非 动态苞元
    # => 要求:[宏头胞&躯胞 可完美拆分为 爻元串]
    # =>要求:[宏头胞&躯胞 为 二幂]
    @property
    @abstractmethod
    def num_bits4macro_header(sf, /):
        '-> uint{>=0}'
        # not {>=1}: e.g. "+[0-9]+"/[radix4macro_header == 1]
        #爻元数纟宏头胞
    ######################
    @cached_property
    @override
    def radix4macro_header(sf, /):
        '-> uint{>=1}'
        return 1<<sf.num_bits4macro_header
    ######################
    ######################
from seed.int_tools.count_num_leading1s import count_num_leading1s_, count_num_leading1s_ex_
from seed.int_tools.count_num_leading1s import count_num_leading0s_, count_num_leading0s_ex_
    #(num_leading0s, imay_num_bits4payload) = count_num_leading0s_ex_(num_bits4digit, digit)
from seed.int_tools.digits.uint25radix_repr import uint2radix_repr_, uint5radix_repr_
>>> [*uint2radix_repr_(10, 963, is_big_endian=False)]
>>> uint5radix_repr_(10, [], is_big_endian=False)
class IPlugin4InfiniteInterval__dynamic_bits(IPlugin4InfiniteInterval):
    'impl:编码方案{变步变殿后动态爻元}#dynamic_bits'
    TODO:
    ######################
    @override
    def peek_test_digits_(sf, offsetted_macro_head_digit, digit_reader, /):
        'offsetted_macro_head_digit -> IDigitReader -> may byproduct7reader # [None=>not_ok]'
        offset4h = sf.offset4macro_head_digit
        if not offsetted_macro_head_digit >= offset4h:
            return None
        macro_head_digit = offsetted_macro_head_digit -offset4h
        if not macro_head_digit < sf.radix4macro_header:
            return None
        byproduct7reader = macro_head_digit
        return byproduct7reader
    @override
    def decode_digits_ex_(sf, digit_reader, byproduct7reader, /):
        'IDigitReader -> byproduct7reader -> uint|^EOFError|^DecodeError'
        macro_head_digit = byproduct7reader
        if not macro_head_digit == sf.max_digit4macro_header:
            max_digits = ()
        else:
            max_digits = (macro_head_digit, *digit_reader.read_while(sf.max_digit4body_cell.__eq__))
        max_digits
        num_max_digits = len(max_digits)
        b_head = num_max_digits==0
        max_digit = sf.max_digit4macro_header if b_head else sf.max_digit4body_cell
        num_bits4digit = sf.num_bits4macro_header if b_head else sf.num_bits4body_cell
        digit = macro_head_digit if b_head else digit_reader.peek1()
        (num_leading1s, imay_num_bits4payload) = count_num_leading1s_ex_(num_bits4digit, max_digit, digit)
        assert imay_num_bits4payload >= 0
        num_bits4payload = imay_num_bits4payload
        #len_dynamic_bits = (0 if b_head else (sf.num_bits4macro_header + (0 if num_max_digits==1 else (num_max_digits-1)*sf.num_bits4body_cell))) + (num_leading1s+1)
            # 『1』in『(num_leading1s+1)』repr the terminal 『0』/terminator
        len_dynamic_bits = (0 if b_head else (sf.num_bits4macro_header + (0 if num_max_digits==1 else (num_max_digits-1)*sf.num_bits4body_cell))) + (num_leading1s+0x000)
            # 『0x000』in『(num_leading1s+1)』repr excluding the terminal 『0』/terminator
        assert sf.num_layers >= 2
        ucmprsr0 = sf.layer_idx2uint_compressor(0)
            # 『0』repr layer0
        uint0 = ucmprsr0.uncompress(len_dynamic_bits)
        _num_digits1 = sf.step*uint0
            # leading『_』repr 『exclued:num_bits4payload』
            # 『1』repr layer1
        num_leading_bits1 = num_bits4payload
        mask = ((1<<num_leading_bits1)-1)
        leading_digit1 = mask&digit
        tail_digits1 = digit_reader.read_eq(_num_digits1)
        digits1 = chain([leading_digit1], tail_digits1)
        s_uint1 = uint5radix_repr_(sf.radix4body_cell, digits1, is_big_endian=True)
            # 『s』repr small/compressed
        ucmprsr1 = sf.layer_idx2uint_compressor(1)
            # 『1』repr layer1
        uint1 = ucmprsr1.uncompress(s_uint1)
        uintX = uint1
        for layer_idx in range(2, sf.num_layers):
            #######
            777;uint4prev_layer = uintX
            777;uintX = None
            #######
            # layerX
            num_digitsX = uint4prev_layer
                # 『X』repr layerX
            digitsX = digit_reader.read_eq(num_digitsX)
            s_uintX = uint5radix_repr_(sf.radix4body_cell, digitsX, is_big_endian=True)
            ucmprsrX = sf.layer_idx2uint_compressor(layer_idx)
            uintX = ucmprsrX.uncompress(s_uintX)
        u = uintX
        return u

    ######################
    ######################
    @override
    @abstractmethod
    def test_uint_(sf, u, /):
        'uint -> may byproduct7uint # [None=>not_ok]'
        ucmprsr7last = sf.layer_idx2uint_compressor(sf.num_layers-1)
        if not u >= ucmprsr7last.offset:
            return None
        return True
    @override
    @abstractmethod
    def iter_encode_uint_ex_(sf, u, byproduct7uint, /):
        'uint -> byproduct7uint -> digitss/(Iter (Iter Digit{j}))'
        assert byproduct7uint is True
        assert sf.num_layers >= 2
        digitss = []
        ls4num_leading0s = []
        _uintX = u
        for j, layer_idx in enumerate(range(1, sf.num_layers)[::-1]):
            #layerX
            _uintX
            ucmprsrX = sf.layer_idx2uint_compressor(layer_idx)
            s_uintX = ucmprsrX.compress(_uintX)
                # 『s』repr small/compressed
            uintX = ucmprsrX.uncompress(s_uintX)
            num_leading0s = uintX-_uintX
            if not num_leading0s == 0:
                if not num_leading0s > 0:raise 000
                if not j > 0:raise 000
            digitsX = uint2radix_repr_(sf.radix4body_cell, s_uintX, is_big_endian=True)
            digitss.append(digitsX)
            if j > 0:ls4num_leading0s.append(num_leading0s)
            #######next round:
            uintX = len(digitsX)
        assert len(digitss) == 1+len(ls4num_leading0s)
        digitss, ls4num_leading0s
            #reversed
            #[..., digits1]
            #[..., num_leading0s{digits2}]
        assert len(digitss) == len(ls4num_leading0s)
        digits1 = digitss.pop()
        digitss, ls4num_leading0s
            #reversed
            #[..., digits2]
            #[..., num_leading0s{digits2}]
        layer_idx, uintX
        assert layer_idx == 0
        uint0 = uintX
        digits1
        TODO...殿后爻元

    ######################
    ######################
class IPlugin4FiniteInterval(IPlugin4UIntInterval):
    'plugin4finite_interval{uint}'
    __slots__ = ()
    # !! [宏头胞 不一致; 未必是二幂]
    # => 无:num_bits4macro_header

class Table4Codecs4uint:
    ___no_slots_ok___ = True
    def 
size4alphabet
size4body_cell
size4head_cell
[size4alphabet == size4head_cell+size4body_cell]
!! size4macro_header{plugin4interval}
xxx:size4macro_header
xxx:[size4macro_header >= size4head_cell]
([(prefix_digits, plugin4finite_interval)], (prefix_digits, plugin4infinite_interval))

class ICodecs4uint(ABC):
    '[codecs4uint :: uint <-> [Digit{j}/uint%radix{j}]]'
    __slots__ = ()
    @abstractmethod
    def _encode_uint_(sf, u, /):
        'uint -> Iter (Iter digit{j})'
    @abstractmethod
    def _decode_uint_(sf, digit_reader, /):
        'IDigitReader -> uint|^EOFError|^DecodeError'
    def encode_uint_(sf, u, T=tuple, /):
        'uint -> [digit{j}]'
        return T(chains(sf._encode_uint_(u)))
    def decode_uint__reader_(sf, digit_reader, /):
        'IDigitReader -> uint|^EOFError|^DecodeError'
        return sf._decode_uint_(digit_reader)
    def decode_uint__seq_(sf, digit_seq, /):
        '[digit{j}] -> uint|^EOFError|^DecodeError'
    def decode_uint__iter_(sf, digits, /):
        'Iter digit{j} -> uint|^EOFError|^DecodeError'

class ICodecs4int(ABC):
    '[codecs4int :: int <-> [Digit{j}/uint%radix{j}]]'
    __slots__ = ()
    def __(sf, /):
        ...:



from seed.int_tools.StepDecoder import IStepDecoder
    ######################
    @property
    @abstractmethod
    def radix_info4digit(sf, /):
        '-> IRadixInfo{radix>=2}'
    ######################
    ######################
    @abstractmethod
    def start_(sf, rxdigit8macro_header, /):
        'rxdigit8macro_header/IRadixedDigit -> st/IBaseState4StepDecoder # allow [num_bits4macro_header > num_bits4digit]'
    @abstractmethod
    def feed_digits_(sf, loop_st7nonfinal, required_digits, /):
        'loop_st7nonfinal/ILoopState4StepDecoder{not is_final_st} -> required_digits/[uint%2**num_bits4digit]{len==loop_st7nonfinal.num_required_digits} -> st/IBaseState4StepDecoder'
    @abstractmethod
    def feed_oresult_remain_(sf, call_st7nontail, oresult7subcall, rxdigit8remain7subcall, /):
        'call_st7nontail/ICallState4StepDecoder{not is_tail_call_st} -> oresult7subcall{return from subcall} -> rxdigit8remain7subcall{return from subcall} -> st/IBaseState4StepDecoder'
    ######################
from seed.int_tools.StepDecoder import IStepDecoder__dynamic_bits, IStepDecoder__fixed_size_bits, IStepDecoder__fixed_size_xbcells
from seed.int_tools.StepDecoder import CallEntry4StepDecoder, Kind4State4StepDecoder, LoopState4StepDecoder__plain, CallState4StepDecoder__plain
    def mk_call_st5four_args_(cls, case, payload, step_decoder4call, state4call, /):
_CallST = CallState4StepDecoder__plain

from seed.int_tools.DigitReader import ISubSeq, IDigitReader, IDigitReader5iter, IDigitReader5seq, IDigitReader5bytes, IDigitReader5binary_file, IDigitReader5text_file
from seed.int_tools.DigitReader import DigitReader5seq, DigitReader5iter, DigitReader5bytes, DigitReader5binary_file, DigitReader5text_file
from seed.int_tools.DigitReader import SubSeq, DigitReader5seq


from enum import Enum, auto
from seed.for_libs.for_collections.override_repr4namedtuple import mk_namedtuple_
from seed.types.Either import Cased, Either
from seed.types.Either import mk_Left, mk_Right

from seed.int_tools.RadixInfo import IZpowRadixInfo, ZpowRadixInfo# mk_ZpowRadixInfo_
from seed.int_tools.RadixInfo import IRadixInfo# RadixInfo, mk_RadixInfo_
from seed.int_tools.RadixInfo import IRadixedDigit, RadixedDigit

from seed.helper.ConstantRepr import ConstantRepr
from seed.int_tools.DigitReader import IDigitReader





__all__
from seed.int_tools.digits.codecs4int import *
