r'''

character-layer: written_style
symbol-layer: language, grammar, grammar_form

tokenize: (Stream<Unit>, Range<Stream<Unit>::StreamPos>) -> Stream<Token>

parse<GrammarForm>: (Grammar<GrammarForm>, Stream<Symbol>) -> SyntaxTree<Symbol>

Token = (Symbol, Range<Stream<Unit>::StreamPos>)
Stream : {tell(), seek(pos), seek_begin(), read(n_units)}
Range<OrderedType> = (begin::OrderedType, end::OrderedType)
OrderedType : {<}
    StreamPos, SeekPos, Symbol

StreamPos = (UnitIndex, SeekPos)

RuleType = 'concat' | 'choose' | 'symbol' | 'regex' | 'tagged_name'
SyntaxTree<Symbol> = (RuleType, RuleID, ...)
    = ('choose', thisID::RuleID, None, [tree_rooted_by_AlternativeID__Tagged_or_not::SyntaxTree<Symbol>])
    = ('concat', RuleID, None, [rooted_by_SubID__Tagged_or_not::SyntaxTree]) # list for concat
    = ('symbol', symbol_in_grammar::Symbol, symbol_in_input_stream::Symbol, None) # exists __eq__(symbol_in_input_stream, symbol_in_grammar) # may not in reversed order
    = ('regex', RuleID, [Symbol], None) # allow ambiguity but ignore tree struct
    = ('tagged_name', TaggedID, (tag, OrgID), [rooted_by_OrgID::SyntaxTree])
    
    

    where
        CountedName = (CountType, Name, [SyntaxTree<Symbol>]) # list for repeat
        CountType = 'Option' | 'Star' | 'Cross' | 'None'
        Name = TopRuleID | Symbol


Grammar<GrammarForm> = Grammar__Text<GrammarForm> | Grammar__SyntaxTree<GrammarForm> | Grammar__Data<GrammarForm>


'''



# syntax_tree_node ::= (case, ID, data::T<case>, children::None | [subtree])
def get_ID(syntax_tree):
    return syntax_tree[1]

def makeSyntaxTree__Symbol(symbol_in_grammar, symbol_in_input): # leaf
    return ('symbol', symbol_in_grammar, symbol_in_input, None)

def makeSyntaxTree__Choose(rule_id, alt_name__syntax_tree):
    subtrees = [alt_name__syntax_tree]
    return ('choose', rule_id, None, subtrees)

def makeSyntaxTree__Concat(rule_id, counted_name__syntax_trees):
    subtrees = list(counted_name__syntax_trees)
    return ('concat', rule_id, None, subtrees)

def makeSyntaxTree__Regex(rule_id, symbols_in_input): # leaves
    return ('regex', rule_id, list(symbols_in_input), None)

class Make_makeSyntaxTree__Count_XXX:
    def __init__(self, count_type):
        self.count_type = count_type
    def __call__(self, tagged_name, org_name, org_name__syntax_trees):
        tag = self.count_type
        subtrees = list(org_name__syntax_trees)
        # since subtrees may be empty, (count_type, org_name) is required
        return ('tagged_name', tagged_name, (tag, org_name), subtrees)

(makeSyntaxTree__Option, makeSyntaxTree__Star, makeSyntaxTree__Cross) = \
                         map(Make_makeSyntaxTree__Count_XXX, '?*+')






    


    









