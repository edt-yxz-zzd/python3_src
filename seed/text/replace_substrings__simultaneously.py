#__all__:goto
r'''[[[
e ../../python3_src/seed/text/replace_substrings__simultaneously.py
see:
    from string import Template

seed.text.replace_substrings__simultaneously
py -m nn_ns.app.debug_cmd   seed.text.replace_substrings__simultaneously -x
py -m nn_ns.app.doctest_cmd seed.text.replace_substrings__simultaneously:__doc__ -ht
py_adhoc_call   seed.text.replace_substrings__simultaneously   @f




>>> replace_substrings__simultaneously_([('a',r'ab\0'), ('b', r'ba\0')], 'aabbabba', str_vs_re=False)
'ab\\0ab\\0ba\\0ba\\0ab\\0ba\\0ba\\0ab\\0'
>>> replace_substrings__simultaneously_([('a',r'ab\0'), ('b', r'ba\0')], 'aabbabba', str_vs_re=True)
'ab\\0ab\\0ba\\0ba\\0ab\\0ba\\0ba\\0ab\\0'

>>> replace_substrings__simultaneously_([('a',r'aak'), ('aa', r'gaa')], 'aabbabba', str_vs_re=False)
'gaabbaakbbaak'
>>> replace_substrings__simultaneously_([('a',r'aak'), ('aa', r'gaa')], 'aabbabba', str_vs_re=True)
'gaabbaakbbaak'

>>> replace_substrings__simultaneously_([('aa', r'gaa'), ('a',r'aak')], 'aabbabba', str_vs_re=False)
'gaabbaakbbaak'
>>> replace_substrings__simultaneously_([('aa', r'gaa'), ('a',r'aak')], 'aabbabba', str_vs_re=True)
'gaabbaakbbaak'

#]]]'''
__all__ = r'''
ReplaceSubstringsSimultaneously
    replace_substrings__simultaneously_
        replace_substrings__simultaneously__str
        replace_substrings__simultaneously__regex

'''.split()#'''
__all__

import re
from seed.text.make_strings_pattern import make_strings_pattern
from seed.tiny_.check import check_type_is
from seed.tiny_.containers import mk_tuple
from seed.tiny_.funcs import fst, snd


class ReplaceSubstringsSimultaneously:
    def __init__(sf, sub_repl_pairs, /, *, str_vs_re:bool):
        check_type_is(bool, str_vs_re)
        #sub_repl_pairs = mk_tuple(sub_repl_pairs)
        sub_repl_pairs = list(sub_repl_pairs)
        for sub, repl in sub_repl_pairs:
            check_type_is(str, sub)
            check_type_is(str, repl)
        sub_repl_pairs.sort(key=lambda p:-len(p[0]))
            #longer before shorter

        sf._sub_repl_pairs = sub_repl_pairs
        sf._str_vs_re = str_vs_re
        _init = sf._init4str if not str_vs_re else sf._init4re
        _init(sub_repl_pairs)
    def _init4str(sf, sub_repl_pairs, /):
        sf._sub2repl = dict(sub_repl_pairs)
        sf._rex = re.compile(make_strings_pattern(_fsts_(sub_repl_pairs)))
    def _repl4str(sf, m, /):
        sub = m.group(0)
        return sf._sub2repl[sub]
    def _init4re(sf, sub_repl_pairs, /):
        j2sub = [*_fsts_(sub_repl_pairs)]
        j2regex = [*map(re.compile, j2sub)]
        j2num_groups = [regex.groups for regex in j2regex]
        new_igroups = [1]
        ig = 1
        for num_groups in j2num_groups:
            ig += num_groups+1
            new_igroups.append(ig)
        new_igroups.pop()

        sf._rex = re.compile('|'.join(f'({sub!s})' for sub, repl in sub_repl_pairs))
        sf._new_igroups = new_igroups

    def _repl4re(sf, m, /):
        for j, ig in enumerate(sf._new_igroups):
            if not None is (s := m.group(ig)):
                break
        else:
            raise 000
        j, s
        return sf._sub_repl_pairs[j][1]
    def sub(sf, txt, /):
        f = sf._repl4str if not sf._str_vs_re else sf._repl4re
        return sf._rex.sub(f, txt)


def replace_substrings__simultaneously_(sub_repl_pairs, txt, /, *, str_vs_re:bool):
    return ReplaceSubstringsSimultaneously(sub_repl_pairs, str_vs_re=str_vs_re).sub(txt)

def replace_substrings__simultaneously__str(sub_repl_pairs, txt, /):
    return replace_substrings__simultaneously_(sub_repl_pairs, txt, str_vs_re=False)
def replace_substrings__simultaneously__regex(sub_repl_pairs, txt, /):
    return replace_substrings__simultaneously_(sub_repl_pairs, txt, str_vs_re=True)

def _fsts_(pairs, /):
    return (a for a, _ in pairs)

__all__
from seed.text.replace_substrings__simultaneously import replace_substrings__simultaneously_, replace_substrings__simultaneously__str, replace_substrings__simultaneously__regex, ReplaceSubstringsSimultaneously
from seed.text.replace_substrings__simultaneously import *
