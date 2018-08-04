

# 2005年中华新韵（14韵）
# 注意多音字


中华新韵2005年 = '''
一麻 a,ia,ua
二波 o,e,uo
三皆 ie,üe
四开 ai,uai
五微 ei,ui(uei)
六豪 ao,iao
七尤 ou,iu(iou)
八寒 an,ian,uan,üan
九文 en,in(ien),un(uen),ün(üen)
十唐 ang,iang,uang
十一庚 eng,ing,ong,iong
十二齐 i,er,ü
十三支 (-i)（零韵母）
十四姑 u
'''
'''
空韵：hm、hng、h、m、n、ng... ??? how ???
十三支：zi, ci, si, zhi, chi, shi, ri
'''

import re
import itertools # chain

中华新韵2005_rex = re.compile(
    '(?P<拼音>'
        '(?P<十三支>zi|ci|si|zhi|chi|shi|ri)'
        '|(?P<其它十三韵>'
            '(?P<声母>b|p|m|f|d|t|n|l|g|k|h|j|q|x|z|c|s|r|zh|ch|sh|y|w|)'
            '(?P<韵母>'
                '(?P<一麻>a|ia|ua)'
                '|(?P<二波>o|e|uo)'
                '|(?P<三皆>ie|ve|ue)' # add 'ue'
                '|(?P<四开>ai|uai)'
                '|(?P<五微>ei|ui|uei)'
                '|(?P<六豪>ao|iao)'
                '|(?P<七尤>ou|iu|iou)'
                '|(?P<八寒>an|ian|uan|van)'
                '|(?P<九文>en|in|ien|un|uen|vn|ven)'
                '|(?P<十唐>ang|iang|uang)'
                '|(?P<十一庚>eng|ing|ong|iong)'
                '|(?P<十二齐>i|er|v)'
                '|(?P<十四姑>u)'
            ')'
        ')'
        '|(?P<空韵>[hmng]+)'
    ')'
    '(?P<声调>[1-4]?)'
    )


def init中华新韵():
    中华新韵2005年.strip()


def 拼音2中华新韵韵目(拼音):
    m = 中华新韵2005_rex.fullmatch(拼音)
    if not m:
        raise ValueError('not PinYin')
    声调 = m['声调']
    声调 = int(声调) if 声调 else 0
    assert 0 <= 声调 <= 4

    if m['其它十三韵']:
        # m['其它十三韵']['韵母']
        韵目, = (k for k,v in m.groupdict().items()
                if v is not None
                    and k not in {'拼音', '其它十三韵', '声母', '韵母', '声调'}
                )
    elif m['十三支']:
        韵目 = '十三支'
    elif m['空韵']:
        raise NotImplementedError('不知 中华新韵 中 空韵 如何处理')
    else:
        raise logic-error
    return 韵目, 声调

汉语拼音音节表 = '''
// a o e ai ei ao ou er an en ang eng
b  ba bo bai bei bao ban ben bang beng bi bie biao bian bin bing
p  pa po pai pao pou pan pen pang peng pi pie piao pian pin ping
m  ma mo me mai mao mou man men mang meng mi mie miao miu mian min ming
f  fa fo fei fou fan fen fang feng
d  da de dai dei dao dou dan dang deng di die diao diu dian ding
t ta te tai tao tou tan tang teng ti tie tiao tian ting
n  na nai nei nao no nen nang neng ni nie niao niu nian nin niang ning
l  la le lai lei lao lou lan lang leng li lia lie liao liu lian lin liang ling
g  ga ge gai gei gao gou gan gen gang geng
k  ka ke kai kou kan ken kang keng
h ha he hai hei hao hou hen hang heng
j  ji jia jie jiao jiu jian jin jiang jing
q qi qia qie qiao qiu qian qin qiang qing
x  xi xia xie xiao xiu xian xin xiang xing
zh zha zhe zhi zhai zhao zhou zhan zhen zhang zheng
ch cha che chi chai chou chan chen chang cheng
sh sha she shi shai shao shou shan shen shang sheng
r re ri rao rou ran ren rang reng
z  za ze zi zai zao zou zang zeng
c  ca ce ci cai cao cou can cen cang ceng
s sa se si sai sao sou san sen sang seng
y  ya yao you yan yang yu ye yue yuan yi yin yun ying
w  wa wo wai wei wan wen wang weng wu
'''
汉语拼音音节ls = tuple(itertools.chain.from_iterable(line.split()[1:]
                        for line in 汉语拼音音节表.strip().split('\n')))


#rint(拼音2中华新韵韵目('yin2'))
#rint(拼音2中华新韵韵目('ri'))

def test():
    try:
        print(拼音2中华新韵韵目('hng'))
    except NotImplementedError:
        pass
    else:
        raise logic-error

    for y in 汉语拼音音节ls:
        #rint(y)
        _, is0 = 拼音2中华新韵韵目(y)
        assert is0 == 0
test()

