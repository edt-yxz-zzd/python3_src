


import hashlib
import codecs


def usrhash(web_site, usr_account, salt):
    hidden_salt = '1, 1, 1, 0, -1, 0, 1, 0, -1, 0, 5, 0, -691'
    # A164555 Numerators of the "original" Bernoulli numbers
    m = hashlib.sha512()
    inputs = [web_site, usr_account, salt, hidden_salt]
    string = ';'.join(inputs)
    bs = string.encode('utf8')
    m.update(bs)
    return m.hexdigest()
    return m.digest()

#rint(usrhash('a', 'b', 'c'))


def main(argv=None):
    import argparse

if '__main__' == __name__:
    import sys
    args = sys.argv[1:]
    print(args)
    web_site, usr_account, salt = args
    h = usrhash(web_site, usr_account, salt)
    print(h)
    print(h[:9])


