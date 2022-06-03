r'''

seed.seq_tools.escape_schemes.universal_single_point_escape_scheme__enable_raw_text__disable_recur
py -m seed.seq_tools.escape_schemes.universal_single_point_escape_scheme__enable_raw_text__disable_recur

e ../../python3_src/seed/seq_tools/escape_schemes/universal_single_point_escape_scheme__enable_raw_text__disable_recur.py
view ../../python3_src/seed/iters/PeekableIterator.py


=================================
below copy from:
    view ../../python3_src/自己的相关数据/on_working.txt
=================================
[[[
原貌字符串
  求一有效结束串囗特定原貌字符串(结束串的结束串，结束串字集，原貌字符串)
    前置条件:
      [len(结束串的结束串) > 0]
      [len(结束串字集) >= 3]
        因为：
        [len(结束串的结束串) == 1][len(结束串字集) == 2][结束串的结束串[0] <- 结束串字集]:
          let ch = 结束串字集\-\{结束串的结束串[0]}
          [?n. 结束串=ch*n]
          [原貌字符串==ch*1]:
            [原貌字符串 必然 提前终止]
            [所有允许编码的结束串均无效]
    后置条件:
      let s = f'{结束串}{结束串的结束串}{原貌字符串}{结束串}'
          a, b, c = s.partition(结束串的结束串)
          d, e, f = c.partition(a)
      assert b == 结束串的结束串
      assert a == e  ##== 任一有效结束串
      assert f == ''
      assert d == 原貌字符串

    简单起见：
      [s 没有 非空真子双缀] =[def]= [@sz. [0 < sz < len(s)] --> [s[:sz] =!= s[len(s)-sz:]]]
      要求『结束串的结束串』没有『非空真子双缀』，以防『结束串』提取终止。
      要求『结束串』没有『非空真子双缀』，以防『原貌字符串』提取终止。

  简单起见：
    由于『结束串的结束串』与『结束串字集』完全受控，可要求使用『结束串的结束串囗单字符』，该字符不在『结束串字集』中。
    再改，将该字符作为『结束串』的尾字符！

  修改格式为：
  求一有效结束串囗特定原貌字符串囗简化(结束串的结束串囗单字符，结束串减囗字集，原貌字符串)
    前置条件:
      [结束串的结束串囗单字符 <-!- 结束串减囗字集]
      [len(结束串减囗字集) >= 1]
        提高效率:[len(结束串减囗字集) >= 2]
          [len(结束串) = O(log<len(结束串减囗字集)>(len(原貌字符串)))]
        证明:[[n>=0][字符串s 包含 字集S的所有长度为n的字符串][len(S)>=1] --> [len(s) >= len(S)**n+(n-1)]]
          let N=len(S)
          !![N >= 0]
          [字集S的所有长度为n的字符串 非空]
          !![字符串s 包含 字集S的所有长度为n的字符串]
          [字符串s 包含 至少一个 字集S的长度为n的字符串]
          [len(s) >= n]

          [n == 0]:
            [len(S)**n+(n-1) = N**0+0-1 = 0 <= len(s)]
          [n>=1][N == 1]:
            [len(S)**n+(n-1) = 1**n+n-1 = n <= len(s)]
          #[n>=1][N >= 2]:
          [n>=1][N >= 1]:
            定义 有向图囗带自环囗无重边:
              节点集 为 字集S的所有长度为(n-1)的字符串
              有向边 连结 满足以下关系的任意两个节点:
                起点[1:] === 终点[:-1]
            ==>>
            [任一节点 出度 为 N]
            [任一节点 入度 为 N]
            [有向边总数===N*节点总数===N**n]
            !![字符串s 包含 字集S的所有长度为n的字符串]
            [需要遍历所有 有向边]
            !![s是字符串 而非 字符环]
            [s初始(n-1)个字符 并没有遍历任何 有向边]
            [len(s) >= (n-1)+有向边总数 === N**n+(n-1)]
    后置条件
      let 结束串=f'{结束串减}{结束串的结束串囗单字符}'
            # ==>> [『结束串』没有『非空真子双缀』]
            # ==>> [[结束串 not in 原貌字符串] --> [原貌字符串 不会 提前终止]]
          s = f'{结束串}{原貌字符串}{结束串}'
          a, b, c = s.partition(结束串的结束串囗单字符*1)
          d, e, f = c.partition(a+b)
      assert b == 结束串的结束串囗单字符*1
      assert a+b == e  ##== 任一有效结束串
      assert f == ''
      assert d == 原貌字符串
      ===找出一个最短的有效 结束串
      ？扫描一遍suffix_array(原貌字符串)
        不行，太多其他字符

      suffix_tree(原貌字符串)
      1.检查『结束串的结束串囗单字符』是否在『原貌字符串』中
        在则...
      2.检查(『结束串减囗字集』\-\『原貌字符串』)是否非空
        非空则...
      3. 找出原貌字符串的所有以『结束串减囗字集』中的字符开始的后缀，层层排查下去(依上面两点)


TODO
e ../../python3_src/seed/seq_tools/escape_schemes/universal_single_point_escape_scheme__enable_raw_text__disable_recur.py
  不允许嵌套但允许内嵌原貌字符串的通用单点转义方案
    txt -> (txt, [txt])
      #转义符 存在的意义 只是 切分 文本而已！
      #     原貌字符串 即使被识别出来，也应当融入 相邻文本
      #至于 转义符 之后 的 转义 序列 的 长度 再由 用户自定义
    [escape schemes]【转义方案】
    ===
    见上面:原貌字符串
    见下面:转义
    ===
    转义次数头囗字符串 <- 允空字符串
    转义次数尾囗字符串 <- 允空字符串
    转义次数数字表囗次序字集{len>=2,不重复,用户自定义次序}
    转义次数 = 转义次数数字表囗次序字集*
    最小转义次数囗字符串 <- 转义次数/-\允空字符串
    单点转义符 = 转义次数头囗字符串 最小转义次数囗字符串 转义次数尾囗字符串
      要求:[单点转义符 <- 非空字符串]
      [[
      ===感觉还是有问题
      ===假如只当作逗号用，能否避免被左右文本融合(而非 仅只要求『从左往右能解析』就成)？
        ==当然文本需要预处理: join(txts)=单点转义符.join(map 预处理 txts)
        ==预处理(txt)=再组(提升(切分<单点转义符囗下降空间>(txt)))
      ==>>边界清晰（无序解析无歧义）
      ==>>[@[a,b<-单点转义符囗下降空间] -> @[i<-[1..min(len a, len b)]] -> [a[-i:] === b[:i]] -> [a===b][i===len a]]
      ==>>:
      **
        [?i. [转义次数尾囗字符串[i] <-/- 转义次数数字表囗次序字集]]
        [?i. [转义次数头囗字符串[i] <-/- 转义次数数字表囗次序字集]]
        ==>> 两者非空！
      **
        [(转义次数头囗字符串++转义次数尾囗字符串) 没有 非空真子双缀]
      **
        lhs = regex_f'{head}[mid]{{L}}{tail}'
        rhs = regex_f'{head}[mid]{{R}}{tail}'

        非空
        +[len(head++tail) > 0]
        let [H=len(head)]
        let [T=len(tail)]

        左对齐
        +[R>L][lhs++regex_f'.{{R-L}}' =/= rhs]

        左不对齐
        +[regex_f'.+' ++lhs++regex_f'.+' =/= rhs]
        +[regex_f'.{{1,len(rhs)-1}}' ++lhs=/= rhs++regex_f'.*']
        or:
          not [regex_f'.{{0,len(rhs)-1}}' ++lhs++regex_f'.*'=== rhs++regex_f'.*']
        ***(not ===)
        let [I<-[0..len(rhs)-1]]
        [I+H+L+T+X===H+R+T+Y]
        * I cut H
          [0 <= I < H]
          * IH cut R
            * IHL cut R/T/Y
          * IH cut T
            * IHL cut T/Y
          * IH cut Y
        * I cut R
          [H <= I < H+R]
          * IH cut R
            * IHL cut R/T/Y
          * IH cut T
            * IHL cut T/Y
          * IH cut Y
        * I cut T
          [H+R <= I < H+R+T]
          * IH cut T
            * IHL cut T/Y
          * IH cut Y
        最多几种组合？
          命名8个点:
            lhs.I/H/L/T
            rhs.H/R/T/Y
          lhs.w 出现 在 rhs.z 之前，则 表示 lhs.I..w < rhs.H..z
          lhs.w 出现 在 rhs.z 之后，则 表示 lhs.I..w >= rhs.H..z
          因为lhs.IHLTX===rhs.HRTY, 故lhs.X不参与,但rhs.Y参与(『>=』==>>lhs.X必在rhs.Y之后)
          choose(4+4,4)=C(8,4)=8*7*6*5/(4*3*2*1)=70
          再除去:[lhs.IH.. < rhs.H] C(8-2,4-2)=C(6,2)=15种
              #再除去:[lhs.I..?0 < rhs.H..?1 <=[所有被包含,但R/Y不在lhs所以其实只有rhs.H] lhs.I..?0]
          再除去:[lhs.I >= rhs.HRT] C(8-3,4-3)=C(5,1)=5种
          70 -15 -5 =50
          已知长度:H,T
          未知长度:I,L,R,X,Y
            I/L/X 与 R/Y 重叠的部分 可取消
            这样一来，就不存在无限长度


      ]]

    单点转义符囗上升空间 = 转义次数头囗字符串 转义次数{次数(.)>次数(最小转义次数囗字符串)} 转义次数尾囗字符串
    单点转义符囗下降空间 =:
      | 单点转义符
      | 单点转义符囗上升空间

    单点转义序列 = 单点转义符 自结尾序列
    自结尾序列 = 单点转义序列囗公共头部囗字符串 转义种类头@kind 单点转义序列囗公共颈部囗字符串 特化自结尾序列的躯干<kind> 单点转义序列囗公共尾部囗字符串
    单点转义序列囗公共头部囗字符串 <- 允空字符串
    单点转义序列囗公共颈部囗字符串 <- 允空字符串
    单点转义序列囗公共尾部囗字符串 <- 允空字符串
    转义种类头 =:
      | 原貌字符串囗转义种类头囗字符串
      | ...
      要求:[转义种类头 <- 非空字符串]
      要求:[[转义次数尾囗字符串 <- 非空字符串]或[转义种类头[0] <-/- 转义次数数字表囗次序字集]]

    结束串囗前缀囗字符串 <- 允空字符串
    结束串囗后缀囗字符串 <- 非空字符串
    结束串囗中段囗字集{len>=2,不重复,标准次序}
    结束串囗中段囗字符串 = 结束串囗中段囗字集*
    结束串囗中后段囗字符串 = 结束串囗中段囗字符串 结束串囗后缀囗字符串

    结束串 = 结束串囗前缀囗字符串 结束串囗中段囗字符串 结束串囗后缀囗字符串

    特化自结尾序列的躯干<原貌字符串囗转义种类头囗字符串> =原貌字符串囗最小封装
    原貌字符串囗最小封装 =结束串@eos (.*?@原貌字符串) (.*){=eos}
      # 独立出来，可以 在其他组件中复用
      #
      # 第二个 结束串 用于 标识 原貌字符串 的 结束
      # 第一个 结束串，是 第二个结束串 的 定义(只针对 后面的 原貌字符串，局部使用)
      #==>>需要 识别 第一个 结束串
      #==>>结束串 自结尾
      #==>>使用 结束串囗后缀囗字符串
      [第一个 结束串 从左至右 可识别/自结尾] ==>>:
          结束串自结尾囗约束(结束串) =[def]= [?i. [结束串囗后缀囗字符串[i] <-/- 结束串囗中段囗字集]]
            #因此 非空
          结束串囗后缀囗中部字集极大后缀囗字符串 =[def]= 结束串囗后缀囗字符串[1+max{i|[[结束串囗后缀囗字符串[i] <-/- 结束串囗中段囗字集]]}:]
          [0 <= len(结束串囗后缀囗中部字集极大后缀囗字符串) < len(结束串囗后缀囗字符串)]
      结束串囗推论一: [[结束串自结尾囗约束(结束串)] -->> [结束串囗中后段囗字符串 的 真子双缀 最长为 len(结束串囗后缀囗中部字集极大后缀囗字符串)]]

      [第二个 结束串 从左至右 经过 原貌字符串 不会 提前出现] ==>>:
          结束串约束囗特化版<原貌字符串>(结束串) =[def]= [结束串 not in (原貌字符串++结束串)[:-1]]

      通用要求:
          #不指定 原貌字符串 的 情形下
          #虽然 结束串 永远是 特定于 原貌字符串 的，但 可以 通过 约束，指定 原貌字符串 集合 而非 特定某个
          #
          结束串约束囗通用版<结束串与原貌字符串的假设关系>(结束串) =[def]= [@原貌字符串. [结束串与原貌字符串的假设关系(结束串,原貌字符串)] -->> 结束串约束囗特化版<原貌字符串>(结束串)]


      基于用途囗细化要求:
        * 特定于 某 原貌字符串，用于 检查 用户提供 的 结束串
          假设:[结束串 not in 原貌字符串]
            # 『整个』结束串
            要求:[结束串  没有 非空真子双缀]
          即：结束串约束囗通用版<[结束串 not in 原貌字符串]>(结束串) <==> [结束串  没有 非空真子双缀]

        * 特定于 某 原貌字符串，用于 自动生成 长度为O(log(len(原貌字符串)))的 结束串
          假设甲:[结束串囗中后段囗字符串 not in (原貌字符串++结束串囗前缀囗字符串)]
            # 归属权更改: 结束串囗前缀囗字符串
          假设甲囗实现方案: 逆转 (原貌字符串++结束串囗前缀囗字符串)，针对 suffix_tree 其于 逆转 结束串囗后缀囗字符串 之下的 子树，求 逆转 结束串囗中段囗字符串
            # 不考虑 结束串囗前缀囗字符串 更容易 实现，但 所得并非最短！
            要求:[结束串  没有 长度大于len(结束串囗前缀囗字符串)的 真子双缀]

          即：结束串约束囗通用版<[结束串囗中后段囗字符串 not in (原貌字符串++结束串囗前缀囗字符串)]>(结束串) <==> [结束串  没有 长度大于len(结束串囗前缀囗字符串)的 真子双缀]


            一级简化要求(不考虑 结束串囗前缀囗字符串):[结束串囗中后段囗字符串  没有 非空真子双缀]
            二级简化要求(考虑 所有 结束串囗中段囗字符串)(不考虑 结束串囗前缀囗字符串):[结束串囗后缀囗字符串[-1] <-/- 结束串囗中段囗字集][结束串囗后缀囗字符串  没有 非空真子双缀]
                !! 结束串囗推论一
                <==> [结束串囗后缀囗字符串[-1] <-/- 结束串囗中段囗字集]
                  即 第二部分可省去

          假设乙:[[结束串囗中段囗字符串 not in 原貌字符串]或[两者皆空]]
            #假设甲囗实现方案 还是 比较 麻烦
          假设乙囗实现方案: 针对 原貌字符串suffix_tree，求 结束串囗中段囗字符串
            #bug:要求:[结束串  没有 长度大于min(len(结束串囗前缀囗字符串),len(结束串囗后缀囗字符串))的 真子双缀]
            要求:[结束串  没有 长度大于len(结束串囗后缀囗字符串)的 真子双缀]
              ##注意！与 假设甲 要求不同！！一个 前缀，一个 后缀

          即：结束串约束囗通用版<[[结束串囗中段囗字符串 not in 原貌字符串]或[两者皆空]]>(结束串) <==> [结束串  没有 长度大于len(结束串囗后缀囗字符串)的 真子双缀]
              !! 结束串囗推论一
              [结束串囗中后段囗字符串 的 真子双缀 最长为 len(结束串囗后缀囗中部字集极大后缀囗字符串)]
              [结束串 的 真子双缀 最长为 len(结束串囗前缀囗字符串)+len(结束串囗后缀囗中部字集极大后缀囗字符串)]

              结束串囗前缀囗中部字集极大前缀囗字符串 =[def]= 结束串囗前缀囗字符串[:min({len(结束串囗前缀囗字符串)}\-/{i|[[结束串囗前缀囗字符串[i] <-/- 结束串囗中段囗字集]]})]
              最大退步数 =[def]= [len(结束串囗前缀囗字符串) - (len(结束串囗后缀囗字符串)-len(结束串囗后缀囗中部字集极大后缀囗字符串))]
              === [len(结束串囗前缀囗字符串)+len(结束串囗后缀囗中部字集极大后缀囗字符串) - len(结束串囗后缀囗字符串)]

            等价要求:[结束串  没有 长度大于len(结束串囗后缀囗字符串) 且 小于等于len(结束串囗后缀囗字符串)+最大退步数 的 真子双缀]

            * [最大退步数 <= 0]:
              ok
            * [最大退步数 > 0]:
              ???见下面『退步数』

            @[退步数 <- [1..最大退步数]]:
              left_side_condition1 =[def]= [退步数 <= len(结束串囗中段囗字符串)]
                前缀 左侧 对照 的 退步串 完全属于 中段 #未触及 前缀
              right_side_condition1 =[def]= [退步数 <= len(结束串囗前缀囗字符串)+len(结束串囗中段囗字符串)-len(结束串囗后缀囗字符串)]
                #bug:后缀 右侧 对照 的 退步串 完全属于 中段
                后缀 右侧 对照 的 退步串 完全属于 前中段 #未触及 后缀
                * [right_side_condition1][len(结束串囗前缀囗字符串)<=len(结束串囗后缀囗字符串)]:
                    后缀 右侧 对照 的 退步串 完全属于 中段
              left_right_independent_condition =[def]= [left_side_condition1][right_side_condition1][2*(len(结束串囗后缀囗字符串)+退步数)<=len(结束串)]
                 === [left_side_condition1][right_side_condition1][len(结束串囗后缀囗字符串)+2*退步数 <= len(结束串囗前缀囗字符串)+len(结束串囗中段囗字符串)]
                 === [left_side_condition1][len(结束串囗后缀囗字符串)+2*退步数 <= len(结束串囗前缀囗字符串)+len(结束串囗中段囗字符串)]
                 === [left_side_condition1][2*退步数 <= len(结束串囗前缀囗字符串)+len(结束串囗中段囗字符串)-len(结束串囗后缀囗字符串)]
                 === [2*退步数 <= len(结束串囗中段囗字符串)+min{len(结束串囗中段囗字符串), len(结束串囗前缀囗字符串)-len(结束串囗后缀囗字符串)}]
                中段 等效于 无限长
              * [left_right_independent_condition][len(结束串囗前缀囗字符串)<=len(结束串囗后缀囗字符串)]:
                即：[中段 等效于 无限长][后缀 右侧 对照 的 退步串 完全属于 中段]
                要求:[[退步数>len(结束串囗前缀囗中部字集极大前缀囗字符串)]或[结束串囗前缀囗字符串[退步数:] =/= 结束串囗后缀囗字符串[:len(结束串囗前缀囗字符串)-退步数]]]


      检查通用要求:
        结束串约束囗通用版<[结束串 not in 原貌字符串]>(结束串) <==> [结束串  没有 非空真子双缀]
        即：检查 [@结束串囗中段囗字符串, [结束串  没有 非空真子双缀]]
        @[退步数 <- [1..最大退步数]]:
          @[变量数量 <- [0..中段等效无限长的最小长度(退步数)]]:
            要求:变量无解，即 不存在某个 中段 使得 在此 退步数 下 的 前缀与后缀 匹配
          [[DONE:
view others/数学/Disjoint-Set.txt
view ../../python3_src/seed/types/union_find_algo/DisjointSet.py
  特定 退步数: 建立 方程组，等价关系传播
grep 'union[ _-]\?find' -i -r . -a -l
grep 'disjoint[ _-]\?set' -i -r . -a -l
xxx view ../../python3_src/nn_ns/RecognizeSystem/Utils.py
view ../../python3_src/seed/types/MergableImmutable.py

view ../../python3_src/seed/algo/page_rank.py
  我的实现

view ../../python3_src/seed/algo/merge_sort.py
merge sort:
  结合律？
    重新打括号
    初始 划分极大上升组/下降组
  霍夫曼编码？
  等价于 求 二叉树，最小化 所有 子树的虚拟叶节点数之和
    二叉树的叶节点 的 虚拟叶节点数 即是 升降区长度(这里还有一个 边界归属问题))
  以前:矩阵乘法链 结合律 优化...
          ]]

      极度简化通用要求:
        +要求:[结束串囗后缀囗字符串[-1] <-/- 结束串囗前缀囗字符串]
        +要求:[结束串囗后缀囗字符串[-1] <-/- 结束串囗中段囗字集]
        #不需要:[结束串囗后缀囗字符串[-1] <-/- 结束串囗后缀囗字符串[:-1]]
    结束串
]]]
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
[[[
转义
  ...是否允许内嵌原貌字符串？==>>两种转义方案
      无条件全局一致转义
  ...是否允许重新配置转义方案？
      状态转移动态转义
  ...是否允许嵌套配置转义方案？
      状态嵌套局部转义
]]]


#'''


r'''
from seed.iters.PeekableIterator import PeekableIterator

class UniversalSinglePointEscapeScheme__enable_raw_text__disable_recur:
    转义次数头囗字符串 <- 允空字符串
    转义次数尾囗字符串 <- 允空字符串
    转义次数数字表囗次序字集{len>=2,不重复,用户自定义次序}
    最小转义次数囗字符串 <- 转义次数/-\允空字符串
    def split__iter2iter_seqs(sf,  begin, iterable, /, *, key):
        'Iter a -> (key::a->k) -> (Iter [a]){len>0}'

        def mk_it(begin, key, it, /):
            '-> Iter (i, k, a)'
            for i, a in enumerate(it, begin):
                k = key(a)
                yield i, k, a
            return
        it = iter(iterable); del iterable
        it = PeekableIterator(mk_it(begin, key, it))


#'''

from itertools import combinations
def _():
    lhs = 'IHLT'
    rhs = 'hrty'
    def before(case, a, b, /):
        # a before a
        ia = case.index(a)
        ib = case.index(b)
        return ia < ib
    def pred(case, /):
        if 1:
            # not t before I
            if before(case, 't', 'I'):
                return False
        if 1:
            # not H before h
            if before(case, 'H', 'h'):
                return False
        return True
    def f0_iter_cases():
        def f(idc, /):
            js = [0]*8
            for i in idc:
                js[i] = 1

            iL = 0
            iR = 0
            for j in js:
                if j:
                    yield rhs[iR]
                    iR += 1
                else:
                    yield lhs[iL]
                    iL += 1
        for js in combinations(range(8), 4):
            case = ''.join(f(js))
            if pred(case):
                yield case
    cases = tuple(f0_iter_cases())

    fix_szsL = 'HT'
    fix_szsR = 'ht'
    var_szsL = 'ILX'
    var_szsR = 'ry'
    def mk_ch2kd_(d, left_vs_right, fix_vs_var, s, /):
        for ch in s:
            if ch in d: raise logic-err
            d[ch] = (left_vs_right, fix_vs_var)
    def mk_ch2kd():
        d = {}
        mk_ch2kd_(d, False, False, fix_szsL)
        mk_ch2kd_(d, True, False, fix_szsR)
        mk_ch2kd_(d, False, True, var_szsL)
        mk_ch2kd_(d, True, True, var_szsR)
        return d
    ch2kd = mk_ch2kd()
    def f1_case2splited_sz(case, /):
        #ch2sum = defaultdict(list)
        ch2sum = {ch:[] for ch in 'X'+lhs+rhs}
        def dropable(nm, /):
            return all(ch2kd[ch][1] for ch in nm)
        def f(curr_ls, next_data, /):
            isR, is_var, next_ch = next_data
            if isR:
                def cat(ch, next_ch, /):
                    return ch+next_ch
            else:
                def cat(ch, next_ch, /):
                    return next_ch+ch
            for _, _, ch in curr_ls:
                nm = cat(ch, next_ch)
                if not dropable(nm):
                    ch2sum[ch].append(nm)
                    ch2sum[next_ch].append(nm)
            curr_ls.clear()
            curr_ls.append(data)

        curr_ls = []
        for ch in case+'X':
            isR, is_var = ch2kd[ch]
            data = isR, is_var, ch
            if (not curr_ls) or curr_ls[0][0] is isR:
                curr_ls.append(data)
            else:
                f(curr_ls, data)
        else:
            # [ch2sum[ch] = []] ==>> len==0
            pass
        return dict(ch2sum)

    def solve_at_given_H_T(sz4H, sz4T, /):
        ch2sz = dict(H=sz4H, T=sz4T, h=sz4H, t=sz4T)
        ... ...

    def _t_f0():
        for i, case in enumerate(cases):
            print(i, case)
    def _t_f1():
        for i, case in enumerate(cases):
            print(i, case, f1_case2splited_sz(case))
    #_t_f0()
    _t_f1()
    return

#from collections import defaultdict
_()
r'''
0 hrItyHLT
1 hrItHyLT
2 hrItHLyT
3 hrItHLTy
4 hrIHtyLT
5 hrIHtLyT
6 hrIHtLTy
7 hrIHLtyT
8 hrIHLtTy
9 hrIHLTty
10 hIrtyHLT
11 hIrtHyLT
12 hIrtHLyT
13 hIrtHLTy
14 hIrHtyLT
15 hIrHtLyT
16 hIrHtLTy
17 hIrHLtyT
18 hIrHLtTy
19 hIrHLTty
20 hIHrtyLT
21 hIHrtLyT
22 hIHrtLTy
23 hIHrLtyT
24 hIHrLtTy
25 hIHrLTty
26 hIHLrtyT
27 hIHLrtTy
28 hIHLrTty
29 hIHLTrty
30 IhrtyHLT
31 IhrtHyLT
32 IhrtHLyT
33 IhrtHLTy
34 IhrHtyLT
35 IhrHtLyT
36 IhrHtLTy
37 IhrHLtyT
38 IhrHLtTy
39 IhrHLTty
40 IhHrtyLT
41 IhHrtLyT
42 IhHrtLTy
43 IhHrLtyT
44 IhHrLtTy
45 IhHrLTty
46 IhHLrtyT
47 IhHLrtTy
48 IhHLrTty
49 IhHLTrty
#'''
