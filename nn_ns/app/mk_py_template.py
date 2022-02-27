r'''

e ../../python3_src/nn_ns/app/mk_py_template.py


py -m nn_ns.app.mk_py_template -o /path/to/python3_src/pkg/module.py
py -m nn_ns.app.mk_py_template -o ../../python3_src/seed/types/mapping/OpaquePseudoMapping__weakref.py

template from:
    view ../../python3_src/useful.txt
        between:
            #[[[[[template4module:begin
            #]]]]]template4module:end
        replace "xxx.yyy" to "pkg.module"


#'''

#contains both ''' and """, should escape...
_example_version_of_snippet_of_useful_txt = """
template4module:goto
main:goto

... ...
... ...


#################################
#[[[[[template4module:begin
#__all__:goto
#main_body_src_code:goto
#HHHHH
#[[[__doc__:begin
r'''
py -m nn_ns.app.mk_py_template -o ../../python3_src/seed/types/mapping/OpaquePseudoMapping__weakref.py
s/^\s*e .*[/]python3_src[/]\(.*\)[.]py$/\1/g
s/[/]/./g
%s/xxx[.]yyy/this_module/g
e ../../python3_src/xxx/yyy.py
xxx.yyy
py -m    xxx.yyy
py -m nn_ns.app.debug_cmd   xxx.yyy

from xxx.yyy import ...

#[[[doc_sections:begin
#doctest_examples:goto
#wwwzzz:goto

#[[[doctest_examples:begin
>>>
...
#]]]doctest_examples:end

#[[[wwwzzz:begin
#]]]wwwzzz:end
#]]]doc_sections:end


#'''
#]]]__doc__:end

#################################
#HHHHH
__all__ = '''

    '''.split()

#################################
#HHHHH
___begin_mark_of_excluded_global_names__0___ = ...
r\"""
import ...
from seed.tiny import str2__all__
__all__ = str2__all__(r'''#)
    #(''')
from seed.abc.abc import ABC, abstractmethod, override, not_implemented, ABCMeta
from seed.helper.repr_input import repr_helper
from seed.tiny import echo, print_err, mk_fprint, mk_assert_eq_f, expectError
from seed.helper.check.checkers import check_pair, check_type_is
  #from seed.helper.check.checkers import checks, checkers, check_funcs
  #view ../../python3_src/seed/helper/check/checkers.py
if 0b00:#[01_to_turn_off]
    #0b01
    print(fr'x={x}')
    from seed.tiny import print_err
    print_err(fr'x={x}')
    from pprint import pprint
    pprint(x)
#\"""
___end_mark_of_excluded_global_names__0___ = ...

#HHHHH
#[[[main_body_src_code:begin
#zzzwww:goto

#[[[zzzwww:begin
#]]]zzzwww:end
#]]]main_body_src_code:end


#HHHHH
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #<BLANKLINE>
    #Traceback (most recent call last):


#]]]]]template4module:end
#################################




#"""


from pathlib import Path


def _f():
    this_file_path = Path(__file__)
    this_file_path = this_file_path.resolve()
    assert this_file_path.is_absolute()
    L = len(__package__.split('.'))+1
    parts = this_file_path.parts
    assert L < len(parts)
    this_pkg_root = Path(*parts[:-L])
    assert this_pkg_root.is_absolute()
    path4useful_txt = this_pkg_root/'useful.txt'
    assert path4useful_txt.exists()
    return this_pkg_root, path4useful_txt
class Globals:
    this_pkg_root, path4useful_txt = _f()



def main(args=None, /):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    parser = argparse.ArgumentParser(
        description='make new python module using template4module in python3_src/useful.txt'
        , epilog=r'''
template from:
    view ../../python3_src/useful.txt
        between:
            #[[[[[template4module:begin
            #]]]]]template4module:end
        replace "xxx.yyy" to "pkg.module"

#'''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    parser.add_argument('-i', '--input', type=str, default=Globals.path4useful_txt
                        , help='input file path for template4module')
    parser.add_argument('-o', '--output', type=str, default=None, required=True
                        , help='output file path for target module')
    parser.add_argument('-e', '--encoding', type=str
                        , default='utf8'
                        , help='input/output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    encoding = args.encoding
    omode = 'wt' if args.force else 'xt'

    may_ifname = args.input
    with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:
        txt = fin.read()
    begin = '#[[[[[template4module:begin\n'
    end = '#]]]]]template4module:end\n'
    substr4replace = r'xxx.yyy'
    i = txt.index(begin) + len(begin)
    j = txt.index(end, i)
    template4module = txt[i:j]

    ofname = args.output
    path4target_module = Path(ofname)
    if not '.py' == path4target_module.suffix: raise ValueError
    path4target_module = path4target_module.resolve()
    rpath = path4target_module.relative_to(Globals.this_pkg_root)
    s = rpath.as_posix()
    assert s.endswith('.py')
    s = s[:-3]
    if '.' in s: raise ValueError(s)
    module_qname = s.replace('/', '.')
    attrs = module_qname.split('.')
    if not attrs: raise ValueError
    if not all(attrs): raise ValueError
    if not all(attr.isidentifier() for attr in attrs): raise ValueError
    txt4output = template4module.replace(substr4replace, module_qname)
    with open(path4target_module, omode, encoding=encoding) as fout:
        fout.write(txt4output)
if __name__ == "__main__":
    main()





