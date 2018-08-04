
mainID = mainID_SRRTL_of_ETL = 'ETL_in_SRRTL'

ETL_in_SRRTL = r'''
ETL_in_SRRTL
    comment = r'/\*([^\*]|\*[^/])*\*/'
        if r'(?!$|\s|,)' error 'comment follows sth'
    spaces = r'\s+'
    separator = ','
    
    string = r"r?'(?!'')([^'\\]|\\.)*'"
        if r'(?!$|\s|,)' error 'string follows sth'
    string = r'r?"(?!"")([^"\\]|\\.)*"'
        if r'(?!$|\s|,)' error 'string follows sth'
    string = "r?\'''((?!\''')([^\\\\]|\\n|\\\\.|\\\\\\n))*\'''"
        if r'(?!$|\s|,)' error 'string follows sth'
    string = 'r?\"""((?!\""")([^\\\\]|\\n|\\\\.|\\\\\\n))*\"""'
        if r'(?!$|\s|,)' error 'string follows sth'
        
    word = r'([^\s,"\'/\*]|/(?!\*)|\*(?!/))+'
        if r'(?!$|\s|,)' error 'word follows sth'
        r'.*/\*.*'
            error 'word follow "/*"'
        r'.*\*/.*'
            error 'word follow "*/"'
    EOF = '$'
        return
'''

word_pattern_ETL = r'([^\s,"\'/\*]|/(?!\*)|\*(?!/))+'

