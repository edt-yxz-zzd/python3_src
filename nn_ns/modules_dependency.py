
'''
modules_dependency of same package

'''

from sand import to_names, top_level_import
__all__ = to_names('''
    
    get_direct_depending_module_names
    get_submodule_basenames
    
    modules_dependency 
    package_to_basename2submodule
    package_to_submodule2depends
    
    try_import
''')
assert top_level_import(__name__, 'sand.forgot_import', args=('logic error',))
assert top_level_import(__name__, 'sand.collect_globals',
                        kwargs=dict(pred=None, include='', exclude='''
    nul_pprint nul_print org_pprint org_print
    package_name cycles height_name_depends_ls
    basename2module_to_basename2depends
    modulename2depends_to_v2name_v2neighbors
    pkg_basename2depends_to_modulename2depends
    '''))


import os.path, importlib
from importlib import import_module
import inspect
from pprint import pprint

from nn_ns.graph.directed_graph import strong_connected_components
from nn_ns.graph.directed_acyclic_graph import u2vtc_to_heights

#suffixes = importlib.machinery.SOURCE_SUFFIXES 


def get_submodule_basenames(path):
    for fname in os.listdir(path):
        module_name = inspect.getmodulename(fname)
        
        if module_name is not None:
            yield module_name
            
def try_import(module_name, package_name):
    try:
        m = import_module(module_name, package_name)
        return m
    except (ImportError, SyntaxError):
        return None

def get_direct_depending_module_names(module):
    names = set()
    for attr in dir(module):
        m = inspect.getmodule(getattr(module, attr))
        if m is not None:
            names.add(m.__name__)
    names.discard(module.__name__)
    return names

org_print = print
nul_print = lambda *args, **kwargs: None
org_pprint = pprint
nul_pprint = nul_print

def package_to_basename2submodule(package_name, basename_pred, debug = False):
    if basename_pred is None:
        basename_pred = lambda basename: not basename.startswith('_')
    print = org_print if debug else nul_print

    # require pkg was imported before import submodule if use __import__
    pkg = import_module(package_name)
    path = os.path.dirname(pkg.__file__)
    submodule_basenames = get_submodule_basenames(path)

    basename2submodule = {}
    pred = basename_pred
    for basename in filter(pred, submodule_basenames):
        submodule = try_import('.'+basename, package_name)
        if submodule is not None:
            basename2submodule[basename] = submodule
            print('imported:', basename)
            continue
        print('skip:', basename)

    return basename2submodule

def basename2module_to_basename2depends(
        basename2module, depend_name_pred, debug = False):
    pprint = org_pprint if debug else nul_pprint

    basename2depends = {}
    for basename, module in basename2module.items():
        depends = get_direct_depending_module_names(module)
        depends = filter(depend_name_pred, depends)
        basename2depends[basename] = sorted(depends)
    pprint(('basename2depends = ',
            basename2depends))
    return basename2depends


    
def package_to_submodule2depends(
        package_name,
        basename_pred=None,
        depend_name_pred=None,
        debug = False):
    '''
basename_pred :: submodule_basename -> bool
depend_name_pred :: depending_module_name -> bool
'''

    if depend_name_pred is None:
        depend_name_pred = lambda depend_name: \
                           depend_name.startswith(package_name)

    basename2submodule = package_to_basename2submodule(
        package_name, basename_pred, debug)
    basename2depends = basename2module_to_basename2depends(
        basename2submodule, depend_name_pred, debug)


    return basename2depends

def pkg_basename2depends_to_modulename2depends(package_name, basename2depends):
    return {package_name+'.'+basename : depends
            for basename, depends in basename2depends.items()}


def modulename2depends_to_v2name_v2neighbors(modulename2depends):
    name2ls = modulename2depends
    v2name = names = sorted(name2ls)
    name2vtx = dict(reversed(v_name) for v_name in enumerate(names))

    v2neighbors = [sorted(name2vtx[name] for name in set(name2ls[name]))
                   for name in names]
    
    return v2name, v2neighbors


    
def modules_dependency(package_name):
    basename2depends = package_to_submodule2depends(package_name)
    modulename2depends = pkg_basename2depends_to_modulename2depends(
        package_name, basename2depends)

    v2name, v2neighbors = modulename2depends_to_v2name_v2neighbors(modulename2depends)
    vtc_ls, edges_ls, discarded_edges = strong_connected_components(v2neighbors)
    #print(vtc_ls, v2neighbors)
    cycles = [sorted(v2name[v] for v in vtc)
              for vtc in vtc_ls if len(vtc) > 1]
    

    heights = u2vtc_to_heights(v2neighbors)
    #print(heights)
    height_name_depends_ls = sorted(
        (height, v2name[v], modulename2depends[v2name[v]])
        for v, height in enumerate(heights))
    return height_name_depends_ls, cycles


if __name__ == "__main__":
    package_name = 'sand'
    height_name_depends_ls, cycles = modules_dependency(package_name)
    if cycles:
        pprint(cycles)
    pprint([tri for tri in height_name_depends_ls if tri[0]])



#package_to_submodule2depends('sand', debug=True)
#
