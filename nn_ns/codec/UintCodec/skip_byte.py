
__all__ = '''
    skip_until
    skip_byte
    '''.split()

def skip_until(file, *, pred, size=1):
    while True:
        bs = file.read(size)
        if not bs:
            # EOF
            break
        if pred(bs):
            break
    return bs

def skip_byte(file, byte):
    begin = file.tell()
    b = skip_until(file, pred = lambda bs: bs != byte)
    end = file.tell()
    size = end - begin - len(b)
    return b, size


    
    
    
