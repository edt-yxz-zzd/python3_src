

r'''
'''



r'''
# the order in subblock may be important if ambiguous

# groups and filters form a DAG, terminated at filters
# filters and fchildren form a forest, terminated at flist or fref
# ends up with list_def/flist_def/fref_def / lchild_def / token_def
# therefore, the parse result tree of XL_in_CFGL has three node types:
#    tagged by 'list' / 'lchild' / 'token'
# those are the leaf tID cases, two more nonleaf case are:
#    'group' / 'filter'
# 
# Left Recursion // opening (uID, pos) to prevent
# infinite empty productions // set to the min times
# opt:
#   # first time match, distinguish with a 'next' match
#   # (other's fail may cause to call next match of this one)
#   # error :(nostate_uID, pos) -> fail or closed_mstate
#   #   xxxxxxxxxxxxxxxxxxxxxxxx
#   #   since we avoid re-enter, so the opening stack affects the result
#   #   
#
#
#   # a uID with its historical parents (that is the call stack),
#   # if its ith child had end at 'end', then next match with the same end
#   # will cause the later matchs fail too
#   (history_list/lchild_uID, ichild, end)
#
# the farthest pos reached for debug





CFGL = top_def +




top_def
    group_def
    filter_def
    list_def
    token_def
    
                                    # ; - <newline> | { - <newline-indent> | } - <dedent>
group_def = group_id ref_id +       # group_id ':' <newline-indent> (ref_id <newline>) + <dedent>
filter_def = filter_id fchild_def + # filter_id <newline-indent> (fchild_def <newline>) + <dedent>
list_def = list_id + lchild_def *   # (list_id '=') + lchild_def * <newline>
token_def = token_id token_name     # token_id 'is' token_name <newline>
token_name = tag

# NOTE :
#     at top layer, 'a = b = ...' ==>> 'a = b; b = ...'
#     at filter block, fref: 'xx' ==>> 'xx = xx'

fchild_def
    ffilter_def = ffilter_id fchild_def + # ffilter_id <newline-indent> (fchild_def <newline>) + <dedent>
    flist_def = flist_id lchild_def *     # flist_id '=' lchild_def * <newline>
    fref_def = top_id                     # top_id <newline>

lchild_def = argname_endflag ? ref_id count ? tag *   # (argname (':'|':-')) ? ref_id count ? tag * 
argname_endflag = argname endflag
endflag
    endflag_yes
    endflag_no
    
ref_id
    top_id
    ffilter_ref_id
    
ffilter_ref_id = filter_id ffilter_id +   # filter_id ('.' ffilter_id) +

top_id
    group_id
    filter_id
    list_id
    token_id

    
count
    star                 # '*'
    plus                 # '+'
    optional             # '?'
    star?                # '*?' nongreedy
    plus?                # '+?'
    optional?            # '??'
    min_max = min max    # '{' min ':' max '}' or max min
    len = len            # '[' len ']'
    
'''

r'''
CFGL
XL_in_CFGL --by-hand--> main_tID + raw-node-forest (7 cases)
           -----------> tID2tnode (5 cases)
# tID may convert to iID, a integer, to save time and space
# tID2tnode --> iID2tID and iID2inode (tIDs and inodes)
# uID is tID or iID, uID2unode may be a dict or list or tuple
parse_CFGL_of_XL<uID2unodes of XL_in_CFGL> (src_in_XL) --> leaf-node-tree (3 cases)



raw parse result of XL_in_CFGL is a list of below nodes (raw-node tree):
    # ID and tID(ref_id) are of XL
    'token', ID, token_name
    'lchild', ref_id, count=None, argname_endflag=None, [tag]=[]
    'top_list', [ID], [lchild_node] # x=y=... => x=y; y=...
    'list', ID, [lchild_node]
    'group', ID, [ref_id]
    'filter', ID, [filter_node/list_node/fref_node]
    'fref', ID # x => x=x
convert to tnodes (tID-to-tnode dict):
    'token', tID, token_name
    'lchild', tID, ref_id, count=None, argname_endflag=None, [tag]=[]
    'list', tID, [lchild_tID]
    'group', tID, [ref_id], [leaf_tID=token_tID/list_tID]
    'filter', tID, [child_tID], [leaf_tID=token_tID/list_tID]
    



parse result of source_in_XL (leaf-node tree):
    tag(leaf-cases) 'list' 'lchild' 'token'
    tID in XL_in_CFGL is a product-rule of XL

    ('list', {'tID':...}, [lchild_node])        # may be list_def/flist_def/fref_def
    ('lchild', [list_node/token_node])          # {'argname':..., 'ref_id':...} is not necessary
    ('token', {'token_id':..., 'token_position':...})

    simplify to: (rng is (pos, end))
    ('list', uID, rng, [lchild_node])            # these two need the tID2info_XL_in_CFGL to
    ('lchild', uID, rng, [list_node/token_node]) # complete the information
    ('token', uID, rng))                         # this needs the tokens_XL_in_CFGL for tokens[pos]

#################
process to generate XL parser info:
case_CFGL: group/filter/list/token/lchild

tID2info_XL_in_CFGL # tID in XL and case in CFGL

tID = tuple of str
info = (case_CFGL, tID, ...) # a tnode
case_CFGL
    group (expand to leaf; discard the duplicated tID)
        children and leaves
    filter (also ffilter)
        children and flists

    list (also flist/fref)
        children
    token
        token_name

    lchild
        ref_id, count, argname, tags


'''

CFGL_in_free_style_CFGL = r'''
# ; - <newline> | { - <newline-indent> | } - <dedent>
# ; - <\n> | { - <\n\t> | } - <\b>

CFGL_in_free_style_CFGL = top_def + ;

top_def {
    group_def ;
    filter_def ;
    list_def ;
    token_def ;
    }

ref_id;     = ref_id ';' ;
fchild_def; = fchild_def ';' ;
list_id=    = list_id '=' ;
flist_id=   = flist_id '=' ;

group_id = filter_id = list_id = token_id = id ;

group_def   = group_id  ':' '{' ref_id; + '}' ;
filter_def  = filter_id '{' fchild_def; + '}' ;
list_def    = list_id= +  lchild_def * ';' ;
token_def   = token_id 'is' token_name ';' ;
token_name = tag

ffilter_id = flist_id = argname = id ;
fchild_def {
    ffilter_def = ffilter_id '{' fchild_def; + '}' ;
    flist_def = flist_id=  lchild_def * ';' ;
    fref_def = top_id ';' ;
    }

lchild_def = argname_endflag ?  ref_id  count ?  tag * ;
argname_endflag = argname endflag ;
endflag
    endflag_yes = ':' ;
    endflag_no = ':-' ;
    
ref_id {
    top_id ;
    ffilter_ref_id ;
    }


ffilter_ref_id = filter_id .ffilter_id + ;
.ffilter_id = '.' ffilter_id ;

top_id {
    group_id ;
    filter_id ;
    list_id ;
    token_id ;
    }
    
count {
    star ;
    plus ;
    optional ;
    star? ;
    plus? ;
    optional? ;
    min_max = '{{' min ':' max '}}' ;
    len = '[[' len ']]' ;
    }

'{{' = '{' ;
'}}' = '}' ;

min = max = len = int ;

id is --w ;
int is --w ;
tag is --# ;

star is --* ;
plus is --+ ;
optional is --? ;
star? is --*? ;
plus? is --+? ;
optional? is --?? ;

'is' is --is ;

'=' is --= ;
'{' is --{ ;
'}' is --} ;
'[[' is --[ ;
']]' is --] ;
';' is --; ;
':' is --: ;
'.' is --. ;
':-' is --:- ;

'''


from sand import explain_node

def count2range(count):
    min, max = count
    assert (min, max) != (None, None)
    inf = float('inf')
    
    if min is None: min = inf
    if max is None: max = inf
    assert min >= 0
    assert max >= 0

    step = -1 if min > max else 1
    return min, max, step




def explain_node_CFGL(node, types = [str, tuple, dict, list]):
    # explain node as :
    # (tag:str, args:tuple?, kwargs:dict?, children:list<node>?)

    
    r = explain_node(node, types, nrequired=1)
    tag, args, kwargs, children = r

    if type(tag) != str:
        raise ValueError('type(tag) != str')
    return r











