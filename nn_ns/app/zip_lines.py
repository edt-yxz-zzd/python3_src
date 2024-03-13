#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/app/zip_lines.py

[[
eg:
    file1:
        a
        b
    file2:
        x
        y
    ==>>:
    file3:
        a:x
        b:y
]]


nn_ns.app.zip_lines
py -m nn_ns.app.debug_cmd   nn_ns.app.zip_lines -x
py -m nn_ns.app.doctest_cmd nn_ns.app.zip_lines:__doc__ --ndiff -ff -v
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %nn_ns.app.zip_lines:XXX@T    =T      ++exclude_prefixes:_

py_adhoc_call   nn_ns.app.zip_lines   @main4zip_files_   :../../python3_src/nn_ns/app/zip_lines.py   :../../python3_src/nn_ns/app/zip_lines.py | less
py_adhoc_call   nn_ns.app.zip_lines   @main4fold_lines_   =2   --may_ipath:../../python3_src/nn_ns/app/zip_lines.py | less

py_adhoc_call   nn_ns.app.zip_lines   @main4zip_files_   :../../python3_src/nn_ns/app/zip_lines.py   :../../python3_src/nn_ns/app/zip_lines.py  --seps='"\n",' | less
py_adhoc_call   nn_ns.app.zip_lines   @main4fold_lines_   =2   --may_ipath:../../python3_src/nn_ns/app/zip_lines.py --seps='"\n",' | less


#]]]'''

__all__ = r'''
main4zip_files_
    zip_files_
main4fold_lines_
    fold_lines_



field5line_
mk_seps_
'''.split()#'''
__all__

from seed.tiny import mk_fprint
from seed.io.may_open import open4w, open4w_err, open4r
#def open4w(may_opath, /, *, force, xencoding):
#def open4r(may_ipath, /, *, xencoding):
from contextlib import ExitStack
from itertools import islice, zip_longest
#zip_longest(iter1 [,iter2 [...]], [fillvalue=None])

def _iter__repeat_last_(default, xs, /):
    x = default
    for x in xs:
        yield x
    while 1:
        yield x
def _prepare4open(smayencoding_path, encoding, /):
    if type(smayencoding_path) is str:
        if smayencoding_path.startswith(':'):
            if not smayencoding_path.count(':') == 2:raise ValueError(smayencoding_path)
            _, encoding, path = smayencoding_path.split(':')
        else:
            path = smayencoding_path
            encoding
        path, encoding
    return path, encoding
def _open4r(smayencoding_ipath, encoding, /):
    ipath, encoding = _prepare4open(smayencoding_ipath, encoding)
    return open4r(ipath, xencoding=encoding)
def field5line_(line, /):
    if line.endswith('\n'):
        #field may contain '\n' from default_field
        field = line[:-1]
    else:
        field = line
    return field



def main4zip_files_(*smayencoding_ipaths, iencodings=None, seps=(), seps_is_str__ok=False, may_opath=None, force=False, oencoding=None, default_field=''):
    d = {**locals()}
    del d['smayencoding_ipaths']
    return zip_files_(*smayencoding_ipaths, **d)
def zip_files_(*smayencoding_ipaths, iencodings, seps, seps_is_str__ok, may_opath, force, oencoding, default_field):
    if not default_field:
        default_field = ''
    if '\n' ==  default_field[-1:]:
        default_field += '\n'

    if not oencoding:
        oencoding = 'utf8'

    if iencodings is None:
        iencodings = ''
    elif type(iencodings) is str:
        iencodings = iencodings.split(',')
    iencodings = _iter__repeat_last_('utf8', iencodings)

    L = len(smayencoding_ipaths)
    seps = mk_seps_(L, seps, seps_is_str__ok=seps_is_str__ok)

    with ExitStack() as stack, open4w(may_opath, xencoding=oencoding, force=force) as ofile:
        ifiles = [*map(stack.enter_context, map(_open4r, smayencoding_ipaths, iencodings))]
        fprint = mk_fprint(ofile)

        if not ifiles:
            return

        for lines in zip_longest(*ifiles, fillvalue=default_field):
            fields = [*map(field5line_, lines)]
            s = ''.join(s for ss in zip(fields, seps) for s in ss)
            fprint(s)
    return




def main4fold_lines_(num_ilines_per_oline, /, *, may_ipath=None, iencoding=None, seps=(), seps_is_str__ok=False, may_opath=None, force=False, oencoding=None, default_field=''):
    d = {**locals()}
    del d['num_ilines_per_oline']
    return fold_lines_(num_ilines_per_oline, **d)
def fold_lines_(num_ilines_per_oline, /, *, may_ipath, iencoding, seps, seps_is_str__ok, may_opath, force, oencoding, default_field):
    if not default_field:
        default_field = ''
    if '\n' ==  default_field[-1:]:
        default_field += '\n'

    if not oencoding:
        oencoding = 'utf8'

    if not iencoding:
        iencoding = 'utf8'

    assert num_ilines_per_oline > 0
    L = num_ilines_per_oline
    seps = mk_seps_(L, seps, seps_is_str__ok=seps_is_str__ok)

    with open4r(may_ipath, xencoding=iencoding) as ifile, open4w(may_opath, xencoding=oencoding, force=force) as ofile:
        fprint = mk_fprint(ofile)
        it = iter(ifile)
        while 1:
            lines = [*islice(it, L)]
            if not lines:
                break
            fields = [*map(field5line_, lines)]
            if len(fields) < L:
                fields += [default_field]*(L-len(fields))
            assert len(fields) == L
            s = ''.join(s for ss in zip(fields, seps) for s in ss)
            fprint(s)
    return


def mk_seps_(num_fields_per_oline, seps, /, *, seps_is_str__ok):
    assert num_fields_per_oline >= 0
    L = num_fields_per_oline
    if type(seps) is str and not seps_is_str__ok: raise TypeError
    if L > 0:
        seps = _iter__repeat_last_(':', seps)
        seps = [*islice(seps, L-1)]
        assert len(seps)+1 == L
        seps.append('')
    else:
        seps = []
    assert len(seps) == L
    return seps


if __name__ == "__main__":
    pass
__all__


from nn_ns.app.zip_lines import main4zip_files_, main4fold_lines_
from nn_ns.app.zip_lines import zip_files_, fold_lines_
from nn_ns.app.zip_lines import *
