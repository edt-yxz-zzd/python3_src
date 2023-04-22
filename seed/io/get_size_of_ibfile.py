#__all__:goto
r'''[[[
e ../../python3_src/seed/io/get_size_of_ibfile.py
copy from:
    view ../../python3_src/nn_ns/codec/DecodeUtils.py

seed.io.get_size_of_ibfile
py -m nn_ns.app.debug_cmd   seed.io.get_size_of_ibfile -x
py -m nn_ns.app.doctest_cmd seed.io.get_size_of_ibfile:__doc__ -v
py -m nn_ns.app.doctest_cmd seed.io.get_size_of_ibfile!
py -m nn_ns.app.adhoc_argparser__main__call8module   seed.io.get_size_of_ibfile   @f

from seed.io.get_size_of_ibfile import get_size_of_ibfile, get_size_of_ibfile_ex, explain_may_negativeable_end_locations_of_ibfile_ex, explain_negativeable_location_of_ibfile_ex, explain_may_negativeable_location_rng_of_ibfile_ex #; #may have [len(ibfile) < end_location]


#]]]'''
__all__ = r'''
    get_size_of_ibfile
        get_size_of_ibfile_ex

    explain_may_negativeable_end_locations_of_ibfile_ex
        explain_negativeable_location_of_ibfile_ex
        explain_may_negativeable_location_rng_of_ibfile_ex
'''.split()#'''
__all__

from seed.io.with4seekback import with4seekback__on_exit, with4seekback__on_err, with4seekback__on_no_err
from seed.tiny_.check import check_uint
#from seed.tiny import ifNone

from os import SEEK_CUR, SEEK_END

with4seekback__on_no_err
check_uint
SEEK_END
def get_size_of_ibfile_ex(ibfile_or_sz, /):
    'usage:ibfile_or_sz = sz = get_size_of_ibfile_ex(ibfile_or_sz)'
    if type(ibfile_or_sz) is int:
        sz = ibfile_or_sz
        check_uint(sz)
    else:
        ibfile = ibfile_or_sz
        sz = get_size_of_ibfile(ibfile)
    return sz
def get_size_of_ibfile(ibfile, /):
    with with4seekback__on_no_err(ibfile):
        ibfile.seek(0, SEEK_END)
        end_pos = ibfile.tell()
    sz = end_pos
    check_uint(sz)
    return sz


def explain_may_negativeable_end_locations_of_ibfile_ex(ibfile_or_sz, may_negativeable_end_location__may_default__pairs, /):
    '-> (ibfile_or_sz, [end_location]) #begin_location.default=0/the_curr_tell_location #end_location.default=None; #may have [len(ibfile) < end_location]'
    end_locations = []
    for may_negativeable_end_location, may_default in may_negativeable_end_location__may_default__pairs:
        if may_negativeable_end_location is None:
            if may_default is None:
                ibfile_or_sz = sz = get_size_of_ibfile_ex(ibfile_or_sz)
                default = sz
            else:
                default = may_default
            default
            negativeable_end_location = default
        else:
            negativeable_end_location = may_negativeable_end_location
        negativeable_end_location

        (ibfile_or_sz, end_location) = explain_negativeable_location_of_ibfile_ex(ibfile_or_sz, negativeable_end_location)
        end_locations.append(end_location)
    return ibfile_or_sz, end_locations







def explain_negativeable_location_of_ibfile_ex(ibfile_or_sz, negativeable_location, /):
    '-> (ibfile_or_sz, location); #may have [len(ibfile) < location]'
    if negativeable_location < 0:
        ibfile_or_sz = sz = get_size_of_ibfile_ex(ibfile_or_sz)
        location = negativeable_location + sz
    else:
        location = negativeable_location
    check_uint(location)
    return ibfile_or_sz, location
def explain_may_negativeable_location_rng_of_ibfile_ex(ibfile_or_sz, the_curr_tell_location, may_negativeable_begin_location, may_negativeable_end_location, /):
    '-> (ibfile_or_sz, (begin_location, end_location)); #may have [len(ibfile) < end_location]'
    (ibfile_or_sz, [begin_location, end_location]) = explain_may_negativeable_end_locations_of_ibfile_ex(ibfile_or_sz, [(may_negativeable_begin_location, the_curr_tell_location), (may_negativeable_end_location, None)])
    return (ibfile_or_sz, (begin_location, end_location))


from seed.io.get_size_of_ibfile import get_size_of_ibfile, get_size_of_ibfile_ex, explain_may_negativeable_end_locations_of_ibfile_ex, explain_negativeable_location_of_ibfile_ex, explain_may_negativeable_location_rng_of_ibfile_ex

from seed.io.get_size_of_ibfile import *

