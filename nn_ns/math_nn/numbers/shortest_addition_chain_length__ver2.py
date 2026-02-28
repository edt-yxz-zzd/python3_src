#__all__:goto
#保留此文件<<==仍被使用:_解读冫编码值讠最小显链长纟靶值扌()
r'''[[[
e ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain_length__ver2.py
    [1..=7320000]#未能获取所有所得数据牜通过程序解压残损下载文件
vs:
    view ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain_length.py
        静态加载:100000
    view ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain_length__ver2.py
        惰性完整加载:7320000
    view ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain_length__ver3.py
        动态逐项加载:7322932


nn_ns.math_nn.numbers.shortest_addition_chain_length__ver2
py -m nn_ns.app.debug_cmd   nn_ns.math_nn.numbers.shortest_addition_chain_length__ver2 -x # -off_defs
py -m nn_ns.app.doctest_cmd nn_ns.math_nn.numbers.shortest_addition_chain_length__ver2:__doc__ -ht # -ff -df
#######

[[
view script/解读冫二进制文件冃靶值讠最小显链长.py
    see:转换格式丶打包存档
du -h ../../python3_src/nn_ns/math_nn/numbers/偏移值文本冃靶值讠最小显链长.le7320000.txt.txz
    712K
du -h ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain_length.py
    912K
]]


'#'; __doc__ = r'#'


>>> (100000).bit_length()
17
>>> 2**16 < 100000 < 2**17
True
>>> 100000 - 2**16
34464
>>> 100000 - 2**17
-31072

>>> (7320000).bit_length()
23
>>> 2**22 < 7320000 < 2**23
True
>>> 7320000 - 2**22
3125696
>>> 7320000 - 2**23
-1068608


timeit(stmt='pass', setup='pass', timer=<built-in function perf_counter>, number=1000000, globals=None)
>>> from timeit import timeit
>>> from nn_ns.math_nn.numbers.shortest_addition_chain_length__ver2 import 取冫靶值讠最小显链长扌
>>> timeit(取冫靶值讠最小显链长扌, number=1)      #doctest: +SKIP
8.247884692624211   #使用pickle前
0.4560535401105881  #使用pickle后
0.31606284715235233 #使用pickle后

#解码加载:耗时8秒！-->读缓存文件:半秒
    DONE:_ignore__tmp/解包后缓存
du -h ../../python3_src/nn_ns/math_nn/numbers/_ignore__tmp/靶值讠最小显链长.le7320000.pickle
    14M

>>> 靶值讠最小显链长 = 取冫靶值讠最小显链长扌(deprecated=False)
>>> len(靶值讠最小显链长)
7320001
>>> 靶值讠最小显链长[:31]
(None, 0, 1, 2, 2, 3, 3, 4, 3, 4, 4, 5, 4, 5, 5, 5, 4, 5, 5, 6, 5, 6, 6, 6, 5, 6, 6, 6, 6, 7, 6)
>>> 靶值讠最小显链长[-30:]
(28, 27, 28, 28, 28, 27, 28, 28, 28, 28, 28, 28, 28, 27, 28, 28, 28, 27, 28, 28, 28, 27, 28, 28, 28, 28, 28, 28, 28, 27)
>>> 靶值讠最小显链长扌(7320000, deprecated=False)
27
>>> 靶值讠最小显链长扌(7320001, deprecated=False)
Traceback (most recent call last):
    ...
IndexError: tuple index out of range


>>> 取冫靶值讠最小显链长扌()
Traceback (most recent call last):
    ...
DeprecationWarning: now use ver3 instead of ver2
>>> 靶值讠最小显链长扌(1)
Traceback (most recent call last):
    ...
DeprecationWarning: now use ver3 instead of ver2


py_adhoc_call   nn_ns.math_nn.numbers.shortest_addition_chain_length__ver2   @删除冫缓存文件扌
    现使用ver3
        !! 缓存文件太大=>影响grep搜索...

]]]'''#'''
__all__ = r'''
取冫靶值讠最小显链长扌
靶值讠最小显链长扌
删除冫缓存文件扌
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.from itertools import islice
from seed.tiny_.check import check_type_is, check_int_ge
___end_mark_of_excluded_global_names__0___ = ...

def 靶值讠最小显链长扌(靶值, /, *, deprecated=True):
    check_int_ge(1, 靶值)
    靶值讠最小显链长 = 取冫靶值讠最小显链长扌(deprecated=deprecated)
    return 靶值讠最小显链长[靶值]

if 0:
    _靶值讠最小显链长 = ...
def 取冫靶值讠最小显链长扌(*, deprecated=True):
    if deprecated:
        raise DeprecationWarning('now use ver3 instead of ver2')#DeprecatedError
    try:
        return _靶值讠最小显链长
    except NameError:
        pass
    _加载冫靶值讠最小显链长扌()
    return 取冫靶值讠最小显链长扌(deprecated=deprecated)

def _加载冫靶值讠最小显链长扌():
    global _靶值讠最小显链长
    #if __name__ == '__main__':
    if not __name__ == 'nn_ns.math_nn.numbers.shortest_addition_chain_length__ver2':
        from nn_ns.math_nn.numbers.shortest_addition_chain_length__ver2 import 取冫靶值讠最小显链长扌
        _靶值讠最小显链长 = 取冫靶值讠最小显链长扌()
        return
    #####
    (path4pkg, path4cache) = _构造冫路径纟库目录丶路径纟缓存文件扌()
        #path4cache:ipath4cache&opath4cache

    if not path4cache.exists():
        ibasename = '偏移值文本冃靶值讠最小显链长.le7320000.txt.txz'
        ipath4tar = path4pkg / ibasename
        _生成冫缓存文件冃靶值讠最小显链长扌(ipath4tar, path4cache)

    _靶值讠最小显链长 = _读取冫缓存文件冃靶值讠最小显链长扌(path4cache)
    assert len(_靶值讠最小显链长) == 1+7320000
    assert _靶值讠最小显链长[0] is None
    return

def _构造冫路径纟库目录丶路径纟缓存文件扌():
    from pathlib import Path
    basename = '靶值讠最小显链长.le7320000.pickle'
    path4pkg = Path(__file__).parent
    path4cache = path4pkg / '_ignore__tmp' / basename
    return (path4pkg, path4cache)
def 删除冫缓存文件扌(*, nonexisted_ok=False):
    (path4pkg, path4cache) = _构造冫路径纟库目录丶路径纟缓存文件扌()
    if path4cache.exists():
        if not path4cache.is_file():
            raise IsADirectoryError(path4cache)
        else:
            path4cache.unlink()
        pass
    else:
        if nonexisted_ok:
            pass
        else:
            #import sys; print(, file=sys.stderr)
            raise FileNotFoundError(path4cache)
        pass
    pass


def _生成冫缓存文件冃靶值讠最小显链长扌(ipath4tar, opath4cache, /):
    import pickle
    if opath4cache.exists(): raise FileExistsError(opath4cache)
    靶值讠最小显链长 = _解码冫靶值讠最小显链长扌(ipath4tar)
    with open(opath4cache, 'xb') as ofile:
        pickle.dump(靶值讠最小显链长, ofile, fix_imports=False)

def _读取冫缓存文件冃靶值讠最小显链长扌(ipath4cache, /):
    import pickle
    with open(ipath4cache, 'rb') as ifile:
        靶值讠最小显链长 = pickle.load(ifile, fix_imports=False)
    return 靶值讠最小显链长

def _解码冫靶值讠最小显链长扌(ipath4tar, /):
    '-> 靶值讠最小显链长'
    from seed.for_libs.for_tarfile import iter_read_solo_tarfile_
    it = iter_read_solo_tarfile_(ipath4tar, xencoding4data='ascii')
    def f():
        ord_0 = ord('0')
        yield None
        for 靶值, line in enumerate(it, 1):
            ch = line.strip()
            编码值 = ord(ch) -ord_0
            if not 0 <= 编码值 <= 9:raise NotImplementedError
            最小显链长纟靶值 = _解读冫编码值讠最小显链长纟靶值扌(靶值, 编码值)
            yield 最小显链长纟靶值
    靶值讠最小显链长 = tuple(f())
    return 靶值讠最小显链长

def _解读冫编码值讠最小显链长纟靶值扌(靶值, 编码值, /):
    'copy from:view script/解读冫二进制文件冃靶值讠最小显链长.py'
    check_int_ge(1, 靶值)
    首爻位纟靶值 = -1+靶值.bit_length()
    阳爻数纟靶值 = 靶值.bit_count()

    首爻位纟阳爻数纟靶值 = -1+阳爻数纟靶值.bit_length()
    阳爻数纟阳爻数纟靶值 = 阳爻数纟靶值.bit_count()

    欤阳爻数是二幂 = (阳爻数纟阳爻数纟靶值 == 1)
    ceil_log2_阳爻数纟靶值 = 首爻位纟阳爻数纟靶值 +(1-欤阳爻数是二幂)
    最小显链长纟靶值 = 首爻位纟靶值 +ceil_log2_阳爻数纟靶值 +编码值
    return 最小显链长纟靶值


__all__
from nn_ns.math_nn.numbers.shortest_addition_chain_length__ver2 import 取冫靶值讠最小显链长扌, 靶值讠最小显链长扌
if 1:from nn_ns.math_nn.numbers.shortest_addition_chain_length__ver2 import _解读冫编码值讠最小显链长纟靶值扌
    #used by: view ../../python3_src/nn_ns/math_nn/numbers/shortest_addition_chain_length__ver3.py
    #def _解读冫编码值讠最小显链长纟靶值扌(靶值, 编码值, /):
from nn_ns.math_nn.numbers.shortest_addition_chain_length__ver2 import *
