
from sand import top_level_import
assert top_level_import(__name__, 'import_main.forgot_import', args=('logic error',))


import os, os.path
import shutil

def get_file_size(*paths):
    
    # os.path.getsize on dir not return usage;
    # shutil.disk_usage not for normal file,
    #        and return the whole disk info instead of dir
    path = os.path.join(*paths)
    try:
        return os.path.getsize(path)
        if os.path.isfile(path) or os.path.islink(path):
            return os.path.getsize(path)
        else:
            return shutil.disk_usage(path).used
    except:
        print(get_file_size, paths, path)
        raise


##def _handle_dir(dirpath):
##    pass
##def file_handler(top_dir, handle_file, handle_dir=_handle_dir):
##    'handle_file(dirpath, fname); handle_dir(dirpath)'
##    for dirpath, dirnames, filenames in os.walk():
##        handle_dir(dirpath)
##        for fname in filenames:
##            handle_file(dirpath, fname)
            
class FileFilter:
    def __init__(self, pred_fname, pred_dir=lambda dirpath:False):
        'pred_fname(dirpath, fname); pred_dir(dirpath)'
        self.pred_fname = pred_fname
        self.pred_dir = pred_dir
    def __call__(self, top_dir, *args, **kwargs):
        '''yield (dirpath,) or (dirpath, fname)
os.walk(top_dir, *args, **kwargs)'''
        for dirpath, dirnames, filenames in os.walk(top_dir, *args, **kwargs):
            if self.pred_dir(dirpath):
                yield (dirpath,)
            for fname in filenames:
                if self.pred_fname(dirpath, fname):
                    yield (dirpath, fname)




def file_size_filter(pred_size, top_dir, *args, **kwargs):
    '''yield filepath
os.walk(top_dir, *args, **kwargs)'''
    pred_fname = lambda dirpath, fname: pred_size(get_file_size(dirpath, fname))
    for dirpath, fname in FileFilter(pred_fname)(top_dir, *args, **kwargs):
        yield os.path.join(dirpath, fname)
    return





if __name__ == '__main__':
    pr = lambda path: print('get_file_size({!r}) = {}'
                            .format(path, get_file_size(path)))
    pr(__file__)
    pr('.')











        
