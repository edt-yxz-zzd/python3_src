#__all__:goto
r'''[[[
e ../../python3_src/seed/types/PlaceholderAsSelf.py
view ../../python3_src/seed/tiny_/at.py


seed.types.PlaceholderAsSelf
py -m nn_ns.app.debug_cmd   seed.types.PlaceholderAsSelf -x
py -m nn_ns.app.doctest_cmd seed.types.PlaceholderAsSelf:__doc__ -ff -v

>>> (f_ := placeholder__to_capture_call[0][:-1].split()[-1])
PlaceholderAsSelf(((((((), (True, 0)), (True, slice(None, -1, None))), (False, 'split')), (Ellipsis, ((), {}))), (True, -1)), False, True)
>>> apply_placeholder__(f_, ['aaa bbb'])
'bb'
>>> curry_apply_placeholder_(f_)(['aaa bbb'])
'bb'
>>> placeholder[0][:-1].split(['aaa bbb'])()
['aaa', 'bb']
>>> placeholder[0][:-1].__class__(['aaa bbb']) is str
True


#]]]'''
__all__ = r'''
PlaceholderAsSelf
    placeholder
        SELF
    placeholder__special_method_via_cls
    placeholder__to_capture_call
curry_apply_placeholder_
    apply_placeholder__
reconfig_placeholder_

'''.split()#'''
__all__

from seed.tiny import check_type_is, curry1, ifNone
from seed.tiny_.check import check_pseudo_identifier
from seed.helper.repr_input import repr_helper

from seed.data_funcs.lnkls import rglnkls_ops, empty_rglnkls, rglnkls_ipush_right, rglnkls_ipop_right, rglnkls2reversed_iterable, rglnkls5iterable

from seed.data_funcs.lnkls import rglnkls2list


class PlaceholderAsSelf:
    'placeholder.xxx[kkk].yyy[iii] === lambda self:self.xxx[kkk].yyy[iii]'
    #def __call__(sf, self, /):
    def __call__(sf, /, *args, **kwargs):
        rglnkls, special_method_via_cls, to_capture_call = object.__getattribute__(sf, '_args')
        if to_capture_call:
            return _mk(sf, ..., (args, kwargs))
        #return apply_placeholder__(sf, self)
        return apply_placeholder__(sf, *args, **kwargs)

    def __init__(sf, rglnkls, special_method_via_cls, to_capture_call, /):
        sf._args = (rglnkls, special_method_via_cls, to_capture_call)
    def __repr__(sf, /):
        args = object.__getattribute__(sf, '_args')
        return repr_helper(sf, *args)
    def __getattribute__(sf, nm, /):
        #check_type_is(str, nm)
        check_pseudo_identifier(nm)
        return _mk(sf, False, nm)
    def __getitem__(sf, k, /):
        return _mk(sf, True, k)

def _mk(sf, nm_vs_argkws_vs_key, nm_or_argkws_or_key, /):
    rglnkls, special_method_via_cls, to_capture_call = object.__getattribute__(sf, '_args')
    rglnkls, _None = rglnkls_ipush_right(rglnkls, (nm_vs_argkws_vs_key, nm_or_argkws_or_key))
    cls = type(sf)
    return cls(rglnkls, special_method_via_cls, to_capture_call)
def curry_apply_placeholder_(sf, /):
    return curry1(apply_placeholder__, sf)
def apply_placeholder__(sf, self, /):
    rglnkls, special_method_via_cls, to_capture_call = object.__getattribute__(sf, '_args')
    ls = rglnkls2list(rglnkls)
    for nm_vs_argkws_vs_key, nm_or_argkws_or_key in ls:
        if nm_vs_argkws_vs_key is False:
            nm = nm_or_argkws_or_key
            if special_method_via_cls and len(nm) >= 4 and nm.startswith('__') and nm.endswith('__'):
                f_ = getattr(type(self), nm)
                v = curry1(f_, self)
            else:
                v = getattr(self, nm)
            v
        elif nm_vs_argkws_vs_key is True:
            k = nm_or_argkws_or_key
            v = self[k]
        elif nm_vs_argkws_vs_key is ...:
            args, kwds = nm_or_argkws_or_key
            v = self(*args, **kwds)
        else:
            raise 000
        v
        self = v
    self
    return self

def reconfig_placeholder_(sf, special_method_via_cls, to_capture_call, /):
    rglnkls, _special_method_via_cls, _to_capture_call = object.__getattribute__(sf, '_args')
    special_method_via_cls = ifNone(special_method_via_cls, _special_method_via_cls)
    to_capture_call = ifNone(to_capture_call, _to_capture_call)
    cls = type(sf)
    return cls(rglnkls, special_method_via_cls, to_capture_call)


SELF = placeholder = PlaceholderAsSelf(empty_rglnkls, False, False)
placeholder__special_method_via_cls = reconfig_placeholder_(placeholder, True, None)
placeholder__to_capture_call = reconfig_placeholder_(placeholder, None, True)

__all__


from seed.types.PlaceholderAsSelf import placeholder, SELF, placeholder__special_method_via_cls, placeholder__to_capture_call
from seed.types.PlaceholderAsSelf import curry_apply_placeholder_, apply_placeholder__, reconfig_placeholder_
from seed.types.PlaceholderAsSelf import *
