
__all__ = ['CalcCompleteSuperBlockSizeBase']

from abc import ABC, abstractmethod
from itertools import count
from math import *
class CalcCompleteSuperBlockSizeBase(ABC):
    '''to calc min_array_length, delta_x__upper_bound, complete_super_block_size

1) min_array_length = calc_min_array_length()
2) delta_x__upper_bound = calc_delta_x__upper_bound(min_array_length)
3) complete_super_block_size = calc_complete_super_block_size(array_length)
see:
    .calc_min_array_length_and_delta_x__upper_bound
    .calc_complete_super_block_size
'''
    @classmethod
    @abstractmethod
    def get_version(cls):
        raise NotImplementedError
    @classmethod
    @abstractmethod
    def calc_complete_super_block_size(cls, array_length):
        assert array_length >= 1
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def get_min_array_length__at_least__from123xxx(cls):
        raise NotImplementedError
    @classmethod
    @abstractmethod
    def delta_x__upper_bound_at_least2__p_ge(cls, min_array_length):
        raise NotImplementedError

    min_array_length__at_least1 = 2
    min_array_length__at_least2 = 4
    min_array_length__at_least3 = 17
    min_array_length__at_least4 = 36


    @classmethod
    def calc_min_array_length(cls, *, print=print, begin=0):
        '''
        min_array_length = min {p | p <- [min_array_length__at_least__from123xxx..]
            , delta_x__upper_bound_at_least__p_ge(p) < delta_x__upper_bound_at_most__p_ge(p)
            }
    '''
        if print is None:
            def print(*args, **kwargs):pass

        print('array_length p, at_least, at_most')
        for p in count(max(begin, cls.get_min_array_length__at_least__from123xxx())):
            at_least = cls.delta_x__upper_bound_at_least__p_ge(p)
            at_most = cls.delta_x__upper_bound_at_most__p_ge(p)
            print(p, at_least, at_most)
            if at_least < at_most:
                return p


    @classmethod
    def calc_delta_x__upper_bound(cls, min_array_length):
        '''
        delta_x__upper_bound = delta_x__upper_bound_at_least__p_ge(min_array_length)
    '''
        return cls.delta_x__upper_bound_at_least__p_ge(min_array_length)



    @classmethod
    def delta_x__upper_bound_at_least__p_ge(cls, min_array_length):
        '''
        delta_x__upper_bound_at_least__p_ge(min_array_length)
            = max delta_x__upper_bound_at_least1__p_ge(min_array_length)
                  delta_x__upper_bound_at_least2__p_ge__verX(min_array_length)
    '''
        return max(
            cls.delta_x__upper_bound_at_least1__p_ge(min_array_length)
            ,cls.delta_x__upper_bound_at_least2__p_ge(min_array_length)
            )

    @classmethod
    def delta_x__upper_bound_at_most__p_ge(cls, min_array_length):
        '''
        delta_x__upper_bound_at_most__p_ge(min_array_length)
            = min {delta_x__at_most_for_p(p) | p <- [min_array_length..]}
            # p>=7, at_most(p) growing
            = delta_x__at_most_for_p(min_array_length)
            = log<log2(min_array_length)>(min_array_length)-2
    '''
        return log(min_array_length, log2(min_array_length))-2

    @classmethod
    def delta_x__upper_bound_at_least1__p_ge(cls, min_array_length):
        '''
    delta_x__upper_bound_at_least1__p_ge(min_array_length)
        = delta_x(p == min {p|p <- [min_array_length..], p==2**power})
        = delta_x(p == 2**ceil_log2(min_array_length))
        = log<min_b>(1+1/min_b**2)
        = log<ceil_log2(min_array_length)>(1+1/ceil_log2(min_array_length)**2)
    '''
        power = ceil(log2(min_array_length))
        return log(1+1/power**2, power)

    @classmethod
    def calc_min_array_length_and_delta_x__upper_bound(cls, *, print=print, begin=0, N=20):
        ver = cls.get_version()
        print(f'calc_min_array_length_and_delta_x__upper_bound(ver = {ver})')
        min_array_length = cls.calc_min_array_length(print=print, begin=begin)
        delta_x__upper_bound = cls.calc_delta_x__upper_bound(min_array_length)

        print()
        print(min_array_length, delta_x__upper_bound)
        print()

        for p in range(min_array_length, min_array_length+N):
            at_least = cls.delta_x__upper_bound_at_least__p_ge(p)
            at_most = cls.delta_x__upper_bound_at_most__p_ge(p)
            print('\t', end='')
            print(p, at_least, at_most, at_most/at_least-1)
        return min_array_length


