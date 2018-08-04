
r'''
-- pdfChar = regular | delimiter | white-space
-- pdfChar is byte; case-sensitive
PdfChar = RegularChar | DelimiterChar | WhiteSpace == byte
-- white space in comment/string/stream is not WhiteSpace
    RegularChar = byte - WhiteSpace - DelimiterChar
        token = RegularChar+ | ...
    DelimiterChar = (, ), <, >, [, ], {, }, /, %
        Any of these characters terminates the entity preceding it and is not included in the entity.
    WhiteSpace = WhiteSpace+ -- many1 as 1
        Newline = CR | LF
        EOL = LF | CR LF?
        StdEOL = CR? LF

        TABLE 3.1   White-space characters
        DECIMAL HEXADECIMAL OCTAL NAME
        0 00 000 Null (NUL)
        9 09 011 Tab (HT)
        10 0A 012 Line feed (LF)  '\n'
        12 0C 014 Form feed (FF)
        13 0D 015 Carriage return (CR) '\r'
        32 20 040 Space (SP)

Token
    = WhiteSpace+ | Comment -- Comment treat as WhiteSpace
    | RegularChar+
    | "<<" ">>"
    | DelimiterChar
    -- not inside Stream/String/Comment
Comment = '%' (byte - Newline)* EOL
    -- not in stream or string

Obj = DirectObjValue | ObjRef
ObjValue = DirectObjValue | IndirectObjValue
DirectObjValue
    = Boolean
    | Integer
    | Real
    | String
    | Name
    | Array
    | Dictionary
    -- | Stream -- an IndirectObj
    | Null
IndirectObjValue = Stream | ...
Number = Integer | Real



let Hex = [0-9A-Fa-f]
Boolean = 'true' | 'false'
Integer = [+-]? \d+ (?!.)
-- Real = [+-]? (\d+ '.' \d* | '.' \d+)
Real = [+-]? \d* '.' \d*  -  [+-]? '.'
String = LiteralString | HexLiteralString
    LiteralString = '(' _LiteralString_ ')'
    _LiteralString_ = LiteralString | [^)\\\r\n] | EscapeSeq | EOL
        -- EOL -> \n
    EscapeSeq = \\ ([nrtbf()\\] | EOL | [0-7]{1,3})
        -- EOL -> "" -- no char
    HexLiteralString = '<' (Hex | WhiteSpace | Comment)* '>'
        -- pad '0' at end to be even length
        -- WhiteSpaces are ignored
        -- what about comment?
Name = '/' (RegularChar | EscapedChar)*
    EscapedChar = '#' Hex Hex
        -- "#00" -> error
        -- must: '#' and non-RegularChar
        --      any of the delimiter or white-space characters
        --      or '#' (i.e. the number sign character itself)

let sepBy1 t s = t (s t)*
let sepBy t s = (sepBy1 t s)?
Array t = @read '[' WhiteSpace* (t WhiteSpace*)* ']' -- allow Ref or not?
        = @write '[' (sepBy t WhiteSpace) ']'
    -- it seems t is Obj, i.e. DirectObjValue or ObjRef, and not Stream

let Dict = Dictionary
Dict t = @read "<<" WhiteSpace* (Name WhiteSpace* t WhiteSpace*)* ">>"
         @write "<<" (Name WhiteSpace t)* ">>"
Stream t = (Dict t) "stream" StdEOL byte* EOL? "endstream"
    -- len(byte*) == dict["/Length"]
Null = "null"

ObjID = ObjNum WhiteSpace+ GenNum
    ObjNum = PInt
    GenNum = UInt -- <= 65535
    ObjNum may be reused if the original obj were deleted
    but the GenNum should be increased
    so never two "difference" objects have same ID no matter whether deleted
    but when a object updated, it's ID is not changed
    why do not use single number as ID?
        the ObjNum is indeed the index in CrossReferenceTable...

    Because updates are appended to PDF files, a file can have several copies of an object with the same object identifier (object number and generation number).
IndirectRef = ObjID WhiteSpace+ "R"
    -- not found <==> null
IndirectObjDef = ObjID WhiteSpace+ "obj" v "endobj" -- definition
    -- v = ObjValue or v = ObjValue | ObjRef
    --      now I think v = ObjValue | ObjRef = Obj | Stream
    -- once : xxx it seems v should not be ObjRef xxx
    -- quot "it is illegal for a compressed object to consist of only an indirect reference"
    --      compressed object : illegal => so, normally legal??

'''
from seed.helper.repr_input import repr_helper
#from decimal import Decimal
import os, re
from itertools import chain
from base64 import b16decode as decodeFromHex


delimiters = b'()<>[]{}/%'
spaces = b' \n\r\0\t\x0C'
newlines = b'\n\r'
eol_markers = (b'\n', b'\r\n', b'\r')
std_eol_markers = (b'\n', b'\r\n')
# print(repr(spaces.decode('ascii')))
# assert spaces.decode('ascii').isspace() -- \00 is not space!
assert len(spaces) == 6
def isDelimiterChar(ch):
    return ch in delimiters
def isWhiteSpace(ch):
    return ch in spaces
def isNewline(ch):
    return ch in newlines
def isRegularChar(ch):
    return not isWhiteSpace(ch) and not isDelimiterChar(ch)

SPACE = 0
DELIMITER = 1
REGULAR = 2

def not_(pred):
    return lambda x: not (pred(x))
def iter_all(it)->None:
    for _ in it: pass
def skipXSpacesAfter(method):
    def f(self):
        x = method(self)
        self.skipWhiteSpacesAndComments0()
        return x
    return f
def try_(method):
    def f(self):
        pos = self.file.tell()
        x = method(self)
        if x is not None:
            return x
        self.file.seek(pos)
        return None
    return f

def const_str(const_bytes):
    assert type(const_bytes) == bytes
    def f(self):
        #print('keyword')
        bs = self.file.read(len(const_bytes))
        if const_bytes != bs:
            return None
        return bs
    return f
def keyword(const_bytes):
    return const_str(const_bytes)
    # version 1
    # token() may read too much
    # but const_str() may not end by delimiters or spaces
    def f(self):
        # pos = self.file.tell()
        tt = self.token()
        if not tt: return
        ty, tk = tt
        if ty != REGULAR or tk != const_bytes:
            return None
        return tk
    return f
def choice(*methods):
    def f(self):
        #print('choice')
        pos = self.file.tell()
        for f in methods:
            r = f(self)
            if r is not None:
                # success
                return r
            # fail
            if pos != self.file.tell():
                # consumed ==>> error
                break
        return None
    return f
def seq(*methods):
    def f(self):
        ls = []
        for f in methods:
            obj = f(self)
            if obj is None:
                #self.file.seek(pos)
                return None
            ls.append(obj)
        return ls
    return f
def sized_bytes(L):
    assert L >= 0
    def f(self):
        bs = self.file.read(L)
        return None if len(bs) != L else bs
    return f

def is_null(result):
    return type(result) == tuple and not result


def get_type_name(result):
    t = type(result)
    if t in _types:
        return t.__name__
    if t == bytes:
        return PDF_TYPE_NAME.PDF_NAME
    if is_null(result):
        return PDF_TYPE_NAME.PDF_NULL
    if result is None:
        raise Exception('result None means fail ("null" should be "()")')
    raise Exception('unknown result type: {!r} {!r}'.format(result, t))
    '''
    if t in (bool, int, PdfFloat, dict, list, PdfStr, bytes):
        return 'PdfName' if t == bytes else t.__name__
    if t == tuple:
        L = len(result)
        if not L: return 'null'
        assert L == 2
        if type(result[0]) is dict:
            assert type(result[1]) is bytes
            return 'DictAndStream'
        assert is_ref_type(result)
        return 'R'
    raise Exception('unknown result type: {!r} {!r}'.format(result, t))
    '''

class PdfObj:
    def __init__(self, val):
        self.__obj = val
    def get(self):
        return self.__obj
    def __eq__(self, other):
        return type(self) == type(other) and self.get() == other.get()
    def __ne__(self, other):
        return not (self == other)
    def __repr__(self):
        return repr_helper(self, self.get())
    def __hash__(self):
        return hash(self.get())
class PdfFloat(PdfObj):
    #BytesDecimalFloat:
    def __init__(self, bs):
        assert type(bs) is bytes
        assert match_exactly(real_decimal_rex, bs)
        super().__init__(bs)


class PdfRef(PdfObj):
    # int int b'R'
    def __init__(self, objID):
        assert is_objID_type(objID)
        super().__init__(objID)
class PdfStr(PdfObj):
    # bytes
    def __init__(self, bs):
        assert type(bs) == bytes
        super().__init__(bs)

    #ef __bytes__(self):
    #   return self.get()
class PdfStream(PdfObj):
    # (dict, bytes)
    def __init__(self, dict_bytes):
        assert type(dict_bytes) is tuple and len(dict_bytes) == 2
        d, bs = dict_bytes
        assert type(d) == dict
        assert type(bs) == bytes
        super().__init__(dict_bytes)
def is_ref_type(ref):
    return type(ref) is PdfRef
    # ref = (objID, b'R')
    if type(ref) == tuple and len(ref) == 2 and ref[-1] == b'R':
        objID = ref[0]
        return is_objID_type(objID)
    return False
def is_objID_type(objID):
    # objID = (int, int)
    if type(objID) == tuple and len(objID) == 2:
        objNum, genNum = objID
        return type(objNum) == type(genNum) == int
    return False
# PDF_TYPE_NAME
_types = (bool, int, PdfFloat, dict, list, PdfStr, PdfRef, PdfStream)
class PDF_TYPE_NAME:
    (PDF_BOOL, PDF_INT, PDF_FLOAT, PDF_DICT, PDF_ARRAY, PDF_STRING
        , PDF_REF, PDF_STREAM) = map(lambda x:x.__name__, _types)
    PDF_NAME, PDF_NULL = 'PdfName', 'PdfNull'



class PdfFile:
    def __init__(self, binary_file, objID2offset=None):
        self.file = binary_file
        self.objID2offset = objID2offset
    def char(self)->'byte | None':
        #print(self.file.tell())
        ch = self.file.read(1)
        return ch if ch else None
    def choice_string(self, strings) -> 'bytes | None':
        file = self.file
        pos = file.tell()
        buf = b''
        for s in strings:
            L = len(s) - len(buf)
            if L > 0: buf += file.read(L)
            if s == buf:
                return buf
        file.seek(pos)
        return None
    def eol(self)->r'\r\n | \n | \r | None':
        return self.choice_string(eol_markers)
    def std_eol(self)->r'\r\n | \n | None':
        return self.choice_string(std_eol_markers)


    def iter_char_if(self, pred)->'iter_bytes':
        while True:
            ch = self.char()
            if ch is None: return
            if not pred(ch):
                self.file.seek(-1, os.SEEK_CUR)
                return
            yield ch
    def read_while(self, pred)->bytes:
        return b''.join(self.iter_char_if(pred))
    def read_until(self, pred)->bytes:
        return b''.join(self.iter_char_if(not_(pred)))
    def skip_while(self, pred)->...:
        iter_all(self.iter_char_if(pred))
        return ...
    def skip_until(self, pred)->...:
        self.skip_while(not_(pred))
        return ...
    def skipWhiteSpaces(self)->...:
        self.skip_while(isWhiteSpace)
        return ...
    def skipToNextLineOrEOF(self)->...:
        self.skip_until(isNewline)
        self.eol()
        return ...
    def skipWhiteSpacesAndComments0(self):
        while True:
            pos = self.tell()
            self.skipWhiteSpaces()
            self.comment()
            if pos == self.tell():
                break
        return ... # to avoid None as fail

    def try_char(self, ch):
        pos = self.file.tell()
        ch_ = self.char()
        if ch_ == ch:
            return ch_
        self.file.seek(pos)
    def comment(self):
        if self.try_char('%'):
            self.skipToNextLineOrEOF()
            return ...
        return None
    def token(self) -> '\x20 | id | delimiter':
        # not call me inside string/stream/comment
        ch = self.char()
        if ch is None: return None
        if isWhiteSpace(ch):
            self.skipWhiteSpaces()
            return (SPACE, ' ')
        elif isDelimiterChar(ch):
            if ch == b'%':
                # Comment
                self.skipToNextLineOrEOF()
                return (SPACE, ' ')
            if ch in b'<>':
                next = self.file.read(1)
                if next == ch:
                    ch += next
                else:
                    self.file.seek(-1, os.SEEK_CUR)
            return (DELIMITER, ch)
        # RegularChar+
        it = chain(iter([ch]), self.iter_char_if(isRegularChar))
        return (REGULAR, b''.join(it))
    def obj(self):
        ref = self.try_ref()
        if ref is not None:
            return ref
        pos = self.file.tell()
        tt = self.token()
        if tt is None: return None
        (token_type, token) = tt
        #print(pos)
        #print(tt)
        if token_type == REGULAR:
            for f in (asNull, asBool, asInteger, asReal):
                obj = f(token)
                if obj is not None:
                    return obj
            self.file.seek(pos);
            #raise self.bad('unrecognized token: {!r}'.format(token))
            # i.e. keyword "endobj"
            return None
        elif token_type == SPACE:
            raise "should skip space/comment first!"
            self.file.seek(pos);
            return None
        f = _begin2reader.get(token)
        if f is None:
            # ie. '>>' end of dict ==>> return None
            # donot seek back
            return None
        return f(self)
    def obj_(self):
        obj = self.obj()
        self.skipWhiteSpacesAndComments0()
        return obj
    obj_ = skipXSpacesAfter(obj)
    def _dict(self):
        ls = []
        self.skipWhiteSpacesAndComments0()
        while True:
            pos = self.tell()
            key = self.name()
            if key is None:
                self.seek(pos)
                break
            self.skipWhiteSpacesAndComments0()
            val = self.obj_()
            if val is None:
                raise self.bad('key without value: {}'.format(key))
            ls.append((key, val))
        tt = self.token()
        if not tt or tt[-1] != b'>>':
            raise self.bad('dict not end by ">>": {!r}'.format(tt))
        return dict(ls)
    def name(self):
        if self.char() != b'/':
            return None
        return self._name()
    def _array(self):
        ls = []
        self.skipWhiteSpacesAndComments0()
        while True:
            pos = self.tell()
            val = self.obj_()
            if val is None:
                self.seek(pos)
                break
            ls.append(val)
        tt = self.token()
        if not tt or tt[-1] != b']':
            raise self.bad('array not end by "]": {!r}'.format(tt))
        return ls
    def _name(self):
        pos = self.file.tell()
        tt = self.token()
        if not tt:
            # "/"
            return b'/'
        ty, token = tt
        if ty == REGULAR:
            #rint(token)
            r = b'/'+decodeName(token) # "#\d\d..."
            #rint(r)
            return r
        if ty == DELIMITER:
            self.file.seek(pos)
        return b'/'

    def regulars1(self):
        tt = self.token()
        if tt:
            ty, token = tt
            if ty == REGULAR:
                return token
        return None
    def _hex_str(self):
        # NOTE: ">>>" <<== "<</key<1A>>>" !!!!
        ls = []
        while True:
            tt = self.token()
            if tt is None:
                raise self.bad('reading pdf hex string: unexpected EOF')
            ty, token = tt
            if ty == REGULAR:
                ls.append(token)
            elif ty == SPACE:
                # skip comment and space
                pass
            elif token[:1] == b'>':
                # '>>' or '>'
                # seek back
                self.seek(1 - len(token), os.SEEK_CUR)
                break
            else:
                raise self.bad("reading pdf hex string: not end by '>'")
        bs = b''.join(ls)
        if len(bs) & 1:
            bs += b'0'
        if not isxdigits0(bs):
            raise self.bad("hex literal str: contain other char")
        return PdfStr(decodeFromHex(bs.upper()))
        return bytes.fromhex(bs)

        # version 1
        hs = self.read_until(lambda ch: ch == b'>')
        if len(hs)%2 != 0: hs += b'0'
        ch = self.char()
        if ch != b'>': raise logic - error
        if not isxdigits0(hs):
            raise self.bad("hex literal str: contain other char")
        return PdfStr(decodeFromHex(hs.upper()))


        hs = self.read_while(isxdigit)
        if len(hs)%2 != 0: hs += b'0'
        # bug:
        # tt = self.token()
        # if not tt or tt[-1] != b'>':
        #    raise self.bad('hex string not end by ">": {!r}'.format(tt))
        ch = self.char()
        if ch != b'>':
            raise self.bad('hex string not end by ">": {!r}'.format(ch))
        return decodeFromHex(hs)
    def _literal_str(self):
        def st():pass
        ls = []
        def init(ch):
            if ch == b'(':
                ls.append(ch)
                st.leftCount += 1
            elif ch == b')':
                ls.append(ch)
                st.leftCount -= 1
                if st.leftCount < 1:
                    st.st = final
                # will include last ')'
            elif ch == b'\\':
                st.st = esc
            elif ch == b'\r':
                st.st = may_skip_one_LF
                ls.append(b'\n') # \n not \r
            else:
                ls.append(ch)
            return True
        def may_skip_one_LF(ch):
            st.st = init
            if ch == b'\n':
                return True
            return st.st(ch) # when call init() ==>> st.st is init
        def final(ch):
            return False
        octs = []
        def esc(ch):
            x = _esc_dict.get(ch)
            _st = None
            if x is not None:
                ls.append(x)
            elif isoctdigit(ch): # b'0'<=ch<=b'7':
                _st = esc_oct
                octs[:] = [ch]
            elif ch == b'\r':
                _st = may_skip_one_LF
                pass # ignore
            elif ch == b'\n':
                pass # ignore
            else:
                raise self.bad('unknown escaped seq: {!r}'.format(ch))

            st.st = init if _st is None else _st
            return True
        def esc_oct(ch):
            if isoctdigit(ch):
                octs.append(ch)
                if len(octs) == 3:
                    complete_octs()
                return True
            else:
                complete_octs()
                return st.st(ch)
        def complete_octs():
            st.st = init
            bs = b''.join(octs)
            i = int(bs, 8)
            try:
                ch = chr(i)
            except:
                self.bad(r'bad escaped seq: {}'.format(bs))
            ls.append(ch)
        def pred(ch):
            return st.st(ch)


        st.st = init
        st.leftCount = 1
        self.skip_while(pred)
        assert ls
        assert ls[-1] == b')'
        ls.pop()
        return PdfStr(b''.join(ls))

    keyword_R, keyword_obj, keyword_endobj\
        , keyword_stream, keyword_endstream = \
        map(keyword, (b'R', b'obj', b'endobj', b'stream', b'endstream'))
    def ref(self):
        t = type(self)
        # pos = self.file.tell()
        tri = self._iiR()
        if tri is None: return
        objNum, genNum, R = tri
        if objNum <= 0 or genNum < 0:
            #self.file.seek(pos)
            raise self.bad('obj ref: {} {} R'.format(objNum, genNum))
        objID = objNum, genNum
        return PdfRef(objID)
        return (objNum, genNum, b'R')
    try_ref = try_(ref)
    def bad(self, errmsg):
        pos = self.file.tell()
        return BadFormat('file offset {}: {}'.format(pos, errmsg))

    def int(self):
        # pos = self.file.tell()
        tt = self.token()
        if not tt: return
        ty, tk = tt
        i = None if ty != REGULAR else asInteger(tk)
        # if i is None: self.file.seek(pos)
        return i
    int_ = skipXSpacesAfter(int)
    def seek(self, *args):
        return self.file.seek(*args)
    def tell(self):
        return self.file.tell()
    _iiR = seq(int_, int_, keyword_R)
    def dict(self):
        #print(self.tell())
        #print(self.file.read(2))
        if self.file.read(2) != b'<<':
            return None
        return self._dict()
        '''
def resolve_to_final(resolve1, is_ref, either_ref_val)->'value':
    # resolve_to_final resolve1 is_ref either_ref_val :: val | KeyError
    # Hashable ref =>
    # resolve1 :: ref -> Maybe (Either ref val)
    # resolve1 :: ref -> (None or KeyError) | (either_ref_val,)
    # is_ref :: either_ref_val -> Bool
    s = set()
    make_errmsg = lambda msg, ref:\
        '@resolve_to_final {!r}: ref={!r}'.format(msg, ref)
    while is_ref(either_ref_val):
        ref = either_ref_val
        if ref in s:
            raise KeyError(make_errmsg('not DAG', ref))
        s.add(ref)
        may_either_ref_val = resolve1(ref)
        if may_either_ref_val is None:
            raise KeyError(make_errmsg('not found', ref))
        either_ref_val, = may_either_ref_val
    val = either_ref_val
    return val
    def resolve_to_final(self, objID)->'value':
        assert is_objID_type(objID)
        return resolve_to_final(self.resolve1__for_final, is_ref_type, PdfRef(objID))
        '''
    def resolve_to_final(self, objID)->'value':
        s = set()
        while True:
            s.add(objID)
            val = self.resolve1(objID)
            if not is_ref_type(val):
                break
            if val in s:
                raise Exception('objID resolve: non-DAG: {}'.format(val))
            objID = val
        return val

    def resolve1__for_final(self, objID)->'(val,) | (ref,)':
        x = self.resolve1(objID)
        assert x is not None
        if is_ref_type(x):
            x = x.get()
        return (x,)
    def resolve1(self, objID)->'value | ref again':
        assert self.is_objID_type(objID)
        objNum, genNum = objID
        if self.objID2offset is None:
            raise Exception('self.objID2offset: not initial@resolve1')
        offset = self.objID2offset.get(objID)
        if offset is None:
            return () # () means "null"
        self.seek(offset)
        r = self.indirect_obj_def(bs, offset) # None as fail
        if r is None:
            raise KeyError('objID {}: offset {}; not found'.format(objID, offset))
        objID_, val = r
        if objID_ != objID:
            raise Exception('objID {}: offset {}; found other obj: {}'.format(objID, offset, objID_))
        return val

        raise NotImplementedError('resolve: {}'.format(objID))
        '''
    def is_ref_type(self, ref):
        if type(ref) == tuple and len(ref) == 2 and ref[-1] == b'R':
            objID = ref[0]
            return self.is_objID_type(objID)
        return False

    def is_objID_type(self, objID):
        if type(objID) == tuple and len(objID) == 2:
            objNum, genNum = objID
            return type(objNum) == type(genNum) == int
        return False
        '''
    def stream(self):
        r = self.stream_or_dict()
        if r is None or type(r) is dict:
            return None
        return r

    try_keyword_stream = try_(keyword_stream)
    def stream_or_dict(self):
        d = self.dict() # may only a dict instead of stream
        if d is None: return None
        self.skipWhiteSpacesAndComments0()
        if self.try_keyword_stream() is None:
            # a dict only
            return d
            return None
        # now must be stream
        L = d.get(b'/Length') # if no L then error
        if L is None or L == ():
            print(d)
            raise self.bad("stream's length is missing")
        if type(L) is not int:
            if not is_ref_type(L):
                raise self.bad("stream's length is not ref or int")
            ref = L
            objID, _ = ref
            L = self.resolve_to_final(objID)
            if L is None:
                raise self.bad("stream's length is missing: {}".format(objID))
            elif type(L) is not int:
                raise self.bad("stream's length is not int: {}".format(ID))
        assert type(L) is int
        if L < 0:
            raise self.bad("stream length error: {} < 0".format(L))
        data = self._stream(L)
        if data is None:
            raise self.bad('stream without data')
            return None
        return PdfStream((d, data))

    def _stream(self, L):
        # just after keyword"stream"
        t = type(self)
        _, data, _, _ = seq \
            ( t.std_eol
            #( keyword_stream, std_eol
            , sized_bytes(L), t.may_eol
            , t.keyword_endstream
            )(self)
        return data

    def may_eol(self):
        # r = try_(type(self).eol)()
        r = self.eol()
        if r is None:
            r = ...
        return r
    try_stream = try_(stream)
    # bug: without try!
    #    _obj_def_value = choice(stream, obj)
    #_obj_def_value = choice(try_stream, obj)
    try_stream_or_dict = try_(stream_or_dict)
    _obj_def_value = choice(try_stream, obj)
    _obj_def_value = choice(try_stream_or_dict, obj)
    _in_def = seq(int_, int_
        , keyword_obj, skipWhiteSpacesAndComments0
        , _obj_def_value, skipWhiteSpacesAndComments0
        , keyword_endobj
        )
    def indirect_obj_def(self):
        #print(self.tell())
        t = type(self)
        m = self._in_def()
        if m is None: return None
        objNum, genNum, _, _, v, _, _ = m
        if objNum <= 0 or genNum < 0:
            raise self.bad('bad obj ID: {} {}'.format(objNum, genNum))
        return (objNum, genNum), v

class BadFormat(Exception):pass

_esc_dict = {b'n':b'\n', b'r':b'\r', b't':b'\t', b'b':b'\b', b'f':b'\f', b'(':b'(', b')':b')', b'\\':b'\\'}
            
xdigit_rex = re.compile(b'[0-9a-fA-F]')
xdigits1_rex = re.compile(b'[0-9a-fA-F]+')
xdigits0_rex = re.compile(b'[0-9a-fA-F]*')
# _name_rex && /RegularChar* but this is a pre-condition
_name_rex = re.compile(b'(?:[^#]|#[0-9a-fA-F][0-9a-fA-F])*')
_name_replace_rex = re.compile(b'#..')
_name_replace_finer_rex = re.compile(
    b'#{hex}{hex}'.replace(b'{hex}', xdigit_rex.pattern))
def isxdigits0(bs):
    return match_exactly(xdigits0_rex, bs)
def isoctdigit(b):
    return b'0' <= b <= b'7'


def match_exactly(rex, string):
    m = rex.match(string)
    return m and m.end() == len(string)

def isxdigit(b):
    return len(b) == 1 and xdigits1_rex.match(b)

def decodeName(token):
    # name = b'/' + token
    if not match_exactly(_name_rex, token):
        raise BadFormat('Name bad format: {!r}'.format(token))
    def f(m):
        assert m
        s = m.group()
        assert len(s) == 3
        assert s[:1] == b'#'
        hexs = s[1:]
        if not isxdigits0(hexs):
            raise BadFormat('Name bad format: {!r}, {!r}'.format(token, s))
        b = decodeFromHex(hexs)
        assert len(b) == 1
        # forbid b == b'\0'??
        return b
        return bytes(int(s[1:], 16))
    return _name_replace_rex.sub(f, token)
assert decodeName(b'#3233#33./') == b'2333./'

_cls = PdfFile
_begin2reader =\
    { b'<<': _cls._dict
    , b'(': _cls._literal_str
    , b'<': _cls._hex_str
    , b'[': _cls._array
    , b'/': _cls._name
    }


def asX(f, rex, string):
    if match_exactly(rex, string):
        return f(string)
    return None
def _asX(rex_f):
    rex, f = rex_f
    return lambda string: asX(f, rex, string)
bool_rex = re.compile(rb'true|false')
int_rex = re.compile(rb'[+-]?\d+')
real_decimal_rex = re.compile(rb'[+-]?(?:\.\d+|\d+\.\d*)')
    # bug: b'.' v.s. rb'\.'
    #   r'' and '\.' !!!

asBool, asInteger, asReal = map(_asX,
    [ (bool_rex, lambda bs: len(bs) == 4)
    , (int_rex, int)
    , (real_decimal_rex, lambda bs: PdfFloat(bs)) #.decode('ascii')))
    ])
def asNull(token):
    if token == b'null':
        return ()
    return None
# def asHexLiteralString(3 token)->bytes:


path = r'C:\Users\Administrator\Desktop\x.pdf'
with open(path, 'rb') as fin:
    pdf = PdfFile(fin)
    i = 0
    while True:
        pdf.skipWhiteSpacesAndComments0()
        obj = pdf.indirect_obj_def()
        if obj is None:
            break
        i += 1
    print(fin.tell())
    print('total: {}'.format(i))



