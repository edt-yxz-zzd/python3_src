

__all__ = '''
    simplified_concrete_CFG_syntax
    simplified_in_simplified
    '''.split()

from .terminal_set__simplified import terminal_set__simplified


# simplified in simplified
simplified_concrete_CFG_syntax \
    = simplified_in_simplified \
    = without_template_case_branch_count_noise = fr'''
# no count {{..}}; but has ?*+
# no no_noise/noise
# no template:
#   t<>; t<>(); t(); !t()
#   ==>> no case_set
# no alternative branch in production
#   no op_bar '|'
# allow comment: '(?<!\S)#.*'


; @start_nonterminal@
    CFG
; @maybedead_nonterminal@
    OR_DiscardBody
    OR_UnitBody
    OR_UnitUnpackBody
    OR_TupleBody
    OR_TupleWithAliasBody
; @ambiguous_nonterminal@

{terminal_set__simplified!s}



; # empty

; remove_Nones$
    CFG = Definition*
; Definition = op_semicolon +DefinitionBody
; DefinitionBody = EmptyDef
; DefinitionBody = TerminalSetDecl
; DefinitionBody = StartNonterminalDecl
; DefinitionBody = AmbiguousNonterminalDecl
; DefinitionBody = MaybedeadNonterminalDecl
; DefinitionBody = Production

; -EmptyDef : @pass@ # <==> "; -EmptyDef :"

; mk_terminal_set_names$
    TerminalSetDecl = kw_terminal_set +terminal_set_name*
; mk_start_nonterminal_names$
    StartNonterminalDecl = kw_start_nonterminal +nonterminal_name*
; mk_ambiguous_nonterminal_names$
    AmbiguousNonterminalDecl = kw_ambiguous_nonterminal +nonterminal_name*
; mk_maybedead_nonterminal_names$
    MaybedeadNonterminalDecl = kw_maybedead_nonterminal +nonterminal_name*

; mk_discard$
    Production : filter* -op_discard def_name -op_colon DiscardBodys1
; DiscardBodys1 = +DiscardBody *OR_DiscardBody*
; DiscardBody = ref_name*
; DiscardBody = kw_pass +@none@?
    # return []

#; OR_DiscardBody = ...
#   see below; not defined in this simplified version

; mk_unit$
    Production : filtered_def_name -op_eq UnitBodys1
; UnitBodys1 = +UnitBody *OR_UnitBody*
#; OR_UnitBody = ...
; mk_unit_body_from_name$
    UnitBody = filtered_ref_name
; mk_unit_body_from_triple$
    UnitBody :
        filtered_ref_name*
        -op_selected filtered_ref_name
        filtered_ref_name*

; mk_unit_unpack$
    Production : filtered_def_name -op_eq UnitUnpackBodys1
; UnitUnpackBodys1 = +UnitUnpackBody *OR_UnitUnpackBody*
#; OR_UnitUnpackBody = ...
; mk_unit_unpack_body$
    UnitUnpackBody :
        op2_filtered_ref_name*
        -op_unpack filtered_ref_name
        op3_filtered_ref_name*

; mk_tuple$
    Production : filtered_def_name -op_colon TupleBodys1
; TupleBodys1 = +TupleBody *OR_TupleBody*
#; OR_TupleBody = ...
; TupleBody = may_op2_filtered_ref_name*
; TupleBody = kw_pass +@none@?

; mk_tuple_with_alias$
    Production : filtered_ex_def_name -op_colon TupleWithAliasBodys1
; TupleWithAliasBodys1 = +TupleWithAliasBody *OR_TupleWithAliasBody*
#; OR_TupleWithAliasBody = ...
; TupleWithAliasBody = decorated_ref_name*
; TupleWithAliasBody = kw_pass +@none@?





; filtered_def_name : filter* def_name
    # f$g$def_name
; filtered_ex_def_name : filter* filter_ex def_name
    # f$g$h$$def_name




; filtered_ref_name : filter* ref_name
    # f$g$ref_name
; op2_filtered_ref_name : op2 filtered_ref_name
    # +f$g$ref_name
    # -f$g$ref_name
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
    # +f$g$ref_name
    # -f$g$ref_name
    # f$g$ref_name

; op3_filtered_ref_name : op3 filtered_ref_name
    # +f$g$ref_name
    # -f$g$ref_name
    # *f$g$ref_name
; decorated_ref_name : may_op2 decorator? filtered_ref_name
    # +a@f$g$ref_name
    # -a@f$g$ref_name
    # a@f$g$ref_name
    # ~@f$g$ref_name
    # +f$g$ref_name
    # -f$g$ref_name
    # f$g$ref_name


; def_name = nonterminal_name
; mk_kw_ref_name$
    ref_name = kw_any
; mk_kw_ref_name$
    ref_name = kw_none
; mk_user_ref_name$
    ref_name = xsymbol_name
; mk_multi_ref_name$
    #bug: ref_name = ref_name multi_op
    ref_name : ref_name multi_op
    #should be:
    #   ref_name : (xsymbol_name|kw_any|kw_none) multi_op
    #why?: ref_name : ref_name multi_op
    #   for complete_version

; xsymbol_name = name
        #| nonterminal_name
        #| terminal_set_name
; nonterminal_name = name
; terminal_set_name = name

; mk_multi_op$
    multi_op = op_multi

#simplified in simplified
'''

