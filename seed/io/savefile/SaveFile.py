
r'''

>>> encoding = 'u8'
>>> kwargs = {'a':b'', 0:[]}

######################################
>>> ofile = io.StringIO()
>>> obj = {1:3, (2,3):[43, 'bbb']}
>>> aPprintSingleObject = aSaveFile__PprintSingleObject
>>> aPprintSingleObject.write_whole(ofile, obj, encoding=encoding, kwargs=kwargs)
>>> print(ofile.getvalue())
--^^--^ nn_ns text Save File ^^--^^-
^^---^^ encoding = 'u8' --^^^--
{0
: []
,'\x00@@file_type@@\x00'
: 'pprint single object'
,'a'
: b''
}
=====
{
    1
    : 3
    ,(
        2
        ,3
    )
    : [
        43
        ,'bbb'
    ]
}
<BLANKLINE>

>>> __ = ofile.seek(0); ifile = ofile
>>> r = aPprintSingleObject.read_whole(ifile)
>>> stable_repr(r)
"('u8', {0: [], 'a': b''}, {1: 3, (2, 3): [43, 'bbb']})"


######################################
>>> ofile = io.StringIO()
>>> obj = [(1,2), ([], ()), ('', 3, b'', {1:2}), (), (1,)]
>>> aTuplePerBlock = aSaveFile__TuplePerBlock
>>> aTuplePerBlock.write_whole(ofile, obj, encoding=encoding, kwargs=kwargs)
>>> print(ofile.getvalue())
--^^--^ nn_ns text Save File ^^--^^-
^^---^^ encoding = 'u8' --^^^--
{0
: []
,'\x00@@file_type@@\x00'
: 'tuple per block'
,'a'
: b''
}
=====
[1
,2
]
[[]
,()
]
[''
,3
,b''
,{1: 2}
]
[]
[1
]
<BLANKLINE>

>>> __ = ofile.seek(0); ifile = ofile
>>> r = aTuplePerBlock.read_whole(ifile)
>>> stable_repr(r)
"('u8', {0: [], 'a': b''}, [(1, 2), ([], ()), ('', 3, b'', {1: 2}), (), (1,)])"



######################################
>>> ofile = io.StringIO()
>>> obj = [(1,2), ([], ()), ('', 3, b'', {1:2}), (), (1,)]
>>> aObjectPerLine = aSaveFile__ObjectPerLine
>>> aObjectPerLine.write_whole(ofile, obj, encoding=encoding, kwargs=kwargs)
>>> print(ofile.getvalue())
--^^--^ nn_ns text Save File ^^--^^-
^^---^^ encoding = 'u8' --^^^--
{0
: []
,'\x00@@file_type@@\x00'
: 'object per line'
,'a'
: b''
}
=====
(1, 2)
([], ())
('', 3, b'', {1: 2})
()
(1,)
<BLANKLINE>

>>> __ = ofile.seek(0); ifile = ofile
>>> r = aObjectPerLine.read_whole(ifile)
>>> stable_repr(r)
"('u8', {0: [], 'a': b''}, [(1, 2), ([], ()), ('', 3, b'', {1: 2}), (), (1,)])"


######################################
>>> ofile = io.StringIO()
>>> obj = {1:2, ():[], (1,2,3):3, '':b''}
>>> aUpdatableDict = aSaveFile__UpdatableDict
>>> aUpdatableDict.write_whole(ofile, obj, encoding=encoding, kwargs=kwargs)

>>> print(ofile.getvalue())
--^^--^ nn_ns text Save File ^^--^^-
^^---^^ encoding = 'u8' --^^^--
{0
: []
,'\x00@@file_type@@\x00'
: 'updatable dict'
,'a'
: b''
}
=====
?1
: 2
.
?''
: b''
.
?()
: []
.
?(1, 2, 3)
: 3
.
<BLANKLINE>

>>> __ = ofile.seek(0); ifile = ofile
>>> r = aUpdatableDict.read_whole(ifile)
>>> stable_repr(r)
"('u8', {0: [], 'a': b''}, {1: 2, '': b'', (): [], (1, 2, 3): 3})"


######################################
>>> ofile = io.StringIO()
>>> obj = {(1,2), ('abc', ()), ('', 3, b''), (), (1,)}
>>> aUpdatableSet = aSaveFile__UpdatableSet
>>> aUpdatableSet.write_whole(ofile, obj, encoding=encoding, kwargs=kwargs)

>>> print(ofile.getvalue())
--^^--^ nn_ns text Save File ^^--^^-
^^---^^ encoding = 'u8' --^^^--
{0
: []
,'\x00@@file_type@@\x00'
: 'updatable set'
,'a'
: b''
}
=====
?()
?(1,)
?(1, 2)
?('abc', ())
?('', 3, b'')
<BLANKLINE>

>>> __ = ofile.seek(0); ifile = ofile
>>> r = aUpdatableSet.read_whole(ifile)
>>> stable_repr(r)
"('u8', {0: [], 'a': b''}, {(), (1,), (1, 2), ('abc', ()), ('', 3, b'')})"



############# create...
>>> ofile = io.StringIO()
>>> obj = (1,2,[3,4])
>>> create_SaveFile__PprintSingleObject(ofile, obj, encoding=encoding, kwargs=kwargs)
>>> print(ofile.getvalue())
--^^--^ nn_ns text Save File ^^--^^-
^^---^^ encoding = 'u8' --^^^--
{0
: []
,'\x00@@file_type@@\x00'
: 'pprint single object'
,'a'
: b''
}
=====
(
    1
    ,2
    ,[
        3
        ,4
    ]
)
<BLANKLINE>



>>> ofile = io.StringIO()
>>> obj = (1,2,[3,4])
>>> create_or_extend_SaveFile__ObjectPerLine(ofile, obj, encoding=encoding, kwargs=kwargs)
>>> create_or_extend_SaveFile__ObjectPerLine(ofile, reversed(obj), encoding=encoding, kwargs=kwargs)
>>> print(ofile.getvalue())
--^^--^ nn_ns text Save File ^^--^^-
^^---^^ encoding = 'u8' --^^^--
{0
: []
,'\x00@@file_type@@\x00'
: 'object per line'
,'a'
: b''
}
=====
1
2
[3, 4]
--^^--^ nn_ns text Save File ^^--^^-
^^---^^ encoding = 'u8' --^^^--
{0
: []
,'\x00@@file_type@@\x00'
: 'object per line'
,'a'
: b''
}
=====
[3, 4]
2
1
<BLANKLINE>



>>> ofile = io.StringIO()
>>> obj = ((), (1,))
>>> create_or_extend_SaveFile__TuplePerBlock(ofile, obj, encoding=encoding, kwargs=kwargs)
>>> _ = ofile.seek(0)
>>> obj = ((2, 3), (0, 3, 4, 5))
>>> create_or_extend_SaveFile__TuplePerBlock(ofile, obj, encoding=encoding, kwargs=kwargs)
>>> print(ofile.getvalue())
--^^--^ nn_ns text Save File ^^--^^-
^^---^^ encoding = 'u8' --^^^--
{0
: []
,'\x00@@file_type@@\x00'
: 'tuple per block'
,'a'
: b''
}
=====
[]
[1
]
[2
,3
]
[0
,3
,4
,5
]
<BLANKLINE>


>>> ofile = io.StringIO()
>>> obj = {1,2}
>>> create_or_update_SaveFile__UpdatableSet(ofile, obj, encoding=encoding, kwargs=kwargs)
>>> _ = ofile.seek(0)
>>> obj = {(1,2),3}
>>> create_or_update_SaveFile__UpdatableSet(ofile, obj, encoding=encoding, kwargs=kwargs)
>>> print(ofile.getvalue())
--^^--^ nn_ns text Save File ^^--^^-
^^---^^ encoding = 'u8' --^^^--
{0
: []
,'\x00@@file_type@@\x00'
: 'updatable set'
,'a'
: b''
}
=====
?1
?2
?3
?(1, 2)
<BLANKLINE>


>>> ofile = io.StringIO()
>>> obj = {1:2, 0:3}
>>> create_or_update_SaveFile__UpdatableDict(ofile, obj, encoding=encoding, kwargs=kwargs)
>>> _ = ofile.seek(0)
>>> obj = {1:3, 0:4}
>>> create_or_update_SaveFile__UpdatableDict(ofile, obj, encoding=encoding, kwargs=kwargs)
>>> _ = ofile.seek(0);
>>> e, kw, obj_ = aUpdatableDict.read_whole(ofile)
>>> e == encoding
True
>>> kw == kwargs
True
>>> obj_ == obj
True
>>> print(ofile.getvalue())
--^^--^ nn_ns text Save File ^^--^^-
^^---^^ encoding = 'u8' --^^^--
{0
: []
,'\x00@@file_type@@\x00'
: 'updatable dict'
,'a'
: b''
}
=====
?0
: 3
.
?1
: 2
.
?0
: 4
.
?1
: 3
.
<BLANKLINE>




################# SaveFileContainerABC
>>> mk = lambda T, iofile, kwargs: T(iofile, encoding='u8', allow_create_file=False, allow_write_file=True, allow_write_header=True, kwargs=kwargs)
>>> iofile = io.StringIO()
>>> T = SaveFileSet
>>> C = mk(T, iofile, kwargs)
>>> C.add(1)
>>> C.add(2)
>>> C.remove(1)
>>> del C
>>> _ = iofile.seek(0)
>>> C = mk(T, iofile, kwargs)
>>> C.add(3)
>>> C.remove(2)
>>> del C
>>> print(iofile.getvalue())
--^^--^ nn_ns text Save File ^^--^^-
^^---^^ encoding = 'u8' --^^^--
{0
: []
,'\x00@@file_type@@\x00'
: 'updatable set'
,'a'
: b''
}
=====
>2
/2
>3
<BLANKLINE>



>>> iofile = io.StringIO()
>>> T = SaveFileDict
>>> C = mk(T, iofile, kwargs)
>>> C[1] = 2
>>> C[3] = 4
>>> C[5] = 6
>>> del C[3]
>>> C[1] = 7
>>> del C
>>> _ = iofile.seek(0)
>>> C = mk(T, iofile, kwargs)
>>> C[-1] = -2
>>> C[-3] = -4
>>> C[-5] = -6
>>> del C[-3]
>>> del C[5]
>>> C[-1] = -7
>>> C[1] = -1
>>> del C
>>> print(iofile.getvalue())
--^^--^ nn_ns text Save File ^^--^^-
^^---^^ encoding = 'u8' --^^^--
{0
: []
,'\x00@@file_type@@\x00'
: 'updatable dict'
,'a'
: b''
}
=====
>1
: 7
.
>5
: 6
.
/5
.
@1
: -1
.
>-5
: -6
.
>-1
: -7
.
<BLANKLINE>


>>> iofile = io.StringIO()
>>> T = SaveFileSeq__ObjectPerLine
>>> C = mk(T, iofile, kwargs)
>>> C.append(1)
>>> C.extend([2, 3])
>>> C += [4, 5]
>>> del C
>>> _ = iofile.seek(0)
>>> C = mk(T, iofile, kwargs)
>>> C += [6]
>>> del C
>>> print(iofile.getvalue())
--^^--^ nn_ns text Save File ^^--^^-
^^---^^ encoding = 'u8' --^^^--
{0
: []
,'\x00@@file_type@@\x00'
: 'object per line'
,'a'
: b''
}
=====
1
2
3
4
5
6
<BLANKLINE>


>>> iofile = io.StringIO()
>>> T = SaveFileSeq__TuplePerBlock
>>> C = mk(T, iofile, kwargs)
>>> C.append(())
>>> C.extend([(1,), (2,3)])
>>> C += []
>>> del C
>>> _ = iofile.seek(0)
>>> C = mk(T, iofile, kwargs)
>>> C += [(4,)]
>>> del C
>>> print(iofile.getvalue())
--^^--^ nn_ns text Save File ^^--^^-
^^---^^ encoding = 'u8' --^^^--
{0
: []
,'\x00@@file_type@@\x00'
: 'tuple per block'
,'a'
: b''
}
=====
[]
[1
]
[2
,3
]
[4
]
<BLANKLINE>


'''


__all__ = '''
    SaveFileMethods__PprintSingleObject
    SaveFileSet
    SaveFileDict
    SaveFileSeq__ObjectPerLine
    SaveFileSeq__TuplePerBlock

    SaveFileException
    Global




    to_std_encoding
    write_savefile_header
    read_savefile_header
    verify_or_setup_savefile_header


    create_SaveFile__PprintSingleObject
    create_or_extend_SaveFile__ObjectPerLine
    create_or_extend_SaveFile__TuplePerBlock
    create_or_update_SaveFile__UpdatableSet
    create_or_update_SaveFile__UpdatableDict

    SaveFileABC
        SaveFile__PprintSingleObject
            aSaveFile__PprintSingleObject
        SaveFile__ObjectPerLine
            aSaveFile__ObjectPerLine
        SaveFile__TuplePerBlock
            aSaveFile__TuplePerBlock
        SaveFile__UpdatableDict
            aSaveFile__UpdatableDict
        SaveFile__UpdatableSet
            aSaveFile__UpdatableSet

    SaveFileMethodsABC
        SaveFileMethods__PprintSingleObject
        SaveFileMethods__ObjectPerLine
            SaveFileSeq__ObjectPerLine
        SaveFileMethods__TuplePerBlock
            SaveFileSeq__TuplePerBlock
        SaveFileMethods__UpdatableSet
            SaveFileSet
        SaveFileMethods__UpdatableDict
            SaveFileDict


    SaveFileContainerABC
        SaveFileSet
        SaveFileDict
        SaveFileSeqABC
            SaveFileSeq__ObjectPerLine
            SaveFileSeq__TuplePerBlock

    '''.split()
    #obj_or_calc_f_to_obj

import os # SEEK_END
import io # StringIO
import binascii # hexlify
import ast # literal_eval
import re
import copy # deepcopy
from collections import OrderedDict
from seed.abc import abstractmethod, override, ABC# final
from seed.helper.safe_eval import safe_eval
from seed.helper.stable_repr import (
    stable_repr
    ,stable_repr_print
    ,sorted_by_SortableIterReprable
    ,sorted_mapping_by_SortableIterReprable
    )
from seed.text.encodings import to_std_encoding as _to_std_encoding
from seed.io.is_file_EOF import is_file_EOF__by_seek, is_file_EOF__by_read_seek

#from seed.helper.fprint import fprint

def to_std_encoding(encoding):
    encoding = _to_std_encoding(encoding)
    encoding = encoding.replace('-', '_')
    return encoding


class SaveFileException(Exception):
    def __init__(self, *args, **kwargs):
        self.kwargs = kwargs
        super().__init__(*args)


class Global:
    begin_of_header_EOL = "--^^--^ nn_ns text Save File ^^--^^-\n"
    encoding_decl_EOL_fmt = "^^---^^ encoding = {nonstd_encoding!r} --^^^--\n"
    end_of_header_EOL = "=====\n"

    file_type_key_name = '\x00@@file_type@@\x00'
    PprintSingleObject = 'pprint single object'
    ObjectPerLine = 'object per line'
    TuplePerBlock = 'tuple per block'
    UpdatableDict = 'updatable dict'
    UpdatableSet = 'updatable set'

    ##########
    def _f(fmt=encoding_decl_EOL_fmt):
        left = fmt[:fmt.index('{')]
        right = fmt[fmt.index('}')+1:]
        _left_pattern = re.escape(left)
        _right_pattern = re.escape(right)
        encoding_decl_EOL_rex = re.compile(f'{_left_pattern}\s*(?P<nonstd_encoding_literal>\S+)\s*{_right_pattern}')
        return encoding_decl_EOL_rex
    encoding_decl_EOL_rex = _f(); del _f

_1level_expand_kwargs = dict(indent='', depth=0, maybe_max_depth=1, has_head_eol_when_indent=False)
def write_savefile_header(ofile, encoding, information):
    write = ofile.write
    write(Global.begin_of_header_EOL)
    write(Global.encoding_decl_EOL_fmt.format(nonstd_encoding=encoding))
    stable_repr_print(ofile, information, **_1level_expand_kwargs)
    write('\n')
    write(Global.end_of_header_EOL)
def read_savefile_header(ifile):
    '-> (encoding, information)'
    begin_of_header_EOL = ifile.read(len(Global.begin_of_header_EOL))
    if begin_of_header_EOL != Global.begin_of_header_EOL:
        raise SaveFileException('not a "nn_ns text Save File": not have good begin_of_header_EOL')

    encoding_decl_EOL = ifile.readline()
    if encoding_decl_EOL[-1:] != '\n':
        raise SaveFileException('unexpected EOF when reading encoding_decl_EOL')
    m = Global.encoding_decl_EOL_rex.fullmatch(encoding_decl_EOL)
    if not m:
        encoding_decl = encoding_decl_EOL[:-1]
        raise SaveFileException(f'bad format: encoding_decl: {encoding_decl!r}', encoding_decl=encoding_decl)

    nonstd_encoding_literal = m['nonstd_encoding_literal']; del m
    encoding = ast.literal_eval(nonstd_encoding_literal)
    if type(encoding) is not str:
        raise SaveFileException(f'bad format: nonstd_encoding_literal: {nonstd_encoding_literal!r}')

    lines = []
    for line in ifile:
        if line.startswith('='):
            break
        lines.append(line)
    else:
        raise SaveFileException('unexpected EOF when reading information dict')

    end_of_header_EOL = line
    if end_of_header_EOL != Global.end_of_header_EOL:
        raise SaveFileException(f'bad format: end_of_header_EOL: {end_of_header_EOL!r}')

    information_literal = ''.join(lines)
    try:
        information = safe_eval(information_literal)
    except Exception:
        raise SaveFileException(f'bad format: information: {information_literal!r}')
    if type(information) not in (dict, OrderedDict):
        raise SaveFileException(f'bad type: information: not dict/OrderedDict: {type(information)!r}')

    return encoding, information



def _test_read_savefile():
    header = r'''--^^--^ nn_ns text Save File ^^--^^-
^^---^^ encoding =   "xxxx"   --^^^--
{
1

: 2
}
=====
text
'''
    fin = io.StringIO(header)
    encoding, information = read_savefile_header(fin)
    assert encoding == 'xxxx'
    assert information == {1:2}
    assert fin.read() == 'text\n'
_test_read_savefile()

def verify_or_setup_savefile_header(
    iofile, encoding, information, *, allow_write_header:bool
    ):
    should_write = is_file_EOF__by_read_seek(iofile)
    if should_write:
        if not allow_write_header:
            raise SaveFileException('empty file is not a savefile')
        start_pos = iofile.tell()
        write_savefile_header(iofile, encoding, information)
        iofile.seek(start_pos)

    encoding_, information_ = read_savefile_header(iofile)
    if to_std_encoding(encoding_) != to_std_encoding(encoding):
        if should_write: raise logic-error
        raise SaveFileException(f'not match: encoding: expected={encoding!r}, actual={encoding_!r}')
    if stable_repr(information_) != stable_repr(information):
        if should_write: raise logic-error
        raise SaveFileException(f'not match: information: expected={information!r}, actual={information_!r}')
    return None


class SaveFileABC(ABC):
    __slots__ = ()
    @abstractmethod
    def get_file_type_enum_name(self):
        raise NotImplementedError
    @abstractmethod
    def read_body(self, ifile):
        raise NotImplementedError
    @abstractmethod
    def write_body(self, ofile, obj):
        raise NotImplementedError
    def get_file_type(self):
        enum_name = self.get_file_type_enum_name()
        file_type = getattr(Global, enum_name)
        return file_type

    def open_verify_or_create_setup_savefile_header(self
        ,path_or_iofile, *
        ,encoding, kwargs
        ,allow_create_file:bool
        ,allow_write_file:bool
        ,allow_write_header:bool
        ):
        '-> return maybe_iofile # (None|iofile)'
        #bug: if allow_create_file: allow_write_file = True
        to_seek_0 = True
        if allow_write_file:
            mode = 'a+t' if allow_create_file else 'r+t'
            #!!!!!!!!!!!! ==>> seek(0)
        else:
            allow_create_file = False
            ###########
            assert not allow_create_file
            allow_write_header = False
            mode = 'rt'

        information = self.make_information(kwargs=kwargs)
        def f(iofile):
            verify_or_setup_savefile_header(
                iofile, encoding, information
                , allow_write_header=allow_write_header)

        if hasattr(path_or_iofile, 'readline'):
            iofile = path_or_iofile
            f(iofile)
            return None
        else:
            path = path_or_iofile
            iofile = open(path, mode, encoding=encoding)
            try:
                iofile.seek(0)
                f(iofile)
            except:
                iofile.close(); del iofile
                raise
            return iofile
    def make_information(self, *, kwargs):
        file_type_key_name = Global.file_type_key_name
        file_type = self.get_file_type()
        if file_type_key_name in kwargs:
            raise ValueError(f'kwargs contains file_type_key_name {file_type_key_name!r}')
        information = {file_type_key_name: file_type, **kwargs}
        return information
    def write_header(self, ofile, *, encoding, kwargs):
        if not is_file_EOF__by_seek(ofile): raise Exception('not EOF')

        information = self.make_information(kwargs=kwargs)
        write_savefile_header(ofile, encoding, information)


    def information2kwargs(self, information):
        kwargs = dict(information)
        file_type = self.get_file_type()
        file_type_key_name = Global.file_type_key_name

        Nothing = []
        may_file_type = kwargs.pop(file_type_key_name, Nothing)
        if may_file_type is Nothing:
            raise SaveFileException(f'not {file_type!r} savefile: has no file_type_key_name {file_type_key_name!r} in input dict "information"')
        else:
            file_type_ = may_file_type
            if file_type_ != file_type:
                raise SaveFileException(f'not {file_type!r} savefile: actual file_type is {file_type_!r}')
        return kwargs


    def read_header(self, ifile):
        '-> (encoding, kwargs)'
        file_type = self.get_file_type()
        (encoding, information) = read_savefile_header(ifile)
        kwargs = self.information2kwargs(information)
        return encoding, kwargs

    def read_whole(self, ifile, *, header_only=False):
        encoding, kwargs = self.read_header(ifile)
        if header_only:
            return encoding, kwargs
        obj = self.read_body(ifile)
        return encoding, kwargs, obj
    def write_whole(self, ofile, obj, *, encoding, kwargs):
        self.write_header(ofile, encoding=encoding, kwargs=kwargs)
        self.write_body(ofile, obj)


class SaveFile__PprintSingleObject(SaveFileABC):
    __slots__ = ()
    @override
    def get_file_type_enum_name(self):
        return 'PprintSingleObject'
    @override
    def read_body(self, ifile):
        object_literal = ifile.read()
        obj = safe_eval(object_literal)
        return obj
    @override
    def write_body(self, ofile, obj):
        stable_repr_print(ofile, obj, depth=0)
        ofile.write('\n')



comment_line_rex = re.compile('^\s*#|^\s*$')
#tuple_end_line_rex = re.compile('^\s*\)')
class SaveFile__ObjectPerLine(SaveFileABC):
    __slots__ = ()
    @override
    def get_file_type_enum_name(self):
        return 'ObjectPerLine'
    @override
    def read_body(self, ifile):
        return list(self.iter_read_body(ifile))
    def iter_read_body(self, ifile):
        for line in ifile:
            if comment_line_rex.match(line):
                continue
            object_literal = line
            obj = safe_eval(object_literal)
            yield obj
    def write_line(self, ofile, obj):
        stable_repr_print(ofile, obj)
        ofile.write('\n')
    @override
    def write_body(self, ofile, iterable):
        write_line = self.write_line
        for obj in iterable:
            write_line(ofile, obj)

class SaveFile__TuplePerBlock(SaveFileABC):
    __slots__ = ()
    @override
    def get_file_type_enum_name(self):
        return 'TuplePerBlock'
    @override
    def read_body(self, ifile):
        return list(self.iter_read_body(ifile))
    def iter_read_body(self, ifile):
        for line in ifile:
            if comment_line_rex.match(line):
                continue
            if not line.startswith('['):
                raise SaveFileException('bad format: not startswith "["')
            if line.startswith('[]'):
                yield tuple(ast.literal_eval(line))
                continue

            lines = [line]
            for line in ifile:
                lines.append(line)
                if line.startswith(']'): #!!!!!!!!!!
                    break
            else:
                raise Exception('unexpected EOF: when reading a block tuple')
            object_literal = ''.join(lines)
            obj = safe_eval(object_literal)
            obj = tuple(obj)
            yield obj
    def write_tuple(self, ofile, tuple_):
        assert type(tuple_) is tuple
        it = iter(tuple_)
        write = ofile.write
        write('[') # !!!!!
        for obj in it:
            stable_repr_print(ofile, obj)
            write('\n')
            break
        for obj in it:
            write(',')
            stable_repr_print(ofile, obj)
            write('\n')
        write(']')
        ofile.write('\n')

    @override
    def write_body(self, ofile, tuples):
        write_tuple = self.write_tuple
        for obj in tuples:
            write_tuple(ofile, obj)



class SaveFile__UpdatableDict(SaveFileABC):
    __slots__ = ()
    caseNEW = '>'
    caseOVERWRITE = '@'
    caseNEWorOVERWRITE = '?'
    caseDELETE = '/'
    all_cases = caseNEW, caseOVERWRITE, caseNEWorOVERWRITE, caseDELETE

    @override
    def get_file_type_enum_name(self):
        return 'UpdatableDict'
    @override
    def read_body(self, ifile):
        Nothing = []
        d = {}
        for case,k,v in self.iter_read_body(ifile):
            if case == self.caseDELETE:
                del d[k]
                continue
            ####
            if case == self.caseNEW:
                if k in d:
                    raise SaveFileException('caseNEW but exists')
            elif case == self.caseOVERWRITE:
                if k not in d:
                    raise SaveFileException('caseOVERWRITE but not exists')
            elif case == self.caseNEWorOVERWRITE:
                pass
            else:
                raise logic-error
            d[k] = v
        return d
    def iter_read_body(self, ifile):
        '-> (case, key, value)'
        state0 = self.all_cases
        state1 = ':'
        state2 = '.'

        state = state0
        for line in ifile:
            if comment_line_rex.match(line):
                continue
            case = line[0]
            if case not in state:
                raise SaveFileException(f'bad format: case: {case!r}  not in {state!r}')

            if state == state0:
                key = safe_eval(line[1:])
                if case == self.caseDELETE:
                    state = state2
                    value = None
                else:
                    state = state1
                case0 = case
            elif state == state1:
                value = safe_eval(line[1:])
                state = state2
            else:
                assert state == state2
                if not comment_line_rex.match(line[1:]):
                    raise SaveFileException(f'bad format: {line!r}')
                yield case0, key, value
                del case0, key, value
                state = state0

    def write_item(self, ofile, case, key, value):
        if case not in self.all_cases:
            raise ValueError(f'bad case: {case!r}')
        write = ofile.write
        write(case)
        stable_repr_print(ofile, key); write('\n')
        if case != self.caseDELETE:
            write(': ')
            stable_repr_print(ofile, value); write('\n')
        write('.\n')

    @override
    def write_body(self, ofile, mapping):
        #self.write_items(ofile, mapping.items())
        pairs = sorted_mapping_by_SortableIterReprable(mapping, key=None, reverse=False, SortableIterReprable=None)
        self.write_items(ofile, pairs)
    def write_items(self, ofile, pairs):
        write_item = self.write_item
        case = self.caseNEWorOVERWRITE
        for key, value in pairs:
            write_item(ofile, case, key, value)




class SaveFile__UpdatableSet(SaveFileABC):
    __slots__ = ()
    caseNEW = '>'
    caseADD = '?'
    caseDELETE = '/'
    all_cases = caseNEW, caseADD, caseDELETE
    @override
    def get_file_type_enum_name(self):
        return 'UpdatableSet'
    @override
    def read_body(self, ifile):
        Nothing = []
        s = set()
        for case, e in self.iter_read_body(ifile):
            if case == self.caseDELETE:
                s.remove(e)
                continue
            ####
            if case == self.caseNEW:
                if e in s:
                    raise SaveFileException('caseNEW but exists')
            elif case == self.caseADD:
                pass
            else:
                raise logic-error
            s.add(e)
        return s
    def iter_read_body(self, ifile):
        '-> (case, element)'
        state0 = self.all_cases
        state = state0
        for line in ifile:
            if comment_line_rex.match(line):
                continue
            case = line[0]
            if case not in state:
                raise SaveFileException(f'bad format: case: {case!r}  not in {state!r}')

            element = safe_eval(line[1:])
            yield case, element
            del case, element

    def write_element(self, ofile, case, element):
        if case not in self.all_cases:
            raise ValueError(f'bad case: {case!r}')
        write = ofile.write
        write(case)
        stable_repr_print(ofile, element); write('\n')


    @override
    def write_body(self, ofile, set):
        write_element = self.write_element
        case = self.caseADD

        ls = sorted_by_SortableIterReprable(set, key=None, reverse=False, SortableIterReprable=None)
        for element in ls:
            write_element(ofile, case, element)


aSaveFile__PprintSingleObject = SaveFile__PprintSingleObject()
aSaveFile__ObjectPerLine = SaveFile__ObjectPerLine()
aSaveFile__TuplePerBlock = SaveFile__TuplePerBlock()
aSaveFile__UpdatableDict = SaveFile__UpdatableDict()
aSaveFile__UpdatableSet = SaveFile__UpdatableSet()



def __create_or_extend_or_update_SaveFile(self, path_or_iofile, obj_or_calc_f, *
    , encoding, kwargs, append:bool):
    _create_or_extend_or_update_SaveFile(
        self, path_or_iofile, obj_or_calc_f
        , encoding=encoding, kwargs=kwargs
        , append=append
        , allow_create_file=True
        , allow_write_file=True
        , allow_write_header=True
        )
def _create_or_extend_or_update_SaveFile(
    self, path_or_iofile, obj_or_calc_f, *
    , encoding, kwargs
    , append:bool
    , allow_create_file:bool
    , allow_write_file:bool
    , allow_write_header:bool
    ):
    maybe_iofile = self.open_verify_or_create_setup_savefile_header(
        path_or_iofile
        , encoding=encoding, kwargs=kwargs
        , allow_create_file=allow_create_file
        , allow_write_file=allow_write_file
        , allow_write_header=allow_write_header
        )
    def f(iofile):
        if append:
            iofile.seek(0, os.SEEK_END)
        else:
            if not is_file_EOF__by_seek(iofile):
                raise ValueError(f'savefile has not empty body')
        obj = obj_or_calc_f_to_obj(obj_or_calc_f)
        self.write_body(iofile, obj)
    if maybe_iofile is None:
        iofile = path_or_iofile
        f(iofile)
    else:
        with iofile:
            f(iofile)


def obj_or_calc_f_to_obj(obj_or_calc_f):
    if callable(obj_or_calc_f):
        calc_f = obj_or_calc_f
        obj = calc_f()
    else:
        obj = obj_or_calc_f
    return obj

def create_SaveFile__PprintSingleObject(path_or_iofile, obj_or_calc_f, *
    , encoding, kwargs):
    self = aSaveFile__PprintSingleObject
    __create_or_extend_or_update_SaveFile(
        self, path_or_iofile, obj_or_calc_f, encoding=encoding, kwargs=kwargs, append=False)
    return
    with open(path, 'xt', encoding=encoding) as ofile:
        self.write_whole(ofile, obj, encoding=encoding, kwargs=kwargs)

def create_or_extend_SaveFile__ObjectPerLine(path_or_iofile, iterable, *
    , encoding, kwargs):
    self = aSaveFile__ObjectPerLine
    __create_or_extend_or_update_SaveFile(
        self, path_or_iofile, iterable, encoding=encoding, kwargs=kwargs, append=True)
def create_or_extend_SaveFile__TuplePerBlock(path_or_iofile, iterable, *
    , encoding, kwargs):
    self = aSaveFile__TuplePerBlock
    __create_or_extend_or_update_SaveFile(
        self, path_or_iofile, iterable, encoding=encoding, kwargs=kwargs, append=True)
def create_or_update_SaveFile__UpdatableSet(path_or_iofile, iterable, *
    , encoding, kwargs):
    self = aSaveFile__UpdatableSet
    __create_or_extend_or_update_SaveFile(
        self, path_or_iofile, iterable, encoding=encoding, kwargs=kwargs, append=True)

def create_or_update_SaveFile__UpdatableDict(path_or_iofile, iterable, *
    , encoding, kwargs):
    self = aSaveFile__UpdatableDict
    __create_or_extend_or_update_SaveFile(
        self, path_or_iofile, iterable, encoding=encoding, kwargs=kwargs, append=True)





class SaveFileMethodsABC(ABC):
    @abstractmethod
    def _get_SaveFile(self):
        '-> SaveFileABC'
    @abstractmethod
    def _get_kwarg_append(self):
        '-> append:bool'

    def __init__(self, *, encoding, kwargs):
        self.encoding = encoding
        self.kwargs = kwargs
    def _create_or_extend_or_update(
        self, path_or_iofile, obj_or_calc_f, *
        , allow_create_file, allow_write_file, allow_write_header
        ):
        aSaveFile = self._get_SaveFile()
        append = self._get_kwarg_append()
        _create_or_extend_or_update_SaveFile(
            aSaveFile, path_or_iofile, obj_or_calc_f
            , encoding=encoding, kwargs=kwargs, append=append
            , allow_create_file=allow_create_file
            , allow_write_file=allow_write_file
            , allow_write_header=allow_write_header
            )



    ##################
    def _create_or_extend_or_update__easy(self, path_or_iofile, obj_or_calc_f):
        self._create_or_extend_or_update(
                path_or_iofile, obj_or_calc_f
                , allow_create_file=True
                , allow_write_file=True
                , allow_write_header=True
                )
    def read(self, path_or_iofile):
        def obj_or_calc_f():
            raise logic-error
        return self._read_or_calc_create(
                path_or_iofile, obj_or_calc_f
                ,allow_create_file=False
                ,allow_write_file=False
                ,allow_write_header=False
                )
    def read_or_calc_create(self
        , path_or_iofile, obj_or_calc_f, *
        , allow_create_file:bool
        , allow_write_file:bool
        , allow_write_header:bool
        ):
        '-> body_obj'
        return self._read_or_calc_create(
                path_or_iofile, obj_or_calc_f
                ,allow_create_file=True
                ,allow_write_file=True
                ,allow_write_header=True
                )

    def _read_or_calc_create(self
        , path_or_iofile, obj_or_calc_f, *
        , allow_create_file:bool
        , allow_write_file:bool
        , allow_write_header:bool
        ):
        '-> body_obj'
        aSaveFile = self._get_SaveFile()
        maybe_iofile = aSaveFile.open_verify_or_create_setup_savefile_header(
                    path_or_iofile
                    ,encoding=self.encoding
                    ,kwargs=self.kwargs
                    ,allow_create_file=allow_create_file
                    ,allow_write_file=allow_write_file
                    ,allow_write_header=allow_write_header
                    )
        def f(iofile):
            def read(iofile):
                obj = aSaveFile.read_body(iofile)
                return obj
            if is_file_EOF__by_seek(iofile):
                # calc and write
                obj = obj_or_calc_f_to_obj(obj_or_calc_f)
                body_begin = iofile.tell()
                aSaveFile.write_body(obj)
                #iofile.seek(body_begin)
                #obj_ = read(iofile)
                #assert obj == obj_
            else:
                # read
                obj = read(iofile)
            return obj
        if maybe_iofile is None:
            iofile = path_or_iofile
            obj = f(iofile)
        else:
            iofile = maybe_iofile
            with iofile:
                obj = f(iofile)
        return obj


class SaveFileMethods__PprintSingleObject(SaveFileMethodsABC):
    @override
    def _get_SaveFile(self):
        '-> SaveFileABC'
        return aSaveFile__PprintSingleObject
    @override
    def _get_kwarg_append(self):
        '-> append:bool'
        return False
    def create(self, path_or_iofile, obj_or_calc_f):
        return self._create_or_extend_or_update__easy(path_or_iofile, obj_or_calc_f)

class SaveFileMethods__ObjectPerLine(SaveFileMethodsABC):
    @override
    def _get_SaveFile(self):
        '-> SaveFileABC'
        return aSaveFile__ObjectPerLine
    @override
    def _get_kwarg_append(self):
        '-> append:bool'
        return True
    def create_or_extend(self, path_or_iofile, obj_or_calc_f):
        return self._create_or_extend_or_update__easy(path_or_iofile, obj_or_calc_f)
class SaveFileMethods__TuplePerBlock(SaveFileMethodsABC):
    @override
    def _get_SaveFile(self):
        '-> SaveFileABC'
        return aSaveFile__TuplePerBlock
    @override
    def _get_kwarg_append(self):
        '-> append:bool'
        return True
    def create_or_extend(self, path_or_iofile, obj_or_calc_f):
        return self._create_or_extend_or_update__easy(path_or_iofile, obj_or_calc_f)
class SaveFileMethods__UpdatableSet(SaveFileMethodsABC):
    @override
    def _get_SaveFile(self):
        '-> SaveFileABC'
        return aSaveFile__UpdatableSet
    @override
    def _get_kwarg_append(self):
        '-> append:bool'
        return True
    def create_or_update(self, path_or_iofile, obj_or_calc_f):
        return self._create_or_extend_or_update__easy(path_or_iofile, obj_or_calc_f)

class SaveFileMethods__UpdatableDict(SaveFileMethodsABC):
    @override
    def _get_SaveFile(self):
        '-> SaveFileABC'
        return aSaveFile__UpdatableDict
    @override
    def _get_kwarg_append(self):
        '-> append:bool'
        return True
    def create_or_update(self, path_or_iofile, obj_or_calc_f):
        return self._create_or_extend_or_update__easy(path_or_iofile, obj_or_calc_f)



##########################################
from collections.abc import Sequence, MutableSet, MutableMapping
'''
Sequence
    __getitem__, __len__
    append, extend, __iadd__
MutableSet
    __contains__, __iter__, __len__, add, discard
MutableMapping
    __getitem__, __setitem__, __delitem__, __iter__, __len__
'''

class SaveFileContainerABC(SaveFileMethodsABC):
    @abstractmethod
    def _init_(self):
        raise NotImplementedError
    @abstractmethod
    def _close_(self):
        raise NotImplementedError

    ######################
    def __init__(self, path_or_iofile, *
        , allow_create_file
        , allow_write_file
        , allow_write_header
        , encoding
        , kwargs
        ):
        aSaveFile = self._get_SaveFile()
        _kwargs = copy.deepcopy(kwargs)
        maybe_iofile = aSaveFile.open_verify_or_create_setup_savefile_header(
                    path_or_iofile
                    ,encoding=encoding
                    ,kwargs=kwargs
                    ,allow_create_file=allow_create_file
                    ,allow_write_file=allow_write_file
                    ,allow_write_header=allow_write_header
                    )

        _should_close = maybe_iofile is not None
        iofile = maybe_iofile if _should_close else path_or_iofile
        ###########
        self.should_close = _should_close
        self._data = aSaveFile.read_body(iofile)
        self.__encoding = encoding
        self.__kwargs = _kwargs
        self._iofile = iofile
        type(self)._init_(self)
        self.__finish_init_ = True
    def set_should_close(self, should_close):
        self.should_close = bool(should_close)
    def close(self):
        if self.__finish_init_:
            type(self)._close_(self)
        if hasattr(self, '_iofile') and self.should_close:
            self._iofile.close()
    def __del__(self):
        self.close()
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
        return None

class SaveFileSeqABC(SaveFileContainerABC, Sequence):
    @override
    def _init_(self):
        self.__length = len(self._data)
    @override
    def _close_(self):
        return
        more = self._data[self.__length:]
        if more:
            aSaveFile = self._get_SaveFile()
            aSaveFile.write_body(self._iofile, more)
    def __getitem__(self, i):
        return self._data[i]
    def __len__(self):
        return len(self._data)
    def append(self, x):
        aSaveFile = self._get_SaveFile()
        aSaveFile.write_body(self._iofile, [x])
        self._data.append(x)
    def extend(self, xs):
        for _ in map(self.append, xs):pass
    def __iadd__(self, xs):
        self.extend(xs)
        return self

class SaveFileSeq__ObjectPerLine(
    SaveFileMethods__ObjectPerLine, SaveFileSeqABC):
    pass
class SaveFileSeq__TuplePerBlock(
    SaveFileMethods__TuplePerBlock, SaveFileSeqABC):
    pass
class SaveFileSet(
    SaveFileMethods__UpdatableSet
    , SaveFileContainerABC
    , MutableSet
    ):
    @override
    def _init_(self):
        self.__data = frozenset(self._data)
    @override
    def _close_(self):
        new_set = self._data
        old_set = self.__data
        more = new_set - old_set
        less = old_set - new_set

        pairs = [
            (SaveFile__UpdatableSet.caseDELETE, less)
            ,(SaveFile__UpdatableSet.caseNEW, more)
            ]
        aSaveFile = self._get_SaveFile()
        ofile = self._iofile
        for case, elements in pairs:
            for element in elements:
                aSaveFile.write_element(ofile, case, element)

    def __contains__(self, x):
        return x in self._data
    def __iter__(self):
        return iter(self._data)
    def __len__(self):
        return len(self._data)
    def add(self, x):
        return self._data.add(x)
    def discard(self, x):
        return self._data.discard(x)

class SaveFileDict(
    SaveFileMethods__UpdatableDict
    , SaveFileContainerABC
    , MutableMapping
    ):
    @override
    def _init_(self):
        self.__data = copy.deepcopy(self._data)
    @override
    def _close_(self):
        new_dict = (self._data)
        old_dict = (self.__data)
        new_set = set(new_dict)
        old_set = set(old_dict)
        common = new_set & old_set
        more = new_set - common
        less = old_set - common
        updated = (k for k in common if new_dict[k] != old_dict[k])
        def mk_dict(it):
            return {k:new_dict.get(k) for k in it}

        more = mk_dict(more)
        less = mk_dict(less)
        updated = mk_dict(updated)

        pairs = [
            (SaveFile__UpdatableDict.caseDELETE, less)
            ,(SaveFile__UpdatableDict.caseOVERWRITE, updated)
            ,(SaveFile__UpdatableDict.caseNEW, more)
            ]
        aSaveFile = self._get_SaveFile()
        ofile = self._iofile
        for case, mapping in pairs:
            for k, v in mapping.items():
                aSaveFile.write_item(ofile, case, k, v)


    def __getitem__(self, k):
        return self._data[k]
    def __setitem__(self, k, v):
        self._data[k] = v
    def __delitem__(self, k):
        del self._data[k]
    def __iter__(self):
        return iter(self._data)
    def __len__(self):
        return len(self._data)



def _test_non_ABC(T):
    assert issubclass(T, SaveFileContainerABC)
    iofile = io.StringIO()
    mk = lambda T, iofile: T(iofile, encoding='u8'
            , allow_create_file=False
            , allow_write_file=True
            , allow_write_header=True
            , kwargs={}
            )
    mk(T, iofile)
def _test_non_ABCs():
    Ts = [SaveFileSet, SaveFileDict
        , SaveFileSeq__ObjectPerLine, SaveFileSeq__TuplePerBlock]
    for T in Ts:
        _test_non_ABC(T)
_test_non_ABCs()




####################################################
####################################################
####################################################
####################################################
####################################################


"""
def dump_information_encoding_to_bytes(information, encoding):
    'not encode(information, encoding=encoding); but encode((information, encode), encode="utf8")'
    pairs = sorted(information.items())
    s = repr((pairs, encoding))
    b = s.encode('utf8')
    return b
def make_physical_file_name(self:IInfo4Save
    , information, encoding, *, ext
    )->str:
    'f"{logic_file_name}-{short_encoded_partial_args}-{hash(information,encoding)}-{encoding}.{ext}"'

    logic_file_name = information['logic_file_name']
    short_encoded_partial_args = self.make_short_encoded_partial_args(information)

    encoding = to_std_encoding(encoding) #self.get_std_codec_name()
    bs = dump_information_encoding_to_bytes(information, encoding)
    hash_value = self.hash_method(bs)
    hash_hex = binascii.hexlify(hash_value)

    #assert '-' not in logic_file_name
    assert '-' not in short_encoded_partial_args
    assert '-' not in encoding
    assert '-' not in ext
    #f"{logic_file_name}-{short_encoded_partial_args}-{hash(information,encoding)}-{encoding}.{ext}"
    physical_file_name = f"{logic_file_name}-{short_encoded_partial_args}-{hash_hex}-{encoding}.{ext}"
    return physical_file_name


















def __on_new_file(self:IInfo4Save
    , file, information, encoding, physical_file_name
    ):
    #print = fprint(file).print
    def fprint_repr(obj):
        print(repr(obj), file=file)
    fwrite = file.write
    def fwrite_item(leading_char, k, v):
        fwrite(leading_char)
        fprint_repr(k)
        fwrite(' : ')
        fprint_repr(v)

    fwrite(Global.header)
    fprint_repr(to_std_encoding(encoding))
    fprint_repr(self.get_std_hash_method_name())
    fprint_repr(physical_file_name)

    it = iter(information.items())
    for k, v in it:
        fwrite_item('{', k, v)
        break
    else:
        #empty information
        assert not information
        fwrite('{\n')
    for k, v in it:
        fwrite_item(',', k, v)
    fwrite('}\n')




def open_saved_file(self:IInfo4Save
    , information, encoding, *, mode='r', ext=None
    ):
    if mode is None:
        mode = 'r'
    if mode not in ('r', 'w', 'x'): raise ValueError
        # avoid 'a'
    mode += 't'

    if encoding is None:
        encoding = 'u8'

    #if ext is None:
    if not ext:
        ext = 'save'

    (physical_file_name
    ) = make_physical_file_name(self, information, encoding, ext=ext)

    file = open(physical_file_name, mode, encoding=encoding)
    try:
        start_pos = file.tell()
        s = file.read(len(Global.header))
        if not s:
            if 'r' in mode:
                # read an empty file
                raise SaveFileException('not a "nn_ns text Save File": empty')
            # create a new file just now
            __on_new_file(self, file, information, encoding, physical_file_name)
            file.seek(start_pos)
            s = file.read(len(Global.header))
        if not s: raise logic-error

        if s != Global.header:
            raise SaveFileException('not a "nn_ns text Save File": not have good header')

        '''
        s = file.read(len(encoding)+1)
        if not (s[-1] == '\n' and s[:-1] == encoding):
            raise SaveFileException('incorrect encoding')

        hash_method_name = self.get_std_hash_method_name()
        s = file.read(len(hash_method_name)+1)
        if not (s[-1] == '\n' and s[:-1] == hash_method_name):
            raise SaveFileException('incorrect hash_method_name')
        '''

        encoding_EOL = file.readline()
        if encoding_EOL[-1:] != '\n':
            raise SaveFileException('unexpected EOF after encoding')
        std_encoding = to_std_encoding(encoding)
        encoding_ = encoding_EOL[:-1]
        if encoding_ != std_encoding:
            raise SaveFileException('incorrect encoding', encoding=encoding_)


        hash_method_name_EOL = file.readline()
        if hash_method_name_EOL[-1:] != '\n':
            raise SaveFileException('unexpected EOF after hash_method_name')
        hash_method_name = self.get_std_hash_method_name()
        hash_method_name_ = hash_method_name_EOL[:-1]
        if hash_method_name_ != hash_method_name:
            raise SaveFileException('incorrect hash_method_name', hash_method_name=hash_method_name_)



        physical_file_name_EOL = file.readline()
        if physical_file_name_EOL[-1:] != '\n':
            raise SaveFileException('unexpected EOF after physical_file_name')
        L = len(physical_file_name) - len(ext) # ext is not important
        if physical_file_name_EOL.startswith(physical_file_name[:L]):
            physical_file_name_ = physical_file_name_EOL[:-1]
            raise SaveFileException('incorrect physical_file_name', physical_file_name=physical_file_name_)

        #information_str = ''.join(file.readline() for _ in range(7))
        ls = []
        for line in file:
            ls.append(line)
            if line[:1] == '}':
                break
        else:
            raise SaveFileException('bad information')
        information_str = ''.join(ls); del ls

        try:
            information_ = ast.literal_eval(information_str)
        except Exception:
            raise SaveFileException('bad information')
        if information_ != information:
            raise SaveFileException('incorrect information', information=information_)

        end_of_header_ = file.readline()
        if end_of_header_ != Global.end_of_header:
            raise SaveFileException('incorrect end_of_header')
    except:
        file.close()
        raise
    return file

class IEncoderInfo4Save:
    def get_std_codec_name(self)->str:
class IHashInfo4Save:
    def get_std_hash_method_name(self)->str:
    def hash_method(self, data_bytes)->bytes:
class IProgramInfo4Save:
    def make_short_encoded_partial_args(self, information)->str:
        'e.g. program.exe -n 3 -quiet ==>> "n3qT"; determined by program'
class IInfo4Save(IProgramInfo4Save, IHashInfo4Save):
    pass


    def main(self):

"""



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doctest: +ELLIPSIS
    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #Traceback (most recent call last):

if False and __name__ == '__main__':
    classes = [
        SaveFileException
        ,Global
        ,SaveFileABC
            ,SaveFile__PprintSingleObject
            ,SaveFile__ObjectPerLine
            ,SaveFile__TuplePerBlock
            ,SaveFile__UpdatableDict
            ,SaveFile__UpdatableSet
        ]
    excludes = '''
        logic
        error
        '''.split()

    from seed.helper.ongo import main
    main(modules=[__name__], classes=classes, excludes=excludes)

