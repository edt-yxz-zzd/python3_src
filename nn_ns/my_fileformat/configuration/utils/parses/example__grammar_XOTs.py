grammar_XOTs = '''
Inline_Path : Inline_Path_OP_Items1 Inline_NonPathObject
Inline_ListItems1 : Inline_ListItem_OPs0 Inline_Object
Inline_DictItems1 : Inline_DictItem_OPs0 Inline_DictItem
CharStringBodyLines1 : CharStringBodyLine_Nulls0 CharStringBodyLine
ListBodyItems1 : ListBodyItem_Nulls0 ListBodyItem
ListBodyItem : Inline_ListItem_OPs0 Object
DictBodyItems1 : DictBodyItem_Nulls0 DictBodyItem
DictBodyItem : Inline_DictItem_OPs0 DictBodyTailItem
'''

