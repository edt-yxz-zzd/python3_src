#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/app/find_forward_calls6haskell_src.py

nn_ns.app.find_forward_calls6haskell_src
py -m nn_ns.app.debug_cmd   nn_ns.app.find_forward_calls6haskell_src -x # -off_defs
py -m nn_ns.app.doctest_cmd nn_ns.app.find_forward_calls6haskell_src:__doc__ -ht # -ff -df
#######
from seed.pkg_tools.ModuleReloader import mk_doctestXmodule_reloader_
doctestXmodule_reloader = mk_doctestXmodule_reloader_('', 'nn_ns.app.find_forward_calls6haskell_src:__doc__', '-ht')
doctestXmodule_reloader(reload_first=False)
doctestXmodule_reloader()
#######

[[
源起:
e ../../python3_src/haskell_src/Framework4Translation__ver5__api_only.hs
由于构建时过于随意，导致调用依赖次序混乱
目标:避免循环调用
实现:十分粗略地进行语法分析，输出前置性调用
]]


'#'; __doc__ = r'#'
>>>


py_adhoc_call   nn_ns.app.find_forward_calls6haskell_src   ,iter_roughly_find_forward_calls6haskell_src_ :../../python3_src/haskell_src/Framework4Translation__ver5__api_only.hs

from nn_ns.app.find_forward_calls6haskell_src import *
]]]'''#'''
__all__ = r'''
iter_roughly_find_forward_calls6haskell_src_


regex4fn_begin
    regex4nonword
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
import re
from itertools import pairwise
#.from seed.tiny_.check import check_type_is, check_int_ge
#.
#.from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.from seed.for_libs.for_importlib__reload import clear_later_variables_if_reload_
#.clear_later_variables_if_reload_(globals(), '')
#.    # <<== seed.pkg_tools.ModuleReloader
#.from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_, force_lazy_imported_func_
#.repr_helper = lazy_import4func_('seed.helper.repr_input', 'repr_helper', __name__)
#.
#.lazy_import4funcs_('seed.tiny_.containers', 'mk_tuple,mk_immutable_seq,mk_immutable_seq5iterT_,mk_immutable_seq5iter__,mk_bytes5iter_', __name__)
#.if 0:from seed.tiny_.containers import mk_tuple,mk_immutable_seq,mk_immutable_seq5iterT_,mk_immutable_seq5iter__,mk_bytes5iter_
#.lazy_import4funcs_('seed.debug.print_err', 'print_err', __name__)
#.if 0:from seed.debug.print_err import print_err
#.lazy_import4funcs_('seed.helper.ifNone', 'ifNone,ifNonef', __name__)
#.if 0:from seed.helper.ifNone import ifNone,ifNonef
#.lazy_import4funcs_('seed.tiny_.funcs', 'echo,fst,snd', __name__)
#.if 0:from seed.tiny_.funcs import echo,fst,snd
#.lazy_import4funcs_('seed.types.Either', 'mk_Left,mk_Right', __name__)
#.if 0:from seed.types.Either import mk_Left,mk_Right
#.
#.
#.#.lazy_import4funcs_('seed.tiny', 'mk_tuple,print_err,ifNone:ifNone_', __name__)
#.#.if 0:from seed.tiny import mk_tuple,print_err,ifNone as ifNone_ #xxx:null_tuple #xxx:echo,fst,snd
#.
#.
#.from seed.helper.repr_input import repr_helper
#.from seed.tiny_._Base4repr import _Base4repr
        #sf._reset4repr(may_args4repr, may_kwds4repr)
        #sf._init4repr(*args4repr, **kwds4repr)
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError(Exception, StopIteration)


regex4single_line_comment = re.compile(r'(?:^|(?<=\n)) *--(?:(?: |\w).*)?(?:\n|$)')
regex4fn_begin = re.compile(r'(?:^|(?<=\n))\w+(?: *::|.* = )')
regex4nonword = re.compile(r'\W+')
def iter_roughly_find_forward_calls6haskell_src_(ipath, /, *, encoding='utf8'):
    with open(ipath, 'rt', encoding=encoding) as ifile:
        txt = ifile.read()
    txt
    txt = regex4single_line_comment.sub('', txt)
    def __():
        #xxx:yield 0
        for m in regex4fn_begin.finditer(txt):
            yield m.start()
        yield len(txt)
    nm4fn_words_pairs = []
        # :: [(nm4fn, [word])]
    for i, j in pairwise(__()):
        #if 0b00000:print(i, j)
        s = txt[i:j]
        words = regex4nonword.split(s)
        nm4fn = words[0]
        del words[0]
        nm4fn_words_pairs.append((nm4fn, words))
    nms4fn = set()
    for (nm4fn, words) in reversed(nm4fn_words_pairs):
        for word in sorted(set(words)):
            if word in nms4fn:
                yield (nm4fn, word)
        nms4fn.add(nm4fn)


__all__
#[f,g] = lazy_import4funcs_('nn_ns.app.find_forward_calls6haskell_src', 'f,g', __name__)
from nn_ns.app.find_forward_calls6haskell_src import *
