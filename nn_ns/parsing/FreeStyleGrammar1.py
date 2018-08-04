

eg = r'''

# comment; till end of line

# naming convention
Nonterminal { 'terminal' } # copy rule
<Nonterminal, too> = { 'terminal, too' }


# explicit rule types
AlternativeRule {
    Alt1
    Alt2*
    'alt3'
    'alt4'+
}

ConcatenateRule = Con1 Con2? 'con3' 'con4' ;


# how to defined special RuleIDs
Null = ;
Undefined {}
Undefined2 { A[1..0] }
Undefined3 = A B Undefined ;
Undefined4 = { Undefined }

# implicit rules
    # with tags
    # implicit: if "A = B + ;" then autogenerate implicit rule "B+ { B[1..] }"
    #        or if "A = B [0..2] ;" then known how to parse RuleID "B[0..2]"
    
    # ordered tags
        egBuiltinIterativeOrderedTags = RuleID ? * + [2] [4..5] [1..] ;
        egBuiltinFiltericOrderedTags = RuleID >>tag >>"tag, too" ;
            # ordered:   "... >>f >>h ..." != "... >>h >>f ..."

    # unordered tags
        egUserLocalUnorderedTags = RuleID -tag -"tag, too" -tag=value -tag=[value1 value2] -tag{key:value ...};
            # unordered: "... -tag1 -tag2 >>f ..." == "... -tag2 -tag1 >>f ..."
            # local:     "... -tag1 -tag2 >>f ..." != "... -tag1 >>f -tag2 ..."
        egUserGlobalUnorderedTags = RuleID --tag --"tag, too" --other_tag_forms="like local tag forms";
            # unordered: "... --tag1 --tag2 ..." == "... --tag2 --tag1 ..."
            # global:    "... --tag >>f ..." == "... >>f --tag ..."


'''

















