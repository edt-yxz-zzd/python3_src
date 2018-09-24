
'''
cmd_call/decoded_cmd_call
    streams using PIPE
    will not output to stdout/stderr
basic_cmd_call/basic_decoded_cmd_call
    streams default to None
        will output to stdout/stderr
'''

__all__ = '''
    cmd_call
    decoded_cmd_call

    basic_cmd_call
    basic_decoded_cmd_call
'''.split()


r'''
#open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

subprocess.Popen(args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None, creationflags=0, restore_signals=True, start_new_session=False, pass_fds=(), *, encoding=None, errors=None)

bufsize
    - creating the stdin/stdout/stderr pipe file objects:
        open(..., buffering=bufsize, ...)
stdin, stdout, stderr
    # should be binary_stream??
    # can be text_stream!!
    - the executed program's standard input, standard output and standard error file handles, respectively.
        can be existing file objects

If encoding or errors are specified, or universal_newlines is true, the file objects stdin, stdout and stderr will be opened in text mode using the encoding and errors specified in the call or the defaults for io.TextIOWrapper.

For stdin, line ending characters '\n' in the input will be converted to the default line separator os.linesep. For stdout and stderr, all line endings in the output will be converted to '\n'. For more information see the documentation of the io.TextIOWrapper class when the newline argument to its constructor is None.

If text mode is not used, stdin, stdout and stderr will be opened as binary streams. No encoding or line ending conversion is performed.


'''


import cmd, sys, locale
import subprocess
from seed.lang.is_bytes_like_object import is_bytes_like_object

def cmd_call(cmd, *, input=None, timeout=None):
    # cmd :: String | [String]
    PIPE = subprocess.PIPE
    return basic_cmd_call(cmd, input=input, timeout=timeout
        , stdin=PIPE, stdout=PIPE, stderr=PIPE)
def basic_cmd_call(cmd, *, input=None, timeout=None
    , stdin=None, stdout=None, stderr=None):
    #assert type(cmd) is list
    #assert type(cmd) in (bytes, bytearray)
    if not (input is None or is_bytes_like_object(input)): raise TypeError

    with subprocess.Popen(cmd, stdin=stdin, stdout=stdout, stderr=stderr) as proc:
        try:
            outs, errs = proc.communicate(timeout=timeout, input=input)
            is_timeout = False
        except subprocess.TimeoutExpired:
            proc.kill()
            outs, errs = proc.communicate()
            is_timeout = True

        returncode = proc.returncode
    return outs, errs, returncode, is_timeout


def basic_decoded_cmd_call(cmd, *, input=None, timeout=None
    #, encoding=None
    , stdin=None, stdout=None, stderr=None):
    output = basic_cmd_call(cmd, input=input, timeout=timeout
                , stdin=stdin, stdout=stdout, stderr=stderr)
    return decode_communicate_output(output)
def decoded_cmd_call(cmd, *, input=None, timeout=None
    #, encoding=None
    ):
    output = cmd_call(cmd, input=input, timeout=timeout)
    return decode_communicate_output(output)



def decode_communicate_output(communicate_output):
    (outs, errs, returncode, is_timeout) = communicate_output
    outs = decode_bytes(outs, encoding=sys.stdout.encoding)
    errs = decode_bytes(errs, encoding=sys.stderr.encoding)
    #outs = decode_bytes(outs, encoding=sys.stdin.encoding)
    #errs = decode_bytes(errs, encoding=sys.stdin.encoding)
    #outs = decode_bytes(outs, encoding='gb18030')
    #errs = decode_bytes(errs, encoding='gb18030')
    return outs, errs, returncode, is_timeout
def decode_bytes(output, *, encoding):
    if isinstance(output, (bytes, bytearray)):
        if encoding is None:
            #encoding = sys.getfilesystemencoding()
            encoding = sys.stdout.encoding

        try:
            output = output.decode(encoding)
        except UnicodeDecodeError:
            encoding = locale.getpreferredencoding(False)
            try:
                output = output.decode(encoding)
            except UnicodeDecodeError:
                print(output)
                raise
    return output










