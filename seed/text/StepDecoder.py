
r'''
seed.text.StepDecoder
py -m seed.text.StepDecoder
from seed.text.StepDecoder import StepDecoder__bytes2str, OutputCase_of_StepDecoderABC_feeds as _FOC

see:
    seed.iters.find
        #search subseq
        #using failure_func
    nn_ns.bin.stream_search
        #search subseq
        #using polynomial hash
    seed.seq_tools.seq_index_if
        #search value
        #using predicator
    seed.text.StepDecoder
        #def&search "line"
        #using step_builder,step_predicator


see:
    codecs.getincrementaldecoder
    codecs.getincrementalencoder

used by:
    <phone_txt>/txt/script/欧路词典.py



LookupError
    codecs.lookup(encoding)
    codecs.getincrementalencoder(encoding)
    codecs.getincrementaldecoder(encoding)

ValueError
    UnicodeError(encoding, object, start, end, reason)
        #err.object[err.start:err.end]

        UnicodeDecodeError
        UnicodeEncodeError
        UnicodeTranslateError
class codecs.IncrementalDecoder
    decode(object[, final])
    reset()
    getstate()
    setstate(state)
 class codecs.CodecInfo(encode, decode, streamreader=None, streamwriter=None, incrementalencoder=None, incrementaldecoder=None, name=None)
    name
    encode
    decode
    incrementalencoder
    incrementaldecoder
    streamwriter
    streamreader



#'''

__all__ = r'''
    StepDecoderABC
        OutputCase_of_StepDecoderABC_feeds
        StepDecoder__bytes2str
        get_end_pos
        flip_enumerate__iter_seq
        flip_enumerate__istream

    to_step_builder
        mk_StepBuilder__convert
    to_step_predicator


    IStepBuilder
        StepBuilder__convert
            StepBuilder__list
            StepBuilderABC__istream
                StepBuilder__str
                StepBuilder__bytes
        StepBuilder__convert_set
            StepBuilder__set
            StepBuilder__frozenset
    IStepPredicator
        StepPredicator__False
        StepPredicator__test_last_only

    '''.split()



#from .abc import ABC, abstractmethod, override, not_implemented, ABCMeta
from abc import ABC, abstractmethod
from seed.tiny import snd, fst
import io
from enum import Enum, unique, auto
from collections import deque
import codecs
from itertools import islice


@unique
class OutputCase_of_StepDecoderABC_feeds(Enum):
    SUCC = auto()
    ERR = auto()
    EOF = auto()
_FOC = OutputCase_of_StepDecoderABC_feeds

class IStepBuilder(ABC):
    @abstractmethod
    def feed(sf, x):
        'x -> ()'
    @abstractmethod
    def mk(sf):
        '-> target'
    @abstractmethod
    def reset(sf):
        '() -> ()'
    @abstractmethod
    def mk_then_reset(sf):
        '-> target'
        r = sf.mk()
        sf.reset()
        return r

class IStepPredicator(ABC):
    #???IStepPredicator <: IStepBuilder???
    #   maybe we want an object has both mk/is_ok
    @abstractmethod
    def is_ok(sf):
        '-> bool'
    @abstractmethod
    def feed(sf, x):
        'x -> ()'
    @abstractmethod
    def reset(sf):
        '() -> ()'




class StepDecoderABC(ABC):
    @abstractmethod
    def get_FeedErrors(sf):
        'tuple<Exception> #feed() decode error bases'
    @abstractmethod
    def reset(sf):
        '() -> ()'
    @abstractmethod
    def feed(sf, begin_pos, x, end_pos):
        'begin_pos -> i -> end_pos -> (may_o, succ_begin_pos, used::[(i, end_pos)], len_remains)'
    @abstractmethod
    def get_len_remains(sf):
        '-> len_remains'
    @abstractmethod
    def get_remain_pairs(sf, remains_end_pos):
        'remains_end_pos -> (remains_begin_pos, remain_pairs::[(i,end_pos)])'
    @abstractmethod
    def append_and_pop_all_and_reset(sf, begin_pos, i, end_pos):
        'begin_pos -> i -> end_pos -> (err_begin_pos, err_i::i, err_end_pos, unused::[(i,end_pos)])#reset decoder!!!'


    def feeds__iter_seq(sf, begin_pos, xs):
        r'''begin_pos -> Iter i -> feeds_output
        feeds_output: output of feeds__pairs
        #'''
        it = flip_enumerate__iter_seq(begin_pos, xs)
        return sf.feeds__pairs(begin_pos, it)

    def feeds__istream(sf, istream):
        r'''istream -> feeds_output
        feeds_output: output of feeds__pairs
        #'''
        begin_pos = istream.tell()
        it = flip_enumerate__istream(istream)
        return sf.feeds__pairs(begin_pos, it)

    def feeds__pairs(sf, begin_pos, pairs):
        'begin_pos -> Iter (i,end_pos) -> Iter <(SUCC, succ_begin_pos, used::[(i,end_pos)], o)  | (ERR, err_begin_pos, err_i::i, err_end_pos) | (EOF, remains_begin_pos, remain_pairs::[(i,end_pos)])>'
        it = sf._feeds__pairs(begin_pos, pairs)
        return it
    def _feeds__pairs(sf, begin_pos, pairs):
        FeedErrors = sf.get_FeedErrors()
        def add_f(pairs):
            pairss.append(iter(pairs))
        def iter_f(pairss):
            while pairss:
                pairs = pairss[-1]
                for i, end_pos in pairs:
                    yield i, end_pos
                    break
                else:
                    pairss.pop()
        pairss = []
        add_f(pairs)
        end_pos = begin_pos
        for i, end_pos in iter_f(pairss):
            #rint(i, end_pos)
            try:
                z = sf.feed(begin_pos, i, end_pos)
            except FeedErrors:
                #bug: [(err_begin_pos, err_i, err_end_pos)] = sf.may_skip1()
                #   when raise, not eat actually
                (err_begin_pos, err_i, err_end_pos, unused) = sf.append_and_pop_all_and_reset(begin_pos, i, end_pos)
                yield _FOC.ERR, err_begin_pos, err_i, err_end_pos
                #bug:begin_pos = err_end_pos
                #   should be: end_pos=err_end_pos, since below update begin_pos=end_pos
                begin_pos = end_pos = err_end_pos
                add_f(unused)
            else:
                [may_o, succ_begin_pos, used, len_remains
                    ] = z
                #bug: without "if may_o:"
                #   cause: feed() API wrong! "o" should be may_o
                if may_o:
                    [o] = may_o
                    yield _FOC.SUCC, succ_begin_pos, used, o
                elif used:
                    raise logic-err
            begin_pos = end_pos
        else:
            remains_end_pos = end_pos
            (remains_begin_pos, remain_pairs) = sf.get_remain_pairs(remains_end_pos)
            yield _FOC.EOF, remains_begin_pos, remain_pairs


    def iter_lines__feeds_output(sf
            , feeds_output
            , *
            , step_builder=None
            , step_predicator=None
            , donot_reset_step_predicator_at_global_start=False
            , donot_reset_step_builder_at_global_start=False
            ):
        r'''step_builder -> step_predicator -> feeds_output -> Iter (line_begin_pos, line::[o], line_end_pos, end_case)


    post-condition:
        * result_iter is not empty
        * last-line-end_pos maybe not stream-end_pos, #but not errs+incomplete_remain_tail+eof
        * empty line or line not accepted by step_predicator ==>> next is err or incomplete_remain_tail+eof

        end_case :: OutputCase_of_StepDecoderABC_feeds
            * EOF: curr line terminated by incomplete_remain_tail+eof
            * ERR: curr line terminated by err
            * SUCC: curr line terminated by step_predicator


    input:
        step_builder :: IStepBuilder or None or callable
            step_builder = to_step_builder(step_builder)
            * None => StepBuilder__list()
                default output list<o>
            * callable => mk_StepBuilder__convert(iter2target)
                NOTE: can be class str

        step_predicator :: IStepPredicator or None or callable or container
            step_predicator = to_step_predicator(step_predicator)
            * None => StepPredicator__False()
                default is_ok()->False forever
            * callable => StepPredicator__test_last_only(predicator)
            * container => StepPredicator__test_last_only(container.__contains__)

        feeds_output:
            output of feeds__pairs/feeds__istream/feeds__iter_seq

        #'''
        step_predicator = to_step_predicator(step_predicator)
        step_builder = to_step_builder(step_builder)


        if not donot_reset_step_predicator_at_global_start:
            step_predicator.reset()
        if not donot_reset_step_builder_at_global_start:
            step_builder.reset()

        def mk(line_begin_pos, line_end_pos, end_case):
            nonlocal step_builder
            line = step_builder.mk_then_reset()
            step_predicator.reset()
            return line_begin_pos, line, line_end_pos, end_case

        prev_case = _FOC.SUCC
        if 1:
            #line_begin_pos = ???
            init = True
        for record in feeds_output:
            if prev_case is _FOC.EOF: raise ValueError('not a valid feeds_output: eof is.not at last')

            if init:
                line_begin_pos = record[1]
                init = False

            case = record[0]
            if case is _FOC.SUCC:
                (_, succ_begin_pos, used, o) = record
                if prev_case is not _FOC.SUCC:
                    line_begin_pos = succ_begin_pos
                if 1:
                    #[o] = may_o
                    step_builder.feed(o)
                    step_predicator.feed(o)
                    if step_predicator.is_ok():
                        succ_end_pos = get_end_pos(succ_begin_pos, used)
                        line_end_pos = succ_end_pos
                        end_case = case
                        yield mk(line_begin_pos, line_end_pos, end_case)
                        line_begin_pos = line_end_pos
            elif case is _FOC.ERR:
                if prev_case is _FOC.SUCC:
                    (_, err_begin_pos, err_i, err_end_pos) = record
                    line_end_pos = err_begin_pos
                    end_case = case
                    yield mk(line_begin_pos, line_end_pos, end_case)
            elif case is _FOC.EOF:
                (_, remains_begin_pos, remain_pairs) = record
                if prev_case is not _FOC.SUCC:
                    line_begin_pos = remains_begin_pos
                line_end_pos = remains_begin_pos
                end_case = case
                yield mk(line_begin_pos, line_end_pos, end_case)
            else:
                raise logic-err
            prev_case = case
        else:
            if prev_case is not _FOC.EOF: raise ValueError('not a valid feeds_output: empty or last is not eof')
        return



def get_end_pos(begin_pos, pairs):
    if pairs:
        end_pos = pairs[-1][1]
    else:
        end_pos = begin_pos
    return end_pos
def flip_enumerate__iter_seq(begin_pos, xs):
    '-> Iter (x, end_pos)'
    for end_pos, x in enumerate(xs, begin_pos+1):
        yield x, end_pos
def flip_enumerate__istream(istream):
    '-> Iter (x, end_pos)'
    end_pos = istream.tell()
    while 1:
        bs = istream.read(1)
        if not bs:
            assert end_pos == istream.tell()
            break
        [x] = bs
        end_pos = istream.tell()
        yield x, end_pos

def ls_map_snd(pairs):
    return [*map(snd, pairs)]




























##################################
##################################
##################################
##################################
def to_step_builder(x):
    r''' x -> IStepBuilder
    x :: IStepBuilder or None or callable
        * step_builder
        * None => StepBuilder__list()
        * callable => mk_StepBuilder__convert(iter2target)
    #'''
    if x is None:
        step_builder = StepBuilder__list()
    elif isinstance(x, IStepBuilder):
        step_builder = x
    elif callable(x):
        iter2target = x
        step_builder = mk_StepBuilder__convert(iter2target)
    else:
        raise TypeError(f'not IStepBuilder: {x!r}')
    return step_builder

def to_step_predicator(x):
    r'''x -> IStepPredicator
    x :: IStepPredicator or None or callable or container
        * step_predicator
        * None => StepPredicator__False()
        * callable => StepPredicator__test_last_only(predicator)
        * container => StepPredicator__test_last_only(container.__contains__)
    #'''

    if x is None:
        step_predicator = StepPredicator__False()
    elif isinstance(x, IStepPredicator):
        step_predicator = x
    elif callable(x):
        predicator = x
        step_predicator = StepPredicator__test_last_only(predicator)
    elif hasattr(x, '__contains__'):
        container = x
        predicator = container.__contains__
        step_predicator = StepPredicator__test_last_only(predicator)
    else:
        raise TypeError(f'not IStepPredicator: {x!r}')
    return step_predicator


def mk_StepBuilder__convert(iter2target):
    r'''
    mk_StepBuilder__convert vs StepBuilder__convert:
        diff:
            iter2target := str
        spec:
            iter2target := bytes
            iter2target := list
            iter2target := set
            iter2target := frozenset

    #'''
    args = []
    if iter2target is str:
        cls = StepBuilder__str
    elif iter2target is bytes:
        cls = StepBuilder__bytes
    elif iter2target is list:
        cls = StepBuilder__list
    elif iter2target is set:
        cls = StepBuilder__set
    elif iter2target is frozenset:
        cls = StepBuilder__frozenset
    else:
        cls = StepBuilder__convert
        args = [iter2target]
    self = cls(*args)
    return self

class StepBuilder__convert(IStepBuilder):
    def __init__(sf, iter2target):
        sf._f = iter2target
        sf.__init()
    def __init(sf):
        sf._ls = []
    def feed(sf, x):
        'x -> ()'
        sf._ls.append(x)
    def mk(sf):
        '-> target'
        return sf._f(iter(sf._ls))
    def reset(sf):
        '() -> ()'
        sf.__init()
    def mk_then_reset(sf):
        '-> target'
        if sf._f is list:
            ls = sf._ls
            sf.__init()
            return ls
        else:
            return super().mk_then_reset()

class StepBuilder__list(IStepBuilder):
    def __init__(sf):
        sf.__init()
    def __init(sf):
        sf._ls = []
    def feed(sf, x):
        'x -> ()'
        sf._ls.append(x)
    def mk(sf):
        '-> target'
        return list(sf._ls)
    def reset(sf):
        '() -> ()'
        sf.__init()
    def mk_then_reset(sf):
        '-> target'
        ls = sf._ls
        sf.__init()
        return ls

class StepBuilderABC__stream(IStepBuilder):
    def __init__(sf, mkIO):
        sf._mkIO = mkIO
        sf.__init()
    def __init(sf):
        sf._stream = sf._mkIO()
        sf._begin = sf._stream.tell()
        sf._sz = 0
    def reset(sf):
        '() -> ()'
        sf.__init()
    def write(sf, xs):
        '[x] -> ()'
        sf._sz += sf._stream.write(xs)
    def mk(sf):
        '-> target'
        end = sf._stream.tell()
        sf._stream.seek(sf._begin)
        s = sf._stream.read(sf._sz)
        if sf._stream.tell() != end:
            raise logic-err
        return s
    def mk_then_reset(sf):
        '-> target'
        return super().mk_then_reset()


class StepBuilder__str(StepBuilderABC__stream):
    def __init__(sf, mkIO=None):
        if mkIO is None:
            mkIO = io.StringIO
        super().__init__(mkIO)
    def feed(sf, x):
        'x -> ()'
        sf.write(x)

class StepBuilder__bytes(StepBuilderABC__stream):
    def __init__(sf, mkIO=None):
        if mkIO is None:
            mkIO = io.BytesIO
        super().__init__(mkIO)
    def feed(sf, x):
        'x -> ()'
        bs = bytes([x])
        sf.write(bs)

class StepBuilder__convert_set(IStepBuilder):
    def __init__(sf, iter2target):
        sf._f = iter2target
        sf.__init()
    def __init(sf):
        sf._set = set()
    def feed(sf, x):
        'x -> ()'
        sf._set.add(x)
    def mk(sf):
        '-> target'
        return sf._f(iter(sf._set))
    def reset(sf):
        '() -> ()'
        sf.__init()
    def mk_then_reset(sf):
        '-> target'
        if sf._f is set:
            s = sf._set
            sf.__init()
            return s
        else:
            return super().mk_then_reset()



class StepBuilder__set(IStepBuilder):
    def __init__(sf):
        sf.__init()
    def __init(sf):
        sf._set = set()
    def feed(sf, x):
        'x -> ()'
        sf._set.add(x)
    def mk(sf):
        '-> target'
        return set(sf._set)
    def reset(sf):
        '() -> ()'
        sf.__init()
    def mk_then_reset(sf):
        '-> target'
        s = sf._set
        sf.__init()
        return s
class StepBuilder__frozenset(StepBuilder__set):
    def mk(sf):
        '-> target'
        return frozenset(sf._set)
    def mk_then_reset(sf):
        '-> target'
        return IStepBuilder.mk_then_reset(sf)




class StepPredicator__False(IStepPredicator):
    def is_ok(sf):
        '-> bool'
        return False
    def feed(sf, x):
        'x -> ()'
        pass
    def reset(sf):
        '() -> ()'
        pass


class StepPredicator__test_last_only(IStepPredicator):
    def __init__(sf, predicator):
        sf._may = ()
        sf._f = predicator
    def is_ok(sf):
        '-> bool'
        return sf._may and sf._f(sf._may[0])
    def feed(sf, x):
        'x -> ()'
        sf._may = (x,)
    def reset(sf):
        '() -> ()'
        sf._may = ()























##################################
##################################
##################################
##################################
class StepDecoder__bytes2str(StepDecoderABC):
    def get_FeedErrors(sf):
        'tuple<Exception> #feed() decode error bases'
        return (UnicodeDecodeError,)
    def __init__(sf, encoding):
        sf._encoding = encoding
        sf._Encoder = codecs.getincrementalencoder(encoding)
        sf._Decoder = codecs.getincrementaldecoder(encoding)
        sf._encoder = sf._Encoder()
        sf._decoder = sf._Decoder()
        sf.__init()
    def __init(sf):
        sf._encoder.reset()
        sf._decoder.reset()
        sf._dq = deque() #[(i, end_pos)]
        #sf._Nothing = object()
        sf._may_remains_begin_pos = []
    def reset(sf):
        '() -> ()'
        sf.__init()
    def get_len_remains(sf):
        '-> len_remains'
        return len(sf._dq)
    def get_remain_pairs(sf, remains_end_pos):
        'remains_end_pos -> (remains_begin_pos, remain_pairs::[(i,end_pos)])'
        if sf._may_remains_begin_pos:
            [remains_begin_pos] = sf._may_remains_begin_pos
        else:
            remains_begin_pos = remains_end_pos
        remain_pairs = [*sf._dq]
        return remains_begin_pos, remain_pairs

    def append_and_pop_all_and_reset(sf, begin_pos, i, end_pos):
        'begin_pos -> i -> end_pos -> (err_begin_pos, err_i::i, err_end_pos, unused::[(i,end_pos)])#reset decoder!!!'
        sf._push(begin_pos, i, end_pos)
        assert sf._dq
        assert sf._may_remains_begin_pos
        [remains_begin_pos] = sf._may_remains_begin_pos
        err_begin_pos = remains_begin_pos
        (err_i, err_end_pos) = sf._dq.popleft()
        remains_begin_pos = err_end_pos
        sf._may_remains_begin_pos = [remains_begin_pos]
        #return (err_begin_pos, err_i, err_end_pos)

        #####
        unused = [*sf._dq]
        sf.reset()
        return (err_begin_pos, err_i, err_end_pos, unused)

    def _push(sf, begin_pos, x, end_pos):
        if sf._may_remains_begin_pos:
            [remains_begin_pos] = sf._may_remains_begin_pos
            prev_end_pos = get_end_pos(begin_pos, sf._dq)
            if begin_pos != prev_end_pos: raise Exception
        else:
            assert not sf._dq
            remains_begin_pos = begin_pos
            sf._may_remains_begin_pos = [remains_begin_pos]
        sf._may_remains_begin_pos
        remains_begin_pos
        sf._dq.append((x, end_pos))

    def _mk_remain_bs(sf):
        rs = bytes(map(fst, sf._dq))
        return rs
    def feed(sf, begin_pos, x, end_pos):
        'begin_pos -> i -> end_pos -> (may_o, succ_begin_pos, used::[(i, end_pos)], len_remains)'
        sf._push(begin_pos, x, end_pos)
        [remains_begin_pos] = sf._may_remains_begin_pos
        dq = sf._dq

        decoder = sf._decoder
        saved_st1_rollback = decoder.getstate()
        def on_err(Error, *args, **kw):
            dq.pop()
            decoder.setstate(saved_st1_rollback)
                #not saved_st2_final!!!!!
            raise Error(*args, **kw)

        b1 = bytes([x])
        try:
            s1 = decoder.decode(b1)
        except ValueError as e:
            [DecodeError] = sf.get_FeedErrors()
            #UnicodeError(encoding, object, start, end, reason)
            rs = sf._mk_remain_bs()
            on_err(DecodeError, sf._encoding, rs, 0, len(rs), f"@bytes[{remains_begin_pos}:{end_pos}]")#UnicodeDecodeError
        assert len(s1) <= 1
        if s1:
            [ch] = s1
            assert ch == s1
            encoder = sf._encoder
            encoder.reset()
            new_bs = encoder.encode(s1, final=True)
            n = len(new_bs)
            rs = sf._mk_remain_bs()
            #old_bs = bytes(map(fst, islice(dq, n)))
            old_bs = rs[:n]
            LogicErr = Exception
            if new_bs != old_bs:
                on_err(LogicErr, f"assume encode is inverse of decode, fail: {rs!r} -> {ch!r} -> {new_bs!r} != {old_bs!r}")

            saved_st2_final = decoder.getstate()
            decoder.reset()
            try:
                s2 = decoder.decode(old_bs, final=True)
            except ValueError:
                on_err(LogicErr, f"assume encode is inverse of decode, fail: {rs!r} -> {ch!r} -> {new_bs!r} -> decode fail")
            if s1 != s2:
                on_err(LogicErr, f"assume encode is inverse of decode, fail: {rs!r} -> {ch!r} -> {new_bs!r} -> {s2!r} != {s1!r}")

            ts = rs[n:]
            decoder.reset()
            try:
                s3 = decoder.decode(ts)
            except ValueError:
                on_err(LogicErr, f"assume encode is inverse of decode, fail: {rs!r} -> {ch!r} -> {new_bs!r};  {ts!r} -> partial decode fail")

            if s3 != '':
                on_err(LogicErr, f"assume encode is inverse of decode, fail: {rs!r} -> {ch!r} -> {new_bs!r};  {ts!r} -> {s3!r} != ''")
            st = decoder.getstate()
            if st != saved_st2_final:
                on_err(LogicErr, f"assume encode is inverse of decode, fail: {rs!r} -> {ch!r} -> {new_bs!r};  {ts!r} -> {s3!r} but st={st!r} != {saved_st2_final!r}")
            len_used = n
            may_ch = (ch,)

        else:
            len_used = 0
            may_ch = ()
        may_ch
        len_used
        #bug:used = [dq.pop() for _ in range(len_used)]
        used = [dq.popleft() for _ in range(len_used)]
        succ_begin_pos = remains_begin_pos
        succ_end_pos = get_end_pos(succ_begin_pos, used)
        remains_begin_pos = succ_end_pos
        sf._may_remains_begin_pos = [remains_begin_pos]
        len_remains = len(dq)

        if 0 and may_ch:
            print(f"{rs!r}, {ch!r}")
            print(f"{succ_begin_pos!r}, {used!r}")
        return (may_ch, succ_begin_pos, used, len_remains)




























def _t():
    txt_1 = r'''
天行健，君子以自强不息
  易::乾
  《象》曰：“天行健，君子以自强不息。”

十室之邑，必有忠信
  论语::公冶长
  子曰：“十室之邑，必有忠信如丘者焉，不如丘之好学也。”

楚师之惧，我不修也...冀州之土，其无令君乎？
  国语::卷十-晋语四::8-楚成王以周礼享重耳
   令尹子玉曰：“请杀晋公子。弗杀，而反晋国，必惧楚师。”王曰：“不可。楚师之惧，我不修也。我之不德，杀之何为！天之祚楚，谁能惧之？楚不可祚，冀州之土，其无令君乎？且晋公子敏而有文，约而不谄，三材待之，天祚之矣。天之所兴，谁能废之？”

奢靡使人迷信:要加钱？不，我选择科学



#''' + '\r\n\n\r\r\n\r\n'
    txt_2 = "富有即榜样，美丽即善良"
    bad_bs = b'\xff'*4
    snippet_bs = b'\xf8c\xbc\xf8\xca\xd2r\x9a\xe6+\xfc\xcf\x94\x03\xf1-\x16\xa3\xc7\x8d\x9fT'
    snippet_cmd = "snippet 20017.eudb -c 1 -n 22 -b 1040"

    encodings = 'u8 utf_16_le utf_32_le gbk'.split()
    encodings = 'u8'.split()



    #encodings = 'utf_32_le'.split()
    sep = '\n'*3
    ban = '='*9
    for encoding in encodings:
        print(f'{sep}{ban}{encoding!r}{ban}')
        step_decoder = StepDecoder__bytes2str(encoding)


        expr_1 = 'txt_1.encode(encoding)'
        bs_1 = eval(expr_1)
        mk_bs_ls = [(expr_1, bs_1), (snippet_cmd, snippet_bs)]

        good_bs = txt_2.encode(encoding)
        incomplete_bs = '我'.encode(encoding)[:-1]
        sss = r"""[b''
            ,bad_bs
            ,good_bs
            #
            ,incomplete_bs
            ,bad_bs+incomplete_bs
            ,good_bs+incomplete_bs
            #
            ,bad_bs+good_bs
            ,good_bs+bad_bs
            ,bad_bs+good_bs+incomplete_bs
            ,good_bs+bad_bs+incomplete_bs
            #
            ,bad_bs+good_bs+bad_bs
            ,good_bs+bad_bs+good_bs
            ,bad_bs+good_bs+bad_bs+incomplete_bs
            ,good_bs+bad_bs+good_bs+incomplete_bs
            #
            ]
            #"""
        exprs = sss.translate(dict(zip(map(ord, '[],#'), ' '*222))).split()
        #bss = [*map(eval, exprs)]

        mk_bs_it_ls = []
        for expr_, bs_ in mk_bs_ls:
            istream_ = io.BytesIO(bs_)
            feeds_output_ = step_decoder.feeds__istream(istream_)
            mk_bs_it_ls.append((expr_, bs_, feeds_output_))
        #for bs_ in bss:
        for expr_ in exprs:
            bs_ = eval(expr_)
            feeds_output_ = step_decoder.feeds__iter_seq(0, bs_)
            mk_bs_it_ls.append((expr_, bs_, feeds_output_))

        for expr_, bs_, feeds_output_ in mk_bs_it_ls:
            step_decoder.reset()
            it = step_decoder.iter_lines__feeds_output(feeds_output_, step_predicator='\n', step_builder=str)
            print()
            print(f'===={expr_!r}====')
            print(f'===={bs_!r}====')
            print(f'====sz={len(bs_)}====')
            for line in it:
                print(f'{line!r}')

if __name__ == '__main__':
    _t()


