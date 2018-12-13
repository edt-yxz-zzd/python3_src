
# terminal_set of simplified
terminal_set__simplified = r'''
; @terminal_set@
    # comment       # r'(?<!\S)[#][^\n]*'
    # ignore        # r'\s+'
    filter          # r'\b(?!\d)\w+[$](?![$])'
    filter_ex       # r'\b(?!\d)\w+[$][$](?![$])'
    decorator       # r'~@|(?<!@)\b\w+@'
    name            # r'\b(?!\d)\w+\b(?![$@])'

    # r'@\w+@'
    kw_terminal_set             # '@terminal_set@'
    kw_start_nonterminal        # '@start_nonterminal@'
    kw_ambiguous_nonterminal    # '@ambiguous_nonterminal@'
    kw_maybedead_nonterminal    # '@maybedead_nonterminal@'
    kw_pass                     # '@pass@'
    kw_any                      # '@any@'
    kw_none                     # '@none@'

    op_semicolon    # ';'       # r'(?<!\S);(?!\S)'
    op_colon        # ':'       # r'(?<!\S):(?!\S)'
    op_eq           # '='       # r'(?<!\S)=(?!\S)'
    # (((
    op_discard      # '-'       # r'(?<!\S)[-](?=\S)(?![,)])'
    op_selected     # '+'       # r'(?<!\S)[+](?=\S)(?![,)])'
    op_unpack       # '*'       # r'(?<!\S)[*](?=\S)(?![,)])'

    # (({[
    op_multi        # '[?*+]'   # r'(?<=[\w)>\]}@])[?*+](?:(?!\S)|(?=[,)]))'



'''

