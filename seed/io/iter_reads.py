def iter_reads(fin, block_size):
    # File -> Maybe NonZeroInt -> Iter [a]{1..}
    read = fin.read
    if block_size is None or block_size < 0:
        bs = read()
        if bs: yield bs
        return

    if block_size == 0: raise ValueError
    while True:
        bs = read(block_size)
        if not bs: break
        yield bs
    return

