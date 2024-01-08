r'''
e ../../python3_src/seed/io/may_open.py

[[
encoding.1
encoding.2
xencoding
may_encoding
===
see:
    view ../../python3_src/seed/io/make_mode_ex4open.py
===
for may_open*():
    encoding :: may str
        #vs:below:encoding :: nonempty_str

===
for open4*():
    xencoding = nonencoding | encoding
    may_encoding = None | encoding

    nonencoding = '' | None | False
    encoding :: nonempty_str
===
]]



[[
may_smay_newline
    <==> open:kwarg:newline
===
    view ../../python3_src/seed/io/iter_line_contents__ver2.py
    def iter_line_contents_ex__file_(ifile, /, *, newlines__or__may_smay_newline, without_last_line_if_empty):
===
translated_or_not: read()
    * translated:
        * None:
            ('\r', '\n', '\r\n') --> '\n'
    * not translated:
        * '':
            ('\r', '\n', '\r\n') --> ('\r', '\n', '\r\n')
        * '\r':
            '\r' --> '\r'
        * '\n':
            '\n' --> '\n'
        * '\r\n':
            '\r\n' --> '\r\n'
===
translated_or_not: write()
    * translated:
        * None:
            '\n' --> os.linesep
        * '\r':
            '\n' --> '\r'
        * '\r\n':
            '\n' --> '\r\n'
    * not translated:
        * '':
            ('\r', '\n', '\r\n') --> ('\r', '\n', '\r\n')
        * '\n':
            '\n' --> '\n'
===
]]




seed.io.may_open
py -m nn_ns.app.debug_cmd   seed.io.may_open -x

from seed.io.may_open import may_open, may_open_stdin, may_open_stdout, may_open_stderr


from seed.io.may_open import open4w, open4w_err, open4r
#def open4w(may_opath, /, *, force, xencoding):
#def open4r(may_ipath, /, *, xencoding):

from seed.io.may_open import open4wt, open4wt_err, open4rt
#def open4wt(may_opath, /, *, force, encoding):
#def open4rt(may_ipath, /, *, encoding):

from seed.io.may_open import check_encoding


from seed.io.make_mode_ex4open import is_binary_mode5xencoding, xencoding2may_encoding, mk_mode_ex4open4w, mk_mode_ex4open4r


#'''

__all__ = r'''
may_open
    may_open_stdin
    may_open_stdout
    may_open_stderr



open4w
open4w_err
open4r

check_encoding
open4wt
open4wt_err
open4rt

'''.split()#'''

from seed.io.make_mode_ex4open import is_binary_mode5xencoding, xencoding2may_encoding, mk_mode_ex4open4w, mk_mode_ex4open4r
from seed.tiny import with_if
import sys

def may_open(fdefault, may_file, mode, /, *, encoding, **kwargs):
    # should be used with "with"
    return with_if(may_file is not None
        , lambda:open(may_file, mode, encoding=encoding, **kwargs)
        , fdefault
        )
def may_open_stdin(may_file, mode, /, *, encoding, **kwargs):
    # should be used with "with"
    return may_open(
        (lambda:sys.stdin.buffer) if 'b' in mode else (lambda:sys.stdin)
        , may_file, mode, encoding=encoding, **kwargs)
def may_open_stdout(may_file, mode, /, *, encoding, **kwargs):
    # should be used with "with"
    return may_open(
        (lambda:sys.stdout.buffer) if 'b' in mode else (lambda:sys.stdout)
        , may_file, mode, encoding=encoding, **kwargs)
def may_open_stderr(may_file, mode, /, *, encoding, **kwargs):
    # should be used with "with"
    return may_open(
        (lambda:sys.stderr.buffer) if 'b' in mode else (lambda:sys.stderr)
        , may_file, mode, encoding=encoding, **kwargs)






def open4w(may_opath, /, *, force, xencoding, **kwargs):
    (mode, may_encoding) = mk_mode_ex4open4w(force=force, xencoding=xencoding)
    return may_open_stdout(may_opath, mode, encoding=may_encoding, **kwargs)
def open4w_err(may_opath, /, *, force, xencoding, **kwargs):
    (mode, may_encoding) = mk_mode_ex4open4w(force=force, xencoding=xencoding)
    return may_open_stderr(may_opath, mode, encoding=may_encoding, **kwargs)
def open4r(may_ipath, /, *, xencoding, **kwargs):
    (mode, may_encoding) = mk_mode_ex4open4r(xencoding=xencoding)
    return may_open_stdin(may_ipath, mode, encoding=may_encoding, **kwargs)







def check_encoding(encoding, /):
    if not (type(encoding) is str and encoding): raise TypeError(f'not nonempty str: {type(encoding)}')

default_may_smay_newline4read = ''
default_may_smay_newline4write = ''

def open4wt(may_opath, /, *, force, encoding, may_smay_newline=default_may_smay_newline4write, **kwargs):
    check_encoding(encoding)
    return open4w(may_opath, force=force, xencoding=encoding, newline=may_smay_newline, **kwargs)
def open4wt_err(may_opath, /, *, force, encoding, may_smay_newline=default_may_smay_newline4write):
    check_encoding(encoding)
    return open4w_err(may_opath, force=force, xencoding=encoding, newline=may_smay_newline, **kwargs)
def open4rt(may_ipath, /, *, encoding, may_smay_newline=default_may_smay_newline4read, **kwargs):
    check_encoding(encoding)
    return open4r(may_ipath, xencoding=encoding, newline=may_smay_newline, **kwargs)





from seed.io.may_open import may_open, may_open_stdin, may_open_stdout, may_open_stderr


from seed.io.may_open import open4w, open4w_err, open4r
from seed.io.may_open import open4wt, open4wt_err, open4rt

from seed.io.may_open import check_encoding
from seed.io.may_open import *



