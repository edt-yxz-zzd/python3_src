
r"""
unicode_cjk_部件_笔画.py
e /storage/emulated/0/0my_files/git_repos/python3_src/nn_ns/CJK/CJK_data/raw/unicode_cjk_部件_笔画.py
py -m nn_ns.CJK.CJK_data.raw.unicode_cjk_部件_笔画

unicode cjk 部件 笔画
http://www.unicode.org/charts/fonts.html


CJK Radicals Supplement
Range: 2E80–2EFF
[2E80, 2E9A)
[2E9B, 2EF4)
(16+10) + (5+16*5+4) = 26+89 = 115 = 16*8-1-(16-4) = 128-13

Kangxi Radicals
Range: 2F00–2FDF
[2F00, 2FD6)
16*13+6 = 225-15-2+6=214
因皆有相应的汉字，故不予理会

Ideographic Description Characters
Range: 2FF0–2FFF
[2FF0, 2FFC)
12

CJK Strokes
Range: 31C0–31EF
[31C0, 31E4)
16*2+4 = 36

Halfwidth and Fullwidth Forms
Range: U+FF00–U+FFEF


unicode 13.0
18 East Asia 18.1 Han
    Blocks Containing Han Ideographs
    Han ideographic characters are found in several blocks of the Unicode Standard, as shown in Table 18-1.
    Table 18-1. Blocks Containing Han Ideographs
    Block Range Comment
    CJK Unified Ideographs 4E00–9FFF Common
    CJK Unified Ideographs Extension A3400–4DBF Rare
    CJK Unified Ideographs Extension B20000–2A6DF Rare, historic
    CJK Unified Ideographs Extension C2A700–2B73F Rare, historic
    CJK Unified Ideographs Extension D2B740–2B81F Uncommon, some in current use
    CJK Unified Ideographs Extension E2B820–2CEAF Rare, historic
    CJK Unified Ideographs Extension F2CEB0–2EBEF Rare, historic
    CJK Unified Ideographs Extension G30000–3134F Rare, historic
    CJK Compatibility Ideographs F900–FAFF Duplicates, unifiable variants, corporate characters
    CJK Compatibility Ideographs Supplement 2F800–2FA1F Unifiable variants

    Table 18-2. Small Extensions to CJK Blocks
    Range Version Comment
    9FA6–9FB3 4.1 Interoperability with HKSCS standard
    9FB4–9FBB 4.1 Interoperability with GB 18030 standard
    9FBC–9FC2 5.1 Interoperability with commercial implementations
    9FC3 5.1 Correction of mistaken unification
    9FC4–9FC6 5.2 Interoperability with ARIB standard
    9FC7–9FCB 5.2 Interoperability with HKSCS standard
    9FCC 6.1 Interoperability with commercial implementations
    9FCD–9FCF 8.0 Interoperability with TGH 2013 standard
    9FD0 8.0 Correction of mistaken unification
    9FD1–9FD5 8.0 Miscellaneous urgently needed characters
    9FD6–9FE9 10.0 Ideographs for Slavonic transcription
    9FEA 10.0 Correction of mistaken unification
    9FEB–9FED 11.0 Ideographs for chemical elements
    9FEE–9FEF 11.0 Interoperability with government implementations
    9FF0–9FFC 13.0 Zoological, chemical, and geological terms
    4DB6-4DBF 13.0 Corrections of mistaken unifications
    2A6D7-2A6DD 13.0 Gongche characters for Kunqu Opera


Symbols Derived from Han Ideographs
A number of symbols derived from Han ideographs can be found in other blocks.
    See
        “Enclosed CJK Letters and Months: U+3200–U+32FF,”
        “CJK Compatibility: U+3300–U+33FF,”
        and “Enclosed Ideographic Supplement: U+1F200–U+1F2FF”
    in Section 22.10, Enclosed and Square.

Ideographic Symbols and Punctuation: U+16FE0–U+16FFF
The Ideographic Symbols and Punctuation block covers historic and less common symbols and punctuation associated with various ideographic scripts. Included, for example, are iteration marks for Tangut, Nüshu, and old Chinese, as well as reading marks associated with Vietnamese use of Han characters.


全角字符
    CJK Symbols and Punctuation
    [3000, 3040)
        [3000, 3020)
        32
    Halfwidth and Fullwidth Forms
    [FF00,FFF0)
        [FF01,FF5F)
        16*6-2=94


#"""


__all__ = """
    CJK_Radicals_Supplement
    Kangxi_Radicals
    Ideographic_Description_Characters
    CJK_Strokes
    """.split()

##section##
#import io
#import re
#from seed.tiny import print_err
##section##
class Globals:
    import nn_ns.CJK.CJK_data.raw as raw
    from pathlib import Path
    [raw_path] = raw.__path__
    根笔_path = Path(raw_path) / r"../output/unicode_cjk_部件_笔画.py.out/unicode_cjk_部件_笔画.txt"
    ####
    kw = dict(
        CJK_Radicals_Supplement
        = (115, [(0x2E80, 0x2E9A), (0x2E9B, 0x2EF4)])
        ,Kangxi_Radicals
        = (214, [(0x2F00, 0x2FD6)])
        ,Ideographic_Description_Characters
        = (12, [(0x2FF0, 0x2FFC)])
        ,CJK_Strokes
        = (36, [(0x31C0, 0x31E4)])
        )
    assert set(kw) == set(__all__)


def _show(d, *, fout):
    for k in sorted(d):
        print(f"##data##\n{k!s} = {d[k]!r}\n#{k!s}\n", file=fout)
def _mk_name2chars(**kw):
    d = {}
    for name, (sz, rngs) in kw.items():
        pre_j = -1
        ls = []
        for i, j in rngs:
            assert pre_j < i
            pre_j = j
            chars = ''.join(map(chr, range(i,j)))
            ls.append(chars)
        chars = ''.join(ls)
        d[name] = chars
        if not len(chars) == sz: raise ValueError((name, (sz, rngs)))
    return d

def _main():
    from pprint import pprint
    d = _mk_name2chars(**Globals.kw)
    #pprint(d)
    with open(Globals.根笔_path, "xt", encoding="utf8") as fout:
        _show(d, fout=fout)


if __name__ == "__main__":
    _main()







##################################
##################################
##################################
##################################
##################################
##################################
##################################
##################################

##data##
CJK_Radicals_Supplement = '⺀⺁⺂⺃⺄⺅⺆⺇⺈⺉⺊⺋⺌⺍⺎⺏⺐⺑⺒⺓⺔⺕⺖⺗⺘⺙⺛⺜⺝⺞⺟⺠⺡⺢⺣⺤⺥⺦⺧⺨⺩⺪⺫⺬⺭⺮⺯⺰⺱⺲⺳⺴⺵⺶⺷⺸⺹⺺⺻⺼⺽⺾⺿⻀⻁⻂⻃⻄⻅⻆⻇⻈⻉⻊⻋⻌⻍⻎⻏⻐⻑⻒⻓⻔⻕⻖⻗⻘⻙⻚⻛⻜⻝⻞⻟⻠⻡⻢⻣⻤⻥⻦⻧⻨⻩⻪⻫⻬⻭⻮⻯⻰⻱⻲⻳'
#CJK_Radicals_Supplement

##data##
CJK_Strokes = '㇀㇁㇂㇃㇄㇅㇆㇇㇈㇉㇊㇋㇌㇍㇎㇏㇐㇑㇒㇓㇔㇕㇖㇗㇘㇙㇚㇛㇜㇝㇞㇟㇠㇡㇢㇣'
#CJK_Strokes

##data##
Ideographic_Description_Characters = '⿰⿱⿲⿳⿴⿵⿶⿷⿸⿹⿺⿻'
#Ideographic_Description_Characters

##data##
Kangxi_Radicals = '⼀⼁⼂⼃⼄⼅⼆⼇⼈⼉⼊⼋⼌⼍⼎⼏⼐⼑⼒⼓⼔⼕⼖⼗⼘⼙⼚⼛⼜⼝⼞⼟⼠⼡⼢⼣⼤⼥⼦⼧⼨⼩⼪⼫⼬⼭⼮⼯⼰⼱⼲⼳⼴⼵⼶⼷⼸⼹⼺⼻⼼⼽⼾⼿⽀⽁⽂⽃⽄⽅⽆⽇⽈⽉⽊⽋⽌⽍⽎⽏⽐⽑⽒⽓⽔⽕⽖⽗⽘⽙⽚⽛⽜⽝⽞⽟⽠⽡⽢⽣⽤⽥⽦⽧⽨⽩⽪⽫⽬⽭⽮⽯⽰⽱⽲⽳⽴⽵⽶⽷⽸⽹⽺⽻⽼⽽⽾⽿⾀⾁⾂⾃⾄⾅⾆⾇⾈⾉⾊⾋⾌⾍⾎⾏⾐⾑⾒⾓⾔⾕⾖⾗⾘⾙⾚⾛⾜⾝⾞⾟⾠⾡⾢⾣⾤⾥⾦⾧⾨⾩⾪⾫⾬⾭⾮⾯⾰⾱⾲⾳⾴⾵⾶⾷⾸⾹⾺⾻⾼⾽⾾⾿⿀⿁⿂⿃⿄⿅⿆⿇⿈⿉⿊⿋⿌⿍⿎⿏⿐⿑⿒⿓⿔⿕'
#Kangxi_Radicals


