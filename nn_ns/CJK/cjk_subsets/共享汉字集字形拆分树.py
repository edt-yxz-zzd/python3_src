r'''
see:
    view ../../python3_src/nn_ns/CJK/cjk_subsets/囗共享汉字集单字信息.py
    view script/collect_hz_components.py

e ../../python3_src/nn_ns/CJK/cjk_subsets/共享汉字集字形拆分树.py

copy from:
    view ../../python3_src/nn_ns/CJK/cjk_subsets/共享汉字集笔顺码.py
    .+1,$s/笔顺码/字形拆分树/g

拆字取名:
    重千里
    野里予
    伪人为
    墨黑土
    默黑犬
象形取名:
    鹿跪乳
跪乳:1.《公羊传．庄公二十四年》"腶修云乎"汉何休注:"凡贽，天子用鬯，诸侯用玉，卿用羔……羔取其执之不鸣，杀之不号，乳必跪而受之，类死义知礼者也。"后以"跪乳"喻指孝义。

from nn_ns.CJK.cjk_subsets.共享汉字集字形拆分树 import 只读囗共享汉字到字形拆分树
py -m nn_ns.app.debug_cmd   nn_ns.CJK.cjk_subsets.共享汉字集字形拆分树

py -m nn_ns.CJK.cjk_subsets.共享汉字集字形拆分树
    生成: ../../python3_src/nn_ns/CJK/cjk_subsets/共享汉字集字形拆分树.py.out.另档.cjk_common_subset_2513.汉字到字形拆分树.txt
!du -h ../../python3_src/nn_ns/CJK/cjk_subsets/共享汉字集字形拆分树.py.out.另档.cjk_common_subset_2513.汉字到字形拆分树.txt
    116K
view ../../python3_src/nn_ns/CJK/cjk_subsets/共享汉字集字形拆分树.py.out.另档.cjk_common_subset_2513.汉字到字形拆分树.txt


[[一些引起注意的地方:begin
@20220502完成初步遍览，发现不少问题

字源分解？
,'乾'
:('⿸', [('⿰', [('hz', '𠦝'), ('hz', '𠂉')]), ('hz', '乙')])
,'斡'
:('⿸', [('⿰', [('hz', '𠦝'), ('hz', '𠆢')]), ('hz', '斗')])
,'於'
:('⿰', [('hz', '方'), ('hz', '仒')])
,'施'
:('⿸', [('ref', '&U-i001+3AC3;'), ('hz', '也')])
,'修'
:('⿸', [('hz', '攸'), ('hz', '彡')])
,'哀'
:('⿴', [('hz', '衣'), ('hz', '口')])
,'存'
:('⿸', [('ref', '&CDP-88F1;'), ('hz', '子')])
,'寇'
:('⿷', [('hz', '完'), ('hz', '攴')])
,'寐'
:('⿸', [('hz', '𪧇'), ('hz', '未')])
,'斑'
:('⿴', [('hz', '玨'), ('hz', '文')])
,'班'
:('⿴', [('hz', '玨'), ('ref', '&CDP-8BEA;')])
,'羸'
:('⿵', [('hz', '𣎆'), ('hz', '羊')])
,'臧'
:('⿵', [('hz', '戕'), ('hz', '臣')])
,'虐'
:('⿸', [('hz', '虍'), ('ref', '&CDP-8DC1;')])
,'街'
:('⿴', [('hz', '行'), ('hz', '圭')])
,'辨'
:('⿴', [('hz', '辡'), ('ref', '&CDP-8BEA;')])


引用外部部件
,'亥'
:('⿳', [('hz', '亠'), ('ref', '&GT-00154;'), ('hz', '人')])
,'牝'
:('⿰', [('ref', '&CDP-8BA9;'), ('hz', '匕')])

人为边界？
,'亨'
:('⿱', [('⿱', [('hz', '亠'), ('hz', '口')]), ('hz', '了')])
,'亭'
:('⿱', [('⿳', [('hz', '亠'), ('hz', '口'), ('hz', '冖')]), ('hz', '丁')])
,'高'
:('⿵', [('⿳', [('hz', '亠'), ('hz', '口'), ('hz', '冂')]), ('hz', '口')])
,'克'
:('⿱', [('hz', '古'), ('hz', '儿')])
,'壹'
:('⿳', [('hz', '士'), ('hz', '冖'), ('hz', '豆')])
,'睿'
:('⿱', [('ref', '&GT-K01554;'), ('⿱', [('ref', '&GT-K00859;'), ('hz', '目')])])
,'索'
:('⿱', [('ref', '&CDP-8D52;'), ('hz', '糸')])
,'薨'
:('⿱', [('ref', '&A-CDP-8D60;'), ('hz', '死')])
,'黍'
:('hz', '黍')
,'黎'
:('⿱', [('hz', '𥝢'), ('ref', '&CDP-8D71;')])


偏旁不太对？
,'拜'
:('⿰', [('hz', '龵'), ('ref', '&CDP-8CE7;')])

使用部件字符而非部首汉字,⺜冃
,'先'
:('⿱', [('hz', '⺧'), ('hz', '儿')])
    #搜索: /[⺳タ具⺢⻖⺗直⺯刃⺜⺇⻀⺫𥄳⺃屮旣⺲⻏灰⺈⺊冗⺼⺧⻢穀⺣⺄⺆充⺪叟者⻞⺶⻃⺌⻤⻌]
    #   <<== view script/collect_hz_components.py
,'冒'
:('⿱', [('hz', '⺜'), ('hz', '目')])
    view script/collect_hz_components.py
    ('⺜', 'CJK RADICAL SUN')
    view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/ucd/parse__CJKRadicals_txt.py.out.ver13_0.txt
        没找到！从『⼀2f00』开始
    『⺜2e9c』
        $ echo $'\u2e9c'
            ⺜
    view /sdcard/0my_files/unzip/e_book/unicode_13__UCD/Blocks.txt
        2E80..2EFF; CJK Radicals Supplement
        2F00..2FDF; Kangxi Radicals
    view /sdcard/0my_files/unzip/e_book/unicode_13__UCD/CJKRadicals.txt
        主线:Kangxi Radicals
        副线:部分简体部件:CJK Radicals Supplement

使用部首汉字而非正字:𠆢人
,'今'
:('⿱', [('hz', '𠆢'), ('hz', '𪜊')])
    人
,'共'
:('⿱', [('hz', '龷'), ('ref', '&GT-K00059;')])
    八
,'刈'
:('⿰', [('hz', '㐅'), ('hz', '刂')])
    乂
,'栗'
:('⿱', [('hz', '覀'), ('hz', '木')])
    西
,'楞'
:('⿰', [('hz', '木'), ('⿱', [('hz', '罒'), ('hz', '方')])])
    罒四
,'茶'
:('⿳', [('hz', '艹'), ('hz', '𠆢'), ('hz', '朩')])
    木

青字底？
,'前'
:('⿸', [('⿱', [('hz', '䒑'), ('ref', '&CDP-8958;')]), ('hz', '刂')])
    没找到『青』
        hz2513实在小
        要不gb2312? 7000上下(6763个汉字，600上下其他非汉字字符)
    view ../../python3_src/nn_ns/CJK/CJK_struct/CHISE_IDS_67b94ff_20191211/basic_decomp.txt
        ,'青'
        : ('hz', '青')
        该拆不拆


使用正字而非偏旁？
,'切'
:('⿰', [('hz', '七'), ('hz', '刀')])
,'到'
:('⿰', [('hz', '至'), ('hz', '刂')])
,'叛'
:('⿰', [('hz', '半'), ('hz', '反')])
,'地'
:('⿰', [('hz', '土'), ('hz', '也')])
,'改'
:('⿰', [('hz', '己'), ('hz', '攵')])
,'攻'
:('⿰', [('hz', '工'), ('hz', '攵')])
,'社'
:('⿰', [('hz', '示'), ('hz', '土')])
,'究'
:('⿱', [('hz', '穴'), ('hz', '九')])
,'竺'
:('⿱', [('hz', '竹'), ('hz', '二')])
,'羚'
:('⿰', [('hz', '羊'), ('hz', '令')])
,'辣'
:('⿰', [('hz', '辛'), ('hz', '束')])
,'邦'
:('⿰', [('hz', '丰'), ('hz', '⻏')])
,'雪'
:('⿱', [('hz', '雨'), ('hz', '彐')])


不完全分解？
,'亢'
:('⿱', [('hz', '亠'), ('hz', '几')])
,'伉'
:('⿰', [('hz', '亻'), ('hz', '亢')])
,'冠'
:('⿱', [('hz', '冖'), ('ref', '&CDP-8DB7;')])
,'凄'
:('⿰', [('hz', '冫'), ('hz', '妻')])
,'妻'
:('⿱', [('ref', '&CDP-89E5;'), ('hz', '女')])

不一致拆分？
,'丘'
:('hz', '丘')
,'兵'
:('⿱', [('hz', '斤'), ('ref', '&GT-K00264;')])
,'名'
:('⿱', [('hz', '夕'), ('hz', '口')])
,'君'
:('⿸', [('hz', '尹'), ('hz', '口')])
,'囚'
:('⿴', [('hz', '囗'), ('hz', '人')])
,'四'
:('hz', '四')
,'坐'
:('⿻', [('hz', '土'), ('hz', '从')])
,'半'
:('hz', '半')
,'乖'
:('hz', '乖')
,'乘'
:('hz', '乘')
,'爽'
:('hz', '爽')
,'幽'
:('⿻', [('hz', '山'), ('hz', '𢆶')])
,'微'
:('⿲', [('hz', '彳'), ('hz', '𡵉'), ('hz', '攵')])
,'徽'
:('⿰', [('hz', '彳'), ('hz', '𢾰')])
,'卞'
:('⿱', [('hz', '丶'), ('hz', '下')])
,'方'
:('hz', '方')
,'甬'
:('⿱', [('hz', '龴'), ('hz', '用')])
,'矛'
:('hz', '矛')
,'薨'
:('⿱', [('ref', '&A-CDP-8D60;'), ('hz', '死')])
,'薯'
:('⿱', [('hz', '艹'), ('hz', '署')])
,'蔑'
:('⿱', [('hz', '𦭝'), ('hz', '戍')])
,'衣'
:('hz', '衣')
,'表'
:('⿱', [('hz', '龶'), ('ref', '&CDP-8B67;')])
,'哀'
:('⿴', [('hz', '衣'), ('hz', '口')])
,'袁'
:('⿱', [('hz', '𠮷'), ('ref', '&CDP-8B67;')])
,'豕'
:('hz', '豕')
,'象'
:('⿱', [('ref', '&GT-K02380;'), ('hz', '𧰨')])
,'羚'
:('⿰', [('hz', '羊'), ('hz', '令')])
,'羞'
:('⿸', [('hz', '⺶'), ('hz', '丑')])
,'金'
:('hz', '金')
,'釜'
:('⿱', [('hz', '父'), ('ref', '&CDP-8DE3;')])
,'自'
:('hz', '自')
,'血'
:('⿱', [('hz', '丿'), ('hz', '皿')])
,'白'
:('hz', '白')
,'百'
:('⿱', [('hz', '一'), ('hz', '白')])
,'面'
:('⿳', [('hz', '一'), ('hz', '丿'), ('hz', '囬')])
,'而'
:('hz', '而')






诡异的拆分？错误的拆分？
,'余'
:('⿱', [('ref', '&CDP-8AFC;'), ('hz', '朩')])
,'合'
:('⿱', [('ref', '&CDP-8AFC;'), ('hz', '口')])
,'命'
:('⿱', [('ref', '&CDP-8AFC;'), ('hz', '叩')])
,'舍'
:('⿱', [('ref', '&CDP-8AFC;'), ('hz', '古')])
,'同'
:('⿵', [('hz', '𠔼'), ('hz', '口')])
,'夙'
:('⿵', [('hz', '几'), ('hz', '歹')])
,'周'
:('⿵', [('hz', '⺆'), ('hz', '𠮷')])
,'月'
:('hz', '月')
,'后'
:('⿸', [('hz', '𠂋'), ('hz', '口')])
,'斤'
:('hz', '斤')
,'斥'
:('hz', '斥')
,'咸'
:('⿴', [('hz', '戌'), ('hz', '口')])
,'威'
:('⿵', [('hz', '戌'), ('hz', '女')])
,'戌'
:('⿵', [('hz', '戊'), ('hz', '一')])
,'戍'
:('⿵', [('hz', '戊'), ('hz', '丶')])
,'瓦'
:('hz', '瓦')
,'戎'
:('⿹', [('hz', '戈'), ('hz', '十')])
,'成'
:('⿵', [('hz', '戊'), ('hz', '𠃌')])
,'寅'
:('⿱', [('hz', '宀'), ('ref', '&CDP-8CE6;')])
,'弟'
:('⿹', [('hz', '丿'), ('hz', '弚')])
,'第'
:('⿱', [('hz', '竹'), ('⿹', [('hz', '丿'), ('hz', '弔')])])




错误的拆分:
,'咫'
:('⿸', [('hz', '尺'), ('hz', '只')])
,'善'
:('⿻', [('hz', '羊'), ('⿱', [('hz', '䒑'), ('hz', '口')])])
,'朗'
:('⿰', [('hz', '良'), ('hz', '月')])
,'甚'
:('⿱', [('ref', '&CDP-88C8;'), ('hz', '匹')])
,'虎'
:('⿸', [('hz', '虍'), ('hz', '儿')])
    几儿
,'蚩'
:('⿳', [('hz', '屮'), ('hz', '一'), ('hz', '虫')])
    屮屮
,'麻'
:('⿸', [('hz', '广'), ('ref', '&A-compU+6797;')])



拆分有歧义？
,'元'
:('⿱', [('hz', '一'), ('hz', '兀')])
,'刀'
:('hz', '刀')
,'刃'
:('⿹', [('hz', '刀'), ('hz', '丿')])
,'千'
:('hz', '千')
,'升'
:('⿱', [('hz', '丿'), ('hz', '廾')])
,'壬'
:('⿱', [('hz', '丿'), ('hz', '士')])
,'失'
:('⿰', [('hz', '丿'), ('hz', '夫')])
,'矢'
:('hz', '矢')
,'爰'
:('⿳', [('hz', '爫'), ('hz', '一'), ('hz', '友')])
,'天'
:('⿱', [('hz', '一'), ('hz', '大')])
,'夭'
:('⿱', [('hz', '丿'), ('hz', '大')])
,'干'
:('hz', '干')
,'平'
:('hz', '平')
,'年'
:('hz', '年')
,'朱'
:('⿰', [('hz', '丿'), ('hz', '未')])
,'牛'
:('hz', '牛')
,'禾'
:('hz', '禾')
,'南'
:('⿱', [('hz', '十'), ('ref', '&CDP-8BDC;')])
,'向'
:('⿵', [('ref', '&CDP-8BD6;'), ('hz', '口')])
,'商'
:('⿱', [('ref', '&CDP-8BAE;'), ('hz', '冏')])
,'高'
:('⿵', [('⿳', [('hz', '亠'), ('hz', '口'), ('hz', '冂')]), ('hz', '口')])
,'帝'
:('⿱', [('ref', '&CDP-8BEC;'), ('hz', '巾')])
,'受'
:('⿱', [('ref', '&CDP-8BB8;'), ('hz', '又')])
,'有'
:('⿱', [('hz', '𠂇'), ('hz', '月')])
,'右'
:('⿸', [('hz', '𠂇'), ('hz', '口')])
,'石'
:('hz', '石')
,'孝'
:('⿱', [('hz', '耂'), ('hz', '子')])
,'省'
:('⿱', [('hz', '少'), ('hz', '目')])
,'看'
:('⿱', [('hz', '龵'), ('hz', '目')])
,'差'
:('⿸', [('hz', '⺶'), ('hz', '工')])
,'辱'
:('⿱', [('hz', '辰'), ('hz', '寸')])
,'唇'
:('⿸', [('hz', '辰'), ('hz', '口')])
,'蜃'
:('⿸', [('hz', '辰'), ('hz', '虫')])
,'感'
:('⿱', [('hz', '咸'), ('hz', '心')])
,'愿'
:('⿸', [('hz', '原'), ('hz', '心')])
,'磨'
:('⿸', [('hz', '麻'), ('hz', '石')])
,'腐'
:('⿸', [('hz', '府'), ('hz', '肉')])
,'基'
:('⿱', [('hz', '其'), ('hz', '土')])
,'堂'
:('⿱', [('ref', '&GT-K05014;'), ('hz', '土')])
,'塞'
:('⿱', [('hz', '𡨄'), ('hz', '土')])
,'墓'
:('⿱', [('hz', '莫'), ('hz', '土')])
,'太'
:('⿵', [('hz', '大'), ('hz', '丶')])
,'奇'
:('⿱', [('hz', '大'), ('hz', '可')])
    『奇』类似『旦』，下单面包围，包围类型归类:
        全包围
        有缺口的包围:
            逆时针起讫
            ---起讫点16个:四角，每边四等分，(正方形轮廓16线段==>>16个起讫点)
            0 F E D C
            1       B
            2       A
            3       9
            4 5 6 7 8
            部件  程度     起讫
            京字头 0/4 虚覆 C0
            宝盖头 1/4 浅包 B1
            ???    2/4
            春字头 3/4 深含 93
            同字框 4/4 全罩 84
            奇/旦  0/4      48
            凶/山  3/4      1B
,'旦'
:('⿱', [('hz', '日'), ('hz', '一')])

,'奉'
:('⿱', [('ref', '&CDP-8BE9;'), ('ref', '&CDP-8BF1;')])
,'少'
:('⿱', [('hz', '小'), ('hz', '丿')])
,'彖'
:('⿱', [('hz', '彑'), ('hz', '𧰨')])
,'睾'
:('⿱', [('hz', '丿'), ('hz', '睪')])
,'血'
:('⿱', [('hz', '丿'), ('hz', '皿')])
,'自'
:('hz', '自')
,'羌'
:('⿸', [('hz', '⺶'), ('hz', '乚')])
,'出'
:('⿱', [('hz', '屮'), ('hz', '凵')])
,'雀'
:('⿱', [('hz', '小'), ('hz', '隹')])
    !???
,'食'
:('⿱', [('hz', '亽'), ('hz', '艮')])
    人良


该拆不拆
,'兜'
:('hz', '兜')
,'欠'
:('hz', '欠')
,'比'
:('hz', '比')
,'熏'
:('hz', '熏')
,'父'
:('hz', '父')
,'爻'
:('hz', '爻')
,'玄'
:('hz', '玄')
,'率'
:('hz', '率')
,'石'
:('hz', '石')
,'示'
:('hz', '示')
,'穴'
:('hz', '穴')
,'立'
:('hz', '立')
,'竹'
:('hz', '竹')
,'羽'
:('hz', '羽')
,'老'
:('hz', '老')
,'舛'
:('hz', '舛')
,'色'
:('hz', '色')
,'衣'
:('hz', '衣')
,'角'
:('hz', '角')
,'谷'
:('hz', '谷')
,'豆'
:('hz', '豆')
,'赤'
:('hz', '赤')
,'辛'
:('hz', '辛')
,'邑'
:('hz', '邑')
,'重'
:('hz', '重')
,'金'
:('hz', '金')
,'阜'
:('hz', '阜')
,'非'
:('hz', '非')
,'革'
:('hz', '革')
,'音'
:('hz', '音')
,'首'
:('hz', '首')
,'骨'
:('hz', '骨')
,'鹿'
:('hz', '鹿')
,'黍'
:('hz', '黍')
,'鼠'
:('hz', '鼠')



注意形近偏旁:𠤎匕
,'化'
:('⿰', [('hz', '亻'), ('hz', '𠤎')])
,'北'
:('⿰', [('ref', '&CDP-8BC5;'), ('hz', '匕')])
,'肌'
:('⿰', [('hz', '⺼'), ('hz', '几')])
,'肖'
:('⿱', [('hz', '⺌'), ('ref', '&CDP-8958;')])
,'肩'
:('⿸', [('hz', '户'), ('ref', '&CDP-8958;')])
]]一些引起注意的地方:end



笔划相通:
    撇捺点竖/竖钩
        竖->点:竹竿，高膏，雨露
        捺->点:林
        点->撇:宝盖头，点，户所，惜
        竖->竖钩:寨
    横提:牛犊
    只有:横/竖/折 三类笔划

部件命名:
    提手
    拜手
    看手
    暴水
    益水
    海水
    恭心
    忧心
    点火/黑火
    炊火/烧火
    青月/背月
    腊月#？肉月
    冒日？冒头
    寨木
    树木
    罪四
    要西
    改己
    切七
    顷七
    化七
    老七
    旨七
    北七
    素丝
    羔羊
    羚羊
    羞羊
    船舟
    雷雨
    雪山
    虐山
    隶山
    衰中/衰日？
    踏足
    部耳#邑
    队耳#阜



#'''

__all__ = '''
    只读囗共享汉字到字形拆分树

    只读囗平凡繁简囗初步缩减囗共享汉字到字形拆分树
    只读囗初步缩减囗共享汉字到字形拆分树
    只读囗平凡繁简囗共享汉字到字形拆分树
    '''.split()

from seed.abc.abc__ver0 import override
from seed.helper.IConfig4load_versioned_repr_txt_file import IConfig4load_versioned_repr_txt_file
from seed.tiny_.pprint4container__depth1 import pprint4container__depth1, show5pprint
from seed.tiny import MapView
from nn_ns.CJK.CJK_struct.CHISE_IDS_67b94ff_20191211.load_parse_result___CHISE_IDS import load_hz2tree___BMP_only, load_hz2tree___ipath, hz2mutable_tree__to__hz2immutable_tree, hz2mutable_tree__from__hz2immutable_tree, mutable_tree2immutable, mutable_tree5immutable

#[[[
#view ../../python3_src/seed/helper/IConfig4load_versioned_repr_txt_file.py
class Config4load_subset_result_file4汉字到字形拆分树(IConfig4load_versioned_repr_txt_file):
    r'''
    readonly_dataobj = MapView<hz2immutable_tree>
        #只读囗另档囗汉字到字形拆分树
    dataobj = hz2immutable_tree
        #另档囗汉字到字形拆分树
        #children :: tuple<tree>
        #subset_result of 汉字到字形拆分树
    st = hz2mutable_tree
        #children :: list<tree>
        #为何st与dataobj不同？主要是满足:
            def _mk4dump_by_name():
                if not {**只读囗另档囗汉字到字形拆分树} == 另档囗汉字到字形拆分树: raise logic-err

    ----:
    sf.dataobj_immutable = False
    sf.state_immutable = False
    #'''
    def __init__(sf, /, *, __file__, data_dir_rpath, basename_fmt, version_str__rex, encoding):
        dataobj_immutable = False
        state_immutable = False
        super().__init__(__file__=__file__, data_dir_rpath=data_dir_rpath, basename_fmt=basename_fmt, version_str__rex=version_str__rex, encoding=encoding, dataobj_immutable=dataobj_immutable, state_immutable=state_immutable)
    @override
    def state2dataobj___create(sf, st, /):
        #.state5dataobj___save
        hz2mutable_tree = st
        hz2immutable_tree = hz2mutable_tree__to__hz2immutable_tree(hz2mutable_tree)
        dataobj = hz2immutable_tree
        return dataobj
    @override
    def check_extra_input4dump(sf, /):
        'can be overrided as: def check_extra_input4dump(sf, /, *args4dump, **kwargs4dump): #check len/keys #same as state5dataobj___save'
        #.state5dataobj___save
        pass

    @override
    def state5dataobj___save(sf, dataobj, /):
        'can be overrided as: def state5dataobj___save(sf, dataobj, /, *args4dump, **kwargs4dump):'
        #.check_extra_input4dump
        #.state2dataobj___create
        hz2immutable_tree = dataobj
        hz2mutable_tree = hz2mutable_tree__from__hz2immutable_tree(hz2immutable_tree)
        st = hz2mutable_tree
        return st




    @override
    def text5state___repr(sf, st, /):
        'can be overrided as: def text5state___repr(sf, st, /, *args4repr, **kwargs4repr):'
        #.text2state___eval
        #.check_extra_input4repr

        #汉字到字形拆分树 = st
        hz2mutable_tree = st
        txt = show5pprint('fout', pprint4container__depth1, hz2mutable_tree)

        return txt
    @override
    def check_extra_input4repr(sf, /):
        'can be overrided as: def check_extra_input4repr(sf, /, *args4repr, **kwargs4repr): #check len/keys #same as text5state___repr'
        #.text5state___repr
        pass



    @override#to avoid RecurView4Seq
    def dataobj2readonly___recur_view(sf, dataobj, /):
        #.dataobj5readonly___literal_rebuild
        'dataobj -> readonly_dataobj'
        #result_readonly=True
        readonly_dataobj = MapView(dataobj)
        return readonly_dataobj

_cfg = Config4load_subset_result_file4汉字到字形拆分树(
    __file__            =__file__
    ,data_dir_rpath     ='./'
    ,basename_fmt       ='共享汉字集字形拆分树.py.out.另档.{}.汉字到字形拆分树.txt'
    ,version_str__rex   =r'^cjk_common_subset_[0-9]+(?:_trivial_TS_[0-9]+)?$'
    ,encoding           ='utf8'
    )
#]]]




def _mk4dump_by_name():
    #另档 的 目的 在于『避免加载nn_ns.CJK.CJK_struct.CHISE_IDS_67b94ff_20191211.parse_result___CHISE_IDS::hz2tree___BMP_only』
    #   因此，只有 _main()使用 _mk4dump_by_name()
    #
    from seed.mapping_tools.dict_op import subset_keys__immutable
    import nn_ns.CJK.cjk_subsets.hanzi as hanzi_lib
    from nn_ns.CJK.cjk_subsets.hanzi import hz_sp_str2hz_set
    from nn_ns.CJK.CJK_struct.CHISE_IDS_67b94ff_20191211.parse_result___CHISE_IDS import hz2tree___BMP_only as 汉字到字形拆分树 #readonly__hz2tree #MapView+tuple children
    ######################
    def _gen(hz_sp_str, /):
        hz_set = hz_sp_str2hz_set(hz_sp_str)
        另档囗汉字到字形拆分树 = subset_keys__immutable(汉字到字形拆分树, hz_set)
        return 另档囗汉字到字形拆分树
    ######################
    def _gen_by_name(汉字字集名, /):
        if not 汉字字集名 in hanzi_lib.__all__:raise ValueError(汉字字集名)
        带空格汉字字集 = getattr(hanzi_lib, 汉字字集名)
        if not type(带空格汉字字集) is str: raise TypeError(汉字字集名)

        另档囗汉字到字形拆分树 = _gen(带空格汉字字集)
        return 另档囗汉字到字形拆分树
    def _dump_by_name(汉字字集名, /, force, may_path_bypass_version_str):
        #force=False, may_path_bypass_version_str=None
        另档囗汉字到字形拆分树 = _gen_by_name(汉字字集名)
        version_str = 汉字字集名
        _cfg.dump_data_file__ver(version_str, 另档囗汉字到字形拆分树, force=force, args4repr=[], kwargs4repr={}, args4dump=[], kwargs4dump={}, is_readonly_dataobj=False, may_path_bypass_version_str=may_path_bypass_version_str)
        只读囗另档囗汉字到字形拆分树 = load_readonly_by_name(version_str, may_path_bypass_version_str=may_path_bypass_version_str)
        try:
            if not {**只读囗另档囗汉字到字形拆分树} == 另档囗汉字到字形拆分树: raise logic-err
        except:
            def f(hz2tree, /):
                print(len(hz2tree))
                print(repr(hz2tree['林']))
            f(只读囗另档囗汉字到字形拆分树)
                #RecurView4Seq(None, ('⿰', (('hz', '木'), ('hz', '木'))))
            f(另档囗汉字到字形拆分树)
                #('⿰', (('hz', '木'), ('hz', '木')))
            #==>> override:dataobj2readonly___recur_view
            raise
        return

    return _dump_by_name
def load_readonly_by_name(汉字字集名, /, may_path_bypass_version_str):
    'FileNotFoundError'
    version_str = 汉字字集名
    只读囗另档囗汉字到字形拆分树 = _cfg.load_data_file__ver(version_str, deepcopy_on_cached_state=False, result_readonly=True, may_path_bypass_version_str=may_path_bypass_version_str)
    return 只读囗另档囗汉字到字形拆分树





def _main():
    #另档 的 目的 在于『避免加载nn_ns.CJK.CJK_struct.CHISE_IDS_67b94ff_20191211.parse_result___CHISE_IDS::hz2tree___BMP_only』
    #   因此，只有 _main()使用 _mk4dump_by_name()
    #
    'FileExistsError'
    _dump_by_name = _mk4dump_by_name()

    汉字字集名 = 'cjk_common_subset_2513'
    _dump_by_name(汉字字集名, force=False, may_path_bypass_version_str=None)


def _load():
    def recur():
        try:
            只读囗共享汉字到字形拆分树 = load_readonly_by_name('cjk_common_subset_2513', may_path_bypass_version_str=None)
        except FileNotFoundError:
            _main()
                # FileExistsError
            return recur()
        return 只读囗共享汉字到字形拆分树
    return recur()
只读囗共享汉字到字形拆分树 = _load()
if __name__ == "__main__":
    pass


from nn_ns.CJK.cjk_subsets.共享汉字集字形拆分树 import 只读囗共享汉字到字形拆分树

######################


