r'''
this grammar split into two part:
    CF part and REG part

CF part:
    CF_rule = OR_rule | CON_rule | COPY_rule
    OR_rule = rule_id ':' name*
    CON_rule = rule_id '=' name_count*
    COPY_rule = rule_id ':=' name

    name_count = name count
    name = rule_id | symbol # nonterminal | terminal
    count = '?' | '*' | '+' | ''

    # keyword : ? * + '' : = :=

REG part:
    after  '------ reg ------'
    REG_rule = re_rule_id '=' re_OR_expr
    re_OR_expr = re_CON_expr ( '|' re_CON_expr )*
    re_CON_expr = re_ATOM_COUNT *
    re_ATOM_COUNT = re_ATOM re_COUNT ?
    re_COUNT = '?' | '*' | '+' | ''
    re_ATOM = re_name | re_group
    re_name = re_rule_id | symbol # the re_rule_ids in right part should not be defined yet
    re_group = '(' re_rule ')'
    
    # keyword : ? * + '' = ( )
    

comment:
    before '----- begin -----'
    after  '------ end ------'
    line comment after '#' # for physic lines
    # xxx line that begin with spaces and not part of a logic line

logic line:
    '\\(\s*\n\s*)\\\s'

grammar:
    main = comment newline \
        \ '----- begin -----' newline \
        \ (CF_rule newline)* \
        \ '------ reg ------' newline \
        \ (REG_rule newline)* \
        \ '------ end ------' newline \
        \ comment


'''
