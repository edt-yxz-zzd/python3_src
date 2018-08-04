raise:
class CyclicDeque:
    def __init__(self, max_len, buffer, begin, end, data_begin, data_end):
        # begin + max_len + 1 == end
        # use buffer[begin:end] only
        # begin <= data_begin < end
        # begin <= data_end < end
        # data_size = (data_end - data_begin)%(end-begin)
        if not begin < end:
def iter_block(iterable, n):
    # iter_block(ls, 3) == zip(ls, ls[1:], ls[2:])


def all_eq(iterable, eq):
    iterable

