#__all__:goto
r'''[[[
e ../../python3_src/seed/for_libs/for_colorsys/_mk4color_table_html.py
    e html_js/html/try_table.html
    view  ../../python3_src/seed/for_libs/for_colorsys/color_table.html


py -m seed.for_libs.for_colorsys._mk4color_table_html
py -m nn_ns.app.debug_cmd   seed.for_libs.for_colorsys._mk4color_table_html -x
py -m nn_ns.app.doctest_cmd seed.for_libs.for_colorsys._mk4color_table_html:__doc__ -ht
py_adhoc_call   seed.for_libs.for_colorsys._mk4color_table_html   @f
from seed.for_libs.for_colorsys._mk4color_table_html import *

RGB Tool:com.fastebro.androidrgbtool
    RGB,HSB
    即py.HSV
        view ../../python3_src/py_stdlib_api.txt
            colorsys.rgb_to_hsv()
                v-
        # HSV: Hue, Saturation, Value
        # H: position in the spectrum
        # S: color saturation ("purity")
        # V: color brightness
        H:色相/色调
            #HSV,HLS两者色相相同
            三基色环形色谱中的位置
        S:饱和度
            #HSV,HLS两者饱和度不同
            (max(r,g,b)-min(r,g,b)) /max(r,g,b)
        V:亮度
            max(r,g,b)

[[[
===
<script>
/*
colors
表格:纵向三基色圆，横向共同色/白色
单、双、主辅
ACC,AAC,ABC
ABC-->210 420 432
:       000------------->444
ACC:400     200 400 422
ABC:420     210 420 432
AAC:440     220 440 442
BAC:240     120 240 342
CAC:040     020 040 242
CAB:042     021 042 243
CAA:044     022 044 244
CBA:024     012 024 234
CCA:004     002 004 224
BCA:204     102 204 324
ACA:404     202 404 424
ACB:402     201 402 423
ACC:400     200 400 422
:           c/2 c   c/2+222

<table><tr><th>
<table><tr><td>

!cp -i html_js/html/try_table.html  ../../python3_src/seed/for_libs/for_colorsys/color_table.html
view  ../../python3_src/seed/for_libs/for_colorsys/color_table.html
!diff html_js/html/try_table.html  ../../python3_src/seed/for_libs/for_colorsys/color_table.html

e html_js/html/try_table.html
view  ../../python3_src/seed/for_libs/for_colorsys/color_table.html

TODO:三基色圆弧度/主从，亮度，白色占比
light亮/浅shallow
pale淡
dark暗/浓/深deep


e html_js/html/try_table.html
    xxx: /sdcard/0my_files/git_repos/python3_src/seed/for_libs/for_colorsys/color_table.html.screenshot.jpg
    /sdcard/0my_files/img/color_table.html.screenshot.jpg

中间色:私命名:
#888:灰色:黑色-白色
#f00:红色:赭色-粉色
#f80:橙色:褐色-色
#ff0:黄色:-藕色
#8f0:幼色:-饥色
#0f0:绿色:碧色-惨色
#0f8:萤色
#0ff:青色
#08f:蔚色
#00f:蓝色
#80f:紫色
#f0f:绛色:棕色-
#f08:粉色:栗色-
#f00:红色:赭色-



褐色/棕色/茶色/咖啡色
    brown
栗色
    chestnut (color); maroon; sorrel; chestnut brown

[[[
view /sdcard/0my_files/tmp/out4py/汉语字典囗.py..nn_ns.fileformat.sqlite3_dump_cmd.out.txt
:read !fgrep 色 /sdcard/0my_files/tmp/out4py/汉语字典囗.py..nn_ns.fileformat.sqlite3_dump_cmd.out.txt
    vim.grep似乎有毛病，表达式含汉字 不能得到预期效果，只有fgrep还行
grep '\w色' /sdcard/0my_files/tmp/out4py/汉语字典囗.py..nn_ns.fileformat.sqlite3_dump_cmd.out.txt -o | grep '[一三两之九于五令似体作侔侧候倦光六其减出印厉原变各品喜墨声多天失女好姿容寒山异彩影怒怡悦惧惭愠愧成或捎掉掷改斑无日春景暖暗暝暮曙月有服本杂染正气润深渔物特画的眼着神秀等纯绝美而肤脸行角货起足退逊酒重面音颜]色' -v | sort -u
木色
朱色
柳色
栗色
棕色
榄色
毛色
火色
灰色
玉色
瑁色
白色
皮色
碧色
竹色
粉色
紫色
縹色
红色
绘色
绛色
绿色
艾色
节色
花色
草色
菜色
蓝色
藕色
褐色
赤色
赭色
遽色
部色
配色
金色
铜色
银色
锖色
霁色
青色
鱍色
鸟色
鸢色
黄色
黑色
黛色



grep '\w[木朱柳栗棕榄毛火灰玉瑁白皮碧竹粉紫縹红绘绛绿艾节花草菜蓝藕褐赤赭遽部配金铜银锖霁青鱍鸟鸢黄黑黛]色' /sdcard/0my_files/tmp/out4py/汉语字典囗.py..nn_ns.fileformat.sqlite3_dump_cmd.out.txt -o | grep '^.' -o | sort -u

丝中乳云土墨天子季微暗木朱材栗桃棕橄橘橙浅淡深澄火灰焦玳理类粉紫红纯绛绿缘肉脂脊花苍茶蓝褐赤蹄金银间青靛鱍鲜黄黑
grep '\w[木朱柳栗棕榄毛火灰玉瑁白皮碧竹粉紫縹红绘绛绿艾节花草菜蓝藕褐赤赭遽部配金铜银锖霁青鱍鸟鸢黄黑黛]色' /sdcard/0my_files/tmp/out4py/汉语字典囗.py..nn_ns.fileformat.sqlite3_dump_cmd.out.txt -o | grep '^[^一上下为于以体作做内出制及古呈和声壳多大实容尖尾层带开心成或指按时是有条果枝染根此比毛泌然状用的皮种级股背脚脸腹茎虫装见身部面项颊额髓]' | sort -u
丝黄色
中黑色
乳白色
云黑色
土黄色
墨绿色
天黄色
子棕色
子白色
子红色
子黄色
子黑色
季节色
微红色
暗红色
暗绿色
暗蓝色
暗褐色
暗黄色
暗黑色
木花色
朱红色
材白色
材黄色
栗棕色
栗红色
桃红色
棕绿色
棕褐色
棕黄色
棕黑色
橄榄色
橘红色
橘黄色
橙红色
橙黄色
浅灰色
浅白色
浅碧色
浅红色
浅绛色
浅蓝色
浅黄色
浅黑色
淡白色
淡紫色
淡红色
淡绿色
淡蓝色
淡褐色
淡黄色
深棕色
深红色
深绿色
深蓝色
深褐色
深青色
深黑色
澄黄色
火红色
灰棕色
灰白色
灰绿色
灰褐色
灰黄色
灰黑色
焦黄色
玳瑁色
理白色
类黄色
粉红色
紫白色
紫红色
紫赤色
紫青色
紫黑色
红棕色
红紫色
红褐色
红黄色
红黑色
纯黑色
绛红色
绿白色
绿褐色
缘红色
肉白色
肉黄色
脂黄色
脊黄色
花白色
花紫色
花红色
花黄色
苍白色
苍绿色
苍艾色
苍黑色
茶褐色
蓝白色
蓝紫色
蓝绿色
蓝褐色
蓝黑色
褐绿色
褐黄色
赤褐色
赤黄色
赤黑色
蹄白色
金黄色
银灰色
银白色
间白色
青灰色
青白色
青紫色
青绿色
青蓝色
青褐色
青赤色
青黄色
青黑色
靛蓝色
鱍鱍色
鲜红色
鲜黄色
黄白色
黄绿色
黄褐色
黄赤色
黄黑色
黑红色
黑绿色
黑蓝色
黑褐色
黑黄色


===
===
]]]
[[[
view /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词典-词汇繁简对照-补空.txt
:read !fgrep '色:' /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词典-词汇繁简对照-补空.txt
    531行

grep '\(黯色\|貝色\|惫色\|表色\|菜色\|茶色\|赤色\|黛色\|蛋青色\|妃色\|粉色\|服色\|古铜色\|鹄色\|贵色\|湖色\|壞色\|晦色\|火色\|酱色\|菫色\|骊色\|栗色\|练色\|柳色\|卵色\|麻灰色\|玫瑰色\|米色\|祕色\|蜜合色\|蜜色\|冥色\|木紅色\|藕色\|縹色,缥色\|铅色\|锖色\|青色\|青生色\|秋香色\|肉色\|閃色\|沈香色\|霜色\|水色\|死色\|松花色\|素色\|桃色\|铁色\|驼色\|香色\|猩色\|玄色\|雪色\|血色\|鸦色\|牙色\|煙色\|银色\|莺背色\|鹰脖色\|玉色\|元色\|中色\|棕色\|醉楊妃色\)' /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词典-词汇繁简对照-补空.txt | grep ':.'
貝色:贝色
憊色:惫色
古銅色:古铜色
鵠色:鹄色
鵠形菜色:鹄形菜色
貴色:贵色
壞色:坏色
醬色:酱色
金聲玉色:金声玉色
驪色:骊色
練色:练色
柳色黃:柳色黄
祕色:秘色
木紅色:木红色
鉛色:铅色
錆色:锖色
閃色:闪色
桃色新聞:桃色新闻
鐵色:铁色
駝色:驼色
鴉色:鸦色
煙色:烟色
銀色:银色
鶯背色:莺背色
鷹脖色:鹰脖色
鳶肩火色:鸢肩火色
棕色人種:棕色人种
醉楊妃色:醉杨妃色

===
]]]
[[[
more /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词典-初步清理.txt
grep '色$' /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词典-初步清理.txt -A 1 | more
grep '色$' /sdcard/0my_files/tmp/out4py/script.欧路词典囗.试读囗囗假设简介字节数地址固定囗.汉语大辞典.out.词典-初步清理.txt -A 1 >  /sdcard/0my_files/tmp/out4grep/grep..色.-A1..汉语大辞典.词典-初步清理..out.txt
view  /sdcard/0my_files/tmp/out4grep/grep..色.-A1..汉语大辞典.词典-初步清理..out.txt
===
黯色
貝色
惫色
表色:取、捨、屈、伸，是名表色。
菜色:飢色
茶色:茶色玻璃:茶褐色
赤色:红色
黛色:青黑色
蛋青色:鸭蛋壳青
妃色:緋色，淡紅色
粉色:白色、粉紅色
服色:改正朔，易服色#遷正黜色
古铜色:深褐色
鹄色:白色
贵色:白色
湖色:淡綠色
壞色:律有三種壞色：青、黑、木蘭。青謂銅青，黑謂雜泥，木蘭即樹皮也。
晦色:變為昏暗之色。亦指暗色。
火色:似火的顏色，指赤紅色。
酱色:深赭色
-棗紅
菫色:淺紫色
骊色:黑色
栗色:像栗子殼般的顏色。
练色:白色
柳色:綠色
卵色:蛋青色
麻灰色:灰色中帶麻點
玫瑰色:淡紫紅色
米色:白而帶淺黃的顏色
祕色:秘色:古代越州官窯所產磁器的顏色。因為帝王所專用，故云。
蜜合色:微黃帶紅的顏色
蜜色:像蜂蜜那樣的顏色；淡黃色。
冥色:淺黑色
木紅色:染色之一種
藕色:淺灰而微紅的顏色
縹色,缥色:淡青色#?竹葉青
铅色:青灰色
锖色:某些礦物表面因氧化作用而形成的薄膜所呈現的色彩，常常不同於礦物固有的顏色。
青色:1.東方之色，春色。2.黑色。
青生色:嫩青色
秋香色:暗黃色
-雨過天青，秋香色，松綠，銀紅。
肉色:淺黃中帶紅的顏色。
閃色:闪色:指織物通過采用對比強烈的異色經緯來取得的顏色。有深青閃大紅、紅閃綠、紅閃青、豆青閃紅等品種。亦指閃緞。
-豆青
沈香色:沉香色:黃黑色
霜色:白色
水色:1.淡青色，接近白色。2.黑色
死色:蒼白灰暗的顏色。
松花色:如松花般的嫩黃色。
素色:白色
桃色:粉紅色
铁色:像鐵一樣的顏色
驼色:像駱駝毛那樣的淺棕色
香色:茶褐色
猩色:鮮紅色。色如猩猩之血，故稱。
玄色:黑裡帶微赤的顏色。
雪色:白色
血色:暗赤或鮮紅的顏色。
鸦色:鴉青色；暗青色。
牙色:與象牙相似的淡黃顏色。
煙色:指暗黃色或深棕色。
银色:銀白色
莺背色:淺黃帶綠的顏色。
鹰脖色:灰白色
玉色:1.瑩白色。2.繪畫上稱粉綠色為玉色。
元色:即玄色，黑色。
中色:中央之色，即黃色。
棕色:像棕毛一樣的顏色。#红褐色
醉楊妃色:粉紅色
===
棕毛?红褐色
锈色?红褐色
赭色?红褐色
    赭褐:栗殼色。
    赭红:红褐色
    赭黄:1.土黃色。2.指黃中帶赤的顏色。
褐色?黃黑色。
    像栗子皮那样的颜色：褐铁矿。

===
===
閒色:闲色
:<B>閒色</B><DIV><DIV>(閒色,闲色)<BR>亦作“間色”。<BR>1.雜色，與正色相對。<NB>《禮記‧玉藻》：“衣正色，裳閒色。”<NB>鄭玄注：“謂冕服玄上纁下。”<NB>孔穎達疏：“玄是天色，故為正；纁是地色，赤黃之雜，故為閒色。<NB>皇氏云：‘正謂青、赤、黃、白、黑五方正色也；不正，謂五方閒色也，綠、紅、碧、紫、騮黃是也。’”<NB>《太平御覽》卷八一四引《環濟要略》：“間色有五，謂紺、紅、縹、紫、流黃也。”<BR>2.指五行相克之色。五行相生之序為木生火、火生土、土生金、金生水、水生木。相克之序則間隔一行，為木克土、火克金、土克水、金克木、水克火。這種規律稱為“比相生，間相克”，故稱“閒色”。色，指五行之色，如木為青色、火為赤色等。<NB>明楊慎《丹鉛總錄‧訂訛‧五行間色》：“五行之理，有相生者，有相克者。相生為正色，相克為間色。”<BR>3.兩種原色相互混合而成的顏色。也叫“第二次色”。如紅黃混合成橙色，黃青混合成綠色，青紅混合成紫色。</DIV></DIV>
綠、紅、碧、紫、騮黃
紺、紅、縹、紫、流黃
相互混合而成的顏色。也叫“第二次色”。如紅黃混合成橙色，黃青混合成綠色，青紅混合成紫色。


闲色=>:
,三原色
:<B>三原色</B><DIV><DIV>1.光學中指紅、綠、藍三種波長的光波。光譜中的各種色光都可以由這三種光波複合而成。<BR>2.顏料或染料中指紅、黃、藍三色。這三種顏色或染料按不同比例混合後，可以合成任何一種顏色。</DIV></DIV>
紅、綠、藍
紅、黃、藍

基色==原色
,原色
:<B>原色</B><DIV><DIV>1.原野的景色。<NB>唐張籍《送安法師》詩：“原色不分路，錫聲遙隔塵。”<BR>2.也叫基色。能配合成各種顏色的基本顏色。顏料中的原色是紅、黃、藍，藍和黃可以配合成綠，紅和藍可以配合成紫。色光中的原色是紅、綠、藍，紅和綠可以配合成黃，紅和藍可以配合成紫。</DIV></DIV>

,套色
:<B>套色</B><DIV><DIV>彩印方法。用平版或凸版分次印刷，每次印一種顏色。利用紅、黃、藍三種原色重疊印刷，可以印出各種顏色。<NB>阿英《民元以前的中國年畫發展概貌》：“石印興起後，桃花塢、楊柳青，都曾改用石印，或套色，或敷彩，也有較好的作品。”</DIV></DIV>
紅、黃、藍


,九色
:<B>九色</B><DIV><DIV>1.九種顏色。<NB>《三國志‧魏志‧烏丸鮮卑東夷傳論》裴松之注引《魏略‧西戎傳》：“﹝大秦國﹞山出九色次玉石，一曰青，二曰赤，三曰黃，四曰白，五曰黑，六曰綠，七曰紫，八曰紅，九曰紺。今伊吾山中有九色石，即其類。”<BR>2.泛指多種色彩。<NB>唐張籍《同嚴給事聞唐昌觀玉藻近有仙過》詩：“九色雲中紫鳳車，尋仙來到洞仙家。”<NB>元虞集《記夢中》詩：“出海雲霞九色芒，金容滉漾水中央。”</DIV></DIV>
一曰青，二曰赤，三曰黃，四曰白，五曰黑，六曰綠，七曰紫，八曰紅，九曰紺。


,六色
:<B>六色</B><DIV><DIV>謂青、白、赤、黑、玄、黃六色。<NB>《周禮‧考工記‧畫繢》：“畫繢之事，雜五色，東方謂之青，南方謂之赤，西方謂之白，北方謂之黑，天謂之玄，地謂之黃。青與白相次也，赤與黑相次也，玄與黃相次也。”<NB>鄭玄注：“此言畫繢六色，所象及布，采之第次，繢以為衣。”<NB>《儀禮‧覲禮》：“方明者，木也，方四尺，設六色：東方青，南方赤，西方白，北方黑，上玄，下黃。”</DIV></DIV>
青、白、赤、黑、玄、黃

,七色
:<B>七色</B><DIV><DIV>1.紅、橙、黃、綠、藍、靛、紫七種顏色。亦泛指多種顏色。<NB>南朝梁江淹《構象臺詞》：“雲八重兮七色，山十影兮九形。”<BR>2.七類。</DIV></DIV>
紅、橙、黃、綠、藍、靛、紫

,五方色
:<B>五方色</B><DIV><DIV>古代以青、赤、黃、白、黑五色分別代表東、南、中、西、北五方。<NB>《論語‧陽貨》“惡紫之奪朱也”南朝梁皇侃疏：“謂青、赤、黃、白、黑，五方正色。不正謂五方間色，綠、紅、碧、紫、騮黃色是也。”<NB>《通典‧兵二》：“旗身旗腳，但取五方色，迴互為之。”</DIV></DIV>
青、赤、黃、白、黑

,玄色
:<B>玄色</B><DIV><DIV>1.黑裡帶微赤的顏色。<NB>《周禮‧考工記‧鍾氏》“五入為緅，七入為緇”漢鄭玄注：“凡玄色者，在緅緇之間，其六入者與？”<BR>2.泛指黑色。<NB>魯迅《吶喊‧藥》：“一個滿臉橫肉的人，披一件玄色布衫，散着紐扣。”</DIV></DIV>


显色+形色+表色
,顯色
:<B>顯色</B><DIV><DIV>(顯色,显色)<BR>1.鮮明的色彩。<NB>章炳麟《國家論》：“凡言色者，當分為三：青黃赤白，是名顯色；曲直方圓，是名形色；取捨屈伸，是名表色。”<BR>2.紡織品以某些染料染色時，使染料(或染料中間體)發生化學變化而呈現預期色澤的處理過程。</DIV></DIV>


,音色
:<B>音色</B><DIV><DIV>聲音的屬性之一，主要由其諧音的多寡及各諧音的相對強度所決定。也稱音品、音質。每個人的聲音以及各種樂器所發出的聲音的區別，就是由音色不同造成的。</DIV></DIV>

,幼色
:<B>幼色</B><DIV><DIV>指美少年。<NB>《大戴禮記‧用兵》：“疏遠國老，幼色是與。”<NB>盧辯注：“言疏遠老成而與幼色者，若楚恭王遠申叔時而用子反也。”</DIV></DIV>

[[
棕毛

现代汉语词典
zōngmáo
棕榈树叶鞘的纤维，包在树干外面，红褐色，可以制蓑衣、绳索、刷子等物品。

汉语大辞典
棕毛
1.棕絲的俗稱。棕櫚樹葉鞘的纖維，紅褐色，堅韌而具彈性，是編結蓑衣、繩索等的原料。
 《中國的土特產‧棕》：“棕絲俗稱棕毛，乃由棕片中抽出之纖維。”
2.元上都別殿的通稱。又稱棕殿，因用棕毛以代陶瓦，故稱。
]]

===
]]]










三十九色里只有十五个颜色有命名<<==:
txt4jr2jc2color===:
[["#000","#888","#fff"]
,["#800","#f00","#f88"]
,["#840","#f80","#fc8"]
,["#880","#ff0","#ff8"]
,["#480","#8f0","#cf8"]
,["#080","#0f0","#8f8"]
,["#084","#0f8","#8fc"]
,["#088","#0ff","#8ff"]
,["#048","#08f","#8cf"]
,["#008","#00f","#88f"]
,["#408","#80f","#c8f"]
,["#808","#f0f","#f8f"]
,["#804","#f08","#f8c"]
,["#800","#f00","#f88"]
]

.,.+16s/ff/ffff/g
.+1,.+14s/[048c]/\00/g
[["#000000","#808080","#ffffff"]
,["#800000","#ff0000","#ff8080"]
,["#804000","#ff8000","#ffc080"]
,["#808000","#ffff00","#ffff80"]
,["#408000","#80ff00","#c0ff80"]
,["#008000","#00ff00","#80ff80"]
,["#008040","#00ff80","#80ffc0"]
,["#008080","#00ffff","#80ffff"]
,["#004080","#0080ff","#80c0ff"]
,["#000080","#0000ff","#8080ff"]
,["#400080","#8000ff","#c080ff"]
,["#800080","#ff00ff","#ff80ff"]
,["#800040","#ff0080","#ff80c0"]
,["#800000","#ff0000","#ff8080"]
]

view  ../../python3_src/seed/for_libs/for_colorsys/color_names_impl/colors_in_css2_1.py
colors_in_css2_1 = {
    'aqua': '#00ffff',
    'black': '#000000',
    'blue': '#0000ff',
    'fuchsia': '#ff00ff',
    'gray': '#808080',
    'green': '#008000',
    'lime': '#00ff00',
    'maroon': '#800000',
    'navy': '#000080',
    'olive': '#808000',
    xxx 'orange': '#ffaa00',
    'purple': '#800080',
    'red': '#ff0000',
    xxx 'silver': '#c0c0c0',
    'teal': '#008080',
    'white': '#ffffff',
    'yellow': '#ffff00'
    }
  排除2个:
    'orange': '#ffaa00',
    'silver': '#c0c0c0',
  15=17-2

:read !grep '\<\(000000\|808080\|ffffff\|800000\|ff0000\|ff8080\|804000\|ff8000\|ffc080\|808000\|ffff00\|ffff80\|408000\|80ff00\|c0ff80\|008000\|00ff00\|80ff80\|008040\|00ff80\|80ffc0\|008080\|00ffff\|80ffff\|004080\|0080ff\|80c0ff\|000080\|0000ff\|8080ff\|400080\|8000ff\|c080ff\|800080\|ff00ff\|ff80ff\|800040\|ff0080\|ff80c0\)\>' -r ../../python3_src/seed/for_libs/for_colorsys/color_names_impl/ -h --exclude-dir=__pycache__ -o -i
  156 lines
  『v』 --> select --> 『u』/小写化字母
:.,.+155sort u
  排序并归一化
  15=156-141
000000
000080
0000ff
008000
008080
00ff00
00ffff
800000
800080
808000
808080
ff0000
ff00ff
ffff00
ffffff

==>>三十九色里只有十五个颜色有命名:here
39==15+24
15:
\<\(000000\|000080\|0000ff\|008000\|008080\|00ff00\|00ffff\|800000\|800080\|808000\|808080\|ff0000\|ff00ff\|ffff00\|ffffff\)\>
24:
\<\(ff8080\|804000\|ff8000\|ffc080\|ffff80\|408000\|80ff00\|c0ff80\|80ff80\|008040\|00ff80\|80ffc0\|80ffff\|004080\|0080ff\|80c0ff\|8080ff\|400080\|8000ff\|c080ff\|ff80ff\|800040\|ff0080\|ff80c0\)\>

:.+1,.+15sort u
15已命名颜色:
15_named_colors:begin
000000
000080
0000ff
008000
008080
00ff00
00ffff
800000
800080
808000
808080
ff0000
ff00ff
ffff00
ffffff
15_named_colors:end

:.+1,.+24sort u
24未命名颜色:
24_unamed_colors:begin
004080
008040
0080ff
00ff80
400080
408000
800040
8000ff
804000
8080ff
80c0ff
80ff00
80ff80
80ffc0
80ffff
c080ff
c0ff80
ff0080
ff8000
ff8080
ff80c0
ff80ff
ffc080
ffff80
24_unamed_colors:end
其中中间色6个:
0080ff~007fff
00ff80~00ff7f
8000ff~7f00ff
80ff00~7fff00
ff0080~ff007f#只有这个不存在??
ff8000~ff7f00

.+1,.+14s/40/3f/g
.+1,.+14s/80/7f/g
.+1,.+14s/c0/bf/g
[["#000000","#7f7f7f","#ffffff"]
,["#7f0000","#ff0000","#ff7f7f"]
,["#7f3f00","#ff7f00","#ffbf7f"]
,["#7f7f00","#ffff00","#ffff7f"]
,["#3f7f00","#7fff00","#bfff7f"]
,["#007f00","#00ff00","#7fff7f"]
,["#007f3f","#00ff7f","#7fffbf"]
,["#007f7f","#00ffff","#7fffff"]
,["#003f7f","#007fff","#7fbfff"]
,["#00007f","#0000ff","#7f7fff"]
,["#3f007f","#7f00ff","#bf7fff"]
,["#7f007f","#ff00ff","#ff7fff"]
,["#7f003f","#ff007f","#ff7fbf"]
,["#7f0000","#ff0000","#ff7f7f"]
]
\<\(ff7f7f\|7f3f00\|ff7f00\|ffbf7f\|ffff7f\|3f7f00\|7fff00\|bfff7f\|7fff7f\|007f3f\|00ff7f\|7fffbf\|7fffff\|003f7f\|007fff\|7fbfff\|7f7fff\|3f007f\|7f00ff\|bf7fff\|ff7fff\|7f003f\|ff007f\|ff7fbf\)\>

:read !grep '\<\(ff7f7f\|7f3f00\|ff7f00\|ffbf7f\|ffff7f\|3f7f00\|7fff00\|bfff7f\|7fff7f\|007f3f\|00ff7f\|7fffbf\|7fffff\|003f7f\|007fff\|7fbfff\|7f7fff\|3f007f\|7f00ff\|bf7fff\|ff7fff\|7f003f\|ff007f\|ff7fbf\)\>' -r ../../python3_src/seed/for_libs/for_colorsys/color_names_impl/ -h --exclude-dir=__pycache__ -o -i
:.,.+23sort u
  5=24-19
007fff
00ff7f
7f00ff
7fff00
ff7f00



:read !ls ../../python3_src/seed/for_libs/for_colorsys/color_names_impl/ -1
__init__.py
__pycache__
colors_in_css2_1.py
colors_in_matplotlib.py
colors_in_pynche_HTML4_0.py
colors_in_pynche_XConsortium_rgb.py
colors_in_pynche_namedcolors.py
colors_in_pynche_webcolors.py
colors_in_tkinter.py
colors_in_tkinter__degraded.py
colors_in_tkinter__degraded__lower.py
colors_in_vim82_css3.py
colors_in_vim82_css3__renamed.py
colors_in_vim82_default.py


:read !grep '\<[0-9a-fA-F]\{6\}\>' -r ../../python3_src/seed/for_libs/for_colorsys/color_names_impl/ -h --exclude-dir=__pycache__ -o -i
  2121 行
:.,.+2120sort u
  591=2121-1530
591_colors:begin
000000
000080
00008b
00009c
0000cd
0000ee
0000ff
006400
00688b
007fff
008000
008080
00868b
008b00
008b45
008b8b
009acd
00b2ee
00bfff
00c5cd
00cd00
00cd66
00cdcd
00ced1
00e5ee
00ee00
00ee76
00eeee
00f5ff
00fa9a
00ff00
00ff7f
00ffff
030303
050505
080808
0a0a0a
0d0d0d
0f0f0f
104e8b
121212
141414
171717
1874cd
191970
1a1a1a
1c1c1c
1c86ee
1e90ff
1f1f1f
20b2aa
212121
215e21
228b22
23238e
236b8e
238e23
238e68
242424
262626
27408b
292929
2b2b2b
2e2e2e
2e8b57
2f2f4f
2f4f2f
2f4f4f
303030
3232cd
3299cc
32cd32
32cd99
333333
363636
36648b
383838
38b0de
3a5fcd
3b3b3b
3cb371
3d3d3d
404040
40e0d0
4169e1
424242
42426f
426f42
436eee
43cd80
454545
458b00
458b74
4682b4
473c8b
474747
483d8b
4876ff
48d1cc
4a4a4a
4a708b
4a766e
4b0082
4d4d4d
4d4dff
4e2f2f
4eee94
4f2f4f
4f4f2f
4f4f4f
4f94cd
525252
527f76
528b8b
53868b
545454
548b54
54ff9f
551a8b
556b2f
575757
595959
5959ab
5c3317
5c4033
5c5c5c
5cacee
5d478b
5e5e5e
5f9ea0
5f9f9f
607b8b
616161
636363
63b8ff
6495ed
663399
666666
668b8b
66cd00
66cdaa
68228b
68838b
6959cd
696969
698b22
698b69
6a5acd
6b238e
6b4226
6b6b6b
6b8e23
6c7b8b
6ca6cd
6e6e6e
6e7b8b
6e8b3d
6f4242
707070
708090
7093db
70db93
70dbdb
737373
757575
76ee00
76eec6
778899
787878
79cdcd
7a378b
7a67ee
7a7a7a
7a8b8b
7ac5cd
7b68ee
7ccd7c
7cfc00
7d26cd
7d7d7d
7ec0ee
7f00ff
7f7f7f
7fff00
7fffd4
800000
800080
808000
808080
828282
836fff
838b83
838b8b
8470ff
855e42
856363
858585
871f78
878787
87ceeb
87cefa
87ceff
8968cd
8a2be2
8a8a8a
8b0000
8b008b
8b0a50
8b1a1a
8b1c62
8b2252
8b2323
8b2500
8b3626
8b3a3a
8b3a62
8b3e2f
8b4500
8b4513
8b4726
8b475d
8b4789
8b4c39
8b5742
8b5a00
8b5a2b
8b5f65
8b636c
8b6508
8b668b
8b6914
8b6969
8b7355
8b7500
8b7765
8b795e
8b7b8b
8b7d6b
8b7d7b
8b7e66
8b814c
8b8378
8b8386
8b864e
8b8682
8b8878
8b8970
8b8989
8b8b00
8b8b7a
8b8b83
8c1717
8c7853
8c8c8c
8db6cd
8deeee
8e2323
8e236b
8e6b23
8ee5ee
8f8f8f
8f8fbd
8fbc8f
90ee90
912cee
919191
9370db
93db70
9400d3
949494
969696
96cdcd
97694f
97ffff
98f5ff
98fb98
9932cc
9932cd
999999
99cc32
9a32cd
9ac0cd
9acd32
9aff9a
9b30ff
9bcd9b
9c9c9c
9e9e9e
9f5f9f
9f79ee
9f9f5f
9fb6cd
a020f0
a0522d
a1a1a1
a2b5cd
a2cd5a
a3a3a3
a4d3ee
a52a2a
a62a2a
a67d3d
a68064
a6a6a6
a8a8a8
a9a9a9
ab82ff
ababab
adadad
add8e6
adeaea
adff2f
aeeeee
afeeee
b03060
b0b0b0
b0c4de
b0e0e6
b0e2ff
b22222
b23aee
b2dfee
b3b3b3
b3ee3a
b452cd
b4cdcd
b4eeb4
b5a642
b5b5b5
b87333
b8860b
b8b8b8
b9d3ee
ba55d3
bababa
bbffff
bc8f8f
bcd2ee
bcee68
bdb76b
bdbdbd
bebebe
bf3eff
bfbfbf
bfefff
c0c0c0
c0d9d9
c0ff3e
c1cdc1
c1cdcd
c1ffc1
c2c2c2
c4c4c4
c6e2ff
c71585
c7c7c7
c9c9c9
cae1ff
caff70
cc3299
cccccc
cd0000
cd00cd
cd1076
cd2626
cd2990
cd3278
cd3333
cd3700
cd4f39
cd5555
cd5b45
cd5c5c
cd6090
cd6600
cd661d
cd6839
cd6889
cd69c9
cd7054
cd7f32
cd8162
cd8500
cd853f
cd8c95
cd919e
cd950c
cd96cd
cd9b1d
cd9b9b
cdaa7d
cdad00
cdaf95
cdb38b
cdb5cd
cdb79e
cdb7b5
cdba96
cdbe70
cdc0b0
cdc1c5
cdc5bf
cdc673
cdc8b1
cdc9a5
cdc9c9
cdcd00
cdcdb4
cdcdc1
cdcdcd
cfb53b
cfcfcf
d02090
d15fee
d19275
d1d1d1
d1eeee
d2691e
d2b48c
d3d3d3
d4d4d4
d6d6d6
d8bfd8
d8d8bf
d98719
d9d919
d9d9d9
d9d9f3
da70d6
daa520
db7093
db70db
db9370
dbdb70
dbdbdb
dc143c
dcdcdc
dda0dd
deb887
dedede
e066ff
e0e0e0
e0eee0
e0eeee
e0ffff
e3e3e3
e47833
e5e5e5
e6e6fa
e6e8fa
e8e8e8
e9967a
e9c2a6
eaadea
eaeaae
ebc79e
ebebeb
ededed
ee0000
ee00ee
ee1289
ee2c2c
ee30a7
ee3a8c
ee3b3b
ee4000
ee5c42
ee6363
ee6a50
ee6aa7
ee7600
ee7621
ee7942
ee799f
ee7ae9
ee8262
ee82ee
ee9572
ee9a00
ee9a49
eea2ad
eea9b8
eead0e
eeaeee
eeb422
eeb4b4
eec591
eec900
eecbad
eecfa1
eed2ee
eed5b7
eed5d2
eed8ae
eedc82
eedd82
eedfcc
eee0e5
eee5de
eee685
eee8aa
eee8cd
eee9bf
eee9e9
eeee00
eeeed1
eeeee0
f08080
f0e68c
f0f0f0
f0f8ff
f0fff0
f0ffff
f2f2f2
f4a460
f5deb3
f5f5dc
f5f5f5
f5fffa
f7f7f7
f8f8ff
fa8072
faa460
faebd7
faf0e6
fafad2
fafafa
fcfcfc
fdf5e6
ff0000
ff00ff
ff1493
ff1cae
ff2400
ff3030
ff34b3
ff3e96
ff4040
ff4500
ff6347
ff69b4
ff6a6a
ff6eb4
ff6ec7
ff7256
ff7f00
ff7f24
ff7f50
ff8247
ff82ab
ff83fa
ff8b8b
ff8bff
ff8c00
ff8c69
ffa07a
ffa500
ffa54f
ffaa00
ffaeb9
ffb5c5
ffb6c1
ffb90f
ffbbff
ffc0cb
ffc125
ffc1c1
ffd39b
ffd700
ffdab9
ffdead
ffe1ff
ffe4b5
ffe4c4
ffe4e1
ffe7ba
ffebcd
ffec8b
ffefd5
ffefdb
fff0f5
fff5ee
fff68f
fff8dc
fffacd
fffaf0
fffafa
ffff00
ffffe0
fffff0
ffffff
591_colors:end




===
named_colors__15
15_named_colors
:read !grep '\<\(000000\|000080\|0000ff\|008000\|008080\|00ff00\|00ffff\|800000\|800080\|808000\|808080\|ff0000\|ff00ff\|ffff00\|ffffff\)\>'  -r ../../python3_src/seed/for_libs/for_colorsys/color_names_impl/ -h --exclude-dir=__pycache__ -i
    155 lines
ctrl+v, u
:.+1,.+155s/ //g
:.+1,.+155s/^ *[{,]\?'\([^']*\)':'#\(\w\{6}\)'[,}]\?$/\2:\1
    150=155-5 # 『css_green=#008000:green=#00ff00』
:.+1,.+150sort u
    54=150-96
:.+1,.+54s/^\(\(\w\+:\).*\)\n\2/\1,
    32=54-22
:.+1,.+32s/^\(\(\w\+:\).*\)\n\2/\1,
    19=32-13
:.+1,.+19s/^\(\(\w\+:\).*\)\n\2/\1,
    15=19-4
000000:black,css_black,gray0,grey0
000080:css_navy,navy,navyblue
0000ff:blue,blue1,css_blue
008000:css_green,green,webgreen
008080:css_teal,teal
00ff00:css_lime,green,green1,lime,x11green
00ffff:aqua,css_aqua,css_cyan,cyan,cyan1
800000:css_maroon,maroon,webmaroon
800080:css_purple,purple,webpurple
808000:css_olive,olive
808080:css_gray,css_grey,gray,grey,webgray,webgrey
ff0000:css_red,red,red1
ff00ff:css_fuchsia,css_magenta,fuchsia,magenta,magenta1
ffff00:css_yellow,yellow,yellow1
ffffff:css_white,gray100,grey100,white
css_gray=#808080:gray=#bebebe
css_green=#008000:green=#00ff00
css_grey=#808080:grey=#bebebe
css_maroon=#800000:maroon=#b03060
css_purple=#800080:purple=#a020f0



=======
000000:black,css_black,gray0,grey0#黑色
000080:css_navy,navy,navyblue#海军蓝/藏青色/深蓝色
0000ff:blue,blue1,css_blue#蓝色
008000:css_green,green,webgreen#xxx绿色??暗绿色
008080:css_teal,teal#水鸭??
00ff00:css_lime,green,green1,lime,x11green#绿色??石灰绿??酸橙色??绿黄色??绿色
00ffff:aqua,css_aqua,css_cyan,cyan,cyan1#水色??淡绿色??氰基??蓝绿色/青蓝色
800000:css_maroon,maroon,webmaroon#栗色/茶色/酱紫色/绛紫色??
800080:css_purple,purple,webpurple#xxx紫色??暗紫色
808000:css_olive,olive#橄榄色??
808080:css_gray,css_grey,gray,grey,webgray,webgrey#灰色
ff0000:css_red,red,red1#红色
ff00ff:css_fuchsia,css_magenta,fuchsia,magenta,magenta1#灯笼海棠/倒挂金钟??紫红色/品红/洋红
ffff00:css_yellow,yellow,yellow1#黄色
ffffff:css_white,gray100,grey100,white#白色
==>>tbl4named_color2std_names:here
    tbl4unamed_colorXnear_named_color2std_names__VER1_X_VER2:goto

=======
===
merge_near_named_colors(unamed_color2near_named_colors__VER1) =>:
all_near_named_colors__VER1
\<\(104e8b\|008b45\|007fff\|00ff7f\|4b0082\|458b00\|8b0a50\|7f00ff\|8b4500\|8470ff\|87ceff\|7fff00\|90ee90\|7fffd4\|97ffff\|ab82ff\|caff70\|ee1289\|ff7f00\|fa8072\|ff6ec7\|ff83fa\|eec591\|fff68f\)\>

===
all_near_named_colors__VER1
:read !grep '\<\(104e8b\|008b45\|007fff\|00ff7f\|4b0082\|458b00\|8b0a50\|7f00ff\|8b4500\|8470ff\|87ceff\|7fff00\|90ee90\|7fffd4\|97ffff\|ab82ff\|caff70\|ee1289\|ff7f00\|fa8072\|ff6ec7\|ff83fa\|eec591\|fff68f\)\>'  -r ../../python3_src/seed/for_libs/for_colorsys/color_names_impl/ -h --exclude-dir=__pycache__ -i
    80 lines
ctrl+v, u
:.+1,.+80s/ //g
:.+1,.+80s/^ *[{,]\?'\([^']*\)':'#\(\w\{6}\)'[,}]\?$/\2:\1
:.+1,.+80sort u
    37=80-43
:.+1,.+37s/^\(\(\w\+:\).*\)\n\2/\1,
    29=37-8
:.+1,.+29s/^\(\(\w\+:\).*\)\n\2/\1,
    24=29-5
007fff:slateblue
008b45:springgreen4
00ff7f:css_springgreen,springgreen,springgreen1
104e8b:dodgerblue4
458b00:chartreuse4
4b0082:css_indigo,indigo
7f00ff:mediumslateblue
7fff00:chartreuse,chartreuse1,css_chartreuse,mediumspringgreen
7fffd4:aquamarine,aquamarine1,css_aquamarine
8470ff:lightslateblue
87ceff:skyblue1
8b0a50:deeppink4
8b4500:darkorange4
90ee90:css_lightgreen,lightgreen,palegreen2
97ffff:darkslategray1
ab82ff:mediumpurple1
caff70:darkolivegreen1
ee1289:deeppink2
eec591:burlywood2
fa8072:css_salmon,salmon
ff6ec7:neonpink
ff7f00:coral,darkorange1,orange
ff83fa:orchid1
fff68f:khaki1
==>>tbl4near_named_color2std_names__VER1:here


===
unamed_color2near_named_colors__VER1
:s/': \['/:/g
:s/'\], '/\r/g
:.+1,.+24sort /:/
0080ff:007fff
008040:008b45
00ff80:00ff7f
004080:104e8b
408000:458b00
400080:4b0082
8000ff:7f00ff
80ff00:7fff00
80ffc0:7fffd4
8080ff:8470ff
80c0ff:87ceff
800040:8b0a50
804000:8b4500
80ff80:90ee90
80ffff:97ffff
c080ff:ab82ff
c0ff80:caff70
ff0080:ee1289
ffc080:eec591
ff8080:fa8072
ff80c0:ff6ec7
ff8000:ff7f00
ff80ff:ff83fa
ffff80:fff68f
==>>tbl4unamed_color2near_named_color__VER1:here

===
tbl4unamed_color2near_named_color__VER1*tbl4near_named_color2std_names__VER1 =>:
/\(:\w*\)\1
0080ff:007fff:slateblue
008040:008b45:springgreen4
00ff80:00ff7f:css_springgreen,springgreen,springgreen1
004080:104e8b:dodgerblue4
408000:458b00:chartreuse4
400080:4b0082:css_indigo,indigo
8000ff:7f00ff:mediumslateblue
80ff00:7fff00:chartreuse,chartreuse1,css_chartreuse,mediumspringgreen
80ffc0:7fffd4:aquamarine,aquamarine1,css_aquamarine
8080ff:8470ff:lightslateblue
80c0ff:87ceff:skyblue1
800040:8b0a50:deeppink4
804000:8b4500:darkorange4
80ff80:90ee90:css_lightgreen,lightgreen,palegreen2
80ffff:97ffff:darkslategray1
c080ff:ab82ff:mediumpurple1
c0ff80:caff70:darkolivegreen1
ff0080:ee1289:deeppink2
ffc080:eec591:burlywood2
ff8080:fa8072:css_salmon,salmon
ff80c0:ff6ec7:neonpink
ff8000:ff7f00:coral,darkorange1,orange
ff80ff:ff83fa:orchid1
ffff80:fff68f:khaki1
==>>tbl4unamed_colorXnear_named_color2std_names__VER1:here



=======
===
merge_near_named_colors(unamed_color2near_named_colors__VER2) =>:
all_near_named_colors__VER2
\<\(00688b\|008b45\|007fff\|00ff7f\|4b0082\|458b00\|800080\|7f00ff\|8b4500\|8470ff\|7ec0ee\|7fff00\|90ee90\|7fffd4\|8deeee\|ab82ff\|caff70\|cd00cd\|ff7f00\|f08080\|ff82ab\|ff83fa\|eec591\|ffec8b\)\>

===
all_near_named_colors__VER2
:read !grep '\<\(00688b\|008b45\|007fff\|00ff7f\|4b0082\|458b00\|800080\|7f00ff\|8b4500\|8470ff\|7ec0ee\|7fff00\|90ee90\|7fffd4\|8deeee\|ab82ff\|caff70\|cd00cd\|ff7f00\|f08080\|ff82ab\|ff83fa\|eec591\|ffec8b\)\>'  -r ../../python3_src/seed/for_libs/for_colorsys/color_names_impl/ -h --exclude-dir=__pycache__ -i
    89 lines
ctrl+v, u
:.+1,.+89s/ //g
:.+1,.+89s/^ *[{,]\?'\([^']*\)':'#\(\w\{6}\)'[,}]\?$/\2:\1
    88=89-1 # 『css_purple=#800080:purple=#a020f0』
:.+1,.+88sort u
    39=88-49
:.+1,.+39s/^\(\(\w\+:\).*\)\n\2/\1,
    30=39-9
:.+1,.+30s/^\(\(\w\+:\).*\)\n\2/\1,
    24=30-6
00688b:deepskyblue4
007fff:slateblue
008b45:springgreen4
00ff7f:css_springgreen,springgreen,springgreen1
458b00:chartreuse4
4b0082:css_indigo,indigo
7ec0ee:skyblue2
7f00ff:mediumslateblue
7fff00:chartreuse,chartreuse1,css_chartreuse,mediumspringgreen
7fffd4:aquamarine,aquamarine1,css_aquamarine
800080:css_purple,purple,webpurple
8470ff:lightslateblue
8b4500:darkorange4
8deeee:darkslategray2
90ee90:css_lightgreen,lightgreen,palegreen2
ab82ff:mediumpurple1
caff70:darkolivegreen1
cd00cd:magenta3
eec591:burlywood2
f08080:css_lightcoral,lightcoral
ff7f00:coral,darkorange1,orange
ff82ab:palevioletred1
ff83fa:orchid1
ffec8b:lightgoldenrod1
==>>tbl4near_named_color2std_names__VER2:here


===
unamed_color2near_named_colors__VER2
:s/': \['/:/g
:s/'\], '/\r/g
:.+1,.+24sort /:/
004080:00688b
0080ff:007fff
008040:008b45
00ff80:00ff7f
408000:458b00
400080:4b0082
80c0ff:7ec0ee
8000ff:7f00ff
80ff00:7fff00
80ffc0:7fffd4
800040:800080
8080ff:8470ff
804000:8b4500
80ffff:8deeee
80ff80:90ee90
c080ff:ab82ff
c0ff80:caff70
ff0080:cd00cd
ffc080:eec591
ff8080:f08080
ff8000:ff7f00
ff80c0:ff82ab
ff80ff:ff83fa
ffff80:ffec8b
==>>tbl4unamed_color2near_named_color__VER2:here

===
tbl4unamed_color2near_named_color__VER2*tbl4near_named_color2std_names__VER2 =>:
/\(:\w*\)\1
004080:00688b:deepskyblue4
0080ff:007fff:slateblue
008040:008b45:springgreen4
00ff80:00ff7f:css_springgreen,springgreen,springgreen1
408000:458b00:chartreuse4
400080:4b0082:css_indigo,indigo
80c0ff:7ec0ee:skyblue2
8000ff:7f00ff:mediumslateblue
80ff00:7fff00:chartreuse,chartreuse1,css_chartreuse,mediumspringgreen
80ffc0:7fffd4:aquamarine,aquamarine1,css_aquamarine
800040:800080:css_purple,purple,webpurple
8080ff:8470ff:lightslateblue
804000:8b4500:darkorange4
80ffff:8deeee:darkslategray2
80ff80:90ee90:css_lightgreen,lightgreen,palegreen2
c080ff:ab82ff:mediumpurple1
c0ff80:caff70:darkolivegreen1
ff0080:cd00cd:magenta3
ffc080:eec591:burlywood2
ff8080:f08080:css_lightcoral,lightcoral
ff8000:ff7f00:coral,darkorange1,orange
ff80c0:ff82ab:palevioletred1
ff80ff:ff83fa:orchid1
ffff80:ffec8b:lightgoldenrod1
==>>tbl4unamed_colorXnear_named_color2std_names__VER2:here



=======
tbl4unamed_colorXnear_named_color2std_names__VER1*tbl4unamed_colorXnear_named_color2std_names__VER2
:.+1,.+48sort u
    32=48-16
        ==24+8
:.+1,.+32s/^\(\(\w\+:\).*\)\n\2/\1;
    24=32-8
004080:00688b:deepskyblue4;104e8b:dodgerblue4#xxx暗天蓝色??;?暗传单蓝色?
008040:008b45:springgreen4#暗春绿色
0080ff:007fff:slateblue#灰瓦蓝色
00ff80:00ff7f:css_springgreen,springgreen,springgreen1#春绿色
400080:4b0082:css_indigo,indigo#暗靛蓝色
408000:458b00:chartreuse4#暗黄绿色/暗草黄色
800040:800080:css_purple,purple,webpurple;8b0a50:deeppink4#xxx紫色??;暗粉红色/暗桃红色
8000ff:7f00ff:mediumslateblue#半瓦蓝色
804000:8b4500:darkorange4#暗橙色
8080ff:8470ff:lightslateblue#亮瓦蓝色
80c0ff:7ec0ee:skyblue2;87ceff:skyblue1#亮天蓝色;..
80ff00:7fff00:chartreuse,chartreuse1,css_chartreuse,mediumspringgreen#草黄色/黄绿色/半春绿色
80ff80:90ee90:css_lightgreen,lightgreen,palegreen2#亮绿色
80ffc0:7fffd4:aquamarine,aquamarine1,css_aquamarine#碧绿色/海绿色/蓝绿色/水蓝色/海蓝色
80ffff:8deeee:darkslategray2;97ffff:darkslategray1#暗瓦灰色??亮瓦灰色
c080ff:ab82ff:mediumpurple1#半紫色
c0ff80:caff70:darkolivegreen1#暗橄榄绿/暗草绿色/暗茶青色
ff0080:cd00cd:magenta3;ee1289:deeppink2#xxx紫红色/品红/洋红??;暗桃红色??桃红色
ff8000:ff7f00:coral,darkorange1,orange#珊瑚红色/暗橙色??/橙色??
ff8080:f08080:css_lightcoral,lightcoral;fa8072:css_salmon,salmon#亮珊瑚红色;鲑鱼肉色/鲜肉色/橙红色#黄粉红色
ff80c0:ff6ec7:neonpink;ff82ab:palevioletred1#氖灯粉红色/霓虹灯粉红色;亮紫红色
ff80ff:ff83fa:orchid1#亮紫色/淡紫色/兰花色
ffc080:eec591:burlywood2#??实木色??
ffff80:ffec8b:lightgoldenrod1;fff68f:khaki1#亮秋麒麟草色(秋麒麟草===一枝黄花);卡其黄色/茶褐色/黄褐色/土黄色
==>>tbl4unamed_colorXnear_named_color2std_names__VER1_X_VER2:here
    tbl4named_color2std_names:goto





*/
</script>

]]]


#]]]'''
__all__ = r'''
'''.split()#'''
__all__

def _extract__591_colors(__doc__, /):
    colors__591 = _extract__data(__doc__, '591_colors', 591)
    return colors__591
def _extract__15_named_colors(__doc__, /):
    named_colors__15 = _extract__data(__doc__, '15_named_colors', 15)
    return named_colors__15
def _extract__24_unamed_colors(__doc__, /):
    unamed_colors__24 = _extract__data(__doc__, '24_unamed_colors', 24)
    return unamed_colors__24
def _extract__data(__doc__, nm, sz, /):
    s = __doc__
    _, _s = s.split(f'{nm}:begin')
    _s_, _ = _s.split(f'{nm}:end')
    ls = _s_.split()
    assert len(ls) == sz
    assert sorted(ls) == ls
    ls = tuple(ls)
    return ls
colors__591 = _extract__591_colors(__doc__)
named_colors__15 = _extract__15_named_colors(__doc__)
unamed_colors__24 = _extract__24_unamed_colors(__doc__)

def check_color(c6, /):
    assert type(c6) is str
    assert len(c6) == 6
    assert c6.lower() == c6
    #assert c6.isxdigit()
    assert c6.isalnum()
    int(c6, 16)
def rgb5color(c6, /):
    check_color(c6)
    r = c6[:2]
    g = c6[2:4]
    b = c6[4:]
    r = int(r, 16)
    g = int(g, 16)
    b = int(b, 16)
    return (r, g, b)
def diff4color(lhs_c6, rhs_c6, /, *, ver):
    lhs = rgb5color(lhs_c6)
    rhs = rgb5color(rhs_c6)
    if ver == 2:
        return sum(0.0 if a==b else (a-b)**2/(a+b)**2 for a, b in zip(lhs, rhs))
    if ver == 1:
        return sum((a-b)**2 for a, b in zip(lhs, rhs))
    raise ValueError(ver)
def find_near_colors(named_colors, unamed_colors, /, *, ver):
    unamed_color2near_named_colors = {c:[] for c in unamed_colors}
    for unamed_color, near_named_colors in unamed_color2near_named_colors.items():
        ps = sorted((diff4color(unamed_color, named_color, ver=ver), named_color) for named_color in named_colors)
        dff = ps[0][0]
        for j, (_dff, _) in enumerate(ps):
            if not _dff == dff:
                break
        near_named_colors.extend(c for _, c in ps[:j])
        assert len(near_named_colors) == 1
    return unamed_color2near_named_colors
def merge_near_named_colors(xnamed_color2near_named_colors, /):
    ls = []
    for _, near_named_colors in sorted(xnamed_color2near_named_colors.items()):
        ls.extend(near_named_colors)
    return tuple(ls)
if 1:
    named_color2exact_named_colors = find_near_colors(colors__591, named_colors__15, ver=1)
    assert (named_color2exact_named_colors == {'000000': ['000000'], '000080': ['000080'], '0000ff': ['0000ff'], '008000': ['008000'], '008080': ['008080'], '00ff00': ['00ff00'], '00ffff': ['00ffff'], '800000': ['800000'], '800080': ['800080'], '808000': ['808000'], '808080': ['808080'], 'ff0000': ['ff0000'], 'ff00ff': ['ff00ff'], 'ffff00': ['ffff00'], 'ffffff': ['ffffff']}), named_color2exact_named_colors
    all_exact_named_colors = merge_near_named_colors(named_color2exact_named_colors)
    assert (all_exact_named_colors == ('000000', '000080', '0000ff', '008000', '008080', '00ff00', '00ffff', '800000', '800080', '808000', '808080', 'ff0000', 'ff00ff', 'ffff00', 'ffffff')), all_exact_named_colors
    assert len(all_exact_named_colors) == 15
    assert len(all_exact_named_colors) == len(named_colors__15)
    assert (all_exact_named_colors) == (named_colors__15)


def diff4unamed_color2near_named_colors(d0, d1, /):
    assert d0.keys() == d1.keys()
    d = {}
    for k, v0 in d0.items():
        v1 = d1[k]
        if not v0 == v1:
            d[k] = (v0, v1)
    return d
def mk_ex__unamed_color2near_named_colors(*, ver):
    unamed_color2near_named_colors = find_near_colors(colors__591, unamed_colors__24, ver=ver)
    all_near_named_colors = merge_near_named_colors(unamed_color2near_named_colors)
    assert len(all_near_named_colors) == 24
    assert len(all_near_named_colors) == len(unamed_colors__24)
    return (unamed_color2near_named_colors, all_near_named_colors)


if 1:
    ver = 1
    (unamed_color2near_named_colors__VER1, all_near_named_colors__VER1) = mk_ex__unamed_color2near_named_colors(ver=ver)
    assert (unamed_color2near_named_colors__VER1 == {'004080': ['104e8b'], '008040': ['008b45'], '0080ff': ['007fff'], '00ff80': ['00ff7f'], '400080': ['4b0082'], '408000': ['458b00'], '800040': ['8b0a50'], '8000ff': ['7f00ff'], '804000': ['8b4500'], '8080ff': ['8470ff'], '80c0ff': ['87ceff'], '80ff00': ['7fff00'], '80ff80': ['90ee90'], '80ffc0': ['7fffd4'], '80ffff': ['97ffff'], 'c080ff': ['ab82ff'], 'c0ff80': ['caff70'], 'ff0080': ['ee1289'], 'ff8000': ['ff7f00'], 'ff8080': ['fa8072'], 'ff80c0': ['ff6ec7'], 'ff80ff': ['ff83fa'], 'ffc080': ['eec591'], 'ffff80': ['fff68f']}), unamed_color2near_named_colors__VER1
    assert (all_near_named_colors__VER1 == ('104e8b', '008b45', '007fff', '00ff7f', '4b0082', '458b00', '8b0a50', '7f00ff', '8b4500', '8470ff', '87ceff', '7fff00', '90ee90', '7fffd4', '97ffff', 'ab82ff', 'caff70', 'ee1289', 'ff7f00', 'fa8072', 'ff6ec7', 'ff83fa', 'eec591', 'fff68f')), all_near_named_colors__VER1


if 1:
    ver = 2
    (unamed_color2near_named_colors__VER2, all_near_named_colors__VER2) = mk_ex__unamed_color2near_named_colors(ver=ver)
    assert (unamed_color2near_named_colors__VER2 == {'004080': ['00688b'], '008040': ['008b45'], '0080ff': ['007fff'], '00ff80': ['00ff7f'], '400080': ['4b0082'], '408000': ['458b00'], '800040': ['800080'], '8000ff': ['7f00ff'], '804000': ['8b4500'], '8080ff': ['8470ff'], '80c0ff': ['7ec0ee'], '80ff00': ['7fff00'], '80ff80': ['90ee90'], '80ffc0': ['7fffd4'], '80ffff': ['8deeee'], 'c080ff': ['ab82ff'], 'c0ff80': ['caff70'], 'ff0080': ['cd00cd'], 'ff8000': ['ff7f00'], 'ff8080': ['f08080'], 'ff80c0': ['ff82ab'], 'ff80ff': ['ff83fa'], 'ffc080': ['eec591'], 'ffff80': ['ffec8b']}), unamed_color2near_named_colors__VER2
    assert (all_near_named_colors__VER2 == ('00688b', '008b45', '007fff', '00ff7f', '4b0082', '458b00', '800080', '7f00ff', '8b4500', '8470ff', '7ec0ee', '7fff00', '90ee90', '7fffd4', '8deeee', 'ab82ff', 'caff70', 'cd00cd', 'ff7f00', 'f08080', 'ff82ab', 'ff83fa', 'eec591', 'ffec8b')), all_near_named_colors__VER2


if 1:
    _d = diff4unamed_color2near_named_colors(unamed_color2near_named_colors__VER1, unamed_color2near_named_colors__VER2)
    assert (_d == {'004080': (['104e8b'], ['00688b']), '800040': (['8b0a50'], ['800080']), '80c0ff': (['87ceff'], ['7ec0ee']), '80ffff': (['97ffff'], ['8deeee']), 'ff0080': (['ee1289'], ['cd00cd']), 'ff8080': (['fa8072'], ['f08080']), 'ff80c0': (['ff6ec7'], ['ff82ab']), 'ffff80': (['fff68f'], ['ffec8b'])}), _d
    assert len(_d) == 8, len(_d)

__all__
from seed.for_libs.for_colorsys._mk4color_table_html import *

