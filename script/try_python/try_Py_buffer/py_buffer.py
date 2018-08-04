
r'''
struct Py_buffer {
    void *obj 
    void *buf 
    Py_ssize_t len
    int readonly
    Py_ssize_t itemsize
    const char *format 
    int ndim
    Py_ssize_t *shape 
    Py_ssize_t *strides 
    Py_ssize_t *suboffsets 
    void *internal 
}

struct PyTypeObject {
    PyObject_VAR_HEAD
    char *tp_name; # offset ~24
    ...
    PyBufferProcs *tp_as_buffer; # offset ~160
    ...
}

struct PyBufferProcs {
    # getbufferproc bf_getbuffer
    int (*bf_getbuffer)(PyObject *exporter, Py_buffer *view, int flags);
    # releasebufferproc bf_releasebuffer
    void (*bf_releasebuffer)(PyObject *exporter, Py_buffer *view);
}
'''

    
r'''
fundamental c type:
    someCBuiltinTypeObj.value
    but what about function_ptr?? void(*)(void)??
        CFUNCTYPE(c_int, argtypes...) or ...
pointer
# ptr type: (T*) ==>> POINTER(someCType)
# ctypes.py_object for (PyObject *)
    deref ==>> py_obj.value
# dereference :
    # not have OOR (original object return)
    # assert ptr.contents is not ptr.contents
    # but ptr.contents = xx # assignment is correct!
    T(*p) ==>> ptr.contents 
        or c_xx_p ==>> ptr.value
    p[x]  ==>> ptr[x]
# addressof : p = &t ==>>
    ptr = pointer(someCTypeObj)
    or ptr.contents = someCTypeObj
    or ptr = POINTER(type(someCTypeObj)).from_address(addressof(someCTypeObj))
    
    or byref(someCTypeObj) # byref(someCTypeObj, byteoffset)
    # result of byref can only be used as a foreign function call parameter.
    # It behaves similar to pointer(obj), but the construction is a lot faster.

    how??? bytes to its string address??

# NULL member : t.p = NULL ==>> someCTypeObj.somePtrMember = None
# cast : a = (A)t ==>> anotherCTypeObj = cast(someCTypeObj, anotherCType)
    how??? obj -> pyaddr -> obj
    pyaddr = id(obj)
    obj = cast(c_void_p(pyaddr), py_object).value
create_string_buffer:
    char[size] ==>> c_char * size

function prototype:
    1) make a type|API|prototype:
        API.argtypes
        API.restype # Use None for void
    2) make a function
        API(...)
DLL
# ctypes.pythonapi # the PyDLL
# obj = dll.static_obj ==>> someCTypeObj = someCType.in_dll(someDll, objName)
'''
import struct
import ctypes
import sys


from ctypes import addressof, cast, c_void_p, py_object, c_int, \
     pointer, sizeof, alignment, c_char_p, POINTER, c_char, string_at,\
     create_string_buffer, pythonapi, CFUNCTYPE, WINFUNCTYPE, c_ssize_t,\
     c_long
#sizeof(CFUNCTYPE) TypeError: this type has no size



c_void_result = None
PyObject_p = py_object
#PyObject_p = c_void_p
Py_ssize_t = c_ssize_t
Py_ssize_t_p = POINTER(Py_ssize_t)
class Py_buffer(ctypes.Structure):
    #_anonymous_ = ()
    _fields_ = [("obj", c_void_p),
                ("buf", c_void_p),
                ("len", Py_ssize_t),
                ("readonly", c_int),
                ("itemsize", Py_ssize_t),
                ("format", c_char_p),
                ("ndim", c_int),
                # follow 3 members are all (Py_ssize_t *)
                ("shape", Py_ssize_t_p),
                ("strides", Py_ssize_t_p),
                ("suboffsets", Py_ssize_t_p),
                ("internal", c_void_p)]
Py_buffer_p = POINTER(Py_buffer) # byref(Py_buffer_obj)???????

c_getbufferproc_func_p = CFUNCTYPE(c_int, PyObject_p, Py_buffer_p, c_int)
c_releasebufferproc_func_p = CFUNCTYPE(c_void_result, PyObject_p, Py_buffer_p)

class PyBufferProcs(ctypes.Structure):
    _fields_ = [("bf_getbuffer", c_getbufferproc_func_p),
                ("bf_releasebuffer", c_releasebufferproc_func_p)]

PyBufferProcs_p = POINTER(PyBufferProcs)



def pyobj2pyaddr(pyobj):
    return id(pyobj)
def pyaddr2pyvoidp(pyaddr):
    return c_void_p(pyaddr)
def pyvoidp2pyobj(pyvoidp):
    return cast(pyvoidp, py_object).value
def pyvoidp2pyaddr(pyvoidp):
    return pyvoidp.contents

def pyobj2pyvoidp(pyobj):
    return pyaddr2pyvoidp(pyobj2pyaddr(pyobj))
def pyaddr2pyobj(pyaddr):
    return pyvoidp2pyobj(pyaddr2pyvoidp(pyaddr))

_byteorder = sys.byteorder
def buffer2uint(buffer):
    return int.from_bytes(memoryview(buffer), _byteorder)
def _1_ptr2addr(ptr):
    return buffer2uint(ptr)
def _2_ptr2addr(ptr):
    tname = type(ptr).__name__
    if tname.startswith('c_'):
        if tname.endswith('_p'):
            # fundamental
            return ptr.value
    return addressof(ptr.contents) # &*p
def ptr2addr(ptr):
    a = _1_ptr2addr(ptr)
    try:
        b = _2_ptr2addr(ptr)
    except:
        raise logic-error
        return a
    assert a == b
    return a




def addrofaddr2addr(addrofptr):
    '''*pp <==> int(pp)->int(p)

input: int(pp)
output: int(p)
p = c_void_p.from_address(int(pp))
int(p) = p.value

return None if input is addr of null_ptr
raise ValueError if input is None / null addr
'''
    if addrofptr is None:
        raise ValueError('input null addr : addrofptr == None')
    voidp = c_void_p.from_address(addrofptr)
    return voidp.value # may be None


# CFUNCTYPE()() has no "value"!!!
_c_func_void_void_p = CFUNCTYPE(None) # this is a type like c_void_p
_null_func = _c_func_void_void_p()
_null_func_addr = buffer2uint(_null_func)
#print(dir(_null_func), _null_func_addr, addressof(_null_func))
def addroffuncaddr2funcaddr(addroffuncaddr):
    f = _c_func_void_void_p(addroffuncaddr)
    if not f:
        return None
    
    bs = string_at(addroffuncaddr, sizeof(_null_func))
    funcaddr = buffer2uint(bs)
    xx = None if funcaddr == _null_func_addr else funcaddr
    return xx





def find_out_offset_of_tp_name_in_PyTypeObject(max=1280):
    name = '_00_01_'
    T = type(name, (), {})
    addr = pyobj2pyaddr(T) # a type object not instance!!
    name = name.encode('utf-8')
    null_ptr = POINTER(c_char_p)()
    assert not null_ptr
    assert null_ptr != POINTER(c_char_p)() # why !!!!!!!!!!!!!
    #no contents:  assert null_ptr.contents != POINTER(c_char_p)().contents
    step = alignment(c_void_p)
    #print(step, sizeof(c_void_p))
    for offset in range(0, max+1, step):
        addr_of_tp_name_addr = addr + offset
        tp_name_addr = addrofaddr2addr(addr_of_tp_name_addr)
        if tp_name_addr is None:
            continue

        try:
            tp_name = string_at(tp_name_addr, 1)
            # assert type(tp_name) is bytes
            #print(tp_name, name)
            if name.startswith(tp_name):
                tp_name = string_at(tp_name_addr, len(name))
                if name == tp_name:
                    break
        except OSError:
            continue
    else:
        raise logic-error
    return offset


sizeof_PyObject_VAR_HEAD = \
        offset_of_tp_name = \
        find_out_offset_of_tp_name_in_PyTypeObject()


def check_type(cls):
    if not isinstance(cls, type):
        raise TypeError
    
def get_tp_name(cls):
    check_type(cls)
    addr_of_tp_name_addr = to_member_addr(cls, offset_of_tp_name)
    tp_name_addr = addrofaddr2addr(addr_of_tp_name_addr)
    return string_at(tp_name_addr).decode('utf-8')

def to_member_addr(obj, offset):
    addr = pyobj2pyaddr(obj)
    return addr + offset


def find_out_offset_of_tp_as_buffer_in_PyTypeObject(
    buffer, notbuffer, max=1280, offset_of_tp_name=offset_of_tp_name):
    memoryview(buffer)
    try:
        memoryview(notbuffer)
    except TypeError:
        pass
    else:
        raise TypeError('memoryview(notbuffer) pass!')
    T1 = type(buffer)
    T2 = type(notbuffer)
    addr1 = pyobj2pyaddr(T1)
    addr2 = pyobj2pyaddr(T2)

    
    step = alignment(_c_func_void_void_p)
    #print(step, sizeof(_c_func_void_void_p))
    for offset in range(offset_of_tp_name, max+1, step):
        addr_of_tp_as_buffer_addr1 = addr1 + offset
        addr_of_tp_as_buffer_addr2 = addr2 + offset
        tp_as_buffer_addr1 = addrofaddr2addr(addr_of_tp_as_buffer_addr1)
        tp_as_buffer_addr2 = addrofaddr2addr(addr_of_tp_as_buffer_addr2)
        if tp_as_buffer_addr1 is None: # ==xx==>> is buffer
            continue
        if tp_as_buffer_addr2 is not None: # ==xx==>> not buffer
            continue
        try:
            string_at(tp_as_buffer_addr1, sizeof(PyBufferProcs))
            tp_as_buffer1 = PyBufferProcs.from_address(tp_as_buffer_addr1)
            
            if not tp_as_buffer1.bf_getbuffer or \
               not tp_as_buffer1.bf_releasebuffer:
                continue
            
        except OSError:
            continue

        #print(offset, tp_as_buffer_addr1)
        # it seems 160 is correct
        return offset # the first one meets above conditions
    raise logic-error
        
    

offset_of_tp_as_buffer = find_out_offset_of_tp_as_buffer_in_PyTypeObject(b'', '')






class _PyTypeObject__part1(ctypes.Structure):
    # AttributeError: type object 'c_char_Array_24' has no attribute '_fields_'
    # bug : _anonymous_ = ('PyObject_VAR_HEAD', '_1')
    # _anonymous_ is not padding!!!
    _fields_ = [("PyObject_VAR_HEAD", c_char * offset_of_tp_name),
                ("tp_name", c_char_p),
                ("_1", c_char * (offset_of_tp_as_buffer
                                 -sizeof(c_char_p)
                                 -offset_of_tp_name)),
                ("tp_as_buffer", PyBufferProcs_p),
                ("tp_flags", c_long)]


def to_PyTypeObject__part1(cls):
    check_type(cls)
    return _PyTypeObject__part1.from_address(id(cls))

def get_tp_flags(T):
    return to_PyTypeObject__part1(T).tp_flags
def set_tp_flags(T, f):
    to_PyTypeObject__part1(T).tp_flags = f
    
def xor_tp_flags(T1, T2):
    f1, f2 = map(get_tp_flags, [T1, T2])
    return f1 ^ f2
print(bin(xor_tp_flags(str, bytes)))


def is_buffer(buf):
    try:
        memoryview(buf)
    except TypeError as e:
        print(e)
        return False
    return True
def is_buffer_type(T):
    check_type(T)
    return is_buffer(T())


if 0:
    import array, operator as op, itertools as itt, functools as fts
    class AA(array.array):
        def __new__(cls):
            return super().__new__(cls, 'B')
            
    buffer_types = [bytes, bytearray, AA, c_void_p, c_long, _c_func_void_void_p]
    nonbuffer_types = [str, list, tuple, int, float, dict, set]
    #print(*filter(is_buffer_type, buffer_types))
    assert all(map(is_buffer_type, buffer_types))
    assert not any(map(is_buffer_type, nonbuffer_types))
    *bfs, = map(get_tp_flags, buffer_types)
    *nbfs, = map(get_tp_flags, nonbuffer_types)
    mask = ((1<<(sizeof(c_long)*8))-1)
    contained_buffer_flag = fts.reduce(op.and_, bfs) | ~fts.reduce(op.or_, bfs)
    not_contained_buffer_flag = fts.reduce(op.and_, nbfs) | ~fts.reduce(op.or_, nbfs)
    # if set buffer_flag is 1
    buffer_flag1_in = fts.reduce(op.and_, bfs) &~ fts.reduce(op.and_, nbfs)
    buffer_flag0_in = fts.reduce(op.or_, bfs) |(~ fts.reduce(op.or_, nbfs))  & mask
    print(*map(bin, [buffer_flag1_in, buffer_flag0_in]))


    print(bin(fts.reduce(op.and_, bfs)))
    print(bin(contained_buffer_flag & mask))

    class B(bytes):pass
    assert is_buffer(B())
    

str__tp_as_buffer = to_PyTypeObject__part1(str).tp_as_buffer
#print(str__tp_as_buffer, str__tp_as_buffer.contents)
assert not str__tp_as_buffer
class BufferWrapperMeta(type):
    def __new__(cls, name, bases, namespace, **kwds):
        self = type.__new__(cls, name, bases, dict(namespace))
        if self.__name__ != name or get_tp_name(self) != name:
            raise logic-error
        # self is the BufferWrapperClass
        # patch it's tp_as_buffer
        CT_self = to_PyTypeObject__part1(self)
        if CT_self.tp_name != name.encode('utf-8'):
            raise logic-error

        if CT_self.tp_as_buffer:
            raise TypeError('self should not be a buffer!!')


        tp_as_buffer = self.make_PyBufferProcs_p() # pointer(PyBufferProcs)
        if type(tp_as_buffer) is not PyBufferProcs_p:
            raise TypeError('self.make_PyBufferProcs_p() not result PyBufferProcs_p')
        if not tp_as_buffer:
            raise ValueError('tp_as_buffer should not be NULL ptr')
        CT_self.tp_as_buffer = tp_as_buffer


        tbuf = to_PyTypeObject__part1(self).tp_as_buffer
        if not (tbuf and
                tbuf.contents.bf_getbuffer and
                tbuf.contents.bf_releasebuffer):
            raise logic-error
        return self

def make_PyBufferProcs(get, rel):
    r = PyBufferProcs() # should hold a ref
    r.bf_getbuffer = type(r.bf_getbuffer)(get)
    r.bf_releasebuffer = type(r.bf_releasebuffer)(rel)
    return r

def try_set_tp_as_buffer(cls):
    check_type(cls)
    
    def get(e, v, f):
        ref
        print('g')
    def rel(e, v):
        ref
        print('r')

    ref = make_PyBufferProcs(get, rel)
    to_PyTypeObject__part1(cls).tp_as_buffer.contents = ref


class U(bytes):pass

try_set_tp_as_buffer(U)
assert is_buffer(U())

#to_PyTypeObject__part1(U).tp_as_buffer.contents.bf_getbuffer(1, None, 1)
org_tp_flags = get_tp_flags(U)
print(org_tp_flags)
f = 1 << 32
f -= 1
while f > 1:
    f >>= 1
    set_tp_flags(U, f | org_tp_flags)
    print(f | org_tp_flags, get_tp_flags(U), org_tp_flags)
    #assert f | org_tp_flags == get_tp_flags(U) != org_tp_flags
    if is_buffer(U()):
        break
    
    

assert is_buffer(U())
raise 
    
class BufferWrapperBase(metaclass=BufferWrapperMeta):
    '''

>>> BufferWrapperBase('')
Traceback (most recent call last):
...
TypeError: not buffer
>>> x = BufferWrapperBase(b'')
>>> m = memoryview(x)
'''
    def __getbuffer(self, view:'Py_buffer_p', flags:int):
        'return int'
        print('__getbuffer')
        exporter = self.__buf
        APIs = self.__APIs
        return type(self).__getbuffer__(
            self, APIs.bf_getbuffer, exporter, view, flags)
    def __releasebuffer(self, view):
        'return None'
        exporter = self.__buf
        APIs = self.__APIs
        return type(self).__releasebuffer__(
            self, APIs.bf_releasebuffer, exporter, view)


    @property
    def __APIs(self):
        exporter = self.__buf
        CT_exporter = to_PyTypeObject__part1(type(exporter))
        APIs = CT_exporter.tp_as_buffer.contents
        return APIs
        
    @classmethod
    def make_PyBufferProcs_p(cls):
##        r = PyBufferProcs(cls.__getbuffer, cls.__releasebuffer)
##        return pointer(r)
        r = cls.__ref__buf_protocol = PyBufferProcs() # should hold a ref
        r.bf_getbuffer = type(r.bf_getbuffer)(cls.__getbuffer)
        r.bf_releasebuffer = type(r.bf_releasebuffer)(cls.__releasebuffer)
        return pointer(r)
    def __new__(cls, buffer):
        CT_exporter = to_PyTypeObject__part1(type(buffer))
        if not CT_exporter.tp_as_buffer:
            raise TypeError('not buffer')
##        if type(buffer) is not cls.buffer_type:
##            raise TypeError
        self = super(__class__, cls).__new__(cls)
        self.__buf = buffer
        return self

        
    def __getbuffer__(self, bf_getbuffer, exporter, view:'Py_buffer_p', flags):
        'return int'
        print('__getbuffer__')
        return bf_getbuffer(exporter, view, flags)
    def __releasebuffer__(self, bf_releasebuffer, exporter, view):
        'return None'
        return bf_releasebuffer(exporter, view)
        

x = BufferWrapperBase(b'')
assert to_PyTypeObject__part1(BufferWrapperBase).tp_as_buffer.contents.bf_getbuffer
assert to_PyTypeObject__part1(BufferWrapperBase).tp_as_buffer.contents.bf_releasebuffer
assert is_buffer(x)
m = memoryview(x)

if __name__ == "__main__":
    import doctest
    doctest.testmod()


if 0:
    Py_buffer_struct_fmt_fmt = ('PP{Py_ssize_t}i{Py_ssize_t}si'
                      '{Py_ssize_t}{Py_ssize_t}{Py_ssize_t}P')

    # PyObject* PyLong_FromSsize_t(Py_ssize_t v) 
    # Return a new PyLongObject object from a C Py_ssize_t, or NULL on failure.
    Py_ssize_t__possibles = 'BHILQN'
    Py_ssize_t__possibles = 'NLIQHB'.lower()

    for Py_ssize_t_fmt in Py_ssize_t__possibles:
        Py_buffer_struct_fmt = Py_buffer_struct_fmt_fmt.format(
            Py_ssize_t=Py_ssize_t_fmt)
        Py_buffer_struct = struct.Struct(Py_buffer_struct_fmt)
        








