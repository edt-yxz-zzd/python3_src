#__all__:goto
r'''[[[
e ../../python3_src/nn_ns/fileformat/png/simple_reader_writer4png__draw.py
TODO:
    view others/数学/编程/设计/设计冫图纸格式.txt

nn_ns.fileformat.png.simple_reader_writer4png__draw
py -m nn_ns.app.debug_cmd   nn_ns.fileformat.png.simple_reader_writer4png__draw -x # -off_defs
py -m nn_ns.app.doctest_cmd nn_ns.fileformat.png.simple_reader_writer4png__draw:__doc__ -ht # -ff -df
py_adhoc_call  seed.helper.print_methods  @wrapped_print_methods   %nn_ns.fileformat.png.simple_reader_writer4png__draw:cls@T    =T   +exclude_attrs5listed_in_cls_doc
#######
from seed.pkg_tools.ModuleReloader import mk_doctestXmodule_reloader_
doctestXmodule_reloader = mk_doctestXmodule_reloader_('', 'nn_ns.fileformat.png.simple_reader_writer4png__draw:__doc__', '-ht')
doctestXmodule_reloader(reload_first=False)
doctestXmodule_reloader()
#######

[[
]]


'#'; __doc__ = r'#'
>>>


画图制表冫三基色灬扌(may_obfile_or_opath8png_file, /, width4macro_pixel, height4macro_pixel, sample_depth, samples4R, samples4G, samples4B, samples4A, *, may_pixel7RGB8background_color4src=None, interlace_method=1, force=False)
py_adhoc_call   nn_ns.fileformat.png.simple_reader_writer4png__draw   @画图制表冫三基色各自五等分扌   :/sdcard/0my_files/tmp/out4py/image/nn_ns.fileformat.png.simple_reader_writer4png__draw..画图制表冫三基色各自五等分扌.out.png

from nn_ns.fileformat.png.simple_reader_writer4png__draw import *
]]]'''#'''
__all__ = r'''
mk_max_sample5depth_
check_samples_
check_pint_31bit_
画图制表冫三基色灬扌
    画图制表冫三基色各自五等分扌
    制表冫三基色灬扌
        mk_mx_
        pixel7RGBA8trns_blk
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
#.#################################
#.from functools import cached_property
from itertools import product #islice
from seed.tiny_.check import check_type_is, check_int_ge, check_int_ge_lt, check_int_ge_le, check_all_
#see:dot_#from seed.func_tools.dot2 import dot
#.
#.from abc import update_abstractmethods
#.from seed.abc.abc__ver1 import abstractmethod, override, ABC
#.#################################
#.from seed.for_libs.for_importlib__reload import clear_later_variables_if_reload_
#.clear_later_variables_if_reload_(globals(), '')
#.    # <<== seed.pkg_tools.ModuleReloader
#.
#.#################################
#.from seed.helper.lazy_import__func7context import mk_ctx4lazy_import8lazy_objs__ver2_
#.with mk_ctx4lazy_import8lazy_objs__ver2_(nonexistent_prefix4qnm4mdl8src='__.', prefix4attr='lazy_', suffix4attr=''):
#.    from __.seed.tiny_.containers import lazy_null_tuple,lazy_null_iter,lazy_null_frozenset as _lazy_null_frozenset_ #null_tuple,null_iter,null_frozenset
#.#################################
#.from seed.helper.lazy_import__func import force_lazy_imported_func_ # lazy_import4func_, lazy_import4funcs_
from seed.helper.lazy_import__func7context import mk_ctx4lazy_import4funcs_ #NOTE:not support "as"
#.with mk_ctx4lazy_import4funcs_(__name__, 'ifNone:_ifNone, ifNonef:_ifNonef'):
#.    from seed.helper.ifNone import ifNone as _ifNone, ifNonef as _ifNonef
with mk_ctx4lazy_import4funcs_(__name__):
    from seed.tiny_.containers import mk_tuple,mk_immutable_seq#mk_immutable_seq5iterT_,mk_immutable_seq5iter__,mk_bytes5iter_,mk_tuple__split_first_if_str #xxx:null_tuple
    from nn_ns.fileformat.png.simple_reader_writer4png import dump_png_file__pixel_matrix7RGBA4src_
#.    from seed.helper.repr_input import repr_helper
#.    from seed.tiny_.types5py import mk_MapView,curry1,kwargs2Attrs #,MapView
#.    from seed.debug.print_err import print_err
#.    from seed.helper.ifNone import ifNone,ifNonef
#.    from seed.tiny_.funcs import echo,fst,snd
#.    from seed.types.Either import mk_Left,mk_Right #Either,Cased
#.    from seed.iters.flatten_recur import flatten_recur
#.    # def flatten_recur(g:Generator, /, *, value:object=None, is_exc=False, boxed=False):
#.    from seed.func_tools.dot_ import dot_
#.    from seed.iters.PeekableIterator import echo_or_mk_PeekableIterator
#.    from seed.for_libs.for_collections.namedtuple__nontuple4cached_property import mk_named_pseudo_tuple_
#.    #def mk_named_pseudo_tuple_(__module__,typename, field_names, /):
#.    #    def _check6make_(sf, /):
#.    from seed.for_libs.for_collections.namedtuple__nontuple4cached_property import collect_tuple_subclasses_with_cached_property
#.    #assert not (__:=collect_tuple_subclasses_with_cached_property(globals(), to_print_err=True)), __
#.#################################
#.:s/\v^from +([_[:alnum:].]+) +import +([^# ]( *[^# ])*).*/lazy_import4funcs_('\1', '\2', __name__)\rif 0:\0



#.#################################
#.from seed.types.LazyList import ToConcatLazyList, decorator4protocol4ToConcatLazyList_
#.from seed.types.LazyList import LazyList, LazyListError
#.from seed.types.LazyList import to_LazyList, to_LazyListIter
#.
#.from seed.tiny_._Base4repr import _Base4repr
        #sf._reset4repr(may_args4repr, may_kwds4repr)
        #sf._init4repr(*args4repr, **kwds4repr)
#.#################################
___end_mark_of_excluded_global_names__0___ = ...

#.class __(ABC):
#.    __slots__ = ()
#.    ___no_slots_ok___ = True
#.    def __repr__(sf, /):
#.        return repr_helper(sf, *args, **kwargs)
#.if __name__ == "__main__":
#.    raise NotImplementedError(Exception, StopIteration)

__all__



def mk_max_sample5depth_(sample_depth, /):
    return (1<<sample_depth) -1
def check_samples_(max_sample, samples, /):
    check_all_([check_int_ge_le, 0, max_sample], samples)
def check_pint_31bit_(u, /):
    check_int_ge_lt(1, 0x80_00_00_00, u)

def mk_mx_(width, height, v, /):
    mx = [[v]*width for _ in range(height)]
    return mx
def 画图制表冫三基色各自五等分扌(may_obfile_or_opath8png_file, /, *, width4macro_pixel=16, height4macro_pixel=16, force=False):
    samples = (0, 64, 128, 192, 255)
    画图制表冫三基色灬扌(may_obfile_or_opath8png_file, width4macro_pixel, height4macro_pixel, sample_depth:=8, samples4R:=samples, samples4G:=samples, samples4B:=samples, samples4A:=samples, may_pixel7RGB8background_color4src=None, interlace_method=1, force=force)

pixel7RGBA8trns_blk = (0,)*4
def 画图制表冫三基色灬扌(may_obfile_or_opath8png_file, /, width4macro_pixel, height4macro_pixel, sample_depth, samples4R, samples4G, samples4B, samples4A, *, may_pixel7RGB8background_color4src=None, interlace_method=1, force=False):
    (mx7RGBA, (wh_size4canvas, samples4R, samples4G, samples4B, samples4A)) = 制表冫三基色灬扌(width4macro_pixel, height4macro_pixel, sample_depth, samples4R, samples4G, samples4B, samples4A)
    jrow2pixels7RGBA7src_image = mx7RGBA
    sample_depths7RGBA4src = (sample_depth,)*4
    dump_png_file__pixel_matrix7RGBA4src_(may_obfile_or_opath8png_file, wh_size4canvas, sample_depths7RGBA4src, jrow2pixels7RGBA7src_image, may_pixel7RGB8background_color4src=may_pixel7RGB8background_color4src, interlace_method=interlace_method, force=force)
def 制表冫三基色灬扌(width4macro_pixel, height4macro_pixel, sample_depth, samples4R, samples4G, samples4B, samples4A, /):
    check_pint_31bit_(width4macro_pixel)
    check_pint_31bit_(height4macro_pixel)
    check_int_ge_le(1, 16, sample_depth)
    samples4R = mk_immutable_seq(samples4R)
    samples4G = mk_immutable_seq(samples4G)
    samples4B = mk_immutable_seq(samples4B)
    samples4A = mk_immutable_seq(samples4A)

    if not samples4R:raise Exception
    if not samples4G:raise Exception
    if not samples4B:raise Exception
    if not samples4A:raise Exception

    max_sample = mk_max_sample5depth_(sample_depth)
    check_samples_(max_sample, samples4R)
    check_samples_(max_sample, samples4G)
    check_samples_(max_sample, samples4B)
    check_samples_(max_sample, samples4A)

    num_macro_pixels4row = len(samples4R)*len(samples4G)
    num_macro_pixels4column = len(samples4B)*len(samples4A)
    width4canvas = width4macro_pixel * num_macro_pixels4column
    height4canvas = height4macro_pixel * num_macro_pixels4row
    check_pint_31bit_(width4canvas)
    check_pint_31bit_(height4canvas)
    wh_size4canvas = (width4canvas, height4canvas)
    mx7RGBA = mk_mx_(width4canvas, height4canvas, pixel7RGBA8trns_blk)
    for jrow4macro, RG in enumerate(product(samples4R, samples4G)):
        jrow = jrow4macro*height4macro_pixel
        rows7RGBA = mx7RGBA[jrow:jrow+height4macro_pixel]
        for row7RGBA in rows7RGBA:
            for jcolumn4macro_pixel, BA in enumerate(product(samples4B, samples4A)):
                jcolumn = jcolumn4macro_pixel*width4macro_pixel
                _jcolumn = jcolumn+width4macro_pixel
                pixel7RGBA = (*RG, *BA)
                pixels7RGBA = [pixel7RGBA]*width4macro_pixel
                row7RGBA[jcolumn:_jcolumn] = pixels7RGBA

    return (mx7RGBA, (wh_size4canvas, samples4R, samples4G, samples4B, samples4A))











__all__
from nn_ns.fileformat.png.simple_reader_writer4png__draw import *
