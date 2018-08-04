
mainID = mainID_SRRTL_of_EPL = 'EPL_in_SRRTL'

EPL_in_SRRTL = r'''
EPL_in_SRRTL
    comment = r'/\*([^\*]|\*[^/])*\*/'
        if r'(?!$|\s|\[|\])' error 'comment follows sth'
    spaces = r'\s+'
    group = r'[\]\[]'
    
    string = r"r?'(?!'')([^'\\]|\\.)*'"
        if r'(?!$|\s|\[|\])' error 'string follows sth'
    string = r'r?"(?!"")([^"\\]|\\.)*"'
        if r'(?!$|\s|\[|\])' error 'string follows sth'
    string = "r?\'''((?!\''')([^\\\\]|\\n|\\\\.|\\\\\\n))*\'''"
        if r'(?!$|\s|\[|\])' error 'string follows sth'
    string = 'r?\"""((?!\""")([^\\\\]|\\n|\\\\.|\\\\\\n))*\"""'
        if r'(?!$|\s|\[|\])' error 'string follows sth'
        
    word = r'([^\s\[\]"\'/\*]|/(?!\*)|\*(?!/))+'
        if r'(?!$|\s|\[|\])' error 'word follows sth'
        r'.*/\*.*'
            error 'word follow "/*"'
        r'.*\*/.*'
            error 'word follow "*/"'
'''


word_pattern_EPL = r'([^\s\[\]"\'/\*]|/(?!\*)|\*(?!/))+'



