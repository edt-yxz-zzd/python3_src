
r"""
input:
    str2values_by_line2expr:
        str = (line newline)*
        line = empty | comment | data comment?
        data = expr
    str2valuess_by_line2exprs:
        str = (line newline)*
        line = empty | comment | data comment?
        data = expr (';' expr)* ';'?
    str2valuess_by_str2blocks_line2expr:
        str = block ('pass' newline block)*
        block = (line newline)*
        line = empty | comment | data comment?
        data = expr
    str2valuesss_by_str2blocks_line2exprs:
        str = block ('pass' newline block)*
        block = (line newline)*
        line = empty | comment | data comment?
        data = expr (';' expr)* ';'?


example:
    str2values_by_line2expr:
        s = r'''
            [1,2,4], [33,25,54]
            [3,2,5], [2, 4, 4]

            # empty line and comment are allowed
            [2,3,4,4,5], [1,2] # comment
            #'''
        input_output_pairs = str2values_by_line2expr(s)

#"""



__all__ = '''
    str2values_by_line2expr
    str2valuess_by_line2exprs
    str2valuess_by_str2blocks_line2expr
    str2valuesss_by_str2blocks_line2exprs
    '''.split()
import ast
from itertools import chain


eval_str = ast.literal_eval
def evalExpr(nodeExpr):
    assert type(nodeExpr) is ast.Expr
    return ast.literal_eval(nodeExpr.value)

assert eval('1#af') == 1




def split_by_None(may_values):
    # blocks is non-empty
    # blocks[-1] may be empty
    blocks = [[]]
    for may_value in may_values:
        if may_value is None:
            # 'None' ==>> open new block
            blocks.append([])
        else:
            value = may_value
            last_block = blocks[-1]
            last_block.append(value)
    return blocks

def str2iter_lines(s):
    for line in s.splitlines():
        line = line.strip()
        if not line or line.startswith('#'): continue
        yield line
def str2iter_parsed_lines(s):
    return map(ast.parse, str2iter_lines(s))
r = ast.parse('pass # abc') # Module(body=[Pass()])
r = ast.parse('1;2;3;') # Module(body=[Expr(value=Num(n=1)), Expr(value=Num(n=2)), Expr(value=Num(n=3))])
#r = ast.parse(';') # Error
#print(ast.dump(r))
assert evalExpr(r.body[0]) == 1



def parsed_line2exprs(parsed_line):
    return _parsed_line2exprs(parsed_line, tuple)
def parsed_line2exprs__list(parsed_line):
    return _parsed_line2exprs(parsed_line, list)
def _parsed_line2exprs(parsed_line, f):
    # line = expr*
    ls = parsed_line.body
    assert ls
    assert all(type(expr) is ast.Expr for expr in ls)
    return f(map(evalExpr, ls))
def parsed_line2may_expr1(parsed_line):
    # line = pass | expr_node
    # return None | (expr_value,)
    ls = parsed_line.body
    L = len(ls)
    if L != 1: raise logic-error
    assert L == 1
    pass_or_expr, = ls
    if type(pass_or_expr) is ast.Pass:
        return None
    expr_node = pass_or_expr
    return (evalExpr(expr_node),)

def parsed_line2may_exprs(parsed_line):
    return _parsed_line2may_exprs(parsed_line, tuple)
def parsed_line2may_exprs__list(parsed_line):
    return _parsed_line2may_exprs(parsed_line, list)
def _parsed_line2may_exprs(parsed_line, f):
    # line = pass | expr_node*
    # return None | [expr_value]
    ls = parsed_line.body
    L = len(ls)
    if L == 1:
        pass_or_expr, = ls
        if type(pass_or_expr) is ast.Pass:
            return None
    return _parsed_line2exprs(parsed_line, f)





def str2values_by_line2expr(s):
    return list(map(eval_str, str2iter_lines(s)))
assert [1, (1,2), ('1',[1])] == str2values_by_line2expr('''
    1 # 23423
    1,2

    # adsd
    '1',[1]
    ''')


def str2valuess_by_line2exprs(s):
    # line.split(';')
    return list(map(parsed_line2exprs__list, str2iter_parsed_lines(s)))
    #return list(map(parsed_line2exprs, str2iter_parsed_lines(s)))
#assert [(1,), ((1,2),), (('1',[1]),), ((1,2),2,(3,))] == str2valuess_by_line2exprs('''
assert [[1], [(1,2)], [('1',[1])], [(1,2),2,(3,)]] == str2valuess_by_line2exprs('''
    1 # 23423
    1,2

    # adsd
    '1',[1]

    1,2;2;3,
    ''')




def str2valuess_by_str2blocks_line2expr(s):
    # str.split('pass'); block.split('\n')
    may_expr1_ls = list(map(parsed_line2may_expr1, str2iter_parsed_lines(s)))
    expr1_block_ls = split_by_None(may_expr1_ls)
    return [list(chain.from_iterable(expr1_block))
            for expr1_block in expr1_block_ls]
assert [[1, (1,2)], [('1',[1])]] == str2valuess_by_str2blocks_line2expr('''
    1 # 23423
    1,2
    pass

    # adsd
    '1',[1]
    ''')



def str2valuesss_by_str2blocks_line2exprs(s):
    # str.split('pass'); block.split('\n'); line.split(';')
    #may_exprs_iter = map(parsed_line2may_exprs, str2iter_parsed_lines(s))
    may_exprs_iter = map(parsed_line2may_exprs__list, str2iter_parsed_lines(s))
    return split_by_None(may_exprs_iter)
#assert [[(1,), ((1,2),)], [(('1',[1]),), ((1,2),2,(3,))]] == str2valuesss_by_str2blocks_line2exprs('''
assert [[[1], [(1,2)]], [[('1',[1])], [(1,2),2,(3,)]]] == str2valuesss_by_str2blocks_line2exprs('''
    1 # 23423
    1,2
    pass

    # adsd
    '1',[1]

    1,2;2;3,
    ''')




