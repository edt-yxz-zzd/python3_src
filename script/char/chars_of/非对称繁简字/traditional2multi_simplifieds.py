
一繁对多简 = r'''
http://www.qqxiuzi.cn/wz/jiantizi-fantizi/227.htm
繁简转换一繁对多简列表，共十余组

发布时间 2012-05-29
在汉字的简化过程中，有少量繁体字被简化成了两个简体字。依据不同的组字用意分别用字。例如繁体字“著”被简化为“著”与“着”两个字，“著作”和“睡着了”就是依据字意的分别用法。

繁体字转换成简体字过程中出现的一繁对多简用字基本上都是一对二，数量也不多，共有十余组。以下是一繁对多简列表。

著→著着
兒→兒儿
乾→乾干
夥→夥伙
藉→藉借
瞭→瞭了
餘→馀余
摺→摺折
徵→徵征
畫→画划
鯰→鲶鲇
瀋→沈渖
鹼→碱硷
蘋→苹蘋
麼→麽么
剋→克剋
'''

import io
from seed.io.iter_line_contents import filter_py_line_contents

total = 16

_sep = '→'
def _iter_t_ss_pairs():
    i = 一繁对多简.find('著→著着')
    fin = io.StringIO(一繁对多简[i:])
    for line in filter_py_line_contents(fin):
        if _sep in line:
            t_char, s_str = line.split(_sep)
            yield t_char, s_str
        else:
            assert False

traditional2multi_simplifieds = dict(_iter_t_ss_pairs())
assert total == len(traditional2multi_simplifieds)
if __name__ == "__main__":
    from pprint import pprint
    pprint(traditional2multi_simplifieds)


