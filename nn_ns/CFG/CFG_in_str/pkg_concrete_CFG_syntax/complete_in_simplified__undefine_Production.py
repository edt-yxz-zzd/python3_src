
__all__ = '''
    complete_in_simplified__undefine_Production
    '''.split()


from .terminal_set__complete import terminal_set__complete

complete_in_simplified__undefine_Production = fr'''
# @no_noise@/@noise@
# count {{..}}
# template:
#   t<>; t<>(); t(); !t()
#   @case_set@/@atomic_case_set@
#       | & -
#   ,
# alternative branch in production
#   op_bar '|'

{terminal_set__complete!s}

; @start_nonterminal@
    CFG
    # <==> in concept "; @start_nonterminal@ = @noise@* +CFG @noise@*"
    #
; @maybedead_nonterminal@
; @ambiguous_nonterminal@




; # empty

; mk_CFG$remove_Nones$
    CFG = Definition*
; Definition = op_semicolon +DefinitionBody
; DefinitionBody = EmptyDef
; DefinitionBody = TerminalSetDecl
; DefinitionBody = StartNonterminalDecl
; DefinitionBody = AmbiguousNonterminalDecl
; DefinitionBody = MaybedeadNonterminalDecl
; DefinitionBody = Production

; DefinitionBody = NoiseDecl
; DefinitionBody = AtomicDisjointCaseSetDecl
; DefinitionBody = NonAtomicCaseSetDef
; DefinitionBody = ExternalNoiseDecl


; mk_NoiseDecl$
    NoiseDecl = -kw_noise -op_colon +nonnullable_ref_names1 *bar_nonnullable_ref_names1*
; mk_ExternalNoiseDecl$
    ExternalNoiseDecl : -kw_external_noise sand? def_name sand?

; const_True$   sand = kw_noise
; const_False$  sand = kw_no_noise
; bar_nonnullable_ref_names1 = op_bar +nonnullable_ref_names1
; verify_nonnullable$
    nonnullable_ref_names1 = ref_name+


; mk_AtomicDisjointCaseSetDecl$
    AtomicDisjointCaseSetDecl = kw_atomic_case_set +case_set_name*
; mk_NonAtomicCaseSetDef$
    NonAtomicCaseSetDef : -kw_case_set +case_set_name op_eq +case_set_expr
; case_set_ex2expr$
    case_set_expr = case_set_name_ex
; mk_case_set_or$
    case_set_expr = +case_set_name_ex *bar_case_set_ref_name+
; mk_case_set_and$
    case_set_expr = +case_set_name_ex *and_case_set_ref_name+
; mk_case_set_diff$
    case_set_expr : case_set_name_ex diff_case_set_ref_name+
; case_set_expr = op_expr_open +case_set_expr op_template_call_close

; case_set_name_ex = kw_any
; case_set_name_ex = kw_none
; case_set_name_ex = case_set_name




; -EmptyDef : @pass@ # <==> "; -EmptyDef :"

; mk_TerminalSetDecl$
    TerminalSetDecl = kw_terminal_set +terminal_set_name*
; mk_StartNonterminalDecl_from_simplified$
    StartNonterminalDecl = kw_start_nonterminal +nonterminal_name*
; mk_StartNonterminalDecl_from_unit_rule$
    StartNonterminalDecl = -kw_start_nonterminal -op_eq sand? nonterminal_name sand?
; mk_AmbiguousNonterminalDecl$
    AmbiguousNonterminalDecl = kw_ambiguous_nonterminal +nonterminal_name*
; mk_MaybedeadNonterminalDecl$
    MaybedeadNonterminalDecl = kw_maybedead_nonterminal +nonterminal_name*

###################################################
#def_name/ref_name
###################################################

; mk_def_name$
    def_name : name case_parameters1? call_parameters1?
    # nonterminal_name
    # template_name
; call_parameters1 =
        -op_template_call_open
            +parameter_name *comma_parameter_name*
        -op_template_call_close
; case_parameters1 =
        -op_template_case_open
            +decl_case_var *comma_decl_case_var*
        -op_template_case_close
; comma_parameter_name = op_comma +parameter_name
; comma_decl_case_var = op_comma +decl_case_var
; decl_case_var : parameter_name -op_in case_set_expr



; mk_ref_name$
    ref_name : baisc_ref_name count_op* multi_op?
; mk_ref_name_from_kw$
    baisc_ref_name = kw_any
; mk_ref_name_from_kw$
    baisc_ref_name = kw_none
; mk_ref_name_from_call_name$
    baisc_ref_name = call_name

; mk_count_op_from_op_multi$
    multi_op = op_multi
; mk_count_op_open_from_array$
    count_op_open = op_count_array_open
; mk_count_op_open_from_range$
    count_op_open = op_count_range_open
; mk_count_op__with_or_with_noise$
    count_op = count_op_open op_colon sand op_count_close
; mk_count_op__join$
    count_op = count_op_open op_colon sand? ref_name sand? op_count_close


; call_name : name_ex case_args1? call_args1?
; name_ex = external_template_name
; name_ex = name
; case_args1 =
        -op_template_case_open
            +case_set_ref_name *comma_case_set_ref_name*
        -op_template_case_close
; call_args1 =
        -op_template_call_open
            +ref_name *comma_ref_name*
        -op_template_call_close
; comma_case_set_ref_name = op_comma +case_set_ref_name
; comma_ref_name = op_comma +ref_name

; mk_case_set_ref_name_from_unpack$
    case_set_ref_name = op_unpack +case_set_expr
; mk_case_set_ref_name_from_var$
    case_set_ref_name = variable_name
    # derived; not input parameter_name
; mk_case_set_ref_name_from_var_in_set$
    case_set_ref_name : variable_name -op_in case_set_expr
; mk_case_set_ref_name_from_arg$
    case_set_ref_name = parameter_name


###################################################
#op3/op2
###################################################
; op3 = op2
; const_neg1$
    -op3 : op_unpack
    # -1 or bool

; const_True$
    op2 : -op_selected
; const_False$
    op2 : -op_discard
###################################################
; nonterminal_name = name
; terminal_set_name = name


#to define: Production
#   use: filter/filter_ex/op_...
#   use: def_name/ref_name
#   use: op3/op2

'''




