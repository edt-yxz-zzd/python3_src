
r"""
f.seek(chunk_size * offset);
ValueError: cannot fit 'int' into an offset-sized integer
    NOTE:
        file_byte_offset = begin*chunk_size

see:hexdump
    /data/data/com.termux/files/usr/bin/hexdump
[
$ hexdump --help

Usage:
 hexdump [options] <file>...

Display file contents in hexadecimal, decimal, octal, or ascii.

Options:
 -b, --one-byte-octal      one-byte octal display
 -c, --one-byte-char       one-byte character display
 -C, --canonical           canonical hex+ASCII display
 -d, --two-bytes-decimal   two-byte decimal display
 -o, --two-bytes-octal     two-byte octal display
 -x, --two-bytes-hex       two-byte hexadecimal display
 -L, --color[=<mode>]      interpret color formatting specifiers
                             colors are enabled by default
 -e, --format <format>     format string to be used for displaying data
 -f, --format-file <file>  file that contains format strings
 -n, --length <length>     interpret only length bytes of input
 -s, --skip <offset>       skip offset bytes from the beginning
 -v, --no-squeezing        output identical lines

 -h, --help                display this help
 -V, --version             display version

Arguments:
 <length> and <offset> arguments may be followed by the suffixes for
   GiB, TiB, PiB, EiB, ZiB, and YiB (the "iB" is optional)

For more details see hexdump(1).
]
#"""



# see a piece in a big binary file
def get_file_chunks(fname, chunk_size = 16, offset = 0, num_chunks = 1):
    assert chunk_size > 0 and num_chunks > 0 and offset >= 0
    
    with open(fname, 'rb') as f:
        f.seek(chunk_size * offset);
        chunks = list(filter(None,
                             (f.read(chunk_size) for _ in range(num_chunks))))
        return chunks


def file_binary_compare(fname1, fname2, range1 = (), range2 = (), chunk_size = 2**20):
    # see: filecmp
    def calc_range(fname, rng):
        
        import os
        size = os.path.getsize(fname)
        if len(rng) == 0:
            rng = (0, size)
        elif len(rng) == 1:
            rng = (rng[0], size)

        #############
        if len(rng) == 2:
            rng = list(rng)
            if rng[1] > size:
                rng[1] = size
            elif rng[1] < 0:
                rng[1] += size
                
            if rng[0] > rng[1]:
                rng = (0, 0)
            elif rng[0] < 0:
                rng[0] += size

            assert 0 <= rng[0] <= rng[1]
            return rng
        else:
            # error!!!
            pass

    def get_diff_idx(bytes1, bytes2):
        assert len(bytes1) == len(bytes2)
        L = len(bytes1)
        assert L > 0
        if L == 1:
            assert bytes1[0] != bytes2[0]
            return 0
        M = L // 2
        left1 = bytes1[0:M]
        left2 = bytes2[0:M]
        if left1 != left2:
            return get_diff_idx(left1, left2)
        return M + get_diff_idx(bytes1[M:], bytes2[M:])

    #import filecmp
    #if filecmp.cmp(f1, f2)
    with open(fname1, 'rb') as f1, open(fname2, 'rb') as f2:
        rng1 = calc_range(fname1, range1)
        rng2 = calc_range(fname2, range2)
        size1 = rng1[1] - rng1[0]
        size2 = rng2[1] - rng2[0]
        if size1 > size2:
            size = size2
        else:
            size = size1
        f1.seek(rng1[0])
        f2.seek(rng2[0])
        same = True
        index = None
        i = -chunk_size
        for i in range(0, size - chunk_size, chunk_size):
            b1 = f1.read(chunk_size)
            b2 = f2.read(chunk_size)
            if b1 != b2:
                same = False
                break
        else:
            i += chunk_size
            chunk_size = size - i
            b1 = f1.read(chunk_size)
            b2 = f2.read(chunk_size)
            same = (b1 == b2)

        if not same:
            index = i + get_diff_idx(b1, b2)

        return (same, index)




def t6():
    p = r'C:\TDDOWNLOAD/[ztjfate@1123456][110225][FrontWing]グリザイアの果実.part3'
    p1 = p + r'.rar_'
    p2 = p + r'(1).rar'
    import filecmp
    return filecmp.cmp(p1, p2)





def t5():
    p1 = r'C:\game\マブラヴオルタネイティヴ14/'
    p2 = r'G:/'
    fn = 'alternative14.rio'
    s1 = ''
    s2 = '.002'
    s3 = '.003'
    import filecmp
    def cmp(s):
        return filecmp.cmp(p1+fn+s, p2+fn+s)
    return (cmp(s1), cmp(s2), cmp(s3))


def t4():
    f1 = r'C:\game\マブラヴ14/' + r'muvluv14.rio.002'
    f2 = r'G:/' + r'muvluv14.rio.002'
    import filecmp
    return filecmp.cmp(f1, f2)







def t3():
    paths = [r'C:\game\マブラヴ14/', r'G:/']
    fnames = [r'muvluv14.rio', r'muvluv14.rio.002']
    for i in range(len(fnames)):
        print(fnames[i], file_binary_compare(paths[0]+fnames[i], paths[1]+fnames[i]))

def t2(chunk_size = 256, offset = 0):
    import os
    paths = [r'C:\game\マブラヴ14/', r'G:/']
    fnames = [r'muvluv14.rio', r'muvluv14.rio.002']
    for fn in fnames:
        chunks = []
        for path in paths:
            chunks.append(get_file_chunks(path+fn, chunk_size, offset))
        print(fn)
        print(chunks)




def t1():
    import os
    path = r'C:\game\WHITE_ALBUM2_-introductory_chapter-\WHITE ALBUM2 -introductory chapter-/'
    fn = r'char.pak'
    ls = os.listdir(path)
    fs = [ fn for fn in ls if fn[-4:].lower() == '.pak' and os.path.isfile(os.path.join( path, fn))]
    hs = [(get_file_chunks(path+fn), fn) for fn in fs]
    hs.sort()
    for h in hs:
        print(h)
        



def main(args = None):
    import argparse, sys
    #from sand import glob1
    from seed.filesys.glob1 import glob1
    from pprint import pprint
    from seed.for_libs.for_argparse import str2pint, str2uint

    parser = argparse.ArgumentParser(
        description='view snippet content of given binary file')
    parser.add_argument('fname', type=str, \
                        help='path pattern of binary file to browse')
    parser.add_argument('-c', '--chunk_size', type=str2pint, default=16, \
                        help='number of bytes per chunk')
    parser.add_argument('-n', '--num_chunks', type=str2pint, default=1, \
                        help='max number of chunks')
    parser.add_argument('-b', '--begin', type=str2uint, default=0,\
                        help='begin index of chunks in file; unit:chunk that is chunk_size bytes.')
    


    args = parser.parse_args(args)
    fname = glob1(args.fname)
    chunks = get_file_chunks(fname,
                              chunk_size = args.chunk_size,
                              offset = args.begin,
                              num_chunks = args.num_chunks)
    pprint(chunks)
    

    parser.exit(0)
    raise logic-error

if __name__ == "__main__":
    main()


