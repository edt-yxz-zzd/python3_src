

r'''
to extract WA2 : kcap / lac / tga files


kcap file:
    head:
        const char[4] = "KCAP" ; 
        uint32le ??;
        uint32le ??;
        uint32le num_entries;
    entry{
        uint32le is_compressed; # none or lzss
        char fname[24];
        uint32le ??;
        uint32le ??;
        uint32le offset;
        uint32le length;
        
        }[num_entries];
    compressed_subfiles[num_entries];
lac file:
    head:
        const char[4] = "LAC" ;
        uint32le num_entries;
    entry{
        char fname[31];
        char is_compressed; # none or lzss
        uint32le offset;
        uint32le length;
        
        }[num_entries];
    compressed_subfiles[num_entries];
        
    

tga file:
    uint32le compressed_size;
    uint32le original_size;
    byte compressed_data[compressed_size];


i.e.
    C:/game/WHITE ALBUM2 -introductory chapter-/tmp/tv100100.tga

'''



from unlzss import unlzss

#class EOFError(ValueError):pass
class FormatError(ValueError):pass
def fast_is_BinaryIO(fin):
    return hasattr(fin, 'readinto')

def read_bytes(file, size):
    assert size >= 0
    bs = file.read(size)
    if len(bs) != size:
        raise EOFError
    return bs
    
def assert_bytes(file, const_bytes):
    if type(const_bytes) is not bytes:
        raise TypeError('not bytes')
    sz = len(const_bytes)
    bs = read_bytes(file, sz)
    if type(bs) is not bytes:
        raise TypeError('file is not BinaryIO')
    if bs != const_bytes:
        raise FormatError('assert_bytes : const_bytes != bytes read from file')
    
def read_uint32le(file):
    bs = read_bytes(file, 4)
    i = int.from_bytes(bs, 'little')
    assert i >= 0
    return i

def seekhold_read(file, pos, size):
    pos0 = file.tell()
    try:
        file.seek(pos)
        return read_bytes(file, size)
    finally:
        file.seek(pos0)



##################### tga_file ###########################

def decode_tga_file(fin):
    assert fast_is_BinaryIO(fin)
    
    sz = read_uint32le(fin)
    org_sz = read_uint32le(fin)
    compressed_data = read_bytes(fin, sz)
    data = unlzss(compressed_data)
    if len(data) != org_sz:
        raise FormatError('uncompressed data size != original size')
    return data


##################### kcap_file ###########################

def decode_kcap_file__head(fin):
    assert fast_is_BinaryIO(fin)

    label = b"KCAP"
    assert_bytes(fin, label)
    _1, _2, num_entries = [read_uint32le(fin) for _ in range(3)]
    return label, _1, _2, num_entries
def decode_kcap_file__entry(fin):
    is_compressed = read_uint32le(fin)
    fname = read_bytes(fin, 24) # not str !!! encoding??
    _1, _2, pos, size = [read_uint32le(fin) for _ in range(4)]
    return is_compressed, fname, _1, _2, pos, size
def iter_decode_kcap_file__entries(fin, num_entries):
    for _ in range(num_entries):
        entry = decode_kcap_file__entry(fin)
        pos = fin.tell()
        yield entry
        fin.seek(pos)


def iter_decode_kcap_file__subfiles(fin, iter_entries):
    '[(fname::bytes, uncompressed_content::bytes)]'

    for entry in iter_entries:
        is_compressed, fname, _1, _2, pos, size = entry
        bs = seekhold_read(fin, pos, size)
        if is_compressed:
            bs = unlzss(bs)
        yield fname, bs


def iter_kcap_file(fin, pred=lambda fname, compressed_size:True, encoding='ascii'):
    '''[(fname::str, content::bytes)]

pred(fname::str, compressed_size)'''
    
    label, _1, _2, num_entries = decode_kcap_file__head(fin)
    def filter_entries():
        for entry in iter_decode_kcap_file__entries(fin, num_entries):
            is_compressed, fname, _1, _2, pos, compressed_size = entry
            fname = fname.decode(encoding)
            if pred(fname, compressed_size):
                # fname updated
                yield is_compressed, fname, _1, _2, pos, compressed_size

    return iter_decode_kcap_file__subfiles(fin, filter_entries())


##################### lac_file ###########################

def decode_lac_file__head(fin):
    assert fast_is_BinaryIO(fin)

    label = b"LAC"
    assert_bytes(fin, label)
    num_entries = read_uint32le(fin)
    return label, num_entries
def decode_lac_file__entry(fin):
    fname = read_bytes(fin, 31) # not str !!! encoding??
    is_compressed, = read_bytes(fin, 1)
    pos, size = [read_uint32le(fin) for _ in range(2)]
    return fname, is_compressed, pos, size
def iter_decode_lac_file__entries(fin, num_entries):
    for _ in range(num_entries):
        entry = decode_lac_file__entry(fin)
        pos = fin.tell()
        yield entry
        fin.seek(pos)



def iter_decode_lac_file__subfiles(fin, iter_entries):
    '[(fname::bytes, uncompressed_content::bytes)]'

    for entry in iter_entries:
        fname, is_compressed, pos, size = entry
        bs = seekhold_read(fin, pos, size)
        if is_compressed:
            bs = unlzss(bs)
        yield fname, bs


def iter_lac_file(fin, pred=lambda fname, compressed_size:True, encoding='ascii'):
    '''[(fname::str, content::bytes)]

pred(fname::str, compressed_size)'''
    
    label, num_entries = decode_lac_file__head(fin)
    def filter_entries():
        for entry in iter_decode_lac_file__entries(fin, num_entries):
            fname, is_compressed, pos, compressed_size = entry
            fname = fname.decode(encoding)
            if pred(fname, compressed_size):
                # fname updated
                yield fname, is_compressed, pos, compressed_size

    return iter_decode_lac_file__subfiles(fin, filter_entries())


###########################################

def extract_xxx_file(fname, directory, iter_file):
    'iter_file::file->[(subfname, content)]'
    with open(fname, 'rb') as fin:
        for subfname, data in iter_f(fin):
            path = os.path.join(directory, subfname)
            with open(path, 'xb') as fout:
                fout.write(data)

def extract_lac_file(fname, directory):
    return extract_xxx_file(fname, directory, iter_lac_file)
def extract_kcap_file(fname, directory):
    return extract_xxx_file(fname, directory, iter_kcap_file)







