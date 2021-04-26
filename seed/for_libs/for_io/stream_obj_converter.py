
r'''
seed.for_libs.for_io.stream_obj_converter
py -m seed.for_libs.for_io.stream_obj_converter

from seed.for_libs.for_io.stream_obj_converter import stream_obj2stream_type_name, raw_binary_stream_obj2buffered_binary_stream_obj, buffered_binary_stream_obj2text_stream_obj

from seed.for_libs.for_io.stream_obj_converter import stream_obj2stream_type_name, is_stream_text, is_stream_buffered_binary, is_stream_raw_binary, stream_obj2text_stream_obj, binary_stream_obj2text_stream_obj, buffered_binary_stream_obj2text_stream_obj, binary_stream_obj2buffered_binary_stream_obj, raw_binary_stream_obj2buffered_binary_stream_obj


#'''

import io

__all__ = '''
    stream_obj2stream_type_name
        is_stream_text
        is_stream_buffered_binary
        is_stream_raw_binary

    stream_obj2text_stream_obj
        binary_stream_obj2text_stream_obj
            buffered_binary_stream_obj2text_stream_obj
            binary_stream_obj2buffered_binary_stream_obj
                raw_binary_stream_obj2buffered_binary_stream_obj

    '''.split()


class Globals:
    r'''
    stream_type_name = ('RawBinaryStream' | 'BufferedBinaryStream' | 'TextStream')
    buffered_case = ('read' | 'write' | 'io')
    #'''
    stream_type_names = ('RawBinaryStream', 'BufferedBinaryStream', 'TextStream')
    buffered_cases = ('read', 'write', 'rw_seek')

def is_stream_text(stream_obj):
    return stream_obj2stream_type_name(stream_obj) == 'TextStream'
def is_stream_buffered_binary(stream_obj):
    return stream_obj2stream_type_name(stream_obj) == 'BufferedBinaryStream'
def is_stream_raw_binary(stream_obj):
    return stream_obj2stream_type_name(stream_obj) == 'RawBinaryStream'

def stream_obj2stream_type_name(stream_obj):
    r'''stream_obj -> stream_type_name
    stream_type_name = ('RawBinaryStream' | 'BufferedBinaryStream' | 'TextStream')

    ## attrs
    raw_binary_stream_obj.readall
    buffered_binary_stream_obj.read1/readinto1
    text_stream_obj:encoding/errors/newlines
    #'''
    stream_type_names = []
    ###
    if hasattr(stream_obj, 'readall'):
        stream_type_names.append('RawBinaryStream')
    ###
    if all(hasattr(stream_obj, nm) for nm in 'read1 readinto1'.split()):
        stream_type_names.append('BufferedBinaryStream')
    ###
    if all(hasattr(stream_obj, nm) for nm in 'encoding errors newlines'.split()):
        stream_type_names.append('TextStream')
    ###
    if 0:
        if not stream_type_names:
            print(stream_obj)
            print(isinstance(stream_obj, io.IOBase))
            print(isinstance(stream_obj, io.RawIOBase))
            print(dir(stream_obj))
            print(hasattr(stream_obj, 'readall'))
            print(hasattr(stream_obj, 'read1'))
            print(hasattr(stream_obj, 'encoding'))
            print(stream_obj.encoding)
    if not stream_type_names: raise TypeError('not stream_obj')
    if len(stream_type_names) > 1: raise Exception('unknown stream_obj: {stream_obj!r}')
    [stream_type_name] = stream_type_names
    return stream_type_name

def stream_obj2text_stream_obj(stream_obj, /,*, encoding, buffered_case, kwargs4buffered_binary_stream, kwargs4text_stream):
    stream_type_name = stream_obj2stream_type_name(stream_obj)
    if stream_type_name == 'TextStream':
        text_stream_obj = stream_obj
    else:
        binary_stream_obj = stream_obj
        text_stream_obj = binary_stream_obj2text_stream_obj(binary_stream_obj, encoding=encoding, buffered_case=buffered_case, kwargs4buffered_binary_stream=kwargs4buffered_binary_stream, kwargs4text_stream=kwargs4text_stream)

    return text_stream_obj

def binary_stream_obj2text_stream_obj(binary_stream_obj, /,*, encoding, buffered_case, kwargs4buffered_binary_stream, kwargs4text_stream):
    b2t = buffered_binary_stream_obj2text_stream_obj

    buffered = binary_stream_obj2buffered_binary_stream_obj(binary_stream_obj, buffered_case=buffered_case, **kwargs4buffered_binary_stream)

    text_stream_obj = b2t(buffered, encoding=encoding, **kwargs4text_stream)
    return text_stream_obj

def binary_stream_obj2buffered_binary_stream_obj(binary_stream_obj, /,*, buffered_case, **kwargs4buffered_binary_stream):
    r2b = raw_binary_stream_obj2buffered_binary_stream_obj

    stream_type_name = stream_obj2stream_type_name(binary_stream_obj)
    if stream_type_name == 'TextStream': raise TypeError
    else:
        if stream_type_name == 'BufferedBinaryStream':
            buffered = binary_stream_obj
        elif stream_type_name == 'RawBinaryStream':
            raw = binary_stream_obj
            buffered = r2b(raw, buffered_case=buffered_case, **kwargs4buffered_binary_stream)
        else:
            raise logic-err
        buffered_binary_stream_obj = buffered
    return buffered_binary_stream_obj


def buffered_binary_stream_obj2text_stream_obj(buffered_binary_stream_obj, /,*, encoding, **kwargs):
    if not stream_obj2stream_type_name(buffered_binary_stream_obj) == 'BufferedBinaryStream': raise TypeError

    text_stream_obj = io.TextIOWrapper(buffered_binary_stream_obj, encoding=encoding, **kwargs)
    return text_stream_obj

def raw_binary_stream_obj2buffered_binary_stream_obj(raw_binary_stream_obj, /,*, buffered_case:str, **kwargs):
    r'''
    buffered_case = ('read' | 'write' | 'rw_seek')
        ==>> io.BufferedReader/BufferedWriter/BufferedRandom
    #'''
    if type(buffered_case) is not str: raise TypeError
    if buffered_case not in ('read', 'write', 'rw_seek'): raise TypeError
    if not stream_obj2stream_type_name(raw_binary_stream_obj) == 'RawBinaryStream': raise TypeError

    if buffered_case == 'read':
        T = io.BufferedReader
    elif buffered_case == 'write':
        T = io.BufferedWriter
    elif buffered_case == 'rw_seek':
        T = io.BufferedRandom
    else:
        raise logic-err
    buffered_binary_stream_obj = T(raw_binary_stream_obj, **kwargs)
    return buffered_binary_stream_obj


def _t():
    import tempfile
    def mk_raw():
        return tempfile.TemporaryFile(buffering=0)
        return tempfile.SpooledTemporaryFile(buffering=0)
            #SpooledTemporaryFile is not stream_obj !!!
    raw = mk_raw()
    buffered = io.BytesIO()
    texted = io.StringIO()

    #stream_obj2stream_type_name
    assert is_stream_raw_binary(raw)
    assert is_stream_buffered_binary(buffered)
    assert is_stream_text(texted)

    # x2y
    encoding = 'utf8'
    for buffered_case in Globals.buffered_cases:
        #if buffered_case == 'write': continue
        #if buffered_case == 'rw_seek': continue
        #print(buffered_case)

        #raw_binary_stream_obj2buffered_binary_stream_obj
        assert is_stream_buffered_binary(raw_binary_stream_obj2buffered_binary_stream_obj(raw, buffered_case=buffered_case))
        raw = mk_raw()

        #binary_stream_obj2buffered_binary_stream_obj
        assert is_stream_buffered_binary(binary_stream_obj2buffered_binary_stream_obj(raw, buffered_case=buffered_case))
        raw = mk_raw()
        assert is_stream_buffered_binary(binary_stream_obj2buffered_binary_stream_obj(buffered, buffered_case=buffered_case))

        #buffered_binary_stream_obj2text_stream_obj
        assert is_stream_text(buffered_binary_stream_obj2text_stream_obj(buffered, encoding=encoding))
        buffered = io.BytesIO()

        #binary_stream_obj2text_stream_obj
        assert is_stream_text(binary_stream_obj2text_stream_obj(raw, encoding=encoding, buffered_case=buffered_case, kwargs4text_stream={}, kwargs4buffered_binary_stream={}))
        raw = mk_raw()
        assert is_stream_text(binary_stream_obj2text_stream_obj(buffered, encoding=encoding, buffered_case=buffered_case, kwargs4text_stream={}, kwargs4buffered_binary_stream={}))
        buffered = io.BytesIO()

        #stream_obj2text_stream_obj
        assert is_stream_text(stream_obj2text_stream_obj(raw, encoding=encoding, buffered_case=buffered_case, kwargs4text_stream={}, kwargs4buffered_binary_stream={}))
        raw = mk_raw()
        assert is_stream_text(stream_obj2text_stream_obj(buffered, encoding=encoding, buffered_case=buffered_case, kwargs4text_stream={}, kwargs4buffered_binary_stream={}))
        buffered = io.BytesIO()
        assert is_stream_text(stream_obj2text_stream_obj(texted, encoding=encoding, buffered_case=buffered_case, kwargs4text_stream={}, kwargs4buffered_binary_stream={}))
    raw.close()


if __name__ == '__main__':
    _t()


