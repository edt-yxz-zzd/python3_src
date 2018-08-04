
def uint2ms0b_idx(u, min_len_bits=None):
    # ms0b == most significant 0 bit after msb or 1<<min_len_bits
    assert u >= 0
    L = u.bit_length()
    if min_len_bits is not None:
        L = max(L, min_len_bits)
    all_1s = (1 << L) - 1 # maybe 0
    flipped = all_1s & ~u
    return flipped.bit_length() - 1 # maybe -1

def test_uint2ms0b_idx():
    data = [
        (0, -1),
        (1, -1),
        (0b10, 0),
        (0b11, -1),
        (0b100, 1),
        (0b101, 1),
        (0b110, 0),
        (0b111, -1),
        (0b1000, 2),
        (0b1001, 2),
        ]
    for u, ans in data:
        assert uint2ms0b_idx(u) == ans
test_uint2ms0b_idx()
