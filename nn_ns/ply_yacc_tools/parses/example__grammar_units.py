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

