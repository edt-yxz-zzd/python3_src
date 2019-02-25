
'''

datetime in http_headers
####################################
Date: Wed, 15 Nov 1995 06:25:24 GMT
Last-Modified: Wed, 15 Nov 1995 04:58:08 GMT
Expires: Thu, 01 Dec 1994 16:00:00 GMT
...
...
####################################
'''

__all__ = '''
    http_datetime_fmt
    parse_datetime_in_http_headers
    touch_file_by_http_datetime__str
    '''.split()
import time
import datetime

http_datetime_fmt = "%a, %d %b %Y %H:%M:%S GMT"
def parse_datetime_in_http_headers(http_datetime__str):
    #https://stackoverflow.com/questions/10175134/last-modified-of-file-downloaded-does-not-match-its-http-header
    # Last-Modified: Wed, 15 Nov 1995 04:58:08 GMT
    http_datetime__float_seconds = time.mktime(time.strptime(http_datetime__str, http_datetime_fmt))
    http_datetime__datetime = datetime.datetime.strptime(http_datetime__str, http_datetime_fmt)
    assert http_datetime__datetime.timestamp() == http_datetime__float_seconds
    return http_datetime__datetime


def touch_file_by_http_datetime__str(path, http_datetime__str):
    http_datetime__datetime = parse_datetime_in_http_headers(http_datetime__str)
    http_datetime__float_seconds = http_datetime__datetime.timestamp()

    #os.utime(ofname, (last_modified_time__float_seconds, last_modified_time__float_seconds))
    os.utime(path, (http_datetime__float_seconds, http_datetime__float_seconds))


