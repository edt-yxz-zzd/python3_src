#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/CJK/CJK_data/raw/unicode_cjk_笔画数讠部首串.py
view ../../python3_src/nn_ns/CJK/CJK_data/raw/unicode_cjk_部件乊汉字区.py

nn_ns.CJK.CJK_data.raw.unicode_cjk_笔画数讠部首串
py -m nn_ns.app.debug_cmd   nn_ns.CJK.CJK_data.raw.unicode_cjk_笔画数讠部首串 -x # -off_defs
py -m nn_ns.app.doctest_cmd nn_ns.CJK.CJK_data.raw.unicode_cjk_笔画数讠部首串:__doc__ -ht # -ff -df

[[
copy from:
    view others/数学/编程/设计/自定义编码纟自然数冃中文序数.txt
]]

]]]'''#'''
__all__ = r'''
笔画数讠部首串
    部首讠笔画数

文本冃笔画数讠部首串
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from types import MappingProxyType as MapView
___end_mark_of_excluded_global_names__0___ = ...



文本冃笔画数讠部首串 = ('''\
01:06:一丨丶丿乙亅
02:25:二亠人儿入八冂冖冫几凵刀力勹匕匚匸十卜卩厂厶又廴讠
03:35:口囗土士夂夊夕大女子宀寸小尢尸屮山巛工己巾干幺广廾弋弓彐彡彳纟门飞饣马
04:42:心戈戶手支攴文斗斤方无日曰月木欠止歹殳毋比毛氏气水火爪父爻爿片牙牛犬瓦禸见贝车长韦风
05:24:玄玉瓜甘生用田疋疒癶白皮皿目矛矢石示禾穴立钅鸟龙
06:31:竹米糸缶网羊羽老而耒耳聿肉臣自至臼舌舛舟艮色艸虍虫血行衣襾页齐
07:21:見角言谷豆豕豸貝赤走足身車辛辰辵邑酉釆里龟
08:11:金長門阜隶隹雨靑非鱼齿
09:13:面革韋韭音頁風飛食首香骨鬼
10:06:馬高髟鬥鬯鬲
11:06:魚鳥鹵鹿麥麻
12:06:黃黍黑黹黽鼎
13:02:鼓鼠
14:02:鼻齊
15:01:齒
16:02:龍龜
17:01:龠
'''#'''
)
文本冃笔画数讠部首串


def __():
    yield '' # @[笔画数==0]
    for s in 文本冃笔画数讠部首串.split():
        _, _, 部首串 = s.split(':')
        yield 部首串

笔画数讠部首串 = tuple(__())
assert len(笔画数讠部首串) == 18
assert 笔画数讠部首串[0] == ''
assert 笔画数讠部首串[1] == '一丨丶丿乙亅'
assert 笔画数讠部首串[17] == '龠'
assert all(sorted(部首串) == list(部首串) for 部首串 in 笔画数讠部首串)


部首讠笔画数 = MapView({部首:笔画数 for 笔画数, 部首串 in enumerate(笔画数讠部首串) for 部首 in 部首串})

__all__
from nn_ns.CJK.CJK_data.raw.unicode_cjk_笔画数讠部首串 import 部首讠笔画数, 笔画数讠部首串 #文本冃笔画数讠部首串
from nn_ns.CJK.CJK_data.raw.unicode_cjk_笔画数讠部首串 import *
