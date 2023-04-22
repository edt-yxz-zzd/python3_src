r'''[[[
e ../../python3_src/seed/for_libs/for_doctest.py
see:
    seed.for_libs.for_doctest
        nn_ns.app.doctest_cmd
    seed.test_utils.doctest_all
        nn_ns.app.doctest_all

py -m nn_ns.app.doctest_cmd seed.math.floor_ceil:floor_kth_root_ -v

py -m nn_ns.app.debug_cmd   seed.for_libs.for_doctest

py -m seed.for_libs.for_doctest -h
    #主要查看『--optionflag』的choices
    #多了{COMPARISON_FLAGS,REPORTING_FLAGS}

py -m seed.for_libs.for_doctest __main__:_Test._f,_Test._g  __main__:_Test
py -m seed.for_libs.for_doctest __main__:_Test._f,_Test._g  __main__:_Test -v

py -m seed.for_libs.for_doctest __main__:_Test._f,_Test._g  __main__:_Test -ff --optionflag REPORT_NDIFF
py -m seed.for_libs.for_doctest __main__:_Test._f,_Test._g  __main__:_Test -ff --optionflag REPORT_NDIFF --verbose


py -m seed.for_libs.for_doctest __main__! -v
py -m seed.for_libs.for_doctest __main__:__doc__ -v
py -m seed.for_libs.for_doctest __main__:_Test -v


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


doctest.testfile(filename, module_relative=True, name=None, package=None, globs=None, verbose=None, report=True, optionflags=0, extraglobs=None, raise_on_error=False, parser=DocTestParser(), encoding=None)
  #name并非对象名:Optional argument name gives the name of the test; by default, or if None, os.path.basename(filename) is used.
doctest.testmod(m=None, name=None, globs=None, verbose=None, report=True, optionflags=0, extraglobs=None, raise_on_error=False, exclude_empty=False)
  #name并非对象名:Optional argument name gives the name of the module; by default, or if None, m.__name__ is used.
doctest.run_docstring_examples(f, globs, verbose=False, name="NoName", compileflags=None, optionflags=0)¶
  #Test examples associated with object f; for example, f may be a string, a module, a function, or a class object.
  #name并非对象名:Optional argument name is used in failure messages, and defaults to "NoName".



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
#_qnm_qnms_re = re.compile(_qnm_qnms_p)

_qnm_sf_p = fr'(?:{_qnm_p}!)'
#_qnm_sf_re = re.compile(_qnm_sf_p)
_qnm_qnms_or_sf_p = fr'(?:{_qnm_p}(?::{_qnms_p}|!))'
_qnm_qnms_or_sf_re = re.compile(_qnm_qnms_or_sf_p)

class ArgParseError(Exception):pass
def parse4module_qname_and_obj_qnames(module_qname_and_obj_qnames__str, /):
    #m = _qnm_qnms_re.fullmatch(module_qname_and_obj_qnames__str)
    m = _qnm_qnms_or_sf_re.fullmatch(module_qname_and_obj_qnames__str)
    if not m:
        raise ArgParseError(f'unknown format(expect: "xxx.yyy!", "xxx.yyy:aaa.bbb,ccc"): {module_qname_and_obj_qnames__str!r}')
    s = module_qname_and_obj_qnames__str
    if s.endswith('!'):
        _qnm_sf_p
        module_qname = s[:-1]
        may_obj_qnames = None
    else:
        _qnm_qnms_p
        (module_qname, _, obj_qnames__str) = s.partition(':')
        obj_qnames = obj_qnames__str.split(',')
        obj_qnames = (*obj_qnames,)
        may_obj_qnames = obj_qnames
    return (module_qname, may_obj_qnames)


def iter_objs5module_qname_and_obj_qnames(module_qname, may_obj_qnames, /):
    module_obj = import_module(module_qname)
    if may_obj_qnames is None:
        attr_obj = module_obj
        name = f'{module_qname}!'
        yield ((module_qname, may_obj_qnames), (module_obj, attr_obj), name)
        return
    obj_qnames = may_obj_qnames
    for obj_qname in obj_qnames:
        attr_obj = attrgetter(obj_qname)(module_obj)
        name = f'{module_qname}:{obj_qname}'
        yield ((module_qname, may_obj_qnames), (module_obj, attr_obj), name)

def doctest__run_docstring_examples4module_qname_and_obj_qnames(module_qname, may_obj_qnames, /, **kwargs4run_docstring_examples):
    if may_obj_qnames is None:
        module_obj = import_module(module_qname)
        name = f'{module_qname}!'
        doctest.testmod(module_obj, name=name, **kwargs4run_docstring_examples)
        return

    obj_qnames = may_obj_qnames
    for ((module_qname, may_obj_qnames), (module_obj, doctesting_obj), name) in iter_objs5module_qname_and_obj_qnames(module_qname, may_obj_qnames):
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
        , help='''qual_name for the doctest-testing obj; format="<module_qname>:<obj_qnames>" / "<module_qname>!", eg. "xxx.yyy:aaa.bbb,ccc", "xxx.yyy:"''')
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


    module_qname_and_may_obj_qnames__pairs = [*map(parse4module_qname_and_obj_qnames, module_qname_and_obj_qnames__strs)]
    #flags = doctest.REPORT_NDIFF|doctest.FAIL_FAST
    flags = 0 #default
    if fail_fast:
        flags |= doctest.FAIL_FAST
    for optionflag_name in optionflag_names:
        flags |= getattr(doctest, optionflag_name)

    for (module_qname, may_obj_qnames) in module_qname_and_may_obj_qnames__pairs:
        doctest__run_docstring_examples4module_qname_and_obj_qnames(module_qname, may_obj_qnames, verbose=verbose, optionflags=flags)

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



