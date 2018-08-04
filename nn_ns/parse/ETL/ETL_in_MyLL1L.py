
mainID_MyLL1L_of_ETL = 'ETL_in_MyLL1L'
ETL_in_MyLL1L = r'''

ETL_in_MyLL1L = tuple, * , EOF

tuple, = item * , ','

item
    word is t'w'
    string is t's'
',' is t','
EOF is t'$'

'''


example_ETL = [
    ('', []),
    ('</def;>, " /", 1 2 3, ,', [('</def;>',), (' /',), ('1', '2', '3'), ()]),
    ]
