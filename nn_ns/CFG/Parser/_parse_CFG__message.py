
r'''
>>> from ..CFG import CFG
>>> from ..the_py_terminal_set_ops import the_py_terminal_set_ops
>>> terminal_set_ops = the_py_terminal_set_ops
>>> terminal_set_name2terminal_set = lambda a:{a}
>>> make = lambda *args, **kwargs: CFG.make_CFG__hashable_name__less(
...     *args
...     , explain_ref_symbol_name=explain_ref_symbol_name
...     , terminal_set_ops=terminal_set_ops
...     , terminal_set_name2terminal_set=terminal_set_name2terminal_set
...     , **kwargs)
>>> __pairs = [('S', ['Ts1']), ('Ts1', ['Ts0', 't']), ('Ts0', ['Ts1']), ('Ts0', [])]

#>>> __pairs = [('S', ['t', 't'])]
#>>> __pairs = [('S', ['t'])]
>>> explain_ref_symbol_name = lambda name: (name[0].isupper(), name)
>>> cfg = make(__pairs)

>>> find_terminal_set_idc = lambda terminal_set_idx2terminal_set, terminal_name: [terminal_set_idx2terminal_set.index({terminal_name})]
>>> class t:pass
>>> token2terminal_name = lambda token: token.__name__
>>> start_nonterminal_name = 'S'
>>> start_nonterminal_idx = cfg.nonterminal_name2nonterminal_idx(start_nonterminal_name)

>>> tokens = [t]*4
>>> r = _parse_CFG__message(cfg, iter(tokens), start_nonterminal_idc=[start_nonterminal_idx], token2terminal_name=token2terminal_name, find_terminal_set_idc=find_terminal_set_idc, ambiguous_nonterminal_idc=())

'''

__all__ = '''
    _parse_CFG__message
    '''.split()


#from ..CFG import CFG, the_py_terminal_set_ops
from ._ParserMessageClosureExecutor import _ParserMessageClosureExecutor
from ..MessageClosureExecutor.show_MessageClosureExecutor import \
    show_MessageClosureExecutor
from ..MessageClosureExecutor.dynamic_sizes_of_MessageClosureExecutor \
    import dynamic_sizes_of_MessageClosureExecutor

from .errors import (
    ParseFailError
    ,NotExistsError
    ,NotTreeError
    ,NotTreeError__recur
    ,NotTreeError__ambiguous
    )
from .ParseTreeNode import ParseTreeNonleafNode, ParseTreeLeafNode
from ._debug_constant_ import _show_dynamic_sizes_of_MessageClosureExecutor


def _parse_CFG__message(__cfg, __iter_tokens, *
    , start_nonterminal_idc
    , token2terminal_name
    , find_terminal_set_idc
    , ambiguous_nonterminal_idc
    #, _show_dynamic_sizes_of_MessageClosureExecutor=False
    ):
    '''

input:
    cfg :: CFG
    start_nonterminal_idc :: {nonterminal_idx}
        nonterminal_idx of the start symbol
    token2terminal_name :: token -> terminal_name
    find_terminal_set_idc :: terminal_set_idx2terminal_set -> terminal_name -> sorted[terminal_set_idx]
    ambiguous_nonterminal_idc :: {nonterminal_idx}
        used in extract_parse_main_tree/extract_parse_local_tree
        for ambiguous nonterminal_idx:
            if match empty: then prefer the empty alternative
            else: try avoid only one child not match empty

output:
    parse_result_tree :: ParseTreeNonleafNode
        parse_result_tree.nonterminal_idx <- start_nonterminal_idc
exception:
    ParseFailError
        NotExistsError
            # parse fail
        NotTreeError
            # more than possibles or recur

'''
    e = _ParserMessageClosureExecutor(__cfg
        ,start_nonterminal_idc=start_nonterminal_idc
        ,token2terminal_name=token2terminal_name
        ,find_terminal_set_idc=find_terminal_set_idc
        ,ambiguous_nonterminal_idc=ambiguous_nonterminal_idc
        )
    try:
        e.execute_until_closure()
        if e.max_required_terminal_position != len(e.tokens):
            raise ParseFailError('start_nonterminal is dead')
        for token in __iter_tokens:
            e.feed(token)
            e.execute_until_closure()
            if e.max_required_terminal_position != len(e.tokens):
                fail_position = len(e.tokens) - 1
                assert fail_position >= 0
                raise ParseFailError(f'fail_position={fail_position}; token={token!r}')
        if _show_dynamic_sizes_of_MessageClosureExecutor:
            print('_show_dynamic_sizes_of_MessageClosureExecutor:on')
            d = dynamic_sizes_of_MessageClosureExecutor(e)
            d['tokens'] = len(e.tokens)
            print(f'dynamic_sizes_of_MessageClosureExecutor: {d}')
        return e.extract_parse_main_tree()
    except ParseFailError:
        #show_MessageClosureExecutor(e)
        raise

def _t():
    from pprint import pprint
    from ..CFG import CFG
    from ..the_py_terminal_set_ops import the_py_terminal_set_ops
    terminal_set_ops = the_py_terminal_set_ops
    terminal_set_name2terminal_set = lambda a:{a}
    make = lambda *args, **kwargs: CFG.make_CFG__hashable_name__less(
        *args
        , explain_ref_symbol_name=explain_ref_symbol_name
        , terminal_set_ops=terminal_set_ops
        , terminal_set_name2terminal_set=terminal_set_name2terminal_set
        , **kwargs)
    __pairs = [('S', ['Ts1']), ('Ts1', ['Ts0', 't']), ('Ts0', ['Ts1']), ('Ts0', [])]
    #__pairs = [('S', ['t', 't'])]
    #__pairs = [('S', ['t'])]
    explain_ref_symbol_name = lambda name: (name[0].isupper(), name)
    cfg = make(__pairs)

    find_terminal_set_idc = lambda terminal_set_idx2terminal_set, terminal_name: [terminal_set_idx2terminal_set.index({terminal_name})]
    class t:pass
    token2terminal_name = lambda token: token.__name__
    start_nonterminal_name = 'S'
    start_nonterminal_idx = cfg.nonterminal_name2nonterminal_idx(start_nonterminal_name)

    tokens = [t]*4
    r = _parse_CFG__message(cfg, iter(tokens), start_nonterminal_idc=[start_nonterminal_idx], token2terminal_name=token2terminal_name, find_terminal_set_idc=find_terminal_set_idc, ambiguous_nonterminal_idc=())
    #pprint(r)#bad#one line!
    from nn_ns.lang.reformat_py_source import easy_print_for_namedtuple
    easy_print_for_namedtuple(r, indent=' '*4, depth=0, file=None)



if __name__ == "__main__":
    _t()
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):

