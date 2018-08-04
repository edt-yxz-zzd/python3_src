
mainID_MyLL1L_of_MKUL = 'MKUL_in_MyLL1L'
MKUL_in_MyLL1L = r'''

MKUL_in_MyLL1L = normal_node

normal_node = '(' , tag , id ? , type ? , args ? , kwargs ? , subnodes ? , ')'
tag = key
id = string
type = frozenset # baseclass
args = tuple
kwargs = dict
subnodes =  '[' , node * , ']' # list of node


hashable_tuple = '(' , key * , ')'
tuple = '(' , arg * , ')'
dict = '{' , key=value * , '}'

frozenset = '{[' , key * , ']}'
set = '{{' , key * , '}}'
list = '[' , arg * , ']'

arg = value
key=value = key , '=' , value
key = hashable_value


node
    content = string
    comment = list # ie: '["""' , str , '"""]'
    normal = normal_node


    
constant
    None = None
    bool = bool
    int = int
    float = float
    imag = imag
    complex = complex
    # digit_word word with digit prefix.
    # 0[-+]?nan; 0[-+]?inf; 0[-+]?nanj; 0[-+]?infj; 
    # 0[-+]?nan[-+]xxj; 0[-+]?inf[-+]xxj;
    # 0none; 0true; 0false

string_tail
    named_str = named_str
    str = str
    word = word # not begin with digit, not contains \s{}[]()'" , and not = (= is a keyword)
    #   ??not None/True/False    
    # word_str # unknown str prefix. \eval'set()' \f<a,b>
string-
    str- = str-
    named_str- = named_str-

bytes_tail
    bstr = bstr
    named_bstr = named_bstr
bytes-
    bstr- = bstr-
    named_bstr- = named_bstr-
string = string- * , string_tail
bytes = bytes- * , bytes_tail


literal_atom
    constant = constant
    bytes = bytes
    string = string

    
hashable_literal_but_tuple
    literal_atom = literal_atom
    frozenset = frozenset
    
hashable_literal
    others = hashable_literal_but_tuple
    tuple = hashable_tuple
    

nonhashable_literal_but_tuple
    list = list
    set = set
    dict = dict
    
literal
    hashable = hashable_literal_but_tuple
    nonhashable = nonhashable_literal_but_tuple
    tuple = tuple


==key=value = '=' , '=' , key=value +
hashable_call_on_args = '{word[' , arg * , ==key=value ? , ']}'
nonhashable_call_on_args = '{word{' , arg * , ==key=value ? , '}}'


nonhashable_call
    on_args = nonhashable_call_on_args
    on_string = nonhashable_call_on_string
    on_bytes = nonhashable_call_on_bytes
hashable_call
    on_args = hashable_call_on_args
    on_string = hashable_call_on_string
    on_bytes = hashable_call_on_bytes
call
    hashable = hashable_call
    nonhashable = nonhashable_call

hashable_value
    call = hashable_call
    literal = hashable_literal
value
    call = call
    literal = literal

# {//] single line comment
# {/*] [*/} multiline comment
# '" ( ) [ ] { } {{ }} {[ ]} =
# str- bstr- bstr str word
# 0none 0bool int 0float 0imag 0complex tfloat timag tcomplex
# {word[ {word{

None = 0none
bool = 0bool
float
    tf = tfloat
    0f = 0float
imag
    ti = timag
    0i = 0imag
complex
    tc = tcomplex
    0c = 0complex


hashable_call_on_bytes is t'H'
nonhashable_call_on_bytes is t'Q'
hashable_call_on_string is t'h'
nonhashable_call_on_string is t'@'

named_str- is t'_'
named_str is t'a'
named_bstr- is t'^'
named_bstr is t'A'

str- is t'-'
bstr- is t'~'
bstr is t'\0'
str is t's'
word is t'w'

int is t'i'
tfloat is t'f'
timag is t'm'
tcomplex is t'c'

0none is t'n'
0bool is t'b'
0float is t'!'
0imag is t'j'
0complex is t'C'





'=' is t'='
'(' is t'('
')' is t')'
'[' is t'['

']'
    'pure]' is t']'
    '-' = ']-' 
']-' is t'>'

'{' is t'{'
'}'
    'pure}' is t'}'
    '-' = '}-' 
'}-' is t'\''


'{word{' is t'"'
'{{' is t'`'
# no '}}' is t'\''
'}}' = '}-' , '}'

'{word[' is t'\\'
'{[' is t'<'
# no ']}' is t'>'
']}' = ']-' , '}'




'''

def _split(s):
    ls = s.split()
    lines = ["{0} is t'{0}'".format(n) for n in ls]
    lines.extend("'{0}' is t'{0}'".format(n) for n in ls)
    return '\n'.join(lines)

example_MKUL = [
    ('''
{//] single line comment
(main {/*] multiline
comment [*/} {#this-is-a-word-comment.~main_children:] [{//] main children
    (hr){/*aaaa] multiline \'''
comment [aaaa*/}
    (a (someargs...) {href="www.xx.cn"} [goto xx])
    (div 'my'- 'name' {[type1 type2]} () {} [
        (p [
            This is the
            (span {font-size=big} [
                content
            ])
        ])

        [{{[]}=3e3} {{{[{[]}]}}} {[]} {1=[]} {1={1=[]}} {1={[]}} {1={1={[]}}}]
        [{1={{{[]}}}}]
        [comment too, but can be seen by processor as a comment child]
        [r''\'this comment form is more
        great.''\']
        
        {/$lalala] multiline string too, but we can choose the delimiter
\\ """ this is not a end delimiter:[alala$/}
hyfj ' \\' ()[]{} [lalala$/}-

        e{/$ala] multiline string too, but escape performs
        \\\\ will be one backslash. \\' \\" ' " ''\'' ""\"" \\0
        [ala$/}
        
        [b{/$]\\\\a[$/}- eb{/$]\\\\a[$/}]
        [{func1=] args ... \\\\ [ ] [=}]
        [e{func2=aaa] args ... \\\\ [ ] [aaa=}]
        [b{func3=] args ... \\\\ [ ] [=}]
        [be{func4=aaa] args ... \\\\ [ ] [aaa=}]
    ])
])
''', ('main', None, frozenset(), (), {}, [
    
        ('hr', None, frozenset(), (), {}, []),
        ('a', None, frozenset(), ('someargs...',), {'href':"www.xx.cn"}, [
            'goto', 'xx'
            ]),
        
        ('div', 'myname', frozenset(['type1', 'type2']), (), {}, [
            ('p', None, frozenset(), (), {}, [
                'This', 'is', 'the',
                ('span', None, frozenset(), (), {'font-size':'big'}, [
                    'content'
                    ])
                ]),

            [{frozenset():3e3}, {frozenset([frozenset()])}, frozenset(), {1:[]},
             {1:{1:[]}}, {1:frozenset()}, {1:{1:frozenset()}}],
            [{1:{frozenset()}}],
            
            ['comment', 'too,', 'but', 'can', 'be', 'seen', 'by', 'processor',
             'as', 'a', 'comment', 'child'],
            [r'''this comment form is more
        great.'''],
            ''' multiline string too, but we can choose the delimiter
\\ """ this is not a end delimiter:[alala$/}
hyfj ' \\' ()[]{} '''\
            ''' multiline string too, but escape performs
        \\ will be one backslash. ' " ' " ''\'' ""\"" \0
        ''',
            [rb'\\a\a'],
            [['func1', r' args ... \\ [ ] ']],
            [['func2', r' args ... \ [ ] ']],
            [['func3', br' args ... \\ [ ] ']],
            [['func4', br' args ... \ [ ] ']],
            ]),
        ])
     ),
    ]
