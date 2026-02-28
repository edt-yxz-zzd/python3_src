


from operator import __index__# __contains__ #no:__int__

def to_may_int_(x, /):
    try:
        return __index__(x)
    except TypeError:
        pass
    try:
        #0 < x
            #TypeError: '<' not supported between instances of 'complex' and 'int'
        0 == x
        i = int(x)
    except (TypeError, ValueError):
        return None
    if not i in [x]:
        return None
    return i


from seed.tiny_.to_may_int_ import to_may_int_
