
r'''
change chardet input from bytes to file

assert file2maybe_encoding('末一'.encode('gbk')) == 'utf-8'
#not good!!!!!!!!!!
'''

__all__ = '''
    detect_encoding
    file2maybe_encoding
    '''.split()


from chardet.universaldetector import UniversalDetector
from seed.io.iter_reads import iter_reads
from io import BytesIO, TextIOWrapper



BLOCK_SIZE = 2048

def detect_encoding(bin_istream, block_size):
    # (bin_istream|bytes) -> result
    # (BinaryIO|Bytes) -> {encoding::Maybe str, confidence::float, language::Maybe str}
    worker = UniversalDetector()
    if not hasattr(bin_istream, 'read'):
        bs = bin_istream
        if not isinstance(bs, (bytes, bytearray)): raise TypeError
        worker.feed(bs)
    else:
        for bs in iter_reads(bin_istream, block_size):
            worker.feed(bs)
            if worker.done: break

    worker.close()
    result = worker.result
    return result
def file2maybe_encoding(bin_fin, block_size=BLOCK_SIZE):
    # (BinaryIO|bytes) -> Maybe str
    # seekable
    is_file = hasattr(bin_fin, 'read')
    if is_file:
        pos = bin_fin.tell()
        try:
            d = detect_encoding(bin_fin, block_size)
        finally:
            bin_fin.seek(pos)
    else:
        bs = bin_fin
        d = detect_encoding(bs, block_size)
    encoding = d['encoding']

    if encoding:
        try:
            if is_file:
                txt_fin = TextIOWrapper(bin_fin, encoding=encoding)
                try:
                    for _ in iter_reads(txt_fin, block_size): pass
                finally:
                    bin_fin.seek(pos)
            else:
                bs.decode(encoding)
        except UnicodeDecodeError:
            encoding = None
    return encoding

def _test():
    assert file2maybe_encoding(b'') is None
    assert file2maybe_encoding(BytesIO(b'')) is None
    assert file2maybe_encoding(b'abcd') == 'ascii'
    assert file2maybe_encoding(BytesIO(b'abcd')) == 'ascii'

#print(file2maybe_encoding('末一'.encode('gbk')))
#print('末一'.encode('gbk').decode('utf8'))
assert file2maybe_encoding('末一'.encode('gbk')) == 'utf-8'
#not good!!!!!!!!!!

_test()








