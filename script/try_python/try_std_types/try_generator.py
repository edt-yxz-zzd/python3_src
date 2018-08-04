
'''
return in generator function
    [7.6. The return statement]
        In a generator function, the return statement indicates that the generator is done and will cause StopIteration to be raised. The returned value (if any) is used as an argument to construct StopIteration and becomes the StopIteration.value attribute.

'''


def generator1():
    raise StopIteration('a')
    yield

def generator2():
    return 'a'
    yield

for g in [generator1, generator2]:
    assert list(g()) == []

    for _ in g():pass

        
    try:
        next(g())
        raise logic-error
    except StopIteration as e:
        assert e.args == ('a',)







