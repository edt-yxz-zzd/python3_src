#__all__:goto
r'''[[[
e ../../python3_src/seed/pkg_tools/ModuleReloader.py
view ../../python3_src/nn_ns/app/doctest_cmd.py
    view ../../python3_src/seed/for_libs/for_doctest.py
    view ../../python3_src/seed/for_libs/for_importlib.py

seed.pkg_tools.ModuleReloader
py -m nn_ns.app.debug_cmd   seed.pkg_tools.ModuleReloader -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.pkg_tools.ModuleReloader:__doc__ -ht # -ff -df

[[
源起:
    debugging:e ../../python3_src/seed/int_tools/StepDecoder.py
using reload when debugging and patching many times:
    $ py -m nn_ns.app.doctest_cmd seed.int_tools.StepDecoder:__doc__ -ht # -ff -df
    -->:
    >>>> from seed.for_libs.for_doctest import main
    >>>> main('seed.int_tools.StepDecoder:__doc__ -ht'.split())
    >>>> reloader = ModuleReloader(['seed.int_tools.StepDecoder'])
    >>>> reloader()
    >>>> main('seed.int_tools.StepDecoder:__doc__ -ht'.split())
]]

[[
usage:doctest
from seed.pkg_tools.ModuleReloader import mk_module_reloader_
from seed.for_libs.for_doctest import main
main('seed.int_tools.StepDecoder:__doc__ -ht'.split())
reloader = mk_module_reloader_('seed.int_tools.StepDecoder')
reloader();main('seed.int_tools.StepDecoder:__doc__ -ht'.split())
-->:
from seed.pkg_tools.ModuleReloader import mk_doctestXmodule_reloader_
doctestXmodule_reloader = mk_doctestXmodule_reloader_('', 'seed.int_tools.StepDecoder:__doc__', '-ht')
doctestXmodule_reloader(reload_first=False)
doctestXmodule_reloader()
    ^Exception: ('dst exist:', (<module 'seed.int_tools.StepDecoder' from '/sdcard/0my_files/git_repos/python3_src/seed/int_tools/StepDecoder.py'>, 'repr_helper'), _LazyImport4Func('seed.helper.repr_input', 'repr_helper', 'seed.int_tools.StepDecoder', ''))
    ==>> ++『if not 'lazy_import4func_' in globals():』


]]
[[
usage:update this module
from seed.pkg_tools.ModuleReloader import mk_module_reloader_, mk_doctestXmodule_reloader_
reloader = mk_module_reloader_('seed.pkg_tools.ModuleReloader')
reloader()
from seed.pkg_tools.ModuleReloader import mk_module_reloader_, mk_doctestXmodule_reloader_
]]
[[
reload cause bug:
    view ../../python3_src/seed/int_tools/StepDecoder.py
===
惰性导入表达式重复定义，导致多次注入而出错
===
^Exception: ('dst exist:', (<module 'seed.int_tools.StepDecoder' from '/sdcard/0my_files/git_repos/python3_src/seed/int_tools/StepDecoder.py'>, 'repr_helper'), _LazyImport4Func('seed.helper.repr_input', 'repr_helper', 'seed.int_tools.StepDecoder', ''))
==>> ++『if not 'lazy_import4func_' in globals():』
]]
[[
reload cause bug:
    view ../../python3_src/seed/int_tools/StepDecoder.py
===
类型重复定义(包括:枚举类型)，而只初始化一次的惰性值包含旧类型的值，导致访问出错
===
#.>>> cases = [*_58_case2dr4rational]
#.>>> type(cases[0]) is _Case4scheme
#.False
#.>>> type(cases[0]).__module__
#.'seed.int_tools.StepDecoder'
#.>>> _Case4scheme.__module__
#.'seed.int_tools.StepDecoder'
#.>>> type(cases[0])
#.<enum 'CodecSchemeCase4StepDecoder4Rational'>
#.>>> _Case4scheme
#.<enum 'CodecSchemeCase4StepDecoder4Rational'>
==>>doctestXmodule_reloader() cause bug:『class _Case4scheme(Enum)』redefined, but『global _58_case2dr4rational』lazy init only once => KeyError
==>> ++『
if '_58_dr4int' in globals():
    del _58_dr4int, _58_case2dr4rational
』

]]

[[
==>>:
统一解决方案:
from seed.for_libs.for_importlib__reload import clear_later_variables_if_reload_
clear_later_variables_if_reload_(globals(), '')
]]



py_adhoc_call   seed.pkg_tools.ModuleReloader   @f
]]]'''#'''
__all__ = r'''
mk_module_reloader_
    ModuleReloader
mk_doctestXmodule_reloader_
    Doctest_X_ModuleReloader
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from importlib import import_module
from importlib import reload as inplace_reload# inplace reload <<== spec.loader.exec_module(module)
from seed.tiny_.check import check_all_, check_pseudo_qual_name #check_type_is, check_int_ge
#.from itertools import islice
#.
#.from seed.abc.abc__ver1 import abstractmethod, override, ABC
if not 'lazy_import4func_' in globals():
    from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_
    repr_helper = lazy_import4func_('seed.helper.repr_input', 'repr_helper', __name__)
    lazy_import4funcs_('seed.tiny', 'mk_tuple,print_err,mk_tuple__split_first_if_str', __name__)
    if 0:from seed.tiny import mk_tuple,print_err,mk_tuple__split_first_if_str #xxx:null_tuple #xxx:echo,fst,snd

    parse4module_qname_and_obj_qnames = lazy_import4func_('seed.for_libs.for_doctest', 'parse4module_qname_and_obj_qnames', __name__)
    lazy_import4func_('seed.for_libs.for_doctest', 'main', __name__, '_main4doctest_cmd')
    #from seed.for_libs.for_doctest import parse4module_qname_and_obj_qnames, main as _main4doctest_cmd
    _main4doctest_cmd
___end_mark_of_excluded_global_names__0___ = ...

def _4qnm4mdl(module_qname_and_obj_qnames__str, /):
    s = module_qname_and_obj_qnames__str
    j = s.find(':')
    if j == -1:
        if not s[-1] == '!': raise Exception(s)
    qnm4mdl = s[:j]
    return qnm4mdl
    parse4module_qname_and_obj_qnames(module_qname_and_obj_qnames__str)
    ...

class Doctest_X_ModuleReloader:
    def __init__(sf, extra_ordered_qnms4mdl, module_qname_and_obj_qnames__strs, options, /):
        'Iter qnm4mdl -> Iter str{format:(expect: "xxx.yyy!", "xxx.yyy:aaa.bbb,ccc")} -> Iter str{eg:"-ht"  "-ff", "-df"} -> None'
        sf.extra_ordered_qnms4mdl = mk_tuple(extra_ordered_qnms4mdl)
        sf.module_qname_and_obj_qnames__strs = mk_tuple(module_qname_and_obj_qnames__strs)
        sf.options = mk_tuple(options)
        #parse4module_qname_and_obj_qnames
        ordered_qnms4mdl = (*extra_ordered_qnms4mdl, *map(_4qnm4mdl, module_qname_and_obj_qnames__strs))
        sf.module_reloader = ModuleReloader(ordered_qnms4mdl)
    def __repr__(sf, /):
        return repr_helper(sf, sf.extra_ordered_qnms4mdl, sf.module_qname_and_obj_qnames__strs, sf.options)
    def __call__(sf, extra_options=(), /, *, reload_first=True):
        if reload_first:
            sf.module_reloader(to_import_if_not_existed=True)
        args = (*sf.module_qname_and_obj_qnames__strs, *sf.options, *extra_options)
        _main4doctest_cmd(args)

class ModuleReloader:
    'inplace_reload modules # [.ordered_qnms4mdl :: tuple{qnm4mdl/str}{order matter}{duplicated ok}]'
    def __init__(sf, ordered_qnms4mdl, /):
        ordered_qnms4mdl = mk_tuple(ordered_qnms4mdl)
        check_all_(check_pseudo_qual_name, ordered_qnms4mdl)
        sf._qnms = ordered_qnms4mdl
    def __repr__(sf, /):
        return repr_helper(sf, sf.ordered_qnms4mdl)
    @property
    def ordered_qnms4mdl(sf, /):
        '-> tuple{qnm4mdl/str}{order matter}{duplicated ok}'
        return sf._qnms
    def __call__(sf, /, *, to_import_if_not_existed=False):
        from sys import modules
        for qnm4mdl in sf.ordered_qnms4mdl:
            #bug:inplace_reload(qnm4mdl)
                #TypeError: reload() argument must be a module
            if to_import_if_not_existed and not qnm4mdl in modules:
                import_module(qnm4mdl)
            else:
                inplace_reload(modules[qnm4mdl])


def mk_module_reloader_(str__or__ordered_qnms4mdl, /):
    '(str|Iter qnm4mdl/str){order matter}{duplicated ok} -> ModuleReloader # using mk_tuple__split_first_if_str'
    ordered_qnms4mdl = mk_tuple__split_first_if_str(str__or__ordered_qnms4mdl, ',')
    ordered_qnms4mdl
    return ModuleReloader(ordered_qnms4mdl)

#.if __name__ == "__main__":
#.    raise NotImplementedError




def mk_doctestXmodule_reloader_(extra_ordered_qnms4mdl, module_qname_and_obj_qnames__strs, options, /):
    'Iter qnm4mdl -> Iter str{format:(expect: "xxx.yyy!", "xxx.yyy:aaa.bbb,ccc")} -> Iter str{eg:"-ht"  "-ff", "-df"} -> Doctest_X_ModuleReloader # using mk_tuple__split_first_if_str'
    extra_ordered_qnms4mdl = mk_tuple__split_first_if_str(extra_ordered_qnms4mdl)
    module_qname_and_obj_qnames__strs = mk_tuple__split_first_if_str(module_qname_and_obj_qnames__strs)
    options = mk_tuple__split_first_if_str(options)
    return Doctest_X_ModuleReloader(extra_ordered_qnms4mdl, module_qname_and_obj_qnames__strs, options)


__all__
#[mk_module_reloader_,mk_doctestXmodule_reloader_] = lazy_import4funcs_('seed.pkg_tools.ModuleReloader', 'mk_module_reloader_,mk_doctestXmodule_reloader_', __name__)
from seed.pkg_tools.ModuleReloader import mk_module_reloader_,mk_doctestXmodule_reloader_

#from seed.pkg_tools.ModuleReloader import ModuleReloader
#from seed.pkg_tools.ModuleReloader import Doctest_X_ModuleReloader
from seed.pkg_tools.ModuleReloader import *
