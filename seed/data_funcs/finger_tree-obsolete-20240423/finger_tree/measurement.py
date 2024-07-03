#__all__:goto
r'''[[[
e ../../python3_src/seed/data_funcs/finger_tree/measurement.py

cached_measurement
#caching measurement
Measured


seed.data_funcs.finger_tree.measurement
py -m nn_ns.app.debug_cmd   seed.data_funcs.finger_tree.measurement -x
py -m nn_ns.app.doctest_cmd seed.data_funcs.finger_tree.measurement:__doc__

#]]]'''
__all__ = r'''
乸词典映射冃缓存度量
    乸词典映射冃缓存度量囗囗长度丶散列值
        加法零元囗囗长度丶散列值

'''.split()#'''
__all__

from seed.helper.repr_input import repr_helper
from seed.tiny import check_type_is
from seed.types.FrozenDict import FrozenDict, mk_FrozenDict
import sys #hash_info
_模数 = sys.hash_info.modulus
    # [2**61-1 == 2305843009213693951]
    # [2**60-1 == II__p2e_({3: 2, 5: 2, 7: 1, 11: 1, 13: 1, 31: 1, 41: 1, 61: 1, 151: 1, 331: 1, 1321: 1})]
    # [(2**61-1) == 1 + II__p2e_({2: 1, 3: 2, 5: 2, 7: 1, 11: 1, 13: 1, 31: 1, 41: 1, 61: 1, 151: 1, 331: 1, 1321: 1})]
    # [37 is min primitive root of (2**61-1)]
    #
#_基数 = sys.hash_info.inf
_基数 = 37

__all__
class 乸词典映射冃缓存度量:
    r'''[[[

    [属性索引讠加法零元 :: 完整{属性索引:加法零元}]

    [例外囗属性索引讠鬽超加法 :: 部分{属性索引:may 超加法}]
        部分:不完整-缺省:加法 使用 py.__all__
        may 缺省:使用getattr(self,f'add4{属性索引}_')(other)
        [超加法 :: 属性索引 -> self/乸词典映射冃缓存度量 -> other/乸词典映射冃缓存度量 -> 属性值<属性索引>]

    #]]]'''#'''
    属性索引讠加法零元 = mk_FrozenDict()
    例外囗属性索引讠鬽超加法 = mk_FrozenDict()
    @property
    def 属性索引讠属性值(sf, /):
        return sf._k2v
    def __init__(sf, 属性索引讠属性值=None, /):
        if 属性索引讠属性值 is None:
            属性索引讠属性值 = sf.属性索引讠加法零元

        sf._k2v = mk_FrozenDict(属性索引讠属性值)
        if not sf._k2v.keys() == sf.属性索引讠加法零元.keys(): raise TypeError
    def __repr__(sf, /):
        return repr_helper(sf, {**sf._k2v})
    def keys(sf, /):
        return sf._k2v.keys()
    def items(sf, /):
        return sf._k2v.items()
    def __getitem__(sf, 属性索引, /):
        return sf._k2v[属性索引]
    def __len__(sf, /):
        return len(sf._k2v)
    def __hash__(sf, /):
        return hash(sf._k2v)
    def __eq__(sf, ot, /):
        if not isinstance(ot, type(sf)):
            return NotImplemented
        if not sf.属性索引讠加法零元 is ot.属性索引讠加法零元:raise TypeError
        return sf._k2v == ot._k2v
    def __add__(sf, ot, /):
        if not isinstance(ot, type(sf)):
            return NotImplemented
        if not sf.属性索引讠加法零元 is ot.属性索引讠加法零元:raise TypeError
        def f():
            例外 = sf.例外囗属性索引讠鬽超加法
            for k, v4sf in sf.items():
                if k in 例外:
                    鬽囗超加法 = 例外[k]
                    if 鬽囗超加法 is None:
                        check_type_is(str, k)
                        nm = f'add4{k}_'
                        v = getattr(sf, nm)(ot)
                    else:
                        超加法 = 鬽囗超加法
                        v = 超加法(k, sf, ot)
                    v
                else:
                    v = v4sf + ot[k]
                v
                yield k, v
        return type(sf)(f())
    __radd__ = __add__




__all__
class 乸词典映射冃缓存度量囗囗长度丶散列值(乸词典映射冃缓存度量):
    属性索引讠加法零元 = mk_FrozenDict(len=0, hash=0, shift_radix4hash=1)
    例外囗属性索引讠鬽超加法 = mk_FrozenDict(hash=None, shift_radix4hash=lambda nm,sf,ot:(sf[nm]*ot[nm])%_模数)
    def add4hash_(sf, ot, /):
        左囗高位偏移量 = sf['shift_radix4hash']
        左囗散列值 = sf['hash']
        右囗散列值 = ot['hash']
        左囗长度 = sf['len']
        #假设 多项式 从左往右 k增: x**k
        return (左囗散列值+右囗散列值*左囗高位偏移量) %_模数
        return (左囗散列值+右囗散列值*pow(_基数, 左囗长度, _模数)) %_模数
乸词典映射冃缓存度量._基数_ = _基数
    #计算 单元素 shift_radix4hash 时 要用的 『_基数_』，必须 引出

加法零元囗囗长度丶散列值 = 乸词典映射冃缓存度量囗囗长度丶散列值()


__all__


from seed.data_funcs.finger_tree.measurement import 乸词典映射冃缓存度量, 乸词典映射冃缓存度量囗囗长度丶散列值, 加法零元囗囗长度丶散列值
from seed.data_funcs.finger_tree.measurement import *
