
SRRTL = 'state_rex_raw_tokenization_language'

mainID = mainID_MyLL1L_of_SRRTL = 'SRRTL_in_MyLL1L'

SRRTL_in_MyLL1L = parser_specification_of_SRRTL_in_MyLL1L = r'''

SRRTL_in_MyLL1L = define_state +
define_state = state_id , newline , sub_define_block # match begins from main state_id;
                                                     # match means startswith in top layer
sub_define_block = indent , define_block , dedent    # find the first match.
                                                     # if none: if in top layer: return
                                                     #         else using parent type_id
define_block = define_token_type +
define_token_type
    named_define = name_eq , define_body
    unnamed_define = define_body # named by parent or discarded if top layer

name_eq = type_id , '='
define_body
    normal_define = define , newline , sub_define_block ? # match means complete match in sublayer
    define_if_clause = if_clause ? , state_op , newline   # if match, generate a token for pre_match;
                                                          # if in top layer, pre_match = ''

define
    rex = rex                  # if match, step in define_body
    otherwise is t'otherwise'  # step in define_body
    
if_clause = if , rex          # an anchor; match the remain string; doesnot consume any char
state_op
    goto = goto , state_id     # call_stack[-1] = state_id;
    call = call , state_id     # call_stack.push(state_id);
    return is t'return'        # call_stack.pop();
    error = error , strings ?  # call_stack.clear(); raise

rex = strings
state_id = name
type_id = name
name
    id is t'id'
    idstrings = idstring +
strings = string +


idstring is t'idstring'
string is t'string'
if is t'if'
goto is t'goto'
call is t'call'
error is t'error'

'=' is t'='
newline is t'\n'

indent is t'\t'
dedent is t'\b'
'''
