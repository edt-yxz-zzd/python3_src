
__all__ = ['TesterBase']

from pprint import pprint
import sys # for stdout
import io

class TesterBase:
    def __init__(self):
        self.turn_on_show()
    def turn_off_show(self):
        self.file = io.StringIO()
    def turn_on_show(self):
        self.file = sys.stdout
        
    def print(self, *args, **kwargs):
        print(*args, file=self.file, **kwargs)
        
    def pprint(self, *args, **kwargs):
        pprint(*args, stream=self.file, **kwargs)
        
    def __getattribute__(self, attr):
        # bug: infinite recur
        #    print = self.print
        if attr.startswith('test__'):
            cls_name = type(self).__name__
            print = self.print
            print('\n'*4)
            print('calling --->>> {}.{}'.format(cls_name, attr))
        return super().__getattribute__(attr)
