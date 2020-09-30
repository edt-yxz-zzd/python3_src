
r"""

e /storage/emulated/0/0my_files/git_repos/python3_src/nn_ns/CJK/CJK_data/raw/香港電腦漢字楷體字形基礎部件表.py
py -m nn_ns.CJK.CJK_data.raw.香港電腦漢字楷體字形基礎部件表
view /storage/emulated/0/0my_files/git_repos/python3_src/nn_ns/CJK/CJK_data/raw/raw\ text\ of\ 香港電腦漢字楷體字形基礎部件表.pdf.txt
    q/
    q:
    :h greedy
    :h \@!
    =====
    /(\([0-9A-F]\{4}\))
    :%s///g

    /\<\([2-9A-F][0-9A-F]\{3}\)\+
    :

    /.\{-}\(\<\([2-9A-F][0-9A-F]\{3}\)\+\)
    :%s// \1/g

    /\(pg \d\d\|\( \([2-9A-F][0-9A-F]\{3}\)\+\)*\).*
    :%s//\1/g

    /\n\+
    :%s//\r/g

    /\w\{4} \@!
    :%s//\0 /g

    :w /storage/emulated/0/0my_files/git_repos/python3_src/nn_ns/CJK/CJK_data/raw/step1\ text\ of\ 香港電腦漢字楷體字形基礎部件表.pdf.txt
view /storage/emulated/0/0my_files/git_repos/python3_src/nn_ns/CJK/CJK_data/raw/step1\ text\ of\ 香港電腦漢字楷體字形基礎部件表.pdf.txt
py -m nn_ns.app.hex2char -i /storage/emulated/0/0my_files/git_repos/python3_src/nn_ns/CJK/CJK_data/raw/step1\ text\ of\ 香港電腦漢字楷體字形基礎部件表.pdf.txt -o ~/tmp/hk.hz.exmpl.txt

=======
Private Use Area (PUA): U+E000..U+F8FF
E115 艹-尺



=======
1:>,(一u4E00h//横【一】)=>
2:>,(//竖),(丨u4E28h//),(亅u4E85h//)=>
3:>,(//撇),(丿u4E3Fh//)=>
4:>,(//点),(丶u4E36h//),(乁u4E41h//),(乀u4E40h//)=>
5:>,(乙u4E59h//横折弯钩【乙】),(//横钩),(//横折),(//横折钩),(//竖折),(//竖弯钩),(乛u4E5Bh//),(乚u4E5Ah//),(uE818h//),(uE819h//),(𠃊u200CAh//),(𠃋u200CBh//),(𠃌u200CCh//),(𠃍u200CDh//),(𠃑u200D1h//),(𠄌u2010Ch//),(𠄎u2010Eh//),(𡿨u21FE8h//)=>
    ,(乙u4E59h//横折弯钩【乙】)
    ,(//横钩),(乛u4E5Bh//)
    ,(//横折) ~ 横撇
    ,(𠃍u200CDh//) ~ 横竖
    ,(//横折钩),(𠃌u200CCh//) ~ 横竖钩
    ,(//竖折),(𠃊u200CAh//)
    ,(//竖弯钩),(乚u4E5Ah//)
    ,(uE818h//)
    ,(uE819h//)
    ,(𠃋u200CBh//)
    ,(𠃑u200D1h//)
    ,(𠄌u2010Ch//)
    ,(𠄎u2010Eh//)
    ,(𡿨u21FE8h//)
13:>,(厂u5382h/厰u53B0h庵u5EB5h廠u5EE0h/厂),(//夏字头),(//左字框),(丆u4E06h//),(uE816h//),(𠂇u20087h//)=>


=======
《信息處理用 GB13000.1 字符集漢字部件規範》

[香港電腦漢字印刷體 (宋體)字形基礎部件表]m_glyph_1img_web.pdf
  644
[香港電腦漢字楷體字形基礎部件表]ly_glyph11_imgcode_web.pdf
  644
  ====
  {open}{sep}{笔画数}{sep}{笔画码}{sep}{hk_gl_idx}{sep}{部件名}{sep}{close}
  {open}㍘{笔画数}㍙{笔画码}㍚{hk_gl_idx}㍛{部件名}{close}
  {open}笔画数{笔画数}{数字止}笔画码{笔画码}{数字止}港序号{港序号}{数字止}单字符{单字符}部件名{部件名}{close}
    全汉字
      数字: "零一二三四五六七八九"
      排序要求:
        {数字止} < min(数字)=一=u4E00h
        {close} < {数字止}
        {close} < {部件名} <- 常见汉字
        {close} < {单字符} <- 正常汉字+汉字部件+汉字笔画
          2E80..2F00:cjk部件:⺀⺁⺂
          2F00..2FF0:cjk康基:⼀⼁⼂⼃⼄⼅⼆
          2FF0..:cjk结构:⿰⿱⿲
          31C0..31F0:cjk笔触:㇀㇁㇂㇃㇄㇅㇆㇇㇈㇉㇊㇋㇌㇍㇎㇏㇐㇑㇒㇓㇔㇕㇖㇗㇘㇙㇚㇛㇜㇝㇞㇟㇠㇡㇢
          ===vim * id rex 不相通。see try
          3300:㍘㍙㍚㍛㍜㍝㍞㍟㍠㍡㎇㎐㎧㏀㏾㏿㐀 < 一
          try:
            ⺀⼀⿰㇀㍘㐀件
            ⺀⼀⿰㇀ !! ㍘㐀一件
            :set iskeyword?
              iskeyword=!-~,^*,^|,^",192-255
              iskeyword=@,48-57,_,192-255
            :h iskeyword
              characters above 255 check the "word" character class.
      open=6_
      sep=
      close=_9
    mannual:
      笔画码
      ?hk_gl_idx
      部件名



#"""


from nn_ns.CJK.CJK_data.unicode_cjk_部件_笔画 import (
    CJK_Radicals_Supplement
    ,Kangxi_Radicals
    ,Ideographic_Description_Characters
    ,CJK_Strokes
    )


##data##r
CJK_Radicals_Supplement = '⺀⺁⺂⺃⺄⺅⺆⺇⺈⺉⺊⺋⺌⺍⺎⺏⺐⺑⺒⺓⺔⺕⺖⺗⺘⺙⺛⺜⺝⺞⺟⺠⺡⺢⺣⺤⺥⺦⺧⺨⺩⺪⺫⺬⺭⺮⺯⺰⺱⺲⺳⺴⺵⺶⺷⺸⺹⺺⺻⺼⺽⺾⺿⻀⻁⻂⻃⻄⻅⻆⻇⻈⻉⻊⻋⻌⻍⻎⻏⻐⻑⻒⻓⻔⻕⻖⻗⻘⻙⻚⻛⻜⻝⻞⻟⻠⻡⻢⻣⻤⻥⻦⻧⻨⻩⻪⻫⻬⻭⻮⻯⻰⻱⻲⻳'
#CJK_Radicals_Supplement








##data##b
CJK_Strokes = '㇀㇁㇂㇃㇄㇅㇆㇇㇈㇉㇊㇋㇌㇍㇎㇏㇐㇑㇒㇓㇔㇕㇖㇗㇘㇙㇚㇛㇜㇝㇞㇟㇠㇡㇢㇣'
#CJK_Strokes








Ideographic_Description_Characters = '⿰⿱⿲⿳⿴⿵⿶⿷⿸⿹⿺⿻'
#Ideographic_Description_Characters








##data##k
Kangxi_Radicals = '⼀⼁⼂⼃⼄⼅⼆⼇⼈⼉⼊⼋⼌⼍⼎⼏⼐⼑⼒⼓⼔⼕⼖⼗⼘⼙⼚⼛⼜⼝⼞⼟⼠⼡⼢⼣⼤⼥⼦⼧⼨⼩⼪⼫⼬⼭⼮⼯⼰⼱⼲⼳⼴⼵⼶⼷⼸⼹⼺⼻⼼⼽⼾⼿⽀⽁⽂⽃⽄⽅⽆⽇⽈⽉⽊⽋⽌⽍⽎⽏⽐⽑⽒⽓⽔⽕⽖⽗⽘⽙⽚⽛⽜⽝⽞⽟⽠⽡⽢⽣⽤⽥⽦⽧⽨⽩⽪⽫⽬⽭⽮⽯⽰⽱⽲⽳⽴⽵⽶⽷⽸⽹⽺⽻⽼⽽⽾⽿⾀⾁⾂⾃⾄⾅⾆⾇⾈⾉⾊⾋⾌⾍⾎⾏⾐⾑⾒⾓⾔⾕⾖⾗⾘⾙⾚⾛⾜⾝⾞⾟⾠⾡⾢⾣⾤⾥⾦⾧⾨⾩⾪⾫⾬⾭⾮⾯⾰⾱⾲⾳⾴⾵⾶⾷⾸⾹⾺⾻⾼⾽⾾⾿⿀⿁⿂⿃⿄⿅⿆⿇⿈⿉⿊⿋⿌⿍⿎⿏⿐⿑⿒⿓⿔⿕'
#Kangxi_Radicals










##data##
香港電腦漢字楷體字形基礎部件表 = r"""
#pg 页码=从部件序号开始(-到部件序号结束)?
#m部件名,h汉字,hx,k康基,r补基,b笔触
#   # hx 引用首例字
#(x|(hk)?部件笔顺码):例字...  #h汉字,hx 可省 笔顺码 为 x
#pg 01=1-15
m平横,h一,k⼀,b㇐
1:一u4E00h,元u5143h,旦u65E6h,吞u541Eh,劍u528Dh,閂u9582h,風u98A8h,衞u885Eh
m提横,b㇀
1:或u6216h,惑u60D1h,國u570Bh,域u57DFh,彧u5F67h
m直竖,h丨,k⼁,b㇑
2:丨u4E28h,在u5728h,存u5B58h,引u5F15h,修u4FEEh,悠u60A0h
m竖钩,h亅,k⼅,b㇚
2:亅u4E85h,亇u4E87h,寜u5BDCh
m撇,h丿,k⼃,b㇓,b㇒
3:丿u4E3Fh,呂u5442h,乏u4E4Fh,星u661Fh,丢u4E22h,么u4E48h,幷u5E77h,呑u5451h
m点,h丶,k⼂,b㇔
4:丶u4E36h,主u4E3Bh,太u592Ah,尤u5C24h,卵u5375h,蚤u86A4h,帆u5E06h,釣u91E3h
m捺,b㇏
4:尺u5C3Ah,uE115h,乆u4E46h
m横捺,h乁
4:乁u4E41h,亪u4EAAh
m提捺,h乀,b㇝
4:乀u4E40h,尐u5C10h
m横钩,h乛,r⺂,b㇖
5:乛u4E5Bh,蛋u86CBh,楚u695Ah,旋u65CBh,疑u7591h,慶u6176h,壽u58FDh,籌u7C4Ch
m横撇,m横折,b㇇
5:今u4ECAh,含u542Bh,岑u5C91h,矜u77DCh,陰u9670h,疏u758Fh,蔬u852Ch
m横折弯钩,h乙,k⼄,b㇠
5:乙u4E59h,乞u4E5Eh,吃u5403h,挖u6316h,疙u7599h
m横竖,h𠃍u200CDh,b㇕ # hk 横竖+横撇 vs gb 横折
5:uF30Bh,巪u5DEAh
m横竖钩,m横折钩,h𠃌u200CCh,b㇆
5:uF7E6h,司u53F8h,詞u8A5Eh,局u5C40h,侷u4FB7h,幻u5E7Bh
m横竖弯钩,r⺄,b㇈
5:虱u8671h,蝨u8768h,訊u8A0Ah,迅u8FC5h,羸u7FB8h
#pg 02=16
m竖弯,b㇄ # hk 竖弯+竖横 vs gb 竖折
5:甚u751Ah,堪u582Ah,斟u659Fh,磡u78E1h,葛u845Bh,喝u559Dh,靄u9744h,蠍u880Dh
m竖横,m竖折,h𠃊u200CAh,b㇗
5:uF311h,斷u65B7h,繼u7E7Ch,陋u964Bh
m竖弯钩,h乚,r⺃,b㇟ #心 作为一个部件，其笔画不是部件? ?心 b㇃ 卧/斜 弯 钩?
5:乚u4E5Ah,乳u4E73h,札u672Dh,紮u7D2Eh,吼u543Ch,輒u8F12h
m竖折折,m竖横竖,h𠃑u200D1h,b㇞
5:uF30Ah,吳u5433h,娛u5A1Bh,俁u4FC1h,悞u609Eh,㻍u3ECDh,呉u5449h,娯u5A2Fh
m撇折折钩,m撇横竖钩,m竖折折钩,m竖横竖钩,b㇉
5:䦇u4987h
m撇折,m撇提,h𠃋u200CBh,b㇜
5:uF30Eh
m竖提,h𠄌u2010Ch,b㇙
5:uF308h
m撇点,h𡿨u21FE8h,b㇛
5:uF30Fh
hx,k⼆
x:二u4E8Ch,仁u4EC1h,勻u52FBh,些u4E9Bh,魂u9B42h,辰u8FB0h,貳u8CB3h,藝u85DDh
hx,k⼗
x:十u5341h,卉u5349h,協u5354h,計u8A08h,南u5357h,真u771Fh,早u65E9h
m敢左角,hx # 敢左角: hk 两笔12 vs gb 一笔5
hk12:丅u4E05h,敢u6562h,橄u6A44h,嚴u56B4h,巖u5DD6h
hx
x:丁u4E01h,亭u4EADh,寧u5BE7h,打u6253h,頂u9802h,貯u8CAFh,行u884Ch,衝u885Dh
m可字框
12:可u53EFh,奇u5947h,歌u6B4Ch,軻u8EFBh,荷u8377h,漪u6F2Ah
m哥字头
12:哥u54E5h,歌u6B4Ch
hx,k⼚
x:厂u5382h,厄u5384h,原u539Fh,炭u70ADh,勵u52F5h,捱u6371h,擔u64D4h,嚴u56B4h
m左字框,h𠂇u20087h
x:uF572h,右u53F3h,希u5E0Ch,宏u5B8Fh,戎u620Eh,雄u96C4h,辣u8FA3h,盔u76D4h
m夏字头,hx
x:丆u4E06h,面u9762h,夏u590Fh,頁u9801h,寡u5BE1h,囂u56C2h,傾u50BEh
#pg 03=33
m七字无钩,m皂字底,hx
15:七u4E03h,皂u7682h,柒u67D2h
m七字带钩,m托右足
15:托u6258h,宅u5B85h,詫u8A6Bh,乇u4E47h
m切字旁,m提七
15:切u5207h,砌u780Ch,袃u8883h
m旨字头,m七字不交无钩 # hk 15 vs gb 35
hk15:旨u65E8h,嘗u5617h,指u6307h,稽u7A3Dh
m比字边,m七字不交带钩 # err: h匕,k⼔
hk15:比u6BD4h,昆u6606h,屁u5C41h,鹿u9E7Fh,琵u7435h,毗u6BD7h,皆u7686h,諧u8AE7h
m比字旁,m提匕
15:比u6BD4h,頃u9803h,皆u7686h,昆u6606h,枇u6787h,麗u9E97h
m号字底,m巧字边,hx
x:丂u4E02h,兮u516Eh,巧u5DE7h,污u6C61h,誇u8A87h,號u865Fh,粵u7CB5h
====TODO 添加 笔顺码
:匚u531Ah,叵u53F5h,匪u532Ah,匱u5331h,愜u611Ch,眶u7736h,筐u7B50h,砸u7838h
:匸u5338h,匹u5339h,匾u533Eh,歐u6B50h,偃u5043h,醫u91ABh
:拷u62F7h,與u8207h,譽u8B7Dh,焉u7109h,嫣u5AE3h,薦u85A6h
:丄u4E04h,啚u555Ah,圖u5716h,鄙u9119h
:貞u8C9Eh,桌u684Ch,鹼u9E7Ch,點u9EDEh,壑u58D1h,寇u5BC7h,鹽u9E7Dh
:刂u5202h,到u5230h,俞u4FDEh,前u524Dh,罰u7F70h,製u88FDh,涮u6DAEh,荊u834Ah
:卜u535Ch,卡u5361h,朴u6734h,赴u8D74h,掛u639Bh,卧u5367h
:冂u5182h,同u540Ch,向u5411h,喬u55ACh,惘u60D8h,備u5099h,亂u4E82h,適u9069h
:奧u5967h,澳u6FB3h,換u63DBh,瓊u74CAh,興u8208h,麗u9E97h
:乞u4E5Eh,無u7121h,敏u654Fh,旗u65D7h,唉u5509h,候u5019h,遊u904Ah,醫u91ABh
#pg 04
:亻u4EBBh,夜u591Ch,雁u96C1h,隻u96BBh,腐u8150h,附u9644h,閥u95A5h,黛u9EDBh
:介u4ECBh,界u754Ch,尬u5C2Ch,疥u75A5h,氘u6C18h
:勿u52FFh,忽u5FFDh,物u7269h,刎u520Eh,湯u6E6Fh,瘍u760Dh,颺u98BAh
:uF53Dh,后u540Eh,叛u53DBh,循u5FAAh,派u6D3Eh,遞u905Eh
:八u516Bh,穴u7A74h,扒u6252h,吩u5429h,公u516Ch,翁u7FC1h,界u754Ch,寒u5BD2h
:谷u8C37h,典u5178h,交u4EA4h,兵u5175h,棋u68CBh,益u76CAh,廣u5EE3h,爾u723Eh
:入u5165h,全u5168h,荃u8343h,詮u8A6Eh,痊u75CAh
:兩u5169h,輛u8F1Bh,懣u61E3h,陝u965Dh
:人u4EBAh,令u4EE4h,浴u6D74h,坎u574Eh,偷u5077h,寥u5BE5h,疥u75A5h
:囚u56DAh,以u4EE5h,刻u523Bh,俎u4FCEh,喝u559Dh,鴿u9D3Fh,幾u5E7Eh,齒u9F52h
:乂u4E42h,爻u723Bh,艾u827Eh,拔u62D4h
:㐅u3405h,凶u51F6h,離u96E2h,希u5E0Ch,殺u6BBAh,腦u8166h,學u5B78h,爽u723Dh
m老字底,m匕字不交无钩
:老u8001h,耆u8006h,姥u59E5h,嗜u55DCh
m北字边,m匕字不交带钩,h匕,k⼔
35:匕u5315h,化u5316h,北u5317h,死u6B7Bh,呢u5462h,疵u75B5h,些u4E9Bh,匙u5319h
m叱字边,m匕字相交带钩 # err: h匕,k⼔
:叱u53F1h
:uF7E8h,危u5371h,魚u9B5Ah,免u514Dh,解u89E3h,煞u715Eh,擔u64D4h,閻u95BBh
:妳u59B3h,欠u6B20h,欺u6B3Ah,厥u53A5h,羨u7FA8h,嗽u55FDh
#pg 05
:用u7528h,周u5468h,週u9031h,嘴u5634h,解u89E3h,懈u61C8h
:勹u52F9h,勾u52FEh,包u5305h,豹u8C79h,忽u5FFDh,楊u694Ah,敬u656Ch,雛u96DBh
:夙u5919h,佩u4F69h,嵐u5D50h,飄u98C4h,瘋u760Bh,颶u98B6h
:几u51E0h,亢u4EA2h,航u822Ah,秃u79C3h,凱u51F1h,凳u51F3h,凡u51E1h,梵u68B5h
:殼u6BBCh,uEB1Ch,䘕u4615h,頏u980Fh,頽u983Dh
:朵u6735h,没u6CA1h,段u6BB5h,發u767Ch,搬u642Ch,盤u76E4h
:兄u5144h,虎u864Eh,允u5141h,兜u515Ch,洗u6D17h,剋u524Bh,贊u8D0Ah,禿u79BFh
:競u7AF6h,頹u9839h,微u5FAEh,贊u8D0Ah
:匹u5339h,空u7A7Ah,詹u8A79h,甚u751Ah,睦u7766h,挖u6316h,俊u4FCAh,船u8239h
:九u4E5Dh,仇u4EC7h,軌u8ECCh,究u7A76h,染u67D3h,旭u65EDh
:鳩u9CE9h,頄u9804h,虓u8653h,uE851h
:兜u515Ch,篼u7BFCh,蔸u8538h,㨮u3A2Eh
:卬u536Ch,昂u6602h,仰u4EF0h,迎u8FCEh
:別u5225h,沒u6C92h,㦲u39B2h,uE364h
:亠u4EA0h,亥u4EA5h,商u5546h,畝u755Dh,停u505Ch,景u666Fh,翠u7FE0h,禽u79BDh
:冫u51ABh,冰u51B0h,次u6B21h,弱u5F31h,冽u51BDh,諮u8AEEh,匀u5300h,决u51B3h
#pg 06
:兌u514Ch
:丷u4E37h,半u534Ah,兌u514Ch,帝u5E1Dh,叛u53DBh,倦u5026h,圈u5708h
:兑u5151h
:兑u5151h
:班u73EDh,辨u8FA8h,帰u5E30h,疈u7588h
:冬u51ACh,於u65BCh,瘀u7600h,斗u6597h,料u6599h,魁u9B41h,蝌u874Ch
:冖u5196h,軍u8ECDh,冠u51A0h,夢u5922h,壹u58F9h,勃u52C3h,侵u4FB5h,學u5B78h
:兜u515Ch,假u5047h,霞u971Eh,遐u9050h
:侯u4FAFh,喉u5589h,候u5019h,猴u7334h,䒭u44ADh
:刁u5201h,叼u53FCh
:凵u51F5h,出u51FAh,凶u51F6h,匈u5308h,離u96E2h,齒u9F52h,涵u6DB5h,屆u5C46h
:卩u5369h,卯u536Fh,卿u537Fh,仰u4EF0h,節u7BC0h,報u5831h,命u547Dh,禦u79A6h
:兯u516Fh,厁u5381h,壭u58EDh
:了u4E86h,亨u4EA8h,烹u70F9h,函u51FDh,涵u6DB5h,丞u4E1Eh,蒸u84B8h
:丩u4E29h,叫u53EBh,收u6536h,糾u7CFEh,赳u8D73h
:力u529Bh,加u52A0h,助u52A9h,勝u52DDh,脅u8105h,辦u8FA6h,别u522Bh,劵u52B5h
:刀u5200h,刃u5203h,召u53ECh,超u8D85h,券u5238h,切u5207h,解u89E3h,齊u9F4Ah
:乆u4E46h,亥u4EA5h,刻u523Bh,咳u54B3h,閡u95A1h
:又u53C8h,奴u5974h,堅u5805h,叉u53C9h,蚤u86A4h,報u5831h,獲u7372h
#pg 07
:桑u6851h,綴u7DB4h,寇u5BC7h,極u6975h,盈u76C8h
:祭u796Dh,際u969Bh,蔡u8521h,擦u64E6h,豋u8C4Bh
:令u4EE4h,聆u8046h,翎u7FCEh,勇u52C7h,涌u6D8Ch,疑u7591h,亂u4E82h
:厶u53B6h,公u516Ch,允u5141h,宏u5B8Fh,麽u9EBDh,私u79C1h,能u80FDh,強u5F37h
:㔾u353Eh,厄u5384h,危u5371h,犯u72AFh,怨u6028h,範u7BC4h,婉u5A49h,卷u5377h
:乜u4E5Ch
:uF316h
:巜u5DDCh,粼u7CBCh,兪u516Ah,喩u55A9h,楡u6961h,偸u5078h,婾u5A7Eh
:㽕u3F55h
:三u4E09h,叄u53C4h,疆u7586h,薑u8591h
:弎u5F0Eh
:半u534Ah,奉u5949h,舉u8209h,用u7528h,周u5468h,勇u52C7h
:干u5E72h,平u5E73h,旱u65F1h,刊u520Ah,肝u809Dh,舌u820Ch,uEB19h,插u63D2h
:于u4E8Eh,盂u76C2h,宇u5B87h,竽u7AFDh,吁u5401h,迂u8FC2h,得u5F97h
:判u5224h,叛u53DBh,頖u9816h,鵥u9D65h
:幵u5E75h,幷u5E77h,倂u5002h
:爰u7230h,萲u8432h,緩u7DE9h,鶢u9DA2h
#pg 08
:亐u4E90h,汚u6C5Ah
:甩u7529h
:土u571Fh,去u53BBh,至u81F3h,佳u4F73h,捱u6371h,掛u639Bh,坐u5750h,嗇u55C7h
:地u5730h,封u5C01h,毀u6BC0h,到u5230h,墫u58ABh,僥u50E5h
:士u58EBh,壯u58EFh,吉u5409h,壬u58ECh,壺u58FAh,喜u559Ch,壽u58FDh,賣u8CE3h
:壻u58FBh,壿u58FFh
:扌u624Ch,打u6253h,提u63D0h,哲u54F2h,拋u62CBh
:工u5DE5h,左u5DE6h,巫u5DEBh,貢u8CA2h,空u7A7Ah,江u6C5Fh,經u7D93h,壽u58FDh
:巧u5DE7h,勁u52C1h,式u5F0Fh,築u7BC9h,尋u5C0Bh,毁u6BC1h,昻u663Bh
:卄u5344h,刑u5211h,開u958Bh,瓶u74F6h,餅u9905h,屏u5C4Fh
:賁u8CC1h,憤u61A4h,噴u5674h,寛u5BDBh
:才u624Dh,財u8CA1h,材u6750h,閉u9589h
:寸u5BF8h,守u5B88h,辱u8FB1h,村u6751h,傅u5085h,冠u51A0h,幫u5E6Bh,籌u7C4Ch
:下u4E0Bh,忑u5FD1h
:廾u5EFEh,升u5347h,卉u5349h,弄u5F04h,蟒u87D2h,戒u6212h
:丌u4E0Ch,亓u4E93h,鼻u9F3Bh,鼾u9F3Eh,畀u7540h,痹u75F9h
#pg 09
:大u5927h,矢u77E2h,吞u541Eh,沃u6C83h,套u5957h,篡u7BE1h,爽u723Dh,夲u5932h
:奇u5947h,奐u5950h,莫u83ABh,咽u54BDh,知u77E5h,鄭u912Dh,猴u7334h
:丈u4E08h,仗u4ED7h,杖u6756h
:兀u5140h,光u5149h,完u5B8Ch,冠u51A0h,鯇u9BC7h,翹u7FF9h,燒u71D2h
:頑u9811h,耀u8000h,輝u8F1Dh,㹕u3E55h,㒯u34AFh
:尢u5C22h,尤u5C24h,就u5C31h,稽u7A3Dh,尷u5C37h,拋u62CBh
:仺u4EFAh
:虐u8650h,瘧u7627h,謔u8B14h,㖸u35B8h
:㐄u3404h,韋u97CBh,葦u8466h,圍u570Dh,舞u821Eh,鄰u9130h,降u964Dh
:至u81F3h,室u5BA4h,屋u5C4Bh,姪u59EAh,倒u5012h,臻u81FBh
:弋u5F0Bh,代u4EE3h,式u5F0Fh,軾u8EFEh,武u6B66h,鵡u9D61h,貳u8CB3h,鳶u9CF6h
:夨u5928h,奊u594Ah,捑u6351h
:上u4E0Ah,卡u5361h,叔u53D4h,戚u621Ah,督u7763h,椒u6912h
:北u5317h,背u80CCh,乖u4E56h,燕u71D5h,剩u5269h,冀u5180h
:以u4EE5h,似u4F3Ch
:步u6B65h,蘋u860Bh,賓u8CD3h,歲u6B72h
:小u5C0Fh,尖u5C16h,劣u52A3h,原u539Fh,叔u53D4h,掠u63A0h,渺u6E3Ah
#pg 10
:尘u5C18h,尙u5C19h,覍u898Dh,尜u5C1Ch,歩u6B69h
:尚u5C1Ah,趟u8D9Fh,光u5149h,宵u5BB5h,瑣u7463h,削u524Ah,常u5E38h,輝u8F1Dh
:口u53E3h,占u5360h,吐u5410h,扣u6263h,高u9AD8h,强u5F3Ah,袞u889Eh,吕u5415h
:囗u56D7h,回u56DEh,嗇u55C7h,檀u6A80h,面u9762h,國u570Bh,氤u6C24h,鹽u9E7Dh
:山u5C71h,仙u4ED9h,峽u5CFDh,崇u5D07h,岔u5C94h,岡u5CA1h,豐u8C50h,島u5CF6h
:巾u5DFEh,帝u5E1Dh,匝u531Dh,帆u5E06h,師u5E2Bh,席u5E2Dh,滿u6EFFh
:繭u7E6Dh,襺u897Ah
:監u76E3h,濫u6FEBh,籃u7C43h,艦u8266h,覽u89BDh
:千u5343h,仟u4EDFh,乖u4E56h
:刋u520Bh,叐u53D0h,圱u5731h,谸u8C38h
:扥u6265h
:川u5DDDh,順u9806h,訓u8A13h
:流u6D41h,蔬u852Ch,侃u4F83h,荒u8352h
:彳u5F73h,很u5F88h,街u8857h,屜u5C5Ch,懲u61F2h,蹤u8E64h
:彡u5F61h,形u5F62h,須u9808h,珍u73CDh,參u53C3h,彪u5F6Ah,修u4FEEh
:匆u5306h,濍u6FCDh,葱u8471h,囪u56EAh
#pg 11
:印u5370h,褎u890Eh,襃u8943h
:犭u72ADh,狗u72D7h,獅u7345h,逛u901Bh,誑u8A91h,嶽u5DBDh
:卯u536Fh,卿u537Fh,聊u804Ah,卵u5375h
:黎u9ECEh,犂u7282h
:執u57F7h,塾u587Eh,熱u71B1h,褻u893Bh,囈u56C8h
:丸u4E38h,芄u8284h,汍u6C4Dh,紈u7D08h,肒u8092h,骫u9AABh,奿u597Fh
:齊u9F4Ah,濟u6FDFh,劑u5291h,霽u973Dh,齋u9F4Bh
:夕u5915h,爹u7239h,夠u5920h,外u5916h,宛u5B9Bh,鴛u9D1Bh,瞬u77ACh
:囱u56F1h,窗u7A97h,總u7E3Dh,麥u9EA5h,嘜u561Ch
:夂u5902h,冬u51ACh,咎u548Eh,峰u5CF0h,愛u611Bh,腹u8179h,俊u4FCAh
:夊u590Ah
:久u4E45h,玖u7396h,灸u7078h,疚u759Ah,柩u67E9h
:广u5E7Fh,度u5EA6h,廣u5EE3h,廂u5EC2h,傭u50ADh,鷓u9DD3h,遮u906Eh
:亡u4EA1h,忙u5FD9h,忘u5FD8h,望u671Bh,氓u6C13h,荒u8352h,網u7DB2h,贏u8D0Fh
:䒑u4491h,並u4E26h,并u5E76h,豆u8C46h,孳u5B73h,喜u559Ch,剛u525Bh
:頭u982Dh,凱u51F1h,澎u6F8Eh,樹u6A39h
:丫u4E2Bh,吖u5416h
#pg 12
:齊u9F4Ah,濟u6FDFh,劑u5291h,霽u973Dh,齋u9F4Bh
:丬u4E2Ch,奨u5968h,荘u8358h
:赱u8D71h
:労u52B4h,単u5358h,弾u5F3Eh,厳u53B3h,栄u6804h
:氵u6C35h,沖u6C96h,決u6C7Ah,況u6CC1h,游u6E38h,衍u884Dh,染u67D3h,樑u6A11h
:忄u5FC4h,快u5FEBh,憤u61A4h,懶u61F6h,罹u7F79h
:宀u5B80h,穴u7A74h,寵u5BF5h,管u7BA1h,館u9928h,崇u5D07h,剜u525Ch
:鶴u9DB4h,確u78BAh,uE148h
:之u4E4Bh,芝u829Dh,乏u4E4Fh,泛u6CDBh
:彐u5F50h,剥u5265h
:雪u96EAh,慧u6167h,尋u5C0Bh,歸u6B78h
:uE796h,榋u698Bh
:韋u97CBh,偉u5049h,韌u97CCh,違u9055h,闈u95C8h,圍u570Dh
:叏u53CFh
:尸u5C38h,尾u5C3Eh,刷u5237h,潺u6F7Ah,擘u64D8h,旎u65CEh
:巳u5DF3h,包u5305h,抱u62B1h,刨u5228h,雹u96F9h,起u8D77h,巷u5DF7h,港u6E2Fh
:攺u653Ah
#pg 13
:巽u5DFDh,熙u7199h,撰u64B0h
:已u5DF2h,uE0BCh
:己u5DF1h,記u8A18h,忌u5FCCh,巻u5DFBh
:改u6539h,妀u5980h,邔u9094h
:弓u5F13h,張u5F35h,弱u5F31h,粥u7CA5h,彎u5F4Eh,發u767Ch
:屮u5C6Eh,出u51FAh,屈u5C48h,黜u9EDCh,嗤u55E4h
:艸u8278h,逆u9006h,塑u5851h,厥u53A5h,芻u82BBh,皺u76BAh,趨u8DA8h
:子u5B50h,李u674Eh,好u597Dh,孟u5B5Fh,孱u5B71h,浮u6D6Eh,學u5B78h
:孑u5B51h,孖u5B56h,乳u4E73h,勃u52C3h,孱u5B71h,熟u719Fh
:孓u5B53h
:也u4E5Fh,他u4ED6h,馳u99B3h,匜u531Ch,竾u7AFEh
:女u5973h,妝u599Dh,安u5B89h,嬰u5B30h,縷u7E37h,姦u59E6h
:她u5979h,嫡u5AE1h,努u52AAh,呶u5476h,茹u8339h,姦u59E6h
:喪u55AAh,展u5C55h,輾u8F3Eh,畏u754Fh,偎u504Eh,餵u9935h
:丞u4E1Eh,拯u62EFh,蒸u84B8h
:刄u5204h,劔u5294h,靱u9771h,仭u4EEDh,釼u91FCh,匁u5301h
:羽u7FBDh,習u7FD2h,翔u7FD4h,翅u7FC5h,扇u6247h,膠u81A0h
#pg 14
:厯u53AFh
:彑u5F51h,互u4E92h,剝u525Dh,錄u9304h,彙u5F59h,彝u5F5Dh,篆u7BC6h
:阝u961Dh,陽u967Dh,都u90FDh,窿u7ABFh,鄉u9109h,墮u58AEh,隧u96A7h
:乃u4E43h,仍u4ECDh,秀u79C0h,透u900Fh,朶u6736h,盈u76C8h,孕u5B55h
:雍u96CDh,擁u64C1h,甕u7515h,鄉u9109h,嚮u56AEh
:廴u5EF4h,建u5EFAh,健u5065h,毽u6BFDh,庭u5EADh,延u5EF6h,筵u7B75h,誕u8A95h
:幺u5E7Ah,幼u5E7Ch,玄u7384h,後u5F8Ch,麼u9EBCh,幽u5E7Dh,幾u5E7Eh,雞u96DEh
:巛u5DDBh,災u707Dh,巡u5DE1h,剿u527Fh,腦u8166h,經u7D93h,莖u8396h,痙u75D9h
:慧u6167h,豐u8C50h,艷u8277h,契u5951h,潔u6F54h,烽u70FDh,縫u7E2Bh
:鋳u92F3h
:王u738Bh,丟u4E1Fh,匡u5321h,琶u7436h,旺u65FAh,閏u958Fh,皇u7687h,鱷u9C77h
:珠u73E0h,斑u6591h,瑯u746Fh,寶u5BF6h,琴u7434h
:生u751Fh,青u9752h,產u7522h,甦u7526h,隆u9686h,星u661Fh,績u7E3Eh
:甥u7525h,戥u6225h,甡u7521h,甧u7527h,㽓u3F53h
:井u4E95h,阱u9631h,耕u8015h
:夫u592Bh,扶u6276h,失u5931h,跌u8DCCh,卷u5377h,騰u9A30h
:規u898Fh,窺u7ABAh,替u66FFh
#pg 15
:発u767Ah,廃u5EC3h
:㒫u34ABh
:耂u8002h,老u8001h,嗜u55DCh,者u8005h,暑u6691h,拷u62F7h,教u6559h
:丐u4E10h,鈣u9223h,麫u9EABh
:艹u8279h,芥u82A5h,蕭u856Dh,藏u85CFh,厲u53B2h,匿u533Fh,嚿u56BFh,孶u5B76h
:寬u5BECh,敬u656Ch,權u6B0Ah,護u8B77h,夢u5922h
:卝u535Dh,㐀u3400h
:共u5171h,暴u66B4h,展u5C55h,借u501Fh,藉u85C9h,散u6563h,黄u9EC4h
:廿u5EFFh,度u5EA6h,遮u906Eh,燕u71D5h,滿u6EFFh,黃u9EC3h,謹u8B39h
:木u6728h,林u6797h,保u4FDDh,採u63A1h,柔u67D4h,痳u75F3h,來u4F86h
:村u6751h,杏u674Fh,困u56F0h,焚u711Ah,雜u96DCh,膝u819Dh,森u68EEh
:朩u6729h,余u4F59h,除u9664h,斜u659Ch
:朮u672Eh,殺u6BBAh,術u8853h,痲u75F2h
:五u4E94h,伍u4F0Dh,吾u543Eh,語u8A9Eh,衙u8859h
:兩u5169h,輛u8F1Bh,爾u723Eh,璽u74BDh,彌u5F4Ch
:巿u5DFFh
:巿u5DFFh,沛u6C9Bh,肺u80BAh,芾u82BEh
:丏u4E0Fh,麪u9EAAh,沔u6C94h
#pg 16
:卅u5345h,uE064h
:不u4E0Dh,杯u676Fh,歪u6B6Ah,盃u76C3h,痞u75DEh
:犬u72ACh,伏u4F0Fh,突u7A81h,獸u7378h,獄u7344h,厭u53ADh
:器u5668h,類u985Eh,饜u995Ch,獎u734Eh
:歹u6B79h,夙u5919h,列u5217h,烈u70C8h,殤u6BA4h,死u6B7Bh
:戸u6238h
:牙u7259h,呀u5440h,邪u90AAh,穿u7A7Fh,芽u82BDh
:屯u5C6Fh,純u7D14h,囤u56E4h,頓u9813h
:戈u6208h,伐u4F10h,戛u621Bh,划u5212h,國u570Bh,盞u76DEh,踐u8E10h
:旡u65E1h,既u65E2h,慨u6168h,概u6982h,暨u66A8h
:兓u5153h,蠶u8836h,簪u7C2Ah,僭u50EDh,潛u6F5Bh
:面u9762h,緬u7DECh,靦u9766h,靨u9768h,髙u9AD9h
:止u6B62h,企u4F01h,步u6B65h,齒u9F52h,歲u6B72h,址u5740h,整u6574h,焉u7109h
:歧u6B67h,武u6B66h,歸u6B78h,此u6B64h,嘴u5634h,疏u758Fh
:足u8DB3h,從u5F9Eh,疋u758Bh,疑u7591h,走u8D70h,赴u8D74h
:日u65E5h,時u6642h,汨u6C68h,旦u65E6h,旬u65ECh,章u7AE0h,者u8005h
:曰u66F0h,汩u6C69h,會u6703h,層u5C64h,勗u52D7h,槽u69FDh
#pg 17
:冒u5192h,冕u5195h,最u6700h,曼u66FCh
:冃u5183h,冑u5191h
:有u6709h,肩u80A9h,青u9752h,清u6E05h,能u80FDh,贏u8D0Fh,胤u80E4h,胄u80C4h
:冄u5184h,枏u678Fh,耼u803Ch
:衰u8870h,蓑u84D1h,簑u7C11h
:中u4E2Dh,仲u4EF2h,盅u76C5h,衷u8877h,簣u7C23h,遺u907Ah,匱u5331h
:uE23Bh
:円u5186h,靑u9751h,淸u6DF8h
:象u8C61h,橡u6A61h,晩u6669h
:雋u96CBh,嶲u5DB2h,鐫u942Bh
:水u6C34h,冰u51B0h,泉u6CC9h,尿u5C3Fh,盥u76E5h
:内u5185h,丙u4E19h,柄u67C4h,病u75C5h,陋u964Bh
:內u5167h,納u7D0Dh,芮u82AEh
:丰u4E30h,害u5BB3h,瞎u778Eh,割u5272h,憲u61B2h
:牛u725Bh,件u4EF6h,牢u7262h,牽u727Dh,犀u7280h,眸u7738h,解u89E3h,告u544Ah
:手u624Bh,掌u638Ch,摩u6469h,攀u6500h
#pg 18
:齊u9F4Ah,劑u5291h,濟u6FDFh,霽u973Dh,斉u6589h
:邦u90A6h,梆u6886h,綁u7D81h
:看u770Bh,拜u62DCh,湃u6E43h
:毛u6BDBh,尾u5C3Eh,毫u6BEBh,耗u8017h,毯u6BEFh,橇u6A47h,㲎u3C8Eh
:氣u6C23h,氧u6C27h,氳u6C33h,汽u6C7Dh
:牲u7272h,牧u7267h,犢u72A2h
:先u5148h,洗u6D17h,贊u8D0Ah
:攵u6535h,攻u653Bh,敢u6562h,變u8B8Ah,條u689Dh,做u505Ah,廠u5EE0h,繁u7E41h
:片u7247h,牌u724Ch,牘u7258h
:亦u4EA6h,奕u5955h,跡u8DE1h,赤u8D64h,螫u87ABh,嚇u5687h
:斤u65A4h,匠u5320h,斧u65A7h,欣u6B23h,近u8FD1h,斬u65ACh,廝u5EDDh,質u8CEAh
:爪u722Ah,抓u6293h,爬u722Ch
:丯u4E2Fh
:戶u6236h,所u6240h
:父u7236h,交u4EA4h,斧u65A7h,爸u7238h,爺u723Ah,爹u7239h
:爫u722Bh,妥u59A5h,受u53D7h,乳u4E73h,滔u6ED4h,辭u8FADh
:胖u80D6h,筋u7B4Bh,淝u6DDDh,膧u81A7h
#pg 19
:月u6708h,朋u670Bh,朗u6717h,藤u85E4h,朣u6723h,盟u76DFh,廟u5EDFh
:uEE56h
:丹u4E39h,坍u574Dh,彤u5F64h
:氏u6C0Fh,昏u660Fh,紙u7D19h,氐u6C10h,底u5E95h,低u4F4Eh,邸u90B8h
:uEABFh,姊u59CAh,笫u7B2Bh
:㸦u3E26h
:旅u65C5h,派u6D3Eh,脈u8108h
:uF7EEh,哀u54C0h,表u8868h,裹u88F9h,囊u56CAh,壞u58DEh,轅u8F45h
:園u5712h,遠u9060h,圜u571Ch
:炙u7099h,祭u796Dh,將u5C07h,遙u9059h,然u7136h,埓u57D3h
:亙u4E99h,恆u6046h
:夜u591Ch,液u6DB2h,掖u6396h,腋u814Bh
:文u6587h,吝u541Dh,紋u7D0Bh,紊u7D0Ah,虔u8654h,斐u6590h
:彥u5F65h,斑u6591h,憫u61ABh,斌u658Ch
:函u51FDh,脊u810Ah,率u7387h,康u5EB7h,隸u96B8h,逮u902Eh
:方u65B9h,坊u574Ah,旅u65C5h,倣u5023h,旁u65C1h,瘀u7600h,房u623Fh
:隔u9694h,融u878Dh,獻u737Bh,嗝u55DDh
#pg 20
:火u706Bh,炎u708Eh,灰u7070h,伙u4F19h,災u707Dh,燄u71C4h
:燒u71D2h,勞u52DEh,愁u6101h,盔u76D4h,滅u6EC5h
:忝u5FDDh,恭u606Dh,慕u6155h
:灬u706Ch,然u7136h,庶u5EB6h,盡u76E1h,駒u99D2h,鳥u9CE5h,鵬u9D6Ch
:户u6237h,妒u5992h,匾u533Eh,遍u904Dh,篇u7BC7h,肇u8087h,戾u623Eh
:礻u793Bh,祖u7956h,視u8996h,禪u79AAh,禱u79B1h
:冘u5198h,沈u6C88h,忱u5FF1h,枕u6795h,耽u803Dh
:鴆u9D06h,邥u90A5h,瓭u74EDh,䪴u4AB4h,䧵u49F5h,㱽u3C7Dh
:心u5FC3h,沁u6C81h,想u60F3h,悶u60B6h,慶u6176h,寧u5BE7h,愛u611Bh,廳u5EF3h
:辶u8FB6h,進u9032h,隨u96A8h,譴u8B74h,蓬u84ECh,導u5C0Eh
:肀u8080h,唐u5510h,塘u5858h,搪u642Ah,糖u7CD6h
:康u5EB7h,慷u6177h,逮u902Eh,隸u96B8h
:爭u722Dh,崢u5D22h,錚u931Ah,靜u975Ch
:尹u5C39h,伊u4F0Ah,君u541Bh,窘u7A98h,裙u88D9h,郡u90E1h
:倉u5009h,搶u6436h,創u5275h,蒼u84BCh,瘡u7621h
:那u90A3h,哪u54EAh
:卐u5350h
#pg 21
:夬u592Ch,決u6C7Ah,快u5FEBh,缺u7F3Ah
:尺u5C3Ah,咫u54ABh,呎u544Eh
:弔u5F14h,第u7B2Ch,弟u5F1Fh,梯u68AFh,剃u5243h
:丑u4E11h,扭u626Dh,紐u7D10h,羞u7F9Eh
:卍u534Dh
:䴡u4D21h
:爿u723Fh,壯u58EFh,裝u88DDh,寢u5BE2h,鏘u93D8h,莊u838Ah,奬u596Ch
:眉u7709h,媚u5A9Ah,聲u8072h
:巴u5DF4h,吧u5427h,爸u7238h,邑u9091h,滬u6EECh,爬u722Ch
:臧u81E7h,贓u8D13h,藏u85CFh,臟u81DFh,贜u8D1Ch
:予u4E88h,序u5E8Fh,舒u8212h,預u9810h
:毌u6BCCh,貫u8CABh,慣u6163h,實u5BE6h
:毋u6BCBh,毐u6BD0h
:及u53CAh,岌u5C8Ch,汲u6C72h,吸u5438h
:葘u8458h,湽u6E7Dh,㿳u3FF3h
:uE794h
:uEEB7h
#pg 22
:春u6625h,樁u6A01h,蠢u8822h,臻u81FBh
:玉u7389h,瑩u7469h,璧u74A7h,鈺u923Ah
:襄u8944h,囊u56CAh,壤u58E4h,寒u5BD2h,溝u6E9Dh
:示u793Ah,宗u5B97h,鬃u9B03h,察u5BDFh,標u6A19h,款u6B3Eh,蒜u849Ch
:未u672Ah,味u5473h,寐u5BD0h,朱u6731h,蛛u86DBh,業u696Dh
:魅u9B45h,犛u729Bh,釐u91D0h,膥u81A5h,鴸u9D38h
:末u672Bh,抹u62B9h,茉u8309h
:逓u9013h,乕u4E55h
:世u4E16h,泄u6CC4h,屜u5C5Ch,諜u8ADCh,葉u8449h
:甘u7518h,甜u751Ch,某u67D0h,謀u8B00h,箝u7B9Dh,嵌u5D4Ch,疳u75B3h
:枾u67BEh
:本u672Ch,笨u7B28h,缽u7F3Dh
:翉u7FC9h
:巨u5DE8h,拒u62D2h,渠u6E20h,苣u82E3h
:囊u56CAh,攮u652Eh,蠹u8839h,橐u6A50h
:石u77F3h,岩u5CA9h,碗u7897h,磨u78E8h,砌u780Ch,礬u792Ch
:戊u620Ah,茂u8302h,威u5A01h,歲u6B72h,咸u54B8h,箴u7BB4h,憾u61BEh
#pg 23
:妻u59BBh,淒u6DD2h,棲u68F2h,萋u840Bh
:戉u6209h,越u8D8Ah,鉞u925Eh,魆u9B46h
:凸u51F8h,uF440h
:歺u6B7Ah,餐u9910h,燦u71E6h,韰u97F0h
:丗u4E17h,帯u5E2Fh
:卌u534Ch,無u7121h,蕪u856Ah,撫u64ABh,舞u821Eh
:瓦u74E6h,瓷u74F7h,瓶u74F6h,甕u7515h
:並u4E26h,普u666Eh,業u696Dh,僕u50D5h,對u5C0Dh,鑿u947Fh,虚u865Ah
:眔u7714h
:泰u6CF0h,暴u66B4h,錄u9304h,剝u525Dh,黏u9ECFh,藤u85E4h
:犀u7280h,屬u5C6Ch,鰥u9C25h,懷u61F7h
:目u76EEh,相u76F8h,睛u775Bh,冒u5192h,算u7B97h,夏u590Fh,督u7763h,瞿u77BFh
:且u4E14h,宜u5B9Ch,組u7D44h,疽u75BDh,寡u5BE1h,疊u758Ah
:助u52A9h,鋤u92E4h,勗u52D7h,雎u96CEh
:蝦u8766h,假u5047h,遐u9050h,霞u971Eh
:申u7533h,伸u4F38h,暢u66A2h
:甲u7532h,呷u5477h,鉀u9240h,匣u5323h,閘u9598h,鴨u9D28h
#pg 24
:曱u66F1h
:由u7531h,油u6CB9h,宙u5B99h,聘u8058h,黃u9EC3h,迪u8FEAh,演u6F14h
:甴u7534h
:奄u5944h,電u96FBh,淹u6DF9h,黾u9EFEh,䋲u42F2h
:鵪u9D6Ah
:竜u7ADCh,篭u7BEDh,滝u6EDDh
:田u7530h,佃u4F43h,甸u7538h,畔u7554h,畜u755Ch,男u7537h,副u526Fh,韁u97C1h
:冉u5189h,購u8CFCh,稱u7A31h,苒u82D2h,髯u9AEFh,再u518Dh
:央u592Eh,鴦u9D26h
:英u82F1h,映u6620h,盎u76CEh
:剣u5263h,倹u5039h
:史u53F2h,駛u99DBh,㳏u3CCFh,鉂u9242h
:免u514Dh,晚u665Ah,勉u52C9h,冕u5195h,兔u5154h,冤u51A4h,饞u995Eh
:兎u514Eh
:官u5B98h,管u7BA1h,綰u7DB0h,耜u801Ch,遣u9063h
:㠯u382Fh
:皿u76BFh,血u8840h,寧u5BE7h,盈u76C8h,溫u6EABh,闔u95D4h
#pg 25
:卹u5379h,衅u8845h,鸕u9E15h
:侖u4F96h,扁u6241h,遍u904Dh,崙u5D19h,嗣u55E3h
:冊u518Ah,柵u67F5h,刪u522Ah
:册u518Ch,㹪u3E6Ah,删u5220h,姗u59D7h,栅u6805h
:罒u7F52h,買u8CB7h,賣u8CE3h,覽u89BDh,屬u5C6Ch,廳u5EF3h,環u74B0h,嘪u562Ah
:四u56DBh,泗u6CD7h,駟u99DFh,讀u8B80h,竇u7AC7h
:禸u79B8h,禽u79BDh,璃u7483h,離u96E2h,籬u7C6Ch
:乍u4E4Dh,作u4F5Ch,怎u600Eh,窄u7A84h
:禾u79BEh,秦u79E6h,酥u9165h,蘇u8607h,乘u4E58h
:和u548Ch,秀u79C0h,穎u7A4Eh,魏u9B4Fh,菌u83CCh,歷u6B77h
:段u6BB5h,鍛u935Bh,葮u846Eh
:丘u4E18h,兵u5175h,岳u5CB3h,蚯u86AFh
:邱u90B1h,屔u5C54h
:白u767Dh,習u7FD2h,伯u4F2Fh,皎u768Eh,帛u5E1Bh,卽u537Dh
:斥u65A5h,坼u577Ch,拆u62C6h,訴u8A34h
#pg 26
:瓜u74DCh,弧u5F27h,菰u83F0h
:瓣u74E3h,寙u5BD9h,窳u7AB3h,蓏u84CFh,瓥u74E5h,㺠u3EA0h
:乎u4E4Eh,呼u547Ch,虖u8656h,歑u6B51h,罅u7F45h
:㸔u3E14h
:丱u4E31h,關u95DCh,聯u806Fh,壣u58E3h
:留u7559h,榴u69B4h,瘤u7624h,劉u5289h
:疒u7592h,病u75C5h,疾u75BEh,癬u766Ch,瘧u7627h,瘋u760Bh
:立u7ACBh,泣u6CE3h,剖u5256h,音u97F3h,龍u9F8Dh,竪u7AEAh,彦u5F66h
:站u7AD9h,竣u7AE3h,竭u7AEDh,端u7AEFh,靖u9756h,颯u98AFh
:丵u4E35h,凿u51FFh,圅u5705h,鑿u947Fh,糳u7CF3h,叢u53E2h,幸u5E78h
:衤u8864h,初u521Dh,補u88DCh,褓u8913h,褪u892Ah
:必u5FC5h,泌u6CCCh,密u5BC6h,瑟u745Fh
:永u6C38h,詠u8A60h,泳u6CF3h,樣u6A23h,昶u6636h
:盡u76E1h,儘u5118h
:庚u5E9Ah,菮u83EEh,賡u8CE1h,㹹u3E79h,uEB18h,掶u63B6h,椩u6929h,焿u713Fh
:鶊u9D8Ah
:即u5373h,節u7BC0h,卿u537Fh,爵u7235h,郎u90CEh,廊u5ECAh,響u97FFh
#pg 27
:民u6C11h,眠u7720h,刡u5221h,暋u668Bh,笢u7B22h
:弗u5F17h,費u8CBBh,佛u4F5Bh,氟u6C1Fh
:凹u51F9h,兕u5155h,㾎u3F8Eh,垇u5787h,uF481h
:皮u76AEh,坡u5761h,疲u75B2h,皺u76BAh,簸u7C38h
:頗u9817h,皰u76B0h,婆u5A46h,櫇u6AC7h
:癶u7676h,發u767Ch,廢u5EE2h,證u8B49h,鄧u9127h,凳u51F3h,葵u8475h,闋u95CBh
:矛u77DBh,柔u67D4h,茅u8305h,務u52D9h,霧u9727h,橘u6A58h,騖u9A16h
:母u6BCDh,姆u59C6h,每u6BCFh,毓u6BD3h,霉u9709h,繁u7E41h
:馬u99ACh,碼u78BCh,驢u9A62h,憑u6191h,闖u95D6h,驚u9A5Ah,羈u7F88h,慿u617Fh
:㦮u39AEh,銭u92ADh,䬻u4B3Bh
:耳u8033h,茸u8338h,洱u6D31h,輯u8F2Fh,聞u805Eh,聲u8072h
:取u53D6h,娶u5A36h,趣u8DA3h,最u6700h,嚴u56B4h,聽u807Dh,聶u8076h
:其u5176h,箕u7B95h,麒u9E92h,廝u5EDDh,簸u7C38h,堪u582Ah,基u57FAh
:帶u5E36h,滯u6EEFh,廗u5ED7h,蔕u8515h,遰u9070h
:晋u664Bh,戬u622Ch,垩u57A9h
:叀u53C0h,曺u66FAh,穂u7A42h,恵u6075h,専u5C02h
:吏u540Fh,使u4F7Fh,㤦u3926h,㹬u3E6Ch
#pg 28
:覀u8980h,要u8981h,飄u98C4h,譚u8B5Ah,覆u8986h,遷u9077h
:襾u897Eh,䙴u4674h,覇u8987h,覉u8989h,覊u898Ah
:朿u673Fh,棘u68D8h,棗u68D7h,策u7B56h,鏼u93FCh
:刺u523Ah,莿u83BFh,棘u68D8h,棗u68D7h,襋u894Bh
:㐁u3401h,䇧u41E7h,弻u5F3Bh
:西u897Fh,哂u54C2h,迺u8FFAh,茜u831Ch,氥u6C25h,甄u7504h
:而u800Ch,耍u800Dh,耐u8010h,端u7AEFh,需u9700h
:uE45Eh
:夷u5937h,咦u54A6h,胰u80F0h,姨u59E8h,荑u8351h,痍u75CDh
:臣u81E3h,臥u81E5h,宦u5BA6h,堅u5805h,藍u85CDh,纜u7E9Ch,姫u59EBh
:彧u5F67h,稶u7A36h,uEC84h
:虍u864Dh,虎u864Eh,遞u905Eh,劇u5287h,戲u6232h,墟u589Fh,慮u616Eh,廬u5EECh
:虛u865Bh,噓u5653h,墟u589Fh,驉u9A49h,魖u9B56h,鱋u9C4Bh
:歔u6B54h,覷u89B7h,戱u6231h,㩬u3A6Ch
:置u7F6Eh,具u5177h,俱u4FF1h,颶u98B6h,顛u985Bh,闐u95D0h
:單u55AEh,彈u5F48h,戰u6230h,簞u7C1Eh,闡u95E1h
:uE4CDh,uE4CEh
#pg 29
:茰u8330h,㻀u3EC0h,㤤u3924h
:㬰u3B30h,螤u87A4h
:曳u66F3h,拽u62FDh,洩u6D29h,跩u8DE9h
:虹u8679h,蚤u86A4h,風u98A8h,燭u71EDh,屬u5C6Ch,蟲u87F2h
:曲u66F2h,農u8FB2h,體u9AD4h,蛐u86D0h,髷u9AF7h
:典u5178h,碘u7898h,痶u75F6h,覥u89A5h
:冎u518Eh,渦u6E26h,過u904Eh,萵u8435h,窩u7AA9h
:骨u9AA8h,滑u6ED1h,骼u9ABCh,髓u9AD3h
:狦u72E6h
:曾u66FEh,增u589Eh,會u6703h,劊u528Ah,繪u7E6Ah
:肉u8089h,瘸u7638h,臠u81E0h
:年u5E74h,姩u59E9h,uF483h,鵇u9D47h
:卸u5378h,啣u5563h,禦u79A6h,篽u7BFDh
:耒u8012h,誄u8A84h,銇u9287h
:耕u8015h,耙u8019h,籍u7C4Dh,耡u8021h
:缶u7F36h,缸u7F38h,陶u9676h,萄u8404h,鷂u9DC2h,寶u5BF6h,罄u7F44h,鬱u9B31h
:制u5236h,製u88FDh,淛u6DDBh,痸u75F8h
#pg 30
:竹u7AF9h
:笛u7B1Bh,筆u7B46h,筏u7B4Fh,噬u566Ch,篷u7BF7h
:乑u4E51h,衆u8846h
:眾u773Eh,聚u805Ah,驟u9A5Fh,藂u85C2h,鄹u9139h
:臼u81FCh,兒u5152h,舂u8202h,插u63D2h,寫u5BEBh,燄u71C4h,韜u97DCh,鼬u9F2Ch
:自u81EAh,咱u54B1h,鼻u9F3Bh,臭u81EDh,道u9053h,邊u908Ah,憩u61A9h
:卑u5351h,碑u7891h,顰u9870h,痺u75FAh
:烏u70CFh,鎢u93A2h,歍u6B4Dh
:阜u961Ch,追u8FFDh,歸u6B78h,師u5E2Bh,獅u7345h,薛u859Bh,孽u5B7Dh
:㐆u3406h,殷u6BB7h,慇u6147h,蒑u8491h,溵u6EB5h,磤u78E4h
:舟u821Fh,洀u6D00h
:船u8239h,盤u76E4h,搬u642Ch
:鹵u9E75h,鹹u9E79h,鹽u9E7Dh,鬯u9B2Fh,鬱u9B31h
:uF409h
:彖u5F56h,篆u7BC6h,緣u7DE3h
:毅u6BC5h,蠡u8821h,鶨u9DA8h,墬u58ACh
:兆u5146h,跳u8DF3h,逃u9003h,窕u7A95h
#pg 31
:售u552Eh,准u51C6h,確u78BAh,崔u5D14h,奪u596Ah,匯u532Fh,羅u7F85h
:羊u7F8Ah,氧u6C27h,癬u766Ch,羣u7FA3h,達u9054h,羸u7FB8h
:羚u7F9Ah,羯u7FAFh,羶u7FB6h,翔u7FD4h
:uEEB4h,美u7F8Eh,差u5DEEh,着u7740h,糕u7CD5h
:米u7C73h,粟u7C9Fh,咪u54AAh,糜u7CDCh,燦u71E6h
:料u6599h,迷u8FF7h,菊u83CAh,澳u6FB3h,糞u7CDEh,奥u5965h
:州u5DDEh,洲u6D32h,酬u916Ch
:聿u807Fh,律u5F8Bh,建u5EFAh,筆u7B46h,肇u8087h
:肅u8085h,蕭u856Dh,繡u7E61h,瀟u701Fh
:書u66F8h,晝u665Dh,畫u756Bh,劃u5283h
:䏋u43CBh
:帇u5E07h
:艮u826Eh,良u826Fh,很u5F88h,墾u58BEh,痕u75D5h
:退u9000h,褪u892Ah,郞u90DEh
:衣u8863h,依u4F9Dh,袋u888Bh,裔u88D4h,嬝u5B1Dh
:裁u88C1h,衾u887Eh,褰u8930h,攐u6510h,搇u6407h,uF50Ah
:臦u81E6h,燛u71DBh,臩u81E9h
#pg 32
:糸u7CF8h,系u7CFBh,素u7D20h,絲u7D72h,潔u6F54h,徽u5FBDh,辮u8FAEh
:糹u7CF9h,紅u7D05h,葯u846Fh,戀u6200h,羅u7F85h,灣u7063h
:镸u9578h,套u5957h,肆u8086h,髮u9AEEh
:畱u7571h,橊u6A4Ah,癅u7645h,籒u7C52h,飅u98C5h
:求u6C42h,球u7403h,俅u4FC5h,莍u838Dh
:救u6551h,裘u88D8h,逑u9011h,毬u6BECh
:車u8ECAh,輔u8F14h,連u9023h,輩u8F29h,輿u8F3Fh,載u8F09h,慚u615Ah,轟u8F5Fh
:甫u752Bh,莆u8386h,傅u5085h,捕u6355h,匍u530Dh,圃u5703h,簿u7C3Fh
:更u66F4h,甦u7526h,硬u786Ch,鞭u97ADh
:郠u90E0h
:曹u66F9h,糟u7CDFh,遭u906Dh
:亜u4E9Ch,唖u5516h,悪u60AAh
:束u675Fh,悚u609Ah,辣u8FA3h
:剌u524Ch,速u901Fh,懶u61F6h,整u6574h,嫩u5AE9h,癩u7669h,籟u7C5Fh
:栆u6806h
:酉u9149h,酣u9163h,酒u9152h,醫u91ABh,酋u914Bh,鄭u912Dh,遵u9075h
:唡u5521h
#pg 33
:丣u4E23h,駵u99F5h,䱖u4C56h,桺u687Ah
:㳤u3CE4h
:豕u8C55h,家u5BB6h,豪u8C6Ah,豚u8C5Ah,隊u968Ah,檬u6AACh
:圂u5702h,豬u8C6Ch,逐u9010h,劇u5287h,豢u8C62h
:姬u59ECh,頤u9824h,熙u7199h,宧u5BA7h
:弬u5F2Ch,煕u7155h
:䑓u4453h,㒗u3497h
:里u91CCh,哩u54E9h,厘u5398h,量u91CFh,撞u649Eh,霾u973Eh,黒u9ED2h
:野u91CEh,墅u5885h,嘢u5622h,uE325h
:堇u5807h,僅u50C5h
:覲u89B2h,勤u52E4h,斳u65B3h,㢙u3899h
:uE987h
:貝u8C9Dh,員u54E1h,穎u7A4Eh,購u8CFCh,儐u5110h,嬰u5B30h,匱u5331h,圓u5713h
:見u898Bh,覓u8993h,現u73FEh,寬u5BECh,窺u7ABAh,攪u652Ah,襯u896Fh
:串u4E32h,患u60A3h,漶u6F36h,賗u8CD7h
:㰱u3C31h,挿u633Fh
:我u6211h,俄u4FC4h,義u7FA9h,儀u5100h,鵝u9D5Dh
#pg 34
:叟u53DFh,搜u641Ch,瘦u7626h,颼u98BCh
:學u5B78h,輿u8F3Fh,舉u8209h,興u8208h,攪u652Ah,嶼u5DBCh
:uF55Ah,盥u76E5h,夓u5913h
:身u8EABh,射u5C04h,謝u8B1Dh,窮u7AAEh,銵u92B5h
:鳥u9CE5h,鴨u9D28h,鴕u9D15h,鳳u9CF3h,鳶u9CF6h,鷹u9DF9h,裊u88CAh,搗u6417h
:釆u91C6h,釆u91C6h,宷u5BB7h
:悉u6089h,審u5BE9h,奧u5967h,釋u91CBh,竊u7ACAh,翻u7FFBh
:豸u8C78h,豹u8C79h,藐u85D0h,墾u58BEh
:言u8A00h,信u4FE1h,議u8B70h,擔u64D4h,罰u7F70h,辯u8FAFh
:慶u6176h,麓u9E93h,麋u9E8Bh,儷u5137h,麒u9E92h
:牽u727Dh,縴u7E34h,㯠u3BE0h,撁u6481h,鏲u93F2h
:菐u83D0h,幞u5E5Eh,樸u6A38h,璞u749Eh
:㡀u3840h,敝u655Dh,蔽u853Dh,撇u6487h,幣u5E63h
:兼u517Ch,嫌u5ACCh,鬑u9B11h,廉u5EC9h,簾u7C3Eh
:歉u6B49h,鶼u9DBCh,鼸u9F38h
:鼠u9F20h,竄u7AC4h,鼬u9F2Ch,獵u7375h
:鼎u9F0Eh,濎u6FCEh
#pg 35
:龍u9F8Dh,寵u5BF5h,嚨u56A8h,壟u58DFh
:戼u623Ch
:uE35Ch
:uE185h,uE516h
:華u83EFh,嘩u5629h,鷨u9DE8h
:夀u5900h
:長u9577h,帳u5E33h,漲u6F32h,萇u8407h
:亞u4E9Eh,啞u555Eh,惡u60E1h,壼u58FCh,氬u6C2Ch,uF526h
:惠u60E0h,蕙u8559h,傳u50B3h,囀u56C0h,團u5718h
:東u6771h,棟u68DFh,菄u83C4h,螴u87B4h,氭u6C2Dh
:鶇u9D87h,㯥u3BE5h,㼯u3F2Fh,䰤u4C24h
:事u4E8Bh,倳u5033h,剚u525Ah,䭄u4B44h
:雨u96E8h,漏u6F0Fh,瘺u763Ah,屚u5C5Ah,uE4B4h,uE4B3h
:憂u6182h,優u512Ah,擾u64FEh,鄾u913Eh
:豖u8C56h,冢u51A2h,塚u585Ah,啄u5544h,瘃u7603h
:剢u5262h,uEB34h
:雪u96EAh,霧u9727h,蕾u857Eh,儒u5112h
#pg 36
:疌u758Ch,捷u6377h,睫u776Bh,寁u5BC1h,萐u8410h
:韭u97EDh,懺u61FAh,籤u7C64h,虀u8640h,翡u7FE1h
:棄u68C4h,uF4C9h
:果u679Ch,彙u5F59h,棵u68F5h,窠u7AA0h,巢u5DE2h
:夥u5925h,顆u9846h,裹u88F9h,剿u527Fh
:婁u5A41h,樓u6A13h,簍u7C0Dh,屢u5C62h,數u6578h,擻u64FBh
:門u9580h,開u958Bh,簡u7C21h,們u5011h,躪u8EAAh
:丳u4E33h
:非u975Eh,匪u532Ah,排u6392h,罪u7F6Ah,霏u970Fh,靡u9761h
:秉u79C9h,棅u68C5h,uEB90h
:臾u81FEh,庾u5EBEh,萸u8438h,諛u8ADBh
:斞u659Eh,惥u60E5h
:淵u6DF5h,鏽u93FDh,瀟u701Fh,簫u7C2Bh
:金u91D1h,鑒u9452h,淦u6DE6h,菳u83F3h,鑫u946Bh
:釒u91D2h,針u91DDh,劉u5289h,銜u929Ch,鍛u935Bh
:飠u98E0h,飾u98FEh,飯u98EFh,饞u995Eh,飲u98F2h
:戠u6220h,識u8B58h,織u7E54h,uE64Eh
#pg 37
:壷u58F7h
:庸u5EB8h,傭u50ADh,鄘u9118h,鷛u9DDBh
:承u627Fh
:㢘u3898h
:uF565h
:揷u63F7h
:柬u67ECh,揀u63C0h,練u7DF4h,萰u8430h
:闌u95CCh,蘭u862Dh,欄u6B04h,爛u721Bh
:鬥u9B25h,鬨u9B28h,鬧u9B27h
:革u9769h,鞋u978Bh,韆u97C6h,鞏u978Fh,霸u9738h,緙u7DD9h
:亀u4E80h,縄u7E04h,竃u7AC3h,穐u7A50h
:禺u79BAh,愚u611Ah,寓u5BD3h,偶u5076h,勵u52F5h,邁u9081h,癘u7658h
:垂u5782h,唾u553Eh,菙u83D9h,厜u539Ch
:甀u7500h,郵u90F5h,㩾u3A7Eh,䳠u4CE0h
:乗u4E57h
:重u91CDh,董u8463h,種u7A2Eh,懂u61C2h,尰u5C30h,籦u7C66h
:動u52D5h,衝u885Dh,慟u615Fh,憅u6185h
#pg 38
:禹u79B9h,齲u9F72h,鄅u9105h,萭u842Dh
:食u98DFh,飧u98E7h,餐u9910h,饜u995Ch,養u990Ah,癢u7662h
:為u70BAh,偽u507Dh,鄬u912Ch,蘤u8624h,寪u5BEAh
:壺u58FAh,㯛u3BDBh
:飛u98DBh,騛u9A1Bh
:㵮u3D6Eh
:剰u5270h
:埀u57C0h
:羲u7FB2h,犧u72A7h,曦u66E6h,爔u7214h,uE97Ah,㰕u3C15h,䂀u4080h
:鬼u9B3Ch,蒐u8490h,塊u584Ah,魅u9B45h,巍u5DCDh,魘u9B58h
:鬬u9B2Ch
:斲u65B2h
:鬭u9B2Dh
:漢u6F22h,歎u6B4Eh,攤u6524h,癱u7671h
:畢u7562h,嗶u55F6h,篳u7BF3h,鷝u9DDDh
:蕐u8550h
:黑u9ED1h,嘿u563Fh,默u9ED8h,墨u58A8h,黛u9EDBh,黨u9EE8h
#pg 39
:爲u7232h,僞u50DEh,潙u6F59h,爳u7233h
:黽u9EFDh,繩u7E69h,鼈u9F08h,鄳u9133h
:uE2E7h,㲊u3C8Ah,䜜u471Ch
:熏u718Fh,薰u85B0h,燻u71FBh,勳u52F3h
:蠿u883Fh,躖u8E96h
:龜uF907h
:龜u9F9Ch,鬮u9B2Eh





#r
CJK_Radicals_Supplement = '
    ⺀⺁
    r⺂
    r⺃
    r⺄
    ⺅⺆⺇⺈⺉⺊⺋
    ⺌⺍⺎⺏⺐⺑⺒⺓⺔⺕
    ⺖⺗
    ⺘⺙⺛⺜⺝⺞⺟⺠
    ⺡⺢⺣⺤⺥⺦⺧⺨⺩
    ⺪⺫⺬⺭⺮⺯⺰⺱⺲⺳⺴⺵
    ⺶⺷⺸⺹⺺⺻⺼⺽⺾⺿⻀
    ⻁⻂⻃⻄⻅⻆⻇⻈⻉⻊⻋
    ⻌⻍⻎⻏⻐⻑⻒⻓⻔⻕⻖
    ⻗⻘⻙⻚⻛⻜⻝⻞⻟⻠⻡⻢
    ⻣⻤⻥⻦⻧⻨⻩⻪⻫⻬⻭⻮⻯⻰⻱⻲⻳'
#CJK_Radicals_Supplement





Kangxi_Radicals = '
    k⼀
    k⼁
    k⼂
    k⼃
    k⼄
    k⼅
    k2
    k⼆
#k
    ⼇⼈⼉⼊⼋⼌⼍⼎⼏⼐⼑⼒⼓
    k⼔
    ⼕⼖
    k⼗
    ⼘⼙
    k⼚
    ⼛⼜
    k3
    ⼝⼞⼟⼠⼡⼢⼣⼤⼥⼦⼧⼨⼩⼪⼫⼬⼭⼮⼯⼰⼱⼲⼳⼴⼵⼶⼷⼸⼹⼺⼻
    k4
    ⼼⼽⼾⼿⽀⽁⽂⽃⽄⽅⽆⽇⽈⽉⽊⽋⽌⽍⽎⽏⽐⽑⽒⽓⽔⽕⽖⽗⽘⽙⽚⽛⽜⽝
    k5
    ⽞⽟⽠⽡⽢⽣⽤⽥⽦⽧⽨⽩⽪⽫⽬⽭⽮⽯⽰⽱⽲⽳⽴
    k6
    ⽵⽶⽷⽸⽹⽺⽻⽼⽽⽾⽿⾀⾁⾂⾃⾄⾅⾆⾇⾈⾉⾊⾋⾌⾍⾎⾏⾐⾑
    k7
    ⾒⾓⾔⾕⾖⾗⾘⾙⾚⾛⾜⾝⾞⾟⾠⾡⾢⾣⾤⾥
    k8
    ⾦⾧⾨⾩⾪⾫⾬⾭⾮
    k9
    ⾯⾰⾱⾲⾳⾴⾵⾶⾷⾸⾹⾺⾻⾼⾽⾾⾿⿀⿁⿂⿃⿄⿅⿆⿇⿈⿉⿊⿋⿌⿍⿎⿏⿐⿑⿒⿓⿔⿕'
#Kangxi_Radicals





CJK_Strokes = '
    b㇀
    ㇁㇂
    ㇃
    b㇄
    ㇅
    b㇆
    b㇇
    b㇈
    b㇉
    ㇊㇋㇌㇍㇎
    b㇏
    b㇐
    b㇑
    b㇒
    b㇓
    b㇔
    b㇕
    b㇖
    b㇗
    ㇘
    b㇙
    b㇚
    b㇛
    b㇜
    b㇝
    b㇞
    b㇟
    b㇠
    ㇡㇢㇣'
b
5:>
    h,(乙u4E59h//横折弯钩【乙】)
    h,(//横折) ~ 横撇
    h,(𠃍u200CDh//) ~ 横竖
    h,(//横折钩),(𠃌u200CCh//) ~ 横竖钩
    h,(//竖折),(𠃊u200CAh//)
    h,(//竖弯钩),(乚u4E5Ah//)
    ,(uE818h//)
    ,(uE819h//)
    h,(𠃋u200CBh//)
    h,(𠃑u200D1h//)
    h,(𠄌u2010Ch//)
    ,(𠄎u2010Eh//)
    h,(𡿨u21FE8h//)


#"""
#香港電腦漢字楷體字形基礎部件表

