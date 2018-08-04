
'''
GrammarTNSA:
    TNSA - T:terminal; N:null sequence; S:nonempty sequence; A:alternative
    start_symbol :: a
    terminals :: Set a
    null_nonterminals :: Set a
    seq_nonterminal2right_part :: Map a [a]
    alt_nonterminal2units :: Map a (Set a)
GrammarB:
    B - BNF-style
    start_symbol :: a
    terminals :: Set a
    nonterminal2right_parts :: Map a (Set [a])

GrammarNew_Old:
    # a - original symbol
    # s - state

GrammarOUT_???:
    # output grammar of Earley
GrammarOUT_TNSA: 
    start_symbols :: Set (a, s, s)
    terminals :: Set (a, s, s)
    null_nonterminals :: Set (a, s, s)
    outseq_nonterminal2right_part :: Map (a, [s]) [(a, s, s)]
    altseq_nonterminal2units :: Map (a, s, s) (Set (a, [s]))
    altalt_nonterminal2units :: Map (a, s, s) (Set (a, s, s))

GrammarOUT_B:
    start_symbol :: (a, s, s)
    terminals :: Set (a, s, s)
    nonterminal2right_parts :: Map (a, s, s) (Set [(a, s, s)])

GrammarTNSA_B: # TNSA from B
    start_symbol :: (a, 0)
    terminals :: Set (a, 0)
    null_nonterminals :: Set (a, i)
    seq_nonterminal2right_part :: Map (a, i) [(a, 0)]
    alt_nonterminal2units :: Map (a, 0) (Set (a, i))



usage:
    (GrammarB, tokens) -> GrammarOUT_B:
        GrammarB -> GrammarTNSA_B
        EarleyOnNDFA__TNSA(GrammarTNSA_B)(tokens) -> GrammarOUT_TNSA_B
        GrammarOUT_TNSA_B -> GrammarOUT_B
'''

symbol_B2TNSA = lambda a: (a, 0)
def box_symbol_B2TNSA(start_symbol_B):
    return symbol_B2TNSA(start_symbol_B)
def box_terminals_B2TNSA(terminals_B):
    terminals_TNSA = set(map(symbol_B2TNSA, terminals_B))
    return terminals_TNSA

def box_GrammarB_to_GrammarTNSA(start_symbol_B, terminals_B, nonterminal2right_parts_B):
    'symbol_B -> (symbol, 0)_TNSA'

    start_symbol_TNSA = box_symbol_B2TNSA(start_symbol_B)
    terminals_TNSA = box_terminals_B2TNSA(terminals_B)
    
    (null_nonterminals_TNSA,
     seq_nonterminal2right_part_TNSA,
     alt_nonterminal2units_TNSA) = box_nonterminal2right_parts_B2TNSA(nonterminal2right_parts_B)
    
    return (start_symbol_TNSA,
            terminals_TNSA,
            null_nonterminals_TNSA,
            seq_nonterminal2right_part_TNSA,
            alt_nonterminal2units_TNSA)
    
def box_nonterminal2right_parts_B2TNSA(nonterminal2right_parts_B):
    null_nonterminals_TNSA = set()
    seq_nonterminal2right_part_TNSA = {}
    alt_nonterminal2units_TNSA = {}

    for nonterminal_B, right_parts_B in nonterminal2right_parts_B.items():
        alt_TNSA = symbol_B2TNSA(nonterminal_B)
        alt_nonterminal2units_TNSA[alt_TNSA] = \
            frozenset((nonterminal_B, i) for i in range(1, 1+len(right_parts_B)))
        
        for i, right_part_B in enumerate(right_parts_B, 1):
            seq_TNSA = nonterminal_B, i
            if not right_part_B:
                null_nonterminals_TNSA.add(seq_TNSA)
            else:
                seq_nonterminal2right_part_TNSA[seq_TNSA] = \
                    tuple(map(symbol_B2TNSA, right_part_B))
        
    return (null_nonterminals_TNSA,
            seq_nonterminal2right_part_TNSA,
            alt_nonterminal2units_TNSA)


def unbox_altalt_OUT_TNSA_B2OUT_B(altalt_nonterminal):
    (a, _0), begin, end = altalt_nonterminal
    assert _0 == 0
    return (a, begin, end)
unbox_terminal_OUT_TNSA_B2OUT_B = unbox_altalt_OUT_TNSA_B2OUT_B
def unbox_altseq_OUT_TNSA_B2OUT_B(altseq_nonterminal):
    (a, _i), begin, end = altseq_nonterminal
    assert _i > 0
    return (a, begin, end)
unbox_outnull_OUT_TNSA_B2OUT_B = unbox_altseq_OUT_TNSA_B2OUT_B
def unbox_outseq_OUT_TNSA_B2OUT_B(outseq_nonterminal):
    (a, _i), states) = outseq_nonterminal
    assert _i > 0
    assert len(states) > 1
    begin = states[0]
    end = states[-1]
    return (a, begin, end)


def unbox_start_symbols_OUT_TNSA_B2OUT_B(start_symbols):
    return set(map(unbox_altalt_OUT_TNSA_B2OUT_B, start_symbols))
def unbox_terminals_OUT_TNSA_B2OUT_B(terminals):
    return set(map(unbox_terminal_OUT_TNSA_B2OUT_B, terminals))
def unbox_rules_OUT_TNSA_B2OUT_B(null_nonterminals,
                                 outseq_nonterminal2right_part,
                                 altseq_nonterminal2units,
                                 altalt_nonterminal2units):

    symbol2right_parts = {unbox_altalt_OUT_TNSA_B2OUT_B(altalt) : set()
                          for altalt in altalt_nonterminal2units}

    for outnull in null_nonterminals:
        symbol = unbox_outnull_OUT_TNSA_B2OUT_B(outnull)
        symbol2right_parts[symbol].add(())
        
    for outseq, altalts in outseq_nonterminal2right_part.items():
        symbol = unbox_outseq_OUT_TNSA_B2OUT_B(outseq)
        symbol2right_parts[symbol].add(tuple(map(unbox_altalt_OUT_TNSA_B2OUT_B, altalts)))
        
    # for altseq, outseqs in altseq_nonterminal2units.items():
    # for altalt, altseqs/outnulls in altalt_nonterminal2units.items():

    return symbol2right_parts











