

__all__ = '''
    rough_complete_in_simplified
    '''.split()

from .complete_in_simplified__undefine_Production import \
    complete_in_simplified__undefine_Production

#rough_complete in simplified
rough_complete_in_simplified = fr'''
# rough_complete
#   rough Production ~ far from exactly Production rule
#   verified by filters instead of syntax
#       Production body shouldnot begin or end with sand
#           now using: [(may_sand, xxx_ref_name)]
#           then only need to check the first may_sand if any
#       Production body should match ExternalNoiseDecl
#       location where ref_name used should match ExternalNoiseDecl of that nonterminal
#
#       unit ==>> len(rhs)>0
#       op_unpack ==>> unit; len(rhs op3) == len(rhs)
#       [no op_unpack][unit] ==>> one op_selected; no other op
#       lhs.dicard ==>> tuple; no op2; no aliase; no lhs.filter_ex
#       tuple ==>> no op_unpack
#       tuple ==>> len(rhs may_op2 set) <= 2
#       aliase ==>> tuple; lhs.filter_ex
#       lhs.filter_ex ==>> tuple
#
#


{complete_in_simplified__undefine_Production!s}

; mk_unit_may_unpack$
    Production : filter* def_name -op_eq UnitMayUnpackBodys1
; UnitMayUnpackBodys1 = +UnitMayUnpackBody *OR_UnitMayUnpackBody*
; OR_UnitMayUnpackBody = op_bar +UnitMayUnpackBody
; mk_UnitMayUnpackBody$
    UnitMayUnpackBody = may_sand_suffix_op3_filtered_ref_name+
; may_sand_suffix_op3_filtered_ref_name
    : sand? suffix_op3_filtered_ref_name
; suffix_op3_filtered_ref_name
    : op3? filtered_ref_name


; mk_tuple__may_with_alias$
    Production : filter* op_discard? filter_ex? def_name -op_colon TupleMayWithAliasBodys1
; TupleMayWithAliasBodys1 = +TupleMayWithAliasBody *OR_TupleMayWithAliasBody*
; OR_TupleMayWithAliasBody = op_bar +TupleMayWithAliasBody
; mk_TupleMayWithAliasBody$
    TupleMayWithAliasBody = kw_pass +@none@?
; mk_TupleMayWithAliasBody$
    TupleMayWithAliasBody = may_sand_suffix_op2_decorated_filtered_ref_name*

; may_sand_suffix_op2_decorated_filtered_ref_name
    : sand? suffix_op2_decorated_filtered_ref_name
; suffix_op2_decorated_filtered_ref_name
    : op2? decorator? filtered_ref_name


; mk_filtered_ref_name$
    filtered_ref_name : filter* ref_name


'''






















r'''
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
; const_True$
    op2 : -op_selected
; const_False$
    op2 : -op_discard
; may_op2 = op2
; -may_op2 : @pass@
    # None or bool
; op3 = op2
; const_neg1$
    -op3 : op_unpack
    # -1 or bool

; may_op2_filtered_ref_name : may_op2 filtered_ref_name

; op3_filtered_ref_name : op3 filtered_ref_name
; decorated_ref_name : may_op2 decorator? filtered_ref_name


'''
