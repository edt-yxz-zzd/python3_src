r'''[[[
e ../../python3_src/seed/recognize/cmdline/adhoc_argparser.py

seed.recognize.cmdline.adhoc_argparser
py -m nn_ns.app.debug_cmd   seed.recognize.cmdline.adhoc_argparser

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



#]]]'''
__all__ = '''
    adhoc_argparse__args
        adhoc_argparse__subcmds
            adhoc_argparser__main__subcmds
        adhoc_argparse__call
            adhoc_argparser__main__call

    AdhocArgParserError
    _NOP_
    '''.split()
    #adhoc_argparser__main
    #adhoc_argparse
    #eval_single_arg_payload

import sys
import re
from seed.helper.safe_eval import safe_eval
from seed.tiny import mk_tuple

arg_pattern = r'(?:(?P<pos_or_kw>(?P<sgl_or_ls>[-][-]|[+][+])(?P<kw_nm>[^:=+-]+))?(?P<str_or_expr>[:=].*)|(?P<off_or_on>[-]|[+])(?P<flag_nm>[^:=+-]+))'
arg_regex = re.compile(arg_pattern)

class AdhocArgParserError(Exception):pass
def eval_single_arg_payload(s, /):
    if s.startswith(':'):
        v = s[1:]
    elif s.startswith('='):
        v = safe_eval(s[1:])
    else:
        raise AdhocArgParserError(f'unknown arg format: {s!r}')
    return v

def adhoc_argparser__main__subcmds(nm2main, may_argv, /):
    (subcmds, positional_args, flag2bool, keyword2arg, keyword2args) = adhoc_argparse__subcmds(may_argv)

    for nm in subcmds:
        nm2main = nm2main[nm]
    main_func = nm2main
    if not callable(main_func): raise AdhocArgParserError(subcmds)

    return main_func(*positional_args, **flag2bool, **keyword2arg, **keyword2args)
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
prefixes4func_name4adhoc_argparser__main__call = {_prefix4unpack_iter, _prefix4normal_call}
def adhoc_argparser__main__call(nm2main, may_argv, /):
    ((options4argparser, (prefix, func_name), args4call), (positional_args, flag2bool, keyword2arg, keyword2args)) = adhoc_argparse__call(prefixes4func_name4adhoc_argparser__main__call, may_argv)

    if options4argparser: raise AdhocArgParserError(NotImplementedError(options4argparser))

    main_func = nm2main[func_name]
    if not callable(main_func): raise AdhocArgParserError(func_name)

    r = main_func(*positional_args, **flag2bool, **keyword2arg, **keyword2args)
    if prefix == _prefix4normal_call:
        if r is not None:
            print(repr(r))
    elif prefix == _prefix4unpack_iter:
        for x in r:
            print(repr(x))
    else:
        raise Exception(f'logic-err:unknown prefix: {prefix!r}')

    return None
        #return r #meaningless since run out iterator when print

def filter_startswith_(prefixes, s, /):
    return tuple(sorted(filter(s.startswith, prefixes)))
def adhoc_argparse__call(prefixes4func_name, may_argv, /):
    '[prefix] -> may [arg] -> ((options4argparser, (prefix, func_name), args4call), (positional_args, flag2bool, keyword2arg, keyword2args))'
    args = args5may_argv(may_argv)
    #if prefixes4func_name is None: prefixes4func_name = prefixes4func_name4adhoc_argparse__call
    prefixes4func_name = mk_tuple(prefixes4func_name)
    for i, s in enumerate(args):
        prefixes = filter_startswith_(prefixes4func_name, s)
        if prefixes:
            break
    else:
        raise AdhocArgParserError(NotImplementedError('not found func_name to call: prefixes4func_name={prefixes4func_name!r}'))
    if not len(prefixes) == 1: raise Exception(f'logic-err:prefixes not mutex: {prefixes!r}')
    [prefix] = prefixes
    func_name = s[len(prefix):]
    if not func_name.isidentifier(): raise AdhocArgParserError
    options4argparser = args[:i]
    args4call = args[i+1:]


    (positional_args, flag2bool, keyword2arg, keyword2args) = adhoc_argparse__args(args4call)
    return ((options4argparser, (prefix, func_name), args4call), (positional_args, flag2bool, keyword2arg, keyword2args))

def adhoc_argparse__args(args, /):
    '[str] -> (positional_args, flag2bool, keyword2arg, keyword2args)'
    positional_args = []
    flag2bool = {}
    keyword2arg = {}
    keyword2args = {}

    for s in args:
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
            v = eval_single_arg_payload(arg_payload)
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

def _NOP_():pass #nop:no-op:无操作:用于 adhoc_argparser__main__subcmds

if __name__ == "__main__":
    from seed.recognize.cmdline.adhoc_argparser import adhoc_argparser__main__call, AdhocArgParserError, _NOP_
    adhoc_argparser__main__call(globals(), None)
        #main()

