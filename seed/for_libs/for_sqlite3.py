#__all__:goto
r'''[[[
e ../../python3_src/seed/for_libs/for_sqlite3.py
see:
    view ../../python3_src/seed/for_libs/for_sqlite3.py
    view ../../python3_src/nn_ns/fileformat/sqlite3_dump_cmd.py
    view script/英语词霸囗.py
    view script/汉语字典囗.py
    view script/汉语辞海囗.py
    #view ../../python3_src/nn_ns/app/sqlite3_dump_.py


seed.for_libs.for_sqlite3
py -m nn_ns.app.debug_cmd   seed.for_libs.for_sqlite3 -x
py -m nn_ns.app.doctest_cmd seed.for_libs.for_sqlite3:__doc__ -ff -v
py -m nn_ns.app.doctest_cmd seed.for_libs.for_sqlite3!


py_adhoc_call   seed.for_libs.for_sqlite3   @sqlite3_dump_meta_ :/sdcard/hugh.android/GHY.DAT
[...]
py_adhoc_call   seed.for_libs.for_sqlite3   ,sqlite3_dump_meta_ :/sdcard/hugh.android/GHY.DAT
<==>
py_adhoc_call   seed.for_libs.for_sqlite3   ,str.sqlite3_iter_dump_ --ipath:/sdcard/hugh.android/GHY.DAT --nm4table:sqlite_master
(... ghy_yunghugh ...)
==>>:
py_adhoc_call   seed.for_libs.for_sqlite3   ,str.sqlite3_iter_dump_ --ipath:/sdcard/hugh.android/GHY.DAT --nm4table:ghy_yunghugh =4


py_adhoc_call   seed.for_libs.for_sqlite3   ,str.sqlite3_iter_dump_ --ipath:/sdcard/hugh.android/GHY.DAT =7

py_adhoc_call   seed.for_libs.for_sqlite3   ,str.sqlite3_iter_dump_ --ipath:/sdcard/hugh.android/GHY.DAT --nm4table:ghy_yunghugh =4 --nms4columns:zi,bsh

py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd --ipath:/sdcard/0my_files/unzip/apk/dictionary/han_yu_zi_dian-assets-x0x1x2x3/x0x1x2x3  --nm4table:zi =4 --nms4columns:zi,xiangjie --condition:'xiangjie NOT NULL'
    无


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





from seed.for_libs.for_sqlite3 import sqlite3_iter_dump_

#]]]'''
__all__ = r'''
    sqlite3_dump_meta_
    sqlite3_iter_dump_
'''.split()#'''
__all__

from seed.tiny import check_callable, echo_args
from itertools import islice, starmap
import sqlite3


def sqlite3_dump_meta_(ipath, /):
    return [*sqlite3_iter_dump_(ipath=ipath, nm4table='sqlite_master')]

#copy from:
#   view ../../python3_src/nn_ns/fileformat/sqlite3_dump_cmd.py
def sqlite3_iter_dump_(*args4islice, ipath, nm4table='', nms4columns='*', condition='', fmtr4row=None):
    if not ipath:
        ipath = None
        #ipath = sys.stdin
    if not ipath: raise TypeError
    condition = condition.strip()
    nms4columns = nms4columns.strip()
    nm4table = nm4table.strip()
    if nm4table:
        hasattr(nm4table, nm4table) #check
        if not nms4columns:
            nms4columns = '*'
        if condition:
            smay_where = f'WHERE {condition!s}'
        else:
            smay_where = ''
    if fmtr4row is None:
        fmtr4row = echo_args
    check_callable(fmtr4row)


    with sqlite3.connect(ipath) as cx:
        if not nm4table:
            it = sql_stmts = cx.iterdump()
        else:
            #it = rows = cx.execute(r'SELECT * FROM ?', [nm4table])
                #sqlite3.OperationalError: near "?": syntax error
            #it = rows = cx.execute(r'SELECT * FROM "?"', [nm4table])
                #sqlite3.OperationalError: no such table: ?
            #cu = cx.execute(fr'SELECT * FROM {nm4table!r}')
            cu = cx.execute(fr'SELECT {nms4columns!s} FROM {nm4table!r} {smay_where!s}')
            it = rows = iter(cu)
        it # Iter (sql_stmt | row)
        if args4islice:
            it = islice(it, *args4islice)
        it
        it = starmap(fmtr4row, it)
        #bug: close cx:return it
        yield from it


from seed.for_libs.for_sqlite3 import *
