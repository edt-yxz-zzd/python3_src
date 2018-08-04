

from unicodedata import name as n
from .chars_of import chars_of_CJK, chars_of_name_startswith


def get_ords_names(s):
    ords = [hex(ord(ch)) for ch in s]
    names = list(map(n, s))
    return ords, names

birds = '⻦鸟'
le_s = '了了'
assert get_ords_names(le_s) ==\
       (['0xf9ba', '0x4e86'], ['CJK COMPATIBILITY IDEOGRAPH-F9BA', 'CJK UNIFIED IDEOGRAPH-4E86'])
assert get_ords_names(birds) == \
       (['0x2ee6', '0x9e1f'], ['CJK RADICAL C-SIMPLIFIED BIRD', 'CJK UNIFIED IDEOGRAPH-9E1F'])




s0 = {'CJK RADICAL THREAD', 'CJK RADICAL PERSON', 'CJK RADICAL LAME FOUR', 'CJK STROKE SP', 'CJK RADICAL MEAT', 'CJK RADICAL GRASS TWO', 'CJK STROKE SWG', 'CJK RADICAL DIVINATION', 'CJK RADICAL WEST TWO', 'CJK RADICAL SMALL ONE', 'CJK STROKE HP', 'CJK STROKE HZZ', 'CJK STROKE HZ', 'CJK RADICAL MOTHER', 'CJK STROKE HZT', 'CJK STROKE HZW', 'CJK STROKE HZZP', 'CJK STROKE HG', 'CJK RADICAL SIMPLIFIED YELLOW', 'CJK STROKE HZZZ', 'CJK RADICAL OLD', 'CJK STROKE HZG', 'CJK STROKE PZ', 'CJK STROKE HXWG', 'CJK STROKE XG', 'CJK RADICAL HEART ONE', 'CJK RADICAL NET ONE', 'CJK STROKE PD', 'CJK RADICAL EYE', 'CJK RADICAL FOOT', 'CJK RADICAL WALK TWO', 'CJK RADICAL HEAD', 'CJK RADICAL SEAL', 'CJK STROKE PG', 'CJK STROKE BXG', 'CJK RADICAL CITY', 'CJK RADICAL EAT TWO', 'CJK STROKE WG', 'CJK RADICAL PAW ONE', 'CJK RADICAL TURTLE', 'CJK RADICAL GRASS THREE', 'CJK STROKE Q', 'CJK STROKE P', 'CJK STROKE S', 'CJK RADICAL SECOND THREE', 'CJK RADICAL JADE', 'CJK RADICAL HAND', 'CJK STROKE H', 'CJK RADICAL C', 'CJK STROKE N', 'CJK RADICAL J', 'CJK STROKE D', 'CJK RADICAL SECOND TWO', 'CJK RADICAL MOON', 'CJK RADICAL SECOND ONE', 'CJK RADICAL SIMPLIFIED HORN', 'CJK RADICAL CHOKE', 'CJK RADICAL BRUSH ONE', 'CJK RADICAL MOUND TWO', 'CJK RADICAL BRUSH TWO', 'CJK STROKE T', 'CJK RADICAL SIMPLIFIED WHEAT', 'CJK RADICAL WATER ONE', 'CJK RADICAL LONG TWO', 'CJK RADICAL NET FOUR', 'CJK RADICAL KNIFE TWO', 'CJK STROKE HZZZG', 'CJK RADICAL WEST ONE', 'CJK STROKE SZZ', 'CJK RADICAL RAM', 'CJK RADICAL SIMPLIFIED WALK', 'CJK STROKE TN', 'CJK RADICAL DEATH', 'CJK RADICAL SNAKE', 'CJK STROKE SZWG', 'CJK RADICAL HEART TWO', 'CJK RADICAL WATER TWO', 'CJK RADICAL PAW TWO', 'CJK RADICAL BOLT OF CLOTH', 'CJK RADICAL NET THREE', 'CJK STROKE SWZ', 'CJK RADICAL TABLE', 'CJK RADICAL COW', 'CJK RADICAL LAME TWO', 'CJK RADICAL RAP', 'CJK RADICAL HORN', 'CJK RADICAL LAME THREE', 'CJK RADICAL SPIRIT TWO', 'CJK STROKE SG', 'CJK RADICAL BONE', 'CJK RADICAL CLOTHES', 'CJK RADICAL SHEEP', 'CJK RADICAL MOUND ONE', 'CJK STROKE SW', 'CJK STROKE ST', 'CJK STROKE SZ', 'CJK RADICAL BLUE', 'CJK RADICAL NET TWO', 'CJK RADICAL SNOUT TWO', 'CJK RADICAL SUN', 'CJK RADICAL SIMPLIFIED HALF TREE TRUNK', 'CJK UNIFIED IDEOGRAPH', 'CJK RADICAL MORTAR', 'CJK RADICAL SILK', 'CJK COMPATIBILITY IDEOGRAPH', 'CJK RADICAL SNOUT ONE', 'CJK RADICAL LAME ONE', 'CJK RADICAL WALK ONE', 'CJK RADICAL REPEAT', 'CJK STROKE HPWG', 'CJK RADICAL BOX', 'CJK RADICAL EWE', 'CJK RADICAL MESH', 'CJK RADICAL LONG ONE', 'CJK STROKE HZWG', 'CJK RADICAL SMALL TWO', 'CJK RADICAL DOG', 'CJK RADICAL EAT THREE', 'CJK RADICAL GRASS ONE', 'CJK RADICAL EAT ONE', 'CJK RADICAL BAMBOO', 'CJK RADICAL KNIFE ONE', 'CJK RADICAL GHOST', 'CJK RADICAL TIGER', 'CJK RADICAL FIRE', 'CJK RADICAL CIVILIAN', 'CJK RADICAL RAIN', 'CJK RADICAL SPIRIT ONE', 'CJK RADICAL CLIFF'}
if 0:
    _s0 = set(n(ch).split('-')[0] for ch in chars_of_CJK())
    assert _s0 == s0


s0_of_1 = {'CJK RADICAL SIMPLIFIED HORN', 'CJK RADICAL SNOUT ONE', 'CJK RADICAL CLIFF', 'CJK RADICAL WALK TWO', 'CJK RADICAL SMALL TWO', 'CJK RADICAL GRASS ONE', 'CJK RADICAL RAIN', 'CJK RADICAL FIRE', 'CJK RADICAL LAME ONE', 'CJK RADICAL CLOTHES', 'CJK RADICAL SECOND ONE', 'CJK RADICAL HEART TWO', 'CJK STROKE PD', 'CJK RADICAL NET THREE', 'CJK RADICAL EAT ONE', 'CJK STROKE Q', 'CJK STROKE XG', 'CJK STROKE HZ', 'CJK STROKE SZZ', 'CJK RADICAL NET TWO', 'CJK STROKE ST', 'CJK STROKE SW', 'CJK STROKE SP', 'CJK STROKE HP', 'CJK STROKE SZ', 'CJK RADICAL DIVINATION', 'CJK STROKE HG', 'CJK RADICAL THREAD', 'CJK STROKE HZZP', 'CJK RADICAL BOLT OF CLOTH', 'CJK STROKE HZZZ', 'CJK RADICAL MOUND TWO', 'CJK RADICAL PAW TWO', 'CJK STROKE HZG', 'CJK RADICAL NET FOUR', 'CJK RADICAL SHEEP', 'CJK STROKE N', 'CJK RADICAL PAW ONE', 'CJK STROKE SWG', 'CJK STROKE PZ', 'CJK RADICAL KNIFE ONE', 'CJK STROKE SWZ', 'CJK STROKE SG', 'CJK RADICAL MESH', 'CJK STROKE PG', 'CJK STROKE BXG', 'CJK RADICAL SIMPLIFIED WHEAT', 'CJK RADICAL MEAT', 'CJK RADICAL HEART ONE', 'CJK RADICAL MOUND ONE', 'CJK RADICAL MOTHER', 'CJK RADICAL SNAKE', 'CJK STROKE P', 'CJK RADICAL REPEAT', 'CJK RADICAL HORN', 'CJK RADICAL CHOKE', 'CJK RADICAL EAT THREE', 'CJK RADICAL SEAL', 'CJK STROKE HZZZG', 'CJK RADICAL SIMPLIFIED HALF TREE TRUNK', 'CJK STROKE T', 'CJK STROKE D', 'CJK RADICAL LAME FOUR', 'CJK RADICAL HEAD', 'CJK RADICAL EAT TWO', 'CJK RADICAL GHOST', 'CJK STROKE S', 'CJK RADICAL SPIRIT TWO', 'CJK RADICAL SECOND TWO', 'CJK RADICAL LONG ONE', 'CJK RADICAL BRUSH TWO', 'CJK RADICAL EYE', 'CJK STROKE H', 'CJK RADICAL SECOND THREE', 'CJK RADICAL SNOUT TWO', 'CJK STROKE SZWG', 'CJK RADICAL OLD', 'CJK RADICAL WALK ONE', 'CJK RADICAL LONG TWO', 'CJK RADICAL DEATH', 'CJK RADICAL WATER TWO', 'CJK STROKE WG', 'CJK STROKE HZZ', 'CJK RADICAL FOOT', 'CJK RADICAL SUN', 'CJK RADICAL COW', 'CJK STROKE HZT', 'CJK RADICAL SILK', 'CJK STROKE HZW', 'CJK RADICAL GRASS TWO', 'CJK RADICAL BLUE', 'CJK RADICAL CITY', 'CJK RADICAL NET ONE', 'CJK RADICAL MOON', 'CJK RADICAL MORTAR', 'CJK RADICAL PERSON', 'CJK RADICAL BAMBOO', 'CJK RADICAL HAND', 'CJK RADICAL WATER ONE', 'CJK STROKE TN', 'CJK RADICAL EWE', 'CJK RADICAL SMALL ONE', 'CJK STROKE HZWG', 'CJK RADICAL SIMPLIFIED WALK', 'CJK RADICAL WEST TWO', 'CJK RADICAL LAME THREE', 'CJK RADICAL SIMPLIFIED YELLOW', 'CJK RADICAL WEST ONE', 'CJK STROKE HPWG', 'CJK RADICAL LAME TWO', 'CJK RADICAL RAP', 'CJK RADICAL GRASS THREE', 'CJK RADICAL RAM', 'CJK RADICAL TIGER', 'CJK RADICAL BONE', 'CJK RADICAL BRUSH ONE', 'CJK STROKE HXWG', 'CJK RADICAL TABLE', 'CJK RADICAL TURTLE', 'CJK RADICAL JADE', 'CJK RADICAL KNIFE TWO', 'CJK RADICAL SPIRIT ONE', 'CJK RADICAL DOG', 'CJK RADICAL CIVILIAN', 'CJK RADICAL BOX'}
if 0:
    _s0_of_1 = set(n(ch) for ch in chars_of_CJK() if '-' not in n(ch))

s0_of_gt1 = s0 - s0_of_1
assert s0_of_gt1 == {'CJK UNIFIED IDEOGRAPH', 'CJK RADICAL J', 'CJK RADICAL C', 'CJK COMPATIBILITY IDEOGRAPH'}



assert {'CJK'} == set(name.split()[0] for name in s0_of_1)
n1_s0_of_1 = set(name.split()[1] for name in s0_of_1)
assert n1_s0_of_1 == {'STROKE', 'RADICAL'}

# 'STROKE' 笔画
# 'RADICAL' 根

if 0:
    cs = ''.join(chars_of_name_startswith('CJK COMPATIBILITY IDEOGRAPH'))
    i = cs.index('\U0002f800')
    assert i == 472
    cs1 = cs[:i]
    cs2 = cs[i:]

prefixes = ['CJK UNIFIED IDEOGRAPH-',
            'CJK COMPATIBILITY IDEOGRAPH-', 
            'CJK STROKE ',
            'CJK RADICAL ', # no '-'
            'CJK RADICAL J-',
            'CJK RADICAL C-']

if 0:
    cs_CJK = ''.join(chars_of_CJK())

    *ls, = map(lambda prefix: ''.join(chars_of_name_startswith(prefix)), prefixes)
    cs_UNIFIED, cs_COMPATIBILITY, cs_STROKE, cs_RADICAL, cs_RADICAL_J, cs_RADICAL_C = ls
    lens = [74605, 1014, 36, 115, 4, 22]
    assert list(map(len, ls)) == lens
    assert len(cs_CJK) == 75770 == sum(lens) - sum(lens[-2:])
    assert '㇀㇁㇂㇃㇄㇅㇆㇇㇈㇉㇊㇋㇌㇍㇎㇏㇐㇑㇒㇓㇔㇕㇖㇗㇘㇙㇚㇛㇜㇝㇞㇟㇠㇡㇢㇣' == cs_STROKE
    assert '⻫⻭⻯⻲' == cs_RADICAL_J
    assert '⺰⻅⻈⻉⻋⻐⻓⻔⻙⻚⻛⻜⻠⻢⻥⻦⻧⻪⻬⻮⻰⻳' == cs_RADICAL_C
    assert cs_RADICAL == '⺀⺁⺂⺃⺄⺅⺆⺇⺈⺉⺊⺋⺌⺍⺎⺏⺐⺑⺒⺓⺔⺕⺖⺗⺘⺙⺛⺜⺝⺞⺟⺠⺡⺢⺣⺤⺥⺦⺧⺨⺩⺪⺫⺬⺭⺮⺯⺰⺱⺲⺳⺴⺵⺶⺷⺸⺹⺺⺻⺼⺽⺾⺿⻀⻁⻂⻃⻄⻅⻆⻇⻈⻉⻊⻋⻌⻍⻎⻏⻐⻑⻒⻓⻔⻕⻖⻗⻘⻙⻚⻛⻜⻝⻞⻟⻠⻡⻢⻣⻤⻥⻦⻧⻨⻩⻪⻫⻬⻭⻮⻯⻰⻱⻲⻳'
    def begin_len2string(begin, L):
        ''.join(map(chr, range(0x2f800, 0x2f800+542)))
    assert cs_COMPATIBILITY == (
        '豈更車賈滑串句龜龜契金喇奈懶癩羅蘿螺裸邏樂洛烙珞落酪駱亂卵欄爛蘭鸞嵐濫藍襤拉臘蠟廊朗浪狼郎來冷勞擄櫓爐盧老蘆虜路露魯鷺碌祿綠菉錄鹿論壟弄籠聾牢磊賂雷壘屢樓淚漏累縷陋勒肋凜凌稜綾菱陵讀拏樂諾丹寧怒率異北磻便復不泌數索參塞省葉說殺辰沈拾若掠略亮兩凉梁糧良諒量勵呂女廬旅濾礪閭驪麗黎力曆歷轢年憐戀撚漣煉璉秊練聯輦蓮連鍊列劣咽烈裂說廉念捻殮簾獵令囹寧嶺怜玲瑩羚聆鈴零靈領例禮醴隸惡了僚寮尿料樂燎療蓼遼龍暈阮劉杻柳流溜琉留硫紐類六戮陸倫崙淪輪律慄栗率隆利吏履易李梨泥理痢罹裏裡里離匿溺吝燐璘藺隣鱗麟林淋臨立笠粒狀炙識什茶刺切度拓糖宅洞暴輻行降見廓兀嗀﨎﨏塚﨑晴﨓﨔凞猪益礼神祥福靖精羽﨟蘒﨡諸﨣﨤逸都﨧﨨﨩飯飼館鶴郞隷侮僧免勉勤卑喝嘆器塀墨層屮悔慨憎懲敏既暑梅海渚漢煮爫琢碑社祉祈祐祖祝禍禎穀突節練縉繁署者臭艹艹著褐視謁謹賓贈辶逸難響頻恵𤋮舘並况全侀充冀勇勺喝啕喙嗢塚墳奄奔婢嬨廒廙彩徭惘慎愈憎慠懲戴揄搜摒敖晴朗望杖歹殺流滛滋漢瀞煮瞧爵犯猪瑱甆画瘝瘟益盛直睊着磌窱節类絛練缾者荒華蝹襁覆視調諸請謁諾諭謹變贈輸遲醙鉶陼難靖韛響頋頻鬒龜𢡊𢡄𣏕㮝䀘䀹𥉉𥳐𧻓齃龎'
        + begin_len2string(0x2f800, 542)) == (
            begin_len2string(0xf900, 366) +
            begin_len2string(0xf900+366+2, 106) +
            begin_len2string(0x2f800, 542))

cs_STROKE = '㇀㇁㇂㇃㇄㇅㇆㇇㇈㇉㇊㇋㇌㇍㇎㇏㇐㇑㇒㇓㇔㇕㇖㇗㇘㇙㇚㇛㇜㇝㇞㇟㇠㇡㇢㇣'
print(cs_STROKE, get_ords_names(cs_STROKE))
stroke_names = get_ords_names(cs_STROKE)[-1]
short_stroke_names = [name.split()[-1] for name in stroke_names]
STROKE_NAMES = ''.join(sorted(set(''.join(short_stroke_names))))
assert STROKE_NAMES == 'BDGHNPQSTWXZ'
en_cn = 'B大D点G钩H横N捺P撇Q圈S竖T提W弯X斜Z折'
en2cn = dict(zip(en_cn[::2], en_cn[1::2]))
cn_short_stroke_names = [''.join(en2cn[ch] for ch in name) for name in short_stroke_names]
assert cn_short_stroke_names == \
       ['提', '弯钩', '斜钩', '大斜钩', '竖弯',
        '横折折', '横折钩', '横撇', '横折弯钩', '竖折弯钩',
        '横折提', '横折折撇', '横撇弯钩', '横折弯', '横折折折',
        '捺', '横', '竖', '撇', '竖撇',
        '点', '横折', '横钩', '竖折', '竖弯折',
        '竖提', '竖钩', '撇点', '撇折', '提捺',
        '竖折折', '竖弯钩', '横斜弯钩', '横折折折钩', '撇钩',
        '圈']
















