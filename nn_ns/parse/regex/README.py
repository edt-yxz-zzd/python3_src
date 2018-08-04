

'''
to search binary file, see mmap, sand.file2buffer

'''



regex app:
    1) input_str : the whole str, not the group0
    2) try_str : the group0, is a substr of input_str, i.e. in find rex...
    whole match:
        accept or not
        try_str == input_str
    partial match:
        exist s, s.t. whole_match(try_str+s)
        try_str == input_str
        turns all non-error states into final

    ############### try_str may not be input_str ###############

    context whole match:
        # i.e. '$' 'aaa(?=bb)'
        # using as a component of concat-rex
        context_whole_match(input_str, begin, end)
        try_str = input_str[begin:end]
    context partial match:
        context_partial_match(input_str, begin, end)
        try_str = input_str[begin:end]


    prefix match:
        try_str = input_str[:end]
        iter [(0, end)]
        prev_end < succ_end
    postfix match:
        try_str = input_str[begin:]
        reversable_stream, reversable_regex ==>> reverse_prefix_match
    "A|B" = A or B = "({|}A)B"
    "A&B" = A and B = "({&}A)B"
    "A!B" = not A and B = "({!}A)B"
    "({~}A)" = not A = "({!}A).*"
    order: "() ! & |"
    "A!B&C|D" = "((A!B)&C)|D"
    "A|B&C!D" = "A|(B&(C!D))"
    capture and anchor and group and scope:
        # decompose the regex into a digraph, not merely series-parallel graph
        # and add some special join-nodes(pred):
        #   1) &: more than one input: (rex1->, r2->, ...)&
        #   2) |: like above
        #   3) ~: one input: rex->~
        #   4) +(>|==)n: more than or exactly n input are true
        
        scope is a noncapture group:
            "({?:S<scope_group_name>}A)"
            "({?:S}A)" # anonymous
            using as anchor.target.begin/end
            1) where the anchor defined gives one end of dedge
            2) and the refered scope/group end gives other
            scope_group_name may not unique and can be embedded
        capture is a group:
            "({?P<capture_group_name>}A)" # keyword_only
            "({?PI<capture_group_name>}A)" # keyword_position
            "({?PI}A)" # 'I' means 'indexable' # position_only
            capture_group_name should be unique
        named_group used at nonlocal ref:
            "({?:<group_name>}A)" # non-capture
            group_name should be unique
        anonymous_group is noncapture group:
            '(A)'
        forwad local anchor:
            using "! &"
            pyrex"^(?=A)B$" = "^A&B$"
            pyrex"^(?!A)B$" = "^A!B$"
        
        nonlocal or backward anchor is hard to implement??:
            nonlocal: diff global by specify a group name
            global anchor pyrex"(?<?[=!]A)"????

            nonlocal anchor using below syntax:
                nonlocal forwad/backward local:
                    "({?=<outmost_group_name>}A)"
                    "({?!<outmost_group_name>}A)"
                    "({?<=<outmost_group_name>}A)"
                    "({?<!<outmost_group_name>}A)"
                    bound by group named <outmost_group_name>
            local:
                "(B({?=..}A)C)" == "(B(A&C))"
                "(B({?!..}A)C)" == "(B(A!C))"
                "(B({?<=..}A)C)" == "((A&B)C)"
                "(B({?<!..}A)C)" == "((A!B)C)"
            global:
                "...(B({?=0}A)C)..." == "({?P<global>}...(B({?=<global>}A)C)...)"
                "...(B({?!0}A)C)..."
                "...(B({?<=0}A)C)..."
                "...(B({?<!0}A)C)..."
            external:
                "...({?=^$}A)..."
                "...({?!^$}A)..."
                "...({?<=^$}A)..."
                "...({?<!^$}A)..."
                
                
            NOTE:
                the parent group: 'g<"..">'
                the global group: 'g<"0">', the try_str
                the external group: 'g<"^$">', the whole input_str

    prefix_match:
        if at most one result, behaviour is well defined
        else:
            implement defined
        prefix_fmt = "({?P<result>}{rex}).*"
    shorest_prefix_match:
        prefix_fmt << "A.+!A"
    longest_prefix_match:
        "({?P<result>}A)(({?!}.+{?<=<result>}A)|$)"
    unique_prefix_match:
        "({?P<result>}A.+!A)(({?!}.+{?<=<result>}A)|$)"
    find all submatch:
        included_overlaps
        how????
        if ".*(A)":
            using prefix match and capture
            
        
