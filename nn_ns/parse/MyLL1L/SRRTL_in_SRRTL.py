
mainID = mainID_SRRTL_of_SRRTL = 'SRRTL_in_SRRTL'

SRRTL_in_SRRTL = raw_tokenization_specification_of_SRRTL_in_SRRTL = r'''

SRRTL_in_SRRTL
    goto startline
startline
    indent = r'((?!\n)\s)*'
        goto endline

endline
    spaces = r'((?!\n)\s)+'
    newlines = r'(?m)\n+'
        goto startline
    comment = r'#.*'
    string = r"r?'(?!'')([^'\\]|\\.)*'" '|' r'r?"(?!"")([^"\\]|\\.)*"'
        if r'(?!$|\s)' error 'string follows sth'
    idstring = r"idr?'(?!'')([^'\\]|\\.)*'" '|' r'idr?"(?!"")([^"\\]|\\.)*"'
        if r'(?!$|\s)' error 'idstring follows sth'
    id = '((?!["' "'])\S)+"
        if r'(?!$|\s)' error 'id follows sth'
        id'=' = '='
    

'''
