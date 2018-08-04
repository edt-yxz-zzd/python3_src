


from .ParserCommon import ParseError, LeftScanIterParserBase
from .LeftScanIterParser import LeftScanIterParser


class AbbrTextParser(LeftScanIterParserBase):
    # __AbbrSentenceType__ = ??
    
    def __init__(self, abbr_sentence_ops, id2rule, main_id):
        self.p = LeftScanIterParser(id2rule, main_id)
        self.ops = abbr_sentence_ops

    def feed(self, char):
        p = self.p
        ops = self.ops
        
        word = ops.abbr_char2word(char)
        T = ops.word2terminal(word)
        p.feed(T)
    
    @property
    def begin_pos(self):
        p = self.p
        return p.begin_pos
    @property
    def pos(self):
        p = self.p
        return p.pos
    def end_at(self, pos=None):
        'is input[begin_pos:pos] a valid sentence?'
        p = self.p
        return p.end_at(pos)
    def is_failed(self):
        'is input[begin_pos:curr_pos] not a prefix of any sentence'
        p = self.p
        return p.is_failed()
    def known_valid_sentence_ends(self):
        p = self.p
        return p.known_valid_sentence_ends()



def test__AbbrTextParser():
    
    from nn_ns.parsing.IterParser.ExprGrammar import expr_sentence_ops, ExprSentenceInForms
    from .ParserCommon import feed_terminals
    
    p = AbbrTextParser(expr_sentence_ops,
                       ExprSentenceInForms.input_id2rule,
                       ExprSentenceInForms.main_id)

    feed_terminals(p, '(x+x)')

    assert p.end_at()
    assert not p.is_failed()
    assert p.known_valid_sentence_ends() == [5]
test__AbbrTextParser()












    
    
