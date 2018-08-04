

from .GrammarETSA_def import GrammarETSA_in_GrammarETSA

# EFS - E:Extended; FS:finite state ==>> regular language
GrammarEFS_in_GrammarETSA = '''
# first rule defined the start symbol

@start_symbol GrammarEFS
@terminals {
    at_start_states # @start_states
    seq_begin       # =
    seq_end         # ;
    alt_begin       # {
    alt_end         # }
    symbol          # r"\w+"
    star            # * 
    cross           # +
    option          # ?
    group_begin     # (
    group_end       # )
    union           # |
    ugroup_begin    # [
    ugroup_end      # ]
}


GrammarEFS { Statement* }

Statement {
    ImportTerminals
    DefineRegularExpression
}

ImportTerminals = at_terminals alt_begin Terminal* alt_end ;
DefineRegularExpression = Nonterminal seq_begin Regex seq_end ;
Regex { Either_UnionRE_ConcatRE }


AtomRE {
    UnionEMarkRE
    GroupRE
    Terminal
    NotYetDefinedNonterminal
}
Either_MarkRE_AtomRE {
    MarkRE
    AtomRE
}

EMarkREs { Either_MarkRE_AtomRE* } 
ConcatRE { EMarkREs }

Either_UnionRE_ConcatRE {
    UnionRE
    ConcatRE
}

UnionRE = ConcatRE union Either_UnionRE_ConcatRE ;
MarkRE = AtomRE Mark+ ;
Mark {
    star            # * 
    cross           # +
    option          # ?
}

UnionEMarkRE = ugroup_begin EMarkREs ugroup_end ; # to allow dead regex
GroupRE = group_begin Regex group_end ;



NotYetDefinedNonterminal { Nonterminal }
Nonterminal { symbol }
Terminal { symbol }

'''







