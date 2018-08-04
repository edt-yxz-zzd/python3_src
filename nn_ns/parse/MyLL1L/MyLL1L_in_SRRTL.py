
mainID = mainID_SRRTL_of_MyLL1L = 'MyLL1L_in_SRRTL'

MyLL1L_in_SRRTL = raw_tokenization_specification_of_MyLL1L_in_SRRTL = r'''

MyLL1L_in_SRRTL
    goto startline
startline
    indent = r'((?!\n)\s)*'
        goto endline
endline
    string = r"'(?!'')([^'\\]|\\.)*'"
    string = r'"(?!"")([^"\\]|\\.)*"'
    string = "\'''((?!\''')([^\\\\]|\\n|\\\\.|\\\\\\n))*\'''"
    string = '\"""((?!\""")([^\\\\]|\\n|\\\\.|\\\\\\n))*\"""'
    comment = '#.*'
    newlines = r'(?m)\n+'
        goto startline
    spacesButNewline = r'((?!\n)\s)+' # if at the beginning of a non-empty line -> indent
    block = '((?![\'"#])\\S)+' # merged if connected others
    

'''
