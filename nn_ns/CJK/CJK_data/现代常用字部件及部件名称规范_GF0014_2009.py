

r"""

py -m nn_ns.CJK.CJK_data.现代常用字部件及部件名称规范_GF0014_2009
e ../../python3_src/nn_ns/CJK/CJK_data/现代常用字部件及部件名称规范_GF0014_2009.py
view ../../python3_src/nn_ns/CJK/CJK_data/output/handle_现代常用字部件表.py.out/现代常用字部件及部件名称规范_GF0014_2009_main_result.json.txt



现代常用字部件及部件名称规范_GF0014_2009_main_result
    现代常用字部件及部件名称规范_GF0014_2009_部件完整属性列表
        :: [属性]{514}
    现代常用字部件笔画序检索表_笔画数到部件名列表
        :: {uint:[部件名]}{15}
        :: {uint_str:[部件名]}{15}
属性
    俗称
    出现次数
    到主形
    单笔
    字
    常用成字
    常用成字_我的判断
    成字
    构字数
    笔画数
    笔画顺序
    简洁部件名
    部件名
    部件序号
    部件组号

#"""



__all__ = '''
    现代常用字部件及部件名称规范_GF0014_2009_main_result
        现代常用字部件及部件名称规范_GF0014_2009_部件完整属性列表
        现代常用字部件笔画序检索表_笔画数到部件名列表
    '''.split()






##section##
r"""
import io
import re
from seed.tiny import print_err
#"""

import json
from seed.io.with_text_input_file import with_text_input_file__path
from types import MappingProxyType #frozenset




##section##
class Globals:
    import nn_ns.CJK.CJK_data.raw as raw
    from pathlib import Path
    [raw_path] = raw.__path__
    部件_json_path = Path(raw_path) / r"../output/handle_现代常用字部件表.py.out/现代常用字部件及部件名称规范_GF0014_2009_main_result.json.txt"
    r"""
    #"""

def _read(部件_json_path):
    return with_text_input_file__path(部件_json_path, json.load, None, encoding="utf8", yield_from=False)

def _tr(现代常用字部件及部件名称规范_GF0014_2009_部件完整属性列表
        ,现代常用字部件笔画序检索表_笔画数到部件名列表
        ):
    r"""
    现代常用字部件及部件名称规范_GF0014_2009_部件完整属性列表
        :: [属性]{514}
    现代常用字部件笔画序检索表_笔画数到部件名列表
        :: {uint:[部件名]}{15}
        :: {uint_str:[部件名]}{15}
    #"""
    assert len(现代常用字部件及部件名称规范_GF0014_2009_部件完整属性列表) == 514
    assert len(现代常用字部件笔画序检索表_笔画数到部件名列表) == 15

    ds = tuple(map(MappingProxyType, 现代常用字部件及部件名称规范_GF0014_2009_部件完整属性列表))
    assert len(ds) == 514
    assert len(ds[0]) == 15

    lss = [None]*len(现代常用字部件笔画序检索表_笔画数到部件名列表)
    for k,ls in 现代常用字部件笔画序检索表_笔画数到部件名列表.items():
        i = int(k)
        assert i >= 0
        lss[i] = tuple(ls)
    lss = tuple(lss)
    assert len(lss) == 15

    return MappingProxyType(dict(
        现代常用字部件及部件名称规范_GF0014_2009_部件完整属性列表=ds
        ,现代常用字部件笔画序检索表_笔画数到部件名列表=lss
        ))

现代常用字部件及部件名称规范_GF0014_2009_main_result = _tr(**_read(Globals.部件_json_path))

globals().update(现代常用字部件及部件名称规范_GF0014_2009_main_result)

现代常用字部件及部件名称规范_GF0014_2009_部件完整属性列表
现代常用字部件笔画序检索表_笔画数到部件名列表

assert len(现代常用字部件及部件名称规范_GF0014_2009_main_result) == 2
assert len(现代常用字部件及部件名称规范_GF0014_2009_部件完整属性列表) == 514
assert len(现代常用字部件及部件名称规范_GF0014_2009_部件完整属性列表[0]) == 15
assert len(现代常用字部件笔画序检索表_笔画数到部件名列表) == 15


if __name__ == "__main__":
    for k in sorted(现代常用字部件及部件名称规范_GF0014_2009_main_result):
        print(k)
    print("="*30)
    for k in sorted(现代常用字部件及部件名称规范_GF0014_2009_部件完整属性列表[0]):
        print(k)






