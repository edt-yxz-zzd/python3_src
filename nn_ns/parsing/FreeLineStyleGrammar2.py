

eg = r'''
# comment ; till end of line

# logic line like haskell

# all Nonterminals are in form:
#     ( '(' tag ')' )* TypeConstructor (tag|arg)*...
#     ( '(' tag ')' )* variable (tag|arg)*...

#
# all 'terminal's are in form:
#     ( '(' tag ')' )* 'terminal' tag*...

# RuleID is either Nonterminal or 'terminal'

# TypeConstructor is AlternativeRuleID
# DataConstructor is ConcatenateRuleID which is not visible by other rules.
#     only Type can be refered to.


# arity?? kind??
RuleID_Arity0   = DataConstructor1 # enum
                | DataConstructor2 ArgRuleID1 'arg_terminal2' # with position-only args
                | DataConstructor3  { attribute1 :: RuleID1 # record syntax
                                    , property2 :: RuleID2
                                    , field_name3 :: RuleID3
                                    , data_member4 :: RuleID4,
                                    , gettor5 :: RuleID5}


TypeConstructor_Arity2 param_rule_id param_arity2
    = Alt1 param_rule_id
    | Alt2 { subconcat1 :: ArgRuleID1
           , subconcat2 :: param_arity2 ArgRuleID2 ArgRuleID3
           , subconcat3 :: func_arity1 param_rule_id
           }

rule_id = RuleID_Arity0
func_arity1 = TypeConstructor_Arity2 rule_id

# postfix operator has higher priority than prefix operator
#     ? * + [x..y] >>filter -tag --option
#     (f a b)? == f ? a b == (f ?) a b == ((?) f) a b == (?) f a b = (?) (f a b)







'''
