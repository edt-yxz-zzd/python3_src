two type:
1. EPL
    one '[]' pair yields one item which may follow by a tag;
    a item has its name, tag and subitems.
    item = [name? item*] tag?
    
    NOTE: comment should be separated by spaces or '[]'
    'word's and 'string's form a name or tag.
    'word' is the content of a string.
    'string' is a python string literal(NOTE:not merged).
2. the parse result
    name_type = tag_type = tuple of str
    result_type = item_type = (name_type, tag_type, list of item_type)
    

EPL = '[r"main" []tag for 0 item [item1] []]'
parse result = (('main',), (), [
    ((), ('tag', 'for', '0', 'item'), []),
    (('item1',), (), []),
    ((), (), []),
])