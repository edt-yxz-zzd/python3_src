

__all__ = '''
    untyped_lambda_grammar
    UntypedLambdaCompiler
    compileUntypedLambda
    '''.split()

from .RecognizeSystemGrammarCompiler import (
    RecognizeSystem, compileRecognizeSystemGrammar__str
    , compilerRecognizeSystemGrammar
    )
from .RecognizeSystem__TokenIsChar import RecognizeSystem__TokenIsChar
from .Stream_Ops import ArrayStream, OffsetedArray

from .RecognizeSystemGrammar import _parse_recognize_system_grammar, tokenize_RecognizeSystemGrammar


untyped_lambda_grammar = r'''
# UntypedLambdaExpr = Expr
*UntypedLambdaExpr =* ?@pass@ # ?@pass@ : to insert a @noise@ here
                        $$/ Expr
                        # test logical-line
                        !@any@
                        # test @predicator@
                        ?pass
                        !fail
                        # test @nullable_recognizer@
                        -many_space

# Expr = ('Abs', (String, Expr)) | ('App', (Expr, Expr)) | Var
*Expr-1 =* $$/ Apps
*Expr-2 =* $$/ Abs

# Apps = ('Apps', ([Expr], [Abs])) -->> Expr
#Apps = $$/ Atom+ Abs?
Apps = $$/
    # test '&' and '{m,}'
    -Atom{1,}& ~
    # test '{m,M}' and hex
    -Atom{1,0xF}& ~
    Atom+
    -Abs{0,1}& ~
    Abs?

# Abs = ('Abs', (String, Expr))
Abs = $$/ -lambda ID -dot Expr

# Atom = Expr
*Atom-Var =* $[ Var ]$                              # test $[ ]$
*Atom-Group =* -open $$ Expr ~ -@noise@ ~ -close    # test $$

# Var = ('Var', String)
Var =* ID

# ID = String
*ID =* many1_alnum_



#######################
# test alias
lambda == char_REVERSE_SOLIDUS
dot == char_FULL_STOP
open == char_LEFT_PARENTHESIS
close == char_RIGHT_PARENTHESIS

#######################
#@token_set@ lambda dot open close alnum_       space
#            \      .   (    )     [0-9a-zA-Z_]  \s
@nullable_recognizer@
    many_space
    none
@nonnull_recognizer@
    #many1_alnum_
    many1_space # test "many1_<char_set>"
@noise@
    # test logical-line
    many1_space
@predicator@ pass fail
@token_set@ char_REVERSE_SOLIDUS char_FULL_STOP
            char_LEFT_PARENTHESIS char_RIGHT_PARENTHESIS
            alnum_
# many1_alnum_ = [Char] -->> String
# *many1_alnum_ =* alnum_/~+ # test "~"
# many1_alnum_ = (Char, [Char]) -->> String
*many1_alnum_ = -alnum_/~none~+& ~ $$ alnum_ ~ alnum_/~* # test "~"
'''




compile_result = compileRecognizeSystemGrammar__str(untyped_lambda_grammar)

class UntypedLambdaCompiler(RecognizeSystem__TokenIsChar):
    def RS_NR_none(self, st):
        return None, st
    def RS_P_pass(self, st):
        return True
    def RS_P_fail(self, st):
        return False
    def RS_Alt2Def_many1_alnum_(self, h_ts):
        h, ts = h_ts
        return ''.join([h] + ts)
    def RS_Alt2Def_Apps(self, alt_val):
        alt_case, (apps, may_abs) = alt_val
        apps.extend(may_abs)
        if len(apps) == 1:
            [r] = apps
        else:
            r = apps[0]
            for expr in apps[1:]:
                r = ('App', (r, expr))
        return r

compilerUntypedLambda = UntypedLambdaCompiler(**compile_result)
start_symbol_recognizer =\
    compilerUntypedLambda.id2recognizer('UntypedLambdaExpr')
def compileUntypedLambda(s):
    st = ArrayStream(OffsetedArray(s))
    v, _ = start_symbol_recognizer(st)
    return v

strs = r'''
ab14234xxcv
x
\x.x
 \x.x
\ x.x
\x .x
\x. x
\x.x  
\x.\y.z
\x. \y. \z. t
(x)
 (x)
( x)
(x )
(x) 
(\x.x)
\x.(x)
\x. (x)


x y
 x y
x y  
x \x.x
x y \x.x
x \x.\y.z
(x)(\x.y)\x.y
(x) (y)
'''
strs = filter(None, strs.split('\n'))
__str2result = {' (x)': ('Var', 'x'),
     ' \\x.x': ('Abs', ('x', ('Var', 'x'))),
     ' x y': ('App', (('Var', 'x'), ('Var', 'y'))),
     '( x)': ('Var', 'x'),
     '(\\x.x)': ('Abs', ('x', ('Var', 'x'))),
     '(x )': ('Var', 'x'),
     '(x)': ('Var', 'x'),
     '(x) ': ('Var', 'x'),
     '(x) (y)': ('App', (('Var', 'x'), ('Var', 'y'))),
     '(x)(\\x.y)\\x.y': ('App',
                         (('App', (('Var', 'x')
                                  , ('Abs', ('x', ('Var', 'y'))))),
                          ('Abs', ('x', ('Var', 'y'))))),
     '\\ x.x': ('Abs', ('x', ('Var', 'x'))),
     '\\x .x': ('Abs', ('x', ('Var', 'x'))),
     '\\x. (x)': ('Abs', ('x', ('Var', 'x'))),
     '\\x. \\y. \\z. t': ('Abs',
                          ('x', ('Abs', ('y', ('Abs', ('z', ('Var', 't'))))))),
     '\\x. x': ('Abs', ('x', ('Var', 'x'))),
     '\\x.(x)': ('Abs', ('x', ('Var', 'x'))),
     '\\x.\\y.z': ('Abs', ('x', ('Abs', ('y', ('Var', 'z'))))),
     '\\x.x': ('Abs', ('x', ('Var', 'x'))),
     '\\x.x  ': ('Abs', ('x', ('Var', 'x'))),
     'ab14234xxcv': ('Var', 'ab14234xxcv'),
     'x': ('Var', 'x'),
     'x \\x.\\y.z': ('App',
                     (('Var', 'x')
                     , ('Abs', ('x', ('Abs', ('y', ('Var', 'z'))))))),
     'x \\x.x': ('App', (('Var', 'x'), ('Abs', ('x', ('Var', 'x'))))),
     'x y': ('App', (('Var', 'x'), ('Var', 'y'))),
     'x y  ': ('App', (('Var', 'x'), ('Var', 'y'))),
     'x y \\x.x': ('App',
                   (('App', (('Var', 'x'), ('Var', 'y'))),
                    ('Abs', ('x', ('Var', 'x')))))}
def __compile_strs():
    from pprint import pprint
    d = {}
    for s in strs:
        print(s)
        r = compileUntypedLambda(s)
        print(r)
        d[s] = r
        assert r == __str2result[s]
    pprint(d)

str_K = r' \ x. \y . x '
str_err = r'\x.\y.x$'
r = compileUntypedLambda(str_K)
assert r == ('Abs', ('x', ('Abs', ('y', ('Var', 'x')))))


#rint(r)


if __name__ == '__main__':
    __compile_strs()
    try:
        compileUntypedLambda(str_err)
    except Exception as e:
        if 0:
            print(e)
            print('success!!!')
        if e.max_pos == 7: pass
        else: raise
    else:
        raise logic-error


