#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/app/search_bytes_in_file.py

nn_ns.app.search_bytes_in_file
py -m nn_ns.app.debug_cmd   nn_ns.app.search_bytes_in_file
py -m nn_ns.app.doctest_cmd nn_ns.app.search_bytes_in_file:__doc__ -v


py -m nn_ns.app.adhoc_argparser__main__call8module   nn_ns.app.search_bytes_in_file   @show_search_bytes_in_file =b'xxx' --ipath:/xxx --opath:/xxx -force
py -m nn_ns.app.search_bytes_in_file   '80 ff 99' -i /xxx -o /xxx -f
py -m nn_ns.app.search_bytes_in_file   'xxx' -e4bs ascii -i /xxx -o /xxx -f


py -m nn_ns.app.search_bytes_in_file   '676f 746f' -i ../../python3_src/nn_ns/app/search_bytes_in_file.py --show_args --format4show_address $'{0}=0x{0:X}\n'
bytes.hex("_",2): 676f_746f
bytes: b'goto'
ipath: '../../python3_src/nn_ns/app/search_bytes_in_file.py'
opath: None
force: False
format4show_address: '{0}=0x{0:X}\n'
9=0x9
746=0x2EA
900=0x384
994=0x3E2


py -m nn_ns.app.search_bytes_in_file   'goto' -e4bs ascii -i ../../python3_src/nn_ns/app/search_bytes_in_file.py --show_args --format4show_address $'{0}=0x{0:X}\n'
bytes.hex("_",2): 676f_746f
bytes: b'goto'
ipath: '../../python3_src/nn_ns/app/search_bytes_in_file.py'
opath: None
force: False
format4show_address: '{0}=0x{0:X}\n'
9=0x9
779=0x30B
986=0x3DA
1147=0x47B


0x9+len('goto') == 13 == first end_idx
py -m nn_ns.app.search_bytes_in_file   'goto' -e4bs ascii -i ../../python3_src/nn_ns/app/search_bytes_in_file.py --format4show_address $'{0}=0x{0:X}\n' --end_idx=12
<无>
py -m nn_ns.app.search_bytes_in_file   'goto' -e4bs ascii -i ../../python3_src/nn_ns/app/search_bytes_in_file.py --format4show_address $'{0}=0x{0:X}\n' --end_idx=13
9=0x9
py -m nn_ns.app.search_bytes_in_file   'goto' -e4bs ascii -i ../../python3_src/nn_ns/app/search_bytes_in_file.py --format4show_address $'{0}=0x{0:X}\n' --begin_idx=9 --end_idx=13
9=0x9
py -m nn_ns.app.search_bytes_in_file   'goto' -e4bs ascii -i ../../python3_src/nn_ns/app/search_bytes_in_file.py --format4show_address $'{0}=0x{0:X}\n' --begin_idx=10 --end_idx=13
<无>


e ../../python3_src/bash_script/app/search_bytes_in_file
py -m nn_ns.app.search_bytes_in_file "$@"
search_bytes_in_file    'goto' -e4bs ascii -i ../../python3_src/nn_ns/app/search_bytes_in_file.py --format4show_address $'{0}=0x{0:X}\n' --end_idx=13
9=0x9

search_bytes_in_file    'goto' -e4bs ascii -i ../../python3_src/nn_ns/app/search_bytes_in_file.py --format4show_address $'{0}=0x{0:X}\n' --end_idx=13 --no_overlap
9=0x9


search_bytes_in_file    'goto' -e4bs ascii -i ../../python3_src/nn_ns/app/search_bytes_in_file.py --format4show_address $'{0}=0x{0:X}\n' --end_idx=13 --fancy
9=0x9





def iter_search_bytes_in_bfile_(ibfile, bs, /, *tmay_stop_location, overlap:bool, fancy:bool):
>>> from nn_ns.app.search_bytes_in_file import get_size_of_ibfile_ex, get_size_of_ibfile, may_begin_idx2tmay_start_location_ex_, may_end_idx2tmay_stop_location_ex_, iter_search_bytes_in_bfile_, show_search_bytes_in_file, int5str, main

>>> from io import BytesIO
>>> min_block_size = 2
>>> bs = b'012aaa6789aaa'
>>> ibfile = BytesIO(bs)

>>> def list__iter_search_bytes_in_bfile_(ibfile, bs, /, *tmay_stop_location, overlap:bool, fancy:bool):
...     it = iter_search_bytes_in_bfile_(ibfile, bs, *tmay_stop_location, overlap=overlap, fancy=fancy)
...     assert it is iter(it)
...     return [*it]

>>> __ = ibfile.seek(0)
>>> list__iter_search_bytes_in_bfile_(ibfile, b'aa', 13, overlap=True, fancy=True)
[3, 4, 10, 11]
>>> __ = ibfile.seek(0)
>>> list__iter_search_bytes_in_bfile_(ibfile, b'aa', 12, overlap=True, fancy=True)
[3, 4, 10]

>>> __ = ibfile.seek(0)
>>> list__iter_search_bytes_in_bfile_(ibfile, b'aa', 13, overlap=False, fancy=True)
[3, 10]
>>> __ = ibfile.seek(0)
>>> list__iter_search_bytes_in_bfile_(ibfile, b'aa', 12, overlap=False, fancy=True)
[3, 10]




>>> __ = ibfile.seek(0)
>>> list__iter_search_bytes_in_bfile_(ibfile, b'aa', 13, overlap=True, fancy=False)
[3, 4, 10, 11]
>>> __ = ibfile.seek(0)
>>> list__iter_search_bytes_in_bfile_(ibfile, b'aa', 12, overlap=True, fancy=False)
[3, 4, 10]

>>> __ = ibfile.seek(0)
>>> list__iter_search_bytes_in_bfile_(ibfile, b'aa', 13, overlap=False, fancy=False)
[3, 10]
>>> __ = ibfile.seek(0)
>>> list__iter_search_bytes_in_bfile_(ibfile, b'aa', 12, overlap=False, fancy=False)
[3, 10]






#]]]'''
__all__ = r'''
    get_size_of_ibfile_ex
    get_size_of_ibfile
    may_begin_idx2tmay_start_location_ex_
    may_end_idx2tmay_stop_location_ex_
    iter_search_bytes_in_bfile_
    show_search_bytes_in_file
    int5str
    main
'''.split()#'''
__all__

from seed.io.find__naive import iter_find_bytes__naive_, list_find_bytes__naive_
from seed.iters.find import iter_search_subseq_on_seq, iter_search_subseq_on_stream
    #def iter_search_subseq_on_stream(istream, subseq, /, *tmay__is_stop_location_or_stop_location, overlap:bool, last_pos2restart_pos=None, _ver=None, offset=0, may_start_locations=None):
from seed.tiny_.mk_fdefault import eliminate_tmay__mix
from seed.helper.safe_eval import safe_eval, safe_exec, data_eval
    #   :: istream -> subseq -> Iter location
from seed.tiny import check_uint, check_type_is
from seed.io.may_open import open4w, open4w_err, open4r
import os
def _():
    from os import SEEK_END
_()
def get_size_of_ibfile_ex(ibfile_or_sz, /):
    if type(ibfile_or_sz) is int:
        sz = ibfile_or_sz
        check_uint(sz)
    else:
        ibfile = ibfile_or_sz
        sz = get_size_of_ibfile(ibfile)
    return sz
def get_size_of_ibfile(ibfile, /):
    curr_pos = ibfile.tell()
    if 1:
        ibfile.seek(0, os.SEEK_END)
        end_pos = ibfile.tell()
    ibfile.seek(curr_pos)

    sz = end_pos
    check_uint(sz)
    return sz
def may_begin_idx2tmay_start_location_ex_(ibfile_or_sz, may_begin_idx, /):
    '-> (tmay_start_location, ibfile_or_sz)'
    (tmay_start_location, ibfile_or_sz) = _may_idx2tmay_location_ex_(ibfile_or_sz, may_begin_idx)
    return (tmay_start_location, ibfile_or_sz)

def may_end_idx2tmay_stop_location_ex_(ibfile_or_sz, may_end_idx, /):
    '-> (tmay_stop_location, ibfile_or_sz)'
    (tmay_stop_location, ibfile_or_sz) = _may_idx2tmay_location_ex_(ibfile_or_sz, may_end_idx)
    return (tmay_stop_location, ibfile_or_sz)
def _may_idx2tmay_location_ex_(ibfile_or_sz, may_idx, /):
    '-> (tmay_location, ibfile_or_sz)'
    if may_idx is None:
        tmay_location = ()
    else:
        idx = may_idx
        check_type_is(int, idx)
        if idx < 0:
            sz = get_size_of_ibfile_ex(ibfile_or_sz)
            idx += sz
            if idx < 0: raise ValueError
            ibfile_or_sz = sz
        assert idx >= 0
        location = idx
        tmay_location = (location,)
    return (tmay_location, ibfile_or_sz)
def iter_search_bytes_in_bfile_(ibfile, bs, /, *tmay_stop_location, overlap:bool, fancy:bool):
    if not len(tmay_stop_location) <= 1: raise TypeError
    if fancy:
        return iter_search_subseq_on_stream(ibfile, bs, *tmay_stop_location, overlap=overlap)
    else:
        may_stop_location = eliminate_tmay__mix(tmay_stop_location, -1, None)
        return iter_find_bytes__naive_(bs, ibfile, may_negativeable_end_location=may_stop_location, overlap=overlap)
#bug:_fmt = r'{0}\n'
_fmt = '{0}\n'
def show_search_bytes_in_file(bs, /, *, ipath, opath=None, force=False, show_args=False, format4show_address=_fmt, may_begin_idx=None, may_end_idx=None, overlap=True, fancy=True):
    bs = bytes(bs) # [uint%256] -> bytes
    may_ipath = ipath; del ipath
    may_opath = opath; del opath
    fmt = format4show_address
    if show_args:
        print('bytes.hex("_",2):', bs.hex("_",2))
        print(f'bytes: {bs!r}')
        print(f'ipath: {may_ipath!r}' )
        print(f'opath: {may_opath!r}')
        print(f'force: {force!r}')
        print(f'format4show_address: {fmt!r}')
        print(f'begin_idx: {may_begin_idx!r}')
        print(f'end_idx: {may_end_idx!r}')

    with open4r(may_ipath, xencoding=None) as ibfile:
      if 1:
        ibfile_or_sz = ibfile
        (tmay_start_location, ibfile_or_sz) = may_begin_idx2tmay_start_location_ex_(ibfile_or_sz, may_begin_idx)
        (tmay_stop_location, ibfile_or_sz) = may_end_idx2tmay_stop_location_ex_(ibfile_or_sz, may_end_idx)
        if show_args:
            print(f'#tmay_start_location: {tmay_start_location!r}')
            print(f'#tmay_stop_location: {tmay_stop_location!r}')
        if tmay_start_location:
            [start_location] = tmay_start_location
            ibfile.seek(start_location)
      with open4w(may_opath, xencoding=None, force=force) as obfile:
        for addr in iter_search_bytes_in_bfile_(ibfile, bs, *tmay_stop_location, overlap=overlap, fancy=fancy):
            if 0:
                print(addr, file=obfile)
                    #TypeError: a bytes-like object is required, not 'str'
            if 1:
                #obfile.write(fb'{addr}\n')
                    #SyntaxError: invalid syntax
                #obfile.write(f'{addr}\n'.encode('ascii'))
                obfile.write(fmt.format(addr).encode('ascii'))
                obfile.flush()



def int5str(s, /):
    return int(safe_eval(s))
def main(args=None, /):
    import argparse
    from seed.io.may_open import open4w, open4w_err, open4r

    parser = argparse.ArgumentParser(
        description='search bytes in file'
        , epilog=''
        , formatter_class=argparse.RawDescriptionHelpFormatter
        )


    parser.add_argument('--no_overlap', action='store_true'
                        , default = False
                        , help='no_overlap: result range overlap or not;  default=False(i.e. allow overlap)')
    parser.add_argument('--fancy', action='store_true'
                        , default = False
                        , help='fancy using seed.iters.find:iter_search_subseq_on_stream; not fancy using seed.io.find__naive:iter_find_bytes__naive_;  default=False')


    parser.add_argument('-begin', '--begin_idx', type=int5str
                        , default=None
                        , help=f'begin location to start search')
    parser.add_argument('-end', '--end_idx', type=int5str
                        , default=None
                        , help=f'end location to stop search')
    parser.add_argument('-fmt', '--format4show_address', type=str
                        , default=_fmt
                        , help=f'format string used to show address found; default={_fmt!r}')
    parser.add_argument('-e4bs', '--encoding4bytes', type=str
                        , default=''
                        , help='encoding for the input bytes; default=""(using py.bytes.fromhex())')
    parser.add_argument('bytes', type=str
                        , help='the input bytes to search')
    parser.add_argument('-i', '--input', type=str, default=None
                        , help='input file path')
    parser.add_argument('-o', '--output', type=str, default=None
                        , help='output file path')
    parser.add_argument('-f', '--force', action='store_true'
                        , default = False
                        , help='open mode for output file')
    parser.add_argument('--show_args', action='store_true'
                        , default = False
                        , help='show actual args in use')

    args = parser.parse_args(args)
    may_ifname = args.input
    may_ofname = args.output
    force = args.force
    show_args = args.show_args
    format4show_address = args.format4show_address
    may_begin_idx = args.begin_idx
    may_end_idx = args.end_idx
    overlap = not args.no_overlap
    fancy = args.fancy

    encoding4bytes = args.encoding4bytes
    str4bytes = args.bytes
    if not encoding4bytes:
        bs = bytes.fromhex(str4bytes)
    else:
        bs = str4bytes.encode(encoding4bytes)

    show_search_bytes_in_file(bs, ipath=may_ifname, opath=may_ofname, force=force, show_args=show_args, format4show_address=format4show_address, may_begin_idx=may_begin_idx, may_end_idx=may_end_idx, overlap=overlap, fancy=fancy)
if __name__ == "__main__":
    main()

