
r'''[[[
e ../../python3_src/seed/for_libs/for_sqlite3--py_adhoc_call.py




[[
fail: .db 不是 sqlite3
    mandoc.db - manual page database
    MANDOC.DB(5):File Formats Manual
<<==:
ipath=~/../usr/share/man/mandoc.db
du -h "$ipath"
    860K
py_adhoc_call   seed.for_libs.for_sqlite3   @sqlite3_dump_meta_ :"$ipath"
    sqlite3.DatabaseError: file is not a database

head -c 200 "$ipath" | od -A x -t x1z -v
tail -c 200 "$ipath" | od -A x -t x1z -v
od -A x -t x1z -v -j 0 -N 200 "$ipath"
od -A x -t x1z -v -j $(($(stat -c %s "$ipath") - 200)) -N 200 "$ipath"
hexdump -C -s 0 -n 200 "$ipath"
hexdump -C -s $(($(stat -c %s "$ipath") - 200)) -n 200 "$ipath"
hexdump -C -s-200 -n 200 "$ipath"
    hexdump: failed to parse offset: '-200': Invalid argument

tar --list -f "$ipath"
    tar: This does not look like a tar archive
    tar: Skipping to next header
    tar: Exiting with failure status due to previous errors


]]


模板
(py_adhoc_call   nn_ns.fileformat.sqlite3_dump_cmd   @sqlite3_dump_cmd
 '%!may2smay=lambda m:(str(m) if m else "")'
 '%!std4NL_=lambda s:(s.replace("\r\n", "\n").replace("\r", "\n"))'
 '%!strips=lambda s:("\n".join(map(str.strip,s.split("\n"))))'
 '%!s_=lambda s:(strips(std4NL_(may2smay(s))).replace("\n", "\n/"))'
 '%!d_=lambda hexs:(bytes.fromhex(hexs).decode("u8"))'
 --ipath:AAA
 --nm4table:XXX
 --nms4columns:YYY,ZZZ
 --fmtr4row='(lambda YYY,ZZZ:f",{d_(YYY)}\n:{s_(ZZZ)}")'
 --opath:BBB
)



#]]]'''#'''
