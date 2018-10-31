
'''
see also: seed.pkg_tools.import_object
#??see also: nn_ns.Import.import_object

* via module
    #importlib.import_module
    xxx.yyy.zzz
        '' means 'builtins'
    .obj.attr1.attr2
        '' means the module object itself
* via eval
    source or source_path
* via exec
    # exec
    source or source_path
    globals
    locals
    .obj.attr1.attr2
* via script
    #seed.pkg_tools.load_as_module.load_as_module_or_package_ex
    (xxx.yyy.zzz, [(bare_name, script_path)], is_package)
    .obj.attr1.attr2
"""
#* via zip
#    #zipimport??
#* json/text/binary
"""


who use me?
    * nn_ns.my_fileformat.configuration.utils.app.show_yacc_productions
        when using PLY
        to show_yacc_productions from:
            * yacc_p_pseudo_moudle_object
                #module/class
                    .p_*
                    .tokens
                    .start
            * yacc_lrparser
                :: ply.yacc.LRParser
            * lex_postprocessor_with_parser
                :: nn_ns.my_fileformat.configuration.utils.LexPostprocessors.LexPostprocessorWithParser



'''


__all__ = '''
    ViaCase
    get_python_object
    get_python_object_via_module_system
    get_python_object_via_script_as_module
    get_python_object_via_exec
    get_python_object_via_eval
    GetPythonObjectHelper


    via_case2get_python_object
    '''.split()
    #get_dot_attrs
    #is_maybe_string
    #check_maybe_string



from seed.pkg_tools.load_as_module import load_as_module_or_package_ex
from seed.types.DictKeyAsObjAttr import DictKeyAsObjAttr
from importlib import import_module
from operator import attrgetter
from enum import Enum
import re
import sys
from pathlib import Path

ViaCase = Enum('ViaCase', '''
    ModuleSystem
    ScriptAsModule
    Exec
    Eval
    '''
    )

def is_maybe_string(x):
    return x is None or type(x) is str
def check_maybe_string(x):
    if not is_maybe_string(x): raise TypeError

def get_python_object_via_eval(
    python_source_string, may_dot_attrs
    , *, globals=None, locals=None
    ):
    #eval
    check_maybe_string(may_dot_attrs)

    if globals is None:
        globals = {}
    if locals is None:
        locals = {}
    obj = eval(python_source_string, globals=globals, locals=locals)
    return get_dot_attrs(obj, may_dot_attrs)


def get_python_object_via_exec(
    python_source_string, may_dot_attrs
    , *
    , globals=None, locals=None
    , using_the_single_object=False
    ):
    #exec
    check_maybe_string(may_dot_attrs)

    if globals is None:
        globals = {}
    if locals is None:
        locals = {}
    exec(python_source_string, globals=globals, locals=locals)
    if using_the_single_object:
        if len(locals) != 1:
            keys = list(locals.keys())
            raise ValueError(f'not single object: {keys}')
        for obj in locals.values():
            break
        else:
            raise logic-error
    else:
        ##### ver1if not may_dot_attrs: return globals
        obj = DictKeyAsObjAttr(globals)
        ##### curr ver: if not may_dot_attrs: return obj
    return get_dot_attrs(obj, may_dot_attrs)

def get_python_object_via_script_as_module(
    may_qname, bare_name_source_path_pairs, may_dot_attrs
    , *, is_package:bool
    ):
    #script
    #seed.pkg_tools.load_as_module.load_as_module_or_package_ex
    check_maybe_string(may_qname)
    check_maybe_string(may_dot_attrs)
    moudle_object = load_as_module_or_package_ex(
        may_qname, bare_name_source_path_pairs, is_package=is_package
        )
    return get_dot_attrs(moudle_object, may_dot_attrs)

def get_python_object_via_module_system(
    may_qname, may_dot_attrs
    ):
    #module
    #importlib.import_module
    '''
may_qname :: None | str
    # None | '' | 'xxx' | 'xxx.yyy'
    if ''|None:
        ==>> 'builtins'
may_dot_attrs :: None | str
    # None | '' | '.aaa' | '.aaa.bbb'
    if ''|None:
        ==>> the moudle object itself
'''
    check_maybe_string(may_qname)
    check_maybe_string(may_dot_attrs)

    qname = may_qname if may_qname else 'builtins'
    moudle_object = import_module(qname)
    return get_dot_attrs(moudle_object, may_dot_attrs)

def get_dot_attrs(moudle_object, may_dot_attrs):
    check_maybe_string(may_dot_attrs)
    if not may_dot_attrs:
        return moudle_object

    dot_attrs = may_dot_attrs
    if dot_attrs[0] != '.': raise ValueError
    return attrgetter(moudle_object, dot_attrs[1:])

via_case2get_python_object = \
    {ViaCase.ModuleSystem: get_python_object_via_module_system
    ,ViaCase.ScriptAsModule: get_python_object_via_script_as_module
    ,ViaCase.Exec: get_python_object_via_exec
    ,ViaCase.Eval: get_python_object_via_eval
    }

def get_python_object(via_case:ViaCase, *args, **kwargs):
    '''
args, kwargs
    see:
        get_python_object_via_*
            get_python_object_via_module_system
            get_python_object_via_script_as_module
            get_python_object_via_exec
            get_python_object_via_eval
'''
    if type(via_case) is not ViaCase: raise TypeError
    f = via_case2get_python_object[via_case]
    return f(*args, **kwargs)



###########################
class GetPythonObjectHelper:
    r'''
    ModuleSystem
        --module x.y.z --dot_attrs .XXX.YYY
    ScriptAsModule # to set the __name__
        --parent x.y [--name_with_path z@path/to/XXX.py]+ --dot_attrs .XXX.YYY

    #from file/stdin/arg
    Exec/Eval
        file
            --input_path path/to/XXX.py --encoding utf8]
        stdin
        arg --python_source
'''

    @staticmethod
    def ModuleSystem(*, module:'x.y.z', dot_attrs:'.X.Y'):
        return get_python_object_via_module_system(module, dot_attrs)
    @staticmethod
    def ScriptAsModule(*
        , parent:'x.y'
        , name_path_pair_strs:'[z@path/to/z.py, w@w.py]::[str]'
        , dot_attrs:'.X.Y', sep='@'
        ):
        f = parse_name_path_pair_str
        name_path_pairs = [f(s, sep) for s in name_path_pair_strs]
        if not name_path_pair_strs:
            return __class__.ModuleSystem(module=parent, dot_attrs=dot_attrs)
        return get_python_object_via_script_as_module(
                parent, name_path_pairs, dot_attrs, is_package=False)
    class __Exec_or_Eval:
        @classmethod
        def file(cls, *, input_path, encoding, dot_attrs):
            python_source = Path(input_path).read_text(encoding=encoding)
            return cls.arg(python_source=python_source, dot_attrs=dot_attrs)
        @classmethod
        def stdin(cls, *, dot_attrs):
            python_source = sys.stdin.read()
            return cls.arg(python_source=python_source, dot_attrs=dot_attrs)
    class Exec(__Exec_or_Eval):
        @classmethod
        def arg(cls, *, python_source, dot_attrs):
            return get_python_object_via_exec(python_source, dot_attrs)

    class Eval(__Exec_or_Eval):
        @classmethod
        def arg(cls, *, python_source, dot_attrs):
            return get_python_object_via_eval(python_source, dot_attrs)
    del __Exec_or_Eval

name_path_regex = re.compile('(?P<name>\w+)(?P<sep>[^\w])(?P<path>.*)', re.DOTALL)
name_path_pattern_fmt = r'(?P<name>\w+)\{sep}(?P<path>.*)'
def parse_name_path_pair_str(s, sep):
    if len(sep) != 1: raise ValueError
    #i = s.find(sep) if i < 0:

    m = name_path_regex.fullmatch(s)
    if not m or m.group('sep') != sep:
        name_path_pattern = name_path_pattern_fmt.format(sep=sep)
        raise ValueError(f'not a vaild name_path_pair_str {name_path_pattern!r}: {s!r}')
    name = m.group('name')
    path = m.group('path')
    if not name.isidentifier(): raise ValueError(f'not an identifier: {name!r}')
    return name, path

