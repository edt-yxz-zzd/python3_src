r'''[[[
e ../../python3_src/seed/for_libs/for_doctest.py
py -m nn_ns.app.doctest_cmd seed.math.floor_ceil:floor_kth_root_ -v

py -m nn_ns.app.debug_cmd   seed.for_libs.for_doctest

py -m seed.for_libs.for_doctest -h
    #主要查看『--optionflag』的choices
    #多了{COMPARISON_FLAGS,REPORTING_FLAGS}

py -m seed.for_libs.for_doctest __main__:_Test._f,_Test._g  __main__:_Test
py -m seed.for_libs.for_doctest __main__:_Test._f,_Test._g  __main__:_Test -v

py -m seed.for_libs.for_doctest __main__:_Test._f,_Test._g  __main__:_Test -ff --optionflag REPORT_NDIFF
py -m seed.for_libs.for_doctest __main__:_Test._f,_Test._g  __main__:_Test -ff --optionflag REPORT_NDIFF --verbose


[[抄袭帮助文档:考虑增加--option,--fail-fast
py -m doctest -h
usage: doctest.py [-h] [-v]
                  [-o {DONT_ACCEPT_TRUE_FOR_1,DONT_ACCEPT_BLANKLINE,NORMALIZE_WHITESPACE,ELLIPSIS,SKIP,IGNORE_EXCEPTION_DETAIL,REPORT_UDIFF,REPORT_CDIFF,REPORT_NDIFF,REPORT_ONLY_FIRST_FAILURE,FAIL_FAST}]
                  [-f]
                  file [file ...]

doctest runner

positional arguments:
  file                  file containing the
                        tests to run

options:
  -h, --help            show this help message
                        and exit
  -v, --verbose         print very verbose
                        output for all tests
  -o {DONT_ACCEPT_TRUE_FOR_1,DONT_ACCEPT_BLANKLINE,NORMALIZE_WHITESPACE,ELLIPSIS,SKIP,IGNORE_EXCEPTION_DETAIL,REPORT_UDIFF,REPORT_CDIFF,REPORT_NDIFF,REPORT_ONLY_FIRST_FAILURE,FAIL_FAST}, --option {DONT_ACCEPT_TRUE_FOR_1,DONT_ACCEPT_BLANKLINE,NORMALIZE_WHITESPACE,ELLIPSIS,SKIP,IGNORE_EXCEPTION_DETAIL,REPORT_UDIFF,REPORT_CDIFF,REPORT_NDIFF,REPORT_ONLY_FIRST_FAILURE,FAIL_FAST}
                        specify a doctest option
                        flag to apply to the
                        test run; may be
                        specified more than once
                        to apply multiple
                        options
  -f, --fail-fast       stop running tests after
                        first failure (this is a
                        shorthand for -o
                        FAIL_FAST, and is in
                        addition to any other -o
                        options)
]]

[[copy from: view /sdcard/0my_files/tmp/out4py/html2text/py_38_doc/doctest.html.txt
if __name__ == '__main__':
    import doctest
    flags = doctest.REPORT_NDIFF|doctest.FAIL_FAST
    if len(sys.argv) > 1:
        name = sys.argv[1]
        if name in globals():
            obj = globals()[name]
        else:
            obj = __test__[name]
        doctest.run_docstring_examples(obj, globals(), name=name,
                                       optionflags=flags)
    else:
        fail, total = doctest.testmod(optionflags=flags)
        print("{} failures out of {} tests".format(fail, total))
]]

#]]]'''
__all__ = '''
    ArgParseError
    parse4module_qname_and_obj_qnames
    iter_objs5module_qname_and_obj_qnames
    doctest__run_docstring_examples4module_qname_and_obj_qnames
    doctest_optionflag_names
    main
    '''.split()

from importlib import import_module
from operator import attrgetter
import doctest
import re

_nm_p = r'(?:\w+)'
_qnm_p = fr'(?:{_nm_p}(?:[.]{_nm_p})*)'
_qnms_p = fr'(?:{_qnm_p}(?:[,]{_qnm_p})*)'
_qnm_qnms_p = fr'(?:{_qnm_p}:{_qnms_p})'
_qnm_qnms_re = re.compile(_qnm_qnms_p)

class ArgParseError(Exception):pass
def parse4module_qname_and_obj_qnames(module_qname_and_obj_qnames__str, /):
    m = _qnm_qnms_re.fullmatch(module_qname_and_obj_qnames__str)
    if not m:
        raise ArgParseError(f'unknown format(expect: "xxx.yyy:aaa.bbb,ccc"): {module_qname_and_obj_qnames__str!r}')
    s = module_qname_and_obj_qnames__str
    (module_qname, _, obj_qnames__str) = s.partition(':')
    obj_qnames = obj_qnames__str.split(',')
    obj_qnames = (*obj_qnames,)
    return (module_qname, obj_qnames)


def iter_objs5module_qname_and_obj_qnames(module_qname, obj_qnames, /):
    module_obj = import_module(module_qname)
    for obj_qname in obj_qnames:
        attr_obj = attrgetter(obj_qname)(module_obj)
        name = f'{module_qname}:{obj_qname}'
        yield ((module_qname, obj_qnames), (module_obj, attr_obj), name)

def doctest__run_docstring_examples4module_qname_and_obj_qnames(module_qname, obj_qnames, /, **kwargs4run_docstring_examples):
    for ((module_qname, obj_qnames), (module_obj, doctesting_obj), name) in iter_objs5module_qname_and_obj_qnames(module_qname, obj_qnames):
        doctest.run_docstring_examples(doctesting_obj, vars(module_obj), name=name, **kwargs4run_docstring_examples)
assert globals() is vars(import_module(__name__))


def _collect_doctest_optionflag_names():
    return (*sorted(nm for nm, val in vars(doctest).items() if type(val) is int and nm.isupper()),)
doctest_optionflag_names = _collect_doctest_optionflag_names()
    #{COMPARISON_FLAGS,DONT_ACCEPT_BLANKLINE,DONT_ACCEPT_TRUE_FOR_1,ELLIPSIS,FAIL_FAST,IGNORE_EXCEPTION_DETAIL,NORMALIZE_WHITESPACE,REPORTING_FLAGS,REPORT_CDIFF,REPORT_NDIFF,REPORT_ONLY_FIRST_FAILURE,REPORT_UDIFF,SKIP}
    #多了{COMPARISON_FLAGS,REPORTING_FLAGS}
#py -m doctest -h
    #{DONT_ACCEPT_TRUE_FOR_1,DONT_ACCEPT_BLANKLINE,NORMALIZE_WHITESPACE,ELLIPSIS,SKIP,IGNORE_EXCEPTION_DETAIL,REPORT_UDIFF,REPORT_CDIFF,REPORT_NDIFF,REPORT_ONLY_FIRST_FAILURE,FAIL_FAST}

def main(args=None, /):
    import argparse

    parser = argparse.ArgumentParser(
        description='doctest on single obj'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('module_qname_and_obj_qnames', type=str, nargs='+'
        , help='''qual_name for the doctest-testing obj; format="<module_qname>:<obj_qnames>", eg. "xxx.yyy:aaa.bbb,ccc"''')
    parser.add_argument('-v', '--verbose', action='store_true', default = False
        , help='print very verbose output for all tests')
    parser.add_argument('-ff', '--fail_fast', action='store_true', default = False
        , help='stop running tests after first failure; <==> --optionflags FAIL_FAST')
    parser.add_argument('-opt_flg', '--optionflag', action='append', default=[]
        , type=str
        , choices=doctest_optionflag_names
        , help='specify a doctest option flag to apply to the test run; may be specified more than once to apply multiple options')

    args = parser.parse_args(args)
    module_qname_and_obj_qnames__strs = args.module_qname_and_obj_qnames
    verbose = args.verbose
    fail_fast = args.fail_fast
    optionflag_names = args.optionflag


    module_qname_and_obj_qnames__pairs = [*map(parse4module_qname_and_obj_qnames, module_qname_and_obj_qnames__strs)]
    #flags = doctest.REPORT_NDIFF|doctest.FAIL_FAST
    flags = 0 #default
    if fail_fast:
        flags |= doctest.FAIL_FAST
    for optionflag_name in optionflag_names:
        flags |= getattr(doctest, optionflag_name)

    for (module_qname, obj_qnames) in module_qname_and_obj_qnames__pairs:
        doctest__run_docstring_examples4module_qname_and_obj_qnames(module_qname, obj_qnames, verbose=verbose, optionflags=flags)

if __name__ == "__main__":
    class _Test:
        r'''[[[
        >>> 1

        #]]]'''
        def _f():
            r'''[[[
            >>> 2
            2

            #]]]'''
        def _g():
            r'''[[[
            >>> 3
            3

            #]]]'''

if __name__ == "__main__":
    main()



