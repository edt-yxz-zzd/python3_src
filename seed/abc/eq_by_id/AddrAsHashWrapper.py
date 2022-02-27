r'''
seed.abc.eq_by_id.AddrAsHashWrapper
from seed.abc.eq_by_id.AddrAsHashWrapper import AddrAsHashWrapper
see:
    seed.abc.eq_by_id.AddrAsHash
    from seed.abc.eq_by_id.AddrAsHash import AddrAsHash as EqById

e ../../python3_src/seed/abc/eq_by_id/AddrAsHashWrapper.py
    AddrAsHashWrapper is copy of StdValue2FastKeyWrapper
    e ../../python3_src/seed/helper/reduce_number_of_objects_with_same_value.py

see:
    seed.abc.eq_by_id.BaseAddrAsHash
        from seed.abc.eq_by_id.BaseAddrAsHash import BaseAddrAsHash
    seed.abc.eq_by_id.AddrAsHash
        from seed.abc.eq_by_id.AddrAsHash import AddrAsHash as EqById
    seed.abc.eq_by_id.AddrAsHashWrapper
        from seed.abc.eq_by_id.AddrAsHashWrapper import AddrAsHashWrapper





#'''

__all__ = '''
    AddrAsHashWrapper
        StdValue2FastKeyWrapper
    '''.split()


class AddrAsHashWrapper:
    #class StdValue2FastKeyWrapper:
    __slots__ = ('_v',)
    __doc__ = r'''
    diff AddrAsHashWrapper vs AddrAsHash:
        AddrAsHashWrapper
            sf.__hash__ be id(sf.the_value_obj/the_wrapped_obj)
                shouldnot be object.__hash__(sf.the_value_obj/the_wrapped_obj)
                    to avoid collide with the_wrapped_obj
        AddrAsHash
            sf.__hash__ be id(sf) or object.__hash__(sf)
    ######################
    ######################
    ######################
    __doc__ for class AddrAsHashWrapper:
        see:seed.types.logic.ZerothOrderLogic
        to cache eval result of prop@env
            but avoid spending too much time on eq<prop>
    ######################
    ######################
    ######################
    __doc__ for class StdValue2FastKeyWrapper:
        see:seed.helper.reduce_number_of_objects_with_same_value
    since the std value is unique
        we neednot to hash/eq too heavy
        ie replace by id/is

        eg.
            register_point :: {weakref<std_value_obj>: weakref<std_value_obj>}
            may update to register_point :: {weakref<std_value_obj>: weakref<wrapped_std_value_obj>}
                but not faster, only when wrap the key of dict
            ====
            old_version_d :: {std_value_obj: ...}
            new_version_d :: {wrapped_std_value_obj: ...}
                #faster!!!
    #'''
    def __new__(cls, value_obj, /):
        if cls is not StdValue2FastKeyWrapper: raise TypeError
        sf = object.__new__(StdValue2FastKeyWrapper)
        if type(sf) is not StdValue2FastKeyWrapper: raise TypeError
        StdValue2FastKeyWrapper.___init___(sf, value_obj)
        return sf
    def ___init___(sf, value_obj, /):
        sf._v = value_obj
    def __eq__(sf, ot, /):
        #bug: return sf is ot
        return sf._v is ot._v
    def __hash__(sf, /):
        #bug:return id(sf)
        return id(sf._v)
    @property
    def the_value_obj(sf, /):
        return sf._v
    def __call__(sf, /):
        return sf._v
StdValue2FastKeyWrapper = AddrAsHashWrapper


