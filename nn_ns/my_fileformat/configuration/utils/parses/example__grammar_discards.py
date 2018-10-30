grammar_discards = '''
MaybeNullIndent : NullIndent | EMPTY
Ignores0 : Ignores1 | EMPTY

middle_open : OP_MIDDLE_OPEN Ignores0
middle_close : Ignores0 OP_MIDDLE_CLOSE
small_open : OP_SMALL_OPEN Ignores0
small_close : Ignores0 OP_SMALL_CLOSE
big_open : OP_BIG_OPEN Ignores0
big_close : Ignores0 OP_BIG_CLOSE
comma : Ignores0 OP_COMMA Ignores1
assign : Ignores1 OP_ASSIGN Ignores1
colon : Ignores1 OP_COLON Ignores1
div : Ignores0 OP_DIV Ignores0
'''

