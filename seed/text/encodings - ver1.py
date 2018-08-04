
__all__ = []
__all__ = ('''
    all_encodings encoding_info to_std_encoding python_encoding2html_encoding
    big5 utf8 gb18030 gbk gb u8
    zh_cn_encoding sys_encoding text_encoding
    exists_encoding
    includes_char
    try_all_encodings try_encoding try_encodings
    name2BOM
    skip_BOM_for_bytes skip_BOM_for_str skip_BOM_for_TextIO

    idecode

''').split()
##
##from sand import fixed__package__
##fixed__package__(globals())
##from sand import top_level_import
##assert top_level_import(__name__, 'import_main.forgot_import', args=('logic error',))
##assert top_level_import(__name__, 'import_main.collect_globals',
##        kwargs=dict(pred=None, include='', exclude='''
##    convert get_encoding_ls
##    get_first_word includes 
##    main'''))



import sys
import locale
import codecs
from seed.filesys.glob1 import glob1
from seed.text.encodings import *


u8 = utf8 = 'utf-8'
gb = gb18030 = 'gb18030'
big5 = 'big5'
gbk = 'gbk'


#mbcs = 'mbcs'


zh_cn_encoding = gb18030






    





#print(name2BOM)
def lengths_of_matched_BOMs(bytes_):
    name_BOM_pairs = which_BOMs_match(bytes_)
    Ls = tuple(map(len, (BOM for name, BOM in name_BOM_pairs)))
    return Ls

def max_length_of_matched_BOM(bytes_):
    Ls = lengths_of_matched_BOMs(bytes_)
    return max(Ls) if Ls else 0

def skip_BOM_for_bytes(bytes_):
    L = max_length_of_matched_BOM(bytes_)
    return bytes_[L:]

def skip_BOM_for_str(str_):
    L = int(str_.startswith('\ufeff'))
    return str_[L:]

def skip_BOM_for_TextIO(file):
    file = iter(file)
    for line in file:
        yield skip_BOM_for_str(line)
    yield from file














def includes_char(encoding, char:str):
    assert len(char) == 1
    try:
        c2 = char.encode(encoding).decode(encoding)
        return char == c2
    except:
        return False
includes = includes_char

#BOM (“Byte Order Mark”)  U+FEFF

def _find_fail_subrange(state, inc_decoder, data, begin, end):
    if end - begin < 2:
        return None

    mid = (begin + end)//2
    try:
        inc_decoder.decode(data[begin:mid], final=False)
    except ValueError:
        inc_decoder.setstate(state)
        end = mid
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
##    
##class DecodeError__FailRange(ValueError):
##    def __init__(self, begin, end):
##        self.begin = begin
##        self.end = end
##        super().__init__('decode fail in [{}:{}]'.format(begin, end))
##import operator
##class Subbytes:
##    def __init__(self, data, offset):
##        self.data = data
##        self.offset = offset
##    def __getitem__(self, idx_or_slice):
##        offset = self.offset
##        if isinstance(idx_or_slice, slice):
##            s = idx_or_slice
##            begin, end, step = s.indices(len(self.data))
##            begin -= offset
##            end -= offset
##            if begin < 0:
##                raise ValueError('out-of-range')
##            return self.data[begin:end:step]
##        else:
##            i = operator.index(idx_or_slice)
##            i -= offset
##            if i < 0:
##                raise ValueError('out-of-range')
##            return self.data[i]
##            

class UnicodeDecodeError_NoObject(UnicodeDecodeError):
    def __init__(self, encoding, fail_bytes, start, end, reason):
        super().__init__(encoding, b'', start, end, reason)
        self.fail_bytes = fail_bytes
    

def makeUnicodeDecodeError(encoding, object, start, end, reason):
    return UnicodeDecodeError(encoding, object, start, end, reason)

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
    

_try_encodings = (zh_cn_encoding, sys_encoding, utf8, big5, 'shift_jis', 'utf_16_le', 'utf_16_be', 'utf_32_be', 'utf_32_le')
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



def main(args = None):
    import argparse, sys

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

    if args == None:
        args = parser.parse_args()
    else:
        args = parser.parse_args(args)

    outputencoding = args.outputencoding
    output = args.output
    b_output = outputencoding or output
    if outputencoding == None:
        outputencoding = utf8
    if output == None:
        output = sys.stdout
    else:
        output = open(output, 'x', encoding=outputencoding)
        

    encodings = args.encodings
    try:
        fname = glob1(args.fname)
    except ValueError as e:
        print(e, file=sys.stderr)
        parser.exit(1)
        raise logic-error
        
    if args.try_all:
        encodings += args.try_all
        rencodings = try_all_encodings(fname, encodings)
        print(rencodings)
        return 0

    
    encoding = try_encodings(fname, encodings, detail=args.detail)
    
    if encoding != None and not b_output:
        print(encoding)
        
    if encoding != None and b_output:
        with open(fname, encoding=encoding) as fin:
            if output is sys.stdout:
                convert(fin, output)
            else:
                with output:
                    convert(fin, output)
            
    


if __name__ == "__main__":
    main()




