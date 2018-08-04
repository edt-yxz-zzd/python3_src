
from kHanyuPinyin__hanzi_pinyins_pairs import hanzi_pinyins_pairs
from itertools import chain

allHanyuPinyin_set = set(chain.from_iterable(
        pinyins for _, pinyins in hanzi_pinyins_pairs))
allHanyuPinyin_list = sorted(allHanyuPinyin_set)

#rint(allHanyuPinyin_list)
#rint(len(allHanyuPinyin_list))
assert len(allHanyuPinyin_list) == 1457


def remove_number(pinyin):
    assert '0' <= pinyin[-1] <= '4'
    return pinyin[:-1]
allHanyuPinyinPrime_set = set(map(remove_number, allHanyuPinyin_set))
allHanyuPinyinPrime_list = sorted(allHanyuPinyinPrime_set)
#rint(allHanyuPinyinPrime_list)
#rint(len(allHanyuPinyinPrime_list))
assert len(allHanyuPinyinPrime_list) == 420

with open('allHanyuPinyinPrime_list.txt', 'x', encoding='utf8') as fout:
    fout.write('\n'.join(allHanyuPinyinPrime_list))

