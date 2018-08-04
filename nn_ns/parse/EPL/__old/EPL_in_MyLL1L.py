
mainID_MyLL1L_of_EPL = 'EPL_in_MyLL1L'
EPL_in_MyLL1L = r'''

EPL_in_MyLL1L = item
nonempty_list
    nameless_list = item +
    named_list = list_name , item *
item = [list] , item_tag ?
[list] = '[' , nonempty_list ? , ']'
list_name = names
item_tag = names
names = name +


name
    word is t'w'
    string is t's'
'[' is t'['
']' is t']'

'''

# item = (list_name, tag, subitems) # ((), (), [])
# list_name = tuple of str = tag
# subitems = list of item
example_EPL = [
    ('[r"main" [item1 args] [item2 []]item2_tag]',
     (('main',), (), [
         (('item1', 'args'), (), []),
         (('item2',), ('item2_tag',), [
             ((), (), [])
             ])
         ])),
    ]
