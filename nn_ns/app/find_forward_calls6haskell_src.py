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
regex4single_line_comment
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
import re
from itertools import pairwise
___end_mark_of_excluded_global_names__0___ = ...



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
