import ctypes as c
PyDLL = c.pythonapi
from ctypes import addressof, cast, c_void_p, py_object, c_int, \
     pointer, sizeof, alignment, c_char_p, POINTER, c_char, string_at,\
     create_string_buffer, pythonapi


import io
bio=io.BytesIO()
bbuf=bio.getbuffer()
assert type(bbuf) is memoryview
# addressof(bbuf) TypeError: invalid type
# print(dir(bbuf))
assert int.from_bytes(bbuf, 'big') == 0
##class T:
##    def __memoryview__(self):
##        raise
##    def __view__(self):
##        raise
##memoryview(T())
# TypeError: memoryview: T object does not have the buffer interface
# should implement buffer interface at C layer????


ptr = c.pointer
py_p = c.py_object
pbuf = py_p(bbuf)
assert pbuf.value is bbuf
addr = id(bbuf)
assert hex(addr)[2:] in repr(bbuf).lower()
#print(bbuf, *map(hex, [addr, id(pbuf), id(bbuf)]))
cbuf = cast(c_void_p(id(bbuf)), py_object).value
assert cbuf is bbuf



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
def ptr2addr(ptr):
    return addressof(ptr.contents) # &*p


i = c_int(345)
p = pointer(i)
pp = pointer(p)
addrofptr = addressof(p)
#print(i, p, pp, pointer(pp))
#print(i, hex(id(i)), p.contents, pp.contents, hex(addrofptr))
assert pp.contents != p # NOT EQ !!!!
assert p.contents != i # NOT EQ !!!!
assert repr(p.contents) == repr(i)
assert addressof(pp.contents) == addrofptr

def addrofaddr2addr(addrofptr):
    voidp = c_void_p.from_address(addrofptr)
    return voidp.value
    pp = c_void_p(addrofptr)
addrofptr2ptrvalue = addrofaddr2addr
assert addrofptr2ptrvalue(addrofptr) == addressof(p.contents)
assert addrofptr2ptrvalue(addressof(p)) == addressof(p.contents) == ptr2addr(p)

buf = create_string_buffer(b'afafaf')
#print(buf)
#print(addressof(buf), string_at(addressof(buf)))

pbuf = c_char_p(addressof(buf))
addr_of_pbuf = addressof(pbuf)
#print(addrofptr2ptrvalue(addr_of_pbuf), addressof(buf))
assert addrofptr2ptrvalue(addr_of_pbuf) == addressof(buf)

pbuf_in_bytes = create_string_buffer(string_at(addressof(pbuf), sizeof(pbuf)))



def find_out_offset_of_tp_name_in_PyTypeObject(max=128):
    step = alignment(c_void_p)
    #print(step, sizeof(c_void_p))
    name = '_00_01_'
    T = type(name, (), {})
    addr = pyobj2pyaddr(T) # a type object not instance!!
    name = name.encode('utf-8')
    null_ptr = POINTER(c_char_p)()
    assert not null_ptr
    assert null_ptr != POINTER(c_char_p)() # why !!!!!!!!!!!!!
    #no contents:  assert null_ptr.contents != POINTER(c_char_p)().contents
    for offset in range(0, max+1, step):
        addr_of_ty_name_addr = addr + offset
        ty_name_addr = addrofaddr2addr(addr_of_ty_name_addr)
        if ty_name_addr is None:
            continue

        try:
            ty_name = string_at(ty_name_addr, 1)
            # assert type(ty_name) is bytes
            #print(ty_name, name)
            if name.startswith(ty_name):
                ty_name = string_at(ty_name_addr, len(name))
                if name == ty_name:
                    break
        except OSError:
            continue
    else:
        raise logic-error
    return offset


offset_of_tp_name = find_out_offset_of_tp_name_in_PyTypeObject()
print(offset_of_tp_name)

