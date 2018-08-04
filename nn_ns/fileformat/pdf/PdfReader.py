

'''
pdf 1.4
1.
1) header -> version
    "%PDF1\.\d{eof}"
2) read startxref
    last line == '%%EOF'
    prev line == '(\d+){whitespace}*?({comment}|{eof})' ==>> xref_addr
    prev line == 'startxref{eof}'

2. input : version, xref_addr
    output : xref_table(freelist, objID2offset), trailer_dict
1) check version <= 1.4
    seek(xref_addr)
2) read xref_table ==>> Map uint (uint, uint, (in_use|free))
    '(xref{eof}({begin_mayObjNum:uint} {size:uint}{eof}(\d{{10}} \d{{5}} [fn]( [\r\n]|\r\n))*)+)+'
3) skip whitespaces and comment
4) read trailer_dict
    'trailer{eof}{dict}{eof}' followed by the prev 'startxref' keyword
5) if /Prev in trailer_dict
    prev xref_addr = trailer_dict[/Prev]
    then return to 2) to read prev xref

3. input : xref_table, trailer_dict
1) read out all objects ==>> Map (pint, uint) (Bool|Integer|Float|()|...)
    -- but leave the string/stream data undecoded

4. input : all_objects_dict, trailer_dict, user_password
1) decrypt string/stream in body except the encryption_dict
    for each (objID, obj):
        compute encrypt key(objID)
        for string/stream in obj:
            decrypt and replace

5. input : decrypted_all_objects_dict, freelist, trailer_dict, version
1) output pdf without user_password
    del /Prev! since Prev trailer_dict and xref_table are not objs
        and be refered by relative position or offset
        if we have merge them into the final ones, then we neednot them

    ...
'''



import os, re
from itertools import repeat
import Objects
from Objects import PdfFile, PdfStream, PdfStr\
    , get_type_name, PDF_TYPE_NAME, is_ref_type\
    , isRegularChar, delimiters, spaces, decodeName
import io # BytesIO
from Encryption import DecryptPDF1_4, PADDING_BYTES
from base64 import b16decode as decodeFromHex, b16encode as encodeToHex


version_rex = re.compile(rb'^%PDF-(\d+)\.(\d+)')
def read_version(pdf):
    # binary file
    pdf.seek(0)
    bs = pdf.read1(100)
    m = version_rex.match(bs)
    if not m:
        return None
    a, b = m.group(1,2)
    a = int(a)
    b = int(b)
    return (a,b)
whitespace_rex = re.compile(rb'[ \n\r\t\f\0]')
eof_rex = re.compile(rb'(?:\n|\r\n?)')
newline_rex = re.compile(rb'[\n\r]')
not_newline_rex = re.compile(rb'[^\n\r]')
eof2_rex = re.compile(rb'(?:\r\n)')
pad_eof_rex = re.compile(
    rb'(?: {newline}|{eof2})'
    .replace(rb'{eof2}', eof2_rex.pattern)
    .replace(rb'{newline}', newline_rex.pattern)
    )
comment_rex = re.compile(
    rb'(?:%.*?({eof}|$))'
    .replace(rb'{eof}', eof_rex.pattern)
    )
skip_stuff_rex = re.compile(
    rb'(?:(?:{whitespace}+|{comment})*)'
    .replace(rb'{whitespace}', whitespace_rex.pattern)
    .replace(rb'{comment}', comment_rex.pattern)
    )
startxref_rex = re.compile(
    rb'(?:.*?[\r\n]startxref{eof}(?P<startxref>\d+){whitespace}*?({comment}|{eof})%%EOF{eof}?)'
    .replace(rb'{eof}', eof_rex.pattern)
    .replace(rb'{comment}', comment_rex.pattern)
    .replace(rb'{whitespace}', whitespace_rex.pattern)
    )
_reversed_startxref_rex = re.compile(
    rb'(?:{newline}*{not_newline}+{newline}){3}'
    .replace(rb'{newline}', newline_rex.pattern)
    .replace(rb'{not_newline}', not_newline_rex.pattern)
    )

xref_entry_rex = re.compile(
    rb'(?:(\d{10}) (\d{5}) ([fn]){pad_eof})'
    .replace(rb'{pad_eof}', pad_eof_rex.pattern)
    )
xref_subsection_header_rex = re.compile(
    rb'(?:(\d+) (\d+){eof})'
    .replace(rb'{eof}', eof_rex.pattern)
    )
xref_section_header_rex = re.compile(
    rb'(?:xref{eof})'
    .replace(rb'{eof}', eof_rex.pattern)
    )


def reverse_bytes(bs):
    bs = bytearray(bs)
    bs.reverse()
    return bytes(bs)
def read_startxref(pdf, *, size=1024):
    pdf.seek(-size, os.SEEK_END)
    bs = pdf.read()
    if True:
        # reverse direction
        rs = reverse_bytes(bs)
        m = _reversed_startxref_rex.match(rs)
        if m is None: return None
        bs = reverse_bytes(m.group(0))
    # print(repr(bs))
    m = startxref_rex.match(bs)
    if m is None: return None
    addr = int(m.group('startxref'))
    return addr



def phase1(pdf):
    v = read_version(pdf)
    a = read_startxref(pdf)
    if None in [v,a]:
        print('error in phase1(pdf): version:{}, startxref:{}'.format(v,a))
        return None
    return (v, a)

xref_rex = re.compile(
    rb'(?:xref{eof}({begin_mayObjNum:uint} {size:uint}{eof}(\d{{10}} \d{{5}} [fn]( [\r\n]|\r\n))*)+)+'
    )
def _skip0(bs, begin):
    m = skip_stuff_rex.match(bs, begin)
    if not m: raise logic-error
    return m.end()

def _read_xref_entry(bs, begin):
    # return (int, int, bool), end
    m = xref_entry_rex.match(bs, begin)
    if not m: return
    i, j, fn = m.groups()
    i = int(i)
    j = int(j)
    b = fn == b'n'
    return (i, j, b), m.end()
def _read_xref_subsection(bs, begin):
    # return (int, int, ls), end
    m = xref_subsection_header_rex.match(bs, begin)
    if not m: return
    i, j = m.groups()
    begin_mayObjNum = int(i)
    size = int(j)
    begin = m.end()
    ls, begin = _read_many0(bs, begin, _read_xref_entry, max=size)
    if len(ls) < size:
        raise Exception('not enough xref_entries in xref_subsection')
    assert len(ls) == size
    return (begin_mayObjNum, size, ls), begin
def _read_many0(bs, begin, reader, max=None):
    rng = repeat(0) if max is None else range(max)
    ls = []
    for _ in rng:
        m = reader(bs, begin)
        if not m: break
        r, begin = m
        ls.append(r)
    return ls, begin
def _read_xref_section(bs, begin):
    # [(int, int, [(int, int, bool)])], int
    # [(begin_mayObjNum, size, [(..., ..., f|n)])], end
    m = xref_section_header_rex.match(bs, begin)
    if not m:
        #rint(begin, bs[begin:begin+10]) # del me
        return None
    begin = m.end()
    ls, begin = _read_many0(bs, begin, _read_xref_subsection)
    return ls, begin
def read_xref(version, xref_addr, bs, begin):
    assert version <= (1, 4)
    #pdf.seek(xref_addr)
    #bs = pdf.read()
    #begin = 0
    ls, begin = _read_many0(bs, begin, _read_xref_section)
    # [[(int, int, [(int, int, bool)])]]
    #print(ls)
    if not ls:
        raise Exception('no xref table found!')
    #pdf.seek(xref_addr+(begin-0))
    return ls, begin
def foldl1(bin_op, iterable):
    it = iter(iterable)
    for head in it:break
    else: raise Exception('foldr1 but no elem')
    for x in it: head = bin_op(head, x)
    return head
def xref_table_foldr1(xref_table2dict, xref_tables):
    # xref_tables :: from most recently to oldest
    return dict_foldr1(xref_table2dict, xref_tables)
def dict_foldr1(elem2dict, elems):
    # elems :: from most recently to oldest
    ls = list(map(elem2dict, elems))
    # foldr
    def update(self, other):
        dict.update(self, other) # -> None
        return self               # -> dict
    d = foldl1(update, reversed(ls))
    return d

def merge_xref_tables_to_objID2offset(xref_tables):
    #ls = [objNum2genNum_offset for objNum2genNum_offset, _, __ in
    #        map(xref_table2dict, xref_tables)]
    xref_table2dict = xref_table2objNum2genNum_offset
    d = xref_table_foldr1(xref_table2dict, xref_tables)
    # use objID as key
    objID2offset = \
        {(objNum, genNum):offset for objNum, (genNum, offset) in d.items()}
    return objID2offset
def xref_table2objNum2genNum_offset(xref_table):
    objNum2genNum_offset, _1, _2, _3 = xref_table2dict_ex(xref_table)
    return objNum2genNum_offset
def xref_table2objNum2genNum_nextObjNum(xref_table):
    _0, objNum2genNum_nextObjNum, _2, _3 = xref_table2dict_ex(xref_table)
    return objNum2genNum_nextObjNum
def xref_table2dict_ex(xref_table):
    d = {}
    for section in xref_table:
        for begin_mayObjNum, size, entries in section:
            assert size == len(entries)
            d.update(enumerate(entries, begin_mayObjNum))
    objNum2genNum_offset = \
        { mayObjNum : (genNum, offset)
        # for sake of overwrite, objNum instead of objID
        #{ (mayObjNum, genNum) : offset
        for mayObjNum, (offset, genNum, isInUse) in d.items()
        if isInUse
        }
    objNum2genNum_nextObjNum = \
        { mayObjNum : (thisNewGenNum, nextObjNum)
        for mayObjNum, (nextObjNum, thisNewGenNum, isInUse) in d.items()
        if not isInUse
        }
    xref_map = d
    return objNum2genNum_offset, objNum2genNum_nextObjNum\
         , xref_table, xref_map
def skip_str(const_str, bs, begin):
    if bs.startswith(const_str, begin):
        begin += len(const_str)
        return begin
    return None
def read_trailer_dict(bs, begin):
    #rint('read_trailer_dict', begin) # del me
    begin = skip_str(b'trailer', bs, begin)
    if begin is None:
        raise Exception('trailer_dict not found')
    begin = _skip0(bs, begin)
    r = read_dict(bs, begin)
    if not r:
        raise Exception('fail to read trailer_dict')
    d, begin = r
    assert d is not None
    return d, begin
def read_dict(bs, begin):
    fin = io.BytesIO(bs)
    fin.seek(begin)
    pdf = PdfFile(fin)
    d = pdf.dict()
    if d is None:
        return None
    return d, pdf.tell()

def phase2(version, xref_addr, bs):
    addr_xref_trailerdict_ls = []
    while True:
        xref, begin = read_xref(version, xref_addr, bs, xref_addr)
        #rint(xref, begin)
        begin = _skip0(bs, begin)
        (trailer_dict, begin) = read_trailer_dict(bs, begin)
        #rint(len(trailer_dict), trailer_dict) # del me
        addr_xref_trailerdict_ls.append((xref_addr, xref, trailer_dict))
        xref_addr = trailer_dict.get(b'/Prev')
        if xref_addr is None:
            break
    #rint(addr_xref_trailerdict_ls)
    #rint(len(addr_xref_trailerdict_ls))
    mk_xref_tables = lambda:\
        (table for _, table, _ in addr_xref_trailerdict_ls)
    objID2offset = merge_xref_tables_to_objID2offset(mk_xref_tables())
    freelist = xref_table_foldr1(xref_table2objNum2genNum_nextObjNum
        , mk_xref_tables()
        )
    trailer_dict = dict_foldr1(lambda tri:tri[-1], addr_xref_trailerdict_ls)
    #trailer_dict.discard(b'/Prev')
    trailer_dict.pop(b'/Prev', None)
    #rint(objID2offset)
    return objID2offset, freelist, trailer_dict, addr_xref_trailerdict_ls





def resolve1_objID(objID2offset, objID, bs):
    # None - error; known offset, but fail to read
    # () - null or no objID
    # val
    offset = objID2offset.get(objID)
    if offset is None:
        return () # () as null
    r = read_indirect_obj(bs, offset) # None as fail
    if r is None:
        raise Exception('objID {}: offset {}; not found'.format(objID, offset))
        return None
    objID_, val = r
    if objID_ != objID:
        raise Exception('objID {}: offset {}; found other obj: {}'.format(objID, offset, objID_))
        return None
    return val

def __make_pdf(bs, begin, objID2offset=None):
    fin = io.BytesIO(bs)
    fin.seek(begin)
    pdf = PdfFile(fin, objID2offset)
    return pdf
def read_indirect_obj(bs, begin):
    pdf = __make_pdf(bs, begin)
    r = pdf.indirect_obj_def()
    if r is None:
        return None
    objID, val = r
    objNum, genNum = objID
    return objID, val
def resolve_to_final__val(objID2val, objID):
    s = set()
    while True:
        s.add(objID)
        val = objID2val.get(objID)
        if val is None: return () # 'null
        if not is_ref_type(val): return val
        objID, _ = val
        if objID in s: raise Exception('recur: obj ref: {}'.format(val))

def resolve_to_final__offset(objID2offset, objID, bs):
    pdf = __make_pdf(bs, 0, objID2offset)
    val = pdf.resolve_to_final()
    return val
def read_all_objs(objID2offset, bs):
    # resolve1_objID(objID2offset, (90, 0), bs)
    objID2val = {objID: resolve1_objID(objID2offset, objID, bs)
                    for objID, offset in objID2offset.items()
                }
    return objID2val
def phase3(objID2offset, bs):
    objID2val = read_all_objs(objID2offset, bs)
    return objID2val

class NotEncrypted(Exception):pass
def get_encryption_dict(objID2val, trailer_dict):
    encryption_dict_or_ref = trailer_dict.get(b'/Encrypt')
    if encryption_dict_or_ref is None:
        raise NotEncrypted('not encrypted')
    if get_type_name(encryption_dict_or_ref) == PDF_TYPE_NAME.PDF_REF:
        # ref
        ref = encryption_dict_or_ref
        objID = ref.get()
        encryption_dict = resolve_to_final__val(objID2val, objID)
    else:
        encryption_dict = encryption_dict_or_ref

    tn = get_type_name(encryption_dict)
    if tn == PDF_TYPE_NAME.PDF_NULL:
        # null ==>> no /Encrypt key
        raise NotEncrypted('not encrypted')
    if tn != PDF_TYPE_NAME.PDF_DICT:
        raise Exception('TypeError: value of encryption_dict is not a dict')
    return encryption_dict
def decrypt_all_data(passwords, objID2val, trailer_dict
    , *, forceIfPasswordFail=False):
    # should not decrypt encryption_dict; but I donot care
    encryption_dict = get_encryption_dict(objID2val, trailer_dict)
    Filter = encryption_dict[b'/Filter']
    if Filter != b'/Standard':
        raise NotImplementedError('not standard filter: {!r}'.format(Filter))

    decryptor = DecryptPDF1_4__StandardFilter(
        encryption_dict, trailer_dict, passwords
        , forceIfPasswordFail=forceIfPasswordFail)
    d = {objID: decryptor.decrypt_val(objID, val)
            for objID, val in objID2val.items()
        }

    return d

def phase4(passwords, objID2val, trailer_dict
        , *, forceIfPasswordFail=False):
    try:
        d = decrypt_all_data(passwords, objID2val, trailer_dict
            , forceIfPasswordFail=forceIfPasswordFail)
        trailer_dict = trailer_dict.copy()
        del trailer_dict[b'/Encrypt']
        user_password = b'' # unsecured pdf
    except NotEncrypted:
        d = objID2val
        user_password = None
    return user_password, d, trailer_dict

class OutputPdf1_4:
    def __init__(self, file):
        self.file = file
    encoding = 'ascii'
    def write(self, bs):
        self.file.write(bs)
    def tell(self):
        return self.file.tell()
    def wb(self, bs):
        return self.write(bs)
    def ws(self, s):
        return self.wb(s.encode(self.encoding))
    def write_pdf(self, version, objID2val, freelist, trailer_dict):
        write_pdf(self, version, objID2val, freelist, trailer_dict)
def output_pdf(path_or_file, version, objID2val, freelist, trailer_dict, *, mode='xb'):
    def f(out):
        pdf = OutputPdf1_4(out)
        pdf.write_pdf(version, objID2val, freelist, trailer_dict)
    if not isinstance(path_or_file, str):
        file = path_or_file
        f(file)
    else:
        fname = path_or_file
        with open(fname, mode) as fout:
            f(fout)
def write_pdf(file, version, objID2val, freelist, trailer_dict):
    # assert b'/Encrypt' not in trailer_dict
    assert isinstance(file, OutputPdf1_4)
    assert version <= (1, 4)
    if b'/Prev' in trailer_dict:
        raise NotImplementedError(
            "'/Prev' in trailer_dict"
            "\n\t - not supported yet;"
            "\n\t - merge xref_table and trailer_dict first!"
            )
    wb = file.wb
    ws = file.ws
    tell = file.tell
    # header
    ma, mi = version
    # bug: only one '%'
    #   ws('%%PDF-{}.{}\n'.format(ma, mi))
    ws('%PDF-{}.{}\n'.format(ma, mi))
    objID2offset = {}
    for objID, val in sorted(objID2val.items()):
        objID2offset[objID] = tell()
        write_indirect_obj_def(file, objID, val)
    xref_addr = tell()
    write_xref(file, objID2offset, freelist)
    # trailer_dict
    wb(b'trailer\n')
    write_dict(file, trailer_dict)
    wb(b'\nstartxref\n')
    write_int(file, xref_addr)
    wb(b'\n%%EOF\n')
def write_int(file, i):
    assert get_type_name(i) == PDF_TYPE_NAME.PDF_INT
    file.ws(str(i))
def write_name(file, name):
    assert get_type_name(name) == PDF_TYPE_NAME.PDF_NAME
    # bug: without escape
    #   file.wb(name)
    file.wb(escape_name(name))
def escape_name(name):
    assert type(name) == bytes
    assert name
    if name[:1] != b'/':
        raise Exception("PdfName not startswith b'/': {!r}".format(name))
    if b'\0' in name:
        raise Exception(r"PdfName contains b'\0': {!r}".format(name))
    clear_name = name[1:]
    cipher_name = bytes(i for ch in clear_name
                            for i in _escape_name_tran(ch))
    assert clear_name == decodeName(cipher_name)
    return b'/' + cipher_name

def need_to_escape_in_name(ch):
    return ch in b'#' or not isRegularChar(ch)
isRegularChar
delimiters
def _escape_char(ch):
    assert 0 <= ch < 0x100
    r = b'#' + encodeToHex(bytes([ch]))
    assert len(r) == 3
    return r
    r = '#{:0>2X}'.format(ch).encode()
_to_escape = b'#'+delimiters+spaces
_sharp = b'#'[0]
_escape_dict =\
    {ch: _escape_char(ch)
    for ch in range(0x100) if need_to_escape_in_name(ch)}
def _escape_name_tran(ch):
    return _escape_dict.get(ch, bytes([ch]))
#print(escape_name(b'/#.<'))
assert escape_name(b'/#.<') == b'/#23.#3C'

def write_null(file, null):
    assert get_type_name(null) == PDF_TYPE_NAME.PDF_NULL
    file.wb(b'null')
def write_float(file, float):
    assert get_type_name(float) == PDF_TYPE_NAME.PDF_FLOAT
    file.wb(float.get())
def write_bool(file, bool):
    assert get_type_name(bool) == PDF_TYPE_NAME.PDF_BOOL
    file.wb(b'true' if bool else b'false')
def write_string(file, string):
    assert get_type_name(string) == PDF_TYPE_NAME.PDF_STRING
    wb = file.wb
    wb(b'<')
    wb(encodeToHex(string.get()))
    wb(b'>')
def write_stream(file, stream):
    assert get_type_name(stream) == PDF_TYPE_NAME.PDF_STREAM
    d, data = stream.get()
    wb = file.wb
    write_dict(file, d)
    wb(b'\nstream\n')
    wb(data)
    wb(b'\nendstream')

def write_dict(file, d):
    assert get_type_name(d) == PDF_TYPE_NAME.PDF_DICT
    wb = file.wb
    wb(b'<<')
    for name, obj in sorted(d.items()):
        write_name(file, name)
        # with ' '
        wb(b' ')
        write_obj(file, obj)
    wb(b'>>')
def write_array(file, ls):
    assert get_type_name(ls) == PDF_TYPE_NAME.PDF_ARRAY
    wb = file.wb
    wb(b'[')
    for obj in ls:
        write_obj(file, obj)
        wb(b' ')
    wb(b']')


def write_ref(file, ref):
    assert get_type_name(ref) == PDF_TYPE_NAME.PDF_REF
    wb = file.wb
    objNum, genNum = ref.get()
    write_int(file, objNum)
    wb(b' ')
    write_int(file, genNum)
    wb(b' R')
def write_XXX(file, XXX):
    assert get_type_name(XXX) == PDF_TYPE_NAME.PDF_
    file.wb(XXX)

typename2writer =\
    { PDF_TYPE_NAME.PDF_NULL : write_null
    , PDF_TYPE_NAME.PDF_NAME : write_name
    , PDF_TYPE_NAME.PDF_INT : write_int
    , PDF_TYPE_NAME.PDF_FLOAT : write_float
    , PDF_TYPE_NAME.PDF_BOOL : write_bool
    , PDF_TYPE_NAME.PDF_STRING : write_string
    , PDF_TYPE_NAME.PDF_STREAM : write_stream
    , PDF_TYPE_NAME.PDF_DICT : write_dict
    , PDF_TYPE_NAME.PDF_ARRAY : write_array
    , PDF_TYPE_NAME.PDF_REF : write_ref
    #, PDF_TYPE_NAME.PDF_ : write_
    }
def write_obj(file, obj):
    t = get_type_name(obj)
    typename2writer[t](file, obj)
def write_indirect_obj_def(file, objID, obj):
    wb = file.wb
    objNum, genNum = objID
    write_int(file, objNum)
    wb(b' ')
    write_int(file, genNum)
    wb(b' obj\n')
    write_obj(file, obj)
    wb(b'\nendobj\n')
def write_xref(file, objID2offset, freelist):
    wb = file.wb
    wb(b'xref\n')
    for begin_objNum, entries in mk_xref_entriess(objID2offset, freelist):
        write_int(file, begin_objNum)
        # bug: forgot ' '
        wb(b' ')
        write_int(file, len(entries))
        wb(b'\n')
        for entry in entries:
            wb(entry2bytes(entry))
    return
def mk_xref_entriess(objID2offset, freelist):
    # -> [(begin_objNum, [(int, int, '[fn]')])]
    objNum2entry = {objNum: (offset, genNum, 'n')
                    for (objNum, genNum), offset in objID2offset.items()}
    objNum2free = {objNum: (nextObjNum, newGenNum, 'f')
                    for objNum, (newGenNum, nextObjNum) in freelist.items()}
    dups = set(objNum2entry) & set(objNum2free)
    if dups:
        raise Exception('objNum duplicates: {}'.format(dups))
    objNum2entry.update(objNum2free)
    prev_objNum = -2
    lsls = []
    for objNum, entry in sorted(objNum2entry.items()):
        if objNum != prev_objNum+1:
            begin_objNum = objNum
            ls = []
            lsls.append((begin_objNum, ls))
        ls.append(entry)
        # bug: forgot increase prev_objNum
        prev_objNum = objNum
    return lsls
def entry2bytes(entry):
    x, gen, fn = entry
    assert gen <= 65535
    assert fn in 'fn'
    r = '{:0>10} {:0>5} {!s} \n'.format(x, gen, fn)
    r = r.encode('ascii')
    assert len(r) == 20
    return r

class DecryptPDF1_4__StandardFilter(DecryptPDF1_4):
    def __init__(self, encryption_dict, trailer_dict, passwords=None
                , *, forceIfPasswordFail=False):
        # try both user_password or owner_password
        super().__init__(encryption_dict, trailer_dict)
        if not passwords:
            # passwords = [PADDING_BYTES, b'']
            passwords = [b'']
        user_passwords = \
            [user_password
                for password in passwords
                for user_password in
                [password, self.owner_password2user_password(password)]
            ]
        passwords = set(map(self.padded_password, user_passwords))
        for user_password in passwords:
            if self.authenticating_user_password(user_password):
                print('authenticating_user_password: success!!!') # del me
                break
        else:
            if not forceIfPasswordFail:
                raise Exception('authenticating password fail')
            user_password = passwords[0]

        self.encryption_key = self.computing_encryption_key(user_password)
        self.user_password = user_password
        self.objID2key = {}
    def MD5(self):
        return super().MD5()
    def RC4(self, key, **kwargs):
        return super().RC4(key, **kwargs)
    def key_for_RC4(self, objID):
        return self.key_for_RC4orAES('RC4', self.encryption_key, objID)
    def get_obj_key(self, objID):
        key = self.objID2key.get(objID)
        if key is None:
            key = self.key_for_RC4(objID)
            self.objID2key[objID] = key
        return key
    def decrypt_bytes(self, objID, bs):
        key = self.get_obj_key(objID)
        bs_ = self.RC4_decrypt(key)(bs).finish()
        assert len(bs_) == len(bs)
        return bs_
    def decrypt_val(self, objID, val):
        val = self._decrypt_val(objID, val)
        get_type_name(val) # verify
        return val
    def _decrypt_val(self, objID, val):
        t = get_type_name(val)
        P = PDF_TYPE_NAME
        this_f = self.decrypt_val
        if t == P.PDF_ARRAY:
            f = lambda val: this_f(objID, val)
            return list(map(f, val))
        if t == P.PDF_DICT:
            # f = lambda (key, val): (key, this_f(objID, val))
            def f(pair):
                key, val = pair
                return key, this_f(objID, val)
            return dict(map(f, val.items()))
        if t == P.PDF_STRING:
            s = PdfStr(self.decrypt_bytes(objID, val.get()))
            return s
            print('decrypted string: {!r}'.format(s))
            print('decrypted string: {!r}'.format(bytes(s).decode('utf8')))
            return s
        if t == P.PDF_STREAM:
            d, data = val.get()
            return PdfStream((d, self.decrypt_bytes(objID, data)))
        if t in ( P.PDF_INT
                , P.PDF_FLOAT
                , P.PDF_NULL
                , P.PDF_NAME
                , P.PDF_BOOL
                , P.PDF_REF
                ):
            return val
def read_pdf(path, file=None, content=None):
    if content is not None:
        return read_pdf__file(None, content)
    if file is not None:
        return read_pdf__file(file)
    if path is None:
        raise Exception('read_pdf: all args are None')
    with open(path, 'rb') as pdf:
        return read_pdf__file(pdf)
def read_pdf__file(file, content=None):
    # content is None or file content
    # or file is None but content is bytes

    if file is None:
        if content is None:
            raise Exception('read_pdf__file: both args are None')
        file = io.BytesIO(content)

    pdf = file; del file # binary file
    bs = content; del content
    pos = pdf.tell()
    r = phase1(pdf)
    if r is None:
        raise Exception('not pdf file: {!r}'.format(path))
    version, xref_addr = r; del r

    # after verify, we read out all bytes
    if bs is None:
        pdf.seek(0)
        bs = pdf.read()

    objID2offset, freelist, trailer_dict, addr_xref_trailerdict_ls =\
                            phase2(version, xref_addr, bs)
    objID2val = phase3(objID2offset, bs)

    # ???
    # bug: should merge?? and remove /Prev
    #   trailer_dict = addr_xref_trailerdict_ls[0][-1]
    #output_pdf(output_pdfname, version, objID2val, freelist, trailer_dict, mode='wb')
    return (objID2val, trailer_dict)\
            , (version, freelist)\
            , (xref_addr, objID2offset, addr_xref_trailerdict_ls)
def verify_pdf_readwrite(path, file=None, content=None):
    (objID2val, trailer_dict), (version, freelist), _ =\
        read_pdf(path, file, content)
    out = io.BytesIO()
    output_pdf(out, version, objID2val, freelist, trailer_dict, mode='wb')
    (_objID2val, _trailer_dict), (_version, _freelist), _ =\
        read_pdf(None, out, out.getvalue())
    assert objID2val == _objID2val
    assert trailer_dict == _trailer_dict
    assert version == _version
    assert freelist == _freelist


def unsecured_pdf(output_path_or_file
                # these three for input
                , input_path, file=None, content=None
                , *, verify=True, passwords=(b'',)
                , output_open_mode='xb'):
    path = input_path
    if verify:
        verify_pdf_readwrite(path, file, content)
    (objID2val, trailer_dict), (version, freelist), _ = \
        read_pdf(path, file, content)
    if False:
        encryption_dict = get_encryption_dict(objID2val, trailer_dict)
        O = encryption_dict[b'/O']
        U = encryption_dict[b'/U']
        P = encryption_dict[b'/P']
        R = encryption_dict[b'/R']
        Length = encryption_dict[b'/Length']
        ID_0 = trailer_dict[b'/ID'][0]
        default_user_password = b''
        assert DecryptPDF1_4__StandardFilter\
            ._authenticating_user_password\
            (O,P,ID_0, R,Length, U, default_user_password)
        return

    #passwords = None
    _, objID2val, trailer_dict = phase4(
        passwords, objID2val, trailer_dict)
    if isinstance(output_path_or_file, str):
        is_file = False
        out_path = output_path_or_file
        def to_verify():
            verify_pdf_readwrite(out_path)
    else:
        is_file = True
        out_file = output_path_or_file
        pos = out_file.tell()
        assert pos == 0 #???
        def to_verify():
            out_file.seek(pos)
            verify_pdf_readwrite(None, out_file)
    if not verify:
        def to_verify():pass
    output_pdf(output_path_or_file
                , version, objID2val
                , freelist, trailer_dict
                , mode = output_open_mode
                )
    to_verify()

def main():
    # bug: since I have modified the /P in "x.pdf" !!
    #   path = r'C:\Users\Administrator\Desktop\x.pdf'
    root = r'C:\Users\Administrator\Desktop'
    output_pdfname = r'\y.pdf'
    path = r'\XML in a Nutshell (2ed)(2002)[chapter 1,2,3].pdf'
    path = r'\t.pdf'
    path = r'\XML in a Nutshell (2ed)(2002)[chapter 1,2,3][SECURED].pdf'
    path = root + path
    output_pdfname = root + output_pdfname


    verify_pdf_readwrite(path)
    #raise stop-here
    unsecured_pdf(output_pdfname, path)





if __name__ == '__main__':
    main()
