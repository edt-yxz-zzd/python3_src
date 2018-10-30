
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


grammar:
WholeFile : MaybeNullIndent TheMainObject # MaybeNullIndent # EOF
TheMainObject
    : Object
    | OP_UNINDENT_DictHead NullIndent DictBody
    | OP_UNINDENT_ObjectArrayHead NullIndent ObjectArrayBody
    | OP_UNINDENT_ObjectTupleHead NullIndent ObjectTupleBody
    | OP_UNINDENT_CharStringHead NullIndent CharStringBody
    | OP_UNINDENT_ByteStringHead NullIndent CharStringBody # ByteStringBody
Object
    : Inline_Object
    | MultiLine_Object
Inline_Object
    : Inline_NonPathObject
    | Inline_Path
Inline_NonPathObject
    : Name
    | Integer
    | Inline_ByteString
    | Inline_CharString
    | Inline_ObjectArray
    | Inline_ObjectTuple
    | Inline_Dict
MultiLine_Object
    : MultiLine_ByteString
    | MultiLine_CharString
    | MultiLine_ObjectArray
    | MultiLine_ObjectTuple
    | MultiLine_Dict


EMPTY :
MaybeNullIndent
    : NullIndent
    | EMPTY
Ignores0
    : Ignores1
    | EMPTY

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


Inline_ObjectArray : middle_open Inline_ListItems0 middle_close
Inline_ObjectTuple : small_open Inline_ListItems0 small_close
Inline_Dict : big_open Inline_DictItems0 big_close

Inline_Path
    : Inline_NonPathObject Inline_Path_OP_Items1
Inline_Path_OP_Items1
    : Inline_Path_OP_Item Inline_Path_OP_Items1
    | Inline_Path_OP_Item
Inline_Path_OP_Item
    : div Inline_NonPathObject

Inline_ListItems0
    : Inline_ListItems1
    | EMPTY
Inline_ListItems1 : Inline_ListItem_OPs0 Inline_Object
#Inline_ListItems1 : Inline_Object Inline_OP_ListItems0
#Inline_OP_ListItems0
    : Inline_OP_ListItem Inline_OP_ListItems0
    | EMPTY
#Inline_OP_ListItem
    : comma Inline_Object
Inline_ListItem_OPs0
    : Inline_ListItem_OPs0 Inline_ListItem_OP
    | EMPTY
Inline_ListItem_OP
    : Inline_Object comma

Inline_DictItems0
    : Inline_DictItems1
    | EMPTY

Inline_DictItem_OPs0
    : Inline_DictItem_OPs0 Inline_DictItem_OP
    | EMPTY
Inline_DictItem_OP
    : Inline_DictItem comma
Inline_DictItems1 : Inline_DictItem_OPs0 Inline_DictItem
#Inline_DictItems1 : Inline_DictItem Inline_OP_DictItems0
#Inline_OP_DictItems0
    : Inline_OP_DictItem Inline_OP_DictItems0
    | EMPTY
#Inline_OP_DictItem
    : comma Inline_DictItem
Inline_DictItem
    : RawDictKey        assign Inline_Object
    | Inline_CharString colon Inline_Object




MultiLine_ByteString
    : OP_ByteStringHead Indent CharStringBody Dedent # ByteStringBody
MultiLine_CharString
    : OP_CharStringHead Indent CharStringBody Dedent
MultiLine_ObjectArray
    : OP_ObjectArrayHead Indent ObjectArrayBody Dedent
MultiLine_ObjectTuple
    : OP_ObjectTupleHead Indent ObjectTupleBody Dedent
MultiLine_Dict
    : OP_DictHead Indent DictBody Dedent

#ByteStringBody
    : ByteStringBodyLines1
#ByteStringBodyLines1
    : ByteStringBodyLine NullIndent ByteStringBodyLines1
    | ByteStringBodyLine
#ByteStringBodyLine : XStringBodyLine

CharStringBody
    : CharStringBodyLines1
CharStringBodyLines1
    : CharStringBodyLine NullIndent CharStringBodyLines1
    | CharStringBodyLine
CharStringBodyLine : XStringBodyLine

ObjectArrayBody
    : ListBody
ObjectTupleBody
    : ListBody


ListBody
    : ListBodyItems1
ListBodyItems1
    : ListBodyItem NullIndent ListBodyItems1
    | ListBodyItem
#ListBodyItems1
    : NonLastListBodyItem ListBodyItems1
    | LastListBodyItem

#NonLastListBodyItem
    : ListBodyItem NullIndent
#LastListBodyItem
    : ListBodyItem Dedent
#ListBodyItem
    : Inline_ListItems1 comma MultiLine_Object
    | MultiLine_Object
    | Inline_ListItems1
ListBodyItem : Inline_ListItem_OPs0 Object



DictBody
    : DictBodyItems1
DictBodyItems1
    : DictBodyItem NullIndent DictBodyItems1
    | DictBodyItem
#DictBodyItems1
    : NonLastDictBodyItem DictBodyItems1
    | LastDictBodyItem

#NonLastDictBodyItem
    : DictBodyItem NullIndent
#LastDictBodyItem
    : DictBodyItem Dedent
DictBodyItem : Inline_DictItem_OPs0 DictBodyTailItem
#DictBodyItem
    : Inline_DictItems1 comma MultiLine_DictItem
    | MultiLine_DictItem
    | Inline_DictItems1
#MultiLine_DictItem
    : RawDictKey        assign MultiLine_Object
    | Inline_CharString colon MultiLine_Object
DictBodyTailItem
    : RawDictKey        assign Object
    | Inline_CharString colon Object

"""""""""""""""""""""""""""""""""


'''


__all__ = '''
    tokens
    start
    '''.split()

from .MyConfiguration2_lex import terminals
from .utils.EchoLexer import EchoLexer
from .utils.set_attrs import set_attrs
from .utils.LexPostprocess import LexPostprocess
#from functools import wraps

tokens = terminals
start = 'WholeFile'

























###################################################
################## part ###########################
################## utils ##########################
###################################################
class LeftList:
    def __init__(self, iterable=()):
        self.__ls = list(iterable)
    def appendleft(self, obj):
        self.__ls.append(obj)
    def __iter__(self):
        return reversed(self.__ls)
class InjectRuleTo:
    '''
usage:
    inject_rule_to = InjectRuleTo(globals())
    @inject_rule_to
    class R_Star:
        def a(p):
            'R R_Star'
        def b(p):
            'EMPTY'
    ==>>
    def R_Star_a(p):
        'R R_Star'
    def R_Star_b(p):
        'EMPTY'
'''
    def __init__(self, *, globals):
        self.__globals = globals
    def __call__(self, cls):
        g = self.__globals
        rule_name = cls.__name__
        assert '_' not in rule_name
        for n, obj in cls.__dict__.items():
            if not callable(obj): continue
            func = obj
            #func_name = n #???
            func_name = func.__name__
            assert n == func_name

            alternative_name = f'p_{rule_name}_{func_name}'
            func_name = func.__name__ = alternative_name
            if alternative_name in g:
                raise KeyError(f'{alternative_name!r} already exists!')
            g[alternative_name] = func
            alternative_body = func.__doc__.lstrip()
                # = r'(\w+(\s+\w+)+)?(|(\w+(\s+\w+)+)?)*'
            rule = f'\n{rule_name} : {alternative_body}'
                # not alternative_name
            func.__doc__ = rule
        return cls

class Maybe:
    '''
usage:
    maybe_of = Maybe('EMPTY', globals=globals())
    maybe_of('Items0', 'Items1', 0)
    maybe_of('MaybeABC', 'A B C', 1)
    maybe_of('JoinSepArgs0', 'JoinSepArgs1', 0)
'''
    def __init__(self, empty_name, *, globals):
        self.__empty_name = empty_name
        self.__globals = globals
        self.__inject_rule_to = InjectRuleTo(globals)
    def __call__(self, maybe_name, item_names, value_idx):
        # item_names = 'xxx yyy'
        # item_names = ['xxx yyy', 'zzz']
        # value_idx ==>> item_value = p[value_idx(+1?+1?)]
        L, item_names, value_idx = _handle_item_names(item_names, value_idx)

        value_idx += 1
        just_body = item_names

        @self.__inject_rule_to
        @set_attrs(__name__=maybe_name)
        class C:
            @set_attrs(__doc__=just_body)
            def just(p):
                p[0] = (p[value_idx],)
            @set_attrs(__doc__=self.__empty_name)
            def empty(p):
                p[0] = ()
        return None

class Many1:
    '''
usage:
    many1_of = Many1(reverse=False, globals=globals())
    many1_of('Items1', 'Item', 0)
    many1_of('COMMA_ARG_pairs1', 'COMMA ARG', 1)
'''
    def __init__(self, *, reverse:bool, globals):
        self.__reverse = bool(reverse)
        self.__list_type = LeftList if reverse else list
        self.__globals = globals
        self.__inject_rule_to = InjectRuleTo(globals)
    def __call__(self, many1_name, item_names, value_idx):
        # item_names = 'xxx yyy'
        # item_names = ['xxx yyy', 'zzz']
        # value_idx ==>> item_value = p[value_idx(+1?+1?)]
        L, item_names, value_idx = _handle_item_names(item_names, value_idx)

        if self.__reverse:
            many2_body = f'{item_names!s} {many1_name!s}'
            value_idx += 1
            list_idx = L+1
            put = self.__list_type.appendleft
        else:
            many2_body = f'{many1_name!s} {item_names!s}'
            value_idx += 2
            list_idx = 1
            put = self.__list_type.append

        @self.__inject_rule_to
        @set_attrs(__name__=many1_name)
        class C:
            @set_attrs(__doc__=many2_body)
            def many2(p):
                ls = p[list_idx]
                put(ls, p[value_idx])
                p[0] = ls
            @set_attrs(__doc__=item_names)
            def singleton(p):
                ls = self.__list_type()
                put(ls, p[1])
                p[0] = ls
        return None

class Many0:
    '''
usage:
    many0_of = Many0('EMPTY', reverse=False, globals=globals())
    many0_of('Items0', 'Item', 0)
    many0_of('COMMA_ARG_pairs0', 'COMMA ARG', 1)
'''
    def __init__(self, empty_name, *, reverse:bool, globals):
        self.__empty_name = empty_name
        self.__reverse = bool(reverse)
        self.__list_type = LeftList if reverse else list
        self.__globals = globals
        self.__inject_rule_to = InjectRuleTo(globals)
    def __call__(self, many0_name, item_names, value_idx):
        # item_names = 'xxx yyy'
        # item_names = ['xxx yyy', 'zzz']
        # value_idx ==>> item_value = p[value_idx(+1?+1?)]
        L, item_names, value_idx = _handle_item_names(item_names, value_idx)

        if self.__reverse:
            many1_body = f'{item_names!s} {many0_name!s}'
            value_idx += 1
            list_idx = L+1
            put = self.__list_type.appendleft
        else:
            many1_body = f'{many0_name!s} {item_names!s}'
            value_idx += 2
            list_idx = 1
            put = self.__list_type.append

        @self.__inject_rule_to
        @set_attrs(__name__=many0_name)
        class C:
            @set_attrs(__doc__=many1_body)
            def many1(p):
                ls = p[list_idx]
                put(ls, p[value_idx])
                p[0] = ls
            @set_attrs(__doc__=self.__empty_name)
            def empty(p):
                p[0] = self.__list_type()
        return None
def _handle_item_names(item_names, value_idx):
    # item_names = 'xxx yyy'
    # item_names = ['xxx yyy', 'zzz']
    # -> str
    if type(item_names) is not str:
        item_names = ' '.join(item_names)
    L = len(item_names.split())

    if value_idx < 0:
        value_idx += L
    if not (0 <= value_idx < L): raise IndexError

    return L, item_names, value_idx
class Join1:
    '''
usage:
    join1_of = Join1('EMPTY', reverse=False, globals=globals())
    join1_of('ARGs1', 'ArgCommaPairs0', 'Ignores0 COMMA Ignores1', 'ARG', 0)
'''
    def __init__(self, empty_name, *, reverse:bool, globals):
        reverse = bool(reverse)

        self.__many0_of = Many0(empty_name, reverse=reverse, globals=globals)
        self.__empty_name = empty_name
        self.__reverse = reverse
        self.__list_type = LeftList if reverse else list
        self.__globals = globals
        self.__inject_rule_to = InjectRuleTo(globals)
    def __call__(self, join1_name, item_sep_pairs0_name
                , sep_names, item_names, value_idx):
        # item_names = 'xxx yyy'
        # item_names = ['xxx yyy', 'zzz']
        # value_idx ==>> item_value = p[value_idx(+1?+1?)]
        #
        # many0_of(item_names sep_names) item_names
        # item_names many0_of(sep_names item_names)
        #
        N, sep_names, _ = _handle_item_names(sep_names, 0)
        L, item_names, value_idx = _handle_item_names(item_names, value_idx)

        if self.__reverse:
            # item_names many0_of(sep_names item_names)
            self.__many0_of(item_sep_pairs0_name
                            , [sep_names, item_names], N+value_idx)
            join1_body = f'{item_names!s} {item_sep_pairs0_name!s}'
            value_idx += 1
            list_idx = L+1
            put = self.__list_type.appendleft
        else:
            # many0_of(item_names sep_names) item_names
            self.__many0_of(item_sep_pairs0_name
                            , [item_names, sep_names], value_idx)
            join1_body = f'{item_sep_pairs0_name!s} {item_names!s}'
            value_idx += 2
            list_idx = 1
            put = self.__list_type.append

        @self.__inject_rule_to
        @set_attrs(__name__=join1_name)
        class C:
            @set_attrs(__doc__=join1_body)
            def join1(p):
                ls = p[list_idx]
                put(ls, p[value_idx])
                p[0] = ls
        return None


###################################################
################## part ###########################
###################################################
#WholeFile/TheMainObject/Object
#Inline_Object/Inline_NonPathObject
#MultiLine_Object
def p_WholeFile(p):
    '''
WholeFile : MaybeNullIndent TheMainObject
'''
    p[0] = p[2]
def p_TheMainObject(p):
    '''
TheMainObject : Object
'''
    p[0] = p[1]
def p_TheMainObject(p):
    '''
TheMainObject : OP_UNINDENT_DictHead NullIndent DictBody
'''
    p[0] = dict(p[3])
def p_TheMainObject(p):
    '''
TheMainObject : OP_UNINDENT_ObjectArrayHead NullIndent ObjectArrayBody
'''
    p[0] = list(p[3])
def p_TheMainObject(p):
    '''
TheMainObject : OP_UNINDENT_ObjectTupleHead NullIndent ObjectTupleBody
'''
    p[0] = tuple(p[3])
def p_TheMainObject(p):
    '''
TheMainObject : OP_UNINDENT_CharStringHead NullIndent CharStringBody
'''
    assert type(p[3]) is str
    p[0] = p[3]
def p_TheMainObject(p):
    '''
TheMainObject : OP_UNINDENT_ByteStringHead NullIndent CharStringBody
'''
    assert type(p[3]) is str
    p[0] = p[3].encode('ascii')

def p_Object(p):
    '''
Object \
    : Inline_Object
    | MultiLine_Object
'''
    p[0] = p[1]
def p_Inline_Object(p):
    '''
Inline_Object \
    : Inline_NonPathObject
    | Inline_Path
'''
    p[0] = p[1]
def p_Inline_NonPathObject(p):
    '''
Inline_NonPathObject \
    : Name
    | Integer
    | Inline_ByteString
    | Inline_CharString
    | Inline_ObjectArray
    | Inline_ObjectTuple
    | Inline_Dict
'''
    p[0] = p[1]
def p_MultiLine_Object(p):
    '''
MultiLine_Object \
    : MultiLine_ByteString
    | MultiLine_CharString
    | MultiLine_ObjectArray
    | MultiLine_ObjectTuple
    | MultiLine_Dict
'''
    p[0] = p[1]
















###################################################
################## part ###########################
###################################################
#EMPTY/ops/Ignores0/...
def p_EMPTY(p):
    '''
EMPTY :
'''
    p[0] = None
def p_MaybeNullIndent(p):
    '''
MaybeNullIndent \
    : NullIndent
    | EMPTY
'''
def p_Ignores0(p):
    '''
Ignores0 \
    : Ignores1
    | EMPTY
'''
def p_middle_open(p):
    '''
middle_open : OP_MIDDLE_OPEN Ignores0
'''
def p_middle_close(p):
    '''
middle_close : Ignores0 OP_MIDDLE_CLOSE
'''
def p_small_open(p):
    '''
small_open : OP_SMALL_OPEN Ignores0
'''
def p_small_close(p):
    '''
small_close : Ignores0 OP_SMALL_CLOSE
'''
def p_big_open(p):
    '''
big_open : OP_BIG_OPEN Ignores0
'''
def p_big_close(p):
    '''
big_close : Ignores0 OP_BIG_CLOSE
'''
def p_comma(p):
    '''
comma : Ignores0 OP_COMMA Ignores1
'''
def p_assign(p):
    '''
assign : Ignores1 OP_ASSIGN Ignores1
'''
def p_colon(p):
    '''
colon : Ignores1 OP_COLON Ignores1
'''
def p_div(p):
    '''
div : Ignores0 OP_DIV Ignores0

'''
















###################################################
################## part ###########################
###################################################
#Inline_*
def p_Inline_ObjectArray(p):
    '''
Inline_ObjectArray : middle_open Inline_ListItems0 middle_close
'''
    p[0] = list(p[2])
def p_Inline_ObjectTuple(p):
    '''
Inline_ObjectTuple : small_open Inline_ListItems0 small_close
'''
    p[0] = list(p[2])
def p_Inline_Dict(p):
    '''
Inline_Dict : big_open Inline_DictItems0 big_close
'''
    p[0] = dict(p[2])
def p_Inline_Path(p):
    '''
Inline_Path : Inline_NonPathObject Inline_Path_OP_Items1
'''
    ls = [p[1]]
    ls.extend(p[2])
    p[0] = ls
many1_of = Many1(reverse=False, globals=globals())
many0_of = Many0('EMPTY', reverse=False, globals=globals())
maybe_of = Maybe('EMPTY', globals=globals())
join1_of = Join1('EMPTY', reverse=False, globals=globals())
TODO

def delete(f):
    ff = globals()[f.__name__]
    if ff is f: raise logic-error
    return ff
many1_of('Inline_Path_OP_Items1', 'Inline_Path_OP_Item', 0)
@delete
def p_Inline_Path_OP_Items1(p):
    '''
Inline_Path_OP_Items1\
    : Inline_Path_OP_Item Inline_Path_OP_Items1
    | Inline_Path_OP_Item
'''
def p_Inline_Path_OP_Item(p):
    '''
Inline_Path_OP_Item \
    : div Inline_NonPathObject
'''
    p[0] = p[1]
TODO
#bug:maybe_of('Inline_ListItems0', 'Inline_ListItems1', 0)
@delete
def p_Inline_ListItems0(p):
    '''
Inline_ListItems0 \
    : Inline_ListItems1
    | EMPTY
'''
join1_of('Inline_ListItems1', 'Inline_ListItem_OPs0', 'comma', 'Inline_Object', 0)
@delete
def p_Inline_ListItems1(p):
    '''
Inline_ListItems1 : Inline_ListItem_OPs0 Inline_Object
'''
    '''
#Inline_ListItems1 : Inline_Object Inline_OP_ListItems0
'''
"""
def p_Inline_OP_ListItems0(p):
    '''
#Inline_OP_ListItems0 \
    : Inline_OP_ListItem Inline_OP_ListItems0
    | EMPTY
'''
def p_Inline_OP_ListItem(p):
    '''
#Inline_OP_ListItem \
    : comma Inline_Object

'''
"""

@delete
def p_Inline_ListItem_OPs0(p):
    '''
Inline_ListItem_OPs0 \
    : Inline_ListItem_OPs0 Inline_ListItem_OP
    | EMPTY
'''
@delete
def p_Inline_ListItem_OP(p):
    '''
Inline_ListItem_OP \
    : Inline_Object comma
'''

TODO
#bug: (maybe ls1) != ls0
#       () | (ls1,) != ls0
#   maybe_of('Inline_DictItems0', 'Inline_DictItems1', 0)
@delete
def p_Inline_DictItems0(p):
    '''
Inline_DictItems0 \
    : Inline_DictItems1
    | EMPTY
'''
join1_of('Inline_DictItems1', 'Inline_DictItem_OPs0', 'comma', 'Inline_DictItem', 0)
@delete
def p_Inline_DictItems1(p):
    '''
Inline_DictItems1 : Inline_DictItem_OPs0 Inline_DictItem
'''
    '''
#Inline_DictItems1 : Inline_DictItem Inline_OP_DictItems0
'''
@delete
def p_Inline_DictItem_OPs0(p):
    '''
Inline_DictItem_OPs0 \
    : Inline_DictItem_OPs0 Inline_DictItem_OP
    | EMPTY
'''

example many1_of('Inline_Path_OP_Items1', 'Inline_Path_OP_Item', 0)
example maybe_of('Items0', 'Items1', 0)
example p[0] = p[1]
example join1_of('ARGs1', 'ArgCommaPairs0', 'Ignores0 COMMA Ignores1', 'ARG', 0)
example @delete
TODO
@delete
def p_Inline_DictItem_OP(p):
    '''
Inline_DictItem_OP \
    : Inline_DictItem comma
'''
"""
def p_Inline_OP_DictItems0(p):
    '''
#Inline_OP_DictItems0 \
    : Inline_OP_DictItem Inline_OP_DictItems0
    | EMPTY
'''
def p_Inline_OP_DictItem(p):
    '''
#Inline_OP_DictItem \
    : comma Inline_DictItem
'''
"""

def p_Inline_DictItem(p):
    '''
Inline_DictItem \
    : RawDictKey        assign Inline_Object
    | Inline_CharString colon Inline_Object
'''
    p[0] = (p[1], p[3])
















###################################################
################## part ###########################
###################################################
#MultiLine_* # except ListBody and DictBody
def p_MultiLine_ByteString(p):
    '''
MultiLine_ByteString \
    : OP_ByteStringHead Indent CharStringBody Dedent
'''
    '''
    : OP_ByteStringHead Indent CharStringBody Dedent # ByteStringBody
'''
    p[0] = p[3].encode('ascii')
def p_MultiLine_CharString(p):
    '''
MultiLine_CharString \
    : OP_CharStringHead Indent CharStringBody Dedent
'''
    p[0] = p[3]
def p_MultiLine_ObjectArray(p):
    '''
MultiLine_ObjectArray \
    : OP_ObjectArrayHead Indent ObjectArrayBody Dedent
'''
    p[0] = p[3]
def p_MultiLine_ObjectTuple(p):
    '''
MultiLine_ObjectTuple \
    : OP_ObjectTupleHead Indent ObjectTupleBody Dedent
'''
    p[0] = p[3]
def p_MultiLine_Dict(p):
    '''
MultiLine_Dict \
    : OP_DictHead Indent DictBody Dedent
'''
    p[0] = p[3]
"""#comment_out
def p_ByteStringBody(p):
    '''
ByteStringBody \
    : ByteStringBodyLines1
'''
def p_ByteStringBodyLines1(p):
    '''
ByteStringBodyLines1 \
    : ByteStringBodyLine NullIndent ByteStringBodyLines1
    | ByteStringBodyLine
'''
def p_ByteStringBodyLine(p):
    '''
ByteStringBodyLine : XStringBodyLine
'''
"""

def p_CharStringBody(p):
    '''
CharStringBody \
    : CharStringBodyLines1
'''
    it = iter(p[1]) # [(''|'\n', tail:str)]
    def iter_parts():
        for _, tail in it:
            assert _ in '\n' # discard
            yield tail
            break
        for fst, snd in it:
            assert fst in '\n'
            yield fst
        yield snd
    p[0] = ''.join(iter_parts())

@delete
def p_CharStringBodyLines1(p):
    '''
CharStringBodyLines1 \
    : CharStringBodyLine NullIndent CharStringBodyLines1
    | CharStringBodyLine

'''

def p_CharStringBodyLine(p):
    '''
CharStringBodyLine : XStringBodyLine
'''


















###################################################
################## part ###########################
###################################################
# ListBody/DictBody
def p_ObjectArrayBody(p):
    '''
ObjectArrayBody \
    : ListBody
'''
def p_ObjectTupleBody(p):
    '''
ObjectTupleBody \
    : ListBody
'''
def p_ListBody(p):
    '''
ListBody \
    : ListBodyItems1
'''
def p_ListBodyItems1(p):
    '''
ListBodyItems1 \
    : ListBodyItem NullIndent ListBodyItems1
    | ListBodyItem
'''
    '''
#ListBodyItems1 \
    : NonLastListBodyItem ListBodyItems1
    | LastListBodyItem

'''
"""
def p_NonLastListBodyItem(p):
    '''
NonLastListBodyItem \
    : ListBodyItem NullIndent
'''
def p_LastListBodyItem(p):
    '''
LastListBodyItem \
    : ListBodyItem Dedent
'''
"""

def p_ListBodyItem(p):
    '''
ListBodyItem : Inline_ListItem_OPs0 Object
'''
    '''
#ListBodyItem \
    : Inline_ListItems1 comma MultiLine_Object
    | MultiLine_Object
    | Inline_ListItems1

'''
def p_DictBody(p):
    '''
DictBody \
    : DictBodyItems1
'''
def p_DictBodyItems1(p):
    '''
DictBodyItems1 \
    : DictBodyItem NullIndent DictBodyItems1
    | DictBodyItem
'''
    '''
#DictBodyItems1 \
    : NonLastDictBodyItem DictBodyItems1
    | LastDictBodyItem
'''
"""
def p_NonLastDictBodyItem(p):
    '''
NonLastDictBodyItem \
    : DictBodyItem NullIndent
'''
def p_LastDictBodyItem(p):
    '''
LastDictBodyItem \
    : DictBodyItem Dedent
'''
"""

def p_DictBodyItem(p):
    '''
DictBodyItem : Inline_DictItem_OPs0 DictBodyTailItem
'''
    '''
#DictBodyItem \
    : Inline_DictItems1 comma MultiLine_DictItem
    | MultiLine_DictItem
    | Inline_DictItems1
'''

def p_DictBodyTailItem(p):
    '''
DictBodyTailItem \
    : RawDictKey        assign Object
    | Inline_CharString colon Object
'''

"""
def p_MultiLine_DictItem(p):
    '''
MultiLine_DictItem \
    : RawDictKey        assign MultiLine_Object
    | Inline_CharString colon MultiLine_Object
'''
"""



def p_error(p):
    raise Exception(p)


