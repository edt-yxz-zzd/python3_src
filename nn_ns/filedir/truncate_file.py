

'''
see:
    os.truncate
        size_of(result) <= size
        # never extend??
    io.IOBase.truncate
        size_of(result) == size
        # pad bytes if extend
'''

