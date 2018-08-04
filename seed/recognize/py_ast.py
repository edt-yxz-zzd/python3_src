
import ast


def parse_expr(s):
    s = s.strip()
    mod = ast.parse(s)
    assert type(mod) is ast.Module
    body = mod.body
    if len(body) != 1:
        raise ValueError('none or too many statements')
    stmt, = body
    if type(stmt) is not ast.Expr:
        raise ValueError('not an expression')

    expr = stmt.value
    assert isinstance(expr, ast.expr)
    return expr


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

class Expr2Obj:
    def __init__(self, allow_types, id2obj):
        # NOTE: id2obj = {'True':True, 'False':False, ...}
        #       allow_types = {'num', 'str', ...}
        self.id2obj = id2obj
        self.allow_types = set(allow_types)
    def expr2maybe_num(self, expr):
        if type(expr) is ast.Num:
            return (expr.n,)
        return ()
    def expr2maybe_str(self, expr):
        if type(expr) is ast.Str:
            return (expr.s,)
        return ()
    def expr2maybe_bytes(self, expr):
        if type(expr) is ast.Bytes:
            return (expr.s,)
        return ()
    def expr2maybe_name(self, expr):
        if type(expr) is ast.Name:
            return (self.id2obj[expr.id],)
        return ()
    def expr2maybe_tuple(self, expr):
        if type(expr) is ast.Tuple:
            return (tuple(map(self, expr.elts)),) # elt ==>> element??
        return ()
    def expr2maybe_list(self, expr):
        if type(expr) is ast.List:
            return (list(map(self, expr.elts)),) # elt ==>> element??
        return ()
    def expr2maybe_ellipsis(self, expr):
        if type(expr) is ast.Ellipsis:
            return (...,)
        return ()
    def expr2maybe_set(self, expr):
        if type(expr) is ast.Set:
            return (set(map(self, expr.elts)),) # elt ==>> element??
        return ()
    def expr2maybe_dict(self, expr):
        if type(expr) is ast.Dict:
            return (dict(zip(map(self, expr.keys), map(self, expr.values))),)
        return ()

    def __call__(self, expr):
        for postfix in self.allow_types:
            name = 'expr2maybe_' + postfix
            to_maybe = getattr(self, name)
            maybe = to_maybe(expr)
            if maybe:
                obj, = maybe
                return obj
        else:
            raise ValueError('donot know how to convert expr to obj: {!r} not in {}'
                             .format(type(expr).__name__, self.allow_types))







                    


