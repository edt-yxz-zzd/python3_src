
import sand
import re

# gb18030 not unicode xx tplNonChineseCharButInChineseBlock = re.compile('[ˉ-ゞ]')
def hz2num_gb2int(c):
    u = int.from_bytes(c.encode(sand.zh_cn_encoding), 'big')
    return u
def num2hz_int2gb(u):
    assert 0 < u < 2**16
    c = u.to_bytes(2, 'big').decode(sand.zh_cn_encoding)
    return c
firstNonChineseCharButInChineseBlock = hz2num_gb2int('ˉ')
lastNonChineseCharButInChineseBlock = hz2num_gb2int('ゞ')
def isNonChineseCharButInChineseBlock(c):
    u = hz2num_gb2int(c)
    return firstNonChineseCharButInChineseBlock <= u <= lastNonChineseCharButInChineseBlock


tplEnglishChar = re.compile('[a-zA-Zａ-ｚＡ-Ｚ]')
def isEnglishChar(c):
    return not not tplEnglishChar.match(c)

def isAscii(c):
    return ord(c) < 128


def getChar(fname, encoding):
    if isinstance(fname, str):
        with open(fname, encoding=encoding) as fin:
            return getCharFromFileObj(fin)
    fin = fname
    return getCharFromFileObj(fin)
def getCharFromFileObj(fin):
    ls = set()
    for line in fin:
        ls.update(line)
    return ls

def isChineseChar(c):
    encoding = sand.zh_cn_encoding
    return c.isidentifier() and c.isalpha() and \
           not isEnglishChar(c) and not isAscii(c) and \
           not isNonChineseCharButInChineseBlock(c) and \
           sand.includes(encoding, c) and \
           len(c.encode(encoding)) == 2

def henzi_used(fname, encoding=sand.zh_cn_encoding):
    ls = getChar(fname, encoding)

    removed_ls = []
    for c in list(ls):
        if isChineseChar(c):
            continue
        ls.remove(c)
        removed_ls.append(c)
    ls = list(ls)
    ls.sort()
    removed_ls.sort()
    
    henzi = ''.join(ls)
    removed = ''.join(removed_ls)
    return henzi, removed


def main(args = None):
    import argparse, sys

    parser = argparse.ArgumentParser(description='which Chinese Characters are in file')
    parser.add_argument('source', type=str, \
                        nargs='?', default=sys.stdin,
                        help='file name. if None, uses STDIN, "ctrl-c" to interrupt, "ctrl-z" + "enter" to end text.')

    parser.add_argument('-e', '--encoding', type=str, \
                        default=sand.zh_cn_encoding,
                        help='file encoding')
    parser.add_argument('-c', '--choice', type=int, choices=range(3),\
                        default=0,
                        help='choose what to be printed. 0:Chinese, 1:others, 2:both')

    if args == None:
        args = parser.parse_args()
    else:
        args = parser.parse_args(args)

    
    fname = args.source
    encoding = args.encoding
    choice = args.choice

    
    
    henzi, removed = henzi_used(fname, encoding)
    #print(choice)
    if choice != 1:
        print(henzi)
    if choice != 0:
        print(repr(removed))


def zhcn_encoding(encoding=sand.zh_cn_encoding):
    import unifont
    ls = []
    for i, j in unifont.gb18030_rng:
        for k in range(i,j):
            c = chr(k)
            if isChineseChar(c):
                bc = c.encode(encoding)
                if len(bc) == 2:
                    ls.append(bc)
                #xx assert len(ls[-1]) == 2

    ls.sort()
    ls = b''.join(ls)
    s = ls.decode(encoding)
    return s

    
            
def hz2num(c):
    encoding=sand.zh_cn_encoding
    h, l = c.encode(encoding)
    return h*1000 + l
def hznum2hl(n):
    return divmod(n, 1000)

def group_hz(txt):
    from data_structure import range_manager_t
    rm = range_manager_t()
    for c in txt:
        n = hz2num(c)
        rm.add((n, n+1))

    dc = dict()
    for i, j in rm:
        ih, il = hznum2hl(i)
        jh, jl = hznum2hl(j)
        assert 128 < ih == jh < 255
        if ih not in dc:
            dc[ih] = []
        dc[ih].append((il, jl))
    #assert len(dc) == 255 - 129 - 1

    hs = []
    rngs2 = [(64, 127), (128, 255)]
    for h in range(129, 255):
        if h not in dc:
            hs.append((h, []))
            continue
        rngs = dc[h]
        if rngs != rngs2:
            hs.append((h, rngs))

    return hs

def t():
    fname = 'hz_gb18030.utf8.zlib' # n21337
    calc_f = zhcn_encoding #lambda : zhcn_encoding()
    txt = sand.read_or_calc_xwrite(fname, calc_f)
    return group_hz(txt)
    [
        (161, [(165, 167), (169, 170)]),
        (162, []),
        (163, []),
        (164, [(161, 244)]),
        (165, [(161, 247)]),
        (166, [(161, 185), (193, 217)]),
        (167, [(161, 194), (209, 242)]),
        (168, [(64, 66), (161, 188), (189, 193), (197, 234)]),
        (169, [(96, 97), (99, 104)]),
        (170, [(64, 127), (128, 161)]),
        (171, [(64, 127), (128, 161)]),
        (172, [(64, 127), (128, 161)]),
        (173, [(64, 127), (128, 161)]),
        (174, [(64, 127), (128, 161)]),
        (175, [(64, 127), (128, 161)]),
        (215, [(64, 127), (128, 250)]),
        (248, [(64, 127), (128, 161)]),
        (249, [(64, 127), (128, 161)]),
        (250, [(64, 127), (128, 161)]),
        (251, [(64, 127), (128, 161)]),
        (252, [(64, 127), (128, 161)]),
        (253, [(64, 127), (128, 161)]),
        (254, [(64, 80), (85, 87), (90, 93), (95, 97), (98, 102),
               (104, 107), (111, 113), (114, 115), (119, 121),
               (122, 126), (128, 132), (133, 144), (146, 160)])
    ]

#print(t())

if __name__ == "__main__":
    main()

    fname = '魔王奶爸[盘古混沌].txt'









