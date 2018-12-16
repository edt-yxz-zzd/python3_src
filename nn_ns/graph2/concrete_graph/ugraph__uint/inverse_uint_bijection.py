
def inverse_uint_bijection(forward_mapping):
    # hedge2fake_clockwise_next_hedge_around_vertex <-> hedge2fake_clockwise_prev_hedge_around_vertex
    # hedge2fake_clockwise_next_hedge_around_fface <-> hedge2fake_clockwise_prev_hedge_around_fface
    L = len(forward_mapping)
    backward_mapping = [None]*L
    for i, o in enumerate(forward_mapping):
        assert type(o) is int and 0 <= o < L
        assert backward_mapping[o] is None
        backward_mapping[o] = i
    return tuple(backward_mapping)


