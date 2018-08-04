
from ast import parse, dump
import ast

try:
    parse('''
        1
    ''')
    # IndentationError: unexpected indent
except IndentationError: pass
else: raise ...

r = parse('''
1
    ''')
assert dump(r) == 'Module(body=[Expr(value=Num(n=1))])'

r = parse('1')
assert dump(r) == 'Module(body=[Expr(value=Num(n=1))])'
# NOTE: 'Expr' is a constructor of 'stmt', its value is 'expr'




def parse_expr(s):
    s = s.strip()
    mod = parse(s)
    if type(mod) is not ast.Module:
        raise ...
    body = mod.body
    if len(body) != 1:
        raise ValueError('none or too many statements')
    stmt, = body
    if type(stmt) is not ast.Expr:
        raise ValueError('not an expression')

    expr = stmt.value
    assert isinstance(expr, ast.expr)
    return expr


r = parse_expr('''
1
    ''')

assert dump(r) == 'Num(n=1)'
r = parse_expr('''
  True
    ''')
assert dump(r) == "Name(id='True', ctx=Load())"

print(dump(r))

def expr2maybe_num(expr):
    if type(expr) is ast.Num:
        return (expr.n,)
    return ()
def expr2maybe_str(expr):
    if type(expr) is ast.Str:
        return (expr.s,)
    return ()
def expr2maybe_name(expr):
    if type(expr) is ast.Name:
        return (expr.id,)
    return ()
def expr2maybe_tuple(expr):
    if type(expr) is ast.Tuple:
        return (expr.elts,) # elt ==>> element??
    return ()







