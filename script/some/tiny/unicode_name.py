


'''
CJK UNIFIED IDEOGRAPH-4E00
meaningless for Chinese characters...

'''

import unicodedata
import re
from data_structure.red_black_tree import RangeManager



# from icu\icu4c-52_1\data\unidata\norm2\uts46.txt
# 3400..4DB5  valid                     # 3.0  CJK UNIFIED IDEOGRAPH-3400..CJK UNIFIED IDEOGRAPH-4DB5

# 4E00..9FA5  valid                     # 1.1  CJK UNIFIED IDEOGRAPH-4E00..CJK UNIFIED IDEOGRAPH-9FA5
# 9FA6..9FBB  valid                     # 4.1  CJK UNIFIED IDEOGRAPH-9FA6..CJK UNIFIED IDEOGRAPH-9FBB
# 9FBC..9FC3  valid                     # 5.1  CJK UNIFIED IDEOGRAPH-9FBC..CJK UNIFIED IDEOGRAPH-9FC3
# 9FC4..9FCB  valid                     # 5.2  CJK UNIFIED IDEOGRAPH-9FC4..CJK UNIFIED IDEOGRAPH-9FCB
# 9FCC        valid                     # 6.1  CJK UNIFIED IDEOGRAPH-9FCC

# 20000..2A6D6valid                     # 3.1  CJK UNIFIED IDEOGRAPH-20000..CJK UNIFIED IDEOGRAPH-2A6D6

# 2A700..2B734valid                     # 5.2  CJK UNIFIED IDEOGRAPH-2A700..CJK UNIFIED IDEOGRAPH-2B734

# 2B740..2B81Dvalid                     # 6.0  CJK UNIFIED IDEOGRAPH-2B740..CJK UNIFIED IDEOGRAPH-2B81D

CJK_UNIFIED_IDEOGRAPH_rng_include_tail = [
    (0x3400, 0x4db5), (0x4e00, 0x9fcc),
    (0x20000, 0x2a6d6),
    (0x2a700, 0x2b734), (0x2B740, 0x2B81D)]
# == [(13312, 19893), (19968, 40908), (131072, 173782), (173824, 177972), (177984, 178205)]

gbk_hanzi_rng = [(19968, 40870), (63788, 63789), (63865, 63866), (63893, 63894), (63975, 63976), (63985, 63986), (64012, 64016), (64017, 64018), (64019, 64021), (64024, 64025), (64031, 64034), (64035, 64037), (64039, 64042),]


to_name = unicodedata.name
get_width = unicodedata.east_asian_width

ud_txt = r'D:\software\programming\library\icu\icu4c-52_1\data\unidata\UnicodeData.txt'

ofname = './named_data.txt.utf8'






def write(fname, s):
    b = s.encode('utf8')

    with open(fname, 'wb') as fout:
        fout.write(b)
    


def to_printable(c):
    if c.isspace() or not c.isprintable():
        c = repr(c)
    return c



def names():
    ls = []
    ns = set()
    dupnames = RangeManager()
    nonames = RangeManager()
    for i in range(0x110000):
        c = chr(i)
        name = to_name(c, None)
        if name is not None:
            if name in ns:
                print(name)
                dupnames.add((i, i+1))
            ns.add(name)
        else:
            name = ''
            nonames.add((i, i+1))
            
        c = to_printable(c)
        ls.append('{};{}'.format(c, name))

    print('dupnames = {}; nonames = {}'.format(dupnames, nonames))
    s = '\n'.join(ls)
    write(ofname, s)
    
    
def bad_code_point():
    'bad range [0xd800, 0xe000)'
    return 0xd800, 0xe000
    rm = RangeManager()
    ls = []
    for i in range(0x110000):
        c = chr(i)
        ls.append(c)

    s = '/'.join(ls)
    b = s.encode('utf8', errors='xmlcharrefreplace')

    with open(ofname, 'wb') as fout:
        fout.write(b)

    t = b.decode('utf8')
    p = r'\&\#[^;]+\;'
    tt = t.replace('///', '/?/')
    ttt = tt.split('/')
    assert len(ttt) == 0x110000

    bad_idx = [i for i, c in enumerate(ttt) if len(c) != 1]

    for i in bad_idx:
        rm.add((i, i+1))

    print(rm)
    [(55296, 57344)]
    [0xd800, 0xe000] # can't not encode by utf8


def f():
    ls = []
    for i in range(0x110000):
        c = chr(i)
        try:
            n = to_name(c)
        except:
            print(i)
            raise

        c = to_printable(c)
        ls.append('{!x};{};{}'.format(i, c, n))
    

    out = '\n'.join(ls)


    with open(ofname, 'w', encoding = 'utf8', errors='backslashreplace') as fout:
        fout.write(out)



def calc():
    with open(ud_txt, encoding = 'utf8') as fin:
        ls = list(fin)

    out = []
    widths = {}
    alls = set()
    for line in ls:
        code = line[:line.index(';')]
        code = int(code, base=16)
        c = chr(code)
        if c in alls:
            print(code, c)
        alls.add(c)

        w = get_width(c)
        if w not in widths:
            widths[w] = []
            print(w, repr(c), c)
        widths[w].append(c)
        
        if c.isspace():
            c = repr(c)
        else:
            pass
        out.append('{};{}'.format(c, line))
    #print(widths)
    for w, cs in widths.items():
        print(w, len(cs))
    raise
    out = ''.join(out)




    with open(ofname, 'w', encoding = 'utf8', errors='backslashreplace') as fout:
        fout.write(out)





