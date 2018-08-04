
id = lambda x: x
flip = lambda f: lambda x: lambda y: f(y)(x)
const = lambda _: id

def from_LinkedList_to_list(linked):
    # LinkedList = () or (a, ()) or (a, (a, (...())))
    ls = []
    while (linked):
        a, linked = linked
        ls.append(a)
    assert linked == ()
    return ls
def uncurry(a2b2c):
    # (a->b->c) -> ((a,b)->c)
    return lambda a, b: a2b2c(a)(b)
def curry(a_b2c):
    # ((a,b)->c) -> (a->b->c)
    return lambda a: lambda b: a_b2c(a,b)


