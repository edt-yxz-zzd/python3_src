
#more_simplified in more_simplified
more_simplified_concrete_CFG_syntax = r'''
# subset of simplified_concrete_CFG_syntax
# no filters/decorators inside rhs, no filter_ex in lhs
#   only filters in lhs
# no unit/unit_unpack/tuple_with_alias
#   only tuple allowed
# op_selected, op_discard is not optional
#   they are MUST
# no op_multi/op_eq/op_unpack
# no kw_none/kw_any/kw_pass
# no kw_start_nonterminal/kw_ambiguous_nonterminal/kw_maybedead_nonterminal
# no EmptyDef
# no StartNonterminalDecl/AmbiguousNonterminalDecl/MaybedeadNonterminalDecl
#
# use regex to parse over tokens
#   t_decl = fr'Tn*'
#   op2_name = fr'[-+]n'
#   production = fr'f*n:{op2_name}*'
#   cfg = fr'(;({production}|{t_decl})*'
#   good_prefix_on_fail = fr'{cfg}(;f*(n(:[-+]?)?)?)?'


# see above simplified_concrete_CFG_syntax for regex pattern
#   use tokenize__simplified_version to tokenize more_simplified
; @terminal_set@
    # comment
    # ignore

    # terminal          # char repr in superregex
    filter              # f
    name                # n

    kw_terminal_set     # T
    op_semicolon        # ;
    op_colon            # :
    op_discard          # -
    op_selected         # +

; to_unit$ CFG : +Definitions0
; to_unit$ Definition : -op_semicolon +DefinitionBody
; to_unit$ DefinitionBody : +TerminalSetDecl
; to_unit$ DefinitionBody : +Production

; mk_terminal_set_names$
    to_unit$ TerminalSetDecl : -kw_terminal_set +terminal_set_names0

; mk_tuple$
    Production : +filtered_def_name -op_colon +TupleBody
; to_unit$ TupleBody : +op2_ref_names0



; filtered_def_name : +filters0 +def_name
    # f$g$def_name




; op2_ref_name : +op2 +ref_name
    # +ref_name
    # -ref_name
; const_True$
    op2 : -op_selected
; const_False$
    op2 : -op_discard



; to_unit$ def_name : +name
    #|nonterminal_name
; to_unit$ ref_name : +name
    #| nonterminal_name
    #| terminal_set_name



# op2_ref_names0
; lnk2list$ to_unit$ op2_ref_names0 : +lnk_op2_ref_names0
; to_unit$ lnk_op2_ref_names0 : +lnk_op2_ref_names1
; lnk_op2_ref_names0 :
; lnk_op2_ref_names1 : +lnk_op2_ref_names0 +op2_ref_name

# terminal_set_names0
; lnk2list$ to_unit$ terminal_set_names0 : +lnk_terminal_set_names0
; to_unit$ lnk_terminal_set_names0 : +lnk_terminal_set_names1
; lnk_terminal_set_names0 :
; lnk_terminal_set_names1 : +lnk_terminal_set_names0 +name
                                                    # +terminal_set_name

# filters0
; lnk2list$ to_unit$ filters0 : +lnk_filters0
; to_unit$ lnk_filters0 : +lnk_filters1
; lnk_filters0 :
; lnk_filters1 : +lnk_filters0 +filter

# Definitions0
; lnk2list$ to_unit$ Definitions0 : +lnk_Definitions0
; to_unit$ lnk_Definitions0 : +lnk_Definitions1
; lnk_Definitions0 :
; lnk_Definitions1 : +lnk_Definitions0 +Definition
'''

