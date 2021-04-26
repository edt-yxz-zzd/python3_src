


r'''
seed.math.calc_hash_digest
from seed.math.calc_hash_digest import calc_SHA256__file

#'''

__all__ = '''
    calc_SHA256__file
    '''.split()


r'''
>>> import hashlib
>>> m = hashlib.sha256()
>>> m.update(b"Nobody inspects")
>>> m.update(b" the spammish repetition")
>>> m.digest()
b'\x03\x1e\xdd}Ae\x15\x93\xc5\xfe\\\x00o\xa5u+7\xfd\xdf\xf7\xbcN\x84:\xa6\xaf\x0c\x95\x0fK\x94\x06'
>>> m.digest_size
32
>>> m.block_size
64
#'''

import hashlib

_BLOCK_SIZE = 2**20 #1MB
def calc_SHA256__file(binary_ifile, /,*, hex:bool, upper:bool):
    m = hashlib.sha256()
    while 1:
        bs = binary_ifile.read(_BLOCK_SIZE)
        if not bs: break
        m.update(bs)
    if hex:
        digest_hex_str = m.hexdigest()
        if upper:
            digest_upper_hex_str = digest_hex_str.upper()
            xdigest = digest_upper_hex_str
        else:
            digest_lower_hex_str = digest_hex_str.lower()
            xdigest = digest_lower_hex_str
    else:
        digest_bytes = m.digest()
        xdigest = digest_bytes
    return xdigest

