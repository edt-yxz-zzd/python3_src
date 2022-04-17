#__all__#goto
r'''[[[[[[[
nn_ns.CJK.CJK_data.raw.用汉字编码数据.高稳定度汉字字集
py -m nn_ns.CJK.CJK_data.raw.用汉字编码数据.高稳定度汉字字集
from nn_ns.CJK.CJK_data.raw.用汉字编码数据.高稳定度汉字字集 import 高稳定度汉字字集囗第三版囗码序囗二百六十一字, 高稳定度汉字字集囗第二版囗降频囗无病字框囗二百五十九字
e ../../python3_src/nn_ns/CJK/CJK_data/raw/用汉字编码数据/高稳定度汉字字集.py


===输出
[[第三版 2个主要输出对象的解释:

* 高稳定度汉字字集囗第三版囗码序囗二百六十一字 = hzs_261
    see:
        hzs_261__definition
        hzs_261__content
        def _mk_261():

* 用统一码十三版数据复刻并兼容初版高稳定度汉字字集囗无病字框囗码序囗三百二十二字 = hzs_334_excludeILL_322
    see:
        hzs_334_excludeILL_322__definition
]]
[[第二版 2/3个主要输出对象的解释:

* 高稳定度汉字字集囗第二版囗...
    * 高稳定度汉字字集囗第二版囗降频囗无病字框囗二百五十九字 = hzs_excludeILL_259
            #可用『爻勺竺』作为括号或转义符与分隔符(空格符/逗号)
    # * xxx 高稳定度汉字字集囗第二版囗降频囗含病字框囗二百五十七字 = hzs_includeILL_257

    see:
        xxx hzs_includeILL_257__definition
        xxx hzs_includeILL_257__content
        hzs_excludeILL_259__definition
        hzs_excludeILL_259__content
        def _mk_257_259():

* 用统一码十三版数据复刻并兼容初版高稳定度汉字字集囗码序囗三百三十四字 = hzs_334
    see:
        hzs_334__definition
        hzs_334__content
        def _试着复刻第一版_但UV版本不同():

]]


===输入
[[第三版 2022年4月 使用unicode13的数据
兼容 第一版342
兼容 第一版复刻版334
但 不兼容 第二版259
    [[为什么又有第三版？
        再次 收集 敏感词
    ]]

第三版 新数据:
!du -h ../../python3_src/raw_data/20220415敏感词.7z
    288K
!cp /storage/emulated/0/Download/20220415敏感词/parse_banned_words.py.字汇.out.txt   ../../python3_src/nn_ns/CJK/CJK_data/raw/用汉字编码数据/第三版数据.20220415敏感词.字汇.3773.parse_banned_words.py.字汇.out.u8

]]
[[第二版 2022年4月 使用unicode13的数据
兼容 第一版342
    [[为什么又有第二版？
        后来才发现 第一版 包含『巳』，可见之前搜集到的形近字很不完整。
        以 第一版 为底本，进行删减。
        * 生僻字也无妨，但笔画不要太多
        * 字集 内部 不要含 形近字，或 大偏旁一样的字；外部 不要有 形近的常用字
        * 『病字框』看起来像广告，也去掉。
        * 保留 257 字以上，以方便转义提供带外信息。
    ]]
]]
[[第一版 不知何年何月，使用unicode9数据
重要历史性数据:chars_in_banned_words
    敏感词的字汇
    !cp ../../python3_src/script/char/common_CJK/chars_in_banned_words.u8   ../../python3_src/nn_ns/CJK/CJK_data/raw/用汉字编码数据/第一版数据.敏感词.字汇.4924.chars_in_banned_words.u8
    ===
    # data collected from 敏感词库 by collect_chars.py
]][[
重要历史性数据:all_similar_chars
view ../../python3_src/script/char/common_CJK/all_similar_chars.u8
    形近字
    !cp ../../python3_src/script/char/common_CJK/all_similar_chars.u8   ../../python3_src/nn_ns/CJK/CJK_data/raw/用汉字编码数据/第一版数据.形近字.字汇.593.all_similar_chars.u8
    ===
    view ../../python3_src/script/char/common_CJK/similar-chars-html.txt
    http://kanji-database.sourceforge.net/variants/similar-chars.html
    ＵＣＳ類似漢字一覧表
    ===
    含:干千，天夭，奸奷，妲姐
    不含:未末，妹妺，旦且
]]

[[[
用于编码二进制数据的高稳定度汉字字集
用汉字编码数据.高稳定度汉字字集
可用于类似『佛曰/与佛论禅』的项目。

===
#高稳定度汉字字集
    用于编码数据，要求:
        + 能被任何汉字编码方案所支持，不被自动替换成缺省字符
        + 任意组合不产生敏感词(日期)，不被屏蔽
        + 繁简唯一可逆(繁简择一)或平凡自反(同时繁简)，不被自动窜改
        + 无变体字(异体字、形近字、同义字、繁简字)，确保人工抄录误码率低
        + 若有可能，再除去 罕见字(罕用字/生僻字)/古今字/通假字/多音字/兼容字(即：是某个unicode字符正态规范分解后的原字)。
收集 形近字/易错字/错别字/混淆字 大全
收集 敏感词/屏蔽词 大全


===
稳定的汉字字集 要求:[[
不被屏蔽，不含 敏感词:
  日期：八九六四
    ==>> 除去 数字
  任意组合：水乳交融
    ==>> 除去 任何能组成 敏感词的字
不被 自动转换：
  #如同其他一切数据：词句/数值/网址/...，任何重要文本 可能出现在任何网页上，被人读写，应当避免常见的可能错误。
  百度百科 将 繁体字 自动替换为 简体字
    ==>> 除去 繁简字不能一一对应的汉字
    ==>> 更进一步 除去 繁简字非平凡(即：非自反)的汉字
  人眼识别，手动抄录：
    ==>> 除去 形近字+异体字+同义字 等等 任何 变体 Unihan_Variants.txt
]]
[[
view ../../python3_src/script/char/common_CJK/[common_CJK]ReadMe.txt
  86 矣郡惟淮荷哉嗣撰巳朕癸亥椅衙旱俺簿旬癌蕃猩塘擢薨懿裳脊稷葡憾蝗梗萄揖晏棠喀梢藩暑膊胤株筵棚沼弧敞榻殆鄂沮璋敖邸嗟膨黜悖逵漕攸蔬蛟嵌俸瘢嗜哺蕉杉侈梭麾胥汾掖琢戟甥荀斛耆隅茵檄
  256 竺笙翊釉宸潼徇礁僖臾泗瑾羲渥拷壕脯壑瑛孺熄瑚琶斡渤爰甄恁苔芍嗔偈褥痰裨舷磐勺簪蟠橡嫦逋珀佃夙濠肪枷剔薇椿蹙茄涓溥衢茸翌窒穹蛾卞衾陟琵菁雉猝曙酵邯懋眸曷瀑焙悸蛭珂揆瑁喙陂淙舫斫麝燮桔愆庠跛黍佚癖蹇曦湍蒜磬珥橙娑怏暹瓢逡嵋跏燧昴疵爻麒橄寤幄胛淞滓狎窈湫帑芹拌荻嬖盂碇燔倨皿瘠蚌祉淅洵楹秧咫筮蚣瞑攫悌跣趺褶灸樟魃倬翡傀殄岬菽俳槁蒿羸侏裟暝袈痘俑稔畛粕翕濂甑蜈葺柑楔椽匐樗嵬溟噫蔗琥匍碣嗾纛禳醵艮戡萸瓠雎槿侑枋肄暾慝梏楮檎汐豌蕨逑桎枳楸慊螟佶畦稗酊圄菖揄孱疥蓍蹉痍枸枇茯廛猊酩荏擘苒眄茱痂篁腱膈筌埴醍柝酎莪疝茴堀檗疳蒡嚆
===
total chars:
    total_gb2312_chars = 7573
    total_common_CJK_chars = 3065
    total_common_CJK_chars_exclude_nonHanzi = 2513
    total_common_CJK_han_chars_exclude_multiST = 2340
    total_common_CJK_uniqueST_han_chars_exclude_similars = 2259
    total_common_CJK_noSimilar_han_chars_exclude_vary_chars = 1520
    total_common_CJK_noSimilar_han_chars_exclude_all_chars_with_variant = 1518
    total_common_CJK_noVariant_han_chars_exclude_banned = 342
    total_common_CJK_nonBanned_han_chars_exclude_numeric = 342
]]

!mkdir   ../../python3_src/nn_ns/CJK/CJK_data/raw/用汉字编码数据/
e ../../python3_src/nn_ns/CJK/CJK_data/raw/用汉字编码数据/高稳定度汉字字集.py


[[重要数据: from ../../python3_src/script/char/common_CJK/
all_chars_has_multiST_variants_obj.py
all_numeric_han_chars.py
all_numeric_han_chars.u8
  73
all_similar_chars.py
all_similar_chars.u8
  593
chars_in_banned_words.py
chars_in_banned_words.u8
vary_charss.py
vary_charss.py.obj
  (chars_with_multi_ST, vary_chars, all_chars_with_variant)
    只使用了:'Unihan_Variants_9_0.txt'
        并不重要
]]
[[
vary_char? 怎么来的？
cd $my_git_py
grep 'vary_char\|古今\|通假' -r . -l
view ../../python3_src/script/char/unicode_database/vary_charss.py.obj.txt
view ../../python3_src/script/char/common_CJK/vary_charss.py
grep 'vary_char' -r . -l
view ../../python3_src/script/char/unicode_database/unihan_variants2dict.py
    def _calc_charss():
    vary_chars = chars_with_multi_ST + all_chars_exclude_ST
    即：Unihan_Variants.txt中 有 多个简体字的、多个繁体字的、(但！缺失:同时 有 繁体字、简体字！)、有至少一个不考虑繁简的其他变体类型的 汉字。
    用的是:'Unihan_Variants_9_0.txt'
        kSemanticVariant
        kSimplifiedVariant
        kSpecializedSemanticVariant
        kTraditionalVariant
        kZVariant
        ===
        变体种类 比 ver13_0 少！



]]






$ cd ../../python3_src/script/char/common_CJK/
$ ls
[[
Bijection.py
'CJK main encodings.txt'
TODO.txt
'[common_CJK]ReadMe.txt'
'[common_CJK]encode.txt'
all_chars_has_multiST_variants_obj.py
all_numeric_han_chars.py
all_numeric_han_chars.u8
all_similar_chars.py
all_similar_chars.u8
chars_in_banned_words.py
chars_in_banned_words.u8
common_CJK_chars.py
common_CJK_chars_exclude_nonHanzi.py
common_CJK_han_chars_exclude_multiST.py
common_CJK_noSimilar_han_chars_exclude_vary_chars.gb
common_CJK_noSimilar_han_chars_exclude_vary_chars.py
common_CJK_noVariant_han_chars_exclude_banned.gb
common_CJK_noVariant_han_chars_exclude_banned.py
common_CJK_nonBanned_han_chars_exclude_numeric.py
common_CJK_ranges.py
common_CJK_uniqueST_han_chars_exclude_similars.py
common_CJK_uniqueST_han_chars_exclude_similars.u8
encoding2ranges.py
exclude_chars.py
freq_sorted_nonBanned_nonNum_han_chars.gb
gb2312_ranges.py
han_chars_sorted_by_frequency.py
han_chars_sorted_by_frequency.u8
similar-chars-html.txt
sorted_chars.txt
std_chars.py
unique_and_sorted_by_frequency.py
vary_charss.py
vary_charss.py.obj
现代汉语常用字表.u8
]]

]]]
#]]]]]]]'''



__all__ = '''
高稳定度汉字字集囗第三版囗码序囗二百六十一字
    hzs_261
高稳定度汉字字集囗第二版囗降频囗无病字框囗二百五十九字
    hzs_excludeILL_259
用统一码十三版数据复刻并兼容初版高稳定度汉字字集囗无病字框囗码序囗三百二十二字
    hzs_334_excludeILL_322
用统一码十三版数据复刻并兼容初版高稳定度汉字字集囗码序囗三百三十四字
    hzs_334



cjk_common_subset_2513__with_variantsUV13__except_TS__591
    hzsUV13_591
cjk_common_subset_2513__removed_chars_in_banned_words_4924__518
    hzsHISTORY_518
cjk_common_subset_2513__with_similar_chars_593__90
    hzsHISTORY_90
cjk_common_subset_2513__removed_chars_in_banned_words_20220415_3773__781
    hzsHISTORY_781





cjk_common_subset_2513__removed_variantsUV13__except_TS__1922
cjk_common_subset_2513__removed_similar_chars_593__2423




load___chars_in_banned_words_4924
load___all_similar_chars_593
load___chars_in_banned_words_20220415_3773
collect_variants__except_TS
hz_str_op__intersect
hz_str_op__xor
hz_str_op__remove
    '''.split()
    #xxx 高稳定度汉字字集囗第二版囗降频囗含病字框囗二百五十七字
    #xxx     hzs_includeILL_257



from pathlib import Path
_pkg_path = Path(__file__).parent


class CachedLoadText:
    def __init__(sf, total, fname, /, *, encoding='utf8'):
        sf._sz = total
        sf._fname = fname
        sf._encoding = encoding
        sf._txt = None
    def __call__(sf, /):
        if sf._txt is not None:
            return sf._txt
        path = _pkg_path / sf._fname
        sf._txt = path.read_text(encoding='utf8')
        if not len(sf._txt) == sf._sz: raise TypeError(len(sf._txt))
        return sf()
load___chars_in_banned_words_4924 = CachedLoadText(4924, '第一版数据.敏感词.字汇.4924.chars_in_banned_words.u8')
load___all_similar_chars_593 = CachedLoadText(593, '第一版数据.形近字.字汇.593.all_similar_chars.u8')
load___chars_in_banned_words_20220415_3773 = CachedLoadText(3773, '第三版数据.20220415敏感词.字汇.3773.parse_banned_words.py.字汇.out.u8')


def __load___chars_in_banned_words_4924():
    chars_in_banned_words = None
    def recur():
        nonlocal chars_in_banned_words
        if chars_in_banned_words is not None:
            return chars_in_banned_words
        path = _pkg_path / 'chars_in_banned_words.u8'
        chars_in_banned_words = path.read_text(encoding='utf8')
        return recur()
    return recur()


if __name__ == "__main__":
    #load___chars_in_banned_words_4924()
    #print(len(load___chars_in_banned_words_4924()))
    if 0:
        assert 4924 == len(load___chars_in_banned_words_4924())


def __load___all_similar_chars_593():
    all_similar_chars = None
    def recur():
        nonlocal all_similar_chars
        if all_similar_chars is not None:
            return all_similar_chars
        path = _pkg_path / 'all_similar_chars.u8'
        all_similar_chars = path.read_text(encoding='utf8')
        return recur()
    return recur()


if __name__ == "__main__":
    #load___all_similar_chars_593()
    #print(len(load___all_similar_chars_593()))
    if 0:
        assert 593 == len(load___all_similar_chars_593())



from nn_ns.CJK.cjk_subsets.hanzi import 高稳定度汉字字集囗第一版囗降频囗三百四十二字
from nn_ns.CJK.cjk_subsets.hanzi import cjk_common_subset_2513, cjk_common_subset_1869
from nn_ns.CJK.cjk_subsets.hanzi import cjk_common_subset_2513_trivial_TS_2227, cjk_common_subset_1869_trivial_TS_1631
from nn_ns.CJK.cjk_subsets.hanzi import hz_set2sorted_hz_str, hz_set2sorted_hz_str__by_reversed_freq


def collect_variants__except_TS(readonly_simplified_result4verDD_D, /):
    d = {**readonly_simplified_result4verDD_D}
    del d['kSimplifiedVariant']
    del d['kTraditionalVariant']
    s = {*[]}
    for kind, hz2hzs in d.items():
        for hz, hzs in hz2hzs.items():
            s.add(hz)
            s.update(hzs)
    #print(len(s))
    #   3684 @ver13_0
    #       vs _calc_charss: len(vary_chars) == 5361 @ver9_0
    return hz_set2sorted_hz_str(s)
def hz_str_op__intersect(lhs__hz_str, /, *rhss__hz_str):
    s = {*lhs__hz_str}
    for rhs__hz_str in rhss__hz_str:
        s &= {*rhs__hz_str}
    return hz_set2sorted_hz_str(s)
def hz_str_op__xor(lhs__hz_str, /, *rhss__hz_str):
    s = {*lhs__hz_str}
    for rhs__hz_str in rhss__hz_str:
        s ^= {*rhs__hz_str}
    return hz_set2sorted_hz_str(s)
def hz_str_op__remove(lhs__hz_str, /, *rhss__hz_str):
    s = {*lhs__hz_str}
    for rhs__hz_str in rhss__hz_str:
        s -= {*rhs__hz_str}
    return hz_set2sorted_hz_str(s)




def _mk_591UV13():
    from nn_ns.CJK.unicode.ucd_unihan.unihan.parsed_result__of__Unihan_Variants_txt__of_ver13_0 import readonly_parsed_result4ver13_0, readonly_simplified_result4ver13_0
    hzs_with_variantsUV13__except_TS__3684 = collect_variants__except_TS(readonly_simplified_result4ver13_0)
    assert 3684 == (len(hzs_with_variantsUV13__except_TS__3684))

    ######################
    hzsUV13_591 = cjk_common_subset_2513__with_variantsUV13__except_TS__591 = hz_str_op__intersect(cjk_common_subset_2513, hzs_with_variantsUV13__except_TS__3684)
    assert 591 == len(hzsUV13_591)
    return hzsUV13_591

def _mk_518HISTORY():
    hzsHISTORY_518 = cjk_common_subset_2513__removed_chars_in_banned_words_4924__518 = hz_str_op__remove(cjk_common_subset_2513, load___chars_in_banned_words_4924())
    # print(hzsHISTORY_518)
    assert 518 == len(hzsHISTORY_518)
    return hzsHISTORY_518

def _mk_90HISTORY():
    hzsHISTORY_90 = cjk_common_subset_2513__with_similar_chars_593__90 = (hz_str_op__intersect(cjk_common_subset_2513, load___all_similar_chars_593()))
    #print(hzsHISTORY_90)
    assert 90 == len(hzsHISTORY_90)
    return hzsHISTORY_90

def _mk_781HISTORY():
    hzsHISTORY_781 = cjk_common_subset_2513__removed_chars_in_banned_words_20220415_3773__781 = hz_str_op__remove(cjk_common_subset_2513, load___chars_in_banned_words_20220415_3773())
    # print(hzsHISTORY_781)
    assert 781 == len(hzsHISTORY_781)
    return hzsHISTORY_781

#assert not {*_mk_518HISTORY()} < {*_mk_781HISTORY()}


######################
######################
######################
#[[[[[
hzsUV13_591 = '一七万三丕丘中乃九乾予事二于五井亡人仇他仙仝仟以任伍低佑余佰侮俟俯偃健傍儒儡全八六兮冒冗凄准凡凶凹出函刀刃分刊利刷刺剃剌剩剪剿劈劫包匈匏匙匹十千卉卒卓博占厄厘叉叔只叫台吃吉吊同吝吟含吸吹吻告周味咀和咨咬咳咽哲唇唾啖啼喜喧嗅嗽嘴器四回困圭坎坐坑坤域基堆堤塑塔塾壬壹外天奇奈奎奔奕妊妙妹姆姻娘娠娩嫉嫩孀子孰完宜宴宿密寇察寡寨寸尉尸尻尿居岩峨峰崔崖嵩嶝巍川巡帆帙幕幡幸庄床座庵庸弄弊弦彬彷往徒御心忍志怪恍恐恤恩悚悠惺愈愉愍愧愿慈慷憔憩扁手才托扼折披抹抽拇拈拓拗拭拯拾拿按挫挽捉捌捏捷掉掩揶搜搬搭擒攀收效敏敦敷文斌斤斥於旁旒旗明昏映昧晁暖暴曜曳更曼望朝期朦朴机村杓杯杰杷板果架柄柏某柚柳栖梁梨棋棕棹椎椰楞楠楫榛榧榴槌樊樽欣欲款歌殃殉毓氓水汨沈沫沸泄泉泛泡泥洞浚浣涅涌涎涕淆淡淫淳淹渚渫湮溯溺滂漆漫漱潺澳澹火灰炯炸照煮熏熔熙爪版牛牟犁犬狸猿玄玖玳珍琅琉瑙璃瓮瓷甬町留略疆疋疏疸疹痒痴痼登百皎皓益眈眠睫睹睾睿瞥瞬瞰瞿矮石砒砥砦砧硬碗磁磊示秉秋秕秘秤移稚稿窕竿笑笛筏答箔算管箴箸粗粘粳糖糟糠纂缶缸罐罔罪置署羌美群羹翅翼耀考耐耕耗耘肆肇股肢肱育肴胄背胚胸脆腕腿膳舍舒舵船芒芟花苛苟苡茉草菌菰萱著葬蒸蔗蔚薯藉藤虐虔虞蚊蚓蚤蛋蛔蛙蛛蜂蝎蝶螂融螳螺蟹衣衿袋袒裙裸褒褓襁襄襟解警豆豚豫豺貌赤跳踊踏踵蹄蹴蹶躁躬辣辨迪迫逃逞速逮逼逾遍遭郁酉酋酢酬醇醒野金阜阡阿陀降陶隍隧雁集雇雍雕雨霜霰靴鞋鞫食餐高魏麟麻默鼎鼓'


if 0:
    assert hzsUV13_591 == _mk_591UV13()
assert 591 == len(hzsUV13_591)
cjk_common_subset_2513__with_variantsUV13__except_TS__591 = hzsUV13_591

######################
cjk_common_subset_2513__removed_variantsUV13__except_TS__1922 = hz_str_op__remove(cjk_common_subset_2513, cjk_common_subset_2513__with_variantsUV13__except_TS__591)
assert 1922 == (len(cjk_common_subset_2513__removed_variantsUV13__except_TS__1922))

######################
hzsHISTORY_518 = '亥仝仟佃佚佰佶侈侏侑俎俑俟俳俸俺倨倬偈傀僖僭儡兀兮冗冽刈剌剔勺匈匍匏匐卜卞卯咫咳哉哺啖喀喙嗅嗔嗜嗟嗣嗽嗾噫嚆囹圄圻垓垠埴堀堤塘塾壑壕壬壹夙娑嫦嬖孚孰孱孵孺宸寤岫岬嵋嵌嵩嵬嵯嶝巳巽帑帙幄幡幢庠庵庶廛弧彖彗徇怏恁恂悌悖悛悸惟愆愍慊慝慷憩憾懋懿戊戌戍戟戡拇拌拗拷捌掖揄揆揖揶摺撰擘擢攫攸敖敞斛斡斫旒旬旱昴昶晁晏暑暝暹暾曙曜曦曳曷朕杉杓杷枇枋枳枷枸柑柝柩株桁桎桔梏梗梢梭棕棚棠棹椅椎椒椰椽椿楔楞楫楮楸楹榛榧榻槁槌槿樗樟樽橄橙橡檄檎檗殄殆毋汐汨汾沮沼泗洌洵浚涅涎涓淀淅淙淞淮渤渥渫湍湟湫溟溥溯滓漕漱潼澄澹濂濠瀑灸烙焙熄燎燔燧燮爪爰爻犁狎猊猝猩玳珀珂珞珥琅琉琢琥琵琶瑁瑚瑛瑾璃璋瓠瓢甄甑甥町畛畦疋疝疥疳疵疸痂痍痘痢痰痼瘠瘢癌癖癸皿盂眄眈眸瞑瞰矣砒砦砧碇碗碣磐磬礁祉祗禳秕秧稔稗稷穰穹窈窒窕竺笙笛筌筐筮筵箔箝箸篁簪簿粕粳纂纛缶缸罐羌羚羲羸羹翊翌翕翡耆聿肄肋肢肪肱胄胚胛胤胥脊脯腕腱膈膊膨膳臼臾舫舷艮芋芍芟芹苒苔苡茄茯茱茴茵茸荀荏荷荻莪菁菖菰菽萄萱萸葡葺蒜蒡蒿蓍蓑蓼蔗蔬蕃蕉蕨薇薨藩蚌蚓蚣蚤蚩蛔蛟蛭蛾蜈蝗螂螟螳蟠衙衢衾衿袈裟裨裳裴褓褥褶襁豌豕豚貊趺跏跛跣踊踵蹇蹉蹙迭逋逑逞逡逵遑邑邯邸郡鄂酉酊酋酎酢酩酪酵醍醴醵釉阡阪阮陂陟隅隋隍雉雎霓鞍鞫魃麒麓麝麾黍黜'

if 0:
    assert hzsHISTORY_518 == _mk_518HISTORY()
assert 518 == len(hzsHISTORY_518)
cjk_common_subset_2513__removed_chars_in_banned_words_4924__518 = hzsHISTORY_518

######################
hzsHISTORY_90 = '丁不九二云仝仟任但位兀充兵冕凡刃刊刑刺剌匈匕北千卯叉友叱咀回坦壬天夭奸姐孑孝少市干延弓彖戊戌戍支改斤日旭昏春晟普曰月朦木林枚柬毋母毛汨爪牙狂狙玉瓜由疋空羊胄臣臼芋蚩袒谷豕辛速逢采鼓'

if 0:
    assert hzsHISTORY_90 == _mk_90HISTORY()
assert 90 == len(hzsHISTORY_90)
cjk_common_subset_2513__with_similar_chars_593__90 = hzsHISTORY_90

######################
cjk_common_subset_2513__removed_similar_chars_593__2423 = (hz_str_op__remove(cjk_common_subset_2513, cjk_common_subset_2513__with_similar_chars_593__90))
assert 2423 == (len(cjk_common_subset_2513__removed_similar_chars_593__2423))

######################
hzsHISTORY_781 = '且丞乞亥仄仝仟伉伎伺伽佃但佚佩佯佶侃侈例侏侑俎俑俟俳俸倦倨倬倭偃偈偏偕傍傲僖僭僻兀允兢兮冕冗冥冽凄凋函刈刎剃剌剔剪剽劈勉勘匈匍匏匐卉卜卞卦卯厄厘吊吏吝吠吩呈呱呵咀咆咐咫咬咳咽哮哺唆啖啼喀喙喧嗅嗜嗟嗣嗤嗽嗾嘲嘶噫嚆嚼囹圃圄圭圻坎坡垂垓垠垢垣埠埴堀堤堪堰塾壅壑壕壤壬夙夷奄奏奠妊妨娑娠娩婉嫉嬖孑孚孜孝孰孺宕宛宥宸寤寥寮屑履岑岫岬峙峻嵋嵌嵩嵬嵯嶝巳巽帑帙幄幡幢庠廊廓廛弛弧弼彖彗彼徊徘徨忖忿怏怠恁恂恍恕恣恪恬恰悉悌悖悛患悸惚惟惰惶惺愆愈愉愍愎愕愧慊慝憎憧憩憬憾懈懋懦戌戚戟戡扇扈扉扼抉抒拂拇拈拌拗拙拭拮挽捌捺掖掩揄揆揖揶搭摺撰擅擘攘攫攸敖敞敷斛斜斟斡斫旌旒旬昊昴昶晁晏晦暄暇暑暝暹暾曜曳曷朦札杉杓杖杞杳杵杷枇枉枋枚枯枳枷柚柝柩柬栖栽桀桁桎桓梏梢梵棕棘棚棹椅椰椽椿楔楞楫楮楸楹榛榧槁槌槿樗樽橄橙檄檎檗歇殄殆毋汐汨汰汲沂沃沐沓沮沼沽沿泌泗泯泳洌洵浚涅涎涓淅淆淙淞淮淳淹渚渤渥渫渺湃湍湛湟湫湮溟溥溯滂滓漕漱潺潼澎澹濂濡濯瀑瀚灸灼炊炙炭烙烽焙煦熄熔燎燔燥燧燮爬爰爻牒牝犁狎猊猖猩猷猿獗玳珀珂珊珞珥琅琢琥琵琶瑁瑕瑚瑛瑾璋璞璧瓠瓢瓣甄甑甚甥町畛畦疋疏疝疥疲疳疵疸疽痂痍痘痢痼瘠瘢癖皿盂盆眄眈眩眸眺睦睫瞑瞥瞬瞰瞳矗矜矣矩砥砦砧碇碌碣磊磋磐磨磬礁祀祉祗禳秕秧稍稔稗稚稠稷稼稽穰窄窈窒窕窘窟竭竺竿笏笞筌筮筵箔箕箝箸篁篆簇簪粕粱粲粳粹紊纂纛缶缸罔罹羌羚羲羸羹翕翩翰耆耘聆聿肄肋肢肪肱肴肺胃胄胛胥胱脆脊脯脾腑腕腱膈膊膣膨膺臂臆臼臾舛舫般舵舶舷艇艮芋芍芟芭芸芹苒苛苟苡茄茫茯茱茴茵茸荀荏莪菁菅菖菰菽萃萱葵葺蒡蓍蓑蓼蔑蔓蔗蔬蕃蕉蕨薨薯藉藕藩藻虞蚌蚓蚣蚤蚩蛔蛟蛭蜀蜃蜈蜚蝗螂螳蟠衢衷衾衿袂袈袒裕裟裨褒褓褥褪褶襁襟誓譬豌豕豚豫貊赳趺趾跋跏跛跣踊踞踵蹇蹉蹙蹴蹶躁躇躬辜迦述逋逑逞逡逮逵逾遁遂遐遑遵遽邀邃邸郁郡鄂酉酊酋酌酎酢酩酪酵醍醯醴醵釉釜阡阪阮陀陂陌陟隅隋隍隘隙雉雌雎雹霓霹鞍鞠鞫馥馨骸魃麝麾黍黛黜'

if 0:
    assert hzsHISTORY_781 == _mk_781HISTORY()
assert 781 == len(hzsHISTORY_781)
cjk_common_subset_2513__removed_chars_in_banned_words_20220415_3773__781 = hzsHISTORY_781



#]]]]]
######################
######################
######################









######################
######################
######################
#[[[[[
# _试着复刻第一版_但UV版本不同()
hzs_2150 = cjk_common_subset_2513_trivial_TS_2227__removed_similar_chars_593__2150 = (hz_str_op__intersect(cjk_common_subset_2513_trivial_TS_2227, cjk_common_subset_2513__removed_similar_chars_593__2423))
assert 2150 == len(hzs_2150)
hzs_1726 = cjk_common_subset_2513_trivial_TS_2227__removed_similar_chars_593__removed_variantsUV13__1726 = (hz_str_op__intersect(cjk_common_subset_2513__removed_variantsUV13__except_TS__1922, cjk_common_subset_2513_trivial_TS_2227__removed_similar_chars_593__2150))
assert 1726 == len(hzs_1726)
hzs_377 = cjk_common_subset_2513_trivial_TS_2227__removed_similar_chars_593__removed_variantsUV13__removed_chars_in_banned_words_4924__377 = (hz_str_op__intersect(cjk_common_subset_2513__removed_chars_in_banned_words_4924__518, cjk_common_subset_2513_trivial_TS_2227__removed_similar_chars_593__removed_variantsUV13__1726))
assert 377 == len(hzs_377)

hzs_342 = 高稳定度汉字字集囗第一版囗降频囗三百四十二字
assert 342 == len(hzs_342)

hzs_334 = '亥佃佚佶侈侏侑俑俳俸俺倨倬偈傀僖剔勺匍匐卞咫哉哺喀喙嗜嗟嗣嗾噫嚆圄埴堀塘壑壕夙娑嫦嬖孱孺宸寤岬嵋嵌嵬巳帑幄庠廛弧徇怏恁悌悖悸惟愆慊慝憾懋懿戟戡拌拷掖揄揆揖撰擘擢攫攸敖敞斛斡斫旬旱昴晏暑暝暹暾曙曦曷朕杉枇枋枷枸柑柝株桎桔梏梗梢梭棚棠椅椽椿楔楮楸楹榻槿樗樟橄橙橡檄檎檗殄殆汐汾沮沼泗洵涓淅淞淮渤渥湍湫溟溥滓漕潼濂濠瀑灸焙熄燔燧燮爰爻狎猊猝猩珀珂珥琢琥琵琶瑁瑚瑛瑾璋瓠瓢甄甑甥畛畦疝疥疳疵痂痍痘痰瘠瘢癌癖癸皿盂眄眸瞑矣碇碣磬礁祉禳秧稔稗稷穹窈窒竺笙筌筮筵篁簿粕纛羲羸翊翌翕翡耆肄肪胛胤胥脯腱膈膊膨臾舫舷艮芍芹苒苔茄茯茱茴茵茸荀荏荷荻莪菁菖菽萄萸葡葺蒜蒡蒿蓍蔬蕃蕉蕨薇薨藩蚌蚣蛟蛭蛾蜈蝗螟蟠衙衢衾袈裟裨裳褥褶豌趺跏跛跣蹇蹉蹙逋逑逡逵邯邸郡鄂酊酎酩酵醍醵釉陂陟隅雉雎魃麒麝麾黍黜'
    #hzs_334__content

assert 334 == len(hzs_334)
assert hzs_334 == hz_str_op__intersect(hzs_342, hzs_377)#_342and377
assert hzs_334 == hz_str_op__intersect(cjk_common_subset_2513__removed_variantsUV13__except_TS__1922, cjk_common_subset_2513_trivial_TS_2227, 高稳定度汉字字集囗第一版囗降频囗三百四十二字)
    #hzs_334__definition
assert hzs_334 == hz_str_op__remove(hzs_342, '嗔枳槁淙磐簪脊蔗') #_342 - _342diff377
hzs_334_excludeILL_322 = hz_str_op__remove(hzs_334, '疝疥疳疵痂痍痘痰瘠瘢癌癖')
        #hzs_334_excludeILL_322__definition
assert 322 == len(hzs_334_excludeILL_322)


def _试着复刻第一版_但UV版本不同():
    # total_common_CJK_chars_exclude_nonHanzi = 2513
    cjk_common_subset_2513

    # total_common_CJK_han_chars_exclude_multiST = 2340
    cjk_common_subset_2513_trivial_TS_2227 # < 2340
        # 不仅 数据版本不同，而且 规则改变:
        #   繁简唯一可逆 改为 繁简平凡自反

    # total_common_CJK_uniqueST_han_chars_exclude_similars = 2259
    hzs_2150 # < 2259


    # total_common_CJK_noSimilar_han_chars_exclude_vary_chars = 1520
    # total_common_CJK_noSimilar_han_chars_exclude_all_chars_with_variant = 1518
    hzs_1726 # > 1518
        #!!! 奇怪！怎么到了这里，反而比 第一版 更多？
        # ver13_0 比 ver9_0 数据更少？
        #


    # total_common_CJK_noVariant_han_chars_exclude_banned = 342
    # total_common_CJK_nonBanned_han_chars_exclude_numeric = 342
    hzs_377 #377 > 342
    ...



    ######################
    # 无法兼容 第一版？
    ######################
    _377diff342 = hz_str_op__remove(hzs_377, hzs_342)
    #print(_377diff342)
    assert _377diff342 == '俎僭冽刈囹圻垓垠孚孵岫嵯巽庶恂悛昶柩桁椒洌湟烙燎珞痢穰筐羚聿肋蓼裴貊遑邑酪醴阮隋霓鞍麓'
    #print(len(_377diff342))
    assert len(_377diff342) == 43

    _342diff377 = hz_str_op__remove(hzs_342, hzs_377)
    #print(_342diff377)
    assert _342diff377 == '嗔枳槁淙磐簪脊蔗'
    #print(len(_342diff377))
    assert len(_342diff377) == 8

    _342and377 = hz_str_op__intersect(hzs_342, hzs_377)
    #print(_342and377)
    #print(len(_342and377))
    334
    assert _342and377 == hzs_334

_试着复刻第一版_但UV版本不同()
#]]]]]
######################
######################
######################



















######################
if 1:
    cjk_common_subset_1869__removed_chars_in_banned_words_4924__140 = hz_str_op__intersect(cjk_common_subset_1869, cjk_common_subset_2513__removed_chars_in_banned_words_4924__518)
    assert 140 == (len(cjk_common_subset_1869__removed_chars_in_banned_words_4924__140))


hzs_85 = hz_str_op__intersect(cjk_common_subset_1869, 高稳定度汉字字集囗第一版囗降频囗三百四十二字)
assert 85 == len(hzs_85)
assert hzs_85 == '亥佃侈俺剔勺哉哺嗜塘嵌巳弧惟憾拌拷撰敞旬旱暑曙杉柑株桔梗梢梭棚棠椅椿樟橙橡沮沼淮渤瀑灸熄猩琢瓢甥痘痰癌癸皿矣礁秧窒簿肪脊脯膊膨芹苔茄茵茸荷萄葡蒜蔗蔬蕉蚌蛾蝗衙裳褥豌鄂酵隅'

hzs_83 = hz_str_op__intersect(cjk_common_subset_1869, hzs_334)
assert 83 == len(hzs_83)
assert hzs_83 == '亥佃侈俺剔勺哉哺嗜塘嵌巳弧惟憾拌拷撰敞旬旱暑曙杉柑株桔梗梢梭棚棠椅椿樟橙橡沮沼淮渤瀑灸熄猩琢瓢甥痘痰癌癸皿矣礁秧窒簿肪脯膊膨芹苔茄茵茸荷萄葡蒜蔬蕉蚌蛾蝗衙裳褥豌鄂酵隅'
assert '脊蔗' == (hz_str_op__remove(hzs_85, hzs_83))


######################
######################
######################
######################
######################

#第二版
def _mk_257_259():
    assert '巳' in hzs_334
        #包含『巳』？！不能满意！i
        #说好的排除形近字呢？all_similar_chars不行！
        #-只能手动排除了，幸好不多。


    hzs_85
        #1869 太凶残，削减太多。
        #
        # 毕竟考虑的是作为『数据』，2513已是所有汉字编码方案都支持的，1869没必要。
        # 生僻字也无妨，但笔画不要太多
        # 字集 内部 不要含 形近字，或 大偏旁一样的字；外部 不要有 形近的常用字
        # 准淮谁推椎: 根据实际情况，只保留『木字旁』，去掉『两点水』『三点水』『言字旁』『提手旁』
        # 『病字框』看起来像广告，也去掉。
        # 『竹字头』『草字头』？
        ######################
        #但不现实，太多了，若要凑足258个以上，不能这么搞。
        #   部首就算了。
        #
        #但12个『病字框』:『疝疥疳疵痂痍痘痰瘠瘢癌癖』，实在不能忍。
        #   更换为：『曦甄悸戟瓢槿樟葡萄拌憾旱』
        #

    r'''
慝te4
    奸邪，邪恶：隐慝（人家不知道的罪恶）。
    阴气。
    灾害：“以伏蛊慝”。
    笔顺：一一丨丨一丿丨乛一乛丶乛丶丶
匿ni4
隐藏，躲藏：隐匿。藏匿。匿名。销声匿迹。
藏躲
笔顺：一一丨丨一丿丨乛一乛

翌yì
    明（天，年）：翌日。翌晨（明天早晨）。翌年。
    笔顺：乛丶一乛丶一丶一丶丿一
翊yì
    辅佐，帮助：翊戴（辅佐拥戴）。翊赞。
    古同“翌”，明日。
    笔顺：丶一丶丿一乛丶一乛丶一
    #古今字？通假字？不能选用。
    #'''

    #hzs_includeILL_257__definition
    _1 = (hz_str_op__remove(
    高稳定度汉字字集囗第一版囗降频囗三百四十二字
    , '嗔枳槁淙磐簪脊蔗'
        #(见上面_342diff377)
        #除去后即为：hzs_334
    , '磬[磐]羲曦甄甑悖悸懿壑嬖檗擘斡戟翊翌瓠瓢蕃藩溟暝瞑螟壕濠槿瑾樟璋娑裟燔蟠楸湫惟淮雉雎旬匍葡荀萄匐'
        #(内部形近)
        #
        #   反出:'曦甄悸戟瓢槿樟葡萄'
    , '慝帑肄麾埴沮拌憾卞皿簿肋旱旬荀巳爰倨檎揄堀羸艮淅庠'
    # [匿努肆摩植诅绊撼下血薄胁早句苟已爱据擒愉掘赢良浙痒]
        #(外部形近)
        #
        #   反出:'慝拌憾皿旱'
    , '衢醵麝纛廛懋燮攫暹'
        #(笔画太多了)
    ))

    _2 = hz_str_op__remove(r'''
    曷孱圄亥矣鄂敞肪脯膊杉攸偈侑盂斛爻臾翕祉灸褥耆癸膨倬禳勺
    噫嚆喀嗾暾曙眄
    沼渤瀑
    榻樗拷
    嵬竺薨
    疳疵痍瘠瘢
    ######################
    疝疥痂痘痰癌癖
    #
    笙筌筮筵篁
    芍芹苒苔茄茯茱茴茵茸荏荷荻莪菁菖菽萸葺蒜蒡蒿蓍蔬蕉蕨薇
    #
    汐汾泗洵涓淞渥湍溥滓漕潼濂
    塘
    掖揆揖撰擢
    枇枋枷枸柑柝株桎桔梏梗梢梭棚棠椅椽椿楔楮楹橄橙橡檄
    #
    佃佚佶侈侏俑俳俸俺傀僖剔咫哉
    哺喙嗜嗟嗣
    夙嫦孺宸寤岬嵋嵌幄弧徇怏恁悌愆慊戡
    敖斫昴晏暑朕
    殄殆
    焙熄燧狎猊猝猩
    珀珂珥琢琥琵琶瑁瑚瑛甥畛畦
    眸碇碣礁秧稔稗稷穹窈窒
    粕翡胛胤胥腱膈舫舷
    蚌蚣蛟蛭蛾蜈蝗衙衾袈裨裳褶豌趺跏跛跣蹇蹉蹙逋逑逡逵邯邸郡酊酎酩酵醍釉陂陟隅魃麒黍黜
    #''', '# \n')

    #print(hz_str_op__xor(_1, _2))
    assert _1 == _2
    assert 257 == len(_1)

    #print((_1))
    assert _1 == '亥佃佚佶侈侏侑俑俳俸俺倬偈傀僖剔勺咫哉哺喀喙嗜嗟嗣嗾噫嚆圄塘夙嫦孱孺宸寤岬嵋嵌嵬幄弧徇怏恁悌愆慊戡拷掖揆揖撰擢攸敖敞斛斫昴晏暑暾曙曷朕杉枇枋枷枸柑柝株桎桔梏梗梢梭棚棠椅椽椿楔楮楹榻樗橄橙橡檄殄殆汐汾沼泗洵涓淞渤渥湍溥滓漕潼濂瀑灸焙熄燧爻狎猊猝猩珀珂珥琢琥琵琶瑁瑚瑛甥畛畦疝疥疳疵痂痍痘痰瘠瘢癌癖癸盂眄眸矣碇碣礁祉禳秧稔稗稷穹窈窒竺笙筌筮筵篁粕翕翡耆肪胛胤胥脯腱膈膊膨臾舫舷芍芹苒苔茄茯茱茴茵茸荏荷荻莪菁菖菽萸葺蒜蒡蒿蓍蔬蕉蕨薇薨蚌蚣蛟蛭蛾蜈蝗衙衾袈裨裳褥褶豌趺跏跛跣蹇蹉蹙逋逑逡逵邯邸郡鄂酊酎酩酵醍釉陂陟隅魃麒黍黜'

    hzs_includeILL_257 = _ill_257 = hz_set2sorted_hz_str__by_reversed_freq(_1)
    #return _ill_257

    '曦甄悸戟瓢槿樟葡萄'
    '慝拌憾皿旱'
    sADD = '曦甄悸戟瓢槿樟葡萄' '慝拌憾皿旱'
    sDEL = '疝疥疳疵痂痍痘痰瘠瘢癌癖'
    s = {*hzs_includeILL_257}
    s.update(sADD)
    #hzs_excludeILL_259__definition
    s -= {*sDEL}
    assert 259 == len(s)
    hzs_excludeILL_259 = _oll_259 = hz_set2sorted_hz_str__by_reversed_freq(s)
    #print(hzs_excludeILL_259)
    return (_ill_257, _oll_259)


hzs_includeILL_257 = '矣郡荷哉嗣撰朕癸亥椅衙俺癌猩塘擢薨裳稷蝗梗揖晏棠喀梢暑膊胤株筵棚沼弧敞榻殆鄂敖邸嗟膨黜逵漕攸蔬蛟嵌俸瘢嗜哺蕉杉侈梭胥汾掖琢甥斛耆隅茵檄竺笙釉宸潼徇礁僖臾泗渥拷脯瑛孺熄瑚琶渤恁苔芍偈褥痰裨舷勺橡嫦逋珀佃夙肪枷剔薇椿蹙茄涓溥茸窒穹蛾衾陟琵菁猝曙酵邯眸曷瀑焙蛭珂揆瑁喙陂舫斫桔愆跛黍佚癖蹇湍蒜珥橙怏逡嵋跏燧昴疵爻麒橄寤幄胛淞滓狎窈芹荻盂碇瘠蚌祉洵楹秧咫筮蚣悌跣趺褶灸魃倬翡傀殄岬菽俳蒿侏袈痘俑稔畛粕翕濂蜈葺柑楔椽樗嵬噫琥碣嗾禳戡萸侑枋暾梏楮汐豌蕨逑桎慊佶畦稗酊圄菖孱疥蓍蹉痍枸枇茯猊酩荏苒眄茱痂篁腱膈筌醍柝酎莪疝茴疳蒡嚆'
    #hzs_includeILL_257__content

hzs_excludeILL_259 = '矣郡荷哉嗣撰朕癸亥椅衙旱俺猩塘擢薨裳稷葡憾蝗梗萄揖晏棠喀梢暑膊胤株筵棚沼弧敞榻殆鄂敖邸嗟膨黜逵漕攸蔬蛟嵌俸嗜哺蕉杉侈梭胥汾掖琢戟甥斛耆隅茵檄竺笙釉宸潼徇礁僖臾泗渥拷脯瑛孺熄瑚琶渤甄恁苔芍偈褥裨舷勺橡嫦逋珀佃夙肪枷剔薇椿蹙茄涓溥茸窒穹蛾衾陟琵菁猝曙酵邯眸曷瀑焙悸蛭珂揆瑁喙陂舫斫桔愆跛黍佚蹇曦湍蒜珥橙怏瓢逡嵋跏燧昴爻麒橄寤幄胛淞滓狎窈芹拌荻盂碇皿蚌祉洵楹秧咫筮蚣悌跣趺褶灸樟魃倬翡傀殄岬菽俳蒿侏袈俑稔畛粕翕濂蜈葺柑楔椽樗嵬噫琥碣嗾禳戡萸槿侑枋暾慝梏楮汐豌蕨逑桎慊佶畦稗酊圄菖孱蓍蹉枸枇茯猊酩荏苒眄茱篁腱膈筌醍柝酎莪茴蒡嚆'
    #hzs_excludeILL_259__content




assert (hzs_includeILL_257, hzs_excludeILL_259) == _mk_257_259()

assert 257 == len(hzs_includeILL_257)
assert 259 == len(hzs_excludeILL_259)
assert '' == hz_str_op__remove(hzs_includeILL_257, hzs_334)
assert '' == hz_str_op__remove(hzs_excludeILL_259, hzs_334)


assert set(hzs_excludeILL_259) < set(hzs_334_excludeILL_322)

高稳定度汉字字集囗第二版囗降频囗含病字框囗二百五十七字 = hzs_includeILL_257
del 高稳定度汉字字集囗第二版囗降频囗含病字框囗二百五十七字, hzs_includeILL_257

高稳定度汉字字集囗第二版囗降频囗无病字框囗二百五十九字 = hzs_excludeILL_259
    #第二版259

用统一码十三版数据复刻并兼容初版高稳定度汉字字集囗码序囗三百三十四字 = hzs_334
    #第一版复刻版334
用统一码十三版数据复刻并兼容初版高稳定度汉字字集囗无病字框囗码序囗三百二十二字 = hzs_334_excludeILL_322
    #第一版复刻去病版322


#第三版
def _mk_261():
    hzsHISTORY_781 #底本 之一

    assert len(hz_str_op__intersect(hzsHISTORY_781, hzs_excludeILL_259)) == 214 < 256 == 2**8
        #无法兼容 第二版259
    assert len(hz_str_op__intersect(hzsHISTORY_781, hzs_342)) == 288 > 256 == 2**8
        #可以兼容 第一版342

    hzs_271 = hz_str_op__intersect(hzsHISTORY_781, hzs_334_excludeILL_322)
    assert len(hzs_271) == 271 > 256 == 2**8
        #可以兼容 第一版复刻去病版322
    #print(hzs_271)
    assert hzs_271 == '亥佃佚佶侈侏侑俑俳俸倨倬偈僖剔匍匐卞咫哺喀喙嗜嗟嗣嗾噫嚆圄埴堀壑壕夙娑嬖孺宸寤岬嵋嵌嵬巳帑幄庠廛弧怏恁悌悖悸惟愆慊慝憾懋戟戡拌掖揄揆揖撰擘攫攸敖敞斛斡斫旬昴晏暑暝暹暾曷杉枇枋枷柝桎梏梢棚椅椽椿楔楮楸楹槿樗橄橙檄檎檗殄殆汐沮沼泗洵涓淅淞淮渤渥湍湫溟溥滓漕潼濂瀑灸焙熄燔燧燮爰爻狎猊猩珀珂珥琢琥琵琶瑁瑚瑛瑾璋瓠瓢甄甑甥畛畦皿盂眄眸瞑矣碇碣磬礁祉禳秧稔稗稷窈窒竺筌筮筵篁粕纛羲羸翕耆肄肪胛胥脯腱膈膊膨臾舫舷艮芍芹苒茄茯茱茴茵茸荀荏莪菁菖菽葺蒡蓍蔬蕃蕉蕨薨藩蚌蚣蛟蛭蜈蝗蟠衢衾袈裟裨褥褶豌趺跏跛跣蹇蹉蹙逋逑逡逵邸郡鄂酊酎酩酵醍醵釉陂陟隅雉雎魃麝麾黍黜'
        # 字数不充裕，不再考虑去除形近字。
        #   保留『巳』
    #hzs_261__definition

    _261 = hz_str_op__remove(hzs_271, '嬖燮爰皿羲羸 窒鄂麝狎')
        #嬖燮爰皿羲羸--娈？变？爱？血？义？赢？看起来就像会被屏蔽掉的样子
        #窒鄂麝狎--窒(窒息)鄂(地名)麝(商品)狎(嫖客)
        #xx 廛(~塵)磬(~罄)
    r'''古今字 这么多？
[[[
廛chan2
古代城市平民的房地：廛里（古代城市中住宅的通称）。市廛（集市）。
古同“缠”，束。
笔顺：丶一丿丨乛一一丨一一丿丶一丨一

纛dao4
古代军队里的大旗。
古代用毛羽做的舞具或帝王车舆上的饰物。
笔顺：一一丨一乛乛丨一丨乛一一一一丨丿丶丿乛乛丶丨丿丶

佃dian4
向地主或官府租种土地的农民：佃户。佃农。佃客（晋代世家豪强荫庇下的一种依附农民）。佃东。
佃tian2
耕作。
古同“畋”，打猎。
笔顺：丿丨丨乛一丨一

佚yi4
同“逸”②③。
放荡：淫佚。佚游。
美：佚女。
姓。
佚die2
古同“迭”，轮流，更替。
笔顺：丿丨丿一一丿丶

侑you4
相助。
在筵席旁助兴，劝人吃喝：侑食。侑饮。侑觞。
报答。
古同“宥”，宽赦。
笔顺：丿丨一丿丨乛一一

倨ju4
傲慢：前倨后恭（先傲慢而后恭敬）。倨傲。倨固。倨慢。
微曲：倨句（钝角形的称“倨”；锐角形的称“句”）。
古同“踞”，伸开脚坐着。
笔顺：丿丨乛一丿一丨丨乛一

堀ku1
古同“窟”，洞穴。
穿穴：“（舜）以其徒属堀地财，取水利……然后免于冻馁之患。”
冲起：“塕然起于穷巷之间，堀堁扬尘。”
笔顺：一丨一乛一丿乛丨丨乛丨

寤wu4
睡醒：“七日而寤”。寤寐以求。
古同“悟”，理解，明白。
古同“牾”，逆。
寐
笔顺：丶丶乛乛丨一丿一丨乛一丨乛一

帑tang3
古代指收藏钱财的府库或钱财：帑藏（指国库）。府帑（府库里的钱财）。重帑（大量的钱财）。
帑nu2
古同“孥”，儿女。
鸟尾：鸟帑。
笔顺：乛丿一乛丶丨乛丨

恁nen4
那么，那样，如此，这样：恁大。恁高。
那：恁时节。
怎么：“却恁地教甚么人在间壁吱吱地哭，搅掩兄弟们吃酒？”
恩，念：“宜亦勤恁旅力，以充厥道”。
恁nin2
古同“您”。
笔顺：丿丨丿一丨一丶乛丶丶

懋mao4
勤奋努力。
古同“茂”，盛大。
勉励，鼓励。
美。
高兴。
笔顺：一丨丿丶乛丶乛丨丿一丨丿丶丶乛丶丶

拌ban4
搅和：搅拌。拌和。拌面。拌菜。拌草料。
口角：拌嘴。
拌pan4
古同“拚”，舍弃。
古同“判”，分开。
笔顺：一丨一丶丿一一丨

掖ye4
用手扶着别人的胳膊：扶掖。
扶持别人：掖护。奖掖。
古同“腋”，旁边。
掖ye1
把东西塞在衣袋或夹缝里：腰里掖着手榴弹。
笔顺：一丨一丶一丿丨丿乛丶丶

擘bo4
大拇指：擘画（计划，布置。亦作“擘划”）。擘窠（指在印章或石碑上用直线划出来的方格子，以使刻写的字整齐）。巨擘（喻杰出的人物）。擘肌分理（喻分析事理很缜密）。
擘bai1
同“掰”。
笔顺：乛一丿丨乛一丶一丶丿一一丨丿一一丨

敖ao2
出游，闲游：“以敖以游”。
古同“熬”，煎熬。
姓。
笔顺：一一丨一乛丿丿一丿丶

敞chang3
（房屋、庭院等）没有遮蔽：敞亮。宽敞。
张开，打开：敞着大门。敞篷马车。敞开供应。
古同“畅”，畅快。
笔顺：丨丶丿丨乛丨乛一丿一丿丶

斡wo4
转，旋：斡流。斡运。斡旋（调解，把弄僵了的局面扭转过来）。
斡guǎn
古同“管”，主管，掌管。
笔顺：一丨丨乛一一一丨丿丶丶丶一丨

晏yan4
迟，晚：晏起。晏驾。
天清无云：天清日晏。
鲜艳。
同“宴”③。
安定，安乐：晏宁晏处（安然处之）。晏安。晏然。
〔晏晏〕温柔，和悦，如“言笑晏晏”。
姓。
笔顺：丨乛一一丶丶乛乛丿一

曷he2
何，什么：“蹈死不顾，亦曷故哉？”
怎么，为什么：“汝曷弗告朕？”
古同“盍”，何不。
何时：“悠悠苍天，曷其有所？”。
笔顺：丨乛一一丿乛丿丶乛

枋fang1
古书上说的一种树，木材可做车。
方柱形木材：枋子（亦指棺材）。
枋bing4
古同“柄”，权柄。
笔顺：一丨丿丶丶一乛丿

柝tuo4
古代打更用的梆子：“朔气传金柝”。
古同“拓”，开拓。
笔顺：一丨丿丶丿丿一丨丶

梢shao1
树枝或条状物的末端：树梢。末梢。梢头。梢林。
末尾：眉梢。收梢。
古代奏乐时拿的竿子。
古同“艄”，船舵尾。
梢sao4
像圆锥体的形状。
柱形物体的横剖面向一端面逐渐缩小的形式。
笔顺：一丨丿丶丨丶丿丨乛一一

殆dai4
危：危殆。危乎殆哉。知足不辱，知止不殆（懂得满足不贪心就不会受辱，懂得适可而止就不会遭到危险）。
大概，几乎：伤亡殆尽。
古同“怠”，懈怠。
笔顺：一丿乛丶乛丶丨乛一

瑛ying1
玉的光彩：玉有瑛华（古籍中“瑛”多作“英”）。
像玉的美石：瑛瑶。琼瑛。
笔顺：一一丨一一丨丨丨乛一丿丶

磬qing4
古代打击兵器，形状像曲尺，用玉、石制成，可悬挂。
佛寺中使用的一种钵状物，用铜铁铸成，既可作念经时的打击乐器，亦可敲响集合寺众。
缢杀：“公族其有死罪，则磬于甸人”。
古同“罄”，空，尽。
笔顺：一丨一乛丨一丿丿乛乛丶一丿丨乛一

竺zhu2
〔天竺〕印度的古称。
姓。
竺du3
古同“笃”，厚。
笔顺：丿一丶丿一丶一一

耆qi2
年老，六十岁以上的人：耆老。耆年。耆绅。耆宿（指在社会上有名望的老年人）。
强横。
耆shì
古同“嗜”，爱好。
笔顺：一丨一丿丿乛丨乛一一

荏ren3
一年生草本植物，茎方形，叶椭圆形，有锯齿，开白色小花，种子通称“苏子”，可榨油；嫩叶可食。亦称“白苏”。
柔，软弱：荏弱。荏染（柔弱的样子）。色厉内荏。
古同“戎”、“壬”，大。
笔顺：一丨丨丿丨丿一丨一

蕉jiao1
指某些有像芭蕉那样的大叶子的植物：香蕉。美人蕉。
生麻，未沤治的麻。
〔芭蕉〕见“芭”。
古同“焦”，枯焦。
笔顺：一丨丨丿丨丶一一一丨一丶丶丶丶

趺fu1
同“跗”。
〔趺坐〕佛教徒盘腿端坐的姿势。
碑下的石座：魑首龟趺。
笔顺：丨乛一丨一丨一一一丿丶

鄂e4
中国湖北省的别称。
古同“谔”，正直的话。
古同“愕”，惊讶。
古同“萼”，花托。
边界：“纷被丽而亡鄂”。
姓。
笔顺：丨乛一丨乛一一一乛乛丨

    #]]]'''
    assert 261 == len(_261),len(_261)
    return _261

hzs_261 = '亥佃佚佶侈侏侑俑俳俸倨倬偈僖剔匍匐卞咫哺喀喙嗜嗟嗣嗾噫嚆圄埴堀壑壕夙娑孺宸寤岬嵋嵌嵬巳帑幄庠廛弧怏恁悌悖悸惟愆慊慝憾懋戟戡拌掖揄揆揖撰擘攫攸敖敞斛斡斫旬昴晏暑暝暹暾曷杉枇枋枷柝桎梏梢棚椅椽椿楔楮楸楹槿樗橄橙檄檎檗殄殆汐沮沼泗洵涓淅淞淮渤渥湍湫溟溥滓漕潼濂瀑灸焙熄燔燧爻猊猩珀珂珥琢琥琵琶瑁瑚瑛瑾璋瓠瓢甄甑甥畛畦盂眄眸瞑矣碇碣磬礁祉禳秧稔稗稷窈竺筌筮筵篁粕纛翕耆肄肪胛胥脯腱膈膊膨臾舫舷艮芍芹苒茄茯茱茴茵茸荀荏莪菁菖菽葺蒡蓍蔬蕃蕉蕨薨藩蚌蚣蛟蛭蜈蝗蟠衢衾袈裟裨褥褶豌趺跏跛跣蹇蹉蹙逋逑逡逵邸郡酊酎酩酵醍醵釉陂陟隅雉雎魃麾黍黜'
    #hzs_261__content


assert hzs_261 == _mk_261(), _mk_261()


高稳定度汉字字集囗第三版囗码序囗二百六十一字 = hzs_261
    #第三版261

