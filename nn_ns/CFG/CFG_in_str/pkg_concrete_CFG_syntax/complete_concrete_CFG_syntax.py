
from .simplified_concrete_CFG_syntax import without_template_case_branch_count_noise

# TODO:
# complete in simplified
complete_concrete_CFG_syntax \
    = with_template_case_branch_count_noise \
    = without_template_case_branch_count_noise + r'''
DefinitionBody
    | NoiseDecl
    | AtomicDisjointCaseSetDecl
    | NonAtomicCaseSetDef
NoiseDecl = '@noise@' op_eq terminal_set_name ('|' terminal_set_name)*
AtomicDisjointCaseSetDecl = '@atomic_case_set@' case_set_name*
NonAtomicCaseSetDef
    = '@case_set@' case_set_name op_eq case_set_name ('|' case_set_name)*
    | '@case_set@' case_set_name op_eq kw_any
    | '@case_set@' case_set_name op_eq kw_none
def_name
    | template_name '(' arg_name (',' arg_name)* ')'
    | template_name '<' decl_case_var (',' decl_case_var)* '>' ( '(' arg_name (',' arg_name)* ')' )?
ref_name
    = '@noise@'
    #| '@no_noise@' | kw_pass ???????
    | arg_name # if inside template define body
    | template_name '(' ref_name (',' ref_name)* ')'
    | template_name '<' case_set_ref_name (',' case_set_ref_name)* '>' ( '(' ref_name (',' ref_name)* ')' )?
    | external_template_name '!' '(' ref_name (',' ref_name)* ')'
multi_op
    {..}

arg_name = '\' name
case_set_ref_name
    = '*' case_set_name
    | '*' kw_any # vs '*' only
    | '?' case_var_name ('<-' case_set_name)?
    | '\' case_var_name
decl_case_var
    = '\' case_var_name '<-' case_set_name
    | '\' case_var_name '<-' kw_any # '*' vs kw_any

'''
