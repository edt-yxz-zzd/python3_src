单手笔顺输入法码表 stroke-seq_MB 2.0 版
    https://github.com/YQ-YSY/stroke-seq_MB
========
开发说明

版权：GPL v3+
遵照《GB13000.1字符集汉字字序（笔画序）规范》共20902个汉字，遵照《GB13000.1字符集汉字笔顺规范》；
并增补GB18030字符集（截止2017年）开源字体可见双字节和四字节汉字8783个（即本输入法编码目前涵盖29685个汉字）；
随着开源字体的完善，以后可继续扩展录入GB18030字符集里的其它汉字，即可涵盖GB18030字符集全部汉字共70377个。
由于Unicode编码包含大量日韩使用的、与汉字字型笔画完全相同的文字（即同一个字重复出现两次），极易造成混淆，故不以此为标准。
编码原理基于专利权已终止的（CN03159505.7）“一种数字笔画汉字输入方法”，原发明人：马晓光 <232937@QQ.com>
参考《数字五笔中文输入系统输入教程及编码查询手册》
开源码表初始手工录入、简化规则、全新重排部件编码（偏旁部首编码）、再次手工录入：一善鱼 YQ-YSY <YQ-YSY@163.com>
拼音采用 wangyanhan（老老朽）整理制作并分享的《CJK汉字拼音表_42907字_14.8.10更新》，以及其它字典网站查询参考。
核心词库包括有《现代汉语常用词汇表》（38285个）以及其它常用词汇和短语共计约36万个，已剔除方言、网络词汇、粗口话和淫秽词语。
欢迎各位朋友利用此码表，或开发独立的笔顺输入法，或嵌入已开发的输入法，新输入法程序名称亦可自行设定。扩展词库现共计有243万个。
为了方便大家编辑并导出其它形式的码表，在此使用TXT文本文件，以及LibreOffice电子表格ods文件，里面有详细的分类编号及排序。
文件夹icon中还附带有本输入法的Logo图标以及部件编码的SVG格式和PNG格式文件，以及“悬浮栏功能设计说明”图JPG格式的文件。

========
一、笔顺码

仅仅以1、2、3、4、5五个数字分别代表“一丨丿丶𠃌”五个笔画，按汉字笔顺进行输入。例如：

“开”字，按笔顺“一、一、丿、丨”，编码为1132；
“我”字为31；“向”字为325；“力”为53；
注意“万”为153，“方”为4153，“忄”为442。

其中有些笔画容易被误解：
“提”归为“一”：如“氵、扌”中的最后一笔；有些电脑字体繁体字的“雨字头”四点显示为四小横，皆按国标笔顺归为四点；
“亅”一竖往左勾的归为“丨”：如“小”字的第一笔、“扌”提手旁等；“乚”一竖往右勾的归为“𠃌”：如“比、民、氏”的左边那一笔；
“点、捺”都归为“丶”：如“文、入、表、厶”的最后一笔；“宀”宝盖头和“冖”秃宝盖的左边那一笔也都是点“丶”，不是竖“丨”；
各种折笔（乛、フ、乚、𠃌、⺄、折弯钩、竖提等）都归为“𠃌”：如“乃、孔、民”中的笔画。

标点符号输入：
常用标点符号可以输入“00”,常用的数字序号可以输入“09”。
========
六、易错易混汉字

以下汉字结构是容易输入错误、被混淆、被误认为属于其它笔顺的：
1、“末、未、果”后四笔形成的“木”形结构，其结构清晰，易于辨认，且笔画顺序与“木”相同，故取“木”的编码12，“柬、谏”不行。
2、“国、因、回”含“囗”的汉字，因按笔顺这些字最后才封口，故不取“口”；正确取法应第一、二笔取“丨、𠃌”，取码25。
3、“都、教、考、孝、老”前三笔形成的“土”形结构，其结构清晰，易于辨认，且笔画顺序与“土”相同，故取“土”的编码19。
4、“里、垂、重、黑”中间的“土”形结构，其笔顺却是先一竖再二横，不是“土”字笔顺，故需按其笔顺取编码（“里”不取“甲”部件）。
5、“衰、蓑”中间的“口”形结构，按笔顺应先写“口”中间的一横，打乱了“口”字的笔顺，故不取“口”字部件编码，取其笔画编码2511。
6、“冒、帽”上面不是“日”字，而是丨𠃌一一，这两横不连接到旁边，即2511。
7、“有、育、膏”的下面不是“月”，而是先一竖，丨𠃌一一，即2511。
8、“用、甩”有类似“月”字的结构，但是结构变形较大，且混杂有其它笔画在其中，不易记忆，所以不取36编码，取笔顺即可。
9、“生”有类似“牛”字的结构，但是从记忆习惯上通常认为是一撇加“”字结构，因此不取“牛”字31编码，而取“”字71编码。
10、“满、螨”有类似“”编码18的部首，但因“艹”字头与下方的一横是断开的，且从习惯上通常认为“一”属于“两”字，故取编码17。
11、“垂、郵、甀、乗、剰”中间有类似“艹”的结构，但是因为混杂在其它笔画之中，不易辨认，故不取17编码，而取笔顺即可。
12、“脑、恼、垴”有类似“文”字的结构，但“乂”与上方的一横是断开的，且“乂”是属于“凶”字结构，故不取“文”字66编码，取笔顺即可。
13、“刪、姍、柵”中有类似“卄”字的结构，但是它的笔顺不是与“侖”字那样先一横再二竖，而是先二竖再一横，所以不取17编码。
14、“刺、棘、枣、策”中有类似“巾”字的结构，但是因为混杂在其它笔画之中，不易辨认，故不取25编码，而取笔顺即可。
15、“熏、薰、醺”中有类似“黑”字的结构，但因中间一竖穿透了“黑”字顶部，与上方其它笔画混杂，故不取86编码，而取笔顺。
16、“粛、簘、嘨”中有类似“米”字的结构，但按笔顺应先写中间一竖，然后接左一撇右一竖，不是"米”字笔顺，故需按其笔顺取编码。
77、有些汉字，在不同的电脑字体里显示出来的写法不一样，例如“爋”字的最后四点，“兏”字的第一笔是横，这类汉字以国标笔顺为准。

以下汉字和部件的笔顺容易出错（括号内为精简码或六全码）：
七：一𠃌　15　　　　　　九：丿𠃌　35　　　　　　匕：丿𠃌　35　　　　　　及：丿𠃌丶　 354
刀：𠃌丿　53　　　　　　力：𠃌丿　53　　　　　　乃：𠃌丿　53　　　　　　办：𠃌丿丶丶5344
万：一𠃌丿　 153　　　　　　　　　　　　小：丨丿丶　 234　　　　　　　　义：丶丿丶　 434
方：丶一𠃌丿 4153（60）　　　　　　　　忄：丶丶丨　 442（49）　　　　　火：丶丿人　 4334（69）
牜：丿一丨一 　3121（31）　　　　　凹：丨𠃌丨𠃌一　25251　　　　　　　长：丿一𠃌丶 3154
牛：丿一一丨 　3112（31）　　　　　凸：丨一丨𠃌一　21251　　　　　　　为：丶丿𠃌丶 4354（6）
车：一𠃌一丨　  1512（77）　　　　比：一𠃌丿𠃌　　1535　　　　　　　　巨：一𠃌一𠃌 1515（72）
轧：一𠃌丨一𠃌  15215（775）　　　世：廿𠃌 　12215（185）　　　　　　瓦：一𠃌𠃌丶 1554（79）
北：丨一一丿𠃌　21135 　　　　　　丹：丿𠃌丶一 3541　　　　　　　　母：𠃌𠃌丶一丶　55414（06）
爿：𠃌丨一丿5213（02）　　　毋：𠃌𠃌丿一 5531（06）　　　　　毌：𠃌𠃌丨一  5521（06）
丑：𠃌丨一一　 5211　　　　　必：丶𠃌丶丿丶 45434（65）　　　出：𠃌丨丨𠃌丨 52252（02）
那：𠃌一一丿阝 511352（51）　　皮：𠃌丿丨又　 53254 　　　　豖：一丿𠃌丿丿丶丿丶 13533434（13）
兆：丿丶一𠃌丿丶 341534　　　　脊：丶一丿丶人丨𠃌一一 4134342511（41343） 
卵：丿𠃌丶丿卩丶 3543524（354354）　　兜：丿日丿𠃌𠃌一丿𠃌 　32511355135（38135）
非：丨一一一丨一一一 21112111（23）　　飛：𠃌丿丶丿丿𠃌丿丶丨　 534335342　（534332）
來：一丨丶丿丶丿丶丿12343434（73）　　爽：一丿丶丿丶丿丶丿丶人13434343434（134344）
尒：丿丶丨丿丶 34234　　　　　　　　　　　　美：丶丿王一丿丶  431121134　  （431）
忝：一一丿丶丨丶丶丶 11342444（113424）　　善：丶丿一丨丶𠃌  431112431251（432）
曲：丨𠃌卄一　251221 （25171）　　　　　　　　曹：一丨𠃌卄一日  12512212511 （125171）
肃：彐丨丿丨八 51123234（0123）　　　　衰：丶 一丨𠃌一一丿𠃌丿丶 4125113534（41251） 
敝：丶丿丨𠃌丨丿丶攵 43252343134（6890）　　重：丿一日丨一一 312511211（318）
噩：一丨口口一口口一 1225125112512511　　（128081）
舆：丿丨一一车𠃌一一一丿丶 32111512511134（987）
========
========
