
'''
supports actions # once, I want to implement temples/id_tuple, but they seem too hard for me.
allows multilines logic line , using '\' at the beginning of the following line
if ',' at beginning, then '\' can be omitted.
but discards named item
'''

'''

# TODO
# template_def = 'template' , template_id , def_body
# template list ( e ) = e , ,item ( e ) *
# template ,item ( e ) = ',' , e
# 'template' is t'template'
# refID = template_id
'''
LL1V2L = 'my_LL1_version2_language'


mainID_MyLL1L_of_LL1V2L = 'LL1V2L_in_MyLL1L'
LL1V2L_in_MyLL1L = r'''
LL1V2L_in_MyLL1L = top_layer
top_layer = top_layer_block


top_layer_block = filter_action\n * , top_layer_def + , rex_section
top_layer_def
    object_def = top_layer_id , def_body
    concept_def = 'concept' , top_layer_id , newline
top_layer_id = concept_id , base_concept_decl ?
base_concept_decl = ':' , concept_id + # why concept? we only care the FIRST of leaves(derived-most id) 



block = filter_action\n * , def + # not {2,} diff from LL1v1
def = id , def_body

def_body
    filter_def = newline , filter_body
    assign_def = ',' ? , as_clause ? , '=' , list , newline , assign_body ?

as_clause = 'as' , as_item, +
as_item, = id ? , :num ? , ','
:num = ':' , num


filter_body = indent , block , dedent
assign_body = indent , assign_action\n + , dedent

list = item_def +
item_def = tagged_item , item_action * , ',' # note : always end up with ','
tagged_item = tag * , item_count , tag *
tag is t'--'                         # an token which value begin with '--', if token.value == '--', then discards the item value
item_count = refID , count ? # without count == { 1 }

count
    '*' is t'*' # short hand for {0,}
    '+' is t'+' #                {1,}
    '?' is t'?' #                {0,1}
    '{}' = '{' , num , ,num? ? , '}' # { n } is not { n , n } . 'a { 2 }' means 'a , a'.

,num? = ',' , num ?

filter_action\n = filter_action , newline
assign_action\n = assign_action , newline

filter_action = action
assign_action = action
item_action = action

action = ?fix , {object_names}{action_names} ? , method_name +

{object_names}{action_names} = {names} { 2 , 2 }
{names} = '{' , name + , '}'

?fix
    prefix is t'->'
    suffix is t'<-'

object_name = name
    # self | child
action_name = name
    # | filter->* list-> list_group-> list_child-> item-> item_group-> item_child
    # | <-default_value_factory # when 'item?' failed, default yield None
    # 
method_name = name # method(self_node, tID2info, tokens, name2methods, **kwargs)
    # item_group kwargs: min max
    # list_group kwargs: tags

name = BTOKEN








rex_section = '--rex' , newline , rex_define + # why rex, because we don't care ambiguity.
rex_define = inline_define , newline # allow one ID with mutiple rules; allow tail recur; longest match wins; don't care ambiguity

inline_define
    define_one_ID = ID , define_body
    bind_define = 'bind' , string + # token_type which is a string, will be binded to a ID named by the string
    split_bind_define = 'split_bind' , string
define_body
    rex_body   = '=' , rex
    token_body = 'is' , token_name
    union_token_body = 'not' ? , 'in' , '{' , token_name * , '}'
    # define any like: any not in { }
rex
    concat = rex_item +
    not = 'not' , rex  # note: "and (not rex) any { 4 , 4 }" may be useful
    and = 'and' , rex_item2s
    or  = 'or' , rex_item2s
    #concat = 'concat' , rex_item2s
rex_item2s = rex_item { 2 , }
rex_item = rex_atom , count
rex_atom
    any = 'any'
    ID = ID
    group = '(' , rex , ')'

token = 'not' ? , token_name +
    # this 'not' is different from the above one
    # only match string of length 1
    # equivalent to "and any (not or token_name+)"
token_name = BTOKEN # t'xx'
ID = BTOKEN
string = BTOKEN

refID = id , .id * # concept id / filter-list id / rex id
.id = '.' , id
concept_id = id


', =' = ',' ? , '='

num = BTOKEN
id = BTOKEN
BTOKEN is t'id'

'concept' is t'concept'
newline is t'\n'
indent is t'\t'
dedent is t'\b'
',' is t','
'=' is t'='
'*' is t'*'
'+' is t'+'
'?' is t'?'
'{' is t'{'
'}' is t'}'
'.' is t'.'
':' is t':'
'(' is t'('
')' is t')'
'is' is t'is'
'in' is t'in'
'as' is t'as'
'not' is t'not'
'and' is t'and'
'or' is t'or'
'any' is t'any'
'bind' is t'bind'
'split_bind' is t'split_bind'
'''


'''
default actions:

::(self_node, tID2info, tokens, name2methods, **kwargs) -> None
default_value_factory
    return None

filter 
    -> pass
    <- pass

list
    -> pass
    <- pass

list_group (self_node, tID2info, tokens, name2methods, tags)
    ->
        self.children = []
        self.value = []
    <-
        self.value = [v for v, tag in zip(self.value, tags) if tag != '--']


list_child
    ->
        r = self.match_result.children[len(self.children)]
        c = self.build(match_result=r, parent=self, attr=self.attr)
        self.children.append(c)

    <-
        c = self.children[-1]
        self.value.append(c.value)

 
item
    -> pass
    <- pass

item_group(self_node, tID2info, tokens, name2methods, min, max)
    ->
        self.children = []
        self.value = []
    <-
        if max == 1:
            if min == 1:
                self.value, = self.value
            elif min == 0:
                if self.value:
                    self.value, = self.value
                else:
                    info = tID2info[self.tID]
                    method_name = tID2info[info.refID].get_action('default_value_factory')
                    factory = name2methods[method_name]
                    default_value = factory(self_node, tID2info, tokens, name2methods)
                    self.value = default_value
                


item_child
    ->
        r = self.match_result.children[len(self.children)]
        c = self.build(match_result=r, parent=self, attr=self.attr)
        self.children.append(c)

    <-
        c = self.children[-1]
        self.value.append(c.value)


is
    -> pass
    <- pass
is_group
    ->
        token = tokens[self.match_result.begin]
        self.value = token.value
    <- pass

'''






