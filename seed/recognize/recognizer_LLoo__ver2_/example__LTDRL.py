#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/example__LTDRL.py

seed.recognize.recognizer_LLoo__ver2_.example__LTDRL
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo__ver2_.example__LTDRL -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo__ver2_.example__LTDRL:__doc__ -ht

[[
selected-copy from:
    view others/数学/编程/设计/语法升级序列.txt
==:
framework of labelled tree data representation language
framework of LTDRL
框架冫带标签树状结构数据类型表达用语言
  LTDRL_I_S6
  LTDRL_I_M8
  LTDRL_II_S8
  LTDRL_II_M16
  LTDRL_II_M41
  LTDRL_II_M64
  LTDRL_II_M85
  LTDRL_II_Muge
===
===
语法牜初版:
###母符:
## 凡 非内敛耂母符 之命名 以『灬』领起 尾前瞻符集
## 凡 母符 之命名 以『冖』领起 头符集
## 凡 允空耂母符 之命名 以『凵』结尾

节点冖起 = 起符 裸节点灬起数冖逗冒 讫符
裸节点灬起数冖逗冒 = 裸叉节点灬起数冖冒 | 裸叶节点灬数冖逗

裸叶节点灬数冖逗 = 逗号 标签灬名冖名凵 体纟裸叶节点灬数冖冒
体纟裸叶节点灬数冖冒 = 冒号 数据灬数冖数凵

裸叉节点灬起数冖冒 = 冒号 标签灬名冖名凵 体纟裸叉节点灬起数冖起逗冒
体纟裸叉节点灬起数冖起逗冒 = 体纟裸标准叉节点灬起冖冒 | 体纟裸孤子叉节点灬起数冖逗 | 体纟裸复叶叉节点冖起

体纟裸标准叉节点灬起冖冒 = 冒号 节点冖起*
体纟裸孤子叉节点灬起数冖逗 = 逗号 裸节点灬起数冖逗冒
体纟裸复叶叉节点冖起 = 起符 体纟裸叶节点灬数冖冒* 讫符

标签灬名冖名凵 = 名符*
数据灬数冖数凵 = 数符*

###种符:
起符
讫符
逗号
冒号
名符
数符

===
[len{起符,逗号,冒号,名符} == 4][讫符 !<- {起符,数符}][冒号=!=数符]

==>>:
*实例{字集[0-9]:单字符料符:六进制:senary:LTDRL_I_S6}
起符#6
讫符#9
逗号#7
冒号#8
名符#[0-5]
数符#[0-5]

==>>:
*实例{字集[0-9]:多字符料符:八进制:octonary:LTDRL_I_M8}
起符#86
讫符#89
逗号#87
冒号#88
名符#[0-7]
数符#[0-7]



===
===
语法牜二版:区分不同类型的起讫符
###母符:
节点 =:
  | 起符纟叶 裸裸叶节点     讫符纟叶
  | 起符纟桠 裸裸标准叉节点 讫符纟桠
  | 起符纟链 裸裸孤子叉节点 讫符纟链
  | 起符纟拳 裸裸复叶叉节点 讫符纟拳
  | 起符纟注 裸裸孤子叉节点 讫符纟注

裸裸叶节点     = 名符* 冒号 数符*
裸裸标准叉节点 = 名符* 冒号 节点*
裸裸孤子叉节点 = 名符* 冒号 半裸节点
裸裸复叶叉节点 = 名符* 冒号 (数符* (逗号 数符*)*)?
  <==> 裸裸复叶叉节点 = 名符* 冒号 (数符|逗号)*

半裸节点 =:
  | 型符纟叶 裸裸叶节点
  | 型符纟桠 裸裸标准叉节点
  | 型符纟链 裸裸孤子叉节点
  | 型符纟拳 裸裸复叶叉节点
  | 型符纟注 裸裸孤子叉节点

###种符:
起符纟叶
起符纟桠
起符纟链
起符纟拳
起符纟注

讫符纟叶
讫符纟桠
讫符纟链
讫符纟拳
讫符纟注

型符纟叶
型符纟桠
型符纟链
型符纟拳
型符纟注

冒号
逗号
名符
数符



===
[len{起符纟叶,起符纟桠,起符纟链,起符纟拳,起符纟注} == 5]
[len{型符纟叶,型符纟桠,型符纟链,型符纟拳,型符纟注} == 5]
[冒号 =!= 名符]
[逗号 =!= 数符]
[讫符纟叶 !<- {数符}]
[讫符纟桠 !<- {起符纟叶,起符纟桠,起符纟链,起符纟拳,起符纟注}]
[讫符纟拳 !<- {数符,逗号}]
[讫符纟链 !<- {数符,逗号,起符纟叶,起符纟桠,起符纟链,起符纟拳,起符纟注}]
[讫符纟注 !<- {数符,逗号,起符纟叶,起符纟桠,起符纟链,起符纟拳,起符纟注}]


===
可行配置牜甲:
[讫符 := 讫符纟叶==讫符纟桠==讫符纟链==讫符纟拳==讫符纟注 !<- {型符纟叶,型符纟桠,型符纟链,型符纟拳,型符纟注}]
[len{型符纟叶,型符纟桠,型符纟链,型符纟拳,型符纟注} == 5]
[起符纟叶==型符纟叶]
[起符纟桠==型符纟桠]
[起符纟链==型符纟链]
[起符纟拳==型符纟拳]
[起符纟注==型符纟注]
[len{讫符,数符,逗号} == 3]
[名符 =!= 冒号]

===
可行配置牜乙<:可行配置牜甲:
[冒号==讫符]
[名符==(数符|逗号)]
  # 名符串 可视为 数符串串 即 数组{自然数}

===
可行配置牜丙:
[讫符 := 讫符纟叶==讫符纟桠==讫符纟链==讫符纟拳==讫符纟注 =!= 起符]
[len{型符纟叶,型符纟桠,型符纟链,型符纟拳,型符纟注} == 5]
[起符纟叶==起符+型符纟叶]
[起符纟桠==起符+型符纟桠]
[起符纟链==起符+型符纟链]
[起符纟拳==起符+型符纟拳]
[起符纟注==起符+型符纟注]
[len{讫符,数符,逗号} == 3]
[名符 =!= 冒号]

===
可行配置牜丁<:可行配置牜丙:
[名符==(数符|逗号)]
  # 名符串 可视为 数符串串 即 数组{自然数}




==>>:
*实例{可行配置牜乙:单字符料符:字集[0-9]:八进制:octonary:LTDRL_II_S8}:
讫符#9
  冒号#9
  讫符纟叶#9
  讫符纟桠#9
  讫符纟链#9
  讫符纟拳#9
  讫符纟注#9

型符纟叶#0
型符纟桠#3
型符纟链#1
型符纟拳#2
型符纟注#4

  起符纟叶#0
  起符纟桠#3
  起符纟链#1
  起符纟拳#2
  起符纟注#4

逗号#8
数符#[0-7]
  名符#[0-8]


==>>:
*实例{可行配置牜丁:多字符料符:字集ascii:base16/base41/base64__urlsafe/base85/unicode_graph_escaped:hexadecimal/?/?/?:LTDRL_II_M16/LTDRL_II_M41/LTDRL_II_M64/LTDRL_II_M85/LTDRL_II_Muge}:
起符 # [
讫符 # ]

型符纟叶# .
型符纟桠# *
型符纟链# /
型符纟拳# %
型符纟注# -

起符纟叶# [.
起符纟桠# [*
起符纟链# [/
起符纟拳# [%
起符纟注# [-

讫符纟叶# ]
讫符纟桠# ]
讫符纟链# ]
讫符纟拳# ]
讫符纟注# ]

冒号# :
逗号# ,
*base16:
  名符# [,0-9A-F]
  数符# [0-9A-F]
*base41:
  名符# [,0-9A-Za-e]
  数符# [0-9A-Za-e]
*base64__urlsafe:
  名符# [,A-Za-z0-9\-_]
  数符# [A-Za-z0-9\-_]
  #不需要『=』填充:类似base85弹性伸缩
  #     [base16:len%2=!=1]
  #     [base41:len%3=!=1]
  #     [base64:len%4=!=1]
  #     [base85:len%5=!=1]
  #     [16**2 == 256**1]
  #     [41**3 / 256**2 ~= 1.0516510009765625]
  #     [64**4 == 256**3]
  #     [85**5 / 256**4 ~= 1.0330819350201637]
*base85/b85_alphabet:
  !! [{} == 『,:[]』 /-\ b85_alphabet]
  名符# [,[:b85_alphabet:]]
  数符# [[:b85_alphabet:]]
*unicode_graph_escaped:
  名符# (,|(?![\\,:\[\]])[[:unicode_graph:]]|\\[.,:\[\]])
  数符# ((?![\\,:\[\]])[[:unicode_graph:]]|\\[.,:\[\]])
  let [[[:unicode_graph:]] := (\pL+\pN+\pP+\pS+\pM) = (\p{Graph}-\p{Co}-\p{Cf}) (148_997)]


<<==:
view ../../python3_src/seed/text/base64.py
  py::base64::字母表 次序:urlsafe:『A-Za-z0-9-_』:填充『=』

view ../../python3_src/seed/int_tools/digits/generic_base85.py
    b85_alphabet = (b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" b"abcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~")
    a85_alphabet = bytes(range(ord(' ')+1, ord('v')))
    assert remain_graph_chars_(b85_alphabet) == '"\',./:[\\]' == r""" " ' , . / : [ \ ] """[1::2] == '\x22\x27\x2c\x2e\x2f\x3a\x5b\x5c\x5d'
    assert remain_graph_chars_(a85_alphabet) == 'vwxyz{|}~'

view ../lots/NOTE/unicode/char_class/word-vs-graphical.txt
  \p{Graph}===\p{XPosixGraph} (286_635) === \pL+\pN+\pP+\pS+\pM+\p{Co}+\p{Cf}
    (\p{Graph}-\p{Co}-\p{Cf}) (148_997)
        148_997 == (286_635) - (137_468) - (170)

===
===
]]


py_adhoc_call   seed.recognize.recognizer_LLoo__ver2_.example__LTDRL   @f
from seed.recognize.recognizer_LLoo__ver2_.example__LTDRL import *
#]]]'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
___end_mark_of_excluded_global_names__0___ = ...



__all__
from seed.recognize.recognizer_LLoo__ver2_.example__LTDRL import *
