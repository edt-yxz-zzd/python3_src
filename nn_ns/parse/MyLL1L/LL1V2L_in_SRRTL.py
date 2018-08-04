
mainID_SRRTL_of_LL1V2L = 'LL1V2L_in_SRRTL'

LL1V2L_in_SRRTL = raw_tokenization_specification_of_LL1V2L_in_SRRTL = r'''

LL1V2L_in_SRRTL
    newlines = '^'
        goto deleted_empty_line
deleted_empty_line
    '$'
        return
    r'((?!\n)\s)*(#.*)?(\n|$)' # I misused (?m) here
    goto startline
startline    
    # logic line continued by '\\' and ','
    del_prev_newlines = r'\s*' r'(\\\s|(?=,\s))'
        goto endline # skip indent
    
    indent = r'((?!\n)\s)*'
        goto endline
endline
    string = r"'(?!'')([^'\\]|\\.)*'"
    string = r'"(?!"")([^"\\]|\\.)*"'
    string = "\'''((?!\''')([^\\\\]|\\n|\\\\.|\\\\\\n))*\'''"
    string = '\"""((?!\""")([^\\\\]|\\n|\\\\.|\\\\\\n))*\"""'
    comment = '#.*'

    newlines = r'(?m)\n+'
        goto deleted_empty_line
        
    spacesButNewline = r'((?!\n)\s)+' # if at the beginning of a non-empty line -> indent
    block = '((?![\'"#])\\S)+' # merged if connected others
    

'''
