#__all__:goto
r'''[[[
e ../../python3_src/seed/text/pack_char_set.py
from:
    view ../../python3_src/nn_ns/CJK/CJK_common/save_load_hanzi2pinyins.py



seed.text.pack_char_set
py -m nn_ns.app.debug_cmd   seed.text.pack_char_set -x
py -m nn_ns.app.doctest_cmd seed.text.pack_char_set:__doc__ -ff -v
py_adhoc_call   seed.text.pack_char_set   @f
>>> from seed.text.pack_char_set import pack_char_set_, pack_char_sets_, pack_char_setvary_depth_

>>> from seed.text.pack_char_set import pack_ordered_strs_, pack_ordered_strss_, pack_ordered_strsvary_depth_

>>> from seed.text.pack_char_set import chain_until_str_, chain_until_char_

>>> [*chain_until_str_([[], '', 'a', 'bc', ['def', ['gh', ['mn'], 'pq']], 'xyz'])]
['', 'a', 'bc', 'def', 'gh', 'mn', 'pq', 'xyz']
>>> [*chain_until_char_([[], '', 'a', 'bc', ['def', ['gh', ['mn'], 'pq']], 'xyz'])]
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'm', 'n', 'p', 'q', 'x', 'y', 'z']

>>> pack_char_set_([*'bbbaaayyyaaa000bbb'])
'0aby'
>>> pack_char_set_(['bbbaaayyyaaa000bbb', '77775553335555666'])
Traceback (most recent call last):
    ...
TypeError: ord() expected a character, but string of length 18 found
>>> pack_char_sets_(['bbbaaayyyaaa000bbb', '77775553335555666'])
'03567aby'
>>> pack_char_setvary_depth_(['bbbaaayyyaaa000bbb', '77775553335555666'])
'03567aby'
>>> pack_char_setvary_depth_([[], '', 'a', 'bc', ['def', ['gh', ['mn'], 'pq']], 'xyz', 'gggg'])
'abcdefghmnpqxyz'





>>> pack_ordered_strs_([*'bbbaaayyyaaa000bbb'])
'bbbaaayyyaaa000bbb'
>>> pack_ordered_strs_(['bbbaaayyyaaa000bbb', '77775553335555666'])
'bbbaaayyyaaa000bbb77775553335555666'
>>> pack_ordered_strss_(['bbbaaayyyaaa000bbb', '77775553335555666'])
'bbbaaayyyaaa000bbb77775553335555666'
>>> pack_ordered_strsvary_depth_(['bbbaaayyyaaa000bbb', '77775553335555666'])
'bbbaaayyyaaa000bbb77775553335555666'
>>> pack_ordered_strsvary_depth_([[], '', 'a', 'bc', ['def', ['gh', ['mn'], 'pq']], 'xyz', 'gggg'])
'abcdefghmnpqxyzgggg'





#]]]'''
__all__ = r'''
    pack_char_set_
    pack_char_sets_
    pack_char_setvary_depth_

    pack_ordered_strs_
    pack_ordered_strss_
    pack_ordered_strsvary_depth_

    chain_until_str_
    chain_until_char_
'''.split()#'''
__all__



from seed.tiny import chains

def pack_char_set_(char_set, /):
    return ''.join(map(chr, sorted(set(map(ord, char_set)))))

def pack_char_sets_(char_sets, /):
    return pack_char_set_(chains(char_sets))

def pack_char_setvary_depth_(char_setvary_depth, /):
    return pack_char_set_(chain_until_char_(char_setvary_depth))



def pack_ordered_strs_(strs, /):
    return ''.join(strs)
def pack_ordered_strss_(strss, /):
    return pack_ordered_strs_(chains(strss))
def pack_ordered_strsvary_depth_(strsvary_depth, /):
    return pack_ordered_strs_(chain_until_str_(strsvary_depth))



def chain_until_str_(char_setvary_depth, /):
    '-> Iter str'
    if type(char_setvary_depth) is str:
        return iter([char_setvary_depth])
    return chains(map(_chain_until_str, char_setvary_depth))

def chain_until_char_(char_setvary_depth, /):
    '-> Iter char'
    if type(char_setvary_depth) is str:
        #-> Iter char
        return iter(char_setvary_depth)
    return chains(map(_chain_until_char, char_setvary_depth))
        # map(_chain_until_char, char_setvary_depth) :: Iter (Iter char)
        # chains(map(_chain_until_char, char_setvary_depth)) :: Iter char
_chain_until_str = chain_until_str_
_chain_until_char = chain_until_char_










from seed.text.pack_char_set import pack_char_set_, pack_char_sets_, pack_char_setvary_depth_
from seed.text.pack_char_set import pack_ordered_strs_, pack_ordered_strss_, pack_ordered_strsvary_depth_

from seed.text.pack_char_set import chain_until_str_, chain_until_char_
from seed.text.pack_char_set import *
