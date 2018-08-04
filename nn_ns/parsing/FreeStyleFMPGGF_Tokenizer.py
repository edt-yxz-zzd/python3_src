
# FIXME:
#     raise_when_left_recur
#     avoid_infinite_repeat_null

r'''
FirstMatchedPrefixGrammar is not CFG
    but lots of artificial language that described by CFG can use this grammar form


FreeStyle_FMPG_GrammarForm =
    { Operator: ConcatChooseCopyOptionStarCross
    , Priority: AvoidPreviousAlternatives, RaiseWhenLeftRecur
    , Greedy: OnlyLargestCount, OnlyOneWhenInfiniteNull
        # so, "A -> 'a'* 'a'" always fails.
        #     "A -> Null* Null" matchs as [[Null], Null]
    , TextStyle: FreeStyle
    , NameConvention: [QuoteTerminals, Option_QuoteNonterminalsByLtGt]
    , LineComment: SpaceSharpSpace
    }
    why not using lower case word as terminal?
        to support language other than English/ascii, e.g. Chinese
        or pure not word character, e.g. space or operators


example:
    S = A? B* C+ D ; # concat
    A { # choose
        B
        C # error: <==> C and not B <==> C \ B
            # bug :
            #   should be: symbols[begin:end] does not contain a prefix that reduces to B
            # (?!B.*$)C.*$
            # not CFG
        D*
    }

    B { 'b' } # copy <==> 
    C { B* } # copy, too # 'B*' as a ImplicitNonterminal
    D {} # no alternatives <==> D not defined


'''



styled_grammar_for_FMPGGF_in_FreeStyleFMPGGF = r'''

# this grammar is
#      for FMPG_GrammarForm(as a symbolic_language whose sentences are symbolic_grammars)
#      in FreeStyle_FMPG_GrammarForm(as a styled_language of which this source/styled_grammar is a sentence)
#   where FMPG = FirstMatchedPrefixGrammar
#         FMPGGF = FMPG_GrammarForm

Grammar { ExplicitRule* }
ExplicitRule {
    AlternativeRule
    ConcatenateRule
}

# A = 'a' A* ;
ConcatenateRule = DefinedRuleID             # using FreeStyle:
                        'begin_concatenate' # '='
                            RuleID*
                        'end_concatenate'   # ';'
                ;

# B { 'b'* B C}
AlternativeRule = DefinedRuleID
                        'begin_alternative' # '{'
                            RuleID*
                        'end_alternative'   # '}'
                ;

# 'a', 'a'*, A, A+, B?,
RuleID { MaybeTaggedRuleID }
MaybeTaggedRuleID = PrimeRuleID UnorderedTag* CallStyleTag* ; # PrimeRuleID Tag* ;
CallStyleTag = OrderedTag UnorderedTag*

Tag {
    OrderedTag   # ? * + [x..y] >>xxx
    UnorderedTag # -xxx --yyy -xxx:zzz --yyy:zzz
}
OrderedTag {
    Iterative_OrderedTag # ? * + [x..y]
    Filter_OrderedTag # >>xxx
}
Iterative_OrderedTag {
    BuiltinIterative_OrderedTag
    UserIterative_OrderedTag
}
Filter_OrderedTag { 'filter_tag' } # >>xxx


BuiltinIterative_OrderedTag {
    'option_tag' # '?'
    'star_tag'   # '*'
    'cross_tag'  # '+'
}

# [min..max]
UserIterative_OrderedTag =  'begin_inclusive_range'
                                    MIN
                                'seperator_inside_range'
                                    MAX
                            'end_inclusive_range' ;
MIN { IntegerExpression }
MAX { IntegerExpression }


UnorderedTag {
    LocalUnorderedTag  # -xxx -xxx:zzz
    GlobalUnorderedTag # --xxx --xxx:zzz
}

# NOT implemented yet
IntegerExpression { }
LocalUnorderedTag { }
GlobalUnorderedTag { }

NoTag { Null }
Null = ;

DefinedRuleID { ExplicitNonterminal }
PrimeRuleID {
    ExplicitNonterminal  #  A   B
    ExplicitTerminal     # 'a' 'b'
}

# input symbol stream of grammar only contains ExplicitNonterminals
#     ImplicitNonterminals (e.g., A*, B? ...) will be added in compile stage
ExplicitNonterminal { 'explicit_nonterminal' }


# input symbol stream may contain implicit_terminal
#     e.g., $ (i.e. EOS, end_of_stream)
ExplicitTerminal { 'explicit_terminal' }

'''


from .SimpleTokenizer import SimpleTokenizer__OrderedRegexes, std__ranged_sequence, TokenizeError


                
class FreeStyleFMPGGF_Tokenizer:
    mid_symbol2regex_pattern = {
        'explicit_nonterminal' : r'\w+|<([^><\s]| )*>',
        'explicit_terminal' : r"'([^'\s]| )*'",
        'keyword' : r'[=;:{}?*+]', # not a final symbol, finals are those chars
        'comment' : r'((?<=\s)|^)#( |#)[^\n]*(?=\n|$)',
        'spaces' : r'\s+',
        }
    keyword_symbol_pairs_str = r'''
= begin_concatenate
; end_concatenate
{ begin_alternative
} end_alternative
? option_tag
* star_tag
+ cross_tag
'''
    keyword_symbol_ls = keyword_symbol_pairs_str.split()
    
    keyword2symbol = dict(zip(keyword_symbol_ls[::2], keyword_symbol_ls[1::2]))
    

    _simple_tokenize = SimpleTokenizer__OrderedRegexes(mid_symbol2regex_pattern.items())

    def prefix_tokenize(self, source, begin=None, end=None):
        'tokenize as long input as possible'
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
                keyword = get_value(rng)
                new_name = __class__.keyword2symbol[keyword]
                symbol_range = new_name, rng
            return symbol_range
        symbol_range_pairs = map(rename_keyword, symbol_range_pairs)
         

## if symbol is symbol, quoted version is terminal!!
##      # quote symbol as 'symbol'
##        def quote(symbol_range):
##            sym, rng = symbol_range
##            new_name = "'" + sym + "'"
##            symbol_range = new_name, rng
##            return symbol_range
##        symbol_range_pairs = tuple(map(quote, symbol_range_pairs))
        
        return remain_begin, symbol_range_pairs

    def __call__(self, source, begin=None, end=None):
        # complete tokenize; see also : prefix tokenize
        (source, begin, end) = std__ranged_sequence(source, begin, end)
        remain_begin, symbol_range_pairs = self.prefix_tokenize(source, begin, end)
        if remain_begin != end:
            print(remain_begin, end)
            print(source[:remain_begin])
            raise TokenizeError('incomplete tokenize : begin={}, halt={}, end={}'
                                .format(begin, remain_begin, end))
        return symbol_range_pairs
    

    def token2symbol(self, token):
        symbol, range = token
        return symbol

    def symbol2terminal(self, symbol):
        # quote symbol
        assert "'" not in symbol
        return "'" + symbol + "'"
        

tokenize = fsfmpggf_tokenize = aFreeStyleFMPGGF_Tokenizer_Tokenizer = \
           FreeStyleFMPGGF_Tokenizer()

grammar_in_tokens_for_FMPGGF_in_FreeStyleFMPGGF = tokenize(styled_grammar_for_FMPGGF_in_FreeStyleFMPGGF)

grammar_in_symbols_for_FMPGGF_in_FreeStyleFMPGGF = tuple(map(tokenize.token2symbol, grammar_in_tokens_for_FMPGGF_in_FreeStyleFMPGGF))
grammar_in_terminals_for_FMPGGF_in_FreeStyleFMPGGF = tuple(map(tokenize.symbol2terminal, grammar_in_symbols_for_FMPGGF_in_FreeStyleFMPGGF))
handed_grammar_for_FMPGGF_in_FreeStyleFMPGGF = [
    # tuple - concat; list - altern
    
    ]

'Grammar', ['ExplicitRule*'],
'ExplicitRule', [
    'AlternativeRule',
    'ConcatenateRule'
],

'ConcatenateRule', ('DefinedRuleID', 'begin_concatenate', 
                            'CountedName*',
                        'end_concatenate')


'AlternativeRule', ('DefinedRuleID', 'begin_alternative', 
                            'RuleID*',
                        'end_alternative')

                ;
# here..............

# 'a', 'a'*, A, A+, B?,
RuleID { MaybeTaggedRuleID }
MaybeTaggedRuleID = PrimeRuleID UnorderedTag* CallStyleTag* ; # PrimeRuleID Tag* ;
CallStyleTag = OrderedTag UnorderedTag*

Tag {
    OrderedTag   # ? * + [x..y] >>xxx
    UnorderedTag # -xxx --yyy -xxx:zzz --yyy:zzz
}
OrderedTag {
    Iterative_OrderedTag # ? * + [x..y]
    Filter_OrderedTag # >>xxx
}
Iterative_OrderedTag {
    BuiltinIterative_OrderedTag
    UserIterative_OrderedTag
}
Filter_OrderedTag { 'filter_tag' } # >>xxx


BuiltinIterative_OrderedTag {
    'option_tag' # '?'
    'star_tag'   # '*'
    'cross_tag'  # '+'
}

# [min..max]
UserIterative_OrderedTag =  'begin_inclusive_range'
                                    MIN
                                'seperator_inside_range'
                                    MAX
                            'end_inclusive_range' ;
MIN { IntegerExpression }
MAX { IntegerExpression }


UnorderedTag {
    LocalUnorderedTag  # -xxx -xxx:zzz
    GlobalUnorderedTag # --xxx --xxx:zzz
}

# NOT implemented yet
IntegerExpression { }
LocalUnorderedTag { }
GlobalUnorderedTag { }

NoTag { Null }
Null = ;

DefinedRuleID { ExplicitNonterminal }
PrimeRuleID {
    ExplicitNonterminal  #  A   B
    ExplicitTerminal     # 'a' 'b'
}

# input symbol stream of grammar only contains ExplicitNonterminals
#     ImplicitNonterminals (e.g., A*, B? ...) will be added in compile stage
ExplicitNonterminal { 'explicit_nonterminal' }


# input symbol stream may contain implicit_terminal
#     e.g., $ (i.e. EOS, end_of_stream)
ExplicitTerminal { 'explicit_terminal' }






#print(grammar_in_terminals_for_FMPGGF_in_FreeStyleFMPGGF)







