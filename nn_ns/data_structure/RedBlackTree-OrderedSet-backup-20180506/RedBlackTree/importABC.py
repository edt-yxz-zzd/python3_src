
#from seed.types.ABC import *
__all__ = '''
    ABC
    not_implemented

'''.split()

from seed.meta.ABC import ABC, not_implemented #, ABCMeta, abstractmethod





'''
from abc import ABCMeta, abstractmethod, ABC
ABC = ABC
    # orinial seed.types.ABC.ABC
    #   fetch data-property instead of cls member object
not_implemented = abstractmethod
    # v.s. orinial seed.types.ABC.not_implemented
    #   replace the method body by "raise NotImplementedError"
'''



