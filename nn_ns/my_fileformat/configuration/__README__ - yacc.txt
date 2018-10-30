
NOTE:
    OK:
        AAAAA : BBBBB
        AAAAA   : BBBBB
            | CCCCC
        AAAAA \
            : BBBBB
            | CCCCC
    ERROR:
        AAAAA
            : BBBBB
Note:
    D:/software/programming/Python/_compile/PLY/ply-3.11/doc/ply.html
    The use of negative indices have a special meaning in yacc;
    p[-1] is not p[len(p)-1]
    Please see the section on "Embedded Actions" for further details.
NOTE:
    LRParser: LALR
        can use "A = (A ,)* A" or "A = A (, A)*"

        NO!!!!
        @deprecated
        ???not allow two nonterminals with some same sentences???
            ??otherwise it doesnot know how to reduce/which one to reduce to.
            ??only there is a strictly longer one, to resolve the confliction.


requires:
    module.tokens
        like lex
        but if raw_tokens->tokens change like MyConfiguration2_lex
        then use new tokens
        MyConfiguration2_lex.tokens is raw_tokens
        MyConfiguration2_yacc.tokens is tokens

    module.start
        start symbol

    lexer
        .input(input)
            # I customize input from string to terminals
        .token() # get_maybe_next_token

        ### below neednot
        #.lineno
        #.lexpos

alternatives:
    A-a1 = ...
    A-a2 = ...
    A = A-a1 | A-a2

    def p_A_a1(p):
    def p_A_a2(p):

    def p_expression(p):
        '''expression : expression PLUS term
                      | expression MINUS term'''
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
    ====>>>>
    def p_expression_plus(p):
        'expression : expression PLUS term'
        p[0] = p[1] + p[3]
    def p_expression_minus(t):
        'expression : expression MINUS term'
        p[0] = p[1] - p[3]


empty and optional:
        def p_empty(p):
            'empty :'
            pass
        def p_optitem(p):
            'optitem : item'
            '        | empty'
            ...

usage:
    import ply.yacc
    parser = ply.yacc.yacc(
        method='LALR', module=None, start=None, outputdir=None)
    result = parser.parse(s)
