

__all__ = '''
    untyped_lambda_grammar
    UntypedLambdaCompiler
    compileUntypedLambda
    '''.split()

from .RecognizeSystemGrammarCompiler import (
    RecognizeSystem, compileRecognizeSystemGrammar__str
    )
from .Stream_Ops import ArrayStream, OffsetedArray
untyped_lambda_grammar = r'''
# Expr = ('Abs', (String, Expr)) | ('App', (Expr, Expr)) | Var
*UntypedLambdaExpr =* -Spaces Expr -Spaces !@any@
*Expr-1 =* Apps
*Expr-2 =* Abs

# ('Apps', ([Expr], [Abs])) -> Expr
Apps = Atom/Spaces+ Spaces_Abs?

# ('Abs', (String, Expr))
Abs = -lambda -Spaces ID -Spaces -dot -Spaces Expr
*Spaces_Abs =* -Spaces Abs

# Expr
*Atom-Var =* Var
*Atom-Group =* -open -Spaces Expr -Spaces -close

# ('Var', String)
Var =* ID

# [Char] -> String
*ID =* id_char+
*Spaces =* space*
@token_set@ lambda dot open close id_char       space
#           \      .   (    )     [0-9a-zA-Z_]  \s
'''

compile_result = compileRecognizeSystemGrammar__str(untyped_lambda_grammar)

class UntypedLambdaCompiler(RecognizeSystem):
    def RS_T_lambda(self, ch):
        return ch == '\\'
    def RS_T_dot(self, ch):
        return ch == '.'
    def RS_T_open(self, ch):
        return ch == '('
    def RS_T_close(self, ch):
        return ch == ')'
    def RS_T_id_char(self, ch):
        return ch.isalnum() or ch == '_'
    def RS_T_space(self, ch):
        return ch.isspace()
    def RS_Alt2Def_ID(self, ch_ls):
        return ''.join(ch_ls)
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

str_K = r'\x.\y.x'
r = compileUntypedLambda(str_K)
assert r == ('Abs', ('x', ('Abs', ('y', ('Var', 'x')))))
#rint(r)



