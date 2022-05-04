r'''
to load parsed_result of kUnihanCore2020@Unihan_DictionaryLikeData.txt


======================
.readonly__sourceIRG_char2char_pt_rngs
    :: MapView {char:NonTouchRanges}
.readonly__common_char_pt_rngs
    :: NonTouchRanges
    = common_char_pt_rngs

======================
.dataobj
    :: (parsed_result, extra_derived_result)
    mutable
.state
    = compact_result
    mutable

======================
.parsed_result
    :: sourceIRG_char2char_pt_rngs
    mutable
.extra_derived_result
    :: common_char_pt_rngs
    immutable
.compact_result
    ===ver5:
    :: sourceIRG_char2char_pt_rngs__len_rng2begin_chars
        mutable

#ver5 come from:
    view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/parse__kIICore8Unihan_IRGSources_txt.py
======================
.sourceIRG_char2char_pt_rngs
    :: {char:NonTouchRanges}
        mutable
    :: (tmp) {char:StackStyleSimpleIntSet}
        mutable
    ###conceptual:
    :: {char: [(int, int)]}
    :: {char: [(HexReprInt, HexReprInt)]}
.common_char_pt_rngs
    :: NonTouchRanges
        immutable
.sourceIRG_char2char_pt_rngs__len_rng2begin_chars
    #ver5
    :: (literal_store) {char: {len_rng/int: "".join(map(chr,begins))}}
        mutable
    ###conceptual:
    :: {str: [(int, int)]}
======================




======================
e ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/dump_load___parsed_result__of__kUnihanCore20208Unihan_DictionaryLikeData_txt.py
copy from:
    view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/dump_load___parsed_result__of__kIICore8Unihan_IRGSources_txt.py
.+1,$s/kIICore\C/kUnihanCore2020/g
.+1,$s/Unihan_IRGSources\C/Unihan_DictionaryLikeData/g




======================
nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__kUnihanCore20208Unihan_DictionaryLikeData_txt

py -m nn_ns.app.debug_cmd   nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__kUnihanCore20208Unihan_DictionaryLikeData_txt

py -m nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__kUnihanCore20208Unihan_DictionaryLikeData_txt -i /sdcard/0my_files/unzip/e_book/unicode_13__Unihan/Unihan_DictionaryLikeData.txt --donot_output_result5load
py -m nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__kUnihanCore20208Unihan_DictionaryLikeData_txt -i /sdcard/0my_files/unzip/e_book/unicode_13__Unihan/Unihan_DictionaryLikeData.txt --dump ver13_0 --donot_output_result5load

py -m nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__kUnihanCore20208Unihan_DictionaryLikeData_txt --load ver13_0 --donot_output_result5load > /sdcard/0my_files/tmp/_.txt
view /sdcard/0my_files/tmp/_.txt
    get:
        hzs_2573 = common_hz_str@ver13_0



from nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__kUnihanCore20208Unihan_DictionaryLikeData_txt import findout_available_version_strs, load_readonly_sourceIRG_char2char_pt_rngs_from_compact_result_file__ver, load_readonly_common_char_pt_rngs_from_compact_result_file__ver



from nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__kUnihanCore20208Unihan_DictionaryLikeData_txt import cache_view__version_str2readonly_dataobj


from nn_ns.CJK.unicode.ucd_unihan.unihan.parse__kUnihanCore20208Unihan_DictionaryLikeData_txt import parse__kUnihanCore20208Unihan_DictionaryLikeData_txt, helper4parse__Unihan_kUnihanCore20208Unihan_DictionaryLikeData_txt as _helper4parse
######from nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__kUnihanCore20208Unihan_DictionaryLikeData_txt import _cfg, Config4load_compact_result_file4Unihan_kUnihanCore20208Unihan_DictionaryLikeData_txt




======================
view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/parse__kUnihanCore20208Unihan_DictionaryLikeData_txt.py
view /sdcard/0my_files/unzip/e_book/unicode_13__Unihan/Unihan_DictionaryLikeData.txt
# Unihan_DictionaryLikeData.txt
# Date: 2020-02-18 18:27:33 GMT [JHJ]
# Unicode version: 13.0.0

view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/parse__kUnihanCore20208Unihan_DictionaryLikeData_txt.py.out.ver13_0.txt
!du -h ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/parse__kUnihanCore20208Unihan_DictionaryLikeData_txt.py.out.ver13_0.txt
    ver5:84K!!!.to_len_rng2begin_chars
        ...ok?
## !rm ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/unihan/parse__kUnihanCore20208Unihan_DictionaryLikeData_txt.py.out.ver13_0.txt
    after get: hzs_2573



#'''


__all__ = '''
    findout_available_version_strs

    load_readonly_sourceIRG_char2char_pt_rngs_from_compact_result_file__ver
    load_readonly_common_char_pt_rngs_from_compact_result_file__ver

    cache_view__version_str2readonly_dataobj


    '''.split()




___begin_mark_of_excluded_global_names__1___ = ...
from nn_ns.CJK.unicode.ucd_unihan.unihan.parse__kUnihanCore20208Unihan_DictionaryLikeData_txt import parse__kUnihanCore20208Unihan_DictionaryLikeData_txt, helper4parse__Unihan_kUnihanCore20208Unihan_DictionaryLikeData_txt as _helper4parse

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
    ,basename_fmt       ='parse__kUnihanCore20208Unihan_DictionaryLikeData_txt.py.out.{}.txt'
    ,version_str__rex   =r'^ver[0-9]+_[0-9]+$'
    ,encoding           ='utf8'
    )

#]]]







def load_readonly_sourceIRG_char2char_pt_rngs_from_compact_result_file__ver(version_str, /, *, may_path_bypass_version_str=None):
    'version_str -> readonly__sourceIRG_char2char_pt_rngs'
    readonly__dataobj = _load_readonly_dataobj_from_compact_result_file__ver(_cfg, version_str, may_path_bypass_version_str=may_path_bypass_version_str)
    (readonly__parsed_result, readonly__extra_derived_result) = readonly__dataobj

    readonly__sourceIRG_char2char_pt_rngs = readonly__parsed_result

    return readonly__sourceIRG_char2char_pt_rngs

def load_readonly_common_char_pt_rngs_from_compact_result_file__ver(version_str, /, *, may_path_bypass_version_str=None):
    'version_str -> readonly__common_char_pt_rngs'
    readonly__dataobj = _load_readonly_dataobj_from_compact_result_file__ver(_cfg, version_str, may_path_bypass_version_str=may_path_bypass_version_str)
    (readonly__parsed_result, readonly__extra_derived_result) = readonly__dataobj

    readonly__common_char_pt_rngs = readonly__extra_derived_result

    return readonly__common_char_pt_rngs









main = _mainT(
    description
    ='parse,dump,load kUnihanCore2020@Unihan_DictionaryLikeData.txt#ETL tool (extract, transform, load)'
    ,epilog
    =''
    ,parse__xxx_txt__lines
    =parse__kUnihanCore20208Unihan_DictionaryLikeData_txt
    ,cfg4load_compact_result_file4xxx_txt
    =_cfg
    ,parsed_result2dataobj
    =_helper4parse.parsed_result2dataobj
    ,args4repr
    =[]
    ,kwargs4repr
    ={}
    ,args4dump
    =[]
    ,kwargs4dump
    ={}
    )
if __name__ == "__main__":
    main()



findout_available_version_strs = _cfg.findout_available_version_strs

cache_view__version_str2readonly_dataobj = _cfg.get_view_of_cache__version_str2readonly_dataobj()


hzs_2573 = common_hz_str__Unihan_ver13_0 = \
    '一丁七万丈三上下不丑且丕世丘丙丞中串丸丹主乂乃久之乍乎乏乖乘乙九乞也乳乾了予事二于云互五井些亡亢交亥亦亨享京亭亮亶人什仁仄仇今介仍仔仕他仗付仙仝仟代令以仰仲件价任企伉伊伍伎伏伐休伯伴伶伸伺似伽佃但位低住佐佑何余佚佛作佩佯佰佳佶使侃侈例侍侏侑侘供依侮侯侵便促俄俊俎俑俗俚保俟信修俯俱俳俵俸俺倍倒候倚借倡倦倨倪倬倭偃假偈偏偕做停健偶傀傅傍催傲像僖僚僧僭僻儒儡兀允元兄充兆先光克免兜兢入全八公六兮共兵其具典兼冀再冒冕冗冠冥冬冶冷冽凄准凋凌凝凡凰凶凸凹出函刀刃分切刈刊刎刑列初判利刮到制刷券刺刻剃削剋剌前剔剖剩剪副割剽剿劈力功加劣助努劫劾勃勇勉勍勒勘募勤勺勾勿包匈匍匏匐匕化北匙匠匡匣匪匹匿十千升午卉半卑卒卓南博卜卞占卦卯印危卵卷卿厄厘厚原厥去又叉及友反叔取受叛口古句叩只叫召叭可台叱史右司吃各合吉吊同名后吏吐向君吝吟吠否吩含吸吹吻吼吾呈告周呱味呵呻呼命咀咆和咎咐咨咫咬咳咸咽哀品哄哈哉哥哨哭哮哲哺唆唇唐唯唱唾啄商啖啼喀善喇喉喊喘喙喜喝喧嗅嗔嗜嗟嗣嗤嗽嗾嘉嘲嘴嘶器噫嚆嚼囊囚四回因困囹固圃圄圈土在圭地圻址均坊坎坐坑坡坤坦坪垂型垓垠垢垣埃埋城域埠埴培基埼堀堂堆堡堤堪堰堵塑塔塘塞塾境墅墓增墟墨壁壅壑壕壤士壬壹夏夕外夙多夜大天太夫夭央失夷奄奇奈奉奎奏契奔奕套奚奠奢女奴奸好如妃妄妊妓妖妙妥妨妹妻妾姆始姐姑姓委姚姜姨姻姿威娃娑娘娜娟娠娥娩娶娼婆婉婚婢媒媚媛嫁嫂嫉嫌嫡嫦嫩嬉嬖孀子孑孔孕字存孚孜孝孟季孤孩孰孱孵孺宅宇守安宋完宏宕宗官宙定宛宜客宣室宥宦宰害宴宵家宸容宿寂寄寅密寇富寐寒寓寞察寡寤寨寮寸寺封射尉尊小少尖尤尨就尸尹尺尻尼尾尿局居屈屋屎屑展屠履屯山屹岐岑岩岫岬岱岳岷岸峙峨峰峻崇崎崔崖崩嵋嵌嵩嵬嵯嶝巍川州巡巢工左巧巨巫差己已巳巴巷巽巾市布帆希帑帖帙帛帝席常帽幄幅幌幕幡幢干平年幸幻幼幽庄庇床序底店庚府庠度座庭庵庶康庸廉廊廓廖廛延廷建弁弄弊式弓引弗弘弛弟弦弧弩弱弼彖彗形彩彪彬彭彰影彷役彼往征待徇徊律後徐徒得徘徙御徨循微徵德徽心必忌忍忖志忘忙忠快念忽忿怏怒怖怜思怠怡急性怨怪怯恁恂恃恍恐恕恙恢恣恤恨恩恪恬恭息恰悉悌悍悔悖悚悛悟悠患悲悴悸悼情惇惑惚惜惟惠惰想惶惹惺愁愆愈愉愍愎意愕愚感愧愿慈慊慌慕慝慢慧慨慰慷憎憔憧憩憬憺憾懈懊懋懦懿戈戊戌戍戎成我戒或戚戟戡截戮戴房所扁扇扈扉手才打托扮扶批扼承技抄抉把抑抒投抗折披抱抵抹押抽拂拇拈拉拌拍拐拒拓拔拗拘拙招拜括拭拮拯拱拳拷拾拿持指按挑挫振挺挽捉捌捏捐捕捧据捷捺捻授掉掌排掖掘掠探接控推掩措揄揆描提揖握揭援揶搏搔搜搬搭摘摩摸摺撒撞撤播撮撰擅操擒擘擢擦攀攘攫支收攸改攻放政故效敏救敖敞敢散敦敬敲整敷文斌斐斑斗料斛斜斟斡斤斥斧斫斯新方於施旁旅旋旌族旒旗日旦旨早旬旭旱旺旻昆昇昊昌明昏易昔星映春昧昨昭是昴昶晁晃晏晞晟晤晦晨普景晴晶智暄暇暑暖暗暝暮暴暹暾曙曜曝曦曰曲曳更曷曹曼曾替最月有朋服朔朕朗望朝期朦木未末本札朱朴机朽杆杉李杏材村杓杖杜杞束杭杯杰杳杵杷松板枇枉枋析枕林枚果枝枯枳架枷枸柄柏某柑染柔柚柝柩柬柯柱柳柴栓栖栗校株核根格栽桀桁桂桃案桎桐桑桓桔桶梁梅梏梓梗梢梧梨梭梯械梳梵棉棋棍棒棕棘棚棠森棹棺椅植椎椒椰椽椿楔楙楚楞楠楫楮楯楷楸楹榕榛榜榧榴榻槁槃槌槐槽槿樊樗樟模樵樽橄橘橙橡檀檄檎檗欠次欣欲欺款歇歌止正此步武歪死殃殄殆殉殊殖段殷殿毅毋母每毒毓比毛毫氏民氓水永氾汀汁求汐汕汗汝汞江池汨汪汰汲汽汾沁沂沃沈沌沐沓沙沚沛沫沮河沸油治沼沽沾沿泄泉泊泌泓法泗泛泡波泣泥注泯泰泳洋洌洗洙洛洞津洪洲洵洸活洽派流浙浚浣浦浩浪浬浮浴海浸涅消涉涌涎涓涕涯液涵淀淅淆淇淋淑淘淙淞淡淫淮深淳混淹添渚渟渠渡渣渤渥渫渭港渴游渺湃湍湖湘湛湟湫湮湲源溜溟溢溥溪溯溶溺滂滉滋滑滓滔滴漂漆漏演漕漠漫漱潘潟潭潮潺潼澄澎澳澹激濂濠濡濯瀑瀚瀛灌火灰灸灼炊炎炒炙炬炭炯炳炸烈烙烝烹烽焉焙焚焦焰然煌煎煤煦照煮煽熄熊熏熔熙熟熬熹燃燎燔燕燥燧燮爆爪爬爰爵父爻爽片版牌牒牙牛牝牟牡牢牧物牲特犀犁犬犯狂狄狎狐狗狙狡狩狸狼猊猖猛猜猝猥猩猷猾猿獗玄率玉王玖玩玲玳珀珂珊珍珞珠珥珪班球琅理琉琢琥琳琴琵琶瑁瑕瑙瑚瑛瑜瑞瑟瑾璃璋璞璧瓜瓠瓢瓣瓦瓮瓷甄甑甘甚生甥甦用甫甬田由甲申男甸町界畏畔留畛畜略畦番畸畿疆疋疏疑疝疥疫疲疳疵疸疹疼疽疾痂病症痍痒痔痕痘痛痢痰痴痼瘟瘠瘢瘤瘦癌癖癸登白百的皆皇皎皓皮皿盂盆盈益盒盛盟目盲直相盾省眄眈眉看眠眩眷眸眺眼睛睡督睦睫睹睾睿瞋瞑瞥瞬瞭瞰瞳瞻瞿矗矛矜矢矣知矩短矮石砂砒砥砦砧破硅硝硫硬硼碇碌碎碑碗碣碧磁磅磊磋磐磨磬礁示社祀祁祇祈祉祐祖祗祚祝神祠祥票祭祺禁福禧禳禹禽禾秀私秉秋科秒秕秘租秤秦秧秩移稀程稍稔稗稙稚稠稷稻稼稽稿穆穗穰穴究穹空穿突窄窈窒窕窘窟立站竟章竣童竭端竹竺竿笏笑笙笛笞笠符第等筋筌筏筐筑筒答策筮筵箔箕算箝管箭箱箴箸篁篆篇簇簧簪簿籍米粉粒粕粗粘粟粥粱粲粳粹精糊糖糟糠系紊素索紫累絮繁纂纛缶缸缺罐罔罕罪置署罹羊羌美羔羚羞群羲羸羹羽翁翅翊翌翔翕翠翡翩翰翼耀老考者耆而耐耕耗耘耳耶耽耿聆聊聘聚聿肄肆肇肉肋肌肖肛肝股肢肥肩肪肯肱育肴肺胃胄背胎胚胛胞胡胤胥胱胴胸能脂脆脊脩脯脾腋腐腑腔腕腥腰腱腹腺腿膀膈膊膏膜膝膣膨膳膺臀臂臆臣臧自臭至致臻臼臾舅舌舍舒舛舜舞舟航舫般舵舶舷船艇艮良色艾芋芍芒芙芝芟芥芬芭芯花芳芸芹芽苑苒苔苗苛苞苟苡若苦苧英茂范茄茅茉茗茨茫茯茱茴茵茶茸茹荀草荏荒荷荻莉莎莞莪莫莽菁菅菊菌菖菜菩菰菱菲菽萃萄萌萍萎萩萱萸落著葛葡董葫葬葵葺蒐蒙蒜蒡蒲蒸蒻蒿蓄蓉蓍蓑蓬蓼蔑蔓蔗蔚蔡蔬蔽蕃蕉蕨薄薇薛薨薪薯薰藉藏藕藜藤藩藻虎虐虔虞虹蚊蚌蚓蚣蚤蚩蛇蛋蛔蛙蛛蛟蛤蛭蛾蜀蜂蜃蜈蜘蜚蜜蝎蝗蝴蝶螂融螟螳螺蟠蟹蟾蠢血行衍衒街衙衡衢衣表衫衰衲衷衾衿袁袂袈袋袍袒袖袗被裁裂裔裕裙裟裨裳裴裸褐褒褓褥褪褶襁襄襟西要覃覆角解言誓警譬谷谿豁豆豌豕豚象豪豫豹豺貂貊貌赤赦赫走赳赴起超越趣足趺趾跋跌跏跛距跣跨路跳踊踏踞踵蹂蹄蹇蹈蹉蹊蹙蹴蹶躁躇身躬辛辜辣辨辰辱迂迅迎近返迦迪迫迭述迷追退送逃逅逆逋逍透逐逑途逗通逝逞速造逡逢逮逵逸逼逾遁遂遇遍遐遑道遣遭遮遵遽避邀邂邃邑那邦邪邯邱邵邸郁郊郡部郭都鄂鄙酉酊酋酌配酎酒酢酩酪酬酵酷酸醇醉醋醍醒醯醴醵采釉里重野量釐金釜阜阡阪阮防阻阿陀陂附陋陌降限陛陞陟院除陪陵陶陷隅隆隋隍隔隘隙障隧雀雁雄雅集雇雉雌雍雎雕雨雪零雷雹需霆震霓霖霜霞霰露霹靖非靡面革靴靺鞋鞍鞠鞨鞫鞭音韶食餐首香馥馨骨骸髓高鬼魁魂魃魄魅魏魔鹿麒麓麝麟麴麻麾黍黎黑黔默黛黜鼎鼓鼠鼻'



if __name__ == "__main__":
    readonly__sourceIRG_char2char_pt_rngs4ver13_0 = load_readonly_sourceIRG_char2char_pt_rngs_from_compact_result_file__ver('ver13_0')
    readonly__common_char_pt_rngs4ver13_0 = load_readonly_common_char_pt_rngs_from_compact_result_file__ver('ver13_0')
    _sz = readonly__common_char_pt_rngs4ver13_0.len_ints()
    assert _sz == 2573
    print(f'common_char_pt_rngs[ver13_0].len_ints() == {_sz}')
    print(f'common_char_pt_rngs[ver13_0] == {readonly__common_char_pt_rngs4ver13_0}')
    _s = ''.join(map(chr, readonly__common_char_pt_rngs4ver13_0.iter_ints()))
    print(f'common_hz_str[ver13_0] == {_s!r}')
    assert hzs_2573 == _s
if __name__ == "__main__":
    version_strs = findout_available_version_strs()
    if 0b01:print(version_strs)
    if 0b00:assert 'ver13_0' in version_strs


from nn_ns.CJK.unicode.ucd_unihan.unihan.dump_load___parsed_result__of__kUnihanCore20208Unihan_DictionaryLikeData_txt import findout_available_version_strs, load_readonly_sourceIRG_char2char_pt_rngs_from_compact_result_file__ver, load_readonly_common_char_pt_rngs_from_compact_result_file__ver
