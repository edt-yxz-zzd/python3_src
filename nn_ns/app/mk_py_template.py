r'''

e ../../python3_src/nn_ns/app/mk_py_template.py




news@20251009
    ++『-s』『--using_simplified_tpl』:使用简化模板 # 用于脚本文件
py_tpl -s ./script/tmp.py




old-API:
    py -m nn_ns.app.mk_py_template -o /path/to/python3_src/pkg/module.py
    py -m nn_ns.app.mk_py_template -o ../../python3_src/seed/types/mapping/OpaquePseudoMapping__weakref.py
new-API:
py -m nn_ns.app.mk_py_template --root_dirs '.' --root_dirs '../../python3_src/' -i '<~.tpl>' --begin4template4module '' --end4template4module '' --placeholder4path4module '\bzz\b'  --placeholder4qnm4module '\bz\b' -o ./script/tmp.py
view ./script/tmp.py
rm ./script/tmp.py
==>>:
py_tpl ./script/tmp.py
py_tpl -o ../../python3_src/seed/tmp.py



py -m nn_ns.app.mk_py_template --root_dirs '.' --root_dirs '../../python3_src/' -i '<useful_txt>' --begin4template4module $'#[[[[[template4module:begin\n' --end4template4module $'#]]]]]template4module:end\n' --placeholder4path4module 'xxx/yyy' --placeholder4qnm4module 'xxx.yyy' -F  -o ../../python3_src/seed/tmp.py
view  ../../python3_src/seed/tmp.py
rm  ../../python3_src/seed/tmp.py


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
    path4std_tpl = this_file_path.with_suffix('.py.tpl')
    path4std_simplified_tpl = this_file_path.with_suffix('.py.simplified.tpl')
    return this_pkg_root, path4useful_txt, path4std_tpl, path4std_simplified_tpl
class Globals:
    this_pkg_root, path4useful_txt, path4std_tpl, path4std_simplified_tpl = _f()
    begin4template4module = '#[[[[[template4module:begin\n'
    end4template4module = '#]]]]]template4module:end\n'
    #placeholder4qnm4module = r'xxx.yyy'
    placeholder4qnm4module = r'xxx[.]yyy'
    placeholder4path4module = r'xxx[/]yyy'

    root_dirs = (this_pkg_root, '.')



def main(args=None, /):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout
    import re
    from seed.text.replace_substrings__simultaneously import replace_substrings__simultaneously_# replace_substrings__simultaneously__str, replace_substrings__simultaneously__regex, ReplaceSubstringsSimultaneously


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

    #cwd = Path.cwd()
        #current working directory
    parser.add_argument('--root_dirs', type=str, default=None#Globals.root_dirs
                        , action='append'
                        , help='root_dirs to place module # [???sys.path???]')

    parser.add_argument('--begin4template4module', type=str, default=Globals.begin4template4module
                        , help='begin_marker for template4module')

    parser.add_argument('--end4template4module', type=str, default=Globals.end4template4module
                        , help='end_marker for template4module')

    parser.add_argument('--placeholder4path4module', type=str, default=Globals.placeholder4path4module
                        , help='placeholder(regex pattern) in template4module to be replaced by path4module')
    parser.add_argument('--placeholder4qnm4module', type=str, default=Globals.placeholder4qnm4module
                        , help='placeholder(regex pattern) in template4module to be replaced by qnm4module')
    parser.add_argument('-F', '--regex_vs_string', action='store_true'
                        , default = False
                        , help='treat placeholder4qnm4module,placeholder4path4module as string instead of regex')


    parser.add_argument('-i', '--input', type=str
                        #, default=Globals.path4useful_txt
                        , default=None
                        , help='input file path for template4module # <~.tpl> | <~.simplified.tpl> | <useful_txt>')
    parser.add_argument('-s', '--using_simplified_tpl', action='store_true'
                        , default = False
                        , help='as if  file path be "<~.simplified.tpl>"')
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

    root_dirs = args.root_dirs
    if root_dirs is None:
        root_dirs = Globals.root_dirs
    root_dirs = [Path(s).resolve() for s in args.root_dirs]

    begin_marker = args.begin4template4module
    end_marker = args.end4template4module
    placeholder4path4module = args.placeholder4path4module
    placeholder4qnm4module = args.placeholder4qnm4module
    #if 0:
    #    if not args.regex_vs_string:
    #        placeholder4path4module = re.compile(placeholder4path4module)
    #        placeholder4qnm4module = re.compile(placeholder4qnm4module)

    may_ifname = args.input
    using_simplified_tpl = args.using_simplified_tpl
    if using_simplified_tpl:
        may_ifname = Globals.path4std_simplified_tpl
    elif may_ifname is None:
        pass
    elif may_ifname == '<~.tpl>':
        may_ifname = Globals.path4std_tpl
    elif may_ifname == '<~.simplified.tpl>':
        may_ifname = Globals.path4std_simplified_tpl
    elif may_ifname == '<useful_txt>':
        may_ifname = Globals.path4useful_txt
    elif may_ifname.startswith('<'):
        raise ValueError(f'unknown builtin path: {may_ifname!r}')


    with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:
        txt = fin.read()
    i = txt.index(begin_marker) + len(begin_marker)
    #j = txt.index(end_marker, i)
    j = txt.rindex(end_marker, i)
        #to allow [end_marker=='']
    template4module = txt[i:j]

    ofname = args.output
    path4target_module = Path(ofname)
    if not '.py' == path4target_module.suffix: raise ValueError('not ".py"')
    if '.' in path4target_module.stem: raise ValueError('"." in stem')
    if not path4target_module.parent.exists(): raise FileNotFoundError(path4target_module.parent)
    if not path4target_module.parent.is_dir(): raise NotADirectoryError(path4target_module.parent)

    path4target_module = path4target_module.resolve()
    try:
        module_qname = mk_qnm4module(root_dirs, path4target_module)
    except ValueError:
        raise ValueError((root_dirs, path4target_module))

    #if 0:
    #    if not args.regex_vs_string:
    #        txt4output = placeholder4qnm4module.sub(module_qname, template4module)
    #        txt4output = placeholder4path4module.sub(ofname, txt4output)
    #    else:
    #        txt4output = template4module.replace(placeholder4qnm4module, module_qname)
    #        txt4output = txt4output.replace(placeholder4path4module, ofname)
    txt4output = replace_substrings__simultaneously_([(placeholder4path4module, ofname), (placeholder4qnm4module, module_qname)], template4module, str_vs_re=not args.regex_vs_string)
    txt4output

    with open(path4target_module, omode, encoding=encoding) as fout:
        fout.write(txt4output)

def mk_qnm4module(root_dirs, path4target_module, /):
    assert path4target_module.is_absolute()
    assert all(path.is_absolute() for path in root_dirs)
    for rt in root_dirs:
        if path4target_module.is_relative_to(rt):
            break
    else:
        raise ValueError
    root_dirs = [rt]
        # it seems as "Path.relative_to(*parts4other)"

    if 1:
        rpath = path4target_module.relative_to(*root_dirs).with_suffix('')
            #^ValueError
            #raise ValueError("{!r} is not in the subpath of {!r}"
        rpath_dir = rpath.parent
    else:
        rpath_dir = path4target_module.parent.relative_to(*root_dirs)
            #^ValueError
        rpath = rpath_dir/path4target_module.stem
    rpath #stem-only
    rpath_dir
    if 0:
        for rt in root_dirs:
            if (rt/rpath_dir).is_dir():
                break
    s = rpath.as_posix()
        #stem-only

    if 0:
        assert s.endswith('.py')
        s = s[:-3]
    if '.' in s: raise ValueError(s)
    module_qname = s.replace('/', '.')

    attrs = module_qname.split('.')
    if not attrs: raise ValueError
    if not all(attrs): raise ValueError
    if not all(attr.isidentifier() for attr in attrs): raise ValueError
    return module_qname


if __name__ == "__main__":
    main()





