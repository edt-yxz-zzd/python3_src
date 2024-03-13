#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/app/sort_lines.py

why?
    since I want sort by len!

nn_ns.app.sort_lines
py -m nn_ns.app.debug_cmd   nn_ns.app.sort_lines -x
py -m nn_ns.app.doctest_cmd nn_ns.app.sort_lines:__doc__ --ndiff -ff -v
py_adhoc_call   nn_ns.app.sort_lines   @main4sort_lines_ --key=len   --may_ipath:../../python3_src/nn_ns/app/sort_lines.py

[[
py_adhoc_call   nn_ns.app.sort_lines   @main4sort_lines_ --key=len   <<here_doc
abc
1
xy
here_doc
==>>:
1
xy
abc

]]
[[
py_adhoc_call   nn_ns.app.sort_lines   @main4sort_lines_ --key=len +reverse  <<here_doc
abc
1
xy
here_doc
==>>:
abc
xy
1

]]


#]]]'''

__all__ = r'''
main4sort_lines_
    sort_lines_


content5line_
'''.split()#'''
__all__


from seed.tiny import mk_fprint
from seed.io.may_open import open4w, open4w_err, open4r
#def open4w(may_opath, /, *, force, xencoding):
#def open4r(may_ipath, /, *, xencoding):

def main4sort_lines_(*, key, reverse=False, may_ipath=None, iencoding=None, may_opath=None, force=False, oencoding=None):
    sort_lines_(**locals())
def sort_lines_(*, key, reverse, may_ipath, iencoding, may_opath, force, oencoding):
    if not key:
        key = None

    if not oencoding:
        oencoding = 'utf8'

    if not iencoding:
        iencoding = 'utf8'

    with open4r(may_ipath, xencoding=iencoding) as ifile:
        #bug: sorted(ifile, key=key)
        lines = ifile
        contents = [*map(content5line_, lines)]
    contents.sort(key=key, reverse=reverse)
    with open4w(may_opath, xencoding=oencoding, force=force) as ofile:
        fprint = mk_fprint(ofile)
        for content in contents:
            fprint(content)

def content5line_(line, /):
    if line.endswith('\n'):
        #content may contain '\n'
        content = line[:-1]
    else:
        content = line
    return content



__all__


from nn_ns.app.sort_lines import main4sort_lines_, sort_lines_
from nn_ns.app.sort_lines import *
