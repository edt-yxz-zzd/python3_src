
#from .MyConfiguration2_yacc import ...
from . import MyConfiguration2_yacc
from .MyConfiguration2_yacc import LexerOverTerminals
from ._try_MyConfiguration2_lex import tokens, source_string
import ply.yacc

import logging
level_filename_pairs = [
    (logging.DEBUG, "parselog - xxxxxxxxxxxx - debug.txt")
    ,(logging.INFO, "parselog - xxxxxxxxxxxx - info.txt")
    ,(logging.ERROR, "parselog - xxxxxxxxxxxx - error.txt")
    ]
def parse_and_log_and_show(level, filename):
    # Set up a logging object
    print(level, filename)
    logging.basicConfig(
        level = level
        ,filename = filename
        ,filemode = "w"
        #,style='%',format = "%(filename)10s:%(lineno)4d:%(message)s"
        ,style='{',format = "{filename!r}:{lineno}:{message}"
    )
    log = logging.getLogger()

    lrparser = ply.yacc.yacc(module=MyConfiguration2_yacc
        , debug=True, debuglog=log, errorlog=log)
    lexer = LexerOverTerminals()
    result = lrparser.parse(tokens, lexer=lexer, debug=log)
    print(result)
def _f():
    for t in tokens: print(t)

    last_e = None
    for level, filename in level_filename_pairs:
        try:
            parse_and_log_and_show(level, filename)
        except Exception as e:
            last_e = e
            print(e)
            pass
    raise last_e

#_f()

def _t():
    for t in tokens: print(t)
    lrparser = ply.yacc.yacc(module=MyConfiguration2_yacc)
    lexer = LexerOverTerminals()
    result = lrparser.parse(tokens, lexer=lexer)
    print(f'result={result}')
_t()

