
from std_chars import std_chars
from seed.io.with_file import to_with_file
def exclude_chars__str(s1, s2):
    return std_chars(set(s1) - set(s2))
def exclude_chars__file(fname1, encoding1, fname2, encoding2, fout, encoding3):
    ''
    f1 = to_with_file(fname1, encoding = encoding1)
    f2 = to_with_file(fname2, encoding = encoding2)
    f3 = to_with_file(fname3, 'x', encoding = encoding3)
    with f1 as f1, f2 as f2, f3 as f3:
        s1 = f1.read()
        s2 = f2.read()
        s3 = exclude_chars__str(s1, s2)
        f3.write(s3)

def intersection(goods, string):
    return std_chars(set(string) & set(goods))



from common_CJK_noSimilar_han_chars_exclude_vary_chars import \
    common_CJK_noSimilar_han_chars_exclude_all_chars_with_variant as s1
maybe_tags_strs = r'''
如是我闻
一切有为法……应作如是观。
据路边社报道、号外、搞个大新闻
亲爱的……此致
……临表涕零
奉天承运皇帝诏曰……钦此
子曰……成仁、诗云、爱问、子不语
阿二不曾说：

话说天下大势……都付笑谈中
冤枉啊大人
异史氏曰
'''

if 0:
    s2 = maybe_tags_strs
    s3 = intersection(s2, s1)
    print(repr(s3))
    for s2_ in s2.split('\n'):
        s3_ = intersection(s2_, s3)
        print(repr(s3_))

    '付作史大奉如帝成我承新有枉此氏法的皇社道'
    ''
    '如我'
    '作如有法'
    '大新社道'
    '此的'
    ''
    '奉帝承此皇'
    '成'
    ''
    ''
    '付大'
    '大枉'
    '史氏'
    ''


#cmd parser
def main(argv=None):
    ...
if __name__ == '__main__':
    main()

