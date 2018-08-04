# -*- coding: gb2312 -*-

from pprint import pprint
from all_chars_has_multiST_variants_obj import all_chars_has_multiST_variants
from common_CJK_chars_exclude_nonHanzi import common_CJK_chars_exclude_nonHanzi

def _make():
    s = set(common_CJK_chars_exclude_nonHanzi) - set(all_chars_has_multiST_variants)
    return ''.join(sorted(s))

if 0:
    common_CJK_han_chars_exclude_multiST = _make()
    print(len(common_CJK_han_chars_exclude_multiST))
    print(common_CJK_han_chars_exclude_multiST)
L = 2340
common_CJK_han_chars_exclude_multiST = \
    '一丁七丈三上下不且丕世丘丙丞中串丸丹主久之乍乎乏乖乘乙九乞也乳予事二互五井些亡亢交亥亦亨享京亭亮人什仁仄今介仍仔仕仗付仙仝仟代令以仰仲件任企伉伊伍伎伏伐休伯伴伶伸伺似伽佃但位低住佐佑何佚佛作佩佯佰佳佶使侃侈例侍侏侑供依侮侯侵便促俄俊俎俑俗俚保俟信修俯俳俸俺倍倒候倚倡倦倨倪倬倭偃假偈偏偕做停健偶傀傅傍催傲僖僚僧僭僻儒儡兀允元兄充兆先光免兜兢入全八公六兮共兵其具典兼冀再冒冕冗冠冥冶冷冽凋凝凡凰凸凹函刀刃分切刈刊刎刑列初判利到刷券刺刻削剌前剔剖剪副割剽剿劈力功加劣努劫劾勃勇勉勒勘募勺勾勿包匈匍匏匐匕化北匙匠匣匪匹匿十午卉半卑卒卓南博卞卦卯印危卵卿厄厚原厥去又叉及友反叔取受叛口古句叩叫召叭可叱史右司各吉名吏吐君吝吟吠否吩含吸吹吻吼吾呈告呱味呵呻命咀咆和咎咐咨咫咬咳哀品哈哉哥哨哭哮哲哺唆唐唯唱唾啄商啼喀善喇喉喊喘喙喜喝嗅嗔嗜嗟嗣嗤嗽嗾嘉嘲嘴嘶器噫嚆嚼囚四因囹固圃圄圈土在地圻址均坊坎坐坑坡坤坦坪垂型垓垠垢垣埃埋城域埠埴培基堀堂堆堡堤堪堰堵塑塔塘塞塾境墅墓墟墨壁壅壑壕壤士壬壹夏夕外夙多夜大天太央失夷奄奇奈奉奎奏契奔奕套奚奠奢女奴好如妃妄妊妓妖妙妥妨妹妻妾姆始姐姑姓委姚姨姻姿威娃娑娜娟娠娥娩娶娼婆婉婚婢媒媚媛嫁嫂嫉嫌嫡嫦嫩嬉嬖孀子孑孔孕字存孚孜孝孟季孤孩孰孱孵孺宅宇守安宋完宏宕宗官宙定宛宜客宣室宥宦宰害宵宸容宿寂寄寅密寇富寐寒寓寞察寡寤寥寨寮寺封射尉尊小少尖尤就尹尻尼尾尿居屈屋屎屑展屠履屯山屹岐岑岫岬岱岷岸峙峨峰峻崇崔崖崩嵋嵌嵩嵬嵯嶝巍川州巡工左巧巨巫差己已巳巴巷巽巾市帆希帑帖帙帛帝常帽幄幅幌幕平年幻幼幽庇序底店庚府庠度座庭庶康庸廉廊廓廖廛延廷建弁弄弊式弓引弗弘弛弟弧弩弱弼彖形彪彬彭彰影彷役彼往待徇徊律徐徒得徘徙徨循微徽心必忌忍忖忘忙忠快忽忿怏怒怖思怠怡急性怨怪怯恁恂恃恍恐恕恙恢恣恤恨恩恪恬恭息恰悉悌悍悔悖悚悛悟悠患悲悴悸悼情惑惚惜惟惠惰想惶惹惺愁愆愉愍愎意愕愚感慈慊慌慕慝慢慧慨慰慷憎憔憧憩憬憾懈懊懋懦懿戈戊戌戍戎成我戒或戟戡截戮戴房所扁扇扈扉手打扮扶批扼承技抄抉把抑抒投抗披抱抹押抽拂拇拉拌拍拐拒拓拔拗拘拙招拜括拭拮拯拱拳拷拾拿持指按挑挫振挺捉捌捏捐捕捧捷捺捻授掉掌排掖掘掠探接控推掩措揄揆描提揖握援揶搏搬搭摘摩摸撒撞撤播撮撰擅操擒擘擢擦攀攘攫支收攸改攻放政故敏救敖敞敢散敦敬敲整敷文斌斐斑料斛斜斟斡斤斥斧斫斯新方施旁旅旌族旒旗日旦旨早旬旭旱旺昊昌明昏易昔星映春昧昨昭是昴昶晁晃晏晟晤晦晨普景晴晶智暄暇暑暖暝暮暴暹暾曙曜曝曦曰曳更曷曹曼曾替最月有朋服朔朕朗望朝期朦木未末本机朽杆杉李杏材杓杖杜杞束杭杳杵杷枇枉枋析枕林枚果枝枯枳架枷枸柄柏某柑染柔柚柝柩柬柯柱柳柴栓校株根格栽桀桁桂桃案桎桐桑桓桔桶梅梏梓梗梢梧梨梭梯械梳梵棉棋棍棒棕棘棚棠森棺椅植椎椒椰椽椿楔楚楞楠楫楮楷楸楹榕榛榜榧榴榻槁槌槐槽槿樊樗樟模樵樽橄橘橙橡檀檄檎檗欠次欣欺款歇歌止正此武歪死殃殄殆殉殊殖段殿毅母毒毓比毛毫氏民氓水永汀汁求汐汕汗汝汞江池汨汪汰汲汽汾沁沂沃沌沐沓沙沛沫沮河沸油治沼沽沾沿泉泊泌泓法泗泡波泣泥泯泰泳洋洌洗洙洛洞津洪洲洵活洽派流浙浚浣浦浪浮浴海浸涅消涎涓涕涯液涵淅淆淇淋淑淘淙淞淡淫淮深淳混淹添渚渠渡渣渤渥渫渭港渺湃湍湖湘湛湟湫湮源溜溟溢溥溯溶溺滂滋滑滓滔滴漂漆漏漕漠漫漱潘潭潮潺潼澄澎澳澹激濂濠濡濯瀑瀚瀛灌火灰灸灼炊炎炒炙炬炭炯炳炸烈烙烹烽焉焙焚焦然煌煎煤煦照煮煽熄熊熔熙熟熬熹燃燎燔燕燥燧燮爆爪爬爰爵父爻爽片版牌牒牙牛牝牟牡牢牧物牲特犀犁犬犯狂狄狎狐狗狙狡狩狸狼猊猖猛猜猝猥猩猷猾猿獗玄率玉王玖玩玲玳珀珂珊珍珞珠珥班球理琉琢琥琳琴琵琶瑁瑕瑙瑚瑛瑜瑞瑟瑾璃璋璞璧瓜瓠瓢瓣瓦瓮瓷甄甑甘甚生甥用甫甬田由甲申男甸町界畏畔留畛畜略畦番畸畿疆疋疏疑疝疥疫疲疳疵疸疹疼疽疾痂病痍痒痔痕痘痛痢痰痼瘟瘠瘢瘤癌癖癸登白百的皆皇皎皓皮皿盂盆盈益盒盛盟目盲直相盾省眄眈眉看眠眩眷眸眺眼睛睡督睦睫睹睾睿瞑瞥瞬瞰瞳瞻瞿矗矛矜矢矣知矩短矮石砂砒砥砦砧破硝硫硬硼碇碌碎碑碗碣碧磁磅磊磋磐磨磬礁示社祀祁祈祉祖祗祚祝神祠祥票祭祺禁福禧禳禹禽禾秀私秉科秒秕租秤秦秧秩移稀程稍稔稗稚稠稷稻稼稽稿穆穗穰穴究穹空穿突窄窈窒窕窘窟立站竟章竣童竭端竹竺竿笏笑笙笛笞笠符第等筋筌筏筐筒策筮筵箔箕算箝管箭箱箴箸篁篆篇簇簧簪簿籍米粉粒粕粘粟粥粱粲粳粹精糊糖糠紊素索紫絮繁纂纛缶缸缺罔罕罪置署罹羊羌美羔羚羞群羲羸羹羽翁翅翊翌翔翕翠翡翩翰翼耀老考者耆而耐耕耗耘耳耶耽耿聆聊聘聚聿肄肆肇肉肋肌肖肛肝股肢肥肩肪肯肱育肺胃胄胎胚胛胞胤胥胱胴胸能脂脆脊脯脾腋腐腑腔腕腥腰腱腹腺腿膀膈膊膏膜膝膣膨膳膺臀臂臆臣臧自臭至臻臼臾舅舌舒舛舜舞舟航舫般舵舶舷船艇艮良色艾芋芍芒芙芝芟芥芬芭芯花芳芹芽苑苒苔苗苛苞苟苡若苦英茂茄茅茉茗茨茫茯茱茴茵茶茸茹荀草荏荒荷荻莉莎莞莪莫莽菁菅菊菌菖菜菩菰菱菲菽萃萄萌萍萎萱萸落葛葡董葫葬葵葺蒜蒡蒲蒸蒿蓄蓉蓍蓬蓼蔓蔗蔚蔡蔬蔽蕃蕉蕨薄薇薛薨薪薯藏藕藜藩藻虎虐虔虞虹蚊蚌蚓蚣蚤蚩蛇蛋蛔蛙蛛蛟蛤蛭蛾蜀蜂蜃蜈蜘蜚蜜蝗蝴蝶螂融螟螳螺蟠蟹蟾蠢血行衍街衙衡衢衣衫衰衲衷衾衿袁袂袈袋袍袒袖被裁裂裔裕裙裟裨裳裴裸褐褒褓褥褪褶襁襄襟西要覃角解言誓警譬豁豆豌豕豚豪豫豹豺貂貊貌赤赦赫走赳赴起超越趣足趺趾跋跌跏跛距跣跨路跳踏踞踵蹂蹄蹇蹈蹉蹊蹙蹴蹶躁躇身躬辛辜辣辨辰辱迂迅迎近返迦迪迫迭述迷追退送逃逅逆逋逍透逐逑途逗通逝逞速造逡逢逮逵逸逼遁遂遇遍遐遑道遣遭遮遵遽避邀邂邃邑那邦邪邯邱邵邸郊郡部郭都鄂鄙酉酊酋酌配酎酒酢酩酪酵酷醇醉醋醍醒醯醴醵釉重野量金釜阜阡阪阮防阻阿陀陂附陋陌降限陛陟院除陪陵陶陷隅隆隋隍隔隘隙障隧雀雁雄雅集雉雌雍雎雨雪零雷雹需霆震霓霖霜霞霰露霹靖非靡革靴鞋鞍鞠鞫鞭音韶食餐首香馥馨骨骸髓高鬼魁魂魃魄魅魏魔鹿麒麓麝麟麾黍黎黔默黛黜鼎鼓鼠鼻'
assert len(common_CJK_han_chars_exclude_multiST) == L
if __name__ == '__main__':
    print(len(common_CJK_han_chars_exclude_multiST))

