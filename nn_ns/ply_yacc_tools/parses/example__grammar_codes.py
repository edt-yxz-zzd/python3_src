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

