

##print(__file__)
##print(globals()['__file__'])
      
from sand import fixed__package__
#fixed__package__(globals())
fixed__package__(__name__)
#print(__file__)
#print(__package__)
#print(__name__)
from .b import *
from .a import *
print('print once')


