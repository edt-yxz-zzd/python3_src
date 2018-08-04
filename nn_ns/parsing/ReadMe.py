
# NOTE : a 'grammar' itself is a sentence of language 'grammar_form'
# NOTE : terminal is not symbol but styled_symbol
# NOTE : explicit_terminals instead of terminals form the styled_alphabet.
#        explicit_symbols instead of symbols form the alphabet.


# why using builtin-types instead of new classes??
#     more obvious but hard to update
#     to fix prevous ??problem??, use TypeClassFuncs
#        i.e. assume we donot know the concrete type and
#             handle the object via typeclass_funcs

a language can have different grammars for a grammar_form

styled_sentence = text
symbolic_sentence = [terminal]
language = {symbolic_sentence}

tokenize : styled_sentence -> [token]
symbolize : styled_sentence -> symbolic_sentence
parse : symbolic_sentence -> syntax_tree

# grammar forms:
styled_grammar :: Text # 'A -> a B\nB -> b'
grammar_in_tokens :: [Token] # [('Nonterminal', (0,1)), ('->', (2,4)), ('Terminal', (5,6)), ('Nonterminal', (7,8)), ('RuleEnd', (8, 9)), ('Nonterminal', (9,10)), ('->', (11, 13)), ('Terminal', (14,15)), ('RuleEnd', (15,15))]
symbolic_grammar :: [Symbol] # ['Nonterminal', '->', 'Terminal', 'Nonterminal', 'RuleEnd', 'Nonterminal', '->', 'Terminal', 'RuleEnd', ]
grammar_in_terminals :: [Terminal] # ...
grammar_in_syntax_tree :: SyntaxTree # ...
grammar_in_rules :: [Rule] # [Rule('A', ['a', 'B']), Rule('B', ['b'])]
handed_grammar :: ?? # ['A', ['a', 'B'], 'B', ['b']]



to parse styled_sentence, we need:
    # Text/Token/Symbol : text/token/symbol type in program language
    # Symbol/Terminal is Text
    tokenize<language_info, sentence_style> :: Text -> [Token]
        # sentence_style ==>> using FreeStyle or IndentStyle ...
        # language ==>> alphabet i.e. {symbol}
    token2symbol : Token -> Symbol
    symbol2terminal<grammar_style> : Symbol -> Terminal
        # symbol may be "a" but grammar_style require it to be "'a'"
        # symbol may be "indent" but rename it to be "'{'"
    parse<grammar_form_info, grammar_style, grammar> : [terminal] -> syntax_tree
        call compile :: styled_grammar -> grammar_in_rules
            styled_grammar -> grammar_in_tokens
                           -> symbolic_grammar
                           -> grammar_in_syntax_tree
                           -> grammar_in_rules
            grammar_in_rules -> working_data :: ??




# why not Token = (symbol::Text, num_chars::Uint)??
#     since we may drop/ignore some tokens, ranges in [token] need not form a complete range.
Token = (symbol::Text, (begin, end)::Range)




RuleID = Terminal | Nonterminal

    # Terminal <= RegexID <= FlatRuleID
    = FlatRuleID | StructRuleID

    
    # A vs A*, A[1..4], A -del, A --
    # so, RuleID may not be Text, can be quite complex
    = PrimeRuleID | TaggedRuleID 

    # A >> tag, A[x..y] vs A -tag, A --tag
    TaggedRuleID = OrderedTaggedRuleID | UnorderedTaggedRuleID

    # A?, A*, A+, A[x..y], A[x] vs A >> tag
    OrderedTaggedRuleID = BuiltinOrderedTaggedRuleID | UserOrderedTaggedRuleID

    # A -tag vs A --tag
    #   A[3] -t1 -t2 [2] <==> A[3] -t2 -t1 [2] but not A[3] -t1 [2] -t2
    #   A[3] --t1 --t2 [2] <==> A[3] --t2 --t1 [2] <==> A[3] --t1 [2] --t2
    UnorderedTaggedRuleID = LocalUnorderedTaggedRuleID | GlobalUnorderedTaggedRuleID
    BuiltinGlobalUnorderedTaggedRuleID # A --

# why not using Range instead of NumTerminals??
#     for CFG, we can reuse one syntax_tree for same substrings.
SyntaxTree = (RuleID, [SyntaxTree] | num_terminals::Uint)
    = (FlatRuleID, NumTerminals) | (StructRuleID, [SyntaxTree])
Grammar = [ExplicitRule]
Nonterminal = ExplicitNonterminal | ImplicitNonterminal
    # ExplicitRule "A -> a A*" ==>> ImplicitRule "A* -> A[0..]" and "A[0..]" and "a"
    #    'A' is an ExplicitNonterminal;
    #    'A*' and 'A[0..]' are ImplicitNonterminal
    #    'A*' ==>> AlternativeRule('A*', ['A[0..]'])
    #    'A[0..]' ==>> IterativeRule('A', min=0, max=None)
    #    # ignore 'a' ==>> TerminalRule('a')
Terminal = ExplicitTerminal | ImplicitTerminal
    # ImplicitTerminal : $ == end-of-stream ...



howto handle syntax tree?
    is_terminal :: RuleID -> Bool # <==> alphabet
    get_terminal :: Token -> Terminal
    is_flat_rule_type :: RuleType -> Bool
    # get_num_terminals
    # get_children

    nonterminal2rule :: dict<nonterminal, rule>
    nonterminal2extra_info :: dict<nonterminal, extra_info>

    parse_rule_ID :: RuleID -> (PrimeRuleID, SortedLocalUnorderedTags), [(OrderedTag, SortedLocalUnorderedTags)], SortedGlobalTags

    post_evaluate: 
        rule_id = get_rule_id(curr_node)
        rule = nonterminal2rule[rule_id]
        rule_type = get_rule_type(rule)

        if is_flat_rule_type(rule_type):
            size = get_num_terminals(curr_node)
            subvalues = tokens[begin:begin+size]
        else:
            subtrees = get_children(curr_node)
            subvalues = [post_evaluate(t) for t in subtrees]

        mid_result = synthesize_by_rule_type(rule_type, subvalues)
        return synthesize_by_rule_id(rule_id, mid_result)
        
        
Rule:
    AlternativeRule(RuleID, alternatives::[RuleID])
    ConcatenateRule(RuleID, subIDs::[RuleID])
    IterativeRule(RuleID, basicID::RuleID, min::Uint, max::Uint|None)
        # priority
        IntegerExpression = IntAtom | PostfixUnaryOp | (CurryCall | PrefixUnaryOp) | InfixBinaryOp
        IntAtom = IntLiteral
                | '(' + IntegerExpression + ')'
                | '[' + BoolExpression + ']'
                | 'c_func(args...)' # NOTE: not 'c_func (args...)'
                # not atom : | 'curry_func args...'
                | ... 'sum f(i) {i in set...}'
                | 
    TaggedRule(RuleID, basicID::RuleID, tag)













