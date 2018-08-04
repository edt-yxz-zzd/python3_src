
__all__ = '''
    mkSubSeqTransformView
    mkSubSeqTransformView_or_notView
    '''.split()

from .SeqSliceView import SeqSliceView
from .SeqTransformView import SeqTransformView
from .View import SeqView

def mkSubSeqTransformView(transform, seq, range_or_slice):
    # result is a view, not a concrete subseq
    # so, even range_or_slice is None, we should not avoid SeqSliceView
    # see: mk_slice
    if transform is None is range_or_slice:
        return SeqView(seq)

    subseq_view = seq
    if transform is not None:
        subseq_view = SeqTransformView(transform, subseq_view)
    if range_or_slice is not None:
        subseq_view = SeqSliceView(subseq_view, range_or_slice)

    return subseq_view

def mkSubSeqTransformView_or_notView(transform, seq, range_or_slice):
    # result is a view or not a view
    # see: mk_slice
    while range_or_slice is not None:
        L = len(seq)
        if isinstance(range_or_slice, range):
            rng = range_or_slice
            if rng == range(L):
                break
        else:
            sl = range_or_slice
            if sl.indices(L) == (0, L, 1):
                break
        return mkSubSeqTransformView(transform, seq, range_or_slice)
    del range_or_slice

    subseq = seq
    if transform is not None:
        subseq = SeqTransformView(transform, subseq)
    return subseq

