#__all__:goto
r'''[[[
e ../../python3_src/seed/for_libs/for_doctest.py
see:
    seed.for_libs.for_doctest
        nn_ns.app.doctest_cmd
    seed.test_utils.doctest_all
        nn_ns.app.doctest_all

[[
news:
    -v/--verbose
    -ff/--fail_fast
    -df/--ndiff
    -ht/--as_helper4test_example_prepare
]]



seed.for_libs.for_doctest
py -m nn_ns.app.debug_cmd   seed.for_libs.for_doctest -x
py -m nn_ns.app.doctest_cmd   seed.for_libs.for_doctest!   -v
py -m nn_ns.app.doctest_cmd   seed.for_libs.for_doctest!   -v -ht
    #NotImplementedError
py -m nn_ns.app.doctest_cmd   seed.for_libs.for_doctest!   -ht
py -m nn_ns.app.doctest_cmd   seed.for_libs.for_doctest:_Test   -ht
py -m nn_ns.app.doctest_cmd   seed.for_libs.for_doctest:_Test._err   -ht

py -m nn_ns.app.doctest_cmd seed.math.floor_ceil:floor_kth_root_ -v
py -m nn_ns.app.doctest_cmd seed.math.floor_ceil! -ht


py -m seed.for_libs.for_doctest -h
    #主要查看『--optionflag』的choices
    #多了{COMPARISON_FLAGS,REPORTING_FLAGS}

py -m seed.for_libs.for_doctest __main__:_Test._f,_Test._g  __main__:_Test
py -m seed.for_libs.for_doctest __main__:_Test._f,_Test._g  __main__:_Test -v

py -m seed.for_libs.for_doctest __main__:_Test._f,_Test._g  __main__:_Test -ff --optionflag REPORT_NDIFF
py -m seed.for_libs.for_doctest __main__:_Test._f,_Test._g  __main__:_Test -ff --optionflag REPORT_NDIFF --verbose

py -m seed.for_libs.for_doctest __main__:_Test._f,_Test._g  __main__:_Test -ff --ndiff
py -m seed.for_libs.for_doctest __main__:_Test._f,_Test._g  __main__:_Test -ff --df

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


doctest.REPORT_NDIFF¶
When specified, differences are computed by difflib.Differ, using the same
algorithm as the popular ndiff.py utility. This is the only method that
marks differences within lines as well as across lines.  For example, if a line
of expected output contains digit 1 where actual output contains letter
l, a line is inserted with a caret marking the mismatching column positions.


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
main
    ArgParseError
    parse4module_qname_and_obj_qnames
    iter_objs5module_qname_and_obj_qnames
    doctest__run_docstring_examples4module_qname_and_obj_qnames
    doctest_optionflag_names

doctest__run_docstring_examples4module_qname_and_obj_qnames____ex
    doctest__run_docstring_examples4module_qname_and_obj_qnames
    print_doctest_example_stmt_
    parse_doctest_output__txt_
    print_corrected_doctest_examples5doctest_output_
    '''.split()
__all__

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


######################
#doctest_output_format:goto
_sepline_p = r'(?:[*]{70})'
_sp3_p = r'(?:[ ]{3})'
_sp4_p = r'(?:[ ]{4})'
_sp5_p = r'(?:[ ]{5})'
# r'' --> fr''
_sp3_block_p = fr'(?:(?:\n{_sp3_p}(?:.*))+)'
_sp4_block_p = fr'(?:(?:\n{_sp4_p}(?:.*))+)'
_sp5_block_p = fr'(?:(?:\n{_sp5_p}(?:.*))+)'
_location_info_p = r'(?:(?:File "(?P<fname>.*)", line|Line) (?P<lineno>\d+), in (?P<qname>\S+))'
_failed_example_p = fr'(?:Failed example:(?P<sp4__example>{_sp4_block_p}))'
_raised_p = fr'(?:Exception raised:\n{_sp4_p}Traceback.*:{_sp5_block_p}\n{_sp4_p}(?P<exc_info>.+))'
_expected_p = fr'(?:Expected nothing|Expected:(?P<sp4__expected>{_sp4_block_p}))'
_got_p = fr'(?:Got:(?P<sp4__got>{_sp4_block_p}))'
_per_doctest_output_p = fr'(?:{_sepline_p}\n{_location_info_p}\n{_failed_example_p}\n(?:{_raised_p}|{_expected_p}\n{_got_p})\n)'

_per_doctest_output_re = re.compile(_per_doctest_output_p)
    #parse_doctest_output__txt_:goto

_tail_p = fr'(?:{_sepline_p}\n\d+ items had failures:{_sp3_block_p}\n[*][*][*]Test Failed[*][*][*] \d+ failures[.]\n)'
_tail_re = re.compile(_tail_p)

r'''[[[
-ht/--as_helper4test_example_prepare

doctest_output_format:here
File "...", line ..., in ...
Line ..., in ...

**********************************************************************
Line ..., in ...
Failed example:
    ...
Exception raised:
    Traceback (most recent call last):
        ...
    ...
**********************************************************************
Line ..., in ...
Failed example:
    ...
Expected nothing
Got:
    ...
**********************************************************************
Line ..., in ...
Failed example:
    ...
Expected:
    ...
Got:
    ...


doctest.run_docstring_examples():without no below tail:
doctest.testmod():has tail:
**********************************************************************
2 items had failures:
   1 of   1 in seed.for_libs.for_doctest!._Test
   3 of   3 in seed.for_libs.for_doctest!._Test._err
***Test Failed*** 4 failures.

or:
**********************************************************************
1 items had failures:
   3 of   3 in seed.for_libs.for_doctest!._Test._err
***Test Failed*** 3 failures.

or:
**********************************************************************
1 items had failures:
   1 of   1 in seed.for_libs.for_doctest!._Test
***Test Failed*** 1 failures.


#]]]'''#'''


__all__
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

def doctest__run_docstring_examples4module_qname_and_obj_qnames____ex(as_helper4test_example_prepare, module_qname, may_obj_qnames, /, **kwargs4run_docstring_examples):
    from contextlib import redirect_stdout, redirect_stderr
    from io import StringIO

    if as_helper4test_example_prepare and kwargs4run_docstring_examples.get('verbose'): raise NotImplementedError

    f = lambda:doctest__run_docstring_examples4module_qname_and_obj_qnames(module_qname, may_obj_qnames, **kwargs4run_docstring_examples)

    if not as_helper4test_example_prepare:
        f()
        return

    iofile = StringIO()
    p0 = iofile.tell()
    with redirect_stdout(iofile):
        f()
    iofile.seek(p0)
    #it = parse_doctest_output__ifile_(iofile)
    txt = iofile.getvalue()
    if not txt: return
    print(txt)
    sss = '#'*22
    print(sss)
    print(sss)
    print(sss)
    print_corrected_doctest_examples5doctest_output_(txt)
def print_corrected_doctest_examples5doctest_output_(txt, /):
    it = parse_doctest_output__txt_(txt)
    for (case, may_fname, lineno, qname, example_stmt, x) in it:
        if 1:
            print()#avoid be 'expected' of prev example
            print(f'# Line {lineno}, in {qname}')
                #need not show:may_fname
        print_doctest_example_stmt_(example_stmt)
        if case == 0:
            exc_info = x
            print('Traceback (most recent call last):')
            print('    ...')
            print(exc_info)
        elif case == 1:
            got = x
            print(got)
        elif case == 2:
            (got,expected) = x
            print(got)
            print()
            print('###buggy expected of above example:')
            print(expected)
        else:
            raise 000
def print_doctest_example_stmt_(example_stmt, /):
    prefix = '>>> '
    for line in example_stmt.split('\n'):
        print(f'{prefix}{line}')
        prefix = '... '
    return
def __():
    def parse_doctest_output__ifile_(ifile, /):
        return parse_doctest_output__txt_(ifile.read())

def parse_doctest_output__txt_(txt, /):
    '-> Iter (case, lineno, fname, example_stmt, exc_info|got|(got,expected)) #doctest_output_format:goto'
    begin = 0
    while not begin == len(txt):
        m = _per_doctest_output_re.match(txt, begin)
        if not m:
            m = _tail_re.match(txt, begin)
            if not m:
                raise Exception(txt[begin:])
            begin = m.end()
            if not begin == len(txt):
                raise Exception(txt[begin:])
            break
        begin = m.end()
        ######################
        may_fname = m['fname']
        lineno = m['lineno']
        qname = m['qname']
        example_stmt = _dedent(4, m['sp4__example'])
        may_exc_info = m['exc_info']
        may_expected = _dedent_may_(4, m['sp4__expected'])
        may_got = _dedent_may_(4, m['sp4__got'])
        assert  (may_exc_info is None) ^ (may_got is None)
        assert  not (may_got is None) or (may_expected is None)
        if not may_exc_info is None:
            exc_info = may_exc_info
            assert may_expected is None
            assert may_got is None
            yield (case:=0, may_fname, lineno, qname, example_stmt, exc_info)
        else:
            assert not may_got is None
            got = may_got
            if may_expected is None:
                yield (case:=1, may_fname, lineno, qname, example_stmt, got)
            else:
                yield (case:=2, may_fname, lineno, qname, example_stmt, (got, expected:=may_expected))
        ######################
    return
def _dedent_may_(n, may_txt, /):
    if may_txt is None:
        return None
    return _dedent(n, txt:=may_txt)
def _dedent(n, txt, /):
    assert not txt or not txt[-1] == '\n'
    if 1:
        assert not txt or txt[0] == '\n'
            # <<== from regex"(\n...)+"
        txt = txt.removeprefix('\n')
    def __(sp, /):
        for line in txt.split('\n'):
            assert line.startswith(sp)#or not line
            yield line[len(sp):]
    return '\n'.join(__(' '*n))

def doctest__run_docstring_examples4module_qname_and_obj_qnames(module_qname, may_obj_qnames, /, **kwargs4run_docstring_examples):
    if may_obj_qnames is None:
        module_obj = import_module(module_qname)
        name = f'{module_qname}!'
        doctest.testmod(module_obj, name=name, **kwargs4run_docstring_examples)
        return

    obj_qnames = may_obj_qnames
    for ((module_qname, may_obj_qnames), (module_obj, doctesting_obj), name) in iter_objs5module_qname_and_obj_qnames(module_qname, may_obj_qnames):
        doctest.run_docstring_examples(doctesting_obj, vars(module_obj), name=name, **kwargs4run_docstring_examples)
        if isinstance(doctesting_obj, type):
            #above test:cls.__doc__ only
            #below test:cls.f.__doc__ only
            cls = doctesting_obj
            for nm, f in vars(cls).items():
                if (_doctesting_obj := getattr(f, '__doc__', None)):
                    doctest.run_docstring_examples(_doctesting_obj, vars(module_obj), name=f'{name}.{nm}', **kwargs4run_docstring_examples)
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
    parser.add_argument('-df', '--ndiff', action='store_true', default = False
        , help='marks differences within lines as well as across lines; <==> --optionflags REPORT_NDIFF')


    parser.add_argument('-opt_flg', '--optionflag', action='append', default=[]
        , type=str
        , choices=doctest_optionflag_names
        , help='specify a doctest option flag to apply to the test run; may be specified more than once to apply multiple options')

    parser.add_argument('-ht', '--as_helper4test_example_prepare', action='store_true', default = False
        , help='collect actually output and show together')

    args = parser.parse_args(args)
    module_qname_and_obj_qnames__strs = args.module_qname_and_obj_qnames
    verbose = args.verbose
    fail_fast = args.fail_fast
    ndiff = args.ndiff
    optionflag_names = args.optionflag
    as_helper4test_example_prepare = args.as_helper4test_example_prepare


    module_qname_and_may_obj_qnames__pairs = [*map(parse4module_qname_and_obj_qnames, module_qname_and_obj_qnames__strs)]
    #flags = doctest.REPORT_NDIFF|doctest.FAIL_FAST
    flags = 0 #default
    if fail_fast:
        flags |= doctest.FAIL_FAST
    if ndiff:
        flags |= doctest.REPORT_NDIFF
    for optionflag_name in optionflag_names:
        flags |= getattr(doctest, optionflag_name)

    for (module_qname, may_obj_qnames) in module_qname_and_may_obj_qnames__pairs:
        #doctest__run_docstring_examples4module_qname_and_obj_qnames(module_qname, may_obj_qnames, verbose=verbose, optionflags=flags)
        doctest__run_docstring_examples4module_qname_and_obj_qnames____ex(as_helper4test_example_prepare, module_qname, may_obj_qnames, verbose=verbose, optionflags=flags)

if 1:
    #if __name__ == "__main__":
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
        def _err():
            r'''[[[

            >>> @str
            stmt1
            >>> for i in range(2):
            ...     i
            stmt2
            >>> raise Exception
            useless-expected
            >>> 'expected nothing'
            >>> 'expected=!=got'
            got=!=expected

            #]]]'''


if __name__ == "__main__":
    from seed.for_libs.for_doctest import *
    #__all__.append(_Test)

if __name__ == "__main__":
    main()


from seed.for_libs.for_doctest import main
from seed.for_libs.for_doctest import *

