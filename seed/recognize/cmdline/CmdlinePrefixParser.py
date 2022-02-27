r'''[[[
seed.recognize.CmdlinePrefixParser
debug_pym seed.recognize.CmdlinePrefixParser
py -m seed.recognize.CmdlinePrefixParser

抽象化:
    如何解析？重置前缀？带状态解析？

    输入:
        pieces :: [str]
    inout:
        #解析过程中 可能重置
        lsymbol2rule_tpl :: {lsymbol:rule_tpl}
        rsymbol2prefix_or_str
            # prefix_or_str = '<{prefix}' | '={str}'
        state #隐参数命名空间
    输出:
        (new_state, tmay lsymbol2rule_tpl, tmay rsymbol2prefix_or_str) = yield piece, (xsymbol, state, args)

    ###########################
    单 piece 内部的解析
    parse(fmt="x?y", s)
        ==>> s2 = on_x(may x, s-may x)
        ==>> parse(fmt="y", s2)
            ==>> s3 = on_y(y, s2-y)
    ###########################
        #rule_tpl is func, input is parse_state/rule_tpl/uint/..., output is str/rsymbol/choice/chain/...
        #choice: unparsed_end_by = .*? end_tag ==>> search end_tag first then parse the skipped unparsed middle section
        #choice: parsed_end_by = loop_body{0,?} end_tag ==>> loop_body 与 end_tag 互斥
        #choice: 互斥并联
        #chain: 非空串联
        #局部噪声:如 数字字面值中的『_』
重做！
    前缀！不得使用 中间分隔符！无需对负载字符串作任何假设约束！
        类似python的fr""，区分 是否引用变量 是否使用转义字符 是否解码字节串（需要 编码名）
            这些 字符串 相关前缀 作用于 任何其他前缀之前！
        带负载的前缀 不得是 其他前缀的 前缀 或 ？后缀？
            #不带负载的前缀 不得等于 其他前缀
        带格式字符串中的特殊分割符？
    行内内嵌注释？行尾注释？括号内尾部注释？
        #注释:
        ---{:tag 行内内嵌注释 ---}:tag
        ---:单块注释
        -----: 行尾注释
        #额外参数:
        +++++: 行尾不解析的额外参数
             根本不处理，保留 iterator
        #xxx: +++{:tag 行内内嵌不解析的额外参数 +++}:tag
        #朴素字符串列表:
        +++++[]: 行尾朴素字符串列表
             字符串数组，是 张量参数 的 特殊形式
        +++[:tag 行内内嵌朴素字符串列表 +++]:tag
             字符串数组，是 张量参数 的 特殊形式
    参数
        * 字符串
        * 张量 [ ... ]
          , <==> 1,
            由外而内
          : <==> 1:
            由内而外
          [ ,参数 ,参数 ...]
            [ .? ,参数 ,参数 ...]
            [:tag .? ,参数 ,参数 ...]:tag
            [.?][ ,参数 ,参数 ...]
            [.?][:tag ,参数 ,参数 ...]:tag
            [.?][ ,1参数 ,1参数 ...]
            [.?][ :1参数 :1参数 ...]
            #array<?>
          [ .?.3 ,参数 :参数 :参数  ,参数 :参数 :参数 ... ]
            [.?.3][ ,参数 :参数 :参数  ,参数 :参数 :参数 ... ]
            [.?.3][ ,1参数 :1参数 :1参数  ,1参数 :1参数 :1参数 ... ]
            [.?.3][ ,1参数 ,2参数 ,2参数  ,1参数 ,2参数 ,2参数 ... ]
            [.?.3][ :2参数 :1参数 :1参数  :2参数 :1参数 :1参数 ... ]
            #matrix<?,3>
            [.?.3][ ,参数 :1参数 :1参数  ,参数 :1参数 :1参数 ... ]
            [.?.3][ :2参数 :1参数 :1参数  :2参数 :1参数 :1参数 ... ]
          [ .?.3.2 :3参数 :1参数 :2参数 :1参数  :2参数 :1参数 :3参数 :1参数 :2参数 :1参数  :2参数 :1参数 :3参数 :1参数 :2参数 :1参数  :2参数 :1参数 ... ]
            [.?.3.2][ :3参数 :1参数 :2参数 :1参数  :2参数 :1参数 :3参数 :1参数 :2参数 :1参数  :2参数 :1参数 :3参数 :1参数 :2参数 :1参数  :2参数 :1参数 ... ]
            #tensor<?,3,2>

        * 参数包 { ... }
        ===
        each piece preprocess? eval or not??
            {:tag !...:tag 求值区 ^%...: 预处理区 =...:tag 字面值区 !1:tag atom_to_be_evalued +1:tag atom_to_be_preprocessed =1: piece_literal }:tag
                # unparsed_pieces_grouo 必须 tagged
                #   保留 suffix ":tag" 的所有 piece_literal/unparsed_piece，再根据open对其前缀含义进行解读，这些 前缀 不加入 全局前缀
                #   即 先解读后缀，若匹配，再解读局部含义的前缀
                # close 其实也一样！先后缀再前缀，如果 open 前冠 预处理符，则 我们 有了两个东西: tag_literal_as_suffix, tag_value_to_match，close 必须使用相同 的 字面值 作为后缀 以识别其特殊含义（而非负载piece_literal），同时 要求 预处理后的tag与open的tag_value_to_match相同，故而 close 与 open 需冠以相同 预处理符
        ===
        区分:
            {{<header>:tag piece_literal_not_to_be_preprocess* }}:tag
                tag必需
            {<header>:tag piece_to_be_preprocess* }:tag
                {<header> piece_to_be_preprocess* }
                tag可有可无
        ===
        tagged?
            [:tag ]:tag
            {:tag }:tag
            ===
            表达式括号
                {():tag expr }:tag
            ===
            调用函数？
                {!:tag !:func ... }:tag
                {!:tag @@:who !:func ... }:tag
                命令行解析器内建+命令行程序内建+终端用户自定义组合器+脚本？
                如何 解包 参数包？
                    可能 返回值 是 参数包
                    {{}=:tag expr }:tag
            多元运算符
                类似python的(x if y else z)
                * 1:
                    ===
                    {!:tag !:head ...
                    head may be ''
                    ===
                    }{/:tag /:middle ...
                    middle may be ''
                    ===
                    }{.:tag .:end }
                    }{/.:tag /.:last ... }
                    end may be ''
                    last may be ''
                    ===
                    but head middle* (end|last) 至少一个不为空
                ===
                ===
                * 2:
                    {!:tag !:head ... /:middle ... }:tag
                    {!:tag !:head ... /:middle ... .:end }:tag
                    {!:tag !:head ... /:middle ... /.:last ... }:tag
                    head may be ''
                    middle may be ''
        ===
        额外参数:{%:tag @@:who @:kw =arg ... }:tag affected_arg
            命令行解析器自用 vs 命令行解析器使用者/命令行程序自用 vs 命令行使用者/终端用户自用
            #3个 参数传入的目标对象，但也可能有更多层，需要 系统性命名、自荐空间限定名、重命名...
            * 命令行解析器自用:
                * 如上面 编码名
                    局部设置，也可设置全行默认值
                * 更换整套命令行解析前缀集合
                    注意[0-9]！
                * 设置更换默认值
                * 设置局部变量%{var}
                    选项参数形式 vs 包形式
                        选项参数形式 不含 who 信息！
                        包形式 含 who 信息！
                * 更换选项名kw
                * 更换目标对象名who
            * 命令行程序自用
            * 终端用户自用:
                如：C++ 宏定义
                    终端用户/命令行使用者 是 C++编译器使用者
                    命令行程序/命令行解析器使用者 是 C++编译器作者
        ===
        透明作用域 用于 约束 环境变量
            配合此功能『更改当前作用域后续部分的局部环境变量』
            透明作用域 会自动解包，但 内部 更改的环境变量 无法逸出。
            {===:tag ... }:tag

    子命令
        !!!:subcmd
    选项-必是 单参数
    开关-双态/三态/四态
    是否可缺省？
        默认值 可字符串化？
            直接编码于定义中
        不可，则tmay
    查询？
        列出、过滤 选项
        查询选项 帮助内容、默认值 等。。。
    位置参数？
    类似python的kwargs？用户自定义？
    设置局部变量？如何引用？
        顺序递增变量: 每次引用自动迭代
$ py -m nn_ns.app.args , ] [ , } { .  @ / - _ + = ? ! : % ^
['/sdcard/0my_files/git_repos/python3_src/nn_ns/app/args.py', ',', ']', '[', ',', '}', '{', '.', '@', '/', '-', '_', '+', '=', '?', '!', ':', '%', '^']
$ py -m nn_ns.app.args # vvb                 ['/sdcard/0my_files/git_repos/python3_src/nn_ns/app/args.py']
特殊含义:
    ; 结束命令
    ~ $home/
    # 行尾注释
    $ 宏，参数
    & logic-and
    * fsys-glob-expand-into-args
    () call? 宏函数调用？
    <> io-file
    | pipe-chain-cmd
    \ 转义+行末续行
    '"` 字符串

$ py -m nn_ns.app.args ;
['/sdcard/0my_files/git_repos/python3_src/nn_ns/app/args.py']
$ py -m nn_ns.app.args )
-bash: syntax error near unexpected token `)'
$ py -m nn_ns.app.args (
-bash: syntax error near unexpected token `('
$ py -m nn_ns.app.args ( )
-bash: syntax error near unexpected token `('
$


=======此前的设计:
    前缀:
      @选项 #后接一个参数
        @选项前缀-选项负载-选项负载... #复杂选项名 只定义前缀
      { 他命令选项转发 } #选项 需要 复杂的参数，比如 转发给 所依赖的命令
      !子命令
      ?查询
      +打开开关
      -关闭开关
      ？参数？
        #vs py::str-literal::fr''==>>引用变量？字符转义？:
        =单参数 #无需转义 raw_string
        ^=转义单参数 # ^{Uxxxx_xxxx}
        ？变量定义与引用？
          ？定义？
            ？let...in？where？
            %{xxx} =单参数
            %{xxx} %=模版单参数
          ？引用？
            %=模版单参数 vs =单参数
            %,模版单参数 vs ,单参数
            %:模版单参数 vs :单参数
          ？模版单参数？
            %% ==>> %
            %{xxx} ==>> 引用
        ？多参数？
          , <==> 1,
            由外而内
          : <==> 1:
            由内而外
          [ ,参数 ,参数 ...]
            [?][ ,参数 ,参数 ...]
            [?][ 1,参数 1,参数 ...]
            [?][ 1:参数 1:参数 ...]
            #array<?>



#]]]'''



from seed.abc.abc import ABC, abstractmethod, override, not_implemented, ABCMeta
from types import MappingProxyType

from seed.iters.PeekableIterator import PeekableIterator
class I:
    r'''
    3个因素影响解析结果:
        * 有2个因素影响解析过程:
            * env 环境变量
                mutable_envs
                env_view
            * cmdline_keyword_setting
                #info_required_by_parse_process
                #may_info_required_by_parse_process
                #reconfig
                #mk_new_toplayer_cmdline_parser_by_reconfig_cmdline_keyword_setting
                只能是用toplayer_only_atom进行设置，此atom本身的解析不受新设置影响。
                    为何不能是inbox?
                        因为close不知该采用旧配置还是新配置。
                    为何不能是raw_tail?
                        其实差不多一个意思，只不过还在可控范围内。
        * 加上另一因素，共3个因素影响解析结果:
            * result_fmt_control
                #results
                此变量为用户自定义，为了不改变解析过程，前两个因素的影响必须反应于results之外，即为mutable_envs+may_new_sf

    #'''
    #################################
    #################################
    #################################
    r'''[自顶向下搜索所需成员函数
=====[[[ /sf[.] @iter_parse_whole_cmdline()
    def iter_parse_whole_cmdline(cls, sf, result_fmt_control, pieces, /):
        mutable_envs = sf.mk_init_mutable_envs()
            is_halt, may_new_sf, results = sf.parse_one_toplayer_atom(result_fmt_control, mutable_envs, iter_pieces)
=====]]]
    #]'''
    @classmethod
    def iter_parse_whole_cmdline(cls, sf, result_fmt_control, pieces, /):
        iter_pieces = PeekableIterator(iter(pieces))
            #? sf.preprocess_piece
        is_halt = False
        mutable_envs = sf.mk_init_mutable_envs()
        while not (is_halt or iter_pieces.is_empty()):
            is_halt, may_new_sf, may_info_required_by_parse_process, results = sf.parse_one_toplayer_atom(result_fmt_control, mutable_envs, iter_pieces)
            if may_new_sf is not None:
                sf = may_new_sf
            yield from results
    r'''[自顶向下搜索所需成员函数
=====[[[ /sf[.] @parse_one_toplayer_atom()
=====]]]
    #]'''
    def parse_one_toplayer_atom(sf, result_fmt_control, mutable_envs, iter_pieces, /):
        r'''-> (is_halt, may_new_sf, may_info_required_by_parse_process, results)
        if curr_toplayer_atom reconfig cmdline_keyword_setting, we need a new parser
        is_halt: whether  meet raw_tail or eof/end_of_input
        results:
            comment ==>> []
            unpack ==>> many0
        #'''
        ... ...
        (case, payload, iter_remain_pieces) = sf.parse_one_atom(result_fmt_control, mutable_envs, iter_pieces)
        if case == 'one_atom':
            (head_indicator_or_prefix, head_mark, head_piece_info, may_info_required_by_parse_process, results) = payload
            if sf.piece_info_query__case_is_inbox_only_atom(head_piece_info):
                #inbox_only_atom
                raise Exception(f'expected toplayer_atom but meet inbox_only_atom: (head_indicator_or_prefix, head_mark, head_piece_info)={(head_indicator_or_prefix, head_mark, head_piece_info)!r}')
            elif sf.piece_info_query__case_is_toplayer_only_atom(head_piece_info):
                # toplayer_only_atom
                pass
            elif sf.piece_info_query__case_is_universal_atom(head_piece_info):
                # universal_atom
                pass
            else:
                raise Exception(f'unknown_head_piece_info:not(toplayer_only | universal | inbox_only):head_piece_info={head_piece_info!r}')

            if sf.piece_info_query__case_is_reconfig_cmdline_keyword_setting_atom(head_piece_info):
                #reconfig_cmdline_keyword_setting_atom
                if may_info_required_by_parse_process is None:
                    raise Exception(f'reconfig_cmdline_keyword_setting_atom but may_info_required_by_parse_process is None')
                info_required_by_parse_process = may_info_required_by_parse_process
                cmdline_keyword_setting_info = sf.extract_cmdline_keyword_setting_info(info_required_by_parse_process)
                new_sf = sf.mk_new_toplayer_cmdline_parser_by_reconfig_cmdline_keyword_setting(cmdline_keyword_setting_info)
                ... ...
            else:
                ... ...


    r'''[自顶向下搜索所需成员函数
=====[[[ /sf[.] @parse_one_atom()
    def parse_one_atom(sf, result_fmt_control, mutable_envs, iter_pieces, /):
        env_view = sf.mk_env_view(mutable_envs)
            piece_value = sf.preprocess_piece(env_view, piece_literal)
            smay_indicator_or_prefix = sf.bisearch_indicator_or_prefix_for_piece_value__exclude_close(piece_value)
            #piece_case_info = sf.get_piece_case_info(indicator_or_prefix)
            piece_info = sf.mk_piece_info(indicator_or_prefix, piece_value, piece_literal)
            if sf.piece_info_query__case_is_open_piece(piece_info):
                if sf.open_piece_info_query__case_body_is_raw_section(open_piece_info):
                    may_info_required_by_parse_process, results = sf.mk_results_from_raw_section(
                        result_fmt_control
                        ,raw_section_open_piece_info
                        ,indicator_or_prefix
                        ,open_mark
                        ,leading_raw_pieces
                        ,local_mark_raw_pieces_pairs
                        ,close_mark
                        )
                    nonraw_section_parser_engine = sf.mk_nonraw_section_parser_engine(nonraw_section_open_piece_info)
                        sf.push_mutable_envs_on_enter_scope(mutable_envs)
                        body_result, may_next_piece_mark, it = sf.parse_nonraw_section_body_only___exclude_close(mutable_envs, nonraw_section_parser_engine, it)
                            #recur:parse_one_atom
                        sf.pop_mutable_envs_on_exit_scope(mutable_envs)
                    may_info_required_by_parse_process, results = sf.mk_results_from_nonraw_section(
                        result_fmt_control
                        ,nonraw_section_open_piece_info
                        ,indicator_or_prefix
                        ,open_mark
                        ,body_result
                        ,close_mark
                        )
            elif sf.piece_info_query__case_is_single_piece_atom(piece_info):
                single_piece_atom_result = sf.parse_single_piece_atom(single_piece_atom_info, piece_value, piece_literal)
                may_info_required_by_parse_process, results = sf.mk_results_from_single_piece_atom(
                    result_fmt_control
                    ,single_piece_atom_info
                    ,single_piece_atom_mark
                    ,single_piece_atom_result
                    )
            elif sf.piece_info_query__case_is_raw_tail_head(piece_info):
                may_info_required_by_parse_process, results = sf.mk_results_from_single_piece_atom(
                    result_fmt_control
                    ,raw_tail_head_piece_info
                    ,raw_tail_head_piece_mark
                    ,iter_raw_tail_iteral_pieces
                    )
=====]]]
    #]'''
    def parse_one_atom(sf, result_fmt_control, mutable_envs, iter_pieces, /):
        r'''
        :: result_fmt_control -> mutable_envs -> Iter<piece_literal::str> -> (case, payload, iter_remain_pieces)
        output:
            #(case, payload, iter_remain_pieces)
            * ('end_of_input', None, iter_remain_pieces)
            * ('unknown_piece', head_mark, iter_remain_pieces)
            * ('one_atom', (head_indicator_or_prefix, head_mark, head_piece_info, may_info_required_by_parse_process, results), iter_remain_pieces)
        #'''
        #end_of_input?
        #preprocess_piece + bisearch indicator or prefix
        #open? tag? if body is raw then search close first else recur parse
        #close? tag==?
        #???update mutable_envs #No!!!
        it = iter(iter_pieces); del iter_pieces
        env_view = sf.mk_env_view(mutable_envs)
        #def recur(it):
        if 1:
            for piece_literal in it:
                break
            else:
                return 'end_of_input', None, it

            piece_value = sf.preprocess_piece(env_view, piece_literal)
            smay_indicator_or_prefix = sf.bisearch_indicator_or_prefix_for_piece_value__exclude_close(piece_value)
            if not smay_indicator_or_prefix:
                # outer scope try to detect close
                head_mark = (piece_value, piece_literal)
                return 'unknown_piece', head_mark, it
                raise Exception(f'no indicator-or-prefix match: piece_value={piece_value!r} = preprocess_piece(piece_literal={piece_literal!r})')
            indicator_or_prefix = smay_indicator_or_prefix
            assert indicator_or_prefix
            assert piece_value.startswith(indicator_or_prefix)
            #piece_case_info = sf.get_piece_case_info(indicator_or_prefix)
            piece_info = sf.mk_piece_info(indicator_or_prefix, piece_value, piece_literal)
            if 1:
                head_indicator_or_prefix = indicator_or_prefix
                head_mark = (piece_value, piece_literal)
                head_piece_info = piece_info
            #if piece_info.case_is_open_piece:
            if sf.piece_info_query__case_is_open_piece(piece_info):
                open_piece_info = piece_info; del piece_info
                indicator_or_prefix
                open_mark = (piece_value, piece_literal)
                #if open_piece_info.case_body_is_raw_section:
                if sf.open_piece_info_query__case_body_is_raw_section(open_piece_info):
                    raw_section_open_piece_info = open_piece_info; del open_piece_info
                    assert raw_section_open_piece_info.is_tagged
                    literal_suffix = raw_section_open_piece_info.tag_literal_as_suffix
                    tag_value = raw_section_open_piece_info.tag_value_to_match
                    leading_raw_pieces = []
                    local_mark_raw_pieces_pairs = []
                        # [(local_mark, [raw_piece])]
                    curr_raw_pieces = leading_raw_pieces
                    for piece_literal in it:
                        if piece_literal.endswith(literal_suffix):
                            piece_value = sf.preprocess_piece(env_view, piece_literal)
                            if not piece_value.endswith(tag_value): raise Exception(f'not piece_value.endswith(tag_value): tag_value={tag_value!r}; piece_value={piece_value!r} = preprocess_piece(piece_literal={piece_literal!r})')
                            if raw_section_open_piece_info.is_close_piece(piece_value, piece_literal):
                                close_mark = (piece_value, piece_literal)
                                leading_raw_pieces
                                local_mark_raw_pieces_pairs
                                break
                            local_mark_literal = piece_literal
                            local_mark_value = piece_value
                            local_mark = (local_mark_value, local_mark_literal)
                            curr_raw_pieces = []
                            local_mark_raw_pieces_pairs.append((local_mark, curr_raw_pieces))
                        else:
                            curr_raw_pieces.append(piece_literal)
                    else:
                        raise Exception(f'end_of_input: piece open {indicator_or_prefix!r} without close')
                    raw_section_open_piece_info
                    indicator_or_prefix
                    open_mark
                    leading_raw_pieces
                    local_mark_raw_pieces_pairs
                    close_mark
                    may_info_required_by_parse_process, results = sf.mk_results_from_raw_section(
                        result_fmt_control
                        ,raw_section_open_piece_info
                        ,indicator_or_prefix
                        ,open_mark
                        ,leading_raw_pieces
                        ,local_mark_raw_pieces_pairs
                        ,close_mark
                        )
                else:
                    # not open_piece_info.case_body_is_raw_section
                    # not sf.open_piece_info_query__case_body_is_raw_section(open_piece_info)
                    nonraw_section_open_piece_info = open_piece_info; del open_piece_info
                    nonraw_section_parser_engine = sf.mk_nonraw_section_parser_engine(nonraw_section_open_piece_info)
                    #assert sf is nonraw_section_open_piece_info.get_background_parser()
                    if 1:
                        #mutable_envs push pop
                        sf.push_mutable_envs_on_enter_scope(mutable_envs)
                        body_result, may_next_piece_mark, it = sf.parse_nonraw_section_body_only___exclude_close(mutable_envs, nonraw_section_parser_engine, it)
                            #recur:parse_one_atom
                        sf.pop_mutable_envs_on_exit_scope(mutable_envs)
                    if may_next_piece_mark is None:
                        raise Exception(f'end_of_input: piece open {indicator_or_prefix!r} without close')
                    (piece_value__via_inner_env, piece_literal) = may_next_piece_mark
                    #到底该用内部还是外部的环境变量？
                    #用外部的环境变量重新预处理（转义+格式化）
                    piece_value__via_outer_env = sf.preprocess_piece(env_view, piece_literal)
                    piece_value = piece_value__via_outer_env
                    if not nonraw_section_open_piece_info.is_close_piece(piece_value, piece_literal):
                        raise Exception(f'unknown case: piece open {indicator_or_prefix!r}: meet unexpected piece: piece_value={piece_value!r} = preprocess_piece(piece_literal={piece_literal!r})')
                    close_mark = (piece_value, piece_literal)
                    ###################
                    nonraw_section_open_piece_info
                    indicator_or_prefix
                    open_mark
                    body_result
                    close_mark
                    may_info_required_by_parse_process, results = sf.mk_results_from_nonraw_section(
                        result_fmt_control
                        ,nonraw_section_open_piece_info
                        ,indicator_or_prefix
                        ,open_mark
                        ,body_result
                        ,close_mark
                        )
            #elif piece_info.case_is_single_piece_atom:
            elif sf.piece_info_query__case_is_single_piece_atom(piece_info):
                #single_piece_atom
                single_piece_atom_info = piece_info; del piece_info
                single_piece_atom_mark = (piece_value, piece_literal)
                single_piece_atom_result = sf.parse_single_piece_atom(single_piece_atom_info, piece_value, piece_literal)
                #########
                single_piece_atom_info
                single_piece_atom_mark
                single_piece_atom_result
                may_info_required_by_parse_process, results = sf.mk_results_from_single_piece_atom(
                    result_fmt_control
                    ,single_piece_atom_info
                    ,single_piece_atom_mark
                    ,single_piece_atom_result
                    )
            #elif piece_info.case_is_raw_tail_head:
            elif sf.piece_info_query__case_is_raw_tail_head(piece_info):
                # raw_tail
                raw_tail_head_piece_info = piece_info; del piece_info
                raw_tail_head_piece_mark = (piece_value, piece_literal)
                iter_raw_tail_iteral_pieces = it
                #raw_tail_body_literal_pieces = tuple(it)
                raw_tail_head_piece_info
                raw_tail_head_piece_mark
                iter_raw_tail_iteral_pieces
                may_info_required_by_parse_process, results = sf.mk_results_from_single_piece_atom(
                    result_fmt_control
                    ,raw_tail_head_piece_info
                    ,raw_tail_head_piece_mark
                    ,iter_raw_tail_iteral_pieces
                    )
            else:
                #not (open/single/tail)
                raise Exception(f'unknown_piece_info:not (open/single/tail): piece_info={piece_info!r}; indicator_or_prefix={indicator_or_prefix!r}; piece_value={piece_value!r} = preprocess_piece(piece_literal={piece_literal!r})')
            if 1:
                may_info_required_by_parse_process, results
                head_indicator_or_prefix
                head_mark
                head_piece_info
            return ('one_atom', (head_indicator_or_prefix, head_mark, head_piece_info, may_info_required_by_parse_process, results), iter_remain_pieces)
            return 'one_atom', results, it

    #end-def parse_one_atom(sf, result_fmt_control, mutable_envs, iter_pieces, /):
    r'''
    def parse_one_piece(sf, piece:str):
        pass
    def parse_one_atom(sf, iter_pieces):
        #{ group }
        #kw =arg
        #scoped_args ...
        #local_args =arg
        ...
        pass
    #'''
    def preprocess_piece(sf, env_view, piece, /):
        'env -> (unparsed_piece/piece_literal ::str) -> (parsed_piece/piece_value ::str) #format(unescape(unparsed_piece))'
    def mk_env_view(sf, mutable_envs, /):
        'mutable_envs -> env_view'
    def mk_init_mutable_envs(sf, /):
        '-> mutable_envs'
class ICmdlinePrefixParser(ABC):
    r'''
    cmd_line = pieces = unparsed_pieces :: [str]
        #see below:whole_toplayer_cmd_args0
    parsed_piece = handle_may_escaped_formatted_prefix(unparsed_piece)
        # '[^]?%?'

    # universal == (toplayer /\ inbox)
    # toplayer_only | universal | inbox_only
    toplayer_atom = universal_atom | toplayer_reconig_group | raw_tail
    universal_atom = universal_group | tensor_arg | universal_single_piece_atom

    universal_single_piece_atom = str_arg | option | switch | positional_argument_indicator | enduser_defined_positional_argument_indicator | enduser_defined_option | enduser_defined_switch | subcommand | query
        # not include: single_piece_comment
        #   omit from rule as noise
        # consider unparsed_piece only
        #   ie. omit '[^]?%?' prefix
        | str_arg = '=.*'
        | option = '@:.*'
        | option_using_default = '@\[_]:.*'
        | option_using_Nothing = '@\[]:.*'
        | switch = '[?][-+]:.*'
            ===to add:
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
        | switch_using_default = '[?]\[_]:.*'
        | switch3_using_Nothing = '[?]\[]:.*'
        | switch4_using_ALL = '[?]\[\.\.]:.*'

        | positional_argument_indicator = '@,'
        | positional_argument_using_default_indicator = '@,\[_]'
        | positional_argument_using_Nothing_indicator = '@,[]'
        | enduser_defined_positional_argument_indicator = '//@,'
        | enduser_defined_positional_argument_using_default_indicator = '//@,\[_]'
        | enduser_defined_positional_argument_using_Nothing_indicator = '//@,[]'

        | enduser_defined_option = '//@:.*'
        | enduser_defined_option_using_default = '//@\[_]:.*'
        | enduser_defined_option_using_Nothing = '//@\[]:.*'
        | enduser_defined_switch = '//[?][-+]:.*'
        | enduser_defined_switch_using_default = '//[?]\[_]:.*'
        | enduser_defined_switch3_using_Nothing = '//[?]\[]:.*'
        | enduser_defined_switch4_using_ALL = '//[?]\[\.\.]:.*'

        | subcommand = '!!!:.*'
        | query = '???:.*'

    raw_tail = line_tail_comment | line_tail_unparsed_arguments
        # omit '[^]?%?' prefix in indicator
        | line_tail_comment = '-----:'  unparsed_piece*
        | line_tail_unparsed_arguments = '+++++:'  unparsed_piece*

    inline_comment = single_piece_comment | comment_group
        | single_piece_comment = '---:.*'
        | comment_group = '---{:(?P<tag>.*)' unparsed_piece* '}:(?P=tag)'
    # below omit rule noise: inline_comment
    # below omit '[^]?%?' prefix in indicator
    tensor_arg = untagged_tensor_arg | tagged_tensor_arg
    untagged_tensor_arg = '[' tensor_body ']'
    tagged_tensor_arg = '[:.*' tensor_body ']:.*'
    tensor_body = tensor_dimensions? sublevel_tensor*
    sublevel_tensor = levelled_separator  arg
        # now using ', =...' instead of ',=...'
        #sublevel_tensor = levelled_separator <NO_SPACE> arg
    levelled_separator = '[,:]\d*'
    arg = single_atom_arg | multi_atom_arg
    single_atom_arg = str_arg | tensor_arg | grouped_arg
    multi_atom_arg = local_environment+ single_atom_arg

    grouped_arg<tagged> = argument_box<tagged> | call_group<tagged> | expr_group<tagged>

    universal_group<tagged> = grouped_arg<tagged> | unpack_group<tagged> | local_environment<tagged> | scoped_environment<tagged> | transparent_scope<tagged>
        # not include: comment_group
        #   omit from rule as noise
        # not include: toplayer_reconig_group
        #   top-layer-only(toplayer_only), cannot be used inside box/group (inbox)
        ##################
        ##################is-arg
        | argument_box<tagged> = '{(?P<may_tag>(?(tagged):.*|))' argument_box_body '}(?P=may_tag)'
        | call_group<tagged> = '{!(?P<may_tag>(?(tagged):.*|))'  call_header call_body '}(?P=may_tag)'
        | expr_group<tagged> = '{\(\)(?P<may_tag>(?(tagged):.*|))'  arg  '}(?P=may_tag)'
        ##################non-arg
        | unpack_group<tagged> = '{{}=(?P<may_tag>(?(tagged):.*|))' unpack_group_body '}(?P=may_tag)'
        | local_environment<tagged> = '{%(?P<may_tag>(?(tagged):.*|))' environment_header environment_body '}(?P=may_tag)'
        | scoped_environment<tagged> = '{%%%(?P<may_tag>(?(tagged):.*|))' environment_header environment_body '}(?P=may_tag)'
        | transparent_scope<tagged> = '{===(?P<may_tag>(?(tagged):.*|))' transparent_scope_body '}(?P=may_tag)'
    transparent_scope_body = inbox_atom*
    argument_box_body = piece_literal_or_suffixed_tagged_local_mark*    #inbox_atom*
    unpack_group_body = arg*  #expected actual arg be argument_box, may be result of call; if str_arg then unbox the str inline; if tensor_arg, unbox as positional_arguments, insert necessary positional_argument_indicator
    call_header = '!:.*'
    call_body = with_middle_op* with_close_op_?
    with_middle_op = args0 middle_op
    with_close_op_ = args0 close_op_
    close_op_ = end_op | last_op args0
    middle_op = '/:.*'
    end_op = '[.]:.*'
    last_op = '/[.]:.*'
    args0 = cmd_arg_span*

    environment_header = '@@:.*'
    environment_body = args0
    inbox_atom = universal_atom | inbox_only_atom
    inbox_only_atom = call_header | middle_op | end_op | last_op | environment_header

    toplayer_reconig_group<tagged> = '{%%%%%(?P<may_tag>(?(tagged):.*|))' environment_body '}(?P=may_tag)'
        # no "who": environment_header

    whole_toplayer_cmd_args0 = (cmd_arg_span | toplayer_reconig_group)* raw_tail?
    #[[[cmd_arg_span
    cmd_arg_span = span_kw_arg | span_sw_arg | span_i_arg | usr_span_kw_arg | usr_span_sw_arg | usr_span_i_arg | subcommand | query
        # all be universal_atom
        | span_kw_arg = option_1 arg | option_0
        | span_sw_arg = switch_0
        | span_i_arg = position_i_1 arg | position_i_0
        | usr_span_kw_arg = u_option_1 arg | u_option_0
        | usr_span_sw_arg = u_switch_0
        | usr_span_i_arg = u_position_i_1 arg | u_position_i_0
        ######################
            | option_1 = option
            | position_i_1 = positional_argument_indicator
            | option_0 = option_using_default | option_using_Nothing
            | switch_0 = switch | switch_using_default | switch3_using_Nothing | switch4_using_ALL
            | position_i_0 = positional_argument_using_default_indicator | positional_argument_using_Nothing_indicator
            #
            | u_option_1 = enduser_defined_option
            | u_position_i_1 = enduser_defined_positional_argument_indicator
            | u_option_0 = enduser_defined_option_using_default | enduser_defined_option_using_Nothing
            | u_switch_0 = enduser_defined_switch | enduser_defined_switch_using_default | enduser_defined_switch3_using_Nothing | enduser_defined_switch4_using_ALL
            | u_position_i_0 = enduser_defined_positional_argument_using_default_indicator | enduser_defined_positional_argument_using_Nothing_indicator
            ##
    #]]]cmd_arg_span
    #'''
    #prefix_names =
    #default_name2prefix =
    cmdline_piece_concept_name2symbol_or_prefix___default = dict(
        escaped_piece_prefix = '^'
        ,formatted_piece_prefix = '%'
            #escaped_piece_prefix 在前，先发生作用，然后才轮到 formatted_piece_prefix 起作用
            # '^%...' 类似python的fr"" === (r"").format(...)
        ##################上面的前缀 与 下面的前缀 自由组合
        ,embedding_comment_open_prefix = '---{:'
        ,embedding_comment_close_prefix = '---}:'
            # ---{:tag 行内内嵌注释 }---:tag
        ,single_piece_comment_prefix = '---:'
            # ---:单块注释
        ,line_tail_comment_indicator = '-----:'
        ,line_tail_unparsed_arguments_indicator = '+++++:'
            # -----: 行尾注释
            # +++++: 行尾不解析的额外参数
            # 这两者 谁先出现，谁有效，后出现者 无效

        ,subcommand_prefix = '!!!:'
            # !!!:subcmd ...
        ,string_argument_piece_prefix = '='
        ,tensor_argument_open = '['
        ,tensor_argument_close = ']'
        ,argument_box_open = '{'
        ,argument_box_close = '}'
        ,tensor_argument_tag_prefix = ':'
            #,tensor_argument_tagged_open_prefix = '[:'
            #,tensor_argument_tagged_close_prefix = ']:'
        ,argument_box_tag_prefix = ':'
            #,argument_box_tagged_open_prefix = '{:'
            #,argument_box_tagged_close_prefix = '}:'
        ,tensor_element_topdown_separator_prefix = ','
        ,tensor_element_bottomup_separator_prefix = ':'
        ,tensor_element_separator_level_digits__little_endian = tuple('0123456789')
            # level >= 1
            #互斥:tensor_element_separator_level_digit vs argument_prefix,escaped_piece_prefix,formatted_piece_prefix
            #   ":1="
            #   ",1="
            #   ",1["
            #   ",1{"
            #   ",1^"
            #   ",1%"
        #tensor has num_faces faces
        #tensor.faces[i] has rank[i]=dimensions[i] channels/rows/columns
        #tensorA.faces[i].channels[j] is tensorB with rankB=rankA[:i]+rankA[i+1:]
        ,tensor_face_dimension_digits__little_endian = tuple('0123456789')
        ,tensor_face_dimension_wildcard = '?'
        ,tensor_face_dimension_separator = '.'
            # [:tag .?.2.3 ... ]:tag
            # [.?.2.3][:tag ... ]:tag
        ##################
        ##################
        ,call_symbol_after_argument_box_open = '!'
        ,func_call_prefix = '!:'
            # {!:tag @@:who !:func ... }:tag
            # {!: !:func ... }:
            # <argument_box_open><call_symbol_after_argument_box_open><argument_box_tag_prefix><tag> <func_call_prefix><func_name> ... <argument_box_close><argument_box_tag_prefix><tag>
        ,who_prefix = '@@:'
            # {!:tag @@:who !:func ... }:tag
            # 额外参数: {%:tag @@:who @:kw =arg ... }:tag affected_arg
        ,expr_symbol_after_argument_box_open = '()'
            # 表达式括号: {():tag expr }:tag
        ,unpack_symbol_after_argument_box_open = '{}='
            # 解包: {{}=:tag expr }:tag
        ,middle_operator_prefix = '/:'
        ,end_operator_prefix = '.:'
        ,last_operator_prefix = '/.:'
            # 多元运算符
            # {!:tag !:head ... /:middle ... }:tag
            # {!:tag !:head ... /:middle ... .:end }:tag
            # {!:tag !:head ... /:middle ... /.:last ... }:tag
        ,middle_call_symbol_after_argument_box_open = '/'
        ,end_call_symbol_after_argument_box_open = '.'
        ,last_call_symbol_after_argument_box_open = '/.'
            # 多元运算符
            # {!:tag !:head ...
            # }{/:tag /:middle ...
            # }{.:tag .:end }
            # }{/.:tag /.:last ... }
        ##################
        ##################
        ,transparent_scope_symbol_after_argument_box_open = '==='
            # 透明作用域
            # {===:tag {%%%:tag @@:who @:kw =arg ... }:tag affected_arg* }:tag unaffected_arg*
        ,local_extra_argument_symbol_after_argument_box_open = '%'
            # 额外参数: {%:tag @@:who @:kw =arg ... }:tag affected_arg
        ,scoped_extra_argument_symbol_after_argument_box_open = '%%%'
            # 影响 所在局部空间域 的 后续部分
            # 额外参数: {%%%:tag @@:who @:kw =arg ... }:tag affected_arg*
        #local_extra_argument_symbol_after_argument_box_open/scoped_extra_argument_symbol_after_argument_box_open 可用于 设置更换默认值，设置局部变量，更换选项名kw，更换目标对象名who
            # 设置局部变量: {%%%:tag @@:the_CmdlinePrefixParser.local_variable.definition @:kw =arg ... }:tag affected_arg*
            # 设置自动递增局部变量: {%%%:tag @@:the_CmdlinePrefixParser.local_variable.definition.integer_increase @:kw =arg ... }:tag affected_arg*
            # 设置自动递减局部变量: {%%%:tag @@:the_CmdlinePrefixParser.local_variable.definition.integer_decrease @:kw =arg ... }:tag affected_arg*
        ,toplayer_reconfigure_cmdline_parser_global_extra_argument_symbol_after_argument_box_open = '%%%%%'
            # 更换整套命令行解析前缀集合
            # 特殊对待，至少要读到 close 才可使新设置生效
            # 只能出现在顶层，影响 顶层 后续部分
            # 额外参数: {%%%%%:tag @:kw =arg ... }:tag affected_arg*
            #   no "who"
        ##################
        ##################
        ,option_prefix = '@:'
            # @:选项名  单参数
        ,option_using_default_prefix = '@[_]:'
        ,option_using_Nothing_prefix = '@[]:'
            # @[_]:选项名
            # @[]:选项名
            # 无参数
        ##################
        ,switch_turn_on_prefix = '?+:'
        ,switch_turn_off_prefix = '?-:'
            # ?+:选项名
            # ?-:选项名
            # 无参数
        ,switch_using_default_prefix = '?[_]:'
        ,switch3_using_Nothing_prefix = '?[]:'
        ,switch4_using_ALL_prefix = '?[..]:'
            # ?[_]:选项名
            # ?[]:选项名
            # ?[..]:选项名
            # 无参数
        ##################
        ,positional_argument_indicator = '@,'
            # 位置参数
            # @,  单参数
        ,positional_argument_using_default_indicator = '@,[_]'
        ,positional_argument_using_Nothing_indicator = '@,[]'
            # @,[_]
            # @,[]
            # 无参数
        ##################
        ##################
        ,enduser_defined_positional_argument_indicator = '//@,'
            # 类似python的args，用户自定义额外参数
            # //@,  单参数
        ,enduser_defined_positional_argument_using_default_indicator = '//@,[_]'
        ,enduser_defined_positional_argument_using_Nothing_indicator = '//@,[]'
            # //@,[_]
            # //@,[]
            # 无参数
        ##################
        ,enduser_defined_option_prefix = '//@:'
            # 类似python的kwargs，用户自定义额外参数
            # //@:选项名  单参数
        ,enduser_defined_option_using_default_prefix = '//@[_]:'
            #可于 额外参数 设置 默认值 #scoped_extra_argument_symbol_after_argument_box_open
        ,enduser_defined_option_using_Nothing_prefix = '//@[]:'
            # //@[_]:选项名
            # //@[]:选项名
            # 无参数
        ##################
        ,enduser_defined_switch_turn_on_prefix = '//?+:'
        ,enduser_defined_switch_turn_off_prefix = '//?-:'
            # //?+:选项名
            # //?-:选项名
            # 无参数
        ,enduser_defined_switch_using_default_prefix = '//?[_]:'
        ,enduser_defined_switch3_using_Nothing_prefix = '//?[]:'
        ,enduser_defined_switch4_using_ALL_prefix = '//?[..]:'
            # //?[_]:选项名
            # //?[]:选项名
            # //?[..]:选项名
            # 无参数
        ##################
        ##################
        ,query_prefix = '???:'
            # 查询
            # 列出、过滤 选项
            # 查询选项 帮助内容、默认值 等。。。
            # ???:符号或前缀
            # 无参数
            #
            # ???:@:
            # ???:!:
        ,
        )
    #####################################
    #####################################
    #####################################
    formatted_string_piece_concept_name2symbol_or_prefix___default = dict(
        #见上面:设置局部变量。顺序递增变量: 每次引用自动迭代
        #如何引用？
        # escape_unformatted_string_to_formatted_string
        #   %{ -> %0{ -> %1{ -> ... -> %9{ -> %00{ -> %01{ -> ... -> %99{ -> %000{ -> %001{ -> ...
        #注意: %{ - prefix; / or [raw_tag]/ - suffix
        #   并非 %{/ - prefix
        # formatted_string
        #   %{/<var_name>}/
        #   %{/<var_name>:/<var_fmt>}/
        #   %{/<expr>:/<recur_embedding_formatted_string4var_fmt>}/
        #   ##var_name/var_fmt may be weird, so required [raw_tag]
        #   %{[raw_tag]/<var_name>}[raw_tag]/
        #   %{[raw_tag]/<var_name>:[raw_tag]/<var_fmt>}[raw_tag]/
        #   %{[raw_tag]/<expr>:[raw_tag]/<recur_embedding_formatted_string4var_fmt>}[raw_tag]/
        #
        #   %{[raw_tag]%/<var_name>}[raw_tag]/
        #       firstly, format var_name once
        #   %{[raw_tag]%%/<var_name>}[raw_tag]/
        #       firstly, format var_name twice
        #   %{[raw_tag]/<var_name>:[raw_tag]%/var_fmt}[raw_tag]/
        #       firstly, format var_fmt once
        #   %{[raw_tag]/<var_name>:[raw_tag]%%/var_fmt}[raw_tag]/
        #       firstly, format var_fmt twice
        pseudo_formatting_piece_header_mark_symbol = '%'
        ,pseudo_formatting_piece_lifted_level_digits__little_endian = tuple('0123456789')
        ,pseudo_formatting_piece_body_mark_symbol = '{' #not '{/'
        ,pseudo_formatting_piece_body_separator_symbol = ':' #not ':/'
        ,pseudo_formatting_piece_end_mark_symbol = '}' #not '}/'
        ,pseudo_formatting_piece_raw_tag_open_symbol = '['
        ,pseudo_formatting_piece_raw_tag_close_symbol = ']'
        ,pseudo_formatting_piece_maybe_raw_tag_and_format_ops_end_symbol = '/'
        ,pseudo_formatting_piece_var_name_format_op_symbol = '%'
            # %3{    #not %3{/
            # %{/xxx:/0>4}/
            # %{[raw_tag]/xxx:[raw_tag]/0>4}[raw_tag]/
            # %{[raw_tag]%/xxx%{/yyy}/:[raw_tag]%/0>4}[raw_tag]/
        ,pseudo_formatting_piece_raw_tagged_body_mark_open_symbol = '{['
        ,pseudo_formatting_piece_raw_tagged_body_mark_close_symbol = ']'
        ,pseudo_formatting_piece_raw_tagged_body_separator_open_symbol = ':['
        ,pseudo_formatting_piece_raw_tagged_body_separator_close_symbol = ']'
        ,pseudo_formatting_piece_raw_tagged_end_mark_open_symbol = '}['
        ,pseudo_formatting_piece_raw_tagged_end_mark_close_symbol = ']'
            # %3{[
            # %{[rrr]xxx:[rrr]0>4}[rrr]
        ,
        )
    #####################################
    #####################################
    #####################################
    escaped_string_piece_concept_name2symbol_or_prefix___default = dict(
        # escape_unescaped_string_to_escaped_string
        #   ^{ -> ^0{ -> ^1{ -> ... -> ^9{ -> ^00{ -> ^01{ -> ... -> ^99{ -> ^000{ -> ^001{ -> ...
        # escaped_string
        #   ^{<escape_case>:<payload>}
        #   ^{U:hhhh_hhhh}
        #   ^{u:hhhh}
        #   ^{x:hh}
        #   ^{U:hhhh_hhhh,hhhh_hhhh}
        #   ^{u:hhhh}
        #   ^{x:hh,hh,hh,hh}
        #   ^{hex%encoding:hh...}
        pseudo_escaping_piece_header_mark_symbol = '^'
        ,pseudo_escaping_piece_lifted_level_digits__little_endian = tuple('0123456789')
        ,pseudo_escaping_piece_body_mark_symbol = '{'
        ,pseudo_escaping_piece_body_separator_symbol = ':'
        ,pseudo_escaping_piece_inter_payload_separator_symbol = ','
        ,pseudo_escaping_piece_intra_payload_separator_symbol = '_'
        ,pseudo_escaping_piece_end_mark_symbol = '}'
        ,pseudo_escaping_piece_escape_case_symbol4unicode32 = 'U'
        ,pseudo_escaping_piece_escape_case_symbol4unicode16 = 'u'
        ,pseudo_escaping_piece_escape_case_symbol4hex8 = 'x'
        #   ^{U:hhhh_hhhh,hhhh_hhhh}
        #   ^{u:hhhh}
        #   ^{x:hh,hh,hh,hh}
        ,
        )
    '\U11111111'
    '\u1111'

    def get_name2prefix(sf, /):
        return MappingProxyType(type(sf).___get_name2prefix___())
    def ___get_name2prefix___(sf, /):
        pass





