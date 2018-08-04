
from chars_of import *
from sand import all_encodings, std_encoding


def show_chars_of_latin_1():
    *cs, = chars_of('iso-8859-1')
    print(cs)
    return cs


def show_encoding_num_chars():
    for e in all_encodings:
        e = std_encoding(e)
        *cs, = chars_of(e)
        L = len(cs)
        print(e, L)
        
'''
ascii 128
big5 13834
big5hkscs 18514
cp037 256
cp424 218
cp437 256
cp500 256
cp720 256
cp737 256
cp775 256
cp850 256
cp852 256
cp855 256
cp856 215
cp857 253
cp858 256
cp860 256
cp861 256
cp862 256
cp863 256
cp864 250
cp865 256
cp866 256
cp869 247
cp874 225
cp875 250
cp932 9402
cp949 17176
cp950 13870
cp1006 255
cp1026 256
cp1140 256
cp1250 251
cp1251 255
cp1252 251
cp1253 239
cp1254 249
cp1255 233
cp1256 256
cp1257 244
cp1258 247
cp65001 1112064
euc_jp 13136
euc_jis_2004 14557
euc_jisx0213 14547
euc_kr 17175
gb2312 7573
gbk 21919
gb18030 1112064
hz 7572
iso2022_jp 7008
iso2022_jp_1 13074
iso2022_jp_2 18727
iso2022_jp_2004 11334
iso2022_jp_3 11323
iso2022_jp_ext 13137
iso2022_kr 8351
iso8859-1 256
iso8859-2 256
iso8859-3 249
iso8859-4 256
iso8859-5 256
iso8859-6 211
iso8859-7 253
iso8859-8 220
iso8859-9 256
iso8859-10 256
iso8859-13 256
iso8859-14 256
iso8859-15 256
iso8859-16 256
johab 17176
koi8-r 256
koi8-u 256
mac-cyrillic 256
mac-greek 256
mac-iceland 256
mac-latin2 256
mac-roman 256
mac-turkish 256
ptcp154 256
shift_jis 7070
shift_jis_2004 11399
shift_jisx0213 11389
utf-32 1114112
utf-32-be 1114112
utf-32-le 1114112
utf-16 1112064
utf-16-be 1112064
utf-16-le 1112064
utf-7 1114112
utf-8 1112064
utf-8-sig 1112064
'''

