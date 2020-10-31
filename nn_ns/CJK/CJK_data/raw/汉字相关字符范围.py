
r"""
rename/move file:
    script/ls笔顺码字符范围.py
    -->
    ../../python3_src/nn_ns/CJK/CJK_data/raw/汉字相关字符范围.py

    mv -n -T    /storage/emulated/0/0my_files/git_repos/txt_phone/txt/script/ls笔顺码字符范围.py     /storage/emulated/0/0my_files/git_repos/python3_src/nn_ns/CJK/CJK_data/raw/汉字相关字符范围.py


======after mv
from nn_ns.CJK.CJK_data.raw.汉字相关字符范围 import union_ranges

py -m nn_ns.CJK.CJK_data.raw.汉字相关字符范围 -do ls笔顺码字符范围__closed_rngs > ~/tmp/ls笔顺码字符范围.txt
py -m nn_ns.CJK.CJK_data.raw.汉字相关字符范围 -do cmp3
py -m nn_ns.CJK.CJK_data.raw.汉字相关字符范围 -do prepare_for_汉字粗拆分 -o ~/tmp/汉字粗拆分working.txt
py -m nn_ns.CJK.CJK_data.raw.汉字相关字符范围 -do prepare_for_2汉字粗拆分2 -o ~/tmp/2汉字粗拆分working2.txt

======before mv

py script/ls笔顺码字符范围.py -do ls笔顺码字符范围__closed_rngs > ~/tmp/ls笔顺码字符范围.txt

view /storage/emulated/0/0my_files/tmp/ls笔顺码字符范围.txt
    1709 lines!!!!

====
e script/ls笔顺码字符范围.py

####view ../../python3_src/seed/
view ../../python3_src/seed/data_funcs/rngs.py


data from
    view ../../python3_src/nn_ns/CJK/CJK_data/raw/汉字Unicode编码范围.txt
    view ../../python3_src/nn_ns/CJK/CJK_data/汉字笔顺.py
#"""



__all__ = """
    union_ranges
        mk笔顺码字符范围__rngs
            load_汉字到笔顺码
        closed_rngs__unicode_13_0_0
        closed_rngs__www
    show_hex_uint_pairs
    rngs_to_closed_rngs
    closed_rngs_to_rngs
        closed_rngs_to_sorted_rngs
        closed_rngs_to_Range
    """.split()
    #ls笔顺码字符范围__closed_rngs
    #cmp3
    #prepare_for_汉字粗拆分








from seed.tiny import fprint
from seed.data_funcs.rngs import (
    sorted_unique_ints_to_iter_nontouch_ranges
    ,make_NonTouchRanges
    ,make_Ranges
    )

#==== www
#(include,include)
closed_rngs__www =\
{(0x4E00, 0x9FA5): (20902, '基本汉字')
,(0x9FA6, 0x9FEF): (74, '基本汉字补充')
,(0x3400, 0x4DB5): (6582, '扩展A')
,(0x20000, 0x2A6D6): (42711, '扩展B')
,(0x2A700, 0x2B734): (4149, '扩展C')
,(0x2B740, 0x2B81D): (222, '扩展D')
,(0x2B820, 0x2CEA1): (5762, '扩展E')
,(0x2CEB0, 0x2EBE0): (7473, '扩展F')
,(0x2F00, 0x2FD5): (214, '康熙部首')
,(0x2E80, 0x2EF3): (115, '部首扩展')
,(0xF900, 0xFAD9): (477, '兼容汉字')
,(0x2F800, 0x2FA1D): (542, '兼容扩展')
,(0xE815, 0xE86F): (81, 'PUA(GBK)部件')
,(0xE400, 0xE5E8): (452, '部件扩展')
,(0xE600, 0xE6CF): (207, 'PUA增补')
,(0x31C0, 0x31E3): (36, '汉字笔画')
,(0x2FF0, 0x2FFB): (12, '汉字结构')
,(0x3105, 0x312F): (43, '汉语注音')
,(0x31A0, 0x31BA): (22, '注音扩展')
,(0x3007, 0x3007): (1, '〇')
}

#===vs unicode 13.0.0 :: charts-East_Asian_Scripts
#(include,include)
closed_rngs__unicode_13_0_0 =\
[(0x20000, 0x2A6DD) #bug:0x2A6CF
,(0x2A700, 0x2B734)
,(0x2B740, 0x2B81D)
,(0x2B820, 0x2CEA1)
,(0x2CEB0, 0x2EBE0)
,(0x2E80, 0x2EFF) #0x2EF3
,(0x2F00, 0x2FDF) #0x2FD5
,(0x2F800, 0x2FA1F) #0x2FA1D
,(0x2FF0, 0x2FFF) #0x2FFB
,(0x30000, 0x3134A)
,(0x3100, 0x312F)
,(0x31A0, 0x31BF)
,(0x31C0, 0x31EF) #0x31E3
,(0x3400, 0x4DBF)
,(0x4E00, 0x9FFC)
,(0xF900, 0xFAFF) #0xFAD9
]

# w|u|m #see below cmp3()
#汉字相关字符范围
union_ranges =\
((0x2E80, 0x2FE0)
,(0x2FF0, 0x3000)
,(0x3007, 0x3008)
,(0x3100, 0x3130)
,(0x31A0, 0x31F0)
,(0x3400, 0x4DC0)
,(0x4E00, 0x9FFD)
,(0xE400, 0xE5E9)
,(0xE600, 0xE6D0)
,(0xE815, 0xE870)
,(0xF900, 0xFB00)
,(0x20000, 0x2A6DE)
,(0x2A700, 0x2B735)
,(0x2B740, 0x2B81E)
,(0x2B820, 0x2CEA2)
,(0x2CEB0, 0x2EBE1)
,(0x2F800, 0x2FA20)
,(0x30000, 0x3134B)
)


def load_汉字到笔顺码():
    from nn_ns.CJK.CJK_data.汉字笔顺 import 汉字到笔顺码
    return 汉字到笔顺码
def mk笔顺码字符范围__rngs():
    汉字到笔顺码 = load_汉字到笔顺码()
    rngs = sorted_unique_ints_to_iter_nontouch_ranges(sorted(map(ord, 汉字到笔顺码)))
    return rngs

def mk笔顺码字符范围__Range():
    rngs = mk笔顺码字符范围__rngs()
    return make_NonTouchRanges(rngs)

def ls笔顺码字符范围__closed_rngs(*, fout):
    rngs = mk笔顺码字符范围__rngs()
    closed_rngs = rngs_to_closed_rngs(rngs)
    show_hex_uint_pairs(closed_rngs, fout=fout)










def show_hex_uint_pairs(uint_pairs, *, fout):
    for a, b in uint_pairs:
        assert a >= 0
        assert b >= 0
        fprint(f",(0x{a:X}, 0x{b:X})", file=fout)
def rngs_to_closed_rngs(rngs):
    for begin, end in rngs:
        assert begin < end
        first = begin
        last = end-1
        assert first <= last
        yield first, last

def closed_rngs_to_rngs(closed_rngs):
    for first, last in closed_rngs:
        assert first <= last
        begin = first
        end = last+1
        assert begin < end
        yield begin, end

def closed_rngs_to_sorted_rngs(closed_rngs):
    return sorted(closed_rngs_to_rngs(closed_rngs))

def closed_rngs_to_Range(closed_rngs):
    return make_Ranges(closed_rngs_to_sorted_rngs(closed_rngs)).to_NonTouchRanges()


def cmp3(*, fout):
    w = rs__w = closed_rngs_to_Range(closed_rngs__www)
    u = rs__u = closed_rngs_to_Range(closed_rngs__unicode_13_0_0)
    m = rs__m = mk笔顺码字符范围__Range()
    d = dict(w=w, u=u, m=m)
    ks = 'wum'
    for k in ks:
        fprint(f"|{k!s}|={d[k].len_ints()}", file=fout)
    fprint("="*9, file=fout)
    for k0 in ks:
        for k1 in ks:
            if k1 != k0:
                diff = d[k1] - d[k0]
                fprint(f"|{k1!s}-{k0!s}|={diff.len_ints()}", file=fout)
    fprint("="*9, file=fout)
    union = w | u | m
    fprint(f"|union|={union.len_ints()}", file=fout)
    fprint(f"|union.ranges|={len(union.ranges)}", file=fout)
    fprint("="*9, file=fout)
    fprint("union.ranges =\\", file=fout)
    show_hex_uint_pairs(union.ranges, fout=fout)
    assert union.ranges == union_ranges
    return union


def prepare_for_汉字粗拆分(*, fout):
    import io
    null = io.StringIO()
    union = cmp3(fout=null)
    汉字到笔顺码 = load_汉字到笔顺码()

    for i in union.iter_ints():
        ch = chr(i)
        fprint(f"{ch!s}u{i:X}h", file=fout)
        ds = 汉字到笔顺码.get(ch, '')
        fprint(f"  ={ds!s}", file=fout)
def prepare_for_2汉字粗拆分2(*, fout):
    #e hz/TODO-汉字拆分设计.txt
    import io
    null = io.StringIO()
    union = cmp3(fout=null)
    汉字到笔顺码 = load_汉字到笔顺码()

    for i in union.iter_ints():
        ch = chr(i)
        head = f"{ch!s}u{i:X}h"
        ds = 汉字到笔顺码.get(ch, '')
        if ds:
            fprint(f"{head!s}<=5:@@{ds!s}", file=fout)
        fprint(f"{head!s}==:", file=fout)
        fprint(f"{head!s}<=4+8:", file=fout)




if 0 and __name__ == '__main__':
    if 0:
        ls笔顺码字符范围__closed_rngs(fout=None)
        #1709 lines
    else:
        cmp3(fout=None)
        r"""
|w|=90128
|u|=94396
|m|=29685
=========
|u-w|=5057
|m-w|=0
|w-u|=789
|m-u|=80
|w-m|=60443
|u-m|=64791
=========
|union|=95185
|union.ranges|=18
=========
union.ranges =\
,(0x2E80, 0x2FE0)
,(0x2FF0, 0x3000)
,(0x3007, 0x3008)
,(0x3100, 0x3130)
,(0x31A0, 0x31F0)
,(0x3400, 0x4DC0)
,(0x4E00, 0x9FFD)
,(0xE400, 0xE5E9)
,(0xE600, 0xE6D0)
,(0xE815, 0xE870)
,(0xF900, 0xFB00)
,(0x20000, 0x2A6DE)
,(0x2A700, 0x2B735)
,(0x2B740, 0x2B81E)
,(0x2B820, 0x2CEA2)
,(0x2CEB0, 0x2EBE1)
,(0x2F800, 0x2FA20)
,(0x30000, 0x3134B)
        #"""

def main(args=None):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout
    choices = [
        ls笔顺码字符范围__closed_rngs
        , cmp3
        , prepare_for_汉字粗拆分
        , prepare_for_2汉字粗拆分2
        ]
    choices = [f.__name__ for f in choices]

    parser = argparse.ArgumentParser(
        description="汉字相关字符范围"
        , epilog=""
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    r"""
    parser.add_argument('-i', '--input', type=str, default=None
                        , help='input file path')
    #"""
    parser.add_argument('-do', '--do'
                        , type=str
                        , required=True#, default=None
                        , choices=choices
                        , help='input file path')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-e', '--encoding', type=str
                        , default='utf8'
                        , help='input/output file encoding')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')

    args = parser.parse_args(args)
    encoding = args.encoding
    omode = 'wt' if args.force else 'xt'
    do = args.do
    f = globals()[do]

    r"""
    may_ifname = args.input
    with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:
    #"""

    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
        f(fout=fout)
if __name__ == "__main__":
    main()


