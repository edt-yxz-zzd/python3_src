
r"""
e ../../python3_src/nn_ns/CJK/CJK_data/raw/汉字笔顺表\[20200913]/stroke-seq_MB-master\[汉字笔顺表]\[20200827]/my_patch.py
py '/storage/emulated/0/0my_files/git_repos/python3_src/nn_ns/CJK/CJK_data/raw/汉字笔顺表[20200913]/stroke-seq_MB-master[汉字笔顺表][20200827]/my_patch.py'
cd '/storage/emulated/0/0my_files/git_repos/python3_src/nn_ns/CJK/CJK_data/raw/汉字笔顺表[20200913]/stroke-seq_MB-master[汉字笔顺表][20200827]/'
py my_patch.py > my_patch.py.out.txt
view /storage/emulated/0/0my_files/git_repos/python3_src/nn_ns/CJK/CJK_data/raw/汉字笔顺表\[20200913]/stroke-seq_MB-master\[汉字笔顺表]\[20200827]/my_patch.py.out.txt



单字_笔顺码_29685个.txt use unicode PUA!!!
gb18030 has move some PUA char out PUA

data from
    ../../python3_src/nn_ns/CJK/CJK_data/raw/Unicode私人使用区PUA.txt
        https://baike.baidu.com/item/GB18030/3204518
            gb18030
#"""


sz_gb18030_old_PUA_char_to_normal_char = 105
gb18030_old_PUA_char_to_normal_char = r"""
A6D9		E78D ()	FE10 (︐)
A6DA		E78E ()	FE12 (︒)
A6DB		E78F ()	FE11 (︑)
A6DC		E790 ()	FE13 (︓)
A6DD		E791 ()	FE14 (︔)
A6DE		E792 ()	FE15 (︕)
A6DF		E793 ()	FE16 (︖)
A6EC		E794 ()	FE17 (︗)
A6ED		E795 ()	FE18 (︘)
A6F3		E796 ()	FE19 (︙)
A8BC	E7C7 ()	1E3F (ḿ)	1E3F (ḿ)
A8BF	E7C8 ()	01F9 (ǹ)	01F9 (ǹ)
A989	E7E7 ()	303E (〾)	303E (〾)
A98A	E7E8 ()	2FF0 (⿰)	2FF0 (⿰)
A98B	E7E9 ()	2FF1 (⿱)	2FF1 (⿱)
A98C	E7EA ()	2FF2 (⿲)	2FF2 (⿲)
A98D	E7EB ()	2FF3 (⿳)	2FF3 (⿳)
A98E	E7EC ()	2FF4 (⿴)	2FF4 (⿴)
A98F	E7ED ()	2FF5 (⿵)	2FF5 (⿵)
A990	E7EE ()	2FF6 (⿶)	2FF6 (⿶)
A991	E7EF ()	2FF7 (⿷)	2FF7 (⿷)
A992	E7F0 ()	2FF8 (⿸)	2FF8 (⿸)
A993	E7F1 ()	2FF9 (⿹)	2FF9 (⿹)
A994	E7F2 ()	2FFA (⿺)	2FFA (⿺)
A995	E7F3 ()	2FFB (⿻)	2FFB (⿻)
FE50	E815 ()	2E81 (⺁)	2E81 (⺁)
FE51	E816 ()	E816 ()	20087 (𠂇)
FE52	E817 ()	E817 ()	20089 (𠂉)
FE53	E818 ()	E818 ()	200CC (𠃌)
FE54	E819 ()	2E84 (⺄)	2E84 (⺄)
FE55	E81A ()	3473 (㑳)	3473 (㑳)
FE56	E81B ()	3447 (㑇)	3447 (㑇)
FE57	E81C ()	2E88 (⺈)	2E88 (⺈)
FE58	E81D ()	2E8B (⺋)	2E8B (⺋)
FE59	E81E ()	E81E ()	9FB4 (龴)
FE5A	E81F ()	359E (㖞)	359E (㖞)
FE5B	E820 ()	361A (㘚)	361A (㘚)
FE5C	E821 ()	360E (㘎)	360E (㘎)
FE5D	E822 ()	2E8C (⺌)	2E8C (⺌)
FE5E	E823 ()	2E97 (⺗)	2E97 (⺗)
FE5F	E824 ()	396E (㥮)	396E (㥮)
FE60	E825 ()	3918 (㤘)	3918 (㤘)
FE61	E826 ()	E826 ()	9FB5 (龵)
FE62	E827 ()	39CF (㧏)	39CF (㧏)
FE63	E828 ()	39DF (㧟)	39DF (㧟)
FE64	E829 ()	3A73 (㩳)	3A73 (㩳)
FE65	E82A ()	39D0 (㧐)	39D0 (㧐)
FE66	E82B ()	E82B ()	9FB6 (龶)
FE67	E82C ()	E82C ()	9FB7 (龷)
FE68	E82D ()	3B4E (㭎)	3B4E (㭎)
FE69	E82E ()	3C6E (㱮)	3C6E (㱮)
FE6A	E82F ()	3CE0 (㳠)	3CE0 (㳠)
FE6B	E830 ()	2EA7 (⺧)	2EA7 (⺧)
FE6C	E831 ()	E831 ()	215D7 (𡗗)
FE6D	E832 ()	E832 ()	9FB8 (龸)
FE6E	E833 ()	2EAA (⺪)	2EAA (⺪)
FE6F	E834 ()	4056 (䁖)	4056 (䁖)
FE70	E835 ()	415F (䅟)	415F (䅟)
FE71	E836 ()	2EAE (⺮)	2EAE (⺮)
FE72	E837 ()	4337 (䌷)	4337 (䌷)
FE73	E838 ()	2EB3 (⺳)	2EB3 (⺳)
FE74	E839 ()	2EB6 (⺶)	2EB6 (⺶)
FE75	E83A ()	2EB7 (⺷)	2EB7 (⺷)
FE76	E83B ()	E83B ()	2298F (𢦏)
FE77	E83C ()	43B1 (䎱)	43B1 (䎱)
FE78	E83D ()	43AC (䎬)	43AC (䎬)
FE79	E83E ()	2EBB (⺻)	2EBB (⺻)
FE7A	E83F ()	43DD (䏝)	43DD (䏝)
FE7B	E840 ()	44D6 (䓖)	44D6 (䓖)
FE7C	E841 ()	4661 (䙡)	4661 (䙡)
FE7D	E842 ()	464C (䙌)	464C (䙌)
FE7E	E843 ()	E843 ()	9FB9 (龹)
FE80	E844 ()	4723 (䜣)	4723 (䜣)
FE81	E845 ()	4729 (䜩)	4729 (䜩)
FE82	E846 ()	477C (䝼)	477C (䝼)
FE83	E847 ()	478D (䞍)	478D (䞍)
FE84	E848 ()	2ECA (⻊)	2ECA (⻊)
FE85	E849 ()	4947 (䥇)	4947 (䥇)
FE86	E84A ()	497A (䥺)	497A (䥺)
FE87	E84B ()	497D (䥽)	497D (䥽)
FE88	E84C ()	4982 (䦂)	4982 (䦂)
FE89	E84D ()	4983 (䦃)	4983 (䦃)
FE8A	E84E ()	4985 (䦅)	4985 (䦅)
FE8B	E84F ()	4986 (䦆)	4986 (䦆)
FE8C	E850 ()	499F (䦟)	499F (䦟)
FE8D	E851 ()	499B (䦛)	499B (䦛)
FE8E	E852 ()	49B7 (䦷)	49B7 (䦷)
FE8F	E853 ()	49B6 (䦶)	49B6 (䦶)
FE90	E854 ()	E854 ()	9FBA (龺)
FE91	E855 ()	E855 ()	241FE (𤇾)
FE92	E856 ()	4CA3 (䲣)	4CA3 (䲣)
FE93	E857 ()	4C9F (䲟)	4C9F (䲟)
FE94	E858 ()	4CA0 (䲠)	4CA0 (䲠)
FE95	E859 ()	4CA1 (䲡)	4CA1 (䲡)
FE96	E85A ()	4C77 (䱷)	4C77 (䱷)
FE97	E85B ()	4CA2 (䲢)	4CA2 (䲢)
FE98	E85C ()	4D13 (䴓)	4D13 (䴓)
FE99	E85D ()	4D14 (䴔)	4D14 (䴔)
FE9A	E85E ()	4D15 (䴕)	4D15 (䴕)
FE9B	E85F ()	4D16 (䴖)	4D16 (䴖)
FE9C	E860 ()	4D17 (䴗)	4D17 (䴗)
FE9D	E861 ()	4D18 (䴘)	4D18 (䴘)
FE9E	E862 ()	4D19 (䴙)	4D19 (䴙)
FE9F	E863 ()	4DAE (䶮)	4DAE (䶮)
FEA0	E864 ()	E864 ()	9FBB (龻)
#""" #gb18030_old_PUA_char_to_normal_char


from seed.tiny import fprint
import re

def uint_to_bytes(u):
    assert u >= 0
    s = f"{u:X}"
    L = (len(s)+1)//2
    assert 2*L-1 <= len(s) <= 2*L
    bs = u.to_bytes(L, byteorder='big')
    assert bs[0] or not u
    assert u == int.from_bytes(bs, byteorder='big')
    return bs

def parse_gb18030_old_PUA_char_to_normal_char(
    raw = gb18030_old_PUA_char_to_normal_char
    ,sz = sz_gb18030_old_PUA_char_to_normal_char
    ):
    lines = [line for line in raw.split("\n") if len(line)> 4]
    assert len(lines) == sz

    rex = re.compile(r"[0-9A-F]+")
    d = {}
    for line in lines:
        codes = [m.group(0) for m in rex.finditer(line)]
        L = len(codes)
        assert 3 <= L <= 4
        codes = [int(s, base=16) for s in codes]
        us = [codes[i] for i in [0,1,-1]]
        assert len(us) == 3 == len(set(us))
        assert codes[2] in us[1:]
        gb, pua, uni = us
        if __debug__:
            try:
                gb_ch = uint_to_bytes(gb).decode('gb18030')
                pua_ch = chr(pua)
                std_ch = chr(uni)
                assert gb_ch in [pua_ch, std_ch]
            except:
                print(line)
                print(f"gb={char2str(gb_ch)}; pua={char2str(pua_ch)}; std={char2str(std_ch)}")
                raise
        #yield gb, pua, uni
        d[chr(pua)] = chr(uni), gb
    assert len(d) == sz
    pua_char2std_char_and_gb_code_pair = d
    return pua_char2std_char_and_gb_code_pair

def char2str(c):
    return f"{c!s}u{ord(c):X}h"
def show_pua2std_gb_pair(
    pua_char2std_char_and_gb_code_pair
    ,*
    ,fout
    ):
    d = pua_char2std_char_and_gb_code_pair
    for pua, (std, gb) in sorted(d.items()):
        fprint(f"{char2str(pua)} {char2str(std)} g{gb:X}h", file=fout)


def _t(*, fout):
    d = parse_gb18030_old_PUA_char_to_normal_char()
    show_pua2std_gb_pair(d, fout=fout)

if 1:
    _t(fout=None)




