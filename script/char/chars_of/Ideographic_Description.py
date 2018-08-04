'''

Unicode-8.0.pdf::18 East Asia::18.2 Ideographic Description Characters
Ideographic Description: U+2FF0–U+2FFB
Ideographic Description Sequence (IDS)
IDS := Ideographic| Radical|CJK_Stroke |Private Use | U+FF1F
    |IDS_BinaryOperator IDS IDS
    |IDS_TrinaryOperator IDS IDS IDS
CJK_Stroke := U+31C0 | U+31C1 | ... | U+31E3
IDS_BinaryOperator := U+2FF0 | U+2FF1 | U+2FF4 | U+2FF5 | U+2FF6 | U+2FF7 | 
    U+2FF8 | U+2FF9 | U+2FFA | U+2FFB
IDS_TrinaryOperator:= U+2FF2 | U+2FF3
'''

IDS_Operator = ''.join(map(chr, range(0x2FF0, 0x2FFB+1)))


assert '⿰⿱⿲⿳⿴⿵⿶⿷⿸⿹⿺⿻' == IDS_Operator
try:
    IDS_Operator.encode('gbk')
    raise logic-error # cannot encoded by 'gbk'
except UnicodeEncodeError:
    pass


bs = IDS_Operator.encode('gb18030')
assert len(bs) == len(IDS_Operator) * 2









