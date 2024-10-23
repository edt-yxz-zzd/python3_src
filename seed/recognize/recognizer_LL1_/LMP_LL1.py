#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LL1_/LMP_LL1.py
view others/数学/编程/设计/语法升级序列.txt
    LMP_LL1:标签耂复式耂点选耂山语法
        tr__AST5TOKENS4LMP_LL1__6LMP_LL1
    独立耂内嵌式注释格式
    独立耂内嵌式字符串格式


seed.recognize.recognizer_LL1_.LMP_LL1
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LL1_.LMP_LL1 -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LL1_.LMP_LL1:__doc__ -ht



[[[[[
@20241004:copy from:view others/数学/编程/设计/语法升级序列.txt

===
[[[
LMP_LL1
  label-multi-pick-LL1
  degrade:LMFP_LL1--
    label-multi-fork-pick-LL1 -『fork』
标签耂复式耂点选耂山语法
    ==降级:标签耂复式耂腹叉耂点选耂山语法 -『腹叉耂』
    山语法==LL1==分路单前瞻左起左展识别用语法
    点选==(拆包|忽略|择留)
    复式==(庸复式|诡复式)
    标签==必空式牜标签型
        #必空式:载入冫标签冃况态:属于后处理的一种

===
后处理程序 注册于 母符/(母符+础符) #并联式
  LL1 不可能有两个并联分支使用 相同 母符(即使算上 后缀/复式)
  [锚定:后处理程序] ==>> [尽量精简表达式]
===
===
[[
tr__AST5TOKENS4LMP_LL1__6LMP_LL1 ::=
  ^^^ 合法整句
  ; 合法整句 .=
    , -"^^^"
    , +整句母符
    , +氵窢母符定义*
    , -"$$$"

  ; 整句母符 @= "母符"
  ; 氵窢母符定义 @=
    -";"
    =母符定义?
  ; 母符定义 .=
    , +"母符"
    , +冫定义体
  ; 冫定义体 :=
    | 冫并联体
    | 冫串联体
    | 冫别名体

  ; 代符 :=
    | "母符"
    | "种符"
  ; 础符 :=
    | 代符
    | "标签" #必空式

  ; 冫并联体 .=
    , +":="     #保留作为标签
    , +丨窢标签化复础符*
  ; 冫串联体 .=
    , +".="     #保留作为标签
    , +丿土复础符*
    # 串联体 需要 『,』分隔 『*』『+』源自:后缀纟诡复式牜略vs点选符
    #   而 别名体 则无需『,』，因为只用了『-』『=』
  ; 冫别名体 .=
    , +"@="     #保留作为标签
    , + 别名体
  ; 别名体 := {|
      | &<'幺'> 复础符
      | &<'取'> 取一体
      |}
  ; 取一体 .=
    , +一冫复础符*
    , +二冫复础符
    , +一冫复础符*
  ; 一冫复础符 .=
    , -"-"
    , +复础符
  ; 二冫复础符 .=
    , -"="
    , +复础符

  ; 丿土复础符 .=
    , -","
    , +点选符
    , +复础符
  ; 点选符 :=
    | "-" #忽略
    | "+" #择留
    | "*" #拆包

  ; 丨窢标签化复础符 .=
    , -"|"
    , +彑标签*
    , +复础符   #注意:标签 本身就是 复础符
    , +彑标签*
  ; 彑标签 @=
    -"&"
    +"标签"

  ; 复础符 :=
    | 庸标签
    | 复代符
  ; 庸标签 .=
    , +标签
    , +后缀纟庸复式?
  ; 复代符 .=
    , +代符
    , +后缀纟复式?

  ; 后缀纟复式 :=
    | &<'庸复式'> 后缀纟庸复式
    | &<'诡复式'> 后缀纟诡复式
  ; 后缀纟庸复式 @=
    -"["
    ="自然数"
    -"]"
  ; 后缀纟诡复式 :=
    | &<'详'> 后缀纟诡复式牜详
    | &<'略'> 后缀纟诡复式牜略
  ; 后缀纟诡复式牜略 :=
    | "?" # {0..=1}
    | "*" # {0..<}
    | "+" # {1..<}
  ; 后缀纟诡复式牜详 .=
    , -"{"
    , +"自然数"
    , +连数符
    , +"自然数"?
    , -"}"
  ; 连数符 :=
    | "..<"
    | "..="
  $$$ #END
#end-tr__AST5TOKENS4LMP_LL1__6LMP_LL1
===
标签:6
<'幺'>
<'取'>
<'庸复式'>
<'诡复式'>
  <'详'>
  <'略'>
===
种符:24
"^^^"
"$$$"
";"
"@="
".="
":="
","
"|"
"&"
"?"
"*"
"+"
"-"
"="
"["
"]"
"{"
"}"
"..<"
"..="
"自然数"    # regex"\d+"
"母符"      # regex"\w+"
"种符"      # 独立耂内嵌式字符串格式
"标签"      # regex"<{独立耂内嵌式字符串格式}>"

===
母符:27
合法整句
整句母符
氵窢母符定义
母符定义
冫定义体
冫并联体
冫串联体
冫别名体
代符
础符
别名体
取一体
一冫复础符
二冫复础符
丨窢标签化复础符
丿土复础符
彑标签
复础符
庸标签
复代符
点选符
后缀纟复式
后缀纟庸复式
后缀纟诡复式
后缀纟诡复式牜略
后缀纟诡复式牜详
连数符
===
]]


===
]]]
[[
独立耂内嵌式注释格式
    避免每种语言单独设计一种格式
vivi:独立耂内嵌式字符串格式
原貌注释牜内嵌式 = regex"\[-#(<[^<>]*>)((?!\1)(.|\r|\n))*?\1#-\]"
  允许多行...
显码注释牜内嵌式 = regex"\[#({转码序列}|(?![?][!])[^\#\r\n])*#]"
  禁止多行...
  注释用引号『#』
    "?!+" --> #

]]
[[
独立耂内嵌式字符串格式
    避免每种语言单独设计一种格式


独立耂内嵌式字符串格式 =
  | 原貌字符串牜内嵌式
  | 显码字符串牜内嵌式


原貌字符串vs显码字符串(==转码字符串)
  原貌-不再解码
  显码-再解码

内嵌式vs行尾式
  内嵌式-带引号
  行尾式-不带引号
  原貌字符串牜内嵌式vs原貌字符串牜行尾式
  显码字符串牜内嵌式vs显码字符串牜行尾式

原貌字符串牜内嵌式 = regex"\[(<[^<>]*>)((?!\1)(.|\r|\n))*?\1\]"
  允许多行...
显码字符串牜内嵌式 = regex"{引号}({转码序列}|(?![?][!])[^\'\"\r\n])*{引号}"
  禁止多行...
  引号 = regex"[\'\"]"
  转码序列 =
    # [.abfnrtv%~,:;+=-] + {...}
    | "?!." --> 『?!』
    | regex"[?][!][{][ +]*((u\x+|[abfnrtv])[ +]*)*[}]"
    | regex"[?][!][abfnrtv]"
        # [:短名列表纟转码序列]:goto

    | "?!%" --> 空串
    | "?!~" --> 空格
    | "?!," --> \t
    | "?!:" --> \r
    | "?!;" --> \n
        # <EMPTY><Space><TAB><CR><LF>
    | "?!+" --> #
        # 注释用引号『#』:见:独立耂内嵌式注释格式
    | "?!=" --> "
    | '?!-' --> '
        # 引号『'』『"』
    #xxx: | "?!'" --> "
    #xxx: | '?!"' --> '
        # 反转单双引号
    #xxx: | "?!`" --> 外引号(" or ')
        # 相对性引号

[[[
[:短名列表纟转码序列]:here
短名列表纟转码序列:abfnrtv
===
abfnrtv<<==py:help('STRINGS')
  |"\a"|ASCII Bell (BEL)          |
  |"\b"|ASCII Backspace (BS)      |
  |"\f"|ASCII Formfeed (FF)       |
  |"\n"|ASCII Linefeed (LF)       |
  |"\r"|ASCII Carriage Return (CR)|
  |"\t"|ASCII Horizontal Tab (TAB)|
  |"\v"|ASCII Vertical Tab (VT)   |
>>> [*b'\a\b\f\n\r\t\v']
[7, 8, 12, 10, 13, 9, 11]
>>> [*map(hex,b'\a\b\f\n\r\t\v')]
['0x7', '0x8', '0xc', '0xa', '0xd', '0x9', '0xb']
>>> {*b'\a\b\f\n\r\t\v'} == set(range(7,14))
True

===
]]]



]]
]]]]]



py_adhoc_call   seed.recognize.recognizer_LL1_.LMP_LL1   @f
from seed.recognize.recognizer_LL1_.LMP_LL1 import *
#]]]'''
__all__ = r'''
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.str_tools.cut_text_by_marker_seq import cut_text_by_marker_seq, strip_text_by_marker_pair

from seed.recognize.tokenizer_.Tokenizer4Text import \
(ITokenizer4Text
,    Tokenizer4Text__no_state
,    Tokenizer4Text__with_state_stack
,        TknzStOp
,            NOP
,            RET
,            mk_jmp_
,            mk_cal_
#
,IWordReader4Text
,    WordReader4Text__parallel__priority
,    WordReader4Text__constant_words__longest_first
,    WordReader4Text__constant_heads__longest_first
,    WordReader4Text__wrapper__replace_tkey
,    IWordReader4Text__wrapper__eval_tdat
,        WordReader4Text__wrapper__eval_tdat
,    WordReader4Text__regex
)



___end_mark_of_excluded_global_names__0___ = ...

######################
######################
######################
tr__AST5TOKENS4LMP_LL1__6LMP_LL1 = strip_text_by_marker_pair(__doc__
,'\ntr__AST5TOKENS4LMP_LL1__6LMP_LL1 ::=\n'
,'\n#end-tr__AST5TOKENS4LMP_LL1__6LMP_LL1\n'
)

######################
######################
######################
ptn4raw_str = pattern4multiline_embedded_style_raw_string_literal = r"\[(<[^<>\s]*>)(?:(?!\1)(?:.|\r|\n))*\1\]"
#pattern4inline_embedded_style_esc_string_literal = r"""(["'])(?:[?][!](?:[.abfnrtv%~,:;+=-]|[{][^\'\"\r\n{}]*[}])|(?![?][!])[^\'\"\r\n])*\1"""
ptn4esc_str = pattern4inline_embedded_style_esc_string_literal = r"""(["'])(?:[?][!](?:[.abfnrtv%~,:;+=-]|[{][ +]*(?:(?:u[0-9a-fA-F]+|\b[abfnrtv]+\b)[ +]*)*[}])|(?![?][!])[^\'\"\r\n])*\1"""
    # [.abfnrtv%~,:;+=-] + {...}
    # regex"[?][!][{][ +]*((u\x+|[abfnrtv])[ +]*)*[}]"
ptn4hdr4raw_str = pattern4header4multiline_embedded_style_raw_string_literal = r"\[<" # ">\]"
ptn4hdr4esc_str = pattern4header4inline_embedded_style_esc_string_literal = r"""["']"""


wr__raw_str = WordReader4Text__regex('raw_str', ptn4hdr4raw_str, ptn4raw_str)
wr__esc_str = WordReader4Text__regex('esc_str', ptn4hdr4esc_str, ptn4esc_str)

wr__str = WordReader4Text__parallel__priority(False, [wr__esc_str, wr__raw_str])


######################
######################
######################
ptn4raw_cmn = pattern4multiline_embedded_style_raw_comment_literal = r"\[-#(<[^<>\s]*>)(?:(?!\1)(?:.|\r|\n))*\1#-\]"
ptn4esc_cmn = pattern4inline_embedded_style_esc_comment_literal = r"""\[#(?:[?][!](?:[.abfnrtv%~,:;+=-]|[{][ +]*(?:(?:u[0-9a-fA-F]+|\b[abfnrtv]+\b)[ +]*)*[}])|(?![?][!])[^#\r\n])*#\]"""

ptn4hdr4raw_cmn = pattern4header4multiline_embedded_style_raw_comment_literal = r"\[-#" # "#-\]"
ptn4hdr4esc_cmn = pattern4header4inline_embedded_style_esc_comment_literal = r"\[#" # "#\]"

wr__raw_cmn = WordReader4Text__regex('raw_cmn', ptn4hdr4raw_cmn, ptn4raw_cmn)
wr__esc_cmn = WordReader4Text__regex('esc_cmn', ptn4hdr4esc_cmn, ptn4esc_cmn)

wr__cmn = WordReader4Text__parallel__priority(False, [wr__esc_cmn, wr__raw_cmn])



######################
######################
######################




######################
######################
######################
__all__
from seed.recognize.recognizer_LL1_.LMP_LL1 import *
