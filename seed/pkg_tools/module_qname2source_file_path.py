
r'''
what file?
    *.py/pyc/...????
here source file


module_object.__file__
inspect.getfile(module_object)

inspect.getfile(inspect.currentframe())
    get the path of the currently running script

#imp.find_module(module_qname)#deprecated
https://stackoverflow.com/questions/247770/retrieving-python-module-path


####################
maybe_spec = importlib.util.find_spec(module_qname)
if maybe_spec is not None:
    spec = maybe_spec
    maybe_source_file_path = spec.origin
    if maybe_source_file_path is not None:
        source_file_path = maybe_source_file_path
        return source_file_path

'''

__all__ = '''
    module_qname2source_file_path
    module_qname2maybe_source_file_path
    '''.split()


from importlib.util import find_spec

def module_qname2source_file_path(module_qname):
    maybe_source_file_path = module_qname2maybe_source_file_path(module_qname)
    if maybe_source_file_path is not None:
        source_file_path = maybe_source_file_path
        return source_file_path
    raise FileNotFoundError(f'donot find source file to {module_qname!r}')
    raise ImportError

def module_qname2maybe_source_file_path(module_qname):
    maybe_spec = find_spec(module_qname) # may raise ValueError
    if maybe_spec is not None:
        spec = maybe_spec
        maybe_source_file_path = spec.origin
        return maybe_source_file_path
    return None

