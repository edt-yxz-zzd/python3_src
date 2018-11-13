
'''
used by CFG_Parser__Earley
    # required by BasicEarleyParser
'''

__all__ = '''
    make_leaf_of_at
    make_nonnull_nonleaf_of_between
    make_null_nonleaf_of_at
    '''.split()

from ..CFG import explain_ref_symbol_psidx
from .ParseTreeNode import (
    ParseTreeNonleafNode
    ,ParseTreeLeafNode
    )
def make_leaf_of_at(cfg
    , token2terminal_name
    , terminal_set_idx
    , token
    , terminal_position_begin
    ):
    return ParseTreeLeafNode(
        terminal_set_idx
            =terminal_set_idx
        ,terminal_set_name
            =cfg.terminal_set_idx2terminal_set_name[terminal_set_idx]
        ,terminal_position_begin
            =terminal_position_begin
        ,terminal_position_end
            =terminal_position_begin+1
        ,terminal_name
            =token2terminal_name(token)
        ,token
            =token
        )
def make_nonnull_nonleaf_of_between(cfg
    , production_idx
    , nodes
    , terminal_position_begin
    , terminal_position_end
    ):
    nonterminal_idx=cfg.production_idx2nonterminal_idx[production_idx]
    nonterminal_name=cfg.nonterminal_idx2nonterminal_name[nonterminal_idx]
    production_name=cfg.production_idx2production_name[production_idx]
    return ParseTreeNonleafNode(
        nonterminal_idx=nonterminal_idx
        ,production_idx=production_idx
        ,nonterminal_name=nonterminal_name
        ,production_name=production_name
        ,terminal_position_begin=terminal_position_begin
        ,terminal_position_end=terminal_position_end
        ,children=tuple(nodes)
        )
def make_null_nonleaf_of_at(cfg
    , nullable_nonterminal_idx
    , terminal_position
    ):
    nonterminal_idx2maybe_one_null_tree = cfg.calc.nonterminal_idx2maybe_one_null_tree
    may = nonterminal_idx2maybe_one_null_tree[nullable_nonterminal_idx]
    if not may: raise ValueError('not nullable_nonterminal_idx')
    is_ambiguous_nullable, production_idx = may
    production_idx2idxalternative = cfg.calc.production_idx2idxalternative

    def mk_node__nonterminal_idx(nonterminal_idx):
        is_ambiguous_nullable, production_idx \
            = nonterminal_idx2maybe_one_null_tree[nonterminal_idx]
        nodes = mk_nodes__production_idx(production_idx)
        nonterminal_name = cfg.nonterminal_idx2nonterminal_name[nonterminal_idx]
        production_name = cfg.production_idx2production_name[production_idx]
        node = ParseTreeNonleafNode(
            nonterminal_idx=nonterminal_idx
            ,production_idx=production_idx
            ,nonterminal_name=nonterminal_name
            ,production_name=production_name
            ,terminal_position_begin=terminal_position
            ,terminal_position_end=terminal_position
            ,children=tuple(nodes)
            )
        return node
    def mk_nodes__production_idx(production_idx):
        # -> [node]
        idxalternative = production_idx2idxalternative[production_idx]
        nodes = []
        for ref_symbol_psidx in idxalternative:
            is_nonterminal, idx = explain_ref_symbol_psidx(ref_symbol_psidx)
            if is_nonterminal:
                nonterminal_idx = idx
                node = mk_node__nonterminal_idx(nonterminal_idx)
            else:
                terminal_set_idx = idx
                raise logic-error --nullable_nonterminal_idx is not null
            nodes.append(node)
        return nodes
    return mk_node__nonterminal_idx(nullable_nonterminal_idx)





