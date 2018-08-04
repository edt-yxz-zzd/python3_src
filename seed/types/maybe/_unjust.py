

def unjust(a):
    if not a:
        raise ValueError("unjust Nothing")
    x, = a
    return x
