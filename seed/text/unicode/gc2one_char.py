#__all__:goto
r'''[[[
e ../../python3_src/seed/text/unicode/gc2one_char.py
view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/xml/ver14_0_0/gc.General_Category.ver14_0_0.xml.out.txt
view ../../python3_src/nn_ns/CJK/unicode/ucd_unihan/parse__PropertyValueAliases_txt.py.out.ver14_0_0.txt

[[
explain naming:
    gc_va2one_char4ver14:
        General_Category.PropertyValueAlias to arbitrary char(indeed the first one) that has such PropertyValueAlias in Unicode ver14_0_0
]]


seed.text.unicode.gc2one_char
py -m nn_ns.app.debug_cmd   seed.text.unicode.gc2one_char -x
py -m nn_ns.app.doctest_cmd seed.text.unicode.gc2one_char:__doc__ -ht


py_adhoc_call   seed.text.unicode.gc2one_char   @generate_ex__gc2one_char__ver_   :ver14_0_0

{[(
>>> (r:=generate_ex__gc2one_char__ver_('ver14_0_0')) == (
... {'Cc': '\x00'
... ,'Cf': '\xad'
... ,'Cn': '\u0378'
... ,'Co': '\ue000'
... ,'Cs': '\ud800'
... ,'Ll': 'a'
... ,'Lm': 'ʰ'
... ,'Lo': 'ª'
... ,'Lt': 'ǅ'
... ,'Lu': 'A'
... ,'Mc': 'ः'
... ,'Me': '҈'
... ,'Mn': '̀'
... ,'Nd': '0'
... ,'Nl': 'ᛮ'
... ,'No': '²'
... ,'Pc': '_'
... ,'Pd': '-'
... ,'Pe': ')'
... ,'Pf': '»'
... ,'Pi': '«'
... ,'Po': '!'
... ,'Ps': '('
... ,'Sc': '$'
... ,'Sk': '^'
... ,'Sm': '+'
... ,'So': '¦'
... ,'Zl': '\u2028'
... ,'Zp': '\u2029'
... ,'Zs': ' '
... }
... , ('Cc', 'Cf', 'Cn', 'Co', 'Cs', 'Ll', 'Lm', 'Lo', 'Lt', 'Lu', 'Mc', 'Me', 'Mn', 'Nd', 'Nl', 'No', 'Pc', 'Pd', 'Pe', 'Pf', 'Pi', 'Po', 'Ps', 'Sc', 'Sk', 'Sm', 'So', 'Zl', 'Zp', 'Zs')
... , '\x00\xad\u0378\ue000\ud800aʰªǅAः҈̀0ᛮ²_-)»«!($^+¦\u2028\u2029 '
... )
True

)]}

>>> print(repr_str_by_uHHHH_UHHHHHHHH(r[-1]))
'\u0000\u00AD\u0378\uE000\uD800\u0061\u02B0\u00AA\u01C5\u0041\u0903\u0488\u0300\u0030\u16EE\u00B2\u005F\u002D\u0029\u00BB\u00AB\u0021\u0028\u0024\u005E\u002B\u00A6\u2028\u2029\u0020'


>>> r == (gc_va2one_char4ver14, vas4gc4ver14, chars4gc4ver14)
True




#]]]'''
__all__ = r'''
generate_ex__gc2one_char__ver_
    gc_va2one_char4ver14
    vas4gc4ver14
    chars4gc4ver14

'''.split()#'''
__all__
from seed.text.repr_str_by_uHHHH_UHHHHHHHH import repr_str_by_uHHHH_UHHHHHHHH

def generate_ex__gc2one_char__ver_(ver:'ver14_0_0', /):
    from nn_ns.CJK.unicode.ucd_unihan.xml.resource_loader import data_loader4depth2__literal_eval__u8 as _loader
    loaderX = getattr(_loader, ver)
    (va2hx2sz, ichr2va) = loaderX.gc
    gc_va2one_char = {va:chr(min(hx2sz)) for va, hx2sz in va2hx2sz.items()}
    vas4gc = tuple(sorted(va2hx2sz))
    chars4gc = ''.join(gc_va2one_char[va] for va in vas4gc)
    return (gc_va2one_char, vas4gc, chars4gc)


chars4gc4ver14 = '\u0000\u00AD\u0378\uE000\uD800\u0061\u02B0\u00AA\u01C5\u0041\u0903\u0488\u0300\u0030\u16EE\u00B2\u005F\u002D\u0029\u00BB\u00AB\u0021\u0028\u0024\u005E\u002B\u00A6\u2028\u2029\u0020'
assert chars4gc4ver14 == '\x00\xad\u0378\ue000\ud800aʰªǅAः҈̀0ᛮ²_-)»«!($^+¦\u2028\u2029 '

vas4gc4ver14 = ('Cc', 'Cf', 'Cn', 'Co', 'Cs', 'Ll', 'Lm', 'Lo', 'Lt', 'Lu', 'Mc', 'Me', 'Mn', 'Nd', 'Nl', 'No', 'Pc', 'Pd', 'Pe', 'Pf', 'Pi', 'Po', 'Ps', 'Sc', 'Sk', 'Sm', 'So', 'Zl', 'Zp', 'Zs')

gc_va2one_char4ver14 = ((
{'Cc': '\x00', 'Cf': '\xad', 'Cn': '\u0378', 'Co': '\ue000', 'Cs': '\ud800'
,'Ll': 'a', 'Lm': 'ʰ', 'Lo': 'ª', 'Lt': 'ǅ', 'Lu': 'A'
,'Mc': 'ः', 'Me': '҈', 'Mn': '̀'
,'Nd': '0', 'Nl': 'ᛮ', 'No': '²'
,'Pc': '_', 'Pd': '-', 'Pe': ')', 'Pf': '»', 'Pi': '«', 'Po': '!', 'Ps': '('
,'Sc': '$', 'Sk': '^', 'Sm': '+', 'So': '¦'
,'Zl': '\u2028', 'Zp': '\u2029', 'Zs': ' '
}))

__all__
from seed.text.unicode.gc2one_char import gc_va2one_char4ver14, vas4gc4ver14, chars4gc4ver14
from seed.text.unicode.gc2one_char import *
