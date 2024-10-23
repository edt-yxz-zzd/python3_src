
#e ../../python3_src/seed/seq_tools/lcp_of.py
from seed.seq_tools.is_prefix_of_seq import len_lcp_of, lcp_of
from seed.seq_tools.is_prefix_of_seq import view_seq_ex, len_lcp_of_ex
from seed.seq_tools.is_prefix_of_seq import len_lcp_of__lsls, len_lcs_of__lsls, lcp_of__lsls, lcs_of__lsls



def len_lcp_of2(xs, ys, /):
    sz = -1
    for sz, (x, y) in enumerate(zip(xs, ys)):
        if not x == y:
            break
    else:
        sz += 1
    sz
    return sz
def lcp_of2(xs, ys, /):
    sz = len_lcp_of2(xs, ys)
    return xs[:sz]


from seed.seq_tools.lcp_of import len_lcp_of2, lcp_of2
from seed.seq_tools.lcp_of import len_lcp_of, lcp_of
from seed.seq_tools.lcp_of import view_seq_ex, len_lcp_of_ex
from seed.seq_tools.lcp_of import len_lcp_of__lsls, len_lcs_of__lsls, lcp_of__lsls, lcs_of__lsls

