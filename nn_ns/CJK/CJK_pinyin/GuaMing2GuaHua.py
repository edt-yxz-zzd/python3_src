

__all__ = '''
    GuaMing2GuaHua
    GuaMing2idx
    idx2GuaMing

    JingGuaMings_str
    GuaHuas_str
    '''.split()

#经卦名
JingGuaMings_str = '乾坤震艮离坎兑巽'
#重卦名　卦画
GuaHuas_str = '''
乾卦　　乾上乾下
坤卦　　坤上坤下
屯卦　　坎上震下
蒙卦　　艮上坎下
需卦　　坎上乾下
讼卦　　乾上坎下
师卦　　坤上坎下
比卦　　坎上坤下
小畜卦　巽上乾下
履卦　　乾上兑下
泰卦　　坤上乾下
否卦　　乾上坤下
同人卦　乾上离下
大有卦　离上乾下
谦卦　　坤上艮下
豫卦　　震上坤下
随卦　　兑上震下
蛊卦　　艮上巽下
临卦　　坤上兑下
观卦　　巽上坤下
噬嗑卦　离上震下
贲卦　　艮上离下
剥卦　　艮上坤下
复卦　　坤上震下
无妄卦　乾上震下
大畜卦　艮上乾下
颐卦　　艮上震下
大过卦　兑上巽下
习坎卦　坎上坎下
离卦　　离上离下
咸卦　　兑上艮下
恒卦　　震上巽下
遯卦　　乾上艮下
大壮卦　震上乾下
晋卦　　离上坤下
明夷卦　坤上离下
家人卦　巽上离下
睽卦　　离上兑下
蹇卦　　坎上艮下
解卦　　震上坎下
损卦　　艮上兑下
益卦　　巽上震下
夬卦　　兑上乾下
姤卦　　乾上巽下
萃卦　　兑上坤下
升卦　　坤上巽下
困卦　　兑上坎下
井卦　　坎上巽下
革卦　　兑上离下
鼎卦　　离上巽下
震卦　　震上震下
艮卦　　艮上艮下
渐卦　　巽上艮下
归妹卦　震上兑下
丰卦　　震上离下
旅卦　　离上艮下
巽卦　　巽上巽下
兑卦　　兑上兑下
涣卦　　巽上坎下
节卦　　坎上兑下
中孚卦　巽上兑下
小过卦　震上艮下
既济卦　坎上离下
未济卦　离上坎下
'''
GuaHuas_str = GuaHuas_str.strip()

def _make():
    # -> (GuaMing2GuaHua, GuaMing2idx, idx2GuaMing)
    # GuaMing2GuaHua :: {rex'\S{1,2}卦' : '\S\S'}
    # GuaMing2idx :: {rex'\S{1,2}卦' : [0..63]}
    # idx2GuaMing :: [rex'\S{1,2}卦']
    #
    GuaHua_strs = GuaHuas_str.split('\n')
    assert len(GuaHua_strs) == 64
    GuaMing2GuaHua = {}
    GuaMing2idx = {}
    idx2GuaMing = []
    for idx, GuaHua_str in enumerate(GuaHua_strs):
        GuaMing, GuaHua = GuaHua_str.split()
        assert GuaMing[-1] == '卦'
        assert GuaHua[1::2] == '上下'
        GuaHua = GuaHua[::2]
        assert len(GuaHua) == 2
        GuaMing2GuaHua[GuaMing] = GuaHua
        GuaMing2idx[GuaMing] = idx
        idx2GuaMing.append(GuaMing)
    GuaHuas = set(GuaMing2GuaHua.values())
    assert len(GuaHuas) == 64

    JingGuaMings = {JingGuaMing
                    for GuaHua in GuaHuas
                    for JingGuaMing in GuaHua}
    assert len(JingGuaMings) == 8
    assert set(JingGuaMings_str) == JingGuaMings

    for JingGuaMing in JingGuaMings:
        head = '习' if JingGuaMing == '坎' else ''
        try:
            assert f'{head}{JingGuaMing}卦' in GuaMing2GuaHua
        except:
            print(GuaMing2GuaHua)
            print(JingGuaMing)
            raise
    return (GuaMing2GuaHua, GuaMing2idx, idx2GuaMing)

#（重）卦名->卦画
#（重）卦名->序号
(GuaMing2GuaHua, GuaMing2idx, idx2GuaMing) = _make()

if __name__ == '__main__':
    from pprint import pprint
    pprint(GuaMing2GuaHua)









