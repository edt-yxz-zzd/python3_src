
TODO

from .complete_in_simplified__undefine_Production import \
    complete_in_simplified__undefine_Production
#complete in simplified
complete_in_simplified = fr'''
# @no_noise@/@noise@
# count {{..}}
# template:
#   t<>; t<>(); t(); !t()
#   @case_set@/@atomic_case_set@
#       | & -
#   ,
# alternative branch in production
#   op_bar '|'

{complete_in_simplified__undefine_Production!s}








#Production
; mk_discard$
    Production : filter* -op_discard def_name -op_colon DiscardBodys1
; DiscardBodys1 = +DiscardBody *OR_DiscardBody*
; DiscardBody = ref_name?
; DiscardBody = ref_name sand_or_ref_name* ref_name
; DiscardBody = -kw_pass
    # return []

; OR_DiscardBody = op_bar +DiscardBody
; sand_or_ref_name = sand
; sand_or_ref_name = ref_name

; mk_unit$
    Production : filtered_def_name -op_eq UnitBodys1
; UnitBodys1 = +UnitBody *OR_UnitBody*
; OR_UnitBody = op_bar +UnitBody
; mk_unit_body_from_name$
    UnitBody = filtered_ref_name
; mk_unit_body_from_5$
    UnitBody :
        filtered_ref_name
        sand_or_filtered_ref_name*
        -op_selected filtered_ref_name
        sand_or_filtered_ref_name*
        filtered_ref_name
; mk_unit_body_from_1_s1$
    UnitBody :
        -op_selected filtered_ref_name
        sand_or_filtered_ref_name*
        filtered_ref_name
; mk_unit_body_from_s1_1$
    UnitBody :
        filtered_ref_name
        sand_or_filtered_ref_name*
        -op_selected filtered_ref_name
; sand_or_filtered_ref_name = sand
; sand_or_filtered_ref_name = filtered_ref_name


; mk_unit_unpack$
    Production : filtered_def_name -op_eq UnitUnpackBodys1
; UnitUnpackBodys1 = +UnitUnpackBody *OR_UnitUnpackBody*
; OR_UnitUnpackBody = op_bar +UnitUnpackBody
; mk_unit_unpack_body_from_5$
    UnitUnpackBody :
        op2_filtered_ref_name
        sand_or_op2_filtered_ref_name*
        -op_unpack filtered_ref_name
        sand_or_op3_filtered_ref_name*
        op3_filtered_ref_name
; mk_unit_unpack_body_from_1_s1$
    UnitUnpackBody :
        -op_unpack filtered_ref_name
        sand_or_op3_filtered_ref_name*
        op3_filtered_ref_name
; mk_unit_unpack_body_from_s1_1$
    UnitUnpackBody :
        op2_filtered_ref_name
        sand_or_op2_filtered_ref_name*
        -op_unpack filtered_ref_name
; sand_or_op2_filtered_ref_name = sand
; sand_or_op2_filtered_ref_name = op2_filtered_ref_name
; sand_or_op3_filtered_ref_name = sand
; sand_or_op3_filtered_ref_name = op3_filtered_ref_name


; mk_tuple$
    Production : filtered_def_name -op_colon TupleBodys1
; TupleBodys1 = +TupleBody *OR_TupleBody*
; OR_TupleBody = op_bar +TupleBody
; TupleBody : -kw_pass
; TupleBody = may_op2_filtered_ref_name?
; TupleBody =
    # may_op2 = ''|'+'|'-', but 3 cases all cannot occur at same time
    may_op2_filtered_ref_name
    sand_or_may_op2_filtered_ref_name*
    may_op2_filtered_ref_name
; sand_or_may_op2_filtered_ref_name = sand
; sand_or_may_op2_filtered_ref_name = may_op2_filtered_ref_name


; mk_tuple_with_alias$
    Production : filtered_ex_def_name -op_colon TupleWithAliasBodys1
; TupleWithAliasBodys1 = +TupleWithAliasBody *OR_TupleWithAliasBody*
; OR_TupleWithAliasBody = op_bar +TupleWithAliasBody
; TupleWithAliasBody : -kw_pass
; TupleWithAliasBody = decorated_ref_name?
; TupleWithAliasBody =
    # may_op2 = ''|'+'|'-', but 3 cases all cannot occur at same time
    decorated_ref_name
    sand_or_decorated_ref_name*
    decorated_ref_name
; sand_or_decorated_ref_name = sand
; sand_or_decorated_ref_name = decorated_ref_name




; filtered_def_name : filter* def_name
; filtered_ex_def_name : filter* filter_ex def_name




; filtered_ref_name : filter* ref_name
; op2_filtered_ref_name : op2 filtered_ref_name

; may_op2 = op2
; -may_op2 : @pass@
    # None or bool


; may_op2_filtered_ref_name : may_op2 filtered_ref_name

; op3_filtered_ref_name : op3 filtered_ref_name
; decorated_ref_name : may_op2 decorator? filtered_ref_name


'''
