

__all__ = '''
    CalcCompleteNormalBlockSize__superVer1
    CalcCompleteNormalBlockSize__superVer2
    '''.split()

from abc import ABC, abstractmethod
from itertools import count
from math import *
from .CalcCompleteSuperBlockSize__ver123 import (
    CalcCompleteSuperBlockSize_Ver1
    ,CalcCompleteSuperBlockSize_Ver2
    )
from .CalcCompleteNormalBlockSizeBase import CalcCompleteNormalBlockSizeBase
from .common_methods import floor_log2, ceil_log2

class CalcCompleteNormalBlockSize__superVer1(
        CalcCompleteSuperBlockSize_Ver1, CalcCompleteNormalBlockSizeBase):
    pass
class CalcCompleteNormalBlockSize__superVer2(
        CalcCompleteSuperBlockSize_Ver2, CalcCompleteNormalBlockSizeBase):
    pass


def calc_complete_normal_block_size(*, print=print, begin=1, size=100):
    assert begin > 0
    assert size >= 0
    C1 = CalcCompleteNormalBlockSize__superVer1
    C2 = CalcCompleteNormalBlockSize__superVer2
    print(f'calc_complete_normal_block_size(begin={begin})')
    print('array_length, complete_normal_block_size__ver1, ...ver2')
    for p in range(begin, begin+size):
        s1 = C1.calc_complete_normal_block_size(p)
        s2 = C2.calc_complete_normal_block_size(p)
        print(p, s1, s2)

def calc_min_array_length_and_delta_y__upper_bound():
    CalcCompleteNormalBlockSize__superVer1.calc_min_array_length_and_delta_y__upper_bound()
    print('\n'*3)
    CalcCompleteNormalBlockSize__superVer2.calc_min_array_length_and_delta_y__upper_bound()

if '__main__' == __name__:
    calc_complete_normal_block_size()
    print('\n'*3)
    calc_min_array_length_and_delta_y__upper_bound()

