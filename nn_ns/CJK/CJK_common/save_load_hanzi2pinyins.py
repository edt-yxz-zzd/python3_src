#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/CJK/CJK_common/save_load_hanzi2pinyins.py

[[output format:

pacted_txt = \s* pacted_txt4sorted_parts   \s*   ',,,'   \s*   pacted_txt4unsorted_parts \s*

pacted_txt4sorted_parts = STAR_JOIN<\s+>( pinyin ':' hz+ )

pacted_txt4unsorted_parts = STAR_JOIN<\s+>(hz ':' STAR_JOIN<','>(pinyin))

eg:
xxx5:囗囗囗囗
xxx5:囗囗囗囗
,,,
囗:xxx5,xxx5
囗:xxx5,xxx5

]]

nn_ns.CJK.CJK_common.save_load_hanzi2pinyins
py -m nn_ns.app.debug_cmd   nn_ns.CJK.CJK_common.save_load_hanzi2pinyins -x
py -m nn_ns.app.doctest_cmd nn_ns.CJK.CJK_common.save_load_hanzi2pinyins:__doc__ -ff -v
py_adhoc_call   nn_ns.CJK.CJK_common.save_load_hanzi2pinyins   @f



#for user:
from nn_ns.CJK.CJK_common.save_load_hanzi2pinyins import save8py_src

#for auto-generated:
from nn_ns.CJK.CJK_common.save_load_hanzi2pinyins import parse as _parse


#pair:
from nn_ns.CJK.CJK_common.save_load_hanzi2pinyins import pack, parse

#util
xxx from nn_ns.CJK.CJK_common.save_load_hanzi2pinyins import pack_char_set_
from seed.text.pack_char_set import pack_char_set_, pack_char_sets_, pack_char_setvary_depth_




#]]]'''
__all__ = r'''
save8py_src
    pack
parse

'''.split()#'''
__all__


from seed.text.pack_char_set import pack_char_set_, pack_char_sets_, pack_char_setvary_depth_
from seed.text.contains_spaces import contains_spaces, check_contains_no_spaces
from seed.tiny import chains, check_bool, ifNone
from seed.tiny import fmap4dict_value, group4dict_value
from seed.mapping_tools.dict_op import inv__k2v_to_v2k, inv__k2v_to_v2ks, inv__k2vs_to_v2k, inv__k2vs_to_v2ks
from seed.iters.iter_unique_by_hash import remove_duplicates_by_hash
from seed.iters.is_sorted import is_sorted
from collections.abc import Sequence #Set, Mapping


def determine__pinyins_ordered(hanzi2pinyins, *, tribool__pinyins_ordered:bool):
    if tribool__pinyins_ordered is ...:
        #pinyins_ordered = (all(isinstance(pinyins, Sequence) for pinyins in hanzi2pinyins.values()) and not all(map(is_sorted, hanzi2pinyins.values())))
        #xxx pinyins_ordered = True
        pinyins_ordered = all(isinstance(pinyins, Sequence) for pinyins in hanzi2pinyins.values())
    else:
        pinyins_ordered = tribool__pinyins_ordered
    check_bool(pinyins_ordered)
    return pinyins_ordered

def tuple_sorted_(ls):
    return tuple(sorted(ls))

def __():
  def pack_char_set_(char_set):
    return ''.join(map(chr, sorted(set(map(ord, char_set)))))


def pack(hanzi2pinyins, *, pinyins_ordered:bool, partition_by_single_pinyin:bool):
    check_bool(pinyins_ordered)
    check_bool(partition_by_single_pinyin)
    if not set(map(len, hanzi2pinyins)) <= {1}: raise ValueError

    #T = tuple if pinyins_ordered else frozenset
    hanzi2pinyins = fmap4dict_value(remove_duplicates_by_hash, hanzi2pinyins)
        # {hz:tuple<pinyin>}




    all_chars = pack_char_sets_([hanzi2pinyins.keys(), chains(chains(hanzi2pinyins.values()))])

    #bug:if not len(all_chars.split()) <= 1: raise ValueError('contain spaces')
    check_contains_no_spaces(all_chars)
    if ':' in all_chars: raise ValueError('contain ":"')
    if ',' in all_chars: raise ValueError('contain ","')



    if not pinyins_ordered:
        hanzi2pinyins = fmap4dict_value(tuple_sorted_, hanzi2pinyins)
        # {hz:tuple<pinyin>}

    if partition_by_single_pinyin:
        #依照汉字是否单音进行分隔
        is_ok = lambda ls:len(ls)==1
    else:
        #依照拼音序列是否升序进行分隔
        #   但 其实 多音字 数量不多，而且 汉字utf8编码 很多3字节以上，...改为 上面 依照汉字是否单音进行分隔
        is_ok = lambda ls:ls and is_sorted(ls)

    is_sorted2hanzi2pinyins = group4dict_value(is_ok, hanzi2pinyins)
        # 『ls and ...』==>> sorted_parts所有汉字有拼音，不至于反转后丢失

    if 0:
        #bug: key may not exist
        sorted_parts = is_sorted2hanzi2pinyins[True]
        unsorted_parts = is_sorted2hanzi2pinyins[False]

    sorted_parts = is_sorted2hanzi2pinyins.get(True, {})
    unsorted_parts = is_sorted2hanzi2pinyins.get(False, {})



    if 1:
        ######################
        sorted_parts
            # change to {pinyin: sorted[hz]}
        assert all(sorted_parts.values())
        pinyin2hzs = inv__k2vs_to_v2ks(sorted_parts)
            #<<==sorted_parts所有汉字有拼音，不至于反转后丢失
        pinyin2hzs_str = fmap4dict_value(pack_char_set_, pinyin2hzs)
        s2s4sd = pinyin2hzs_str
            #no『,』
        ######################
    if 1:
        ######################
        unsorted_parts
            # keep {hz: unsorted[pinyin]}
        hanzi2pinyins_str = fmap4dict_value(','.join, unsorted_parts)
        s2s4un = hanzi2pinyins_str
        ######################

    txt4sd, txt4un = ('\n'.join(f'{t}:{s}' for t,s in sorted(s2s.items())) for s2s in [s2s4sd, s2s4un])
    assert not ',' in txt4sd
    txt = '\n'.join([txt4sd, ',,,', txt4un])

    #assert parse(txt, pinyins_ordered=pinyins_ordered) == hanzi2pinyins
    assert parse(txt) == hanzi2pinyins
    return txt

def parse(txt, *, pinyins_ordered:bool):
    check_bool(pinyins_ordered)
def parse(txt):
    txt4sd, txt4un = txt.split(',,,')
    sorted_parts = _parse__unorder(txt4sd)
        # unorder hence can be sorted
    unsorted_parts = _parse__order(txt4un)
        # unsorted must be treated ordered
    hanzi2pinyins = {**sorted_parts, **unsorted_parts}
    return hanzi2pinyins
def _parse__order(txt):
    return dict(_parse__order__impl(txt))
def _parse__order__impl(txt):
    ss = txt.split()
    for hz_s in ss:
        [hz],s = hz_s.split(':')
        pinyins = s.split(',')
        yield hz, tuple(pinyins)
def _parse__unorder(txt):
    ss = txt.split()
    pinyin2hzs_str = dict(pinyin_hzs.split(':') for pinyin_hzs in ss)
    hanzi2pinyins = inv__k2vs_to_v2ks(pinyin2hzs_str)
    hanzi2pinyins = fmap4dict_value(tuple_sorted_, hanzi2pinyins)
    return hanzi2pinyins

_fmt4out = """\
#hanzi2pinyins generated by {nm4data_mkr}

from nn_ns.CJK.CJK_common.save_load_hanzi2pinyins import parse as {alias4parse_func}

{nm4varable4hanzi2pinyins} = {alias4parse_func}(r'''
{txt}
'''#'''
)
"""#"""
(
#, pinyins_ordered={pinyins_ordered}
)

"""#"""

def save8py_src(hanzi2pinyins, *, nm4varable4hanzi2pinyins, nm4data_mkr, partition_by_single_pinyin:bool, tribool__pinyins_ordered=..., alias4parse_func='_parse'):
    pinyins_ordered = determine__pinyins_ordered(hanzi2pinyins, tribool__pinyins_ordered=tribool__pinyins_ordered)
    txt = pack(hanzi2pinyins, pinyins_ordered=pinyins_ordered, partition_by_single_pinyin=partition_by_single_pinyin)
    py_src = _fmt4out.format(txt=txt, pinyins_ordered=pinyins_ordered, nm4varable4hanzi2pinyins=nm4varable4hanzi2pinyins, nm4data_mkr=nm4data_mkr, alias4parse_func=alias4parse_func)
    return py_src

#pkg, basename


from nn_ns.CJK.CJK_common.save_load_hanzi2pinyins import save8py_src
from nn_ns.CJK.CJK_common.save_load_hanzi2pinyins import parse
from nn_ns.CJK.CJK_common.save_load_hanzi2pinyins import *
