
__all__ = '''
    simplified_in_more_simplified
    '''.split()

from .terminal_set__simplified import terminal_set__simplified


#simplified in more_simplified
simplified_in_more_simplified = fr'''
# see simplified_concrete_CFG_syntax for regex pattern
#   use tokenize__simplified_version to tokenize more_simplified
# see more_simplified_concrete_CFG_syntax for grammar of this string
#
{terminal_set__simplified}


; mk_main_result$ remove_Nones$
    to_unit$ CFG : +Definitions0
; to_unit$ Definition : -op_semicolon +DefinitionBody
; to_unit$ DefinitionBody : +EmptyDef
; to_unit$ DefinitionBody : +TerminalSetDecl
; to_unit$ DefinitionBody : +StartNonterminalDecl
; to_unit$ DefinitionBody : +AmbiguousNonterminalDecl
; to_unit$ DefinitionBody : +MaybedeadNonterminalDecl
; to_unit$ DefinitionBody : +Production

; const_None$ EmptyDef :

; mk_terminal_set_names$
    to_unit$ TerminalSetDecl : -kw_terminal_set +terminal_set_names0

; mk_start_nonterminal_names$
    to_unit$ StartNonterminalDecl : -kw_start_nonterminal +nonterminal_names0

; mk_ambiguous_nonterminal_names$
    to_unit$ AmbiguousNonterminalDecl : -kw_ambiguous_nonterminal +nonterminal_names0
; mk_maybedead_nonterminal_names$
    to_unit$ MaybedeadNonterminalDecl : -kw_maybedead_nonterminal +nonterminal_names0

; mk_discard$
    Production : +filters0 -op_discard +def_name -op_colon +DiscardBody
; to_unit$ DiscardBody : +ref_names0
; to_list$ DiscardBody : -kw_pass
    # return []


; mk_unit$
    Production : +filtered_def_name -op_eq +UnitBody
; mk_unit_body_from_name$
    to_unit$ UnitBody : +filtered_ref_name
; mk_unit_body_from_triple$
    UnitBody :
        +filtered_ref_names0
        -op_selected +filtered_ref_name
        +filtered_ref_names0

; mk_unit_unpack$
    Production : +filtered_def_name -op_eq +UnitUnpackBody
; mk_unit_unpack_body$
    UnitUnpackBody :
        +op2_filtered_ref_names0
        -op_unpack +filtered_ref_name
        +op3_filtered_ref_names0

; mk_tuple$
    Production : +filtered_def_name -op_colon +TupleBody
; to_unit$ TupleBody : +may_op2_filtered_ref_names0
; to_list$ TupleBody : +kw_pass

; mk_tuple_with_alias$
    Production : +filtered_ex_def_name -op_colon +TupleWithAliasBody
; to_unit$ TupleWithAliasBody : +decorated_ref_names0
; to_list$ TupleWithAliasBody : -kw_pass




; filtered_def_name : +filters0 +def_name
; filtered_ex_def_name : +filters0 +filter_ex +def_name





; mk_filtered_ref_name$
    filtered_ref_name : +filters0 +ref_name
; op2_filtered_ref_name : +op2 +filtered_ref_name
; const_True$
    op2 : -op_selected
; const_False$
    op2 : -op_discard
; to_unit$ may_op2 : +op2
; const_None$ may_op2 :
    # None or bool
; mk_op3_from_op2$ to_unit$ op3 : +op2
; const_op3_unpack$
    op3 : -op_unpack

; may_op2_filtered_ref_name : +may_op2 +filtered_ref_name
; mk_op3_filtered_ref_name$
    op3_filtered_ref_name : +op3 +filtered_ref_name
; decorated_ref_name : +may_op2 +may_decorator +filtered_ref_name
; may_decorator : +decorator
; may_decorator :

; to_unit$ def_name : +nonterminal_name
; mk_kw_ref_name$
    to_unit$ ref_name : +kw_any
; mk_kw_ref_name$
    to_unit$ ref_name : +kw_none
; mk_user_ref_name$
    to_unit$ ref_name : +xsymbol_name
; mk_multi_ref_name$
    ref_name : +ref_name +op_multi
    #ref_name : +(xsymbol_name|kw_any|kw_none) +op_multi
        #since no {{n}}

; to_unit$ xsymbol_name : +name
        #| nonterminal_name
        #| terminal_set_name
; to_unit$ nonterminal_name : +name




; to_unit$ terminal_set_names0 : +names0
; to_unit$ nonterminal_names0 : +names0

# names0
; lnk2list$ to_unit$ names0 : +lnk_names0
; to_unit$ lnk_names0 : +lnk_names1
; lnk_names0 :
; lnk_names1 : +lnk_names0 +name

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


#ref_names0
; lnk2list$ to_unit$ ref_names0 : +lnk_ref_names0
; to_unit$ lnk_ref_names0 : +lnk_ref_names1
; lnk_ref_names0 :
; lnk_ref_names1 : +lnk_ref_names0 +ref_name
#filtered_ref_names0
; lnk2list$ to_unit$ filtered_ref_names0 : +lnk_filtered_ref_names0
; to_unit$ lnk_filtered_ref_names0 : +lnk_filtered_ref_names1
; lnk_filtered_ref_names0 :
; lnk_filtered_ref_names1 : +lnk_filtered_ref_names0 +filtered_ref_name
#op2_filtered_ref_names0
; lnk2list$ to_unit$ op2_filtered_ref_names0 : +lnk_op2_filtered_ref_names0
; to_unit$ lnk_op2_filtered_ref_names0 : +lnk_op2_filtered_ref_names1
; lnk_op2_filtered_ref_names0 :
; lnk_op2_filtered_ref_names1 : +lnk_op2_filtered_ref_names0 +op2_filtered_ref_name
#op3_filtered_ref_names0
; lnk2list$ to_unit$ op3_filtered_ref_names0 : +lnk_op3_filtered_ref_names0
; to_unit$ lnk_op3_filtered_ref_names0 : +lnk_op3_filtered_ref_names1
; lnk_op3_filtered_ref_names0 :
; lnk_op3_filtered_ref_names1 : +lnk_op3_filtered_ref_names0 +op3_filtered_ref_name
#may_op2_filtered_ref_names0
; lnk2list$ to_unit$ may_op2_filtered_ref_names0 : +lnk_may_op2_filtered_ref_names0
; to_unit$ lnk_may_op2_filtered_ref_names0 : +lnk_may_op2_filtered_ref_names1
; lnk_may_op2_filtered_ref_names0 :
; lnk_may_op2_filtered_ref_names1 : +lnk_may_op2_filtered_ref_names0 +may_op2_filtered_ref_name
#decorated_ref_names0
; lnk2list$ to_unit$ decorated_ref_names0 : +lnk_decorated_ref_names0
; to_unit$ lnk_decorated_ref_names0 : +lnk_decorated_ref_names1
; lnk_decorated_ref_names0 :
; lnk_decorated_ref_names1 : +lnk_decorated_ref_names0 +decorated_ref_name




#simplified in more_simplified
'''

