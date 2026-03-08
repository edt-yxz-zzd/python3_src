#__all__:goto
r'''[[[
e ../../python3_src/seed/int_tools/int_repr7compact7lex_order7baseGL.py
view ../../python3_src/seed/int_tools/int_repr7human7lex_order7alnum.py
mv -iv ../../python3_src/seed/int_tools/int_repr7compact7baseGA7lex_order.py ../../python3_src/seed/int_tools/int_repr7compact7lex_order7baseGL.py


view ../../python3_src/nn_ns/app/int_repr7human.py
view ../../python3_src/nn_ns/app/int_repr7compact.py
view ../../python3_src/nn_ns/app/fraction_repr7compact.py

view ../../python3_src/bash_script/app/int_repr7human
view ../../python3_src/bash_script/app/int_repr7compact
view ../../python3_src/bash_script/app/fraction_repr7compact


seed.int_tools.int_repr7compact7lex_order7baseGL
py -m nn_ns.app.debug_cmd   seed.int_tools.int_repr7compact7lex_order7baseGL -x # -off_defs
py -m nn_ns.app.doctest_cmd seed.int_tools.int_repr7compact7lex_order7baseGL:__doc__ -ht # -ff -df
#######

[[
[baseGL == base67]
[baseGA == base64]
[字母表 == regex'[-.0-9=@A-Z_a-z]']
[字母表牜头胞 == regex'[-=@]']
    3
    -0+
    或者:
    [字母表牜头胞 == regex'[!-=@^]']
        5
        -oo - 0 + +oo
[字母表牜体胞 == regex'[.0-9A-Z_a-z]']
    [64 == 1+10+26+1+26]
    6爻元

考虑体胞表达自然数:
    + 16 ++0体胞 => 4爻元
    + 16 ++1体胞 => 10爻元
    + 16 ++2体胞 => 16爻元
    + 8  ++3体胞 => 21爻元
    + 1  ++4体胞 => 24爻元
    + 1  ++5体胞 => 30爻元
    + 1  ++6体胞 => 36爻元
    + 1  ++7体胞 => 42爻元
    + 1  ++8体胞 => 48爻元
    + 1  ++?体胞 => 61:深入
    + 1  ++0体胞 => 62:+oo
    + 1  ++?体胞 => 63:保留

    61:深入:
    61: +16 ++9体胞 => 58爻元
    61: +16 ++10体胞 => 64爻元
    61: +1*16 ++11..26体胞 => 66..156爻元
    61: +1*8 ++1..8体胞 ++..(-1+2**48)体胞 => ..6*(-1+2**48)爻元
    61: +1*4 ++1..4体胞 ++..(-1+2**24)体胞 ++..(-1+2**(6*(-1+2**24)))体胞 => ..6*(-1+2**(6*(-1+2**24)))爻元
    61: +4:待定义to_be_continued


e ../../python3_src/seed/int_tools/int_repr7lex_order7base.py
(分区表纟丮前导节辻循环节厈/[分区表纟单胞/[(规模纟占位, 体胞数纟首层, 增量纟总层数)]], 配置纟深入/(后手处理器|长度纟尾循环))
    [起始总层数:=0]

]]

[[
[0123456789]
[OIZEASGLBP]...既非升序亦非降序
口丨/亅/工乙彐亼/又与囟乁/勹吕/日巳/尸
壹贰叁肆伍陆柒捌玖拾念佰仟
一二三四五六七八九十廿百千

>>> sorted('0aA._+-@=')
['+', '-', '.', '0', '=', '@', 'A', '_', 'a']
>>> sorted('0aA._!-@=^')
['!', '-', '.', '0', '=', '@', 'A', '^', '_', 'a']

>>> import urllib.parse
>>> urllib.parse.quote_plus(' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~') # -._~
'+%21%22%23%24%25%26%27%28%29%2A%2B%2C-.%2F0123456789%3A%3B%3C%3D%3E%3F%40ABCDEFGHIJKLMNOPQRSTUVWXYZ%5B%5C%5D%5E_%60abcdefghijklmnopqrstuvwxyz%7B%7C%7D~'


view ../../python3_src/seed/text/mk_char_pt_ranges5predicator.py
assert printable_ascii_sorted_chars == ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

>>> bytes([61])
b'='
>>> bytes([63,64,65,66])
b'?@AB'

]]


'#'; __doc__ = r'#'
>>> 6*(-1+2**48)
1688849860263930
>>> 2**4
16
>>> 2**10
1024
>>> 2**16
65536
>>> 2**21
2097152
>>> 2**24
16777216
>>> 2**30
1073741824
>>> 2**36
68719476736
>>> 2**42
4398046511104
>>> 2**48
281474976710656
>>> 2**58
288230376151711744
>>> 2**64
18446744073709551616

>>> 6*11
66
>>> 6*26
156
>>> 2**66
73786976294838206464
>>> 2**72
4722366482869645213696
>>> 2**150
1427247692705959881058285969449495136382746624
>>> 2**156
91343852333181432387730302044767688728495783936
>>> 2**162
5846006549323611672814739330865132078623730171904

>>> 6*63
378
>>> 2**378
615656346818663737691860001564743965704370926101022604186692084441339402679643915803347910232576806887603562348544

>>> 6*(-1+2**12)
24570
>>> 2**24570
Traceback (most recent call last):
    ...
ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit


>>> +oo
(+oo)
>>> -oo
(-oo)



>>> _匴自然数位元串表达牜基表六四.表述冫数据讠位元串表达扌(0, 欤校验=False)
b'\x00'
>>> _匴自然数位元串表达牜基表六四.表述冫数据讠位元串表达扌(1, 欤校验=False)
b'\x01'
>>> _匴自然数位元串表达牜基表六四.解读冫数据巛位元串表达扌(b'\0', 欤校验=False)
0
>>> _匴自然数位元串表达牜基表六四.解读冫数据巛位元串表达扌(b'\1', 欤校验=False)
1

>>> _匴整数位元串表达牜基表六七.表述冫数据讠位元串表达扌(0, 欤校验=False)
b'A'
>>> _匴整数位元串表达牜基表六七.表述冫数据讠位元串表达扌(1, 欤校验=False)
b'B\x01'
>>> _匴整数位元串表达牜基表六七.解读冫数据巛位元串表达扌(b'A', 欤校验=False)
0
>>> _匴整数位元串表达牜基表六七.解读冫数据巛位元串表达扌(b'B\1', 欤校验=False)
1



>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(0)
'='
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(1)
'@0'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(15)
'@E'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(16)
'@FF'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(1023)
'@Uz'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(1024)
'@VF.'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(65535)
'@jzz'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(65536)
'@kF..'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(2097151)
'@rzzz'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(2097152)
'@s7...'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(16777215)
'@szzzz'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(16777216)
'@t0....'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(1073741823)
'@tzzzzz'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(1073741824)
'@u0.....'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(68719476735)
'@uzzzzzz'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(68719476736)
'@v0......'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(4398046511103)
'@vzzzzzzz'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(4398046511104)
'@w0.......'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(281474976710655)
'@wzzzzzzzz'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(281474976710656)
'@x.0........'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(288230376151711743)
'@xEzzzzzzzzz'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(288230376151711744)
'@xFF.........'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(18446744073709551615)
'@xUzzzzzzzzzz'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(18446744073709551616)
'@xVF..........'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(18446744073709551617)
'@xVF.........0'



>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(73786976294838206463)
'@xVzzzzzzzzzzz'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(73786976294838206464)
'@xW0...........'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(4722366482869645213695)
'@xWzzzzzzzzzzzz'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(4722366482869645213696)
'@xX0............'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(1427247692705959881058285969449495136382746623)
'@xizzzzzzzzzzzzzzzzzzzzzzzzz'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(1427247692705959881058285969449495136382746624)
'@xj0.........................'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(91343852333181432387730302044767688728495783935)
'@xjzzzzzzzzzzzzzzzzzzzzzzzzzz'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(91343852333181432387730302044767688728495783936)
'@xkQ0..........................'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(5846006549323611672814739330865132078623730171903)
'@xkQzzzzzzzzzzzzzzzzzzzzzzzzzzz'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(5846006549323611672814739330865132078623730171904)
'@xkR0...........................'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(615656346818663737691860001564743965704370926101022604186692084441339402679643915803347910232576806887603562348543)
'@xkzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(615656346818663737691860001564743965704370926101022604186692084441339402679643915803347910232576806887603562348544)
'@xl0.0...............................................................'



>>> a = 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(-1+2**24570)
>>> b = 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(2**24570)
>>> len(a)
4100
>>> len(b)
4102
>>> a.startswith('@xlzzzzzz')
True
>>> b.startswith('@xm0..0......')
True
>>> a == '@xl' + 'z'*(4100-3)
True
>>> b == '@xm0..0' + '.'*(4102-7)
True


>>> 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(+oo)
'@y'

grep '表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌([0-9]\+)' ../../python3_src/seed/int_tools/int_repr7compact7lex_order7baseGL.py -o | grep '[0-9]\+' -o

>>> us = (
... [1
... ,15
... ,16
... ,1023
... ,1024
... ,65535
... ,65536
... ,2097151
... ,2097152
... ,16777215
... ,16777216
... ,1073741823
... ,1073741824
... ,68719476735
... ,68719476736
... ,4398046511103
... ,4398046511104
... ,281474976710655
... ,281474976710656
... ,288230376151711743
... ,288230376151711744
... ,18446744073709551615
... ,18446744073709551616
... ,18446744073709551617
... ,73786976294838206463
... ,73786976294838206464
... ,4722366482869645213695
... ,4722366482869645213696
... ,1427247692705959881058285969449495136382746623
... ,1427247692705959881058285969449495136382746624
... ,91343852333181432387730302044767688728495783935
... ,91343852333181432387730302044767688728495783936
... ,5846006549323611672814739330865132078623730171903
... ,5846006549323611672814739330865132078623730171904
... ,615656346818663737691860001564743965704370926101022604186692084441339402679643915803347910232576806887603562348543
... ,615656346818663737691860001564743965704370926101022604186692084441339402679643915803347910232576806887603562348544
... ,+oo
... ])

>>> ns = [-u for u in reversed(us)]
>>> ints = [*ns, 0, *us]
>>> len(ints) == len(set(ints))
True
>>> ints == sorted(ints)
True
>>> ss = [*map(表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌, ints)]
>>> len(ss) == len(set(ss))
True
>>> ss == sorted(ss)
True
>>> _ints = [*map(解读冫整数巛文本表达牜紧凑牜词典序牜基表六七扌, ss)]
>>> _ints == ints
True
>>> for s, i in zip(ss, ints):
...     print(s, i, sep=':')
-0:(-oo)
-1Dyzyzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz:-615656346818663737691860001564743965704370926101022604186692084441339402679643915803347910232576806887603562348544
-1E................................................................:-615656346818663737691860001564743965704370926101022604186692084441339402679643915803347910232576806887603562348543
-1EYyzzzzzzzzzzzzzzzzzzzzzzzzzzz:-5846006549323611672814739330865132078623730171904
-1EZ...........................:-5846006549323611672814739330865132078623730171903
-1EZyzzzzzzzzzzzzzzzzzzzzzzzzzz:-91343852333181432387730302044767688728495783936
-1F..........................:-91343852333181432387730302044767688728495783935
-1Fyzzzzzzzzzzzzzzzzzzzzzzzzz:-1427247692705959881058285969449495136382746624
-1G.........................:-1427247692705959881058285969449495136382746623
-1Syzzzzzzzzzzzz:-4722366482869645213696
-1T............:-4722366482869645213695
-1Tyzzzzzzzzzzz:-73786976294838206464
-1U...........:-73786976294838206463
-1Ujzzzzzzzzzy:-18446744073709551617
-1Ujzzzzzzzzzz:-18446744073709551616
-1V..........:-18446744073709551615
-1jjzzzzzzzzz:-288230376151711744
-1k.........:-288230376151711743
-1zyzzzzzzzz:-281474976710656
-2........:-281474976710655
-2yzzzzzzz:-4398046511104
-3.......:-4398046511103
-3yzzzzzz:-68719476736
-4......:-68719476735
-4yzzzzz:-1073741824
-5.....:-1073741823
-5yzzzz:-16777216
-6....:-16777215
-6rzzz:-2097152
-7...:-2097151
-Ejzz:-65536
-F..:-65535
-Ujz:-1024
-V.:-1023
-jj:-16
-k:-15
-y:-1
=:0
@0:1
@E:15
@FF:16
@Uz:1023
@VF.:1024
@jzz:65535
@kF..:65536
@rzzz:2097151
@s7...:2097152
@szzzz:16777215
@t0....:16777216
@tzzzzz:1073741823
@u0.....:1073741824
@uzzzzzz:68719476735
@v0......:68719476736
@vzzzzzzz:4398046511103
@w0.......:4398046511104
@wzzzzzzzz:281474976710655
@x.0........:281474976710656
@xEzzzzzzzzz:288230376151711743
@xFF.........:288230376151711744
@xUzzzzzzzzzz:18446744073709551615
@xVF..........:18446744073709551616
@xVF.........0:18446744073709551617
@xVzzzzzzzzzzz:73786976294838206463
@xW0...........:73786976294838206464
@xWzzzzzzzzzzzz:4722366482869645213695
@xX0............:4722366482869645213696
@xizzzzzzzzzzzzzzzzzzzzzzzzz:1427247692705959881058285969449495136382746623
@xj0.........................:1427247692705959881058285969449495136382746624
@xjzzzzzzzzzzzzzzzzzzzzzzzzzz:91343852333181432387730302044767688728495783935
@xkQ0..........................:91343852333181432387730302044767688728495783936
@xkQzzzzzzzzzzzzzzzzzzzzzzzzzzz:5846006549323611672814739330865132078623730171903
@xkR0...........................:5846006549323611672814739330865132078623730171904
@xkzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz:615656346818663737691860001564743965704370926101022604186692084441339402679643915803347910232576806887603562348543
@xl0.0...............................................................:615656346818663737691860001564743965704370926101022604186692084441339402679643915803347910232576806887603562348544
@y:(+oo)








>>> from fractions import Fraction
>>> 表述冫有理数讠文本表达牜紧凑牜词典序牜基表六七扌(0)
'='
>>> 表述冫有理数讠文本表达牜紧凑牜词典序牜基表六七扌(1)
'@1'
>>> 表述冫有理数讠文本表达牜紧凑牜词典序牜基表六七扌(2)
'@3'
>>> 表述冫有理数讠文本表达牜紧凑牜词典序牜基表六七扌(3)
'@5'
>>> 表述冫有理数讠文本表达牜紧凑牜词典序牜基表六七扌(666)
'@VJo'
>>> 表述冫有理数讠文本表达牜紧凑牜词典序牜基表六七扌(999)
'@VUD'
>>> 表述冫有理数讠文本表达牜紧凑牜词典序牜基表六七扌(Fraction(1/2))
'@0yy'
>>> 表述冫有理数讠文本表达牜紧凑牜词典序牜基表六七扌(Fraction(1/3))
'@0xx.KKKKKKKKJ0'
>>> 表述冫有理数讠文本表达牜紧凑牜词典序牜基表六七扌(Fraction(1/4))
'@0wy'
>>> 表述冫有理数讠文本表达牜紧凑牜词典序牜基表六七扌(Fraction(3/2))
'@2yy'
>>> 表述冫有理数讠文本表达牜紧凑牜词典序牜基表六七扌(Fraction(5/2))
'@4yy'
>>> 表述冫有理数讠文本表达牜紧凑牜词典序牜基表六七扌(Fraction(5/3))
'@2z01zueeeeeeefy'
>>> 表述冫有理数讠文本表达牜紧凑牜词典序牜基表六七扌(Fraction(5/4))
'@2wy'
>>> 表述冫有理数讠文本表达牜紧凑牜词典序牜基表六七扌(Fraction(377/233))
'@2z.z.z.z.z.z.3uyY47z650'
>>> 表述冫有理数讠文本表达牜紧凑牜词典序牜基表六七扌(Fraction(144/233))
'@0z.z.z.z.z.z.3uyY47z650'

>>> 解读冫有理数巛文本表达牜紧凑牜词典序牜基表六七扌('=')
Fraction(0, 1)





grep '^>>> 表述冫有理数讠文本表达牜紧凑牜词典序牜基表六七扌(.*)$' ../../python3_src/seed/int_tools/int_repr7compact7lex_order7baseGL.py -o | grep '(.*)$' -o
.+1,.+16s/(\(.*\))/\1
>>> ps = (
... (1
... ,2
... ,3
... ,666
... ,999
... ,Fraction(1/3)
... ,Fraction(5/3)
... ,Fraction(377/233)
... ,Fraction(144/233)
... ,Fraction(1,3)
... ,Fraction(1,4)
... ,Fraction(3,2)
... ,Fraction(5,2)
... ,Fraction(5,3)
... ,Fraction(5,4)
... ,Fraction(1,2)
... ,Fraction(2,3)
... ,Fraction(3,5)
... ,Fraction(5,8)
... ,Fraction(8,13)
... ,Fraction(13,21)
... ,Fraction(21,34)
... ,Fraction(34,55)
... ,Fraction(55,89)
... ,Fraction(89,144)
... ,Fraction(144,233)
... ,Fraction(233,377)
... ,Fraction(377,233)
... ,+oo
... ))

>>> ns = [-p for p in reversed(ps)]
>>> frs = [*ns, 0, *ps]
>>> len(frs) == len(set(frs))
True
>>> frs = sorted(frs)
>>> ss = [*map(表述冫有理数讠文本表达牜紧凑牜词典序牜基表六七扌, frs)]
>>> len(ss) == len(set(ss))
True
>>> ss == sorted(ss)
True
>>> _frs = [*map(解读冫有理数巛文本表达牜紧凑牜词典序牜基表六七扌, ss)]
>>> _frs == frs
True
>>> for s, i in zip(ss, frs):
...     print(s, i, sep=':')
-0:(-oo)
-UVl:-999
-UfA:-666
-t:-3
-u00:-5/2
-v:-2
-w.yx.4KKKKKKKJ0:-7505999378950827/4503599627370496
-w.yy:-5/3
-w.z.z.z.z.z.zv40Rur.sty:-910867521201007/562949953421312
-w.z.z.z.z.z00:-377/233
-w00:-3/2
-w20:-5/4
-x:-1
-y.yy:-2/3
-y.z.yy:-5/8
-y.z.z.yy:-13/21
-y.z.z.z.yy:-34/55
-y.z.z.z.z.yy:-89/144
-y.z.z.z.z.z.yy:-233/377
-y.z.z.z.z.z.zv40Rur.sty:-347917567779695/562949953421312
-y.z.z.z.z.z00:-144/233
-y.z.z.z.z00:-55/89
-y.z.z.z00:-21/34
-y.z.z00:-8/13
-y.z00:-3/5
-y00:-1/2
-y10:-1/3
-y11zeeeeeeeefy:-6004799503160661/18014398509481984
-y20:-1/4
=:0
@0wy:1/4
@0xx.KKKKKKKKJ0:6004799503160661/18014398509481984
@0xy:1/3
@0yy:1/2
@0z.yy:3/5
@0z.z.yy:8/13
@0z.z.z.yy:21/34
@0z.z.z.z.yy:55/89
@0z.z.z.z.z.yy:144/233
@0z.z.z.z.z.z.3uyY47z650:347917567779695/562949953421312
@0z.z.z.z.z.z00:233/377
@0z.z.z.z.z00:89/144
@0z.z.z.z00:34/55
@0z.z.z00:13/21
@0z.z00:5/8
@0z00:2/3
@1:1
@2wy:5/4
@2yy:3/2
@2z.z.z.z.z.yy:377/233
@2z.z.z.z.z.z.3uyY47z650:910867521201007/562949953421312
@2z00:5/3
@2z01zueeeeeeefy:7505999378950827/4503599627370496
@3:2
@4yy:5/2
@5:3
@VJo:666
@VUD:999
@y:(+oo)















>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(0)
'.'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(1)
'0'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(15)
'E'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(16)
'FF'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(1023)
'Uz'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(1024)
'VF.'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(65535)
'jzz'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(65536)
'kF..'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(2097151)
'rzzz'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(2097152)
's7...'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(16777215)
'szzzz'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(16777216)
't0....'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(1073741823)
'tzzzzz'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(1073741824)
'u0.....'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(68719476735)
'uzzzzzz'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(68719476736)
'v0......'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(4398046511103)
'vzzzzzzz'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(4398046511104)
'w0.......'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(281474976710655)
'wzzzzzzzz'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(281474976710656)
'x.0........'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(288230376151711743)
'xEzzzzzzzzz'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(288230376151711744)
'xFF.........'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(18446744073709551615)
'xUzzzzzzzzzz'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(18446744073709551616)
'xVF..........'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(18446744073709551617)
'xVF.........0'



>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(73786976294838206463)
'xVzzzzzzzzzzz'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(73786976294838206464)
'xW0...........'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(4722366482869645213695)
'xWzzzzzzzzzzzz'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(4722366482869645213696)
'xX0............'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(1427247692705959881058285969449495136382746623)
'xizzzzzzzzzzzzzzzzzzzzzzzzz'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(1427247692705959881058285969449495136382746624)
'xj0.........................'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(91343852333181432387730302044767688728495783935)
'xjzzzzzzzzzzzzzzzzzzzzzzzzzz'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(91343852333181432387730302044767688728495783936)
'xkQ0..........................'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(5846006549323611672814739330865132078623730171903)
'xkQzzzzzzzzzzzzzzzzzzzzzzzzzzz'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(5846006549323611672814739330865132078623730171904)
'xkR0...........................'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(615656346818663737691860001564743965704370926101022604186692084441339402679643915803347910232576806887603562348543)
'xkzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(615656346818663737691860001564743965704370926101022604186692084441339402679643915803347910232576806887603562348544)
'xl0.0...............................................................'



>>> a = 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(-1+2**24570)
>>> b = 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(2**24570)
>>> len(a)
4099
>>> len(b)
4101
>>> a.startswith('xlzzzzzz')
True
>>> b.startswith('xm0..0......')
True
>>> a == 'xl' + 'z'*(4100-3)
True
>>> b == 'xm0..0' + '.'*(4102-7)
True


>>> 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(+oo)
'y'


>>> us = (
... [1
... ,15
... ,16
... ,1023
... ,1024
... ,65535
... ,65536
... ,2097151
... ,2097152
... ,16777215
... ,16777216
... ,1073741823
... ,1073741824
... ,68719476735
... ,68719476736
... ,4398046511103
... ,4398046511104
... ,281474976710655
... ,281474976710656
... ,288230376151711743
... ,288230376151711744
... ,18446744073709551615
... ,18446744073709551616
... ,18446744073709551617
... ,73786976294838206463
... ,73786976294838206464
... ,4722366482869645213695
... ,4722366482869645213696
... ,1427247692705959881058285969449495136382746623
... ,1427247692705959881058285969449495136382746624
... ,91343852333181432387730302044767688728495783935
... ,91343852333181432387730302044767688728495783936
... ,5846006549323611672814739330865132078623730171903
... ,5846006549323611672814739330865132078623730171904
... ,615656346818663737691860001564743965704370926101022604186692084441339402679643915803347910232576806887603562348543
... ,615656346818663737691860001564743965704370926101022604186692084441339402679643915803347910232576806887603562348544
... ,+oo
... ])

>>> uints = [0, *us]
>>> len(uints) == len(set(uints))
True
>>> uints == sorted(uints)
True
>>> ss = [*map(表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌, uints)]
>>> len(ss) == len(set(ss))
True
>>> ss == sorted(ss)
True
>>> _uints = [*map(解读冫自然数巛文本表达牜紧凑牜词典序牜基表六四扌, ss)]
>>> _uints == uints
True
>>> for s, i in zip(ss, uints):
...     print(s, i, sep=':')
.:0
0:1
E:15
FF:16
Uz:1023
VF.:1024
jzz:65535
kF..:65536
rzzz:2097151
s7...:2097152
szzzz:16777215
t0....:16777216
tzzzzz:1073741823
u0.....:1073741824
uzzzzzz:68719476735
v0......:68719476736
vzzzzzzz:4398046511103
w0.......:4398046511104
wzzzzzzzz:281474976710655
x.0........:281474976710656
xEzzzzzzzzz:288230376151711743
xFF.........:288230376151711744
xUzzzzzzzzzz:18446744073709551615
xVF..........:18446744073709551616
xVF.........0:18446744073709551617
xVzzzzzzzzzzz:73786976294838206463
xW0...........:73786976294838206464
xWzzzzzzzzzzzz:4722366482869645213695
xX0............:4722366482869645213696
xizzzzzzzzzzzzzzzzzzzzzzzzz:1427247692705959881058285969449495136382746623
xj0.........................:1427247692705959881058285969449495136382746624
xjzzzzzzzzzzzzzzzzzzzzzzzzzz:91343852333181432387730302044767688728495783935
xkQ0..........................:91343852333181432387730302044767688728495783936
xkQzzzzzzzzzzzzzzzzzzzzzzzzzzz:5846006549323611672814739330865132078623730171903
xkR0...........................:5846006549323611672814739330865132078623730171904
xkzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz:615656346818663737691860001564743965704370926101022604186692084441339402679643915803347910232576806887603562348543
xl0.0...............................................................:615656346818663737691860001564743965704370926101022604186692084441339402679643915803347910232576806887603562348544
y:(+oo)










[[
e ../../python3_src/bash_script/app/fraction_repr7compact
fraction_repr7compact encode -- 7777 +233/377
    @Yn1
    @0z.z.z.z.z.z00

]]
py -m nn_ns.app.fraction_repr7compact
[[
fraction_repr7compact encode -- 0 1 -1 999 -999 +11 -11 +7777 -7777  +144/233 -144/233 +233/377 -233/377
    =
    @1
    -x
    @VUD
    -UVl
    @FL
    -jd
    @Yn1
    -RBx
    @0z.z.z.z.z.yy
    -y.z.z.z.z.z00
    @0z.z.z.z.z.z00
    -y.z.z.z.z.z.yy


fraction_repr7compact decode -- = @1 -x @VUD -UVl @FL -jd @Yn1 -RBx @0z.z.z.z.z.yy -y.z.z.z.z.z00 @0z.z.z.z.z.z00 -y.z.z.z.z.z.yy
    0
    1
    -1
    999
    -999
    11
    -11
    7777
    -7777
    144/233
    -144/233
    233/377
    -233/377

fraction_repr7compact xdecode  aaa-y.z.z.z.z.z.yy555bbb --begin 3 --end -3
    (Fraction(-233, 377), 18)

fraction_repr7compact xdecode  aaa-y.z.z.z.z.z.yy555bbb --begin 3 --end 17
    ^EOFError: (1, 0, b'')
fraction_repr7compact xdecode  aaa-y.z.z.z.z.z.yy555bbb --begin 3 --end -7
    ^EOFError: (1, 0, b'')

fraction_repr7compact xdecode  aaa-y.z.z.z.z.z.yy555bbb --begin 3 --end -6
    (Fraction(-233, 377), 18)
fraction_repr7compact xdecode  aaa-y.z.z.z.z.z.yy555bbb --begin 3 --end 18
    (Fraction(-233, 377), 18)

fraction_repr7compact xdecode  aaa-y.z.z.z.z.z.yy555bbb --begin 3 --end 18 --strict
    -233/377

fraction_repr7compact xdecode  aaa-y.z.z.z.z.z.yy555bbb --begin 3 --end 19 --strict
    ^seed.int_tools.int_repr7lex_order7base.FormatError: ('5', 18, 19)

]]

[[
e ../../python3_src/bash_script/app/int_repr7compact
int_repr7compact encode 7777
    @WtW
]]
py -m nn_ns.app.int_repr7compact
[[
int_repr7compact encode 0 1 -1 999 -999 +11 -11 +7777 -7777
    =
    @0
    -y
    @Ub
    -VN
    @A
    -o
    @WtW
    -T5T

int_repr7compact decode -- = @0 -y @Ub -VN @A -o @WtW -T5T
    0
    1
    -1
    999
    -999
    11
    -11
    7777
    -7777

int_repr7compact xdecode  aaa-T5T555bbb --begin 3 --end -3
    (-7777, 7)

int_repr7compact xdecode  aaa-T5T555bbb --begin 3 --end 6
    ^EOFError: (2, 1, b'9')

int_repr7compact xdecode  aaa-T5T555bbb --begin 3 --end 7
    (-7777, 7)

int_repr7compact xdecode  aaa-T5T555bbb --begin 3 --end 7 --strict
    -7777

int_repr7compact xdecode  aaa-T5T555bbb --begin 3 --end 8 --strict
    ^seed.int_tools.int_repr7lex_order7base.FormatError: ('5', 7, 8)

]]


py_adhoc_call   seed.int_tools.int_repr7compact7lex_order7baseGL   @f
]]]'''#'''
#.__all__ = r'''
#.
#.
#.FormatError
#.    表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌
#.    解读冫整数巛文本表达牜紧凑牜词典序牜基表六七扌
#.        详解读冫整数巛文本表达牜紧凑牜词典序牜基表六七扌
#.        详解读冫整数巛趃文本表达牜紧凑牜词典序牜基表六七扌
#.
#.    表述冫整数讠位元串牜紧凑牜词典序牜基表六七扌
#.    详解读冫整数巛趃位元串牜紧凑牜词典序牜基表六七扌
#.
#.
#.表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌
#.    表述冫自然数讠位元串牜紧凑牜词典序牜基表六四扌
#.        表述冫自然数讠趃位元串串牜紧凑牜词典序牜基表六四扌
#.详解读冫自然数巛文本表达牜紧凑牜词典序牜基表六四扌
#.    详解读冫自然数巛趃文本表达牜紧凑牜词典序牜基表六四扌
#.        详解读冫自然数巛趃位元串牜紧凑牜词典序牜基表六四扌
#.'''.split()#'''
__all__ = r'''
匴整数耂文本表达牜紧凑牜词典序牜基表六七
    表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌
    解读冫整数巛文本表达牜紧凑牜词典序牜基表六七扌
    详解读冫整数巛文本表达牜紧凑牜词典序牜基表六七扌
    详解读冫整数巛趃文本表达牜紧凑牜词典序牜基表六七扌
        encode_int2txt7compact7lex_order7baseGL_
        decode_int5txt7compact7lex_order7baseGL_
        xdecode_int5txt7compact7lex_order7baseGL_
        xdecode_int5iter_chars7compact7lex_order7baseGL_






匴有理数耂文本表达牜紧凑牜词典序牜基表六七
    表述冫有理数讠文本表达牜紧凑牜词典序牜基表六七扌
    解读冫有理数巛文本表达牜紧凑牜词典序牜基表六七扌
    详解读冫有理数巛文本表达牜紧凑牜词典序牜基表六七扌
    详解读冫有理数巛趃文本表达牜紧凑牜词典序牜基表六七扌
        encode_fraction2txt7compact7lex_order7baseGL_
        decode_fraction5txt7compact7lex_order7baseGL_
        xdecode_fraction5txt7compact7lex_order7baseGL_
        xdecode_fraction5iter_chars7compact7lex_order7baseGL_









匴自然数耂文本表达牜紧凑牜词典序牜基表六四
    表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌
    解读冫自然数巛文本表达牜紧凑牜词典序牜基表六四扌
    详解读冫自然数巛文本表达牜紧凑牜词典序牜基表六四扌
    详解读冫自然数巛趃文本表达牜紧凑牜词典序牜基表六四扌
        encode_uint2txt7compact7lex_order7baseGL_
        decode_uint5txt7compact7lex_order7baseGL_
        xdecode_uint5txt7compact7lex_order7baseGL_
        xdecode_uint5iter_chars7compact7lex_order7baseGL_


'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...

from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
with mk_ctx4lazy_import4funcs_(__name__):
    from itertools import islice, pairwise, chain
    from seed.tiny_.check import check_type_is, check_int_ge, check_int_ge_lt
    from bisect import  bisect_left, bisect_right
    from seed.tiny_.funcs import fst,snd


    from seed.text.base64 import uint__to__radix64_digits_, uint__from__radix64_digits_# uint__to__radix64_digits__b64__str_, uint__from__radix64_digits__b64__str_
    #.def uint__to__radix64_digits_(u, /, *, bigendian, may_digit5uint6):
    #.    '-> [uint%64]&bytes'
    #def uint__from__radix64_digits_(bs, /, *, bigendian, may_digit2uint6):
    from seed.types.FrozenDict import mk_FrozenDict

from seed.int_tools.int_repr7lex_order7base import FormatError
from seed.int_tools.int_repr7lex_order7base import 乸数据字符串表达牜词典序牜前置长度牜使用匴数据位元串表达, 乸有理数位元串表达牜词典序牜前置长度牜连分数牜无穷大收尾
    #乸数据字符串表达牜词典序牜前置长度牜使用匴数据位元串表达(匴数据位元串表达, 列表纟字母表牜头胞辻多种体胞)
    #乸有理数位元串表达牜词典序牜前置长度牜连分数牜无穷大收尾(毝延后无穷大收尾, 匴整数位元串表达, 匴自然数位元串表达, 内符型讠外符型纟匴整数位元串表达, 内符型讠外符型纟匴自然数位元串表达)


from seed.int_tools.int_repr7lex_order7base import 乸整数位元串表达牜词典序牜前置长度牜整数零编码为单胞牜使用自然数编码器
    #乸整数位元串表达牜词典序牜前置长度牜整数零编码为单胞牜使用自然数编码器(欤深一, 规模纟头胞, 匴自然数位元串表达牜词典序牜前置长度)
from seed.int_tools.int_repr7lex_order7base__part2 import 乸自然数位元串表达牜词典序牜前置长度牜无颈胞牜分区表配置
    #乸自然数位元串表达牜词典序牜前置长度牜无颈胞牜分区表配置(欤编码无需头胞, 符型讠规模纟字母表, 分区表配置纟扩增自然数编码方案, 越界值讠深度, 升列纟自然数范围辻分区定位)
from seed.int_tools.int_repr7lex_order7base__part2 import 乸匴全局参数设置纟自然数编解码器, 乸分区方案纟扩增自然数编码, 乸缓存纟自由编码器, 乸分区表配置纟扩增自然数编码方案
    #乸分区表配置纟扩增自然数编码方案(深度讠配置, 后手编解码器)
    #乸分区方案纟扩增自然数编码(总层数, 规模纟占位, 体胞数纟首层, 符型牜首层体胞, 分区编解码器)
    #乸匴全局参数设置纟自然数编解码器(ops:(_魖共通, 魖数据位元串表达牜词典序牜前置长度))
    #乸缓存纟自由编码器(匴全局参数设置, 罓扩增自然数讠自由编码器讠层号讠带符型位元串, 罓体胞规模讠自然数讠位元串)
from seed.int_tools.int_repr7lex_order7base__part2 import 乸自然数分区断头编解码器牜体胞符型唯一牜带偏移, 无效后手编解码器牜自然数, 无效越界断头编解码器, 乸越界断头编解码器牜正无穷大
    #乸自然数分区断头编解码器牜体胞符型唯一牜带偏移(总层数, 体胞数纟首层, 符型纟体胞, 末层偏移量, 首胞偏移量)
    #乸越界断头编解码器牜正无穷大(符型纟体胞)
from seed.tiny_.oo8inf import oo


___end_mark_of_excluded_global_names__0___ = ...
###########################
###########################
###########################
###########################

#整数:牜紧凑牜词典序牜基表六七
#自然数:牜紧凑牜词典序牜基表六四
def _prepare():
    '-> (匴自然数位元串表达牜基表六四, 匴整数位元串表达牜基表六七, 匴整数字符串表达牜基表六七)'
    #########
    '自然数:牜紧凑牜词典序牜基表六四'
    符型讠规模纟字母表 = (64,)
    后手编解码器 = 无效后手编解码器牜自然数
    无效越界断头编解码器

    cfg = (
        #(总层数, 规模纟占位, 体胞数纟首层, 首胞偏移量)
        ((1, 16, 0, 0)
        ,(1, 16, 1, 0)
        ,(1, 16, 2, 0)
        ,(1, 8, 3, 0)
        ,(2, 5, 0, 4) #(1, 1, 4, 0), ...
        )
    ,#---------
        ((1, 16, 9, 0)
        ,(1, 16, 10, 0)
        ,(2, 16, 0, 11)
        ,(3, 8, 0, 1)
        ,(4, 4, 0, 1)
        )
    ,#---
        #(1, 4, 0, 0):to_be_continued
    )
    深度讠区号讠最大爻元数 = (
        ((4, 10, 16, 21, 48)
        ,(58, 64, 156) #,(58, 64, 156, 6*(-1+2**48))
            #取消最后一项<<==将会变成(2**最大爻元数) ^MemoryError
        ))

    越界值讠深度 = mk_FrozenDict({+oo:0})
    升列纟自然数范围辻分区定位 = tuple(((起点, 讫点), (深度, 区号)) for (_, _, 起点), (深度, 区号, 讫点) in pairwise(chain([(-1, -1, 0)], ((深度, 区号, 1<<最大爻元数) for 深度, 区号讠最大爻元数 in enumerate(深度讠区号讠最大爻元数) for 区号, 最大爻元数 in enumerate(区号讠最大爻元数)))))
        #((0, 1<<4), (0, 0))
        #((1<<4, 1<<10), (0, 1))
        #((1<<10, 1<<16), (0, 2))

    分区表配置纟扩增自然数编码方案 = _5cfg(cfg)
    #########
    匴自然数位元串表达牜基表六四 = 乸自然数位元串表达牜词典序牜前置长度牜无颈胞牜分区表配置(欤编码无需头胞:=True, 符型讠规模纟字母表, 分区表配置纟扩增自然数编码方案, 越界值讠深度, 升列纟自然数范围辻分区定位)
    #########
    '整数:牜紧凑牜词典序牜基表六七'
    匴整数位元串表达牜基表六七 = 乸整数位元串表达牜词典序牜前置长度牜整数零编码为单胞牜使用自然数编码器(欤深一:=True, 规模纟头胞:=3, 匴自然数位元串表达牜基表六四)
    #########
    列表纟字母表牜三丶六四 = 列表纟字母表牜头胞辻多种体胞 = (
    ('-=@'
    ,'.0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz'
    ))
    #########
    匴整数字符串表达牜基表六七 = 乸数据字符串表达牜词典序牜前置长度牜使用匴数据位元串表达(匴整数位元串表达牜基表六七, 列表纟字母表牜三丶六四)
    #########
    #.return (匴自然数位元串表达牜基表六四, 匴整数位元串表达牜基表六七, 匴整数字符串表达牜基表六七)
    #########
    列表纟字母表牜六四 = 列表纟字母表牜头胞辻多种体胞 = (
    (*''
    ,'.0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz'
    ))
    #########
    匴自然数字符串表达牜基表六四 = 乸数据字符串表达牜词典序牜前置长度牜使用匴数据位元串表达(匴自然数位元串表达牜基表六四, 列表纟字母表牜六四)
    #########
    return (匴自然数位元串表达牜基表六四, 匴整数位元串表达牜基表六七, 匴整数字符串表达牜基表六七, 匴自然数字符串表达牜基表六四)


def _5cfg(cfg, /):
    唯一符型 = 0
    符型牜首层体胞 = 唯一符型
    符型纟体胞 = 唯一符型
    末层偏移量 = 0
    后手编解码器 = 无效后手编解码器牜自然数
    越界断头编解码器 = 无效越界断头编解码器
    越界断头编解码器牜正无穷大 = 乸越界断头编解码器牜正无穷大(唯一符型)

    深度讠配置 = []
    for j, ts in enumerate(cfg):
        区号讠分区方案 = []
        for (总层数, 规模纟占位, 体胞数纟首层, 首胞偏移量) in ts:
            分区编解码器 = 乸自然数分区断头编解码器牜体胞符型唯一牜带偏移(总层数, 体胞数纟首层, 符型纟体胞, 末层偏移量, 首胞偏移量)
            分区方案 = 乸分区方案纟扩增自然数编码(总层数, 规模纟占位, 体胞数纟首层, 符型牜首层体胞, 分区编解码器)
            区号讠分区方案.append(分区方案)
        区号讠分区方案 = tuple(区号讠分区方案)
        配置乊深度 = (唯一符型, 区号讠分区方案, 越界断头编解码器 if j else 越界断头编解码器牜正无穷大)
        深度讠配置.append(配置乊深度)
    深度讠配置 = tuple(深度讠配置)
    分区表配置纟扩增自然数编码方案 = 乸分区表配置纟扩增自然数编码方案(深度讠配置, 后手编解码器)
    return 分区表配置纟扩增自然数编码方案
(_匴自然数位元串表达牜基表六四, _匴整数位元串表达牜基表六七, _匴整数字符串表达牜基表六七, _匴自然数字符串表达牜基表六四) = _prepare()
def _prepare2():
    匴有理数位元串表达牜基表六七 = 乸有理数位元串表达牜词典序牜前置长度牜连分数牜无穷大收尾(毝延后无穷大收尾:=0, 匴整数位元串表达:=_匴整数位元串表达牜基表六七, 匴自然数位元串表达:=_匴自然数位元串表达牜基表六四, 内符型讠外符型纟匴整数位元串表达:=(0,1), 内符型讠外符型纟匴自然数位元串表达:=(1,))
    匴有理数字符串表达牜基表六七 = 乸数据字符串表达牜词典序牜前置长度牜使用匴数据位元串表达(匴有理数位元串表达牜基表六七, _匴整数字符串表达牜基表六七.列表纟字母表牜头胞辻多种体胞)
    return 匴有理数字符串表达牜基表六七
_匴有理数字符串表达牜基表六七 = _prepare2()


__all__
###########################
###########################
###########################
###########################
FormatError = FormatError

#整数:牜紧凑牜词典序牜基表六七
#自然数:牜紧凑牜词典序牜基表六四
#.class 乸匴整数耂文本表达牜紧凑牜词典序牜基表六七(魖整数位元串表达牜词典序牜前置长度牜整数零编码为单胞, 魖数据字符串表达牜词典序牜前置长度):
#.    ___no_slots_ok___ = True
#.    #@override
#.    列表纟字母表牜头胞辻多种体胞 = (
#.    ('-=@'
#.    ,'.0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz'
#.    ))
#.
#.    @override
#.    def 罓解读冫正整数巛定型定长前取器扌(sf, 删负偏移后头胞纟正整数编码, 定型定长前取器, /):
#.        assert 删负偏移后头胞纟正整数编码 == 1
#.        return _罓解读冫正整数巛定型定长前取器扌(sf, 定型定长前取器)
#.    @override
#.    def 罓表述冫正整数讠趃序列纟带符型位元串扌(sf, 正整数, /):
#.        #bug:头胞串 = bytes([1]) #删负偏移后
#.        头胞串 = bytes([2])
#.        yield (0, 头胞串)
#.        yield from _罓表述冫正整数讠趃序列纟带符型位元串扌(sf, 正整数)
#._匴六七 = 匴整数耂文本表达牜紧凑牜词典序牜基表六七 = 乸匴整数耂文本表达牜紧凑牜词典序牜基表六七()
###########################
###########################
#整数:
###########################
###########################
_匴六七 = 匴整数耂文本表达牜紧凑牜词典序牜基表六七 = _匴整数字符串表达牜基表六七

表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌 = _匴六七.encode_dat2txt7lex_order_
解读冫整数巛文本表达牜紧凑牜词典序牜基表六七扌 = _匴六七.decode_dat5txt7lex_order_
详解读冫整数巛文本表达牜紧凑牜词典序牜基表六七扌 = _匴六七.xdecode_dat5txt7lex_order_
详解读冫整数巛趃文本表达牜紧凑牜词典序牜基表六七扌 = _匴六七.xdecode_dat5iter_chars7lex_order_
encode_int2txt7compact7lex_order7baseGL_ = 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌
decode_int5txt7compact7lex_order7baseGL_ = 解读冫整数巛文本表达牜紧凑牜词典序牜基表六七扌
xdecode_int5txt7compact7lex_order7baseGL_ = 详解读冫整数巛文本表达牜紧凑牜词典序牜基表六七扌
xdecode_int5iter_chars7compact7lex_order7baseGL_ = 详解读冫整数巛趃文本表达牜紧凑牜词典序牜基表六七扌


###########################
###########################
#有理数:
###########################
###########################
_匴六七 = 匴有理数耂文本表达牜紧凑牜词典序牜基表六七 = _匴有理数字符串表达牜基表六七

表述冫有理数讠文本表达牜紧凑牜词典序牜基表六七扌 = _匴六七.encode_dat2txt7lex_order_
解读冫有理数巛文本表达牜紧凑牜词典序牜基表六七扌 = _匴六七.decode_dat5txt7lex_order_
详解读冫有理数巛文本表达牜紧凑牜词典序牜基表六七扌 = _匴六七.xdecode_dat5txt7lex_order_
详解读冫有理数巛趃文本表达牜紧凑牜词典序牜基表六七扌 = _匴六七.xdecode_dat5iter_chars7lex_order_
encode_fraction2txt7compact7lex_order7baseGL_ = 表述冫有理数讠文本表达牜紧凑牜词典序牜基表六七扌
decode_fraction5txt7compact7lex_order7baseGL_ = 解读冫有理数巛文本表达牜紧凑牜词典序牜基表六七扌
xdecode_fraction5txt7compact7lex_order7baseGL_ = 详解读冫有理数巛文本表达牜紧凑牜词典序牜基表六七扌
xdecode_fraction5iter_chars7compact7lex_order7baseGL_ = 详解读冫有理数巛趃文本表达牜紧凑牜词典序牜基表六七扌


###########################
###########################
#自然数:
###########################
###########################
_匴六四 = 匴自然数耂文本表达牜紧凑牜词典序牜基表六四 = _匴自然数字符串表达牜基表六四

表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌 = _匴六四.encode_dat2txt7lex_order_
解读冫自然数巛文本表达牜紧凑牜词典序牜基表六四扌 = _匴六四.decode_dat5txt7lex_order_
详解读冫自然数巛文本表达牜紧凑牜词典序牜基表六四扌 = _匴六四.xdecode_dat5txt7lex_order_
详解读冫自然数巛趃文本表达牜紧凑牜词典序牜基表六四扌 = _匴六四.xdecode_dat5iter_chars7lex_order_
encode_uint2txt7compact7lex_order7baseGL_ = 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌
decode_uint5txt7compact7lex_order7baseGL_ = 解读冫自然数巛文本表达牜紧凑牜词典序牜基表六四扌
xdecode_uint5txt7compact7lex_order7baseGL_ = 详解读冫自然数巛文本表达牜紧凑牜词典序牜基表六四扌
xdecode_uint5iter_chars7compact7lex_order7baseGL_ = 详解读冫自然数巛趃文本表达牜紧凑牜词典序牜基表六四扌





###########################

###########################
#.class 乸匴自然数耂文本表达牜紧凑牜词典序牜基表六四(魖自然数位元串表达牜词典序牜前置长度, 魖数据字符串表达牜词典序牜前置长度):
#.    ___no_slots_ok___ = True
#.    #@override
#.    欤编码无需头胞 = True
#.    #@override
#.    列表纟字母表牜头胞辻多种体胞 = (
#.    (*[]
#.    ,'.0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz'
#.    ))
#.
#.    ##################
#.    @abstractmethod
#.    def 罓表述冫数据讠趃序列纟带符型位元串扌(sf, 数据, /):
#.        '数据 -> 趃序列纟带符型位元串/(Iter 带符型位元串/(符型/uint%len(符型讠规模纟字母表), 位元串牜子表/[位元{符型}]/(tuple|bytes|WordSeq)))'
#.    @abstractmethod
#.    def 罓解读冫数据巛定型定长前取器扌(sf, 定型定长前取器, /):
#.        '乸定型定长前取器{位元{符型}} -> 数据'
#.    ##################






###########################
def _main_(args=None, /):
    from seed.int_tools.int_repr7compact7lex_order7baseGL import encode_int2txt7compact7lex_order7baseGL_, decode_int5txt7compact7lex_order7baseGL_, xdecode_int5txt7compact7lex_order7baseGL_, xdecode_int5iter_chars7compact7lex_order7baseGL_
    import argparse
    parser = argparse.ArgumentParser(
        description='encode/decode int: [-=@][.0-9A-Z_a-z]*'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    action7subcmd = parser.add_subparsers(dest='subcmd', required=True)


    #######
    subparser7encode = action7subcmd.add_parser('encode', description='encode ints...')
    subparser7encode.add_argument('ints', nargs='*', type=int, help='ints to be encoded')

    #######
    subparser7decode = action7subcmd.add_parser('decode', description='strict decode strs as ints...')
    subparser7decode.add_argument('strs', nargs='*', type=str, help='strs to be encoded')


    #######
    subparser7xdecode = action7subcmd.add_parser('xdecode', description='nonstrict decode txt as int:output:(int, end)')
    subparser7xdecode.add_argument('txt', type=str, help='txt to be encoded')
    subparser7xdecode.add_argument('--strict', action='store_true', default=False, help='strict mode:output:int only')
    subparser7xdecode.add_argument('--begin', type=int, default=None, help='begin addr for txt')
    subparser7xdecode.add_argument('--end', type=int, default=None, help='end addr for txt')

    #######
    args = parser.parse_args(args)
    match args.subcmd:
        case 'encode':
            # encode_int2txt7compact7lex_order7baseGL_(int, /, *, validate=True) -> str
            for i in args.ints:
                print(encode_int2txt7compact7lex_order7baseGL_(i))
        case 'decode':
            # decode_int5txt7compact7lex_order7baseGL_(txt, begin=None, end=None, /, *, validate=True) -> int
            for s in args.strs:
                print(decode_int5txt7compact7lex_order7baseGL_(s))
        case 'xdecode':
            # xdecode_int5txt7compact7lex_order7baseGL_(txt, begin=None, end=None, /, *, validate=True) -> (int, end)
            (s, j, k) = _args = (args.txt, args.begin, args.end)
            (j, k, _1) = slice(j, k).indices(len(s))
            if args.strict:
                print(decode_int5txt7compact7lex_order7baseGL_(s, j, k))
            else:
                print(xdecode_int5txt7compact7lex_order7baseGL_(s, j, k))
        case bad:
            raise Exception(bad)
if __name__ == '__main__':
    from seed.int_tools.int_repr7compact7lex_order7baseGL import *
    from seed.int_tools.int_repr7compact7lex_order7baseGL import encode_int2txt7compact7lex_order7baseGL_, decode_int5txt7compact7lex_order7baseGL_, xdecode_int5txt7compact7lex_order7baseGL_, xdecode_int5iter_chars7compact7lex_order7baseGL_
    if 1:from seed.int_tools.int_repr7compact7lex_order7baseGL import _main_
    _main_()

###########################




###########################
def _main4fraction_(args=None, /):
    from fractions import Fraction
    from seed.int_tools.int_repr7compact7lex_order7baseGL import encode_fraction2txt7compact7lex_order7baseGL_, decode_fraction5txt7compact7lex_order7baseGL_, xdecode_fraction5txt7compact7lex_order7baseGL_, xdecode_fraction5iter_chars7compact7lex_order7baseGL_
    import argparse
    parser = argparse.ArgumentParser(
        description='encode/decode fraction: [-=@][.0-9A-Z_a-z]*'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )
    action7subcmd = parser.add_subparsers(dest='subcmd', required=True)


    #######
    subparser7encode = action7subcmd.add_parser('encode', description='encode fractions...')
    subparser7encode.add_argument('fractions', nargs='*', type=Fraction, help='fractions to be encoded')

    #######
    subparser7decode = action7subcmd.add_parser('decode', description='strict decode strs as fractions...')
    subparser7decode.add_argument('strs', nargs='*', type=str, help='strs to be encoded')


    #######
    subparser7xdecode = action7subcmd.add_parser('xdecode', description='nonstrict decode txt as Fraction:output:(Fraction, end)')
    subparser7xdecode.add_argument('txt', type=str, help='txt to be encoded')
    subparser7xdecode.add_argument('--strict', action='store_true', default=False, help='strict mode:output:Fraction only')
    subparser7xdecode.add_argument('--begin', type=int, default=None, help='begin addr for txt')
    subparser7xdecode.add_argument('--end', type=int, default=None, help='end addr for txt')

    #######
    args = parser.parse_args(args)
    match args.subcmd:
        case 'encode':
            # encode_fraction2txt7compact7lex_order7baseGL_(Fraction, /, *, validate=True) -> str
            for i in args.fractions:
                print(encode_fraction2txt7compact7lex_order7baseGL_(i))
        case 'decode':
            # decode_fraction5txt7compact7lex_order7baseGL_(txt, begin=None, end=None, /, *, validate=True) -> Fraction
            for s in args.strs:
                print(decode_fraction5txt7compact7lex_order7baseGL_(s))
        case 'xdecode':
            # xdecode_fraction5txt7compact7lex_order7baseGL_(txt, begin=None, end=None, /, *, validate=True) -> (Fraction, end)
            (s, j, k) = _args = (args.txt, args.begin, args.end)
            (j, k, _1) = slice(j, k).indices(len(s))
            if args.strict:
                print(decode_fraction5txt7compact7lex_order7baseGL_(s, j, k))
            else:
                print(xdecode_fraction5txt7compact7lex_order7baseGL_(s, j, k))
        case bad:
            raise Exception(bad)
if __name__ == '__main__':
    from seed.int_tools.int_repr7compact7lex_order7baseGL import *
    from seed.int_tools.int_repr7compact7lex_order7baseGL import encode_fraction2txt7compact7lex_order7baseGL_, decode_fraction5txt7compact7lex_order7baseGL_, xdecode_fraction5txt7compact7lex_order7baseGL_, xdecode_fraction5iter_chars7compact7lex_order7baseGL_
    if 1:from seed.int_tools.int_repr7compact7lex_order7baseGL import _main4fraction_
    #_main4fraction_()

###########################





















###########################
###########################
#首版:{硬编码}:
###########################
###########################
#:
#:
#:#.import string
#:#._字母表牜体胞 = f'.{string.digits}{string.ascii_uppercase}_{string.ascii_lowercase}'
#:_字母表牜体胞 = '.0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz'
#:_字母表牜头胞 = '-=@'
#:_字母表 = '.0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz-=@'
#:
#:_字符巛位元 = _字母表.__getitem__
#:_字符讠位元 = {ch:j for j, ch in enumerate(_字母表)}.__getitem__
#:
#:
#:def _u5GA(bs, /):
#:    u = uint__from__radix64_digits_(bs, bigendian=True, may_digit2uint6=None)
#:    return u
#:def _u2GA(u, /):
#:    bs = uint__to__radix64_digits_(u, bigendian=True, may_digit5uint6=None)
#:    return bs
#:class FormatError(Exception):pass
#:def 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(整数, /, *, 欤校验=True):
#:    '整数/int -> 文本/str'
#:    bs = 表述冫整数讠位元串牜紧凑牜词典序牜基表六七扌(整数, 欤校验=True)
#:    文本 = ''.join(map(_字符巛位元, bs))
#:    if 欤校验:
#:        (i, _end) = 详解读冫整数巛文本表达牜紧凑牜词典序牜基表六七扌(文本, 欤校验=False)
#:        if not _end == len(文本):raise Exception(整数, i, 文本, len(文本), _end)
#:        if not i == 整数:raise Exception(整数, i, 文本)
#:    return 文本
#:
#:def 解读冫整数巛文本表达牜紧凑牜词典序牜基表六七扌(文本, /, *, 欤校验=True):
#:    '文本/str -> 整数/int'
#:    (i, _end) = 详解读冫整数巛文本表达牜紧凑牜词典序牜基表六七扌(文本, 欤校验=欤校验)
#:    if not _end == len(文本):raise FormatError('tailing chars:', 文本[:_end], 文本[_end:])
#:    return i
#:def 详解读冫整数巛文本表达牜紧凑牜词典序牜基表六七扌(文本, 起址=None, 讫址=None, /, *, 欤校验=True):
#:    '文本/str -> 起址/uint -> 讫址/uint -> (整数/int, 讫址/uint)'
#:    check_type_is(str, 文本)
#:    js = range(len(文本))[起址:讫址]
#:    if not js:raise FormatError('empty')
#:    起址 = js[0]
#:    讫址 = 1+js[-1]
#:    趃文本 = map(文本.__getitem__, js)
#:    (i, sz, it) = 详解读冫整数巛趃文本表达牜紧凑牜词典序牜基表六七扌(趃文本)
#:    _end = 起址+sz
#:    if 欤校验:
#:        s = 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌(i, 欤校验=False)
#:        if not len(s) == sz:raise Exception(len(s), sz, 文本[起址:_end], s, i)
#:        if not s == (t:=文本[起址:_end]):raise Exception(t, s, i)
#:    return (i, _end)
#:def 详解读冫整数巛趃文本表达牜紧凑牜词典序牜基表六七扌(趃文本, /):
#:    '趃文本/(Iter char) -> (整数/int, 字符数牜消耗/uint, 趃文本/Iterator{char})'
#:    趃文本 = iter(趃文本)
#:    趃位元串 = map(_字符讠位元, 趃文本)
#:    (i, sz, it) = 详解读冫整数巛趃位元串牜紧凑牜词典序牜基表六七扌(趃位元串)
#:    return (i, sz, 趃文本)
#:
#:def 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(自然数, /, *, 欤允零=True, 欤校验=True):
#:    '自然数/int -> 文本/str'
#:    bs = 表述冫自然数讠位元串牜紧凑牜词典序牜基表六四扌(自然数, 欤允零=欤允零, 欤校验=False)
#:    文本 = ''.join(map(_字符巛位元, bs))
#:    if 欤校验:
#:        (u, _end) = 详解读冫自然数巛文本表达牜紧凑牜词典序牜基表六四扌(文本, 欤校验=False)
#:        if not _end == len(文本):raise Exception(自然数, u, 文本, len(文本), _end)
#:        if not u == 自然数:raise Exception(自然数, u, 文本)
#:    return 文本
#:
#:def 详解读冫自然数巛文本表达牜紧凑牜词典序牜基表六四扌(文本, 起址=None, 讫址=None, /, *, 欤允零=True, 欤校验=True):
#:    '文本/str -> 起址/uint -> 讫址/uint -> (自然数/uint, 讫址/uint)'
#:    check_type_is(str, 文本)
#:    js = range(len(文本))[起址:讫址]
#:    if not js:raise FormatError('empty')
#:    起址 = js[0]
#:    讫址 = 1+js[-1]
#:    趃文本 = map(文本.__getitem__, js)
#:    (u, sz, it) = 详解读冫自然数巛趃文本表达牜紧凑牜词典序牜基表六四扌(趃文本, 欤允零=欤允零)
#:    _end = 起址+sz
#:    if 欤校验:
#:        s = 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌(u, 欤允零=欤允零, 欤校验=False)
#:        if not len(s) == sz:raise Exception(len(s), sz, 文本[起址:_end], s, u)
#:        if not s == (t:=文本[起址:_end]):raise Exception(t, s, u)
#:    return (u, _end)
#:
#:def 详解读冫自然数巛趃文本表达牜紧凑牜词典序牜基表六四扌(趃文本, /, *, 欤允零=True):
#:    '趃文本/(Iter char) -> (自然数/uint, 字符数牜消耗/uint, 趃文本/Iterator{char})'
#:    趃文本 = iter(趃文本)
#:    趃位元串 = map(_字符讠位元, 趃文本)
#:    (u, sz, it) = 详解读冫自然数巛趃位元串牜紧凑牜词典序牜基表六四扌(趃位元串, 欤允零=欤允零)
#:    return (u, sz, 趃文本)
#:
#:
#:
#:def _趃取反冫体胞字节串扌(bs, /):
#:    return map((63).__xor__, bs)
#:def _取反冫体胞字节串扌(bs, /):
#:    return bytes(_趃取反冫体胞字节串扌(bs))
#:
#:def 表述冫整数讠位元串牜紧凑牜词典序牜基表六七扌(整数, /, *, 欤校验=True):
#:    '整数/int -> 位元串/([uint%67]&bytes)'
#:    check_type_is(int, 整数)
#:    if 整数 == 0:
#:        return b'A' # 65 as 0 # 64,65,66 as -0+
#:    自然数 = abs(整数)
#:    _bs = 表述冫自然数讠位元串牜紧凑牜词典序牜基表六四扌(自然数, 欤允零=False, 欤校验=False)
#:    if 整数 < 0:
#:        _bs = _取反冫体胞字节串扌(_bs)
#:        b0 = b'@'
#:    else:
#:        b0 = b'B'
#:    bs = b0 + _bs
#:    if 欤校验:
#:        (i, sz, it) = 详解读冫整数巛趃位元串牜紧凑牜词典序牜基表六七扌(bs)
#:        if not (sz==len(bs)):raise Exception(整数, i, bs, bs[:sz], len(bs), sz)
#:        if not (i==整数):raise Exception(整数, i, bs)
#:        for _ in it: raise 000
#:    return bs
#:def 详解读冫整数巛趃位元串牜紧凑牜词典序牜基表六七扌(趃位元串, /):
#:    '趃位元串/(Iter uint%67) -> (整数/int, 消耗量/uint, 趃位元串/Iterator{uint%67})'
#:    it = iter(趃位元串)
#:    head = _next(it, '<EOF>')
#:    check_int_ge_lt(64, 67, head)
#:    sign = head -65
#:    if sign == 0:
#:        i = 0
#:        return (i, 1, it)
#:    if sign < 0:
#:        it = _趃取反冫体胞字节串扌(it)
#:    (u, 消耗量, it) = 详解读冫自然数巛趃位元串牜紧凑牜词典序牜基表六四扌(it, 欤允零=False)
#:    i = sign*u
#:    return (i, 1+消耗量, it)
#:
#:
#:
#:#_max1_uint21 = 0x20_0000 #0x11_0000
#:#._max1_uint21 = (1<<21)
#:#._max1_uint4 = (1<<4)
#:#._max1_uint10 = (1<<10)
#:#._max1_uint16 = (1<<16)
#:#._max1_uint21 = (1<<21)
#:#._max1_uint24 = (1<<24)
#:#._max1_uint30 = (1<<30)
#:#._max1_uint36 = (1<<36)
#:#._max1_uint42 = (1<<42)
#:#._max1_uint48 = (1<<48)
#:#._max1_uint58 = (1<<58)
#:#._max1_uint64 = (1<<64)
#:def 表述冫自然数讠位元串牜紧凑牜词典序牜基表六四扌(自然数, /, *, 欤允零=True, 欤校验=True):
#:    '自然数/uint -> 位元串/([uint%64]&bytes)'
#:    bs = b''.join(表述冫自然数讠趃位元串串牜紧凑牜词典序牜基表六四扌(自然数, 欤允零=欤允零))
#:    if 欤校验:
#:        (u, sz, it) = 详解读冫自然数巛趃位元串牜紧凑牜词典序牜基表六四扌(bs, 欤允零=欤允零)
#:        if not (sz==len(bs)):raise Exception(自然数, u, bs, bs[:sz], len(bs), sz)
#:        if not (u==自然数):raise Exception(自然数, u, bs)
#:        for _ in it: raise 000
#:    return bs
#:def 表述冫自然数讠趃位元串串牜紧凑牜词典序牜基表六四扌(自然数, /, *, 欤允零=True):
#:    '自然数/uint -> 趃位元串串/Iter ([uint%64]&bytes)'
#:    check_int_ge(0, 自然数)
#:    if not 欤允零 and 0 == 自然数:raise TypeError
#:    u = 自然数
#:    #if u < _max1_uint21:
#:    #if u < 16:
#:    bsz = u.bit_length()
#:    #match bsz:
#:    if bsz <= 4:
#:        yield bytes([u])
#:        return
#:    # [bsz > 4]
#:    bs = _u2GA(u)
#:    L = len(bs)
#:    if bsz <= 64:
#:        # [4 < bsz <= 64]
#:        j = bisect_left(_bsz_params_ls, bsz, key=fst)
#:        assert j > 0
#:            # !! [bsz > 4]
#:        assert fst(_bsz_params_ls[j-1]) < bsz <= fst(_bsz_params_ls[j])
#:
#:        (总负载爻元数, 头胞偏移量, 头胞爻元数, 体胞数) = _bsz_params_ls[j]
#:        if L < 1+体胞数:
#:            bs = b'\0'*(1+体胞数 -L) +bs
#:            777;L = len(bs)
#:        if not L == 1+体胞数:raise 000
#:        if not bsz <= 48:
#:            yield b'=' # 61:深入
#:        yield bytes([头胞偏移量+bs[0]])
#:        yield bs[1:]
#:        return
#:    assert 10 < L
#:    # [11 <= L]
#:    yield b'=' # 61:深入
#:    if L <= 26:
#:        # [11 <= L <= 26]
#:        yield bytes([32 +(L-11)])
#:        yield bs
#:        return
#:    bs4L = _u2GA(L)
#:    L4L = len(bs4L)
#:    assert 0 < L4L
#:    # [1 <= L4L]
#:    if L4L <= 8:
#:        # [1 <= L4L <= 8]
#:        yield bytes([48 +(L4L-1)])
#:        yield bs4L
#:        yield bs
#:        return
#:    bs4L4L = _u2GA(L4L)
#:    L4L4L = len(bs4L4L)
#:    assert 0 < L4L4L
#:    # [1 <= L4L4L]
#:    if L4L4L <= 4:
#:        # [1 <= L4L4L <= 4]
#:        yield bytes([56 +(L4L4L-1)])
#:        yield bs4L4L
#:        yield bs4L
#:        yield bs
#:        return
#:    raise NotImplementedError('to_be_continued...')
#:
#:
#:# [bsz_params :: (总负载爻元数, 头胞偏移量, 头胞爻元数, 体胞数)]
#:_bsz_params_ls = (
#:[(4, 0, 4, 0)
#:,(10, 16, 4, 1)
#:,(16, 32, 4, 2)
#:,(21, 48, 3, 3)
#:,(24, 56, 0, 4)
#:,(30, 57, 0, 5)
#:,(36, 58, 0, 6)
#:,(42, 59, 0, 7)
#:,(48, 60, 0, 8)
#:#61:深入:
#:,(58, 0, 4, 9)
#:,(64, 16, 4, 10)
#:])
#:def 详解读冫自然数巛趃位元串牜紧凑牜词典序牜基表六四扌(趃位元串, /, *, 欤允零=True):
#:    '趃位元串/(Iter uint%64) -> (自然数/uint, 消耗量/uint, 趃位元串/Iterator{uint%64})'
#:    it = iter(趃位元串)
#:    head = _next(it, '<EOF>')
#:    check_int_ge_lt(0, 64, head)
#:    if head < 16:
#:        u = head
#:        return (u, 1, it)
#:    # [16 <= head]
#:    if head < 61:
#:        # [16 <= head < 61]
#:        j = bisect_right(_bsz_params_ls, head, 0, len(_bsz_params_ls)-2, key=snd)
#:            # bug:『-2』
#:            #   --> 『len(_bsz_params_ls)-2』
#:        assert j >= 2, (head, j, _bsz_params_ls[max(0,j-1):j+1])
#:            # !! [head >= 16]
#:        assert snd(_bsz_params_ls[j-1]) <= head < (snd(_bsz_params_ls[j]) or 61)
#:
#:        (总负载爻元数, 头胞偏移量, 头胞爻元数, 体胞数) = _bsz_params_ls[j-1]
#:        b0 = bytes([head -头胞偏移量])
#:        _bs = _take_bytes__sz_eq(体胞数, it)
#:        bs = b0 + _bs
#:        u = _u5GA(bs)
#:        return (u, 1+体胞数, it)
#:    if head == 61:
#:        neck = _next(it, '<EOF>')
#:        check_int_ge_lt(0, 64, neck)
#:        if neck < 32:
#:            if neck < 16:
#:                b0 = bytes([neck-0])
#:                体胞数 = 9
#:            else:
#:                b0 = bytes([neck-16])
#:                体胞数 = 10
#:            _bs = _take_bytes__sz_eq(体胞数, it)
#:            bs = b0 + _bs
#:            u = _u5GA(bs)
#:            return (u, 2+体胞数, it)
#:        # [32 <= neck]
#:        if neck < 48:
#:            # [32 <= neck < 48]
#:            体胞数 = 11 +(neck -32)
#:            bs = _take_bytes__sz_eq(体胞数, it)
#:            u = _u5GA(bs)
#:            return (u, 2+体胞数, it)
#:        # [48 <= neck]
#:        if neck < 56:
#:            # [48 <= neck < 56]
#:            L4L = 1 +(neck-48)
#:            bs4L = _take_bytes__sz_eq(L4L, it)
#:            L = _u5GA(bs4L)
#:            bs = _take_bytes__sz_eq(L, it)
#:            u = _u5GA(bs)
#:            return (u, 2+L4L+L, it)
#:        # [56 <= neck]
#:        if neck < 60:
#:            # [56 <= neck < 60]
#:            L4L4L = 1 +(neck-56)
#:            bs4L4L = _take_bytes__sz_eq(L4L4L, it)
#:            L4L = _u5GA(bs4L4L)
#:            bs4L = _take_bytes__sz_eq(L4L, it)
#:            L = _u5GA(bs4L)
#:            bs = _take_bytes__sz_eq(L, it)
#:            u = _u5GA(bs)
#:            return (u, 2+L4L4L+L4L+L, it)
#:        # [60 <= neck]
#:        if neck >= 60: raise NotImplementedError('to_be_continued...')
#:        raise 000
#:
#:    # [61 < head]
#:    if head > 61: raise NotImplementedError('to_be_continued...')
#:    raise 000
#:
#:
#:
#:
#:def _next(it, errmsg, /):
#:    for c in it:
#:        return c
#:    raise FormatError(errmsg)
#:def _take_bytes__sz_eq(sz, it, /):
#:    bs = bytes(islice(it, 0, sz))
#:    if not len(bs) == sz:raise FormatError('<EOF>')
#:    return bs
#:
#:__all__
#:from seed.int_tools.int_repr7compact7lex_order7baseGL import 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌, 解读冫整数巛文本表达牜紧凑牜词典序牜基表六七扌

__all__
from seed.int_tools.int_repr7compact7lex_order7baseGL import 匴整数耂文本表达牜紧凑牜词典序牜基表六七

from seed.int_tools.int_repr7compact7lex_order7baseGL import 表述冫整数讠文本表达牜紧凑牜词典序牜基表六七扌, 解读冫整数巛文本表达牜紧凑牜词典序牜基表六七扌, 详解读冫整数巛文本表达牜紧凑牜词典序牜基表六七扌, 详解读冫整数巛趃文本表达牜紧凑牜词典序牜基表六七扌
from seed.int_tools.int_repr7compact7lex_order7baseGL import encode_int2txt7compact7lex_order7baseGL_, decode_int5txt7compact7lex_order7baseGL_, xdecode_int5txt7compact7lex_order7baseGL_, xdecode_int5iter_chars7compact7lex_order7baseGL_








from seed.int_tools.int_repr7compact7lex_order7baseGL import 匴有理数耂文本表达牜紧凑牜词典序牜基表六七
from seed.int_tools.int_repr7compact7lex_order7baseGL import 表述冫有理数讠文本表达牜紧凑牜词典序牜基表六七扌, 解读冫有理数巛文本表达牜紧凑牜词典序牜基表六七扌, 详解读冫有理数巛文本表达牜紧凑牜词典序牜基表六七扌, 详解读冫有理数巛趃文本表达牜紧凑牜词典序牜基表六七扌
from seed.int_tools.int_repr7compact7lex_order7baseGL import encode_fraction2txt7compact7lex_order7baseGL_, decode_fraction5txt7compact7lex_order7baseGL_, xdecode_fraction5txt7compact7lex_order7baseGL_, xdecode_fraction5iter_chars7compact7lex_order7baseGL_










from seed.int_tools.int_repr7compact7lex_order7baseGL import 匴自然数耂文本表达牜紧凑牜词典序牜基表六四
from seed.int_tools.int_repr7compact7lex_order7baseGL import 表述冫自然数讠文本表达牜紧凑牜词典序牜基表六四扌, 解读冫自然数巛文本表达牜紧凑牜词典序牜基表六四扌, 详解读冫自然数巛文本表达牜紧凑牜词典序牜基表六四扌, 详解读冫自然数巛趃文本表达牜紧凑牜词典序牜基表六四扌
from seed.int_tools.int_repr7compact7lex_order7baseGL import encode_uint2txt7compact7lex_order7baseGL_, decode_uint5txt7compact7lex_order7baseGL_, xdecode_uint5txt7compact7lex_order7baseGL_, xdecode_uint5iter_chars7compact7lex_order7baseGL_







if 1:from seed.int_tools.int_repr7compact7lex_order7baseGL import _main_
if 1:from seed.int_tools.int_repr7compact7lex_order7baseGL import _main4fraction_
from seed.int_tools.int_repr7compact7lex_order7baseGL import *
