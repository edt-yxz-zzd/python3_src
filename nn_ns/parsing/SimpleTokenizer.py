
r'''
Token = (symbol::Text, (begin, end)::Range)

why not Token = (symbol::Text, num_chars::Uint)??
    since we may drop/ignore some tokens, ranges in [token] need not form a complete range.
    

'''


import re


def std__ranged_sequence(string, begin=None, end=None):
    if begin is None:
        begin = 0
    if end is None:
        end = len(string)

    if begin > end:
        begin = end

    return string, begin, end

class TokenizeError(ValueError):pass


class SimpleTokenizer__OrderedRegexes:
    'tokenize in the given order; forbid matching empty string'
    def __init__(self, symbol_regex_pattern_pairs):
        symbol_rex_pairs = tuple(
            (symbol, re.compile(regex_pattern))
            for symbol, regex_pattern in symbol_regex_pattern_pairs)
        self.symbol_rex_pairs = symbol_rex_pairs

    def __call__(self, source, begin=None, end=None):
        'return remain_begin, [(symbol, (begin, end))]'
        source, begin, end = std__ranged_sequence(source, begin, end)
        ls = symbol_range_pairs = list(self.iter_symbol_range_pairs(source, begin, end))
        remain_begin = begin if not ls else ls[-1][-1][-1]
        
        return remain_begin, symbol_range_pairs
    def iter_symbol_range_pairs(self, source, begin=None, end=None):
        source, begin, end = std__ranged_sequence(source, begin, end)

        pairs = self.symbol_rex_pairs
        while begin < end:
            for symbol, rex in pairs:
                m = rex.match(source, begin, end)
                if m is not None:
                    # found a new token
                    end_ = m.end()
                    if begin == end_:
                        raise TokenizeError('symbol should not matched a empty string')
                    yield (symbol, (begin, end_))
                    begin = end_
                    break
            else:
                # no new token recognized
                break

            
