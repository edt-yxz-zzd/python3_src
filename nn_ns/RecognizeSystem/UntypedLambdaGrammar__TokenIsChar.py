

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

# String
*ID =* many1_alnum_
*Spaces =* many_space
*lambda =* char_REVERSE_SOLIDUS
*dot =* char_FULL_STOP
*open =* char_LEFT_PARENTHESIS
*close =* char_RIGHT_PARENTHESIS

#@token_set@ lambda dot open close alnum_       space
#            \      .   (    )     [0-9a-zA-Z_]  \s
@token_set@ char_REVERSE_SOLIDUS char_FULL_STOP
@nullable_recognizer@ many_space
@nonnull_recognizer@ many1_alnum_
@token_set@ char_LEFT_PARENTHESIS char_RIGHT_PARENTHESIS
'''


if 0:
    recognizer = compilerRecognizeSystemGrammar.id2recognizer('kw_nullable_recognizer')
    st = ArrayStream(OffsetedArray([('keyword', '@nullable_recognizer@'), ('space1s', ' '), ('word_char', 'm')]))
    v, ts = recognizer(st)
    print(v, ts)
    recognizer = compilerRecognizeSystemGrammar.id2recognizer('kw_nonnull_recognizer')
    st = ArrayStream(OffsetedArray([('keyword', '@nonnull_recognizer@'), ('space1s', ' '), ('word_char', 'm')]))
    v, ts = recognizer(st)
    print(v, ts)
    raise

    def print_split_at(seq, pos, middle):
        print(seq[:pos])
        print(middle)
        print(seq[pos:])
    tokens = tokenize_RecognizeSystemGrammar(untyped_lambda_grammar)
    print_split_at(tokens, 482, '#'*20)
    raise

    r = _parse_recognize_system_grammar(untyped_lambda_grammar)
    print(r)





compile_result = compileRecognizeSystemGrammar__str(untyped_lambda_grammar)

class UntypedLambdaCompiler(RecognizeSystem__TokenIsChar):
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
str_err = r'\x.\y.x$'
r = compileUntypedLambda(str_K)
assert r == ('Abs', ('x', ('Abs', ('y', ('Var', 'x')))))
#rint(r)


if __name__ == '__main__':
    try:
        compileUntypedLambda(str_err)
    except Exception as e:
        print(e)
    else:
        raise logic-error


