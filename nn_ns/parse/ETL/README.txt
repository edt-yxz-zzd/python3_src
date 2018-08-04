two type:
1. ETL
    one ',' yields one tuple which may be empty;
    between two ',''s, there are 'word', 'string' and 'comment';
    the above three types are separated by spaces(NOTE:comment).
    'word' and 'string' form the tuple.
    'word' is the content of the string in the tuple.
    'string' is a python string literal in the tuple(NOTE:not merged).
2. the parse result
    list of tuple of str
    empty tuple stands for a separater token
    nonempty-tuple: the first item is the token name.
    

ETL = '</def;>, " /", 1 2 3, ,'
parse result = [('</def;>',), (' /',), ('1', '2', '3'), ()]