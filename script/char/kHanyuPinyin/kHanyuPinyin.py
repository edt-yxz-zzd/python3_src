
'2015 kHanyuPinyin.txt @https://github.com/mozillazg/pinyin-data'
path = r'kHanyuPinyin.txt'
'''
U+91CC: lǐ  # 里
U+91CD: zhòng,chóng,tóng  # 重
U+5973: nǚ,nǜ,rǔ  # 女

U+5463: móu,ḿ,m̀  # 呣
U+5514: wù,wú,ńg,ḿ  # 唔
U+55EF: ńg,ń,ňg,ň,ǹg,ǹ  # 嗯
U+54FD: gěng,yǐng,yìng,ńg,ń  # 哽
U+54B9: è,àn,ń  # 咹
U+3576: ňg,ň  # 㕶
U+54CF: hěn,ǹ,gén  # 哏
U+5638: fǔ,m̄  # 嘸
U+6B38: āi,ǎi,xiè,ế,éi,ê̌,ěi,ề,èi,ê̄  # 欸
U+8A92: xī,yì,ê̄,ế,éi,ê̌,ěi,ề,èi  # 誒
U+54FC: hēng,hng  # 哼
U+5535: ǎn,ng,n  # 唵
U+275C8: n  # 𧗈

hng 哼
m 呣唔嘸
n 𧗈㕶咹哏哽唵嗯
ng 哽唔唵嗯㕶
ê 欸誒

hng m n ng ê
nia re
U+35B8: xué,niā  # 㖸



ǹ  ň  ń ḿ


ˉˊˇˋ˙＾
¨
ê  ê̄  ế   ê̌  ề
m  m̄  ḿ   m̌  m̀
n  n̄  ń   ň  ǹ
'''

import re
from pprint import pprint


line_rex = re.compile(r'U\+(?P<ord>[0-9A-F]+):(?P<pinyin>[^#]+)(#.*)?')
def line2item(line):
    m = line_rex.fullmatch(line)
    if not m:
        raise ValueError('bad format: {!r}'.format(line))
    ord = int(m['ord'], 16)
    pinyin_str = m['pinyin'].strip()
    assert ' ' not in pinyin_str
    pinyin_ls = pinyin_str.split(',')
    ch = chr(ord)
    return ch, pinyin_ls

aoeiuv = '''\
aāáǎà
oōóǒò
eēéěè
iīíǐì
uūúǔù
üǖǘǚǜ
ê?ế?ề
n?ńňǹ
m?ḿ??
?̄ˊ̌̀\
'''
def init_aoeiuv_table():
    d = {}
    for line in aoeiuv.split():
        #print(line)
        #print(len(line))
        #assert len(line) == 5
        
        name = line[0]
        values = line[1:]
        L = len(d)
        d.update((line[i], (name, i)) for i in range(1, 5))
        #print(name)
        #assert len(d) == L + 4
    #print(len(d))
    #print(d)
    del d['?']
    assert len(d) == (6+1)*4 + 2 + 3 + 1
    def change_name(name):
        return '' if name == '?' else name
    d = {ch : (change_name(name), i) for ch, (name, i) in d.items()}

    name__ch_i_pairs__pairs = \
        [('ê', [('ê̄', 1), ('ê̌', 3)])
        ,('m', [('m̄', 1), ('m̌', 3), ('m̀', 4)])
        ,('n', [('n̄', 1)])
        ]
    for name, ch_i_pairs in name__ch_i_pairs__pairs :
        for ch, i in ch_i_pairs:
            d[ch] = (name, i)
    assert len(d) == (6+4)*4
    return d

aoeiuv_table = init_aoeiuv_table()
aoeiuv_keys = set(aoeiuv_table)
#rint(aoeiuv_table)


def marked_pinyin2pinyin_number(marked_pinyin):
    main = set(marked_pinyin) & aoeiuv_keys
    #print(main, marked_pinyin, set(marked_pinyin), aoeiuv_keys)
    L = len(main)
    if L == 1:
        main_old, = main
        main_new, number = aoeiuv_table[main_old]
        pinyin = marked_pinyin.replace(main_old, main_new)
        number = str(number)
    elif L == 0:
        pinyin = marked_pinyin
        number = '0'
    else:
        raise ValueError('not PinYin: {!s}'.format(marked_pinyin))
    pinyin_number = pinyin + number
    # error: pinyin_number = pinyin_number.replace('ê', 'e')
    pinyin_number = pinyin_number.replace('ü', 'v')
    return pinyin_number

assert len('m̄') == 2
assert 'm̄'.replace('ˉ', '') == 'm̄'
assert 'mˉ'.replace('ˉ', '') == 'm'
assert marked_pinyin2pinyin_number('m̄') == 'm1'
#assert marked_pinyin2pinyin_number('êˊ') == 'e2'
#assert marked_pinyin2pinyin_number('êˊ') == 'ê2'
assert marked_pinyin2pinyin_number('eˊ') == 'e2'
assert marked_pinyin2pinyin_number('zhòng') == 'zhong4'
assert marked_pinyin2pinyin_number('zhong') == 'zhong0'

ls = []
with open(path, encoding='utf8') as fin:
    for line in fin:
        line = line.strip()
        item = ch, pinyin_ls = line2item(line)
        pinyin_ls = list(map(marked_pinyin2pinyin_number, pinyin_ls))
        ls.append((ch, pinyin_ls))


with open('kHanyuPinyin__hanzi_pinyins_pairs.py', 'x', encoding='utf8') as fout:
    fout.write('hanzi_pinyins_pairs = \\\n')
    pprint(ls, stream = fout)
if 0:
    with open('kHanyuPinyin_new.txt', 'x', encoding='utf8') as fout:
        for ch, pinyin_ls in ls:
            line = '{}:{}\n'.format(ch, ','.join(pinyin_ls))
            fout.write(line)


