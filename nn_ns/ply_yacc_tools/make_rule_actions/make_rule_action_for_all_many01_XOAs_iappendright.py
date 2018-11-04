
__all__ = '''
    make_rule_action_for_all_many01_XOAs_iappendright
    basic_make_rule_action_for_all_many01_XOAs_iappendright
    '''.split()

from .imports import set_attrs
from .parse_triples_in_str import parse_triples_in_str
from .make_rule_inject_to import make_rule_inject_to
from .handle_rule_many01 import (
    handle_many1_iappendright
    ,handle_many0_iappendright
    ,handle_empty_iappendright
    )


def make_rule_action_for_all_many01_XOAs_iappendright(
    locals, empty_name:str, triples_in_str:str, *, inject_empty_rule=True
    ):
    r'''
X - + plus
O - 0 * star
A - 'a'/'an' one element
    # always A* = A+ | Empty
    XOA
        X = O A
        A+ = A* A
    XAO
        X = A O
        A+ = A A*
many01
    means output two Nonterminals: A+ A*
        0 - A*
        1 - A+

input:
    locals:
        class XXX:
            make_rule_action_for_all_many01_XOAs_iappendright(locals(), ...)
    empty_name:
        e.g. 'Empty_iappendright'
    triples_in_str:
        e.g.
            """
                Rules1 Rules0 Rule
                Lines1 Lines0 Line
            """


usage:
make_rule_action_for_all_many01_XOAs_iappendright(
    locals
    , 'Empty_iappendright'
    , """
    ...
    Rules1 Rules0 Rule
    ...
    """
    , inject_empty_rule=True
    )
==>>
    inject_to = make_rule_inject_to(locals())
    ...
    @inject_to
    def p_(p):
        r'Rules1 : Rules0 Rule'
        handle_many1_iappendright(p)
    @inject_to
    def p_(p):
        r'Rules0 : Rules1 | Empty_iappendright'
        handle_many0_iappendright(p)
    @inject_to
    def p_(p):
        r'Empty_iappendright :'
        handle_empty_iappendright(p)
    ...
'''
    inject_to = make_rule_inject_to(locals); del locals
    triples = parse_triples_in_str(triples_in_str)
    return basic_make_rule_action_for_all_many01_XOAs_iappendright(
        inject_to, empty_name, triples
        , inject_empty_rule=inject_empty_rule
        )
def basic_make_rule_action_for_all_many01_XOAs_iappendright(
    inject_to, empty_name:str, triples:str, *, inject_empty_rule=True
    ):

    if inject_empty_rule:
        empty_rule = f'{empty_name} : '
        @inject_to
        @set_attrs(__doc__=empty_rule)
        def p_(p, *, f=handle_empty_iappendright):
            f(p)

    for xs1, xs0, x in triples:
        xs1_rule = f'{xs1} : {xs0} {x}'
        xs0_rule = f'{xs0} : {xs1} | {empty_name}'
        @inject_to
        @set_attrs(__doc__=xs1_rule)
        def p_(p, *, f=handle_many1_iappendright):
            f(p)
        @inject_to
        @set_attrs(__doc__=xs0_rule)
        def p_(p, *, f=handle_many0_iappendright):
            f(p)
    return
'''
class _Handler:
    def __init__(self, f, *args):
        self.f = f
        self.args = args
    def __call__(self, inject_to, rule_str):
        @inject_to
        @set_attrs(__doc__=rule_str)
        def p_(p):
            self.f(p, *args)
        del inject_to, rule_str
_handle_many0_iappendright = _Handler(handle_many0_iappendright)
_handle_many1_iappendright = _Handler(handle_many1_iappendright)
_handle_empty_iappendright = _Handler(handle_empty_iappendright)
'''
