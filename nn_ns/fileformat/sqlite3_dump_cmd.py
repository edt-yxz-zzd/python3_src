#__all__:goto
r"""[[[
e ../../python3_src/nn_ns/fileformat/sqlite3_dump_cmd.py
see:
    view ../../python3_src/seed/for_libs/for_sqlite3.py
    view ../../python3_src/nn_ns/fileformat/sqlite3_dump_cmd.py
    view script/英语词霸囗.py
    view script/汉语字典囗.py
    view script/汉语辞海囗.py
    #view ../../python3_src/nn_ns/app/sqlite3_dump_.py


nn_ns.fileformat.sqlite3_dump_cmd
py -m nn_ns.app.debug_cmd   nn_ns.fileformat.sqlite3_dump_cmd -x
py -m nn_ns.app.doctest_cmd nn_ns.fileformat.sqlite3_dump_cmd:__doc__ -ff -v
py -m nn_ns.app.doctest_cmd nn_ns.fileformat.sqlite3_dump_cmd!

from nn_ns.fileformat.sqlite3_dump_cmd import sqlite3_dump_cmd, sqlite3_dump_, sqlite3_iter_dump_


py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd



view script/汉语字典囗.py
#builtin table
py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd --ipath:/sdcard/hugh.android/GHY.DAT --nm4table:sqlite_master
('table', 'android_metadata', 'android_metadata', 2, 'CREATE TABLE android_metadata(locale text)')
('table', 'ghy_yunghugh', 'ghy_yunghugh', 3, 'CREATE TABLE ghy_yunghugh (\r\n_id INTEGER primary key,\r\nzi text,\r\nyinjie text,\r\nbs text,\r\nbsbh text,\r\nzbh text,\r\nbsh text,\r\nshiyi text)')


#userdef table
py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd --ipath:/sdcard/hugh.android/GHY.DAT --nm4table:ghy_yunghugh =600 =602
py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd --ipath:/sdcard/hugh.android/GHY.DAT =6


py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd --ipath:/sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian-assets-x0x1x2x3/x0x1x2x3  --nm4table:sqlite_master
<==>
py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   ,str.sqlite3_dump_cmd --ipath:/sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian-assets-x0x1x2x3/x0x1x2x3  --nm4table:sqlite_master --opath=...
<=?=> #eqv only if output row not sql_stmt # repr<T> vs str<T> for T=tuple|str
py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   ,sqlite3_dump_cmd --ipath:/sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian-assets-x0x1x2x3/x0x1x2x3  --nm4table:sqlite_master --opath=...
('table', 'android_metadata', 'android_metadata', 2, 'CREATE TABLE android_metadata (locale TEXT)')
('table', 'zi', 'zi', 3, 'CREATE TABLE zi (id INTEGER primary key autoincrement,zi TEXT,py TEXT,wubi TEXT,bushou TEXT,bihua int,pinyin TEXT,jijie TEXT,xiangjie TEXT,bishun TEXT)')
('table', 'sqlite_sequence', 'sqlite_sequence', 4, 'CREATE TABLE sqlite_sequence(name,seq)')



view script/汉语辞海囗.py
py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd \
 '%!may2smay=lambda m:(str(m) if m else "")' \
 '%!std4NL_=lambda s:(s.replace("\r\n", "\n").replace("\r", "\n"))' \
 '%!strips=lambda s:("\n".join(map(str.strip,s.split("\n"))))' \
 '%!s_=lambda s:(strips(std4NL_(may2smay(s))).replace("\n", "\n/"))' \
 '%!d_=lambda hexs:(bytes.fromhex(hexs).decode("u8"))' \
 --ipath:/sdcard/zidian/cihai/cihai.dat \
 --nm4table:hanyu \
 --nms4columns:ciyu,content \
 --fmtr4row='(lambda ciyu,content:f",{d_(ciyu)}\n:{s_(content)}")' \
 --opath:/sdcard/0my_files/tmp/out4py/汉语辞海囗.py..nn_ns.fileformat.sqlite3_dump_cmd.out.txt







echo "INSERT INTO 'xxx' VALUES('\"\"', \"''\");" | py -m sqlparse -
INSERT INTO 'xxx' VALUES('""', "''");
    ??? 『''』未变

>>> import sqlite3
>>> cx = sqlite3.connect(':memory:')
>>> cx.executescript(r'''BEGIN TRANSACTION; CREATE TABLE xxx (txt text); COMMIT; ''')
>>> __ = cx.executescript(r'''BEGIN TRANSACTION; INSERT INTO xxx VALUES('\t"''\0'); INSERT INTO xxx VALUES("\t'""\0"); COMMIT; ''')
>>> for x in cx.iterdump():print(x)
BEGIN TRANSACTION;
CREATE TABLE xxx (txt text);
INSERT INTO "xxx" VALUES('\t"''\0');
INSERT INTO "xxx" VALUES('\t''"\0');
COMMIT;
>>> __ = cx.executescript(r'''BEGIN TRANSACTION; SELECT * FROM xxx; COMMIT; ''')
>>> __ = cx.executescript(r''' SELECT * FROM xxx;  ''')
>>> for row in cx.execute(r''' SELECT * FROM xxx;  '''):print(row) #raw-string???
('\\t"\'\\0',)
('\\t\'"\\0',)
>>> cu = cx.cursor()
>>> __ = cu.execute('INSERT INTO xxx VALUES(?)', ['\t\0']) #can but neednot 『;』
>>> for row in cx.execute(r''' SELECT * FROM xxx;  '''):print(row) #not only raw-string
('\\t"\'\\0',)
('\\t\'"\\0',)
('\t\x00',)
>>> cx.close()




#]]]"""
__all__ = r'''
    sqlite3_dump_cmd
        sqlite3_dump_
            sqlite3_iter_dump_
'''.split()#'''
__all__

__all__

from seed.for_libs.for_sqlite3 import sqlite3_iter_dump_
from seed.for_libs.for_builtins.py_help import py_help_, py_help
from seed.io.may_open import open4w, open4w_err, open4r
from seed.tiny import check_type_is, echo, print_err, mk_fprint, mk_assert_eq_f, expectError
import re
from ast import literal_eval
from itertools import islice
import sqlite3

def __():
    class FormatError(Exception):pass
    regex4sql_stmt__INSERT_INTO = re.compile(r'(?:\s+ INSERT \s+ INTO \s+ (?P<nm4tbl>"[^"]*") \s+ VALUES \s+ (?P<row>[(] .* [)]) \s+ ; \s+)', re.DOTALL|re.MULTILINE|re.VERBOSE|re.IGNORECASE)
    def unescape__sql_stmt_(sql_stmt, /):
        raise DeprecationWarning('see: sqlite3_dump_()::using SELECT FROM')
        check_type_is(str, sql_stmt)
        s = sql_stmt
        if '""' in s: raise NotImplementedError
        #bug:s = s.replace("''", "'")
        s = s.replace("\\", r"\\")
            #『\』-->『\\』--->『\』
        s = s.replace("''", r"\'")
            #『''』-->『\'』--->『'』
        return s
    def eval__sql_stmt__INSERT_INTO_(sql_stmt, /):
        raise DeprecationWarning('see: sqlite3_dump_()::using SELECT FROM')
        s = unescape__sql_stmt_(sql_stmt)
        m = regex4sql_stmt__INSERT_INTO.fullmatch(s)
        if m is None: raise FormatError(f'{s!r}')
        nm4tbl = literal_eval(m['nm4tbl'])
        row = literal_eval(m['row'])
        return nm4tbl, row

if 0:
    __xxx = True
def sqlite3_dump_cmd(*args, **kwds):
    'see:sqlite3_dump_'
    #def sqlite3_dump_cmd(*args4islice, ipath, opath, force=False):
    global __xxx
    __xxx = True
    try:
        return sqlite3_dump_(*args, **kwds)
        #return sqlite3_dump_(*args4islice, ipath=ipath, opath=opath, force=force)
    except TypeError as e:
        if __xxx:
            #err_msg = help(sqlite3_dump_)
            [err_msg] = e.args
            #err_msg += r'  # sqlite3_dump_(*args4islice, ipath, opath, force=False)'
            err_msg = f'{err_msg}\n{__help4sqlite3_dump_}'
            print_err(err_msg)
            raise TypeError(err_msg) from e
        raise
    raise 000

Ellipsis
def sqlite3_dump_(*args4islice, ipath, opath=None, force=False, nm4table='', nms4columns='*', condition='', fmtr4row=None) -> '(Iter (sql_stmt if not nm4table else row)) if opath is Ellipsis else None':
    'opath=Ellipsis => return iterator; opath=None => print result to sys.stdout'
    global __xxx
    __xxx = False

    it = sqlite3_iter_dump_(*args4islice, ipath=ipath, nm4table=nm4table, nms4columns=nms4columns, condition=condition, fmtr4row=fmtr4row)

    if ... is opath:
        return it

    if not opath:
        opath = None #==>> sys.stdout
    with open4w(opath, xencoding='u8', force=force) as fout:
        fprint = mk_fprint(fout)
        for sql_stmt__or__row in it:
            fprint(sql_stmt__or__row)

def __():
  #moved to seed.for_libs.for_sqlite3
  def sqlite3_iter_dump_(*args4islice, ipath, nm4table=''):
    if not ipath:
        ipath = None
        #ipath = sys.stdin
    if not ipath: raise TypeError

    with sqlite3.connect(ipath) as cx:
        if not nm4table:
            it = sql_stmts = cx.iterdump()
        else:
            hasattr(nm4table, nm4table) #check
            #it = rows = cx.execute(r'SELECT * FROM ?', [nm4table])
                #sqlite3.OperationalError: near "?": syntax error
            #it = rows = cx.execute(r'SELECT * FROM "?"', [nm4table])
                #sqlite3.OperationalError: no such table: ?
            cu = cx.execute(fr'SELECT * FROM {nm4table!r}')
            it = rows = iter(cu)
        it # Iter (sql_stmt | row)
        if args4islice:
            it = islice(it, *args4islice)
        it
        #bug: close cx:return it
        yield from it

__help4sqlite3_dump_ = py_help_(sqlite3_dump_)


from nn_ns.fileformat.sqlite3_dump_cmd import sqlite3_dump_cmd, sqlite3_dump_, sqlite3_iter_dump_
from nn_ns.fileformat.sqlite3_dump_cmd import *
if __name__ == "__main__":
    pass
