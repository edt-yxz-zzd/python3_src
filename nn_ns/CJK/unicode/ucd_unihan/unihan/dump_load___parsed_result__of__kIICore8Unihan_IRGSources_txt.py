

r'''
to load parsed_result of kIICore@Unihan_IRGSources.txt


======================
.readonly__level_char2char_pt_rngs
    :: MapView {char:NonTouchRanges}
.readonly__sourceIRG_char2char_pt_rngs
    :: MapView {char:NonTouchRanges}
.readonly__levelA_common_char_pt_rngs
    :: NonTouchRanges
    = levelA_common_char_pt_rngs


======================
.dataobj
    :: (parsed_result, extra_derived_result)
    mutable
.state
    = compact_result
    mutable

======================
.parsed_result
    :: (level_char2char_pt_rngs, sourceIRG_char2char_pt_rngs)
    mutable
.extra_derived_result
    :: levelA_common_char_pt_rngs
    immutable
.compact_result
    :: cased_char2char_pt_rngs__HexReprInt
    mutable


======================
.level_char2char_pt_rngs/.sourceIRG_char2char_pt_rngs
    :: {char:NonTouchRanges}
        mutable
    :: (tmp) {char:StackStyleSimpleIntSet}
        mutable
    ###conceptual:
    :: {char: [(int, int)]}
    :: {char: [(HexReprInt, HexReprInt)]}
.levelA_common_char_pt_rngs
    :: NonTouchRanges
        immutable
.cased_char2char_pt_rngs
.cased_char2char_pt_rngs__HexReprInt
    # st 4 store
    :: (literal_store) {f'{case}={key_char}': [(HexReprInt, HexReprInt)]}
        mutable
    case = "lvl" | "src"
    ###conceptual:
    :: {str: [(int, int)]}
======================




======================
e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/dump_load___parsed_result__of__kIICore8Unihan_IRGSources_txt.py
.+1,$s/Blocks/kIICore8Unihan_IRGSources/g
.+1,$s/UCD\C/Unihan/g
.+1,$s/\<ucd\>\C/unihan/g




======================
nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__kIICore8Unihan_IRGSources_txt

py -m nn_ns.app.debug_cmd   nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__kIICore8Unihan_IRGSources_txt

py -m nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__kIICore8Unihan_IRGSources_txt -i /sdcard/0my_files/unzip/e_book/unicode_13__Unihan/Unihan_IRGSources.txt --donot_output_result4load
py -m nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__kIICore8Unihan_IRGSources_txt -i /sdcard/0my_files/unzip/e_book/unicode_13__Unihan/Unihan_IRGSources.txt --dump ver13_0 --donot_output_result4load

py -m nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__kIICore8Unihan_IRGSources_txt --load ver13_0 --donot_output_result4load > /sdcard/0my_files/tmp/_.txt
view /sdcard/0my_files/tmp/_.txt
    get:
        hz_2143 = levelA_common_hz_str@ver13_0



from nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__kIICore8Unihan_IRGSources_txt import findout_available_version_strs, load_readonly_level_char2char_pt_rngs_from_compact_result_file__ver, load_readonly_sourceIRG_char2char_pt_rngs_from_compact_result_file__ver, load_readonly_levelA_common_char_pt_rngs_from_compact_result_file__ver



from nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__kIICore8Unihan_IRGSources_txt import cache_view__version_str2readonly_dataobj


from nn_ns.CJK.unicode.ucd_unihan.unihan.parse__kIICore8Unihan_IRGSources_txt import parse__kIICore8Unihan_IRGSources_txt, helper4parse__Unihan_kIICore8Unihan_IRGSources_txt as _helper4parse
######from nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__kIICore8Unihan_IRGSources_txt import _cfg, Config4load_compact_result_file4Unihan_kIICore8Unihan_IRGSources_txt




======================
view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/parse__kIICore8Unihan_IRGSources_txt.py
view /sdcard/0my_files/unzip/e_book/unicode_13__Unihan/Unihan_IRGSources.txt
# Unihan_IRGSources.txt
# Date: 2020-02-18 18:27:33 GMT [JHJ]
# Unicode version: 13.0.0

view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/parse__kIICore8Unihan_IRGSources_txt.py.out.ver13_0.txt
!du -h ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/parse__kIICore8Unihan_IRGSources_txt.py.out.ver13_0.txt
    ver1:548K!!!.to_hex_repr_pair_list
    ver2:292K!!!.to_hexXhexszpair_list
    ver3:244K!!!.to_len_rng2hexbegins
        !du -h ../../python3_src/seed/data_funcs/rngs.py
            88K
    ver4:156K!!!.to_len_rng2hexbegins_str
        !du -h ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/dump_load___parsed_result__of__kIICore8Unihan_IRGSources_txt.py
            16K
    ver5:92K!!!.to_len_rng2begin_chars
        ...ok?
## !rm ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/parse__kIICore8Unihan_IRGSources_txt.py.out.ver13_0.txt
    after get: hz_2143



#'''


__all__ = '''
    findout_available_version_strs

    load_readonly_level_char2char_pt_rngs_from_compact_result_file__ver
    load_readonly_sourceIRG_char2char_pt_rngs_from_compact_result_file__ver
    load_readonly_levelA_common_char_pt_rngs_from_compact_result_file__ver

    cache_view__version_str2readonly_dataobj


    '''.split()




___begin_mark_of_excluded_global_names__1___ = ...
from nn_ns.CJK.unicode.ucd_unihan.unihan.parse__kIICore8Unihan_IRGSources_txt import parse__kIICore8Unihan_IRGSources_txt, helper4parse__Unihan_kIICore8Unihan_IRGSources_txt as _helper4parse

from seed.helper.IConfig4load_versioned_repr_txt_file import IConfig4load_versioned_repr_txt_file, Config4load_versioned_repr_txt_file__using__IHelper4parse__xxx_txt__stable_repr__expand_top_layer
from seed.abc.abc__ver0 import override
from seed.helper.stable_repr import stable_repr__expand_top_layer
from nn_ns.CJK.unicode.ucd_unihan._main4dump_load___parsed_result__of__xxx_txt import mainT as _mainT, load_readonly_dataobj_from_compact_result_file__ver as _load_readonly_dataobj_from_compact_result_file__ver

___end_mark_of_excluded_global_names__1___ = ...


#[[[

_cfg = Config4load_versioned_repr_txt_file__using__IHelper4parse__xxx_txt__stable_repr__expand_top_layer(_helper4parse
    ,dataobj_immutable = False
    ,state_immutable = False
    ,__file__            =__file__
    ,data_dir_rpath     ='./'
    ,basename_fmt       ='parse__kIICore8Unihan_IRGSources_txt.py.out.{}.txt'
    ,version_str__rex   =r'^ver[0-9]+_[0-9]+$'
    ,encoding           ='utf8'
    )

#]]]







def load_readonly_level_char2char_pt_rngs_from_compact_result_file__ver(version_str, /, *, may_path_bypass_version_str=None):
    'version_str -> readonly__level_char2char_pt_rngs'
    readonly__dataobj = _load_readonly_dataobj_from_compact_result_file__ver(_cfg, version_str, may_path_bypass_version_str=may_path_bypass_version_str)
    (readonly__parsed_result, readonly__extra_derived_result) = readonly__dataobj

    (readonly__level_char2char_pt_rngs, readonly__sourceIRG_char2char_pt_rngs) = readonly__parsed_result

    return readonly__level_char2char_pt_rngs

def load_readonly_sourceIRG_char2char_pt_rngs_from_compact_result_file__ver(version_str, /, *, may_path_bypass_version_str=None):
    'version_str -> readonly__sourceIRG_char2char_pt_rngs'
    readonly__dataobj = _load_readonly_dataobj_from_compact_result_file__ver(_cfg, version_str, may_path_bypass_version_str=may_path_bypass_version_str)
    (readonly__parsed_result, readonly__extra_derived_result) = readonly__dataobj

    (readonly__level_char2char_pt_rngs, readonly__sourceIRG_char2char_pt_rngs) = readonly__parsed_result

    return readonly__sourceIRG_char2char_pt_rngs

def load_readonly_levelA_common_char_pt_rngs_from_compact_result_file__ver(version_str, /, *, may_path_bypass_version_str=None):
    'version_str -> readonly__levelA_common_char_pt_rngs'
    readonly__dataobj = _load_readonly_dataobj_from_compact_result_file__ver(_cfg, version_str, may_path_bypass_version_str=may_path_bypass_version_str)
    (readonly__parsed_result, readonly__extra_derived_result) = readonly__dataobj

    readonly__levelA_common_char_pt_rngs = readonly__extra_derived_result

    return readonly__levelA_common_char_pt_rngs









main = _mainT(
    description
    ='parse,dump,load kIICore@Unihan_IRGSources.txt#ETL tool (extract, transform, load)'
    ,epilog
    =''
    ,parse__xxx_txt__lines
    =parse__kIICore8Unihan_IRGSources_txt
    ,cfg4load_compact_result_file4xxx_txt
    =_cfg
    ,parsed_result2dataobj
    =_helper4parse.parsed_result2dataobj
    ,args4repr
    =[]
    ,kwargs4repr
    ={}
    #=dict(maybe_max_depth4repr=1)
    #=dict(maybe_max_depth4repr=None)
    ,args4dump
    =[]
    ,kwargs4dump
    ={}
    )
if __name__ == "__main__":
    main()



findout_available_version_strs = _cfg.findout_available_version_strs

cache_view__version_str2readonly_dataobj = _cfg.get_view_of_cache__version_str2readonly_dataobj()




hz_2143 = levelA_common_hz_str__Unihan_ver13_0 = \
        '一丁七丈三上下不丑且丕世丘丙丞中串丸丹主乃久之乍乎乏乖乙九乞也乳乾了予事二于云互五井些亡交亥亦亨享京亭亮人什仁仄仇今介仍仔仕他付仙仟代令以仰仲件任企伉伊伍伏伐休伯伴伶伸伺似伽佃但位低住佐佑何余佛作佩佰佳使侃侈例侍侏供依侮侯侵便促俄俊俑俗俚保俟信修俯俳俸俺倍倒候倚借倦倪倭偈偏偕做停健偶傀傅傍催傲像僖僚僧僭僻儒儡兀允元兄充兆先光克免兜入全八公六共兵其具典兼冀再冒冕冠冥冬冶冷冽准凋凌凝凡凰凶凸凹出函刀刃分切刊刎刑列初判利刮到制刷券刺刻剃削剋剌前剖剪副割剽劈力功加劣助努劫劾勃勇勉勒勘募勤勾勿包匈匐匕化北匙匠匡匣匪匹匿十千升午卉半卑卒卓南博卜卞占卦卯印危卵卿厄厘厚原厥去又叉及友反叔取受叛口古句叩只叫召可台叱史右司吃各合吉同名后吏吐向君吝吟吠否含吸吹吻吼吾呈告周味呵呻呼命咀咆和咎咫咬咳咸咽哀品哄哈哉哥哨哭哮哲哺唆唐唯唱唾啄商啖啼喀善喉喊喘喜喝喧嗅嗜嗟嗣嗤嘉嘲嘴嘶器噫嚼囚四回因困固圃圈土在圭地址均坊坐坑坡坤坦坪垂型垠垢垣埃埋城域埠培基堂堆堡堤堪堰堵塑塔塘塾境墓墟墨壁壑壕壤士壬壹夏夕外夙多夜大天太夫夭央失夷奄奇奈奉奎奏契奔奕套奚奠奢女奴奸好如妃妄妊妓妖妙妥妨妹妻妾姆始姐姑姓委姚姜姨姻姿威娃娑娘娜娟娠娥娩娼婆婉婚婢媒媚媛嫁嫉嫌嫡嫦嫩嬉子孔孕字存孚孜孝孟季孤孰孵宅宇守安宋完宏宗官宙定宛宜客宣室宥宦宰害宴宵家容宿寂寄寅密寇富寐寒寓寞察寡寨寮寸寺封射尉尊小少尖尤就尹尺尼尾尿局居屈屋屎屑展屠履屯山屹岐岑岩岱岳岷岸峙峨峰峻崇崎崔崖崩嵌嵩巍川州巡工左巧巨巫差己已巳巴巷巾市布帆希帑帖帛帝席常帽幅幌幕幢干平年幸幻幼幽庇序底店庚府度座庭庵庶康庸廉廊廓廖延廷建弄弊式弓引弗弘弛弟弦弧弩弱弼彗形彩彪彬彭彰影彷役彼往征待徇徊律徐徒得徘徙御徨循微徽心必忌忍忖志忘忙忠快念忽忿怒怖思怠怡急性怨怪怯恃恍恐恒恕恢恣恨恩恪恬恭息恰悉悍悔悖悟悠患悲悴悸悼情惑惚惜惟惠惰想惶惹惺愁愈愉意愕愚感愧慈慌慕慢慧慨慰慷憎憔憧憩憬憾懈懿戈戊戌戍戎成我戒或戚戟截戮戴房所扁扇扈扉手才打托扮扶批承技抄抉把抑抒投抗折披抱抵抹押抽拇拉拌拍拐拒拓拗拘拙招括拭拮拱拳拷拾拿持指按挑挫振挺挽捉捏捐捕捧捷捻授掉掌排掖掘掠探接控推掩措描提揖握援搬搭摘摩摸摺撒撞撤播撮撰擅操擒擦攀攘攫支收改攻放政故效敏救敖敞敢散敦敬敲整敷文斌斐斑斗料斜斟斡斤斥斧斯新方於施旁旅旋族旗日旦旨早旬旭旱旺昆昊昌明昏易昔星映春昧昨昭是晃晏晤晦晨普景晴晶智暇暑暖暗暮暴曙曜曝曦曰曲曳更曹曼曾替最月有朋服朔朕朗望朝期朦木未末本札朱朴朽杉李杏材村杖杜杞束杭杯杰杳杵杷松板枇析枕林枚果枝枯架柄柏某柑染柔柚柩柯柱柳柴栓校株核根格栽桂桃案桐桑桓桔桶梁梅梓梗梢梧梨梯械梳梵棉棋棍棒棘棚棠森棺椅植椎椒椰椿楔楚楞楠楫楷榕榛榜榴槌槐槽樊樟模樵樽橘橙橡檀檄欠次欣欲欺款歌止正此武歪死殆殉殊殖段殷殿毅母毒毓比毛毫氏民氓水永氾汀汁求汐汕汗汝江池汪汰汲汽沁沂沃沈沌沐沙沛沫沮河沸油治沼沽沿泄泉泊泌法泗泡波泣泥注泰泳洋洗洛洞津洪洲活洽派流浙浚浣浦浩浪浮浴海浸消涌涎涓涯液涵淆淇淋淑淘淞淡淫淮深淳混淹添渚渠渡渤渥渭港游渺湃湍湖湘湛源溜溢溥溪溯溶溺滂滋滑滓滔滴漂漆漏演漠漫漱潘潭潮潺澄澎澳澹激濠濡濯瀑瀚瀛灌火灰灸灼炊炎炒炙炬炭炯炳炸烈烙烹焉焙焚焦然煌煎煤照煮煽熄熊熔熙熟熹燃燎燕燥燧燮爆爪爬爵父爽片版牌牒牙牛牝牟牡牢牧物牲特犀犬犯狂狄狎狐狗狙狡狩狼猖猛猜猥猩猷猾猿獗玄率玉王玖玩玲玳珀珊珍珠班球琅理琉琢琥琳琴琵琶瑁瑕瑙瑚瑛瑜瑞瑟璃璋璧瓜瓢瓣瓦瓷甘甚生甥用甫田由甲申男甸界畏畔留畜略畦番畸疆疏疑疝疥疫疲疵疹疼疽疾病症痔痕痘痛痢痰瘤癌癖癸登白百的皆皇皎皓皮皿盂盆盈益盒盛盟目盲直相盾省眉看眠眩眷眸眺眼睛睡督睦睫睿瞑瞥瞬瞭瞰瞳瞻瞿矗矛矜矢知矩短矮石砂砥砧破硝硫硬碌碑碗碧磁磊磋磐磨礁示社祀祁祇祈祉祖祗祚祝神祠祥票祭祺禁福禧禹禽禾秀私秉秋科秒秘租秤秦秧秩移稀程稍稔稚稠稷稼稽稿穀穆穗穴究穹空穿突窄窈窒窘窟立站竟章竣童端竹竺竿笑笙笛笠符第等筋筏筐筒答策筵箔箕算管箭箱箴篆篇簇簿籍米粉粒粗粘粟粥精糊糖糟糠系紊素索紫累絮繁纂罐罪置署罹羊美羚羞群羲羹羽翁翅翌翔翟翠翡翩翰翼耀老考者耆而耐耕耗耘耳耶耽耿聆聊聘聚聿肆肇肉肋肌肖肛肝股肢肥肩肪肯肱育肴肺胃背胎胚胞胡胤胥胱胴胸能脂脆脊脾腋腐腑腔腕腰腱腹腺腿膀膏膜膝膨膳臀臂臆臣自臭至致臻臼舅舌舍舒舜舞舟航舫般舵舶舷船艇良色艾芋芍芒芙芝芥芬芭芯花芳芷芸芹芽苑苔苗苛苞若苦英茂范茄茅茉茗茨茫茱茶茸茹荀草荏荒荷荻莉莎莞莫莽菁菊菌菜菩菱菲萃萄萌萍萎萱落著葛葡董葬葵蒙蒜蒲蒸蓄蓉蓑蓬蔑蔓蔚蔡蔬蔽蕃蕉蕨薄薇薛薪薯藉藏藤藩藻虎虐虔虞虹蚊蚓蚤蛇蛋蛙蛛蛟蛤蛭蛾蜀蜂蜘蜚蜜蝴蝶螂融螺蟹蠢血行衍街衙衡衣表衰衷袁袂袈袋袍袖被裁裂裔裕裙裟裳裴裸褐褥褪褶襄襟西要覃覆角解言詹誓警谷豁豆豚象豪豫豹貂貌赤赦赫走赳赴起超越趣足趾跋跌距跨路跳踏踵蹂蹄蹉蹊蹶躁躇身躬辛辜辣辰辱迂迅迎近返迦迪迫迭述迷追退送逃逅逆逍透逐途逗通逝逞速造逢逮逵逸逼遁遂遇遍遑道遣遭遮遵遽避邂邑那邦邪邱邵邸郁郊郡部郭都鄂鄙酉酊酋酌配酒酩酪酬酵酷酸醇醋醒采釉里重野量金釜閒阜阪阮防阻阿陀附陋降限陛院除陪陵陶隅隆隋隔隘隙障隧雀雁雄雅集雉雌雍雨雪零雷雹需霆震霖霜霞露霹靖非靡面革靴鞋鞍鞠鞭音韶食餐首香馥馨骨骸高鬼魁魂魄魅魏魔鹿麒麓麝麟麻麾黍黎黛鼎鼓鼠鼻'

if __name__ == "__main__":
    readonly__level_char2char_pt_rngs4ver13_0 = load_readonly_level_char2char_pt_rngs_from_compact_result_file__ver('ver13_0')
    readonly__sourceIRG_char2char_pt_rngs4ver13_0 = load_readonly_sourceIRG_char2char_pt_rngs_from_compact_result_file__ver('ver13_0')
    readonly__levelA_common_char_pt_rngs4ver13_0 = load_readonly_levelA_common_char_pt_rngs_from_compact_result_file__ver('ver13_0')
    _sz = readonly__levelA_common_char_pt_rngs4ver13_0.len_ints()
    assert _sz == 2143
    print(f'levelA_common_char_pt_rngs[ver13_0].len_ints() == {_sz}')
    #print(f'levelA_common_char_pt_rngs[ver13_0] == {readonly__levelA_common_char_pt_rngs4ver13_0}')
    _s = ''.join(map(chr, readonly__levelA_common_char_pt_rngs4ver13_0.iter_ints()))
    print(f'levelA_common_hz_str[ver13_0] == {_s!r}')
    assert hz_2143 == _s
if __name__ == "__main__":
    version_strs = findout_available_version_strs()
    if 0b01:print(version_strs)
    if 0b00:assert 'ver13_0' in version_strs


from nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__kIICore8Unihan_IRGSources_txt import findout_available_version_strs, load_readonly_level_char2char_pt_rngs_from_compact_result_file__ver, load_readonly_sourceIRG_char2char_pt_rngs_from_compact_result_file__ver, load_readonly_levelA_common_char_pt_rngs_from_compact_result_file__ver
