#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/CJK/CJK_data/笔画数到依笔顺排序的汉字串.py
view ../../python3_src/nn_ns/CJK/CJK_data/raw/汉字笔顺.py

nn_ns.CJK.CJK_data.笔画数到依笔顺排序的汉字串
py -m nn_ns.app.debug_cmd   nn_ns.CJK.CJK_data.笔画数到依笔顺排序的汉字串
py -m nn_ns.app.doctest_cmd nn_ns.CJK.CJK_data.笔画数到依笔顺排序的汉字串:__doc__ -v
py -m nn_ns.app.adhoc_argparser__main__call8module   nn_ns.CJK.CJK_data.笔画数到依笔顺排序的汉字串   ,str.切片囗囗笔画数到依笔顺排序的汉字串囗   =None  =None > /sdcard/0my_files/tmp/out4py/nn_ns.CJK.CJK_data.笔画数到依笔顺排序的汉字串..out.all.txt
view /sdcard/0my_files/tmp/out4py/nn_ns.CJK.CJK_data.笔画数到依笔顺排序的汉字串..out.all.txt

!mkdir ../../python3_src/nn_ns/CJK/CJK_data/output/笔画数到依笔顺排序的汉字串.py.out/
py -m nn_ns.app.adhoc_argparser__main__call8module   nn_ns.CJK.CJK_data.笔画数到依笔顺排序的汉字串   @not_show.输出到路径囗   =None  :../../python3_src/nn_ns/CJK/CJK_data/output/笔画数到依笔顺排序的汉字串.py.out/笔画数到依笔顺排序的汉字串.txt
view ../../python3_src/nn_ns/CJK/CJK_data/output/笔画数到依笔顺排序的汉字串.py.out/笔画数到依笔顺排序的汉字串.txt


from nn_ns.CJK.CJK_data.笔画数到依笔顺排序的汉字串 import 笔画数到依笔顺排序的汉字串

>>> from nn_ns.CJK.CJK_data.笔画数到依笔顺排序的汉字串 import 最大笔画数, 最大笔画数囗, 笔画数到依笔顺排序的汉字串, 笔画数到依笔顺排序的汉字串囗, 笔画数到依笔顺排序的汉字串囗长度, 笔画数到依笔顺排序的汉字串囗长度囗, 切片囗囗笔画数到依笔顺排序的汉字串囗
>>> from nn_ns.CJK.CJK_data.笔画数到依笔顺排序的汉字串 import 类囗笔画数到依笔顺排序的汉字串, 例囗笔画数到依笔顺排序的汉字串
>>> from nn_ns.CJK.CJK_data.笔画数到依笔顺排序的汉字串 import 输出到路径囗, 输出到文件囗


>>> 最大笔画数 == 最大笔画数囗()
True
>>> 笔画数到依笔顺排序的汉字串囗长度[1] == 笔画数到依笔顺排序的汉字串囗长度囗(1)
True
>>> 笔画数到依笔顺排序的汉字串[1] is 笔画数到依笔顺排序的汉字串囗(1)
True
>>> 笔画数到依笔顺排序的汉字串[2:5:2] == 切片囗囗笔画数到依笔顺排序的汉字串囗(2,5,2)
True


>>> def show1(*args):
...     for _ in map(print, 切片囗囗笔画数到依笔顺排序的汉字串囗(*args)):pass

>>> def show2__if_num_hzs_lt(num_hzs_upperbound, /):
...     for num_strokes, hzs in enumerate(笔画数到依笔顺排序的汉字串):
...         if 0 < len(hzs) < num_hzs_upperbound:
...             print((num_strokes, len(hzs), hzs))


>>> 最大笔画数
52
>>> 笔画数到依笔顺排序的汉字串囗长度
(0, 21, 63, 111, 256, 411, 765, 1248, 1717, 2043, 2301, 2568, 2767, 2497, 2358, 2227, 1919, 1537, 1211, 1018, 785, 551, 445, 323, 233, 137, 77, 66, 41, 18, 16, 6, 5, 8, 2, 2, 2, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1)


##看来py还是不太行，当py脚本文件 包含 超长汉字行 时，生成的代码有问题
>>> show1(0,2)
<BLANKLINE>
一丨亅丿丶乀乁⺄乙乚乛𠃊𠃋𠃌𠃍𠃑𠄌𠄎𡿨

#>>> show1(0,4)
<BLANKLINE>
一丨亅丿丶乀乁⺄乙乚乛𠃊𠃋𠃌𠃍𠃑𠄌𠄎𡿨
二丁丅十丆厂𠂇丂七匚匸丄刂卜冂𠂉亻⺁𠂆㐅乂 人入八𠆢⺈九儿几勹匕𠂊𠘨𠤎亠冫丷冖讠刁丩了凵卩阝 乃刀力乄厶又廴龴⺋㔾乜巜
三亍于干亏亐土士工扌卄艹才下寸㐉丌廾丈大兀尢兀𡯁与㐄㔿万夨弋𠫓上小凣⺌口囗山巾千乇乞川亿彳彡凢 亼个𠆤乊亽㐈亾兦亇犭丸久么凡勺及夂夊夕㐇饣丬广亡门䒑丫义氵忄宀之辶彐卂尸己已巳弓卫子孑孒屮卪孓也女乆刃刄飞劜习㐃叉彑纟马乡幺巛

>>> show2__if_num_hzs_lt(20)
(29, 18, '䰖驪䯁韊虋鬱麷靏䶪䶩鸜䶑䥹钃讟䀍𥩔纞')
(30, 16, '䆐驫鸝厵䂅䉹籱爨𪈳𨰹饢鱺鸞癵麣𩱳')
(31, 6, '䡿𨤍䚖𧖣灩䴐')
(32, 5, '䖇籲𨰻龖灪')
(33, 8, '䰱龗䴑䨊鱻麤爩𡤻')
(34, 2, '䯂䶫')
(35, 2, '䴒齾')
(36, 2, '䨺齉')
(39, 1, '靐')
(44, 1, '䲜')
(48, 1, '龘')
(52, 1, '䨻')




#>>> show2__if_num_hzs_lt(300)
(1, 21, '一丨亅丿丶乀乁⺄乙乚乛\ue818\ue819𠃊 𠃋𠃌𠃍𠃑𠄌𠄎𡿨')
(2, 63, '二丁丅十丆厂\ue816𠂇丂七匚匸丄刂卜冂\ue817𠂉亻⺁\ue815𠂆㐅乂人入八𠆢⺈九儿几勹匕\ue81c 𠂊𠘨𠤎亠冫丷冖讠刁丩了凵卩阝乃刀力乄厶又廴龴\ue81e⺋㔾乜巜\ue81d')
(3, 111, '三亍于干亏亐土士工扌卄艹才下寸㐉丌廾丈大兀尢兀𡯁与㐄㔿万夨弋𠫓上小凣⺌\ue822口囗山巾千乇乞川亿彳彡凢亼个𠆤乊亽㐈亾兦亇犭丸久么凡勺及夂夊夕㐇饣丬广亡门䒑丫义氵忄宀之辶彐卂尸己已巳弓卫子孑孒屮卪孓也女乆刃刄飞劜习㐃叉彑纟马乡幺巛')
(4, 256, '亖丰王龶\ue82b𤣩亓井开天夫元无韦专云弌㠪𠥼耂圡𡈽㐊㐋丐圠扎廿龷\ue82c艺木朩𣎴𥘅乤五巿帀邒㔹支丏厅卅不冇仄㔫太犬𠀋区历厷友尤歹匹厄辷车戸巨牙㸦屯戈兂旡比互切瓦卝止攴少尐⺗\ue823冃冄日曰中𠮜円𦉫乢𡴭內内冈水罓贝𠔿见𦉪禸午手牛龵\ue826毛气⺧壬牜\ue830𡈼升夭攵长仁什仃片仆仈仇仉化屲币仂仍仅仏斤爪𢒼丯戶反仐兮刈介仌从父爻乥仑尣𡯂爫仒今凶分乏公仓勻月卆厃氏𠂔勿勽匁欠风𠘰𧘇勼匂丹匀乌䢳卬凤勾厹殳㓅卞亣六文亢方闩火兯为斗㲸㣺忆灬㝉计订户㐧㓀礻讣㓁认⺳冗冘讥\ue838心丮肀尹卐夬尺㢧弖弔引丑䦹䦺卍爿孔巴㞢队𠙶阞収𠬝丒刅办夃以允㕚予邓劝㕕㕛厸双毌书毋乣幻')
(24, 233, '瓛蠺䰏䰐䰑鬢鬡㚁攬驝䮻驟𩧃䮺䮼驞壩 䟒䟑鼞囍攭韇韆䪋䪉虉䖃虂䘍虆䖀虈觀鸏矗欗欓欔鸉䫶䵆䵄䡼蠹鹽醽䤘釂釀醾醿㕔䶠礹礸䃺䝔靅䨷靂靈靃䴇靄靇䨸蠶艷鬭顰䶢䶡齵齶䶤齲齴齳齷鹼鸆鸈囓矖矙贜曭𡆀囕躤䠰躝䠯鷺躞躟䠮蠷蠵𡆇囑鸅羈䴉鸀羉巙䵱䵹穲穳䉶籩籬籪鸒黌鷽鱟儾雥雦齅齆軈𤿂䫵鸌䴌䴋鸃鸄衢艭瓥𨯨𨯧鑮𨯪鑩鑬䥶鑪䥵𨯬𨯩䥷𨯵鑫鑨貛䭦饝鱯𩼰䲔鱤鱩鱥䲐鱡鱦鱧鱢鱰鱞䲙鱮䲓鱠鱫䲒鱣䲑鱐𠓗䬟㺧䚭讙讕讑讖讒讓矕鸇鷹癱癲㿛㿚斖麠䴫贛䤗𩑈鷾鸁齹䴊鼈爤爣𪆵灠灞𤅟灝㶞㶟𤅡鸂灟襻襹𧟌襸衋鷫𢦀屭鷿鸊䰞韥孎䂎䌰纗䌱')
(25, 137, '𤫢纛䰓䰔鬣㚂攮𩧉䮽㩸㩹鼟壪𪇟䕿𧕴臡 韉䪊䖁蘒䫷欖欛欙欝欘欚䝄覊鸍䝕靉豒鬬𪙛齻䶣齺齸𪙊䴞顱𧹍矘䂄䴍鸎䨉囔曯躡躣躢躥𤴆鼉㘛㱎䵴䵲䵳黵髗䦆\ue84f犪䵜籭䉷籮籫齇㿩鑶鑵𨯿𨰃鑭鑰鑯𨰜鑱鑲鑳龣㒪饞饟䭧𣬚䲖鱴鱱鱬鱨䲘䲗鱭鱶鸑觿馕讘讛讗蠻臠㝈廳麡戅戆䊴䊳爦䶴顲爥灢鼝灣鸋㝲襽彠斸䥸糶㜼鸐矡纚䌳纙纘䌴')
(26, 77, '䰕驠驥驢䮾驣趲䖄䪍䪌顴飌虊䖂欜轥䡽釃釅釄䚕黶䃻㔶靊䨹䶦䶥虪糳𧹏矚躪躧躦䴎鸓氎㲲蠼圞䭳䵵籰𥸎籯釁㘜鸔㼖鑷鑺鑸鑴𨰉𨰝鑹龥龤䭨䲛鱵鱳鱲讝讚𪇵癳驡糷㶠灦灎灤䙱鼊㜻')
(27, 66, '鬤驧驩驦驤䮿顳䪎䴏䖆䖅𧅵虌鬰䡾靍鸖靎靋靌豓鬮䶧鸕蠽𨷻躩蠾黷馫䉸㸑犫齈䶐軉灥鑻𨰣𨰫鑼鑽𨰦䶵貜饠饡䭩鱷䲚鱸飍讞讜鑾鸗𤅷灧𤅺灨㦭飝纜纝䌵蠿')
(28, 41, '𤫩䯀驨𢺳鸛欟欞䤙鸘豔齽齼䶨鑿鸚𣌟𨈇躨䠱䘎囖㠨黸鼺雧钄钀钂钁𨰰鸙鱹䯬𪈠㿜癴麢戇龞爧䄥')
(29, 18, '䰖驪䯁韊虋鬱麷靏䶪䶩鸜䶑䥹钃讟䀍𥩔纞')
(30, 16, '䆐驫鸝厵䂅䉹籱爨𪈳𨰹饢鱺鸞癵麣𩱳')
(31, 6, '䡿𨤍䚖𧖣灩䴐')
(32, 5, '䖇籲𨰻龖灪')
(33, 8, '䰱龗䴑䨊鱻麤爩𡤻')
(34, 2, '䯂䶫')
(35, 2, '䴒齾')
(36, 2, '䨺齉')
(39, 1, '靐')
(44, 1, '䲜')
(48, 1, '龘')
(52, 1, '䨻')




#]]]'''
__all__ = r'''

最大笔画数
最大笔画数囗
笔画数到依笔顺排序的汉字串囗长度
笔画数到依笔顺排序的汉字串囗长度囗
笔画数到依笔顺排序的汉字串
笔画数到依笔顺排序的汉字串囗
切片囗囗笔画数到依笔顺排序的汉字串囗

类囗笔画数到依笔顺排序的汉字串
    例囗笔画数到依笔顺排序的汉字串

输出到路径囗
    输出到文件囗

'''.split()#'''
__all__

from nn_ns.CJK.CJK_data.汉字笔顺 import 汉字到笔顺码

from seed.helper.repr_input import repr_helper
from seed.io.may_open import may_open_stdin, may_open_stdout

def _5may_sf(may_sf, /):
    if may_sf is None:
        sf = 例囗笔画数到依笔顺排序的汉字串
    else:
        sf = may_sf
    return sf
def 输出到路径囗(may_sf, may_ofname, /, *, oencoding='utf8', force=False):
    sf = _5may_sf(may_sf)
    return sf.输出到路径囗(may_ofname, oencoding=oencoding, force=force)
def 输出到文件囗(may_sf, ofile, /):
    sf = _5may_sf(may_sf)
    return sf.输出到文件囗(ofile)


class 类囗笔画数到依笔顺排序的汉字串:
    def __init__(sf, 汉字到笔顺码, /):
        (笔画数到依笔顺排序的汉字串, 笔画数到依笔顺排序的汉字串囗长度) = _mk(汉字到笔顺码)
        sf._hz2istrokes = 汉字到笔顺码
        sf._num_strokes2hzs = 笔画数到依笔顺排序的汉字串
        sf._num_strokes2num_hzs = 笔画数到依笔顺排序的汉字串囗长度

    def __repr__(sf, /):
        return repr_helper(sf, sf._hz2istrokes)

    @property
    def 笔画数到依笔顺排序的汉字串(sf, /):
        return sf._num_strokes2hzs
    @property
    def 笔画数到依笔顺排序的汉字串囗长度(sf, /):
        return sf._num_strokes2num_hzs

    @property
    def 最大笔画数(sf, /):
        return -1+len(sf._num_strokes2num_hzs)

    def 最大笔画数囗(sf, /):
        return sf.最大笔画数

    def 笔画数到依笔顺排序的汉字串囗长度囗(sf, 笔画数, /):
        return sf.笔画数到依笔顺排序的汉字串囗长度[笔画数]

    def 笔画数到依笔顺排序的汉字串囗(sf, 笔画数, /):
        return sf.笔画数到依笔顺排序的汉字串[笔画数]

    def 切片囗囗笔画数到依笔顺排序的汉字串囗(sf, 笔画数囗下界含, 笔画数囗上界超, 步长=1, /):
        return sf.笔画数到依笔顺排序的汉字串[笔画数囗下界含:笔画数囗上界超:步长]

    def 输出到路径囗(sf, may_ofname, /, *, oencoding='utf8', force=False):
        omode = 'wt' if force else 'xt'
        with may_open_stdout(may_ofname, omode, encoding=oencoding) as fout:
            sf.输出到文件囗(fout)
    def 输出到文件囗(sf, ofile, /):
        for num_strokes, hzs in enumerate(sf.笔画数到依笔顺排序的汉字串):
            #if 0 < len(hzs) < num_hzs_upperbound:
            if hzs:
                print(f'{num_strokes}:{len(hzs)}:{hzs!s}', file=ofile)



def _mk(汉字到笔顺码, /):
    M = max(map(len, 汉字到笔顺码.values()))
    lss = [[] for _ in range(M+1)]
    for hz, s in 汉字到笔顺码.items():
        num_strokes = len(s)
        lss[num_strokes].append((num_strokes, s, hz))
    for num_strokes, ls in enumerate(lss):
        ls.sort()
        lss[num_strokes] = hzs = ''.join(hz for (num_strokes, s, hz) in ls)
        assert len(hzs) == len(ls)
    lss = tuple(lss)
    assert sum(map(len, lss)) == len(汉字到笔顺码)
    笔画数到依笔顺排序的汉字串 = lss
    笔画数到依笔顺排序的汉字串囗长度 = tuple(map(len, 笔画数到依笔顺排序的汉字串))
    return (笔画数到依笔顺排序的汉字串, 笔画数到依笔顺排序的汉字串囗长度)

例囗笔画数到依笔顺排序的汉字串 = 类囗笔画数到依笔顺排序的汉字串(汉字到笔顺码)

最大笔画数= 例囗笔画数到依笔顺排序的汉字串.最大笔画数
最大笔画数囗= 例囗笔画数到依笔顺排序的汉字串.最大笔画数囗

笔画数到依笔顺排序的汉字串= 例囗笔画数到依笔顺排序的汉字串.笔画数到依笔顺排序的汉字串
笔画数到依笔顺排序的汉字串囗= 例囗笔画数到依笔顺排序的汉字串.笔画数到依笔顺排序的汉字串囗

笔画数到依笔顺排序的汉字串囗长度= 例囗笔画数到依笔顺排序的汉字串.笔画数到依笔顺排序的汉字串囗长度
笔画数到依笔顺排序的汉字串囗长度囗= 例囗笔画数到依笔顺排序的汉字串.笔画数到依笔顺排序的汉字串囗长度囗

切片囗囗笔画数到依笔顺排序的汉字串囗= 例囗笔画数到依笔顺排序的汉字串.切片囗囗笔画数到依笔顺排序的汉字串囗






from nn_ns.CJK.CJK_data.笔画数到依笔顺排序的汉字串 import 笔画数到依笔顺排序的汉字串

from nn_ns.CJK.CJK_data.笔画数到依笔顺排序的汉字串 import 最大笔画数, 最大笔画数囗, 笔画数到依笔顺排序的汉字串, 笔画数到依笔顺排序的汉字串囗, 笔画数到依笔顺排序的汉字串囗长度, 笔画数到依笔顺排序的汉字串囗长度囗, 切片囗囗笔画数到依笔顺排序的汉字串囗
from nn_ns.CJK.CJK_data.笔画数到依笔顺排序的汉字串 import 类囗笔画数到依笔顺排序的汉字串, 例囗笔画数到依笔顺排序的汉字串
from nn_ns.CJK.CJK_data.笔画数到依笔顺排序的汉字串 import 输出到路径囗, 输出到文件囗


