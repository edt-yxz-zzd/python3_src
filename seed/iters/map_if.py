
def map_if(func, iterable):
    'func can be None(=eye_key); take one iterable unlike std map(f, *iterables)'
    if func is None:
        return iter(iterable)
    return map(func, iterable)
