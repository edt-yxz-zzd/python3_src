
class Counter(dict):
     def __missing__(self, key):
         return 0


c = Counter()
assert c[2] == 0
assert 2 not in c # not added to dict!!


c[2] += 1
assert 2 in c
assert c[2] == 1





