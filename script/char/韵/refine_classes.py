

from collections import defaultdict
def refine_classes__set(iterables):
    return frozenset(map(frozenset, refine_classes(iterables)))
def refine_classes(iterables):
    '''\
refine_classes :: [[a]] -> [[a]]
classes = refine_classes(objectss)
assert all(classes)
for cls in classes:
    for a, b in product(cls, cls):
        assert all(bool(a in objs) == bool(b in objs) for objs in objectss)
for cls0, cls1 in product(classes, classes):
    if cls0 is cls1: continue
    assert not all(bool(a in objs) == bool(b in objs) for objs in objectss)

'''
    return list(refine_classes__impl(iterables).values())
def refine_classes__impl(iterables):
    obj2idc = defaultdict(set)
    for i, iterable in enumerate(iterables):
        for obj in iterable:
            # multi obj ==>> use set instead of list
            obj2idc[obj].add(i)
    idc2objs = defaultdict(list)
    for obj, idc in obj2idc.items():
        idc = tuple(sorted(idc))
        idc2objs[idc].append(obj)
    return dict(idc2objs)


def _test(objectss):
    objectss = list(map(list, objectss))
    classes = refine_classes(objectss)
    for cls in classes:
        for a, b in product(cls, cls):
            assert all(bool(a in objs) == bool(b in objs) for objs in objectss)
    for cls0, cls1 in product(classes, classes):
        if cls0 is cls1: continue
        assert not all(bool(a in objs) == bool(b in objs) for objs in objectss)

def test_refine_classes__set():
    objectss = [(), (1,-1, 2,-2, 3,-3), (3,-3, 4,-4, 5,-5), (5,-5, 6,-6, 1,-1)]
    ans = [(a,-a) for a in range(1, 7)]
    ans = frozenset(map(frozenset, ans))
    assert ans == refine_classes__set(objectss)
test_refine_classes__set()


