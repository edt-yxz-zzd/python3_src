3 froms:
    FSM, [Rule], regular_expression

    FSM:
        TotalState : FSM
            formal - FSM{initial :: TotalState,
                         finals :: Set TotalState,
                         error :: TotalState,
                         transition :: Map TotalState (Map Symbol TotalState)
                         }
            informal - NFSM{initials :: Set PartialState,
                            finals :: Set PartialState,
                            error :: Set PartialState, # empty_set
                            transition :: Map PartialState (Map (Maybe Symbol) (Set PartialState))
                            }
        PartialState : FA
            # esp cleaned_dfa
            formal - DFA {initial :: Maybe PartialState,
                          finals :: Set PartialState,
                          error :: Maybe PartialState, # nothing
                          transition :: Map PartialState (Map Symbol PartialState)
                          }
            informal - NDFA {initials :: Set PartialState,
                             finals :: Set PartialState,
                             error :: Set PartialState, # empty_set
                             transition :: Map PartialState (Map (Maybe Symbol) (Set PartialState))
                             }

    {initials::Set PartialState, transition::[Rule]}: # NDFA-RuleForm # a direct map into/from a NDFA
        FormalNDFARule :: (PartialState, Maybe (Maybe Symbol, PartialState))
            (a, Nothing) -> [a in finals]
            (a, Just (maybe_symbol, b)) -> "a = maybe_symbol b"
        InformalNDFARule :: (Nonterminal, [Symbol], Maybe Nonterminal)
            where PartialState = (Nonterminal, Integer)
            (a, ls, Nothing) -> [(a, len(ls)) in finals]



    regular_expression: # RE-RuleForm # using star but without recur (even tail-recur) # DAG
        BasicRe a = ReConcat [BasicRe a]
                  | ReUnion [BasicRe a]
                  | ReStar (BasicRe a)
                  | ReSymbol a
        ExtendedRe a = BasicRe a
                     | ReComplement a
                     | ReIntersect a













    
