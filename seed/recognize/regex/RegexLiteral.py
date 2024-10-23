#__all__:goto
r'''[[[
e ../../python3_src/seed/recognize/regex/RegexLiteral.py
view ../../python3_src/seed/seq_tools/mk_prefix_tree.py
view ../../python3_src/seed/seq_tools/avoid_substrs.py
    view ../../python3_src/seed/seq_tools/prefixes2tree.py
view ../../python3_src/seed/seq_tools/escape_schemes/README.txt
    view ../../python3_src/seed/seq_tools/escape_schemes/universal_single_point_escape_scheme__enable_raw_text__disable_recur.py


seed.recognize.regex.RegexLiteral
py -m nn_ns.app.debug_cmd   seed.recognize.regex.RegexLiteral -x
py -m nn_ns.app.doctest_cmd seed.recognize.regex.RegexLiteral:__doc__ -ht
py -m nn_ns.app.doctest_cmd seed.recognize.regex.RegexLiteral:__doc__ -ht    >  /sdcard/0my_files/tmp/0tmp      2>&1
view /sdcard/0my_files/tmp/0tmp
%s/\n\n*# Line .*//


[[[[[[[
[[[
===
预处理:忽略空格
换码/转义:区分:普通文本,超文本
换码序列前缀:『?!』
禁用『?!?...』
普通文本:
    非空格耂普通字符
    『?!.』-->『?!』
    『?!-』-->『 』
    『?!:』-->『\r』
    『?!;』-->『\n』
    『?!,』-->『\t』
    『?![...]』
        『?![字符编码 字符编码 ...]』-->字符串
            字符编码:
                "+{十六进制数}"
                "@{名纟字符}"
                "."
                "-"
                ","
                ":"
                ";"
        『?![#注释...#]』-->'comment' if _to_output_comment_
超文本:
    『?!(...)』
    变量定义:
        『?!({;)』『?!(;变量名=)』表达式...『?!(;})』表达式
            特别是 表达式牜字集运算
    变量引用:
        『?!(&:变量名)』
        『?!(&%内置变量名)』
        『?!(&@统合码版本号.属性名=属性值)』
            SetRepr_5Unicode_property
    字符集合:
        『?!({.|)』字符 ... 『?!(|.})』
            枚举字集
        『?!({|)』字符/字集变量 ... 『?!(|})』
            并集
            SetRepr_Union
        『?!({~)』字符 字符 『?!(~})』
            区间
            SetRepr_5Intervals
            #xxx 『?!({~)』字符 『?!(..=)』 字符 『?!(,)』 ... 『?!(~})』
        表达式牜字集运算:
            『?!({|)』字符/字集变量 ... 『?!(|})』
                并集
                SetRepr_Union
            『?!({&)』字符/字集变量 ... 『?!(&})』
                交集
                SetRepr_Intersection
            『?!({-)』字符/字集变量 字符/字集变量 『?!(-})』
                差集
                SetRepr_Diff
            『?!({%-)』字符/字集变量 『?!(-%})』
                补集
                SetRepr_Negation
            『?!({%})』
                全集
    正则表达式:
        默认串联
        #xxx『?!([,)』字符/字集变量 ... 『?!(,])』
            RegexRepr_Concatenation
            RegexRepr_HollowTransition
            RegexRepr_SolidTransition
        『?!([|)』字符/字集变量 『?!(|)』... 『?!(|])』
            RegexRepr_Alternation
        『?!([*,)』字符/字集变量 ... 『?!(,*])』
            RegexRepr_Repetition
        『?!([+,)』字符/字集变量 ... 『?!(,+])』
            RegexRepr_Many1
        『?!([?,)』字符/字集变量 ... 『?!(,?])』
            RegexRepr_Optional
        『?!([[min:max],)』字符/字集变量 ... 『?!(,[:]])』
            RegexRepr_Array
        『?!($^终态名)』
            RegexRepr_Colored

===
料符串化
#前提:已经过:预处理:忽略空格:dry_()
先识别并区分超凡:
    ?!(...)
再识别并替换文本:
    #包括『?!(...)』的负载文本
    ?![...]
    ?!{单字符}

===
语法书
#前提:已经过:文本替换
正则表达式 = 顽式*

顽式 =:
    | 普通字符 ##<---普通文本
    | 变量定义
    | 正则表达式变量引用
        # 变量名纟正则表达式 = "[" 名 "]"
        #此处不能用:无印『变量引用』#因为 下面的『字符集合』已经包含了『字集变量引用』
    | 字符集合
    #xxx| 串式
    | 并式
    | 复式
    | 终态着色式
字符集合 =:
    | 字集变量引用
        # 变量名纟字符集合 = "{" 名 "}"
    | 区间
    | 枚举字集
    | 并集
    | 交集
    | 差集
    | 补集
    | 全集
#xxx串式 = '[,' 正则表达式 ',]'
并式 = '[|' 正则表达式 ('|' 正则表达式 )* '|]'
复式 =:
    | '[*,' 正则表达式 ',*]'
    | '[+,' 正则表达式 ',+]'
    | '[?,' 正则表达式 ',?]'
    | '[[:],'{.min,.may_max} 正则表达式 ',[:]]'
并集 = '{|' 集内字集* '|}'
交集 = '{&' 集内字集* '&}'
差集 = '{-' 字符集合 集内字集+ '-}'
补集 = '{%-' 集内字集* '-%}'
全集 = '{%}'

##集内字集 =:
##    | 普通文本
##    | 字符集合
#使用『枚举字集』=>:
集内字集 = 字符集合

枚举字集 = '{.|' 普通字符* '|.}'
区间 = '{~' 普通字符 普通字符 '~}'
变量定义 = '{;' 定义式* ';}'
定义式 =:
    | 正则表达式定义式
    | 字集定义式
正则表达式定义式 = ';[]='{.name} 正则表达式
字符集合定义式 = ';{}='{.name} 字符集合
##变量引用 =:
##    | 自定义变量引用
##    | 内置变量引用
##    | 统合码属性字集引用
正则表达式变量引用 =:
    | 自定义正则表达式变量引用
    | 内置正则表达式变量引用
字集变量引用 =:
    | 自定义字集变量引用
    | 内置字集变量引用
    | 统合码属性字集引用

##自定义变量引用 = '&:'{.name}
##内置变量引用 = '&%'{.name}

自定义正则表达式变量引用 = '&:[]'{.name}
内置正则表达式变量引用 = '&%[]'{.name}

自定义字集变量引用 = '&:{}'{.name}
内置字集变量引用 = '&%{}'{.name}
统合码属性字集引用 = '&@.='{.unicode_version,.property_name,.property_value}
终态着色式 = '$^'{.color}
###普通文本 = 普通字符*
普通字符 = 'char'{.char}

===
种符:
xxx '[,'
xxx ',]'
'[|'
'|'
'|]'
'[*,'
',*]'
'[+,'
',+]'
'[?,'
',?]'
'[[:],'
',[:]]'
'{|'
'|}'
'{&'
'&}'
'{-'
'-}'
'{%-'
'-%}'
'{%}'
'{.|'
'|.}'
'{~'
'~}'
'{;'
';}'
';[]='
';{}='
'&:[]'
'&%[]'
'&:{}'
'&%{}'
'&@.='
'$^'
'char'

##'&:'
##'&%'
===
???锚式???
    前瞻型锚式?
    回顾型锚式?
===
]]]

[[[
view ../../python3_src/seed/recognize/regex/RegexRepr.py
===

ISetRepr
    SetRepr_5Intervals
    SetRepr_5Unicode_property
    SetRepr_Union
    SetRepr_Intersection
    SetRepr_Diff
    SetRepr_Negation


IRegexRepr
    RegexRepr_Concatenation
    RegexRepr_Alternation
    RegexRepr_Repetition
    RegexRepr_HollowTransition
    RegexRepr_SolidTransition
    RegexRepr_Colored
    RegexRepr_Array
    RegexRepr_Optional
    RegexRepr_Many1


===
]]]

[[[
regex_literal_format
===
*ignore_space
*[is_anti_bifix__simple_mode(prefix4escape_seq)]
*[len(escape_seq) > len(prefix4escape_seq)][escape_seq[len(prefix4escape_seq)] =!= prefix4escape_seq[0]]
===
[is_anti_bifix__simple_mode(prefix4escape_seq)] =[def]=:
    [len(prefix4escape_seq) > 0]
    [prefix4escape_seq[0] not in prefix4escape_seq[1:]]
    [prefix4escape_seq[-1] not in prefix4escape_seq[:-1]]
===
ignore_space
[[
view ../../python3_src/seed/seq_tools/escape_schemes/README.txt
view ../lots/NOTE/char/space.txt
===
@[unicode14_0_0&py3_11_9_re2_2_1]

py.re.space:29
unicode14.WSpace:25
unicode14.Pat_WS:11

relationship:
  [ranges4Pat_WS <!> ranges4WSpace]
  [ranges4Pat_WS <!> ranges4space4py_re]
  [ranges4WSpace < ranges4space4py_re]

ranges4Pat_WS_and_py_re_sp:31
  {0x9: 5, 0x1C: 5, 0x85: 1, 0xA0: 1, 0x1680: 1, 0x2000: 11, 0x200E: 2, 0x2028: 2, 0x202F: 1, 0x205F: 1, 0x3000: 1}
  '\t\n\x0b\x0c\r\x1c\x1d\x1e\x1f \x85\xa0\u1680\u2000\u2001\u2002\u2003\u2004\u2005\u2006\u2007\u2008\u2009\u200a\u200e\u200f\u2028\u2029\u202f\u205f\u3000'
  ages4sp
    {'3.0', '3.2', '1.1'}
    scripts4sp
      {'Ogam', 'Zyyy'}
  scripts4sp
    {'Ogam', 'Zyyy'}
### [:list_all_spaces6unicode14_0_0__py3_11_9_re2_2_1]:goto


]]
]]]
]]]]]]]

[[[[[[[
{{{{{{{

>>> def tokenize__str(s, /):
...     it = ((c,j) for j,c in enumerate(s, 1))
...     return [*tokenizer4RegexLiteral.tokenize(0, it)]

>>> def tokenize__str(s, /):
...     return [*tokenizer4RegexLiteral.tokenize__str(s)]


#>>> tokenize__str(' \t\r\n')
#
#>>> tokenize__str('?!.')
#>>> tokenize__str('?!-')
#>>> tokenize__str('?!,')
#>>> tokenize__str('?!:')
#>>> tokenize__str('?!;')
#
#>>> tokenize__str('?![#...comment...#]')
#>>> tokenize__str('?![]')
#>>> tokenize__str('?![@solidus+41+3000@space]')
#>>> tokenize__str('?![.-,:;]')
#
#>>> tokenize__str('?!')
#>>> tokenize__str('?!()')
#>>> tokenize__str('?!(...)')
#>>> tokenize__str('?!(?!(|))')
#
#>>> tokenize__str(r"""abc 012 -+*!? ~@#$%^&*/-_+=<>|\:;,.  "'` ()[]{}""")
#
xxx #>>> tokenize__str('?!([,)')
xxx #>>> tokenize__str('?!(,])')
#>>> tokenize__str('?!([|)')
#>>> tokenize__str('?!(|)')
#>>> tokenize__str('?!(|])')
#>>> tokenize__str('?!([*,)')
#>>> tokenize__str('?!(,*])')
#>>> tokenize__str('?!([+,)')
#>>> tokenize__str('?!(,+])')
#>>> tokenize__str('?!([?,)')
#>>> tokenize__str('?!(,?])')
#>>> tokenize__str('?!([[:],)')
#>>> tokenize__str('?!(,[:]])')
#>>> tokenize__str('?!({|)')
#>>> tokenize__str('?!(|})')
#>>> tokenize__str('?!({&)')
#>>> tokenize__str('?!(&})')
#>>> tokenize__str('?!({-)')
#>>> tokenize__str('?!(-})')
#>>> tokenize__str('?!({%-)')
#>>> tokenize__str('?!(-%})')
#>>> tokenize__str('?!({%})')
#>>> tokenize__str('?!({.|)')
#>>> tokenize__str('?!(|.})')
#>>> tokenize__str('?!({~)')
#>>> tokenize__str('?!(~})')
#>>> tokenize__str('?!({;)')
#>>> tokenize__str('?!(;})')
#>>> tokenize__str('?!(;[]=)')
#>>> tokenize__str('?!(;{}=)')
#>>> tokenize__str('?!(&:[])')
#>>> tokenize__str('?!(&%[])')
#>>> tokenize__str('?!(&:{})')
#>>> tokenize__str('?!(&%{})')
#>>> tokenize__str('?!(&@.=)')
#>>> tokenize__str('?!($^)')
#>>> tokenize__str('?!(char)')
#
#
#>>> tokenize__str('?!([[:],)')
#>>> tokenize__str('?!([[666:],)')
#>>> tokenize__str('?!([[:999],)')
#>>> tokenize__str('?!([[666:999],)')
#>>> tokenize__str('?!(;[usr_regex_nm]=)')
#>>> tokenize__str('?!(;{usr_charset_nm}=)')
#>>> tokenize__str('?!(&:[usr_regex_nm])')
#>>> tokenize__str('?!(&%[std_regex_nm])')
#>>> tokenize__str('?!(&:{usr_charset_nm})')
#>>> tokenize__str('?!(&%{std_charset_nm})')
#>>> tokenize__str('?!(&@ver14_0_0.sc=Zyyy)')
#>>> tokenize__str('?!($^color_00ff00)')
#
#




>>> tokenize__str(' \t\r\n')
[]
>>> tokenize__str('?!.')
[(2, ('char', {'char': '?'}), 3), (3, ('char', {'char': '!'}), 3)]
>>> tokenize__str('?!-')
[(2, ('char', {'char': ' '}), 3)]
>>> tokenize__str('?!,')
[(2, ('char', {'char': '\t'}), 3)]
>>> tokenize__str('?!:')
[(2, ('char', {'char': '\r'}), 3)]
>>> tokenize__str('?!;')
[(2, ('char', {'char': '\n'}), 3)]
>>> tokenize__str('?![#...comment...#]')
[]
>>> tokenize__str('?![]')
[]
>>> tokenize__str('?![.-,:;]')
[(3, ('char', {'char': '?'}), 4), (4, ('char', {'char': '!'}), 4), (4, ('char', {'char': ' '}), 5), (5, ('char', {'char': '\t'}), 6), (6, ('char', {'char': '\r'}), 7), (7, ('char', {'char': '\n'}), 8)]
>>> tokenize__str('?![@solidus+41+3000@space]')
[(3, ('char', {'char': '/'}), 11), (11, ('char', {'char': 'A'}), 14), (14, ('char', {'char': '\u3000'}), 19), (19, ('char', {'char': ' '}), 25)]
>>> tokenize__str('?!')
Traceback (most recent call last):
    ...
seed.recognize.regex.RegexLiteral.BadFormat__eof: 2
>>> tokenize__str('?!()')
Traceback (most recent call last):
    ...
seed.recognize.regex.RegexLiteral.BadFormat__unknown_meta_char_payload: (3, '', 3)
>>> tokenize__str('?!(...)')
Traceback (most recent call last):
    ...
seed.recognize.regex.RegexLiteral.BadFormat__unknown_meta_char_payload: (3, '...', 6)
>>> tokenize__str('?!(?!(|))')
Traceback (most recent call last):
    ...
seed.recognize.regex.RegexLiteral.BadFormat__unexpected_esc: (3, 5)
>>> tokenize__str('?!([,)') #[(3, ('[,', {}), 5)]
Traceback (most recent call last):
    ...
seed.recognize.regex.RegexLiteral.BadFormat__unknown_meta_char_payload: (3, '[,', 5)
>>> tokenize__str('?!(,])') #[(3, (',]', {}), 5)]
Traceback (most recent call last):
    ...
seed.recognize.regex.RegexLiteral.BadFormat__unknown_meta_char_payload: (3, ',]', 5)
>>> tokenize__str('?!([|)')
[(3, ('[|', {}), 5)]
>>> tokenize__str('?!(|)')
[(3, ('|', {}), 4)]
>>> tokenize__str('?!(|])')
[(3, ('|]', {}), 5)]
>>> tokenize__str('?!([*,)')
[(3, ('[*,', {}), 6)]
>>> tokenize__str('?!(,*])')
[(3, (',*]', {}), 6)]
>>> tokenize__str('?!([+,)')
[(3, ('[+,', {}), 6)]
>>> tokenize__str('?!(,+])')
[(3, (',+]', {}), 6)]
>>> tokenize__str('?!([?,)')
[(3, ('[?,', {}), 6)]
>>> tokenize__str('?!(,?])')
[(3, (',?]', {}), 6)]
>>> tokenize__str('?!([[:],)')
[(3, ('[[:],', {'min': 0, 'may_max': None}), 8)]
>>> tokenize__str('?!(,[:]])')
[(3, (',[:]]', {}), 8)]
>>> tokenize__str('?!({|)')
[(3, ('{|', {}), 5)]
>>> tokenize__str('?!(|})')
[(3, ('|}', {}), 5)]
>>> tokenize__str('?!({&)')
[(3, ('{&', {}), 5)]
>>> tokenize__str('?!(&})')
[(3, ('&}', {}), 5)]
>>> tokenize__str('?!({-)')
[(3, ('{-', {}), 5)]
>>> tokenize__str('?!(-})')
[(3, ('-}', {}), 5)]
>>> tokenize__str('?!({%-)')
[(3, ('{%-', {}), 6)]
>>> tokenize__str('?!(-%})')
[(3, ('-%}', {}), 6)]
>>> tokenize__str('?!({%})')
[(3, ('{%}', {}), 6)]
>>> tokenize__str('?!({.|)')
[(3, ('{.|', {}), 6)]
>>> tokenize__str('?!(|.})')
[(3, ('|.}', {}), 6)]
>>> tokenize__str('?!({~)')
[(3, ('{~', {}), 5)]
>>> tokenize__str('?!(~})')
[(3, ('~}', {}), 5)]
>>> tokenize__str('?!({;)')
[(3, ('{;', {}), 5)]
>>> tokenize__str('?!(;})')
[(3, (';}', {}), 5)]
>>> tokenize__str('?!(;[]=)')
Traceback (most recent call last):
    ...
seed.recognize.regex.RegexLiteral.BadFormat__unknown_meta_char_payload: (3, ';[]=', 7)
>>> tokenize__str('?!(;{}=)')
Traceback (most recent call last):
    ...
seed.recognize.regex.RegexLiteral.BadFormat__unknown_meta_char_payload: (3, ';{}=', 7)
>>> tokenize__str('?!(&:[])')
Traceback (most recent call last):
    ...
seed.recognize.regex.RegexLiteral.BadFormat__unknown_meta_char_payload: (3, '&:[]', 7)
>>> tokenize__str('?!(&%[])')
Traceback (most recent call last):
    ...
seed.recognize.regex.RegexLiteral.BadFormat__unknown_meta_char_payload: (3, '&%[]', 7)
>>> tokenize__str('?!(&:{})')
Traceback (most recent call last):
    ...
seed.recognize.regex.RegexLiteral.BadFormat__unknown_meta_char_payload: (3, '&:{}', 7)
>>> tokenize__str('?!(&%{})')
Traceback (most recent call last):
    ...
seed.recognize.regex.RegexLiteral.BadFormat__unknown_meta_char_payload: (3, '&%{}', 7)
>>> tokenize__str('?!(&@.=)')
Traceback (most recent call last):
    ...
seed.recognize.regex.RegexLiteral.BadFormat__unknown_meta_char_payload: (3, '&@.=', 7)
>>> tokenize__str('?!($^)')
Traceback (most recent call last):
    ...
seed.recognize.regex.RegexLiteral.BadFormat__unknown_meta_char_payload: (3, '$^', 5)
>>> tokenize__str('?!(char)')
Traceback (most recent call last):
    ...
seed.recognize.regex.RegexLiteral.BadFormat__unknown_meta_char_payload: (3, 'char', 7)
>>> tokenize__str('?!([[:],)')
[(3, ('[[:],', {'min': 0, 'may_max': None}), 8)]
>>> tokenize__str('?!([[666:],)')
[(3, ('[[:],', {'min': 666, 'may_max': None}), 11)]
>>> tokenize__str('?!([[:999],)')
[(3, ('[[:],', {'min': 0, 'may_max': 999}), 11)]
>>> tokenize__str('?!([[666:999],)')
[(3, ('[[:],', {'min': 666, 'may_max': 999}), 14)]
>>> tokenize__str('?!(;[usr_regex_nm]=)')
[(3, (';[]=', {'name': 'usr_regex_nm'}), 19)]
>>> tokenize__str('?!(;{usr_charset_nm}=)')
[(3, (';{}=', {'name': 'usr_charset_nm'}), 21)]
>>> tokenize__str('?!(&:[usr_regex_nm])')
[(3, ('&:[]', {'name': 'usr_regex_nm'}), 19)]
>>> tokenize__str('?!(&%[std_regex_nm])')
[(3, ('&%[]', {'name': 'std_regex_nm'}), 19)]
>>> tokenize__str('?!(&:{usr_charset_nm})')
[(3, ('&:{}', {'name': 'usr_charset_nm'}), 21)]
>>> tokenize__str('?!(&%{std_charset_nm})')
[(3, ('&%{}', {'name': 'std_charset_nm'}), 21)]
>>> tokenize__str('?!(&@ver14_0_0.sc=Zyyy)')
[(3, ('&@.=', {'unicode_version': 'ver14_0_0', 'property_name': 'sc', 'property_value': 'Zyyy'}), 22)]
>>> tokenize__str('?!($^color_00ff00)')
[(3, ('$^', {'color': 'color_00ff00'}), 17)]



>>> tokenize__str(r"""abc 012 -+*!? ~@#$%^&*/-_+=<>|\:;,.  "'` ()[]{}""") == (
... [(0, ('char', {'char': 'a'}), 1)
... , (1, ('char', {'char': 'b'}), 2)
... , (2, ('char', {'char': 'c'}), 3)
... , (3, ('char', {'char': '0'}), 5)
... , (5, ('char', {'char': '1'}), 6)
... , (6, ('char', {'char': '2'}), 7)
... , (7, ('char', {'char': '-'}), 9)
... , (9, ('char', {'char': '+'}), 10)
... , (10, ('char', {'char': '*'}), 11)
... , (11, ('char', {'char': '!'}), 12)
... , (12, ('char', {'char': '?'}), 13)
... , (13, ('char', {'char': '~'}), 15)
... , (15, ('char', {'char': '@'}), 16)
... , (16, ('char', {'char': '#'}), 17)
... , (17, ('char', {'char': '$'}), 18)
... , (18, ('char', {'char': '%'}), 19)
... , (19, ('char', {'char': '^'}), 20)
... , (20, ('char', {'char': '&'}), 21)
... , (21, ('char', {'char': '*'}), 22)
... , (22, ('char', {'char': '/'}), 23)
... , (23, ('char', {'char': '-'}), 24)
... , (24, ('char', {'char': '_'}), 25)
... , (25, ('char', {'char': '+'}), 26)
... , (26, ('char', {'char': '='}), 27)
... , (27, ('char', {'char': '<'}), 28)
... , (28, ('char', {'char': '>'}), 29)
... , (29, ('char', {'char': '|'}), 30)
... , (30, ('char', {'char': '\\'}), 31)
... , (31, ('char', {'char': ':'}), 32)
... , (32, ('char', {'char': ';'}), 33)
... , (33, ('char', {'char': ','}), 34)
... , (34, ('char', {'char': '.'}), 35)
... , (35, ('char', {'char': '"'}), 38)
... , (38, ('char', {'char': "'"}), 39)
... , (39, ('char', {'char': '`'}), 40)
... , (40, ('char', {'char': '('}), 42)
... , (42, ('char', {'char': ')'}), 43)
... , (43, ('char', {'char': '['}), 44)
... , (44, ('char', {'char': ']'}), 45)
... , (45, ('char', {'char': '{'}), 46)
... , (46, ('char', {'char': '}'}), 47)])
True


######################
######################
######################
# recur comment:
#
>>> [*tokenizer4RegexLiteral.tokenize__str('?![#?!-?![-,:;.+41]666?![#777?![#abc#]888#]999#]')]
[]
>>> [*tokenizer4RegexLiteral__with_comment.tokenize__str('?![#?!-?![-,:;.+41]666?![#777?![#abc#]888#]999#]')]
[(4, ('comment', {'comment': '  \t\r\n?!.A666?![#777?![#abc#]888#]999'}), 48)]

>>> [*tokenizer4RegexLiteral.tokenize__str('?!(|)')]
[(3, ('|', {}), 4)]
>>> [*tokenizer4RegexLiteral.tokenize__str('?![#?!(|)#]')]
Traceback (most recent call last):
    ...
seed.recognize.regex.RegexLiteral.BadFormat__forbid_mata_char: 6
>>> [*tokenizer4RegexLiteral__with_comment.tokenize__str('?![#?!(|)#]')]
Traceback (most recent call last):
    ...
seed.recognize.regex.RegexLiteral.BadFormat__forbid_mata_char: 6

}}}}}}}
#]]]]]]]
#]]]]]
]]]]]]]


[[[[[[[
{{{{{{{
>>> parser__2x2 = parser4RegexLiteral__with_2x2_builtins

>>> parser__2x2.parse__text(r"""
... ?![#...comment...#]
... """)
RegexRepr_HollowTransition()
>>> parser__2x2.parse__text(r'?!-')
RegexRepr_SolidTransition(SetRepr_5Intervals((Solo(' '),)))
>>> parser__2x2.parse__text(r'?')
RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('?'),)))
>>> parser__2x2.parse__text(r'?!.')
RegexRepr_Concatenation(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('?'),))), RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('!'),))))
>>> repr(parser__2x2.parse__text(r"""
... ?!.
... ?!-
... ?!,
... ?!:
... ?!;
... """)) == (r"""
... RegexRepr_Concatenation(
... RegexRepr_Concatenation(
... RegexRepr_Concatenation(
... RegexRepr_Concatenation(
... RegexRepr_Concatenation(
... RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('?'),)))
... , RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('!'),)))
... ), RegexRepr_SolidTransition(SetRepr_5Intervals((Solo(' '),)))
... ), RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('\t'),)))
... ), RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('\r'),)))
... ), RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('\n'),)))
... )
... """).replace('\n', '')
True


>>> parser__2x2.parse__text(r'?')
RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('?'),)))
>>> parser__2x2.parse__text(r'!')
RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('!'),)))
>>> parser__2x2.parse__text(r'? ! ;')
RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('\n'),)))

>>> parser__2x2.parse__text(r'?!({;)  ?!(;[rex]=) a ?!(;})') is hollow_regex # ""
True
>>> hollow_regex
RegexRepr_HollowTransition()
>>> parser__2x2.parse__text(r'?!({;)  ?!(;[rex]=) a ?!(;}) ?!(&:[rex])') # "a"
RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'),)))
>>> parser__2x2.parse__text(r'?!({;)  ?!(;[rex]=) a ?!(;}) ?!(&:[rex2])')
Traceback (most recent call last):
    ...
KeyError: '[rex2]'
>>> parser__2x2.parse__text(r'?!({;)  ?!(;[rex]=) a ?!(;}) ?!(&:[rex])  ?!({;)  ?!(;[rex]=) b ?!(;}) ?!(&:[rex])') # "ab"
RegexRepr_Concatenation(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'),))), RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('b'),))))
>>> parser__2x2.parse__text(r'?!({;)  ?!(;[rex]=) a ?!(;}) ?!([|) ?!({;)  ?!(;[rex]=) b ?!(;})  ?!(&:[rex]) ?!(|]) ?!(&:[rex])') # "ba"
RegexRepr_Concatenation(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('b'),))), RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'),))))
>>> parser__2x2.parse__text(r'?!({;)  ?!(;[rex]=) a  ?!(;[rex]=) b  ?!(;}) ?!(&:[rex]) ') # "b"
RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('b'),)))
>>> parser__2x2.parse__text(r'?!({;)  ?!(;[rex]=) a  ?!(;[rex2]=) b  ?!(;}) ?!(&:[rex2]) ?!(&:[rex]) ') # "ba"
RegexRepr_Concatenation(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('b'),))), RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'),))))
>>> parser__2x2.parse__text(r'?!(&%[dead_regex])') is dead_regex
True
>>> dead_regex
RegexRepr_SolidTransition(SetRepr_5Intervals(()))


>>> parser__2x2.parse__text(r'?!(&%{empty_set_repr})')
RegexRepr_SolidTransition(SetRepr_5Intervals(()))
>>> hollow_regex / empty_set_repr
RegexRepr_SolidTransition(SetRepr_5Intervals(()))
>>> parser__2x2.parse__text(r'?!(&%{whole_set_repr})')
RegexRepr_SolidTransition(SetRepr_5Intervals((oo[:-oo:, :+oo:],)))
>>> hollow_regex / whole_set_repr
RegexRepr_SolidTransition(SetRepr_5Intervals((oo[:-oo:, :+oo:],)))


>>> parser__2x2.parse__text(r'?!({;)  ?!(;{cset}=) ?!({.|) a ?!(|.}) ?!(;}) ?!(&:{cset})') # "a"
RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'),)))
>>> parser__2x2.parse__text(r'?!({;)  ?!(;{cset}=) a ?!(;}) ?!(&:{cset})') # "a"
Traceback (most recent call last):
    ...
seed.recognize.regex.RegexLiteral.ParseFail__unexpected_tkey: (((1, 21), ('char', {'char': 'a'}), (1, 23)), dict_keys(['&:{}', '&%{}', '&@.=', '{~', '{.|', '{|', '{&', '{-', '{%-', '{%}']))
>>> parser__2x2.parse__text(r'?!({;)  ?!(;{cset}=) ?!({|) a ?!(|}) ?!(;}) ?!(&:{cset})') # "a"
Traceback (most recent call last):
    ...
seed.recognize.regex.RegexLiteral.ParseFail__unexpected_tkey: (((1, 28), ('char', {'char': 'a'}), (1, 30)), dict_keys(['&:{}', '&%{}', '&@.=', '{~', '{.|', '{|', '{&', '{-', '{%-', '{%}']))



>>> parser__2x2.parse__text(r'?!([|)   a ?!(|) bc ?!(|])') # "a|bc"
RegexRepr_Alternation(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'),))), RegexRepr_Concatenation(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('b'),))), RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('c'),)))))
>>> parser__2x2.parse__text(r'?!([*,)   a b ?!(,*])') # "(ab)*"
RegexRepr_Repetition(RegexRepr_Concatenation(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'),))), RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('b'),)))))
>>> parser__2x2.parse__text(r'?!([+,)   a b ?!(,+])') # "(ab)+"
RegexRepr_Many1(RegexRepr_Concatenation(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'),))), RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('b'),)))))
>>> parser__2x2.parse__text(r'?!([?,)   a b ?!(,?])') # "(ab)?"
RegexRepr_Optional(RegexRepr_Concatenation(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'),))), RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('b'),)))))
>>> parser__2x2.parse__text(r'?!([[:],) a b ?!(,[:]])') # "(ab){:}"
RegexRepr_Repetition(RegexRepr_Concatenation(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'),))), RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('b'),)))))
>>> parser__2x2.parse__text(r'?!([[2:2],) a b ?!(,[:]])') # "(ab){:}"
RegexRepr_Array(RegexRepr_Concatenation(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'),))), RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('b'),)))), RegexRepr_Concatenation(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'),))), RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('b'),)))), 2, 2)


>>> parser__2x2.parse__text(r'?!($^color_00ff00)')
RegexRepr_Colored(RegexRepr_HollowTransition(), 'color_00ff00')
>>> parser__2x2.parse__text(r'?!([|)   a ?!($^color_000) ?!(|) bc ?!($^color_111) ?!(|])') # "a|bc"
RegexRepr_Alternation(RegexRepr_Concatenation(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'),))), RegexRepr_Colored(RegexRepr_HollowTransition(), 'color_000')), RegexRepr_Concatenation(RegexRepr_Concatenation(RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('b'),))), RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('c'),)))), RegexRepr_Colored(RegexRepr_HollowTransition(), 'color_111')))






字符集合
>>> parser__2x2.parse__text(r'?!(&%{empty_set_repr})')
RegexRepr_SolidTransition(SetRepr_5Intervals(()))
>>> parser__2x2.parse__text(r'?!(&:{empty_set_repr})')
Traceback (most recent call last):
    ...
KeyError: '{empty_set_repr}'
>>> parser__2x2.parse__text(r'?!({~) a ?![+3000] ?!(~})')
RegexRepr_SolidTransition(SetRepr_5Intervals((oo['a'::, ::'\u3000'],)))
>>> parser__2x2.parse__text(r'?!({~) ?![+61+3000] ?!(~})')
RegexRepr_SolidTransition(SetRepr_5Intervals((oo['a'::, ::'\u3000'],)))
>>> parser__2x2.parse__text(r'?!({.|) ?![+61+3000] ?!(|.})')
RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'), Solo('\u3000'))))
>>> parser__2x2.parse__text(r'?!({.|)  ?!(|.})')
RegexRepr_SolidTransition(SetRepr_5Intervals(()))
>>> parser__2x2.parse__text(r'?!({.|) a ?!(|.})')
RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'),)))
>>> parser__2x2.parse__text(r'?!({.|) abc ?!(|.})')
RegexRepr_SolidTransition(SetRepr_5Intervals((Solo('a'), Solo('b'), Solo('c'))))
>>> parser__2x2.parse__text(r'?!({|)  ?!(|})')
RegexRepr_SolidTransition(SetRepr_Union(()))
>>> parser__2x2.parse__text(r'?!({|) ?!({~) ?![+61+3000] ?!(~})  ?!({~) 09 ?!(~}) ?!(|})')
RegexRepr_SolidTransition(SetRepr_Union((SetRepr_5Intervals((oo['a'::, ::'\u3000'],)), SetRepr_5Intervals((oo['0'::, ::'9'],)))))
>>> parser__2x2.parse__text(r'?!({&)  ?!(&})')
RegexRepr_SolidTransition(SetRepr_Intersection(()))
>>> parser__2x2.parse__text(r'?!({&) ?!({~) 5a ?!(~})  ?!({~) 09 ?!(~}) ?!(&})')
RegexRepr_SolidTransition(SetRepr_Intersection((SetRepr_5Intervals((oo['5'::, ::'a'],)), SetRepr_5Intervals((oo['0'::, ::'9'],)))))
>>> parser__2x2.parse__text(r'?!({-) ?!({~) 5a ?!(~})  ?!({~) 09 ?!(~}) ?!(-})')
RegexRepr_SolidTransition(SetRepr_Diff(SetRepr_5Intervals((oo['5'::, ::'a'],)), SetRepr_5Intervals((oo['0'::, ::'9'],))))
>>> parser__2x2.parse__text(r'?!({%-) ?!({~) 5a ?!(~})  ?!({~) 09 ?!(~}) ?!(-%})')
RegexRepr_SolidTransition(SetRepr_Negation(SetRepr_Union((SetRepr_5Intervals((oo['5'::, ::'a'],)), SetRepr_5Intervals((oo['0'::, ::'9'],))))))
>>> parser__2x2.parse__text(r'?!({%-)  ?!({~) 09 ?!(~}) ?!(-%})')
RegexRepr_SolidTransition(SetRepr_Negation(SetRepr_Union((SetRepr_5Intervals((oo['0'::, ::'9'],)),))))
>>> parser__2x2.parse__text(r'?!({%-)  ?!(-%})')
RegexRepr_SolidTransition(SetRepr_Negation(SetRepr_Union(())))
>>> parser__2x2.parse__text(r'?!({%})')
RegexRepr_SolidTransition(SetRepr_5Intervals((oo[:-oo:, :+oo:],)))




#}}}}}}}
#}}}}}
}}}}}}}
]]]]]]]

py_adhoc_call   seed.recognize.regex.RegexLiteral   @f
#]]]'''
__all__ = r'''
Parser4RegexLiteral
    parser4RegexLiteral__no_builtins
    parser4RegexLiteral__with_2x2_builtins
tokenizer4RegexLiteral
tokenizer4RegexLiteral__with_comment












Fail
    ParseFail
        ParseFail__eof
        ParseFail__unexpected_tkey
        ParseFail__expected_tkey
    TokenizeFail
        BadFormat
            BadFormat__eof
            BadFormat__char_esc_fmt
            BadFormat__esc_esc
            BadFormat__unknown_meta_char_payload
            BadFormat__forbid_mata_char
            BadFormat__forbid_esc_inside_escaped_chars
            BadFormat__unexpected_esc
            BadFormat__unknown_char_esc_fmt
            BadFormat__unknown_single_char_payload


Parser4RegexLiteral
    parser4RegexLiteral__no_builtins
    parser4RegexLiteral__with_2x2_builtins
Tokenizer4RegexLiteral
    tokenizer4RegexLiteral
Tokenizer4RegexLiteral__with_comment
    tokenizer4RegexLiteral__with_comment
mk_positioned_chars5text
mk_positioned_chars5str

IterUntilEndMarker
dry_
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from itertools import chain, pairwise
import re
#from string import hexdigits as _hxs
#isxdigit = _hxs.__contains__
from unicodedata import lookup as _nm2ch

#DONE:ctx-->HistoryMapping
from seed.types.mapping.DynamicStackedMapping import DynamicStackedMapping
    #p0 = d.env_tell()
    #d.env_pop_until(p0)
    #with d.mk_contextmanager() as p0:
from seed.iters.PeekableIterator import PeekableIterator, echo_or_mk_PeekableIterator
from seed.tiny_.check import check_type_is, check_type_le, check_int_ge, check_pair



from seed.tiny import fst, snd, ifNone, echo, MapView
from seed.tiny_.HashedPair import Solo
from seed.recognize.regex.RegexRepr import hollow_regex, dead_regex, empty_set_repr, whole_set_repr
from seed.recognize.regex.RegexRepr import SetRepr_5Unicode_property
from seed.recognize.regex.RegexRepr import \
(ISetRepr
,    ISetRepr_IntervalBased
,        ISetRepr_Wrapper
,            SetRepr_5Unicode_property
,            SetRepr_Wrapper
,                SetRepr_Diff
,        SetRepr_5Intervals
,            slice2soloXopen_interval
,            solo2open_interval
,            empty_set_repr
,        SetRepr_Negation
,        SetRepr_Union
,        SetRepr_Intersection
#
,IRegexRepr
,    ISetRepr
,        ISetRepr_IntervalBased
,    Colored
,    HollowTransition
,    SolidTransition
#
,IRegexRepr
,    IRegexRepr__start_pst_is_0__stop_pst_is_1
,        offset_uint2pst_
,        RegexRepr_Concatenation
,        RegexRepr_Alternation
,        RegexRepr_Repetition
,        RegexRepr_HollowTransition
,            hollow_regex
,        RegexRepr_SolidTransition
,            dead_regex
,    RegexRepr_Wrapper
,        RegexRepr_Colored
,        RegexRepr_Array
,        RegexRepr_Optional
,        RegexRepr_Many1
)

___end_mark_of_excluded_global_names__0___ = ...

######################
class Fail(Exception):pass
class ParseFail(Fail):pass
class TokenizeFail(Fail):pass
class BadFormat(TokenizeFail):pass

######################
ParseFail
class ParseFail__eof(ParseFail):pass
class ParseFail__unexpected_tkey(ParseFail):pass
class ParseFail__expected_tkey(ParseFail):pass

######################
BadFormat
class BadFormat__eof(BadFormat):pass
class BadFormat__char_esc_fmt(BadFormat):pass
class BadFormat__esc_esc(BadFormat):pass
class BadFormat__unknown_meta_char_payload(BadFormat):pass
class BadFormat__forbid_mata_char(BadFormat):pass
class BadFormat__forbid_esc_inside_escaped_chars(BadFormat):pass
class BadFormat__unexpected_esc(BadFormat):pass
class BadFormat__unknown_char_esc_fmt(BadFormat):pass
class BadFormat__unknown_single_char_payload(BadFormat):pass
######################





######################
_rex4sp = re.compile(r'\s+')
def dry_(raw_txt, /):
    dry_txt = _rex4sp.sub('', raw_txt)
    return dry_txt
######################

class Parser4RegexLiteral:
    r'''[[[
    LL1
    [positioned_chars :: Iter (char, position_info)]
    [token :: (position_info, (tkey/str, tdat/dict), position_info)]
    #]]]'''#'''
    def __init__(sf, gctx4builtins, /):
        sf._gctx = MapView(gctx4builtins)
            # vs:ctx-usrdef
    def parse__text(sf, text, position_info=(1,1), /):
        tokens = tokenizer4RegexLiteral.tokenize__text(text, position_info)
        return sf.parse__tokens(position_info, tokens)
    def parse__str(sf, s, position_info=0, /):
        tokens = tokenizer4RegexLiteral.tokenize__str(s, position_info)
        return sf.parse__tokens(position_info, tokens)

    def parse(sf, position_info, positioned_chars, /):
        'position_info -> Iter (char, position_info) -> IRegexRepr'
        tokens = tokenizer4RegexLiteral.tokenize(position_info, positioned_chars)
        return sf.parse__tokens(position_info, tokens)
    def parse__tokens(sf, position_info, tokens, /):
        'position_info -> Iter token -> IRegexRepr'
        tokens = echo_or_mk_PeekableIterator(tokens)
        ctx = DynamicStackedMapping({}) # usrdefs
        regex_repr, end_position_info = sf._parse_regex(ctx, position_info, tokens, non_eof_ok=False)
        check_type_le(IRegexRepr, regex_repr)
        return regex_repr
    def _parse_regex(sf, ctx, position_info, tokens, /, *, non_eof_ok=True):
        #to used with _parse_xxx_between/_parse_xxx_array_sepby_endby_tkey ==>> [default:non_eof_ok:=True]
        'ctx -> position_info -> PeekableIterator token -> (IRegexRepr, position_info)'
        check_type_is(PeekableIterator, tokens)
        #正则表达式
        #ls = []
        r = hollow_regex
        p = position_info
        with ctx.mk_contextmanager():
          while not tokens.is_empty():
            if non_eof_ok:
                tkn = sf._peek1(position_info, tokens)
                (_prev_p, (tkey, tdat), _p) = tkn
                tkey2nm = sf._4parse_atomic_regex
                if not tkey in tkey2nm:
                    break
            regex_repr, p = sf._parse_atomic_regex(ctx, p, tokens)
            #ls.append(regex_repr)
            r <<= regex_repr
        #if len(ls) == 1:
        #    [regex_repr] = ls
        #else:
        #    regex_repr = RegexRepr_Concatenation(ls)
        regex_repr = r
        return regex_repr, p
    def _switch(sf, tkey2nm, ctx, position_info, tokens, /):
        tkn = sf._peek1(position_info, tokens)
        (prev_p, (tkey, tdat), p) = tkn
        m = tkey2nm.get(tkey)
        if m is None:
            raise ParseFail__unexpected_tkey(tkn, tkey2nm.keys())
        nm = m
        return getattr(sf, nm)(ctx, position_info, tokens)
    def _peek1(sf, position_info, tokens, /):
        if tokens.is_empty():
            raise ParseFail__eof(position_info)
        return tokens.head
    def _read1(sf, position_info, tokens, /):
        tkn = sf._peek1(position_info, tokens)
        next(tokens)
        return tkn
    def _parse_constant_tkeys(sf, tkeys, ctx, position_info, tokens, /):
        '[tkey] -> ctx -> position_info -> PeekableIterator token -> ([tdat], position_info)'
        p = position_info
        tdats = []
        for tkey in tkeys:
            tkn = sf._read1(position_info, tokens)
            (prev_p, (_tkey, tdat), p) = tkn
            if not _tkey == tkey:
                raise ParseFail__expected_tkey(tkey, tkn)
            tdats.append(tdat)
        return (tdats, p)
    def _parse_tkey_array(sf, tkey, ctx, position_info, tokens, /):
        'tkey -> ctx -> position_info -> PeekableIterator token -> ([tdat], position_info)'
        prev_p = position_info
        tdats = []
        while not tokens.is_empty():
            tkn = tokens.head
            (prev_p, (_tkey, tdat), p) = tkn
            if not _tkey == tkey:
                #raise ParseFail__expected_tkey(tkey, tkn)
                break
            tokens.read1()
            tdats.append(tdat)
            prev_p = p
        return (tdats, prev_p)
    def _parse_xxx_between(sf, tkey8open, tkey8end, _parse_xxx, ctx, position_info, tokens, /):
        'tkey -> tkey -> (ctx -> position_info -> PeekableIterator token -> (xxx, position_info)) -> ctx -> position_info -> PeekableIterator token -> ((tdat, IRegexRepr, tdat), position_info)'
        p = position_info
        [tdat6open], p = sf._parse_constant_tkeys([tkey8open], ctx, p, tokens)
        xxx, p = _parse_xxx(ctx, p, tokens)
        [tdat6end], p = sf._parse_constant_tkeys([tkey8end], ctx, p, tokens)
        return (tdat6open, xxx, tdat6end), p
    def _parse_xxx_array_sepby_endby_tkey(sf, tkey8sep, tkey8end, _parse_xxx, ctx, position_info, tokens, /):
        'tkey -> tkey -> (ctx -> position_info -> PeekableIterator token -> (xxx, position_info)) -> ctx -> position_info -> PeekableIterator token -> ([xxx], tdat, position_info)'
        p = position_info
        ls = []
        while 1:
            tkn = sf._peek1(p, tokens)
            (prev_p, (_tkey, tdat6end), p) = tkn
            if _tkey == tkey8end:
                tokens.read1()
                break
            if ls:
                [tdat6sep], prev_p = sf._parse_constant_tkeys([tkey8sep], ctx, prev_p, tokens)
            xxx, p = _parse_xxx(ctx, prev_p, tokens)
            ls.append(xxx)
        return (ls, tdat6end, p)
    def _parse_xxx_array_endby_tkey(sf, tkey8end, _parse_xxx, ctx, position_info, tokens, /):
        'tkey -> (ctx -> position_info -> PeekableIterator token -> (xxx, position_info)) -> ctx -> position_info -> PeekableIterator token -> ([xxx], tdat, position_info)'
        p = position_info
        ls = []
        while 1:
            tkn = sf._peek1(p, tokens)
            (prev_p, (_tkey, tdat), p) = tkn
            if _tkey == tkey8end:
                tokens.read1()
                break
            xxx, p = _parse_xxx(ctx, prev_p, tokens)
            ls.append(xxx)
        return (ls, tdat, p)

    #see:_4parse_atomic_regex
        #see:_4parse_charset
    _4parse_atomic_regex__excluded_charset = (
    {'char':'_parse_atomic_regex__char'
    ,'{;':'_parse_atomic_regex__def'
    #,:'_parse_atomic_regex__ref'
    ,'&:[]':'_parse_atomic_regex__ref_usr'
    ,'&%[]':'_parse_atomic_regex__ref_std'
    #,:'_parse_atomic_regex__charset'
        #see:_4parse_charset
    ,'[|':'_parse_atomic_regex__alternation'
    #,:'_parse_atomic_regex__array'
    ,'[*,':'_parse_atomic_regex__array_many0'
    ,'[+,':'_parse_atomic_regex__array_many1'
    ,'[?,':'_parse_atomic_regex__array_optional'
    ,'[[:],':'_parse_atomic_regex__array_min_oomax'
    ,'$^':'_parse_atomic_regex__color'
    })
    def _parse_atomic_regex(sf, ctx, position_info, tokens, /):
        'ctx -> position_info -> PeekableIterator token -> (IRegexRepr, position_info)'
        check_type_is(PeekableIterator, tokens)
        #顽式
        tkey2nm = sf._4parse_atomic_regex
        (regex_repr, p) = sf._switch(tkey2nm, ctx, position_info, tokens)
        check_type_le(IRegexRepr, regex_repr)
        return regex_repr, p
    def _parse_atomic_regex__char(sf, ctx, position_info, tokens, /):
        'ctx -> position_info -> PeekableIterator token -> (IRegexRepr, position_info)'
        #普通字符
        [tdat], p = sf._parse_constant_tkeys(['char'], ctx, position_info, tokens)
        char = tdat['char']
        regex_repr = hollow_regex / empty_set_repr[:char:]
        return regex_repr, p
    def _parse_atomic_regex__def(sf, ctx, position_info, tokens, /):
        'ctx -> position_info -> PeekableIterator token -> (IRegexRepr, position_info)'
        #变量定义
        _, position_info = sf._parse_constant_tkeys(['{;'], ctx, position_info, tokens)
        named_ls, tdat6end, p = sf._parse_xxx_array_endby_tkey(';}', sf._parse_def_stmt, ctx, position_info, tokens)
        for (is_regex, name, set_repr_or_regex_repr) in named_ls:
            if is_regex:
                regex_repr = set_repr_or_regex_repr
                check_type_le(IRegexRepr, regex_repr)
            else:
                set_repr = set_repr_or_regex_repr
                check_type_le(ISetRepr_IntervalBased, set_repr)
            xnm = f'[{name}]' if is_regex else f'{{{name}}}'
            ctx[xnm] = set_repr_or_regex_repr
        ctx
        regex_repr = hollow_regex
        return regex_repr, p
    def _parse_atomic_regex__ref(sf, ctx, position_info, tokens, /):
        'ctx -> position_info -> PeekableIterator token -> (IRegexRepr, position_info)'
        #正则表达式变量引用
        raise NotImplementedError
    def _parse_atomic_regex__ref_usr(sf, ctx, position_info, tokens, /):
        'ctx -> position_info -> PeekableIterator token -> (IRegexRepr, position_info)'
        #自定义正则表达式变量引用
        [tdat], p = sf._parse_constant_tkeys(['&:[]'], ctx, position_info, tokens)
        nm = tdat['name']
        regex_repr = ctx[f'[{nm}]']
        check_type_le(IRegexRepr, regex_repr)
        return regex_repr, p
    def _parse_atomic_regex__ref_std(sf, ctx, position_info, tokens, /):
        'ctx -> position_info -> PeekableIterator token -> (IRegexRepr, position_info)'
        #内置正则表达式变量引用
        [tdat], p = sf._parse_constant_tkeys(['&%[]'], ctx, position_info, tokens)
        nm = tdat['name']
        regex_repr = sf._gctx[f'[{nm}]']
        check_type_le(IRegexRepr, regex_repr)
        return regex_repr, p
    def _parse_atomic_regex__charset(sf, ctx, position_info, tokens, /):
        'ctx -> position_info -> PeekableIterator token -> (IRegexRepr, position_info)'
        #字符集合
        set_repr, p = sf._parse_charset(ctx, position_info, tokens)
        regex_repr = hollow_regex / set_repr
        return regex_repr, p
    def _parse_atomic_regex__alternation(sf, ctx, position_info, tokens, /):
        'ctx -> position_info -> PeekableIterator token -> (IRegexRepr, position_info)'
        #并式
        _, position_info = sf._parse_constant_tkeys(['[|'], ctx, position_info, tokens)
        regex_reprs, tdat6end, p = sf._parse_xxx_array_sepby_endby_tkey('|', '|]', sf._parse_regex, ctx, position_info, tokens)
        #regex_repr = RegexRepr_Alternation(regex_reprs)
        regex_repr = dead_regex
        for r in regex_reprs:
            regex_repr |= r
        return regex_repr, p
    def _parse_atomic_regex__array(sf, ctx, position_info, tokens, /):
        'ctx -> position_info -> PeekableIterator token -> (IRegexRepr, position_info)'
        #复式
        raise NotImplementedError
    def _parse_atomic_regex__array_many0(sf, ctx, position_info, tokens, /):
        'ctx -> position_info -> PeekableIterator token -> (IRegexRepr, position_info)'
        #复式
        (tdat6open, regex_repr, tdat6end), p = sf._parse_xxx_between('[*,', ',*]', sf._parse_regex, ctx, position_info, tokens)
        regex_repr = regex_repr[0:]
        return regex_repr, p
    def _parse_atomic_regex__array_many1(sf, ctx, position_info, tokens, /):
        'ctx -> position_info -> PeekableIterator token -> (IRegexRepr, position_info)'
        #复式
        (tdat6open, regex_repr, tdat6end), p = sf._parse_xxx_between('[+,', ',+]', sf._parse_regex, ctx, position_info, tokens)
        regex_repr = regex_repr[1:]
        return regex_repr, p
    def _parse_atomic_regex__array_optional(sf, ctx, position_info, tokens, /):
        'ctx -> position_info -> PeekableIterator token -> (IRegexRepr, position_info)'
        #复式
        (tdat6open, regex_repr, tdat6end), p = sf._parse_xxx_between('[?,', ',?]', sf._parse_regex, ctx, position_info, tokens)
        regex_repr = regex_repr[0:1]
        return regex_repr, p
    def _parse_atomic_regex__array_min_oomax(sf, ctx, position_info, tokens, /):
        'ctx -> position_info -> PeekableIterator token -> (IRegexRepr, position_info)'
        #复式
        (tdat6open, regex_repr, tdat6end), p = sf._parse_xxx_between('[[:],', ',[:]]', sf._parse_regex, ctx, position_info, tokens)
        match tdat6open:
            case {'min':min, 'may_max':may_max}:
                pass
            case _:
                raise 000
        regex_repr = regex_repr[min:may_max]
        return regex_repr, p
    def _parse_atomic_regex__color(sf, ctx, position_info, tokens, /):
        'ctx -> position_info -> PeekableIterator token -> (IRegexRepr, position_info)'
        #终态着色式
        [tdat], p = sf._parse_constant_tkeys(['$^'], ctx, position_info, tokens)
        color = tdat['color']
        regex_repr = hollow_regex % color
        return regex_repr, p
    _4parse_def_stmt = (
    {';[]=':'_parse_def_stmt__regex'
    ,';{}=':'_parse_def_stmt__charset'
    })
    def _parse_def_stmt(sf, ctx, position_info, tokens, /):
        'ctx -> position_info -> PeekableIterator token -> ((is_regex, name, (set_repr|regex_repr)), position_info)'
        #定义式
        tkey2nm = sf._4parse_def_stmt
        (xxx, p) = sf._switch(tkey2nm, ctx, position_info, tokens)
        return (xxx, p)
    def _parse_def_stmt__regex(sf, ctx, position_info, tokens, /):
        'ctx -> position_info -> PeekableIterator token -> ((is_regex, name, (set_repr|regex_repr)), position_info)'
        # 正则表达式定义式
        [tdat], position_info = sf._parse_constant_tkeys([';[]='], ctx, position_info, tokens)
        regex_repr, p = sf._parse_regex(ctx, position_info, tokens, non_eof_ok=True)
        name = tdat['name']
        return (is_regex:=True, name, regex_repr), p
    def _parse_def_stmt__charset(sf, ctx, position_info, tokens, /):
        'ctx -> position_info -> PeekableIterator token -> ((is_regex, name, (set_repr|regex_repr)), position_info)'
        # 字集定义式
        [tdat], position_info = sf._parse_constant_tkeys([';{}='], ctx, position_info, tokens)
        set_repr, p = sf._parse_charset(ctx, position_info, tokens)
        name = tdat['name']
        return (is_regex:=False, name, set_repr), p

    _4parse_charset = (
    {'&:{}':'_parse_charset_ref_usr'
    ,'&%{}':'_parse_charset_ref_std'
    ,'&@.=':'_parse_charset_ref_unicode_property'
    ,'{~':'_parse_charset_interval'
    ,'{.|':'_parse_charset_chars'
    ,'{|':'_parse_charset_union'
    ,'{&':'_parse_charset_intersection'
    ,'{-':'_parse_charset_diff'
    ,'{%-':'_parse_charset_complement'
    ,'{%}':'_parse_charset_whole'
    })
    _4parse_atomic_regex = {**{k:'_parse_atomic_regex__charset' for k,_ in _4parse_charset.items()}, **_4parse_atomic_regex__excluded_charset}
        #see:_4parse_charset
        #see:_4parse_atomic_regex__excluded_charset
    def _parse_charset(sf, ctx, position_info, tokens, /):
        'ctx -> position_info -> PeekableIterator token -> (ISetRepr_IntervalBased, position_info)'
        check_type_is(PeekableIterator, tokens)
        #字符集合
        tkey2nm = sf._4parse_charset
        (set_repr, p) = sf._switch(tkey2nm, ctx, position_info, tokens)
        check_type_le(ISetRepr_IntervalBased, set_repr)
        return set_repr, p

    def _parse_charset_ref(sf, ctx, position_info, tokens, /):
        'ctx -> position_info -> PeekableIterator token -> (ISetRepr_IntervalBased, position_info)'
        #字集变量引用
        #{'&:{}', '&%{}', '&@.='}
        raise NotImplementedError
    def _parse_charset_ref_usr(sf, ctx, position_info, tokens, /):
        'ctx -> position_info -> PeekableIterator token -> (ISetRepr_IntervalBased, position_info)'
        #自定义字集变量引用
        #{'&:{}'}
        [tdat], p = sf._parse_constant_tkeys(['&:{}'], ctx, position_info, tokens)
        nm = tdat['name']
        set_repr = ctx[f'{{{nm}}}']
        check_type_le(ISetRepr_IntervalBased, set_repr)
        return set_repr, p
    def _parse_charset_ref_std(sf, ctx, position_info, tokens, /):
        'ctx -> position_info -> PeekableIterator token -> (ISetRepr_IntervalBased, position_info)'
        #内置字集变量引用
        #{'&%{}'}
        [tdat], p = sf._parse_constant_tkeys(['&%{}'], ctx, position_info, tokens)
        nm = tdat['name']
        set_repr = sf._gctx[f'{{{nm}}}']
        check_type_le(ISetRepr_IntervalBased, set_repr)
        return set_repr, p
    def _parse_charset_ref_unicode_property(sf, ctx, position_info, tokens, /):
        'ctx -> position_info -> PeekableIterator token -> (ISetRepr_IntervalBased, position_info)'
        #统合码属性字集引用
        #{'&@.='}
        [tdat], p = sf._parse_constant_tkeys(['&@.='], ctx, position_info, tokens)
        match tdat:
            case {'unicode_version':unicode_version, 'property_name':property_name, 'property_value':property_value}:
                pass
            case _:
                raise 000
        set_repr = SetRepr_5Unicode_property(unicode_version, property_name, property_value)
        return set_repr, p
    def _parse_charset_interval(sf, ctx, position_info, tokens, /):
        'ctx -> position_info -> PeekableIterator token -> (ISetRepr_IntervalBased, position_info)'
        #区间
        #{'{~'}
        tdats, p = sf._parse_constant_tkeys(['{~', 'char', 'char', '~}'], ctx, position_info, tokens)
        match tdats:
            case [{}, {'char':char8min}, {'char':char8max}, {}]:
                pass
            case _:
                raise 000
        set_repr = empty_set_repr[char8min::char8max]
        return set_repr, p
    def _parse_charset_chars(sf, ctx, position_info, tokens, /):
        'ctx -> position_info -> PeekableIterator token -> (ISetRepr_IntervalBased, position_info)'
        #枚举字集
        #{'{.|'}
        _, position_info = sf._parse_constant_tkeys(['{.|'], ctx, position_info, tokens)
        tdats, position_info = sf._parse_tkey_array('char', ctx, position_info, tokens)
        _, position_info = sf._parse_constant_tkeys(['|.}'], ctx, position_info, tokens)
        s = ''.join(tdat['char'] for tdat in tdats)
        set_repr = SetRepr_5Intervals(map(Solo, s))
        return set_repr, position_info
    def _parse_charset_union(sf, ctx, position_info, tokens, /):
        'ctx -> position_info -> PeekableIterator token -> (ISetRepr_IntervalBased, position_info)'
        #并集
        #{'{|'}
        _, position_info = sf._parse_constant_tkeys(['{|'], ctx, position_info, tokens)
        set_reprs, tdat6end, p = sf._parse_xxx_array_endby_tkey('|}', sf._parse_charset, ctx, position_info, tokens)
        set_repr = SetRepr_Union(set_reprs)
        return set_repr, p
    def _parse_charset_intersection(sf, ctx, position_info, tokens, /):
        'ctx -> position_info -> PeekableIterator token -> (ISetRepr_IntervalBased, position_info)'
        #交集
        #{'{&'}
        _, position_info = sf._parse_constant_tkeys(['{&'], ctx, position_info, tokens)
        set_reprs, tdat6end, p = sf._parse_xxx_array_endby_tkey('&}', sf._parse_charset, ctx, position_info, tokens)
        set_repr = SetRepr_Intersection(set_reprs)
        return set_repr, p
    def _parse_charset_diff(sf, ctx, position_info, tokens, /):
        'ctx -> position_info -> PeekableIterator token -> (ISetRepr_IntervalBased, position_info)'
        #差集
        #{'{-'}
        _, position_info = sf._parse_constant_tkeys(['{-'], ctx, position_info, tokens)
        s0, position_info = sf._parse_charset(ctx, position_info, tokens)
        s1, position_info = sf._parse_charset(ctx, position_info, tokens)
        set_reprs, tdat6end, p = sf._parse_xxx_array_endby_tkey('-}', sf._parse_charset, ctx, position_info, tokens)
        s2 = SetRepr_Union(chain([s1], set_reprs)) if set_reprs else s1
        set_repr = SetRepr_Diff(s0, s2)
        return set_repr, p

    def _parse_charset_complement(sf, ctx, position_info, tokens, /):
        'ctx -> position_info -> PeekableIterator token -> (ISetRepr_IntervalBased, position_info)'
        #补集
        #{'{%-'}
        _, position_info = sf._parse_constant_tkeys(['{%-'], ctx, position_info, tokens)
        set_reprs, tdat6end, p = sf._parse_xxx_array_endby_tkey('-%}', sf._parse_charset, ctx, position_info, tokens)
        set_repr = SetRepr_Union(set_reprs)
        set_repr = SetRepr_Negation(set_repr)
        return set_repr, p
    def _parse_charset_whole(sf, ctx, position_info, tokens, /):
        'ctx -> position_info -> PeekableIterator token -> (ISetRepr_IntervalBased, position_info)'
        #全集
        #{'{%}'}
        _, p = sf._parse_constant_tkeys(['{%}'], ctx, position_info, tokens)
        return whole_set_repr, p
#end-class Parser4RegexLiteral:
parser4RegexLiteral__no_builtins = Parser4RegexLiteral({})
parser4RegexLiteral__with_2x2_builtins = Parser4RegexLiteral({'{empty_set_repr}':empty_set_repr, '{whole_set_repr}':whole_set_repr, '[hollow_regex]':hollow_regex, '[dead_regex]':dead_regex})
__all__

def mk_positioned_chars5text(position_info, text, /):
    '(lineno, columno) -> Iter char -> positioned_chars'
    check_pair(position_info)
    (lineno, columno) = position_info
    check_type_is(int, lineno)
    check_type_is(int, columno)
    it = echo_or_mk_PeekableIterator(text)
    #_4newline
    for ch in it:
        if ch == '\r':
            if not it.is_empty() and it.head == '\n':
                next(it)
            ch = '\n'
        #####
        if ch == '\n':
            lineno += 1
            columno = 0 #<<==newline.end_position_info
        else:
            columno += 1
        yield ch, (lineno, columno)
def mk_positioned_chars5str(position_info, s, /):
    'idx -> Iter char -> positioned_chars'
    check_type_is(int, position_info)
    j = position_info
    it = ((c,j) for j,c in enumerate(s, 1+j))
    return it

class _Raw:
    def __init__(sf, tkn, /):
        sf.tkn = tkn
class Tokenizer4RegexLiteral:
    r'''[[[
    LL1
    [positioned_chars :: Iter (char, position_info)]
    [token :: (position_info, (tkey/str, tdat/dict), position_info)]
    #]]]'''#'''
    _to_output_comment_ = False
    def tokenize__text(sf, text, position_info=(1,1), /):
        positioned_chars = mk_positioned_chars5text(position_info, text)
        return sf.tokenize(position_info, positioned_chars)
    def tokenize__str(sf, s, position_info=0, /):
        positioned_chars = mk_positioned_chars5str(position_info, s)
        return sf.tokenize(position_info, positioned_chars)
    def tokenize(sf, position_info, positioned_chars, /):
        'position_info -> Iter (char, position_info) -> Iter token/(position_info, (tkey/str, tdat/dict), position_info)' ' #return-end_position_info'
        positioned_maychars = sf.preprocess(positioned_chars)
        return sf._tokenize(position_info, positioned_maychars, meta_char_ok=True)
    def _tokenize(sf, position_info, positioned_maychars, /, *, meta_char_ok):
        'position_info -> Iter (may char, position_info) -> Iter token/(position_info, (tkey/str, tdat/dict), position_info)' ' #return-end_position_info'
        prev_p = position_info
        it = iter(positioned_maychars)
        to_mark_raw_char = not meta_char_ok
        if to_mark_raw_char:
            def mark(tkn, /):
                return _Raw(tkn)
        else:
            mark = echo
        mark
        for m, p in it:
            if m is None:
                prev_p = yield from sf.on_escape_seq(p, it, meta_char_ok=meta_char_ok)
                continue
            ch = m
            yield mark(sf.mk_token4char(prev_p, ch, p))
            prev_p = p
        return (end_position_info := prev_p)
    def on_escape_seq(sf, position_info, positioned_maychars, /, *, meta_char_ok):
        'position_info -> Iter (may char, position_info) -> Iter token | ^BadFormat__... | ^BadFormat__eof' ' #return-end_position_info'
        it = iter(positioned_maychars)
        #prev_p = position_info
        (m, p) = sf._read1(position_info, it)
            # ^BadFormat__eof
        if m is None:
            raise BadFormat__esc_esc(p)
        ch = m
        if ch == '(':
            if not meta_char_ok:
                raise BadFormat__forbid_mata_char(position_info)
            _it = sf.iter_meta_char_tokens5payload(p, it)
        elif ch == '[':
            _it = sf.iter_escaped_char_tokens5long_payload(p, it)
        else:
            _it = sf.iter_escaped_char_tokens5single_char_payload(position_info, ch, p)
        return _it  #return-end_position_info

    def _read1(sf, prev_p, it, /):
        for x in it:
            return x
        raise BadFormat__eof(prev_p)
    def iter_meta_char_tokens5payload(sf, prev_p, it, /):
        ''
        ' #return-end_position_info'
        sf._greedy_reads_ex
        (s, _prev_p, item, it) = sf._greedy_reads_ex(#(
                ')'.__ne__, prev_p, it)
        (m, p) = item
        #(
        assert m == ')'
        yield sf.mk_token4meta_char(prev_p, s, _prev_p)
        prev_p = p
        return (end_position_info := prev_p)
    def iter_comment_tokens5long_payload(sf, prev_p, it, /):
        ''
        ' #return-end_position_info'
        p0 = prev_p
        p = prev_p
        b = sf._to_output_comment_
        if b:
            ss = []
        ch_ = ''
        for tkn in sf._tokenize(prev_p, it, meta_char_ok=False):
            is_raw = type(tkn) is _Raw
            if is_raw:
                raw = tkn
                tkn = raw.tkn
            tkn, is_raw
            (prev_p, (tkey, tdat), p) = tkn
            if not tkey in 'char comment':raise Exception(tkey)
            if is_raw:
                if not tkey == 'char':raise Exception(tkey)
                ch = tdat['char']
                if ch == '#':
                    ch_ = '#'
                elif ch == ']':
                    if ch_ == '#':
                        break
                else:
                    ch_ = ''
            else:
                ch_ = ''

            if not b:
                continue
            if tkey == 'char':
                ch = tdat['char']
                ss.append(ch)
            elif tkey == 'comment':
                s = tdat['comment']
                ss.append('?![#')
                ss.append(s)
                ss.append('#]')
            else:
                raise 000
        else:
            raise BadFormat__eof(p)
        assert is_raw
        assert ch == ']'
        assert ch_ == '#'
        if b:
            assert ss
            assert ss[-1] == '#'
            ss.pop()
            def __(ss, /):
                if ss:
                    yield ss[0]
                for a, b in pairwise(ss):
                    yield b
                    if a == '?' and b == '!':
                        yield '.'
            comment = ''.join(__(ss))
            yield sf.mk_token4comment(p0, comment, p)
        return (end_position_info:=p)
    def iter_escaped_char_tokens5long_payload(sf, prev_p, it, /):
        ''
        ' #return-end_position_info'
        (m, p) = sf._read1(prev_p, it)
            # ^BadFormat__eof
        if m == '#':
            prev_p = p
            prev_p = yield from sf.iter_comment_tokens5long_payload(prev_p, it)
            return (end_position_info := prev_p)
            ######################
            ########old:
            try:
                for m, p in _4suffix4comment.iter_until_end_marker(it, key=fst, eof_ok=False):
                    # ^BadFormat__eof
                    if m is None:
                        raise BadFormat__forbid_esc_inside_escaped_chars(prev_p, p)
                    prev_p = p
            except BadFormat__eof:
                raise BadFormat__eof(prev_p)

            return (end_position_info := prev_p)

        while 1:
            prev_p, (m, p), it
            if m is None:
                raise BadFormat__forbid_esc_inside_escaped_chars(prev_p, p)
            ch = m
            if ch == ']':
                prev_p = p
                break
            if ch in _4single:
                yield from sf.iter_escaped_char_tokens5single_char_payload(prev_p, ch, p)
                prev_p = p
                (m, p) = item = sf._read1(prev_p, it)
                prev_p, (m, p), it
                continue
            if not ch in '+@':
                raise BadFormat__unknown_char_esc_fmt(prev_p, ch, p)
            (s, _prev_p, item, it) = sf._greedy_reads_ex(lambda c:c=='_' or c.isalnum(), p, it)
                #str.isidentifier
                #str.isalnum
                # ^BadFormat__eof...
            if not s:
                raise BadFormat__char_esc_fmt(prev_p, ch, p, s, _prev_p)
            try:
                if ch == '+':
                    _ch = chr(int(s, 16))
                elif ch == '@':
                    _ch = _nm2ch(s)
                else:
                    raise 000
            except Exception:
                raise BadFormat__char_esc_fmt(prev_p, ch, p, s, _prev_p)
            _ch
            # ((ch, p), s) --> _ch
            # (prev_p, (ch, p), s, _prev_p, item, it)
            # --> (prev_p, _ch, _prev_p, item, it)
            yield sf.mk_token4char(prev_p, _ch, _prev_p)
            prev_p = _prev_p
            (m, p) = item
            ##777;    next(it)
            prev_p, (m, p), it
        return (end_position_info := prev_p)
    def _greedy_reads_ex(sf, char2ok_, prev_p, it, /):
        '-> (str, prev_p, item, it)'
        cs = []
        while 1:
            (m, p) = x = sf._read1(prev_p, it)
                # ^BadFormat__eof
            m, p = x
            if m is None:
                raise BadFormat__unexpected_esc(prev_p, p)
            ch = m
            if not char2ok_(ch):
                cs = ''.join(cs)
                return (cs, prev_p, x, it)
            cs.append(ch)
            prev_p = p


    def iter_escaped_char_tokens5single_char_payload(sf, prev_p, ch, p, /):
        ''
        ' #return-end_position_info'
        try:
            txt = _4single[ch]
        except KeyError:
            raise BadFormat__unknown_single_char_payload(p, ch)
        for _ch in txt:
            yield sf.mk_token4char(prev_p, _ch, p)
            prev_p = p
        prev_p = p
        return (end_position_info := prev_p)

    def mk_token4meta_char(sf, begin_position_info, s, end_position_info, /):
        if s in _tkeys__no_params:
            return sf.mk_token(begin_position_info, s, end_position_info)
        #_tkeys__with_params
        m = _rex4meta_char.fullmatch(s)
        if not m:
            raise BadFormat__unknown_meta_char_payload(begin_position_info, s, end_position_info)
        d = {k:v for k, v in m.groupdict().items() if v is not None}
        for attr in d:
            break
        else:
            raise 000
        tkey = _attr2tkey4meta_char[attr]
        if attr.endswith('ef'):
            assert len(d) == 1
            #d['name'] = d[attr]
            d = dict(name = d[attr])
        else:
            assert len(d) > 1 or attr == 'color'
        if tkey == '[[:],': #]
            min = d['min']
            may_max = d['may_max']
            d = (dict
                (min = int(min) if min else 0
                ,may_max = int(may_max) if may_max else None
                ))
        tdat = d

        #tdat = None
        #match s[0]:
        #    case '$':
        #        match s[:2]:
        #            case '$^':
        #               m['color']
        #    case '[':#]
        #    case ';':
        #        match s[:2]:
        #            case ';[':#]
        #            case ';{':#}
        #    case '&':
        #        if s[:2] == '&@':
        #        match s[:3]:
        #            case '&:[':#]
        #            case '&%[':#]
        #            case '&:{':#}
        #            case '&%{':#}
        #if tdat is None:
        #    raise 000

        return sf.mk_token(begin_position_info, tkey, end_position_info, **tdat)
    def mk_token4comment(sf, begin_position_info, comment, end_position_info, /):
        return sf.mk_token(begin_position_info, 'comment', end_position_info, comment=comment)
    def mk_token4char(sf, begin_position_info, char, end_position_info, /):
        return sf.mk_token(begin_position_info, 'char', end_position_info, char=char)
    def mk_token(sf, begin_position_info, tkey, end_position_info, /, **tdat):
        '-> token/(position_info, (tkey/str, tdat/dict), position_info)'
        check_type_is(str, tkey)
        return (begin_position_info, (tkey, tdat), end_position_info)
    def preprocess(sf, positioned_chars, /):
        'Iter (char, position_info) -> Iter (may char, position_info)'
        positioned_chars = sf.denoise(positioned_chars)
        positioned_maychars = sf.cut(positioned_chars)
        return positioned_maychars
    def cut(sf, positioned_chars, /):
        'Iter (char, position_info) -> Iter (may char, position_info)'
        it = iter(positioned_chars)
        f = _4prefix.iter_until_end_marker
        while 1:
            may_prefix = yield from f(it, key=fst, eof_ok=True)
            if may_prefix:
                # '?!' --> (None, p)
                prefix = may_prefix
                match prefix:
                    case [('?', _), ('!', p)]:
                        pass
                    case _:
                        raise 000
                yield None, p
            else:
                # None @eof
                assert may_prefix is None
                break
        return
        ######################
    def denoise(sf, positioned_chars, /):
        'Iter (char, position_info) -> Iter (char, position_info)'
        for (ch, p) in positioned_chars:
            if not ch.isspace():
                yield (ch, p)


_4single = (
{'.':'?!'
,'-':' '
,':':'\r'
,';':'\n'
,',':'\t'
})
#end-class Tokenizer4RegexLiteral:
class Tokenizer4RegexLiteral__with_comment(Tokenizer4RegexLiteral):
    #@override
    _to_output_comment_ = True
tokenizer4RegexLiteral = Tokenizer4RegexLiteral()
tokenizer4RegexLiteral__with_comment = Tokenizer4RegexLiteral__with_comment()

__all__
class IterUntilEndMarker:
    def __init__(sf, end_marker, /):
        if not end_marker:raise ValueError
        if end_marker[0] in end_marker[1:]:raise ValueError
        sf._ls = end_marker
    def iter_until_end_marker(sf, iterable, /, *, key=None, eof_ok=False):
        'Iter x -> (Iter x){return-may [x]~=~end_marker}'
        key = ifNone(key, echo)
        ls = sf._ls
        sz = len(ls)
        prevs = []
        assert sz
        for x in iterable:
            #assert sz
            #assert sz + len(prevs) == len(ls)
            k = key(x)
            if k == ls[len(prevs)]:
                prevs.append(x)
                sz -= 1
                if not sz:
                    #assert len(prevs) == len(ls)
                    return prevs
                continue
            if prevs:
                #flush
                yield from prevs
                prevs.clear()
                sz = len(ls)
            #assert not prevs
            yield x
        else:
            #eof
            #assert sz
            if prevs:
                #flush
                yield from prevs
                prevs.clear()
            #assert not prevs
        #assert not prevs
        #assert sz
        if not eof_ok:
            raise BadFormat__eof
        return None
#end-class IterUntilEndMarker:
__all__

_4newline = IterUntilEndMarker('\r\n')
_4prefix = IterUntilEndMarker('?!')
# [#
_4suffix4comment = IterUntilEndMarker('#]')

_tkeys__no_params = (
#'[,'
#',]'
{'[|'
,'|]'
,'{|'
,'|}'
,'{&'
,'&}'
,'{-'
,'-}'
,'{~'
,'~}'
,'{;'
,';}'
#
#
,'[*,'
,',*]'
,'[+,'
,',+]'
,'[?,'
,',?]'
,'{%-'
,'-%}'
,'{%}'
,'{.|'
,'|.}'
#
#
,'|'
    #[
,',[:]]'
})

_tkeys__with_params = (
#except:'char'
#total:9:contains params:
{'$^'
,'&@.='
,'&:[]'
,'&%[]'
,'&:{}'
,'&%{}'
,';[]='
,';{}='
,'[[:],' #]
})

_attr2tkey4meta_char = (dict
(color='$^'

,unicode_version='&@.='
,property_name='&@.='
,property_value='&@.='

,usr_regex_nm_ref='&:[]'
,std_regex_nm_ref='&%[]'
,usr_charset_nm_ref='&:{}'
,std_charset_nm_ref='&%{}'

,usr_regex_nm_def=';[]='
,usr_charset_nm_def=';{}='

,min='[[:],' #]
,may_max='[[:],' #]
))
_rex4meta_char = re.compile(r'''(?x)#verbose:
  \$\^ (?P<color>\w+)
        #$^ [^()]+

| &@ (?P<unicode_version>\w+)
    \. (?P<property_name>\w+)
    = (?P<property_value>\w+)

| &:\[  (?P<usr_regex_nm_ref>\w+) \]
| &%\[  (?P<std_regex_nm_ref>\w+) \]
| &:\{  (?P<usr_charset_nm_ref>\w+) \}
| &%\{  (?P<std_charset_nm_ref>\w+) \}
| ;\[  (?P<usr_regex_nm_def>\w+) \]=
| ;\{  (?P<usr_charset_nm_def>\w+) \}=

| \[\[  (?P<min>\d*) :  (?P<may_max>\d*) \],
    #]

'''#'''
)


__all__
#[[[
##import re
##
##
###from seed.seq_tools.avoid_substrs import strings2prefix_st_tree_ex_
##
##from seed.seq_tools.mk_prefix_tree import mk_prefix_tree, update4prefix_tree, lookup4prefix_tree, lookup_longest_prefix4prefix_tree, iter_lookup_prefix4prefix_tree
##from seed.seq_tools.mk_prefix_tree import view_seq____not_seq_eq_hash, view_seq____seq_eq_hash
##
##
##from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
##_rex4sp = re.compile(r'\s+')
##def dry_(raw_txt, /):
##    dry_txt = _rex4sp.sub('', raw_txt)
##    return dry_txt
##
##def is_anti_bifix__simple_mode(s, /):
##    assert s
##    assert not s[0] in s[1:]
##    assert not s[-1] in s[:-1]
##    assert s == dry_(s)
##class IParser4RegexLiteral(ABC):
##class IParser(ABC):
##    __slots__ = ()
##    def validate(sf, /):
##        s = sf.prefix4escape_seq
##        assert is_anti_bifix__simple_mode(s)
##
##        s1 = sf.chars4single_char_op
##        assert s1 == dry_(s1)
##        assert not s[0] in s1
##        assert len(s1) == len(set(s1))
##        assert is_anti_bifix__simple_mode(s1)
##
##        d = sf.op_prefix2suffix
##        for op_prefix0, op_prefix1 in pairwise(sorted(d)):
##            assert not op_prefix1.startswith(op_prefix0)
##        for op_prefix, op_suffix in d.items():
##            assert op_prefix
##            assert op_suffix
##            assert not op_prefix[0] == s[0]
##            assert not op_prefix[0] in s1
##            assert is_anti_bifix__simple_mode(op_suffix)
##
##
##    @property
##    @abstractmethod
##    def prefix4escape_seq(sf, /):
##        '-> str'
##    @property
##    @abstractmethod
##    def chars4single_char_op(sf, /):
##        '-> str'
##    @property
##    @abstractmethod
##    def op_prefix2suffix(sf, /):
##        '-> {str:str}'
##    @cached_property
##    def op_prefix_tree(sf, /):
##        '-> prefix_tree<op_prefix>'
##mk_prefix_tree
##    def preprocess(sf, raw_txt, /):
##        'raw_txt/str -> (header/str, [dry_txt/str]) #ignore_space'
##        dry_txt = dry_(raw_txt)
##        #return dry_txt
##        [header, *ls4dry_txt] = dry_txt.split(sf.prefix4escape_seq)
##        assert not header[:1] == sf.prefix4escape_seq[0]
##        assert all(map(len, ls4dry_txt))
##        assert not any(dry_txt[0] == sf.prefix4escape_seq[0] for dry_txt in ls4dry_txt)
##        return (header, mk_tuple(ls4dry_txt))
##
#]]]


__all__
from seed.recognize.regex.RegexLiteral import Parser4RegexLiteral, parser4RegexLiteral__no_builtins, parser4RegexLiteral__with_2x2_builtins, tokenizer4RegexLiteral, tokenizer4RegexLiteral__with_comment
from seed.recognize.regex.RegexLiteral import *
