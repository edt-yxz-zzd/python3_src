
r'''
a simple encrypt/decrypt algo
email blog psw


input_charset - a set of allow input chars
output_charset - a set of allow output chars

len_input_charset
len_output_charset

encrypt :: [UInt x] -> [UInt len_input_charset] -> [UInt len_output_charset]
decrypt :: [UInt x] -> [UInt len_output_charset] -> [UInt len_input_charset]

changes:
    version1 -> version2:
        add uint2uint_by_mod
'''


__all__ = '''
    Crypt
    aCrypt
    '''.split()

import random
import string
from itertools import count
from operator import __add__, __sub__
from nn_ns.Bijection.BijectiveNumeration import \
    (bidigits2uint__little_endian
    ,uint2bidigits__little_endian
    )
from nn_ns.Bijection.IntegerBJ.UInt2UInt_by_mod import UInt2UInt_by_mod


class Bijections:
    @staticmethod
    def digits2uint(radix, digits, little_endian:bool):
        # Iter (UInt radix) -> UInt
        bidigits = list(d+1 for d in digits)
        if not little_endian:
            bidigits.reverse()
        return bidigits2uint__little_endian(radix, bidigits)

    @staticmethod
    def uint2digits(radix, uint, little_endian:bool):
        # UInt -> Iter (UInt radix)
        bidigits = uint2bidigits__little_endian(radix, uint)
        f = iter if little_endian else reversed
        return (bd-1 for bd in f(bidigits))

    @staticmethod
    def int2uint(i):
        # Int -> UInt
        if i < 0:
            u = -i-1
            u <<= 1
            u |= 1
        else:
            u = i << 1
        return u
    @staticmethod
    def uint2int(u):
        # UInt -> Int
        i = u >> 1
        if u&1:
            return -(i+1)
        else:
            return i
        pass


    @staticmethod
    def pad_uint(pad, uint):
        i = __class__.uint2int(uint)
        i += pad
        uint = __class__.int2uint(i)
        return uint

    @staticmethod
    def uint2uint_by_mod(odd_K, A, uint, backward:bool):
        bj = UInt2UInt_by_mod(odd_K, A)
        if backward:
            f = bj.typechecked_backward
        else:
            f = bj.typechecked_forward
        return f(uint)

def _test_Bijections():
    digits2uint = Bijections.digits2uint
    uint2digits = Bijections.uint2digits
    uint2int = Bijections.uint2int
    int2uint = Bijections.int2uint
    uint2uint_by_mod = Bijections.uint2uint_by_mod

    assert digits2uint(2, [], True) == 0
    assert digits2uint(2, [0], True) == 1
    assert digits2uint(2, [1], True) == 2
    assert digits2uint(2, [0,0], True) == 3
    assert digits2uint(2, [1,0], True) == 4
    assert digits2uint(2, [0,1], True) == 5
    assert digits2uint(2, [1,1], True) == 6
    assert digits2uint(2, [0,1], False) == 4

    assert list(uint2digits(2, 0, True)) == []
    assert list(uint2digits(2, 1, True)) == [0]
    assert list(uint2digits(2, 2, True)) == [1]
    assert list(uint2digits(2, 3, True)) == [0,0]
    assert list(uint2digits(2, 4, True)) == [1,0]
    assert list(uint2digits(2, 5, True)) == [0,1]
    assert list(uint2digits(2, 6, True)) == [1,1]
    assert list(uint2digits(2, 5, False)) == [1,0]



    assert uint2int(0) == 0
    assert uint2int(1) == -1
    assert uint2int(2) == 1
    assert uint2int(3) == -2
    assert uint2int(4) == 2

    assert int2uint(-2) == 3
    assert int2uint(-1) == 1
    assert int2uint(0) == 0
    assert int2uint(1) == 2
    assert int2uint(2) == 4


    assert uint2uint_by_mod(3, 5, 23, False) == 26
    assert uint2uint_by_mod(3, 5, 26, True) == 23
    assert uint2uint_by_mod(3, 5, 0, False) == 0
    assert uint2uint_by_mod(3, 5, 0, True) == 0
    assert uint2uint_by_mod(3, 5, 1, False) == 1
    assert uint2uint_by_mod(3, 5, 1, True) == 1
_test_Bijections()
del _test_Bijections


##########################################

#ciphertext
#message = cleartext
class CryptPrime:
    # for [uint]
    PAD = 42621823628496
    K = -365
    A = 2018010120180801
    def __init__(self, len_input_charset, len_output_charset, len_psw_charset):
        self.len_input_charset = len_input_charset
        self.len_output_charset = len_output_charset
        self.len_psw_charset = len_psw_charset

    def iter_infinite_psw(self, psw):
        if len(psw) == 0: raise TypeError
        L = self.len_psw_charset
        for i in count(0):
            for ch in psw:
                assert 0 <= ch < L
                yield (ch + i)%L
        pass
    def iter_message_with_psw(self, psw, message, add:bool):
        L = self.len_input_charset
        f = __add__ if add else __sub__
        for m, c in zip(message, self.iter_infinite_psw(psw)):
            assert 0 <= m < L
            yield f(m, c)%L
        pass


    def encrypt(self, psw, message):
        PAD = __class__.PAD
        K = __class__.K
        A = __class__.A

        radixI = self.len_input_charset
        digitsI = self.iter_message_with_psw(psw, message, True)
        #[*digitsI] = digitsI

        uintI = Bijections.digits2uint(radixI, digitsI, True)
        uintM = Bijections.pad_uint(PAD, uintI)
        uintO = Bijections.uint2uint_by_mod(K, A, uintM, False)

        radixO = self.len_output_charset
        digitsO = Bijections.uint2digits(radixO, uintO, False)
        #[*digitsO] = digitsO
        ciphertext = digitsO

        if 0 and __debug__:
            print(uintI, uintO)
            print(digitsI)
            print(digitsO)
        return iter(ciphertext)

    def decrypt(self, psw, ciphertext):
        PAD = __class__.PAD
        K = __class__.K
        A = __class__.A

        digitsO = ciphertext
        #[*digitsO] = digitsO
        radixO = self.len_output_charset
        uintO = Bijections.digits2uint(radixO, digitsO, False)
        uintM = Bijections.uint2uint_by_mod(K, A, uintO, True)
        uintI = Bijections.pad_uint(-PAD, uintM)

        radixI = self.len_input_charset
        digitsI = Bijections.uint2digits(radixI, uintI, True)
        #[*digitsI] = digitsI
        #bug:message = self.iter_message_with_psw(psw, digitsI, True)
        message = self.iter_message_with_psw(psw, digitsI, False)
        if 0 and __debug__:
            print(uintI, uintO)
            print(digitsI)
            print(digitsO)
        return iter(message)

def chars2maps(chars):
    chars = set(chars)
    chars = sorted(chars)
    assert all(len(ch) == 1 for ch in chars)
    idx2char = ''.join(chars)
    char2idx = {ch:i for i,ch in enumerate(idx2char)}
    return idx2char, char2idx
def str2iter_idc(char2idx, s):
    for ch in s:
        yield char2idx[ch]
    pass
def str2idc(char2idx, s):
    return list(str2iter_idc(char2idx, s))
def idc2iter_str(idx2char, idc):
    for idx in idc:
        yield idx2char[idx]
    pass
def idc2str(idx2char, idc):
    return ''.join(idc2iter_str(idx2char, idc))

def random_split(seq, min_len, upper_len):
    words = []
    L = len(seq)
    i = 0
    while i < L:
        j = random.randrange(min_len, upper_len)
        assert j > 0
        j += i
        words.append(seq[i:j])
        i = j
    return words

class Crypt:
    # for [char]
    def __init__(self, input_chars, output_chars, psw_chars):
        idx2charI, char2idxI = chars2maps(input_chars)
        idx2charO, char2idxO = chars2maps(output_chars)
        idx2charP, char2idxP = chars2maps(psw_chars) # e.g. xdigit [0-9A-F]
        worker = CryptPrime(len(idx2charI), len(idx2charO), len(idx2charP))
        if not idx2charI: raise TypeError
        if not idx2charO: raise TypeError
        if 1 != len(idx2charO.split()): raise TypeError

        self.idx2charI, self.char2idxI = idx2charI, char2idxI
        self.idx2charO, self.char2idxO = idx2charO, char2idxO
        self.idx2charP, self.char2idxP = idx2charP, char2idxP
        self.worker = worker

    def encrypt(self, psw, message):
        if not all(ch in self.char2idxP for ch in psw): raise TypeError
        if not all(ch in self.char2idxI for ch in message): raise TypeError

        i_psw = str2idc(self.char2idxP, psw)
        i_message = str2iter_idc(self.char2idxI, message)
        #[*i_message] = i_message
        i_ciphertext = self.worker.encrypt(i_psw, i_message)
        #[*i_ciphertext] = i_ciphertext
        ciphertext = idc2str(self.idx2charO, i_ciphertext)

        # insert ' ' and '\n'
        words = random_split(ciphertext, 1, 8)
        lines = random_split(words, 1, 8)
        lines = '\n'.join(' '.join(words) for words in lines)
        ciphertext = lines

        if 0 and __debug__:
            print('encrypt')
            print(i_message)
            print(i_ciphertext)
        return ciphertext
    def decrypt(self, psw, ciphertext):
        if not all(ch in self.char2idxP for ch in psw): raise TypeError

        # remove any spaces (include ' ' and '\n')
        ciphertext = ''.join(ciphertext.split())
        if not all(ch in self.char2idxO for ch in ciphertext): raise TypeError

        i_psw = str2idc(self.char2idxP, psw)
        i_ciphertext = str2iter_idc(self.char2idxO, ciphertext)
        #[*i_ciphertext] = i_ciphertext
        i_message = self.worker.decrypt(i_psw, i_ciphertext)
        #[*i_message] = i_message
        message = idc2str(self.idx2charI, i_message)

        if 0 and __debug__:
            print('decrypt')
            print(i_message)
            print(i_ciphertext)
        return message

def enum_chars(min, max):
    min = ord(min)
    max = ord(max)
    return ''.join(map(chr, range(min, max+1)))
def remove_spaces(s):
    return ''.join(s.split())
def remove_chars(s, dels):
    return ''.join(ch for ch in s if ch not in dels)

class Data:
    char_09 = enum_chars('0', '9') # string.digits
    char_af = enum_chars('a', 'f')
    char_az = enum_chars('a', 'z')
    char_AZ = enum_chars('A', 'Z')
    char_ascii = enum_chars('\0', '\x7f')
    char_ascii_printable = string.printable
    char_ascii_printable_nonspace = remove_spaces(char_ascii_printable)

    psw_chars = char_09 + char_af
    input_chars = char_ascii_printable_nonspace + ' \n'
    output_chars = char_ascii_printable_nonspace.replace(char_AZ, '')
    output_chars = remove_chars(output_chars, '<>&;?"\'`\\/')
    output_chars = remove_chars(output_chars, '<>&;?"\'`\\/-')
    r'''
        to avoid:
            * hyper_link: /
            * html: <>&;
            * unknown surrogate escape: ?
            * left-right quot: "'
            * -- become one char: -
            ......
            * ' 7x6 ' may become ' 7\xd76 '
                !!!!!!!!!!!WTF!!!!!!!!!
        should use <pre>
    '''
    output_chars = char_09 + char_az

    # assume using output of md5/sha1/sha256 as psw
    assert psw_chars == '0123456789abcdef'
    assert len(psw_chars) == 16 == len(set(psw_chars))
    #print(repr(input_chars))
    #print(repr(output_chars))
    #print(len(input_chars))
    #print(len(output_chars))
    assert len(input_chars) == 96
    #assert len(output_chars) == 58
    assert len(output_chars) == 36
    assert input_chars == '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \n'
    #assert output_chars == '0123456789abcdefghijklmnopqrstuvwxyz!#$%()*+,-.:=@[]^_{|}~'
    assert output_chars == '0123456789abcdefghijklmnopqrstuvwxyz'


aCrypt = Crypt(Data.input_chars, Data.output_chars, Data.psw_chars)
def _test_Crypt():
    psw = 'af23546b32'
    for message in ['', '1', 'a fd\na3l4t a{}']:
        #print('\n'*3+'-------------')
        ciphertext = aCrypt.encrypt(psw, message)
        message2 = aCrypt.decrypt(psw, ciphertext)
        if 0 and __debug__:
            print(ciphertext)
            print(repr(ciphertext))
            print(repr(message))
            print(repr(message2))
        assert message == message2
_test_Crypt()
del _test_Crypt




###############################################

def main(argv=None):
    import argparse
    from seed.io.may_open import may_open_stdin, may_open_stdout

    encoding = 'ascii'

    parser = argparse.ArgumentParser(
        description='simple encrypt ascii text'
        , epilog=r'only " " and "\n" are allowed, other control/whitespace should not occur in input text'
        #, formatter_class=argparse.RawDescriptionHelpFormatter
        )
    #parser.add_argument('-e', '--encoding', type=str, default='utf8', help='input/output file encoding')
    parser.add_argument('cmd', type=str, choices='encrypt decrypt'.split()
                        , help='encrypt/decrypt - treat input as cleartext/ciphertext')
    parser.add_argument('psw', type=str
                        , help='password: regex = [0-9a-f]*')
    parser.add_argument('-i', '--input', type=str, default = None
                        , help='input file path')
    parser.add_argument('-o', '--output', type=str, default = None
                        , help='output file path')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')



    args = parser.parse_args(argv)
    psw = args.psw
    if not all(ch in aCrypt.char2idxP for ch in psw): raise TypeError
    omode = 'wt' if args.force else 'xt'
    does_encrypt = args.cmd == 'encrypt'

    may_ifname = args.input
    with may_open_stdin(may_ifname, 'rt', encoding=encoding) as fin:
        input_text = ''.join(fin)

    if does_encrypt:
        message = input_text
        ciphertext = aCrypt.encrypt(psw, message)
        output_text = ciphertext
    else:
        ciphertext = input_text
        message = aCrypt.decrypt(psw, ciphertext)
        output_text = message

    may_ofname = args.output
    with may_open_stdout(may_ofname, omode, encoding=encoding) as fout:
        fout.write(output_text)

    parser.exit(0)
    return 0



if __name__ == "__main__":
    main()

