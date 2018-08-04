
class ParseError(Exception):pass

class IterParserBase:
    def feed(self, terminal):
        raise NotImplementedError


def feed_terminals(iterparser, terminals):
    assert isinstance(iterparser, IterParserBase)
    for T in terminals:
        iterparser.feed(T)



def is_valid_pos(aLeftScanIterParser, pos):
    self = aLeftScanIterParser
    assert isinstance(self, LeftScanIterParserBase)
    return self.begin_pos <= pos <= self.pos

def std_pos(aLeftScanIterParser, pos):
    self = aLeftScanIterParser
    if pos is None:
        pos = self.pos

    if not is_valid_pos(self, pos):
        raise ValueError('not a valid pos')
    return pos

class LeftScanIterParserBase(IterParserBase):
    @property
    def begin_pos(self):
        raise NotImplementedError
    @property
    def pos(self):
        'curr_pos'
        raise NotImplementedError
    def end_at(self, pos=None):
        'is input[begin_pos:pos] a valid sentence?'
        pos = std_pos(pos)
        return pos in self.known_valid_sentence_ends()
    def is_failed(self):
        'is input[begin_pos:curr_pos] not a prefix of any sentence'
        raise NotImplementedError
    def known_valid_sentence_ends(self):
        'return a sorted list'
        raise NotImplementedError


