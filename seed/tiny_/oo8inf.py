#__all__:goto
r'''[[[
e ../../python3_src/seed/tiny_/oo8inf.py

seed.tiny_.oo8inf
py -m nn_ns.app.debug_cmd   seed.tiny_.oo8inf -x
py -m nn_ns.app.doctest_cmd seed.tiny_.oo8inf:__doc__ -ht
py_adhoc_call   seed.tiny_.oo8inf   @f


[[
[infinity == +oo]
[infinitesimal == 1/+oo]
    # cancel: [1/+oo == +o0o]

(+oo) is used by:
    min_oolen@sentence@rule @Grammar

(1/+oo + terminal_symbol) is used by:
    boundary@interval@rngs_based_set @Regex
]]





>>> oo
OO4repr()

>>> inf__pos
(+oo)
>>> inf__neg
(-oo)
>>> +oo
(+oo)
>>> -oo
(-oo)

>>> -oo is inf__neg
True
>>> +oo is inf__pos
True
>>> +oo is -oo
False

>>> +oo <= -oo
False
>>> +oo < -oo
False
>>> +oo >= -oo
True
>>> +oo > -oo
True
>>> +oo == -oo
False
>>> +oo != -oo
True

>>> pp = (+oo, +999)
>>> nn = (-oo, -999)
>>> ee = (0, 0)
>>> ls = [pp, nn]
>>> for (x,a) in ls:
...  for (y,b) in ls:
...   assert (x==y) is (a==b)
...   assert (x!=y) is (a!=b)
...   assert (x<=y) is (a<=b)
...   assert (x>=y) is (a>=b)
...   assert (x<y) is (a<b)
...   assert (x>y) is (a>b)


>>> ++oo
(+oo)
>>> -+oo
(-oo)
>>> abs(+oo)
(+oo)

>>> +-oo
(-oo)
>>> --oo
(+oo)
>>> abs(-oo)
(+oo)




>>> +oo + +oo
(+oo)
>>> +oo - +oo
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.Error__NaN
>>> +oo * +oo
(+oo)
>>> +oo / +oo
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.Error__NaN
>>> +oo // +oo
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.Error__NaN




>>> fpp = float('inf')
>>> fnn = float('-inf')
>>> fpp
inf
>>> fnn
-inf


>>> fpp + fpp
inf
>>> fpp - fpp
nan
>>> fpp * fpp
inf
>>> fpp / fpp
nan
>>> fpp // fpp
nan


>>> 999 // fpp
0.0
>>> 999 // fnn
-1.0
>>> (-999) // fpp
-1.0
>>> divmod(-999, fpp)
(-1.0, inf)
>>> fpp // 999 #py-bug!!!
nan
>>> fpp // -999 #py-bug!!!
nan
>>> divmod(fpp, 999) #py-bug!!!
(nan, nan)
>>> divmod(fpp, -999) #py-bug!!!
(nan, nan)
>>> fnn // 999 #py-bug!!!
nan
>>> fnn // -999 #py-bug!!!
nan
>>> divmod(fnn, 999) #py-bug!!!
(nan, nan)
>>> divmod(fnn, -999) #py-bug!!!
(nan, nan)


>>> +oo // +999
(+oo)
>>> +oo // -999
(-oo)
>>> -oo // +999
(-oo)
>>> -oo // -999
(+oo)

>>> +999 // +oo
0
>>> +999 // -oo # bug-fixed:0 --> -1
-1
>>> -999 // +oo # bug-fixed:0 --> -1
-1
>>> -999 // -oo
0




>>> (-999) ** fpp #py-bug!!!
inf
>>> fnn ** fpp #py-bug!!!
inf
>>> 0 ** fnn #py-bug!!!
inf
>>> (-0.5) ** fnn #py-bug!!!
inf
>>> (-1) ** fpp #py-bug!!!
1.0
>>> (-1) ** fnn #py-bug!!!
1.0
>>> fpp ** 0.5
inf
>>> fnn ** 0.5 #py-bug!!!
inf


>>> 0 ** 0
1
>>> 0 ** -1
Traceback (most recent call last):
    ...
ZeroDivisionError: 0.0 cannot be raised to a negative power


>>> (-999) ** (+oo)
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.Error__NaN
>>> (-oo) ** (+oo)
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.Error__NaN
>>> 0 ** (-oo) # [Error__NaN --> Error__Div0] <<== see:[0**-1] but [0**-inf == inf]
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.Error__Div0
>>> (-0.5) ** (-oo)
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.Error__NaN
>>> (-1) ** (+oo)
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.Error__NaN
>>> (-1) ** (-oo)
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.Error__NaN


>>> (+oo) ** 0 # see:[0**0]
1
>>> (-oo) ** 0
1
>>> (+oo) ** 0.5
(+oo)
>>> (-oo) ** 0.5
Traceback (most recent call last):
    ...
TypeError: <class 'float'>


#after ++Tag_o0o8inv_inf:
#   now: truediv --> inv_inf__pos/inv_inf__neg
#>>> 0 / (+oo)
#>>> -1 / (+oo)
#>>> +1 / (+oo)
#>>> 0 / (-oo)
#>>> -1 / (-oo)
#>>> +1 / (-oo)

>>> 0 / (+oo)
0
>>> -1 / (+oo)
(1/-oo+0)
>>> +1 / (+oo)
(1/+oo+0)
>>> 0 / (-oo)
0
>>> -1 / (-oo)
(1/+oo+0)
>>> +1 / (-oo)
(1/-oo+0)
>>> +1 / (-oo) + 999
(1/-oo+999)
>>> 998.999 < +1 / (-oo) + 999 < 999
True
>>> +1 / (-oo) + 999 == +1 / (-oo) + 999
True
>>> 999.001 > +1 / (+oo) + 999 > 999
True
>>> +1 / (+oo) + 999 == +1 / (+oo) + 999
True

>>> 1 / (+oo) + +oo
(+oo)
>>> 1 / (+oo) + -oo
(-oo)
>>> 1 / (-oo) + +oo
(+oo)
>>> 1 / (-oo) + -oo
(-oo)

>>> (+oo) + 1 / +oo
(+oo)
>>> (+oo) + 1 / -oo
(+oo)
>>> (-oo) + 1 / +oo
(-oo)
>>> (-oo) + 1 / -oo
(-oo)


>>> 1 / (+oo) - +oo
(-oo)
>>> 1 / (+oo) - -oo
(+oo)
>>> 1 / (-oo) - +oo
(-oo)
>>> 1 / (-oo) - -oo
(+oo)

>>> (+oo) - 1 / +oo
(+oo)
>>> (+oo) - 1 / -oo
(+oo)
>>> (-oo) - 1 / +oo
(-oo)
>>> (-oo) - 1 / -oo
(-oo)

>>> def _lshift_(x, y, /):
...     return x * 2**y
>>> def _rshift_(x, y, /):
...     return x * 2**(-y)
>>> from seed.debug.expectError import expectError
>>> from itertools import product, chain
>>> from operator import __add__, __sub__, __mul__, __truediv__, __floordiv__, __pow__, __lshift__, __rshift__
>>> ops = [__add__, __sub__, __mul__, __truediv__, __floordiv__, __pow__, __lshift__, __rshift__, _lshift_, _rshift_]
>>> xxs = [(+oo,fpp), (-oo,fnn), (0,0), (+999,+999), (-999,-999), (-0.5,-0.5), (+0.5,+0.5), (-1,-1), (+1,+1)]
>>> yys = xxs[:2]
>>> inf = fpp
>>> nan = fpp-fpp
>>> infos4ignore4bug = (
... [[(+oo, inf), (999, 999), 'floordiv', 'nan']
... ,[(+oo, inf), (-999, -999), 'floordiv', 'nan']
... ,[(-oo, -inf), (999, 999), 'floordiv', 'nan']
... ,[(-oo, -inf), (-999, -999), 'floordiv', 'nan']
... ,[((+oo), inf), (-0.5, -0.5), 'floordiv', 'nan']
... ,[((+oo), inf), (0.5, 0.5), 'floordiv', 'nan']
... ,[((+oo), inf), (-1, -1), 'floordiv', 'nan']
... ,[((+oo), inf), (1, 1), 'floordiv', 'nan']
... ,[((+oo), -inf), (-0.5, -0.5), 'floordiv', 'nan']
... ,[((+oo), -inf), (0.5, 0.5), 'floordiv', 'nan']
... ,[((+oo), -inf), (-1, -1), 'floordiv', 'nan']
... ,[((+oo), -inf), (1, 1), 'floordiv', 'nan']
... ,[((-oo), inf), (-0.5, -0.5), 'floordiv', 'nan']
... ,[((-oo), inf), (0.5, 0.5), 'floordiv', 'nan']
... ,[((-oo), inf), (-1, -1), 'floordiv', 'nan']
... ,[((-oo), inf), (1, 1), 'floordiv', 'nan']
... ,[((-oo), -inf), (-0.5, -0.5), 'floordiv', 'nan']
... ,[((-oo), -inf), (0.5, 0.5), 'floordiv', 'nan']
... ,[((-oo), -inf), (-1, -1), 'floordiv', 'nan']
... ,[((-oo), -inf), (1, 1), 'floordiv', 'nan']
... #
... #,[(999, 999), (-oo, -inf), 'floordiv', '-1.0']
... #,[(-999, -999), (+oo, inf), 'floordiv', '-1.0']
... #
... ,[((-oo), -inf), ((+oo), inf), 'pow', 'inf']
... ,[(0, 0), ((-oo), -inf), 'pow', 'inf']
... ,[(-999, -999), ((+oo), inf), 'pow', 'inf']
... ,[(-0.5, -0.5), ((-oo), -inf), 'pow', 'inf']
... ,[(-1, -1), ((+oo), inf), 'pow', '1.0']
... ,[(-1, -1), ((-oo), -inf), 'pow', '1.0']
... #
... #
... ,[(999, 999), ((+oo), inf), 'truediv', '0.0']
... ,[(999, 999), ((-oo), -inf), 'truediv', '-0.0']
... ,[(-999, -999), ((+oo), inf), 'truediv', '-0.0']
... ,[(-999, -999), ((-oo), -inf), 'truediv', '0.0']
... ,[(-0.5, -0.5), ((+oo), inf), 'truediv', '-0.0']
... ,[(-0.5, -0.5), ((-oo), -inf), 'truediv', '0.0']
... ,[(+0.5, +0.5), ((+oo), inf), 'truediv', '0.0']
... ,[(+0.5, +0.5), ((-oo), -inf), 'truediv', '-0.0']
... ,[(-1, -1), ((+oo), inf), 'truediv', '-0.0']
... ,[(-1, -1), ((-oo), -inf), 'truediv', '0.0']
... ,[(+1, +1), ((+oo), inf), 'truediv', '0.0']
... ,[(+1, +1), ((-oo), -inf), 'truediv', '-0.0']
... ,
... ])
>>> err_msgs4ignored_TypeError = (
... ["unsupported operand type(s) for <<: 'float' and 'float'"
... ,"unsupported operand type(s) for <<: 'int' and 'float'"
... ,"unsupported operand type(s) for <<: 'float' and 'int'"
... ,"unsupported operand type(s) for >>: 'float' and 'float'"
... ,"unsupported operand type(s) for >>: 'int' and 'float'"
... ,"unsupported operand type(s) for >>: 'float' and 'int'"
... ,
... ])
>>> for (x,a), (y,b) in chain(product(xxs, yys), product(yys, xxs)):
...  for op in ops:
...   f = lambda:op(x,y)
...   try:
...     r = op(a,b)
...   except ZeroDivisionError:
...     s = 'ZeroDivisionError'
...     #no:r
...   except TypeError as e:
...     #TypeError: unsupported operand type(s) for <<: 'float' and 'float'
...     assert str(e) in err_msgs4ignored_TypeError, e
...     #s = ???
...     continue
...   else:
...     s = repr(r)
...   #no:r
...   info = [(x,a), (y,b), op.__name__, s] #, r
...   if info in infos4ignore4bug:continue
...   if s == 'ZeroDivisionError':
...     assert expectError(Error__Div0, f), info
...   elif s == 'nan':
...     assert expectError(Error__NaN, f), info
...   elif s == 'inf':
...     if op is __pow__ and type(y) is float and x is -oo:
...       assert expectError(TypeError, f), info
...       continue
...     assert not expectError(Error__NaN, f) and f() is +oo, info
...   elif s == '-inf':
...     assert f() is -oo, info
...   else:
...     assert not expectError(Error__NaN, f) and f() == r, info
...     ##now:bug-fixed: return (-1|0)
...     ##<<==:
...     ##below: when __rfloordiv__ return 0
...     #AssertionError: [(999, 999), (-oo, -inf), 'floordiv', '-1.0']
...     #AssertionError: [(-999, -999), (+oo, inf), 'floordiv', '-1.0']
...     ######################
...     ###but:py-bug:cause:
...     ######################
...     #AssertionError: [(+oo, inf), (999, 999), 'floordiv', 'nan']
...     #AssertionError: [(+oo, inf), (-999, -999), 'floordiv', 'nan']
...     #AssertionError: [(-oo, -inf), (999, 999), 'floordiv', 'nan']
...     #AssertionError: [(-oo, -inf), (-999, -999), 'floordiv', 'nan']
...     #
...     #
...     #AssertionError: [((+oo), inf), (-0.5, -0.5), 'floordiv', 'nan']
...     #AssertionError: [((+oo), inf), (0.5, 0.5), 'floordiv', 'nan']
...     #AssertionError: [((+oo), inf), (-1, -1), 'floordiv', 'nan']
...     #AssertionError: [((+oo), inf), (1, 1), 'floordiv', 'nan']
...     #AssertionError: [((+oo), -inf), (-0.5, -0.5), 'floordiv', 'nan']
...     #AssertionError: [((+oo), -inf), (0.5, 0.5), 'floordiv', 'nan']
...     #AssertionError: [((+oo), -inf), (-1, -1), 'floordiv', 'nan']
...     #AssertionError: [((+oo), -inf), (1, 1), 'floordiv', 'nan']
...     #
...     #AssertionError: [((-oo), inf), (-0.5, -0.5), 'floordiv', 'nan']
...     #AssertionError: [((-oo), inf), (0.5, 0.5), 'floordiv', 'nan']
...     #AssertionError: [((-oo), inf), (-1, -1), 'floordiv', 'nan']
...     #AssertionError: [((-oo), inf), (1, 1), 'floordiv', 'nan']
...     #AssertionError: [((-oo), -inf), (-0.5, -0.5), 'floordiv', 'nan']
...     #AssertionError: [((-oo), -inf), (0.5, 0.5), 'floordiv', 'nan']
...     #AssertionError: [((-oo), -inf), (-1, -1), 'floordiv', 'nan']
...     #AssertionError: [((-oo), -inf), (1, 1), 'floordiv', 'nan']
...     #
...     #
...     #
...     #
...     #AssertionError: [((-oo), -inf), ((+oo), inf), 'pow', 'inf']
...     #AssertionError: [(0, 0), ((-oo), -inf), 'pow', 'inf']
...     #AssertionError: [(-999, -999), ((+oo), inf), 'pow', 'inf']
...     #AssertionError: [(-0.5, -0.5), ((-oo), -inf), 'pow', 'inf']
...     #AssertionError: [(-1, -1), ((+oo), inf), 'pow', '1.0']
...     #AssertionError: [(-1, -1), ((-oo), -inf), 'pow', '1.0']
...     #
...     #
...     #
...     #after ++Tag_o0o8inv_inf:
...     #   now: truediv --> inv_inf__pos/inv_inf__neg
...     #AssertionError: [(999, 999), ((+oo), inf), 'truediv', '0.0']
...     #
...     #
...     #




######################
######################
>>> +999 / +oo
(1/+oo+0)
>>> +1   / +oo
(1/+oo+0)
>>> +0.5 / +oo
(1/+oo+0)
>>> 0    / +oo
0
>>> -0.5 / +oo
(1/-oo+0)
>>> -1   / +oo
(1/-oo+0)
>>> -999 / +oo
(1/-oo+0)


>>> +999 / -oo
(1/-oo+0)
>>> +1   / -oo
(1/-oo+0)
>>> +0.5 / -oo
(1/-oo+0)
>>> 0    / -oo
0
>>> -0.5 / -oo
(1/+oo+0)
>>> -1   / -oo
(1/+oo+0)
>>> -999 / -oo
(1/+oo+0)


######################
######################
>>> (-oo)   << (-oo)
Traceback (most recent call last):
...
seed.tiny_.oo8inf.Error__NaN
>>> (+oo)   << (-oo)
Traceback (most recent call last):
...
seed.tiny_.oo8inf.Error__NaN
>>> 2**(-oo)
0
>>> (+oo) * 0
Traceback (most recent call last):
...
seed.tiny_.oo8inf.Error__NaN
>>> (-oo) * 0
Traceback (most recent call last):
...
seed.tiny_.oo8inf.Error__NaN

######################
######################
######################
######################
__lshift__
__rshift__
__pow__


#
#
#######################
#######################
#>>> (-oo)   << (+oo)
#>>> (-oo)   << (+999)
#>>> (-oo)   << (+666)
#>>> (-oo)   << (+1)
#>>> (-oo)   << (+0.5)
#>>> (-oo)   << (0)
#>>> (-oo)   << (-0.5)
#>>> (-oo)   << (-1)
#>>> (-oo)   << (-666)
#>>> (-oo)   << (-999)
#>>> (-oo)   << (-oo)
#
#
#>>> (+oo)   << (+oo)
#>>> (+oo)   << (+999)
#>>> (+oo)   << (+666)
#>>> (+oo)   << (+1)
#>>> (+oo)   << (+0.5)
#>>> (+oo)   << (0)
#>>> (+oo)   << (-0.5)
#>>> (+oo)   << (-1)
#>>> (+oo)   << (-666)
#>>> (+oo)   << (-999)
#>>> (+oo)   << (-oo)
#
#
#>>> (+oo)   <<  (-oo)
#>>> (+999)  <<  (-oo)
#>>> (+666)  <<  (-oo)
#>>> (+1)    <<  (-oo)
#>>> (+0.5)  <<  (-oo)
#>>> (0)     <<  (-oo)
#>>> (-0.5)  <<  (-oo)
#>>> (-1)    <<  (-oo)
#>>> (-666)  <<  (-oo)
#>>> (-999)  <<  (-oo)
#>>> (-oo)   <<  (-oo)
#
#
#>>> (+oo)   <<  (+oo)
#>>> (+999)  <<  (+oo)
#>>> (+666)  <<  (+oo)
#>>> (+1)    <<  (+oo)
#>>> (+0.5)  <<  (+oo)
#>>> (0)     <<  (+oo)
#>>> (-0.5)  <<  (+oo)
#>>> (-1)    <<  (+oo)
#>>> (-666)  <<  (+oo)
#>>> (-999)  <<  (+oo)
#>>> (-oo)   <<  (+oo)
#
#
#
#
#######################
#######################
#>>> (-oo)   >> (+oo)
#>>> (-oo)   >> (+999)
#>>> (-oo)   >> (+666)
#>>> (-oo)   >> (+1)
#>>> (-oo)   >> (+0.5)
#>>> (-oo)   >> (0)
#>>> (-oo)   >> (-0.5)
#>>> (-oo)   >> (-1)
#>>> (-oo)   >> (-666)
#>>> (-oo)   >> (-999)
#>>> (-oo)   >> (-oo)
#
#
#>>> (+oo)   >> (+oo)
#>>> (+oo)   >> (+999)
#>>> (+oo)   >> (+666)
#>>> (+oo)   >> (+1)
#>>> (+oo)   >> (+0.5)
#>>> (+oo)   >> (0)
#>>> (+oo)   >> (-0.5)
#>>> (+oo)   >> (-1)
#>>> (+oo)   >> (-666)
#>>> (+oo)   >> (-999)
#>>> (+oo)   >> (-oo)
#
#
#>>> (+oo)   >>  (-oo)
#>>> (+999)  >>  (-oo)
#>>> (+666)  >>  (-oo)
#>>> (+1)    >>  (-oo)
#>>> (+0.5)  >>  (-oo)
#>>> (0)     >>  (-oo)
#>>> (-0.5)  >>  (-oo)
#>>> (-1)    >>  (-oo)
#>>> (-666)  >>  (-oo)
#>>> (-999)  >>  (-oo)
#>>> (-oo)   >>  (-oo)
#
#
#>>> (+oo)   >>  (+oo)
#>>> (+999)  >>  (+oo)
#>>> (+666)  >>  (+oo)
#>>> (+1)    >>  (+oo)
#>>> (+0.5)  >>  (+oo)
#>>> (0)     >>  (+oo)
#>>> (-0.5)  >>  (+oo)
#>>> (-1)    >>  (+oo)
#>>> (-666)  >>  (+oo)
#>>> (-999)  >>  (+oo)
#>>> (-oo)   >>  (+oo)
#
#
#
#
#
#######################
#######################
#>>> (-oo)   ** (+oo)
#>>> (-oo)   ** (+999)
#>>> (-oo)   ** (+666)
#>>> (-oo)   ** (+1)
#>>> (-oo)   ** (+0.5)
#>>> (-oo)   ** (0)
#>>> (-oo)   ** (-0.5)
#>>> (-oo)   ** (-1)
#>>> (-oo)   ** (-666)
#>>> (-oo)   ** (-999)
#>>> (-oo)   ** (-oo)
#
#
#>>> (+oo)   ** (+oo)
#>>> (+oo)   ** (+999)
#>>> (+oo)   ** (+666)
#>>> (+oo)   ** (+1)
#>>> (+oo)   ** (+0.5)
#>>> (+oo)   ** (0)
#>>> (+oo)   ** (-0.5)
#>>> (+oo)   ** (-1)
#>>> (+oo)   ** (-666)
#>>> (+oo)   ** (-999)
#>>> (+oo)   ** (-oo)
#
#
#>>> (+oo)   **  (-oo)
#>>> (+999)  **  (-oo)
#>>> (+666)  **  (-oo)
#>>> (+1)    **  (-oo)
#>>> (+0.5)  **  (-oo)
#>>> (0)     **  (-oo)
#>>> (-0.5)  **  (-oo)
#>>> (-1)    **  (-oo)
#>>> (-666)  **  (-oo)
#>>> (-999)  **  (-oo)
#>>> (-oo)   **  (-oo)
#
#
#>>> (+oo)   **  (+oo)
#>>> (+999)  **  (+oo)
#>>> (+666)  **  (+oo)
#>>> (+1)    **  (+oo)
#>>> (+0.5)  **  (+oo)
#>>> (0)     **  (+oo)
#>>> (-0.5)  **  (+oo)
#>>> (-1)    **  (+oo)
#>>> (-666)  **  (+oo)
#>>> (-999)  **  (+oo)
#>>> (-oo)   **  (+oo)
#
#
#
#
#
#######################
#######################
#
#
#







######################
######################
######################
>>> (-oo)   << (+oo)
(-oo)
>>> (-oo)   << (+999)
(-oo)
>>> (-oo)   << (+666)
(-oo)
>>> (-oo)   << (+1)
(-oo)
>>> (-oo)   << (+0.5)
(-oo)
>>> (-oo)   << (0)
(-oo)
>>> (-oo)   << (-0.5)
(-oo)
>>> (-oo)   << (-1)
(-oo)
>>> (-oo)   << (-666)
(-oo)
>>> (-oo)   << (-999)
(-oo)
>>> (-oo)   << (-oo)
Traceback (most recent call last):
...
seed.tiny_.oo8inf.Error__NaN
>>> (+oo)   << (+oo)
(+oo)
>>> (+oo)   << (+999)
(+oo)
>>> (+oo)   << (+666)
(+oo)
>>> (+oo)   << (+1)
(+oo)
>>> (+oo)   << (+0.5)
(+oo)
>>> (+oo)   << (0)
(+oo)
>>> (+oo)   << (-0.5)
(+oo)
>>> (+oo)   << (-1)
(+oo)
>>> (+oo)   << (-666)
(+oo)
>>> (+oo)   << (-999)
(+oo)
>>> (+oo)   << (-oo)
Traceback (most recent call last):
...
seed.tiny_.oo8inf.Error__NaN
>>> (+oo)   <<  (-oo)
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.Error__NaN
>>> (+999)  <<  (-oo) #0
(1/+oo+0)
>>> (+666)  <<  (-oo) #0
(1/+oo+0)
>>> (+1)    <<  (-oo) #0
(1/+oo+0)
>>> (+0.5)  <<  (-oo) #0
(1/+oo+0)
>>> (0)     <<  (-oo)
0
>>> (-0.5)  <<  (-oo) #0
(1/-oo+0)
>>> (-1)    <<  (-oo) #0
(1/-oo+0)
>>> (-666)  <<  (-oo) #0
(1/-oo+0)
>>> (-999)  <<  (-oo) #0
(1/-oo+0)
>>> (-oo)   <<  (-oo)
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.Error__NaN
>>> (+oo)   <<  (+oo)
(+oo)
>>> (+999)  <<  (+oo)
(+oo)
>>> (+666)  <<  (+oo)
(+oo)
>>> (+1)    <<  (+oo)
(+oo)
>>> (+0.5)  <<  (+oo)
(+oo)
>>> (0)     <<  (+oo)
Traceback (most recent call last):
...
seed.tiny_.oo8inf.Error__NaN
>>> (-0.5)  <<  (+oo)
(-oo)
>>> (-1)    <<  (+oo)
(-oo)
>>> (-666)  <<  (+oo)
(-oo)
>>> (-999)  <<  (+oo)
(-oo)
>>> (-oo)   <<  (+oo)
(-oo)
>>> (-oo)   >> (+oo)
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.Error__NaN
>>> (-oo)   >> (+999)
(-oo)
>>> (-oo)   >> (+666)
(-oo)
>>> (-oo)   >> (+1)
(-oo)
>>> (-oo)   >> (+0.5)
(-oo)
>>> (-oo)   >> (0)
(-oo)
>>> (-oo)   >> (-0.5)
(-oo)
>>> (-oo)   >> (-1)
(-oo)
>>> (-oo)   >> (-666)
(-oo)
>>> (-oo)   >> (-999)
(-oo)
>>> (-oo)   >> (-oo)
(-oo)
>>> (+oo)   >> (+oo)
Traceback (most recent call last):
...
seed.tiny_.oo8inf.Error__NaN
>>> (+oo)   >> (+999)
(+oo)
>>> (+oo)   >> (+666)
(+oo)
>>> (+oo)   >> (+1)
(+oo)
>>> (+oo)   >> (+0.5)
(+oo)
>>> (+oo)   >> (0)
(+oo)
>>> (+oo)   >> (-0.5)
(+oo)
>>> (+oo)   >> (-1)
(+oo)
>>> (+oo)   >> (-666)
(+oo)
>>> (+oo)   >> (-999)
(+oo)
>>> (+oo)   >> (-oo)
(+oo)
>>> (+oo)   >>  (-oo)
(+oo)
>>> (+999)  >>  (-oo)
(+oo)
>>> (+666)  >>  (-oo)
(+oo)
>>> (+1)    >>  (-oo)
(+oo)
>>> (+0.5)  >>  (-oo)
(+oo)
>>> (0)     >>  (-oo)
Traceback (most recent call last):
...
seed.tiny_.oo8inf.Error__NaN
>>> (-0.5)  >>  (-oo)
(-oo)
>>> (-1)    >>  (-oo)
(-oo)
>>> (-666)  >>  (-oo)
(-oo)
>>> (-999)  >>  (-oo)
(-oo)
>>> (-oo)   >>  (-oo)
(-oo)
>>> (+oo)   >>  (+oo)
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.Error__NaN
>>> (+999)  >>  (+oo) #0
(1/+oo+0)
>>> (+666)  >>  (+oo) #0
(1/+oo+0)
>>> (+1)    >>  (+oo) #0
(1/+oo+0)
>>> (+0.5)  >>  (+oo) #0
(1/+oo+0)
>>> (0)     >>  (+oo)
0
>>> (-0.5)  >>  (+oo) #0
(1/-oo+0)
>>> (-1)    >>  (+oo) #0
(1/-oo+0)
>>> (-666)  >>  (+oo) #0
(1/-oo+0)
>>> (-999)  >>  (+oo) #0
(1/-oo+0)
>>> (-oo)   >>  (+oo)
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.Error__NaN
>>> (-oo)   ** (+oo)
Traceback (most recent call last):
...
seed.tiny_.oo8inf.Error__NaN
>>> (-oo)   ** (+999)
(-oo)
>>> (-oo)   ** (+666)
(+oo)
>>> (-oo)   ** (+1)
(-oo)
>>> (-oo)   ** (+0.5)
Traceback (most recent call last):
...
TypeError: <class 'float'>
>>> (-oo)   ** (0)
1
>>> (-oo)   ** (-0.5)
0
>>> (-oo)   ** (-1)
0
>>> (-oo)   ** (-666)
0
>>> (-oo)   ** (-999)
0
>>> (-oo)   ** (-oo)
0
>>> (+oo)   ** (+oo)
(+oo)
>>> (+oo)   ** (+999)
(+oo)
>>> (+oo)   ** (+666)
(+oo)
>>> (+oo)   ** (+1)
(+oo)
>>> (+oo)   ** (+0.5)
(+oo)
>>> (+oo)   ** (0)
1
>>> (+oo)   ** (-0.5)
0
>>> (+oo)   ** (-1)
0
>>> (+oo)   ** (-666)
0
>>> (+oo)   ** (-999)
0
>>> (+oo)   ** (-oo)
0
>>> (+oo)   **  (-oo)
0
>>> (+999)  **  (-oo)
0
>>> (+666)  **  (-oo)
0
>>> (+1)    **  (-oo)
1
>>> (+0.5)  **  (-oo)
(+oo)
>>> (0)     **  (-oo)
Traceback (most recent call last):
...
seed.tiny_.oo8inf.Error__Div0
>>> (-0.5)  **  (-oo)
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.Error__NaN
>>> (-1)    **  (-oo)
Traceback (most recent call last):
...
seed.tiny_.oo8inf.Error__NaN
>>> (-666)  **  (-oo)
0
>>> (-999)  **  (-oo)
0
>>> (-oo)   **  (-oo)
0
>>> (+oo)   **  (+oo)
(+oo)
>>> (+999)  **  (+oo)
(+oo)
>>> (+666)  **  (+oo)
(+oo)
>>> (+1)    **  (+oo)
1
>>> (+0.5)  **  (+oo)
0
>>> (0)     **  (+oo)
0
>>> (-0.5)  **  (+oo)
0
>>> (-1)    **  (+oo)
Traceback (most recent call last):
...
seed.tiny_.oo8inf.Error__NaN
>>> (-666)  **  (+oo)
Traceback (most recent call last):
...
seed.tiny_.oo8inf.Error__NaN
>>> (-999)  **  (+oo)
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.Error__NaN
>>> (-oo)   **  (+oo)
Traceback (most recent call last):
...
seed.tiny_.oo8inf.Error__NaN

















######################
######################
######################
+oo, -oo, 0, +1, -1, +999, -999, +0.5, -0.5
#>>> (1/+oo)  + (+oo)
#>>> (1/+oo)  - (+oo)
#>>> (1/+oo)  * (+oo)
#>>> (1/+oo)  / (+oo)
#>>> (1/+oo) // (+oo)
#>>> (1/+oo) ** (+oo)
#>>> (1/+oo) << (+oo)
#>>> (1/+oo) >> (+oo)
#
#>>> (1/+oo)  + (-oo)
#>>> (1/+oo)  - (-oo)
#>>> (1/+oo)  * (-oo)
#>>> (1/+oo)  / (-oo)
#>>> (1/+oo) // (-oo)
#>>> (1/+oo) ** (-oo)
#>>> (1/+oo) << (-oo)
#>>> (1/+oo) >> (-oo)
#
#>>> (1/-oo)  + (+oo)
#>>> (1/-oo)  - (+oo)
#>>> (1/-oo)  * (+oo)
#>>> (1/-oo)  / (+oo)
#>>> (1/-oo) // (+oo)
#>>> (1/-oo) ** (+oo)
#>>> (1/-oo) << (+oo)
#>>> (1/-oo) >> (+oo)
#
#>>> (1/-oo)  + (-oo)
#>>> (1/-oo)  - (-oo)
#>>> (1/-oo)  * (-oo)
#>>> (1/-oo)  / (-oo)
#>>> (1/-oo) // (-oo)
#>>> (1/-oo) ** (-oo)
#>>> (1/-oo) << (-oo)
#>>> (1/-oo) >> (-oo)
#
#
#######################
#>>> (+oo)  + (1/+oo)
#>>> (+oo)  - (1/+oo)
#>>> (+oo)  * (1/+oo)
#>>> (+oo)  / (1/+oo)
#>>> (+oo) // (1/+oo)
#>>> (+oo) ** (1/+oo)
#>>> (+oo) << (1/+oo)
#>>> (+oo) >> (1/+oo)
#
#>>> (+oo)  + (1/-oo)
#>>> (+oo)  - (1/-oo)
#>>> (+oo)  * (1/-oo)
#>>> (+oo)  / (1/-oo)
#>>> (+oo) // (1/-oo)
#>>> (+oo) ** (1/-oo)
#>>> (+oo) << (1/-oo)
#>>> (+oo) >> (1/-oo)
#
#>>> (-oo)  + (1/+oo)
#>>> (-oo)  - (1/+oo)
#>>> (-oo)  * (1/+oo)
#>>> (-oo)  / (1/+oo)
#>>> (-oo) // (1/+oo)
#>>> (-oo) ** (1/+oo)
#>>> (-oo) << (1/+oo)
#>>> (-oo) >> (1/+oo)
#
#>>> (-oo)  + (1/-oo)
#>>> (-oo)  - (1/-oo)
#>>> (-oo)  * (1/-oo)
#>>> (-oo)  / (1/-oo)
#>>> (-oo) // (1/-oo)
#>>> (-oo) ** (1/-oo)
#>>> (-oo) << (1/-oo)
#>>> (-oo) >> (1/-oo)



>>> (1/+oo)  + (+oo)
(+oo)
>>> (1/+oo)  - (+oo)
(-oo)
>>> (1/+oo)  * (+oo)
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.Error__NaN
>>> (1/+oo)  / (+oo)
(1/+oo+0)
>>> (1/+oo) // (+oo)
0
>>> (1/+oo) ** (+oo) #??? --> (1/+oo+0)
0
>>> (1/+oo) << (+oo)
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.Error__NaN
>>> (1/+oo) >> (+oo)
(1/+oo+0)
>>> (1/+oo)  + (-oo)
(-oo)
>>> (1/+oo)  - (-oo)
(+oo)
>>> (1/+oo)  * (-oo)
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.Error__NaN
>>> (1/+oo)  / (-oo)
(1/-oo+0)
>>> (1/+oo) // (-oo)
-1
>>> (1/+oo) ** (-oo)
(+oo)
>>> (1/+oo) << (-oo)
(1/+oo+0)
>>> (1/+oo) >> (-oo)
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.Error__NaN
>>> (1/-oo)  + (+oo)
(+oo)
>>> (1/-oo)  - (+oo)
(-oo)
>>> (1/-oo)  * (+oo)
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.Error__NaN
>>> (1/-oo)  / (+oo)
(1/-oo+0)
>>> (1/-oo) // (+oo)
-1
>>> (1/-oo) ** (+oo) #??? unknowm sign
0
>>> (1/-oo) << (+oo)
Traceback (most recent call last):
...
seed.tiny_.oo8inf.Error__NaN
>>> (1/-oo) >> (+oo)
(1/-oo+0)
>>> (1/-oo)  + (-oo)
(-oo)
>>> (1/-oo)  - (-oo)
(+oo)
>>> (1/-oo)  * (-oo)
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.Error__NaN
>>> (1/-oo)  / (-oo)
(1/+oo+0)
>>> (1/-oo) // (-oo)
0
>>> (1/-oo) ** (-oo)
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.Error__NaN
>>> (1/-oo) << (-oo)
(1/-oo+0)
>>> (1/-oo) >> (-oo)
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.Error__NaN
>>> (+oo)  + (1/+oo)
(+oo)
>>> (+oo)  - (1/+oo)
(+oo)
>>> (+oo)  * (1/+oo)
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.Error__NaN
>>> (+oo)  / (1/+oo)
(+oo)
>>> (+oo) // (1/+oo)
(+oo)
>>> (+oo) ** (1/+oo)
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.Error__NaN
>>> (+oo) << (1/+oo)
(+oo)
>>> (+oo) >> (1/+oo)
(+oo)
>>> (+oo)  + (1/-oo)
(+oo)
>>> (+oo)  - (1/-oo)
(+oo)
>>> (+oo)  * (1/-oo)
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.Error__NaN
>>> (+oo)  / (1/-oo)
(-oo)
>>> (+oo) // (1/-oo)
(-oo)
>>> (+oo) ** (1/-oo)
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.Error__NaN
>>> (+oo) << (1/-oo)
(+oo)
>>> (+oo) >> (1/-oo)
(+oo)
>>> (-oo)  + (1/+oo)
(-oo)
>>> (-oo)  - (1/+oo)
(-oo)
>>> (-oo)  * (1/+oo)
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.Error__NaN
>>> (-oo)  / (1/+oo)
(-oo)
>>> (-oo) // (1/+oo)
(-oo)
>>> (-oo) ** (1/+oo)
Traceback (most recent call last):
...
seed.tiny_.oo8inf.Error__NaN
>>> (-oo) << (1/+oo)
(-oo)
>>> (-oo) >> (1/+oo)
(-oo)
>>> (-oo)  + (1/-oo)
(-oo)
>>> (-oo)  - (1/-oo)
(-oo)
>>> (-oo)  * (1/-oo)
Traceback (most recent call last):
...
seed.tiny_.oo8inf.Error__NaN
>>> (-oo)  / (1/-oo)
(+oo)
>>> (-oo) // (1/-oo)
(+oo)
>>> (-oo) ** (1/-oo)
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.Error__NaN
>>> (-oo) << (1/-oo)
(-oo)
>>> (-oo) >> (1/-oo)
(-oo)







######################
######################
######################
interval_based_mapping
interval_based_set
open_set
open_end_boundary

>>> (b"xx" < (1/-oo+b"xy") < b"xy" < (1/+oo+b"xy") < b"xy\0" < b"xz"
... ) # TypeError: unsupported operand type(s) for +: 'int' and 'bytes'
True



>>> OpenInterval(-oo, +oo)
oo[:-oo:, :+oo:]
>>> OpenInterval(-oo, 1/+oo)
oo[:-oo:, ::0]
>>> OpenInterval(-oo, 1/+oo+999)
oo[:-oo:, ::999]
>>> OpenInterval(1/-oo, 1/+oo+999)
oo[0::, ::999]
>>> OpenInterval(1/-oo+999, 1/+oo+999)
oo[:999:]
>>> bool(OpenInterval(1/-oo+999, 1/+oo+999))
True
>>> 999 in OpenInterval(1/-oo+999, 1/+oo+999)
True
>>> 998 in OpenInterval(1/-oo+999, 1/+oo+999)
False
>>> 1000 in OpenInterval(1/-oo+999, 1/+oo+999)
False
>>> 998.999 in OpenInterval(1/-oo+999, 1/+oo+999)
False
>>> 999.001 in OpenInterval(1/-oo+999, 1/+oo+999)
False

>>> osp = OpenInterval(-oo, +oo)
>>> osp.low
(-oo)
>>> osp.up
(+oo)
>>> osp.span
((-oo), (+oo))
>>> osp.length
(+oo)

>>> OpenInterval(1/-oo+0, +oo).length
(+oo)
>>> OpenInterval(1/-oo+0, 1/+oo+4).length
(1/+oo+4)
>>> OpenInterval(1/-oo+0, 1/-oo+4).length
4
>>> OpenInterval(1/-oo+0, 1/-oo+0).length
0
>>> OpenInterval(1/-oo+0, 1/-oo-1).length
0
>>> OpenInterval(1/-oo+0, 1/+oo-1).length
0
>>> OpenInterval(1/-oo+0, 1/+oo+0).length
(1/+oo+0)

>>> bool(OpenInterval(1/-oo+0, 1/+oo-1))
False
>>> bool(OpenInterval(1/-oo+0, 1/+oo+0))
True
>>> bool(OpenInterval(1/-oo+0, 1/+oo+1))
True
>>> bool(OpenInterval(1/-oo+0, 1/-oo-1))
False
>>> bool(OpenInterval(1/-oo+0, 1/-oo+0))
False
>>> bool(OpenInterval(1/-oo+0, 1/-oo+1))
True

>>> bool(OpenInterval(1/+oo+0, 1/+oo-1))
False
>>> bool(OpenInterval(1/+oo+0, 1/+oo+0))
False
>>> bool(OpenInterval(1/+oo+0, 1/+oo+1))
True
>>> bool(OpenInterval(1/+oo+0, 1/-oo-1))
False
>>> bool(OpenInterval(1/+oo+0, 1/-oo+0))
False
>>> bool(OpenInterval(1/+oo+0, 1/-oo+1))
True


>>> OpenInterval(1/-oo+111, 1/+oo+999) < OpenInterval(1/+oo+111, 1/+oo-666) # to_support_sort:[to support sorted() instead of set inclusion cmp] #True #--> now deprecated by using『key=OpenInterval.key4sort』
Traceback (most recent call last):
    ...
TypeError: '<' not supported between instances of 'OpenInterval' and 'OpenInterval'

>>> {OpenInterval(1/-oo+111, +oo):999} #hash()
{oo[111::, :+oo:]: 999}

>>> {OpenInterval(1/-oo+111, +oo):999} == {oo[111::, :+oo:]: 999}
True

#>>> oo[111::, :+oo:]
#>>> oo[::111, :-oo:]
#>>> oo[+oo::, -oo::]
#>>> oo[::+oo, ::-oo]
#>>> oo[:+oo:]
#>>> oo[:-oo:]
#>>> oo[:999:]
#>>> oo[999::]
#>>> oo[::999]


>>> oo[111::, :+oo:]
oo[111::, :+oo:]
>>> oo[::111, :-oo:]
oo[::111, :-oo:]
>>> oo[+oo::, -oo::]
oo[:+oo:, :-oo:]
>>> oo[::+oo, ::-oo]
oo[:+oo:, :-oo:]
>>> oo[:+oo:, :+oo:]
oo[:+oo:]
>>> oo[:+oo:, +oo::]
oo[:+oo:]
>>> oo[:+oo:]
oo[:+oo:]
>>> oo[+oo::]
oo[:+oo:]
>>> oo[::+oo]
oo[:+oo:]
>>> oo[:-oo:]
oo[:-oo:]
>>> oo[-oo::]
oo[:-oo:]
>>> oo[::-oo]
oo[:-oo:]
>>> oo[:999:]
oo[:999:]
>>> oo[999::]
oo[999::]
>>> oo[::999]
oo[::999]
>>> oo[999::, 999::]
oo[999::]
>>> oo[::999, ::999]
oo[::999]

#>>> oo[:999:, ::999]
#>>> oo[:999:, :999:]
#>>> oo[:999:, 999::]
#>>> oo[999::, ::999]
#>>> oo[999::, :999:]
#>>> oo[999::, 999::]

>>> oo[:999:, ::999]
oo[:999:]
>>> oo[:999:, :999:]
oo[:999:]
>>> oo[:999:, 999::]
oo[999::]
>>> oo[999::, ::999]
oo[:999:]
>>> oo[999::, :999:]
oo[:999:]
>>> oo[999::, 999::]
oo[999::]


>>> str(oo)
'OO4repr()'
>>> str(+oo)
'(+oo)'
>>> str(1/+oo)
'Tag_o0o8inv_inf(False, 0)'
>>> str(oo[999::, 999::])
'OpenInterval((1/-oo+999), (1/-oo+999))'






ltle__as_lower_boundary
gtge__as_upper_boundary

>>> (1/+oo+999) in (oo[999::, :+oo:])
True
>>> (1/+oo+999) in (oo[:999:, :+oo:])
True
>>> (1/+oo+999) in (oo[::999, :+oo:])
True
>>> (1/+oo+999) in (oo[:-oo:, 999::])
False
>>> (1/+oo+999) in (oo[:-oo:, :999:])
False
>>> (1/+oo+999) in (oo[:-oo:, ::999])
False

>>> (1/-oo+999) in (oo[999::, :+oo:])
False
>>> (1/-oo+999) in (oo[:999:, :+oo:])
False
>>> (1/-oo+999) in (oo[::999, :+oo:])
False
>>> (1/-oo+999) in (oo[:-oo:, 999::])
True
>>> (1/-oo+999) in (oo[:-oo:, :999:])
True
>>> (1/-oo+999) in (oo[:-oo:, ::999])
True

>>> (+oo) in (oo[:-oo:, :999:])
False
>>> (+oo) in (oo[:999:, :+oo:])
True
>>> (-oo) in (oo[:-oo:, :999:])
True
>>> (-oo) in (oo[:999:, :+oo:])
False


mk_sorted_nonempty_open_intervals
    merge_sorted_nonempty_open_intervals
        union_iterable_of_merged_sorted_nonempty_open_intervals
        mk_merged_sorted_nonempty_open_intervals


>>> mk_sorted_nonempty_open_intervals([oo[:222:,:222:], oo[:222:,:222:], oo[::222,::222], oo[:+oo:,:-oo:], oo[:+oo:,:+oo:], oo[:33:,:66:], oo[:11:,:22:], oo[88::,99::], oo[77::,88::], oo[333::,666::], oo[444::,555::], oo[777::,888::], oo[800::,900::], oo[999::,900::]])
[oo[11::, ::22], oo[33::, ::66], oo[77::, 88::], oo[88::, 99::], oo[:222:], oo[:222:], oo[333::, 666::], oo[444::, 555::], oo[777::, 888::], oo[800::, 900::]]
>>> mk_merged_sorted_nonempty_open_intervals([oo[:222:,:222:], oo[:222:,:222:], oo[::222,::222], oo[:+oo:,:-oo:], oo[:+oo:,:+oo:], oo[:33:,:66:], oo[:11:,:22:], oo[88::,99::], oo[77::,88::], oo[333::,666::], oo[444::,555::], oo[777::,888::], oo[800::,900::], oo[999::,900::]])
(oo[11::, ::22], oo[33::, ::66], oo[77::, 99::], oo[:222:], oo[333::, 666::], oo[777::, 900::])
>>> [*merge_sorted_nonempty_open_intervals(mk_sorted_nonempty_open_intervals([oo[:222:,:222:], oo[:222:,:222:], oo[::222,::222], oo[:+oo:,:-oo:], oo[:+oo:,:+oo:], oo[:33:,:66:], oo[:11:,:22:], oo[88::,99::], oo[77::,88::], oo[333::,666::], oo[444::,555::], oo[777::,888::], oo[800::,900::], oo[999::,900::]]))]
[oo[11::, ::22], oo[33::, ::66], oo[77::, 99::], oo[:222:], oo[333::, 666::], oo[777::, 900::]]

>>> [*union_iterable_of_merged_sorted_nonempty_open_intervals(map(mk_merged_sorted_nonempty_open_intervals
... ,([oo[:222:,:222:], oo[:222:,:222:], oo[::222,::222], oo[:+oo:,:-oo:], oo[:+oo:,:+oo:], oo[:33:,:66:], oo[:11:,:22:], oo[88::,99::], oo[77::,88::], oo[333::,666::], oo[444::,555::], oo[777::,888::], oo[800::,900::], oo[999::,900::]]
...  ,[oo[:222:,:222:], oo[:222:,:222:], oo[::222,::222], oo[:+oo:,:-oo:], oo[:+oo:,:+oo:], oo[:33:,:66:], oo[:11:,:22:], oo[88::,99::], oo[77::,88::], oo[333::,666::], oo[444::,555::], oo[777::,888::], oo[800::,900::], oo[999::,900::]]
... )))]
[oo[11::, ::22], oo[33::, ::66], oo[77::, 99::], oo[:222:], oo[333::, 666::], oo[777::, 900::]]




>>> oo[:-oo:, :-oo:].the_min_or_raise
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.OpenIntervalError__empty: OpenInterval((-oo), (-oo))
>>> oo[:+oo:, :+oo:].the_max_or_raise
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.OpenIntervalError__empty: OpenInterval((+oo), (+oo))

>>> oo[:-oo:, :+oo:].the_min_or_raise
(-oo)
>>> oo[:-oo:, :+oo:].the_max_or_raise
(+oo)
>>> oo[:999:].the_min_or_raise
999
>>> oo[:999:].the_max_or_raise
999
>>> oo[:999:].the_min_max_pair_or_raise
(999, 999)


>>> oo[::999, ::999].the_min_max_pair_or_raise
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.OpenIntervalError__empty: OpenInterval((1/+oo+999), (1/+oo+999))
>>> oo[::999, 999::].the_min_max_pair_or_raise
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.OpenIntervalError__empty: OpenInterval((1/+oo+999), (1/-oo+999))
>>> oo[999::, ::999].the_min_max_pair_or_raise
(999, 999)
>>> oo[999::, 999::].the_min_max_pair_or_raise
Traceback (most recent call last):
    ...
seed.tiny_.oo8inf.OpenIntervalError__empty: OpenInterval((1/-oo+999), (1/-oo+999))








#>>> oo[::666, ::999].the_min_max_pair_or_raise
#>>> oo[::666, 999::].the_min_max_pair_or_raise
#>>> oo[666::, ::999].the_min_max_pair_or_raise
#>>> oo[666::, 999::].the_min_max_pair_or_raise


>>> oo[::666, ::999].the_min_max_pair_or_raise
((1/+oo+666), 999)
>>> oo[::666, 999::].the_min_max_pair_or_raise
((1/+oo+666), (1/-oo+999))
>>> oo[666::, ::999].the_min_max_pair_or_raise
(666, 999)
>>> oo[666::, 999::].the_min_max_pair_or_raise
(666, (1/-oo+999))



#]]]'''
__all__ = r'''
oo
OpenInterval


#]]]'''
__all__ = r'''
oo
OpenInterval
mk_sorted_nonempty_open_intervals
    merge_sorted_nonempty_open_intervals
        union_iterable_of_merged_sorted_nonempty_open_intervals
        mk_merged_sorted_nonempty_open_intervals
negation_merged_sorted_nonempty_open_intervals
intersection_iterable_of_merged_sorted_nonempty_open_intervals

mk_open_intervals5hex2sz
    mk_open_intervals5IRanges
    mk_open_intervals5rngs





BaseError4OO8inf
    Error__NaN
    Error__Div0
OO8inf
    inf__pos
    inf__neg
OO4repr
    oo









Tag_o0o8inv_inf
    inv_inf__pos
    inv_inf__neg


OpenIntervalError
    OpenIntervalError__empty
OpenInterval
    check_boundary
    check_open_interval
'''.split()#'''
__all__
___begin_mark_of_excluded_global_names__0___ = ...
import weakref
from numbers import Number, Integral
from seed.tiny_.check import check_type_is, check_type_le, check_int_ge

from seed.tiny_.containers import mk_tuple, null_tuple, null_iter

from seed.helper.lazy_import__func import lazy_import4func_, lazy_import4funcs_
repr_helper = lazy_import4func_('seed.helper.repr_input', 'repr_helper', __name__)
if 0:from seed.helper.repr_input import repr_helper
___end_mark_of_excluded_global_names__0___ = ...

class BaseError4OO8inf(Exception):pass
class Error__NaN(BaseError4OO8inf):pass
class Error__Div0(BaseError4OO8inf, ZeroDivisionError):pass

class OO8inf(Number):
    _0_frozen_0_ = False
    def __init_subclass__(cls, /):
        if __class__._0_frozen_0_:raise TypeError(cls)
    def __new__(cls, is_neg, /):
        try:
            return inf__neg if is_neg else inf__pos
        except NameError:
            pass

        if cls._0_frozen_0_:raise TypeError(cls)
        check_type_is(bool, is_neg)
        sf = super(__class__, cls).__new__(cls)
        sf._neg = is_neg
        return sf

    def as_rng_boundary(sf, /, *, char_ok=False, inf_ok=False):
        '[inf_ok] => sf #to support OpenInterval.to_rng()'
        del char_ok
        if not inf_ok:raise ValueError(sf)
        return sf
    def as_sorted_pseudo_boundary_pair(sf, /):
        'to support OpenInterval.the_min_or_raise/the_max_or_raise'
        return (sf, sf)
    def ltle__as_lower_boundary(sf, ot, /):
        'to support OpenInterval.__contains__'
        if not sf._neg:
            # +oo < ot
            # exclude +oo
            return sf < ot
        # -oo <= ot
        # include -oo
        return sf <= ot
    def gtge__as_upper_boundary(sf, ot, /):
        'to support OpenInterval.__contains__'
        if not sf._neg:
            # +oo >= ot
            # include +oo
            return sf >= ot
        # -oo > ot
        # exclude -oo
        return sf > ot
    @property
    def _repr6slice(sf, /):
        'to support OpenInterval.__repr__'
        sign = '+-'[sf._neg]
        return f':{sign}oo:'
    def __repr__(sf, /):
        'supported by OO4repr.__pos__&.__neg__'
        return '(-oo)' if sf._neg else '(+oo)'
        return '-oo' if sf._neg else '+oo'
    def __bool__(sf, /):
        return True

    def __hash__(sf, /):
        return id(sf)
    def __eq__(sf, ot, /):
        return sf is ot
    def __lt__(sf, ot, /):
        return sf is not ot if sf._neg else False
    def __gt__(sf, ot, /):
        return False if sf._neg else sf is not ot

    def __le__(sf, ot, /):
        return not sf > ot
    def __ge__(sf, ot, /):
        return not sf < ot
    def __ne__(sf, ot, /):
        return not sf == ot



    def __abs__(sf, /):
        return inf__pos
    def __pos__(sf, /):
        return sf
    def __neg__(sf, /):
        return inf__pos if sf._neg else inf__neg

    def __add__(sf, ot, /):
        if -sf is not ot:
            return sf
        raise Error__NaN
    def __sub__(sf, ot, /):
        if sf is not ot:
            return sf
        raise Error__NaN
    def __mul__(sf, ot, /):
        if abs(ot) == inv_inf__pos:
            raise Error__NaN
        if ot > 0:
            return sf
        if ot < 0:
            return -sf
        if ot == 0:
            raise Error__NaN
        raise 000
    def __truediv__(sf, ot, /):
        if abs(ot) is inf__pos:
            raise Error__NaN
        if ot > 0:
            return sf
        if ot < 0:
            return -sf
        if ot == 0:
            raise Error__Div0
        raise 000
    def __floordiv__(sf, ot, /):
        # !! [limit{a//b | [a-->+oo]} = [b==0]error + [b>0](+oo) + [b<0](-oo)]
        # !! [limit{a//b | [a-->-oo]} = [b==0]error + [b>0](-oo) + [b<0](+oo)]
        return sf / ot
    #xxx:def __mod__(sf, ot, /):
    #xxx:def __divmod__(sf, ot, /):
    #xxx:def __and__(sf, ot, /):
    #xxx:def __or__(sf, ot, /):
    #xxx:def __xor__(sf, ot, /):
    def __lshift__(sf, ot, /):
        # sf * 2**ot
        if ot is inf__neg:
            # ([+-]oo) * 2**(-oo)
            # ([+-]oo) * 0
            raise Error__NaN
        # ([+-]oo) * (+oo|...{>0})
        return sf
    def __rshift__(sf, ot, /):
        # sf * 2**(-ot)
        if ot is inf__pos:
            # ([+-]oo) * 2**(-oo)
            # ([+-]oo) * 0
            raise Error__NaN
        # ([+-]oo) * (+oo|...{>0})
        return sf
    def __pow__(sf, ot, /):
        # sf ** ot
        if abs(ot) == inv_inf__pos:
            raise Error__NaN
        if ot < 0:
            # ([+-]oo)**(-oo|{<0})
            return 0
        if ot == 0:
            # ([+-]oo) ** 0
            return 1

        # ([+-]oo) ** (+oo|{not <=0})
        if not sf._neg:
            # +oo
            # (+oo) ** (+oo|{not <=0})
            if ot > 0:
                return sf
            raise 000
        # -oo
        # (-oo) ** (+oo|{not <=0})
        if not ot > 0:
            raise 000
        # [ot > 0]
        if ot is inf__pos:
            # (-oo)**(+oo)
            # [+-]??
            raise Error__NaN
        # (-oo)**({>0}&&not +oo)
        if isinstance(ot, Integral):
            if ot & 1:
                #odd
                # (-oo)**odd
                return sf
            #even
            # (-oo)**even
            return -sf
        raise TypeError(type(ot))






    def __radd__(sf, ot, /):
        return sf + ot
    def __rsub__(sf, ot, /):
        return -(sf - ot)
    def __rmul__(sf, ot, /):
        if abs(ot) == inv_inf__pos:
            raise Error__NaN
        return sf * ot
    def __rtruediv__(sf, ot, /):
        'to support Tag_o0o8inv_inf.__repr__'
        # ot / sf
        if abs(ot) is inf__pos:
            raise Error__NaN
        if ot == 0:
            return 0
        ##return 0
        return inv_inf__pos if (ot < 0) is sf._neg else inv_inf__neg
        #bug:return inv_inf__pos if ot > 0 else (inv_inf__neg if ot < 0 else 0)
    def __rfloordiv__(sf, ot, /):
        # ot // sf
        if abs(ot) is inf__pos:
            raise Error__NaN
        #bug:return 0
        #   !! [limit{a//b | [b-->+oo]} = [a>=0]0 + [a<0](-1)]
        #   !! [limit{a//b | [b-->-oo]} = [a<=0]0 + [a>0](-1)]
        if ot < 0:
            return 0 if sf._neg else -1
        if ot > 0:
            return -1 if sf._neg else 0
        if ot == 0:
            return 0
        raise 000
    #xxx:def __rmod__(sf, ot, /):
    #xxx:def __rdivmod__(sf, ot, /):
    #xxx:def __rand__(sf, ot, /):
    #xxx:def __ror__(sf, ot, /):
    #xxx:def __rxor__(sf, ot, /):
    def __rlshift__(sf, ot, /):
        # ot * 2**sf
        if sf._neg:
            # ot * 2**(-oo)
            # ot * (+0)
            if abs(ot) is inf__pos:
                raise Error__NaN
            ##return 0
            ##return inv_inf__pos * ot
            if ot == 0:
                return 0
            return inv_inf__pos if not ot < 0 else inv_inf__neg
        # ot * 2**(+oo)
        # ot * (+oo)
        # ot * sf
        return sf * ot
    def __rrshift__(sf, ot, /):
        # ot * 2**(-sf)
        #bug:return __class__.__lshift__(-sf, ot)
        return __class__.__rlshift__(-sf, ot)

    def __rpow__(sf, ot, /):
        # ot ** sf
        if isinstance(ot, Tag_o0o8inv_inf):
            if ot.offset == 1:
                raise Error__NaN
        if abs(ot) > 1:
            # ([+-]oo|{>1}|{<-1})**([+-]oo)
            if ot < -1 and not sf._neg:
                # (-oo|{<-1})**(+oo)
                # [+-]??
                raise Error__NaN
            return 0 if sf._neg else inf__pos
                # 0 vs (1/+oo) but sign is what??
        if abs(ot) < 1:
            # ({-1<.<1})**([+-]oo)
            if ot <= 0 and sf._neg:
                # ({-1<.<=0})**(-oo)
                # [+-]??
                raise Error__Div0 if ot == 0 else Error__NaN
            return inf__pos if sf._neg else 0
        if ot == 1:
            return 1
        if ot == -1:
            raise Error__NaN
        raise 000


inf__pos = OO8inf(False)
inf__neg = OO8inf(True)
OO8inf._0_frozen_0_ = True

assert inf__pos is OO8inf(False)
assert inf__neg is OO8inf(True)

class OO4repr:
    _0_frozen_0_ = False
    def __init_subclass__(cls, /):
        if __class__._0_frozen_0_:raise TypeError(cls)
    def __new__(cls, /):
        try:
            return oo
        except NameError:
            pass

        if cls._0_frozen_0_:raise TypeError(cls)
        sf = super(__class__, cls).__new__(cls)
        return sf

    def __repr__(sf, /):
        return repr_helper(sf)

    def __pos__(sf, /):
        'to support OO8inf.__repr__'
        return inf__pos
    def __neg__(sf, /):
        'to support OO8inf.__repr__'
        return inf__neg
    def __getitem__(sf, k, /):
        'to support OpenInterval.__repr__'
        match k:
            case (k0, k1):
                pass
            #case slice(start=None, stop=v, step=None):
            case slice():
                k0 = k1 = k
            case _:
                raise _mk_err4oo_getitem(k)
        low = _tag_o0o5slice(True, k0)
        up = _tag_o0o5slice(False, k1)
        return OpenInterval(low, up)

def _mk_err4oo_getitem(k, /):
    _errmsg4oo_getitem = 'format: (oo[bnd] | oo[bnd, bnd]) where bnd = (:v: | v:: | ::v)'
    return TypeError(_errmsg4oo_getitem, k)
#def _intvl5slice(gt_vs_lt, k, /):
def _tag_o0o5slice(gt_vs_lt, k, /):
    match k:
        case slice(start=None, stop=None, step=None):
            raise _mk_err4oo_getitem(k)
        case slice(start=v, stop=None, step=None):
            gt_vs_lt = True
        case slice(start=None, stop=None, step=v):
            gt_vs_lt = False
        case slice(start=None, stop=v, step=None):
            pass
        case _:
            raise _mk_err4oo_getitem(k)
    gt_vs_lt
    v
    return Tag_o0o8inv_inf(gt_vs_lt, v)

oo = OO4repr()
OO4repr._0_frozen_0_ = True
assert oo is OO4repr()



assert -oo is inf__neg
assert +oo is inf__pos




__all__


class Tag_o0o8inv_inf(Number):
    '([+-]o0o + offset) == (1/[+-]oo + offset) # offset maybe int,str,.. #bug:Number?'
    _0_frozen_0_ = False
    def __init_subclass__(cls, /):
        if __class__._0_frozen_0_:raise TypeError(cls)
    def __new__(cls, gt_vs_lt, offset, /):
        'mk: ([+-]o0o + offset)'
        if not cls is __class__:raise TypeError(cls)
        check_type_is(bool, gt_vs_lt)
        #if offset in [0]:
        if not offset and __class__._0_frozen_0_:
            offset = 0
            sf = inv_inf__neg if gt_vs_lt else inv_inf__pos
        elif isinstance(offset, OO8inf):
            return offset # not sf
        elif isinstance(offset, __class__):
            ot = offset
            if not type(ot) is cls:raise TypeError(type(ot), cls)
            if not ot._lt is gt_vs_lt:raise Error__NaN(gt_vs_lt, ot) #(1/+oo + 1/-oo)
            sf = ot
        else:
            sf = super(__class__, cls).__new__(cls)
            sf._lt = gt_vs_lt
            sf._offset = offset
            sf._h = None
            sf._may_neg = None
        check_type_is(cls, sf)
        return sf

    def as_rng_boundary(sf, /, *, char_ok=False, inf_ok=False):
        '[offset <: int] => int #to support OpenInterval.to_rng()'
        del inf_ok
        offset = sf.offset
        if type(offset) is str:
            s = offset
            if not (char_ok and len(s) == 1): raise TypeError(str)
            ch = s
            offset = ord(ch)
        return offset + (1-sf.gt_vs_lt)
    def as_sorted_pseudo_boundary_pair(sf, /):
        'to support OpenInterval.the_min_or_raise/the_max_or_raise'
        if sf._lt:
            return (sf, sf._offset)
        return (sf._offset, sf)
    def ltle__as_lower_boundary(sf, ot, /):
        'to support OpenInterval.__contains__'
        if sf._lt:
            # 1/-oo+b < ot
            # exclude (1/-oo+b)
            return sf < ot
        # 1/+oo+b <= ot
        # include (1/+oo+b)
        return sf <= ot
    def gtge__as_upper_boundary(sf, ot, /):
        'to support OpenInterval.__contains__'
        if sf._lt:
            # 1/-oo+b >= ot
            # include (1/-oo+b)
            return sf >= ot
        # 1/+oo+b > ot
        # exclude (1/+oo+b)
        return sf > ot
    @property
    def _repr6slice(sf, /):
        'to support OpenInterval.__repr__'
        return f'{sf.offset!r}::' if sf._lt else f'::{sf.offset!r}'
    def __repr__(sf, /):
        'supported by OO8inf.__rtruediv__'
        sign = '+-'[sf._lt]
        ##return f'({sign!s}o0o+{sf.offset!r})'
        return f'(1/{sign!s}oo+{sf.offset!r})'
    def __str__(sf, /):
        return repr_helper(sf, sf._lt, sf._offset)

    __match_args__ = ('gt_vs_lt', 'offset')
    @property
    def offset(sf, /):
        return sf._offset
    @property
    def gt_vs_lt(sf, /):
        return sf._lt

    def __bool__(sf, /):
        return True

    def __hash__(sf, /):
        if sf._h is None:
            sf._h = hash((id(type(sf)), sf._lt, sf._offset))
            return hash(sf)
        return sf._h
    def __eq__(sf, ot, /):
        'match hash()'
        return (sf is ot) or (type(sf) is type(ot) and sf._lt is ot._lt and sf._offset == ot._offset)

    # [unbox sf][not [sf._offset <: type(sf)]] => the __lt__/__gt__ cmp will make progress
    def __lt__(sf, ot, /):
        return ot >= sf._offset if sf._lt else (sf != ot > sf._offset)
    def __gt__(sf, ot, /):
        return (sf != ot < sf._offset) if sf._lt else ot <= sf._offset

    def __le__(sf, ot, /):
        return not sf > ot
    def __ge__(sf, ot, /):
        return not sf < ot
    def __ne__(sf, ot, /):
        return not sf == ot


    def _mk_other_(sf, gt_vs_lt, offset, /):
        ot = type(sf)(gt_vs_lt, offset)
        return ot

    @property
    def _mirror(sf, /):
        'to support OpenInterval.__repr__'
        ot = sf._mk_other_(not sf._lt, sf._offset)
            # vs: (-sf): [+-]offset
        return ot
    def __abs__(sf, /):
        #bug:if sf._lt:
        if sf < 0:
            return -sf
        return sf
    def __pos__(sf, /):
        return sf
    def __neg__(sf, /):
        if sf._may_neg is None:
            ot = sf._mk_other_(not sf._lt, -sf._offset)
            sf._may_neg = weakref.ref(ot)
            ot._may_neg = weakref.ref(sf)
            assert sf is -ot
            assert ot is -sf
            return -sf
        return sf._may_neg()

    def __add__(sf, ot, /):
        if not ot:
            return sf
        offset = sf._offset
        ##offset = ot if offset in [0] else offset+ot
        offset = ot+offset if offset else ot
            #<<== TypeError: unsupported operand type(s) for +: 'int' and 'bytes'
        _ot = sf._mk_other_(sf._lt, offset)
        return _ot
    def __sub__(sf, ot, /):
        return sf + (-ot)
    #def __mul__(sf, ot, /):
    #def __truediv__(sf, ot, /):
    #def __floordiv__(sf, ot, /):
    #xxx:def __mod__(sf, ot, /):
    #xxx:def __divmod__(sf, ot, /):
    #xxx:def __and__(sf, ot, /):
    #xxx:def __or__(sf, ot, /):
    #xxx:def __xor__(sf, ot, /):
    #def __lshift__(sf, ot, /):
    #def __rshift__(sf, ot, /):
    #def __pow__(sf, ot, /):






    def __radd__(sf, ot, /):
        # ot + sf
        return sf + ot
    def __rsub__(sf, ot, /):
        # ot - sf
        return -sf + ot
    #def __rmul__(sf, ot, /):
    #def __rtruediv__(sf, ot, /):
    #def __rfloordiv__(sf, ot, /):
    #xxx:def __rmod__(sf, ot, /):
    #xxx:def __rdivmod__(sf, ot, /):
    #xxx:def __rand__(sf, ot, /):
    #xxx:def __ror__(sf, ot, /):
    #xxx:def __rxor__(sf, ot, /):
    #def __rlshift__(sf, ot, /):
    #def __rrshift__(sf, ot, /):
    #def __rpow__(sf, ot, /):



    def __mul__(sf, ot, /):
        if abs(ot) is inf__pos:
            raise Error__NaN
        if ot == 0:
            return 0
        if abs(sf) == inv_inf__pos:
            return inv_inf__pos if (ot < 0) is sf._lt else inv_inf__neg
        _ot = sf._mk_other_(not sf._lt is (ot < 0), ot * sf._offset)
        return _ot


    def __rmul__(sf, ot, /):
        return sf * ot
    def __truediv__(sf, ot, /):
        # sf / ot
        if isinstance(ot, __class__) and not ot.offset: raise Error__NaN # (1/+oo / (1/+oo))
        if ot == 0:
            raise Error__Div0
        _ot = sf._mk_other_(not sf._lt is (ot < 0), sf._offset / ot)
        return _ot
    def __rtruediv__(sf, ot, /):
        # ot / sf
        if not sf._offset:
            # ot / ([+-]o0o)
            # ot * ([+-]oo)
            inv_sf = inf__neg if sf._lt else inf__pos
            return inv_sf * ot
        # ot / (offset+[+-]o0o)
        # (ot/offset) / (1+[+-]o0o/offset)
        # (ot/offset) * (1-[+-]o0o/offset+...)
        # (ot/offset) - ([+-]o0o*ot/offset**2+...)
        if ot == 0:
            return 0
        _ot = sf._mk_other_(sf._lt is (ot < 0), ot / sf._offset)
        return _ot



inv_inf__pos = Tag_o0o8inv_inf(False, 0)
##inv_inf__neg = -Tag_o0o8inv_inf(True, 0)
inv_inf__neg = -inv_inf__pos
Tag_o0o8inv_inf._0_frozen_0_ = True

assert inv_inf__pos == Tag_o0o8inv_inf(False, 0)
assert inv_inf__neg == Tag_o0o8inv_inf(True, 0)

##class O0O4repr:
##    _0_frozen_0_ = False
##    def __init_subclass__(cls, /):
##        if __class__._0_frozen_0_:raise TypeError(cls)
##    def __new__(cls, /):
##        try:
##            return o0o
##        except NameError:
##            pass
##
##        if cls._0_frozen_0_:raise TypeError(cls)
##        sf = super(__class__, cls).__new__(cls)
##        return sf
##
##    def __repr__(sf, /):
##        return repr_helper(sf)
##
##    def __pos__(sf, /):
##        return inv_inf__pos
##    def __neg__(sf, /):
##        return inv_inf__neg
##o0o = O0O4repr()
##O0O4repr._0_frozen_0_ = True
##assert o0o is O0O4repr()
##
##assert -o0o is inv_inf__neg
##assert +o0o is inv_inf__pos




assert hash(0) == 0
assert hash(False) == 0
assert hash(1) == 1
assert hash(True) == 1

_Ts4boundary = (Tag_o0o8inv_inf, OO8inf)
def __():
    for T in _Ts4boundary:
        T._repr6slice
__()
def check_boundary(boundary, /):
    check_type_le(_Ts4boundary, boundary)
def check_open_interval(lower_boundary, upper_boundary, /):
    check_boundary(lower_boundary)
    check_boundary(upper_boundary)
    #if not lower_boundary <= upper_boundary:raise ValueError
##def check_lower_boundary(lower_boundary, /):
##    check_type_le(_Ts4boundary, lower_boundary)
##    if lower_boundary is inf__pos:raise ValueError
##def check_upper_boundary(upper_boundary, /):
##    check_type_le(_Ts4boundary, upper_boundary)
##    if upper_boundary is inf__neg:raise ValueError

class OpenIntervalError(Exception):pass
class OpenIntervalError__empty(OpenIntervalError):pass
class OpenInterval:
    r'''[[[
    '[total_ordering][boundary :: (OO8inf|Tag_o0o8inv_inf)][emay_boundary :: (...|boundary)]'

    (OO8inf|Tag_o0o8inv_inf).ltle__as_lower_boundary/gtge__as_upper_boundary && (Tag_o0o8inv_inf).as_sorted_pseudo_boundary_pair
        <<==:
    NOTE: for the sake to pick one element out from nonempty interval, we have the following conventions:
        [-oo < b < +oo]:
            [_b := 1/+oo + b]
            [b_ := 1/-oo + b]
            [-oo < b_ < b < _b < +oo]

            [b <- oo[-oo, _b]]
            [b <-/- oo[_b, +oo]]
            [_b <-/- oo[-oo, _b]]
            [_b <- oo[_b, +oo]]

            [b <-/- oo[-oo, b_]]
            [b <- oo[b_, +oo]]
            [b_ <- oo[-oo, b_]]
            [b_ <-/- oo[b_, +oo]]
        [+oo <- oo[-oo,+oo]]
        [-oo <- oo[-oo,+oo]]
        [+oo <-/- oo[-oo,-oo]]
        [-oo <-/- oo[-oo,-oo]]
        i.e.:
            [oo[-oo, +oo] == math_notation"[-oo, +oo]"]
            [oo[+oo, -oo] == math_notation"(+oo, -oo)"]

            [oo[1/-oo+a, 1/+oo+b] == math_notation"[a, b]"]
            [oo[1/+oo+a, 1/-oo+b] == math_notation"(a, b)"=="[1/+oo+a, 1/-oo+b]"]

        i.e.
            "[+oo, ...]" --> "+oo < ..."
            "[-oo, ...]" --> "-oo <= ..."
            "[1/+oo+b, ...]" --> "1/+oo+b <= ..."
            "[1/-oo+b, ...]" --> "1/-oo+b < ..." --> "b <= ..."
            "[..., 1/-oo+b]" --> "... <= 1/-oo+b"
            "[..., 1/+oo+b]" --> "... < 1/+oo+b" --> "... <= b"
            "[..., +oo]" --> "... <= +oo"
            "[..., -oo]" --> "... < -oo"


    #]]]'''#'''
    def __init__(sf, emay_lower_boundary, emay_upper_boundary, /):
        lower_boundary = inf__neg if emay_lower_boundary is ... else emay_lower_boundary
        upper_boundary = inf__pos if emay_upper_boundary is ... else emay_upper_boundary


        check_open_interval(lower_boundary, upper_boundary)

        sf._low = lower_boundary
        sf._up  = upper_boundary
        sf._h = None
        sf._b = None
        sf._tm_sz = null_tuple
    __match_args__ = ('low', 'up')
    @property
    def low(sf, /):
        '-> lower_boundary'
        return sf._low
    @property
    def up(sf, /):
        '-> upper_boundary'
        return sf._up
    @property
    def span(sf, /):
        '-> (lower_boundary, upper_boundary)'
        return (sf._low, sf._up)
    key4sort = span.fget

    @property
    def the_min_or_raise(sf, /):
        '-> the_min_element_if_nonempty|^OpenIntervalError__empty'
        if not sf:raise OpenIntervalError__empty(sf)
        # !! [bool(sf)]
        # [low =!= +oo]
        # [result =!= +oo] #maybe -oo
        return sf._low.as_sorted_pseudo_boundary_pair()[1]
    @property
    def the_max_or_raise(sf, /):
        '-> the_max_element_if_nonempty|^OpenIntervalError__empty'
        if not sf:raise OpenIntervalError__empty(sf)
        # !! [bool(sf)]
        # [up =!= -oo]
        # [result =!= -oo] #maybe +oo
        return sf._up.as_sorted_pseudo_boundary_pair()[0]
    @property
    def the_min_max_pair_or_raise(sf, /):
        '-> the_min_max_element_pair_if_nonempty|^OpenIntervalError__empty'
        return (sf.the_min_or_raise, sf.the_max_or_raise)
    @property
    def length(sf, /):
        '-> ??? #turnoff:Error__NaN'
        if sf._tm_sz:
            return sf._tm_sz[0]
        elif not sf:
            # (+oo) -(+oo)
            # (1/+oo) -(1/+oo)
            sz = 0
        elif type(sf._up) is Tag_o0o8inv_inf is type(sf._low) and sf._up.gt_vs_lt is sf._low.gt_vs_lt:
            sz = (sf._up.offset -sf._low.offset)
        else:
            try:
                sz = (sf._up -sf._low) #^Error__NaN
            except Error__NaN:
                raise 000
        sz
        #if sz is None:raise TypeError
        sf._tm_sz = (sz,)
        return sf.length
    def __repr__(sf, /):
        'supported by OO4repr.__getitem__'
        if not sf and sf.low == sf.up:
            return f'oo[{sf.low._repr6slice}]'
        if sf and inf__neg is not sf.low and sf.low._mirror == sf.up:
            return f'oo[:{sf.up.offset}:]'
        return f'oo[{sf.low._repr6slice}, {sf.up._repr6slice}]'
    def __str__(sf, /):
        return repr_helper(sf, sf._low, sf._up)
    def __contains__(sf, k, /):
        #bug:return bool(sf) and sf._low < k and sf._up > k
        return bool(sf) and sf._low.ltle__as_lower_boundary(k) and sf._up.gtge__as_upper_boundary(k)
    def __bool__(sf, /):
        '-> is_interval_nonempty/bool'
        if sf._b is None:
            sf._b = sf._low < sf._up
            return bool(sf)
        return sf._b

    def __hash__(sf, /):
        if sf._h is None:
            sf._h = hash((id(type(sf)), sf._low, sf._up))
            return hash(sf)
        return sf._h
    def __eq__(sf, ot, /):
        'match hash()'
        return type(sf) is type(ot) and sf._low == ot._low and sf._up == ot._up

    ##def __lt__(sf, ot, /):
    ##    'to_support_sort:[to support sorted() instead of set inclusion cmp]'
    ##    if not type(ot) is type(sf):
    ##        return NotImplemented
    ##    return sf.span < ot.span
    ##def __gt__(sf, ot, /):
    ##    if not type(ot) is type(sf):
    ##        return NotImplemented
    ##    return ot < sf

    ##def __le__(sf, ot, /):
    ##    return not sf > ot
    ##def __ge__(sf, ot, /):
    ##    return not sf < ot
    def __ne__(sf, ot, /):
        return not sf == ot
    @classmethod
    def from_rng(cls, rng, /):
        (begin, end) = rng
        return oo[begin::, end::]
        777; 'asif (begin-0.5, end-0.5)'
    def to_rng(sf, /, *, char_ok=False, inf_ok=False):
        begin = sf.low.as_rng_boundary(char_ok=char_ok, inf_ok=inf_ok)
        end = sf.up.as_rng_boundary(char_ok=char_ok, inf_ok=inf_ok)
        return (begin, end)
    def to_then_from_rng(sf, /, *, char_ok=False, inf_ok=False):
        return type(sf).from_rng(sf.to_rng(char_ok=char_ok, inf_ok=inf_ok))

def mk_open_intervals5hex2sz(hex2sz, /):
    '{int:uint} -> [OpenInterval]'
    from seed.data_funcs.rngs import IRanges
    ranges = IRanges.from_hex2sz(hex2sz)
    return mk_open_intervals5IRanges(ranges)
def mk_open_intervals5IRanges(ranges, /):
    'IRanges -> [OpenInterval]'
    return mk_open_intervals5rngs(ranges.ranges)
def mk_open_intervals5rngs(rngs, /):
    '[(int,int)]{sored,nonoverlapped} -> [OpenInterval]'
    return mk_tuple(map(OpenInterval.from_rng, rngs))

def mk_sorted_nonempty_open_intervals(open_intervals, /):
    'Iter OpenInterval -> [nonempty-OpenInterval]{sorted}'
    sorted_nonempty_open_intervals = sorted(filter(None, open_intervals), key=OpenInterval.key4sort)
    return sorted_nonempty_open_intervals

def mk_merged_sorted_nonempty_open_intervals(open_intervals, /):
    'Iter OpenInterval -> [nonempty-OpenInterval]{sorted,merged/(nonoverlap&&nontouch)}'
    sorted_nonempty_open_intervals = mk_sorted_nonempty_open_intervals(open_intervals)

    return mk_tuple(merge_sorted_nonempty_open_intervals(sorted_nonempty_open_intervals))


def negation_merged_sorted_nonempty_open_intervals(merged_sorted_nonempty_open_intervals, /):
    'merged_sorted_nonempty_open_intervals -> merged_sorted_nonempty_open_intervals/(Iter OpenInterval){[sorted by .key4sort/.span][merged/(nonoverlap&&nontouch)]}'
    b = -oo
    for intvl in merged_sorted_nonempty_open_intervals:
        if b < intvl.low:
            yield OpenInterval(b, intvl.low)
        b = intvl.up
    if b < +oo:
        yield OpenInterval(b, +oo)
    return


def union_iterable_of_merged_sorted_nonempty_open_intervals(merged_sorted_nonempty_open_intervalss, /):
    'Iter merged_sorted_nonempty_open_intervals -> merged_sorted_nonempty_open_intervals/(Iter OpenInterval){[sorted by .key4sort/.span][merged/(nonoverlap&&nontouch)]}'
    merged_sorted_nonempty_open_intervalss = mk_tuple(merged_sorted_nonempty_open_intervalss)
    L = len(merged_sorted_nonempty_open_intervalss)
    if L < 2:
        if L:
            [it] = merged_sorted_nonempty_open_intervalss
            return it
        return null_iter
    return _union_iterable_of_merged_sorted_nonempty_open_intervals(merged_sorted_nonempty_open_intervalss)
def _union_iterable_of_merged_sorted_nonempty_open_intervals(merged_sorted_nonempty_open_intervalss, /):
 
    from heapq import merge
    sorted_nonempty_open_intervals = merge(*merged_sorted_nonempty_open_intervalss, key=OpenInterval.key4sort)
    return merge_sorted_nonempty_open_intervals(sorted_nonempty_open_intervals)
def merge_sorted_nonempty_open_intervals(sorted_nonempty_open_intervals, /):
    'sorted_nonempty_open_intervals/(Iter OpenInterval){sorted by .key4sort/.span} -> merged_sorted_nonempty_open_intervals/(Iter OpenInterval){[sorted by .key4sort/.span][merged/(nonoverlap&&nontouch)]}'
    m = None
    for rhs in sorted_nonempty_open_intervals:
        if not rhs:
            continue
        if m is None:
            m = rhs
            continue
        lhs = m
        # [lhs.low <= rhs.low]
        if rhs.low <= lhs.up:
            # [lhs.low <= rhs.low <= lhs.up]
            if lhs.up < rhs.up:
                # [lhs.low <= rhs.low <= lhs.up < rhs.up]
                #merge
                m = OpenInterval(lhs.low, rhs.up)
            else:
                # [lhs.low <= rhs.low < rhs.up <= lhs.up]
                pass
        else:
            # [lhs.low < lhs.up < rhs.low < rhs.up]
            yield lhs
            m = rhs

    if not m is None:
        lhs = m
        yield lhs
    return



def intersection_iterable_of_merged_sorted_nonempty_open_intervals(merged_sorted_nonempty_open_intervalss, /):
    'Iter merged_sorted_nonempty_open_intervals -> merged_sorted_nonempty_open_intervals/(Iter OpenInterval){[sorted by .key4sort/.span][merged/(nonoverlap&&nontouch)]}'
    merged_sorted_nonempty_open_intervalss = mk_tuple(merged_sorted_nonempty_open_intervalss)
    L = len(merged_sorted_nonempty_open_intervalss)
    if L < 2:
        if L:
            [it] = merged_sorted_nonempty_open_intervalss
            return it
        return null_iter
    return _intersection_iterable_of_merged_sorted_nonempty_open_intervals(merged_sorted_nonempty_open_intervalss)
def _intersect_two_merged_sorted_nonempty_open_intervalss(lhs, rhs, /):
    from seed.iters.PeekableIterator import PeekableIterator
    #lhs = PeekableIterator(lhs)
    check_type_is(PeekableIterator, lhs)
    rhs = PeekableIterator(rhs)
    while not (lhs.is_empty() or rhs.is_empty()):
        lkey = lhs.head
            # ^StopIteration
        rkey = rhs.head
            # ^StopIteration
            #
            # ???RuntimeError: generator raised StopIteration
            #
        if lkey.up <= rkey.low:
            next(lhs)
        elif rkey.up <= lkey.low:
            next(rhs)
        else:
            # [(*.low) < (*.up)]
            # [max(*.low) < min(*.up)]
            max_low = max(lkey.low, rkey.low)
            lhs_has_min_up = lkey.up < rkey.up
            (min_up, max_up) = (lkey.up, rkey.up) if lhs_has_min_up else (rkey.up, lkey.up)

            yield OpenInterval(max_low, min_up)
            if lhs_has_min_up:
                lt, gt = lhs, rhs
            else:
                lt, gt = rhs, lhs
            next(lt)
            next(gt)
            tail = OpenInterval(min_up, max_up)
            if tail:
                gt.append_left(tail)

    return
def _intersection_iterable_of_merged_sorted_nonempty_open_intervals(merged_sorted_nonempty_open_intervalss, /):
    from seed.iters.PeekableIterator import PeekableIterator
    assert len(merged_sorted_nonempty_open_intervalss) >= 2
    it = map(iter, merged_sorted_nonempty_open_intervalss)
    lhs = next(it)
    for rhs in it:
        lhs = PeekableIterator(lhs)
        if lhs.is_empty():
            break
        lhs = _intersect_two_merged_sorted_nonempty_open_intervalss(lhs, rhs)
    return lhs


__all__

from seed.tiny_.oo8inf import oo, OpenInterval
from seed.tiny_.oo8inf import mk_merged_sorted_nonempty_open_intervals
from seed.tiny_.oo8inf import \
(mk_sorted_nonempty_open_intervals
,   merge_sorted_nonempty_open_intervals
,       union_iterable_of_merged_sorted_nonempty_open_intervals
,       mk_merged_sorted_nonempty_open_intervals
,negation_merged_sorted_nonempty_open_intervals
,intersection_iterable_of_merged_sorted_nonempty_open_intervals
,mk_open_intervals5hex2sz
,   mk_open_intervals5IRanges
,   mk_open_intervals5rngs
)

from seed.tiny_.oo8inf import *
