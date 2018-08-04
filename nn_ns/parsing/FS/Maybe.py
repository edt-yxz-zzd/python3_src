
nothing = () # for Maybe a
def unjust(maybe_a):
    assert is_Maybe(maybe_a)
    a, = maybe_a
    return a

def just(a):
    return (a,)


def is_Maybe(obj):
    return type(obj) == tuple and len(obj) <= 1


def is_Maybe_a(obj, alphabet):
    return is_Maybe(obj) and \
           (obj == nothing or obj[0] in alphabet)
