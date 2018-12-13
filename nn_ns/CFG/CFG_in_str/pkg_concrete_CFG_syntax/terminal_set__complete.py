

__all__ = '''
    terminal_set__complete
    terminal_set__complete__delta
    '''.split()



from .terminal_set__simplified import terminal_set__simplified


terminal_set__complete__delta = r'''

; @terminal_set@
    kw_noise                # '@noise@'
    kw_no_noise             # '@no_noise@'
    kw_case_set             # '@case_set@'
    kw_atomic_case_set      # '@atomic_case_set@'
    kw_external_noise       # '@external_noise@'

    parameter_name          # r'\\\w+'
    external_template_name  # r'!\w+'
    variable_name           # r'\?\w+'

    # uint = r'[1-9][0-9]*'
    # no space in op_count_array/op_count_range
    # {{[
    op_count_array_open     # {{...}} # r'(?<=[\w)>\]}}@])[{{]{uint}(?!\.)'
    op_count_close          # r'[}}]'
    # {{[
    op_count_range_open     # {{...}} # r'(?<=[\w)>\]}}@])[{{]{uint}?[.][.]{uint}?'

    op_template_case_open   # '<' # r'(?<=\w)<'
    op_template_case_close  # '>' # r'>'
    op_expr_open            # '(' # r'(?<!\S)[(]' # )
    op_template_call_open   # '(' # r'(?<=[\w>])[(]'
    op_template_call_close  # ')' # r'[)]'
    op_comma                # ','
    op_bar                  # r'(?<!\S)[|](?!\S)'
    op_and                  # r'(?<!\S)[&](?!\S)'
    op_diff                 # r'(?<!\S)-(?!\S)'
                            # not op_multi [-]
                            # not op_discard [-]

    op_in                   # r'(?<!\S)<-(?!\S)'

'''



terminal_set__complete = fr'''
## terminal_set__simplified
{terminal_set__simplified!s}

## terminal_set__complete__delta
{terminal_set__complete__delta!s}
'''







