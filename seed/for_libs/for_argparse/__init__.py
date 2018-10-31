
__all__ = '''
    eval_to
    
    str2int
    str2bounded_int
    str2uint
    str2pint
'''.split()

#from sand.big.safe_eval import safe_eval
from seed.helper.safe_eval import safe_eval
from argparse import ArgumentTypeError


def eval_to(expr_str, type_name, convertor=None):
    try:
        obj = safe_eval(expr_str)
        return obj if convertor is None else convertor(obj)
    except Exception as e:
        raise ArgumentTypeError(
            '{!r} is not a {} expression; details: {!r}'
            .format(expr_str, type_name, e))
def str2int(expr_str):
    return eval_to(expr_str, 'integer', int)

def str2bounded_int(expr_str, *, min = None, max = None):
    i = str2int(expr_str)
    if min is not None and i < min:
        raise ArgumentTypeError('eval_to_int({!r})=={!r} < {!r}==min'
                                .format(expr_str, i, min))
    if max is not None and i > max:
        raise ArgumentTypeError('eval_to_int({!r})=={!r} > {!r}==max'
                                .format(expr_str, i, max))
    return i

def str2uint(expr_str):
    return str2bounded_int(expr_str, min=0)

def str2pint(expr_str):
    return str2bounded_int(expr_str, min=1)
