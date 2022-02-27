#__all__:goto
#main_body_src_code:goto
#HHHHH
#[[[__doc__:begin
r'''
seed.abc.storage.MemberGetter
py -m    seed.abc.storage.MemberGetter
py -m nn_ns.app.debug_cmd   seed.abc.storage.MemberGetter
see:
    e ../../python3_src/seed/types/OpaqueInstanceStorage.py

from seed.abc.storage.MemberGetter import ...

#[[[doc_sections:begin
#doctest_examples:goto
#wwwzzz:goto

#[[[doctest_examples:begin
>>>
...
#]]]doctest_examples:end

#[[[wwwzzz:begin
arr i o => get i o
mget i o =[def]= get i (Maybe o)

IMemberGetter :: mget packet member_value
IRigidMemberGetter :: get packet member_value

register:
    permanent_obj2member_getter[type(packet)] = member_getter<packet, member_value>
    g1 = wrap<member_getter>(type)
    g2 = wrap<member_getter>(permanent_obj2member_getter.__getitem__)
    member_value = (g2 . g1 $ packet) $ packet
    whole-member_getter = apply . with_input $ chain<g1, g2>

depth-chain:
    mget i x -> mget x o -> mget i o
    mget i x -> mget x y -> mget i (x, y)
width-star:
    mget i x -> mget i y -> mget i (x, y)
        #all
    mget i o -> mget i o -> mget i o
        #any
        #priority-selection
wrap:
    o -> mget i o
    (Maybe o) -> mget i o
    () -> mget i o
    (i -> o) -> mget i o
    (i -> Maybe o) -> mget i o
echo:
    mget x x
fan_out:
    mget x (x, x, ...)
        #link: chain/star and switch/parallel

apply:
    mget x (i, mget i o) -> mget x o #apply
    ---
    mget i o -> mget i (i, o) #with_input
    mget i (mget i o) -> mget i o #collapse # == apply . with_input
    ---
    mget i o -> (i -> Maybe o)
        #unwrap
        #def-intensional

switch:
    mget a b -> mget x y -> mget (Either a x) (Either b y)
    (@[c:Case] -> mget i[c] o[i]) -> mget (?[c:Case], i[c]) (?[c:Case], o[c])
    mget i (?[c:Case], o) -> mget i o
parallel:
    mget a b -> mget x y -> mget (a, x) (b, y)
    (@[c:Case] -> mget i[c] o[i]) -> mget (@[c:Case] -> i[c]) (@[c:Case] -> o[c])

iterator:
    (i -> Maybe o) -> mget (Iter i) o
    ----
    (i -> o) -> mget (Iter i) (Iter o) #map
    mget (Iter (Maybe o)) o #any_fst
    ---
    #cls --> (__mro__::[cls]) --> (Iter __dict__) --> cls.x
iterator -> lazy_singly_linked_list
    lazy_singly_linked_list.x :: (iterator | () | (err,) | (v, lazy_singly_linked_list))

#]]]wwwzzz:end
#]]]doc_sections:end


#'''
#]]]__doc__:end

#################################
#HHHHH
__all__ = '''
    IMemberGetter
        IAutoMemberGetter
            IRigidMemberGetter
        IMemberGetter__composite
            collect_tmays__tmay_all
            select_tmays__any_first
            select_tmays__all1_last

            IMemberGetter__star
            IMemberGetter__star_all
            IMemberGetter__star_any
            IMemberGetter__chain
                IMemberGetter__chain_all
                IMemberGetter__chain_last
            IAutoMemberGetter__star_any
            IAutoMemberGetter__star_all
            IAutoMemberGetter__chain
                IAutoMemberGetter__chain_all
                IAutoMemberGetter__chain_last
    IMemberGetter__cased_subpackets
        IMemberGetter__switch
            IMemberGetter__switch_either
        IMemberGetter__parallel_mapping
        IMemberGetter__parallel_tuple
            IMemberGetter__parallel_pair
        IAutoMemberGetter__cased_subpackets
            IAutoMemberGetter__switch
                IAutoMemberGetter__switch_either
            IAutoMemberGetter__parallel_mapping
            IAutoMemberGetter__parallel_tuple
                IAutoMemberGetter__parallel_pair
    IMemberGetter__wrap_member_getter
        IMemberGetter__apply
        IMemberGetter__collapse
    IIndirectMemberGetter

    IMemberPatcher
        IAutoMemberPatcher
        IMemberSetter
            IAutoMemberSetter
    IIndirectMemberGetter__via_collapse
        IMemberAdaptor
            IAutoMemberAdaptor
    '''.split()

#################################
#HHHHH
___begin_mark_of_excluded_global_names__0___ = ...
from seed.abc.abc__ver1 import ABC, abstractmethod, override
from seed.tiny import get_abstractmethod_names, check_manifest4abstractmethods
from seed.tiny import check_uint, check_pair, is_iterator, check_type_is, expectError#, check_type_le, check_tuple
from seed.tiny import expectError, MapView
from seed.helper.check.checkers import check_instance, check_is_None, check_bool, check_int, check_tmay
from seed.tiny_.mk_fdefault import mk_default, eliminate_tmay__cased, eliminate_tmay__mix
    #mk_tmay_from_default2value
#from seed.types.mapping.PseudoMapping import IPseudoMapping___get, IPseudoMapping___get__setdefault
from collections.abc import Mapping


r"""
import ...
from seed.tiny import str2__all__
__all__ = str2__all__(r'''#)
    #(''')
from seed.abc.abc import ABC, abstractmethod, override, not_implemented, ABCMeta
from seed.helper.repr_input import repr_helper
from seed.tiny import echo, print_err, mk_fprint, mk_assert_eq_f, expectError
from seed.helper.check.checkers import check_pair, check_type_is
  #from seed.helper.check.checkers import checks, checkers, check_funcs
  #view ../../python3_src/seed/helper/check/checkers.py
if 0b00:#[01_to_turn_off]
    #0b01
    print(fr'x={x}')
    from seed.tiny import print_err
    print_err(fr'x={x}')
    from pprint import pprint
    pprint(x)
#"""
___end_mark_of_excluded_global_names__0___ = ...

#HHHHH
#[[[main_body_src_code:begin
#MemberGetter:goto
#MemberRegister:goto
#MemberAdaptor:goto
#MemberGetter__mixin:goto
#zzzwww:goto

r'''
TODO:
    key -> packet/obj/instance
        %s/key\C/packet/g
        %s/\<value\>\C/member_value/g
    #cancel IMemberGetter -> IOptionalMemberGetter
        %s/IMemberGetter\C/IOptionalMemberGetter/g
    IMemberGetter -> IRigidMemberGetter
    get_member__Nothing -> get_member__Nothing
        %s/get__Nothing\C/get_member__Nothing/g
        %s/get__tmay\C/get_member__tmay/g
        %s/get__may\C/get_member__may/g
    register_member__fvalue -> register_member__fvalue
        %s/register__fvalue\C/register_member__fvalue/g
        %s/register__value\C/register_member__value/g
        %s/register__default\C/register_member__default/g
        %s/mk_value_on_default\C/mk_member_value_on_default/g
    IAutoMemberRegister --> IAutoMemberRegister
        %s/MemberRegister__default\C/AutoMemberRegister/g
    IMemberRegister --> IMemberRegister
        %s/MemberRegister__fvalue\C/MemberRegister/g
    fvalue -> imay_xdefault_rank, xdefault
    auto-register
    ([IRigidMemberGetter(<=auto-register)], [IAutoMemberRegister], IMemberRegister) => IMemberRegister
    get-Nothing -> tmay/xdefault
        get_member__Nothing -> get_member__tmay/get_member__xdefault__cased/get_member__xdefault__mix


    to add?:
        ___is_rigid_member_getter__dynamic___
        ___is_auto_member_getter__dynamic___
        get_or_auto_install_member
        get_or_try_auto_install_member
            for IndirectMemberGetter, target_member_getter is indeterminate
        try_register_member__xvalue
        try_register_member_getter__xvalue

    mounter register setter patcher
    setter/getter -> setter/getter
        %s/ettor\C/etter/g

    MemberPatcher
    member_value -> member_value+plugin4member/patch4member
        register() -> patch()
    ___auto_install_member___ -> ___auto_patch_member___ -> ___auto_supply_member___ -> ___auto_fill_member___ -> ___auto_fulfill_member___ -> ___auto_setup_member___ -> ___auto_install_member___
        %s/auto_install\C/auto_install/g
#'''

#[[[MemberGetter:begin
class IMemberGetter(ABC):
    'packet=key=obj=instance; member_value=property=member=member_value'
    __slots__ = ()

    @abstractmethod
    def check_packet(sf, packet, /):
        return
    @abstractmethod
    def check_member_value(sf, member_value, /):
        return
    r'''
    @abstractmethod
    def ___get_member__Nothing___(sf, Nothing, packet, /):
        'get_member__Nothing(); -> member_value|Nothing'
    def get_member__Nothing(sf, Nothing, packet, /):
        '___get_member__Nothing___(); -> member_value|Nothing'
        sf.check_packet(packet)
        value_or_Nothing = type(sf).___get_member__Nothing___(sf, Nothing, packet)
        if not (value_or_Nothing is Nothing): sf.check_member_value(value_or_Nothing)
        return value_or_Nothing

    def get_member__tmay(sf, packet, /):
        '___get_member__Nothing___(); -> tmay member_value'
        Nothing = object()
        value_or_Nothing = sf.get_member__Nothing(Nothing, packet)
        if value_or_Nothing is Nothing:
            return ()
        else:
            member_value = value_or_Nothing
            return (member_value,)
    #'''
    @abstractmethod
    def ___get_member__tmay___(sf, packet, /):
        'get_member__tmay(); -> tmay member_value'
    def get_member__tmay(sf, packet, /):
        '___get_member__tmay___(); -> tmay member_value'
        sf.check_packet(packet)
        tmay_member_value = type(sf).___get_member__tmay___(sf, packet)
        check_tmay(tmay_member_value)
        if tmay_member_value: sf.check_member_value(*tmay_member_value)
        return tmay_member_value
    def get_member__xdefault__mix(sf, packet, imay_xdefault_rank, xdefault, /):
        (is_member_value, default_or_member_value) = sf.get_member__xdefault__cased(packet, imay_xdefault_rank, xdefault)
        return default_or_member_value
    def get_member__xdefault__cased(sf, packet, imay_xdefault_rank, xdefault, /):
        '-> (is_member_value, default_or_member_value)'
        check_int(imay_xdefault_rank, min=-1, max=2)
        tmay_member_value = sf.get_member__tmay(packet)
        cased_either = (is_member_value, default_or_member_value) = eliminate_tmay__cased(imay_xdefault_rank, xdefault, sf, packet)
        return cased_either



    def get_member__may(sf, packet, /):
        '___get_member__tmay___(); -> may member_value'
        #not: return sf.get_member__xdefault__mix(packet, -1, None)
        if not expectError(Exception, lambda:sf.check_member_value(None)): raise TypeError
        return sf.get_member__avoid_default(packet, None)
    def get_member__avoid_default(sf, packet, default, /):
        #not: return sf.get_member__xdefault__mix(packet, -1, default)
        #no:assert expectError(Exception, lambda:sf.check_member_value(default))
        #   Nothing may pass check_member_value()
        (is_member_value, default_or_member_value) = sf.get_member__xdefault__cased(packet, -1, default)
        if is_member_value and default is default_or_member_value:
            member_value = default_or_member_value
            ###########################
            if member_value is default: sf.check_member_value(member_value)
            if member_value is default: sf.check_member_value(default)
            if member_value is default: raise logic-err
            raise logic-err
        return default_or_member_value
#print(IMemberGetter.__abstractmethods__)
#assert (IMemberGetter.__abstractmethods__) == frozenset({'check_member_value', 'check_packet', '___get_member__tmay___'})
check_manifest4abstractmethods(IMemberGetter, r'''
        check_packet
        check_member_value
        ___get_member__tmay___
    #''')
#class IMemberGetter(ABC):

class IAutoMemberGetter(IMemberGetter):
    r'''
    why?
        as base_cls of (IRigidMemberGetter, IAutoMemberPatcher)
        see below: incompatible
            incompatible<IMemberPatcher,IRigidMemberGetter>
    #'''
    __slots__ = ()

    @abstractmethod
    def ___auto_install_member___(sf, packet, /):
        'get_or_auto_install_member(); -> None'
        #def ___get_or_auto_install_member___(sf, packet, /):
        #'get_or_auto_install_member(); -> member_value'
    def get_or_auto_install_member(sf, packet, /):
        '___auto_install_member___(); -> member_value'
        tmay_member_value = sf.get_member__tmay(packet)
        if not tmay_member_value:
            _ = type(sf).___auto_install_member___(sf, packet)
            check_is_None(_)
            tmay_member_value = sf.get_member__tmay(packet)
        if not tmay_member_value: raise logic-err
        [member_value] = tmay_member_value
        return member_value

    r'''no below since required as branch-test:
    @override
    def ___get_member__tmay___(sf, packet, /):
        'get_member__tmay(); -> tmay member_value'
        member_value = sf.get_member__rigid(packet)
        return (member_value,)
    #'''
#print(IAutoMemberGetter.__abstractmethods__)
#assert (IAutoMemberGetter.__abstractmethods__) == frozenset({'check_member_value', 'check_packet', '___get_member__tmay___', '___auto_install_member___'})
check_manifest4abstractmethods(IAutoMemberGetter, r'''
        check_packet
        check_member_value
        ___get_member__tmay___
        ___auto_install_member___
    #''')
#class IAutoMemberGetter(IMemberGetter):

class ___0:
    __slots__ = ()
class ___1:
    __slots__ = ()
class ___2:
    __slots__ = ()
class IRigidMemberGetter(IAutoMemberGetter, ___2, ___1, ___0):
    r'''
    intent:
        to get member that was initialized
        eg. obj -> ops<obj> / type(obj)
        eg. cls -> cls.__name__ / cls.__mro__
    ---
    member should be set already
        must exist:
            get_member__Nothing -> member_value
        neednot register_member__fvalue
    #'''
    __slots__ = ()

    @abstractmethod
    def ___get_member__rigid___(sf, packet, /):
        'get_member__rigid(); -> member_value'
    def get_member__rigid(sf, packet, /):
        '___get_member__rigid___(); -> member_value'
        sf.check_packet(packet)
        member_value = type(sf).___get_member__rigid___(sf, packet)
        sf.check_member_value(member_value)
        return member_value

    @override
    def ___get_member__tmay___(sf, packet, /):
        'get_member__tmay(); -> tmay member_value'
        member_value = sf.get_member__rigid(packet)
        return (member_value,)

    @override
    def ___auto_install_member___(sf, packet, /):
        'get_or_auto_install_member(); -> None'
        raise logic-err#SHOULD NEVER call ___auto_install_member___
#print(IRigidMemberGetter.__abstractmethods__)
#assert (IRigidMemberGetter.__abstractmethods__) == frozenset({'check_member_value', 'check_packet', '___get_member__rigid___'})
check_manifest4abstractmethods(IRigidMemberGetter, r'''
        check_packet
        check_member_value
        ___get_member__rigid___
    #''')
#class IRigidMemberGetter(IMemberGetter):

#composite
class IMemberGetter__composite(IMemberGetter):
    'composite: iter member_getter => sf/member_getter'
    __slots__ = ()

    ___base_cls4member_getter4composite___ = IMemberGetter
    def check_member_getter4composite(sf, member_getter, /):
        check_instance(type(sf).___base_cls4member_getter4composite___, member_getter)
    r'''
    def check_member_getters4composite(sf, member_getters, /):
        for member_getter in member_getters:
            sf.check_member_getter4composite(member_getter)
    #'''

    @abstractmethod
    def ___iter_member_getters4composite___(sf, /):
        #def ___iter_chain_of_member_getters___(sf, /):
        'iter_member_getters4composite(); -> Iter<IMemberGetter>'
    def iter_member_getters4composite(sf, /):
        '___iter_member_getters4composite___(); -> Iter<IMemberGetter>'
        #iter<member_getter>
        it = type(sf).___iter_member_getters4composite___(sf)
        if not is_iterator(it): raise TypeError
        #sf.check_member_getters4composite(it)
        for member_getter in it:
            sf.check_member_getter4composite(member_getter)
            yield member_getter
        return
#class IMemberGetter__composite(IMemberGetter):

def collect_tmays__tmay_all(tmays, /):
    'Iter (tmay x) -> (tmay tuple<x>)'
    ls = []
    for tmay_x in tmays:
        if not tmay_x:
            [] = tmay_x
            return ()
        [x] = tmay_x
        ls.append(x)
    ls = tuple(ls)
    return (ls,)
def select_tmays__any_first(tmays, /):
    'Iter (tmay x) -> (tmay x)'
    for tmay_x in tmays:
        if tmay_x: break
    else:
        return ()
    [x] = tmay_x
    return (x,)
def select_tmays__all1_last(tmays, /):
    'Iter (tmay x) -> (tmay x) #nonempty_iter'
    #tmay_r = ()
    for tmay_r in tmays:
        if not tmay_r:
            break
    return tmay_r #nonempty_iter=>tmay_r assigned

#star
class IMemberGetter__star(IMemberGetter__composite):
    'star:width'
    __slots__ = ()

    def iter_tmay_submembers4composite(sf, packet, /):
        '-> Iter (tmay submember_value)'
        it = sf.iter_member_getters4composite()
        assert iter(it) is it
        for member_getter in it:
            tmay_x = member_getter.get_member__tmay(packet)
                #should avoid use Nothing
            yield tmay_x
#class IMemberGetter__star(IMemberGetter):

class IMemberGetter__star_all(IMemberGetter__composite):
    'star_all:width/all'
    __slots__ = ()

    @override
    def ___get_member__tmay___(sf, packet, /):
        'get_member__tmay(); -> tmay member_value'
        it = sf.iter_tmay_submembers4composite(packet)
        return collect_tmays__tmay_all(it)
        #return ((),) #if not member_getter in star
#class IMemberGetter__star_all(IMemberGetter__composite):

class IMemberGetter__star_any(IMemberGetter__composite):
    'star_any:width/any/first/priority_choice'
    __slots__ = ()

    @override
    def ___get_member__tmay___(sf, packet, /):
        'get_member__tmay(); -> tmay member_value'
        it = sf.iter_tmay_submembers4composite(packet)
        return select_tmays__any_first(it)
        #return () #if not member_getter in star
#class IMemberGetter__star_any(IMemberGetter__composite):



#chain
class IMemberGetter__chain(IMemberGetter__composite):
    'chain:depth'
    __slots__ = ()

    def iter_tmay_transitional_members4composite(sf, packet, /):
        '-> Iter (tmay transitional_member_value); #nonempty_iter:first is (packet,)'
        it = sf.iter_member_getters4composite()
        assert iter(it) is it
        r = packet
        tmay_r = (r,); del r
        yield tmay_r
        for member_getter in it:
            if tmay_r:
                [r] = tmay_r
                tmay_r = member_getter.get_member__tmay(r)
                    #should avoid use Nothing
            yield tmay_r
#class IMemberGetter__chain(IMemberGetter):

class IMemberGetter__chain_all(IMemberGetter__composite):
    'chain_all:depth/collect_all'
    __slots__ = ()
    @override
    def ___get_member__tmay___(sf, packet, /):
        'get_member__tmay(); -> tmay member_value'
        it = sf.iter_tmay_transitional_members4composite(packet)
        return collect_tmays__tmay_all(it)
        #return ((packet,),) #if not member_getter in chain
#class IMemberGetter__chain_all(IMemberGetter):



class IMemberGetter__chain_last(IMemberGetter__composite):
    'chain_last:depth/last'
    __slots__ = ()
    @override
    def ___get_member__tmay___(sf, packet, /):
        'get_member__tmay(); -> tmay member_value'
        it = sf.iter_tmay_transitional_members4composite(packet)
        #nonempty_iter=>tmay_r assigned
        return select_tmays__all1_last(it)
        #return (packet,) #if not member_getter in chain
#class IMemberGetter__chain_last(IMemberGetter):




r''' IMemberGetter__star_any need only any0 sub-member_getter be IAutoMemberGetter
class IAutoMemberGetter__composite(IMemberGetter__composite, IAutoMemberGetter):
    __slots__ = ()

    # @override
    ___base_cls4member_getter4composite___ = IAutoMemberGetter
#'''

#star_any
class IAutoMemberGetter__star_any(IMemberGetter__star_any, IAutoMemberGetter):
    __slots__ = ()

    # @override
    #no: ___base_cls4member_getter4composite___ = IAutoMemberGetter
    @override
    def check_member_getter4composite(sf, member_getter, /):
        super().check_member_getter4composite(member_getter)


    @override
    def ___auto_install_member___(sf, packet, /):
        'get_or_auto_install_member(); -> None'
        it = sf.iter_member_getters4composite()
        assert iter(it) is it
        for member_getter in it:
            m = getattr(member_getter, 'get_or_auto_install_member', None)
            if m is not None and isinstance(member_getter, IAutoMemberGetter):
                get_or_auto_install_member = m
                get_or_auto_install_member(packet)
                break
        else:
            raise TypeError # no sub-member_getter should never call this func; if has sub-member_getter, but none is IAutoMemberGetter => err
        return None
#class IAutoMemberGetter__star_any(IMemberGetter__star_any, IAutoMemberGetter):



#star_all
class IAutoMemberGetter__star_all(IMemberGetter__star_all, IAutoMemberGetter):
    __slots__ = ()

    # @override
    ___base_cls4member_getter4composite___ = IAutoMemberGetter

    @override
    def ___auto_install_member___(sf, packet, /):
        'get_or_auto_install_member(); -> None'
        it = sf.iter_member_getters4composite()
        assert iter(it) is it
        for auto_member_getter in it:
            auto_member_getter.get_or_auto_install_member(packet)
        return None
#class IAutoMemberGetter__star_all(IMemberGetter__star_all, IAutoMemberGetter):


#chain
class IAutoMemberGetter__chain(IMemberGetter__chain, IAutoMemberGetter):
    __slots__ = ()

    # @override
    ___base_cls4member_getter4composite___ = IAutoMemberGetter

    @override
    def ___auto_install_member___(sf, packet, /):
        'get_or_auto_install_member(); -> None'
        r = packet
        it = sf.iter_member_getters4composite()
        assert iter(it) is it
        for auto_member_getter in it:
            r = auto_member_getter.get_or_auto_install_member(r)
        return None
#class IAutoMemberGetter__chain(IMemberGetter__chain, IAutoMemberGetter):
class IAutoMemberGetter__chain_all(IMemberGetter__chain_all, IAutoMemberGetter__chain):
    __slots__ = ()
class IAutoMemberGetter__chain_last(IMemberGetter__chain_last, IAutoMemberGetter__chain):
    __slots__ = ()

class IMemberGetter__cased_subpackets(IMemberGetter):
    'cased_subpackets'
    __slots__ = ()
    @abstractmethod
    def ___iter_cased_subpackets_from_packet___(sf, packet, /):
        'packet -> Iter (case, subpacket)'
    @abstractmethod
    def ___mk_tmay_member_value_from_cased_tmay_submember_value_iterator___(sf, cased_tmay_submember_value_iterator, /):
        'Iter (case, tmay submember_value) -> tmay_member_value'
    @abstractmethod
    def ___get_submember_getter_at_case___(sf, case, /):
        'get_submember_getter_at_case; case -> submember_getter::IMemberGetter'
    def get_submember_getter_at_case(sf, case, /):
        '___get_submember_getter_at_case___; case -> submember_getter::IMemberGetter'
        sf.check_switch_case4submember_getter(case)
        submember_getter = type(sf).___get_submember_getter_at_case___(sf, case)
        sf.check_submember_getter_at_case(case, submember_getter)
        return submember_getter
    def check_switch_case4submember_getter(sf, case, /):
        return
    def check_submember_getter_at_case(sf, case, member_getter, /):
        check_instance(IMemberGetter, member_getter)
        return
    def cased_subpackets_to_cased_tmay_submember_value_iterator(sf, cased_subpackets, /):
        'Iter (case, subpacket) -> Iter (case, tmay submember_value)'
        return map(sf.cased_subpacket2cased_tmay_submember_value, cased_subpackets)
    def cased_subpacket2cased_tmay_submember_value(sf, cased_subpacket, /):
        '(case, subpacket) -> (case, tmay submember_value)'
        check_pair(cased_subpacket)
        (case, subpacket) = cased_subpacket
        submember_getter = sf.get_submember_getter_at_case(case)
        tmay_submember_value = submember_getter.get_member__tmay(subpacket)
        return (case, tmay_submember_value)

    @override
    def ___get_member__tmay___(sf, packet, /):
        'get_member__tmay(); -> tmay member_value'
        cased_subpackets = type(sf).___iter_cased_subpackets_from_packet___(sf, packet)
        cased_tmay_submember_value_iterator = sf.cased_subpackets_to_cased_tmay_submember_value_iterator(cased_subpackets)
        tmay_member_value = type(sf).___mk_tmay_member_value_from_cased_tmay_submember_value_iterator___(sf, cased_tmay_submember_value_iterator)
        return tmay_member_value


class IAutoMemberGetter__cased_subpackets(IMemberGetter__cased_subpackets, IAutoMemberGetter):
    __slots__ = ()
    @override
    def ___auto_install_member___(sf, packet, /):
        'get_or_auto_install_member(); -> None'
        cased_subpackets = type(sf).___iter_cased_subpackets_from_packet___(sf, packet)
        for case, subpacket in cased_subpackets:
            submember_getter = sf.get_submember_getter_at_case(case)
            submember_getter.get_or_auto_install_member(subpacket)
        return None


class IMemberGetter__switch(IMemberGetter__cased_subpackets):
    'switch'
    __slots__ = ()
    @override
    def check_packet(sf, packet, /):
        check_pair(packet)
        (case, subpacket) = cased_subpacket = packet
        #sf.check_switch_case4submember_getter(case)
        submember_getter = sf.get_submember_getter_at_case(case)
        submember_getter.check_packet(subpacket)
        return
    @override
    def check_member_value(sf, member_value, /):
        check_pair(member_value)
        (case, submember_value) = cased_submember_value = member_value
        #sf.check_switch_case4submember_getter(case)
        submember_getter = sf.get_submember_getter_at_case(case)
        submember_getter.check_member_value(submember_value)
        return
    @override
    def ___iter_cased_subpackets_from_packet___(sf, packet, /):
        'packet -> Iter (case, subpacket)'
        check_pair(packet)
        cased_subpacket = packet
        yield cased_subpacket
    @override
    def ___mk_tmay_member_value_from_cased_tmay_submember_value_iterator___(sf, cased_tmay_submember_value_iterator, /):
        'Iter (case, tmay submember_value) -> tmay_member_value'
        [cased_tmay_submember_value] = cased_tmay_submember_value_iterator
        (case, tmay_submember_value) = cased_tmay_submember_value

        if tmay_submember_value:
            [submember_value] = tmay_submember_value
            cased_submember_value = (case, submember_value)
            member_value = cased_submember_value
            tmay_member_value = (member_value,)
        else:
            tmay_member_value = ()
        return tmay_member_value

class IMemberGetter__parallel_mapping(IMemberGetter__cased_subpackets):
    'parallel_mapping'
    __slots__ = ()
    @override
    def check_packet(sf, packet, /):
        check_instance(Mapping, packet)
        for case, subpacket in packet.items():
            submember_getter = sf.get_submember_getter_at_case(case)
            submember_getter.check_packet(subpacket)
        return
    @override
    def check_member_value(sf, member_value, /):
        check_instance(Mapping, member_value)
        for case, submember_value in member_value.items():
            submember_getter = sf.get_submember_getter_at_case(case)
            submember_getter.check_member_value(submember_value)
        return
    @override
    def ___iter_cased_subpackets_from_packet___(sf, packet, /):
        'packet -> Iter (case, subpacket)'
        return packet.items()
    @override
    def ___mk_tmay_member_value_from_cased_tmay_submember_value_iterator___(sf, cased_tmay_submember_value_iterator, /):
        'Iter (case, tmay submember_value) -> tmay_member_value'
        d = {}
        for (case, tmay_submember_value) in (cased_tmay_submember_value_iterator):
            if case in d: raise TypeError
            if not tmay_submember_value:
                tmay_member_value = ()
                break
            [submember_value] = tmay_submember_value
            d[case] = (submember_value)
        else:
            member_value = MapView(d)
            tmay_member_value = (member_value,)
        return tmay_member_value


class IMemberGetter__parallel_tuple(IMemberGetter__cased_subpackets):
    'parallel_tuple'
    __slots__ = ()
    @override
    def check_packet(sf, packet, /):
        check_type_is(tuple, packet)
        L = len(packet)
        for case in reversed(range(L)):
            subpacket = packet[case]
            submember_getter = sf.get_submember_getter_at_case(case)
            submember_getter.check_packet(subpacket)
        return
    @override
    def check_member_value(sf, member_value, /):
        check_type_is(tuple, member_value)
        L = len(member_value)
        for case in reversed(range(L)):
            submember_value = member_value[case]
            submember_getter = sf.get_submember_getter_at_case(case)
            submember_getter.check_member_value(submember_value)
        return
    @override
    def ___iter_cased_subpackets_from_packet___(sf, packet, /):
        'packet -> Iter (case, subpacket)'
        check_type_is(tuple, packet)
        return enumerate(packet)
    @override
    def ___mk_tmay_member_value_from_cased_tmay_submember_value_iterator___(sf, cased_tmay_submember_value_iterator, /):
        'Iter (case, tmay submember_value) -> tmay_member_value'
        ls = []
        for i, (case, tmay_submember_value) in enumerate(cased_tmay_submember_value_iterator):
            if i != case: raise TypeError
            if not tmay_submember_value:
                tmay_member_value = ()
                break
            [submember_value] = tmay_submember_value
            ls.append(submember_value)
        else:
            member_value = tuple(ls)
            tmay_member_value = (member_value,)
        return tmay_member_value
    @override
    def check_switch_case4submember_getter(sf, case, /):
        if type(case) is bool:
            return
        check_uint(case)

class IMemberGetter__parallel_pair(IMemberGetter__parallel_tuple):
    'parallel_pair'
    __slots__ = ()
    @override
    def check_switch_case4submember_getter(sf, case, /):
        #check_bool(case)
        super().check_switch_case4submember_getter(case)
        if not 0 <= case < 2: raise TypeError
class IMemberGetter__switch_either(IMemberGetter__switch):
    'switch_either'
    __slots__ = ()
    @override
    def check_switch_case4submember_getter(sf, case, /):
        check_bool(case)
        super().check_switch_case4submember_getter(case)

class IAutoMemberGetter__switch(IMemberGetter__switch, IAutoMemberGetter__cased_subpackets):
    __slots__ = ()
class IAutoMemberGetter__parallel_mapping(IMemberGetter__parallel_mapping, IAutoMemberGetter__cased_subpackets):
    __slots__ = ()
class IAutoMemberGetter__parallel_tuple(IMemberGetter__parallel_tuple, IAutoMemberGetter__cased_subpackets):
    __slots__ = ()
class IAutoMemberGetter__switch_either(IMemberGetter__switch_either, IAutoMemberGetter__switch):
    __slots__ = ()
class IAutoMemberGetter__parallel_pair(IMemberGetter__parallel_pair, IAutoMemberGetter__parallel_tuple):
    __slots__ = ()

class IMemberGetter__wrap_member_getter(IMemberGetter):
    __slots__ = ()
    @abstractmethod
    def ___get_the_wrapped_member_getter___(sf, case, /):
        'get_the_wrapped_member_getter; -> the_wrapped_member_getter::IMemberGetter'
    def get_the_wrapped_member_getter(sf, case, /):
        '___get_the_wrapped_member_getter___; -> the_wrapped_member_getter::IMemberGetter'
        the_wrapped_member_getter = type(sf).___get_the_wrapped_member_getter___(sf)
        sf.check_the_wrapped_member_getter(the_wrapped_member_getter)
        return the_wrapped_member_getter
    def check_the_wrapped_member_getter(sf, the_wrapped_member_getter, /):
        check_instance(IMemberGetter, the_wrapped_member_getter)
        return
class IMemberGetter__apply(IMemberGetter__wrap_member_getter):
    'mget x (i, mget i o) -> mget x o #apply'
    __slots__ = ()

    @override
    def ___get_member__tmay___(sf, packet, /):
        'get_member__tmay(); -> tmay member_value'
        the_wrapped_member_getter = sf.get_the_wrapped_member_getter()
        tmay_transitional_member_value = the_wrapped_member_getter.get_member__tmay(packet)
        if tmay_transitional_member_value:
            [transitional_member_value] = tmay_transitional_member_value
            check_pair(tmay_transitional_member_value)
            (_packet, _member_getter) = transitional_member_value
            sf.check_transitional_member_getter(_member_getter)
            tmay_member_value = _member_getter.get_member__tmay(_packet)
        else:
            tmay_member_value = ()
        return tmay_member_value
    def check_transitional_member_getter(sf, transitional_member_getter, /):
        check_instance(IMemberGetter, transitional_member_getter)
        return

class IMemberGetter__collapse(IMemberGetter__wrap_member_getter):
    'mget i (mget i o) -> mget i o #collapse'
    __slots__ = ()

    @override
    def ___get_member__tmay___(sf, packet, /):
        'get_member__tmay(); -> tmay member_value'
        the_wrapped_member_getter = sf.get_the_wrapped_member_getter()
        tmay_transitional_member_value = the_wrapped_member_getter.get_member__tmay(packet)
        if tmay_transitional_member_value:
            [transitional_member_value] = tmay_transitional_member_value
            _member_getter = transitional_member_value
            sf.check_transitional_member_getter(_member_getter)
            tmay_member_value = _member_getter.get_member__tmay(packet)
        else:
            tmay_member_value = ()
        return tmay_member_value
    def check_transitional_member_getter(sf, transitional_member_getter, /):
        check_instance(IMemberGetter, transitional_member_getter)
        return


#class IIndirectMemberGetter(IMemberGetter__wrap_member_getter):

class IIndirectMemberGetter(IMemberGetter):
    #class IIndirectMemberGetter(IMemberGetter, ___1, ___2, ___0):
    r'''(i->tmay h) -> (h->tmay (mget i o)) -> mget i o  #indirect
    ----
    (mget i h) -> (mget h (mget i o)) -> mget i o  #indirect === collapse . chain<i2h,h2i2o>

    #################################
    #################################
    indirect_member_getter
    IndirectMemberGetter
    IIndirectMemberGetter
        (packet, member_getter) -> (new_packet, new_member_getter)|(member_getter,)|()
        => packet.handler4packet.target_member_getter<sf.packet, sf.member_value>
        ---
        member_getter not change:
            (sf, packet, state4member_getter) -> (new_packet, new_state4member_getter)|(member_getter,)|()
        ---
        packet not change:
            (sf, packet) -> new_member_getter|(member_getter,)|()
        ---
        mix:
            (sf, packet) -> tmay target_member_getter
                (sf, packet) -> (tmay handler4packet, tmay handler4target_member_getter)
                #member_getter4handler4packet
                #member_getter4handler4target_member_getter/member_register4handler4target_member_getter
                (sf, handler4packet, handler4target_member_getter) -> target_member_getter

    #'''
    __slots__ = ()
    @abstractmethod
    def ___get_handler4packet_from_packet__tmay___(sf, packet, /):
        'get_handler4packet_from_packet__tmay(); -> tmay handler4packet'
    @abstractmethod
    def ___get_target_member_getter_from_handler4packet__tmay___(sf, handler4packet, /):
        'get_target_member_getter_from_handler4packet__tmay(); -> tmay target_member_getter'
        #tmay_handler4target_member_getter = sf.get_handler4target_member_getter_from_handler4packet__tmay(handler4packet)
        #check_tmay

    def get_handler4packet_from_packet__tmay(sf, packet, /):
        '___get_handler4packet_from_packet__tmay___(); -> tmay handler4packet'
        sf.check_packet(packet)
        tmay_handler4packet = type(sf).___get_handler4packet_from_packet__tmay___(sf, packet)
        check_tmay(tmay_handler4packet)
        if tmay_handler4packet: sf.check_handler4packet(*tmay_handler4packet)
        return tmay_handler4packet
    def get_target_member_getter_from_handler4packet__tmay(sf, handler4packet, /):
        '___get_target_member_getter_from_handler4packet__tmay___(); -> tmay target_member_getter'
        sf.check_handler4packet(handler4packet)
        tmay_target_member_getter = type(sf).___get_target_member_getter_from_handler4packet__tmay___(sf, handler4packet)
        check_tmay(tmay_target_member_getter)
        if tmay_target_member_getter: sf.check_target_member_getter(*tmay_target_member_getter)
        return tmay_target_member_getter

    #def get_handler4target_member_getter_from_handler4packet__tmay(sf, handler4packet, /):
        '-> tmay handler4target_member_getter'

    @abstractmethod
    def check_handler4packet(sf, handler4packet, /):
        return
    def check_target_member_getter(sf, target_member_getter, /):
        check_instance(IMemberGetter, target_member_getter)

    @override
    def ___get_member__tmay___(sf, packet, /):
        'get_member__tmay(); -> tmay member_value'
        tmay_handler4packet = sf.get_handler4packet_from_packet__tmay(packet)
        if not tmay_handler4packet:
            return ()
        [handler4packet] = tmay_handler4packet
        del tmay_handler4packet

        tmay_target_member_getter = sf.get_target_member_getter_from_handler4packet__tmay(handler4packet)
        if not tmay_target_member_getter:
            return ()
        [target_member_getter] = tmay_target_member_getter
        del tmay_target_member_getter

        handler4packet
        target_member_getter
        del handler4packet
        return target_member_getter.get_member__tmay(packet)




#assert (IIndirectMemberGetter.__abstractmethods__) == frozenset({'check_handler4packet', 'check_packet', '___get_handler4packet_from_packet__tmay___', 'check_member_value', '___get_target_member_getter_from_handler4packet__tmay___'}), (IIndirectMemberGetter.__abstractmethods__)
check_manifest4abstractmethods(IIndirectMemberGetter, r'''
        check_packet
        check_member_value
        check_handler4packet
        ___get_handler4packet_from_packet__tmay___
        ___get_target_member_getter_from_handler4packet__tmay___
    #''')
#class IIndirectMemberGetter(IMemberGetter, ___1, ___2, ___0):



Iter i -> (i -> Maybe o) -> mget (Iter i) o
Iter i -> (i -> o) -> mget (Iter i) (Iter o)
cls --> (__mro__::[cls]) --> (Iter __dict__) --> cls.x



r'''
prototype_mro.PseudoMapping...=> one member_getter, many intermediate_obj/transitional_obj
    OR-priority-choice-alternatives
concrete:
    __call__:
        callable :: packet -> member_value
            wrap :: packet -> wrapper<packet>
        callable :: packet -> tmay_member_value
        callable :: packet -> may member_value
        callable :: Nothing -> packet -> member_value|Nothing
    __getitem__:
        key -> PseudoMapping<packet>.get/setdefault
        idx -> Seq<packet>[idx]
    __getattribute__
        attr -> getattr(packet, attr) / setattr(packet, attr, member_value)
#'''


#]]]MemberGetter:end

#[[[MemberRegister:begin
class IMemberPatcher(IMemberGetter, ___2, ___0, ___1):
    r'''
    asymmetry<input=plugin4member, output=member_value>
        why?
            plugin4member may be member_getter...
            member_value may be view...
    #'''
    __slots__ = ()

    @abstractmethod
    def check_plugin4member(sf, plugin4member, /):
        'plugin4member <: member_value; plugin4member is valid member_value, but member_value may not be valid plugin4member'
        if sf.get_relationship_between_plugin4member_and_member_value():
            sf.check_member_value(plugin4member)
        return
    def check_pre_patch_plugin4member(sf, packet, plugin4member, /):
        sf.check_plugin4member(plugin4member)
        relationship = sf.get_relationship_between_plugin4member_and_member_value()
        if relationship != 0:
            # <: |  == | is
            #plugin4member is valid member_value
            sf.check_member_value(plugin4member)
    def check_post_patch_plugin4member(sf, packet, plugin4member, new_member_value, /):
        relationship = sf.get_relationship_between_plugin4member_and_member_value()
        if 1 != relationship != 0:
            # == | is
            if relationship == 3:
                if not new_member_value is plugin4member: raise logic-err
            elif relationship == 2:
                if not (new_member_value is plugin4member or new_member_value == plugin4member): raise logic-err
            else:
                raise logic-err
    @abstractmethod
    def ___get_relationship_between_plugin4member_and_member_value___(sf, /):
        'get_relationship_between_plugin4member_and_member_value(); -> [0,1,2,3] #0:None, 1:SUBSET,2:EQ,3:IS # 1:plugin-is-valid-member_value, 2:plugin-EQ-result-member_value, 3:plugin-IS-result-member_value'
    def get_relationship_between_plugin4member_and_member_value(sf, /):
        '___get_relationship_between_plugin4member_and_member_value___(); -> [0,1,2,3] #0:None, 1:SUBSET,2:EQ,3:IS # 1:plugin-is-valid-member_value, 2:plugin-EQ-result-member_value, 3:plugin-IS-result-member_value'
        # <> | <: |  == | is
        relationship = type(sf).___get_relationship_between_plugin4member_and_member_value___(sf)
        check_int(relationship, min=0, max=3)
        return relationship
    @abstractmethod
    def ___patch_member__plugin___(sf, packet, plugin4member, /):
        'patch_member__xplugin(); -> None|raise ???'
    def patch_member__xplugin(sf, packet, imay_xplugin_rank, xplugin4member, /, member_exist_ok):
        '___patch_member__plugin___(); -> (tmay_plugin4member, member_value)|raise ???'
        check_bool(member_exist_ok)
        (is_member_value, default_or_member_value) = sf.get_member__xdefault__cased(packet, imay_xplugin_rank, xplugin4member)
        if not is_member_value:
            default = default_or_member_value
            plugin4member = default
                #default should be plugin4member, but may not be member_value
            sf.check_pre_patch_plugin4member(packet, plugin4member)
            _ = type(sf).___patch_member__plugin___(sf, packet, plugin4member)
            check_is_None(_)
            tmay_member_value = sf.get_member__tmay(packet)
            if not tmay_member_value: raise logic-err#patched, but get Nothing
            [new_member_value] = tmay_member_value
            sf.check_post_patch_plugin4member(packet, plugin4member, new_member_value)
            member_value = new_member_value
            tmay_plugin4member = (plugin4member,)
            pass
        else:
            old_member_value = default_or_member_value
            if not member_exist_ok: raise LookupError('member exists')
            member_value = old_member_value
            tmay_plugin4member = ()
        return tmay_plugin4member, member_value


#assert (IMemberPatcher.__abstractmethods__) == frozenset({'___get_relationship_between_plugin4member_and_member_value___', 'check_member_value', '___patch_member__plugin___', '___get_member__tmay___', 'check_plugin4member', 'check_packet'}), (IMemberPatcher.__abstractmethods__)
check_manifest4abstractmethods(IMemberPatcher, r'''
        check_packet
        check_member_value
        ___get_member__tmay___
        check_plugin4member
        ___patch_member__plugin___
        ___get_relationship_between_plugin4member_and_member_value___
    #''')
#class IMemberPatcher(IMemberGetter, ___2, ___0, ___1):


class IMemberSetter(IMemberPatcher):
    __slots__ = ()

    r'''IMemberAdaptor impl ___patch_member__plugin___, donot known ___set_member__value___
    -----
    @abstractmethod
    def ___set_member__value___(sf, packet, member_value, /):
        'set_member__xvalue(); -> None|raise ???'
    @override
    def ___patch_member__plugin___(sf, packet, plugin4member, /):
        'patch_member__xplugin(); -> None|raise ???'
        member_value = plugin4member
        type(sf).___set_member__value___(member_value)
    #'''


    def set_member__xvalue(sf, packet, imay_xvalue_rank, xvalue4member, /, member_exist_ok):
        '-> (is_new_value, member_value)|raise ???'
        ##'___set_member__value___(); -> (is_new_value, member_value)|raise ???'
        (tmay_new_value, member_value_from_get) = super().patch_member__xplugin(packet, imay_xvalue_rank, xvalue4member, member_exist_ok=member_exist_ok)
        is_new_value = bool(tmay_new_value)
        if is_new_value:
            [new_member_value_from_xvalue] = tmay_new_value
            if not new_member_value_from_xvalue is member_value_from_get: raise logic-err
        return (is_new_value, member_value_from_get)

    r'''
    @abstractmethod
    @override
    def check_member_value(sf, member_value, /):
        super().check_member_value(member_value)
        plugin4member = member_value
            bug!!!  plugin4member <: member_value;
        return
    #'''
    @override
    def check_plugin4member(sf, plugin4member, /):
        'plugin4member <: member_value; plugin4member is valid member_value, but member_value may not be valid plugin4member'
        super().check_plugin4member(plugin4member)
            #remove @abstractmethod by @override
        return
        member_value = plugin4member
            #plugin4member <: member_value;
        sf.check_member_value(member_value)
        return
    @override
    def ___get_relationship_between_plugin4member_and_member_value___(sf, /):
        'get_relationship_between_plugin4member_and_member_value(); -> [0,1,2,3] #0:None, 1:SUBSET,2:EQ,3:IS # 1:plugin-is-valid-member_value, 2:plugin-EQ-result-member_value, 3:plugin-IS-result-member_value'
        return 3#IS
    @override
    def patch_member__xplugin(sf, packet, imay_xplugin_rank, xplugin4member, /, member_exist_ok):
        '___patch_member__plugin___(); -> (tmay_plugin4member, member_value)|raise ???'
        (is_new_value, member_value) = sf.set_member__xvalue(packet, imay_xplugin_rank, xplugin4member, member_exist_ok=member_exist_ok)
        plugin4member = member_value
        tmay_plugin4member = (plugin4member,) if is_new_value else ()
        return tmay_plugin4member, member_value
class IAutoMemberPatcher(IMemberPatcher, IAutoMemberGetter):#(, IRigidMemberGetter):
    r'''
    why not [IAutoMemberPatcher <: IRigidMemberGetter]?
        IRigidMemberGetter::get_member__tmay <<== get_member__rigid
        IAutoMemberPatcher::get_member__auto_install <<== [get_member__tmay, ...]
        if get_member__rigid := get_member__auto_install: recur-inf

        IAutoMemberPatcher.get_member__tmay is used to detect whether registered
        IRigidMemberGetter.get_member__tmay should return (Just member_value) (never Nothing)
        hence incompatible<IMemberPatcher,IRigidMemberGetter>
        hence incompatible<IAutoMemberPatcher,IRigidMemberGetter>
        hence incompatible<IMemberSetter,IRigidMemberGetter>
        hence incompatible<IAutoMemberSetter,IRigidMemberGetter>
    #'''
    __slots__ = ()


    @abstractmethod
    def ___mk_plugin4member_on_default___(sf, packet, /):
        'mk_plugin4member_on_default(); -> plugin4member'
    def mk_plugin4member_on_default(sf, packet, /):
        '___mk_plugin4member_on_default___(); -> plugin4member'
        sf.check_packet(packet)
        plugin4member = type(sf).___mk_plugin4member_on_default___(sf, packet)
        sf.check_plugin4member(plugin4member)
        return plugin4member
    def patch_member__default(sf, packet, /, member_exist_ok):
        '-> (tmay_plugin4member, member_value)|raise ???'
        return sf.patch_member__xplugin(packet, 1, sf.mk_plugin4member_on_default, member_exist_ok=member_exist_ok)

    @override
    def ___auto_install_member___(sf, packet, /):
        'get_or_auto_install_member(); -> None'
        sf.patch_member__default(packet, member_exist_ok=False)
        return

#assert (IAutoMemberPatcher.__abstractmethods__) == frozenset({'check_plugin4member', '___get_member__tmay___', '___patch_member__plugin___', 'check_member_value', '___mk_plugin4member_on_default___', 'check_packet', '___get_relationship_between_plugin4member_and_member_value___'}), (IAutoMemberPatcher.__abstractmethods__)
check_manifest4abstractmethods(IAutoMemberPatcher, r'''
        check_packet
        check_member_value
        ___get_member__tmay___
        check_plugin4member
        ___patch_member__plugin___
        ___get_relationship_between_plugin4member_and_member_value___
        ___mk_plugin4member_on_default___
    #''')
#class IAutoMemberPatcher(IMemberPatcher, IAutoMemberGetter):#(, IRigidMemberGetter):

class IAutoMemberSetter(IMemberSetter, IAutoMemberPatcher):
    __slots__ = ()
#end-class IAutoMemberSetter(IMemberSetter, IAutoMemberPatcher):
#assert (IAutoMemberSetter.__abstractmethods__) == frozenset({'___get_member__tmay___', '___patch_member__plugin___', 'check_member_value', '___mk_plugin4member_on_default___', 'check_packet'}), (IAutoMemberSetter.__abstractmethods__)
check_manifest4abstractmethods(IAutoMemberSetter, r'''
        check_packet
        check_member_value
        ___get_member__tmay___
        ___patch_member__plugin___
        ___mk_plugin4member_on_default___
    #''')

#]]]MemberRegister:end


#[[[MemberAdaptor:begin
class IIndirectMemberGetter__via_collapse(IIndirectMemberGetter):
    r'''(mget i h) -> (mget h h2) -> (h -> h2 -> (mget i o)) -> mget i o
    #(mget i h) -> (mget h (mget i o)) -> mget i o  #indirect === collapse . chain<i2h,h2i2o>

    #################################
    handler4packet: eg. type(packet)
    handler4target_member_getter: eg. attr
    #################################
    IMemberAdaptor
        .fst=IMemberGetter<packet, handler4packet>
        .snd=IMemberGetter<handler4packet, handler4target_member_getter>
        #return what? tmay_member_value? apply__handler4target_member_getter(handler4target_member_getter, packet)->tmay_member_value
        mk_target_member_getter_from_handler(handler4packet, handler4target_member_getter)->member_getter
            :: handler4target_member_getter -> IMemberGetter<packet, member_value>

    #'''
    __slots__ = ()

    @abstractmethod
    def ___mk_target_member_getter_from_handler___(sf, handler4packet, handler4target_member_getter, /):
        'mk_target_member_getter_from_handler(); -> target_member_getter~IMemberGetter<sf> :: IMemberGetter<packet=sf.packet, member_value=sf.member_value>'
    @abstractmethod
    def ___get_member_getter4handler4packet___(sf, /):
        'get_member_getter4handler4packet(); -> member_getter4handler4packet :: IMemberGetter<packet=packet, member_value=handler4packet>'
    @abstractmethod
    def ___get_member_getter4handler4target_member_getter___(sf, /):
        'get_member_getter4handler4target_member_getter(); -> member_getter4handler4target_member_getter :: IMemberGetter<packet=handler4packet, member_value=handler4target_member_getter>'



    def check_member_getter4handler4packet(sf, member_getter4handler4packet, /):
        check_instance(IMemberGetter, member_getter4handler4packet)
    def check_member_getter4handler4target_member_getter(sf, member_getter4handler4target_member_getter, /):
        check_instance(IMemberGetter, member_getter4handler4target_member_getter)



    def get_member_getter4handler4packet(sf, /):
        '___get_member_getter4handler4packet___(); -> member_getter4handler4packet :: IMemberGetter<packet=packet, member_value=handler4packet>'
        member_getter4handler4packet = type(sf).___get_member_getter4handler4packet___(sf)
        sf.check_member_getter4handler4packet(member_getter4handler4packet)
        return member_getter4handler4packet
    def get_member_getter4handler4target_member_getter(sf, /):
        '___get_member_getter4handler4target_member_getter___(); -> member_getter4handler4target_member_getter :: IMemberGetter<packet=handler4packet, member_value=handler4target_member_getter>'
        member_getter4handler4target_member_getter = type(sf).___get_member_getter4handler4target_member_getter___(sf)
        sf.check_member_getter4handler4target_member_getter(member_getter4handler4target_member_getter)
        return member_getter4handler4target_member_getter

    def mk_target_member_getter_from_handler(sf, handler4packet, handler4target_member_getter, /):
        '___mk_target_member_getter_from_handler___(); -> target_member_getter~IMemberGetter<sf> :: IMemberGetter<packet=sf.packet, member_value=sf.member_value>'
        sf.check_handler4packet(handler4packet)
        sf.check_handler4target_member_getter(handler4target_member_getter)
        target_member_getter = type(sf).___mk_target_member_getter_from_handler___(sf, handler4packet, handler4target_member_getter)
        sf.check_target_member_getter(target_member_getter)
        return target_member_getter





    @override
    def check_handler4packet(sf, handler4packet, /):
        member_getter4handler4packet = sf.get_member_getter4handler4packet()
        member_getter4handler4packet.check_member_value(handler4packet)
        del member_getter4handler4packet
        member_getter4handler4target_member_getter = sf.get_member_getter4handler4target_member_getter()
        member_getter4handler4target_member_getter.check_packet(handler4packet)
        del member_getter4handler4target_member_getter
        return
    def check_handler4target_member_getter(sf, handler4target_member_getter, /):
        member_getter4handler4target_member_getter = sf.get_member_getter4handler4target_member_getter()
        member_getter4handler4target_member_getter.check_member_value(handler4target_member_getter)
        return

    @override
    def check_packet(sf, packet, /):
        member_getter4handler4packet = sf.get_member_getter4handler4packet()
        member_getter4handler4packet.check_packet(packet)
        return

    @override
    def ___get_handler4packet_from_packet__tmay___(sf, packet, /):
        'get_handler4packet_from_packet__tmay(); -> tmay handler4packet'
        member_getter4handler4packet = sf.get_member_getter4handler4packet()
        tmay_handler4packet = member_getter4handler4packet.get_member__tmay(packet)
        return tmay_handler4packet
    @override
    def ___get_target_member_getter_from_handler4packet__tmay___(sf, handler4packet, /):
        'get_target_member_getter_from_handler4packet__tmay(); -> tmay target_member_getter'
        member_getter4handler4target_member_getter = sf.get_member_getter4handler4target_member_getter()
        tmay_handler4target_member_getter = member_getter4handler4target_member_getter.get_member__tmay(handler4packet)
        del member_getter4handler4target_member_getter
        if not tmay_handler4target_member_getter:
            return ()
        [handler4target_member_getter] = tmay_handler4target_member_getter
        #sf.check_handler4target_member_getter(handler4target_member_getter)
        del tmay_handler4target_member_getter
        target_member_getter = sf.mk_target_member_getter_from_handler(handler4packet, handler4target_member_getter)
        return (target_member_getter,)
    r'''
    @override
    def ___get_member__tmay___(sf, packet, /):
        'get_member__tmay(); -> tmay member_value'
        member_getter4handler4packet = sf.get_member_getter4handler4packet()
        tmay_handler4packet = member_getter4handler4packet.get_member__tmay(packet)
        del member_getter4handler4packet
        if not tmay_handler4packet:
            return ()
        [handler4packet] = tmay_handler4packet
        sf.check_handler4packet(handler4packet)
        del tmay_handler4packet

        member_getter4handler4target_member_getter = sf.get_member_getter4handler4target_member_getter()
        tmay_handler4target_member_getter = member_getter4handler4target_member_getter.get_member__tmay(handler4packet)
        del member_getter4handler4target_member_getter
        if not tmay_handler4target_member_getter:
            return ()
        [handler4target_member_getter] = tmay_handler4target_member_getter
        sf.check_handler4target_member_getter(handler4target_member_getter)
        del tmay_handler4target_member_getter

        handler4packet
        handler4target_member_getter
        target_member_getter = sf.mk_target_member_getter_from_handler(handler4packet, handler4target_member_getter)
        sf.check_target_member_getter(target_member_getter)
        return target_member_getter.get_member__tmay(packet)
    #'''
#assert (IIndirectMemberGetter__via_collapse.__abstractmethods__) == frozenset({'___get_member_getter4handler4target_member_getter___', '___get_member_getter4handler4packet___', 'check_member_value', '___mk_target_member_getter_from_handler___'}), (IIndirectMemberGetter__via_collapse.__abstractmethods__)
check_manifest4abstractmethods(IIndirectMemberGetter__via_collapse, r'''
        check_member_value
        ___get_member_getter4handler4packet___
        ___get_member_getter4handler4target_member_getter___
        ___mk_target_member_getter_from_handler___
    #''')



class IMemberAdaptor(IIndirectMemberGetter__via_collapse, IMemberPatcher):
    #class IMemberAdaptor(IIndirectMemberGetter__via_collapse, ___1, ___2, ___0):
    r'''(mget-auto i h) -> (mget-patcher h h2) -> (h -> h2 -> (mget i o)) -> mget i o
    #'''
    __slots__ = ()
    @override
    def check_member_getter4handler4packet(sf, member_getter4handler4packet, /):
        check_instance(IAutoMemberGetter, member_getter4handler4packet)
        super().check_member_getter4handler4packet(member_getter4handler4packet)
    @override
    def check_member_getter4handler4target_member_getter(sf, member_getter4handler4target_member_getter, /):
        check_instance(IMemberPatcher, member_getter4handler4target_member_getter)
        super().check_member_getter4handler4target_member_getter(member_getter4handler4target_member_getter)

    @override
    def check_plugin4member(sf, plugin4member, /):
        'plugin4member <: member_value; plugin4member is valid member_value, but member_value may not be valid plugin4member'
        super().check_plugin4member(plugin4member)
        member_getter4handler4target_member_getter = sf.get_member_getter4handler4target_member_getter()
        member_patcher = member_getter4handler4target_member_getter
        member_patcher.check_plugin4member(plugin4member)
    @override
    def ___patch_member__plugin___(sf, packet, plugin4member, /):
        'patch_member__xplugin(); -> None|raise ???'
        member_getter4handler4packet = sf.get_member_getter4handler4packet()
        handler4packet = member_getter4handler4packet.get_or_auto_install_member(packet)
        sf.patch_member__xplugin__via_handler4packet(handler4packet, -1, plugin4member)

    #register
    def patch_member__xplugin__via_handler4packet(sf, handler4packet, imay_xplugin_rank, xplugin4member, /, member_exist_ok):
        '-> tmay_plugin4member|raise ???'
        member_getter4handler4target_member_getter = sf.get_member_getter4handler4target_member_getter()
        member_patcher = member_getter4handler4target_member_getter

        (tmay_plugin4member, __member_value) = member_patcher.patch_member__xplugin(handler4packet, imay_xplugin_rank, xplugin4member, member_exist_ok=member_exist_ok)
        return tmay_plugin4member

    @override
    def ___get_relationship_between_plugin4member_and_member_value___(sf, /):
        'get_relationship_between_plugin4member_and_member_value(); -> [0,1,2,3] #0:None, 1:SUBSET,2:EQ,3:IS # 1:plugin-is-valid-member_value, 2:plugin-EQ-result-member_value, 3:plugin-IS-result-member_value'
        return 0#no-relation
    r'''
    def register_handler4target_member_getter__xvalue__via_handler4packet(sf, handler4packet, imay_xvalue_rank4handler4target_member_getter, xvalue4handler4target_member_getter, /, registered_ok):
        sf.check_handler4packet(handler4packet)
        member_register4handler4target_member_getter = sf.get_member_register4handler4target_member_getter()
        member_register4handler4target_member_getter.register_member__xvalue(handler4packet, imay_xvalue_rank4handler4target_member_getter, xvalue4handler4target_member_getter, registered_ok=registered_ok)
    def register_handler4target_member_getter__xvalue__via_packet(sf, packet, imay_xvalue_rank4handler4target_member_getter, xvalue4handler4target_member_getter, /, registered_ok):
        sf.check_packet(packet)
        member_getter4handler4packet = sf.get_member_getter4handler4packet()
        handler4packet = member_getter4handler4packet.get_or_auto_install_member(packet)
        sf.check_handler4packet(handler4packet)
        del member_getter4handler4packet

        sf.register_handler4target_member_getter__xvalue__via_handler4packet(handler4packet, imay_xvalue_rank4handler4target_member_getter, xvalue4handler4target_member_getter, registered_ok=registered_ok)
    def register_member__xvalue(sf, packet, imay_xvalue_rank, xvalue, /, registered_ok):
        #'''

#assert (IMemberAdaptor.__abstractmethods__) == frozenset({'___get_member_getter4handler4packet___', '___get_member_getter4handler4target_member_getter___', 'check_member_value', '___mk_target_member_getter_from_handler___'}), (IMemberAdaptor.__abstractmethods__)
check_manifest4abstractmethods(IMemberAdaptor, r'''
        check_member_value
        ___get_member_getter4handler4packet___
        ___get_member_getter4handler4target_member_getter___
        ___mk_target_member_getter_from_handler___
    #''')
#class IMemberAdaptor(IMemberGetter, ___1, ___2, ___0):
IIndirectMemberGetter

class IAutoMemberAdaptor(IMemberAdaptor, IAutoMemberPatcher):
    __slots__ = ()
    @abstractmethod
    def ___mk_plugin4member_on_default__via_handler4packet___(sf, handler4packet, /):
        'mk_plugin4member_on_default__via_handler4packet(); -> plugin4member'

    def mk_plugin4member_on_default__via_handler4packet(sf, handler4packet, /):
        '___mk_plugin4member_on_default__via_handler4packet___(); -> plugin4member'
        sf.check_packet(handler4packet)
        plugin4member = type(sf).___mk_plugin4member_on_default__via_handler4packet___(sf, handler4packet)
        sf.check_plugin4member(plugin4member)
        return plugin4member

    def patch_member__default__via_handler4packet(sf, handler4packet, /, member_exist_ok):
        '-> tmay_plugin4member|raise ???'
        return sf.patch_member__xplugin__via_handler4packet(handler4packet, 1, sf.mk_plugin4member_on_default__via_handler4packet, member_exist_ok=member_exist_ok)
    @override
    def ___mk_plugin4member_on_default___(sf, packet, /):
        'mk_plugin4member_on_default(); -> plugin4member'
        member_getter4handler4packet = sf.get_member_getter4handler4packet()
        handler4packet = member_getter4handler4packet.get_or_auto_install_member(packet)
        return sf.mk_plugin4member_on_default__via_handler4packet(handler4packet)

#assert (IAutoMemberAdaptor.__abstractmethods__) == frozenset({'___get_member_getter4handler4packet___', '___get_member_getter4handler4target_member_getter___', 'check_member_value', '___mk_target_member_getter_from_handler___', '___mk_plugin4member_on_default__via_handler4packet___'}), (IAutoMemberAdaptor.__abstractmethods__)
check_manifest4abstractmethods(IAutoMemberAdaptor, r'''
        check_member_value
        ___get_member_getter4handler4packet___
        ___get_member_getter4handler4target_member_getter___
        ___mk_target_member_getter_from_handler___
        ___mk_plugin4member_on_default__via_handler4packet___
    #''')





#]]]MemberAdaptor:end

#[[[MemberGetter__mixin:begin
r'''
attr: x -> x.__dict__
key: x -> x[k]
call: x -> x(*args, **kwargs)
func: x -> f(x, *args, **kwargs) #type(x)
extern: x -> extern[x]

#'''
#]]]MemberGetter__mixin:end

#[[[zzzwww:begin
def _t2(A, B):
    class C(A, B):
        __slots__ = ()
assert not expectError(Exception, lambda:_t2(___0, IMemberGetter))
def _t_permutation2(*Bs):
    #from itertools import product
    #it = product(2, Bs)
    for A in Bs:
        for B in Bs:
            if A is not B:
                assert expectError(Exception, lambda:_t2(A, B))
#_t_permutation2(IRigidMemberGetter, IMemberRegister, IMemberAdaptor)
#_t_permutation2(IRigidMemberGetter, IMemberPatcher, IMemberAdaptor)
_t_permutation2(IRigidMemberGetter, IMemberPatcher)
_t_permutation2(IRigidMemberGetter, IMemberAdaptor)



r"""[[[[[
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
class IMemberGetter__composite___using_fixed_len_tuple4member_getters4composite(IMemberGetter__composite):
    #class IMemberGetter__chain___chain_is_fixed_len_tuple(IMemberGetter__chain):
    __slots__ = ()

    @classmethod
    @abstractmethod
    class ___the_number_of_member_getters4composite___:
        #class ___the_number_of_member_getters_in_chain___:
        'get_number_of_member_getters4composite(); -> uint'
    @classmethod
    def get_number_of_member_getters4composite(cls, /):
        #def get_number_of_member_getters_in_chain(cls, /):
        '___the_number_of_member_getters4composite___(); -> uint'
        sz = cls.___the_number_of_member_getters4composite___
        check_type_is(int, sz)
        if not sz >= 0: raise TypeError
        return sz
    @abstractmethod
    def ___get_member_getters4composite_as_tuple___(sf, /):
        #def ___get_chain_of_member_getters__tuple___(sf, /):
        'get_member_getters4composite_as_tuple(); -> tuple<IMemberGetter>'
    def get_member_getters4composite_as_tuple(sf, /):
        #def get_chain_of_member_getters__tuple(sf, /):
        '___get_member_getters4composite_as_tuple___(); -> tuple<IMemberGetter>'
        member_getters = type(sf).___get_member_getters4composite_as_tuple___(sf)
        sf._shallow_check_member_getters4composite_as_tuple(member_getters)
        if not sf.___checked__check_member_getters4composite_as_tuple___:
            sf.check_member_getters4composite_as_tuple(member_getters)
            sf.___checked__check_member_getters4composite_as_tuple___ = True
            if not sf.___checked__check_member_getters4composite_as_tuple___: raise TypeError
        return member_getters
    def get_member_getter4composite_at_index(sf, i, /):
        #def get_member_getter_in_chain_at_index(sf, i, /):
        check_int(i)
        return sf.get_member_getters4composite_as_tuple()[i]

    def _shallow_check_member_getters4composite_as_tuple(sf, member_getters, /):
        #def _shallow_check_chain_of_member_getters__tuple(sf, member_getters, /):
        check_type_is(tuple, member_getters)
        if not len(member_getters) == type(sf).get_number_of_member_getters4composite(): raise TypeError

    @property
    @abstractmethod
    def ___checked__check_member_getters4composite_as_tuple___(sf, /):
        #def ___checked__check_chain_of_member_getters__tuple___(sf, /):
        '-> bool; turnon-only'
    def check_member_getters4composite_as_tuple(sf, member_getters, /):
        #def check_chain_of_member_getters__tuple(sf, member_getters, /):
        sf._shallow_check_member_getters4composite_as_tuple(member_getters)
        for member_getter in member_getters:
            sf.check_member_getter_in_chain(member_getter)

    @override
    def ___iter_member_getters4composite___(sf, /):
        'iter_member_getters4composite(); -> Iter<IMemberGetter>'
        return iter(sf.get_member_getters4composite_as_tuple())
#class IMemberGetter__composite___using_fixed_len_tuple4member_getters4composite(IMemberGetter__chain):



class IMemberGetter__composite___using_fixed_len_type_schema_tuple4member_getters4composite(IMemberGetter__composite___using_fixed_len_tuple4member_getters4composite):
    #class IMemberGetter__chain___chain_with_fixed_len_type_schema_tuple(IMemberGetter__composite___using_fixed_len_tuple4member_getters4composite):
    __slots__ = ()

    @classmethod
    @abstractmethod
    class ___base_cls_schema_tuple4member_getters4composite___:
        #class ___base_cls_tuple4member_getters_in_chain___:
        ' :: tuple<base_cls<sub-member_getter> >'

    @classmethod
    @override
    def get_base_cls_schema_tuple4member_getters4composite(cls, /):
        #def get_base_cls_schema_tuple4member_getters4composite(cls, /):
        #def get_base_cls_tuple4member_getters_in_chain(cls, /):
        bases = cls.___base_cls_schema_tuple4member_getters4composite___
        check_type_is(tuple, bases)
        if len(bases) != cls.get_number_of_member_getters4composite(): raise TypeError
        return bases

    @override
    def check_member_getters4composite_as_tuple(sf, member_getters, /):
        super().check_member_getters4composite_as_tuple(member_getters)
        cls = type(sf)
        bases = cls.get_base_cls_schema_tuple4member_getters4composite()
        assert len(bases) == len(member_getters)
        for base_cls, member_getter in zip(bases, member_getters):
            check_instance(base_cls, member_getter)
#class IMemberGetter__composite___using_fixed_len_type_schema_tuple4member_getters4composite(IMemberGetter__composite___using_fixed_len_tuple4member_getters4composite):

#chain

class IMemberGetter__chain___chain_is_pair(IMemberGetter__composite___using_fixed_len_tuple4member_getters4composite):
    __slots__ = ()
    # @override
    ___the_number_of_member_getters4composite___ = 2
    @property
    def fst_member_getter(sf, /):
        fst, snd = sf.get_member_getters4composite_as_tuple()
        return fst
    @property
    def snd_member_getter(sf, /):
        fst, snd = sf.get_member_getters4composite_as_tuple()
        return snd
#class IMemberGetter__chain___chain_is_pair(IMemberGetter__composite___using_fixed_len_tuple4member_getters4composite):

#chain
class IMemberGetter__chain___chain_with_type_schema_pair(IMemberGetter__chain___chain_is_pair, IMemberGetter__composite___using_fixed_len_type_schema_tuple4member_getters4composite):
    __slots__ = ()
#end-class IMemberGetter__chain___chain_with_type_schema_pair(IMemberGetter__chain___chain_is_pair, IMemberGetter__composite___using_fixed_len_type_schema_tuple4member_getters4composite):
#]]]]]"""


r"""[[[[[

if 0:
  class IMemberRegister(IMemberPatcher):
    #class IMemberRegister(IMemberGetter, ___2, ___0, ___1):
    #class IMemberRegister__fvalue(IMemberGetter, ___0, ___1):
    #   since register getter@cls now named as IMemberAdaptor
    #       old-ver:IMemberRegister__fvalue vs IMemberRegister__via_ops_property_getter(IMemberGetter__via_ops_property_getter)
    #       new-ver:IMemberRegister vs IMemberAdaptor
    __slots__ = ()

    @abstractmethod
    def ___register_member__value___(sf, packet, member_value, /):
        'register_member__fvalue(); -> None|raise ???'
    def register_member__fvalue(sf, packet, fvalue, /, registered_ok):
        '___register_member__value___(); -> None|raise ???'
        sf.register_member__xvalue(packet, 0, fvalue)
    def register_member__xvalue(sf, packet, imay_xvalue_rank, xvalue, /, registered_ok):
        '___register_member__value___(); -> None|raise ???'
        check_bool(registered_ok)
        (is_member_value, default_or_member_value) = sf.get_member__xdefault__cased(packet, imay_xdefault_rank, xdefault)
        if not is_member_value:
            default = default_or_member_value
            sf.check_member_value(default)
            member_value = default
            _ = type(sf).___register_member__value___(sf, packet, member_value)
            check_is_None(_)
            tmay_member_value = sf.get_member__tmay(packet)
            if not tmay_member_value: raise logic-err
            [_member_value] = tmay_member_value
            if not _member_value is member_value: raise logic-err
            pass
        else:
            if not registered_ok: raise LookupError('registered')
if 0:
  #print(IMemberRegister.__abstractmethods__)
  assert (IMemberRegister.__abstractmethods__) == frozenset({'___register_member__value___', 'check_packet', 'check_member_value', '___get_member__tmay___'})
  #class IMemberRegister(IMemberGetter):

if 0:
  class IAutoMemberRegister(IMemberRegister, IAutoMemberGetter):#(, IRigidMemberGetter):
    #class IAutoMemberRegister(IMemberRegister__default, IAutoMemberGetter):#(, IRigidMemberGetter):
    r'''
    why not [IAutoMemberRegister <: IRigidMemberGetter]?
        IRigidMemberGetter::get_member__tmay <<== get_member__rigid
        IAutoMemberRegister::get_member__auto_install <<== [get_member__tmay, ...]
        if get_member__rigid := get_member__auto_install: recur-inf

        IAutoMemberRegister.get_member__tmay is used to detect whether registered
        IRigidMemberGetter.get_member__tmay should return (Just member_value) (never Nothing)
        hence incompatible<IAutoMemberRegister,IRigidMemberGetter>
        hence incompatible<IMemberRegister,IRigidMemberGetter>
    #'''
    __slots__ = ()


    #begin-class IMemberRegister__default(IMemberRegister):
    r'''
    ___get_member__tmay___, ___mk_member_value_on_default___, ___register_member__value___, check_packet, check_member_value
    __slots__ = ()
    #'''

    @abstractmethod
    def ___mk_member_value_on_default___(sf, packet, /):
        'mk_member_value_on_default(); -> member_value'
    def mk_member_value_on_default(sf, packet, /):
        '___mk_member_value_on_default___(); -> member_value'
        sf.check_packet(packet)
        member_value = type(sf).___mk_member_value_on_default___(sf, packet)
        sf.check_member_value(member_value)
        return member_value
    def register_member__default(sf, packet, /, registered_ok):
        sf.register_member__xvalue(packet, 1, sf.mk_member_value_on_default, registered_ok=registered_ok)
        return
        fvalue = lambda:sf.mk_member_value_on_default(packet)
        sf.register_member__fvalue(packet, fvalue, registered_ok=registered_ok)
    #end-class IMemberRegister__default(IMemberRegister):

    #class IAutoMemberRegister(IMemberRegister__default, IAutoMemberGetter):#(, IRigidMemberGetter):
    @override
    def ___auto_install_member___(sf, packet, /):
        'get_or_auto_install_member(); -> None'
        sf.register_member__default(packet, registered_ok=False)
        return
if 0:
  #print(IAutoMemberRegister.__abstractmethods__)
  assert (IAutoMemberRegister.__abstractmethods__) == frozenset({'___mk_member_value_on_default___', 'check_packet', 'check_member_value', '___get_member__tmay___', '___register_member__value___'})
  #end-class IAutoMemberRegister(IMemberRegister, IAutoMemberGetter):#(, IRigidMemberGetter):


#chain
IMemberGetter__chain
IMemberGetter__chain___chain_with_type_schema_pair
class IMemberRegister__concatTWO(IMemberGetter__chain___chain_with_type_schema_pair, IMemberRegister):
    r'''
    see:
        IAutoMemberGetter__chain for fst_member_getter
    #'''
    __slots__ = ()

    # @override
    ___base_cls_schema_tuple4member_getters4composite___ = (IAutoMemberGetter, IMemberRegister)

    @override
    def ___register_member__value___(sf, packet, member_value, /):
        'register_member__fvalue(); -> None|raise ???'
        #intermediate_obj
        transitional_obj = sf.fst_member_getter.get_or_auto_install_member(packet)
        sf.snd_member_getter.register_member__xvalue(packet, -1, member_value)
    @override
    def check_packet(sf, packet, /):
        sf.fst_member_getter.check_packet(packet)
        return
    @override
    def check_member_value(sf, member_value, /):
        sf.snd_member_getter.check_member_value(member_value)
        return
#print(IMemberRegister__concatTWO.__abstractmethods__)
assert (IMemberRegister__concatTWO.__abstractmethods__) == frozenset({'___get_member_getters4composite_as_tuple___', '___checked__check_member_getters4composite_as_tuple___'})
#class IMemberRegister__concatTWO(IMemberGetter__chain___chain_with_type_schema_pair, IMemberRegister):
#]]]]]"""


r"""[[[[[
######################################
######################################
######################################
class IMemberRegister___mixin__via_external_mapping(IMemberRegister):
    __slots__ = ('_d')
    @abstractmethod
    class ExternalMappingType:pass
    def __init__(sf, /):
        sf._d = type(sf).ExternalMappingType()
    @override
    def ___get_member__Nothing___(sf, Nothing, packet, /):
        'get_member__Nothing(); -> member_value|Nothing'
        return sf._d.get(packet, Nothing)
    @override
    def ___register_member__value___(sf, packet, member_value, /):
        'register_member__fvalue(); -> None|raise ???'
        sf._d.setdefault(packet, member_value)

class IMemberRegister___mixin__arbitrary_packet_ok(IMemberRegister):
    __slots__ = ()
    @override
    def check_packet(sf, packet, /):
        permanent_obj = packet
        #pass
        return

class IMemberRegister___mixin__arbitrary_packet_ok__via_external_mapping(IMemberRegister___mixin__via_external_mapping, IMemberRegister___mixin__arbitrary_packet_ok):
    __slots__ = ()
    ExternalMappingType = PermanentKeyRefDict

class IMemberGetter___mixin__value_is_OpaqueStorage(IMemberGetter):
    __slots__ = ()

    @override
    def check_member_value(sf, member_value, /):
        opaque_storage = member_value
        check_type_is(OpaqueStorage, opaque_storage)
        return
    assert expectError(Exception, lambda:check_member_value(None, None))
class IAutoMemberRegister___mixin__value_is_OpaqueStorage(IMemberGetter___mixin__value_is_OpaqueStorage, IAutoMemberRegister):
    __slots__ = ()

    @override
    def ___mk_member_value_on_default___(sf, packet, /):
        'mk_member_value_on_default(); -> member_value'
        return OpaqueStorage()
class MemberRegister__external_opaque_storage4permanent_obj(IMemberRegister___mixin__arbitrary_packet_ok__via_external_mapping, IAutoMemberRegister___mixin__value_is_OpaqueStorage, IAutoMemberRegister):
    __slots__ = ()
MemberRegister__external_opaque_storage4permanent_obj()

class IMemberRegister___mixin__packet_is_Weakable(IMemberRegister):
    __slots__ = ()
    @override
    def check_packet(sf, packet, /):
        weakable_obj = packet
        check_Weakable(weakable_obj)
        return
class IMemberRegister___mixin__packet_is_Weakable__via_external_mapping(IMemberRegister___mixin__via_external_mapping, IMemberRegister___mixin__packet_is_Weakable):
    __slots__ = ()
    ExternalMappingType = WeakKeyRefDict
class MemberRegister__external_opaque_storage4weakable_obj(IMemberRegister___mixin__packet_is_Weakable__via_external_mapping, IAutoMemberRegister___mixin__value_is_OpaqueStorage, IAutoMemberRegister):
    __slots__ = ()
MemberRegister__external_opaque_storage4weakable_obj()

class IMemberRegister___mixin__via_descriptor(IMemberRegister):
    __slots__ = ('_d')
    @override
    def check_packet(sf, packet, /):
        Nothing = object()
        value_or_Nothing = type(sf).___get_member__Nothing___(sf, Nothing, packet)
            #raise TypeError
            #AttributeError==>>Nothing
        return
    def __init__(sf, descriptor, /):
        #from seed.lang.apply_descriptor_protocol import is_descriptor, is_data_descriptor, is_non_data_descriptor
        #if not is_descriptor(descriptor):raise TypeError
        #if not is_data_descriptor(descriptor):raise TypeError
        cls4descriptor = type(descriptor)
        if not (hasattr(cls4descriptor, '__get__') and hasattr(cls4descriptor, '__set__')):raise TypeError
        sf._d = descriptor
    @override
    def ___get_member__Nothing___(sf, Nothing, packet, /):
        'get_member__Nothing(); -> member_value|Nothing'
        instance = packet
        descriptor = sf._d
        cls4descriptor = type(descriptor)
        try:
            member_value = cls4descriptor.__get__(descriptor, instance, None)
        except AttributeError:
            return Nothing
        if member_value is Nothing: raise logic-err
        return member_value
    @override
    def ___register_member__value___(sf, packet, member_value, /):
        'register_member__fvalue(); -> None|raise ???'
        instance = packet
        descriptor = sf._d
        cls4descriptor = type(descriptor)
        cls4descriptor.__set__(descriptor, instance, member_value)

class MemberRegister__internal_opaque_storage_via_descriptor(IMemberRegister___mixin__via_descriptor, IAutoMemberRegister___mixin__value_is_OpaqueStorage, IAutoMemberRegister):
    __slots__ = ()
MemberRegister__internal_opaque_storage_via_descriptor(_descriptor)



class IMemberRegister___mixin__via_attribute(IMemberRegister):
    __slots__ = ('_attr')
    @override
    def check_packet(sf, packet, /):
        Nothing = object()
        value_or_Nothing = type(sf).___get_member__Nothing___(sf, Nothing, packet)
            #raise TypeError
            #AttributeError==>>Nothing
        return
    def __init__(sf, attr, /):
        check_pseudo_identifier(attr)
        sf._attr = attr
    @override
    def ___get_member__Nothing___(sf, Nothing, packet, /):
        'get_member__Nothing(); -> member_value|Nothing'
        instance = packet
        attr = sf._attr
        return getattr(instance, attr, Nothing)
    @override
    def ___register_member__value___(sf, packet, member_value, /):
        'register_member__fvalue(); -> None|raise ???'
        instance = packet
        attr = sf._attr
        setattr(instance, attr, member_value)



class IMemberRegister___mixin__via_internal_mapping(IMemberRegister):
    __slots__ = ()

    @abstractmethod
    def ___get_internal_mapping4set___(sf, packet, /):
        '-> internal_mapping #for ___register_member__value___'
        instance = packet
        internal_mapping = instance.__dict__
        return internal_mapping
    @abstractmethod
    def ___iter_all_internal_mappings4get___(sf, packet, /):
    #def ___iter_alternate_internal_mappings4get___(sf, packet, /):
        '-> Iter internal_mapping #for ___get_member__Nothing___'
        instance = packet
        internal_mapping = instance.__dict__
        yield internal_mapping
        return;yield
    @abstractmethod
    def ___get_key4internal_mapping___(sf, /):
        '-> key4internal_mapping'
        #instance = packet
        key4internal_mapping = cls = type(sf)
        return key4internal_mapping
    @abstractmethod
    def check_key4internal_mapping(sf, key4internal_mapping, /):
        'internal_mapping.get(key4internal_mapping, Nothing)'
        check_Hashable__deep(key4internal_mapping)
        check_instance(AddrAsHash, key4internal_mapping)
        check_Weakable(key4internal_mapping)
    def iter_all_internal_mappings4get(sf, packet, /):
    #def iter_alternate_internal_mappings4get(sf, packet, /):
        '-> Iter internal_mapping #for ___get_member__Nothing___'
        #internal_mappings = type(sf).___iter_alternate_internal_mappings4get___(sf, packet)
        internal_mappings = type(sf).___iter_all_internal_mappings4get___(sf, packet)
        if not iter(internal_mappings) is internal_mappings: raise TypeError
        #return internal_mappings
        internal_mapping = None
        for internal_mapping in internal_mappings:
            if not hasattr(internal_mapping, 'get'): raise TypeError
            yield internal_mapping
        if internal_mapping is None: raise logic-err# iter_all_internal_mappings4get() -> null_iter
        return
    def get_internal_mapping4set(sf, packet, /):
        '-> internal_mapping #for ___register_member__value___'
        internal_mapping = type(sf).___get_internal_mapping4set___(sf, packet)
        if not hasattr(internal_mapping, 'setdefault'): raise TypeError
        return internal_mapping
    def get_key4internal_mapping(sf, /):
        '-> key4internal_mapping'
        key4internal_mapping = type(sf).___get_key4internal_mapping___(sf)
        sf.check_key4internal_mapping(key4internal_mapping)
        return key4internal_mapping


    @override
    def ___get_member__Nothing___(sf, Nothing, packet, /):
        'get_member__Nothing(); -> member_value|Nothing'
        instance = packet
        key4internal_mapping = sf.get_key4internal_mapping()
        #internal_mapping = sf.get_internal_mapping4set(instance)
        #for internal_mapping in itertools.chain([internal_mapping], sf.iter_alternate_internal_mappings4get(instance)):
        for internal_mapping in sf.iter_all_internal_mappings4get(instance):
            value_or_Nothing = internal_mapping.get(key4internal_mapping, Nothing)
            if value_or_Nothing is not Nothing:
                member_value = value_or_Nothing
                break
        else:
            return Nothing
        return member_value

    @override
    def ___register_member__value___(sf, packet, member_value, /):
        'register_member__fvalue(); -> None|raise ???'
        instance = packet
        internal_mapping = sf.get_internal_mapping4set(instance)
        key4internal_mapping = sf.get_key4internal_mapping()
        internal_mapping.setdefault(key4internal_mapping, member_value)


class IMemberRegister___mixin__via_std_dict(IMemberRegister___mixin__via_internal_mapping):
    __slots__ = ()

    @override
    def check_key4internal_mapping(sf, key4internal_mapping, /):
        'internal_mapping.get(key4internal_mapping, Nothing)'
        check_Hashable__deep(key4internal_mapping)

    @override
    def ___get_internal_mapping4set___(sf, packet, /):
        '-> internal_mapping #for ___register_member__value___'
        instance = packet
        internal_mapping = instance.__dict__
        return internal_mapping
class IMemberRegister___mixin__via_std_dict__shallow(IMemberRegister___mixin__via_std_dict):
    r'''
    ___get_key4internal_mapping___, check_member_value
    #'''
    __slots__ = ()

    @override
    def check_packet(sf, packet, /):
        instance = packet
        instance.__dict__
        return

    @override
    def ___iter_all_internal_mappings4get___(sf, packet, /):
        '-> Iter internal_mapping #for ___get_member__Nothing___'
        instance = packet
        yield instance.__dict__
        return;yield

class IMemberRegister___mixin__via_std_dict__mro(IMemberRegister___mixin__via_std_dict):
    r'''
    ___get_key4internal_mapping___, check_member_value
    #'''
    __slots__ = ()

    @override
    def check_packet(sf, packet, /):
        cls_as_instance = instance = packet
        check_instance(type, cls_as_instance)
        cls_as_instance.__dict__
        cls_as_instance.__mro__
        return

    @override
    def ___iter_all_internal_mappings4get___(sf, packet, /):
        '-> Iter internal_mapping #for ___get_member__Nothing___'
        cls_as_instance = packet
        for super_cls in cls_as_instance.__mro__:
            #if super_cls is not cls_as_instance:
                yield super_cls.__dict__
        return;yield



#via_cls_property_getter

class IMemberGetter___mixin__value_is_callable(IMemberGetter):
    'eg. member_value=property_getter   #see:IMemberGetter__via_ops_property_getter'
    __slots__ = ()

    @override
    def check_member_value(sf, member_value, /):
        f = member_value
        check_callable(f)
        return
    assert expectError(Exception, lambda:check_member_value(None, None))



class IMemberGetter__via_ops_property_getter(IMemberGetter):
    'ops<packet>.property_getter(packet)->member_value'
    __slots__ = ()
    @abstractmethod
    def ___check_ops4packet___(sf, ops4packet, /):
        check_instance(type, ops4packet)
    @abstractmethod
    def ___get_ops4packet___(sf, packet, /):
        'get_ops4packet(); -> ops<packet>'
        ops4packet = type(packet)
        return ops4packet

    def check_ops4packet(sf, ops4packet, /):
        _ = type(sf).___check_ops4packet___(sf, ops4packet)
        member_getter4ops = sf.get_member_getter4ops_property_getter()
        member_getter4ops.check_packet(ops4packet)
    def get_ops4packet(sf, packet, /):
        '___get_ops4packet___(); -> ops<packet>'
        ops4packet = type(sf).___get_ops4packet___(sf)
        sf.check_ops4packet(ops4packet)
        return ops4packet
    @abstractmethod
    def ___get_member_getter4ops_property_getter___(sf, /):
        'get_member_getter4ops_property_getter(); -> IMemberGetter<packet=ops<instance>, member_value=property_getter>'
    def get_member_getter4ops_property_getter(sf, /):
        '___get_member_getter4ops_property_getter___(); -> IMemberGetter<packet=ops<instance>, member_value=property_getter>'
        member_getter4ops = type(sf).___get_member_getter4ops_property_getter___(sf)
        sf.check_member_getter4ops(member_getter4ops)
        return member_getter4ops
    def check_member_getter4ops(sf, member_getter4ops, /):
        check_instance(IMemberGetter___mixin__value_is_callable, member_getter4ops)
    @override
    def ___get_member__Nothing___(sf, Nothing, packet, /):
        'get_member__Nothing(); -> member_value|Nothing'
        instance = packet
        ops4instance = sf.get_ops4packet(instance)
        member_getter4ops = sf.get_member_getter4ops_property_getter()
        may_property_getter = member_getter4ops.get_member__may(ops4instance)
        if may_property_getter is None:
            return Nothing
        property_getter = may_property_getter
        check_callable(property_getter)
        member_value = member = property_getter(instance)
        return member_value
class IMemberRegister__via_ops_property_getter(IMemberGetter__via_ops_property_getter):
    __slots__ = ()
    @abstractmethod
    def ___get_member_register4ops_property_getter___(sf, /):
        'get_member_register4ops_property_getter(); -> IMemberRegister<packet=ops<instance>, member_value=property_getter>'
    def get_member_register4ops_property_getter(sf, /):
        '___get_member_register4ops_property_getter___(); -> IMemberRegister<packet=ops<instance>, member_value=property_getter>'
        member_register4ops = type(sf).___get_member_register4ops_property_getter___(sf)
        sf.check_member_register4ops_property_getter(member_register4ops)
        return member_register4ops
    def check_member_register4ops_property_getter(sf, member_register4ops, /):
        check_instance(IMemberGetter___mixin__value_is_callable, member_register4ops)
        check_instance(IMemberRegister, member_register4ops)

    @override
    def ___get_member_getter4ops_property_getter___(sf, /):
        member_register4ops = sf.get_member_register4ops_property_getter()
        member_getter4ops = member_register4ops
        return member_getter4ops

    def register__property_getter(sf, ops4packet, property_getter, /, registered_ok):
        'ops<packet> -> (packet -> member_value) -> None|raise ???'
        check_callable(property_getter)
        sf.check_ops4packet(ops4packet)
        ops4instance = ops4packet
        member_register4ops = sf.get_member_register4ops_property_getter()

        value4ops = property_getter
        fvalue4ops = lambda:value4ops
        member_register4ops.register_member__fvalue(ops4packet, fvalue4ops, registered_ok=registered_ok)

class IMemberGetter__via_cls_property_getter(IMemberGetter__via_ops_property_getter):
    'ops<packet> := cls<packet>'
    __slots__ = ()
    @override
    def ___check_ops4packet___(sf, ops4packet, /):
        check_instance(type, ops4packet)
    @override
    def ___get_ops4packet___(sf, packet, /):
        'get_ops4packet(); -> ops<packet>'
        ops4packet = type(packet)
        return ops4packet

class IPseudoMutableMapping:
    get
    setdefault
    __contains__
    __setitem__?
    __bool__?
    __len__?
    __iter__?
    __getitem__?
e ../../python3_src/seed/abc/storage/MemberGetter.py
py -m nn_ns.app.mk_py_template -o   ../../python3_src/seed/abc/storage/MemberGetter.py
e ../../python3_src/seed/types/mapping/PseudoMapping.py
e ../../python3_src/seed/types/mapping/OpaquePseudoMapping.py
e ../../python3_src/seed/lang/hasattr__as_cls.py
py -m nn_ns.app.mk_py_template -o  ../../python3_src/seed/lang/hasattr__as_cls.py
from seed.types.mapping.PseudoMapping import IPseudoMapping___get, IPseudoMapping___get__setdefault

from seed.tiny_.mk_fdefault import mk_tmay_from_try_fvalue_KeyError, mk_tmay_from_default2value, mk_tmay_from_is_safe_fvalue, mk_default
        default = mk_default(imay_xdefault_rank, xdefault, mapping, key)
class IMemberGetter___mixin__value_is_IPseudoMutableMapping
class IAutoMemberRegister___mixin__value_is_IPseudoMutableMapping(IMemberGetter___mixin__value_is_IPseudoMutableMapping, IAutoMemberRegister):
    IAutoMemberRegister___mixin__value_is_IPseudoMutableMapping+packet~IMemberRegister__
class IAutoMemberRegister___mixin__via_attribute__value_is_IPseudoMutableMapping(IMemberRegister___mixin__via_attribute, IAutoMemberRegister___mixin__value_is_IPseudoMutableMapping):
class MemberRegister___mixin__via_attribute__value_is_callable(IMemberRegister___mixin__via_attribute, IAutoMemberRegister, IMemberGetter___mixin__value_is_callable):
    __slots__ = ()
MemberRegister___mixin__via_attribute__value_is_callable('___dict_on_as_isolated_ops___')
MemberRegister___mixin__via_attribute__value_is_callable('___dict_on_as_cls_in_mro___')

class MemberGetter__via_cls_property_getter__via_dict_on_as_isolated_ops(IMemberRegister__via_ops_property_getter, IMemberGetter__via_cls_property_getter):
    MemberRegister_
    _attr
######################################
######################################
######################################
#]]]]]"""

#]]]zzzwww:end
#]]]main_body_src_code:end


#HHHHH
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #<BLANKLINE>
    #Traceback (most recent call last):


