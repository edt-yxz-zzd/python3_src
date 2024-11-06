#__all__:goto
#begin__doctest,end__doctest,doctest_cmd:goto
#simplified_typing:goto
#simplified_constraints:goto
#extra_constraints:goto
#
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/solo_rgnr_transform_cases.py
view ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/solo_rgnr_transform_cases-old.py

seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases:__doc__ -ht
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases:__doc__ -ht   >  /sdcard/0my_files/tmp/0tmp
view /sdcard/0my_files/tmp/0tmp


[[
######################
case4protection:
    + snapshot:into,hide,none
        pass into:
            * (... >> snapshot)
            * snapshot; (... + dummy_unlocker)
            * (... + dummy_unlocker)
    + unlocker:into,hide,free
        pass into:
            * (unlocker >> ...)
            * (dummy_unlocker >> ...)
            * unlocker.unlocker_release(); (dummy_unlocker >> ...)
    3*3==9
    ((snapshot_into|snapshot_hide|snapshot_none)*(unlocker_into|unlocker_hide))

######################


##may assume[no:protected_ok], but it is possible impl
    # !! [ok:have called unlocker.unlocker_release()]
    # [no:protected_ok]
ok:
    protected_ok:
        protected_forgivable_ok
        protected_severe_ok
    unprotected_ok:
        unprotected_forgivable_ok
        unprotected_severe_ok
fail:
    protected_fail:
        protected_forgivable_fail
        protected_severe_fail
    unprotected_fail:
        unprotected_forgivable_fail
        unprotected_severe_fail
<==> ((protected|unprotected)*(forgivable|severe)*(ok|fail))
    [protected=[def]=[child:unlocker_release() called]]
    [forgivable=[def]=[child:monotonic_idx8begin unchanged]]
    [ok=[def]=[child:reply.ok]]
######################
######################

接口只有{case4reply5child:case4reply5self},(case4seekback)是冗余信息, (case4protection)只是实现细节(也是更高层数据的冗余信息)
    #虽然case4protection两子部件 正交/无关:unlocker_xxx 声明头部; snapshot_xxx 用于调头(seekback)，但也是冗余信息
    (case4seekback)是sconfig的导出信息,是sexconfig的冗余信息
    (case4protection)是sconfigpack的导出信息,是sexconfigpack的冗余信息

{(case4reply5child,case4reply5self):{case4protection}}
    #
    #1:
    #xxx:{uint%64:{uint%9}}
    #xxx:{uint%64:uint%(2**9)}
    #
    #2:
    #xxx:{uint%64:({uint%3},{uint%3})}
    #xxx:{uint%64:(uint%(2**3),uint%(2**3))}
    #xxx:{uint%64:uint%(2**(3+3))}
    #   <<==case4protection两子部件 正交
    #
    #3:
    #{uint%64:(uint%3,uint%3)}
    #   !! case4protection两子部件 正交
    #   !! case4protection各子部件 在约束条件下 合法值集 紧致
    #{uint%64:uint%9}
    #   item~uint%576
    #

######################
#simplify:here

[child.unprotected-->self.protected]:
    <==> [child.unlocker.known_released-->not self.unlocker.known_released]
    ==>>:
    [unlocker_hide]
[pack.always:self.unprotected]:
    <==> [unlocker_free]

[child.forgivable-->self.forgivable]:
    ==>>:
    [no_seekback]
[child.severe-->self.severe]:
    ==>>:
    [no_seekback]
[child.forgivable-->self.severe]:
    ==>>:
    _L
        # !! eof
[child.severe-->self.forgivable]:
    <==> [to_seekback]
    ==>>:
    [not snapshot_none]
[pack.always:[child.severe-->self.severe]]:
    <==> [pack.always:no_seekback]:
    <==> [snapshot_none]
[child.unprotected_severe-->self.forgivable]:
    ==>>:
    [snapshot_hide]

[pack.always:not [child.unprotected_severe-->self.forgivable]]:
    <==> [pack.always:[child.unprotected_severe-->self.severe]]
    ==>>:
    [not snapshot_hide]
[pack.always:[child.severe-->self.severe]]:
    <==> [snapshot_none]

######################
==>>:
#simplified_constraints:here

[unlocker_free] <==> [pack.always:self.unprotected]
[unlocker_hide] <==> [pack.any:[child.unprotected-->self.protected]]
[unlocker_into] <==> [[pack.any:self.protected][pack.always:[child.unprotected-->self.unprotected]]]

[snapshot_none] <==> [pack.always:[child.severe-->self.severe]]
[snapshot_hide] <==> [pack.any:[child.unprotected_severe-->self.forgivable]]
[snapshot_into] <==> [[pack.any:[child.severe-->self.forgivable]][pack.always:[child.unprotected_severe-->self.severe]]]

[to_seekback] <==> [child.severe-->self.forgivable]
[no_seekback] <==> [[child.severe-->self.severe][child.forgivable-->self.forgivable]]

==>>determine_low_case4protection6sconfig_()
==>>determine_case4seekback5sconfig_()

extra_constraints:here
forbid:[child.forgivable-->self.severe]
    !! eof
    4:num_output_cases-4
    clousure_under_composition:[self.severe-->child.severe]
forbid:[child.severe_fail-->self.severe_ok]
    !! *_severe_fail .monotonic_idx8end unpredictable
    2:num_output_cases-2
    clousure_under_composition:[self.severe_ok-->child.severe_ok]
#####
optional:[forbid_xxx_protected_ok:=True]:
forbid:[[child.protected_ok]or[self.protected_ok]]
    clousure_under_composition:[[child.protected_ok]or[self.protected_ok]]

######################
#simplified_typing:here

sconfig := (case4reply5child, case4reply5self)
low_case4protection := Case4protection((low_unlocker_xxx, low_snapshot_xxx))
cache4sconfig := (low_case4protection, case4seekback)
    # NOTE:but:[low_xxx_xxx.value is max_xxx_xxx], since def@class in reversed order
sexconfig := (cache4sconfig, sconfig)
sconfigpack := full-{case4reply5child:case4reply5self}
sexconfigpack := (case4protection8summary, sconfigpack)
    where:case4protection8summary.value == (upper all low_unlocker_xxx, upper all low_snapshot_xxx)
    # NOTE:but:[low_xxx_xxx.value is max_xxx_xxx], since def@class in reversed order
maynotlow_cache4sconfig := (case4protection8summary, seekback)
maynotlow_sexconfig := (maynotlow_cache4sconfig, sconfig)

########counting<sconfig>:
echo $[8+8+8+8 + 8+8+8+8]
64
echo $[4+4+4+4 + 6+6+8+8]
44
    4:num_output_cases-4
    2:num_output_cases-2
    == total<sconfig>
    == total<sexconfig>

[forbid_xxx_protected_ok:=True]:
echo $[0+3+3+3 + 5+5+0+6]
25
    == total<sconfig,+forbid_xxx_protected_ok>
    == total<sexconfig,+forbid_xxx_protected_ok>

########counting<sconfigpack>:
echo $[1<<24]
16777216
1677_7216

echo $[8*8*8*8 * 8*8*8*8]
16777216
echo $[4*4*4*4 * 6*6*8*8]
589824
    4:num_output_cases-4
    2:num_output_cases-2
    == total<sconfigpack>
    == total<sexconfigpack>

[forbid_xxx_protected_ok:=True]:
echo $[1*3*3*3 * 5*5*1*6]
4050
    #『1』stands for 『deleted』
    == total<sconfigpack,+forbid_xxx_protected_ok>
    == total<sexconfigpack,+forbid_xxx_protected_ok>
######################

[[forbid_xxx_protected_ok:=False] -> [total4sconfig == (4+4+4+4 + 6+6+8+8) == 44]]
[[forbid_xxx_protected_ok:=True]  -> [total4sconfig == (0+3+3+3 + 5+5+0+6) == 25]]

[[forbid_xxx_protected_ok:=False] -> [total4sconfigpack == (4*4*4*4 * 6*6*8*8) == 589824]]
[[forbid_xxx_protected_ok:=True]  -> [total4sconfigpack == (1*3*3*3 * 5*5*1*6) == 4050]]

######################
]]
[[
get_info_ex4high_freq_sconfigpack_
get_symbol8high_freq_sconfigpack_
    _high_freq_sconfigpacks
        _mkr4high_freq_sconfigpacks
<<==:
DONE:list high freq sexconfigpack and register them...
  * unlocker_hide+snapshot_hide:
      * lookahead: ignore=inherit
      * followed_by: ignore=True
      * not_followed_by: ignore=True#the only one 'flip/invert_ok_err' instance
      * [nonprimitive]:protect_whole === (protect_header <<< whole8header) =!= trial_and_error
        #unprotected_fail-->protected_forgivable_fail
  * unlocker_into+snapshot_into:
      * protect_header === trial_and_error
        #protected_fail-->protected_forgivable_fail
      * [nonprimitive]:optional__forgivable === (spostprocess <<< lift__forgivable <<< protect_header)
        #(protected_fail&unprotected_forgivable_fail)-->forgivable_ok
        # lift (tmay oresult) as new-oresult
      * [nonprimitive]:optional__strict === (spostprocess <<< lift__strict <<< protect_header)
        #protected_fail-->forgivable_ok
        #   unprotected_forgivable_fail leaves
        # lift (tmay oresult) as new-oresult
  * unlocker_into+snapshot_none:
      * lift__forgivable#no_seekback
        #forgivable_fail-->forgivable_ok
        #lift (eresult, ...) as new-oresult
      * lift__strict#no_seekback
        #protected_forgivable_fail-->forgivable_ok
        #lift (eresult, ...) as new-oresult
  * unlocker_hide+snapshot_none:
      * whole8header:
        #unprotected_forgivable_fail-->protected_forgivable_fail
        #unprotected_severe_fail-->protected_severe_fail
        combine:[protect_whole === (protect_header <<< whole8header)]
        combine:(optional <<< whole8header)
  * unlocker_free+snapshot_none:
      * empty8header # to force severe_fail
        #forgivable_fail-->unprotected_forgivable_fail
        #severe_fail-->unprotected_severe_fail
]]


begin__doctest
[[[[[[[

>>> len(setting1.sorted_good_sexconfigs) # [no:protected_ok]
25
>>> len(setting0.sorted_good_sexconfigs)
44
>>> for cache4sconfig, sconfig in setting0.sorted_good_sexconfigs:
...     print(sconfig)
...     print('   ', cache4sconfig)
(unprotected_severe_ok, protected_forgivable_ok)
    (unlocker_hide__snapshot_hide, to_seekback)
(unprotected_severe_ok, protected_forgivable_fail)
    (unlocker_hide__snapshot_hide, to_seekback)
(unprotected_severe_fail, protected_forgivable_ok)
    (unlocker_hide__snapshot_hide, to_seekback)
(unprotected_severe_fail, protected_forgivable_fail)
    (unlocker_hide__snapshot_hide, to_seekback)
(unprotected_forgivable_ok, protected_forgivable_ok)
    (unlocker_hide__snapshot_none, no_seekback)
(unprotected_forgivable_ok, protected_forgivable_fail)
    (unlocker_hide__snapshot_none, no_seekback)
(unprotected_forgivable_fail, protected_forgivable_ok)
    (unlocker_hide__snapshot_none, no_seekback)
(unprotected_forgivable_fail, protected_forgivable_fail)
    (unlocker_hide__snapshot_none, no_seekback)
(unprotected_severe_ok, protected_severe_ok)
    (unlocker_hide__snapshot_none, no_seekback)
(unprotected_severe_ok, protected_severe_fail)
    (unlocker_hide__snapshot_none, no_seekback)
(unprotected_severe_fail, protected_severe_fail)
    (unlocker_hide__snapshot_none, no_seekback)
(protected_severe_ok, protected_forgivable_ok)
    (unlocker_into__snapshot_into, to_seekback)
(protected_severe_ok, protected_forgivable_fail)
    (unlocker_into__snapshot_into, to_seekback)
(protected_severe_fail, protected_forgivable_ok)
    (unlocker_into__snapshot_into, to_seekback)
(protected_severe_fail, protected_forgivable_fail)
    (unlocker_into__snapshot_into, to_seekback)
(protected_forgivable_ok, protected_forgivable_ok)
    (unlocker_into__snapshot_none, no_seekback)
(protected_forgivable_ok, protected_forgivable_fail)
    (unlocker_into__snapshot_none, no_seekback)
(protected_forgivable_fail, protected_forgivable_ok)
    (unlocker_into__snapshot_none, no_seekback)
(protected_forgivable_fail, protected_forgivable_fail)
    (unlocker_into__snapshot_none, no_seekback)
(protected_severe_ok, protected_severe_ok)
    (unlocker_into__snapshot_none, no_seekback)
(protected_severe_ok, protected_severe_fail)
    (unlocker_into__snapshot_none, no_seekback)
(protected_severe_fail, protected_severe_fail)
    (unlocker_into__snapshot_none, no_seekback)
(unprotected_severe_ok, unprotected_forgivable_ok)
    (unlocker_free__snapshot_hide, to_seekback)
(unprotected_severe_ok, unprotected_forgivable_fail)
    (unlocker_free__snapshot_hide, to_seekback)
(unprotected_severe_fail, unprotected_forgivable_ok)
    (unlocker_free__snapshot_hide, to_seekback)
(unprotected_severe_fail, unprotected_forgivable_fail)
    (unlocker_free__snapshot_hide, to_seekback)
(protected_severe_ok, unprotected_forgivable_ok)
    (unlocker_free__snapshot_into, to_seekback)
(protected_severe_ok, unprotected_forgivable_fail)
    (unlocker_free__snapshot_into, to_seekback)
(protected_severe_fail, unprotected_forgivable_ok)
    (unlocker_free__snapshot_into, to_seekback)
(protected_severe_fail, unprotected_forgivable_fail)
    (unlocker_free__snapshot_into, to_seekback)
(protected_forgivable_ok, unprotected_forgivable_ok)
    (unlocker_free__snapshot_none, no_seekback)
(protected_forgivable_ok, unprotected_forgivable_fail)
    (unlocker_free__snapshot_none, no_seekback)
(protected_forgivable_fail, unprotected_forgivable_ok)
    (unlocker_free__snapshot_none, no_seekback)
(protected_forgivable_fail, unprotected_forgivable_fail)
    (unlocker_free__snapshot_none, no_seekback)
(protected_severe_ok, unprotected_severe_ok)
    (unlocker_free__snapshot_none, no_seekback)
(protected_severe_ok, unprotected_severe_fail)
    (unlocker_free__snapshot_none, no_seekback)
(protected_severe_fail, unprotected_severe_fail)
    (unlocker_free__snapshot_none, no_seekback)
(unprotected_forgivable_ok, unprotected_forgivable_ok)
    (unlocker_free__snapshot_none, no_seekback)
(unprotected_forgivable_ok, unprotected_forgivable_fail)
    (unlocker_free__snapshot_none, no_seekback)
(unprotected_forgivable_fail, unprotected_forgivable_ok)
    (unlocker_free__snapshot_none, no_seekback)
(unprotected_forgivable_fail, unprotected_forgivable_fail)
    (unlocker_free__snapshot_none, no_seekback)
(unprotected_severe_ok, unprotected_severe_ok)
    (unlocker_free__snapshot_none, no_seekback)
(unprotected_severe_ok, unprotected_severe_fail)
    (unlocker_free__snapshot_none, no_seekback)
(unprotected_severe_fail, unprotected_severe_fail)
    (unlocker_free__snapshot_none, no_seekback)



validate:
    xxx&lift__xxx --> unlocker_into__snapshot_none
    True&not_followed_by --> unlocker_free__snapshot_hide
    True&optional__xxx --> unlocker_free__snapshot_into
    <<==:
>>> for forbid_xxx_protected_ok, nm in product([False, True], name_set4high_freq_sconfigpack):
...     sym = get_symbol8high_freq_sconfigpack_(forbid_xxx_protected_ok, nm)
...     sexconfigpack = get_weak_symbolize_register4sexconfigpack_(forbid_xxx_protected_ok).lookup(sym)
...     (case4protection8summary, sconfigpack) = sexconfigpack
...     print((forbid_xxx_protected_ok, nm, case4protection8summary))
(False, '_echo_', unlocker_into__snapshot_none)
(False, 'empty8header', unlocker_free__snapshot_none)
(False, 'followed_by', unlocker_into__snapshot_hide)
(False, 'lift__forgivable', unlocker_into__snapshot_none)
(False, 'lift__strict', unlocker_into__snapshot_none)
(False, 'lookahead', unlocker_into__snapshot_hide)
(False, 'not_followed_by', unlocker_into__snapshot_hide)
(False, 'optional__forgivable', unlocker_into__snapshot_into)
(False, 'optional__strict', unlocker_into__snapshot_into)
(False, 'protect_header', unlocker_into__snapshot_into)
(False, 'protect_whole', unlocker_hide__snapshot_hide)
(False, 'trial_and_error', unlocker_into__snapshot_into)
(False, 'whole8header', unlocker_hide__snapshot_none)
(True, '_echo_', unlocker_into__snapshot_none)
(True, 'empty8header', unlocker_free__snapshot_none)
(True, 'followed_by', unlocker_into__snapshot_hide)
(True, 'lift__forgivable', unlocker_into__snapshot_none)
(True, 'lift__strict', unlocker_into__snapshot_none)
(True, 'lookahead', unlocker_into__snapshot_hide)
(True, 'not_followed_by', unlocker_free__snapshot_hide)
(True, 'optional__forgivable', unlocker_free__snapshot_into)
(True, 'optional__strict', unlocker_free__snapshot_into)
(True, 'protect_header', unlocker_into__snapshot_into)
(True, 'protect_whole', unlocker_hide__snapshot_hide)
(True, 'trial_and_error', unlocker_into__snapshot_into)
(True, 'whole8header', unlocker_hide__snapshot_none)



]]]]]]]
end__doctest


py_adhoc_call     seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases @validate____roughly_composite__case4protection_ -forbid_xxx_protected_ok
py_adhoc_call     seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases @validate____roughly_composite__case4protection_ +forbid_xxx_protected_ok


#]]]'''
__all__ = r'''
mk_gi4IRecognizerLLoo__5solo_rgnr_transform_cases_
    CASES
    name_set4high_freq_sconfigpack
    get_info_ex4high_freq_sconfigpack_
        default_info4mk_gi
        get_symbol8high_freq_sconfigpack_
    get_setting_
    get_weak_symbolize_register4sexconfigpack_
        is_good_sexconfigpack_








Case4reply6xprotected
    protected
    unprotected
Case4reply6xforgivable
    forgivable
    severe
Case4reply6xok
    ok
    fail
Case4reply
    protected_forgivable_ok
    protected_forgivable_fail
    protected_severe_ok
    protected_severe_fail
    unprotected_forgivable_ok
    unprotected_forgivable_fail
    unprotected_severe_ok
    unprotected_severe_fail
Case4protection6snapshot
    snapshot_hide
    snapshot_into
    snapshot_none
Case4protection6unlocker
    unlocker_hide
    unlocker_into
    unlocker_free
Case4protection
    unlocker_hide__snapshot_hide
    unlocker_hide__snapshot_into
    unlocker_hide__snapshot_none
    unlocker_into__snapshot_hide
    unlocker_into__snapshot_into
    unlocker_into__snapshot_none
    unlocker_free__snapshot_hide
    unlocker_free__snapshot_into
    unlocker_free__snapshot_none
    pcmp4Case4protection_
Case4seekback
    to_seekback
    no_seekback


mk_gi4IRecognizerLLoo__5solo_rgnr_transform_cases_
    mk_case4reply5xxx
        mk_case4reply5child
        mk_case4reply5self
    get_weak_symbolize_register4sexconfigpack_
        weak_symbolize_register4sexconfigpack__allow_xxxx_protected_ok
        weak_symbolize_register4sexconfigpack__forbid_xxx_protected_ok





composite__sexconfigpack_
    mk_sexconfigpack_
    composite__sconfigpack_
        composite__sconfig_
    determine_summary_case4protection5sconfigpack_
        determine_low_case4protection6sconfig_
        upper4Case4protection_
            upper4Case4protection6unlocker_
            upper4Case4protection6snapshot_
composite__sexconfig_
    mk_sexconfig_
    composite__sconfig_
    determine_cache4sconfig6sconfig_
        determine_low_case4protection6sconfig_
        determine_case4seekback5sconfig_


Bad
    Bad__sconfigpack__nonfull
    Bad__unmatch_case4reply5child
    Bad__unmatch_case4reply5child_set
    Bad__sconfig
folds_
Setting
    get_setting_
        setting0
        setting1
    validate____roughly_composite__case4protection_

is_good_sexconfigpack_

'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.types.stream.IRecoverableInputStream import dummy_unlocker, DetectionUnlocker#detection_unlocker

from collections import OrderedDict
from enum import Enum, auto
from itertools import product# combinations
from functools import partial
from math import prod


from seed.types.FrozenOrderedSet import FrozenOrderedSet, FrozenOrderedDict
from seed.types.mapping.symbolize import WeakSymbolizeRegister, ISymbolizeRegister__subset# PersistentSymbolizeRegister
    # to symbolize sexconfigpack

from seed.tiny_.check import check_type_is, check_int_ge
from seed.tiny_.group__partition import partition_xs_by_bool_, xs_to_vss_, xs_to_k2vs_
from seed.tiny import fst, snd, print_err
___end_mark_of_excluded_global_names__0___ = ...

class _Lt:
    if 0:
        def __str__(sf, /):
            return sf.name
    def __repr__(sf, /):
        return sf.name
    def __lt__(sf, ot, /):
        if not type(sf) is type(ot):
            return NotImplemented
        return sf.value < ot.value
class Case4reply6xprotected(_Lt, Enum):
    protected   = auto()
    unprotected = auto()
    def __invert__(sf, /):
        match sf:
            case __class__.protected:
                return unprotected
            case __class__.unprotected:
                return protected
            case _:
                raise 000
class Case4reply6xforgivable(_Lt, Enum):
    forgivable  = auto()
    severe      = auto()
    def __invert__(sf, /):
        match sf:
            case __class__.forgivable:
                return severe
            case __class__.severe:
                return forgivable
            case _:
                raise 000
class Case4reply6xok(_Lt, Enum):
    ok          = auto()
    fail        = auto()
    def __invert__(sf, /):
        match sf:
            case __class__.ok:
                return fail
            case __class__.fail:
                return ok
            case _:
                raise 000
sorted(Case4reply6xprotected)
sorted(Case4reply6xok)

protected   = Case4reply6xprotected.protected
unprotected = Case4reply6xprotected.unprotected
forgivable  = Case4reply6xforgivable.forgivable
severe      = Case4reply6xforgivable.severe
ok          = Case4reply6xok.ok
fail        = Case4reply6xok.fail
class Case4reply(_Lt, Enum):
    # 2*2*2==8
    protected_forgivable_ok     = (protected, forgivable, ok)
    protected_forgivable_fail   = (protected, forgivable, fail)
    protected_severe_ok         = (protected, severe, ok)
    protected_severe_fail       = (protected, severe, fail)
    unprotected_forgivable_ok   = (unprotected, forgivable, ok)
    unprotected_forgivable_fail = (unprotected, forgivable, fail)
    unprotected_severe_ok       = (unprotected, severe, ok)
    unprotected_severe_fail     = (unprotected, severe, fail)
    ######################
    def get_xprotected(sf, /):
        return sf.value[0]
    def get_xforgivable(sf, /):
        return sf.value[1]
    def get_xok(sf, /):
        return sf.value[2]
    ######################
    def flip_xprotected(sf, /):
        (a, b, c) = sf.value
        return Case4reply((~a, b, c))
    def flip_xforgivable(sf, /):
        (a, b, c) = sf.value
        return Case4reply((a, ~b, c))
    def flip_xok(sf, /):
        (a, b, c) = sf.value
        return Case4reply((a, b, ~c))
    ######################
    def is_protected(sf, /):
        return sf.value[0] == protected
    def is_forgivable(sf, /):
        return sf.value[1] == forgivable
    def is_ok(sf, /):
        return sf.value[2] == ok
    ######################
    def is_protected_ok(sf, /):
        return sf.is_protected() and sf.is_ok()
    ######################
    def is_unprotected(sf, /):
        return sf.value[0] == unprotected
    def is_severe(sf, /):
        return sf.value[1] == severe
    def is_fail(sf, /):
        return sf.value[2] == fail
    ######################
    def is_severe_ok(sf, /):
        return sf.is_severe() and sf.is_ok()
    def is_severe_fail(sf, /):
        return sf.is_severe() and sf.is_fail()
    def is_unprotected_severe(sf, /):
        return sf.is_unprotected() and sf.is_severe()
    def is_protected_severe(sf, /):
        return sf.is_protected() and sf.is_severe()
    ######################
    def is_forgivable_fail(sf, /):
        return sf.is_forgivable() and sf.is_fail()
    ######################

protected_forgivable_ok     = Case4reply.protected_forgivable_ok
protected_forgivable_fail   = Case4reply.protected_forgivable_fail
protected_severe_ok         = Case4reply.protected_severe_ok
protected_severe_fail       = Case4reply.protected_severe_fail
unprotected_forgivable_ok   = Case4reply.unprotected_forgivable_ok
unprotected_forgivable_fail = Case4reply.unprotected_forgivable_fail
unprotected_severe_ok       = Case4reply.unprotected_severe_ok
unprotected_severe_fail     = Case4reply.unprotected_severe_fail

assert protected_forgivable_ok.is_protected()
assert protected_forgivable_ok.is_forgivable()
assert protected_forgivable_ok.is_ok()
assert not unprotected_severe_fail.is_protected()
assert not unprotected_severe_fail.is_forgivable()
assert not unprotected_severe_fail.is_ok()

_Case4reply__if____forbid____protected_ok = {c for c in Case4reply if not c.is_protected_ok()}
_Case4reply__if____allow_____protected_ok = {*Case4reply}
assert len(_Case4reply__if____forbid____protected_ok) == len(Case4reply)-2
assert len(_Case4reply__if____allow_____protected_ok) == len(Case4reply)





class _LowerThan4reversed_order:
    def lower_than4pcmp_(sf, ot, /):
        #vs:__lt__
        #asif:__gt__ <<== define enum in reversed order
        if not type(sf) is type(ot):
            raise TypeError(type(ot))
            return NotImplemented
        return sf.value > ot.value
class Case4protection6snapshot(_LowerThan4reversed_order, _Lt, Enum):
    snapshot_hide = auto()
    snapshot_into = auto()
    snapshot_none = auto()
class Case4protection6unlocker(_LowerThan4reversed_order, _Lt, Enum):
    unlocker_hide = auto()
    unlocker_into = auto()
    unlocker_free = auto()
snapshot_hide = Case4protection6snapshot.snapshot_hide
snapshot_into = Case4protection6snapshot.snapshot_into
snapshot_none = Case4protection6snapshot.snapshot_none
unlocker_hide = Case4protection6unlocker.unlocker_hide
unlocker_into = Case4protection6unlocker.unlocker_into
unlocker_free = Case4protection6unlocker.unlocker_free

class Case4protection(_Lt, Enum):
    #snapshot:hide,into,none
    #unlocker:hide,into,free
    #3*3==9
    unlocker_hide__snapshot_hide = (unlocker_hide, snapshot_hide)
    unlocker_hide__snapshot_into = (unlocker_hide, snapshot_into)
    unlocker_hide__snapshot_none = (unlocker_hide, snapshot_none)
    unlocker_into__snapshot_hide = (unlocker_into, snapshot_hide)
    unlocker_into__snapshot_into = (unlocker_into, snapshot_into)
    unlocker_into__snapshot_none = (unlocker_into, snapshot_none)
    unlocker_free__snapshot_hide = (unlocker_free, snapshot_hide)
    unlocker_free__snapshot_into = (unlocker_free, snapshot_into)
    unlocker_free__snapshot_none = (unlocker_free, snapshot_none)
    ######################
    def pcmp(sf, ot, /):
        'Case4protection -> Case4protection -> may (-1|0|1)'
        return pcmp4Case4protection_(sf, ot)
    ######################
    def get_unlocker_xxx(sf, /):
        return sf.value[0]
    def get_snapshot_xxx(sf, /):
        return sf.value[1]

    ######################
    def is_unlocker_hide(sf, /):
        return sf.value[0] == unlocker_hide
    def is_unlocker_into(sf, /):
        return sf.value[0] == unlocker_into
    def is_unlocker_free(sf, /):
        return sf.value[0] == unlocker_free
    ######################
    def is_snapshot_hide(sf, /):
        return sf.value[1] == snapshot_hide
    def is_snapshot_into(sf, /):
        return sf.value[1] == snapshot_into
    def is_snapshot_none(sf, /):
        return sf.value[1] == snapshot_none
    ######################
unlocker_hide__snapshot_hide = Case4protection.unlocker_hide__snapshot_hide
unlocker_hide__snapshot_into = Case4protection.unlocker_hide__snapshot_into
unlocker_hide__snapshot_none = Case4protection.unlocker_hide__snapshot_none
unlocker_into__snapshot_hide = Case4protection.unlocker_into__snapshot_hide
unlocker_into__snapshot_into = Case4protection.unlocker_into__snapshot_into
unlocker_into__snapshot_none = Case4protection.unlocker_into__snapshot_none
unlocker_free__snapshot_hide = Case4protection.unlocker_free__snapshot_hide
unlocker_free__snapshot_into = Case4protection.unlocker_free__snapshot_into
unlocker_free__snapshot_none = Case4protection.unlocker_free__snapshot_none
def pcmp4Case4protection_(lhs, rhs, /):
    'Case4protection -> Case4protection -> may (-1|0|1)'
    #L0, L1 = (case4protection6unlocker4lhs, case4protection6snapshot4lhs) = lhs.value
    #R0, R1 = (case4protection6unlocker4rhs, case4protection6snapshot4rhs) = rhs.value
    L0, L1 = lhs.value
    R0, R1 = rhs.value
    #return (R0 < L0, R1 < L1)
        # !! [xxx_hide is smallest by __lt__]
        # !! [xxx_hide is biggest by pcmp_]
        # => [flip (<)]
    if R0 < L0:
        if L1 < R1:
            # R0 < L0
            # R1 > L1
            return None
        # R0 < L0
        # R1 <= L1
        return -1
    if R0 == L0:
        if R1 < L1:
            # R0 == L0
            # R1 < L1
            return -1
        if R1 == L1:
            # R0 == L0
            # R1 == L1
            return 0
        # R0 == L0
        # R1 > L1
        return +1
    # R0 > L0
    if R1 < L1:
        # R0 > L0
        # R1 < L1
        return None
    if R1 == L1:
        # R0 > L0
        # R1 == L1
        return +1
    # R0 > L0
    # R1 > L1
    return +1


def _mk_pcmp_le_table4Case4protection_():
    '-> {Case4protection:{Case4protection}} # {k:{v{v<=k}}}'
    x2smaller_xs = {lhs: {rhs for rhs in sorted(Case4protection) if pcmp4Case4protection_(lhs, rhs) in (0,1)} for lhs in sorted(Case4protection)}
    return x2smaller_xs
_pcmp_le_table4Case4protection = _mk_pcmp_le_table4Case4protection_()
def _mk_pcmp_xxx_table4Case4protection__name_ver_(_pcmp_xxx_table4Case4protection, /):
    d = _pcmp_xxx_table4Case4protection
    return {k.name:{v.name for v in vs} for k, vs in d.items()}
_pcmp_le_table4Case4protection__name_ver = _mk_pcmp_xxx_table4Case4protection__name_ver_(_pcmp_le_table4Case4protection)
def _mk_pcmp_lt_table4Case4protection_():
    d = _pcmp_le_table4Case4protection
    return {k:{v for v in vs if not v==k} for k, vs in d.items()}
_pcmp_lt_table4Case4protection = _mk_pcmp_lt_table4Case4protection_()
_pcmp_lt_table4Case4protection__name_ver = _mk_pcmp_xxx_table4Case4protection__name_ver_(_pcmp_lt_table4Case4protection)

class Case4seekback(_Lt, Enum):
    # whether seekback monotonic_idx8begin
    # 2
    to_seekback     = auto()
    no_seekback = auto()
to_seekback     = Case4seekback.to_seekback
no_seekback = Case4seekback.no_seekback

def _collect_enums():
    from seed.types.Namespace import NamespaceForbidModify
    nm2x = {}
    for nm, x in globals().items():
        T = type(x)
        if T.__module__ == __name__ and T.__name__.startswith('Case4'):
            nm2x[nm] = x
    assert len(nm2x) == (3+3)+3*3 + (2+2+2)+2*2*2 +2 == 31, len(nm2x)
    return NamespaceForbidModify(nm2x)
_cases = _collect_enums()
CASES = _cases

__all__

class Bad(Exception):pass
class Bad__sconfigpack__nonfull(Bad):pass
class Bad__unmatch_case4reply5child(Bad):pass
class Bad__unmatch_case4reply5child_set(Bad):pass
class Bad__sconfig(Bad):pass
def upper4Case4protection6unlocker_(sf, ot, /):
    'Case4protection6unlocker -> Case4protection6unlocker -> Case4protection6unlocker'
    check_type_is(Case4protection6unlocker, sf)
    check_type_is(Case4protection6unlocker, ot)
    return ot if sf.lower_than4pcmp_(ot) else sf
def upper4Case4protection6snapshot_(sf, ot, /):
    'Case4protection6snapshot -> Case4protection6snapshot -> Case4protection6snapshot'
    check_type_is(Case4protection6snapshot, sf)
    check_type_is(Case4protection6snapshot, ot)
    return ot if sf.lower_than4pcmp_(ot) else sf

def upper4Case4protection_(sf, ot, /):
    'Case4protection -> Case4protection -> Case4protection'
    check_type_is(Case4protection, sf)
    check_type_is(Case4protection, ot)
    a, b = sf.value
    c, d = ot.value
    x = upper4Case4protection6unlocker_(a, c)
    y = upper4Case4protection6snapshot_(b, d)
    return Case4protection((x, y))
def _determine_case4seekback(case4reply5child, case4reply5self, /):
    sconfig = (case4reply5child, case4reply5self)
    return determine_case4seekback5sconfig_(sconfig)
def determine_case4seekback5sconfig_(sconfig, /):
    'sconfig{extra_constraints} -> Case4seekback |^Bad__sconfig'
    (case4reply5child, case4reply5self) = sconfig
    #simplified_constraints:goto

    if case4reply5child.get_xforgivable() == case4reply5self.get_xforgivable():
        # [no_seekback] <==> [[child.severe-->self.severe][child.forgivable-->self.forgivable]]
        return no_seekback
    if case4reply5child.is_severe():
        # [to_seekback] <==> [child.severe-->self.forgivable]
        return to_seekback
    assert case4reply5child.is_forgivable() and case4reply5self.is_severe()
    return Bad__sconfig(sconfig)
def determine_low_case4protection6sconfig_(sconfig, /):
    'sconfig{extra_constraints} -> low-Case4protection'
    (case4reply5child, case4reply5self) = sconfig
    #simplified_constraints:goto
    #extra_constraints:goto

    # [unlocker_free] <==> [pack.always:self.unprotected]
    # [unlocker_hide] <==> [pack.any:[child.unprotected-->self.protected]]
    # [unlocker_into] <==> [[pack.any:self.protected][pack.always:[child.unprotected-->self.unprotected]]]
    #
    if case4reply5self.is_unprotected():
        low_unlocker_xxx = unlocker_free
    elif case4reply5child.is_unprotected():
        low_unlocker_xxx = unlocker_hide
    else:
        assert case4reply5child.is_protected() and case4reply5self.is_protected()
        low_unlocker_xxx = unlocker_into
    low_unlocker_xxx

    # [snapshot_none] <==> [pack.always:[child.severe-->self.severe]]
    # [snapshot_hide] <==> [pack.any:[child.unprotected_severe-->self.forgivable]]
    # [snapshot_into] <==> [[pack.any:[child.severe-->self.forgivable]][pack.always:[child.unprotected_severe-->self.severe]]]
    if case4reply5child.is_severe() is case4reply5self.is_severe():
        low_snapshot_xxx = snapshot_none
    elif case4reply5child.is_unprotected_severe() and case4reply5self.is_forgivable():
        low_snapshot_xxx = snapshot_hide
    else:
        assert case4reply5child.is_protected_severe() and case4reply5self.is_forgivable()
        low_snapshot_xxx = snapshot_into
    low_snapshot_xxx

    low_case4protection = Case4protection((low_unlocker_xxx, low_snapshot_xxx))
    return low_case4protection

def folds_(op2_, default, lowables, /):
    'Iter _LowerThan4reversed_order -> may _LowerThan4reversed_order'
    lowables = iter(lowables)
    for x in lowables:
        break
    else:
        return default
    for y in lowables:
        x = op2_(x, y)
    return x
def determine_summary_case4protection5sconfigpack_(sconfigpack, /):
    'sconfigpack -> case4protection8summary/Case4protection'
    #simplified_constraints:goto

    assert sconfigpack
    #for sconfig in sconfigpack.items():
    #    low_case4protection = determine_low_case4protection6sconfig_(sconfig)
    case4protection = folds_(upper4Case4protection_, None, map(determine_low_case4protection6sconfig_, sconfigpack.items()))
    return case4protection


def composite__sconfig_(sconfig4self, sconfig4child, /):
    'sconfig4self -> sconfig4child -> sconfig4composite'
    (case4reply5child, case4reply5self) = sconfig4self
    (case4reply5grandchild, _case4reply5child) = sconfig4child
    if not case4reply5child == _case4reply5child:raise Bad__unmatch_case4reply5child(sconfig4self, sconfig4child)
    sconfig4composite = (case4reply5grandchild, case4reply5self)
    return sconfig4composite
def composite__sconfigpack_(sconfigpack4self, sconfigpack4child, /):
    'sconfigpack4self -> sconfigpack4child -> sconfigpack4composite'
    if not len(sconfigpack4self) == len(sconfigpack4child):raise Bad__unmatch_case4reply5child_set
    if not sconfigpack4self.keys() == sconfigpack4child.keys():raise Bad__unmatch_case4reply5child_set

    sconfigpack4composite = {}
    for sconfig4child in sconfigpack4child.items():
        (case4reply5grandchild, case4reply5child) = sconfig4child
        try:
            case4reply5self = sconfigpack4self[case4reply5child]
                # ^KeyError
        except KeyError:
            raise Bad__sconfigpack__nonfull(sconfigpack4self, case4reply5child)
        if 0:
            sconfig4self = (case4reply5child, case4reply5self)
            sconfig4composite = composite__sconfig_(sconfig4self, sconfig4child)
            #if not case4reply5child == _case4reply5child:raise Bad__unmatch_case4reply5child(sconfig4self, sconfig4child)
        sconfigpack4composite[case4reply5grandchild] = case4reply5self
    sconfigpack4composite
    assert len(sconfigpack4composite) == len(sconfigpack4child)
    return sconfigpack4composite

def composite__sexconfigpack_(sexconfigpack4self, sexconfigpack4child, /):
    'sexconfigpack4self -> sexconfigpack4child -> sexconfigpack4composite'
    (case4protection4self, sconfigpack4self) = sexconfigpack4self
    (case4protection4child, sconfigpack4child) = sexconfigpack4child
    sconfigpack4composite = composite__sconfigpack_(sconfigpack4self, sconfigpack4child)

    sexconfigpack4composite = mk_sexconfigpack_(sconfigpack4composite)
    return sexconfigpack4composite
def mk_sexconfigpack_(sconfigpack, /):
    'sconfigpack -> sexconfigpack'
    case4protection8summary = determine_summary_case4protection5sconfigpack_(sconfigpack)
    sexconfigpack = (case4protection8summary, sconfigpack)
    return sexconfigpack

def composite__sexconfig_(sexconfig4self, sexconfig4child, /):
    'sexconfig4self -> sexconfig4child -> sexconfig4composite'
    (low_case4protection4self, sconfig4self) = sexconfig4self
    (low_case4protection4child, sconfig4child) = sexconfig4child
    sconfig4composite = composite__sconfig_(sconfig4self, sconfig4child)
    sexconfig4composite = mk_sexconfig_(sconfig4composite)
    return sexconfig4composite

def determine_cache4sconfig6sconfig_(sconfig, /):
    'sconfig -> cache4sconfig'
    low_case4protection = determine_low_case4protection6sconfig_(sconfig)
    case4seekback = determine_case4seekback5sconfig_(sconfig)
    cache4sconfig = (low_case4protection, case4seekback)
    return cache4sconfig
def mk_sexconfig_(sconfig, /):
    'sconfig -> sexconfig'
    cache4sconfig = determine_cache4sconfig6sconfig_(sconfig)
    sexconfig = (cache4sconfig, sconfig)
    return sexconfig

class Setting:
    def __init__(sf, /, *, forbid_xxx_protected_ok:bool):
        check_type_is(bool, forbid_xxx_protected_ok)
        sf._no_xpk = forbid_xxx_protected_ok
            # => is_legal_case4reply_()
            # => legal_case4reply_set
            # => _tabulate_1

        sorted_legal_case4reply_seq = sorted(filter(sf.is_legal_case4reply_, Case4reply))
        #legal_case4reply_set = OrderedDict.fromkeys(sorted_legal_case4reply_seq).keys()
        legal_case4reply_set = FrozenOrderedSet(sorted_legal_case4reply_seq)
        sf._cs4r = legal_case4reply_set
            # => iter_all_good_sconfigs_
        j2good_sconfig = [*sf.iter_all_good_sconfigs_()]
        assert j2good_sconfig == sorted(j2good_sconfig)
        c2cs = xs_to_k2vs_(fst, snd, j2good_sconfig)
        c2cs = FrozenOrderedDict((c, FrozenOrderedSet(cs)) for c, cs in sorted(c2cs.items()))
        legal_case4reply5child_Z_set4good_case4reply5self = c2cs


        sf._j2good_sconfig = j2good_sconfig
            # => _tabulate_2
        _tabulate_1(sf)
            # => j2case4protection_
            # => j2legal_case4reply_
            # => j5legal_case4reply_
        _tabulate_2(sf)
            # => j2good_sconfig_
            # => j5good_sconfig_
            # => j2good_sexconfig_
            # => j5good_sexconfig_
            #tabulation ver of good-sconfig,good-sexconfig
            # => convert_good_sexconfigpack2uint_ver_
            # => convert_good_sexconfigpack5uint_ver_
            # => sexconfigpack5or_uint_ver_

        #see:above:sf._no_xpk = forbid_xxx_protected_ok
        #see:above:sf._cs4r = legal_case4reply_set
        sf._c2cs = legal_case4reply5child_Z_set4good_case4reply5self
    @property
    def forbid_xxx_protected_ok(sf, /):
        '-> bool'
        return sf._no_xpk
    def is_legal_case4reply_(sf, case4reply, /):
        check_type_is(Case4reply, case4reply)
        return not (sf.forbid_xxx_protected_ok and case4reply.is_protected_ok())
    @property
    def legal_case4reply_set(sf, /):
        '-> view OrderedSet{legal-Case4reply}'
        return sf._cs4r
    @property
    def legal_case4reply5child_Z_set4good_case4reply5self(sf, /):
        '-> view OrderedDict{legal-case4reply5child:view OrderedSet{good-case4reply5self}[#is_good_sconfig_#]}'
        return sf._c2cs
    def j2case4protection_(sf, j, /):
        'j4case4protection/uint -> Case4protection'
        return sf._j2case4protection[j]
    def j5case4protection_(sf, case4protection, /):
        'Case4protection -> j4case4protection/uint'
        #return case4protection._idx_
        return sf._j5case4protection[case4protection]
    def j2legal_case4reply_(sf, j, /):
        'j4legal_case4reply/uint -> legal-Case4reply'
        return sf._j2legal_case4reply[j]
    def j5legal_case4reply_(sf, legal_case4reply, /):
        'legal-Case4reply -> j4legal_case4reply/uint'
        return sf._j5legal_case4reply[legal_case4reply]
    def j2good_sconfig_(sf, j, /):
        'j4good_sconfig -> good-sconfig'
        return sf._j2good_sconfig[j]
    def j5good_sconfig_(sf, sconfig, /):
        'good-sconfig -> j4good_sconfig'
        return sf._j5good_sconfig[sconfig]
    def j2good_sexconfig_(sf, j, /):
        'j4good_sconfig -> good-sexconfig'
        return sf._j2good_sexconfig[j]
    def j5good_sexconfig_(sf, sexconfig, /):
        'good-sexconfig -> j4good_sconfig'
        # [j4good_sexconfig == j4good_sconfig]
        (cache4sconfig, sconfig) = sexconfig
        return sf.j5good_sconfig_(sconfig)
    def j2cache4sconfig_(sf, j, /):
        'j4cache4sconfig -> cache4sconfig'
        return sf._j2cache4sconfig[j]
    def j5cache4sconfig_(sf, cache4sconfig, /):
        'cache4sconfig -> j4cache4sconfig'
        return sf._j5cache4sconfig[cache4sconfig]


    @property
    def sorted_good_sconfigs(sf, /):
        '-> sorted [good-sconfig]'
        return sf._j2good_sconfig
    @property
    def sorted_good_sexconfigs(sf, /):
        '-> sorted [good-sexconfig]'
        return sf._j2good_sexconfig


    def is_good_sconfig_(sf, sconfig, /):
        'sconfig -> bool'
        #extra_constraints:goto
        return _is_good_sconfig(sf, sconfig)

    def is_good_sexconfig_(sf, sexconfig, /):
        'sexconfig -> bool'
        (cache4sconfig, sconfig) = sexconfig
        return sf.is_good_sconfig_(sconfig)
    def is_good_sconfigpack_(sf, sconfigpack, /):
        'sconfigpack -> bool'
        return sconfigpack.keys() == sf.legal_case4reply_set and all(map(sf.is_good_sconfig_, sconfigpack.items()))
    def is_good_sexconfigpack_(sf, sexconfigpack, /):
        'sexconfigpack -> bool'
        (case4protection8summary, sconfigpack) = sexconfigpack
        return sf.is_good_sconfigpack_(sconfigpack) and case4protection8summary == determine_summary_case4protection5sconfigpack_(sconfigpack)

    def _iter_all_cache4sconfigs(sf, /):
        '-> Iter maynotlow_cache4sconfig/cache4sconfig'
        #may be not good
        #   !! case4protection8summary <-- sexconfigpack

        #
        #cache4sconfig = (low_case4protection, case4seekback)
        return product(sorted(Case4protection), sorted(Case4seekback))
    def iter_all_sconfigs_(sf, /):
        '-> Iter sconfig'
        s = sf.legal_case4reply_set
        #s = sorted(s)#!! OrderedSet
        return product(s, s)
    def iter_all_good_sconfigs_(sf, /):
        '-> Iter good-sconfig'
        return filter(sf.is_good_sconfig_, sf.iter_all_sconfigs_())
    def iter_all_good_sexconfigs_(sf, /):
        '-> Iter good-sexconfig'
        return map(mk_sexconfig_, sf.iter_all_good_sexconfigs_())
    def iter_all_good_sconfigpacks_(sf, /):
        '-> Iter good-sconfigpack'
        return _iter_all_good_sconfigpacks(sf)
    def iter_all_good_sexconfigpacks_(sf, /):
        '-> Iter good-sexconfigpack'
        return map(mk_sexconfigpack_, sf.iter_all_good_sconfigpacks_())
    def convert_good_sexconfigpack5uint_ver_(sf, sexconfigpack__uint_ver, /):
        'sexconfigpack__uint_ver -> sexconfigpack/sexconfigpack__case_ver    # [sexconfigpack__uint_ver :: (j4case4protection, [j4legal_case4reply]{len==len(sf.legal_case4reply_set)})]'
        return _convert_good_sexconfigpack5uint_ver(sf, sexconfigpack__uint_ver)
    def convert_good_sexconfigpack2uint_ver_(sf, sexconfigpack, /):
        'sexconfigpack/sexconfigpack__case_ver -> sexconfigpack__uint_ver    # [sexconfigpack__uint_ver :: (j4case4protection, [j4legal_case4reply]{len==len(sf.legal_case4reply_set)})]'
        return _convert_good_sexconfigpack2uint_ver(sf, sexconfigpack)
    def sexconfigpack5or_uint_ver_(sf, case_vs_uint, sexconfigpack_or_uint_ver, /):
        val = sexconfigpack_or_uint_ver
        if case_vs_uint:
            sexconfigpack__uint_ver = val
            sexconfigpack = sf.convert_good_sexconfigpack5uint_ver_(sexconfigpack__uint_ver)
        else:
            sexconfigpack = val
        sexconfigpack
        return sexconfigpack
#-end-class-API

def _is_good_sconfig(sf, sconfig, /):
    'Setting -> sconfig -> bool'
    #extra_constraints:goto
    (case4reply5child, case4reply5self) = sconfig

    if sf.forbid_xxx_protected_ok:
        if case4reply5child.is_protected_ok() or case4reply5self.is_protected_ok():
            return False
    assert sf.is_legal_case4reply_(case4reply5child)
    assert sf.is_legal_case4reply_(case4reply5self)

    #
    if (case4reply5child.is_forgivable() and case4reply5self.is_severe()):
        # forbid:[child.forgivable-->self.severe]
        #   !! eof
        return False
    #
    if (case4reply5child.is_severe_fail() and case4reply5self.is_severe_ok()):
        # forbid:[child.severe_fail-->self.severe_ok]
        #   !! *_severe_fail .monotonic_idx8end unpredictable
        return False
    #
    return True
#end-def _is_good_sconfig(sf, sconfig, /):
def _iter_all_good_sconfigpacks(sf, /):
    'Setting -> Iter good-sconfigpack'
    c2cs = sf.legal_case4reply5child_Z_set4good_case4reply5self
        # :: {case4reply5child:{case4reply5self}[#is_good_sconfig_#]}
        # !! OrderedDict<c,OrderedSet>
        # =>no:sorted()

    ps = [*c2cs.items()]
    k_cs_pairs = ps
    ks = [*map(fst, k_cs_pairs)]
        # :: [case4reply5child]
    css = [*map(snd, k_cs_pairs)]
        # :: [{case4reply5self}]
    szs = [*map(len, css)]
    full_count = prod(szs)
        # [[forbid_xxx_protected_ok:=False] -> [total4sconfigpack == (4*4*4*4 * 6*6*8*8) == 589824]]
        # [[forbid_xxx_protected_ok:=True]  -> [total4sconfigpack == (1*3*3*3 * 5*5*1*6) == 4050]]
        #
        # [[forbid_xxx_protected_ok:=False] -> [total4sconfig == (4+4+4+4 + 6+6+8+8) == 44]]
        # [[forbid_xxx_protected_ok:=True]  -> [total4sconfig == (0+3+3+3 + 5+5+0+6) == 25]]

    full_count
    _sz = 0
    for _sz, cs in enumerate(product(*css), 1):
        k2c = dict(zip(ks, cs))
        sconfigpack = k2c
        assert sf.is_good_sconfigpack_(sconfigpack)
        yield sconfigpack
    assert _sz == full_count, (sf.forbid_xxx_protected_ok, k_cs_pairs, (_sz, full_count))
    return
#end-def _iter_all_good_sconfigpacks(sf, /):

def _mk_bijection(xs, /):
    j2x = sorted(xs)
    j5x = {x:j for j, x in enumerate(j2x)}
    if not len(j2x) == len(j5x):raise Exception
    return (j2x, j5x)
def _tabulate_1(sf, /):
    '# sf.legal_case4reply_set => sf.(_j2case4protection, _j5case4protection, _j2legal_case4reply, _j5legal_case4reply)'
    #j2case4protection = sorted(Case4protection)
    #for i, c in enumerate(j2case4protection):
    #    c._idx_ = i
    (j2case4protection, j5case4protection) = _mk_bijection(Case4protection)
    (j2legal_case4reply, j5legal_case4reply) = _mk_bijection(sf.legal_case4reply_set)

    sf._j2case4protection = j2case4protection
    sf._j5case4protection = j5case4protection
    sf._j2legal_case4reply = j2legal_case4reply
    sf._j5legal_case4reply = j5legal_case4reply
    return


def _tabulate_2(sf, /):
    'tabulation ver of good-sconfig,good-sexconfig # sf._j2good_sconfig => sf.(_j2good_sexconfig, _j5good_sconfig, sf._j2cache4sconfig, sf._j5cache4sconfig)'
    (_j2good_sconfig, sf._j5good_sconfig) = _mk_bijection(sf._j2good_sconfig)
    assert _j2good_sconfig == sf._j2good_sconfig
    (sf._j2good_sexconfig, _j5good_sexconfig) = _mk_bijection(map(mk_sexconfig_, sf._j2good_sconfig))
    #no:_j5good_sexconfig
    (sf._j2cache4sconfig, sf._j5cache4sconfig) = _mk_bijection(sf._iter_all_cache4sconfigs())
    return
def _convert_good_sexconfigpack5uint_ver(sf, sexconfigpack__uint_ver, /):
    'Setting -> sexconfigpack__uint_ver -> sexconfigpack/sexconfigpack__case_ver    # [sexconfigpack__uint_ver :: (j4case4protection, [j4legal_case4reply]{len==len(sf.legal_case4reply_set)})]'

    (i, j2k) = sexconfigpack__uint_ver
    assert len(j2k) == len(sf.legal_case4reply_set)

    case4protection8summary = sf.j2case4protection_(i)
    #bug:cache4sconfig = sf.j2cache4sconfig_(i)

    j2c_ = sf.j2legal_case4reply_
    sconfigpack = {j2c_(j):j2c_(k) for j, k in enumerate(j2k)}
        # {case4reply5child:case4reply5self}

    assert sconfigpack.keys() == sf.legal_case4reply_set.set_view()
    sexconfigpack = (case4protection8summary, sconfigpack)
    return sexconfigpack#case_ver
def _convert_good_sexconfigpack2uint_ver(sf, sexconfigpack, /):
    'Setting -> sexconfigpack/sexconfigpack__case_ver -> sexconfigpack__uint_ver    # [sexconfigpack__uint_ver :: (j4case4protection, [j4legal_case4reply]{len==len(sf.legal_case4reply_set)})]'
    (case4protection8summary, sconfigpack) = sexconfigpack

    assert sconfigpack.keys() == sf.legal_case4reply_set.set_view()

    #bug:i = sf.j5cache4sconfig_(cache4sconfig)
    i = sf.j5case4protection_(case4protection8summary)
    j2k = tuple(map(sf.j5good_sconfig_, sorted(sconfigpack.items())))
    assert len(j2k) == len(sf.legal_case4reply_set)

    sexconfigpack__uint_ver = (i, j2k)
    return sexconfigpack__uint_ver


#end-class Setting:




#sorted
#-forbid_xxx_protected_ok
#frozen



class _WeakSymbolizeRegister4sexconfigpack(WeakSymbolizeRegister):
    'WeakSymbolizeRegister<sexconfigpack>'
    def __init__(sf, setting, /, *, case_vs_uint):
        check_type_is(Setting, setting)
        check_type_is(bool, case_vs_uint)
        sf._setting = setting
        sf._case_vs_uint = case_vs_uint
        super().__init__()
    @property
    def setting(sf, /):
        '-> Setting'
        return sf._setting
    @property
    def case_vs_uint(sf, /):
        '-> bool'
        return sf._case_vs_uint

    #@override
    def _check_value_(sf, val, /):
        'val/hashable -> None|^Exception'
        sexconfigpack = sf._setting.sexconfigpack5or_uint_ver_(sf._case_vs_uint, val)
        if not sf._setting.is_good_sexconfigpack_(sexconfigpack):raise Exception(val)

if 1:
    setting0 = Setting(forbid_xxx_protected_ok=False)
    setting1 = Setting(forbid_xxx_protected_ok=True)
    _2setting = (setting0, setting1)
if 1:
    weak_symbolize_register4sexconfigpack__allow_xxxx_protected_ok = _WeakSymbolizeRegister4sexconfigpack(setting0, case_vs_uint=False)
    weak_symbolize_register4sexconfigpack__forbid_xxx_protected_ok = _WeakSymbolizeRegister4sexconfigpack(setting1, case_vs_uint=False)
    _2wk25good_sexconfigpack = (weak_symbolize_register4sexconfigpack__allow_xxxx_protected_ok, weak_symbolize_register4sexconfigpack__forbid_xxx_protected_ok)

def get_setting_(forbid_xxx_protected_ok, /):
    '-> Setting'
    check_type_is(bool, forbid_xxx_protected_ok)
    return _2setting[forbid_xxx_protected_ok]
def get_weak_symbolize_register4sexconfigpack_(forbid_xxx_protected_ok, /):
    check_type_is(bool, forbid_xxx_protected_ok)
    return _2wk25good_sexconfigpack[forbid_xxx_protected_ok]

def is_good_sexconfigpack_(sexconfigpack, /, *, forbid_xxx_protected_ok):
    'sexconfigpack -> bool'
    setting = get_setting_(forbid_xxx_protected_ok)
    return setting.is_good_sexconfigpack_(sexconfigpack)



























######################
######################
######################
######################
######################
######################
######################
######################
######################
######################

def mk_gi4IRecognizerLLoo__5solo_rgnr_transform_cases_(mk_Call_, to_lift:bool, good_sexconfigpack:'sexconfigpack{good}', rgnr, unlocker, ignore, istream, /, *, case_vs_sym_vs_uint:'may bool', forbid_xxx_protected_ok:False):
    'to_lift/bool -> sexconfigpack{good} -> IRecognizerLLoo -> IUnlocker -> ignore/bool -> istream/IRecoverableInputStream -> GenIter[#see:IRecognizerLLoo._mk_gi4recognize_()#]  # [whether?allow?:protected_ok/(protected_severe_ok|protected_forgivable_ok)] #[sexconfigpack ~=~ (i/uint%9, [k{<(8|6)}]{len=(8|6)})] ==>> [case_vs_uint/bool: (sexconfigpack | (i,j2k/[k]))] #[case_vs_sym_vs_uint == may case_vs_uint]'
    setting = get_setting_(forbid_xxx_protected_ok)
    if not forbid_xxx_protected_ok is setting.forbid_xxx_protected_ok:raise TypeError
    #assert sf.is_good_sexconfigpack_(good_sexconfigpack)

    if case_vs_sym_vs_uint is None:
        _sym = good_sexconfigpack
        _wd = weak_symbolize_register4exconfigpack = get_weak_symbolize_register4sexconfigpack_(forbid_xxx_protected_ok)
        if not forbid_xxx_protected_ok is _wd.setting.forbid_xxx_protected_ok:raise TypeError
        if not setting is _wd.setting:raise TypeError
        good_sexconfigpack = _wd.lookup(_sym)
        case_vs_uint = _wd.case_vs_uint
    else:
        case_vs_uint = case_vs_sym_vs_uint
    good_sexconfigpack
    case_vs_uint
    check_type_is(bool, case_vs_uint)
    if case_vs_uint:
        sexconfigpack__uint_ver = good_sexconfigpack
        (_i, _j2k) = sexconfigpack__uint_ver
        case4protection8summary = setting.j2case4protection_(_i)
    else:
        sexconfigpack = good_sexconfigpack
        (case4protection8summary, sconfigpack) = sexconfigpack
    case4protection8summary
    #(unlocker_xxx, snapshot_xxx) = case4protection8summary.value
    (case4protection6unlocker, case4protection6snapshot) = case4protection8summary.value
    ######################
    # maybe [unlocker.known_released]
    #   eg [unlocker := dummy_unlocker]
    unlocker4self = unlocker if not unlocker.known_released else (detection_unlocker := DetectionUnlocker())
    assert not unlocker4self.known_released
    # [not unlocker4self.known_released]
    del unlocker
    match case4protection6unlocker:
        case _cases.unlocker_into:
            unlocker4child = unlocker4self
        case _cases.unlocker_hide:
            unlocker4child = dummy_unlocker
        case _cases.unlocker_free:
            unlocker4self.unlocker_release()
            # [unlocker4self.known_released]
            unlocker4child = dummy_unlocker
        case _:
            raise 000
    unlocker4child
    # maybe [unlocker4child.known_released]
    #   !! dummy_unlocker
    # maybe [unlocker4self.known_released]
    #   !! unlocker_free
    # [[unlocker4self.known_released] <-> [unlocker_free]]

    ######################
    #unlocker4child += detection_unlocker = DetectionUnlocker()
    match case4protection6snapshot:
        case _cases.snapshot_none:
            pass#no:snapshot
            may_snapshot = None
        case _cases.snapshot_into:
            snapshot = istream.save2snapshot()
            may_snapshot = snapshot
        case _cases.snapshot_hide:
            snapshot = istream.save2snapshot()
            may_snapshot = snapshot
            pass#not attach to unlocker4child
        case _:
            raise 000
    may_snapshot
    # maybe [unlocker4child.known_released]
    if unlocker4child.known_released:
        detection_unlocker = DetectionUnlocker()
        unlocker4child = detection_unlocker
    assert not unlocker4child.known_released

    # [[unlocker4self.known_released] <-> [unlocker_free]]
    # [not unlocker4child.known_released]
    ######################
    if to_lift:
        ext_info8begin = istream.tell_ext_info()
    monotonic_idx8begin = istream.tell_monotonic_idx()
    reply5child = yield mk_Call_(rgnr, unlocker4child, ignore, istream)
    istream8end = istream
    case4reply5child = mk_case4reply5child(unlocker4child, monotonic_idx8begin, reply5child, istream8end)
    #paritally_check_case4reply5xxx___whether_protected_ok(case4reply5child, forbid_xxx_protected_ok=forbid_xxx_protected_ok)
    _check_case4reply5xxx(case4reply5child, forbid_xxx_protected_ok)
    ######################
    if case_vs_uint:
        _j = setting.j5legal_case4reply_(case4reply5child)
        _k = _j2k[_j]
        case4reply5self = setting.j2legal_case4reply_(_k)
    else:
        case4reply5self = sconfigpack[case4reply5child]
    case4reply5self
    case4seekback = _determine_case4seekback(case4reply5child, case4reply5self)
    reply = reply5child
    ######################
    if to_lift:
        # [should be first alter of reply]
        sconfig = (case4reply5child, case4reply5self)
        maynotlow_cache4sconfig = (case4protection8summary, case4seekback)
        maynotlow_sexconfig = (maynotlow_cache4sconfig, sconfig)
            #may be not good
            #   !! case4protection8summary <-- sexconfigpack
        maynotlow_sexconfig
        payload4lifted_eresult = (reply5child, maynotlow_sexconfig, ext_info8begin)
            # ++reply5child.ext_info8end
        reply = reply.ireplace(eresult=reply.eresult.ireplace__payload(payload4lifted_eresult))
    ######################
    match case4seekback:
        case _cases.no_seekback:
            pass
        case _cases.to_seekback:
            snapshot.restore_and_release(istream)
            istream8end = istream
            reply = reply.ireplace(ext_info8end=istream8end.tell_ext_info())
                # [ext_info8end := ext_info8begin]
        case _:
            raise 000
    if not may_snapshot is None:
        snapshot.snapshot_release()
    ######################
    #(case4reply6xprotected, case4reply6xforgivable, case4reply6xok) = case4reply5self
    ######
    if case4reply5self.is_unprotected():
        unlocker4self.unlocker_release()
            #<<==unlocker_hide
        #bug:
            # !! unlocker_hide
            #『unlocker4child.unlocker_release()』
            #『assert not _protected』
        #now cancel auto release:unlocker_release() <<== [@fail:not reply.ok: (unlocker>>snapshot) should not unlocker_release()!]
    else:
        assert not unlocker4self.known_released
        assert case4reply5child.is_protected() or case4protection8summary.is_unlocker_hide()
    ######
    #bug:assert case4reply5self.is_forgivable() is case4reply5child.is_forgivable()
    if case4reply5self.is_forgivable():
        assert case4reply5child.is_forgivable() or case4seekback == to_seekback
    else:
        assert not case4reply5child.is_forgivable()
    ######
    if case4reply5self.is_ok() is case4reply5child.is_ok():
        pass
    else:
        reply = reply.ireplace(eresult=~reply.eresult)
    ######
    reply
    ######################
    reply5self = reply
    _case4reply5self = mk_case4reply5self(unlocker4self, monotonic_idx8begin, reply5self, istream8end)
    assert case4reply5self == _case4reply5self
    _check_case4reply5xxx(case4reply5self, forbid_xxx_protected_ok)
    ######################
    return reply5self
def _check_case4reply5xxx(case4reply5xxx, forbid_xxx_protected_ok, /):
    if forbid_xxx_protected_ok:
        if case4reply5xxx.is_protected_ok():raise TypeError
def mk_case4reply5child(unlocker4child, monotonic_idx8begin, reply5child, istream8end, /):
    return mk_case4reply5xxx(unlocker4child, monotonic_idx8begin, reply5child, istream8end)
def mk_case4reply5self(unlocker4self, monotonic_idx8begin, reply5self, istream8end, /):
    return mk_case4reply5xxx(unlocker4self, monotonic_idx8begin, reply5self, istream8end)
def mk_case4reply5xxx(unlocker4xxx, monotonic_idx8begin, reply5xxx, istream8end, /):
    unchanged = monotonic_idx8begin == istream8end.tell_monotonic_idx()
    _protected = not unlocker4xxx.known_released
    _forgivable = unchanged
    _ok = reply5xxx.ok
    case4reply6xprotected = protected if _protected else unprotected
    case4reply6xforgivable = forgivable if _forgivable else severe
    case4reply6xok = ok if _ok else fail
    case4reply5child = Case4reply((case4reply6xprotected, case4reply6xforgivable, case4reply6xok))
    return case4reply5child








def _pseudo_sexconfigpack5sexconfig(setting, sexconfig, /):
    ((low_case4protection, case4seekback), (case4reply5child, case4reply5self)) = (cache4sconfig, sconfig) = sexconfig
    sz = len(setting.legal_case4reply_set)
    pseudo_sconfigpack = _Pseudo_sconfigpack(sz, case4reply5child, case4reply5self)
    pseudo_sexconfigpack = (case4protection8summary:=low_case4protection, pseudo_sconfigpack)
    return pseudo_sexconfigpack

class _Pseudo_sconfigpack:
    def __init__(sf, sz, case4reply5child, case4reply5self, /):
        sf._sz = sz
        sf._k = case4reply5child
        sf._v = case4reply5self
    def __len__(sf, /):
        return sf._sz
    def __getitem__(sf, k, /):
        if not k == sf._k:raise KeyError(k, sf._k)
        return sf._v





#behin:validate____roughly_composite__case4protection_

def _init4validate____roughly_composite__case4protection_(setting, /):
    from seed.tiny import echo
    from seed.types.Either import Cased, Either
    from seed.types.Either import mk_Left, mk_Right

    #sexconfig := (cache4sconfig, sconfig)
    #cache4sconfig := (low_case4protection, case4seekback)
    good_sexconfigs = setting.sorted_good_sexconfigs
        # :: [sexconfig]
        # :: [(cache4sconfig, sconfig)]
        # :: [((low_case4protection, case4seekback), (case4reply5child, case4reply5self))]

    def f(sexconfig4self, /):
        'sexconfig4self -> case4reply5self'
        (cache4sconfig4self, (case4reply5child, case4reply5self)) = sexconfig4self
        return case4reply5self

    case4reply5self_Z_sexconfigs4self = xs_to_k2vs_(f, echo, good_sexconfigs)
        # :: {case4reply5self:[sexconfig4self]}
    case4reply5child_Z_sexconfigs4child = case4reply5self_Z_sexconfigs4self
        # :: {case4reply5child:[sexconfig4child]}
    sz = len(setting.legal_case4reply_set)
    assert len(case4reply5child_Z_sexconfigs4child) == sz, (len(case4reply5child_Z_sexconfigs4child), sz, setting.forbid_xxx_protected_ok, sorted(case4reply5child_Z_sexconfigs4child))

    ######################
    from seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo import IRecognizerLLoo, Reply, RecognizeReply, dummy_unlocker# mk_Call_, RecognizeCall
    def mk_Call_(rgnr, unlocker, ignore, istream, /):
        '-> pseudo_rcall/(rgnr, unlocker, ignore, istream)'
        return (rgnr, unlocker, ignore, istream)
    def mk_pseudo_rgnr_and_reset_istream_(case4reply5grandchild, pseudo_istream, /):
        pseudo_istream.seek_monotonic_idx(monotonic_idx8begin)
        def pseudo_rgnr(unlocker4grandchild, pseudo_istream, /):
            assert not unlocker4grandchild.known_released
            assert pseudo_istream.tell_monotonic_idx() == monotonic_idx8begin
            if case4reply5grandchild.is_unprotected():
                unlocker4grandchild.unlocker_release()
            if case4reply5grandchild.is_severe():
                pseudo_istream.seek_monotonic_idx(monotonic_idx8end)
            pseudo_istream
            eresult5grandchild = Either(case4reply5grandchild.is_ok(), 999)
            reply5grandchild = Reply(eresult5grandchild, pseudo_istream.tell_ext_info())
            _case4reply5grandchild = mk_case4reply5xxx(unlocker4xxx:=unlocker4grandchild, monotonic_idx8begin, reply5xxx:=reply5grandchild, istream8end:=pseudo_istream)
            assert case4reply5grandchild == _case4reply5grandchild, (case4reply5grandchild, _case4reply5grandchild)
            return reply5grandchild
        return pseudo_rgnr
    from seed.types.stream.IRecoverableInputStream import PlainRecoverableInputStream5token_seq#dummy_unlocker, DetectionUnlocker
    from seed.types.IToken import mk_token_rawstream__5xs__idx_
    #def mk_token_rawstream__5xs__idx_(offset, xs, ex_arg=None, /, *, tkey_vs_tdat_vs_tkd:'(0|1|2)'):
    chars = 'abc'
    rawstream = mk_token_rawstream__5xs__idx_(offset:=0, tdats:=chars, tkey:='char', tkey_vs_tdat_vs_tkd=1)
    (prev_token_end_gap_position_info, iter_tokens) = rawstream
    token_seq = [*iter_tokens]; del iter_tokens
    #
    mk_Call_
    to_lift = True
    mk_token_rawstream__5xs__idx_#pseudo_rgnr
    ignore = False
    pseudo_istream = PlainRecoverableInputStream5token_seq(max_num_tokens6backward:=0, may_prev_token_end_gap_position_info:=None, offset:=0, token_seq)
    777;    monotonic_idx8begin = pseudo_istream.tell_monotonic_idx()
    777;    monotonic_idx8end = monotonic_idx8begin+1
    ######################
    def vivi_call(pseudo_sexconfigpack4self, pseudo_rgnr8self, unlocker4self, pseudo_rcall2reply5child, /, *args4pseudo_rcall2reply5child):
        #def mk_gi4IRecognizerLLoo__5solo_rgnr_transform_cases_(mk_Call_, to_lift:bool, good_sexconfigpack:'sexconfigpack{good}', rgnr, unlocker, ignore, istream, /, *, case_vs_sym_vs_uint:'may bool', forbid_xxx_protected_ok:False):
        #mk_Call_
        #to_lift
        #ignore
        #pseudo_istream
        gi8self = mk_gi4IRecognizerLLoo__5solo_rgnr_transform_cases_(mk_Call_, to_lift, pseudo_sexconfigpack4self, pseudo_rgnr8self, unlocker4self, ignore, pseudo_istream, case_vs_sym_vs_uint=False, forbid_xxx_protected_ok=setting.forbid_xxx_protected_ok)
        pseudo_rcall8child = gi8self.send(None)
        reply5child = pseudo_rcall2reply5child(pseudo_rcall8child, *args4pseudo_rcall2reply5child)
        try:
            gi8self.send(reply5child)
        except StopIteration as e:
            reply5self = e.value
        else:
            raise 000
        return reply5self
    def pseudo_rcall2reply5child(pseudo_rcall8child, pseudo_sexconfigpack4child, /):
        '-> reply5child'
        #pseudo_rcall/(rgnr, unlocker, ignore, istream)
        (pseudo_rgnr8child, unlocker4child, ignore, pseudo_istream) = pseudo_rcall8child
        reply5child = vivi_call(pseudo_sexconfigpack4child, pseudo_rgnr8child, unlocker4child, pseudo_rcall2reply5grandchild)
        return reply5child
    def pseudo_rcall2reply5grandchild(pseudo_rcall8grandchild, /):
        '-> reply5grandchild'
        (pseudo_rgnr8grandchild, unlocker4grandchild, ignore, pseudo_istream) = pseudo_rcall8grandchild
        #assert pseudo_rgnr8grandchild is pseudo_rgnr
        pseudo_rgnr = pseudo_rgnr8grandchild
        reply5grandchild = pseudo_rgnr(unlocker4grandchild, pseudo_istream)
        return reply5grandchild
    ######################
    _init_result4validate = (good_sexconfigs, case4reply5child_Z_sexconfigs4child, (mk_Call_, to_lift, mk_pseudo_rgnr_and_reset_istream_, ignore, pseudo_istream, vivi_call, pseudo_rcall2reply5child, pseudo_rcall2reply5grandchild))
    return _init_result4validate
#end-def _init4validate____roughly_composite__case4protection_(setting, /):
def _iter4validate____roughly_composite__case4protection_(setting, good_sexconfigs, case4reply5child_Z_sexconfigs4child, /):
    def h(sexconfig4self, /):
        'sexconfig4self -> case4reply5child'
        (cache4sconfig4self, (case4reply5child, case4reply5self)) = sexconfig4self
        return case4reply5child
    def iter_sexconfigs4child_5sexconfig4self_(sexconfig4self, /):
        '-> Iter sexconfig4child'
        case4reply5child = h(sexconfig4self)
        sexconfigs4child = case4reply5child_Z_sexconfigs4child[case4reply5child]
        return iter(sexconfigs4child)
    iter_sexconfigs4child_5sexconfig4self_

    for sexconfig4self in good_sexconfigs:
      for sexconfig4child in iter_sexconfigs4child_5sexconfig4self_(sexconfig4self):
        sexconfig4composite = composite__sexconfig_(sexconfig4self, sexconfig4child)
        #(cache4sconfig4xxx, (case4reply5child, case4reply5self)) = sexconfig4xxx
        #   (self|child|composite)
        #
        ######################
        #find a best sexconfigpack contains this sexconfig
        pseudo_sexconfigpack4self = _pseudo_sexconfigpack5sexconfig(setting, sexconfig4self)
        pseudo_sexconfigpack4child = _pseudo_sexconfigpack5sexconfig(setting, sexconfig4child)
        pseudo_sexconfigpack4composite = _pseudo_sexconfigpack5sexconfig(setting, sexconfig4composite)
        # pseudo_sexconfigpack4xxx
        #   (self|child|composite)
        yield (sexconfig4self, sexconfig4child, pseudo_sexconfigpack4self, pseudo_sexconfigpack4child, pseudo_sexconfigpack4composite)
    return

def validate____roughly_composite__case4protection_(*, forbid_xxx_protected_ok):
    setting = get_setting_(forbid_xxx_protected_ok)
    _init_result4validate = _init4validate____roughly_composite__case4protection_(setting)
    (good_sexconfigs, case4reply5child_Z_sexconfigs4child, (mk_Call_, to_lift, mk_pseudo_rgnr_and_reset_istream_, ignore, pseudo_istream, vivi_call, pseudo_rcall2reply5child, pseudo_rcall2reply5grandchild)) = _init_result4validate
    for (sexconfig4self, sexconfig4child, pseudo_sexconfigpack4self, pseudo_sexconfigpack4child, pseudo_sexconfigpack4composite) in _iter4validate____roughly_composite__case4protection_(setting, good_sexconfigs, case4reply5child_Z_sexconfigs4child):
        (cache4sconfig4child, (case4reply5grandchild, _case4reply5child)) = sexconfig4child
        pseudo_rgnr = mk_pseudo_rgnr_and_reset_istream_(case4reply5grandchild, pseudo_istream)
        pseudo_rgnr8self = pseudo_rgnr
        unlocker4self = DetectionUnlocker()
        assert not unlocker4self.known_released
        _1_reply5self = vivi_call(pseudo_sexconfigpack4composite, pseudo_rgnr8self, unlocker4self, pseudo_rcall2reply5grandchild)
            # reply5self via single composite layer

        pseudo_rgnr = mk_pseudo_rgnr_and_reset_istream_(case4reply5grandchild, pseudo_istream)
        pseudo_rgnr8self = pseudo_rgnr
        unlocker4self = DetectionUnlocker()
        _2_reply5self = vivi_call(pseudo_sexconfigpack4self, pseudo_rgnr8self, unlocker4self, pseudo_rcall2reply5child, pseudo_sexconfigpack4child)
            # reply5self via two layers

    return
#end-def validate____roughly_composite__case4protection_(*, forbid_xxx_protected_ok):























class _mkr4high_freq_sconfigpacks:
    r'''[[[
    maker<sconfigpack> :: forbid_xxx_protected_ok -> name<filter_> -> sconfigpack
    filter_<sconfigpack> :: case4reply5child -> case4reply5self

name<filter_>:
_echo_,lookahead,not_followed_by,protect_header,lift__forgivable,lift__strict,whole8header,empty8header,followed_by,protect_whole,optional__forgivable,optional__strict,trial_and_error
    trial_and_error=[def]=protect_header

######################
#_echo_ : _ --> _
#lookahead : severe --> forgivable
#not_followed_by === (invert_ok_err <<< lookahead)
#protect_header : protected_severe_fail --> protected_forgivable_fail
#lift__forgivable : forgivable_fail --> forgivable_ok
#lift__strict : protected_forgivable_fail --> forgivable_ok
#whole8header : unprotected-->protected
#empty8header : protected --> unprotected
######################
#followed_by = lookahead # ++[ignore:=True]
#trial_and_error = protect_header
#protect_whole = composite__sconfigpack_(protect_header, whole8header)
#optional__forgivable = composite__sconfigpack_(lift__forgivable, protect_header) # >>> (spostprocess)
#optional__strict = composite__sconfigpack_(lift__strict, protect_header) # >>> (spostprocess)
######################
    #]]]'''#'''
    ######################
    #maker<sconfigpack>
    ######################
    def mk_sconfigpack_(forbid_xxx_protected_ok, name, /):
        '-> sconfigpack'
        from seed.tiny import echo
        setting = get_setting_(forbid_xxx_protected_ok)
        filter_ = getattr(__class__, name)
        g = __class__._on_forbid_xxx_protected_ok if forbid_xxx_protected_ok else echo
        sconfigpack = {case4reply5child: g(filter_(case4reply5child)) for case4reply5child in setting.legal_case4reply_set}
        return sconfigpack
    def _on_forbid_xxx_protected_ok(case4reply5self, /):
        if case4reply5self.is_protected_ok():
            case4reply5self = case4reply5self.flip_xprotected()
        return case4reply5self

    ######################
    #name<filter_>
    ######################
    name_seq4filter = tuple('_echo_,lookahead,not_followed_by,protect_header,lift__forgivable,lift__strict,whole8header,empty8header,followed_by,protect_whole,optional__forgivable,optional__strict,trial_and_error'.split(','))

    ######################
    #filter_<sconfigpack>
    ######################
    def _echo_(case4reply5child, /):
        case4reply5self = case4reply5child
        return case4reply5self
    def lookahead(case4reply5child, /):
        case4reply5self = case4reply5child.flip_xforgivable() if case4reply5child.is_severe() else case4reply5child
        return case4reply5self
    def not_followed_by(case4reply5child, /):
        case4reply5self = __class__.lookahead(case4reply5child).flip_xok()
        #not_followed_by = flip_xok <<< lookahead # ++[ignore:=True]
        return case4reply5self
    def protect_header(case4reply5child, /):
        case4reply5self = protected_forgivable_fail if case4reply5child == protected_severe_fail else case4reply5child
        return case4reply5self
    def lift__forgivable(case4reply5child, /):
        case4reply5self = case4reply5child.flip_xok() if case4reply5child.is_forgivable_fail() else case4reply5child
        return case4reply5self
    def lift__strict(case4reply5child, /):
        case4reply5self = protected_forgivable_ok if case4reply5child == protected_forgivable_fail else case4reply5child
        return case4reply5self
    def whole8header(case4reply5child, /):
        case4reply5self = case4reply5child.flip_xprotected() if case4reply5child.is_unprotected() else case4reply5child
        return case4reply5self
    def empty8header(case4reply5child, /):
        case4reply5self = case4reply5child.flip_xprotected() if case4reply5child.is_protected() else case4reply5child
        return case4reply5self
    def followed_by(case4reply5child, /):
        case4reply5self = __class__.lookahead(case4reply5child)
        #followed_by = lookahead # ++[ignore:=True]
        return case4reply5self
    trial_and_error = protect_header
    def protect_whole(case4reply5child, /):
        case4reply5self = __class__.protect_header(__class__.whole8header(case4reply5child))
        #protect_whole = composite__sconfigpack_(protect_header, whole8header)
        return case4reply5self
    def optional__forgivable(case4reply5child, /):
        case4reply5self = __class__.lift__forgivable(__class__.protect_header(case4reply5child))
        #optional__forgivable = composite__sconfigpack_(lift__forgivable, protect_header) # >>> (spostprocess)
        return case4reply5self
    def optional__strict(case4reply5child, /):
        case4reply5self = __class__.lift__strict(__class__.protect_header(case4reply5child))
        #optional__strict = composite__sconfigpack_(lift__strict, protect_header) # >>> (spostprocess)
        return case4reply5self
#end-class _mkr4high_freq_sconfigpacks:

class _high_freq_sconfigpacks:
    r'''[[[

2may_ignore
    followed_by=True
    not_followed_by=True
forbid_xxx_protected_ok=>
    del (protected_ok-->?)
    rename (?-->protected_ok) (?-->unprotected_ok)

    #]]]'''#'''
    ######################
    def register():
        __class__
        __class__.validate()
        b2nm2sym = ({}, {})
        for forbid_xxx_protected_ok, nm in product([False, True], __class__._nms):
            setting = get_setting_(forbid_xxx_protected_ok)
            weak_symbolize_register4sexconfigpack = get_weak_symbolize_register4sexconfigpack_(forbid_xxx_protected_ok)
            nm2sym = b2nm2sym[forbid_xxx_protected_ok]
            ######################
            sconfigpack__compute = _mkr4high_freq_sconfigpacks.mk_sconfigpack_(forbid_xxx_protected_ok, nm)
            sexconfigpack = mk_sexconfigpack_(sconfigpack__compute)
            ######################
            sym = weak_symbolize_register4sexconfigpack.symbolize(sexconfigpack)
            nm2sym[nm] = sym
        return b2nm2sym
    def validate():
        __class__
        assert (__0:=__class__._nms) == (__1:={*_mkr4high_freq_sconfigpacks.name_seq4filter}), (__0-__1, __1-__0)
        forbid_xxx_protected_ok = False
        setting = get_setting_(forbid_xxx_protected_ok)
        #for nm in _mkr4high_freq_sconfigpacks.name_seq4filter:
        for nm in __class__._nms:
            sconfigpack__compute = _mkr4high_freq_sconfigpacks.mk_sconfigpack_(forbid_xxx_protected_ok, nm)
            sconfigpack__manually = getattr(__class__, nm)
            assert sconfigpack__manually.keys() == setting.legal_case4reply_set.set_view
            assert sconfigpack__manually == sconfigpack__compute, (nm, sconfigpack__manually, sconfigpack__compute)
    ######################
    _nms = ...
    _nms = {*locals()}
    ######################
#_echo_ : _ --> _
    _echo_ = ({**{}
,protected_forgivable_ok        :protected_forgivable_ok
,protected_forgivable_fail      :protected_forgivable_fail
,protected_severe_ok            :protected_severe_ok
,protected_severe_fail          :protected_severe_fail
,unprotected_forgivable_ok      :unprotected_forgivable_ok
,unprotected_forgivable_fail    :unprotected_forgivable_fail
,unprotected_severe_ok          :unprotected_severe_ok
,unprotected_severe_fail        :unprotected_severe_fail
})
#lookahead : severe --> forgivable
    lookahead = ({**{}
,protected_forgivable_ok        :protected_forgivable_ok
,protected_forgivable_fail      :protected_forgivable_fail
,protected_severe_ok            :protected_forgivable_ok
,protected_severe_fail          :protected_forgivable_fail
,unprotected_forgivable_ok      :unprotected_forgivable_ok
,unprotected_forgivable_fail    :unprotected_forgivable_fail
,unprotected_severe_ok          :unprotected_forgivable_ok
,unprotected_severe_fail        :unprotected_forgivable_fail
})
#not_followed_by === (invert_ok_err <<< lookahead)
    not_followed_by = ({**{}
,protected_forgivable_ok        :protected_forgivable_fail
,protected_forgivable_fail      :protected_forgivable_ok
,protected_severe_ok            :protected_forgivable_fail
,protected_severe_fail          :protected_forgivable_ok
,unprotected_forgivable_ok      :unprotected_forgivable_fail
,unprotected_forgivable_fail    :unprotected_forgivable_ok
,unprotected_severe_ok          :unprotected_forgivable_fail
,unprotected_severe_fail        :unprotected_forgivable_ok
})
#protect_header : protected_severe_fail --> protected_forgivable_fail
    protect_header = ({**{}
,protected_forgivable_ok        :protected_forgivable_ok
,protected_forgivable_fail      :protected_forgivable_fail
,protected_severe_ok            :protected_severe_ok
,protected_severe_fail          :protected_forgivable_fail
,unprotected_forgivable_ok      :unprotected_forgivable_ok
,unprotected_forgivable_fail    :unprotected_forgivable_fail
,unprotected_severe_ok          :unprotected_severe_ok
,unprotected_severe_fail        :unprotected_severe_fail
})
#lift__forgivable : forgivable_fail --> forgivable_ok
    lift__forgivable = ({**{}
,protected_forgivable_ok        :protected_forgivable_ok
,protected_forgivable_fail      :protected_forgivable_ok
,protected_severe_ok            :protected_severe_ok
,protected_severe_fail          :protected_severe_fail
,unprotected_forgivable_ok      :unprotected_forgivable_ok
,unprotected_forgivable_fail    :unprotected_forgivable_ok
,unprotected_severe_ok          :unprotected_severe_ok
,unprotected_severe_fail        :unprotected_severe_fail
})
#lift__strict : protected_forgivable_fail --> forgivable_ok
    lift__strict = ({**{}
,protected_forgivable_ok        :protected_forgivable_ok
,protected_forgivable_fail      :protected_forgivable_ok
,protected_severe_ok            :protected_severe_ok
,protected_severe_fail          :protected_severe_fail
,unprotected_forgivable_ok      :unprotected_forgivable_ok
,unprotected_forgivable_fail    :unprotected_forgivable_fail
,unprotected_severe_ok          :unprotected_severe_ok
,unprotected_severe_fail        :unprotected_severe_fail
})
#...whole8header : unprotected_fail-->protected_fail
#whole8header : unprotected-->protected
    whole8header = ({**{}
,protected_forgivable_ok        :protected_forgivable_ok
,protected_forgivable_fail      :protected_forgivable_fail
,protected_severe_ok            :protected_severe_ok
,protected_severe_fail          :protected_severe_fail
,unprotected_forgivable_ok      :protected_forgivable_ok
,unprotected_forgivable_fail    :protected_forgivable_fail
,unprotected_severe_ok          :protected_severe_ok
,unprotected_severe_fail        :protected_severe_fail
})
#...empty8header : protected_fail --> unprotected_fail
#empty8header : protected --> unprotected
    empty8header = ({**{}
,protected_forgivable_ok        :unprotected_forgivable_ok
,protected_forgivable_fail      :unprotected_forgivable_fail
,protected_severe_ok            :unprotected_severe_ok
,protected_severe_fail          :unprotected_severe_fail
,unprotected_forgivable_ok      :unprotected_forgivable_ok
,unprotected_forgivable_fail    :unprotected_forgivable_fail
,unprotected_severe_ok          :unprotected_severe_ok
,unprotected_severe_fail        :unprotected_severe_fail
})


    ######################
    followed_by = lookahead # ++[ignore:=True]
    trial_and_error = protect_header
    protect_whole = composite__sconfigpack_(protect_header, whole8header)
    optional__forgivable = composite__sconfigpack_(lift__forgivable, protect_header) # >>> (spostprocess)
    optional__strict = composite__sconfigpack_(lift__strict, protect_header) # >>> (spostprocess)
    ######################
    _nms = {*locals()} -_nms
    ######################
#end-class _high_freq_sconfigpacks:
_high_freq_sconfigpacks.validate()
_b2nm2sym = _high_freq_sconfigpacks.register()
    #b2nm2sym
def _mk_info4mk_gi(may_ignore=None, to_lift=False, may_spostprocess6err=None, may_spostprocess6ok=None, to_invert_ok_err=False):
    return (may_ignore, to_lift, may_spostprocess6err, may_spostprocess6ok, to_invert_ok_err)
def _spostprocess6ok__4optional_after_lifted(lifted_oresult, /):
    payload4lifted_eresult = lifted_oresult
    (reply5child, maynotlow_sexconfig, ext_info8begin) = payload4lifted_eresult
    tmay_oresult = reply5child.eresult.to_tmay_right()
    return tmay_oresult
def _spostprocess6err__4optional_after_lifted(lifted_errmsg, /):
    payload4lifted_eresult = lifted_errmsg
    (reply5child, maynotlow_sexconfig, ext_info8begin) = payload4lifted_eresult
    errmsg = reply5child.errmsg
    return errmsg
default_info4mk_gi = _mk_info4mk_gi()
_nm2info = (dict(**{}
#{nm:may info4mk_gi/(may_ignore, to_lift, may_spostprocess6err, may_spostprocess6ok, to_invert_ok_err)}
#bug:,not_followed_by=_mk_info4mk_gi(True, to_invert_ok_err=True)
,not_followed_by=_mk_info4mk_gi(True, to_invert_ok_err=False)
    # !! already flip ok in sconfigpack
    #       to_invert_ok_err is part of postprocess
,followed_by=_mk_info4mk_gi(True)
,lift__forgivable=_mk_info4mk_gi(None, True)
,lift__strict=_mk_info4mk_gi(None, True)
,optional__forgivable=_mk_info4mk_gi(None, True, _spostprocess6err__4optional_after_lifted, _spostprocess6ok__4optional_after_lifted)
,optional__strict=_mk_info4mk_gi(None, True, _spostprocess6err__4optional_after_lifted, _spostprocess6ok__4optional_after_lifted)
,_echo_=None
,lookahead=None
,whole8header=None
,empty8header=None
,protect_header=None
,protect_whole=None
,trial_and_error=None
))
assert _nm2info.keys() == _high_freq_sconfigpacks._nms
def get_info_ex4high_freq_sconfigpack_(forbid_xxx_protected_ok, name4sconfigpack, /):
    'bool -> str -> info_ex/(sym, may info4mk_gi/(may_ignore, to_lift, may_spostprocess6err, may_spostprocess6ok, to_invert_ok_err))|^KeyError'
    sym = get_symbol8high_freq_sconfigpack_(forbid_xxx_protected_ok, name4sconfigpack)
        # ^KeyError
    may_info4mk_gi = _nm2info[name4sconfigpack]
    info_ex = (sym, may_info4mk_gi)
    return info_ex
def get_symbol8high_freq_sconfigpack_(forbid_xxx_protected_ok, name4sconfigpack, /):
    'bool -> str -> sym|^KeyError'
    check_type_is(bool, forbid_xxx_protected_ok)
    nm2sym = _b2nm2sym[forbid_xxx_protected_ok]
    return nm2sym[name4sconfigpack]

#name_set4high_freq_sconfigpack = frozenset(_high_freq_sconfigpacks._nms)
name_set4high_freq_sconfigpack = FrozenOrderedSet(sorted(_high_freq_sconfigpacks._nms))

__all__
from seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases import mk_gi4IRecognizerLLoo__5solo_rgnr_transform_cases_


from seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases import get_setting_, get_weak_symbolize_register4sexconfigpack_, is_good_sexconfigpack_

from seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases import CASES, name_set4high_freq_sconfigpack, get_info_ex4high_freq_sconfigpack_, default_info4mk_gi, get_symbol8high_freq_sconfigpack_

from seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases import *
