
r'''
encrypt/decrypt by RC4
example:
    key = b'iiiiiiiii'
    clear_text = b'zzzzzzzzzzz'
    cipher_text = rc4(key, clear_text, decrypt=False)
it seems rc4 encrypt==decrypt!!
'''

from seed.exec.cmd_call import cmd_call
import subprocess, os.path, io
from base64 import b16encode, b16decode
def encodeToHex(bs:bytes)->str:
    # encode :: bytes -> str!!!!!!! not str -> bytes!!!
    # bytes is clear_text!!
    return b16encode(bs).decode('ascii')
def decodeFromHex(s:str)->bytes:
    assert len(s) & 1 == 0
    return b16decode(s.encode('ascii'))
def rc4_bat(key_text_pairs:[(bytes, bytes)], decrypt:bool)->[((bytes, bytes), bytes)]:
    # the decrypt flag is useless for RC4
    # decrypt != encrypt??
    # len(cipher_text) == len(clear_text)
    arg = 'decrypt' if decrypt else 'encrypt'
    curr_dir = os.path.dirname(__file__) # use as CLASSPATH for java
    CLASSPATH = curr_dir
    cmd = ['java', '-cp', CLASSPATH, 'subprog.RC4_bat', arg]

    key_text_pairs = [(key, text) for key, text in key_text_pairs]
    stdin = ''.join('{}\n{}\n'.format(encodeToHex(key), encodeToHex(text))
                    for key, text in key_text_pairs)
    #clear_text = subprocess.check_output(cmd, stdin=stdin)
    #               check_output require fileno!!
    outs, errs, returncode, is_timeout = \
        cmd_call(cmd, input=stdin.encode('ascii'))
    if (b'', 0, False) != (errs, returncode, is_timeout):
        print('rc4 fail:'
                '\n\t key_text_pairs:{}'
                '\n\t outs:{}'
                '\n\t errs:{}'
                '\n\t returncode:{}'
                '\n\t is_timeout:{}'
                .format(key_text_pairs
                        , outs, errs, returncode, is_timeout)
                )
        raise Exception('rc4 fail')
    outs = outs.decode('ascii')
    # assume to decrypt
    clear_text_lines = io.StringIO(outs)
    clear_text_ls = [decodeFromHex(line.rstrip())
                        for line in clear_text_lines]
    result = list(zip(key_text_pairs, clear_text_ls))
    assert all(len(cipher_text) == len(clear_text)
                for (key, cipher_text), clear_text in result)
    return result

def rc4(key:bytes, text:bytes, decrypt:bool)->bytes:
    # version 2
    [((_key, _text), result)] = rc4_bat([(key, text)], decrypt)
    return result
def _rc4_ver1(key:bytes, cipher_text_or_clear_text:bytes, decrypt:bool)->bytes:
    # version 1
    # decrypt != encrypt??
    # len(cipher_text) == len(clear_text)
    arg = 'decrypt' if decrypt else 'encrypt'
    # assume to decrypt
    cipher_text = cipher_text_or_clear_text
    L = len(cipher_text)
    curr_dir = os.path.dirname(__file__) # use as CLASSPATH for java
    CLASSPATH = curr_dir
    cmd = ['java', '-cp', CLASSPATH, 'subprog.RC4', arg]

    stdin = '{}\n{}\n'.format(encodeToHex(key), encodeToHex(cipher_text))
    #clear_text = subprocess.check_output(cmd, stdin=stdin)
    #               check_output require fileno!!
    outs, errs, returncode, is_timeout = \
        cmd_call(cmd, input=stdin.encode('ascii'))
    if (b'', 0, False) != (errs, returncode, is_timeout):
        print('rc4 fail:'
                '\n\t text:{}'
                '\n\t key:{}'
                '\n\t outs:{}'
                '\n\t errs:{}'
                '\n\t returncode:{}'
                '\n\t is_timeout:{}'
                .format(cipher_text, key
                        , outs, errs, returncode, is_timeout)
                )
        raise Exception('rc4 fail')
    outs = outs.decode('ascii')
    eol = outs[L*2:]
    clear_text = decodeFromHex(outs[:L*2])
    #print((eol, clear_text))
    assert not eol or eol.isspace()
    assert len(clear_text) == L
    return clear_text


if __name__ == '__main__':
    print(rc4(b'1122334455', b'2123', True))
    print(rc4(b'1122334455', b'2123', False))

