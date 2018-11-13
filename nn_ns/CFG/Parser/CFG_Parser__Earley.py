
__all__ = '''
    CFG_Parser__Earley
    '''.split()


from ._debug_constant_ import _show_rough_size_of_BasicEarleyParser
from seed.tiny import print_err

from ..CFG import CFG
#from ._parse_CFG__Earley import _parse_CFG__Earley
from .BasicEarleyParser import BasicEarleyParser
from .CFG_ParserABC import CFG_ParserABC
from .make_node import (
    make_leaf_of_at
    ,make_nonnull_nonleaf_of_between
    ,make_null_nonleaf_of_at
    )
from .abc import override
import functools # partial

class CFG_Parser__Earley(CFG_ParserABC):
    @override
    def parse_tokens(self, __tokens):
        return _parse_CFG__Earley(
            self.cfg, __tokens
            ,start_nonterminal_idc=self.start_nonterminal_idc
            ,token2terminal_name=self.token2terminal_name
            ,find_terminal_set_idc=self.find_terminal_set_idc
            ,ambiguous_nonterminal_idc=self.ambiguous_nonterminal_idc
            )
    @override
    def parse_tokens(self, __tokens):
        calc = self.cfg.calc
        parser = BasicEarleyParser(
            production_idx2nonterminal_idx
                =calc.production_idx2nonterminal_idx
            ,production_idx2idxalternative
                =calc.production_idx2idxalternative
            ,nonterminal_idx2sorted_production_idc
                =calc.nonterminal_idx2sorted_production_idc
            ,nonterminal_idx2is_nullable
                =calc.nonterminal_idx2is_nullable
            ,start_nonterminal_idc
                =self.start_nonterminal_idc
            ,token2terminal_name
                =self.token2terminal_name
            ,terminal_set_ops
                =calc.terminal_set_ops
            ,terminal_set_idx2terminal_set
                =calc.terminal_set_idx2terminal_set
            ,nonterminal_idx2nonterminal_name
                =calc.nonterminal_idx2nonterminal_name
            ,nonterminal_idx2maybe_one_null_tree
                =calc.nonterminal_idx2maybe_one_null_tree
            )

        try:
            for _ in map(parser.feed, __tokens):pass
        except:
            for attr, obj in vars(parser).items():
                print_err(attr)
                print_err(' '*4, '=', obj)
            #for attr in dir(parser): print_err(attr, getattr(parser, attr))
            raise
        if _show_rough_size_of_BasicEarleyParser:
            print_err('_show_rough_size_of_BasicEarleyParser:on')
            print_err(parser._get_rough_size())

        cfg = self.cfg
        node = parser.extract_parse_main_tree(
            ambiguous_nonterminal_idc
                =self.ambiguous_nonterminal_idc
            ,make_leaf_of_at
                =functools.partial(make_leaf_of_at
                                    , cfg, self.token2terminal_name)
            ,make_nonnull_nonleaf_of_between
                =functools.partial(make_nonnull_nonleaf_of_between, cfg)
            ,make_null_nonleaf_of_at
                =functools.partial(make_null_nonleaf_of_at, cfg)
            )
        return node
    parse_tokens.__doc__ = CFG_ParserABC.parse_tokens.__doc__


