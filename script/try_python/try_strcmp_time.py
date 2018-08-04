
import timeit

dt = timeit.timeit

s0 = lambda:'3525'
s1 = s0()*100000000
s2 = s0()*100000000
s3 = s1
f1 = lambda: s1 == s3
f2 = lambda: s1 == s2

for f in [f1, f2]:
    print(dt(f, number=1))

    

2.4435765946414324e-06  # 'is' are used!
1.3563140308701918      # even 'str's are immutable, they don't be unified into one object.



