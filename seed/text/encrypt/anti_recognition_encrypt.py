#__all__:goto
#TODO:goto
#[:__cmds__]:goto
r'''[[[
e ../../python3_src/seed/text/encrypt/anti_recognition_encrypt.py

加密目的:防搜索，防识别
    ==>>自解密#无需记忆:协议+密钥

[[
TODO:加密-公开-防搜索-区间循环:
  明文->'加密协议-区间表-密码-盐-密文'
  比如:保存 电话
  view ../../python3_src/nn_ns/app/register_xor.py
  [:翻译前缀冫防]:goto
  anti_recognition_encrypt

]]


[validate :: int|bool]
    深度纟校验
    负数<==>+oo
    mk_validate4sub_call_







???明文-->原文
???密文-->矫文

裸vs裹
函-->圅-->裹
.+1,$s/函/圅/g
.+1,$s/圅/裹/g

密钥纟加密-->顺钥
密钥纟解密-->逆钥
明文文本牜外赋协议顺钥-->明文文本牜裸
密文文本牜外赋协议内禀逆钥-->密文文本牜裹
密文文本牜内禀协议逆钥-->密文文本牜裹裹
.+1,$s/牜外赋协议顺钥/牜裸/g
.+1,$s/牜内禀协议逆钥/牜裹/g


[[[
:read !grep 'def .*validate' ../../python3_src/seed/text/encrypt/anti_recognition_encrypt.py | sort -u
.,.+18s/.*def \(\S*\)(.*):/\1
    #补偿:(:
%s/\([.]\(加密冫明文数据牜裸扌\|加密冫明文文本牜裸扌\|加密冫明文文本牜裸裸扌\|加密牜区内加密扌\|区内加密乊孤码扌\|易位扌\|编码冫密文文本牜裹裹扌\|编码冫密文牜裸扌\|编码冫密文牜裹扌\|编码冫密文牜裹牜灬扌\|封装冫负载扌\|编码冫逆钥扌\|脱水编码冫状态乊位次变更扌\|解码冫明文牜裸扌\|解码冫顺钥扌\|转义冫文本扌\)[(].*\)[)]/\1, validate=_validate)
/def \(加密冫明文数据牜裸扌\|加密冫明文文本牜裸扌\|加密冫明文文本牜裸裸扌\|加密牜区内加密扌\|区内加密乊孤码扌\|易位扌\|编码冫密文文本牜裹裹扌\|编码冫密文牜裸扌\|编码冫密文牜裹扌\|编码冫密文牜裹牜灬扌\|封装冫负载扌\|编码冫逆钥扌\|脱水编码冫状态乊位次变更扌\|解码冫明文牜裸扌\|解码冫顺钥扌\|转义冫文本扌\)
===
    def 加密冫明文数据牜裸扌(sf, 顺钥数据, 明文数据牜裸, /, *, validate):
    def 加密冫明文文本牜裸扌(sf, 顺钥文本, 明文文本牜裸, /, *, validate):
    def 加密冫明文文本牜裸裸扌(sf, 匾协议, 顺钥文本, 明文文本牜裸, /, *, validate):
    def 加密牜区内加密扌(sf, 状态乊位次保持, 位号串乊位次保持, /, *, validate):
    def 区内加密乊孤码扌(sf, 序号纟码元匕有效明文, 状态乊位次保持, 位号, /, *, validate):
    def 易位扌(sf, 状态乊位次保持, /, *, validate):
    def 编码冫密文文本牜裹裹扌(sf, 匾协议, 密文文本牜裹, /, *, validate):
    def 编码冫密文牜裸扌(sf, 密文数据牜裸, /, *, validate):
    def 编码冫密文牜裹扌(sf, 密文数据牜裹, /, *, validate):
    def 编码冫密文牜裹牜灬扌(sf, 逆钥文本, 密文文本牜裸, /, *, validate):
    def 封装冫负载扌(sf, 负载, /, *, validate):
    def 编码冫逆钥扌(sf, 逆钥数据, /, *, validate):
    def 脱水编码冫状态乊位次变更扌(sf, 状态乊位次变更, /, *, validate):
    def 解码冫明文牜裸扌(sf, 明文文本牜裸, /, *, validate):
    def 解码冫顺钥扌(sf, 顺钥文本, /, *, validate):
    def 转义冫文本扌(sf, 文本乊转义前, /, *, validate):
]]]






[:__cmds__]:here
py -m seed.text.encrypt.anti_recognition_encrypt
py -m nn_ns.app.debug_cmd   seed.text.encrypt.anti_recognition_encrypt -x
py -m nn_ns.app.doctest_cmd seed.text.encrypt.anti_recognition_encrypt:__doc__ -ht
from seed.text.encrypt.anti_recognition_encrypt import *



py_adhoc_call   seed.text.encrypt.anti_recognition_encrypt   @灬加密冫明文文本牜裸裸扌  --validate=1 :mod_add :19 :6180339887498948482045868343656381177203091798
'mod_add:19:ZV3W0188997DDFBGDIDCHJNMPLNNRRTRXRSZ0WVZX707AA'

py_adhoc_call   seed.text.encrypt.anti_recognition_encrypt   @灬简自解密冫密文文本牜裹裹扌 :mod_add:19:ZV3W0188997DDFBGDIDCHJNMPLNNRRTRXRSZ0WVZX707AA
'6180339887498948482045868343656381177203091798'

py_adhoc_call   seed.text.encrypt.anti_recognition_encrypt   @g_encrypt_  --validate=1 :mod_add :19 :'110 119 114'
'mod_add:19:TUU WX6 Z04'
py_adhoc_call   seed.text.encrypt.anti_recognition_encrypt   @g_self_decrypt__brief_ :'mod_add:19:TUU WX6 Z04'
'110 119 114'

py_adhoc_call   seed.text.encrypt.anti_recognition_encrypt   @g_encrypt_decrypt_  :+ :'110 119 120'
'mod_add:19:TUU WX6 Z10'
py_adhoc_call   seed.text.encrypt.anti_recognition_encrypt   @g_encrypt_decrypt_  :-  :'mod_add:19:TUU WX6 Z10'
'110 119 120'

echo 'py_adhoc_call   seed.text.encrypt.anti_recognition_encrypt   @g_encrypt_decrypt_   "$@"' >>  ../../python3_src/bash_script/app/g_encrypt_decrypt_

g_encrypt_decrypt_  :+ :'110 119 120'
'mod_add:19:TUU WX6 Z10'
g_encrypt_decrypt_  :-  :'mod_add:19:TUU WX6 Z10'
'110 119 120'




灬加密冫明文文本牜裸裸扌
灬自解密冫密文文本牜裹裹扌
灬简自解密冫密文文本牜裹裹扌
>>> _validate = -1
>>> 匾协议 = 'mod_add'
>>> 顺钥文本 = str(2**61 -1)
>>> 明文文本牜裸 = '244:1341 - 0484$#'
>>> 密文文本牜裹裹 = 灬加密冫明文文本牜裸裸扌(匾协议, 顺钥文本, 明文文本牜裸, validate=_validate)
>>> (_匾协议, 逆钥文本, _明文文本牜裸) = 灬自解密冫密文文本牜裹裹扌(密文文本牜裹裹)
>>> _匾协议 == 匾协议
True
>>> _明文文本牜裸 == 明文文本牜裸
True
>>> 逆钥文本 == 顺钥文本
True
>>> 密文文本牜裹裹
'mod_add:2305843009213693951:WZ0:Y131 - 16B8$#'
>>> 顺钥文本
'2305843009213693951'
>>> 灬自解密冫密文文本牜裹裹扌('mod_add:2305843009213693951:WZ0:Y131 - 16B8$#')
('mod_add', '2305843009213693951', '244:1341 - 0484$#')
>>> 灬简自解密冫密文文本牜裹裹扌('mod_add:2305843009213693951:WZ0:Y131 - 16B8$#')
'244:1341 - 0484$#'


>>> 顺钥文本 = '19'
>>> 密文文本牜裹裹 = 灬加密冫明文文本牜裸裸扌(匾协议, 顺钥文本, 明文文本牜裸, validate=_validate)
>>> 密文文本牜裹裹
'mod_add:19:WZ0:Y131 - 16B8$#'

>>> 顺钥文本 = '1'
>>> 密文文本牜裹裹 = 灬加密冫明文文本牜裸裸扌(匾协议, 顺钥文本, 明文文本牜裸, validate=_validate)
>>> 密文文本牜裹裹
'mod_add:1:EHI:GJLJ - JOTQ$#'

>>> 匴加密 = 灬查找扌(匾协议)
>>> 明文有效长度 = 匴加密.统计冫明文有效长度牜文本扌(明文文本牜裸)

>>> 顺钥文本 = str(-明文有效长度)
>>> 密文文本牜裹裹 = 灬加密冫明文文本牜裸裸扌(匾协议, 顺钥文本, 明文文本牜裸, validate=_validate)
>>> 密文文本牜裹裹
'mod_add:-11:256:4797 - 7CHE$#'



匴转义冫文本牜极简具现
匴转义冫超文本牜极简具现
abfnrtv0
>>> 匴转义冫文本牜极简具现.转义冫文本扌('', validate=-1)
''
>>> 匴转义冫文本牜极简具现.转义冫文本扌('abcd \u3000\a\b\f\n\r\t\v\0!?', validate=-1)
'abcd!?-!?=!?a!?b!?f!?n!?r!?t!?v!?0!?.'


>>> 匴转义冫超文本牜极简具现.转义冫超文本扌([], validate=-1)
''

#>>> 匴转义冫超文本牜极简具现.转义冫超文本扌([''], validate=-1)
#''
#>>> 匴转义冫超文本牜极简具现.转义冫超文本扌(['', ()], validate=-1)
#''
#>>> 匴转义冫超文本牜极简具现.转义冫超文本扌(['', ('',)], validate=-1)
#>>> 匴转义冫超文本牜极简具现.转义冫超文本扌(['', ('','')], validate=-1)
#>>> 匴转义冫超文本牜极简具现.转义冫超文本扌(['', ('','','?!x')], validate=-1)
>>> 匴转义冫超文本牜极简具现.转义冫超文本扌(['', ('a',)], validate=-1)
'!?^a'
>>> 匴转义冫超文本牜极简具现.转义冫超文本扌(['', ('aa',)], validate=-1)
'!?^(aa)'
>>> 匴转义冫超文本牜极简具现.转义冫超文本扌(['', ('a','b')], validate=-1)
'!?^(a,b)'
>>> 匴转义冫超文本牜极简具现.转义冫超文本扌(['', ('a','b','?!x')], validate=-1)
'!?^(a,b,?!x)'
>>> 匴转义冫超文本牜极简具现.转义冫超文本扌(['abcd \u3000\a\b\f\n\r\t\v\0!?'], validate=-1)
'abcd!?-!?=!?a!?b!?f!?n!?r!?t!?v!?0!?.'
>>> 匴转义冫超文本牜极简具现.转义冫超文本扌(['abcd \u3000\a\b\f\n\r\t\v\0!?', ('a','b','?!x'), '!?', ('yyy',), '\0', ('zzz','aaa')], validate=-1)
'abcd!?-!?=!?a!?b!?f!?n!?r!?t!?v!?0!?.!?^(a,b,?!x)!?.!?^(yyy)!?0!?^(zzz,aaa)'






>>> 'abcd \u3000\x07\x08\x0c\n\r\t\x0b\x00!?' == 'abcd \u3000\a\b\f\n\r\t\v\0!?'
True
>>> 匴转义冫超文本牜极简具现.还原冫超文本扌('abcd!?-!?=!?a!?b!?f!?n!?r!?t!?v!?0!?.!?^(a,b,?!x)!?.!?^(yyy)!?0!?^(zzz,aaa)')
('abcd \u3000\x07\x08\x0c\n\r\t\x0b\x00!?', ('a', 'b', '?!x'), '!?', ('yyy',), '\x00', ('zzz', 'aaa'))
>>> 匴转义冫超文本牜极简具现.还原冫超文本扌('abcd!?-!?=!?a!?b!?f!?n!?r!?t!?v!?0!?.')
('abcd \u3000\x07\x08\x0c\n\r\t\x0b\x00!?',)
>>> 匴转义冫超文本牜极简具现.还原冫超文本扌('!?^a')
('', ('a',))
>>> 匴转义冫超文本牜极简具现.还原冫超文本扌('!?^(aa)')
('', ('aa',))
>>> 匴转义冫超文本牜极简具现.还原冫超文本扌('!?^(a,b)')
('', ('a', 'b'))
>>> 匴转义冫超文本牜极简具现.还原冫超文本扌('!?^(a,b,?!x)')
('', ('a', 'b', '?!x'))





#]]]'''
__all__ = r'''
g_encrypt_decrypt_
注册处纟加密牜防识别牜文本
    灬注册扌
    灬查找扌
    灬枚举冫匾协议乊已注册扌
    灬加密冫明文文本牜裸裸扌
    灬自解密冫密文文本牜裹裹扌
    灬简自解密冫密文文本牜裹裹扌
    g_register_
    g_lookup_
    g_iter_nms4protocol_
    g_encrypt_
    g_self_decrypt__verbose_
    g_self_decrypt__brief_

匴加密牜防识别牜文本氺自定义数据牜区内变换乊孤码牜恒状态牜模加
乸区位配置牜码元为字符编码点

乸匴转义冫文本牜极简具现
乸匴转义冫超文本牜极简具现
















魖注册处纟加密牜防识别牜文本
    乸注册处纟加密牜防识别牜文本
        注册处纟加密牜防识别牜文本

魖匴加密牜防识别牜自定义数据
    魖匴加密牜防识别牜自定义数据牜区内变换
        魖匴加密牜防识别牜自定义数据牜区内变换乊孤码

魖匴加密牜防识别牜文本
    魖匴加密牜防识别牜文本氺自定义数据
        魖匴加密牜防识别牜文本氺自定义数据牜区内变换
            魖匴加密牜防识别牜文本氺自定义数据牜区内变换乊孤码
                乸匴加密牜防识别牜文本氺自定义数据牜区内变换乊孤码牜恒状态牜模加
                    匴加密牜防识别牜文本氺自定义数据牜区内变换乊孤码牜恒状态牜模加


置换扌
mk_validate4sub_call_

魖区位配置
    乸区位配置牜码元为字符编码点
魖匴转义冫超文本
    乸匴转义冫超文本牜极简具现
        匴转义冫超文本牜极简具现
魖匴转义冫文本
    乸匴转义冫文本牜极简具现
        匴转义冫文本牜极简具现
        匴转义冫用于分隔匾协议

'''.split()#'''
__all__
from itertools import cycle as cycle_

from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.tiny import fst, snd, print_err# echo, chains
from seed.seq_tools.split_tuples import unzip_pairs
from seed.seq_tools.inverse_uint_bijection_array import inverse_uint_bijection_array
from seed.tiny_.check import check_type_is, check_type_le, check_int_ge
#from seed.iters.group_by import group_by

from seed.helper.repr_input import repr_helper

def mk_validate4sub_call_(validate, /):
    r'''[[[
[validate :: int|bool]
    深度纟校验
    负数<==>+oo
    #]]]'''#'''
    check_type_le(int, validate)
    _validate = validate and (-1 if validate < 0 else validate-1)

    return _validate
assert 1 == mk_validate4sub_call_(2)
assert 0 == mk_validate4sub_call_(1)
assert 0 == mk_validate4sub_call_(0)
assert -1 == mk_validate4sub_call_(-1)
assert -1 == mk_validate4sub_call_(-2)

class 魖注册处纟加密牜防识别牜文本(ABC):
    __slots__ = ()
    @abstractmethod
    def 枚举冫匾协议乊已注册扌(sf, /):
        '-> Iter 匾协议/str'
    @abstractmethod
    def 查找扌(sf, 匾协议, /):
        '匾协议/str -> 匴加密/魖匴加密牜防识别牜文本 | ^LookupError'
    @abstractmethod
    def 注册扌(sf, 匴加密, /):
        '匴加密/魖匴加密牜防识别牜文本 -> None'
        匴加密.匾协议
    @abstractmethod
    def 编码冫密文文本牜裹裹扌(sf, 匾协议, 密文文本牜裹, /, *, validate):
        '匾协议 -> 密文文本牜裹 -> 密文文本牜裹裹'
        #格式化
    @abstractmethod
    def 解码冫密文文本牜裹裹扌(sf, 密文文本牜裹裹, /):
        '密文文本牜裹裹 -> (匾协议, 密文文本牜裹)'
        #解析

    def 加密冫明文文本牜裸裸扌(sf, 匾协议, 顺钥文本, 明文文本牜裸, /, *, validate):
        '匾协议/str -> 顺钥文本/str -> 明文文本牜裸/str -> 密文文本牜裹裹/str'
        _validate = mk_validate4sub_call_(validate)
        匴加密 = sf.查找扌(匾协议)
        密文文本牜裹 = 匴加密.加密冫明文文本牜裸扌(顺钥文本, 明文文本牜裸, validate=_validate)
        密文文本牜裹裹 = sf.编码冫密文文本牜裹裹扌(匾协议, 密文文本牜裹, validate=_validate)
        if validate:
            #if not sf.自解密冫密文文本牜裹裹扌(密文文本牜裹裹) == (匾协议, 逆钥文本, 明文文本牜裸):raise Exception((sf, (匾协议, 顺钥文本, 明文文本牜裸), '??逆钥文本', (密文文本牜裹裹)))
            if not sf.自解密冫密文文本牜裹裹扌(密文文本牜裹裹)[0::2] == (匾协议, 明文文本牜裸):raise Exception((sf, (匾协议, 顺钥文本, 明文文本牜裸), (密文文本牜裹裹)))
        return 密文文本牜裹裹
    def 自解密冫密文文本牜裹裹扌(sf, 密文文本牜裹裹, /):
        '密文文本牜裹裹/str -> (匾协议, 逆钥文本, 明文文本牜裸)/(str,str,str)'
        #xxx:不一定有:顺钥文本
        (匾协议, 密文文本牜裹) = sf.解码冫密文文本牜裹裹扌(密文文本牜裹裹)
        匴加密 = sf.查找扌(匾协议)
        (逆钥文本, 明文文本牜裸) = 匴加密.自解密冫密文文本牜裹扌(密文文本牜裹)
        return (匾协议, 逆钥文本, 明文文本牜裸)
    def 简自解密冫密文文本牜裹裹扌(sf, 密文文本牜裹裹, /):
        '密文文本牜裹裹/str -> 明文文本牜裸/str'
        (匾协议, 逆钥文本, 明文文本牜裸) = sf.自解密冫密文文本牜裹裹扌(密文文本牜裹裹)
        return 明文文本牜裸

class 魖匴加密牜防识别牜自定义数据(ABC):
    __slots__ = ()
    @abstractmethod
    def 加密冫明文数据牜裸扌(sf, 顺钥数据, 明文数据牜裸, /, *, validate):
        '顺钥数据/? -> 明文数据牜裸/? -> 密文数据牜裹/(逆钥数据,密文数据牜裸)/(?,?)'
    @abstractmethod
    def 自解密冫密文数据牜裹扌(sf, 密文数据牜裹, /):
        '密文数据牜裹/(逆钥数据,密文数据牜裸)/(?,?) -> (逆钥数据, 明文数据牜裸)/(?,?)'
        #xxx:不一定有:顺钥数据

class 魖匴加密牜防识别牜文本(ABC):
    __slots__ = ()
    @property
    @abstractmethod
    def 匾协议(sf, /):
        '-> 匾协议/str'
    @abstractmethod
    def 加密冫明文文本牜裸扌(sf, 顺钥文本, 明文文本牜裸, /, *, validate):
        '顺钥文本/str -> 明文文本牜裸/str -> 密文文本牜裹/str'
    @abstractmethod
    def 自解密冫密文文本牜裹扌(sf, 密文文本牜裹, /):
        '密文文本牜裹/str -> (逆钥文本, 明文文本牜裸)/(str,str)'
        #xxx:不一定有:顺钥文本

class 魖匴加密牜防识别牜文本氺自定义数据(魖匴加密牜防识别牜文本, 魖匴加密牜防识别牜自定义数据):
    __slots__ = ()
    ######################
    @abstractmethod
    def 解码冫顺钥扌(sf, 顺钥文本, /, *, validate):
        '顺钥文本 -> 顺钥数据'
        #validate@解码向  <<== 此乃加密向
    @abstractmethod
    def 编码冫顺钥扌(sf, 顺钥数据, /):
        '顺钥数据 -> 顺钥文本'
    ######################
    @abstractmethod
    def 解码冫逆钥扌(sf, 逆钥文本, /):
        '逆钥文本 -> 逆钥数据'
    @abstractmethod
    def 编码冫逆钥扌(sf, 逆钥数据, /, *, validate):
        '逆钥数据 -> 逆钥文本'
    ######################
    ######################
    #有:密文文本牜裸,密文文本牜裹
    #有:密文数据牜裸,密文数据牜裹
    #有:明文文本牜裸,但无:明文文本牜裹
    #有:明文数据牜裸,但无:明文数据牜裹囗囗囗不存在
    ######################
    ######################
    @abstractmethod
    def 解码冫明文牜裸扌(sf, 明文文本牜裸, /, *, validate):
        '明文文本牜裸 -> 明文数据牜裸'
        #validate@解码向  <<== 此乃加密向
    @abstractmethod
    def 编码冫明文牜裸扌(sf, 明文数据牜裸, /):
        '明文数据牜裸 -> 明文文本牜裸'
    ######################
    @abstractmethod
    def 解码冫密文牜裸扌(sf, 密文文本牜裸, /):
        '密文文本牜裸 -> 密文数据牜裸'
    @abstractmethod
    def 编码冫密文牜裸扌(sf, 密文数据牜裸, /, *, validate):
        '密文数据牜裸 -> 密文文本牜裸'
    ######################
    @abstractmethod
    def 解码冫密文牜裹牜灬扌(sf, 密文文本牜裹, /):
        '密文文本牜裹 -> (逆钥文本, 密文文本牜裸)'
        #解析/parse
    @abstractmethod
    def 编码冫密文牜裹牜灬扌(sf, 逆钥文本, 密文文本牜裸, /, *, validate):
        '逆钥文本 -> 密文文本牜裸 -> 密文文本牜裹'
        #格式化/format
    ######################
    def 解码冫密文牜裹扌(sf, 密文文本牜裹, /):
        '密文文本牜裹 -> 密文数据牜裹'
        (逆钥文本, 密文文本牜裸) = sf.解码冫密文牜裹牜灬扌(密文文本牜裹)
        密文数据牜裸 = sf.解码冫密文牜裸扌(密文文本牜裸)
        逆钥数据 = sf.解码冫逆钥扌(逆钥文本)
        密文数据牜裹 = (逆钥数据,密文数据牜裸)
        return 密文数据牜裹
    def 编码冫密文牜裹扌(sf, 密文数据牜裹, /, *, validate):
        '密文数据牜裹 -> 密文文本牜裹'
        _validate = mk_validate4sub_call_(validate)
        (逆钥数据,密文数据牜裸) = 密文数据牜裹
        逆钥文本 = sf.编码冫逆钥扌(逆钥数据, validate=_validate)
        密文文本牜裸 = sf.编码冫密文牜裸扌(密文数据牜裸, validate=_validate)
        密文文本牜裹 = sf.编码冫密文牜裹牜灬扌(逆钥文本, 密文文本牜裸, validate=_validate)
        if validate:
            if not sf.解码冫密文牜裹扌(密文文本牜裹) == (密文数据牜裹):raise Exception((sf, (密文数据牜裹), (密文文本牜裹)))
        return 密文文本牜裹
    ######################
    @override
    def 加密冫明文文本牜裸扌(sf, 顺钥文本, 明文文本牜裸, /, *, validate):
        '顺钥文本/str -> 明文文本牜裸/str -> 密文文本牜裹/str'
        _validate = mk_validate4sub_call_(validate)
        顺钥数据 = sf.解码冫顺钥扌(顺钥文本, validate=_validate)
        明文数据牜裸 = sf.解码冫明文牜裸扌(明文文本牜裸, validate=_validate)
        密文数据牜裹 = sf.加密冫明文数据牜裸扌(顺钥数据, 明文数据牜裸, validate=_validate)
        密文文本牜裹 = sf.编码冫密文牜裹扌(密文数据牜裹, validate=_validate)
        if validate:
            #if not sf.自解密冫密文文本牜裹扌(密文文本牜裹) == (逆钥文本, 明文文本牜裸):raise Exception((sf, (顺钥文本, 明文文本牜裸), '??逆钥文本', (密文文本牜裹)))
            if not sf.自解密冫密文文本牜裹扌(密文文本牜裹)[1] == 明文文本牜裸:raise Exception((sf, (顺钥文本, 明文文本牜裸), (密文文本牜裹)))
        return 密文文本牜裹
    @override
    def 自解密冫密文文本牜裹扌(sf, 密文文本牜裹, /):
        '密文文本牜裹/str -> (逆钥文本, 明文文本牜裸)/(str,str)'
        _validate = False
        密文数据牜裹 = sf.解码冫密文牜裹扌(密文文本牜裹)
        (逆钥数据, 明文数据牜裸) = sf.自解密冫密文数据牜裹扌(密文数据牜裹)
        逆钥文本 = sf.编码冫逆钥扌(逆钥数据, validate=_validate)
        明文文本牜裸 = sf.编码冫明文牜裸扌(明文数据牜裸)
        return (逆钥文本, 明文文本牜裸)
    ######################
    ######################
    ######################
    ######################
    ######################
    ######################
    ######################
    ######################
    ######################
class 魖区位配置(ABC):
    __slots__ = ()
    @property
    @abstractmethod
    def 区数(sf, /):
        '-> 区数/uint # [0 ~==~ +oo]'
    @abstractmethod
    def 区号讠位数扌(sf, 区号, /):
        '区号/uint%区数 -> 位数乊区号/uint # [0 ~==~ +oo]'
    @abstractmethod
    def 码元讠鬽区位号扌(sf, 码元, /):
        '码元 -> may 区位号/(区号/uint%区数,位号/uint%位数乊区号) | ^LookupError'
    @abstractmethod
    def 码元巛区位号扌(sf, 区位号, /):
        '区位号/(区号/uint%区数,位号/uint%位数乊区号) -> 码元'


class 魖匴加密牜防识别牜自定义数据牜区内变换(魖匴加密牜防识别牜自定义数据):
    r'''[[[
    各区不相交，各区码元变换不窜区
    明文数据牜裸 :: [码元]
    密文数据牜裸 :: [码元]

区位配置:
    区号讠位数扌 :: 区号 -> 位数乊区号
    码元讠鬽区位号扌 :: 码元 -> may 区位号 | ^LookupError
        区位号=>有效码元
        None=>无关码元/不动点
        LookupError=>禁用码元
    码元巛区位号扌 :: 区位号 -> 码元


码元串讠有效区位号串辻序号串扌 :: [码元] -> (区位号串,序号串纟有效码元匕整体明文)/([区位号],[uint%明文整体长度)
    过滤掉:无关码元
有效码元串巛区位号串扌 :: [区位号] -> [码元]
码元串巛有效码元串辻序号串辻码元串乊异端扌 :: 有效码元串/[码元] -> 序号串纟有效码元匕整体明文/[uint%明文整体长度] -> 码元串乊异端/[码元] -> 码元串/[码元]

注水解码冫状态乊位次保持扌/注水扌/加盐扌 :: 顺钥数据 -> 区号串乊位次保持/[区号] -> 状态乊位次保持
岛链，孤岛，孤码
序号相关 :: ((序号纟码元匕有效明文,序号纟码元匕岛链,序号纟码元匕孤岛),(序号纟孤岛匕有效明文,序号纟孤岛匕岛链),(序号纟岛链匕有效明文,))
    状态乊位次保持:可能包含:
        明文有效长度/数量纟有效码元
            [囜文 == (明文|密文)]
        序号纟岛链匕有效明文 -> [序号纟孤岛匕有效明文]
        序号纟孤岛匕有效明文 -> (首序号,尾序号)/(序号纟码元匕有效明文,序号纟码元匕有效明文)
        序号纟码元匕有效明文 -> (区号,序号相关)
            <<==区号串乊位次保持
    状态乊位次变更:可能包含:
        序号纟码元匕有效密文 -> (区号,序号相关)
        明文有效长度/数量纟有效码元
明文整体长度==密文整体长度
明文有效长度==密文有效长度
明文有效长度==数量纟有效码元==明文整体长度-数量纟无关码元

加密牜区内加密扌 :: 状态乊位次保持 -> 位号串乊位次保持/[位号] -> (状态乊位次保持, 位号串乊位次保持/[位号])
*区内加密乊孤码扌 :: 序号纟码元匕有效明文 -> 状态乊位次保持 -> 位号 -> (状态乊位次保持, 位号)
*区内加密乊孤岛扌 :: 序号纟孤岛匕有效明文 -> 状态乊位次保持 -> 位号串纟孤岛/[位号] -> (状态乊位次保持, 位号串纟孤岛/[位号])
*区内加密乊岛链扌 :: 序号纟岛链匕有效明文 -> 状态乊位次保持 -> 位号串纟岛链/[位号] -> (状态乊位次保持, 位号串纟岛链/[位号])

索引置换牜顺向 :: [uint%明文有效长度]
索引置换牜逆向 :: [uint%明文有效长度]
索引置换牜顺向==旧址讠新址冃置换映射
索引置换牜逆向==新址讠旧址冃置换映射
索引置换牜逆向==inv(索引置换牜顺向)

易位扌/洗牌扌 :: 状态乊位次保持 -> (状态乊位次变更, 索引置换牜顺向/[uint%明文有效长度])
    shuffle/permutation
脱水编码冫状态乊位次变更扌 :: 状态乊位次变更 -> 逆钥数据
注水解码冫状态乊位次变更扌 :: 区号串乊位次变更/[区号] -> 逆钥数据 -> 状态乊位次变更
复位扌/还原扌 :: 状态乊位次变更 -> (状态乊位次保持, 索引置换牜逆向/[uint%明文有效长度])


解密牜区内解密扌 :: 状态乊位次保持 -> 位号串乊位次保持/[位号] -> (状态乊位次保持, 位号串乊位次保持/[位号])
*区内解密乊孤码扌 :: 序号纟码元匕有效明文 -> 状态乊位次保持 -> 位号 -> (状态乊位次保持, 位号)
*区内解密乊孤岛扌 :: 序号纟孤岛匕有效明文 -> 状态乊位次保持 -> 位号串纟孤岛/[位号] -> (状态乊位次保持, 位号串纟孤岛/[位号])
*区内解密乊岛链扌 :: 序号纟岛链匕有效明文 -> 状态乊位次保持 -> 位号串纟岛链/[位号] -> (状态乊位次保持, 位号串纟岛链/[位号])

    #]]]'''#'''
    __slots__ = ()

    @property
    @abstractmethod
    def 区位配置(sf, /):
        '-> 魖区位配置'

    def 统计冫明文有效长度牜自定义数据扌(sf, 囜文数据牜裸, /):
        '囜文数据牜裸/[码元] -> 明文有效长度/uint'
        明文有效长度 = sum(map(bool, map(sf.区位配置.码元讠鬽区位号扌, 囜文数据牜裸)))
        return 明文有效长度

    @abstractmethod
    def 易位扌(sf, 状态乊位次保持, /, *, validate):
        '状态乊位次保持 -> (状态乊位次变更, 索引置换牜顺向/[uint%明文有效长度])'
    @abstractmethod
    def 复位扌(sf, 状态乊位次变更, /):
        '状态乊位次变更 -> (状态乊位次保持, 索引置换牜逆向/[uint%明文有效长度])'
    @abstractmethod
    def 脱水编码冫状态乊位次变更扌(sf, 状态乊位次变更, /, *, validate):
        '状态乊位次变更 -> 逆钥数据'
    @abstractmethod
    def 注水解码冫状态乊位次变更扌(sf, 区号串乊位次变更, 逆钥数据, /):
        '区号串乊位次变更/[区号] -> 逆钥数据 -> 状态乊位次变更'
    @abstractmethod
    def 注水解码冫状态乊位次保持扌(sf, 顺钥数据, 区号串乊位次保持, /):
        '顺钥数据 -> 区号串乊位次保持/[区号] -> 状态乊位次保持'
        #本该:validate@解码向  <<== 此乃加密向
        #   但:没有相应的编码版！

    @abstractmethod
    def 加密牜区内加密扌(sf, 状态乊位次保持, 位号串乊位次保持, /, *, validate):
        '状态乊位次保持 -> 位号串乊位次保持/[位号] -> (状态乊位次保持, 位号串乊位次保持/[位号])'
    @abstractmethod
    def 解密牜区内解密扌(sf, 状态乊位次保持, 位号串乊位次保持, /):
        '状态乊位次保持 -> 位号串乊位次保持/[位号] -> (状态乊位次保持, 位号串乊位次保持/[位号])'


    @override
    def 加密冫明文数据牜裸扌(sf, 顺钥数据, 明文数据牜裸, /, *, validate):
        '顺钥数据/? -> 明文数据牜裸/? -> 密文数据牜裹/(逆钥数据,密文数据牜裸)/(?,?)'
        _validate = mk_validate4sub_call_(validate)
        (区位号串,序号串纟有效码元匕整体明文) = sf.码元串讠有效区位号串辻序号串扌(明文数据牜裸)
        (区号串乊位次保持, 位号串乊位次保持) = map(tuple, unzip_pairs(区位号串乊位次保持:=区位号串))
        状态乊位次保持 = sf.注水解码冫状态乊位次保持扌(顺钥数据, 区号串乊位次保持)
        (状态乊位次保持, 位号串乊位次保持) = sf.加密牜区内加密扌(状态乊位次保持, 位号串乊位次保持, validate=_validate)
        (状态乊位次变更, 索引置换牜顺向) = sf.易位扌(状态乊位次保持, validate=_validate)
        区位号串乊位次保持 = tuple(zip(区号串乊位次保持, 位号串乊位次保持))
        有效码元串乊位次保持 = sf.有效码元串巛区位号串扌(区位号串乊位次保持)
        有效码元串乊位次变更 = 置换扌(索引置换牜顺向, 有效码元串乊位次保持)
        码元串乊位次变更 = sf.码元串巛有效码元串辻序号串辻码元串乊异端扌(有效码元串乊位次变更, 序号串纟有效码元匕整体明文, 明文数据牜裸)
        密文数据牜裸 = 码元串乊位次变更
        逆钥数据 = sf.脱水编码冫状态乊位次变更扌(状态乊位次变更, validate=_validate)
        密文数据牜裹 = (逆钥数据,密文数据牜裸)
        if validate:
            if not sf.自解密冫密文数据牜裹扌(密文数据牜裹) == (逆钥数据, 明文数据牜裸):raise Exception((sf, (顺钥数据, 明文数据牜裸), 逆钥数据, (密文数据牜裹)))
        return 密文数据牜裹
    @override
    def 自解密冫密文数据牜裹扌(sf, 密文数据牜裹, /):
        '密文数据牜裹/(逆钥数据,密文数据牜裸)/(?,?) -> (逆钥数据, 明文数据牜裸)/(?,?)'
        (逆钥数据,密文数据牜裸) = 密文数据牜裹
        (区位号串,序号串纟有效码元匕整体密文) = sf.码元串讠有效区位号串辻序号串扌(密文数据牜裸)
        序号串纟有效码元匕整体明文 = 序号串纟有效码元匕整体密文
        区号串乊位次变更 = tuple(map(fst, 区位号串乊位次变更:=区位号串))
        状态乊位次变更 = sf.注水解码冫状态乊位次变更扌(区号串乊位次变更, 逆钥数据)
        (状态乊位次保持, 索引置换牜逆向) = sf.复位扌(状态乊位次变更)
        区位号串乊位次保持 = 置换扌(索引置换牜逆向, 区位号串乊位次变更:=区位号串)
        (区号串乊位次保持, 位号串乊位次保持) = map(tuple, unzip_pairs(区位号串乊位次保持))

        (状态乊位次保持, 位号串乊位次保持) = sf.解密牜区内解密扌(状态乊位次保持, 位号串乊位次保持)
        区位号串乊位次保持 = tuple(zip(区号串乊位次保持, 位号串乊位次保持))
        有效码元串乊位次保持 = sf.有效码元串巛区位号串扌(区位号串乊位次保持)
        码元串乊位次保持 = sf.码元串巛有效码元串辻序号串辻码元串乊异端扌(有效码元串乊位次保持, 序号串纟有效码元匕整体明文, 密文数据牜裸)
        明文数据牜裸 = 码元串乊位次保持
        #xxx:不一定有:顺钥数据
        return (逆钥数据,明文数据牜裸)
    def 码元串讠有效区位号串辻序号串扌(sf, 码元串, /):
        '[码元] -> (区位号串,序号串纟有效码元匕整体明文)/([区位号],[uint%明文整体长度)'
        #过滤掉:无关码元
        (区位号串,序号串纟有效码元匕整体明文) = map(tuple, unzip_pairs((区位号,序号) for 序号,鬽区位号 in enumerate(map(sf.区位配置.码元讠鬽区位号扌, 码元串)) if not (区位号:=鬽区位号) is None))
        return (区位号串,序号串纟有效码元匕整体明文)
    def 有效码元串巛区位号串扌(sf, 区位号串, /):
        '[区位号] -> [码元]'
        有效码元串 = tuple(map(sf.区位配置.码元巛区位号扌, 区位号串))
        return 有效码元串
    def 码元串巛有效码元串辻序号串辻码元串乊异端扌(sf, 有效码元串, 序号串纟有效码元匕整体明文, 码元串乊异端, /):
        '有效码元串/[码元] -> 序号串纟有效码元匕整体明文/[uint%明文整体长度] -> 码元串乊异端/[码元] -> 码元串/[码元]'
        if not len(有效码元串) == len(序号串纟有效码元匕整体明文) <= len(码元串乊异端):raise TypeError
        def __():
            prev_j = -1
            it = iter(有效码元串)
            for j in 序号串纟有效码元匕整体明文:
                yield from 码元串乊异端[prev_j+1:j]
                    #不动点@gap
                    #===像纟不动点@gap
                yield next(it)
                    #像纟动点@j
                prev_j = j
            else:
                j = 明文整体长度 = len(码元串乊异端)
                yield from 码元串乊异端[prev_j+1:j]
                    #不动点@gap
                    #===像纟不动点@gap
        码元串 = tuple(__())
        return 码元串

def 置换扌(旧址讠新址冃置换映射, 输入串, /):
    'j_new5j_old/[uint%L]{len=L} -> [c]{len=L} -> [c]{len=L}'
    j_new5j_old = 旧址讠新址冃置换映射
    j_new2j_old = inverse_uint_bijection_array(j_new5j_old)
    L = len(j_new2j_old)
    if not len(输入串) == L:raise TypeError
    输出串 = tuple(输入串[j_new2j_old[j]] for j in range(L))
    return 输出串

class 魖匴加密牜防识别牜自定义数据牜区内变换乊孤码(魖匴加密牜防识别牜自定义数据牜区内变换):
    __slots__ = ()
    @abstractmethod
    def 区内加密乊孤码扌(sf, 序号纟码元匕有效明文, 状态乊位次保持, 位号, /, *, validate):
        '序号纟码元匕有效明文 -> 状态乊位次保持 -> 位号 -> (状态乊位次保持, 位号)'
    @abstractmethod
    def 区内解密乊孤码扌(sf, 序号纟码元匕有效明文, 状态乊位次保持, 位号, /):
        '序号纟码元匕有效明文 -> 状态乊位次保持 -> 位号 -> (状态乊位次保持, 位号)'

    @override
    def 加密牜区内加密扌(sf, 状态乊位次保持, 位号串乊位次保持, /, *, validate):
        '状态乊位次保持 -> 位号串乊位次保持/[位号] -> (状态乊位次保持, 位号串乊位次保持/[位号])'
        _validate = mk_validate4sub_call_(validate)
        (状态乊位次保持_, 位号串乊位次保持_) = (状态乊位次保持, 位号串乊位次保持)
        ls = []
        for (序号纟码元匕有效明文, 位号) in enumerate(位号串乊位次保持):
            (状态乊位次保持, 位号) = sf.区内加密乊孤码扌(序号纟码元匕有效明文, 状态乊位次保持, 位号, validate=_validate)
            ls.append(位号)
        状态乊位次保持
        位号串乊位次保持 = tuple(ls)
        (_状态乊位次保持, _位号串乊位次保持) = (状态乊位次保持, 位号串乊位次保持)
        if validate:
            if not sf.解密牜区内解密扌(_状态乊位次保持, _位号串乊位次保持) == (状态乊位次保持_, 位号串乊位次保持_):raise Exception((sf, (状态乊位次保持_, 位号串乊位次保持_), (_状态乊位次保持, _位号串乊位次保持)))
        return (_状态乊位次保持, _位号串乊位次保持)

    @override
    def 解密牜区内解密扌(sf, 状态乊位次保持, 位号串乊位次保持, /):
        '状态乊位次保持 -> 位号串乊位次保持/[位号] -> (状态乊位次保持, 位号串乊位次保持/[位号])'
        ls = []
        for (序号纟码元匕有效明文, 位号) in zip(range(len(位号串乊位次保持))[::-1], reversed(位号串乊位次保持)):
            (状态乊位次保持, 位号) = sf.区内解密乊孤码扌(序号纟码元匕有效明文, 状态乊位次保持, 位号)
            ls.append(位号)
        ls.reverse() #bug:once miss this line
        状态乊位次保持
        位号串乊位次保持 = tuple(ls)
        return (状态乊位次保持, 位号串乊位次保持)


class 魖匴加密牜防识别牜文本氺自定义数据牜区内变换(魖匴加密牜防识别牜自定义数据牜区内变换, 魖匴加密牜防识别牜文本氺自定义数据):
    __slots__ = ()
    @abstractmethod
    def 统计冫明文有效长度牜文本扌(sf, 囜文文本牜裸, /):
        '囜文文本牜裸/str -> 明文有效长度/uint'
        # 未知:关系(码元,字符)
        #囜文数据牜裸 = sf.???(囜文文本牜裸)
        #明文有效长度 = sf.统计冫明文有效长度牜自定义数据扌(囜文数据牜裸)
        #return 明文有效长度
    pass
class 魖匴加密牜防识别牜文本氺自定义数据牜区内变换乊孤码(魖匴加密牜防识别牜自定义数据牜区内变换乊孤码, 魖匴加密牜防识别牜文本氺自定义数据牜区内变换):
    __slots__ = ()
    pass





class 魖匴转义冫文本(ABC):
    r'''[[[
    '无:带外符号/超符'
        见:魖匴转义冫超文本
    ===
    避免:类似c/py的编码方案:
        因为:导致多次转义后长度指数型爆炸！
        『\』-->『\\』-->『\\\\』-->『\\\\\\\\』-->『\\\\\\\\\\\\\\\\』
    简单的避免方案:
        『!?』-->『!?.』-->『!?..』-->『!?...』-->『!?....』
    #]]]'''#'''
    __slots__ = ()
    @abstractmethod
    def 转义冫文本扌(sf, 文本乊转义前, /):
        '文本乊转义前/str -> 文本乊转义后/str'
    @abstractmethod
    def 还原冫文本扌(sf, 文本乊转义后, /):
        '文本乊转义后/str -> 文本乊转义前/str'
class 魖匴转义冫超文本(ABC):
    r'''[[[
    '允许含:带外符号/超符'
        见:魖匴转义冫文本
    [超符 may be str]
    [超文本 :: [文本{非空unless[索引==0]} if 索引%2==0 else 非空超符串]]
    [非标准型超文本 :: [(欤超符串, (文本|超符串))]/[(bool,(str|[超符]))]]
        # [负载牜裹裹纟文本 == '!?{负载牜裹纟文本}' == '!?[^(^]' | '!?(.*)']
        # [负载牜裹纟文本 == (单字符/负载牜裸纟文本 | '({负载牜裸纟文本})') == (单字符/'[^(^]' | '(.*)')]
        # [负载牜裹裹纟超符串 == '!?^{负载牜裹纟超符串}' == '!?^[:all:]' | '!?^(.*)']
        # [负载牜裹纟超符串 == (单字符/负载牜裸纟超符串 | '({负载牜裸纟超符串})') == (单字符/'[[:all:]]' | '(.*)')]
    ===
    避免:类似c/py的编码方案:
        因为:导致多次转义后长度指数型爆炸！
        『\』-->『\\』-->『\\\\』-->『\\\\\\\\』-->『\\\\\\\\\\\\\\\\』
    简单的避免方案:
        『!?』-->『!?.』-->『!?..』-->『!?...』-->『!?....』
    #]]]'''#'''
    #前缀纟超符:特殊负载前缀:变长负载or定长负载
    __slots__ = ()
    @abstractmethod
    def 转义冫超文本扌(sf, 超文本乊转义前, /):
        '超文本 -> 文本/str'
    @abstractmethod
    def 还原冫超文本扌(sf, 超文本乊转义后, /):
        '文本/str -> 超文本'
class 乸匴转义冫超文本牜极简具现(魖匴转义冫超文本):
    '极简版:[超符 :: str]'
    ___no_slots_ok___ = True
    ######################
    ######################
    ######################
    def __init__(sf, /, *
        , 字符串冃转义序列前缀='!?'
        , 起字符串纟变长负载='('
        , 讫字符串纟变长负载=')'
        , 头字符串纟变长负载纟超符串='^'
        , 隔字符串纟变长负载纟超符串=','
        , 编码向冫负载字符串纟转义序列前缀='.'
        , 编码向冫原字符讠负载字符串={'\a':'a','\b':'b','\f':'f','\n':'n','\r':'r','\t':'t','\v':'v','\0':'0',' ':'-','　':'='}
        , 解码向冫负载字符串讠原字符={'a':'\a','b':'\b','f':'\f','n':'\n','r':'\r','t':'\t','v':'\v','0':'\0','-':' ','=':'　'}
        , 解码向冫鬽后备解码器纟负载字符串=None
        #, 解码向冫超符巛负载字符串扌=echo
        ):
        '极简:负载为单字符或变长负载；除了『转义序列前缀』外，只转义单字符(编码时不再使用正则表达式)'
        # abfnrtv0:\n... + 2 spaces
        # 『\』-->『!?』-->『!?.』
        # 『\xhh』-->『!?(xhh)』-->解码向冫鬽后备解码器纟负载字符串('xhh')
        d = dict(locals())
        del d['sf']
        sf.__dict__.update(d)
        sf._kwds = d
        assert 字符串冃转义序列前缀
        #assert 编码向冫负载字符串纟转义序列前缀
        assert 起字符串纟变长负载
        assert 讫字符串纟变长负载
        assert 头字符串纟变长负载纟超符串
        assert 隔字符串纟变长负载纟超符串
        assert all(len(ch)==1 for ch in 编码向冫原字符讠负载字符串)
        ...
    def __repr__(sf, /):
        args = ()
        kwargs = sf._kwds
        return repr_helper(sf, *args, **kwargs)

    def 还原冫负载纟超符串扌(sf, 负载牜裸纟超符串, /):
        '负载牜裸纟超符串 -> 超符串'
        超符串 = tuple(负载牜裸纟超符串.split(sf.隔字符串纟变长负载纟超符串))
        return 超符串
    def 还原冫负载纟文本扌(sf, 负载牜裸纟文本, /):
        '负载牜裸纟文本 -> 原字符串'
        if 负载牜裸纟文本 == sf.编码向冫负载字符串纟转义序列前缀:
            m = sf.字符串冃转义序列前缀
        else:
            m = sf.解码向冫负载字符串讠原字符.get(负载牜裸纟文本)
        m
        if m is None:
            if None is sf.解码向冫鬽后备解码器纟负载字符串:
                raise Exception(f'解码失败:负载牜裸纟文本={负载牜裸纟文本!r}')
            原字符串 = sf.解码向冫鬽后备解码器纟负载字符串(负载牜裸纟文本)
        else:
            原字符串 = m
        return 原字符串
    def 封装冫负载巛超符串扌(sf, 超符串, /, *, validate):
        '超符串 -> 负载牜裹裹纟超符串'
        _validate = mk_validate4sub_call_(validate)
        #xxx:if not 超符串
        负载牜裸纟超符串 = sf.隔字符串纟变长负载纟超符串.join(超符串)
        负载牜裹裹纟超符串 = sf.封装冫负载纟文本扌(负载牜裸纟超符串, head=sf.头字符串纟变长负载纟超符串, validate=_validate)
        if validate:
            #xxx:if not sf.还原冫负载纟文本扌(负载) == ():raise Exception((sf, (), ()))
            #没有相应的解码版！
            pass
        return 负载牜裹裹纟超符串
    def 封装冫负载纟文本扌(sf, 负载牜裸纟文本, /, *, validate, head=''):
        '负载牜裸纟文本 -> 负载牜裹裹纟文本'
        _validate = mk_validate4sub_call_(validate)
        if len(负载牜裸纟文本) == 1:
            assert not 负载牜裸纟文本 == sf.起字符串纟变长负载[0]
            负载牜裹纟文本 = 单字符负载 = 负载牜裸纟文本
        else:
            负载牜裹纟文本 = f'{sf.起字符串纟变长负载}{负载牜裸纟文本}{sf.讫字符串纟变长负载}'
        负载牜裹纟文本
        负载牜裹裹纟文本 = f'{sf.字符串冃转义序列前缀}{head}{负载牜裹纟文本}'
        if validate:
            #xxx:if not sf.还原冫负载纟文本扌(负载?) == ():raise Exception((sf, (), ()))
            #没有相应的解码版！
            pass
        return 负载牜裹裹纟文本
    def 检查冫超文本扌(sf, 超文本, /):
        '标准型#并最少空串'
        ######################
        超文本[:0] # seq?
        ######################
        for x in 超文本[0::2]:
            check_type_is(str, x)
        for x in 超文本[1::2]:
            check_type_is(tuple, x)
            for y in x:
                check_type_is(str, y)
        ######################
        for 超符串 in 超文本[1::2]:
            for 超符 in 超符串:
                if not 超符:raise Exception #封装时会产生歧义！
        ######################
        ss = (sf.字符串冃转义序列前缀, sf.隔字符串纟变长负载纟超符串, sf.讫字符串纟变长负载)
        for 超符串 in 超文本[1::2]:
            for 超符 in 超符串:
                for s in ss:
                    if s in 超符:raise Exception(超符)
        ######################
        if len(超文本) == 1 and not 超文本[0]:raise Exception((0, 超文本))
        it = iter(超文本)
        _ = next(it, 000)
        for j, x in enumerate(it, 1):
            if not x:raise Exception((j, 超文本))
        ######################

    @override
    def 转义冫超文本扌(sf, 超文本, /, *, validate):
        '超文本 -> 文本/str'
        sf.检查冫超文本扌(超文本)
        _validate = mk_validate4sub_call_(validate)
        z = sf.封装冫负载纟文本扌(sf.编码向冫负载字符串纟转义序列前缀, validate=_validate)
        def _h():
            #return z.join(s for j,x in enumerate(超文本) for s in (_f1 if (欤超符串:=j&1) else _f0)(x))
                #SyntaxError: assignment expression cannot be used in a comprehension iterable expression
            return ''.join(f(x) for f,x in zip(cycle_([_f0, _f1]), 超文本))
            return ''.join(s for j,x in enumerate(超文本) for s in (_f1 if (j&1) else _f0)(x)) # (欤超符串:=j&1)
        def _f1(超符串, /):
            '-> 部分文本乊转义后'
            部分文本乊转义后 = sf.封装冫负载巛超符串扌(超符串, validate=_validate)
            #if 0b0000:print_err(repr(部分文本乊转义后))
            return 部分文本乊转义后
        def _f0(文本乊转义前, /):
            '-> 部分文本乊转义后'
            部分文本乊转义后 = z.join(_f00(文本乊转义前))
            return 部分文本乊转义后
        def _f00(文本乊转义前, /):
            '-> Iter 部分文本乊转义后'
            for s in 文本乊转义前.split(sf.字符串冃转义序列前缀):
                部分文本乊转义后 = ''.join(_g(s))
                #if 0b0000:print_err(repr(部分文本乊转义后))
                yield 部分文本乊转义后
        def _g(s, /):
            '-> Iter (转义序列|原字符)'
            for ch in s:
                m = sf.编码向冫原字符讠负载字符串.get(ch)
                t = ch if m is None else sf.封装冫负载纟文本扌(负载:=m, validate=_validate)
                yield t
        #if 0b0000:print_err(文本乊转义前)
        #if 0b0000:print_err(文本乊转义前.split(sf.字符串冃转义序列前缀))
        文本乊转义后 = _h()
        #if 0b0000:print_err(文本乊转义后)
        if validate:
            超文本牜去除尾零 = [*超文本]
            while 超文本牜去除尾零 and not 超文本牜去除尾零[-1]:
                超文本牜去除尾零.pop()
            if not (r:=[*sf.还原冫超文本扌(文本乊转义后)]) == 超文本牜去除尾零:raise Exception((sf, 超文本, 文本乊转义后, (超文本牜去除尾零,r)))
        return 文本乊转义后
    @override
    def 还原冫超文本扌(sf, 文本, /):
        '文本/str -> 超文本'
        check_type_is(str, 文本)
        def _h():
            '-> 超文本'
            lsls = [['']]
            def put_meta_(超符串, /):
                if len(lsls)&1:
                    lsls.append([])
                lsls[-1].extend(超符串)
            def put_str_(文本, /):
                if not len(lsls)&1:
                    lsls.append([])
                lsls[-1].append(文本)
            def _fill_lsls():
                #for 欤超符串, it in group_by(_f(), key=fst, container=iter):
                for 欤超符串, x in _f():
                    if not x:
                        pass
                    elif 欤超符串:
                        超符串 = x
                        put_meta_(超符串)
                    else:
                        文本 = x
                        put_str_(文本)
            _fill_lsls()
            lsls
            超文本 = tuple(f(ls) for ls, f in zip(lsls, cycle_([''.join, tuple])))
            if 超文本 == ('',):
                超文本 = ()
            return 超文本
        def _f():
            '-> Iter (欤超符串, (文本|超符串))'
            first = True
            for s in 文本.split(sf.字符串冃转义序列前缀):
                if first:
                    first = False
                    yield (欤超符串:=False,s)
                else:
                    yield from _g(s)
        def _g(s, /):
            '-> Iter (欤超符串, (文本|超符串))'
            h0 = 0
            if s.startswith(sf.头字符串纟变长负载纟超符串):
                h0 = len(sf.头字符串纟变长负载纟超符串)

            if h0==0 and s.startswith(sf.编码向冫负载字符串纟转义序列前缀):
                i = h0
                j = len(sf.编码向冫负载字符串纟转义序列前缀)
                end = j+0
            elif s.startswith(sf.起字符串纟变长负载, h0):
                i = h0+len(sf.起字符串纟变长负载)
                j = s.index(sf.讫字符串纟变长负载, i)
                end = j + len(sf.讫字符串纟变长负载)
            else:
                i = h0
                j = i+1
                end = j+0
            h0, i, j, end
            欤超符串 = bool(h0)
            负载牜裸纟囜囜囜 = s[i:j]
            其余纟不动串 = s[end:]

            if 欤超符串:
                超符串 = sf.还原冫负载纟超符串扌(负载牜裸纟超符串:=负载牜裸纟囜囜囜)
                yield (欤超符串, 超符串)
            else:
                原字符串 = sf.还原冫负载纟文本扌(负载牜裸纟文本:=负载牜裸纟囜囜囜)
                yield (欤超符串, 原字符串)
            yield (欤超符串:=False,其余纟不动串)
        try:
            超文本 = _h()
        except:
            raise Exception(文本)
        return 超文本
#class 乸匴转义冫超文本牜极简具现(魖匴转义冫超文本):
匴转义冫超文本牜极简具现 = 乸匴转义冫超文本牜极简具现()






class 乸匴转义冫文本牜极简具现(魖匴转义冫文本):
    '极简版'
    ___no_slots_ok___ = True
    ######################
    ######################
    ######################
    r'''[[[
    def __init__(sf, /, *, 字符串纟转义='!', 负载字符冃转义='.', 负载字符冃空格='_', 负载字符冃换行='n', 负载字符冃制表='t', 起字符串纟变长负载='(', 讫字符串纟变长负载=')'):
        ...
    def __init__(sf, /, *, 字符串冃转义序列前缀='!', 编码向冫原串讠负载字符串={}, 编码向冫正则表达式纟前缀讠正则表达式纟原串讠编码器={}, 解码向冫负载字符串讠原串={}, 解码向冫正则表达式纟前缀讠正则表达式纟负载字符串讠解码器={}):
        #变长负载vs定长负载
        #   !(...)
        #   !⑷xxxx
        ...
    def __init__(sf, /, *, 字符串冃转义序列前缀='!', 起字符串纟变长负载='(', 讫字符串纟变长负载=')', 编码向冫原字符讠负载字符串={'!':'.'}, 编码向冫正则表达式纟转义序列前缀相关原串辻编码器=('!', '!.'), 解码向冫负载字符串讠原字符={'.':'!'}, 解码向冫正则表达式纟前缀讠正则表达式纟负载字符串讠解码器={}):
        '简化:负载为单字符或变长负载；除了『转义序列前缀』相关外，只转义单字符(编码时只使用一个正则表达式)'
        ...
    #]]]'''#'''
    ######################
    ######################
    ######################
    def __init__(sf, /, *
        , 字符串冃转义序列前缀='!?'
        , 起字符串纟变长负载='('
        , 讫字符串纟变长负载=')'
        , 编码向冫负载字符串纟转义序列前缀='.'
        , 编码向冫原字符讠负载字符串={'\a':'a','\b':'b','\f':'f','\n':'n','\r':'r','\t':'t','\v':'v','\0':'0',' ':'-','　':'='}
        , 解码向冫负载字符串讠原字符={'a':'\a','b':'\b','f':'\f','n':'\n','r':'\r','t':'\t','v':'\v','0':'\0','-':' ','=':'　'}
        , 解码向冫鬽后备解码器纟负载字符串=None
        ):
        '极简:负载为单字符或变长负载；除了『转义序列前缀』外，只转义单字符(编码时不再使用正则表达式)'
        # abfnrtv0:\n... + 2 spaces
        # 『\』-->『!?』-->『!?.』
        # 『\xhh』-->『!?(xhh)』-->解码向冫鬽后备解码器纟负载字符串('xhh')
        d = dict(locals())
        del d['sf']
        sf.__dict__.update(d)
        sf._kwds = d
        assert 字符串冃转义序列前缀
        #assert 编码向冫负载字符串纟转义序列前缀
        assert 起字符串纟变长负载
        assert 讫字符串纟变长负载
        assert all(len(ch)==1 for ch in 编码向冫原字符讠负载字符串)
        ...
    def __repr__(sf, /):
        args = ()
        kwargs = sf._kwds
        return repr_helper(sf, *args, **kwargs)
    def 还原冫负载扌(sf, 负载, /):
        if 负载 == sf.编码向冫负载字符串纟转义序列前缀:
            m = sf.字符串冃转义序列前缀
        else:
            m = sf.解码向冫负载字符串讠原字符.get(负载)
        m
        if m is None:
            if None is sf.解码向冫鬽后备解码器纟负载字符串:
                raise Exception(f'解码失败:负载={负载!r}')
            原字符串 = sf.解码向冫鬽后备解码器纟负载字符串(负载)
        else:
            原字符串 = m
        return 原字符串
    def 封装冫负载扌(sf, 负载, /, *, validate):
        _validate = mk_validate4sub_call_(validate)
        if len(负载) == 1:
            assert not 负载 == sf.起字符串纟变长负载[0]
            pass
        else:
            负载 = f'{sf.起字符串纟变长负载}{负载}{sf.讫字符串纟变长负载}'
        if validate:
            #xxx:if not sf.还原冫负载扌(负载) == ():raise Exception((sf, (), ()))
            #没有相应的解码版！
            pass
        return f'{sf.字符串冃转义序列前缀}{负载}'
    @override
    def 转义冫文本扌(sf, 文本乊转义前, /, *, validate):
        '文本乊转义前/str -> 文本乊转义后/str'
        _validate = mk_validate4sub_call_(validate)
        def _h():
            z = sf.封装冫负载扌(sf.编码向冫负载字符串纟转义序列前缀, validate=_validate)
            return z.join(_f())
        def _f():
            '-> Iter 部分文本乊转义后'
            for s in 文本乊转义前.split(sf.字符串冃转义序列前缀):
                部分文本乊转义后 = ''.join(_g(s))
                yield 部分文本乊转义后
        def _g(s, /):
            '-> Iter (转义序列|原字符)'
            for ch in s:
                m = sf.编码向冫原字符讠负载字符串.get(ch)
                t = ch if m is None else sf.封装冫负载扌(负载:=m, validate=_validate)
                yield t
        #if 0b0000:print_err(文本乊转义前)
        #if 0b0000:print_err(文本乊转义前.split(sf.字符串冃转义序列前缀))
        文本乊转义后 = _h()
        #if 0b0000:print_err(文本乊转义后)
        if validate:
            if not sf.还原冫文本扌(文本乊转义后) == 文本乊转义前:raise Exception((sf, 文本乊转义前, 文本乊转义后))
        return 文本乊转义后
    @override
    def 还原冫文本扌(sf, 文本乊转义后, /):
        '文本乊转义后/str -> 文本乊转义前/str'
        def _h():
            #z = sf.编码向冫负载字符串纟转义序列前缀
            z = ''
            return z.join(_f())
        def _f():
            first = True
            for s in 文本乊转义后.split(sf.字符串冃转义序列前缀):
                if first:
                    first = False
                    yield s
                else:
                    yield from _g(s)
        def _g(s, /):
            if s.startswith(sf.编码向冫负载字符串纟转义序列前缀):
                i = 0
                j = len(sf.编码向冫负载字符串纟转义序列前缀)
                end = j+0
            elif s.startswith(sf.起字符串纟变长负载):
                i = len(sf.起字符串纟变长负载)
                j = s.index(sf.讫字符串纟变长负载, i)
                end = j + len(sf.讫字符串纟变长负载)
            else:
                i = 0
                j = 1
                end = j+0
            i, j, end
            负载 = s[i:j]
            其余纟不动串 = s[end:]

            原字符串 = sf.还原冫负载扌(负载)
            yield 原字符串
            yield 其余纟不动串
        try:
            文本乊转义前 = _h()
        except:
            raise Exception(文本乊转义后)
        return 文本乊转义前
#class 乸匴转义冫文本牜极简具现(魖匴转义冫文本):
匴转义冫文本牜极简具现 = 乸匴转义冫文本牜极简具现()
匴转义冫用于分隔匾协议 = 乸匴转义冫文本牜极简具现(*''
    , 编码向冫原字符讠负载字符串={':':'='}
    , 解码向冫负载字符串讠原字符={'=':':'}
    )


class 乸注册处纟加密牜防识别牜文本(魖注册处纟加密牜防识别牜文本):
    'using:匴转义冫用于分隔匾协议'
    ___no_slots_ok___ = True
    def __init__(sf, d=None, /):
        sf._d = {} if d is None else d
    def __repr__(sf, /):
        return repr_helper(sf, sf._d)
    @override
    def 枚举冫匾协议乊已注册扌(sf, /):
        '-> Iter 匾协议/str'
        return iter(sf._d)
    @override
    def 查找扌(sf, 匾协议, /):
        '匾协议/str -> 匴加密/魖匴加密牜防识别牜文本 | ^LookupError'
        return sf._d[匾协议]
    @override
    def 注册扌(sf, 匴加密, /):
        '匴加密/魖匴加密牜防识别牜文本 -> None'
        匾协议 = 匴加密.匾协议
        if 匾协议 in sf._d:raise KeyError(f'已注册冫匾协议:{匾协议}')
        sf._d[匾协议] = 匴加密
        return
    @override
    def 编码冫密文文本牜裹裹扌(sf, 匾协议, 密文文本牜裹, /, *, validate):
        '匾协议 -> 密文文本牜裹 -> 密文文本牜裹裹'
        #格式化
        _validate = mk_validate4sub_call_(validate)
        nm4protocol = 匴转义冫用于分隔匾协议.转义冫文本扌(匾协议, validate=_validate)
        密文文本牜裹裹 = f'{nm4protocol}:{密文文本牜裹}'
        if validate:
            if not sf.解码冫密文文本牜裹裹扌(密文文本牜裹裹) == (匾协议, 密文文本牜裹):raise Exception((sf, (匾协议, 密文文本牜裹), 密文文本牜裹裹))
        return 密文文本牜裹裹
    @override
    def 解码冫密文文本牜裹裹扌(sf, 密文文本牜裹裹, /):
        '密文文本牜裹裹 -> (匾协议, 密文文本牜裹)'
        #解析
        (nm4protocol, sep, 密文文本牜裹) = 密文文本牜裹裹.partition(':')
        if not sep:raise Exception((密文文本牜裹, ':'))
        匾协议 = 匴转义冫用于分隔匾协议.还原冫文本扌(nm4protocol)
        return (匾协议, 密文文本牜裹)

import re

from seed.data_funcs.rngs import StackStyleSimpleIntMapping #make_Ranges, sorted_ints_to_iter_nontouch_ranges, detect_iter_ranges, StackStyleSimpleIntSet, , TouchRangeBasedIntMapping
from seed.text.unicode.constant import CHAR_ORD_UPPER# MAX_CHAR_ORD


class 乸区位配置牜码元为字符编码点(魖区位配置):
    r'''[[[
[码元 == 字符编码点]
[位移量臫位号臸字符编码点 =[def]= 字符编码点-位号]

多区配置简易表达 :: [单区配置简易表达] or '::;'.join(iter单区配置简易表达)
单区配置简易表达 :: [单块配置简易表达] or '::,'.join(iter单块配置简易表达)
单块配置简易表达:
    # 位号<<==次序敏感,禁止重复码元
    * 连续式/range:
        A..<Z => [A-Y]
        A..=Z => [A-Z]
            #反双缀<<==添加『<』『=』
            #区别于『直列式/list』<<=『..』重复字符
    * 直列式/list:
        ^ax-0.6 => [ax06.^-]
     ###listXrange:
        ^ax-0.6::,A..=Z
        ######################
        分区符:『::;』
        分块符:『::,』#非必需
        连续符纟左无穷右无穷区间:『..__』#『..__』用于表达[..]
        连续符纟左无穷右开区间:『..^^<』#『..^^<x』用于表达[..<x]
        连续符纟左无穷右闭区间:『..^^=』#『..^^=x』用于表达[..=x]
        连续符纟左闭右无穷区间:『..$$』#『a..$$』用于表达[a..]
        连续符纟左闭右开区间:『..<』
        连续符纟闭区间:『..=』
        <<==:
        要求:带外编码集:反双缀&&含重复字符
        <<==:
        #歧义:a...x
        a;;...x
        a...;;x
        #歧义:a;;;x
        a;,,x
        a,,;x
        #歧义:a,;;;x
        #歧义:a,,,;x
        a;,;x
        #歧义:a;,;,;x

    #]]]'''#'''
    ___no_slots_ok___ = True
    分区符 = '::;'#非必需
    分块符 = '::,'#非必需
    连续符纟左无穷右无穷区间 = '..__' #『..__』用于表达[..]
    连续符纟左无穷右开区间 = '..^^<' #『..^^<x』用于表达[..<x]
    连续符纟左无穷右闭区间 = '..^^=' #『..^^=x』用于表达[..=x]
    连续符纟左闭右无穷区间 = '..$$' #『a..$$』用于表达[a..]
    连续符纟左闭右开区间 = '..<'
    连续符纟闭区间 = '..='
    @classmethod
    def 构造冫正则表达式纟连续符扌(cls, /):
        a00 = re.escape(cls.连续符纟左无穷右无穷区间)
        b01 = re.escape(cls.连续符纟左无穷右开区间)
        c01 = re.escape(cls.连续符纟左无穷右闭区间)
        d10 = re.escape(cls.连续符纟左闭右无穷区间)
        e11 = re.escape(cls.连续符纟左闭右开区间)
        f11 = re.escape(cls.连续符纟闭区间)

        #正则表达式纟连续符 = re.compile(r'(?:[.][.]__|[.][.][^][^][<=].|.[.][.][$][$]|.[.][.][<=].)', re.DOTALL)
        return (正则表达式纟连续符 := re.compile(fr'({a00}|{b01}.|{c01}.|.{d10}|.{e11}.|.{f11}.)', re.DOTALL))
            #capturing parentheses are used in pattern for "re.split()"

    def __init__(sf, /, *区号讠单区配置简易表达, 不动区配置简易表达=''):
        ######################
        cls = type(sf)
        rex4sep = cls.正则表达式纟连续符
        ######################
        def f(下一个位号, 小块, 欤连续块):
            '-> (数量, Iter (起始位号, 数量, 起始字符编码点))'
            if not 欤连续块:
                # 直列块
                assert not '..' in 小块
                it = ((起始位号:=位号, 数量:=1, 起始字符编码点:=code_pt) for 位号, code_pt in enumerate(map(ord, 小块), 下一个位号))
                数量 = len(小块)
            else:
                # 连续块
                assert '..' in 小块
                if ((sep:=cls.连续符纟左无穷右无穷区间) in 小块):
                    assert sep == 小块[:]
                    begin_pt = 0
                    end_pt = CHAR_ORD_UPPER
                elif ((sep:=cls.连续符纟左无穷右开区间) in 小块):
                    assert sep == 小块[:-1]
                    begin_pt = 0
                    end_pt = ord(小块[-1])
                elif ((sep:=cls.连续符纟左无穷右闭区间) in 小块):
                    assert sep == 小块[:-1]
                    begin_pt = 0
                    end_pt = 1+ord(小块[-1])
                elif ((sep:=cls.连续符纟左闭右无穷区间) in 小块):
                    assert sep == 小块[1:]
                    begin_pt = ord(小块[0])
                    end_pt = CHAR_ORD_UPPER
                elif ((sep:=cls.连续符纟左闭右开区间) in 小块):
                    assert sep == 小块[1:-1]
                    begin_pt = ord(小块[0])
                    end_pt = ord(小块[-1])
                elif ((sep:=cls.连续符纟闭区间) in 小块):
                    assert sep == 小块[1:-1]
                    begin_pt = ord(小块[0])
                    end_pt = 1+ord(小块[-1])
                else:
                    raise 000
                begin_pt, end_pt
                起始位号 = 下一个位号
                数量 = end_pt-begin_pt
                if not 数量 >= 0:raise Exception(小块)
                it = iter([(起始位号, 数量, 起始字符编码点:=begin_pt)])
            return (数量, it)
        ######################
        def g(单区配置简易表达, /):
            '-> Iter (起始位号, 数量, 起始字符编码点)'
            下一个位号 = 0
            for 单块配置简易表达 in 单区配置简易表达.split(cls.分块符):
                assert '::' not in 单块配置简易表达
                for j, 小块 in enumerate(rex4sep.split(单块配置简易表达)):
                    欤连续块 = bool(j&1)
                    (数量, it) = f(下一个位号, 小块, 欤连续块)
                    yield from it
                    下一个位号 += 数量
        ######################
        def mk_mapping_(begin_sz_v_triples, /):
            d = StackStyleSimpleIntMapping()
            begin_sz_v_triples.sort()
            for begin,sz,v in begin_sz_v_triples:
                end = begin+sz
                rng = begin, end
                #if 0b0000:print_err((rng, v))
                d.push_rng_value(rng, v)
            d = d.to_TouchRangeBasedIntMapping()
            return d

        ######################
        ######################
        def main():
            # [位移量臫位号臸字符编码点 =[def]= 字符编码点-位号]
            #   因为 块状映射 要求 像纟块 一致
            区号讠位号讠位移量臸字符编码点 = []
            列表纟卂起始字符编码点丶数量丶卂区号丶位移量臫位号厈厈 = []
            for 区号,单区配置简易表达 in enumerate(区号讠单区配置简易表达):
                列表纟卂起始位号丶数量丶起始字符编码点厈 = [*g(单区配置简易表达)]
                列表纟卂起始位号丶数量丶位移量臸字符编码点厈 = [(j,sz,pt-j) for j,sz,pt in 列表纟卂起始位号丶数量丶起始字符编码点厈]
                位号讠位移量臸字符编码点 = mk_mapping_(列表纟卂起始位号丶数量丶位移量臸字符编码点厈)
                区号讠位号讠位移量臸字符编码点.append(位号讠位移量臸字符编码点)
                列表纟卂起始字符编码点丶数量丶卂区号丶位移量臫位号厈厈.extend((pt,sz,(区号,pt-j)) for j,sz,pt in 列表纟卂起始位号丶数量丶起始字符编码点厈)
            else:
                #不动区:
                单区配置简易表达 = 不动区配置简易表达
                区号 = -1
                列表纟卂起始位号丶数量丶起始字符编码点厈 = [*g(单区配置简易表达)]
                #列表纟卂起始字符编码点丶数量丶卂区号丶位移量臫位号厈厈.extend((pt,sz,(区号,pt-j)) for j,sz,pt in 列表纟卂起始位号丶数量丶起始字符编码点厈)
                    #位号无用，应该自动排序...
                def __():
                    列表纟卂起始位号丶数量丶起始字符编码点厈.sort(key=lambda t:t[-1])
                    j = 0
                    for _,sz,pt in 列表纟卂起始位号丶数量丶起始字符编码点厈:
                        yield (pt,sz,(区号,pt-j))
                        j += sz
                列表纟卂起始字符编码点丶数量丶卂区号丶位移量臫位号厈厈.extend(__())
            #==>>:
            区号讠位号讠位移量臸字符编码点
            列表纟卂起始字符编码点丶数量丶卂区号丶位移量臫位号厈厈
            字符编码点讠卂区号丶位移量臫位号厈 = mk_mapping_(列表纟卂起始字符编码点丶数量丶卂区号丶位移量臫位号厈厈)

            sf._区号讠位号讠位移量臸字符编码点 = 区号讠位号讠位移量臸字符编码点
                #to vivi:区号讠位号讠字符编码点
                #不含:无关码元#[区号>=0]
            sf._字符编码点讠卂区号丶位移量臫位号厈 = 字符编码点讠卂区号丶位移量臫位号厈
                #to vivi:字符编码点讠区位号
                #含:无关码元:[区号==-1]
            sf._args = 区号讠单区配置简易表达
            sf._kwds = dict(不动区配置简易表达=不动区配置简易表达) if 不动区配置简易表达 else {}
                #for:__repr__
            #if 0b0000:print_err(字符编码点讠卂区号丶位移量臫位号厈)

        main()
    def __repr__(sf, /):
        return repr_helper(sf, *sf._args, **sf._kwds)
    @classmethod
    def 构造冫区位配置巛多区配置简易表达扌(cls, 多区配置简易表达, 不动区配置简易表达, /):
        '多区配置简易表达 -> 不动区配置简易表达 -> 乸区位配置牜码元为字符编码点'
        #d = StackStyleSimpleIntMapping()
        #d.push_rng_value(rng, 区号)
        #d = d.to_TouchRangeBasedIntMapping()
        if type(多区配置简易表达) is str:
            多区配置简易表达 = 多区配置简易表达.split(cls.分区符)
        区号讠单区配置简易表达 = 多区配置简易表达
        return cls(*区号讠单区配置简易表达, 不动区配置简易表达=不动区配置简易表达)
    ######################
    #区号讠位数扌, 区数, 码元巛区位号扌, 码元讠鬽区位号扌
    @property
    @override
    def 区数(sf, /):
        '-> 区数/uint # [0 ~==~ +oo]'
        row2col2diff_by_pt = sf._区号讠位号讠位移量臸字符编码点
        return len(row2col2diff_by_pt)
    @override
    def 区号讠位数扌(sf, 区号, /):
        '区号/uint%区数 -> 位数乊区号/uint # [0 ~==~ +oo]'
        row2col2diff_by_pt = sf._区号讠位号讠位移量臸字符编码点
        return len(row2col2diff_by_pt[区号])
    @override
    def 码元讠鬽区位号扌(sf, 码元, /):
        '码元 -> may 区位号/(区号/uint%区数,位号/uint%位数乊区号) | ^LookupError'
        字符编码点 = 码元
        (区号,位移量臫位号) = sf._字符编码点讠卂区号丶位移量臫位号厈[字符编码点]
            #^KeyError
        if 区号 == -1:
            #不动区
            #无关码元
            return None
        位号 = 字符编码点-位移量臫位号
        assert 0 <= 位号 < sf.区号讠位数扌(区号)
        区位号 = (区号, 位号)
        return 区位号
    @override
    def 码元巛区位号扌(sf, 区位号, /):
        '区位号/(区号/uint%区数,位号/uint%位数乊区号) -> 码元'
        (区号, 位号) = 区位号
        check_int_ge(0, 区号)
        check_int_ge(0, 位号)

        row2col2diff_by_pt = sf._区号讠位号讠位移量臸字符编码点
        位移量臫位号臸字符编码点 = row2col2diff_by_pt[区号][位号]
        字符编码点 = 位号 + 位移量臫位号臸字符编码点
        码元 = 字符编码点
        return 码元
乸区位配置牜码元为字符编码点.正则表达式纟连续符 = 乸区位配置牜码元为字符编码点.构造冫正则表达式纟连续符扌()
#end-class 乸区位配置牜码元为字符编码点(魖区位配置):
class 乸匴加密牜防识别牜文本氺自定义数据牜区内变换乊孤码牜恒状态牜模加(魖匴加密牜防识别牜文本氺自定义数据牜区内变换乊孤码):
    __slots__ = ()
    def __repr__(sf, /):
        return repr_helper(sf)
    @override
    def 统计冫明文有效长度牜文本扌(sf, 囜文文本牜裸, /):
        '囜文文本牜裸/str -> 明文有效长度/uint'
        # !! [码元 :: ichr/unicode_pt/code_pt]
        囜文数据牜裸 = [*map(ord, 囜文文本牜裸)]
        明文有效长度 = sf.统计冫明文有效长度牜自定义数据扌(囜文数据牜裸)
        return 明文有效长度

    #@override
    匾协议 = 'mod_add'
    #@override
    区位配置 = 乸区位配置牜码元为字符编码点.构造冫区位配置巛多区配置简易表达扌('0..=9A..=Z::;_a..=z', r' +-#@%,.!?:;~$^&*[](){}<>|=\/')
    #
    #
    # [顺钥数据,逆钥数据 :: int] #允负
    # [码元 :: ichr/unicode_pt/code_pt]

    # 编码冫明文牜裸扌
    # 解码冫明文牜裸扌
    # 编码冫密文牜裸扌
    # 解码冫密文牜裸扌
    # 编码冫密文牜裹牜灬扌
    # 解码冫密文牜裹牜灬扌

    # 编码冫逆钥扌
    # 解码冫逆钥扌
    # 编码冫顺钥扌
    # 解码冫顺钥扌
    #
    #
    #
    # [状态乊位次保持 :: (顺钥数据,区号串乊位次保持)]
    # [状态乊位次变更 :: (区号串乊位次变更,逆钥数据)]
    # [索引置换牜顺向 == range(明文有效长度)]
    # [索引置换牜逆向 == 索引置换牜顺向]
    # [逆钥数据 == 顺钥数据]
    #
    # 注水解码冫状态乊位次保持扌
    # 注水解码冫状态乊位次变更扌
    # 脱水编码冫状态乊位次变更扌
    # 复位扌
    # 易位扌
    #
    #
    # 区内加密乊孤码扌
    # 区内解密乊孤码扌
    #
    #
    #
    @override
    def 解码冫逆钥扌(sf, 逆钥文本, /):
        '逆钥文本 -> 逆钥数据'
        逆钥数据 = int(逆钥文本, 10)
        return 逆钥数据
    @override
    def 编码冫逆钥扌(sf, 逆钥数据, /, *, validate):
        '逆钥数据 -> 逆钥文本'
        _validate = mk_validate4sub_call_(validate)
        check_type_is(int, 逆钥数据)
        逆钥文本 = str(逆钥数据)
        if validate:
            if not sf.解码冫逆钥扌(逆钥文本) == (逆钥数据):raise Exception((sf, (逆钥数据), (逆钥文本)))
        return 逆钥文本
    @override
    def 解码冫顺钥扌(sf, 顺钥文本, /, *, validate):
        '顺钥文本 -> 顺钥数据'
        #validate@解码向  <<== 此乃加密向
        _validate = mk_validate4sub_call_(validate)
        顺钥数据 = int(顺钥文本, 10)
        if validate:
            if not sf.编码冫顺钥扌(顺钥数据) == (顺钥文本):raise Exception((sf, (顺钥文本), (顺钥数据)))
        return 顺钥数据
    @override
    def 编码冫顺钥扌(sf, 顺钥数据, /):
        '顺钥数据 -> 顺钥文本'
        check_type_is(int, 顺钥数据)
        顺钥文本 = str(顺钥数据)
        return 顺钥文本
    @override
    def 解码冫明文牜裸扌(sf, 明文文本牜裸, /, *, validate):
        '明文文本牜裸 -> 明文数据牜裸'
        #validate@解码向  <<== 此乃加密向
        _validate = mk_validate4sub_call_(validate)
        明文数据牜裸 = tuple(map(ord, 明文文本牜裸))
        if validate:
            if not sf.编码冫明文牜裸扌(明文数据牜裸) == (明文文本牜裸):raise Exception((sf, (明文文本牜裸), (明文数据牜裸)))
        return 明文数据牜裸
    @override
    def 编码冫明文牜裸扌(sf, 明文数据牜裸, /):
        '明文数据牜裸 -> 明文文本牜裸'
        #bug:return tuple(map(chr, 明文数据牜裸))
        return ''.join(map(chr, 明文数据牜裸))
    ######################
    @override
    def 解码冫密文牜裸扌(sf, 密文文本牜裸, /):
        '密文文本牜裸 -> 密文数据牜裸'
        return tuple(map(ord, 密文文本牜裸))
    @override
    def 编码冫密文牜裸扌(sf, 密文数据牜裸, /, *, validate):
        '密文数据牜裸 -> 密文文本牜裸'
        #bug:return tuple(map(chr, 密文数据牜裸))
        _validate = mk_validate4sub_call_(validate)
        密文文本牜裸 = ''.join(map(chr, 密文数据牜裸))
        if validate:
            if not sf.解码冫密文牜裸扌(密文文本牜裸) == (密文数据牜裸):raise Exception((sf, (密文数据牜裸), (密文文本牜裸)))
        return 密文文本牜裸
    ######################
    @override
    def 解码冫密文牜裹牜灬扌(sf, 密文文本牜裹, /):
        '密文文本牜裹 -> (逆钥文本, 密文文本牜裸)'
        #解析/parse
        (逆钥文本, sep, 密文文本牜裸) = 密文文本牜裹.partition(':')
        if not sep:raise Exception((密文文本牜裹, ':'))
        return (逆钥文本, 密文文本牜裸)
    @override
    def 编码冫密文牜裹牜灬扌(sf, 逆钥文本, 密文文本牜裸, /, *, validate):
        '逆钥文本 -> 密文文本牜裸 -> 密文文本牜裹'
        #格式化/format
        _validate = mk_validate4sub_call_(validate)
        密文文本牜裹 = f'{逆钥文本}:{密文文本牜裸}'
        if validate:
            if not sf.解码冫密文牜裹牜灬扌(密文文本牜裹) == (逆钥文本, 密文文本牜裸):raise Exception((sf, (逆钥文本, 密文文本牜裸), (密文文本牜裹)))
        return 密文文本牜裹





    @override
    def 注水解码冫状态乊位次保持扌(sf, 顺钥数据, 区号串乊位次保持, /):
        '顺钥数据 -> 区号串乊位次保持/[区号] -> 状态乊位次保持'
        #本该:validate@解码向  <<== 此乃加密向
        #   但:没有相应的编码版！
        状态乊位次保持 = (顺钥数据,区号串乊位次保持)
        return 状态乊位次保持
    @override
    def 注水解码冫状态乊位次变更扌(sf, 区号串乊位次变更, 逆钥数据, /):
        '区号串乊位次变更/[区号] -> 逆钥数据 -> 状态乊位次变更'
        状态乊位次变更 = (区号串乊位次变更,逆钥数据)
        return 状态乊位次变更
    @override
    def 脱水编码冫状态乊位次变更扌(sf, 状态乊位次变更, /, *, validate):
        '状态乊位次变更 -> 逆钥数据'
        _validate = mk_validate4sub_call_(validate)
        (区号串乊位次变更,逆钥数据) = 状态乊位次变更
        if validate:
            if not sf.注水解码冫状态乊位次变更扌(区号串乊位次变更, 逆钥数据) == (状态乊位次变更):raise Exception((sf, (状态乊位次变更), 区号串乊位次变更, (逆钥数据)))
        return 逆钥数据
    @override
    def 易位扌(sf, 状态乊位次保持, /, *, validate):
        '状态乊位次保持 -> (状态乊位次变更, 索引置换牜顺向/[uint%明文有效长度])'
        # 不动:恒等变换
        _validate = mk_validate4sub_call_(validate)
        (顺钥数据,区号串乊位次保持) = 状态乊位次保持
        明文有效长度 = len(区号串乊位次保持)
        索引置换牜顺向 = range(明文有效长度)
        逆钥数据 = 顺钥数据
        区号串乊位次变更 = 置换扌(索引置换牜顺向,区号串乊位次保持)
        状态乊位次变更 = sf.注水解码冫状态乊位次变更扌(区号串乊位次变更,逆钥数据)
        if validate:
            if not sf.复位扌(状态乊位次变更) == (状态乊位次保持,索引置换牜逆向:=索引置换牜顺向):raise Exception((sf, (状态乊位次保持), (状态乊位次变更,索引置换牜顺向)))
        return (状态乊位次变更,索引置换牜顺向)
    @override
    def 复位扌(sf, 状态乊位次变更, /):
        '状态乊位次变更 -> (状态乊位次保持, 索引置换牜逆向/[uint%明文有效长度])'
        # 不动:恒等变换
        (区号串乊位次变更,逆钥数据) = 状态乊位次变更
        明文有效长度 = len(区号串乊位次变更)
        索引置换牜逆向 = range(明文有效长度)
            # 索引置换牜逆向 = 索引置换牜顺向
        区号串乊位次保持 = 置换扌(索引置换牜逆向,区号串乊位次变更)
        顺钥数据 = 逆钥数据
        状态乊位次保持 = sf.注水解码冫状态乊位次保持扌(顺钥数据, 区号串乊位次保持)
        return (状态乊位次保持, 索引置换牜逆向)






    def 罓区内变换乊孤码扌(sf, 序号纟码元匕有效明文, 状态乊位次保持, 位号, /, *, 加密丷解密):
        '序号纟码元匕有效明文 -> 状态乊位次保持 -> 位号 -> (状态乊位次保持, 位号)'
        #恒状态
        (顺钥数据,区号串乊位次保持) = 状态乊位次保持
        明文有效长度 = len(区号串乊位次保持)
        # !! 位号@序号纟码元匕有效明文
        区号 = 区号串乊位次保持[序号纟码元匕有效明文]
        位数乊区号 = sf.区位配置.区号讠位数扌(区号)
        n = 明文有效长度%位数乊区号
        i = 序号纟码元匕有效明文%位数乊区号
        j = 顺钥数据%位数乊区号
        k = (n+i+j)%位数乊区号
        if 加密丷解密:
            #解密
            k = -k
        位号 = (位号+k)%位数乊区号
        区号串乊位次保持#恒状态
        return (状态乊位次保持, 位号)
    @override
    def 区内加密乊孤码扌(sf, 序号纟码元匕有效明文, 状态乊位次保持, 位号, /, *, validate):
        '序号纟码元匕有效明文 -> 状态乊位次保持 -> 位号 -> (状态乊位次保持, 位号)'
        #恒状态
        _validate = mk_validate4sub_call_(validate)
        (_状态乊位次保持, _位号) = sf.罓区内变换乊孤码扌(序号纟码元匕有效明文, 状态乊位次保持, 位号, 加密丷解密=False)
        if validate:
            if not (状态乊位次保持, 位号) == sf.区内解密乊孤码扌(序号纟码元匕有效明文, _状态乊位次保持, _位号):raise Exception({**locals()})
        return (_状态乊位次保持, _位号)
    @override
    def 区内解密乊孤码扌(sf, 序号纟码元匕有效明文, 状态乊位次保持, 位号, /):
        '序号纟码元匕有效明文 -> 状态乊位次保持 -> 位号 -> (状态乊位次保持, 位号)'
        #恒状态
        return sf.罓区内变换乊孤码扌(序号纟码元匕有效明文, 状态乊位次保持, 位号, 加密丷解密=True)
    pass

#end-class 乸匴加密牜防识别牜文本氺自定义数据牜区内变换乊孤码牜恒状态牜模加(魖匴加密牜防识别牜文本氺自定义数据牜区内变换乊孤码):

匴加密牜防识别牜文本氺自定义数据牜区内变换乊孤码牜恒状态牜模加 = 乸匴加密牜防识别牜文本氺自定义数据牜区内变换乊孤码牜恒状态牜模加()
注册处纟加密牜防识别牜文本 = 乸注册处纟加密牜防识别牜文本()
注册处纟加密牜防识别牜文本.注册扌(匴加密牜防识别牜文本氺自定义数据牜区内变换乊孤码牜恒状态牜模加)


灬注册扌 = 注册处纟加密牜防识别牜文本.注册扌
灬查找扌 = 注册处纟加密牜防识别牜文本.查找扌
灬枚举冫匾协议乊已注册扌 = 注册处纟加密牜防识别牜文本.枚举冫匾协议乊已注册扌

灬加密冫明文文本牜裸裸扌 = 注册处纟加密牜防识别牜文本.加密冫明文文本牜裸裸扌
灬自解密冫密文文本牜裹裹扌 = 注册处纟加密牜防识别牜文本.自解密冫密文文本牜裹裹扌
灬简自解密冫密文文本牜裹裹扌 = 注册处纟加密牜防识别牜文本.简自解密冫密文文本牜裹裹扌

g_register_ = 灬注册扌
g_lookup_ = 灬查找扌
g_iter_nms4protocol_ = 灬枚举冫匾协议乊已注册扌
g_encrypt_ = 灬加密冫明文文本牜裸裸扌
g_self_decrypt__verbose_ = 灬自解密冫密文文本牜裹裹扌
g_self_decrypt__brief_ = 灬简自解密冫密文文本牜裹裹扌

def _try(注册处=注册处纟加密牜防识别牜文本, /):
    ###view ../../python3_src/nn_ns/math_nn/numbers/exponents4Mersenne_prime.py
    #-->
    #view ../../python3_src/nn_ns/math_nn/numbers/Mersenne_exponents.py
    _validate = -1
    匾协议 = 'mod_add'
    顺钥文本 = str(2**61 -1)
    明文文本牜裸 = '244:1341 - 0484$#'
    密文文本牜裹裹 = 注册处.加密冫明文文本牜裸裸扌(匾协议, 顺钥文本, 明文文本牜裸, validate=_validate)
    #if 0b0000:print_err((匾协议, 顺钥文本, 明文文本牜裸))
    #if 0b0000:print_err(密文文本牜裹裹)
    (_匾协议, 逆钥文本, _明文文本牜裸) = 注册处.自解密冫密文文本牜裹裹扌(密文文本牜裹裹)
    assert _匾协议 == 匾协议, (匾协议, _匾协议)
    assert _明文文本牜裸 == 明文文本牜裸, (明文文本牜裸, _明文文本牜裸)
    assert 逆钥文本 == 顺钥文本, (顺钥文本, 逆钥文本)
    assert 密文文本牜裹裹 == 'mod_add:2305843009213693951:WZ0:Y131 - 16B8$#', (顺钥文本, 密文文本牜裹裹)
    assert 顺钥文本 == '2305843009213693951', (顺钥文本, 密文文本牜裹裹)

    顺钥文本 = '19'
    密文文本牜裹裹 = 注册处.加密冫明文文本牜裸裸扌(匾协议, 顺钥文本, 明文文本牜裸, validate=_validate)
    assert 密文文本牜裹裹 == 'mod_add:19:WZ0:Y131 - 16B8$#', (顺钥文本, 密文文本牜裹裹)

    顺钥文本 = '1'
    密文文本牜裹裹 = 注册处.加密冫明文文本牜裸裸扌(匾协议, 顺钥文本, 明文文本牜裸, validate=_validate)
    assert 密文文本牜裹裹 == 'mod_add:1:EHI:GJLJ - JOTQ$#', (顺钥文本, 密文文本牜裹裹)

    匴加密 = 注册处.查找扌(匾协议)
    明文有效长度 = 匴加密.统计冫明文有效长度牜文本扌(明文文本牜裸)

    #顺钥文本 = str(-11) #11==(明文有效长度)
    顺钥文本 = str(-明文有效长度)
    密文文本牜裹裹 = 注册处.加密冫明文文本牜裸裸扌(匾协议, 顺钥文本, 明文文本牜裸, validate=_validate)
    assert 密文文本牜裹裹 == 'mod_add:-11:256:4797 - 7CHE$#', (顺钥文本, 密文文本牜裹裹)


#_try()
assert '!?^a' == (__:=匴转义冫超文本牜极简具现.转义冫超文本扌(['', ('a',)], validate=-1)), __

__all__

def g_encrypt_decrypt_(ed:'[+-]', msg, /, *, key='19', protocol='mod_add'):
    if ed == '+':
        #encrypt
        return g_encrypt_(protocol, key, msg, validate=1)
    elif ed == '-':
        #decrypt
        return g_self_decrypt__brief_(msg)
    else:
        raise Exception(f'[+-] not {ed!r}')

from seed.text.encrypt.anti_recognition_encrypt import g_encrypt_decrypt_

from seed.text.encrypt.anti_recognition_encrypt import g_register_, g_lookup_, g_iter_nms4protocol_, g_encrypt_, g_self_decrypt__verbose_, g_self_decrypt__brief_

from seed.text.encrypt.anti_recognition_encrypt import 灬加密冫明文文本牜裸裸扌,灬自解密冫密文文本牜裹裹扌,灬简自解密冫密文文本牜裹裹扌
from seed.text.encrypt.anti_recognition_encrypt import 灬注册扌,灬查找扌,灬枚举冫匾协议乊已注册扌
from seed.text.encrypt.anti_recognition_encrypt import 注册处纟加密牜防识别牜文本
from seed.text.encrypt.anti_recognition_encrypt import 匴加密牜防识别牜文本氺自定义数据牜区内变换乊孤码牜恒状态牜模加,乸区位配置牜码元为字符编码点
from seed.text.encrypt.anti_recognition_encrypt import 乸匴转义冫文本牜极简具现,乸匴转义冫超文本牜极简具现

from seed.text.encrypt.anti_recognition_encrypt import *
