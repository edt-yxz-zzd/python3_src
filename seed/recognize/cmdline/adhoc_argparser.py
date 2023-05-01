#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/cmdline/adhoc_argparser.py

see:py_all@bash_script
    py_adhoc_call ''  ,str.list '%difflib:__all__@all' =all

[[
TODO:选项:添加:『+lineno』:『,』枚举时附加行号
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
     |stable_repr

?新增『+lineno』:
    or函数名之前的选项:
        xxx.yyy +lineno ,f
    or模块名之前的选项:
        +lineno xxx.yyy ,f
        def____adhoc_argparser__main__call8module.options4argparser_func_name_to_main_func.options4argparser 处理的是 模块名之后~函数名之前 的选项！

新增:
    %!<py_script>
        safe_exec(script)
新增:
    %...  import ...
    %...:...  from ... import ...
    %...:new=old,xx,yy  from ... import old as new, xx, yy
    ----or:
    _.pkg.xxx().obj.yyy

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

from importlib import import_module
from operator import attrgetter
from collections.abc import Mapping
import sys
import re
import builtins

from seed.lang.call_ import call_
from seed.func_tools.detect_depth4fail import decorator4show_py_help
from seed.helper.stable_repr import stable_repr
from seed.helper.safe_eval import safe_eval, safe_exec
from seed.tiny import mk_tuple, check_type_is, check_type_le, check_callable, ifNone
from seed.text.useful_regex_patterns import nm__pattern, qnm__pattern
    #nm__pattern = r'(?:(?!\d)\w+)'
    #qnm__pattern = fr'(?:{nm__pattern}(?:[.]{nm__pattern})*)'

#qnm_as__pattern = r'(?:(?P<qnm>\w[\w.]*(?<![.]))(?P<qnm_as>@\w*)?)'
#   named pattern duplicated below
#   re.error: redefinition of group name 'qnm' as group 7; was group 5 at position 129
#qnm_as__pattern = r'(?:(?:\w[\w.]*(?<![.]))(?:@\w*)?)'
#   err: %0
#   err: %x..y

qnm_as__pattern = fr'(?:{qnm__pattern}(?:@{nm__pattern}?)?)'
smay_qnm_as__pattern = fr'(?:{qnm__pattern}?(?:@{nm__pattern}?)?)'
import_pattern = fr'(?:%(?P<pkg_as>{smay_qnm_as__pattern})(?:(?P<from_import>[:])(?P<ls4import>(?:{qnm_as__pattern}(?:,{qnm_as__pattern})*)?))?)'##++smay_qnm_as__pattern
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

def _framework4adhoc_argparser__main__call(options4argparser_func_name_to_main_func, may_argv, /):
    try:
        ((options4argparser, (prefix, payload4prefix, func_name), args4call), (positional_args, flag2bool, keyword2arg, keyword2args)) = adhoc_argparse__call(prefixes4func_name4adhoc_argparser__main__call, may_argv)
    except AdhocArgParserError__show_help_then_exit_with_err as e:
        print(repr(e))
        show_help();exit(1);
    except AdhocArgParserError__show_help_then_exit_with_ok__found_help_flag:
        show_help();exit(0);


    setting4prefix = _parse_payload4prefix(prefix, payload4prefix)
    to_show = setting4prefix
    if not callable(to_show):raise AdhocArgParserError

    main_func = options4argparser_func_name_to_main_func(options4argparser, func_name)
    if not callable(main_func): raise AdhocArgParserError(func_name)

    r = decorator4show_py_help(main_func)(*positional_args, **flag2bool, **keyword2arg, **keyword2args)
    if prefix == _prefix4normal_call:
        if r is not None:
            to_show(r)
    elif prefix == _prefix4unpack_iter:
        for x in r:
            to_show(x)
    else:
        raise Exception(f'logic-err:unknown prefix: {prefix!r}')

    return None
        #return r #meaningless since run out iterator when print

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

#『repr』-->『not_show/stable_repr』/py.__builtins__.『repr/str/hex/ascii/...』
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
    # "import_pattern": 『%xxx.yyy@zzz:aaa.bbb,ccc.ddd@,e.f@g』
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
def _mk__to_show(to_str, /):
    if not callable(to_str):raise logic-err
    #if not callable(to_str):raise AdhocArgParserError
    def to_show(x, /):
        print(to_str(x))
    return to_show
def _parse_payload4prefix(prefix, payload4prefix, /):
    'prefix -> payload4prefix -> setting4prefix'
    check_type_is(str, payload4prefix)
    #if payload4prefix: raise NotImplementedError
    if not payload4prefix:
        to_str = repr
        to_show = _mk__to_show(to_str)
        to_str = None
    elif not payload4prefix.endswith('.'):raise AdhocArgParserError
    else:
        nm = payload4prefix[:-1]
        if nm == 'not_show':
            to_show = _not_show
        else:
            if nm == 'stable_repr':
                to_str = stable_repr
            elif not hasattr(builtins, nm):raise AdhocArgParserError
            else:
                to_str = getattr(builtins, nm)
            to_show = _mk__to_show(to_str)
            to_str = None
    setting4prefix = to_show
    return setting4prefix

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

