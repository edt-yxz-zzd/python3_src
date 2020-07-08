



import unicodedata as U



#UnicodeDecodeError: 'gb2312' codec can't decode byte 0xd7 in position 0: illegal multibyte sequence
#   0xA0 + 55
#   b'\xd7\xfa'
#UnicodeDecodeError: 'gb2312' codec can't decode byte 0xaf in position 0: illegal multibyte sequence
#   0xA0 + 15
OFFSET = 0xA0 # +160 == +128 +32
rng = range(1, 94+1)
encoding = 'gb2312'
count_CJK = 0
count_non_CJK = 0
rngs = [(10,15), (88,94), (1,9)]
for i in rng:
  if any(a<=i<=b for a,b in rngs):
    continue
  for j in rng:
    if i == 55 and j >= 90: continue
    bs = bytes([OFFSET+i, OFFSET+j])
    try:
        char = bs.decode(encoding)
    except:
        print(str(bs))
        raise
    if len(char) != 1: raise logic-error
    if not U.name(char).startswith('CJK'):
        print(char)
        count_non_CJK += 1
    else:
        count_CJK += 1
#print(f'count_CJK={count_CJK}, count_non_CJK={count_non_CJK}')
assert count_CJK == 6763
assert count_non_CJK == 0

'''
    NOTE: GB2312::55区90-94未编码
        GB2312::汉字 = [16..87]*[1..94] - [55]*[90..94]
            total = (87-16+1)*94 - 5 = 6763
'''

'''
from cjkradlib import RadicalFinder
finder = RadicalFinder(lang='zh')  # default is 'zh'
result = finder.search('麻')
print(result.compositions)  # ['广', '林']
print(result.supercompositions)  # ['摩', '魔', '磨', '嘛', '麽', '靡', '糜', '麾']
print(result.variants)  # ['菻']




Examples

Get characters by pronunciation (here: “국” in Korean):

    >>> from cjklib import characterlookup
    >>> cjk = characterlookup.CharacterLookup('T')
    >>> cjk.getCharactersForReading(u'국', 'Hangul')
    [u'匊', u'國', u'局', u'掬', u'菊', u'跼', u'鞠', u'鞫', u'麯', u'麴']

Get stroke order of characters:

    >>> cjk.getStrokeOrder(u'说')
    [u'㇔', u'㇊', u'㇔', u'㇒', u'㇑', u'㇕', u'㇐', u'㇓', u'㇟']

Convert pronunciation data (here from Pinyin to IPA):

    >>> from cjklib.reading import ReadingFactory
    >>> f = ReadingFactory()
    >>> f.convert(u'lǎoshī', 'Pinyin', 'MandarinIPA')
    u'lau˨˩.ʂʅ˥˥'

Access a dictionary (here using Jim Breen’s EDICT):

    >>> from cjklib.dictionary import EDICT
    >>> d = EDICT()
    >>> d.getForTranslation('Tokyo')
    [EntryTuple(Headword=u'東京', Reading=u'とうきょう', Translation=u'/(n) Tokyo (current capital of Japan)/(P)/')]

'''

'''
from cjkradlib import characterlookup
cjk = characterlookup.CharacterLookup('T')
ls = cjk.getDecompositionEntries('攀')
tree = cjk.getDecompositionTreeList('攀')
print(ls)
print(tree)
'''

from cjkradlib import RadicalFinder
finder = RadicalFinder(lang='zh')  # default is 'zh'
result = finder.search('攀')
print(type(result))
print('\n'.join(dir(result)))
print(result.compositions)



