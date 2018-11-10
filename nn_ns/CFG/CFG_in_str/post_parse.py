

'''
after .make_CFG
we are to parse text in that CFG
'''

__all__ = '''
    post_parse
    '''.split()


from ..Parser.parse_CFG import parse_CFG
from ..Parser.eval_parse_result_node import eval_parse_result_node
from ..errors import ParseBaseError
from .make_CFG import make_CFG_ex
from .abstract_syntax_datatype import (
    collect_filter_names, collect_filter_ex_names)

def post_parse(__iter_tokens, *
    , start_nonterminal_idc
    , token2terminal_name
    , find_terminal_set_idc
    , ambiguous_nonterminal_idc

    , cfg
    , production_name2production

    , token2value
    , filter_name2func
    , filter_ex_name2func
    ):
    '''

input:
    # input of parse_CFG
        tokens
        start_nonterminal_idc
        token2terminal_name
        find_terminal_set_idc
        ambiguous_nonterminal_idc

    # result of make_CFG_ex
        cfg
        production_name2production

    # input of eval_parse_result_node
        token2value

    # input of Production.eval
        filter_name2func
        filter_ex_name2func
output:
    value
        from filter_name2func/filter_ex_name2func/default filter
'''
    production_names = set(cfg.production_idx2production_name)
    undefined_production_names = production_names - set(production_name2production)
    if undefined_production_names:
        raise ParseBaseError(f'undefined_production_names: {undefined_production_names}')


    productions = {
            production_name2production[production_name]
            for production_name in production_names
            }
    filter_names = collect_filter_names(productions)
    filter_ex_names = collect_filter_ex_names(productions)

    undefined_filter_names = set(filter_names) - set(filter_name2func)
    undefined_filter_ex_names = set(filter_ex_names) - set(filter_ex_name2func)
    if undefined_filter_names:
        raise ParseBaseError(f'undefined_filter_names: {undefined_filter_names}')
    if undefined_filter_ex_names:
        raise ParseBaseError(f'undefined_filter_ex_names: {undefined_filter_ex_names}')




    tree = parse_CFG(cfg, __iter_tokens
            , start_nonterminal_idc=start_nonterminal_idc
            , token2terminal_name=token2terminal_name
            , find_terminal_set_idc=find_terminal_set_idc
            , ambiguous_nonterminal_idc=ambiguous_nonterminal_idc
            )

    production_idx2reduction = make_production_idx2reduction(
        production_idx2production_name=cfg.production_idx2production_name
        ,production_name2production=production_name2production
        ,filter_name2func=filter_name2func
        ,filter_ex_name2func=filter_ex_name2func
        )

    value = eval_parse_result_node(
            node=tree
            , cfg=cfg
            , token2value=token2value
            , production_idx2reduction=production_idx2reduction
            )
    return value



def make_production_idx2reduction(*
    ,production_idx2production_name
    ,production_name2production
    ,filter_name2func
    ,filter_ex_name2func
    ):
    production_idx2reduction = []
    for production_idx, production_name in enumerate(
        production_idx2production_name
        ):
        # production :: Production
        production = production_name2production[production_name]
        reduction = make_production_reduction(
            production=production
            ,filter_name2func=filter_name2func
            ,filter_ex_name2func=filter_ex_name2func
            )
        production_idx2reduction.append(reduction)
    return production_idx2reduction

class LazyValue:
    def __init__(self, value):
        self.value = value
    def __call__(self):
        return self.value

class ProductionReduction:
    def __init__(self, *
        ,production
        ,filter_name2func
        ,filter_ex_name2func
        ):
        self.production = production
        self.filter_name2func = filter_name2func
        self.filter_ex_name2func = filter_ex_name2func

    def __call__(self, child_values):
        # -> value
        child_lazy_values = tuple(map(LazyValue, child_values))
        return self.production.eval(
                self.filter_name2func
                ,self.filter_ex_name2func
                ,child_lazy_values
                )

make_production_reduction = ProductionReduction

if __name__ == "__main__":
    from ..the_py_terminal_set_ops import the_py_terminal_set_ops
    from .parse__more_simplified_version__ver2 import \
        parse__more_simplified_version__ver2

    grammar_in_more_simplified = r'''
        ; to_unit$
            S : +Ts1
        ; lnk2list$ to_unit$
            Ts1 : +lnk_Ts1
        ; lnk_Ts1 : +lnk_Ts0 +t
        ; to_unit$
            lnk_Ts0 : +lnk_Ts1
        ; lnk_Ts0 :
        ; @terminal_set@ t
        '''

    terminal_set_name2terminal_set=lambda a:{a}
    start_nonterminal_names={'S'}

    (cfg, production_name2production
    , filter_names, filter_ex_names
    , start_nonterminal_idc, ambiguous_nonterminal_idc
    ) = parse__more_simplified_version__ver2(
            grammar_in_more_simplified
            ,terminal_set_ops=the_py_terminal_set_ops
            ,terminal_set_name2terminal_set=terminal_set_name2terminal_set
            ,start_nonterminal_names=start_nonterminal_names
            ,ambiguous_nonterminal_names=()
            ,maybedead_nonterminal_names=()
            )
    assert start_nonterminal_idc

    def to_unit(ls):
        [a] = ls
        return a
    def lnk2list(lnk):
        ls = []
        while lnk:
            lnk, last = lnk
            ls.append(last)
        ls.reverse()
        return ls

    tokens = 't'*6
    token2terminal_name=lambda t:t
    find_terminal_set_idc=lambda ls, t: [ls.index({t})]
    token2value = lambda t: 'o'
    filter_name2func = {
        'to_unit$' : to_unit
        ,'lnk2list$' : lnk2list
        }
    filter_ex_name2func = {}

    value = post_parse(tokens
        , start_nonterminal_idc=start_nonterminal_idc
        , token2terminal_name=token2terminal_name
        , find_terminal_set_idc=find_terminal_set_idc
        , ambiguous_nonterminal_idc=ambiguous_nonterminal_idc

        , cfg=cfg
        , production_name2production=production_name2production

        , token2value=token2value
        , filter_name2func=filter_name2func
        , filter_ex_name2func=filter_ex_name2func
        )
    print(value)
    assert value == ['o', 'o', 'o', 'o', 'o', 'o']

