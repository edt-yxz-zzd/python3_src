
r"""

py -m nn_ns.CJK.CJK_data.raw.汉字繁简
py -m nn_ns.CJK.CJK_data.汉字繁简
e ../../python3_src/nn_ns/CJK/CJK_data/raw/汉字繁简.py
view ../../python3_src/nn_ns/CJK/CJK_data/output/parse_繁简.py.out/简繁.txt


[[[
bug:数据有误
===

bug:
'bug:包含:  ․˙‥¨′＇═〓「“」”『‘』’〞″䊷䌶'
bug:包含:\u25A1
    'name': 'WHITE SQUARE'
    9633 == 0x25A1

grep $'\u25A1' -r '../../python3_src/nn_ns/CJK/CJK_data/raw/繁简转换[20200913]/' -l
../../python3_src/nn_ns/CJK/CJK_data/raw/繁简转换[20200913]/funNLP-master/fanjian_suoyin.txt
    只有一个文件

view ../../python3_src/nn_ns/CJK/CJK_data/raw/繁简转换[20200913]/funNLP-master/fanjian_suoyin.txt
搜索:
/\%u25a1

xxx并非gbk view ++enc=gbk ../../python3_src/nn_ns/CJK/CJK_data/raw/繁简转换[20200913]/funNLP-master/fanjian_suoyin.txt
]]]

[[[
宁
===
㝉宁寧
苎苧薴
伫佇儜
𪾣眝矃
纻紵𦆭
===
简繁字对囗补丁囗㝉宁相关:
㝉宁
宁寧
伫佇
佇儜
𪾣眝
眝矃
苎苧
苧薴
纻紵
紵𦆭

===
繁：「寧（níng）」、「宁（zhù）」；「薴（níng）烯」、「苧（zhù）麻」
简：「宁（níng）」、「㝉（zhù）」；「苧（níng）烯」、「苎（zhù）麻」
繁：「檸（níng）」、「濘（nìng）」；「柠（chǔ）」、「泞（zhù）」
简：「柠（níng）」、「泞（nìng）」；「？【⿰木㝉】（chǔ）」、「？【⿰氵㝉】（zhù）」
===
view /storage/emulated/0/0my_files/git_repos/txt_phone/lots/NOTE/汉字/说「㝉（宁）」字.txt
cp -t ../../python3_src/nn_ns/CJK/CJK_data/raw/繁简转换/ /storage/emulated/0/0my_files/git_repos/txt_phone/lots/NOTE/汉字/说「㝉（宁）」字.txt
view ../../python3_src/nn_ns/CJK/CJK_data/raw/繁简转换/说「㝉（宁）」字.txt
view  ../../python3_src/nn_ns/CJK/CJK_data/raw/汉字繁简.py
view ../../python3_src/nn_ns/CJK/CJK_data/output/parse_繁简.py.out/简繁.txt
===
view ../../python3_src/nn_ns/CJK/CJK_data/raw/汉字笔顺表[20200913]/stroke-seq_MB-master[汉字笔顺表][20200827]/单字_笔顺码_29685个.txt
view ../../python3_src/nn_ns/CJK/CJK_struct/cjk_decomp_0_4_0/cjk-decomp-0.4.0.txt
grep 㝉 ../../python3_src/nn_ns/CJK/CJK_struct/cjk_decomp_0_4_0/cjk-decomp-0.4.0.txt
[[
41518:d(㝉,八,目)
41581:d(㝉,由,灬)
41930:d(㝉,皿,丁)
42602:d(㝉,𧖧)
44506:d(㝉,53203)
48664:d(㝉,𧴪)
54233:d(㝉,谷)
㝉:d(宀,㇐)
㝟:d(㝉,見)
伫:a(亻,㝉)
纻:a(纟,㝉)
苎:d(卄,㝉)
贮:a(贝,㝉)
𡧂:d(㝉,勹)
𡧆:d(㝉,八)
𡧘:d(㝉,99750)
𡧤:d(㝉,勿)
𡧴:d(㝉,匆)
𡩂:d(㝉,血,八)
𡩅:d(㝉,26827,21895)
𡩟:d(㝉,臾)
𡩪:d(㝉,21715)
𥩟:a(立,㝉)
𪧅:d(㝉,山)
𪾣:a(目,㝉)
𫎓:a(貝,㝉)
]]
==>> [亻纟卄贝目立]
==>> [亻纟卄贝目立糹貝]

贮:a(贝,㝉)
𥩟:a(立,㝉)
𫎓:a(貝,㝉)
-
竚:a(立,宁)
貯:a(貝,宁)
=>:
贮貯
贮𫎓
𥩟竚

grep 宁 ../../python3_src/nn_ns/CJK/CJK_struct/cjk_decomp_0_4_0/cjk-decomp-0.4.0.txt
[[
17108:stl(⺹,宁)
60353:d(61994,宁)
㤖:a(忄,宁)
㿾:d(宁,皿)
䇡:d(⺮,宁)
䍆:a(缶,宁)
䘢:a(衤,宁)
佇:a(亻,宁)
咛:a(口,宁)
坾:a(土,宁)
宁:d(宀,丁)
拧:a(扌,宁)
柠:a(木,宁)
泞:a(氵,宁)
狞:a(犭,宁)
眝:a(目,宁)
竚:a(立,宁)
紵:a(糹,宁)
羜:a(⺶,宁)
聍:a(耳,宁)
苧:d(卄,宁)
詝:a(言,宁)
貯:a(貝,宁)
𡧲:a(宁,中)
𡨸:a(宁,字)
𡨹:a(守,宁)
𡨺:a(宁,守)
𡪄:a(宁,者)
𡪇:a(宁,修)
𢁼:a(巾,宁)
𤆼:a(火,宁)
𤕞:a(爻,宁)
𤱤:a(甲,宁)
𤲑:a(甾,宁)
𤴍:a(25747,宁)
𥹍:a(米,宁)
𧉞:a(虫,宁)
𧵒:d(宁,貝)
𨀉:a(足,宁)
𩶂:a(魚,宁)
𪥰:a(女,宁)
𫛢:a(宁,鸟)
]]

grep 寧 ../../python3_src/nn_ns/CJK/CJK_struct/cjk_decomp_0_4_0/cjk-decomp-0.4.0.txt
[[
㣷:a(彳,寧)
㲰:a(寧,毛)
䗿:a(虫,寧)
䭢:a(食,寧)
儜:a(亻,寧)
嚀:a(口,寧)
嬣:a(女,寧)
寧:d(寍,丁)
懧:a(忄,寧)
擰:a(扌,寧)
檸:a(木,寧)
濘:a(氵,寧)
獰:a(犭,寧)
矃:a(目,寧)
聹:a(耳,寧)
薴:d(卄,寧)
鑏:a(金,寧)
鬡:d(髟,寧)
鸋:a(寧,鳥)
𡫸:a(寧,吉)
𡬗:a(寧,26350)
𤘓:a(牙,寧)
𤪥:a(王,寧)
𤻝:stl(疒,寧)
𤾱:a(白,寧)
𥣗:a(禾,寧)
𦆭:a(糹,寧)
𦡲:a(月,寧)
𧭈:a(言,寧)
𧰗:a(豆,寧)
𨊓:a(身,寧)
𨲸:a(镸,寧)
𩁔:a(寧,隹)
𩕳:a(寧,頁)
𫍾:a(讠,寧)
]]
==>> [彳虫食亻口女忄扌木氵犭目耳卄金髟牙王白禾糹月言豆身镸讠疒毛鳥吉隹頁]
==>> [彳虫食亻口女忄扌木氵犭目耳卄金髟牙王白禾糹月言豆身镸讠疒毛鳥吉隹頁纟鸟页]
佇:a(亻,宁)
眝:a(目,宁)
苧:d(卄,宁)
紵:a(糹,宁)
-
㤖:a(忄,宁)
咛:a(口,宁)
拧:a(扌,宁)
泞:a(氵,宁)
狞:a(犭,宁)
聍:a(耳,宁)
𧉞:a(虫,宁)
𪥰:a(女,宁)
柠:a(木,宁)
𫛢:a(宁,鸟)
詝:a(言,宁)
-
==>> [虫口女忄扌木氵犭耳言讠鳥鸟]
懧:a(忄,寧)
嚀:a(口,寧)
擰:a(扌,寧)
濘:a(氵,寧)
獰:a(犭,寧)
聹:a(耳,寧)
䗿:a(虫,寧)
嬣:a(女,寧)
檸:a(木,寧)
鸋:a(寧,鳥)
𧭈:a(言,寧)
𫍾:a(讠,寧)
=>:
㤖懧
咛嚀
拧擰
泞濘
狞獰
聍聹
𧉞䗿
𪥰嬣
柠檸
𫛢鸋
詝𧭈
𫍾𧭈


[亻纟卄贝目立糹貝] ==>>:
儜:a(亻,寧)
矃:a(目,寧)
薴:d(卄,寧)
𦆭:a(糹,寧)
-
佇:a(亻,宁)
眝:a(目,宁)
苧:d(卄,宁)
紵:a(糹,宁)
-
伫:a(亻,㝉)
𪾣:a(目,㝉)
苎:d(卄,㝉)
纻:a(纟,㝉)


]]]



#"""



__all__ = '''
    简繁字对集
        繁体字到简体字串
        简体字到繁体字串
    '''.split()






##section##
r"""
import io
import re
from seed.tiny import print_err
#"""

from nn_ns.CJK.CJK_common.is_hz import is_hz__tribool_, partition_charset_by_is_hz_
from seed.io.iter_row_based_Z_delimited_text_file import iter_TSV__path
from types import MappingProxyType #frozenset




##section##
class Globals:
    import nn_ns.CJK.CJK_data.raw as raw
    from pathlib import Path
    [raw_path] = raw.__path__
    简繁_TSV_path = Path(raw_path) / r"../output/parse_繁简.py.out/简繁.txt"
    r"""
    #"""

def _read(简繁_TSV_path):
    return set(_iter_read(简繁_TSV_path))
def _iter_read(简繁_TSV_path):
    it = iter_TSV__path(简繁_TSV_path, encoding='utf8')
    for _, parts in it:
        [简繁] = parts
        [简, 繁] = 简繁
        yield 简繁

def _mk_繁体字到简体字串(简繁字对集):
    it = ((繁, 简) for 简, 繁 in 简繁字对集)
    return _mk_x2ys(it)
def _mk_简体字到繁体字串(简繁字对集):
    it = ((简, 繁) for 简, 繁 in 简繁字对集)
    return _mk_x2ys(it)
def _mk_x2ys(xy_iter):
    x2ys = {}
    for x, y in xy_iter:
        ys = x2ys.setdefault(x, [])
        ys.append(y)
    x2ys = {x:"".join(sorted(ys)) for x, ys in x2ys.items()}
    return x2ys

#简繁字对集 = frozenset(_read(Globals.简繁_TSV_path))
#   'bug:包含:  ․˙‥¨′＇═〓「“」”『‘』’〞″䊷䌶'
_简繁字对集 = frozenset(_read(Globals.简繁_TSV_path))

简繁字对集 = frozenset(TS for TS in _简繁字对集 if all(is_hz__tribool_(ch) is True for ch in TS))
_unknown_pairs = frozenset(TS for TS in _简繁字对集 if not all(type(is_hz__tribool_(ch)) is bool for ch in TS))
_nonhz_pairs = _简繁字对集 -简繁字对集 -_unknown_pairs
if 0b0:
    print(_unknown_pairs)
    print(_nonhz_pairs)
    print(len(_unknown_pairs))
    print(len(_nonhz_pairs))
assert len(_unknown_pairs) == 1
assert len(_nonhz_pairs) == 2912
assert _unknown_pairs == frozenset({'□\ue5f1'})
assert frozenset({'□鴹', '□騹', '□餹', '□鐹', '□錹', '□輹', '□鵸', '□齸'}) < _nonhz_pairs
_nonhz_pairs_1 = {ab for ab in _nonhz_pairs if ab[0]=='\u25A1'}
_nonhz_pairs_2 = {ab for ab in _nonhz_pairs if not ab[0]=='\u25A1'}
if 0b0:
    print(_nonhz_pairs_1)
    print(_nonhz_pairs_2)
    print(len(_nonhz_pairs_1))
    print(len(_nonhz_pairs_2))

assert len(_nonhz_pairs_1) == 2893
assert len(_nonhz_pairs_2) == 19
assert _nonhz_pairs_2 == {'眺※', '”」', '．•', '″〞', '’』', '鹮□', '翻※', '刾□', '鳚□', '菱※', '＇′', '鲃□', '“「', '〓═', '¨‥', '‘『', '．‧', '˙․', '鳤□'}
assert _nonhz_pairs_2 > {'”」', '．•', '″〞', '’』', '＇′', '“「', '〓═', '¨‥', '‘『', '．‧', '˙․'}
assert not '․˙‥¨′＇═〓「“」”『‘』’〞″' == ''.join(sorted(ab[::-1] for ab in {'”」', '．•', '″〞', '’』', '＇′', '“「', '〓═', '¨‥', '‘『', '．‧', '˙․'}))
assert  '•．․˙‥¨‧．′＇═〓「“」”『‘』’〞″' == ''.join(sorted(ab[::-1] for ab in {'”」', '．•', '″〞', '’』', '＇′', '“「', '〓═', '¨‥', '‘『', '．‧', '˙․'}))



简繁字对囗补丁囗㝉宁相关 = r'''
㝉宁
宁寧
伫佇
佇儜
𪾣眝
眝矃
苎苧
苧薴
纻紵
紵𦆭

贮貯
贮𫎓
𥩟竚

㤖懧
咛嚀
拧擰
泞濘
狞獰
聍聹
𧉞䗿
𪥰嬣
柠檸
𫛢鸋
詝𧭈
𫍾𧭈
'''.split()#'''
简繁字对集 |= frozenset(简繁字对囗补丁囗㝉宁相关)

繁体字到简体字串 = MappingProxyType(_mk_繁体字到简体字串(简繁字对集))
简体字到繁体字串 = MappingProxyType(_mk_简体字到繁体字串(简繁字对集))







