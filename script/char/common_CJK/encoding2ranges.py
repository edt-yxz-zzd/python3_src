
__all__ = '''
    gb2312_ranges
    encoding2ranges
    iter_char_ords
    is_char_ord
    '''.split()

def sorted_ord_to_iter_ord_ranges(ords):
    ords = iter(ords)
    for begin in ords: break
    else: return

    end = begin+1
    for ord in ords:
        assert ord >= end
        if ord == end:
            end += 1
        else:
            yield (begin, end)
            begin = ord
            end = begin+1
    else:
        yield (begin, end)

    pass


def sorted_ord_to_ord_ranges(ords):
    return list(sorted_ord_to_iter_ord_ranges(ords))

assert sorted_ord_to_ord_ranges([0,1,2,4,6,7]) == [(0,3), (4,5), (6,8)]


# iter char ords
utf8 = 'utf-8'
end_of_unicode = 0x110000
def iter_all_char_ords():
    return range(end_of_unicode)
def iter_char_ords(ranges=None):
    if ranges is None:
        return iter_all_char_ords()
    for begin, end in ranges:
        yield from range(begin, end)
    pass

def is_char_ord(ord, encoding=utf8):
    try:
        ch = chr(ord)
        ch.encode(encoding)
    except:
        return False
    return True
assert is_char_ord(0)
assert not is_char_ord(end_of_unicode)


# all_char_ord_ranges
def iter_all_char_ords(encoding, ranges):
    f = lambda ord: is_char_ord(ord, encoding)
    ords = filter(f, iter_char_ords(ranges))
    return ords
def iter_all_char_ord_ranges(encoding=utf8, ranges=None):
    ords = iter_all_char_ords(encoding=encoding, ranges=ranges)
    return sorted_ord_to_iter_ord_ranges(ords)

if 0:
    all_char_ord_ranges = tuple(iter_all_char_ord_ranges())
    print(all_char_ord_ranges)
    assert all_char_ord_ranges == ((0, 55296), (57344, 1114112))
all_char_ord_ranges = ((0, 55296), (57344, 1114112))


# encoding2ranges
def encoding2ranges(encoding, ranges):
    return list(iter_all_char_ord_ranges(encoding, ranges))
def common_char_ord_ranges(encodings, ranges):
    for e in encodings:
        ranges = encoding2ranges(e, ranges)
    return ranges


def pprint_int_pair(pair):
    return '({})'.format(', '.join(map(hex, pair)))
def pprint_ranges(ranges, pair2str = pprint_int_pair):
    pairs = ranges
    pair_strs = map(pair2str, pairs)
    pairs_str = ', '.join(pair_strs)
    return '[{}]'.format(pairs_str)
assert pprint_ranges([(0, 1), (3,2)]) == '[(0x0, 0x1), (0x3, 0x2)]'



# gb2312_ranges
gb2312 = 'gb2312'
if 0:
    rngs = encoding2ranges(gb2312, all_char_ord_ranges)
    print(rngs)
    #print(pprint_ranges(gb2312_rngs))
    from pprint import pprint
    print(gb2312_rngs)
from gb2312_ranges import gb2312_ranges






