

def bin_open(file, mode, **kwargs):
    return open(file, mode+'b', **kwargs)
def txt_open(file, mode, **kwargs):
    return open(file, mode+'t', **kwargs)


