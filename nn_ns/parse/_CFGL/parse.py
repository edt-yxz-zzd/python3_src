

3-phase are required:
    using gramma to discript a language:
    1. parse:
        input: token_names
        ouput: tfnode
    but the tfnode is not what we need
    so we must to explain the tfnode.
    usually, the token_names are not enough,
    because we were not satisfied to get the struct infomation.
    we use sematic info to explain the text, therefore the
    source and token_rngs are needed as input:
    (but not token_values, this is the job of expain) 
    2. expain:
        input: tfnode, source, token_rngs
        output: any thing comfortable
    therefore, we require the tokenize phase
    3. tokenize:
        input: source
        output: token_names, token_rngs


tokenize can be viewed as 3-phase too:
    1. subtokenize:
        input: string
        output: subtoken_names:list<char>,
                subtoken_rngs:[(0,1), (1,2)...]
    2. subparse:
        input: subtoken_names:list<char>
        output: subfnode:list<tnode2>
                        :[(tnode_case, tnode_rng)]
                        :[(supertoken_name, supertoken_rng)]
    3. subexplain:
        input: fnode, source, subtoken_rngs
        output: supertoken_names, supertoken_rngs

we define these 3-phase as:
    recognize<  T<charset, token_name_set>,
                P<token_name_set, tfnode<tnode_case_set, is_forest:bool>>,
                E<tfnode<tnode_case_set, is_forest:bool>, ast<'x_lang'>>
             >
    NOTE: I mix the use of set and type
    set ~ type
    let SET<type T> be the set of all possible values of T
    let ENUM<set S> be a type T s.t. SET<T> == S
    SET<ENUM<S>> is S
    ENUM<SET<T>> is T


subtype relationship:
    if SET<T> <= SET<D>: then T is subtype of D
    if T is subtype of D:
        list<T> is subtype of list<D>
    

token<token_name_set> = ENUM<token_name_set>
tokens<token_name_set> = list<token>

# tfnode : tree node or forest node
# forest node is list of tree
# tree node is a tree(tnode3) or leaf(tnode2
tfnode<tnode_case_set, is_forest = true> is tnode<tnode_case_set>
tfnode<tnode_case_set, is_forest = false> is fnode<tnode_case_set>
tnode<tnode_case_set> is tnode2<tnode_case_set> or tnode3<tnode_case_set>
tnode2<tnode_case_set> is (tnode_case, rng)
tnode3<tnode_case_set> is (tnode_case, rng, fnode<tnode_case_set>)
fnode<tnode_case_set> is list<tnode<tnode_case_set>>



source
'A;A;A' --> ['one', 'sep', 'one', 'sep', 'one'] 
            [(0,1),(1,2),(2,3),(3,4),(4,5)]
                --> ('count', (0,5), [('1', (0,1)), ('1', (2,3)), ('1', (4,5))])
                    --> 3
'A,A,A' --> the same as above
'AAA'   --> ['one', 'one', 'one'] # different type with aboves {'one'} {'one', 'sep'}
            [(0,1),(1,2),(2,3)]
                # NOTE: the same type {'count', '1'}
                --> ('count', (0,3), [('1', (0,1)), ('1', (1,2)), ('1', (2,3))])
                    --> 3
'3'     --> ['i']
            [(0,1)]
                --> ('int', (0,1))
                    --> 3

these 4 examples show that the previous phase can be different
tokenize of e0) and e1) are different, but the result are of same type
parse result of e0-1) and e2) are of same type
expain result of e0-2) and e3) are of same type

NOTE:
    tokenize result type of e2) is subtype of that of e0-1)
    so it may be parsed by the above parser, but usually cause failure.






    













