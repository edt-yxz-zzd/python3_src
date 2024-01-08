#__all__:goto
r'''[[[
e ../../python3_src/seed/types/OverrideOrdering.py
    view ../../python3_src/seed/for_libs/for_heapq.py
        override __le__ via kwds:__le__
    view ../../python3_src/seed/types/Heap.py
        override __le__ via obj2item+WithSortKey/OverrideOrdering

    view ../../python3_src/seed/types/Heap.py
    view ../../python3_src/seed/types/OverrideOrdering.py
    view ../../python3_src/seed/for_libs/for_heapq.py


seed.types.OverrideOrdering
py -m nn_ns.app.debug_cmd   seed.types.OverrideOrdering -x
py -m nn_ns.app.doctest_cmd seed.types.OverrideOrdering:__doc__ -ff -v
py_adhoc_call   seed.types.OverrideOrdering   @f
from seed.types.OverrideOrdering import *
>>> setting_NNF = OrderingSetting(None, None, False)
>>> nnf_111 = OverrideOrdering(setting_NNF, '111')
>>> nnf_222 = OverrideOrdering(setting_NNF, '222')
>>> nnf_111 < nnf_111
False
>>> nnf_111 <= nnf_111
True
>>> nnf_111 < nnf_222
True
>>> nnf_111 <= nnf_222
True
>>> nnf_222 < nnf_111
False
>>> nnf_222 <= nnf_111
False
>>> setting_NNT = OrderingSetting(None, None, True)
>>> nnt_111 = OverrideOrdering(setting_NNT, '111')
>>> nnt_222 = OverrideOrdering(setting_NNT, '222')
>>> nnt_111 < nnt_111
False
>>> nnt_111 <= nnt_111
True
>>> nnt_111 < nnt_222
False
>>> nnt_111 <= nnt_222
False
>>> nnt_222 < nnt_111
True
>>> nnt_222 <= nnt_111
True
>>> nnt_222 <= nnf_111
Traceback (most recent call last):
    ...
seed.types.OverrideOrdering.Error__ordering_setting_mismatch
>>> setting_LNF = OrderingSetting(len, None, False)
>>> lnf_111 = OverrideOrdering(setting_LNF, '111')
>>> lnf_222 = OverrideOrdering(setting_LNF, '222')
>>> lnf_111 < lnf_111
False
>>> lnf_111 <= lnf_111
True
>>> lnf_111 < lnf_222 # use "functools.total_ordering" and defined '__le__' only without '__eq__' will give wrong result 'True' here. since: [(x < y) =[def]= (x <= y) && (x != y)]
False
>>> lnf_111 <= lnf_222
True
>>> lnf_222 < lnf_111
False
>>> lnf_222 <= lnf_111
True
>>> lnf_111
OverrideOrdering(OrderingSetting(<built-in function len>, <built-in function le>, False), '111')
>>> lnf_222
OverrideOrdering(OrderingSetting(<built-in function len>, <built-in function le>, False), '222')
>>> str(lnf_111)
"OverrideOrdering(OrderingSetting(<built-in function len>, <built-in function le>, False), '111', (3,))"
>>> str(lnf_222)
"OverrideOrdering(OrderingSetting(<built-in function len>, <built-in function le>, False), '222', (3,))"


cp /data/data/com.termux/files/usr/lib/python3.10/functools.py /sdcard/0my_files/tmp/out4py/py_src/py-functools.py
view /sdcard/0my_files/tmp/out4py/py_src/py-functools.py

def _lt_from_le(self, other, NotImplemented=NotImplemented):
    'Return a < b.  Computed by @total_ordering from (a <= b) and (a != b).'
    op_result = type(self).__le__(self, other)
    if op_result is NotImplemented:
        return op_result
    return op_result and self != other



>>> setting_NGF = OrderingSetting(None, lambda x,y:x>=y, False)
>>> ngf_111 = OverrideOrdering(setting_NGF, '111')
>>> ngf_222 = OverrideOrdering(setting_NGF, '222')
>>> ngf_111 < ngf_111
False
>>> ngf_111 <= ngf_111
True
>>> ngf_111 < ngf_222
False
>>> ngf_111 <= ngf_222
False
>>> ngf_222 < ngf_111
True
>>> ngf_222 <= ngf_111
True


######################
###test gt, ge:
>>> nnf_111 > nnf_111
False
>>> nnf_111 >= nnf_111
True
>>> nnf_111 > nnf_222
False
>>> nnf_111 >= nnf_222
False
>>> nnf_222 > nnf_111
True
>>> nnf_222 >= nnf_111
True


#]]]'''
__all__ = r'''
OrderingSetting
OverrideOrdering
    Error__ordering_setting_mismatch
'''.split()#'''
__all__

#from functools import total_ordering
from seed.abc.ITotalOrdering import ITotalOrdering5le

from seed.tiny_.std____key__le__reverse_ import std____key__le__reverse_
from seed.tiny import null_tuple
from seed.helper.repr_input import repr_helper

class OrderingSetting:
    def __repr__(sf, /):
        return repr_helper(sf, *sf.args)
    def __init__(sf, key, __le__, reverse, /):
        (key, __le__, reverse) = std____key__le__reverse_(key, __le__, reverse)
        sf.args = (key, __le__, reverse)
    @property
    def key(sf, /):
        return sf.args[0]
    @property
    def le(sf, /):
        return sf.args[1]
    @property
    def reverse(sf, /):
        return sf.args[2]
class Error__ordering_setting_mismatch(Exception):pass

class OverrideOrdering(ITotalOrdering5le):
    ___no_slots_ok___ = True
#@total_ordering
#class OverrideOrdering:


    def __str__(sf, /):
        return repr_helper(sf, sf.ordering_setting, sf.obj, sf._tmay_key4obj)
        return repr_helper(sf, sf.ordering_setting, sf.obj, sf.key4obj)
    def __repr__(sf, /):
        return repr_helper(sf, sf.ordering_setting, sf.obj)
    def __init__(sf, ordering_setting, obj, /):
        sf._ordering_setting = ordering_setting
        sf._obj = obj
        sf._tmay_key4obj = null_tuple
    @property
    def ordering_setting(sf, /):
        return sf._ordering_setting
    @property
    def obj(sf, /):
        return sf._obj
    @property
    def key4obj(sf, /):
        tm = sf._tmay_key4obj
        if not tm:
            k = sf.ordering_setting.key(sf.obj)
            sf._tmay_key4obj = (k,)
            k = sf.key4obj
        else:
            [k] = tm
        return k
    #@override
    def __le__(sf, ot, /):
        if not type(ot) is type(sf):
            return NotImplemented
        if not ot.ordering_setting is sf.ordering_setting: raise Error__ordering_setting_mismatch
        ordering_setting = sf.ordering_setting

        k4sf = sf.key4obj
        k4ot = ot.key4obj
        if ordering_setting.reverse:
            k4sf, k4ot = k4ot, k4sf
        return ordering_setting.le(k4sf, k4ot)

__all__


from seed.types.OverrideOrdering import OrderingSetting, OverrideOrdering
from seed.types.OverrideOrdering import *
