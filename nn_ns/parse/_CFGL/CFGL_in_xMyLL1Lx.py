


main_ID_of_free_style_CFGL_in_xMyLL1Lx = 'free_style_CFGL'
free_style_CFGL_in_xMyLL1Lx = r'''

# CFGL is not a LL1, here just try to parse it,
# but not generate the parser

free_style_CFGL = top_def + 

top_def 
    group_def = group_def
    filter_def = filter_def
    list_def  = list_def
    token_def  = token_def
    

ref_id;     = ref_id , ';'
fchild_def; = fchild_def , ';' 
list_id=    = list_id , '=' 
flist_id=   = flist_id , '=' 



group_def   = group_id ,  ':' , '{' , ref_id; + , '}' 
filter_def  = filter_id , '{' , fchild_def; + , '}' 
list_def    = list_id= +  , lchild_def *  , ';' 
token_def   = token_id , 'is' , token_name , ';' 
token_name = tag


fchild_def 
    ffilter_def = ffilter_id , '{' , fchild_def; + , '}' 
    flist_def = flist_id= ,  lchild_def * , ';' 
    fref_def = top_id , ';' 
    

lchild_def = argname_endflag ? ,  ref_id ,  count ? ,  tag * 
argname_endflag = argname , endflag
endflag
    endflag_yes = ':' 
    endflag_no = ':-'

ref_id 
    top_id  = top_id
    ffilter_ref_id  = ffilter_ref_id
    


ffilter_ref_id = filter_id , .ffilter_id + 
.ffilter_id = '.' , ffilter_id 

top_id 
    group_id  = group_id
    filter_id  = filter_id
    list_id  = list_id
    token_id  = token_id
    

group_id = id 
filter_id = id 
list_id = id 
token_id = id 
ffilter_id = id 
flist_id = id 
argname = id

count 
    star  = star
    plus  = plus
    optional  = optional
    star?  = star?
    plus?  = plus?
    optional?  = optional?
    min_max = '{{' , min , ':' , max , '}}' 
    len = '[[' , len , ']]' 
    

'{{' = '{'
'}}' = '}'

min = int
max = int
len = int

id is t'w'
int is t'w'
tag is t'#'

star is t'*'
plus is t'+' 
optional is t'?' 
star? is t'*?'
plus? is t'+?' 
optional? is t'??' 

'is' is  t'is'

'=' is t'=' 
'{' is t'{' 
'}' is t'}' 
'[[' is t'[' 
']]' is t']' 
';' is t';' 
':' is t':' 
'.' is t'.' 
':-' is t':-' 


'''







def gen_CFGL_rnode_tree_of_xtokenized_style_CFGL(CFGL_in_xMyLL1Lx=free_style_CFGL_in_xMyLL1Lx):
    from MyLL1L.ProcessMatchResult_MyLL1L_of_MyLL1L import \
         ProcessMatchResult_MyLL1L_of_MyLL1L as tokens2processor
    from MyLL1L.Parser_MyLL1L_of_MyLL1L import parser_MyLL1L_of_MyLL1L

    p = parser_MyLL1L_of_MyLL1L
    tokens = p.tokenize(CFGL_in_xMyLL1Lx)
    match_result = p.parse_tokens(tokens)


    processor = tokens2processor(tokens)
    raw_info_list = processor.to_raw_info_list(match_result)

    string_of_raw_info_list = processor.raw_info_list2string(raw_info_list)

    ##def x(i):
    ##    print(raw_info_list[i].get_raw_init_repr())
    ##
    ##raw_id2info = processor.to_raw_id2info(match_result)
    ##sd = processor.raw_id2info_to_string(raw_id2info)

    def InfoIDItem(nID, top_ref_id, min, max, key = None):
        argname_endflag = (key, True) if key is not None else None
        count = (min, max)
        tags = []
        ref_id = (top_ref_id,)
        return 'lchild', ref_id, count, argname_endflag, tags

    def InfoIDToken(token_type, ID):
        return 'token', ID, token_type
    def InfoIDList(ID, children = []):
        assert all(c[0] == 'lchild' for c in children)
        return 'list', ID, children
    def InfoIDBlock(ID, children = []):
        s = {'list', 'filter'}
        assert all(c[0] in s for c in children)
        return 'filter', ID, children

    infos = eval(string_of_raw_info_list) ####### using the above functions.
    cfgl_rnode_tree_of_xtokenized_style_CFGL = infos
    
##    import pprint
##    p=pprint.PrettyPrinter(indent=4).pprint
##
##    p(raw_parse_result_of_CFGL_in_CFGL)
    
    return cfgl_rnode_tree_of_xtokenized_style_CFGL



free_style_CFGL_in_xMyLL1Lx
cfgl_rnode_tree_of_xtokenized_style_CFGL = gen_CFGL_rnode_tree_of_xtokenized_style_CFGL(free_style_CFGL_in_xMyLL1Lx)
import pprint
p=pprint.PrettyPrinter(indent=4).pprint

p(cfgl_rnode_tree_of_xtokenized_style_CFGL)


[   (   'list',
        'free_style_CFGL',
        [('lchild', ('top_def',), (1, None), None, [])]),
    (   'filter',
        'top_def',
        [   (   'list',
                'group_def',
                [('lchild', ('group_def',), (1, 1), None, [])]),
            (   'list',
                'filter_def',
                [('lchild', ('filter_def',), (1, 1), None, [])]),
            (   'list',
                'list_def',
                [('lchild', ('list_def',), (1, 1), None, [])]),
            (   'list',
                'token_def',
                [('lchild', ('token_def',), (1, 1), None, [])])]),
    (   'list',
        'ref_id;',
        [   ('lchild', ('ref_id',), (1, 1), None, []),
            ('lchild', ("';'",), (1, 1), None, [])]),
    (   'list',
        'fchild_def;',
        [   ('lchild', ('fchild_def',), (1, 1), None, []),
            ('lchild', ("';'",), (1, 1), None, [])]),
    (   'list',
        'list_id=',
        [   ('lchild', ('list_id',), (1, 1), None, []),
            ('lchild', ("'='",), (1, 1), None, [])]),
    (   'list',
        'flist_id=',
        [   ('lchild', ('flist_id',), (1, 1), None, []),
            ('lchild', ("'='",), (1, 1), None, [])]),
    (   'list',
        'group_def',
        [   ('lchild', ('group_id',), (1, 1), None, []),
            ('lchild', ("':'",), (1, 1), None, []),
            ('lchild', ("'{'",), (1, 1), None, []),
            ('lchild', ('ref_id;',), (1, None), None, []),
            ('lchild', ("'}'",), (1, 1), None, [])]),
    (   'list',
        'filter_def',
        [   ('lchild', ('filter_id',), (1, 1), None, []),
            ('lchild', ("'{'",), (1, 1), None, []),
            ('lchild', ('fchild_def;',), (1, None), None, []),
            ('lchild', ("'}'",), (1, 1), None, [])]),
    (   'list',
        'list_def',
        [   ('lchild', ('list_id=',), (1, None), None, []),
            ('lchild', ('lchild_def',), (0, None), None, []),
            ('lchild', ("';'",), (1, 1), None, [])]),
    (   'list',
        'token_def',
        [   ('lchild', ('token_id',), (1, 1), None, []),
            ('lchild', ("'is'",), (1, 1), None, []),
            ('lchild', ('token_name',), (1, 1), None, []),
            ('lchild', ("';'",), (1, 1), None, [])]),
    ('list', 'token_name', [('lchild', ('tag',), (1, 1), None, [])]),
    (   'filter',
        'fchild_def',
        [   (   'list',
                'ffilter_def',
                [   ('lchild', ('ffilter_id',), (1, 1), None, []),
                    ('lchild', ("'{'",), (1, 1), None, []),
                    ('lchild', ('fchild_def;',), (1, None), None, []),
                    ('lchild', ("'}'",), (1, 1), None, [])]),
            (   'list',
                'flist_def',
                [   ('lchild', ('flist_id=',), (1, 1), None, []),
                    ('lchild', ('lchild_def',), (0, None), None, []),
                    ('lchild', ("';'",), (1, 1), None, [])]),
            (   'list',
                'fref_def',
                [   ('lchild', ('top_id',), (1, 1), None, []),
                    ('lchild', ("';'",), (1, 1), None, [])])]),
    (   'list',
        'lchild_def',
        [   ('lchild', ('argname_endflag',), (0, 1), None, []),
            ('lchild', ('ref_id',), (1, 1), None, []),
            ('lchild', ('count',), (0, 1), None, []),
            ('lchild', ('tag',), (0, None), None, [])]),
    (   'list',
        'argname_endflag',
        [   ('lchild', ('argname',), (1, 1), None, []),
            ('lchild', ('endflag',), (1, 1), None, [])]),
    (   'filter',
        'endflag',
        [   (   'list',
                'endflag_yes',
                [('lchild', ("':'",), (1, 1), None, [])]),
            (   'list',
                'endflag_no',
                [('lchild', ("':-'",), (1, 1), None, [])])]),
    (   'filter',
        'ref_id',
        [   ('list', 'top_id', [('lchild', ('top_id',), (1, 1), None, [])]),
            (   'list',
                'ffilter_ref_id',
                [('lchild', ('ffilter_ref_id',), (1, 1), None, [])])]),
    (   'list',
        'ffilter_ref_id',
        [   ('lchild', ('filter_id',), (1, 1), None, []),
            ('lchild', ('.ffilter_id',), (1, None), None, [])]),
    (   'list',
        '.ffilter_id',
        [   ('lchild', ("'.'",), (1, 1), None, []),
            ('lchild', ('ffilter_id',), (1, 1), None, [])]),
    (   'filter',
        'top_id',
        [   (   'list',
                'group_id',
                [('lchild', ('group_id',), (1, 1), None, [])]),
            (   'list',
                'filter_id',
                [('lchild', ('filter_id',), (1, 1), None, [])]),
            (   'list',
                'list_id',
                [('lchild', ('list_id',), (1, 1), None, [])]),
            (   'list',
                'token_id',
                [('lchild', ('token_id',), (1, 1), None, [])])]),
    ('list', 'group_id', [('lchild', ('id',), (1, 1), None, [])]),
    ('list', 'filter_id', [('lchild', ('id',), (1, 1), None, [])]),
    ('list', 'list_id', [('lchild', ('id',), (1, 1), None, [])]),
    ('list', 'token_id', [('lchild', ('id',), (1, 1), None, [])]),
    ('list', 'ffilter_id', [('lchild', ('id',), (1, 1), None, [])]),
    ('list', 'flist_id', [('lchild', ('id',), (1, 1), None, [])]),
    ('list', 'argname', [('lchild', ('id',), (1, 1), None, [])]),
    (   'filter',
        'count',
        [   ('list', 'star', [('lchild', ('star',), (1, 1), None, [])]),
            ('list', 'plus', [('lchild', ('plus',), (1, 1), None, [])]),
            (   'list',
                'optional',
                [('lchild', ('optional',), (1, 1), None, [])]),
            ('list', 'star?', [('lchild', ('star?',), (1, 1), None, [])]),
            ('list', 'plus?', [('lchild', ('plus?',), (1, 1), None, [])]),
            (   'list',
                'optional?',
                [('lchild', ('optional?',), (1, 1), None, [])]),
            (   'list',
                'min_max',
                [   ('lchild', ("'{{'",), (1, 1), None, []),
                    ('lchild', ('min',), (1, 1), None, []),
                    ('lchild', ("':'",), (1, 1), None, []),
                    ('lchild', ('max',), (1, 1), None, []),
                    ('lchild', ("'}}'",), (1, 1), None, [])]),
            (   'list',
                'len',
                [   ('lchild', ("'[['",), (1, 1), None, []),
                    ('lchild', ('len',), (1, 1), None, []),
                    ('lchild', ("']]'",), (1, 1), None, [])])]),
    ('list', "'{{'", [('lchild', ("'{'",), (1, 1), None, [])]),
    ('list', "'}}'", [('lchild', ("'}'",), (1, 1), None, [])]),
    ('list', 'min', [('lchild', ('int',), (1, 1), None, [])]),
    ('list', 'max', [('lchild', ('int',), (1, 1), None, [])]),
    ('list', 'len', [('lchild', ('int',), (1, 1), None, [])]),
    ('token', 'id', 'w'),
    ('token', 'int', 'w'),
    ('token', 'tag', '#'),
    ('token', 'star', '*'),
    ('token', 'plus', '+'),
    ('token', 'optional', '?'),
    ('token', 'star?', '*?'),
    ('token', 'plus?', '+?'),
    ('token', 'optional?', '??'),
    ('token', "'is'", 'is'),
    ('token', "'='", '='),
    ('token', "'{'", '{'),
    ('token', "'}'", '}'),
    ('token', "'[['", '['),
    ('token', "']]'", ']'),
    ('token', "';'", ';'),
    ('token', "':'", ':'),
    ('token', "'.'", '.'),
    ('token', "':-'", ':-')]
    

