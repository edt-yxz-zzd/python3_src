'''
my_LL1 = my_LL1_parse_method
MyLL1L = my_LL1_language

XL_in_MyLL1L # repr of x-language of type 'text', writing in language MyLL1L
mainID_MyLL1L_of_XL = main ID in XL_in_MyLL1L

name like:
    yyy_MyLL1L_of_XL can be treated as yyy<MyLL1L, XL>
means to use tools provided by MyLL1L, to handle text in XL

to parse tokens:
    from Parser_MyLL1L_of_XL import Parser_MyLL1L_of_XL
    Parser_MyLL1L_of_XL(mainID_MyLL1L_of_XL, XL_in_MyLL1L).parse_tokens


token requirement:
    token.type exists, and it is a string
define line in XL_in_MyLL1L like:
    some_id is t'ok'
means some_id will match a token with .type=='ok'


    
    


'''

'''
SRRTL = 'state_rex_raw_tokenization_language'
a language to descript how to tokenize using rex under some state

'raw' stands it can be used as the first step of tokenization
since it is too hard to make a complete tokenization to fit all needs.

I seperate the tokenization 2 steps:
1. raw tokenize
2. user tokenize
I offer tools to ease step2:
    discard : such as spaces, comments
    merge   : one logic line from multiple physic lines
    insert  : such as indent and dedent in python
    retype  : to identify keywords or operators
these tools work like string-style functions
you need to provide a string such that each character stands for a virtual type.
one virtual type may stand for some real type.
and then you can use a regular expression to identiy substrings.

to raw tokenize:
    from RawTokenizer_SRRTL_of_XL import RawTokenizer_SRRTL_of_XL
    RawTokenizer_SRRTL_of_XL(mainID_SRRTL_of_XL, XL_in_SRRTL).raw_tokenize
    
'''

'''

decode : string <- bytes # encoding?
pos2xy : define funcion to calc line number and column number from pos
'''

'''
there are 7 steps for all the work:
0. decode
1. user: write xl_in_SRRTL
    examples:
        MyLL1L_in_SRRTL
        SRRTL_in_SRRTL
2. auto: raw tokenize
    from RawTokenizer_SRRTL_of_XL import RawTokenizer_SRRTL_of_XL
    RawTokenizer_SRRTL_of_XL(mainID_SRRTL_of_XL, XL_in_SRRTL).raw_tokenize
3. user: tokenize
    examples:
        raw2tokens_of_MyLL1L
        raw2tokens_of_SRRTL
4. user: write xl_in_MyLL1L
    examples:
        MyLL1L_in_MyLL1L
        SRRTL_in_MyLL1L
5. auto: parse
    from Parser_MyLL1L_of_XL import Parser_MyLL1L_of_XL
    Parser_MyLL1L_of_XL(mainID_MyLL1L_of_XL, XL_in_MyLL1L).parse_tokens
6. user: process parse result
    examples
        ProcessMatchResult_MyLL1L_of_MyLL1L
        ProcessMatchResult_MyLL1L_of_SRRTL


text -> raw_tokenize<mainID_SRRTL_of_XL, XL_in_SRRTL>
     -> raw_tokens_to_tokens
     -> parse_tokens<mainID_MyLL1L_of_XL, XL_in_MyLL1L>
     -> process_result
'''




