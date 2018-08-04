
def count_while(pred, iterable):
    i = -1
    for i, x in enumerate(iterable):
        if not pred(x):
            return i
    return i+1

