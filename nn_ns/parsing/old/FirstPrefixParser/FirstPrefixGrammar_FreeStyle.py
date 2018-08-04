
r'''
GrammarForm =
    { Operator: ConcatChooseCopyOptionStarCross
    , Priority: AvoidPreviousAlternatives
    , Greedy: OnlyLargestCount
    , TextStyle: FreeStyle
    , NameConvenience: QuoteTerminals__Option_QuoteNonterminalsByLtGt
    , LineComment: SpaceSharpSpace
    }

example:
    S = A? B* C+ D ; # concat
    A { # choose
        B
        C # <==> C and not B <==> C \ B
            # bug :
            #   should be: symbols[begin:end] does not contain a prefix that reduces to B
            # (?!B.*)C.*
        D # <==> D and not C and not B <==> D \ C \ B
    }

    B { 'b' } # copy <==> 
    C { B* } # copy, too
    D {} # no alternatives <==> D not defined


'''


grammar_in_self = ThisGrammar__FreeStyle__in__Self = '''
# grammar for ThisGrammar__FreeStyle in ThisGrammar__FreeStyle

Grammar { Rule* }
Rule {
    ConcatRule
    ChooseRule
}

ConcatRule = DefiningName '=' CountedName* ';' ;
ChooseRule = DefiningName '{' CountedName* '}' ;

CountedName = Name Count ;
Count {
    '?'
    '*'
    '+'
    Null
}
Null = ;

DefiningName { 'nonterminal' }
Name {
    'nonterminal'
    'terminal'
}


'''


from .SimpleTokenizer import SimpleTokenizer__OrderedRegexes, std__ranged_sequence, TokenizeError


                
class FirstPrefixGrammar_FreeStyle_Tokenizer:
    symbol2regex_pattern = {
        'nonterminal' : r'\w+|<([^><\s]| )*>',
        'terminal' : r"'([^'\s]| )*'",
        'keyword' : r'[=;:{}?*+]', # not a final symbol, finals are those chars
        'comment' : r'((?<=\s)|^)#( |#)[^\n]*(?=\n|$)',
        'spaces' : r'\s+',
        }

    _simple_tokenize = SimpleTokenizer__OrderedRegexes(symbol2regex_pattern.items())

    def prefix_tokenize(self, source, begin=None, end=None):
        remain_begin, symbol_range_pairs = self._simple_tokenize(source, begin, end)

        # remove comments and spaces
        def valid(symbol_range):
            sym, _ = symbol_range
            return sym not in {'comment', 'spaces'}
                
        symbol_range_pairs = filter(valid, symbol_range_pairs)


        # rename 'keyword' by value(the matched substring)
        def get_value(rng):
            (begin, end) = rng
            return source[begin:end]
        def rename_keyword(symbol_range):
            sym, rng = symbol_range
            if sym == 'keyword':
                new_name = get_value(rng)
                symbol_range = new_name, rng
            return symbol_range
        symbol_range_pairs = map(rename_keyword, symbol_range_pairs)
            

        # quote symbol as 'symbol'
        def quote(symbol_range):
            sym, rng = symbol_range
            new_name = "'" + sym + "'"
            symbol_range = new_name, rng
            return symbol_range
        symbol_range_pairs = tuple(map(quote, symbol_range_pairs))
        
        return remain_begin, symbol_range_pairs

    def __call__(self, source, begin=None, end=None):
        (source, begin, end) = std__ranged_sequence(source, begin, end)
        remain_begin, symbol_range_pairs = self.prefix_tokenize(source, begin, end)
        if remain_begin != end:
            print(remain_begin, end)
            print(source[:remain_begin])
            raise TokenizeError('incomplete tokenize : begin={}, halt={}, end={}'
                                .format(begin, remain_begin, end))
        return symbol_range_pairs
    
        

tokenize = aFirstPrefixGrammar_FreeStyle_Tokenizer = FirstPrefixGrammar_FreeStyle_Tokenizer()

_tokens = tokenize(grammar_in_self)

_symbols = tuple(sym for sym, _ in tokens)


#print(symbols)







