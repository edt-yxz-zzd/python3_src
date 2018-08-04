

def get_class_qualname(bounded_class_method):
    n = bounded_class_method.__name__
    q = bounded_class_method.__qualname__
    #g = bounded_method.__globals__
    class_qualname = q[:-1-len(n)]
    return class_qualname

    sub = bounded_method.__self__.__class__
    for t in sub.mro():
        print(t)
        if t.__qualname__ == c:
            return t

class init_once_class:
    def __init__(self, *args, **key_args):
        this = init_once_class
        mro = type(self).mro()
        init_ls = []
        qnames = tuple(c.__qualname__ for c in mro)
        
        qthis = this.__qualname__
        i = 0
        end = len(qnames) - 1
        qcurr = get_class_qualname(self._init_once)
        while i < end:
            try:
                i = qnames.index(qcurr, i)
            except:
                print(i, qnames)
                print(qcurr)
            assert i < end
            if qthis == qcurr: break

            curr = mro[i]
            if issubclass(curr, this): init_ls.append(curr)
            qcurr = get_class_qualname(super(curr, self)._init_once)

        else:
            raise '??'
        init_ls.append(this)
        for t, c in zip(init_ls, init_ls[1:]):
            assert t is not c

        
        for c in reversed(init_ls):
            c._init_once(self, *args, **key_args)
            
    def _init_once(self, *args, **key_args):
        pass
        
class my_except(init_once_class, Exception):
    def _init_once(self, *args, **key_args):
        Exception.__init__(self, args, key_args)

class internet_except(my_except): pass

class unknown_case_except(my_except): pass

if __name__ == '__main__':
    print(internet_except.__init__)
    print(internet_except._init_once)
    internet_except('', a='')
