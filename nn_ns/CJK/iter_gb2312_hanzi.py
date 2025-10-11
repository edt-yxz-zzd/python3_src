r'''[[[
e ../../python3_src/nn_ns/CJK/iter_gb2312_hanzi.py

py -m nn_ns.CJK.iter_gb2312_hanzi
[gb2312 |<=| {0x4E00..=0x9FA0} == [一..=龠]]
[gb2312 |<=| {0x4E00..<0xA000}]

#]]]'''#'''
__all__ = ['iter_gb2312_hanzi']

import unicodedata as U
def iter_gb2312_hanzi():
    count=0
    OFFSET = 0xA0
    encoding = 'gb2312'
    total = 6763
    for i in range(16, 87+1):
        for j in range(1, 94+1):
            if i == 55 and j >= 90: continue
            bs = bytes([i+OFFSET, j+OFFSET])
            char = bs.decode(encoding)
            assert len(char) == 1
            assert U.name(char).startswith('CJK')
            count += 1
            yield char
    assert count == total


def main():
    from seed.data_funcs.rngs import make_Ranges, sorted_ints_to_iter_nontouch_ranges
    it = iter_gb2312_hanzi()
    js = sorted(map(ord, it))
    rngs = sorted_ints_to_iter_nontouch_ranges(js)
    ranges = make_Ranges(rngs)
    assert 6763 == ranges.len_ints()
    assert 3542 == ranges.len_rngs()
    assert (0x4E00, 0x4E02) == (19968, 19970) == ranges.ranges[0]
    assert (0x9F9F, 0x9FA1) == (40863, 40865) == ranges.ranges[-1]
    assert 0x4E00 == js[0]
    assert 0x9FA0 == js[-1]
        #=>: [gb2312 |<=| {0x4E00..=0x9FA0}]
        #=>: [gb2312 |<=| {0x4E00..<0xA000}]
    r'''[[[
    view others/app/gvim/regex_cjk.txt
    [〇\uE600-\uE6CF\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF\U00020000-\U0003FFFF]
    \u4E00-\u9FFF:最初汉字区

[[
e ../lots/NOTE/unicode/cjk/汉字区.txt
for j in range(0x9FA0,0xA000):print(hex(j), chr(j))
0x9fa0 龠
0x9fa1 龡
... ...
... ...
0x9fed 鿭
0x9fee 鿮
0x9fef 鿯
0x9ff0 鿰
... ...
... ...
0x9ffb 鿻
0x9ffc 鿼
0x9ffd �
0x9ffe �
0x9fff �
    ==>>字体:unicode_ver11:[0x4E00..=0x9FEF]
    ==>>终端:unicode_ver13:[0x4E00..=0x9FFC]
]]
[[
import unicodedata as U
for j in range(0x9FA0,0xA000):print(hex(j), U.name(chr(j)))
... ...
0x9fff CJK UNIFIED IDEOGRAPH-9FFF
  ==>>py3_11_9.unicodedata:unicode_ver14:[0x4E00..=0x9FFF]
]]





e ../lots/NOTE/unicode/cjk/汉字区.txt
    unicode_ver11:[0x4E00..=0x9FEF]
    unicode_ver13:[0x4E00..=0x9FFC]
    unicode_ver14:[0x4E00..=0x9FFF]



    #]]]'''#'''

if __name__ == "__main__":
    main()

from nn_ns.CJK.iter_gb2312_hanzi import iter_gb2312_hanzi
from nn_ns.CJK.iter_gb2312_hanzi import *
