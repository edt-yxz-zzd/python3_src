
def get(self):
    print('get property')

I_am_property = property(get)

#import try_module_property
__import__(__name__).I_am_property
import try_module_property
# no string printed!!!!!!!!!!!
# fail !!!!!!!!!!!!!!!!







