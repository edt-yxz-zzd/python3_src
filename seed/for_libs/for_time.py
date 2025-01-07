#__all__:goto
r'''[[[
e ../../python3_src/seed/for_libs/for_time.py

[[
===
duration types:
    float
        unit:second
        resolution:???
    timedelta
        resolution:microsecond
===
timezone types:
    tzinfo(ABC)
    timezone(tzinfo)
===
time types:
    timestamp<platform_epoch>/float
        aware
        platform dependent
        ===
        unit:second
        resolution:???
    time_struct/struct_time
        naive
        ===
        resolution:second
    datetime<may_tz>
        naive_datetime<>
        aware_datetime<tz>
        ===
        resolution:microsecond

    formatted_str<smay_utcoffset>
        naive_formatted_str<>
        aware_formatted_str<utcoffset>
        ===
        * isoformat/fromisoformat
            timespec
            Case4datetime_isoformat_timespec

        * strftime/strptime
            time_fmt
            TimeFormatDirective
                '%z' time_zone_offset__5char__7char__14char
===
]]





seed.for_libs.for_time
py -m nn_ns.app.debug_cmd   seed.for_libs.for_time -x
py -m nn_ns.app.doctest_cmd seed.for_libs.for_time:__doc__ -ff -v
py_adhoc_call   seed.for_libs.for_time   @f

from seed.for_libs.for_time import (
time_struct8platform_epoch___tz4utc
,time_struct8platform_epoch___tz4local
,aware_datetime8platform_epoch
,tz4utc
,tz4local





,Case4datetime_isoformat_timespec
,TimeFormatDirective
    ,time_fmt5py_str_fmt_
    ,time_fmt5snippets_
,default_time_fmt
    ,time_fmt5may_



,get_now__timestamp
,get_now__time_struct_
,get_now__aware_datetime_

,get_consumed_duration__system_wide__monotonic
,get_consumed_duration__system_wide__highest_resolution
,get_consumed_duration__process_wide
,get_consumed_duration__thread_wide


,Timer
    ,timer__thread_wide
    ,timer__process_wide
    ,timer__system_wide__highest_resolution
    ,timer__system_wide__monotonic

    ,Timer__print_err
        ,timer__print_err__thread_wide
        ,timer__print_err__process_wide
        ,timer__print_err__system_wide__highest_resolution
        ,timer__print_err__system_wide__monotonic




,aware_datetime5timestamp_
,aware_datetime2timestamp_

,aware_datetime5formatted_str_
,aware_datetime2formatted_str_

,timestamp2formatted_str__via_datetime__
,timestamp5formatted_str__via_datetime__

,datetime2formatted_str_
,datetime5formatted_str_

,time_struct5timestamp_
,time_struct2timestamp_

,time_struct2formatted_str_
,time_struct5formatted_str_

,timestamp2formatted_str__via_time_struct__
,timestamp5formatted_str__via_time_struct__



,is_datetime_aware
,is_datetime_naive
,check_aware_datetime
)




[[
time — Time access and conversions¶

This module provides various time-related functions.
    For related functionality, see also the datetime and calendar modules.

Although this module is always available, not all functions are available on all platforms.
    Most of the functions defined in this module call platform C library functions with the same name.
    It may sometimes be helpful to consult the platform documentation, because the semantics of these functions varies among platforms.


An explanation of some terminology and conventions is in order.

The epoch is the point where the time starts, and is platform dependent.
    For Unix, the epoch is January 1, 1970, 00:00:00 (UTC).  To find out what the epoch is on a given platform, look at time.gmtime(0).


The term seconds since the epoch refers to the total number of elapsed seconds since the epoch, typically excluding leap seconds.
    Leap seconds are excluded from this total on all POSIX-compliant platforms.


The functions in this module may not handle dates and times before the epoch or far in the future.
    The cut-off point in the future is determined by the C library; for 32-bit systems, it is typically in 2038.


Function strptime() can parse 2-digit years when given %y format code.
    When 2-digit years are parsed, they are converted according to the POSIX and ISO C standards:
        values 69–99 are mapped to 1969–1999
        , and values 0–68 are mapped to 2000–2068.


UTC is Coordinated Universal Time
    (formerly known as Greenwich Mean Time, or GMT).
    The acronym UTC is not a mistake but a compromise between English and French.


DST is Daylight Saving Time
    , an adjustment of the timezone by (usually) one hour during part of the year.
    DST rules are magic (determined by local law) and can change from year to year.
    The C library has a table containing the local rules (often it is read from a system file for flexibility) and is the only source of True Wisdom in this respect.


The precision of the various real-time functions may be less than suggested by the units in which their value or argument is expressed.
    E.g. on most Unix systems, the clock “ticks” only 50 or 100 times a second.
On the other hand, the precision of time() and sleep() is better than their Unix equivalents:
    times are expressed as floating point numbers
    , time() returns the most accurate time available (using Unix gettimeofday() where available)
    , and sleep() will accept a time with a nonzero fraction (Unix select() is used to implement this, where available).

The time value as
    returned by gmtime(), localtime(), and strptime()
    , and accepted by asctime(), mktime() and strftime()
    , is a sequence of 9 integers.
    The return values of gmtime(), localtime(), and strptime() also offer attribute names for individual fields.
See struct_time for a description of these objects.

Changed in version 3.3: The struct_time type was extended to provide the tm_gmtoff and tm_zone attributes when platform supports corresponding struct tm members.


Changed in version 3.6: The struct_time attributes tm_gmtoff and tm_zone are now available on all platforms.

See also
    datetime
        More object-oriented interface to dates and times.

    locale
        Internationalization services.  The locale setting affects the interpretation
    of many format specifiers in strftime() and strptime().

    calendar
        General calendar-related functions.
        timegm() is the inverse of gmtime() from this module.







duration repr:
    * float/seconds
    * int/seconds
timestamp repr:
    * seconds since undefined reference point
        * float/seconds
        * ??int/seconds
        * int/nanoseconds
        ===
        * system-wide
        * process-wide
        * thread-specific
    * seconds since the epoch
        * float
        * int
    * struct_time/tuple
        * UTC
        * localtime
        * ...
S5_
    ===
    The reference point of the returned value is undefined
        , so that only the difference between the results of consecutive calls is valid.

system-wide vs process-wide vs thread-specific
    * thread-specific:
        not include time elapsed during sleep.
    * process-wide:
        not include time elapsed during sleep.
    * system-wide:
        include time elapsed during sleep
        not includes time that the system is suspended


let DRN := duration

let S5_ := seconds since undefined reference point
let S5E := seconds since the epoch
let STT := struct_time
let LCT := localtime
    #LCT/UTC is a timezone
let WS := system-wide
let WP := process-wide
let WT := thread-specific




1 nanoseconds = 10**-9 seconds
    十亿分之一秒
    纳秒
    毫微秒




time.get_clock_info(name)¶
    -> clock_info
    ===
    name: func
        'monotonic': time.monotonic()
        'perf_counter': time.perf_counter()
        'process_time': time.process_time()
        'thread_time': time.thread_time()
        'time': time.time()
    ===
    clock_info:
        adjustable:
            True <==> the clock can be changed automatically (e.g. by a NTP daemon) or manually by the system administrator
        monotonic:
            True <==> the clock cannot go backward
        resolution:
            The resolution of the clock in seconds (float)
        implementation:
            The name of the underlying C function used to get the clock value.
            Refer to Clock ID Constants for possible values.






time.time_ns() → int¶
    -> S5E<int/nanoseconds>
time.time() → float¶
    --> S5E<float/seconds>
    The specific date of the epoch and the handling of leap seconds is platform dependent.
        To find out what the epoch is on a given platform, look at gmtime(0).
    Note that even though the time is always returned as a floating point number, not all systems provide time with a better precision than 1 second.
    While this function normally returns non-decreasing values, it can return a lower value than a previous call if the system clock has been set back between the two calls.

time.monotonic_ns() → int¶
    -> WS-S5_<int/nanoseconds>
time.monotonic() → float¶
    -> WS-S5_<float/seconds>
    Return the value (in fractional seconds) of a monotonic clock
        , i.e. a clock that cannot go backwards.
        The clock is not affected by system clock updates.



time.perf_counter_ns() → int¶
    -> WS-S5_<int/nanoseconds>
time.perf_counter() → float¶
    -> WS-S5_<float/seconds>
    Return the value (in fractional seconds) of a performance counter
        , i.e. a clock with the highest available resolution to measure a short duration.


time.process_time_ns() → int¶
    -> WP-S5_<int/nanoseconds>
time.process_time() → float¶
    -> WP-S5_<float/seconds>
    Return the value (in fractional seconds) of the sum of the system and user CPU time of the current process.

time.thread_time_ns() → int¶
    -> WT-S5_<int/nanoseconds>
time.thread_time() → float¶
    -> WT-S5_<float/seconds>
    Return the value (in fractional seconds) of the sum of the system and user CPU time of the current thread.  It does not include time elapsed during sleep.
r


time.sleep(secs)¶
    DRN<int/float/seconds> -> None
    Suspend execution of the calling thread for the given number of seconds.
    suspension time may be longer than requested by an arbitrary amount because of the scheduling of other activity in the system.
    sleeps at least secs even if the sleep is interrupted by a signal, except if the signal handler raises an exception (see PEP 475 for the rationale).







calendar.timegm(struct_time) -> timestamp
    STT<UTC> --> S5E
    vs:time.gmtime([timestamp/seconds/float]) -> struct_time
time.gmtime([secs])¶
    S5E --> STT<UTC>
    time.gmtime() === time.gmtime(time())
    vs:calendar.timegm(struct_time) -> timestamp

time.mktime(t)¶
    STT<LCT> --> S5E<float>
time.localtime([secs])¶
    S5E --> STT<LCT>
    time.localtime() === time.localtime(time())
    vs:time.mktime(t)


time.asctime([t])¶
    STT -->:
time.ctime([secs])¶
    S5E -->:
    -->:
        'Sun Jun 20 23:21:05 1993'
        'Wed Jun  9 04:26:40 1993'.
        format="%a %b %d %H:%M:%S %Y"
        see:strptime

    time.ctime(secs) === time.asctime(localtime(secs))
    time.ctime() === time.ctime(time())
    time.asctime() === time.asctime(localtime())


time.strftime(format[, t])¶
    fmt -> STT<UTC|LCT> -> str
    time.strftime(format) === time.strftime(format, localtime())
    vs:strptime()
    timestamp_format:goto

time.strptime(string, format="%a %b %d %H:%M:%S %Y")¶
    str -> fmt -> STT<UTC|LCT>
    vs:strftime()
    timestamp_format:goto
    strptime(ctime()) #<<== default format
    default for output attributes:
        The default values used to fill in any missing data when more accurate values cannot be inferred are
            (1900, 1, 1, 0, 0, 0, 0, 1, -1).

        >>> import time
        >>> time.strptime("30 Nov 00", "%d %b %y")
        time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1)


    Support for the %Z directive is based on the values contained in tzname and whether daylight is true.  Because of this, it is platform-specific except for recognizing UTC and GMT which are always known (and are considered to be non-daylight savings timezones).

    Only the directives specified in the documentation are supported.
        Because strftime() is implemented per platform it can sometimes offer more directives than those listed.  But strptime() is independent of any platform and thus does not necessarily support all directives available that are not documented as supported.




[[
timestamp_format:here
datetime____strftime__and__strptime__Behavior:goto
===
timestamp format:
Directive:Meaning:Notes


%%
A literal '%' character.


%y
Year without century as a decimal number [00,99].
%Y
Year with century as a decimal number.
%m
Month as a decimal number [01,12].
%j
Day of the year as a decimal number [001,366].
%d
Day of the month as a decimal number [01,31].
%H
Hour (24-hour clock) as a decimal number [00,23].
%I
Hour (12-hour clock) as a decimal number [01,12].
%p
Locale’s equivalent of either AM or PM.  (1)
%M
Minute as a decimal number [00,59].
%S
Second as a decimal number [00,61].  (2)

%z
Time zone offset indicating a positive or negative time difference from UTC/GMT of the form +HHMM or -HHMM, where H represents decimal hour digits and M represents decimal minute digits [-23:59, +23:59].
%Z
Time zone name (no characters if no time zone exists).




%w
Weekday as a decimal number [0(Sunday),6].

%U
Week number of the year (Sunday as the first day of the week) as a decimal number [00,53].
All days in a new year preceding the first Sunday are considered to be in week 0.  (3)

%W
Week number of the year (Monday as the first day of the week) as a decimal number [00,53].
All days in a new year preceding the first Monday are considered to be in week 0.  (3)

%a
Locale’s abbreviated weekday name.
%A
Locale’s full weekday name.

%b
Locale’s abbreviated month name.
%B
Locale’s full month name.


%c
Locale’s appropriate date and time representation.
%x
Locale’s appropriate date representation.
%X
Locale’s appropriate time representation.








Notes:

When used with the strptime() function, the %p directive only affects the output hour field if the %I directive is used to parse the hour.
The range really is 0 to 61; value 60 is valid in timestamps representing leap seconds and value 61 is supported for historical reasons.
When used with the strptime() function, %U and %W are only used in calculations when the day of the week and the year are specified.

Here is an example, a format for dates compatible with that specified  in the
RFC 2822 Internet email standard.  1
>>> from time import gmtime, strftime #doctest: +SKIP
>>> strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()) #doctest: +SKIP
'Thu, 28 Jun 2001 14:17:15 +0000'


]]

]]
[[
datetime — Basic date and time types¶
===
aware object 保存充分信息，无歧义
naive object 保存信息不完整，一般靠本地配置(localtime之类)解释
===
Aware and Naive Objects¶
Date and time objects may be categorized as “aware” or “naive.”

With sufficient knowledge of applicable algorithmic and political time adjustments, such as time zone and daylight saving time information, an aware object can locate itself relative to other aware objects.
An aware object represents a specific moment in time that is not open to interpretation. 1

A naive object does not contain enough information to unambiguously locate itself relative to other date/time objects.
    Whether a naive object represents Coordinated Universal Time (UTC), local time, or time in some other timezone is purely up to the program, just like it is up to the program whether a particular number represents metres, miles, or mass.
    Naive objects are easy to understand and to work with, at the cost of ignoring some aspects of reality.

For applications requiring aware objects, datetime and time objects have an optional time zone information attribute, tzinfo, that can be set to an instance of a subclass of the abstract tzinfo class.
    These tzinfo objects capture information about the offset from UTC time, the time zone name, and whether daylight saving time is in effect.
Only one concrete tzinfo class, the timezone class, is supplied by the datetime module.
    The timezone class can represent simple timezones with fixed offsets from UTC, such as UTC itself or North American EST and EDT timezones.
    Supporting timezones at deeper levels of detail is up to the application.
        The rules for time adjustment across the world are more political than rational, change frequently, and there is no standard suitable for every application aside from UTC.


===
datetime.MINYEAR = 1
datetime.MAXYEAR = 9999
    The smallest/largest year number allowed in a date or datetime object.



[[
datetime____strftime__and__strptime__Behavior:here
timestamp_format:goto
===

%f
Microsecond as a decimal number, zero-padded on the left.
000000, 000001, …, 999999
(5)

%z
UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive).
(empty), +0000, -0400, +1030, +063415, -030712.345216


Several additional directives not required by the C89 standard are included for convenience. These parameters all correspond to ISO 8601 date values.
%G
ISO 8601 year with century representing the year that contains the greater part of the ISO week (%V).
0001, 0002, …, 2013, 2014, …, 9998, 9999
(8)

%u
ISO 8601 weekday as a decimal number where 1 is Monday.
1, 2, …, 7


%V
ISO 8601 week as a decimal number with Monday as the first day of the week.
Week 01 is the week containing Jan 4.
01, 02, …, 53
(8), (9)



These may not be available on all platforms when used with the strftime() method. The ISO 8601 year and ISO 8601 week directives are not interchangeable with the year and week number directives above. Calling strptime() with incomplete or ambiguous ISO 8601 directives will raise a ValueError.

]]

]]



    time_struct8platform_epoch___tz4utc
    time_struct8platform_epoch___tz4local
>>> time_struct8platform_epoch___tz4utc
time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
>>> time_struct8platform_epoch___tz4local
time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=8, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)


    get_now__timestamp
>>> timestamp = get_now__timestamp()
>>> type(timestamp) is float
True

>>> timestamp = float.fromhex('0x1.93939985bce89p+30')
>>> timestamp
1692722785.434481
>>> timestamp.hex()
'0x1.93939985bce89p+30'

    time_struct5timestamp_
    time_struct2timestamp_
    #loss accuracy: [resolution==1 second] i.e. be int when converted back, see:timegm__int
    #use datetime instead
>>> local_time_struct = time_struct5timestamp_(False, timestamp)
>>> local_time_struct
time.struct_time(tm_year=2023, tm_mon=8, tm_mday=23, tm_hour=0, tm_min=46, tm_sec=25, tm_wday=2, tm_yday=235, tm_isdst=0)
>>> timestamp_5local = time_struct2timestamp_(False, local_time_struct)
>>> timestamp_5local
1692722785.0

>>> utc_time_struct = time_struct5timestamp_(True, timestamp)
>>> utc_time_struct
time.struct_time(tm_year=2023, tm_mon=8, tm_mday=22, tm_hour=16, tm_min=46, tm_sec=25, tm_wday=1, tm_yday=234, tm_isdst=0)
>>> timestamp_5utc_ = timegm__int(utc_time_struct)
>>> timestamp_5utc_
1692722785
>>> timestamp_5utc = time_struct2timestamp_(True, utc_time_struct)
>>> timestamp_5utc
1692722785.0
>>> type(timestamp_5local) is float
True
>>> type(timestamp_5utc) is float
True
>>> type(timestamp_5utc_) is int
True


    TimeFormatDirective
        time_fmt5py_str_fmt_
        time_fmt5snippets_
    default_time_fmt
        time_fmt5may_
>>> default_time_fmt == "%a %b %d %H:%M:%S %Y"
True
>>> __ = TimeFormatDirective
>>> default_time_fmt == time_fmt5snippets_(__.W_abbr, ' ', __.M_abbr, ' ', __.DD, ' ', __.hh, ':', __.mm, ':', __.ss, ' ', __.YYYY)
True
>>> default_time_fmt == time_fmt5py_str_fmt_('{W_abbr} {M_abbr} {DD} {hh}:{mm}:{ss} {YYYY}')
True
>>> time_fmt5py_str_fmt_('%')
'%%'


    time_struct2formatted_str_
    time_struct5formatted_str_
>>> time_struct2formatted_str_(None, local_time_struct)
'Wed Aug 23 00:46:25 2023'
>>> time_struct5formatted_str_(None, _)
time.struct_time(tm_year=2023, tm_mon=8, tm_mday=23, tm_hour=0, tm_min=46, tm_sec=25, tm_wday=2, tm_yday=235, tm_isdst=-1)
>>> time_struct2formatted_str_(None, utc_time_struct)
'Tue Aug 22 16:46:25 2023'
>>> time_struct5formatted_str_(None, _)
time.struct_time(tm_year=2023, tm_mon=8, tm_mday=22, tm_hour=16, tm_min=46, tm_sec=25, tm_wday=1, tm_yday=234, tm_isdst=-1)


    timestamp2formatted_str__via_time_struct__
    timestamp5formatted_str__via_time_struct__
>>> timestamp2formatted_str__via_time_struct__(None, False, timestamp)
'Wed Aug 23 00:46:25 2023'
>>> timestamp5formatted_str__via_time_struct__(None, False, _)
1692722785.0
>>> timestamp2formatted_str__via_time_struct__(None, True, timestamp)
'Tue Aug 22 16:46:25 2023'
>>> timestamp5formatted_str__via_time_struct__(None, True, _)
1692722785.0


    get_consumed_duration__system_wide__monotonic
    get_consumed_duration__system_wide__highest_resolution
    get_consumed_duration__process_wide
    get_consumed_duration__thread_wide

>>> get_consumed_duration__system_wide__monotonic() #doctest: +SKIP
13735536.812056776
>>> get_consumed_duration__system_wide__highest_resolution() #doctest: +SKIP
13735536.814709084
>>> get_consumed_duration__process_wide() #doctest: +SKIP
0.540129381
>>> get_consumed_duration__thread_wide() #doctest: +SKIP
0.540573765

>>> get_consumed_duration__system_wide__monotonic() #doctest: +SKIP
13735536.8161167
>>> get_consumed_duration__system_wide__highest_resolution() #doctest: +SKIP
13735536.816553624
>>> get_consumed_duration__process_wide() #doctest: +SKIP
0.541914996
>>> get_consumed_duration__thread_wide() #doctest: +SKIP
0.542356227




>>> from time import sleep


########
########>>> with timer__thread_wide() as r:
########...     sleep(1)
########>>> r.get_duration_without_unit() #doctest: +SKIP
########0.0003442300000000009
########>>> r.get_duration_without_unit() < 0.7
########True
########
########>>> timer = timer__system_wide__highest_resolution
########>>> with timer() as r:
########...     sleep(2)
########>>> 2.0 <= r.get_duration_without_unit() < 4.0
########True
########
########>>> with timer() as r:
########...     sleep(4)
########>>> r.get_duration_without_unit() > 4.0
########True
########
########>>> with timer() as r:
########...     sleep(2)
########>>> 2.0 <= r.get_duration_without_unit() < 4.0
########True
########

>>> timer = timer__system_wide__highest_resolution
>>> with timer() as r:
...     sleep(0.2)
>>> 0.2 <= r.get_duration_without_unit() < 0.4
True
>>> r.get_duration_without_unit() #doctest: +SKIP
0.20153722912073135
>>> r.get_unit()
datetime.timedelta(seconds=1)
>>> r.get() #doctest: +SKIP
(0.20153722912073135, datetime.timedelta(seconds=1))
>>> r.get() == (r.get_duration_without_unit(), timedelta(seconds=1))
True
>>> r.get() == (r.get_duration_without_unit(), r.get_unit())
True

>>> with timer(print) as r: #doctest: +SKIP
...     sleep(0.2)
0.2015569992363453 0:00:01
>>> print(timer.get_unit())
0:00:01
>>> timer.get_unit()
datetime.timedelta(seconds=1)
>>> timer.get_time_() #doctest: +SKIP
13773734.696721207
>>> timer.get_time_ is get_consumed_duration__system_wide__highest_resolution
True
>>> with timer(lambda duration, unit,/:print(f'{duration:.2} *({unit!s})')) as r:
...     sleep(0.2)
0.2 *(0:00:01)




######################
#datetime:
######################
>>> from datetime import timedelta
>>> timedelta(seconds=0.005)
datetime.timedelta(microseconds=5000)
>>> from datetime import datetime
>>> datetime.utcfromtimestamp(0.0) #naive!!! why???
datetime.datetime(1970, 1, 1, 0, 0)
>>> datetime.fromtimestamp(0.0)
datetime.datetime(1970, 1, 1, 8, 0)
>>> datetime.fromtimestamp(0.0) -datetime.utcfromtimestamp(0.0)
datetime.timedelta(seconds=28800)
>>> datetime.utcnow() #doctest: +SKIP
datetime.datetime(2023, 8, 23, 0, 3, 8, 790431)
>>> datetime.today() #doctest: +SKIP
datetime.datetime(2023, 8, 23, 8, 3, 8, 790783)
>>> from time import time_ns
>>> ns4now = time_ns()
>>> ns4now #doctest: +SKIP
1692748988791250312
>>> datetime.fromtimestamp(ns4now/10**9) #doctest: +SKIP
datetime.datetime(2023, 8, 23, 8, 3, 8, 791250)


    aware_datetime5timestamp_
    aware_datetime2timestamp_
>>> timestamp.hex()
'0x1.93939985bce89p+30'
>>> datetime__tz4local = aware_datetime5timestamp_(tz4local, timestamp)
>>> datetime__tz4utc = aware_datetime5timestamp_(tz4utc, timestamp)
>>> datetime__tz4utc == datetime__tz4local
True
>>> datetime__tz4utc.date == datetime__tz4local.date
False
>>> datetime__tz4local
datetime.datetime(2023, 8, 23, 0, 46, 25, 434481, tzinfo=datetime.timezone(datetime.timedelta(seconds=28800), 'seed.for_libs.for_time.tz4local'))
>>> aware_datetime5timestamp_(False, timestamp)
datetime.datetime(2023, 8, 23, 0, 46, 25, 434481, tzinfo=datetime.timezone(datetime.timedelta(seconds=28800), 'seed.for_libs.for_time.tz4local'))
>>> datetime__tz4utc
datetime.datetime(2023, 8, 22, 16, 46, 25, 434481, tzinfo=datetime.timezone.utc)
>>> aware_datetime5timestamp_(True, timestamp)
datetime.datetime(2023, 8, 22, 16, 46, 25, 434481, tzinfo=datetime.timezone.utc)


>>> f = lambda aware_datetime,/:(aware_datetime - datetime(1970, 1, 1, tzinfo=timezone.utc)).total_seconds()
>>> f(datetime__tz4local)
1692722785.434481
>>> f(datetime__tz4utc)
1692722785.434481
>>> datetime__tz4local.timestamp()
1692722785.434481
>>> datetime__tz4utc.timestamp()
1692722785.434481
>>> aware_datetime2timestamp_(datetime__tz4local)
1692722785.434481
>>> aware_datetime2timestamp_(datetime__tz4utc)
1692722785.434481
>>> datetime__tz4local.timestamp() == datetime__tz4utc.timestamp() == aware_datetime2timestamp_(datetime__tz4local) == aware_datetime2timestamp_(datetime__tz4utc)
True

>>> aware_datetime2timestamp_(datetime__tz4local).hex()
'0x1.93939985bce89p+30'
>>> aware_datetime2timestamp_(datetime__tz4utc).hex()
'0x1.93939985bce89p+30'
>>> datetime__tz4local.timestamp().hex()
'0x1.93939985bce89p+30'
>>> datetime__tz4utc.timestamp().hex()
'0x1.93939985bce89p+30'



    datetime2formatted_str_
    datetime5formatted_str_
>>> time_fmt = time_fmt5py_str_fmt_('{YYYY}{MM}{DD}-{hh}:{mm}:{ss}.{ffffff}{xhhmm_ss_ffffff}')
>>> time_fmt
'%Y%m%d-%H:%M:%S.%f%z'
>>> datetime2formatted_str_(time_fmt, datetime__tz4utc)
'20230822-16:46:25.434481+0000'
>>> datetime5formatted_str_(time_fmt, _) # --> aware_datetime
datetime.datetime(2023, 8, 22, 16, 46, 25, 434481, tzinfo=datetime.timezone.utc)
>>> datetime2formatted_str_(time_fmt, datetime__tz4utc.replace(tzinfo=None), mismatch_tzinfo_ok=True)
'20230822-16:46:25.434481'
>>> datetime5formatted_str_(time_fmt, _) #??? why strptime mismatch strftime??? %z can output empty???  # --> e ../lots/NOTE/Python/python-bug/datetime-bug.txt
Traceback (most recent call last):
    ...
ValueError: time data '20230822-16:46:25.434481' does not match format '%Y%m%d-%H:%M:%S.%f%z'
>>> datetime5formatted_str_(time_fmt[:-2], _) # --> naive_datetime
datetime.datetime(2023, 8, 22, 16, 46, 25, 434481)

>>> datetime2formatted_str_(time_fmt, datetime__tz4local)
'20230823-00:46:25.434481+0800'
>>> datetime5formatted_str_(time_fmt, _) # --> aware_datetime
datetime.datetime(2023, 8, 23, 0, 46, 25, 434481, tzinfo=datetime.timezone(datetime.timedelta(seconds=28800)))



    aware_datetime5formatted_str_
    aware_datetime2formatted_str_
>>> time_fmt
'%Y%m%d-%H:%M:%S.%f%z'
>>> aware_datetime2formatted_str_(time_fmt, datetime__tz4utc)
'20230822-16:46:25.434481+0000'
>>> aware_datetime5formatted_str_(time_fmt, _) # --> aware_datetime
datetime.datetime(2023, 8, 22, 16, 46, 25, 434481, tzinfo=datetime.timezone.utc)
>>> aware_datetime2formatted_str_(time_fmt, datetime__tz4utc.replace(tzinfo=None))
Traceback (most recent call last):
    ...
TypeError: not aware: datetime.datetime(2023, 8, 22, 16, 46, 25, 434481)
>>> aware_datetime5formatted_str_(time_fmt, '20230822-16:46:25.434481')
Traceback (most recent call last):
    ...
ValueError: time data '20230822-16:46:25.434481' does not match format '%Y%m%d-%H:%M:%S.%f%z'
>>> aware_datetime5formatted_str_(time_fmt[:-2], '20230822-16:46:25.434481')
Traceback (most recent call last):
    ...
seed.for_libs.for_time.Error__miss_tzinfo__strptime_mismatch_strftime

>>> aware_datetime2formatted_str_(time_fmt, datetime__tz4local)
'20230823-00:46:25.434481+0800'
>>> aware_datetime5formatted_str_(time_fmt, _) # --> aware_datetime
datetime.datetime(2023, 8, 23, 0, 46, 25, 434481, tzinfo=datetime.timezone(datetime.timedelta(seconds=28800)))


    timestamp2formatted_str__via_datetime__
    timestamp5formatted_str__via_datetime__



>>> default_time_fmt
'%a %b %d %H:%M:%S %Y'
>>> time_fmt
'%Y%m%d-%H:%M:%S.%f%z'
>>> timestamp.hex()
'0x1.93939985bce89p+30'
>>> tz4utc
datetime.timezone.utc
>>> tz4local
datetime.timezone(datetime.timedelta(seconds=28800), 'seed.for_libs.for_time.tz4local')
>>> time_struct8platform_epoch___tz4utc
time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
>>> time_struct8platform_epoch___tz4local
time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=8, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
>>> aware_datetime8platform_epoch
datetime.datetime(1970, 1, 1, 0, 0, tzinfo=datetime.timezone.utc)

def timestamp2formatted_str__via_datetime__(may_time_fmt, local_vs_utc__or__tz, timestamp, /, *, mismatch_tzinfo_ok=False):
>>> timestamp2formatted_str__via_datetime__(None, False, timestamp)
'Wed Aug 23 00:46:25 2023'
>>> formatted_str___default_time_fmt___tz4local = _
>>> timestamp2formatted_str__via_datetime__(None, True, timestamp)
Traceback (most recent call last):
    ...
seed.for_libs.for_time.Error__miss_tzinfo__strptime_mismatch_strftime
>>> timestamp2formatted_str__via_datetime__(None, True, timestamp, mismatch_tzinfo_ok=True)
'Tue Aug 22 16:46:25 2023'
>>> formatted_str___default_time_fmt___tz4utc = _

>>> timestamp2formatted_str__via_datetime__(time_fmt, False, timestamp)
'20230823-00:46:25.434481+0800'
>>> formatted_str___nondefault_time_fmt___tz4local = _
>>> timestamp2formatted_str__via_datetime__(time_fmt, True, timestamp)
'20230822-16:46:25.434481+0000'
>>> formatted_str___nondefault_time_fmt___tz4utc = _

def timestamp5formatted_str__via_datetime__(may_time_fmt, local_vs_utc__or__tz, formatted_str, /, ):
>>> timestamp5formatted_str__via_datetime__(None, False, formatted_str___default_time_fmt___tz4local)
1692722785.0
>>> timestamp5formatted_str__via_datetime__(None, True, formatted_str___default_time_fmt___tz4local)
1692751585.0
>>> timestamp5formatted_str__via_datetime__(None, False, formatted_str___default_time_fmt___tz4utc)
1692693985.0
>>> timestamp5formatted_str__via_datetime__(None, True, formatted_str___default_time_fmt___tz4utc)
1692722785.0

#above local_vs_utc__or__tz takes effect
#   since [not '%z' in default_time_fmt]
#below local_vs_utc__or__tz takes no effect
#   since ['%z' in time_fmt]
>>> timestamp5formatted_str__via_datetime__(time_fmt, False, formatted_str___nondefault_time_fmt___tz4local)
1692722785.434481
>>> timestamp5formatted_str__via_datetime__(time_fmt, True, formatted_str___nondefault_time_fmt___tz4local)
1692722785.434481
>>> timestamp5formatted_str__via_datetime__(time_fmt, False, formatted_str___nondefault_time_fmt___tz4utc)
1692722785.434481
>>> timestamp5formatted_str__via_datetime__(time_fmt, True, formatted_str___nondefault_time_fmt___tz4utc)
1692722785.434481





get_now__timestamp
get_now__time_struct_
get_now__aware_datetime_

>>> get_now__timestamp() #doctest: +SKIP
1692850531.802958
>>> get_now__time_struct_(False) #doctest: +SKIP
time.struct_time(tm_year=2023, tm_mon=8, tm_mday=24, tm_hour=12, tm_min=15, tm_sec=31, tm_wday=3, tm_yday=236, tm_isdst=0)
>>> get_now__time_struct_(True) #doctest: +SKIP
time.struct_time(tm_year=2023, tm_mon=8, tm_mday=24, tm_hour=4, tm_min=15, tm_sec=31, tm_wday=3, tm_yday=236, tm_isdst=0)
>>> get_now__aware_datetime_() #doctest: +SKIP
datetime.datetime(2023, 8, 24, 12, 15, 31, 806859, tzinfo=datetime.timezone(datetime.timedelta(seconds=28800), 'seed.for_libs.for_time.tz4local'))
>>> get_now__aware_datetime_(False) #doctest: +SKIP
datetime.datetime(2023, 8, 24, 12, 15, 31, 807456, tzinfo=datetime.timezone(datetime.timedelta(seconds=28800), 'seed.for_libs.for_time.tz4local'))
>>> get_now__aware_datetime_(True) #doctest: +SKIP
datetime.datetime(2023, 8, 24, 4, 15, 31, 807931, tzinfo=datetime.timezone.utc)
>>> get_now__aware_datetime_(tz4local) #doctest: +SKIP
datetime.datetime(2023, 8, 24, 12, 15, 31, 808421, tzinfo=datetime.timezone(datetime.timedelta(seconds=28800), 'seed.for_libs.for_time.tz4local'))
>>> get_now__aware_datetime_(tz4utc) #doctest: +SKIP
datetime.datetime(2023, 8, 24, 4, 15, 31, 808944, tzinfo=datetime.timezone.utc)

#]]]'''
__all__ = r'''
PeriodicToilLeisureTime
    default_mkr4seconds4leisure



time_struct8platform_epoch___tz4utc
time_struct8platform_epoch___tz4local

time_struct5timestamp_
time_struct2timestamp_

TimeFormatDirective
    time_fmt5py_str_fmt_
    time_fmt5snippets_
default_time_fmt
    time_fmt5may_

time_struct2formatted_str_
time_struct5formatted_str_

timestamp2formatted_str__via_time_struct__
timestamp5formatted_str__via_time_struct__

get_now__timestamp
get_now__time_struct_

get_consumed_duration__system_wide__monotonic
get_consumed_duration__system_wide__highest_resolution
get_consumed_duration__process_wide
get_consumed_duration__thread_wide

Timer
    timer__thread_wide
    timer__process_wide
    timer__system_wide__highest_resolution
    timer__system_wide__monotonic
    Timer__print_err
        timer__print_err__thread_wide
        timer__print_err__process_wide
        timer__print_err__system_wide__highest_resolution
        timer__print_err__system_wide__monotonic


aware_datetime8platform_epoch
tz4utc
tz4local
    utcoffset4local
        total_seconds4utcoffset4local

tz5or__local_vs_utc_
    check_tzinfo





Error
    Error__miss_tzinfo__strptime_mismatch_strftime
    Error__mismatch_tzinfo

is_datetime_aware
is_datetime_naive
check_aware_datetime
get_now__aware_datetime_
Case4datetime_isoformat_timespec
is_the_time_zone_offset_directive_in_time_fmt


aware_datetime5timestamp_
aware_datetime2timestamp_

datetime2formatted_str_
datetime5formatted_str_

aware_datetime5formatted_str_
aware_datetime2formatted_str_

timestamp2formatted_str__via_datetime__
timestamp5formatted_str__via_datetime__


'''.split()#'''
    #timegm__float
    #Result4Timer
__all__

___begin_mark_of_excluded_global_names__0___ = ...

#import time
from time import sleep

from time import strftime, strptime
from time import struct_time
from time import gmtime
from calendar import timegm as timegm__int
from time import mktime, localtime
from time import time as _time
from time import monotonic, perf_counter, process_time, thread_time
from enum import Enum, auto


from seed.tiny import check_callable
from seed.tiny import check_type_is
from seed.tiny import ifNone
from seed.helper.with4cleanup import with4cleanup__on_exit
from seed.tiny import print_err

from datetime import timedelta
___end_mark_of_excluded_global_names__0___ = ...

time_struct8platform_epoch___tz4utc = gmtime(0.0)
time_struct8platform_epoch___tz4local = localtime(0.0)


def time_struct5timestamp_(local_vs_utc, timestamp, /):
    r'''[[[
    local_vs_utc/bool -> timestamp<platform_epoch>/float -> time_struct<local_vs_utc>/struct_time

    #loss accuracy: [resolution==1second] i.e. be int when converted back, see:timegm__int #use datetime instead'

    vs:
        time_struct5timestamp_.resolution==1second
        aware_datetime5timestamp_.resolution==1microsecond
    #]]]'''#'''
    check_type_is(bool, local_vs_utc)
    check_type_is(float, timestamp)
    if local_vs_utc is False:
        f = localtime
    else:
        f = gmtime
    time_struct = f(timestamp)
    return time_struct

def timegm__float(utc_time_struct, /):
    'utc_time_struct/struct_time<UTC> -> timestamp<platform_epoch>/float'
    check_type_is(struct_time, utc_time_struct)
    i = timegm__int(utc_time_struct)
    check_type_is(int, i)
    timestamp = float(i)
    return timestamp
def time_struct2timestamp_(local_vs_utc, time_struct, /):
    'local_vs_utc/bool -> time_struct<local_vs_utc>/struct_time -> timestamp<platform_epoch>/float'
    check_type_is(bool, local_vs_utc)
    check_type_is(struct_time, time_struct)
    if local_vs_utc is False:
        f = mktime
    else:
        f = timegm__float
    timestamp = f(time_struct)
    return timestamp




class TimeFormatDirective(Enum):
    'to mk time_fmt or convert from normal py_str_fmt;  now include directive from py.datetime module'
    ######################
    #py.time:
    ######################

    ######################
    #descriptive name:
    ######################
    escape_char = '%%'
    year_4digit = '%Y'
    year_2digit = '%y'
    month_2digit = '%m'
    day6month__2digit = '%d'
    day6year__3digit = '%j'
    hour_24__2digit = '%H'
    hour_12__2digit = '%I'
    AM_or_PM__locale = '%p'
    minute_2digit = '%M'
    second_2digit = '%S'

    #rename:time_zone_offset__5char = '%z'
    time_zone_offset4time_struct__5char = '%z'
    time_zone_name__smay = '%Z'

    weekday06_1digit = '%w'
    week_number4day6year__5Sunday__2digit = '%U'
    week_number4day6year__5Monday__2digit = '%W'
    weekday_name__abbreviated___locale = '%a'
    weekday_name__full___locale = '%A'
    month_name__abbreviated___locale = '%b'
    month_name__full___locale = '%B'

    datetime__locale = '%c'
    date6datetime__locale = '%x'
    time6datetime__locale = '%X'
    ######################



    ######################
    #alias:
    ######################
    o_o = escape_char
    YYYY = year_4digit
    YY = year_2digit
    MM = month_2digit
    DD6month = day6month__2digit
    DDD6year = day6year__3digit
    DD = DD6month

    hh24 = hour_24__2digit
    hh12 = hour_12__2digit
    hh = hh24
    mm = minute_2digit
    ss = second_2digit

    xhhmm = time_zone_offset4time_struct__5char
    tz_name = time_zone_name__smay

    W = weekday06_1digit
    iweek6year5Sunday = week_number4day6year__5Sunday__2digit
    iweek6year5Monday = week_number4day6year__5Monday__2digit
    W_abbr = weekday_name__abbreviated___locale
    W_full = weekday_name__full___locale
    M_abbr = month_name__abbreviated___locale
    M_full = month_name__full___locale
    YYYYMMDDhhmmss = datetime__locale
    YYYYMMDD = date6datetime__locale
    hhmmss = time6datetime__locale
    ######################



    ######################
    #py.datetime:
    ######################
    #datetime____strftime__and__strptime__Behavior:goto
    #update: %z
    #new: %f
    #new-extra: %G %u %V
    ######################

    ######################
    #descriptive name:
    ######################
    microsecond_6digit = '%f'
    #update:time_zone_offset4time_struct__5char = '%z'
    time_zone_offset__5char__7char__14char = '%z'
        #UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive).
        #(empty), +0000, -0400, +1030, +063415, -030712.345216
    ######################
    #extra:
    ISO8601_year__4digit = '%G'
    ISO8601_weekday17__1digit = '%u'
    ISO8601_week_number4day6year__5Monday6week_containing_Jan_4__2digit = '%V'
    ######################

    ######################
    #alias:
    ######################
    ffffff = microsecond_6digit
    xhhmm_ss_ffffff = time_zone_offset__5char__7char__14char
    ######################
    #extra:
    ISO_YYYY = ISO8601_year__4digit
    ISO_W = ISO8601_weekday17__1digit
    ISO_iweek6year = ISO8601_week_number4day6year__5Monday6week_containing_Jan_4__2digit
    ######################











def time_fmt5py_str_fmt_(py_str_fmt, /):
    'normal-py-fmt/str -> time_fmt/str'
    #bug:time_fmt = py_str_fmt.format(**TimeFormatDirective.__members__)
    C = TimeFormatDirective
    e = C.escape_char.value
    escaped_py_str_fmt = py_str_fmt.replace('%', e)
    time_fmt = escaped_py_str_fmt.format(**_nm2directive)
    return time_fmt

_nm2directive = {nm:case.value for nm, case in TimeFormatDirective.__members__.items()}

def time_fmt5snippets_(*str_or_TimeFormatDirective__seq):
    'snippet/(str|TimeFormatDirective)... -> time_fmt/str'
    def _iter(snippets, /):
        C = TimeFormatDirective
        e = C.escape_char.value
        for snippet in snippets:
            T = type(snippet)
            if T is str:
                raw_str = snippet
                escaped_str = raw_str.replace('%', e)
                yield escaped_str
            elif T is C:
                case = snippet
                directive = case.value
                assert type(directive) is str
                #assert len(directive) == 2
                #assert directive[0] == '%'
                yield directive
            else:
                raise TypeError(f'not str or TimeFormatDirective: {T!r}')

    it = _iter(str_or_TimeFormatDirective__seq)
    time_fmt = ''.join(it)
    return time_fmt



default_time_fmt = "%a %b %d %H:%M:%S %Y"
__ = TimeFormatDirective
assert default_time_fmt == time_fmt5snippets_(__.W_abbr, ' ', __.M_abbr, ' ', __.DD, ' ', __.hh, ':', __.mm, ':', __.ss, ' ', __.YYYY)
assert default_time_fmt == time_fmt5py_str_fmt_('{W_abbr} {M_abbr} {DD} {hh}:{mm}:{ss} {YYYY}')



def time_fmt5may_(may_time_fmt, /):
    'may time_fmt/str -> time_fmt/str #see:default_time_fmt'
    time_fmt = ifNone(may_time_fmt, default_time_fmt)
    check_type_is(str, time_fmt)
    return time_fmt

def time_struct2formatted_str_(may_time_fmt, time_struct, /):
    'may time_fmt/str -> time_struct<local_vs_utc>/struct_time -> formatted_str<local_vs_utc>/str'
    time_fmt = time_fmt5may_(may_time_fmt)
    check_type_is(struct_time, time_struct)
    formatted_str = strftime(time_fmt, time_struct)
    return formatted_str
def time_struct5formatted_str_(may_time_fmt, formatted_str, /):
    'may time_fmt/str -> formatted_str<local_vs_utc>/str -> time_struct<local_vs_utc>/struct_time'
    time_fmt = time_fmt5may_(may_time_fmt)
    check_type_is(str, formatted_str)
    #bug:time_struct = strptime(time_fmt, formatted_str)
    time_struct = strptime(formatted_str, time_fmt)
    return time_struct






def timestamp2formatted_str__via_time_struct__(may_time_fmt, local_vs_utc, timestamp, /):
    'may time_fmt/str -> local_vs_utc/bool -> timestamp<platform_epoch>/float -> formatted_str<local_vs_utc>/str  #loss accuracy: [resolution==1 second] i.e. be int when converted back, see:timegm__int #use datetime instead'
    time_struct = time_struct5timestamp_(local_vs_utc, timestamp)
    formatted_str = time_struct2formatted_str_(may_time_fmt, time_struct)
    return formatted_str
def timestamp5formatted_str__via_time_struct__(may_time_fmt, local_vs_utc, formatted_str, /):
    'may time_fmt/str -> local_vs_utc/bool -> formatted_str<local_vs_utc>/str -> timestamp<platform_epoch>/float'
    time_struct = time_struct5formatted_str_(may_time_fmt, formatted_str)
    timestamp = time_struct2timestamp_(local_vs_utc, time_struct)
    return timestamp

def get_now__timestamp():
    '-> timestamp<platform_epoch>/float'
    timestamp = _time()
    return timestamp
def get_now__time_struct_(local_vs_utc, /):
    'local_vs_utc/bool -> now/time_struct<local_vs_utc>/struct_time'
    timestamp__now = get_now__timestamp()
    time_struct__now = time_struct5timestamp_(local_vs_utc, timestamp__now)
    return time_struct__now

monotonic, perf_counter, process_time, thread_time
def get_consumed_duration__system_wide__monotonic():
    '-> consumed_duration<system_wide&monotonic>/float'
    duration__WS_mono = monotonic()
    return duration__WS_mono
def get_consumed_duration__system_wide__highest_resolution():
    '-> consumed_duration<system_wide&highest_resolution>/float'
    duration__WS_fine = perf_counter()
    return duration__WS_fine
def get_consumed_duration__process_wide():
    '-> consumed_duration<process_wide>/float'
    duration__WP = process_time()
    return duration__WP
def get_consumed_duration__thread_wide():
    '-> consumed_duration<thread_wide>/float'
    duration__WT = thread_time()
    return duration__WT









######################
# with timer:
######################


class Result4Timer:
    'future result'
    def __init__(sf, t0, t1=None, /, *, unit):
        sf._t0 = t0
        sf._t1 = t1
        sf._u = unit
    def _set_t1(sf, t1, /):
        sf._dt = t1 -sf._t0
        sf._t1 = t1
    def get_unit(sf, /):
        return sf._u
    def get(sf, /):
        return (sf._dt, sf._u)
    def get_duration_without_unit(sf, /):
        return sf._dt

#def with4cleanup__on_exit(may_cleanup_on_exit, /, *prepare5____tmay_Nothing___or___args4mk_default_or_raise, mirror=False):
#def cleanup_on_exit(internal_state, external_obj, /):
def _cleanup_on_exit(sf, r, /):
    t1 = sf._g()
    r._set_t1(t1)
def _mk_cleanup_on_exit(callback_on_exit_, /):
    check_callable(callback_on_exit_)
    def cleanup_on_exit(sf, r, /):

        _cleanup_on_exit(sf, r)
        duration, unit = r.get()
        callback_on_exit_(duration, unit)
    return cleanup_on_exit

def _setup_on_enter():
    pass
def _mk_lazy_with_setup(x, setup_on_enter_, /):
    def lazy_with_setup_():
        setup_on_enter_()
        return x
    return lazy_with_setup_
class Timer:
    def __init__(sf, get_time_, /, *, unit, default_cleanup_on_exit=_cleanup_on_exit, default_setup_on_enter=_setup_on_enter):
        sf._g = get_time_
        sf._u = unit
        sf._cln = default_cleanup_on_exit
        sf._stp = default_setup_on_enter
    @property
    def default_cleanup_on_exit(sf, /):
        return sf._cln
        return _cleanup_on_exit
    @property
    def default_setup_on_enter(sf, /):
        return sf._stp
    def get_unit(sf, /):
        return sf._u
    @property
    def get_time_(sf, /):
        return sf._g
    #def __enter__(sf, /):
    def __call__(sf, may_callback_on_exit_=None, may_setup_on_enter_=None, /):
        'sf/Timer -> may callback_on_exit_/(duration_without_unit -> unit -> None) -> withable_obj<Result4Timer>'
        t0 = sf._g()
        unit = sf.get_unit()
        r = Result4Timer(t0, unit=unit)
        if may_callback_on_exit_ is None:
            cleanup_on_exit = sf.default_cleanup_on_exit
        else:
            callback_on_exit_ = may_callback_on_exit_
            cleanup_on_exit = _mk_cleanup_on_exit(callback_on_exit_)
        cleanup_on_exit


        if may_setup_on_enter_ is None:
            setup_on_enter_ = sf.default_setup_on_enter
        else:
            setup_on_enter_ = may_setup_on_enter_
        setup_on_enter_
        lazy_with_setup_ = _mk_lazy_with_setup((sf, r), setup_on_enter_)


        return with4cleanup__on_exit(cleanup_on_exit, 0, lazy_with_setup_)
        return with4cleanup__on_exit(cleanup_on_exit, -1, (sf, r))

_unit = _1second = timedelta(seconds=1)
    #unit, not resolution
timer__thread_wide = Timer(get_consumed_duration__thread_wide, unit=_unit)
timer__process_wide = Timer(get_consumed_duration__process_wide, unit=_unit)
timer__system_wide__highest_resolution = Timer(get_consumed_duration__system_wide__highest_resolution, unit=_unit)
timer__system_wide__monotonic = Timer(get_consumed_duration__system_wide__monotonic, unit=_unit)

class Timer__print_err(Timer):
    r'''[[[
usage/example:

view ../../python3_src/seed/math/sqrts_mod_.py

from seed.for_libs.for_time import (
Timer__print_err
    ,timer__print_err__thread_wide
    ,timer__print_err__process_wide
    ,timer__print_err__system_wide__highest_resolution
    ,timer__print_err__system_wide__monotonic
)

timer = timer__print_err__thread_wide
_to_show_ = __name__ == "__main__"

with timer(prefix='basic...', _to_show_=True, _show_hint_on_enter_=True):
    do...

with timer(prefix='basic...', _to_show_=_to_show_):
    from math import isqrt as floor_sqrt_
with timer(prefix='prime_gens', _to_show_=_to_show_):
    from seed.math.prime_gens import prime_gen


py -m seed.math.sqrts_mod_
basic...:duration: 0.006129770000000007 *(unit: 0:00:01)
prime_gens:duration: 0.212392231 *(unit: 0:00:01)
inv_mod_:duration: 0.015584998999999988 *(unit: 0:00:01)
radix_repr2uint:duration: 0.10070369400000001 *(unit: 0:00:01)
uint2radix_repr:duration: 0.007977075 *(unit: 0:00:01)

    #]]]'''#'''
    #_cleanup_on_exit = _mk_cleanup_on_exit(print_err)
    if 0:
        def __init__(sf, get_time_, /, *, unit, default_cleanup_on_exit=_cleanup_on_exit):
            super().__init__(get_time_, unit=unit, default_cleanup_on_exit=default_cleanup_on_exit)
    def __init__(sf, get_time_, /, *, unit, default_print=print_err):
        sf._pr = default_print
        #super().__init__(get_time_, unit=unit, default_cleanup_on_exit=__class__._cleanup_on_exit)
        super().__init__(get_time_, unit=unit)
    if 0:
        @property
        def default_cleanup_on_exit(sf, /):
            return __class__._cleanup_on_exit
    def __call__(sf, /, *args, _to_show_=True, _fmt_='{prefix}:duration: {duration} *(unit: {unit})', prefix='...', _show_hint_on_enter_=False, _low_duration_threshold4show_=0, **kwds):
        'sf/Timer__print_err -> (*args) -> **{_to_show_,_fmt_,_show_hint_on_enter_,prefix,**kwds} -> withable_obj<Result4Timer>'
        if not _to_show_:
            may_callback_on_exit_ = None
        else:
            def callback_on_exit_(duration_without_unit, unit, /):
                #if not _to_show_: return
                if duration_without_unit < _low_duration_threshold4show_:
                    return
                s = _fmt_.format(*args, prefix=prefix, duration=duration_without_unit, unit=unit, **kwds)
                print_err = sf._pr
                #if not _to_show_: return
                print_err(s, flush=True)
            may_callback_on_exit_ = callback_on_exit_
        may_callback_on_exit_

        if not (_to_show_ and _show_hint_on_enter_):
            may_setup_on_enter_ = None
        else:
            def setup_on_enter_():
                s = f'{prefix}: ... ...'
                print_err = sf._pr
                print_err(s, flush=True)
            may_setup_on_enter_ = setup_on_enter_
        may_setup_on_enter_
        may_callback_on_exit_
        return super().__call__(may_callback_on_exit_, may_setup_on_enter_)
timer__print_err__thread_wide = Timer__print_err(get_consumed_duration__thread_wide, unit=_unit)
timer__print_err__process_wide = Timer__print_err(get_consumed_duration__process_wide, unit=_unit)
timer__print_err__system_wide__highest_resolution = Timer__print_err(get_consumed_duration__system_wide__highest_resolution, unit=_unit)
timer__print_err__system_wide__monotonic = Timer__print_err(get_consumed_duration__system_wide__monotonic, unit=_unit)

######################
# datetime ...
######################
___begin_mark_of_excluded_global_names__1___ = ...
from datetime import timedelta
from datetime import datetime
from datetime import timezone
from datetime import tzinfo
import re
___end_mark_of_excluded_global_names__1___ = ...

#>>> datetime.fromtimestamp(0)
#datetime.datetime(1970, 1, 1, 8, 0)

#>>> datetime.fromtimestamp(0, timezone(timedelta(days=0.5)))
#datetime.datetime(1970, 1, 1, 12, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=43200)))



assert None is datetime.fromtimestamp(0.0).tzinfo
assert None is datetime.utcfromtimestamp(0.0).tzinfo
  #bug?
  #view ../lots/NOTE/Python/python-bug/datetime-bug.txt
#print(repr(datetime.fromtimestamp(0.0))) #set tzinfo?
    #datetime.datetime(1970, 1, 1, 8, 0)
#print(repr(datetime.utcfromtimestamp(0.0))) #set tzinfo?
    #datetime.datetime(1970, 1, 1, 0, 0)
#print(datetime.fromtimestamp(0.0))
    #1970-01-01 08:00:00
#print(datetime.utcfromtimestamp(0.0))
    #1970-01-01 00:00:00

assert timezone.utc == timezone(timedelta(0))

class Error(Exception):pass
class Error__miss_tzinfo__strptime_mismatch_strftime(Error):pass
class Error__mismatch_tzinfo(Error):pass



r'''[[[
##try:
##    utcoffset4local___abs_may_ge_1day = (datetime.fromtimestamp(0.0) -datetime.utcfromtimestamp(0.0))
##except TypeError:
##    utcoffset4local___abs_may_ge_1day = (datetime.fromtimestamp(0.0) -datetime.utcfromtimestamp(0.0).replace(tzinfo=None))
##utcoffset4local___abs_may_ge_1day
##    #may have [abs(utcoffset4local) >= 1day] which is not allowed
##total_seconds4utcoffset4local___abs_may_ge_1day = utcoffset4local___abs_may_ge_1day.total_seconds()
##
##def _mk_may_tz4local():
##    try:
##        tz4local = timezone(utcoffset4local___abs_may_ge_1day)
##            # timezone require: [abs(utcoffset4local) < 1day]
##    except ValueError:
##        may_tz4local = None
##    else:
##        may_tz4local = tz4local
##    return may_tz4local
##may_tz4local = _mk_may_tz4local()
##tz4utc = timezone.utc
###print(tz4local)
##    #UTC+08:00
##
##
##class Error__platform_epoch_is_too_far_from_utc0(Error):pass
##
##
##
##
###def time_struct5timestamp_(local_vs_utc, timestamp, /):
###    'local_vs_utc/bool -> timestamp<platform_epoch>/float -> time_struct<local_vs_utc>/struct_time  #loss accuracy: [resolution==1 second] i.e. be int when converted back, see:timegm__int #use datetime instead'
###datetime.fromtimestamp(timestamp, tz=None) -> naive datetime object if tz is None
##
##def tz5or__local_vs_utc_(local_vs_utc__or__tz, /):
##    if type(local_vs_utc__or__tz) is bool:
##        local_vs_utc = local_vs_utc__or__tz
##        #tz = tz4local if local_vs_utc is False else tz4utc
##        if local_vs_utc is False:
##            if may_tz4local is None:
##                raise Error__platform_epoch_is_too_far_from_utc0
##            tz4local = may_tz4local
##            tz = tz4local
##        else:
##            tz = tz4utc
##    else:
##        tz = local_vs_utc__or__tz
##    tz
##
##    check_tzinfo(tz)
##    return tz
##def check_tzinfo(tz, /):
##    if not isinstance(tz, tzinfo):raise TypeError(tz)
##def aware_datetime5timestamp_(tzXXX__or__Ellipsis, local_vs_utc__or__tzYYY, timestamp__tzYYY, /):
##    r' ''[[[
##    :: (tzXXX/tzinfo | Ellipsis) -> (local_vs_utc/bool | tzYYY/tzinfo) -> timestamp<platform_epoch|tz4utc|tzYYY>/float -> aware_datetime<tzXXX|(tz4local|tz4utc|tzYYY)>/datetime
##
##    #loss accuracy: [resolution==1microsecond]
##
##    vs:
##        time_struct5timestamp_.resolution==1second
##        aware_datetime5timestamp_.resolution==1microsecond
##
##    #]]]' ''#'' '
##    utcoffset4local___abs_may_ge_1day
##    try:
##        tzYYY = tz5or__local_vs_utc_(local_vs_utc__or__tzYYY)
##    except Error__platform_epoch_is_too_far_from_utc0:
##        if tzXXX__or__Ellipsis is ...:
##            raise
##        care_local = True
##    else:
##        care_local = False
##    if care_local:
##        timestamp__tz4local = timestamp__tzYYY
##        timestamp__tz4utc = timestamp__tz4local + total_seconds4utcoffset4local___abs_may_ge_1day
##        ######################
##        tzZZZ = tz4utc
##        timestamp__tzZZZ = timestamp__tz4utc
##        ######################
##    else:
##        ######################
##        tzZZZ = tzYYY
##        timestamp__tzZZZ = timestamp__tzYYY
##        ######################
##    aware_datetime__tzZZZ = datetime.fromtimestamp(timestamp__tzZZZ, tzZZZ)
##    if tzXXX__or__Ellipsis is ...:
##        if care_local:
##            raise logic-err
##            pass
##        else:
##            tzXXX = tzYYY
##    else:
##            tzXXX = tzXXX__or__Ellipsis
##            check_tzinfo(tzXXX)
##            care_local = False
##    if care_local:
##            raise logic-err
##    tzXXX
##    aware_datetime__tzXXX = aware_datetime__tzZZZ.astimezone(tzXXX)
##
##    return aware_datetime
#]]]'''#'''
try:
    utcoffset4local = (datetime.fromtimestamp(0.0) -datetime.utcfromtimestamp(0.0))
except TypeError:
    utcoffset4local = (datetime.fromtimestamp(0.0) -datetime.utcfromtimestamp(0.0).replace(tzinfo=None))
utcoffset4local
assert abs(utcoffset4local) < timedelta(days=1)
total_seconds4utcoffset4local = utcoffset4local.total_seconds()
tz4local = timezone(utcoffset4local, f'{__name__}.tz4local')

tz4utc = timezone.utc
#print(tz4local)
    #UTC+08:00
aware_datetime8platform_epoch = datetime.fromtimestamp(0.0, tz4utc)
    #use arbitrary tzinfo is ok, since from same timestamp==0.0


#class Error__platform_epoch_is_too_far_from_utc0(Error):pass




def __():
    def time_struct5timestamp_(local_vs_utc, timestamp, /):
        'local_vs_utc/bool -> timestamp<platform_epoch>/float -> time_struct<local_vs_utc>/struct_time  #loss accuracy: [resolution==1 second] i.e. be int when converted back, see:timegm__int #use datetime instead'
    #datetime.fromtimestamp(timestamp, tz=None) -> naive datetime object if tz is None

def tz5or__local_vs_utc_(local_vs_utc__or__tz, /):
    if type(local_vs_utc__or__tz) is bool:
        local_vs_utc = local_vs_utc__or__tz
        tz = tz4local if local_vs_utc is False else tz4utc
    else:
        tz = local_vs_utc__or__tz
    tz

    check_tzinfo(tz)
    return tz
def check_tzinfo(tz, /):
    if not isinstance(tz, tzinfo):raise TypeError(tz)

def aware_datetime5timestamp_(local_vs_utc__or__tz, timestamp, /):
    r'''[[[
    :: (local_vs_utc/bool | tz/tzinfo) -> timestamp<platform_epoch>/float -> aware_datetime<tz>/datetime

    #loss accuracy: [resolution==1microsecond]

    vs:
        time_struct5timestamp_.resolution==1second
        aware_datetime5timestamp_.resolution==1microsecond

    #]]]'''#'''
    #utcoffset4local
    check_type_is(float, timestamp)
    tz = tz5or__local_vs_utc_(local_vs_utc__or__tz)
    aware_datetime = datetime.fromtimestamp(timestamp, tz)
    return aware_datetime

assert aware_datetime5timestamp_(True, 0.0) == aware_datetime5timestamp_(tz4utc, 0.0)
assert aware_datetime5timestamp_(False, 0.0) == aware_datetime5timestamp_(tz4local, 0.0)

assert aware_datetime5timestamp_(True, 0.0) == datetime.fromtimestamp(0.0, tz4utc)
#assert aware_datetime5timestamp_(False, 0.0) == datetime.fromtimestamp(0.0, None), (aware_datetime5timestamp_(False, 0.0), datetime.fromtimestamp(0.0, None))
    #AssertionError: (datetime.datetime(1970, 1, 1, 8, 0, tzinfo=datetime.timezone(datetime.timedelta(seconds=28800))), datetime.datetime(1970, 1, 1, 8, 0))
#assert not (aware_datetime5timestamp_(False, 0.0) -datetime.fromtimestamp(0.0, None)), (aware_datetime5timestamp_(False, 0.0), datetime.fromtimestamp(0.0, None))
    #TypeError: can't subtract offset-naive and offset-aware datetimes
assert aware_datetime5timestamp_(False, 0.0).timetuple() == datetime.fromtimestamp(0.0, None).timetuple()
assert aware_datetime5timestamp_(False, 0.0).replace(tzinfo=None) == datetime.fromtimestamp(0.0, None)

def is_datetime_aware(x_datetime, /):
    return not is_datetime_naive(x_datetime)
def is_datetime_naive(x_datetime, /):
    check_type_is(datetime, x_datetime)
    return x_datetime.tzinfo is None
def check_aware_datetime(aware_datetime, /):
    if is_datetime_naive(aware_datetime): raise TypeError(f'not aware: {aware_datetime!r}')
    return
    check_type_is(datetime, aware_datetime)
    if aware_datetime.tzinfo is None: raise TypeError(f'not aware: {aware_datetime!r}')
def aware_datetime2timestamp_(aware_datetime, /):
    r'''[[[
    :: aware_datetime<tz>/datetime -> timestamp<platform_epoch>/float



datetime.timestamp() -> float/timestamp
    === (aware_datetime - datetime(1970, 1, 1, tzinfo=timezone.utc)).total_seconds()
        weird. why? this is timestamp<epoch=1970_01_01_000000> not timestamp<platform_epoch>
        #since termux epoch==1970_01_01_000000, donot detect diff
        run test, impl <==>:
          timestamp = (aware_datetime - datetime.fromtimestamp(0.0, aware_datetime.tzinfo)).total_seconds()
                #use arbitrary tzinfo is ok, since from same timestamp==0.0
    or:
    === mktime(naive_datetime.timetuple())
      ~ (naive_datetime - datetime.fromtimestamp(0.0)).total_seconds()
      xxx ~ (naive_datetime - datetime(1970, 1, 1, tzinfo=None)).total_seconds()

    #]]]'''#'''
    #??? weird:timestamp = aware_datetime.timestamp()

    #timestamp = (naive_datetime - datetime.fromtimestamp(0.0)).total_seconds()

    #timestamp = (aware_datetime - datetime.fromtimestamp(0.0, aware_datetime.tzinfo)).total_seconds()
        #use arbitrary tzinfo is ok, since from same timestamp==0.0
    check_aware_datetime(aware_datetime)
    timestamp = (aware_datetime - aware_datetime8platform_epoch).total_seconds()
    return timestamp



get_now__timestamp
get_now__time_struct_
def get_now__aware_datetime_(local_vs_utc__or__tz=False, /):
    '(local_vs_utc/bool | tz/tzinfo) -> now/aware_datetime<tz>/datetime'
    timestamp__now = get_now__timestamp()
    aware_datetime__now = aware_datetime5timestamp_(local_vs_utc__or__tz, timestamp__now)
        #use arbitrary tzinfo is ok, since from same timestamp__now
    return aware_datetime__now

class Case4datetime_isoformat_timespec(Enum):
    r'''[[[
    datetime.isoformat(sep='T', timespec='auto')¶

datetime.fromisoformat
datetime.isoformat
  datetime.isoformat(sep='T', timespec='auto')¶
fmt: YYYY-MM-DD{sep}HH:MM:SS[.ffffff][+HH:MM[:SS[.ffffff]]]
  #see:time.isoformat():kw:timespec
  >>> datetime(2019, 5, 18, 15, 17, 8, 132263).isoformat()
  '2019-05-18T15:17:08.132263'
  >>> datetime(2019, 5, 18, 15, 17, tzinfo=timezone.utc).isoformat()
  '2019-05-18T15:17:00+00:00'

date.fromisoformat
date.isoformat() -> str
  fmt: 'YYYY-MM-DD'

time.fromisoformat
time.isoformat
  time.isoformat(timespec='auto')¶
fmt: HH:MM:SS[.ffffff][+HH:MM[:SS[.ffffff]]]
  ??? [.microsecond == 0]
  ??? [.utcoffset() is None]

  timespec:
      'auto':
          HH:MM:SS[.ffffff] format
      'microseconds':
          HH:MM:SS.ffffff format
      'milliseconds':
          HH:MM:SS.sss format
            #truncate, not round
      'seconds':
          HH:MM:SS format
      'minutes':
          HH:MM format
      'hours':
          HH format



    #]]]'''#'''
    until_hour = 'hours'
    until_minute = 'minutes'
    until_second = 'seconds'
    until_millisecond = 'milliseconds'
    until_microsecond = 'microseconds'
    auto_omit_microsecond = 'auto'
TimeFormatDirective
#strftime?
#timespec?



def __():
    def time_struct2formatted_str_(may_time_fmt, time_struct, /):
        'may time_fmt/str -> time_struct<local_vs_utc>/struct_time -> formatted_str<local_vs_utc>/str'
    def time_struct5formatted_str_(may_time_fmt, formatted_str, /):
        'may time_fmt/str -> formatted_str<local_vs_utc>/str -> time_struct<local_vs_utc>/struct_time'

def datetime2formatted_str_(may_time_fmt, x_datetime, /, *, mismatch_tzinfo_ok=False):
    r'''[[[
    'may time_fmt/str -> x_datetime<may_tz>/datetime -> formatted_str<smay_utcoffset>/str'

[x_datetime :: (aware_datetime|naive_datetime)]

datetime.ctime() -> str<timestamp>
  === time.ctime(time.mktime(d.timetuple()))
    !!!drop tzinfo!!!
    ===
    using same default_time_fmt
        ==>> time_fmt5may_

    #]]]'''#'''
    check_type_is(datetime, x_datetime)
    time_fmt = time_fmt5may_(may_time_fmt)
    if not mismatch_tzinfo_ok:
        if not (is_datetime_aware(x_datetime) is is_the_time_zone_offset_directive_in_time_fmt(time_fmt)): raise Error__miss_tzinfo__strptime_mismatch_strftime

    formatted_str = x_datetime.strftime(time_fmt)
    return formatted_str
def datetime5formatted_str_(may_time_fmt, formatted_str, /):
    r'''[[[
    'may time_fmt/str -> formatted_str<smay_utcoffset>/str -> x_datetime<may_tz>/datetime'
[x_datetime :: (aware_datetime|naive_datetime)]
    #]]]'''#'''

    time_fmt = time_fmt5may_(may_time_fmt)
    x_datetime = datetime.strptime(formatted_str, time_fmt)
    return x_datetime

#re.compile(r'(?:[^%]|%.)')
_time_fmt_directive__regex = re.compile(r'(%.)')
assert _time_fmt_directive__regex.split('a%%b%cd') == ['a', '%%', 'b', '%c', 'd']
assert _time_fmt_directive__regex.split('a%%bc%d') == ['a', '%%', 'bc', '%d', '']

def _parse_time_fmt(time_fmt, /):
    check_type_is(str, time_fmt)
    raw_or_directive__ls = _time_fmt_directive__regex.split(time_fmt)
    return raw_or_directive__ls
def is_the_time_zone_offset_directive_in_time_fmt(time_fmt, /):
    raw_or_directive__ls = _parse_time_fmt(time_fmt)
    return ('%z' in raw_or_directive__ls)

def aware_datetime2formatted_str_(time_fmt, aware_datetime, /):
    'time_fmt/str -> aware_datetime<tz>/datetime -> formatted_str<utcoffset>/str'
    check_aware_datetime(aware_datetime)
    #time_fmt = time_fmt5may_(may_time_fmt)
    #   default_time_fmt doesnot contain '%z'
    check_type_is(str, time_fmt)

    #if not ('%z' in time_fmt): raise Error__miss_tzinfo__strptime_mismatch_strftime
    if not is_the_time_zone_offset_directive_in_time_fmt(time_fmt): raise Error__miss_tzinfo__strptime_mismatch_strftime
    formatted_str = datetime2formatted_str_(time_fmt, aware_datetime)
    return formatted_str

def aware_datetime5formatted_str_(time_fmt, formatted_str, /):
    'time_fmt/str -> formatted_str<utcoffset>/str -> aware_datetime<tz>/datetime'
    # default_time_fmt doesnot contain '%z'
    check_type_is(str, formatted_str)
    check_type_is(str, time_fmt)
    if not is_the_time_zone_offset_directive_in_time_fmt(time_fmt): raise Error__miss_tzinfo__strptime_mismatch_strftime
    x_datetime = datetime5formatted_str_(time_fmt, formatted_str)
    check_aware_datetime(x_datetime)
    aware_datetime = x_datetime
    return aware_datetime

def __():
    def timestamp2formatted_str__via_time_struct__(may_time_fmt, local_vs_utc, timestamp, /):
        'may time_fmt/str -> local_vs_utc/bool -> timestamp<platform_epoch>/float -> formatted_str<local_vs_utc>/str  #loss accuracy: [resolution==1 second] i.e. be int when converted back, see:timegm__int #use datetime instead'
    def timestamp5formatted_str__via_time_struct__(may_time_fmt, local_vs_utc, formatted_str, /):
        'may time_fmt/str -> local_vs_utc/bool -> formatted_str<local_vs_utc>/str -> timestamp<platform_epoch>/float'

def timestamp2formatted_str__via_datetime__(may_time_fmt, local_vs_utc__or__tz, timestamp, /, *, mismatch_tzinfo_ok=False):
    'may time_fmt/str -> (local_vs_utc/bool | tz/tzinfo) -> timestamp<platform_epoch>/float -> formatted_str<tz,smay_utcoffset>/str  #loss accuracy: [resolution==1microsecond]'
    aware_datetime = aware_datetime5timestamp_(local_vs_utc__or__tz, timestamp)
    mismatch_tzinfo_ok = mismatch_tzinfo_ok or aware_datetime.tzinfo == tz4local
    #aware_datetime2formatted_str_
    formatted_str = datetime2formatted_str_(may_time_fmt, aware_datetime, mismatch_tzinfo_ok=mismatch_tzinfo_ok)
    return formatted_str
def timestamp5formatted_str__via_datetime__(may_time_fmt, local_vs_utc__or__tz, formatted_str, /, ):
    'may time_fmt/str -> tz4default/(local_vs_utc/bool | tz/tzinfo) -> formatted_str<tz4default,smay_utcoffset>/str -> timestamp<platform_epoch>/float'
    tz4default = tz5or__local_vs_utc_(local_vs_utc__or__tz)
    #aware_datetime5formatted_str_
    x_datetime = datetime5formatted_str_(may_time_fmt, formatted_str)
    if is_datetime_naive(x_datetime):
        naive_datetime = x_datetime
        #x_datetime = naive_datetime.replace(tzinfo=tz4local)
        x_datetime = naive_datetime.replace(tzinfo=tz4default)
    check_aware_datetime(x_datetime)
    aware_datetime = x_datetime
    #if not aware_datetime.tzinfo == tz: raise Error__mismatch_tzinfo
    timestamp = aware_datetime2timestamp_(aware_datetime)
    return timestamp





#rest,relax,leisure
#work,labor,toil
#class PeriodicWorkRest
def default_mkr4seconds4leisure(seconds4toil, seconds4leisure, actual_seconds4toil, /):
    'seconds4toil/float -> seconds4leisure/float -> actual_seconds4toil/float -> actual_seconds4leisure/float'
    actual_seconds4leisure = seconds4leisure
    return actual_seconds4leisure
class PeriodicToilLeisureTime:
    'sleep if work too long enough'
    # used in:view script/搜索冫最短加链长度.py
    # see also:view ../../python3_src/seed/for_libs/for_signal.py
    #       PostponeKeyboardInterrupt
    def __init__(sf, seconds4toil:float, seconds4leisure:float, may_mkr4seconds4leisure=None, /, *, may_prompt_string6resting=None):
        '[may_mkr4seconds4leisure :: may (seconds4toil/float -> seconds4leisure/float -> actual_seconds4toil/float -> actual_seconds4leisure/float)]'
        mkr4seconds4leisure = ifNone(may_mkr4seconds4leisure, default_mkr4seconds4leisure)
        check_callable(mkr4seconds4leisure)
        if mkr4seconds4leisure is default_mkr4seconds4leisure:
            may_mkr4seconds4leisure = None

        if not (prompt_string6resting := may_prompt_string6resting) is None:
            check_type_is(str, prompt_string6resting)

        #check_type_is(float, seconds4toil)
        #check_type_is(float, seconds4leisure)
        sf.seconds4toil = float(seconds4toil)
        sf.seconds4leisure = float(seconds4leisure)
        sf.mkr4seconds4leisure = mkr4seconds4leisure
        sf.may_mkr4seconds4leisure = may_mkr4seconds4leisure
        sf.may_prompt_string6resting = may_prompt_string6resting
        sf._g = get_consumed_duration__thread_wide
        sf.reset()
    def reset(sf, /):
        sf._t0 = sf._g()
    def resting_(sf, actual_seconds4toil, /):
        if not (prompt_string6resting := sf.may_prompt_string6resting) is None:
            print_err(prompt_string6resting, end='')
        actual_seconds4leisure = sf.mkr4seconds4leisure(sf.seconds4toil, sf.seconds4leisure, actual_seconds4toil)
        sleep(actual_seconds4leisure)
        #sleep(sf.seconds4leisure)
        sf.reset()
    def __call__(sf, /):
        'sleep if work too long enough'
        t1 = sf._g()
        t0 = sf._t0
        dt = t1 -t0
        if not dt < sf.seconds4toil:
            sf.resting_(dt)
        return
    def sleep_if_work_too_long_enough_(sf, /):
        sf()

######################
######################
######################

__all__

if __name__ == "__main__":
    pass
__all__


# :,$s/ \w\@=/ ,/g
from seed.for_libs.for_time import (
time_struct8platform_epoch___tz4utc
,time_struct8platform_epoch___tz4local
,aware_datetime8platform_epoch
,tz4utc
,tz4local
    ,utcoffset4local
        ,total_seconds4utcoffset4local





,Case4datetime_isoformat_timespec
,TimeFormatDirective
    ,time_fmt5py_str_fmt_
    ,time_fmt5snippets_
,default_time_fmt
    ,time_fmt5may_


,Error
    ,Error__miss_tzinfo__strptime_mismatch_strftime
    ,Error__mismatch_tzinfo






,get_now__timestamp
,get_now__time_struct_
,get_now__aware_datetime_

,get_consumed_duration__system_wide__monotonic
,get_consumed_duration__system_wide__highest_resolution
,get_consumed_duration__process_wide
,get_consumed_duration__thread_wide


,Timer
    ,timer__thread_wide
    ,timer__process_wide
    ,timer__system_wide__highest_resolution
    ,timer__system_wide__monotonic

    ,Timer__print_err
        ,timer__print_err__thread_wide
        ,timer__print_err__process_wide
        ,timer__print_err__system_wide__highest_resolution
        ,timer__print_err__system_wide__monotonic




,aware_datetime5timestamp_
,aware_datetime2timestamp_

,aware_datetime5formatted_str_
,aware_datetime2formatted_str_

,timestamp2formatted_str__via_datetime__
,timestamp5formatted_str__via_datetime__

,datetime2formatted_str_
,datetime5formatted_str_

,time_struct5timestamp_
,time_struct2timestamp_

,time_struct2formatted_str_
,time_struct5formatted_str_

,timestamp2formatted_str__via_time_struct__
,timestamp5formatted_str__via_time_struct__





,tz5or__local_vs_utc_
    ,check_tzinfo

,is_datetime_aware
,is_datetime_naive
,check_aware_datetime
,is_the_time_zone_offset_directive_in_time_fmt
)

from seed.for_libs.for_time import PeriodicToilLeisureTime










from seed.for_libs.for_time import *
