
#import locale
import codecs
from seed.text.encodings import sys_encoding, text_encoding
from seed.tiny import print_err

gb18030 = 'gb18030'
big5 = 'big5'
gbk = 'gbk'
utf8 = 'utf-8'

zh_cn_encoding = gb18030


def _find_fail_subrange(state, inc_decoder, data, begin, end):
    if end - begin < 2:
        return None

    mid = (begin + end)//2
    try:
        inc_decoder.decode(data[begin:mid], final=False)
    except ValueError:
        inc_decoder.setstate(state)
        end = mid
    except Exception:
        print_err(f'begin={begin}, mid={mid}, end={end}')
        print_err(f'inc_decoder={inc_decoder}')
        raise
    else:
        state = inc_decoder.getstate()
        begin = mid
    return (state, begin, end)

def find_fail_range(state, inc_decoder, offset, data, final):
    inc_decoder.setstate(state)
    if final:
        try:
            inc_decoder.decode(data, final=False)
        except:
            # not caused by final=True
            pass
        else:
            unused_bytes, _ = inc_decoder.getstate()
            end = offset + len(data)
            begin = end - len(unused_bytes)
            return begin, end

    final = False

    begin = 0
    end = len(data)
    while True:
        r = _find_fail_subrange(state, inc_decoder, data, begin, end)
        if not r:
            break

        (state, begin, end) = r

    unused_bytes, _ = inc_decoder.getstate()
    end = offset + end
    begin = end - len(unused_bytes)
    return begin, end


def _decode(inc_decoder, offset, data, final):
    # data = org_bytes[offset:len(data)]
    state = inc_decoder.getstate()
    try:
        r = inc_decoder.decode(data, final=final)
        return (True, r)
    except:
        pass

    # find fail position
    begin, end = rng = find_fail_range(state, inc_decoder, offset, data, final)
    fail_bytes = data[begin-offset:end-offset]

    return (False, (rng, fail_bytes))
find_fail_range

class UnicodeDecodeError_NoObject(UnicodeDecodeError):
    def __init__(self, encoding, fail_bytes, start, end, reason):
        super().__init__(encoding, b'', start, end, reason)
        self.fail_bytes = fail_bytes



codecs
def idecode(file, encoding, errors='strict', *, chunk_size = 2**10):
    'yield str; raise UnicodeDecodeError_NoObject'
    assert chunk_size > 0
    codec_info = codecs.lookup(encoding)
    inc_decoder = codec_info.incrementaldecoder(errors)
    final = False
    offset = 0
    bs = b'1' # only for initial
    while bs:
        bs = file.read(chunk_size)
        final = not bs

        success, r = _decode(inc_decoder, offset, bs, final)
        if success:
            string = r
            yield string
            offset += len(bs)
        else:
            (begin, end), _ = fail_range, fail_bytes = r
            raise UnicodeDecodeError_NoObject(
                encoding=encoding,
                reason='raise when decoding',
                start=begin, end=end,
                fail_bytes=fail_bytes)


    return





_try_encodings = (zh_cn_encoding, sys_encoding, text_encoding, utf8, big5
        , 'shift_jis', 'utf_16_le', 'utf_16_be', 'utf_32_be', 'utf_32_le')
def try_encoding(fname, encoding, detail=None, errors='strict'):
    # detail is a file to output error msg

    try:
##        with open(fname, encoding=encoding, errors=errors) as fin:
##            for line in fin:
##                pass
        with open(fname, 'rb') as fin:
            for _ in idecode(fin, encoding, errors=errors):pass

    except UnicodeDecodeError_NoObject as e:
        if detail is not None:
            s = ('err={!s}; encoding={!r}; reason={!r}; '
                 'fail_range=[{}:{}]; fail_bytes={!r}; '
                 .format(e, e.encoding, e.reason,
                         e.start, e.end, e.fail_bytes)
                 )
            print(s, file=detail)
        return False

    except UnicodeError as e:
        if detail is not None:
            s = ('err={!s}; encoding={!r}; reason={!r}; '
                 'fail_range=[{}:{}]; fail_bytes={!r}; '
                 .format(e, e.encoding, e.reason,
                         e.start, e.end, e.object[e.start:e.end])
                 )
            print(s, file=detail)
        return False
    except ValueError as e:
        if detail is not None:
            s = ('err={!s}; encoding={!r}; mode={!r}'
                 .format(e, encoding, errors)
                 )
            print(s, file=detail)
        #raise logic - error # not UnicodeError ??
        return False
    except Exception:
        print_err(f'encoding={encoding}')
        raise
    return True

def try_encodings(fname, encodings = _try_encodings, detail=None):
    for encoding in encodings:
        if try_encoding(fname, encoding, detail=detail):
            return encoding
    else:
        return None

def try_all_encodings(fname, encodings = _try_encodings):
    ls = [encoding for encoding in encodings if try_encoding(fname, encoding)]
    return ls



def convert(fin, fout):
    for line in fin:
        fout.write(line)







utf8

_try_encodings
try_all_encodings
try_encodings
convert

def iter_apply_without_encodings(encodings, without_encodings):
    without_encodings = frozenset(without_encodings)
    return (encoding for encoding in encodings
            if encoding not in without_encodings
            )
def main(argv = None):
    import argparse, sys
    from seed.filesys.glob1 import glob1
    from seed.text.encodings import all_encodings, encoding_info

    parser = argparse.ArgumentParser(description='try some encodings to decode a file')
    parser.add_argument('fname', type=str,
                        help='file name')

    parser.add_argument('-oe', '--outputencoding', type=str,
                        default=None,
                        help='encoding of output file')
    parser.add_argument('-o', '--output', type=str,
                        default=None,
                        help='name of output file')

    parser.add_argument('-e', '--encodings', type=str,
                        nargs='+', default=_try_encodings,
                        help='encoding list which would be used to decode file, '
                        'possible encoding names are:\n' + encoding_info)

    parser.add_argument('-d', '--detail', action='store_const',
                        const=sys.stderr, default=None,
                        help='show fail bytes in stderr if fail and not try_all')

    parser.add_argument('--try_all', action='store_const',
                        const=all_encodings, default=(),
                        help='try all known encodings: ' + repr(all_encodings))

    parser.add_argument('-wo', '--without_encodings', type=str,
                        nargs='+', default=[],
                        help='encoding list which would be avoid to use to decode file'
                        )

    args = parser.parse_args(argv)
    encodings = args.encodings
    without_encodings = frozenset(args.without_encodings)
    try:
        fname = glob1(args.fname)
    except ValueError as e:
        print(e, file=sys.stderr)
        parser.exit(1)
        raise logic-error

    if args.try_all:
        encodings += args.try_all
    encodings = iter_apply_without_encodings(encodings, without_encodings)

    if args.try_all:
        result_encodings = try_all_encodings(fname, encodings)
        print(result_encodings)
        return 0


    encoding = try_encodings(fname, encodings, detail=args.detail)
    if encoding is None:
        parser.exit(0)
        return 0

    outputencoding = args.outputencoding
    output = args.output
    to_convert = outputencoding or output
    if not to_convert:
        print(encoding)
        parser.exit(0)
        return 0



    with open(fname, encoding=encoding) as fin:
        if output is None:
            fout = sys.stdout
            convert(fin, fout)
            parser.exit(0)
            return 0

        if outputencoding == None:
            outputencoding = utf8
        with open(output, 'xt', encoding=outputencoding) as fout:
            convert(fin, fout)
            parser.exit(0)
            return 0




if __name__ == "__main__":
    main()



