
r'''
this script proof: "except:" catch any BaseException!!! not only Exception


py -m script.try_python.try_keywords.try_except

try:
    ...
except:
    ...
    this script proof: "except:" catch any BaseException!!! not only Exception
else:
    ...
finally:
    ...
:
#'''

try:
    quit()
except:
    print('catch quit()')
    pass

try:
    raise BaseException
except:
    print('catch BaseException')
    pass

