r'''[[[
e ../../python3_src/seed/recognize/cmdline/adhoc_argparser.py
from seed.recognize.cmdline.adhoc_argparser import adhoc_argparser__main, adhoc_argparse

#]]]'''
__all__ = '''
    adhoc_argparser__main
    adhoc_argparse
    '''.split()

import sys
from seed.helper.safe_eval import safe_eval
import re

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

def adhoc_argparser__main(nm2main, may_argv, /):
    (subcmds, positional_args, flag2bool, keyword2arg, keyword2args) = adhoc_argparse(may_argv)

    for nm in subcmds:
        nm2main = nm2main[nm]
    main_func = nm2main
    if not callable(main_func): raise AdhocArgParserError(subcmds)

    return main_func(*positional_args, **flag2bool, **keyword2arg, **keyword2args)

def adhoc_argparse(may_argv, /):
    if may_argv is None:
        args = sys.argv[1:]
    else:
        args = may_argv
    subcmds = args[0].split('.')
    #if not subcmds: raise AdhocArgParserError

    positional_args = []
    flag2bool = {}
    keyword2arg = {}
    keyword2args = {}

    for s in args[1:]:
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
    return (subcmds, positional_args, flag2bool, keyword2arg, keyword2args)


