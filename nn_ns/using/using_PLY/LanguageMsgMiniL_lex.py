
''' see "parser design.txt" in Haskell style :: MsgMiniL

'''


from .lex_common import t_error, iter_tokens

# -< <- --> >- ; , ( ) [ ] {} -- {- -}
# why recognize () [] {}? we use "," to seperate Msg, but it may occur in a tuple, etc
# from now on, we discard "," and "( ) [ ] {}"


# -< <- --> >- ; -- {- -} Mxxx Ixxx
# regex
wrap = lambda pattern: r'(?<!\S){}(?!\S)'.format(pattern)
''' # as word first
t_IMPORT = wrap('-<')
t_EXPORTED_BY = wrap('<-')
t_OUTPUT = wrap('-->')
t_IMPORTED_BY = wrap('>-')
t_TOP_STMT_HEAD = wrap(';')
'''
# 
# t_COLON = r'\:' # using in Map # or treat a:b is an element of set {a:b}
# : - can be concat x:[] or map to {a:b}
# record: D {a = b} ==>> call D on set {"a=b"} where "a=b" is a special type
t_ignore_LINE_COMMENT = wrap('--') + '.*'
t_ignore_MLINE_COMMENT = wrap(r'\{-') + '(?:.|\s)*?' + wrap(r'-\}') # not embed???
_t_WORD = r'(?!(--|\{-|-\})(?!\S))\S+' # "afa+\af." is a word
t_ignore_SPACES = r'\s+'

reserved = dict(zip(
    '-<     <-          -->    >-          ;            '.split(),
    'IMPORT EXPORTED_BY OUTPUT IMPORTED_BY TOP_STMT_HEAD'.split()))
def t_WORD(t):
    t.type = reserved.get(t.value, 'WORD')
    if t.value[0] == 'M':
        t.type = 'MConstructor'
    elif t.value[0] == 'I':
        t.type = 'IConstructor'
    return t
t_WORD.__doc__ = _t_WORD

tokens = '''
    IMPORT
    EXPORTED_BY
    OUTPUT
    IMPORTED_BY
    TOP_STMT_HEAD
    WORD
    MConstructor
    IConstructor
'''.split()



# tokenizable, not parsable
__example = r'''
; --> Msrc a, Msrc, Msrc a b c -->
; I >- Mi, Mi a , Mi a b c
; M --> Mo, Mo a, Mo a b c
; Mimport a b -< I a b <- Mexport --> Mout, Mout a b
    -< I <- M1 -- no output
         <- M2 --> Mo
    -< I <- M1 <- M2
; Mi -< I <- M1 --> Mo, Mo, Mo a b <- M2 -> Mo -< I <- M1 <- M2
; a+b.\'~ --> (?.>-<-->-,???) ([.])
'''


def test_lexer():
    itokens = iter_tokens(__name__, __example)
    return list(itokens)


def test_lexer_error():
    'no error at all'
    src = ('''
; M{} --> a
''')
    itokens = iter_tokens(__name__, src)
    try:
        print(list(itokens))
    except Exception as e:
        try:
            assert str(e) == 'fail at line:2, column:4, lexpos:4, total:13'
        except:
            print(e)
            raise
    else:
        raise logic-error
    

test_lexer()
#test_lexer_error()


if __name__ == '__main__':
    from pprint import pprint
    pprint(test_lexer())







