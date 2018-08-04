
token:
    comment: 
        single line: {//]...
        multilines : {/*]...[*/}
    spaces
    string: 
        python-style: '...' ".." '''...''' """..."""
        word: fafj   !#$^&*k,./\...
        
    string-: '...'- // string- and string makeup a big one
    bytes: b'...' // python-style
    bytes-: b'...'-
    
    
    constant:
        number: int float complex
        0-word: 0none; 0-inf; 0nan; 0true; ...
    delimitor:
        {word[   {word{
        {[ ]}    {{ }}
        = ( ) [ ] { }
        

structure tree:
    normal node::tuple
        has some attrs and children
        the first one is required - tag::hashable
        other attrs:
            id::str
            type::frozenset
            args::tuple
            kwargs::dict
            children::list of node
    comment node::a list
    content node::a string
    