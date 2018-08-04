

import re
mainID = mainID_SRRTL_of_MKUL = 'MKUL_in_SRRTL'

char_pattern = re.compile(r'[^\s()=[\]{}\'"]')
ascii_char_pattern = re.compile(r'[\x00-\xff]')
not_after_string_char_pattern = re.compile(
    r'(<<char>>|[\'"])'.format(char_pattern.pattern))


 
power_pattern = re.compile(r'([-+]?[0-9]+)')
# NOTE: match '' or '.?e?...'
positive_pattern = re.compile(r'[0-9]*(\.[0-9]*)?(e<<power>>)?'\
                              .replace('<<power>>', power_pattern.pattern))
#nonchar_pattern = re.compile(r'[\s()=[\]{}\'"]')

word_pattern_MKUL = re.compile(r'[-+.]+|[-+]?([^0-9.]|\.[^0-9])<<char>>*'\
                               .replace('<<char>>', char_pattern.pattern))

named_b_string_pattern_MKUL = re.compile(
    r'(?s)(?P<byte_esc>be|e?b?)'\
    r'\{/\$(?P<tag><<char>>*)\]'\
    r'(?P<content>.*?)'\
    r'\[(?P=tag)\$/\}(?P<tail>-?)'\
    .replace('<<char>>', char_pattern.pattern))

call_on_b_string_pattern_MKUL = re.compile(
    r'(?s)(?P<byte_esc>be|e?b?)'\
    r'\{(?P<func><<char>>*)=(?P<tag><<char>>*)(?P<rtype>\)|\])'\
    r'(?P<hashable>(?<=\)))?'\
    r'(?P<content>.*?)'\
    r'(?(hashable)\(|\[)(?P=tag)=\}'\
    .replace('<<char>>', char_pattern.pattern))

p = r'(\)|\])(?P<hashable>(?<=\)))?' r'(?(hashable)\(|\[)'
m = re.match
r = m(p, r')(')
s = m(p, r'][')

MKUL_in_SRRTL = r'''
MKUL_in_SRRTL
    spaces = r'\s+'

    # {//]...
    line_comment = r'\{//\].*'
    # {#...]
    word_comment = r'\{#<<char>>*\]'
    # {/*tag]...[tag*/}
    multi_comment = r'(?s)\{/\*(?P<tag><<char>>*)\].*?\[(?P=tag)\*/\}'
    r'\{/\*<<char>>*\]|\[<<char>>*\*/\}'
        error 'mismatch multiline comment'



    # (be|e?b?){/$tag]...[tag$/}-?
    named_string = r'(?s)(be|e?b?)\{/\$(?P<tag><<char>>*)\].*?\[(?P=tag)\$/\}-?'
        #if r'(?!$|[\s()=[\]{}])' error 'named string/bytes follows sth'
        if r'(?=<<not_after>>)' error 'named string/bytes follows sth'
        
        r'(?s)(be|e?b).+'
            named_bytes = r'\w*\{<<char>>*\]<<ascii>>*\[<<char>>*\}-?'
                named_bstr- = r'(?s).+-'
            error 'bad named bytes: not all ascii'
        named_str- = r'(?s).+-'
    
    r'(be|e?b?)\{/\$<<char>>*\]|\[<<char>>*\$/\}'
        error 'mismatch named string/bytes'

    # call with only one arg, the content text
    # prefix (be|e?b?)
    # {func=tag)...(tag=} -> hashable
    # {func=tag]...[tag=}
    call_on_string = r'(?s)(be|e?b?)\{<<char>>*=(?P<tag><<char>>*)(\)|\])(?P<hashable>(?<=\)))?.*?(?(hashable)\(|\[)(?P=tag)=\}'
        # if r'(?=<<not_after>>)' error 'call on string/bytes follows sth'
        
        r'(?s)(be|e?b).+'
            call_on_bytes = r'\w*\{<<char>>*=<<char>>*(\)|\])<<ascii>>*(\(|\[)<<char>>*=\}'
                hashable_call_on_bytes = r'(?s)\w*\{<<char>>*=<<char>>*\).+'
                nonhashable_call_on_bytes = otherwise
                error 'logic-error a'
            error 'bad call on bytes: not all ascii'
        hashable_call_on_string = r'(?s)\w*\{<<char>>*=<<char>>*\).+'
        nonhashable_call_on_string = otherwise
        error 'logic-error b'
    
    r'(be|e?b?)\{<<char>>*=<<char>>*(\)|\])|(\(|\[)<<char>>*=\}'
        error 'mismatch call on string/bytes'
    
    # call with args kwargs
    # {func[...= =...]} -> hashable
    # {func{...= =...}}
    {word[ = r'\{<<char>>+\['
    {word{ = r'\{<<char>>+\{'
    
    ]}- = r'[\]\}](?=\})'
        }- = r'\}'
        ]- = r'\]'
        
    sep = r'\{(?=\{\[)|\{\{|\{\[|\]\}|\}\}|[()=[\]{}]'
        r'\]\}|\}\}'
            error 'logic error'


    string = r"(?s)(br|r?b?)(?P<tag>\'\'\'|\"\"\"|\'|\").*?(?<!\\)(\\\\)*(?P=tag)-?"
        if r'(?=<<not_after>>)' error 'string/bytes follows sth'
        r'(?s)\w*(\'(?!\')|\"(?!\")).*(?<!\\)(\\\\)*\n.*'
            error r'single line string/bytes with nonescaped "\n"'
        r'(?s)(br|r?b).+'
            bytes = r'<<ascii>>+'
                bstr- = r'(?s).+-'
            error 'bad bytes: not all ascii'
        str- = r'(?s).+-'

    r'(br|r?b?)[\'\"]'
        error 'mismatch string/bytes'
    r'<<char>>+[\'\"]'
        error 'unknown string/bytes prefix'




    may_word = r'<<char>>+'
        if r'(?=<<not_after>>)' error 'word follows sth'
        word = r'[-+.]+|[-+]?([^0-9.]|\.[^0-9]).*'
        
        may_digit_word = r'[-+]?\.?[0-9].*'
            int = r'(?i)[-+]?([1-9][0-9]*|0+|0b[01]+|0o[0-7]+|0x[0-9a-f]+)'
            
            r'(?i)[-+]?0+[1-9][0-9]*'
                error 'bad int literal'


            float = r'(?i)[-+]?<<positive>>'
                r'(?i)[-+]*\.?(e<<power>>)?'
                    error 'logic error: should not come here'
            imag = r'(?i)[-+]?<<positive>>j'
                r'(?i)[-+]*\.?(e<<power>>)?j'
                    error 'logic error: should not come here'
            complex = r'(?i)[-+]?<<positive>>' r'[-+](<<positive>>|nan|inf)j'
                r'(?i)[-+]?\.?(e<<power>>)?' r'[-+]+<<positive>>j'
                    error 'logic error: should not come here'
                r'(?i)[-+]?<<positive>>' r'[-+]+\.?(e<<power>>)?j'
                    error 'bad complex literal: imag part broken'
            digit_word = r'[0-9].*'
                r'0(none|true|false)'
                    0none = '0none'
                    0bool = '0true|0false'
                    error 'logic-error'
                    
                0float = '0[+-]?(nan|inf)'
                0imag = '0[+-]?(nan|inf)j'
                0complex = r'(?i)0[+-]?(nan|inf)' r'[-+](<<positive>>|nan|inf)j'
                    r'(?i)0[+-]?(nan|inf)' r'[-+]+\.?(e<<power>>)?j'
                        error 'bad complex literal: imag part broken'
                error 'unknown digit_word'
            error 'unknown may_digit_word'
        error 'unknown may_word'

    if '(?!$)' error 'bad string or bytes literal'
        

'''.replace('<<char>>', char_pattern.pattern)\
.replace('<<ascii>>', ascii_char_pattern.pattern)\
.replace('<<not_after>>', not_after_string_char_pattern.pattern)\
.replace('<<positive>>', positive_pattern.pattern)\
.replace('<<power>>', power_pattern.pattern)








r'''

    string = r"(?s)(br|r?b?)(?P<tag>\'\'\'|\"\"\"|\'|\").*?(?<!\\)(\\\\)*(?P=tag)-?"
        if r'(?!$|[\s()=[\]{}])' error 'string/bytes follows sth'
        r'(?s)\w*(\'(?!\')|\"(?!\")).*(?<!\\)(\\\\)*\n.*'
            error r'single line string/bytes with nonescaped "\n"'
        r'(?s)(br|r?b).+'
            bytes = r'[\x00-\xff]+'
                bstr- = r'(?s).+-'
            error 'bad bytes: not all ascii'
        str- = r'(?s).+-'

    r'(br|r?b?)[\'\"]'
        error 'mismatch string/bytes'
        
##    string = r"(?s)r?(?P<tag>\'\'\'|\"\"\").*?(?<!\\)(\\\\)*(?P=tag)-?"
##        if r'(?!$|[\s()=[\]{}])' error 'string follows sth'
##        str- = r'(?s).+-'
##    r'r?(\'\'\'|\"\"\")'
##        error 'mismatch string'
##        
##    #string = r"r?(?P<tag>\'|\")(\\.|(?!(?P=tag)).)*(?P=tag)-?"
##    string = r"r?(?P<tag>\'|\").*?(?<!\\)(\\\\)*(?P=tag)-?"
##        if r'(?!$|[\s()=[\]{}])' error 'string follows sth'
##        str- = r'(?s).+-'
##    r'r?[\'\"]'
##        error 'mismatch string'


##    bytes = r"(?as)(br|rb|b)(?P<tag>\'\'\'|\"\"\").*?(?<!\\)(\\\\)*(?P=tag)-?"
##        if r'(?!$|[\s()=[\]{}])' error 'bytes follows sth'
##        bstr- = r'(.|\n)+-'
##    r'(br|rb|b)(\'\'\'|\"\"\")'
##        error 'mismatch bytes'
##        
##    bytes = r"(?a)(br|rb|b)(?P<tag>\'|\").*?(?<!\\)(\\\\)*(?P=tag)-?"
##        if r'(?!$|[\s()=[\]{}])' error 'bytes follows sth'
##        bstr- = r'(.|\n)+-'
##    r'(br|rb|b)[\'\"]'
##        error 'mismatch bytes'

        
##    string = r"r?'(?!'')([^'\\]|\\.)*'-?"
##        if r'(?!$|[\s()=[\]{}])' error 'string follows sth'
##        str- = r'(.|\n)+-'
##    string = r'r?"(?!"")([^"\\]|\\.)*"-?'
##        if r'(?!$|[\s()=[\]{}])' error 'string follows sth'
##        str- = r'(.|\n)+-'
##    string = "r?\'''((?!\''')([^\\\\]|\\n|\\\\.|\\\\\\n))*\'''-?"
##        if r'(?!$|[\s()=[\]{}])' error 'string follows sth'
##        str- = r'(.|\n)+-'
##    string = 'r?\"""((?!\""")([^\\\\]|\\n|\\\\.|\\\\\\n))*\"""-?'
##        if r'(?!$|[\s()=[\]{}])' error 'string follows sth'
##        str- = r'(.|\n)+-'
##    r'r?[\'"]'
##        error 'mismatch string'


    

##        
##    bytes = r"(?a)(br|rb|b)'(?!'')([^'\\]|\\.)*'-?"
##        if r'(?!$|[\s()=[\]{}])' error 'bytes follows sth'
##        bstr- = r'(.|\n)+-'
##    bytes = r'(?a)(br|rb|b)"(?!"")([^"\\]|\\.)*"-?'
##        if r'(?!$|[\s()=[\]{}])' error 'bytes follows sth'
##        bstr- = r'(.|\n)+-'
##    bytes = "(?a)(br|rb|b)\'''((?!\''')([^\\\\]|\\n|\\\\.|\\\\\\n))*\'''-?"
##        if r'(?!$|[\s()=[\]{}])' error 'bytes follows sth'
##        bstr- = r'(.|\n)+-'
##    bytes = '(?a)(br|rb|b)\"""((?!\""")([^\\\\]|\\n|\\\\.|\\\\\\n))*\"""-?'
##        if r'(?!$|[\s()=[\]{}])' error 'bytes follows sth'
##        bstr- = r'(.|\n)+-'
##    r'(br|rb|b)[\'"]'
##        error 'mismatch bytes'

'''
