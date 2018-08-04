

__all__ = '''
    decoded_cmd_call
    cmd_call
'''.split()


import cmd, sys
import subprocess
from seed.lang.is_bytes_like_object import is_bytes_like_object

def cmd_call(cmd, input=None, timeout=None):
    #assert type(cmd) is list
    #assert type(cmd) in (bytes, bytearray)
    if not (input is None or is_bytes_like_object(input)): raise TypeError

    PIPE = subprocess.PIPE
    with subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE) as proc:
        try:
            outs, errs = proc.communicate(timeout=timeout, input=input)
            is_timeout = False
        except subprocess.TimeoutExpired:
            proc.kill()
            outs, errs = proc.communicate()
            is_timeout = True

        returncode = proc.returncode
    return outs, errs, returncode, is_timeout


def decoded_cmd_call(cmd, input=None, timeout=None,
                     *, encoding=None):
    outs, errs, returncode, is_timeout = cmd_call(cmd, input, timeout)
    outs = decode_bytes(outs, encoding)
    errs = decode_bytes(errs, encoding)
    return outs, errs, returncode, is_timeout
def decode_bytes(output, encoding):
    if isinstance(output, (bytes, bytearray)):
        encoding = sys.getfilesystemencoding() if encoding is None else encoding
        output = output.decode(encoding)
    return output










