
def iter_cycle_from(forward_mapping, a):
    # hedge2iter_fake_clockwise_hedges_around_fface
    # hedge2iter_fake_clockwise_hedges_around_vertex
    b = a
    while True:
        yield b
        b = forward_mapping[b]
        if b == a: break


