################ parts of MyConfiguration2_lex.py
    0 define 'tokens' 'states'
    1 utils:
        make_Pattern... # which has been moved out
    2 define patterns
    3 define token actions
    4 define token value parsers
        parse_Inline_CharString... # which has been moved out
    5 tokens filter
        extract indents from big_newlines

#################
D:/software/programming/Python/_compile/PLY/ply-3.11/doc/ply.html
    re.VERBOSE
        Patterns are compiled using the re.VERBOSE flag
        lexer = ply.lex.lex(reflags=re.VERBOSE)

        r'[ ][#]'
        r'\ \x20\#'

    @TOKEN
        # ==>> t_XXX.__doc__ = regex_pattern
        @TOKEN(regex_pattern)
        def t_XXX(token):
            ...

    clone
        newlexer = lexer.clone()
        # the clone allows a different set of input text to be supplied which may be processed separately.

        lexer.input(string0)
        newlexer = lexer.clone()
        lexer.input(string1)
        newlexer.input(string2)

    property
        lexer.lineno
            # user should update it by himself
        lexer.lexpos
            # end of last token
            # begin of next token
            # == next_token.lexpos
            # == last_token.lexpos + len(last_token.value)
        lexer.lexdata
            # whole input string
        lexer.lexmatch
            # re.match() for last_token

        ############basic used in ply.yacc
        token.type
        token.value
        ###########extended from ply.lex
        token.lexpos
        token.lineno
        ###
        token.lexer
            lexdata is needed to product columnno

    handle state
        token.lexer.begin(state) # jump to
        token.lexer.push_state(state)
        token.lexer.pop_state()

    t_error(token)
    t_state_error(token)
        #token.value == remain_string
        token.value == token.lexer.lexdata[token.lexpos:]


#################
################ see: "state - inclusive exclusive.txt"
################ state - inclusive/exclusive
## search "flex   start condition":
http://dinosaur.compilertools.net/flex/flex_11.html
    Start conditions are declared in the definitions (first) section of the input using unindented lines beginning with either `%s' or `%x' followed by a list of names. The former declares inclusive start conditions, the latter exclusive start conditions. A start condition is activated using the BEGIN action. Until the next BEGIN action is executed, rules with the given start condition will be active and rules with other start conditions will be inactive. If the start condition is inclusive, then rules with no start conditions at all will also be active. If it is exclusive, then only rules qualified with the start condition will be active. A set of rules contingent on the same exclusive start condition describe a scanner which is independent of any of the other rules in the flex input. Because of this, exclusive start conditions make it easy to specify "mini-scanners" which scan portions of the input that are syntactically different from the rest (e.g., comments).

