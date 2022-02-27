重做！
    前缀！不得使用 中间分隔符！无需对负载字符串作任何假设约束！
        类似python的fr""，区分 是否引用变量 是否使用转义字符 是否解码字节串（需要 编码名）
            这些 字符串 相关前缀 作用于 任何其他前缀之前！
        前缀 不得是 其他前缀的 前缀 或 ？后缀？
    行内内嵌注释？行尾注释？
    参数
        * 字符串
        * 张量 [ ... ]
          , <==> 1,
            由外而内
          : <==> 1:
            由内而外
          [ ,参数 ,参数 ...]
            [?][ ,参数 ,参数 ...]
            [?][ 1,参数 1,参数 ...]
            [?][ 1:参数 1:参数 ...]
            #array<?>
          [3: ,参数 :参数 :参数  ,参数 :参数 :参数 ... ]
            [?.3][ ,参数 :参数 :参数  ,参数 :参数 :参数 ... ]
            [?.3][ 1,参数 1:参数 1:参数  1,参数 1:参数 1:参数 ... ]
            [?.3][ 1,参数 2,参数 2,参数  1,参数 2,参数 2,参数 ... ]
            [?.3][ 2:参数 1:参数 1:参数  2:参数 1:参数 1:参数 ... ]
            #matrix<?,3>
            [?.3][ ,参数 1:参数 1:参数  ,参数 1:参数 1:参数 ... ]
            [?.3][ 2:参数 1:参数 1:参数  2:参数 1:参数 1:参数 ... ]
          [3.2: 3:参数 1:参数 2:参数 1:参数  2:参数 1:参数 3:参数 1:参数 2:参数 1:参数  2:参数 1:参数 3:参数 1:参数 2:参数 1:参数  2:参数 1:参数 ... ]
            [?.3.2][ 3:参数 1:参数 2:参数 1:参数  2:参数 1:参数 3:参数 1:参数 2:参数 1:参数  2:参数 1:参数 3:参数 1:参数 2:参数 1:参数  2:参数 1:参数 ... ]
            #tensor<?,3,2>

        * 参数包 { ... }
        ===
        tagged?
            [:tag ]:tag
            {:tag }:tag
            ===
            {:tag !func }:tag
            调用函数？命令行解析器内建+命令行程序内建+终端用户自定义组合器+脚本？
                如何解包 参数包？
                    可能 返回值 是 参数包
        ===
        额外参数:%{ ... }=...
            命令行解析器自用 vs 命令行解析器使用者/命令行程序自用 vs 命令行使用者/终端用户自用
            #3个 参数传入的目标对象，但也可能有更多层，需要 系统性命名、自荐空间限定名、重命名...
            * 命令行解析器自用:
                * 如上面 编码名
                    局部设置，也可设置全行默认值
                * 更换整套 命令行解析前缀集合
                    注意[0-9]！
                * 设置更换 默认值
            * 命令行程序自用
            * 终端用户自用:
                如：C++ 宏定义
                    终端用户/命令行使用者 是 C++编译器使用者
                    命令行程序/命令行解析器使用者 是 C++编译器作者
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

r'''
seed.recognize.CmdlinePrefixParser
debug_pym seed.recognize.CmdlinePrefixParser
py -m seed.recognize.CmdlinePrefixParser




TODO:
    add arg_begin/arg_end for arg
    add arg_end to main_parsed_result
TODO:
    DONE!
    case_or_prefix_setting --> case_or_prefix_setting_or_optional_prefix_setting_pair_seq
    ancestors --> level_match_pieces
    cased_argv_ex --> main_parsed_results
    cased_arg_ex --> main_parsed_result
    cased_parse_result --> local_parsed_result
    cmay_cased_parse_result --> cmay_local_parsed_result

std_prefix_setting = {bifix: case_or_optional_std_prefix_setting_pair_seq}
optional_std_prefix_setting_pair_seq = nonempty tuple<(optional, std_prefix_setting)>{this[-1][0]==False}
prefix :: nonempty str


prefix_setting = {prefix_or_bifix: case_or_prefix_setting_or_optional_prefix_setting_pair_seq}
case_or_prefix_setting_or_optional_prefix_setting_pair_seq = case|prefix_setting|optional_prefix_setting_pair_seq
prefix_or_bifix = prefix|bifix
bifix = (prefix, suffix)
prefix, suffix, case :: str
    prefix :: nonempty str
optional_prefix_setting_pair_seq = tuple<(optional, prefix_setting)>
    # nonempty? yes! to simplify check by restrict locally: optional_prefix_setting_pair_seq nonempty, last optional==False, all prefix nonempty
    #prefix space/direct-product
optional :: bool

case2group = {case:group}
case, group :: str
    #group = std_case #eqv case class

main_parsed_result:
    #main branch = as std always choose optional_prefix_setting_pair_seq[-1]
    local_parsed_result = (case, [level_match_piece], ipayload)
    cmay_local_parsed_result = ()|local_parsed_result
    main_parsed_result = (main_case, [level_match_piece], (arg, arg_begin, ipayload, arg_end))
    level_match_piece = (key_match_piece, [cmay_nonmain_branch_match_piece])
    key_match_piece = (key, capture)
        # '{prefix}{capture}{suffix}{payload4continue_parse}'
    key = prefix_or_bifix
    nonmain_branch_match_piece = (product_case, [level_match_piece])
    cmay_nonmain_branch_match_piece = ()|nonmain_branch_match_piece
        == cmay_local_parsed_result[:-1]




my argparser
      example: doctest fail on nn_ns.filedir.inf_dir::main
    * avoid raise SystemExit when fail
      funtional useful for testing
    * avoid print to sys.stderr
      configurable/redirectable
      doctest(nn_ns.filedir.inf_dir) -> show too many error info
    * multi option require/conflict/depend/... instead of single
      nn_ns.filedir.inf_dir require at least one of -i,-p
      -h/--help is another example
    * subcmd of subcmd, options before subcmd ...
    * prefix as arg case/type
      '**' ==>> subcmd
      '+' ==>> option
        take args until eol or non-arg
        array vs tuple
      '-' ==>> option
        take exactly one arg
          can use kw '[' ']' to group
          or use ',' prefix'
          ===now:
          [{tag} ]{tag}
            not use ',' prefix, since ',[' hard to impl
                #其实，还是太过注重 优化常用情景，如果『=』是参数必带的前缀，则 『,[[』、『,=...』、『,^=...』、『,&^=...』、『,&=...』可完全区分开！
      '?' ==>> switch/help/query-default-choices
        #switch
        '?-' off
        '?+' on
        #help/query-default-choices
        '?:'
            '?:??' for switch
            '?:+' for option
            '?:-' for option
            '?:**' for subcmd

      '&' ==>> define var
        usage: setting path used locally(this cmd only, hs::let)
            <==> let x=y in z
            z is format_str: {x}
        xxx regex'&[^=]*='
        regex'&.*'
            take exactly one arg
                not allow '['
                expect str formated? escaped?
      xxx '#' ==>> int
      xxx '@' ==>> path
        prefix regex'@(/|./|&)'
        '@/' abspath
        '@./' relative_path
        '@&' spec named file STDOUT DEVNULL...
      '=' ==>> str
        prefix regex'=(\[(regex|glob)])?[=&][=~]'
        (regex|glob)? str or regex or glob
        [=&] formated? {var} or &{var} or {&var}
        [=~] raw vs escaped


      kw:
        list:
          '[' ']'
            element sep by ' ' #space
          '{' ':' ',' ';' '.' '!' '}'
            element prefix by ordered: ':' ',' ';' '.' '!'




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
          [3 ,参数 :参数 :参数  ,参数 :参数 :参数 ... ]
            [?*3][ ,参数 :参数 :参数  ,参数 :参数 :参数 ... ]
            #matrix<?,3>
            [?*3][ ,参数 1:参数 1:参数  ,参数 1:参数 1:参数 ... ]
            [?*3][ 2:参数 1:参数 1:参数  2:参数 1:参数 1:参数 ... ]
          [3*2 3:参数 1:参数 2:参数 1:参数  2:参数 1:参数 3:参数 1:参数 2:参数 1:参数  2:参数 1:参数 3:参数 1:参数 2:参数 1:参数  2:参数 1:参数 ... ]
            [?*3*2][ 3:参数 1:参数 2:参数 1:参数  2:参数 1:参数 3:参数 1:参数 2:参数 1:参数  2:参数 1:参数 3:参数 1:参数 2:参数 1:参数  2:参数 1:参数 ... ]
            #tensor<?,3,2>



#'''


___begin_mark_of_excluded_global_names__0___ = ...

__all__ = '''
    PrefixSettingDict
    deepcopy_prefix_setting
    check_prefix_setting
        check_prefix_setting__PrefixSettingDict
            check_type_is_PrefixSettingDict
    check_argv
    cmdline_prefix_parse
    CmdlinePrefixParser
    Globals
    '''.split()

from collections.abc import Mapping
from seed.tiny import echo, fst, snd
from seed.helper.check.checkers import check_pair, check_type_is, check_tuple, check_cased_tuple__free, check_str, check_bool, check_obj_is, check_all, check_len_of, check_callable, check_uint
#from seed.seq_tools.is_prefix_of_seq import is_prefix_of_seq#, is_suffix_of_seq
from seed.seq_tools.bisearch import bisearch
from seed.types.FrozenDict import FrozenDict
___end_mark_of_excluded_global_names__0___ = ...



class PrefixSettingDict(FrozenDict):
    'required@use_bisearch=True'
    def __init__(sf, /, *args, **kwargs):
        super().__init__(*args, **kwargs)
        prefix_setting = sf
        prefix_or_bifix__sorted_ls = sorted(prefix_setting.keys(), key=_either2bifix) #_key_func__prefix_or_bifix#_either2bifix
        sf.__sorted_keys = tuple(prefix_or_bifix__sorted_ls)
        sf.__max_len_of_prefixes = max(map(len, map(_either2prefix, sf.__sorted_keys)), default=0)
    def get_sorted_keys(sf, /):
        return sf.__sorted_keys
    def get_max_len_of_prefixes(sf, /):
        return sf.__max_len_of_prefixes

def _key_func__prefix_or_bifix(prefix_or_bifix):
    'prefix_or_bifix__sorted_ls = sorted(prefix_setting.keys(), key=_key_func__prefix_or_bifix)'
    #ver2
    return _either2bifix(prefix_or_bifix)
    #ver1
    return (type(prefix_or_bifix).__name__, prefix_or_bifix)

def deepcopy_prefix_setting(items2mapping, prefix_setting, /,*, is_prefix_setting_std:bool, to_deepcopy_as_std_prefix_setting:bool):
    check_bool(is_prefix_setting_std)
    check_bool(to_deepcopy_as_std_prefix_setting)
    check_prefix_setting(prefix_setting, is_prefix_setting_std=is_prefix_setting_std)

    def convert_case_or_prefix_setting_or_optional_prefix_setting_pair_seq(case_or_prefix_setting_or_optional_prefix_setting_pair_seq):
        if type(case_or_prefix_setting_or_optional_prefix_setting_pair_seq) is str:
            case = case_or_prefix_setting_or_optional_prefix_setting_pair_seq
            new_case = case
            new_case_or_prefix_setting_or_optional_prefix_setting_pair_seq = new_case
        elif type(case_or_prefix_setting_or_optional_prefix_setting_pair_seq) is tuple:
            optional_prefix_setting_pair_seq = case_or_prefix_setting_or_optional_prefix_setting_pair_seq
            new_optional_prefix_setting_pair_seq = tuple((optional, convert_prefix_setting(prefix_setting)) for optional, prefix_setting in optional_prefix_setting_pair_seq)
            new_case_or_prefix_setting_or_optional_prefix_setting_pair_seq = new_optional_prefix_setting_pair_seq
        else:
            prefix_setting = case_or_prefix_setting_or_optional_prefix_setting_pair_seq
            new_prefix_setting = convert_prefix_setting(prefix_setting)
            if to_deepcopy_as_std_prefix_setting:
                new_optional_prefix_setting_pair_seq = ((False, new_prefix_setting),)
                new_case_or_prefix_setting_or_optional_prefix_setting_pair_seq = new_optional_prefix_setting_pair_seq
            else:
                new_case_or_prefix_setting_or_optional_prefix_setting_pair_seq = new_prefix_setting
            new_case_or_prefix_setting_or_optional_prefix_setting_pair_seq
        new_case_or_prefix_setting_or_optional_prefix_setting_pair_seq

        return new_case_or_prefix_setting_or_optional_prefix_setting_pair_seq

    if to_deepcopy_as_std_prefix_setting:
        convert_key = _either2bifix
    else:
        convert_key = echo
    def convert_prefix_setting(prefix_setting):
        return items2mapping(
            (convert_key(prefix_or_bifix), convert_case_or_prefix_setting_or_optional_prefix_setting_pair_seq(case_or_prefix_setting_or_optional_prefix_setting_pair_seq))
            for prefix_or_bifix, case_or_prefix_setting_or_optional_prefix_setting_pair_seq in prefix_setting.items()
            )
    def main():
        new_prefix_setting = convert_prefix_setting(prefix_setting)
        check_prefix_setting(new_prefix_setting, is_prefix_setting_std=is_prefix_setting_std or to_deepcopy_as_std_prefix_setting)
        return new_prefix_setting
    return main()

def check_type_is_PrefixSettingDict(prefix_setting):
    check_type_is(PrefixSettingDict, prefix_setting)
def check_prefix_setting__PrefixSettingDict(prefix_setting, /,*, is_prefix_setting_std:bool, check_case=None):
    check_prefix_setting(prefix_setting, check_mapping=check_type_is_PrefixSettingDict, check_case=check_case, is_prefix_setting_std=is_prefix_setting_std)
def check_prefix_setting(prefix_setting, /,*, is_prefix_setting_std:bool, check_mapping=None, check_case=None):
    check_bool(is_prefix_setting_std)

    if check_mapping is None:
        check_mapping = echo
    if check_case is None:
        check_case = echo
    check_callable(check_mapping)
    check_callable(check_case)

    def put(occured_cases, case):
        #detect duplicate
        #for duplicate:see:case2group
        if case in occured_cases: raise ValueError(fr'case duplicate: {case!r}')
        occured_cases.add(case)

    def recur4check_pairs(occured_cases, optional_prefix_setting_pair_seq):
        check_tuple(optional_prefix_setting_pair_seq)
        check_all(check_pair, optional_prefix_setting_pair_seq)
        check_len_of(optional_prefix_setting_pair_seq, min=1)
        check_all(check_bool, map(fst, optional_prefix_setting_pair_seq))
        check_obj_is(False, fst(optional_prefix_setting_pair_seq[-1]))

        #check_all(recur, map(snd, optional_prefix_setting_pair_seq))
        _, main_branch = optional_prefix_setting_pair_seq[-1]
        recur(occured_cases, main_branch)
        for _, nonmain_branch in optional_prefix_setting_pair_seq[:-1]:
            recur(set(), nonmain_branch)
    def recur(occured_cases, prefix_setting):
        if not isinstance(prefix_setting, Mapping): raise TypeError
        check_mapping(prefix_setting)
        for prefix_or_bifix in prefix_setting.keys():
            if type(prefix_or_bifix) is str:
                prefix = prefix_or_bifix
                if is_prefix_setting_std: raise ValueError
                pass
            else:
                bifix = prefix_or_bifix
                check_pair(bifix)
                prefix, suffix = bifix
                check_type_is(str, prefix)
                check_type_is(str, suffix)

        for case_or_prefix_setting_or_optional_prefix_setting_pair_seq in prefix_setting.values():
            if type(case_or_prefix_setting_or_optional_prefix_setting_pair_seq) is str:
                case = case_or_prefix_setting_or_optional_prefix_setting_pair_seq
                check_case(case)
                put(occured_cases, case)
            elif type(case_or_prefix_setting_or_optional_prefix_setting_pair_seq) is tuple:
                optional_prefix_setting_pair_seq = case_or_prefix_setting_or_optional_prefix_setting_pair_seq
                recur4check_pairs(occured_cases, optional_prefix_setting_pair_seq)
            else:
                prefix_setting = case_or_prefix_setting_or_optional_prefix_setting_pair_seq
                if is_prefix_setting_std: raise ValueError
                recur(occured_cases, prefix_setting)

        prefixes = [*map(_either2prefix, prefix_setting.keys())]
        prefixes.sort()
        sorted_prefixes = prefixes; del prefixes
        for prev_prefix, curr_prefix in zip(sorted_prefixes, sorted_prefixes[1:]):
            if curr_prefix.startswith(prev_prefix): raise ValueError(fr'prefix conflct: {curr_prefix!r}.startswith({prev_prefix!r})')
    #end-def recur(occured_cases, prefix_setting):

    recur(set(), prefix_setting)
    return

def check_argv(argv):
    check_tuple(argv)
    if not all(type(arg) is str for arg in argv):raise TypeError
def cmdline_prefix_parse(prefix_setting, argv, /,*, use_bisearch:bool, is_prefix_setting_std:bool):
    'prefix_setting -> argv::[arg] -> main_parsed_results::[main_parsed_result]'
    check_bool(use_bisearch)
    if use_bisearch:
        check_prefix_setting__PrefixSettingDict(prefix_setting, is_prefix_setting_std=is_prefix_setting_std)
    else:
        check_prefix_setting(prefix_setting, is_prefix_setting_std=is_prefix_setting_std)

    argv = tuple(argv)
    check_argv(argv)
    main_parsed_results = _cmdline_prefix_parse(prefix_setting, argv, use_bisearch=use_bisearch)
    return main_parsed_results
def _cmdline_prefix_parse(prefix_setting, argv, /,*, use_bisearch:bool):
    'prefix_setting -> argv::[arg] -> main_parsed_results::[main_parsed_result]'
    #not check:check_prefix_setting(prefix_setting)
    #check_argv(argv)
    check_bool(use_bisearch)

    main_parsed_results = tuple(_cmdline_prefix_parse__arg2main_parsed_result(prefix_setting, arg, use_bisearch=use_bisearch, arg_begin=None, arg_end=None) for arg in argv)
    return main_parsed_results

def _either2prefix(prefix_or_bifix):
    prefix, suffix = _either2bifix(prefix_or_bifix)
    return prefix
def _either2bifix(prefix_or_bifix):
    if type(prefix_or_bifix) is str:
        prefix = prefix_or_bifix
        suffix = ''
    else:
        bifix = prefix_or_bifix
        prefix, suffix = bifix
    return prefix, suffix

def _cmdline_prefix_parse__arg2main_parsed_result(prefix_setting, arg, /,*, use_bisearch:bool, arg_begin:int, arg_end:int):
    'prefix_setting -> arg::str -> main_parsed_result'
    #not check:check_prefix_setting(prefix_setting)
    check_str(arg)
    if arg_begin is None:
        arg_begin = 0
    if arg_end is None:
        arg_end = len(arg)
    check_uint(arg_begin)
    check_uint(arg_end)
    #L = len(arg)
    if not 0 <= arg_begin <= arg_end <= len(arg): raise ValueError

    def startswith(arg_idx, prefix):
        return arg.startswith(prefix, arg_idx, arg_end)
        #return is_prefix_of_seq(prefix, arg, begin=arg_idx)

    #mk_filtered_items_ex = mk_filtered_items_ex__bisearch if use_bisearch else mk_filtered_items_ex__plain
    #py3.8 bug? why? def mk_filtered_items_ex__bisearch(prefix_setting:PrefixSettingDict, arg_idx, /):
    #   SystemError: no locals when loading 'PrefixSettingDict'
    def mk_filtered_items_ex__bisearch(prefix_setting, arg_idx, /):
        check_type_is(PrefixSettingDict, prefix_setting)
        sorted_keys = prefix_setting.get_sorted_keys()
        max_len_of_prefixes = prefix_setting.get_max_len_of_prefixes()
        s = arg[arg_idx:min(arg_end, arg_idx+max_len_of_prefixes)]
        lower, upper = bisearch(s, sorted_keys, key=_either2prefix)
        assert 0 <= lower <= upper <= len(sorted_keys)
        assert upper == len(sorted_keys) or s < _either2prefix(sorted_keys[upper])
        assert upper == lower or s == _either2prefix(sorted_keys[upper-1])
        assert lower == upper or s == _either2prefix(sorted_keys[lower])
        assert lower == 0 or s > _either2prefix(sorted_keys[lower-1])

        while lower:
            i = lower - 1
            key = sorted_keys[i]
            if s.startswith(_either2prefix(key)):
                lower = i
            else:
                break
        filtered_items = [(key, prefix_setting[key]) for key in sorted_keys[lower:upper]]
        return filtered_items

    def mk_filtered_items_ex__plain(prefix_setting, arg_idx, /):
        filtered_items = []
        for prefix_or_bifix, case_or_prefix_setting_or_optional_prefix_setting_pair_seq in prefix_setting.items():
            prefix = _either2prefix(prefix_or_bifix)

            #if arg.startswith(prefix):
            if startswith(arg_idx, prefix):
                filtered_items.append((prefix_or_bifix, case_or_prefix_setting_or_optional_prefix_setting_pair_seq))
        return filtered_items
    mk_filtered_items_ex = mk_filtered_items_ex__bisearch if use_bisearch else mk_filtered_items_ex__plain

    #level_match_pieces = []
    def recur(level_match_pieces, prefix_setting, arg_idx, /,*, optional:bool):
        '-> cmay_local_parsed_result #== ()|local_parsed_result #optional=False==>>local_parsed_result'
        filtered_items = mk_filtered_items_ex(prefix_setting, arg_idx)
        if not filtered_items:
            if optional:
                cmay_local_parsed_result = ()
                return cmay_local_parsed_result
            prefix_or_bifix__sorted_ls = sorted(prefix_setting.keys(), key=_key_func__prefix_or_bifix)
            raise ValueError(fr'no prefix match arg={arg!r}@[{arg_idx}:{arg_end}]: level_match_pieces={level_match_pieces!r}, sub-keys={prefix_or_bifix__sorted_ls!r}')
        if len(filtered_items) > 1:
            prefix_or_bifix__sorted_ls = sorted(map(fst, filtered_items), key=_key_func__prefix_or_bifix)
            try:
                check_prefix_setting(prefix_setting, is_prefix_setting_std=False)
            except:
                #print(fr'bad fmt: prefix_setting:{prefix_setting!r}')
                raise ValueError(fr'too many prefixes match arg={arg!r}@[{arg_idx}:{arg_end}]: {prefix_or_bifix__sorted_ls!r} ###bad fmt: prefix_setting:{prefix_setting!r}')
                raise
            else:
                raise logic-err
        assert len(filtered_items) == 1

        [(prefix_or_bifix, case_or_prefix_setting_or_optional_prefix_setting_pair_seq)] = filtered_items
        if 1:
            prefix, suffix = bifix = _either2bifix(prefix_or_bifix)
            iprefix = arg_idx
            icapture = iprefix + len(prefix)
            imay_isuffix = arg.find(suffix, icapture, arg_end)
            if imay_isuffix == -1:
                raise ValueError(fr'not found suffix={suffix!r} for arg={arg!r}@[{arg_idx}:{arg_end}]: level_match_pieces={level_match_pieces!r}, bifix={(prefix, suffix)!r}')
            isuffix = imay_isuffix
            ipayload = isuffix + len(suffix)
            capture = arg[icapture:isuffix]
            assert 0 <= arg_begin <= arg_idx == iprefix <= icapture <= isuffix <= ipayload <= arg_end <= len(arg)
            assert prefix == arg[iprefix:icapture]
            assert capture == arg[icapture:isuffix]
            assert suffix == arg[isuffix:ipayload]



            key = prefix_or_bifix
            key_match_piece = (key, capture)
        #################################
        #################################
        #################################
        if type(case_or_prefix_setting_or_optional_prefix_setting_pair_seq) is str:
            case = case_or_prefix_setting_or_optional_prefix_setting_pair_seq
            cmay_nonmain_branch_match_pieces = ()
            update_level_match_pieces(level_match_pieces, key_match_piece, cmay_nonmain_branch_match_pieces)

            #payload = arg[ipayload:arg_end]
            level_match_pieces = tuple(level_match_pieces)
            local_parsed_result = (case, level_match_pieces, ipayload)
        elif type(case_or_prefix_setting_or_optional_prefix_setting_pair_seq) is tuple:
            optional_prefix_setting_pair_seq = case_or_prefix_setting_or_optional_prefix_setting_pair_seq
            assert optional_prefix_setting_pair_seq
            assert fst(optional_prefix_setting_pair_seq[-1]) is False

            cmay_nonmain_branch_match_pieces = []
            for (optional, next_prefix_setting) in optional_prefix_setting_pair_seq[:-1]:
                next_arg_idx = ipayload

                #nonmain_branch
                cmay_local_parsed_result = recur([], next_prefix_setting, next_arg_idx, optional=optional)

                #update ipayload
                if cmay_local_parsed_result == ():
                    #not update ipayload
                    pass
                else:
                    local_parsed_result = cmay_local_parsed_result
                    (_case, _level_match_pieces, ipayload) = local_parsed_result
                        #update ipayload
                cmay_nonmain_branch_match_piece = cmay_local_parsed_result[:-1]
                cmay_nonmain_branch_match_pieces.append(cmay_nonmain_branch_match_piece)
            #end-for-loop-pairs[:-1]

            update_level_match_pieces(level_match_pieces, key_match_piece, cmay_nonmain_branch_match_pieces)

            #handle-main_branch-pairs[-1]
            (optional, next_prefix_setting) = optional_prefix_setting_pair_seq[-1]
            next_arg_idx = ipayload
            if not optional is False: raise ValueError
            #main_branch
            local_parsed_result = recur(level_match_pieces, next_prefix_setting, next_arg_idx, optional=False)

        else:
            next_prefix_setting = case_or_prefix_setting_or_optional_prefix_setting_pair_seq
            next_arg_idx = ipayload

            cmay_nonmain_branch_match_pieces = ()
            update_level_match_pieces(level_match_pieces, key_match_piece, cmay_nonmain_branch_match_pieces)

            #main_branch
            local_parsed_result = recur(level_match_pieces, next_prefix_setting, next_arg_idx, optional=False)
        local_parsed_result
        cmay_local_parsed_result = local_parsed_result
        return cmay_local_parsed_result
    #end-def recur(level_match_pieces, prefix_setting, arg_idx, /,*, optional:bool):
    def update_level_match_pieces(level_match_pieces, key_match_piece, cmay_nonmain_branch_match_pieces, /):
        #update level_match_pieces
        cmay_nonmain_branch_match_pieces = tuple(cmay_nonmain_branch_match_pieces)
        level_match_piece = (key_match_piece, cmay_nonmain_branch_match_pieces)
        level_match_pieces.append(level_match_piece)

    #main_branch
    local_parsed_result = recur([], prefix_setting, arg_begin, optional=False)
    check_cased_tuple__free(local_parsed_result)
    (case, level_match_pieces, ipayload) = local_parsed_result

    main_case = case
    main_parsed_result = (main_case, level_match_pieces, (arg, arg_begin, ipayload, arg_end))
    check_cased_tuple__free(main_parsed_result)
    return main_parsed_result
#end-def _cmdline_prefix_parse__arg2main_parsed_result(prefix_setting, arg, /,*, use_bisearch:bool, arg_begin:int, arg_end:int):

class CmdlinePrefixParser:
    def __init__(sf, prefix_setting, /,*, to_deepcopy_prefix_setting:bool=False, to_deepcopy_as_std_prefix_setting:bool=False, use_bisearch:bool=True, use_arbitrary_mapping4prefix_setting:bool=False, is_prefix_setting_std:bool=False):
        check_bool(to_deepcopy_prefix_setting)
        check_bool(use_bisearch)
        check_bool(use_arbitrary_mapping4prefix_setting)

        if to_deepcopy_prefix_setting:
            prefix_setting = deepcopy_prefix_setting(PrefixSettingDict, prefix_setting, is_prefix_setting_std=is_prefix_setting_std, to_deepcopy_as_std_prefix_setting=to_deepcopy_as_std_prefix_setting)

        is_prefix_setting_std = is_prefix_setting_std or (to_deepcopy_prefix_setting and to_deepcopy_as_std_prefix_setting)
        if to_deepcopy_prefix_setting or use_bisearch or not use_arbitrary_mapping4prefix_setting:
            check_prefix_setting__PrefixSettingDict(prefix_setting, is_prefix_setting_std=is_prefix_setting_std)
        else:
            check_prefix_setting(prefix_setting, is_prefix_setting_std=is_prefix_setting_std)

        sf.prefix_setting = prefix_setting
        sf.use_bisearch = use_bisearch
    def parse_arg(sf, arg:str, /,*, arg_begin:int=None, arg_end:int=None):
        'arg::str -> main_parsed_result::(main_case, [level_match_piece], (arg, arg_begin, ipayload, arg_end))'
        main_parsed_result = _cmdline_prefix_parse__arg2main_parsed_result(sf.prefix_setting, arg, use_bisearch=sf.use_bisearch, arg_begin=arg_begin, arg_end=arg_end)
        return main_parsed_result
    def parse_argv(sf, argv, /):
        'argv::[arg] -> main_parsed_results::[main_parsed_result]'
        main_parsed_results = _cmdline_prefix_parse(sf.prefix_setting, argv, use_bisearch=sf.use_bisearch)
        return main_parsed_results



class Globals:
    prefix_setting = {
        '*':'subcmd'
        ,'-':'option'
        ,'?':{
            #'switch'
            '-':'switch_off'
            ,'+':'switch_on'
            }
        ,'&':'var'
        ,'#':'int'
        ,'@':{
            #'path'
            '/':'abspath'
            ,'./':'relative_path'
            ,'&':'spec_named_file' # STDOUT DEVNULL...
            }
        ,'=':(
            #'str'
            (True, {('[', ']'): 'str_format'})
            ,(False, {'=': 'not_format_str', '&':'format_str'})
            ,(False, {'=': 'raw_str', '~':'escaped_str'})
            )
        }
    prefix_setting = deepcopy_prefix_setting(PrefixSettingDict, prefix_setting, is_prefix_setting_std=False, to_deepcopy_as_std_prefix_setting=True)

    cmdline_prefix_parser = CmdlinePrefixParser(prefix_setting, to_deepcopy_prefix_setting=False, to_deepcopy_as_std_prefix_setting=False, use_bisearch=True, use_arbitrary_mapping4prefix_setting=False, is_prefix_setting_std=True)

def _t():
    parse_arg = Globals.cmdline_prefix_parser.parse_arg
    arg2ans = {
        '-o':('option', (((('-', ''), ''), ()),), ('-o', 0, 1, 2))
        ,'@./p':('relative_path', (((('@', ''), ''), ()), ((('./', ''), ''), ())), ('@./p', 0, 3, 4))
        ,'=[fmt]==xs_r':('raw_str', (((('=', ''), ''), (('str_format', (((('[', ']'), 'fmt'), ()),)), ('not_format_str', (((('=', ''), ''), ()),)))), ((('=', ''), ''), ())), ('=[fmt]==xs_r', 0, 8, 12))
        ,'=&~s_fe':('escaped_str', (((('=', ''), ''), ((), ('format_str', (((('&', ''), ''), ()),)))), ((('~', ''), ''), ())), ('=&~s_fe', 0, 3, 7))
        #,'':()
        #,'+++':()
        }


    for arg, ans in arg2ans.items():
        try:
            r = parse_arg(arg)
        except Exception as e:
            print(fr'parse_arg({arg!r}) raise != {ans!r} : {e!r}')
            raise
        else:
            if r != ans:
                print(fr'parse_arg({arg!r}) == {r!r} != {ans!r}')

_t()








