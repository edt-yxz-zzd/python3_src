
'''
concept:
    NonPathObject = Dict | ObjectArray | ObjectTuple | CharString | ByteString | Integer | Bool | None
    Object = NonPathObject | Inline_Path

tokens:
    #raw_tokens:
        #BigNewlineNoIndents
        #BigNewlineIndents1
    Indent
    Dedent
    NullIndent

    #CharStringBodyLine
    #ByteStringBodyLine
    XStringBodyLine
    Ignores1

    Name
    Integer
    RawDictKey
    Inline_ByteString
    Inline_CharString

    OP_UNINDENT_CharStringHead
    OP_UNINDENT_ByteStringHead
    OP_UNINDENT_ObjectTupleHead
    OP_UNINDENT_ObjectArrayHead
    OP_UNINDENT_DictHead

    OP_COMMA
    OP_COLON
    OP_ASSIGN
    OP_DIV
    OP_CharStringHead
    OP_ByteStringHead
    OP_ObjectTupleHead
    OP_ObjectArrayHead
    OP_DictHead

    OP_SMALL_OPEN
    OP_SMALL_CLOSE
    OP_MIDDLE_OPEN
    OP_MIDDLE_CLOSE
    OP_BIG_OPEN
    OP_BIG_CLOSE
'''

######################### unit ###########################
grammar_units = '''
WholeFile = MaybeNullIndent +TheMainObject
TheMainObject
    = Object
    | OP_UNINDENT_DictHead NullIndent +DictBody
    | OP_UNINDENT_ObjectArrayHead NullIndent +ObjectArrayBody
    | OP_UNINDENT_ObjectTupleHead NullIndent +ObjectTupleBody
    | OP_UNINDENT_CharStringHead NullIndent +CharStringBody
    | OP_UNINDENT_ByteStringHead NullIndent +ByteStringBody
Object = Inline_Object | MultiLine_Object


Inline_Object = Inline_NonPathObject | Inline_Path
Inline_NonPathObject
    = Name
    | Integer
    | Inline_ByteString
    | Inline_CharString
    | Inline_ObjectArray
    | Inline_ObjectTuple
    | Inline_Dict
MultiLine_Object
    = MultiLine_ByteString
    | MultiLine_CharString
    | MultiLine_ObjectArray
    | MultiLine_ObjectTuple
    | MultiLine_Dict



Inline_Path_OP_Item = div +Inline_NonPathObject
Inline_ListItems0 = Inline_ListItems1 | EMPTY
Inline_ListItem_OP = +Inline_Object comma
Inline_DictItems0 = Inline_DictItems1 | EMPTY
Inline_DictItem_OP = +Inline_DictItem comma


MultiLine_ByteString = OP_ByteStringHead Indent +ByteStringBody Dedent
MultiLine_CharString = OP_CharStringHead Indent +CharStringBody Dedent
MultiLine_ObjectArray = OP_ObjectArrayHead Indent +ObjectArrayBody Dedent
MultiLine_ObjectTuple = OP_ObjectTupleHead Indent +ObjectTupleBody Dedent
MultiLine_Dict = OP_DictHead Indent +DictBody Dedent
CharStringBodyLine_Null = +CharStringBodyLine NullIndent
CharStringBodyLine = XStringBodyLine


ListBodyItem_Null = +ListBodyItem NullIndent
DictBodyItem_Null = +DictBodyItem NullIndent
'''
######################### unit ###########################



################# discard below #################
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
################# discard above #################


################ XOA #############
grammar_XOAs = '''
Inline_Path_OP_Items1 Inline_Path_OP_Items0 Inline_Path_OP_Item
Inline_ListItem_OPs1 Inline_ListItem_OPs0 Inline_ListItem_OP
Inline_DictItem_OPs1 Inline_DictItem_OPs0 Inline_DictItem_OP
CharStringBodyLine_Nulls1 CharStringBodyLine_Nulls0 CharStringBodyLine_Null
ListBodyItem_Nulls1 ListBodyItem_Nulls0 ListBodyItem_Null
DictBodyItem_Nulls1 DictBodyItem_Nulls0 DictBodyItem_Null
'''
################ XOA #############

################ XOT #############
grammar_XOTs = '''
Inline_Path : Inline_Path_OP_Items1 Inline_NonPathObject
Inline_ListItems1 : Inline_ListItem_OPs0 Inline_Object
Inline_DictItems1 : Inline_DictItem_OPs0 Inline_DictItem
CharStringBodyLines1 CharStringBodyLine_Nulls0 CharStringBodyLine
ListBodyItems1 : ListBodyItem_Nulls0 ListBodyItem
ListBodyItem : Inline_ListItem_OPs0 Object
DictBodyItems1 : DictBodyItem_Nulls0 DictBodyItem
DictBodyItem : Inline_DictItem_OPs0 DictBodyTailItem
'''
################ XOT #############

######################### code ###########################
grammar_codes = '''

ByteStringBody
    CharStringBody
        # CharStringBody ==>> ByteStringBody
        return CharStringBody.encode('ascii')

CharStringBody
    CharStringBodyLines1
        assert CharStringBodyLines1
        it = iter(CharStringBodyLines1)
        def iter_parts()
            _, fst = next(it, None)
            yield fst
            for a,b in it:
                yield a
                yield b
        return ''.join(iter_parts())

Inline_ObjectArray
    middle_open Inline_ListItems0 middle_close
        return list(Inline_ListItems0)
Inline_ObjectTuple
    small_open Inline_ListItems0 small_close
        return tuple(Inline_ListItems0)
Inline_Dict
    big_open Inline_DictItems0 big_close
        return dict(Inline_DictItems0)

Inline_DictItem
    RawDictKey assign Inline_Object | Inline_CharString colon Inline_Object
        return p[1], Inline_Object

ObjectTupleBody
    ListBodyItems1
        return tuple(ListBodyItems1)
ObjectArrayBody
    ListBodyItems1
        return list(ListBodyItems1)
DictBody
    DictBodyItems1
        return dict(DictBodyItems1)
DictBodyTailItem
    RawDictKey assign Object | Inline_CharString colon Object
        return p[1], Object

EMPTY
    <>
        return List_iappendright()
'''
######################### code ###########################


__all__ = '''
    tokens
    start

    grammar_codes
    grammar_XOTs
    grammar_XOAs
    grammar_discards
    grammar_units
    '''.split()

from .MyConfiguration2_lex import terminals
from .utils.EchoLexer import EchoLexer
from .utils.set_attrs import set_attrs
from .utils.LexPostprocess import LexPostprocess
#from functools import wraps

tokens = terminals
start = 'WholeFile'

def p_error(p):
    raise Exception(p)


