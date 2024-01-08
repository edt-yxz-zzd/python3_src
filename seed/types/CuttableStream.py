#__all__:goto
r'''[[[
e ../../python3_src/seed/types/CuttableStream.py

used for tokenization, token above token
TODO:
    userdata at _filling_begin_position/farthest_touched_end_position
    callback:
        callback when cut__position
            _cutting_end_position
        callback when iter_new_token
            _filling_begin_position
        register/unregister callback

seed.types.CuttableStream
py -m nn_ns.app.debug_cmd   seed.types.CuttableStream
py -m seed.types.CuttableStream

>>> from seed.types.CuttableStream import CuttableStream, Position, mk_CuttableStream_from_ground_level_tokens, mk_CuttableStream_from_ground_level_tokens5file, mk_userdata__pair, mk_userdata__token, iter_tokens5file
>>> from seed.types.CuttableStream import CuttableStreamError
>>> from seed.types.CuttableStream import CuttableStreamError, CuttableStreamError__invalid_Position, CuttableStreamError__addr_out_of_range, CuttableStreamError__EOF, CuttableStreamError__cut_beyond, CuttableStreamError__reenter_cutting, CuttableStreamError__reenter_filling, CuttableStreamError__seek_when_cutting, CuttableStreamError__seek_when_filling

>>> from seed.types.CuttableStream import IMkUserData4CuttableStream, MkUserData4CuttableStream5callable__mk_userdata, MkUserData4CuttableStream5callable__mk_huserdata__pair8userdata
>>> from seed.types.CuttableStream import Mkr4XUserData4CuttableStream, XUserData4CuttableStream





>>> from seed.types.CuttableStream import CuttableStream, Position, mk_CuttableStream_from_ground_level_tokens, mk_CuttableStream_from_ground_level_tokens5file, mk_userdata__pair, mk_userdata__token, iter_tokens5file

>>> p = Position(-5, None)
>>> p
Position(-5, None)
>>> p = Position(3, p)
>>> p
Position(3, Position(-5, None))
>>> p.as_int()
3
>>> p.as_ints()
(3, -5)
>>> p.as_positions()
(Position(3, Position(-5, None)), Position(-5, None))
>>> Position.mk_may_position_from_ints(iter(''))
>>> Position.mk_may_position_from_ints([-5])
Position(-5, None)
>>> Position.mk_may_position_from_ints([3, -5])
Position(3, Position(-5, None))
>>> Position.from_ints(-2, [3])
Position(-2, Position(3, None))
>>> Position.from_ints(-2, [])
Position(-2, None)
>>> Position.from_int1s([3])
Position(3, None)
>>> Position.from_int1s([])
Traceback (most recent call last):
    ...
Exception: len(offset1s)==0

>>> lhs = Position(3, None)
>>> rhs = Position(3, None)
>>> lhs == rhs
False
>>> lhs < rhs
False
>>> lhs <= rhs
True
>>> lhs >= rhs
True
>>> lhs > rhs
False
>>> len({lhs, rhs})
2









>>> stream = mk_CuttableStream_from_ground_level_tokens(mk_userdata__pair, 0, '0123456789')
>>> stream.tell()
Position(0, None)
>>> stream.peek1()
(Position(0, None), '0')


>>> from io import StringIO
>>> stream = mk_CuttableStream_from_ground_level_tokens5file(mk_userdata__token, 0, StringIO('0123456789'))
>>> stream.get_num_cached_tokens()
0
>>> stream.get_num_relax_tokens()
0
>>> stream.tell()
Position(0, None)


>>> stream.detect_eof()
False
>>> stream.get_num_cached_tokens()
1
>>> stream.get_num_relax_tokens()
1
>>> stream.tell()
Position(0, None)
>>> p1 = stream.tell__relative(1)
>>> p1 is stream.tell__absulote(1)
True
>>> p1
Position(1, None)


>>> stream.seek__relative(0)
>>> stream.tell()
Position(0, None)
>>> stream.seek__relative(1)
>>> stream.tell()
Position(1, None)
>>> stream.get_num_cached_tokens()
1
>>> stream.get_num_relax_tokens()
0
>>> stream.seek__relative(-1)
>>> stream.tell()
Position(0, None)
>>> stream.get_num_cached_tokens()
1
>>> stream.get_num_relax_tokens()
1

>>> stream.seek__absulote(0)
>>> stream.tell()
Position(0, None)
>>> stream.seek__absulote(1)
>>> stream.tell()
Position(1, None)
>>> stream.get_num_cached_tokens()
1
>>> stream.get_num_relax_tokens()
0
>>> stream.seek__absulote(0)
>>> stream.tell()
Position(0, None)
>>> stream.get_num_cached_tokens()
1
>>> stream.get_num_relax_tokens()
1


>>> stream.seek__relax__leftmost()
>>> stream.tell()
Position(0, None)
>>> stream.seek__relax__rightmost()
>>> stream.tell()
Position(1, None)
>>> stream.seek__relax__leftmost()
>>> stream.tell()
Position(0, None)

>>> p0 = stream.tell()
>>> stream.seek__position(p1)
>>> stream.tell()
Position(1, None)
>>> stream.seek__position(p0)
>>> stream.tell()
Position(0, None)


>>> stream.peek1()
'0'
>>> stream.read_le(0)
()

>>> stream.read_le(1)
('0',)
>>> stream.tell()
Position(1, None)

>>> stream.read1()
'1'
>>> stream.tell()
Position(2, None)
>>> stream.get_num_cached_tokens()
2
>>> stream.get_num_relax_tokens()
0



>>> stream.peek_le(2)
('2', '3')
>>> stream.tell()
Position(2, None)
>>> stream.get_num_cached_tokens()
4
>>> stream.get_num_relax_tokens()
2

>>> stream.peek_le__relax(1)
('2',)
>>> stream.peek_le__relax(2)
('2', '3')
>>> stream.peek_le__relax(3)
('2', '3')
>>> stream.tell()
Position(2, None)
>>> stream.get_num_cached_tokens()
4
>>> stream.get_num_relax_tokens()
2


>>> stream.read_le__relax(3)
('2', '3')
>>> stream.tell()
Position(4, None)
>>> stream.get_num_cached_tokens()
4
>>> stream.get_num_relax_tokens()
0
>>> stream.peek_le__relax(3)
()
>>> stream.read_le__relax(3)
()


>>> stream.cut__position(p0)
>>> stream.get_num_cached_tokens()
4
>>> stream.get_num_relax_tokens()
0
>>> stream.cut__position(p1)
>>> stream.get_num_cached_tokens()
3
>>> stream.get_num_relax_tokens()
0
>>> stream.seek__position(p1)
>>> stream.cut__position(p1)
>>> stream.tell()
Position(1, None)
>>> stream.cut__position(p0) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
CuttableStreamError__cut_beyond
>>> stream.tell()
Position(1, None)
>>> stream.seek__relative(3)
>>> stream.cut__relative(-3)
>>> stream.tell()
Position(4, None)
>>> stream.get_num_cached_tokens()
3
>>> stream.get_num_relax_tokens()
0

>>> stream.cut__relative(-2)
>>> stream.tell()
Position(4, None)
>>> stream.get_num_cached_tokens()
2
>>> stream.get_num_relax_tokens()
0


>>> stream.cut__relative(-1)
>>> stream.tell()
Position(4, None)
>>> stream.get_num_cached_tokens()
1
>>> stream.get_num_relax_tokens()
0


>>> stream.cut__relative(0)
>>> stream.tell()
Position(4, None)
>>> stream.get_num_cached_tokens()
0
>>> stream.get_num_relax_tokens()
0


>>> stream.read_le(9)
('4', '5', '6', '7', '8', '9')
>>> stream.tell()
Position(10, None)
>>> stream.get_num_cached_tokens()
6
>>> stream.get_num_relax_tokens()
0
>>> stream.detect_eof()
True



>>> stream.seek__relative(-2)
>>> stream.tell()
Position(8, None)
>>> stream.get_num_cached_tokens()
6
>>> stream.get_num_relax_tokens()
2
>>> stream.detect_eof()
False


>>> stream.cut__absulote(4)
>>> stream.tell()
Position(8, None)
>>> stream.get_num_cached_tokens()
6
>>> stream.get_num_relax_tokens()
2
>>> stream.cut__absulote(5)
>>> stream.tell()
Position(8, None)
>>> stream.get_num_cached_tokens()
5
>>> stream.get_num_relax_tokens()
2
>>> stream.cut__absulote(7)
>>> stream.tell()
Position(8, None)
>>> stream.get_num_cached_tokens()
3
>>> stream.get_num_relax_tokens()
2

>>> stream.seek__absulote(7)
>>> stream.tell()
Position(7, None)
>>> stream.seek__absulote(6) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
CuttableStreamError__addr_out_of_range
>>> stream.tell()
Position(7, None)
>>> stream.seek__absulote(11) #doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
    ...
CuttableStreamError__addr_out_of_range
>>> stream.tell()
Position(7, None)
>>> stream.seek__absulote(10)
>>> stream.tell()
Position(10, None)
>>> stream.detect_eof()
True



>>> p3_ = lambda s:(s.tell_cutting_end_position(), s.tell(), s.tell_filling_begin_position())


news:
    detect_required_cutting
    detect_required_filling
    tell_cutting_end_position
    tell_filling_begin_position
    register_callback4before_cutting
    register_callback4after_filling
    unregister_callback4before_cutting
    unregister_callback4after_filling
    get_huserdata8filling_begin_position
    peek1__xuserdata__relax

    IMkUserData4CuttableStream
    MkUserData4CuttableStream5callable__mk_userdata
    MkUserData4CuttableStream5callable__mk_huserdata__pair8userdata
    Mkr4XUserData4CuttableStream
        XUserData4CuttableStream

    CuttableStreamError__reenter_cutting
    CuttableStreamError__reenter_filling
    CuttableStreamError__seek_when_cutting
    CuttableStreamError__seek_when_filling


>>> mk_userdata = MkUserData4CuttableStream5callable__mk_huserdata__pair8userdata(lambda p:p)
>>> stream = mk_CuttableStream_from_ground_level_tokens(mk_userdata, -3, range(6, 16))
>>> stream.get_huserdata8filling_begin_position()
Position(-3, None)
>>> stream.peek1__xuserdata__relax()
Position(-3, None)
>>> stream.detect_required_cutting()
False
>>> stream.detect_required_filling()
True

>>> stream.peek1()
(Position(-3, None), 6)
>>> stream.detect_required_cutting()
False
>>> stream.detect_required_filling()
False
>>> stream.get_huserdata8filling_begin_position()
Position(-2, None)
>>> stream.peek1__xuserdata__relax()
(Position(-3, None), 6)

>>> stream.read_le(3)
((Position(-3, None), 6), (Position(-2, None), 7), (Position(-1, None), 8))
>>> stream.detect_required_cutting()
True
>>> stream.detect_required_filling()
True
>>> stream.peek1()
(Position(0, None), 9)
>>> stream.detect_required_cutting()
True
>>> stream.detect_required_filling()
False
>>> stream.tell_cutting_end_position()
Position(-3, None)
>>> stream.tell_filling_begin_position()
Position(1, None)
>>> stream.tell()
Position(0, None)


>>> f4c = lambda stream, position:print(9999, position)
>>> f4f = lambda stream, old_position, token, userdata, new_position, huserdata:print(77, token, userdata, new_position, huserdata)
>>> stream.register_callback4before_cutting(f4c)
>>> stream.register_callback4after_filling(f4f)
>>> stream.cut__relative(-3)
>>> stream.cut__relative(-2)
9999 Position(-2, None)
>>> stream.peek1()
(Position(0, None), 9)
>>> stream.read_le(3)
77 10 (Position(1, None), 10) Position(2, None) Position(2, None)
77 11 (Position(2, None), 11) Position(3, None) Position(3, None)
((Position(0, None), 9), (Position(1, None), 10), (Position(2, None), 11))
>>> stream.peek1()
77 12 (Position(3, None), 12) Position(4, None) Position(4, None)
(Position(3, None), 12)
>>> stream.unregister_callback4before_cutting(f4c)
>>> stream.unregister_callback4after_filling(f4f)
>>> stream.cut__relative(-1)
>>> stream.read_le(2)
((Position(3, None), 12), (Position(4, None), 13))





#XUserData4CuttableStream
>>> mk_userdata = Mkr4XUserData4CuttableStream(dict)
>>> stream = mk_CuttableStream_from_ground_level_tokens(mk_userdata, -3, range(6, 16))
>>> stream.get_huserdata8filling_begin_position()
XUserData4CuttableStream(Position(-3, None), {})
>>> stream.peek1__xuserdata__relax()
XUserData4CuttableStream(Position(-3, None), {})

>>> stream.peek1()
XUserData4CuttableStream(Position(-3, None), {}, 6)
>>> stream.get_huserdata8filling_begin_position()
XUserData4CuttableStream(Position(-2, None), {})
>>> stream.peek1__xuserdata__relax()
XUserData4CuttableStream(Position(-3, None), {}, 6)


CuttableStreamError__reenter_cutting
CuttableStreamError__reenter_filling
CuttableStreamError__seek_when_cutting
CuttableStreamError__seek_when_filling
>>> stream.seek__relative(1)
>>> stream.detect_required_cutting()
True
>>> stream.detect_required_filling()
True
>>> stream.tell()
Position(-2, None)
>>> f4c = lambda stream, position:stream.cut__relative(0)
>>> f4f = lambda stream, old_position, token, userdata, new_position, huserdata:stream.read1()
>>> stream.register_callback4before_cutting(f4c)
>>> stream.register_callback4after_filling(f4f)
>>> stream.cut__relative(0)
Traceback (most recent call last):
    ...
seed.types.CuttableStream.CuttableStreamError__reenter_cutting
>>> stream.read1()
Traceback (most recent call last):
    ...
seed.types.CuttableStream.CuttableStreamError__seek_when_filling
>>> stream.unregister_callback4after_filling(f4f)
>>> f4f = lambda stream, old_position, token, userdata, new_position, huserdata:stream.peek1()
>>> stream.register_callback4after_filling(f4f)
>>> stream.read1()
XUserData4CuttableStream(Position(-1, None), {}, 8)
>>> stream.unregister_callback4after_filling(f4f)
>>> f4f = lambda stream, old_position, token, userdata, new_position, huserdata:stream.peek_le(2)
>>> stream.register_callback4after_filling(f4f)
>>> stream.read1()
Traceback (most recent call last):
    ...
seed.types.CuttableStream.CuttableStreamError__reenter_filling
>>> p3_(stream)
(Position(-3, None), Position(1, None), Position(1, None))
>>> stream.unregister_callback4before_cutting(f4c)
>>> f4c = lambda stream, position:stream.seek__relative(-1)
>>> stream.register_callback4before_cutting(f4c)
>>> stream.cut__relative(-3)
Traceback (most recent call last):
    ...
seed.types.CuttableStream.CuttableStreamError__seek_when_cutting





fill when cutting
>>> mk_userdata = Mkr4XUserData4CuttableStream(dict)
>>> stream = mk_CuttableStream_from_ground_level_tokens(mk_userdata, -3, range(6, 16))
>>> f4c = lambda stream, position:stream.peek_le(2)
>>> stream.register_callback4before_cutting(f4c)

>>> stream.detect_required_cutting()
False
>>> stream.detect_required_filling()
True
>>> p3_(stream)
(Position(-3, None), Position(-3, None), Position(-3, None))
>>> stream.cut__relative(0)#stream.seek__relative(2)
>>> p3_(stream)
(Position(-3, None), Position(-3, None), Position(-3, None))
>>> stream.read1()
XUserData4CuttableStream(Position(-3, None), {}, 6)
>>> stream.detect_required_cutting()
True
>>> stream.detect_required_filling()
True
>>> p3_(stream)
(Position(-3, None), Position(-2, None), Position(-2, None))

>>> stream.cut__relative(0);stream.seek__relative(2)
>>> stream.detect_required_cutting()
True
>>> stream.detect_required_filling()
True
>>> p3_(stream)
(Position(-2, None), Position(0, None), Position(0, None))

>>> stream.peek1()
XUserData4CuttableStream(Position(0, None), {}, 9)
>>> stream.detect_required_cutting()
True
>>> stream.detect_required_filling()
False
>>> p3_(stream)
(Position(-2, None), Position(0, None), Position(1, None))

>>> stream.cut__relative(0);stream.seek__relative(2)
>>> stream.detect_required_cutting()
True
>>> stream.detect_required_filling()
True
>>> p3_(stream)
(Position(0, None), Position(2, None), Position(2, None))





XUserData4CuttableStream<Namespace>
get_mk_userdata
>>> from seed.types.Namespace import Namespace, NamespaceSetOnce, NamespaceForbidOverwriteImplicitly, NamespaceForbidNewKey
>>> mk_userdata = Mkr4XUserData4CuttableStream(NamespaceSetOnce)
>>> mk_userdata == Mkr4XUserData4CuttableStream(NamespaceSetOnce)
True
>>> mk_userdata is not Mkr4XUserData4CuttableStream(NamespaceSetOnce)
True
>>> stream = mk_CuttableStream_from_ground_level_tokens(mk_userdata, -3, range(6, 16))
>>> mk_userdata is stream.get_mk_userdata() == Mkr4XUserData4CuttableStream(NamespaceSetOnce)
True
>>> stream.get_huserdata8filling_begin_position()
XUserData4CuttableStream(Position(-3, None), NamespaceSetOnce())



news:
    get_xuserdata__absulote
    get_xuserdata__relative
    get_xuserdata__position

>>> stream.get_xuserdata__relative(0)
XUserData4CuttableStream(Position(-3, None), NamespaceSetOnce())
>>> stream.read1()
XUserData4CuttableStream(Position(-3, None), NamespaceSetOnce(), 6)
>>> stream.tell()
Position(-2, None)
>>> stream.get_xuserdata__relative(0)
XUserData4CuttableStream(Position(-2, None), NamespaceSetOnce())
>>> stream.tell()
Position(-2, None)
>>> stream.get_xuserdata__relative(-1)
XUserData4CuttableStream(Position(-3, None), NamespaceSetOnce(), 6)
>>> stream.tell()
Position(-2, None)
>>> stream.get_xuserdata__absulote(-2)
XUserData4CuttableStream(Position(-2, None), NamespaceSetOnce())
>>> stream.tell()
Position(-2, None)
>>> stream.get_xuserdata__absulote(-3)
XUserData4CuttableStream(Position(-3, None), NamespaceSetOnce(), 6)
>>> stream.tell()
Position(-2, None)


#]]]'''


__all__ = r'''
CuttableStream
    Position
    mk_CuttableStream_from_ground_level_tokens
    mk_CuttableStream_from_ground_level_tokens5file
    mk_userdata__pair
    mk_userdata__token
    iter_tokens5file

IMkUserData4CuttableStream
    MkUserData4CuttableStream5callable__mk_userdata
    MkUserData4CuttableStream5callable__mk_huserdata__pair8userdata
    Mkr4XUserData4CuttableStream
        XUserData4CuttableStream

CuttableStreamError
    CuttableStreamError__invalid_Position
    CuttableStreamError__addr_out_of_range
    CuttableStreamError__EOF
    CuttableStreamError__cut_beyond
    CuttableStreamError__reenter_cutting
    CuttableStreamError__reenter_filling
    CuttableStreamError__seek_when_cutting
    CuttableStreamError__seek_when_filling
'''.split()#'''
__all__
from seed.tiny import check_type_is, check_type_in
from seed.tiny import check_callable
from seed.helper.repr_input import repr_helper
from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots

class _Data:
    __slots__ = r'''
        _position
        _userdata
    '''.split()#'''
    def __init__(sf, position, userdata, /):
        check_type_is(Position, position)
        sf._position = position
        sf._userdata = userdata
    @property
    def position(sf, /):
        return sf._position
    @property
    def userdata(sf, /):
        return sf._userdata

class Position:
    'high order Position'
    __slots__ = r'''
        _offset
        _may_position4low_level
    '''.split()#'''
    def __init__(sf, offset, may_position4low_level, /):
        check_type_is(int, offset)
        check_type_in(MayPositionTypes, may_position4low_level)
        sf._offset = offset
        sf._may_position4low_level = may_position4low_level
    def __repr__(sf, /):
        return repr_helper(sf, sf._offset, sf._may_position4low_level)

    ######
    def as_int(sf, /):
        return sf._offset

    def iter_positions(sf, /):
        yield sf
        if sf._may_position4low_level is not None:
            yield from sf._may_position4low_level.iter_positions()

    ######
    def as_ints(sf, /):
        return (*map(__class__.as_int, sf.iter_positions()),)
    def as_positions(sf, /):
        return (*sf.iter_positions(),)

    ######
    @classmethod
    def mk_may_position_from_ints(cls, offsets, /):
        may_position = None
        if not hasattr(offsets, '__reversed__'):
            offsets = [*offsets]
        for offset in reversed(offsets):
            may_position = Position(offset, may_position)
        return may_position
    @classmethod
    def from_int1s(cls, offset1s, /):
        may_position = cls.mk_may_position_from_ints(offset1s)
        if may_position is None: raise Exception('len(offset1s)==0')
        position = may_position
        return position
    @classmethod
    def from_ints(cls, offset, offsets, /):
        may_position = cls.mk_may_position_from_ints(offsets)
        position = Position(offset, may_position)
        return position

    def __hash__(sf, /):
        return id(sf)
    def __eq__(sf, ot, /):
        return sf is ot

    #
    @classmethod
    def _lt_(cls, lhs, rhs, /):
        if not type(lhs) is cls is type(rhs):
            return NotImplemented
        return lhs.as_int() < rhs.as_int()
    #似乎有毛病:等价关系『not <>』 不是『__eq__』
    def __lt__(sf, ot, /):
        return sf._lt_(sf, ot)
    def __gt__(sf, ot, /):
        return sf._lt_(ot, sf)
    def __le__(sf, ot, /):
        return not sf._lt_(ot, sf)
    def __ge__(sf, ot, /):
        return not sf._lt_(sf, ot)


MayPositionTypes = (Position, type(None))
class CuttableStreamError(Exception):pass
class CuttableStreamError__invalid_Position(CuttableStreamError):pass
class CuttableStreamError__addr_out_of_range(CuttableStreamError):pass
class CuttableStreamError__EOF(CuttableStreamError):pass
class CuttableStreamError__cut_beyond(CuttableStreamError):pass

class CuttableStreamError__reenter_cutting(CuttableStreamError):pass
    #since callback4before_cutting
class CuttableStreamError__reenter_filling(CuttableStreamError):pass
    #since callback4after_filling
class CuttableStreamError__seek_when_cutting(CuttableStreamError):pass
    #since callback4before_cutting
class CuttableStreamError__seek_when_filling(CuttableStreamError):pass
    #since callback4after_filling
ValueError

def mk_userdata__token(position, token, /):
    '-> userdata-token-version'
    return token
def mk_userdata__pair(position, token, /):
    '-> userdata-pair-version'
    return (position, token)
def iter_tokens5file(ifile, /):
    while 1:
        tokens = ifile.read(1)
        if not tokens:
            [] = tokens
            break
        [token] = tokens
        yield token

def mk_CuttableStream_from_ground_level_tokens(mk_userdata, offset, tokens, /):
    return CuttableStream.from_ground_level_tokens(mk_userdata, offset, tokens)
def mk_CuttableStream_from_ground_level_tokens5file(mk_userdata, offset, ifile, /):
    return CuttableStream.from_ground_level_tokens5file(mk_userdata, offset, ifile)

class IMkUserData4CuttableStream(ABC):
    __slots__ = ()
    @abstractmethod
    def mk_huserdata__without_token(sf, position, /):
        'position -> huserdata/half_userdata'
    @abstractmethod
    def mk_userdata5half(sf, position, huserdata, token, /):
        'position -> huserdata -> token -> userdata'

    def mk_userdata__with_token(sf, position, token, /):
        'position -> token -> userdata'
        huserdata = sf.mk_huserdata__without_token(position)
        userdata = sf.mk_userdata5half(position, huserdata, token)
        return userdata
def _eq__f(sf, ot, /):
    return type(sf) is type(ot) and sf._f == ot._f
class MkUserData4CuttableStream5callable__mk_userdata(IMkUserData4CuttableStream):
    r'''
    huserdata=None
    mk_userdata(position, token) -> userdata
    '''#'''
    __slots__ = '_f'
    __eq__ = _eq__f
    def __init__(sf, mk_userdata, /):
        check_callable(mk_userdata)
        sf._f = mk_userdata
    @override
    def mk_huserdata__without_token(sf, position, /):
        'position -> huserdata/half_userdata'
        return None
    @override
    def mk_userdata5half(sf, position, huserdata, token, /):
        'position -> huserdata -> token -> userdata'
        assert huserdata is None
        return sf._f(position, token)


class MkUserData4CuttableStream5callable__mk_huserdata__pair8userdata(IMkUserData4CuttableStream):
    r'''
    mk_huserdata(position) -> huserdata
    userdata = (huserdata, token)
    '''#'''
    __slots__ = '_f'
    __eq__ = _eq__f
    def __init__(sf, mk_huserdata, /):
        check_callable(mk_huserdata)
        sf._f = mk_huserdata
    @override
    def mk_huserdata__without_token(sf, position, /):
        'position -> huserdata/half_userdata'
        return sf._f(position)
    @override
    def mk_userdata5half(sf, position, huserdata, token, /):
        'position -> huserdata -> token -> userdata'
        return (huserdata, token)

class XUserData4CuttableStream:
    def __repr__(sf, /):
        return repr_helper(sf, sf.position, sf.payload, *sf.tmay_token)

    def __init__(sf, position, payload, /, *tmay_token):
        if not len(tmay_token) < 2: raise TypeError
        check_type_is(Position, position)
        sf._position = position
        sf._tmay_token = tmay_token
        sf._payload = payload

    @property
    def position(sf, /):
        return sf._position
    @property
    def tmay_token(sf, /):
        return sf._tmay_token
    @property
    def payload(sf, /):
        return sf._payload
    @property
    def token(sf, /):
        if not sf._tmay_token: raise AttributeError('token not fixed')
        return sf._tmay_token[0]
    def fix_token(sf, token, /):
        if sf._tmay_token: raise AttributeError('token fixed')
        sf._tmay_token = (token,)
    token = token.setter(fix_token)
    assert token.fset is fix_token
class Mkr4XUserData4CuttableStream(IMkUserData4CuttableStream):
    r'''
    userdata = huserdata :: XUserData4CuttableStream<payload>
    mk_payload :: () -> payload
    '''#'''
    __slots__ = '_f'
    __eq__ = _eq__f
    def __init__(sf, mk_payload, /):
        check_callable(mk_payload)
        sf._f = mk_payload
    @override
    def mk_huserdata__without_token(sf, position, /):
        'position -> huserdata/half_userdata'
        payload = sf._f()
        xuserdata = XUserData4CuttableStream(position, payload)
        huserdata = xuserdata
        return huserdata
    @override
    def mk_userdata5half(sf, position, huserdata, token, /):
        'position -> huserdata -> token -> userdata'
        xuserdata = huserdata
        check_type_is(XUserData4CuttableStream, xuserdata)
        assert xuserdata.position is position
        xuserdata.token = token
        xuserdata.token
        userdata = xuserdata
        return userdata


class CuttableStream:
    r'''
    mk_userdata :: IMkUserData4CuttableStream
    or: mk_userdata(position, token) -> userdata
        e.g. mk_userdata__token -> token
        e.g. mk_userdata__pair -> (position, token)

    'callback4before_cutting :: (cuttable_stream, position) -> None'

    'callback4after_filling :: (cuttable_stream, old_position, token, userdata, new_position, huserdata) -> None'

    [_cutting_end_position <= _curr_position <= _filling_begin_position]

    [xuserdata =[def]= userdata | huserdata]

    [position -> [_cutting_end_position <= position <= _filling_begin_position] -> xuserdata]
        * [position -> [_cutting_end_position <= position < _filling_begin_position] -> userdata]
        * [position -> [position is _filling_begin_position] -> huserdata]

    '''#'''

    @classmethod
    def from_ground_level_tokens5file(cls, mk_userdata, offset, ifile, /):
        return cls.from_ground_level_tokens(mk_userdata, offset, iter_tokens5file(ifile))
    @classmethod
    def from_ground_level_tokens(cls, mk_userdata, offset, tokens, /):
        may_begin_position4low_level = None
        iter_token_may_end_position4low_level_pairs = ((token, None) for token in tokens)
        sf = cls(mk_userdata, offset, may_begin_position4low_level, iter_token_may_end_position4low_level_pairs)
        return sf

    def get_mk_userdata(sf, /):
        '-> IMkUserData4CuttableStream'
        return sf._mk_userdata
    def __init__(sf, mk_userdata, offset, may_begin_position4low_level, iter_token_may_end_position4low_level_pairs, /):
        if not isinstance(mk_userdata, IMkUserData4CuttableStream):
            check_callable(mk_userdata)
            mk_userdata = MkUserData4CuttableStream5callable__mk_userdata(mk_userdata)
        assert isinstance(mk_userdata, IMkUserData4CuttableStream)

        offset_position = Position(offset, may_begin_position4low_level)
        sf._ps = iter(iter_token_may_end_position4low_level_pairs)
            #(token, may_end_position4low_level)
        sf._fs = sf.__iter_fills()
        sf._filling_stop = False
        sf._cutting_ls = []
        sf._filling_ls = []
        sf._cutting_end_position = offset_position
        sf._filling_begin_position = offset_position
        sf._curr_position = offset_position
        sf._ok4cut = True
        sf._ok4fill = True
        sf._callbacks4before_cutting = []
        sf._callbacks4after_filling = []
        sf._mk_userdata = mk_userdata
        sf._huserdata = mk_userdata.mk_huserdata__without_token(sf._filling_begin_position)
        sf._saved_offset = offset
        sf._saved_may_begin_position4low_level = may_begin_position4low_level
    def get_num_cached_tokens(sf, /):
        return sf._filling_begin_position.as_int() -sf._cutting_end_position.as_int()
    def get_num_relax_tokens(sf, /):
        return sf._filling_begin_position.as_int() -sf._curr_position.as_int()
    def detect_eof(sf, /):
        return len(sf.peek_le(1)) == 0
    #__bool__ = detect_eof
    def detect_required_filling(sf, /):
        return sf._curr_position is sf._filling_begin_position
    def detect_required_cutting(sf, /):
        return sf._curr_position is not sf._cutting_end_position

    def tell_cutting_end_position(sf, /):
        return sf._cutting_end_position
    def tell_filling_begin_position(sf, /):
        return sf._filling_begin_position
    def tell(sf, /):
        return sf._curr_position
    def tell__relative(sf, offset, /):
        check_type_is(int, offset)
        addr = sf._curr_position.as_int() + offset
        return sf.tell__absulote(addr)
    def tell__absulote(sf, addr, /):
        check_type_is(int, addr)
        if addr == sf._filling_begin_position.as_int():
            position = sf._filling_begin_position
        else:
            k, data = sf._get_k_data5addr(addr)
            position = data.position
        return position
    def seek__relative(sf, offset, /):
        sf._curr_position = sf._position5relative_addr(offset)
    def seek__absulote(sf, addr, /):
        sf._curr_position = sf._position5absulote_addr(addr)
    def _position5relative_addr(sf, offset, /):
        check_type_is(int, offset)
        addr = sf._curr_position.as_int() + offset
        return sf._position5absulote_addr(addr)
    def _position5absulote_addr(sf, addr, /):
        check_type_is(int, addr)
        iL = sf._filling_begin_position.as_int()
        if addr == iL:
            return sf._filling_begin_position
        else:
            k, data = sf._get_k_data5addr(addr)
            return data.position
    def seek__relax__rightmost(sf, /):
        #furthest
        sf._curr_position = sf._filling_begin_position
    def seek__relax__leftmost(sf, /):
        sf._curr_position = sf._cutting_end_position
    def seek__position(sf, position, /):
        if position is sf._curr_position:
            return
        check_type_is(Position, position)
        addr = position.as_int()
        if not position is sf._position5absulote_addr(addr): raise CuttableStreamError__invalid_Position
        sf._curr_position = position

    def _calc_k5addr(sf, addr, /):
        check_type_is(int, addr)
        i_N = sf._cutting_end_position.as_int()
        iL = sf._filling_begin_position.as_int()
        if not i_N <= addr < iL: raise CuttableStreamError__addr_out_of_range
        L = len(sf._filling_ls)
        i0 = iL - L
        k = addr - i0
        return k
    def _get_k_data5addr(sf, addr, /):
        k = sf._calc_k5addr(addr)
        data = sf.__get_data5k(k)
        if not data.position.as_int() == addr: raise logic-err
        return k, data
    def __get_data5k(sf, k, /):
        if k >= 0:
            data = sf._filling_ls[k]
        else:
            data = sf._cutting_ls[k]
        return data



    def _unregister(sf, ls, f, /):
        i = ls.index(f)
        del ls[i]
    def _register(sf, ls, f, /):
        check_callable(f)
        ls.append(f)
    def unregister_callback4before_cutting(sf, callback4before_cutting, /):
        sf._unregister(sf._callbacks4before_cutting, callback4before_cutting)
    def unregister_callback4after_filling(sf, callback4after_filling, /):
        sf._unregister(sf._callbacks4after_filling, callback4after_filling)

    def register_callback4before_cutting(sf, callback4before_cutting, /):
        'callback4before_cutting :: (cuttable_stream, position) -> None'
        sf._register(sf._callbacks4before_cutting, callback4before_cutting)
    def register_callback4after_filling(sf, callback4after_filling, /):
        'callback4after_filling :: (cuttable_stream, old_position, token, userdata, new_position, huserdata) -> None'
        sf._register(sf._callbacks4after_filling, callback4after_filling)


    def _before_cutting_(sf, position, /):
        #cut__position
        assert sf._cutting_end_position.as_int() < position.as_int() <= sf._curr_position.as_int()

        if not sf._ok4cut: raise CuttableStreamError__reenter_cutting
        sf._ok4cut = False
        try:
            sf._before_cutting_impl(position)
        finally:
            sf._ok4cut = True
    def _before_cutting_impl(sf, position, /):
        ls = sf._callbacks4before_cutting
        save = sf._curr_position
        for f in ls:
            f(sf, position)
            if not save is sf._curr_position: raise CuttableStreamError__seek_when_cutting
    def _after_filling_(sf, old_position, token, userdata, new_position, huserdata, /):
        #def _after_filling_(sf, position, /):
        #__iter_fills
        #_fill1
        ls = sf._callbacks4after_filling
        save = sf._curr_position
        for f in ls:
            f(sf, old_position, token, userdata, new_position, huserdata)
            if not save is sf._curr_position: raise CuttableStreamError__seek_when_filling
    def __iter_fills(sf, /):
        for (token, may_end_position4low_level) in sf._ps:
            position = sf._filling_begin_position
            sf._filling_begin_position = Position(position.as_int()+1, may_end_position4low_level)
            huserdata = sf._huserdata
            #userdata = sf._mk_userdata(position, token)
            userdata = sf._mk_userdata.mk_userdata5half(position, huserdata, token)
            del huserdata
            data = _Data(position, userdata)
            sf._filling_ls.append(data)
            sf._huserdata = sf._mk_userdata.mk_huserdata__without_token(sf._filling_begin_position)
            yield data, (position, token, userdata, sf._filling_begin_position, sf._huserdata)
        sf._filling_stop = True

    def _fill1_impl(sf, /):
        for data, (old_position, token, userdata, new_position, huserdata) in sf._fs:
            sf._after_filling_(old_position, token, userdata, new_position, huserdata)
            break
        else:
            raise CuttableStreamError__EOF
    def _fill1(sf, /):
        if not sf._ok4fill: raise CuttableStreamError__reenter_filling
        sf._ok4fill = False
        try:
            sf._fill1_impl()
        finally:
            sf._ok4fill = True

    def get_xuserdata__absulote(sf, addr, /):
        position = sf.tell__absulote(addr)
        return sf.get_xuserdata__position(position)
    def get_xuserdata__relative(sf, offset, /):
        position = sf.tell__relative(offset)
        return sf.get_xuserdata__position(position)
    def get_xuserdata__position(sf, position, /):
        save = sf.tell()
        try:
            sf.seek__position(position)
            return sf.peek1__xuserdata__relax()
        finally:
            sf.seek__position(save)
    def get_huserdata8filling_begin_position(sf, /):
        return sf._huserdata
    def peek1__xuserdata__relax(sf, /):
        'xuserdata = userdata | huserdata'
        if sf._curr_position is sf._filling_begin_position:
            return sf.get_huserdata8filling_begin_position()
        return sf.peek1()

    def peek1(sf, /):
        if sf._curr_position is sf._filling_begin_position:
            sf._fill1()
        assert not sf._curr_position is sf._filling_begin_position
        addr = sf._curr_position.as_int()
        k, data = sf._get_k_data5addr(addr)
        return data.userdata
    def read1(sf, /):
        userdata = sf.peek1()
        sf.seek__relative(1)
        return userdata


    def read_le(sf, sz, /):
        #if sz < 1: return ()
        ls = []
        try:
            for _ in range(sz):
                ls.append(sf.read1())
        except CuttableStreamError__EOF:
            pass
        return (*ls,)
    def peek_le(sf, sz, /):
        position = sf.tell()
        ls = sf.read_le(sz)
        del sz
        #sf.seek__relative(-len(ls))
        sf.seek__position(position)
        return ls
    def peek_le__relax(sf, sz, /):
        check_type_is(int, sz)
        sz = min(sz, sf.get_num_relax_tokens())
        if sz < 1:
            return ()
        i = sf._curr_position.as_int()
        k = sf._calc_k5addr(i)
        ls = (*map(_Data.userdata.fget, map(sf.__get_data5k, range(k, k+sz))),)
        assert len(ls) == sz
        return ls
    def read_le__relax(sf, sz, /):
        ls = sf.peek_le__relax(sz)
        sf.seek__relative(len(ls))
        return ls


    def cut__relative(sf, offset, /):
        position = sf.tell__relative(offset)
        sf.cut__position(position)
    def cut__absulote(sf, addr, /):
        position = sf.tell__absulote(addr)
        sf.cut__position(position)
    def cut__position(sf, position, /):
        check_type_is(Position, position)
        def main():
            if position is sf._cutting_end_position:
                return
            if not position.as_int() <= sf._curr_position.as_int(): raise CuttableStreamError__cut_beyond
            if not position.as_int() >= sf._cutting_end_position.as_int(): raise CuttableStreamError__cut_beyond
            if position is sf._filling_begin_position:
                assert not sf._cutting_end_position is sf._filling_begin_position
                assert sf._curr_position is sf._filling_begin_position

                #save = sf._filling_begin_position
                sf._before_cutting_(position)
                #if not save is sf._filling_begin_position:
                if not position is sf._filling_begin_position:
                    f(True)
                    return
                sf._cutting_end_position = sf._filling_begin_position
                sf._cutting_ls.clear()
                sf._filling_ls.clear()
            else:
                f(False)
            return
        #end-def main():
        def f(callback_done, /):
            addr = position.as_int()
            k, data = sf._get_k_data5addr(addr)
            if not data.position is position: raise CuttableStreamError__invalid_Position

            assert sf._cutting_end_position.as_int() < position.as_int() <= sf._curr_position.as_int()
            assert position.as_int() < sf._filling_begin_position.as_int()
            if not callback_done:
                sf._before_cutting_(position)

            sf._cutting_end_position = position

            if k > 0:
                #swap, clear
                L = len(sf._filling_ls)
                assert 0 < k < L
                k -= L
                assert -L < k < 0
                sf._cutting_ls = sf._filling_ls
                sf._filling_ls = []

            else:
                pass
            if k == 0:
                sf._cutting_ls.clear()
            else:
                assert k < 0
                N = len(sf._cutting_ls)
                ls = sf._cutting_ls
                for i in reversed(range(-N, k)):
                    if ls[i] is None:
                        break
                    ls[i] = None
                num_nulls = k+N
                assert 0 < num_nulls < N
                assert ls[num_nulls-1] is None
                assert not ls[num_nulls] is None
                if not 2*num_nulls < N:
                    del ls[:num_nulls]
        #end-def f(callback_done, /):
        main()
    #end-def cut__position(sf, position, /):


#end-class CuttableStream:


from seed.types.CuttableStream import CuttableStream, Position, mk_CuttableStream_from_ground_level_tokens, mk_CuttableStream_from_ground_level_tokens5file, mk_userdata__pair, mk_userdata__token, iter_tokens5file
from seed.types.CuttableStream import CuttableStreamError
from seed.types.CuttableStream import CuttableStreamError, CuttableStreamError__invalid_Position, CuttableStreamError__addr_out_of_range, CuttableStreamError__EOF, CuttableStreamError__cut_beyond, CuttableStreamError__reenter_cutting, CuttableStreamError__reenter_filling, CuttableStreamError__seek_when_cutting, CuttableStreamError__seek_when_filling

from seed.types.CuttableStream import IMkUserData4CuttableStream, MkUserData4CuttableStream5callable__mk_userdata, MkUserData4CuttableStream5callable__mk_huserdata__pair8userdata
from seed.types.CuttableStream import Mkr4XUserData4CuttableStream, XUserData4CuttableStream




from seed.types.CuttableStream import *

if __name__ == "__main__":
    import doctest
    doctest.testmod()

def _t():
    XXX = CuttableStream

    from seed.helper.print_methods import wrapped_print_methods
    wrapped_print_methods(XXX)
if __name__ == '__main__':
    #_t()
    pass


