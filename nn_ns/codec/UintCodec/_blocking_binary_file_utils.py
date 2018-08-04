
def read_bytes_from_blocking_binary_file(file, n):
    assert n >= 0
    bs = file.read(n)
    if bs is None:
        raise TypeError('file should not be in non-blocking mode')
    if type(bs) is not bytes:
        raise TypeError('file should not be text mode')
    return bs
def peek_bytes_from_blocking_binary_file(file, n):
    begin = file.tell()
    try:
        return read_bytes_from_blocking_binary_file(file, n)
    finally:
        file.seek(begin)
