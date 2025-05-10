#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/cmdline/adhoc_argparser.py

see:py_all@bash_script
    py_adhoc_call ''  ,str.list '%difflib:__all__@all' =all
    py_adhoc_call ''  ,str.list %%:@_  =_._.difflib.__all__

py -m nn_ns.app.debug_cmd   seed.recognize.cmdline.adhoc_argparser -x
py -m nn_ns.app.doctest_cmd   seed.recognize.cmdline.adhoc_argparser:__doc__

view ../../python3_src/seed/helper/safe_eval.py
    @20250118: ++kw:using_extended_globals
@20250118: ++kw:flush4print
@20250129: ++kw:to_postpone_KeyboardInterrupt_until_yield ++kw:prompt_string4postpone_KeyboardInterrupt_until_yield => to_postpone_KeyboardInterrupt_until_yield

@20250201
    ++kw:to_show_timedelta
    ++kw:may_prompt_string6resting
    ++kw:may_args4PeriodicToilLeisureTime

@20250202:++to_show_StopIteration_value

@20250301
    ++kw:to_show_total_timedelta

@20250404
    ++kw:smay_kwd4supply_func4resting
        supply/provide


[[
TODO:

定义:资源路径，含 格式/解码协议
  py_adhoc_call 除了『=eval-expr』『:echo-str』，新增『//=load-resource』
    也许可以考虑 直接打开文件:
        『//^rb=open_read-path』
        『//^wb=open_write-path』
e ../../python3_src/seed/recognize/cmdline/adhoc_argparser.py
resource-load-path==protocol+path => loadable path
  path = *.zip:::inner_patb
  dump#raw_bytes
    pickle.dump
  u8
    str#raw_text
    repr
    json.dump
    base64
    a85,b85

serializing-deserializing


]]

[[
py_adhoc_call xxx.yyy ,f | lineno
<--
py_adhoc_call { -lineno } xxx.yyy ,f
<<==:
DONE?:TODO:选项:添加:『+lineno』:『,』枚举时附加行号
  py -m nn_ns.app.adhoc_argparser__main__call8module +lineno  x   ,f
  0:...
  1:...

]]
see:show_help():
    [[
py_adhoc_call =[def]=:
    py -m nn_ns.app.adhoc_argparser__main__call8module "$@"
    ]]

%s/^py -m nn_ns.app.adhoc_argparser__main__call8module/py_adhoc_call/g


seed.recognize.cmdline.adhoc_argparser
py -m nn_ns.app.debug_cmd   seed.recognize.cmdline.adhoc_argparser -x
py -m nn_ns.app.doctest_cmd   seed.recognize.cmdline.adhoc_argparser:__doc__

py -m seed.recognize.cmdline.adhoc_argparser @_NOP_
py -m seed.recognize.cmdline.adhoc_argparser @_test1__at

#太麻烦！『*』换成『!』py -m seed.recognize.cmdline.adhoc_argparser '*_test2__start'
#『!』竟然也被占用！py -m seed.recognize.cmdline.adhoc_argparser !_test2__start
.../txt_phone/txt $ echo !xxx
bash: !xxx: event not found
.../txt_phone/txt $ echo TODO.tx?
TODO.txt
『*』『?』被占用:通配符
『;』被占用:分割命令
改用『,』
py -m seed.recognize.cmdline.adhoc_argparser ,_test2__start

from seed.recognize.cmdline.adhoc_argparser import adhoc_argparse__args, adhoc_argparse__subcmds, adhoc_argparser__main__subcmds, adhoc_argparse__call, adhoc_argparser__main__call, AdhocArgParserError, _NOP_


if __name__ == "__main__":
    from seed.recognize.cmdline.adhoc_argparser import adhoc_argparser__main__subcmds, AdhocArgParserError, _NOP_
    adhoc_argparser__main__subcmds(globals(), None)
        #main()

if __name__ == "__main__":
    from seed.recognize.cmdline.adhoc_argparser import adhoc_argparser__main__call, AdhocArgParserError, _NOP_
    adhoc_argparser__main__call(globals(), None)
        #main()


py_adhoc_call xxx.yyy @f =... :... +xxx -xxx ++xxx:... ++xxx:... --xxx=...
py_adhoc_call xxx.yyy ,f =... :... +xxx -xxx ++xxx:... ++xxx:... --xxx=...
if __name__ == "__main__":
    from seed.recognize.cmdline.adhoc_argparser import adhoc_argparser__main__call8module, AdhocArgParserError, _NOP_
    adhoc_argparser__main__call8module(None)
        #main()

py_adhoc_call xxx.yyy @f =... :... +xxx -xxx ++xxx:... ++xxx:... --xxx=...
py_adhoc_call xxx.yyy ,f =... :... +xxx -xxx ++xxx:... ++xxx:... --xxx=...

xxx.yyy 模块全名
@f 显示结果:f(...)
,f 逐行显示:iter(f(...))
=... save_eval
:... 字符串
+xxx xxx=True
-xxx xxx=False
--xxx:... xxx=...
--xxx=... xxx='...'
++xxx=... xxx=[... ..., ...]
++xxx:... xxx=[... ..., '...']

新增:
    @g.f
    ,g.f

    g=repr|str|ascii|hex|... #builtins.*
     |not_show
     |dump8show #dump bytes directly to stdout
     |pickle_dump8show #dump bytes directly to stdout
     |stable_repr
     |stable_repr__expand_top_layer
     |stable_repr__expand_all_layer
     |stable_repr__expand_all_layer__noindent
     |pprint__pformat
     |pprint__pformat_d3...
     |stable_repr__F__i1...
     |stable_repr__T__i1...
     |stable_repr__F__i1__d3...
     |stable_repr__T__i1__d3...

新增:islice
    @233:f
    @g.233:f
    ,233:f
    ,g.233:f
    ==>>:
    @list.233:f
        py_adhoc_call   script.搜索冫进制数基数乊同一表达型解读为素数   @list.100:枚举冫进制数基数乊同一表达型解读为素数扌 :17401
        py_adhoc_call   script.对数纟差分倍增   @list.100:枚举冫插入位置纟小数部分纟对数纟差分倍增扌 +使用冫负对数


?新增『+lineno』:
    or函数名之前的选项:
        xxx.yyy +lineno ,f
    or模块名之前的选项:
        +lineno xxx.yyy ,f
        def____adhoc_argparser__main__call8module.options4argparser_func_name_to_main_func.options4argparser 处理的是 模块名之后~函数名之前 的选项！
新增『+lineno』:
    py_adhoc_call { --lineno=233 } xxx.yyy ,f
    py_adhoc_call { --lineno=None } xxx.yyy ,f
        <==> py_adhoc_call xxx.yyy ,f
    py_adhoc_call { -lineno } xxx.yyy ,f
        <==> py_adhoc_call { --lineno=0 } xxx.yyy ,f
    py_adhoc_call { +lineno } xxx.yyy ,f
        <==> py_adhoc_call { --lineno=1 } xxx.yyy ,f
新增:++smay_kwd4supply_func4resting
    py_adhoc_call { +flush4print +to_show_timedelta  --may_args4PeriodicToilLeisureTime='(60,60)' --may_prompt_string6resting:$'\n\n    resting...\n\n'  --smay_kwd4supply_func4resting:try_resting_ }  script.辅助冫有限域本原根判定牜泛化梅森指数   ,枚举冫拟泛化梅森指数纟素基灬牜输出指定数量每基扌  --case4trial_division:bit_length --bases4SPRP=[2,3,5,7]  +verbose --num_exps_per_radix=1  --radix2begin4exp='{269:3167+1}'  >> /sdcard/0my_files/tmp/0tmp
    if try_resting_ is None:
        def try_resting_():pass

新增::++to_show_StopIteration_value
    py_adhoc_call  { +to_show_StopIteration_value } seed.math.factor_pint.sprp_factor_pint__via_Lehman_method__O_cube_root   ,iter_try_factor1_pint__via_Lehman_method__layered__easy_   ='(2**17-1)*(2**31-1)'
新增:
    ++kw:to_show_timedelta
    ++kw:may_prompt_string6resting
    ++kw:may_args4PeriodicToilLeisureTime
    py_adhoc_call { +to_postpone_KeyboardInterrupt_until_yield +to_show_timedelta --may_args4PeriodicToilLeisureTime='(60,60)' --may_prompt_string6resting:$'\n\n    resting...\n\n' }  script.搜索冫伪素数牜临近幂方   ,main  =2  =1 =3000+1   =2 =4  --may_prime_basis='[2,3,5,7]' --path:script/搜索冫伪素数牜临近幂方.py..header.2.1-_.sz4.2_3_5_7-SPRP.out.txt
新增『-to_postpone_KeyboardInterrupt_until_yield』『--prompt_string4postpone_KeyboardInterrupt_until_yield=...』:
    『ctrl+c』
    py_adhoc_call  { +to_postpone_KeyboardInterrupt_until_yield }  script.搜索冫伪素数牜临近幂方   ,迭代搜索冫偏移量纟伪素数牜临近幂方扌  '=[2,3]'  '=range(100,110+1)' =10
        ^C KeyboardInterrupt
新增『-flush4print』:
    py_adhoc_call { -flush4print }  script.辅助冫有限域本原根判定   ,stable_repr.factor_ppowmms__via_GNU_factor_ =2 ='range(1,10)' +to_stderr
    py_adhoc_call { +flush4print }  script.辅助冫有限域本原根判定   ,stable_repr.factor_ppowmms__via_GNU_factor_ =2 ='range(1,10)' +to_stderr
新增『-end4print』:
    『-end4print』 <==> 『--end4print='""'』
    『+end4print』 <==> 『--end4print='None'』 <==> 『--end4print='"\n"'』
    py_adhoc_call  { -end4print }  seed.for_libs.for_tarfile   @str.read_solo_tarfile_  :script/搜索冫最短加链长度.py..statistics.out.txt.tar.lzma  --xencoding4data:ascii

新增:
    %!<py_script>
        safe_exec(script)
新增:
    %...  import ...
    %...:...  from ... import ...
    %...:new=old,xx,yy  from ... import old as new, xx, yy
    ----or:
    _.pkg.xxx().obj.yyy
新增:
    %%:@zzz     [zzz:=rjstplr]

py_adhoc_call       seed.math.matrix_chain_product.matrix_chain_product__polygon_partitioning__O_NlogN @matrix_chain_product__polygon_partitioning__O_NlogN  --may_imin=None  '--_turnon_debug=0'  ='[10,11,25,40,12]'




py_adhoc_call       seed.math.matrix_chain_product.matrix_chain_product__dynamic_programming__O_NNN ,matrix_chain_product__dynamic_programming__O_NNN ='[10,11,25,40,12]'




py_adhoc_call       seed.math.matrix_chain_product.test4matrix_chain_product__polygon_partitioning__O_NlogN @随机测试囗囗矩阵乘法链囗多边形囗词典序最先的最优三角化方案囗类同排序算法耗时 '--L2num_tests={L:1000//L for L in range(2,100)}' '--upper4weight=10000' '--version=3' '--_turnon_debug=0'



:%s/^>>> \(\w*\)[.]fullmatch(\([^)]*\)) is None or None$/>>> match_(\1, \2)
:%s/^>>> \(\w*\)[.]fullmatch(\([^)]*\))$/>>> not_match_(\1, \2)
>>> import re
>>> def match_(regex, s, /):
...    return None if not None is regex.fullmatch(s) else False
>>> def not_match_(regex, s, /):
...    return None if None is regex.fullmatch(s) else False

from seed.recognize.cmdline.adhoc_argparser import import_regex

>>> match_(import_regex, '%xxx')
>>> match_(import_regex, '%xxx.yyy')
>>> match_(import_regex, '%x.y@')
>>> match_(import_regex, '%x.y@zzz')
>>> match_(import_regex, '%x.y@z:')
>>> match_(import_regex, '%x.y@:')
>>> match_(import_regex, '%x.y:')
>>> match_(import_regex, '%x:')
>>> match_(import_regex, '%x:aaa')
>>> match_(import_regex, '%x:aaa,bbb')
>>> match_(import_regex, '%x:aaa.bbb')
>>> match_(import_regex, '%x:aaa.bbb@')
>>> match_(import_regex, '%x:aaa.bbb@ccc')
>>> match_(import_regex, '%x:a.b@c,d@e')


>>> not_match_(import_regex, '%x:,a.b@c,d@e')
>>> not_match_(import_regex, '%x:,a.b@c,d@')
>>> not_match_(import_regex, '%x:,a.b@c,d')
>>> not_match_(import_regex, '%x:,a.b@c')
>>> not_match_(import_regex, '%x:,a.b@')
>>> not_match_(import_regex, '%x:,a.b')
>>> not_match_(import_regex, '%x:,a')


>>> not_match_(import_regex, '%') ##++smay_qnm_as__pattern
False
>>> not_match_(import_regex, '%.')
>>> not_match_(import_regex, '%.x')
>>> not_match_(import_regex, '%x.')
>>> not_match_(import_regex, '%x@.')
>>> not_match_(import_regex, '%x:.')
>>> not_match_(import_regex, '%x:.a')
>>> not_match_(import_regex, '%x:a.')



>>> not_match_(import_regex, '%0')
>>> not_match_(import_regex, '%x:0')
>>> not_match_(import_regex, '%x..y')
>>> not_match_(import_regex, '%x:a..b')


>>> match_(import_regex, '%%:@loader')
>>> not_match_(import_regex, '%%:@0')
>>> not_match_(import_regex, '%%:@a.b')


py_adhoc_call   seed.recognize.cmdline.adhoc_argparser @_fwd_call_    %seed.math.matrix_chain_product.test4matrix_chain_product__polygon_partitioning__O_NlogN:随机测试囗囗矩阵乘法链囗多边形囗词典序最先的最优三角化方案囗类同排序算法耗时@f  =f '--L2num_tests={L:1000//L for L in range(2,100)}' '--upper4weight=10000' '--version=3' '--_turnon_debug=0'
    # %xxx.yyy:aaa@f
    #   ok!












py_adhoc_call   seed.recognize.cmdline.adhoc_argparser @_fwd_call_    %seed.math.matrix_chain_product.test4matrix_chain_product__polygon_partitioning__O_NlogN@m '%!f=m.随机测试囗囗矩阵乘法链囗多边形囗词典序最先的最优三角化方案囗类同排序算法耗时'  =f '--L2num_tests={L:1000//L for L in range(2,100)}' '--upper4weight=10000' '--version=3' '--_turnon_debug=0'
    # %xxx.yyy@m  '%!f=m.aaa'
    #   ok!
    # not: 『%xxx.yyy@m  %!f=m.aaa』
    #   『!』has special meaning in shell
    #       see:『HISTORY EXPANSION』
                view others/app/termux/help/bash.man.txt









py_adhoc_call   seed.recognize.cmdline.adhoc_argparser @_fwd_call_    '%!from seed.math.matrix_chain_product.test4matrix_chain_product__polygon_partitioning__O_NlogN import 随机测试囗囗矩阵乘法链囗多边形囗词典序最先的最优三角化方案囗类同排序算法耗时 as f'  =f '--L2num_tests={L:1000//L for L in range(2,100)}' '--upper4weight=10000' '--version=3' '--_turnon_debug=0'
    # '%!from xxx.yyy import aaa as f'
    #   fail: safe_exec() forbid the use of __import__()
    #   SystemError: /home/builder/.termux-build/python/src/Objects/dictobject.c:1490: bad argument to internal function



py_adhoc_call  { -lineno } seed.math.continued_fraction.iter_radix_digits_of_continued_fraction_  ,5:iter_radix_digits_of_continued_fraction__with_int__via_cf_ops_   %itertools:repeat   =10 '=repeat(1)'  +to_chain_integer_part +using_LazyList
0:1
1:6
2:1
3:8
4:0


py_adhoc_call  { +lineno } seed.math.continued_fraction.iter_radix_digits_of_continued_fraction_  ,5:iter_radix_digits_of_continued_fraction__with_int__via_cf_ops_   %itertools:repeat   =10 '=repeat(1)'  +to_chain_integer_part +using_LazyList
1:1
2:6
3:1
4:8
5:0

py_adhoc_call  { --lineno=-10 } seed.math.continued_fraction.iter_radix_digits_of_continued_fraction_  ,5:iter_radix_digits_of_continued_fraction__with_int__via_cf_ops_   %itertools:repeat   =10 '=repeat(1)'  +to_chain_integer_part +using_LazyList
-10:1
-9:6
-8:1
-7:8
-6:0



#]]]'''
__all__ = '''
    adhoc_argparse__args
        adhoc_argparse__subcmds
            adhoc_argparser__main__subcmds
        adhoc_argparse__call
            adhoc_argparser__main__call
            adhoc_argparser__main__call8module

    AdhocArgParserError
    _NOP_


























































    '''.split()#'''
'''
nm__pattern
qnm__pattern
qnm_as__pattern
smay_qnm_as__pattern
import_pattern
arg_pattern
arg_regex
import_regex
AdhocArgParserError
AdhocArgParserError__show_help_then_exit_with_ok__found_help_flag
AdhocArgParserError__show_help_then_exit_with_err
eval_single_arg_payload
adhoc_argparser__main__subcmds
adhoc_argparser__main
args5may_argv
adhoc_argparse__subcmds
adhoc_argparse
prefixes4func_name4adhoc_argparser__main__call
adhoc_argparser__main__call
adhoc_argparser__main__call8module
show_help
help_flags
is_help_flag_
filter_startswith_
adhoc_argparse__call
checked_fullmatch__import_pattern
adhoc_argparse__import
adhoc_argparse__args
adhoc_argparse__args__ver2
adhoc_argparse__args__ver1
    '''.split()#'''
    #adhoc_argparser__main
    #adhoc_argparse
    #eval_single_arg_payload
#__all__:goto

___begin_mark_of_excluded_global_names__0___ = ...
from pprint import pformat as _pprint__pformat
    #pformat(object, indent=1, width=80, depth=None, *, compact=False, sort_dicts=True, underscore_numbers=False)
    #==>>pprint__pformat
from importlib import import_module
from operator import attrgetter
from collections.abc import Mapping
import sys
import re
import builtins
from itertools import islice

from seed.for_libs.for_signal import PostponeKeyboardInterrupt
    # ++kw:to_postpone_KeyboardInterrupt_until_yield => flush4print

# ++kw:to_show_total_timedelta

# ++kw:to_show_timedelta
# ++kw:may_prompt_string6resting
# ++kw:may_args4PeriodicToilLeisureTime
from seed.for_libs.for_time import timer__print_err__thread_wide as timer
#   with postpone, timer(prefix=f'{n}', _to_show_=_to_show_, _show_hint_on_enter_=True):
from seed.for_libs.for_time import PeriodicToilLeisureTime, mkr4try_resting_
#def mkr4try_resting_(*, may_prompt_string6resting, may_args4PeriodicToilLeisureTime:[None,(float,float)]):
#    '-> try_resting_/(()->None) # [may sleep_if_work_too_long_enough_]'



from seed.pkg_tools.load_module5attr import Rjstplr, rjstplr
from seed.lang.call_ import call_
from seed.func_tools.detect_depth4fail import decorator4show_py_help
from seed.helper.stable_repr import stable_repr
    #def stable_repr(obj, *, indent:str='    ', depth:int=-1, maybe_max_depth:[None, int]=None, has_head_eol_when_indent:bool=True):
    #==>> regex'stable_repr__[TF]__i\d+(__d\d+)?'
    #   _match__stable_repr_regex(nm) -> kwds4stable_repr
    # stable_repr__F__i1__d3/stable_repr__T__i1__d3
from seed.helper.stable_repr import stable_repr__expand_all_layer
from seed.helper.stable_repr import stable_repr__expand_all_layer__noindent
from seed.helper.stable_repr import stable_repr__expand_top_layer
#from seed.helper.safe_eval import safe_eval, safe_exec
from seed.helper.safe_eval import safe_eval_ex as safe_eval, safe_exec_ex as safe_exec
    #@20250118: ++kw:using_extended_globals
from seed.tiny import mk_tuple, check_type_is, check_type_le, check_callable, ifNone, echo
from seed.text.useful_regex_patterns import nm__pattern, qnm__pattern
    #nm__pattern = r'(?:(?!\d)\w+)'
    #qnm__pattern = fr'(?:{nm__pattern}(?:[.]{nm__pattern})*)'
___end_mark_of_excluded_global_names__0___ = ...

#qnm_as__pattern = r'(?:(?P<qnm>\w[\w.]*(?<![.]))(?P<qnm_as>@\w*)?)'
#   named pattern duplicated below
#   re.error: redefinition of group name 'qnm' as group 7; was group 5 at position 129
#qnm_as__pattern = r'(?:(?:\w[\w.]*(?<![.]))(?:@\w*)?)'
#   err: %0
#   err: %x..y

qnm_as__pattern = fr'(?:{qnm__pattern}(?:@{nm__pattern}?)?)'
smay_qnm_as__pattern = fr'(?:{qnm__pattern}?(?:@{nm__pattern}?)?)'
import_pattern = fr'(?:%%:@(?P<rjstplr>{nm__pattern})|%(?P<pkg_as>{smay_qnm_as__pattern})(?:(?P<from_import>[:])(?P<ls4import>(?:{qnm_as__pattern}(?:,{qnm_as__pattern})*)?))?)'##++smay_qnm_as__pattern
    # %xxx.yyy:aaa.bbb,ddd.eee@ccc
        #import the name "aaa", "ccc"
    # %xxx.yyy@:aaa.bbb@
        #import the name "yyy", "bbb"
    # %xxx.yyy
        #import the name "xxx" not "yyy"
    # %xxx.yyy:
        #load and check exists only, import nothing
    # %xxx.yyy@:
    # %xxx.yyy@
        #import the name "yyy" not "xxx"
    # %xxx.yyy@zzz:
    # %xxx.yyy@zzz
        #import the name "zzz"
    #
    # news:
    # %%:@zzz
    #   <==> %seed.pkg_tools.load_module5attr:rjstplr
    #   <==> from seed.pkg_tools.load_module5attr import rjstplr as zzz
    #

arg_pattern = r'(?:(?P<pos_or_kw>(?P<sgl_or_ls>[-][-]|[+][+])(?P<kw_nm>[^:=+-]+))?(?P<str_or_expr>[:=].*)|(?P<off_or_on>[-]|[+])(?P<flag_nm>[^:=+-]+))'
    #positional:
    # :xxxx
    # =xxxx
    #
    #keyword:
    # --aaa:xxxx
    # --aaa=xxxx
    #
    #keyword.append:
    # ++aaa:xxxx
    # ++aaa=xxxx
    #
    #boolean-flag
    # -aaa
    # +aaa
    #
#bug:re.DOTALL:arg_regex = re.compile(arg_pattern)
#
arg_regex = re.compile(arg_pattern, re.DOTALL)
import_regex = re.compile(import_pattern)
    #see:adhoc_argparse__import





_stable_repr_regex = re.compile(r'stable_repr__([FT])__i(\d+)(__d(\d+))?')
    #stable_repr => stable_repr__F__i1__d3/stable_repr__T__i1__d3
def _match__stable_repr_regex(s, /):
    '-> kwds4stable_repr'
    m = _stable_repr_regex.fullmatch(s)
    if m is None:
        return
    gs = m.groups()
    assert len(gs) == 4, (len(gs), gs)
    has_head_eol_when_indent = bool('FT'.index(gs[0]))
    indent = ' '*int(gs[1])
    depth = 0
    if gs[2]:
        maybe_max_depth = int(gs[3])
    else:
        maybe_max_depth = None
    kwds4stable_repr = dict(indent=indent, depth=depth, maybe_max_depth=maybe_max_depth, has_head_eol_when_indent=has_head_eol_when_indent)
    return kwds4stable_repr

def pprint__pformat(x, /, **kwds):
    return _pprint__pformat(x, compact=True, **kwds)
def pprint__pformat_d(depth, /):
    def pprint__pformat(x, /, **kwds):
        return _pprint__pformat(x, compact=True, depth=depth, **kwds)
    return pprint__pformat
class AdhocArgParserError(Exception):pass
class AdhocArgParserError__show_help_then_exit_with_ok__found_help_flag(AdhocArgParserError):pass
class AdhocArgParserError__show_help_then_exit_with_err(AdhocArgParserError):pass
def eval_single_arg_payload(may_locals, s, /):
    if s.startswith(':'):
        v = s[1:]
    elif s.startswith('='):
        #bug:v = safe_eval(s[1:], locals=may_locals)
        #   lambda would bind __globals__ only, __closure__ is None??
        v = safe_eval(s[1:], locals=may_locals, nonlocals=...)
    else:
        raise AdhocArgParserError(f'unknown arg format: {s!r}')
    return v

def adhoc_argparser__main__subcmds(nm2main, may_argv, /):
    (subcmds, positional_args, flag2bool, keyword2arg, keyword2args) = adhoc_argparse__subcmds(may_argv)

    for nm in subcmds:
        nm2main = nm2main[nm]
    main_func = nm2main
    if not callable(main_func): raise AdhocArgParserError(subcmds)

    #bug:return main_func(*positional_args, **flag2bool, **keyword2arg, **keyword2args)
    #   eg:main_func=dir/locals/globals
    return call_(main_func, *positional_args, **flag2bool, **keyword2arg, **keyword2args)
adhoc_argparser__main = adhoc_argparser__main__subcmds



def args5may_argv(may_argv, /):
    if may_argv is None:
        args = sys.argv[1:]
    else:
        args = may_argv
    args = (*args,)
    assert all(type(s) is str for s in args)
    return args
def adhoc_argparse__subcmds(may_argv, /):
    'may [str] -> (subcmds, positional_args, flag2bool, keyword2arg, keyword2args)'
    args = args5may_argv(may_argv)
    subcmds = args[0].split('.')
    #if not subcmds: raise AdhocArgParserError
    (positional_args, flag2bool, keyword2arg, keyword2args) = adhoc_argparse__args(args[1:])
    return (subcmds, positional_args, flag2bool, keyword2arg, keyword2args)
adhoc_argparse = adhoc_argparse__subcmds






_prefix4unpack_iter = ','
_prefix4normal_call = '@'
if 0:
    _setting4using_repr = 'repr.'
    _setting4using_str = 'str.'
    _setting4using_ascii = 'ascii.'
    _setting4using_hex = 'hex.'
    _setting4not_show = 'not_show.'
    _setting4using_stable_repr = 'stable_repr.'
    _setting4using_stable_repr__expand_top_layer = 'stable_repr__expand_top_layer.'
    _setting4using_stable_repr__expand_all_layer = 'stable_repr__expand_all_layer.'
    _setting4using_stable_repr__expand_all_layer__noindent = 'stable_repr__expand_all_layer__noindent.'
    _setting4using_pprint__pformat = 'pprint__pformat.'
prefixes4func_name4adhoc_argparser__main__call = {_prefix4unpack_iter, _prefix4normal_call}

def adhoc_argparser__main__call(nm2main, may_argv, /):
    def options4argparser_func_name_to_main_func(options4argparser, func_name, /):
        if 0:
            #move to adhoc_argparse__args
            #####
            #now add "import_pattern": 『%xxx.yyy@zzz:aaa.bbb,ccc.ddd@,e.f@g』
            adhoc_argparse__import
        else:
            if options4argparser: raise AdhocArgParserError(NotImplementedError(options4argparser))
        main_func = nm2main[func_name]
        return main_func
    return _framework4adhoc_argparser__main__call(options4argparser_func_name_to_main_func, may_argv)
#def____adhoc_argparser__main__call8module
def adhoc_argparser__main__call8module(may_argv, /):
    def options4argparser_func_name_to_main_func(options4argparser, func_name, /):
        if not len(options4argparser)==1: raise AdhocArgParserError(NotImplementedError(options4argparser))
        [smay_module_qname] = options4argparser
        check_type_is(str, smay_module_qname)
        module_qname = smay_module_qname if smay_module_qname else 'builtins'
        module = import_module(module_qname)
        main_func = getattr(module, func_name)
        return main_func
    return _framework4adhoc_argparser__main__call(options4argparser_func_name_to_main_func, may_argv)

def _postprocess4framework4adhoc_argparser__main__call(options4argparser, /):
    def _mk_postprocess_ex(*, lineno=None, end4print=None, flush4print=False, to_postpone_KeyboardInterrupt_until_yield=False, prompt_string4postpone_KeyboardInterrupt_until_yield=None, may_prompt_string6resting=None, may_args4PeriodicToilLeisureTime:[None,(float,float)]=None, to_show_timedelta=False, to_show_StopIteration_value=False, to_show_total_timedelta=False, smay_kwd4supply_func4resting=''):
        ######################
        check_type_is(str, smay_kwd4supply_func4resting)
        if smay_kwd4supply_func4resting:dict(**{smay_kwd4supply_func4resting:1})
        ######################
        check_type_is(bool, to_show_total_timedelta)
        ######################
        check_type_is(bool, to_show_StopIteration_value)
        ######################
        check_type_is(bool, to_show_timedelta)
        try_resting_ = mkr4try_resting_(may_prompt_string6resting=may_prompt_string6resting, may_args4PeriodicToilLeisureTime=may_args4PeriodicToilLeisureTime)
        try_resting_, to_show_timedelta
        ######################
        check_type_is(bool, flush4print)
        check_type_is(bool, to_postpone_KeyboardInterrupt_until_yield)
        if None is prompt_string4postpone_KeyboardInterrupt_until_yield:
            prompt_string4postpone_KeyboardInterrupt_until_yield = '\n\n... postpone_KeyboardInterrupt_until_yield ...\n\n'
        else:
            to_postpone_KeyboardInterrupt_until_yield = True
        check_type_is(str, prompt_string4postpone_KeyboardInterrupt_until_yield)
        # ++kw:prompt_string4postpone_KeyboardInterrupt_until_yield => to_postpone_KeyboardInterrupt_until_yield
        if to_postpone_KeyboardInterrupt_until_yield:
            flush4print = True
        # ++kw:to_postpone_KeyboardInterrupt_until_yield => flush4print
        ######################
        postpone = PostponeKeyboardInterrupt(whether_turnoff:=not to_postpone_KeyboardInterrupt_until_yield, may_prompt_string=prompt_string4postpone_KeyboardInterrupt_until_yield)
        ######################
        if end4print is None:
            may_end4print = None
        else:
            if type(end4print) is bool:
                end4print = '' if not end4print else '\n'
            check_type_is(str, end4print)
            may_end4print = end4print
        may_end4print
        ######################
        if type(lineno) is bool:
            #lineno = None if not lineno else 0
            lineno = int(lineno)
        #xxx:may be None:check_type_is(int, lineno)
        ######################
        if lineno is None:
            def _postprocess(*, lineno):
                pass
        else:
            check_type_is(int, lineno)
            offset = lineno
            def _postprocess(*, lineno):
                lineno += offset
                print(lineno, end=':')
                pass
        #@20250404:++kw:smay_kwd4supply_func4resting
        return (_postprocess, may_end4print, flush4print, postpone, try_resting_, to_show_timedelta, to_show_StopIteration_value, to_show_total_timedelta, smay_kwd4supply_func4resting)
        #@20250129: ++kw:to_postpone_KeyboardInterrupt_until_yield ++kw:prompt_string4postpone_KeyboardInterrupt_until_yield => to_postpone_KeyboardInterrupt_until_yield
        return (_postprocess, may_end4print, flush4print, postpone, try_resting_, to_show_timedelta, to_show_StopIteration_value, to_show_total_timedelta)
        #@20250118: ++kw:flush4print
        return (_postprocess, may_end4print, flush4print)
        return (_postprocess, may_end4print)
        return _postprocess

    #raise Exception(options4argparser)
    #if options4argparser[0] == '{':
    if options4argparser and options4argparser[0] == '{':
        j = options4argparser.index('}')
        args4postprocess = options4argparser[1:j]
        options4argparser = options4argparser[j+1:]
    else:
        args4postprocess = []
        options4argparser
    (positional_args, flag2bool, keyword2arg, keyword2args) = adhoc_argparse__args(args4postprocess)
    _mk_postprocess_ex
    (_postprocess, may_end4print, flush4print, postpone, try_resting_, to_show_timedelta, to_show_StopIteration_value, to_show_total_timedelta, smay_kwd4supply_func4resting) = decorator4show_py_help(_mk_postprocess_ex)(*positional_args, **flag2bool, **keyword2arg, **keyword2args)
    return (_postprocess, may_end4print, flush4print, postpone, try_resting_, to_show_timedelta, to_show_StopIteration_value, to_show_total_timedelta, smay_kwd4supply_func4resting, options4argparser)

def _framework4adhoc_argparser__main__call(options4argparser_func_name_to_main_func, may_argv, /):
  if 1:
    try:
        ((options4argparser, (prefix, payload4prefix, func_name), args4call), (positional_args, flag2bool, keyword2arg, keyword2args)) = adhoc_argparse__call(prefixes4func_name4adhoc_argparser__main__call, may_argv)
    except AdhocArgParserError__show_help_then_exit_with_err as e:
        print(repr(e))
        show_help();exit(1);
    except AdhocArgParserError__show_help_then_exit_with_ok__found_help_flag:
        show_help();exit(0);

    (_postprocess, may_end4print, flush4print, postpone, try_resting_, to_show_timedelta, to_show_StopIteration_value, to_show_total_timedelta, smay_kwd4supply_func4resting, options4argparser) = _postprocess4framework4adhoc_argparser__main__call(options4argparser)
        # cut prefix of options4argparser
        # prefix === '{' ... '}'

    setting4prefix = _parse_payload4prefix(prefix, payload4prefix, may_end4print=may_end4print, flush4print=flush4print)
    777;postpone, try_resting_, to_show_timedelta, to_show_StopIteration_value, to_show_total_timedelta
    to_show, islice_ = setting4prefix
    if not callable(to_show):raise AdhocArgParserError
    kwds4extra = {smay_kwd4supply_func4resting:try_resting_} if smay_kwd4supply_func4resting else {}

    main_func = options4argparser_func_name_to_main_func(options4argparser, func_name)
    if not callable(main_func): raise AdhocArgParserError(func_name)
  #end-if 1:
  with timer(prefix=f'total:', _to_show_=to_show_total_timedelta, _show_hint_on_enter_=False):

    r = decorator4show_py_help(main_func)(*positional_args, **flag2bool, **keyword2arg, **keyword2args, **kwds4extra)
    r = islice_(r)
    if prefix == _prefix4normal_call:
        if r is not None:
            #with postpone:
                to_show(r)
    elif prefix == _prefix4unpack_iter:
        r = iter(r)


        #.Nothing = object()
        b_stop = False
        lineno = -1
        while not b_stop:
            lineno += 1
            try_resting_()
            with postpone, timer(prefix=f'{lineno}', _to_show_=to_show_timedelta, _show_hint_on_enter_=True):
                #.x = next(r, Nothing)
                #.if x is Nothing:break
                try:
                    x = next(r)
                except StopIteration as e:
                    ev = e.value
                    if not to_show_StopIteration_value: break
                    x = ev
                    b_stop = True
                _postprocess(lineno=lineno)
                to_show(x)
            #end-with postpone:
                # ^KeyboardInterrupt@__exit__ if any && not whether_turnoff
        #######
        #.with postpone:
        #.    for lineno, x in enumerate(r):
        #.        ...
        #.        postpone.exit_then_enter()
        #######
        #.r = iter(r)
        #.it = enumerate(r)
        #.while 1:
        #.    with postpone:
        #.        for lineno, x in it:
        #.            _postprocess(lineno=lineno)
        #.            to_show(x)
        #.            break
        #.    #end-with postpone:
        #.        # ^KeyboardInterrupt@__exit__ if any && not whether_turnoff
        #######
    else:
        raise Exception(f'logic-err:unknown prefix: {prefix!r}')

    return None
        #return r #meaningless since run out iterator when print
  #end-with timer(prefix=f'total:', _to_show_=to_show_total_timedelta, _show_hint_on_enter_=False):

def show_help():
    print(r'''
py_adhoc_call =[def]=:
    py -m nn_ns.app.adhoc_argparser__main__call8module "$@"

to show this help:
    py_adhoc_call    --help
    py_adhoc_call    -h
    py_adhoc_call

to call xxx.yyy::g()
    py_adhoc_call    xxx.yyy  @g
    py_adhoc_call    xxx.yyy  ,g

usage:
py_adhoc_call    xxx.yyy  @g =1 :2 --p=3 ++ls=4 ++ls:5 -f +t
    <==> from xxx.yyy import g; print(repr(g(1,'2',p=3,ls=[4,'5'],f=False,t=True)))

#『repr』-->『not_show/stable_repr/stable_repr__expand_top_layer/stable_repr__expand_all_layer/stable_repr__expand_all_layer__noindent/pprint__pformat』/py.__builtins__.『repr/str/hex/ascii/...』
py_adhoc_call    xxx.yyy  @not_show.g
    <==> from xxx.yyy import g; g()
py_adhoc_call    xxx.yyy  @hex.g
    <==> from xxx.yyy import g; print(hex(g()))

#『@』-->『,』
py_adhoc_call    xxx.yyy  ,g
    <==> from xxx.yyy import g; for r in g():print(repr(r))

#import
py_adhoc_call    xxx.yyy  @g  %qqq.ppp@:a.b,c.d@,s.t@u  '=(ppp,a,d,u)'
    <==> from xxx.yyy import g; import qqq.ppp as ppp; from qqq.ppp import a,c,s;a.b;d=c.d;u=s.t;del c,s;print(repr(g((ppp,a,d,u))))

py_adhoc_call    xxx.yyy  @g  %%:@loader  '=loader._.math.pi'
    <==> from xxx.yyy import g; from seed.pkg_tools.load_module5attr import rjstplr as loader;print(repr(g(loader._.math.pi)))
    ~= from xxx.yyy import g; import math;print(repr(g(math.pi)))


#exec without import-support #__import__ is removed
py_adhoc_call    xxx.yyy  @g  '%!a=0xfff' =a '=a+a'
    <==> from xxx.yyy import g;a=0xfff;print(repr(g(a,a+a)))
#NOTE:『!』should be wrapped by '!' or escaped by "\!", otherwise => 『HISTORY EXPANSION』

''')#'''
help_flags = {'-h', '--help', '+h', '++help', '/h', '/help', '?', '-?', '/?'}
def is_help_flag_(s, /):
    return s.lower() in help_flags
def filter_startswith_(prefixes, s, /):
    return tuple(sorted(filter(s.startswith, prefixes)))
def adhoc_argparse__call(prefixes4func_name, may_argv, /):#, *, exit__vs__raise__vs__return=None
    '[prefix] -> may [arg] -> ((options4argparser, (prefix, func_name), args4call), (positional_args, flag2bool, keyword2arg, keyword2args))'
    #check_type_is(bool, )
    #########
    #########
    args = args5may_argv(may_argv)
    if not args:
            raise AdhocArgParserError__show_help_then_exit_with_ok__found_help_flag
    #########

    #if prefixes4func_name is None: prefixes4func_name = prefixes4func_name4adhoc_argparse__call
    prefixes4func_name = mk_tuple(prefixes4func_name)
    for i, s in enumerate(args):
        prefixes = filter_startswith_(prefixes4func_name, s)
        if prefixes:
            break
        if is_help_flag_(s):
            #return EXIT0
            #show_help();exit(0);
            raise AdhocArgParserError__show_help_then_exit_with_ok__found_help_flag
                #??? but this is not error!!
    else:
        args = [*args]
        #this is error!!: return EXIT1
        #show_help();exit(1);
        raise AdhocArgParserError__show_help_then_exit_with_err(f'not found func_name to call: prefixes4func_name={prefixes4func_name!r}::::args={args}')

    if not len(prefixes) == 1: raise Exception(f'logic-err:prefixes not mutex: {prefixes!r}')
    [prefix] = prefixes
    pseudo_func_name = s[len(prefix):]
    (payload4prefix, func_name) = _parse_pseudo_func_name(pseudo_func_name)
    if not func_name.isidentifier(): raise AdhocArgParserError(repr(func_name))
    options4argparser = args[:i]
    args4call = args[i+1:]


    (positional_args, flag2bool, keyword2arg, keyword2args) = adhoc_argparse__args(args4call)
    return ((options4argparser, (prefix, payload4prefix, func_name), args4call), (positional_args, flag2bool, keyword2arg, keyword2args))

def _parse_pseudo_func_name(pseudo_func_name, /):
    'pseudo_func_name -> (payload4prefix, func_name)'
    for ch in pseudo_func_name[::-1]:
        #bug:@末尾字符是数字:if not (ch=='_' or ch.isidentifier()):
        if not (ch=='_' or ch.isalnum()):
            i = 1+pseudo_func_name.rindex(ch)
            break
    else:
        i = 0
    func_name = pseudo_func_name[i:]
    payload4prefix = pseudo_func_name[:i]
    return (payload4prefix, func_name)
def _parse__qnm_as(s, /):
    (qnm, smay_at, smay_nm) = s.partition('@')
    qnm4check = qnm
    if smay_nm:
        as_nm = smay_nm
        qnm4obj = qnm
    elif smay_at:
        (_, _, last_nm) = qnm.rpartition('.')
        as_nm = last_nm
        qnm4obj = qnm
    else:
        (first_nm, _, _) = qnm.partition('.')
        as_nm = first_nm
        qnm4obj = first_nm
    return (qnm4check, qnm4obj, smay_at, as_nm)
def _parse__import_pattern(m, /):
    if (alias4rjstplr := m['rjstplr']):
        return {alias4rjstplr:rjstplr}

    pkg_as = m['pkg_as']
    may_from_import = m['from_import']
    #smay_ls4import = m.get('ls4import', '')
    #   AttributeError: 're.Match' object has no attribute 'get'
    may_smay_ls4import = m['ls4import']
    if 0:
        smay_ls4import = ifNone(may_smay_ls4import, '')
        qnm_as__ls = smay_ls4import.split(',')
        #bug: ''.split(',') == [''] != []
    else:
        qnm_as__ls = may_smay_ls4import.split(',') if may_smay_ls4import else []
    d = {}

    if pkg_as.startswith('@') or not pkg_as:
        ##++smay_qnm_as__pattern
        pkg_as = f'builtins{pkg_as}'
    #print(pkg_as)
    (qnm4check, qnm4obj, smay_at, as_nm) = _parse__qnm_as(pkg_as)
    module_obj4from = import_module(qnm4check)
    if smay_at or not may_from_import:
        d[as_nm] = module_obj4export = import_module(qnm4obj)
    else:
        #not import module
        #   %xxx.yyy:aaa.... #no "@" but has ":"
        pass
    for qnm_as in qnm_as__ls:
        (qnm4check, qnm4obj, smay_at, as_nm) = _parse__qnm_as(qnm_as)
        attrgetter(qnm4check)(module_obj4from)
        obj = attrgetter(qnm4obj)(module_obj4from)
        d[as_nm] = obj #permitted__overwrite!!!
    return d
def checked_fullmatch__import_pattern(s, /):
    m = import_regex.fullmatch(s)
    if m is None:
        raise ValueError(f'not satisfy import_pattern:『%xxx.yyy@zzz:aaa.bbb,ccc.ddd@,e.f@g』:{s!r}')
    return m
def adhoc_argparse__import(strs, /):
    # "import_pattern": 『%xxx.yyy@zzz:aaa.bbb,ccc.ddd@,e.f@g』|『%%:@zzz』
    #   see:rjstplr
    def import_(d, m, /):
        _d = _parse__import_pattern(m)
        d.update(_d) #permitted__overwrite!!!
    strs = [*strs]
    ms = [checked_fullmatch__import_pattern(s) for s in strs]
    ##check all, then load
    d = {}
    for m in ms:
        import_(d, m)
    return d

def _not_show(x, /):pass
def _dump8show(x, /):
    #check_type_is(bytes, x)
    import sys
    sys.stdout.buffer.write(x)
def _pickle_dump8show(x, /):
    import sys
    import pickle
    pickle.dump(x, sys.stdout.buffer)
def _mk__to_show(to_str, /, *, may_end4print, flush4print:bool):
    if not callable(to_str):raise logic-err
    #if not callable(to_str):raise AdhocArgParserError
    def to_show(x, /):
        print(to_str(x), end=may_end4print, flush=flush4print)
    return to_show

_payload4prefix__regex = re.compile(r'(?P<nm>(?:\w+[.])?)(?P<num4islice>(?:\d+[:])?)')
def _parse_payload4prefix(prefix, payload4prefix, /, *, may_end4print, flush4print):
    'prefix -> payload4prefix -> setting4prefix'
    check_type_is(str, payload4prefix)
    m = _payload4prefix__regex.fullmatch(payload4prefix)
    if m is None:
        raise AdhocArgParserError(payload4prefix)
    smay_nm_dot = m['nm']
    smay_num4islice_colon = m['num4islice']
    if not smay_num4islice_colon:
        islice_ = echo
    else:
        num4islice = int(smay_num4islice_colon[:-1])
        if prefix == ',':
            def islice_(r, /):
                it = r
                return islice(it, num4islice)
        elif prefix == '@':
            def islice_(r, /):
                ls = r
                try:
                    return ls[:num4islice]
                except TypeError:
                    #TypeError: 'generator' object is not subscriptable
                    #   see:above:『py_adhoc_call   script.对数纟差分倍增   @list.100:枚举冫插入位置纟小数部分纟对数纟差分倍增扌 +使用冫负对数』
                    it = r
                    assert iter(it) is it
                    #return list(islice(it, num4islice))
                    return islice(it, num4islice)
        else:
            raise AdhocArgParserError(prefix)
        islice_
    islice_


    #if payload4prefix: raise NotImplementedError
    #if payload4prefix.endswith(':'): ...
    #smay_nm_dot = payload4prefix
    to_show = _payload4prefix_smay_nm_dot2to_show(smay_nm_dot, may_end4print=may_end4print, flush4print=flush4print)
    setting4prefix = to_show, islice_
    return setting4prefix

def _payload4prefix_smay_nm_dot2to_show(smay_nm_dot, /, *, may_end4print, flush4print):
    if not smay_nm_dot:
        to_str = repr
        to_show = _mk__to_show(to_str, may_end4print=may_end4print, flush4print=flush4print)
        to_str = None
    elif not smay_nm_dot.endswith('.'):raise AdhocArgParserError(smay_nm_dot)
    else:
        nm = smay_nm_dot[:-1]
        to_show = _payload4prefix_nm2to_show(nm, may_end4print=may_end4print, flush4print=flush4print)
    return to_show
def _payload4prefix_nm2to_show(nm, /, *, may_end4print, flush4print):
    if nm == 'not_show':
        to_show = _not_show
    elif nm == 'dump8show':
        to_show = _dump8show
    elif nm == 'pickle_dump8show':
        to_show = _pickle_dump8show
    else:
        if nm == 'stable_repr':
            to_str = stable_repr
        elif nm == 'stable_repr__expand_top_layer':
            to_str = stable_repr__expand_top_layer
        elif nm == 'stable_repr__expand_all_layer':
            to_str = stable_repr__expand_all_layer
        elif nm == 'stable_repr__expand_all_layer__noindent':
            to_str = stable_repr__expand_all_layer__noindent
        elif nm == 'pprint__pformat':
            to_str = pprint__pformat
        elif nm.startswith('pprint__pformat_d'):
            depth = int(nm[len('pprint__pformat_d'):])
            to_str = pprint__pformat_d(depth)
        elif nm.startswith('stable_repr__') and (kwds4stable_repr:=_match__stable_repr_regex(nm)):
            #stable_repr__F__i1__d3/stable_repr__T__i1__d3
            to_str = lambda x,/:stable_repr(x, **kwds4stable_repr)
        elif not hasattr(builtins, nm):raise AdhocArgParserError(nm)
        else:
            to_str = getattr(builtins, nm)
        to_show = _mk__to_show(to_str, may_end4print=may_end4print, flush4print=flush4print)
        to_str = None
    return to_show

def adhoc_argparse__args(args, /, *, locals=None):
    '[str] -> (positional_args, flag2bool, keyword2arg, keyword2args)'
    return adhoc_argparse__args__ver2(locals, args)
def adhoc_argparse__args__ver2(may_locals, args, /):
    '[str] -> (positional_args, flag2bool, keyword2arg, keyword2args)'
    #ver2: add "import_pattern": 『%xxx.yyy@zzz:aaa.bbb,ccc.ddd@,e.f@g』
    adhoc_argparse__import
    if may_locals is None:
        locals = {}
    else:
        locals = may_locals
    locals; del may_locals
    check_type_le(Mapping, locals)
    def _check():
        for s in args:
            if s.startswith('%'):
                if s.startswith('%!'):
                    #py script/stmts
                    script = s[2:]
                    compile(script, '<adhoc_argparse__args__ver2:arg>', 'exec')
                else:
                    #import_pattern
                    checked_fullmatch__import_pattern(s)
    _check()

    def extra_process(may_locals, s, /):
        locals = may_locals
        consumed = s.startswith('%')
        if consumed:
            if s.startswith('%!'):
                #py script/stmts
                script = s[2:]
                #bug:safe_exec(script, locals=locals)
                #   lambda would bind __globals__ only, __closure__ is None??
                safe_exec(script, locals=locals, nonlocals=...)
            else:
                #import_pattern
                #d = adhoc_argparse__import([s])
                #locals.update(d) #permitted__overwrite!!!
                m = checked_fullmatch__import_pattern(s)
                _d = _parse__import_pattern(m)
                locals.update(_d) #permitted__overwrite!!!
        return consumed
    return adhoc_argparse__args__ver1(args, extra_process=extra_process, locals=locals)

def adhoc_argparse__args__ver1(args, /, *, extra_process=None, locals=None):
    '[str] -> (*extra_process::may (may_locals -> str->consumed/book)) -> (positional_args, flag2bool, keyword2arg, keyword2args)'
    may_locals = locals; del locals
    positional_args = []
    flag2bool = {}
    keyword2arg = {}
    keyword2args = {}
    if extra_process is None:
        def extra_process(may_locals, s, /):
            consumed = False
            return consumed
    check_callable(extra_process)

    for s in args:
        if extra_process(may_locals, s):
            continue
        m = arg_regex.fullmatch(s)
        if not m:
            raise AdhocArgParserError(f'bad arg fmt: {s!r}')
        #may_arg_payload = m.get('str_or_expr')
        may_arg_payload = m['str_or_expr']
        if may_arg_payload is None:
            # flag
            flag_nm = m['flag_nm']
            off_or_on = m['off_or_on']
            off_or_on = '-+'.index(off_or_on)
            off_or_on = bool(off_or_on)
            if flag_nm in flag2bool: raise AdhocArgParserError(f'duplicated flag: {flag_nm!r}')
            flag2bool[flag_nm] = off_or_on
        else:
            arg_payload = may_arg_payload
            v = eval_single_arg_payload(may_locals, arg_payload)
            #if not m.get('pos_or_kw'):
            if not m['pos_or_kw']:
                positional_args.append(v)
            else:
                #kw
                #kw_nm = m.get('kw_nm')
                #sgl_or_ls = m.get('sgl_or_ls')
                kw_nm = m['kw_nm']
                sgl_or_ls = m['sgl_or_ls']
                sgl_or_ls = ('--', '++').index(sgl_or_ls)
                sgl_or_ls = bool(sgl_or_ls)
                if sgl_or_ls:
                    #append
                    ls = keyword2args.setdefault(kw_nm, [])
                    ls.append(v)
                else:
                    if kw_nm in keyword2arg: raise AdhocArgParserError(f'duplicated keyword: {kw_nm!r}')
                    keyword2arg[kw_nm] = v
    return (positional_args, flag2bool, keyword2arg, keyword2args)


#print(adhoc_argparse__subcmds('a.bb.ccc :0 =11 --d:2 ++ee:33 ++ee=444 -f +gg'.split()))
assert (adhoc_argparse__subcmds('a.bb.ccc :0 =11 --d:2 ++ee:33 ++ee=444 -f +gg'.split()) == (['a', 'bb', 'ccc'], ['0', 11], {'f': False, 'gg': True}, {'d': '2'}, {'ee': ['33', 444]}))


def _test1__at():
    return '999   777'
def _test2__start():
    yield '555   333'
    yield 444

def _fwd_call_(f, /, *args, **kwds):
    return f(*args, **kwds)
def _NOP_():pass #nop:no-op:无操作:用于 adhoc_argparser__main__subcmds

if __name__ == "__main__":
    from seed.recognize.cmdline.adhoc_argparser import adhoc_argparser__main__call, AdhocArgParserError, _NOP_
    adhoc_argparser__main__call(globals(), None)
        #main()

