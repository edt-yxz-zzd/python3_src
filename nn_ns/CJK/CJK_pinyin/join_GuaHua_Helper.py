
__all__ = '''
    join_GuaHua_Helper
    '''.split()
from .GuaMing2GuaHua import (
    GuaMing2GuaHua, JingGuaMings_str, GuaMing2idx, idx2GuaMing)
from pathlib import PurePath as Path
this_file = Path(__file__)
this_folder = this_file.parent
this_file_name = this_file.name

class Global:
    ifname = 'final_sm2ym2num2good_hanzi_str[refined_by_hand].txt'
    iencoding = 'gbk'
    ipath = this_folder / ifname
    with open(ipath, encoding=iencoding) as fin:
        txt = fin.read()
    final_sm2ym2num2good_hanzi_str__refined_by_hand = eval(txt)
    del fin, txt
    pinyin2hanzi_str = {
        f'{sm}{ym}{num}': good_hanzi_str
        for sm, ym2num2good_hanzi_str
            in final_sm2ym2num2good_hanzi_str__refined_by_hand.items()
        for ym, num2good_hanzi_str in ym2num2good_hanzi_str.items()
        for num, good_hanzi_str in num2good_hanzi_str.items()
        }

def join_GuaHua_Helper(GuaHua_Helper):
    '{JingGuaMing:(sm,ym)}8 -> {GuaMing : (sm,ym)}64'
    assert set(GuaHua_Helper) == set(JingGuaMings_str)
    assert all(len(sm_ym_pair) == 2 for sm_ym_pair in GuaHua_Helper.values())

    GuaMing2sm_ym_pair = {}
    for GuaMing, GuaHua in GuaMing2GuaHua.items():
        up_JingGuaMing, down_JingGuaMing = GuaHua
        GuaMing2sm_ym_pair[GuaMing] = (
            GuaHua_Helper[up_JingGuaMing][0]
            ,GuaHua_Helper[down_JingGuaMing][1]
            )
    return GuaMing2sm_ym_pair

# see: 'final_sm2ym2num2good_hanzi_str[refined_by_hand].txt'
# 天苍地诞雷攻山凸，离蛤习坎兑沼巽臭。
GuaHua_Helper = \
    {'乾':('c', 'ang1')#苍
    ,'坤':('d', 'an4')#诞
    ,'震':('g', 'ong1')#攻
    ,'艮':('t', 'u1')#凸
    ,'离':('h', 'a1')#蛤
    ,'坎':('k', 'an3')#坎
    ,'兑':('zh', 'ao3')#沼
    ,'巽':('ch', 'ou4')#臭
    }

if __name__ == '__main__':
    from pprint import pprint
    pinyin2hanzi_str = Global.pinyin2hanzi_str

    GuaMing2sm_ym_pair = join_GuaHua_Helper(GuaHua_Helper)
    #pprint(GuaMing2sm_ym_pair)
    #print('=======')
    for GuaMing in idx2GuaMing:
        sm, ym = GuaMing2sm_ym_pair[GuaMing]
        pinyin = sm+ym
        assert len(GuaMing) < 4
        assert len(pinyin) < 7
        hanzi_str = pinyin2hanzi_str[pinyin]
        print(f'{GuaMing:　<4}{pinyin: <8}{hanzi_str}')

