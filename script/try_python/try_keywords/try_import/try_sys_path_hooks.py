
import sys

ls = sys.path_hooks
print(ls)
i = 1
if i == 0:
    def fNone(path): # return None means fail
        print('fNone : ' + path)
        return

    def fError(path): # raise ImportError means ignore and continue
        print('fError : ' + path)
        raise ImportError('try : ' + path)
        return


    ls[0:0] = [fError, fNone, fError]
    import nn_ns
elif i == 1:
    class module_T:
        def __getitem__(self, key):
            print('module_T.'+attr)
            return key
        def __getattribute__(self, attr):
            print('module_T.'+attr)
            raise
            return attr
        def __getattr__(self, attr):
            print('module_T.'+attr)
            return attr
        nn_ns = 'afaf'
    class loader_T:
        def load_module(self, qname):
            print('loader_T().load_module :' + qname)
            return module_T()
            raise ImportError
            return None
    class path_entry_finder_T:
        def find_loader(self, qname):
            return None, [module_T()]
            return None, {'nn_ns':loader_T()}
            return None, [loader_T(), loader_T()]

    def fPortion(path):
        print('fPortion : ' + path)
        return path_entry_finder_T()

    ls[0:0] = [fPortion]
    import nn_ns
    import nn_ns.afaf
    import nn_ns.afafadfd.afaddg.afaf




        
