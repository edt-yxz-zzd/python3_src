
#[[[__doc__
r'''
e ../../python3_src/seed/recognize/SimplifiedCmdlinePrefixParser.py

SimplifiedCmdlinePrefixParser is a simplified-version of CmdlinePrefixParser

    * has no { } except raw_piece_list
        没有以下功能:
            [顶层]更改命令行解析器关键字配置
            参数包
            函数调用
            解包#解包 参数包
            透明作用域#约束 更改作用域后续环境变量
            额外参数
                包形式的更改作用域后续的环境变量
                包形式的更改下一个参数的环境变量
            ...
    #主要功能有:
    * 预处理:转义,格式化
        预处理任何一个字符串(朴素字符串区间内的除外)
        ^转义
        %格式化
        读取前缀 regex"[%^]*"
            从右向左 依次 进行预处理
        "^%%=%{...}abc"
            1. 切分为 "^%%"  "=%{...}abc"
            2. 转义(格式化(格式化("=%{...}abc")))

    * 子命令
    * 位置参数 缺省
    * 选项参数 缺省
    * 开关 多态
    * 选项参数形式的更改作用域后续的环境变量
        由于没有 包，顶层作用域 是唯一的 作用域
        <==> [顶层]选项参数形式的更改命令行后续的环境变量
        vs 包形式的更改作用域后续的环境变量
        选项参数形式 vs 包形式
            选项参数形式 不含 who 信息！
            包形式 含 who 信息！
    * 字符串参数
    * 张量参数:
        * 普通张量参数
        * 朴素字符串列表
            * 行尾朴素字符串列表
            * 行内内嵌朴素字符串列表
    * 行尾不解析的额外参数
    * 注释:单块注释,行尾注释,行内内嵌注释
    -----
    * 转义字符串
    * 解码转义字节串#原始字符串--[+fmt:decode/unescape/literal_eval]->字节串--[+encoding:decode]->字符串
    * 格式化字符串#引用 环境变量
    * ?查询?
        可选，可能不实现

======示例
    * 预处理:转义,格式化
        预处理的转义前导符 = '^'
        预处理的格式化前导符 = '%'
            #两两相互间 非前缀，非后缀
        ===
        ^转义
        %格式化
    * 子命令
        子命令名的前缀 = '!!!:'
        ===
        !!!:子命令名
    * 位置参数 缺省
        位置参数可省索引的前缀 = '@,:'
        位置参数可省索引的实参为默认值的前缀 = '@,[_]:'
        位置参数可省索引的实参为空的前缀 = '@,[]:'
        ===
        @,:  1参数
            按次序填充
        @,:2  1参数
            第二个参数
        @,[_]:
            默认值
        @,[]:
            Nothing
    * 选项参数 缺省
        #append,extend for list??
        选项名的前缀 = '@:'
        选项名的实参为默认值的前缀 = '@[_]:'
        选项名的实参为空的前缀 = '@[]:'
        ===
        @:选项名  1参数
        @[_]:选项名
            默认值
        @[]:选项名
            Nothing
    * 开关 多态
        开关名的开的偏序大于的前缀 = '?+:'
        开关名的关的偏序小于的前缀 = '?-:'
        开关名的实参为空的偏序无关的前缀 = '?[]:'
        开关名的实参为满的偏序相等的前缀 = '?[..]:'
        开关名的实参为默认值的前缀 = '?[_]:'
        开关名的前缀 = '?:'
        ===
        ?+:开关名
            双态:开
            三态:全序大于/+1
            四态:偏序大于#[偏序大于等于][!偏序小于等于]
        ?-:开关名
            双态:关
            三态:全序小于/-1
            四态:偏序小于#[!偏序大于等于][偏序小于等于]
        ?[]:开关名
            #三态
            Nothing/空
            三态:全序等于/0
            四态:偏序无关#[!偏序大于等于][!偏序小于等于]
        ?[..]:开关名
            #四态
            ALL/满
            四态:偏序相等#[偏序大于等于][偏序小于等于]
        ?[_]:开关名
            默认值
        ?:开关名 1字符串参数
            - +
            < = >
            -1 0 +1
            ~<~ ~<>~ ~>~ ~=~
            [] [_] [..]
            Nothing default ALL
            false true
            False True
            off on
            OFF ON

    * 选项参数形式的更改作用域后续的环境变量
        环境变量名的变量类型为字符串的前缀 = '@%:'
        环境变量名的变量类型为字符串的删除指令的前缀 = '@%[]:'
        ===
        @%:变量名 1字符串参数
        @%[]:变量名
            删除环境变量
    * 字符串参数
        字符串参数的前缀 = '='
        ===
        =字符串
        === ^ % 前缀 并不是 字符串参数 特有的，它们是 预处理
        %=格式化字符串
        ^=转义后的字符串
        ^%=转义后的格式化字符串

    * 张量参数:普通张量参数,行尾朴素字符串列表,行内内嵌朴素字符串列表
        普通张量参数的无标签的首符 = '['
        普通张量参数的带标签的首符的前缀 = '[:'
            ---局部前缀 或 局部符号
            普通张量参数的无标签的尾符 = ']'
            普通张量参数的带标签的尾符的前缀 = ']:'
            普通张量参数的一级分隔符 = ','
            普通张量参数的二级分隔符 = ':'
            普通张量参数的秩的前缀 = '.'
            普通张量参数的秩的维度分隔符 = '.'
            普通张量参数的秩的维度通配符 = '?'
        行尾朴素字符串列表的无标签的首符 = '+++++[]:'
        行内内嵌朴素字符串列表的带标签的首符的前缀 = '+++[:'
            ---局部前缀 或 局部符号
            行内内嵌朴素字符串列表的带标签的尾符的前缀 = '+++]:'
        ===
        #普通张量参数
        #   取消 regex"[,:]\d+"
        #   仅保留 『,』『:』
        [ ]
        [:标签 ]:标签
        [秩:标签 ]:标签
        [ , 1参数 ]
            注意 逗号之后的空格
        [ , 1参数 : 1参数 ]
            注意 冒号之后的空格

        #朴素字符串列表:
        +++++[]: 行尾朴素字符串列表
             字符串数组，是 张量参数 的 特殊形式
        +++[:标签 行内内嵌朴素字符串列表 +++]:标签
             字符串数组，是 张量参数 的 特殊形式
        ####
        [ .?.2.5.?.3 ]
        [:tag .?.2.5.?.3 ]:tag
        [ , =字符串 ]
            [x]
        [ , =字符串 : =字符串 ]
            [[x,y]]
        [ , [ ] : [ ] ]
            [[[],[]]]


    * 行尾不解析的额外参数
        行尾不解析的额外参数的无标签的首符 = '+++++:'
        ===
        #额外参数:
        +++++: 行尾不解析的额外参数
             根本不处理，保留 iterator
        #xxx: +++{:标签 行内内嵌不解析的额外参数 +++}:标签
        #   见上面: 行内内嵌朴素字符串列表
    * 注释:单块注释,行尾注释,行内内嵌注释
        单块注释的前缀 = '---:'
        行尾注释的无标签的首符 = '-----:'
        行内内嵌注释的带标签的首符的前缀 = '---{:'
            ---局部前缀 或 局部符号
            行内内嵌注释的带标签的尾符的前缀 = '---}:'
        ===
        #注释:
        ---{:标签 行内内嵌注释 ---}:标签
        ---:单块注释
        -----: 行尾注释
    ----
    * 转义字符串
        字符串转义序列的前缀的左半符 = '^'
        字符串转义序列的前缀的右半符 = '{'
        字符串转义序列的前缀的转义提升等级表达用的从小到大排列的所有数字符 = tuple('0123456789')
        字符串转义序列的转义方法名与负载的分隔符 = ':'
        #字符串转义序列的负载的切分符 = ','
        #字符串转义序列的负载的所有噪声符 = ('_',)
        字符串转义序列的终止符 = '}'
            #先搜 } 再回头搜 :

        ===
        ^转义字符串
        ---
        ^=abcd^{U:hhhh_hhhh}
        ---串中的转义字符序列
        #   ^{ -> ^0{ -> ^1{ -> ... -> ^9{ -> ^00{ -> ^01{ -> ... -> ^99{ -> ^000{ -> ^001{ -> ...
        #   ^{<escape_case>:<payload>}
        #   ^{U:hhhh_hhhh}
        #   ^{u:hhhh}
        #   ^{x:hh}
        #   ^{U:hhhh_hhhh,hhhh_hhhh}
        #   ^{u:hhhh,hhhh}
        #   ^{x:hh,hh,hh,hh}
    * 解码转义字节串#原始字符串--[+fmt:decode/unescape/literal_eval]->字节串--[+encoding:decode]->字符串
        #   ^{hex%encoding:hh...}

    * 格式化字符串#引用 环境变量
        字符串格式化序列的前缀的左半符 = '%'
        字符串格式化序列的前缀的右半符 = '{'
        字符串格式化序列的前缀的格式化提升等级表达用的从小到大排列的所有数字符 = tuple('0123456789')
        字符串格式化序列的标签的起始符 = '['
        字符串格式化序列的标签的终止符 = ']'
        字符串格式化序列的单次格式化的标示符 = '%'
        字符串格式化序列的可省标签多次格式化标示的附后符 = '/'
        字符串格式化序列的无标签的终止符 = '}/'
        字符串格式化序列的带标签的终止符的前缀 = '}'
        字符串格式化序列的带标签的终止符的后缀 = '/'
            #先搜 }/ 或 }[tag]/ 再回头搜

        ===
        #   %{ -> %0{ -> %1{ -> ... -> %9{ -> %00{ -> %01{ -> ... -> %99{ -> %000{ -> %001{ -> ...
        #注意: %{ - prefix; / or [raw_tag]/ - suffix
        #   并非 %{/ - prefix
        #   %{/<var_name>}/
        #   %{[raw_tag]/<var_name>}[raw_tag]/
        #       #var_name/var_fmt may be weird, so required [raw_tag]
        #   %{[raw_tag]%/<var_name>}[raw_tag]/
        #       firstly, format var_name once
        #   %{[raw_tag]%%/<var_name>}[raw_tag]/
        #       firstly, format var_name twice

        =====取消下面这些复杂的用法var_fmt
        #   %{/<var_name>:/<var_fmt>}/
        #   %{/<var_fmt>:/<recur_embedding_formatted_string4var_fmt>}/
        #   ##var_name/var_fmt may be weird, so required [raw_tag]
        #   %{[raw_tag]/<var_name>:[raw_tag]/<var_fmt>}[raw_tag]/
        #   %{[raw_tag]/<var_name>:[raw_tag]/<recur_embedding_formatted_string4var_fmt>}[raw_tag]/
        ----
        # %3{    #not %3{/
        # %{/xxx:/0>4}/
        # %{[raw_tag]/xxx:[raw_tag]/0>4}[raw_tag]/
        #
        #   %{[raw_tag]%/<var_name>}[raw_tag]/
        #       firstly, format var_name once
        #   %{[raw_tag]%%/<var_name>}[raw_tag]/
        #       firstly, format var_name twice
        #   %{[raw_tag]/<var_name>:[raw_tag]%/var_fmt}[raw_tag]/
        #       firstly, format var_fmt once
        #   %{[raw_tag]/<var_name>:[raw_tag]%%/var_fmt}[raw_tag]/
        #       firstly, format var_fmt twice

    * ?查询?
        可选，可能不实现
        查询的前缀 = '???:'
        ===
        ???:@,:位置参数的索引
        ???:@:选项名
        ???:?:开关名
        ...


======
#[[[收集结果见下面SimplifiedCmdlinePrefixParser其下的 收集上面所列的前缀或符号定义值的结果/局部前缀或局部符号
view others/app/gvim/filter.txt

收集上面所列的前缀或符号定义值，使用gvim如下：
#gvim
yy
    复制行
p
    粘贴行
x
    删除字符
q/
    搜索语句窗口
/\(前缀\|符\)\> =

q:
    命令行窗口
    复制粘贴命令
:filter /\(前缀\|符\)\> =/ :%l
:filter /\(前缀\|符\)\> =/ :%p

:redir @">
  redirect messages to the unnamed register.
:filter /\(前缀\|符\)\> =/ :%l

p
  paste/p unnamed register
:redir END
  end redirecting messages.
ctrl+v
    用于删除行号

#]]]收集结果见下面SimplifiedCmdlinePrefixParser其下的 收集上面所列的前缀或符号定义值的结果/局部前缀或局部符号
#'''
#]]]__doc__

from seed.iters.PeekableIterator import PeekableIterator
from types import MappingProxyType





class SimplifiedCmdlinePrefixParser:
    def __init__(sf, /
        #局部前缀或局部符号 = True
            #[[[收集上面所列的前缀或符号定义值的结果
        ,预处理的转义前导符 = '^'
        ,预处理的格式化前导符 = '%'
        ,子命令名的前缀 = '!!!:'
        ,位置参数可省索引的前缀 = '@,:'
        ,位置参数可省索引的实参为默认值的前缀 = '@,[_]:'
        ,位置参数可省索引的实参为空的前缀 = '@,[]:'
        ,选项名的前缀 = '@:'
        ,选项名的实参为默认值的前缀 = '@[_]:'
        ,选项名的实参为空的前缀 = '@[]:'
        ,开关名的开的偏序大于的前缀 = '?+:'
        ,开关名的关的偏序小于的前缀 = '?-:'
        ,开关名的实参为空的偏序无关的前缀 = '?[]:'
        ,开关名的实参为满的偏序相等的前缀 = '?[..]:'
        ,开关名的实参为默认值的前缀 = '?[_]:'
        ,开关名的前缀 = '?:'
        ,环境变量名的变量类型为字符串的前缀 = '@%:'
        ,环境变量名的变量类型为字符串的删除指令的前缀 = '@%[]:'
        ,字符串参数的前缀 = '='
        ,普通张量参数的无标签的首符 = '['
        ,普通张量参数的带标签的首符的前缀 = '[:'
        #if 局部前缀或局部符号:
        ,    普通张量参数的无标签的尾符 = ']'
        ,    普通张量参数的带标签的尾符的前缀 = ']:'
        ,    普通张量参数的一级分隔符 = ','
        ,    普通张量参数的二级分隔符 = ':'
        ,    普通张量参数的秩的前缀 = '.'
        ,    普通张量参数的秩的维度分隔符 = '.'
        ,    普通张量参数的秩的维度通配符 = '?'
        ,行尾朴素字符串列表的无标签的首符 = '+++++[]:'
        ,行内内嵌朴素字符串列表的带标签的首符的前缀 = '+++[:'
        #if 局部前缀或局部符号:
        ,    行内内嵌朴素字符串列表的带标签的尾符的前缀 = '+++]:'
        ,行尾不解析的额外参数的无标签的首符 = '+++++:'
        ,单块注释的前缀 = '---:'
        ,行尾注释的无标签的首符 = '-----:'
        ,行内内嵌注释的带标签的首符的前缀 = '---{:'
        #if 局部前缀或局部符号:
        ,    行内内嵌注释的带标签的尾符的前缀 = '---}:'
        ,查询的前缀 = '???:'
        ###################################
        ###################################
        #字符串内部
        ,字符串转义序列的前缀的左半符 = '^'
        ,字符串转义序列的前缀的右半符 = '{'
        ,字符串转义序列的前缀的转义提升等级表达用的从小到大排列的所有数字符 = tuple('0123456789')
        ,字符串转义序列的转义方法名与负载的分隔符 = ':'
        ,#字符串转义序列的负载的切分符 = ','
        ,#字符串转义序列的负载的所有噪声符 = ('_',)
        ,字符串转义序列的终止符 = '}'

        ,字符串格式化序列的前缀的左半符 = '%'
        ,字符串格式化序列的前缀的右半符 = '{'
        ,字符串格式化序列的前缀的格式化提升等级表达用的从小到大排列的所有数字符 = tuple('0123456789')
        ,字符串格式化序列的标签的起始符 = '['
        ,字符串格式化序列的标签的终止符 = ']'
        ,字符串格式化序列的单次格式化的标示符 = '%'
        ,字符串格式化序列的可省标签多次格式化标示的附后符 = '/'
        ,字符串格式化序列的无标签的终止符 = '}/'
        ,字符串格式化序列的带标签的终止符的前缀 = '}'
        ,字符串格式化序列的带标签的终止符的后缀 = '/'
            #]]]收集上面所列的前缀或符号定义值的结果
        #del 局部前缀或局部符号
        ):
        d = {**locals()}
        del d['sf']
        sf.__dict__.update(d)
        ... ...





    r'''
    (xxx_info, xxx) = parse_one_xxx(env_view, peekable_iter_pieces)
    ===
    preprocess_piece env piece
    try_skip_one_noise
    skip_noises
    parse_one_atom


    parse_one_comment
    parse_one_noise
        <- parse_one_comment
    parse_one_str_arg
    parse_one_raw_tail_arg
    parse_one_raw_section_arg
    parse_one_tenser_arg
    parse_one_tagged_tenser_arg
    parse_one_untagged_tenser_arg
    parse_tenser_body__exclude_close

    search_toplayer_prefix_info
    parse_one_arg
        (prefix, prefix_info) <- search_toplayer_prefix_info head_piece
        case prefix_info:
            字符串参数的前缀
                -> parse_one_str_arg
            行尾朴素字符串列表的无标签的首符
                -> parse_one_raw_tail_arg
            行内内嵌朴素字符串列表的带标签的首符的前缀
                -> parse_one_raw_section_arg
            普通张量参数的无标签的首符
            普通张量参数的带标签的首符的前缀
                -> parse_one_tenser_arg
                -> parse_one_tagged_tenser_arg
                -> parse_one_untagged_tenser_arg
                -> parse_tenser_body__exclude_close
    parse_many0_noises_and_one_str_arg
    parse_many0_noises_and_one_arg
        loop:
            toplayer_atom <- parse_one_toplayer_atom
            case toplayer_atom:
                噪声 -> append; continue
                参数 -> return
                _ -> error
    parse_one_toplayer_atom
        (prefix, prefix_info) <- search_toplayer_prefix_info head_piece
        case prefix_info:
            #注释 -> parse_one_comment...
            噪声 -> parse_one_noise...
            参数 -> parse_one_arg...
            ###
            单块 -> ...dispatch
            行尾 -> 行尾不解析的额外参数的无标签的首符...
            首符 -> error
    iter_parse_whole_cmdline
        toplayer_atom <- parse_one_toplayer_atom
        case toplayer_atom:
            噪声 -> discard
            参数 -> error
            不需要参数的 -> ...
            需要字符串参数的 ->
                (noise0s, str_arg) <- parse_many0_noises_and_one_str_arg
                ...
            需要参数的 ->
                (noise0s, arg) <- parse_many0_noises_and_one_arg
                ...

    需要字符串参数的:
        ,开关名的前缀 = '?:'
        ,环境变量名的变量类型为字符串的前缀 = '@%:'
    需要参数的:
        ,位置参数可省索引的前缀 = '@,:'
        ,选项名的前缀 = '@:'
    不需要参数的:
        ,子命令名的前缀 = '!!!:'
        ,位置参数可省索引的实参为默认值的前缀 = '@,[_]:'
        ,位置参数可省索引的实参为空的前缀 = '@,[]:'
        ,选项名的实参为默认值的前缀 = '@[_]:'
        ,选项名的实参为空的前缀 = '@[]:'
        ,开关名的开的偏序大于的前缀 = '?+:'
        ,开关名的关的偏序小于的前缀 = '?-:'
        ,开关名的实参为空的偏序无关的前缀 = '?[]:'
        ,开关名的实参为满的偏序相等的前缀 = '?[..]:'
        ,开关名的实参为默认值的前缀 = '?[_]:'
        ,环境变量名的变量类型为字符串的删除指令的前缀 = '@%[]:'
        ,查询的前缀 = '???:'
        ,字符串参数的前缀 = '='
            #参数
        ,单块注释的前缀 = '---:'
            #噪声注释

    行尾:
        ,行尾朴素字符串列表的无标签的首符 = '+++++[]:'
            #参数
        ,行尾不解析的额外参数的无标签的首符 = '+++++:'
            #不处理
        ,行尾注释的无标签的首符 = '-----:'
            #噪声注释

    首符:
        ,普通张量参数的无标签的首符 = '['
            #参数
        ,普通张量参数的带标签的首符的前缀 = '[:'
            #参数
        ,行内内嵌朴素字符串列表的带标签的首符的前缀 = '+++[:'
            #参数
        ,行内内嵌注释的带标签的首符的前缀 = '---{:'
            #噪声注释

    局部前缀或局部符号:
        ,    普通张量参数的无标签的尾符 = ']'
        ,    普通张量参数的带标签的尾符的前缀 = ']:'
        ,    普通张量参数的一级分隔符 = ','
        ,    普通张量参数的二级分隔符 = ':'
        ,    普通张量参数的秩的前缀 = '.'
        ,    普通张量参数的秩的维度分隔符 = '.'
        ,    普通张量参数的秩的维度通配符 = '?'

        ,    行内内嵌朴素字符串列表的带标签的尾符的前缀 = '+++]:'

        ,    行内内嵌注释的带标签的尾符的前缀 = '---}:'
        #'''


    query_info_about_toplayer_atom
        'is噪声?',
        'is参数?',
        'is不需要参数的?',
        'is需要字符串参数的?',
        'is需要参数的?',
        'is环境变量指令?',
    mk_results_from_standalone_toplayer_atom
    mk_results_from_toplayer_atom_with_single_arg
    def mk_env_view(sf, mutable_envs, /):
        env_view = MappingProxyType(mutable_envs)
        return env_view
    def mk_init_mutable_envs(sf, /):
        mutable_envs = {}
        return mutable_envs
    def iter_parse_whole_cmdline(sf, pieces, /):
        '-> Iter<result>'
        peekable_iter_pieces = PeekableIterator(iter(pieces)); del pieces
            #? sf.preprocess_piece
        mutable_envs = sf.mk_init_mutable_envs()
        env_view = sf.mk_env_view(mutable_envs)
        while not (peekable_iter_pieces.is_empty()):
            toplayer_atom = sf.parse_one_toplayer_atom(env_view, peekable_iter_pieces)
            tmay_arg = ()
            if sf.query_info_about_toplayer_atom('is噪声?', toplayer_atom):
                #discard
                results = []
                pass
            elif sf.query_info_about_toplayer_atom('is参数?', toplayer_atom):
                #error
                raise Exception(f'toplayer_atom: naked arg')
            elif sf.query_info_about_toplayer_atom('is不需要参数的?', toplayer_atom):
                results = sf.mk_results_from_standalone_toplayer_atom(toplayer_atom)
            elif sf.query_info_about_toplayer_atom('is需要字符串参数的?', toplayer_atom):
                (noise0s, str_arg) = sf.parse_many0_noises_and_one_str_arg(env_view, peekable_iter_pieces)
                results = sf.mk_results_from_toplayer_atom_with_single_arg(toplayer_atom, str_arg)
                tmay_arg = (str_arg,)
            elif sf.query_info_about_toplayer_atom('is需要参数的?', toplayer_atom):
                (noise0s, arg) = sf.parse_many0_noises_and_one_arg(env_view, peekable_iter_pieces)
                results = sf.mk_results_from_toplayer_atom_with_single_arg(toplayer_atom, arg)
                tmay_arg = (arg,)
            else:
                raise Exception(f'unknown case')
            toplayer_atom
            tmay_arg
            results
            yield from results
            if sf.query_info_about_toplayer_atom('is环境变量指令?', toplayer_atom):
                sf.update_mutable_envs(toplayer_atom, tmay_arg, results)
            #############
            if sf.query_info_about_toplayer_atom('is行尾?', toplayer_atom):
                break
        return
    #end-def iter_parse_whole_cmdline(sf, pieces, /):

    def parse_one_toplayer_atom(sf, env_view, peekable_iter_pieces, /):
        '-> toplayer_atom'
        if peekable_iter_pieces.is_empty():
            raise Exception(f'end_of_input')
        raw_head_piece = peekable_iter_pieces.peek1()
        head_piece = sf.preprocess_piece(env_view, raw_head_piece)
        (prefix, prefix_info) = sf.search_toplayer_prefix_info(head_piece)
        if sf.query_info_about_prefix_info('is噪声?', prefix_info):
            noise = sf.parse_one_noise(env_view, peekable_iter_pieces)
            toplayer_atom = '/噪声/', noise
        elif sf.query_info_about_prefix_info('is参数?', prefix_info):
            arg = sf.parse_one_arg(env_view, peekable_iter_pieces)
            toplayer_atom = '/参数/', arg
        elif sf.query_info_about_prefix_info('is单块?', prefix_info):
            toplayer_atom = sf.parse_one_nonarg_single_piece_toplayer_atom__dispatch(env_view, prefix, prefix_info, head_piece, raw_head_piece)
        elif sf.query_info_about_prefix_info('is行尾?', prefix_info):
            if not sf.query_info_about_prefix_info('is行尾不解析的额外参数的无标签的首符?', prefix_info): raise logic-err
            #toplayer_atom = sf.parse_one_toplayer_atom__行尾不解析的额外参数的无标签的首符(env_view, peekable_iter_pieces)
            #iter_raw_tail_args = sf.parse_行尾不解析的额外参数(env_view, peekable_iter_pieces)
            peekable_iter_pieces.read1()
            iter_raw_tail_args = peekable_iter_pieces
            toplayer_atom = '/行尾/', iter_raw_tail_args
        elif sf.query_info_about_prefix_info('is首符?', prefix_info): raise logic-err
        else:
            raise Exception(f'unknown case')
        toplayer_atom
        return toplayer_atom
    #end-def parse_one_toplayer_atom(sf, env_view, peekable_iter_pieces, /):



    parse_many0_noises_and_one_str_arg
    parse_many0_noises_and_one_arg
        loop:
            toplayer_atom <- parse_one_toplayer_atom
            case toplayer_atom:
                噪声 -> append; continue
                参数 -> return
                _ -> error

