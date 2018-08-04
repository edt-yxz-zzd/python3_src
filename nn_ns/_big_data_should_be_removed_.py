
from sand import fixed__package__
fixed__package__(globals())
from sand import top_level_import
assert top_level_import(__name__, 'import_main.forgot_import', args=('logic error',))
assert top_level_import(__name__, 'import_main.collect_globals',
        kwargs=dict(pred=None, include='', exclude='''
    main'''))

from sand import to_names, unzip
from sand import dot, apply, pdot, papp, id_func

from nn_ns.filedir.file_filter import file_size_filter, FileFilter, get_file_size
import os
from pprint import pprint


import nn_ns


K = 2**10
M = K**2
G = K**3



def module2root(module):
    root = os.path.dirname(os.path.abspath(module.__file__))
    return root

def files_of_size_gt(size, top_dir, *args, **kwargs):
    pred_size = lambda fsize: fsize > size
    yield from file_size_filter(pred_size, top_dir, *args, **kwargs)

##print(module2root(nn_ns))
##path = r'E:\my_data\program_source\python3_src\nn_ns\algo'
##print(get_file_size(path))
##papp(list, ..., FileFilter(print, print)(path))
##papp(list, ..., files_of_size_gt(50*K, module2root(nn_ns)))

def show_big_files_in_package(module, size=50*K,
                              *, print=pprint, relpath=True,
                              dict=dict):
    root = module2root(module)
    if relpath == True:
        rel = lambda path: os.path.relpath(path, root)
    else:
        rel = id_func
    #apply(print, list, map, ..., rel, files_of_size_gt(size, root))
        
    path2rel_size = lambda path: (rel(path), get_file_size(path))
    apply(print, dict, map, ..., path2rel_size, files_of_size_gt(size, root))

show_big_files_in_package(nn_ns)



