
__all__ = '''
    find_valid_prefix_ends
    LeftScanIterParser    
'''.split()

from .ParserCommon import ParseError, LeftScanIterParserBase
from .LParser import LParser, box_id2rule, box_id\
     , unambiguous_flat_result2tree, cleaned

def find_valid_prefix_ends(  terminals,
                             unboxed_id2rule,
                             unboxed_main_id, *,
                             begin_pos = 0,
                             undefined_IDs_allowed=False,
                             to_clean_id2rule=True):
    parser = LeftScanIterParser(unboxed_id2rule, unboxed_main_id,
                               begin_pos = begin_pos,
                               undefined_IDs_allowed = undefined_IDs_allowed,
                               to_clean_id2rule = to_clean_id2rule
                               )
    try:
        feed_terminals(parser, terminals)
    except ParseError:
        pass
    return parser.known_valid_sentence_ends()

    
class LeftScanIterParser(LeftScanIterParserBase):
    def __init__(self, unboxed_id2rule, unboxed_main_id, *,
                 begin_pos = 0,
                 undefined_IDs_allowed=False,
                 to_clean_id2rule=True):
        boxed_id2rule = box_id2rule(unboxed_id2rule)
        boxed_main_id = box_id(unboxed_main_id)
        self.__p = LParser(boxed_id2rule, boxed_main_id,
                           begin_pos = begin_pos,
                           undefined_IDs_allowed = undefined_IDs_allowed,
                           to_clean_id2rule = to_clean_id2rule
                           )

    def feed(self, unboxed_terminal):
        p = self.__p
        boxed_terminal = box_id(unboxed_terminal)
        p.feed(boxed_terminal)

    @property
    def begin_pos(self):
        p = self.__p
        return p.begin_pos
    @property
    def pos(self):
        p = self.__p
        return p.pos
    def expected_terminals_at(self, pos=None):
        p = self.__p
        return p.expects_at(pos)
    def end_at(self, pos=None):
        p = self.__p
        main_out = p.make_main_output_id(pos)
        return main_out in p.wanted2wanted_instances[p.main_wanted]
    def is_failed(self):
        return not self.expected_terminals_at()
    def known_valid_sentence_ends(self):
        p = self.__p
        main_outs = p.wanted2wanted_instances[p.main_wanted]
        return sorted(out.end for out in main_outs)
    
    def build_flat_output_id2rule(self, pos=None):
        p = self.__p
        if not self.end_at(pos):
            return {}
        g = p.build_output_grammar_end_at(pos)
        d = p.flatten_output_grammar(g)
        return d
    def make_main_flat_output_id(self, pos=None):
        p = self.__p
        main_super_id = p.make_main_super_id(pos)
        main_flat_output_id = p.flatten_super_id(main_super_id)
        return main_flat_output_id
        
        
    def to_tree(self, pos=None):
        g = self.build_flat_output_id2rule(pos)
        main_flat_id = self.make_main_flat_output_id(pos)
        cleaned_result = cleaned(g, main_flat_id)
        return unambiguous_flat_result2tree(cleaned_result)
        
    
    
