
mainID_MyLL1L_of_EPL = 'EPL_in_MyLL1L'
EPL_in_MyLL1L = r'''

EPL_in_MyLL1L = item

item = '[' , name ? , item * , ']' , tag ?


name = chunks
tag = chunks
chunks = chunk +


chunk
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
