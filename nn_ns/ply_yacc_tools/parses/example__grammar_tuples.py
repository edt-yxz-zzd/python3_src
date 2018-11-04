grammar_tuples = r'''
DictBodyTailItem
    = +RawDictKey assign +Object
    | +Inline_CharString -colon +Object
Inline_DictItem
    = RawDictKey -assign Inline_Object
    | Inline_CharString -colon Inline_Object
a
    = b | c d | b c d
    | +b | +c +d | +b +c +d
    | -b | -c -d | -b -c -d
    | b | +c -d | -b +c -d
'''
