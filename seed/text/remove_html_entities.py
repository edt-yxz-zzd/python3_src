
__all__ = ['html_entity_rex', 'remove_html_entities']

import re
from html.entities import entitydefs as name2txt
from .. import zh_cn2ascii__translate_map

pattern = '|'.join(['[&﹠＆][#﹟＃]((\d|[０-９0-9])+)[;﹔；]?',
                    '[&﹠＆][#﹟＃][xXｘＸ]((\d|[０-９0-9a-fA-Fａ-ｆＡ-Ｆ])+)[;﹔；]?',
                    '[&﹠＆]([a-zA-Zａ-ｚＡ-Ｚ]+)[;﹔；]?',
                    ]
                   )

html_entity_rex = re.compile(pattern)

def _translate(s):
    return s.translate(zh_cn2ascii__translate_map)

def _replace(match_obj):
    original_str = match_obj.group(0)
    digits, xdigits, name = map(_translate, match_obj.group(1,3,5))
    if digits is not None:
        return chr(int(digits))
    elif xdigits is not None:
        return chr(int(xdigits, base = 16))
    elif name is not None:
        txt = name2txt.get(name, None)
        if txt is None:
            txt = name2txt.get(name+';', original_str)
        return txt
    
    raise logic-error

def remove_html_entities(txt):
    return html_entity_rex.sub(_replace, txt)

_test_data = ['&gt;', '&#100', '&#x3a3']

if 0:
    for s in _test_data:
        m = html_entity_rex.match(s)
        print(m.group(1,3,5))

    print(remove_html_entities(''.join(_test_data)))











