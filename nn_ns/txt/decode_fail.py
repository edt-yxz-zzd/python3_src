


import codecs
import collections # deque


class DecodeError(ValueError):pass

def decode_01byte(decoder, b, ls):
    assert len(b) <= 1
    try:
        c = decoder.decode(b, not b)
    except ValueError as err:
        unused, _ = decoder.getstate()
        return True, len(unused) # failed, len
    
    assert len(c) <= 1
    if c:
        ls.append(c)
        
    return False, c # not failed, char

def decode_fail(fname, encoding, nchar=-1):
    assert nchar >= -1

    maxlen = None if nchar == -1 else nchar
    deque = collections.deque([], maxlen)
    n = 0
    '''
    with open(fname, 'r', encoding=encoding) as fin:
        err = None
        while fin:
            try:
                pos = fin.tell()
                c = fin.read(1)
            except ValueError as err:
                print('pos = {}, n = {}'.format(pos, n))
                break
            else:
                n += 1
                deque.append(c)

        
        pos = fin.tell()
        assert err is None or -1 != str(err).find(str(pos))
        
    txt = ''.join(deque)
    assert nchar == -1 or len(txt) <= nchar
    
    return pos, txt'''



    
    '''
        stream = decoder('strict')
        txt = stream.decode(fin)
        if nchar >= 0:
            txt = txt[len(txt)-nchar : len(txt)]
            
        pos = fin.tell() if fin.seekable() else None

        return pos, txt
    pass'''

    decoder = codecs.getincrementaldecoder(encoding)
    with open(fname, 'rb') as fin:
        stream = decoder('strict')
        while True:
            b = fin.read(1)
            #error: assert b
            failed, L = decode_01byte(stream, b, deque)
            if failed or not b:
                pos = fin.tell() - (L if failed else 0)
                break
                
    txt = ''.join(deque)
    assert nchar == -1 or len(txt) <= nchar

    return pos, txt


'''
    reader = codecs.getreader(encoding)
    with open(fname, 'rb') as fin:
        stream = reader(fin, 'strict')
        txt = stream.read()
        if nchar >= 0:
            txt = txt[len(txt)-nchar : len(txt)]
            
        pos = fin.tell() if fin.seekable() else None

        return pos, txt
    pass
'''

def main(args = None):
    import argparse, sys

    parser = argparse.ArgumentParser(description =
            'get the position and the ahead charaters of '\
            'the decoding-failed place.')
    parser.add_argument('fname', type=str,
                        help='file name to decode')
    
    
    parser.add_argument('encoding', type=str,
                        help='encoding')
    
    parser.add_argument('nchar', type=int,
                        nargs='?', default=None,
                        help='number of ahead charaters to print.'\
                        'None - return position; -1 - all txt.')


    args = parser.parse_args(args)
    nchar = args.nchar
    if nchar == None:
        nchar = 0

    pos, txt = decode_fail(args.fname, args.encoding, nchar)

    if args.nchar == None:
        r = pos
    else:
        r = txt
    print(r)
    return 0
    


if __name__ == "__main__":
    main()


