
__all__ = '''
    calc_complete_normal_block_size
    calc_complete_super_block_size

    calc_complete_super_block_size__ver2_or_3
    calc_complete_super_block_size__ver1
    '''.split()

from .CalcCompleteNormalBlockSizeBase import CalcCompleteNormalBlockSizeBase
from .CalcCompleteSuperBlockSize__ver123 import (
    CalcCompleteSuperBlockSize_Ver1
    ,CalcCompleteSuperBlockSize_Ver2
    )
calc_complete_normal_block_size = \
    CalcCompleteNormalBlockSizeBase.calc_complete_normal_block_size


calc_complete_super_block_size__ver2_or_3 =\
    CalcCompleteSuperBlockSize_Ver2.calc_complete_super_block_size
calc_complete_super_block_size__ver1 =\
    CalcCompleteSuperBlockSize_Ver1.calc_complete_super_block_size

def calc_complete_super_block_size(array_length, superVersion=None):
    if superVersion is None or superVersion in [2,3]:
        f = calc_complete_super_block_size__ver2_or_3
    elif superVersion == 1:
        f = calc_complete_super_block_size__ver1
    else:
        raise Exception('unknown superVersion')
    return f(array_length)
