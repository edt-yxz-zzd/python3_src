#__all__:goto
r'''[[[
e ../../python3_src/seed/io/savefile__str_tuple.py

!!!only read/write@[`newline` in ('','\n')] are compatible!!!
[[
why?
    to save dictionary in form:
        ,{word}
        :{body_line}
        /{body_line}
        /{body_line}
        /{body_line}
    see:
        view script/欧路词典囗.py
        view script/汉语辞海囗.py
        view script/汉语字典囗.py
]]








seed.io.savefile__str_tuple
py -m nn_ns.app.debug_cmd   seed.io.savefile__str_tuple -x
py -m nn_ns.app.doctest_cmd seed.io.savefile__str_tuple:__doc__ -ff -v
py -m nn_ns.app.doctest_cmd seed.io.savefile__str_tuple!
py_adhoc_call   seed.io.savefile__str_tuple   @f





from seed.str_tools.iter_split_ex_by_ import iter_split_ex_by_
from seed.io.savefile__str_tuple import iter_split_ex_by_may_smay_newline_
from seed.io.savefile__str_tuple import SaveStrTupleAsMultiLine, std_saver4str_tuple
    #SaveStrTupleAsMultiLine(prefix4first_element, prefix4following_element, may_prefix4continue_element_line, smay4empty_tuple, may_prefix4first_comment_line, may_prefix4continue_comment_line, may_smay_newline=, empty_line_ok=)
from seed.io.savefile__str_tuple import BaseFail, ReadFail, SaveFail
from seed.io.savefile__str_tuple import check_supported__may_smay_newline, regex4newlines, iter_split_ex_by_may_smay_newline_, read_until_may_smay_newline
from seed.io.savefile__str_tuple import SaveConstantStrToFile, SaveStrAsMultiLine, SaveCasedStrAsMultiLine, SaveStrTupleAsMultiLine











#copy to: view ../../python3_src/py_stdlib_api.txt :: io__newline__newlines
#   ++test___newlines
[[
io::`newlines` 对象属性 总结:
io::`newline` 构建参数 总结:
===
stream.newlines
    newlines :: None|str|tuple<str>
    不是 构建参数 newline!!
    只在universal_newline模式下起作用:
        只记录连续读操作中，遇到的newline类型
            写操作清零
#test___newlines:goto
#test .newlines
    case param newline of
        None | '' -> None | '\r' | '\n' | '\r\n' | ('\r', '\n', '\r\n') | ('\r', '\n'), ...
        _ -> None
    只在universal_newline模式下起作用:
        #write() null .newlines
        #read() extend .newlines
        #tell() donot change .newlines
        #seek() donot change .newlines
    非universal_newline模式，.newlines恒定为None:
        # [newline=='\r\n'] ==>> [.newlines===None]
        # [newline=='\r'] ==>> [.newlines===None]
        # [newline=='\n'] ==>> [.newlines===None]
.newlines 声明:
 |  newlines
 |      Line endings translated so far.
 |      Only line endings translated during reading are considered.
===
stream.__init__(..., newline, ...):
    StringIO default '\n'
    TextIOWrapper default None
    open() default None
===
构建参数newline:
translated_or_not: read(), write()
both non-translated ==>> '','\n'
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
py_help io@TextIOWrapper
py_help io@IOBase
 |  encoding
 |      Encoding of the text stream.
 |      Subclasses should override.
 |
 |  errors
 |      The error setting of the decoder or encoder.
 |      Subclasses should override.
 |
 |  newlines
 |      Line endings translated so far.
 |      Only line endings translated during reading are considered.
 |      Subclasses should override.
===
py_help io@TextIOWrapper
    TextIOWrapper(buffer, encoding=None, errors=None, newline=None, line_buffering=False, write_through=False)
===
py_help io@TextIOWrapper.readline
    readline(self, size=-1, /)
        Read until newline or EOF.
===
py_help io@StringIO
    StringIO(initial_value='', newline='\n')
===
py_help @open
help(open):
    [[
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

newline controls how universal newlines works (it only applies to text mode). It can be None, '', '\n', '\r', and '\r\n'.  It works as follows:
* On input
    , if newline is None, universal newlines mode is enabled. Lines in the input can end in '\n', '\r', or '\r\n', and these are translated into '\n' before being returned to the caller.
    If it is '', universal newline mode is enabled, but line endings are returned to the caller untranslated.
    If it has any of the other legal values, input lines are only terminated by the given string, and the line ending is returned to the caller untranslated.
* On output
    , if newline is None, any '\n' characters written are translated to the system default line separator, os.linesep.
    If newline is '' or '\n', no translation takes place.
    If newline is any of the other legal values, any '\n' characters written are translated to the given string.
    ]]

]]










read_until_may_smay_newline
iter_split_ex_by_may_smay_newline_

%s/s\@<!may_newline/may_smay_newline/g
    ... 搜 may_smay_newline 确认 替换正确 & 『newline:=』 正确




TextIOWrapper(buffer, encoding=None, errors=None, newline=None, line_buffering=False, write_through=False)
>>> from io import StringIO, BytesIO, TextIOWrapper

>>> ifile = StringIO('\r\n|\n\r-\r\t\n')
>>> ifile.newlines is None
True
>>> [*ifile]
['\r\n', '|\n', '\r-\r\t\n']

>>> ifile = StringIO('\r\n|\n\r-\r\t\n', '\n')
>>> ifile.newlines is None
True
>>> [*ifile]
['\r\n', '|\n', '\r-\r\t\n']

## replace 3`newlines` by '\n'
>>> ifile = StringIO('\r\n|\n\r-\r\t\n', None)
>>> ifile.newlines
('\r', '\n', '\r\n')
>>> [*ifile]
['\n', '|\n', '\n', '-\n', '\t\n']
>>> ifile.newlines = '\n'
Traceback (most recent call last):
    ...
AttributeError: attribute 'newlines' of '_io.StringIO' objects is not writable
>>> ifile.newlines
('\r', '\n', '\r\n')

## replace '\n' by '\r'
>>> ifile = StringIO('\r\n|\n\r-\r\t\n', '\r')
>>> ifile.newlines is None
True
>>> [*ifile]
['\r', '\r', '|\r', '\r', '-\r', '\t\r']

## replace '\n' by '\r\n'
>>> ifile = StringIO('\r\n|\n\r-\r\t\n', '\r\n')
>>> ifile.newlines is None
True
>>> [*ifile]
['\r\r\n', '|\r\n', '\r-\r\t\r\n']

>>> ifile = StringIO('\r\n|\n\r-\r\t\n', '\n\r')
Traceback (most recent call last):
    ...
ValueError: illegal newline value: '\n\r'
>>> ifile = StringIO('\r\n|\n\r-\r\t\n', ('\n', '\r'))
Traceback (most recent call last):
    ...
TypeError: newline must be str or None, not tuple


#>>> dir(ifile)
## no replace
>>> ifile = StringIO('', '\n')
>>> ifile.write('\r\n|\n\r-\r\t\n')
9
>>> ifile.getvalue()
'\r\n|\n\r-\r\t\n'

## replace '\n' by '\r'
>>> ifile = StringIO('', '\r')
>>> ifile.write('\r\n|\n\r-\r\t\n')
9
>>> ifile.getvalue()
'\r\r|\r\r-\r\t\r'

## replace '\n' by '\r\n'
>>> ifile = StringIO('', '\r\n')
>>> ifile.write('\r\n|\n\r-\r\t\n')
9
>>> ifile.getvalue()
'\r\r\n|\r\n\r-\r\t\r\n'
>>> __ = ifile.seek(0)
>>> [*ifile]
['\r\r\n', '|\r\n', '\r-\r\t\r\n']

## replace 3`newlines` by '\n'
>>> ifile = StringIO('', None)
>>> ifile.write('\r\n|\n\r-\r\t\n')
9
>>> ifile.getvalue()
'\n|\n\n-\n\t\n'


>>> help(ifile.reconfigure)
Traceback (most recent call last):
    ...
AttributeError: '_io.StringIO' object has no attribute 'reconfigure'


#>>> ifile.newlines
('\r', '\n', '\r\n')


#>>> dir(ifile)
>>> ibfile = BytesIO(b'\r\n|\n\r-\r\t\n')
>>> ifile = TextIOWrapper(ibfile, encoding='u8', newline=('\n', '\r'))
Traceback (most recent call last):
    ...
TypeError: TextIOWrapper() argument 'newline' must be str or None, not tuple
>>> ifile = TextIOWrapper(ibfile, encoding='u8', newline='\n\r') #doctest: +NORMALIZE_WHITESPACE
Traceback (most recent call last):
    ...
ValueError: illegal newline value:
<BLANKLINE>
<BLANKLINE>

    #doctest: +NORMALIZE_WHITESPACE
    #doctest: +IGNORE_EXCEPTION_DETAIL
    #<BLANKLINE>
## replace 3`newlines` by '\n'
>>> ifile = TextIOWrapper(ibfile, encoding='u8', newline=None)
>>> ifile.newlines is None
True
>>> ifile.read()
'\n|\n\n-\n\t\n'
>>> __ = ifile.seek(0)
>>> [*ifile]
['\n', '|\n', '\n', '-\n', '\t\n']
>>> __ = ifile.detach()

## no replace
>>> ifile = TextIOWrapper(ibfile, encoding='u8', newline='\n')
>>> ifile.newlines is None
True
>>> __ = ifile.seek(0)
>>> ifile.read()
'\r\n|\n\r-\r\t\n'
>>> __ = ifile.seek(0)
>>> [*ifile]
['\r\n', '|\n', '\r-\r\t\n']
>>> __ = ifile.detach()

## no replace
>>> ifile = TextIOWrapper(ibfile, encoding='u8', newline='\r')
>>> ifile.newlines is None
True
>>> __ = ifile.seek(0)
>>> ifile.read()
'\r\n|\n\r-\r\t\n'
>>> __ = ifile.seek(0)
>>> [*ifile]
['\r', '\n|\n\r', '-\r', '\t\n']
>>> __ = ifile.detach()


## no replace
>>> ifile = TextIOWrapper(ibfile, encoding='u8', newline='\r\n')
>>> ifile.newlines is None  #WTF?!
True
>>> __ = ifile.seek(0)
>>> ifile.read()
'\r\n|\n\r-\r\t\n'
>>> __ = ifile.seek(0)
>>> [*ifile]
['\r\n', '|\n\r-\r\t\n']
>>> __ = ifile.detach()


>>> ibfile = BytesIO()


## replace '\n' by '\r\n'
>>> ifile = TextIOWrapper(ibfile, encoding='u8', newline='\r\n')
>>> ifile.write('\r\n|\n\r-\r\t\n')
9
>>> __ = ifile.seek(0)
>>> ifile.read()  #WTF?!
'\r\r\n|\r\n\r-\r\t\r\n'
>>> __ = ifile.detach()
>>> ibfile.getvalue()
b'\r\r\n|\r\n\r-\r\t\r\n'

not-bug: .write() replace '\n', .read() keep original, incompatible, multi read write unstable
not-bug: .newlines -> None !! when set '\r\n', '\r' !!
export bugs to:
    view ../lots/NOTE/Python/python-bug/io-bug.txt
        @Python 3.10.5 (main, Jun  7 2022, 03:52:12) [Clang 12.0.8 (https://android.googlesource.com/toolchain/llvm-project c935d99d7 on linux



#>>> help(ifile.reconfigure)
TextIOWrapper.reconfigure(*, encoding=None, errors=None, newline=None, line_buffering=None, write_through=None)
>>> ifile = TextIOWrapper(ibfile, encoding='u8', newline='\r\n')
>>> ifile.reconfigure(encoding='ascii')
>>> __ = ifile.seek(0)
>>> ifile.read()  # ==>> `newline` not changed
'\r\r\n|\r\n\r-\r\t\r\n'
>>> __ = ifile.seek(0)
>>> [*ifile]
['\r\r\n', '|\r\n', '\r-\r\t\r\n']
>>> ibfile.getvalue()
b'\r\r\n|\r\n\r-\r\t\r\n'
>>> ifile.reconfigure(newline='\r')
>>> ifile.newlines is None
True
>>> __ = ifile.seek(0)
>>> ifile.read()
'\r\r\n|\r\n\r-\r\t\r\n'
>>> __ = ifile.seek(0)
>>> [*ifile]
['\r', '\r', '\n|\r', '\n\r', '-\r', '\t\r', '\n']
>>> ibfile.getvalue()
b'\r\r\n|\r\n\r-\r\t\r\n'
>>> ifile.write('\r\n|\n\r-\r\t\n')
9
>>> __ = ifile.seek(0)
>>> ifile.read()
'\r\r\n|\r\n\r-\r\t\r\n\r\r|\r\r-\r\t\r'
>>> __ = ifile.seek(0)
>>> [*ifile]
['\r', '\r', '\n|\r', '\n\r', '-\r', '\t\r', '\n\r', '\r', '|\r', '\r', '-\r', '\t\r']
>>> ibfile.getvalue()
b'\r\r\n|\r\n\r-\r\t\r\n\r\r|\r\r-\r\t\r'



## # write not replace # read does replace
>>> ibfile = BytesIO()
>>> ifile = TextIOWrapper(ibfile, encoding='u8', newline=None)
>>> ifile.write('\r\n|\n\r-\r\t\n')
9
>>> __ = ifile.seek(0)
>>> ifile.read() # read does replace
'\n|\n\n-\n\t\n'
>>> __ = ifile.detach()
>>> ibfile.getvalue() # write not replace
b'\r\n|\n\r-\r\t\n'

## no replace
>>> ibfile = BytesIO()
>>> ifile = TextIOWrapper(ibfile, encoding='u8', newline='\n')
>>> ifile.write('\r\n|\n\r-\r\t\n')
9
>>> __ = ifile.seek(0)
>>> ifile.read()
'\r\n|\n\r-\r\t\n'
>>> __ = ifile.detach()
>>> ibfile.getvalue()
b'\r\n|\n\r-\r\t\n'

## replace '\n' by '\r'
>>> ibfile = BytesIO()
>>> ifile = TextIOWrapper(ibfile, encoding='u8', newline='\r')
>>> ifile.write('\r\n|\n\r-\r\t\n')
9
>>> __ = ifile.seek(0)
>>> ifile.read()
'\r\r|\r\r-\r\t\r'
>>> __ = ifile.detach()
>>> ibfile.getvalue()
b'\r\r|\r\r-\r\t\r'


## replace '\n' by '\r\n'
>>> ibfile = BytesIO()
>>> ifile = TextIOWrapper(ibfile, encoding='u8', newline='\r\n')
>>> ifile.write('\r\n|\n\r-\r\t\n')
9
>>> __ = ifile.seek(0)
>>> ifile.read()
'\r\r\n|\r\n\r-\r\t\r\n'
>>> __ = ifile.detach()
>>> ibfile.getvalue()
b'\r\r\n|\r\n\r-\r\t\r\n'



[[[
#test___newlines
#test .newlines
    case param newline of
        None | '' -> None | '\r' | '\n' | '\r\n' | ('\r', '\n', '\r\n') | ('\r', '\n'), ...
        _ -> None
    只在universal_newline模式下起作用:
        #write() null .newlines
        #read() extend .newlines
        #tell() donot change .newlines
        #seek() donot change .newlines
    非universal_newline模式，.newlines恒定为None:
        # [newline=='\r\n'] ==>> [.newlines===None]
        # [newline=='\r'] ==>> [.newlines===None]
        # [newline=='\n'] ==>> [.newlines===None]

>>> ibfile = BytesIO()
>>> ifile = TextIOWrapper(ibfile, encoding='u8', newline='\r\n')
>>> ifile.write('\r\n|\n\r-\r\t\n')
9
>>> ifile.newlines is None
True
>>> __ = ifile.seek(0)
>>> ifile.read()
'\r\r\n|\r\n\r-\r\t\r\n'
>>> ifile.newlines is None # [newline=='\r\n'] ==>> [.newlines===None]
True
>>> __ = ifile.detach()

>>> ibfile = BytesIO()
>>> ifile = TextIOWrapper(ibfile, encoding='u8', newline='\r')
>>> ifile.write('\r\n|\n\r-\r\t\n')
9
>>> ifile.newlines is None
True
>>> __ = ifile.seek(0)
>>> ifile.read()
'\r\r|\r\r-\r\t\r'
>>> ifile.newlines is None # [newline=='\r'] ==>> [.newlines===None]
True
>>> __ = ifile.detach()

>>> ibfile = BytesIO()
>>> ifile = TextIOWrapper(ibfile, encoding='u8', newline='\n')
>>> ifile.write('\r\n|\n\r-\r\t\n')
9
>>> ifile.newlines is None
True
>>> __ = ifile.seek(0)
>>> ifile.read()
'\r\n|\n\r-\r\t\n'
>>> ifile.newlines is None # [newline=='\n'] ==>> [.newlines===None]
True
>>> __ = ifile.detach()

>>> ibfile = BytesIO()
>>> ifile = TextIOWrapper(ibfile, encoding='u8', newline='')
>>> ifile.write('\r\n|\n\r-\r\t\n')
9
>>> ifile.newlines is None
True
>>> __ = ifile.seek(0)
>>> ifile.read()
'\r\n|\n\r-\r\t\n'
>>> ifile.newlines
('\r', '\n', '\r\n')
>>> __ = ifile.detach()




>>> ibfile = BytesIO()
>>> ifile = TextIOWrapper(ibfile, encoding='u8', newline=None)
>>> ifile.write('\r\n|\n\r-\r\t\n')
9
>>> ifile.newlines is None
True
>>> __ = ifile.seek(0)
>>> ifile.read()
'\n|\n\n-\n\t\n'
>>> ifile.newlines
('\r', '\n', '\r\n')
>>> __ = ifile.detach()

>>> ibfile = BytesIO()
>>> ifile = TextIOWrapper(ibfile, encoding='u8', newline=None)
>>> ifile.write('\r\n')
2
>>> ifile.newlines is None
True
>>> __ = ifile.seek(0)
>>> ifile.read(1)
'\n'
>>> ifile.newlines
'\r\n'
>>> ifile.read(1)
''
>>> ifile.newlines
'\r\n'
>>> addr1 = ifile.tell()
>>> ifile.write('\n')
1
>>> ifile.newlines is None
True
>>> __ = ifile.seek(-1,1)
Traceback (most recent call last):
    ...
io.UnsupportedOperation: can't do nonzero cur-relative seeks
>>> __ = ifile.seek(addr1)
>>> ifile.read(1)
'\n'
>>> ifile.newlines
'\n'
>>> ifile.read(1)
''
>>> ifile.newlines
'\n'
>>> addr2 = ifile.tell() #tell() donot change .newlines
>>> ifile.newlines
'\n'
>>> ifile.write('\r') #write() null .newlines
1
>>> ifile.newlines is None
True
>>> __ = ifile.seek(addr2)
>>> ifile.read(1)
'\n'
>>> ifile.newlines
'\r'
>>> ifile.read(1)
''
>>> ifile.newlines
'\r'
>>> __ = ifile.seek(addr1) #seek() donot change .newlines
>>> ifile.newlines
'\r'
>>> ifile.read(1)
'\n'
>>> ifile.newlines  #read() extend .newlines
('\r', '\n')
>>> __ = ifile.detach()

#end-test___newlines
]]]



















>>> from seed.io.savefile__str_tuple import iter_split_ex_by_may_smay_newline_, escape_str_as_multiline
>>> [*iter_split_ex_by_may_smay_newline_(None, '\r\n|\n\r-\r\t\n')]
[('', '\r\n'), ('|', '\n'), ('', '\r'), ('-', '\r'), ('\t', '\n'), ('', '')]
>>> [*iter_split_ex_by_may_smay_newline_('', '\r\n|\n\r-\r\t\n')]
[('', '\r\n'), ('|', '\n'), ('', '\r'), ('-', '\r'), ('\t', '\n'), ('', '')]
>>> [*iter_split_ex_by_may_smay_newline_('\r', '\r\n|\n\r-\r\t\n')]
[('', '\r'), ('\n|\n', '\r'), ('-', '\r'), ('\t\n', '')]
>>> [*iter_split_ex_by_may_smay_newline_('\n', '\r\n|\n\r-\r\t\n')]
[('\r', '\n'), ('|', '\n'), ('\r-\r\t', '\n'), ('', '')]
>>> [*iter_split_ex_by_may_smay_newline_('\r\n', '\r\n|\n\r-\r\t\n')]
[('', '\r\n'), ('|\n\r-\r\t\n', '')]


    #escape_str_as_multiline(prefix4first_line, may_prefix4continue_line, may_smay_newline, s, turnoff_may_smay_newline=turnoff_may_smay_newline)
>>> escape_str_as_multiline('#', '%', None, '\r\n|\n\r-\r\t\n', turnoff_may_smay_newline=True)
'#\r\n%|\n%\r-\r\t\n%'
>>> escape_str_as_multiline('#', '%', None, '\r\n|\n\r-\r\t\n', turnoff_may_smay_newline=False)
'#\r\n%|\n%\r%-\r%\t\n%'
>>> escape_str_as_multiline('#', '%', '', '\r\n|\n\r-\r\t\n', turnoff_may_smay_newline=False)
'#\r\n%|\n%\r%-\r%\t\n%'
>>> escape_str_as_multiline('#', '%', '\n', '\r\n|\n\r-\r\t\n', turnoff_may_smay_newline=False)
'#\r\n%|\n%\r-\r\t\n%'
>>> escape_str_as_multiline('#', '%', '\r', '\r\n|\n\r-\r\t\n', turnoff_may_smay_newline=False)
'#\r%\n|\n\r%-\r%\t\n'
>>> escape_str_as_multiline('#', '%', '\r\n', '\r\n|\n\r-\r\t\n', turnoff_may_smay_newline=False)
'#\r\n%|\n\r-\r\t\n'


    #SaveStrTupleAsMultiLine(prefix4first_element, prefix4following_element, may_prefix4continue_element_line, smay4empty_tuple, may_prefix4first_comment_line, may_prefix4continue_comment_line, may_smay_newline=, empty_line_ok=)

>>> from seed.io.savefile__str_tuple import SaveStrTupleAsMultiLine, std_saver4str_tuple
>>> from contextlib import redirect_stdout, redirect_stderr

>>> with redirect_stderr(sys.stdout):
...     __ = SaveStrTupleAsMultiLine(',', ':', None, '', None, None, may_smay_newline=None, empty_line_ok=False) #doctest: +ELLIPSIS
/sdcard/0my_files/git_repos/python3_src/seed/io/savefile__str_tuple.py:...: UserWarning: !!!only read/write@[`newline` in ('','\n')] are compatible!!! ::: read/write@[may_smay_newline==None in (None,'\r','\r\n')] are incompatible
  warnings.warn(fr"!!!only read/write@[`newline` in ('','\n')] are compatible!!! ::: read/write@[may_smay_newline=={may_smay_newline!r} in (None,'\r','\r\n')] are incompatible")

>>> nonstd_saver = SaveStrTupleAsMultiLine(',', ':', None, '', None, None, may_smay_newline=None, empty_line_ok=False)

>>> nonstd_saver
SaveStrTupleAsMultiLine(',', ':', None, '', None, None, empty_line_ok = False, may_smay_newline = None)
>>> std_saver4str_tuple
SaveStrTupleAsMultiLine(',', ':', '/', '()', '#', '%', empty_line_ok = True, may_smay_newline = '\n')




>>> kw = dict(flush=True, turnoff_may_smay_newline=True)
>>> std_saver4str_tuple.save_empty_line_to_ofile_(None, **kw)
<BLANKLINE>

# '\r' in py-src file will be replaced by '\n' #universal_newline??
#>>> std_saver4str_tuple.save_comment_to_ofile_(None, 'a\rb\r\nc\n', **kw)
#ab
%c
%
>>> obfile = BytesIO()
>>> ofile = TextIOWrapper(obfile, encoding='u8', newline='\n')
>>> std_saver4str_tuple.save_comment_to_ofile_(ofile, 'a\rb\r\nc\n', **kw)
>>> obfile.getvalue()
b'#a\rb\r\n%c\n%\n'
>>> std_saver4str_tuple.save_comment_to_ofile_(None, 'a\nb\nc\n', **kw)
#a
%b
%c
%
>>> std_saver4str_tuple.save_str_tuple_to_ofile_(sys.stdout, ('a\nb\nc\n', '1\n2', '', 'x'), **kw)
,a
/b
/c
/
:1
/2
:
:x
>>> std_saver4str_tuple.save_str_tuple_to_ofile_(sys.stdout, (), **kw)
()
>>> std_saver4str_tuple.save_str_tuple_to_ofile_(sys.stdout, [], **kw)
Traceback (most recent call last):
    ...
TypeError
>>> std_saver4str_tuple.save_str_tuple_to_ofile_(sys.stdout, (1,), **kw)
Traceback (most recent call last):
    ...
TypeError




>>> obfile = BytesIO()
>>> ofile = TextIOWrapper(obfile, encoding='u8', newline=std_saver4str_tuple.get_may_smay_newline())
>>> std_saver4str_tuple.save_comment_to_ofile_(ofile, 'a\rb\r\nc\n', **kw)
>>> obfile.getvalue()
b'#a\rb\r\n%c\n%\n'
>>> std_saver4str_tuple.save_str_tuple_to_ofile_(ofile, (), **kw)
>>> obfile.getvalue()
b'#a\rb\r\n%c\n%\n()\n'
>>> std_saver4str_tuple.save_empty_line_to_ofile_(ofile, **kw)
>>> obfile.getvalue()
b'#a\rb\r\n%c\n%\n()\n\n'
>>> std_saver4str_tuple.save_empty_line_to_ofile_(ofile, **kw)
>>> std_saver4str_tuple.save_comment_to_ofile_(ofile, 'c', **kw)
>>> std_saver4str_tuple.save_comment_to_ofile_(ofile, 'd', **kw)
>>> obfile.getvalue()
b'#a\rb\r\n%c\n%\n()\n\n\n#c\n#d\n'
>>> std_saver4str_tuple.save_str_tuple_to_ofile_(ofile, ('a\rb\r\nc\n', '1\n\n2', '', '\nx', '\n', '\n\n\n'), **kw)
>>> obfile.getvalue()
b'#a\rb\r\n%c\n%\n()\n\n\n#c\n#d\n,a\rb\r\n/c\n/\n:1\n/\n/2\n:\n:\n/x\n:\n/\n:\n/\n/\n/\n'
>>> ifile = ofile
>>> __ = ifile.seek(0)

    # (may_row, outer_inners_outer__mcommentss, may_exc)
    ## postcondition:[(0 if may_row is None else len(may_row))+1 == len(outer_inners_outer__mcommentss)][outer_inners_outer__mcommentss[0] or not may_row is None]
>>> [*std_saver4str_tuple.iter_read_str_tuple_ex_from_ifile_(ifile)]
[((), (['a\rb\r\nc\n'],), None), (('a\rb\r\nc\n', '1\n\n2', '', '\nx', '\n', '\n\n\n'), ([None, None, 'c', 'd'], [], [], [], [], [], []), ReadFail__eof())]
>>> __ = ofile.seek(0,2)
>>> std_saver4str_tuple.save_empty_line_to_ofile_(ofile, **kw)
>>> std_saver4str_tuple.save_comment_to_ofile_(ofile, 'e', **kw)
>>> __ = ifile.seek(0)
>>> [*std_saver4str_tuple.iter_read_str_tuple_ex_from_ifile_(ifile)]
[((), (['a\rb\r\nc\n'],), None), (('a\rb\r\nc\n', '1\n\n2', '', '\nx', '\n', '\n\n\n'), ([None, None, 'c', 'd'], [], [], [], [], [], [None, 'e']), ReadFail__eof())]
>>> [*std_saver4str_tuple.iter_read_str_tuple_from_ifile_(ifile)]
[]
>>> __ = ifile.seek(0)
>>> [*std_saver4str_tuple.iter_read_str_tuple_from_ifile_(ifile)]
[(), ('a\rb\r\nc\n', '1\n\n2', '', '\nx', '\n', '\n\n\n')]


nonstd_saver
>>> __ = ifile.seek(0)
>>> [*nonstd_saver.iter_read_str_tuple_from_ifile_(ifile)]
Traceback (most recent call last):
    ...
seed.io.savefile__str_tuple.ReadFail__not_found_suitable_prefix4first_line
>>> ifile.tell()
0
>>> obfile = BytesIO()
>>> ofile = TextIOWrapper(obfile, encoding='u8', newline=nonstd_saver.get_may_smay_newline())
>>> ifile = ofile
>>> nonstd_saver
SaveStrTupleAsMultiLine(',', ':', None, '', None, None, empty_line_ok = False, may_smay_newline = None)
>>> nonstd_saver.save_empty_line_to_ofile_(ofile, **kw)
Traceback (most recent call last):
    ...
seed.io.savefile__str_tuple.SaveFail__not_support_empty_line
>>> nonstd_saver.save_comment_to_ofile_(ofile, 'd', **kw)
Traceback (most recent call last):
    ...
seed.io.savefile__str_tuple.SaveFail__not_support_comment
>>> nonstd_saver.save_str_tuple_to_ofile_(ofile, (), **kw)
Traceback (most recent call last):
    ...
seed.io.savefile__str_tuple.SaveFail__not_support_empty_tuple
>>> nonstd_saver.save_str_tuple_to_ofile_(ofile, ('\n',), **kw)
Traceback (most recent call last):
    ...
seed.io.savefile__str_tuple.SaveFail__not_support_multiline
>>> obfile.getvalue()
b''
>>> nonstd_saver.save_str_tuple_to_ofile_(ofile, ('',), **kw)
>>> nonstd_saver.save_str_tuple_to_ofile_(ofile, ('a',), **kw)
>>> obfile.getvalue()
b',\n,a\n'
>>> nonstd_saver.save_str_tuple_to_ofile_(None, ('a', 'b', '', 'd'), **kw)
,a
:b
:
:d
>>> nonstd_saver.save_str_tuple_to_ofile_(ofile, ('a', 'b', '', 'd'), **kw)
>>> obfile.getvalue()
b',\n,a\n,a\n:b\n:\n:d\n'
>>> __ = ifile.seek(0)
>>> [*nonstd_saver.iter_read_str_tuple_from_ifile_(ifile)]
[('',), ('a',), ('a', 'b', '', 'd')]



save_header_to_ofile_
>>> obfile = BytesIO()
>>> ofile = TextIOWrapper(obfile, encoding='u8', newline=nonstd_saver.get_may_smay_newline())
>>> nonstd_saver.save_header_to_ofile_(ofile, **kw)
Traceback (most recent call last):
    ...
seed.io.savefile__str_tuple.SaveFail__not_support_comment
>>> std_saver4str_tuple.save_header_to_ofile_(ofile, **kw)
>>> obfile.getvalue()
b"#'u8'\n#SaveStrTupleAsMultiLine(',', ':', '/', '()', '#', '%', empty_line_ok = True, may_smay_newline = '\\n')\n"
>>> print(obfile.getvalue().decode('ascii'))
#'u8'
#SaveStrTupleAsMultiLine(',', ':', '/', '()', '#', '%', empty_line_ok = True, may_smay_newline = '\n')
<BLANKLINE>
>>> print(obfile.getvalue().decode('ascii'), end='')
#'u8'
#SaveStrTupleAsMultiLine(',', ':', '/', '()', '#', '%', empty_line_ok = True, may_smay_newline = '\n')

>>> ot = std_saver4str_tuple.rebuild_with_new_may_smay_newline_('\r\n')
>>> not ot is std_saver4str_tuple
True
>>> ot
SaveStrTupleAsMultiLine(',', ':', '/', '()', '#', '%', empty_line_ok = True, may_smay_newline = '\r\n')
>>> std_saver4str_tuple
SaveStrTupleAsMultiLine(',', ':', '/', '()', '#', '%', empty_line_ok = True, may_smay_newline = '\n')



#]]]'''
__all__ = r'''
BaseFail
    BaseFail__unsupport__may_smay_newline__need_translation__ofile_tell_incompatible_with_buffer
    BaseFail__unsupport__may_smay_newline__need_translation__ofile_without_buffer
    BaseFail__unsupported__newline
    BaseFail__bad_config__may_smay_newline_incompatible_with_ifile

    ReadFail
        ReadFail__eof
        ReadFail__empty_line
        ReadFail__not_found_suitable_prefix4first_line
        ReadFail__bad_prefix4first_line

    SaveFail
        SaveFail__not_support_multiline
        SaveFail__not_support_empty_line
        SaveFail__not_support_comment
        SaveFail__not_support_empty_tuple

read_may_line_ex
    read_line_ex_or_raise_
read_may_empty_line
    read_may_constant_line
    peek_empty_line_or_raise_
        peek_constant_line_or_raise_
is_eof
    peek_
read_until_may_smay_newline


check_supported__may_smay_newline
    check_may_str
    all_supported_newlines
    all_supported_may_smay_newlines
regex4newlines
iter_split_ex_by_may_smay_newline_
    iter_split_ex_by_universal_newline_
    iter_split_ex_by_



write_str_to_ofile_
    escape_str_as_multiline
        str2iter_escaped_lines
ISaveStrToFile
    SaveConstantStrToFile
    IMixin4SaveStrToFile
        SaveStrAsMultiLine

SaveCasedStrAsMultiLine
SaveStrTupleAsMultiLine
    std_saver4str_tuple

'''.split()#'''
            #ReadFail__following_element_without_first_element
__all__

from seed.abc.abc__ver1 import abstractmethod, override, ABC, ABC__no_slots
from seed.str_tools.iter_split_ex_by_ import iter_split_ex_by_
from seed.helper.repr_input import repr_helper
from seed.seq_tools.bisearch import bisearch
from seed.io.with4seekback import with4seekback__on_exit, with4seekback__on_err, with4seekback__on_no_err
from seed.tiny import check_type_is, null_tuple, chains, mk_tuple, check_type_le, ifNone, echo_args_kwargs
from seed.text.are_all_prefixes_mutex import find_may_non_mutex_prefix_pair_, are_all_prefixes_mutex, check_all_prefixes_mutex
from operator import __index__
#from itertools import chain
from itertools import islice, starmap
import re
from io import StringIO
import logging
logging.log
import warnings
warnings.warn
import sys
__all__

assert [*StringIO('\r\n|\n\r-\r\t\n')] == [*StringIO('\r\n|\n\r-\r\t\n', '\n')] == ['\r\n', '|\n', '\r-\r\t\n']
assert [*StringIO('\r\n|\n\r-\r\t\n', None)] == ['\n', '|\n', '\n', '-\n', '\t\n']
    #universal_newline

def _warn4may_smay_newline_(may_smay_newline, /):
    if not may_smay_newline in ('','\n'):
        warnings.warn(fr"!!!only read/write@[`newline` in ('','\n')] are compatible!!! ::: read/write@[may_smay_newline=={may_smay_newline!r} in (None,'\r','\r\n')] are incompatible")

class BaseFail(Exception):pass

class BaseFail__unsupport__may_smay_newline__need_translation__ofile_tell_incompatible_with_buffer(BaseFail):pass
class BaseFail__unsupport__may_smay_newline__need_translation__ofile_without_buffer(BaseFail):pass
class BaseFail__unsupported__newline(BaseFail):pass
    #io.UnsupportedOperation
class ReadFail(BaseFail):pass
class SaveFail(BaseFail):pass

class BaseFail__bad_config__may_smay_newline_incompatible_with_ifile(BaseFail):pass
class ReadFail__eof(ReadFail):pass
    #EOFError
class ReadFail__empty_line(ReadFail):pass
class ReadFail__not_found_suitable_prefix4first_line(ReadFail):pass
#class ReadFail__following_element_without_first_element(ReadFail):pass
class ReadFail__bad_prefix4first_line(ReadFail):pass
#class ReadFail__bad_prefix4continue_line(ReadFail):pass
class SaveFail__not_support_multiline(SaveFail):pass
class SaveFail__not_support_empty_line(SaveFail):pass
class SaveFail__not_support_comment(SaveFail):pass
class SaveFail__not_support_empty_tuple(SaveFail):pass

def read_may_line_ex(ifile, prefix, may_smay_newline, /):
    '-> may (_line_, smay_newline) | ^BaseFail__bad_config__may_smay_newline_incompatible_with_ifile #exclude prefix'
    try:
        (_line_, smay_newline) = read_line_ex_or_raise_(ReadFail, ifile, prefix, may_smay_newline)
    except ReadFail:
        return None
    return (_line_, smay_newline)

def read_line_ex_or_raise_(ErrT, ifile, prefix, may_smay_newline, /):
    '-> (_line_, smay_newline) | ^ErrT | ^BaseFail__bad_config__may_smay_newline_incompatible_with_ifile  #exclude prefix'
    with with4seekback__on_err(ifile):
        s = ifile.read(len(prefix))
        if not s == prefix: raise ErrT(s, prefix)
        #???ifile.readline()

        _line_, smay_newline = read_until_may_smay_newline(ifile, may_smay_newline)
            #prefix has been readed ==>> _line_ not line_
            # ^BaseFail__bad_config__may_smay_newline_incompatible_with_ifile
    return (_line_, smay_newline)
def read_may_empty_line(ifile, may_smay_newline, /):
    '-> may smay_newline | ^BaseFail__bad_config__may_smay_newline_incompatible_with_ifile'
    return read_may_constant_line(ifile, may_smay_newline, '')
def read_may_constant_line(ifile, may_smay_newline, content, /):
    '-> may smay_newline | ^BaseFail__bad_config__may_smay_newline_incompatible_with_ifile'
    try:
        smay_newline = peek_constant_line_or_raise_(ReadFail, ifile, may_smay_newline, content)
    except ReadFail:
        return None
    s = ifile.read(len(content)+len(smay_newline))
        #read not peek => ifile.tell() change
    assert s == content + smay_newline
    return smay_newline
def peek_empty_line_or_raise_(ErrT, ifile, may_smay_newline, /):
    '-> smay_newline | ^ErrT | ^BaseFail__bad_config__may_smay_newline_incompatible_with_ifile'
    return peek_constant_line_or_raise_(ErrT, ifile, may_smay_newline, '')
def peek_constant_line_or_raise_(ErrT, ifile, may_smay_newline, content, /):
    r"-> smay_newline | ^ErrT | ^BaseFail__bad_config__may_smay_newline_incompatible_with_ifile #precondition:[content not contain '\r','\n']"
    check_supported__may_smay_newline(may_smay_newline)
    #check_may_str(may_smay_newline)
    #if not may_smay_newline is None:
    if may_smay_newline is None:
        # None universal_newline
        newline = '\n' # read() translated to this
        L = 1
    elif may_smay_newline:
        newline = may_smay_newline
        L = len(newline)
    else:
        # '' universal_newline
        L = 2 # 1|2
    #if not L > 0:raise ValueError(newline, '`newline` cannot be ""')
    assert L > 0

    L
    sz = len(content) + L
    with with4seekback__on_exit(ifile):
        #s = ifile.readline(sz)
        #assert len(s) <= sz
        line_, smay_newline = read_until_may_smay_newline(ifile, may_smay_newline, sz)
            # ^BaseFail__bad_config__may_smay_newline_incompatible_with_ifile
    #use read_until_may_smay_newline??
    if not line_ == content:
        #assume [content not contain '\r','\n']
        raise ErrT('not match', content, line_, smay_newline)

    #if not s.startswith(content):
    #    raise ErrT('not startswith', content, s)
    #t = s[len(content):]
    #if not t:
    #    #eof <<== assume [content not contain '\r','\n']
    #    smay_newline = ''
    #elif may_smay_newline or may_smay_newline is None:
    #    # newline or None universal_newline
    #    if not t == newline:
    #        raise ErrT('!= newline', newline, t)
    #    smay_newline = newline
    #else:
    #    # '' universal_newline
    #    m = regex4newlines.match(t)
    #    #xxx m = regex4newlines.fullmatch(t)
    #    if m is None:
    #        raise ErrT('not universal_newline', t)
    #    newline = m.group(0)
    #    smay_newline = newline
    #smay_newline
    return smay_newline

def peek_(ifile, sz, /):
    with with4seekback__on_exit(ifile):
        return ifile.read(sz)
def is_eof(ifile, /):
    return not peek_(ifile, 1)

def read_until_may_smay_newline(ifile, may_smay_newline, imay_sz=-1, /):
    '-> (line_, smay_newline) | ^BaseFail__bad_config__may_smay_newline_incompatible_with_ifile  #precondition: [may_smay_newline compatible with ifile]'
    #now: assume [may_smay_newline compatible with ifile]
    s = ifile.readline(imay_sz)
    assert imay_sz < 0 or len(s) <= imay_sz
    _it = iter_split_ex_by_may_smay_newline_(may_smay_newline, s)
    it = islice(_it, 2)
    ls = [*it]
    if len(ls) == 2:
        if any(ls[1]):
            # bad: e.g: s=='\n\r' --> [('', '\n'), ('\r', '')]
            raise BaseFail__bad_config__may_smay_newline_incompatible_with_ifile(f'may_smay_newline incompatible with ifile')
        else:
            # ok:  e.g: s=='\n' --> [('', ''), ('\r', '')]
            [] = _it
            ls.pop()
            pass
    assert ls
    assert len(ls) == 1
    [(line_, smay_newline)] = ls
    assert len(s) == len(line_) + len(smay_newline)
    if not len(s) == imay_sz:
        #need more verify
        if not (smay_newline or is_eof(ifile)):
            #MUST terminated by newline or eof
            raise BaseFail__bad_config__may_smay_newline_incompatible_with_ifile(f'may_smay_newline incompatible with ifile')

        if not may_smay_newline:
            # universal_newline None|''
            if smay_newline == '\r' and peek_(ifile, 1) == '\n':
                # cannot cut '\r\n' to '\r'
                raise BaseFail__bad_config__may_smay_newline_incompatible_with_ifile(f'may_smay_newline incompatible with ifile')
    else:
        # len(s) == imay_sz >= 0
        # ok: terminated by limit
        pass
    return (line_, smay_newline)
    ##old-version2: too difficult to impl
    '-> (line_, smay_newline)'
    check_supported__may_smay_newline(may_smay_newline)
    assert may_smay_newline == '\n'
    the_newline = '\n'
    with with4seekback__on_err(ifile):
        line = ifile.readline()
        i = line.find(the_newline)
        L = len(line)
        if i == L-1:
            smay_newline = the_newline
        elif i == -1:
            #check eof

            #if not is_eof(ifile)
            if ifile.read(1):
                #not eof
                raise BaseFail__bad_config__may_smay_newline_incompatible_with_ifile(f'only "\n" supported')
            #eof
            smay_newline = ''
        else:
            raise BaseFail__bad_config__may_smay_newline_incompatible_with_ifile(f'only "\n" supported')
    smay_newline
    line_ = line[:L-len(smay_newline)]
    return (line_, smay_newline)
    ##bug!!: old-version: fail: .newlines readonly
    #   .newlines 不是 构建参数newline/may_smay_newline

    check_supported__may_smay_newline(may_smay_newline)
    saved = ifile.newlines
    try:
        ifile.newlines = may_smay_newline

        line = ifile.readline()
    finally:
        ifile.newlines = saved

    L = len(line)
    if may_smay_newline is None:
        m = regex4newlines.search(line, max(0,L-2))
        i = L if m is None else m.start(0)
        smay_newline = line[L:]
    else:
        newline = may_smay_newline
        smay_newline = newline
    smay_newline
    line_ = line[:L-len(smay_newline)]
    return (line_, smay_newline)
#end-def read_until_may_smay_newline(ifile, may_smay_newline, imay_sz=-1, /):


def check_supported__may_smay_newline(may_smay_newline, /):
    check_may_str(may_smay_newline)
    if not may_smay_newline in all_supported_may_smay_newlines:raise BaseFail__unsupported__newline('unsupported newline', may_smay_newline)
def check_may_str(may_s, /):
    if not may_s is None:
        s = may_s
        check_type_is(str, s)


#all_supported_newlines = ('\r\n', '\n\r', '\r', '\n')
    #??? ('\r', '\n', '\r\n')
#all_supported_may_smay_newlines = (None, *all_supported_newlines)
#all_supported_may_smay_newlines = ('\n',)
    # only support '\n'
    # others are buggy; see: 『WTF』 above __doc__
#without: '\n\r'
all_supported_newlines = ('\r\n', '\r', '\n')
all_supported_may_smay_newlines = ('\r\n', '\r', '\n', '', None)

#regex4bad_newlines = re.compile(r'\r\n|\n\r|\r')
#xxx regex4newlines = re.compile(r'\r\n|\n\r|\r|\n')
regex4newlines = re.compile(r'\r\n|\r|\n')
def iter_split_ex_by_universal_newline_(s, /):
    '-> (line_, smay_newline)'
    i = 0
    for m in regex4newlines.finditer(s):
        j, k = m.span(0)
        line_ = s[i:j]
        smay_newline = s[j:k]
        assert smay_newline
        yield (line_, smay_newline)
        i = k
    line_ = s[i:]
    smay_newline = ''
    yield (line_, smay_newline)
    return

def __():
#copy to seed.str_tools.iter_split_ex_by_
  def iter_split_ex_by_(substr, s, /):
    '-> Iter (gap, smay substr)  # str | bytes'
    if not len(substr): raise ValueError
    L = len(substr)
    i = 0
    while 1:
        j = s.find(substr, i)
        if j == -1:break
        gap = s[i:j]
        yield gap, substr
        i = j+L
    gap = s[i:]
    yield gap, substr[:0]
    return

def iter_split_ex_by_may_smay_newline_(may_smay_newline, s, /):
    check_may_str(may_smay_newline)
    #if may_smay_newline is None:
    if not may_smay_newline:
        # universal_newline None | ''
        return iter_split_ex_by_universal_newline_(s)
    newline = may_smay_newline
    return iter_split_ex_by_(newline, s)




def write_str_to_ofile_(may_ofile, s, /, *, may_smay_newline, flush:bool, turnoff_may_smay_newline:bool):
    ofile = ifNone(may_ofile, sys.stdout)

    may_smay_newline = '\n' if turnoff_may_smay_newline else may_smay_newline

    if may_smay_newline in ('', '\n'):
        #no translation takes place
        print(s, file=ofile, end='\n', flush=flush)
        return

    try:
        obfile = ofile.buffer
    except AttributeError:
        raise BaseFail__unsupport__may_smay_newline__need_translation__ofile_without_buffer

    if not obfile.tell() == ofile.tell(): raise BaseFail__unsupport__may_smay_newline__need_translation__ofile_tell_incompatible_with_buffer
    bs = s.encode(ofile.encoding)
    addr4txt_ = ofile.tell()
    addr4bs_ = obfile.tell()
    obfile.write(bs)
    _addr4bs = obfile.tell()
    obfile.seek(addr4bs_)
    if not addr4bs_ + len(bs) == _addr4bs: raise logic-err
    if ofile.readable() and ofile.seekable():
        ofile.seek(addr4txt_)
        if not s == ofile.read(len(s)): raise logic-err

    if not obfile.tell() == ofile.tell(): raise BaseFail__unsupport__may_smay_newline__need_translation__ofile_tell_incompatible_with_buffer

    return
#end-def write_str_to_ofile_(ofile, s, /, *, may_smay_newline, flush:bool, turnoff_may_smay_newline:bool):






class ISaveStrToFile(ABC):
    'read fail => ifile.tell() not changed'
    __slots__ = ()

    @abstractmethod
    def __repr__(sf, /):
        raise NotImplementedError
    @abstractmethod
    def get_prefix4first_line(sf, /):
        '-> str'
        raise NotImplementedError
    @abstractmethod
    def get_may_prefix4continue_line(sf, /):
        '-> may str # None => not support multiline'
        raise NotImplementedError
    @abstractmethod
    def get_may_smay_newline(sf, /):
        '-> may str # None/"" => universal_newline'
        raise NotImplementedError
    @abstractmethod
    def read_str_from_ifile_(sf, ifile, /):
        'ifile -> str | ^ReadFail__bad_prefix4first_line | ^BaseFail__bad_config__may_smay_newline_incompatible_with_ifile'
        raise NotImplementedError
    @abstractmethod
    def save_str_to_ofile_(sf, ofile, s, /, *, flush:bool, turnoff_may_smay_newline:bool):
        'ofile -> str -> None'
        raise NotImplementedError


class SaveConstantStrToFile(ISaveStrToFile):
    #for smay4empty_tuple
    'read fail => ifile.tell() not changed'
    ___no_slots_ok___ = True
    def __init__(sf, content, /, *, may_smay_newline):
        sf._saver = SaveStrAsMultiLine(content, None, may_smay_newline=may_smay_newline) #check args...

        _warn4may_smay_newline_(may_smay_newline)
        sf._args = (content, may_smay_newline)
    @override
    def __repr__(sf, /):
        (content, may_smay_newline) = sf._args
        return repr_helper(sf, content, may_smay_newline=may_smay_newline)

    @override
    def get_prefix4first_line(sf, /):
        '-> str'
        return sf._saver.get_prefix4first_line()
    @override
    def get_may_prefix4continue_line(sf, /):
        '-> may str # None => not support multiline'
        return None
        return sf._saver.get_may_prefix4continue_line()
    @override
    def get_may_smay_newline(sf, /):
        '-> may str # None/"" => universal_newline'
        return sf._saver.get_may_smay_newline()
    @override
    def read_str_from_ifile_(sf, ifile, /):
        'ifile -> str | ^ReadFail__bad_prefix4first_line | ^BaseFail__bad_config__may_smay_newline_incompatible_with_ifile'
        prefix_as_content = sf.get_prefix4first_line()
        may_smay_newline = sf.get_may_smay_newline()
        _may_smay_newline = read_may_constant_line(ifile, may_smay_newline, prefix_as_content)
            # | ^BaseFail__bad_config__may_smay_newline_incompatible_with_ifile
        if _may_smay_newline is None:
            #not match
            raise ReadFail__bad_prefix4first_line
        return '' # <~~~> save ''
    @override
    def save_str_to_ofile_(sf, ofile, s, /, *, flush:bool, turnoff_may_smay_newline:bool):
        'ofile -> str -> None'
        check_type_is(str, s)
        if not s == '': raise ValueError
        sf._saver.save_str_to_ofile_(ofile, '', flush=flush, turnoff_may_smay_newline=turnoff_may_smay_newline)
        return


class IMixin4SaveStrToFile(ISaveStrToFile):
    'read fail => ifile.tell() not changed'
    __slots__ = ()

    @override
    def read_str_from_ifile_(sf, ifile, /):
        'ifile -> str | ^ReadFail__bad_prefix4first_line | ^BaseFail__bad_config__may_smay_newline_incompatible_with_ifile'
        #may_smay_newline = sf.get_may_smay_newline()
        #newline = ifNone(may_smay_newline, '\n')
        it = sf.iter_line_contents_ex_from_ifile_(ifile)
            # | ^BaseFail__bad_config__may_smay_newline_incompatible_with_ifile
        return ''.join(chains(it))
    def iter_line_contents_ex_from_ifile_(sf, ifile, /):
        'ifile -> Iter (_line_, smay_newline) | ^ReadFail__bad_prefix4first_line  | ^BaseFail__bad_config__may_smay_newline_incompatible_with_ifile #exclude prefix'
        may_smay_newline = sf.get_may_smay_newline()
        prefix = sf.get_prefix4first_line()
        _fst_line_, smay_newline = read_line_ex_or_raise_(ReadFail__bad_prefix4first_line, ifile, prefix, may_smay_newline)
            #  | ^BaseFail__bad_config__may_smay_newline_incompatible_with_ifile
        #xxx yield _fst_line_, smay_newline #exclude prefix
        prev = _fst_line_, smay_newline
        while 1:
            if not smay_newline:
                #eof
                break

            m = sf.get_may_prefix4continue_line()
            if m is None:
                # not support multiline
                break

            prefix = m
            while 1:
                m = read_may_line_ex(ifile, prefix, may_smay_newline)
                    # | ^BaseFail__bad_config__may_smay_newline_incompatible_with_ifile
                if m is None:
                    break
                _line_, smay_newline = m
                #xxx yield _line_, smay_newline
                yield prev
                prev = _line_, smay_newline
            break
        _last_line_, _ = prev
        yield (_last_line_, '')
        return

    @override
    def save_str_to_ofile_(sf, ofile, s, /, *, flush:bool, turnoff_may_smay_newline:bool):
        'ofile -> str -> None'
        ##!! update with turnoff_may_smay_newline !!: save_empty_line_to_ofile_/save_cased_str_to_ofile_/save_comment_to_ofile_/save_str_tuple_to_ofile_/save_str_to_ofile_
        check_type_is(str, s)
        _s = sf.escape_str_as_multiline(s, turnoff_may_smay_newline=turnoff_may_smay_newline)
            # check turnoff_may_smay_newline
        may_smay_newline = sf.get_may_smay_newline()
        write_str_to_ofile_(ofile, _s, may_smay_newline=may_smay_newline, flush=flush, turnoff_may_smay_newline=turnoff_may_smay_newline)
        return
        ## old-version
        _s = sf.escape_str_as_multiline(s)
        may_smay_newline = sf.get_may_smay_newline()
        newline = ifNone(may_smay_newline, '\n')

        print(_s, file=ofile, end=newline, flush=flush)
        return
    def escape_str_as_multiline(sf, s, /, *, turnoff_may_smay_newline:bool):
        #return escape_str_as_multiline(prefix4first_line, may_prefix4continue_line, may_smay_newline, s, turnoff_may_smay_newline=turnoff_may_smay_newline)
        return ''.join(sf.str2iter_escaped_lines(s, turnoff_may_smay_newline=turnoff_may_smay_newline))
    def str2iter_escaped_lines(sf, s, /, *, turnoff_may_smay_newline:bool):
        prefix4first_line = sf.get_prefix4first_line()
        may_prefix4continue_line = sf.get_may_prefix4continue_line()
        may_smay_newline = sf.get_may_smay_newline()
        return str2iter_escaped_lines(prefix4first_line, may_prefix4continue_line, may_smay_newline, s, turnoff_may_smay_newline=turnoff_may_smay_newline)

def str2iter_escaped_lines(prefix4first_line, may_prefix4continue_line, may_smay_newline, s, /, *, turnoff_may_smay_newline:bool):
    check_type_is(bool, turnoff_may_smay_newline)
    may_smay_newline = '\n' if turnoff_may_smay_newline else may_smay_newline
    #if may_smay_newline:
        #it = iter(StringIO(s, None))
    it = iter_split_ex_by_may_smay_newline_(may_smay_newline, s)
    assert it is iter(it)
    prefix = prefix4first_line
    m = may_prefix4continue_line
    has_next_line = True
    for line_, smay_newline in it:
        assert has_next_line
        has_next_line = bool(smay_newline)
        yield f'{prefix}{line_}{smay_newline}'
        if has_next_line:
            if m is None:
                raise SaveFail__not_support_multiline #not support multiline
            prefix = m
    assert not has_next_line
    return


def escape_str_as_multiline(prefix4first_line, may_prefix4continue_line, may_smay_newline, s, /, *, turnoff_may_smay_newline:bool):
    return ''.join(str2iter_escaped_lines(prefix4first_line, may_prefix4continue_line, may_smay_newline, s, turnoff_may_smay_newline=turnoff_may_smay_newline))



assert not ''.isspace()
class SaveStrAsMultiLine(IMixin4SaveStrToFile):
    'read fail => ifile.tell() not changed' '  # may_smay_newline=None/"" => universal_newline'
    ___no_slots_ok___ = True
    #SaveStrAsMultiLine(prefix4first_line, may_prefix4continue_line, may_smay_newline=)
    def __init__(sf, prefix4first_line, may_prefix4continue_line, /, *, may_smay_newline):
        check_type_is(str, prefix4first_line)
        check_may_str(may_prefix4continue_line)
        #check_may_str(may_smay_newline)
        check_supported__may_smay_newline(may_smay_newline)

            #if not newline: raise TypeError('`newline` cannot be ""')


        ls = [prefix4first_line]
        if not may_prefix4continue_line is None:
            prefix4continue_line = may_prefix4continue_line

            ls.append(prefix4continue_line)
        for prefix in ls:
            #assert not ''.isspace()
            #using prefix[:1] instead of prefix[0]
            #   prefix may be ''
            #       although only one case
            if prefix[:1].isspace():raise ValueError(f'prefix[:1] is space: {prefix!r}')

        #if not may_smay_newline is None:
        if may_smay_newline:
            newline = may_smay_newline
            ls.append(newline)
        else:
            # universal_newline None|''
            #ls.extend(all_supported_newlines)
            ls.extend('\r\n')
        check_all_prefixes_mutex(ls)



        sf._p4fst = prefix4first_line
        sf._mp4ctn = may_prefix4continue_line
        sf._mnwl = may_smay_newline
        _warn4may_smay_newline_(may_smay_newline)
        sf._args = ()
    @override
    def __repr__(sf, /):
        (prefix4first_line, may_prefix4continue_line, may_smay_newline) = sf._args
        return repr_helper(sf, prefix4first_line, may_prefix4continue_line, may_smay_newline=may_smay_newline)
    @override
    def get_prefix4first_line(sf, /):
        '-> str'
        return sf._p4fst
    @override
    def get_may_prefix4continue_line(sf, /):
        '-> may str # None => not support multiline'
        return sf._mp4ctn
    @override
    def get_may_smay_newline(sf, /):
        '-> may str # None/"" => universal_newline'
        return sf._mnwl










class SaveCasedStrAsMultiLine:
    'read fail => ifile.tell() not changed'
    def __init__(sf, iter4ISaveStrToFile, /, *, may_smay_newline, empty_line_ok:bool):
        check_type_is(bool, empty_line_ok)
        #check_may_str(may_smay_newline)
        check_supported__may_smay_newline(may_smay_newline)
        savers = mk_tuple(iter4ISaveStrToFile)
        #if not savers:raise ValueError('requires at least 1 ISaveStrToFile')
        def __():
            for saver in savers:
                check_type_le(ISaveStrToFile, saver)
        __()


        mnwls = {saver.get_may_smay_newline() for saver in savers}
        mnwls = sorted(mnwls, key=repr)
        if not len(mnwls) <= 1:
            raise ValueError(f'incompatible may_smay_newline: {mnwls}')
        if not all(mnwl == may_smay_newline for mnwl in mnwls):raise ValueError(f'incompatible may_smay_newline: {mnwls} with {may_smay_newline!r}')


        fsts = (saver.get_prefix4first_line() for saver in savers)
        sorted_fsts = sorted(fsts)
        check_all_prefixes_mutex(sorted_fsts, is_sorted=True)

        mflws = {saver.get_may_prefix4continue_line() for saver in savers}
        mflws.discard(None)
        flws = mflws; del mflws
        for flw in flws:
            (i,j) = bisearch(flw, sorted_fsts)
            assert i==j # <<== check_all_prefixes_mutex(sorted_fsts, is_sorted=True)
            ls = sorted_fsts[max(0,i-1):j+1]
            if not ls:
                raise logic-err
            elif i==0:
                k = 0
            else:
                k = 1
            k
            ls.insert(k, flw)
            check_all_prefixes_mutex(ls, is_sorted=True)

        sf._ls = savers
        sf._ok = empty_line_ok
        sf._mnwl = may_smay_newline
        _warn4may_smay_newline_(may_smay_newline)
        sf._args = (savers, may_smay_newline, empty_line_ok)
    def __repr__(sf, /):
        (savers, may_smay_newline, empty_line_ok) = sf._args
        return repr_helper(sf, [*savers], may_smay_newline=may_smay_newline, empty_line_ok=empty_line_ok)
    def get_savers(sf, /):
        return sf._ls
    def is_empty_line_ok(sf, /):
        return sf._ok
    def get_may_smay_newline(sf, /):
        '-> may str # None/"" => universal_newline'
        return sf._mnwl

    def read_may_cased_str_from_ifile_(sf, ifile, /, *, excluded_idc):
        'ifile -> may (idx, str) | ^ReadFail__eof | ^ReadFail__empty_line | ^ReadFail__not_found_suitable_prefix4first_line | ^BaseFail__bad_config__may_smay_newline_incompatible_with_ifile  # None => [[empty_line_ok][empty_line found not at eof]] # ^ReadFail__empty_line => [[not empty_line_ok][empty_line found not at eof]]'
        may_smay_newline = sf.get_may_smay_newline()
        _may_smay_newline = read_may_empty_line(ifile, may_smay_newline)
            # | ^BaseFail__bad_config__may_smay_newline_incompatible_with_ifile
        if not _may_smay_newline is None:
            smay_newline = _may_smay_newline
            if not smay_newline:
                #eof
                raise ReadFail__eof
            else:
                #not eof
                #empty_line
                if not sf.is_empty_line_ok(): raise ReadFail__empty_line
                return None
        #not eof
        #not empty_line
        for idx, saver in enumerate(sf.get_savers()):
            if idx in excluded_idc:continue
            try:
                s = saver.read_str_from_ifile_(ifile)
                    # | ^BaseFail__bad_config__may_smay_newline_incompatible_with_ifile
            except ReadFail__bad_prefix4first_line:
                continue
            break
        else:
            raise ReadFail__not_found_suitable_prefix4first_line
        return idx, s
    def save_empty_line_to_ofile_(sf, ofile, /, *, flush:bool, turnoff_may_smay_newline:bool):
        if not sf.is_empty_line_ok():
            raise SaveFail__not_support_empty_line #not support empty_line
        may_smay_newline = sf.get_may_smay_newline()
        write_str_to_ofile_(ofile, '', may_smay_newline=may_smay_newline, flush=flush, turnoff_may_smay_newline=turnoff_may_smay_newline)
        return


    def save_cased_str_to_ofile_(sf, ofile, idx, s, /, *, flush:bool, turnoff_may_smay_newline:bool):
        'ofile -> idx -> str -> None'
        savers = sf.get_savers()
        idx = __index__(idx)
        if not 0 <= idx < len(savers): raise IndexError(idx)
        saver = savers[idx]
        saver.save_str_to_ofile_(ofile, s, flush=flush, turnoff_may_smay_newline=turnoff_may_smay_newline)
        return




class SaveStrTupleAsMultiLine:
    'read fail => ifile.tell() not changed'
    #__slots__ = ()
    #SaveStrTupleAsMultiLine(prefix4first_element, prefix4following_element, may_prefix4continue_element_line, smay4empty_tuple, may_prefix4first_comment_line, may_prefix4continue_comment_line, may_smay_newline=, empty_line_ok=)

    def __init__(sf, prefix4first_element, prefix4following_element, may_prefix4continue_element_line, smay4empty_tuple, may_prefix4first_comment_line, may_prefix4continue_comment_line, /, *, may_smay_newline, empty_line_ok:bool):
        check_type_is(bool, empty_line_ok)
        check_type_is(str, smay4empty_tuple)

        #SaveStrAsMultiLine(prefix4first_line, may_prefix4continue_line, may_smay_newline=)
        fst_hdlr = SaveStrAsMultiLine(prefix4first_element, may_prefix4continue_element_line, may_smay_newline=may_smay_newline)
        flw_hdlr = SaveStrAsMultiLine(prefix4following_element, may_prefix4continue_element_line, may_smay_newline=may_smay_newline)
        hdlrs = [fst_hdlr, flw_hdlr]
        idx4fst_hdlr = 0
        idx4flw_hdlr = 1

        check_may_str(may_prefix4first_comment_line)
        check_may_str(may_prefix4continue_comment_line)
        if may_prefix4first_comment_line is None and not may_prefix4continue_comment_line is None: raise TypeError
        if not may_prefix4first_comment_line is None:
            prefix4first_comment_line = may_prefix4first_comment_line
            cmm_hdlr = SaveStrAsMultiLine(prefix4first_comment_line, may_prefix4continue_comment_line, may_smay_newline=may_smay_newline)
            idx4cmm_hdlr = len(hdlrs)
            hdlrs.append(cmm_hdlr)
            may_idx4cmm_hdlr = idx4cmm_hdlr
        else:
            may_idx4cmm_hdlr = None
        may_idx4cmm_hdlr

        if smay4empty_tuple:
            str4empty_tuple = smay4empty_tuple
            nll_hdlr = SaveConstantStrToFile(str4empty_tuple, may_smay_newline=may_smay_newline)
            idx4nll_hdlr = len(hdlrs)
            hdlrs.append(nll_hdlr)
            may_idx4nll_hdlr = idx4nll_hdlr
        else:
            may_idx4nll_hdlr = None
        may_idx4nll_hdlr

        may_idx4cmm_hdlr
        may_idx4nll_hdlr
        hdlrs
        saver = SaveCasedStrAsMultiLine(hdlrs, empty_line_ok=empty_line_ok, may_smay_newline=may_smay_newline)

        sf._saver = saver
        sf._mi4cmm = may_idx4cmm_hdlr
        sf._mi4nll = may_idx4nll_hdlr
        _warn4may_smay_newline_(may_smay_newline)
        sf._args = (prefix4first_element, prefix4following_element, may_prefix4continue_element_line, smay4empty_tuple, may_prefix4first_comment_line, may_prefix4continue_comment_line, may_smay_newline, empty_line_ok)
    def get_args_kwargs(sf, /):
        (prefix4first_element, prefix4following_element, may_prefix4continue_element_line, smay4empty_tuple, may_prefix4first_comment_line, may_prefix4continue_comment_line, may_smay_newline, empty_line_ok) = sf._args
        (args, kwargs) = echo_args_kwargs(prefix4first_element, prefix4following_element, may_prefix4continue_element_line, smay4empty_tuple, may_prefix4first_comment_line, may_prefix4continue_comment_line, may_smay_newline=may_smay_newline, empty_line_ok=empty_line_ok)
        return (args, kwargs)
    def __repr__(sf, /):
        (args, kwargs) = sf.get_args_kwargs()
        return repr_helper(sf, *args, **kwargs)
    def rebuild_with_new_may_smay_newline_(sf, may_smay_newline, /):
        (args, kwargs) = sf.get_args_kwargs()
        del kwargs['may_smay_newline']
        cls = type(sf)
        return cls(*args, may_smay_newline=may_smay_newline, **kwargs)
    def get_may_smay_newline(sf, /):
        '-> may str # None/"" => universal_newline'
        return sf._saver.get_may_smay_newline()




    def _step_read_cased_may_comment_or_element_str_from_ifile_(sf, ifile, /, to_read_following_element):
        'ifile -> cased_x/((0, may comment) | (1, first_element/str) | (2, following_element/str) | (3, empty_tuple)) | ^ReadFail__eof | ^ReadFail__empty_line | ^ReadFail__not_found_suitable_prefix4first_line  # may_comment=None => [[empty_line_ok][empty_line found not at eof]] # ^ReadFail__empty_line => [[not empty_line_ok][empty_line found not at eof]]'
        check_type_is(bool, to_read_following_element)
        idx4fst_hdlr = 0
        idx4flw_hdlr = 1

        may_idx4cmm_hdlr = sf._mi4cmm
        may_idx4nll_hdlr = sf._mi4nll

        excluded_idc = []
        if to_read_following_element:
            excluded_idc.append(idx4fst_hdlr)
            if not may_idx4nll_hdlr is None:
                idx4nll_hdlr = may_idx4nll_hdlr
                excluded_idc.append(idx4nll_hdlr)
        else:
            excluded_idc.append(idx4flw_hdlr)

        saver = sf._saver

        m = saver.read_may_cased_str_from_ifile_(ifile, excluded_idc=excluded_idc)
            # ^ReadFail__eof
            # ^ReadFail__empty_line
            # ^ReadFail__not_found_suitable_prefix4first_line
        if m is None:
            #empty_line
            return (0, None)
        idx, s = m
        if idx == may_idx4cmm_hdlr:
            #comment
            comment = s
            return (0, comment)
        if idx == may_idx4nll_hdlr:
            #empty_tuple
            return (3, null_tuple)
        assert 0 <= idx < 2
        if idx == 1:
            #flw_hdlr
            following_element = s
            return (2, following_element)
        if idx == 0:
            #fst_hdlr
            first_element = s
            return (1, first_element)
        raise logic-err


    #def _read_lshift1_str_tuple_ex_from_ifile_(sf, ifile, /):
    #    'ifile -> (nohead_row/tuple<str>, inner_mcommentss/tuple([may comment]){len=len(nohead_row)}, outer_mcomments, begin_addr4next_row, cased_info4next_row/((0,empty_tuple/None)|(1,first_element4next_row)|(2,exc44next_row))) | ^ReadFail__eof | ^ReadFail__empty_line | ^ReadFail__not_found_suitable_prefix4first_line  # may_comment=None => [[empty_line_ok][empty_line found not at eof]] # ^ReadFail__empty_line => [[not empty_line_ok][empty_line found not at eof]]'
    #    # as-if --> ([may_comment], following_element; ...; [may_comment], ((0,empty_tuple)|(1, next row first_element)|(2,exc)))
    #def read_may_comment_or_str_tuple_ex_from_ifile_(sf, may_first_element, ifile, /):
    #    'ifile -> may comment | (row/tuple<str>, inner_mcommentss/tuple([may comment]){len=len(row)}, may_first_element4next_row) | ^ReadFail__eof | ^ReadFail__empty_line | ^ReadFail__not_found_suitable_prefix4first_line  # may_comment=None => [[empty_line_ok][empty_line found not at eof]] # ^ReadFail__empty_line => [[not empty_line_ok][empty_line found not at eof]]'
    #    # as-if --> (first_element, [may_comment]; following_element, [may_comment]; ...), may next row first_element
    #    (nohead_row, mss, _ms, begin_addr4next_row, cased_info4next_row) = sf._read_lshift1_str_tuple_ex_from_ifile_(ifile)










    def read_str_tuple_ex_from_ifile_(sf, ifile, /):
        'ifile -> (may row/tuple<str>, outer_inners_outer__mcommentss/tuple<[may comment]>{len=len(row)+1}, may_exc) | ^ReadFail__eof | ^ReadFail__empty_line | ^ReadFail__not_found_suitable_prefix4first_line  # may_comment=None => [[empty_line_ok][empty_line found not at eof]] # ^ReadFail__empty_line => [[not empty_line_ok][empty_line found not at eof]] # postcondition:[(0 if may_row is None else len(may_row))+1 == len(outer_inners_outer__mcommentss)][outer_inners_outer__mcommentss[0] or not may_row is None]'
        #assert (0 if may_row is None else len(may_row))+1 == len(outer_inners_outer__mcommentss)
        #assert outer_inners_outer__mcommentss[0] or not may_row is None


        #'ifile -> (may row/tuple<str>, may inner_mcommentss/tuple<[may comment]>{len=len(row)}, outer_mcomments/[may comment], may_exc) | ^ReadFail__eof | ^ReadFail__empty_line | ^ReadFail__not_found_suitable_prefix4first_line  # may_comment=None => [[empty_line_ok][empty_line found not at eof]] # ^ReadFail__empty_line => [[not empty_line_ok][empty_line found not at eof]] # postcondition:[outer_mcomments or not may_row is None][[may_row == ()] -> [outer_mcomments before row/empty_tuple]][[bool(may_row)] -> [outer_mcomments after row]]'

        #'ifile -> (is_empty_tuple, row/tuple<str>, inner_mcommentss/tuple<[may comment]>{len=len(row)}, outer_mcomments/[may comment], may_exc) | ^ReadFail__eof | ^ReadFail__empty_line | ^ReadFail__not_found_suitable_prefix4first_line  # may_comment=None => [[empty_line_ok][empty_line found not at eof]] # ^ReadFail__empty_line => [[not empty_line_ok][empty_line found not at eof]] # postcondition:[[is_empty_tuple or row or outer_mcomments][(may_exc is None) is is_empty_tuple]]'
        _step_read = sf._step_read_cased_may_comment_or_element_str_from_ifile_

        es = []
        mss = []
        _ms = []
        is_empty_tuple = False
        may_exc = None
        while 1:
            #saved_addr = ifile.tell()
                #for first_element of next row
            assert len(es) == len(mss)
            try:
                (case, x) = _step_read(ifile, to_read_following_element=bool(es))
                # ^ReadFail__eof
                # ^ReadFail__empty_line
                # ^ReadFail__not_found_suitable_prefix4first_line
            except (ReadFail__eof, ReadFail__empty_line, ReadFail__not_found_suitable_prefix4first_line) as exc:
            #xxx except Exception as exc:
                #cased_info4next_row = (2, exc)
                #if not es: raise
                if not (es or _ms):
                    #nothing available => ifile.tell() not changed
                    raise
                may_exc = exc
                break

            assert 0 <= case < 4
            if case == 0:
                may_comment = x
                check_may_str(may_comment)
                if 0 and not es:
                    assert not mss
                    assert not _ms
                    #outer_mcomment
                    return may_comment
                #inner_mcomment/appened-outer_mcomment
                _ms.append(may_comment)
                continue
            elif case == 3:
                #empty_tuple
                _null_tuple = x
                assert () == _null_tuple, _null_tuple
                is_empty_tuple = True
                #cased_info4next_row = (0, None)
                break
            elif case == 2:
                #flw_hdlr
                #raise ReadFail__following_element_without_first_element
                following_element = x
                check_type_is(str, following_element)
                mss.append(_ms)
                _ms = []
                es.append(following_element)
                continue
            elif case == 1:
                #fst_hdlr
                first_element = x
                check_type_is(str, first_element)
                #cased_info4next_row = (1, first_element)
                #break
                mss.append(_ms)
                _ms = []
                es.append(first_element)
                continue
            raise logic-err
        assert len(es) == len(mss)
        if 1:
            mss.append(_ms)
            _mss_ = mss; del mss
            assert len(es)+1 == len(_mss_)
        #begin_addr4next_row = saved_addr
        #return (tuple(es), tuple(mss), _ms, begin_addr4next_row, cased_info4next_row)
        #xxx assert (may_exc is None) is (not es)
        row = mk_tuple(es)
        outer_inners_outer__mcommentss = mk_tuple(_mss_)
        assert len(row)+1 == len(outer_inners_outer__mcommentss)
        assert (is_empty_tuple or row or outer_inners_outer__mcommentss[0])
            #something has been read
        #return (is_empty_tuple, row, inner_mcommentss, outer_mcomments, may_exc)

        assert (may_exc is None) is is_empty_tuple
            #empty_tuple or read until fail
        #return (is_empty_tuple, row, inner_mcommentss, outer_mcomments)
        if is_empty_tuple or row:
            may_row = row
            #may_inner_mcommentss = inner_mcommentss
        else:
            # fail but read comment or empty_line
            assert not is_empty_tuple
            assert not row
            #assert not inner_mcommentss
            #assert outer_mcomments
            assert len(outer_inners_outer__mcommentss) == 1
            assert outer_inners_outer__mcommentss[0]
            may_row = None
            #may_inner_mcommentss = None
        #assert outer_mcomments or not may_row is None
        #return (may_row, may_inner_mcommentss, outer_mcomments, may_exc)
        assert (0 if may_row is None else len(may_row))+1 == len(outer_inners_outer__mcommentss)
        assert outer_inners_outer__mcommentss[0] or not may_row is None
        return (may_row, outer_inners_outer__mcommentss, may_exc)
        #Deprecated# [may_row == ()] ==>> [outer_mcomments before row/empty_tuple]
        #Deprecated# [bool(may_row)] ==>> [outer_mcomments after row]
    read_str_tuple_ex_from_ifile_

    def iter_read_str_tuple_ex_from_ifile_(sf, ifile, /):
        'ifile -> Iter (may row/tuple<str>, outer_inners_outer__mcommentss/tuple<[may comment]>{len=len(row)+1}, may_exc) | ^ReadFail__empty_line | ^ReadFail__not_found_suitable_prefix4first_line  # may_comment=None => [[empty_line_ok][empty_line found not at eof]] # ^ReadFail__empty_line => [[not empty_line_ok][empty_line found not at eof]] # postcondition:[(0 if may_row is None else len(may_row))+1 == len(outer_inners_outer__mcommentss)][outer_inners_outer__mcommentss[0] or not may_row is None]'

        #'ifile -> Iter (may row/tuple<str>, may inner_mcommentss/tuple<[may comment]>{len=len(row)}, outer_mcomments/[may comment], may_exc) | ^ReadFail__empty_line | ^ReadFail__not_found_suitable_prefix4first_line  # may_comment=None => [[empty_line_ok][empty_line found not at eof]] # ^ReadFail__empty_line => [[not empty_line_ok][empty_line found not at eof]] # postcondition:[outer_mcomments or not may_row is None][[may_row == ()] -> [outer_mcomments before row/empty_tuple]][[bool(may_row)] -> [outer_mcomments after row]]'


        # remove: ^ReadFail__eof
        try:
            while 1:
                #(may_row, may_inner_mcommentss, outer_mcomments, may_exc) = sf.read_str_tuple_ex_from_ifile_(ifile)
                #yield (may_row, may_inner_mcommentss, outer_mcomments, may_exc)
                (may_row, outer_inners_outer__mcommentss, may_exc) = sf.read_str_tuple_ex_from_ifile_(ifile)
                yield (may_row, outer_inners_outer__mcommentss, may_exc)
        except ReadFail__eof:
            return

    def read_str_tuple_from_ifile_(sf, ifile, /):
        'ifile -> row/tuple<str> | ^ReadFail__eof | ^ReadFail__empty_line | ^ReadFail__not_found_suitable_prefix4first_line  # ^ReadFail__empty_line => [[not empty_line_ok][empty_line found not at eof]]    #discard comment, empty_line'
        with with4seekback__on_err(ifile):
            #(may_row, may_inner_mcommentss, outer_mcomments, may_exc) = sf.read_str_tuple_ex_from_ifile_(ifile)
            #assert outer_mcomments or not may_row is None
            (may_row, outer_inners_outer__mcommentss, may_exc) = sf.read_str_tuple_ex_from_ifile_(ifile)
            assert (0 if may_row is None else len(may_row))+1 == len(outer_inners_outer__mcommentss)
            assert outer_inners_outer__mcommentss[0] or not may_row is None
            if may_row is None:
                # no data available
                assert not may_exc is None
                exc = may_exc
                raise exc
            row = may_row

        check_type_is(tuple, row)
        return row  #discard comment, empty_line

    def iter_read_str_tuple_from_ifile_(sf, ifile, /):
        'ifile -> Iter row/tuple<str> | ^ReadFail__empty_line | ^ReadFail__not_found_suitable_prefix4first_line  # ^ReadFail__empty_line => [[not empty_line_ok][empty_line found not at eof]]    #discard comment, empty_line'
        # remove: ^ReadFail__eof
        try:
            while 1:
                row = sf.read_str_tuple_from_ifile_(ifile)
                yield row
        except ReadFail__eof:
            pass
        return
    def read_may_str_tuple_from_ifile_(sf, ifile, /):
        'ifile -> may row/tuple<str> # not ^ReadFail #discard comment, empty_line'
        try:
            row = sf.read_str_tuple_from_ifile_(ifile)
        except ReadFail:
            may_row = None
        else:
            may_row = row
        return may_row








    def save_header_to_ofile_(sf, ofile, /, *, flush:bool, turnoff_may_smay_newline:bool):
        sf.save_comment_to_ofile_(ofile, repr(ofile.encoding), flush=flush, turnoff_may_smay_newline=turnoff_may_smay_newline)
        sf.save_comment_to_ofile_(ofile, repr(sf), flush=flush, turnoff_may_smay_newline=turnoff_may_smay_newline)

    def save_str_tuple_to_ofile_(sf, ofile, str_tuple, /, *, flush:bool, turnoff_may_smay_newline:bool):
        'ofile -> tuple<str> -> None'
        check_type_is(tuple, str_tuple)
        if not str_tuple:
            #empty_tuple
            may_idx4nll_hdlr = sf._mi4nll
            if may_idx4nll_hdlr is None:
                raise SaveFail__not_support_empty_tuple #not support empty_tuple
            idx4nll_hdlr = may_idx4nll_hdlr
            sf._saver.save_cased_str_to_ofile_(ofile, idx4nll_hdlr, '', flush=flush, turnoff_may_smay_newline=turnoff_may_smay_newline)
            return

        idx4fst_hdlr = 0
        idx4flw_hdlr = 1
        idx = idx4fst_hdlr
        for s in str_tuple:
            sf._saver.save_cased_str_to_ofile_(ofile, idx, s, flush=flush, turnoff_may_smay_newline=turnoff_may_smay_newline)
            idx = idx4flw_hdlr
        return
    def save_comment_to_ofile_(sf, ofile, comment, /, *, flush:bool, turnoff_may_smay_newline:bool):
        'ofile -> comment/str -> None'
        #check_type_is(str, comment)
        may_idx4cmm_hdlr = sf._mi4cmm
        if may_idx4cmm_hdlr is None:
            raise SaveFail__not_support_comment #not support comment
        idx4cmm_hdlr = may_idx4cmm_hdlr
        sf._saver.save_cased_str_to_ofile_(ofile, idx4cmm_hdlr, comment, flush=flush, turnoff_may_smay_newline=turnoff_may_smay_newline)
    def save_empty_line_to_ofile_(sf, ofile, /, *, flush:bool, turnoff_may_smay_newline:bool):
        'ofile -> None'
        sf._saver.save_empty_line_to_ofile_(ofile, flush=flush, turnoff_may_smay_newline=turnoff_may_smay_newline)
#end-class SaveStrTupleAsMultiLine:
    #SaveStrTupleAsMultiLine(prefix4first_element, prefix4following_element, may_prefix4continue_element_line, smay4empty_tuple, may_prefix4first_comment_line, may_prefix4continue_comment_line, may_smay_newline=, empty_line_ok=)
std_saver4str_tuple = SaveStrTupleAsMultiLine(',', ':', '/', '()', '#', '%', may_smay_newline='\n', empty_line_ok=True)
if __name__ == "__main__":
    pass
__all__

def __():
    def split_by_universal_newline_(s, /):
        return regex4newlines.split(s)
    def split_by_newline_or_universal_newline_(may_smay_newline, s, /):
        #if may_smay_newline is None:
        if not may_smay_newline:
            return split_by_universal_newline_(s)
        newline = may_smay_newline
        return s.split(newline)
    assert split_by_universal_newline_('\r\n|\n\r-\r\t\n') == ['', '|', '-', '\t', '']

    def escape_newlines_in_str_(prefix4continue_line, s, /, *, may_smay_newline):
        check_type_is(str, prefix4continue_line)
        check_type_is(str, s)
        #if may_smay_newline is None:
        if not may_smay_newline:
            p_ = f'\n{prefix4continue_line!s}'
            def repl_(m, /):
                return p_
        else:
            def repl_(m, /):
                newline = m.group(0)
                return f'{newline!s}{prefix4continue_line!s}'
        s = regex4newlines.sub(repl_, s)
        return s
    assert escape_newlines_in_str_('/', '\r\n|\n\r|\r|\n', may_smay_newline=None) == '\n/|\n/|\n/|\n/'


    def str5strs_(ss, /, end):
        ss = map(escape_newlines_in_str_, ss)
        for head in ss:
            break
        else:
            yield '.'
        yield f',{head!s}'
        for s in ss:
            yield f',{s!s}'
        if end:
            #end = escape_newlines_in_str_(end)
            if regex4newlines.search(end):raise ValueError
            yield f'{end!s}'



from seed.str_tools.iter_split_ex_by_ import iter_split_ex_by_
from seed.io.savefile__str_tuple import iter_split_ex_by_may_smay_newline_
from seed.io.savefile__str_tuple import SaveStrTupleAsMultiLine, std_saver4str_tuple
    #SaveStrTupleAsMultiLine(prefix4first_element, prefix4following_element, may_prefix4continue_element_line, smay4empty_tuple, may_prefix4first_comment_line, may_prefix4continue_comment_line, may_smay_newline=, empty_line_ok=)
from seed.io.savefile__str_tuple import BaseFail, ReadFail, SaveFail
from seed.io.savefile__str_tuple import check_supported__may_smay_newline, regex4newlines, iter_split_ex_by_may_smay_newline_, read_until_may_smay_newline
from seed.io.savefile__str_tuple import SaveConstantStrToFile, SaveStrAsMultiLine, SaveCasedStrAsMultiLine, SaveStrTupleAsMultiLine
from seed.io.savefile__str_tuple import *
