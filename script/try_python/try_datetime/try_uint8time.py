
r'''
py -m script.try_python.try_datetime.try_uint8time
e ../../python3_src/script/try_python/try_datetime/try_uint8time.py

由来:
    手机-阅读app.finalDate属性:例:1647303785952
    is Python.timestamp???
        No. OverflowError
        #OverflowError: timestamp out of range for platform time_t
    but [div 1000 is Python.timestamp]
        (datetime.datetime.fromtimestamp(1647303785952/1000))
            #2022-03-15 08:23:05.952000
#'''


import datetime as dt

#print(dir(dt))
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']

#print(dir(dt.datetime))
['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fold', 'fromisocalendar', 'fromisoformat', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year']

#print(dt.datetime.fromtimestamp(1647303785952))
    #OverflowError: timestamp out of range for platform time_t


#print(dir(dt.time))
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'dst', 'fold', 'fromisoformat', 'hour', 'isoformat', 'max', 'microsecond', 'min', 'minute', 'replace', 'resolution', 'second', 'strftime', 'tzinfo', 'tzname', 'utcoffset']    


#print(dir(dt.date))
['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'ctime', 'day', 'fromisocalendar', 'fromisoformat', 'fromordinal', 'fromtimestamp', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'min', 'month', 'replace', 'resolution', 'strftime', 'timetuple', 'today', 'toordinal', 'weekday', 'year']

#print(dt.datetime.now())
#2022-03-15 18:05:27.285931

#print(dt.datetime.now().time())
#18:08:16.662627

#print(dt.datetime.now().second)
#10

#print(dt.datetime.now().timestamp())
#1647338848.837638
#vs above 1647303785952 -- 1647303785.952

#print(dt.datetime.fromtimestamp(1647303785952/1000))
#2022-03-15 08:23:05.952000
#success!!!


#print(dir(float))
#print((int(dt.datetime.now().timestamp()*1000)))
#1647339733874


print(dt.datetime.fromtimestamp(0.0))
#1970-01-01 08:00:00

