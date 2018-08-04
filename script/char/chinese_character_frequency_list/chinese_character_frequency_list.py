
r'''
line format
    /* Columns are tab delimited. 行间分隔符为Tab键。*/
    /* 序列号	汉字	频率	累计频率(%)	拼音	英文翻译 */
'''

from seed.io.iter_line_contents import filter_line_contents \
    , beginswith_spaces_digit

ifname = r'汉字单字字频总表.txt'
iencoding = 'gb18030'

class Line:
    def __init__(self, serialNo, han, count, acc_frequency, pinyins, explains):
        self.serialNo = serialNo # begin from 0
        self.han = han
        self.count = count
        self.acc_frequency = acc_frequency
        self.pinyins = pinyins
        self.explains = explains
def iter_parse_file(fin):
    for line in filter_line_contents(fin, [beginswith_spaces_digit]):
        serialNo, han, count, acc_frequency, pinyins, explains = \
            line.split('\t')
        assert len(han) == 1
        serialNo = int(serialNo) - 1
        assert serialNo >= 0
        count = int(count)
        #acc_frequency = float(acc_frequency)
        #pinyins = pinyins.split('/')
        #explains = explains.split('/')
        line_obj = Line(serialNo=serialNo, han=han, count=count
                        , acc_frequency=acc_frequency
                        , pinyins=pinyins
                        , explains=explains)
        yield line_obj

def _make():
    with open(ifname, encoding=iencoding) as fin:
        line_objs = list(iter_parse_file(fin))
    assert all(obj.serialNo == i for i, obj in enumerate(line_objs))
    return line_objs

chinese_character_frequency_list = _make()




