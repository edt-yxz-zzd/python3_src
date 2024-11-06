#__all__:goto
view ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/solo_rgnr_transform_cases.py
<<==:
mv -iv ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/solo_rgnr_transform_cases.py ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/solo_rgnr_transform_cases-old.py
py_tpl ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/solo_rgnr_transform_cases.py
e ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/solo_rgnr_transform_cases.py

#begin__doctest,end__doctest,doctest_cmd:goto
#simplified_typing:goto
#simplified_constraints:goto
#
#TODO:mk_gi:postcondition remove or forbid protected_ok(count under this condition)
#
#TODO:composite__exconfigpack_,连同unlocker_xxx也得变更
#???TODO:is_best_exconfigpack_ is wrong, change to is_true_best_exconfigpack_:正交=>只比较snapshot_xxx #unlocker_xxx属于外部可见属性,作为接口不可更改
#   不对！接口只有{case4reply5child:case4reply5self},(case4seekback)是冗余信息, (case4protection)只是实现细节
#   {(case4reply5child,case4reply5self):{case4protection}} #simplify:goto
#           #{uint%64:{uint%9}}
#           #{uint%64:uint%512}
#DONE:!!def composite exconfigpack!!
#   [(apply postprocessR exconfigpackR) == (apply postprocessB exconfigpackB) . (apply postprocessA exconfigpackA)]
#   (case4protection4composite, case4reply5grandchild/INPUT, case4reply5self/OUTPUT)
#   <<==:
#   (case4protection4self, case4reply5child/LINK, case4reply5self/OUTPUT)
#   (case4protection4child, case4reply5grandchild/INPUT, case4reply5child/LINK)
#   ==>>:
#   only case4protection4composite drew attention
#   [case4protection4composite === (case4protection4self . case4protection4child)]
#   ==>>:
#   # (Case4protection6unlocker, Case4protection6snapshot)
#   9*9==81
#   ==>>:
#   def composite__unlocker_xxx_
#   case (Case4protection6unlocker<self>, Case4protection6unlocker<child>) of:
#   (unlocker_hide, _) -> unlocker_hide
#   (unlocker_free, _) -> unlocker_free
#   (unlocker_into, unlocker_xxx) -> unlocker_xxx
#   2+3==5
#
#   3*3==9
#   ==>>:
#   def roughly_composite__snapshot_xxx_
#   case (Case4protection6snapshot<self>, Case4protection6snapshot<child>) of:
#   (snapshot_hide, _) -> snapshot_hide
#   (_, snapshot_hide) -> snapshot_hide
#   (snapshot_none, snapshot_xxx) -> snapshot_xxx
#   (snapshot_xxx, snapshot_none) -> snapshot_xxx
#   (snapshot_into, snapshot_into) -> snapshot_into
#
#   def roughly_composite__case4protection_ === (composite__unlocker_xxx_ +++ roughly_composite__snapshot_xxx_)
#   above() just ensure "ability" but maybe not "best"
#       DONE:use VM to emulate/simulate:validate____roughly_composite__case4protection_()
#
#
#TODO:list high freq exconfigpack and register them...
# * unlocker_hide+snapshot_hide:
#     * lookahead: ignore=inherit
#     * followed_by: ignore=True
#     * not_followed_by: ignore=True#the only one 'flip/invert_ok_err' instance
#     * [nonprimitive]:protect_whole === (protect_header <<< whole8header) =!= trial_and_error
#       #unprotected_fail-->protected_forgivable_fail
# * unlocker_into+snapshot_into:
#     * protect_header === trial_and_error
#       #protected_fail-->protected_forgivable_fail
#     * [nonprimitive]:optional__forgivable === (postprocess <<< lift__forgivable <<< protect_header)
#       #(protected_fail&unprotected_forgivable_fail)-->forgivable_ok
#       # lift (tmay oresult) as new-oresult
#     * [nonprimitive]:optional__strict === (postprocess <<< lift__strict <<< protect_header)
#       #protected_fail-->forgivable_ok
#       #   unprotected_forgivable_fail leaves
#       # lift (tmay oresult) as new-oresult
# * unlocker_into+snapshot_none:
#     * lift__forgivable#no_seekback
#       #forgivable_fail-->forgivable_ok
#       #lift (eresult, ...) as new-oresult
#     * lift__strict#no_seekback
#       #protected_forgivable_fail-->forgivable_ok
#       #lift (eresult, ...) as new-oresult
# * unlocker_hide+snapshot_none:
#     * whole8header:
#       #unprotected_forgivable_fail-->protected_forgivable_fail
#       #unprotected_severe_fail-->protected_severe_fail
#       combine:[protect_whole === (protect_header <<< whole8header)]
#       combine:(optional <<< whole8header)
# * unlocker_free+snapshot_none:
#     * empty8header # to force severe_fail
#       #forgivable_fail-->unprotected_forgivable_fail
#       #severe_fail-->unprotected_severe_fail

#DONE:new_constraint4seekback:to_seekback=>case4reply5child.is_severe()&&case4reply5self.is_forgivable()
#DONE:new_constraint4seekback:no_seekback=>(case4reply5child.is_severe()==case4reply5self.is_severe())
#   see:below label 『news__constraint4xx_seekback』
#   bug-fixed:cancel:『constraint4seekback:to_seekback <<== [child:*_forgivable_*]』
#   now:case4seekback is redundant#see:determine_case4seekback_
#   update:is_good_exconfig_()
#   bug:len(sorted_all_good_exconfigs) == 164 <-- 245 #before fix bug___case4reply5child_has_no_severe
#   len(sorted_all_good_exconfigs) ==  245 #after fix bug___case4reply5child_has_no_severe
#DONE:new:constraint@pack:not snapshot_none->at_least1:to_seekback@severe
#   update:is_good_exconfigpack_()
#   update:iter_all_good_exconfigpacks_(): _count_only_=True: prod(W)-prod(W-to_seekback) easy...
#   _is_required_item_4new_constraint4configpack__if_not_snapshot_none
#
#TODO:???DONE???:useless:new:constraint:unlocker_* -> ?snapshot_*?
#   不对！接口只有{case4reply5child:case4reply5self},(case4seekback)是冗余信息, (case4protection)只是实现细节
#   no:new:constraint:unlocker_free->snapshot_* #to_seekback as forgivable
#   no:new:constraint:unlocker_into->snapshot_* #to_seekback as forgivable
#   no:new:constraint:unlocker_hide->snapshot_* #to_seekback as forgivable
#   两者正交/无关:unlocker_* 声明头部; snapshot_* 用于调头
r'''[[[
e ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/solo_rgnr_transform_cases.py
see:
    view ../../python3_src/seed/recognize/recognizer_LLoo__ver2_/IRecognizerLLoo.py
        [:lookahead__vs__try__vs__optional__vs__lift]:goto
        [:protected_fail__vs__forgivable_fail__vs__severe_fail]:goto

seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases
py -m nn_ns.app.debug_cmd   seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases -x
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases:__doc__ -ht
py -m nn_ns.app.doctest_cmd seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases:__doc__ -ht   >  /sdcard/0my_files/tmp/0tmp
view /sdcard/0my_files/tmp/0tmp


[[
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

constraint4no_seekback
[{<not seekback monotonic_idx8begin>}] ->:
    #require one of:
    Nothing
    # * [child:*_*_*]
    news__constraint4xx_seekback:
    * [child:*_severe_*][self:*_severe_*]
    * [child:*_forgivable_*][self:*_forgivable_*]

constraint4seekback
[{<seekback monotonic_idx8begin>}] ->:
    #require one of:
    #news__constraint4xx_seekback==>>cancel:* [child:*_forgivable_*]
        #bug-fixed
    * [self:snapshot into][child:protected_severe_*]
    * [self:snapshot hide]
    news__constraint4xx_seekback:
    #and require one of:
    * [child:*_severe_*][self:*_forgivable_*]
#DONE:new_constraint4seekback:to_seekback=>case4reply5child.is_severe()&&case4reply5self.is_forgivable()
#DONE:new_constraint4seekback:no_seekback=>(case4reply5child.is_severe()==case4reply5self.is_severe())

######################
######################
constraint4severe_fail
[...-->[self:*_severe_fail]] ->:
    #require one of:
    * {<not seekback monotonic_idx8begin>}[child:*_severe_*]
    #avoid eof
constraint4severe_ok
[...-->[self:*_severe_ok]] ->:
    #require one of:
    * {<not seekback monotonic_idx8begin>}[child:*_severe_ok]
    #no:* {<not seekback monotonic_idx8begin>}[child:*_severe_fail]
        !! *_severe_fail .monotonic_idx8end unpredictable
    #avoid eof

constraint4forgivable
[...-->[self:*_forgivable_*]] ->:
    #require one of:
    * {<seekback monotonic_idx8begin>}
    news__constraint4xx_seekback:
    * {<not seekback monotonic_idx8begin>}[child:*_forgivable_*]

[...-->[self:unprotected_*_*]] ->:
    #require one of:
    Nothing
    # * [child:*_*_*]

constraint4protected
[...-->[self:protected_*_*]] ->:
    #require one of:
    * [self:unlocker_hide]
    * [self:unlocker_into][child:protected_*_*]

######################
######################
接口只有{case4reply5child:case4reply5self},(case4seekback)是冗余信息, (case4protection)只是实现细节
{(case4reply5child,case4reply5self):{case4protection}}
    #{uint%64:{uint%9}}
    #{uint%64:uint%512}
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
extra:
forbid:[child.forgivable-->self.severe]
    !! eof
    4:num_output_cases-4
    clousure_under_composition:[self.severe-->child.severe]
forbid:[child.severe_fail-->self.severe_ok]
    !! *_severe_fail .monotonic_idx8end unpredictable
    2:num_output_cases-2
    clousure_under_composition:[self.severe_ok-->child.severe_ok]
#####
optional:[forbid____protected_ok:=True]:
forbid:[[child.protected_ok]or[self.protected_ok]]
    clousure_under_composition:[[child.protected_ok]or[self.protected_ok]]

######################
#simplified_typing:here

sconfig := (case4reply5child, case4reply5self)
cache4sconfig := (min_unlocker_xxx, min_snapshot_xxx, case4seekback)
    # NOTE:but:[min_xxx_xxx.value is max one], since def@class in reversed order
sexconfig := (cache4sconfig, sconfig)
sconfigpack := full-{case4reply5child:case4reply5self}
sexconfigpack := (case4protection8summary, sconfigpack)
    where:case4protection8summary.value == (max min_unlocker_xxx, max min_snapshot_xxx)
    # NOTE:but:[min_xxx_xxx.value is max one], since def@class in reversed order

########counting<sconfig>:
echo $[8+8+8+8 + 8+8+8+8]
64
    == total<exconfig>/len(Case4protection6snapshot)/len(Case4seekback)
        == 1152/9/2
echo $[4+4+4+4 + 6+6+8+8]
44
    4:num_output_cases-4
    2:num_output_cases-2
    == total<sconfig>
    == total<sexconfig>
    vs: [245==total<good_exconfig>]

[forbid____protected_ok:=True]:
echo $[0+3+3+3 + 5+5+0+6]
25
    == total<sconfig,+forbid____protected_ok>
    == total<sexconfig,+forbid____protected_ok>
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
    == total<best_exconfigpack>
        #也就是简化前的best_exconfigpack总数#calc_total_all_best_exconfigpacks_via_iter_

[forbid____protected_ok:=True]:
echo $[1*3*3*3 * 5*5*1*6]
4050
    #『1』stands for 『deleted』
    == total<sconfigpack,+forbid____protected_ok>
    == total<sexconfigpack,+forbid____protected_ok>
    == total<best_exconfigpack,+forbid____protected_ok>
        #也就是简化前的best_exconfigpack总数#calc_total_all_best_exconfigpacks_via_iter_(...,+forbid____protected_ok)
######################
######################
]]


bad_count=>below count changed:

py_adhoc_call     { +lineno } seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases ,iter_all_best_exconfigpacks_
py_adhoc_call     seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases @calc_total_all_best_exconfigpacks_via_iter_ -to_show_countings
??? #best&&include:protected_ok
    #old:589824@{before-using-bad_count}
    #   new one is same
    #old:589824@{before:new constraint4seekback}
    #old:65536 #before fix bug___case4reply5child_has_no_severe
    #   #==2**16???why???fortuity???
    #
    #now:?589824?likely
py_adhoc_call     seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases @calc_total_all_best_exconfigpacks_via_iter_ -to_show_countings +forbid____protected_ok
4050 #best&&exclude:protected_ok
    #old:4050@{before-using-bad_count}
    #   new one is same
    #old:4050@{before:new constraint4seekback}
    #old:729 #before fix bug___case4reply5child_has_no_severe
    #now:4050
py_adhoc_call     seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases @pprint__pformat_d3._init4iter_all_good_exconfigpacks_ =None  +forbid____protected_ok +to_name_ver

py_adhoc_call     { +lineno } seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases ,iter_all_good_exconfigpacks_
py_adhoc_call     seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases @calc_total_all_good_exconfigpacks_via_iter_
716352 #good&&include:protected_ok
    #old:751296@{before-using-bad_count}
    #   new one is smaller
    #old:716352@{before:new constraint4seekback}
    #old:69888 #before fix bug___case4reply5child_has_no_severe
    #now:716352
py_adhoc_call     seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases @calc_total_all_good_exconfigpacks_via_iter_ +forbid____protected_ok
5648 #good&&exclude:protected_ok
    #old:6424@{before-using-bad_count}
    #   new one is smaller
    #old:5648@{before:new constraint4seekback}
    #old:937 #before fix bug___case4reply5child_has_no_severe
    #now:5648

py_adhoc_call     seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases @calc_total_all_good_exconfigs_via_iter_ -to_show_countings
245 #include:protected_ok
    #old:245@{before:new constraint4seekback}
    #old:164 #before fix bug___case4reply5child_has_no_severe
    #now:245
py_adhoc_call     seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases @calc_total_all_good_exconfigs_via_iter_ -to_show_countings +forbid____protected_ok
144 #exclude:protected_ok
    #old:144@{before:new constraint4seekback}
    #old:96 #before fix bug___case4reply5child_has_no_severe
    #now:144
py_adhoc_call     seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases @calc_total_all_possible_exconfigs_via_iter_ +to_show_countings
1152
    # 9*8*2*8==1152

py_adhoc_call       { +lineno } seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases ,str.sorted_all_good_exconfigs_ +as_name '%seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases@this'  =this.unlocker_hide__snapshot_hide
py_adhoc_call       { +lineno } seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases @calc_total_all_good_exconfigs_via_iter_ '%seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases@this'  =this.unlocker_hide__snapshot_hide
44 #after fix bug___case4reply5child_has_no_severe

py_adhoc_call     seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases @validate____roughly_composite__case4protection_ -forbid____protected_ok
    ok #after fix bug___case4reply5child_has_no_severe

py_adhoc_call     seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases @validate_composite__exconfigpack__6all_best_exconfigpacks -forbid____protected_ok +verbose


begin__doctest
[[
py_adhoc_call       { +lineno } seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases ,str.sorted_all_good_exconfigs_ +as_name

bug-fixed:reply5child miss:*_severe_*
    bug___case4reply5child_has_no_severe
>>> for i, s in enumerate(sorted_all_good_exconfigs_(None, forbid____protected_ok=False, as_name=True), 1):print(f'{i:0>3}:{s}')



]]



>>> _pcmp_le_table4Case4protection__name_ver

True

#>>> from seed.helper.stable_repr import stable_repr
#>>> stable_repr(_case4protection_Z_case4reply5child_Z_pairs_4_6case4seekback_case4reply5self9__name_ver)
#[[[
:s/}, /}\r,/g
:.,.+8s/: {/\r  :{/g
:.,.+18s/], /]\r  ,/g
:.,.+64s/: \[/\r    :[/g
:.,.+118s/]}/]\r  }/g
>>> _case4protection_Z_case4reply5child_Z_pairs_4_6case4seekback_case4reply5self9__name_ver

True


























(_i2case4protection, _j2case4reply, _b2case4seekback, _jp2pair, _pair2jp)
    #tabulation ver of _case4protection_Z_case4reply5child_Z_pairs_4_6case4seekback_case4reply5self9
    [exconfigpack ~=~ (i, full-{j:jp})]
    [exconfigpack ~=~ (i, full-{j:k})]
    [i :: uint%9]
    [j :: uint%8]
    [exconfigpack ~=~ (i/uint%9, [jp%16]{len=8})]
    [exconfigpack ~=~ (i/uint%9, [k{<8}]{len=8})]
    [case4protection := _i2case4protection[i]]
    [case4reply := _j2case4reply[j]]
    [i := case4protection._idx_]
    [j := case4reply5child._idx_]
    [0 <= k < _max_sz == 8]
    [jp <- _used_jp_set == {0, 1, 4, 5, 10, 11, 14, 15}]
    [jp := i2j2k2jp[i][j][k]]
    [(case4seekback, case4reply5self) := _jp2pair[jp]]

    [jg :: uint%245]
    [jg2good_exconfig := sorted_all_good_exconfigs]


_i2case4protection, _j2case4reply, _b2case4seekback)
(_jp2pair__name_ver, _pair2jp__name_ver)
(_i2j2k2jg, _i2j2k2jp, _i2j2sz, _max_sz, _used_jp_set)
>>> _list2name_ver(_i2case4protection)
['unlocker_hide__snapshot_hide', 'unlocker_hide__snapshot_into', 'unlocker_hide__snapshot_none', 'unlocker_into__snapshot_hide', 'unlocker_into__snapshot_into', 'unlocker_into__snapshot_none', 'unlocker_free__snapshot_hide', 'unlocker_free__snapshot_into', 'unlocker_free__snapshot_none']
>>> _list2name_ver(_j2case4reply)
['protected_forgivable_ok', 'protected_forgivable_fail', 'protected_severe_ok', 'protected_severe_fail', 'unprotected_forgivable_ok', 'unprotected_forgivable_fail', 'unprotected_severe_ok', 'unprotected_severe_fail']
>>> _list2name_ver(_b2case4seekback)
['to_seekback', 'no_seekback']
>>> _jp2pair__name_ver == (
... ['to_seekback.protected_forgivable_ok'
... ,'to_seekback.protected_forgivable_fail'
... ,'to_seekback.protected_severe_ok'
... ,'to_seekback.protected_severe_fail'
... ,'to_seekback.unprotected_forgivable_ok'
... ,'to_seekback.unprotected_forgivable_fail'
... ,'to_seekback.unprotected_severe_ok'
... ,'to_seekback.unprotected_severe_fail'
... ,'no_seekback.protected_forgivable_ok'
... ,'no_seekback.protected_forgivable_fail'
... ,'no_seekback.protected_severe_ok'
... ,'no_seekback.protected_severe_fail'
... ,'no_seekback.unprotected_forgivable_ok'
... ,'no_seekback.unprotected_forgivable_fail'
... ,'no_seekback.unprotected_severe_ok'
... ,'no_seekback.unprotected_severe_fail'
... ])
True
>>> _pair2jp__name_ver == (
... {'to_seekback.protected_forgivable_ok': 0
... ,'to_seekback.protected_forgivable_fail': 1
... ,'to_seekback.protected_severe_ok': 2
... ,'to_seekback.protected_severe_fail': 3
... ,'to_seekback.unprotected_forgivable_ok': 4
... ,'to_seekback.unprotected_forgivable_fail': 5
... ,'to_seekback.unprotected_severe_ok': 6
... ,'to_seekback.unprotected_severe_fail': 7
... ,'no_seekback.protected_forgivable_ok': 8
... ,'no_seekback.protected_forgivable_fail': 9
... ,'no_seekback.protected_severe_ok': 10
... ,'no_seekback.protected_severe_fail': 11
... ,'no_seekback.unprotected_forgivable_ok': 12
... ,'no_seekback.unprotected_forgivable_fail': 13
... ,'no_seekback.unprotected_severe_ok': 14
... ,'no_seekback.unprotected_severe_fail': 15
... })
True

#[[[[
:s/]], /]]\r,/g
>>> _i2j2k2jg

True

#[[[[
:s/]], /]]\r,/g
>>> _i2j2k2jp

True

>>> _i2j2sz

>>> _max_sz # [0 <= k < _max_sz]

>>> _used_jp_set  # [jp==j4pair <- _used_jp_set]

True
>>> len(_used_jp_set)


end__doctest
#]]]'''
__all__ = r'''
mk_gi4IRecognizerLLoo__5solo_rgnr_transform_cases_
    weak_symbolize_register4exconfigpack
    weak_symbolize_register4exconfigpack_____forbid____protected_ok
        convert_exconfigpack2uint_ver
        convert_exconfigpack5uint_ver
jg2good_exconfig  sorted_all_good_exconfigs

calc_total_all_best_exconfigpacks_via_iter_
    iter_all_best_exconfigpacks_
        is_best_exconfigpack_

calc_total_all_good_exconfigpacks_via_iter_
    iter_all_good_exconfigpacks_
        is_good_exconfigpack_
        iter_all_good_exconfigs_
            is_good_exconfig_

calc_total_all_good_exconfigs_via_iter_
        iter_all_good_exconfigs_

sorted_all_good_exconfigs_










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


jg2good_exconfig  sorted_all_good_exconfigs
    sorted_all_good_exconfigs_
        exconfig2str
            config2str
calc_total__via_iter_
calc_total_all_good_exconfigs_via_iter_
        iter_all_good_exconfigs_
calc_total_all_good_exconfigpacks_via_iter_
    iter_all_good_exconfigpacks_
        is_good_exconfigpack_
        iter_all_good_exconfigs_
            is_good_exconfig_
            iter_all_possible_exconfigs_
                iter_all_possible_cases4protection_
                iter_all_possible_configs_
calc_total_all_possible_exconfigs_via_iter_
                iter_all_possible_configs_

calc_total_all_best_exconfigpacks_via_iter_
    iter_all_best_exconfigpacks_
        is_best_exconfigpack_
tail_

mk_gi4IRecognizerLLoo__5solo_rgnr_transform_cases_
    mk_case4reply5xxx
        mk_case4reply5child
        mk_case4reply5self
    weak_symbolize_register4exconfigpack
    weak_symbolize_register4exconfigpack_____forbid____protected_ok
        convert_exconfigpack2uint_ver
        convert_exconfigpack5uint_ver
            exconfigpack5or_uint_ver_




determine_case4seekback_

composite__exconfigpack_
    composite__configpack_
    roughly_composite__exconfigpack_
        roughly_composite__exconfig_
            roughly_composite__case4protection_
                composite__unlocker_xxx_
                roughly_composite__snapshot_xxx_



validate____roughly_composite__case4protection_
validate_composite__exconfigpack__6all_best_exconfigpacks



'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
from seed.types.stream.IRecoverableInputStream import dummy_unlocker, DetectionUnlocker#detection_unlocker

from enum import Enum, auto
from itertools import product# combinations
from functools import partial
from math import prod

from seed.types.mapping.symbolize import WeakSymbolizeRegister, ISymbolizeRegister__subset# PersistentSymbolizeRegister
    # to symbolize exconfigpack

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
class Case4reply6xforgivable(_Lt, Enum):
    forgivable  = auto()
    severe      = auto()
class Case4reply6xok(_Lt, Enum):
    ok          = auto()
    fail        = auto()
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





class Case4protection6snapshot(_Lt, Enum):
    snapshot_hide = auto()
    snapshot_into = auto()
    snapshot_none = auto()
class Case4protection6unlocker(_Lt, Enum):
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
        if T.__module__ == __name__:
            nm2x[nm] = x
    return NamespaceForbidModify(nm2x)
_cases = _collect_enums()


#detection_unlocker
def iter_all_possible_cases4protection_():
    '-> Iter case4protection'
    yield from Case4protection
##def iter_all_possible_configs6protection_(case4protection, /):
##    '-> Iter config<case4protection>'
def iter_all_possible_configs_():
    '-> Iter config/(case4reply5child, case4seekback, case4reply5self)'
    for case4reply5child in Case4reply:
        for case4seekback in Case4seekback:
            for case4reply5self in Case4reply:
                # 8*2*8==128
                yield (case4reply5child, case4seekback, case4reply5self)
def config2str(config, /):
    (case4reply5child, case4seekback, case4reply5self) = config
    return f'{case4reply5child.name}.{case4seekback.name}.{case4reply5self.name}'
def exconfig2str(exconfig, /):
    (case4protection, config) = exconfig
    return f'{case4protection.name}.{config2str(config)}'
def sorted_all_good_exconfigs_(may_case4protection:None, /, *, forbid____protected_ok:False, as_name=False):
    '-> sorted [exconfig{good}]'
    it = iter_all_good_exconfigs_(may_case4protection, forbid____protected_ok=forbid____protected_ok)
    ls = sorted(it)
    if as_name:
        ls = [*map(exconfig2str, ls)]
    return ls
def iter_all_good_exconfigs_(may_case4protection:None, /, *, forbid____protected_ok:False):
    '-> Iter exconfig{good}'
    good_exconfigs = filter(partial(is_good_exconfig_, forbid____protected_ok=forbid____protected_ok), iter_all_possible_exconfigs_(may_case4protection))
    return good_exconfigs
def iter_all_possible_exconfigs_(may_case4protection:None, /):
    '-> Iter exconfig/(case4protection, config)'
    if may_case4protection is None:
        it = iter_all_possible_cases4protection_()
    else:
        case4protection = may_case4protection
        check_type_is(Case4protection, case4protection)
        it = iter([case4protection])
    it
    for case4protection in it:
        for config in iter_all_possible_configs_():
            # 9*128==1152
            yield (case4protection, config)
def tail_(ls, /):
    return ls[1:]
def calc_total__via_iter_(iterable, /, *, to_show_countings:False):
    'Iter x -> num_xs'
    iterable = iter(iterable)
    sz = 0
    it = enumerate(iterable, 1)
    it = map(fst, it)
    if to_show_countings:
        print(sz)
        def iprint(sz, /):
            print(sz)
            return sz
        it = map(iprint, it)
    for sz in it:
        pass
    return sz
def calc_total_all_possible_exconfigs_via_iter_(may_case4protection=None, /, *, to_show_countings=False):
    '-> num_possible_exconfigs'
    it = iter_all_possible_exconfigs_(may_case4protection)
    return calc_total__via_iter_(it, to_show_countings=to_show_countings)
def calc_total_all_good_exconfigs_via_iter_(may_case4protection=None, /, *, to_show_countings=False, forbid____protected_ok=False):
    '-> num_good_exconfigs'
    it = iter_all_good_exconfigs_(may_case4protection, forbid____protected_ok=forbid____protected_ok)
    return calc_total__via_iter_(it, to_show_countings=to_show_countings)
def calc_total_all_best_exconfigpacks_via_iter_(may_case4protection=None, /, *, to_show_countings=False, forbid____protected_ok=False):
    '-> num_best_exconfigpacks'
    it = iter_all_best_exconfigpacks_(may_case4protection, forbid____protected_ok=forbid____protected_ok)
    return calc_total__via_iter_(it, to_show_countings=to_show_countings)
def calc_total_all_good_exconfigpacks_via_iter_(may_case4protection=None, /, *, forbid____protected_ok=False):
    '-> num_good_exconfigpacks'
    it = iter_all_good_exconfigpacks_(may_case4protection, _count_only_=True, _good_vs_best_=False, forbid____protected_ok=forbid____protected_ok)
    return sum(it)
    ##it = iter_all_good_exconfigpacks_(may_case4protection, _count_only_=False, _good_vs_best_=False, forbid____protected_ok=forbid____protected_ok)
    ##return calc_total__via_iter_(it)
def iter_all_best_exconfigpacks_(may_case4protection:None, /, *, forbid____protected_ok:False):
    return iter_all_good_exconfigpacks_(may_case4protection, _count_only_=False, _good_vs_best_=True, forbid____protected_ok=forbid____protected_ok)
def _get_pseudo_Case4reply(forbid____protected_ok, /):
    if forbid____protected_ok:
        #bug:fixed:
        _Case4reply = _Case4reply__if____forbid____protected_ok
    else:
        _Case4reply = _Case4reply__if____allow_____protected_ok
    _Case4reply
    return _Case4reply
def iter_all_good_exconfigpacks_(may_case4protection:None, /, *, _count_only_:False, _good_vs_best_:False, forbid____protected_ok:False):
    '-> Iter exconfigpack{good} if not _count_only_ else Iter count/uint'
    if _count_only_ and _good_vs_best_:raise NotImplementedError
    pn2r5c2sb_r5s_pairs = _init4iter_all_good_exconfigpacks_(may_case4protection, forbid____protected_ok=forbid____protected_ok)
        # :: {case4protection:{case4reply5child:[(case4seekback, case4reply5self)]}}
    _Case4reply = _get_pseudo_Case4reply(forbid____protected_ok)
    if 0b0000:
        rs = sorted({r for r2x in pn2r5c2sb_r5s_pairs.values() for r in r2x})
        print_err('mid_keys@pn2r5c2sb_r5s_pairs', len(rs), ','.join(_list2name_ver(rs)))
        #
        #only 4@(2*2*2==8)
        #   protected_severe_ok,protected_severe_fail,unprotected_severe_ok,unprotected_severe_fail
        #==>>: no:*_forgivable_*
        #

    for case4protection, r5c2sb_r5s_pairs in pn2r5c2sb_r5s_pairs.items():
        #if 0b0001:print_err('r5c2sb_r5s_pairs', len(r5c2sb_r5s_pairs), ','.join(_list2name_ver(sorted(r5c2sb_r5s_pairs.keys()))))
        if not len(r5c2sb_r5s_pairs) == len(_Case4reply):
            continue
        ps = [*r5c2sb_r5s_pairs.items()]
        k_vs_pairs = ps
        ks = [*map(fst, k_vs_pairs)]
            # :: [case4reply5child]
        vss = [*map(snd, k_vs_pairs)]
            # :: [[(case4seekback, case4reply5self)]]
        szs = [*map(len, vss)]
        full_count = prod(szs)
        ######################
        #DONE:new:constraint@pack:not snapshot_none->at_least1:to_seekback@severe
        if not case4protection.is_snapshot_none():
            f = _is_required_item_4new_constraint4configpack__if_not_snapshot_none
            _vss = [[v for v in vs if not f((k,v))] for k, vs in k_vs_pairs]
            _szs = [*map(len, _vss)]
            bad_count = prod(_szs)
        else:
            bad_count = 0
        bad_count
        count = full_count -bad_count
        ######################
        if _count_only_:
            assert not _good_vs_best_
            yield count
            continue
        _sz = 0
        #bug:for _sz, vs in enumerate(product(*vss), 1):
        for vs in product(*vss):
            k2v = dict(zip(ks, vs))
            configpack = k2v
            exconfigpack = (case4protection, configpack)
            if not is_good_exconfigpack_(exconfigpack, forbid____protected_ok=forbid____protected_ok):
                continue
            _sz += 1 # include not best
            if _good_vs_best_:
                #best
                if not is_best_exconfigpack_(exconfigpack, forbid____protected_ok=forbid____protected_ok):
                    continue
            yield exconfigpack
        assert _sz == count, (k_vs_pairs, case4protection, (_sz, count, full_count, bad_count))
    return
def _init4iter_all_good_exconfigpacks_(may_case4protection:None, /, *, forbid____protected_ok:False, to_name_ver=False):
    #good_exconfigs = iter_all_good_exconfigs_(may_case4protection, forbid____protected_ok=forbid____protected_ok)
    good_exconfigs = sorted_all_good_exconfigs_(may_case4protection, forbid____protected_ok=forbid____protected_ok)
        # :: [exconfig]
        # :: [(case4protection, config)]
    case4protectionZconfigs = xs_to_k2vs_(fst, snd, good_exconfigs)
        # :: {case4protection:[config]}
        # :: {case4protection:[(case4reply5child, case4seekback, case4reply5self)]}
    777;    del good_exconfigs
    pn2r5c2sb_r5s_pairs = case4protectionZcase4reply5childZcase4seekback_case4reply5self_pairs = {case4protection:xs_to_k2vs_(fst, tail_, configs) for case4protection, configs in case4protectionZconfigs.items()}
        # :: {case4protection:{case4reply5child:[(case4seekback, case4reply5self)]}}
    if to_name_ver:
        return _name_ver5c2c2ls4cc(pn2r5c2sb_r5s_pairs)
    return pn2r5c2sb_r5s_pairs

def is_best_exconfigpack_(exconfigpack, /, *, forbid____protected_ok:False):
    'exconfigpack -> best/bool #no smaller case4protection satisfied'
    if not is_good_exconfigpack_(exconfigpack, forbid____protected_ok=forbid____protected_ok):
        return False
    (case4protection, configpack) = exconfigpack
    return not any(is_good_exconfigpack_((smaller, configpack), forbid____protected_ok=forbid____protected_ok) for smaller in _pcmp_lt_table4Case4protection[case4protection])
def is_good_exconfigpack_(exconfigpack, /, *, forbid____protected_ok:False):
    'exconfigpack/(case4protection, configpack/full-{case4reply5child:(case4seekback, case4reply5self)}) -> good/bool'
    (case4protection, configpack) = exconfigpack
    _Case4reply = _get_pseudo_Case4reply(forbid____protected_ok)
    if not configpack.keys() == _Case4reply:raise Exception(configpack.keys(), _Case4reply)
    for case4reply5child, (case4seekback, case4reply5self) in configpack.items():
        config = (case4reply5child, case4seekback, case4reply5self)
        exconfig = (case4protection, config)
        if not is_good_exconfig_(exconfig, forbid____protected_ok=forbid____protected_ok):
            return False
    ######################
    #DONE:new:constraint@pack:not snapshot_none->at_least1:to_seekback@severe
    if not case4protection.is_snapshot_none():
        if not any(map(_is_required_item_4new_constraint4configpack__if_not_snapshot_none, configpack.items())):
            return False
    ######################
    return True
def _is_required_item_4new_constraint4configpack__if_not_snapshot_none(item, /):
    #DONE:new:constraint@pack:not snapshot_none->at_least1:to_seekback@severe
    (case4reply5child, (case4seekback, case4reply5self)) = item
    return case4seekback == to_seekback and case4reply5child.is_severe()
def is_good_exconfig_(exconfig, /, *, forbid____protected_ok:False):
    'exconfig -> bool'
    (case4protection, config) = exconfig
    (case4reply5child, case4seekback, case4reply5self) = config
    ######################
    #forbid____protected_ok
    ######################
    #constraint4seekback
    #constraint4no_seekback
    #constraint4severe_fail
    #constraint4severe_ok
    #constraint4forgivable
    #constraint4protected
    ######################

    ######################
    #forbid____protected_ok
    ######################
    if forbid____protected_ok:
        if case4reply5self.is_protected_ok():
            return False
        ########
        if case4reply5child.is_protected_ok():
            return False

    ######################
    #constraint4seekback
    ######################
    if case4seekback == to_seekback:
        if case4protection.is_snapshot_into() and case4reply5child.is_protected():#neednot『 and case4reply5child.is_severe():』
            # [self:snapshot into][child:protected_severe_*]
            pass
        elif case4protection.is_snapshot_hide():
            # [self:snapshot hide]
            pass
        #cancel:elif case4reply5child.is_forgivable():
            # news__constraint4xx_seekback==>>cancel:[child:*_forgivable_*]
            pass
        else:
            return False
        #news__constraint4xx_seekback:
        ########
        #and require one of:
        if case4reply5child.is_severe() and case4reply5self.is_forgivable():
            # * [child:*_severe_*][self:*_forgivable_*]
            pass
        else:
            return False
    ######################
    #see:below:new_constraint4seekback
    #   --> now:news__constraint4xx_seekback
    ######################

    ######################
    #constraint4no_seekback
    ######################
    #news__constraint4xx_seekback:
    if case4seekback == no_seekback:
        if case4reply5child.is_severe() and case4reply5self.is_severe():
            # * [child:*_severe_*][self:*_severe_*]
            pass
        #bug:if case4reply5child.is_forgivable() and case4reply5self.is_forgivable():
        #   fixed:『if』-->『elif』
        #   named:bug___case4reply5child_has_no_severe
        elif case4reply5child.is_forgivable() and case4reply5self.is_forgivable():
            # * [child:*_forgivable_*][self:*_forgivable_*]
            pass
        else:
            return False

    ######################
    #constraint4severe_fail
    ######################
    if case4reply5self.is_severe_fail():
        if case4seekback == no_seekback and case4reply5child.is_severe():
            # {<not seekback monotonic_idx8begin>}[child:*_severe_*]
            pass
        else:
            return False

    ######################
    #constraint4severe_ok
    ######################
    if case4reply5self.is_severe_ok():
        if case4seekback == no_seekback and case4reply5child.is_severe_ok():
            # {<not seekback monotonic_idx8begin>}[child:*_severe_ok]
            pass
        else:
            return False

    ######################
    #constraint4forgivable
    ######################
    if case4reply5self.is_forgivable():
        if case4seekback == to_seekback:
            # {<seekback monotonic_idx8begin>}
            pass
        elif case4reply5child.is_forgivable():
            # news__constraint4xx_seekback:
            # * {<not seekback monotonic_idx8begin>}[child:*_forgivable_*]
            pass
        else:
            return False


    ######################
    #constraint4protected
    ######################
    if case4reply5self.is_protected():
        if case4protection.is_unlocker_hide():
            # [self:unlocker_hide]
            pass
        elif case4protection.is_unlocker_into() and case4reply5child.is_protected():
            # [self:unlocker_into][child:protected_*_*]
            pass
        else:
            return False
    ######################


    return True

    ######################
    #see:above:constraint4seekback
    ######################
    #DONE:new_constraint4seekback:to_seekback=>case4reply5child.is_severe()&&case4reply5self.is_forgivable()
    #DONE:new_constraint4seekback:no_seekback=>(case4reply5child.is_severe()==case4reply5self.is_severe())
    ######################
    if case4seekback == to_seekback:
        if not (case4reply5child.is_severe() and case4reply5self.is_forgivable()):
            if 0b0001: print_err('@is_good_exconfig_:cccccc:to_seekback', exconfig2str(exconfig))
            return False
    else:
        #no_seekback
        #if 0b0001: print_err('@is_good_exconfig_:gggggg:no_seekback', exconfig2str(exconfig))
        if not (case4reply5child.get_xforgivable() == case4reply5self.get_xforgivable()):
            if 0b0001: print_err('@is_good_exconfig_:bbbbbb:no_seekback', exconfig2str(exconfig))
            raise 000-'???no one reach here???'
            return False
    ######################
    assert case4reply5child.is_severe() or case4reply5self.is_forgivable()
    assert not (case4reply5child.is_forgivable() or case4reply5self.is_severe())
    ######################
    return True
    ######################
    #bug:
    if not (case4seekback == to_seekback) is (case4reply5child.is_severe() and case4reply5self.is_forgivable()):
        if 0b0001: print_err('@is_good_exconfig_:aaaaaa', exconfig2str(exconfig))
        raise 000-'bug'
        return False
    ######################
    return True


sorted_all_good_exconfigs = tuple(sorted_all_good_exconfigs_(None, forbid____protected_ok=False))
assert len(sorted_all_good_exconfigs) == 245, len(sorted_all_good_exconfigs)
jg2good_exconfig = sorted_all_good_exconfigs




_case4protection_Z_case4reply5child_Z_pairs_4_6case4seekback_case4reply5self9 = _init4iter_all_good_exconfigpacks_(None, forbid____protected_ok=False)#may_case4protection
        # :: {case4protection:{case4reply5child:[(case4seekback, case4reply5self)]}}
def _name_ver5c2c2ls4cc(c2c2ls4cc, /):
    return {c0.name:{c1.name:[(c2.name, c3.name) for c2, c3 in ls4cc] for c1, ls4cc in c2ls4cc.items()} for c0, c2ls4cc in c2c2ls4cc.items()}
_case4protection_Z_case4reply5child_Z_pairs_4_6case4seekback_case4reply5self9__name_ver = _name_ver5c2c2ls4cc(_case4protection_Z_case4reply5child_Z_pairs_4_6case4seekback_case4reply5self9)
#if 0b0001:print_err('_case4protection_Z_case4reply5child_Z_pairs_4_6case4seekback_case4reply5self9__name_ver', _case4protection_Z_case4reply5child_Z_pairs_4_6case4seekback_case4reply5self9__name_ver)

def _tabulate_1():
    for i, c in enumerate(i2case4protection:=sorted(Case4protection)):
        c._idx_ = i
    for i, c in enumerate(j2case4reply:=sorted(Case4reply)):
        c._idx_ = i
    for i, c in enumerate(b2case4seekback:=sorted(Case4seekback)):
        c._idx_ = i
    jp2pair = []
    pair2jp = {}
    for i, s in enumerate(sorted(Case4seekback)):
        for j, r in enumerate(sorted(Case4reply)):
            jp = len(jp2pair)
            pair = s, r
            jp2pair.append(pair)
            pair2jp[pair] = jp
    return (i2case4protection, j2case4reply, b2case4seekback, jp2pair, pair2jp)

def _tabulate_2(sorted_all_good_exconfigs, jp2pair, pair2jp, /):
    'tabulation ver of _case4protection_Z_case4reply5child_Z_pairs_4_6case4seekback_case4reply5self9'
    i2j2k2jp = [[[] for _ in range(len(Case4reply))] for _ in range(len(Case4protection))]
    i2j2k2jg = [[[] for _ in range(len(Case4reply))] for _ in range(len(Case4protection))]
    for jg, exconfig in enumerate(sorted_all_good_exconfigs):
        (case4protection, config) = exconfig
        (case4reply5child, case4seekback, case4reply5self) = config
        pair = config[1:] #(case4seekback, case4reply5self)
        jp = pair2jp[pair]
        k2jp = i2j2k2jp[case4protection._idx_][case4reply5child._idx_]
        k2jp.append(jp)
        #
        k2jg = i2j2k2jg[case4protection._idx_][case4reply5child._idx_]
        k2jg.append(jg)
        #
    used_jp_set = {jp for j2k2jp in i2j2k2jp for k2jp in j2k2jp for jp in k2jp}
    i2j2sz = tuple(tuple(map(len, j2k2jp)) for j2k2jp in i2j2k2jp)
    max_sz = max(sz for j2sz in i2j2sz for sz in j2sz)
    return (i2j2k2jg, i2j2k2jp, i2j2sz, max_sz, used_jp_set)

def _list2name_ver(ls, /):
    return [c.name for c in ls]
def _pair2name_ver(pair, /):
    a, b = pair
    return f'{a.name}.{b.name}'
(_i2case4protection, _j2case4reply, _b2case4seekback, _jp2pair, _pair2jp) = _tabulate_1()
(_i2j2k2jg, _i2j2k2jp, _i2j2sz, _max_sz, _used_jp_set) = _tabulate_2(sorted_all_good_exconfigs, _jp2pair, _pair2jp)
    #tabulation ver of _case4protection_Z_case4reply5child_Z_pairs_4_6case4seekback_case4reply5self9
_jp2pair__name_ver = [*map(_pair2name_ver, _jp2pair)]
_pair2jp__name_ver = {_pair2name_ver(p):jp for p, jp in _pair2jp.items()}
(_jp2pair__name_ver, _pair2jp__name_ver)


def convert_exconfigpack5uint_ver(exconfigpack__uint_ver, /, *, forbid____protected_ok):
    'exconfigpack__uint_ver -> exconfigpack/exconfigpack__case_ver'
    (i, j2k) = exconfigpack__uint_ver
    case4protection = _i2case4protection[i]
    j2k2jp = _i2j2k2jp[i]
    configpack = {}
    for j, k in enumerate(j2k):
        jp = j2k2jp[j][k]
        pair = _jp2pair[jp]
        (case4seekback, case4reply5self) = pair
        case4reply5child = _j2case4reply[j]
        configpack[case4reply5child] = pair
    configpack
    exconfigpack = (case4protection, configpack)
    return exconfigpack#case_ver
def convert_exconfigpack2uint_ver(exconfigpack, /, *, forbid____protected_ok):
    'exconfigpack/exconfigpack__case_ver -> exconfigpack__uint_ver'
    _Case4reply = _get_pseudo_Case4reply(forbid____protected_ok)

    (case4protection, configpack) = exconfigpack
    check_type_is(Case4protection, case4protection)
    assert configpack.keys() == _Case4reply

    i = case4protection._idx_
    j2k2jp = _i2j2k2jp[i]
    j2k = [None]*len(Case4reply)
    for case4reply5child, pair in configpack.items():
        (case4seekback, case4reply5self) = pair
        check_type_is(Case4reply, case4reply5child)
        check_type_is(Case4seekback, case4seekback)
        check_type_is(Case4reply, case4reply5self)
        j = case4reply5child._idx_
        jp = _pair2jp[pair]
        k = j2k2jp[j].index(jp)
        j2k[j] = k
    assert sum(m is not None for m in j2k) == len(_Case4reply)
    j2k = tuple(j2k)
    exconfigpack__uint_ver = (i, j2k)
    return exconfigpack__uint_ver

class _WeakSymbolizeRegister4exconfigpack(WeakSymbolizeRegister):
    forbid____protected_ok = False
    case_vs_uint = False
    #@override
    def _check_value_(sf, val, /):
        'val/hashable -> None|^Exception'
        exconfigpack = exconfigpack5or_uint_ver_(sf.case_vs_uint, val)
        if not is_best_exconfigpack_(exconfigpack, forbid____protected_ok=sf.forbid____protected_ok):raise Exception(val)
weak_symbolize_register4exconfigpack = _WeakSymbolizeRegister4exconfigpack()
def exconfigpack5or_uint_ver_(case_vs_uint, exconfigpack_or_uint_ver, /):
    val = exconfigpack_or_uint_ver
    if case_vs_uint:
        exconfigpack__uint_ver = val
        exconfigpack = convert_exconfigpack5uint_ver(exconfigpack__uint_ver)
    else:
        exconfigpack = val
    exconfigpack
    return exconfigpack
class _WeakSymbolizeRegister4exconfigpack_____forbid____protected_ok(ISymbolizeRegister__subset):
    ___no_slots_ok___ = True
    #@final
    forbid____protected_ok = True
    case_vs_uint = False
    @property
    def case_vs_uint(sf, /):
        return sf.backgroud_symbolizer.case_vs_uint
    #@override
    def _check_value__more_(sf, val, /):
        '[backgroud_symbolizer checked]=>val/hashable -> None|^Exception'
        exconfigpack = exconfigpack5or_uint_ver_(sf.case_vs_uint, val)
        if not is_best_exconfigpack_(exconfigpack, forbid____protected_ok=sf.forbid____protected_ok):raise Exception(val)
weak_symbolize_register4exconfigpack_____forbid____protected_ok = _WeakSymbolizeRegister4exconfigpack_____forbid____protected_ok(weak_symbolize_register4exconfigpack)
_fpk2wd = (weak_symbolize_register4exconfigpack, weak_symbolize_register4exconfigpack_____forbid____protected_ok)


def mk_gi4IRecognizerLLoo__5solo_rgnr_transform_cases_(Call, to_lift:bool, best_exconfigpack:'exconfigpack{best}', rgnr, unlocker, ignore, istream, /, *, case_vs_sym_vs_uint:'may bool', forbid____protected_ok:False):
    'to_lift/bool -> exconfigpack{best} -> IRecognizerLLoo -> IUnlocker -> ignore/bool -> istream/IRecoverableInputStream -> GenIter[#see:IRecognizerLLoo._mk_gi4recognize_()#]  # [allow:protected_ok/(protected_severe_ok|protected_forgivable_ok)] #[exconfigpack ~=~ (i/uint%9, [k{<8}]{len=8})] ==>> [case_vs_uint/bool:exconfigpack or (i,j2k/[k])] #[case_vs_sym_vs_uint == may case_vs_uint]'
    #assert is_best_exconfigpack_(best_exconfigpack, forbid____protected_ok=forbid____protected_ok)
    _wd = weak_symbolize_register4exconfigpack = _fpk2wd[forbid____protected_ok]
    if not forbid____protected_ok is _wd.forbid____protected_ok:raise TypeError

    if case_vs_sym_vs_uint is None:
        _sym = best_exconfigpack
        best_exconfigpack = _wd.lookup(_sym)
        case_vs_uint = _wd.case_vs_uint
    else:
        case_vs_uint = case_vs_sym_vs_uint
    case_vs_uint
    check_type_is(bool, case_vs_uint)
    if case_vs_uint:
        exconfigpack__uint_ver = best_exconfigpack
        (_i, _j2k) = exconfigpack__uint_ver
        case4protection = _i2case4protection[_i]
    else:
        exconfigpack = best_exconfigpack
        (case4protection, configpack) = exconfigpack
    case4protection
    (case4protection6unlocker, case4protection6snapshot) = case4protection.value
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
    monotonic_idx8begin = istream.tell_monotonic_idx()
    reply5child = yield Call(rgnr, unlocker4child, ignore, istream)
    istream8end = istream
    case4reply5child = mk_case4reply5child(unlocker4child, monotonic_idx8begin, reply5child, istream8end)
    #paritally_check_case4reply5xxx___whether_protected_ok(case4reply5child, forbid____protected_ok=forbid____protected_ok)
    _check_case4reply5xxx(case4reply5child, forbid____protected_ok)
    ######################
    if case_vs_uint:
        _j = case4reply5child._idx_
        _k = _j2k[_j]
        _jp = _i2j2k2jp[_i][_j][_k]
        pair = _jp2pair[_jp]
    else:
        pair = configpack[case4reply5child]
    pair
    (case4seekback, case4reply5self) = pair
    reply = reply5child
    ######################
    if to_lift:
        # [should be first alter of reply]
        config = (case4reply5child, case4seekback, case4reply5self)
        exconfig = (case4protection, config)
        if case_vs_uint:
            _jg = _i2j2k2jg[_i][_j][_k]
            _exconfig = jg2good_exconfig[_jg]
            assert exconfig == _exconfig
            exconfig = _exconfig
        exconfig
        payload = (reply, exconfig)
        reply = reply.ireplace(eresult=reply.eresult.ireplace__payload(payload))
    ######################
    match case4seekback:
        case _cases.no_seekback:
            pass
        case _cases.to_seekback:
            snapshot.restore_and_release(istream)
            istream8end = istream
            reply = reply.ireplace(ext_info8end=istream8end.tell_ext_info())
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
        assert case4reply5child.is_protected() or case4protection.is_unlocker_hide()
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
    _check_case4reply5xxx(case4reply5self, forbid____protected_ok)
    ######################
    return reply5self
def _check_case4reply5xxx(case4reply5xxx, forbid____protected_ok, /):
    if forbid____protected_ok:
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

def determine_case4seekback_(case4reply5child, case4reply5self, /):
    'case4reply5child -> case4reply5self -> case4seekback |^Exception # [news__constraint4xx_seekback=>[case4seekback is redundant]]'
    if case4reply5child.is_severe() and case4reply5self.is_forgivable():
        return to_seekback
    if case4reply5child.is_forgivable() and case4reply5self.is_severe(): raise Exception
    assert case4reply5child.get_xforgivable() == case4reply5self.get_xforgivable()
    return no_seekback

def composite__unlocker_xxx_(unlocker_xxx4self, unlocker_xxx4child, /):
    'Case4protection6unlocker -> Case4protection6unlocker -> Case4protection6unlocker'
    unlocker_xxx4composite = unlocker_xxx4self if not unlocker_xxx4self == unlocker_into else unlocker_xxx4child
    return unlocker_xxx4composite
def roughly_composite__snapshot_xxx_(snapshot_xxx4self, unlocker_xxx4child, snapshot_xxx4child, /):
    'Case4protection6snapshot -> Case4protection6unlocker -> Case4protection6snapshot -> Case4protection6snapshot'
    C = Case4protection6snapshot
    match snapshot_xxx4self:
        case C.snapshot_hide:
            return snapshot_hide
        case C.snapshot_none:
            return snapshot_xxx4child
        case C.snapshot_into:
            pass
        case _:
            raise 000
    # [snapshot_xxx4self == snapshot_into]
    if snapshot_xxx4child == snapshot_hide:
            return snapshot_hide
    # [snapshot_xxx4self == snapshot_into]
    # [snapshot_xxx4child <- {snapshot_into,snapshot_none}]
    Cu = Case4protection6unlocker
    match unlocker_xxx4child:
        case Cu.unlocker_hide:
            return snapshot_hide
        case Cu.unlocker_into:
            return snapshot_into
        case Cu.unlocker_free:
            #snapshot_xxx4self be released immediately
            return snapshot_xxx4child
        case _:
            raise 000
    raise 000



def roughly_composite__case4protection_(case4protection4self, case4protection4child, /):
    'Case4protection -> Case4protection -> Case4protection'
    # roughly_composite__case4protection_ === (composite__unlocker_xxx_ +++ roughly_composite__snapshot_xxx_)
    (unlocker_xxx4self, snapshot_xxx4self) = case4protection4self.value
    (unlocker_xxx4child, snapshot_xxx4child) = case4protection4child.value
    unlocker_xxx4composite = composite__unlocker_xxx_(unlocker_xxx4self, unlocker_xxx4child)
    snapshot_xxx4roughly_composite = roughly_composite__snapshot_xxx_(snapshot_xxx4self, unlocker_xxx4child, snapshot_xxx4child)
    case4protection4roughly_composite = Case4protection((unlocker_xxx4composite, snapshot_xxx4roughly_composite))
    return case4protection4roughly_composite
def roughly_composite__exconfig_(exconfig4self, exconfig4child, /):
    'exconfig4self -> exconfig4child -> exconfig4roughly_composite'
    #(case4protection, (case4reply5child, case4seekback, case4reply5self)) = exconfig
    (case4protection4self, (case4reply5child, case4seekback4self, case4reply5self)) = exconfig4self
    (case4protection4child, (case4reply5grandchild, case4seekback4child, _case4reply5child)) = exconfig4child
    if not case4reply5child == _case4reply5child:raise Exception
    case4seekback4composite = determine_case4seekback_(case4reply5grandchild, case4reply5self)
    #case4protection4composite
    case4protection4roughly_composite = roughly_composite__case4protection_(case4protection4self, case4protection4child)
    exconfig4roughly_composite = (case4protection4roughly_composite, (case4reply5grandchild, case4seekback4composite, case4reply5self))
    return exconfig4roughly_composite
def composite__configpack_(configpack4self, configpack4child, /):
    'configpack4self -> configpack4child -> configpack4composite'
    #for case4reply5child, (case4seekback, case4reply5self) in configpack.items():
    configpack4composite = {}
    for case4reply5grandchild, (_case4seekback4child, case4reply5child) in configpack4child.items():
        (_case4seekback4self, case4reply5self) = configpack4self[case4reply5child]
        case4seekback4composite = determine_case4seekback_(case4reply5grandchild, case4reply5self)
        configpack4composite[case4reply5grandchild] = (case4seekback4composite, case4reply5self)
    configpack4composite
    return configpack4composite
def roughly_composite__exconfigpack_(exconfigpack4self, exconfigpack4child, /):
    'exconfigpack4self -> exconfigpack4child -> exconfigpack4roughly_composite[#maybe not best#]'
    #vs:exconfig4roughly_composite = roughly_composite__exconfig_(exconfig4self, exconfig4child)
    #(case4protection, configpack) = exconfigpack
    (case4protection4self, configpack4self) = exconfigpack4self
    (case4protection4child, configpack4child) = exconfigpack4child
    configpack4composite = composite__configpack_(configpack4self, configpack4child)
    case4protection4roughly_composite = roughly_composite__case4protection_(case4protection4self, case4protection4child)
    exconfigpack4roughly_composite = (case4protection4roughly_composite, configpack4composite)
    return exconfigpack4roughly_composite
def composite__exconfigpack_(exconfigpack4self, exconfigpack4child, /):
    'exconfigpack4self -> exconfigpack4child -> exconfigpack4roughly_composite[#best#]'
    forbid____protected_ok = False

    exconfigpack4roughly_composite = roughly_composite__exconfigpack_(exconfigpack4self, exconfigpack4child)
    #search best one #i.e. change case4protection.snapshot_xxx
    #   !! composite__unlocker_xxx_
    #   !! roughly_composite__snapshot_xxx_
    (case4protection4roughly_composite, configpack4composite) = exconfigpack4roughly_composite

    (unlocker_xxx4composite, snapshot_xxx4roughly_composite) = case4protection4roughly_composite.value
    min_case4protection4composite = Case4protection((unlocker_xxx4composite, snapshot_none))
        #snapshot_none is min in pcmp, but has biggest idx
    max_case4protection4composite = case4protection4roughly_composite
    assert min_case4protection4composite in _pcmp_le_table4Case4protection[max_case4protection4composite]

    min_idx = max_case4protection4composite._idx_
    max_idx = min_case4protection4composite._idx_
        #snapshot_none is min in pcmp, but has biggest idx

    assert max_idx -min_idx <= 2
    for i in range(min_idx, max_idx+1):
        assert _i2case4protection[i].get_unlocker_xxx() == unlocker_xxx4composite
    ######################
    #TODO:composite__exconfigpack_,连同unlocker_xxx也得变更
    #   但是 可能 多个 极值 #<<==偏序
    #   也许 该使用 符号推导...
    for i in reversed(range(min_idx, max_idx+1)):
        #snapshot_none is min in pcmp, but has biggest idx
        case4protection = _i2case4protection[i]
        exconfigpack = (case4protection, configpack4composite)
        if is_good_exconfigpack_(exconfigpack, forbid____protected_ok=forbid____protected_ok):
            exconfigpack4composite = exconfigpack
            break
    else:
        raise Exception('composite__exconfigpack_ result not is_good_exconfigpack_', exconfigpack4self, exconfigpack4child, exconfigpack4roughly_composite)

    exconfigpack4composite

    if not is_best_exconfigpack_(exconfigpack4composite, forbid____protected_ok=forbid____protected_ok):
        #see:below:1640267@validate_composite__exconfigpack__6all_best_exconfigpacks
        raise Exception('composite__exconfigpack_ result not is_best_exconfigpack_', exconfigpack4self, exconfigpack4child, exconfigpack4roughly_composite, exconfigpack4composite)
    return exconfigpack4composite
#end-def composite__exconfigpack_(exconfigpack4self, exconfigpack4child, /):



def _4binop(f, xs, /):
    ls = []
    for x in xs:
        for y in ls:
            # [iy < ix]
            f(y, x)
        ls.append(x)
        for y in ls:
            # [iy <= ix]
            f(x, y)
def validate_composite__exconfigpack__6all_best_exconfigpacks(*, forbid____protected_ok, verbose=False):
    best_exconfigpacks = iter_all_best_exconfigpacks_(None, forbid____protected_ok=forbid____protected_ok)
    if not verbose:
        f = composite__exconfigpack_
    else:
        g = composite__exconfigpack_
        j = 0
        def f(x, y, /):
            nonlocal j
            print_err(j)
            j += 1
            g(x, y)
    f
    _4binop(f, best_exconfigpacks)
    return
    ######################
    #j==1640267:
    #Exception: ('composite__exconfigpack_ result not is_best_exconfigpack_', (unlocker_hide__snapshot_hide, {protected_forgivable_ok: (no_seekback, protected_forgivable_ok), protected_forgivable_fail: (no_seekback, protected_forgivable_ok), protected_severe_ok: (to_seekback, protected_forgivable_ok), protected_severe_fail: (to_seekback, unprotected_forgivable_ok), unprotected_forgivable_ok: (no_seekback, protected_forgivable_ok), unprotected_forgivable_fail: (no_seekback, unprotected_forgivable_ok), unprotected_severe_ok: (to_seekback, protected_forgivable_ok), unprotected_severe_fail: (to_seekback, protected_forgivable_ok)}), (unlocker_hide__snapshot_hide, {protected_forgivable_ok: (no_seekback, protected_forgivable_ok), protected_forgivable_fail: (no_seekback, protected_forgivable_ok), protected_severe_ok: (to_seekback, protected_forgivable_ok), protected_severe_fail: (to_seekback, protected_forgivable_ok), unprotected_forgivable_ok: (no_seekback, unprotected_forgivable_fail), unprotected_forgivable_fail: (no_seekback, unprotected_forgivable_fail), unprotected_severe_ok: (to_seekback, unprotected_forgivable_fail), unprotected_severe_fail: (no_seekback, protected_severe_fail)}), (unlocker_hide__snapshot_hide, {protected_forgivable_ok: (no_seekback, protected_forgivable_ok), protected_forgivable_fail: (no_seekback, protected_forgivable_ok), protected_severe_ok: (to_seekback, protected_forgivable_ok), protected_severe_fail: (to_seekback, protected_forgivable_ok), unprotected_forgivable_ok: (no_seekback, unprotected_forgivable_ok), unprotected_forgivable_fail: (no_seekback, unprotected_forgivable_ok), unprotected_severe_ok: (to_seekback, unprotected_forgivable_ok), unprotected_severe_fail: (to_seekback, unprotected_forgivable_ok)}), (unlocker_hide__snapshot_hide, {protected_forgivable_ok: (no_seekback, protected_forgivable_ok), protected_forgivable_fail: (no_seekback, protected_forgivable_ok), protected_severe_ok: (to_seekback, protected_forgivable_ok), protected_severe_fail: (to_seekback, protected_forgivable_ok), unprotected_forgivable_ok: (no_seekback, unprotected_forgivable_ok), unprotected_forgivable_fail: (no_seekback, unprotected_forgivable_ok), unprotected_severe_ok: (to_seekback, unprotected_forgivable_ok), unprotected_severe_fail: (to_seekback, unprotected_forgivable_ok)}))
    ######################
    best_exconfigpacks = [*best_exconfigpacks]
    assert len(best_exconfigpacks) == 4050

    j = 0
    if verbose:
        print_err(L:=len(best_exconfigpacks))
        print_err(j, divmod(j, L))
    ps = product(best_exconfigpacks, best_exconfigpacks)
    for j, (exconfigpack4self, exconfigpack4child) in enumerate(ps, 1):
        if verbose:
            print_err(j, divmod(j, L))
        composite__exconfigpack_(exconfigpack4self, exconfigpack4child)






def _pseudo_exconfigpack5exconfig(exconfig, /, *, forbid____protected_ok):
    (case4protection, (case4reply5child, case4seekback, case4reply5self)) = exconfig
    _Case4reply = _get_pseudo_Case4reply(forbid____protected_ok)
    sz = len(_Case4reply)
    pseudo_configpack = _Pseudo_configpack(sz, case4reply5child, case4seekback, case4reply5self)
    pseudo_exconfigpack = (case4protection, pseudo_configpack)
    return pseudo_exconfigpack

class _Pseudo_configpack:
    def __init__(sf, sz, case4reply5child, case4seekback, case4reply5self, /):
        assert case4seekback == determine_case4seekback_(case4reply5child, case4reply5self)
        sf._sz = sz
        sf._k = case4reply5child
        sf._v = (case4seekback, case4reply5self)
    def __len__(sf, /):
        return sf._sz
    def __getitem__(sf, k, /):
        if not k == sf._k:raise KeyError(k, sf._k)
        return sf._v





#behin:validate____roughly_composite__case4protection_

def _init4validate____roughly_composite__case4protection_(*, forbid____protected_ok):
    from seed.tiny import echo
    from seed.types.Either import Cased, Either
    from seed.types.Either import mk_Left, mk_Right

    good_exconfigs = sorted_all_good_exconfigs_(None, forbid____protected_ok=forbid____protected_ok)
        # :: [exconfig]
        # :: [(case4protection, config)]
        # :: [(case4protection, (case4reply5child, case4seekback, case4reply5self))]

    def f(exconfig4self, /):
        'exconfig4self -> case4reply5self'
        (case4protection4self, (case4reply5child, case4seekback, case4reply5self)) = exconfig4self
        return case4reply5self
    ##def g(exconfig4self, /):
    ##    'exconfig4self -> (case4protection4self, case4reply5child)'
    ##    (case4protection4self, (case4reply5child, case4seekback, case4reply5self)) = exconfig4self
    ##    return (case4protection4self, case4reply5child)

    ##case4reply5self_Z_case4protection4self_case4reply5child_pairs = xs_to_k2vs_(f, g, good_exconfigs)
    ##    # :: {case4reply5self:[(case4protection4self, case4reply5child)]}
    ##case4reply5child_Z_case4protection4child_case4reply5grandchild_pairs = case4reply5self_Z_case4protection4self_case4reply5child_pairs
    ##    # :: {case4reply5child:[(case4protection4child, case4reply5grandchild)]}
    ##case4reply5child_Z_case4protection4child_case4reply5grandchild_pairs

    case4reply5self_Z_exconfigs4self = xs_to_k2vs_(f, echo, good_exconfigs)
        # :: {case4reply5self:[exconfig4self]}
    case4reply5child_Z_exconfigs4child = case4reply5self_Z_exconfigs4self
        # :: {case4reply5child:[exconfig4child]}
    _Case4reply = _get_pseudo_Case4reply(forbid____protected_ok)
    assert len(case4reply5child_Z_exconfigs4child) == len(_Case4reply), (len(case4reply5child_Z_exconfigs4child), len(_Case4reply), forbid____protected_ok, sorted(case4reply5child_Z_exconfigs4child))

    ######################
    from seed.recognize.recognizer_LLoo__ver2_.IRecognizerLLoo import IRecognizerLLoo, Reply, RecognizeReply, dummy_unlocker# Call, RecognizeCall
    def Call(rgnr, unlocker, ignore, istream, /):
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
    Call
    to_lift = True
    mk_token_rawstream__5xs__idx_#pseudo_rgnr
    ignore = False
    pseudo_istream = PlainRecoverableInputStream5token_seq(max_num_tokens6backward:=0, may_prev_token_end_gap_position_info:=None, offset:=0, token_seq)
    777;    monotonic_idx8begin = pseudo_istream.tell_monotonic_idx()
    777;    monotonic_idx8end = monotonic_idx8begin+1
    ######################
    def vivi_call(pseudo_exconfigpack4self, pseudo_rgnr8self, unlocker4self, pseudo_rcall2reply5child, /, *args4pseudo_rcall2reply5child):
        #def mk_gi4IRecognizerLLoo__5solo_rgnr_transform_cases_(Call, to_lift:bool, best_exconfigpack:'exconfigpack{best}', rgnr, unlocker, ignore, istream, /, *, case_vs_sym_vs_uint:'may bool', forbid____protected_ok:False):
        #Call
        #to_lift
        #ignore
        #pseudo_istream
        gi8self = mk_gi4IRecognizerLLoo__5solo_rgnr_transform_cases_(Call, to_lift, pseudo_exconfigpack4self, pseudo_rgnr8self, unlocker4self, ignore, pseudo_istream, case_vs_sym_vs_uint=False, forbid____protected_ok=forbid____protected_ok)
        pseudo_rcall8child = gi8self.send(None)
        reply5child = pseudo_rcall2reply5child(pseudo_rcall8child, *args4pseudo_rcall2reply5child)
        try:
            gi8self.send(reply5child)
        except StopIteration as e:
            reply5self = e.value
        else:
            raise 000
        return reply5self
    def pseudo_rcall2reply5child(pseudo_rcall8child, pseudo_exconfigpack4child, /):
        '-> reply5child'
        #pseudo_rcall/(rgnr, unlocker, ignore, istream)
        (pseudo_rgnr8child, unlocker4child, ignore, pseudo_istream) = pseudo_rcall8child
        reply5child = vivi_call(pseudo_exconfigpack4child, pseudo_rgnr8child, unlocker4child, pseudo_rcall2reply5grandchild)
        return reply5child
    def pseudo_rcall2reply5grandchild(pseudo_rcall8grandchild, /):
        '-> reply5grandchild'
        (pseudo_rgnr8grandchild, unlocker4grandchild, ignore, pseudo_istream) = pseudo_rcall8grandchild
        #assert pseudo_rgnr8grandchild is pseudo_rgnr
        pseudo_rgnr = pseudo_rgnr8grandchild
        reply5grandchild = pseudo_rgnr(unlocker4grandchild, pseudo_istream)
        return reply5grandchild
    ######################
    _init_result4validate = (good_exconfigs, case4reply5child_Z_exconfigs4child, (Call, to_lift, mk_pseudo_rgnr_and_reset_istream_, ignore, pseudo_istream, vivi_call, pseudo_rcall2reply5child, pseudo_rcall2reply5grandchild))
    return _init_result4validate
#end-def _init4validate____roughly_composite__case4protection_(*, forbid____protected_ok):
def _iter4validate____roughly_composite__case4protection_(good_exconfigs, case4reply5child_Z_exconfigs4child, *, forbid____protected_ok):
    def h(exconfig4self, /):
        'exconfig4self -> case4reply5child'
        (case4protection4self, (case4reply5child, case4seekback, case4reply5self)) = exconfig4self
        return case4reply5child
    def iter_exconfigs4child_5exconfig4self_(exconfig4self, /):
        '-> Iter exconfig4child'
        case4reply5child = h(exconfig4self)
        exconfigs4child = case4reply5child_Z_exconfigs4child[case4reply5child]
        return iter(exconfigs4child)
    iter_exconfigs4child_5exconfig4self_

    for exconfig4self in good_exconfigs:
      for exconfig4child in iter_exconfigs4child_5exconfig4self_(exconfig4self):
        exconfig4roughly_composite = roughly_composite__exconfig_(exconfig4self, exconfig4child)
        #(case4protection4xxx, (case4reply5child, case4seekback, case4reply5self)) = exconfig4xxx
        #   (self|child|roughly_composite)
        #
        ######################
        #find a best exconfigpack contains this exconfig
        pseudo_exconfigpack4self = _pseudo_exconfigpack5exconfig(exconfig4self, forbid____protected_ok=forbid____protected_ok)
        pseudo_exconfigpack4child = _pseudo_exconfigpack5exconfig(exconfig4child, forbid____protected_ok=forbid____protected_ok)
        pseudo_exconfigpack4roughly_composite = _pseudo_exconfigpack5exconfig(exconfig4roughly_composite, forbid____protected_ok=forbid____protected_ok)
        # pseudo_exconfigpack4xxx
        #   (self|child|roughly_composite)
        yield (exconfig4self, exconfig4child, pseudo_exconfigpack4self, pseudo_exconfigpack4child, pseudo_exconfigpack4roughly_composite)
    return

def validate____roughly_composite__case4protection_(*, forbid____protected_ok):
    _init_result4validate = _init4validate____roughly_composite__case4protection_(forbid____protected_ok=forbid____protected_ok)
    (good_exconfigs, case4reply5child_Z_exconfigs4child, (Call, to_lift, mk_pseudo_rgnr_and_reset_istream_, ignore, pseudo_istream, vivi_call, pseudo_rcall2reply5child, pseudo_rcall2reply5grandchild)) = _init_result4validate
    for (exconfig4self, exconfig4child, pseudo_exconfigpack4self, pseudo_exconfigpack4child, pseudo_exconfigpack4roughly_composite) in _iter4validate____roughly_composite__case4protection_(good_exconfigs, case4reply5child_Z_exconfigs4child, forbid____protected_ok=forbid____protected_ok):
        (case4protection4child, (case4reply5grandchild, case4seekback4child, _case4reply5child)) = exconfig4child
        pseudo_rgnr = mk_pseudo_rgnr_and_reset_istream_(case4reply5grandchild, pseudo_istream)
        pseudo_rgnr8self = pseudo_rgnr
        unlocker4self = DetectionUnlocker()
        assert not unlocker4self.known_released
        _1_reply5self = vivi_call(pseudo_exconfigpack4roughly_composite, pseudo_rgnr8self, unlocker4self, pseudo_rcall2reply5grandchild)
            # reply5self via single composite layer

        pseudo_rgnr = mk_pseudo_rgnr_and_reset_istream_(case4reply5grandchild, pseudo_istream)
        pseudo_rgnr8self = pseudo_rgnr
        unlocker4self = DetectionUnlocker()
        _2_reply5self = vivi_call(pseudo_exconfigpack4self, pseudo_rgnr8self, unlocker4self, pseudo_rcall2reply5child, pseudo_exconfigpack4child)
            # reply5self via two layers

    return
#end-def validate____roughly_composite__case4protection_(*, forbid____protected_ok):


__all__
from seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases import mk_gi4IRecognizerLLoo__5solo_rgnr_transform_cases_
from seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases import is_best_exconfigpack_
from seed.recognize.recognizer_LLoo__ver2_.solo_rgnr_transform_cases import *
