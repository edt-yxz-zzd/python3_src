r'''
py -m nn_ns.app.py_eval
py -m nn_ns.app.debug_cmd   nn_ns.app.py_eval

######################
py -c 'print(hex(333))'
0x14d

######################
echo $[3 + 7]  $[2 ** 3]  $[2 ^ 3]
10 8 1

######################
echo -e 'a\nb'
a
b

######################
py -m nn_ns.app.py_eval -i 'hex(333)' '3 + 7' '2 ** 3' '2 ^ 3'
'0x14d'
10
8
1

######################
py_eval -i 1 -i 2 3
1
2
3


######################
py_eval --postprocess 'hex' -i '333'
'0x14d'

py_eval --preprocess 'lambda s:"0x"+s' -i '333'
819

py_eval  --startup 'from builtins import hex as h'   -i 'h(333)'
'0x14d'

py_eval --preprocess 'lambda s:"0x"+s'  --postprocess 'hex' -i '333'
'0x333'

py_eval  --startup 'from builtins import hex as h'   --preprocess 'lambda s:"0x"+s'    --postprocess 'h' -i '333'
'0x333'



py_eval --preprocess repr -i 'a\nb'
'a\\nb'

py_eval --preprocess '"\"{}\"".format'  -i 'a\nb'
'a\nb'

py_eval --preprocess '"\"{}\"".format'  -i 'a\nb' --turnoff_repr
a
b

py_eval -i '{2:4,1:3}'
{2: 4, 1: 3}

py_eval -i '{2:4,1:3}' --stable_repr
{1: 3, 2: 4}


py_eval -i '{2:4,1:3}' --turnoff_eval
'{2:4,1:3}'


py_eval -i '{2:4,1:3}' --literal_eval
{2: 4, 1: 3}

py_eval -i 'set()' --literal_eval
ValueError: malformed node or string: <_ast.Call object at 0xb64827d8>

py_eval -i 'set()'
set()

py_eval -i 'eval("1")'
NameError: name 'eval' is not defined

py_eval -i 'eval("1")' --turnoff_safe4eval
1


py_literal_eval -i '{2:4,1:3}'
{2: 4, 1: 3}

py_literal_eval -i 'set()'
ValueError: malformed node or string: <_ast.Call object at 0xb64827d8>











e ../../python3_src/nn_ns/app/py_eval.py
    #e ../../python3_src/nn_ns/app/hex.py
e ../../python3_src/bash_script/app/py_eval
py -m nn_ns.app.py_eval -i "$@"
e ../../python3_src/bash_script/app/hex
py -m nn_ns.app.py_eval --postprocess 'hex' -i "$@"
e ../../python3_src/bash_script/app/py_literal_eval
py -m nn_ns.app.py_eval --literal_eval -i "$@"















 importlib.import_module(name, package=None)

#'''

from seed.func_tools.fmapT.fmapT__tiny import fmapT__list, fmapT__tuple
from seed.helper.safe_eval import safe_eval
from seed.helper.stable_repr import stable_repr
import re
from pathlib import Path
from sys import stdin
from ast import literal_eval

assert '0x14d' == hex(333)
assert 819 == (0x333)

if 0:
    def eval_then_show(expr, /, *, fout):
        print(safe_eval(expr), file=fout)
else:
    def eval_then_show(locals_, preprocess_fs, postprocess_fs, expr, /, *, fout, to_txt, main_action):
        for f in reversed(preprocess_fs):
            expr = f(expr)

        x = main_action(expr, locals=locals_)

        for f in iter(postprocess_fs):
            x = f(x)

        print(to_txt(x), file=fout)



def echo4main_action(expr, /, *, locals):
    return expr
def literal_eval4main_action(expr, /, *, locals):
    return literal_eval(expr)
def unsafe_eval4main_action(expr, /, *, locals):
    return eval(expr, locals, locals)
def safe_eval4main_action(expr, /, *, locals):
    return safe_eval(expr, locals=locals)

class _4main:
    def __init__(sf, /, *, iencoding):
        sf._may_txt4stdin__cache = []
        sf.iencoding = iencoding
    def arg2txt__unescape(sf, arg, /):
        if arg.startswith('!@'):
            path = Path(arg[2:])
            txt = path.read_text(encoding=sf.iencoding)
        elif arg.startswith('!:'):
            txt = arg[2:]
        elif arg == '!-stdin-!':
            _may_txt4stdin__cache = sf._may_txt4stdin__cache
            while not _may_txt4stdin__cache:
                txt = stdin.read()
                _may_txt4stdin__cache.append(txt)
            [txt] = _may_txt4stdin__cache
        elif arg.startswith('!'):
            raise ValueError(f'arg in ill-form: {arg!r}')
        else:
            txt = arg
        return txt

    def unescape4eval(sf, /, *lslsls):
        f = fmapT__list(fmapT__list(fmapT__list(sf.arg2txt__unescape)))
        return f(lslsls)

    def prepare4eval(sf, startup_lsls, preprocess_lsls, postprocess_lsls, /):
        (startup_lsls, preprocess_lsls, postprocess_lsls) = sf.unescape4eval(startup_lsls, preprocess_lsls, postprocess_lsls)
        locals_ = {}

        setup4eval(locals_, startup_lsls)
        (preprocess_fs, postprocess_fs) = eval_lslsls(locals_, preprocess_lsls, postprocess_lsls)
        #print(postprocess_fs)
        if not all(map(callable, preprocess_fs)): raise TypeError
        if not all(map(callable, postprocess_fs)): raise TypeError
        return (locals_, preprocess_fs, postprocess_fs)

def eval_lslsls(locals_, /, *lslsls):
    def _eval(txt, /):
        return eval(txt, locals_, locals_)
    f = fmapT__list(fmapT__list(fmapT__list(_eval)))
    lslsls = f(lslsls)
    ######################
    #concat/join
    lsls = [[] for _ in lslsls]
    g = fmapT__tuple(*[fmapT__list(ls.extend) for ls in lsls])
    g(lslsls)
    fss = lsls
    return fss
def setup4eval(locals_, startup_lsls, /):
    #unescaped startup_lsls
    def _exec(txt, /):
        exec(txt, locals_, locals_)
    f = (fmapT__list(fmapT__list(_exec)))
    f(startup_lsls)



def _test():
    locals_ = {}
    __import__('seed.helper.safe_eval', locals_, locals_, ['safe_eval'], level=0)
        #from py_doc::level specifies whether to use absolute or relative imports. 0 (the default) means only perform absolute imports.
    #assert locals_['safe_eval'] is safe_eval
        #KeyError!!!
    assert not locals_
_test()

r'''[[[
def _mk_rex():
    # (?:)
    name = r'(?:\w+)'
    qname = fr'(?:{name}(?:[.]{name})*)'
    as_name = fr'(?:[@]{name})'
    pkg = fr'(?:{qname}{as_name}?)'
    var = fr'(?:{name}{as_name}?)'
    var_list = fr'(?:[:][:]{var}(?:[,]{var})*)'

    import_request = fr'(?:{pkg}{var_list}?)'
    import_request__rex = re.compile(import_request)
    return import_request__rex
import_request__rex = _mk_rex()

def handle_import_request(env, import_request, /, *, encoding):
    if import_request.startswith('!'):
        if import_request.startswith('!:'):
            # immediate startup script
            startup_script = import_request[2:]
        elif import_request.startswith('!@'):
            path4startup_script = import_request[2:]
            path4startup_script = Path(path4startup_script)
            startup_script = path4startup_script.read_text(encoding=encoding)
        else:
            raise ValueError(f'import_request in bad-form: {import_request!r}')
        startup_script
        exec(startup_script, env, env)
        return

    m = import_request__rex.fullmatch(import_request)
    if m is None:
        raise ValueError(f'import_request in bad-form: {import_request!r}')
    pkg_as, _, may_vs = import_request.partition('::')
    pkg, _, may_pkg_alias = pkg_as.partition('@')

    var_alias_pairs = []
    if not may_vs:
        #var_alias_pairs = []
        pass
    else:
        var_as__ls = may_vs.split(',')
        for var_as in var_as__ls:
            var, _, may_var_alias = var_as.partition('@')
            var_alias = may_var_alias if may_var_alias else var
            var_alias_pairs.append((var, var_alias))
    ######################
    var_alias_pairs
    pkg, may_pkg_alias
    ######################
    ...
def import4eval(import_stmtss, /):
    'import into locals to eval python expression; fmt=xxx.yyy.zzz or fmt=xxx.yyy.zzz@newzzz::aaa,bbb,ccc@newccc or fmt="!:py-script-as-startup-setting" or fmt="!@file-path-for-py-script-as-startup-setting"')
    if 
    locals_ = {}
    ...
    return locals_
#]]]'''






def main(args=None, /):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description='python eval and print result'
        , epilog=r'''
arg:
    [arg not startswith "!"]
        => [arg is raw-text]
    [arg startswith "!:"]
        => [arg[2:] is raw-text]
    [arg startswith "!@"]
        => [arg is path to file contains raw-text using iencoding]
    [arg == "!-stdin-!"]
        => [arg is text from STDIN]
    [otherwise]
        => raise


#'''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    if 0:
        parser.add_argument('--imports', type=str, nargs='*', default=[], action='append'
            , help='import into locals to eval python expression; fmt=xxx.yyy.zzz or fmt=xxx.yyy.zzz@newzzz::aaa,bbb,ccc@newccc or fmt="!=py-script-as-startup-setting" or fmt="!@file-path-for-py-script-as-startup-setting"')


    parser.add_argument('--startup', type=str, nargs='*', default=[], action='append'
            , help='"py-script-as-startup-setting" or "!@file-path-for-py-script-as-startup-setting"; last arg perform last')
    parser.add_argument('--preprocess', type=str, nargs='*', default=[], action='append'
                        , help='a python expression as preprocess before eval; last arg perform first')
    parser.add_argument('--postprocess', type=str, nargs='*', default=[], action='append'
                        , help='a python expression as postprocess after eval; last arg perform last')
    parser.add_argument('--literal_eval', action='store_true'
                        , default = False
                        , help='main action be ast.literal_eval instead of eval')
    parser.add_argument('--turnoff_eval', action='store_true'
                        , default = False
                        , help='main action be echo instead of eval')
    parser.add_argument('--turnoff_safe4eval', action='store_true'
                        , default = False
                        , help='main action be unsafe_eval instead of safe_eval')

    parser.add_argument('--stable_repr', action='store_true'
                        , default = False
                        , help='output result by stable_repr(result)')
    parser.add_argument('--turnoff_repr', action='store_true'
                        , default = False
                        , help='output result by str(result)')
    parser.add_argument('-i', '--input', type=str, nargs='*', default=[], action='append'
                        , help='input python expression')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-ie', '--iencoding', type=str
                        , default='utf8'
                        , help='input file encoding')
    parser.add_argument('-oe', '--oencoding', type=str
                        , default='utf8'
                        , help='output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    iencoding = args.iencoding
    oencoding = args.oencoding
    omode = 'wt' if args.force else 'xt'

    #may_ifname = args.input
    #with may_open_stdin(may_ifname, 'rt', encoding=iencoding) as fin:

    #import_stmtss = args.imports
    startup_lsls = args.startup
    preprocess_lsls = args.preprocess
    postprocess_lsls = args.postprocess
    (locals_, preprocess_fs, postprocess_fs) = _4main(iencoding=iencoding).prepare4eval(startup_lsls, preprocess_lsls, postprocess_lsls)

    if args.turnoff_eval:
        main_action = echo4main_action
    elif args.literal_eval:
        main_action = literal_eval4main_action
    elif args.turnoff_safe4eval:
        main_action = unsafe_eval4main_action
    else:
        main_action = safe_eval4main_action

    if args.turnoff_repr:
        to_txt = str
    elif args.stable_repr:
        to_txt = stable_repr
    else:
        to_txt = repr

    exprss = args.input
    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=oencoding) as fout:
        for exprs in exprss:
            for expr in exprs:
                if 0:
                    eval_then_show(expr, fout=fout)
                else:
                    eval_then_show(locals_, preprocess_fs, postprocess_fs, expr, fout=fout, to_txt=to_txt, main_action=main_action)

if __name__ == "__main__":
    main()


