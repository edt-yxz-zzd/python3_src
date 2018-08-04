
__all__ = '''
    EmptyStackError
    PopEmptyStackErrorForRaise
    TopEmptyStackErrorForRaise
    ABC
    abstractmethod

    obj_classmethod
    obj_constructor
    instance_const_method
    instance_inplace_eval
    instance_inplace_stmt
    instance_pseudo_inplace_stmt
    instance_pseudo_inplace_eval

    echo
    null_iter
    '''.split()


'''
from .StackOpsCommon import (
    ,EmptyStackError
    ,PopEmptyStackErrorForRaise
    ,TopEmptyStackErrorForRaise
    ,ABC, abstractmethod

    ,obj_classmethod
    ,obj_constructor
    ,instance_const_method
    ,instance_inplace_eval
    ,instance_inplace_stmt
    ,instance_pseudo_inplace_eval
    ,instance_pseudo_inplace_stmt
    ,echo
    ,null_iter
    )
'''

from abc import ABC, ABCMeta, abstractmethod

# EmptyStackError is used to catch
EmptyStackError = Exception
# PopEmptyStackErrorForRaise is used to raise
class PopEmptyStackErrorForRaise(EmptyStackError):pass
class TopEmptyStackErrorForRaise(EmptyStackError):pass

echo = lambda x:x
null_iter = iter(())
ABC = ABC
abstractmethod = abstractmethod


def obj_classmethod(f):
    return f
def obj_constructor(f):
    return obj_classmethod(f)

def instance_const_method(f):
    return f

# mutable ops
def instance_inplace_eval(f):
    return f
def instance_inplace_stmt(f):
    return f


# pseudo immutable ops
def instance_pseudo_inplace_stmt(f):
    return f
def instance_pseudo_inplace_eval(f):
    return f




