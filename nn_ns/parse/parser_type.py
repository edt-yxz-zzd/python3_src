

tokenset - abstract set;
    like charset=utf8
    __contains__(self, token_name_t) -> bool
ntokenset - abstract set; disjoint with tokenset
grammarstruct<grammarlanguages_name, tokenset, ntokenset>
    - abstract relationship of symbols;
    that is what grammars try to repr
    ntokenset is disjoint with tokenset
language_name :: str


main_ref :: token_name_t - should not in tokenset; may not in ntokenset
tokenizer<..> :: source_t -> [token_t<..>]
tokenparser<..> :: [token_t<..>] -> parse_tree_t<..>
    sourceparser<..> :: source_t -> parse_tree_t<..>
compiler<..> :: parse_tree_t<..> -> target_t
    tokenparser_compiler<..> :: parse_tree_t<..> -> tokenparser<..>
    sourceparser_compiler<..> :: parse_tree_t<..> -> sourceparser<..>
parserparser<..> :: grammar::source_t -> tokenparser<..>


tokenlanguage<language_name, main_ref, grammarstruct<..>>
    one language can have many grammarstruct in same or diff grammarlanguages
tokenparser<tokenlanguage, token_struct, parse_tree_struct>
    sourceparser<tokenlanguage, token_struct, parse_tree_struct, source_t>
compiler<parse_tree_struct, grammarstruct<..>, target_t>
    tokenparser_compiler<
        # grammar.parse_tree_t<..>
        grammar.parse_tree_struct, grammar.grammarstruct<..>,
        # target.tokenparser<..>
        target.tokenlanguage, target.token_struct, target.parse_tree_struct>
    sourceparser_compiler<
        # grammar.parse_tree_t<..>
        grammar.parse_tree_struct, grammar.grammarstruct<..>,
        # target.tokenparser<..>
        target.tokenlanguage, target.token_struct, target.parse_tree_struct,
        target.source_t>
parserparser<
    # grammar.sourceparser<..>
    grammar.tokenlanguage, grammar.token_struct, grammar.parse_tree_struct,
    grammar.source_t
    # grammar.sourceparser_compiler<..>
    #   grammar.parse_tree_t<..> included
    #   target.tokenparser<..>:
    target.tokenlanguage, target.token_struct, target.parse_tree_struct,
    target.source_t
    >

tokenizer<source_t, token_struct, tokenset>

token_struct - program data type
    i.e. token_name::str | (str, rng::(int,int)) | (str, rng, substr::str)
token_t<token_struct, tokenset> - restrict to tokenset

parse_tree_struct - program data type
    i.e.
    ParseTreeStruct1 rule_id token_t = \
         Token token_t | Rule rule_id [ParseTreeStruct1 rule_id token_t]
    ParseTreeStruct2 rule_id = \
         Token | Rule rule_id [ParseTreeStruct2 rule_id]
    ParseTreeStruct3 rule_id token_t = \
         Token token_t Rng | Rule rule_id Rng [ParseTreeStruct1 rule_id token_t]
        where Rng = (begin::int, end::int) # tokens.pos
        
parse_tree_t<parse_tree_struct, grammarstruct<..>> - restrict to grammarstruct


