
MyLL1L = 'my_LL1_language'

mainID = mainID_MyLL1L_of_MyLL1L = 'MyLL1L_in_MyLL1L'

MyLL1L_in_MyLL1L = parser_specification_of_MyLL1L_in_MyLL1L = r'''
# this is a comment
# not allow nullable => exist FIRST
# never trace back, next token determines the only one match or failure.
#
MyLL1L_in_MyLL1L = rex
rex = id_define +
id_define = id , define

define
    define_newline = inline_define , newline
    newline_block = newline , block
    
inline_define
    is_token = 'is' , token type
    eq_list = '=' , list ls

block = indent , subrex , dedent
subrex = id_define { 2 , }

list = item , ,item *
,item = ',' , item # ',item' is an id
item = id_count id_count , name ? name
id_count = id id , count ? count
count
    '?' is t'?' # means token.type == '?'
    '*' is t'*'
    '+' is t'+'
    '{}' = '{' , n min , ',' , n ? max , '}' # result_node[1] is result_node['min'], result_node['max'] is a list of len 1 or 0

',' is t',' # "','" is an id
'{' is t'{'
'}' is t'}'
'=' is t'='
'is' is t'is'

name = B
n = B
id = B
token = B
B is t'B' # ONE example (only one): 335&(*&(*_)_5ajf334'  '\gj""" aoi jfv"""''

newline is t'\n'
indent is t'\t'
dedent is t'\b'
'''

'''
child of IDBlock can be IDBlock or IDList or IDToken, but not IDItem
child of IDList is IDItem
IDItem and IDToken have no children


disjoint rule:
for each IDBlock, all FIRST(child) disjoint
for each IDItem I that min < max, FIRST(refID of I) disjoint with FOLLOW(I)


FIRST FOLLOW depenancy:
b <- a : means a should be evaluated first
for IDItem I:
    FIRST(I) <- FIRST(refID of I)
    FOLLOW(refID of I) <- FOLLOW(I)
for IDList L:
    FIRST(L) <- FIRST(child) for child in children from left to right until child not nullable
    FOLLOW(child) <- FOLLOW(L) if child is the last one
                  <- FIRST(next child) elif next child is not nullable
                  <- FIRST(next child) union FOLLOW(next child) otherwise
for IDBlock B:
    FIRST(B) <- FIRST(child) for each child
    FOLLOW(child) <- FOLLOW(B) for each child


FIRST FOLLOW:
id1
    id2
    id3
    
id1 = id2{0,x} id3
id1 = id4 id2{0,x} id3
id1 = id2 id2{0,x} id3
id1 = id2{y,x!=y} id3

id1 = id2{y,x!=y} # FIRST(id2) & FOLLOW(id1) == {}
id4
    id5 = id1 id3

FIRST(id2) & FIRST(id3) == {}
'''
