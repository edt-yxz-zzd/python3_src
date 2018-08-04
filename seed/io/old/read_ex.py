'''
another version of read_or_calc_xwrite
'''

__all__ = ['read_ex', 'set_read_ex_home']
#from .. import LogicError
import pickle, os, io

def to_type(x, T):
    if type(x) is T:
        return x
    return T(x)

def to_tuple(iterable):
    return to_type(iterable, tuple)
def std_args(args):
    return to_type(args, tuple)

def std_kwargs(kwargs):
    return to_type(kwargs, dict)

def std_args_kwargs(args, kwargs):
    return std_args(args), std_kwargs(kwargs)

def skipN(iterable, N):
    'since islice return a empty generator if no N elements instead of raise'
    if not N >= 0:
        raise ValueError('N < 0')
    
    it = iter(iterable)
    if not N:
        return it
    
    start = int(-N+1)
    assert start <= 0
    for i, _ in enumerate(it, -N+1):
        if not i:
            return it
    raise ValueError('too few elements')


def takeN_ex(iterable, N):
    '''take first N values

ls, iter_tail = takeN(iterable, N)
assert len(ls) == N
'''
    if not N >= 0:
        raise ValueError('N < 0')
    
    it = iter(iterable)
    ls = [x for _, x in zip(range(N), it)]
    
    if len(ls) != N:
        assert len(ls) < N
        raise ValueError('too few elements')
    return ls, it


__read_ex_home = ''

def set_read_ex_home(path=None):
    'if path is None, return home else set it'
    global __read_ex_home
    if path is None:
        return __read_ex_home
    else:
        __read_ex_home = path
    return

class ReadWriteObjects:
    '''

format : length, obj...
iread - iter (obj...)
iread_ex - iter (length, obj...)
write - write out objects
'''
    ################## os ops ##################
    
    def open_(self, *args, **kwargs):
        return open(*args, **kwargs)
    def remove(self, path):
        'both exists or not - precondition'
        os.remove(path)
    def join(self, path, *paths):
        return os.path.join(path, *paths)
    def exists(self, path):
        return os.path.exists(path)
    def abspath(self, path):
        return os.path.abspath(path)

    #################### worker ###################

    def __init__(self, protocol=None):
        self.protocol = protocol
    def iread_file_ex(self, fin, *, yield_len=True, check_len=None):
        '''check len(file.objs) == check_len if check_len is not None'''
        load = pickle.Unpickler(fin).load
        L = load()
        if check_len is not None:
            if L != check_len:
                raise ValueError('length not match')
        if yield_len:
            yield L
            
        for _ in range(L):
            yield load()
        
    def iread_path_ex(self, path, *, yield_len=True, check_len=None):
        with self.open_(path, 'rb') as fin:
            yield from self.iread_file_ex(fin,
                                          yield_len=yield_len,
                                          check_len=check_len)
        return

    def iread_file(self, fin, *, check_len=None):
        return self.iread_file_ex(fin,
                                  yield_len=False,
                                  check_len=check_len)


    def iread_path(self, path, *, check_len=None):
        return self.iread_path_ex(fin,
                                  yield_len=False,
                                  check_len=check_len)

    
    

    def write_file(self, fout, objs):
        objs = to_tuple(objs)
        L = len(objs)
        dump = pickle.Pickler(fout, self.protocol).dump
        dump(L)
        for obj in objs:
            dump(obj)
    def write_path(self, path, force, objs, remove=True):
        'remove if fail'
        flag = 'wb' if force else 'xb'
        objs = to_tuple(objs)
        
        fout = old_fout = [] # fout maybe any thing
        try:
            with self.open_(path, flag) as fout:
                self.write_file(fout, objs)
        except:
            if fout is not old_fout:
                # del file
                if remove:
                    self.remove(path)
            raise
        return

class ReadWriteObjects__BytesIOMixin:
    'override ReadWriteObjects::os_ops'
    
    def _newfile(self, abspath, initial=b''):
        if self._exists(abspath):
            raise FileExistsError
        self.abspath2file[abspath] = file = io.BytesIO(initial)
        def close():
            self.abspath2file[abspath] = file.getvalue()
            return type(file).close(file)
        file.close = close
        return file
    def _access_check(self, abspath):
        if not self._exists(abspath):
            raise FileNotFoundError
        if self._opened(abspath):
            raise PermissionError('file opened')
    def _removefile(self, abspath):
        if self._opened(abspath):
            raise PermissionError('file opened')
        self.abspath2file.pop(abspath, None)
    def _getfile(self, abspath):
        self._access_check(abspath)
        bs = self.abspath2file[abspath]
        self._removefile(abspath)
        return self._newfile(abspath, bs)
    def _exists(self, abspath):
        return abspath in self.abspath2file
    def _opened(self, abspath):
        return type(self.abspath2file.get(abspath, b'')) is not bytes

    
    def __init__(self):
        self.abspath2file = {}
        
    def open_(self, path, flag):
        if flag not in ['rb', 'wb', 'xb']:
            raise ValueError('unknown open flag')
        path = self.abspath(path)
        if flag == 'rb':
            return self._getfile(path)
        if flag == 'xb':
            pass
        elif flag == 'wb':
            self.remove(path)
        else:
            raise logic-error
        return self._newfile(path)

    
    def remove(self, path):
        self._removefile(self.abspath(path))
    def exists(self, path):
        return self._exists(self.abspath(path))
    
class Bytes_RWObjs(ReadWriteObjects__BytesIOMixin, ReadWriteObjects):
    def __init__(self, protocol=None):
        ReadWriteObjects__BytesIOMixin.__init__(self)
        ReadWriteObjects.__init__(self, protocol)

def read_ex(fname, calc, *, args=(), kwargs={},
            dir=None, force=True, extend=False, readonly=False,
            readwriter = ReadWriteObjects()):
    '''another version of read_or_calc_xwrite

args and kwargs should be version or algorithm info about calc

dir::None|str - home directory ==>> path = join(dir, fname)
force::bool - when open file to write, using 'x' or 'w'
extend::bool - return value or (value, args, kwargs)
readonly::bool - try_read_or_calc_xwrite or read
calc, args, kwargs - value = calc(*args, **kwargs)


## implement:
if dir is None:
    dir = read_ex_home
    # so, we can set a default home # see set_read_ex_home
path = dir+fname

if not readonly:
    (args, kwargs, value) = _read(path)
    if path not exist or (args, kwargs) not match:
        # update file
        recalc the result
        if file exists and not force:
            raise ...
        write (args, kwargs, value) to file
else:
    (args, kwargs, value) = _read(path)
if extend:
    return args, kwargs, value
else:
    return value
'''
    if dir is None:
        dir = set_read_ex_home()
    args, kwargs = std_args_kwargs(args, kwargs)
    _read_ex = readwriter.iread_path_ex
    _write = readwriter.write_path
    _join = readwriter.join # os.path.join
    _exists = readwriter.exists # os.path.exists

    path = _join(dir, fname)
    if not readonly:
        if (args, kwargs) != (args, kwargs):
            raise TypeError('(args, kwargs) != (args, kwargs)')
        
        #isfile = os.path.isfile(path) # not dir; what about link??
        exists = _exists(path)
        recalc = True
        if exists:
            # (L, _args, _kwargs, _value) = _read_ex(path)
            
            it = _read_ex(path, check_len=3, yield_len=False)
            [_args, _kwargs], it = takeN_ex(it, 2)
            
            if (_args, _kwargs) == (args, kwargs):
                recalc = False
                _value, = it
            else:
                del _args, _kwargs
        if recalc:
            if exists and not force:
                raise FileExistsError('file and not force to write')
            value = calc(*args, **kwargs)
            _write(path, force, (args, kwargs, value))
            (_L, _args, _kwargs, _value) = _read_ex(path)
            if not (_L, _args, _kwargs) == (3, args, kwargs):
                raise TypeError('data != data_read_back')

            # _value != value # maynot eq
        (_args, _kwargs, _value)
    else:
        (_L, _args, _kwargs, _value) = _read_ex(path)


    if extend:
        return (_args, _kwargs, _value)
    else:
        return _value
        

def _test_read_ex():
    rw = Bytes_RWObjs()
    path = 'xxx'
    result = 'result'
    class T:
        def __init__(self):
            self.called = False
        def __call__(self, *args, **kwargs):
            if self.called:
                raise test-fail
            self.called = True
            return result
    assert result == read_ex(path, lambda : result, readwriter=rw)
    
    calc = T()
    assert result == read_ex(path, calc, readwriter=rw)
    assert not calc.called
    
    rw = Bytes_RWObjs()
    assert result == read_ex(path, calc, readwriter=rw)
    assert calc.called
    assert result == read_ex(path, calc, readwriter=rw)
    
    rw = Bytes_RWObjs(0)
    calc = T()
    assert result == read_ex(path, calc, readwriter=rw,
                             args=(1,2,3,4), kwargs={'1':'2', '3':'4', '5':'6'})
    #print(rw.abspath2file)
#if __main__ == __name__:
_test_read_ex()
    
    

    
